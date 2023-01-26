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

def create_new_card(idList, name, due):
	url = 'https://api.trello.com/1/cards'

	query['name'] = name
	query['due'] = due
	query['idList'] = idList
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


create_new_card(queueId, "TESTING", "2017-05-19T14:00:00")


