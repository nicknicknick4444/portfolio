import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import requests

def api_call(q):
    return requests.get("http://api.weatherapi.com/v1/current.json?key=b2bf55e4a6c24c55abe104821222603&q={}".format(q))

# badloc = [[1,51,290],[2,202,303],[3,253,340]]
# goodloc = [[1,363,162],[2,376,98],[3,285,19]]

def plotto(goodloc, badloc):
    #plt.rcParams["figure.figsize"] = [6.00,3.87]
    plt.rcParams["figure.autolayout"] = True
    im = plt.imread("./static/images/uk3.png")
    fig, ax = plt.subplots()
    #ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%1f"))
    im = ax.imshow(im, extent=[0, 387, 0, 600])
    #plt.figure()
    for index, i in enumerate(goodloc):
        x=i[3][0]
        y=i[3][1]
        plt.scatter(x,y,marker=".",color="#07e32b")
        plt.text(x+4, y+1, str(index+1), fontsize=9)
    
    for index, i in enumerate(badloc):
        #x = np.array(range(258))
        x=i[3][0]
        y=i[3][1]
        #https://stackoverflow.com/questions/14432557/matplotlib-scatter-plot-with-different-text-at-each-data-point
        
        #plt.text(x, y, "YURKLE", fontdict=None, fontsize=12, ha="center", va="center")
        #plt.scatter(x, y, ls=4, c="#ee0000")
        plt.scatter(x,y, marker=".", color="#f70707")
        plt.text(x+4, y+1, str(index+1), fontsize=9)
        #ax.annotate(txt, x[1], y[1])
        #ax.plot(x, x, ls="dotted", linewidth=2, color="#ee0000")

    plt.axis("off")
# #     plt.grid()
# #     major_ticks_top=np.linspace(0,400,9)
# #     #minor_ticks_top=np.linspace(0,400,9)
# #     major_ticks_bottom=np.linspace(0,600,13)
# #     ax.set_xticks(major_ticks_top)
# #     ax.set_yticks(major_ticks_bottom)
# #     ax.tick_params(axis="both", which="major", labelsize=8)
    fig.set_size_inches(2.58,4)
    fig.savefig("./static/images/boorish.png",bbinches="tight", dpi=113)
        #plt.show()
        #return ax.plot
    
