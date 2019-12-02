#!/usr/bin/env bash
gunicorn Bus.wsgi:application &
