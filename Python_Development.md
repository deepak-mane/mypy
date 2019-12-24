# Python Development
```python ```

## Using conda to manage environments
Although all of these tools share the same broad goals. Some of the differences between these tools are touched on in the Alternatives section.

There are two steps to using an environment (with a third step needed if you want to use Jupyter notebooks)

1. Creating the environment, either from scratch (a new project) or from a yaml file (duplicating an environment)
2. Activating the environment for use.
3. Register the environment with Jupyter.

To leave an environment, we have to deactivate it. The quickstart below will walk through the typical workflow.

### Using an environment (quickstart)
Let's say you wanted to create an environment test_env to do some testing with Python 3.6, and install numpy and Pandas. At the terminal, type the following:

```python
# create the (empty) environment
$ conda create --name test_env python=3.6

# activate the environment
$ source activate test_env

# Now in the new environment, install the packages.
# Note the prompt will (typically) tell you about the environment
(test_env) $ conda install numpy pandas
```
If you want Jupyter notebooks to see your new environment, you need a couple of extra instructions. Jupyter sees the different environments as different kernels. Once we create a new environment, we need to tell Jupyter that it is there:



```python ```
