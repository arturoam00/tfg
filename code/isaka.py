def isaka(dictio, key):
	c = True
	for t in dictio:
		if (t == key):
			print(dictio[t])
			c = False
	if (c):
		print("none")	



myDict = {"temp" : 1, "humidity" : 2134, "wind" : 243, "tor": 98243}

isaka(myDict, "temp")

