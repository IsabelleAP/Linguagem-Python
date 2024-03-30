#!/usr/bin/env python
# coding: utf-8

# In[75]:


get_ipython().system('pip install biopython')


# In[76]:


from Bio import SeqIO


# ### Records
# A record in a fasta file is defined using the ">" symbol as the identifier of the sequence <br>
# * how many records are in the file?

# In[77]:


records = list (SeqIO.parse("dna2.fasta", "fasta"))
print("The file has %i records" % len(records))


# ### Tamanho da sequência
# * qual o tamanho de cada sequência no arquivo?
# * qual é o identificador de cada uma dessa sequência?
# * qual a sequência mais longa?
# * qual a sequência mais curta?
# * tem mais de uma mais longa ou mais curta?

# In[78]:


from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio import SeqIO

records = list(SeqIO.parse("dna2.fasta", "fasta"))
for record in records:
    print("ID:", record.id)
    print("Length:", len(record.seq))

with open("dna2.fasta") as in_handle:
    len_and_ids = sorted(
    (len(seq), title.split(None,1)[0])
    for title, seq in SimpleFastaParser(in_handle)
    )
ids = reversed([id for (lenght, id) in len_and_ids])
del len_and_ids
record_index = SeqIO.index("dna2.fasta","fasta")
with open("sorted.fasta","wb") as out_handle:
    for id in ids:
        out_handle.write(record_index.get_raw(id))
print("---------------")
ordenado = list(SeqIO.parse("sorted.fasta", "fasta"))
for ordem in ordenado:
    print("ID:", ordem.id)
    print("Length:", len(ordem.seq))


# ### Identify all ORFS
# Open Reading Frames (ORFs) are regions of nucleotides with no in frame stop codons
# * identify their length
# * the identifier of the longest one
# * the starting position of the longest ORF

# In[79]:


fasta_file = "dna2.fasta"
table = 1
min_pro_len = 100

all_orfs = []
for record in SeqIO.parse(fasta_file,"fasta"):
    print("ID:", record.id)
    for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:
        for frame in range(-3,4):
            lenght = 3* ((len(record.seq) - frame) -1 // 3)
            frame_seq = nuc[frame:] if strand == +1 else nuc[frame:].reverse_complement()
            for pro in nuc[frame : frame + lenght].translate(table).split("*"):
                if len(pro) >= min_pro_len:
                    print("%s...%s - length %i, strand %i, frame %i"
                         % (pro[:30],pro[-3:],len(pro),strand,frame)
                         )
                    all_orfs.append(pro)
    print("-----------")
    

all_orfs.sort(key=len,reverse=True)
if all_orfs:
    print("ORF mais longa:")
    print(all_orfs[0])
    print("Comprimento:", len(all_orfs[0]))
else:
    print("Nenhuma ORF encontrada.")


# In[ ]:





# In[ ]:




