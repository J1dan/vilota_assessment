import numpy as np
import open3d as o3d

def create_bounding_box_wireframe(center, extents, rotations):
    # Calculate corner points of the bounding box
    l, w, h = extents
    bounding_box = np.array([
        [-l/2, -w/2, -h/2],
        [l/2, -w/2, -h/2],
        [l/2, w/2, -h/2],
        [-l/2, w/2, -h/2],
        [-l/2, -w/2, h/2],
        [l/2, -w/2, h/2],
        [l/2, w/2, h/2],
        [-l/2, w/2, h/2]
    ])

    # Apply rotation about x-axis
    rotation_x_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(rotations[0]), -np.sin(rotations[0])],
        [0, np.sin(rotations[0]), np.cos(rotations[0])]
    ])
    bounding_box_rotated_x = np.dot(rotation_x_matrix, bounding_box.T).T

    # Apply rotation about y-axis
    rotation_y_matrix = np.array([
        [np.cos(rotations[1]), 0, np.sin(rotations[1])],
        [0, 1, 0],
        [-np.sin(rotations[1]), 0, np.cos(rotations[1])]
    ])
    bounding_box_rotated_xy = np.dot(rotation_y_matrix, bounding_box_rotated_x.T).T

    # Apply rotation about z-axis
    rotation_z_matrix = np.array([
        [np.cos(rotations[2]), -np.sin(rotations[2]), 0],
        [np.sin(rotations[2]), np.cos(rotations[2]), 0],
        [0, 0, 1]
    ])
    bounding_box_rotated_xyz = np.dot(rotation_z_matrix, bounding_box_rotated_xy.T).T

    # Translate to center
    bounding_box_translated = bounding_box_rotated_xyz + center
    print(bounding_box_rotated_xyz)
    print(center)

    # Define line segments for the wireframe
    lines = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    # Create LineSet geometry
    line_set = o3d.geometry.LineSet(
        points=o3d.utility.Vector3dVector(bounding_box_translated),
        lines=o3d.utility.Vector2iVector(lines)
    )

    return line_set

def animate_bounding_box_motion(visualizer):
    # Create a bounding box
    center = np.array([0.0, 0.0, 0.0])
    extents = np.array([1, 1, 1])
    rotations = np.array([0.0, 0.0, 0.0])
    # Set initial view parameters
    # view_control = visualizer.get_view_control()
    # view_control.set_constant_z_far(1000)
    # Animate bounding box motion
    for i in range(360):
        print(i)
        # Update bounding box parameters (e.g., rotate around x, y, and z axes)
        rotations = np.radians([i, i, i])

        # Update translation
        translation = np.array([0.01, 0.01, 0.01])
        center += translation

        # Create wireframe for the updated bounding box
        line_set = create_bounding_box_wireframe(center, extents, rotations)

        # Update visualizer
        visualizer.add_geometry(line_set)
        view_ctl = visualizer.get_view_control()
        view_ctl.camera_local_translate(forward=-2, right=0, up=0)
        visualizer.poll_events()
        visualizer.update_renderer()
        # vis.remove_geometry(line_set)

# Create a visualization object and window
vis = o3d.visualization.Visualizer()
vis.create_window()

# Animate bounding box motion
animate_bounding_box_motion(vis)

# Close the visualization window
vis.destroy_window()
