import requests
import csv
from xml.dom.minidom import parseString

url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

#print (doc.toprettyxml())

objTrainPositions_node = doc.getElementsByTagName("objTrainPositions")
for objTrainPositions_node in objTrainPositions_node:
    TrainCode_node = objTrainPositions_node.getElementsByTagName("TrainCode").item(0)
    TrainCode = TrainCode_node.firstChild.nodeValue.strip()
    print(TrainCode)