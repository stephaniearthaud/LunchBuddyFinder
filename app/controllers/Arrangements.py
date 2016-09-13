from system.core.controller import *
import datetime

class Arrangements(Controller):
    def __init__(self, action):
        super(Arrangements, self).__init__(action)
        self.load_model('Arrangement')
        self.load_model('User')

    def index(self):
    	return redirect('/users/dashboard')

    def match(self):
        info = {
            'id': session['id']
        }
        friend_id = self.models['Arrangement'].get_friend_id(info)
        if session['id'] == friend_id[0]['friend']:
            friend = friend_id[0]['linkedin_user_id']    
        else:
            friend = friend_id[0]['friend']
        friend_info = {
            'user_id': friend
        }
        friend_user = self.models['Arrangement'].get_user_info(friend_info)

        if session['id'] == friend_id[0]['friend']:
            friend_checkers = {
                'user_id': friend_id[0]['linkedin_user_id']
            }
            friend_check = self.models['Arrangement'].get_user(friend_checkers)
        else:
            friend_checkers = {
                'friend_id': friend_id[0]['friend'] 
            } 
            friend_check = self.models['Arrangement'].get_friend(friend_checkers)
        
        
        return self.load_view('/arrangements/match.html', friend_user=friend_user[0], friend_check=friend_check)

    def add(self):

        if request.form['topic_new']:
            topic = request.form['topic_new']
            a = {
                'topic': topic
            }
            topic_check = self.models['Arrangement'].get_topic_by_name(a)
            if topic_check:
                print "topic already exists"
            else:
                self.models['Arrangement'].add_topic(a)
    	else:
    		topic = request.form['topic']

    	if request.form['location_new']:
            location = request.form['location_new']
            b = {
                'location': location
            }
            location_check = self.models['Arrangement'].get_location_by_name(b)
            if location_check:
                print "location already exists"
            else:
                self.models['Arrangement'].add_location(b)
    	else:
    		location = request.form['location']

    	topic_info = {
    		'topic': topic
    	}
    	topic_id = self.models['Arrangement'].get_topic_id(topic_info)

        location_info = {
            'location': location
        }
        location_id = self.models['Arrangement'].get_location_id(location_info)
        date = datetime.date.today()
        add_id = {
            'user_id': session['id']
        }
        get = self.models['Arrangement'].get_aplist(add_id)
        if get:
            date2 = get[0]['created_at']
            if date2 == date:
                flash('You are already on the list for today')
            return self.load_view('partials/flash.html')
            # return redirect('/users/dashboard')
        else:
            friend_info = {
                'friend_id': session['id']
            }
            friend_check = self.models['Arrangement'].get_friend(friend_info)
            if not friend_check:
                info = {
                    'id': session['id'],
                    'topic_id': topic_id[0]['id'],
                    'location': location_id[0]['id'],
                }
                add_status = self.models['Arrangement'].add_arrangement(info)
                if add_status['status'] == True:
                    # return redirect('/users/dashboard')
                    return ''
                else:
                    for message in add_status['errors']:
                        flash(message)
                    # return redirect('/users/dashboard')
                    return self.load_view('partials/flash.html')
            else:
                flash('You are already on the list for today')
                # return redirect('/users/dashboard')
                return self.load_view('partials/flash.html')

    def delete(self, id):
        delete_id = id
        info = {
            'id': delete_id
        }
        self.models['Arrangement'].delete_arrangement(info)
        availables = self.models['Arrangement'].get_availables()
        return redirect('/users/dashboard')

    def friend(self, id):
    	user_id = id
        friend_id = session['id']
        availables = self.models['Arrangement'].get_availables()
        user_info = {
            'user_id': user_id
        }
        user_check = self.models['Arrangement'].get_user(user_info)
        friend_info = {
            'friend_id': friend_id
        }
        friend_check = self.models['Arrangement'].get_friend(friend_info)

        if user_id == friend_id:
            flash('You can not eat with yourself!')
            return redirect('/users/dashboard')
        else:
            info = {
                'friend_id': friend_id,
                'user_id': user_id
            }
            self.models['Arrangement'].add_friend(info)

        info_check = {
            'user_id': friend_id
        }
        get_user = self.models['Arrangement'].get_user(info_check)
        print get_user
        if get_user:
            info2 = {
                'friend_id': user_id,
                'user_id': friend_id
            }
            self.models['Arrangement'].add_friend(info2)
            return redirect('/arrangements/match')
        else:
            info3 = {
                'id': user_id
            }
            get_friend_info = self.models['Arrangement'].get_friend_info(info3)
            topic = get_friend_info[0]['topic_id']
            location = get_friend_info[0]['location_id']
            full_info = {
                'friend_id': user_id,
                'id': friend_id,
                'topic_id': topic,
                'location': location
            }
            get_user = self.models['Arrangement'].add_full_arrangement(full_info)
            return redirect('/arrangements/match')

    def get_availables(self):
        availables = self.models['Arrangement'].get_availables()
        return self.load_view('partials/arrangements.html', availables=availables)

    def get_flash(self):
        return self.load_view('partials/flash.html')

    def get_arrangements(self):
        return self.load_view('partials/conversation.html')
