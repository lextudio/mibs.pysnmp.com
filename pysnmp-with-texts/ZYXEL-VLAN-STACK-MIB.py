#
# PySNMP MIB module ZYXEL-VLAN-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-VLAN-STACK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:52:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, MibIdentifier, TimeTicks, NotificationType, Gauge32, ObjectIdentity, Integer32, Bits, Counter32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "MibIdentifier", "TimeTicks", "NotificationType", "Gauge32", "ObjectIdentity", "Integer32", "Bits", "Counter32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelVlanStack = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89))
if mibBuilder.loadTexts: zyxelVlanStack.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelVlanStack.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelVlanStack.setContactInfo('')
if mibBuilder.loadTexts: zyxelVlanStack.setDescription('The subtree for VLAN Stack')
zyxelVlanStackSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1))
zyVlanStackState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanStackState.setStatus('current')
if mibBuilder.loadTexts: zyVlanStackState.setDescription('Enable/Disable VLAN Stacking for the switch.')
zyxelVlanStackPortTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2), )
if mibBuilder.loadTexts: zyxelVlanStackPortTable.setStatus('current')
if mibBuilder.loadTexts: zyxelVlanStackPortTable.setDescription('The table contains VLAN stack configuration.')
zyxelVlanStackPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: zyxelVlanStackPortEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelVlanStackPortEntry.setDescription('An entry contains VLAN stack configuration.')
zyVlanStackPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("access", 2), ("tunnel", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanStackPortMode.setStatus('current')
if mibBuilder.loadTexts: zyVlanStackPortMode.setDescription("VLAN stacking mode of the port: Set Normal mode to have the switch ignore frames received(or transmitted) on this port with VLAN stacking tags. Set Access mode to have the switch add the SP TPID tag to all incoming frames received on this port. It is for ingress ports at the edge of the service provider's network. Set Tunnel mode (available for Gigabit ports only) for egress ports at the edge of the service provider's network. In order to support VLAN stacking on a port, the port must be able to allow frames of 1526 Bytes (1522 Bytes + 4 Bytes for the second tag) to pass through it.")
zyVlanStackPortVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanStackPortVid.setStatus('current')
if mibBuilder.loadTexts: zyVlanStackPortVid.setDescription("Stacking port VLAN ID is the service provider's VLAN ID (the outer VLAN tag). Set the service provider ID (from 1 to 4094) for frames received on this port.")
zyVlanStackPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("priority0", 0), ("priority1", 1), ("priority2", 2), ("priority3", 3), ("priority4", 4), ("priority5", 5), ("priority6", 6), ("priority7", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanStackPortPriority.setStatus('current')
if mibBuilder.loadTexts: zyVlanStackPortPriority.setDescription("Set a priority level (from 0 to 7). This is the service provider's priority level that adds to the frames received on this port. 0 is the lowest priority level and 7 is the highest.")
zyVlanStackTunnelPortTpid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyVlanStackTunnelPortTpid.setStatus('current')
if mibBuilder.loadTexts: zyVlanStackTunnelPortTpid.setDescription("TPID is a standard Ethernet type code identifying the frame and indicates whether the frame carries IEEE 802.1Q tag information. Set a four-digit hexadecimal number from 0000 to FFFF that the switch adds in the outer VLAN tag of the frames sent on the tunnel port(s). The switch also uses this to check if the received frames are double-tagged. The value of this field is 0x8100 as defined in IEEE 802.1Q. If the switch needs to communicate with other vendors' devices, they should use the same TPID.")
zySelectiveQinQMaxNumberOfRules = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySelectiveQinQMaxNumberOfRules.setStatus('current')
if mibBuilder.loadTexts: zySelectiveQinQMaxNumberOfRules.setDescription('The maximum number of selective Q-in-Q that can be created.')
zyxelSelectiveQinQTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4), )
if mibBuilder.loadTexts: zyxelSelectiveQinQTable.setStatus('current')
if mibBuilder.loadTexts: zyxelSelectiveQinQTable.setDescription('The table contains selective Q-in-Q configuration.')
zyxelSelectiveQinQEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1), ).setIndexNames((0, "ZYXEL-VLAN-STACK-MIB", "zySelectiveQinQPort"), (0, "ZYXEL-VLAN-STACK-MIB", "zySelectiveQinQCvid"))
if mibBuilder.loadTexts: zyxelSelectiveQinQEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelSelectiveQinQEntry.setDescription('An entry contains selective Q-in-Q configuration.')
zySelectiveQinQName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySelectiveQinQName.setStatus('current')
if mibBuilder.loadTexts: zySelectiveQinQName.setDescription('Set the name of selective Q-in-Q entry.')
zySelectiveQinQPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: zySelectiveQinQPort.setStatus('current')
if mibBuilder.loadTexts: zySelectiveQinQPort.setDescription('Interface port ID.')
zySelectiveQinQCvid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 3), Integer32())
if mibBuilder.loadTexts: zySelectiveQinQCvid.setStatus('current')
if mibBuilder.loadTexts: zySelectiveQinQCvid.setDescription('The customer VLAN ID (the inner VLAN tag) from 1 to 4094. This is the VLAN tag carried in the packets from the subscribers.')
zySelectiveQinQSpvid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySelectiveQinQSpvid.setStatus('current')
if mibBuilder.loadTexts: zySelectiveQinQSpvid.setDescription("Stacking port VLAN ID is the service provider's VLAN ID (the outer VLAN tag). Set the service provider ID (from 1 to 4094) for frames received on this port.")
zySelectiveQinQPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("priority0", 0), ("priority1", 1), ("priority2", 2), ("priority3", 3), ("priority4", 4), ("priority5", 5), ("priority6", 6), ("priority7", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zySelectiveQinQPriority.setStatus('current')
if mibBuilder.loadTexts: zySelectiveQinQPriority.setDescription("Set a priority level (from 0 to 7). This is the service provider's priority level that adds to the frames received on this port. 0 is the lowest priority level and 7 is the highest.")
zySelectiveQinQRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zySelectiveQinQRowStatus.setStatus('current')
if mibBuilder.loadTexts: zySelectiveQinQRowStatus.setDescription('This object allows entries to be created and deleted from the selective Q-in-Q table')
mibBuilder.exportSymbols("ZYXEL-VLAN-STACK-MIB", zySelectiveQinQCvid=zySelectiveQinQCvid, zySelectiveQinQPort=zySelectiveQinQPort, zyxelVlanStackPortTable=zyxelVlanStackPortTable, zyxelVlanStack=zyxelVlanStack, zyxelVlanStackSetup=zyxelVlanStackSetup, PYSNMP_MODULE_ID=zyxelVlanStack, zySelectiveQinQMaxNumberOfRules=zySelectiveQinQMaxNumberOfRules, zyVlanStackTunnelPortTpid=zyVlanStackTunnelPortTpid, zyxelSelectiveQinQTable=zyxelSelectiveQinQTable, zyxelSelectiveQinQEntry=zyxelSelectiveQinQEntry, zyVlanStackPortMode=zyVlanStackPortMode, zyVlanStackPortVid=zyVlanStackPortVid, zyxelVlanStackPortEntry=zyxelVlanStackPortEntry, zySelectiveQinQName=zySelectiveQinQName, zyVlanStackPortPriority=zyVlanStackPortPriority, zyVlanStackState=zyVlanStackState, zySelectiveQinQSpvid=zySelectiveQinQSpvid, zySelectiveQinQRowStatus=zySelectiveQinQRowStatus, zySelectiveQinQPriority=zySelectiveQinQPriority)