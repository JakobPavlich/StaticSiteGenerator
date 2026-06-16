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

    # def __eq__(self, other: "HTMLnode") -> bool:
    #     if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
    #         return True
