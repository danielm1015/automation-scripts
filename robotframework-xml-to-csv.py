import csv
import xml.etree.ElementTree as ET


tree = ET.parse("Results\output.xml")
root = tree.getroot()

testdata = open('test.csv', 'w', newline='')

# create the csv writer object
csvwriter = csv.writer(testdata)

row_head = ['A', 'B', 'C', 'D', 'C', 'E' ]
for suite in root.findall('suite'):
    test_row = []
    csvwriter.writerow(row_head)
   
    for test in suite.findall('test'):
        for item in suite.findall('metadata/item'):
            test_row.append(item.text)

        test_row.append(test.get('name'))
        test_row.append(test.find('doc').text)
        
        tagdata  = [] 
        for t in test.findall('tags/tag'):
            tagdata.append(t.text)
        test_row.append(tagdata)
        test_row.append(test.find('status').get('status'))
        test_row.append(test.find('status').get('starttime'))
        test_row.append(test.find('status').get('endtime'))
        test_row.append(test.find('status').text)
        tests_keywords = []
        args = []
        for keyword in test.findall('kw'):
            if keyword.get('name') == 'Run Keyword And Continue On Failure':
                for arguments in keyword.findall('arguments'):
                    tests_keywords.append(arguments.find('arg').text)
                    for arg in arguments.findall('arg'):
                        args.append(arg.text)
        test_row.append(tests_keywords)
        test_row.append(args)

        csvwriter.writerow(test_row)
        test_row = []
    
testdata.close()
