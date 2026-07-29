import os
import joblib
import pandas as pd
import gradio as gr


# ==========================================================
# Load Machine Learning Model
# ==========================================================

try:
    model = joblib.load("admission_model.pkl")
    print("Admission Model Loaded Successfully")

except Exception as e:
    print("Model Loading Error:", e)
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
        return "❌ Model file not found"

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


        if str(result).lower() in ["1","yes","approved"]:

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
❌ ADMISSION REJECTED

The student admission probability is low.

Prediction Result:
❌ Not Approved

Algorithm:
Random Forest Classifier
"""


    except Exception as e:

        return f"Prediction Error:\n{e}"



# ==========================================================
# CSS Styling
# ==========================================================

css = """

body{

background-image:
url("https://images.unsplash.com/photo-1562774053-701939374585");

background-size:cover;

background-attachment:fixed;

}


/* Main container */

.gradio-container{

background:rgba(255,255,255,0.92);

border-radius:20px;

padding:25px;

color:black !important;

}


/* All text black */

*{

color:black !important;

}


input, textarea, select{

color:black !important;

background:white !important;

}


/* Developer Information Box */

#developer{

background:white;

border-radius:15px;

padding:20px;

height:220px;

overflow-y:auto;

font-size:16px;

}



/* Horizontal Input Layout */

.gr-row{

display:flex;

flex-wrap:wrap;

gap:15px;

}


footer{

display:none;

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

<b>College:</b> Panipat Institute of Engineering and Technology<br>

<b>Project:</b> College Admission Prediction using Machine Learning<br>


<hr>


<h3>Technology Used</h3>

Python | Pandas | Scikit-Learn | Random Forest | Joblib | Gradio


<hr>


<h3>About Project</h3>

This AI based system predicts admission approval
based on academic records, entrance scores,
college preferences and student details.


</div>

"""



# ==========================================================
# Interface
# ==========================================================


with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:


    gr.HTML(header)


    gr.Markdown(
        """
        ## 📝 Enter Student Details
        """
    )


    with gr.Row():

        Age = gr.Number(label="Age")

        Category = gr.Dropdown(
            ["General","OBC","SC","ST"],
            label="Category"
        )

        Family_Income = gr.Number(
            label="Family Income (₹)"
        )



    with gr.Row():

        Class10 = gr.Number(
            label="Class 10 %"
        )

        Class12 = gr.Number(
            label="Class 12 %"
        )

        PCM = gr.Number(
            label="PCM %"
        )



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



    with gr.Row():

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



    with gr.Row():

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



    with gr.Row():

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



    with gr.Row():

        Hostel = gr.Dropdown(
            ["Yes","No"],
            label="Hostel Required"
        )

        Probability = gr.Number(
            label="Admission Probability"
        )

        Fee = gr.Number(
            label="Tuition Fee (₹)"
        )


    button = gr.Button(
        "🎯 Predict Admission"
    )


    output = gr.Textbox(
        label="Prediction Result",
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
# Render Deployment
# ==========================================================

if __name__=="__main__":

    demo.launch(

        server_name="0.0.0.0",

        server_port=int(
            os.environ.get("PORT",7860)
        )

    )
