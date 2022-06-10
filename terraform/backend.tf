terraform {
  cloud {
    organization = "andrewimeson"
    workspaces {
      name = "file_management"
    }
  }

  required_version = ">= 1.2.0"
}
