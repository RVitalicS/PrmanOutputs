# KATANA Render Outputs

**for RenderMan**


![alt text](./Doc/description.png)





**Launcher Example**

```bash
#!/usr/bin/env bash
# Katana launcher script
 
THISDIR=$(dirname "$(readlink -e "$BASH_SOURCE")")
 
export LUA_PATH=$THISDIR/OpScript/?.lua
export RMANOUTPUTS=$THISDIR
 
export KATANA_RESOURCES=$KATANA_RESOURCES:$RMANOUTPUTS
 
# export KATANA_HOME=...
# exec "${KATANA_HOME}/bin/katanaBin" "$@"
```