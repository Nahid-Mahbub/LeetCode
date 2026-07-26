#!/usr/bin/env python3

import os
import re
import shutil
import requests
import time

# ==========================
# CONFIGURATION
# ==========================
ROOT = "/run/media/nahid-mahbub/New Drive/University/Programing/LeetCode/Python"

GRAPHQL_URL = "https://leetcode.com/graphql"

# Create destination folders
for folder in ["Easy", "Medium", "Hard"]:
    os.makedirs(os.path.join(ROOT, folder), exist_ok=True)


def camel_to_slug(name):
    """
    addBinary -> add-binary
    longestCommonPrefix -> longest-common-prefix
    """
    name = os.path.splitext(name)[0]
    slug = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', name)
    return slug.lower()


def get_difficulty(slug):
    query = """
    query getQuestion($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        difficulty
      }
    }
    """

    variables = {"titleSlug": slug}

    try:
        response = requests.post(
            GRAPHQL_URL,
            json={"query": query, "variables": variables},
            timeout=10,
        )

        data = response.json()

        if (
            "data" in data
            and data["data"]["question"] is not None
        ):
            return data["data"]["question"]["difficulty"]

    except Exception:
        pass

    return None


for filename in os.listdir(ROOT):

    path = os.path.join(ROOT, filename)

    if os.path.isdir(path):
        continue

    if not filename.endswith(".py"):
        continue

    slug = camel_to_slug(filename)

    print(f"Checking {filename} -> {slug}")

    difficulty = get_difficulty(slug)

    if difficulty is None:
        print("  ❌ Not found")
        continue

    destination = os.path.join(ROOT, difficulty)

    shutil.move(path, os.path.join(destination, filename))

    print(f"  ✅ {difficulty}")

    time.sleep(0.3)

print("\nFinished!")
