import re

def segment(input: str):
    input = input.lower()

    # Define separator patterns
    delimiters = [
        "tp.", "t.", "thành phố", "tỉnh",
        "q.", "h.", "quận", "huyện",
        "p.", "x.", "phường", "xã",
        "-", ","
    ]
    regex_pattern = '|'.join(map(re.escape, delimiters))
    
    # Split the address based on the separator patterns
    parts = list(filter(
        lambda p: p != '' and p != ' ',
        re.split(regex_pattern, input)
    ))
    parts = [p.strip() for p in parts]

    return {
        "province": parts[-1],
        "district": parts[-2],
        "ward": parts[-3]
    }

# if __name__ == "main":
test1 = "Xã Thịnh Sơn H., Đo dương T. Nghệ An"
test2 = "X. Hoi Thượng - Đống Hỷ- Thái 20yêN"
test3 = "Tổ 73 -Hoàng Cầu -TP.1 C Xm Đông Đa - Hà Ni"
test4 = "Phường 14, Quận 10, Tp. Hồ Chí Minh"
test5 = "P.14Q.10 -  Hồ Chí Minh"
print(segment(test3))