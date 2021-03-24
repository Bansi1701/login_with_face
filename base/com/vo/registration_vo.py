from base import database


class faceVO(database.Model):
    __tablename__ = 'face_database'
    face_id = database.Column('face_id', database.Integer, primary_key=True, autoincrement=True)
    face_name = database.Column('face_name', database.String(100))
    face_email_id = database.Column('face_email_id', database.String(100))
    face_password= database.Column('face_password', database.String(100), nullable=False)
    face_txt=database.column('face_txt',database.string(100),nullable=False,default="default.txt")


    def as_dict(self):
        return {
            'face_id': self.face_id,
            'face_name': self.face_name,
            'face_email_id': self.face_email_id,
            'face_password':self.face.password,
            'face_txt':self.face_txt

        }


database.create_all()
