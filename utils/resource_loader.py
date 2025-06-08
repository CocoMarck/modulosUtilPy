import pathlib


class ResourceLoader():
    def __init__(
        self, 
        base_dir=pathlib.Path().parent.absolute(),
        recource_dir_name='resources'
    ):
        super().__init__()
        
        self.base_dir = pathlib.Path().parent.absolute()

        self.data_dir = self.base_dir.joinpath( 'data' )

        self.config_dir = self.base_dir.joinpath( 'config' )

        self.resource_dir = self.base_dir.joinpath( 'resources' )
        self.images_dir = self.resource_dir.joinpath( 'images' )
        self.icons_dir = self.resource_dir.joinpath( 'icons' )


    def get_data( self, file: str ) -> pathlib.Path:
        '''
        Obtiene la ruta de las base de datos. Normalmente SQLite3
        '''
        return self.data_dir.joinpath( file )


    def get_config( self, file: str ) -> pathlib.Path:
        '''
        Obtiene la ruta de los archivos de configuracion. Pueden ser xml, json, .confg, .txt, .ini
        '''
        return self.config_dir.joinpath( file )
        

    def exists(self) -> bool:
        '''
        Determina si existe la ruta `resources`
        '''
        return self.resource_dir.is_dir()


    def get_image( self, image: str ) -> pathlib.Path:
        '''
        Obtiene la ruta donde estan las imagenes.
        '''
        return self.images_dir.joinpath( image )


    def get_icon( self, icon: str ) -> pathlib.Path:
        '''
        Obtiene la ruta donde estan las imagenes.
        '''
        return self.icons_dir.joinpath( icon )
    
    
    def get_recursive_tree(self, path: object | pathlib.Path ) -> dict:
        '''
        Obtener directorio y archivos de manera recursiva. Depende del parametro `path`
        '''
        dict_path = {
            "directory" : [],
            "file" : []
        }
        for dir_or_file in path.rglob('*'):
            if dir_or_file.is_dir():
                dict_path["directory"].append( dir_or_file )
            elif dir_or_file.is_file():
                dict_path["file"].append( dir_or_file )

        return dict_path
        
        

    def get_data_tree( self ) -> dict:
        '''
        En `data` obtener de manera recursiva los directorios y archivos.
        '''
        return self.get_recursive_tree( self.data_dir )
        
        
    def get_config_tree( self ) -> dict:
        '''
        En `config` obtener de manera recursiva los directorios y archivos.
        '''
        return self.get_recursive_tree( self.config_dir )
            

    def get_image_tree( self ) -> dict:
        '''
        En `resources/images` obtener de manera recursiva los directorios y archivos.
        '''
        return self.get_recursive_tree( self.images_dir )
        
        
    def get_icon_tree( self ) -> dict:
        '''
        En `resources/icon` obtener de manera recursiva los directorios y archivos.
        '''
        return self.get_recursive_tree( self.icons_dir )