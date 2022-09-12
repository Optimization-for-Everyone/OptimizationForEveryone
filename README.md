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
git clone https://github.com/Optimization-for-Everyone/OptimizationForEveryone.git
```
* Install packages using script below. pip must be installed in your environment to execute this script.
```
pip install -r requirements.txt
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
Optimizer: HHO
ObjFucName: ackley
StartTime: 2022-08-23-15-58-59
EndTime: 2022-08-23-15-59-00
ExecutionTime: 1.2919793128967285
Best: 0.8523060992341915
BestIndividual:
[0.07709894 0.09411086 0.19324962 0.02339462 0.10257858 0.0276828
 0.12537082 0.06725648 0.09388774 0.09958472 0.12137024 0.02291474
 0.0975003  0.07889066 0.08116112 0.20592682 0.1061973  0.09311069
 0.12012845 0.08617068 0.07852312 0.12372042 0.08774778 0.07935038
 0.12469214 0.0650703  0.02309113 0.08295719 0.00837619 0.10117705]
```
