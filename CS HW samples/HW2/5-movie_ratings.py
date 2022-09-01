
def movie_ratings(movie_database, chosen_list):
    try:
        f_movie_db = open(movie_database)
        f_ch_list = open(chosen_list)
        id_chosen_list = f_ch_list.readlines()
        f_ch_list.close()

        #format ids list
        for i in range(len(id_chosen_list)):
            id_chosen_list[i] = id_chosen_list[i].replace('\n','')
        new_file = open('new_list.txt', 'w') #Output list created

        #iterate over each movie
        movie_loop(f_movie_db, id_chosen_list, new_file)

        f_movie_db.close()
        new_file.close()

    except FileNotFoundError:
        print('One of the provided files does not exist')
        try:
            f_ch_list.close()
            f_movie_db.close()
            new_file.close()
        except:
            #error might have been closing a file that was already closed, nothing to communicate
            pass
        exit()

def movie_loop(f_movie_db, id_chosen_list, new_file):
    # asume receiving headers on file and write them to new list
    movie_headers = f_movie_db.readline()
    new_file.writelines(movie_headers)

    movie = f_movie_db.readline()

    while (movie):
        # correct structure (remove \n on last column, convert to list, treat numbers as int or float accordingly)
        current_movie = movie.split(',')
        if (current_movie[2][-1::] == '\n'):
            current_movie[2] = current_movie[2][0:-1]

        # check if in desired ids list and write to new_list
        if (current_movie[0] in id_chosen_list):
            current_movie[1] = float(current_movie[1])
            current_movie[2] = int(current_movie[2])
            new_file.writelines(str(tuple(current_movie)) + '\n')

        movie = f_movie_db.readline()



#### EXECUTION ####
movie_ratings('/PATH/TO/database.csv','/PATH/TO/ids.csv')