"""
트라이 알고리즘
O(m) : m => 문자열의 길이
"""

class Node(object):
    def __init__(self, key, data=None):
        # key => 값으로 입력될 문자
        self.key = key
        # data => 문자의 종료를 알리는 flag
        self.data = data
        # children => 자식 노드를 저장하는 딕셔너리
        self.children = {}

class Trie:
    def __init__(self):
        # head를 빈 노드로 설정하기.
        self.head = Node(None)

    def insert(self, string):
        """
        트리를 생성하기 위한 함수로, 입력된 문자열의 하나하나를 children에 확인 후 저장하고,
        문자열을 다 돌면 마지막 노드의 data에 문자열을 저장함.
        :param string: 문자열
        """
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        """
        문자열이 존재하는지에 대한 여부 리턴하는 함수
        문자열을 하나씩 돌면서 확인 후 마지막 노드에 data가 존재한다면 True를,
        그렇지 않거나 애초에 children에 존재하지 않는다면 False를 리턴합니다.
        :param string: 문자열
        :return: 문자열 존재 여부, True / False
        """
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        """
        prefix 단어로 시작하는 단어를 찾고 배열로 리턴하는 함수입니다.
        prefix 단어까지 tree를 순회 한 이후 그다음부터 data가 존재하는 것들만 배열에 저장하여 리턴합니다.
        :param prefix: 접두사 String
        :return: 접두사로 시작하는 단어 리스트 / List
        """
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []

        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words


