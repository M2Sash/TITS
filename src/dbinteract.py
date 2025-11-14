# Script will be modified to use SQLITE Databases, this approach is currently used for dev simplicity
# We are a camelcase house hold, f u berry

import os
import json
class bDBFile: #betaDBFile
    def __init__(self, file="assets/database.json"):
        DBFExist = os.path.exists(file)
        if DBFExist:
            with open(file, "r", encoding="utf-8") as dbf:
                self.DBF = json.loads(dbf.read())
        else:
            self.createEmptyDB(file)

    def createEmptyDB(self, filename="assets/database.json"):
        emptyDBData = {"acad": {}, "users": {}}
        with open(filename, "w", encoding="utf-8") as f:
            f.write(
                json.dumps(emptyDBData, indent=1)
            )

        self.DBF = emptyDBData
        self.save()

    def createAcademy(self, id):
        if id not in self.DBF["acad"]:
            self.DBF["acad"][id] = {"cabinets": {}, "users": {}}
            self.save()
        else:
            print(f"Academy with same ID exists! ({id})")

    def createCabinet(self, acadID, cabID):
        if acadID in self.DBF["acad"]:
            if cabID not in self.DBF["acad"][acadID]["cabinets"]:
                self.DBF["acad"][acadID]["cabinets"][cabID] = {"components": [{"id":"water", "amount": -1, "image":"imageurlorsmth", "logs": ["+inf:admin"]}]}
                self.save()

            else: print(f"Cabinet already exists ({cabID})")
        else: print(f"Academy doesn`t exist ({acadID})")
        
    
    def createUser(self, username, email, passwordhash):
        if username not in self.DBF["users"]:
            self.DBF["users"][username] = {"pass": passwordhash, "email": email, "access": []}
        else:
            print(f"Username already in use ({username})")

        self.save()
    def save(self, filename="assets/database.json"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(
                json.dumps(self.DBF, indent=1)
            )