# =====================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# PART 1 : IMPORTS + MODEL + IMAGE HANDLING + PREDICTION
# =====================================================


import os
import base64
import joblib
import pandas as pd
import gradio as gr



# =====================================================
# LOAD MACHINE LEARNING MODEL
# =====================================================


MODEL_PATH = "college_admission_approval.pkl"


try:

    model = joblib.load(MODEL_PATH)

    print("✅ Admission Model Loaded Successfully")


except Exception as e:

    print("❌ Model Loading Error:", e)

    model = None





# =====================================================
# LOAD BACKGROUND IMAGES SAFELY
# Render Compatible
# =====================================================


def load_background_images():


    image_order = [

        "1.jpg",
        "2.jpg",
        "3.jpg",
        "4.jpg",
        "5.jpg"

    ]


    images = []


    base_dir = os.path.dirname(
        os.path.abspath(__file__)
    )


    image_folder = os.path.join(
        base_dir,
        "images"
    )



    for img in image_order:


        path = os.path.join(
            image_folder,
            img
        )


        if os.path.exists(path):


            try:

                with open(
                    path,
                    "rb"
                ) as file:


                    encoded = base64.b64encode(
                        file.read()
                    ).decode()


                    images.append(encoded)


                    print(
                        "✅ Loaded:",
                        img
                    )


            except Exception as e:


                print(
                    "Image Error:",
                    e
                )


        else:


            print(
                "⚠️ Image not found:",
                path
            )



    return images





BACKGROUND_IMAGES = load_background_images()



print(
    "Total Images Loaded:",
    len(BACKGROUND_IMAGES)
)



# Default blank background if images missing

if len(BACKGROUND_IMAGES) == 0:


    BACKGROUND_IMAGES = [

        ""

    ]





# =====================================================
# PREDICTION FUNCTION
# =====================================================


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



        prediction = model.predict(
            input_data
        )[0]




        if str(prediction).lower() in [

            "1",

            "yes",

            "approved"

        ]:


            return """

🎉 ADMISSION APPROVED


Student has a high chance of getting admission.


Algorithm Used:
Random Forest Classifier


"""


        else:


            return """

❌ ADMISSION NOT APPROVED


Student has a low chance of admission.


Algorithm Used:
Random Forest Classifier


"""



    except Exception as e:


        return f"""

❌ Prediction Error


{e}

"""
# =====================================================
# PART 2 : CSS DESIGN
# =====================================================


if len(BACKGROUND_IMAGES) >= 5:

    img1 = BACKGROUND_IMAGES[0]
    img2 = BACKGROUND_IMAGES[1]
    img3 = BACKGROUND_IMAGES[2]
    img4 = BACKGROUND_IMAGES[3]
    img5 = BACKGROUND_IMAGES[4]

else:

    img1 = img2 = img3 = img4 = img5 = ""




css = f"""



/* =====================================================
   FULL PAGE BACKGROUND
===================================================== */


.gradio-container {{


    min-height:100vh !important;


    width:100% !important;


    background-size:cover !important;


    background-position:center !important;


    background-attachment:fixed !important;


    animation:backgroundChange 25s infinite;


    background-image:

    linear-gradient(

        rgba(0,0,0,0.35),

        rgba(0,0,0,0.35)

    ),

    url(

    "data:image/jpg;base64,{img1}"

    );



}}






/* =====================================================
   BACKGROUND SLIDESHOW
===================================================== */


@keyframes backgroundChange {{



0% {{


background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{img1}"

);


}}



20% {{


background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{img2}"

);


}}



40% {{


background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{img3}"

);


}}



60% {{


background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{img4}"

);


}}



80% {{


background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{img5}"

);


}}



100% {{


background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{img1}"

);


}}


}}







/* =====================================================
   MAIN GLASS CONTAINER
===================================================== */


#main-container {{


    width:90% !important;


    max-width:1200px !important;


    margin:40px auto !important;


    padding:35px !important;


    background:

    rgba(

    255,

    255,

    255,

    0.85

    ) !important;



    border-radius:30px !important;


    backdrop-filter:blur(15px) !important;


    -webkit-backdrop-filter:blur(15px) !important;


    box-shadow:

    0px 15px 40px

    rgba(0,0,0,0.4);



}}







/* =====================================================
   HEADER BOX
===================================================== */


#header-box {{


    text-align:center;


    padding:25px;


    background:

    rgba(

    255,

    255,

    255,

    0.90

    );


    border-radius:25px;


    border-left:

    8px solid

    #059669;



}}



#header-box h1 {{


    color:#064e3b !important;


    font-size:40px !important;


    font-weight:900;



}}




#header-box h2 {{


    color:#047857 !important;


}}



#header-box h3 {{


    color:#065f46 !important;


}}




#header-box p {{


    color:#111827 !important;


    font-size:17px;



}}






/* =====================================================
   MARKDOWN TEXT
===================================================== */


.markdown-text {{


    color:#064e3b !important;


    font-weight:bold;



}}







/* =====================================================
   INPUT BOXES
===================================================== */


input,

textarea,

select {{


    background:

    white !important;


    color:black !important;


    border:

    2px solid

    #10b981 !important;


    border-radius:12px !important;



}}







label {{


    color:#064e3b !important;


    font-weight:bold !important;



}}







/* =====================================================
   BUTTON
===================================================== */


button {{


    background:

    linear-gradient(

    135deg,

    #065f46,

    #10b981

    ) !important;



    color:white !important;


    font-size:20px !important;


    font-weight:bold !important;


    border-radius:15px !important;


    padding:12px !important;



}}





button:hover {{


    transform:scale(1.05);


    transition:0.3s;



}}







/* =====================================================
   OUTPUT BOX
===================================================== */


textarea {{


    font-size:18px !important;


    font-weight:bold !important;


}}






/* =====================================================
   REMOVE FOOTER
===================================================== */


footer {{


display:none !important;


}}



"""
# =====================================================
# PART 3 : GRADIO USER INTERFACE
# =====================================================



header = """

<div id="header-box">


<h1>
🎓 AI College Admission Approval System
</h1>


<h2>
Machine Learning Based Admission Prediction Platform
</h2>


<hr>


<h3>
👩‍💻 Developer Details
</h3>


<p>
<b>Name:</b> Manya Singla
</p>


<p>
<b>College:</b> Panipat Institute of Engineering and Technology
</p>


<p>
<b>Project:</b> College Admission Prediction using Machine Learning
</p>



<hr>


<h3>
💻 Technologies Used
</h3>


<p>
Python | Pandas | Scikit-Learn |
Random Forest | Joblib | Gradio
</p>



<hr>


<p>

🤖 AI system predicts admission approval
based on academic performance,
entrance exam scores,
college preference and student details.

</p>


</div>

"""





# =====================================================
# CREATE GRADIO BLOCKS
# =====================================================


with gr.Blocks(

    css=css,

    title="AI College Admission Approval System"

) as demo:



    with gr.Column(

        elem_id="main-container"

    ):



        gr.HTML(header)



        gr.Markdown(
"""
## 📝 Enter Student Details

Fill all details and click Predict Admission.
"""
        )



        # ==============================
        # BASIC DETAILS
        # ==============================


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




        # ==============================
        # ACADEMIC DETAILS
        # ==============================


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





        # ==============================
        # COLLEGE DETAILS
        # ==============================


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






        # ==============================
        # VERIFICATION DETAILS
        # ==============================


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





        # ==============================
        # ADDITIONAL DETAILS
        # ==============================


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





        # ==============================
        # PREDICT BUTTON
        # ==============================


        predict_button = gr.Button(

            "🎯 Predict Admission",

            variant="primary"

        )





        output = gr.Textbox(

            label="🎓 Admission Prediction Result",

            lines=8

        )
# =====================================================
# PART 4 : BUTTON CONNECTION
# =====================================================


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


            outputs=output

        )
