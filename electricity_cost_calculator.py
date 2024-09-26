import tkinter as tk
from tkinter import ttk

def konfigurieren():
    # Window and general settings
    window.geometry("510x350")  # Window size
    window.config(bg="#2E2E2E")  # Dark background

    # Grid-Layout configuration for centered items
    for i in range(8):  # 8 lines
        window.rowconfigure(i, weight=1)
    for j in range(2):  # 2 columns
        window.columnconfigure(j, weight=1)

def berechnen():
    try:
        # Get values ​​from the input fields and convert them to integers
        costs = int(input_costs.get())
        powerOutput = int(input_powerOutput.get())
        workTime = int(input_workTime.get())

        # Calculations
        powerWork = powerOutput * workTime
        powerHours = powerOutput / 1000
        kws = powerHours * costs

        # Show the labels
        result_label.config(
            text=f"{powerHours} Wh\n{powerWork:.2f} kWh\n{round(kws)} cent\n{kws / 100:.2f} Euro",
            justify="center",
            anchor="e",  # Right-align the numbers
        )
    except ValueError:
        result_label.config(text="Bitte nur Zahlen eingeben!")

# Create main window
window = tk.Tk()
window.title("Stromkostenrechner")

# open configurations
konfigurieren()

# Labels for inputs field
label_costs = tk.Label(window, text="Electricity price in cents/kWh:", font=("Helvetica", 15), foreground="white", background="#2E2E2E")
label_powerOutput = tk.Label(window, text="Power in watts:", font=("Helvetica", 15), foreground="white", background="#2E2E2E")
label_workTime = tk.Label(window, text="Worktime in hours:", font=("Helvetica", 15), foreground="white", background="#2E2E2E")

# input fields
input_costs = tk.Entry(window, font=("Helvetica", 14), bg="#505050", fg="white", insertbackground="white", relief="flat")
input_powerOutput = tk.Entry(window, font=("Helvetica", 14), bg="#505050", fg="white", insertbackground="white", relief="flat")
input_workTime = tk.Entry(window, font=("Helvetica", 14), bg="#505050", fg="white", insertbackground="white", relief="flat")

# Button to calculate
calc_button = tk.Button(window, text="Calculate", command=berechnen, font=("Helvetica", 14), fg="white", bg="#3A3A3A", 
                             activebackground="#505050", bd=2, highlightbackground="royalblue", highlightcolor="royalblue", relief="flat")


result_label = tk.Label(window, text="", font=("Helvetica", 16), background="#2E2E2E", foreground="white")

# Formate items in window
label_costs.grid(row=0, column=0, sticky="w", pady=(10, 5), padx=10)
input_costs.grid(row=0, column=1, pady=(10, 5), padx=10)
label_powerOutput.grid(row=1, column=0, sticky="w", pady=(5, 5), padx=10)
input_powerOutput.grid(row=1, column=1, pady=(5, 5), padx=10)
label_workTime.grid(row=2, column=0, sticky="w", pady=(5, 5), padx=10)
input_workTime.grid(row=2, column=1, pady=(5, 5), padx=10)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Show window
window.mainloop()
