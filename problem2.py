s = input('')
c = 0
counter = 0
while c != len(s)-2:
    if s[c] == "b" and s[c + 1] == "o" and s[c + 2] == "b":
        counter = counter + 1
    c = c + 1
print(counter)

        
        
    
 
