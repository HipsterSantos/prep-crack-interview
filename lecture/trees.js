function treeNode(value){
    this.value = value; 
    this.children = []
}


function binaryTreeNode(value){
    this.value = value ; 
    this.left = null; 
    this.right = null;
}

function binaryTree(){
    this._root = null;
}

binaryTreeNode.prototype.preOrderTraverse = function(){
    binaryTreeHelper(this._root);
    function traversePreOrderHelper(node){
        if(!node)return; 
        traversePreOderHelper(this.left);
        traversePreOrderHelper(this.right)
    }
}