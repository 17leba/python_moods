$(function(){
	var home = {
		init:function(){
			this.renderPost();
			this.closePost()
		},
		renderPost:function(){
			var $moodList = $(".moods-list");
			$moodList.on("click",function(){
				$(".mask").removeClass("hide")
				var $this = $(this),
				    postId = $this.attr("data-id"),
				    html = '';
				$.ajax({
					url:"/view",
					data:{"postId":postId},
					success:function(res){
						html= '<p class="post-content">'+res.content+'<span class="post-time">'+res.posted_on+'</span></p>';
						$(html).appendTo($(".post-detail-zone"))
					}
				})
			})
		},
		closePost:function(){
			$(".close-btn").on("click",function(){
				$(".mask").addClass("hide");
				$(".post-detail-zone").html("")
			})
		}
	}
	home.init()
})
