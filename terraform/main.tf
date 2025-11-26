resource "google_container_cluster" "primary"{
    name = "my-gitops-cluster"
    location = "europe-west1-b"
    remove_default_node_pool = true
    initial_node_count = 1 
}

resource "google_container_node_pool" "primary_nodes"{
    name = "sait-node-pool"
    location = "europe-west1-b"
    cluster = google_container_cluster.primary.name
    node_count = 4
    node_config {
    disk_size_gb = 20
    preemptible  = true # Spot instance benzeri (Çok daha ucuzdur, demo için ideal)
    machine_type = "e2-medium" # 2 vCPU, 4GB RAM (Rahat rahat yeter)

    # Google servislerine erişim yetkileri
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
   
}