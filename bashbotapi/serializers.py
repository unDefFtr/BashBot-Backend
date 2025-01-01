from rest_framework import serializers
import os
import subprocess
import time

class BashSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)

    def to_representation(self, instance):
        #encoded_string = base64.b64encode(instance['text'].encode('utf-8')).decode('utf-8')
        #encoded_strings = os.popen("bash -c '" + instance['text'] + "'").readlines()
        proc = subprocess.Popen("bash -c '" + instance['text'] + "'", stderr=subprocess.STDOUT, stdout = subprocess.PIPE, shell=True)
        t_beginning = time.time()
        while True:
            if proc.poll() is not None:
                break
            seconds_passwd = time.time() - t_beginning
            if seconds_passwd > 60:
                proc.terminate()
                return {'command_result' : '60s timeout'}
            time.sleep(0.1)
        encoded_strings = proc.stdout.readlines()
        encoded_string = ""
        for i in encoded_strings:
            encoded_string += i.decode('utf-8')
            encoded_string += "\n"
        return {'command_result': encoded_string}
