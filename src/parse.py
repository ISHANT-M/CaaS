import hashlib

from bs4 import BeautifulSoup


def hash_cg_data(data: list[list[str]]) -> str:
    sha256 = hashlib.sha256()
    
    for inner_list in data:
        # This ensures ['a', 'b'] is distinct from ['ab']
        inner_str = '\0'.join(inner_list)
        
        # This ensures [['a'], ['b']] is distinct from [['a', 'b']]
        inner_str += '\0\0' 
        
        # 3. Update the hash
        sha256.update(inner_str.encode('utf-8'))

    return sha256.hexdigest()

def make_sense(html_doc):
    if not html_doc:
        return (-1, "", [])
    soup = BeautifulSoup(html_doc, 'html.parser')
    soup.find("tbody")
    #rows = soup.find_all("tr")
    rows = soup.select("#table-1 > tbody > tr")
    row_num = len(rows)
    all_cg_data: list[list[str]] = []
    msg = list()
    for i in range(1,row_num+1):
        message = ''
        sem_code = soup.select_one(f"#table-1 > tbody > tr:nth-child({i}) > td:nth-child(1)").text
        sem_credits = soup.select_one(f"#table-1 > tbody > tr:nth-child({i}) > td:nth-child(2)").text
        points_secured = soup.select_one(f"#table-1 > tbody > tr:nth-child({i}) > td:nth-child(4)").text
        sgpa = soup.select_one(f"#table-1 > tbody > tr:nth-child({i}) > td:nth-child(5)").text
        cgpa = soup.select_one(f"#table-1 > tbody > tr:nth-child({i}) > td:nth-child(6)").text
        message = message + sem_code + f" ({points_secured:>5} / {sem_credits:>4})" + " : " + sgpa + " | " + cgpa + "."
        msg.append(message)

        ## Maintain whole sem table
        sem_data = []
        for j in range(1,7):
            col = rows[i-1].select_one(f"td:nth-child({j})")
            col = col.text.strip() if col else ""
            sem_data.append(col)
        all_cg_data.append(sem_data)
    hashed_cg = hash_cg_data(all_cg_data)
    return (row_num, hashed_cg, msg)