from WorkoutPlanner.workout_plan import get_workout_plan
#from DietPlanner.diet_plan import get_diet_plan
from ProgressTracker.progress_tracker import track_progress

def create_fitness_plan():
    # Get individual components of the fitness plan
    workout_plan = get_workout_plan()
    diet_plan = get_diet_plan()
    progress = track_progress()
    
    # Combine everything into a comprehensive plan
    fitness_plan = {
        "workout_plan": workout_plan,
        "diet_plan": diet_plan,
        "progress": progress
    }
    
    return fitness_plan

if __name__ == "__main__":
    # Example usage
    plan = create_fitness_plan()
    print("Your Fitness Plan:")
    print(plan)
