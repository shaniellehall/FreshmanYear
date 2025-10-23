#Program HW02_projectile.py
#Name : Shanielle Hall
#Date : April 8, 2025
#Purpose : Write a program that asks the user to enter the launch angle and velocity, and a distance
#          along the trajectory. The program then calculates and displays the height y of the
#          projectile at a distance x.

import math

def calculateProjectileMotion(theta, speed, distance):
    g = 9.81 #Gravity
    theta = math.radians(theta)
    
    topPart = g * (distance ** 2) #numerator
    bottomPart = 2.0 * (speed ** 2) * (math.cos(theta) ** 2) #denominator
    fraction = topPart / bottomPart
    trajectory = distance * math.tan(theta) - fraction
    
    rounded_trajectory = round(trajectory, 2)
    
    print("The height of this projectile at a distance of", distance, "meters along its trajectory is", rounded_trajectory , "meters")

if __name__ == "__main__":
    launch_angle = int(input("Enter launch angle in degrees: "))
    launch_velocity = int(input("Enter launch velocity in meters per second: "))
    launch_distance = int(input("Enter distance in meters: "))
    
    calculateProjectileMotion(launch_angle, launch_velocity, launch_distance) 