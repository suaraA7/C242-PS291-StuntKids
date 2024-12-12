from flask import Flask, Blueprint, jsonify, request
from .model import load_my_model
from .predict import make_prediction

main = Blueprint('main', __name__)

# Muat model sekali saat server dijalankan
model = load_my_model()

@main.route('/predict', methods=['POST'])
def predict():

    try:
        # Ambil data dari multipart-form
        input_text = request.form.get('input')  # Ambil teks dari form field 'input'
        
        if not input_text:
            return jsonify({
                "status": "error",
                "message": "'input' field is required in the form data"
            }), 400

        # Konversi teks ke format yang sesuai untuk model
        # Misalnya: konversi ke array jika model memerlukan array
        input_data = [float(x) for x in input_text.split(',')]  # Contoh parsing CSV teks
        
        # Lakukan prediksi menggunakan model
        prediction = make_prediction(model, input_data)
        
        # Format hasil prediksi menjadi teks
        response_text = f"Prediction result: {prediction}"
        
        # Kembalikan hasil sebagai JSON
        return jsonify({
            "status": "success",
            "result": response_text
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
