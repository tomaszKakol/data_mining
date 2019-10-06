import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

import sklearn
from sklearn import cluster
from sklearn.datasets.samples_generator import make_blobs
from sklearn.neighbors import kneighbors_graph

_file_name = "Superstore.xls"


def print_data(_file_name):
    data = pd.read_excel(_file_name)

    print(data)
    print(data.dtypes)

    return data


def clustering(_file_name):
    data = pd.read_excel(_file_name)

    plt.scatter(data.Sales/data.Quantity, data.Quantity)
    plt.xlabel('Price')
    plt.ylabel('Quantity')
    data = data[data.City.isin(["Los Angeles", "Concord"])]
    plt.scatter(data.City, data.Sales)
    plt.xlabel('City')
    plt.ylabel('Sales')
    plt.scatter(data.Quantity, data.Discount)
    plt.xlabel('Quantity')
    plt.ylabel('Discount')
    plt.show()


def quantity_for_each_month(_file_name):
    data = pd.read_excel(_file_name)

    count_q = []
    for i in range(1, 13):
        d = data[data.OrderDate.dt.month == i]
        count_q.append(d.Quantity.sum())

    print(count_q)
    month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                 'August', 'September', 'October', 'November', 'December']
    plt.bar(month_lst, count_q)
    plt.xlabel('Month')
    plt.ylabel('Quantity')
    plt.show()


def date_compare_to_price(_file_name):
    data = pd.read_excel(_file_name)
    data = data.sort_values('OrderDate')
    data = data[(data.ProductName.str.contains(pat='Xerox')) & (data.SubCategory == "Paper")]
    #price = data.Sales/data.Quantity
    print(data)
    plt.scatter(data.OrderDate.dt.strftime("%m-%d"), data.Sales/data.Quantity)
    plt.ylabel('Price')
    plt.xlabel('Date')
    plt.xticks(rotation=90)
    plt.show()


def state_compare_to_price(_file_name):
    data = pd.read_excel(_file_name)

    plt.scatter(data.State, data.Sales/data.Quantity)
    plt.ylabel('Price')
    plt.xlabel('State')
    plt.xticks(rotation=90)
    plt.show()


def quantity_price_discount(_file_name):
    data = pd.read_excel(_file_name)

    ax = plt.axes(projection='3d')
    #zline = np.linspace(0, 15, 1000)
    #xline = np.sin(zline)
    #yline = np.cos(zline)
    #ax.plot3D(xline, yline, zline, 'gray')
    ax.scatter3D(data["Quantity"], data["Sales"]/data["Quantity"], data["Discount"])
    ax.set_xlabel('Quantity')
    ax.set_ylabel('Price')
    ax.set_zlabel('Discount');
    plt.show()
    print(data)


def data_with_price(_file_name):
    data = pd.read_excel(_file_name)

    data["Price"] = data["Sales"]/data["Quantity"]
    data = data.round({"Sales": 2, "Profit": 2, "Price": 2})
    # print(data)
    return data


def price_avarege_depend_on_state(_file_name):
    data = data_with_price(_file_name)

    count_avg = []
    for state_name in data.State.unique():
        data_temp = data[(data.State == state_name) & (data.SubCategory == "Phones")]
        count_avg.append(data_temp.Sales.mean())
    c = 0
    d2 = data[(data.SubCategory == "Phones")]
    d2 = d2.ProductName.value_counts()
    print(d2)
    plt.scatter(data.State.unique(), count_avg)
    plt.xlabel('State')
    plt.ylabel('Price avg')
    plt.xticks(rotation=90)
    plt.show()


def what(_file_name):
    data = data_with_price(_file_name)
    data2 = data.ProductName.value_counts()
    print(data2)
    data3 = data[data.ProductName == "Staples"]
    print(data3)
    data3 = data[data.ProductName == "Staple envelope"]
    print(data3)
    data3 = data[data.ProductName == "Easy-staple paper"]
    print(data3)
    data2 = data[data.Category == "Office Supplies"]
    data2 = data2.SubCategory.value_counts()
    print(data2)


def what_data(_file_name):
    data = data_with_price(_file_name)
    #data = data[data.ProductName == "Staples"]
    #data = data[data.Category == "Office Supplies"]
    #data = data[data.SubCategory == "Paper"]
    data = data[(data.ProductName.str.contains(pat='Xerox')) & (data.SubCategory == "Paper")]
    #print(data)

    count_price_avg = []
    count_discount_avg = []
    for state_name in data.City.unique():
        data_temp = data[(data.City == state_name) & (data.Quantity.nunique() > 2)]
        count_price_avg.append(data_temp.Price.mean())
        count_discount_avg.append(data_temp.Quantity.mean())

    X = np.column_stack((count_discount_avg, count_price_avg))

    kmeans = cluster.AgglomerativeClustering(n_clusters=4, linkage='ward')

    #kmeans = cluster.KMeans(n_clusters=3, init="random")
    #kmeans.fit(X)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    plt.title('Srednia cena i ilosc kupionych rzeczy w danym miescie (papier "Xerox")')
    plt.xlabel('Srednia ilosc kupionych rzeczy')
    plt.ylabel('Srednia cena')
    #centers = kmeans.cluster_centers_
    #plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
    plt.show()


def example():
    X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)
    plt.scatter(X[:, 0], X[:, 1], s=50);
    print(X)
    print(type(X))
    kmeans = cluster.KMeans(n_clusters=4)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)

    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
    plt.show()


if __name__ == '__main__':
  # print_data(_file_name)
  # quantity_for_each_month(_file_name)
  # date_compare_to_price(_file_name)
  # state_compare_to_price(_file_name)
  # quantity_price_discount(_file_name)
  # data_with_price(_file_name)
  # price_avarege_depend_on_state(_file_name)
  # what(_file_name)
  what_data(_file_name)
  # example()
