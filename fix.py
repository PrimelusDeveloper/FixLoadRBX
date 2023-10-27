import base64
import datetime
import os
import shutil
import struct
import sys
import traceback
import zlib
from textwrap import dedent
from pathlib import Path
import sys
import traceback
import webbrowser

__socials__ = "https://discord.gg/Qeq5ahR8Uh"

def open_roblox_webclient():
    url = "https://www.roblox.com"
    print("Opening Roblox Webclient. Please check your browser.")
    webbrowser.open_new(url)

def main():
    username = os.getlogin()
    print(f'Welcome, {username}. Press "Enter" to open Roblox Webclient')
    print('By the way, it is still in beta. If you encounter any bugs or errors, contact Primelus#3979')
    
    user_input = input()
    if not user_input:
        open_roblox_webclient()
        input('Done! Successfully opened the Webclient!')
    else:
        print("Invalid input. Exiting.")
        
    print(f"Socials: {__socials__}\n")
    
if __name__ == '__main__':
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        pass
    except Exception as err:
        print('Oops, something went wrong...')
        print(f'Error message: {err}')