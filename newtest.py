from flask import Flask, request, jsonify, make_response
import json
from datetime import datetime, timezone

app = Flask(__name__)

game_client_config_data = {
    "pollingConfiguration": [
        {"id32": 2298181301, "interval": 900}, {"id32": 1090315739, "interval": 90},
        {"id32": 1370749971, "interval": 300}, {"id32": 2401412089, "interval": 300},
        {"id32": 2885838245, "interval": 60}, {"id32": 1663330584, "interval": 90},
        {"id32": 4239899827, "interval": 60}, {"id32": 1101022388, "interval": 60},
        {"id32": 2321903753, "interval": 300}, {"id32": 3012448242, "interval": 600},
        {"id32": 3443535003, "interval": 9000}, {"id32": 3181113487, "interval": 9000},
        {"id32": 3069176075, "interval": 9000}, {"id32": 2701907425, "interval": 300},
        {"id32": 1896257217, "interval": 600}, {"id32": 3813637705, "interval": 9000},
        {"id32": 924828572, "interval": 300}, {"id32": 952049051, "interval": 20},
        {"id32": 1869673247, "interval": 9000}, {"id32": 3753697600, "interval": 10},
        {"id32": 2869249345, "interval": 300}, {"id32": 907021859, "interval": 90},
        {"id32": 1950849984, "interval": 45}, {"id32": 1453632692, "interval": 10},
        {"id32": 1977859078, "interval": 360}, {"id32": 2187912720, "interval": 300},
        {"id32": 895335920, "interval": 1800}, {"id32": 2442802038, "interval": 0},
        {"id32": 2668903150, "interval": 125}, {"id32": 2406296651, "interval": 4},
        {"id32": 3891819455, "interval": 6}, {"id32": 3486820593, "interval": 0},
        {"id32": 1250723970, "interval": 1}, {"id32": 2771693880, "interval": 4},
        {"id32": 2244166905, "interval": 256}, {"id32": 1272239318, "interval": 30},
        {"id32": 1383229038, "interval": 60}, {"id32": 1548226027, "interval": 900}
    ],
    "featureConfiguration": [
        {"id32": 3836664312, "enabled": True, "data": "", "probability": 100},
        {"id32": 1191893463, "enabled": False, "data": "", "probability": 0},
        {"id32": 1731970340, "enabled": True, "data": "", "probability": 100},
        {"id32": 147543665, "enabled": True, "data": "", "probability": 100},
        {"id32": 3050214232, "enabled": True, "data": "", "probability": 100},
        {"id32": 2349288591, "enabled": True, "data": "", "probability": 100},
        {"id32": 1037736245, "enabled": True, "data": "", "probability": 100},
        {"id32": 2938211500, "enabled": True, "data": "", "probability": 100},
        {"id32": 3977691125, "enabled": False, "data": "true", "probability": 100},
        {"id32": 2056779757, "enabled": True, "data": "", "probability": 100}
    ],
    "onlineOverrideConfiguration": [
        {"id32": 3836664312, "mixId": 3836664312, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 1731970340, "mixId": 1731970340, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 2122501867, "mixId": 1730283156, "parentMixId": 1731970340, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 1181373120, "mixId": 1470246927, "parentMixId": 1731970340, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 426721852, "mixId": 163828688, "parentMixId": 1731970340, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 271322048, "mixId": 3250093964, "parentMixId": 1731970340, "enabled": True, "data": "5", "dataType": 5, "probability": 100},
        {"id32": 1684721270, "mixId": 66753034, "parentMixId": 1731970340, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 2483371866, "mixId": 774580170, "parentMixId": 1731970340, "enabled": True, "data": "8", "dataType": 5, "probability": 100},
        {"id32": 609105814, "mixId": 2800439123, "parentMixId": 1731970340, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 365754012, "mixId": 3931218534, "parentMixId": 1731970340, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 1576391531, "mixId": 375722071, "parentMixId": 1731970340, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 701374015, "mixId": 3169599608, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 2422325091, "mixId": 4240916675, "parentMixId": 3169599608, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 1634896105, "mixId": 1349423522, "parentMixId": 3169599608, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 3435642769, "mixId": 2582729456, "parentMixId": 3169599608, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 3494162224, "mixId": 2817067926, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 262888231, "mixId": 2362886741, "parentMixId": 2817067926, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 2422325091, "mixId": 658815317, "parentMixId": 2817067926, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 1634896105, "mixId": 2347591732, "parentMixId": 2817067926, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 3435642769, "mixId": 1114811238, "parentMixId": 2817067926, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 262888231, "mixId": 1506492344, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 3494162224, "mixId": 1121137709, "parentMixId": 1506492344, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 2422325091, "mixId": 4065938616, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 701374015, "mixId": 2874273475, "parentMixId": 4065938616, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 3494162224, "mixId": 2958337325, "parentMixId": 4065938616, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 3435642769, "mixId": 2161307696, "parentMixId": 4065938616, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 1634896105, "mixId": 1592827353, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 701374015, "mixId": 3062600086, "parentMixId": 1592827353, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 3494162224, "mixId": 2911820408, "parentMixId": 1592827353, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 3435642769, "mixId": 2540658315, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 701374015, "mixId": 3977082940, "parentMixId": 2540658315, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 3494162224, "mixId": 4127732690, "parentMixId": 2540658315, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 2422325091, "mixId": 2746774780, "parentMixId": 2540658315, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 147543665, "mixId": 147543665, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 3550970463, "mixId": 4049186208, "parentMixId": 147543665, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 2117564271, "mixId": 824842026, "parentMixId": 147543665, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 216534926, "mixId": 182133893, "parentMixId": 147543665, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 3050214232, "mixId": 3050214232, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 900631814, "mixId": 2283105102, "parentMixId": 3050214232, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 2349288591, "mixId": 2349288591, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 1797233012, "mixId": 1270538380, "parentMixId": 2349288591, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 3726540269, "mixId": 1476117903, "parentMixId": 2349288591, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 1037736245, "mixId": 1037736245, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 2825683808, "mixId": 425449573, "parentMixId": 1037736245, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 2178119527, "mixId": 705871493, "parentMixId": 1037736245, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 2325312666, "mixId": 2662298477, "parentMixId": 1037736245, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 2764011581, "mixId": 4088618188, "parentMixId": 1037736245, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 2938211500, "mixId": 2938211500, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 434365072, "mixId": 240163142, "parentMixId": 2938211500, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 4174527442, "mixId": 2621129951, "parentMixId": 240163142, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 788007814, "mixId": 617872317, "parentMixId": 2938211500, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 4174527442, "mixId": 997795168, "parentMixId": 617872317, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 4129662363, "mixId": 4201226499, "parentMixId": 2938211500, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 4174527442, "mixId": 1338891998, "parentMixId": 4201226499, "enabled": True, "data": "false", "dataType": 7, "probability": 100},
        {"id32": 3809493971, "mixId": 2550465041, "parentMixId": 2938211500, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 4174527442, "mixId": 3960996740, "parentMixId": 2550465041, "enabled": True, "data": "true", "dataType": 7, "probability": 100},
        {"id32": 4205559465, "mixId": 48726272, "parentMixId": 2938211500, "enabled": True, "data": "10", "dataType": 6, "probability": 100},
        {"id32": 2056779757, "mixId": 2056779757, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 3031275039, "mixId": 2453758708, "parentMixId": 2056779757, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 3124066580, "mixId": 1787495693, "parentMixId": 2453758708, "enabled": True, "data": "", "dataType": 0, "probability": 100},
        {"id32": 1893896155, "mixId": 3416152325, "parentMixId": 1787495693, "enabled": True, "data": "100", "dataType": 6, "probability": 100},
        {"id32": 897386910, "mixId": 2123114616, "parentMixId": 1787495693, "enabled": True, "data": "10", "dataType": 6, "probability": 100}
    ],
    "matchMakingConfiguration": {
        "ping": [{"weight": 1, "value": 0}, {"weight": 1, "value": 1}],
        "inLoadout": [{"weight": 1, "value": 0}, {"weight": 1, "value": 1}],
        "preferenceGroupMatch": [{"weight": 1, "value": 0}, {"weight": 1, "value": 1}],
        "gameProgress": [{"weight": 0.1, "value": 100}, {"weight": 1, "value": 50}, {"weight": 1, "value": 0}],
        "partySize": [{"weight": 0.1, "value": 4}, {"weight": 0.1, "value": 2}, {"weight": 1, "value": 1}],
        "hostability": [{"weight": 0.5, "value": 0}, {"weight": 1, "value": 1}],
        "isFriend": [{"weight": 1, "value": 1}, {"weight": 1, "value": 0}],
        "isClanMember": [{"weight": 1, "value": 0}, {"weight": 1, "value": 1}],
        "sosBeacons": [{"weight": 0.5, "value": 0}, {"weight": 1, "value": 1}],
        "missionSelected": [{"weight": 0.75, "value": 0}, {"weight": 1, "value": 1}],
        "operationProgression": [{"weight": 0.5, "value": 100}, {"weight": 1, "value": 0}],
        "difficultyGap": [{"weight": 0.1, "value": 3}, {"weight": 0.75, "value": 2}, {"weight": 1, "value": 1}, {"weight": 1, "value": 0}]
    },
    "matchMakingProperties": [
        {"id32": 2315033710, "values": [0, 1], "weights": [1, 1]},
        {"id32": 1038221924, "values": [0, 1], "weights": [0.5, 1]},
        {"id32": 1778784146, "values": [100, 50, 0], "weights": [0.1, 1, 1]},
        {"id32": 2042807422, "values": [4, 2, 1], "weights": [0.1, 0.1, 1]},
        {"id32": 2887792429, "values": [0, 1], "weights": [0.5, 2]},
        {"id32": 1310771148, "values": [0, 1], "weights": [0.75, 1]},
        {"id32": 1272241989, "values": [100, 0], "weights": [0.5, 1]},
        {"id32": 3698074356, "values": [3, 2, 1, 0], "weights": [0.1, 0.75, 1, 1]},
        {"id32": 2538489315, "values": [0, 1], "weights": [1, 1]},
        {"id32": 2711371980, "values": [0, 1], "weights": [1, 1]},
        {"id32": 184805542, "values": [0, 1], "weights": [1, 1]}
    ]
}

war_info_801_data = {
  "warId": 801,
  "startDate": 1706040313,
  "endDate": 1833653095,
  "layoutVersion": 44,
  "minimumClientVersion": "0.3.0",
  "planetInfos": [
    {
      "index": 0,
      "settingsHash": 897386910,
      "position": {
        "x": 0,
        "y": 0
      },
      "waypoints": [],
      "sector": 0,
      "maxHealth": 1000000,
      "disabled": False,
      "initialOwner": 1
    },
    {
      "index": 1,
      "settingsHash": 3621417917,
      "position": {
        "x": 0.05373042,
        "y": 0.10565466
      },
      "waypoints": [],
      "sector": 1,
      "maxHealth": 1000000,
      "disabled": False,
      "initialOwner": 1
    },
    {
      "index": 2,
      "settingsHash": 2543303604,
      "position": {
        "x": 0.04664221,
        "y": 0.16758725
      },
      "waypoints": [],
      "sector": 1,
      "maxHealth": 1000000,
      "disabled": False,
      "initialOwner": 1
    },
    {
      "index": 3,
      "settingsHash": 2768073863,
      "position": {
        "x": 0.12536779,
        "y": 0.11821219
      },
      "waypoints": [],
      "sector": 1,
      "maxHealth": 1000000,
      "disabled": False,
      "initialOwner": 1
    },
    {
      "index": 4,
      "settingsHash": 158585041,
      "position": {
        "x": 0.10280278,
        "y": 0.05765711
      },
      "waypoints": [],
      "sector": 1,
      "maxHealth": 1000000,
      "disabled": False,
      "initialOwner": 1
    },
    {
      "index": 5,
      "settingsHash": 1008084099,
      "position": {
        "x": 0.15988354,
        "y": 0.043583166
      },
      "waypoints": [],
      "sector": 1,
      "maxHealth": 1000000,
      "disabled": False,
      "initialOwner": 1
    }
  ]
}

galactic_war_effects_data = [
  {"id":1,"gameplayEffectId32":0,"effectType":43,"flags":0,"nameHash":1016609603,"descriptionFluffHash":0,"descriptionGamePlayLongHash":3703951420,"descriptionGamePlayShortHash":473399848,"valueTypes":[1,0],"values":[-1,0]},
  {"id":5,"gameplayEffectId32":0,"effectType":1,"flags":0,"nameHash":3228578710,"descriptionFluffHash":0,"descriptionGamePlayLongHash":3577056812,"descriptionGamePlayShortHash":3338837552,"valueTypes":[2,0],"values":[-10,0]},
  {"id":8,"gameplayEffectId32":0,"effectType":44,"flags":0,"nameHash":1950950127,"descriptionFluffHash":0,"descriptionGamePlayLongHash":1634139783,"descriptionGamePlayShortHash":1534518605,"valueTypes":[2,0],"values":[200,0]},
  {"id":12,"gameplayEffectId32":0,"effectType":45,"flags":0,"nameHash":824899430,"descriptionFluffHash":0,"descriptionGamePlayLongHash":3900785263,"descriptionGamePlayShortHash":1948172020,"valueTypes":[7,0],"values":[3639986401,0]},
  {"id":13,"gameplayEffectId32":0,"effectType":46,"flags":0,"nameHash":668075036,"descriptionFluffHash":0,"descriptionGamePlayLongHash":1131410354,"descriptionGamePlayShortHash":1788167922,"valueTypes":[1,0],"values":[3600,0]},
  {"id":55,"gameplayEffectId32":0,"effectType":25,"flags":0,"nameHash":76488365,"descriptionFluffHash":0,"descriptionGamePlayLongHash":1828599885,"descriptionGamePlayShortHash":1755351526,"valueTypes":[2,0],"values":[100,0]}
]

news_ticker_data = {"messages":[{"id32":2399790664,"context":1,"group":0},{"id32":2061243786,"context":1,"group":0},{"id32":3667104994,"context":1,"group":0},{"id32":422331606,"context":1,"group":1},{"id32":627359968,"context":1,"group":1},{"id32":3323676179,"context":1,"group":0},{"id32":4217315838,"context":1,"group":0},{"id32":4141672169,"context":1,"group":0},{"id32":1511706843,"context":1,"group":0},{"id32":677322851,"context":1,"group":0},{"id32":893408910,"context":1,"group":0},{"id32":766228818,"context":1,"group":0},{"id32":2552962615,"context":1,"group":2},{"id32":1542765264,"context":1,"group":2},{"id32":983707629,"context":1,"group":0},{"id32":2801833803,"context":1,"group":3},{"id32":2706258613,"context":1,"group":3},{"id32":3262302717,"context":1,"group":0},{"id32":421418845,"context":1,"group":0},{"id32":2464718481,"context":1,"group":0},{"id32":450787924,"context":1,"group":0},{"id32":1401708733,"context":1,"group":4},{"id32":2237848324,"context":1,"group":4},{"id32":2121224478,"context":1,"group":0},{"id32":110359831,"context":1,"group":5},{"id32":2077769934,"context":1,"group":5},{"id32":1918416101,"context":1,"group":0},{"id32":1898505845,"context":1,"group":0},{"id32":2902232420,"context":1,"group":0},{"id32":2782937074,"context":1,"group":0},{"id32":1391161752,"context":1,"group":0},{"id32":980743299,"context":1,"group":0},{"id32":1006242818,"context":1,"group":0},{"id32":1293830708,"context":1,"group":0},{"id32":3699613863,"context":1,"group":0},{"id32":3547528638,"context":1,"group":0},{"id32":4287360836,"context":1,"group":0},{"id32":968713913,"context":1,"group":0},{"id32":1214176856,"context":1,"group":0},{"id32":2144846208,"context":1,"group":7},{"id32":2365925959,"context":1,"group":0},{"id32":3994324289,"context":1,"group":7},{"id32":2616020441,"context":1,"group":0},{"id32":3279518460,"context":1,"group":0},{"id32":2683120236,"context":1,"group":0},{"id32":574562412,"context":1,"group":0},{"id32":2222856057,"context":1,"group":0},{"id32":1865943011,"context":1,"group":8},{"id32":199902803,"context":1,"group":8},{"id32":3412098611,"context":1,"group":0},{"id32":478168078,"context":1,"group":0},{"id32":257436714,"context":1,"group":0},{"id32":4010359064,"context":1,"group":0},{"id32":3933634258,"context":1,"group":0},{"id32":368572468,"context":1,"group":0},{"id32":1820072234,"context":1,"group":0},{"id32":1402635182,"context":1,"group":0},{"id32":786752156,"context":1,"group":0},{"id32":1307362764,"context":1,"group":0},{"id32":358548648,"context":1,"group":0},{"id32":3705692862,"context":2,"group":0},{"id32":2504204569,"context":1,"group":0},{"id32":1752849254,"context":1,"group":0},{"id32":81523500,"context":1,"group":0},{"id32":3744612820,"context":1,"group":0},{"id32":1248813848,"context":1,"group":0},{"id32":234584469,"context":1,"group":0},{"id32":1698977452,"context":1,"group":0},{"id32":1784509355,"context":1,"group":0},{"id32":1233597562,"context":1,"group":0},{"id32":1916939864,"context":1,"group":0},{"id32":4130639501,"context":1,"group":0},{"id32":3719011487,"context":1,"group":0},{"id32":382654467,"context":1,"group":0},{"id32":781677224,"context":1,"group":0},{"id32":1287780346,"context":1,"group":0},{"id32":1334351473,"context":1,"group":0},{"id32":3821064877,"context":1,"group":0},{"id32":3115257147,"context":1,"group":0},{"id32":98611233,"context":1,"group":0},{"id32":836288058,"context":1,"group":0},{"id32":900097455,"context":1,"group":0},{"id32":4149219876,"context":1,"group":0},{"id32":1739141267,"context":1,"group":0},{"id32":2435973138,"context":1,"group":0},{"id32":2989731610,"context":1,"group":0},{"id32":3515520839,"context":1,"group":0},{"id32":2875263080,"context":1,"group":0}]}

assignment_war_801_data = [{"id32":1659376888,"progress":[9039838,10193095,4665875],"expiresIn":458480,"setting":{"type":4,"overrideTitle":"MAJOR ORDER","overrideBrief":"Aid in the Ministry of Defense's Weapons Efficacy Review by killing the targeting number of enemies with one of the three designated machine guns.","taskDescription":"","tasks":[{"type":3,"values":[2,1,500000000,0,1,1978117092,0,0,0,0],"valueTypes":[1,2,3,4,6,5,8,9,11,12]},{"type":3,"values":[2,1,500000000,0,1,934703916,0,0,0,0],"valueTypes":[1,2,3,4,6,5,8,9,11,12]},{"type":3,"values":[2,1,500000000,0,1,4038802832,0,0,0,0],"valueTypes":[1,2,3,4,6,5,8,9,11,12]}],"rewards":[{"type":1,"id32":897894480,"amount":55}],"reward":{"type":1,"id32":897894480,"amount":55},"flags":2}}]

war_status_801_data = {
  "warId": 801,
  "time": 40109140,
  "impactMultiplier": 0.006899937,
  "storyBeatId32": 3744361090,
  "planetStatus": [
    {
      "index": 0,
      "owner": 1,
      "health": 6200000,
      "regenPerSecond": 4.1666665,
      "players": 109902,
      "position": {
        "x": 0,
        "y": 0
      }
    },
    {
      "index": 1,
      "owner": 1,
      "health": 1000000,
      "regenPerSecond": 4.1666665,
      "players": 0,
      "position": {
        "x": 0.05373042,
        "y": 0.10565466
      }
    },
    {
      "index": 2,
      "owner": 1,
      "health": 1000000,
      "regenPerSecond": 4.1666665,
      "players": 0,
      "position": {
        "x": 0.04664221,
        "y": 0.16758725
      }
    },
    {
      "index": 3,
      "owner": 4,
      "health": 1000000,
      "regenPerSecond": 208.33333,
      "players": 65,
      "position": {
        "x": 0.12536779,
        "y": 0.11821219
      }
    },
    {
      "index": 4,
      "owner": 4,
      "health": 1000000,
      "regenPerSecond": 208.33333,
      "players": 184,
      "position": {
        "x": 0.10280278,
        "y": 0.05765711
      }
    },
    {
      "index": 5,
      "owner": 4,
      "health": 1000000,
      "regenPerSecond": 208.33333,
      "players": 101,
      "position": {
        "x": 0.15988354,
        "y": 0.043583166
      }
    }
    
  ],
  "planetAttacks": [
    {
      "source": 0,
      "target": 1
    },
    {
      "source": 1,
      "target": 2
    },
    {
      "source": 2,
      "target": 3
    },
    {
      "source": 3,
      "target": 4
    },
    {
      "source": 4,
      "target": 5
    }
  ],
  "campaigns": [
    {
      "id": 0,
      "planetIndex": 162,
      "type": 0,
      "count": 2,
      "race": 1
    },
    {
      "id": 1,
      "planetIndex": 113,
      "type": 0,
      "count": 9,
      "race": 1
    },
    {
      "id": 2,
      "planetIndex": 218,
      "type": 0,
      "count": 2,
      "race": 1
    },
    {
      "id": 3,
      "planetIndex": 175,
      "type": 0,
      "count": 3,
      "race": 1
    },
    {
      "id": 4,
      "planetIndex": 70,
      "type": 0,
      "count": 5,
      "race": 1
    },
    {
      "id": 5,
      "planetIndex": 128,
      "type": 0,
      "count": 7,
      "race": 1
    }
  ],
  "communityTargets": [],
  "jointOperations": [],
  "planetEvents": [],
  "planetActiveEffects": [
    {
      "index": 1,
      "galacticEffectId": 1243
    },
    {
      "index": 2,
      "galacticEffectId": 1245
    },
    {
      "index": 3,
      "galacticEffectId": 1217
    },
    {
      "index": 4,
      "galacticEffectId": 1271
    },
    {
      "index": 5,
      "galacticEffectId": 1269
    },
    {
      "index": 0,
      "galacticEffectId": 1270
    }
  ],
  "planetRegions": [
    {
      "planetIndex": 0,
      "regionIndex": 1,
      "owner": 1,
      "health": 483101,
      "regerPerSecond": -11,
      "availabilityFactor": 1,
      "isAvailable": True,
      "players": 0
    },
    {
      "planetIndex": 0,
      "regionIndex": 2,
      "owner": 1,
      "health": 240494,
      "regerPerSecond": -8,
      "availabilityFactor": 1,
      "isAvailable": True,
      "players": 0
    },
    {
      "planetIndex": 0,
      "regionIndex": 3,
      "owner": 1,
      "health": 600000,
      "regerPerSecond": 0,
      "availabilityFactor": 1,
      "isAvailable": False,
      "players": 0
    },
    {
      "planetIndex": 0,
      "regionIndex": 4,
      "owner": 1,
      "health": 600000,
      "regerPerSecond": 0,
      "availabilityFactor": 1,
      "isAvailable": False,
      "players": 0
    },
    {
      "planetIndex": 0,
      "regionIndex": 5,
      "owner": 1,
      "health": 600000,
      "regerPerSecond": 0,
      "availabilityFactor": 1,
      "isAvailable": False,
      "players": 0
    },
    {
      "planetIndex": 0,
      "regionIndex": 6,
      "owner": 1,
      "health": 379932,
      "regerPerSecond": -8,
      "availabilityFactor": 1,
      "isAvailable": True,
      "players": 0
    },
    {
      "planetIndex": 0,
      "regionIndex": 0,
      "owner": 4,
      "health": 600000,
      "regerPerSecond": -13,
      "availabilityFactor": 1,
      "isAvailable": False,
      "players": 2
    }
  ],
  "activeElectionPolicyEffects": [],
  "globalEvents": [
    {
      "eventId": 1499462,
      "id32": 3667530279,
      "portraitId32": 0,
      "title": "",
      "titleId32": 0,
      "message": "",
      "messageId32": 0,
      "race": 0,
      "flag": 4,
      "introMediaId32": 0,
      "outroMediaId32": 0,
      "assignmentId32": 0,
      "effectIds": [],
      "planetIndices": [],
      "expireTime": 40791480
    },
    {
      "eventId": 1499467,
      "id32": 4067884805,
      "portraitId32": 0,
      "title": "SUCCESS",
      "titleId32": 2998873950,
      "message": "The initial salvos of the Illuminate invasion of Super Earth have been launched, and the Helldivers have dug in to defend our home: its Mega Cities and its high-class citizens. Waves of Illuminate invaders have been righteously slain, in a valiant, well-coordinated defense.\n\nThe significant blow to the enemy's surface and airborne detachments has <i=1>caused a 10% hit to Illuminate Fleet Strength,</i> in addition to their losses from attrition. \n\nIn this dark hour, innumerable tales of heroic patriotism have arisen. SEAF soldiers, fighting side-by-side with Helldivers, report decisive leadership, impeccable marksmanship, and unhesitating acts of self-sacrifice. \n\nCitizens across the galaxy are doing their part, listening to updates of the fighting as they work late to sustain the warfighting effort.\n\nBut despite the heroism of the Helldivers, no longer do all 7 of our great Mega Cities stand. The Battle for Super Earth is far from over.",
      "messageId32": 3195688721,
      "race": 1,
      "flag": 2,
      "introMediaId32": 0,
      "outroMediaId32": 1157982340,
      "assignmentId32": 0,
      "effectIds": [],
      "planetIndices": [],
      "expireTime": 40245315
    },
    {
      "eventId": 1499468,
      "id32": 182086879,
      "portraitId32": 0,
      "title": "BRIEFING",
      "titleId32": 2908633975,
      "message": "Eagleopolis, a venerable stronghold of Managed Democracy since time immemorial, lies in ruins. Its tattered shopping centers stand in warning as to the fate that awaits the rest of Super Earth, should our mission fail.\n\nThe initial wave of assault is over. <i=1>The Battle for Super Earth</i> now enters its critical next phase. \n\n<i=1>Illuminate Fleet Strength currently stands at 49%.</i> 6 Mega Cities remain standing. The Helldivers must dig in, alongside their SEAF allies, and continue to fight, day and night, to defend the heart of our Federation. \n\nThe surviving Mega Cities must be defended at all costs. The Helldivers must deploy to the Mega Cities as Illuminate pressure shifts among them to prevent them from falling. Once they fall, <i=1>they cannot be reclaimed.</i>\n\nFollowing an exhaustive Military Choice-Making Process, the Helldivers are ordered to execute a <i=1>sustained campaign of successful operations on Super Earth.</i> Completing the targeted number will result in an additional impact to Illuminate Fleet Strength. This course of action is the brilliant result of thorough analysis of our top strategic minds.\n\nThe fight ahead is long. Our resolve will be tested. To unleash the flames of Justice and triumph over Tyranny, we must battle through the inferno before us. Endure. Prevail. And avenge Eagleopolis.",
      "messageId32": 2369697708,
      "race": 1,
      "flag": 1,
      "introMediaId32": 392750462,
      "outroMediaId32": 0,
      "assignmentId32": 1307277960,
      "effectIds": [],
      "planetIndices": [],
      "expireTime": 40425270
    }
  ],
  "superEarthWarResults": [],
  "spaceStations": [],
  "globalResources": [
    {
      "id32": 175685818,
      "currentValue": 18566252,
      "maxValue": 40000000,
      "flags": 0
    }
  ],
  "layoutVersion": 44
}

news_feed_801_data = [{"id":2797,"published":2414563,"type":0,"tagIds":[],"message":"Terminid spores have engulfed Heeth and Angel's Venture, spawning hordes of Terminids that overwhelmed our colonial militias. Clearly, the bug hive instinct oriented their mindless expansion towards dishonoring the memory of those who fought to free these planets.\n\nYour fellow Helldivers paid for these lands with their lives. We cannot lose them now. Hold the planets until SEAF reinforcements arrive."}, {"id":2798,"published":2499000,"type":0,"tagIds":[],"message":"The Advanced Liberation Tools Research Agency (ALTRA) has tested successful prototypes of a new combat asset. Helldivers are advised to review proper mechanical operation procedures in preparation for the incoming asset."}, {"id":2799,"published":2507100,"type":0,"tagIds":[],"message":"NEW MAJOR ORDER\nTien Kwan is home to the sole arsenal of new Exosuit technology. It is only a matter of time before the Automatons discover the arsenal and steal it for themselves. Liberate Tien Kwan, before it's too late."}, {"id":2800,"published":2531100,"type":0,"tagIds":[],"message":"AUTOMATON COUNTERATTACK\nIntercepted messages indicate bot plans for a significant push. Increased resistance on Automaton planets is anticipated."}, {"id":2801,"published":2598240,"type":0,"tagIds":[],"message":"Well done, Helldivers. Tien Kwan has been returned to the care of Managed Democracy. The Morgunson Arsenal, and its stockpile of freshly-produced Exosuits, were recovered intact.\n\nThe EXO-45 PATRIOT EXOSUIT is now available for requisition."}, {"id":2802,"published":2705219,"type":0,"tagIds":[],"message":"Upon each Barrier Planet now stands a network of massive, Termicide-dispensing towers: the Terminid Control System. Once activated, the TCS will exterminate every Terminid on that planet, and inoculate it against all future infestations. \n\nHowever, surges in Terminid activity have forced the SEAF Engineers to evacuate. Now, only the Helldivers can ensure the safety of our citizens.\n\nThe Terminid Control System must be activated—at any cost."}, {"id":2803,"published":2705235,"type":0,"tagIds":[],"message":"NEW MAJOR ORDER\nActivate Terminid Control System"}, {"id":2804,"published":2822793,"type":0,"tagIds":[],"message":"FENRIR III SECURED\nThe Terminid Control System is now fully activated on Fenrir III."}, {"id":2805,"published":2899259,"type":0,"tagIds":[],"message":"TURING SECURED\nThe Terminid Control System is now fully activated on Turing."}, {"id":2806,"published":2899330,"type":0,"tagIds":[],"message":"The TCS has been fully activated on half of the Barrier Planets."}]


@app.route('/api/Configuration/GameClient', methods=['GET'])
def get_game_configuration():
    print(f"Received GET request for /api/Configuration/GameClient")
    print(f"Request Headers: {request.headers}")

    response = make_response(jsonify(game_client_config_data))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['Cache-Control'] = 'public,max-age=30'
    response.headers['Server'] = 'MockFlaskServer/1.0'
    return response

@app.route('/api/Account/Login', methods=['POST'])
def account_login():
    print(f"Received POST request for /api/Account/Login")
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    print(f"Request Headers: {request.headers}")
    print(f"Login Request Data: {data}")

    return jsonify({"status": "success", "message": "Login successful"}), 200

@app.route('/api/WarSeason/current/WarId', methods=['GET'])
def war_id():
    return jsonify({"id": 801})

@app.route('/api/WarSeason/801/warinfo', methods=['GET'])
def get_war_info_801():
    print(f"Received GET request for /api/WarSeason/801/warinfo")
    print(f"Request Headers: {request.headers}")
    return jsonify(war_info_801_data)

@app.route('/api/WarSeason/801/timeSinceStart', methods=['GET'])
def get_time_since_war_start():
    start_time_str = "2024-01-23 12:05:13"
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)

    current_time = datetime.now(timezone.utc)

    time_difference = current_time - start_time

    seconds_since_start = int(time_difference.total_seconds())

    print(f"Received GET request for /api/WarSeason/801/timeSinceStart")
    print(f"Request Headers: {request.headers}")
    return jsonify({"secondsSinceStart": seconds_since_start})

@app.route('/api/Account/InfoLookup', methods=['POST'])
def account_info_lookup():
    print(f"Received POST request for /api/Account/InfoLookup")
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    print(f"Request Headers: {request.headers}")
    print(f"InfoLookup Request Data: {data}")

    return jsonify({"status": "success", "message": "Info lookup successful"}), 200

@app.route('/api/WarSeason/GalacticWarEffects', methods=['GET'])
def get_galactic_war_effects():
    print(f"Received GET request for /api/WarSeason/GalacticWarEffects")
    print(f"Request Headers: {request.headers}")
    return jsonify(galactic_war_effects_data)

@app.route('/api/WarSeason/NewsTicker', methods=['GET'])
def get_news_ticker():
    print(f"Received GET request for /api/WarSeason/NewsTicker")
    print(f"Request Headers: {request.headers}")
    return jsonify(news_ticker_data)

@app.route('/api/v2/Assignment/War/801', methods=['GET'])
def get_assignment_war_801():
    print(f"Received GET request for /api/v2/Assignment/War/801")
    print(f"Request Headers: {request.headers}")
    return jsonify(assignment_war_801_data)

@app.route('/api/WarSeason/801/Status', methods=['GET'])
def get_war_status_801():
    print(f"Received GET request for /api/WarSeason/801/Status")
    print(f"Request Headers: {request.headers}")
    return jsonify(war_status_801_data)

@app.route('/api/NewsFeed/801', methods=['GET'])
def get_news_feed_801():
    print(f"Received GET request for /api/NewsFeed/801")
    print(f"Request Headers: {request.headers}")
    return jsonify(news_feed_801_data)

@app.route('/api/Operation', methods=['GET'])
def get_operation_ids():
    print(f"Received GET request for /api/Operation")
    print(f"Request Headers: {request.headers}")
    return jsonify({"operationIds": [0, 0, 0, 0, 0]})

if __name__ == '__main__':
    print("Starting mock Helldivers API server with HTTPS...")
    app.run(debug=True, host='0.0.0.0', port=443)