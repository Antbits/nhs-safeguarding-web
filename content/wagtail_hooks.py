import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import BlockElementHandler
from wagtail.core import hooks


@hooks.register('register_rich_text_features')
def register_nhs_header_feature(features):
    feature_name = 'datestamp'
    type_ = 'datestamp'

    control = {
        'type': type_,
        'label': 'DT',
        'description': 'Datestamp',
        # Optionally, we can tell Draftail what element to use when displaying those blocks in the editor.
        'element': 'h4',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control, css={'all': ['css/datestamp.css']})
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'h4[class=datestamp]': BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: {'element': 'h4', 'props': {'class': 'datestamp'}}}},  
    })
@hooks.register('register_rich_text_features')
def register_nhs_header_feature(features):
    feature_name = 'anchorlist'
    type_ = 'anchorlist'

    control = {
        'type': type_,
        'label': 'AL',
        'description': 'Anchor list',
        # Optionally, we can tell Draftail what element to use when displaying those blocks in the editor.
        'element': 'li',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control, css={'all': ['css/anchorlist.css']})
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'li[class=anchorlist]': BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: {'element': 'li', 'props': {'class': 'anchorlist'}}}},  
    })
@hooks.register('register_rich_text_features')
def register_nhs_header_feature(features):
    feature_name = 'warninglist'
    type_ = 'warninglist'

    control = {
        'type': type_,
        'label': 'WL',
        'description': 'Warning list',
        # Optionally, we can tell Draftail what element to use when displaying those blocks in the editor.
        'element': 'li',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control, css={'all': ['css/warninglist.css']})
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'li[class=warninglist]': BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: {'element': 'li', 'props': {'class': 'warninglist'}}}},  
    })
@hooks.register('register_rich_text_features')
def register_nhs_header_feature(features):
    feature_name = 'blockquotelist'
    type_ = 'blockquotelist'

    control = {
        'type': type_,
        'label': 'WBL',
        'description': 'White Blockquote list',
        'element': 'li',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control, css={'all': ['css/blockquotelist.css']})
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'li[class=blockquotelist]': BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: {'element': 'li', 'props': {'class': 'blockquotelist'}}}},  
    })
@hooks.register('register_rich_text_features')
def register_nhs_header_feature(features):
    feature_name = 'greyblockquotelist'
    type_ = 'greyblockquotelist'

    control = {
        'type': type_,
        'label': 'GBL',
        'description': 'Grey Blockquote list',
        'element': 'li',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control, css={'all': ['css/greyblockquotelist.css']})
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'li[class=greyblockquotelist]': BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: {'element': 'li', 'props': {'class': 'greyblockquotelist'}}}},  
    })
@hooks.register('register_rich_text_features')
def register_nhs_header_feature(features):
    feature_name = 'scrolltop'
    type_ = 'scrolltop'

    control = {
        'type': type_,
        'label': 'ST',
        'description': 'Scroll to top',
        'element': 'span',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control, css={'all': ['css/scrolltop.css']})
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'span[class=scrolltop]': BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: {'element': 'span', 'props': {'class': 'scrolltop'}}}},  
    })
@hooks.register('register_rich_text_features')
def register_nhs_header_feature(features):
    feature_name = 'webonly'
    type_ = 'webonly'

    control = {
        'type': type_,
        'label': 'Web',
        'description': 'Display on web only',
        'element': 'div',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control, css={'all': ['css/webonly.css']})
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'div[class=webonly]': BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: {'element': 'div', 'props': {'class': 'webonly'}}}},  
    })
@hooks.register('register_rich_text_features')
def register_nhs_header_feature(features):
    feature_name = 'apponly'
    type_ = 'apponly'

    control = {
        'type': type_,
        'label': 'App',
        'description': 'Display on app only',
        'element': 'div',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control, css={'all': ['css/apponly.css']})
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'div[class=apponly]': BlockElementHandler(type_)},
        'to_database_format': {'block_map': {type_: {'element': 'div', 'props': {'class': 'apponly'}}}},  
    })
