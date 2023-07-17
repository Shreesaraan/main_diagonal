def main_diagonal_sum(rows,columns,matrix):
    sum=matrix[0]
    iterator=1
    for i in range(rows-1):
        index=(columns+1)*iterator
        sum+=matrix[index]
        iterator+=1
    return sum

input_list=list(map(int,input().split()))
rows=input_list[0]
columns=input_list[1]
matrix=input_list[2:]
print(main_diagonal_sum(rows,columns,matrix))