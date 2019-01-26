#!/usr/bin/python

import dataWriter as dw
import requests
import json
import datetime

result = []

tab = [
	{
		"s": {
			"lat": 48.8910037,
			"lng": 2.2389773,
			"name": "La Defense (92)"
		},
		"e": {
			"lat": 48.8841945,
			"lng": 2.3139067,
			"name": "Parc Monceau (75017)"
		}
	},{
		"s": {
			"lat": 48.87299429999999,
			"lng": 2.3328503,
			"name": "Boulevard Haussmann (75009)"
		},
		"e": {
            "lat": 48.8688165,
            "lng": 2.2833208,
			"name": "Avenue Victor Hugo (75016)"
        }
	},{
		"s": {
            "lat": 48.8697452,
            "lng": 2.3079456,
			"name": "Champs Elysees"
        },
		"e": {
            "lat": 48.83763099999999,
            "lng": 2.481699,
			"name": "Nogent Sur Marne"
        }
	},{
		"s": {
            "lat": 48.8408222,
            "lng": 2.3694391,
			"name": "Quai Austerlitz (75013)"
        },
		"e": {
            "lat": 48.7515616,
            "lng": 2.2966475,
			"name": "Anthony (92160)"
        }
	},{
		"s": {
            "lat": 48.8854993,
            "lng": 2.2653713,
			"name": "Neuilly sur Seine (92200)"
        },
		"e": {
			"lat": 49.0096906,
            "lng": 2.5479245,
			"name": "Aeroport Roissy Charles De Gaulle"
        }
	},{
		"s": {
            "lat": 48.8537981,
            "lng": 2.3333285,
			"name": "Saint Germain des pres (75006)"
        },
		"e": {
            "lat": 48.8726896,
            "lng": 2.2846359,
			"name": "Avenue Foch (75016)"
        }
	},{
		"s": {
            "lat": 48.8854993,
            "lng": 2.2653713,
			"name": "Neuilly sur Seine (92200)"
        },
		"e": {
            "lat": 48.8251079,
            "lng": 2.3303259,
			"name": "12 Rue Lacaze (75013)"
        }
	},{
		"s": {
            "lat": 48.8697452,
            "lng": 2.3079456,
			"name": "Champs Elysees (75008)"
        },
		"e": {
            "lat": 48.7262433,
            "lng": 2.3652472,
			"name": "aeroport Orly"
        }
	},{
		"s": {
            "lat": 48.863812,
            "lng": 2.448451,
			"name": "Montreuil"
        },
		"e": {
            "lat": 48.8821898,
            "lng": 2.3372805,
			"name": "Pigalle"
        }
	},{
		"s": {
            "lat": 48.84430380000001,
            "lng": 2.3743773,
			"name": "Gare de Lyon"
        },
		"e": {
            "lat": 48.8288252,
            "lng": 2.32445,
			"name": "Alesia"
        }
	},{
		"s": {
            "lat": 48.8372728,
            "lng": 2.3353873,
			"name": "Montparnasse"
        },
		"e": {
            "lat": 48.88474799999999,
            "lng": 2.23964,
			"name": "puteaux"
        }
	},{
		"s": {
            "lat": 48.8638489,
            "lng": 2.2855198,
			"name": "Trocadero"
        },
		"e": {
            "lat": 48.8741511,
            "lng": 2.2923323,
			"name": "Place de l etoile"
        }
	},{
		"s": {
        	"lat": 48.83763099999999,
            "lng": 2.481699,
			"name": "Nogent sur Marne"
        },
		"e": {
            "lat": 48.884831,
            "lng": 2.26851,
			"name": "Neuilly sur seine"
        }
	}
]

now = datetime.datetime.now()

lecab_url = "https://api.lecab.fr/release/jobs/estimate"

uber_url = "https://api.uber.com/v1.2/estimates/price"

lecab_header = {
	"Authorization": "X-Api-Key 89696335d20acc59d7060642ba312cc6",
	"Content-Type": "application/json"
}

uber_header = {
    "Authorization": "Token XaJPd4JM3OEv_KzCp1ReJ3UrnTLR-557eBZdSaCQ",
}

for adr in tab:
	final = {
		"Depart": adr['s']['name'],
		"Destination": adr['e']['name']
	}
	lecab_jsn = {
		"pickup": {
			"latitude": adr['s']['lat'],
			"longitude": adr['s']['lng']
		},
		"drop": {
			"latitude": adr['e']['lat'],
			"longitude": adr['e']['lng']
		},
		"service": "P508",
		"date": now.strftime("%Y-%m-%dT%H:%M:%S+00:00")
	}
	res = requests.post(url = lecab_url, headers = lecab_header, json = lecab_jsn)
	final['Lecab'] = json.loads(res.content)["price_net"]
	uber_params = {
        "start_latitude": adr['s']['lat'],
        "start_longitude": adr['s']['lng'],
        "end_latitude": adr['e']['lat'],
        "end_longitude": adr['e']['lng']
        }
	res = requests.get(url = uber_url, headers = uber_header, params = uber_params)
	data = json.loads(res.content)
	arr = data["prices"]
	for cur in arr:
	    final[cur['display_name']] = cur['estimate']
        final['Lecab'] = final.get('Lecab', 'Pas de traget')
	final['Green'] = final.get('Green', 'Pas de traget')
	final['UberX'] = final.get('UberX', 'Pas de traget')
	final['Berline'] = final.get('Berline', 'Pas de traget')
	final['Van'] = final.get('Van', 'Pas de traget')
	final['ACCESS'] = final.get('ACCESS', 'Pas de traget')
	result.append(final)

dw.print_result(result)
