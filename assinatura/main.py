from .auth import *
from .get_data import *
from .create_user import *
from .database_check_exists import *

# Este fluxo funciona desde que a assinatura de cada uma das funcionalidades deste fluxo sejam garantidas
def register():
	data = get_data()

	if auth(data):
		if not database_check_exists(data):
			create_user(data)


register()