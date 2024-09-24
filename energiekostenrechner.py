import tkinter as tk

def konfigurieren():
    # Window size and general settings
    window.geometry("500x350")  # Size of the window
    window.config(bg="#2E2E2E")  # Dark background

    # Config of the Grid-Layouts
    for i in range(8):  # 8 lines 
        window.rowconfigure(i, weight=1)
    for j in range(2):  # 2 columns
        window.columnconfigure(j, weight=1)

def berechnen():
    try:
        # Get and convert values from the input field
        consum = float(input_consum.get())
        efficiency = float(input_efficiency.get())
        hours = float(input_hours.get())
        days = int(input_days.get())
        costs = float(input_costs.get())

        # Calculations
        work_hours = days * hours
        ce = consum / efficiency
        cek = ce / 1000
        costs_month = cek * ce * costs
        costs_year = costs_month * 12

        # Output of the results
        result_label.config(
            text=f"Energiekosten pro Monat: {costs_month:.2f} Euro\n"
                 f"Energiekosten pro Jahr: {costs_year:.2f} Euro",
            justify="center"
        )
    except ValueError:
        result_label.config(text="Bitte nur gültige Zahlen eingeben!")

# Create main window
window = tk.Tk()
window.title("Energiekostenrechner")

# Open configuration
konfigurieren()

# Labels for input fields
label_consum = tk.Label(window, text="Verbrauch in Watt:", font=("Helvetica", 15), foreground="white", background="#2E2E2E")
label_efficiency = tk.Label(window, text="Wirkungsgrad in %:", font=("Helvetica", 15), foreground="white", background="#2E2E2E")
label_hours = tk.Label(window, text="Stunden pro Tag:", font=("Helvetica", 15), foreground="white", background="#2E2E2E")
label_days = tk.Label(window, text="Anzahl der Tage:", font=("Helvetica", 15), foreground="white", background="#2E2E2E")
label_costs = tk.Label(window, text="Stromkosten in Cent/kWh:", font=("Helvetica", 15), foreground="white", background="#2E2E2E")

# Input fields
input_consum = tk.Entry(window, font=("Helvetica", 14), bg="#505050", fg="white", insertbackground="white", relief="flat")
input_efficiency = tk.Entry(window, font=("Helvetica", 14), bg="#505050", fg="white", insertbackground="white", relief="flat")
input_hours = tk.Entry(window, font=("Helvetica", 14), bg="#505050", fg="white", insertbackground="white", relief="flat")
input_days = tk.Entry(window, font=("Helvetica", 14), bg="#505050", fg="white", insertbackground="white", relief="flat")
input_costs = tk.Entry(window, font=("Helvetica", 14), bg="#505050", fg="white", insertbackground="white", relief="flat")

# Button for calculation
calculate_button = tk.Button(window, text="Berechnen", command=berechnen, font=("Helvetica", 14), fg="white", bg="#3A3A3A", 
                             activebackground="#505050", bd=2, highlightbackground="royalblue", highlightcolor="royalblue", relief="flat")

# Label for output
result_label = tk.Label(window, text="", font=("Helvetica", 18), background="#2E2E2E", foreground="white")

# === Arrange elements on the window ===

# Consumption
label_consum.grid(row=0, column=0, sticky="w", pady=(10, 5), padx=10)
input_consum.grid(row=0, column=1, pady=(10, 5), padx=10)

# Efficiency
label_efficiency.grid(row=1, column=0, sticky="w", pady=(5, 5), padx=10)
input_efficiency.grid(row=1, column=1, pady=(5, 5), padx=10)

# Hours
label_hours.grid(row=2, column=0, sticky="w", pady=(5, 5), padx=10)
input_hours.grid(row=2, column=1, pady=(5, 5), padx=10)

# Days
label_days.grid(row=3, column=0, sticky="w", pady=(5, 5), padx=10)
input_days.grid(row=3, column=1, pady=(5, 5), padx=10)

# Electricity costs
label_costs.grid(row=4, column=0, sticky="w", pady=(5, 5), padx=10)
input_costs.grid(row=4, column=1, pady=(5, 5), padx=10)

# Button
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Show result
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Show window
window.mainloop()
