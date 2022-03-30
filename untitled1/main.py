import pyray as pr
from raylib import BeginMode2D, BeginMode3D, CloseWindow, DrawCube, DrawCubeWires, DrawGrid, EndMode3D

screenWidth = int(800)
screenHeight = int(450)

pr.init_window(screenWidth, screenHeight, "raylib [core] example - 3d camera free")

camera = pr.Camera3D()
camera.position = pr.Vector3(10.0, 0.0,  10.0)
camera.target = pr.Vector3(0.0, 0.0, 0.0)
camera.up = pr.Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = pr.CAMERA_PERSPECTIVE

cubePosition = pr.Vector3(0.0, 0.0, 0.0)
cubeScreenPosition = pr.Vector2(0.0, 0.0)

pr.set_camera_mode(camera, pr.CAMERA_FREE)#pr.CAMERA_FIRST_PERSON)

pr.set_target_fps(60)

while (not pr.window_should_close()):
    pr.update_camera(camera)

    cubeScreenPosition = pr.get_world_to_screen(pr.Vector3(cubePosition.x, cubePosition.y + 2.5, cubePosition.z), camera)
    pr.begin_drawing()

    pr.clear_background(pr.RAYWHITE)
    pr.begin_mode_3d(camera)

    pr.draw_cube(cubePosition, 2.0, 2.0, 2.0, pr.RED)
    pr.draw_cube_wires(cubePosition, 2.0, 2.0, 2.0, pr.MAROON)
    pr.draw_grid(10, 1.0)

    pr.end_mode_3d()

    pr.draw_text("Enemy: 100 / 100", int(cubeScreenPosition.x - pr.measure_text("Enemy: 100/100", 20)/2), int(cubeScreenPosition.y), 20, pr.BLACK)
    pr.draw_text("Text is always on top of the cube", int((screenWidth - pr.measure_text("Text is always on top of the cube", 20))/2), 25, 20, pr.GRAY)
    pr.end_drawing()

pr.close_window()
