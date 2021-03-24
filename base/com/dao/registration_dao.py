from base.com.vo.registration_vo import *


class UserDAO:
    def insert_user_details(self, user_vo):
        database.session.add(user_vo)
        database.session.commit()

    def view_email_id(self):
        user_vo_list = UserVO.query.all()
        return user_vo_list