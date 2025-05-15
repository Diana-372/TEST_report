
def payout(empl_data_dict, all_var_list):
    all_var_list = ['department', 'name', 'hours_worked', 'hourly_rate', 'Payout']
    empl_text = '  ID  |'
    sort_list = []
    sort_dict = {}

    for empl_numb_list in empl_data_dict.items():
        if empl_numb_list[1]['department'] not in sort_list:
            sort_list.append(empl_numb_list[1]['department'])

    for var in all_var_list:
        templ_empl_text = var.center(20, '_')
        empl_text = empl_text + '' + templ_empl_text + '|'

    print('sorted payout table')

    final_text = empl_text
    for depart_var in sort_list:
        for empl_numb_list in empl_data_dict:
            if depart_var == empl_data_dict[empl_numb_list]['department']:
                temp = empl_data_dict[empl_numb_list]
                empl_text = f'{empl_numb_list}'.center(6) + '|'
                for var in all_var_list:
                    if var != 'Payout':
                        if var in empl_data_dict[empl_numb_list]:
                            templ_empl_text = empl_data_dict[empl_numb_list][var].center(20, '_')
                        else:
                            templ_empl_text = ''.center(20, '_')

                        empl_text = empl_text + '' + templ_empl_text + '|'
                    else:
                        hw_var = int(empl_data_dict[empl_numb_list]['hours_worked'])
                        hr_var = int(empl_data_dict[empl_numb_list]['hourly_rate'])
                        payout = hw_var * hr_var
                        templ_empl_text = str(payout).center(20, '_')
                        empl_text = empl_text + '' + templ_empl_text + '|'

                final_text = final_text + '\n' + empl_text
    return (final_text)

