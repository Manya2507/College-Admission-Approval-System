# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# PART 1/6
# IMPORTS + MODEL LOADING + IMAGE LOADING
# ==========================================================


import os
import base64
import joblib
import pandas as pd
import gradio as gr





# ==========================================================
# MODEL PATH
# CHANGE ONLY THIS NAME IF YOUR FILE NAME IS DIFFERENT
# ==========================================================


MODEL_PATH = "admission_model.pkl"



try:

    model = joblib.load(MODEL_PATH)

    print("✅ Model Loaded Successfully")


except Exception as e:

    print("❌ Model Loading Error:", e)

    model = None






# ==========================================================
# IMAGE FOLDER
# ==========================================================


IMAGE_FOLDER = "images"



BACKGROUND_IMAGES = []





# Automatically load all jpg images
# No need to rename images


if os.path.exists(IMAGE_FOLDER):


    print("\nImages Found:")


    for file in os.listdir(IMAGE_FOLDER):


        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):


            image_path = os.path.join(

                IMAGE_FOLDER,

                file

            )


            with open(

                image_path,

                "rb"

            ) as img:


                encoded_image = base64.b64encode(

                    img.read()

                ).decode()



                BACKGROUND_IMAGES.append(

                    encoded_image

                )


            print(
                "✅ Loaded:",
                file
            )



else:


    print(
        "❌ images folder not found"
    )





print(

    "Total Images Loaded:",

    len(BACKGROUND_IMAGES)

)





# ==========================================================
# CHECK IMAGES
# ==========================================================


if len(BACKGROUND_IMAGES) == 0:


    raise Exception(

        """

        No images found.

        Create an images folder and add jpg images.

        Example:

        images/
            image1.jpg
            image2.jpg
            image3.jpg
            image4.jpg
            image5.jpg

        """

    )





# Keep minimum 5 images
# If more images exist they will also work


while len(BACKGROUND_IMAGES) < 5:


    BACKGROUND_IMAGES.append(

        BACKGROUND_IMAGES[0]

    )





# ==========================================================
# BASIC PREDICTION FUNCTION
# (Final connection will be added in Part 6)
# ==========================================================


def predict_admission(data):


    try:


        if model is None:


            return (

                "❌ Model not loaded",

                0

            )



        prediction = model.predict(

            data

        )[0]



        probability = 0



        if hasattr(

            model,

            "predict_proba"

        ):


            probability = round(

                max(

                    model.predict_proba(data)[0]

                )

                * 100,

                2

            )





        if prediction == 1:


            result = (

                "🎉 Admission Approved"

            )


        else:


            result = (

                "❌ Admission Not Approved"

            )





        return result, probability





    except Exception as e:


        return (

            "Prediction Error: " + str(e),

            0

        )
# ==========================================================
# PART 2/6
# BACKGROUND SLIDESHOW CSS
# ==========================================================



image1 = BACKGROUND_IMAGES[0]
image2 = BACKGROUND_IMAGES[1]
image3 = BACKGROUND_IMAGES[2]
image4 = BACKGROUND_IMAGES[3]
image5 = BACKGROUND_IMAGES[4]





css = f"""

.gradio-container {{
    min-height:100vh !important;
    width:100% !important;
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

    animation: backgroundChange 120s infinite;

}}



@keyframes backgroundChange {{

0% {{

background-image:
linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),
url("data:image/jpg;base64,{image1}");

}}



20% {{

background-image:
linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),
url("data:image/jpg;base64,{image2}");

}}



40% {{

background-image:
linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),
url("data:image/jpg;base64,{image3}");

}}



60% {{

background-image:
linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),
url("data:image/jpg;base64,{image4}");

}}



80% {{

background-image:
linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),
url("data:image/jpg;base64,{image5}");

}}



100% {{

background-image:
linear-gradient(
rgba(0,0,0,0.45),
rgba(0,0,0,0.45)
),
url("data:image/jpg;base64,{image1}");

}}

}}




/* Remove boxes */

.block,
.panel,
.form,
fieldset {{

background:transparent !important;

border:none !important;

box-shadow:none !important;

}}



h1,h2,h3,p,label,span {{

color:white !important;

text-shadow:2px 2px 8px black !important;

}}



button {{

background:
linear-gradient(
135deg,
#00c853,
#00e676
) !important;

color:white !important;

font-weight:bold !important;

border-radius:15px !important;

}}



input,
textarea,
select {{

background:rgba(255,255,255,0.85) !important;

color:black !important;

border-radius:12px !important;

}}

footer {{

display:none !important;

}}

"""# ==========================================================
# PART 3/6
# GRADIO INTERFACE DESIGN
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

    Smart AI Based College Admission Prediction

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

    ### 👇 Click the sections below and enter student details

    """

    )





    # ======================================================
    # SECTION BUTTONS
    # ======================================================


    with gr.Row():


        academic_btn = gr.Button(

            "📚 Academic Details"

        )


        entrance_btn = gr.Button(

            "🎯 Entrance Exam"

        )


        college_btn = gr.Button(

            "🏫 College Preference"

        )



    with gr.Row():


        verification_btn = gr.Button(

            "✅ Verification"

        )


        scholarship_btn = gr.Button(

            "💰 Scholarship"

        )






    # ======================================================
    # ACADEMIC SECTION
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

                label="Family Income"

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



        with gr.Row():


            Graduation = gr.Textbox(

                label="Previous Qualification"

            )


            Backlogs = gr.Number(

                label="Number of Backlogs"

            )





    # ======================================================
    # ENTRANCE SECTION
    # ======================================================


    with gr.Group(

        visible=False

    ) as entrance_section:


        gr.Markdown(

            "## 🎯 Entrance Exam Details"

        )


        with gr.Row():


            Exam_Name = gr.Textbox(

                label="Entrance Exam Name"

            )


            Exam_Score = gr.Number(

                label="Entrance Score"

            )


            Rank = gr.Number(

                label="Entrance Rank"

            )



        with gr.Row():


            Percentile = gr.Number(

                label="Percentile"

            )


            Attempts = gr.Number(

                label="Number of Attempts"

            )







    # ======================================================
    # COLLEGE PREFERENCE SECTION
    # ======================================================


    with gr.Group(

        visible=False

    ) as college_section:


        gr.Markdown(

            "## 🏫 College Preference Details"

        )


        with gr.Row():


            Preferred_College = gr.Textbox(

                label="Preferred College"

            )


            Preferred_Branch = gr.Textbox(

                label="Preferred Branch"

            )


            College_Type = gr.Dropdown(

                choices=[

                    "Government",

                    "Private"

                ],

                label="College Type"

            )



        with gr.Row():


            College_Rank = gr.Number(

                label="College Rank"

            )


            Hostel = gr.Dropdown(

                choices=[

                    "Yes",

                    "No"

                ],

                label="Hostel Required"

            )


            Location = gr.Textbox(

                label="Preferred Location"

            )






    # ======================================================
    # VERIFICATION SECTION
    # ======================================================


    with gr.Group(

        visible=False

    ) as verification_section:


        gr.Markdown(

            "## ✅ Verification Details"

        )



        with gr.Row():


            Documents = gr.Dropdown(

                choices=[

                    "Verified",

                    "Not Verified"

                ],

                label="Documents Status"

            )


            Interview_Score = gr.Number(

                label="Interview Score"

            )


            Communication = gr.Number(

                label="Communication Skill"

            )






    # ======================================================
    # SCHOLARSHIP SECTION
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

                label="Scholarship Required"

            )


            Family_Status = gr.Textbox(

                label="Family Status"

            )


            Fee_Budget = gr.Number(

                label="Fee Budget"

            )






    # ======================================================
    # PREDICTION AREA
    # ======================================================


    gr.Markdown(

        "## 🚀 Final Admission Prediction"

    )



    predict_button = gr.Button(

        "🚀 Predict Admission",

        variant="primary"

    )



    result = gr.Textbox(

        label="Prediction Result",

        lines=3

    )



    probability = gr.Slider(

        minimum=0,

        maximum=100,

        value=0,

        label="📊 Admission Probability (%)"

    )
# ==========================================================
# PART 4/6
# BUTTON EVENTS + PREDICTION CONNECTION
# ==========================================================




# ==========================================================
# SHOW SECTION FUNCTION
# ==========================================================


def show_section():

    return gr.update(

        visible=True

    )





# ==========================================================
# BUTTON CONNECTIONS
# ==========================================================



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
# PREPARE MODEL INPUT
# ==========================================================


def final_prediction(


    Age,

    Category,

    Family_Income,


    Class10,

    Class12,

    PCM,


    Graduation,

    Backlogs,


    Exam_Name,

    Exam_Score,

    Rank,

    Percentile,

    Attempts,


    Preferred_College,

    Preferred_Branch,

    College_Type,

    College_Rank,

    Hostel,

    Location,


    Documents,

    Interview_Score,

    Communication,


    Scholarship,

    Family_Status,

    Fee_Budget


):


    try:



        # Creating dataframe

        input_data = pd.DataFrame({



            "Age":[Age],


            "Category":[Category],


            "Family_Income":[Family_Income],



            "Class10":[Class10],


            "Class12":[Class12],


            "PCM":[PCM],



            "Graduation":[Graduation],


            "Backlogs":[Backlogs],



            "Exam_Name":[Exam_Name],


            "Exam_Score":[Exam_Score],


            "Rank":[Rank],


            "Percentile":[Percentile],


            "Attempts":[Attempts],



            "Preferred_College":[Preferred_College],


            "Preferred_Branch":[Preferred_Branch],


            "College_Type":[College_Type],


            "College_Rank":[College_Rank],


            "Hostel":[Hostel],


            "Location":[Location],



            "Documents":[Documents],


            "Interview_Score":[Interview_Score],


            "Communication":[Communication],



            "Scholarship":[Scholarship],


            "Family_Status":[Family_Status],


            "Fee_Budget":[Fee_Budget]


        })





        # Prediction

        prediction, probability_value = predict_admission(

            input_data

        )



        return (

            prediction,

            probability_value

        )




    except Exception as e:


        return (

            "❌ Prediction Error : " + str(e),

            0

        )







# ==========================================================
# PREDICTION BUTTON EVENT
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


        Graduation,

        Backlogs,


        Exam_Name,

        Exam_Score,

        Rank,

        Percentile,

        Attempts,


        Preferred_College,

        Preferred_Branch,

        College_Type,

        College_Rank,

        Hostel,

        Location,


        Documents,

        Interview_Score,

        Communication,


        Scholarship,

        Family_Status,

        Fee_Budget


    ],



    outputs=[


        result,

        probability


    ]

)
# ==========================================================
# PART 5/6
# MODEL PREPROCESSING + SAFE PREDICTION
# ==========================================================




# ==========================================================
# ENCODE USER INPUT
# ==========================================================


def preprocess_input(df):


    df = df.copy()



    # Convert common Yes/No fields


    yes_no_columns = [

        "Hostel",

        "Scholarship"

    ]



    for col in yes_no_columns:


        if col in df.columns:


            df[col] = df[col].map(

                {

                    "Yes":1,

                    "No":0

                }

            )





    # Category encoding


    category_map = {


        "General":0,

        "OBC":1,

        "SC":2,

        "ST":3


    }



    if "Category" in df.columns:


        df["Category"] = df["Category"].map(

            category_map

        )






    # College type encoding


    college_map = {


        "Government":0,

        "Private":1


    }



    if "College_Type" in df.columns:


        df["College_Type"] = df["College_Type"].map(

            college_map

        )






    # Document verification


    document_map = {


        "Verified":1,

        "Not Verified":0


    }



    if "Documents" in df.columns:


        df["Documents"] = df["Documents"].map(

            document_map

        )






    # Remaining text columns

    # convert into numerical labels


    for col in df.columns:


        if df[col].dtype == "object":


            df[col] = (

                df[col]

                .astype("category")

                .cat.codes

            )





    # Fill missing values


    df = df.fillna(0)



    return df







# ==========================================================
# UPDATED PREDICTION FUNCTION
# ==========================================================


def predict_admission(data):


    try:



        if model is None:


            return (

                "❌ Model not loaded",

                0

            )





        processed_data = preprocess_input(

            data

        )





        prediction = model.predict(

            processed_data

        )[0]







        probability = 0





        if hasattr(

            model,

            "predict_proba"

        ):


            probability = round(

                max(

                    model.predict_proba(

                        processed_data

                    )[0]

                )

                *100,

                2

            )





        else:


            if prediction == 1:


                probability = 85


            else:


                probability = 25






        if prediction == 1:


            message = f"""

            🎉 Admission Approved


            Probability: {probability}%


            """



        else:


            message = f"""

            ❌ Admission Not Approved


            Probability: {probability}%


            """






        return (

            message,

            probability

        )





    except Exception as e:



        return (

            "❌ Prediction Failed : " + str(e),

            0

        )
# ==========================================================
# PART 6/6
# FINAL LAUNCH
# ==========================================================



# ==========================================================
# RUN APPLICATION
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
