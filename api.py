import requests
import config

url = 'https://api.trello.com/1/'
boardId = '61f2d57bc0130938a690edd4'
queueId = '61f2d57bc0130938a690edd5'

headers = {
  "Accept": "application/json"
}

query = {
  'key': config.api_key,
  'token': config.api_token,
}

def get(url, params = []):
	query.update(query)
	return requests.request(
		"GET",
		url,
		params = query
	).json()

def post(url, params):
	query.update(query)
	return requests.request(
		"POST",
		url,
		params = query
	).json()
	
# Labels

def get_label_id_by_name(boardId = '61f2d57bc0130938a690edd4', name = "personal"):
	url = 'https://api.trello.com/1/board/{}/labels'.format(boardId)

	response = get(url)

	for label in response:
		if label['name'] == name:
			return label['id']

def create_idLabels_from_names(names):
	ids = []
	for name in names:
		ids.append(get_label_id_by_name(name = name))

	return ids

# Cards

def create_new_card(name, due, idLabels, idList = '61f2d57bc0130938a690edd5'):
	url = 'https://api.trello.com/1/cards'

	query['name'] = name
	query['due'] = due
	query['idList'] = idList
	query['idLabels'] = idLabels

	print(post(url, query))

# Lists

def get_lists_from_board(boardId):
	url = "https://api.trello.com/1/boards/{}/lists".format(boardId)
	return get(url)

# Boards

def get_boards():
	url = 'https://api.trello.com/1/'
	url += 'members/me/boards'
	return get(url)

# Helper

# Date Format YYYY-MM-DDTHH:mm:ssZ
def date_formatter(year, month, day, time = "11:59:59"):
	return "{}-{}-{}T{}Z".format(year, month, day, time)
