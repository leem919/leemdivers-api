from flask import Flask, request, jsonify, make_response
import json
import os
from datetime import datetime, timezone

app = Flask(__name__)

# load data

data_dir = os.path.join(os.path.dirname(__file__), "data")

def load_json(filename):
    path = os.path.join(data_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

game_client_config_data = load_json("GameClientConfig.json")

war_info_data = load_json("WarInfo.json")

galactic_war_effects_data = load_json("GalacticWarEffects.json")

news_ticker_data = load_json("NewsTicker.json")

war_assignment_data = load_json("WarAssignment.json")

war_status_data = load_json("WarStatus.json")

operation_data = load_json("Operation.json")

item_packages_data = load_json("ItemPackages.json")

progression_packages_data = load_json("ProgressionPackages.json")

progression_items_data = load_json("ProgressionItems.json")

level_spec_data = load_json("LevelSpec.json")

progression_data = load_json("Progression.json")

progression_inventory_data = load_json("ProgressionInventory.json")

reward_entries_data = load_json ("RewardEntries.json")

season_pass_data = load_json("SeasonPass.json")

news_feed_data = load_json("NewsFeed.json")

# create required endpoints

@app.route('/api/Configuration/GameClient', methods=['GET'])
def get_game_configuration():
    return jsonify(game_client_config_data)

@app.route('/api/Account/Login', methods=['POST'])
def account_login():
    data = request.get_json()

    return jsonify({"status": "success"}), 200

@app.route('/api/WarSeason/current/WarId', methods=['GET'])
def war_id():
    return jsonify({"id": 801})

@app.route('/api/WarSeason/801/warinfo', methods=['GET'])
def get_war_info_801():
    return jsonify(war_info_data)

@app.route('/api/WarSeason/801/timeSinceStart', methods=['GET'])
def get_time_since_war_start():
    start_time_str = "2024-01-23 12:05:13"
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)

    current_time = datetime.now(timezone.utc)

    time_difference = current_time - start_time

    seconds_since_start = int(time_difference.total_seconds())

    return jsonify({"secondsSinceStart": seconds_since_start})

@app.route('/api/WarSeason/GalacticWarEffects', methods=['GET'])
def get_galactic_war_effects():
    return jsonify(galactic_war_effects_data)

@app.route('/api/WarSeason/NewsTicker', methods=['GET'])
def get_news_ticker():
    return jsonify(news_ticker_data)

@app.route('/api/v2/Assignment/War/801', methods=['GET'])
def get_assignment_war_801():
    return jsonify(war_assignment_data)

@app.route('/api/WarSeason/801/Status', methods=['GET'])
def get_war_status_801():
    return jsonify(war_status_data)

@app.route('/api/NewsFeed/801', methods=['GET'])
def get_news_feed_801():
    return jsonify(news_feed_data)

@app.route('/api/Operation', methods=['GET'])
def get_operation_ids():
    return jsonify(operation_data)

@app.route('/api/Progression/ItemPackages', methods=['GET'])
def get_item_packages():
    return jsonify(item_packages_data)

@app.route('/api/Progression/ProgressionPackages', methods=['GET'])
def get_progression_packages():
    return jsonify(progression_packages_data)

@app.route('/api/Progression/items', methods=['GET'])
def get_progression_items():
    return jsonify(progression_items_data)

@app.route('/api/Progression/levelspec', methods=['GET'])
def get_level_spec():
    return jsonify(level_spec_data)

@app.route('/api/Progression', methods=['GET'])
def get_progression():
    return jsonify(progression_data)

@app.route('/api/Progression/inventory', methods=['GET'])
def get_progression_inventory():
    return jsonify(progression_inventory_data)

@app.route('/api/Progression/customization', methods=['GET'])
def get_progression_customization():
    return jsonify({})

@app.route('/api/Mission/RewardEntries', methods=['GET'])
def get_reward_entries():
    return jsonify(reward_entries_data)

@app.route('/api/SeasonPass', methods=['GET'])
def get_season_pass():
    return jsonify(season_pass_data)

# older endpoint test

@app.route('/api/Progression/items/discounts/801', methods=['GET'])
def get_items_discounts():
    return jsonify([])

# browser result

@app.route('/', methods=['GET'])
def generic_message():
    return jsonify({"message": "darkfluid-api running on this host"})
