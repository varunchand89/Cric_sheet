import pandas as pd
import numpy as np
from match_info import info
import mysql.connector
import urllib.parse
from  sqlalchemy import create_engine

mydb =mysql.connector.connect(host="localhost",user="root",password="Varunchand@8",database="Cric_sheet")
password = urllib.parse.quote("Varunchand@8")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/Cric_sheet")
mycursor = mydb.cursor()

#score cleaning 
#test = C:/Users/Hp/Downloads/tests_json
#t20  = C:/Users/Hp/Downloads/t20s_json
#odi  = C:/Users/Hp/Downloads/Json_files_cric/odis_json

folder_path = "C:/Users/Hp/Downloads/tests_json"
info_object = info(folder_path)  
player_data = info_object.info_2()

df = pd.DataFrame(player_data)


df['match_referees'] = df['match_referees'].fillna('Jack Badley')
df['reserve_umpires'] = df['reserve_umpires'].fillna('Javed Akhtar')
df['umpires_1'] = df['umpires_1'].fillna('Brian Aldridge')
df['umpires_2'] = df['umpires_2'].fillna('Jack Badley')
df['city'] = df['city'].fillna('India')
df['event_name'] = df['event_name'].fillna('test_internationals')
df['tv_umpires'] = df['tv_umpires'].fillna('Richard Kettleborough')
df['by'] = df['by'].fillna(np.random.choice(range(1,100)))



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


df.to_sql(name= "match_info_test",con=engine,if_exists="replace",index=False)


import pandas as pd
import numpy as np
from match_info import info
import mysql.connector
import urllib.parse
from  sqlalchemy import create_engine

mydb =mysql.connector.connect(host="localhost",user="root",password="Varunchand@8",database="Cric_sheet")
password = urllib.parse.quote("Varunchand@8")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/Cric_sheet")
mycursor = mydb.cursor()

#score cleaning 
#test = C:/Users/Hp/Downloads/tests_json
#t20  = C:/Users/Hp/Downloads/t20s_json
#odi  = C:/Users/Hp/Downloads/Json_files_cric/odis_json

folder_path = "C:/Users/Hp/Downloads/tests_json"
info_object = info(folder_path)  
player_data = info_object.info_2()

df = pd.DataFrame(player_data)


df['match_referees'] = df['match_referees'].fillna('Jack Badley')
df['reserve_umpires'] = df['reserve_umpires'].fillna('Javed Akhtar')
df['umpires_1'] = df['umpires_1'].fillna('Brian Aldridge')
df['umpires_2'] = df['umpires_2'].fillna('Jack Badley')
df['city'] = df['city'].fillna('India')
df['event_name'] = df['event_name'].fillna('test_internationals')
df['tv_umpires'] = df['tv_umpires'].fillna('Richard Kettleborough')
df['by'] = df['by'].fillna(np.random.choice(range(1,100)))



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


df.to_sql(name= "match_info_test",con=engine,if_exists="replace",index=False)

