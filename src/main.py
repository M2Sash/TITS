import dbinteract as dbI
from lib import *

DB = dbI.bDBFile()
DB.createAcademy("man_uni")
DB.createCabinet("man_uni", "cab104")
DB.createUser("Alex", "Alex@M2Inc.Dev", passwordhash=hash("qwerty123"))