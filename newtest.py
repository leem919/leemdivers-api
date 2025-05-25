from flask import Flask, request, jsonify, make_response
import json
from datetime import datetime, timezone

app = Flask(__name__)

game_client_config_data = {"pollingConfiguration": [{"id32": 2298181301, "interval": 900}, {"id32": 1090315739, "interval": 90},{"id32": 1370749971, "interval": 300}, {"id32": 2401412089, "interval": 300},{"id32": 2885838245, "interval": 60}, {"id32": 1663330584, "interval": 90},{"id32": 4239899827, "interval": 60}, {"id32": 1101022388, "interval": 60},{"id32": 2321903753, "interval": 300}, {"id32": 3012448242, "interval": 600},{"id32": 3443535003, "interval": 9000}, {"id32": 3181113487, "interval": 9000},{"id32": 3069176075, "interval": 9000}, {"id32": 2701907425, "interval": 300},{"id32": 1896257217, "interval": 600}, {"id32": 3813637705, "interval": 9000},{"id32": 924828572, "interval": 300}, {"id32": 952049051, "interval": 20},{"id32": 1869673247, "interval": 9000}, {"id32": 3753697600, "interval": 10},{"id32": 2869249345, "interval": 300}, {"id32": 907021859, "interval": 90},{"id32": 1950849984, "interval": 45}, {"id32": 1453632692, "interval": 10},{"id32": 1977859078, "interval": 360}, {"id32": 2187912720, "interval": 300},{"id32": 895335920, "interval": 1800}, {"id32": 2442802038, "interval": 0},{"id32": 2668903150, "interval": 125}, {"id32": 2406296651, "interval": 4},{"id32": 3891819455, "interval": 6}, {"id32": 3486820593, "interval": 0},{"id32": 1250723970, "interval": 1}, {"id32": 2771693880, "interval": 4},{"id32": 2244166905, "interval": 256}, {"id32": 1272239318, "interval": 30},{"id32": 1383229038, "interval": 60}, {"id32": 1548226027, "interval": 900}],"featureConfiguration": [{"id32": 3836664312, "enabled": True, "data": "", "probability": 100},{"id32": 1191893463, "enabled": False, "data": "", "probability": 0},{"id32": 1731970340, "enabled": True, "data": "", "probability": 100},{"id32": 147543665, "enabled": True, "data": "", "probability": 100},{"id32": 3050214232, "enabled": True, "data": "", "probability": 100},{"id32": 2349288591, "enabled": True, "data": "", "probability": 100},{"id32": 1037736245, "enabled": True, "data": "", "probability": 100},{"id32": 2938211500, "enabled": True, "data": "", "probability": 100},{"id32": 3977691125, "enabled": False, "data": "true", "probability": 100},{"id32": 2056779757, "enabled": True, "data": "", "probability": 100}],"onlineOverrideConfiguration": [{"id32": 3836664312, "mixId": 3836664312, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 1731970340, "mixId": 1731970340, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 2122501867, "mixId": 1730283156, "parentMixId": 1731970340, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 1181373120, "mixId": 1470246927, "parentMixId": 1731970340, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 426721852, "mixId": 163828688, "parentMixId": 1731970340, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 271322048, "mixId": 3250093964, "parentMixId": 1731970340, "enabled": True, "data": "5", "dataType": 5, "probability": 100},{"id32": 1684721270, "mixId": 66753034, "parentMixId": 1731970340, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 2483371866, "mixId": 774580170, "parentMixId": 1731970340, "enabled": True, "data": "8", "dataType": 5, "probability": 100},{"id32": 609105814, "mixId": 2800439123, "parentMixId": 1731970340, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 365754012, "mixId": 3931218534, "parentMixId": 1731970340, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 1576391531, "mixId": 375722071, "parentMixId": 1731970340, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 701374015, "mixId": 3169599608, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 2422325091, "mixId": 4240916675, "parentMixId": 3169599608, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 1634896105, "mixId": 1349423522, "parentMixId": 3169599608, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 3435642769, "mixId": 2582729456, "parentMixId": 3169599608, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 3494162224, "mixId": 2817067926, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 262888231, "mixId": 2362886741, "parentMixId": 2817067926, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 2422325091, "mixId": 658815317, "parentMixId": 2817067926, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 1634896105, "mixId": 2347591732, "parentMixId": 2817067926, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 3435642769, "mixId": 1114811238, "parentMixId": 2817067926, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 262888231, "mixId": 1506492344, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 3494162224, "mixId": 1121137709, "parentMixId": 1506492344, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 2422325091, "mixId": 4065938616, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 701374015, "mixId": 2874273475, "parentMixId": 4065938616, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 3494162224, "mixId": 2958337325, "parentMixId": 4065938616, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 3435642769, "mixId": 2161307696, "parentMixId": 4065938616, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 1634896105, "mixId": 1592827353, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 701374015, "mixId": 3062600086, "parentMixId": 1592827353, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 3494162224, "mixId": 2911820408, "parentMixId": 1592827353, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 3435642769, "mixId": 2540658315, "parentMixId": 375722071, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 701374015, "mixId": 3977082940, "parentMixId": 2540658315, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 3494162224, "mixId": 4127732690, "parentMixId": 2540658315, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 2422325091, "mixId": 2746774780, "parentMixId": 2540658315, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 147543665, "mixId": 147543665, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 3550970463, "mixId": 4049186208, "parentMixId": 147543665, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 2117564271, "mixId": 824842026, "parentMixId": 147543665, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 216534926, "mixId": 182133893, "parentMixId": 147543665, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 3050214232, "mixId": 3050214232, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 900631814, "mixId": 2283105102, "parentMixId": 3050214232, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 2349288591, "mixId": 2349288591, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 1797233012, "mixId": 1270538380, "parentMixId": 2349288591, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 3726540269, "mixId": 1476117903, "parentMixId": 2349288591, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 1037736245, "mixId": 1037736245, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 2825683808, "mixId": 425449573, "parentMixId": 1037736245, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 2178119527, "mixId": 705871493, "parentMixId": 1037736245, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 2325312666, "mixId": 2662298477, "parentMixId": 1037736245, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 2764011581, "mixId": 4088618188, "parentMixId": 1037736245, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 2938211500, "mixId": 2938211500, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 434365072, "mixId": 240163142, "parentMixId": 2938211500, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 4174527442, "mixId": 2621129951, "parentMixId": 240163142, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 788007814, "mixId": 617872317, "parentMixId": 2938211500, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 4174527442, "mixId": 997795168, "parentMixId": 617872317, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 4129662363, "mixId": 4201226499, "parentMixId": 2938211500, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 4174527442, "mixId": 1338891998, "parentMixId": 4201226499, "enabled": True, "data": "false", "dataType": 7, "probability": 100},{"id32": 3809493971, "mixId": 2550465041, "parentMixId": 2938211500, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 4174527442, "mixId": 3960996740, "parentMixId": 2550465041, "enabled": True, "data": "true", "dataType": 7, "probability": 100},{"id32": 4205559465, "mixId": 48726272, "parentMixId": 2938211500, "enabled": True, "data": "10", "dataType": 6, "probability": 100},{"id32": 2056779757, "mixId": 2056779757, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 3031275039, "mixId": 2453758708, "parentMixId": 2056779757, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 3124066580, "mixId": 1787495693, "parentMixId": 2453758708, "enabled": True, "data": "", "dataType": 0, "probability": 100},{"id32": 1893896155, "mixId": 3416152325, "parentMixId": 1787495693, "enabled": True, "data": "100", "dataType": 6, "probability": 100},{"id32": 897386910, "mixId": 2123114616, "parentMixId": 1787495693, "enabled": True, "data": "10", "dataType": 6, "probability": 100}],"matchMakingConfiguration": {"ping": [{"weight": 1, "value": 0}, {"weight": 1, "value": 1}],"inLoadout": [{"weight": 1, "value": 0}, {"weight": 1, "value": 1}],"preferenceGroupMatch": [{"weight": 1, "value": 0}, {"weight": 1, "value": 1}],"gameProgress": [{"weight": 0.1, "value": 100}, {"weight": 1, "value": 50}, {"weight": 1, "value": 0}],"partySize": [{"weight": 0.1, "value": 4}, {"weight": 0.1, "value": 2}, {"weight": 1, "value": 1}],"hostability": [{"weight": 0.5, "value": 0}, {"weight": 1, "value": 1}],"isFriend": [{"weight": 1, "value": 1}, {"weight": 1, "value": 0}],"isClanMember": [{"weight": 1, "value": 0}, {"weight": 1, "value": 1}],"sosBeacons": [{"weight": 0.5, "value": 0}, {"weight": 1, "value": 1}],"missionSelected": [{"weight": 0.75, "value": 0}, {"weight": 1, "value": 1}],"operationProgression": [{"weight": 0.5, "value": 100}, {"weight": 1, "value": 0}],"difficultyGap": [{"weight": 0.1, "value": 3}, {"weight": 0.75, "value": 2}, {"weight": 1, "value": 1}, {"weight": 1, "value": 0}]},"matchMakingProperties": [{"id32": 2315033710, "values": [0, 1], "weights": [1, 1]},{"id32": 1038221924, "values": [0, 1], "weights": [0.5, 1]},{"id32": 1778784146, "values": [100, 50, 0], "weights": [0.1, 1, 1]},{"id32": 2042807422, "values": [4, 2, 1], "weights": [0.1, 0.1, 1]},{"id32": 2887792429, "values": [0, 1], "weights": [0.5, 2]},{"id32": 1310771148, "values": [0, 1], "weights": [0.75, 1]},{"id32": 1272241989, "values": [100, 0], "weights": [0.5, 1]},{"id32": 3698074356, "values": [3, 2, 1, 0], "weights": [0.1, 0.75, 1, 1]},{"id32": 2538489315, "values": [0, 1], "weights": [1, 1]},{"id32": 2711371980, "values": [0, 1], "weights": [1, 1]},{"id32": 184805542, "values": [0, 1], "weights": [1, 1]}]}

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

assignment_war_801_data = [{"id32":1659376888,"progress":[9039838,10193095,4665875],"expiresIn":458480,"setting":{"type":4,"overrideTitle":"MAJOR ORDER","overrideBrief":"Shit your pants","taskDescription":"","tasks":[{"type":3,"values":[2,1,500000000,0,1,1978117092,0,0,0,0],"valueTypes":[1,2,3,4,6,5,8,9,11,12]},{"type":3,"values":[2,1,500000000,0,1,934703916,0,0,0,0],"valueTypes":[1,2,3,4,6,5,8,9,11,12]},{"type":3,"values":[2,1,500000000,0,1,4038802832,0,0,0,0],"valueTypes":[1,2,3,4,6,5,8,9,11,12]}],"rewards":[{"type":1,"id32":897894480,"amount":999}],"reward":{"type":1,"id32":897894480,"amount":999},"flags":2}}]

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
      "players": 95483745,
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
      "planetIndex": 0,
      "type": 0,
      "count": 2,
      "race": 3
    },
    {
      "id": 1,
      "planetIndex": 1,
      "type": 0,
      "count": 9,
      "race": 2
    },
    {
      "id": 2,
      "planetIndex": 2,
      "type": 0,
      "count": 2,
      "race": 3
    },
    {
      "id": 3,
      "planetIndex": 3,
      "type": 0,
      "count": 3,
      "race": 2
    },
    {
      "id": 4,
      "planetIndex": 4,
      "type": 0,
      "count": 5,
      "race": 2
    },
    {
      "id": 5,
      "planetIndex": 5,
      "type": 0,
      "count": 7,
      "race": 3
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
      "regionIndex": 0,
      "owner": 1,
      "health": 483101,
      "regerPerSecond": -11,
      "availabilityFactor": 1,
      "isAvailable": True,
      "players": 0
    },
    {
      "planetIndex": 1,
      "regionIndex": 1,
      "owner": 1,
      "health": 240494,
      "regerPerSecond": -8,
      "availabilityFactor": 1,
      "isAvailable": True,
      "players": 0
    },
    {
      "planetIndex": 2,
      "regionIndex": 1,
      "owner": 1,
      "health": 600000,
      "regerPerSecond": 0,
      "availabilityFactor": 1,
      "isAvailable": True,
      "players": 0
    },
    {
      "planetIndex": 3,
      "regionIndex": 1,
      "owner": 1,
      "health": 600000,
      "regerPerSecond": 0,
      "availabilityFactor": 1,
      "isAvailable": True,
      "players": 0
    },
    {
      "planetIndex": 4,
      "regionIndex": 1,
      "owner": 1,
      "health": 600000,
      "regerPerSecond": 0,
      "availabilityFactor": 1,
      "isAvailable": True,
      "players": 0
    },
    {
      "planetIndex": 5,
      "regionIndex": 1,
      "owner": 1,
      "health": 379932,
      "regerPerSecond": -8,
      "availabilityFactor": 1,
      "isAvailable": True,
      "players": 0
    }
  ],
  "activeElectionPolicyEffects": [],
  "globalEvents": [
    {
      "eventId": 1499462,
      "id32": 3667530278,
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
      "eventId": 1499149,
      "id32": 4067884804,
      "portraitId32": 0,
      "title": "LEEMDIVERS SERVER",
      "titleId32": 2998873949,
      "message": "This is a test.",
      "messageId32": 3195688720,
      "race": 1,
      "flag": 2,
      "introMediaId32": 0,
      "outroMediaId32": 0,
      "assignmentId32": 0,
      "effectIds": [],
      "planetIndices": [],
      "expireTime": 40245315
    },
    {
      "eventId": 1499149,
      "id32": 182086878,
      "portraitId32": 0,
      "title": "test",
      "titleId32": 2908633974,
      "message": "test",
      "messageId32": 2369697707,
      "race": 1,
      "flag": 1,
      "introMediaId32": 0,
      "outroMediaId32": 0,
      "assignmentId32": 0,
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

news_feed_801_data = []

operations_data = {"nextOperationId":531,"operations":[{"id":0,"seed":0,"warId":0,"planetIndex":0,"placementNodeIndex":0,"isActive":False,"type":0,"difficulty":0,"race":0,"missions":[],"rewards":[]},{"id":0,"seed":0,"warId":0,"planetIndex":0,"placementNodeIndex":0,"isActive":False,"type":0,"difficulty":0,"race":0,"missions":[],"rewards":[]},{"id":0,"seed":0,"warId":0,"planetIndex":0,"placementNodeIndex":0,"isActive":False,"type":0,"difficulty":0,"race":0,"missions":[],"rewards":[]},{"id":0,"seed":0,"warId":0,"planetIndex":0,"placementNodeIndex":0,"isActive":False,"type":0,"difficulty":0,"race":0,"missions":[],"rewards":[]},{"id":0,"seed":0,"warId":0,"planetIndex":0,"placementNodeIndex":0,"isActive":False,"type":0,"difficulty":0,"race":0,"missions":[],"rewards":[]}]}

item_packages_data = []

progression_packages_data = []

progression_items_data = []

level_spec_data = [{"level":1,"requiredExperience":1},{"level":2,"requiredExperience":100},{"level":3,"requiredExperience":350},{"level":4,"requiredExperience":850},{"level":5,"requiredExperience":1600},{"level":6,"requiredExperience":2600},{"level":7,"requiredExperience":3600},{"level":8,"requiredExperience":4600},{"level":9,"requiredExperience":5850},{"level":10,"requiredExperience":7100},{"level":11,"requiredExperience":8400},{"level":12,"requiredExperience":9900},{"level":13,"requiredExperience":11400},{"level":14,"requiredExperience":12900},{"level":15,"requiredExperience":14400},{"level":16,"requiredExperience":15900},{"level":17,"requiredExperience":17900},{"level":18,"requiredExperience":19900},{"level":19,"requiredExperience":21900},{"level":20,"requiredExperience":23900},{"level":21,"requiredExperience":25900},{"level":22,"requiredExperience":28400},{"level":23,"requiredExperience":30900},{"level":24,"requiredExperience":33400},{"level":25,"requiredExperience":35900},{"level":26,"requiredExperience":38400},{"level":27,"requiredExperience":41400},{"level":28,"requiredExperience":44400},{"level":29,"requiredExperience":47400},{"level":30,"requiredExperience":50400},{"level":31,"requiredExperience":53400},{"level":32,"requiredExperience":56900},{"level":33,"requiredExperience":60400},{"level":34,"requiredExperience":63900},{"level":35,"requiredExperience":67400},{"level":36,"requiredExperience":70900},{"level":37,"requiredExperience":74900},{"level":38,"requiredExperience":78900},{"level":39,"requiredExperience":82900},{"level":40,"requiredExperience":86900},{"level":41,"requiredExperience":90900},{"level":42,"requiredExperience":95400},{"level":43,"requiredExperience":99900},{"level":44,"requiredExperience":104400},{"level":45,"requiredExperience":108900},{"level":46,"requiredExperience":113400},{"level":47,"requiredExperience":118400},{"level":48,"requiredExperience":123400},{"level":49,"requiredExperience":128400},{"level":50,"requiredExperience":133400},{"level":51,"requiredExperience":138900},{"level":52,"requiredExperience":144400},{"level":53,"requiredExperience":149900},{"level":54,"requiredExperience":155400},{"level":55,"requiredExperience":161000},{"level":56,"requiredExperience":167000},{"level":57,"requiredExperience":173000},{"level":58,"requiredExperience":179000},{"level":59,"requiredExperience":185000},{"level":60,"requiredExperience":191000},{"level":61,"requiredExperience":197500},{"level":62,"requiredExperience":204000},{"level":63,"requiredExperience":210500},{"level":64,"requiredExperience":217000},{"level":65,"requiredExperience":223500},{"level":66,"requiredExperience":230500},{"level":67,"requiredExperience":237500},{"level":68,"requiredExperience":244500},{"level":69,"requiredExperience":251500},{"level":70,"requiredExperience":258500},{"level":71,"requiredExperience":266000},{"level":72,"requiredExperience":273500},{"level":73,"requiredExperience":281000},{"level":74,"requiredExperience":288500},{"level":75,"requiredExperience":296000},{"level":76,"requiredExperience":304000},{"level":77,"requiredExperience":312000},{"level":78,"requiredExperience":320000},{"level":79,"requiredExperience":328000},{"level":80,"requiredExperience":336000},{"level":81,"requiredExperience":344500},{"level":82,"requiredExperience":353000},{"level":83,"requiredExperience":361500},{"level":84,"requiredExperience":370000},{"level":85,"requiredExperience":378500},{"level":86,"requiredExperience":387500},{"level":87,"requiredExperience":396500},{"level":88,"requiredExperience":405500},{"level":89,"requiredExperience":414500},{"level":90,"requiredExperience":423500},{"level":91,"requiredExperience":433000},{"level":92,"requiredExperience":442500},{"level":93,"requiredExperience":452000},{"level":94,"requiredExperience":461500},{"level":95,"requiredExperience":471000},{"level":96,"requiredExperience":481000},{"level":97,"requiredExperience":491000},{"level":98,"requiredExperience":501000},{"level":99,"requiredExperience":511000},{"level":100,"requiredExperience":521500},{"level":101,"requiredExperience":532000},{"level":102,"requiredExperience":542500},{"level":103,"requiredExperience":553000},{"level":104,"requiredExperience":564000},{"level":105,"requiredExperience":575000},{"level":106,"requiredExperience":586000},{"level":107,"requiredExperience":597000},{"level":108,"requiredExperience":608000},{"level":109,"requiredExperience":619500},{"level":110,"requiredExperience":631000},{"level":111,"requiredExperience":642500},{"level":112,"requiredExperience":654000},{"level":113,"requiredExperience":665500},{"level":114,"requiredExperience":677500},{"level":115,"requiredExperience":689500},{"level":116,"requiredExperience":701500},{"level":117,"requiredExperience":713500},{"level":118,"requiredExperience":725500},{"level":119,"requiredExperience":738000},{"level":120,"requiredExperience":750500},{"level":121,"requiredExperience":763000},{"level":122,"requiredExperience":775500},{"level":123,"requiredExperience":788000},{"level":124,"requiredExperience":801000},{"level":125,"requiredExperience":814000},{"level":126,"requiredExperience":827000},{"level":127,"requiredExperience":840000},{"level":128,"requiredExperience":853000},{"level":129,"requiredExperience":866500},{"level":130,"requiredExperience":880000},{"level":131,"requiredExperience":893500},{"level":132,"requiredExperience":907000},{"level":133,"requiredExperience":920500},{"level":134,"requiredExperience":934500},{"level":135,"requiredExperience":948500},{"level":136,"requiredExperience":962500},{"level":137,"requiredExperience":976500},{"level":138,"requiredExperience":990500},{"level":139,"requiredExperience":1005000},{"level":140,"requiredExperience":1019500},{"level":141,"requiredExperience":1034000},{"level":142,"requiredExperience":1048500},{"level":143,"requiredExperience":1063000},{"level":144,"requiredExperience":1078000},{"level":145,"requiredExperience":1093000},{"level":146,"requiredExperience":1108000},{"level":147,"requiredExperience":1123000},{"level":148,"requiredExperience":1138000},{"level":149,"requiredExperience":1153000},{"level":150,"requiredExperience":1168000},{"level":151,"requiredExperience":8088010},{"level":152,"requiredExperience":8205310},{"level":153,"requiredExperience":8323310},{"level":154,"requiredExperience":8442010},{"level":155,"requiredExperience":8561410},{"level":156,"requiredExperience":8681510},{"level":157,"requiredExperience":8802310},{"level":158,"requiredExperience":8923810},{"level":159,"requiredExperience":9046010},{"level":160,"requiredExperience":9168910},{"level":161,"requiredExperience":9292510},{"level":162,"requiredExperience":9416810},{"level":163,"requiredExperience":9541810},{"level":164,"requiredExperience":9667510},{"level":165,"requiredExperience":9793910},{"level":166,"requiredExperience":9921010},{"level":167,"requiredExperience":10048810},{"level":168,"requiredExperience":10177310},{"level":169,"requiredExperience":10306510},{"level":170,"requiredExperience":10436410},{"level":171,"requiredExperience":10567010},{"level":172,"requiredExperience":10698310},{"level":173,"requiredExperience":10830310},{"level":174,"requiredExperience":10963010},{"level":175,"requiredExperience":11096410},{"level":176,"requiredExperience":11230510},{"level":177,"requiredExperience":11365310},{"level":178,"requiredExperience":11500810},{"level":179,"requiredExperience":11637010},{"level":180,"requiredExperience":11773910},{"level":181,"requiredExperience":11911510},{"level":182,"requiredExperience":12049810},{"level":183,"requiredExperience":12188810},{"level":184,"requiredExperience":12328510},{"level":185,"requiredExperience":12468910},{"level":186,"requiredExperience":12610010},{"level":187,"requiredExperience":12751810},{"level":188,"requiredExperience":12894310},{"level":189,"requiredExperience":13037510},{"level":190,"requiredExperience":13181410},{"level":191,"requiredExperience":13326010},{"level":192,"requiredExperience":13471310},{"level":193,"requiredExperience":13617310},{"level":194,"requiredExperience":13764010},{"level":195,"requiredExperience":13911410},{"level":196,"requiredExperience":14059510},{"level":197,"requiredExperience":14208310},{"level":198,"requiredExperience":14357810},{"level":199,"requiredExperience":14508010},{"level":200,"requiredExperience":14658910}]

progression_data = {"experience":1930930,"selectedProgressionPackage":131213678,"activeSeasonPass":1929468580,"onboardingState":128,"onboardingFlags":3768187,"packageProgress":[{"id32":1949876251,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":3439606727,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":2221505542,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":2659105163,"level":5,"progress":126,"sortOrder":0,"claimedLevels":[]},{"id32":1334452973,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":4111972552,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":4090978686,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":2373460877,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":1973516948,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":1681710644,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":3499835822,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":1059686006,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":287968734,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":1445043045,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":3988417885,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":3479006272,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":1414744964,"level":7,"progress":36,"sortOrder":0,"claimedLevels":[]},{"id32":2679158493,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":2750223772,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":2941409959,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":2093204274,"level":24,"progress":4704,"sortOrder":0,"claimedLevels":[]},{"id32":652555970,"level":8,"progress":821,"sortOrder":0,"claimedLevels":[]},{"id32":2031945469,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":297733241,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":1240353314,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":1125762146,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":3350514626,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":3247913466,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":1437213432,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":3391943729,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":1691930195,"level":1,"progress":0,"sortOrder":0,"claimedLevels":[]},{"id32":515780825,"level":9,"progress":0,"sortOrder":3,"claimedLevels":[2,3,4,5,6,7,8,1]},{"id32":131213678,"level":5,"progress":0,"sortOrder":0,"claimedLevels":[3,1,2,4]},{"id32":4202868518,"level":5,"progress":0,"sortOrder":0,"claimedLevels":[1,2,3,4]},{"id32":2822932719,"level":5,"progress":0,"sortOrder":0,"claimedLevels":[2,3,1,4]},{"id32":792686718,"level":5,"progress":0,"sortOrder":0,"claimedLevels":[1,2,3,4]},{"id32":1831255310,"level":5,"progress":0,"sortOrder":0,"claimedLevels":[1,2,3,4]},{"id32":2636037703,"level":5,"progress":0,"sortOrder":0,"claimedLevels":[1,2,3,4]}],"assignments":[{"id32":680227134,"progress":[0],"expiresIn":0,"setting":{"type":2,"overrideTitle":"","overrideBrief":"","taskDescription":"","tasks":[{"type":7,"values":[0,0,3,0,0,0,0,0,0],"valueTypes":[1,2,3,8,7,9,10,11,12]}],"rewards":[{"type":1,"id32":897894480,"amount":15}],"reward":{"type":1,"id32":897894480,"amount":15},"flags":0}},{"id32":2981755580,"progress":[],"expiresIn":0,"setting":{"type":0,"overrideTitle":"","overrideBrief":"","taskDescription":"","tasks":[{"type":8,"values":[1],"valueTypes":[3]}],"rewards":[{"type":1,"id32":1849408484,"amount":1}],"reward":{"type":1,"id32":1849408484,"amount":1},"flags":0}}],"purchasedSeasonPassItems":[445,450,444,447,453,455,456,452,457,462,443,458,454,446,448,459,451,463,460,449,461,417,408,415,405,403,416,402,76,78,89,87,82,84,92,558,542,545,543,541,540,548,549,551,546,376,382,375,377,384,383,390,378,386,387,385,381,400,401,404,399,413,406,414,412,407,409,410,418,411,420,419,427,424,425,422,421,423,426,428,432,430,433,436,434,440,439,438,442,437,441,429,435,431,392,397,396,391,398,395,393,394,465,464,468,475,474,471,470,467,479,469,472,478,481,466,476,480,477,483,482,473,555,550,547,554,553,556,552,557,491,488,489,486,484,494,496,492,497,503,495,504,502,499,505,493,485,490,487,498,501,500,388,379,380,389,8,6,12,13,18,20,3,17,4,7,1,9,15,11,23,26,21,27,28,16,19,37,34,40,32,39,29,38,50,48,46,52,45,30,31,53,55,59,99,36,24,61,60,54,67,71,65,64,49,43,51,68,256,258,58,62,77,101,100,74,70,86,69,85,259,260,271,72,267,317,318,326,324,320,325,322,334,323,321,319,327,328,333,329,332,331,330,339,335,342,336,338,337,340,341,511,510,506,507,508,509,516,513,517,515,512,514,519,518,521,80,88,98,96,102,297,94,97,95,90,272,268,261,255,266,257,262,371,374,265,269,274,276,273,277,373,278,275,279,300,298,301,302,305,309,310,306,307,296,299,303,295,304,311,314,313,315,308,316,312,522,520,233],"shipName":[45,18],"location":{"warId":-1,"planetIndex":-1,"territoryIndex":-1},"achievements":[{"id":6,"value":1539},{"id":8,"value":257731},{"id":17,"value":3220},{"id":24,"value":1693}]}

progression_inventory_data = {}

progression_customization_data = {"undergarment_type":826373086,"helmet_set":1318035279,"cape_set":1180159923,"armor_set":2006219485,"voice_pack_set":2128091030,"victory_pose_index":1964594095,"banner":1541157352,"shuttle":0,"hellpod":0,"combat_walker_skin":0,"combat_walker_emancipator_skin":0,"titleId32":2471970991}

reward_entries_data = {"badges":[{"id32":2365423054,"amount":0,"influence":0,"itemRewards":[]},{"id32":4184186012,"amount":0,"influence":0,"itemRewards":[]},{"id32":1624799956,"amount":0,"influence":0,"itemRewards":[]},{"id32":334721601,"amount":0,"influence":0,"itemRewards":[]},{"id32":1150782017,"amount":0,"influence":5,"itemRewards":[{"mixId":3608481516,"amount":50}]},{"id32":1497655096,"amount":0,"influence":10,"itemRewards":[{"mixId":3608481516,"amount":100}]},{"id32":3900407341,"amount":0,"influence":20,"itemRewards":[{"mixId":3608481516,"amount":150}]},{"id32":2984854125,"amount":0,"influence":5,"itemRewards":[{"mixId":3608481516,"amount":50}]},{"id32":106414693,"amount":0,"influence":10,"itemRewards":[{"mixId":3608481516,"amount":100}]},{"id32":3412826211,"amount":0,"influence":20,"itemRewards":[{"mixId":3608481516,"amount":150}]},{"id32":1595769879,"amount":0,"influence":5,"itemRewards":[{"mixId":3608481516,"amount":50}]},{"id32":2701252726,"amount":0,"influence":10,"itemRewards":[{"mixId":3608481516,"amount":100}]},{"id32":4283980414,"amount":0,"influence":20,"itemRewards":[{"mixId":3608481516,"amount":150}]},{"id32":889185878,"amount":0,"influence":100,"itemRewards":[{"mixId":3608481516,"amount":500}]},{"id32":3839642669,"amount":0,"influence":100,"itemRewards":[{"mixId":3608481516,"amount":500}]},{"id32":1748229498,"amount":0,"influence":50,"itemRewards":[{"mixId":3608481516,"amount":200}]},{"id32":3673690865,"amount":0,"influence":50,"itemRewards":[{"mixId":3608481516,"amount":200}]},{"id32":396353427,"amount":0,"influence":40,"itemRewards":[{"mixId":3608481516,"amount":200}]},{"id32":185689788,"amount":0,"influence":40,"itemRewards":[{"mixId":3608481516,"amount":200}]},{"id32":1265668144,"amount":0,"influence":40,"itemRewards":[{"mixId":3608481516,"amount":200}]},{"id32":3071768642,"amount":0,"influence":20,"itemRewards":[{"mixId":3608481516,"amount":100}]},{"id32":4140461052,"amount":0,"influence":100,"itemRewards":[{"mixId":3608481516,"amount":500}]},{"id32":357290428,"amount":0,"influence":25,"itemRewards":[{"mixId":3608481516,"amount":125}]},{"id32":3181424819,"amount":0,"influence":25,"itemRewards":[{"mixId":3608481516,"amount":125}]},{"id32":738696266,"amount":0,"influence":25,"itemRewards":[{"mixId":3608481516,"amount":125}]},{"id32":792703122,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":1}]},{"id32":201763195,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":2}]},{"id32":3154752032,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":3}]},{"id32":3661601579,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":2}]},{"id32":64984334,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":4}]},{"id32":137631288,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":3}]},{"id32":1382575844,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":5}]},{"id32":2462669900,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":6}]},{"id32":1495751876,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":4}]},{"id32":280848384,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":6}]},{"id32":2320144617,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":8}]},{"id32":4142807363,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":5}]},{"id32":1028127799,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":7}]},{"id32":1923384995,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":9}]},{"id32":1376484766,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":6}]},{"id32":283480591,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":8}]},{"id32":1945945030,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":10}]},{"id32":1265652808,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":7}]},{"id32":658544424,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":10}]},{"id32":2283307406,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":12}]},{"id32":1039359204,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":8}]},{"id32":3053361929,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":11}]},{"id32":3532218295,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":14}]},{"id32":2183770126,"amount":0,"influence":0,"itemRewards":[{"mixId":3608481516,"amount":-25}]},{"id32":3973473708,"amount":0,"influence":20,"itemRewards":[{"mixId":3608481516,"amount":50}]},{"id32":1449100876,"amount":0,"influence":1,"itemRewards":[{"mixId":3608481516,"amount":4}]},{"id32":2328168609,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":9}]},{"id32":1544112617,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":12}]},{"id32":3041491160,"amount":0,"influence":0,"itemRewards":[{"mixId":897894480,"amount":15}]}],"multipliers":[{"id32":540020798,"factor":1,"influenceFactor":1},{"id32":357436400,"factor":0,"influenceFactor":0},{"id32":1029670384,"factor":1,"influenceFactor":1},{"id32":2459419623,"factor":1,"influenceFactor":1},{"id32":2389643433,"factor":1.25,"influenceFactor":1.25},{"id32":4122185694,"factor":1.5,"influenceFactor":1.5},{"id32":33707031,"factor":1.75,"influenceFactor":1.75},{"id32":1237009911,"factor":2,"influenceFactor":2},{"id32":1155577500,"factor":2.5,"influenceFactor":2.5},{"id32":851354768,"factor":3,"influenceFactor":3},{"id32":1714937842,"factor":3.5,"influenceFactor":3.5},{"id32":1551907567,"factor":4,"influenceFactor":4},{"id32":2736093795,"factor":4.5,"influenceFactor":4.5},{"id32":2607705626,"factor":5,"influenceFactor":5},{"id32":3068507239,"factor":0.5,"influenceFactor":0.5}]}

season_pass_data = []

war_summary_801_data = {"galaxy_stats": {"missionsWon": 1,"missionsLost": 1,"missionTime": 1,"bugKills": 1,"automatonKills": 1,"illuminateKills": 1,"bulletsFired": 1,"bulletsHit": 1,"timePlayed": 1,"deaths": 1,"revives": 2,"friendlies": 1,"missionSuccessRate": 91,"accurracy": 100},"planets_stats": [{"planetIndex": 0,"missionsWon": 1,"missionsLost": 1,"missionTime": 1,"bugKills": 1,"automatonKills": 1,"illuminateKills": 1,"bulletsFired": 1,"bulletsHit": 1,"timePlayed": 1,"deaths": 1,"revives": 0,"friendlies": 1,"missionSuccessRate": 85,"accurracy": 100},{"planetIndex": 1,"missionsWon": 1,"missionsLost": 1,"missionTime": 1,"bugKills": 1,"automatonKills": 0,"illuminateKills": 0,"bulletsFired": 1,"bulletsHit": 1,"timePlayed": 1,"deaths": 1,"revives": 0,"friendlies": 0,"missionSuccessRate": 50,"accurracy": 100},{"planetIndex": 2,"missionsWon": 1,"missionsLost": 0,"missionTime": 1,"bugKills": 1,"automatonKills": 0,"illuminateKills": 0,"bulletsFired": 1,"bulletsHit": 0,"timePlayed": 1,"deaths": 1,"revives": 0,"friendlies": 0,"missionSuccessRate": 100,"accurracy": 0},{"planetIndex": 3,"missionsWon": 1,"missionsLost": 1,"missionTime": 1,"bugKills": 1,"automatonKills": 0,"illuminateKills": 1,"bulletsFired": 1,"bulletsHit": 1,"timePlayed": 1,"deaths": 1,"revives": 0,"friendlies": 1,"missionSuccessRate": 87,"accurracy": 100},{"planetIndex": 4,"missionsWon": 1,"missionsLost": 1,"missionTime": 1,"bugKills": 1,"automatonKills": 0,"illuminateKills": 1,"bulletsFired": 1,"bulletsHit": 1,"timePlayed": 1,"deaths": 1,"revives": 0,"friendlies": 1,"missionSuccessRate": 91,"accurracy": 100},{"planetIndex": 5,"missionsWon": 1,"missionsLost": 1,"missionTime": 1,"bugKills": 1,"automatonKills": 0,"illuminateKills": 1,"bulletsFired": 1,"bulletsHit": 1,"timePlayed": 1,"deaths": 1,"revives": 0,"friendlies": 1,"missionSuccessRate": 89,"accurracy": 100}]}

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

@app.route('/api/lobby/clear', methods=['POST'])
def lobby_clear():
    print(f"Received POST request for /api/lobby/clear")
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    print(f"Request Headers: {request.headers}")
    print(f"InfoLookup Request Data: {data}")

    return jsonify({"status": "success", "message": "Lobby clear successful"}), 200

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
    return jsonify(operations_data)

@app.route('/api/Operation/Abandon', methods=['POST'])
def operation_abandon():
    print(f"Received POST request for /api/Operation/Abandon")
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    print(f"Request Headers: {request.headers}")
    print(f"InfoLookup Request Data: {data}")

    return jsonify({"status": "success", "message": "Operation abandon successful"}), 200

@app.route('/api/Progression/ItemPackages', methods=['GET'])
def get_item_packages():
    print(f"Received GET request for /api/Progression/ItemPackages")
    print(f"Request Headers: {request.headers}")
    return jsonify(item_packages_data)

@app.route('/api/Progression/ProgressionPackages', methods=['GET'])
def get_progression_packages():
    print(f"Received GET request for /api/Progression/ProgressionPackages")
    print(f"Request Headers: {request.headers}")
    return jsonify(progression_packages_data)

@app.route('/api/Progression/items', methods=['GET'])
def get_progression_items():
    print(f"Received GET request for /api/Progression/items")
    print(f"Request Headers: {request.headers}")
    return jsonify(progression_items_data)

@app.route('/api/Progression/levelspec', methods=['GET'])
def get_level_spec():
    print(f"Received GET request for /api/Progression/levelspec")
    print(f"Request Headers: {request.headers}")
    return jsonify(level_spec_data)

@app.route('/api/Progression', methods=['GET'])
def get_progression():
    print(f"Received GET request for /api/Progression")
    print(f"Request Headers: {request.headers}")
    return jsonify(progression_data)

@app.route('/api/Progression/inventory', methods=['GET'])
def get_progression_inventory():
    print(f"Received GET request for /api/Progression/inventory")
    print(f"Request Headers: {request.headers}")
    return jsonify(progression_inventory_data)

@app.route('/api/Progression/customization', methods=['GET'])
def get_progression_customization():
    print(f"Received GET request for /api/Progression/customization")
    print(f"Request Headers: {request.headers}")
    return jsonify(progression_customization_data)

@app.route('/api/Mission/RewardEntries', methods=['GET'])
def get_reward_entries():
    print(f"Received GET request for /api/Mission/RewardEntries")
    print(f"Request Headers: {request.headers}")
    return jsonify(reward_entries_data)

@app.route('/api/SeasonPass', methods=['GET'])
def get_season_pass():
    print(f"Received GET request for /api/SeasonPass")
    print(f"Request Headers: {request.headers}")
    return jsonify(season_pass_data)


# non-requirements tests

@app.route('/api/Stats/war/801/summary', methods=['GET'])
def get_war_summary():
    print(f"Received GET request for /api/Stats/war/801/summary")
    print(f"Request Headers: {request.headers}")
    return jsonify(war_summary_801_data)

# non-requirements successes

@app.route('/api/Operation/Create', methods=['POST'])
def operation_create():
    print(f"Received POST request for /api/Operation/Create")
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    print(f"Request Headers: {request.headers}")
    print(f"InfoLookup Request Data: {data}")

    return jsonify({"status": "success", "message": "Operation create successful"}), 200

@app.route('/api/Account/ReportPosition', methods=['POST'])
def account_report_position():
    print(f"Received POST request for /api/Account/ReportPosition")
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    print(f"Request Headers: {request.headers}")
    print(f"InfoLookup Request Data: {data}")

    return jsonify({"status": "success", "message": "Report position successful"}), 200

# older requirements tests

@app.route('/api/Progression/items/discounts/801', methods=['GET'])
def get_items_discounts():
    print(f"Received GET request for /api/Progression/items/discounts/801")
    print(f"Request Headers: {request.headers}")
    return jsonify([])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=443)