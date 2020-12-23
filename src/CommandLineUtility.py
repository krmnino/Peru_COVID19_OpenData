def print_table(data):
    print('=====================================================')
    idx = 0
    for i in data:
        print('%2s'%(idx), '%15s'%(i + ':'), '%15s'%(data[i]))
        idx += 1
    print('=====================================================')

def check_data_menu(data):
    while(True):
        print_table(data)
        user = input('Edit numbers by entering index [0-6]. Proceed? [Y/N]: ')
        if(user == 'N' or user == 'n'):
            return 1
        elif (user == 'Y' or user == 'y'):
            return 0
        elif(user == '0'):
            data_keys = list(data.keys())
            data[data_keys[int(user)]] = input(data_keys[int(user)] + ': ')
            continue
        elif(user == '1' or user == '2' or user == '3' or user == '4' or user == '5' or user == '6'):
            data_keys = list(data.keys())
            new_data = input(data_keys[int(user)] + ': ')
            if(new_data == 'N' or new_data == 'n'):
                print('Skip edit.')
                continue
            try:
                int(new_data)
            except:
                print('Error: input must be an integer or [N/n] to skip.')
                continue
            print(data[data_keys[int(user)]])
            data[data_keys[int(user)]] = new_data
            continue
        else:
            print('Wrong input. Try Again.')
            continue