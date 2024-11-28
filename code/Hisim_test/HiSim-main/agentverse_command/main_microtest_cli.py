import os
import logging
from argparse import ArgumentParser

from agentverse.logging import logger
from agentverse.micro_test import Simulation_Align

parser = ArgumentParser()
parser.add_argument("--task", type=str, default="simulation/prisoner_dilemma")
parser.add_argument(
    "--tasks_dir",
    type=str,
    default=os.path.join(os.path.dirname(__file__), "..", "agentverse", "tasks"),
)
parser.add_argument("--debug", action="store_true")
parser.add_argument("--ckpt_dir", type=str, default=None)
args = parser.parse_args()

logger.set_level(logging.DEBUG if args.debug else logging.INFO)


def cli_main():
    agentverse = Simulation_Align.from_task(args.task, args.tasks_dir, args.ckpt_dir)
    agentverse.run()


if __name__ == "__main__":
    cli_main()
