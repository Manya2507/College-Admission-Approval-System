import os
import gradio as gr
import joblib
import pandas as pd


# ==========================================================
# LOAD MODEL
# ==========================================================

MODEL_PATH = "college_admission_approval.pkl"


try:

    model = joblib.load(MODEL_PATH)

    print("✅ Model Loaded Successfully")


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
):

    if model is None:

        return "❌ Model not loaded"


    try:

        data = pd.DataFrame([{

            "Age":Age,
            "Category":Category,
            "Family_Income":Family_Income,

            "Class10_%":Class10,
            "Class12_%":Class12,
            "PCM_%":PCM,

            "Entrance_Exam":Entrance,
            "JEE_Percentile":JEE,
            "JEE_Rank":Rank,
            "CUET_Score":CUET,

            "Preferred_Branch":Branch,
            "Preferred_College":College,

            "College_Type":College_Type,

            "NIRF_Rank":NIRF,
            "College_Tier":Tier,

            "Branch_Cutoff_Rank":Cutoff,

            "Available_Seats":Seats,

            "Reservation_Quota":Quota,

            "Documents_Verified":Docs,

            "Interview_Score":Interview,
            "Communication_Score":Communication,
            "Aptitude_Score":Aptitude,

            "Scholarship_Applied":Scholarship,

            "Scholarship_Eligibility":
            Scholarship_Eligibility,

            "Hostel_Required":Hostel,

            "Admission_Probability":
            Probability,

            "Tuition_Fee":Fee

        }])


        prediction = model.predict(data)[0]


        if str(prediction).lower() in [
            "1",
            "yes",
            "approved"
        ]:


            return """

🎉 ADMISSION APPROVED


Prediction:
✅ Approved


Algorithm:
Random Forest Classifier

"""


        else:


            return """

❌ ADMISSION NOT APPROVED


Prediction:
❌ Not Approved


Algorithm:
Random Forest Classifier

"""


    except Exception as e:


        return f"Prediction Error: {e}"



# ==========================================================
# CORRECT CSS
# ==========================================================

css = """

html,
body{

margin:0;
padding:0;

background:transparent !important;

}



.gradio-container{

background:transparent !important;

}



/* BACKGROUND */

#background{

position:fixed;

top:0;

left:0;


width:100vw;

height:100vh;


z-index:0;


overflow:hidden;

}




#background img{


position:absolute;


width:100%;


height:100%;


object-fit:cover;


opacity:0;


animation:slide 20s infinite;

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




@keyframes slide{


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



/* OVERLAY */


#overlay{


position:fixed;


top:0;

left:0;


width:100%;


height:100%;


background:rgba(0,0,0,0.25);


z-index:1;


}



/* CONTENT */


#main{


position:relative;


z-index:2;


width:90%;


margin:30px auto;


padding:30px;


background:rgba(255,255,255,0.35);


border-radius:25px;


backdrop-filter:blur(12px);


}




#main *{


color:black !important;

}




button{


background:#087f5b !important;


color:white !important;


font-weight:bold !important;

}



footer{

display:none !important;

}

"""



# ==========================================================
# BACKGROUND HTML
# ==========================================================

background = """

<div id="background">


<img src="/gradio_api/file=images/college-img-1.jpg">


<img src="/gradio_api/file=images/images (2).jpg">


<img src="/gradio_api/file=images/images (3).jpg">


<img src="/gradio_api/file=images/images (4).jpg">


</div>



<div id="overlay"></div>


"""



# ==========================================================
# HEADER
# ==========================================================

header = """

<h1 style="text-align:center">

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

<b>Technology:</b>
Python | ML | Random Forest | Gradio

</p>

"""



# ==========================================================
# GRADIO APP
# ==========================================================


with gr.Blocks(
    css=css,
    title="College Admission Approval System"
) as demo:


    gr.HTML(background)


    with gr.Column(elem_id="main"):


        gr.HTML(header)


        gr.Markdown(
        """
        ## Enter Student Details
        """
        )


        Age = gr.Number(label="Age")

        Category = gr.Dropdown(
            ["General","OBC","SC","ST"],
            label="Category"
        )

        Family_Income = gr.Number(
            label="Family Income"
        )


        Class10 = gr.Number(
            label="Class 10 Percentage"
        )


        Class12 = gr.Number(
            label="Class 12 Percentage"
        )


        PCM = gr.Number(
            label="PCM Percentage"
        )


        Entrance = gr.Textbox(
            label="Entrance Exam"
        )


        JEE = gr.Number(
            label="JEE Percentile"
        )


        Rank = gr.Number(
            label="JEE Rank"
        )


        CUET = gr.Number(
            label="CUET Score"
        )


        Branch = gr.Textbox(
            label="Preferred Branch"
        )


        College = gr.Textbox(
            label="Preferred College"
        )


        College_Type = gr.Dropdown(
            ["Government","Private"],
            label="College Type"
        )


        NIRF = gr.Number(
            label="NIRF Rank"
        )


        Tier = gr.Number(
            label="College Tier"
        )


        Cutoff = gr.Number(
            label="Branch Cutoff Rank"
        )


        Seats = gr.Number(
            label="Available Seats"
        )


        Quota = gr.Textbox(
            label="Reservation Quota"
        )


        Docs = gr.Dropdown(
            ["Yes","No"],
            label="Documents Verified"
        )


        Interview = gr.Number(
            label="Interview Score"
        )


        Communication = gr.Number(
            label="Communication Score"
        )


        Aptitude = gr.Number(
            label="Aptitude Score"
        )


        Scholarship = gr.Dropdown(
            ["Yes","No"],
            label="Scholarship Applied"
        )


        Scholarship_Eligibility = gr.Dropdown(
            ["Yes","No"],
            label="Scholarship Eligibility"
        )


        Hostel = gr.Dropdown(
            ["Yes","No"],
            label="Hostel Required"
        )


        Probability = gr.Number(
            label="Admission Probability"
        )


        Fee = gr.Number(
            label="Tuition Fee"
        )


        button = gr.Button(
            "🎯 Predict Admission"
        )


        output = gr.Textbox(
            lines=8
        )


        button.click(
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
            outputs=output
        )



# ==========================================================
# RUN
# ==========================================================

if __name__=="__main__":


    image_folder=os.path.abspath("images")


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
