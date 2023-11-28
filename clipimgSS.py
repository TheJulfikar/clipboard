import os
import time
import keyboard
from PIL import ImageGrab
import pyperclip

# Create 'Screenshots' folder if not exists
if not os.path.exists("Screenshots"):
    os.makedirs("Screenshots")

# Create 'Clipboard Images' folder if not exists
if not os.path.exists("Clipboard Images"):
    os.makedirs("Clipboard Images")

def save_screenshot(index):
    try:
        screenshot_path = f"Screenshots/screenshot_{index}.png"
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)
        print(f"Captured Screenshot. Written to {screenshot_path}")
    except Exception as e:
        print(f"Error capturing screenshot: {e}")

def save_clipboard_image(index):
    try:
        clipboard_image_path = f"Clipboard Images/clipboard_image_{index}.png"
        clipboard_image = ImageGrab.grabclipboard()
        if clipboard_image:
            clipboard_image.save(clipboard_image_path)
            print(f"Captured Clipboard Image. Written to {clipboard_image_path}")
        else:
            print("No image in clipboard.")
    except Exception as e:
        print(f"Error capturing clipboard image: {e}")

def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        save_screenshot(on_key_event.screenshot_index)
        save_clipboard_image(on_key_event.clipboard_image_index)

        on_key_event.screenshot_index += 1
        on_key_event.clipboard_image_index += 1

# Initialize the index variables
on_key_event.screenshot_index = 1
on_key_event.clipboard_image_index = 1

# Set up the keyboard hook
keyboard.hook(on_key_event)

# Run the script indefinitely
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up and exit on KeyboardInterrupt (Ctrl+C)
    keyboard.unhook_all()
