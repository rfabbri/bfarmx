import bpy
bpy.data.screens["Default"].name = "Default"
#bpy.context.area.type = 'USER_PREFERENCES'
bpy.ops.wm.addon_enable(module ='netrender')
#bpy.ops.screen.userpref_show()
#bpy.data.window_managers["WinMan"].addon_filter = 'Render'
bpy.context.scene.render.engine = 'NET_RENDER'
bpy.context.scene.network_render.mode = 'RENDER_MASTER'
bpy.context.scene.network_render.server_address = "10.0.10.100" #cluster"10.0.10.100"
bpy.ops.render.netclientstart()
bpy.ops.render.netclientscan()

