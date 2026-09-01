#!/bin/sh
# Assemble the public site into _dist/ — only the files that should be on the
# internet. Internal material (the client questionnaire PDF, client-answers.md,
# voice-spec.md, the page generator) is deliberately left out.
#
# The leading underscore is load-bearing: claude-os's Design tab walks this
# folder for HTML and skips "_"-prefixed directories. Named "dist", the build
# output shows up as a second, duplicate copy of every page in the Design tab.
set -e
rm -rf _dist
mkdir -p _dist
cp index.html about.html service-*.html _dist/
cp -R public _dist/public
echo "_dist/ built:"
find _dist -type f | sort
