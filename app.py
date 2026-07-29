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
        return "❌ Model not loaded"


    try:

        input_data = pd.DataFrame([{

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


        prediction = model.predict(input_data)[0]


        if str(prediction).lower() in [
            "1",
            "yes",
            "approved"
        ]:

            return """
🎉 ADMISSION APPROVED

Student has a high chance of getting admission.

Prediction:
✅ Approved

Model:
Random Forest Classifier
"""


        else:

            return """
❌ ADMISSION NOT APPROVED

Student has a low chance of getting admission.

Prediction:
❌ Not Approved

Model:
Random Forest Classifier
"""


    except Exception as e:

        return f"❌ Prediction Error\n{e}"





# ==========================================================
# CSS WITH VISIBLE BACKGROUND SLIDESHOW
# ==========================================================

css = """

html, body {

    margin:0;
    padding:0;

    background:transparent !important;

}



.gradio-container {

    width:100% !important;

    min-height:100vh !important;

    background:transparent !important;

}



/* ===============================
   BACKGROUND SLIDESHOW
================================*/


#background {

    position:fixed;

    top:0;
    left:0;

    width:100vw;
    height:100vh;

    z-index:-3;

    overflow:hidden;

}



#background img {

    position:absolute;

    width:100%;
    height:100%;

    object-fit:cover;

    opacity:0;

    animation:changeImage 20s infinite;

}



#background img:nth-child(1){

    animation-delay:0s;

}


#background img:nth-child(2){

    animation-delay:5s;

}


#background img:nth-child(3){

    animation-delay:10s;

}


#background img:nth-child(4){

    animation-delay:15s;

}



@keyframes changeImage{


0%{

opacity:0;

transform:scale(1);

}


5%{

opacity:1;

}


20%{

opacity:1;

transform:scale(1.08);

}


25%{

opacity:0;

}


100%{

opacity:0;

}

}



/* Dark transparent layer */


#overlay{

position:fixed;

inset:0;

background:rgba(0,0,0,0.20);

z-index:-2;

}



/* Main glass container */


#main-container{


position:relative;

z-index:2;


width:min(1200px,90%);


margin:30px auto;


padding:30px;


border-radius:25px;


background:rgba(255,255,255,0.35);


backdrop-filter:blur(12px);


-webkit-backdrop-filter:blur(12px);


box-shadow:

0 10px 40px rgba(0,0,0,0.4);


}



#main-container *{

color:black !important;

}


"""
# ==========================================================
# BACKGROUND HTML
# ==========================================================

background_html = """

<div id="background">

    <img src="/gradio_api/file=images/college-img-1.jpg">

    <img src="/gradio_api/file=images/images (2).jpg">

    <img src="/gradio_api/file=images/images (3).jpg">

    <img src="/gradio_api/file=images/images (4).jpg">

</div>


<div id="overlay"></div>

"""



# ==========================================================
# DEVELOPER HEADER
# ==========================================================

header_html = """

<div style="
text-align:center;
padding:25px;
background:rgba(255,255,255,0.45);
border-radius:20px;
">


<h1>
🎓 AI College Admission Approval System
</h1>


<hr>


<h2>
👩‍💻 Developer Details
</h2>


<p>
<b>Name:</b> Manya Singla
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
💻 Technologies Used
</h3>


<p>

Python |
Pandas |
Scikit-Learn |
Random Forest |
Joblib |
Gradio

</p>


<hr>


<h3>
🤖 About Project
</h3>


<p>

This AI-based system predicts whether a student
will get admission approval based on academic records,
entrance examination scores, college preferences,
and student information.

</p>


</div>

"""



# ==========================================================
# CREATE GRADIO APPLICATION
# ==========================================================


with gr.Blocks(

    css=css,

    theme=gr.themes.Soft(),

    title="AI College Admission Approval System"

) as demo:



    # Background slideshow

    gr.HTML(background_html)



    # Main glass container

    with gr.Column(

        elem_id="main-container"

    ):



        # Developer section

        gr.HTML(header_html)



        gr.Markdown(

"""

# 📝 Student Admission Details

Enter student information to predict admission approval.

"""

        )



        # ==================================================
        # INPUT ROW 1
        # ==================================================


        with gr.Row():


            Age = gr.Number(

                label="Age"

            )


            Category = gr.Dropdown(

                choices=[

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



        # ==================================================
        # INPUT ROW 2
        # ==================================================


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



        # ==================================================
        # INPUT ROW 3
        # ==================================================


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



        # ==================================================
        # INPUT ROW 4
        # ==================================================


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



        # ==================================================
        # INPUT ROW 5
        # ==================================================


        with gr.Row():


            College_Type = gr.Dropdown(

                choices=[

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
                    # ==================================================
        # INPUT ROW 6
        # ==================================================

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



        # ==================================================
        # INPUT ROW 7
        # ==================================================

        with gr.Row():


            Docs = gr.Dropdown(

                choices=[

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



        # ==================================================
        # INPUT ROW 8
        # ==================================================

        with gr.Row():


            Aptitude = gr.Number(

                label="Aptitude Score"

            )


            Scholarship = gr.Dropdown(

                choices=[

                    "Yes",
                    "No"

                ],

                label="Scholarship Applied"

            )


            Scholarship_Eligibility = gr.Dropdown(

                choices=[

                    "Yes",
                    "No"

                ],

                label="Scholarship Eligibility"

            )



        # ==================================================
        # INPUT ROW 9
        # ==================================================

        with gr.Row():


            Hostel = gr.Dropdown(

                choices=[

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



        # ==================================================
        # PREDICT BUTTON
        # ==================================================

        predict_btn = gr.Button(

            "🎯 Predict Admission",

            variant="primary"

        )



        # ==================================================
        # OUTPUT
        # ==================================================

        output = gr.Textbox(

            label="🎓 Admission Prediction Result",

            lines=8

        )



        # ==================================================
        # BUTTON CONNECTION
        # ==================================================

        predict_btn.click(

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
# RESPONSIVE CSS ADDITION
# ==========================================================

css += """



/* Input boxes */

input,
textarea,
select {


    background:rgba(255,255,255,0.85) !important;

    border-radius:10px !important;

    border:2px solid #4caf50 !important;

    color:black !important;

}




/* Button styling */


button {


    background:

    linear-gradient(

        135deg,

        #087f5b,

        #18a875

    ) !important;


    color:white !important;


    font-size:18px !important;


    font-weight:bold !important;


    border-radius:15px !important;


}



button span{

    color:white !important;

}




/* Markdown */


.markdown h1,
.markdown h2,
.markdown h3 {


    color:black !important;

}



/* Hide Gradio footer */


footer{

    display:none !important;

}




/* Mobile view */


@media(max-width:700px){


    #main-container{


        width:92% !important;


        padding:15px !important;


        margin:15px auto !important;


    }



    h1{


        font-size:25px !important;

    }


}

"""



# ==========================================================
# RUN APPLICATION
# ==========================================================


if __name__ == "__main__":



    image_folder = os.path.abspath("images")



    print(
        "📁 Image Folder:",
        image_folder
    )



    if os.path.exists(image_folder):


        print(

            "📷 Images Found:",

            os.listdir(image_folder)

        )


    else:


        print(

            "❌ Images Folder Not Found"

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
from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("model", RandomForestClassifier())
])


pipeline.fit(X_train,y_train)


joblib.dump(
    pipeline,
    "college_admission_approval.pkl"
)
