import random

questions = [["Which data structure uses LIFO (Last In, First Out) ordering?","Queue","Stack","Linked List","Tree",2],["What is the time complexity of searching for an element in a balanced binary search tree (BST)?","O(1)","O(log n)","O(n)","O(n log n)",2],["Which sorting algorithm has the best average-case time complexity?","Bubble Sort","Selection Sort","Quick Sort","Insertion Sort",3],["What does a hash function do in a hash table?","Sorts data","Searches for data","Maps a key to an index","Merges data",3],["Which traversal of a binary tree processes the root before its subtrees?","Inorder", "Preorder","Postorder","Level-order",2],["Which of the following data structures is most suitable for implementing recursion?","Stack","Queue","Array","Linked List",1],["What is the worst-case time complexity of Quick Sort?","O(n log n)","O(log n)","O(n)","O(n²)",4],["In a min-heap, what is the relation between a parent node and its children?",
"Parent ≥ Children","Parent ≤ Children","Parent = Children","No relation",2],["Which graph traversal uses a queue and visits nodes level by level?","DFS","BFS","Dijkstra","Bellman-Ford",2],["What is the time complexity to insert an element into a binary search tree (average case)?","O(n)", "O(n log n)", "O(log n)", "O(1)",3],["Which of the following is not a stable sorting algorithm?","Merge Sort", "Insertion Sort", "Quick Sort", "Bubble Sort",3],["Which data structure is used in the implementation of a priority queue?","Stack","Array","Heap","Linked List",3],["In a graph, which algorithm guarantees the shortest path from a single source to all other vertices (no negative weights)?","BFS", "DFS", "Dijkstra", "Kruskal",3],["Which of the following problems can be solved using the sliding window technique?","Shortest Path", "Maximum Subarray Sum", "Graph Coloring", "Topological Sorting",2]]

#Rules of the game

correct_rules = [
    "You gain 1 XP! +1 towards becoming a 1337 coder!",
    "You unlock a coffee voucher — because good code deserves caffeine ☕.",
    "You’re now eligible to fix one production bug... blindfolded! 🐞",
    "Earn a badge: ‘Bug Smasher Level 1’",
    "Prize amount of 1lakh will be in your account by today !"
]

incorrect_rules = [
    "Do 10 push-ups or debug someone else's code. 🏋️‍♂️",
    "Write one line of code without using Stack Overflow. 😱",
    "You must explain Big-O to the next person who walks in. 📈",
    "Get a sticker that says: ‘I tried to binary search a linked list.’",
    "Lose 1 XP. Go back and study trees 🌳."
]

for idx, q in enumerate(questions, 1):
    print(f"\nQuestion {idx}: {q[0]}")
    for i, option in enumerate(q[1:5], 1):
        print(f"{i}) {option}")

    user_answer = input("Enter your answer (1-4): ")
    
    # Validate input
    if not user_answer.isdigit() or int(user_answer) not in range(1, 5):
        print("Invalid input! Counting as incorrect.")
        user_answer = -1
    else:
        user_answer = int(user_answer)
    
    if user_answer == q[5]:
        print("✅ Correct!")
        print(random.choice(correct_rules))
    else:
        print("❌ Incorrect!")
        print(random.choice(incorrect_rules))

"""
1)for idx, q in enumerate(questions, 1):
This line starts a for loop that goes through each item in the list called questions.

questions is a list where each element q is itself a list representing a question.

The enumerate() function adds a counter to the loop:

idx is the counter variable, starting from 1 because of the second argument to enumerate(questions, 1).

q is the current question (a list of question text, options, and correct answer index).

Essentially, this means:
For each question q in questions, do the following, and label it number idx starting from 1

2)print(f"\nQuestion {idx}: {q[0]}")
This prints the current question number and the question text.

f"" means f-string (formatted string) in Python, allowing you to embed variables directly.

\n means a newline, so each question prints with a blank line before it for readability.

q[0] accesses the first element of the question list, which is the text of the question itself.

3)for i, option in enumerate(q[1:5], 1):
This is a nested loop inside the question loop.

q[1:5] slices the question list to get elements from index 1 up to but not including 5.
These correspond to the 4 answer options.

enumerate(..., 1) here:

i is the option number, starting from 1.

option is the actual text of each answer option.

This loop goes through the 4 answer choices for the current question.
4)print(f"{i}) {option}")
This prints each option in a numbered list format.

Again uses an f-string.


"""
