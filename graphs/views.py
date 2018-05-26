from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components


def debug(x, name):
    print('\n' * 5)
    print('{} = {}'.format(name, x))
    print('type({}) = {}'.format(name, type(x)))
    print('\n' * 5)

def home(request):
    return render_to_response('home_links.html')

def plot(request):
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

    # add a line renderer with legend and line thickness
    p.line(x, y, legend="Temp.", line_width=2)
    # Store components
    script, div = components(p)

    # Feed them to the Django template.
    return render(request, 'bokeh_graph.html',
                              {'script': script, 'div': div})

def vbar(request):
    plot = figure(plot_width=800, plot_height=500, x_axis_type = 'datetime')

    from random import randint
    x = [i for i in range(15)]
    y = [randint(1, 100) for i in range(len(x))]
    plot.vbar(x=x, width=0.5, bottom=0, top=y, color="#CAB2D6")

    plot.xaxis.axis_label = 'Tempo'
    plot.yaxis.axis_label = 'Ocorrencias'


    plot.title.text_font = "times"
    plot.title.text_font_style = "italic"
    plot.title.text = 'A good title'
    plot.title.align = 'center'
    plot.title.text_font_size = '20pt'

    script, div = components(plot)

    # Feed them to the Django template.
    return render(request, 'bokeh_graph.html',
                  {'script': script, 'div': div})

