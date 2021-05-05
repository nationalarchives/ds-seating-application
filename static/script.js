var check_researching_by_self = function () {
    var ischecked = $("#researchingbyself_yes").is(":checked")
    if (ischecked) {
        $("#quietzone").show()
    } else {
        $("#quietzone").hide()
        $("#quietzone_yes").prop("checked", false)
        $("#quietzone_no").prop("checked", false)
    }
}
$(document).ready(function () {
    check_researching_by_self()
});
$("#researchingbyself").on('change', function () {
    check_researching_by_self();
})