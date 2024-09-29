from pynput.keyboard import Key, Controller
from time import sleep

# Create a keyboard controller object
keyboard = Controller()

def volumeup():
    """Simulate pressing the volume up key multiple times."""
    for _ in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)  # Sleep for 0.1 seconds between presses

def volumedown():
    """Simulate pressing the volume down key multiple times."""
    for _ in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)  # Sleep for 0.1 seconds between presses

# Test the functions
if __name__ == "__main__":
    print("Increasing volume...")
    volumeup()
    sleep(1)  # Wait for 1 second
    print("Decreasing volume...")
    volumedown()
