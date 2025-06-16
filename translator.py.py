import asyncio
from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES, Translator

# Async translate function
async def async_translate(text, src_lang, dest_lang):
    translator = Translator()
    translation = await translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

# Translate button function
def translate_text():
    src_lang = comb_sor.get()
    dest_lang = comb_dest.get()
    text = src_txt.get(1.0, END).strip()

    if not text:
        return

    # Get the language keys from names
    lang_dict = {v: k for k, v in LANGUAGES.items()}
    src_key = lang_dict.get(src_lang.lower(), 'en')
    dest_key = lang_dict.get(dest_lang.lower(), 'en')

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    translated = loop.run_until_complete(async_translate(text, src_key, dest_key))
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, translated)

# GUI Setup
root = Tk()
root.title("Translator")
root.geometry("600x600")
root.configure(bg="white")

# Title
Label(root, text="🌐 Translator App", font=("Arial", 25, "bold"), bg="white").pack(pady=10)

# Source Text Area
Label(root, text="Enter Text:", font=("Arial", 12, "bold"), bg="white").pack()
src_txt = Text(root, font=("Arial", 12), height=6, width=60, wrap=WORD)
src_txt.pack(pady=5)

# Dropdowns for Language Selection
frame = Frame(root, bg="white")
frame.pack(pady=10)

lang_list = list(LANGUAGES.values())

Label(frame, text="From", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, padx=5)
comb_sor = ttk.Combobox(frame, values=lang_list, state='readonly', width=25)
comb_sor.grid(row=0, column=1, padx=5)
comb_sor.set("english")

Label(frame, text="To", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=2, padx=5)
comb_dest = ttk.Combobox(frame, values=lang_list, state='readonly', width=25)
comb_dest.grid(row=0, column=3, padx=5)
comb_dest.set("hindi")

# Translate Button
Button(root, text="Translate", font=("Arial", 12, "bold"), command=translate_text, bg="blue", fg="white").pack(pady=10)

# Destination Text Area
Label(root, text="Translated Text:", font=("Arial", 12, "bold"), bg="white").pack()
dest_txt = Text(root, font=("Arial", 12), height=6, width=60, wrap=WORD)
dest_txt.pack(pady=5)

root.mainloop()



