
input_file = open("variants_gatk_seg.csv", 'r')
input_lines = input_file.readlines()

output_file = open("variants_gatk_seg.txt", 'w')

for line in input_lines[1:]:
    line = line.replace(",","\t")
    line = line.replace("\"", "")
    output_file.write(line)
    
input_file.close()
output_file.close()
