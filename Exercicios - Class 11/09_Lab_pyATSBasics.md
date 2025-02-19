# Lab 09: Creating and Running a Basic pyATS Test

## Objective:

In this lab, you'll set up the basic structure for a pyATS test and execute it using the provided job and script files.

## Steps

### 1. **Install Required Tools**:
Since `vim` isn't available in the pyATS Docker container, you'll need to install it:
```
apt update
apt install vim -y
```

### 2. **Create the Job File: `basic_example_job.py`**:

Use `vim` to create a new file:
```
vim basic_example_job.py
```

Copy and paste the following content:

```python
# To run the job:
# pyats run job basic_example_job.py
# Description: This example shows the basic functionality of pyATS
# with few passing tests
import os
from pyats.easypy import run

# All run() must be inside a main function
def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(test_path, 'basic_example_script.py')
    # Execute the testscript
    run(testscript=testscript)
```

Save and exit the editor.

### 3. **Create the Test Script: `basic_example_script.py`**:

Again, use `vim` to create the other file:
```
vim basic_example_script.py
```

Copy and paste the following content:

```python
#!/usr/bin/env python
"""
basic_example.py: A very simple test script example which includes:
- common_setup
- Testcases
- common_cleanup

The purpose of this sample test script is to demonstrate the "hello world" of aetest.
"""

# Imports
import logging
from pyats import aetest

# Logger setup
log = logging.getLogger(__name__)

### COMMON SETUP SECTION ###
# This section describes how to create a CommonSetup.
# It's possible to have none or one CommonSetup.
# The name of CommonSetup can be arbitrary.

class common_setup(aetest.CommonSetup):
    """Common Setup section"""

    # Subsections in CommonSetup
    @aetest.subsection
    def sample_subsection_1(self):
        """Common Setup subsection"""
        log.info("Aetest Common Setup")

    @aetest.subsection
    def sample_subsection_2(self, section):
        """Common Setup subsection"""
        log.info(f"Inside {section}")
        log.info(f"Inside class {self.uid}")

### TESTCASES SECTION ###
# This section describes how to create a testcase.
# It's possible to have multiple testcases.

class tc_one(aetest.Testcase):
    """User Testcases section"""
    # Testcase setup
    @aetest.setup
    def prepare_testcase(self, section):
        """Testcase Setup section"""
        log.info("Preparing the test")
        log.info(section)

    # Test sections
    @aetest.test
    def simple_test_1(self):
        """Sample test section"""
        log.info("First test section")

    @aetest.test
    def simple_test_2(self):
        """Sample test section"""
        log.info("Second test section")

    # Testcase cleanup
    @aetest.cleanup
    def clean_testcase(self):
        """Testcase cleanup section"""
        log.info("Pass testcase cleanup")

class tc_two(aetest.Testcase):
    """User Testcases section"""
    
    @aetest.test
    def simple_test_1(self):
        """Sample test section"""
        log.info("First test section")
        self.failed('This is an intentional failure')

    @aetest.test
    def simple_test_2(self):
        """Sample test section"""
        log.info("Second test section")

    @aetest.cleanup
    def clean_testcase(self):
        """Testcase cleanup section"""
        log.info("Pass testcase cleanup")

### COMMON CLEANUP SECTION ###
# This section describes how to create a CommonCleanup.
# It's possible to have none or one CommonCleanup.
# The name of CommonCleanup can be arbitrary.

class common_cleanup(aetest.CommonCleanup):
    """Common Cleanup for Sample Test"""
    
    @aetest.subsection
    def clean_everything(self):
        """Common Cleanup Subsection"""
        log.info("Aetest Common Cleanup")

if __name__ == '__main__':
    aetest.main()
```

Save and exit the editor once done.

### 4. **Run the Test**:

With both the job and script files in place, run the test using the following command:

```
pyats run job basic_example_job.py
```

## Conclusion

Upon executing the above command, pyATS will run the tests specified in the script, and you should observe the log outputs and results of each test case.