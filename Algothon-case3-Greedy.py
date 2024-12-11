from heapq import heappush, heappop
from collections import defaultdict

def schedule_jobs(n, m, jobs, dependencies):
    graph = defaultdict(list)
    in_degree = [0] * n
    job_completion = [0] * n  # Tracks the completion time for each job
    job_order = []  # To track the order of job completions

    # Build graph and compute in-degrees
    for u, v in dependencies:
        graph[u].append(v)
        in_degree[v] += 1
        
    # max-heap for jobs with no dependencies (jobs with longer execution times are prioritized)
    job_queue = []
    for i in range(n):
        if in_degree[i] == 0:
            heappush(job_queue, (-jobs[i], i))  # Negative time for max-heap behavior

    # Min-heap for machine availability (availability_time, machine_id)
    machine_heap = [(0, i) for i in range(m)]
    makespan = 0
    
    # Process jobs
    while job_queue: # O(n)
        # Get the longest job ready to execute
        job_time, job = heappop(job_queue) #O(log(n))

        # Get the earliest available machine
        avail_time, machine_id = heappop(machine_heap) # O(Log(m))

        # Calculate the time the job can start
        # Job can start after the machine is available and after its dependencies are completed
        job_start_time = max(avail_time, job_completion[job])

        # Calculate job finish time
        job_finish_time = job_start_time + jobs[job]

        # Update the job completion time
        job_completion[job] = job_finish_time
            
        # Push the updated machine availability back to the heap
        heappush(machine_heap, (job_finish_time, machine_id)) #O(log(m))

        # Update makespan
        makespan = max(makespan, job_finish_time)

        # Add job to the order of completion
        job_order.append(job)

        # Update dependencies for the completed job
        for dep in graph[job]: # O(e)
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                heappush(job_queue, (-jobs[dep], dep))  # Add new ready job
                
            #To makesure that the job gets assigned after the prerequiste job is done
            #compute the start time of the job with dependency
            job_completion[dep] = max(job_completion[dep], job_completion[job])
            
    return makespan, job_order

# Example usage
if __name__ == "__main__":
    m = 2  # Number of machines
    jobs =  [3, 8, 7, 6, 2, 5, 1, 4, 8, 1]
    dependencies = [(0, 2), (1, 2), (2, 3), (3, 4), (3, 5), (6, 3), (1, 9)]
    n = len(jobs)

    makespan, job_order = schedule_jobs(n, m, jobs, dependencies)
    print("Minimized Makespan:", makespan)
    print("Order of Jobs Completed:", job_order)
