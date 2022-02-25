
with open("all_data_by_genes.txt", 'r') as f:
    newline = []
    for word in f.readlines():
        splits = word.split("\t")
        if splits[1].startswith("-") :
            word = word.replace(splits[1], "Na")
        word = word.replace("|chr1", "")
        newline.append(word.replace("Gene Symbol", "Hugo_Symbol").replace("Gene ID", "Entrez_Gene_Id"))
         
            


with open("all_data_by_genes.txt", "w") as f:
    for line in newline:
        f.writelines(line)
