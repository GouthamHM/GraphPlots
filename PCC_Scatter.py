import csv
from numpy import corrcoef
import pandas as pd
import scipy.io as sio
import matplotlib.pyplot as plt

def getattributes (list_of_attrs,start,end):
    dict = {}
    for attr in list_of_attrs[start-1:end]:
        dict[attr]= list_of_attrs.index(attr)
    return dict

def getcolumndata(filelocation, column_number):
    with open(filelocation, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        li = []
        for num, row in enumerate(datareader):
            if num != 0:
                li.append(float(row[column_number]))
        return li

def get_attribute_data(file_location,dict_of_attrs):
    for attr in dict_of_attrs:
        dict_of_attrs[attr]=getcolumndata(file_location,dict_of_attrs[attr])
    return dict_of_attrs

def getcolumnlist(filelocation):
    with open(filelocation) as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in datareader:
            return row

def plot_scatter_pcc(title,x_data,y_data,x_name,y_name):
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.scatter(x_data,y_data,norm=1)
    plt.title(title)
    plt.savefig('./captures/PCC_'+x_name+'vs'+y_name+'.png')
    plt.clf()


def corcoeff_matrix(data):
    keys = data.keys()
    final_dict = []
    matrix=[]
    max_coeff = 0
    max_pair = []
    min_coeff = 999999
    min_pair = []
    for (index,attr) in enumerate(data.keys()):
        corccoeff = []
        for other_attrs in keys:
            corccoeff.append(corrcoef(data[attr],data[other_attrs])[0,1])
        final_dict.append(corccoeff)
        max_cor_list = corccoeff[:]
        max_cor_list.pop(index)
        print max_cor_list
        if max(max_cor_list)>max_coeff :
            max_coeff = max(max_cor_list)
            max_pair = [attr,keys[corccoeff.index(max(max_cor_list))]]
        if min(corccoeff)<min_coeff:
            min_coeff = min(corccoeff)
            min_pair = [attr,keys[corccoeff.index(min(corccoeff))]]
        matrix.append((attr,corccoeff))
    df = pd.DataFrame.from_items(matrix,orient='index',columns=keys)
    df.to_csv('df.csv', index=True, header  =True, sep=',')
    a_dict = {col_name: df[col_name].values for col_name in df.columns.values}
    sio.savemat('df.mat',{'struct':a_dict})
    return {'min':min_pair,'max':max_pair,'max_value':max_coeff,'min_value':min_coeff}




if __name__ =='__main__':
    file_loc = './data/SkillCraft1_Dataset.csv'
    data = get_attribute_data(file_loc,getattributes(getcolumnlist(filelocation=file_loc),6,20))
    #print data
    max_min = corcoeff_matrix(data)
    plot_scatter_pcc('MAX PCC='+str(max_min['max_value']),data[max_min['max'][0]],data[max_min['max'][1]],max_min['max'][0],max_min['max'][1])
    plot_scatter_pcc('MIN PCC='+str(max_min['min_value']),data[max_min['min'][0]], data[max_min['min'][1]], max_min['min'][0], max_min['min'][1])