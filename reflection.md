# Reflection & Justification

# Design Decisions & Architecture

The system is designed to detect **spatio-temporal conflicts** among UAVs operating in shared airspace. 

- **`mission.py`** handles core logic for conflict detection by parsing drone trajectory data from JSON files.
- **`visualize.py`** is dedicated to generating 4D visualizations where time is mapped to the z-axis in a 3D plot.
- **`test_cases/`** holds unit tests that simulate diverse operational scenarios.
- **Data separation**: Input data is structured in clearly defined JSON schemas under a `data/` folder, and output visualizations are saved in `output/`.


---

# Spatial and Temporal Checks

To detect conflicts, the system performs the following:

# Spatial Check
For every waypoint in the primary drone's mission:
- Compare the Euclidean distance to waypoints from other drones.
- Use `math.dist()` on the 3D coordinates `(x, y, z)`.

# Temporal Check
- Conflicts are only considered valid if the waypoints occur at the same timestamp.
- This is critical to differentiate near-misses from actual conflicts.

Only when both conditions are true is a **spatio-temporal conflict** reported.

---

# AI Integration

The system was developed using an iterative, AI-assisted approach with OpenAI’s ChatGPT:

- **Test Cases**: Suggested realistic and edge-case drone scenarios for unit testing.
- **Documentation**: Auto-generated scaffolding for the README and reflection documents.
- **Debugging**: Assisted in fixing logic bugs during the development phase.


---

# Testing Strategy & Edge Cases

Used `pytest` to ensure functional correctness. Test cases covered:

- Conflict when drones are spatially close and time-aligned.
- No conflict when spatial distance exceeds threshold.
- No conflict when time mismatch occurs.
- Multiple drone conflicts occurring at different timestamps.

# Edge Cases Considered

- Only one waypoint per drone.
- Identical waypoints for different drones.
- Overlapping time without spatial conflict.

This coverage ensures that the logic behaves correctly in real-world edge cases.

---

# Scalability for Real-World Deployment

To handle **tens of thousands of drones**:

# 1. **Data Ingestion**
- Replace static JSON input with a real-time stream from UAV telemetry.
- Introduce pre-processing filters to discard stale or irrelevant data.

# 2. **Visualization**
- Integrate web-based dashboards to visualize conflicts in near real-time.

This system acts as a working prototype and can scale into a production-grade airspace monitoring tool with these improvements.

 
