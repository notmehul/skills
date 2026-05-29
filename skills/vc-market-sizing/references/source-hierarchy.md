# Source Hierarchy + Where to Pull Inputs

Goal: prefer auditable, primary sources; use analyst reports as context, not the full argument.

## Default Source Order

1. Government / official statistics (counts, output, employment, trade)
2. Regulators / administrative datasets (regulated volume, approvals, claims, procedures)
3. Public company filings (segment notes, customer counts, geo mix, ARPU/ASP hints)
4. Industry associations / standards bodies (taxonomy, installed base, certification counts)
5. Academic / credible surveys (methodology transparent)
6. Commercial analyst reports (use for definitions/triangulation; validate)

## Classification Systems (Pick One Early)

- US: NAICS (industry), Census geographies
- EU: NACE (industry), NUTS geographies
- Global: ISIC (industry)
- Trade: HS codes (products)

Map your category to 1-3 codes; document inclusions/exclusions.

## High-Signal Public Data Sources

### Global

- World Bank Open Data (macro denominators, country comparables): https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information
- OECD datasets + SDMX (cross-country): https://data.oecd.org/api/sdmx-json-documentation/
- IMF Data (macro/finance): https://data.imf.org/en/Resource-Pages/IMF-API
- UNdata hub: https://data.un.org/
- UN Comtrade (trade flows by product/partner): https://comtradedeveloper.un.org/

### United States

- US Census API (Economic Census, CBP, etc.): https://census.gov/data/api.html
- Economic Census data landing page: https://www.census.gov/programs-surveys/economic-census/data.html
- BEA API (industry accounts, value added, gross output): https://apps.bea.gov/API/docs/index.htm
- BLS industry statistics overview (employment/wages/productivity entry point): https://www.bls.gov/bls/industry.htm
- Data.gov (dataset discovery): https://www.data.gov/

### EU / UK

- Eurostat API (EU official statistics): https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-introduction
- ECB Data Portal API (financial series): https://data.ecb.europa.eu/help/api/overview
- data.europa.eu (EU open data catalog): https://data.europa.eu/en
- UK Companies House API (registry + filings metadata): https://developer.company-information.service.gov.uk/

### Public Company Filings

- SEC EDGAR API documentation: https://www.sec.gov/edgar/sec-api-documentation

### Regulators (Example: Healthcare)

- openFDA (FDA datasets): https://open.fda.gov/

## Reconciling Conflicting Numbers

- Align definitions: revenue vs gross output vs value added vs GMV vs spend (do not average mismatched constructs)
- Align year/geo/currency: lock year; specify nominal vs real; specify FX vs PPP
- Prefer official totals; use filings for splits; use regulators for throughput constraints
- Report low/base/high tied to explicit drivers (coverage, inclusion rules, penetration)
