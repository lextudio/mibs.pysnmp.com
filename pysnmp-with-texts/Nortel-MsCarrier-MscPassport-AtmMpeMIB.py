#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-AtmMpeMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-AtmMpeMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:29:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
RowStatus, DisplayString, Unsigned32, StorageType, Counter32, Integer32, InterfaceIndex = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "RowStatus", "DisplayString", "Unsigned32", "StorageType", "Counter32", "Integer32", "InterfaceIndex")
Link, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "Link")
mscComponents, mscPassportMIBs = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscComponents", "mscPassportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, Unsigned32, Counter64, IpAddress, TimeTicks, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Integer32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Unsigned32", "Counter64", "IpAddress", "TimeTicks", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Integer32", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmMpeMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65))
mscAtmMpe = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118))
mscAtmMpeRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1), )
if mibBuilder.loadTexts: mscAtmMpeRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeRowStatusTable.setDescription('This entry controls the addition and deletion of mscAtmMpe components.')
mscAtmMpeRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"))
if mibBuilder.loadTexts: mscAtmMpeRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeRowStatusEntry.setDescription('A single entry in the table represents a single mscAtmMpe component.')
mscAtmMpeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscAtmMpeRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscAtmMpe components. These components can be added and deleted.')
mscAtmMpeComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscAtmMpeStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeStorageType.setDescription('This variable represents the storage type value for the mscAtmMpe tables.')
mscAtmMpeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: mscAtmMpeIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeIndex.setDescription('This variable represents the index for the mscAtmMpe tables.')
mscAtmMpeCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 10), )
if mibBuilder.loadTexts: mscAtmMpeCidDataTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeCidDataTable.setDescription("This group contains the attribute for a component's Customer Identifier (CID). Refer to the attribute description for a detailed explanation of CIDs.")
mscAtmMpeCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"))
if mibBuilder.loadTexts: mscAtmMpeCidDataEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeCidDataEntry.setDescription('An entry in the mscAtmMpeCidDataTable.')
mscAtmMpeCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscAtmMpeCustomerIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeCustomerIdentifier.setDescription("This attribute holds the Customer Identifier (CID). Every component has a CID. If a component has a cid attribute, the component's CID is the provisioned value of that attribute; otherwise the component inherits the CID of its parent. The top- level component has a CID of 0. Every operator session also has a CID, which is the CID provisioned for the operator's user ID. An operator will see only the stream data for components having a matching CID. Also, the operator will be allowed to issue commands for only those components which have a matching CID. An operator CID of 0 is used to identify the Network Manager (referred to as 'NetMan' in DPN). This CID matches the CID of any component. Values 1 to 8191 inclusive (equivalent to 'basic CIDs' in DPN) may be assigned to specific customers.")
mscAtmMpeIfEntryTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 11), )
if mibBuilder.loadTexts: mscAtmMpeIfEntryTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeIfEntryTable.setDescription('This group contains the provisionable attributes for the ifEntry.')
mscAtmMpeIfEntryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"))
if mibBuilder.loadTexts: mscAtmMpeIfEntryEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeIfEntryEntry.setDescription('An entry in the mscAtmMpeIfEntryTable.')
mscAtmMpeIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscAtmMpeIfAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeIfAdminStatus.setDescription('The desired state of the interface. The up state indicates the interface is operational. The down state indicates the interface is not operational. The testing state indicates that no operational packets can be passed.')
mscAtmMpeIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 11, 1, 2), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeIfIndex.setDescription('This is the index for the IfEntry. Its value is automatically initialized during the provisioning process.')
mscAtmMpeProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 12), )
if mibBuilder.loadTexts: mscAtmMpeProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeProvTable.setDescription('This group contains the provisioned attributes for the AtmMpe component.')
mscAtmMpeProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"))
if mibBuilder.loadTexts: mscAtmMpeProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeProvEntry.setDescription('An entry in the mscAtmMpeProvTable.')
mscAtmMpeMaxTransmissionUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(256, 9188)).clone(9188)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscAtmMpeMaxTransmissionUnit.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeMaxTransmissionUnit.setDescription('This attribute sets the size of the largest datagram which can be sent on the interface. This includes the size of the Logical Link Control header (if applicable) as well as the protocol data unit.')
mscAtmMpeEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("llcEncap", 1), ("ipVcEncap", 2), ("ipxVcEncap", 3))).clone('llcEncap')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscAtmMpeEncapType.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeEncapType.setDescription('This attribute specifies the rfc1483 encapsulation type to be used for the AtmConnections under this AtmMpe. Specifying llcEncap allows multiplexing of multiple protocols over the VCCs. The protocol of the carried PDU will be identified by an IEEE 802.2 Logical Link Control header. If Bridging or Inverse ARP is to be carried over a VCC, llcEncap must be used. Specifying ipVcEncap or ipxVcEncap indicates that all the VCCs (i.e. AtmConnections) under an AtmMpe component will use VC based multiplexing and will carry IP or IPX PDUs only. Thus an IpxPort cannot be provisioned under a protocol port linked to an AtmMpe component with encapsulation type of ipVcEncap. Similarly, an IpPort cannot be provisioned under a protocol port linked to an AtmMpe component with encapsulation type of ipxVcEncap.')
mscAtmMpeIlsForwarder = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 12, 1, 3), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscAtmMpeIlsForwarder.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeIlsForwarder.setDescription('This attribute specifies the IlsForwarder component this AtmMpe component is using.')
mscAtmMpeMediaProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 13), )
if mibBuilder.loadTexts: mscAtmMpeMediaProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeMediaProvTable.setDescription('This group contains the base provisioning data for the Atm Mpe component.')
mscAtmMpeMediaProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"))
if mibBuilder.loadTexts: mscAtmMpeMediaProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeMediaProvEntry.setDescription('An entry in the mscAtmMpeMediaProvTable.')
mscAtmMpeLinkToProtocolPort = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 13, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscAtmMpeLinkToProtocolPort.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeLinkToProtocolPort.setDescription('This attribute contains a protocol port component name. The attribute associates an AtmMpe application with a protocol port.')
mscAtmMpeStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 14), )
if mibBuilder.loadTexts: mscAtmMpeStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
mscAtmMpeStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 14, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"))
if mibBuilder.loadTexts: mscAtmMpeStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeStateEntry.setDescription('An entry in the mscAtmMpeStateTable.')
mscAtmMpeAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 14, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
mscAtmMpeOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
mscAtmMpeUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
mscAtmMpeOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 15), )
if mibBuilder.loadTexts: mscAtmMpeOperStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeOperStatusTable.setDescription('This group includes the Operational Status attribute. This attribute defines the current operational state of this component.')
mscAtmMpeOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 15, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"))
if mibBuilder.loadTexts: mscAtmMpeOperStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeOperStatusEntry.setDescription('An entry in the mscAtmMpeOperStatusTable.')
mscAtmMpeSnmpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeSnmpOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeSnmpOperStatus.setDescription('The current state of the interface. The up state indicates the interface is operational and capable of forwarding packets. The down state indicates the interface is not operational, thus unable to forward packets. testing state indicates that no operational packets can be passed.')
mscAtmMpeAc = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2))
mscAtmMpeAcRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1), )
if mibBuilder.loadTexts: mscAtmMpeAcRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcRowStatusTable.setDescription('This entry controls the addition and deletion of mscAtmMpeAc components.')
mscAtmMpeAcRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeAcIndex"))
if mibBuilder.loadTexts: mscAtmMpeAcRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcRowStatusEntry.setDescription('A single entry in the table represents a single mscAtmMpeAc component.')
mscAtmMpeAcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscAtmMpeAcRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscAtmMpeAc components. These components can be added and deleted.')
mscAtmMpeAcComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscAtmMpeAcStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcStorageType.setDescription('This variable represents the storage type value for the mscAtmMpeAc tables.')
mscAtmMpeAcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: mscAtmMpeAcIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcIndex.setDescription('This variable represents the index for the mscAtmMpeAc tables.')
mscAtmMpeAcProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 10), )
if mibBuilder.loadTexts: mscAtmMpeAcProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcProvTable.setDescription('This group contains the provisioned attributes for the AtmConnection component.')
mscAtmMpeAcProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeAcIndex"))
if mibBuilder.loadTexts: mscAtmMpeAcProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcProvEntry.setDescription('An entry in the mscAtmMpeAcProvTable.')
mscAtmMpeAcAtmConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscAtmMpeAcAtmConnection.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcAtmConnection.setDescription('This attribute specifies the Atm nailed up endpoint, AtmIf/n Vcc/ vpi.vci Nep, that this connection is associated with.')
mscAtmMpeAcIpCoS = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscAtmMpeAcIpCoS.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcIpCoS.setDescription("This attribute specifies the Class of Service (CoS) given to each packet received on an ATM connection. The initial CoS given to a packet may be overridden when the cosPolicyAssignment attribute is defined on either the IpPort component of the ProtocolPort linked to the ATM MPE or the Ip component of the protocol port's VirtualRouter. When a packet is to be transmitted on an ATM MPE protocol port where multiple connections are available for the packet's next hop, the packet is forwarded on the connection where the ipCos value matches the CoS of the packet. When the packets' CoS does not match the ipCos value of any of the available connections, the packet is forwarded using next lowest CoS; failing this, the packet is forwarded using the next highest CoS.")
mscAtmMpeAcStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 11), )
if mibBuilder.loadTexts: mscAtmMpeAcStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
mscAtmMpeAcStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeAcIndex"))
if mibBuilder.loadTexts: mscAtmMpeAcStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcStateEntry.setDescription('An entry in the mscAtmMpeAcStateTable.')
mscAtmMpeAcAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
mscAtmMpeAcOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
mscAtmMpeAcUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
mscAtmMpeAcOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 12), )
if mibBuilder.loadTexts: mscAtmMpeAcOperTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcOperTable.setDescription('This group contains the operational attributes for the AtmConnection component.')
mscAtmMpeAcOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeAcIndex"))
if mibBuilder.loadTexts: mscAtmMpeAcOperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcOperEntry.setDescription('An entry in the mscAtmMpeAcOperTable.')
mscAtmMpeAcSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 12, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcSpeed.setDescription('This attribute indicates the approximate bit rate for the connection. The bit rate is determined from the cell rate provisioned for the Vcc linked to this connection. The cell rate is multiplied by 53 bytes per cell and 8 bits per byte to obtain the bit rate. The ifSpeed of the entry in the ifTable corresponding to the AtmMpe component is the lowest speed of all the connections associated with the AtmMpe component.')
mscAtmMpeAcStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13), )
if mibBuilder.loadTexts: mscAtmMpeAcStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcStatsTable.setDescription('This group contains the frame based statistics maintained for the AtmConnection component. For cell based statistics, see the Vcc component.')
mscAtmMpeAcStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeIndex"), (0, "Nortel-MsCarrier-MscPassport-AtmMpeMIB", "mscAtmMpeAcIndex"))
if mibBuilder.loadTexts: mscAtmMpeAcStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcStatsEntry.setDescription('An entry in the mscAtmMpeAcStatsTable.')
mscAtmMpeAcOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcOutPackets.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcOutPackets.setDescription('This attribute counts the total number of packets sent on this connection. This counter will wrap around to 0 when it exceeds its maximum count.')
mscAtmMpeAcOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcOutOctets.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcOutOctets.setDescription('This attribute counts the total number of octets sent on this connection. This counter will wrap around to 0 when it exceeds its maximum count. DESCRIPTION')
mscAtmMpeAcOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcOutDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcOutDiscards.setDescription('This attribute counts the total number of packets which were supposed to be sent on this connection but were discarded due to congestion or the connection being down. This counter will wrap around to 0 when it exceeds its maximum count. DESCRIPTION')
mscAtmMpeAcInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcInPackets.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcInPackets.setDescription('This attribute counts the total number of packets received on this connection. This counter will wrap around to 0 when it exceeds its maximum count. DESCRIPTION')
mscAtmMpeAcInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcInOctets.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcInOctets.setDescription('The attribute counts the total number of octets received on this connection. This counter will wrap around to 0 when it exceeds its maximum count. DESCRIPTION')
mscAtmMpeAcInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcInUnknownProtos.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcInUnknownProtos.setDescription('This attribute counts the total number of packets received on this connection which were discarded because they contained an unknown or unsupported protocol (includes packets received for protocols not currently bound to the associated ProtocolPort component). This counter will wrap around to 0 when it exceeds its maximum count. DESCRIPTION')
mscAtmMpeAcInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 118, 2, 13, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscAtmMpeAcInErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscAtmMpeAcInErrors.setDescription('This attribute counts the total number of packets received on the connection which contained errors preventing them from being delivered to a higher-layer protocol (includes short frames). This counter will wrap around to 0 when it exceeds its maximum count. DESCRIPTION')
atmMpeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 1))
atmMpeGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 1, 1))
atmMpeGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 1, 1, 3))
atmMpeGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 1, 1, 3, 2))
atmMpeCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 3))
atmMpeCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 3, 1))
atmMpeCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 3, 1, 3))
atmMpeCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 65, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-AtmMpeMIB", mscAtmMpeRowStatusEntry=mscAtmMpeRowStatusEntry, mscAtmMpeAcStateEntry=mscAtmMpeAcStateEntry, atmMpeGroup=atmMpeGroup, mscAtmMpeAcSpeed=mscAtmMpeAcSpeed, mscAtmMpeMediaProvTable=mscAtmMpeMediaProvTable, mscAtmMpeIfEntryTable=mscAtmMpeIfEntryTable, mscAtmMpeCustomerIdentifier=mscAtmMpeCustomerIdentifier, mscAtmMpeAcUsageState=mscAtmMpeAcUsageState, mscAtmMpeAcStateTable=mscAtmMpeAcStateTable, mscAtmMpeAcProvTable=mscAtmMpeAcProvTable, mscAtmMpeAc=mscAtmMpeAc, mscAtmMpeAcStorageType=mscAtmMpeAcStorageType, atmMpeCapabilitiesCA02=atmMpeCapabilitiesCA02, mscAtmMpe=mscAtmMpe, mscAtmMpeOperationalState=mscAtmMpeOperationalState, mscAtmMpeProvTable=mscAtmMpeProvTable, mscAtmMpeAdminState=mscAtmMpeAdminState, mscAtmMpeAcOutDiscards=mscAtmMpeAcOutDiscards, mscAtmMpeAcIndex=mscAtmMpeAcIndex, mscAtmMpeOperStatusEntry=mscAtmMpeOperStatusEntry, mscAtmMpeAcIpCoS=mscAtmMpeAcIpCoS, mscAtmMpeProvEntry=mscAtmMpeProvEntry, atmMpeMIB=atmMpeMIB, mscAtmMpeUsageState=mscAtmMpeUsageState, mscAtmMpeAcRowStatusTable=mscAtmMpeAcRowStatusTable, mscAtmMpeAcAdminState=mscAtmMpeAcAdminState, mscAtmMpeCidDataEntry=mscAtmMpeCidDataEntry, mscAtmMpeIndex=mscAtmMpeIndex, mscAtmMpeAcOperTable=mscAtmMpeAcOperTable, mscAtmMpeRowStatus=mscAtmMpeRowStatus, mscAtmMpeAcAtmConnection=mscAtmMpeAcAtmConnection, mscAtmMpeAcComponentName=mscAtmMpeAcComponentName, mscAtmMpeSnmpOperStatus=mscAtmMpeSnmpOperStatus, mscAtmMpeStorageType=mscAtmMpeStorageType, mscAtmMpeAcOutOctets=mscAtmMpeAcOutOctets, mscAtmMpeLinkToProtocolPort=mscAtmMpeLinkToProtocolPort, mscAtmMpeAcInUnknownProtos=mscAtmMpeAcInUnknownProtos, atmMpeCapabilitiesCA=atmMpeCapabilitiesCA, mscAtmMpeAcInPackets=mscAtmMpeAcInPackets, atmMpeGroupCA=atmMpeGroupCA, atmMpeGroupCA02A=atmMpeGroupCA02A, mscAtmMpeIfAdminStatus=mscAtmMpeIfAdminStatus, mscAtmMpeStateEntry=mscAtmMpeStateEntry, mscAtmMpeEncapType=mscAtmMpeEncapType, mscAtmMpeAcOperEntry=mscAtmMpeAcOperEntry, mscAtmMpeCidDataTable=mscAtmMpeCidDataTable, mscAtmMpeAcInErrors=mscAtmMpeAcInErrors, mscAtmMpeComponentName=mscAtmMpeComponentName, mscAtmMpeIfIndex=mscAtmMpeIfIndex, mscAtmMpeMaxTransmissionUnit=mscAtmMpeMaxTransmissionUnit, mscAtmMpeAcStatsTable=mscAtmMpeAcStatsTable, mscAtmMpeAcOutPackets=mscAtmMpeAcOutPackets, atmMpeCapabilitiesCA02A=atmMpeCapabilitiesCA02A, mscAtmMpeAcRowStatusEntry=mscAtmMpeAcRowStatusEntry, atmMpeGroupCA02=atmMpeGroupCA02, mscAtmMpeOperStatusTable=mscAtmMpeOperStatusTable, mscAtmMpeAcOperationalState=mscAtmMpeAcOperationalState, atmMpeCapabilities=atmMpeCapabilities, mscAtmMpeAcProvEntry=mscAtmMpeAcProvEntry, mscAtmMpeAcRowStatus=mscAtmMpeAcRowStatus, mscAtmMpeStateTable=mscAtmMpeStateTable, mscAtmMpeIlsForwarder=mscAtmMpeIlsForwarder, mscAtmMpeAcStatsEntry=mscAtmMpeAcStatsEntry, mscAtmMpeAcInOctets=mscAtmMpeAcInOctets, mscAtmMpeMediaProvEntry=mscAtmMpeMediaProvEntry, mscAtmMpeIfEntryEntry=mscAtmMpeIfEntryEntry, mscAtmMpeRowStatusTable=mscAtmMpeRowStatusTable)