function analyticsObj(key) {
    var self = this;
    this.makeID = function (l) {
        var output = "";
        var chars = "123456789ABCDEFG";
        for (var i = 0; i < l; i++)
            output += chars.charAt(Math.floor(Math.random() * chars.length));

        return output;
    }
    this.setCookie = function (name, value, days) {
        var expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/";
    }
    this.getCookie = function (name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }
    this.eraseCookie = function (name) {
        document.cookie = name + '=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
    this.reset = function () {
        self.eraseCookie('cc_cookie')
        self.eraseCookie('antbits_analytics')
        console.log('cookies cleared')
    }
    this.init = function (key) {
        var permissions = JSON.parse(self.getCookie('cc_cookie'))
        if (permissions != null) {
            if (permissions.categories.includes('analytics')) {
                var analyticsObj = self.getCookie('antbits_analytics')
                var now = Date.now();
                if (analyticsObj === null) {
                    analyticsObj = { 'session': { 'id': 'Safeguarding-Web', 'a': 'start', 'v': 1, 'date': now, 'uid': self.makeID(16), 'journey_id': self.makeID(16) } }
                } else {
                    analyticsObj = JSON.parse(analyticsObj)
                    if (now - 180000 > parseInt(analyticsObj.session.date)) {
                        analyticsObj.session['a'] = 'return'
                        analyticsObj.session['v'] = analyticsObj.session['v'] + 1
                        analyticsObj.session['journey_id'] = self.makeID(16)
                    } else {
                        analyticsObj.session['a'] = 'nav'
                    }
                    analyticsObj.session['date'] = now;
                }
                var tmp = window.location.pathname.split('/')
                var endpoint = 'https://preview.antbits.com/tracking/tracker.gif?'
                analyticsObj.session['l2'] = ''
                analyticsObj.session['l3'] = ''
                analyticsObj.session['plat'] = isMobile.any() ? (isMobile.iOS() ? 'iOS' : 'Android') : 'desktop'
                if (tmp.length > 2) {
                    if (tmp[1].length > 0) {
                        analyticsObj.session['l2'] = tmp[1]
                    }
                    if (tmp[2].length > 0) {
                        analyticsObj.session['l3'] = tmp[2]
                    }
                }
                self.setCookie('antbits_analytics', JSON.stringify(analyticsObj), 365)
                for (var key in analyticsObj.session) {
                    endpoint += key + '=' + analyticsObj.session[key] + '&'
                }

                var request = new XMLHttpRequest();
                request.open('GET', endpoint.slice(0,-1), true);
                request.send();

            }
        }


    }
}
var analyticsObj = new analyticsObj(window.location)