
pwlist=[
		'UUU','UUC','UUA','UUG','UCU','UCC','UCA',
		'UCG','UAU','UAC','UAA','UAG','UGU','UGC',
		'UGA','UGG',

		'CUU','CUC','CUA','CUG','CCU','CCC','CCA',
		'CCG','CAU','CAC','CAA','CAG','CGU','CGC',
		'CGA','CGG',

		'AUU','AUC','AUA','AUG','ACU','ACC','ACA',
		'ACG','AAU','AAC','AAA','AAG','AGU','AGC',
		'AGA','AGG',

		'GUU','GUC','GUA','GCU','GCC','GAU','GAC',
		'GAA','GGU','GGC','GCA','GCG','GUG','GAG',
		'GGG','GGA']

aacidlist=[
		'Phe/F','Phe/F','Leu/L','Leu/L','Ser/S','Ser/S',
		'Ser/S','Ser/S','Tyr/Y','Tyr/Y','Termination','Termination',
		'Cys/C','Cys/C','Termination','Trp/W',

		'Leu/L','Leu/L','Leu/L','Leu/L','Pro/P','Pro/P',
		'Pro/P','Pro/P','His/H','His/H','Gln/Q','Gln/Q',
		'Arg/R','Arg/R','Arg/R','Arg/R',

		'Ile/I','Ile/I','Ile/I','Met/M','Thr/T','Thr/T',
		'Thr/T','Thr/T','Asn/N','Asn/N','Lys/K','Lys/K',
		'Ser/S','Ser/S','Arg/R','Arg/R',

		'Val/V','Val/V','Val/V','Ala/A','Ala/A','Asp/D',
		'Asp/D','Glu/E','Gly/G','Gly/G','Ala/A','Ala/A',
		'Val/V','Glu/E','Gly/G','Gly/G']

def transfer(seq):

	#inti
	seqlist=list(seq)
	translist=[]
	animolist=[]
	animo=''


	for i in range(1,int(len(seqlist)/3)+1):
		translist=(seqlist[3*(i-1):3*i])

		for j in range(0,len(translist)):
			animo+=translist[0]
			del translist[0]

		animolist.append(animo)
		animo=''

	return animolist

def decode(seq):
	declist=transfer(seq)
	unclist=[]

	for i in range(0,len(declist)):
		for j in range(0,63):
			if declist[i]==pwlist[j]:
				if aacidlist[j]=='Termination':
					break
				else:
					unclist.append(aacidlist[j])

	return unclist

