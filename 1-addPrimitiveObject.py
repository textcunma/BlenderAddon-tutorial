'''
プリミティブオブジェクトの作成
create primitive mesh object
'''

import bpy                                                              # bpy : Blender module
from bpy.types import Operator                                          # for process

# addon info
bl_info = {
    "name": "add_primitive-object",                             # addon name
    "author": "textcunma",                                      # addon author
    "version": (1, 0),                                          # addon version
    "blender": (3, 0, 0),                                       # Blender version
    "location": "View3D > Add > Mesh > ball",                   # addon display location
    "description": "add primitive object mesh",                 # addon description
    "warning": "",                                              # addon warning
    "support": "TESTING",                                       # addon classification('COMMUNITY' or 'TESTING')
    "wiki_url": "https://github.com/textcunma/BlenderAddon-tutorial",     # addon description (GitHub URL etc...)
    "tracker_url": "https://github.com/textcunma/BlenderAddon-tutorial",  # addon support (GitHub URL etc...)
    "category": "Add Mesh"                                      # addon category
}

# オブジェクト追加するオペレータ
# adding object class (Operator class inheritance)
class AddPrimitiveBall(Operator):
    bl_idname = "mesh.primitiveball"              # ID for Blender process (!prohibit using capital letter!)
    bl_label = "ball"                           # label on menu
    bl_description = "add ball object mesh"     # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}           # process attribute
                                                #'REGISTER'     :for register menu
                                                #'UNDO'         :for return unprocess

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add(radius=2.0, location=(10.0, -10.0, 0.0), rotation=(0.0,0.0,0.0))
        return {'FINISHED'}

# menu process(!need 'context'!)
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(AddPrimitiveBall.bl_idname)

# classes for registering Blender
classes = [
    AddPrimitiveBall,
]

# アドオン有効時の処理
# process when activate this addon
def register():
    for c in classes:                               # register class
        bpy.utils.register_class(c)      
    bpy.types.VIEW3D_MT_mesh_add.append(menu_fn)    # add menu

# アドオン無効時の処理
# process when disable this addon
def unregister():
    for c in classes:                               # unregister class
        bpy.utils.unregister_class(c)    
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_fn)    # remove menu

if __name__ == "__main__":
    register()