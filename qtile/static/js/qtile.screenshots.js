var init_screenshots = function(){
    (function($){
        var init_masonry = function($gallery){
            $gallery.masonry({
                columnsWidth: '.gallery-item',
                gutter: 0,
                isAnimated: true,
                itemSelector: '.gallery-item'
            });
        };

        $(document).ready(function(){
            var $gallery = $('.gallery');

            $gallery.find('.gallery-item').each(function(){
                var $this = $(this);
                console.log($this);
                if($this.hasClass('width-1')){
                    $this.addClass('col-xs-12 col-sm-4 col-md-3');
                } else if($this.hasClass('width-2')){
                    $this.addClass('col-xs-12 col-sm-6 col-md-6');
                } else if($this.hasClass('width-3')){
                    // Some day...
                    $this.addClass('col-xs-12 col-sm-12 col-md-9');
                } else {
                    $this.addClass('col-xs-12');
                }
            });

            $gallery.imagesLoaded(function(){ init_masonry($gallery); });
            $(window).resize(function(){ init_masonry($gallery); });
        });
    })(jQuery);
};
