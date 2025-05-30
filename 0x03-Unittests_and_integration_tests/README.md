# 🧪 TestAccessNestedMap

Unit tests for the `access_nested_map` function from `utils.py`, using `unittest` and `parameterized`.

## ✅ What It Tests

`access_nested_map(nested_map, path)` should return the value found by traversing `nested_map` with the keys in `path`.

### Example Cases

| Expected | Nested Map            | Path        |
|----------|------------------------|-------------|
| `1`      | `{"a": 1}`             | `("a",)`    |
| `{"b":2}`| `{"a": {"b": 2}}`      | `("a",)`    |
| `2`      | `{"a": {"b": 2}}`      | `("a", "b")`|

## 🛠️ Run Tests

```bash
pip install parameterized
python3 test_utils.py
