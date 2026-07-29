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
# PART 2/4
# SAFE CSS + BACKGROUND SLIDESHOW
# ==========================================================


img1 = BACKGROUND_IMAGES[0]
img2 = BACKGROUND_IMAGES[1]
img3 = BACKGROUND_IMAGES[2]
img4 = BACKGROUND_IMAGES[3]
img5 = BACKGROUND_IMAGES[4]



css = """



/* ===============================
FULL SCREEN BACKGROUND
================================ */


html,
body,
.gradio-container {


    min-height:100vh !important;

    width:100% !important;


    background:

    linear-gradient(
        rgba(0,0,0,0.45),
        rgba(0,0,0,0.45)
    ),

    url("IMAGE1");


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





/* ===============================
SLOW IMAGE CHANGE
================================ */


@keyframes backgroundSlide {



0% {


background:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE1");

}



20% {


background:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE2");

}



40% {


background:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE3");

}



60% {


background:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE4");

}



80% {


background:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE5");

}



100% {


background:

linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),

url("IMAGE1");

}


}





/* ===============================
REMOVE DEFAULT GRADIO BACKGROUND
================================ */


.gradio-container {


background:transparent !important;


}







/* ===============================
NO WHITE / GREY BOX
================================ */


.block,
.form,
.panel {


background:transparent !important;

border:none !important;

box-shadow:none !important;


}





/* ===============================
MAIN CONTENT
================================ */


#main-container {


width:95% !important;

margin:auto !important;

padding:20px !important;


background:transparent !important;


border:none !important;


box-shadow:none !important;


}





/* ===============================
TEXT VISIBILITY
================================ */


h1,
h2,
h3,
p,
label,
span {


color:white !important;


text-shadow:

2px 2px 6px black !important;


}






/* ===============================
TITLE STYLE
================================ */


#title {


text-align:center !important;


font-size:45px !important;


font-weight:900 !important;


color:white !important;


text-shadow:

3px 3px 8px black !important;


}







/* ===============================
BUTTON DESIGN
================================ */


button {


background:

linear-gradient(

135deg,

#059669,

#10b981

) !important;



color:white !important;


font-weight:bold !important;


font-size:16px !important;


border-radius:15px !important;


border:none !important;


padding:12px !important;



box-shadow:

0px 5px 15px rgba(0,0,0,0.5);



}





button:hover {


transform:scale(1.05);


transition:0.3s;


}






/* ===============================
INPUT BOXES
================================ */


input,
textarea,
select {


background:

rgba(255,255,255,0.85)

!important;



color:black !important;


border-radius:12px !important;


border:

2px solid #10b981 !important;


}





/* ===============================
HIDE FOOTER
================================ */


footer {


display:none !important;


}


"""





# ==========================================================
# INSERT IMAGES
# ==========================================================


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
# PART 3/4
# COMPLETE GRADIO INTERFACE
# EVERYTHING INSIDE ONE BLOCKS
# ==========================================================



with gr.Blocks(

    css=css,

    title="AI College Admission Approval System"

) as demo:



    # ======================================================
    # HEADER
    # ======================================================


    gr.HTML(

"""
<div id="title">

🎓 AI College Admission Approval System

<br>

<span style="font-size:22px">

Smart AI Based Admission Prediction

</span>

<br>

<span style="font-size:16px">

Developed by Manya

</span>

</div>

"""

    )




    gr.Markdown(

"""
### Select a section to enter student details
"""

    )




    # ======================================================
    # SECTION BUTTONS
    # ======================================================


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



    with gr.Row():


        verification_btn = gr.Button(

            "✅ Verification Details"

        )


        scholarship_btn = gr.Button(

            "💰 Scholarship Details"

        )







    # ======================================================
    # ACADEMIC DETAILS
    # ======================================================


    with gr.Group(
        visible=False
    ) as academic_section:



        gr.Markdown(
            "## 📚 Academic Details"
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
    # ENTRANCE DETAILS
    # ======================================================


    with gr.Group(
        visible=False
    ) as entrance_section:



        gr.Markdown(

            "## 🎯 Entrance Exam Details"

        )



        with gr.Row():



            Entrance = gr.Textbox(

                label="Entrance Exam Name"

            )


            JEE = gr.Number(

                label="JEE Percentile"

            )


            Rank = gr.Number(

                label="Entrance Rank"

            )



        with gr.Row():


            CUET = gr.Number(

                label="CUET Score"

            )







    # ======================================================
    # COLLEGE PREFERENCE
    # ======================================================


    with gr.Group(
        visible=False
    ) as college_section:



        gr.Markdown(

            "## 🏫 College Preference Details"

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

                label="Cutoff Rank"

            )



        with gr.Row():


            Seats = gr.Number(

                label="Available Seats"

            )


            Quota = gr.Textbox(

                label="Reservation Quota"

            )








    # ======================================================
    # VERIFICATION DETAILS
    # ======================================================


    with gr.Group(
        visible=False
    ) as verification_section:



        gr.Markdown(

            "## ✅ Verification Details"

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
    # SCHOLARSHIP DETAILS
    # ======================================================


    with gr.Group(
        visible=False
    ) as scholarship_section:



        gr.Markdown(

            "## 💰 Scholarship Details"

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


            Previous_Probability = gr.Number(

                label="Previous Admission Probability"

            )


            Fee = gr.Number(

                label="Tuition Fee (₹)"

            )







    # ======================================================
    # PREDICTION AREA
    # ======================================================



    gr.Markdown(

"""
## 🚀 Final Prediction

"""

    )



    predict_button = gr.Button(

        "🚀 Predict Admission",

        variant="primary"

    )



    output = gr.Textbox(

        label="Prediction Result",

        lines=6

    )



    probability_gauge = gr.Slider(

        minimum=0,

        maximum=100,

        value=0,

        label="📊 Admission Probability (%)"

    )
# ==========================================================
# PART 4/4
# BUTTON EVENTS + MODEL CONNECTION + RENDER LAUNCH
# ==========================================================



# ==========================================================
# SECTION BUTTON ACTIONS
# ==========================================================


academic_btn.click(

    fn=lambda: gr.update(
        visible=True
    ),

    outputs=academic_section

)



entrance_btn.click(

    fn=lambda: gr.update(
        visible=True
    ),

    outputs=entrance_section

)



college_btn.click(

    fn=lambda: gr.update(
        visible=True
    ),

    outputs=college_section

)



verification_btn.click(

    fn=lambda: gr.update(
        visible=True
    ),

    outputs=verification_section

)



scholarship_btn.click(

    fn=lambda: gr.update(
        visible=True
    ),

    outputs=scholarship_section

)





# ==========================================================
# PREDICTION BUTTON CONNECTION
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






# ==========================================================
# END OF BLOCKS
# ==========================================================



# ==========================================================
# RENDER LAUNCH
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
