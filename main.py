from worker import *

# ------------------------------------------------------------------------------
# PROCESS STEPS
# ------------------------------------------------------------------------------


def step1(x):
    return file.file_to_str(x)


def step2(x):
    return file.str_to_json(x)


def step3(x):
    return id(x)


def step4(x):
    return dir.copy_folder(x.src, x.dest)


# ------------------------------------------------------------------------------
# SUB PROCESS
# ------------------------------------------------------------------------------


def sub_process(x):
    y = process.process_steps(x, [step1, step2, step3])
    return y


# ------------------------------------------------------------------------------
# PROCESS
# ------------------------------------------------------------------------------


def process(input):
    s4 = process.process_steps(input, [sub_process, step4])
    return s4


# ------------------------------------------------------------------------------
# PRODUCER -> CONSUMER
# ------------------------------------------------------------------------------

import goless

# main
#
if __name__ == "__main__":

    ## Define Channels
    ##
    done = goless.chan()
    ins = goless.chan()
    outs = goless.chan()

    #      +--+--+
    #      |  P  |
    #      +--+--+
    #         | INS
    #    +----+----+--- ... ---+
    #    |         |           |
    # +--+--+   +--+--+     +--+--+
    # | C 1 |   | C 2 | ... | C n |
    # +--+--+   +--+--+     +--+--+
    #    |         |
    #    +----+----+
    #         | OUTS
    #      +--+--+
    #      |  L  |
    #      +--+--+
    #         |
    #        DONE

    #
    # PRODUCER (P)
    #

    def produce():
        # Produce inputs
        #
        print("start produce!")
        xs = dir.list_dir("./input")
        print(
            f"produced {len(xs)} items",
        )
        print("send items into consumer channel")
        for x in xs:
            ins.send(x)

        # All inputs send -> close channel
        #
        ins.close()

    ##
    ## CONSUMER (C n)
    ##

    def consume(name):
        for in_ in ins:  # Drain all inputs (ins)
            outs.send("%s: '%s' " % (name, in_))
        outs.close()

    #
    # Logger (L)
    #
    def logger():
        for out in outs:  # Drain all outputs (outs)
            print(out)
        # If channel is empty -> send done
        done.send()

    # 1 Produce
    goless.go(produce)

    # 2 start N consumers
    for i in range(0, 3):
        goless.go(consume, "consumer_" + str(i))

    # 3 Log out
    goless.go(logger)

    # Wait until done
    #
    done.recv()
    print("done!!")
