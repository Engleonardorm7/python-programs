import sys
clients = 'kelly, leonardo,'

def create_client(client_name):
	global clients

	if client_name not in clients :
		clients += client_name
		_add_comma()
	else:
		print ('Client already is in the client\'s list')

def list_clients():
	global clients

	print(clients)


def updated_client(client_name, updated_client_name):
	global clients

	if client_name in clients :
		clients = clients.replace (client_name + ',', updated_client_name + ',' )
	else:
		print ('Client is no it client\'s list')


def delete_client(client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', '')
	else:
		print('Client is not in client\'s list')

def search_client(client_name):
	clients_list = clients.split(',')

	for client in clients_list:
		if client != client_name:
			continue
		else:
			return True

def _add_comma():
	global clients

	clients += ','


def _print_welcome():
	print ('WELCOME')
	print ('What would you like to do? ')
	print ('[C]reate client')
	print ('[L]ist client')
	print ('[U]pdated client')
	print ('[D]elete client')
	print ('[S]earch client')


def _get_client_name ():
	client_name = None

	while not client_name:
		client_name = str.lower(input('What is the client name ? '))

		if client_name == 'exit':
			client_name = None
			break

	if not client_name:
			sys.exit()

	return client_name

if __name__ == '__main__':
	_print_welcome()

	command = input()
	command = command.upper()

	if command == 'C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'L':
		list_clients()
	elif command == 'U':
		client_name = _get_client_name()
		updated_client_name = str.lower(input ('What is the updated client name ? '))
		updated_client(client_name, updated_client_name)
		list_clients()
	elif command == 'D':
		client_name = _get_client_name()
		delete_client(client_name)
		list_clients()
	elif command == 'S':
		client_name = _get_client_name()
		found = search_client(client_name)

		if found:
			print('The client is in the client\'s list')
		else:
			print('The client: {} is not in our client\'s list'.format(client_name))

	else:
		print ('Invalid command')