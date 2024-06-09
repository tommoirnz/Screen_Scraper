#Screen Scraper
#T.J.Moir June 2024
# You must create a directory under Downloads called screenscraper
import requests
import winsound
from bs4 import BeautifulSoup
import os
import tkinter as tk
from tkinter import simpledialog
from gtts import gTTS
import shutil

# Beep sound parameters
frequency = 500  # Frequency in Hertz
duration = 500  # Duration in ms

# Create the root window
root = tk.Tk()
root.geometry('500x200+1200+500')
root.title("Screen Scraper")

# Create a StringVar to associate with the label
text_var = tk.StringVar()
text_var.set("Screen Scraper")

# Create the label widget
label = tk.Label(root,
                 textvariable=text_var,
                 anchor=tk.CENTER,
                 bg="white",
                 height=2,
                 width=50,
                 bd=3,
                 font=("Times", 12, "bold"),
                 cursor="hand2",
                 fg="grey",
                 padx=15,
                 pady=15,
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                 wraplength=250)
label.pack(pady=20)



# Function to handle screen scraping and audio conversion
def screen_scrape():
    winsound.Beep(frequency, duration)
    url = simpledialog.askstring("Input", "URL for screenscrape")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    home_dir = os.path.expanduser('~')
    text_var.set("Please wait, doing audio first")
    text = ""
    for p in paragraphs:
        text += p.get_text()
    tts = gTTS(text, lang='en-uk')
    download_dir = os.path.join(home_dir, 'Downloads', 'screenscraper')
    if not os.path.exists(download_dir):
        raise FileNotFoundError(f"The directory {download_dir} does not exist.")
    winsound.Beep(frequency, duration)
    mp3_name = simpledialog.askstring("Input", "Enter .mp3 filename:")
    tts.save(mp3_name)
    shutil.move(mp3_name, download_dir)
    text_var.set("Finished audio part")
    winsound.Beep(frequency, duration)
    file_name = simpledialog.askstring("Input", "Enter filename:")
    root.destroy()
    file_path = os.path.join(download_dir, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        for p in paragraphs:
            file.write(p.get_text() + '\n')

# Create the screen scrape button
screen_scrape_btn = tk.Button(root, text="Screen Scrape", command=screen_scrape)
screen_scrape_btn.pack(pady=10)
screen_scrape_btn.place(x=200, y=150)

root.mainloop()
