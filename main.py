from kb import MacroPad
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes


keyboard = MacroPad()

# Add media keys extension for volume and media controls
keyboard.extensions.append(MediaKeys())


rgb = RGB(
    pixel_pin=keyboard.rgb_pin,  # Data pin from kb.py
    num_pixels=keyboard.num_pixels, 
    animation_mode=AnimationModes.BREATHING_RAINBOW, 
    brightness=0.3, 
    brightness_step=0.05, 
    brightness_limit=0.8, 
    animation_speed=2, 
)
keyboard.extensions.append(rgb)

# Set up the rotary encoder module
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)


encoder_handler.pins = (
    (keyboard.encoder_a, keyboard.encoder_b, None),  # (Pin A, Pin B, Button Pin)
)

# Map encoder rotation to volume up/down
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),  # Clockwise = Volume Up, Counter-clockwise = Volume Down
]


keyboard.keymap = [
    [
        # Button 1 (SW1 - GP10): Copy
        KC.LGUI(KC.C),
        
        # Button 2 (SW2 - GP9): Paste
        KC.LGUI(KC.V),
        
        # Button 3 (SW3 - GP8): Undo
        KC.LGUI(KC.Z),
        
        # Button 4 (SW4 - GP29): Play/Pause media
        KC.MEDIA_PLAY_PAUSE,
        
        # Button 5 (SW5 - GP28): Mute/Unmute audio
        KC.MUTE,
    ]
]


if __name__ == '__main__':
    keyboard.go()