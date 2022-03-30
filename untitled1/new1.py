
import pyray as pr
from Camera import Camera
import constants as ct
from math import atan2, sin, cos, pi

camera = Camera({
    # 'position': pr.Vector3(15, 15, 15),
    'position': pr.Vector3(10,5,0),
    'target': pr.Vector3(0,0,0),
    'up':pr.Vector3(0.0, 1.0, 0.0),
    'fovy': 60,
    'projection': pr.CAMERA_PERSPECTIVE,
    # 'mode': pr.CAMERA_FIRST_PERSON,#pr.CAMERA_FREE,#pr.CAMERA_FIRST_PERSON,
    # 'mode': pr.CAMERA_FREE
    'mode': pr.CAMERA_THIRD_PERSON
})

# SETUP
pr.init_window(ct.MAX_X, ct.MAX_Y, ct.TITLE)
pr.set_target_fps(30)
pr.disable_cursor()

# TEXTURE
model1 = pr.load_model(r'Python2022\untitled1\assets\terrain3.obj')
texture = pr.load_texture(r'Python2022\untitled1\assets\NEW_TEXTURE.png')
# model1.materials[0].maps[pr.MATERIAL_MAP_DIFFUSE].texture = texture
model1.materials[0].maps[0].texture = texture; 

# CUBE
cube1 = pr.Vector3(0,1,0)
ray = pr.Ray(cube1, pr.Vector3(0,1,0))

FLT_MAX = 340282346638528859811704183484516925440.0
FLT_MAX = 1.7976931348623157e+308
# MAIN

camera.camera.target = cube1
runOnce = False





collision = {
    'hit': False
}
grav = 0


# def collision():
angle = 0
def keyMovement():
    global angle
    angle = atan2(float(camera.camera.position.z - cube1.y), float(camera.camera.position.x - cube1.x))
    halfPI = pi
    if(pr.is_key_down(pr.KEY_A)):
        cube1.x += cos(angle)
        cube1.z -= sin(angle+halfPI)
        camera.camera.position.x += 1
    if(pr.is_key_down(pr.KEY_D)):
        cube1.x -= cos(angle)
        cube1.z += sin(angle+halfPI)
    if(pr.is_key_down(pr.KEY_W)):
        cube1.x += sin(angle)
        cube1.z -= cos(angle+halfPI)
    if(pr.is_key_down(pr.KEY_S)):
        cube1.x -= sin(angle)
        cube1.z += cos(angle+halfPI)

while not pr.window_should_close():

    keyMovement()
    pr.update_camera(camera.camera)
    ray.position = pr.Vector3(cube1.x, 1, cube1.z)

    model1Box = pr.get_model_bounding_box(model1)
    prevCube = cube1

#  BEGIN COLLISION
    grav += 0.002
    cube1.y -= grav
   
    collide = pr.get_ray_collision_box(ray, model1Box)
    if(collide.hit and collide.distance < FLT_MAX):
        modelHitInfo = pr.get_ray_collision_model(ray, model1)
        if(modelHitInfo.hit):
            grav = 0
            mhi =  modelHitInfo.point
            cube1 = pr.Vector3(mhi.x, mhi.y, mhi.z)
    else: 
        pass

    
    # BEGIN DRAWING
    camera.camera.target = cube1

    pr.begin_drawing()
    pr.begin_mode_3d(camera.camera)
    pr.draw_grid(10,1)
    pr.clear_background(pr.RAYWHITE)
    pr.draw_cube(cube1, 1.0, 1.0, 1.0, pr.RED)
    pr.draw_cube_wires(cube1, 1.0, 1.0, 1.0, pr.MAROON)
    pr.draw_ray(ray, pr.BLACK)
    pr.draw_model(model1, pr.Vector3(0,0,0), 1.0, pr.WHITE)
    pr.draw_bounding_box(model1Box, pr.BLACK)
    
    normalEnd = pr.Vector3(modelHitInfo.point.x + modelHitInfo.normal.x,    
                           modelHitInfo.point.y + modelHitInfo.normal.y,
                           modelHitInfo.point.z + modelHitInfo.normal.z)
    pr.draw_line_3d(modelHitInfo.point, normalEnd, pr.RED)
    pr.end_mode_3d()
    pr.draw_text(str(angle), 50, 50, 20, pr.VIOLET)
    pr.end_drawing()
pr.enable_cursor()
pr.close_window()

