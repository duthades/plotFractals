import matplotlib.pyplot as plt #To run this code you will need matplotlib lib
import math
import os  # To clear window "os.systen('clear') "

__author__ = "Sanket Duthade"
__version__ = "1.0.1"
__email__ = "duthade.sanket@iitgn.ac.in"

'''A fractal is a natural phenomenon or a mathematical set
that exhibits a repeating pattern that displays at every scale.'''

plt.show()

def color ():
    # colour for the ploting
    color=raw_input("\nColor\t\tcharacter\n "
                "Blue\t\t   b\n "
                "Green\t\t   g\n "
                "Red\t\t   r\n "
                "Cyan\t\t   c\n"
                " Magenta\t   m\n"
                " Yellow\t\t   y\n "
                "Black\t\t   k\n "
                "Multicolour\t   x\n\n"
                "color : ")
    if color != 'x':
        return color
    else :
        return ''


def Fractal_Tree(x1, y1, angle,length,HOW, depth,color):
    # Recursion two branches
    if depth >0 :

        x2 = x1 + int(math.cos(math.radians(angle)) * length * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * length * 10.0)
        plt.plot((x1, x2), (y1, y2),color)
        if HOW == 'y':
            plt.pause(0.0001)
            plt.xlim([-1800,1800])
            plt.ylim([0,3000])
        Fractal_Tree(x2, y2, angle - 30, length*0.7,HOW,depth - 1,color)
        Fractal_Tree(x2, y2, angle + 30, length*0.7,HOW,depth - 1,color)
    


def square(xm,ym,length,HOW,depth,color):
    # plot square when the middle point and length is given
    # recursion 4 T
    if depth > 0:
        x1 = xm - length/2
        y1 = ym - length/2
        
        x2 = xm + length/2
        y2 = ym - length/2
        
        x3 = xm + length/2
        y3 = ym + length/2
        
        x4 = xm - length/2
        y4 = ym + length/2


        plt.plot([x1,x2,x3,x4,x1],[y1,y2,y3,y4,y1],color)
        if HOW == 'y':
            plt.pause(0.0001)
            plt.xlim([-101,101])
            plt.ylim([-101,101])
        square(x1,y1,length*0.5,HOW,depth-1,color)
        square(x2,y2,length*0.5,HOW,depth-1,color)
        square(x3,y3,length*0.5,HOW,depth-1,color)
        square(x4,y4,length*0.5,HOW,depth-1,color)



def triangle_fractal(x1,y1,x2,y2,x3,y3,HOW,depth,color):
    # find the middle of the triangle length
    # recursion 3 T 
    if depth>0:
        plt.plot([x1,x2,x3,x1],[y1,y2,y3,y1],color)
        x12=(x1+x2)/2.0
        x23=(x2+x3)/2.0
        x31=(x3+x1)/2.0
        y12=(y1+y2)/2.0
        y23=(y2+y3)/2.0
        y31=(y3+y1)/2.0
        plt.plot([x12,x23,x31,x12],[y12,y23,y31,y12],color)
        if HOW == 'y':
            plt.pause(0.0001)
            plt.xlim([0,10])
            plt.ylim([0,9])
        triangle_fractal(x1,y1,x12,y12,x31,y31,HOW,depth-1,color)
        triangle_fractal(x12,y12,x2,y2,x23,y23,HOW,depth-1,color)
        triangle_fractal(x31,y31,x23,y23,x3,y3,HOW,depth-1,color)
        


def nested_triangle_fractal(x1,y1,x2,y2,x3,y3,HOW,depth,m,n,color):
    # section formula m , n
    # recursion 1T
    if depth>0:
        plt.plot([x1,x2,x3,x1],[y1,y2,y3,y1],color)
        x12=(m*x1+n*x2)/(m+n)*1.0
        x23=(m*x2+n*x3)/(m+n)*1.0
        x31=(m*x3+n*x1)/(m+n)*1.0
        y12=(m*y1+n*y2)/(m+n)*1.0
        y23=(m*y2+n*y3)/(m+n)*1.0
        y31=(m*y3+n*y1)/(m+n)*1.0
        plt.plot([x12,x23,x31,x12],[y12,y23,y31,y12],color)
        if HOW == 'y':
            plt.pause(0.0001)
            plt.xlim([0,10])
            plt.ylim([0,9])
        nested_triangle_fractal(x12,y12,x23,y23,x31,y31,HOW,depth-1,m,n,color)



def _square_(xm,ym,length,HOW,depth,m,n,color):
    # forms the square given moddle point
    # calls square fractal
    x1 = xm - length/2
    y1 = ym - length/2
        
    x2 = xm + length/2
    y2 = ym - length/2
        
    x3 = xm + length/2
    y3 = ym + length/2
        
    x4 = xm - length/2
    y4 = ym + length/2


    plt.plot([x1,x2,x3,x4,x1],[y1,y2,y3,y4,y1],color)
    square_fractal(x1,y1,x2,y2,x3,y3,x4,y4,HOW,depth,m,n,color)



def square_fractal(x1,y1,x2,y2,x3,y3,x4,y4,HOW,depth,m,n,color):
    # nested fractal
    # recursion 1 T
    if depth>0:
        
        x12=(m*x1+n*x2)/(m+n)*1.0
        x23=(m*x2+n*x3)/(m+n)*1.0
        x34=(m*x3+n*x4)/(m+n)*1.0
        x41=(m*x4+n*x1)/(m+n)*1.0
        
        y12=(m*y1+n*y2)/(m+n)*1.0
        y23=(m*y2+n*y3)/(m+n)*1.0
        y34=(m*y3+n*y4)/(m+n)*1.0
        y41=(m*y4+n*y1)/(m+n)*1.0
        if HOW == 'y':
            plt.pause(0.0001)
            plt.xlim([-55,55])
            plt.ylim([-55,55])
        plt.plot([x12,x23,x34,x41,x12],[y12,y23,y34,y41,y12],color)
        square_fractal(x12,y12,x23,y23,x34,y34,x41,y41,HOW,depth-1,m,n,color)




def centroid (x1,y1,x2,y2,x3,y3,HOW,depth,color) :
    # finds the centriod
    # recursion 3 T
    if depth > 0:
        xc=(x1+x2+x3)/3.0
        yc=(y1+y2+y3)/3.0

        plt.plot([x1,xc,x2,xc,x3],[y1,yc,y2,yc,y3],color)
        if HOW == 'y':
            plt.pause(0.0001)
            plt.xlim([0,10])
            plt.ylim([0,9])
        centroid (x1,y1,x2,y2,xc,yc,HOW,depth-1,color) 
        centroid (xc,yc,x2,y2,x3,y3,HOW,depth-1,color) 
        centroid (x1,y1,xc,yc,x3,y3,HOW,depth-1,color) 
        

def Rectangle(x1,y1,x2,y2,b,h,m,n,HOW,depth,color):
    
    plt.plot([x1,x2,x2,x1,x1,1],[y1,y2,(y2+b),(y1+b),y1,1],color)   

    if depth > 0:
        x1c=(m*x1+n*x2)/(m+n)
        y1c=(m*y1+n*y2)/(m+n)
        x2c=(n*x1+m*x2)/(m+n)
        y2c=(n*y1+m*y2)/(m+n)


def options():
    # This acts like switch each option calls a function
    # Also calls itself 

    option = raw_input("options\t\tfractals\n\n "
                   " 1\t\tFractal Tree\n "
                   " 2\t\tT-square fractal\n "
                   " 3\t\tSierpinski triangle fractal\n "
                   " 4\t\tNested Triangle fractal\n "
                   " 5\t\tNested square fractal\n "
                   " 6\t\tUniform Mass Center Triangle Fractal\n "
                   " 7\t\tRectangle"
                   "\noption: ")



    if option == '1':
        Fractal_Tree(0, 0, 90,100,(raw_input("\nShow Formation( y or n ) :")), int(raw_input("\nTo see formation please use depth 1 to 8""\nDepth (1 to 12 ) : ")),color())
    elif option == '2':
        square(0,0,100,(raw_input("\nShow Formation( y or n )")),int(raw_input("\nTo see formation please use depth 1 to 5""\nDepth (1 to 8) : ")),color())
    elif option == '3':
        triangle_fractal(0,0,10,0,10/2,10*math.sin(math.radians(60)),(raw_input("\nShow Formation( y or n )")),int(raw_input("\nTo see formation please use depth 1 to 5""\nDepth (1 to 8) : ")),color())
    elif option == '4':
        nested_triangle_fractal(0,0,10,0,5,10*math.sin(math.radians(60)),(raw_input("\nShow Formation( y or n )")),int(raw_input("\nTo see formation please use depth 1 to 100""\ndepth (1 to 400): ")),100,1.1,color())
    elif option == '5':
        _square_(0,0,100,(raw_input("\nShow Formation( y or n )")), int(raw_input("\nTo see formation please use depth 1 to 100""\nDepth (1 to 500) : ")),100,1.1,color())
    elif option == '6':
        centroid (0,0,10,0,5,10*0.866,(raw_input("\nShow Formation( y or n )")),int(raw_input("\nTo see formation please use depth 1 to 5""\nDepth (1 to 8) : ")),color())
    elif option == '7':
        Rectangle (0,0,10,0,3,0.5,float(raw_input("m?")),float(raw_input("n?")),(raw_input("\nShow Formation( y or n )")),int(raw_input("\nTo see formation please use depth 1 to 5""\nDepth (1 to 8) : ")),color())
    plt.show()
    os.system('clear') 


    if raw_input("\n\nTo try another one press c or else press q to quit : ")=='c':

        os.system('clear')  # It clears the windows consol

        options()
        

options()        

