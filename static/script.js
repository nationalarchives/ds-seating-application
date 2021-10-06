var check_researching_by_self = function () {
    var ischecked = $("#researchingbyself_yes").is(":checked");
    if (ischecked) {
        $("#quietzone").show();
        $("#quietzone_yes").prop("disabled", false);
        $("#quietzone_no").prop("disabled", false);
    } else {
        $("#quietzone").hide();
        $("#quietzone_yes").prop("checked", false);
        $("#quietzone_no").prop("checked", false);
        $("#quietzone_yes").prop("disabled", true);
        $("#quietzone_no").prop("disabled", true);
    }
}
$(document).ready(function () {
    check_researching_by_self();
});
$("#researchingbyself").on('change', function () {
    check_researching_by_self();
})