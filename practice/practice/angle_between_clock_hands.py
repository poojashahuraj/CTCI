"""
Hour hand: 360 degrees in 12*60 minutes. that is 0.5 degrees per minutes
Minutes hand: 360 degrees in 60 minutes. that is 6 degrees per minutes
"""



def calculate_angle_between_min_hour_hands(hour, min):
    hour_angle = (hour*60+min)*0.5
    minutes_angle = min*6
    # both these angles are from 12 o clock
    dff = abs (hour_angle - minutes_angle)
    return dff

print calculate_angle_between_min_hour_hands(3,27)