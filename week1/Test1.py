user_input = ''

open_cafe = True

while  open_cafe == True and user_input not in ['0','1']:
    user_input = input('please give me a insert ')

    if user_input == '0':
        open_cafe = False
    
    elif user_input == '1':
        print('1')
        user_input = '600'

        

    # elif user_input == '2':

    #     print('2')
    # elif user_input == '3':

    #     print('3')

    # elif user_input == '4':
    #     print('4')

