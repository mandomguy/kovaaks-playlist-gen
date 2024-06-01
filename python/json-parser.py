import json

def save_scenarios_by_aim_type(scenarios_file):
    with open(scenarios_file, "r", encoding="utf-8") as f:
        all_scenarios = json.load(f)

    aim_type_scenarios = {}
    for scenario in all_scenarios:
        if "scenario" in scenario: 
            aim_type = scenario["scenario"].get("aimType")
            if aim_type is None:
                aim_type = "Other"

            scenario_data = {
                "scenarioName": scenario["scenarioName"],
            }
            aim_type_scenarios.setdefault(aim_type, []).append(scenario_data)
        else:
            print(f"Skipping scenario without 'scenario' key: {scenario}")

    output_directory = r"" 
    for aim_type, data in aim_type_scenarios.items():
        filename = f"{output_directory}\\{aim_type.lower().replace(' ', '_')}_scenarios.json"
        with open(filename, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=2)

if __name__ == "__main__":
    scenarios_file = r""
    save_scenarios_by_aim_type(scenarios_file)

    print("Scenarios parsed and saved by aim type!")
