from flask import Flask, jsonify, render_template
from DataCollection.data_input import collect_data
from WorkoutPlanner.workout_plan import get_workout_plan
from DietPlanner.diet_plan import get_diet_plan
from AIIntegration.ai_integration import analyze_data
from ProgressTracker.progress_tracker import track_progress
from FitnessPlanner.fitness_planner import create_fitness_plan
from UserInterface.user_interface import get_ui

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')  # Ensure home.html is in the templates folder

@app.route("/collect-data")
def data_collection():
    return jsonify(collect_data())

@app.route("/workout-plan")
def workout_plan():
    return render_template('workout/workout.html')

@app.route('/goal')
def goal():
    return render_template('Goal/goal.html')


@app.route("/home")
def home():
    return render_template('home/home.html')


@app.route("/aichat")
def aichat():
    return render_template('aichat/aichat.html')





@app.route('/diet')
def diet():
    return render_template('Diet/diet.html')  # Ensure path is correct for your other templates

@app.route("/analyze-data")
def analyze():
    sample_data = {"steps": 10000, "calories": 2000}
    return jsonify(analyze_data(sample_data))

@app.route("/track-progress")
def progress():
   return render_template('progressTracker/progress.html')


@app.route("/fitness-plan")
def fitness_plan():
    return jsonify(create_fitness_plan())

@app.route("/ui")
def ui():
    return jsonify(get_ui())

if __name__ == "__main__":
    app.run(debug=True)
