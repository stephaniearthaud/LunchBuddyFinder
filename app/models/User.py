
from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def get_user(self, info):
        get_user_query = "SELECT * from linkedin_users WHERE access_token= :access_token"
        get_user_data = {'access_token': info['token']}
        user = self.db.query_db(get_user_query, get_user_data)
        return user

    def get_user_by_email(self, info):
        get_user_query = "SELECT * from linkedin_users WHERE email= :email"
        get_user_data = {'email': info['email']}
        user = self.db.query_db(get_user_query, get_user_data)
        return user

    def get_all_users(self):
        get_all_users_query = "SELECT name FROM linkedin_users"
        return self.db.query_db(get_all_users_query)

    def create_user(self, info):
        create_user_query = "INSERT INTO linkedin_users (access_token, name, email, first_name, headline, industry, location, image_link, created_at, updated_at) VALUES (:access_token,:name,:email,:first_name,:headline,:industry,:location,:image_link, NOW(), NOW())"
        create_user_data = {'access_token': info['access_token'], 'name': info['name'], 'email': info['email'], 'first_name': info['first_name'], 'headline': info['headline'], 'industry': info['industry'], 'location': info['location'], 'image_link': info['image_link']}
        return self.db.query_db(create_user_query, create_user_data)

    def update_user_token(self, info):
        update_query = "UPDATE linkedin_users SET access_token= :access_token, updated_at=NOW() WHERE email= :email"
        update_data = {'access_token': info['access_token'], 'email': info['email']}
        return self.db.query_db(update_query, update_data)


    def add_to_aplist(self,info):     
        create_arrangement_list_query = "INSERT INTO arrangements (linkedin_users_id, created_at, updated_at) VALUES (:linkedin_users_id, NOW(), NOW())"
        appoint_list_data = {'linkedin_users_id': info['user_id']}
        return self.db.query_db(create_arrangement_list_query, appoint_list_data)

    def show_applist(self):
        show_query = "SELECT linkedin_users.headline, linkedin_users.industry, linkedin_users.location, arrangement.linkedin_users_id FROM linkedin_users JOIN arrangement ON linkedin_users.id = arrangements.linkedin_users_id"
        return self.db.query_db(show_query)