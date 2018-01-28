import subprocess
import os

fn = 'a11'
gpp_path = None

def setup_module(module):
    global gpp_path
    try_paths = [['C:%s'%os.sep, 'Program Files (x86)', 'Dev-Cpp'],
                 ['C:%s'%os.sep, 'Program Files', 'Dev-Cpp'],
                 ['/', 'usr', 'bin']]


    tried_paths = []
    for p in try_paths:
        path = os.path.join(*p)  # splat the list

        gpp_name = 'g++'
        if os.name == 'nt': gpp_name += '.exe'  # windows!

        exec_path = find(gpp_name, path)
        if exec_path is not None:
            gpp_path = exec_path  # gotcha
            return
        tried_paths.append(path)

    assert False, """Failed to find g++ in any known location. Make sure you have one of the following in the default paths:
        - *nix or Mac (we'll look for g++ in /usr/bin)
        - Dev-CPP IDE installed in
        - Cygnus distribution, see here http://www1.cmc.edu/pages/faculty/alee/g++/g++.html

        Looked in:
        """ + str(tried_paths)


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def teardown_module(module):
    cleanup()  # cleanup at end to remove object code file
    pass

def compile_program():
    if gpp_path is None:
        assert False, "No g++, cannot continue."

    args = [gpp_path, fn+'.cpp', '-o', fn+'.out', '-w'] # suppress warning (for windows)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    print err
    # print '[', out, ']'
    return (err == '' or err == None) # no error means we compiled fine

def cleanup():
    import os
    frem = fn + '.out'
    if os.path.exists(frem):
        os.remove(frem)

def test_compile():
    res = compile_program()
    assert res


##### TESTS START HERE



def test_hello():
    args = ['./' + fn + '.out']
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    ground = ['Hello world!', 'Hello world from cout ...']

    # windows and it's \r issue
    out_stripped = [i.strip() for i in out.split('\n') if i.strip() != '']

    assert out_stripped == ground



# output capturing decorator
def capture_output(fn):
    def wrapper(*args, **kwargs):
        import StringIO
        import sys
        orig_stdout = sys.stdout
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput

        v = fn(*args, **kwargs)

        sys.stdout = orig_stdout # don't rely on __stdout__

        # print 'Captured', capturedOutput.getvalue()
        output_val = capturedOutput.getvalue()
        return v, output_val

    return wrapper
