ids_to_elements = {
  0: "StartEvent",
  1: "ServiceTask",
  2: "EndEvent",
  3: "UserTask",

  30: "SequenceFlowShort",
  31: "SequenceFlowLong",

  40: "GatewayInclusive",
  41: "GatewayExclusive",
  42: "GatewayParallel",
}


def id_to_elements(id):
    try:
      return ids_to_elements[id]
    except:
      return "Unknown element type for id: " + str(id)
