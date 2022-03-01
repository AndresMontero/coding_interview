# Data-Structures-and-Algorithms

## Big - O Notation
| Notation | Name |
| ------------- | ------------- |
| O(1) | Constant |
| O(logn) | Logarithmic |
| O(n) | Linear |
| O(nlogn) | n log-star n |
| O(n^2) | Quadratic |

## Array
| Operation  | Time Complexity |
| ------------- | ------------- |
| Retrieve with index.   | O(1) - Constant time |
| Retrieve without index.  | O(n) - Linear time |
| Add an element to full array. | O(n) - Linear time | 
| Add an element to the end of an array. (has space) | O(1) - Constant time |
| Insert or update an element at a specific index. | O(1) - Constant time |
| Delete an element by setting it to null. | O(1) - Constant time | 
| Delete an element by shifting elements. | O(n) - Linear time |

## Performance analysis of Data Structures

### Array
| Operation  | Time Complexity |
| ------------- | ------------- |
| Indexcing | O(1)|
| Insert/Delete at begining | O(n) you need to copy values to increase size |
| Insert/Delete at end | O(1) - amortized|
| Insert/Delete in the middle | O(n)|



### LinkedList
| Operation  | Time Complexity |
| ------------- | ------------- |
| Indexcing | O(n)|
| Insert/Delete at begining | O(1) you only change the pointer |
| Insert/Delete at end | O(n)|
| Insert/Delete in the middle | O(n)|

### Hash Table
| Operation  | Time Complexity |
| ------------- | ------------- |
| Look up by key | O(1) on average|
| Insert/Delete | O(1) on average |



### Stack
LIFO (Last-in-first-out)

| Operation  | Time Complexity |
| ------------- | ------------- |
| Push/Pop | O(1) |
| Search Element by value | O(n) |

Can implement with list or collections.deque or queue.LifoQueue
.pop() last value of the list 

### Queue
FIFO (First-in-first-out)

| Operation  | Time Complexity |
| ------------- | ------------- |
| Push/Pop | O(1) |
| Search Element by value | O(n) |

collections.dequeue or list 


### Binary Search Tree ( BST )

| Operation  | Time Complexity |
| ------------- | ------------- |
| Insertion | O(logn) |
| Deletion | O(logn) |
| Retrieval | O(logn) |

* in order: left, root, right
* post order: left, right, root
* pre order: root, left, right

![Alt text](./static/data_structures_big_o.png?raw=true "Title")



## Search Algorithms

### Linear Search

| Operation  | Time Complexity |
| ------------- | ------------- |
| Search | O(n) |

### Binary Search

| Operation  | Time Complexity |
| ------------- | ------------- |
| Search | O(logn) |


## Time Complexities of all Sorting Algorithms
### Bubble Sort
| Performance  | Time Complexity |
| ------------- | ------------- |
| Worst Case | O(n^2) - Quadratic time |
| Avarage Case | O(n^2) - Quadratic time |
| Best Case | O(n) - Linear time |

### Selection Sort
| Performance  | Time Complexity |
| ------------- | ------------- |
| Worst Case | O(n^2) - Quadratic time |
| Avarage Case | O(n^2) - Quadratic time |
| Best Case | O(n^2) - Quadratic time |

### Insertion Sort
| Performance  | Time Complexity |
| ------------- | ------------- |
| Worst Case | O(n^2) - Quadratic time |
| Avarage Case | O(n^2) - Quadratic time |
| Best Case | O(n) - Linear time |

### Shell Sort
| Performance  | Time Complexity |
| ------------- | ------------- |
| Worst Case | O(n^2) - Quadratic time |
| Avarage Case | O(nlogn) - n log-star n |
| Best Case | O(nlogn) - n log-star n |

### Merge Sort
| Performance  | Time Complexity |
| ------------- | ------------- |
| Worst Case | O(nlogn) - n log-star n |
| Avarage Case | O(nlogn) - n log-star n |
| Best Case | O(nlogn) - n log-star n |

### Quick Sort
| Performance  | Time Complexity |
| ------------- | ------------- |
| Worst Case | O(n^2) - Quadratic time |
| Avarage Case | O(nlogn) - n log-star n |
| Best Case | O(nlogn) - n log-star n |

### Counting Sort
| Performance  | Time Complexity |
| ------------- | ------------- |
| Worst Case | O(n+k) |
| Avarage Case | O(n+k) |
| Best Case | O(n+k) |

### Radix Sort
| Performance  | Time Complexity |
| ------------- | ------------- |
| Worst Case | O(kn) |
| Avarage Case | O(kn) |
| Best Case | O(kn) |

![Alt text](./static/algorithms_big_o.png?raw=true "Title")
