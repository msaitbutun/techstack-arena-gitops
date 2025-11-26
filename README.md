# GCP GKE Üzerinde Production-Ready Kubernetes Altyapısı (GitOps & Service Mesh)

![Terraform](https://img.shields.io/badge/Terraform-v1.5+-purple?style=for-the-badge&logo=terraform)
![Kubernetes](https://img.shields.io/badge/Kubernetes-GKE-blue?style=for-the-badge&logo=kubernetes)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-orange?style=for-the-badge&logo=argo)
![Istio](https://img.shields.io/badge/Service_Mesh-Istio-blueviolet?style=for-the-badge&logo=istio)
![GCP](https://img.shields.io/badge/Google_Cloud-Platform-green?style=for-the-badge&logo=google-cloud)
<img width="2833" height="1646" alt="image" src="https://github.com/user-attachments/assets/ecbb7334-7d31-47a7-9dc5-b59adbecf3b1" />


## 📖 Proje Özeti

Bu proje, **Google Cloud Platform (GCP)** üzerinde uçtan uca otomatize edilmiş, ölçeklenebilir ve üretime hazır (production-grade) bir Kubernetes altyapısını simüle etmek amacıyla geliştirilmiştir.

Geleneksel manuel sunucu yönetiminin aksine, bu projede modern **DevOps** ve **Cloud Native** prensipleri benimsenmiştir. Altyapı katmanı **Terraform** (IaC) ile kodlanmış, uygulama dağıtım süreçleri ise **ArgoCD** (GitOps) ile tam otomatik hale getirilmiştir. Ayrıca mikroservisler arası güvenli iletişim ve trafik yönetimi için **Istio Service Mesh** entegre edilmiştir.

### 🎯 Neden Bu Proje?
Bu çalışmanın temel amacı, sadece "çalışan" bir sistem değil, **"sürdürülebilir, izlenebilir ve kendini iyileştirebilen"** bir platform mimarisi kurmaktır.

* **Sıfır Manuel Müdahale:** Tüm altyapı kod ile yönetilir (Infrastructure as Code).
* **GitOps Akışı:** Git üzerindeki bir değişiklik, otomatik olarak canlı sisteme yansır.
* **Gelişmiş Trafik Yönetimi:** Canary deployment ve mTLS güvenliği Istio ile sağlanır.

---
*(Not: Altyapı Terraform ile, uygulama iş yükleri ArgoCD ile yönetilmektedir.)*

---

## 🛠️ Kullanılan Teknolojiler

| Bileşen | Teknoloji | Kullanım Amacı |
| :--- | :--- | :--- |
| **Bulut Sağlayıcı** | Google Cloud (GCP) | GKE Cluster, VPC Ağları ve IAM yönetimi. |
| **IaC** | Terraform | Altyapı kaynaklarının (Provisioning) kod ile kurulması. |
| **Orchestration** | Kubernetes (GKE) | Konteyner orkestrasyonu ve yönetimi. |
| **CD / GitOps** | ArgoCD | Sürekli dağıtım (Continuous Delivery) ve senkronizasyon. |
| **Service Mesh** | Istio | Trafik yönetimi, güvenlik (mTLS) ve gözlemlenebilirlik. |
| **İzleme (Monitoring)** | Prometheus & Grafana | Metrik toplama ve görselleştirme panoları. |

---

## 🚀 Kurulum ve Çalıştırma

Bu projeyi kendi GCP ortamınızda ayağa kaldırmak için aşağıdaki adımları izleyebilirsiniz.

### Ön Gereksinimler
* [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) kurulu ve yetkilendirilmiş olmalı.
* [Terraform](https://www.terraform.io/downloads) kurulu olmalı.
* [Kubectl](https://kubernetes.io/docs/tasks/tools/) kurulu olmalı.
* Faturalandırması aktif bir GCP Projesi.

### 1. Altyapıyı Kurma (Infrastructure)
Repoyu klonlayın ve Terraform ile GKE cluster'ını ayağa kaldırın.

```bash
git clone https://github.com/msaitbutun/techstack-arena-gitops.git
cd infrastructure
terraform init
terraform plan
terraform apply -auto-approve

