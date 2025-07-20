import pandas as pd
from players_id import id
import mysql.connector
import pandas as pd
import streamlit as st
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


folder_path = "C:/Users/Hp/Downloads/Json_files_cric/odis_json"



id_object = id(folder_path)  
player_data = id_object.id_1()

df = pd.DataFrame(player_data)



dz = df.drop_duplicates(subset = ['players_name','players_id',],keep="first")





dz.to_sql(name = "players_id_odi", con=engine, if_exists="replace", index=True)





