# link: https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # Part1: Building Graph (Node: Adjacency list)
        def singleLetterDifference(w1, w2):
            """
            Finds the count of different letters in the two words
            If the count is equals to 1 it return True
            Meaning we can add w1 and w2 in each others adjacency lists
            else return False
            """
            if len(w1) != len(w2):
                return False
            if node[wordList[i]] in adj[node[wordList[j]]] or node[wordList[j]] in adj[node[wordList[i]]]:
                return False
            cnt = 0
            for x in range(len(w1)):
                if w1[x] != w2[x]:
                    cnt += 1
            return cnt == 1
        
        if beginWord not in wordList:
            flag = False
        else:
            flag = True
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        node = {}
        for i in range(len(wordList)):
            node[wordList[i]] = i
            
        
        adj = [[] for i in range(len(wordList))]
        
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if singleLetterDifference(wordList[i], wordList[j]):
                    adj[node[wordList[i]]].append(node[wordList[j]])
                    adj[node[wordList[j]]].append(node[wordList[i]])
        
        #print(node)
        #print(adj)
        
        # Part2: BFS
        
        def get_key(val):
            for key, value in node.items():
                 if val == value:
                        return key

            return "key doesn't exist"
        
        queue = []
        visited = set()
        #distance = 0
        
        queue.append(node[beginWord])
        visited.add(node[beginWord])
        distance = 0
        
        while len(queue):
            nextWordIndex = queue.pop(0)
            distance += 1
            for nxt in adj[nextWordIndex]:
                #print(queue)
                #print(visited)
                if nxt not in visited:
                    if get_key(nxt) == endWord:
                        if flag:
                            return distance + 1
                        else:
                            return distance
                    queue.append(nxt)
                    visited.add(nxt)         
        
        return 0