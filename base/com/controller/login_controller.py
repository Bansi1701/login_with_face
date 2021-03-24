import os

import cv2
from flask import *

from base import *
from base.com.dao.registration_dao import UserDAO


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/user_login', methods=["POST"])
def user_login():
    user_email_id = request.form.get('email')
    session['user_email_id'] = user_email_id
    user_dao = UserDAO()
    user_vo_list = user_dao.view_email_id()
    print(user_vo_list[0].user_email_id)
    for user_details in user_vo_list:
        if (user_details.user_email_id) == user_email_id:
            session['user_name'] = user_details.user_name
            return redirect(url_for('login_with_face'))
        else:
            continue
    else:
        flash('email not registred......')
        return redirect(url_for('index'))


@app.route('/login_with_face')
def login_with_face():
    name_of_user = None
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel/" + session['user_email_id'] + ".yml")
    harcascadePath = "C:/Users/bansi/PycharmProjects/login_with_face/base/static/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                return render_template('welcome.html', username=session['user_name'])
            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)

        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    cam.release()
    cv2.destroyAllWindows()
