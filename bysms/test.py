def  grabOnePage(url):
    print('代码发起请求，抓取网页信息，具体代码省略')

for pageIdx in range(1,101):
    url = f'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,{pageIdx}.html'
    grabOnePage(url)