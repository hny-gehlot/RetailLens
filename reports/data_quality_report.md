# RetailLens — Data Quality Report

## 1. Dataset Overview

- Dataset: UCI Online Retail
- Original records: 541,909
- Original columns: 8
- Records after removing exact duplicates: 536,641
- Duplicate records removed: 5,268

## 2. Missing Values

- Missing CustomerIDs: 135,037
- Missing Descriptions: 1,454
- Missing CustomerID records contribute approximately 14.88% of total calculated revenue.

**Decision:** Retain missing values instead of inserting fabricated customer IDs or product descriptions.

## 3. Duplicate Records

A total of 5,268 exact duplicate rows were identified and removed.

**Decision:** Remove exact duplicates while preserving the original raw dataset.

## 4. Cancellation and Negative Revenue Analysis

- Negative revenue records: 9,253
- Cancellation invoice records: 9,251
- Negative revenue from cancellations: £893,979.73
- Other negative revenue records: 2
- Negative revenue from other records: £22,124.12

The two non-cancellation negative revenue records have the description "Adjust bad debt".

**Decision:** Retain and flag cancellation records and accounting adjustments separately.

## 5. Zero-Price Records

- Zero UnitPrice records: 2,515
- These include operational descriptions such as damaged, adjustment, check and found.

**Decision:** Retain for further investigation and exclude from ordinary sales calculations where appropriate.

## 6. Revenue Overview

- Positive revenue: £10,642,110.80
- Negative revenue: -£916,103.85
- Net calculated revenue: £9,726,006.95

## 7. Cleaning Strategy

The cleaned dataset will:
- Remove exact duplicate rows.
- Preserve missing values.
- Preserve cancellation and adjustment records.
- Create a Revenue column.
- Add classification flags for different transaction types.
- Preserve the original raw dataset.

