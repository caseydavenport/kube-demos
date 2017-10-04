# PCI Compliance using Kubernetes Network Policy

This demo shows one way to implement a PCI compliant firewall using Kubernetes
Network Policy.

In this demo, we use Namespace's as a mechanism for ensuring that only a subset of
desired pods have access to a redis database which contains sensitive customer
information.
