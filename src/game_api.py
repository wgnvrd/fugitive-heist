from pymongo import MongoClient
import json

with open("config.json") as f:
        config = json.load(f)
        password = config["MONGO_PASSWORD"]
client = MongoClient("mongodb+srv://konohatomonoduval:" + password + "@anton-1.gzjzi9c.mongodb.net/test") 
db = client.get_database('fugitive_heist')
current_game = db.current_game

# Documents
# Games
# Players

class GameAPI():
    def __init__(self):
        self.game_state = {
            'game_id': 1,
            'status': 'Running',
            'leader': '', # a user id
            'fugitives': [], # stores references to player_ids
            'guards': [],
            'gems': []
        }
    
    def set_game_leader(self, discord_id):
        self.game_state.leader = discord_id

    def get_game_leader(self):
        return self.game_state.leader

    def set_new_player(self, discord_id, team):
        new_player = {"discord_id":discord_id, "team":team, }
        if team == "guards":
            new_player.update({"captures":0})
        elif team == "fugitives":
            new_player.update({"gem_held":0, "has_supplies":True, "is_tagged":False})

        current_game.insert_one(new_player)

    def create_gem(self):
        # maybe it's better to use a python class for this
        gem_dict = {
            "location_name": "",
            "gem_type": ""
        }
        

if __name__=="__main__":
    api = GameAPI()
    
    api.set_new_player("1234", "guards")
    print("hello")
