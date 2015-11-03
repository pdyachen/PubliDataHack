import csv

def make_block(address):
	address_frmd = address.split(' ')[0]
	if len(address_frmd) == 4:
		address = address_frmd[:-3] + 'XXX' + address[4:]
	elif len(address_frmd) == 5:
		address = address_frmd[:-4] + 'XXXX' + address[5:]
	elif len(address_frmd) == 3:
		address = address_frmd[:-2] + 'XX' + address[3:]
		pass	
	return address
	pass

ph_dict = {} 
f = open(r'C:\Users\pdyachen\Google Диск\Learn\Python\DataHack\LearningMaterials\potholes.csv', 'r')
csv_dict = csv.DictReader(f)
for row in csv_dict:
	address = row['STREET ADDRESS']
	block_addr = make_block(address)
	if block_addr in ph_dict:
		ph_dict[block_addr] += 1
	else:
		ph_dict[block_addr] =1
		pass
print('Number of open potholes by address')
for addr in sorted(ph_dict):
    print('%8s %d' % (addr, ph_dict[addr]))
