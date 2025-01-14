import asyncio
from clean_data import run_data_explore

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    notebook_path = "notebooks/data_explore.ipynb"
    output_path = "notebooks/outputs/data_explore_executed.ipynb"

    # Execute the notebook and save the output
    run_data_explore(notebook_path, save_output=True, output_path=output_path)
