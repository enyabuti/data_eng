"""Week 1 - Day 1: Python Environment Setup and First Script.

This script verifies a basic Python data engineering setup by importing
key libraries, printing a welcome message, formatting user input, and
creating a timestamped output folder.
"""

from __future__ import annotations

import datetime
import os
from importlib import import_module, util
from typing import Final, Iterable

REQUIRED_LIBRARIES: Final[tuple[str, ...]] = ("pandas", "requests")
WELCOME_MESSAGE: Final[str] = "Hello, Data Engineer! Your environment is ready."


def verify_dependencies(libraries: Iterable[str]) -> None:
    """Ensure that the required third-party libraries are available."""
    missing = [name for name in libraries if util.find_spec(name) is None]
    if missing:
        libs = ", ".join(sorted(missing))
        raise ModuleNotFoundError(
            "Missing required libraries: "
            f"{libs}. Install them with 'pip install {libs.replace(', ', ' ')}'."
        )

    for name in libraries:
        import_module(name)


def format_message(name: str) -> str:
    """Return a clean, formatted welcome message for a user."""
    cleaned_name = name.strip().title()
    return f"Welcome {cleaned_name}! Let's build some data pipelines."


def main() -> None:
    """Run the setup script steps."""
    verify_dependencies(REQUIRED_LIBRARIES)
    print(WELCOME_MESSAGE)

    user_name = input("Enter your name: ")
    print(format_message(user_name))

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    folder_name = f"data_output_{current_date}"
    os.makedirs(folder_name, exist_ok=True)

    print(
        f"✅ Folder '{folder_name}' created successfully. You're ready to start coding!"
    )


if __name__ == "__main__":
    main()
