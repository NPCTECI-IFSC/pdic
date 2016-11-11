var getOptions = function(a, b, c, d) {
    b ? $.ajax({
        method: "GET",
        url: "/api/" + d + b,
        success: function(b) {
            var d = "<option value=''>Selecione</option>";
            a.removeAttr("disabled"), b.forEach(function(a) {
                d += "<option value='" + a.id + "'>" + a[c] + "</option>"
            }), a.html(d)
        }
    }) : $(".combo").html("").attr("disabled", "")
};
