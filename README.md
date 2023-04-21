# Call Center Simulator

A basic project for practicing multithreading in Python.

## Description

### The Call Center

* There are `n` operators available in the call center.
* A number of callers are waiting in the queue.
* Each call is categorized as either customer service, technical support, or sales support.
* Operators start handling the callers until there are none left.

### Operator

* While there is at least one caller left, the operator answers a call. Each call will take a specific amount of time depending on its category:
  * Customer service: 0.3 seconds
  * Technical support: 0.5 seconds
  * Sales support: 0.2 seconds
* If the call signal is weak, it will be 0.1 seconds longer.
* Then the operator directs the caller to fill the survey and starts taking a 0.1 second break.
* If the operator has worked longer than 1 second (since the last extended break), he/she will need an extended break which is 0.5 seconds longer than a typical break.
* After his/her return, the operator will resume handling callers.

### Caller

* After filling the survey, which will take 0.1 seconds, the caller can optionally send a feecback which will take 0.2 seconds.
* Finally, the caller ends the call.
