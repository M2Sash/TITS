# Script will be modified to use SQLITE Databases, this approach is currently used for dev simplicity


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
        emptyDBData = {"acad": [], "class": [], "users": [], "components": []}
        with open(filename, "w", encoding="utf-8") as f:
            f.write(
                json.dumps(emptyDBData, indent=1)
            )

        self.DBF = emptyDBData



