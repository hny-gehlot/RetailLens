# RetailLens — Data Quality Report

## 1. Dataset Overview

- **Dataset:** UCI Online Retail
- **Original records:** 541,909
- **Original columns:** 8
- **Exact duplicate records identified:** 5,268
- **Records after duplicate removal:** 536,641
- **Columns after adding Revenue:** 9

The dataset contains retail transaction records, including invoice numbers, product codes, quantities, prices, customer IDs and countries.

## 2. Missing Value Analysis

After removing exact duplicates:

- **Missing CustomerIDs:** 135,037 (approximately 25.17% of records)
- **Missing Descriptions:** 1,454
- **Total missing cells:** 136,491
- **Revenue from records with missing CustomerIDs:** £1,447,487.53
- **Percentage of total calculated revenue:** 14.88%

Records with missing descriptions contribute £0 in calculated revenue.

**Decision:** Retain missing values rather than inserting fabricated customer IDs or product descriptions. Records with missing CustomerIDs can still contribute to overall sales analysis, although they cannot be reliably used for customer-level identification.

## 3. Duplicate Records

- **Exact duplicate rows identified:** 5,268
- **Unique invoices containing duplicate rows:** 1,933
- **Revenue represented by duplicate rows:** £21,740.98
- **Quantity represented by duplicate rows:** 13,948

**Decision:** Remove exact duplicate rows while preserving the original raw dataset. The revenue represented by duplicates is not automatically assumed to be overstated revenue.

## 4. Cancellation and Negative Quantity Analysis

After duplicate removal:

- **Negative quantity records:** 10,587
- **Negative quantity records with C-prefixed invoices:** 9,251
- **Negative quantity records without C-prefixed invoices:** 1,336
- **Revenue from all negative quantity records:** -£893,979.73

The 1,336 unusual negative-quantity records without a C prefix have missing descriptions, zero UnitPrice and missing CustomerIDs.

**Decision:** Retain negative quantity records for cancellation and transaction analysis. Investigate unusual records separately rather than deleting them automatically.

## 5. Price Analysis

After duplicate removal:

### Zero-price records

- **Records with UnitPrice = 0:** 2,510
- Common descriptions include check, damages, damaged, found and adjustment.
- **Revenue from zero-price records:** £0.00

For comparison, the original dataset contained 2,515 zero-price records before duplicate removal.

**Decision:** Retain zero-price records for further investigation. Exclude them from ordinary sales calculations only when the analytical definition requires it.

### Negative-price records

- **Records with UnitPrice below zero:** 2
- Both records have the description "Adjust bad debt".
- **Combined negative revenue:** -£22,124.12

**Decision:** Retain these accounting-related adjustments and distinguish them from ordinary product transactions.

## 6. Revenue Overview

Revenue is calculated using:

`Revenue = Quantity × UnitPrice`

After duplicate removal:

| Revenue category | Amount |
|---|---:|
| Positive revenue | £10,642,110.80 |
| Negative revenue | -£916,103.85 |
| Zero revenue | £0.00 |
| **Net calculated revenue** | **£9,726,006.95** |

Negative revenue consists of:

- C-prefixed invoice records: -£893,979.73
- Other negative-revenue records (bad-debt adjustments): -£22,124.12

This is calculated net transaction revenue, not necessarily accounting-recognised revenue.

## 7. Cleaning Strategy

The current cleaning pipeline:

- Loads the original Excel dataset.
- Removes exact duplicate rows.
- Calculates revenue for each transaction.
- Preserves missing CustomerIDs and descriptions.
- Preserves cancellation records.
- Preserves zero-price and negative-price records.
- Investigates unusual negative quantities.
- Separates positive, negative and zero revenue.
- Exports the processed dataset as a CSV file.

The original raw dataset remains unchanged.

## 8. Future Improvements

- Add explicit transaction classification flags.
- Investigate unusual transaction types further.
- Develop exploratory data analysis (EDA).
- Analyse product performance and customer purchasing patterns.
- Build visualisations and a business intelligence dashboard.

---

**Project:** RetailLens — Retail Sales Intelligence  
**Dataset:** UCI Online Retail  
**Current stage:** Data inspection and cleaning