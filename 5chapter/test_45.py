import unittest
from neko2 import Morph, Chunk, extract_case_patterns


class TestExtractPredicate(unittest.TestCase):
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


class TestExtractCasePatterns(unittest.TestCase):
    def test_no_verbs_in_sentence(self):
        chunk0 = Chunk([Morph(surface='名前', base='名前', pos='名詞', pos1='一般'),
                        Morph(surface='は', base='は', pos='助詞', pos1='係助詞')],
                       dst=1)
        chunk1 = Chunk([Morph(surface='無い', base='無い', pos='形容詞', pos1='自立')],
                       dst=-1, srcs=[0])
        sentence = [chunk0, chunk1]
        case_patterns = extract_case_patterns(sentence)
        self.assertEqual(case_patterns, [])

    def test_one_verb_one_particle_in_sentence(self):
        chunk0 = Chunk([Morph(surface='もの', base='もの', pos='名詞', pos1='非自立'),
                        Morph(surface='を', base='を', pos='助詞', pos1='格助詞')],
                       dst=1)
        chunk1 = Chunk([Morph(surface='見た', base='見る', pos='動詞', pos1='自立'),
                        Morph(surface='た', base='た', pos='助動詞', pos1='*')],
                       dst=-1, srcs=[0])
        sentence = [chunk0, chunk1]
        case_patterns = extract_case_patterns(sentence)
        self.assertEqual(case_patterns, ['見る\tを'])

    def test_one_verb_two_particles_in_sentence(self):
        chunk0 = Chunk([Morph(surface='我輩', base='我輩', pos='名詞', pos1='代名詞'),
                        Morph(surface='は', base='は', pos='助詞', pos1='係助詞')],
                       dst=2)
        chunk1 = Chunk([Morph(surface='もの', base='もの', pos='名詞', pos1='非自立'),
                        Morph(surface='を', base='を', pos='助詞', pos1='格助詞')],
                       dst=2)
        chunk2 = Chunk([Morph(surface='見た', base='見る', pos='動詞', pos1='自立'),
                        Morph(surface='た', base='た', pos='助動詞', pos1='*')],
                       dst=-1, srcs=[0, 1])
        sentence = [chunk0, chunk1, chunk2]
        case_patterns = extract_case_patterns(sentence)
        self.assertEqual(case_patterns, ['見る\tは を'])

    def test_two_case_patterns_in_sentence(self):
        chunk0 = Chunk([Morph(surface='我輩', base='我輩', pos='名詞', pos1='代名詞'),
                        Morph(surface='は', base='は', pos='助詞', pos1='係助詞')],
                       dst=5)
        chunk1 = Chunk([Morph(surface='ここ', base='ここ', pos='名詞', pos1='代名詞'),
                        Morph(surface='で', base='で', pos='助詞', pos1='格助詞')],
                       dst=2)
        chunk2 = Chunk([Morph(surface='始め', base='始める', pos='動詞', pos1='自立'),
                        Morph(surface='て', base='て', pos='助詞', pos1='接続助詞')],
                       dst=3, srcs=[1])
        chunk3 = Chunk([Morph(surface='人間', base='人間', pos='名詞', pos1='一般'),
                        Morph(surface='という', base='という', pos='助詞', pos1='格助詞')],
                       dst=4, srcs=[2])
        chunk4 = Chunk([Morph(surface='もの', base='もの', pos='名詞', pos1='非自立'),
                        Morph(surface='を', base='を', pos='助詞', pos1='格助詞')],
                       dst=5, srcs=[3])
        chunk5 = Chunk([Morph(surface='見た', base='見る', pos='動詞', pos1='自立'),
                        Morph(surface='た', base='た', pos='助動詞', pos1='*')],
                       dst=-1, srcs=[0, 4])
        sentence = [chunk0, chunk1, chunk2, chunk3, chunk4, chunk5]
        case_patterns = extract_case_patterns(sentence)
        self.assertEqual(case_patterns, ['始める\tで', '見る\tは を'])


if __name__ == '__main__':
    unittest.main()
