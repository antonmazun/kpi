$(document).ready(change_add_adress);


function change_add_adress()
{
	$('#adress').hide()
	$('.form-adress').hide()
	$('#change_add_adress').click(show_hidden);
	$('#close_pop_up').click(close_popup);
	
	function show_hidden(e){
		e.preventDefault();
		if ($('#adress').css('display') == 'none'){
			$('#adress').show('slow');
			$('body').css('background' ,  'rgba(230, 225, 225, 0.4)');
//			$('body').css('z-index' ,  '-1');
//			$('body'). = 'red';
		}
		else{
			$('#adress').hide('slow');
			$('body').css('background' ,  'rgba(255, 225, 225, 1)');
		}

	}
	function close_popup(e){
		e.preventDefault();
		$('#adress').hide('slow');
		$('body').css('background' ,  'rgb(255, 255, 255)');
	}
	
}