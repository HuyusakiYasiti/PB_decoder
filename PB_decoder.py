fiftys = [
    ['０', 'わ', 'を', 'ん', '゛', '゜', '６', '７', '８', '９'],
    ['E', 'あ', 'い', 'う', 'え', 'お', 'A', 'B', 'C', 'D'],
    ['J', 'か', 'き', 'く', 'け', 'こ', 'F', 'G', 'H', 'I'], 
    ['O', 'さ', 'し', 'す', 'せ', 'そ', 'K', 'L', 'M', 'N'], 
    ['T', 'た', 'ち', 'つ', 'て', 'と', 'P', 'Q', 'R', 'S'], 
    ['Y', 'な', 'に', 'ぬ', 'ね', 'の', 'U', 'V', 'W', 'X'], 
    ['/', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'Z', '？', '！', 'ー'], 
    ['', 'ま', 'み', 'む', 'め', 'も', '￥', '＆', '', ''], 
    ['', 'や', '（', 'ゆ', '）', 'よ', '＊', '＃', '　', ''], 
    ['５', 'ら', 'り', 'る', 'れ', 'ろ', '１', '２', '３', '４'],
]

s = input("separated by spaces: ")

s = s.split(" ")

for i in s:
    print(fiftys[int(i[0])][int(i[1])], end="")
    if len(s) != s.index(i) + 1:
        print(" ", end="")
    else:
        print("")

