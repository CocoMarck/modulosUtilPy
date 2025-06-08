import utils


resource_obj = utils.ResourceLoader()

print( resource_obj.resource_dir )
print( resource_obj.get_image('sponge.png' ) ); print()

print( 
    resource_obj.get_data_tree(), "\n\n",
    resource_obj.get_config_tree(), "\n\n",
    resource_obj.get_image_tree(), "\n\n",
    resource_obj.get_icon_tree()
)