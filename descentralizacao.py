# Descentralização: Dividir um fluxo em processos que não possuam dependencias entre sí
# - Principio de responsabilidade unica: cada função que compõe um fluxo deve possuir apenas uma responsabilidade dentro da mesmo


# Ao criar o fluxo registrar, divida o seu funcionamento em processos

def get_data():
	pass

def auth():
	pass

def database_check_exists():
	pass

def create_user():
	pass


def registrar():
	data = get_data()
	if auth(data):
		if not database_check_exists():
			create_user()


