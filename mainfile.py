import pandas as pd
import numpy as np
from match_info import info
import mysql.connector
import urllib.parse
from  sqlalchemy import create_engine
from visualization import information

mydb =mysql.connector.connect(host="localhost",user="root",password="Varunchand@8",database="Cric_sheet")
password = urllib.parse.quote("Varunchand@8")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/Cric_sheet")
mycursor = mydb.cursor()




folder_path = "C:/Users/Hp/Downloads/t20s_json"
info_object = information(folder_path)  
player_data = info_object.info_3()

df = pd.DataFrame(player_data)

df['match_referees'] = df['match_referees'].fillna('Suresh Shastri')
df['reserve_umpires'] = df['reserve_umpires'].fillna('Gamini Silva')
df['umpires_1'] = df['umpires_1'].fillna('Aleem Dar')
df['umpires_2'] = df['umpires_2'].fillna('Jeff Luck')
df['city'] = df['city'].fillna('india')
df['event_name'] = df['event_name'].fillna('T20_internationals')
df['tv_umpires'] = df['tv_umpires'].fillna('Richard Kettleborough')
df['by'] = df['by'].fillna('60')



for toss_winner in df['toss_winner']:
    df['winner'] = df['winner'].fillna(toss_winner)


df['team_1_players']= df['team_1_players'].apply(lambda x: x.split(',') if isinstance(x, str) else x)
df['team_2_players'] = df['team_2_players'].apply(lambda x: x.split(',') if isinstance(x, str) else x)
df['player_of_match'] = df.apply(
    
    lambda row: np.random.choice(row['team_1_players']+row['team_2_players']) if pd.isna(row['player_of_match']) else row['player_of_match'], 
    axis=1
)
df['team_1_players']= df['team_1_players'].apply(lambda x: ','.join(x) if isinstance(x, list) else x)
df['team_2_players'] = df['team_2_players'].apply(lambda x: ','.join(x) if isinstance(x, list) else x)

df['overs'] = df['overs'].fillna("innings finished")
if 'batter' in df.columns:
 df['batter'] = df['batter'].fillna("innings finished")
if 'bowler' in df.columns: 
 df['bowler'] = df['bowler'].fillna("innings finished")
if 'non_striker' in df.columns:
 df['non_striker'] = df['non_striker'].fillna("innings finished")
if 'batter_runs' in df.columns:
 df['batter_runs'] = df['batter_runs'].fillna("innings finished")
if 'extra_runs' in df.columns:
 df['extra_runs'] = df['extra_runs'].fillna("innings finished")
if  'total_runs' in df.columns: 
 df['total_runs'] = df['total_runs'].fillna("innings finished")
if 'wicket' in df.columns:
 df['wicket'] = df['wicket'].fillna("not yet")
if 'kind' in df.columns:
 df['kind'] = df['kind'].fillna("not yet")
if 'powerplay_from' in df.columns:
 df['powerplay_from'] = df['powerplay_from'].fillna("not available")
if 'powerplay_to' in df.columns:
 df['powerplay_to'] = df['powerplay_to'].fillna("not available")
if 'powerplay_type' in df.columns:
 df['powerplay_type'] = df['powerplay_type'].fillna("not available")
if 'target_runs' in df.columns:
 df['target_runs'] = df['target_runs'].fillna("0")
if 'target_overs' in df.columns:
 df['target_overs'] = df['target_overs'].fillna("20")



try:
    batch_size = 1000
    for i in range(0, len(df), batch_size):
      df_batch = df.iloc[i:i+batch_size]
      df_batch.to_sql(name="t20", if_exists="append", con=engine, index=False)
   
except Exception as e:
    
    print(f"Error: {e}")