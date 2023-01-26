import requests
import json
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

def get_label_id_by_name(boardId = '61f2d57bc0130938a690edd4', name = "personal"):
	url = 'https://api.trello.com/1/board/{}/labels'.format(boardId)

	response = requests.request(
		"GET",
		url,
		params = query
	).json()
	for label in response:
		if label['name'] == name:
			return label['id']

def create_idLabels_from_names(names):
	ids = []
	for name in names:
		ids.append(get_label_id_by_name(name = name))

	return ids

def create_new_card(name, due, idLabels, idList = '61f2d57bc0130938a690edd5'):
	url = 'https://api.trello.com/1/cards'

	query['name'] = name
	query['due'] = due
	query['idList'] = idList
	query['idLabels'] = idLabels

	response = requests.request(
		"POST",
		url,
		params = query
	)
	print(response.text)

def get_cards(idList):
	print('')

def get_list_id(boardId):
	url = "https://api.trello.com/1/boards/{boardId}/lists"
	response = requests.request(
		"GET",
		url,
		params=query
	)

	print(response.text)

def get_boards():
	url = 'https://api.trello.com/1/'
	url += 'members/me/boards'
	response = requests.request(
		"GET",
		url,
		params=query
	)
	print(response.text)


