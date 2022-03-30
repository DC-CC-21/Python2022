from pyray import *

screenWidth = int(800)
screenHeight = int(600)

init_window(screenWidth, screenHeight, "raylib [core] example - 3d camera first person");


camera = Camera3D()
camera.position = Vector3(4.0, 2.0, 4.0)
camera.target = Vector3(0.0, 1.8, 0.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 60.0
camera.projection = CAMERA_PERSPECTIVE;

heights = []
positions = []
colors = []

for i in range(10):
    heights.append(float(get_random_value(1, 12)))
    positions.append(Vector3(get_random_value(-15, 15), heights[i]/2.0, get_random_value(-15, 15)))
    colors.append(Color(get_random_value(20, 255), get_random_value(10, 55), 30, 255))


set_camera_mode(camera, CAMERA_FIRST_PERSON)

set_target_fps(60)

while not window_should_close():
    update_camera(camera)
    # camera.position.y = 10
    # camera.up = Vector3(4,10,4)
    
    begin_drawing()
    clear_background(RAYWHITE)
    begin_mode_3d(camera)

    draw_plane(Vector3(0.0, 0.0, 0.0), Vector2(32.0, 32.0), LIGHTGRAY)
    draw_cube(Vector3( -16.0, 2.5, 0.0), 1.0, 5.0, 32.0, BLUE)
    draw_cube(Vector3( 16.0, 2.5, 0.0 ), 1.0, 5.0, 32.0, LIME) 
    draw_cube(Vector3( 0.0, 2.5, 16.0 ), 32.0, 5.0, 1.0, GOLD)

    for i in range(10):
        draw_cube(positions[i], 2.0, heights[i], 2.0, colors[i]);
        draw_cube_wires(positions[i], 2.0, heights[i], 2.0, MAROON);

    end_mode_3d()
    draw_rectangle( 10, 10, 220, 70, fade(SKYBLUE, 0.5))
    draw_rectangle_lines( 10, 10, 220, 70, BLUE)

    draw_text("First person camera default controls:", 20, 20, 10, BLACK)
    draw_text("- Move with keys: W, A, S, D", 40, 40, 10, DARKGRAY)
    draw_text("- Mouse move to look around", 40, 60, 10, DARKGRAY)

    end_drawing()

close_window()     
