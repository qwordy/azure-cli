# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from azure.cli.core.util import sdk_no_wait


def billing_account_list(client,
                         expand=None):
    return client.list(expand=expand)


def billing_account_show(client,
                         account_name,
                         expand=None):
    return client.get(billing_account_name=account_name,
                      expand=expand)


def billing_account_update(client,
                           account_name,
                           display_name=None,
                           sold_to=None,
                           departments=None,
                           enrollment_accounts=None,
                           billing_profiles_value=None,
                           no_wait=False):
    parameters = {}
    parameters['display_name'] = display_name
    parameters['sold_to'] = sold_to
    parameters['departments'] = departments
    parameters['enrollment_accounts'] = enrollment_accounts
    parameters['billing_profiles'] = {}
    parameters['billing_profiles']['value'] = billing_profiles_value
    return sdk_no_wait(no_wait,
                       client.update,
                       billing_account_name=account_name,
                       parameters=parameters)


def billing_balance_show(client,
                         account_name,
                         profile_name):
    return client.get(billing_account_name=account_name,
                      billing_profile_name=profile_name)


def billing_profile_list(client,
                         account_name,
                         expand=None):
    return client.list_by_billing_account(billing_account_name=account_name,
                                          expand=expand)


def billing_profile_show(client,
                         account_name,
                         profile_name,
                         expand=None):
    return client.get(billing_account_name=account_name,
                      billing_profile_name=profile_name,
                      expand=expand)


def billing_profile_create(client,
                           account_name,
                           profile_name,
                           display_name=None,
                           po_number=None,
                           bill_to=None,
                           invoice_email_opt_in=None,
                           enabled_azure_plans=None,
                           invoice_sections_value=None,
                           no_wait=False):
    parameters = {}
    parameters['display_name'] = display_name
    parameters['po_number'] = po_number
    parameters['bill_to'] = bill_to
    parameters['invoice_email_opt_in'] = invoice_email_opt_in
    parameters['enabled_azure_plans'] = enabled_azure_plans
    parameters['invoice_sections'] = {}
    parameters['invoice_sections']['value'] = invoice_sections_value
    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       billing_account_name=account_name,
                       billing_profile_name=profile_name,
                       parameters=parameters)


def billing_profile_update(client,
                           account_name,
                           profile_name,
                           display_name=None,
                           po_number=None,
                           bill_to=None,
                           invoice_email_opt_in=None,
                           enabled_azure_plans=None,
                           invoice_sections_value=None,
                           no_wait=False):
    parameters = {}
    parameters['display_name'] = display_name
    parameters['po_number'] = po_number
    parameters['bill_to'] = bill_to
    parameters['invoice_email_opt_in'] = invoice_email_opt_in
    parameters['enabled_azure_plans'] = enabled_azure_plans
    parameters['invoice_sections'] = {}
    parameters['invoice_sections']['value'] = invoice_sections_value
    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       billing_account_name=account_name,
                       billing_profile_name=profile_name,
                       parameters=parameters)


def billing_customer_list(client,
                          account_name,
                          profile_name=None,
                          search=None,
                          filter_=None):
    if account_name is not None and profile_name is not None:
        return client.list_by_billing_profile(billing_account_name=account_name,
                                              billing_profile_name=profile_name,
                                              search=search,
                                              filter=filter_)
    return client.list_by_billing_account(billing_account_name=account_name,
                                          search=search,
                                          filter=filter_)


def billing_customer_show(client,
                          account_name,
                          customer_name,
                          expand=None):
    return client.get(billing_account_name=account_name,
                      customer_name=customer_name,
                      expand=expand)


def billing_invoice_section_list(client,
                                 account_name,
                                 profile_name):
    return client.list_by_billing_profile(billing_account_name=account_name,
                                          billing_profile_name=profile_name)


def billing_invoice_section_show(client,
                                 account_name,
                                 profile_name,
                                 invoice_section_name):
    return client.get(billing_account_name=account_name,
                      billing_profile_name=profile_name,
                      invoice_section_name=invoice_section_name)


def billing_invoice_section_create(client,
                                   account_name,
                                   profile_name,
                                   invoice_section_name,
                                   display_name=None,
                                   labels=None,
                                   no_wait=False):
    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       billing_account_name=account_name,
                       billing_profile_name=profile_name,
                       invoice_section_name=invoice_section_name,
                       display_name=display_name,
                       labels=labels)


def billing_invoice_section_update(client,
                                   account_name,
                                   profile_name,
                                   invoice_section_name,
                                   display_name=None,
                                   labels=None,
                                   no_wait=False):
    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       billing_account_name=account_name,
                       billing_profile_name=profile_name,
                       invoice_section_name=invoice_section_name,
                       display_name=display_name,
                       labels=labels)


# pylint: disable=no-else-return
def billing_subscription_list(client,
                              account_name,
                              profile_name=None,
                              invoice_section_name=None,
                              customer_name=None):
    if account_name is not None and profile_name is not None and invoice_section_name is not None:
        return client.list_by_invoice_section(billing_account_name=account_name,
                                              billing_profile_name=profile_name,
                                              invoice_section_name=invoice_section_name)
    elif account_name is not None and customer_name is not None:
        return client.list_by_customer(billing_account_name=account_name,
                                       customer_name=customer_name)
    elif account_name is not None and profile_name is not None:
        return client.list_by_billing_profile(billing_account_name=account_name,
                                              billing_profile_name=profile_name)
    return client.list_by_billing_account(billing_account_name=account_name)


def billing_subscription_show(client,
                              account_name):
    return client.get(billing_account_name=account_name)


def billing_subscription_update(client,
                                account_name,
                                subscription_billing_status=None,
                                cost_center=None,
                                sku_id=None):
    parameters = {}
    parameters['subscription_billing_status'] = subscription_billing_status
    parameters['cost_center'] = cost_center
    parameters['sku_id'] = sku_id
    return client.update(billing_account_name=account_name,
                         parameters=parameters)


def billing_subscription_move(client,
                              account_name,
                              destination_invoice_section_id,
                              no_wait=False):
    return sdk_no_wait(no_wait,
                       client.move,
                       billing_account_name=account_name,
                       destination_invoice_section_id=destination_invoice_section_id)


def billing_subscription_validate_move(client,
                                       account_name,
                                       destination_invoice_section_id):
    return client.validate_move(billing_account_name=account_name,
                                destination_invoice_section_id=destination_invoice_section_id)


def billing_product_list(client,
                         account_name,
                         profile_name=None,
                         invoice_section_name=None,
                         filter_=None,
                         customer_name=None):
    if account_name is not None and profile_name is not None and invoice_section_name is not None:
        return client.list_by_invoice_section(billing_account_name=account_name,
                                              billing_profile_name=profile_name,
                                              invoice_section_name=invoice_section_name,
                                              filter=filter_)
    elif account_name is not None and profile_name is not None:
        return client.list_by_billing_profile(billing_account_name=account_name,
                                              billing_profile_name=profile_name,
                                              filter=filter_)
    elif account_name is not None and customer_name is not None:
        return client.list_by_customer(billing_account_name=account_name,
                                       customer_name=customer_name)
    return client.list_by_billing_account(billing_account_name=account_name,
                                          filter=filter_)


def billing_product_show(client,
                         account_name,
                         product_name):
    return client.get(billing_account_name=account_name,
                      product_name=product_name)


def billing_product_update(client,
                           account_name,
                           product_name,
                           auto_renew=None,
                           status=None,
                           billing_frequency=None):
    parameters = {}
    parameters['auto_renew'] = auto_renew
    parameters['status'] = status
    parameters['billing_frequency'] = billing_frequency
    return client.update(billing_account_name=account_name,
                         product_name=product_name,
                         parameters=parameters)


def billing_product_move(client,
                         account_name,
                         product_name,
                         destination_invoice_section_id=None):
    return client.move(billing_account_name=account_name,
                       product_name=product_name,
                       destination_invoice_section_id=destination_invoice_section_id)


def billing_product_validate_move(client,
                                  account_name,
                                  product_name,
                                  destination_invoice_section_id=None):
    return client.validate_move(billing_account_name=account_name,
                                product_name=product_name,
                                destination_invoice_section_id=destination_invoice_section_id)


def billing_invoice_list(client,
                         period_start_date,
                         period_end_date,
                         account_name=None,
                         profile_name=None):
    if account_name is not None and profile_name is not None and period_start_date is not None and period_end_date is not None:
        return client.list_by_billing_profile(billing_account_name=account_name,
                                              billing_profile_name=profile_name,
                                              period_start_date=period_start_date,
                                              period_end_date=period_end_date)
    elif account_name is not None and period_start_date is not None and period_end_date is not None:
        return client.list_by_billing_account(billing_account_name=account_name,
                                              period_start_date=period_start_date,
                                              period_end_date=period_end_date)
    return client.list_by_billing_subscription(period_start_date=period_start_date,
                                               period_end_date=period_end_date)


def billing_invoice_show(client,
                         account_name,
                         name):
    return client.get(billing_account_name=account_name,
                      invoice_name=name)


def billing_transaction_list(client,
                             account_name,
                             invoice_name):
    return client.list_by_invoice(billing_account_name=account_name,
                                  invoice_name=invoice_name)


def billing_policy_update(client,
                          account_name,
                          profile_name,
                          marketplace_purchases=None,
                          reservation_purchases=None,
                          view_charges=None):
    parameters = {}
    parameters['marketplace_purchases'] = marketplace_purchases
    parameters['reservation_purchases'] = reservation_purchases
    parameters['view_charges'] = view_charges
    return client.update(billing_account_name=account_name,
                         billing_profile_name=profile_name,
                         parameters=parameters)


def billing_property_show(client):
    return client.get()


def billing_property_update(client,
                            cost_center=None):
    return client.update(cost_center=cost_center)
