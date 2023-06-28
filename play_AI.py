import minimax

is_limit = input('Type 1 if you want to play with a time limit: ')

if is_limit == '1':
    limit = int(input('What would you like the time limit to be (in seconds): '))
    minimax.set_max_time(limit)

depth = int(input('What depth would you like to play against: '))
minimax.set_depth(depth)

if is_limit == '1':
    minimax.play_against_user_time_limit()

else:
    minimax.play_against_user()

print('Good Game!')