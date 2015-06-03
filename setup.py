from setuptools import setup, find_packages

setup(
    name='uparse-python',
    version='0.1.0',
    install_requires=[
        'Click >= 4.0',
    ],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        uparse_fasta_number.py = uparse_python.fasta_number:fasta_number
        uparse_fastq_strip_barcode_relabel.py = uparse_python.fastq_strip_barcode_relabel:fastq_strip_barcode_relabel
        uparse_faqual2fastq.py = uparse_python.faqual2fastq:faqual2fastq
        uparse_uc2otutab.py = uparse_python.uc2otutab:uc2otutab
    ''',
)
