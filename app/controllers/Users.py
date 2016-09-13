
from system.core.controller import *
from flask import abort, request
import oauth2 as oauth
import urllib
import urlparse
import requests
import requests.auth
import datetime
import time
import OAuth


class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Arrangement')

    def index(self):
        return self.load_view('/users/index.html')

    def logout(self):
        session.pop('name', None)
        session.pop('full_name', None)
        session.pop('headline', None)
        session.pop('industry', None)
        session.pop('location', None)
        session.pop('image_link', None)
        session.pop('id', None)
        session.pop('token', None)
        return redirect('/')

    def auth(self):
        client_id = OAuth.client_id

        redirect_uri = OAuth.redirect_uri
        authorization_base_url = 'https://www.linkedin.com/uas/oauth2/authorization?'

        data = {
            'client_id': OAuth.client_id,
            'response_type': 'code',
            'redirect_uri' : OAuth.redirect_uri,
            'state': "LunchTogethr",
            'scope' : 'r_basicprofile,r_emailaddress'
        }

        red_url = authorization_base_url + urllib.urlencode(data)
        if 'token' in session:
            return redirect('/users/dashboard')
        else:
            return redirect(red_url)


    def callback(self):
        token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'
        client_secret = OAuth.client_secret
        client_id = OAuth.client_id
        error = request.args.get('error', '')
        if error:
            return "Error: " + error
        state = request.args.get('state', '')
        if state != 'LunchToghethr':
            abort(403)
        code = request.args.get('code')
        client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': OAuth.redirect_uri,
            'client_id': OAuth.client_id,
            'client_secret': OAuth.client_secret
        }
        if 'token' not in session:
            response = requests.post(token_url, data=data)
            token_json = response.json()
            session['token'] = token_json['access_token']

            return redirect('/users/create')
        else:
            return redirect('/users/dashboard')

    def create(self):

        info_user = {
            'token': session['token']
        }
        user = self.models['User'].get_user(info_user)
        if user:
            session['id'] = user[0]['id']
            session['name'] = user[0]['name']
            session['email'] = user[0]['email']
            session['full_name'] = user[0]['full_name']
            session['headline'] = user[0]['headline']
            session['industry'] = user[0]['industry']
            session['location'] = user[0]['location']
            session['image_link'] = user[0]['image_link']

        else:
            red_url = 'https://api.linkedin.com/v1/people/~:(id,first-name,last-name,maiden-name,formatted-name,headline,location,industry,summary,specialties,picture-url,public-profile-url,email-address)?format=json'
            headers = {'Authorization': 'Bearer {}'.format(session['token'])}
            r = requests.get(red_url, headers=headers)
            data = r.json()

            check = {
                'email': data['emailAddress']
            }
            user_check = self.models['User'].get_user_by_email(check)
            if user_check:
                check = {
                'email': data['emailAddress'],
                'access_token': session['token']
                }
                self.models['User'].update_user_token(check)
            else:
                info_create = {
                    'access_token': session['token'],
                    'email': data['emailAddress'],
                    'name': data['formattedName'],
                    'first_name': data['firstName'],
                    'headline': data['headline'],
                    'industry': data['industry'],
                    'location': data['location']['name'],
                    'image_link': data['pictureUrl']
                }
                self.models['User'].create_user(info_create)

        return redirect('/users/dashboard')

    def dashboard(self):
        topics = self.models['Arrangement'].get_all_topics()
        locations = self.models['Arrangement'].get_all_locations()
        availables = self.models['Arrangement'].get_availables()
        arrangements = self.models['Arrangement'].get_all_arrangements()
        print "here"
        print arrangements
        if 'token' in session:
            info_user = {
                'token': session['token']
            }
            user = self.models['User'].get_user(info_user)
            if user:
                session['id'] = user[0]['id']
                session['name'] = user[0]['first_name']
                session['email'] = user[0]['email']
                session['full_name'] = user[0]['name']
                session['headline'] = user[0]['headline']
                session['industry'] = user[0]['industry']
                session['location'] = user[0]['location']
                session['image_link'] = user[0]['image_link']
        # currentdate = date.fromtimestamp(date)
        # friend_info = {
        #     'friend_id': session['id']
        # }
        # friend_check = self.models['Arrangement'].get_friend(friend_info)
        info = {
            'id': session['id']
            }
        friend_id = self.models['Arrangement'].get_friend_id(info)
        if friend_id:
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
        else:
            friend_info = {
                'friend_id': session['id']
            }
            friend_check = self.models['Arrangement'].get_friend(friend_info)
        return self.load_view('/users/dashboard.html', topics=topics, locations=locations, availables=availables, friend_check=friend_check, arrangements=arrangements)

    def get_info(self):
        red_url = 'https://api.linkedin.com/v1/people/~:(first-name,last-name,maiden-name,formatted-name,headline,location,industry,summary,specialties,picture-url,public-profile-url,email-address)?format=json'
        headers = {'Authorization': 'Bearer {}'.format(session['token'])}
        response = requests.get(red_url, headers=headers)
        usr_data = response.text

        return usr_data

    def add_to_aplist(self):
        date = datetime.date.today()
        print date
        add_status = {
            'user_id': session['id']
        }
        get = self.models['User'].get_aplist(add_status)

        if get:
            date2 = get[0]['created_at']
            if date2 == date :
                flash('You are already on the list for today' )

                return redirect('/users/dashboard')
        else:
            self.models['User'].add_to_aplist(add_status)
            return redirect('/users/dashboard')

    def profile(self):
        info = {
            'email': session['email']
        }
        user = self.models['User'].get_user_by_email(info)

        # friend_info = {
        #     'friend_id': session['id']
        # }
        info = {
            'id': session['id']
        }
        friend_id = self.models['Arrangement'].get_friend_id(info)
        if friend_id:
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
        else:
            friend_info = {
                'friend_id': session['id']
            }
            friend_check = self.models['Arrangement'].get_friend(friend_info)
        return self.load_view('/users/profile.html', user=user[0], friend_check=friend_check)
    # def show_aplist(self):
