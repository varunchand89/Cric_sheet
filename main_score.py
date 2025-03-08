import pandas as pd
from match_score import score
import mysql.connector
import urllib.parse
from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

mydb =mysql.connector.connect(host="localhost",user="root",password="Varunchand@8",database="Cric_sheet")
password = urllib.parse.quote("Varunchand@8")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/Cric_sheet")
mycursor = mydb.cursor()

#score cleaning 
#test = C:/Users/Hp/Downloads/tests_json
#t20  = C:/Users/Hp/Downloads/t20s_json
#odi  = C:/Users/Hp/Downloads/Json_files_cric/odis_json

folder_path = "C:/Users/Hp/Downloads/tests_json"
score_2 = score(folder_path)
score_data = score_2.score_1()

df = pd.DataFrame(score_data)



df['overs'] = df['overs'].fillna("innings finished")
df['batter'] = df['batter'].fillna("0")
df['bowler'] = df['bowler'].fillna("innings finished")
df['non_striker'] = df['non_striker'].fillna("innings finished")
df['batter_runs'] = df['batter_runs'].fillna("innings finished")
df['extra_runs'] = df['extra_runs'].fillna("innings finished")
df['total_runs'] = df['total_runs'].fillna("innings finished")
df['wicket'] = df['wicket'].fillna("not yet")
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
 df['target_overs'] = df['target_overs'].fillna("50")



try:
    batch_size = 1000
    for i in range(0, len(df), batch_size):
      df_batch = df.iloc[i:i+batch_size]
      df_batch.to_sql(name="match_score_test", if_exists="append", con=engine, index=False)
   
except Exception as e:
    
    print(f"Error: {e}")

