import pandas as pd
from match_score import score
import mysql.connector
import urllib.parse
from  sqlalchemy import create_engine
import streamlit as st

mydb =mysql.connector.connect(host="localhost",user="root",password="Varunchand@8",database="Cric_sheet")
password = urllib.parse.quote("Varunchand@8")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/Cric_sheet")
mycursor = mydb.cursor()

#sql_analysis



query_1 = "SELECT batter, SUM(batter_runs) AS Total_runs FROM match_score_odi GROUP BY batter ORDER BY Total_runs  DESC limit  10 "
df = pd.read_sql(query_1,con = engine)
print(f"Query 1  : {df}")


query_2 = "SELECT bowler, count(wicket) AS Total_wicket FROM match_score_odi WHERE wicket != 'not yet' GROUP BY bowler ORDER BY Total_wicket DESC;"
dz = pd.read_sql(query_2,con=engine)
print(f"Query 2  : {dz}")


query_3 = "SELECT winner, COUNT(winner) AS Total_times,ROUND((COUNT(winner) * 100.0) / (SELECT COUNT(winner) FROM match_info_test), 2) AS Win_Percentage from match_info_test group by winner order by Total_times DESC"
dg = pd.read_sql(query_3,con=engine)
print(f"Query 3  : {dg}")


query_4 = "SELECT dates,team_1,team_2,winner,`by` from match_info_odi ORDER BY CAST(`by` AS DECIMAL) ASC limit 10"
dh = pd.read_sql(query_4,con = engine) 
print(f"Query 4  : {dh}")


query_5 = "SELECT  COUNT(DISTINCT match_number_type) AS total_matches FROM match_score_t20 "
df_1 = pd.read_sql(query_5,con = engine)
print(f"Query 5 [Total matches played]  : {df_1}")

query_6 = "SELECT team, SUM(total_runs) AS total_runs FROM match_score_t20 GROUP BY team "
df_2 = pd.read_sql(query_6,con = engine)
print(f"Query 6 [Total runs scored by each team]  : {df_2}")

query_7 = "SELECT batter, SUM(batter_runs) AS runs FROM match_score_t20 GROUP BY batter ORDER BY runs DESC LIMIT 10"
df_3 = pd.read_sql(query_7,con = engine)
print(f"Query 7 [Top 10 batters by total run]  : {df_3}")

query_8 = "SELECT bowler, COUNT(*) AS wickets FROM match_score_t20 WHERE wicket != 'not yet' GROUP BY bowler ORDER BY wickets DESC LIMIT 10"
df_4 = pd.read_sql(query_8,con = engine)
print(f"Query 8 [Top 10 bowlers by wickets]  : {df_4}")

query_9 = "SELECT match_number_type, SUM(total_runs)/MAX(overs) AS run_rate FROM match_score_t20 GROUP BY match_number_type"
df_5 = pd.read_sql(query_9,con = engine)
print(f"Query 9 [Run rate per match]  : {df_5}")

query_10 = "SELECT DISTINCT match_number_event, target_runs FROM match_score_t20 WHERE target_runs > 200"
df_6 = pd.read_sql(query_10,con = engine)
print(f"Query 10 [Matches with target over 200]  : {df_6}")

query_11 = "SELECT AVG(total_runs) AS avg_powerplay_runs FROM match_score_t20 WHERE overs <= 6.0 "
df_7 = pd.read_sql(query_11,con = engine)
print(f"Query 11 [Average score in Powerplay (first 6 overs)]  : {df_7}")

query_12 = "SELECT batter, COUNT(*) AS sixes FROM match_score_t20 WHERE batter_runs = 6 GROUP BY batter ORDER BY sixes DESC"
df_8 = pd.read_sql(query_12,con = engine)
print(f"Query 12 [Most sixes (assumed 6-run batter hits)]  : {df_8}")

query_13 = "SELECT batter, COUNT(*) AS fours FROM match_score_odi WHERE batter_runs = 4 GROUP BY batter ORDER BY fours DESC"
df_9 = pd.read_sql(query_13,con = engine)
print(f"Query 13 [Most fours (4-run hits)(odi)]  : {df_9}")

query_14 = """SELECT batter, non_striker, SUM(total_runs) AS partnership_runs
FROM match_score_odi
GROUP BY batter, non_striker
ORDER BY partnership_runs DESC LIMIT 10"""
df_10 = pd.read_sql(query_14,con = engine)
print(f"Query 14 [Top partnerships (by non-striker)]  : {df_10}")

query_15 = """ SELECT bowler, SUM(total_runs)/COUNT(DISTINCT overs) AS economy
FROM match_score_odi
GROUP BY bowler
ORDER BY economy ASC"""
df_11 = pd.read_sql(query_15,con = engine)
print(f"Query 15 [Bowler economy (runs per over)]  : {df_11}")

query_16 = """ SELECT FLOOR(overs) AS over_num, SUM(total_runs) AS runs
FROM match_score_odi
GROUP BY over_num
ORDER BY over_num"""
df_12 = pd.read_sql(query_16,con = engine)
print(f"Query 16 [Runs scored per over across all matches] : {df_12}")

query_17 = """SELECT team, AVG(total_runs) AS avg_score
FROM match_score_odi
WHERE overs < 20.0
GROUP BY team"""
df_13 = pd.read_sql(query_17,con = engine)
print(f"Query 17 [Team-wise average first innings score] : {df_13}")

query_18 = "SELECT MAX(target_runs) AS max_target FROM match_score_t20"
df_14 = pd.read_sql(query_18,con = engine)
print(f"Query 18 [Max target_runs] : {df_14}")

query_19 = """SELECT team, COUNT(*) AS wickets_lost
FROM match_score_t20
WHERE wicket != 'not yet'
GROUP BY team"""
df_15 = pd.read_sql(query_19,con = engine)
print(f"Query 19 [Team-wise wicket count] : {df_15}")


query_20 = """SELECT team, COUNT(*) AS wickets_lost
FROM match_score_t20
WHERE wicket != 'not yet'
GROUP BY team"""
df_16 = pd.read_sql(query_20,con = engine)
print(f"Query 20 [Team-wise wicket count] : {df_16}")