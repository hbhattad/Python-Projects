import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

# Function to download video
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    destination = filedialog.askdirectory()
    if not destination:
        messagebox.showerror("Error", "Please select a destination folder")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=destination)
        messagebox.showinfo("Success", f"Downloaded: {yt.title}\nSaved to: {destination}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {str(e)}")

# Function to exit the application
def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title('YouTube Video Downloader')

# URL entry
tk.Label(root, text='YouTube URL:').grid(row=0, column=0)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1)

# Download button
download_button = tk.Button(root, text='Download', command=download_video)
download_button.grid(row=0, column=2)

# Exit button
exit_button = tk.Button(root, text='Exit', command=exit_app)
exit_button.grid(row=1, column=2)

# Run the application
root.mainloop()
