var isMobile = {
    Android: function() {
        return navigator.userAgent.match(/Android/i) ? true : false;
    },
	Tablet: function() {
        return navigator.userAgent.match(/iPad|(?!.*mobile).*Android*/i) ? true : false;
    },
    iOS: function() {
        return navigator.userAgent.match(/iPhone|iPad|iPod/i) ? true : false;
    },
    any: function() {
        return (isMobile.Android() || isMobile.iOS());
    }
};