data = [
    {
        'nume': 'George',
        'filme': ['Shrek', 'Bond', 'Fight Club']
    },
    {
        'nume': 'Cristian',
        'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']
    },
    {
        'nume': 'Stefan',
        'filme': ['Fight Club', 'Slumdog Millionaire']
    }
]

#Cel mai vizionat film

movie_count = {}

for person_data in data:
    for movie in person_data['filme']:
        if movie in movie_count:
            movie_count[movie] += 1
        else:
            movie_count[movie] = 1

most_watched_movie = max(movie_count, key=movie_count.get)

print("The most watched movie is:", most_watched_movie)



#Utilizatorul cu cele mai multe filme vizionate
user_movie_count = {}

for person_data in data:
    user_name = person_data['nume']
    num_movies_watched = len(person_data['filme'])
    user_movie_count[user_name] = num_movies_watched


most_movies_watched_user = max(user_movie_count, key=user_movie_count.get)


print("Utilizatorul cu cele mai multe filme vizionate este:", most_movies_watched_user)


#Top utilizatori cu cele mai multe filme vizionate


user_movie_count = {}


for person_data in data:
    user_name = person_data['nume']
    num_movies_watched = len(person_data['filme'])
    user_movie_count[user_name] = num_movies_watched

# Tupple
user_movie_count_list = [(user, count) for user, count in user_movie_count.items()]

# Sortarea listei max-min
user_movie_count_list.sort(key=lambda x: x[1], reverse=True)

print("Top utilizatori cu cele mai multe filme vizionate :")
for user, count in user_movie_count_list:
    print(f"{user}: {count} filme")


#Top filme dupa vizionari:
movie_count = {}


for person_data in data:
    for movie in person_data['filme']:
        if movie in movie_count:
            movie_count[movie] += 1
        else:
            movie_count[movie] = 1

# Tupple
movie_count_list = [(movie, count) for movie, count in movie_count.items()]

# Sortare tupple
movie_count_list.sort(key=lambda x: x[1], reverse=True)

# Print the sorted list
print("Top filme dupa vizionari:")
for movie, count in movie_count_list:
    if movie_count[movie] == 1:
        print(f"{movie}: o vizionare")
    else:
        print(f"{movie}: {count} ori")


