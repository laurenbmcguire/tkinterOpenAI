from tkinter import *
from tkinter import ttk
import openai
from openai import Completion

key = "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"
openai.api_key = key

def get_completion():
    completion: Completion = openai.Completion.create(
      engine="code-davinci-002",
      prompt=textentry.get("1.0", 'end-1c'),
      temperature=0,
      max_tokens=3900,
      top_p=1,
      frequency_penalty=0.4,
      presence_penalty=0.4
    )
    
    output_text.insert(INSERT, completion.choices[0].text)
    
root = Tk()
root.title("OpenAI")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

textentry = Text(mainframe, width=30, height=10)
textentry.grid(column=2, row=1, sticky=(W, E))

output_text = Text(mainframe, width=50, height=25)
output_text.grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Get completion", command=get_completion).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Prompt:").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Completion:").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

textentry.focus()
root.bind('<Return>', get_completion)

root.mainloop()