import time
import random   #Importing Modules
import pandas as pd


random = random.randint(1, 2) #Creating variable that picks random digit. 



# Program starts from here,
print("Welcome to CTrading App")
time.sleep(1)
name=input('Enter your Name: ')
psswd = input('Set Your Pass: ')
c_psswd = input('Confirm Your Pass: ')
if c_psswd == psswd:
    print('Profile Setup Completed.')
    print('Sending Metadeta....')
    time.sleep(3)
    print('Completed.')

print('------------------')
print(name)
print('Logged In.')
wallet = 55
print('Wallet: ',wallet,'$')
print('------------------')

while True:    # Created a chart hahahaha little fun i guess.
    print('_____________________________________________________________________________')
    print(' |    |    |     |      |      |      |         |            |')
    print(' |    |    |     |      |-     |      |         |  -         |')
    print(' |    |    |     |   -  |   -  |      |      -  |     -      |')
    print(' |    |   -|     |-     |      |-     |    -    |       -    |')
    print(' |    | -  |  -  |      |      |   ---|--       |         -  |')
    print(' |   -|    |     |      |      |      |         |            |-')
    print('-|--  |    |     |      |      |      |         |            |   ---')
    print('_|____|____|_____|______|______|______|_________|____________|________________')
    print(' ')
    print(' ')
    print('[Sell]                                                        [Invest]') 
    print(' ')
    ask1 = input('Select: ').lower()
    if ask1 == 'invest':
        if wallet <= 40:
            time.sleep(1)
            print('You dont have sufficient balance in your wallet..')
            time.sleep(1)
        else:
            ask2 = int(input('How Much Do You Want to Invest? -->  '))
            if ask2 <= wallet:
                print('Select If the chart go [1] Up or [2] Down ? ')
                ask3 = int(input('Select: '))
                if ask3 == random:
                    time.sleep(2)
                    print('Trading Successfull..')
                    wallet = wallet+ask2*2
                else:
                    time.sleep(2)
                    print('Trading Unsuccessfull..')
                    wallet = wallet-ask2
            else:
                time.sleep(1)
                print('You dont have sufficient balance.')
                
    # Made a section for coins to sell... I know coins are different from real world but thats a game haha.. 
    elif ask1 == 'sell':
        print('Selling Section Selected.')
        time.sleep(2)
        print('recieving data....')
        time.sleep(2)
        coins = pd.read_csv('coins.csv')
        print(coins)
        if wallet == 200 & wallet<=500:
            time.sleep(1)
            print('Bandi Coin Available')
            ask2 = input('Wanna Sell it ? ').lower()
            if ask2 == 'yes':
                time.sleep(1)
                print('Bandi Sold Successfull..')
                wallet = wallet+400
                time.sleep(2)
            else:
                time.sleep(1)
                print('Not Selling anycoin.')            
                time.sleep(1)
        elif wallet ==500 & wallet>=500:
            time.sleep(1)
            print('Syndim Coin Available')
            ask3 = input('Wanna Sell it ? ').lower()
            if ask3 == 'yes':
                time.sleep(1)
                print('Syndim Sold Successfull...')
                wallet = wallet+1000
            else:
                time.sleep(1)
                print('Not Selling anycoin.')
                time.sleep(1)
        else:
            time.sleep(1)
            print('Not enough money...')
            time.sleep(1)
    else:
        print('Quitting!..')
        break
        
    
    
    # It Shows you your name and your current wallet   
    print('------------------')
    print(name)
    print('Wallet: ',wallet,'$')
    print('------------------')
                
            
