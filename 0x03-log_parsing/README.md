# 0x03. Log Parsing

`Focus`: `Algorith` `Python`

Write a script that reads stdin line by line and computes metrics:

<ul><li>Input format: `IP Address` - `date` `GET /projects/260 HTTP/1.1` `status code file size` (if the format is not this one, the line must be skipped)</li>
<li>After every 10 lines and/or a keyboard interruption `(CTRL + C)`, print these statistics from the beginning:
<ul><li>Total file size: `File size: total size`</li>
<li>where `total size` is the sum of all previous `file size` (see input format above)</li>
<li>Number of lines by status code:
<ul><li>possible status code: `200, 301, 400, 401, 403, 404, 405 and 500`</li>
<li>if a status code doesn’t appear or is not an integer, don’t print anything for this status code</li>
<li>format: `status code: number`</li>
<li>status codes should be printed in ascending order</li></ul></li></ul></li></ul>

**Warning:** In this sample, you will have random value - it’s normal to not have the same output as this one.
