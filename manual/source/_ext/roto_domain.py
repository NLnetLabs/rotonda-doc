from sphinx.directives import ObjectDescription
from sphinx.domains import Domain
from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.application import Sphinx

class RotoFunctionLike(ObjectDescription):
    """Generic Roto function-like object that we don't register into the domain"""
    
    class_name = ""

    def handle_signature(self, sig, signode):
        """Append the nodes for the sig into the signode"""
 
        if '.' in sig:
            receiver, _, sig = sig.partition('.')
        else:
            receiver = None

        name, _, rest = sig.partition('(')
        params, _, ret = rest.partition(')')
        
        sig_param_list = addnodes.desc_parameterlist()
        for param in params.split(','):
            if not param:
                continue
            param_name, _, ty = param.partition(': ') 
            sig_param = addnodes.desc_parameter()
            sig_param += addnodes.desc_name(text=param_name)
            sig_param += addnodes.desc_sig_punctuation(text=':')
            sig_param += addnodes.desc_sig_space(text=' ')
            sig_param += addnodes.desc_type(text=ty)
            sig_param_list += sig_param

        signode += addnodes.desc_annotation(text=self.class_name)

        if receiver:
            signode += addnodes.desc_addname(text=f"{receiver}")
            signode += addnodes.desc_sig_punctuation(text='.')
    
        signode += addnodes.desc_name(text=name)
        signode += addnodes.desc_sig_punctuation('(')
        signode += sig_param_list
        signode += addnodes.desc_sig_punctuation(')')
        
        ret = ret.strip().removeprefix('->').strip()
        sig_ret = addnodes.desc_returns()
        sig_ret += addnodes.desc_type(text=ret)

        signode += sig_ret

        signode['path'] = sig
        signode['fullname'] = fullname = f"{receiver}.{name}"
        return fullname

    def needs_arglist(self):
        return False

class RotoType(ObjectDescription):
    def handle_signature(self, sig: str, signode):
        signode += addnodes.desc_annotation(text="type")
        signode += addnodes.desc_name(text=sig)
        return sig

class RotoFunction(RotoFunctionLike):
    class_name = "function"

class RotoStaticMethod(RotoFunctionLike):
    class_name = "static method"

class RotoMethod(RotoFunctionLike):
    class_name = "method"

class RecipeDomain(Domain):
    name = 'roto'
    label = 'Roto'
    roles = {}

    directives = {
        'function': RotoFunction,
        'method': RotoMethod,
        'static_method': RotoStaticMethod,
        'type': RotoType,
    }

    indices = []

    initial_data = {
        'functions': {},
        'methods': {},
        'static_methods': {},
        'types': {},
    }

    data_version = 0


    def get_full_qualified_name(self, node):
        return f'roto.{node.arguments[0]}'


def setup(app: Sphinx):
    app.add_domain(RecipeDomain)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
