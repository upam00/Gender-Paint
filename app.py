from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras.utils import get_file
import numpy as np
import cv2
import os
import cvlib as cv
from flask import Flask, redirect, url_for, request, render_template,g, jsonify
import json
from json import JSONEncoder
import base64
from waitress import serve

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
    
model = load_model("gender_detection.model")

def predict(image, model):
# read input image
    #image = cv2.imread(file)
    image= cv2.resize(image,(400,400))
    if image is None:
        print("Could not read input image")
        exit()

# detect faces in the image
    face, confidence = cv.detect_face(image)

    classes = ['man','woman']

# loop through detected faces
    for idx, f in enumerate(face):
    
         # get corner points of face rectangle       
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]
    
        # draw rectangle over face
        cv2.rectangle(image, (startX,startY), (endX,endY), (0,255,0), 2)
    
        # crop the detected face region
        face_crop = np.copy(image[startY:endY,startX:endX])
    
        # preprocessing for gender detection model
        face_crop = cv2.resize(face_crop, (96,96))
        face_crop = face_crop.astype("float") / 255.0
        face_crop = img_to_array(face_crop)
        face_crop = np.expand_dims(face_crop, axis=0)
    
        # apply gender detection on face
        conf = model.predict(face_crop)[0]
        print(conf)
        print(classes)
    
        # get label with max accuracy
        idx = np.argmax(conf)
        label = classes[idx]
    
        label = "{}: {:.2f}%".format(label, conf[idx] * 100)
    
        Y = startY - 10 if startY - 10 > 10 else startY + 10
    
        # write label and confidence above face rectangle
        cv2.putText(image, label, (startX, Y),  cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2)
    
    
    return image

app = Flask(__name__)

@app.route("/status")
def check_status():
    return jsonify({"status":"Success", "data": []})

@app.route('/upload', methods=['POST'])
def upload():
        image_base64=request.json["base64"]  #Send base64 field in POST
        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.b64decode(image_base64))
        image = cv2.imread('imageToSave.png')

        # Make prediction
        image = predict(image, model)    #Call Predict Function from model
        #cv2.imshow("gender detection", image)
        # press any key to close window
        #cv2.waitKey()
        # save output
        cv2.imwrite("gender_detection.jpg", image)
        # release resources
        #cv2.destroyAllWindows()


        
        
        with open("gender_detection.jpg", "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())

        return b64_string


if __name__ == "__main__":  #Local
    app.run(host="localhost", port="3435", debug=True, use_reloader=True,threaded=True)

else:     #Production (Heroku)
    port = int(os.environ.get('PORT', 33507))
    serve(app,port=port)