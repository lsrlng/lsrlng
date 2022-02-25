
with open("all_data_by_genes.txt") as f:
    headerzeile = f.readline().rstrip()

with open("data_clinical_sample.txt", 'a') as file:
    sampleIDs = headerzeile.split('\t')[3:] #liste von samples
    patientIDs = list(map(lambda s: '-'.join(s.split('-')[:3]), sampleIDs))
    l = len(sampleIDs)
    for i in range(l):
        file.write(patientIDs[i] + '\t' + sampleIDs[i] + '\n')
