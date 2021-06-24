import sys

def print_data_table(data):
    print('\n=====================================================')
    idx = 0
    for i in data:
        print('%2s'%(idx), '%15s'%(i + ':'), '%15s'%(data[i]))
        idx += 1
    print('=====================================================')

def check_data_menu(data):
    while(True):
        print_data_table(data)
        user = input('Edit numbers by entering index [0-6]. Proceed? [Y/N]: ')
        if(user == 'N' or user == 'n'):
            sys.exit('Discard readings. Exiting...')
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

def print_tweets_table(data):
    print('\n=====================================================')
    for i, val in enumerate(data):
        print('%4s'%(i), '%20s'%(val.tweet_id), '%60s'%(val.message[0:57]) + '...')
    print('=====================================================')

def check_tweets_menu(data):
    while(True):
        print_tweets_table(data)
        user = input('Select a tweet by entering index number. Enter [N] to cancel: ')
        if(user == 'N' or user == 'n'):
            sys.exit('Discard tweets. Exiting...')
        try:
            int(user)
            break
        except:
            print('Error: input must be an integer or [N/n] to cancel.')
    return data[int(user)]