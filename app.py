# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# PART 1/5
# FLASK BACKEND + MACHINE LEARNING MODEL
# ==========================================================


import os
import joblib
import pandas as pd

from flask import (
    Flask,
    render_template,
    request,
    jsonify
)





# ==========================================================
# CREATE FLASK APP
# ==========================================================


app = Flask(__name__)





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
# HOME PAGE
# ==========================================================


@app.route("/")

def home():

    return render_template(
        "index.html"
    )







# ==========================================================
# PREDICTION API
# ==========================================================


@app.route(
    "/predict",
    methods=["POST"]
)

def predict():



    try:



        # Receive data from HTML


        data = request.json




        input_data = pd.DataFrame([{


            "Age":

            float(data["Age"]),



            "Category":

            data["Category"],



            "Family_Income":

            float(data["Family_Income"]),



            "Class10_%":

            float(data["Class10_%"]),



            "Class12_%":

            float(data["Class12_%"]),



            "PCM_%":

            float(data["PCM_%"]),



            "Entrance_Exam":

            data["Entrance_Exam"],



            "JEE_Percentile":

            float(data["JEE_Percentile"]),



            "JEE_Rank":

            float(data["JEE_Rank"]),



            "CUET_Score":

            float(data["CUET_Score"]),



            "Preferred_Branch":

            data["Preferred_Branch"],



            "Preferred_College":

            data["Preferred_College"],



            "College_Type":

            data["College_Type"],



            "NIRF_Rank":

            float(data["NIRF_Rank"]),



            "College_Tier":

            float(data["College_Tier"]),



            "Branch_Cutoff_Rank":

            float(data["Branch_Cutoff_Rank"]),



            "Available_Seats":

            float(data["Available_Seats"]),



            "Reservation_Quota":

            data["Reservation_Quota"],



            "Documents_Verified":

            data["Documents_Verified"],



            "Interview_Score":

            float(data["Interview_Score"]),



            "Communication_Score":

            float(data["Communication_Score"]),



            "Aptitude_Score":

            float(data["Aptitude_Score"]),



            "Scholarship_Applied":

            data["Scholarship_Applied"],



            "Scholarship_Eligibility":

            data["Scholarship_Eligibility"],



            "Hostel_Required":

            data["Hostel_Required"],



            "Admission_Probability":

            float(data["Admission_Probability"]),



            "Tuition_Fee":

            float(data["Tuition_Fee"])



        }])







        # Prediction


        prediction = model.predict(

            input_data

        )[0]






        # Probability


        try:


            probability = max(

                model.predict_proba(

                    input_data

                )[0]

            )


            probability = round(

                probability * 100,

                2

            )


        except:


            probability = 0







        if str(prediction).lower() in [


            "approved",

            "yes",

            "1"


        ]:



            result = {

                "status":

                "🎉 ADMISSION APPROVED",


                "message":

                "High chance of admission",


                "probability":

                probability

            }



        else:



            result = {


                "status":

                "❌ ADMISSION NOT APPROVED",


                "message":

                "Low chance of admission",


                "probability":

                probability


            }






        return jsonify(result)







    except Exception as e:



        return jsonify({


            "status":

            "❌ Prediction Error",


            "message":

            str(e),


            "probability":

            0


        })







# ==========================================================
# RUN APPLICATION
# ==========================================================


if __name__ == "__main__":



    app.run(


        host="0.0.0.0",


        port=int(

            os.environ.get(

                "PORT",

                7860

            )

        )


    )
<!-- ======================================================
 AI COLLEGE ADMISSION APPROVAL SYSTEM
 PART 2/5
 HTML FRONTEND DASHBOARD
====================================================== -->


<!DOCTYPE html>

<html lang="en">


<head>


<meta charset="UTF-8">


<meta name="viewport" content="width=device-width, initial-scale=1.0">


<title>
AI College Admission Approval System
</title>



<link rel="stylesheet" href="/static/style.css">


</head>



<body>



<div class="overlay">



<!-- ================= HEADER ================= -->


<div class="header">


<h1>
🎓 AI College Admission Approval System
</h1>


<h2>
Machine Learning Based Admission Prediction Platform
</h2>


<p>
Predict your admission chances using academic,
entrance exam and college details.
</p>



<div class="developer">


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
<b>Technology:</b> Python | Flask | Machine Learning | Random Forest
</p>


</div>


</div>





<!-- ================= BUTTON MENU ================= -->


<div class="menu">


<button onclick="showSection('academic')">

📚 Academic Analysis

</button>



<button onclick="showSection('entrance')">

🎯 Entrance Analysis

</button>



<button onclick="showSection('college')">

🏫 College Matching

</button>



<button onclick="showSection('verification')">

✅ Verification

</button>



<button onclick="showSection('scholarship')">

💰 Scholarship

</button>


</div>







<!-- ================= FORM ================= -->


<div class="form-container">



<form id="admissionForm">





<!-- =============== ACADEMIC ================= -->


<div id="academic" class="section">


<h2>
📚 Academic Details
</h2>


<div class="grid">



<input 
type="number"
id="Age"
placeholder="Age"
>



<select id="Category">

<option>General</option>
<option>OBC</option>
<option>SC</option>
<option>ST</option>

</select>




<input
type="number"
id="Family_Income"
placeholder="Family Income ₹"
>




<input
type="number"
id="Class10_%"
placeholder="Class 10 Percentage"
>



<input
type="number"
id="Class12_%"
placeholder="Class 12 Percentage"
>



<input
type="number"
id="PCM_%"
placeholder="PCM Percentage"
>



</div>


</div>









<!-- =============== ENTRANCE ================= -->


<div id="entrance" class="section hidden">


<h2>
🎯 Entrance Exam Details
</h2>



<div class="grid">



<input
id="Entrance_Exam"
placeholder="Entrance Exam Name"
>




<input
type="number"
id="JEE_Percentile"
placeholder="JEE Percentile"
>



<input
type="number"
id="JEE_Rank"
placeholder="JEE Rank"
>



<input
type="number"
id="CUET_Score"
placeholder="CUET Score"
>




</div>


</div>









<!-- =============== COLLEGE ================= -->


<div id="college" class="section hidden">


<h2>
🏫 College Preference Details
</h2>



<div class="grid">



<input
id="Preferred_Branch"
placeholder="Preferred Branch"
>



<input
id="Preferred_College"
placeholder="Preferred College"
>



<select id="College_Type">


<option>
Government
</option>


<option>
Private
</option>


</select>




<input
type="number"
id="NIRF_Rank"
placeholder="NIRF Rank"
>



<input
type="number"
id="College_Tier"
placeholder="College Tier"
>



<input
type="number"
id="Branch_Cutoff_Rank"
placeholder="Branch Cutoff Rank"
>



<input
type="number"
id="Available_Seats"
placeholder="Available Seats"
>




<input
id="Reservation_Quota"
placeholder="Reservation Quota"
>



</div>


</div>









<!-- =============== VERIFICATION ================= -->


<div id="verification" class="section hidden">


<h2>
✅ Verification & Interview Details
</h2>



<div class="grid">



<select id="Documents_Verified">


<option>
Yes
</option>


<option>
No
</option>


</select>




<input
type="number"
id="Interview_Score"
placeholder="Interview Score"
>




<input
type="number"
id="Communication_Score"
placeholder="Communication Score"
>



<input
type="number"
id="Aptitude_Score"
placeholder="Aptitude Score"
>



</div>


</div>









<!-- =============== SCHOLARSHIP ================= -->


<div id="scholarship" class="section hidden">


<h2>
💰 Scholarship & Additional Details
</h2>



<div class="grid">



<select id="Scholarship_Applied">


<option>
Yes
</option>


<option>
No
</option>


</select>





<select id="Scholarship_Eligibility">


<option>
Yes
</option>


<option>
No
</option>


</select>





<select id="Hostel_Required">


<option>
Yes
</option>


<option>
No
</option>


</select>




<input
type="number"
id="Admission_Probability"
placeholder="Previous Admission Probability"
>




<input
type="number"
id="Tuition_Fee"
placeholder="Tuition Fee ₹"
>



</div>


</div>








<!-- ================= PREDICT BUTTON ================= -->


<button 
type="button"
class="predict-btn"
onclick="predictAdmission()">

🚀 Predict Admission

</button>






</form>



</div>








<!-- ================= RESULT ================= -->


<div class="result-box">


<h2>
🎓 Prediction Result
</h2>



<p id="result">

Fill all details and click predict.

</p>



</div>





</div>





<script src="/static/script.js"></script>



</body>


</html>
/* ==========================================================
 AI COLLEGE ADMISSION APPROVAL SYSTEM
 PART 3/5
 CSS DESIGN + BACKGROUND SLIDESHOW
========================================================== */



/* ==============================
   BASIC SETTINGS
============================== */


*{

    margin:0;

    padding:0;

    box-sizing:border-box;

    font-family:

    'Segoe UI',
    sans-serif;

}




body{


    min-height:100vh;


    color:white;


    overflow-x:hidden;


}





/* ==============================
   BACKGROUND SLIDESHOW
============================== */


body::before{


    content:"";


    position:fixed;


    top:0;


    left:0;


    width:100%;


    height:100%;



    z-index:-2;




    background-size:cover;


    background-position:center;


    background-repeat:no-repeat;



    animation:

    backgroundChange 40s infinite,

    zoomEffect 20s infinite alternate;


}







/* ==============================
   IMAGE SLIDES
============================== */



@keyframes backgroundChange{


0%{


background-image:

linear-gradient(

rgba(0,0,40,0.65),

rgba(0,0,40,0.65)

),

url("/static/images/images (1).jpg");


}




20%{


background-image:

linear-gradient(

rgba(0,0,40,0.65),

rgba(0,0,40,0.65)

),

url("/static/images/images (2).jpg");


}




40%{


background-image:

linear-gradient(

rgba(0,0,40,0.65),

rgba(0,0,40,0.65)

),

url("/static/images/images(3).jpg");


}




60%{


background-image:

linear-gradient(

rgba(0,0,40,0.65),

rgba(0,0,40,0.65)

),

url("/static/images/images(4).jpg");


}




80%{


background-image:

linear-gradient(

rgba(0,0,40,0.65),

rgba(0,0,40,0.65)

),

url("/static/images/images(5).jpg");


}




100%{


background-image:

linear-gradient(

rgba(0,0,40,0.65),

rgba(0,0,40,0.65)

),

url("/static/images/images (1).jpg");


}


}






@keyframes zoomEffect{


from{


background-size:

100%;


}


to{


background-size:

115%;


}



}








/* ==============================
   MAIN OVERLAY
============================== */



.overlay{


    width:100%;


    min-height:100vh;


    padding:30px;


}








/* ==============================
   HEADER
============================== */



.header{


    text-align:center;


    padding:25px;


}






.header h1{


    font-size:48px;


    font-weight:900;


    text-shadow:

    3px 3px 15px black;


    color:#00ffff;


}







.header h2{


    margin-top:10px;


    font-size:28px;


    color:white;


}





.header p{


    font-size:18px;


    margin-top:10px;


}





.developer{


    margin-top:20px;


    font-size:18px;


    line-height:1.8;


}







.developer h3{


    color:#00ff99;


    font-size:28px;


}









/* ==============================
   BUTTON MENU
============================== */


.menu{


    display:flex;


    justify-content:center;


    flex-wrap:wrap;


    gap:20px;


    margin:30px 0;


}






.menu button{


    padding:15px 25px;


    border-radius:30px;


    border:

    2px solid white;



    cursor:pointer;



    background:

    linear-gradient(

    135deg,

    #00c6ff,

    #0072ff

    );



    color:white;


    font-size:17px;


    font-weight:bold;



    transition:

    0.3s;


}






.menu button:hover{


    transform:

    scale(1.1);



    background:

    linear-gradient(

    135deg,

    #00ff99,

    #00c6ff

    );


}








/* ==============================
   FORM CONTAINER
============================== */



.form-container{


    width:90%;


    margin:auto;


}








.section{


    background:

    rgba(0,0,30,0.45);



    padding:25px;



    border-radius:25px;


    border:

    1px solid rgba(255,255,255,0.4);



    backdrop-filter:

    blur(10px);



    animation:

    fadeIn 0.5s;


}






.hidden{


    display:none;


}








.section h2{


    color:#00ffff;


    margin-bottom:20px;


    text-align:center;


}









/* ==============================
   INPUT GRID
============================== */


.grid{


    display:grid;


    grid-template-columns:


    repeat(

    3,

    1fr

    );


    gap:20px;


}






input,

select{


    width:100%;


    padding:14px;


    border-radius:15px;


    border:none;



    outline:none;


    font-size:16px;



    background:

    rgba(255,255,255,0.9);



    color:black;


}







input:focus,

select:focus{


    border:

    3px solid #00ffff;


}










/* ==============================
   PREDICT BUTTON
============================== */


.predict-btn{


    display:block;


    margin:35px auto;


    padding:18px 50px;


    border-radius:40px;


    border:none;



    background:

    linear-gradient(

    135deg,

    #00ff88,

    #009944

    );



    color:white;


    font-size:22px;


    font-weight:bold;



    cursor:pointer;


    transition:

    0.3s;


}






.predict-btn:hover{


    transform:

    scale(1.1);


}









/* ==============================
   RESULT BOX
============================== */



.result-box{


    margin:30px auto;


    width:80%;


    padding:25px;



    text-align:center;


    border-radius:25px;



    background:

    rgba(0,0,0,0.55);



    border:

    2px solid #00ffff;



    font-size:22px;


}







#result{


    margin-top:15px;


    color:#00ffcc;


    font-weight:bold;


}








/* ==============================
   ANIMATION
============================== */



@keyframes fadeIn{


from{


opacity:0;


transform:

translateY(20px);


}



to{


opacity:1;


transform:

translateY(0);


}


}









/* ==============================
   MOBILE RESPONSIVE
============================== */


@media(max-width:900px){



.grid{


grid-template-columns:

1fr;


}



.header h1{


font-size:32px;


}


.menu button{


width:100%;


}


}
// ==========================================================
// AI COLLEGE ADMISSION APPROVAL SYSTEM
// PART 4/5
// JAVASCRIPT BUTTON CONTROL + PREDICTION REQUEST
// ==========================================================



// ==========================================================
// SECTION SWITCHING
// ==========================================================


function showSection(sectionName){


    let sections = document.querySelectorAll(".section");


    sections.forEach(function(section){


        section.classList.add("hidden");


    });



    document
    .getElementById(sectionName)
    .classList.remove("hidden");



}







// ==========================================================
// COLLECT FORM DATA
// ==========================================================


function getFormData(){


    return {


        Age:

        document.getElementById("Age").value,



        Category:

        document.getElementById("Category").value,



        Family_Income:

        document.getElementById("Family_Income").value,



        "Class10_%":

        document.getElementById("Class10_%").value,



        "Class12_%":

        document.getElementById("Class12_%").value,



        "PCM_%":

        document.getElementById("PCM_%").value,



        Entrance_Exam:

        document.getElementById("Entrance_Exam").value,



        JEE_Percentile:

        document.getElementById("JEE_Percentile").value,



        JEE_Rank:

        document.getElementById("JEE_Rank").value,



        CUET_Score:

        document.getElementById("CUET_Score").value,



        Preferred_Branch:

        document.getElementById("Preferred_Branch").value,



        Preferred_College:

        document.getElementById("Preferred_College").value,



        College_Type:

        document.getElementById("College_Type").value,



        NIRF_Rank:

        document.getElementById("NIRF_Rank").value,



        College_Tier:

        document.getElementById("College_Tier").value,



        Branch_Cutoff_Rank:

        document.getElementById("Branch_Cutoff_Rank").value,



        Available_Seats:

        document.getElementById("Available_Seats").value,



        Reservation_Quota:

        document.getElementById("Reservation_Quota").value,



        Documents_Verified:

        document.getElementById("Documents_Verified").value,



        Interview_Score:

        document.getElementById("Interview_Score").value,



        Communication_Score:

        document.getElementById("Communication_Score").value,



        Aptitude_Score:

        document.getElementById("Aptitude_Score").value,



        Scholarship_Applied:

        document.getElementById("Scholarship_Applied").value,



        Scholarship_Eligibility:

        document.getElementById("Scholarship_Eligibility").value,



        Hostel_Required:

        document.getElementById("Hostel_Required").value,



        Admission_Probability:

        document.getElementById("Admission_Probability").value,



        Tuition_Fee:

        document.getElementById("Tuition_Fee").value



    };


}







// ==========================================================
// PREDICTION FUNCTION
// ==========================================================


function predictAdmission(){



    let formData = getFormData();




    let resultBox = document.getElementById("result");



    resultBox.innerHTML = 
    "⏳ Processing Admission Prediction...";






    fetch("/predict",{


        method:"POST",



        headers:{


            "Content-Type":

            "application/json"


        },



        body:

        JSON.stringify(formData)



    })



    .then(response => response.json())



    .then(data => {



        resultBox.innerHTML = `



        <h2>

        ${data.status}

        </h2>



        <br>


        📊 Admission Probability:

        <b>

        ${data.probability}%

        </b>


        <br><br>



        ${data.message}



        `;



    })



    .catch(error => {



        resultBox.innerHTML = `



        ❌ Error occurred:


        ${error}



        `;



    });



}







// ==========================================================
// PAGE LOAD DEFAULT SECTION
// ==========================================================


window.onload=function(){


    showSection("academic");


};
