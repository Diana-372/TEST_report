def payout(empl_data_dict, all_var_list):
    import json

    all_var_list=['email', 'name', 'department', 'hours_worked', 'hourly_rate', 'Payout']
    empl_text='  ID  |'

    for var in all_var_list:
        
        templ_empl_text=var.center(20, '_')
        empl_text=empl_text+''+templ_empl_text+'|'

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(empl_data_dict, file, ensure_ascii=False, indent=4)

    print('payout table')
    final_text = empl_text

    for empl_numb_list in empl_data_dict:

        temp=empl_data_dict[empl_numb_list]
        empl_text=f'{empl_numb_list}'.center(6)+'|'
        
        for var in all_var_list:
            
            if var!='Payout':
                if var in empl_data_dict[empl_numb_list]:
                    templ_empl_text=empl_data_dict[empl_numb_list][var].center(20, '_')

                else:
                    templ_empl_text=''.center(20, '_')

                empl_text=empl_text+''+templ_empl_text+'|'

            else:
                hw_var=int(empl_data_dict[empl_numb_list]['hours_worked'])
                hr_var=int(empl_data_dict[empl_numb_list]['hourly_rate'])
                payout=hw_var*hr_var
                templ_empl_text=str(payout).center(20, '_')
                empl_text=empl_text+''+templ_empl_text+'|'

        final_text = final_text + '\n' + empl_text
    return(final_text)



