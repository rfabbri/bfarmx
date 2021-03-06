# To run single instance with nohup
import bpy

bpy.context.scene.render.engine = 'CYCLES'

bpy.context.scene.cycles.device = 'CPU'     # make it ‘CPU’ for cpu and 'GPU' for gpu
bpy.context.scene.render.threads_mode = "AUTO"   # on the cluster, auto-detect

# Dataset-specific:
bpy.context.scene.render.resolution_percentage = 5 
bpy.context.scene.frame_start=10 
bpy.context.scene.frame_end=12
bpy.context.scene.render.filepath = "//sunset-" + str(bpy.context.scene.render.resolution_percentage) + "%-"

# Render animation
bpy.ops.render.render(animation=True)

# bpy.ops.render.render(write_still=True)
#               bpy.ops.render.netclientsendframe()
