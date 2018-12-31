
![Screenshot](/res/logo/vateslogo.jpg?raw=true width="800")

# Vates Quantum

**Vates** is a simple implementation of Grover's algorithm.
It's using the power of IBM Quantum at backend and power of tkinter on the frontend.
Qiskit is made up elements that work together to enable quantum computing. This element is **Terra** and is the foundation on which the rest of Qiskit is built.

## Installation

I encourage installing Qiskit via the pip tool (a python package manager), which installs all Qiskit elements, including Terra.

```bash
pip install qiskit
```

PIP will handle all dependencies automatically and you will always install the latest (and well-tested) version.
To install from source, follow the instructions in the [contribution guidelines](.github/CONTRIBUTING.rst).

**Also** you need tkinter. I also encourage installing Tkinter via the pip tool.
```bash
pip install tkinter
```
Great, now you are all set! Let's continue with running it.

## Running
All you need to do is cloning this repo and running programGui.py
```bash
python ./programGui.py
```
### Executing code on a real quantum chip
You can also use Qiskit to execute your code on a
**real quantum chip**.
In order to do so, you need to configure Qiskit for using the credentials in
your IBM Q account:

#### Configure your IBMQ credentials

1. Create an _[IBM Q](https://quantumexperience.ng.bluemix.net) > Account_ if you haven't already done so.

2. Get an API token from the IBM Q website under _My Account > Advanced > API Token_.

3. Take your token from step 2, here called `MY_API_TOKEN`, and run:

   ```python
   >>> from qiskit import IBMQ
   >>> IBMQ.save_account('MY_API_TOKEN')
    ```

4. If you have access to the IBM Q Network features, you also need to pass the
   URL listed on your IBM Q account page to `save_account`.

After calling `IBMQ.save_account()`, your credentials will be stored on disk.
Once they are stored, at any point in the future we can load and use them.

## Screenshots
Flow, left to right.
![Screenshot](/res/logo/flow.jpg?raw=true)

## Next Steps

Right now, Grover's Algorithm in this state doesn't make much sense. However,
we can create something useful and practical in upcoming years. I, myself, am not
a real Quantum Researcher, I'm only a hobbyist. Hence, if you spot any problems or
misguidance caused by me, please create an issue so we all can learn more about this unexplored
Quantum realm.

## Authors

Vates created by me, however, Qiskit Terra is the work of [many people](https://github.com/Qiskit/qiskit-terra/graphs/contributors) who contribute
to the project at different levels.
