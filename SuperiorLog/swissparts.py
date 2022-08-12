

spart1001968 = 'SwissPartsInfo/1001-968.txt'
spart56566942 = 'SwissPartsInfo/5656-6942.txt'
spart69830001= 'SwissPartsInfo/6983-0001.txt'



swissparts = [spart1001968, spart56566942, spart69830001]
swisspartnumbers = []
swisscycletimes = []
swiss_setuptimes = []



for part in swissparts:
	with open(part) as s:
		swissextractpartinfo = s.readlines()
		swisspartnumber = swissextractpartinfo[1]
		swisspartnumbers.append(swisspartnumber.strip())
		swisscycletime = swissextractpartinfo[3]
		swisscycletimes.append(swisscycletime.strip())
		swiss_setuptime = swissextractpartinfo[5]
		swiss_setuptimes.append(swiss_setuptime.strip())
		s.close()



print('Swiss parts loaded.')







