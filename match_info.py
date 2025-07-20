import json 
import pandas as pd
import os







class info:
   
  def __init__(self,folder_path):
     self.json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
     self.folder_path = folder_path
  
  
  def info_2(self):
   player_data = []
   for json_file in self.json_files:
    file_path = os.path.join(self.folder_path, json_file)

    
    with  open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)


    info_1 = data['info']
    if isinstance(info_1, dict):   
        event = info_1.get('event', {})
        toss = info_1.get('toss', {})
        officials = info_1.get('officials', {})
        outcome = info_1.get('outcome', {})
        players = info_1.get('players', {})
        team_1, team_2 = list(players.keys()) if len(players) == 2 else (None, None)
        team_1_players = ", ".join(players[team_1]) if team_1 else None
        team_2_players = ", ".join(players[team_2]) if team_2 else None
        player_data.append({
                    "balls_per_over": info_1.get('balls_per_over'),
                    "city": info_1.get('city'),
                    "dates": info_1['dates'][0],
                    "event_name": event.get('name'),
                    "match_number_event": event.get('match_number'),
                    "gender": info_1.get('gender'),
                    "match_type": info_1.get('match_type'),
                    "match_number_type": info_1.get('match_type_number'),
                    "overs": info_1.get('overs'),
                    "player_of_match": info_1['player_of_match'][0] if 'player_of_match' in info_1 else None,
                    "season": info_1.get('season'),
                    "team_type": info_1.get('team_type'),
                    "venue": info_1.get('venue'),
                    "team_1": info_1['teams'][0],
                    "team_2": info_1['teams'][1],
                    "team_1": team_1,
                    "team_2": team_2,
                    "team_1_players": team_1_players,
                    "team_2_players": team_2_players,
                    "decision": toss.get('decision'),
                    "toss_winner": toss.get('winner'),
                    "match_referees": info_1['officials']['match_referees'][0] if 'match_referees' in officials else None,
                    "reserve_umpires": info_1['officials']['reserve_umpires'][0] if 'reserve_umpires' in officials else None,
                    "tv_umpires":info_1['officials']['tv_umpires'][0] if 'tv_umpires' in officials else None,
                    "umpires_1": officials.get('umpires', [None])[0] if officials.get('umpires') else None,
                    "umpires_2": officials.get('umpires', [None, None])[1] if officials.get('umpires') and len(officials.get('umpires')) > 1 else None,
                    "winner": outcome.get('winner'),
                    "by": outcome.get('by', {}).get('runs')
                })
   return  player_data     

  



