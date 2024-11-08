# generate_coaching_report.py
from openpyxl import Workbook
from data_ops import add_headers, add_data
from chart_ops import update_chart

# Initialize workbook and worksheet
wb = Workbook()
ws = wb.active
ws.title = "Client Progress Report"

# Initial data to add
initial_data = [
    [1, "C001", "2024-05-01", 5, 3, "Recommended mindfulness exercises"],
    [2, "C001", "2024-05-08", 6, 6, "Suggested reading on stress management"],
    [3, "C001", "2024-05-15", 4, 4, "Encouraged social activities"],
    [4, "C001", "2024-05-22", 6, 5, "Introduced advanced coping strategies"],
    [5, "C001", "2024-05-29", 4, 4, "Maintaining progress, consider group sessions"],
    [6, "C001", "2024-06-05", 6, 7, "Recommended goal-setting and reflection"],
    [7, "C001", "2024-06-12", 7, 6, "Suggested regular journaling to track progress"],
    [8, "C001", "2024-06-19", 5, 8, "Encouraged deeper meditation practice"],
    [9, "C001", "2024-06-26", 6, 3, "Consider support from peers or mentors"],
    [10, "C001", "2024-07-03", 7, 4, "Maintain consistency in healthy habits"],
    [11, "C001", "2024-07-10", 6, 7, "Explore new coping mechanisms"],
    [12, "C001", "2024-07-17", 7, 6, "Recommended mindfulness exercises"],
    [13, "C001", "2024-07-24", 5, 2, "Suggested reading on stress management"],
    [14, "C001", "2024-07-31", 8, 4, "Encouraged social activities"],
    [15, "C001", "2024-08-07", 9, 3, "Introduced advanced coping strategies"],
    [16, "C001", "2024-08-14", 6, 7, "Maintaining progress, consider group sessions"],
    [17, "C001", "2024-08-21", 7, 5, "Recommended goal-setting and reflection"],
    [18, "C001", "2024-08-28", 4, 9, "Suggested regular journaling to track progress"],
    [19, "C001", "2024-09-04", 8, 4, "Encouraged deeper meditation practice"],
    [20, "C001", "2024-09-11", 9, 3, "Consider support from peers or mentors"],
    [21, "C001", "2024-09-18", 6, 7, "Maintain consistency in healthy habits"],
    [22, "C001", "2024-09-25", 5, 8, "Explore new coping mechanisms"],
    [23, "C001", "2024-10-02", 8, 4, "Recommended mindfulness exercises"],
    [24, "C001", "2024-10-09", 7, 5, "Suggested reading on stress management"]
]

# Add headers and initial data
add_headers(ws)
add_data(ws, initial_data)

# Create and update chart
update_chart(ws)

# Save the workbook
wb.save("Client_Progress_Report.xlsx")
print("Spreadsheet created successfully as Client_Progress_Report.xlsx")