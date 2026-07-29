# =====================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# PART 1 : IMPORTS + MODEL + IMAGE LOADING + PREDICTION
# =====================================================

import os
import base64
import joblib
import pandas as pd
import gradio as gr

# =====================================================
# LOAD MODEL
# =====================================================

MODEL_PATH = "college_admission_approval.pkl"

try:
    model = joblib.load(MODEL_PATH)
    print("✅ Admission Model Loaded Successfully")
except Exception as e:
    print("❌ Model Loading Error:", e)
    model = None

# =====================================================
# LOAD BACKGROUND IMAGES
# ORDER: 1.jpg → 3.jpg → 4.jpg → 5.jpg → 2.jpg
# =====================================================

def load_background_images():
    image_order = [
        "1.jpg",
        "3.jpg",
        "4.jpg",
        "5.jpg",
        "2.jpg"
    ]
    encoded_images = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    for image in image_order:
        image_path = os.path.join(BASE_DIR, "images", image)
        if os.path.exists(image_path):
            with open(image_path, "rb") as f:
                encoded_images.append(base64.b64encode(f.read()).decode())
        else:
            print("Missing background image:", image_path)

    # Provide a blank placeholder image if files are missing to prevent UI crash
    if not encoded_images:
        placeholder = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
        encoded_images = [placeholder] * 5

    return encoded_images

BACKGROUND_IMAGES = load_background_images()

# Ensure list has exactly 5 slots for the slideshow animation
while len(BACKGROUND_IMAGES) < 5:
    BACKGROUND_IMAGES.append(BACKGROUND_IMAGES[0])

# =====================================================
# PREDICTION FUNCTION
# =====================================================

def predict_admission(
    Age, Category, Family_Income, Class10_Percentage, Class12_Percentage,
    PCM_Percentage, Entrance_Exam, JEE_Percentile, JEE_Rank, CUET_Score,
    Preferred_Branch, Preferred_College, College_Type, NIRF_Rank,
    College_Tier, Branch_Cutoff_Rank, Available_Seats, Reservation_Quota,
    Documents_Verified, Interview_Score, Communication_Score, Aptitude_Score,
    Scholarship_Applied, Scholarship_Eligibility, Hostel_Required,
    Admission_Probability, Tuition_Fee
):
    if model is None:
        return "❌ Model not loaded. Please ensure 'college_admission_approval.pkl' exists in the app folder."

    try:
        data = pd.DataFrame([{
            "Age": Age,
            "Category": Category,
            "Family_Income": Family_Income,
            "Class10_%": Class10_Percentage,
            "Class12_%": Class12_Percentage,
            "PCM_%": PCM_Percentage,
            "Entrance_Exam": Entrance_Exam,
            "JEE_Percentile": JEE_Percentile,
            "JEE_Rank": JEE_Rank,
            "CUET_Score": CUET_Score,
            "Preferred_Branch": Preferred_Branch,
            "Preferred_College": Preferred_College,
            "College_Type": College_Type,
            "NIRF_Rank": NIRF_Rank,
            "College_Tier": College_Tier,
            "Branch_Cutoff_Rank": Branch_Cutoff_Rank,
            "Available_Seats": Available_Seats,
            "Reservation_Quota": Reservation_Quota,
            "Documents_Verified": Documents_Verified,
            "Interview_Score": Interview_Score,
            "Communication_Score": Communication_Score,
            "Aptitude_Score": Aptitude_Score,
            "Scholarship_Applied": Scholarship_Applied,
            "Scholarship_Eligibility": Scholarship_Eligibility,
            "Hostel_Required": Hostel_Required,
            "Admission_Probability": Admission_Probability,
            "Tuition_Fee": Tuition_Fee
        }])

        result = model.predict(data)[0]

        if str(result).strip().lower() in ["1", "yes", "approved", "1.0"]:
            return "🎉 ADMISSION APPROVED\n\n✅ Student has high probability of admission.\n\n🤖 Algorithm Used:\nRandom Forest Classifier"
        else:
            return "❌ ADMISSION NOT APPROVED\n\nStudent has low probability of admission.\n\n🤖 Algorithm Used:\nRandom Forest Classifier"

    except Exception as e:
        return f"❌ Prediction Error: {str(e)}"

# =====================================================
# PART 2 : COMPLETE CSS DESIGN
# =====================================================

css = f"""
/* FULL SCREEN BACKGROUND */
.gradio-container {{
    min-height: 100vh !important;
    width: 100% !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
    animation: backgroundSlide 25s infinite;
    background-image: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url("data:image/jpg;base64,{BACKGROUND_IMAGES[0]}");
}}

/* BACKGROUND IMAGE SLIDESHOW */
@keyframes backgroundSlide {{
    0% {{
        background-image: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url("data:image/jpg;base64,{BACKGROUND_IMAGES[0]}");
    }}
    20% {{
        background-image: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url("data:image/jpg;base64,{BACKGROUND_IMAGES[1]}");
    }}
    40% {{
        background-image: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url("data:image/jpg;base64,{BACKGROUND_IMAGES[2]}");
    }}
    60% {{
        background-image: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url("data:image/jpg;base64,{BACKGROUND_IMAGES[3]}");
    }}
    80% {{
        background-image: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url("data:image/jpg;base64,{BACKGROUND_IMAGES[4]}");
    }}
    100% {{
        background-image: linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url("data:image/jpg;base64,{BACKGROUND_IMAGES[0]}");
    }}
}}

/* GLASS MAIN CONTAINER */
#main-container {{
    width: 90% !important;
    max-width: 1250px !important;
    margin: 40px auto !important;
    padding: 35px !important;
    background: rgba(255, 255, 255, 0.65) !important;
    backdrop-filter: blur(18px) !important;
    -webkit-backdrop-filter: blur(18px) !important;
    border-radius: 30px !important;
    border: 2px solid rgba(255, 255, 255, 0.8) !important;
    box-shadow: 0px 15px 50px rgba(0, 0, 0, 0.5) !important;
}}

/* HEADER DESIGN */
#header-box {{
    text-align: center;
    padding: 30px;
    background: rgba(255, 255, 255, 0.50);
    border-radius: 25px;
    border-left: 8px solid #059669;
}}

#header-box h1 {{
    font-size: 42px;
    font-weight: 900;
    color: #064e3b !important;
}}

#header-box h2 {{
    font-size: 25px;
    color: #047857 !important;
}}

#header-box h3 {{
    color: #065f46 !important;
}}

#header-box p {{
    color: #111827 !important;
    font-size: 17px;
}}

/* INPUT FIELDS */
input, textarea, select {{
    background: rgba(255, 255, 255, 0.90) !important;
    color: black !important;
    border: 2px solid #10b981 !important;
    border-radius: 12px !important;
}}

label {{
    color: #064e3b !important;
    font-weight: bold !important;
}}

/* BUTTON STYLE */
button {{
    background: linear-gradient(135deg, #065f46, #10b981) !important;
    color: white !important;
    font-size: 20px !important;
    font-weight: bold !important;
    border-radius: 15px !important;
    padding: 12px !important;
}}

button:hover {{
    transform: scale(1.05);
    transition: 0.3s;
}}

/* OUTPUT BOX */
textarea {{
    font-size: 18px !important;
    font-weight: bold !important;
}}

/* HIDE FOOTER */
footer {{
    display: none !important;
}}
"""

# =====================================================
# PART 3 : GRADIO USER INTERFACE
# =====================================================

header = """
<div id="header-box">
    <h1>🎓 AI College Admission Approval System</h1>
    <h2>Machine Learning Based Admission Prediction Platform</h2>
    <hr>
    <h3>👩‍💻 Developer Details</h3>
    <p><b>Name:</b> Manya Singla</p>
    <p><b>College:</b> Panipat Institute of Engineering and Technology</p>
    <p><b>Project:</b> College Admission Prediction using Machine Learning</p>
    <hr>
    <h3>💻 Technologies Used</h3>
    <p>Python | Pandas | Scikit-Learn | Random Forest | Joblib | Gradio</p>
    <hr>
    <p>🤖 This AI system predicts college admission approval using academic performance, entrance exam scores, college preferences and student details.</p>
</div>
"""

with gr.Blocks(css=css, title="AI College Admission Approval System") as demo:
    with gr.Column(elem_id="main-container"):
        gr.HTML(header)
        gr.Markdown("## 📝 Enter Student Details\nFill all details to predict admission approval.")

        # BASIC DETAILS
        with gr.Row():
            Age = gr.Number(label="Age", value=18)
            Category = gr.Dropdown(choices=["General", "OBC", "SC", "ST"], label="Category", value="General")
            Family_Income = gr.Number(label="Family Income (₹)", value=500000)

        # ACADEMIC DETAILS
        with gr.Row():
            Class10 = gr.Number(label="Class 10 Percentage", value=85)
            Class12 = gr.Number(label="Class 12 Percentage", value=88)
            PCM = gr.Number(label="PCM Percentage", value=86)

        with gr.Row():
            Entrance = gr.Textbox(label="Entrance Exam", value="JEE Main")
            JEE = gr.Number(label="JEE Percentile", value=92)
            Rank = gr.Number(label="JEE Rank", value=25000)

        with gr.Row():
            CUET = gr.Number(label="CUET Score", value=650)
            Branch = gr.Textbox(label="Preferred Branch", value="Computer Science")
            College = gr.Textbox(label="Preferred College", value="PIET")

        # COLLEGE DETAILS
        with gr.Row():
            College_Type = gr.Dropdown(choices=["Government", "Private"], label="College Type", value="Private")
            NIRF = gr.Number(label="NIRF Rank", value=150)
            Tier = gr.Number(label="College Tier", value=2)

        with gr.Row():
            Cutoff = gr.Number(label="Branch Cutoff Rank", value=30000)
            Seats = gr.Number(label="Available Seats", value=120)
            Quota = gr.Textbox(label="Reservation Quota", value="General")

        # VERIFICATION DETAILS
        with gr.Row():
            Docs = gr.Dropdown(choices=["Yes", "No"], label="Documents Verified", value="Yes")
            Interview = gr.Number(label="Interview Score", value=80)
            Communication = gr.Number(label="Communication Score", value=85)

        # ADDITIONAL DETAILS
        with gr.Row():
            Aptitude = gr.Number(label="Aptitude Score", value=82)
            Scholarship = gr.Dropdown(choices=["Yes", "No"], label="Scholarship Applied", value="No")
            Scholarship_Eligibility = gr.Dropdown(choices=["Yes", "No"], label="Scholarship Eligibility", value="No")

        with gr.Row():
            Hostel = gr.Dropdown(choices=["Yes", "No"], label="Hostel Required", value="Yes")
            Probability = gr.Number(label="Admission Probability", value=0.85)
            Fee = gr.Number(label="Tuition Fee (₹)", value=120000)

        # BUTTON
        predict_button = gr.Button("🎯 Predict Admission", variant="primary")

        # RESULT BOX
        output = gr.Textbox(label="🎓 Admission Prediction Result", lines=8)

    # =====================================================
    # PART 4 : BUTTON CONNECTION
    # =====================================================
    predict_button.click(
        fn=predict_admission,
        inputs=[
            Age, Category, Family_Income, Class10, Class12, PCM,
            Entrance, JEE, Rank, CUET, Branch, College, College_Type,
            NIRF, Tier, Cutoff, Seats, Quota, Docs, Interview,
            Communication, Aptitude, Scholarship, Scholarship_Eligibility,
            Hostel, Probability, Fee
        ],
        outputs=output
    )

# =====================================================
# RUN APPLICATION
# =====================================================
if __name__ == "__main__":
    print("🚀 Starting AI College Admission Approval System")
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
