class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        if head in self.visited:
            return self.visited[head]

        newNode = Node(head.val)
        self.visited[head] = newNode

        newNode.next = self.copyRandomList(head.next)
        newNode.random = self.copyRandomList(head.random)

        return newNode
