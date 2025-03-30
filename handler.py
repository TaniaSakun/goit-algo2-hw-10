import random
import timeit
import matplotlib.pyplot as plt

# Sorting Algorithms
def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def visualize_results(random_times, deterministic_times, sizes):
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, random_times, marker='o', label='Randomized QuickSort')
    plt.plot(sizes, deterministic_times, marker='x', label='Deterministic QuickSort')
    plt.title('QuickSort Comparison')
    plt.xlabel('Array size')
    plt.ylabel('Execution time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Teacher Scheduling
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    assigned_teachers = []
    while uncovered_subjects:
        best_teacher = max(
            teachers,
            key=lambda t: (len(t.can_teach_subjects & uncovered_subjects), -t.age),
            default=None
        )
        if not best_teacher or not (best_teacher.can_teach_subjects & uncovered_subjects):
            return None
        best_teacher.assigned_subjects = best_teacher.can_teach_subjects & uncovered_subjects
        assigned_teachers.append(best_teacher)
        uncovered_subjects -= best_teacher.assigned_subjects
    return assigned_teachers