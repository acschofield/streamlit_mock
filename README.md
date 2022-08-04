# streamlit_mock

Mock of streamlit to allow unit tests

## Background

Our simple streamlit applciation calling a REST API backend grew over time, became not so simple and needed a test suite.
We wrote some Selenium tests, but these are tricky to get right and run relatively slowly.
This package "mocks" most streamlit class to allow "pytest" to be used for testing.

Goals:

* Allow tests to be written using pytest
  
* Tests should run quickly so that multiple edge cases and variants can be tested
  
* Tests should be concise and easy to write

Non-Goals

* Testing streamlit itself (the package removes all dependnecies on the real streamlitk)
  
* Testing that the app uses Streamlit correctly (the package fakes input and records outputs)
  
* To be as complete as an end-to-end Selenium test (Streamlit/web server are out of the loop)

## Limitations

* The "mock" is probably missing some Streamlit calls.

* The "mock" code could probably be simplified using Python magic to remove some of the boilerplate

* If you want to mock the values of input elements, they should all have a "key" value. This may require some application changes but it is not obtrusive and is probably good preactice anyway.

## Usage

The "test" directory contains some very simple Streamlit applications, each with a corresponding test. The tests also
serve as programming examples.

```
$ cd test/simple_calculator
```

then, to run the application under streamlit:

```
$ streamlit run main_simple_calculator.py
```

and to run the test with Streamlit mocked out

```
$ pytest test_simple_calculator.py
```



## Writing tests

See the examples, but the steps are-.

1. import streamlit_mock - this adds itself to the front of the Python "path" so that the real Streamlit will not be used.

2. Create a "test_xxx" function to be executed by "pytest"

3. Set the inputs in `st.session_state`, See the "form_calculator" example to see how form_submit_button's are handled. These do not have a "key".
   
4. Run the streamlit application and get the "results".

5. "results" is a dictionary of lists where the interactions are recorded

6. Assert that the results are as expected. I have found it useful to temporarily print the results during test development to see what is expected/missing and then add asserts to confirm this behavior on future runs. Perhaps this should be added as a pytest option
   
## Tests requiring multiple "run"s

Some tests require that the streamlit application be run more than once to create intermediate results in `session_state`.

In this case, you can follow the following sps (assuminh two "run"s)

1. Create a StreamlitMock and get it's session_state in variable `session_state_1`
2. Set up the input values in `session_state_1`
3. Call "run" on the StreamlitMock object
4. Optionally assert some values in "results"
5. Create a new StreamlitMock and get its session_state in variable `session_state_2`
6. `session_state_2.update(session_state_1)`
7. Set additional input values in `session_state_2` for the second run
8. Call "run" on the second StreamlitMock object
9. Assert the results