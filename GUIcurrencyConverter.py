# gui_currency_converter.py

from tkinter import *
from tkinter import ttk, messagebox
from forex_python.converter import CurrencyRates

# Initialize CurrencyRates
cr = CurrencyRates()

# Function to convert currency
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        result = cr.convert(from_curr, to_curr, amount)
        result_label.config(text=f"{amount} {from_curr} = {round(result, 2)} {to_curr}")
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))

# Create main window
root = Tk()
root.title("Currency Converter")
root.geometry("420x300")
root.resizable(False, False)
root.config(bg="#e3f2fd")

# Heading
Label(root, text="Currency Converter", font=("Helvetica", 18, "bold"), bg="#e3f2fd").pack(pady=10)

# Amount input
Label(root, text="Amount:", font=("Helvetica", 12), bg="#e3f2fd").pack()
amount_entry = Entry(root, font=("Helvetica", 12), justify=CENTER)
amount_entry.pack(pady=5)

# Currency selection
frame = Frame(root, bg="#e3f2fd")
frame.pack(pady=10)

currencies = sorted(cr.get_rates('USD').keys())  # List of available currencies

from_currency = ttk.Combobox(frame, values=currencies, width=10, state="readonly", font=("Helvetica", 11))
from_currency.set("USD")
from_currency.grid(row=0, column=0, padx=10)

to_currency = ttk.Combobox(frame, values=currencies, width=10, state="readonly", font=("Helvetica", 11))
to_currency.set("INR")
to_currency.grid(row=0, column=1, padx=10)

# Convert Button
Button(root, text="Convert", command=convert_currency, font=("Helvetica", 12),
        bg="#4caf50", fg="white", padx=10).pack(pady=10)

# Result Label
result_label = Label(root, text="", font=("Helvetica", 14, "bold"), fg="blue", bg="#e3f2fd")
result_label.pack(pady=10)

# Run GUI
root.mainloop()
