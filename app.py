import os
import joblib
import pandas as pd
import gradio as gr


# ==========================================================
# Load Machine Learning Model
# ==========================================================

try:
    model = joblib.load("college_admission_approval.pkl")
    print("✅ Admission Model Loaded Successfully")

except Exception as e:
    print("❌ Model Loading Error:", e)
    model = None


# ==========================================================
# Prediction Function
# ==========================================================

def predict_admission(
    Age,
    Category,
    Family_Income,
    Class10_Percentage,
    Class12_Percentage,
    PCM_Percentage,
    Entrance_Exam,
    JEE_Percentile,
    JEE_Rank,
    CUET_Score,
    Preferred_Branch,
    Preferred_College,
    College_Type,
    NIRF_Rank,
    College_Tier,
    Branch_Cutoff_Rank,
    Available_Seats,
    Reservation_Quota,
    Documents_Verified,
    Interview_Score,
    Communication_Score,
    Aptitude_Score,
    Scholarship_Applied,
    Scholarship_Eligibility,
    Hostel_Required,
    Admission_Probability,
    Tuition_Fee
):

    if model is None:
        return "❌ Model file not found. Please add admission_model.pkl"

    try:

        # Create input data
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


        # Model prediction
        result = model.predict(data)[0]


        # Approved result
        if str(result).lower() in ["1", "yes", "approved"]:

            return """
🎉 ADMISSION APPROVED

The student has a high probability of getting admission.

Prediction Result:
✅ Approved

Algorithm:
Random Forest Classifier
"""


        # Rejected result
        else:

            return """
❌ ADMISSION NOT APPROVED

The student admission probability is low.

Prediction Result:
❌ Not Approved

Algorithm:
Random Forest Classifier
"""


    except Exception as e:

        return f"❌ Prediction Error:\n{e}"


# ==========================================================
# Background Slideshow HTML
# ==========================================================

slideshow = """

<div class="background-slideshow">

    <div class="slide slide1"></div>

    <div class="slide slide2"></div>

    <div class="slide slide3"></div>

    <div class="slide slide4"></div>

</div>

<div class="dark-overlay"></div>

"""


# ==========================================================
# CSS Styling
# ==========================================================

css = """

/* ======================================================
   Full Screen Background
====================================================== */

body {

    margin: 0;

    background: #071a13;

}


/* ======================================================
   Background Slideshow
====================================================== */

.background-slideshow {

    position: fixed;

    top: 0;

    left: 0;

    width: 100%;

    height: 100%;

    z-index: -3;

    overflow: hidden;

}


.slide {

    position: absolute;

    width: 100%;

    height: 100%;

    background-size: cover;

    background-position: center;

    background-repeat: no-repeat;

    opacity: 0;

    animation: slideshow 20s infinite;

}


/* Image 1 */

.slide1 {

    background-image:
    url("/gradio_api/file=images/piet.jpg");

    animation-delay: 0s;

}


/* Image 2 */

.slide2 {

    background-image:
    url("/gradio_api/file=images/piet_building.jpg");

    animation-delay: 5s;

}


/* Image 3 */

.slide3 {

    background-image:
    url("/gradio_api/file=images/iit_delhi.jpg");

    animation-delay: 10s;

}


/* Image 4 */

.slide4 {

    background-image:
    url("/gradio_api/file=images/chitkara.jpg");

    animation-delay: 15s;

}


/* Smooth fade animation */

@keyframes slideshow {

    0% {

        opacity: 0;

        transform: scale(1);

    }


    5% {

        opacity: 1;

    }


    25% {

        opacity: 1;

        transform: scale(1.06);

    }


    30% {

        opacity: 0;

    }


    100% {

        opacity: 0;

    }

}


/* ======================================================
   Dark Overlay
====================================================== */

.dark-overlay {

    position: fixed;

    top: 0;

    left: 0;

    width: 100%;

    height: 100%;

    background:

    linear-gradient(

        135deg,

        rgba(0, 25, 20, 0.72),

        rgba(0, 0, 0, 0.55)

    );

    z-index: -2;

}


/* ======================================================
   Main Gradio Container
====================================================== */

.gradio-container {

    max-width: 1250px !important;

    margin: 25px auto !important;

    padding: 30px !important;

    border-radius: 25px !important;

    background:

    rgba(255, 255, 255, 0.88) !important;

    backdrop-filter:

    blur(12px) !important;

    -webkit-backdrop-filter:

    blur(12px) !important;

    border:

    2px solid rgba(255, 255, 255, 0.5);

    box-shadow:

    0 15px 50px

    rgba(0, 0, 0, 0.45);

}


/* ======================================================
   Developer Information
====================================================== */

#developer {

    background:

    linear-gradient(

        135deg,

        rgba(230, 255, 246, 0.96),

        rgba(255, 255, 255, 0.96)

    );

    border-radius: 20px;

    padding: 25px;

    margin-bottom: 25px;

    border-left:

    8px solid #087f5b;

    box-shadow:

    0 8px 25px

    rgba(0, 0, 0, 0.15);

}


#developer h1 {

    color: #075a42 !important;

    text-align: center;

    font-size: 34px;

}


#developer h2 {

    color: #087f5b !important;

}


#developer h3 {

    color: #075a42 !important;

}


/* ======================================================
   Input Boxes
====================================================== */

input,

textarea,

select {

    background:

    rgba(255, 255, 255, 0.97) !important;

    color:

    black !important;

    border:

    1.5px solid #63b99f !important;

    border-radius:

    10px !important;

}


/* Input focus */

input:focus,

textarea:focus,

select:focus {

    border:

    2px solid #087f5b !important;

    box-shadow:

    0 0 10px

    rgba(8, 127, 91, 0.4);

}


/* ======================================================
   Labels
====================================================== */

label {

    color:

    #063d2e !important;

    font-weight:

    bold !important;

}


/* ======================================================
   Prediction Button
====================================================== */

button {

    background:

    linear-gradient(

        135deg,

        #087f5b,

        #0ca678

    ) !important;

    color:

    white !important;

    font-size:

    20px !important;

    font-weight:

    bold !important;

    border-radius:

    14px !important;

    padding:

    14px !important;

    border:

    none !important;

    transition:

    0.3s !important;

    box-shadow:

    0 7px 20px

    rgba(0, 100, 70, 0.35);

}


button:hover {

    transform:

    translateY(-3px);

    box-shadow:

    0 10px 25px

    rgba(0, 100, 70, 0.5);

}


/* ======================================================
   Output Box
====================================================== */

textarea {

    font-size:

    17px !important;

    font-weight:

    bold !important;

}


/* ======================================================
   Hide Gradio Footer
====================================================== */

footer {

    display: none !important;

}


/* ======================================================
   Mobile Design
====================================================== */

@media(max-width: 700px) {

    .gradio-container {

        margin:

        8px !important;

        padding:

        15px !important;

    }


    #developer h1 {

        font-size:

        25px;

    }

}

"""


# ==========================================================
# Header Information
# ==========================================================

header = """

<div id="developer">

<h1>🎓 AI College Admission Approval System</h1>

<h2>👩‍💻 Developer Details</h2>

<b>Name:</b> Manya Singla<br>
<b>Github:</b>https://github.com/Manya2507/College-Admission-Approval-System/edit/main/app.py<br>
<b>Linkedin:</b>https://www.linkedin.com/in/manya-singla-438502423/<br>

<b>College:</b>
Panipat Institute of Engineering and Technology<br>

<b>Project:</b>
College Admission Prediction using Machine Learning


<hr>


<h3>💻 Technology Used</h3>

Python | Pandas | Scikit-Learn |
Random Forest | Joblib | Gradio


<hr>


<h3>🤖 About Project</h3>

This AI-based system predicts admission approval
using academic performance, entrance examination
scores, college preferences and student details.

</div>

"""


# ==========================================================
# Gradio Interface
# ==========================================================

with gr.Blocks(

    css=css,

    theme=gr.themes.Soft(),

    title="AI College Admission System"

) as demo:


    # Background slideshow
    gr.HTML(slideshow)


    # Header
    gr.HTML(header)


    gr.Markdown(

        """

        # 📝 Enter Student Details

        Fill in all the details carefully and click
        **Predict Admission**.

        """

    )


    # ------------------------------------------------------
    # Row 1
    # ------------------------------------------------------

    with gr.Row():

        Age = gr.Number(label="Age")

        Category = gr.Dropdown(

            ["General", "OBC", "SC", "ST"],

            label="Category"

        )

        Family_Income = gr.Number(

            label="Family Income (₹)"

        )


    # ------------------------------------------------------
    # Row 2
    # ------------------------------------------------------

    with gr.Row():

        Class10 = gr.Number(

            label="Class 10 Percentage"

        )

        Class12 = gr.Number(

            label="Class 12 Percentage"

        )

        PCM = gr.Number(

            label="PCM Percentage"

        )


    # ------------------------------------------------------
    # Row 3
    # ------------------------------------------------------

    with gr.Row():

        Entrance = gr.Textbox(

            label="Entrance Exam"

        )

        JEE = gr.Number(

            label="JEE Percentile"

        )

        Rank = gr.Number(

            label="JEE Rank"

        )


    # ------------------------------------------------------
    # Row 4
    # ------------------------------------------------------

    with gr.Row():

        CUET = gr.Number(

            label="CUET Score"

        )

        Branch = gr.Textbox(

            label="Preferred Branch"

        )

        College = gr.Textbox(

            label="Preferred College"

        )


    # ------------------------------------------------------
    # Row 5
    # ------------------------------------------------------

    with gr.Row():

        College_Type = gr.Dropdown(

            ["Government", "Private"],

            label="College Type"

        )

        NIRF = gr.Number(

            label="NIRF Rank"

        )

        Tier = gr.Number(

            label="College Tier"

        )


    # ------------------------------------------------------
    # Row 6
    # ------------------------------------------------------

    with gr.Row():

        Cutoff = gr.Number(

            label="Branch Cutoff Rank"

        )

        Seats = gr.Number(

            label="Available Seats"

        )

        Quota = gr.Textbox(

            label="Reservation Quota"

        )


    # ------------------------------------------------------
    # Row 7
    # ------------------------------------------------------

    with gr.Row():

        Docs = gr.Dropdown(

            ["Yes", "No"],

            label="Documents Verified"

        )

        Interview = gr.Number(

            label="Interview Score"

        )

        Communication = gr.Number(

            label="Communication Score"

        )


    # ------------------------------------------------------
    # Row 8
    # ------------------------------------------------------

    with gr.Row():

        Aptitude = gr.Number(

            label="Aptitude Score"

        )

        Scholarship = gr.Dropdown(

            ["Yes", "No"],

            label="Scholarship Applied"

        )

        Scholarship_Eligibility = gr.Dropdown(

            ["Yes", "No"],

            label="Scholarship Eligibility"

        )


    # ------------------------------------------------------
    # Row 9
    # ------------------------------------------------------

    with gr.Row():

        Hostel = gr.Dropdown(

            ["Yes", "No"],

            label="Hostel Required"

        )

        Probability = gr.Number(

            label="Admission Probability"

        )

        Fee = gr.Number(

            label="Tuition Fee (₹)"

        )


    # ======================================================
    # Prediction Button
    # ======================================================

    button = gr.Button(

        "🎯 Predict Admission",

        variant="primary"

    )


    # ======================================================
    # Output
    # ======================================================

    output = gr.Textbox(

        label="🎓 Admission Prediction Result",

        lines=8

    )


    # ======================================================
    # Connect Button to Prediction Function
    # ======================================================

    button.click(

        fn=predict_admission,

        inputs=[

            Age,
            Category,
            Family_Income,

            Class10,
            Class12,
            PCM,

            Entrance,
            JEE,
            Rank,

            CUET,
            Branch,
            College,

            College_Type,
            NIRF,
            Tier,

            Cutoff,
            Seats,
            Quota,

            Docs,
            Interview,
            Communication,

            Aptitude,
            Scholarship,
            Scholarship_Eligibility,

            Hostel,
            Probability,
            Fee

        ],

        outputs=output

    )


# ==========================================================
# Run Application
# ==========================================================

if __name__ == "__main__":

    demo.launch(

        server_name="0.0.0.0",

        server_port=int(

            os.environ.get(

                "PORT",

                7860

            )

        ),

        allowed_paths=[

            os.path.abspath(

                "images"

            )

        ]

    )
