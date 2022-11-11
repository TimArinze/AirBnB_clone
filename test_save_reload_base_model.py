#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print('Type of all_objs is {}'.format(type(all_objs)))
print(all_objs)

print('\n\n')

print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    cls_name = obj_id.split('.')[0]
    if cls_name == 'BaseModel':
        obj = all_objs[obj_id]
        print(obj)

print('\n\n')

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
