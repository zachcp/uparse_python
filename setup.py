import os, sys
from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='uparse-python',
    version='0.1.1',
    description='python scripts from UParse',
    author='zach powers',
    author_email='zcharlop@rockefeller.edu',
    url='https://github.com/zachcp/uparse_python',
    zip_safe=False,
    license="GPL",
    keywords=['uparse','usearch', 'uclust'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
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

