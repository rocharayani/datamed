 
 //i am assuming you are searching through a table...
    //search input field listening for key pressed
    $('#busca').keyup(function (e) {
        //listening if the key pressed is the enter button
        if (e.which === 13) {
            //inserting the value of textfield content, you can add if statement to check if the field is null or empty
            var search_param = $(this).val();
            //value of field stored into a variable
            $('tr').removeClass('item_found');
            //remove item_found class attributed to a td AND search all td to find the one that march the search parameter
            if ($('td:contains("' + search_param + '")').html() !== undefined) {
                //if there is any td that has that record... then check for the closest tr and add a class with item_found as value
                $('td:contains("' + search_param + '")').closest('tr').attr('class', 'item_found');
                //add some highlight to it.
                $('td:contains("' + search_param + '")').closest('tr').css({background:'yellow',color:'black'});
                //then scroll to the item
                $(window).scrollTop($('.item_found').first().offset().top);
            } else {
                //if item is not found display no result found
                alert("Sorry no result found")
            }
        }
    });