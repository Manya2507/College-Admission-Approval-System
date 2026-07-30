# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# PART 1/3
# IMPORTS + MODEL + IMAGE SLIDESHOW + CSS DESIGN
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
# ==========================================================


def load_images():


    image_folder = os.path.join(

        os.path.dirname(__file__),

        "images"

    )


    image_files = [

        "images (1).jpg",

        "images (2).jpg",

        "images(3).jpg",

        "images(4).jpg",

        "images(5).jpg"

    ]



    encoded_images = []



    print("Image Folder:")

    print(image_folder)



    for img in image_files:


        path = os.path.join(

            image_folder,

            img

        )


        if os.path.exists(path):


            with open(path,"rb") as f:


                encoded_images.append(

                    base64.b64encode(

                        f.read()

                    ).decode()

                )


            print("Loaded:",img)



        else:

            print("Missing:",img)




    return encoded_images






BACKGROUND_IMAGES = load_images()



print(

    "Total Images:",

    len(BACKGROUND_IMAGES)

)



if len(BACKGROUND_IMAGES) < 5:


    print(

        "⚠️ Add 5 images inside images folder"

    )





# ==========================================================
# MODERN AI DASHBOARD CSS
# ==========================================================


css = f"""



/* ================================
   FULL SCREEN BACKGROUND
================================ */



body {{

    overflow-x:hidden;

}}




.gradio-container {{


    min-height:100vh !important;


    background:transparent !important;


}}





.gradio-container::before {{


    content:"";


    position:fixed;


    top:0;


    left:0;


    width:100%;


    height:100%;



    z-index:-1;




    background-size:cover;


    background-position:center;


    background-repeat:no-repeat;




    animation:

    slideshow 60s infinite,

    zoom 20s infinite alternate;



}}







/* ================================
   IMAGE SLIDESHOW
================================ */



@keyframes slideshow {{



0% {{


background-image:

linear-gradient(

rgba(0,0,30,0.55),

rgba(0,0,30,0.55)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[0] if len(BACKGROUND_IMAGES)>0 else ''}"

);



}}




25% {{


background-image:

linear-gradient(

rgba(0,0,30,0.55),

rgba(0,0,30,0.55)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[1] if len(BACKGROUND_IMAGES)>1 else ''}"

);



}}






50% {{


background-image:

linear-gradient(

rgba(0,0,30,0.55),

rgba(0,0,30,0.55)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[2] if len(BACKGROUND_IMAGES)>2 else ''}"

);



}}







75% {{


background-image:

linear-gradient(

rgba(0,0,30,0.55),

rgba(0,0,30,0.55)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[3] if len(BACKGROUND_IMAGES)>3 else ''}"

);



}}






100% {{


background-image:

linear-gradient(

rgba(0,0,30,0.55),

rgba(0,0,30,0.55)

),

url(

"data:image/jpg;base64,{BACKGROUND_IMAGES[4] if len(BACKGROUND_IMAGES)>4 else ''}"

);



}}



}}







@keyframes zoom {{


from {{

background-size:100%;

}}



to {{

background-size:115%;

}}



}}






/* ================================
   REMOVE BOX BACKGROUNDS
================================ */



.block,


.form,


.panel,


fieldset {{


background:

transparent !important;


border:none !important;


box-shadow:none !important;


}}







/* ================================
   TEXT DESIGN
================================ */



h1,h2,h3,p,label {{


color:white !important;


text-shadow:

3px 3px 10px black;


font-weight:bold;


}}







/* ================================
   BUTTON STYLE
================================ */



button {{


background:

linear-gradient(

135deg,

#00c6ff,

#0072ff

)!important;



color:white !important;



font-size:18px !important;



font-weight:bold !important;



border-radius:20px !important;



border:

1px solid white !important;



transition:0.3s;



}}





button:hover {{


transform:scale(1.08);


}}







/* ================================
   INPUT STYLE
================================ */



input,

textarea,

select {{


background:

rgba(255,255,255,0.9)

!important;



color:black !important;



border-radius:12px !important;



border:

2px solid #00e5ff !important;



}}







/* ================================
   HIDE FOOTER
================================ */



footer {{


display:none !important;


}}



"""
# ==========================================================
# PART 2/3
# HORIZONTAL DASHBOARD UI
# ==========================================================




# ==========================================================
# HEADER CONTENT
# ==========================================================


header = """

<div style="text-align:center">


<h1 style="font-size:45px">

🎓 AI College Admission Approval System

</h1>


<h2 style="color:#00ffff">

Machine Learning Based Admission Prediction Platform

</h2>



<p style="font-size:20px">

Predict admission chances using academics,
entrance exams, college preferences and student profile.

</p>



<h3>

👩‍💻 Developer: Manya Singla

</h3>


<p>

Panipat Institute of Engineering and Technology

<br>

Python | Pandas | Scikit-Learn | Random Forest | Gradio

</p>



</div>

"""





# ==========================================================
# CREATE SINGLE GRADIO APPLICATION
# ==========================================================


with gr.Blocks(

    css=css,

    title="AI College Admission Approval System"

) as demo:




    gr.HTML(header)





    # ======================================================
    # FEATURE BUTTON ROW
    # ======================================================



    gr.Markdown(
"""
## 🔍 Admission Analysis Sections
"""
)



    with gr.Row():



        academic_btn = gr.Button(

            "📚 Academic Analysis"

        )


        entrance_btn = gr.Button(

            "🎯 Entrance Analysis"

        )


        college_btn = gr.Button(

            "🏫 College Matching"

        )


        verification_btn = gr.Button(

            "✅ Verification"

        )


        scholarship_btn = gr.Button(

            "💰 Scholarship"

        )






    # ======================================================
    # SECTION 1 - ACADEMIC
    # ======================================================



    with gr.Group(

        visible=True

    ) as academic_section:



        gr.Markdown(
"""
### 📚 Academic Details
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






    # ======================================================
    # SECTION 2 - ENTRANCE
    # ======================================================



    with gr.Group(

        visible=False

    ) as entrance_section:



        gr.Markdown(
"""
### 🎯 Entrance Exam Details
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







    # ======================================================
    # SECTION 3 - COLLEGE
    # ======================================================



    with gr.Group(

        visible=False

    ) as college_section:



        gr.Markdown(
"""
### 🏫 College Preference Details
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








    # ======================================================
    # SECTION 4 - VERIFICATION
    # ======================================================



    with gr.Group(

        visible=False

    ) as verification_section:



        gr.Markdown(
"""
### ✅ Verification & Interview Details
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









    # ======================================================
    # SECTION 5 - SCHOLARSHIP + EXTRA
    # ======================================================



    with gr.Group(

        visible=False

    ) as scholarship_section:



        gr.Markdown(
"""
### 💰 Scholarship & Additional Details
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





    # ======================================================
    # OUTPUT AREA
    # ======================================================



    gr.Markdown(
"""
## 🎓 Admission Prediction Result
"""
)



    with gr.Row():



        predict_button = gr.Button(

            "🚀 Predict Admission",

            variant="primary"

        )



        probability_gauge = gr.Slider(

            minimum=0,

            maximum=100,

            value=0,

            label="📊 Admission Probability %"

        )



    output = gr.Textbox(

        label="Prediction Result",

        lines=8

    )
# ==========================================================
# PART 3/3
# BUTTON EVENTS + PREDICTION + RENDER LAUNCH
# ==========================================================





# ==========================================================
# SECTION BUTTON FUNCTIONS
# ==========================================================


def show_section(section):


    return (


        gr.update(

            visible=section=="academic"

        ),


        gr.update(

            visible=section=="entrance"

        ),


        gr.update(

            visible=section=="college"

        ),


        gr.update(

            visible=section=="verification"

        ),


        gr.update(

            visible=section=="scholarship"

        )

    )







# ==========================================================
# BUTTON CONNECTIONS
# ==========================================================



academic_btn.click(

    lambda:

    show_section("academic"),


    outputs=[

        academic_section,

        entrance_section,

        college_section,

        verification_section,

        scholarship_section

    ]

)




entrance_btn.click(

    lambda:

    show_section("entrance"),


    outputs=[

        academic_section,

        entrance_section,

        college_section,

        verification_section,

        scholarship_section

    ]

)




college_btn.click(

    lambda:

    show_section("college"),


    outputs=[

        academic_section,

        entrance_section,

        college_section,

        verification_section,

        scholarship_section

    ]

)




verification_btn.click(

    lambda:

    show_section("verification"),


    outputs=[

        academic_section,

        entrance_section,

        college_section,

        verification_section,

        scholarship_section

    ]

)




scholarship_btn.click(

    lambda:

    show_section("scholarship"),


    outputs=[

        academic_section,

        entrance_section,

        college_section,

        verification_section,

        scholarship_section

    ]

)






# ==========================================================
# FINAL PREDICTION FUNCTION
# ==========================================================



def final_prediction(


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


            "Scholarship_Eligibility":Scholarship_Eligibility,


            "Hostel_Required":Hostel,


            "Admission_Probability":Probability,


            "Tuition_Fee":Fee


        }])




        prediction = model.predict(data)[0]




        if hasattr(model,"predict_proba"):


            probability = round(

                max(

                    model.predict_proba(data)[0]

                )*100,

                2

            )


        else:


            probability = 0






        if str(prediction).lower() in [

            "approved",

            "yes",

            "1"

        ]:


            result = f"""

🎉 ADMISSION APPROVED


📊 Probability:

{probability}%


🟢 Admission Chance: HIGH


🤖 Model:

Random Forest Classifier

"""



        else:



            result = f"""

❌ ADMISSION NOT APPROVED


📊 Probability:

{probability}%


🔴 Admission Chance: LOW


🤖 Model:

Random Forest Classifier

"""



        return result, probability




    except Exception as e:



        return (

            "❌ Prediction Error:\n\n"+str(e),

            0

        )







# ==========================================================
# PREDICTION BUTTON
# ==========================================================



predict_button.click(


    fn=final_prediction,


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






# ==========================================================
# START APPLICATION
# ==========================================================


if __name__ == "__main__":


    demo.launch(


        server_name="0.0.0.0",


        server_port=int(

            os.environ.get(

                "PORT",

                7860

            )

        ),


        show_error=True

    )
