import pygal
bar_chart = pygal.Bar()
bar_chart.add("namber of car", [0, 10, 33, 56, 74, 99, 124, 643])

bar_chart.render_to_file('barchart.svg')