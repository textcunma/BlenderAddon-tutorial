'''
三角錐メッシュオブジェクトの作成
create pyramid mesh object
'''

import bpy                                                              # bpy : Blender module
from bpy.types import Operator                                          # for process
from bpy.props import FloatVectorProperty                               # for vector info
from bpy_extras.object_utils import object_data_add,AddObjectHelper     # for adding object
from mathutils import Vector                                            # for vector data

# addon info
bl_info = {
    "name": "add_Pyramid",                                      # addon name
    "author": "textcunma",                                      # addon author
    "version": (1, 0),                                          # addon version
    "blender": (3, 0, 0),                                       # Blender version
    "location": "View3D > Add > Mesh > Pyramid",                # addon display location
    "description": "add Pyramid object mesh",                   # addon description
    "warning": "",                                              # addon warning
    "support": "TESTING",                                       # addon classification('COMMUNITY' or 'TESTING')
    "wiki_url": "https://github.com/textcunma/BlenderAddon-tutorial",     # addon description (GitHub URL etc...)
    "tracker_url": "https://github.com/textcunma/BlenderAddon-tutorial",  # addon support (GitHub URL etc...)
    "category": "Add Mesh"                                      # addon category
}

# add Pyramid function
def add_object(self, context):

    # get scale info
    scale_x = self.scale.x
    scale_y = self.scale.y
    scale_z = self.scale.z

    # create vertices
    verts = [
        Vector((-1 * scale_x, 1 * scale_y, 0 * scale_z)),
        Vector((1 * scale_x, 1 * scale_y, 0 * scale_z)),
        Vector((1 * scale_x, -1 * scale_y, 0 * scale_z)),
        Vector((1 * scale_x, 1 * scale_y, 1 * scale_z)),
    ]

    edges = [] # create edges(!no need for creatin faces:面生成するため不要!)                                           
    faces = [[0, 1, 2],[0, 2, 3],[0, 1, 3],[1, 2, 3]]     # create faces

    mesh = bpy.data.meshes.new(name="Pyramid")      # create new object mesh
    mesh.from_pydata(verts, edges, faces)           # register datas about vertices,edges,faces
    object_data_add(context, mesh, operator=self)   # add new object mesh

# オブジェクト追加するオペレータ
# adding object class (Operator class inheritance)
class AddPyramid(Operator,AddObjectHelper):
    bl_idname = "mesh.pyramid"                      # ID for Blender process (!prohibit using capital letter!)
    bl_label = "Pyramid"                            # label on menu
    bl_description = "add Pyramid mesh object"      # description on menu when hover mouse
    bl_options = {'REGISTER', 'UNDO'}               # process attribute
                                                    #'REGISTER'     :for register menu
                                                    #'UNDO'         :for return unprocess
                                                    
    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    #実行時に呼び出されるメイン処理
    # main process when run program
    def execute(self, context):
        add_object(self, context)
        return {'FINISHED'}

# menu process(!need 'context'!)
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(AddPyramid.bl_idname)

# classes for registering Blender
classes = [
    AddPyramid,
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


# AddObjectHelper
# https://blender.stackexchange.com/questions/205567/typeerror-mesh-ot-add-triangle-is-property-setlocation-not-found