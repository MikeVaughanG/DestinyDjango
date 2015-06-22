import os
import pickle

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DestHub.settings")
from weapon_data.models import Weapon
with open('manifest.pickle', 'rb') as data:
    all_data = pickle.load(data)
    
items = all_data['DestinyInventoryItemDefinition']
talent_grids = all_data['DestinyTalentGridDefinition']

weapon_types = ['Rocket Launcher', 'Scout Rifle', 'Fusion Rifle', 'Sniper Rifle', 
                'Shotgun', 'Machine Gun', 'Pulse Rifle', 'Auto Rifle', 'Hand Cannon', 
                'Sidearm']

all_weapons = {}        
for item, v in items.items():
    try:
        if v['itemTypeName'] in weapon_types:
            all_weapons[v['itemName']] = v
    except KeyError:
        pass
        

for k,v in all_weapons.items():
    if '###Missing' not in k:
        w = Weapon(weapon_name = v['itemName'], weapon_tier = v['tierTypeName'],
                   weapon_type = v['itemTypeName'], weapon_descrip = v['itemDescription'])
        try:
            talent_grid = talent_grids[v['talentGridHash']]['nodes']
        except KeyError:
            print v
        
        nodes = {}
        for node in talent_grid:
            name = str(node['row'])+str(node['column'])
            nodes[name] = []
            for step in node['steps']:
                try:
                    nodes[name].append((step['nodeStepName'], step['icon']))
                except KeyError:
                    pass
                    
        w.weapon_rolls = str(nodes)
        w.save()
        