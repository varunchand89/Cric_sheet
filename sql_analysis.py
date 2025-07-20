import pandas as pd
from match_score import score
import mysql.connector
import urllib.parse
from  sqlalchemy import create_engine

mydb =mysql.connector.connect(host="localhost",user="root",password="Varunchand@8",database="Cric_sheet")
password = urllib.parse.quote("Varunchand@8")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/Cric_sheet")
mycursor = mydb.cursor()

#sql_analysis



query_1 = "SELECT batter, SUM(batter_runs) AS Total_runs FROM match_score_odi GROUP BY batter ORDER BY Total_runs  DESC limit  10 "
df = pd.read_sql(query_1,con = engine)


query_2 = "SELECT bowler, count(wicket) AS Total_wicket FROM match_score_odi WHERE wicket != 'not yet' GROUP BY bowler ORDER BY Total_wicket DESC;"
dz = pd.read_sql(query_2,con=engine)


query_3 = "SELECT winner, COUNT(winner) AS Total_times,ROUND((COUNT(winner) * 100.0) / (SELECT COUNT(winner) FROM match_info_test), 2) AS Win_Percentage from match_info_test group by winner order by Total_times DESC"
dg = pd.read_sql(query_3,con=engine)


query_4 = "SELECT dates,team_1,team_2,winner,`by` from match_info_odi ORDER BY CAST(`by` AS DECIMAL) ASC "
dh = pd.read_sql(query_4,con = engine) 

