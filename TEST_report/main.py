import argparse
import os
import importlib
all_var_list = []
empl_data_dict={}
def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    try:
        parser = argparse.ArgumentParser(description='Employee Report') 
        parser.add_argument('basename', type=str, help='List the databases eg: base1.cvs data1.cvs', nargs="+") 
        parser.add_argument('--report', type=str, help='Сreate a report with the selected parameters', nargs="*", default=['payout'])
        args = parser.parse_args()
        
        
        print(args.basename)
        for database in args.basename: 
            
            text=open(database).read() 
            empl_data_list=text.split('\n')
            var_list=empl_data_list[0].split(',')
            empl_data_list.pop(0)
            id_index= var_list.index("id")
            var_list.pop(id_index)
            for numb_empl in empl_data_list:

                numb_empl=(numb_empl.split(','))
                if len(numb_empl)>1:
                    id_val=numb_empl[id_index]
                    numb_empl.pop(id_index)
                    sec_dict={}
                    i=0 
                    for var in var_list:

                        if var=='rate' or var=='salary':
                            var='hourly_rate'

                        if var not in all_var_list:
                            all_var_list.append(var)

                        sec_dict[var]=numb_empl[i]
                        i=i+1

                    empl_data_dict[id_val]=sec_dict

        for add in args.report:
            try:
                
                module = importlib.import_module(f"Addons.{add}")
                if hasattr(module, 'payout'):
                    
                    addon_function = getattr(module, 'payout')
                    print(addon_function(empl_data_dict, all_var_list))
                else:
                    print(f"Error: Module {add} does not have a function named payout")

            except ImportError:
                print(f"Error: Could not import module {add}")
            except Exception as e:
                print(f"An error occurred: {e}")

        
    except:
        print('Incorrect value or argument')
        parser.print_help()
main()