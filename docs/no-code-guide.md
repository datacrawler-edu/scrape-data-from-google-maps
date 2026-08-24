# Scrape data from Google Maps without code

The hosted Actor can be run from Apify's web interface. This is the simplest option when you want Google Maps business data as a downloadable Dataset without installing a package.

## Step-by-step

1. Open [Google Maps Business Scraper on Apify](https://apify.com/datascraperes/actor-google-maps?fpr=edudata).
2. Open the **Input** tab.
3. Add at least one value to **Locations**.
4. Add at least one business category or term to **Search Queries**.
5. Select one **Language** and the matching **Country code**.
6. Set **Max Results** to a small positive number for the first test.
7. Click **Start**.
8. Open **Dataset** when the run finishes, then export JSON, CSV, Excel or JSONL.

## First test

Use [`data/sample-input.json`](../data/sample-input.json). It searches one category in one city and requests one unique result. Google Maps data changes over time, so compare the returned structure with the fixture instead of expecting the same business.

## Use Apify's monthly free usage credit

Apify's Free plan currently includes **$5 in monthly prepaid usage** and does not require a credit card. Use one location, one query and a low result limit first. The credit is not unlimited, and unused usage expires at the end of the billing cycle.

See the [current Apify pricing](https://apify.com/pricing?fpr=edudata) for current terms.

## What to check in the output

Each Dataset item represents one unique business. Start with `name`, `placeId`, `address`, `phone`, `website`, `avgRating`, `tags`, `lat` and `long`. Optional values can be empty because Google Maps does not expose every field for every listing.

## Larger searches and pricing

Every query runs in every location, and large geographic areas create wider search plans. `maxResults` is the global result and billing limit. The current price is $1.00 per 1,000 unique business results. Check the [Actor page](https://apify.com/datascraperes/actor-google-maps?fpr=edudata) before production use because pricing and limits can change.
