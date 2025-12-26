"""Main entry point for resume generator."""

import datetime
import logging
from pathlib import Path

import jinja2

from .models import Resume

log = logging.getLogger(__name__)


def date_format(d: datetime.date, format_str: str = "%B %Y") -> str:
    """Format a date."""
    return d.strftime(format_str)


def main(yaml_file: str) -> None:
    """Generate LaTeX resume from YAML file."""
    log.debug("Processing YAML file: %s", yaml_file)
    resume = Resume.parse_file(yaml_file)

    latex_jinja_env = jinja2.Environment(
        block_start_string="((*",
        block_end_string="*))",
        variable_start_string="(((",
        variable_end_string=")))",
        comment_start_string="((=",
        comment_end_string="=))",
        line_statement_prefix="%%",
        line_comment_prefix="%#",
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=False,  # noqa: S701
        loader=jinja2.FileSystemLoader(searchpath=Path.cwd()),
    )

    latex_jinja_env.filters["date_fmt"] = date_format
    template = latex_jinja_env.get_template("template.tex.jinja2")

    log.debug("Writing resume-full.tex")
    with Path("resume-full.tex").open("w", encoding="utf-8") as f:
        f.write(
            template.render(
                condensed=False,
                today=datetime.date.today(),
                hardware=resume.hardware.entries,
                operating_systems=resume.operating_systems.entries,
                applications=resume.applications.entries,
                programming=resume.programming.entries,
                cloud=resume.cloud.entries,
                experience=resume.experience,
                courses=resume.courses,
                education=resume.education,
            )
        )

    log.debug("Writing resume-condensed.tex")
    with Path("resume-condensed.tex").open("w", encoding="utf-8") as f:
        f.write(
            template.render(
                condensed=True,
                today=datetime.date.today(),
                hardware=resume.hardware.entries,
                operating_systems=resume.operating_systems.entries,
                applications=resume.applications.entries,
                programming=resume.programming.entries,
                cloud=resume.cloud.entries,
                experience=resume.experience,
                courses=resume.courses,
                education=resume.education,
            )
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to YAML file for input")
    parser.add_argument(
        "-l",
        "--log-level",
        help="Amount of logging desired.  (default: %(default)s)",
        choices=["debug", "info", "warning", "error", "critical"],
        default="warning",
    )

    args = parser.parse_args()

    log_level_map = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=log_level_map[args.log_level],
    )

    main(args.input_file)
