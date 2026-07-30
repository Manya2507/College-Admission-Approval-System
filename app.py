# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# PART 1
# IMPORTS + MODEL + IMAGE LOADING + PREDICTION
# ==========================================================


import os
import base64
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
# LOAD BACKGROUND IMAGES
# FROM IMAGES FOLDER
# ==========================================================


def load_background_images():

    image_names = [

    "images (1).jpg",
    "images (2).jpg",
    "images(3).jpg",
    "images(4).jpg",
    "images(5).jpg"

]
    images=[]

    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )

    image_folder = os.path.join(
        BASE_DIR,
        "images"
    )

    print("Image Folder Location:")
    print(image_folder)


    if not os.path.exists(image_folder):

        raise Exception(
            "Images folder not found"
        )


    print(
        "Files inside images folder:"
    )

    print(
        os.listdir(image_folder)
    )


    for img in image_names:

        path = os.path.join(
            image_folder,
            img
        )


        if os.path.exists(path):

            with open(path,"rb") as f:

                images.append(
                    base64.b64encode(
                        f.read()
                    ).decode()
                )

            print(
                "Loaded:",
                img
            )

        else:

            print(
                "Missing:",
                img
            )


    return images




BACKGROUND_IMAGES = load_background_images()



print(
    "Total Images Loaded:",
    len(BACKGROUND_IMAGES)
)



if len(BACKGROUND_IMAGES) == 0:


    raise Exception(
        "No images found. Upload images folder with jpg files."
    )





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
            "❌ Model not loaded",
            0
        )



    try:



        input_data = pd.DataFrame([{


            "Age":Age,


            "Category":Category,


            "Family_Income":Family_Income,


            "Class10_%":Class10_Percentage,


            "Class12_%":Class12_Percentage,


            "PCM_%":PCM_Percentage,


            "Entrance_Exam":Entrance_Exam,


            "JEE_Percentile":JEE_Percentile,


            "JEE_Rank":JEE_Rank,


            "CUET_Score":CUET_Score,


            "Preferred_Branch":Preferred_Branch,


            "Preferred_College":Preferred_College,


            "College_Type":College_Type,


            "NIRF_Rank":NIRF_Rank,


            "College_Tier":College_Tier,


            "Branch_Cutoff_Rank":Branch_Cutoff_Rank,


            "Available_Seats":Available_Seats,


            "Reservation_Quota":Reservation_Quota,


            "Documents_Verified":Documents_Verified,


            "Interview_Score":Interview_Score,


            "Communication_Score":Communication_Score,


            "Aptitude_Score":Aptitude_Score,


            "Scholarship_Applied":Scholarship_Applied,


            "Scholarship_Eligibility":Scholarship_Eligibility,


            "Hostel_Required":Hostel_Required,


            "Admission_Probability":Admission_Probability,


            "Tuition_Fee":Tuition_Fee


        }])





        prediction = model.predict(input_data)[0]





        # Probability Calculation

        try:


            probability = model.predict_proba(
                input_data
            )[0][1]


            probability = round(
                probability * 100,
                2
            )


        except:


            probability = 0






        if str(prediction).lower() in [

            "1",

            "yes",

            "approved"

        ]:


            result = f"""

🎉 ADMISSION APPROVED


📊 Admission Probability:

{probability}%


🟢 Chance Level:

HIGH


🤖 Model Used:

Random Forest Classifier


"""


        else:


            result = f"""

❌ ADMISSION NOT APPROVED


📊 Admission Probability:

{probability}%


🔴 Chance Level:

LOW


🤖 Model Used:

Random Forest Classifier


"""



        return result, probability





    except Exception as e:


        return (

            f"❌ Prediction Error\n\n{e}",

            0

        )
# ==========================================================
# PART 2
# COMPLETE CSS DESIGN
# ==========================================================


css = f"""



/* ==================================================
   FULL SCREEN BACKGROUND SLIDESHOW
================================================== */


.gradio-container {{

    min-height:100vh !important;

    width:100% !important;


    background-size:cover !important;

    background-position:center !important;

    background-repeat:no-repeat !important;


    background-attachment:fixed !important;


    animation:backgroundSlide 120s infinite ease-in-out;


    background-image:

    linear-gradient(

        rgba(0,0,0,0.45),

        rgba(0,0,0,0.45)

    ),

    url(

    "data:image/jpg;base64,{BACKGROUND_IMAGES[0]}"

    );

}}




/* ==================================================
   BACKGROUND IMAGE CHANGE
================================================== */


@keyframes backgroundSlide {{



0% {{

background-image:

linear-gradient(

rgba(0,0,0,0.45),

rgba(0,0,0,0.45)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[0]}"

);

}}




20% {{

background-image:

linear-gradient(

rgba(0,0,0,0.45),

rgba(0,0,0,0.45)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[1]}"

);

}}




40% {{

background-image:

linear-gradient(

rgba(0,0,0,0.45),

rgba(0,0,0,0.45)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[2]}"

);

}}




60% {{

background-image:

linear-gradient(

rgba(0,0,0,0.45),

rgba(0,0,0,0.45)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[3]}"

);

}}




80% {{

background-image:

linear-gradient(

rgba(0,0,0,0.45),

rgba(0,0,0,0.45)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[4]}"

);

}}




100% {{

background-image:

linear-gradient(

rgba(0,0,0,0.45),

rgba(0,0,0,0.45)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[0]}"

);

}}



}}







/* ==================================================
   REMOVE WHITE BACKGROUND BOXES
================================================== */


#main-container,


.gradio-container .block,


.gradio-container .form,


.gradio-container .panel {{


    background:transparent !important;


    border:none !important;


    box-shadow:none !important;


}}







/* ==================================================
   HERO SECTION
================================================== */


.hero-section {{


    text-align:center;


    padding:30px;


    background:transparent !important;


}}





.hero-section h1 {{


    font-size:50px;


    font-weight:900;


    color:white !important;


    text-shadow:

    4px 4px 15px black;


}}





.hero-section h2 {{


    font-size:28px;


    color:#00ffcc !important;


    text-shadow:

    3px 3px 10px black;


}}





.hero-section p {{


    color:white !important;


    font-size:20px;


    text-shadow:

    2px 2px 8px black;


}}







/* ==================================================
   STATISTICS CARDS
================================================== */


.stats {{


    display:flex;


    justify-content:center;


    gap:25px;


    flex-wrap:wrap;


    margin:30px;


}}




.stats div {{


    background:

    rgba(0,0,0,0.45);


    padding:15px 25px;


    border-radius:20px;


    border:

    1px solid white;


    backdrop-filter:blur(8px);


}}





.stats h3 {{


    color:#00ffcc !important;


    font-size:28px;


}}








/* ==================================================
   FEATURE BUTTONS
================================================== */


.feature-box {{


    display:flex;


    justify-content:center;


    flex-wrap:wrap;


    gap:15px;


}}





.feature-box span {{


    background:

    rgba(0,0,0,0.45);


    color:white !important;


    padding:12px 20px;


    border-radius:30px;


    border:

    1px solid white;


    font-size:16px;


    backdrop-filter:blur(10px);


}}









/* ==================================================
   DEVELOPER DETAILS
================================================== */


.developer {{


    margin-top:35px;


    text-align:center;


}}





.developer h3 {{


    color:#00ffcc !important;


    font-size:28px;


}}





.developer p {{


    color:white !important;


    font-size:18px;


    text-shadow:

    2px 2px 8px black;


}}








/* ==================================================
   SECTION HEADINGS
================================================== */


h1,h2,h3 {{


    text-shadow:

    2px 2px 8px black;


}}







/* ==================================================
   INPUT DESIGN
================================================== */


input,

textarea,

select {{


    background:

    rgba(255,255,255,0.85)

    !important;


    color:black !important;


    border-radius:12px !important;


    border:

    2px solid #00ffcc !important;


}}





label {{


    color:white !important;


    font-weight:bold !important;


    text-shadow:

    2px 2px 5px black;


}}







/* ==================================================
   BUTTON DESIGN
================================================== */


button {{


    background:

    linear-gradient(

    135deg,

    #059669,

    #00ffcc

    ) !important;



    color:white !important;


    font-size:20px !important;


    font-weight:bold !important;


    border-radius:20px !important;


    padding:15px !important;


}}




button:hover {{


    transform:scale(1.05);


    transition:0.3s;


}}







/* ==================================================
   OUTPUT DESIGN
================================================== */


textarea {{


    font-size:18px !important;


    font-weight:bold !important;


}}







/* ==================================================
   HIDE FOOTER
================================================== */


footer {{


display:none !important;


}}



"""
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


    gr.HTML(header)


    # all input fields here


    predict_button = gr.Button(
        "🎯 Predict Admission"
    )


    output = gr.Textbox()


    probability_gauge = gr.Slider(
        minimum=0,
        maximum=100
    )


    # ✅ PASTE HERE

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
            Probability,
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
