import board
from digitalio import DigitalInOut, Direction, Pull
import busio
import time
import adafruit_ssd1306
import adafruit_rfm69

# Button Setup
btnA = DigitalInOut(board.D5)
btnA.direction = Direction.INPUT
btnA.pull = Pull.UP

btnB = DigitalInOut(board.D6)
btnB.direction = Direction.INPUT
btnB.pull = Pull.UP

btnC = DigitalInOut(board.D12)
btnC.direction = Direction.INPUT
btnC.pull = Pull.UP

# Create the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# 128x32 OLED Display Setup
reset_pin = DigitalInOut(board.D4)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)

# Allow display to initialize
time.sleep(1)

# Clear the display
display.fill(0)
display.show()

width = display.width
height = display.height

# RFM69 Configuration
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

while True:
    # Draw a black filled box to clear the image
    display.fill(0)

    # Attempt to set up the RFM69 Module
    try:
        rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, 915.0)
        display.text('RFM69: Detected', 0, 0, 1)
    except RuntimeError as error:
        display.text('RFM69: ERROR', 0, 0, 1)
        print('RFM69 Error:', error)

    # Check buttons
    if not btnA.value:
        display.text('Ada', width-85, height-7, 1)
        display.show()
        time.sleep(0.1)

    if not btnB.value:
        display.text('Fruit', width-75, height-7, 1)
        display.show()
        time.sleep(0.1)

    if not btnC.value:
        display.text('Radio', width-65, height-7, 1)
        display.show()
        time.sleep(0.1)

    display.show()
    time.sleep(0.1)

