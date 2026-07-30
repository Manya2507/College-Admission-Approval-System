# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# FLASK BACKEND
# PART 1
# ==========================================================

import os
import joblib
import pandas as pd

from flask import Flask, render_template, request, jsonify

# ==========================================================
# CREATE FLASK APPLICATION
# ==========================================================

app = Flask(__name__)

# ==========================================================
# CATEGORY MAPPINGS
# ==========================================================

category_map = {
    "General": 0,
    "OBC": 1,
    "SC": 2,
    "ST": 3
}

exam_map = {
    "JEE": 0,
    "CUET": 1,
    "NEET": 2,
    "Other": 3
}

branch_map = {
    "CSE": 0,
    "IT": 1,
    "ECE": 2,
    "EEE": 3,
    "Mechanical": 4,
    "Civil": 5
}

college_map = {
    "PIET": 0,
    "NIT": 1,
    "IIT": 2,
    "Other": 3
}

college_type_map = {
    "Government": 0,
    "Private": 1
}

tier_map = {
    "1": 1,
    "2": 2,
    "3": 3
}

quota_map = {
    "General": 0,
    "EWS": 1,
    "OBC": 2,
    "SC": 3,
    "ST": 4
}

documents_map = {
    "Yes": 1,
    "No": 0
}

scholarship_applied_map = {
    "Yes": 1,
    "No": 0
}

scholarship_eligibility_map = {
    "Yes": 1,
    "No": 0
}

hostel_map = {
    "Yes": 1,
    "No": 0
}

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
# HOME PAGE
# ==========================================================

@app.route("/")
def home():
    return render_template("index.html")
# ==========================================================
# PREDICTION ROUTE
# ==========================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        if model is None:
            return jsonify({
                "status": "Model Not Loaded",
                "message": "college_admission_approval.pkl not found"
            })

        data = request.get_json(force=True)
        input_data = pd.DataFrame([{

            "Age": float(data.get("Age", 0)),

            "Category": category_map.get(
                data.get("Category"),
                0
            ),

            "Family_Income": float(
                data.get("Family_Income", 0)
            ),

            "Class10_%": float(
                data.get("Class10_%", 0)
            ),

            "Class12_%": float(
                data.get("Class12_%", 0)
            ),

            "PCM_%": float(
                data.get("PCM_%", 0)
            ),

            "Entrance_Exam": exam_map.get(
                data.get("Entrance_Exam"),
                0
            ),

            "JEE_Percentile": float(
                data.get("JEE_Percentile", 0)
            ),

            "JEE_Rank": float(
                data.get("JEE_Rank", 0)
            ),

            "CUET_Score": float(
                data.get("CUET_Score", 0)
            ),

            "Preferred_Branch": branch_map.get(
                data.get("Preferred_Branch"),
                0
            ),

            "Preferred_College": college_map.get(
                data.get("Preferred_College"),
                0
            ),

            "College_Type": college_type_map.get(
                data.get("College_Type"),
                0
            ),

            "NIRF_Rank": float(
                data.get("NIRF_Rank", 0)
            ),

            "College_Tier": tier_map.get(
                data.get("College_Tier"),
                1
            ),

            "Branch_Cutoff_Rank": float(
                data.get("Branch_Cutoff_Rank", 0)
            ),

            "Available_Seats": float(
                data.get("Available_Seats", 0)
            ),

            "Reservation_Quota": quota_map.get(
                data.get("Reservation_Quota"),
                0
            ),

            "Documents_Verified": documents_map.get(
                data.get("Documents_Verified"),
                0
            ),

            "Interview_Score": float(
                data.get("Interview_Score", 0)
            ),

            "Communication_Score": float(
                data.get("Communication_Score", 0)
            ),

            "Aptitude_Score": float(
                data.get("Aptitude_Score", 0)
            ),

            "Scholarship_Applied": scholarship_applied_map.get(
                data.get("Scholarship_Applied"),
                0
            ),

            "Scholarship_Eligibility": scholarship_eligibility_map.get(
                data.get("Scholarship_Eligibility"),
                0
            ),

            "Hostel_Required": hostel_map.get(
                data.get("Hostel_Required"),
                0
            ),

            "Admission_Probability": float(
                data.get("Admission_Probability", 0)
            ),

            "Tuition_Fee": float(
                data.get("Tuition_Fee", 0)
            )

        }])

        prediction = model.predict(input_data)[0]

        if hasattr(model, "predict_proba"):
            probability = round(
                max(model.predict_proba(input_data)[0]) * 100,
                2
            )
        else:
            probability = 0

        if str(prediction).lower() in [
            "1",
            "approved",
            "yes",
            "true"
        ]:

            result = "🎓 ADMISSION APPROVED"
            message = "Congratulations! The student is eligible for admission."

                prediction = model.predict(input_data)[0]

        if hasattr(model, "predict_proba"):
            probability = round(
                max(model.predict_proba(input_data)[0]) * 100,
                2
            )
        else:
            probability = 0

        if str(prediction).lower() in [
            "1",
            "approved",
            "yes",
            "true"
        ]:

            result = "🎓 ADMISSION APPROVED"
            message = "Congratulations! The student is eligible for admission."

        else:

            result = "❌ ADMISSION REJECTED"
            message = "Sorry! The student is not eligible for admission."

        return jsonify({
            "status": result,
            "message": message,
            "probability": probability
        })

    except Exception as e:

        return jsonify({
            "status": "Prediction Error",
            "message": str(e),
            "probability": 0
        })

    except Exception as e:

        return jsonify({

            "status": "Prediction Error",

            "message": str(e),

            "probability": 0

        })


# ==========================================================
# RUN FLASK APPLICATION
# ==========================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=int(os.environ.get("PORT", 7860)),

        debug=False

    )
            
       
