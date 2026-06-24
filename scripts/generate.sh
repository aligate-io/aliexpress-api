#!/usr/bin/env bash
#
# Generate the Python, TypeScript (axios) and Java clients from openapi.yaml using the
# pinned OpenAPI Generator Docker image. Output goes to generated/{python,typescript,java}.
#
# Usage:  scripts/generate.sh [VERSION]
#   VERSION  semver stamped into each package (default: derived from the spec's info.version).
#
# Requires: docker. No local Java/Node/Python toolchain needed to generate.
set -euo pipefail

# Repo root = parent of this script's dir.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

GEN_VERSION="$(grep -o '"version": *"[0-9.]*"' openapitools.json | head -1 | grep -o '[0-9.]*')"
IMAGE="openapitools/openapi-generator-cli:v${GEN_VERSION}"

# SDK version: explicit arg, else the spec's info.version normalized to semver (X.Y -> X.Y.0).
SDK_VERSION="${1:-}"
if [[ -z "$SDK_VERSION" ]]; then
  RAW="$(grep -E '^  version:' openapi.yaml | head -1 | sed -E 's/.*version:[[:space:]]*"?([0-9.]+)"?.*/\1/')"
  case "$(grep -o '\.' <<<"$RAW" | wc -l | tr -d ' ')" in
    0) SDK_VERSION="${RAW}.0.0" ;;
    1) SDK_VERSION="${RAW}.0" ;;
    *) SDK_VERSION="$RAW" ;;
  esac
fi
echo "▶ generator=${IMAGE}  sdk_version=${SDK_VERSION}"

rm -rf generated
mkdir -p generated

run() { docker run --rm -v "${ROOT}:/local" "$IMAGE" "$@"; }

echo "▶ validating spec"
run validate -i /local/openapi.yaml

echo "▶ generating python"
run generate -i /local/openapi.yaml -g python -o /local/generated/python \
  -c /local/config/python.json \
  --additional-properties=packageVersion="${SDK_VERSION}"

echo "▶ generating typescript-axios"
run generate -i /local/openapi.yaml -g typescript-axios -o /local/generated/typescript \
  -c /local/config/typescript-axios.json \
  --additional-properties=npmVersion="${SDK_VERSION}"

echo "▶ generating java (native)"
run generate -i /local/openapi.yaml -g java -o /local/generated/java \
  -c /local/config/java.json \
  --additional-properties=artifactVersion="${SDK_VERSION}"

echo "✅ generated all clients into ${ROOT}/generated"
