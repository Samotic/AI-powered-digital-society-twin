# Ethics, Privacy, and Limitations

SocietyTwin is a university research and education project. It is intended for **simulation, exploration, research, testing, and hypothesis generation**. It is **not** a prediction engine for real human behaviour, and it is **not** a representation of real Turkish citizens.

## 1. Boundaries (CONFIRMED project principles)

- **Population-level and research-only.** Results describe synthetic populations and cohorts, not real individuals.
- **Aggregate data.** Populations are generated from official aggregate statistics. No personal data is needed or collected for the MVP.
- **No identity reconstruction.** No attempt is made to reconstruct, match, or approximate any real person.
- **No impersonation.** No persona is presented as a specific real Turkish citizen. As a PROPOSED design rule, personas have codes, not names ([persona-schema.md](persona-schema.md#2-design-rules)).
- **Minimal data.** No unnecessary personal data is stored: no real names, contact details, addresses, or identifiers.
- **Explicit assumptions and uncertainty.** Every attribute has a provenance class, and every result is reported with its validation status and limitations.
- **Reproducibility.** Every population and experiment can be traced to its data, configuration, code version, model, and seed.

## 2. Privacy and legal context

- TÜİK publishes aggregate statistics under the confidentiality rules of Statistics Law No. 5429. The Official Statistics Programme notes that the Personal Data Protection Law No. 6698 (KVKK), Article 28(b), exempts the processing of personal data for purposes such as research, planning, and statistics when the data is made anonymous. SocietyTwin's MVP processes **only published aggregates**, so it does not process personal data.
- Special categories of personal data under KVKK Article 6 (for example ethnic origin, religion, political opinion, health) are **excluded from the schema**, even as synthetic attributes.
- If microdata is ever used, it is accessed only through TÜİK's official procedures, never committed to Git, and never used to create records that resemble real respondents ([data-strategy.md §3](data-strategy.md#3-microdata-not-required-for-the-mvp)).
- LLM providers receive only synthetic persona cards and research instruments, never personal data. Provider data-retention terms are part of the **OPEN DECISION** on provider choice.

## 3. Risks and mitigations

| Risk | Description | Mitigation |
|---|---|---|
| **Bias in source data** | Official statistics have coverage gaps, reference-year mismatches, and sampling error; some groups are measured less precisely. | Record sources and years; report subgroup errors; do not publish results for cells below a documented minimum size. |
| **Representation limits** | A small schema cannot capture the diversity of real people; everything not modelled is invisible. | State what is not modelled in every persona card and report; avoid claims beyond the modelled attributes. |
| **Statistical uncertainty** | Synthetic populations are random draws; small provinces and subgroups are noisy. | Multiple seeds; interval estimates; report small-area results separately. |
| **Modelled dependencies** | Higher-order relationships are modelled from 2–3-way tables, not measured. | Provenance classes; held-out conditional validation; ablation against independent sampling. |
| **Hallucination** | Agents may invent attributes, facts, or experiences not in their persona. | Unknowns statement; structured outputs; attribute self-report checks; rationales treated as generated text, not evidence. |
| **LLM persona stereotyping** | LLMs can exaggerate or caricature group identities ([Cheng et al., 2023](sources.md#core-methodology-sources)) and flatten within-group diversity ([Wang et al., 2025](sources.md#core-methodology-sources)). | No sensitive attributes; stereotype audits of rationales; report within-subgroup variance; no ethnic or religious framing in prompts. |
| **Model opinion bias** | LLMs reflect some populations' opinions more than others ([Santurkar et al., 2023](sources.md#core-methodology-sources); [Durmus et al., 2023](sources.md#core-methodology-sources)); Turkish-language behaviour may differ from English. | Compare with published Turkish aggregates; cross-model checks; report the model with every result. |
| **Fragile results** | Small prompt or format changes can shift outcomes substantially ([Ye et al., 2026](sources.md#core-methodology-sources)). | Robustness audits before drawing conclusions; versioned prompts. |
| **Over-interpretation / misuse** | Results could be presented as predictions of Turkish public opinion or used to justify decisions about groups or individuals. | Mandatory "synthetic, not a prediction" labels on every page and export; intended-use statement in every report; no individual-level outputs. |
| **Limits of synthetic-user research** | Simulated respondents do not replace human studies; MatrAIx itself states that human studies remain necessary before applying conclusions to real populations. | Frame results as hypotheses to be tested with real data. |
| **Data-licence non-compliance** | Reuse terms for some sources are not yet confirmed. | Licence field in the manifest; **OPEN DECISION** until confirmed. |
| **Secrets leakage** | API keys could be exposed. | Keys only in server-side environment variables; `.env` git-ignored; never sent to the browser. |

## 4. Limitations of the MVP (known in advance)

1. The population reproduces only the attributes and cross-tabulations that TÜİK publishes; it is not a full picture of Turkish society.
2. Linked households, social networks, and relationships between people are not modelled in the MVP.
3. Persona agents answer as an LLM conditioned on a short card; their answers are not measurements of real opinions.
4. Experiment validity can only be checked for items with published Turkish aggregates.
5. Counterfactual scenarios cannot be validated against reality because they did not happen.
6. Results depend on the LLM, its version, the prompt template, and the language; they are reported together.

## 5. Required labels

- Every UI page and export with persona output: *"Synthetic personas and AI-generated responses. Not real people. Not a prediction of real behaviour."*
- Every population summary: *"Synthetic population generated from official aggregate statistics (sources listed). Not a census."*
