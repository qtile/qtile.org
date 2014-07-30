var init_videos = function(video_list){
    (function($){
        $(document).ready(function(){
            var render = tmpl('video_detail'),
                loading = tmpl('loading'),
                still_loading = tmpl('still_loading'),
                $container = $('#video_container');

            // If no content has loaded after 1 second, display a loading spinner
            setTimeout(function(){
                if($container.is(':empty')){
                    $container.append(loading({}));
                }
            }, 1000);

            // Fetch the video data via noembed and render each video
            $.each(video_list, function(index, video){
                var url = 'http://noembed.com/embed?nowrap=on&url=' + video.url;
                $.getJSON(url, function(data){
                    $container.find('.loading').remove();
                    $container.append(render(data));
                });
            });
        });
    })(jQuery);
};
