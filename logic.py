import secrets
import time 


def spin_reels():
    num_one = secrets.choice(range(1,9))
    num_two = secrets.choice(range(1,9))
    num_three = secrets.choice(range(1,9))

    result = [num_one, num_two, num_three]

    if num_one == num_two == num_three:
        message = "ДЖЕКПОТ!"
    else:
        message = "Попробуй еще раз!"
        
    return {
            "reels": result,
            "message": message,
            "win": num_one == num_two == num_three
        }
