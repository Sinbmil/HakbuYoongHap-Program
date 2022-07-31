import pandas as pd

# 파일 불러오기, names에 들어간 열 이름에 대한 해당 열 값을 가져옴(여러 열 불러오기 가능)
# 여기서 넣어주는 csv는 색 1가지만 선정된 csv 파일을 넣어주어야 한다.
csv = pd.read_csv('toneColor.csv', names=['color'], encoding='CP949')
# 그 중 한 열에 대한 값을 가져옴
check = csv['color']
# 그 열에 대한 모든 값들을 넣어줌
pick_check = check.values
# 그 값들을 리스트로 넣어줌
color_list = pick_check.tolist()

# 위 csv 변수에 들어간 csv 파일 명과 동일하게 넣어준다
f = open("toneColor.csv", "w")

# for문을 통해 color_list에 있는 값이 어떤 색일 경우 그 색에 맞는 톤 리스트를 뽑아 엑셀화 해준다.
for i in range(len(color_list)) :
        if((color_list[i] == "red") or (color_list[i] == "tomatto") or (color_list[i] == "Coral") or (color_list[i] == "Indian Red") or (color_list[i] == "light coral") or (color_list[i] == "Orange Red")
            or (color_list[i] == "Dark orange") or (color_list[i] == "Orange") or (color_list[i] == "Aqua") or (color_list[i] == "Light purple red") or (color_list[i] == "Sandy Brown") or (color_list[i] == "Peach Puff")
            or (color_list[i] == "a misty rose") or (color_list[i] == "Linen") or (color_list[i] == "Old Race") or (color_list[i] == "Papaya whip") or (color_list[i] == "Floral White")): 
            # write() 함수를 통해 어울리는 tone을 넣어준다.
            f.write(color_list[i] + ',' + 'ws' + ',' + '' + ',' + '' + ',' + ''+ '\n')
        
        elif ((color_list[i] == "Crimson") or (color_list[i] == "Medium Aqua Marine") or (color_list[i] == "Medium Sea Green") or (color_list[i] == "Bright Sea Green")
            or (color_list[i] == "pale turquoise") or (color_list[i] == "Powder Blue") or (color_list[i] == "Deep sky blue") or (color_list[i] == "skyblue") or (color_list[i] == "Light sky blue")
            or (color_list[i] == "middle purple") or (color_list[i] == "plum") or (color_list[i] == "Violet") or (color_list[i] == "Orchid") or (color_list[i] == "Hot pink") or (color_list[i] == "Light Steel Blue")
            or (color_list[i] == "Lavender") or (color_list[i] == "sweet water") or (color_list[i] == "dark gray") or (color_list[i] == "Silver") or (color_list[i] == "Bright gray") or (color_list[i] == "Gainsboro")
            or (color_list[i] == "white smoke")):
            # write() 함수를 통해 어울리는 tone을 넣어준다.
            f.write(color_list[i] + ',' + '' + ',' + 'cs' + ',' + '' + ',' + ''+ '\n')
        
        elif ((color_list[i] == "Reddish brown") or (color_list[i] == "Dark red") or (color_list[i] == "Brown") or (color_list[i] == "a fire brick") or (color_list[i] == "Deep salmon") or (color_list[i] == "Salmon")
          or (color_list[i] == "light salmon") or (color_list[i] == "gold") or (color_list[i] == "a dark golden bar") or (color_list[i] == "Golden Bar") or (color_list[i] == "dark khaki") or (color_list[i] == "Olive")
          or (color_list[i] == "Dark Olive Green") or (color_list[i] == "olive monotonous") or (color_list[i] == "Water duck") or (color_list[i] == "dark turquoise") or (color_list[i] == "Cadet Blue")
          or (color_list[i] == "indigo") or (color_list[i] == "Bisque") or (color_list[i] == "Blanched almonds") or (color_list[i] == "Wheat") or (color_list[i] == "Chocolate") or (color_list[i] == "a burly tree")
          or (color_list[i] == "yellowish brown") or (color_list[i] == "Mochacin") or (color_list[i] == "Navajo a White")):
            # write() 함수를 통해 어울리는 tone을 넣어준다.
            f.write(color_list[i] + ',' + '' + ',' + '' + ',' + 'wf' + ',' + ''+ '\n')
        
        elif((color_list[i] == "Yellow") or (color_list[i] == "Dark green") or (color_list[i] == "Green") or (color_list[i] == "Forest Green") or (color_list[i] == "Sea green")
          or (color_list[i] == "Dark Slate Gray") or (color_list[i] == "Light blue-green") or (color_list[i] == "Steel Blue") or (color_list[i] == "Corn Flower Blue") or (color_list[i] == "Dodger Blue")
          or (color_list[i] == "Medium Blue") or (color_list[i] == "Bluish") or (color_list[i] == "Royal Blue") or (color_list[i] == "Dark Slate Blue") or (color_list[i] == "Slate Blue") or (color_list[i] == "Intermediate Slate Blue")
          or (color_list[i] == "dark magenta") or (color_list[i] == "an intermediate orchid") or (color_list[i] == "Purple") or (color_list[i] == "Order of the Thistle") or (color_list[i] == "Magenta")
          or (color_list[i] == "Medium Purple Red") or (color_list[i] == "dark pink" )or (color_list[i] == "Lavender Blush") or (color_list[i] == "sea shells") or (color_list[i] == "Mint Cream") or (color_list[i] == "Slate Gray")
          or (color_list[i] == "Light Slate Gray") or (color_list[i] == "Alice Blue") or (color_list[i] == "Ghost White") or (color_list[i] == "celestial blue") or (color_list[i] == "snow") or (color_list[i] == "Black")
          or (color_list[i] == "a faint gray") or (color_list[i] == "Gray") or (color_list[i] == "White")):
            # write() 함수를 통해 어울리는 tone을 넣어준다.
            f.write(color_list[i] + ',' + '' + ',' + '' + ',' + '' + ',' + 'cw'+ '\n')
        
        elif((color_list[i] == "Light green") or (color_list[i] == "Grass green") or(color_list[i] == "Reuse Chart") or (color_list[i] == "Green Yellow") or (color_list[i] == "Lime") or (color_list[i] == "Lime Green")
          or (color_list[i] == "Light greens") or (color_list[i] == "light green2") or (color_list[i] == "Mid-Spring Green") or (color_list[i] == "Spring Green") or (color_list[i] == "dark turquoises")
          or (color_list[i] == "Turkish jade") or (color_list[i] == "Medium Turquoise") or (color_list[i] == "Aqua Marine") or (color_list[i] == "Blue Violet") or (color_list[i] == "dark purple") or (color_list[i] == "a dark orchid")):
            # write() 함수를 통해 어울리는 tone을 넣어준다.
            f.write(color_list[i] + ',' + 'ws' + ',' + 'cs' + ',' + '' + ',' + ''+ '\n')
        
        elif((color_list[i] == "a pale golden bar") or (color_list[i] == "khaki cloth") or (color_list[i] == "Light pink") or (color_list[i] == "Pink") or (color_list[i] == "Antique White") or (color_list[i] == "beige") or (color_list[i] == "Corn silk")
          or (color_list[i] == "Lemon chiffon") or (color_list[i] == "Light golden bar yellow") or (color_list[i] == "light yellow") or (color_list[i] == "Birds Brown") or (color_list[i] == "Sienna") or (color_list[i] == "Peru") 
          or (color_list[i] == "rose brown") or (color_list[i] == "Ivory")):
            # write() 함수를 통해 어울리는 tone을 넣어준다.
            f.write(color_list[i] + ',' + 'ws' + ',' + '' + ',' + 'wf' + ',' + ''+ '\n')
        
        elif((color_list[i] == "midnight blue") or (color_list[i] == "the senior service") or (color_list[i] == "Dark blue")):
            # write() 함수를 통해 어울리는 tone을 넣어준다.
            f.write(color_list[i] + ',' + '' + ',' + 'cs' + ',' + '' + ',' + 'cw'+ '\n')
        
# close() 함수를 통해 엑셀 파일을 닫아준다.
f.close()
# 위 코드 자체만으로는 출력 결과가 터미널에 나오는 것이 아니라 엑셀에만 값이 저장되므로
# 성공적으로 수행됐지는지 확인하기 위해 done이라는 문구를 출력해준다.
print("done")
