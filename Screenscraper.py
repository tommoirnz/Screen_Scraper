# Screen scraper from a URL
# import requests
import requests as requests
from bs4 import BeautifulSoup
import os
import tkinter as tk
from tkinter import simpledialog

# Specify the URL
url = 'https://www.dailymail.co.uk/news/article-13502811/British-men-vanished-UFO-picture-sinister-men-silence-colleague-reveals-happened.html'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired data (example: all paragraphs)
paragraphs = soup.find_all('p')

# Print the text of each paragraph
for p in paragraphs:
    print(p.get_text())

# Get the user's home directory
home_dir = os.path.expanduser('~')
#
# Construct the path to the  folder. I created a folder under Downloads called screenscraper
download_dir = os.path.join(home_dir, 'Downloads\screenscraper')

# Ensure the Desktop directory exists
if not os.path.exists(download_dir):
    raise FileNotFoundError(f"The directory {download_dir} does not exist.")

# Specify the file name
# file_name = 'example.txt'
# Prompt the user to enter filename
# file_name = input("Enter your input: ")

# Create the root window
root = tk.Tk()

#root.withdraw()  # Hide the main window

# Create the input dialog
file_name = simpledialog.askstring("Input", 'Enter filename')

# Destroy the root window
root.destroy()

# Full path to the file
file_path = os.path.join(download_dir, file_name)

# Save the text to a file
with open(file_path, 'w', encoding='utf-8') as file:
    for p in paragraphs:
        file.write(p.get_text() + '\n')
