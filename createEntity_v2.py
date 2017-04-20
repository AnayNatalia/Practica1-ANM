import requests 
import json

url = 'http://130.206.112.29:5050/iot/devices'

headers = {'fiware-Service': 'icai16318',
           'fiware-servicePath':'/environment',
           'Content-Type': 'application/json'}

payload = {"devices":
            [
                {
                 "device_id": "Smartlight2017001",
                 "entity_name": "SML01",
                 "entity_type": "Smartlight",
                 "attributes":
                 [
                 	{
                        "object_id": "loc",
                        "name": "Location",
                        "type": "String"
                    },
                    {
                        "object_id": "adr",
                        "name": "Address",
                        "type": "String"
                    },
                    {
                        "object_id": "cond",
                        "name": "Condition_status",
                        "type": "String"
                    },
                    {
                        "object_id": "idcirc",
                        "name": "ID_circuit",
                        "type": "String"
                    },
                    {   "object_id": "bri",
                        "name": "Brightness",
                        "type": "Integer"
                    },
                    {
                        "object_id": "pres",
                        "name": "Presence",
                        "type": "Boolean"
                    },
                    {
                        "object_id": "sta",
                        "name": "State",
                        "type": "Boolean",
                    },
                 ],
                 "transport": "MQTT"
                },
                {
                 "device_id": "Smartlight2017002",
                 "entity_name": "SML02",
                 "entity_type": "Smartlight",
                 "attributes":
                 [
                    {
                        "object_id": "loc",
                        "name": "Location",
                        "type": "String"
                    },
                    {
                        "object_id": "adr",
                        "name": "Address",
                        "type": "String"
                    },
                    {
                        "object_id": "cond",
                        "name": "Condition_status",
                        "type": "String"
                    },
                    {
                        "object_id": "idcirc",
                        "name": "ID_circuit",
                        "type": "String"
                    },
                    {   "object_id": "bri",
                        "name": "Brightness",
                        "type": "Integer"
                    },
                    {
                        "object_id": "pres",
                        "name": "Presence",
                        "type": "Boolean"
                    },
                    {
                        "object_id": "sta",
                        "name": "State",
                        "type": "Boolean",
                    },
                 ],
                 "transport": "MQTT"
                },
                {
                 "device_id": "Smartlight2017003",
                 "entity_name": "SML03",
                 "entity_type": "Smartlight",
                 "attributes":
                 [
                    {
                        "object_id": "loc",
                        "name": "Location",
                        "type": "String"
                    },
                    {
                        "object_id": "adr",
                        "name": "Address",
                        "type": "String"
                    },
                    {
                        "object_id": "cond",
                        "name": "Condition_status",
                        "type": "String"
                    },
                    {
                        "object_id": "idcirc",
                        "name": "ID_circuit",
                        "type": "String"
                    },
                    {   "object_id": "bri",
                        "name": "Brightness",
                        "type": "Integer"
                    },
                    {
                        "object_id": "pres",
                        "name": "Presence",
                        "type": "Boolean"
                    },
                    {
                        "object_id": "sta",
                        "name": "State",
                        "type": "Boolean",
                    },
                 ],
                 "transport": "MQTT"
                },                  
              ],
            }

r = requests.post(url, headers=headers, data=json.dumps(payload))

print r
print r.content




