import csv
import os

cwd = os.getcwd()
#print(cwd)

for file in os.listdir('.'):  # use the directory name here

    file_name, file_ext = os.path.splitext(file)
    if file_ext == '.csv':
        with open(file,'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            #csv_reader.next()  ## skip one line (the first one)

            newfile = file.split('.')[0] + 'next.txt'

            for line in csv_reader:
                with open(newfile, 'a') as new_txt:    #new file has .txt extn
                    txt_writer = csv.writer(new_txt, delimiter = ',') #writefile
                    txt_writer.writerow(line)   #write the lines to file`
