'''
選択されたオブジェクトをZ軸において並行移動
'''

import bpy                          # bpy : Blender module
from bpy.types import Operator      # for process

# addon information
bl_info = {
    "name": "move object",                                              # addon name
    "author": "textcunma",                                              # addon author
    "version": (1, 0),                                                  # addon version
    "blender": (3, 0, 0),                                               # Blender version
    "location": "View3D > Object",                                      # addon display location
    "description": "move object forward and backward on Z-axis ",       # addon description
    "warning": "",                                                      # addon warning
    "support": "TESTING",                                               # addon classification
    "wiki_url": "https://github.com/textcunma/BlenderAddon-tutorial",     # addon description (GitHub URL etc...)
    "tracker_url": "https://github.com/textcunma/BlenderAddon-tutorial",  # addon support (GitHub URL etc...)
    "category": "Object"                                                # addon category
}

# オブジェクトを前進するクラス
# move forward object class (Operator class inheritance)
class ForwardObjectZ(Operator):
    bl_idname = "object.forward_z_1"                                        # ID for Blender process (!prohibit using capital letter!)
    bl_label = "+1 on Z-axis"                                               # label on menu
    bl_description = "Translational movement in forward Z-axis direction"   # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                       # process attribute
                                                                            #'REGISTER'     :for register menu
                                                                            #'UNDO'         :for return unprocess

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self, context):
        active_obj = context.active_object
        active_obj.location[2] += 1.0       #X:location[0] Y:location[1] Z:location[2]
        return {'FINISHED'}

# オブジェクトを後進するクラス
# move backward object class (Operator class inheritance)
class BackwardObjectZ(Operator):
    bl_idname = "object.backward_z_1"                                           # ID for Blender process (!prohibit using capital letter!)
    bl_label = "-1 on Z-axis"                                                   # label on menu
    bl_description = "Translational movement in backward Z-axis direction"      # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                           # process attribute
                                                                                #'REGISTER'     :for register menu
                                                                                #'UNDO'         :for return unprocess

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self, context):
        active_obj = context.active_object
        active_obj.location[2] -= 1.0       #X:location[0] Y:location[1] Z:location[2]
        return {'FINISHED'}

# menu process(!need 'context'!)
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(ForwardObjectZ.bl_idname)
    self.layout.operator(BackwardObjectZ.bl_idname)

# classes for registering Blender
classes = [
    ForwardObjectZ,
    BackwardObjectZ,
]

# アドオン有効時の処理
# process when activate this addon
def register():
    for c in classes:                               # register class
        bpy.utils.register_class(c)      
    bpy.types.VIEW3D_MT_object.append(menu_fn)      # add menu (!change : bpy.types.VIEW3D_MT_mesh_add (addPyramid.py etc...)!)

# アドオン無効時の処理
# process when disable this addon
def unregister():
    for c in classes:                               # unregister class
        bpy.utils.unregister_class(c)    
    bpy.types.VIEW3D_MT_object.append(menu_fn)      # add menu (!change : bpy.types.VIEW3D_MT_mesh_add (addPyramid.py etc...)!)

if __name__ == "__main__":
    register()