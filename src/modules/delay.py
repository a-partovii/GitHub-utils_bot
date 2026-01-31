import time
import random
from rich.console import Console
console = Console()

def delay(min=1, max=4):
    try:
        delay = random.randint(min, max)
        with console.status(f"Waiting for delay: {delay} secends"):
            time.sleep(delay)
    # Error handeling
    except (TypeError, ValueError):
        min = int(min) if str(min).isdigit() else 1
        max = int(max) if str(max).isdigit() else 4
        if min < 0: min = 0
        if max <= min: max = min + 1

        delay(min, max)
# -----------------------

def gap_handler(gap, variance_ratio=0.25):
    if gap <= 1:
        return 1
    gap_min = round(gap * variance_ratio - gap)
    gap_max = round(gap * variance_ratio + gap)
    return random.randint(gap_min, gap_max)

gap = 0
run_count = 0
def super_delay(min=10, max=50, gap_og=8):
    global run_count, gap
    run_count += 1
    if gap == 0 :
        gap = gap_handler(gap_og, variance_ratio=0.25)
    
    if run_count == gap:
        delay(min, max)
        gap = gap_handler(gap_og, variance_ratio=0.25)
        run_count = 0
 # ---------------------------

def delay_and_super_delay(min, max, super_min, super_max, super_gap):
    delay(min, max)
    super_delay(super_min, super_max, super_gap)


