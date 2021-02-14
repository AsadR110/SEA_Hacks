# Change the parameters below for your HomeBridge
hostname = '192.168.1.75'
port = '51066'
auth = '668-24-916'

# End parameters

# Start of definitions
url = 'http://' + hostname + ':' + str(port) + '/'
headers = {'Content-Type': 'Application/json', 'authorization': auth}

accessories={}
selectedAccessories=[]
selectedAccessoryNames={}
argumentLength = len(sys.argv)

def getAccessories():
	global getAcc
	try:
		getAcc = requests.get(url + 'accessories', headers=headers)
		if getAcc.status_code == 200:
			getAcc = getAcc.json()
		# load sample data for debugging
		# with open('acc.json') as f:
		#   data = json.load(f)
		for item in getAcc['accessories']:
			if getAcc['accessories'].index(item) != 0:
				interfaces = []
				for i in item['services'][1]['characteristics'][1:]:
					if i['format'] not in ['bool','string','tlv8','uint8','float']:
						interfaces.append({'iid':i['iid'],'description': i['description'],'maxValue': i['maxValue'],'minValue': i['minValue'],'minStep': i['minStep'], 'value': i['value']})
					else:
						interfaces.append({'iid':i['iid'],'description': i['description'],'value': i['value']})
				accessories.update({str(item['services'][0]['characteristics'][3]['value']).replace(' ','_') : {'aid':item['aid'],'iid':10,'type':item['services'][0]['characteristics'][2]['value'],'value':interfaces}})

	except:
		if sys.argv[1] == '-d' or sys.argv[1] == '--debug':
			logging.error(Exception, exc_info=True)
		print('Exception logged: ' + exceptionFile)
	return accessories

def selectAccessory(inputName):
	try:
		for key in accessories:
			if inputName in key.lower():
				selectedAccessoryNames.update({accessories[key]['aid']:{'name':key}})
				selectedAccessories.append({'aid':accessories[key]['aid'], 'value':accessories[key]['value']})
	except:
		if sys.argv[1] == '-d' or sys.argv[1] == '--debug':
			logging.error(Exception, exc_info=True)
			print('Exception logged: ' + exceptionFile)

def selectGroup(inputName):
	try:
		for key in accessories:
			if accessories[key]['type'].lower().startswith(inputName[:len(inputName)-2]):
				selectedAccessoryNames.update({accessories[key]['aid']:{'name':key}})
				selectedAccessories.append({'aid':accessories[key]['aid'], 'iid':accessories[key]['iid'], 'value':accessories[key]['value']})
	except:
		if sys.argv[1] == '-d' or sys.argv[1] == '--debug':
			logging.error(Exception, exc_info=True)
			print('Exception logged: ' + exceptionFile)

def printAccessories(param=''):
	try:
		if param == 'json':
			print(json.dumps(accessories))
			return
		for key in accessories:
			if param == 'aid':
				print(str(accessories[key]['aid']) + ' ', end='')
			print(key, end=' ')
			if param == 'type' or param == 'all':
				print(str(accessories[key]['type']) + ' ', end='')
			if param in ['value','iid','all']:
				# print(str(accessories[key]['value']), end='')
				for i in accessories[key]['value']:
					print('\n   ', end='')
					if param == 'iid' or param == 'all':
						print(str(i['iid']) + ' ' + str(i['value']), end=' ')
					if param == 'value' or param == 'all':
						print(str(i['description']) + ' ' + str(i['value']), end='')
			print('')
	except:
		if sys.argv[1] == '-d' or sys.argv[1] == '--debug':
			# debugHandler(json.dumps(sys.exc_info()))
			logging.error(Exception, exc_info=True)
			print('Exception logged: ' + exceptionFile)

def toggleSwitch()

for item in selectedAccessories:
    if sys.argv[argumentLength-2] not in ['-b', '-h', '-sat', '-t', '--brightness', '--hue', '--saturation', '--temperature'] and sys.argv[argumentLength-1] not in ['-b', '-h', '-sat', '-t', '--brightness', '--hue', '--saturation', '--temperature']:
        if sys.argv[argumentLength-1].isdigit():
            item['value'][0]['value'] = sys.argv[argumentLength-1]
        elif item['value'][0]['value'] == 0 or item['value'][0]['value'] == False:
            item['value'][0]['value'] = '1'
        else:
            item['value'][0]['value'] = '0'
    else:

        if sys.argv[argumentLength-2] in ['-b', '--brightness'] or sys.argv[argumentLength-1] in ['-b', '--brightness']:
            valueIndex = next((item['value'].index(v) for v in item['value'] if v['description'] == 'Brightness'), 0)
        elif sys.argv[argumentLength-2] in ['-h', '--hue'] or sys.argv[argumentLength-1] in ['-h', '--hue']:
            valueIndex = next((item['value'].index(v) for v in item['value'] if v['description'] == 'Hue'), 0)
        elif sys.argv[argumentLength-2] in ['-sat', '--saturation'] or sys.argv[argumentLength-1] in ['-sat', '--saturation']:
            valueIndex = next((item['value'].index(v) for v in item['value'] if v['description'] == 'Saturation'), 0)
        elif sys.argv[argumentLength-2] in ['-t', '--temperature'] or sys.argv[argumentLength-1] in ['-t', '--temperature']:
            valueIndex = next((item['value'].index(v) for v in item['value'] if v['description'] == 'Color Temperature'), 0)

        if sys.argv[argumentLength-1].isdigit():
            if (int(sys.argv[argumentLength-1]) <= item['value'][valueIndex]['maxValue']) and (int(sys.argv[argumentLength-1]) >= item['value'][valueIndex]['minValue']) and (int(sys.argv[argumentLength-1])%item['value'][valueIndex]['minStep'] == 0):
                item['value'][valueIndex]['value'] = int(sys.argv[argumentLength-1])
            else:
                print('Error:\n   Max Value: ' + str(item['value'][valueIndex]['maxValue']) + '\n   Min Value: ' + str(item['value'][valueIndex]['minValue']) +  '\n   Min Step: ' + str(item['value'][valueIndex]['minStep']))
        elif item['value'][valueIndex]['value'] >= ((item['value'][valueIndex]['maxValue']-item['value'][valueIndex]['minValue'])/2) - (((item['value'][valueIndex]['maxValue']-item['value'][valueIndex]['minValue'])/2)%item['value'][valueIndex]['minStep']):
            item['value'][valueIndex]['value'] = item['value'][valueIndex]['maxValue']
        else:
            item['value'][valueIndex]['value'] = item['value'][valueIndex]['minValue']

    selectedAccessoryNames[item['aid']].update({'iid': item['value'][valueIndex]['iid'], 'value': item['value'][valueIndex]['value']})
    setData.append({'aid': item['aid'],'iid': item['value'][valueIndex]['iid'], 'value': item['value'][valueIndex]['value']})
    setReq = requests.put(url + 'characteristics', headers=headers, data='{"characteristics":' + str(setData).replace('\'','\"') + '}')