check_digit_two= (1*0)+(2*4)+(3*2)+(4*7)+(5*1)
check_digit= (check_digit_two % 10)
print (check_digit)
string= str('172-40-') + str(check_digit)
print (string)


function= (check_digit)**2-(check_digit)+8
print (function)

print (function / 3)
print (function // 3)
print (function % 3)