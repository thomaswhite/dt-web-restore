window.onload = function() {
  var query = window.location.search.substring(1);
  var path = window.location.pathname;
  switch (path) {
    case "/playlist/":
      url="http://weeklyedit.com/cgi/build_playlist.cgi?"+query
      break;
    case "/shoot-with-harry/":
      url="http://weeklyedit.com/cgi/build_shootwithharry.cgi";
      break;
    case "/patreon-support/":
      url="http://weeklyedit.com/cgi/build_patreonsupport.cgi";
      break;
    case "/my-workflow/":
      url="http://weeklyedit.com/cgi/build_myworkflow.cgi";
      break;
    case "/edit-my-raw/":
      url="http://weeklyedit.com/cgi/build_editmyraw.cgi";
      break;
    case "/about-us/":
      url="http://weeklyedit.com/cgi/build_aboutus.cgi";
      break;
    case "/awesome-links/":
      url="http://weeklyedit.com/cgi/build_awesomelinks.cgi";
      break;
    case "/tpe/":
      url="http://weeklyedit.com/cgi/build_tpe.cgi";
      break;
    case "/order-prints-of-my-work/":
      url="http://weeklyedit.com/cgi/build_orderprintsofmywork.cgi";
      break;
    case "/lab-reference-chart/":
      url="http://weeklyedit.com/cgi/build_labreference.cgi";
      break;
    case "/show-suggestions/":
      url="http://weeklyedit.com/cgi/build_showsuggestions.cgi";
      break;
    default:
      url="http://weeklyedit.com/cgi/build_links.cgi?title="+document.title;
      break;
  }
  var aj=new XMLHttpRequest();
  aj.onreadystatechange = function () {
    if (aj.readyState == 4 ) {
      if ( aj.status == 200 || aj.status == 0 ) {
        aj_r = decodeURIComponent(aj.responseText);
        var aj_out='';
        var aj_l = aj_r.split("\n");
        for (var i= 0; i < aj_l.length; i++) {
          aj_out=aj_out+aj_l[i]+'<BR>';
        }
        document.getElementById('results').innerHTML = aj_out;
      }
    }
  }
  aj.open("GET", url, false);
  aj.send();
}
