import api

class Card:
    def __init__(self, list : str, name : str, label : str, due : str):
        self.list = list
        self.listId = api.getListIdByName()
        self.name = name
        self.label = label
        self.labelId = api.getLabelIdByName()
        self.due = due

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






