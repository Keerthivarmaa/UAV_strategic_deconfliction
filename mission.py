# mission.py
import json
import math
from typing import List, Dict, Tuple
from visualize import plot_missions

SAFETY_DISTANCE = 5.0  # meters

def load_mission(file_path: str) -> Dict:
    with open(file_path, 'r') as f:
        return json.load(f)

def euclidean_distance(p1: Dict, p2: Dict) -> float:
    return math.sqrt((p1['x'] - p2['x']) ** 2 + (p1['y'] - p2['y']) ** 2 + (p1['z'] - p2['z']) ** 2)

def check_spatio_temporal_conflicts(primary_mission: Dict, flights: List[Dict]) -> Tuple[bool, List[Dict]]:
    conflicts = []
    primary_wp = primary_mission['waypoints']

    for flight in flights:
        for wp1 in primary_wp:
            for wp2 in flight['waypoints']:
                if abs(wp1['time'] - wp2['time']) < 1e-2:
                    dist = euclidean_distance(wp1, wp2)
                    if dist < SAFETY_DISTANCE:
                        conflicts.append({
                            "conflict_time": wp1['time'],
                            "primary_wp": wp1,
                            "other_drone": flight['drone_id'],
                            "other_wp": wp2,
                            "distance": dist
                        })
    return (len(conflicts) > 0), conflicts

def check_mission(primary_file: str, flights_file: str) -> None:
    primary_mission = load_mission(primary_file)
    flights = load_mission(flights_file)['flights']

    conflict, details = check_spatio_temporal_conflicts(primary_mission, flights)

    if not conflict:
        print("\u2705 Mission Status: CLEAR - No conflicts detected.")
    else:
        print("\u274C Mission Status: CONFLICT DETECTED")
        for d in details:
            print(f"\n\u26D4 Conflict at time {d['conflict_time']}s:")
            print(f"   → Primary WP: {d['primary_wp']}")
            print(f"   → Other Drone: {d['other_drone']} at WP {d['other_wp']}")
            print(f"   → Distance: {d['distance']:.2f} m")

    plot_missions(primary_mission, flights, details if conflict else None)

if __name__ == "__main__":
    check_mission("data/primary_mission.json", "data/simulated_drones.json")

