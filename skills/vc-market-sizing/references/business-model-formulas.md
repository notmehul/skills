# Business-Model Formulas (Bottom-up Defaults)

Pick the model that matches how revenue is actually captured. Keep units consistent.

## Seat-based B2B SaaS

Formula:

`TAM ($/yr) = #target orgs × avg eligible seats/org × adoption% × realized $/seat/yr`

Anchors (public list prices; adjust for discounting/packaging):

- Salesforce Sales pricing (tier examples): https://www.salesforce.com/sales/pricing/

Gotchas:

- Eligible seats != headcount (role-based)
- List price != realized price (discounts, EAs)
- Multi-year prepay: convert to annualized

## Location-based SaaS

Formula:

`TAM = #locations × adoption% × ACV_per_location`

Gotchas:

- "Locations" definition (store vs warehouse vs office)
- Franchises vs corporate-owned counting

## Usage-based SaaS / Consumption

Formula:

`TAM = addressable usage units × realized $/unit`

Anchor (pricing mechanics + free tier concept):

- AWS Lambda pricing (requests + duration): https://aws.amazon.com/lambda/pricing/

Gotchas:

- Included units/free tier => effective price
- Seasonality/burstiness => forecasting error

## API / Communications (per message)

Formula:

`TAM = messages × net $/message + phone_numbers + add-ons`

Anchor:

- Twilio US SMS pricing (per segment; carrier fees noted): https://www.twilio.com/en-us/sms/pricing/us

Gotchas:

- Segmenting (160-char splits)
- Carrier fees/registration overhead

## Payments / Fintech Take-Rate

Formula:

`Revenue = TPV × take_rate + txn_count × fixed_fee − refunds/disputes − fraud_losses`

Anchors:

- Stripe pricing mechanics (blended vs interchange-plus): https://stripe.com/resources/more/interchange-plus-pricing-explained
- Interchange as large share of processing fees (context for net economics): https://stripe.com/resources/more/interchange-fees-101-what-they-are-how-they-work-and-how-to-cut-costs

Gotchas:

- Headline take-rate vs net after interchange/network fees
- Mix varies by geo, card type, auth method

## Marketplaces

Formula:

`Revenue = GMV × take_rate` (then subtract payment processing, incentives, trust/safety)

Anchor (operator benchmark framing by marketplace type):

- Mostly Metrics take-rate comparisons: https://www.mostlymetrics.com/p/comparing-marketplace-take-rates

Gotchas:

- Disintermediation/leakage
- Subsidized take-rate via promos

## App/Digital Goods Platforms

Formula:

`Revenue = developer GMV × commission%`

Anchor:

- Apple Small Business Program (15% commission for qualifying developers): https://developer.apple.com/app-store/small-business-program/

Gotchas:

- Blended commission tiers; regional policy differences

## Healthcare Provider-based

Formula:

`TAM = #providers × $spend/provider/year × addressable category% × adoption%`

Anchors:

- US licensed physicians count (anchor for provider universe): https://www.fsmb.org/advocacy/news-releases/fsmb-physician-census-identifies-1082187-licensed-physicians-in-u.s/
- CMS National Health Expenditure datasets (spend baselines): https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data

Gotchas:

- Providers != practices (ownership roll-ups)
- Payer mix drives willingness to pay

## Developer tools

Formula:

`TAM = #developers × paid penetration% × $/dev/month × 12` (+ usage credits if metered)

Anchor (pricing tiers + metered premium requests):

- GitHub Copilot plans: https://github.com/features/copilot/plans

Gotchas:

- Suite bundling and enterprise contracts hide true price
- AI/compute costs can create margin cliffs if priced per-seat
