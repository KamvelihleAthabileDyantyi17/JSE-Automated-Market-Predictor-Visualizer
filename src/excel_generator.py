import os
import pandas as pd
from datetime import datetime

def generate_report(df):
    """Takes the analyzed DataFrame and generates a formatted Excel file."""
    # Ensure the reports folder exists
    os.makedirs("reports", exist_ok=True)
    
    # Create a timestamped filename
    date_str = datetime.now().strftime("%Y-%m-%d")
    filepath = f"reports/JSE_Market_Report_{date_str}.xlsx"
    
    print(f"\n[+] Generating visual report: {filepath}")
    
    # Initialize the Excel writer
    writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Market Summary', index=False)
    
    # Access the workbook and worksheet to apply formatting
    workbook  = writer.book
    worksheet = writer.sheets['Market Summary']
    
    # Define custom formats
    header_format = workbook.add_format({'bold': True, 'bg_color': '#D7E4BC', 'border': 1})
    buy_format = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
    sell_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
    
    # Format the header row
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
        
    # Set column widths
    worksheet.set_column('A:A', 12)
    worksheet.set_column('B:E', 15)
    worksheet.set_column('F:F', 25)
    
    # Apply conditional formatting to the Signal column (Column F)
    num_rows = len(df.index)
    worksheet.conditional_format(1, 5, num_rows, 5, {
        'type': 'text', 'criteria': 'containing', 'value': 'Buy', 'format': buy_format
    })
    worksheet.conditional_format(1, 5, num_rows, 5, {
        'type': 'text', 'criteria': 'containing', 'value': 'Risk', 'format': sell_format
    })
    
    writer.close()
    print(f"[+] Report successfully saved! Check your 'reports' folder.")