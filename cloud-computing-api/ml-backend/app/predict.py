import numpy as np

class_label=['normal', 'severly stunting', 'stunting', 'tinggi']

def make_prediction(model, input_data):
    # Ubah input menjadi format array yang sesuai untuk model
    try:
        # Ubah input menjadi format array numpy dengan dimensi yang sesuai
        input_tensor = np.array(input_data).reshape(1, -1)

        # Prediksi menggunakan model
        prediction = model.predict(input_tensor)

        # Cari indeks prediksi dengan probabilitas tertinggi
        predicted_class = np.argmax(prediction)

        # Dapatkan label berdasarkan indeks
        if predicted_class < len(class_label):
            predict_label = class_label[predicted_class]
        else:
            raise ValueError("Predicted class index out of range")

        return predict_label  # Kembalikan label hasil prediksi

    except Exception as e:
        # Tangani error prediksi
        raise ValueError(f"Error during prediction: {str(e)}")
