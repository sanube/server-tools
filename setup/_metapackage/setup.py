import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo9-addons-oca-server-tools",
    description="Meta package for oca-server-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo9-addon-admin_technical_features',
        'odoo9-addon-attachment_base_synchronize',
        'odoo9-addon-auditlog',
        'odoo9-addon-auth_from_http_remote_user',
        'odoo9-addon-auth_session_timeout',
        'odoo9-addon-auth_signup_verify_email',
        'odoo9-addon-auth_supplier',
        'odoo9-addon-auth_totp',
        'odoo9-addon-auth_totp_password_security',
        'odoo9-addon-auto_backup',
        'odoo9-addon-base_cron_exclusion',
        'odoo9-addon-base_custom_info',
        'odoo9-addon-base_export_manager',
        'odoo9-addon-base_external_dbsource',
        'odoo9-addon-base_fontawesome',
        'odoo9-addon-base_import_match',
        'odoo9-addon-base_kanban_stage',
        'odoo9-addon-base_manifest_extension',
        'odoo9-addon-base_multi_image',
        'odoo9-addon-base_name_search_improved',
        'odoo9-addon-base_optional_quick_create',
        'odoo9-addon-base_report_auto_create_qweb',
        'odoo9-addon-base_search_fuzzy',
        'odoo9-addon-base_suspend_security',
        'odoo9-addon-base_technical_features',
        'odoo9-addon-base_tier_validation',
        'odoo9-addon-base_user_gravatar',
        'odoo9-addon-base_user_role',
        'odoo9-addon-base_view_inheritance_extension',
        'odoo9-addon-configuration_helper',
        'odoo9-addon-database_cleanup',
        'odoo9-addon-date_range',
        'odoo9-addon-datetime_formatter',
        'odoo9-addon-dbfilter_from_header',
        'odoo9-addon-dead_mans_switch_client',
        'odoo9-addon-disable_odoo_online',
        'odoo9-addon-external_file_location',
        'odoo9-addon-fetchmail_bydate',
        'odoo9-addon-fetchmail_notify_error_to_sender',
        'odoo9-addon-html_image_url_extractor',
        'odoo9-addon-html_text',
        'odoo9-addon-keychain',
        'odoo9-addon-kpi',
        'odoo9-addon-letsencrypt',
        'odoo9-addon-mail_cleanup',
        'odoo9-addon-mail_environment',
        'odoo9-addon-mail_log_messages_to_process',
        'odoo9-addon-mass_editing',
        'odoo9-addon-menu_technical_info',
        'odoo9-addon-module_auto_update',
        'odoo9-addon-module_prototyper',
        'odoo9-addon-oauth_provider',
        'odoo9-addon-oauth_provider_jwt',
        'odoo9-addon-password_security',
        'odoo9-addon-res_config_settings_enterprise_remove',
        'odoo9-addon-scheduler_error_mailer',
        'odoo9-addon-sequence_check_digit',
        'odoo9-addon-server_environment',
        'odoo9-addon-server_environment_files_sample',
        'odoo9-addon-server_environment_ir_config_parameter',
        'odoo9-addon-sql_export',
        'odoo9-addon-sql_request_abstract',
        'odoo9-addon-subscription_action',
        'odoo9-addon-test_configuration_helper',
        'odoo9-addon-users_ldap_mail',
        'odoo9-addon-users_ldap_populate',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
