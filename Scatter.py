import csv
import matplotlib.pyplot as plt
import numpy as np

def getcolumndata(filelocation,column_number):
    with open(filelocation,'r') as csvfile:
        datareader = csv.reader(csvfile,delimiter=',',quotechar='"')
        li = []
        for num,row in enumerate(datareader):
            if num!=0:
                li.append(float(row[column_number]))
        return li

def getcolumnlist(filelocation):
    with open(filelocation) as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in datareader:
            return row

def plot_scatter(filename,x_name,y_name):
    x_data = getcolumndata(filename,getcolumnlist(filename).index(x_name))
    y_data = getcolumndata(filename,getcolumnlist(filename).index(y_name))
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.scatter(x_data,y_data,norm=1)
    plt.savefig('./captures/scatter_'+x_name+'vs'+y_name+'.png')
    plt.clf()



if __name__ == '__main__':
    file = './data/SkillCraft1_Dataset.csv'
    x_axis = 'SelectByHotkeys'
    y_axis = 'AssignToHotkeys'
    plot_scatter(file,x_name=x_axis,y_name=y_axis)

    x_axis = 'NumberOfPACs'
    y_axis = 'GapBetweenPACs'
    plot_scatter(file, x_name=x_axis, y_name=y_axis)



