docker stop qf_cpu
docker rm qf_cpu
docker run -d -p 8888:8888 -v %CD%/:/src --restart=always --name qf_cpu qf