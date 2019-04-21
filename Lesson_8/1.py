"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
import heapq
from collections import Counter, namedtuple

# нашел на просторах такой вариант, рассказать бы на курсах по модуль heapq
# и в принципе можно на курсе и использовать
# http://e-postulat.ru/index.php/Postulat/article/view/617/638


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):

        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def encode(string):
    heap = []
    for ch, freq in Counter(string).items():
        heap.append((freq, len(heap), Leaf(ch)))
    heapq.heapify(heap)
    count = len(heap)
    while len(heap) > 1 :
        freq1, _count1, left = heapq.heappop(heap)
        freq2, _count2, right = heapq.heappop(heap)

        heapq.heappush(heap, (freq1+freq2, count, Node(left, right)))

        count += 1
    code = {}
    if heap:
        [(_freq, _count, root)] = heap
        root.walk(code, '')
    return code


def decode(encoded, code):
    sx = []
    enc_ch = ''
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch=''
                break
    return ''.join(sx)


string = 'мама мыла раму'
code = encode(string)
encoded = ''.join(code[ch] for ch in string)
print(len(code), len(encoded))
for ch in sorted(code):
    print(f'{ch}: {code[ch]}')
print(encoded)
print(decode(encoded, code))

