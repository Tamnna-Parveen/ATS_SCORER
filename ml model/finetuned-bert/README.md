---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:224
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-mpnet-base-v2
widget:
- source_sentence: Sales Manager with 3 years of experience in B2B sales and client
    acquisition. Skilled in Negotiation, B2B Sales, Pipeline Management, Account Management.
  sentences:
  - 'Business Intelligence Analyst at a mid-size consultancy. Required skills: Data
    Warehousing, Power BI, SQL, KPI Analysis. 9+ years of experience preferred. Location:
    Pune.'
  - 'We are hiring a Sales Manager for a healthcare network. Must have strong knowledge
    of Salesforce, B2B Sales, Pipeline Management, Account Management. Minimum 4 years
    of relevant experience. Location: Pune.'
  - 'Job opening: Digital Marketing Specialist at a global retail chain. Candidate
    should be proficient in PPC, Google Ads, Content Marketing, Email Marketing, SEO,
    Analytics, with at least 7 years of experience. Location: Mumbai.'
- source_sentence: Product Manager professional, 9 years in the industry, specializing
    in product strategy and lifecycle management with expertise in User Research,
    Stakeholder Management, Market Analysis, Agile, Roadmapping, JIRA, A/B Testing.
  sentences:
  - a fast-growing startup is looking for a Product Manager. Key requirements include
    User Research, Stakeholder Management, Agile, Roadmapping, JIRA, A/B Testing.
    Ideal candidate has 9+ years of experience. Based in Chennai.
  - 'Job opening: Data Scientist at a Fortune 500 company. Candidate should be proficient
    in Statistics, Deep Learning, NLP, Python, with at least 1 years of experience.
    Location: Delhi NCR.'
  - a global retail chain is looking for a Frontend Developer. Key requirements include
    UI/UX, TypeScript, HTML5, React, CSS, Redux. Ideal candidate has 5+ years of experience.
    Based in Chennai.
- source_sentence: Results-driven Backend Developer with 2 years of professional experience.
    Strong background in Kubernetes, Spring Boot, Microservices, Docker, REST APIs.
  sentences:
  - 'Backend Developer at a Fortune 500 company. Required skills: Spring Boot, Kubernetes,
    REST APIs, Docker. 2+ years of experience preferred. Location: remote.'
  - a SaaS company is looking for a Content Writer. Key requirements include Content
    Strategy, Editing, SEO Writing, Blogging. Ideal candidate has 5+ years of experience.
    Based in Noida.
  - a mid-size consultancy is looking for a Product Manager. Key requirements include
    Market Analysis, Stakeholder Management, User Research, Product Strategy, Roadmapping,
    JIRA. Ideal candidate has 1+ years of experience. Based in remote.
- source_sentence: Results-driven Full Stack Developer with 2 years of professional
    experience. Strong background in Express.js, MongoDB, Node.js, React, REST APIs.
  sentences:
  - 'Machine Learning Engineer at a SaaS company. Required skills: PyTorch, TensorFlow,
    Docker, Deep Learning, Python. 7+ years of experience preferred. Location: Delhi
    NCR.'
  - 'We are hiring a Data Scientist for a financial services firm. Must have strong
    knowledge of Deep Learning, Scikit-learn, NLP, Python. Minimum 6 years of relevant
    experience. Location: Delhi NCR.'
  - 'Data Scientist at a global retail chain. Required skills: Deep Learning, Scikit-learn,
    Pandas, NLP. 5+ years of experience preferred. Location: Hyderabad.'
- source_sentence: Healthcare Data Analyst with 12 years of experience in healthcare
    analytics. Skilled in Data Visualization, EHR Systems, SQL, Healthcare Analytics.
  sentences:
  - 'Job opening: UI/UX Designer at an e-commerce platform. Candidate should be proficient
    in Figma, Usability Testing, Adobe XD, User Research, with at least 11 years of
    experience. Location: Pune.'
  - 'Sales Manager at a global retail chain. Required skills: Negotiation, B2B Sales,
    Pipeline Management, Client Relationship. 8+ years of experience preferred. Location:
    Bangalore.'
  - 'Healthcare Data Analyst at an enterprise firm. Required skills: EHR Systems,
    HIPAA Compliance, SQL, Healthcare Analytics. 1+ years of experience preferred.
    Location: Noida.'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer based on sentence-transformers/all-mpnet-base-v2
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: ats val
      type: ats-val
    metrics:
    - type: pearson_cosine
      value: 0.9396763335456306
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.9209201102602335
      name: Spearman Cosine
---

# SentenceTransformer based on sentence-transformers/all-mpnet-base-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for retrieval.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) <!-- at revision e8c3b32edf5434bc2275fc9bab85f82640a19130 -->
- **Maximum Sequence Length:** 384 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'MPNetModel'})
  (1): Pooling({'embedding_dimension': 768, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Healthcare Data Analyst with 12 years of experience in healthcare analytics. Skilled in Data Visualization, EHR Systems, SQL, Healthcare Analytics.',
    'Healthcare Data Analyst at an enterprise firm. Required skills: EHR Systems, HIPAA Compliance, SQL, Healthcare Analytics. 1+ years of experience preferred. Location: Noida.',
    'Job opening: UI/UX Designer at an e-commerce platform. Candidate should be proficient in Figma, Usability Testing, Adobe XD, User Research, with at least 11 years of experience. Location: Pune.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.4815, 0.0715],
#         [0.4815, 1.0000, 0.1053],
#         [0.0715, 0.1053, 1.0000]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Semantic Similarity

* Dataset: `ats-val`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.9397     |
| **spearman_cosine** | **0.9209** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 224 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                         | sentence_1                                                                         | label                                                            |
  |:---------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------|
  | type     | string                                                                             | string                                                                             | float                                                            |
  | modality | text                                                                               | text                                                                               |                                                                  |
  | details  | <ul><li>min: 26 tokens</li><li>mean: 34.27 tokens</li><li>max: 45 tokens</li></ul> | <ul><li>min: 33 tokens</li><li>mean: 42.96 tokens</li><li>max: 54 tokens</li></ul> | <ul><li>min: 0.02</li><li>mean: 0.53</li><li>max: 0.98</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                       | sentence_1                                                                                                                                                                               | label             |
  |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
  | <code>Business Intelligence Analyst professional, 2 years in the industry, specializing in business intelligence and reporting with expertise in Power BI, SQL, KPI Analysis, Tableau.</code>    | <code>Business Intelligence Analyst at a global retail chain. Required skills: ETL, DAX, Reporting, KPI Analysis. 1+ years of experience preferred. Location: remote.</code>             | <code>0.4</code>  |
  | <code>Data Scientist professional, 9 years in the industry, specializing in predictive modeling and analytics with expertise in Statistics, Machine Learning, Deep Learning, SQL, Python.</code> | <code>DevOps Engineer at a global retail chain. Required skills: AWS, CI/CD, Docker. 9+ years of experience preferred. Location: Delhi NCR.</code>                                       | <code>0.26</code> |
  | <code>Product Manager with 10 years of experience in product strategy and lifecycle management. Skilled in User Research, Agile, Roadmapping, JIRA, A/B Testing.</code>                          | <code>Product Manager at a financial services firm. Required skills: User Research, Agile, Roadmapping, JIRA, A/B Testing. 9+ years of experience preferred. Location: Delhi NCR.</code> | <code>0.98</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss",
      "cos_score_transformation": "torch.nn.modules.linear.Identity"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 16
- `num_train_epochs`: 10
- `fp16`: True
- `per_device_eval_batch_size`: 16
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 16
- `num_train_epochs`: 10
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 16
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `warmup_ratio`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch | Step | ats-val_spearman_cosine |
|:-----:|:----:|:-----------------------:|
| 1.0   | 14   | 0.7974                  |
| 2.0   | 28   | 0.8759                  |
| 3.0   | 42   | 0.8925                  |
| 4.0   | 56   | 0.9071                  |
| 5.0   | 70   | 0.9150                  |
| 6.0   | 84   | 0.9165                  |
| 7.0   | 98   | 0.9209                  |


### Training Time
- **Training**: 50.9 seconds

### Framework Versions
- Python: 3.12.13
- Sentence Transformers: 5.6.0
- Transformers: 5.13.1
- PyTorch: 2.11.0+cu128
- Accelerate: 1.14.0
- Datasets: 4.0.0
- Tokenizers: 0.22.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->