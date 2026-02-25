# AI Tool Usage Documentation

## AI Tools Used

The following AI tools were used during the development of this project:

- ChatGPT (OpenAI)
- Claude (Anthropic)

These tools were used as supporting assistants for verification, documentation, and conceptual clarification.

---

## How AI Tools Were Used

AI tools were used in the following ways:

- Verifying the correctness of preprocessing, feature engineering, and inference pipeline logic
- Assisting in improving documentation such as REPORT.md and README.md
- Clarifying concepts related to anomaly detection and Isolation Forest
- Suggesting improvements in project structure and organization
- Reviewing feature engineering ideas and helping refine explanations

The core implementation, feature engineering design, model training, and anomaly detection pipeline were developed independently, with AI used mainly for review and validation.

---

## Tasks Where AI Was Helpful

AI tools were particularly helpful in:

- Improving clarity and structure of documentation
- Explaining theoretical concepts behind Isolation Forest and anomaly detection
- Suggesting improvements in feature engineering approaches
- Helping refine the inference pipeline structure
- Providing feedback on project organization and reporting

These suggestions helped improve code quality and documentation clarity.

---

## Areas Where AI Struggled

AI tools sometimes provided generic recommendations that did not fully align with the specific dataset characteristics or project requirements. For example:

- Some anomaly detection evaluation suggestions assumed labeled anomaly data, which was not available in this project.
- Certain threshold-based approaches suggested by AI required adjustment based on actual physical relationships in the charging data.
- AI did not always accurately account for the behavior of Isolation Forest when abnormal values formed small clusters instead of being isolated immediately.

These limitations required careful manual review and independent analysis to ensure the correctness and reliability of the final implementation.

---

## Validation of AI-Generated Code and Suggestions

All AI-assisted suggestions were manually reviewed and validated before being included in the project.

Validation steps included:

- Running and testing the anomaly detection pipeline on real data
- Verifying that detected anomalies corresponded to physically abnormal behavior
- Ensuring consistency between feature engineering and inference pipeline
- Confirming correctness of model predictions through visualization and inspection

Only verified and validated code was used in the final project.

---

## Summary

AI tools were used responsibly as development aids for verification, documentation, and conceptual clarification. Final implementation decisions, feature engineering, model training, and evaluation were performed independently, with AI serving as a supporting tool rather than the primary developer.