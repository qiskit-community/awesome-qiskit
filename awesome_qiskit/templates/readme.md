<!--lint ignore double-link-->

# Awesome Qiskit [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![ecosystem](https://img.shields.io/badge/Qiskit-Ecosystem-blueviolet) 

<!--lint enable double-link-->

<br />
<p align="center">
  <p align="center">
    <a href="https://qiskit.org/">
      <img alt="Qiskit" src="https://qiskit.org/images/qiskit-logo.png" width="70" />
    </a>
  </p>
  <h3 align="center">Awesome Qiskit</h3>
</p>

[Qiskit](https://qiskit.org/) is an open-source SDK for working with quantum computers at the level of pulses, circuits, and application modules.

This repository is an awesome list of projects, tools, utilities, libraries and tutorials from a broad community of developers and researchers.

## Contents

{% for tier, projects in members.items() -%}
* [{{ tier }}](#{{ tier.lower() }}) - {{ tiers[tier] }}
{% endfor %}

{% for tier, projects in members.items() -%}
## {{ tier }}

{% for project in projects.values() -%}
{% if project.description[-1] == "." %}
* [{{ project.name }}]({{ project.url }}) - {{ project.description | capitalize }}
{% else %}
* [{{ project.name }}]({{ project.url }}) - {{ project.description | capitalize }}.
{% endif %}
{%- endfor %}

{% endfor %}