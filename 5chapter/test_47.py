import unittest
from neko2 import Morph, Chunk, extract_LVCs


class TestExtractSahen(unittest.TestCase):
    def test_no_sahen_in_chunk(self):
        actual = Chunk([Morph(surface='ここ', base='ここ', pos='名詞', pos1='代名詞'),
                        Morph(surface='で', base='で', pos='助詞', pos1='格助詞')]).extract_sahen()
        self.assertEqual(actual, '')

    def test_sahen_in_chunk(self):
        actual = Chunk([Morph(surface='返事', base='返事', pos='名詞', pos1='サ変接続'),
                        Morph(surface='を', base='を', pos='助詞', pos1='格助詞')]).extract_sahen()
        self.assertEqual(actual, '返事を')


class TestExtractLightVerbConstructions(unittest.TestCase):
    def test_no_LVCs_in_sentence(self):
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
        case_patterns = extract_LVCs(sentence)
        self.assertEqual(case_patterns, [])

    def test_one_LVC_in_sentence(self):
        chunk0 = Chunk([Morph(surface='別段', base='別段', pos='副詞', pos1='副詞類接続')],
                       dst=1)
        chunk1 = Chunk([Morph(surface='くる', base='くる', pos='動詞', pos1='自立'),
                        Morph(surface='に', base='に', pos='助詞', pos1='格助詞'),
                        Morph(surface='も', base='も', pos='助詞', pos1='係助詞')],
                       dst=2, srcs=[0])
        chunk2 = Chunk([Morph(surface='及ば', base='及ぶ', pos='動詞', pos1='自立'),
                        Morph(surface='ん', base='ん', pos='助動詞', pos1='*'),
                        Morph(surface='さ', base='さ', pos='助詞', pos1='終助詞'),
                        Morph(surface='と', base='と', pos='助詞', pos1='格助詞')],
                       dst=6, srcs=[1])
        chunk3 = Chunk([Morph(surface='主人', base='主人', pos='名詞', pos1='一般'),
                        Morph(surface='は', base='は', pos='助詞', pos1='係助詞')],
                       dst=6)
        chunk4 = Chunk([Morph(surface='手紙', base='手紙', pos='名詞', pos1='一般'),
                        Morph(surface='に', base='に', pos='助詞', pos1='格助詞')],
                       dst=6)
        chunk5 = Chunk([Morph(surface='返事', base='返事', pos='名詞', pos1='サ変接続'),
                        Morph(surface='を', base='を', pos='助詞', pos1='格助詞')],
                       dst=6)
        chunk6 = Chunk([Morph(surface='する', base='する', pos='動詞', pos1='自立')],
                       dst=-1, srcs=[2, 3, 4, 5])
        sentence = [chunk0, chunk1, chunk2, chunk3, chunk4, chunk5, chunk6]
        case_frames = extract_LVCs(sentence)
        self.assertEqual(case_frames, ['返事をする\tと に は\t及ばんさと 手紙に 主人は'])


if __name__ == '__main__':
    unittest.main()
