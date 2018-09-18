(function() {
  init();

  function init() {
    $('.query-params-button').click(function(event) {
      var queryParams = $('.query-params-value').val();

      createIframe(queryParams);
    });
  }

  function createIframe(queryParams){
    var basePath = $('.base-path').val();

    if (!basePath && !queryParams) return;

    var i = document.createElement("iframe");
    console.log(basePath+'?'+queryParams);
    i.src = basePath+'?'+queryParams;
    i.frameborder = "0";
    i.style.cssText = "border:0";
    i.width = "100%";
    i.height = "690px";
    $("#wkdaIframe").empty().append(i);
  };
})();
