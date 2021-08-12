ids_to_elements = {0: "StartEvent", 1: "ServiceTask", 2: "EndEvent", 30: "SequenceFlowShort", 31: "SequenceFlowLong"}


def id_to_elements(id):
    try:
      return ids_to_elements[id]
    except:
      return "Unknown element type for id:" + str(id)