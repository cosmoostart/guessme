from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('5247968465:AAEhAIzt_ahDsSqhq1o5f4UQEMhjRDndJpw')
MONGO_URI = getenv('mongodb://laziz:UZWwSX7MIQmmPOnO@cluster0-shard-00-00.4tuag.mongodb.net:27017,cluster0-shard-00-01.4tuag.mongodb.net:27017,cluster0-shard-00-02.4tuag.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-bkrqrd-shard-0&authSource=admin&retryWrites=true&w=majority')
SUDO_USERS = list(map(int, getenv('674193259').split()))
