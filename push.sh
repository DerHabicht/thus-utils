#!/bin/bash

source "$HOME/lib/thus_utils/default_repos.sh"

# Sync Taskwarrior
task sync

# Sync relevant Git repositories
cat ~/.active_proj_dirs >> ~/.proj_dirs
printf "%s\n" "${default_repos[@]}" >> ~/.proj_dirs


failed=()
while IFS= read -r line
do
    cd "$line"
    printf "\nCommitting `pwd`...\n"
    git add *
    git commit -a -m "Automated commit from $HOSTNAME"
    git push
    if [ "$?" != 0 ]
    then
        failed+=(`pwd`)
    fi
done < ~/.proj_dirs

rm ~/.proj_dirs

if [ "$failed" ]
then
    printf "\nThe following repositories failed to push:\n"
    printf "    ${failed[@]}"
fi
