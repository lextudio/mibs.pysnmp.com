#
# PySNMP MIB module CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:05:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
cldcClientMacAddress, = mibBuilder.importSymbols("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, TimeTicks, Gauge32, ObjectIdentity, iso, Counter64, ModuleIdentity, Bits, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Gauge32", "ObjectIdentity", "iso", "Counter64", "ModuleIdentity", "Bits", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Integer32")
MacAddress, DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
ciscoLwappDot11ClientRmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 767))
ciscoLwappDot11ClientRmMIB.setRevisions(('2010-12-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappDot11ClientRmMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappDot11ClientRmMIB.setLastUpdated('201012130000Z')
if mibBuilder.loadTexts: ciscoLwappDot11ClientRmMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoLwappDot11ClientRmMIB.setContactInfo('Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappDot11ClientRmMIB.setDescription("This MIB is intended to be implemented on all those devices operating as Central controllers, that terminate the Light Weight Access Point Protocol tunnel from Cisco Light-weight LWAPP Access Points. The relationship between CC and the LWAPP APs can be depicted as follows: +......+ +......+ +......+ +......+ + + + + + + + + + CC + + CC + + CC + + CC + + + + + + + + + +......+ +......+ +......+ +......+ .. . . . .. . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + AP + + AP + + AP + + AP + + AP + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ . . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + MN + + MN + + MN + + MN + + MN + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ The LWAPP tunnel exists between the controller and the APs. The MNs communicate with the APs through the protocol defined by the 802.11 standard. LWAPP APs, upon bootup, discover and join one of the controllers and the controller pushes the configuration, that includes the WLAN parameters, to the LWAPP APs. The APs then encapsulate all the 802.11 frames from wireless clients inside LWAPP frames and forward the LWAPP frames to the controller. GLOSSARY Access Point ( AP ) An entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. LWAPP APs encapsulate all the 802.11 frames in LWAPP frames and sends them to the controller to which it is logically connected. Central Controller ( CC ) The central entity that terminates the LWAPP protocol tunnel from the LWAPP APs. Throughout this MIB, this entity also referred to as 'controller'. Cisco Compatible eXtensions (CCX) Wireless LAN Access Points (APs) manufactured by Cisco Systems have features and capabilities beyond those in related standards (e.g., IEEE 802.11 suite of standards, Wi-Fi recommendations by WECA, 802.1X security suite, etc). A number of features provide higher performance. For example, Cisco AP transmits a specific Information Element, which the clients adapt to for enhanced performance. Similarly, a number of features are implemented by means of proprietary Information Elements, which Cisco clients use in specific ways to carry out tasks above and beyond the standard. Other examples of feature categories are roaming and power saving. Light Weight Access Point Protocol ( LWAPP ) This is a generic protocol that defines the communication between the Access Points and the Central Controller. Mobile Node ( MN ) A roaming 802.11 wireless device in a wireless network associated with an access point. The terms 'Mobile node' and 'client' are used interchangeably. Radio Management (RM) This term refers to managing the 802.11 radio environment to provide the best quality service to to the 802.11 wireless clients. Service Set Identifier ( SSID ) SSID is a unique identifier that APs and clients use to identify with each other. SSID is a simple means of access control and is not for security. The SSID can be any alphanumeric entry up to 32 characters. REFERENCE [1] Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications [2] Draft-obara-capwap-lwapp-00.txt, IETF Light Weight Access Point Protocol")
ciscoLwapDot11ClientRmMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 767, 0))
ciscoLwappDot11ClientRmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 767, 1))
ciscoLwappDot11ClientRmMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 767, 2))
cldccrRmReq = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1))
cldccrRmResp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2))
cldccrRmReqStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3))
class CiscoLwappCcxRmReqStatus(TextualConvention, Integer32):
    description = 'This attribute is used to initiate/track a request to the ccxv4 client.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inProgress", 1), ("success", 2), ("failure", 3))

cldccrRmReqTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1), )
if mibBuilder.loadTexts: cldccrRmReqTable.setStatus('current')
if mibBuilder.loadTexts: cldccrRmReqTable.setDescription('This table is used to configure the radio measurement request parameters to be sent to the ccxv4 clients.')
cldccrRmReqEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"))
if mibBuilder.loadTexts: cldccrRmReqEntry.setStatus('current')
if mibBuilder.loadTexts: cldccrRmReqEntry.setDescription('Each entry represents a conceptual row in this table. An entry corresponds to a client for which a certain type of report is being fetched.')
cldccrRmReqReportType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("channelLoadReport", 0), ("histogramReport", 1), ("beaconReport", 2), ("frameReport", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldccrRmReqReportType.setStatus('current')
if mibBuilder.loadTexts: cldccrRmReqReportType.setDescription('This object is set to list of radio measurement requests the reports of which will be sent by the ccxv4 client to the controller.')
cldccrRmInitiateReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldccrRmInitiateReq.setStatus('current')
if mibBuilder.loadTexts: cldccrRmInitiateReq.setDescription('This object is used to send the rm req message to the client.')
cldccrRmReqNumIterations = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 250))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldccrRmReqNumIterations.setStatus('current')
if mibBuilder.loadTexts: cldccrRmReqNumIterations.setDescription('This attribute is used to set the number of times the rm request will be sent to the client.')
cldccrRmReqMeasDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 32400))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldccrRmReqMeasDuration.setStatus('current')
if mibBuilder.loadTexts: cldccrRmReqMeasDuration.setDescription('The time interval between two RM Reqs in seconds.')
cldccrRmReqRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cldccrRmReqRowStatus.setStatus('current')
if mibBuilder.loadTexts: cldccrRmReqRowStatus.setDescription('This is the status column for this row and is used to create and delete specific instances of rows in this table.')
cldccrRmHistRepTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1), )
if mibBuilder.loadTexts: cldccrRmHistRepTable.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepTable.setDescription('This table contains the noise histogram reports of the clients which were queried for the same.')
cldccrRmHistRepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"), (0, "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistIndex"))
if mibBuilder.loadTexts: cldccrRmHistRepEntry.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepEntry.setDescription('There is an entry in the table where entry is identified by the client Mac address.')
cldccrRmHistIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 28)))
if mibBuilder.loadTexts: cldccrRmHistIndex.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistIndex.setDescription('Index which will be the channel number in most cases.')
cldccrRmHistRepChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistRepChannelNumber.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepChannelNumber.setDescription('Channel number indicates the channel number to which the noise histogram Report applies.')
cldccrRmHistRepTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistRepTimeStamp.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepTimeStamp.setDescription('Timestamp of the histogram report.')
cldccrRmHistRepRPIDensity0 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity0.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity0.setDescription('This Field stores the RPI density in power range power << -87 db.')
cldccrRmHistRepRPIDensity1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity1.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity1.setDescription('This Field stores the RPI density in power range -87 < power << -82.')
cldccrRmHistRepRPIDensity2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity2.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity2.setDescription('This Field stores the RPI density in power range -82 < power << -77.')
cldccrRmHistRepRPIDensity3 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity3.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity3.setDescription('This Field stores the RPI density in power range -77 < power << -72.')
cldccrRmHistRepRPIDensity4 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity4.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity4.setDescription('This Field stores the RPI density in power range -72< Power << -67.')
cldccrRmHistRepRPIDensity5 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity5.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity5.setDescription('This Field stores the RPI density in power range -67< Power << -62.')
cldccrRmHistRepRPIDensity6 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity6.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity6.setDescription('This Field stores the RPI density in power range -62< Power<< -57.')
cldccrRmHistRepRPIDensity7 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity7.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistRepRPIDensity7.setDescription('This Field stores the RPI density in power range -57< Power<< -52.')
cldccrRmBeaconRepTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2), )
if mibBuilder.loadTexts: cldccrRmBeaconRepTable.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRepTable.setDescription('This table contains the beacon reports of the clients which were queried for the same.')
cldccrRmBeaconRepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"), (0, "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconIndex"))
if mibBuilder.loadTexts: cldccrRmBeaconRepEntry.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRepEntry.setDescription('There is an entry in the table where entry is identified by the client Mac address.')
cldccrRmBeaconIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 28)))
if mibBuilder.loadTexts: cldccrRmBeaconIndex.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconIndex.setDescription('Index which will be the channel number in most cases.')
cldccrRmBeaconRptChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmBeaconRptChannelNumber.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRptChannelNumber.setDescription('Channel number indicates the channel number to which the noise beacon report applies.')
cldccrRmBeaconRptTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmBeaconRptTimeStamp.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRptTimeStamp.setDescription('Timestamp of the beacon report.')
cldccrRmBeaconRptPhyType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("fh", 1), ("dss", 2), ("unused", 3), ("ofdm", 4), ("highDataRateDss", 5), ("erp", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmBeaconRptPhyType.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRptPhyType.setDescription('Phy type indicates the physical medium used.')
cldccrRmBeaconRptReceivedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmBeaconRptReceivedPower.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRptReceivedPower.setDescription('This field indicates the received strength of the beacon or probe response frame in dBm.')
cldccrRmBeaconRptBSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmBeaconRptBSSID.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRptBSSID.setDescription('This field contains the 6-byte BSSID of the STA that transmitted the beacon or probe response frame.')
cldccrRmBeaconRptParentTsf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmBeaconRptParentTsf.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRptParentTsf.setDescription('This field is used to store the parent TSF Parent TSF contains the lower 4 bytes of the serving APs. TSF value at the time the measuring STA received the beacon or probe response frame.')
cldccrRmBeaconRptTargetTsf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmBeaconRptTargetTsf.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRptTargetTsf.setDescription('This field is used to store the Target TSF. Target TSF contains the 8-byte TSF value contained in the beacon or probe response received by the measuring STA.')
cldccrRmBeaconRptInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmBeaconRptInterval.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRptInterval.setDescription('This field is equal to the 2-byte Beacon Interval field in the received beacon or probe response.')
cldccrRmBeaconRptCapInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmBeaconRptCapInfo.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconRptCapInfo.setDescription('This attribute represents the capability info.')
cldccRmChannelLoadReportTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3), )
if mibBuilder.loadTexts: cldccRmChannelLoadReportTable.setStatus('current')
if mibBuilder.loadTexts: cldccRmChannelLoadReportTable.setDescription('This table contains the channel load reports of the clients which were queried for the same.')
cldccRmChannelLoadReportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"), (0, "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmChannelLoadReportIndex"))
if mibBuilder.loadTexts: cldccRmChannelLoadReportEntry.setStatus('current')
if mibBuilder.loadTexts: cldccRmChannelLoadReportEntry.setDescription('There is an entry in the table where entry is identified by the client Mac address.')
cldccRmChannelLoadReportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cldccRmChannelLoadReportIndex.setStatus('current')
if mibBuilder.loadTexts: cldccRmChannelLoadReportIndex.setDescription('This indicates the index of the report table.')
cldccRmChannelLoadReportChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccRmChannelLoadReportChannelNumber.setStatus('current')
if mibBuilder.loadTexts: cldccRmChannelLoadReportChannelNumber.setDescription('Channel Number indicates the channel number to which the Channel Load Report applies.')
cldccRmChannelLoadReportTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccRmChannelLoadReportTimeStamp.setStatus('current')
if mibBuilder.loadTexts: cldccRmChannelLoadReportTimeStamp.setDescription('Timestamp of the channel load report.')
cldccRmChannelLoadReportCCABusyFraction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccRmChannelLoadReportCCABusyFraction.setStatus('current')
if mibBuilder.loadTexts: cldccRmChannelLoadReportCCABusyFraction.setDescription('CCA Busy Fraction shall contain the fractional duration over which CCA indicated the channel was busy during the measurement duration.')
cldccRmFrameReportTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4), )
if mibBuilder.loadTexts: cldccRmFrameReportTable.setStatus('current')
if mibBuilder.loadTexts: cldccRmFrameReportTable.setDescription('This table contains the frame reports of the clients which were queried for the same.')
cldccRmFrameReportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"), (0, "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportElemIndex"), (0, "CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportSubElemIndex"))
if mibBuilder.loadTexts: cldccRmFrameReportEntry.setStatus('current')
if mibBuilder.loadTexts: cldccRmFrameReportEntry.setDescription('There is an entry in the table where entry is identified by the client Mac address.')
cldccRmFrameReportElemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cldccRmFrameReportElemIndex.setStatus('current')
if mibBuilder.loadTexts: cldccRmFrameReportElemIndex.setDescription('This attribute represents the index of element index of frame report.')
cldccRmFrameReportSubElemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cldccRmFrameReportSubElemIndex.setStatus('current')
if mibBuilder.loadTexts: cldccRmFrameReportSubElemIndex.setDescription('This attribute represents the index of the sub element in a frame report.')
cldccRmFrameReportChanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccRmFrameReportChanNumber.setStatus('current')
if mibBuilder.loadTexts: cldccRmFrameReportChanNumber.setDescription('This attribute represents the channel number of frame report.')
cldccRmFrameReportTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccRmFrameReportTimeStamp.setStatus('current')
if mibBuilder.loadTexts: cldccRmFrameReportTimeStamp.setDescription('Timestamp of the frame report.')
cldccRmFrameReportTransmitAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccRmFrameReportTransmitAddr.setStatus('current')
if mibBuilder.loadTexts: cldccRmFrameReportTransmitAddr.setDescription('This represents the transmitted address.')
cldccRmFrameReportBssid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccRmFrameReportBssid.setStatus('current')
if mibBuilder.loadTexts: cldccRmFrameReportBssid.setDescription('This represents the bssid.')
cldccRmFrameReportRecvSigPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccRmFrameReportRecvSigPower.setStatus('current')
if mibBuilder.loadTexts: cldccRmFrameReportRecvSigPower.setDescription('This field indicates the received strength of the beacon or probe response frame in dBm.')
cldccRmFrameReportFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 2, 4, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccRmFrameReportFrameCount.setStatus('current')
if mibBuilder.loadTexts: cldccRmFrameReportFrameCount.setDescription('This field indicates the received strength of the beacon or probe response frame in dBm.')
cldccrRmReqStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1), )
if mibBuilder.loadTexts: cldccrRmReqStatusTable.setStatus('current')
if mibBuilder.loadTexts: cldccrRmReqStatusTable.setDescription('This table is used to get the status for each of the reports.')
cldccrRmReqStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"))
if mibBuilder.loadTexts: cldccrRmReqStatusEntry.setStatus('current')
if mibBuilder.loadTexts: cldccrRmReqStatusEntry.setDescription('There is an entry in the table where entry is identified by the client Mac address.')
cldccrRmFrameReqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1, 1, 1), CiscoLwappCcxRmReqStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmFrameReqStatus.setStatus('current')
if mibBuilder.loadTexts: cldccrRmFrameReqStatus.setDescription('This attribute is used to initiate/track a frame report request to the ccxv4 client.')
cldccrRmHistogramReqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1, 1, 2), CiscoLwappCcxRmReqStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmHistogramReqStatus.setStatus('current')
if mibBuilder.loadTexts: cldccrRmHistogramReqStatus.setDescription('This attribute is used to initiate/track a noise histogram request to the ccxv4 client.')
cldccrRmBeaconReqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1, 1, 3), CiscoLwappCcxRmReqStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmBeaconReqStatus.setStatus('current')
if mibBuilder.loadTexts: cldccrRmBeaconReqStatus.setDescription('This attribute is used to initiate/track a beacon request to the ccxv4 client.')
cldccrRmChanLoadReqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 767, 1, 3, 1, 1, 4), CiscoLwappCcxRmReqStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cldccrRmChanLoadReqStatus.setStatus('current')
if mibBuilder.loadTexts: cldccrRmChanLoadReqStatus.setDescription('This attribute is used to initiate/track a channel load request to the ccxv4 client.')
ciscoLwappDot11ClientRmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 767, 2, 1))
ciscoLwappDot11ClientRmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 767, 2, 2))
ciscoLwappDot11ClientRmMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 767, 2, 1, 1)).setObjects(("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "ciscoLwappDot11ClientRmConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientRmMibCompliance = ciscoLwappDot11ClientRmMibCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappDot11ClientRmMibCompliance.setDescription('The compliance statement for the SNMP entities that implement the ciscoLwappDot11ClientRmMIB module.')
ciscoLwappDot11ClientRmConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 767, 2, 2, 1)).setObjects(("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmReqReportType"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmInitiateReq"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmReqNumIterations"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmReqMeasDuration"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmReqRowStatus"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepChannelNumber"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepTimeStamp"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity0"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity1"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity2"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity3"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity4"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity5"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity6"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistRepRPIDensity7"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptChannelNumber"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptTimeStamp"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptPhyType"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptReceivedPower"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptBSSID"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptParentTsf"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptTargetTsf"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptInterval"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconRptCapInfo"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmChannelLoadReportChannelNumber"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmChannelLoadReportTimeStamp"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmChannelLoadReportCCABusyFraction"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportChanNumber"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportTimeStamp"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportTransmitAddr"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportBssid"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportRecvSigPower"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccRmFrameReportFrameCount"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmFrameReqStatus"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmHistogramReqStatus"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmBeaconReqStatus"), ("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", "cldccrRmChanLoadReqStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappDot11ClientRmConfigGroup = ciscoLwappDot11ClientRmConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappDot11ClientRmConfigGroup.setDescription('This collection of objects represent the reports of the CCX Clients.')
mibBuilder.exportSymbols("CISCO-LWAPP-DOT11-CLIENT-CCX-REPORTS-MIB", cldccRmChannelLoadReportEntry=cldccRmChannelLoadReportEntry, ciscoLwappDot11ClientRmMIB=ciscoLwappDot11ClientRmMIB, cldccrRmReqReportType=cldccrRmReqReportType, cldccrRmBeaconIndex=cldccrRmBeaconIndex, cldccrRmHistRepRPIDensity5=cldccrRmHistRepRPIDensity5, cldccrRmBeaconRptInterval=cldccrRmBeaconRptInterval, cldccRmFrameReportChanNumber=cldccRmFrameReportChanNumber, cldccrRmHistRepRPIDensity2=cldccrRmHistRepRPIDensity2, cldccRmFrameReportRecvSigPower=cldccRmFrameReportRecvSigPower, cldccRmChannelLoadReportCCABusyFraction=cldccRmChannelLoadReportCCABusyFraction, cldccrRmBeaconRepEntry=cldccrRmBeaconRepEntry, cldccRmFrameReportElemIndex=cldccRmFrameReportElemIndex, cldccrRmReqStatus=cldccrRmReqStatus, cldccrRmReqEntry=cldccrRmReqEntry, cldccrRmReqRowStatus=cldccrRmReqRowStatus, cldccrRmReqMeasDuration=cldccrRmReqMeasDuration, PYSNMP_MODULE_ID=ciscoLwappDot11ClientRmMIB, cldccrRmHistRepRPIDensity6=cldccrRmHistRepRPIDensity6, cldccrRmHistogramReqStatus=cldccrRmHistogramReqStatus, cldccrRmFrameReqStatus=cldccrRmFrameReqStatus, cldccrRmHistRepRPIDensity0=cldccrRmHistRepRPIDensity0, cldccrRmBeaconRepTable=cldccrRmBeaconRepTable, cldccrRmResp=cldccrRmResp, cldccRmChannelLoadReportTable=cldccRmChannelLoadReportTable, ciscoLwappDot11ClientRmMIBConform=ciscoLwappDot11ClientRmMIBConform, cldccRmFrameReportSubElemIndex=cldccRmFrameReportSubElemIndex, cldccrRmReqStatusTable=cldccrRmReqStatusTable, cldccrRmReq=cldccrRmReq, cldccrRmInitiateReq=cldccrRmInitiateReq, cldccrRmBeaconRptBSSID=cldccrRmBeaconRptBSSID, cldccrRmBeaconRptCapInfo=cldccrRmBeaconRptCapInfo, ciscoLwappDot11ClientRmMIBObjects=ciscoLwappDot11ClientRmMIBObjects, cldccrRmHistRepTimeStamp=cldccrRmHistRepTimeStamp, cldccRmFrameReportEntry=cldccRmFrameReportEntry, cldccRmFrameReportTable=cldccRmFrameReportTable, cldccrRmBeaconRptReceivedPower=cldccrRmBeaconRptReceivedPower, ciscoLwappDot11ClientRmMIBCompliances=ciscoLwappDot11ClientRmMIBCompliances, CiscoLwappCcxRmReqStatus=CiscoLwappCcxRmReqStatus, ciscoLwappDot11ClientRmConfigGroup=ciscoLwappDot11ClientRmConfigGroup, cldccRmChannelLoadReportIndex=cldccRmChannelLoadReportIndex, cldccrRmBeaconRptPhyType=cldccrRmBeaconRptPhyType, cldccRmChannelLoadReportChannelNumber=cldccRmChannelLoadReportChannelNumber, cldccrRmReqStatusEntry=cldccrRmReqStatusEntry, cldccrRmBeaconRptTargetTsf=cldccrRmBeaconRptTargetTsf, cldccrRmBeaconRptTimeStamp=cldccrRmBeaconRptTimeStamp, cldccrRmBeaconReqStatus=cldccrRmBeaconReqStatus, cldccrRmHistRepRPIDensity4=cldccrRmHistRepRPIDensity4, ciscoLwappDot11ClientRmMIBGroups=ciscoLwappDot11ClientRmMIBGroups, cldccrRmReqNumIterations=cldccrRmReqNumIterations, cldccrRmHistRepRPIDensity3=cldccrRmHistRepRPIDensity3, cldccRmFrameReportTimeStamp=cldccRmFrameReportTimeStamp, ciscoLwapDot11ClientRmMIBNotifs=ciscoLwapDot11ClientRmMIBNotifs, cldccrRmBeaconRptChannelNumber=cldccrRmBeaconRptChannelNumber, cldccrRmHistRepEntry=cldccrRmHistRepEntry, cldccRmFrameReportTransmitAddr=cldccRmFrameReportTransmitAddr, cldccrRmBeaconRptParentTsf=cldccrRmBeaconRptParentTsf, cldccrRmHistRepChannelNumber=cldccrRmHistRepChannelNumber, cldccrRmReqTable=cldccrRmReqTable, ciscoLwappDot11ClientRmMibCompliance=ciscoLwappDot11ClientRmMibCompliance, cldccRmFrameReportBssid=cldccRmFrameReportBssid, cldccrRmHistRepRPIDensity7=cldccrRmHistRepRPIDensity7, cldccrRmHistRepRPIDensity1=cldccrRmHistRepRPIDensity1, cldccrRmHistIndex=cldccrRmHistIndex, cldccrRmChanLoadReqStatus=cldccrRmChanLoadReqStatus, cldccRmChannelLoadReportTimeStamp=cldccRmChannelLoadReportTimeStamp, cldccrRmHistRepTable=cldccrRmHistRepTable, cldccRmFrameReportFrameCount=cldccRmFrameReportFrameCount)