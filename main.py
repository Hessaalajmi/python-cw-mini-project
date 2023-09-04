# write your code here
def padel_court_cost(court_type):
    if court_type == 'indoor':
        return 30
    elif court_type == 'outdoor':
        return 20
    else:
        print('Court type not valid')

def rackets_cost(racket_brand):
    if racket_brand == 'bullpadel':
        return 100
    elif racket_brand == 'nox':
       return 140
    elif racket_brand == 'siux':
       return 200
    else:
        print('Racket brand is not valid')


def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5 
    else:
        print('Number od balls is not valid')

def padel_game_cost():
    court_type = input('Enter your court type: ')
    racket_brand = input('Enter your racket brand: ')
    ball_boxes = int(input('Enter how many balls you need: '))
    game_cost = padel_court_cost(court_type) + rackets_cost(racket_brand) + padel_balls_cost(ball_boxes)
    return game_cost


print(padel_game_cost())
