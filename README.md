# [File Management API](https://github.com/andrewimeson/file_management)

An example API service that retrieves a file.

## Developing

1. Clone the repository

    ```sh
    git clone git@github.com:andrewimeson/file_management.git
    cd file_management
    ```

> **Note**
> Optional pre-commit hooks are available to take care of autoformatting,
> With pre-commit installed, run `pre-commit install` to install the git hooks

## Functional Requirements

- [ ] Expose an HTTP endpoint at the URL `/manage_file` that accepts a JSON
      payload.
- [ ] If the payload includes `"action": "download"`, fetch the file at
      `https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt`
      and store it locally.
- [ ] If the payload includes `"action": "read"`, return the contents of the
      file.
- [ ] Ensure your service returns proper status codes for all requests, and
      otherwise behaves appropriately for a standard HTTP service.
