from flask import Flask, request
from flask_restful import Resource, Api
import tensorflow as tf
import numpy as np
from flask_cors import CORS
from PIL import Image
import io

app = Flask(__name__)
CORS(app, origins=['http://localhost:8501'])
api = Api(app)

class UploadImage(Resource):
    def post(self):
        # Get the image from the request data
        image_file = request.files.get("image")

        # Check if an image is included
        if image_file:
            # Load and compile the model
            cnn = tf.keras.models.load_model('cat_dog.h5')
            cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

            try:
                # Open and preprocess the image
                img = Image.open(image_file)
                img = img.resize((64, 64))
                img = img.convert('RGB')  # Ensure image is in RGB format
                test_image = tf.keras.preprocessing.image.img_to_array(img)
                test_image = np.expand_dims(test_image, axis=0)

                # Predict using the model
                result = cnn.predict(test_image)
                if result[0][0] == 1:
                    prediction = 'dog'
                else:
                    prediction = 'cat'

                return {"message": prediction}, 200  # Success status code
            except Exception as e:
                return {"message": f"Error processing image: {str(e)}"}, 400  # Bad request status code
        else:
            return {"message": "No image selected"}, 400  # Bad request status code

# Add the endpoint to the API
api.add_resource(UploadImage, "/classify")

if __name__ == "__main__":
    app.run(debug=True)
