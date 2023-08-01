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

* [Community](#community) - Software packages supported by the Qiskit community, not maintained by IBM Quantum
* [Main](#main) - The main Qiskit packages maintained by IBM Quantum
* [Extensions](#extensions) - IBM Quantum supported Qiskit extensions


## Community


* [Blueqat](https://github.com/Blueqat/Blueqat) - A quantum computing sdk.

* [qiskit-classroom-converter](https://github.com/KMU-quantum-classroom/qiskit-classroom-converter) - Convert quantum circuits, matrices, and bra-ket strings. this converter includes the following conversion functions: quantum circuit to bra-ket notation, quantum circuit to matrix, matrix to quantum circuit, bra-ket notation to matrix.

* [qiskit-machine-learning](https://github.com/qiskit-community/qiskit-machine-learning) - The machine learning package contains sample datasets and quantum ml algorithms.

* [qiskit-optimization](https://github.com/qiskit-community/qiskit-optimization) - Framework that covers the whole range from high-level modeling of optimization problems, with automatic conversion of problems to different required representations, to a suite of easy-to-use quantum optimization algorithms that are ready to run on classical simulators, as well as on real quantum devices via qiskit.

* [kaleidoscope](https://github.com/QuSTaR/kaleidoscope) - Kaleidoscope.

* [RasQberry](https://github.com/JanLahmann/RasQberry) - Rasqberry is a functional model of ibm quantum system one, and can run qiskit on the integrated raspberry pi.

* [qiskit-cold-atom](https://github.com/qiskit-community/qiskit-cold-atom) - This project builds on this functionality to describe programmable quantum simulators of trapped cold atoms in a gate- and circuit-based framework.

* [pyEPR](https://github.com/zlatko-minev/pyEPR) - Qiskit metal e&m analysis with ansys and the energy-participation-ratio method is based on pyepr.

* [q-kernel-ops](https://github.com/Travis-S-IBM/q-kernel-ops) - Code base on the paper kernel matrix completion for offline quantum-enhanced machine learning [2112.08449](https://arxiv.org/abs/2112.08449).

* [qiskit-nature](https://github.com/qiskit-community/qiskit-nature) - Qiskit nature allows researchers and developers in different areas of natural sciences (including physics, chemistry, material science and biology) to model and solve domain-specific problems using quantum simulations.

* [quantumcat](https://github.com/artificial-brain/quantumcat) - Quantumcat is a platform-independent, open-source, high-level quantum computing library, which allows the quantum community to focus on developing platform-independent quantum applications without much effort.

* [Qiskit Nature PySCF](https://github.com/qiskit-community/qiskit-nature-pyscf) - Qiskit nature pyscf is a third-party integration plugin of qiskit nature and pyscf.

* [purplecaffeine](https://github.com/IceKhan13/purplecaffeine) - Project is aimed to create simple general interface to track quantum experiments, store and search them in an easy way.

* [qiskit-symb](https://github.com/SimoneGasperini/qiskit-symb) - Easy-to-use python package designed to enable symbolic quantum computation in qiskit. it provides the basic tools for the symbolic evaluation of statevectors, density matrices, and unitary operators directly created from parametric qiskit quantum circuits. the implementation is based on the sympy library as backend for symbolic expressions manipulation.

* [pytorch-quantum](https://github.com/mit-han-lab/pytorch-quantum) - A pytorch-centric hybrid classical-quantum dynamic neural networks framework.

* [pennylane-qiskit](https://github.com/PennyLaneAI/pennylane-qiskit) - The pennylane-qiskit plugin integrates the qiskit quantum computing framework with pennylane's quantum machine learning capabilities.

* [qiskit-nature-pyscf-dft-embedding](https://github.com/mrossinek/qiskit-nature-pyscf-dft-embedding) - This repository contains the latest prototype implementation of the qiskit nature + pyscf dft embedding. it is based on the following publication: > max rossmannek, panagiotis kl. barkoutsos, pauline j. ollitrault, ivano tavernelli; > quantum hf/dft-embedding algorithms for electronic structure calculations: scaling up to complex molecular systems. > j. chem. phys. 21 march 2021; 154 (11): 114105.

* [QPong](https://github.com/HuangJunye/QPong) - A quantum version of the classic game pong built with qiskit and pygame.

* [vqls-prototype](https://github.com/QuantumApplicationLab/vqls-prototype) - The variational quantum linear solver (vqls) uses an optimization approach to solve linear systems of equations. the vqls-prototype allows to easily setup and deploy a vqls instance on different backends through the use of qiskit primitives and the runtime library.

* [qiskit-superstaq](https://github.com/SupertechLabs/qiskit-superstaq) - This package is used to access superstaq via a web api through qiskit. qiskit programmers can take advantage of the applications, pulse level optimizations, and write-once-target-all features of superstaq with this package.

* [mitiq](https://github.com/unitaryfund/mitiq) - Mitiq is a python toolkit for implementing error mitigation techniques on quantum computers.

* [diskit](https://github.com/Interlin-q/diskit) - Distributed quantum computing is a concept that proposes to connect multiple quantum computers in a network to leverage a collection of more, but physically separated, qubits. in order to perform distributed quantum computing, it is necessary to add the addition of classical communication and entanglement distribution so that the control information from one qubit can be applied to another that is located on another quantum computer. for more details on distributed quantum computing, see this blog post: [distributed quantum computing: a path to large scale quantum computing](https://medium.com/@stephen.diadamo/distributed-quantum-computing-1c5d38a34c50) in this project, we aim to validate distributed quantum algorithms using qiskit. because qiskit does not yet come with networking features, we embed a "virtual network topology" into large circuits to mimic distributed quantum computing. the idea is to take a monolithic quantum circuit developed in the qiskit language and distribute the circuit according to an artificially segmented version of a quantum processor. the inputs to the library are a quantum algorithm written monolithically (i.e., in a single circuit) and a topology parameter that represents the artificial segmentation of the single quantum processor. the algorithm takes these two inputs and remaps the qiskit circuit to the specified segmentation, adding all necessary steps to perform an equivalent distributed quantum circuit. our algorithm for achieving this is based on the work: [distributed quantum computing and network control for accelerated vqe](https://ieeexplore.ieee.org/document/9351762). the algorithm output is another qiskit circuit with the equivalent measurement statistics but with all of the additional logic needed to perform a distributed version.

* [quantum-tetris](https://github.com/olivierbrcknr/quantum-tetris) - What would happen if you combine tetris with a quantum computer? the winning entry of the quantum design jam from ibm and parsons in october 2021 explores just that!.

* [qBraid](https://github.com/qBraid/qBraid) - The qbraid-sdk is a python toolkit for cross-framework abstraction, transpilation, and execution of quantum programs.

* [qiskit-finance](https://github.com/qiskit-community/qiskit-finance) - Qiskit finance is an open-source framework that contains uncertainty components for stock/securities problems, ising translators for portfolio optimizations and data providers to source real or random data to finance experiments.

* [c3](https://github.com/q-optimize/c3) - The c3 package is intended to close the loop between open-loop control optimization, control pulse calibration, and model-matching based on calibration data.

* [QiskitOpt.jl](https://github.com/psrenergy/QiskitOpt.jl) - Qiskitopt.jl is a julia package that exports a jump wrapper for qiskit-optimization.

* [qiskit-toqm](https://github.com/qiskit-toqm/qiskit-toqm) - Qiskit transpiler routing method using the time-optimal qubit mapping (toqm) algorithm, described in https://doi.org/10.1145/3445814.3446706.

* [qiskit-bip-mapper](https://github.com/qiskit-community/qiskit-bip-mapper) - The repository contains a standalone routing stage plugin to use the bipmapping [routing](https://qiskit.org/documentation/apidoc/transpiler.html#routing-stage) pass. the bip mapping pass solves the routing and [layout](https://qiskit.org/documentation/apidoc/transpiler.html#layout-stage) problems as a binary integer programming (bip) problem. the algorithm used in this pass is described in: g. nannicini et al. "optimal qubit assignment and routing via integer programming." [arxiv:2106.06446](https://arxiv.org/abs/2106.06446).

* [bosonic-qiskit](https://github.com/C2QA/bosonic-qiskit) - Nqi c2qa project to simulate hybrid boson-qubit systems within qiskit.

* [qiskit-metal](https://github.com/qiskit-community/qiskit-metal) - Qiskit metal is an open-source framework for engineers and scientists to design superconducting quantum devices with ease.

* [qiskit-rigetti](https://github.com/rigetti/qiskit-rigetti) - Rigetti provider for qiskit.

* [QiskitBot](https://github.com/infiniteregrets/QiskitBot) - A discord bot that allows you to execute quantum circuits, look up the qiskit's documentation, and search questions on the quantum computing stackexchange.

* [quantuminspire](https://github.com/QuTech-Delft/quantuminspire) - Platform allows to execute quantum algorithms using the cqasm language.

* [qiskit-ionq](https://github.com/Qiskit-Partners/qiskit-ionq) - Project contains a provider that allows access to ionq ion trap quantum systems.

* [sat-circuits-engine](https://github.com/ohadlev77/sat-circuits-engine) - A python-qiskit-based package that provides capabilities of easily generating, executing and analyzing quantum circuits for satisfiability problems according to user-defined constraints. the circuits being generated by the program are based on grover's algorithm and its amplitude-amplification generalization.

* [QuantumCircuits.jl](https://github.com/Adgnitio/QuantumCircuits.jl) - Quantumcircuits is an open-source library written in julia for working with quantum computers at the application level, especially for quantum finance and quantum machine learning. it allows to creation and manipulation of the quantum circuits and executes them in julia or convert them to qiskit python object. the library also contains the quantum binomial tree implementation for derivative pricing.

* [dsm-swap](https://github.com/qiskit-community/dsm-swap) - A doubly stochastic matrices-based approach to optimal qubit routing.

* [spinoza](https://github.com/smu160/spinoza) - Spinoza is a quantum state simulator (implemented in rust) that is one of the fastest open-source simulators. spinoza is implemented using a functional approach. additionally, spinoza has a `quantumcircuit` object-oriented interface, which partially matches qiskit's interface. spinoza is capable of running in a myriad of computing environments (e.g., small workstations), and on various architectures. at this juncture, spinoza only utilizes a single thread; however, it is designed to be easily extended into a parallel version, as well as a distributed version. the paper associated with spinoza is available [here](https://arxiv.org/pdf/2303.01493.pdf).

* [python-open-controls](https://github.com/qctrl/python-open-controls) - Q-ctrl open controls is an open-source python package that makes it easy to create and deploy established error-robust quantum control protocols from the open literature.

* [pytket-qiskit](https://github.com/CQCL/pytket-extensions/tree/develop/modules/pytket-qiskit) - An extension to pytket (a python module for interfacing with cqc tket) that allows pytket circuits to be run on ibm backends and simulators, as well as conversion to and from qiskit representations.

* [zoose-codespace](https://github.com/ianhellstrom/zoose-codespace) - Github codespace template repository based on zoose quantum, a custom docker image with everything included, so you can be up and running with any of the major quantum libraries (incl. qiskit) with only two clicks! no installation required. ideal for beginners or people who want to code quantum circuits on the go. code quantum circuits straight in your browser with vscode.

* [qtcodes](https://github.com/yaleqc/qtcodes) - Qiskit topological codes.


## Main


* [qiskit-ibm-provider](https://github.com/Qiskit/qiskit-ibm-provider) - Project contains a provider that allows accessing the ibm quantum systems and simulators.

* [OpenQASM](https://github.com/openqasm/openqasm) - Openqasm is an imperative programming language designed for near-term quantum computing algorithms and applications. quantum programs are described using the measurement-based quantum circuit model with support for classical feed-forward flow control based on measurement outcomes.

* [qiskit-aer](https://github.com/Qiskit/qiskit-aer) - Aer provides high-performance quantum computing simulators with realistic noise models.

* [qiskit-ibm-runtime](https://github.com/qiskit/qiskit-ibm-runtime) - This module provides the interface to access qiskit runtime.


## Extensions


* [mthree](https://github.com/Qiskit-Partners/mthree) - Matrix-free measurement mitigation (m3).

* [Quantum Random Access Optimization](https://github.com/qiskit-community/prototype-qrao) - The quantum random access optimization (qrao) module is designed to enable users to leverage a new quantum method for combinatorial optimization problems.

* [qiskit-experiments](https://github.com/Qiskit-Extensions/qiskit-experiments) - Qiskit experiments is an open-source project for running characterizing, calibrating, and benchmarking experiments in qiskit.

* [qiskit-research](https://github.com/qiskit-community/qiskit-research) - This project contains modules for running quantum computing research experiments using qiskit and the ibm quantum services, demonstrating by example best practices for running such experiments.

* [qiskit-dynamics](https://github.com/Qiskit-Extensions/qiskit-dynamics) - Dynamics is an open-source project for building, transforming, and solving time-dependent quantum systems in qiskit.

* [quantum-serverless](https://github.com/Qiskit-Extensions/quantum-serverless) - The quantum serverless package aims to allow developers to easily offload computations to cloud resources, without being experts in packaging code for remote execution environments.

* [circuit-knitting-toolbox](https://github.com/Qiskit-Extensions/circuit-knitting-toolbox) - Circuit knitting is the process of decomposing a quantum circuit into smaller circuits, executing those smaller circuits on a quantum processor(s), and then knitting their results into a reconstruction of the original circuit's outcome. circuit knitting includes techniques such as entanglement forging, circuit cutting, and classical embedding. the circuit knitting toolbox (ckt) is a collection of such tools.

* [qiskit-alt](https://github.com/Qiskit-Extensions/qiskit-alt) - Python package uses a backend written in julia to implement high performance features for standard qiskit.

* [Entanglement forging](https://github.com/qiskit-community/prototype-entanglement-forging) - This module allows a user to simulate chemical and physical systems using a variational quantum eigensolver (vqe) enhanced by entanglement forging. entanglement forging doubles the size of the system that can be exactly simulated on a fixed set of quantum bits.

* [Quantum kernel training](https://github.com/qiskit-community/prototype-quantum-kernel-training) - The quantum kernel training (qkt) toolkit is designed to enable users to leverage quantum kernels for machine learning tasks; in particular, researchers who are interested in investigating quantum kernel training algorithms in their own research, as well as practitioners looking to explore and apply these algorithms to their machine learning applications.

* [qiskit-qec](https://github.com/qiskit-community/qiskit-qec) - Framework for quantum error correction is an open-source framework for developers, experimentalist and theorists of quantum error correction (qec).


