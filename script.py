import csv

file1 = open("1_1_UE_Long-staying cell.txt","r+")
#print(file1.read(10))

#print(file1.readline(10))
# Using readline() 
 
count = 0
data = []
  
while True: 
    
    # Get next line from file 
    line = file1.readline() 
  
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    
    #print("{}".format(line.strip())) 
    linedata = line[2:17],line[21:36],line[45:65],line[70:73]
    
    data.append(linedata)
#print(data[6898627])
file1.close()

header = ("imsi", "cell_id", "Data_Duration","RN")
filename = "1_1_3.csv"

def writer(header, data, filename):
  with open (filename, "w", newline = "") as csvfile:
    movies = csv.writer(csvfile)
    movies.writerow(header)
    for x in data:
      movies.writerow(x)
      
#writer(header, data[0:1048500], filename)"1_1_1.csv"
#filename = "1_1_2.csv"
#writer(header, data[1048500:2097000],filename)
#filename = "1_1_3.csv"
#writer(header, data[2097000:3145500], filename)
#filename = "1_1_4.csv"
#writer(header, data[3145500:4194000], filename)
#filename = "1_1_5.csv"
#writer(header, data[4194000:5242500], filename)
#filename = "1_1_6.csv"
#writer(header, data[5242500:6291000], filename)
#filename = "1_1_7.csv"
#writer(header, data[6291000:6898628], filename)
