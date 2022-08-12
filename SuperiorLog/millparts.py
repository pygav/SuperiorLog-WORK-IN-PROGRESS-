

mpart10999 = 'MillPartsInfo/10-999.txt'
mpart20856 = 'MillPartsInfo/20-856.txt'
mpart30741= 'MillPartsInfo/30-741.txt'
mpart40555= 'MillPartsInfo/40-555.txt'
mpart50505= 'MillPartsInfo/50-505.txt'

millparts = [mpart10999,mpart20856,mpart30741,mpart40555,mpart50505]
millpartnumbers = []
millcycletimes = []
millsetuptimes = []



for part in millparts:
	with open(part) as m:
		millextractpartinfo = m.readlines()
		millpartnumber = millextractpartinfo[1]
		millpartnumbers.append(millpartnumber.strip())
		millcycletime = millextractpartinfo[3]
		millcycletimes.append(millcycletime.strip())
		millsetuptime = millextractpartinfo[5]
		millsetuptimes.append(millsetuptime.strip())
		m.close()



print('Mill parts loaded.')