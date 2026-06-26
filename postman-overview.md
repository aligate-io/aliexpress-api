# AliExpress Data API — Products, Reviews, Sellers, Coupons & Search

A fast, real-time **AliExpress API** for **product data**, **reviews**, **seller / store info**,
**store coupons**, **seller catalogs**, and product **search by text or image** — every response
scoped to the country & currency you ask for. Distributed on **RapidAPI**.

If you're looking for an **AliExpress product data API**, an **AliExpress price API**, or an
**AliExpress image search API**, this is the quickest way to integrate it — built for
**dropshipping**, **price monitoring**, catalog enrichment, and e-commerce product research.

## Quickstart

1. Get a key on [RapidAPI](https://rapidapi.com/aligate/api/aligate-aliexpress-data-api).
2. Set the collection variable **`x-rapidapi-key`** to your key.
3. Send any request (e.g. **Get Product Info**) — done.

Every request needs two headers, already wired here as collection variables:

| Header | Value |
| --- | --- |
| `x-rapidapi-key` | your RapidAPI key |
| `x-rapidapi-host` | `aligate-aliexpress-data-api.p.rapidapi.com` |

## Endpoints

| Operation | What it returns |
| --- | --- |
| **Get Product Info** | Full product detail: pricing, SKUs/variants, stock, shipping, seller, optional description. |
| **Get Product Reviews** | Paginated buyer reviews with rating breakdown, filters, and sorting. |
| **Get Seller Info** | Store profile: ratings, feedback, followers, store age, categories. |
| **Get Seller Coupons** | Active store coupon campaigns, scoped to country & currency. |
| **Get Seller Products** | A store's product catalog, paginated and best-selling first. |
| **Search By Text** | Products matching a keyword, plus category facets. |
| **Search By Image** | Products visually matching an uploaded image. |

## Official SDKs

Generated from the same OpenAPI spec as this collection:

- **Python** — `pip install aligate`
- **Node.js** — `npm install @aligate/sdk`
- **Java** — `io.aligate:aligate-sdk` (Maven Central)
- **Go** — `go get github.com/aligate-io/aliexpress-go/v2`

## Links

- **Interactive docs (Swagger):** https://api.aligate.io/docs
- **OpenAPI spec:** https://api.aligate.io/openapi.yaml
- **API key & plans (RapidAPI):** https://rapidapi.com/aligate/api/aligate-aliexpress-data-api

---

*Unofficial. AliGate is an independent third-party service and is not affiliated with, endorsed by,
or sponsored by Alibaba Group or AliExpress. "AliExpress" is a trademark of its respective owner.*
