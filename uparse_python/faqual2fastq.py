import sys
import click
from uparse_python import fasta, fastq, die


@click.command()
@click.option('--fasta', type=click.File('r'), prompt=True,help="name of the FASTA file")
@click.option('--qual', type=click.File('r'), prompt=True,help="name of the QUAL file")
def faqual2fastq(fasta, qual):
	"""
	see: http://drive5.com/python/faqual2fastq_py.html
	"""

	ff = open(fasta)
	fq = open(qual)

	while 1:
		Linef = ff.readline()
		if len(Linef) == 0:
			break
		Labelf = Linef.strip()
		Seqf = ff.readline().strip()
		L = len(Seqf)
		assert L != 0

		Labelq = fq.readline().strip()
		Seqq = fq.readline().strip()
		assert len(Seqq) != 0

		Labf = Labelf.split()[0]
		Labq = Labelq.split()[0]

		if Labf != Labq:
			print >> sys.stderr
			print >> sys.stderr, "LABEL MISMATCH"
			print >> sys.stderr, "Labelf:", Labelf
			print >> sys.stderr, "Labelq:", Labelq
			sys.exit(1)

		Quals = Seqq.split()
		LQ = len(Quals)
		if LQ != L:
			die.Die("LS %u, LQ %u >%s" % (L, LQ, Labelf))

		q = ""
		for Qual in Quals:
			iq = int(Qual)
			cq = fastq.IntQualToChar(iq)
			q += cq

		assert len(q) == L
		fastq.WriteRec(sys.stdout, Labelf, Seqf, q)
