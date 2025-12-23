import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation

# Define the keyboard hardware configuration
class MacroPad(KMKKeyboard):
    def __init__(self):
        # Initialize the parent class
        super().__init__()
        
        # Set up the diode orientation for your button matrix
        self.diode_orientation = DiodeOrientation.COL2ROW
        
        # Define your GPIO pins for the 5 buttons based on your schematic
        # SW1-SW5 are connected to GP10, GP9, GP8, GP29, GP28
        # All buttons share a common ground rail through diodes
        self.col_pins = (board.GP10, board.GP9, board.GP8, board.GP29, board.GP28)
        self.row_pins = (board.GP13,)  # Common ground connection via diodes
        
        # Rotary encoder pins (SW6)
        # A=GP26, B=GP27, C=GP28 (center button, shared with SW5)
        self.encoder_a = board.GP26
        self.encoder_b = board.GP27
        
        # RGB LED data pin for SK6812MINI LEDs
        self.rgb_pin = board.GP7
        self.num_pixels = 2  # D1 and D2 on your board