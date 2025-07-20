import json 
import pandas as pd
import os

class score():
 
 def __init__(self, folder_path):
   self.json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
   self.folder_path = folder_path
    
 def score_1(self): 
    record_1=[]  
    for json_file in self.json_files:
      file_path = os.path.join(self.folder_path, json_file)

      with open(file_path, "r", encoding="utf-8") as f:
          data = json.load(f)
      info_1 = data['info']
      event = info_1.get('event', {})
      for teams in data['innings']:
          team = teams["team"]
          for overs in teams['overs']:
              overs_1 = overs['over']
              ball_count = 0
              for deliverie in overs['deliveries']:
                  runs = deliverie.get("runs")
                  wicket = None
                  kind = None
                  if 'wickets' in deliverie:
                      for wicket_info in deliverie['wickets']:
                          wicket = wicket_info.get('player_out')
                          kind = wicket_info.get('kind')
                  current_over = f"{overs_1}.{ball_count}"
                  ball_count +=1  
                  
                  record_1.append({
                      "dates": info_1['dates'][0],
                      "event_name": event.get('name'),
                      "match_number_event": event.get('match_number'),
                      "match_number_type": info_1.get('match_type_number'),
                      "team": team,
                      "overs": current_over,
                      "batter": deliverie.get('batter'),
                      "bowler": deliverie.get('bowler'),
                      "non_striker": deliverie.get('non_striker'),
                      "batter_runs": runs.get('batter'),
                      "extra_runs": runs.get('extras'),
                      "total_runs": runs.get('total'),
                      "wicket": wicket,
                      "kind": kind})

          if "target" in teams:
              target = teams["target"]
              target_runs = target.get("runs")
              target_overs = target.get("overs")

              record_1.append({
                  "team": team,
                  "target_runs": target_runs,
                  "target_overs": target_overs
              }) 
          
          if "powerplays" in teams:
              for powerplay in teams["powerplays"]:
                  record_1.append({
                      "team": team,
                      "powerplay_from": powerplay.get("from"),
                      "powerplay_to": powerplay.get("to"),
                      "powerplay_type": powerplay.get("type")
                  })    

    return record_1 



