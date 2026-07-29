import os
import joblib
import pandas as pd
import gradio as gr


# ==========================================================
# LOAD MACHINE LEARNING MODEL
# ==========================================================

MODEL_PATH = "college_admission_approval.pkl"

try:
    model = joblib.load(MODEL_PATH)
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
        return "❌ Model file not found. Please add college_admission_approval.pkl"

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

        if str(result).strip().lower() in [
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
# CSS
# ==========================================================

css = """

/* =====================================================
   PAGE BACKGROUND
===================================================== */

html,
body {

    margin: 0 !important;
    padding: 0 !important;

    background: #111111 !important;

}


/* Remove Gradio's default background */

.gradio-container {

    max-width: none !important;

    min-height: 100vh !important;

    margin: 0 !important;

    padding: 0 !important;

    background: transparent !important;

}


/* =====================================================
   BACKGROUND SLIDESHOW
===================================================== */

#background-slideshow {

    position: fixed !important;

    top: 0 !important;
    left: 0 !important;

    width: 100vw !important;
    height: 100vh !important;

    z-index: 0 !important;

    overflow: hidden !important;

    pointer-events: none !important;

}


/* Background images */

#background-slideshow img {

    position: absolute !important;

    inset: 0 !important;

    width: 100% !important;
    height: 100% !important;

    object-fit: cover !important;

    object-position: center !important;

    opacity: 0 !important;

    animation-name: imageSlide !important;

    animation-duration: 20s !important;

    animation-iteration-count: infinite !important;

    animation-timing-function: ease-in-out !important;

}


/* Image timing */

#background-slideshow .image1 {

    animation-delay: 0s !important;

}


#background-slideshow .image2 {

    animation-delay: 5s !important;

}


#background-slideshow .image3 {

    animation-delay: 10s !important;

}


#background-slideshow .image4 {

    animation-delay: 15s !important;

}


/* =====================================================
   SLIDESHOW ANIMATION
===================================================== */

@keyframes imageSlide {

    0% {

        opacity: 0;

        transform: scale(1);

    }


    5% {

        opacity: 1;

    }


    20% {

        opacity: 1;

        transform: scale(1.06);

    }


    25% {

        opacity: 0;

    }


    100% {

        opacity: 0;

    }

}


/* =====================================================
   DARK OVERLAY
===================================================== */

#background-overlay {

    position: fixed !important;

    top: 0 !important;
    left: 0 !important;

    width: 100vw !important;
    height: 100vh !important;

    background: rgba(0, 0, 0, 0.30) !important;

    z-index: 1 !important;

    pointer-events: none !important;

}


/* =====================================================
   MAIN CONTENT
===================================================== */

#main-content {

    position: relative !important;

    z-index: 2 !important;

    width: min(1250px, 94%) !important;

    margin: 35px auto !important;

    padding: 30px !important;

    background: rgba(
        255,
        255,
        255,
        0.62
    ) !important;

    backdrop-filter: blur(7px) !important;

    -webkit-backdrop-filter: blur(7px) !important;

    border: 2px solid
    rgba(
        255,
        255,
        255,
        0.75
    ) !important;

    border-radius: 25px !important;

    box-shadow:
    0 10px 45px
    rgba(
        0,
        0,
        0,
        0.50
    ) !important;

}


/* =====================================================
   ALL TEXT BLACK
===================================================== */

#main-content,
#main-content h1,
#main-content h2,
#main-content h3,
#main-content h4,
#main-content p,
#main-content label,
#main-content span {

    color: black !important;

}


/* =====================================================
   HEADER
===================================================== */

#developer {

    background:
    rgba(
        255,
        255,
        255,
        0.50
    ) !important;

    padding: 25px !important;

    border-left:
    8px solid
    #087f5b !important;

    border-radius:
    18px !important;

}


#developer h1 {

    text-align: center !important;

    font-size: 38px !important;

    font-weight: 800 !important;

}


/* =====================================================
   INPUT FIELDS
===================================================== */

#main-content input,
#main-content textarea,
#main-content select {

    background:
    rgba(
        255,
        255,
        255,
        0.92
    ) !important;

    color:
    black !important;

    border:
    2px solid
    #4ca88a !important;

    border-radius:
    10px !important;

}


/* =====================================================
   BUTTON
===================================================== */

#main-content button {

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

    border-radius:
    14px !important;

}


#main-content button * {

    color:
    white !important;

}


/* =====================================================
   FOOTER
===================================================== */

footer {

    display: none !important;

}


/* =====================================================
   MOBILE
===================================================== */

@media screen and (max-width: 700px) {

    #main-content {

        width: 92% !important;

        margin: 10px auto !important;

        padding: 15px !important;

    }


    #developer h1 {

        font-size: 25px !important;

    }

}

"""


# ==========================================================
# BACKGROUND HTML
# ==========================================================

background_html = """

<div id="background-slideshow">

    <img
        class="image1"
        src="/gradio_api/file=images/college-img-1.jpg"
    >

    <img
        class="image2"
        src="/gradio_api/file=images/images (2).jpg"
    >

    <img
        class="image3"
        src="/gradio_api/file=images/images (3).jpg"
    >

    <img
        class="image4"
        src="/gradio_api/file=images/images (4).jpg"
    >

</div>


<div id="background-overlay"></div>

"""


# ==========================================================
# HEADER HTML
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

<p>
<b>Name:</b>
Manya Singla
</p>

<p>
<b>College:</b>
Panipat Institute of Engineering and Technology
</p>

<p>
<b>Project:</b>
College Admission Prediction using Machine Learning
</p>

<hr>

<h3>
💻 Technology Used
</h3>

<p>
Python | Pandas | Scikit-Learn |
Random Forest | Joblib | Gradio
</p>

<hr>

<h3>
🤖 About Project
</h3>

<p>
This AI-based system predicts admission approval
using academic records, entrance examination scores,
college preferences and student details.
</p>

</div>

"""


# ==========================================================
# CREATE GRADIO APP
# ==========================================================

with gr.Blocks(

    css=css,

    theme=gr.themes.Soft(),

    title="AI College Admission Approval System"

) as demo:


    # Background is outside the main content card

    gr.HTML(background_html)


    # All visible content is inside this one wrapper

    with gr.Column(

        elem_id="main-content"

    ):


        # HEADER

        gr.HTML(header)


        gr.Markdown(

            """

# 📝 Enter Student Details

Fill in all student details carefully.

"""

        )


        # ROW 1

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


        # ROW 2

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


        # ROW 3

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


        # ROW 4

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


        # ROW 5

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


        # ROW 6

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


        # ROW 7

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


        # ROW 8

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


        # ROW 9

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


        # BUTTON

        button = gr.Button(

            "🎯 Predict Admission",

            variant="primary"

        )


        # OUTPUT

        output = gr.Textbox(

            label="🎓 Admission Prediction Result",

            lines=8

        )


        # CONNECT BUTTON

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

    print("📁 Image folder:", image_folder)

    print(
        "📷 Images found:",
        os.listdir(image_folder)
        if os.path.exists(image_folder)
        else "IMAGE FOLDER NOT FOUND"
    )


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
