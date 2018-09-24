$(document).ready(function(){
    $('bt-add').click(function(){
        $("pa-c").append(
           "<div><select class= \"form-control\" >{% for item in stuff_type %}<option>{{item}}</option>{%endfor%}</select></div>"
        )
    })
})

