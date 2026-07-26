# Ibrutinib gene interactions and CIViC variants

- Source: https://claude.ai/share/9ad52a71-74c1-40a5-aa22-afc03e5fa940
- Author: Lars S
- Created: 2026-01-14
- Messages: 2

---

## Human

What genes interact with the drug Ibrutinib, and which of those genes have specific variants in CIViC associated with sensitivity or resistance?

---

## Assistant

I'll help you find genes that interact with Ibrutinib and then check which of those genes have variants in CIViC associated with sensitivity or resistance.
```
This block is not supported on your current device yet.
```

Now let me search CIViC for evidence about sensitivity and resistance for the top interacting genes:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me also check for PLCG2 variants specifically, as this was the top-scoring gene for drug interactions:
```
This block is not supported on your current device yet.
```

Let me also check for CIViC assertions to get the most validated clinical evidence:
```
This block is not supported on your current device yet.
```

Here's a comprehensive summary of what I found:

## Genes That Interact with Ibrutinib

Based on DGIdb data, the top genes interacting with Ibrutinib include:

| Gene | Interaction Score | Interaction Type | Key Sources |
|------|------------------|------------------|-------------|
| **PLCG2** | 4.61 | - | [CGI](https://www.cancergenomeinterpreter.org/biomarkers), [DoCM](http://docm.info/), [PMID:24869598](https://pubmed.ncbi.nlm.nih.gov/24869598/) |
| **MYD88** | 1.54 | - | [CGI](https://www.cancergenomeinterpreter.org/biomarkers), [CIViC](https://www.civicdb.org), [PharmGKB](http://www.pharmgkb.org) |
| **BTK** | 0.38 | Inhibitor (inhibitory) | [Multiple sources](https://www.civicdb.org) including CIViC, TTD, CGI, ChEMBL |
| Other genes: BMX, TEC, LYN, SMARCA4, CSF3R, EPHA8, etc.

---

## CIViC Variants Associated with Ibrutinib Response

### Sensitivity/Response Variants

| Gene | Variant | Disease | Evidence Level | CIViC Link |
|------|---------|---------|----------------|------------|
| **MYD88** | L265P | Lymphoplasmacytic Lymphoma | B (Clinical) | [EID:986](https://identifiers.org/civic.eid:986), [PMID:25853747](http://www.ncbi.nlm.nih.gov/pubmed/25853747) |
| **BTK** | Expression | B-cell ALL | D (Preclinical) | [EID:9287](https://identifiers.org/civic.eid:9287), [PMID:28031181](http://www.ncbi.nlm.nih.gov/pubmed/28031181) |

### Resistance Variants

| Gene | Variant | Disease | Evidence Level | CIViC Link |
|------|---------|---------|----------------|------------|
| **BTK** | C481S | CLL | B (Clinical) | [EID:436](https://identifiers.org/civic.eid:436), [PMID:24869598](http://www.ncbi.nlm.nih.gov/pubmed/24869598); [EID:1770](https://identifiers.org/civic.eid:1770), [PMID:26182309](http://www.ncbi.nlm.nih.gov/pubmed/26182309) |
| **BTK** | T316A | CLL | C (Case study) | [EID:1985](https://identifiers.org/civic.eid:1985), [PMID:27626698](http://www.ncbi.nlm.nih.gov/pubmed/27626698) |
| **PIM1** | L2V, P81S, S97N | DLBCL-ABC | D (Preclinical) | [EID:9945-9947](https://identifiers.org/civic.eid:9945), [PMID:27904766](http://www.ncbi.nlm.nih.gov/pubmed/27904766) |

---

## Key Findings

**Overlapping genes** (appear in both DGIdb drug interactions AND CIViC with sensitivity/resistance evidence):

1. **BTK** - The primary target of ibrutinib
   - **Resistance**: C481S mutation (most common acquired resistance mechanism in CLL - found in ~80% of resistant cases) and T316A
   - **Sensitivity**: BTK expression associated with response in B-ALL

2. **MYD88** - Key interacting gene
   - **Sensitivity**: L265P mutation associated with better response in Waldenström's macroglobulinemia/lymphoplasmacytic lymphoma

**PLCG2** - Although it has the highest interaction score in DGIdb and is known to be involved in ibrutinib resistance (mutations found in patients with acquired resistance), I did not find specific PLCG2 variant evidence entries in CIViC for ibrutinib at this time.
