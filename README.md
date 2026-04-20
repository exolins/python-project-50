### Hexlet tests and linter status:
[![Actions Status](https://github.com/exolins/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/exolins/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=exolins_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=exolins_python-project-50)
[![asciicast](https://asciinema.org/a/YFp6AhRnhU8ZHqmO.svg)](https://asciinema.org/a/YFp6AhRnhU8ZHqmO)
# Install
```
make build
make package-install
```

# Usage
Supported file formats:
- JSON
- YAML
Output format:
- Stylish (default)
- Plain
- JSON
## Stylish view
```
gendiff file1.json file2.json
gendiff file1.json file2.json -f stylish
```
## Plain view
```
gendiff file1.json file2.json -f plain
```
## JSON view
```
gendiff file1.json file2.json -f json
```
