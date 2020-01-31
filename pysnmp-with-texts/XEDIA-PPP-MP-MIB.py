#
# PySNMP MIB module XEDIA-PPP-MP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-PPP-MP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:43:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, NotificationType, Gauge32, MibIdentifier, Bits, IpAddress, ModuleIdentity, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "IpAddress", "ModuleIdentity", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaPppMpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 21))
if mibBuilder.loadTexts: xediaPppMpMIB.setLastUpdated('9809171500Z')
if mibBuilder.loadTexts: xediaPppMpMIB.setOrganization('Xedia Corp.')
if mibBuilder.loadTexts: xediaPppMpMIB.setContactInfo('support@xedia.com')
if mibBuilder.loadTexts: xediaPppMpMIB.setDescription("This module defines objects for management of Xedia's PPP Multilink Protocol component.")
xediaPppMpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 21, 1))
xediaPppMpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 21, 2))
mpBundle = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1))
class Unsigned32(Gauge32):
    pass

mpBundleStatusTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1), )
if mibBuilder.loadTexts: mpBundleStatusTable.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusTable.setDescription('A table containing Multilink PPP bundle specific variables for this Multilink PPP implementation. The following objects reflect the values of the option parameters negotiated during the PPP Link Control Protocol negotiation for links that reside in this MP Bundle: mpBundleStatusLocalMRRU mpBundleStatusRemoteMRRU mpBundleStatusLocalEndpointDiscr mpBundleStatusRemoteEndpointDiscr mpBundleStatusRcvShortSeq mpBundleStatusXmtShortSeq mpBundleStatusSmallPktMaxSize mpBundleStatusMediumPktMaxSize These values are not meaningful until after the PPP Option negotiation has completed, which is indicated by the link reaching the open state (i.e., ifOperStatus is set to up). Therefore, when ifOperStatus is not up, the values of these variables will reflect unnegotiated values, i.e. MRRU and Endpoint Discriminator values will be 0 while the Rcv and Xmt Short Sequence Numbers will be disabled.')
mpBundleStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mpBundleStatusEntry.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusEntry.setDescription('Management information about a particular PPP Multilink Protocol Bundle.')
mpBundleStatusPacketTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusPacketTooLongs.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusPacketTooLongs.setDescription('The number of received packets that have been discarded because their length exceeded the MRRU.')
mpBundleStatusLocalMRRU = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusLocalMRRU.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusLocalMRRU.setDescription('The current value of the Maximum Receive Reconstructed Unit (MRRU) for the local MP entity. This value is the MRRU that the remote MP entity is using when sending packets to the local MP entity. The value of this object is meaningful only when the bundle has reached the open state (ifOperStatus is up).')
mpBundleStatusRemoteMRRU = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusRemoteMRRU.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusRemoteMRRU.setDescription('The current value of the Maximum Receive Reconstructed Unit (MRRU) for the remote Multilink PPP Entity. This value is the MRRU that the local entity is using when sending packets to the remote Multilink PPP entity. The value of this object is meaningful only when the bundle has reached the open state (ifOperStatus is up).')
mpBundleStatusLocalEndptDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(21, 21)).setFixedLength(21)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusLocalEndptDiscr.setReference('Section 5.1.3, Endpoint Discriminator Option, of RFC1990.')
if mibBuilder.loadTexts: mpBundleStatusLocalEndptDiscr.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusLocalEndptDiscr.setDescription('The current value of the Endpoint Discriminator which identifies this Multilink PPP bundle on the local peer. When the remote peer desires to add a new link to this Multilink PPP bundle, it will include this value during link establishment of the new link. This value will indicate to the local peer that the new link is intended to join this existing Multilink PPP bundle. The first byte in the string identifies the Class of the Endpoint Discriminator. The remaining bytes in the string contain the actual Endpoint Discriminator value.')
mpBundleStatusRemoteEndptDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusRemoteEndptDiscr.setReference('Section 5.1.3, Endpoint Discriminator Option, of RFC1990.')
if mibBuilder.loadTexts: mpBundleStatusRemoteEndptDiscr.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusRemoteEndptDiscr.setDescription('The current value of the Endpoint Discriminator which identifies this Multilink PPP bundle on the remote peer. When the local peer desires to add a new link to this Multilink PPP bundle, it will include this value during link establishment of the new link. This value will indicate to the remote peer that the new link is intended to join this existing Multilink PPP bundle. The first byte in the string identifies the Class of the Endpoint Discriminator. The remaining bytes in the string contain the actual Endpoint Discriminator value.')
mpBundleStatusRcvShortSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusRcvShortSeq.setReference('Section 5.1.2, Short Sequence Number Header Format Option, of RFC1990.')
if mibBuilder.loadTexts: mpBundleStatusRcvShortSeq.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusRcvShortSeq.setDescription('Indicates whether the remote Multilink PPP entity will use the Short Sequence Number Header Format when transmitting packets to the local Multilink PPP entity. The value of this object is meaningful only when the bundle has reached the open state (ifOperStatus is up).')
mpBundleStatusXmtShortSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusXmtShortSeq.setReference('Section 5.1.2, Short Sequence Number Header Format Option, of RFC1990.')
if mibBuilder.loadTexts: mpBundleStatusXmtShortSeq.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusXmtShortSeq.setDescription('Indicates whether the local Multilink PPP entity will use the Short Sequence Number Header Format when transmitting packets to the remote Multilink PPP entity. The value of this object is meaningful only when the bundle has reached the open state (ifOperStatus is up).')
mpBundleStatusSmallPktMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusSmallPktMaxSize.setReference('(Not explicitly defined by RFC1990)')
if mibBuilder.loadTexts: mpBundleStatusSmallPktMaxSize.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusSmallPktMaxSize.setDescription('The maximum size in bytes of a Small PPP packet. Use of this parameter is no longer recommended. The MP fragmentation threshold is controlled by mpBundleStatusMediumPktMaxSize. Small PPP packets are defined to be those which will be encapsulated in a single Multilink Protocol Fragment and always sent on the first link in the Bundle. Note that this parameter only applies to outgoing PPP packets sent by this system. Reassembly of incoming packets is unaffected by this value. Note that the default value of 12 bytes effectively means that no packets are subject to this rule.')
mpBundleStatusMediumPktMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusMediumPktMaxSize.setReference('(Not explicitly defined by RFC1990)')
if mibBuilder.loadTexts: mpBundleStatusMediumPktMaxSize.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusMediumPktMaxSize.setDescription("The maximum size in bytes of a Medium PPP packet. This value specifies the threshold at which Multilink fragmentation is applied to transmitted packets, i.e. packets smaller than this size will be encapsulated in a single Multilink Protocol fragment and sent on a single link, packets larger than this size will be fragmented over all links in the bundle. This value starts at mpBundleConfigMediumPktMaxSize and is adjusted downwards according to the peer's MRRU and each of the peer's link's MRUs. Medium PPP packets are defined to be those which will be encapsulated in a single Multilink Protocol Fragment and sent on each link in the Bundle in a round-robin fashion. Packets larger than this threshold are considered Large PPP packets. Large PPP packets will be fragmented into multiple Multilink Protocol Fragments and sent across all links in the bundle. Setting this value to its maximum (65535) will prevent fragmentation at the MP layer of outgoing PPP packets, i.e. it will cause all outgoing PPP packets to be considered either Small or Medium sized PPP packets. Note that this parameter only applies to outgoing PPP packets sent by this system. Reassembly of incoming packets is unaffected by this value.")
mpBundleStatusSingleFragsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusSingleFragsRcvd.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusSingleFragsRcvd.setDescription('The number of MP fragments received that contain an entire PPP packet.')
mpBundleStatusReasmReqds = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusReasmReqds.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusReasmReqds.setDescription('The number of MP fragments received that require reassembly into PPP packets.')
mpBundleStatusReasmFails = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusReasmFails.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusReasmFails.setDescription('The number of fragmented PPP packets which failed to be reassembled.')
mpBundleStatusReasmOks = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusReasmOks.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusReasmOks.setDescription('The number of fragmented PPP packets received and successfully reassembled.')
mpBundleStatusRcvdFragsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusRcvdFragsDiscarded.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusRcvdFragsDiscarded.setDescription('The number of MP fragments discarded for some reason by the MP layer.')
mpBundleStatusDropTooManyFrags = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusDropTooManyFrags.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusDropTooManyFrags.setDescription('The number of MP fragments discarded because the MP layer has no more space to buffer fragments.')
mpBundleStatusSingleFragsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusSingleFragsSent.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusSingleFragsSent.setDescription('The number of MP fragments sent that contain an entire PPP packet.')
mpBundleStatusFragCreates = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusFragCreates.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusFragCreates.setDescription('The number of MP fragments created to contain a fragment of a PPP packet.')
mpBundleStatusFragFails = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusFragFails.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusFragFails.setDescription('The number of attempts to create an MP fragment which failed and resulted in discarding of the PPP packet to be transmitted.')
mpBundleStatusFragOks = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusFragOks.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusFragOks.setDescription('The number of MP fragments successfully sent which contain a fragment of a PPP packet.')
mpBundleStatusRcvdFragsBuffered = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpBundleStatusRcvdFragsBuffered.setStatus('current')
if mibBuilder.loadTexts: mpBundleStatusRcvdFragsBuffered.setDescription('The number of received MP fragments currently buffered awaiting reassembly and delivery')
mpBundleConfigTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2), )
if mibBuilder.loadTexts: mpBundleConfigTable.setStatus('current')
if mibBuilder.loadTexts: mpBundleConfigTable.setDescription('A table containing the LCP configuration parameters for this PPP MP Bundle. These variables represent the initial configuration of the PPP MP Bundle. The actual values of the negotiable parameters (MRRU and Short Sequence Numbers) may be changed during LCP negotiation as the link is brought up. The following objects reflect the initial values that will be proposed when LCP negotiation begins: mpBundleConfigLocalMRRU mpBundleConfigLocalEndptDiscr mpBundleConfigRcvShortSeq Note: the Endpoint Discriminator is non-negotiable, the value configured above (or the default if this is not configured) will be the Endpoint Discriminator used. The following objects are not negotiated during LCP: mpBundleConfigSmallPktMaxSize mpBundleConfigMediumPktMaxSize.')
mpBundleConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mpBundleConfigEntry.setStatus('current')
if mibBuilder.loadTexts: mpBundleConfigEntry.setDescription('Configuration information for a particular Multilink PPP Bundle.')
mpBundleConfigLocalMRRU = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpBundleConfigLocalMRRU.setReference('Section 5.1.1, Multilink MRRU LCP option of RFC 1990.')
if mibBuilder.loadTexts: mpBundleConfigLocalMRRU.setStatus('current')
if mibBuilder.loadTexts: mpBundleConfigLocalMRRU.setDescription('The initial Maximum Receive Reconstructed Unit (MRRU) that the local MP entity will advertise to the remote entity at the onset of LCP negotiation. If the value of this variable is 0 then the local MP entity will advertise the default MRRU value of 1600 bytes. Changing this object will have effect when the link is next restarted. After the link comes up, the status variable mpBundleStatusLocalMRRU will reflect the actual MRRU negotiated with the peer during LCP negotiation.')
mpBundleConfigLocalEndptDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 21)).clone(hexValue="0")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpBundleConfigLocalEndptDiscr.setReference('Section 5.1.3, Endpoint Discriminator Option, of RFC 1990.')
if mibBuilder.loadTexts: mpBundleConfigLocalEndptDiscr.setStatus('current')
if mibBuilder.loadTexts: mpBundleConfigLocalEndptDiscr.setDescription('The value to be advertised to the remote peer as the Endpoint Discriminator to be used to identify this Multilink PPP bundle. After the remote peer has received this value, it should include this value during LCP negotiation of any new links intended to join this Multilink PPP bundle. The first byte in the string identifies the Class of the Endpoint Discriminator. The remaining bytes in the string contain the actual Endpoint Discriminator value. If the value of this variable is 0 then the local peer will use the MAC address of the local box as the value to advertise as the local Endpoint Discriminator. After the link comes up, the status variable mpBundleStatusLocalEndptDiscr will reflect this Endpoint Discriminator value which has been sent to the peer (i.e. this value is not negotiated with the peer, the peer must accept whatever Endpoint Discriminator we send to them).')
mpBundleConfigRcvShortSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpBundleConfigRcvShortSeq.setReference('Section 5.1.2, Short Sequence Number Header Format Option, of RFC1990.')
if mibBuilder.loadTexts: mpBundleConfigRcvShortSeq.setStatus('current')
if mibBuilder.loadTexts: mpBundleConfigRcvShortSeq.setDescription('If enabled(1) then the local peer will attempt to negotiate Short Sequence Number Header Format for the MP encapsulated PPP traffic sent from the remote peer to the local peer. If disabled(2) then no attempt to negotiate Short Sequence Numbers will be performed, indicating that instead the default Long Sequence Number Fragment Format should be used for all traffic sent by the remote peer to the local peer. This setting has no effect on the negotation of Short Sequence Number Header Format for the traffic flowing in the opposite direction (from the local peer to the remote peer). The use of Short Sequence Number Fragment Format on that traffic will be determined by whatever the remote peer proposes. Changing this object will have effect when the link is next restarted (either by toggling ifAdminStatus for this interface down and then up again, or by rebooting the entire system). After the link comes up, the status variable mpBundleStatusLocalMRRU will reflect the actual MRRU negotiated with the peer during LCP negotiation.')
mpBundleConfigSmallPktMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(12)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpBundleConfigSmallPktMaxSize.setReference('(Not explicitly defined by RFC1990)')
if mibBuilder.loadTexts: mpBundleConfigSmallPktMaxSize.setStatus('current')
if mibBuilder.loadTexts: mpBundleConfigSmallPktMaxSize.setDescription('The maximum size in bytes of a Small PPP packet. Use of this parameter is no longer recommended. To control the MP fragmentation threshold see mpBundleConfigMediumPktMaxSize. Small PPP packets are defined to be those which will be encapsulated in a single Multilink Protocol Fragment and always sent on the first link in the Bundle. Note that this parameter only applies to outgoing PPP packets sent by this system. Reassembly of incoming packets is unaffected by this value. Note that the default value of 12 bytes effectively means that no packets are subject to this rule.')
mpBundleConfigMediumPktMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpBundleConfigMediumPktMaxSize.setReference('(Not explicitly defined by RFC1990)')
if mibBuilder.loadTexts: mpBundleConfigMediumPktMaxSize.setStatus('current')
if mibBuilder.loadTexts: mpBundleConfigMediumPktMaxSize.setDescription('The maximum size in bytes of a Medium PPP packet. This value specifies the threshold at which Multilink fragmentation is applied to transmitted packets, i.e. packets smaller than this size will be encapsulated in a single Multilink Protocol fragment and sent on a single link, packets larger than this size will be fragmented over all links in the bundle. Medium PPP packets are defined to be those which will be encapsulated in a single Multilink Protocol Fragment and sent on each link in the Bundle in a round-robin fashion. Packets larger than this threshold are considered Large PPP packets. Large PPP packets will be fragmented into multiple Multilink Protocol Fragments and sent across all links in the bundle. Setting this value to its maximum (65535) will prevent fragmentation at the MP layer of outgoing PPP packets, i.e. it will cause all outgoing PPP packets to be considered either Small or Medium sized PPP packets. Note that this parameter only applies to outgoing PPP packets sent by this system. Reassembly of incoming packets is unaffected by this value.')
mpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 1))
mpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 2))
mpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 1, 1)).setObjects(("XEDIA-PPP-MP-MIB", "mpAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpCompliance = mpCompliance.setStatus('current')
if mibBuilder.loadTexts: mpCompliance.setDescription('The compliance statement for all agents that support this MIB. A compliant agent implements all objects defined in this MIB.')
mpAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 2, 1)).setObjects(("XEDIA-PPP-MP-MIB", "mpBundleStatusPacketTooLongs"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusLocalMRRU"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusRemoteMRRU"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusLocalEndptDiscr"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusRemoteEndptDiscr"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusRcvShortSeq"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusXmtShortSeq"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusSmallPktMaxSize"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusMediumPktMaxSize"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusSingleFragsRcvd"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusReasmReqds"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusReasmFails"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusReasmOks"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusRcvdFragsDiscarded"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusDropTooManyFrags"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusSingleFragsSent"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusFragCreates"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusFragFails"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusFragOks"), ("XEDIA-PPP-MP-MIB", "mpBundleStatusRcvdFragsBuffered"), ("XEDIA-PPP-MP-MIB", "mpBundleConfigLocalMRRU"), ("XEDIA-PPP-MP-MIB", "mpBundleConfigLocalEndptDiscr"), ("XEDIA-PPP-MP-MIB", "mpBundleConfigRcvShortSeq"), ("XEDIA-PPP-MP-MIB", "mpBundleConfigSmallPktMaxSize"), ("XEDIA-PPP-MP-MIB", "mpBundleConfigMediumPktMaxSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpAllGroup = mpAllGroup.setStatus('current')
if mibBuilder.loadTexts: mpAllGroup.setDescription('The set of all accessible objects in this MIB.')
mibBuilder.exportSymbols("XEDIA-PPP-MP-MIB", mpBundleStatusRcvdFragsDiscarded=mpBundleStatusRcvdFragsDiscarded, mpBundleConfigTable=mpBundleConfigTable, xediaPppMpConformance=xediaPppMpConformance, mpCompliances=mpCompliances, mpBundleStatusEntry=mpBundleStatusEntry, Unsigned32=Unsigned32, mpAllGroup=mpAllGroup, mpBundleStatusSingleFragsRcvd=mpBundleStatusSingleFragsRcvd, mpBundleStatusPacketTooLongs=mpBundleStatusPacketTooLongs, mpBundleStatusLocalEndptDiscr=mpBundleStatusLocalEndptDiscr, mpBundleConfigLocalEndptDiscr=mpBundleConfigLocalEndptDiscr, mpBundleStatusRcvShortSeq=mpBundleStatusRcvShortSeq, mpBundleConfigRcvShortSeq=mpBundleConfigRcvShortSeq, mpBundleStatusFragOks=mpBundleStatusFragOks, mpBundleConfigLocalMRRU=mpBundleConfigLocalMRRU, mpBundleConfigEntry=mpBundleConfigEntry, mpBundleStatusXmtShortSeq=mpBundleStatusXmtShortSeq, mpBundleStatusSingleFragsSent=mpBundleStatusSingleFragsSent, mpBundleStatusReasmOks=mpBundleStatusReasmOks, PYSNMP_MODULE_ID=xediaPppMpMIB, mpBundleStatusRemoteEndptDiscr=mpBundleStatusRemoteEndptDiscr, mpBundleStatusDropTooManyFrags=mpBundleStatusDropTooManyFrags, mpBundleStatusLocalMRRU=mpBundleStatusLocalMRRU, mpBundleStatusReasmReqds=mpBundleStatusReasmReqds, mpCompliance=mpCompliance, mpBundleStatusTable=mpBundleStatusTable, mpBundleConfigSmallPktMaxSize=mpBundleConfigSmallPktMaxSize, mpBundleStatusFragCreates=mpBundleStatusFragCreates, mpBundleConfigMediumPktMaxSize=mpBundleConfigMediumPktMaxSize, mpBundleStatusMediumPktMaxSize=mpBundleStatusMediumPktMaxSize, mpBundleStatusSmallPktMaxSize=mpBundleStatusSmallPktMaxSize, mpBundleStatusRcvdFragsBuffered=mpBundleStatusRcvdFragsBuffered, mpBundleStatusFragFails=mpBundleStatusFragFails, xediaPppMpObjects=xediaPppMpObjects, mpBundle=mpBundle, mpGroups=mpGroups, mpBundleStatusReasmFails=mpBundleStatusReasmFails, xediaPppMpMIB=xediaPppMpMIB, mpBundleStatusRemoteMRRU=mpBundleStatusRemoteMRRU)