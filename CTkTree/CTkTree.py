import customtkinter as ctk


class CTkTree(ctk.CTkFrame):
    def __init__(
            self,
            master: any,
            padx: int = 1,
            pady: int = 0,
            border_width: int = 0,
            font: ctk.CTkFont = None,
            corner_radius: int = 25,
            command=None,
            anchor: str = 'c',
            **kwargs) -> None:

        super().__init__(master, fg_color='transparent')
        self.master = master
        self.padx = padx
        self.pady = pady
        self.border_width = border_width
        self.font = font
        self.corner_radius = corner_radius
        self.command = command
        self.anchor = anchor

        self.tree = {'root':{}}
        self.frame = ctk.CTkFrame(self.master)
        self.nodes = 0
        self.parent_nodes = 1
        self.node_constant = '!!!NODE!!!'
        self.pack_constant = '!!!PACK!!!'

    def place(self, **kwargs) -> None:
        """
        Place the widget on the window specified by the master.
        """
        self.frame.place(**kwargs)

    def pack(self, **kwargs) -> None:
        """
        Pack the widget on the window specified by the master.
        """
        self.frame.pack(**kwargs, fill='both', expand=True)
        

    def add(self, path:str='', name:str='') -> None:
        """Add a node to the tree
        path : The path of the node seperated by '/'
            e.g.
                root/firstnode/secondnode
        name : The name of the new node
        """
        if name == '':
            name = str(len(self.tree))

        path_list = path.split('/')
        value = self.tree

        for key in path_list:
            value = value[key]

        
        pack_info = {'x':(len(path_list) - 1) * 10, 'y':self.nodes* 30}
        node = ctk.CTkButton(self.frame, text=name, command=lambda:self.node_click(path_list, name))

        if len(path_list) == 1:
            node.place(**pack_info)

        value[name] = {self.node_constant:node, self.pack_constant:pack_info}
        self.nodes += 1


    def node_click(self, path:list[str], name:str) -> None:
        value = self.tree
        for key in path:
            value = value[key]
        value = value[name]

        for key in value:
            if key not in (self.node_constant, self.pack_constant):
                node:ctk.CTkButton = value[key][self.node_constant]
                pack_info = value[key][self.pack_constant]
                if node.winfo_ismapped():
                    node.place_forget()
                else:
                    node.place(**pack_info)

if __name__ == "__main__":
    root = ctk.CTk()

    tree = CTkTree(root)
    tree.add('root', 'hello')
    tree.add('root/hello', 'hi')
    tree.add('root/hello/hi', 'new')
    tree.add('root', 'goodbye')
    tree.add('root/goodbye', 'bye')

    tree.pack()

    root.mainloop()




