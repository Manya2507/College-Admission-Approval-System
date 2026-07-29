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
# LOAD BACKGROUND IMAGES FOR SLIDESHOW
# =====================================================


def convert_image_to_base64(image_path):

    with open(image_path, "rb") as img:

        return base64.b64encode(
            img.read()
        ).decode()



# =====================================================
# LOAD 5 BACKGROUND IMAGES IN YOUR REQUIRED ORDER
# =====================================================

def load_background_images():

    image_files = [

        "1.jpg",

        "3.jpg",

        "4.jpg",

        "5.jpg",

        "2.jpg"

    ]


    encoded_images = []


    for image in image_files:


        image_path = os.path.join(

            os.path.dirname(__file__),

            "images",

            image

        )


        with open(image_path, "rb") as img:


            encoded_images.append(

                base64.b64encode(

                    img.read()

                ).decode()

            )


    return encoded_images



BACKGROUND_IMAGES = load_background_images()



if len(BACKGROUND_IMAGES) == 4:

    print("✅ All 4 background images loaded")

else:

    print(
        "⚠️ Background images loaded:",
        len(BACKGROUND_IMAGES)
    )





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


        return "❌ Model file not found"




    try:


        data = pd.DataFrame([{


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



        result = model.predict(data)[0]



        if str(result).lower() in [

            "1",

            "yes",

            "approved"

        ]:


            return """

🎉 ADMISSION APPROVED


✅ Student has high probability of admission.


Algorithm:

Random Forest Classifier

"""


        else:


            return """

❌ ADMISSION NOT APPROVED


Student has low probability of admission.


Algorithm:

Random Forest Classifier

"""



    except Exception as e:


        return f"❌ Prediction Error:\n{e}"
# =====================================================
# CSS DESIGN WITH CONTINUOUS BACKGROUND SLIDESHOW
# =====================================================


css = f"""

.gradio-container {{

    min-height:100vh;


    background-size:cover;

    background-position:center;

    background-attachment:fixed;


    background-image:

    linear-gradient(

    rgba(0,0,0,0.35),

    rgba(0,0,0,0.35)

    ),

    url(

    "data:image/jpg;base64,{BACKGROUND_IMAGES[0]}"

    );


    animation:

    backgroundSlide 25s infinite;

}}




@keyframes backgroundSlide {{


0% {{

background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[0]}"

);

}}



20% {{

background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[1]}"

);

}}



40% {{

background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[2]}"

);

}}



60% {{

background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[3]}"

);

}}



80% {{

background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[4]}"

);

}}



100% {{

background-image:

linear-gradient(

rgba(0,0,0,0.35),

rgba(0,0,0,0.35)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[0]}"

);

}}


}}

"""





# =====================================================
# MAIN GLASS CONTAINER
# =====================================================

css = """

#main-container {

    width: 90%;

    max-width: 1250px;

    margin: 35px auto;

    padding: 35px;


    background: rgba(255, 255, 255, 0.65);


    backdrop-filter: blur(15px);

    -webkit-backdrop-filter: blur(15px);


    border-radius: 30px;


    border: 2px solid rgba(255,255,255,0.7);


    box-shadow:

    0 15px 50px rgba(0,0,0,0.5);

}

"""


/* =====================================
   HEADER STYLE
===================================== */


#header-box {{


    text-align:center;


    padding:25px;



    background:

    rgba(

    255,

    255,

    255,

    0.45

    );



    border-radius:25px;


}}





#header-box h1 {{


    font-size:42px;


    font-weight:900;



    color:#064e3b !important;



    animation:

    titleAnimation 3s infinite alternate;


}}





@keyframes titleAnimation {{


from {{

transform:scale(1);

}}


to {{

transform:scale(1.05);

}}


}}





#header-box h2 {{


color:#047857 !important;


}}





#header-box p {{


font-size:17px;


color:#111 !important;


}}





/* =====================================
   INPUT BOXES
===================================== */


input,

textarea,

select {{


    background:

    rgba(

    255,

    255,

    255,

    0.90

    ) !important;



    border:

    2px solid

    #10b981 !important;



    border-radius:12px !important;



    color:black !important;



}}





label {{


color:#064e3b !important;


font-weight:bold !important;


}}





/* =====================================
   BUTTON
===================================== */


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





/* REMOVE GRADIO FOOTER */


footer {{

display:none !important;

}}



"""
# =====================================================
# HEADER / DEVELOPER SECTION
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

🤖 This AI system predicts admission approval using

student academic performance, entrance exam scores,

college preferences and admission-related details.

</p>



</div>

"""





# =====================================================
# CREATE GRADIO APPLICATION
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

Provide complete student information for prediction.

"""

        )




        # ===============================
        # BASIC DETAILS
        # ===============================


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





        # ===============================
        # ACADEMIC DETAILS
        # ===============================


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





        # ===============================
        # COLLEGE DETAILS
        # ===============================


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





        # ===============================
        # VERIFICATION DETAILS
        # ===============================


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





        # ===============================
        # ADDITIONAL DETAILS
        # ===============================


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
# =====================================================
# PREDICTION BUTTON
# =====================================================


        predict_button = gr.Button(

            "🎯 Predict Admission",

            variant="primary"

        )




# =====================================================
# OUTPUT BOX
# =====================================================


        output = gr.Textbox(

            label="🎓 Admission Prediction Result",

            lines=8

        )





# =====================================================
# CONNECT BUTTON WITH MODEL
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





# =====================================================
# RUN APPLICATION FOR RENDER
# =====================================================


if __name__ == "__main__":



    print("🚀 Starting AI College Admission Approval System")



    demo.launch(


        server_name="0.0.0.0",


        server_port=int(


            os.environ.get(

                "PORT",

                7860

            )

        )


    )
