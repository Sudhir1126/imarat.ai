import tkinter as tk

def generate_report():
    # Code to generate report (integrate with data analysis script)
    print("Report generated successfully.")

root = tk.Tk()
root.title("Construction Management Tool")

label = tk.Label(root, text="Welcome to Imarat.ai")
label.pack()

button = tk.Button(root, text="Generate Report", command=generate_report)
button.pack()

root.mainloop()