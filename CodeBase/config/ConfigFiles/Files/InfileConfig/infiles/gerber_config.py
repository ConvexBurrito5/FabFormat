from CodeBase.config.ConfigFiles.Files.file_parent import FileParent


class GerberFile(FileParent):
    def __init__(self, filepath, layer_type, file_name, active_layers):
        file_type = "gerber"
        super().__init__(filepath, layer_type, file_name, file_type, active_layers)
        pass