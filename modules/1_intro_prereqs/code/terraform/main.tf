terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
  # configuration options
  credentials = "./keys/my-creds.json"
  project = "enhanced-bonito-411221"
  region  = "europe-north1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "enhanced-bonito-411221-terra-bucket"
  location      = "EU"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}