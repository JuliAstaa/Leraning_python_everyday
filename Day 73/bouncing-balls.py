""" 
A child is playing with a ball on the nth floor of a tall building. The height od this floor is above ground level, h, is known.

He drops the ball out of the window. The ball bounces, to two-third of its height

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in from of her window(include when it's falling and bouncing)?

Three condition must met for a valid experiment:
    - Float parameter 'h' is meters must be greater than 0
    - Float parameter 'bounce' must be greater than 0 and less than 1
    - Float parameter 'window' must less than h

if all three conditions above are fullfilled, return positive integer, otherwise return -1

Note:
the ball can onlu be seem if the height of the rebounding ball is strictlu greater than the window parameter


Example:
input: h = 3, bounce = 0.66, window = 1.5
output: 3

input: h = 3, bounce = 1, window = 1.5
output: 0

"""

def bouncing_ball(h: float, bounce: float, window: float) -> int:
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h: return -1
    bouncing_ball_total = 0
    while True:
        bouncing_ball_total += 1
        h = h * bounce
        if h <= window:
            break
        bouncing_ball_total += 1
       

    return bouncing_ball_total


print(bouncing_ball(3, 0.66, 1.5))