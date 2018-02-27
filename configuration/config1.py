import configparser
setting = {'GAME':{'count_gamers':1, 'special': 'off'},'canvasMap':{'scale':0.2, }, 'canvasTickets':{'height':80, 'width': 40, 'count_tickets': 8} }
def read_standart_setting():
	config = configparser.ConfigParser()
	config.read_dict(setting)
	
	config.read('setting.ini')
	print(config.sections())
	
def write_setting(new_settings):#dict --> ini
	config = configparser.ConfigParser()
	for key in new_settings.keys():
		config[key] = new_settings[key]
	with open('setting1.ini', 'w') as configfile:
		config.write(configfile)