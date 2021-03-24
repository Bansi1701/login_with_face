from base import database


class UserVO(database.Model):
    __tablename__ = 'user_database'
    user_id = database.Column('user_id', database.Integer, primary_key=True, autoincrement=True)
    user_name = database.Column('user_name', database.String(100))
    user_email_id = database.Column('user_email_id', database.String(100))
    user_password= database.Column('user_password', database.String(100), nullable=False)


    def as_dict(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_email_id': self.user_email_id,
            'user_password':self.user_password

        }


database.create_all()
