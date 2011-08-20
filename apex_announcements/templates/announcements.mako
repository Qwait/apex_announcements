<%def name="show_announcements()">
	%for announcement in announcements:
		<h3>${announcement.title}</h3>
		<p>${announcement.content}</p>
	%endfor
</%def>