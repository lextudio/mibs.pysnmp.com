# SNMP MIB module (FE-FIREEYE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FE-FIREEYE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:48 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fireeyeMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 20, 1)
)
fireeyeMibModule.setRevisions(
        ("2014-04-07 11:20",
         "2014-04-02 10:40",
         "2014-03-19 10:40",
         "2014-03-10 10:00",
         "2014-01-21 21:00",
         "2011-09-08 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fireeye_ObjectIdentity = ObjectIdentity
fireeye = _Fireeye_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597)
)
_Variables_ObjectIdentity = ObjectIdentity
variables = _Variables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 1)
)
_Lms_ObjectIdentity = ObjectIdentity
lms = _Lms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1)
)
_LmsVersion_Type = OctetString
_LmsVersion_Object = MibScalar
lmsVersion = _LmsVersion_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 1),
    _LmsVersion_Type()
)
lmsVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lmsVersion.setStatus("current")
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1)
)
eventEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "eventIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
_EventIndex_Type = Unsigned32
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventIndex.setStatus("current")
_EventId_Type = Unsigned32
_EventId_Object = MibTableColumn
eventId = _EventId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 2),
    _EventId_Type()
)
eventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventId.setStatus("current")
_EventType_Type = OctetString
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 3),
    _EventType_Type()
)
eventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_EventDate_Type = OctetString
_EventDate_Object = MibTableColumn
eventDate = _EventDate_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 4),
    _EventDate_Type()
)
eventDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDate.setStatus("current")
_EventTime_Type = OctetString
_EventTime_Object = MibTableColumn
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 5),
    _EventTime_Type()
)
eventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_EventTraceId_Type = Counter64
_EventTraceId_Object = MibTableColumn
eventTraceId = _EventTraceId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 6),
    _EventTraceId_Type()
)
eventTraceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTraceId.setStatus("current")
_EventSrcIp_Type = IpAddress
_EventSrcIp_Object = MibTableColumn
eventSrcIp = _EventSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 7),
    _EventSrcIp_Type()
)
eventSrcIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcIp.setStatus("current")
_EventDstIp_Type = IpAddress
_EventDstIp_Object = MibTableColumn
eventDstIp = _EventDstIp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 8),
    _EventDstIp_Type()
)
eventDstIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDstIp.setStatus("current")
_EventSrcMac_Type = OctetString
_EventSrcMac_Object = MibTableColumn
eventSrcMac = _EventSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 9),
    _EventSrcMac_Type()
)
eventSrcMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcMac.setStatus("current")
_EventDstMac_Type = OctetString
_EventDstMac_Object = MibTableColumn
eventDstMac = _EventDstMac_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 10),
    _EventDstMac_Type()
)
eventDstMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDstMac.setStatus("current")
_EventDstPort_Type = Integer32
_EventDstPort_Object = MibTableColumn
eventDstPort = _EventDstPort_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 11),
    _EventDstPort_Type()
)
eventDstPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDstPort.setStatus("current")
_EventVlan_Type = Integer32
_EventVlan_Object = MibTableColumn
eventVlan = _EventVlan_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 12),
    _EventVlan_Type()
)
eventVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventVlan.setStatus("current")
_EventProtocol_Type = OctetString
_EventProtocol_Object = MibTableColumn
eventProtocol = _EventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 13),
    _EventProtocol_Type()
)
eventProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventProtocol.setStatus("current")
_EventProfileId_Type = Unsigned32
_EventProfileId_Object = MibTableColumn
eventProfileId = _EventProfileId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 14),
    _EventProfileId_Type()
)
eventProfileId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventProfileId.setStatus("current")
_EventOsInfo_Type = OctetString
_EventOsInfo_Object = MibTableColumn
eventOsInfo = _EventOsInfo_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 15),
    _EventOsInfo_Type()
)
eventOsInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventOsInfo.setStatus("current")
_EventService_Type = OctetString
_EventService_Object = MibTableColumn
eventService = _EventService_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 16),
    _EventService_Type()
)
eventService.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventService.setStatus("current")
_EventAttackType_Type = OctetString
_EventAttackType_Object = MibTableColumn
eventAttackType = _EventAttackType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 17),
    _EventAttackType_Type()
)
eventAttackType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAttackType.setStatus("current")
_EventSignatureName_Type = OctetString
_EventSignatureName_Object = MibTableColumn
eventSignatureName = _EventSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 18),
    _EventSignatureName_Type()
)
eventSignatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSignatureName.setStatus("current")
_EventSignatureType_Type = OctetString
_EventSignatureType_Object = MibTableColumn
eventSignatureType = _EventSignatureType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 19),
    _EventSignatureType_Type()
)
eventSignatureType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSignatureType.setStatus("current")
_EventSrcHost_Type = OctetString
_EventSrcHost_Object = MibTableColumn
eventSrcHost = _EventSrcHost_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 20),
    _EventSrcHost_Type()
)
eventSrcHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcHost.setStatus("current")
_EventCncNo_Type = Unsigned32
_EventCncNo_Object = MibTableColumn
eventCncNo = _EventCncNo_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 21),
    _EventCncNo_Type()
)
eventCncNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventCncNo.setStatus("current")
_AlertSignatureId_Type = Unsigned32
_AlertSignatureId_Object = MibTableColumn
alertSignatureId = _AlertSignatureId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 22),
    _AlertSignatureId_Type()
)
alertSignatureId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSignatureId.setStatus("current")
_AlertCncHost_Type = OctetString
_AlertCncHost_Object = MibTableColumn
alertCncHost = _AlertCncHost_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 23),
    _AlertCncHost_Type()
)
alertCncHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertCncHost.setStatus("current")
_AlertCncPort_Type = Integer32
_AlertCncPort_Object = MibTableColumn
alertCncPort = _AlertCncPort_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 24),
    _AlertCncPort_Type()
)
alertCncPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertCncPort.setStatus("current")
_AlertChecksum_Type = OctetString
_AlertChecksum_Object = MibTableColumn
alertChecksum = _AlertChecksum_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 25),
    _AlertChecksum_Type()
)
alertChecksum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertChecksum.setStatus("current")
_AlertAnalysisType_Type = OctetString
_AlertAnalysisType_Object = MibTableColumn
alertAnalysisType = _AlertAnalysisType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 26),
    _AlertAnalysisType_Type()
)
alertAnalysisType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertAnalysisType.setStatus("current")
_AlertProfile_Type = OctetString
_AlertProfile_Object = MibTableColumn
alertProfile = _AlertProfile_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 27),
    _AlertProfile_Type()
)
alertProfile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertProfile.setStatus("current")
_AlertAction_Type = OctetString
_AlertAction_Object = MibTableColumn
alertAction = _AlertAction_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 28),
    _AlertAction_Type()
)
alertAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertAction.setStatus("current")
_AlertInterface_Type = OctetString
_AlertInterface_Object = MibTableColumn
alertInterface = _AlertInterface_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 29),
    _AlertInterface_Type()
)
alertInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertInterface.setStatus("current")
_AlertSensorIp_Type = IpAddress
_AlertSensorIp_Object = MibTableColumn
alertSensorIp = _AlertSensorIp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 30),
    _AlertSensorIp_Type()
)
alertSensorIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSensorIp.setStatus("current")
_AlertSensorHost_Type = OctetString
_AlertSensorHost_Object = MibTableColumn
alertSensorHost = _AlertSensorHost_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 31),
    _AlertSensorHost_Type()
)
alertSensorHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSensorHost.setStatus("current")
_AlertSensorProduct_Type = OctetString
_AlertSensorProduct_Object = MibTableColumn
alertSensorProduct = _AlertSensorProduct_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 32),
    _AlertSensorProduct_Type()
)
alertSensorProduct.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSensorProduct.setStatus("current")
_AlertSensorRelease_Type = OctetString
_AlertSensorRelease_Object = MibTableColumn
alertSensorRelease = _AlertSensorRelease_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 33),
    _AlertSensorRelease_Type()
)
alertSensorRelease.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertSensorRelease.setStatus("current")
_AlertUrl_Type = OctetString
_AlertUrl_Object = MibTableColumn
alertUrl = _AlertUrl_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 34),
    _AlertUrl_Type()
)
alertUrl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alertUrl.setStatus("current")
_EventSrcAddrType_Type = InetAddressType
_EventSrcAddrType_Object = MibTableColumn
eventSrcAddrType = _EventSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 35),
    _EventSrcAddrType_Type()
)
eventSrcAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcAddrType.setStatus("current")
_EventSrcAddr_Type = InetAddress
_EventSrcAddr_Object = MibTableColumn
eventSrcAddr = _EventSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 36),
    _EventSrcAddr_Type()
)
eventSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcAddr.setStatus("current")
_EventDstAddrType_Type = InetAddressType
_EventDstAddrType_Object = MibTableColumn
eventDstAddrType = _EventDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 37),
    _EventDstAddrType_Type()
)
eventDstAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDstAddrType.setStatus("current")
_EventDstAddr_Type = InetAddress
_EventDstAddr_Object = MibTableColumn
eventDstAddr = _EventDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 38),
    _EventDstAddr_Type()
)
eventDstAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDstAddr.setStatus("current")
_EventSensorAddrType_Type = InetAddressType
_EventSensorAddrType_Object = MibTableColumn
eventSensorAddrType = _EventSensorAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 39),
    _EventSensorAddrType_Type()
)
eventSensorAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSensorAddrType.setStatus("current")
_EventSensorAddr_Type = InetAddress
_EventSensorAddr_Object = MibTableColumn
eventSensorAddr = _EventSensorAddr_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 40),
    _EventSensorAddr_Type()
)
eventSensorAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSensorAddr.setStatus("current")
_EventSrcPort_Type = Integer32
_EventSrcPort_Object = MibTableColumn
eventSrcPort = _EventSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 41),
    _EventSrcPort_Type()
)
eventSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventSrcPort.setStatus("current")
_EventDateTime_Type = OctetString
_EventDateTime_Object = MibTableColumn
eventDateTime = _EventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 42),
    _EventDateTime_Type()
)
eventDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventDateTime.setStatus("current")
_IpsSignatureId_Type = Unsigned32
_IpsSignatureId_Object = MibTableColumn
ipsSignatureId = _IpsSignatureId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 43),
    _IpsSignatureId_Type()
)
ipsSignatureId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsSignatureId.setStatus("current")
_IpsSignatureRevision_Type = Unsigned32
_IpsSignatureRevision_Object = MibTableColumn
ipsSignatureRevision = _IpsSignatureRevision_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 44),
    _IpsSignatureRevision_Type()
)
ipsSignatureRevision.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsSignatureRevision.setStatus("current")
_IpsMatchCount_Type = Gauge32
_IpsMatchCount_Object = MibTableColumn
ipsMatchCount = _IpsMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 45),
    _IpsMatchCount_Type()
)
ipsMatchCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsMatchCount.setStatus("current")
_IpsSeverity_Type = OctetString
_IpsSeverity_Object = MibTableColumn
ipsSeverity = _IpsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 46),
    _IpsSeverity_Type()
)
ipsSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsSeverity.setStatus("current")
_IpsSignatureName_Type = OctetString
_IpsSignatureName_Object = MibTableColumn
ipsSignatureName = _IpsSignatureName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 47),
    _IpsSignatureName_Type()
)
ipsSignatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsSignatureName.setStatus("current")
_IpsReferenceId_Type = OctetString
_IpsReferenceId_Object = MibTableColumn
ipsReferenceId = _IpsReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 48),
    _IpsReferenceId_Type()
)
ipsReferenceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsReferenceId.setStatus("current")
_IpsBlockMode_Type = OctetString
_IpsBlockMode_Object = MibTableColumn
ipsBlockMode = _IpsBlockMode_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 49),
    _IpsBlockMode_Type()
)
ipsBlockMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsBlockMode.setStatus("current")
_IpsAttackTarget_Type = OctetString
_IpsAttackTarget_Object = MibTableColumn
ipsAttackTarget = _IpsAttackTarget_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 2, 1, 50),
    _IpsAttackTarget_Type()
)
ipsAttackTarget.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipsAttackTarget.setStatus("current")
_EventCount_Type = Unsigned32
_EventCount_Object = MibScalar
eventCount = _EventCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 1, 1, 3),
    _EventCount_Type()
)
eventCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventCount.setStatus("current")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 3)
)
_NotificationPrefix_ObjectIdentity = ObjectIdentity
notificationPrefix = _NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0)
)
_FeCommon_ObjectIdentity = ObjectIdentity
feCommon = _FeCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11)
)
_FeSystem_ObjectIdentity = ObjectIdentity
feSystem = _FeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1)
)
_FeSystemTraps_ObjectIdentity = ObjectIdentity
feSystemTraps = _FeSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0)
)
_FeSystemInfo_ObjectIdentity = ObjectIdentity
feSystemInfo = _FeSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1)
)
_FeSystemStatus_Type = OctetString
_FeSystemStatus_Object = MibScalar
feSystemStatus = _FeSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 1),
    _FeSystemStatus_Type()
)
feSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSystemStatus.setStatus("current")
_FeHardwareModel_Type = OctetString
_FeHardwareModel_Object = MibScalar
feHardwareModel = _FeHardwareModel_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 2),
    _FeHardwareModel_Type()
)
feHardwareModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feHardwareModel.setStatus("current")
_FeSerialNumber_Type = OctetString
_FeSerialNumber_Object = MibScalar
feSerialNumber = _FeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 3),
    _FeSerialNumber_Type()
)
feSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSerialNumber.setStatus("current")
_FeTemperatureValue_Type = Integer32
_FeTemperatureValue_Object = MibScalar
feTemperatureValue = _FeTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 4),
    _FeTemperatureValue_Type()
)
feTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTemperatureValue.setStatus("current")
_FeTemperatureStatus_Type = OctetString
_FeTemperatureStatus_Object = MibScalar
feTemperatureStatus = _FeTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 5),
    _FeTemperatureStatus_Type()
)
feTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTemperatureStatus.setStatus("current")
_FeTemperatureIsHealthy_Type = TruthValue
_FeTemperatureIsHealthy_Object = MibScalar
feTemperatureIsHealthy = _FeTemperatureIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 6),
    _FeTemperatureIsHealthy_Type()
)
feTemperatureIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTemperatureIsHealthy.setStatus("current")
_FeIfLinkChangeIfname_Type = OctetString
_FeIfLinkChangeIfname_Object = MibScalar
feIfLinkChangeIfname = _FeIfLinkChangeIfname_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 7),
    _FeIfLinkChangeIfname_Type()
)
feIfLinkChangeIfname.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeIfname.setStatus("current")
_FeIfLinkChangeOldAdminUp_Type = TruthValue
_FeIfLinkChangeOldAdminUp_Object = MibScalar
feIfLinkChangeOldAdminUp = _FeIfLinkChangeOldAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 8),
    _FeIfLinkChangeOldAdminUp_Type()
)
feIfLinkChangeOldAdminUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeOldAdminUp.setStatus("current")
_FeIfLinkChangeNewAdminUp_Type = TruthValue
_FeIfLinkChangeNewAdminUp_Object = MibScalar
feIfLinkChangeNewAdminUp = _FeIfLinkChangeNewAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 9),
    _FeIfLinkChangeNewAdminUp_Type()
)
feIfLinkChangeNewAdminUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeNewAdminUp.setStatus("current")
_FeIfLinkChangeOldLinkUp_Type = TruthValue
_FeIfLinkChangeOldLinkUp_Object = MibScalar
feIfLinkChangeOldLinkUp = _FeIfLinkChangeOldLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 10),
    _FeIfLinkChangeOldLinkUp_Type()
)
feIfLinkChangeOldLinkUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeOldLinkUp.setStatus("current")
_FeIfLinkChangeNewLinkUp_Type = TruthValue
_FeIfLinkChangeNewLinkUp_Object = MibScalar
feIfLinkChangeNewLinkUp = _FeIfLinkChangeNewLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 11),
    _FeIfLinkChangeNewLinkUp_Type()
)
feIfLinkChangeNewLinkUp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeNewLinkUp.setStatus("current")
_FeIfLinkChangeOldSpeed_Type = Integer32
_FeIfLinkChangeOldSpeed_Object = MibScalar
feIfLinkChangeOldSpeed = _FeIfLinkChangeOldSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 12),
    _FeIfLinkChangeOldSpeed_Type()
)
feIfLinkChangeOldSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeOldSpeed.setStatus("current")
_FeIfLinkChangeNewSpeed_Type = Integer32
_FeIfLinkChangeNewSpeed_Object = MibScalar
feIfLinkChangeNewSpeed = _FeIfLinkChangeNewSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 13),
    _FeIfLinkChangeNewSpeed_Type()
)
feIfLinkChangeNewSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeNewSpeed.setStatus("current")
_FeIfLinkChangeOldDuplex_Type = Integer32
_FeIfLinkChangeOldDuplex_Object = MibScalar
feIfLinkChangeOldDuplex = _FeIfLinkChangeOldDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 14),
    _FeIfLinkChangeOldDuplex_Type()
)
feIfLinkChangeOldDuplex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeOldDuplex.setStatus("current")
_FeIfLinkChangeNewDuplex_Type = Integer32
_FeIfLinkChangeNewDuplex_Object = MibScalar
feIfLinkChangeNewDuplex = _FeIfLinkChangeNewDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 15),
    _FeIfLinkChangeNewDuplex_Type()
)
feIfLinkChangeNewDuplex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeNewDuplex.setStatus("current")
_FeIfLinkChangeOldAutoNeg_Type = TruthValue
_FeIfLinkChangeOldAutoNeg_Object = MibScalar
feIfLinkChangeOldAutoNeg = _FeIfLinkChangeOldAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 16),
    _FeIfLinkChangeOldAutoNeg_Type()
)
feIfLinkChangeOldAutoNeg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeOldAutoNeg.setStatus("current")
_FeIfLinkChangeNewAutoNeg_Type = TruthValue
_FeIfLinkChangeNewAutoNeg_Object = MibScalar
feIfLinkChangeNewAutoNeg = _FeIfLinkChangeNewAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 1, 17),
    _FeIfLinkChangeNewAutoNeg_Type()
)
feIfLinkChangeNewAutoNeg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feIfLinkChangeNewAutoNeg.setStatus("current")
_FeStorage_ObjectIdentity = ObjectIdentity
feStorage = _FeStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2)
)
_FeStorageTraps_ObjectIdentity = ObjectIdentity
feStorageTraps = _FeStorageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 0)
)
_FeStorageInfo_ObjectIdentity = ObjectIdentity
feStorageInfo = _FeStorageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1)
)
_FeRaidStatus_Type = OctetString
_FeRaidStatus_Object = MibScalar
feRaidStatus = _FeRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 1),
    _FeRaidStatus_Type()
)
feRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feRaidStatus.setStatus("current")
_FeRaidIsHealthy_Type = TruthValue
_FeRaidIsHealthy_Object = MibScalar
feRaidIsHealthy = _FeRaidIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 2),
    _FeRaidIsHealthy_Type()
)
feRaidIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feRaidIsHealthy.setStatus("current")
_FePhysicalDiskTable_Object = MibTable
fePhysicalDiskTable = _FePhysicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3)
)
if mibBuilder.loadTexts:
    fePhysicalDiskTable.setStatus("current")
_FePhysicalDiskEntry_Object = MibTableRow
fePhysicalDiskEntry = _FePhysicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1)
)
fePhysicalDiskEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "fePhysicalDiskIndex"),
)
if mibBuilder.loadTexts:
    fePhysicalDiskEntry.setStatus("current")
_FePhysicalDiskIndex_Type = Unsigned32
_FePhysicalDiskIndex_Object = MibTableColumn
fePhysicalDiskIndex = _FePhysicalDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 1),
    _FePhysicalDiskIndex_Type()
)
fePhysicalDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskIndex.setStatus("current")
_FePhysicalDiskName_Type = OctetString
_FePhysicalDiskName_Object = MibTableColumn
fePhysicalDiskName = _FePhysicalDiskName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 2),
    _FePhysicalDiskName_Type()
)
fePhysicalDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskName.setStatus("current")
_FePhysicalDiskStatus_Type = OctetString
_FePhysicalDiskStatus_Object = MibTableColumn
fePhysicalDiskStatus = _FePhysicalDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 3),
    _FePhysicalDiskStatus_Type()
)
fePhysicalDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskStatus.setStatus("current")
_FePhysicalDiskIsHealthy_Type = TruthValue
_FePhysicalDiskIsHealthy_Object = MibTableColumn
fePhysicalDiskIsHealthy = _FePhysicalDiskIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 4),
    _FePhysicalDiskIsHealthy_Type()
)
fePhysicalDiskIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskIsHealthy.setStatus("current")
_FePhysicalDiskDeviceSupport_Type = OctetString
_FePhysicalDiskDeviceSupport_Object = MibTableColumn
fePhysicalDiskDeviceSupport = _FePhysicalDiskDeviceSupport_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 5),
    _FePhysicalDiskDeviceSupport_Type()
)
fePhysicalDiskDeviceSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskDeviceSupport.setStatus("current")
_FePhysicalDiskSelfAssess_Type = OctetString
_FePhysicalDiskSelfAssess_Object = MibTableColumn
fePhysicalDiskSelfAssess = _FePhysicalDiskSelfAssess_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 6),
    _FePhysicalDiskSelfAssess_Type()
)
fePhysicalDiskSelfAssess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskSelfAssess.setStatus("current")
_FePhysicalDiskTotalBytes_Type = OctetString
_FePhysicalDiskTotalBytes_Object = MibTableColumn
fePhysicalDiskTotalBytes = _FePhysicalDiskTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 1, 3, 1, 7),
    _FePhysicalDiskTotalBytes_Type()
)
fePhysicalDiskTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePhysicalDiskTotalBytes.setStatus("current")
_FePowerSupply_ObjectIdentity = ObjectIdentity
fePowerSupply = _FePowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3)
)
_FePowerSupplyTraps_ObjectIdentity = ObjectIdentity
fePowerSupplyTraps = _FePowerSupplyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 0)
)
_FePowerSupplyInfo_ObjectIdentity = ObjectIdentity
fePowerSupplyInfo = _FePowerSupplyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1)
)
_FePowerSupplyOverallStatus_Type = OctetString
_FePowerSupplyOverallStatus_Object = MibScalar
fePowerSupplyOverallStatus = _FePowerSupplyOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 1),
    _FePowerSupplyOverallStatus_Type()
)
fePowerSupplyOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePowerSupplyOverallStatus.setStatus("current")
_FePowerSupplyOverallIsHealthy_Type = TruthValue
_FePowerSupplyOverallIsHealthy_Object = MibScalar
fePowerSupplyOverallIsHealthy = _FePowerSupplyOverallIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 2),
    _FePowerSupplyOverallIsHealthy_Type()
)
fePowerSupplyOverallIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePowerSupplyOverallIsHealthy.setStatus("current")
_FePowerSupplyTable_Object = MibTable
fePowerSupplyTable = _FePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 3)
)
if mibBuilder.loadTexts:
    fePowerSupplyTable.setStatus("current")
_FePowerSupplyEntry_Object = MibTableRow
fePowerSupplyEntry = _FePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 3, 1)
)
fePowerSupplyEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "fePowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    fePowerSupplyEntry.setStatus("current")
_FePowerSupplyIndex_Type = Unsigned32
_FePowerSupplyIndex_Object = MibTableColumn
fePowerSupplyIndex = _FePowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 3, 1, 1),
    _FePowerSupplyIndex_Type()
)
fePowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePowerSupplyIndex.setStatus("current")
_FePowerSupplyStatus_Type = OctetString
_FePowerSupplyStatus_Object = MibTableColumn
fePowerSupplyStatus = _FePowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 3, 1, 2),
    _FePowerSupplyStatus_Type()
)
fePowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePowerSupplyStatus.setStatus("current")
_FePowerSupplyIsHealthy_Type = TruthValue
_FePowerSupplyIsHealthy_Object = MibTableColumn
fePowerSupplyIsHealthy = _FePowerSupplyIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 1, 3, 1, 3),
    _FePowerSupplyIsHealthy_Type()
)
fePowerSupplyIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePowerSupplyIsHealthy.setStatus("current")
_FeFanHealth_ObjectIdentity = ObjectIdentity
feFanHealth = _FeFanHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4)
)
_FeFanHealthTraps_ObjectIdentity = ObjectIdentity
feFanHealthTraps = _FeFanHealthTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 0)
)
_FeFanHealthInfo_ObjectIdentity = ObjectIdentity
feFanHealthInfo = _FeFanHealthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1)
)
_FeFanOverallStatus_Type = OctetString
_FeFanOverallStatus_Object = MibScalar
feFanOverallStatus = _FeFanOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 1),
    _FeFanOverallStatus_Type()
)
feFanOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanOverallStatus.setStatus("current")
_FeFanOverallIsHealthy_Type = TruthValue
_FeFanOverallIsHealthy_Object = MibScalar
feFanOverallIsHealthy = _FeFanOverallIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 2),
    _FeFanOverallIsHealthy_Type()
)
feFanOverallIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanOverallIsHealthy.setStatus("current")
_FeFanStatusTable_Object = MibTable
feFanStatusTable = _FeFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3)
)
if mibBuilder.loadTexts:
    feFanStatusTable.setStatus("current")
_FeFanStatusEntry_Object = MibTableRow
feFanStatusEntry = _FeFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1)
)
feFanStatusEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feFanIndex"),
)
if mibBuilder.loadTexts:
    feFanStatusEntry.setStatus("current")
_FeFanIndex_Type = Unsigned32
_FeFanIndex_Object = MibTableColumn
feFanIndex = _FeFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1, 1),
    _FeFanIndex_Type()
)
feFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanIndex.setStatus("current")
_FeFanStatus_Type = OctetString
_FeFanStatus_Object = MibTableColumn
feFanStatus = _FeFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1, 2),
    _FeFanStatus_Type()
)
feFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanStatus.setStatus("current")
_FeFanIsHealthy_Type = TruthValue
_FeFanIsHealthy_Object = MibTableColumn
feFanIsHealthy = _FeFanIsHealthy_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1, 3),
    _FeFanIsHealthy_Type()
)
feFanIsHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanIsHealthy.setStatus("current")
_FeFanSpeed_Type = Unsigned32
_FeFanSpeed_Object = MibTableColumn
feFanSpeed = _FeFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 1, 3, 1, 4),
    _FeFanSpeed_Type()
)
feFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feFanSpeed.setStatus("current")
_FeApplication_ObjectIdentity = ObjectIdentity
feApplication = _FeApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5)
)
_FeApplicationTraps_ObjectIdentity = ObjectIdentity
feApplicationTraps = _FeApplicationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0)
)
_FeApplicationInfo_ObjectIdentity = ObjectIdentity
feApplicationInfo = _FeApplicationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1)
)
_FeInstalledSystemImage_Type = OctetString
_FeInstalledSystemImage_Object = MibScalar
feInstalledSystemImage = _FeInstalledSystemImage_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 1),
    _FeInstalledSystemImage_Type()
)
feInstalledSystemImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInstalledSystemImage.setStatus("current")
_FeSystemImageVersionCurrent_Type = OctetString
_FeSystemImageVersionCurrent_Object = MibScalar
feSystemImageVersionCurrent = _FeSystemImageVersionCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 2),
    _FeSystemImageVersionCurrent_Type()
)
feSystemImageVersionCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSystemImageVersionCurrent.setStatus("current")
_FeSystemImageVersionLatest_Type = OctetString
_FeSystemImageVersionLatest_Object = MibScalar
feSystemImageVersionLatest = _FeSystemImageVersionLatest_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 3),
    _FeSystemImageVersionLatest_Type()
)
feSystemImageVersionLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSystemImageVersionLatest.setStatus("current")
_FeIsSystemImageLatest_Type = TruthValue
_FeIsSystemImageLatest_Object = MibScalar
feIsSystemImageLatest = _FeIsSystemImageLatest_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 4),
    _FeIsSystemImageLatest_Type()
)
feIsSystemImageLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feIsSystemImageLatest.setStatus("current")
_FeSecurityContentVersion_Type = OctetString
_FeSecurityContentVersion_Object = MibScalar
feSecurityContentVersion = _FeSecurityContentVersion_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 5),
    _FeSecurityContentVersion_Type()
)
feSecurityContentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSecurityContentVersion.setStatus("current")
_FeLastContentUpdatePassed_Type = TruthValue
_FeLastContentUpdatePassed_Object = MibScalar
feLastContentUpdatePassed = _FeLastContentUpdatePassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 6),
    _FeLastContentUpdatePassed_Type()
)
feLastContentUpdatePassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLastContentUpdatePassed.setStatus("current")
_FeLastContentUpdateTime_Type = OctetString
_FeLastContentUpdateTime_Object = MibScalar
feLastContentUpdateTime = _FeLastContentUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 7),
    _FeLastContentUpdateTime_Type()
)
feLastContentUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feLastContentUpdateTime.setStatus("current")
_FeGIVersionTable_Object = MibTable
feGIVersionTable = _FeGIVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8)
)
if mibBuilder.loadTexts:
    feGIVersionTable.setStatus("current")
_FeGIVersionEntry_Object = MibTableRow
feGIVersionEntry = _FeGIVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1)
)
feGIVersionEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feGIIndex"),
)
if mibBuilder.loadTexts:
    feGIVersionEntry.setStatus("current")
_FeGIIndex_Type = Unsigned32
_FeGIIndex_Object = MibTableColumn
feGIIndex = _FeGIIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1, 1),
    _FeGIIndex_Type()
)
feGIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feGIIndex.setStatus("current")
_FeGIName_Type = OctetString
_FeGIName_Object = MibTableColumn
feGIName = _FeGIName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1, 2),
    _FeGIName_Type()
)
feGIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feGIName.setStatus("current")
_FeGIVersion_Type = OctetString
_FeGIVersion_Object = MibTableColumn
feGIVersion = _FeGIVersion_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1, 3),
    _FeGIVersion_Type()
)
feGIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feGIVersion.setStatus("current")
_FeGIEnabled_Type = TruthValue
_FeGIEnabled_Object = MibTableColumn
feGIEnabled = _FeGIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1, 4),
    _FeGIEnabled_Type()
)
feGIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feGIEnabled.setStatus("current")
_FeGIInstallDateTime_Type = OctetString
_FeGIInstallDateTime_Object = MibTableColumn
feGIInstallDateTime = _FeGIInstallDateTime_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 8, 1, 5),
    _FeGIInstallDateTime_Type()
)
feGIInstallDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feGIInstallDateTime.setStatus("current")
_FeActiveVMs_Type = Unsigned32
_FeActiveVMs_Object = MibScalar
feActiveVMs = _FeActiveVMs_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 9),
    _FeActiveVMs_Type()
)
feActiveVMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feActiveVMs.setStatus("current")
_FeProductLicenseActive_Type = TruthValue
_FeProductLicenseActive_Object = MibScalar
feProductLicenseActive = _FeProductLicenseActive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 10),
    _FeProductLicenseActive_Type()
)
feProductLicenseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feProductLicenseActive.setStatus("current")
_FeContentLicenseActive_Type = TruthValue
_FeContentLicenseActive_Object = MibScalar
feContentLicenseActive = _FeContentLicenseActive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 11),
    _FeContentLicenseActive_Type()
)
feContentLicenseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feContentLicenseActive.setStatus("current")
_FeSupportLicenseActive_Type = TruthValue
_FeSupportLicenseActive_Object = MibScalar
feSupportLicenseActive = _FeSupportLicenseActive_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 12),
    _FeSupportLicenseActive_Type()
)
feSupportLicenseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feSupportLicenseActive.setStatus("current")
_FeLicenseFeatureName_Type = OctetString
_FeLicenseFeatureName_Object = MibScalar
feLicenseFeatureName = _FeLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 13),
    _FeLicenseFeatureName_Type()
)
feLicenseFeatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLicenseFeatureName.setStatus("current")
_FeLicenseNewActiveState_Type = TruthValue
_FeLicenseNewActiveState_Object = MibScalar
feLicenseNewActiveState = _FeLicenseNewActiveState_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 14),
    _FeLicenseNewActiveState_Type()
)
feLicenseNewActiveState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLicenseNewActiveState.setStatus("current")
_FeLicenseOldActiveState_Type = TruthValue
_FeLicenseOldActiveState_Object = MibScalar
feLicenseOldActiveState = _FeLicenseOldActiveState_Object(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 1, 15),
    _FeLicenseOldActiveState_Type()
)
feLicenseOldActiveState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feLicenseOldActiveState.setStatus("current")
_FeCMS_ObjectIdentity = ObjectIdentity
feCMS = _FeCMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 12)
)
_FeCMSTraps_ObjectIdentity = ObjectIdentity
feCMSTraps = _FeCMSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 12, 0)
)
_FeCMSInfo_ObjectIdentity = ObjectIdentity
feCMSInfo = _FeCMSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1)
)
_FeTotalAppliancesAttached_Type = Unsigned32
_FeTotalAppliancesAttached_Object = MibScalar
feTotalAppliancesAttached = _FeTotalAppliancesAttached_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 1),
    _FeTotalAppliancesAttached_Type()
)
feTotalAppliancesAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalAppliancesAttached.setStatus("current")
_FeTotalWMPSAttached_Type = Unsigned32
_FeTotalWMPSAttached_Object = MibScalar
feTotalWMPSAttached = _FeTotalWMPSAttached_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 2),
    _FeTotalWMPSAttached_Type()
)
feTotalWMPSAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalWMPSAttached.setStatus("current")
_FeTotalEMPSAttached_Type = Unsigned32
_FeTotalEMPSAttached_Object = MibScalar
feTotalEMPSAttached = _FeTotalEMPSAttached_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 3),
    _FeTotalEMPSAttached_Type()
)
feTotalEMPSAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEMPSAttached.setStatus("current")
_FeTotalFMPSAttached_Type = Unsigned32
_FeTotalFMPSAttached_Object = MibScalar
feTotalFMPSAttached = _FeTotalFMPSAttached_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 4),
    _FeTotalFMPSAttached_Type()
)
feTotalFMPSAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalFMPSAttached.setStatus("current")
_FeTotalMASAttached_Type = Unsigned32
_FeTotalMASAttached_Object = MibScalar
feTotalMASAttached = _FeTotalMASAttached_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 5),
    _FeTotalMASAttached_Type()
)
feTotalMASAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMASAttached.setStatus("current")
_FeCMSApplianceTable_Object = MibTable
feCMSApplianceTable = _FeCMSApplianceTable_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6)
)
if mibBuilder.loadTexts:
    feCMSApplianceTable.setStatus("current")
_FeCMSApplianceEntry_Object = MibTableRow
feCMSApplianceEntry = _FeCMSApplianceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1)
)
feCMSApplianceEntry.setIndexNames(
    (0, "FE-FIREEYE-MIB", "feCMSApplianceIndex"),
)
if mibBuilder.loadTexts:
    feCMSApplianceEntry.setStatus("current")
_FeCMSApplianceIndex_Type = Unsigned32
_FeCMSApplianceIndex_Object = MibTableColumn
feCMSApplianceIndex = _FeCMSApplianceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 1),
    _FeCMSApplianceIndex_Type()
)
feCMSApplianceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceIndex.setStatus("current")
_FeCMSApplianceName_Type = OctetString
_FeCMSApplianceName_Object = MibTableColumn
feCMSApplianceName = _FeCMSApplianceName_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 2),
    _FeCMSApplianceName_Type()
)
feCMSApplianceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceName.setStatus("current")
_FeCMSApplianceDiskSpacePassed_Type = TruthValue
_FeCMSApplianceDiskSpacePassed_Object = MibTableColumn
feCMSApplianceDiskSpacePassed = _FeCMSApplianceDiskSpacePassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 3),
    _FeCMSApplianceDiskSpacePassed_Type()
)
feCMSApplianceDiskSpacePassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceDiskSpacePassed.setStatus("current")
_FeCMSApplianceFanPassed_Type = TruthValue
_FeCMSApplianceFanPassed_Object = MibTableColumn
feCMSApplianceFanPassed = _FeCMSApplianceFanPassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 4),
    _FeCMSApplianceFanPassed_Type()
)
feCMSApplianceFanPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceFanPassed.setStatus("current")
_FeCMSAppliancePowerSupplyPassed_Type = TruthValue
_FeCMSAppliancePowerSupplyPassed_Object = MibTableColumn
feCMSAppliancePowerSupplyPassed = _FeCMSAppliancePowerSupplyPassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 5),
    _FeCMSAppliancePowerSupplyPassed_Type()
)
feCMSAppliancePowerSupplyPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSAppliancePowerSupplyPassed.setStatus("current")
_FeCMSApplianceRaidPassed_Type = TruthValue
_FeCMSApplianceRaidPassed_Object = MibTableColumn
feCMSApplianceRaidPassed = _FeCMSApplianceRaidPassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 6),
    _FeCMSApplianceRaidPassed_Type()
)
feCMSApplianceRaidPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceRaidPassed.setStatus("current")
_FeCMSApplianceTemperaturePassed_Type = TruthValue
_FeCMSApplianceTemperaturePassed_Object = MibTableColumn
feCMSApplianceTemperaturePassed = _FeCMSApplianceTemperaturePassed_Object(
    (1, 3, 6, 1, 4, 1, 25597, 12, 1, 6, 1, 7),
    _FeCMSApplianceTemperaturePassed_Type()
)
feCMSApplianceTemperaturePassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feCMSApplianceTemperaturePassed.setStatus("current")
_FeEMPS_ObjectIdentity = ObjectIdentity
feEMPS = _FeEMPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 13)
)
_FeEMPSTraps_ObjectIdentity = ObjectIdentity
feEMPSTraps = _FeEMPSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0)
)
_FeEMPSInfo_ObjectIdentity = ObjectIdentity
feEMPSInfo = _FeEMPSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1)
)
_FeTotalEmailCount_Type = Counter64
_FeTotalEmailCount_Object = MibScalar
feTotalEmailCount = _FeTotalEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 1),
    _FeTotalEmailCount_Type()
)
feTotalEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailCount.setStatus("current")
_FeTotalEmailCountH_Type = Counter32
_FeTotalEmailCountH_Object = MibScalar
feTotalEmailCountH = _FeTotalEmailCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 2),
    _FeTotalEmailCountH_Type()
)
feTotalEmailCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailCountH.setStatus("current")
_FeTotalEmailCountL_Type = Counter32
_FeTotalEmailCountL_Object = MibScalar
feTotalEmailCountL = _FeTotalEmailCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 3),
    _FeTotalEmailCountL_Type()
)
feTotalEmailCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailCountL.setStatus("current")
_FeInfectedEmailCount_Type = Counter64
_FeInfectedEmailCount_Object = MibScalar
feInfectedEmailCount = _FeInfectedEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 4),
    _FeInfectedEmailCount_Type()
)
feInfectedEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedEmailCount.setStatus("current")
_FeInfectedEmailCountH_Type = Counter32
_FeInfectedEmailCountH_Object = MibScalar
feInfectedEmailCountH = _FeInfectedEmailCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 5),
    _FeInfectedEmailCountH_Type()
)
feInfectedEmailCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedEmailCountH.setStatus("current")
_FeInfectedEmailCountL_Type = Counter32
_FeInfectedEmailCountL_Object = MibScalar
feInfectedEmailCountL = _FeInfectedEmailCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 6),
    _FeInfectedEmailCountL_Type()
)
feInfectedEmailCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedEmailCountL.setStatus("current")
_FeAnalyzedEmailCount_Type = Counter64
_FeAnalyzedEmailCount_Object = MibScalar
feAnalyzedEmailCount = _FeAnalyzedEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 7),
    _FeAnalyzedEmailCount_Type()
)
feAnalyzedEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedEmailCount.setStatus("current")
_FeAnalyzedEmailCountH_Type = Counter32
_FeAnalyzedEmailCountH_Object = MibScalar
feAnalyzedEmailCountH = _FeAnalyzedEmailCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 8),
    _FeAnalyzedEmailCountH_Type()
)
feAnalyzedEmailCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedEmailCountH.setStatus("current")
_FeAnalyzedEmailCountL_Type = Counter32
_FeAnalyzedEmailCountL_Object = MibScalar
feAnalyzedEmailCountL = _FeAnalyzedEmailCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 9),
    _FeAnalyzedEmailCountL_Type()
)
feAnalyzedEmailCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedEmailCountL.setStatus("current")
_FeTotalUrlCount_Type = Counter64
_FeTotalUrlCount_Object = MibScalar
feTotalUrlCount = _FeTotalUrlCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 10),
    _FeTotalUrlCount_Type()
)
feTotalUrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlCount.setStatus("current")
_FeTotalUrlCountH_Type = Counter32
_FeTotalUrlCountH_Object = MibScalar
feTotalUrlCountH = _FeTotalUrlCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 11),
    _FeTotalUrlCountH_Type()
)
feTotalUrlCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlCountH.setStatus("current")
_FeTotalUrlCountL_Type = Counter32
_FeTotalUrlCountL_Object = MibScalar
feTotalUrlCountL = _FeTotalUrlCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 12),
    _FeTotalUrlCountL_Type()
)
feTotalUrlCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlCountL.setStatus("current")
_FeInfectedUrlCount_Type = Counter64
_FeInfectedUrlCount_Object = MibScalar
feInfectedUrlCount = _FeInfectedUrlCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 13),
    _FeInfectedUrlCount_Type()
)
feInfectedUrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedUrlCount.setStatus("current")
_FeInfectedUrlCountH_Type = Counter32
_FeInfectedUrlCountH_Object = MibScalar
feInfectedUrlCountH = _FeInfectedUrlCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 14),
    _FeInfectedUrlCountH_Type()
)
feInfectedUrlCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedUrlCountH.setStatus("current")
_FeInfectedUrlCountL_Type = Counter32
_FeInfectedUrlCountL_Object = MibScalar
feInfectedUrlCountL = _FeInfectedUrlCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 15),
    _FeInfectedUrlCountL_Type()
)
feInfectedUrlCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedUrlCountL.setStatus("current")
_FeAnalyzedUrlCount_Type = Counter64
_FeAnalyzedUrlCount_Object = MibScalar
feAnalyzedUrlCount = _FeAnalyzedUrlCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 16),
    _FeAnalyzedUrlCount_Type()
)
feAnalyzedUrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedUrlCount.setStatus("current")
_FeAnalyzedUrlCountH_Type = Counter32
_FeAnalyzedUrlCountH_Object = MibScalar
feAnalyzedUrlCountH = _FeAnalyzedUrlCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 17),
    _FeAnalyzedUrlCountH_Type()
)
feAnalyzedUrlCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedUrlCountH.setStatus("current")
_FeAnalyzedUrlCountL_Type = Counter32
_FeAnalyzedUrlCountL_Object = MibScalar
feAnalyzedUrlCountL = _FeAnalyzedUrlCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 18),
    _FeAnalyzedUrlCountL_Type()
)
feAnalyzedUrlCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedUrlCountL.setStatus("current")
_FeTotalAttachmentCount_Type = Counter64
_FeTotalAttachmentCount_Object = MibScalar
feTotalAttachmentCount = _FeTotalAttachmentCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 19),
    _FeTotalAttachmentCount_Type()
)
feTotalAttachmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalAttachmentCount.setStatus("current")
_FeTotalAttachmentCountH_Type = Counter32
_FeTotalAttachmentCountH_Object = MibScalar
feTotalAttachmentCountH = _FeTotalAttachmentCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 20),
    _FeTotalAttachmentCountH_Type()
)
feTotalAttachmentCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalAttachmentCountH.setStatus("current")
_FeTotalAttachmentCountL_Type = Counter32
_FeTotalAttachmentCountL_Object = MibScalar
feTotalAttachmentCountL = _FeTotalAttachmentCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 21),
    _FeTotalAttachmentCountL_Type()
)
feTotalAttachmentCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalAttachmentCountL.setStatus("current")
_FeInfectedAttachmentCount_Type = Counter64
_FeInfectedAttachmentCount_Object = MibScalar
feInfectedAttachmentCount = _FeInfectedAttachmentCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 22),
    _FeInfectedAttachmentCount_Type()
)
feInfectedAttachmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedAttachmentCount.setStatus("current")
_FeInfectedAttachmentCountH_Type = Counter32
_FeInfectedAttachmentCountH_Object = MibScalar
feInfectedAttachmentCountH = _FeInfectedAttachmentCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 23),
    _FeInfectedAttachmentCountH_Type()
)
feInfectedAttachmentCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedAttachmentCountH.setStatus("current")
_FeInfectedAttachmentCountL_Type = Counter32
_FeInfectedAttachmentCountL_Object = MibScalar
feInfectedAttachmentCountL = _FeInfectedAttachmentCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 24),
    _FeInfectedAttachmentCountL_Type()
)
feInfectedAttachmentCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feInfectedAttachmentCountL.setStatus("current")
_FeAnalyzedAttachmentCount_Type = Counter64
_FeAnalyzedAttachmentCount_Object = MibScalar
feAnalyzedAttachmentCount = _FeAnalyzedAttachmentCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 25),
    _FeAnalyzedAttachmentCount_Type()
)
feAnalyzedAttachmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedAttachmentCount.setStatus("current")
_FeAnalyzedAttachmentCountH_Type = Counter32
_FeAnalyzedAttachmentCountH_Object = MibScalar
feAnalyzedAttachmentCountH = _FeAnalyzedAttachmentCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 26),
    _FeAnalyzedAttachmentCountH_Type()
)
feAnalyzedAttachmentCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedAttachmentCountH.setStatus("current")
_FeAnalyzedAttachmentCountL_Type = Counter32
_FeAnalyzedAttachmentCountL_Object = MibScalar
feAnalyzedAttachmentCountL = _FeAnalyzedAttachmentCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 27),
    _FeAnalyzedAttachmentCountL_Type()
)
feAnalyzedAttachmentCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feAnalyzedAttachmentCountL.setStatus("current")
_FeTotalEmailHasAttachment_Type = Counter64
_FeTotalEmailHasAttachment_Object = MibScalar
feTotalEmailHasAttachment = _FeTotalEmailHasAttachment_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 28),
    _FeTotalEmailHasAttachment_Type()
)
feTotalEmailHasAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasAttachment.setStatus("current")
_FeTotalEmailHasAttachmentH_Type = Counter32
_FeTotalEmailHasAttachmentH_Object = MibScalar
feTotalEmailHasAttachmentH = _FeTotalEmailHasAttachmentH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 29),
    _FeTotalEmailHasAttachmentH_Type()
)
feTotalEmailHasAttachmentH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasAttachmentH.setStatus("current")
_FeTotalEmailHasAttachmentL_Type = Counter32
_FeTotalEmailHasAttachmentL_Object = MibScalar
feTotalEmailHasAttachmentL = _FeTotalEmailHasAttachmentL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 30),
    _FeTotalEmailHasAttachmentL_Type()
)
feTotalEmailHasAttachmentL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasAttachmentL.setStatus("current")
_FeTotalEmailHasUrl_Type = Counter64
_FeTotalEmailHasUrl_Object = MibScalar
feTotalEmailHasUrl = _FeTotalEmailHasUrl_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 31),
    _FeTotalEmailHasUrl_Type()
)
feTotalEmailHasUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasUrl.setStatus("current")
_FeTotalEmailHasUrlH_Type = Counter32
_FeTotalEmailHasUrlH_Object = MibScalar
feTotalEmailHasUrlH = _FeTotalEmailHasUrlH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 32),
    _FeTotalEmailHasUrlH_Type()
)
feTotalEmailHasUrlH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasUrlH.setStatus("current")
_FeTotalEmailHasUrlL_Type = Counter32
_FeTotalEmailHasUrlL_Object = MibScalar
feTotalEmailHasUrlL = _FeTotalEmailHasUrlL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 33),
    _FeTotalEmailHasUrlL_Type()
)
feTotalEmailHasUrlL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasUrlL.setStatus("current")
_FeTotalEmailHasBadAttachment_Type = Counter64
_FeTotalEmailHasBadAttachment_Object = MibScalar
feTotalEmailHasBadAttachment = _FeTotalEmailHasBadAttachment_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 34),
    _FeTotalEmailHasBadAttachment_Type()
)
feTotalEmailHasBadAttachment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadAttachment.setStatus("current")
_FeTotalEmailHasBadAttachmentH_Type = Counter32
_FeTotalEmailHasBadAttachmentH_Object = MibScalar
feTotalEmailHasBadAttachmentH = _FeTotalEmailHasBadAttachmentH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 35),
    _FeTotalEmailHasBadAttachmentH_Type()
)
feTotalEmailHasBadAttachmentH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadAttachmentH.setStatus("current")
_FeTotalEmailHasBadAttachmentL_Type = Counter32
_FeTotalEmailHasBadAttachmentL_Object = MibScalar
feTotalEmailHasBadAttachmentL = _FeTotalEmailHasBadAttachmentL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 36),
    _FeTotalEmailHasBadAttachmentL_Type()
)
feTotalEmailHasBadAttachmentL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadAttachmentL.setStatus("current")
_FeTotalEmailHasBadUrl_Type = Counter64
_FeTotalEmailHasBadUrl_Object = MibScalar
feTotalEmailHasBadUrl = _FeTotalEmailHasBadUrl_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 37),
    _FeTotalEmailHasBadUrl_Type()
)
feTotalEmailHasBadUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadUrl.setStatus("current")
_FeTotalEmailHasBadUrlH_Type = Counter32
_FeTotalEmailHasBadUrlH_Object = MibScalar
feTotalEmailHasBadUrlH = _FeTotalEmailHasBadUrlH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 38),
    _FeTotalEmailHasBadUrlH_Type()
)
feTotalEmailHasBadUrlH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadUrlH.setStatus("current")
_FeTotalEmailHasBadUrlL_Type = Counter32
_FeTotalEmailHasBadUrlL_Object = MibScalar
feTotalEmailHasBadUrlL = _FeTotalEmailHasBadUrlL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 39),
    _FeTotalEmailHasBadUrlL_Type()
)
feTotalEmailHasBadUrlL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalEmailHasBadUrlL.setStatus("current")


class _FeeQuarantineUsage_Type(Unsigned32):
    """Custom type feeQuarantineUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FeeQuarantineUsage_Type.__name__ = "Unsigned32"
_FeeQuarantineUsage_Object = MibScalar
feeQuarantineUsage = _FeeQuarantineUsage_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 40),
    _FeeQuarantineUsage_Type()
)
feeQuarantineUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feeQuarantineUsage.setStatus("current")
_FeBypassEmailCount_Type = Counter64
_FeBypassEmailCount_Object = MibScalar
feBypassEmailCount = _FeBypassEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 41),
    _FeBypassEmailCount_Type()
)
feBypassEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feBypassEmailCount.setStatus("current")
_FeBypassEmailCountH_Type = Counter32
_FeBypassEmailCountH_Object = MibScalar
feBypassEmailCountH = _FeBypassEmailCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 42),
    _FeBypassEmailCountH_Type()
)
feBypassEmailCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feBypassEmailCountH.setStatus("current")
_FeBypassEmailCountL_Type = Counter32
_FeBypassEmailCountL_Object = MibScalar
feBypassEmailCountL = _FeBypassEmailCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 43),
    _FeBypassEmailCountL_Type()
)
feBypassEmailCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feBypassEmailCountL.setStatus("current")
_FeDeferredEmailCount_Type = Unsigned32
_FeDeferredEmailCount_Object = MibScalar
feDeferredEmailCount = _FeDeferredEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 44),
    _FeDeferredEmailCount_Type()
)
feDeferredEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feDeferredEmailCount.setStatus("current")
_FeHoldQueueEmailCount_Type = Unsigned32
_FeHoldQueueEmailCount_Object = MibScalar
feHoldQueueEmailCount = _FeHoldQueueEmailCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 45),
    _FeHoldQueueEmailCount_Type()
)
feHoldQueueEmailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feHoldQueueEmailCount.setStatus("current")
_FeOpenSmtpConnections_Type = Unsigned32
_FeOpenSmtpConnections_Object = MibScalar
feOpenSmtpConnections = _FeOpenSmtpConnections_Object(
    (1, 3, 6, 1, 4, 1, 25597, 13, 1, 46),
    _FeOpenSmtpConnections_Type()
)
feOpenSmtpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feOpenSmtpConnections.setStatus("current")
_FeWMPS_ObjectIdentity = ObjectIdentity
feWMPS = _FeWMPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 14)
)
_FeWMPSTraps_ObjectIdentity = ObjectIdentity
feWMPSTraps = _FeWMPSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0)
)
_FeWMPSInfo_ObjectIdentity = ObjectIdentity
feWMPSInfo = _FeWMPSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 14, 1)
)
_FeMAS_ObjectIdentity = ObjectIdentity
feMAS = _FeMAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 15)
)
_FeMASTraps_ObjectIdentity = ObjectIdentity
feMASTraps = _FeMASTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 15, 0)
)
_FeMASInfo_ObjectIdentity = ObjectIdentity
feMASInfo = _FeMASInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1)
)
_FeTotalObjectAnalyzedCount_Type = Counter64
_FeTotalObjectAnalyzedCount_Object = MibScalar
feTotalObjectAnalyzedCount = _FeTotalObjectAnalyzedCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 1),
    _FeTotalObjectAnalyzedCount_Type()
)
feTotalObjectAnalyzedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalObjectAnalyzedCount.setStatus("current")
_FeTotalObjectAnalyzedCountH_Type = Counter32
_FeTotalObjectAnalyzedCountH_Object = MibScalar
feTotalObjectAnalyzedCountH = _FeTotalObjectAnalyzedCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 2),
    _FeTotalObjectAnalyzedCountH_Type()
)
feTotalObjectAnalyzedCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalObjectAnalyzedCountH.setStatus("current")
_FeTotalObjectAnalyzedCountL_Type = Counter32
_FeTotalObjectAnalyzedCountL_Object = MibScalar
feTotalObjectAnalyzedCountL = _FeTotalObjectAnalyzedCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 3),
    _FeTotalObjectAnalyzedCountL_Type()
)
feTotalObjectAnalyzedCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalObjectAnalyzedCountL.setStatus("current")
_FeTotalMaliciousObjectCount_Type = Counter64
_FeTotalMaliciousObjectCount_Object = MibScalar
feTotalMaliciousObjectCount = _FeTotalMaliciousObjectCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 4),
    _FeTotalMaliciousObjectCount_Type()
)
feTotalMaliciousObjectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousObjectCount.setStatus("current")
_FeTotalMaliciousObjectCountH_Type = Counter32
_FeTotalMaliciousObjectCountH_Object = MibScalar
feTotalMaliciousObjectCountH = _FeTotalMaliciousObjectCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 5),
    _FeTotalMaliciousObjectCountH_Type()
)
feTotalMaliciousObjectCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousObjectCountH.setStatus("current")
_FeTotalMaliciousObjectCountL_Type = Counter32
_FeTotalMaliciousObjectCountL_Object = MibScalar
feTotalMaliciousObjectCountL = _FeTotalMaliciousObjectCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 6),
    _FeTotalMaliciousObjectCountL_Type()
)
feTotalMaliciousObjectCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousObjectCountL.setStatus("current")
_FeTotalUrlAnalyzedCount_Type = Counter64
_FeTotalUrlAnalyzedCount_Object = MibScalar
feTotalUrlAnalyzedCount = _FeTotalUrlAnalyzedCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 7),
    _FeTotalUrlAnalyzedCount_Type()
)
feTotalUrlAnalyzedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlAnalyzedCount.setStatus("current")
_FeTotalUrlAnalyzedCountH_Type = Counter32
_FeTotalUrlAnalyzedCountH_Object = MibScalar
feTotalUrlAnalyzedCountH = _FeTotalUrlAnalyzedCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 8),
    _FeTotalUrlAnalyzedCountH_Type()
)
feTotalUrlAnalyzedCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlAnalyzedCountH.setStatus("current")
_FeTotalUrlAnalyzedCountL_Type = Counter32
_FeTotalUrlAnalyzedCountL_Object = MibScalar
feTotalUrlAnalyzedCountL = _FeTotalUrlAnalyzedCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 9),
    _FeTotalUrlAnalyzedCountL_Type()
)
feTotalUrlAnalyzedCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalUrlAnalyzedCountL.setStatus("current")
_FeTotalMaliciousUrlCount_Type = Counter64
_FeTotalMaliciousUrlCount_Object = MibScalar
feTotalMaliciousUrlCount = _FeTotalMaliciousUrlCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 10),
    _FeTotalMaliciousUrlCount_Type()
)
feTotalMaliciousUrlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousUrlCount.setStatus("current")
_FeTotalMaliciousUrlCountH_Type = Counter32
_FeTotalMaliciousUrlCountH_Object = MibScalar
feTotalMaliciousUrlCountH = _FeTotalMaliciousUrlCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 11),
    _FeTotalMaliciousUrlCountH_Type()
)
feTotalMaliciousUrlCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousUrlCountH.setStatus("current")
_FeTotalMaliciousUrlCountL_Type = Counter32
_FeTotalMaliciousUrlCountL_Object = MibScalar
feTotalMaliciousUrlCountL = _FeTotalMaliciousUrlCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 12),
    _FeTotalMaliciousUrlCountL_Type()
)
feTotalMaliciousUrlCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousUrlCountL.setStatus("current")
_FeTotalFileUploadedCount_Type = Counter64
_FeTotalFileUploadedCount_Object = MibScalar
feTotalFileUploadedCount = _FeTotalFileUploadedCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 13),
    _FeTotalFileUploadedCount_Type()
)
feTotalFileUploadedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalFileUploadedCount.setStatus("current")
_FeTotalFileUploadedCountH_Type = Counter32
_FeTotalFileUploadedCountH_Object = MibScalar
feTotalFileUploadedCountH = _FeTotalFileUploadedCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 14),
    _FeTotalFileUploadedCountH_Type()
)
feTotalFileUploadedCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalFileUploadedCountH.setStatus("current")
_FeTotalFileUploadedCountL_Type = Counter32
_FeTotalFileUploadedCountL_Object = MibScalar
feTotalFileUploadedCountL = _FeTotalFileUploadedCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 15),
    _FeTotalFileUploadedCountL_Type()
)
feTotalFileUploadedCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalFileUploadedCountL.setStatus("current")
_FeTotalMaliciousFileCount_Type = Counter64
_FeTotalMaliciousFileCount_Object = MibScalar
feTotalMaliciousFileCount = _FeTotalMaliciousFileCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 16),
    _FeTotalMaliciousFileCount_Type()
)
feTotalMaliciousFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousFileCount.setStatus("current")
_FeTotalMaliciousFileCountH_Type = Counter32
_FeTotalMaliciousFileCountH_Object = MibScalar
feTotalMaliciousFileCountH = _FeTotalMaliciousFileCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 17),
    _FeTotalMaliciousFileCountH_Type()
)
feTotalMaliciousFileCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousFileCountH.setStatus("current")
_FeTotalMaliciousFileCountL_Type = Counter32
_FeTotalMaliciousFileCountL_Object = MibScalar
feTotalMaliciousFileCountL = _FeTotalMaliciousFileCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 18),
    _FeTotalMaliciousFileCountL_Type()
)
feTotalMaliciousFileCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousFileCountL.setStatus("current")
_FeTotalLiveModeCount_Type = Counter64
_FeTotalLiveModeCount_Object = MibScalar
feTotalLiveModeCount = _FeTotalLiveModeCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 19),
    _FeTotalLiveModeCount_Type()
)
feTotalLiveModeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalLiveModeCount.setStatus("current")
_FeTotalLiveModeCountH_Type = Counter32
_FeTotalLiveModeCountH_Object = MibScalar
feTotalLiveModeCountH = _FeTotalLiveModeCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 20),
    _FeTotalLiveModeCountH_Type()
)
feTotalLiveModeCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalLiveModeCountH.setStatus("current")
_FeTotalLiveModeCountL_Type = Counter32
_FeTotalLiveModeCountL_Object = MibScalar
feTotalLiveModeCountL = _FeTotalLiveModeCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 21),
    _FeTotalLiveModeCountL_Type()
)
feTotalLiveModeCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalLiveModeCountL.setStatus("current")
_FeTotalMaliciousLiveModeCount_Type = Counter64
_FeTotalMaliciousLiveModeCount_Object = MibScalar
feTotalMaliciousLiveModeCount = _FeTotalMaliciousLiveModeCount_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 22),
    _FeTotalMaliciousLiveModeCount_Type()
)
feTotalMaliciousLiveModeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousLiveModeCount.setStatus("current")
_FeTotalMaliciousLiveModeCountH_Type = Counter32
_FeTotalMaliciousLiveModeCountH_Object = MibScalar
feTotalMaliciousLiveModeCountH = _FeTotalMaliciousLiveModeCountH_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 23),
    _FeTotalMaliciousLiveModeCountH_Type()
)
feTotalMaliciousLiveModeCountH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousLiveModeCountH.setStatus("current")
_FeTotalMaliciousLiveModeCountL_Type = Counter32
_FeTotalMaliciousLiveModeCountL_Object = MibScalar
feTotalMaliciousLiveModeCountL = _FeTotalMaliciousLiveModeCountL_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 24),
    _FeTotalMaliciousLiveModeCountL_Type()
)
feTotalMaliciousLiveModeCountL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feTotalMaliciousLiveModeCountL.setStatus("current")
_FeMaid_Type = CounterBasedGauge64
_FeMaid_Object = MibScalar
feMaid = _FeMaid_Object(
    (1, 3, 6, 1, 4, 1, 25597, 15, 1, 25),
    _FeMaid_Type()
)
feMaid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    feMaid.setStatus("current")
_FeMibAdminInfo_ObjectIdentity = ObjectIdentity
feMibAdminInfo = _FeMibAdminInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 20)
)
_FeMibCompliances_ObjectIdentity = ObjectIdentity
feMibCompliances = _FeMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 20, 2)
)
_FeMibGroups_ObjectIdentity = ObjectIdentity
feMibGroups = _FeMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3)
)

# Managed Objects groups

feVariablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 1)
)
feVariablesGroup.setObjects(
      *(("FE-FIREEYE-MIB", "lmsVersion"),
        ("FE-FIREEYE-MIB", "eventCount"),
        ("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventProfileId"),
        ("FE-FIREEYE-MIB", "eventOsInfo"),
        ("FE-FIREEYE-MIB", "eventService"),
        ("FE-FIREEYE-MIB", "eventAttackType"),
        ("FE-FIREEYE-MIB", "eventSignatureName"),
        ("FE-FIREEYE-MIB", "eventSignatureType"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventCncNo"),
        ("FE-FIREEYE-MIB", "alertSignatureId"),
        ("FE-FIREEYE-MIB", "alertCncHost"),
        ("FE-FIREEYE-MIB", "alertCncPort"),
        ("FE-FIREEYE-MIB", "alertChecksum"),
        ("FE-FIREEYE-MIB", "alertAnalysisType"),
        ("FE-FIREEYE-MIB", "alertProfile"),
        ("FE-FIREEYE-MIB", "alertAction"),
        ("FE-FIREEYE-MIB", "alertInterface"),
        ("FE-FIREEYE-MIB", "alertSensorIp"),
        ("FE-FIREEYE-MIB", "alertSensorHost"),
        ("FE-FIREEYE-MIB", "alertSensorProduct"),
        ("FE-FIREEYE-MIB", "alertSensorRelease"),
        ("FE-FIREEYE-MIB", "alertUrl"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"),
        ("FE-FIREEYE-MIB", "eventSensorAddrType"),
        ("FE-FIREEYE-MIB", "eventSensorAddr"),
        ("FE-FIREEYE-MIB", "eventSrcPort"),
        ("FE-FIREEYE-MIB", "eventDateTime"),
        ("FE-FIREEYE-MIB", "ipsSignatureId"),
        ("FE-FIREEYE-MIB", "ipsSignatureRevision"),
        ("FE-FIREEYE-MIB", "ipsMatchCount"),
        ("FE-FIREEYE-MIB", "ipsSeverity"),
        ("FE-FIREEYE-MIB", "ipsSignatureName"),
        ("FE-FIREEYE-MIB", "ipsReferenceId"),
        ("FE-FIREEYE-MIB", "ipsBlockMode"),
        ("FE-FIREEYE-MIB", "ipsAttackTarget"))
)
if mibBuilder.loadTexts:
    feVariablesGroup.setStatus("current")

feSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 11)
)
feSystemInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feSystemStatus"),
        ("FE-FIREEYE-MIB", "feHardwareModel"),
        ("FE-FIREEYE-MIB", "feSerialNumber"),
        ("FE-FIREEYE-MIB", "feTemperatureValue"),
        ("FE-FIREEYE-MIB", "feTemperatureStatus"),
        ("FE-FIREEYE-MIB", "feTemperatureIsHealthy"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeIfname"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeIfname"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldAdminUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewAdminUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldLinkUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewLinkUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldSpeed"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewSpeed"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldDuplex"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewDuplex"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldAutoNeg"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewAutoNeg"))
)
if mibBuilder.loadTexts:
    feSystemInfoGroup.setStatus("current")

feStorageInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 13)
)
feStorageInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feRaidStatus"),
        ("FE-FIREEYE-MIB", "feRaidIsHealthy"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskIndex"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskName"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskStatus"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskIsHealthy"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskDeviceSupport"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskSelfAssess"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskTotalBytes"))
)
if mibBuilder.loadTexts:
    feStorageInfoGroup.setStatus("current")

fePowerSupplyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 15)
)
fePowerSupplyInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "fePowerSupplyOverallStatus"),
        ("FE-FIREEYE-MIB", "fePowerSupplyOverallIsHealthy"),
        ("FE-FIREEYE-MIB", "fePowerSupplyIndex"),
        ("FE-FIREEYE-MIB", "fePowerSupplyStatus"),
        ("FE-FIREEYE-MIB", "fePowerSupplyIsHealthy"))
)
if mibBuilder.loadTexts:
    fePowerSupplyInfoGroup.setStatus("current")

feFanHealthInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 17)
)
feFanHealthInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feFanOverallStatus"),
        ("FE-FIREEYE-MIB", "feFanOverallIsHealthy"),
        ("FE-FIREEYE-MIB", "feFanIndex"),
        ("FE-FIREEYE-MIB", "feFanStatus"),
        ("FE-FIREEYE-MIB", "feFanIsHealthy"),
        ("FE-FIREEYE-MIB", "feFanSpeed"))
)
if mibBuilder.loadTexts:
    feFanHealthInfoGroup.setStatus("current")

feApplicationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 19)
)
feApplicationInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feInstalledSystemImage"),
        ("FE-FIREEYE-MIB", "feSystemImageVersionCurrent"),
        ("FE-FIREEYE-MIB", "feSystemImageVersionLatest"),
        ("FE-FIREEYE-MIB", "feIsSystemImageLatest"),
        ("FE-FIREEYE-MIB", "feSecurityContentVersion"),
        ("FE-FIREEYE-MIB", "feLastContentUpdatePassed"),
        ("FE-FIREEYE-MIB", "feLastContentUpdateTime"),
        ("FE-FIREEYE-MIB", "feGIIndex"),
        ("FE-FIREEYE-MIB", "feGIName"),
        ("FE-FIREEYE-MIB", "feGIVersion"),
        ("FE-FIREEYE-MIB", "feGIEnabled"),
        ("FE-FIREEYE-MIB", "feGIInstallDateTime"),
        ("FE-FIREEYE-MIB", "feActiveVMs"),
        ("FE-FIREEYE-MIB", "feProductLicenseActive"),
        ("FE-FIREEYE-MIB", "feContentLicenseActive"),
        ("FE-FIREEYE-MIB", "feSupportLicenseActive"),
        ("FE-FIREEYE-MIB", "feLicenseFeatureName"),
        ("FE-FIREEYE-MIB", "feLicenseNewActiveState"),
        ("FE-FIREEYE-MIB", "feLicenseOldActiveState"))
)
if mibBuilder.loadTexts:
    feApplicationInfoGroup.setStatus("current")

feCMSInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 21)
)
feCMSInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feTotalAppliancesAttached"),
        ("FE-FIREEYE-MIB", "feTotalWMPSAttached"),
        ("FE-FIREEYE-MIB", "feTotalEMPSAttached"),
        ("FE-FIREEYE-MIB", "feTotalFMPSAttached"),
        ("FE-FIREEYE-MIB", "feTotalMASAttached"),
        ("FE-FIREEYE-MIB", "feCMSApplianceIndex"),
        ("FE-FIREEYE-MIB", "feCMSApplianceName"),
        ("FE-FIREEYE-MIB", "feCMSApplianceDiskSpacePassed"),
        ("FE-FIREEYE-MIB", "feCMSApplianceFanPassed"),
        ("FE-FIREEYE-MIB", "feCMSAppliancePowerSupplyPassed"),
        ("FE-FIREEYE-MIB", "feCMSApplianceRaidPassed"),
        ("FE-FIREEYE-MIB", "feCMSApplianceTemperaturePassed"))
)
if mibBuilder.loadTexts:
    feCMSInfoGroup.setStatus("current")

feEMPSInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 23)
)
feEMPSInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feTotalEmailCount"),
        ("FE-FIREEYE-MIB", "feTotalEmailCountH"),
        ("FE-FIREEYE-MIB", "feTotalEmailCountL"),
        ("FE-FIREEYE-MIB", "feInfectedEmailCount"),
        ("FE-FIREEYE-MIB", "feInfectedEmailCountH"),
        ("FE-FIREEYE-MIB", "feInfectedEmailCountL"),
        ("FE-FIREEYE-MIB", "feAnalyzedEmailCount"),
        ("FE-FIREEYE-MIB", "feAnalyzedEmailCountH"),
        ("FE-FIREEYE-MIB", "feAnalyzedEmailCountL"),
        ("FE-FIREEYE-MIB", "feTotalUrlCount"),
        ("FE-FIREEYE-MIB", "feTotalUrlCountH"),
        ("FE-FIREEYE-MIB", "feTotalUrlCountL"),
        ("FE-FIREEYE-MIB", "feInfectedUrlCount"),
        ("FE-FIREEYE-MIB", "feInfectedUrlCountH"),
        ("FE-FIREEYE-MIB", "feInfectedUrlCountL"),
        ("FE-FIREEYE-MIB", "feAnalyzedUrlCount"),
        ("FE-FIREEYE-MIB", "feAnalyzedUrlCountH"),
        ("FE-FIREEYE-MIB", "feAnalyzedUrlCountL"),
        ("FE-FIREEYE-MIB", "feTotalAttachmentCount"),
        ("FE-FIREEYE-MIB", "feTotalAttachmentCountH"),
        ("FE-FIREEYE-MIB", "feTotalAttachmentCountL"),
        ("FE-FIREEYE-MIB", "feInfectedAttachmentCount"),
        ("FE-FIREEYE-MIB", "feInfectedAttachmentCountH"),
        ("FE-FIREEYE-MIB", "feInfectedAttachmentCountL"),
        ("FE-FIREEYE-MIB", "feAnalyzedAttachmentCount"),
        ("FE-FIREEYE-MIB", "feAnalyzedAttachmentCountH"),
        ("FE-FIREEYE-MIB", "feAnalyzedAttachmentCountL"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasAttachment"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasAttachmentH"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasAttachmentL"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasUrl"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasUrlH"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasUrlL"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadAttachment"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadAttachmentH"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadAttachmentL"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadUrl"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadUrlH"),
        ("FE-FIREEYE-MIB", "feTotalEmailHasBadUrlL"),
        ("FE-FIREEYE-MIB", "feeQuarantineUsage"),
        ("FE-FIREEYE-MIB", "feBypassEmailCount"),
        ("FE-FIREEYE-MIB", "feBypassEmailCountH"),
        ("FE-FIREEYE-MIB", "feBypassEmailCountL"),
        ("FE-FIREEYE-MIB", "feDeferredEmailCount"),
        ("FE-FIREEYE-MIB", "feHoldQueueEmailCount"),
        ("FE-FIREEYE-MIB", "feOpenSmtpConnections"))
)
if mibBuilder.loadTexts:
    feEMPSInfoGroup.setStatus("current")

feMASInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 27)
)
feMASInfoGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feTotalObjectAnalyzedCount"),
        ("FE-FIREEYE-MIB", "feTotalObjectAnalyzedCountH"),
        ("FE-FIREEYE-MIB", "feTotalObjectAnalyzedCountL"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousObjectCount"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousObjectCountH"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousObjectCountL"),
        ("FE-FIREEYE-MIB", "feTotalUrlAnalyzedCount"),
        ("FE-FIREEYE-MIB", "feTotalUrlAnalyzedCountH"),
        ("FE-FIREEYE-MIB", "feTotalUrlAnalyzedCountL"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousUrlCount"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousUrlCountH"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousUrlCountL"),
        ("FE-FIREEYE-MIB", "feTotalFileUploadedCount"),
        ("FE-FIREEYE-MIB", "feTotalFileUploadedCountH"),
        ("FE-FIREEYE-MIB", "feTotalFileUploadedCountL"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousFileCount"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousFileCountH"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousFileCountL"),
        ("FE-FIREEYE-MIB", "feTotalLiveModeCount"),
        ("FE-FIREEYE-MIB", "feTotalLiveModeCountH"),
        ("FE-FIREEYE-MIB", "feTotalLiveModeCountL"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousLiveModeCount"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousLiveModeCountH"),
        ("FE-FIREEYE-MIB", "feTotalMaliciousLiveModeCountL"),
        ("FE-FIREEYE-MIB", "feMaid"))
)
if mibBuilder.loadTexts:
    feMASInfoGroup.setStatus("current")


# Notification objects

fireeyeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 1)
)
fireeyeAlert.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventProfileId"),
        ("FE-FIREEYE-MIB", "eventOsInfo"),
        ("FE-FIREEYE-MIB", "eventService"),
        ("FE-FIREEYE-MIB", "eventAttackType"),
        ("FE-FIREEYE-MIB", "eventSignatureName"),
        ("FE-FIREEYE-MIB", "eventSignatureType"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventCncNo"),
        ("FE-FIREEYE-MIB", "alertSignatureId"),
        ("FE-FIREEYE-MIB", "alertCncHost"),
        ("FE-FIREEYE-MIB", "alertCncPort"),
        ("FE-FIREEYE-MIB", "alertChecksum"),
        ("FE-FIREEYE-MIB", "alertAnalysisType"),
        ("FE-FIREEYE-MIB", "alertProfile"),
        ("FE-FIREEYE-MIB", "alertAction"),
        ("FE-FIREEYE-MIB", "alertInterface"),
        ("FE-FIREEYE-MIB", "alertSensorIp"),
        ("FE-FIREEYE-MIB", "alertSensorHost"),
        ("FE-FIREEYE-MIB", "alertSensorRelease"),
        ("FE-FIREEYE-MIB", "alertSensorProduct"),
        ("FE-FIREEYE-MIB", "alertUrl"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"),
        ("FE-FIREEYE-MIB", "eventSensorAddrType"),
        ("FE-FIREEYE-MIB", "eventSensorAddr"))
)
if mibBuilder.loadTexts:
    fireeyeAlert.setStatus(
        "current"
    )

executionAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 2)
)
executionAnomaly.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventProfileId"),
        ("FE-FIREEYE-MIB", "eventOsInfo"),
        ("FE-FIREEYE-MIB", "eventService"),
        ("FE-FIREEYE-MIB", "eventAttackType"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    executionAnomaly.setStatus(
        "current"
    )

networkAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 3)
)
networkAnomaly.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventProfileId"),
        ("FE-FIREEYE-MIB", "eventOsInfo"),
        ("FE-FIREEYE-MIB", "eventService"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventCncNo"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    networkAnomaly.setStatus(
        "current"
    )

signatureMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 4)
)
signatureMatch.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventSignatureName"),
        ("FE-FIREEYE-MIB", "eventSignatureType"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    signatureMatch.setStatus(
        "current"
    )

ccConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 9)
)
ccConnect.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventCncNo"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    ccConnect.setStatus(
        "current"
    )

ccSigmatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 10)
)
ccSigmatch.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventCncNo"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    ccSigmatch.setStatus(
        "current"
    )

osChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 11)
)
osChange.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventDate"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventTraceId"),
        ("FE-FIREEYE-MIB", "eventSrcIp"),
        ("FE-FIREEYE-MIB", "eventDstIp"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventVlan"),
        ("FE-FIREEYE-MIB", "eventProtocol"),
        ("FE-FIREEYE-MIB", "eventSrcHost"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"))
)
if mibBuilder.loadTexts:
    osChange.setStatus(
        "current"
    )

ipsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 3, 0, 12)
)
ipsAlert.setObjects(
      *(("FE-FIREEYE-MIB", "eventIndex"),
        ("FE-FIREEYE-MIB", "eventId"),
        ("FE-FIREEYE-MIB", "eventType"),
        ("FE-FIREEYE-MIB", "eventTime"),
        ("FE-FIREEYE-MIB", "eventSrcAddrType"),
        ("FE-FIREEYE-MIB", "eventSrcAddr"),
        ("FE-FIREEYE-MIB", "eventSrcPort"),
        ("FE-FIREEYE-MIB", "eventSrcMac"),
        ("FE-FIREEYE-MIB", "eventDstAddrType"),
        ("FE-FIREEYE-MIB", "eventDstAddr"),
        ("FE-FIREEYE-MIB", "eventDstPort"),
        ("FE-FIREEYE-MIB", "eventDstMac"),
        ("FE-FIREEYE-MIB", "ipsSignatureId"),
        ("FE-FIREEYE-MIB", "ipsSignatureRevision"),
        ("FE-FIREEYE-MIB", "ipsMatchCount"),
        ("FE-FIREEYE-MIB", "ipsSeverity"),
        ("FE-FIREEYE-MIB", "ipsSignatureName"),
        ("FE-FIREEYE-MIB", "ipsReferenceId"),
        ("FE-FIREEYE-MIB", "ipsBlockMode"),
        ("FE-FIREEYE-MIB", "ipsAttackTarget"),
        ("FE-FIREEYE-MIB", "alertSensorProduct"),
        ("FE-FIREEYE-MIB", "alertSensorHost"),
        ("FE-FIREEYE-MIB", "alertSensorRelease"),
        ("FE-FIREEYE-MIB", "alertUrl"))
)
if mibBuilder.loadTexts:
    ipsAlert.setStatus(
        "current"
    )

feExcessiveTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 1)
)
feExcessiveTemperature.setObjects(
    ("FE-FIREEYE-MIB", "feTemperatureIsHealthy")
)
if mibBuilder.loadTexts:
    feExcessiveTemperature.setStatus(
        "current"
    )

feNormalTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 2)
)
feNormalTemperature.setObjects(
    ("FE-FIREEYE-MIB", "feTemperatureIsHealthy")
)
if mibBuilder.loadTexts:
    feNormalTemperature.setStatus(
        "current"
    )

feIfLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 1, 0, 3)
)
feIfLinkChange.setObjects(
      *(("FE-FIREEYE-MIB", "feIfLinkChangeIfname"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldAdminUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewAdminUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldLinkUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewLinkUp"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldSpeed"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewSpeed"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldDuplex"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewDuplex"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeOldAutoNeg"),
        ("FE-FIREEYE-MIB", "feIfLinkChangeNewAutoNeg"))
)
if mibBuilder.loadTexts:
    feIfLinkChange.setStatus(
        "current"
    )

feRaidFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 0, 1)
)
feRaidFailure.setObjects(
    ("FE-FIREEYE-MIB", "feRaidIsHealthy")
)
if mibBuilder.loadTexts:
    feRaidFailure.setStatus(
        "current"
    )

feRaidRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 0, 2)
)
feRaidRecover.setObjects(
    ("FE-FIREEYE-MIB", "feRaidIsHealthy")
)
if mibBuilder.loadTexts:
    feRaidRecover.setStatus(
        "current"
    )

fePhysicalDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 0, 3)
)
fePhysicalDiskFailure.setObjects(
    ("FE-FIREEYE-MIB", "fePhysicalDiskIsHealthy")
)
if mibBuilder.loadTexts:
    fePhysicalDiskFailure.setStatus(
        "current"
    )

fePhysicalDiskRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 2, 0, 4)
)
fePhysicalDiskRecover.setObjects(
    ("FE-FIREEYE-MIB", "fePhysicalDiskIsHealthy")
)
if mibBuilder.loadTexts:
    fePhysicalDiskRecover.setStatus(
        "current"
    )

fePowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 0, 1)
)
fePowerSupplyFailure.setObjects(
    ("FE-FIREEYE-MIB", "fePowerSupplyOverallIsHealthy")
)
if mibBuilder.loadTexts:
    fePowerSupplyFailure.setStatus(
        "current"
    )

fePowerSupplyRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 3, 0, 2)
)
fePowerSupplyRecover.setObjects(
    ("FE-FIREEYE-MIB", "fePowerSupplyOverallIsHealthy")
)
if mibBuilder.loadTexts:
    fePowerSupplyRecover.setStatus(
        "current"
    )

feFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 0, 1)
)
feFanFailure.setObjects(
    ("FE-FIREEYE-MIB", "feFanOverallIsHealthy")
)
if mibBuilder.loadTexts:
    feFanFailure.setStatus(
        "current"
    )

feFanRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 4, 0, 2)
)
feFanRecover.setObjects(
    ("FE-FIREEYE-MIB", "feFanOverallIsHealthy")
)
if mibBuilder.loadTexts:
    feFanRecover.setStatus(
        "current"
    )

feLicenseStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0, 1)
)
feLicenseStateChanged.setObjects(
      *(("FE-FIREEYE-MIB", "feLicenseFeatureName"),
        ("FE-FIREEYE-MIB", "feLicenseNewActiveState"),
        ("FE-FIREEYE-MIB", "feLicenseOldActiveState"))
)
if mibBuilder.loadTexts:
    feLicenseStateChanged.setStatus(
        "current"
    )

feSecurityUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 11, 5, 0, 2)
)
if mibBuilder.loadTexts:
    feSecurityUpdateFailed.setStatus(
        "current"
    )

feCMSHAUnexpectedFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 12, 0, 1)
)
if mibBuilder.loadTexts:
    feCMSHAUnexpectedFailover.setStatus(
        "current"
    )

feCMSHAManualFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 12, 0, 2)
)
if mibBuilder.loadTexts:
    feCMSHAManualFailover.setStatus(
        "current"
    )

feDeferredQueueThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 1)
)
feDeferredQueueThreshold.setObjects(
    ("FE-FIREEYE-MIB", "feDeferredEmailCount")
)
if mibBuilder.loadTexts:
    feDeferredQueueThreshold.setStatus(
        "current"
    )

feBypassCountThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 2)
)
if mibBuilder.loadTexts:
    feBypassCountThreshold.setStatus(
        "current"
    )

feSmtpInterfaceRefuseConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 3)
)
if mibBuilder.loadTexts:
    feSmtpInterfaceRefuseConnection.setStatus(
        "current"
    )

feSmtpInterfaceRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 4)
)
if mibBuilder.loadTexts:
    feSmtpInterfaceRecover.setStatus(
        "current"
    )

feEMPSBypassStateEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 5)
)
if mibBuilder.loadTexts:
    feEMPSBypassStateEntered.setStatus(
        "current"
    )

feEMPSBypassStateExited = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 13, 0, 6)
)
if mibBuilder.loadTexts:
    feEMPSBypassStateExited.setStatus(
        "current"
    )

feHttpThroughputNotIncrease = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0, 1)
)
if mibBuilder.loadTexts:
    feHttpThroughputNotIncrease.setStatus(
        "current"
    )

feHardwareBypassEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 14, 0, 2)
)
if mibBuilder.loadTexts:
    feHardwareBypassEntered.setStatus(
        "current"
    )

feMaliciousMaid = NotificationType(
    (1, 3, 6, 1, 4, 1, 25597, 15, 0, 1)
)
feMaliciousMaid.setObjects(
    ("FE-FIREEYE-MIB", "feMaid")
)
if mibBuilder.loadTexts:
    feMaliciousMaid.setStatus(
        "current"
    )


# Notifications groups

feNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 2)
)
feNotificationsGroup.setObjects(
      *(("FE-FIREEYE-MIB", "fireeyeAlert"),
        ("FE-FIREEYE-MIB", "executionAnomaly"),
        ("FE-FIREEYE-MIB", "networkAnomaly"),
        ("FE-FIREEYE-MIB", "signatureMatch"),
        ("FE-FIREEYE-MIB", "ccConnect"),
        ("FE-FIREEYE-MIB", "ccSigmatch"),
        ("FE-FIREEYE-MIB", "osChange"),
        ("FE-FIREEYE-MIB", "ipsAlert"))
)
if mibBuilder.loadTexts:
    feNotificationsGroup.setStatus(
        "current"
    )

feSystemTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 12)
)
feSystemTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feExcessiveTemperature"),
        ("FE-FIREEYE-MIB", "feNormalTemperature"),
        ("FE-FIREEYE-MIB", "feIfLinkChange"))
)
if mibBuilder.loadTexts:
    feSystemTrapGroup.setStatus(
        "current"
    )

feStorageTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 14)
)
feStorageTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feRaidFailure"),
        ("FE-FIREEYE-MIB", "feRaidRecover"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskFailure"),
        ("FE-FIREEYE-MIB", "fePhysicalDiskRecover"))
)
if mibBuilder.loadTexts:
    feStorageTrapGroup.setStatus(
        "current"
    )

fePowerSupplyTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 16)
)
fePowerSupplyTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "fePowerSupplyFailure"),
        ("FE-FIREEYE-MIB", "fePowerSupplyRecover"))
)
if mibBuilder.loadTexts:
    fePowerSupplyTrapGroup.setStatus(
        "current"
    )

feFanHealthTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 18)
)
feFanHealthTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feFanFailure"),
        ("FE-FIREEYE-MIB", "feFanRecover"))
)
if mibBuilder.loadTexts:
    feFanHealthTrapGroup.setStatus(
        "current"
    )

feApplicationTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 20)
)
feApplicationTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feLicenseStateChanged"),
        ("FE-FIREEYE-MIB", "feSecurityUpdateFailed"))
)
if mibBuilder.loadTexts:
    feApplicationTrapGroup.setStatus(
        "current"
    )

feCMSTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 22)
)
feCMSTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feCMSHAUnexpectedFailover"),
        ("FE-FIREEYE-MIB", "feCMSHAManualFailover"))
)
if mibBuilder.loadTexts:
    feCMSTrapGroup.setStatus(
        "current"
    )

feEMPSTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 24)
)
feEMPSTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feDeferredQueueThreshold"),
        ("FE-FIREEYE-MIB", "feBypassCountThreshold"),
        ("FE-FIREEYE-MIB", "feSmtpInterfaceRefuseConnection"),
        ("FE-FIREEYE-MIB", "feSmtpInterfaceRecover"),
        ("FE-FIREEYE-MIB", "feEMPSBypassStateEntered"),
        ("FE-FIREEYE-MIB", "feEMPSBypassStateExited"))
)
if mibBuilder.loadTexts:
    feEMPSTrapGroup.setStatus(
        "current"
    )

feWMPSTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 26)
)
feWMPSTrapGroup.setObjects(
      *(("FE-FIREEYE-MIB", "feHttpThroughputNotIncrease"),
        ("FE-FIREEYE-MIB", "feHardwareBypassEntered"))
)
if mibBuilder.loadTexts:
    feWMPSTrapGroup.setStatus(
        "current"
    )

feMASTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25597, 20, 3, 28)
)
feMASTrapGroup.setObjects(
    ("FE-FIREEYE-MIB", "feMaliciousMaid")
)
if mibBuilder.loadTexts:
    feMASTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

feMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25597, 20, 2, 1)
)
if mibBuilder.loadTexts:
    feMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FE-FIREEYE-MIB",
    **{"fireeye": fireeye,
       "variables": variables,
       "lms": lms,
       "lmsVersion": lmsVersion,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventIndex": eventIndex,
       "eventId": eventId,
       "eventType": eventType,
       "eventDate": eventDate,
       "eventTime": eventTime,
       "eventTraceId": eventTraceId,
       "eventSrcIp": eventSrcIp,
       "eventDstIp": eventDstIp,
       "eventSrcMac": eventSrcMac,
       "eventDstMac": eventDstMac,
       "eventDstPort": eventDstPort,
       "eventVlan": eventVlan,
       "eventProtocol": eventProtocol,
       "eventProfileId": eventProfileId,
       "eventOsInfo": eventOsInfo,
       "eventService": eventService,
       "eventAttackType": eventAttackType,
       "eventSignatureName": eventSignatureName,
       "eventSignatureType": eventSignatureType,
       "eventSrcHost": eventSrcHost,
       "eventCncNo": eventCncNo,
       "alertSignatureId": alertSignatureId,
       "alertCncHost": alertCncHost,
       "alertCncPort": alertCncPort,
       "alertChecksum": alertChecksum,
       "alertAnalysisType": alertAnalysisType,
       "alertProfile": alertProfile,
       "alertAction": alertAction,
       "alertInterface": alertInterface,
       "alertSensorIp": alertSensorIp,
       "alertSensorHost": alertSensorHost,
       "alertSensorProduct": alertSensorProduct,
       "alertSensorRelease": alertSensorRelease,
       "alertUrl": alertUrl,
       "eventSrcAddrType": eventSrcAddrType,
       "eventSrcAddr": eventSrcAddr,
       "eventDstAddrType": eventDstAddrType,
       "eventDstAddr": eventDstAddr,
       "eventSensorAddrType": eventSensorAddrType,
       "eventSensorAddr": eventSensorAddr,
       "eventSrcPort": eventSrcPort,
       "eventDateTime": eventDateTime,
       "ipsSignatureId": ipsSignatureId,
       "ipsSignatureRevision": ipsSignatureRevision,
       "ipsMatchCount": ipsMatchCount,
       "ipsSeverity": ipsSeverity,
       "ipsSignatureName": ipsSignatureName,
       "ipsReferenceId": ipsReferenceId,
       "ipsBlockMode": ipsBlockMode,
       "ipsAttackTarget": ipsAttackTarget,
       "eventCount": eventCount,
       "notifications": notifications,
       "notificationPrefix": notificationPrefix,
       "fireeyeAlert": fireeyeAlert,
       "executionAnomaly": executionAnomaly,
       "networkAnomaly": networkAnomaly,
       "signatureMatch": signatureMatch,
       "ccConnect": ccConnect,
       "ccSigmatch": ccSigmatch,
       "osChange": osChange,
       "ipsAlert": ipsAlert,
       "feCommon": feCommon,
       "feSystem": feSystem,
       "feSystemTraps": feSystemTraps,
       "feExcessiveTemperature": feExcessiveTemperature,
       "feNormalTemperature": feNormalTemperature,
       "feIfLinkChange": feIfLinkChange,
       "feSystemInfo": feSystemInfo,
       "feSystemStatus": feSystemStatus,
       "feHardwareModel": feHardwareModel,
       "feSerialNumber": feSerialNumber,
       "feTemperatureValue": feTemperatureValue,
       "feTemperatureStatus": feTemperatureStatus,
       "feTemperatureIsHealthy": feTemperatureIsHealthy,
       "feIfLinkChangeIfname": feIfLinkChangeIfname,
       "feIfLinkChangeOldAdminUp": feIfLinkChangeOldAdminUp,
       "feIfLinkChangeNewAdminUp": feIfLinkChangeNewAdminUp,
       "feIfLinkChangeOldLinkUp": feIfLinkChangeOldLinkUp,
       "feIfLinkChangeNewLinkUp": feIfLinkChangeNewLinkUp,
       "feIfLinkChangeOldSpeed": feIfLinkChangeOldSpeed,
       "feIfLinkChangeNewSpeed": feIfLinkChangeNewSpeed,
       "feIfLinkChangeOldDuplex": feIfLinkChangeOldDuplex,
       "feIfLinkChangeNewDuplex": feIfLinkChangeNewDuplex,
       "feIfLinkChangeOldAutoNeg": feIfLinkChangeOldAutoNeg,
       "feIfLinkChangeNewAutoNeg": feIfLinkChangeNewAutoNeg,
       "feStorage": feStorage,
       "feStorageTraps": feStorageTraps,
       "feRaidFailure": feRaidFailure,
       "feRaidRecover": feRaidRecover,
       "fePhysicalDiskFailure": fePhysicalDiskFailure,
       "fePhysicalDiskRecover": fePhysicalDiskRecover,
       "feStorageInfo": feStorageInfo,
       "feRaidStatus": feRaidStatus,
       "feRaidIsHealthy": feRaidIsHealthy,
       "fePhysicalDiskTable": fePhysicalDiskTable,
       "fePhysicalDiskEntry": fePhysicalDiskEntry,
       "fePhysicalDiskIndex": fePhysicalDiskIndex,
       "fePhysicalDiskName": fePhysicalDiskName,
       "fePhysicalDiskStatus": fePhysicalDiskStatus,
       "fePhysicalDiskIsHealthy": fePhysicalDiskIsHealthy,
       "fePhysicalDiskDeviceSupport": fePhysicalDiskDeviceSupport,
       "fePhysicalDiskSelfAssess": fePhysicalDiskSelfAssess,
       "fePhysicalDiskTotalBytes": fePhysicalDiskTotalBytes,
       "fePowerSupply": fePowerSupply,
       "fePowerSupplyTraps": fePowerSupplyTraps,
       "fePowerSupplyFailure": fePowerSupplyFailure,
       "fePowerSupplyRecover": fePowerSupplyRecover,
       "fePowerSupplyInfo": fePowerSupplyInfo,
       "fePowerSupplyOverallStatus": fePowerSupplyOverallStatus,
       "fePowerSupplyOverallIsHealthy": fePowerSupplyOverallIsHealthy,
       "fePowerSupplyTable": fePowerSupplyTable,
       "fePowerSupplyEntry": fePowerSupplyEntry,
       "fePowerSupplyIndex": fePowerSupplyIndex,
       "fePowerSupplyStatus": fePowerSupplyStatus,
       "fePowerSupplyIsHealthy": fePowerSupplyIsHealthy,
       "feFanHealth": feFanHealth,
       "feFanHealthTraps": feFanHealthTraps,
       "feFanFailure": feFanFailure,
       "feFanRecover": feFanRecover,
       "feFanHealthInfo": feFanHealthInfo,
       "feFanOverallStatus": feFanOverallStatus,
       "feFanOverallIsHealthy": feFanOverallIsHealthy,
       "feFanStatusTable": feFanStatusTable,
       "feFanStatusEntry": feFanStatusEntry,
       "feFanIndex": feFanIndex,
       "feFanStatus": feFanStatus,
       "feFanIsHealthy": feFanIsHealthy,
       "feFanSpeed": feFanSpeed,
       "feApplication": feApplication,
       "feApplicationTraps": feApplicationTraps,
       "feLicenseStateChanged": feLicenseStateChanged,
       "feSecurityUpdateFailed": feSecurityUpdateFailed,
       "feApplicationInfo": feApplicationInfo,
       "feInstalledSystemImage": feInstalledSystemImage,
       "feSystemImageVersionCurrent": feSystemImageVersionCurrent,
       "feSystemImageVersionLatest": feSystemImageVersionLatest,
       "feIsSystemImageLatest": feIsSystemImageLatest,
       "feSecurityContentVersion": feSecurityContentVersion,
       "feLastContentUpdatePassed": feLastContentUpdatePassed,
       "feLastContentUpdateTime": feLastContentUpdateTime,
       "feGIVersionTable": feGIVersionTable,
       "feGIVersionEntry": feGIVersionEntry,
       "feGIIndex": feGIIndex,
       "feGIName": feGIName,
       "feGIVersion": feGIVersion,
       "feGIEnabled": feGIEnabled,
       "feGIInstallDateTime": feGIInstallDateTime,
       "feActiveVMs": feActiveVMs,
       "feProductLicenseActive": feProductLicenseActive,
       "feContentLicenseActive": feContentLicenseActive,
       "feSupportLicenseActive": feSupportLicenseActive,
       "feLicenseFeatureName": feLicenseFeatureName,
       "feLicenseNewActiveState": feLicenseNewActiveState,
       "feLicenseOldActiveState": feLicenseOldActiveState,
       "feCMS": feCMS,
       "feCMSTraps": feCMSTraps,
       "feCMSHAUnexpectedFailover": feCMSHAUnexpectedFailover,
       "feCMSHAManualFailover": feCMSHAManualFailover,
       "feCMSInfo": feCMSInfo,
       "feTotalAppliancesAttached": feTotalAppliancesAttached,
       "feTotalWMPSAttached": feTotalWMPSAttached,
       "feTotalEMPSAttached": feTotalEMPSAttached,
       "feTotalFMPSAttached": feTotalFMPSAttached,
       "feTotalMASAttached": feTotalMASAttached,
       "feCMSApplianceTable": feCMSApplianceTable,
       "feCMSApplianceEntry": feCMSApplianceEntry,
       "feCMSApplianceIndex": feCMSApplianceIndex,
       "feCMSApplianceName": feCMSApplianceName,
       "feCMSApplianceDiskSpacePassed": feCMSApplianceDiskSpacePassed,
       "feCMSApplianceFanPassed": feCMSApplianceFanPassed,
       "feCMSAppliancePowerSupplyPassed": feCMSAppliancePowerSupplyPassed,
       "feCMSApplianceRaidPassed": feCMSApplianceRaidPassed,
       "feCMSApplianceTemperaturePassed": feCMSApplianceTemperaturePassed,
       "feEMPS": feEMPS,
       "feEMPSTraps": feEMPSTraps,
       "feDeferredQueueThreshold": feDeferredQueueThreshold,
       "feBypassCountThreshold": feBypassCountThreshold,
       "feSmtpInterfaceRefuseConnection": feSmtpInterfaceRefuseConnection,
       "feSmtpInterfaceRecover": feSmtpInterfaceRecover,
       "feEMPSBypassStateEntered": feEMPSBypassStateEntered,
       "feEMPSBypassStateExited": feEMPSBypassStateExited,
       "feEMPSInfo": feEMPSInfo,
       "feTotalEmailCount": feTotalEmailCount,
       "feTotalEmailCountH": feTotalEmailCountH,
       "feTotalEmailCountL": feTotalEmailCountL,
       "feInfectedEmailCount": feInfectedEmailCount,
       "feInfectedEmailCountH": feInfectedEmailCountH,
       "feInfectedEmailCountL": feInfectedEmailCountL,
       "feAnalyzedEmailCount": feAnalyzedEmailCount,
       "feAnalyzedEmailCountH": feAnalyzedEmailCountH,
       "feAnalyzedEmailCountL": feAnalyzedEmailCountL,
       "feTotalUrlCount": feTotalUrlCount,
       "feTotalUrlCountH": feTotalUrlCountH,
       "feTotalUrlCountL": feTotalUrlCountL,
       "feInfectedUrlCount": feInfectedUrlCount,
       "feInfectedUrlCountH": feInfectedUrlCountH,
       "feInfectedUrlCountL": feInfectedUrlCountL,
       "feAnalyzedUrlCount": feAnalyzedUrlCount,
       "feAnalyzedUrlCountH": feAnalyzedUrlCountH,
       "feAnalyzedUrlCountL": feAnalyzedUrlCountL,
       "feTotalAttachmentCount": feTotalAttachmentCount,
       "feTotalAttachmentCountH": feTotalAttachmentCountH,
       "feTotalAttachmentCountL": feTotalAttachmentCountL,
       "feInfectedAttachmentCount": feInfectedAttachmentCount,
       "feInfectedAttachmentCountH": feInfectedAttachmentCountH,
       "feInfectedAttachmentCountL": feInfectedAttachmentCountL,
       "feAnalyzedAttachmentCount": feAnalyzedAttachmentCount,
       "feAnalyzedAttachmentCountH": feAnalyzedAttachmentCountH,
       "feAnalyzedAttachmentCountL": feAnalyzedAttachmentCountL,
       "feTotalEmailHasAttachment": feTotalEmailHasAttachment,
       "feTotalEmailHasAttachmentH": feTotalEmailHasAttachmentH,
       "feTotalEmailHasAttachmentL": feTotalEmailHasAttachmentL,
       "feTotalEmailHasUrl": feTotalEmailHasUrl,
       "feTotalEmailHasUrlH": feTotalEmailHasUrlH,
       "feTotalEmailHasUrlL": feTotalEmailHasUrlL,
       "feTotalEmailHasBadAttachment": feTotalEmailHasBadAttachment,
       "feTotalEmailHasBadAttachmentH": feTotalEmailHasBadAttachmentH,
       "feTotalEmailHasBadAttachmentL": feTotalEmailHasBadAttachmentL,
       "feTotalEmailHasBadUrl": feTotalEmailHasBadUrl,
       "feTotalEmailHasBadUrlH": feTotalEmailHasBadUrlH,
       "feTotalEmailHasBadUrlL": feTotalEmailHasBadUrlL,
       "feeQuarantineUsage": feeQuarantineUsage,
       "feBypassEmailCount": feBypassEmailCount,
       "feBypassEmailCountH": feBypassEmailCountH,
       "feBypassEmailCountL": feBypassEmailCountL,
       "feDeferredEmailCount": feDeferredEmailCount,
       "feHoldQueueEmailCount": feHoldQueueEmailCount,
       "feOpenSmtpConnections": feOpenSmtpConnections,
       "feWMPS": feWMPS,
       "feWMPSTraps": feWMPSTraps,
       "feHttpThroughputNotIncrease": feHttpThroughputNotIncrease,
       "feHardwareBypassEntered": feHardwareBypassEntered,
       "feWMPSInfo": feWMPSInfo,
       "feMAS": feMAS,
       "feMASTraps": feMASTraps,
       "feMaliciousMaid": feMaliciousMaid,
       "feMASInfo": feMASInfo,
       "feTotalObjectAnalyzedCount": feTotalObjectAnalyzedCount,
       "feTotalObjectAnalyzedCountH": feTotalObjectAnalyzedCountH,
       "feTotalObjectAnalyzedCountL": feTotalObjectAnalyzedCountL,
       "feTotalMaliciousObjectCount": feTotalMaliciousObjectCount,
       "feTotalMaliciousObjectCountH": feTotalMaliciousObjectCountH,
       "feTotalMaliciousObjectCountL": feTotalMaliciousObjectCountL,
       "feTotalUrlAnalyzedCount": feTotalUrlAnalyzedCount,
       "feTotalUrlAnalyzedCountH": feTotalUrlAnalyzedCountH,
       "feTotalUrlAnalyzedCountL": feTotalUrlAnalyzedCountL,
       "feTotalMaliciousUrlCount": feTotalMaliciousUrlCount,
       "feTotalMaliciousUrlCountH": feTotalMaliciousUrlCountH,
       "feTotalMaliciousUrlCountL": feTotalMaliciousUrlCountL,
       "feTotalFileUploadedCount": feTotalFileUploadedCount,
       "feTotalFileUploadedCountH": feTotalFileUploadedCountH,
       "feTotalFileUploadedCountL": feTotalFileUploadedCountL,
       "feTotalMaliciousFileCount": feTotalMaliciousFileCount,
       "feTotalMaliciousFileCountH": feTotalMaliciousFileCountH,
       "feTotalMaliciousFileCountL": feTotalMaliciousFileCountL,
       "feTotalLiveModeCount": feTotalLiveModeCount,
       "feTotalLiveModeCountH": feTotalLiveModeCountH,
       "feTotalLiveModeCountL": feTotalLiveModeCountL,
       "feTotalMaliciousLiveModeCount": feTotalMaliciousLiveModeCount,
       "feTotalMaliciousLiveModeCountH": feTotalMaliciousLiveModeCountH,
       "feTotalMaliciousLiveModeCountL": feTotalMaliciousLiveModeCountL,
       "feMaid": feMaid,
       "feMibAdminInfo": feMibAdminInfo,
       "fireeyeMibModule": fireeyeMibModule,
       "feMibCompliances": feMibCompliances,
       "feMibCompliance": feMibCompliance,
       "feMibGroups": feMibGroups,
       "feVariablesGroup": feVariablesGroup,
       "feNotificationsGroup": feNotificationsGroup,
       "feSystemInfoGroup": feSystemInfoGroup,
       "feSystemTrapGroup": feSystemTrapGroup,
       "feStorageInfoGroup": feStorageInfoGroup,
       "feStorageTrapGroup": feStorageTrapGroup,
       "fePowerSupplyInfoGroup": fePowerSupplyInfoGroup,
       "fePowerSupplyTrapGroup": fePowerSupplyTrapGroup,
       "feFanHealthInfoGroup": feFanHealthInfoGroup,
       "feFanHealthTrapGroup": feFanHealthTrapGroup,
       "feApplicationInfoGroup": feApplicationInfoGroup,
       "feApplicationTrapGroup": feApplicationTrapGroup,
       "feCMSInfoGroup": feCMSInfoGroup,
       "feCMSTrapGroup": feCMSTrapGroup,
       "feEMPSInfoGroup": feEMPSInfoGroup,
       "feEMPSTrapGroup": feEMPSTrapGroup,
       "feWMPSTrapGroup": feWMPSTrapGroup,
       "feMASInfoGroup": feMASInfoGroup,
       "feMASTrapGroup": feMASTrapGroup}
)
