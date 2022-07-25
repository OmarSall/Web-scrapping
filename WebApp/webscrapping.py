import justpy as jp
import pandas as pd
# from datetime import datetime
# from pytz import utc
import matplotlib.pyplot as plt

data = pd.read_csv("Output.csv")
data['House address'] = data['Address']
data['House Price'] = data['Price']

chart_def = """
 {
    chart: {
        type: 'column',
        styledMode: true,
        options3d: {
            enabled: true,
            alpha: 15,
            beta: 15,
            depth: 50
        }
    },
    title: {
        text: 'Highcharts 3d column in styled mode'
    },
    plotOptions: {
        column: {
            depth: 25
        }
    },
    xAxis: {
        categories: 
    },
    series: [{
        data: ,
        colorByPoint: true
    }]
}

"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Web scrapping", classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "Omar Salloum")
    hc = jp.HighCharts(a = wp, options = chart_def)

    hc.options.title.text = "Pricing characteristics"
    # because timestamp is set as category 
    hc.options.xAxis.categories = list(data['Address'])
    hc.options.yAxis.categories = list(data['Price'])

   

    # print(hc.options.title.text)
    # print(type(hc.options))

    return wp

#wp is a quasar instance

jp.justpy(app)