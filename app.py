# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# PART 1/5
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

    print("✅ Model Loaded Successfully")


except Exception as e:

    print("❌ Model Loading Error:", e)

    model = None




# ==========================================================
# LOAD BACKGROUND IMAGES
# ==========================================================


def load_background_images():


    BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
    )


    image_folder = os.path.join(
        BASE_DIR,
        "images"
    )


    print("Image Folder:")
    print(image_folder)



    if not os.path.exists(image_folder):

        raise FileNotFoundError(
            "images folder not found"
        )



    images = []



    files = os.listdir(image_folder)



    print("Files Found:")
    print(files)



    for file in sorted(files):


        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):


            path = os.path.join(

                image_folder,

                file

            )


            with open(

                path,

                "rb"

            ) as image:


                encoded = base64.b64encode(

                    image.read()

                ).decode()



                images.append(encoded)



                print(
                    "Loaded:",
                    file
                )



    if len(images) == 0:


        raise Exception(
            "No images found inside images folder"
        )



    print(
        "Total Images Loaded:",
        len(images)
    )


    return images




BACKGROUND_IMAGES = load_background_images()





# ==========================================================
# TEXT ENCODING
# ==========================================================


def preprocess_data(data):


    mapping = {


        # Category

        "General":0,
        "OBC":1,
        "SC":2,
        "ST":3,


        # College Type

        "Government":0,
        "Private":1,


        # Yes No

        "Yes":1,
        "No":0

    }



    data = data.replace(
        mapping
    )



    return data





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


        return (

            "❌ Model not loaded",

            0

        )



    try:



        input_data = pd.DataFrame([{


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




        input_data = preprocess_data(
            input_data
        )



        prediction = model.predict(
            input_data
        )[0]



        probability = 0



        if hasattr(
            model,
            "predict_proba"
        ):


            probability = (

                model.predict_proba(
                    input_data
                )[0][1]

                * 100

            )



        else:

            probability = Probability




        if str(prediction).lower() in [

            "1",

            "yes",

            "approved"

        ]:


            result = f"""

🎉 ADMISSION APPROVED


Student has high admission chances.


📊 Probability:
{round(probability,2)}%


🤖 Algorithm:
Random Forest Classifier

"""



        else:


            result = f"""

❌ ADMISSION NOT APPROVED


Student has low admission chances.


📊 Probability:
{round(probability,2)}%


🤖 Algorithm:
Random Forest Classifier

"""



        return (

            result,

            probability

        )



    except Exception as e:


        return (

            f"""

❌ Prediction Error


{e}

""",

            0

        )
# ==========================================================
# PART 2/5
# CSS DESIGN + FULL SCREEN BACKGROUND SLIDESHOW
# NO WHITE/GREY CONTAINER
# ==========================================================


css = f"""



/* ======================================================
   FULL SCREEN BACKGROUND
====================================================== */


html,
body,
.gradio-container {{


    min-height:100vh !important;


    width:100% !important;


    background-image:


    linear-gradient(

        rgba(0,0,0,0.45),

        rgba(0,0,0,0.45)

    ),


    url(

    "data:image/jpg;base64,{BACKGROUND_IMAGES[0]}"

    );


    background-size:cover !important;


    background-position:center !important;


    background-repeat:no-repeat !important;


    background-attachment:fixed !important;


    animation:

    backgroundSlide

    120s

    infinite

    ease-in-out;


}






/* ======================================================
   SLOW BACKGROUND SLIDESHOW
====================================================== */


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



}






/* ======================================================
   REMOVE ALL DEFAULT WHITE BACKGROUNDS
====================================================== */


.gradio-container {{


    background:transparent !important;


}






/* ======================================================
   MAIN INTERFACE
   NO BOX BEHIND CONTENT
====================================================== */


#main-container {{


    width:95% !important;


    margin:auto !important;


    padding:25px !important;


    background:transparent !important;


    backdrop-filter:none !important;


    border:none !important;


    box-shadow:none !important;


}






/* ======================================================
   HEADER DIRECTLY ON IMAGE
====================================================== */


#header-box {{


    text-align:center !important;


    padding:20px !important;


    background:transparent !important;


    border:none !important;


    color:white !important;


}






#header-box h1 {{


    font-size:45px !important;


    font-weight:900 !important;


    color:white !important;


    text-shadow:

    3px 3px 8px black;


}




#header-box h2 {{


    font-size:28px !important;


    color:#d1fae5 !important;


    text-shadow:

    3px 3px 8px black;


}




#header-box h3 {{


    color:white !important;


    text-shadow:

    2px 2px 6px black;


}





#header-box p {{


    color:white !important;


    font-size:18px !important;


    text-shadow:

    2px 2px 6px black;


}






/* ======================================================
   ALL TEXT VISIBILITY
====================================================== */


h1,
h2,
h3,
p,
label,
span {{


    text-shadow:

    2px 2px 5px black !important;


}







/* ======================================================
   BUTTON DESIGN
====================================================== */


button {{


    background:


    linear-gradient(

        135deg,

        #059669,

        #10b981

    ) !important;



    color:white !important;


    font-size:17px !important;


    font-weight:bold !important;


    border-radius:15px !important;


    border:none !important;


    padding:12px !important;



    box-shadow:

    0px 5px 15px rgba(0,0,0,0.4);



}



button:hover {{


    transform:scale(1.05);


    transition:0.3s;


}







/* ======================================================
   INPUT BOXES
====================================================== */


input,
textarea,
select {{


    background:

    rgba(

    255,

    255,

    255,

    0.80

    ) !important;



    color:black !important;


    border-radius:12px !important;


    border:

    2px solid #10b981 !important;



}






/* ======================================================
   OUTPUT BOX
====================================================== */


textarea {{


    font-size:18px !important;


    font-weight:bold !important;


}






/* ======================================================
   HIDE FOOTER
====================================================== */


footer {{


    display:none !important;


}


"""
# ==========================================================
# PART 3/5
# DASHBOARD + FEATURE BUTTONS
# ==========================================================



# ==========================================================
# HEADER
# ==========================================================


header = """

<div id="header-box">


<h1>
🎓 AI College Admission Approval System
</h1>


<h2>
Machine Learning Based Admission Prediction Platform
</h2>



<p>

Predict admission approval using academic performance,
entrance exams, college preferences and student profile.

</p>



<hr>



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

<b>Technologies:</b>

Python |
Pandas |
Scikit-Learn |
Random Forest |
Gradio

</p>



</div>

"""






# ==========================================================
# FEATURE INFORMATION FUNCTIONS
# ==========================================================



def show_academic():

    return gr.update(
        visible=True
    )



def show_entrance():

    return gr.update(
        visible=True
    )



def show_college():

    return gr.update(
        visible=True
    )



def show_verification():

    return gr.update(
        visible=True
    )



def show_scholarship():

    return gr.update(
        visible=True
    )






# ==========================================================
# GRADIO APPLICATION START
# ==========================================================



with gr.Blocks(

    css=css,

    title="AI College Admission Approval System"

) as demo:



    gr.HTML(header)




    gr.Markdown(

"""
## 🔍 Select Information Category

Click a button to enter details.
"""
)





# ==========================================================
# FEATURE BUTTON ROW
# ==========================================================



    with gr.Row():



        academic_btn = gr.Button(

            "📚 Academic Analysis"

        )



        entrance_btn = gr.Button(

            "🎯 Entrance Exam Details"

        )



        college_btn = gr.Button(

            "🏫 College Preference"

        )



        verification_btn = gr.Button(

            "✅ Verification Details"

        )



        scholarship_btn = gr.Button(

            "💰 Scholarship Details"

        )






# ==========================================================
# SECTION VISIBILITY CONTROLS
# ==========================================================



    academic_section = gr.Group(

        visible=False

    )



    entrance_section = gr.Group(

        visible=False

    )



    college_section = gr.Group(

        visible=False

    )



    verification_section = gr.Group(

        visible=False

    )



    scholarship_section = gr.Group(

        visible=False

    )




# ==========================================================
# BUTTON CONNECTIONS
# ==========================================================



    academic_btn.click(

        fn=show_academic,

        outputs=academic_section

    )



    entrance_btn.click(

        fn=show_entrance,

        outputs=entrance_section

    )



    college_btn.click(

        fn=show_college,

        outputs=college_section

    )



    verification_btn.click(

        fn=show_verification,

        outputs=verification_section

    )



    scholarship_btn.click(

        fn=show_scholarship,

        outputs=scholarship_section

    )
    # ==========================================================
# PART 4/5
# ALL 27 INPUT FIELDS
# ==========================================================



# ==========================================================
# ACADEMIC DETAILS SECTION
# ==========================================================


with academic_section:


    gr.Markdown(
"""
## 📚 Academic Analysis Details
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





# ==========================================================
# ENTRANCE DETAILS SECTION
# ==========================================================


with entrance_section:



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
# COLLEGE PREFERENCE SECTION
# ==========================================================



with college_section:



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
# VERIFICATION SECTION
# ==========================================================


with verification_section:



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
# SCHOLARSHIP SECTION
# ==========================================================



with scholarship_section:



    gr.Markdown(
"""
## 💰 Scholarship & Additional Details
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
# PREDICTION AREA
# ==========================================================



gr.Markdown(
"""
# 🎓 Admission Prediction
"""
)



predict_button = gr.Button(

    "🚀 Predict Admission",

    variant="primary"

)



output = gr.Textbox(

    label="Prediction Result",

    lines=10

)



probability_gauge = gr.Slider(

    minimum=0,

    maximum=100,

    value=0,

    label="📊 Admission Probability %"

)
# ==========================================================
# PART 5/5
# BUTTON CONNECTION + RENDER LAUNCH
# ==========================================================



# ==========================================================
# PREDICTION BUTTON CONNECTION
# IMPORTANT:
# KEEP THIS INSIDE WITH gr.Blocks()
# ==========================================================



predict_button.click(


    fn=predict_admission,


    inputs=[


        # Academic

        Age,

        Category,

        Family_Income,

        Class10,

        Class12,

        PCM,


        # Entrance

        Entrance,

        JEE,

        Rank,

        CUET,


        # College

        Branch,

        College,

        College_Type,

        NIRF,

        Tier,

        Cutoff,

        Seats,

        Quota,


        # Verification

        Docs,

        Interview,

        Communication,

        Aptitude,


        # Scholarship

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
# RUN APPLICATION
# ==========================================================


if __name__ == "__main__":



    print(
        "🚀 Starting AI College Admission Approval System"
    )



    demo.launch(


        server_name="0.0.0.0",


        server_port=int(

            os.environ.get(

                "PORT",

                7860

            )

        )

    )
