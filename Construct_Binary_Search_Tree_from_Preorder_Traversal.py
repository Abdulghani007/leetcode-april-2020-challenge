class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        tree = TreeNode(preorder[0])
        del preorder[0]
        for i in range(len(preorder)):
            cur = tree
            while cur != None:
                pre = cur
                if preorder[i]<=cur.val:
                    cur = cur.left
                    ans = "L"
                else:
                    cur = cur.right
                    ans = "R"
            if ans == "R":
                pre.right = TreeNode(preorder[i])
            elif ans == "L":
                pre.left = TreeNode(preorder[i])
        return tree
