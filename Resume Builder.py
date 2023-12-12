import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
import os

FONT_TITLE = ("Helvetica", 20, "bold")
FONT_LABEL = ("Helvetica", 12)
FONT_BUTTON = ("Helvetica", 12, "bold")
COLOR_BG = "#f2f2f2"


def submit_form():
    name = entry_vars[0].get()
    number = entry_vars[1].get()
    email = entry_vars[2].get()
    qualification = entry_vars[3].get()
    skills = entry_vars[4].get()


    if not name or not number or not email or not qualification or not skills:
        messagebox.showerror("Error", "Please fill in all the fields.")
        return


    if not selected_photo:
        messagebox.showerror("Error", "Please select a photo.")
        return


    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    generate_portfolio_pdf(file_path, name, number, email, qualification, skills, selected_photo)
    messagebox.showinfo("Success", f"Portfolio created successfully.\nPDF saved at {file_path}")

    app.destroy() 

def generate_portfolio_pdf(filename, name, number, email, qualification, skills, photo_filename):
    c = canvas.Canvas(filename)

    c.setFont(FONT_TITLE[0], FONT_TITLE[1])
    c.drawCentredString(300, 700, "Portfolio")
    c.setFont(FONT_LABEL[0], FONT_LABEL[1])
    c.drawString(50, 650, f"Name: {name}")
    c.drawString(50, 620, f"Number: {number}")
    c.drawString(50, 590, f"Email: {email}")
    c.drawString(50, 560, f"Qualification: {qualification}")
    c.drawString(50, 530, f"Skills:")
    c.setFont(FONT_LABEL[0], FONT_LABEL[1] - 2)
    c.drawString(50, 500, skills)

    try:
        photo = Image.open(photo_filename)
        photo.thumbnail((200, 200))
        thumbnail_filename = f"thumbnail_{os.path.basename(photo_filename)}"
        photo.save(thumbnail_filename)
        c.drawImage(thumbnail_filename, 400, 500)
    except Exception as e:
        messagebox.showerror("Error", f"Error processing photo: {e}")
        c.drawString(400, 500, "Photo Not Available")

    c.showPage()
    c.save()

    if os.path.exists(thumbnail_filename):
        os.remove(thumbnail_filename) 


def upload_photo():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if filename:
        global selected_photo
        selected_photo = filename
        img = Image.open(filename)
        img.thumbnail((150, 150))
        photo = ImageTk.PhotoImage(img)
        photo_label.config(image=photo) 
        photo_label.image = photo


app = tk.Tk()
app.title("Portfolio Creator")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}")
app.resizable(True, True)

FONT_LABEL = ("Helvetica", 12)
COLOR_BG = "#f2f2f2"


frame = tk.Frame(app, bg=COLOR_BG)
frame.pack(padx=20, pady=20)

labels = ["Name:", "Number:", "Email:", "Qualification:", "Skills:"]
entry_vars = []
for label_text in labels:
    # Creating labels and entry fields
    label = tk.Label(frame, text=label_text, font=FONT_LABEL, bg=COLOR_BG)
    label.pack(pady=(10, 5))
    entry_var = tk.Entry(frame, font=FONT_LABEL)
    entry_var.pack(pady=5)
    entry_vars.append(entry_var)  # Storing entry variables for later retrieval

# Button to upload a photo
upload_button = tk.Button(frame, text="Upload Photo", font=FONT_LABEL, command=upload_photo)
upload_button.pack(pady=10)

selected_photo = None
# Label to display the selected photo
photo_label = tk.Label(frame, text="Selected Photo Will Appear Here", font=FONT_LABEL, bg=COLOR_BG)
photo_label.pack(pady=10)

# Button to submit the form
submit_button = tk.Button(frame, text="Submit", font=FONT_LABEL, command=submit_form)
submit_button.pack(pady=20)

app.mainloop()