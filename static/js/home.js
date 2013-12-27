$(function(){
	$(".moods-list").click(function(){
		var	id = $(this).attr("data-id")
		$.ajax({
			type:'GET',
			url:'/view',
			data:{"id":id},
			success:function(data){
				console.log(data.id)
			}
		})
	})
})
