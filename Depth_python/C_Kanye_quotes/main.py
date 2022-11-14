from tkinter import *
import requests

# Function


def get_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()

    data = response.json()
    canvas.itemconfig(quote_text, text=data['quote'])


    # UI
root = Tk()
root.title('Kanye Says...')
root.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r'Depth_python\C_Kanye_quetes\background.png')
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207, text='Lorem ipsum dolor sit amet', width=250, font=('Arial', 15, 'bold'))
canvas.grid(column=0, row=0)

kanye_img = PhotoImage(file=r'Depth_python\C_Kanye_quetes\kanye.png')
kanye_btn = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_btn.grid(column=0, row=1)

get_quote()


root.mainloop()
