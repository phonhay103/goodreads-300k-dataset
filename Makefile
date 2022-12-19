# Best effort commands
amend:
	@git commit --amend --no-edit && git push -f
am: amend

add:
	@git add -A && git reset -- Makefile
a: add

amend-all: add amend
aa: amend-all

pull-new:
	@git add -A && git stash
	@git checkout develop
	@git pull
p: pull-new
