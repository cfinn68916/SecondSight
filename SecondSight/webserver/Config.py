#!/usr/bin/env python

import logging
from flask import Flask, render_template, Response, redirect, request, jsonify
import SecondSight


def start(app):
    @app.route('/config', methods=['GET', 'POST'])
    def config():
        conf = SecondSight.config.Configuration()  # I think this is how singleton classes work
        if request.method=='GET':
            return render_template('config.html', nt_dest=conf.get_value('nt_dest'))  # , cams=cams)
        else:
            conf.set_value('nt_dest', request.form['nt_addr'])
            conf.set_value('cameras', [])
            conf.set_value('detects', [])
            for k, v in request.form.items():
                if k == 'cube2023':
                    conf.set_value('detects', conf.get_value('detects')+['cube2023'])
                if k.startswith('cam_port_'):
                    roles = []
                    if f"apriltags_{k.split('_')[-1]}" in request.form:
                        if request.form[f"apriltags_{k.split('_')[-1]}"] == 'on':
                            roles.append('apriltag')
                    if f"game_objs_{k.split('_')[-1]}" in request.form:
                        if request.form[f"game_objs_{k.split('_')[-1]}"] == 'on':
                            roles.append('conecube')
                    conf.set_value('cameras', conf.get_value('cameras') +
                                   [{
                                       'port': v,
                                       'calibration': None,
                                       'role': roles,
                                       'pos': None
                                   }])
            app.cameras = SecondSight.Cameras.loadCameras()
            conf.set_value('config_required', False)
            conf.write()
            return Response('Please restart the code')


if __name__ == "__main__":
    # This file should never be run
    pass
