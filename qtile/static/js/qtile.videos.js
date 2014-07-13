var init_videos = function(video_list){
    (function($){
        $(document).ready(function(){
            var render = tmpl('video_detail'),
                loading = tmpl('loading'),
                $container = $('#video_container');

            // If no content has loaded after 500ms, display a loading spinner
            setTimeout(function(){
                if($container.is(':empty')){
                    $container.append(loading({}));
                }
            }, 500);

            // Fetch the video data via noembed and render each video
            $.each(video_list, function(index, video_url){
                var url = 'http://noembed.com/embed?nowrap=on&url=' + video_url;
                $.getJSON(url, function(data){
                    $container.find('.loading').remove();
                    $container.append(render(data));
                });
            });
        });
    })(jQuery);
};
