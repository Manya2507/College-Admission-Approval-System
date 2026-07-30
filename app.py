# ==========================================================
# PART 1/4
# IMPORTS + MODEL + IMAGES + PREDICTION FUNCTION
# ==========================================================


import os
import base64
import joblib
import pandas as pd
import gradio as gr




# ==========================================================
# LOAD MACHINE LEARNING MODEL
# ==========================================================


MODEL_PATH = "college_admission_model.pkl"


try:

    model = joblib.load(MODEL_PATH)

    print("✅ Admission Model Loaded Successfully")


except Exception as e:

    print("❌ Model Loading Error:", e)

    model = None

# ==========================================================
# LOAD BACKGROUND IMAGES
# ==========================================================


IMAGE_FOLDER = "images"


BACKGROUND_IMAGES = []



image_files = [

    "images (1).jpg",
    "images (2).jpg",
    "images(3).jpg",
    "images(4).jpg",
    "images(5).jpg"

]



print("\nImage Folder Location:")

print(
    os.path.abspath(IMAGE_FOLDER)
)



if os.path.exists(IMAGE_FOLDER):


    print(
        "Files inside images folder:"
    )


    print(
        os.listdir(IMAGE_FOLDER)
    )




    for img in image_files:


        path = os.path.join(

            IMAGE_FOLDER,

            img

        )


        if os.path.exists(path):


            with open(
                path,
                "rb"
            ) as file:


                encoded = base64.b64encode(
                    file.read()
                ).decode()



                BACKGROUND_IMAGES.append(
                    encoded
                )


            print(
                "✅ Loaded:",
                img
            )



        else:

            print(
                "⚠️ Missing:",
                img
            )



else:

    print(
        "❌ Images folder not found"
    )




print(
    "Total Images Loaded:",
    len(BACKGROUND_IMAGES)
)





# ==========================================================
# CHECK IMAGES
# ==========================================================


if len(BACKGROUND_IMAGES) < 5:


    raise Exception(

        """
        Minimum 5 images required.

        Upload images folder containing:

        images (1).jpg
        images (2).jpg
        images(3).jpg
        images(4).jpg
        images(5).jpg

        """

    )






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

    Previous_Probability,
    Fee

):



    try:



        if model is None:


            return (

                "❌ Model not loaded",

                0

            )





        input_data = pd.DataFrame({


            "Age":[Age],

            "Category":[Category],

            "Family_Income":[Family_Income],


            "Class10":[Class10],

            "Class12":[Class12],

            "PCM":[PCM],


            "Entrance":[Entrance],

            "JEE":[JEE],

            "Rank":[Rank],

            "CUET":[CUET],


            "Branch":[Branch],

            "College":[College],

            "College_Type":[College_Type],


            "NIRF":[NIRF],

            "Tier":[Tier],

            "Cutoff":[Cutoff],

            "Seats":[Seats],

            "Quota":[Quota],


            "Docs":[Docs],

            "Interview":[Interview],

            "Communication":[Communication],

            "Aptitude":[Aptitude],


            "Scholarship":[Scholarship],

            "Scholarship_Eligibility":[Scholarship_Eligibility],

            "Hostel":[Hostel],


            "Previous_Probability":[Previous_Probability],

            "Fee":[Fee]


        })





        prediction = model.predict(
            input_data
        )[0]



        try:

            probability = model.predict_proba(
                input_data
            )[0][1]


            probability = round(

                probability * 100,

                2

            )


        except:


            probability = Previous_Probability





        if prediction == 1:


            result = (

                "🎉 Admission Approved\n\n"

                "Student has high chances "

                "of getting admission."

            )



        else:


            result = (

                "❌ Admission Not Approved\n\n"

                "Student needs improvement "

                "in profile."

            )




        return result, probability




    except Exception as e:


        return (

            "Prediction Error:\n" + str(e),

            0

        )
# ==========================================================
# PART 2
# BACKGROUND SLIDESHOW CSS
# ==========================================================


img1 = BACKGROUND_IMAGES[0]
img2 = BACKGROUND_IMAGES[1]
img3 = BACKGROUND_IMAGES[2]
img4 = BACKGROUND_IMAGES[3]
img5 = BACKGROUND_IMAGES[4]



css = """

html, body {

    margin:0;
    padding:0;

}


.gradio-container {


    min-height:100vh !important;

    width:100% !important;


    background-color:transparent !important;


}




.gradio-container::before {


    content:"";

    position:fixed;

    top:0;

    left:0;


    width:100%;

    height:100%;


    z-index:-1;


    background-size:cover;

    background-position:center;


    animation:slideBackground 120s infinite;


}




@keyframes slideBackground {



0% {


background-image:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE1");


}



20% {


background-image:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE2");


}



40% {


background-image:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE3");


}



60% {


background-image:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE4");


}



80% {


background-image:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE5");


}



100% {


background-image:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE1");


}


}





/* TEXT DIRECTLY ON IMAGE */


h1,h2,h3,p,label,span {


color:white !important;


text-shadow:

2px 2px 6px black;


}





/* REMOVE WHITE BOX */


.block,
.panel,
.form {


background:transparent !important;

border:none !important;

box-shadow:none !important;


}





button {


background:#059669 !important;

color:white !important;

border-radius:15px !important;

font-weight:bold !important;


}





input,
textarea,
select {


background:rgba(255,255,255,0.85) !important;

color:black !important;


}

"""



css = css.replace(
    "IMAGE1",
    "data:image/jpg;base64," + img1
)

css = css.replace(
    "IMAGE2",
    "data:image/jpg;base64," + img2
)

css = css.replace(
    "IMAGE3",
    "data:image/jpg;base64," + img3
)

css = css.replace(
    "IMAGE4",
    "data:image/jpg;base64," + img4
)

css = css.replace(
    "IMAGE5",
    "data:image/jpg;base64," + img5
)
# ==========================================================
# PART 3
# GRADIO USER INTERFACE
# ==========================================================



# ==========================================================
# HEADER DESIGN
# ==========================================================


header = """

<div class="hero-section">


<h1>
🎓 AI College Admission Approval System
</h1>


<h2>
Machine Learning Based Admission Prediction Platform
</h2>


<p>
Predict college admission chances using academic,
entrance exam and college preference details.
</p>



<div class="stats">


<div>

<h3>
🤖 AI
</h3>

<p>
Powered Prediction
</p>

</div>



<div>

<h3>
98%
</h3>

<p>
Accuracy Target
</p>

</div>




<div>

<h3>
24+
</h3>

<p>
Student Features
</p>

</div>


</div>



<div class="feature-box">


<span>
📚 Academic Analysis
</span>


<span>
🎯 Entrance Exam Evaluation
</span>


<span>
🏫 College Matching
</span>


<span>
💰 Scholarship Analysis
</span>


<span>
📊 Admission Probability
</span>


</div>



<div class="developer">


<h3>
👩‍💻 Developer Details
</h3>


<p>
<b>Name:</b> Manya Singla
</p>


<p>
<b>College:</b>
Panipat Institute of Engineering and Technology
</p>


<p>
<b>Technology:</b>
Python | Pandas | Scikit-Learn | Random Forest | Gradio
</p>



</div>


</div>


"""





# ==========================================================
# CREATE GRADIO APP
# ==========================================================


with gr.Blocks(

    css=css,

    title="AI College Admission Approval System"

) as demo:



    gr.HTML(header)



    gr.Markdown(

"""
# 📝 Enter Student Information

"""
    )





# ==========================================================
# BASIC DETAILS
# ==========================================================


    gr.Markdown(
"""
## 👤 Student Basic Details
"""
)



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






# ==========================================================
# ACADEMIC DETAILS
# ==========================================================


    gr.Markdown(
"""
## 📚 Academic Performance Details
"""
)



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






# ==========================================================
# ENTRANCE EXAM DETAILS
# ==========================================================


    gr.Markdown(
"""
## 🎯 Entrance Exam Details
"""
)



    with gr.Row():


        Entrance = gr.Textbox(

            label="Entrance Exam Name"

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






# ==========================================================
# COLLEGE PREFERENCE DETAILS
# ==========================================================


    gr.Markdown(
"""
## 🏫 College Preference Details
"""
)



    with gr.Row():


        Branch = gr.Textbox(

            label="Preferred Branch"

        )


        College = gr.Textbox(

            label="Preferred College"

        )


        College_Type = gr.Dropdown(

            choices=[

                "Government",

                "Private"

            ],

            label="College Type"

        )





    with gr.Row():


        NIRF = gr.Number(

            label="NIRF Rank"

        )


        Tier = gr.Number(

            label="College Tier"

        )


        Cutoff = gr.Number(

            label="Branch Cutoff Rank"

        )





    with gr.Row():


        Seats = gr.Number(

            label="Available Seats"

        )


        Quota = gr.Textbox(

            label="Reservation Quota"

        )






# ==========================================================
# VERIFICATION DETAILS
# ==========================================================


    gr.Markdown(
"""
## ✅ Verification & Interview Details
"""
)



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






    with gr.Row():


        Aptitude = gr.Number(

            label="Aptitude Score"

        )






# ==========================================================
# EXTRA DETAILS
# ==========================================================


    gr.Markdown(
"""
## 🎓 Additional Student Details
"""
)



    with gr.Row():


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


        Hostel = gr.Dropdown(

            choices=[

                "Yes",

                "No"

            ],

            label="Hostel Required"

        )





    with gr.Row():


        Probability = gr.Number(

            label="Previous Admission Probability"

        )


        Fee = gr.Number(

            label="Tuition Fee (₹)"

        )






# ==========================================================
# BUTTON
# ==========================================================


    predict_button = gr.Button(

        "🎯 Predict Admission",

        variant="primary"

    )





# ==========================================================
# OUTPUT
# ==========================================================


    output = gr.Textbox(

        label="🎓 Prediction Result",

        lines=8

    )





# ==========================================================
# PROBABILITY GAUGE
# ==========================================================


    probability_gauge = gr.Slider(

        minimum=0,

        maximum=100,

        value=0,

        label="📊 Admission Probability %"

    )
# ==========================================================
# PART 4
# BUTTON CONNECTION + RENDER LAUNCH
# ==========================================================



# ==========================================================
# CONNECT BUTTON WITH MODEL
# ==========================================================









# ==========================================================
# START APPLICATION
# ==========================================================


with gr.Blocks(

    css=css,

    title="AI College Admission Approval System"

) as demo:


    # ==========================================================
# BUTTON ACTIONS
# ==========================================================


def show_section():

    return gr.update(
        visible=True
    )



academic_btn.click(

    fn=show_section,

    inputs=None,

    outputs=academic_section

)



entrance_btn.click(

    fn=show_section,

    inputs=None,

    outputs=entrance_section

)



college_btn.click(

    fn=show_section,

    inputs=None,

    outputs=college_section

)



verification_btn.click(

    fn=show_section,

    inputs=None,

    outputs=verification_section

)



scholarship_btn.click(

    fn=show_section,

    inputs=None,

    outputs=scholarship_section

)





# ==========================================================
# PREDICTION BUTTON
# ==========================================================


predict_button.click(

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

        Previous_Probability,
        Fee

    ],


    outputs=[

        output,

        probability_gauge

    ]

)
# keep this outside

if __name__ == "__main__":

    demo.launch(
        server_name="0.0.0.0",
        server_port=int(
            os.environ.get(
                "PORT",
                7860
            )
        )
    )
