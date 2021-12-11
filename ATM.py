print('Welcome to Bank ATM')
restart = 'Y'
chances = 3
balance = 200000
while chances >= 0:
    pin = int(input('Please Enter Your 4 Digit Pin: '))
    if pin == 1234:
        print('\nYou Entered Your Pin Correctly\n')

        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 For Your Balance')
            print('Please Press 2 To Make a Withdrawl')
            print('Please Press 3 To Pay in')
            print('Please Press 4 To Return Card')
            option = int(input('\nWhat Would You Like To Choose ?: '))
            if option == 1:
                print('Your Balance Is $ ', balance)
                restart = input('Would You Like To Goback ?')
                if restart in ('n', 'N', 'No', 'no'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = 'y'
                Withdrawl = float(input('Enter Amount You Want To Withdraw 10,20,40,60,80,100 for '
                                        'other enter 1: ?'))
                if Withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - Withdrawl
                    print('\n Your Balance is now $ ', balance)
                    restart = input('Would You Like To Goback ?')
                    if restart in ('n', 'N', 'no', 'NO'):
                        print('Thank You')
                        break

                elif Withdrawl == 1:
                    Withdrawl = float(input('\nPlease Enter Desired Amount'))
                    balance = balance - Withdrawl
                    print('Your Balance is $ ', balance)

            elif option == 3:
                Pay_in = float(input('How Much Would You Like To Pay in ?'))
                balance = balance + Pay_in
                print('\n Your Balance is now $ ', balance)
                restart = input('Would You Like to Goback ?')
                if restart in ('n', 'N', 'no', 'NO'):
                    print('Thank You!')
                    break
            elif option == 4:
                print('Please Wait While Your Card is Returned...\n')
                print('Thank You !\n Visit Again')
                break
            else:
                print('Please Enter a Correct Number.\n')
                restart = 'y'

    elif pin != '1234':
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\n No more tries')
            break