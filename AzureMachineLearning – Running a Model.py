import os
from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment

# Connect to Azure ML Workspace
workspace = Workspace.from_config(path="<PATH_TO_CONFIG_FILE>")  # Use your config path or parameters
experiment = Experiment(workspace, "example_experiment")

# Define environment and script
env = Environment.from_conda_specification(name="example_env", file_path="environment.yml")
src = ScriptRunConfig(source_directory="path/to/code", script="train.py", environment=env)

# Submit the experiment run
run = experiment.submit(src)
print("Running experiment...")

# Wait for the run to complete and get results
run.wait_for_completion(show_output=True)
print("Run completed. Results:", run.get_metrics())
