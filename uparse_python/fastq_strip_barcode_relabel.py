#!/usr/bin/python
# Expect seq = <barcode><primer><gene>
# Allow 2 mismatches with primer
# Allow 0 mismatches with barcode
# Strips primer & barcode, adds barcode to seq label.

import sys
import click
from uparse_python import fasta, fastq, primer


@click.command()
@click.option('--fastq', type=click.Path(exists=True), prompt=True,help="name of the FASTQ file")
@click.option('--primer', type=click.STRING, prompt=True,help="primer string")
@click.option('--barcodefilename', type=click.File('r'), prompt=True, help="barcodes in FASTA format")
@click.option('--labelprefix', type=click.STRING, default="OTU_", help="fileprefix")
def fastq_strip_barcode_relabel(fastq, primer,barcodefilename,labelprefix):
	"""
	see also: http://drive5.com/python/fastq_strip_barcode_relabel_py.html
	"""

	MAX_PRIMER_MISMATCHES = 2

	FileName = fastq
	Primer = primer
	BarcodeFileName = barcodefilename
	LabelPrefix = labelprefix

	SeqCount = 0
	OutCount = 0
	BarcodeMismatchCount = 0
	PrimerMismatchCount = 0
	PL = len(Primer)

	#set glboal variables
	global PL, LabelPrefix, Barcode, SeqCount, OutCount, BarcodeMismatchCount, PrimerMismatchCount, MAX_PRIMER_MISMATCHES, Primer

	#process data

	Barcodes = fasta.ReadSeqsDict(BarcodeFileName)
	fastq.ReadRecs(FileName, OnRec)

	print >> sys.stderr, "%10u seqs" % SeqCount
	print >> sys.stderr, "%10u matched" % OutCount
	print >> sys.stderr, "%10u barcode mismatches" % BarcodeMismatchCount
	print >> sys.stderr, "%10u primer mismatches" % PrimerMismatchCount

def MatchesPrimer(Seq, Primer):
	return primer.MatchPrefix(Seq, Primer)

def FindBarcode(Seq):
	global Barcodes
	for BarcodeLabel in Barcodes.keys():
		Barcode = Barcodes[BarcodeLabel]
#		print "Barcode", Barcode, "Seq", Seq
		if Seq.startswith(Barcode):
			return Barcode
	return ""
	
def OnRec(Label, Seq, Qual):

	SeqCount += 1
	Barcode = FindBarcode(Seq)
	if Barcode == "":
		BarcodeMismatchCount += 1
		return

	BarcodeLength = len(Barcode)
	Seq = Seq[BarcodeLength:]
	Qual = Qual[BarcodeLength:]

	Diffs = MatchesPrimer(Seq, Primer)
	if Diffs > MAX_PRIMER_MISMATCHES:
		PrimerMismatchCount += 1
		return

	OutCount += 1
	if LabelPrefix == "-":
		NewLabel = Label + ";barcodelabel=" + Barcode + ";"
	else:
		NewLabel = LabelPrefix + str(OutCount) + ";barcodelabel=" + Barcode + ";"
	fastq.WriteRec(sys.stdout, NewLabel, Seq[PL:], Qual[PL:])


