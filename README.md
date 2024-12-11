# Algothon 2024

## Round 02

We’re super excited to have you all here for an awesome day of coding, problem-solving, and of course, algorithms. This is your chance to flex those brain muscles and show off your skills by developing efficient algorithms to tackle tricky, real-world problems.

### What's Expected from You?

- We’ve got **3 tricky cases** lined up for you. First, select one of those and understand what’s being asked. You have to create an algorithm for the selected case only. Break it down. Draw diagrams. Scribble on your notebook. Whatever works for you.

- Next, use your problem-solving ninja skills to design an algorithm that solves the problem efficiently. You’ll need to think about time complexity and how to make sure your solution runs smoothly even when the inputs get BIG. You can even use any predefined mathematical or statistical algorithms too in any step of your final algorithm. But you should have a clear idea about your approach.

- Once you've got your algorithm, **calculate and explain the time complexity** (think: Big O notation). Remember, the goal is to reduce the time complexity as much as possible, so make sure your algorithm scales well!

- After you crack the solution, **summarize your solution in a 3-page max report**. Be clear, concise, and make sure to explain your thought process, algorithm design, and why you think it’s efficient. Please mention your team name, university name, and the names of your team members on the first page of the report. There is no predefined structure for the report. Use it to show your work as clearly as possible.

- After submitting your report, you’ll present your solution in a **viva session** where you’ll explain how your algorithm works, justify its efficiency, and answer questions about the time complexity. This will be just a 10 to 15-minute viva. Viva date will be scheduled between **12th to 20th of November** according to the convenience of the viva panel and yours.

- You have full freedom to develop the algorithm for the selected case. There is no universally correct or wrong answer for each case. The evaluation will be based on your understanding of the algorithm, the correctness of the work, and the time complexity.

---

### Case A

A large logistics company wants to optimize its delivery routes. The city is represented as a grid with **N intersections** and **M roads** between them. The roads are unidirectional, and each road has a variable traffic delay that changes periodically, but for now, you can assume static traffic delays between any two intersections. The company wants to deliver goods from a **central warehouse (node 1)** to multiple delivery points across the city. 

#### Task:
Design an algorithm to find the shortest delivery time from the central warehouse to **K delivery points**. Ensure the algorithm accounts for traffic delays to minimize the overall delivery time across all deliveries. Your algorithm should be able to handle cases with multiple intersections and roads efficiently.

#### Constraints:
- The grid size can be up to **10⁵ intersections and roads**.
- Each road has a specific traffic delay.
- The company wants an algorithm that minimizes the time complexity as much as possible.

---

### Case B

A tech company needs to schedule **N computational jobs** across **M machines**. Each job has a different execution time, and some jobs have dependencies, meaning one job cannot start until another one finishes. 

#### Task:
Schedule the jobs on the machines in such a way that the total completion time (**makespan**) is minimized.

#### Constraints:
- There are up to **10,000 jobs** and **1,000 machines**.
- Some jobs may have dependencies, making this a **directed acyclic graph (DAG)**.
- The objective is to reduce the overall time while respecting job dependencies and machine constraints.

---

### Case C

A cloud service provider has multiple servers that can be dynamically allocated to incoming tasks. Each task has a different resource requirement (e.g., CPU, memory), and each server has a maximum capacity for these resources. Tasks arrive continuously in real-time, and the system must allocate servers to tasks efficiently without exceeding server capacity and without causing excessive waiting time for tasks.

#### Task:
Design an algorithm to allocate servers to tasks efficiently while ensuring:
1. No server exceeds its capacity.
2. Task waiting time is minimized.

#### Constraints:
- The number of servers is up to **1,000**.
- Tasks can go up to **10⁶**.
- Each server has a fixed resource limit.
- Tasks have varying resource requirements and cannot be split across multiple servers.

---

### Happy Algorithm Crafting!
