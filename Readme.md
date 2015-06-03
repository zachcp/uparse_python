##### Uparse python scripts packaged for ease of use

uparse/usearch comes with an optional set of [python scripts](http://drive5.com/python/).
This package combines these scripts and makes them available system wide, hopefully reducing filesystem clutter
and enhancing reproducibility. 


[fasta_number.py](http://drive5.com/python/fasta_number_py.html)
```[python]
uparse_fasta_number.py --fasta fastafile --prefix "awesome_experiment" > fastafile
```

[fastq_strip_barcode_relabel_py](http://drive5.com/python/fastq_strip_barcode_relabel_py.html)
```[python]
uparse_fastq_strip_barcode_relabel_py --fastq fastqfile --primer "ACCTTAC" --barcodefilename barcodes.txt --labelprefix "my_label" > output
```

[faqual2fastq.py](http://drive5.com/python/faqual2fastq_py.html)
```[python]
uparse_faqual2fastq.py --fasta fastafile --qual qualfile > output
```


[uc2otutab.py](http://drive5.com/python/faqual2fastq_py.html)
```[python]
uparse_uc2otutab.py --ucfile ucfile > output
```
