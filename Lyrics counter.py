import plotly
from plotly.offline import init_notebook_mode
import plotly.graph_objs as go
import bs4 as bs
from urllib.request import Request, urlopen
import random
import operator
import collections
import time


def url_parse(url1):
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    req = Request(url=url1, headers=hdr)
    wb = urlopen(req).read()
    resp = bs.BeautifulSoup(wb, 'html.parser')
    para = resp.find('div', attrs={'class': 'holder lyric-box'})
    return para.text


def file_writer(text):
    with open('C:/Users/ACER/Desktop/rSong.txt', 'w') as f:
        for line in text:
            f.write(line)


def starting_url():
    number = random.randint(1, 9999)
    url = ''.join(['https://songmeanings.com/songs/view/', str(number), '/'])
    return url


def file_reader():
    fo = open("C:/Users/ACER/Desktop/rSong.txt", "r")
    lyric_list = []
    with fo:
        for line in fo:
            lyric_list.extend(line.split())

    return lyric_list


def dict_counter(ly):
    unique_words = set(ly)
    return unique_words


def dict_sort(ly, uw):
    histogram = dict.fromkeys(uw, 0)
    for word in ly:
        histogram[word] = histogram[word] + 1
    sorted_h = sorted(histogram.items(), key=operator.itemgetter(1), reverse=True)
    rem = int(0.1 * len(sorted_h))
    for _ in range(rem):
        del sorted_h[_]
        sorted_h.pop()
        sorted_h.pop()
    random.shuffle(sorted_h)
    histogram_sorted = collections.OrderedDict(sorted_h)
    return histogram_sorted


def graph_trace(histogram_sorted, uw):
    init_notebook_mode(connected=True)
    trace = go.Scatter(
        x=list(uw),
        y=list(histogram_sorted.values())
    )
    data = [trace]
    layout = go.Layout(
        title=go.layout.Title(
            text='Lyrics Words Count',
            xref='paper',
            x=0
        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text='Unique Words',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text='Number Of Occurrences',
                font=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            )
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='scatter.html')


def main():
    start_time = time.time()
    u = starting_url()
    f = url_parse(u)
    file_writer(f)
    ly = file_reader()
    uw = dict_counter(ly)
    gdata = dict_sort(ly, uw)
    graph_trace(gdata, uw)
    print('{} seconds taken'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
