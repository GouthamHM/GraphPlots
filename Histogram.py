import csv
import matplotlib.pyplot as plt

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

def plothist(column_data,no_of_bins):
    bins = (max(column_data) - min(column_data)) / no_of_bins
    bins = range(0, int(max(column_data)), int(bins))
    plt.hist(column_data, bins=bins, range=(0, max(column_data)))
    plt.xticks(bins)
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.savefig('./captures/' + column_name + '.png')
    plt.clf()

if __name__ == '__main__':
    file = './data/SkillCraft1_Dataset.csv'
    column_name = 'GapBetweenPACs'
    no_of_bins = 25
    column_data = getcolumndata(file,getcolumnlist(file).index(column_name))
    plothist(column_data,no_of_bins)
    column_name = 'ActionsInPAC'
    no_of_bins = 10
    column_data = getcolumndata(file, getcolumnlist(file).index(column_name))
    plothist(column_data, no_of_bins)


