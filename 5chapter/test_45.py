import unittest
from neko2 import Morph, Chunk, extract_predicate_from_chunk


class TestExtractPredicate(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_verbs_in_phrase(self):
        morphs = [Morph(surface='我輩', base='我輩', pos='名詞', pos1='代名詞'),
                  Morph(surface='は', base='は', pos='助詞', pos1='係助詞')]
        chunk = Chunk(morphs)
        predicate = extract_predicate_from_chunk(chunk)
        self.assertEqual(predicate, '')

    def test_one_verb_in_phrase(self):
        morphs = [Morph(surface='生れ', base='生れる', pos='動詞', pos1='自立'),
                  Morph(surface='た', base='た', pos='助動詞', pos1='*'),
                  Morph(surface='か', base='か', pos='助詞', pos1='副助詞')]
        chunk = Chunk(morphs)
        predicate = extract_predicate_from_chunk(chunk)
        self.assertEqual(predicate, '生れる')

    def test_two_verb_in_phrase(self):
        morphs = [Morph(surface='記憶', base='記憶', pos='名詞', pos1='サ変接続'),
                  Morph(surface='し', base='する', pos='動詞', pos1='自立'),
                  Morph(surface='て', base='て', pos='助詞', pos1='接続助詞'),
                  Morph(surface='いる', base='いる', pos='動詞', pos1='非自立')]
        chunk = Chunk(morphs)
        predicate = extract_predicate_from_chunk(chunk)
        self.assertEqual(predicate, 'する')

if __name__ == '__main__':
    unittest.main()
