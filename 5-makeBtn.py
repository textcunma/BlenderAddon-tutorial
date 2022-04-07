'''
ボタン作成（UI構築）
'''

import bpy                                  # bpy : Blender module
from bpy.types import Operator,Panel        # for process

# addon information
bl_info = {
    "name": "make Button",                                              # addon name
    "author": "textcunma",                                              # addon author
    "version": (1, 0),                                                  # addon version
    "blender": (3, 0, 0),                                               # Blender version
    "location": "View3D > Side bar",                                    # addon display location
    "description": "make Button and move object when push the button",  # addon description
    "warning": "",                                                      # addon warning
    "support": "TESTING",                                               # addon classification
    "wiki_url": "https://github.com/textcunma/BlenderAddon-tutorial",     # addon description (GitHub URL etc...)
    "tracker_url": "https://github.com/textcunma/BlenderAddon-tutorial",  # addon support (GitHub URL etc...)
    "category": "User Interface"                                        # addon category
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

# Create Custom Panel   : class name format  XXX_PT_YYY
class Create_PT_CustomPanel(Panel):
    bl_label = "Custom Panel"         # header
    bl_space_type = 'VIEW_3D'         # space of registring custom panel
    bl_region_type = 'UI'             # region
    bl_category ="Custom tab"         # tab name
    bl_context = "objectmode"         # context (display custom panel only when object mode)
                                      #オブジェクトモードの時のみカスタムパネルを使用

    # judge (display or undisplay)　物体が選択された場合にのみタブを表示
    @classmethod
    def poll(cls, context):
        for o in bpy.data.objects:
            if o.select_get():      # display menu only when select object
                return True
        return False

    # header design
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='PLUGIN')

    # main process for UI design
    def draw(self, context):
        layout = self.layout

        # add Button
        layout.label(text="Translation Object:")
        layout.operator(ForwardObjectZ.bl_idname, text="Translation:Z+1")
        layout.operator(BackwardObjectZ.bl_idname, text="Translation:Z-1")

classes = [
    ForwardObjectZ,
    BackwardObjectZ,
    Create_PT_CustomPanel,
]

# アドオン有効時の処理
# process when activate this addon
def register():
    for c in classes:
        bpy.utils.register_class(c)

# アドオン無効時の処理
# process when disable this addon
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()