# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# ALL 25 INPUT FIELDS + HIGH-VISIBILITY BACKGROUND SLIDESHOW
# ==========================================================

import base64
import mimetypes
import os
import gradio as gr
import joblib
import pandas as pd

# ==========================================================
# PART 1: MODEL & IMAGE LOADING
# ==========================================================

MODEL_PATH = "admission_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
    print("✅ Model Loaded Successfully")
except Exception as e:
    print("❌ Model Loading Error:", e)
    model = None

IMAGE_FOLDER = "images"
BACKGROUND_IMAGES = []

if os.path.exists(IMAGE_FOLDER):
    print("\nImages Found:")
    for file in os.listdir(IMAGE_FOLDER):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(IMAGE_FOLDER, file)

            mime_type, _ = mimetypes.guess_type(image_path)
            mime_type = mime_type or "image/jpeg"

            with open(image_path, "rb") as img:
                encoded_image = base64.b64encode(img.read()).decode()
                BACKGROUND_IMAGES.append(
                    f"data:{mime_type};base64,{encoded_image}"
                )
            print("✅ Loaded:", file)
else:
    print("❌ 'images' folder not found")

# Fallback online high-res images if no local images exist
if len(BACKGROUND_IMAGES) == 0:
    BACKGROUND_IMAGES = [
        "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=1600",
        "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=1600",
        "https://images.unsplash.com/photo-1562774053-701939374585?q=80&w=1600",
        "https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?q=80&w=1600",
        "https://images.unsplash.com/photo-1523240795612-9a054b0db644?q=80&w=1600",
    ]

# Ensure at least 5 images exist for keyframe transitions
while len(BACKGROUND_IMAGES) < 5:
    BACKGROUND_IMAGES.append(BACKGROUND_IMAGES[0])

# ==========================================================
# PART 2: STYLED CSS FOR HIGH VISIBILITY OVER SLIDESHOW
# ==========================================================

css = f"""
/* Fix main page viewport */
.gradio-container {{
    min-height: 100vh !important;
    width: 100% !important;
    background: transparent !important;
    padding: 20px !important;
}}

/* Fixed Background Slideshow Animation */
.gradio-container::before {{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    animation: backgroundChange 25s infinite ease-in-out;
    filter: brightness(0.55); /* Darkened slightly to boost foreground text readability */
}}

@keyframes backgroundChange {{
    0%, 100% {{ background-image: url("{BACKGROUND_IMAGES[0]}"); }}
    20% {{ background-image: url("{BACKGROUND_IMAGES[1]}"); }}
    40% {{ background-image: url("{BACKGROUND_IMAGES[2]}"); }}
    60% {{ background-image: url("{BACKGROUND_IMAGES[3]}"); }}
    80% {{ background-image: url("{BACKGROUND_IMAGES[4]}"); }}
}}

/* Frosted Glass Panels for Form Groups */
.gradio-group {{
    background: rgba(15, 23, 42, 0.75) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 16px !important;
    padding: 20px !important;
    margin-top: 15px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
}}

/* Header & Label Text Readability Enhancement */
h1, h2, h3, h4, p, span {{
    color: #ffffff !important;
    text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.9) !important;
}}

label span {{
    color: #f8fafc !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.9) !important;
}}

/* High Contrast Input Fields */
input, textarea, select {{
    background-color: #ffffff !important;
    color: #0f172a !important;
    font-weight: 500 !important;
    border: 2px solid #94a3b8 !important;
    border-radius: 8px !important;
}}

/* Button Styling */
button.primary {{
    background: linear-gradient(135deg, #10b981, #059669) !important;
    color: #ffffff !important;
    font-weight: bold !important;
    font-size: 16px !important;
    border-radius: 10px !important;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4) !important;
}}

button.secondary {{
    background: rgba(255, 255, 255, 0.15) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255, 255, 255, 0.4) !important;
    backdrop-filter: blur(5px) !important;
    font-weight: 600 !important;
}}

footer {{
    display: none !important;
}}
"""

# ==========================================================
# PART 3: PREPROCESSING & PREDICTION
# ==========================================================


def preprocess_input(df):
    df = df.copy()

    yes_no_map = {"Yes": 1, "No": 0}
    if "Hostel" in df.columns:
        df["Hostel"] = df["Hostel"].map(yes_no_map)
    if "Scholarship" in df.columns:
        df["Scholarship"] = df["Scholarship"].map(yes_no_map)

    category_map = {"General": 0, "OBC": 1, "SC": 2, "ST": 3}
    if "Category" in df.columns:
        df["Category"] = df["Category"].map(category_map)

    college_map = {"Government": 0, "Private": 1}
    if "College_Type" in df.columns:
        df["College_Type"] = df["College_Type"].map(college_map)

    document_map = {"Verified": 1, "Not Verified": 0}
    if "Documents" in df.columns:
        df["Documents"] = df["Documents"].map(document_map)

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].apply(
                lambda x: abs(hash(str(x))) % 1000 if pd.notna(x) else 0
            )

    df = df.fillna(0)

    if model is not None and hasattr(model, "feature_names_in_"):
        expected_cols = model.feature_names_in_
        for col in expected_cols:
            if col not in df.columns:
                df[col] = 0
        df = df[expected_cols]

    return df


def predict_admission(data):
    try:
        if model is None:
            return "❌ Model file not found.", 0

        processed_data = preprocess_input(data)
        prediction = model.predict(processed_data)[0]

        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(processed_data)[0]
            probability = (
                round(probs[1] * 100, 2)
                if len(probs) > 1
                else round(probs[0] * 100, 2)
            )
        else:
            probability = 85.0 if prediction == 1 else 25.0

        if prediction == 1:
            message = (
                f"🎉 Admission Approved!\n\nEstimated Probability: {probability}%"
            )
        else:
            message = f"❌ Admission Not Approved.\n\nEstimated Probability: {probability}%"

        return message, probability

    except Exception as e:
        return f"❌ Prediction Failed: {str(e)}", 0


def final_prediction(
    Age,
    Category,
    Family_Income,
    Class10,
    Class12,
    PCM,
    Graduation,
    Backlogs,
    Exam_Name,
    Exam_Score,
    Rank,
    Percentile,
    Attempts,
    Preferred_College,
    Preferred_Branch,
    College_Type,
    College_Rank,
    Hostel,
    Location,
    Documents,
    Interview_Score,
    Communication,
    Scholarship,
    Family_Status,
    Fee_Budget,
):
    input_data = pd.DataFrame(
        [
            {
                "Age": Age,
                "Category": Category,
                "Family_Income": Family_Income,
                "Class10": Class10,
                "Class12": Class12,
                "PCM": PCM,
                "Graduation": Graduation,
                "Backlogs": Backlogs,
                "Exam_Name": Exam_Name,
                "Exam_Score": Exam_Score,
                "Rank": Rank,
                "Percentile": Percentile,
                "Attempts": Attempts,
                "Preferred_College": Preferred_College,
                "Preferred_Branch": Preferred_Branch,
                "College_Type": College_Type,
                "College_Rank": College_Rank,
                "Hostel": Hostel,
                "Location": Location,
                "Documents": Documents,
                "Interview_Score": Interview_Score,
                "Communication": Communication,
                "Scholarship": Scholarship,
                "Family_Status": Family_Status,
                "Fee_Budget": Fee_Budget,
            }
        ]
    )

    return predict_admission(input_data)


# ==========================================================
# PART 4: GRADIO USER INTERFACE
# ==========================================================

with gr.Blocks(css=css, title="AI College Admission Approval System") as demo:

    gr.HTML(
        """
        <div style="text-align: center; margin-bottom: 25px;">
            <h1 style="font-size: 34px; font-weight: 800;">🎓 AI College Admission Approval System</h1>
            <p style="font-size: 18px; color: #e2e8f0;">Smart AI-Based College Admission Prediction Platform</p>
        </div>
        """
    )

    gr.Markdown("### 👇 Click the sections below to open and edit student details")

    # SECTION NAVIGATION BUTTONS
    with gr.Row():
        academic_btn = gr.Button("📚 Academic Details", variant="secondary")
        entrance_btn = gr.Button("🎯 Entrance Exam", variant="secondary")
        college_btn = gr.Button("🏫 College Preference", variant="secondary")

    with gr.Row():
        verification_btn = gr.Button("✅ Verification", variant="secondary")
        scholarship_btn = gr.Button("💰 Scholarship", variant="secondary")

    # SECTION 1: ACADEMICS
    with gr.Group(visible=True) as academic_section:
        gr.Markdown("## 📚 Academic Details")
        with gr.Row():
            Age = gr.Number(label="Age", value=18)
            Category = gr.Dropdown(
                choices=["General", "OBC", "SC", "ST"],
                label="Category",
                value="General",
            )
            Family_Income = gr.Number(label="Family Income (₹)", value=500000)
        with gr.Row():
            Class10 = gr.Number(label="Class 10 Percentage (%)", value=85)
            Class12 = gr.Number(label="Class 12 Percentage (%)", value=85)
            PCM = gr.Number(label="PCM Percentage (%)", value=85)
        with gr.Row():
            Graduation = gr.Textbox(
                label="Previous Qualification", value="High School"
            )
            Backlogs = gr.Number(label="Number of Backlogs", value=0)

    # SECTION 2: ENTRANCE EXAM
    with gr.Group(visible=False) as entrance_section:
        gr.Markdown("## 🎯 Entrance Exam Details")
        with gr.Row():
            Exam_Name = gr.Textbox(label="Entrance Exam Name", value="JEE Main")
            Exam_Score = gr.Number(label="Entrance Score", value=180)
            Rank = gr.Number(label="Entrance Rank", value=15000)
        with gr.Row():
            Percentile = gr.Number(label="Percentile", value=95.0)
            Attempts = gr.Number(label="Number of Attempts", value=1)

    # SECTION 3: COLLEGE PREFERENCE
    with gr.Group(visible=False) as college_section:
        gr.Markdown("## 🏫 College Preference Details")
        with gr.Row():
            Preferred_College = gr.Textbox(
                label="Preferred College", value="ABC Institute of Tech"
            )
            Preferred_Branch = gr.Textbox(
                label="Preferred Branch", value="Computer Science"
            )
            College_Type = gr.Dropdown(
                choices=["Government", "Private"],
                label="College Type",
                value="Government",
            )
        with gr.Row():
            College_Rank = gr.Number(label="College Rank", value=25)
            Hostel = gr.Dropdown(
                choices=["Yes", "No"], label="Hostel Required", value="Yes"
            )
            Location = gr.Textbox(label="Preferred Location", value="Metro")

    # SECTION 4: VERIFICATION
    with gr.Group(visible=False) as verification_section:
        gr.Markdown("## ✅ Verification Details")
        with gr.Row():
            Documents = gr.Dropdown(
                choices=["Verified", "Not Verified"],
                label="Documents Status",
                value="Verified",
            )
            Interview_Score = gr.Number(
                label="Interview Score (Out of 10)", value=8
            )
            Communication = gr.Number(
                label="Communication Skill (Out of 10)", value=8
            )

    # SECTION 5: SCHOLARSHIP
    with gr.Group(visible=False) as scholarship_section:
        gr.Markdown("## 💰 Scholarship Details")
        with gr.Row():
            Scholarship = gr.Dropdown(
                choices=["Yes", "No"], label="Scholarship Required", value="No"
            )
            Family_Status = gr.Textbox(
                label="Family Status", value="Middle Class"
            )
            Fee_Budget = gr.Number(label="Fee Budget (₹)", value=200000)

    # OUTPUT REGION
    with gr.Group():
        gr.Markdown("## 🚀 Final Admission Prediction")
        predict_button = gr.Button(
            "🚀 Predict Admission Status", variant="primary"
        )

        result = gr.Textbox(label="Prediction Result", lines=3)
        probability = gr.Slider(
            minimum=0,
            maximum=100,
            value=0,
            label="📊 Admission Probability (%)",
        )

    # SECTION TOGGLE EVENTS
    academic_btn.click(
        fn=lambda: gr.update(visible=True), outputs=academic_section
    )
    entrance_btn.click(
        fn=lambda: gr.update(visible=True), outputs=entrance_section
    )
    college_btn.click(
        fn=lambda: gr.update(visible=True), outputs=college_section
    )
    verification_btn.click(
        fn=lambda: gr.update(visible=True), outputs=verification_section
    )
    scholarship_btn.click(
        fn=lambda: gr.update(visible=True), outputs=scholarship_section
    )

    # EXECUTE PREDICTION EVENT
    predict_button.click(
        fn=final_prediction,
        inputs=[
            Age,
            Category,
            Family_Income,
            Class10,
            Class12,
            PCM,
            Graduation,
            Backlogs,
            Exam_Name,
            Exam_Score,
            Rank,
            Percentile,
            Attempts,
            Preferred_College,
            Preferred_Branch,
            College_Type,
            College_Rank,
            Hostel,
            Location,
            Documents,
            Interview_Score,
            Communication,
            Scholarship,
            Family_Status,
            Fee_Budget,
        ],
        outputs=[result, probability],
    )

# ==========================================================
# PART 5: LAUNCH APP
# ==========================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port, show_error=True)
