# Document extraction fields and cross-checks

Per document: the fields to extract, the validation on each, and the cross-checks across documents. Mask Aadhaar to its last four digits at capture; never store the full number or an unmasked image. `knowledge-and-extraction` owns the extraction build (parser choice, schema, validators, review queue); this file is the field list it fills. As of Oct 2026.

## Identity

- **PAN card.** PAN (regex; fourth character P for an individual), name, father's name, date of birth, photo present. Cross-check name and date of birth against Aadhaar and the bank statement; PAN-Aadhaar linkage status through the lender's API.
- **Aadhaar** (masked copy; offline XML or QR preferred). Name, date or year of birth, gender, address, last four digits, XML or QR generation date (3 working days or fewer for video KYC).

## Income, salaried

- **Salary slips, latest three.** Employer name and address, employee id, pay period, gross, basic, HRA, other allowances, deductions (PF, professional tax, TDS), net pay, payment mode, bank account last four. Cross-check net pay against salary credits in the statement; employer name against the credit narration; period continuity across the three slips.
- **Form 16, ITR (two years), 26AS.** PAN, assessment year, employer TAN, gross salary, taxable income, TDS. Cross-check ITR income against bank inflows.

## Income, self-employed

- **ITR-3 or ITR-4.** Gross receipts, net profit, depreciation, partner remuneration; 26AS TDS totals. Cross-check against bank inflows and GST turnover.
- **GST returns.** GSTIN, filing periods, GSTR-3B turnover, tax paid, filing regularity.
- **Business proofs.** Udyam or shop-act registration, partnership deed or MOA, audited P&L and balance sheet for three years with the auditor's UDIN.

## Bank statements, 6 to 12 months, PDF or AA

Account holder, account number last four, IFSC and bank, period, opening and closing balance, every transaction (date, narration, debit, credit, balance). Derived: salary credits by employer, average monthly balance, days below minimum balance, inward and outward bounces, existing EMIs from NACH and ECS narrations, cash-deposit ratio, UPI merchant categories, circular transfers.

PDF only: a tamper score from fonts, metadata and running-balance arithmetic. AA: `consent_id`, FIP, data life. Cross-check: period coverage with no gaps; closing balance of one month equals opening balance of the next.

## Property

- **APF project.** Project RERA number, APF or lender approval reference, builder name, tower and unit, carpet area, agreement value, payment schedule, demand letter (amount, due date, stage). Cross-check the unit against the APF inventory.
- **Resale or non-APF.** Sale deed or agreement to sell, chain of title in years, encumbrance certificate, approved plan, occupancy or completion certificate, property-tax receipts, society NOC, valuation report (fair market value, stage of construction).

## Other sets

- **Co-applicant.** The same identity and income fields, plus relationship and ownership share.
- **Existing loan, for a balance transfer.** Sanction letter (sanction date, benchmark, spread), latest statement (outstanding, EMI, reset date), foreclosure letter, list of documents held by the lender. The sanction date decides the prepayment-charge treatment (1 Jan 2026 rule).
- **Consents.** Bureau pull, AA consent artefact, data-protection notice version, recording-consent timestamp.

## Output contract for the operator

Per document: a status (ok, unreadable, mismatch, missing), the fields with a confidence each, and one human-readable "pending items" message in the borrower's language, ready to send. Measure field-level accuracy on at least 100 documents spanning every layout and language before quoting a number.
