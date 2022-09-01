

def text_decoder(text_file, key_file):
    try:
        #open key_file and create two lists one from left-most letters & one from right most letters
        list_key, list_value = prepara_validate_key(key_file)

        with open(text_file) as cf:
            #capitalize letters for comparison to lists and iterate over each
            char = cf.read(1)
            while( char ):
                # find index of matching letter in key_list, use the same index in value_list to decode.
                if char.upper() in list_key:
                    match = list_key.index(char.upper())
                    #Print char in its original CASE.
                    if ( char.isupper() ):
                        print(list_value[match], end='')
                    else:
                        print(list_value[match].lower(), end='')
                # print punctuation and whitespaces since they will not be found in the key_list
                elif ( char in [' ',',','.'] ):
                    print(char, end='')
                #use * for unknown characters
                else:
                    print('*', end='')
                char = cf.read(1)

    except FileNotFoundError:
        print('One of the provided files does not exist')
        exit()



def prepara_validate_key(key_file):
    list_key, list_value = [], []
    with open(key_file) as kf:
        for line in kf:
            (key, value) = map(str, line.rstrip().split(":"))
            list_key.append(key)
            list_value.append(value)
        # check that key is valid (every letter appears only once in both lists
        for e in list_key:
            if list_key.count(e) > 1:
                print(e + " appears more than once in list_key")
                exit()
        for e in list_value:
            if list_value.count(e) > 1:
                print(e + " appears more than once in list_value")
                exit()

    return list_key, list_value


#### EXECUTION ####
text_decoder('cipher.txt', 'key.txt')




