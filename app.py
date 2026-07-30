# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# COMPLETE BULLETPROOF SCRIPT
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

            # Determine correct mime type dynamically (.jpg vs .png)
            mime_type, _ = mimetypes.guess_type(image_path)
            mime_type = mime_type or "image/jpeg"

            with open(image_path, "rb") as img:
                encoded_image = base64.b64encode(img.read()).decode()
                # Store as full data URI string
                BACKGROUND_IMAGES.append(
                    f"data:{mime_type};base64,{encoded_image}"
                )
            print("✅ Loaded:", file)
else:
    print("❌ 'images' folder not found")

print("Total Images Loaded:", len(BACKGROUND_IMAGES))

# Fallback dummy image if no folder/images exist
if len(BACKGROUND_IMAGES) == 0:
    # 1x1 transparent PNG pixel as default fallback to avoid startup crash
    fallback_uri = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
    BACKGROUND_IMAGES = [fallback_uri] * 5

# Ensure minimum 5 images for CSS 5-stage keyframes
while len(BACKGROUND_IMAGES) < 5:
    BACKGROUND_IMAGES.append(BACKGROUND_IMAGES[0])

# ==========================================================
# PART 2: BACKGROUND SLIDESHOW CSS
# ==========================================================

css = f"""
.gradio-container {{
    min-height: 100vh !important;
    width: 100% !important;
    background: transparent !important;
}}

.gradio-container::before {{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    animation: backgroundChange 120s infinite;
}}

@keyframes backgroundChange {{
    0%, 100% {{ background-image: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), url("{BACKGROUND_IMAGES[0]}"); }}
    20% {{ background-image: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), url("{BACKGROUND_IMAGES[1]}"); }}
    40% {{ background-image: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), url("{BACKGROUND_IMAGES[2]}"); }}
    60% {{ background-image: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), url("{BACKGROUND_IMAGES[3]}"); }}
    80% {{ background-image: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), url("{BACKGROUND_IMAGES[4]}"); }}
}}

.block, .panel, .form, fieldset {{
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}}

h1, h2, h3, p, label, span {{
    color: white !important;
    text-shadow: 2px 2px 8px black !important;
}}

button {{
    background: linear-gradient(135deg, #00c853, #00e676) !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 15px !important;
}}

input, textarea, select {{
    background: rgba(255, 255, 255, 0.85) !important;
    color: black !important;
    border-radius: 12px !important;
}}

footer {{
    display: none !important;
}}
"""

# ==========================================================
# PART 5: PREPROCESSING & PREDICTION
# ==========================================================


def preprocess_input(df):
    df = df.copy()

    # Fixed Dictionary Mappings
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

    # Convert remaining non-numeric columns using hash-based encoding or numeric conversion
    for col in df.columns:
        if df[col].dtype == "object":
            # Simple numeric hash fallback to avoid all strings becoming 0
            df[col] = df[col].apply(
                lambda x: abs(hash(str(x))) % 1000 if pd.notna(x) else 0
            )

    df = df.fillna(0)

    # Align columns with model feature names if available
    if model is not None and hasattr(model, "feature_names_in_"):
        expected_cols = model.feature_names_in_
        # Reorder and add any missing expected columns
        for col in expected_cols:
            if col not in df.columns:
                df[col] = 0
        df = df[expected_cols]

    return df


def predict_admission(data):
    try:
        if model is None:
            return "❌ Model not loaded", 0

        processed_data = preprocess_input(data)
        prediction = model.predict(processed_data)[0]

        # Get probability safely
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
                f"🎉 Admission Approved\n\nProbability: {probability}%"
            )
        else:
            message = f"❌ Admission Not Approved\n\nProbability: {probability}%"

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


def toggle_section(current_state):
    return gr.update(visible=not current_state)


# ==========================================================
# PART 3 & 4: GRADIO INTERFACE
# ==========================================================

with gr.Blocks(css=css, title="AI College Admission Approval System") as demo:

    gr.HTML(
        """
        <div id="title" style="text-align: center; margin-bottom: 20px;">
            <h1 style="font-size: 32px;">🎓 AI College Admission Approval System</h1>
            <span style="font-size: 22px;">Smart AI Based College Admission Prediction</span><br>
            <span style="font-size: 16px;">Developed by Manya</span>
        </div>
        """
    )

    gr.Markdown("### 👇 Click the sections below to enter student details")

    # SECTION BUTTONS
    with gr.Row():
        academic_btn = gr.Button("📚 Academic Details")
        entrance_btn = gr.Button("🎯 Entrance Exam")
        college_btn = gr.Button("🏫 College Preference")

    with gr.Row():
        verification_btn = gr.Button("✅ Verification")
        scholarship_btn = gr.Button("💰 Scholarship")

    # SECTIONS WITH TOGGLES
    with gr.Group(visible=False) as academic_section:
        gr.Markdown("## 📚 Academic Details")
        with gr.Row():
            Age = gr.Number(label="Age", value=18)
            Category = gr.Dropdown(
                choices=["General", "OBC", "SC", "ST"],
                label="Category",
                value="General",
            )
            Family_Income = gr.Number(label="Family Income", value=500000)
        with gr.Row():
            Class10 = gr.Number(label="Class 10 Percentage", value=85)
            Class12 = gr.Number(label="Class 12 Percentage", value=85)
            PCM = gr.Number(label="PCM Percentage", value=85)
        with gr.Row():
            Graduation = gr.Textbox(
                label="Previous Qualification", value="High School"
            )
            Backlogs = gr.Number(label="Number of Backlogs", value=0)

    with gr.Group(visible=False) as entrance_section:
        gr.Markdown("## 🎯 Entrance Exam Details")
        with gr.Row():
            Exam_Name = gr.Textbox(label="Entrance Exam Name", value="JEE Main")
            Exam_Score = gr.Number(label="Entrance Score", value=180)
            Rank = gr.Number(label="Entrance Rank", value=15000)
        with gr.Row():
            Percentile = gr.Number(label="Percentile", value=95.0)
            Attempts = gr.Number(label="Number of Attempts", value=1)

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

    with gr.Group(visible=False) as verification_section:
        gr.Markdown("## ✅ Verification Details")
        with gr.Row():
            Documents = gr.Dropdown(
                choices=["Verified", "Not Verified"],
                label="Documents Status",
                value="Verified",
            )
            Interview_Score = gr.Number(label="Interview Score", value=8)
            Communication = gr.Number(label="Communication Skill", value=8)

    with gr.Group(visible=False) as scholarship_section:
        gr.Markdown("## 💰 Scholarship Details")
        with gr.Row():
            Scholarship = gr.Dropdown(
                choices=["Yes", "No"], label="Scholarship Required", value="No"
            )
            Family_Status = gr.Textbox(
                label="Family Status", value="Middle Class"
            )
            Fee_Budget = gr.Number(label="Fee Budget", value=200000)

    # OUTPUT REGION
    gr.Markdown("## 🚀 Final Admission Prediction")
    predict_button = gr.Button("🚀 Predict Admission", variant="primary")

    result = gr.Textbox(label="Prediction Result", lines=3)
    probability = gr.Slider(
        minimum=0, maximum=100, value=0, label="📊 Admission Probability (%)"
    )

    # TOGGLE EVENTS
    academic_btn.click(
        fn=lambda: gr.update(visible=True),
        outputs=academic_section,
    )
    entrance_btn.click(
        fn=lambda: gr.update(visible=True),
        outputs=entrance_section,
    )
    college_btn.click(
        fn=lambda: gr.update(visible=True),
        outputs=college_section,
    )
    verification_btn.click(
        fn=lambda: gr.update(visible=True),
        outputs=verification_section,
    )
    scholarship_btn.click(
        fn=lambda: gr.update(visible=True),
        outputs=scholarship_section,
    )

    # PREDICTION EVENT
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
# PART 6: LAUNCH
# ==========================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port, show_error=True)
