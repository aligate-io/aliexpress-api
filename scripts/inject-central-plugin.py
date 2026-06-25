#!/usr/bin/env python3
"""Inject the Sonatype central-publishing-maven-plugin into a generated pom.xml.

OpenAPI Generator's Java pom has GPG signing (in the `sign-artifacts` profile) and
source/javadoc jars, but not the Central Portal publishing plugin. We add it to the
build <plugins> so `mvn deploy` uploads to Maven Central. Idempotent.

Usage: inject-central-plugin.py path/to/pom.xml
"""
import sys

PLUGIN = """            <plugin>
                <groupId>org.sonatype.central</groupId>
                <artifactId>central-publishing-maven-plugin</artifactId>
                <version>0.11.0</version>
                <extensions>true</extensions>
                <configuration>
                    <publishingServerId>central</publishingServerId>
                    <autoPublish>true</autoPublish>
                    <waitUntil>published</waitUntil>
                </configuration>
            </plugin>
"""

def main(path: str) -> None:
    pom = open(path, encoding="utf-8").read()
    if "central-publishing-maven-plugin" in pom:
        print("central-publishing-maven-plugin already present; nothing to do")
        return
    # The build section's closing tag is indented 8 spaces; the profile's is deeper,
    # so this targets the build <plugins> only.
    marker = "        </plugins>"
    if marker not in pom:
        sys.exit("could not find build </plugins> marker in pom.xml")
    pom = pom.replace(marker, PLUGIN + marker, 1)
    open(path, "w", encoding="utf-8").write(pom)
    print("injected central-publishing-maven-plugin into", path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: inject-central-plugin.py path/to/pom.xml")
    main(sys.argv[1])
