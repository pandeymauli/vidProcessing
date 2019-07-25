## Goal : Generate forefinger saccades for audio and Braille

# First get the coordinates of the box
# Next, look at the location of aruco markers
#   Red dot where the marker is (outside and inside the box)
# Merge the files

# Limitations :
# What is the hand is in the air?
# I can go through each frame and decide if the marker should be 'counted'
# Code for that :
    # Display frame : Grey and RGB
    # I press 1 for counting marker 1, 2 for counting marker 2, 4 for counting both, 0 for counting none
    # *In cases marker not detected, log the frame name, and make a copy in a different folder

# *Will think of a way to tackle this
