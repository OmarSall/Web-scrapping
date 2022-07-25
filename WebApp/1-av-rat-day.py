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
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to web scrapping data'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'House Address'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Pricing'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
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
    hc.options.series[0].data = list(data['Price'])

   

    # print(hc.options.title.text)
    # print(type(hc.options))

    return wp

#wp is a quasar instance

jp.justpy(app)