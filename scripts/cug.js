var str = $response.body;

var json = JSON.parse(str);

var url = $request.url;

if (url.endsWith('%E5%AE%A1%E6%A0%B8%E9%80%9A%E8%BF%87') || url.endsWith('all')) {
    var myDate = new Date();
    var year = myDate.getFullYear();
    var month = myDate.getMonth() + 1;
    var date = myDate.getDate();
    if (month < 10) {
        month = "0" + month;
    }
    if (date < 10) {
        date = "0" + date;
    }
    var dateStr = year + "-" + month + "-" + date;

    json.rows[0].outtimetext = dateStr + ' 08:35:59'
    json.rows[0].backtimetext = dateStr + ' 23:35:59';
}

$done({ body: JSON.stringify(json) });
