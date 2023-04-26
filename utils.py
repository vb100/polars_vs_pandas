"""
This collections of functions and procedures supports the main testing script
test.py to compare Polars and Pandas modules. The following functions performs
calculation of average working duration, delivers results to terminal window
and display results on graphs.
"""

# Import modules and packages
import numpy as np
import timeit
from matplotlib import pyplot as plt

# Supporting functions
def test_it(setup: str, statement: str, R: int, N: int) -> list:
    """
    Test specific function and return durations in generated list.
    """

    t = timeit.repeat(setup=setup,
                      stmt=statement,
                      repeat=R,
                      number=N)
    return t


def show_results(dur_pd: list, dur_pl: list, test_name:str) -> None:
    """
    Show results directly in terminal windows (average durations and standard
    deviation)
    """

    if dur_pd > dur_pl:
        winner = 'Polars'
    else:
        winner = 'Pandas'

    print(f'| Test name: {test_name}')
    print(f'|   Average duration (Pandas): {np.round(np.mean(dur_pd), 3)}, Std: {np.round(np.std(dur_pd), 3)}')
    print(f'|   Average duration (Polars): {np.round(np.mean(dur_pl), 3)}, Std: {np.round(np.std(dur_pl), 3)}')
    print(f'|   --> {winner} is faster {np.round(np.max([np.mean(dur_pd), np.mean(dur_pl)]) / np.min([np.mean(dur_pl), np.mean(dur_pd)]), 2)} times.')
    print('-'*10)

    return None


def show_graph(dur_pd : list, dur_pl: list, text_name:str) -> None:
    """
    Showing a histogram representing duration of a given function to perform for
    both Pandas and Polar modules.
    """
    names = ['Pandas', 'Polar']
    avg_pd, avg_pl = np.mean(dur_pd), np.mean(dur_pl)
    _ = plt.bar(x=names[0], height=avg_pd,
                edgecolor='black',
                linewidth=5,
                alpha=0.8,
                fill=True,
                color=['#154c79'],
                label=f'{names[0]} = {np.round(np.mean(dur_pd), 2)} s')
    _ = plt.bar(x=names[1], height=avg_pl,
                edgecolor='black',
                linewidth=5,
                alpha=0.8,
                fill=True,
                color=['#4454c7'],
                label=f'{names[1]} = {np.round(np.mean(dur_pl), 2)} s')
    _ = plt.title(text_name, fontsize=12)
    _ = plt.grid(which='major', color='black', linestyle='--', alpha=0.5)
    _ = plt.xlabel('Python module', fontsize=11)
    _ = plt.ylabel('Duration [s]', fontsize=11)
    _ = plt.legend(shadow=True)
    plt.show()

    return None


def evaluate_and_show(setup_pd: str, setup_pl,
                      stmt_pd: str, stmt_pl,
                      R: int, N: int, test_name: str) -> None:
    """
    Orchestrate statement evaluation and show results in terminal and in barchart.
    """
    t_pandas = test_it(setup=setup_pd, statement=stmt_pd, R=R, N=N)
    t_polars = test_it(setup=setup_pl, statement=stmt_pl, R=R, N=N)
    show_results(dur_pd=t_pandas, dur_pl=t_polars, test_name=test_name)
    show_graph(dur_pd=t_pandas, dur_pl=t_polars, text_name=test_name)

    return None
