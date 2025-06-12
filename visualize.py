# visualize.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_missions(primary, flights, conflict_points=None):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot primary drone
    px = [wp['x'] for wp in primary['waypoints']]
    py = [wp['y'] for wp in primary['waypoints']]
    pz = [wp.get('z', 0) for wp in primary['waypoints']]
    pt = [wp['time'] for wp in primary['waypoints']]
    ax.plot(px, py, pt, 'bo-', label='Primary Drone')

    # Plot other drones
    for drone in flights:
        dx = [wp['x'] for wp in drone['waypoints']]
        dy = [wp['y'] for wp in drone['waypoints']]
        dz = [wp.get('z', 0) for wp in drone['waypoints']]
        dt = [wp['time'] for wp in drone['waypoints']]
        ax.plot(dx, dy, dt, '--', label=drone['drone_id'])

    # Plot conflicts
    if conflict_points:
        for point in conflict_points:
            ax.scatter(point['primary_wp']['x'], point['primary_wp']['y'], point['primary_wp']['time'], c='r', s=50, marker='x')
            ax.scatter(point['other_wp']['x'], point['other_wp']['y'], point['other_wp']['time'], c='r', s=50, marker='^')
        ax.set_title("Conflict Detected")
    else:
        ax.set_title("Conflict-Free Mission")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Time (Z axis used as Time)")
    ax.legend()
    plt.tight_layout()
    plt.savefig("output/mission_plot_4d.png")
    plt.show()

