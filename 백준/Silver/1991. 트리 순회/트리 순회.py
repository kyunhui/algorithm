import sys 

input = sys.stdin.readline

n = int(input())

# 딕셔너리로 
tree = {}

for i in range(n):
    root, left, right = input().strip().split()
    tree[root] = [left, right]
    
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])  
        
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
        