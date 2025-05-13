'''
🍪문제 번호 :
ch14_tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

🍊풀이 시간 :
failed

🍒풀이 방법 :
스택 풀이가 아직 익숙하지 않은 것 같음. 링크드리스트, 트리 구조가 나오면 해당 풀이를 먼저 생각하도록 암기하기.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = ''
        que = [root]

        while que :
            node = que.pop(0)

            if node :
                que.append(node.left)
                que.append(node.right)
                ans +=str(node.val)+"*"
            else :
                ans +='None*'

        return ans
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'None*' : return []

        nodes = data.split('*')
        root = TreeNode(int(nodes[0]))
        idx = 1

        que = [root]
        while que :
            node = que.pop(0)

            if nodes[idx]!='None' :
                node.left = TreeNode(int(nodes[idx]))
                que.append(node.left)
            idx +=1

            if nodes[idx]!='None' :
                node.right = TreeNode(int(nodes[idx]))
                que.append(node.right)
            idx +=1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))