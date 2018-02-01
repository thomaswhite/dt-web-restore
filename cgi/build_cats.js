window.onload = function () {
    url = "http://weeklyedit.com/cgi/build_topics.cgi";
    var ajax_cats = new XMLHttpRequest();
    ajax_cats.onreadystatechange = function () {
        if (ajax_cats.readyState == 4) {
            if (ajax_cats.status == 200 || ajax_cats.status == 0) {
                ajax_cats_r = decodeURIComponent(ajax_cats.responseText);
                var ajax_cats_out = '';
                var ajax_cats_l = ajax_cats_r.split("\n");
                for (var i = 0; i < ajax_cats_l.length; i++) {
                    ajax_cats_out = ajax_cats_out + ajax_cats_l[i] + '<BR>';
                }
                document.getElementById('topics').innerHTML = ajax_cats_out;
            }
        }
    }
    ajax_cats.open("GET", url, false);
    ajax_cats.send();
    url = "http://weeklyedit.com/cgi/build_modules.cgi";
    var ajax_cats = new XMLHttpRequest();
    ajax_cats.onreadystatechange = function () {
        if (ajax_cats.readyState == 4) {
            if (ajax_cats.status == 200 || ajax_cats.status == 0) {
                ajax_cats_r = decodeURIComponent(ajax_cats.responseText);
                var ajax_cats_out = '';
                var ajax_cats_l = ajax_cats_r.split("\n");
                for (var i = 0; i < ajax_cats_l.length; i++) {
                    ajax_cats_out = ajax_cats_out + ajax_cats_l[i] + '<BR>';
                }
                document.getElementById('modules').innerHTML = ajax_cats_out;
            }
        }
    }
    ajax_cats.open("GET", url, false);
    ajax_cats.send();
}
