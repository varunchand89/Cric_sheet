#Cric_sheet match data analysis 
CREATE TABLE odi_team_summary AS
SELECT 
    team,
    SUM(CASE WHEN team = winner THEN 1 ELSE 0 END) AS wins,
    SUM(CASE WHEN team != winner AND winner NOT IN ('Draw', 'No Result') THEN 1 ELSE 0 END) AS losses,
    COUNT(*) AS total_matches
FROM (
    SELECT team_1 AS team, winner FROM match_info_odi
    UNION ALL
    SELECT team_2 AS team, winner FROM match_info_odi
) AS all_matches
GROUP BY team
ORDER BY wins DESC;

CREATE TABLE 20_team_summary AS
SELECT 
    team,
    SUM(CASE WHEN team = winner THEN 1 ELSE 0 END) AS wins,
    SUM(CASE WHEN team != winner AND winner NOT IN ('Draw', 'No Result') THEN 1 ELSE 0 END) AS losses,
    COUNT(*) AS total_matches
FROM (
    SELECT team_1 AS team, winner FROM match_info_20
    UNION ALL
    SELECT team_2 AS team, winner FROM match_info_20
) AS all_matches
GROUP BY team
ORDER BY wins DESC;


CREATE TABLE test_team_summary AS
SELECT 
    team,
    SUM(CASE WHEN team = winner THEN 1 ELSE 0 END) AS wins,
    SUM(CASE WHEN team != winner AND winner NOT IN ('Draw', 'No Result') THEN 1 ELSE 0 END) AS losses,
    COUNT(*) AS total_matches
FROM (
    SELECT team_1 AS team, winner FROM match_info_test
    UNION ALL
    SELECT team_2 AS team, winner FROM match_info_test
) AS all_matches
GROUP BY team
ORDER BY wins DESC;


---------------------------------------------
#win percentage
create table percent as
SELECT 
    team,
    COUNT(*) AS matches_played,
    SUM(CASE WHEN team = winner THEN 1 ELSE 0 END) AS wins,
    ROUND(100.0 * SUM(CASE WHEN team = winner THEN 1 ELSE 0 END) / COUNT(*), 2) AS win_percentage
FROM (
    SELECT team_1 AS team, winner FROM match_info_odi
    UNION ALL
    SELECT team_2 AS team, winner FROM match_info_odi
) AS combined
GROUP BY team
ORDER BY win_percentage DESC;

#average runs per match
create table avgruns as
SELECT 
    batter,
    team,
    SUM(batter_runs) AS total_runs,
    COUNT(DISTINCT match_number_type) AS matches,
    ROUND(SUM(batter_runs) / NULLIF(COUNT(DISTINCT match_number_type), 0), 0) AS avg_runs_per_match
FROM match_score_odi
GROUP BY batter, team
ORDER BY total_runs DESC;

#batting average
create table batting_average AS
SELECT 
    batter,
    SUM(total_runs) AS total_run,
    COUNT(*) AS innings_played,
    ROUND(SUM(total_runs) * 1 / COUNT(*), 2) AS batting_average
FROM match_score_t20
GROUP BY batter
ORDER BY batting_average DESC;

#highest score
create table highest_score AS
SELECT 
    batter AS player_name,
    MAX(total_match_runs) AS highest_score
FROM (
    SELECT 
        match_number_event,
        batter,
        SUM(batter_runs) AS total_match_runs
    FROM match_score_t20
    GROUP BY match_number_event, batter
) AS match_scores
GROUP BY batter
ORDER BY highest_score DESC;

#wicket taken and runs 
create table wicket AS
SELECT 
    bowler,
    SUM(COALESCE(total_runs, 0)) AS runs_conceded,
    COUNT(CASE WHEN LOWER(TRIM(wicket)) != 'not yet' THEN 1 END) AS total_wickets
FROM match_score_t20
GROUP BY bowler;

#bowling average
create table bow_av as 
SELECT 
    bowler,
    IFNULL(
        ROUND(
            SUM(COALESCE(total_runs, 0)) * 1.0 / NULLIF(COUNT(CASE WHEN LOWER(TRIM(wicket)) != 'not yet' THEN 1 END), 0),
            2
        ),
        0.00
    ) AS bowling_average
FROM match_score_t20
GROUP BY bowler
ORDER BY bowling_average ASC;


#head to head 
create table HTH AS
SELECT 
    LEAST(team_1, team_2) AS team_a,
    GREATEST(team_1, team_2) AS team_b,
    COUNT(*) AS total_matches,
    SUM(CASE WHEN winner = team_1 THEN 1 WHEN winner = team_2 THEN 0 ELSE 0 END) AS team_a_wins,
    SUM(CASE WHEN winner = team_2 THEN 1 WHEN winner = team_1 THEN 0 ELSE 0 END) AS team_b_wins,
    SUM(CASE WHEN winner NOT IN (team_1, team_2) THEN 1 ELSE 0 END) AS no_result
FROM match_info_20
GROUP BY 
    LEAST(team_1, team_2),
    GREATEST(team_1, team_2)
ORDER BY total_matches DESC;

#match outcomes by teams 
create table outcomes AS
SELECT 
    team,
    SUM(CASE WHEN team = winner THEN 1 ELSE 0 END) AS wins,
    SUM(CASE WHEN team != winner AND winner NOT IN ('Draw', 'No Result') THEN 1 ELSE 0 END) AS losses,
    COUNT(*) AS total_matches
FROM (
    -- Only include team batting in 1st innings
    SELECT match_number_type, team_1 AS team, winner
    FROM match_info_20
    WHERE match_number_type = 1
    
    UNION ALL
    
    -- Include team bowling in 1st innings
    SELECT match_number_type, team_2 AS team, winner
    FROM match_info_20
    WHERE match_number_type = 1
) AS one_innings
GROUP BY team
ORDER BY wins DESC;


#strike rate
create table strike794 AS
SELECT 
    match_number_type,
    batter,
    SUM(batter_runs) AS total_runs,
    COUNT(*) AS balls_faced,
    ROUND(SUM(batter_runs) * 100.0 / NULLIF(COUNT(*), 0), 2) AS strike_rate
FROM match_score_odi
WHERE match_number_type = 794  -- change to your match
GROUP BY match_number_type, batter
ORDER BY strike_rate DESC;

#bowling economy
create table economy794 AS
SELECT 
    match_number_type,
    bowler,
    SUM(total_runs) AS runs_conceded,
    COUNT(*) AS balls_bowled,
    ROUND(SUM(total_runs) * 1.0 / (COUNT(*) / 6), 2) AS economy_rate
FROM match_score_odi
WHERE match_number_type = 794  -- replace with your match
GROUP BY match_number_type, bowler
ORDER BY economy_rate ASC;

#compare two playwers

