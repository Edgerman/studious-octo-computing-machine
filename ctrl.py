from pynput import mouse, keyboard

def on_move(x, y):
    print(f"Pointer moved to {(x, y)}")

def on_click(x, y, button, pressed):
    print(f"{'Pressed' if pressed else 'Released'} {button.name} at {(x, y)}")

def on_scroll(x, y, dx, dy):
    print(f"Scrolled {'down' if dy < 0 else 'up'} at {(x, y)}")

def on_press(key):
    if key == keyboard.Key.esc:
        print("🛑 Esc pressed — stopping listener...")
        mouse_listener.stop()
        return False  # stop keyboard listener too
    else:
        print(key)

# Start mouse listener
mouse_listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
mouse_listener.start()

# Start keyboard listener (waits until Esc is pressed)
with keyboard.Listener(on_press=on_press) as kb_listener:
    kb_listener.join()

dsd