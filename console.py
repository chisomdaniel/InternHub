#!/usr/bin/python3
''' Console application to interace directly with our database'''
import cmd
from models.internship import Internship
from models import storage

tables = {'Internship': Internship}

class Devshell(cmd.Cmd):
    ''' our console class '''
    prompt = "[Devshell] "

    def do_EOF(self, arg):
        '''Exits console at EOF'''
        return True
    
    def emptyline(self):
        ''' Custom empty line output '''
        return False
    
    def do_quit(self, arg):
        ''' Quit on quit command '''
        return True
    
    def do_create(self, arg):
        ''' Create a new internship data in the DB

        [Usage] create <model name> <space separated data and value pair>

        Ensure the value for each specified column is also specified,
        i.e everything is separated with a space
        '''
        args = arg.split()

        if len(args) == 0:
            print("** Parameters needed to create data not provided **")
            print("[Usage] update <model name> <space separated data and value pair>")
            return False
        
        if args[0] not in tables.keys():
            print("** table does not exist **")
            print('Available tables are', tables.keys())
            return False
        
        if len(args[1:]) % 2 != 0:
            print("** incomplete data passes, Ensure the value for each specified column is also specified **")
            return False
        
        new_dict = {}
        count = 0
        args2 = args[1:]
        for i in args2:
            if count % 2 == 0:
                new_dict[args2[count]] = args2[count + 1]
            count += 1
        
        print(new_dict)
        instance = tables[args[0]](**new_dict)
        print(instance.id)
    
    
    def do_show(self, arg):
        ''' Display a specific data info using its id '''
        args = arg.split()

        if len(args) <= 0:
            print("** No table specified **")
            return False
        
        if args[0] not in tables.keys():
            print("** Invalid table name spacified **")
            print('Available tables are', tables.keys())
            return False
        
        if len(args) <= 1:
            print("** Incomplete parameters **")
            print("[Usage] show <model name> <model id>")
        
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all(args[0]).keys():
            print(storage.all(args[0])[key])
        else:
            print("** Invalid id specified **")
        
        return False

    def do_all(self, arg):
        ''' Display all data '''
        args = arg.split()

        if len(args) <= 0:
            data_dict = storage.all()
        elif args[0] in tables.keys():
            data_dict = storage.all(args[0])
        else:
            print("** Invalid table name spacified **")
            print('Available tables are', tables.keys())
            return False

        for each in data_dict.values():
            print(each)
    
    def do_delete(self, arg):
        ''' Delete a model instance from database '''
        args = arg.split()

        if len(args) <= 1:
            print("** Incomplete parameters **")
            print("[Usage] delete <model name> <model id>")
            return False
        
        if args[0] not in tables.keys():
            print("** Invalid table name spacified **")
            print('Available tables are', tables.keys())
            return False
        
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all(args[0]).keys():
            storage.all(args[0])[key].delete()
        else:
            print("** Invalid id specified/model not found **")

    def do_update(self, arg):
        ''' Update the parameters of a model

        [Usage] update <model name> <model id> <space separated data and value pair>

        Ensure the value for each specified column is also specified,
        i.e everything is separated with a space
        '''
        args = arg.split()

        if len(args) <= 2:
            print("** Incomplete parameters **")
            print("[Usage] update <model name> <model id> <space separated data and value pair>")
            return False
        
        if args[0] not in tables.keys():
            print("** Invalid table name spacified **")
            print('Available tables are', tables.keys())
            return False
        
        if len(args[2:]) % 2 != 0:
            print("** incomplete data passes, Ensure the value for each specified column is also specified **")
            return False

        key = "{}.{}".format(args[0], args[1])
        if key in storage.all(args[0]).keys():
            instance = storage.all(args[0])[key]
        
            count = 0
            ignore = ['id', 'updated_at', 'created_at', '__class__', '_sa_instance_state']
            args2 = args[2:]
            for i in args[2:]:
                if i in ignore:
                    continue
                if count % 2 == 0:
                    setattr(instance, args2[count], args2[count + 1])
            
            instance.save()
        else:
            print("** No model with the id specified ")
                
if __name__ == "__main__":
    Devshell().cmdloop()
