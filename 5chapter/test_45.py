import unittest
from neko2 import Morph, Chunk


class TestExtractPredicate(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_verbs_in_phrase(self):
        morphs = [Morph(surface='我輩', base='我輩', pos='名詞', pos1='代名詞'),
                  Morph(surface='は', base='は', pos='助詞', pos1='係助詞')]
        predicate = Chunk(morphs).extract_verb()
        self.assertEqual(predicate, '')

    def test_one_verb_in_phrase(self):
        morphs = [Morph(surface='生れ', base='生れる', pos='動詞', pos1='自立'),
                  Morph(surface='た', base='た', pos='助動詞', pos1='*'),
                  Morph(surface='か', base='か', pos='助詞', pos1='副助詞')]
        predicate = Chunk(morphs).extract_verb()
        self.assertEqual(predicate, '生れる')

    def test_two_verb_in_phrase(self):
        morphs = [Morph(surface='記憶', base='記憶', pos='名詞', pos1='サ変接続'),
                  Morph(surface='し', base='する', pos='動詞', pos1='自立'),
                  Morph(surface='て', base='て', pos='助詞', pos1='接続助詞'),
                  Morph(surface='いる', base='いる', pos='動詞', pos1='非自立')]
        predicate = Chunk(morphs).extract_verb()
        self.assertEqual(predicate, 'する')


class TestExtractParticles(unittest.TestCase):
    def test_no_particles_in_phrase(self):
        morphs = [Morph(surface='見た', base='見る', pos='動詞', pos1='自立'),
                  Morph(surface='た', base='た', pos='助動詞', pos1='*')]
        particles = Chunk(morphs).extract_particles()
        self.assertEqual(particles, [])

    def test_one_particle_in_phrase(self):
        morphs = [Morph(surface='生れ', base='生れる', pos='動詞', pos1='自立'),
                  Morph(surface='た', base='た', pos='助動詞', pos1='*'),
                  Morph(surface='か', base='か', pos='助詞', pos1='副助詞')]
        particles = Chunk(morphs).extract_particles()
        self.assertEqual(particles, ['か'])

    def test_two_particles_in_phrase(self):
        morphs = [Morph(surface='書生', base='書生', pos='名詞', pos1='一般'),
                  Morph(surface='という', base='という', pos='助詞', pos1='格助詞'),
                  Morph(surface='の', base='の', pos='名詞', pos1='非自立'),
                  Morph(surface='は', base='は', pos='助詞', pos1='係助詞')]
        particles = Chunk(morphs).extract_particles()
        self.assertEqual(particles, ['という', 'は'])

if __name__ == '__main__':
    unittest.main()
