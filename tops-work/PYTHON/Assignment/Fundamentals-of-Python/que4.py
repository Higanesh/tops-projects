"""
Que4. How memory is managed in Python?  

Ans-> In Python, memory management is handled automatically through a combination of reference counting, garbage collection, and memory pooling mechanisms.

a) Reference Counting
    Python uses reference counting to track how many references point to an object in memory. When an object’s reference count drops to zero, the memory occupied by that object is automatically freed.

b) Garbage Collection (GC)
    Python has a garbage collector to clean up circular references that reference counting alone can’t handle. Python uses the Generational Garbage Collector for this.

c) Memory Pooling and Optimization
    Python internally reuses small objects (like integers and strings) to save memory.
"""