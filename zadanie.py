import re
import math
from scipy.stats import chisquare



targetColumn = []
# opening file
with open('convertcsv.csv', newline='', encoding='utf8') as csvfile:
# with open('census_2009b', newline='') as csvfile:
    data = csvfile.readlines()


#  finding the index of target column to avoid hard coding the index.
for headers in data[:1]:
    print(headers)
    headers = headers.replace('\r','').replace('\n','')
    fileHeaders = re.findall(r"(\w+)", headers, 0)
    columnNumber = fileHeaders.index('7_2009')
    print(columnNumber)

# staighting up the file columns, cutting only words and numbers from the file to align column count.
for row in data[1:]:
    sub = re.sub(r"[^A-Za-z0-9. ()'-/]+",", ",row, 0, re.MULTILINE).split(', ')
    if len(sub) == len(fileHeaders)+1:  # i didnt menage to find regex for multiple and single spaces, my data will be missing 7 rows
        targetColumn.append(sub[columnNumber])
# calculating procentage of provided number occuring on first position of every number provided in a dataset
print(targetColumn)
def countRatio(listOfNumbers, number):
    counter = 0
    if len(listOfNumbers)>10:
        for x in listOfNumbers:
            if int(x[0]) == number:
                counter+=1
        # return str(number)+' occured '+str(counter)+' times, ratio is: '+ str(round(counter/len(listOfNumbers)*100,1))
        return round(counter/len(listOfNumbers)*100,1)
    else:
        print('Provide a list containing more than 10 records!')


realValues = []
expectedValues = []
for x in range(1,10):
    realValues.append(countRatio(targetColumn,x))
    expectedValues.append(round(math.log10(1+(1/x))*100,1))


# print(realValues)
# print()
# print(expectedValues)

# calculating if data obey the law using chisquare test.
powerDivergence = float(str(chisquare(realValues, f_exp=expectedValues)).split('pvalue=')[1].replace(')',''))*100
print(powerDivergence)
if powerDivergence > 95:
    print('Data obeys Benford\'s Law')
else:
    print('Data does not obey Benford\'s Law')