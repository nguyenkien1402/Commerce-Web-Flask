// Copyright 2018 Google LLC.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Script for configuring FilePond, a file upload library.
// See https://github.com/pqina/filepond for more information.

FilePond.setOptions({
  instantUpload: false,
  allowMultiple: false,
  allowReplace: false,
  allowImagePreview: true,
  server: {
    process: 'https://us-central1-commerce-store-serverless.cloudfunctions.net/upload-image',
    fetch: null,
    revert: null,
    restore: null,
    load: null
  }
});
FilePond.registerPlugin(
  FilePondPluginImagePreview
);
const pond = FilePond.create(document.querySelector('input[type="file"]'));
pond.on('processfile', (error, file) => {
  if (error === null) {
    let id = file.serverId;
    let uploadFileIdInputNode = document.querySelector(`#image`);
    uploadFileIdInputNode.value = id;
  }
})