import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube

def download_video():
    url = url_entry.get()
    download_location = download_location_entry.get()
    
    try:
        yt = YouTube(url)
        content = quality_var.get()
        
        if content == 1:
            stream = yt.streams.get_highest_resolution()
        elif content == 3:
            stream = yt.streams.get_audio_only()
        else:
            stream = yt.streams.get_lowest_resolution()

        stream.download(output_path=download_location, filename_prefix="YouTube Video")
        messagebox.showinfo("Success", "Your video has been downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def clear_url():
    url_entry.delete(0, tk.END)

def browse_location():
    download_location = filedialog.askdirectory()
    if download_location:
        download_location_entry.delete(0, tk.END)
        download_location_entry.insert(0, download_location)

# Create main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL Entry
url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Quality Selection
quality_label = tk.Label(root, text="Select Quality:")
quality_label.grid(row=1, column=0, padx=5, pady=5)
quality_var = tk.IntVar()
quality_var.set(1)  # Default to highest resolution
quality_radio1 = tk.Radiobutton(root, text="Highest Resolution", variable=quality_var, value=1)
quality_radio1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
quality_radio2 = tk.Radiobutton(root, text="Lowest Resolution", variable=quality_var, value=2)
quality_radio2.grid(row=2, column=1, padx=5, pady=5, sticky="w")
quality_radio3 = tk.Radiobutton(root, text="Audio Only", variable=quality_var, value=3)
quality_radio3.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Download Location
download_location_label = tk.Label(root, text="Download Location:")
download_location_label.grid(row=4, column=0, padx=5, pady=5)
download_location_entry = tk.Entry(root, width=50)
download_location_entry.grid(row=4, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_location)
browse_button.grid(row=4, column=2, padx=5, pady=5)

# Download Button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=5, column=1, padx=5, pady=5)

# Clear Button
clear_button = tk.Button(root, text="Clear URL", command=clear_url)
clear_button.grid(row=0, column=2, padx=5, pady=5)

# Close Button
close_button = tk.Button(root, text="Close", command=root.quit)
close_button.grid(row=5, column=2, padx=5, pady=5)

# Start GUI
root.mainloop()
