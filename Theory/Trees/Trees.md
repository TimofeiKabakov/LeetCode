## Trees

A **tree** is an undirected graph with no cycles.

Equivalently, a **tree** is a connected graph with N nodes and N - 1 edges.

The **height** of a tree is a number of edges from the root to the lowest leaf.

The **degree** of a node is the number of nodes it is connected to.

**Tree representations:**

- Edge list (fast to iterate over, cheap to store BUT storing a tree as a list lacks the structure to efficiently quarry all the neighbors of a node)
- Adjacency list
- Adjacency matrix (not efficient in terms of memory - O(n^2))

![Alt text](image-2.png)

## Binary Trees

**Binary trees** are trees for which every node has at most two child nodes.

### Depth-first Traversal/Search:

A depth-first traversal starts at the root, and **always visits the children of a visited node before its siblings**. It does not make any guarantees about the order in which nodes on a particular level are visited.

**Pseudocode:**
![Alt text](image-3.png)

**Iterative implementation with stack (js):**
![Alt text](image-4.png)
We can change the order of lines 33 and 34 to get a desired order of depth-first traversal.

**Recursive implementation (js):**
![Alt text](image-5.png)

**Complexity:** O(n)

**Space:** O(n)

### Breadth-first Traversal/Search:

A breadth-first traversal starts at the root, and **always visits all the nodes on the current level of the tree before visiting nodes on the next level**. It does not make any guarantees about the order in which nodes on a particular level are visited.

**Iterative implementation with queue (js):**
![Alt text](image-6.png)

**Complexity:** O(n)

**Space:** O(n)

### Special cases:

1. V: visit the node
2. L: traverse the left subtree of the node
3. R: traverse the right subtree of the node

**Pre-order Traversal:** The pre-order traversal is a special case of the **depth-first traversal**. In the pre-order traversal, we start at the root, and then perform the above operations in the order: **VLR**. That is, every node is visited before both of its subtrees, and then we always traverse the left subtree before the right subtree.

**In-order Traversal:** The in-order traversal performs the traversal operations in the sequence: **LVR**, starting at the root. That is, the left subtree of a node is always traversed before the node is visited, and the right subtree of a node is always traversed after the node is visited. **In-order traversal is neither breadth-first, nor depth-first traversal**.

**Post-order Traversal:** The post-order traversal starts at the root and performs the traversal operations in the sequence: **LRV**. That is, both the left and right subtrees of a node t are traversed before t is visited. Again, this is **neither a breadth-first, nor depth-first traversal**.

## Binary Search Trees (BST)

Binary Search Trees are **trees** which satisfy the **BST invariant** which states that for every node x:

<div align="center">
x.left.value <= x.value <= x.right.value
</div>

## Storing Rooted Trees

Maintain a pointer reference to the **root node**.

Each node has access to a list of its **children**.

Sometimes it is useful to maintain a pointer to a node's **parent node** effectively making edges **bidirectional**.

### Flattened array

If your tree is a **binary tree**, you can store it in a **flattened array** where each node has an assigned index position based on where it is in the tree.

The root node is always at index 0 and the children of the current node i are accessed relative to position i.

![Alt text](image-1.png)

## Theoretical Problems

### Problem 1: Leaf Node Sum

What is the sum of all leaf node values in a tree?

![Alt text](image-7.png)

### Problem 2: Tree Height

Find the height of a binary tree.

![Alt text](image-8.png)

OR

![Alt text](image-9.png)

### Problem 3: Rooting a tree

Sometimes it is useful to root an undirected tree to add structure to the problem you are trying to solve.

You can root a tree using any of its nodes. However, not every node will give you a well-balanced tree.

In some situations, it is also useful to keep a reference to the parent node in order to walk up the tree.

Rooting a tree is easily done with depth-first search (during the traversal).

![Alt text](image-10.png)

![Alt text](image-11.png)

### Problem 4: Tree center(s)

There can be more than one center. But no more than 2.

Notice that the center is always the middle vertex or middle two vertices in every longest path along the tree.

Another approach to find the center is to iteratively pick off each leaf node layer like we are peeling an onion --> identify the leaf nodes by counting the degree of each node and prune them.

![Alt text](image-12.png)

### Problem 5: Identifying Isomorphic Trees

The question of asking whether two graphs G1 and G2 are **isomorphic** is asking whether they are structurally the same.

![Alt text](image-13.png)

We can also define the notion of isomorphism more rigorously:

G1(V1, E1) and G2(V2, E2) are isomorphic if there exists a **bijection** $\varphi$ between the sets V1 -> V2 such that:

![Alt text](image-14.png)

In simple terms, for an isomorphism to exist, there needs to be a function $\varphi$ which can map all the nodes/edges in G1 to G2 and vice-versa.

The method presented here involves **serializing** a tree into a **unique encoding**. This unique encoding is simply a unique string that represents a tree. If another tree has the same encoding, then they are isomorphic.

**For rooted trees:** one caveat to watch out is to ensure that the same root node is selected in both trees when rooting them (Problem 3) before serializing/encoding the trees. Otherwise, you will get two different encodings for isomorphic trees.

To select a common node between both trees, we can use what we learned from finding the center(s) of a tree (Problem 4).

Thus, the steps are:

1. Find the centers of trees
2. Root the trees at their center nodes
3. Generate the encoding for each tree and compare the serialized trees for equality.

The tree encoding is simply a sequence of left and right brackets. However, you can also think of them as 1's and 0's.

It should also be possible to reconstruct the tree solely from the encoding.

The **AHU** (Aho, Hopcroft, Ullman) algorithm is a clever serialization technique for representing a tree as a unique string. AHU is able to capture a complete history of a tree's **degree spectrum** and structure, ensuring a deterministic method of checking for tree isomorphism.

**AHU:**

1. Assign all leaf nodes Knuth tuples: '()'
2. Process all nodes with grayed out children, combine labels of their child nodes and wrap them in brackets. Notice that labels are **sorted** lexicographically when combined before wrapping them in brackets, this is important.
   ![Alt text](image-15.png)
   ![Alt text](image-16.png)
3. You can not process a node until you have processed all its children.
4. Repeat till the root

#### Pseudocode

![Alt text](image-18.png)

![Alt text](image-17.png)
In regards to the second tree's loop: we do not know what center to choose in case the second tree has two centers. Therefore, we try both and compare them to the encoding of the first tree.

![Alt text](image-19.png)

### Problem 6: Lowest Common Ancestor (LCA) Problem | Eulerian path method

The **Lowest Common Ancestor (LCA)** of two nodes `a` and `b` in a **rooted tree** is the _deepest_ node `c` that has both `a` and `b` as descendants (where a node can be a descendant of itself).

Note: the notion of LCA also exists for Directed Acyclic Graphs (DAGs) but here we are only looking at LCA in the context of trees.

![Alt text](image-20.png)

![Alt text](image-21.png)

You can also find LCA of more than 2 nodes.

![Alt text](image-22.png)

#### Eulerian tour + Range Minimum Query (RMQ) method

This method can answer LCA in O(1) time with O(nlogn) pre-processing when using a **Sparse Table** to do the RMQs.

However, the pre-processing time can be improved to O(n) with **Farach-Colton and Bender optimization**.

Given a tree we want to do LCA queries on, first:

1. Make sure the tree is **rooted**.
2. Ensure that all nodes are **uniquely indexed** in some way, so that we can reference them later. One easy way - assigning each node a unique id between [0, n-1].

#### Eulerian Tour (Eulerian circuit):

This method begins by finding an Eulerian tour of the edges in a rooted tree. Rather than doing an Eulerian tour on the white edges of our tree, we are going to do the Euler tour on a new set of imaginary **green edges** which wrap around the tree. This ensures that our tour visits every node in the tree.

![Alt text](image-24.png)

Start at the root node, traverse all green edges, and finally return to the root node. As you do this, keep track of which nodes you visit and this will be your Euler tour.

We also need to keep track of depths while doing the Euler tour:

![Alt text](image-25.png)

What is **LCA(6, 5)** for this example?

1. Find the index position value for the nodes `a` and `b` (5 and 6 respectively). In this example, `a` is at index 10 and `b` is at index 7.
2. Using the depth array, find the index of the minimum value in the range of the indices obtained in step 1. I.e. query the range [7, 10] in the depth array to find the index of the minimum value. This can be done in O(1) with Sparse Table. For this example, the index is `9` with a value of `1`.
3. Using the index obtained in step 2, find the LCA of `a` and `b` in the `nodes` array -> with index 9 found in step 2, retrieve the LCA at `nodes[9]`.

For this example, the answer will be 2.

**Issue:** what do we do with nodes that have more than 1 index in the Euler tour? For instance, node with value `1` from the previous example has two indices: 1 and 3.

There are $2n - 1$ node index position in the Euler tour and only $n$ nodes in total, so a perfect 1 to 1 **inverse mapping** is impossible.

The answer is that it **does not matter**. Any of the inverse index values will do. However, in practice, it is easier to select the **last encountered index** while doing the Euler tour.

To maintain the **inverse mapping**, we are going to keep track of some additional information, namely an inverse map called `map`. We are going to be saving the last encountered index position.

![Alt text](image-26.png)

#### Pseudocode

![Alt text](image-27.png)

![Alt text](image-28.png)

![Alt text](image-29.png)

Pay attention to the second `visit` call after calling `dfs` on the subtree. We do this, since we want to maintain proper tour_index, last, etc numbers.

![Alt text](image-30.png)

[Video: Lowest Common Ancestor (LCA) Problem | Eulerian path method](https://www.youtube.com/watch?v=sD1IoalFomA&list=PLDV1Zeh2NRsDfGc8rbQ0_58oEZQVtvoIc&index=7&ab_channel=WilliamFiset)
