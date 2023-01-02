from tqdm import tqdm
import time

def progress_bar():
    """
    Progress bar animation
    adds a progressbar which doesn't really serve a function to the program itself, but it does look cool.
    """
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)
