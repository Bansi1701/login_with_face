from base.com.vo.registration_vo import *


class faceDAO:
    def insert_category(self, face_vo):
        database.session.add(face_vo)
        database.session.commit()