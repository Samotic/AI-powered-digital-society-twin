# Tests

**Status:** Planned. No tests exist yet, because no code has been written.

The PROPOSED v2 testing strategy is in [report §28](../docs/societytwin-v2-architecture.md#28-testing-strategy). In summary:

| Level | Examples |
|---|---|
| Unit | IPF convergence on small tables; allocation preserves totals; masks respected; metrics match hand-computed values |
| Property-based (Hypothesis) | Totals preserved, zero hard-constraint violations, same seed gives identical output, independence from partition processing order |
| Schema and configuration | Schema, instrument, and experiment configurations validate; invalid ones are rejected |
| Integration | Artificial data → 10K build → validation → cohort → SURVEY experiment with the stub model → results |
| API and frontend | FastAPI contract tests; Vitest component tests |
| Performance | 10K / 100K / 1M benchmarks (manual or scheduled, not in every CI run) |

Rules: no real LLM calls and no real TÜİK data in CI. Small, clearly artificial fixtures live in `tests/fixtures/`.
