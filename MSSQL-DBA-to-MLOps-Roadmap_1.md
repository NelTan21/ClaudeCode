# Roadmap: Infrastructure MSSQL DBA → MLOps Engineer

**Objective of this document:** Give you a phased, gap-based transition plan that leverages your existing DBA/infrastructure background instead of treating you as a blank-slate beginner. Use this as a living checklist — re-run the gap assessment every 4-6 weeks as you close items.

**Focus points while executing this roadmap:**
- Your DBA background is a genuine accelerant for MLOps, not a detour — lean into it (see Section 2).
- Be cautious of: (a) over-investing in ML *theory* at the expense of *operations* skills — MLOps hiring managers screen for production/pipeline competence, not modeling depth; (b) certification-only prep without hands-on lab time, which shows up immediately in interviews.
- Stage you're in: **Requirements gathering / idea phase** — this roadmap starts at Phase 0 accordingly.

---

## 1. Hierarchy of the Transition (Top-Down View)

| Level | Layer | What It Covers |
|---|---|---|
| L0 | **Foundations Gap Assessment** | Where your DBA skills already transfer vs. true gaps |
| L1 | **Programming & ML Literacy** | Python fluency, ML lifecycle concepts, model evaluation basics |
| L2 | **Cloud & MLOps Tooling** | AWS SageMaker, containers, orchestration, IaC |
| L3 | **Pipeline & Deployment Engineering** | CI/CD for ML, model registries, automated retraining |
| L4 | **Production Operations & Monitoring** | Drift detection, rollback, observability, governance |
| L5 | **Certification & Portfolio Proof** | AWS ML Engineer – Associate, GitHub portfolio, projects |
| L6 | **Market Entry** | Resume repositioning, targeting, interview prep |

Each level below is a **workflow stage**, not a rigid gate — L1 and L2 run in parallel once L0 is done.

---

## 2. Phase 0 — Foundations Gap Assessment (Objective: know exactly what transfers vs. what's net-new)

**Objective:** Avoid wasting study time relearning things you already know as a DBA, and avoid underestimating gaps in software engineering practice.

### 2a. Skill Transfer Map (DBA → MLOps)

| Your Existing DBA Skill | MLOps Equivalent | Transfer Strength |
|---|---|---|
| Backup/restore, point-in-time recovery | Model versioning & rollback strategy | High — same discipline, different artifact |
| Index/query performance tuning | Inference latency & throughput optimization | High — same diagnostic mindset |
| HA/DR (Always On, clustering) | High-availability model serving endpoints | High |
| Job scheduling (SQL Agent) | Pipeline orchestration (Airflow/Step Functions) | Medium-High — concept transfers, tool is new |
| Monitoring (perf counters, alerts) | Model/data drift monitoring, observability stacks | Medium — same instinct, new metrics (accuracy/drift vs. IOPS/latency) |
| Security/permissions/compliance | ML governance, responsible AI, data privacy | Medium |
| T-SQL scripting | Python for automation | **Low — this is your primary net-new skill** |
| ETL familiarity (SSIS or similar) | Data pipelines (Airflow, Glue) | Medium-High |

**Real-world scenario:** A hiring manager screening MLOps resumes from a "plumbing" lens (per current 2026 recruiting guidance) wants to see *outcomes*, not tool lists — e.g., "reduced model retraining cycle from 3 days to 4 hours" reads the same way "reduced query time from 12s to 200ms" would on a DBA resume. Frame your DBA wins the same way going forward.

### 2b. Net-New Gap (be honest about this one)
Python is the one area with genuinely low transfer. Every source consulted for this roadmap converges on Python as non-negotiable — it is the backbone of automation, pipeline orchestration, and model deployment scripting in MLOps.

---

## 3. Phase 1 — Programming & ML Literacy (Est. 6-10 weeks, part-time)

**Objective:** Build just enough ML theory to be dangerous in conversations with data scientists, while prioritizing production-facing Python.

| Category | Topics | Why It Matters for You |
|---|---|---|
| Python core | Scripting, OOP basics, virtual environments, packaging | Required for everything downstream |
| ML lifecycle literacy | Data prep → training → validation → deployment → monitoring → retraining | This is the mental model MLOps automates around |
| Model evaluation basics | Accuracy, precision/recall, ROC curves | Lets you sanity-check what data scientists hand you |
| SQL → data engineering bridge | Feature stores, ETL/ELT for ML | Your strongest starting point — build from here, not from zero |

**Q&A Example:**
- **Question:** Do I need to become a data scientist to work in MLOps?
- **Answer:** No.
- **Explanation:** MLOps engineers operationalize models that data scientists build; you need enough ML fluency to evaluate whether a deployed model is behaving correctly (drift, degraded accuracy) and enough software engineering skill to package, deploy, and monitor it reliably. Deep modeling expertise is the data scientist's job, not yours.

---

## 4. Phase 2 — Cloud & MLOps Tooling (Est. 8-12 weeks, overlapping Phase 1)

**Objective:** Get hands-on with the AWS ML stack specifically, since that's your existing certification anchor (AI Practitioner).

| Category | Tools/Services | Notes |
|---|---|---|
| Core AWS ML platform | Amazon SageMaker (training, tuning, endpoints, Model Registry) | Current AWS ML Engineer Associate exam content is heavily SageMaker-centric |
| Containers | Docker | Table-stakes — every 2026 MLOps job posting expects this |
| Orchestration | Kubernetes basics, Kubeflow or Airflow, ArgoCD/Flux for GitOps | Airflow is a natural extension of your SQL Agent scheduling background |
| Infrastructure as Code | Terraform | Pairs with your existing infra background |
| Experiment tracking / registry | MLflow, SageMaker Model Registry | Model registry ≈ your mental model of a config/version repository |
| GenAI integration (2026 addition) | Amazon Bedrock | Now embedded in both AI Practitioner and ML Engineer Associate exam guides — don't skip it |

**Windows-specific note:** Use WSL2 for Docker/Kubernetes/Python tooling — most MLOps tutorials and CLI tools assume a Linux shell, and WSL2 avoids the friction of native Windows container tooling.

---

## 5. Phase 3 — Pipeline & Deployment Engineering (Est. 6-8 weeks)

**Objective:** Move from "I can run a notebook" to "I can automate the path from commit to production endpoint."

- **Sub-steps:**
  - Build a CI/CD pipeline that packages a model on commit (GitHub Actions or CodePipeline)
  - Automate retraining triggers based on schedule or drift signal
  - Implement a model registry promotion flow (staging → production)
  - Add automated rollback logic when a new model underperforms live traffic

**Real-world scenario:** This is functionally your SQL Agent job + change management process, rebuilt around model artifacts instead of stored procedures — same governance instinct, new object type.

---

## 6. Phase 4 — Production Operations & Monitoring (Est. 4-6 weeks)

**Objective:** Apply your DBA "keep it alive in prod" instincts to model serving.

| Category | Focus |
|---|---|
| Observability | Prometheus, Grafana, or Datadog for endpoint health |
| Model-specific monitoring | Data drift, concept drift, accuracy decay alerts |
| Governance/compliance | Responsible AI practices, audit trails, data privacy (this maps closely to security/compliance work you already do) |

**Q&A Example:**
- **Question:** Who is responsible for model drift detection in AWS-hosted ML — AWS or the customer?
- **Answer:** The customer/end-user.
- **Explanation:** Per the AWS shared responsibility model, AWS manages the underlying infrastructure and managed-service scalability (e.g., SageMaker's training/hosting infrastructure), but the customer owns model quality, monitoring configuration, drift response, and data governance — the same division of labor you already navigate with RDS/EC2-hosted SQL Server today.

---

## 7. Phase 5 — Certification & Portfolio Proof

### 7a. AWS Certification Path (grounded against current AWS documentation, July 2026)

| Certification | Status as of July 2026 | Recommendation for You |
|---|---|---|
| AWS Certified AI Practitioner (AIF-C01) | **You already hold this** | Foundation is done |
| AWS Certified Machine Learning Engineer – Associate (MLA-C01) | Active, current role-based cert for production ML/MLOps | **Your next target** — directly validates operationalizing ML workloads, ~1 year SageMaker/AWS ML experience recommended (not required) |
| AWS Certified Machine Learning – Specialty (MLS-C01) | **Retired March 31, 2026 — no longer available to sit** | Do not pursue; MLA-C01 has absorbed its operational scope |
| AWS Certified Generative AI Developer – Professional (AIP-C01) | Beta/emerging | Longer-term stretch goal once MLA-C01 is done and you're deploying GenAI/Bedrock workloads |

**Disagreement flag (per your preference for grounded pushback):** Some older blog content still recommends the ML Specialty as the "capstone" AWS ML cert. That guidance is now stale — AWS confirmed MLS-C01 retirement, and the Associate-level ML Engineer cert is the current production-facing credential recruiters screen for. Follow the current AWS page, not older listicles.

### 7b. Portfolio Projects (build these in parallel with study, not after)
- End-to-end pipeline: ingest → train → deploy on SageMaker → monitor → auto-retrain
- One project explicitly reusing a DBA skill (e.g., a feature store fed by a SQL Server change-data-capture pipeline) — this is your strongest differentiator in interviews since almost no other MLOps candidate pool has deep RDBMS operations background

---

## 8. Phase 6 — Market Entry

- Reframe resume bullets from "maintained X databases" → "owned reliability/performance/deployment of X production systems," quantified with metrics (uptime %, latency reduction, deployment frequency)
- Target job titles in order of accessibility given your background: **MLOps Engineer**, **ML Platform Engineer**, **Machine Learning Infrastructure Engineer** — these value your ops background more than pure "Machine Learning Engineer" postings, which skew toward modeling-heavy candidates

---

## 9. Key Insights (Summary for Validation)

1. Your DBA background is a legitimate accelerant, not a liability — most of your ops/HA/monitoring instincts transfer directly; Python is your one true from-scratch skill.
2. AWS's own 2026 certification restructuring already matches your natural next step: AI Practitioner (done) → ML Engineer Associate (next) — no need to invent a path, follow AWS's stated progression.
3. Hiring signal in 2026 has shifted toward *production outcomes* over *tool lists* — your resume rewrite should mirror how you'd already describe a DBA win, just applied to model pipelines.
4. GenAI/Bedrock content is now baked into the certification you're targeting — don't treat it as optional or "later."

---

## 10. QA Notes — Confidence Flags

- **High confidence:** MLS-C01 retirement date (March 31, 2026) and MLA-C01 being the current associate-level ML/MLOps cert — sourced directly from AWS's own certification pages.
- **Medium confidence:** Salary figures cited across sources varied noticeably ($95K-$240K+ depending on source, seniority, and city) — treat these as directional, not precise, and verify against current regional listings before using in negotiation.
- **Lower confidence / worth validating yourself:** Exact study-time estimates per phase (6-12 weeks) are aggregated from multiple training-provider blogs, which have a natural incentive to either overstate or understate difficulty — validate against your own weekly available study hours rather than treating these as fixed.

---

## 11. Tool & Workflow Suggestions

- **MCP/agent tooling:** If you're doing this study plan alongside real project work, a connected GitHub or Google Drive tool could let me pull your actual project code/READMEs directly into future coaching sessions instead of you pasting snippets.
- **Scheduling assistant:** Given this is a multi-month, phase-based plan, a recurring check-in (e.g., a calendar-based monthly review) would keep the gap-assessment loop (Section 2) honest — worth setting up a recurring reminder outside this chat.
- **Skill suggestion:** If you end up repeatedly asking for feedback on Python/pipeline code as you build the Phase 3 project, that's a good candidate for a dedicated code-review workflow — flag it if that becomes a recurring need.

---

## Sources

- AWS Certified Machine Learning Engineer – Associate — aws.amazon.com/certification/certified-machine-learning-engineer-associate/
- AWS Certified Machine Learning – Specialty (retirement notice) — aws.amazon.com/certification/certified-machine-learning-specialty/
- AWS Certified AI Practitioner — aws.amazon.com/certification/certified-ai-practitioner/
- AWS AI Certifications 2026 Guide — flashgenius.net/blog-article/aws-ai-certifications-2026-complete-guide-to-ai-practitioner-ml-engineer-generative-ai-developer
- Is AWS Machine Learning Certification Worth It in 2026? — thinkcloudly.com/blog/aws-machine-learning-certification/
- MLOps Engineer Skills / Resume Guide 2026 — interviewkickstart.com/skills/mlops-engineer ; techiecv.com/resume-guides/mlops-engineer-resume
- How to Become an MLOps Engineer 2026 — pluralsight.com/resources/blog/ai-and-data/how-become-an-mlops-engineer ; coursera.org/articles/mlops-engineer
