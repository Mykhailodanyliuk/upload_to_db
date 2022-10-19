import os
import shutil
import pymongo
import json
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client["db"]
col = db['clinical_trials']
RootDir1 = r'G:/AllAPIJSON'
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
    for name in files:
        if name.endswith('.json'):
            print ("Found")
            print(name, root, dirs)
            f = open(f'{root}/{name}')
            data = json.load(f)
            col.insert_one(data)
            print(data)