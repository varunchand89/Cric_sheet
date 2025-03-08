import json 
import pandas as pd
import os

class id():
  
  def __init__(self,folder_path):
      self.json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
      self.folder_path = folder_path
       
  def id_1(self):
   record = []
   for json_file in self.json_files:
    file_path = os.path.join(self.folder_path, json_file)

    
    with  open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    info_1 = data['info']
    for registry in info_1.get('registry').values():
            for people_name, people_id in registry.items():
                    record.append({
                    "players_name": people_name,
                    "players_id": people_id
                })
   return record                
                  



