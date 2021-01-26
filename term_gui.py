import signal
from blessed import Terminal

term = Terminal()

def on_resize(sig, action):
    print(f'height={term.height}, width={term.width}')

signal.signal(signal.SIGWINCH, on_resize)

# wait for keypress
term.inkey()