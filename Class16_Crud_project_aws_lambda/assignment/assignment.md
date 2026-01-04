# 🐍 AWS Lambda Runtime Updater

## Overview

This Python script automates the process of updating **AWS Lambda functions** to a target Python runtime version based on specific **tags**.

It iterates through all Lambda functions in your AWS account, checks for a matching tag (`key=value`), and updates those functions to the specified target runtime.

The script is designed to be **educational and beginner-friendly**, using a simple manual pagination approach instead of AWS paginators.

---

## ✨ Features

- ✅ Filters Lambda functions by tag key and value  
- ✅ Updates runtime only for matching functions  
- ✅ Supports **dry-run mode** (no real updates, only prints actions)  
- ✅ Handles pagination using the `Marker` / `NextMarker` pattern  
- ✅ Captures success, skip, and error results cleanly  

---

## 🧩 Function Description

### `update_python_runtime(target_runtime, tag_key, tag_value, dry_run=False)`

**Purpose:**  
Update all AWS Lambda functions with a specific tag (`tag_key=tag_value`) to the given `target_runtime`.

**Parameters:**

| Name | Type | Description |
|------|------|--------------|
| `target_runtime` | `str` | The desired runtime version (e.g. `"python3.13"`) |
| `tag_key` | `str` | The Lambda tag key to filter by |
| `tag_value` | `str` | The Lambda tag value to match |
| `dry_run` | `bool` | If `True`, only prints what would be updated (no actual change) |

**Returns:**
A list of tuples in the form:
```python
[
    ("function_name", "old_runtime", "new_runtime_or_reason"),
    ...
]
