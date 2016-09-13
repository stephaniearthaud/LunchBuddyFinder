
from system.core.model import Model

class Arrangement(Model):
    def __init__(self):
        super(Arrangement, self).__init__()


#arrangement methods
    def get_all_locations(self):
    	get_all_locations_query = "SELECT location FROM locations"
    	query = self.db.query_db(get_all_locations_query)
    	return query

    def add_arrangement(self, info):
        location = info['location']
        topic = info['topic_id']
        errors = []
        if not location:
            errors.append('You need to select a location')
        if not topic:
            errors.append('You need to select a topic')
        if errors:
            return {'status': False, 'errors': errors}
        else:
            add_arrangement_query = "INSERT INTO arrangements (topic_id, linkedin_user_id, location_id, created_at, updated_at) VALUES(:topic_id, :id, :location, NOW(), NOW())"
            add_arrangement_data = {'topic_id': info['topic_id'], 'id': info['id'], 'location': info['location']}
            self.db.query_db(add_arrangement_query, add_arrangement_data)
            return {'status': True}

    def add_full_arrangement(self, info):
        add_arrangement_query = "INSERT INTO arrangements (topic_id, linkedin_user_id, friend, location_id, created_at, updated_at) VALUES(:topic_id, :id, :friend_id, :location, NOW(), NOW())"
        add_arrangement_data = {'topic_id': info['topic_id'], 'id': info['id'], 'friend_id': info['friend_id'], 'location': info['location']}
        return self.db.query_db(add_arrangement_query, add_arrangement_data)

    def delete_arrangement(self, info):
        delete_arrangement_query = "DELETE FROM arrangements WHERE linkedin_user_id= :linkedin_user_id"
        delete_arrangement_data = {'linkedin_user_id': info['id']}
        return self.db.query_db(delete_arrangement_query, delete_arrangement_data)

    def get_all_arrangements(self):
        query = "SELECT DISTINCT topic, location, arrangements.created_at FROM arrangements JOIN topics ON topics.id = arrangements.topic_id JOIN locations ON locations.id = arrangements.location_id WHERE arrangements.friend IS NOT NULL AND arrangements.created_at = CURDATE()"
        return self.db.query_db(query)

    def get_availables(self):
    	query = 'SELECT linkedin_users.name, linkedin_users.headline, linkedin_users.industry, locations.location, arrangements.linkedin_user_id, topics.topic FROM linkedin_users JOIN arrangements ON linkedin_users.id = arrangements.linkedin_user_id JOIN topics ON topics.id = arrangements.topic_id JOIN locations ON locations.id = arrangements.location_id WHERE arrangements.friend IS NULL AND arrangements.created_at = CURDATE()'
        x = self.db.query_db(query)
    	return x

    def get_aplist(self,info):
        select_query = "SELECT * FROM arrangements WHERE linkedin_user_id = :linkedin_user_id AND arrangements.created_at = CURDATE()"
        data = {'linkedin_user_id': info['user_id']}
        x = self.db.query_db(select_query,data)
        return x

    def get_user_info(self, info):
        get_user_query = "SELECT * FROM linkedin_users WHERE id = :user_id"
        get_user_data = {'user_id': info['user_id']}
        return self.db.query_db(get_user_query, get_user_data)

    def get_user(self, info):
        get_user_query = "SELECT linkedin_user_id FROM arrangements WHERE linkedin_user_id = :linkedin_user_id"
        get_user_data = {'linkedin_user_id': info['user_id']}
        return self.db.query_db(get_user_query, get_user_data)

    def get_friend(self, info):
        get_friend_query = "SELECT friend FROM arrangements WHERE friend = :friend AND arrangements.created_at = CURDATE()"
        get_friend_data = {'friend': info['friend_id']}
        return self.db.query_db(get_friend_query, get_friend_data)

    def add_friend(self, info):
        add_friend_query = "UPDATE arrangements SET friend = :friend WHERE linkedin_user_id = :linkedin_user_id AND created_at = CURDATE()"
        add_friend_data = {'friend': info['friend_id'], 'linkedin_user_id': info['user_id']}
        return self.db.query_db(add_friend_query, add_friend_data)

    def get_friend_id(self, info):
        get_friend_id_query = "SELECT friend, linkedin_user_id FROM arrangements JOIN linkedin_users ON arrangements.friend = linkedin_users.id WHERE linkedin_user_id = :linkedin_user_id AND arrangements.updated_at > CURDATE() OR friend = :friend AND arrangements.updated_at > CURDATE()"
        get_friend_id_data = {'linkedin_user_id': info['id'], 'friend': info['id']}
        return self.db.query_db(get_friend_id_query, get_friend_id_data)

    def get_friend_info(self, info):
        get_friend_query = "SELECT * FROM arrangements WHERE linkedin_user_id = :linkedin_user_id AND arrangements.updated_at > CURDATE()"
        get_friend_data = {'linkedin_user_id': info['id']}
        data = self.db.query_db(get_friend_query, get_friend_data)
        if data.length > 0:
            return data
        else:
            get_friend_query = "SELECT * FROM arrangements WHERE friend = :friend AND arrangements.updated_at > CURDATE()"
            get_friend_data = {'friend': info['id']}
            return self.db.query_db(get_friend_query, get_friend_data)

#topic methods
    def get_topic_id(self, info):
    	query = "SELECT id from topics WHERE topic= :topic"
    	data = {'topic': info['topic']}
    	return self.db.query_db(query, data)

    def add_topic(self, info):
    	query = "INSERT INTO topics (topic, created_at, updated_at) VALUES(:topic, NOW(), NOW())"
    	data = {'topic': info['topic']}
    	return self.db.query_db(query, data)

    def get_all_topics(self):
    	query = "SELECT topic from topics"
    	return self.db.query_db(query)

    def get_topic_by_name(self, info):
        query = "SELECT * FROM topics WHERE topic= :topic"
        data = {'topic': info['topic']}
        return self.db.query_db(query, data)

#location methods
    def add_location(self, info):
        query = "INSERT INTO locations (location, created_at, updated_at) VALUES(:location, NOW(), NOW())"
        data = {'location': info['location']}
        return self.db.query_db(query, data)

    def get_location_by_name(self, info):
        query = "SELECT * FROM locations WHERE location= :location"
        data = {'location': info['location']}
        return self.db.query_db(query, data)

    def get_all_locations(self):
        query = "SELECT * FROM locations"
        return self.db.query_db(query)


    def get_location_id(self, info):
        query = "SELECT id from locations WHERE location= :location"
        data = {'location': info['location']}
        return self.db.query_db(query, data)
