import os
from pathlib import Path
from invoke import task
from airoh.containers import docker_run, docker_build, docker_archive, docker_setup 

@task
def setup(c):
    """
    Setup all the requirements.
    """
    from airoh.utils import setup_env_python
    setup_env_python(c, "requirements.txt")
    print(f"✨ Setup complete!")

@task
def fetch(c):
    """
    Retrieve all data assets.
    """
    from airoh.datalad import import_file
    import_file(c, "papers")

@task
def run_simulation(c):
    """
    Run a small simulation.
    """
    output_dir = Path(c.config.get("output_data_dir"))
    from code.simulation import simulation
    simulation(output_dir)

@task(pre=[run_simulation])
def run_figure(c):
    """
    Generate figures from the simulation output using a notebook.
    """
    from airoh.utils import run_figures, ensure_dir_exist

    notebooks_dir = Path(c.config.get("notebooks_dir"))
    output_dir = Path(c.config.get("output_data_dir")).resolve()
    source_dir = Path(c.config.get("source_data_dir")).resolve()

    ensure_dir_exist(c, "output_data_dir")
    run_figures(c, notebooks_dir, output_dir, keys=["source_data_dir", "output_data_dir"])

@task(pre=[run_simulation, run_figure])
def run(c):
    print("all analyses completed")

@task
def clean(c):
    """
    Clean the output folder.
    """
    from airoh.utils import clean_folder
    clean_folder(c, "output_data_dir", "*.png")
    clean_folder(c, "output_data_dir", "*.csv")

