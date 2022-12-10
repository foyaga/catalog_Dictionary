from collections import Counter

import JSFinder

d1 = []


def do_url(url):
    """处理URL，获取网站目录"""
    del_http = url.split('//')[1]
    path_list = del_http.split('/')
    for item in range(1, len(path_list) - 1):
        path = path_list[item]
        if path.isalnum() and len(path) <= 20:
            d1.append(path)


def get_url(target):
    """调用JSFinder获取URL"""
    d1.clear()
    urls = JSFinder.main(target)
    if urls:
        for url in urls:
            if "//" in url:
                print(url)
                do_url(url)


def save_data():
    """排序保存更新网站目录"""
    all_data = []
    key_list = []
    sx_list = []
    with open("res.txt", "r", encoding='utf-8') as lines:
        for line in lines.readlines():
            line = line.strip()
            all_data.append((line.split(" ")[0], int(line.split(" ")[1])))
    d2 = Counter(d1)
    res = sorted(d2.items(), key=lambda x: x[1], reverse=True)
    print(f"当前URL目录：{res}")
    for key in all_data:
        key_list.append(key[0])
    for i in res:
        if i[0] in key_list:
            wz = key_list.index(i[0])
            su = all_data[wz]
            count = su[1] + i[1]
            path = i[0]
            all_data.pop(wz)
            key_list.pop(wz)
            all_data.append((path, count))
        else:
            sx_list.append(i)
    all_data.extend(sx_list)
    data = sorted(all_data, key=lambda t: t[1], reverse=True)
    open("res.txt", 'w').close()  # 清空文件
    for i in data:
        with open("res.txt", "a", encoding='utf-8') as ff:
            ff.write(i[0] + " " + str(i[1]) + "\n")


if __name__ == "__main__":
    with open("url.txt", "r", encoding='utf-8') as f:
        for lines in f.readlines():
            url = lines.strip()
            get_url(url)
            save_data()
