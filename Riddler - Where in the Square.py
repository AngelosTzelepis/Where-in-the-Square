allUnique=[]
#For each possible 4x4 grid of filled-in squares (2^16)
for i in range(0,65535):
    
    #Generate a 16-character string for that square
    x=(("0000000000000000"+(str(bin(i)))[2:])[-16:])
    
    #Snip all the 2x2 squares from the larger square
    parts=[]
    parts.append(x[0:1]+x[1:2]+x[4:5]+x[5:6])
    parts.append(x[1:2]+x[2:3]+x[5:6]+x[6:7])
    parts.append(x[2:3]+x[3:4]+x[6:7]+x[7:8])    
    parts.append(x[4:5]+x[5:6]+x[8:9]+x[9:10])
    parts.append(x[5:6]+x[6:7]+x[9:10]+x[10:11])
    parts.append(x[6:7]+x[7:8]+x[10:11]+x[11:12])    
    parts.append(x[8:9]+x[9:10]+x[12:13]+x[13:14])
    parts.append(x[9:10]+x[10:11]+x[13:14]+x[14:15])
    parts.append(x[10:11]+x[11:12]+x[14:15]+x[15:16])

    #Check for 9 unique values. If so, add that square to the list of "solutions"    
    if len(set(parts))==9:
        allUnique.append(x)

print allUnique, len(allUnique)