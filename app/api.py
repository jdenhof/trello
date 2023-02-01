import requests
import config
import debug

url = 'https://api.trello.com/1/'

query = {
  'key': config.api_key,
  'token': config.api_token,
}

def get(url, params = []):
	return call("GET", url, params)

def post(url, params):
	return call("POST", url, params)

def call(request, url, params):
	query.update(params)
	return requests.request(
		request,
		url,
		params = query
	).json()

# Labels

def getLabelsFromBoard(boardId):
	labels = []
	for label in get('https://api.trello.com/1/board/{}/labels'.format(boardId)):
		labels.append(label['name'])
	return labels



def getLabelIdByName(name, board):

	labels = get('https://api.trello.com/1/board/{}/labels'.format(boardId))

	for label in labels:
		if label['name'] == name:
			return label['id']

# Cards

def createNewCard(idList, name, idLabel, due):
	url = 'https://api.trello.com/1/cards'

	query['name'] = name
	query['due'] = due
	query['idList'] = idList
	query['idLabels'] = idLabel

	response = post(url, query)
	if debug.DEBUG:
		print("id: ", response['id'])

# Lists

def getListsByName():

	lstNames = []
	
	for list in getListsFromBoard():
		lstNames.append(list['name'])

	return lstNames

def getListIdByName(name):

	for list in getListsFromBoard():
		if list['name'] == name:
			return list['id']
	# Current Queue ID
	return '61f2d57bc0130938a690edd5'

def getListsFromBoard(boardId = '61f2d57bc0130938a690edd4'):
	url = "https://api.trello.com/1/boards/{}/lists".format(boardId)
	return get(url)

# Boards

def getBoardIdFromName(board : str):

	for boardObj in getListOfBoards():
		if boardObj['name'] == board:
			return boardObj['id']
	return 

def getListOfBoardNames():
	names = []
	for board in getListOfBoards():
		if board['closed'] == False:
			names.append(board['name'])
	return names

def getListOfBoards():
	url = 'https://api.trello.com/1/members/me/boards'
	return get(url)