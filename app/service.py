import api

class Card:
    def __init__(self, board : str, list : str, name : str, label : str, day, month, year):
        self.list = list
        self.listId = api.getListIdByName(list)
        self.name = name
        self.label = label
        self.labelId = api.getLabelIdByName(label, board)
        self.due = dateFormatter(year, month, day)
        self.board = board

def getListOfListOptions() -> list:
    options = []
    for list in api.getListsFromBoard(): options.append(list['name']) 
    return options

def getListOfLabelOptions(board) -> list:
    return api.getLabelsFromBoard(api.getBoardIdFromName(board))

def getListOfBoardOptions() -> list:
    return api.getListOfBoardNames()

def createNewCard(card : Card):
    api.createNewCard(card.listId, card.name, card.labelId, card.due)

# Date Format YYYY-MM-DDTHH:mm:ssZ
def dateFormatter(year, month, day, time = "11:59:59"):
	if len(day) == 1:
		day = "0" + day
	if len(month) == 1:
		month = "0" + month
	return "{}-{}-{}T{}Z".format(year, month, day, time)






