import os
import joblib
import pandas as pd
import gradio as gr


# ==========================================================
# LOAD MACHINE LEARNING MODEL
# ==========================================================

try:
    model = joblib.load("college_admission_approval.pkl")
    print("✅ Admission Model Loaded Successfully")

except Exception as e:
    print("❌ Model Loading Error:", e)
    model = None


# ==========================================================
# PREDICTION FUNCTION
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


        if str(result).lower() in [
            "1",
            "yes",
            "approved"
        ]:

            return """
🎉 ADMISSION APPROVED

The student has a high probability of getting admission.

Prediction Result:
✅ Approved

Algorithm:
Random Forest Classifier
"""

        else:

            return """
❌ ADMISSION NOT APPROVED

The student has a low probability of getting admission.

Prediction Result:
❌ Not Approved

Algorithm:
Random Forest Classifier
"""


    except Exception as e:

        return f"❌ Prediction Error:\n{e}"


# ==========================================================
# CSS FOR BACKGROUND SLIDESHOW
# ==========================================================

css = """

/* ======================================================
   COMPLETE PAGE
====================================================== */

html,
body {

    margin: 0 !important;

    padding: 0 !important;

    min-height: 100% !important;

    color: black !important;

}


/* ======================================================
   BACKGROUND SLIDESHOW
====================================================== */

#slideshow {

    position: fixed !important;

    top: 0 !important;

    left: 0 !important;

    width: 100vw !important;

    height: 100vh !important;

    overflow: hidden !important;

    z-index: -100 !important;

}


/* Every slide */

.background-image {

    position: absolute !important;

    top: 0 !important;

    left: 0 !important;

    width: 100% !important;

    height: 100% !important;

    object-fit: cover !important;

    object-position: center !important;

    opacity: 0 !important;

    animation:

    backgroundAnimation

    20s

    infinite !important;

}


/* Image 1 */

.image1 {

    animation-delay: 0s !important;

}


/* Image 2 */

.image2 {

    animation-delay: 5s !important;

}


/* Image 3 */

.image3 {

    animation-delay: 10s !important;

}


/* Image 4 */

.image4 {

    animation-delay: 15s !important;

}


/* ======================================================
   SLIDESHOW ANIMATION
====================================================== */

@keyframes backgroundAnimation {

    0% {

        opacity: 0;

        transform: scale(1);

    }


    5% {

        opacity: 1;

    }


    22% {

        opacity: 1;

        transform: scale(1.05);

    }


    27% {

        opacity: 0;

    }


    100% {

        opacity: 0;

    }

}


/* ======================================================
   DARK TRANSPARENT OVERLAY
====================================================== */

#background-overlay {

    position: fixed !important;

    top: 0 !important;

    left: 0 !important;

    width: 100vw !important;

    height: 100vh !important;

    background:

    rgba(0, 0, 0, 0.30) !important;

    z-index: -90 !important;

}


/* ======================================================
   MAIN GRADIO CONTAINER
====================================================== */

.gradio-container {

    position: relative !important;

    z-index: 10 !important;

    max-width: 1250px !important;

    margin: 25px auto !important;

    padding: 30px !important;

    background:

    rgba(
        255,
        255,
        255,
        0.88
    ) !important;

    backdrop-filter:

    blur(10px) !important;

    -webkit-backdrop-filter:

    blur(10px) !important;

    border:

    2px solid

    rgba(
        255,
        255,
        255,
        0.75
    ) !important;

    border-radius:

    25px !important;

    box-shadow:

    0 10px 45px

    rgba(
        0,
        0,
        0,
        0.45
    ) !important;

}


/* ======================================================
   ALL TEXT BLACK
====================================================== */

.gradio-container,

.gradio-container *,

.gradio-container p,

.gradio-container span,

.gradio-container label,

.gradio-container h1,

.gradio-container h2,

.gradio-container h3,

.gradio-container h4 {

    color: black !important;

}


/* ======================================================
   DEVELOPER BOX
====================================================== */

#developer {

    background:

    rgba(
        255,
        255,
        255,
        0.93
    ) !important;

    color:

    black !important;

    border-radius:

    18px !important;

    padding:

    25px !important;

    border-left:

    8px solid

    #087f5b !important;

    box-shadow:

    0 5px 20px

    rgba(
        0,
        0,
        0,
        0.18
    ) !important;

}


/* Heading */

#developer h1 {

    text-align:

    center !important;

    font-size:

    35px !important;

    font-weight:

    bold !important;

    color:

    black !important;

}


/* ======================================================
   INPUT FIELDS
====================================================== */

input,

textarea,

select {

    background:

    white !important;

    color:

    black !important;

    border:

    2px solid

    #4ca88a !important;

    border-radius:

    10px !important;

}


/* Placeholder text */

input::placeholder,

textarea::placeholder {

    color:

    #333333 !important;

}


/* ======================================================
   INPUT LABELS
====================================================== */

label {

    color:

    black !important;

    font-size:

    15px !important;

    font-weight:

    bold !important;

}


/* ======================================================
   PREDICTION BUTTON
====================================================== */

button {

    background:

    linear-gradient(

        135deg,

        #087f5b,

        #18a875

    ) !important;

    color:

    white !important;

    font-size:

    20px !important;

    font-weight:

    bold !important;

    border:

    none !important;

    border-radius:

    14px !important;

    padding:

    14px !important;

    box-shadow:

    0 7px 18px

    rgba(
        0,
        0,
        0,
        0.30
    ) !important;

}


/* Button text must remain white */

button * {

    color:

    white !important;

}


/* Button hover */

button:hover {

    transform:

    scale(1.02) !important;

}


/* ======================================================
   OUTPUT BOX
====================================================== */

textarea {

    font-size:

    17px !important;

    font-weight:

    bold !important;

    color:

    black !important;

}


/* ======================================================
   REMOVE GRADIO FOOTER
====================================================== */

footer {

    display:

    none !important;

}


/* ======================================================
   MOBILE VIEW
====================================================== */

@media screen and (max-width: 700px) {

    .gradio-container {

        margin:

        8px !important;

        padding:

        15px !important;

    }


    #developer h1 {

        font-size:

        24px !important;

    }

}

"""


# ==========================================================
# HEADER
# ==========================================================

header = """

<div id="developer">

<h1>
🎓 AI College Admission Approval System
</h1>

<hr>

<h2>
👩‍💻 Developer Details
</h2>

<b>Name:</b>
Manya Singla

<br><br>

<b>College:</b>
Panipat Institute of Engineering and Technology

<br><br>

<b>Project:</b>
College Admission Prediction using Machine Learning

<hr>

<h3>
💻 Technology Used
</h3>

Python | Pandas | Scikit-Learn |
Random Forest | Joblib | Gradio

<hr>

<h3>
🤖 About Project
</h3>

This AI-based system predicts admission approval
using academic records, entrance examination scores,
college preferences and student details.

</div>

"""


# ==========================================================
# GRADIO APPLICATION
# ==========================================================

with gr.Blocks(

    css=css,

    theme=gr.themes.Soft(),

    title="AI College Admission Approval System"

) as demo:


    # ======================================================
    # BACKGROUND SLIDESHOW
    # ======================================================

    gr.HTML(

        """

        <div id="slideshow">

            <img

            class="background-image image1"

            src="/gradio_api/file=data:image/jpeg;base64,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"

            >


            <img

            class="background-image image2"

            src="/gradio_api/file=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBakU-4HlNRGo4x4JYlhjKxkEwMhfDtLSv88xE8N2efQ&s=10"

            >


            <img

            class="background-image image3"

            src="/gradio_api/file=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9qvww5W9uAk6iORTQn2HNIl7Uf04jrvv5xcmeDDh7_g&s=10"

            >


            <img

            class="background-image image4"

            src="/gradio_api/file=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuDmesQ7DOPxCzvhjGLZwh0fWC3qOcikTOOCbRwdSpcw&s=10"

            >

        </div>


        <div id="background-overlay">

        </div>

        """

    )


    # ======================================================
    # HEADER
    # ======================================================

    gr.HTML(header)


    gr.Markdown(

        """

        # 📝 Enter Student Details

        Fill in all student details carefully.

        """

    )


    # ======================================================
    # INPUT ROW 1
    # ======================================================

    with gr.Row():

        Age = gr.Number(
            label="Age"
        )

        Category = gr.Dropdown(
            [
                "General",
                "OBC",
                "SC",
                "ST"
            ],
            label="Category"
        )

        Family_Income = gr.Number(
            label="Family Income (₹)"
        )


    # ======================================================
    # INPUT ROW 2
    # ======================================================

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


    # ======================================================
    # INPUT ROW 3
    # ======================================================

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


    # ======================================================
    # INPUT ROW 4
    # ======================================================

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


    # ======================================================
    # INPUT ROW 5
    # ======================================================

    with gr.Row():

        College_Type = gr.Dropdown(
            [
                "Government",
                "Private"
            ],
            label="College Type"
        )

        NIRF = gr.Number(
            label="NIRF Rank"
        )

        Tier = gr.Number(
            label="College Tier"
        )


    # ======================================================
    # INPUT ROW 6
    # ======================================================

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


    # ======================================================
    # INPUT ROW 7
    # ======================================================

    with gr.Row():

        Docs = gr.Dropdown(
            [
                "Yes",
                "No"
            ],
            label="Documents Verified"
        )

        Interview = gr.Number(
            label="Interview Score"
        )

        Communication = gr.Number(
            label="Communication Score"
        )


    # ======================================================
    # INPUT ROW 8
    # ======================================================

    with gr.Row():

        Aptitude = gr.Number(
            label="Aptitude Score"
        )

        Scholarship = gr.Dropdown(
            [
                "Yes",
                "No"
            ],
            label="Scholarship Applied"
        )

        Scholarship_Eligibility = gr.Dropdown(
            [
                "Yes",
                "No"
            ],
            label="Scholarship Eligibility"
        )


    # ======================================================
    # INPUT ROW 9
    # ======================================================

    with gr.Row():

        Hostel = gr.Dropdown(
            [
                "Yes",
                "No"
            ],
            label="Hostel Required"
        )

        Probability = gr.Number(
            label="Admission Probability"
        )

        Fee = gr.Number(
            label="Tuition Fee (₹)"
        )


    # ======================================================
    # BUTTON
    # ======================================================

    button = gr.Button(

        "🎯 Predict Admission",

        variant="primary"

    )


    # ======================================================
    # OUTPUT
    # ======================================================

    output = gr.Textbox(

        label="🎓 Admission Prediction Result",

        lines=8

    )


    # ======================================================
    # BUTTON CONNECTION
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
# RUN APPLICATION
# ==========================================================

if __name__ == "__main__":

    image_folder = os.path.abspath("images")


    demo.launch(

        server_name="0.0.0.0",

        server_port=int(

            os.environ.get(

                "PORT",

                7860

            )

        ),

        allowed_paths=[

            image_folder

        ]

    )
