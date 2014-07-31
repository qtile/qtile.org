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

var init_screenshot_lightbox = function(){
    (function($){
        $(document).ready(function(){
            $('.screenshot.thumbnail a.fullsize').on('click', function(){
                console.log('WTF IS THIS');
                var $this = $(this),
                    $modal = $('#lightbox');

                $modal.find('.modal-title, .modal-body, .modal-footer').empty();

                $modal.find('.modal-title').text($this.data('title'));
                $modal.find('.modal-body').html(
                    $('<a>')
                        .attr('href', $this.attr('href'))
                        .html(
                            $('<img>')
                                .attr('src', $this.attr('href'))
                                .attr('alt', $this.data('title'))
                                .addClass('thumbnail')
                        )
                );

                if($this.data('config')) {
                    $modal.find('.modal-footer').html(
                        $('<a>')
                            .text(' View Config')
                            .attr('href', $this.data('config'))
                            .prepend(
                                $('<span>').addClass('fa fa-fw fa-cogs text-muted')
                            )
                    );
                }
                $modal.modal({show: true});
                return false;
            });
        });
    })(jQuery);
};
