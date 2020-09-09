var contentHeight = $('.content').height()
var windowHeight = window.innerHeight
var footHeight = $('footer').height()


if (contentHeight+footHeight+20 < windowHeight) {
  console.log('change');
  $('footer').offset({top: windowHeight-footHeight-20})
}
