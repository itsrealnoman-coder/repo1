import csv
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill

# Read CSV
with open('/projects/sandbox/repo1/family_register_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

# Create workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Family Register"

# Add data
for row in data:
    ws.append(row)

# Styling
header_font = Font(bold=True, size=11)
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
header_font_white = Font(bold=True, size=11, color="FFFFFF")
thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# Style header row
for cell in ws[1]:
    cell.font = header_font_white
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    cell.border = thin_border

# Style data rows
for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
    for cell in row:
        cell.border = thin_border
        cell.alignment = Alignment(vertical='center', wrap_text=True)

# Auto-adjust column widths
column_widths = {
    'A': 6,   # Sr. No
    'B': 10,  # Family No
    'C': 18,  # Family Member
    'D': 22,  # Name
    'E': 16,  # CNIC
    'F': 20,  # CNIC Issue Date
    'G': 22,  # D.O.B
    'H': 6,   # Age
    'I': 12,  # Height (cm)
    'J': 12,  # Weight (kg)
    'K': 11,  # Heartbeat
    'L': 35,  # Disease
    'M': 14,  # Profession
    'N': 16,  # House Condition
    'O': 30,  # Notes
}

for col, width in column_widths.items():
    ws.column_dimensions[col].width = width

# Freeze header row
ws.freeze_panes = 'A2'

# Save
wb.save('/projects/sandbox/repo1/family_register_data.xlsx')
print("Excel file created successfully!")
