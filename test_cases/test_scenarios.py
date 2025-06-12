import pytest
from mission import check_spatio_temporal_conflicts

def test_no_conflict_scenario():
    primary = {
        "drone_id": "primary",
        "waypoints": [
            {"x": 0, "y": 0, "z": 0, "time": 0},
            {"x": 10, "y": 10, "z": 10, "time": 10}
        ]
    }

    flights = [
        {
            "drone_id": "drone_safe_1",
            "waypoints": [
                {"x": 50, "y": 50, "z": 50, "time": 0},
                {"x": 60, "y": 60, "z": 60, "time": 10}
            ]
        }
    ]

    conflict, details = check_spatio_temporal_conflicts(primary, flights)
    assert conflict is False
    assert details == []

def test_spatial_conflict_same_time():
    primary = {
        "drone_id": "primary",
        "waypoints": [
            {"x": 10, "y": 10, "z": 10, "time": 10}
        ]
    }

    flights = [
        {
            "drone_id": "drone_conflict",
            "waypoints": [
                {"x": 11, "y": 11, "z": 10, "time": 10}
            ]
        }
    ]

    conflict, details = check_spatio_temporal_conflicts(primary, flights)
    assert conflict is True
    assert len(details) == 1
    assert details[0]['primary_wp']['time'] == 10
    assert details[0]['other_wp']['time'] == 10
 

def test_temporal_mismatch_no_conflict():
    primary = {
        "drone_id": "primary",
        "waypoints": [
            {"x": 20, "y": 20, "z": 5, "time": 50}
        ]
    }

    flights = [
        {
            "drone_id": "drone_late",
            "waypoints": [
                {"x": 20, "y": 20, "z": 5, "time": 51}
            ]
        }
    ]

    conflict, details = check_spatio_temporal_conflicts(primary, flights)
    assert conflict is False
    assert len(details) == 0

def test_exact_overlap_conflict():
    primary = {
        "drone_id": "primary",
        "waypoints": [
            {"x": 100, "y": 100, "z": 50, "time": 200}
        ]
    }

    flights = [
        {
            "drone_id": "drone_overlap",
            "waypoints": [
                {"x": 100, "y": 100, "z": 50, "time": 200}
            ]
        }
    ]

    conflict, details = check_spatio_temporal_conflicts(primary, flights)
    assert conflict is True
    assert len(details) == 1
    assert details[0]['distance'] == 0.0

