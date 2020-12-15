# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_ssh_public_key_create
from .example_steps import step_ssh_public_key_show
from .example_steps import step_ssh_public_key_generate_key_pair
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg):
    setup_scenario(test, rg)
    step_ssh_public_key_create(test, rg, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("publicKey", "{ssh-rsa public key}", case_sensitive=False),
        test.check("name", "{mySshPublicKey}", case_sensitive=False),
    ])
    step_ssh_public_key_show(test, rg, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("publicKey", "{ssh-rsa public key}", case_sensitive=False),
        test.check("name", "{mySshPublicKey}", case_sensitive=False),
    ])
    step_ssh_public_key_generate_key_pair(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class VmScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestvm_myResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_vm_Scenario(self, rg):

        self.kwargs.update({
            'mySshPublicKey': 'mySshPublicKeyName',
        })

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()

