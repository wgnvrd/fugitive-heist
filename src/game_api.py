from pymongo import MongoClient
password = input("password for konohatomonoduval: ")
client = MongoClient("mongodb+srv://konohatomonoduval:" + password + "@anton-1.gzjzi9c.mongodb.net/test") 
db = client.get_database('fugitive_heist')
current_game = db.current_game

# Docu
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

    def set_new_player(self, name, team):
        new_player = {"name":name, "team":team, }
        if team == "guards":
            new_player.update({"captures":0})
        elif team == "fugitives":
            new_player.update({"gem_held":})
        current_game.insert_one()
        

    def create_player(self, name, team):
        pass     

    def create_gem(self):
        # maybe it's better to use a python class for this
        gem_dict = {
            "location_name": "",
            "gem_type": ""
        }
        pass
        