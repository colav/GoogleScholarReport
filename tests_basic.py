import os
import sys
import time

import re
import unidecode

import pandas as pd

import lxml
import helium

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

import unittest
from GsFacProfile import main

class GsFacProfileTestCase(unittest.TestCase):

	def setUp(self):
                self.bibtex = [{'publisher': 'APS', 
                                'year': '2017', 
                                'pages': '052503', 
                                'number': '5', 
                                'volume': '96', 
                                'journal': 'Physical Review A', 
                                'author': 'Ordóñez-Lasso, Andrés Felipe and Sanz-Vicario, José Luis and Martı́n, Fernando',
                                'title': 'Effect of potential screening on the H 2 autoionizing states', 
                                'ENTRYTYPE': 'article', 'ID': 'ordonez2017effect'}]
                
                self.dft = pd.read_csv('./data/dft.csv')
        
        def text_extract_title(self):

                self.dft['titleU']=self.dft['title'].apply(lambda s: unidecode.unidecode(s))

                self.assertEqual(self.dft['titleU'].apply(main.extract_title).loc[2] ==
                                'Revista Actualidades Biologicas: 100 editions of scientific communication')

                self.assertEqual(dft['titleU'].apply(main.extract_title).loc[0]==
                                'Riqueza, endemismo y conservacion de los mamiferos de Colombia')

                self.assertEqual(dft['titleU']. apply(main.extract_title).loc[3]==
                                'BEHAVIOUR OF HIGH TEMPERATURA PHASES OF THE POLYMERIC SYSTEM PVOH+ NAH 2 PO 4+ H 2')

                self.assertEqual(dft['titleU'].apply(main.extract_title).loc[1]==
                                'Brans-Dicke Theory with : Black Holes and Large Scale Structures')
                                               
        def test_read_bibtex(self):
                
                with open('./data/readbib.bib') as bibfile:
                        bib_str=bibfile.read()
                
                bibreaded=main.read_bibtex(bib_str)

                self.assertEqual(bibreaded.get_entry_list,self.bibtex)

        def test_merge(self):
                pass

if __name__=='__main__':
	unittest.main()
