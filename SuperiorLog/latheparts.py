lpart59601 = 'LathePartsInfo/596-01.txt'
lpart74522 = 'LathePartsInfo/745-22.txt'
lpart99999 = 'LathePartsInfo/999-99.txt'


latheparts = [lpart59601, lpart74522, lpart99999]
lathepartnumbers = []
lathecycletimes = []
lathesetuptimes = []



for part in latheparts:
	with open(part) as l:
		latheextractpartinfo = l.readlines()
		lathepartnumber = latheextractpartinfo[1]
		lathepartnumbers.append(lathepartnumber.strip())
		lathecycletime = latheextractpartinfo[3]
		lathecycletimes.append(lathecycletime.strip())
		lathesetuptime = latheextractpartinfo[5]
		lathesetuptimes.append(lathesetuptime.strip())
		lathekeydim1 = latheextractpartinfo[7]
		lathekeydim2 = latheextractpartinfo[9]
		lathekeydim3 = latheextractpartinfo[11]
		lathekeydim4 = latheextractpartinfo[13]
		lathekeydim5 = latheextractpartinfo[15]
		l.close()

print('Lathe parts loaded.')


