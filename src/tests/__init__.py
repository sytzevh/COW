import unittest
import json

from converter import Converter
from rdflib import Dataset


class TestConversion(unittest.TestCase):

    def test_intialization(self):
        """
        Tests basic initialization capability of converter.Converter class
        """
        with open('tests/qber-output-example.json') as dataset_file:
            dataset = json.load(dataset_file)

        author_profile = {
            'email': 'john@doe.com',
            'name': 'John Doe',
            'id': '2938472912'
        }

        c = Converter(dataset['dataset'], author_profile)

    def test_simple_conversion(self):
        """
        Tests simple conversion (non-parallel) capability of converter.Converter class
        """
        with open('tests/qber-output-example.json') as dataset_file:
            dataset = json.load(dataset_file)

        author_profile = {
            'email': 'john@doe.com',
            'name': 'John Doe',
            'id': '2938472912'
        }

        c = Converter(dataset['dataset'], author_profile)
        c.setProcesses(1)

        c.convert()

    def test_parallel_conversion(self):
        """
        Tests parallel conversion (2 threads) capability of converter.Converter class
        """
        with open('tests/qber-output-example.json') as dataset_file:
            dataset = json.load(dataset_file)

        author_profile = {
            'email': 'john@doe.com',
            'name': 'John Doe',
            'id': '2938472912'
        }

        c = Converter(dataset['dataset'], author_profile)
        c.setProcesses(2)

        c.convert()

    def test_datatype_conversion(self):
        """
        Tests simple conversion that takes datatypes for 'other' variables in converter.Converter class
        """
        with open('tests/qber-output-example.json') as dataset_file:
            dataset = json.load(dataset_file)

        author_profile = {
            'email': 'john@doe.com',
            'name': 'John Doe',
            'id': '2938472912'
        }

        c = Converter(dataset['dataset'], author_profile, target="output.nq")
        c.setProcesses(1)

        c.convert()

        dataset = Dataset()
        with open("output.nq", "r") as graph_file:
            dataset.load(graph_file, format='nquads')

        q = """
            ASK {
                GRAPH ?g {
                    <http://data.socialhistory.org/ns/resource/observation/utrecht_1829_clean_01/224> <http://data.socialhistory.org/resource/utrecht_1829_clean_01/variable/leeftijd> "55"^^<http://www.w3.org/2001/XMLSchema#integer> .
                    <http://data.socialhistory.org/ns/resource/observation/utrecht_1829_clean_01/1272> <http://data.socialhistory.org/resource/utrecht_1829_clean_01/variable/huisnummer> "170"^^<http://www.w3.org/2001/XMLSchema#integer>  .
                }
            }
        """

        result = dataset.query(q)

        for row in result:
            assert row is True





if __name__ == '__main__':
    unittest.main()
