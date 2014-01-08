$(function(){
	var $mask = $(".mask");
	var home = {
		init:function(){
			this.renderPost();
			this.addPostShow();
			this.closePost()
		},
		renderPost:function(){
			var $moodList = $(".moods-list");
			$moodList.on("click",function(){
				$mask.append($("#post-detail").text());
				$mask.removeClass("hide");
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
		addPostShow:function(){
			var $addBtn = $(".add-post-btn");
			$addBtn.on("click",function(){
				$mask.append($("#add-post").text());
				$mask.removeClass("hide");
			})
		},
		addPost:function(){
			var $addPostBtn = $("")
		},
		closePost:function(){
			$(".close-btn").live("click",function(){
				$mask.addClass("hide");
				if($(".popup").length){
					$(".popup").remove()
				}
			})
		}
	}
	home.init()
})
