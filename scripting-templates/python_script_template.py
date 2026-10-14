#!/usr/bin/env python3
"""
Standard CLI Script Template & Boilerplate
Author: Mohammad Bagus Satrio (https://github.com/bagusa13)
Repository: developer-journal

Description:
    Production-grade template for building robust Python command-line tools.
    Includes typed argument parsing, structured logging, safe interrupt handling,
    and deterministic Unix exit codes.

Usage:
    python python_script_template.py --input input.txt --output result.json -v
"""

import sys
import os
import argparse
import logging
from typing import Optional, List
from datetime import datetime

# --- Exit Code Constants ---
EXIT_SUCCESS = 0
EXIT_GENERAL_ERROR = 1
EXIT_INVALID_USAGE = 2
EXIT_INTERRUPTED = 130


def setup_logger(verbose: bool = False, log_file: Optional[str] = None) -> logging.Logger:
    """Configures structured console and optional file logging."""
    logger = logging.getLogger("ScriptRunner")
    log_level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(log_level)

    # Clean ISO-like timestamp format
    formatter = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)-7s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def parse_arguments() -> argparse.Namespace:
    """Defines and parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Standard CLI Automation Boilerplate by Mohammad Bagus Satrio",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Example: python python_script_template.py -i data.csv -o output.json --dry-run"
    )

    parser.add_argument(
        "-i", "--input",
        required=True,
        type=str,
        help="Path to input target file or directory"
    )
    parser.add_argument(
        "-o", "--output",
        required=False,
        type=str,
        default=None,
        help="Optional path to output file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate execution without writing changes"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable debug logging"
    )
    parser.add_argument(
        "--log-file",
        type=str,
        default=None,
        help="Write logs to a designated log file"
    )

    return parser.parse_args()


def process_task(input_path: str, output_path: Optional[str], dry_run: bool, logger: logging.Logger) -> bool:
    """Core business logic for script execution."""
    logger.info(f"Target path verified: {input_path}")

    if not os.path.exists(input_path):
        logger.error(f"Input path does not exist: {input_path}")
        return False

    if dry_run:
        logger.warning("[DRY-RUN] Simulation mode enabled - no disk modifications will occur.")

    # Simulated processing logic
    logger.debug("Executing preliminary validation checks...")
    file_size = os.path.getsize(input_path) if os.path.isfile(input_path) else 0
    logger.info(f"Processing target (Size: {file_size} bytes)")

    if output_path:
        if dry_run:
            logger.info(f"[DRY-RUN] Would write output to: {output_path}")
        else:
            logger.info(f"Writing results to: {output_path}")
            # Write logic goes here

    logger.info("Task completed successfully.")
    return True


def main() -> int:
    """Main execution entry point."""
    try:
        args = parse_arguments()
    except Exception as err:
        sys.stderr.write(f"Argument parsing error: {err}\n")
        return EXIT_INVALID_USAGE

    logger = setup_logger(verbose=args.verbose, log_file=args.log_file)
    logger.info("Initializing script execution...")

    try:
        success = process_task(
            input_path=args.input,
            output_path=args.output,
            dry_run=args.dry_run,
            logger=logger
        )
        return EXIT_SUCCESS if success else EXIT_GENERAL_ERROR

    except KeyboardInterrupt:
        logger.warning("\nExecution canceled by user (SIGINT). Exiting cleanly.")
        return EXIT_INTERRUPTED
    except Exception as exc:
        logger.critical(f"Unhandled runtime exception: {exc}", exc_info=args.verbose)
        return EXIT_GENERAL_ERROR


if __name__ == "__main__":
    sys.exit(main())
