# Drone Flight Calculator

CSC 325 Python project for calculating drone active flight time based on payload weight.

## AI-Use Disclosure

Used GitHub Copilot Chat (/tests) to generate the initial unit test skeletons. I reviewed the generated tests and added tests for zero payload, a typical payload, a heavy payload that reaches zero flight time, and a negative weight that raises ValueError. I verified all tests pass with pytest.