import os
import function as f
import user_interface as us_int

clear = lambda: os.system('cls')

def run_note():
    sel_user = ''
    while sel_user != '7':
        us_int.menu()
        sel_user = input().strip()
        if sel_user == '1':
            f.print_all_notes()
        if sel_user == '2':
            f.ins_note()
        if sel_user == '3':
            f.del_note()
        if sel_user == '4':
            f.upd_note()
        if sel_user == '5':
            f.print_date_notes()
        if sel_user == '6':
            f.print_id_notes()
        if sel_user == '7':
            us_int.exit()
            break