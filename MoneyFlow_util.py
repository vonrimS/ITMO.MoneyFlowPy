
def check_user_input(options, msg):
    valid_inputs = []
    i = -1
    for key in options:
        valid_inputs.append(key)
    try:
        i = int(input(msg))
    except ValueError:
        print('...check your input')
    while i not in valid_inputs:
        try:
            print('Once again...')
            i = int(input(msg))
        except ValueError:
            print('...check your input')
    return i

def check_item_delete():
    try:
        i = int(input('Enter record number to delete: '))
    except ValueError:
        print('...check your input')
    return i

