import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place

classname = {
            "BaseModel" : BaseModel,
            "User" : User,
            "Place" : Place,
            "State" : State,
            "Review" : Review,
            "Amenity" : Amenity,
            "City" : City
        }

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle EOF to exit the program"""
        return True

    def help_quit(self):
        """Help information for quit command"""
        # print("Quit command to exit the program")

    def help_EOF(self):
        """Help information for EOF command"""
        # print("EOF command to exit the program")

    def emptyline(self):
        """Do nothing on empty input line"""
        pass
    
    
    
    def do_create(self, arg):
            
            if arg:                         
                if arg in classname:
                        new_instance = classname[arg]()
                        new_instance.save()
                        print(new_instance.id)
                else:                                               # 1
                        print("** class doesn't exist **")
        
            else:                                                  # 2
                        print("** class name missing **")
                        
                        
    def do_show(self, arg):
        
        split_arg = arg.split()    

        if len(split_arg ) < 1:                          # 1
            print("** class name missing **")
        elif split_arg[0] not in classname:                    # 2
            print("** class doesn't exist **")
        elif len(split_arg ) < 2:                             # 3
            print("** instance id missing **")
        else:
            new_str = f"{split_arg[0]}.{split_arg[1]}"
            obj_sp = storage.all().get(new_str)
            if obj_sp:
                print(obj_sp)
            else:                                             # 4
                print("** no instance found **")
                
                
    def do_destroy(self, arg):
        
        split_arg = arg.split()    

        if len(split_arg ) < 1:                   # 1
            print("** class name missing **")
        elif split_arg[0] not in classname:            # 2
            print("** class doesn't exist **")
        elif len(split_arg ) < 2:                     # 3
            print("** instance id missing **")
        else:
            new_str = f"{split_arg[0]}.{split_arg[1]}"        # 4
            if new_str not in storage.all().keys():
                print("** no instance found **")
            else:
                del(storage.all()[new_str])
                storage.save()
                
    
    
    def do_all(self, arg):             ###     يحتاج تعديل في الاخراج فقط   ###
        
        if arg:
            if arg in classname:
                for key, value in storage.all().items():
                            print(str(value))
                            
            else:                                                      ## 
                            print("** class doesn't exist **")
        else:
                for key, value in storage.all().items():
                            print(str(value))
                            
                            
    def do_update(self, arg):
        
        split_arg = arg.split()
        
        if len(split_arg) < 1:   # 1
                print("** class name missing **")   
            
        elif split_arg[0] not in classname:              # 2
                print("** class doesn't exist **")
            
        elif len(split_arg) < 2:                                        # 3        
                print("** instance id missing **")

        else:                                          # 4
                new_str = f"{split_arg[0]}.{split_arg[1]}"
                if new_str not in storage.all().keys():
                    print("** no instance found **")
            
                elif len(split_arg) < 3:                      # 5
                    print("** attribute name missing **")
                                
                elif len(split_arg) < 4:                #6
                    print("** value missing **")
                        
                else:
                    setattr(storage.all()[new_str], split_arg[2], split_arg[3])
                    storage.save()
                                
                
        
        
            
            
            
            
            
            
            
            
            
                
                    
                
                
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
