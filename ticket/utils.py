from django.core.paginator import Paginator
import random
import uuid

def generateTicket():
    # the number of rows and columns
    num_rows = 3
    num_columns = 9

    # Will make 2D array
    ticket = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

    #only fifteen values in the ticket
    occupancyLimit = 15

    while occupancyLimit > 0:
        i = generateRandomNumber(2)
        j = generateRandomNumber(8)

        data = validateAndReturnNumber(i, j, ticket)
        if data > 0:
            ticket[i][j] = data
            occupancyLimit -= 1
        
    return ticket

def generateRandomNumber(num):
    return random.randint(0, num)

def validateAndReturnNumber(i,j, ticket):

    #If value already filled it should not be overide
    if ticket[i][j] != 0:
        return -1
    
    rowCounter = 0
    for r in range(0,3):
        if ticket[r][j]!= 0:
            rowCounter += 1
    
    #Columns cannot contains more than two values
    if(rowCounter >= 2):
        return -1
    
    columnCounter = 0

    for c in range(0,9):
        if ticket[i][c] != 0:
            columnCounter += 1

    #Row cannot have more than 5 elements    
    if columnCounter >= 5:
        return -1
    
    data = 0
    isValueSet = False

    data = generateRandomNumberCol(j)
    isValueSet = isValueExistsCol(ticket, i, j, data)
    while isValueSet:
        data = generateRandomNumberCol(j)
        isValueSet = isValueExistsCol(ticket, i, j, data)
        
    return data

#checking if value exists in column
def isValueExistsCol(ticket, i, j, data):
    status = False
    for k in range(0, 3):
        if ticket[k][j] == data:
            status = True
            break
    return status

#will generate number for a column
def generateRandomNumberCol(high):
    if high == 0:
        high = 10
    else:
        high = (high +1) * 10
    
    low = high - 9

    return generateRandomNumber(high - low) + low

def generateId():
    return uuid.uuid4()

def getPaginatedData(data, page_number):
    paginator = Paginator(data,6)
    final_data = paginator.get_page(page_number)
    return final_data   