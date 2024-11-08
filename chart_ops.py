# chart_ops.py
from openpyxl.chart import LineChart, Reference
from openpyxl.chart.series import Series
from openpyxl.chart import LineChart, Reference, Series

def update_chart(ws):
    chart = LineChart()
    chart.title = "Client Mood and Stress Over Time with Predictions"
    chart.x_axis.title = "Session Date"
    chart.y_axis.title = "Score"
    chart.style = 13

    max_row = ws.max_row

    # Historical Mood Score
    mood_data_historical = Reference(ws, min_col=4, min_row=1, max_row=max_row - 4)  # Excluding predictions
    chart.add_data(mood_data_historical, titles_from_data=True)
    mood_series_historical = chart.series[-1]
    mood_series_historical.graphicalProperties.line.solidFill = "006600"  # Green color for historical mood

    # Predicted Mood Score
    mood_pred_data = Reference(ws, min_col=4, min_row=max_row - 3, max_row=max_row)
    mood_series_predicted = Series(mood_pred_data, title="Predicted Mood Score")  # Set title in Series initializer
    mood_series_predicted.graphicalProperties.line.dashStyle = "sysDot"  # Dashed line for predictions
    mood_series_predicted.graphicalProperties.line.solidFill = "00FF00"  # Green color for predicted mood
    chart.series.append(mood_series_predicted)

    # Historical Stress Level
    stress_data_historical = Reference(ws, min_col=5, min_row=1, max_row=max_row - 4)
    chart.add_data(stress_data_historical, titles_from_data=True)
    stress_series_historical = chart.series[-1]
    stress_series_historical.graphicalProperties.line.solidFill = "FF0000"  # Red color for stress level

    # Predicted Stress Level
    stress_pred_data = Reference(ws, min_col=5, min_row=max_row - 3, max_row=max_row)
    stress_series_predicted = Series(stress_pred_data, title="Predicted Stress Level")  # Set title in Series initializer
    stress_series_predicted.graphicalProperties.line.dashStyle = "sysDot"  # Dashed line for predictions
    stress_series_predicted.graphicalProperties.line.solidFill = "FFA500"  # Orange color for predicted stress
    chart.series.append(stress_series_predicted)

    # Set categories for the X-axis (Session Dates)
    dates_ref = Reference(ws, min_col=3, min_row=2, max_row=max_row)
    chart.set_categories(dates_ref)

    # Position the chart on the worksheet
    ws.add_chart(chart, "G2")