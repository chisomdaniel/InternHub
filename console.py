#!/usr/bin/python3
''' Console application to interace directly with our database'''
import cmd
from models.internship import Internship

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
        ''' Create a new internship data in the DB'''
        args = arg.split()

        if len(args) == 0:
            print("** Parameters needed to create data not provided **")
            return False
        
        if args[0] not in tables.keys():
            print("** table does not exist **")
            print('Available tables are', tables.keys())
            return False
        

        
