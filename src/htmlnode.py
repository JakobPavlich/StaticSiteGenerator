class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        html_string = ""
        if not self.props:
            return html_string
        for prop, value in self.props.items():
            html_string += f' {prop}="{value}"'

        return html_string

    def __repr__(self):
        return f"HTMLnode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.props == other.props
            and self.children == other.children
        )


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Needs to have a value.")
        if self.tag is None:
            return self.value
        else:
            if self.tag == "img":
                return f'<img{self.props_to_html()}>'
            # elif self.tag == "code":
            #     return f'<pre><{self.tag}{self.props_to_html()}>{self.value}</{self.tag}></pre>'
            else:
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.props == other.props
        )


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("A tag is neccessary")
        if not self.children:
            raise ValueError("A parent node has to have children nodes")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        # children_html = "".join(child.to_html() for child in self.children)

        # if self.props is not None:
        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'
        # else:
        #     return f'<{self.tag}>{children_html}</{self.tag}>'

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

    def __eq__(self, other):
        if not isinstance(other, ParentNode):
            return False
        return (
            self.tag == other.tag
            and self.children == other.children
            and self.props == other.props
        )
