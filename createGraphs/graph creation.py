import pyodbc
import pandas as pd
from bokeh.plotting import figure
import bokeh.models as bmo
from bokeh.io import output_file,show

output_file('xsf_ticket_details.html')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=smtcb00410.rd.corpintra.net,1433;'
                      'UID=KPI_RW;''PWD=P@ssW0rD$623;'
                      'Database=VDC_KPI;'
                      'Trusted_Connection=yes;'
                      )
df = pd.read_sql('SELECT * FROM dbo.XSF_TICKET_DETAILS', conn)
x = list(df['STATUS'])
y = list(df['Number of Tickets'])
p = figure(x_range=x,plot_width=900, plot_height=500, title="XSF Ticket Details", x_axis_label='Status',y_axis_label='Number Of Tickets')
p.vbar(x=x, top=y, width=0.4,color='#F35A53')
hover = bmo.HoverTool(
    tooltips=[
        ("Status", "@x"),
        ('Number Of Tickets', '@top')
    ]
)
p.add_tools(hover)
p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
conn.close()
