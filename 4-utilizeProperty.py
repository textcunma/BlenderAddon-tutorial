'''
選択されたオブジェクトをXYZ軸において並行移動（プロパティを使用）
ショートカットキーの適用
'''

import bpy                                          # bpy : Blender module
from bpy.types import Operator                      # for process
from bpy.props import FloatProperty, EnumProperty   # for property

# addon information
bl_info = {
    "name": "move object using property",                               # addon name
    "author": "textcunma",                                              # addon author
    "version": (1, 0),                                                  # addon version
    "blender": (3, 0, 0),                                               # Blender version
    "location": "View3D > Object",                                      # addon display location
    "description": "move object forward and backward",                  # addon description
    "warning": "",                                                      # addon warning
    "support": "TESTING",                                               # addon classification
    "wiki_url": "https://github.com/textcunma/BlenderAddon-tutorial",     # addon description (GitHub URL etc...)
    "tracker_url": "https://github.com/textcunma/BlenderAddon-tutorial",  # addon support (GitHub URL etc...)
    "category": "Object"                                                # addon category
}

# オブジェクトを前進するクラス
# move forward object class (Operator class inheritance)
class MoveObjectXYZ(Operator):
    bl_idname = "object.forwardbackward_xyz"                                # ID for Blender process (!prohibit using capital letter!)
    bl_label = "translation-XYZ"                                            # label on menu
    bl_description = "Translational movement in XYZ-axis direction"         # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}                                       # process attribute
                                                                            #'REGISTER'     :for register menu
                                                                            #'UNDO'         :for return unprocess

    # 軸方向の決定
    # set axis
    axis: EnumProperty(
        name="axis",
        description="set axis direction",
        default='X',
        items=[
            ('X', "X-axis", "move on X-axis"),
            ('Y', "Y-axis", "move on Y-axis"),
            ('Z', "Z-axis", "move on Z-axis"),
        ]
    )

    # 移動量の決定
    # set translation amount
    amount: FloatProperty(
        name="translation amout",
        description="set translation amount",
        default=1.0,
        step=100.0,     # (1/100) * 100.0 = 1.0 <- move amount
    )

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self, context):
        active_obj = context.active_object
        if self.axis == 'X':
            active_obj.location[0] += self.amount
        elif self.axis == 'Y':
            active_obj.location[1] += self.amount
        elif self.axis == 'Z':
            active_obj.location[2] += self.amount

        self.report({'INFO'}, "{}:{} axis -> {}".format(active_obj.name, self.axis, self.amount))
        return {'FINISHED'}

# menu process(!need 'context'!)
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(MoveObjectXYZ.bl_idname)

# classes for registering Blender
classes = [
    MoveObjectXYZ,
]

# List for shortcut key
addon_keymaps = []

# register shortcut key
def registershortcut():
    kc = bpy.context.window_manager.keyconfigs.addon         # info about all keymap
    if kc:
        km = kc.keymaps.new(name="3D View", space_type='VIEW_3D')  # register key on 3D Viewport 

        kmi = km.keymap_items.new(          # shortcut key : T + Shift + Ctrl
            idname=MoveObjectXYZ.bl_idname,
            type='T',
            value='PRESS',
            shift=True,
            ctrl=True,
            alt=False)

        addon_keymaps.append((km, kmi))     # register

# unregister shortcut key
def unregistershortcut():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

# アドオン有効時の処理
# process when activate this addon
def register():
    for c in classes:                               # register class
        bpy.utils.register_class(c)      
    bpy.types.VIEW3D_MT_object.append(menu_fn)      # add menu (!change : bpy.types.VIEW3D_MT_mesh_add (addPyramid.py etc...)!)
    registershortcut()                              # register shortcut key

# アドオン無効時の処理
# process when disable this addon
def unregister():
    unregistershortcut()                            # register shortcut key
    for c in classes:                               # unregister class
        bpy.utils.unregister_class(c)    
    bpy.types.VIEW3D_MT_object.remove(menu_fn)      # add menu (!change : bpy.types.VIEW3D_MT_mesh_add (addPyramid.py etc...)!)

if __name__ == "__main__":
    register()