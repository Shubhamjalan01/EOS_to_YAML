# EOS_to_YAML
### Running the Scripts
<pre>
# Clone the repo
git clone https://github.com/Shubhamjalan01/EOS_to_YAML.git

# Import Yaml library in python scripts

# Run the Python script
</pre>
## Task1: Access lists
### Input:
EOS Configuration:  
<pre>
IP Access List test1
  10 permit ip 10.10.10.0/24 any  
  20 permit ip 10.30.10.0/24 host 10.20.10.1
</pre>  
### Expected output:
YAML:
<pre>
access_lists:
  test1:
    counters_per_entry: true
    sequence_numbers:
      10:
        action: permit ip 10.10.10.0/24 any
      20:
        action: permit ip 10.30.10.0/24 host 10.20.10.1
</pre>
