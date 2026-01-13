from bs4 import BeautifulSoup
def make_sense(html_doc):
    if not html_doc:
        return (-1, [])
    soup = BeautifulSoup(html_doc, 'html.parser')
    soup.find("tbody")
    #rows = soup.find_all("tr")
    rows = soup.select("#table-1 > tbody > tr")
    row_num = len(rows)
    #print(row_num)
    msg = list()
    for i in range(1,row_num+1):
        message = ''
        message = message + soup.select_one(f"#table-1 > tbody > tr:nth-child({i}) > td:nth-child(1)").text + " : " + soup.select_one(f"#table-1 > tbody > tr:nth-child({i}) > td:nth-child(5)").text + " | " + soup.select_one(f"#table-1 > tbody > tr:nth-child({i}) > td:nth-child(6)").text + "."
        msg.append(message)
    return (row_num, msg)