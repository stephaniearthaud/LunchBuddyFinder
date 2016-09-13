
from system.core.router import routes

#user routes
routes['default_controller'] = 'Users'
routes['/users/auth'] = 'Users#auth'
routes['/users/logout'] = 'Users#logout'
routes['/users/dashboard'] = 'Users#dashboard'
routes['/users/callback'] = 'Users#callback'
routes['/users/get_info'] = 'Users#get_info'
routes['/users/create'] = 'Users#create'
routes['/users/profile'] = 'Users#profile'
routes['/code'] = "Users#code"

# routes for arrangements
routes['POST']['/users/add'] = 'Users#add_to_aplist'
routes['/arrangements/get_availables'] = 'Arrangements#get_availables'
routes['/arrangements/get_flash'] = 'Arrangements#get_flash'
routes['/arrangements/get_arrangements'] = 'Arrangements#get_arrangements'


#arrangements routes
routes['/arrangements'] = 'Arrangements#index'
routes['/arrangements/match'] = 'Arrangements#match'
routes['POST']['/arrangements/form'] = 'Arrangements#form'
routes['POST']['/arrangements/add'] = "Arrangements#add"
routes['POST']['/arrangements/buddy/<id>'] = 'Arrangements#friend'
routes['POST']['/arrangements/delete/<id>'] = 'Arrangements#delete'