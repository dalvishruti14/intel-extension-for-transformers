#  Copyright (c) 2023 Intel Corporation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

set(TARGET falcon)
add_library_w_warning(${TARGET} falcon.cpp falcon_utils.cpp ${MODEL_UTILS_SOURCE})
target_compile_features(${TARGET} PUBLIC cxx_std_11) # don't bump
set_target_properties(${TARGET} PROPERTIES POSITION_INDEPENDENT_CODE ON)
target_link_libraries(${TARGET} PUBLIC ne_layers ${LLAMA_EXTRA_LIBS} jblas::jblas)
