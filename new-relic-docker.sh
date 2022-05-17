docker run \
-d \
--name newrelic-infra \
--network=host \
--cap-add=SYS_PTRACE \
--privileged \
--pid=host \
-v "/:/host:ro" \
-v "/var/run/docker.sock:/var/run/docker.sock" \
-e NRIA_LICENSE_KEY=e9f41394799407405c74b789d72e126a3a41NRAL \
newrelic/infrastructure:latest