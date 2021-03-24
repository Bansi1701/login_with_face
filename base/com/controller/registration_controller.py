import os

import cv2
import numpy as np
from PIL import Image
from flask import *

from base import *
from base.com.dao.registration_dao import UserDAO
from base.com.vo.registration_vo import UserVO


@app.route('/load_registration')
def load_registration():
    return render_template('register.html')


@app.route('/user_registration', methods=['POST'])
def user_registration():
    user_name = request.form.get('name')
    user_email_id = request.form.get('email')
    user_password = request.form.get('password')
    session['email'] = user_email_id

    user_vo = UserVO()
    user_dao = UserDAO()
    user_vo.user_name = user_name
    user_vo.user_email_id = user_email_id
    user_vo.user_password = user_password
    user_dao.insert_user_details(user_vo)

    cam = cv2.VideoCapture(0)
    harcascadePath = "C:/Users/bansi/PycharmProjects/login_with_face/base/static/haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    sampleNum = 0
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # incrementing sample number
            sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder TrainingImage
            cv2.imwrite("TrainingImage\ " + user_name + '.' + str(sampleNum) + ".jpg",
                        gray[y:y + h, x:x + w])
            # display the frame
            cv2.imshow('frame', img)
        # wait for 100 miliseconds
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 100
        elif sampleNum > 60:
            break
    cam.release()
    cv2.destroyAllWindows()
    return redirect(url_for('Train_Images'))


@app.route('/Train_Images')
def Train_Images():
    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "C:/Users/bansi/PycharmProjects/login_with_face/base/static/haarcascade_frontalface_default.xml"

    detector = cv2.CascadeClassifier(harcascadePath)
    # print("hashnsajkdf>>>>", harcascadePath)
    faces, Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    # print("recognizer::>>>>>>>", recognizer)
    recognizer.save("TrainingImageLabel/" + session['email'] + ".yml")
    flash("Now you can login your self")  # +",".join(str(f) for f in Id)
    return render_template('login.html')


@app.route('/getImagesAndLables')
def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)
        # print(faces)
        # print(Ids)
    return faces, Ids
