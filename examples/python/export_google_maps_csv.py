"""Export Google Maps business Dataset JSON to CSV."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


FIELDS = [
    "name",
    "placeId",
    "googleMapsUrl",
    "address",
    "city",
    "region",
    "postalCode",
    "countryCode",
    "phone",
    "website",
    "avgRating",
    "totalReviews",
    "priceRange",
    "tags",
    "description",
    "businessPhoto",
    "photoUrls",
    "hours",
    "lat",
    "long",
    "discoveryQuery",
    "searchLocation",
    "searchCoordinates",
    "scrapeTimestamp",
]


def csv_value(value: Any) -> Any:
    """Serialize nested values without losing their structure."""
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    return value


def export_csv(input_path: Path, output_path: Path) -> None:
    rows: list[dict[str, Any]] = json.loads(input_path.read_text(encoding="utf-8"))
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(
            {field: csv_value(row.get(field)) for field in FIELDS} for row in rows
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input", type=Path, nargs="?", default=Path("data/sample-output.json")
    )
    parser.add_argument(
        "output", type=Path, nargs="?", default=Path("data/exported-google-maps.csv")
    )
    args = parser.parse_args()
    export_csv(args.input, args.output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
