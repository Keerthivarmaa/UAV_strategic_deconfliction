# UAV_strategic_deconfliction

This project detects and visualizes **spatio-temporal conflicts** between drones sharing the same airspace.

# Features

- Detects spatial proximity conflicts.
- Visualizes drone trajectories and conflict points.

# Installation

1. Clone the repository:

        git clone https://github.com/your-username/uav_deconfliction.git

        cd uav_strategic_deconfliction
    
2. Create an activate virtual environment:

        python3 -m venv venv

        source venv/bin/activate

3. Install dependencies:

        pip install -r requirements.txt

# How to run

1. Check for conflicts:

        python3 mission.py

    - Reads flight data from data/primary_mission.json and data/simulated_drones.json.

    - Outputs whether a spatio-temporal conflict was detected.

    - Saves a 4D plot of all drone paths in output/mission_plot_4d.png.

# Dependencies

Listed in requirements.txt:

        numpy
        matplotlib
        pytest

# AI use reflection

This project was completed with assistance from an AI assistant (ChatGPT) for:

- Debugging spatio-temporal logic

- Generating test cases


