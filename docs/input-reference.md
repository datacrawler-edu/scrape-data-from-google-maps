# Input reference

The hosted Actor accepts four required fields and one optional result limit.

| Field | Type | Required | Default | Accepted values | Description |
| --- | --- | :---: | --- | --- | --- |
| `locations` | `string[]` | Yes | — | One or more unique non-empty cities, regions or countries | Every location is combined with every query. |
| `queries` | `string[]` | Yes | — | One or more unique non-empty business categories or search terms | Examples include `restaurants`, `dentists` and `hotels`. |
| `language` | `string` | Yes | `es` | A language code offered by the Input selector | Applies to labels and localized Google Maps data for the complete run. |
| `countryCode` | `string` | Yes | `ES` | An uppercase country code offered by the Input selector | Disambiguates and constrains every location in the run. |
| `maxResults` | `integer` | No | `1000` | `0` or greater | Global maximum number of unique Dataset items; `0` means no result limit. |

## Location and query combinations

The Actor searches every query in every location. Two locations and three queries therefore produce six search targets before geographic subdivision.

Repeated identical values are normalized and processed once. One shared `countryCode` applies to all locations, so use separate runs when searching different countries.

## Geographic scope

A city name searches that city. Selecting a country code does not automatically expand a city search to the full country. To request the widest country coverage, enter the country name itself as the location and select its matching country code.

Large regions and countries require wider geographic plans and usually take longer than a city. Start with a small positive `maxResults` before removing the limit.

## Result and cost controls

`maxResults` limits unique businesses across all queries, locations and search sectors. Apify's **Maximum cost per run** setting can provide an additional spending cap, especially when `maxResults` is `0`.
