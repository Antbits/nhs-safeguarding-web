var pagetype = '';
// funcs
var wrap = function (toWrap, wrapper) {
    wrapper = wrapper || document.createElement('div');
    toWrap.parentNode.appendChild(wrapper);
    return wrapper.appendChild(toWrap);
};
// format links
var links = document.getElementsByTagName("a");
for (var i = 0;i < links.length;i++) {
    var str = links[i].innerHTML
    var href = links[i].getAttribute('href')
    var id = links[i].getAttribute('id')
    var classes = document.getElementById('page-content').classList
    if(href.slice(0,1) == '#' && id != null){
        links[i].classList.add('anchor')
        links[i].removeAttribute('href')
    } else if(href.slice(-4)== '.pdf'){
        links[i].setAttribute("target", "_new");
    }
    if (href.slice(0,4) === 'http' || href.slice(0,4) === 'www.' || href.indexOf('@') > -1) {
       links[i].classList.add('external')
    }
}
// format images
var images = document.getElementsByTagName("img");
if (images.length > 0) {
    for (var i =0;i<images.length;i++) {
        images[i].removeAttribute('width')
        images[i].removeAttribute('height')
    }
}
// App store redirects
if(window.location.pathname === '/'){
    if(isMobile.iOS()){
        document.body.classList.add('iOS')
    }
    if(isMobile.Android()){
        document.body.classList.add('Android')
    }
}


const deviceType = () => {
    const ua = navigator.userAgent;
    if (/(tablet|ipad|playbook|silk)|(android(?!.*mobi))/i.test(ua)) {
        return "tablet";
    }
    else if (/Mobile|Android|iP(hone|od)|IEMobile|BlackBerry|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(ua)) {
        return "mobile";
    }
    return "desktop";
};
const validateSearchForm = (event) =>{
    if(document.getElementById('search-text').value.length < 3){
        event.preventDefault();
    }
}
document.body.addEventListener("keydown", function (event) {
    if(event.keyCode === 9){
        document.body.classList.add('keynav')
    }
})
document.body.addEventListener("click", function (event) {
    document.body.classList.remove('keynav')  
})

