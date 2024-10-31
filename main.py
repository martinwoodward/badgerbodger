# To learn more see https://gh.io/badger

import badger2040

display = badger2040.Badger2040()

# Set Pen to white and then clear scren
display.set_pen(15)
display.clear()

display.set_update_speed(badger2040.UPDATE_NORMAL) # 
display.set_font("sans") # Set font

# Set Pen to black
display.set_pen(0)
display.set_thickness(2)

# Write text to screen
display.text("Hello World!", 20, 40, scale=1)
display.text("With love from GitHub", 20, 80, scale=.7)

# Update the screen
display.update()
