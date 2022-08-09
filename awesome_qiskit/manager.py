"""Awesome list generator entrypoint."""
import json
import os

import requests
from jinja2 import Environment, PackageLoader, select_autoescape
from requests import RequestException

URL_ECOSYSTEM_MEMBERS = (
    "https://raw.githubusercontent.com/qiskit-community/"
    "ecosystem/main/ecosystem/resources/members.json"
)
URL_ECOSYSTEM_TIERS = (
    "https://raw.githubusercontent.com/qiskit-community/"
    "ecosystem/main/ecosystem/resources/tiers.json"
)


class Manager:
    """Class to manage cli commands."""

    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("awesome_qiskit"), autoescape=select_autoescape()
        )
        self.readme_template = self.env.get_template("readme.md")
        self.rootdir = os.path.abspath(os.getcwd())

    def generate_readme(self):
        """Generates readme file."""

        # get ecosystem projects
        ecosystem_members_response = requests.get(URL_ECOSYSTEM_MEMBERS)
        ecosystem_tiers_response = requests.get(URL_ECOSYSTEM_TIERS)

        if ecosystem_members_response.ok and ecosystem_tiers_response.ok:
            members = json.loads(ecosystem_members_response.text)
            tiers = json.loads(ecosystem_tiers_response.text)

            readme_content = self.readme_template.render(
                tiers={tier["name"]: tier["description"] for tier in tiers},
                members=members,
            )
            with open(f"{self.rootdir}/README.md", "w") as file:
                file.write(readme_content)
        else:
            raise RequestException(
                "There an error occurred during fetching information from ecosystem:"
                "\n-%s\n-%s",
                ecosystem_tiers_response.text,
                ecosystem_tiers_response.text,
            )
