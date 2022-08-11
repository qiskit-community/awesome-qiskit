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

* [Main](#main) - The main Qiskit packages maintained by IBM Quantum
* [Community](#community) - Software packages supported by the Qiskit community, not maintained by IBM Quantum
* [Prototypes](#prototypes) - Software packages supporting cutting-edge research on quantum algorithms and applications
* [Partners](#partners) - A select group of providers and vendors that are verified for Qiskit compatibility and validity
* [Extension](#extension) - IBM Quantum supported Qiskit extensions


## Main


* [qiskit-terra](https://github.com/Qiskit/qiskit-terra) - Terra is the foundation on which the rest of qiskit is built.

* [qiskit-aer](https://github.com/Qiskit/qiskit-aer) - Aer provides high-performance quantum computing simulators with realistic noise models.

* [qiskit-optimization](https://github.com/Qiskit/qiskit-optimization) - Qiskit optimization is an open-source framework that covers the whole range from high-level modeling of optimization problems, with automatic conversion of problems to different required representations, to a suite of easy-to-use quantum optimization algorithms that are ready to run on classical simulators, as well as on real quantum devices via qiskit.

* [qiskit-metal](https://github.com/Qiskit/qiskit-metal) - Qiskit metal is an open-source framework for engineers and scientists to design superconducting quantum devices with ease.

* [qiskit-machine-learning](https://github.com/Qiskit/qiskit-machine-learning) - The machine learning package contains sample datasets and quantum ml algorithms.

* [qiskit-nature](https://github.com/Qiskit/qiskit-nature) - Qiskit nature allows researchers and developers in different areas of natural sciences (including physics, chemistry, material science and biology) to model and solve domain-specific problems using quantum simulations.

* [qiskit-finance](https://github.com/Qiskit/qiskit-finance) - Qiskit finance is an open-source framework that contains uncertainty components for stock/securities problems, ising translators for portfolio optimizations and data providers to source real or random data to finance experiments.

* [qiskit-dynamics](https://github.com/Qiskit/qiskit-dynamics) - Qiskit dynamics is an open-source project for building, transforming, and solving time-dependent quantum systems in qiskit.


## Community


* [pyEPR](https://github.com/zlatko-minev/pyEPR) - Qiskit metal e&m analysis with ansys and the energy-participation-ratio method is based on pyepr.

* [c3](https://github.com/q-optimize/c3) - The c3 package is intended to close the loop between open-loop control optimization, control pulse calibration, and model-matching based on calibration data.

* [qiskit-superstaq](https://github.com/SupertechLabs/qiskit-superstaq) - This package is used to access superstaq via a web api through qiskit. qiskit programmers can take advantage of the applications, pulse level optimizations, and write-once-target-all features of superstaq with this package.

* [qtcodes](https://github.com/yaleqc/qtcodes) - Qiskit topological codes.

* [kaleidoscope](https://github.com/QuSTaR/kaleidoscope) - Kaleidoscope.

* [pytket-extensions](https://github.com/CQCL/pytket-extensions) - Repository contains a collection of python extension modules for cqc's pytket quantum sdk.

* [quantuminspire](https://github.com/QuTech-Delft/quantuminspire) - Platform allows to execute quantum algorithms using the cqasm language.

* [mitiq](https://github.com/unitaryfund/mitiq) - Mitiq is a python toolkit for implementing error mitigation techniques on quantum computers.

* [pennylane-qiskit](https://github.com/PennyLaneAI/pennylane-qiskit) - The pennylane-qiskit plugin integrates the qiskit quantum computing framework with pennylane's quantum machine learning capabilities.

* [quantumcat](https://github.com/artificial-brain/quantumcat) - Quantumcat is a platform-independent, open-source, high-level quantum computing library, which allows the quantum community to focus on developing platform-independent quantum applications without much effort.

* [Blueqat](https://github.com/Blueqat/Blueqat) - A quantum computing sdk.

* [python-open-controls](https://github.com/qctrl/python-open-controls) - Q-ctrl open controls is an open-source python package that makes it easy to create and deploy established error-robust quantum control protocols from the open literature.

* [qiskit-rigetti](https://github.com/rigetti/qiskit-rigetti) - Rigetti provider for qiskit.

* [QiskitBot](https://github.com/infiniteregrets/QiskitBot) - A discord bot that allows you to execute quantum circuits, look up the ibmq qiskit's documentation, and search questions on the quantum computing stackexchange.

* [pytorch-quantum](https://github.com/mit-han-lab/pytorch-quantum) - A pytorch-centric hybrid classical-quantum dynamic neural networks framework.

* [QPong](https://github.com/HuangJunye/QPong) - A quantum version of the classic game pong built with qiskit and pygame.


## Prototypes


* [Entanglement forging](https://github.com/qiskit-community/prototype-entanglement-forging) - This module allows a user to simulate chemical and physical systems using a variational quantum eigensolver (vqe) enhanced by entanglement forging. entanglement forging doubles the size of the system that can be exactly simulated on a fixed set of quantum bits.

* [Quantum kernel training](https://github.com/qiskit-community/prototype-quantum-kernel-training) - The quantum kernel training (qkt) toolkit is designed to enable users to leverage quantum kernels for machine learning tasks; in particular, researchers who are interested in investigating quantum kernel training algorithms in their own research, as well as practitioners looking to explore and apply these algorithms to their machine learning applications.

* [Quantum Random Access Optimization](https://github.com/qiskit-community/prototype-qrao) - The quantum random access optimization (qrao) module is designed to enable users to leverage a new quantum method for combinatorial optimization problems.


## Partners


* [qiskit-ibm-runtime](https://github.com/qiskit/qiskit-ibm-runtime) - This module provides the interface to access qiskit runtime.

* [qiskit-ionq](https://github.com/Qiskit-Partners/qiskit-ionq) - Project contains a provider that allows access to ionq ion trap quantum systems.

* [qiskit-ibm-provider](https://github.com/Qiskit/qiskit-ibm-provider) - Project contains a provider that allows accessing the ibm quantum systems and simulators.

* [mthree](https://github.com/Qiskit-Partners/mthree) - Matrix-free measurement mitigation (m3).


## Extension


* [qiskit-alt](https://github.com/Qiskit-Extensions/qiskit-alt) - Python package uses a backend written in julia to implement high performance features for standard qiskit.

* [qiskit-cold-atom](https://github.com/Qiskit-Extensions/qiskit-cold-atom) - This project builds on this functionality to describe programmable quantum simulators of trapped cold atoms in a gate- and circuit-based framework.


