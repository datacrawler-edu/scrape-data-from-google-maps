# Output reference

The default Dataset stores one item per unique accepted Google Maps business. Results are deduplicated by `placeId` across the complete run.

| Field | Type | Required | Description |
| --- | --- | :---: | --- |
| `name` | string | Yes | Business name shown on Google Maps. |
| `placeId` | string | Yes | Stable Google Place ID and deduplication key. |
| `googleMapsUrl` | string or null | No | Direct Google Maps listing URL. |
| `address` | string or null | No | Most complete returned street address. |
| `city` | string or null | No | City, municipality or locality. |
| `region` | string or null | No | Region, state or province. |
| `postalCode` | string or null | No | Postal or ZIP code. |
| `countryCode` | string or null | No | Two-letter country code. |
| `phone` | string or null | No | Public phone number as displayed. |
| `website` | string or null | No | Public website associated with the listing. |
| `avgRating` | number or null | No | Average Google Maps rating when exposed. |
| `totalReviews` | integer or null | No | Review-count value when exposed. |
| `priceRange` | string or null | No | Price-level text when exposed. |
| `tags` | string array or null | No | Localized business categories. |
| `description` | string or null | No | Business description when exposed. |
| `businessPhoto` | string or null | No | Main returned business-photo URL. |
| `photoUrls` | string array or null | No | Unique returned photo URLs. |
| `hours` | object array or null | No | Available localized opening-hours entries. |
| `lat` | number or null | No | Business latitude. |
| `long` | number or null | No | Business longitude. |
| `discoveryQuery` | string or null | No | Query that discovered the unique business. |
| `searchLocation` | string or null | No | Input location being processed when discovered. |
| `searchCoordinates` | string or null | No | Latitude and longitude of the search sector. |
| `scrapeTimestamp` | string or null | No | ISO 8601 collection timestamp. |

## Opening-hours objects

Each `hours` item can contain:

- `day`: localized day label.
- `hours`: human-readable opening interval.
- `open24Hour`: available opening-hour component in 24-hour format.
- `close24Hour`: available closing-hour component in 24-hour format.

Use the `hours` string when minutes or split intervals matter. The returned array is not guaranteed to contain all seven days.

## Missing values

Optional text can be `null` or an empty string. Optional arrays can be empty or `null`, and optional numbers can be `null`. Numeric zero can be a valid value and should not automatically be treated as missing.

Inspect [`../data/sample-output.json`](../data/sample-output.json) for one complete item from a successful published Actor run.
