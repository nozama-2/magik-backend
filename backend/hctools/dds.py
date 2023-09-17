import pymongo
import os
from uuid import uuid4
from pymongo import MongoClient
from datetime import datetime, timedelta
from bson.timestamp import Timestamp

# Loads environment variables using dotenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

password = os.environ.get("DDS_PASS")
conn_url = f"mongodb://rwuser:{password}@192.168.0.118:8635,192.168.0.240:8635/games?authSource=admin&replicaSet=replica"
print(conn_url)

client = MongoClient(conn_url,connectTimeoutMS=5000)
db = client.games
tangram = db.tangram

dict = {
    "_id": str(uuid4()),
    "userId": 0,
    "solveTime": datetime.now(),
    "solveState": "success",
    "sessionDuration": 34,
    "piecesPlaced": [
        {
            "placedTime": datetime.now() - timedelta(seconds=5),
            "pieceId": 3,
            "pieceStatus": "success",
            "pieceCoodinates": [
                [4,0,3,0],
                [4,2,3,-2],
                [4,-2,3,-2]
            ]
        },
        {
            "placedTime": datetime.now() - timedelta(seconds=2),
            "pieceId": 1,
            "pieceStatus": "success",
            "pieceCoodinates": [
                [4,0,3,0],
                [4,2,3,-2],
                [4,-2,3,-2]
            ]
        },
        {
            "placedTime": datetime.now() - timedelta(seconds=9),
            "pieceId": 1,
            "pieceStatus": "success",
            "pieceCoodinates": [
                [4,0,3,0],
                [4,2,3,-2],
                [4,-2,3,-2]
            ]
        },
        {
            "placedTime": datetime.now() - timedelta(seconds=14),
            "pieceId": 2,
            "pieceStatus": "success",
            "pieceCoodinates": [
                [4,0,3,0],
                [4,2,3,-2],
                [4,-2,3,-2]
            ]
        },
        {
            "placedTime": datetime.now() - timedelta(seconds=18),
            "pieceId": 4,
            "pieceStatus": "success",
            "pieceCoodinates": [
                [4,0,3,0],
                [4,2,3,-2],
                [4,-2,3,-2]
            ]
        },
        {
            "placedTime": datetime.now() - timedelta(seconds=22),
            "pieceId": 3,
            "pieceStatus": "success",
            "pieceCoodinates": [
                [4,0,3,0],
                [4,2,3,-2],
                [4,-2,3,-2]
            ]
        },
        {
            "placedTime": datetime.now() - timedelta(seconds=27),
            "pieceId": 5,
            "pieceStatus": "success",
            "pieceCoodinates": [
                [4,0,3,0],
                [4,2,3,-2],
                [4,-2,3,-2]
            ]
        }
    ]
}


def add_game(data):
    tangram.insert_one(dict)
#print(type(datetime.now()))
#print(type(datetime.now() - timedelta(seconds=3)))
#print(client.server_info())
#print(client.games)
