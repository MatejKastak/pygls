############################################################################
# Original work Copyright 2017 Palantir Technologies, Inc.                 #
# Original work licensed under the MIT License.                            #
# See ThirdPartyNotices.txt in the project root for license information.   #
# All modifications Copyright (c) Open Law Library. All rights reserved.   #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License")           #
# you may not use this file except in compliance with the License.         #
# You may obtain a copy of the License at                                  #
#                                                                          #
#     http: // www.apache.org/licenses/LICENSE-2.0                         #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,        #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
# See the License for the specific language governing permissions and      #
# limitations under the License.                                           #
############################################################################
"""This module contains Language Server Protocol types
https://microsoft.github.io/language-server-protocol/specification

-- Language Features - Implementation --

Class attributes are named with camel case notation because client is expecting
that.
"""
from typing import Optional

from pygls.lsp.types.basic_structures import (Model, PartialResultParams,
                                              StaticRegistrationOptions,
                                              TextDocumentPositionParams,
                                              TextDocumentRegistrationOptions,
                                              WorkDoneProgressOptions, WorkDoneProgressParams)


class ImplementationClientCapabilities(Model):
    dynamic_registration: Optional[bool]
    link_support: Optional[bool]


class ImplementationOptions(WorkDoneProgressOptions):
    pass


class ImplementationRegistrationOptions(ImplementationOptions,
                                        TextDocumentRegistrationOptions,
                                        StaticRegistrationOptions):
    pass


class ImplementationParams(TextDocumentPositionParams, WorkDoneProgressParams, PartialResultParams):
    pass
