from bokeh.plotting import figure, output_file, show

if __name__=="__main__":

    output_file('simple_graph.html')
    fig = figure()
    #type(figure)

    total_vals=int(input("How many values ​​do you want to graph?"))
    x_vals=list(range(total_vals))
    y_vals=[]
    for i in x_vals:
        val= int(input(f"Value Y for {i}: "))
        y_vals.append(val)

    fig.line(x_vals,y_vals,line_width=2)
    show(fig)
    