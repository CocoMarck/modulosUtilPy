import utils
from core.util_system import *
from core.util_text import *
from core.display_number import *
from views.interface import show_print

# ResourceLoader
resource_obj = utils.ResourceLoader()
'''
print( resource_obj.resources_dir )
print( resource_obj.get_image('sponge.png' ) ); print()

print( 
    resource_obj.get_data_tree(), "\n\n",
    resource_obj.get_config_tree(), "\n\n",
    resource_obj.get_image_tree(), "\n\n",
    resource_obj.get_icon_tree()
)
'''

# Texto a guadar
log_file = resource_obj.get_log( "log.md" )
log_text = ""



clean_screen()

# util_text | read_text
log_text += show_print.title( "util_text.py | read_text()" )

readme = resource_obj.get_base_path("README.md")
log_text += show_print.code_box(
    read_text( readme, "ModeList" ), "python"
)
log_text += show_print.code_box(
    read_text( readme, "ModeDict" ), "python"
)
log_text += show_print.code_box(
    read_text( readme, "ModeTextOnly" )
)
log_text += show_print.code_box(
    read_text( readme, "ModeText" )
)

log_text += show_print.separator()


# util_text | Comentarios
show_print.title( "util_text.py | Comentarios" )

run_command_file = resource_obj.get_base_path("config/runCommand.txt")
log_text += show_print.code_box( 
    read_text( run_command_file, "ModeText" ), "bash"
)

log_text += show_print.code_box(
    ignore_comment(
        read_text( run_command_file, "ModeText" ), '#'
    )
)

log_text += show_print.code_box(
    only_the_comment(
        read_text( run_command_file, "ModeText" ), '#'
    )
)
log_text += show_print.separator()


# util_text | separe text
log_text += show_print.title( "util_text.py | separe_text()" )
log_text += show_print.code_box( 
    separe_text("variable=40"), "python"
)


# util_text | only_one_char
log_text += show_print.title( "util_text.py | only_one_char()" )
log_text += show_print.code_box(
    only_one_char( "-", "Hace    rato   yo   sali del fin  de mi    redimir")
)


# util_text | pass_text_filter/ignore_text_filter
log_text += show_print.title( "util_text.py | pass_text_filter/ignore_text_filter" )
log_text += show_print.print_and_return(  
    text = (
        f'{pass_text_filter( "texto numero 2126232@2321", "1234567890 " )}\n'
        f'{ignore_text_filter( "texto numero 2126232@2321", "1234567890 " )}\n'
    )
)


# util_text | abc_list
log_text += show_print.title( "util_text.py | abc_list" )

log_text += show_print.code_box(
    abc_list( ["q", "d", "k", "n", "z", "w", "t", "o", "a", "e", "s", "m"] ), "python"
)

# util_text | not_repeat_item
log_text += show_print.title( "util_text.py | not_repeat_item()" )
log_text += show_print.code_box(
    not_repeat_item( ["a", "a", "a", "b", "a", "a", "a", "a"] ), "python"
)





log_text += show_print.title( "show_print.py | command_box()/title()/separator()/input_continue()" )
log_text += show_print.command_box( "whereis firefox" )

show_print.input_continue()

log_text += show_print.separator()




# util_system | get_system
log_text += show_print.title( 
    'util_system.py | get_system() view_echo() run_command() get_display_resolution()' 
)
log_text += show_print.print_and_return( f"El sistema operativo es: {get_system()}" )

# util_system | show_file
log_text += show_print.code_box( show_file() )

# util_system | view_echo
log_text += show_print.print_and_return( f'El directorio home: {view_echo("$HOME")}' )

# util_system | get_display_resolution
log_text += show_print.print_and_return( f"Resolución de pantalla: {get_display_resolution()}" )

# util_system | command_output
log_text += show_print.code_box( command_output("ls"), "bash" )
log_text += show_print.code_box( command_output("cacahuete"), "bash" )

log_text += show_print.separator()

# util_system | run_command
print( "~~~" )
run_command( "neofetch", False ); print()
run_command( "neofetch", True, "Preciona enter para continuar" ); print()
print( "~~~" )

show_print.separator()




# display_number | get_display_number
show_print.title( "display_number.py | get_display_number()" )
log_text += show_print.print_and_return(
    f"El 50% del ancho de resolución de pantalla: {get_display_number(multipler=0.5, based='width')}" 
) + show_print.print_and_return()

log_text += show_print.print_and_return(
    f"El ancho de pantalla entre tres: {get_display_number(divisor=3, based='width')}"
) + show_print.print_and_return()





# Escribir log
with open( log_file, 'w' ) as log:
    log.write( log_text )