var isAjaxSupported = (window.ActiveXObject != "undefined" || window.XMLHttpRequest != "undefined");
function $(id) {
    return document.getElementById(id);
}

function getBrowser() {
    var b = navigator.userAgent.toLowerCase();
    return {
        safari: /webkit/.test(b),
        opera: /opera/.test(b),
        ie6: /msie 6/.test(b) && !/opera/.test(b),
        ie7: /msie 7/.test(b) && !/opera/.test(b),
        msie: /msie/.test(b) && !/opera/.test(b),
        mozilla: /mozilla/.test(b) && !/(compatible|webkit)/.test(b)
    };
}

function copyCode(e) {
    var text = '';
    if (typeof e != 'string') {
        var iptEle = e.parentNode.parentNode.getElementsByTagName('input')[0];
        iptEle.select();
        text = iptEle.value;

    }
    else
        text = e;
    var browser = getBrowser()
    if (browser.ie6) {
       window.clipboardData.setData('text', text);
       alert('已经复制!');
    }
}
