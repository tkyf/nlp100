import unittest
from neko2 import Morph, Chunk, extract_case_frames


class TestExtractCaseFrames(unittest.TestCase):
    def test_no_verbs_in_sentence(self):
        chunk0 = Chunk([Morph(surface='名前', base='名前', pos='名詞', pos1='一般'),
                        Morph(surface='は', base='は', pos='助詞', pos1='係助詞')],
                       dst=1)
        chunk1 = Chunk([Morph(surface='無い', base='無い', pos='形容詞', pos1='自立')],
                       dst=-1, srcs=[0])
        sentence = [chunk0, chunk1]
        case_frames = extract_case_frames(sentence)
        self.assertEqual(case_frames, [])

    def test_one_verb_one_particle_in_sentence(self):
        chunk0 = Chunk([Morph(surface='もの', base='もの', pos='名詞', pos1='非自立'),
                        Morph(surface='を', base='を', pos='助詞', pos1='格助詞')],
                       dst=1)
        chunk1 = Chunk([Morph(surface='見た', base='見る', pos='動詞', pos1='自立'),
                        Morph(surface='た', base='た', pos='助動詞', pos1='*')],
                       dst=-1, srcs=[0])
        sentence = [chunk0, chunk1]
        case_frames = extract_case_frames(sentence)
        self.assertEqual(case_frames, ['見る\tを\tものを'])

    def test_one_verb_two_particles_in_sentence(self):
        chunk0 = Chunk([Morph(surface='吾輩', base='吾輩', pos='名詞', pos1='代名詞'),
                        Morph(surface='は', base='は', pos='助詞', pos1='係助詞')],
                       dst=2)
        chunk1 = Chunk([Morph(surface='もの', base='もの', pos='名詞', pos1='非自立'),
                        Morph(surface='を', base='を', pos='助詞', pos1='格助詞')],
                       dst=2)
        chunk2 = Chunk([Morph(surface='見た', base='見る', pos='動詞', pos1='自立'),
                        Morph(surface='た', base='た', pos='助動詞', pos1='*')],
                       dst=-1, srcs=[0, 1])
        sentence = [chunk0, chunk1, chunk2]
        case_frames = extract_case_frames(sentence)
        self.assertEqual(case_frames, ['見る\tは を\t吾輩は ものを'])

    def test_two_case_frames_in_sentence(self):
        chunk0 = Chunk([Morph(surface='吾輩', base='吾輩', pos='名詞', pos1='代名詞'),
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
        case_frames = extract_case_frames(sentence)
        self.assertEqual(case_frames, ['始める\tで\tここで', '見る\tは を\t吾輩は ものを'])


if __name__ == '__main__':
    unittest.main()
