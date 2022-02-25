
with open("all_thresholded_by_genes.txt", 'r') as f:
    newline = []
    for word in f.readlines():
        splits = word.split("\t")
        word = "\t".join(splits[0:2])+ "\t" + "\t".join(splits[3:])
        newline.append(word.replace("Gene Symbol", "Hugo_Symbol").replace("Locus ID", "Entrez_Gene_Id"))

with open("all_thresholded_by_genes.txt", "w") as f:
    for line in newline:
        f.writelines(line)












