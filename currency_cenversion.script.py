import pandas as pd
from forex_python.converter import CurrencyRates

# Load the Excel file
file_path = "path/to/your/excel/file.xlsx"
df = pd.read_excel(file_path)

# Define the currency conversion rate
conversion_rate = CurrencyRates().get_rate('CZK', 'EUR')

# Convert the 'Umsatz' column to Euro
df['Umsatz_Euro'] = df['Umsatz'] * conversion_rate

# Save the result to a new Excel file
output_path = "path/to/your/output/file.xlsx"
df.to_excel(output_path, index=False)

print(f"Conversion completed. Results saved to {output_path}")
