from handler import *

if __name__ == '__main__':
    # QuickSort Performance Comparison
    sizes = [10_000, 50_000, 100_000, 500_000]
    times_randomized = []
    times_deterministic = []
    repeats = 5
    
    for size in sizes:
        arr = [random.randint(1, 10**3) for _ in range(size)]
        t_rand = timeit.timeit(lambda: randomized_quick_sort(arr), number=repeats)/repeats
        times_randomized.append(t_rand)
        
        t_det = timeit.timeit(lambda: deterministic_quick_sort(arr), number=repeats)/repeats
        times_deterministic.append(t_det)
    
    print("Test results (sec):")
    print(f"{'Size':<10}{'Randomized':<20}{'Deterministic':<20}")
    for i in range(len(sizes)):
        print(f"{sizes[i]:<10}{times_randomized[i]:<20.6f}{times_deterministic[i]:<20.6f}")
    
    visualize_results(times_randomized, times_deterministic, sizes)

    # Teacher Scheduling
    subjects = {'Mathematics', 'Physics', 'Chemistry', 'Informatics', 'Biology'}
    teachers = [
        Teacher("Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {'Mathematics', 'Physics'}),
        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {'Chemistry'}),
        Teacher("Serhiy", "Kovalenko", 50, "s.kovalenko@example.com", {'Informatics', 'Mathematics'}),
        Teacher("Natalia", "Shevchenko", 29, "n.shevchenko@example.com", {'Biology', 'Chemistry'}),
        Teacher("Dmytro", "Bondarenko", 35, "d.bondarenko@example.com", {'Physics', 'Informatics'}),
        Teacher("Olena", "Hrytsenko", 42, "o.grytsenko@example.com", {'Biology'})
    ]
    
    schedule = create_schedule(subjects, teachers)
    if schedule:
        print("Schedule:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} years old, email: {teacher.email}")
            print(f"   Teaching: {', '.join(teacher.assigned_subjects)}")
    else:
        print("Not enough teachers to cover all subjects.")