

def pascal_row(n):
    if n < 0:
        print("Negative integer input")
        exit()
    else:
        if n == 0:
            return [1]

        #add first element (always '1')
        row = [1]
        #add 'n-1' elements per row, each one the sum of sequenced pairs of elements from previous row
        #for 'n==1' do not iterate as it is a defined [1,1] row
        for i in range(1, n):
            row.append( sum( pascal_row(n-1)[i-1:i+1] ) )
        # add last element (always '1')
        row.append(1)
        return row


#### TEST CASES ####
print('n = 0:', pascal_row(0) ) #expect [1]
print('n = 1:', pascal_row(1) ) #expect [1,1]
print('n = 2:', pascal_row(2) ) #expect [1,2,1]
print('n = 3:', pascal_row(3) ) #expect [1,3,3,1]
print('n = 4:', pascal_row(4) ) #expect [1,4,6,4,1]
print('n = 5:', pascal_row(5) ) #expect [1,5,10,10,5,1]
print('n = 6:', pascal_row(6) ) #expect [1,6,15,20,15,6,1]
print('n = 7:', pascal_row(7) ) #expect [1,7,21,35,35,21,7,1]