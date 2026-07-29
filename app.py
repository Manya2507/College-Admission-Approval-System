import os
import joblib
import pandas as pd
import gradio as gr



# ==========================================================
# LOAD MODEL
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


            "Scholarship_Eligibility":
            Scholarship_Eligibility,


            "Hostel_Required":Hostel_Required,


            "Admission_Probability":
            Admission_Probability,


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


        return f"❌ Prediction Error:\n{e}"






# ==========================================================
# FINAL CSS WITH WORKING BACKGROUND SLIDESHOW
# ==========================================================


css = """



/* ===============================
   REMOVE DEFAULT GRADIO BACKGROUND
================================ */


html,
body{

margin:0;

padding:0;

background:transparent !important;

}





.gradio-container{


background:transparent !important;


}



/* ===============================
   BACKGROUND SLIDESHOW
================================ */



body::before{


content:"";


position:fixed;


top:0;

left:0;



width:100vw;


height:100vh;



z-index:-10;



background-size:cover;


background-position:center;



animation:bgSlide 20s infinite;



}





@keyframes bgSlide{


0%{


background-image:url('/gradio_api/file=images/college-img-1.jpg');


}



25%{


background-image:url('/gradio_api/file=images/images (2).jpg');


}



50%{


background-image:url('/gradio_api/file=images/images (3).jpg');


}



75%{


background-image:url('/gradio_api/file=images/images (4).jpg');


}



100%{


background-image:url('/gradio_api/file=images/college-img-1.jpg');


}



}





/* Dark transparent overlay */


body::after{


content:"";


position:fixed;


top:0;

left:0;


width:100vw;


height:100vh;



background:rgba(0,0,0,0.25);



z-index:-5;


}






/* ===============================
   MAIN GLASS CONTAINER
================================ */



#main-container{


width:90%;


max-width:1200px;



margin:30px auto;



padding:30px;



background:rgba(255,255,255,0.45);



backdrop-filter:blur(12px);



border-radius:25px;



box-shadow:

0 10px 40px rgba(0,0,0,0.4);



}





#main-container *{


color:black !important;


}





button{


background:#087f5b !important;


color:white !important;


font-weight:bold !important;


border-radius:12px !important;


}





footer{


display:none !important;


}


"""
# ==========================================================
# HEADER SECTION
# ==========================================================

header = """

<div style="

text-align:center;

padding:25px;

background:rgba(255,255,255,0.35);

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

This AI-based system predicts admission approval
using student academic details, entrance scores,
college preferences and other admission factors.

</p>


</div>

"""





# ==========================================================
# CREATE GRADIO APP
# ==========================================================


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
# 📝 Enter Student Details

Fill all details to predict admission approval.

"""

        )



        # ===============================================
        # ROW 1
        # ===============================================


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





        # ===============================================
        # ROW 2
        # ===============================================


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





        # ===============================================
        # ROW 3
        # ===============================================


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





        # ===============================================
        # ROW 4
        # ===============================================


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





        # ===============================================
        # ROW 5
        # ===============================================


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
                    # ===============================================
        # ROW 6
        # ===============================================


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





        # ===============================================
        # ROW 7
        # ===============================================


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





        # ===============================================
        # ROW 8
        # ===============================================


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





        # ===============================================
        # ROW 9
        # ===============================================


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





        # ===============================================
        # PREDICT BUTTON
        # ===============================================


        predict_button = gr.Button(

            "🎯 Predict Admission",

            variant="primary"

        )





        # ===============================================
        # OUTPUT BOX
        # ===============================================


        output = gr.Textbox(

            label="🎓 Admission Prediction Result",

            lines=8

        )
                # ===============================================
        # CONNECT BUTTON WITH FUNCTION
        # ===============================================


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

            "❌ Images folder not found"

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
