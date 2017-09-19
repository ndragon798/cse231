import pylab

def draw_plot( x, y, plt_title, x_label, y_label):
    ''' Draw x vs. y (lists should have the same length)
    Sets the title of plot and the labels of x and y axis '''
    
    pylab.title(plt_title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    
    pylab.plot( x, y )
    pylab.show()
    