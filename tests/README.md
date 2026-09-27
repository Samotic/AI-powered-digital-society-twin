# Tests

**Status:** Planned. No tests exist yet, because no code has been implemented.

Tests will be written alongside each module as it is implemented, and are planned to use `pytest`.

## Planned test areas

| Area | What the tests will check |
|---|---|
| Population generation | The generator produces a population of the requested size with valid attribute values. |
| Distribution matching | The synthetic population's distributions match the source statistics within agreed tolerances. |
| Agent rules | Each behavioral rule changes agent state as documented, including edge cases. |
| Simulation reproducibility | The same configuration and random seed always produce identical results. |
| Scenario configuration | Valid configurations are accepted and invalid ones are rejected with a clear error. |
| Validation metrics | Goodness-of-fit measures return correct values on small, hand-checked examples. |

Tests will use small, clearly artificial inputs created inside the tests themselves. They will not depend on the instructor's dataset.
