import bpy
bpy.data.screens["Default"].name = "Default"
bpy.ops.wm.addon_enable(module ='netrender')
#bpy.data.window_managers["WinMan"].addon_filter = 'Render'
bpy.context.scene.render.engine = 'NET_RENDER'
bpy.context.scene.network_render.mode = 'RENDER_SLAVE'
bpy.context.scene.network_render.server_address = "10.0.10.100" #cluster"10.0.10.100"
bpy.ops.render.netclientstart()
