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

        <h2 class="result-title">${data.status}</h2>

        <p class="result-message">${data.message}</p>

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


    showSection("basic");


};
