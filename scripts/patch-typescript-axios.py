#!/usr/bin/env python3
"""Annotate createRequestFunction's return type in the generated TypeScript client.

Backport of openapi-generator PR #24526 (merged 2026-07-30, master only — it is in
neither 7.23.0 nor 7.24.0).

Why: 7.23.0's typescript-axios/common.mustache emits `createRequestFunction` with no
explicit return type. axios >= 1.19.0 defaults `AxiosInstance.request`'s `R` to
`AxiosResponseDefault = typeof axiosResponseDefault`, an un-exported `unique symbol`
(axios index.d.ts:568), so `tsc` with `declaration: true` cannot name the inferred
type and fails the build with:

    common.ts(122,14): error TS2527: The inferred type of 'createRequestFunction'
    references an inaccessible 'unique symbol' type. A type annotation is necessary.

The generated package.json floats `axios: "^1.16.0"` and there is no lockfile
(scripts/generate.sh wipes generated/ every run), so CI resolved 1.18.1 in July and
1.19.0 afterwards — same commit, different outcome.

Remove this script and its call sites when openapitools.json's generator-cli.version
is bumped to a release containing #24526. Until then it is a no-op on already-fixed
output, so a premature bump degrades gracefully. Find the call sites with:

    grep -rn patch-typescript-axios .

Call it from the workflow, NOT from scripts/generate.sh: generate.sh writes through a
root Docker container and the workflow's "Fix generated file ownership" chown runs
after it, so patching inside generate.sh would fail with PermissionError on CI.

Usage: patch-typescript-axios.py path/to/generated/typescript/common.ts
"""
import sys

ARROW_OLD = "basePath: string = BASE_PATH) => {"
ARROW_NEW = "basePath: string = BASE_PATH): Promise<R> => {"
RETURN_OLD = "return axios.request<T, R>(axiosRequestArgs);"
RETURN_NEW = "return axios.request<T, R>(axiosRequestArgs) as Promise<R>;"


def main(path: str) -> None:
    src = open(path, encoding="utf-8").read()
    if ARROW_NEW in src and RETURN_NEW in src:
        print("common.ts already has the #24526 fix; nothing to do")
        return
    # Exactly one occurrence each, or we are patching output we do not recognise.
    if src.count(ARROW_OLD) != 1 or src.count(RETURN_OLD) != 1:
        sys.exit(
            f"unexpected generator output in {path}: expected exactly one of each\n"
            f"  {ARROW_OLD!r}\n"
            f"  {RETURN_OLD!r}\n"
            f"got {src.count(ARROW_OLD)} and {src.count(RETURN_OLD)}. Check whether "
            "openapi-generator PR #24526 shipped in the pinned generator version — if "
            "it did, delete scripts/patch-typescript-axios.py and its call sites; if "
            "not, re-derive the anchors above from the new output."
        )
    src = src.replace(ARROW_OLD, ARROW_NEW, 1).replace(RETURN_OLD, RETURN_NEW, 1)
    open(path, "w", encoding="utf-8").write(src)
    print("annotated createRequestFunction's return type in", path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: patch-typescript-axios.py path/to/common.ts")
    main(sys.argv[1])
