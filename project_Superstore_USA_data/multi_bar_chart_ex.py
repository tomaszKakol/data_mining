import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def quantity_for_each_month(men, women):
    count_m = []
    for i in range(1, 13):
        d = men[men.OrderDate.dt.month == i]
        count_m.append(d.Quantity.sum() / len(men))
        #count_m.append(d.Discount.sum()/len(d.Discount))
        #count_m.append(d.Profit.sum()/d.Quantity.sum())

    #count_m[:] = [x / len(data) for x in count_m]
    count_w = []
    for i in range(1, 13):
        d2 = women[women.OrderDate.dt.month == i]
        count_w.append(d2.Quantity.sum()/len(women))

    #count_w[:] = [x / len(women) for x in count_w]
    month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                 'August', 'September', 'October', 'November', 'December']

    ind = np.arange(len(month_lst))
    width = 0.27  # the width of the bars
    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind, count_m, width, color='g')
    rects2 = ax.bar(ind + width, count_w, width, color='r')

    ax.set_ylabel('Quantity per person')
    ax.set_xlabel('Month')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((month_lst))
    ax.legend((rects1[0], rects2[0]), ('men', 'women'))

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%.2f' % float(h),#'%d' % int(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)


if __name__ == '__main__':
  data = pd.read_excel("Superstore.xls")
  men = pd.read_excel("men.xlsx")
  men = men[(men.Segment == 'Consumer') & (men.ProductName.str.contains(pat='Green'))]
  print(men.ProductName)
  # print(len(men))
  #print(men.ProductName)

  women = pd.read_excel("women.xlsx")
  women = women[(women.Segment == 'Consumer') & (women.ProductName.str.contains(pat='Green'))]#(women.SubCategory == 'Art')&
  quantity_for_each_month(men, women)
  plt.title('Segment Consumer & ProductName with \'Green\'')
  plt.show()


