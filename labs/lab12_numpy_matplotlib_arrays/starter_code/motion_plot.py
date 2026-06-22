import numpy as np
import matplotlib.pyplot as plt

def position(t, x0, v0, a):
    return x0 +v0*t+0.5*a*(t*t)

def velocity(t, v0, a):
    return v0 + a * t

def main():
    # Consider a projectile launched at a speed of 50 m/s and an angle of 45 degrees.
    #
    # Goal: create plots of x vs. t, y vs. t, v_x vs. t, and v_y vs. t
    #       for 0 < t < 10 seconds
    #
    # TODO: create time array using np.linspace
    # TODO: compute position and velocity arrays
    # TODO: make and save plots
    time=np.linspace(0,5,1000)
    speed = 50
    angle = 30
    a = -9.805
    v0x = speed * np.cos(angle * np.pi / 180)
    v0y = speed * np.sin(angle * np.pi / 180)
    xpos = position(time, 0, v0x, 0)
    ypos = position(time, 0, v0y, a)
    xvel = velocity(time, v0x, 0)
    yvel = velocity(time, v0y, a)



    fig, ax = plt.subplots(2,2)
    ax[0,0].plot(time, xpos, label='x position')
    ax[0,0].set_xlabel('time')
    ax[0,0].set_ylabel('velocity')
    ax[0,1].plot(time, ypos, label='y velocity')
    ax[0,1].set_xlabel('time')
    ax[0,1].set_ylabel('velocity')
    ax[1,0].plot(time, xvel, label='x velocity')
    ax[1,0].set_xlabel('time')
    ax[1,0].set_ylabel('velocity')
    ax[1,1].plot(time, yvel, label='y velocity')
    ax[1,1].set_xlabel('time')
    ax[1,1].set_ylabel('velocity')
    plt.tight_layout(pad=2.0, w_pad=1.5, h_pad=1.5)
    plt.show()


main()
#Commit 1: Add NumPy array calculations
#Commit 2: Add position plot
#Commit 3: Add velocity plot
#Commit 4: Save plots and cleanup