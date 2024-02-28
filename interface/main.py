from .interfaces.get_data import GetData
from .interfaces.auth import Auth
from .interfaces.database_check_exists import DatabaseCheckExists
from .interfaces.create_user import CreateUser

def register(
	database_check_exists: DatabaseCheckExists, 
	create_user: CreateUser,
	get_data: GetData, 
	auth: Auth,
):
	data = get_data.call()
	if auth.call(data):
		if not database_check_exists.call(data):
			create_user.call(data)


register()