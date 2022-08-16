# Optimization for Everyone

## Introduction
* Optimization for Everyone is a tool that you can compare meta-heuristic algorithms 
* It allows you to manipulate paramaters of the algorithms
* In a single graph, plots the rate of convergence up to three algorithms.
* Saves the results to a file for each run.

## Installation 
* We suggest you to use an environment management system such as conda, venv, etc...
* Clone the code from
```
git clone https://github.com/Tlamir/OptimizationForEveryone.git
```
* Install packages using script below. pip must be installed in your environment to execute this script.
```
pip install requirements.txt
```
* Run the the script below on the terminal
```
python main.py
```

## How to Use

* Select at least one algoritm and one function 

<p align="center">
  <img src="https://user-images.githubusercontent.com/75381086/184797832-cb46835f-d160-4d61-9f2e-a3c5b03b5417.png" width="950" height="780">
</p>

* Hit run button and get the convergence plot. It will plot only result of the selected algorithm.
 You can select up to three algorithms to compare or one algorithm for three different parameters.
 
<p align="center">
  <img src="https://user-images.githubusercontent.com/75381086/184797938-6168c1be-a4ef-4f76-8d71-0ff06843dc3f.png" width="950" height="800">
</p>

* The result of comparison  look likes this for ackley function. We have 16 more pre-defined well-known functions.  

<p align="center">
  <img src="https://user-images.githubusercontent.com/75381086/184810790-2a4d1489-6928-4d59-b093-3702ca44c284.png" width="950" height="800">
</p>

* SMA (Slime Mould Algorithm) has different parameters from other algorithms. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/75381086/184812854-0a471eb9-5364-4ea4-8988-5e663f40e3b2.png" width="375" height="290">
  &nbsp; &nbsp; &nbsp; &nbsp;
  <img src="https://user-images.githubusercontent.com/75381086/184812731-a295bb55-51ef-4d40-881c-003d7a8101e0.png" width="375" height="290">
</p>

* To get detailed explanation and formula of the selected function hit the question mark. You can see ackley's detailed information below. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/75381086/184798496-f0d87ac9-35ce-484c-b214-6c381078260c.png" width="950" height="780">
</p>

* You can select custom function to run your custom function. Please be careful about syntax. Only use numpy functions to build your custom function. 
More information: https://numpy.org/doc/stable/reference/index.html#reference

<p align="center">
  <img src="https://user-images.githubusercontent.com/75381086/184800912-46ca4b65-f6f7-4f89-b671-63ce6c75024a.png" width="950" height="780">
</p>

* You can use the following script to understand creating custom function. The following example is ackley function rewritten version using numpy functions.

```
sum(x**2)-20*exp( -0.2*sqrt( sum(x**2) / len(x) )) - exp( sum( cos( 2* pi * x )) / len(x) ) + 20 + exp(1)
```

* After execution is finished, information about results and execution time is written to the output file.

```
Optimizer: SMA
ObjFucName: ackley
StartTime: 2022-08-16-07-21-47
EndTime: 2022-08-16-07-21-51
ExecutionTime: 4.237316370010376
Best: 4.440892098500626e-16
BestIndividual:
[ 1.80356613e-20 -1.39912129e-21 -8.10681734e-22  1.40011247e-15
 -3.88976988e-18  2.16023819e-20  6.29118259e-20 -9.61058569e-23
  3.96714124e-22 -2.41437999e-18 -1.76417470e-19 -1.58269008e-16
 -1.32902467e-22 -9.41617999e-17  4.52735953e-17 -6.79870823e-18
  1.53703202e-17 -1.04426948e-18 -2.60638506e-18 -2.25866131e-18
  8.10218532e-20  3.54562889e-21  8.52042921e-18 -4.75712732e-20
  2.86157885e-20  5.16661293e-17  1.47227889e-17 -3.25729509e-17
 -3.74403011e-21 -1.01430381e-23  6.25834417e-18  5.31243882e-18
  7.80124152e-18  1.47236254e-17  1.74552089e-16 -1.03396889e-18
  8.73908132e-20  6.47569741e-17  2.51628530e-19  1.84929569e-18
  1.11576971e-19  5.80691436e-22 -3.82821786e-19 -1.11263528e-17
 -1.78462064e-18  1.59309301e-18 -1.33162619e-26  8.31706589e-19
 -2.03889429e-18 -2.32761920e-18 -1.69713147e-16 -7.14709630e-21
  2.08979351e-22  3.68957959e-17  1.96590849e-19  3.00580202e-19
 -1.54217834e-22  8.03457844e-21  1.50208643e-19 -3.13245920e-19
 -5.05431232e-18 -3.55669547e-18  1.53332814e-18  2.87136380e-18
 -4.68199454e-19  5.66031364e-16 -2.18314448e-18  7.20554717e-20
 -1.24159793e-20  4.30512044e-16 -7.01425228e-21 -1.93803334e-19
  5.93907121e-19  1.95204283e-17  1.06887170e-19  7.49404507e-22
 -3.71488434e-17  1.29174632e-19  4.01767808e-20  5.82683374e-19
 -1.61900445e-19  7.34795188e-20  5.74721005e-17 -3.89662601e-20
 -1.46320489e-16 -6.74901066e-20  4.43591674e-24  8.27286006e-16
  8.53647069e-19 -1.34661649e-15 -1.95893816e-18 -5.03861728e-18
  1.46821273e-16 -2.01285418e-17 -8.75111361e-19 -3.87351726e-21
 -2.32237506e-20 -2.75509928e-21  5.01753405e-20 -5.42435664e-20]
```
