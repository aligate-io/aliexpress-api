# AliGate — AliExpress Data API SDKs (Python · Node.js · Java)

> Official AliGate SDKs for the **AliExpress Data API** — products, reviews, sellers, coupons,
> text & image search. Bring your RapidAPI key.

Official, multi-language client SDKs for the **AliGate AliExpress Data API** — a fast, real-time
**AliExpress data API** for product data, reviews, sellers, store coupons, store catalogs, and
product **search by text or image**. The API is distributed through **RapidAPI**; these SDKs wrap it
in idiomatic clients for **Python, Node.js, and Java**.

Looking for Go? → **[aligate-io/aliexpress-go](https://github.com/aligate-io/aliexpress-go)**.

If you've been searching for an **AliExpress product data API**, an **AliExpress API on RapidAPI**,
an **AliExpress image search API**, or an **AliExpress price API**, these SDKs are the quickest way
to integrate it — useful for **dropshipping**, **price monitoring**, catalog enrichment, and
e-commerce product research.

---

## Packages

| Language | Package | Install |
| --- | --- | --- |
| Python | [`aligate`](https://pypi.org/project/aligate/) (PyPI) | `pip install aligate` |
| Node.js | [`@aligate/sdk`](https://www.npmjs.com/package/@aligate/sdk) (npm) | `npm install @aligate/sdk` |
| Java | `io.aligate:aligate-sdk` (Maven Central) | see [Java](#java) |
| Go | [`aligate-io/aliexpress-go`](https://github.com/aligate-io/aliexpress-go) | `go get github.com/aligate-io/aliexpress-go/v2` |

---

## What you can do

| Operation | Description |
| --- | --- |
| **Product data** | Full product detail by product ID: pricing, SKUs/variants, stock, shipping, seller, optional description — per country & currency. |
| **Product reviews** | Paginated buyer reviews with rating breakdown, filters, and sorting. |
| **Seller / store info** | Store profile: ratings, feedback, followers, store age, categories. |
| **Seller coupons** | Active store coupon campaigns, scoped to country & currency. |
| **Seller products** | A store's product catalog, paginated and best-selling first. |
| **Text search** | Products matching a keyword, plus category facets. |
| **Image search** | Products visually matching an uploaded image. |

Prices, shipping, and search results are resolved for the requested **country** and **currency**.

---

## Authentication

The AliGate AliExpress Data API is served through **RapidAPI**. Every request (except the health
check) needs two headers:

| Header | Value |
| --- | --- |
| `x-rapidapi-key` | Your RapidAPI key |
| `x-rapidapi-host` | `aligate-aliexpress-data-api.p.rapidapi.com` |

Base URL: `https://aligate-aliexpress-data-api.p.rapidapi.com`

Get a key from the **[AliGate listing on RapidAPI](https://rapidapi.com/aligate/api/aligate-aliexpress-data-api)** (linked from
[aligate.io/docs](https://aligate.io/docs)). The SDKs accept your RapidAPI key and attach the
required headers for you.

---

## Quickstart

> Examples are illustrative; the exact surface is produced by the SDK generator. Each published
> package ships its own detailed README on its package page.

### Python

```python
import aligate

config = aligate.Configuration(host="https://aligate-aliexpress-data-api.p.rapidapi.com")
client = aligate.ApiClient(config)
client.default_headers["x-rapidapi-key"] = "YOUR_RAPIDAPI_KEY"
client.default_headers["x-rapidapi-host"] = "aligate-aliexpress-data-api.p.rapidapi.com"

api = aligate.DefaultApi(client)
res = api.get_product_info(product_id=1005004530469845, country="PL", currency="PLN")
print(res.item.title)
```

### Node.js

```ts
import { DefaultApi, Configuration } from "@aligate/sdk";

const api = new DefaultApi(new Configuration({
  basePath: "https://aligate-aliexpress-data-api.p.rapidapi.com",
  baseOptions: {
    headers: {
      "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
      "x-rapidapi-host": "aligate-aliexpress-data-api.p.rapidapi.com",
    },
  },
}));

const res = await api.getProductInfo(1005004530469845, "PL", "PLN");
console.log(res.data.item?.title);
```

### Java

```xml
<dependency>
  <groupId>io.aligate</groupId>
  <artifactId>aligate-sdk</artifactId>
  <version>2.1.1</version>
</dependency>
```

```java
import io.aligate.sdk.ApiClient;
import io.aligate.sdk.api.DefaultApi;

ApiClient client = new ApiClient();
client.setRequestInterceptor(b -> b
    .header("x-rapidapi-key", "YOUR_RAPIDAPI_KEY")
    .header("x-rapidapi-host", "aligate-aliexpress-data-api.p.rapidapi.com"));

DefaultApi api = new DefaultApi(client);
var res = api.getProductInfo(1005004530469845L, "PL", "PLN");
System.out.println(res.getItem().getTitle());
```

### Go

See **[aligate-io/aliexpress-go](https://github.com/aligate-io/aliexpress-go)**.

---

## Documentation

- **Docs:** [aligate.io/docs](https://aligate.io/docs) — with a page per language.
- **API key & plans:** [AliGate on RapidAPI](https://rapidapi.com/aligate/api/aligate-aliexpress-data-api).
- Each published package (PyPI / npm / Maven Central) includes its own generated reference.

---

## Versioning

All SDKs share a single version that tracks the API version, so a given SDK version maps to a known
API version (e.g. API `2.1` → SDK `2.1.x`). The clients are generated from the AliGate API's
OpenAPI specification.

---

## Disclaimer

**Unofficial.** AliGate is an independent third-party service and is **not affiliated with,
endorsed by, or sponsored by Alibaba Group or AliExpress**. "AliExpress" is a trademark of its
respective owner and is used here only to describe the data this API provides.

---

## Support

- Website & docs: [aligate.io](https://aligate.io) · [aligate.io/docs](https://aligate.io/docs)
- Email: [admin@aligate.io](mailto:admin@aligate.io)
- Issues with the SDKs: open an issue in this repository.

## License

See [LICENSE](LICENSE).
