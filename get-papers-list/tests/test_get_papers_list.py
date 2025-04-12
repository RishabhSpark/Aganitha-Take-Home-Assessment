import unittest
from get_papers_list.pubmed import fetch_papers

class TestPubMedFunctions(unittest.TestCase):
    def test_fetch_papers_valid_query(self):
        query = "machine learning"
        result = fetch_papers(query)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0, "Expected some PubMed IDs for 'machine learning'")

    def test_fetch_papers_empty_query(self):
        query = ""
        result = fetch_papers(query)
        self.assertEqual(result, [], "Expected empty result for empty query")

    def test_fetch_papers_invalid_query(self):
        query = "nonexistentquery"
        result = fetch_papers(query)
        self.assertEqual(result, [], "Expected empty result for nonexistent query")

if __name__ == "__main__":
    unittest.main()
