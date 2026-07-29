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
# IMAGE PATHS
# ==========================================================

# The folder name shown in GitHub is "image"

IMAGE_FOLDER = os.path.abspath("image")

IMAGE_1 = os.path.join(
    IMAGE_FOLDER,
    "college-img-1.jpg"
)

IMAGE_2 = os.path.join(
    IMAGE_FOLDER,
    "images (2).jpg"
)

IMAGE_3 = os.path.join(
    IMAGE_FOLDER,
    "images (3).jpg"
)

IMAGE_4 = os.path.join(
    IMAGE_FOLDER,
    "images (4).jpg"
)


# Check whether images are available

print("\n========== IMAGE CHECK ==========")

for image_path in [
    IMAGE_1,
    IMAGE_2,
    IMAGE_3,
    IMAGE_4
]:

    if os.path.exists(image_path):

        print(
            "✅ Image found:",
            image_path
        )

    else:

        print(
            "❌ Image not found:",
            image_path
        )

print("=================================\n")


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

        return (
            "❌ Model file not found.\n\n"
            "Please add:\n"
            "college_admission_approval.pkl"
        )


    try:

        data = pd.DataFrame([{

            "Age":
            Age,

            "Category":
            Category,

            "Family_Income":
            Family_Income,


            "Class10_%":
            Class10_Percentage,

            "Class12_%":
            Class12_Percentage,

            "PCM_%":
            PCM_Percentage,


            "Entrance_Exam":
            Entrance_Exam,

            "JEE_Percentile":
            JEE_Percentile,

            "JEE_Rank":
            JEE_Rank,

            "CUET_Score":
            CUET_Score,


            "Preferred_Branch":
            Preferred_Branch,

            "Preferred_College":
            Preferred_College,

            "College_Type":
            College_Type,


            "NIRF_Rank":
            NIRF_Rank,

            "College_Tier":
            College_Tier,

            "Branch_Cutoff_Rank":
            Branch_Cutoff_Rank,


            "Available_Seats":
            Available_Seats,

            "Reservation_Quota":
            Reservation_Quota,


            "Documents_Verified":
            Documents_Verified,


            "Interview_Score":
            Interview_Score,

            "Communication_Score":
            Communication_Score,

            "Aptitude_Score":
            Aptitude_Score,


            "Scholarship_Applied":
            Scholarship_Applied,

            "Scholarship_Eligibility":
            Scholarship_Eligibility,


            "Hostel_Required":
            Hostel_Required,

            "Admission_Probability":
            Admission_Probability,

            "Tuition_Fee":
            Tuition_Fee

        }])


        result = model.predict(
            data
        )[0]


        if str(result).lower() in [

            "1",

            "yes",

            "approved",

            "true"

        ]:


            return """

🎉 ADMISSION APPROVED

The student has a high probability
of getting admission.

Prediction Result:
✅ Approved

Algorithm:
Random Forest Classifier

"""


        else:


            return """

❌ ADMISSION NOT APPROVED

The student has a low probability
of getting admission.

Prediction Result:
❌ Not Approved

Algorithm:
Random Forest Classifier

"""


    except Exception as e:


        return (

            "❌ Prediction Error:\n\n"

            f"{e}"

        )


# ==========================================================
# CSS
# ==========================================================

css = """

/* =====================================================
   COMPLETE PAGE
===================================================== */

html,
body {

    margin:
    0 !important;

    padding:
    0 !important;

    width:
    100% !important;

    min-height:
    100% !important;

    background:
    transparent !important;

}


/* =====================================================
   FULL SCREEN BACKGROUND
===================================================== */

#background {

    position:
    fixed !important;

    top:
    0 !important;

    left:
    0 !important;

    width:
    100vw !important;

    height:
    100vh !important;

    overflow:
    hidden !important;

    z-index:
    -100 !important;

}


/* =====================================================
   BACKGROUND IMAGES
===================================================== */

.background-slide {

    position:
    absolute !important;

    top:
    0 !important;

    left:
    0 !important;

    width:
    100vw !important;

    height:
    100vh !important;

    object-fit:
    cover !important;

    object-position:
    center !important;

    opacity:
    0 !important;

    animation:
    slideShow
    20s
    infinite !important;

}


/* =====================================================
   IMAGE TIMING
===================================================== */

.slide-1 {

    animation-delay:
    0s !important;

}


.slide-2 {

    animation-delay:
    5s !important;

}


.slide-3 {

    animation-delay:
    10s !important;

}


.slide-4 {

    animation-delay:
    15s !important;

}


/* =====================================================
   SLIDESHOW ANIMATION
===================================================== */

@keyframes slideShow {


    0% {

        opacity:
        0;

        transform:
        scale(1);

    }


    5% {

        opacity:
        1;

    }


    22% {

        opacity:
        1;

        transform:
        scale(1.08);

    }


    27% {

        opacity:
        0;

    }


    100% {

        opacity:
        0;

    }

}


/* =====================================================
   DARK OVERLAY
===================================================== */

#background-overlay {

    position:
    fixed !important;

    top:
    0 !important;

    left:
    0 !important;

    width:
    100vw !important;

    height:
    100vh !important;

    background:
    rgba(
        0,
        0,
        0,
        0.20
    ) !important;

    z-index:
    -90 !important;

}


/* =====================================================
   GRADIO MAIN CONTAINER
===================================================== */

.gradio-container {

    position:
    relative !important;

    z-index:
    10 !important;

    max-width:
    1250px !important;

    margin:
    25px auto !important;

    padding:
    30px !important;

    background:
    rgba(
        255,
        255,
        255,
        0.70
    ) !important;

    backdrop-filter:
    blur(8px) !important;

    -webkit-backdrop-filter:
    blur(8px) !important;

    border:
    2px solid
    rgba(
        255,
        255,
        255,
        0.70
    ) !important;

    border-radius:
    25px !important;

    box-shadow:
    0 10px 45px
    rgba(
        0,
        0,
        0,
        0.40
    ) !important;

}


/* =====================================================
   ALL TEXT BLACK
===================================================== */

.gradio-container,

.gradio-container *,

.gradio-container p,

.gradio-container span,

.gradio-container label,

.gradio-container h1,

.gradio-container h2,

.gradio-container h3,

.gradio-container h4 {

    color:
    black !important;

}


/* =====================================================
   HEADER BOX
===================================================== */

#developer {

    background:
    rgba(
        255,
        255,
        255,
        0.85
    ) !important;

    padding:
    25px !important;

    border-radius:
    18px !important;

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


#developer h1 {

    text-align:
    center !important;

    font-size:
    35px !important;

    font-weight:
    bold !important;

}


/* =====================================================
   INPUT FIELDS
===================================================== */

input,

textarea,

select {

    background:
    rgba(
        255,
        255,
        255,
        0.96
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
   INPUT LABELS
===================================================== */

label {

    color:
    black !important;

    font-size:
    15px !important;

    font-weight:
    bold !important;

}


/* =====================================================
   PREDICTION BUTTON
===================================================== */

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

}


button * {

    color:
    white !important;

}


button:hover {

    transform:
    scale(
        1.02
    ) !important;

}


/* =====================================================
   OUTPUT BOX
===================================================== */

textarea {

    font-size:
    17px !important;

    font-weight:
    bold !important;

}


/* =====================================================
   REMOVE GRADIO FOOTER
===================================================== */

footer {

    display:
    none !important;

}


/* =====================================================
   MOBILE VIEW
===================================================== */

@media screen and (
    max-width:
    700px
) {


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
# CREATE GRADIO APP
# ==========================================================

with gr.Blocks(

    css=css,

    theme=gr.themes.Soft(),

    title=
    "AI College Admission Approval System"

) as demo:


    # ======================================================
    # BACKGROUND SLIDESHOW
    # ======================================================

    gr.HTML(

        f"""

<div id="background">

<img

class="background-slide slide-1"

src="/gradio_api/file={IMAGE_1}"

>


<img

class="background-slide slide-2"

src="/gradio_api/file={IMAGE_2}"

>


<img

class="background-slide slide-3"

src="/gradio_api/file={IMAGE_3}"

>


<img

class="background-slide slide-4"

src="/gradio_api/file={IMAGE_4}"

>

</div>


<div id="background-overlay">

</div>

"""

    )


    # ======================================================
    # HEADER
    # ======================================================

    gr.HTML(
        header
    )


    gr.Markdown(

        """

# 📝 Enter Student Details

Fill in all student details carefully.

        """

    )


    # ======================================================
    # ROW 1
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

            label=
            "Family Income (₹)"

        )


    # ======================================================
    # ROW 2
    # ======================================================

    with gr.Row():

        Class10 = gr.Number(

            label=
            "Class 10 Percentage"

        )

        Class12 = gr.Number(

            label=
            "Class 12 Percentage"

        )

        PCM = gr.Number(

            label=
            "PCM Percentage"

        )


    # ======================================================
    # ROW 3
    # ======================================================

    with gr.Row():

        Entrance = gr.Textbox(

            label=
            "Entrance Exam"

        )

        JEE = gr.Number(

            label=
            "JEE Percentile"

        )

        Rank = gr.Number(

            label=
            "JEE Rank"

        )


    # ======================================================
    # ROW 4
    # ======================================================

    with gr.Row():

        CUET = gr.Number(

            label=
            "CUET Score"

        )

        Branch = gr.Textbox(

            label=
            "Preferred Branch"

        )

        College = gr.Textbox(

            label=
            "Preferred College"

        )


    # ======================================================
    # ROW 5
    # ======================================================

    with gr.Row():

        College_Type = gr.Dropdown(

            [
                "Government",
                "Private"
            ],

            label=
            "College Type"

        )

        NIRF = gr.Number(

            label=
            "NIRF Rank"

        )

        Tier = gr.Number(

            label=
            "College Tier"

        )


    # ======================================================
    # ROW 6
    # ======================================================

    with gr.Row():

        Cutoff = gr.Number(

            label=
            "Branch Cutoff Rank"

        )

        Seats = gr.Number(

            label=
            "Available Seats"

        )

        Quota = gr.Textbox(

            label=
            "Reservation Quota"

        )


    # ======================================================
    # ROW 7
    # ======================================================

    with gr.Row():

        Docs = gr.Dropdown(

            [
                "Yes",
                "No"
            ],

            label=
            "Documents Verified"

        )

        Interview = gr.Number(

            label=
            "Interview Score"

        )

        Communication = gr.Number(

            label=
            "Communication Score"

        )


    # ======================================================
    # ROW 8
    # ======================================================

    with gr.Row():

        Aptitude = gr.Number(

            label=
            "Aptitude Score"

        )

        Scholarship = gr.Dropdown(

            [
                "Yes",
                "No"
            ],

            label=
            "Scholarship Applied"

        )

        Scholarship_Eligibility = gr.Dropdown(

            [
                "Yes",
                "No"
            ],

            label=
            "Scholarship Eligibility"

        )


    # ======================================================
    # ROW 9
    # ======================================================

    with gr.Row():

        Hostel = gr.Dropdown(

            [
                "Yes",
                "No"
            ],

            label=
            "Hostel Required"

        )

        Probability = gr.Number(

            label=
            "Admission Probability"

        )

        Fee = gr.Number(

            label=
            "Tuition Fee (₹)"

        )


    # ======================================================
    # PREDICT BUTTON
    # ======================================================

    button = gr.Button(

        "🎯 Predict Admission",

        variant=
        "primary"

    )


    # ======================================================
    # OUTPUT
    # ======================================================

    output = gr.Textbox(

        label=
        "🎓 Admission Prediction Result",

        lines=
        8

    )


    # ======================================================
    # BUTTON FUNCTION
    # ======================================================

    button.click(

        fn=
        predict_admission,

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

        outputs=
        output

    )


# ==========================================================
# RUN APPLICATION
# ==========================================================

if __name__ == "__main__":

    demo.launch(

        server_name=
        "0.0.0.0",

        server_port=
        int(

            os.environ.get(

                "PORT",

                7860

            )

        ),

        allowed_paths=[

            IMAGE_FOLDER

        ]

    )
