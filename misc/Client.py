import bpy
bpy.data.screens["Default"].name = "Default"
#bpy.data.window_managers["WinMan"].addon_filter = 'Render'
bpy.ops.wm.addon_enable(module ='netrender')
bpy.context.scene.render.engine = 'NET_RENDER'
bpy.context.scene.network_render.mode = 'RENDER_CLIENT'
bpy.context.scene.network_render.server_address = "192.168.1.116" #cluster"10.0.10.100"
#bpy.ops.wm.save_mainfile()

bpy.ops.render.netclientanim()


