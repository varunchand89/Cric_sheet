import mysql.connector
import pandas as pd
import streamlit as st
import urllib.parse
from  sqlalchemy import create_engine

mydb =mysql.connector.connect(host="localhost",user="root",password="Varunchand@8",database="zomato")
password = urllib.parse.quote("Varunchand@8")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/zomato")
mycursor = mydb.cursor()


