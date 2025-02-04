import pyperclip

def copy_to_clipboard(text):
    """Copy the given text to the clipboard."""
    pyperclip.copy(text)

def paste_from_clipboard():
    """Paste the text from the clipboard."""
    return pyperclip.paste()
