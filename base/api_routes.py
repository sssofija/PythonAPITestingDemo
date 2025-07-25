api_routes = {
    'categories': {
        'get_categories': '/api/v1/categories/all/',
        'post_categories': '/api/v1/categories/',
        'put_categories_id': '/api/v1/categories/{}/',
        'patch_categories_id': '/api/v1/categories/{}/',
        'delete_categories_id': '/api/v1/categories/{}/',
    },
    'countries': {
        'get_countries': '/api/v1/countries/',
    },
    'currency': {
        'get_currency': '/api/v1/currency/'
    },
    'operations': {
        'get_operations': '/api/v1/operations/all/',
        'post_operations': '/api/v1/operations/',
        'get_operations_id': '/api/v1/operations/{}/',
        'put_operations_id': '/api/v1/operations/{}/',
        'patch_operations_id': '/api/v1/operations/{}/',
        'delete_operations_id': '/api/v1/operations/{}/',
    },
    'password': {
        'get_password_reset_confirm': '/api/v1/password/reset/confirm/',
    },
    'profile': {
        'get_profile': '/api/v1/profile/',
        'patch_profile': '/api/v1/profile/',
    },
    'targets': {
        'get_targets': '/api/v1/targets/',
        'post_targets': '/api/v1/targets/',
        'put_targets_id': '/api/v1/targets/{}/',
        'patch_targets_id': '/api/v1/targets/{}/',
        'delete_targets_id': '/api/v1/targets/{}/',
        'delete_targets_id_return_money': '/api/v1/targets/{id}/return_money/',
        'get_targets_by_id': '/api/v1/targets/{}/'
    }
}
