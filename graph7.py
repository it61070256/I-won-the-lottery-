"""
Win the lotterys
"""
import pandas as pd
import matplotlib.pyplot as plt
def main():
    """Print Last Two lottery graph (Beta)"""
    test([])

def test(lis_y):
    """Plot a Bar Graph of Last Two lottery"""
    lis_x = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    data = pd.read_csv('Book1.csv')
    group = data.groupby(['Years'])
    y2013 = group.get_group(2013)
    y2014 = group.get_group(2014)
    y2015 = group.get_group(2015)
    y2016 = group.get_group(2016)
    y2017 = group.get_group(2017)
    y2018 = group.get_group(2018)
    First_pos = count_1(y2013, y2014, y2015, y2016, y2017, y2018)
    plt.bar(lis_x, First_pos)
    plt.show()

def count_1(y2013, y2014, y2015, y2016, y2017, y2018):
    dig = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    for i in y2013.LastTwo:
        num = "%02d"%(i)
        dig[num[0]] += 0.5
    for i in y2014.LastTwo:
        num = "%02d"%(i)
        dig[num[0]] += 0.5
    for i in y2015.LastTwo:
        num = "%02d"%(i)
        dig[num[0]] += 0.5
    for i in y2016.LastTwo:
        num = "%02d"%(i)
        dig[num[0]] += 0.5
    for i in y2017.LastTwo:
        num = "%02d"%(i)
        dig[num[0]] += 0.5
    for i in y2018.LastTwo:
        num = "%02d"%(i)
        dig[num[0]] += 0.5
    return dig.values()

main()
