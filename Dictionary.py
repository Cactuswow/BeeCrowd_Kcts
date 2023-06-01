left = "qwertasdfgzxcvb";
rigth = "yuiophjklnm";
rta="yes";
word = input();
word = list(word);
C = "None";

for i in range(len(word)):

    if(left.find(word[i]) != -1 and (C == "None" or C == "Rigth")):
        C = "Left";
    else:
        if(rigth.find(word[i]) != -1 and (C == "None" or C == "Left")):
            C = "Rigth";
        else:
            rta = "no";
            break;
        
print(rta);