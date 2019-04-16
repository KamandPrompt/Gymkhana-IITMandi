import csv

with open('Website_details - Hostel Society.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # print(row[0])
        for i in range(len(row)):
            # print (i)
            # if(col=='')
            # print(row[i])
            s="<tr>\n"
            s+= "  <td class='tg-i6ua'>"+row[0]+"<br></td>\n"
            s+="  <td class='tg-03to'>"+row[1]+"<br></td>\n"
            s+="  <td class='tg-03to'>"+row[2]+"</td>\n"
            s+=                "  <td class='tg-03to'>"+row[3]+"</td>\n"
            s+=                "  <td class='tg-03to'>"+row[4]+"</td>\n"
            s+=                "  <td class='tg-kr4b'>"+row[5]+"</td>\n"
            s+=                "  <td class='tg-03to'>"+row[6]+"</td>\n"
            s+=              "</tr>"
        print(s)
        # if line_count == 0:
        #     print('Column names are {', '.join(row)}')
        #     line_count += 1
        # else:
        #     print('\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        #     line_count += 1
    # print(f'Processed {line_count} lines.')
