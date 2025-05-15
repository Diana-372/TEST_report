import pytest
import main 
from unittest.mock import patch
import os 
import sys
import io

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Addons')))

def test_main_with_args():
    with patch('sys.argv', ['main.py', 'data1.csv', '--report', 'sort_payout', 'payout']):
        
        main.main()
        assert 'email' in main.all_var_list
        assert 'name' in main.all_var_list
        assert 'department' in main.all_var_list
        assert 'hours_worked' in main.all_var_list
        assert ('hourly_rate' or 'rate' or 'salary') in main.all_var_list

@pytest.fixture
def sample_data():
    empl_data_dict={'1': {'email': 'alice@example.com', 'name': 'Alice Johnson', 'department': 'Marketing', 'hours_worked': '160', 'hourly_rate': '50'}, 
                    '2': {'email': 'bob@example.com', 'name': 'Bob Smith', 'department': 'Design', 'hours_worked': '150', 'hourly_rate': '40'}, 
                    '3': {'email': 'carol@example.com', 'name': 'Carol Williams', 'department': 'Design', 'hours_worked': '170', 'hourly_rate': '60'}, 
                    '101': {'department': 'HR', 'email': 'grace@example.com', 'name': 'Grace Lee', 'hours_worked': '160', 'hourly_rate': '45'}, 
                    '102': {'department': 'Marketing', 'email': 'henry@example.com', 'name': 'Henry Martin', 'hours_worked': '150', 'hourly_rate': '35'}, 
                    '103': {'department': 'HR', 'email': 'ivy@example.com', 'name': 'Ivy Clark', 'hours_worked': '158', 'hourly_rate': '38'}, 
                    '201': {'email': 'karen@example.com', 'name': 'Karen White', 'department': 'Sales', 'hours_worked': '165', 'hourly_rate': '50'}, 
                    '202': {'email': 'liam@example.com', 'name': 'Liam Harris', 'department': 'HR', 'hours_worked': '155', 'hourly_rate': '42'}, 
                    '203': {'email': 'mia@example.com', 'name': 'Mia Young', 'department': 'Sales', 'hours_worked': '160', 'hourly_rate': '37'}}
    all_var_list = ['department', 'name', 'hours_worked', 'hourly_rate', 'Payout']
    return empl_data_dict, all_var_list

import Addons.sort_payout

@patch('builtins.print')
def test_sort_payout(mock_print, sample_data):
    text=Addons.sort_payout.payout(sample_data[0], sample_data[1])
    mock_print.assert_any_call('sorted payout table')
    
    
    for i in sample_data[0]:
        assert i in text
        assert sample_data[0][i]['name'] in text
        assert sample_data[0][i]['department'] in text
    for i in sample_data[1]:
        assert i in text

import Addons.payout

@patch('builtins.print')
def test_payout(mock_print, sample_data):
    text=Addons.sort_payout.payout(sample_data[0], sample_data[1])
    mock_print.assert_any_call('sorted payout table')
    
    
    for i in sample_data[0]:
        assert i in text
        assert sample_data[0][i]['name'] in text
        assert sample_data[0][i]['department'] in text
    for i in sample_data[1]:
        assert i in text
  
