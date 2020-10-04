''' Author: @anuskrishnav
Problem : https://www.hackerrank.com/challenges/find-a-string/problem
'''

string = input().strip()
sub_string = input().strip()
count = 0
position = string.find(sub_string) 
while position != -1:
        count += 1
        string = string[:position] + '' + string[position+1:]
        position = string.find(sub_string)

print(count)