var VERSION = "1.0b4";
var UPDATE_TIME = "2004-8-17";

function prt(str) {
	document.write(str);
}
function writeTop() {
	prt("<table class=\"HeaderTable\" width=\"760\" cellpadding=\"4\" align=\"center\">");
	prt("<tr>");
    prt("<td width=\"100%\" height=\"36\">JavaScript Validation Framework</td> ");
	prt("<td class=\"VersionText\" valign=\"bottom\">"+VERSION+"</td>");
	prt("</tr>");
	prt("</table>");
}


function writeNav() {
	var str = "";
	str+="::����::";
	str+="<ul>";
	str+="<li><a href=\"index.html\">��ҳ</a></li>";
	str+="<li><a href=\"download.html\">����</a></li>";
	str+="<li><a href=\"userguide.html\">�û��ֲ�</a></li>";
	str+="<li><a href=\"devguide.html\">����ָ��</a></li>";
	str+="<li><a href=\"demo.html\">��ʾ</a></li>";
	str+="<li><a href=\"faq.html\">FAQ</a></li>";
	str+="<li><a href=\"contributors.html\">������</a></li>";
	str+="</ul>";

	prt(str);
}