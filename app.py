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


# =====================================================
# LOAD BACKGROUND IMAGES
# =====================================================

import os
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("BASE DIRECTORY:", BASE_DIR)
print("=" * 60)

print("Files in BASE_DIR:")

try:
    print(os.listdir(BASE_DIR))
except Exception as e:
    print("Error:", e)

IMAGES_DIR = os.path.join(BASE_DIR, "images")

print("\nImages Folder Path:")
print(IMAGES_DIR)

print("\nDoes images folder exist?")
print(os.path.exists(IMAGES_DIR))

if os.path.exists(IMAGES_DIR):
    print("\nImages Folder Contents:")
    print(os.listdir(IMAGES_DIR))
else:
    print("\n❌ images folder NOT FOUND!")


# =====================================================
# LOAD BACKGROUND IMAGES FROM IMAGES FOLDER
# =====================================================

def load_background_images():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    IMAGE_FOLDER = os.path.join(
        BASE_DIR,
        "images"
    )

    print("Checking folder:")
    print(IMAGE_FOLDER)


    if not os.path.exists(IMAGE_FOLDER):

        print("❌ Images folder not found")

        return []


    encoded_images = []


    for file in sorted(os.listdir(IMAGE_FOLDER)):


        if file.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):


            image_path = os.path.join(
                IMAGE_FOLDER,
                file
            )


            print(
                "Loading image:",
                image_path
            )


            with open(
                image_path,
                "rb"
            ) as img:


                encoded_images.append(

                    base64.b64encode(
                        img.read()
                    ).decode()

                )


    print(
        "Total Images Loaded:",
        len(encoded_images)
    )


    return encoded_images



BACKGROUND_IMAGES = load_background_images()


if len(BACKGROUND_IMAGES) == 0:

    print(
        "⚠️ No images found. Running without background images."
    )

print("\n" + "=" * 60)
print("Total Images Loaded:", len(BACKGROUND_IMAGES))
print("=" * 60)

# Prevent Render from crashing if images are missing
if len(BACKGROUND_IMAGES) == 0:

    print("⚠️ No images loaded. Using blank background.")

    BACKGROUND_IMAGES = [""] * 5

elif len(BACKGROUND_IMAGES) < 5:

    print("⚠️ Some images are missing.")

    while len(BACKGROUND_IMAGES) < 5:
        BACKGROUND_IMAGES.append(BACKGROUND_IMAGES[-1])

else:

    print("✅ All 5 images loaded successfully.")




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


        # ===============================
        # LABEL ENCODING
        # ===============================


        category_map = {
            "General":0,
            "OBC":1,
            "SC":2,
            "ST":3
        }


        college_map = {
            "Government":0,
            "Private":1
        }


        yes_no_map = {
            "No":0,
            "Yes":1
        }



        data = pd.DataFrame([{


            "Age":Age,

            "Category":category_map.get(Category,0),

            "Family_Income":Family_Income,


            "Class10_%":Class10_Percentage,

            "Class12_%":Class12_Percentage,

            "PCM_%":PCM_Percentage,


            "Entrance_Exam":0,


            "JEE_Percentile":JEE_Percentile,

            "JEE_Rank":JEE_Rank,


            "CUET_Score":CUET_Score,


            "Preferred_Branch":0,


            "Preferred_College":0,


            "College_Type":college_map.get(
                College_Type,0
            ),


            "NIRF_Rank":NIRF_Rank,


            "College_Tier":College_Tier,


            "Branch_Cutoff_Rank":Branch_Cutoff_Rank,


            "Available_Seats":Available_Seats,


            "Reservation_Quota":0,


            "Documents_Verified":
            yes_no_map.get(
                Documents_Verified,0
            ),


            "Interview_Score":Interview_Score,


            "Communication_Score":
            Communication_Score,


            "Aptitude_Score":
            Aptitude_Score,


            "Scholarship_Applied":
            yes_no_map.get(
                Scholarship_Applied,0
            ),


            "Scholarship_Eligibility":
            yes_no_map.get(
                Scholarship_Eligibility,0
            ),


            "Hostel_Required":
            yes_no_map.get(
                Hostel_Required,0
            ),


            "Admission_Probability":
            Admission_Probability,


            "Tuition_Fee":
            Tuition_Fee


        }])



        prediction = model.predict(data)[0]



        if prediction == 1:


            return """

🎉 ADMISSION APPROVED


✅ Student is eligible for admission.

🤖 Model:
Random Forest Classifier

"""


        else:


            return """

❌ ADMISSION NOT APPROVED


Student does not meet admission criteria.

🤖 Model:
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

.gradio-container {{

    min-height:100vh !important;

    width:100% !important;

    background-size:cover !important;

    background-position:center !important;

    background-repeat:no-repeat !important;

    background-attachment:fixed !important;

    animation:backgroundSlide 120s infinite ease-in-out !important;

}}



@keyframes backgroundSlide {{


0% {{

background-image:

linear-gradient(
rgba(0,0,0,0.25),
rgba(0,0,0,0.25)
),

url("data:image/jpg;base64,{BACKGROUND_IMAGES[0]}");

}}



20% {{

background-image:

linear-gradient(
rgba(0,0,0,0.25),
rgba(0,0,0,0.25)
),

url("data:image/jpg;base64,{BACKGROUND_IMAGES[1]}");

}}



40% {{

background-image:

linear-gradient(
rgba(0,0,0,0.25),
rgba(0,0,0,0.25)
),

url("data:image/jpg;base64,{BACKGROUND_IMAGES[2]}");

}}



60% {{

background-image:

linear-gradient(
rgba(0,0,0,0.25),
rgba(0,0,0,0.25)
),

url("data:image/jpg;base64,{BACKGROUND_IMAGES[3]}");

}}



80% {{

background-image:

linear-gradient(
rgba(0,0,0,0.25),
rgba(0,0,0,0.25)
),

url("data:image/jpg;base64,{BACKGROUND_IMAGES[4]}");

}}



100% {{

background-image:

linear-gradient(
rgba(0,0,0,0.25),
rgba(0,0,0,0.25)
),

url("data:image/jpg;base64,{BACKGROUND_IMAGES[0]}");

}}


}}


#main-container {{

    width:90% !important;

    max-width:1400px !important;

    margin:auto !important;

    padding:20px !important;

    background:transparent !important;

    border:none !important;

    box-shadow:none !important;

    backdrop-filter:none !important;

}}





#header-box {{

    text-align:center;

    padding:20px;

    background:transparent !important;

    border:none !important;

}}

.gradio-container .block,
.gradio-container .form,
.gradio-container .panel {{

    background:transparent !important;

    border:none !important;

    box-shadow:none !important;

}}



#header-box h1 {{

    font-size:45px;

    font-weight:900;

    color:white !important;

    text-shadow:

    3px 3px 10px black;

}}



#header-box h2 {{

    font-size:28px;

    color:#ffffff !important;

    text-shadow:

    2px 2px 8px black;

}}



#header-box h3 {{

    color:#00ffcc !important;

    text-shadow:

    2px 2px 8px black;

}}



#header-box p {{

    color:white !important;

    font-size:18px;

    text-shadow:

    2px 2px 8px black;

}}



label {{

    color:white !important;

    font-weight:bold !important;

    text-shadow:

    2px 2px 6px black;

}}


input,

textarea,

select {{

    background:white !important;

    color:black !important;

}}



button {{

    background:#059669 !important;

    color:white !important;

    border-radius:15px !important;

}}



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
<b>Project:</b> College Admission Approval System
</p>

<hr>

<p>
🤖 Predict admission approval using academic,
entrance exam and college preference details.
</p>

</div>

"""



with gr.Blocks(
    css=css,
    title="AI College Admission Approval System"
) as demo:


    with gr.Column(elem_id="main-container"):


        gr.HTML(header)



        # =========================================
        # STUDENT DETAILS
        # =========================================


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
                ["General","OBC","SC","ST"],
                label="Category"
            )

            Family_Income = gr.Number(
                label="Family Income (₹)"
            )



        # =========================================
        # ACADEMIC DETAILS
        # =========================================


        gr.Markdown(
        """
        ## 📚 Academic Details
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



        # =========================================
        # ENTRANCE DETAILS
        # =========================================


        gr.Markdown(
        """
        ## 📝 Entrance Exam Details
        """
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



        # =========================================
        # COLLEGE PREFERENCE DETAILS
        # =========================================


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
                [
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



        # =========================================
        # VERIFICATION DETAILS
        # =========================================


        gr.Markdown(
        """
        ## 📄 Document & Interview Details
        """
        )


        with gr.Row():

            Docs = gr.Dropdown(
                [
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



        # =========================================
        # EXTRA DETAILS
        # =========================================


        gr.Markdown(
        """
        ## 💰 Scholarship & Other Details
        """
        )


        with gr.Row():


            Scholarship = gr.Dropdown(
                [
                    "Yes",
                    "No"
                ],
                label="Scholarship Applied"
            )


            Scholarship_Eligibility = gr.Dropdown(
                [
                    "Yes",
                    "No"
                ],
                label="Scholarship Eligibility"
            )


            Hostel = gr.Dropdown(
                [
                    "Yes",
                    "No"
                ],
                label="Hostel Required"
            )


        with gr.Row():


            Probability = gr.Number(
                label="Admission Probability"
            )


            Fee = gr.Number(
                label="Tuition Fee (₹)"
            )



        # =========================================
        # BUTTON
        # =========================================


        predict_button = gr.Button(
            "🎯 Predict Admission",
            variant="primary"
        )


        output = gr.Textbox(
            label="🎓 Prediction Result",
            lines=8
        )

        # ==============================
        # PREDICT BUTTON
        # ==============================


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
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":

    print("🔥 Launching Gradio Server...")


    demo.launch(

        server_name="0.0.0.0",

        server_port=int(
            os.environ.get(
                "PORT",
                7860
            )
        )

    )
