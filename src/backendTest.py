#MongoDB basics: https://www.youtube.com/watch?v=pWbMrx5rVBE
#Atlas with pymongo: https://www.youtube.com/watch?v=VQnmcBnguPY
#Figure out how to limit values (just guards/thieves), how to modify existing documents with object ID, require capture field for guards
#   There might be something called object templates? We can make one for each entity

from pymongo import MongoClient
password = input("password for konohatomonoduval: ")
client = MongoClient("mongodb+srv://konohatomonoduval:" + password + "@anton-1.gzjzi9c.mongodb.net/test") 
db = client.get_database('fugitive_heist')
playerDB = db.Players
print(playerDB.count_documents({}))

new_player = {'name':'Kazu', 'team':'guards', 'captures':0}

#playerDB.insert_one(new_player)

playersList = list(playerDB.find())
print(playersList)

kazu = playerDB.find_one({'name':'Kazu'})

print(kazu)

def increment_captures(player_name): #switch to using object IDs in case of repeats
    current_captures = playerDB.find_one({'name':player_name})['captures']
    update = {'captures': current_captures + 1}
    playerDB.update_one({'name':'Kazu'}, {'$set':update})

#increment_captures('Kazu')
