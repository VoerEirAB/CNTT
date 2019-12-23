[<< Back](../)

# 4. NFVI Test Case Traceability to Architecture Requirements
<p align="right"><img src="../figures/bogo_ifo.png" alt="scope" title="Scope" width="35%"/></p>

## Table of Contents
* [4.1 Introduction](#4.1)
* [4.2 Selection Criteria](#4.2)
* [4.3 Traceability Matrix](#4.3)
  * [4.3.1 Architecture and OpenStack Based](#4.3.1)
  * [4.3.2 Infrastructure](#4.3.2)
  * [4.3.3 VIM](#4.3.3)
  * [4.3.4 Interfaces & APIs](#4.3.4)
  * [4.3.5 Tenants](#4.3.5)
  * [4.3.6 LCM](#4.3.6)
  * [4.3.7 Assurance](#4.3.7)
  * [4.3.8 Security](#4.3.8)

<a name="4.1"></a>
## 4.1 Introduction

The scope of this chapter is to identify and list down test cases based on requirements defined in [Reference Architecture-1 (RA-1)](../../../ref_arch/openstack/README.md). This will serve as traceability between test cases and requirements.

Note that each requirement may have one or more test cases associated with it. 

**must**: Test Cases that are marked as must are considered mandatory and must pass succesfully.

**should**: Test Cases that are marked as should are expected to be fulfilled by NFVI but it is up to each service provider to accept an NFVI tagetting reference architecture that is not reflecting on any of those requirements. The same applies to should not.

**may**: Test cases that are marked as may are considered optional. The same applies to may not.

<a name="4.2"></a>
## 4.2 Selection Criteria
> Test cases below are selected based on available test cases in open-source tools like OPNFV FuncTest, YardStick, DoveTail etc.

<a name="4.3"></a>
## 4.3 Traceability Matrix

- Write content that explains this section defines the mapping, or traceability of RM/RA-1 requirements to test cases.

<a name="4.3.1"></a>
### 4.3.1 Architecture and OpenStack Requirements

- Describe and define in detail, RM/RA-1 OpenStack requirements.

<a name="4.3.2"></a>
### 4.3.2 Infrastructure


| Test case # | sub-category | Description | Requirement # |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `cert.test.inf.01` | Compute | Create a virtual machine with CPU pinning and 2 NUMA nodes. | `req.inf.com.05` |
| `cert.test.inf.02` | Compute | Create a virtual machine with CPU pinning enabled. | `req.inf.com.06` |
| `cert.test.inf.03` | Compute | Create 2 virtual machines and associate block storage to it. | `req.inf.stg.01	` |
| `cert.test.inf.04` | Compute | Create 2 virtual machines which are booted from block storage. | `req.inf.stg.01	` |

<a name="4.3.3"></a>
### 4.3.3 VIM


| Test case # | sub-category | Description | Requirement # |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `cert.test.vim.01` | VIM | Create a virtual machine with CPU pinning, HugePages and 2 NUMA nodes. | `req.vim.04` |
| `cert.test.vim.02` | VIM | Upload an image to image repository and download it back. | `req.vim.05` |
| `cert.test.vim.03` | VIM | Deploy a heat stack having 2 virtual machines with associated network. | `req.vim.06` |
| `cert.test.vim.04` | VIM | Create 2 tenants and then create virtual machine in each tenant. | `req.vim.07` |

<a name="4.3.4"></a>
### 4.3.4 Interfaces & APIs
This defines the test cases around the functionality that are exposed by OpenStack APIs. All the defined OpenStack 
service APIs in RA-1's [chapter 05](../../../ref_arch/openstack/chapters/chapter05.md) will be the scope here. 

Note: It will only target the functionality that are exposed by standard OpenStack APIs.  

#### 4.3.4.1 Identity - Keystone

It covers the test cases against identity management operations like user management, project management, 
multi-tenancy etc. The test cases are defined around the chosen service version and the enabled extensions for a 
normal user and admin user. See Keystone in [§5.2](../../../ref_arch/openstack/chapters/chapter05.md#5.2) for more
 details. 

| Test case # | sub-category | Description | Requirement # |
|----|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| `cert.api.identity.01` | API Discovery | Test that user is able to list api versions. |  |
| `cert.api.identity.01` | API Discovery | Test that user is able to list api media types. |  |
| `cert.api.identity.01` | API Discovery | Test that user is able to list api version statuses. |  |
| `cert.api.identity.01` | API Discovery | Test that user is able to see v3 as current in listed api versions. |  |
| `cert.api.identity.01` | Token | Test that user is able to create an authentication token. |  |
| `cert.api.identity.01` | Token | Test that user is able to validate an existing authentication token. |  |
| `cert.api.identity.01` | Application Credential | Test that user is able to list active application credentials. |  |
| `cert.api.identity.01` | Application Credential | Test that user is able to create an application credential with expiry time. |  |
| `cert.api.identity.01` | Application Credential | Test that user is able to delete an existing application credential. |  |
| `cert.api.identity.01` | Application Credential | Test that user is able to authenticate an existing application credential. |  |
| `cert.api.identity.01` | Application Credential | Test that admin user is able to create an application credential with roles. |  |
| `cert.api.identity.01` | Service | Test that user is able to list service catalog and it contains endpoint for each core service. | `req.int.api.01` |
| `cert.api.identity.01` | Service | Test that admin user is able to list service catalog and it contains endpoint for each all available services. | `req.int.api.01` |
| `cert.api.identity.01` | Service | Test that admin user is able to create a new endpoint. |  |
| `cert.api.identity.01` | Service | Test that admin user is able to update an existing endpoint. |  |
| `cert.api.identity.01` | Service | Test that admin user is able to delete an existing endpoint. |  |
| `cert.api.identity.01` | Service | Test that admin user is able to create a service. |  |
| `cert.api.identity.01` | Service | Test that admin user is able to update an existing service. |  |
| `cert.api.identity.01` | Service | Test that admin user is able to delete an existing service. |  |
| `cert.api.identity.01` | Security Compliance | Test that user account gets locked out for a particular duration after a defined number of incorrect attempts. |  |
| `cert.api.identity.01` | Domain | Test that user is able to check default domain. |  |
| `cert.api.identity.01` | Domain | Test that admin user is able to list existing domains. |  |
| `cert.api.identity.01` | Domain | Test that admin user is able to create a domain. |  |
| `cert.api.identity.01` | Domain | Test that admin user is able to enable/disable a domain. |  |
| `cert.api.identity.01` | Domain | Test that admin user is able to delete a domain. |  |
| `cert.api.identity.01` | Tenant | Test that user is able to list accessible tenants. |  |
| `cert.api.identity.01` | Tenant | Test that admin user is able to create a tenant. |  |
| `cert.api.identity.01` | Tenant | Test that admin user is able to update an existing tenant. |  |
| `cert.api.identity.01` | Tenant | Test that admin user is able to delete an existing tenant. |  |
| `cert.api.identity.01` | User | Test that user is able to update his/her own password. |  |
| `cert.api.identity.01` | User | Test that admin user is able to list existing users. |  |
| `cert.api.identity.01` | User | Test that admin user is able to create a user. |  |
| `cert.api.identity.01` | User | Test that admin user is able to update an existing user details. |  |
| `cert.api.identity.01` | User | Test that admin user is able to delete an existing user. |  |
| `cert.api.identity.01` | User | Test that admin user is able to add user to an existing tenant. |  |
| `cert.api.identity.01` | User | Test that admin user is able to remove user from an existing tenant. |  |
| `cert.api.identity.01` | User | Test that admin user is able to list all tenants associated with an existing user. |  |
| `cert.api.identity.01` | Region | Test that admin user is able to list regions. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to list roles. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to create a role. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to delete a role. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to list the roles of the user. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to assign a role to the user. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to revoke a role to the user. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to list the roles of the group. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to assign a role to the group. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to revoke a role to the group. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to create a domain role. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to delete a domain role. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to list the roles of the domain user. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to assign a role to the domain user. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to revoke a role to the domain user. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to list the roles of the domain group. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to assign a role to the domain group. |  |
| `cert.api.identity.01` | Role | Test that admin user is able to revoke a role to the domain group. |  |



#### 4.3.4.2 Image - Glance
It covers the test cases against image management operations. 


#### 4.3.4.3 Block Storage - Cinder
It covers the test cases against volume management operations.

#### 4.3.4.4 Object Storage - Swift
It covers the test cases against object management operations.


#### 4.3.4.5 Networking - Neutron
It covers the test cases against networking management operations.


#### 4.3.4.6 Compute - Nova
It covers the test cases against compute management operations.

#### 4.3.4.7 Orchestration - Heat
It covers the test cases against orchestration operations.

<a name="4.3.5"></a>
### 4.3.5 Tenants

<a name="4.3.6"></a>
### 4.3.6 LCM

<a name="4.3.7"></a>
### 4.3.7 Assurance

<a name="4.3.8"></a>
### 4.3.8 Security
