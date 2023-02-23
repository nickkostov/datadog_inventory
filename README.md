
How to use:
```bash
DD_SITE="datadoghq.<?>" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "dd-gen-inventory.py"
```

Created with the help of:

[DataDog Monitor API](https://docs.datadoghq.com/api/latest/monitors/)


```python
pip3 install pandas
```
```python
pip3 install datadog-api-client
```

To do:
- [ ] Add inventory of all users in current datadog org
- [ ] Get the API/APP credentials and URL from a config file under .datadog/credentials.
- [ ] Get all hosts that have datadog agent installed
- [ ] Get all hosts that do not have datadog agent installed