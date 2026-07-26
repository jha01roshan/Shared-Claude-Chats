# Adding Kerberos Authentication to Hadoop Cluster on EC2

- Source: https://claude.ai/share/9b229911-00ea-4c43-8ee5-04fd8e372794
- Author: Zbigniew
- Created: 2025-03-19
- Messages: 8

---

## Human

On the `/Users/zbigniewtomanek/work/hadoop-cluster-on-ec2/README.md` you can find my project which exposes hadoop cluster. Now the goal is to add kerberos authentication to it. Examine current configurations and then prepare a plan how kerberos auth can be added to this project

---

## Assistant

I'll help you add Kerberos authentication to your Hadoop cluster on EC2. Let's first examine the current configuration in your project by looking at the README and other relevant files.
```
This block is not supported on your current device yet.
```



Let's check the docker-compose.yml file to better understand the cluster setup:
```
This block is not supported on your current device yet.
```



Let's also check the Hadoop configuration files:
```
This block is not supported on your current device yet.
```




```
This block is not supported on your current device yet.
```





Let's also check the environment files:
```
This block is not supported on your current device yet.
```






```
This block is not supported on your current device yet.
```



Based on the examination of your project's configuration files, I can see you have a multi-container Hadoop cluster running on EC2 with Spark and Hive, but no Kerberos authentication currently configured. Let me create a comprehensive plan to add Kerberos authentication to your Hadoop cluster.

# Plan to Add Kerberos Authentication to Hadoop Cluster on EC2

## 1. Overview of Kerberos Authentication for Hadoop

Kerberos is an authentication protocol that uses tickets to allow nodes communicating over a non-secure network to prove their identity to one another securely. In a Hadoop environment, Kerberos authentication ensures that:

- Users and services authenticate themselves before accessing cluster resources
- Services can authenticate each other (service-to-service authentication)
- Data transfer between clients and services can be secured

## 2. Prerequisites

1. A KDC (Key Distribution Center) server to manage Kerberos authentication
2. MIT Kerberos client libraries installed on all nodes
3. Proper DNS resolution for all hosts in the cluster
4. Time synchronization across all nodes (crucial for Kerberos)

## 3. Implementation Plan

### Step 1: Set up a KDC (Key Distribution Center)

You have two options:
- Set up a dedicated KDC server
- Add KDC service to an existing server in your cluster

```bash
# Install Kerberos server packages
apt-get update
apt-get install -y krb5-kdc krb5-admin-server

# Configure KDC
cat > /etc/krb5.conf << EOF
[libdefaults]
    default_realm = HADOOP.DEMO-DATAWALK.COM
    dns_lookup_realm = false
    dns_lookup_kdc = false
    ticket_lifetime = 24h
    renew_lifetime = 7d
    forwardable = true

[realms]
    HADOOP.DEMO-DATAWALK.COM = {
        kdc = kdc.hadoop.demo-datawalk.com
        admin_server = kdc.hadoop.demo-datawalk.com
    }

[domain_realm]
    .hadoop.demo-datawalk.com = HADOOP.DEMO-DATAWALK.COM
    hadoop.demo-datawalk.com = HADOOP.DEMO-DATAWALK.COM
EOF

# Create KDC database
krb5_newrealm

# Configure admin access
kadmin.local -q "addprinc admin/admin"
```

### Step 2: Create Kerberos Principals for Hadoop Services

Create principals for each Hadoop service:

```bash
# Connect to kadmin
kadmin.local

# Create service principals for HDFS
addprinc -randkey nn/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM
addprinc -randkey dn/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM
addprinc -randkey HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM

# Create service principals for YARN
addprinc -randkey rm/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM
addprinc -randkey nm/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM
addprinc -randkey jhs/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM

# Create service principals for Hive
addprinc -randkey hive/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM

# Create service principals for Spark
addprinc -randkey spark/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM

# Export keytabs for each service
ktadd -k /etc/security/keytabs/nn.service.keytab nn/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM
ktadd -k /etc/security/keytabs/dn.service.keytab dn/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM
ktadd -k /etc/security/keytabs/rm.service.keytab rm/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM
ktadd -k /etc/security/keytabs/nm.service.keytab nm/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM
ktadd -k /etc/security/keytabs/jhs.service.keytab jhs/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM
ktadd -k /etc/security/keytabs/hive.service.keytab hive/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM
ktadd -k /etc/security/keytabs/spark.service.keytab spark/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM

# Create user principals (for admins and regular users)
addprinc hadoop-admin
addprinc -randkey hadoop-admin
ktadd -k /etc/security/keytabs/hadoop-admin.keytab hadoop-admin@HADOOP.DEMO-DATAWALK.COM
```

### Step 3: Modify Hadoop Configuration Files to Enable Kerberos

#### 1. Create a new directory for Kerberos configs:

```bash
mkdir -p /Users/zbigniewtomanek/work/hadoop-cluster-on-ec2/kerberos-config
```

#### 2. Modify core-site.xml:

```xml
<property>
  <n>hadoop.security.authentication</n>
  <value>kerberos</value>
</property>
<property>
  <n>hadoop.security.authorization</n>
  <value>true</value>
</property>
<property>
  <n>hadoop.rpc.protection</n>
  <value>privacy</value>
</property>
<property>
  <n>hadoop.security.auth_to_local</n>
  <value>
    RULE:[2:$1@$0](nn@HADOOP.DEMO-DATAWALK.COM)s/.*/hdfs/
    RULE:[2:$1@$0](dn@HADOOP.DEMO-DATAWALK.COM)s/.*/hdfs/
    RULE:[2:$1@$0](rm@HADOOP.DEMO-DATAWALK.COM)s/.*/yarn/
    RULE:[2:$1@$0](nm@HADOOP.DEMO-DATAWALK.COM)s/.*/yarn/
    RULE:[2:$1@$0](jhs@HADOOP.DEMO-DATAWALK.COM)s/.*/mapred/
    RULE:[2:$1@$0](hive@HADOOP.DEMO-DATAWALK.COM)s/.*/hive/
    RULE:[2:$1@$0](spark@HADOOP.DEMO-DATAWALK.COM)s/.*/spark/
    DEFAULT
  </value>
</property>
```

#### 3. Modify hdfs-site.xml:

```xml
<property>
  <n>dfs.block.access.token.enable</n>
  <value>true</value>
</property>
<property>
  <n>dfs.namenode.keytab.file</n>
  <value>/etc/security/keytabs/nn.service.keytab</value>
</property>
<property>
  <n>dfs.namenode.kerberos.principal</n>
  <value>nn/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM</value>
</property>
<property>
  <n>dfs.namenode.kerberos.internal.spnego.principal</n>
  <value>HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM</value>
</property>
<property>
  <n>dfs.datanode.keytab.file</n>
  <value>/etc/security/keytabs/dn.service.keytab</value>
</property>
<property>
  <n>dfs.datanode.kerberos.principal</n>
  <value>dn/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM</value>
</property>
<property>
  <n>dfs.web.authentication.kerberos.principal</n>
  <value>HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM</value>
</property>
<property>
  <n>dfs.web.authentication.kerberos.keytab</n>
  <value>/etc/security/keytabs/nn.service.keytab</value>
</property>
<property>
  <n>dfs.data.transfer.protection</n>
  <value>privacy</value>
</property>
```

#### 4. Modify yarn-site.xml:

```xml
<property>
  <n>yarn.resourcemanager.keytab</n>
  <value>/etc/security/keytabs/rm.service.keytab</value>
</property>
<property>
  <n>yarn.resourcemanager.principal</n>
  <value>rm/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM</value>
</property>
<property>
  <n>yarn.nodemanager.keytab</n>
  <value>/etc/security/keytabs/nm.service.keytab</value>
</property>
<property>
  <n>yarn.nodemanager.principal</n>
  <value>nm/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM</value>
</property>
<property>
  <n>yarn.timeline-service.keytab</n>
  <value>/etc/security/keytabs/jhs.service.keytab</value>
</property>
<property>
  <n>yarn.timeline-service.principal</n>
  <value>jhs/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM</value>
</property>
<property>
  <n>yarn.timeline-service.http-authentication.type</n>
  <value>kerberos</value>
</property>
<property>
  <n>yarn.timeline-service.http-authentication.kerberos.principal</n>
  <value>HTTP/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM</value>
</property>
<property>
  <n>yarn.timeline-service.http-authentication.kerberos.keytab</n>
  <value>/etc/security/keytabs/jhs.service.keytab</value>
</property>
```

#### 5. Modify mapred-site.xml:

```xml
<property>
  <n>mapreduce.jobhistory.keytab</n>
  <value>/etc/security/keytabs/jhs.service.keytab</value>
</property>
<property>
  <n>mapreduce.jobhistory.principal</n>
  <value>jhs/hadoop.demo-datawalk.com@HADOOP.DEMO-DATAWALK.COM</value>
</property>
```

#### 6. Add krb5.conf for all containers:

```
[libdefaults]
    default_realm = HADOOP.DEMO-DATAWALK.COM
    dns_lookup_realm = false
    dns_lookup_kdc = false
    ticket_lifetime = 24h
    renew_lifetime = 7d
    forwardable = true

[realms]
    HADOOP.DEMO-DATAWALK.COM = {
        kdc = kdc.hadoop.demo-datawalk.com
        admin_server = kdc.hadoop.demo-datawalk.com
    }

[domain_realm]
    .hadoop.demo-datawalk.com = HADOOP.DEMO-DATAWALK.COM
    hadoop.demo-datawalk.com = HADOOP.DEMO-DATAWALK.COM
```

### Step 4: Update Docker Compose File

Update your docker-compose.yml to include the Kerberos configurations and mount the keytab files:

```yaml
version: "3"

services:
  kdc:
    image: sequenceiq/kerberos:latest
    container_name: kdc
    hostname: kdc.hadoop.demo-datawalk.com
    volumes:
      - ./kerberos-config/:/etc/krb5kdc/
      - kerberos_data:/var/kerberos
    environment:
      - KRB5_REALM=HADOOP.DEMO-DATAWALK.COM
      - DOMAIN_REALM=hadoop.demo-datawalk.com
    restart: always
    network_mode: "host"
    
  namenode:
    image: bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8
    container_name: namenode
    restart: always
    volumes:
      - hadoop_namenode:/hadoop/dfs/name
      - ./hadoop-config/core-site.xml:/etc/hadoop/core-site.xml
      - ./hadoop-config/hdfs-site.xml:/etc/hadoop/hdfs-site.xml
      - ./kerberos-config/krb5.conf:/etc/krb5.conf
      - ./kerberos-config/keytabs:/etc/security/keytabs
    environment:
      - CLUSTER_NAME=test
      - CORE_CONF_fs_defaultFS=hdfs://hadoop.demo-datawalk.com:9010
      - HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check=false
      - CORE_CONF_hadoop_security_authentication=kerberos
      - CORE_CONF_hadoop_security_authorization=true
      - CORE_CONF_hadoop_rpc_protection=privacy
    env_file:
      - ./hadoop.env
    hostname: hadoop.demo-datawalk.com
    network_mode: "host"
    depends_on:
      - kdc

  # ... (similar updates for other services)
```

For each service in the docker-compose.yml, add:
- Volume mounts for krb5.conf and keytabs
- Kerberos environment variables
- Dependency on the KDC service

### Step 5: Create Installation and Setup Scripts

1. Create a script to generate and distribute keytabs:

```bash
#!/bin/bash
# generate-keytabs.sh

mkdir -p kerberos-config/keytabs

# Run commands inside KDC container to create principals
docker exec -it kdc bash -c "
kadmin.local -q 'addprinc -randkey nn/hadoop.demo-datawalk.com'
kadmin.local -q 'addprinc -randkey dn/hadoop.demo-datawalk.com'
kadmin.local -q 'addprinc -randkey HTTP/hadoop.demo-datawalk.com'
kadmin.local -q 'addprinc -randkey rm/hadoop.demo-datawalk.com'
kadmin.local -q 'addprinc -randkey nm/hadoop.demo-datawalk.com'
kadmin.local -q 'addprinc -randkey jhs/hadoop.demo-datawalk.com'
kadmin.local -q 'addprinc -randkey hive/hadoop.demo-datawalk.com'
kadmin.local -q 'addprinc -randkey spark/hadoop.demo-datawalk.com'

# Create keytabs
kadmin.local -q 'ktadd -k /tmp/nn.service.keytab nn/hadoop.demo-datawalk.com HTTP/hadoop.demo-datawalk.com'
kadmin.local -q 'ktadd -k /tmp/dn.service.keytab dn/hadoop.demo-datawalk.com HTTP/hadoop.demo-datawalk.com'
kadmin.local -q 'ktadd -k /tmp/rm.service.keytab rm/hadoop.demo-datawalk.com HTTP/hadoop.demo-datawalk.com'
kadmin.local -q 'ktadd -k /tmp/nm.service.keytab nm/hadoop.demo-datawalk.com HTTP/hadoop.demo-datawalk.com'
kadmin.local -q 'ktadd -k /tmp/jhs.service.keytab jhs/hadoop.demo-datawalk.com HTTP/hadoop.demo-datawalk.com'
kadmin.local -q 'ktadd -k /tmp/hive.service.keytab hive/hadoop.demo-datawalk.com HTTP/hadoop.demo-datawalk.com'
kadmin.local -q 'ktadd -k /tmp/spark.service.keytab spark/hadoop.demo-datawalk.com HTTP/hadoop.demo-datawalk.com'

# Add user principals
kadmin.local -q 'addprinc -pw hadoop hadoop-admin'
kadmin.local -q 'ktadd -k /tmp/hadoop-admin.keytab hadoop-admin'
"

# Copy keytabs from KDC container to local directory
docker cp kdc:/tmp/nn.service.keytab kerberos-config/keytabs/
docker cp kdc:/tmp/dn.service.keytab kerberos-config/keytabs/
docker cp kdc:/tmp/rm.service.keytab kerberos-config/keytabs/
docker cp kdc:/tmp/nm.service.keytab kerberos-config/keytabs/
docker cp kdc:/tmp/jhs.service.keytab kerberos-config/keytabs/
docker cp kdc:/tmp/hive.service.keytab kerberos-config/keytabs/
docker cp kdc:/tmp/spark.service.keytab kerberos-config/keytabs/
docker cp kdc:/tmp/hadoop-admin.keytab kerberos-config/keytabs/

# Set correct permissions
chmod 400 kerberos-config/keytabs/*.keytab
```

2. Create a script to set up Kerberos client configuration:

```bash
#!/bin/bash
# setup-kerberos-client.sh

# Create krb5.conf file
cat > kerberos-config/krb5.conf << EOF
[libdefaults]
    default_realm = HADOOP.DEMO-DATAWALK.COM
    dns_lookup_realm = false
    dns_lookup_kdc = false
    ticket_lifetime = 24h
    renew_lifetime = 7d
    forwardable = true

[realms]
    HADOOP.DEMO-DATAWALK.COM = {
        kdc = kdc.hadoop.demo-datawalk.com
        admin_server = kdc.hadoop.demo-datawalk.com
    }

[domain_realm]
    .hadoop.demo-datawalk.com = HADOOP.DEMO-DATAWALK.COM
    hadoop.demo-datawalk.com = HADOOP.DEMO-DATAWALK.COM
EOF
```

### Step 6: Modify Client Connection Scripts

Update client connection scripts to use Kerberos authentication:

1. Create a kinit script for users:

```bash
#!/bin/bash
# kinit.sh

# Provide a username if desired, otherwise use hadoop-admin
USERNAME=${1:-hadoop-admin}

# Authenticate with Kerberos
docker exec -it kdc kinit $USERNAME
```

2. Update HDFS access script:

```bash
#!/bin/bash
# hdfs-client.sh

# Ensure we have a Kerberos ticket
klist || ./kinit.sh

# Run HDFS commands
docker exec -it namenode hdfs dfs -ls /
```

### Step 7: Test and Verification

1. Start the cluster with Kerberos enabled:

```bash
docker-compose down
./generate-keytabs.sh
./setup-kerberos-client.sh
docker-compose up -d
```

2. Verify Kerberos authentication:

```bash
# Get a Kerberos ticket
./kinit.sh

# Check if the ticket was granted
klist

# Access HDFS
./hdfs-client.sh

# Access Web UI
# Use browser with SPNEGO support
```

3. Testing user access:

```bash
# Test with valid credentials
kinit hadoop-admin
hdfs dfs -ls /

# Test without credentials (should fail)
kdestroy
hdfs dfs -ls /
```

## 4. Additional Considerations

1. **SSL/TLS Configuration**: To enhance security, configure HTTPS:
   - Generate SSL certificates for web UIs
   - Update configurations to use SSL
   - Enable SSL for service-to-service communication

2. **Security Best Practices**:
   - Implement proper ACLs for HDFS directories
   - Configure group mapping for user authorization
   - Set up data encryption at rest
   - Implement secure log collection and monitoring

3. **Troubleshooting**:
   - Keep track of common Kerberos issues:
     - Time synchronization problems
     - DNS resolution issues
     - Keytab permission problems
     - Realm configuration mistakes

## 5. Implementation Checklist

- [ ] Set up KDC container
- [ ] Create Kerberos principals and keytabs
- [ ] Update Hadoop configuration files
- [ ] Modify docker-compose.yml for Kerberos
- [ ] Create automation scripts
- [ ] Test authentication
- [ ] Document the process and troubleshooting steps
- [ ] Train users on Kerberos authentication
- [ ] Implement additional security measures

By following this plan, you'll add Kerberos authentication to your Hadoop cluster on EC2, significantly improving its security posture.

---

## Human

now use available tools to apply these changes

---

## Assistant

I'll help you apply these changes to your Hadoop cluster using the available tools. Let's implement the Kerberos authentication plan step by step.

First, let's create the necessary directories for our Kerberos configuration:
```
This block is not supported on your current device yet.
```



Now, let's create the krb5.conf file which will be used for Kerberos client configuration:
```
This block is not supported on your current device yet.
```





Now, let's create the modified configuration files for Hadoop services. First, let's create a Kerberos-enabled core-site.xml:
```
This block is not supported on your current device yet.
```







Now, let's create a Kerberos-enabled hdfs-site.xml:
```
This block is not supported on your current device yet.
```









Next, let's create a Kerberos-enabled yarn-site.xml:
```
This block is not supported on your current device yet.
```






Now, let's create a Kerberos-enabled mapred-site.xml:
```
This block is not supported on your current device yet.
```







Let's modify the hadoop.env file to add Kerberos-related environment variables:
```
This block is not supported on your current device yet.
```









Now, let's create scripts for generating keytabs and user authentication:
```
This block is not supported on your current device yet.
```








```
This block is not supported on your current device yet.
```








```
This block is not supported on your current device yet.
```











Now, let's make the scripts executable:
```
This block is not supported on your current device yet.
```









Finally, let's update the docker-compose.yml to include the Kerberos configurations:
```
This block is not supported on your current device yet.
```











Let's create a new docker-compose.yml file with Kerberos support:
```
This block is not supported on your current device yet.
```

---

## Human

continue

---

## Assistant

Let me continue writing the docker-compose-kerberos.yml file to add Kerberos authentication to the rest of the services:
```
This block is not supported on your current device yet.
```



Now, let's create a script to start the Kerberos-enabled Hadoop cluster:
```
This block is not supported on your current device yet.
```





Let's make this script executable:
```
This block is not supported on your current device yet.
```









Finally, let's create a README file documenting the Kerberos integration:
```
This block is not supported on your current device yet.
```





Great! I've completed implementing the Kerberos authentication for your Hadoop cluster on EC2. Here's a summary of the changes made:

1. **Created Kerberos Configuration Files**:
   - `krb5.conf` - Main Kerberos client configuration
   - Kerberos-enabled versions of `core-site.xml`, `hdfs-site.xml`, `yarn-site.xml`, and `mapred-site.xml`
   - Updated `hadoop.env` with Kerberos settings

2. **Created Scripts**:
   - `generate-keytabs.sh` - Creates service principals and keytabs
   - `kinit.sh` - User authentication script
   - `hdfs-client.sh` - Example client script with Kerberos authentication
   - `start-kerberos-cluster.sh` - Orchestrates the deployment of the Kerberos-enabled cluster

3. **Created a Kerberos-enabled Docker Compose File**:
   - Added a KDC (Key Distribution Center) service
   - Updated all services with Kerberos configurations
   - Added volume mounts for keytabs and configuration files
   - Added proper service dependencies

4. **Added Documentation**:
   - Created `KERBEROS-README.md` with detailed instructions on how to use the Kerberos-enabled cluster
   - Included troubleshooting tips and security best practices

To use the Kerberos-enabled Hadoop cluster:

1. Run `./start-kerberos-cluster.sh` to start the cluster with Kerberos authentication
2. Use `./kinit.sh` to authenticate (default password for hadoop-admin is "hadoop")
3. Access HDFS and other services with `./hdfs-client.sh`

These changes will provide your Hadoop cluster with secure authentication, ensuring that only authorized users and services can access cluster resources. The configuration follows Hadoop security best practices while maintaining compatibility with your existing setup.

---

## Human

services.hive-server.environment.CORE_CONF_hadoop_security_authorization contains true, which is an invalid type, it should be a string, number, or a null
services.historyserver.environment.CORE_CONF_hadoop_security_authorization contains true, which is an invalid type, it should be a string, number, or a null
services.nodemanager.environment.CORE_CONF_hadoop_security_authorization contains true, which is an invalid type, it should be a string, number, or a null
services.resourcemanager.environment.CORE_CONF_hadoop_security_authorization contains true, which is an invalid type, it should be a string, number, or a null
services.hive-metastore.environment.CORE_CONF_hadoop_security_authorization contains true, which is an invalid type, it should be a string, number, or a null
services.datanode.environment.CORE_CONF_hadoop_security_authorization contains true, which is an invalid type, it should be a string, number, or a null

---

## Assistant

I'll fix those issues in the docker-compose-kerberos.yml file. The problem is that I used boolean values (true) instead of strings ("true") for the environment variables. Let me correct this:
```
This block is not supported on your current device yet.
```



I've corrected the docker-compose-kerberos.yml file by converting all the boolean values to strings in the environment variables. This is important because Docker Compose expects environment variables to be strings, not native YAML boolean types.

The changes made:
1. Changed `CORE_CONF_hadoop_security_authentication: kerberos` to `CORE_CONF_hadoop_security_authentication: "kerberos"`
2. Changed `CORE_CONF_hadoop_security_authorization: true` to `CORE_CONF_hadoop_security_authorization: "true"`
3. Changed `CORE_CONF_hadoop_rpc_protection: privacy` to `CORE_CONF_hadoop_rpc_protection: "privacy"`

These changes were applied across all services in the docker-compose-kerberos.yml file. The environment variables are now properly formatted as strings, which will resolve the validation errors you encountered.

The Hadoop configuration system will still interpret these string values correctly ("true" will be interpreted as a boolean true value in the XML configuration).

All the services should now start properly when you run the `start-kerberos-cluster.sh` script.
