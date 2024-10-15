# SNMP MIB module (MERU-VOICE-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-VOICE-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:17 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwStatistics,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwStatistics")

(MwlDeviceType,
 MwlNetProtocol,
 MwlOnOffSwitch,
 MwlQosCallState,
 MwlQosProtocol) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlDeviceType",
    "MwlNetProtocol",
    "MwlOnOffSwitch",
    "MwlQosCallState",
    "MwlQosProtocol")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwVoiceStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwPhoneTable_Object = MibTable
mwPhoneTable = _MwPhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mwPhoneTable.setStatus("current")
_MwPhoneEntry_Object = MibTableRow
mwPhoneEntry = _MwPhoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1)
)
mwPhoneEntry.setIndexNames(
    (0, "MERU-VOICE-STATISTICS-MIB", "mwPhoneTableIndex"),
)
if mibBuilder.loadTexts:
    mwPhoneEntry.setStatus("current")
_MwPhoneTableIndex_Type = Integer32
_MwPhoneTableIndex_Object = MibTableColumn
mwPhoneTableIndex = _MwPhoneTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 1),
    _MwPhoneTableIndex_Type()
)
mwPhoneTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwPhoneTableIndex.setStatus("current")
_MwPhoneIp_Type = IpAddress
_MwPhoneIp_Object = MibTableColumn
mwPhoneIp = _MwPhoneIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 2),
    _MwPhoneIp_Type()
)
mwPhoneIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneIp.setStatus("current")
_MwPhoneAp_Type = Integer32
_MwPhoneAp_Object = MibTableColumn
mwPhoneAp = _MwPhoneAp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 3),
    _MwPhoneAp_Type()
)
mwPhoneAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneAp.setStatus("current")
_MwPhoneMac_Type = MacAddress
_MwPhoneMac_Object = MibTableColumn
mwPhoneMac = _MwPhoneMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 4),
    _MwPhoneMac_Type()
)
mwPhoneMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneMac.setStatus("current")
_MwPhoneType_Type = MwlQosProtocol
_MwPhoneType_Object = MibTableColumn
mwPhoneType = _MwPhoneType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 5),
    _MwPhoneType_Type()
)
mwPhoneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneType.setStatus("current")
_MwPhoneApName_Type = DisplayString
_MwPhoneApName_Object = MibTableColumn
mwPhoneApName = _MwPhoneApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 6),
    _MwPhoneApName_Type()
)
mwPhoneApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneApName.setStatus("current")
_MwPhoneServer_Type = DisplayString
_MwPhoneServer_Object = MibTableColumn
mwPhoneServer = _MwPhoneServer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 7),
    _MwPhoneServer_Type()
)
mwPhoneServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneServer.setStatus("current")
_MwPhoneUsername_Type = DisplayString
_MwPhoneUsername_Object = MibTableColumn
mwPhoneUsername = _MwPhoneUsername_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 8),
    _MwPhoneUsername_Type()
)
mwPhoneUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneUsername.setStatus("current")
_MwPhoneTransport_Type = MwlNetProtocol
_MwPhoneTransport_Object = MibTableColumn
mwPhoneTransport = _MwPhoneTransport_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 9),
    _MwPhoneTransport_Type()
)
mwPhoneTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneTransport.setStatus("current")
_MwPhoneDeviceType_Type = MwlDeviceType
_MwPhoneDeviceType_Object = MibTableColumn
mwPhoneDeviceType = _MwPhoneDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 1, 1, 10),
    _MwPhoneDeviceType_Type()
)
mwPhoneDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneDeviceType.setStatus("current")
_MwPhoneCallTable_Object = MibTable
mwPhoneCallTable = _MwPhoneCallTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    mwPhoneCallTable.setStatus("current")
_MwPhoneCallEntry_Object = MibTableRow
mwPhoneCallEntry = _MwPhoneCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1)
)
mwPhoneCallEntry.setIndexNames(
    (0, "MERU-VOICE-STATISTICS-MIB", "mwPhoneCallTableIndex"),
)
if mibBuilder.loadTexts:
    mwPhoneCallEntry.setStatus("current")
_MwPhoneCallTableIndex_Type = Integer32
_MwPhoneCallTableIndex_Object = MibTableColumn
mwPhoneCallTableIndex = _MwPhoneCallTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 1),
    _MwPhoneCallTableIndex_Type()
)
mwPhoneCallTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwPhoneCallTableIndex.setStatus("current")
_MwPhoneCallToIp_Type = IpAddress
_MwPhoneCallToIp_Object = MibTableColumn
mwPhoneCallToIp = _MwPhoneCallToIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 2),
    _MwPhoneCallToIp_Type()
)
mwPhoneCallToIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallToIp.setStatus("current")
_MwPhoneCallToAp_Type = Integer32
_MwPhoneCallToAp_Object = MibTableColumn
mwPhoneCallToAp = _MwPhoneCallToAp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 3),
    _MwPhoneCallToAp_Type()
)
mwPhoneCallToAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallToAp.setStatus("current")
_MwPhoneCallType_Type = MwlQosProtocol
_MwPhoneCallType_Object = MibTableColumn
mwPhoneCallType = _MwPhoneCallType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 4),
    _MwPhoneCallType_Type()
)
mwPhoneCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallType.setStatus("current")
_MwPhoneCallToMac_Type = MacAddress
_MwPhoneCallToMac_Object = MibTableColumn
mwPhoneCallToMac = _MwPhoneCallToMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 5),
    _MwPhoneCallToMac_Type()
)
mwPhoneCallToMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallToMac.setStatus("current")
_MwPhoneCallState_Type = MwlQosCallState
_MwPhoneCallState_Object = MibTableColumn
mwPhoneCallState = _MwPhoneCallState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 6),
    _MwPhoneCallState_Type()
)
mwPhoneCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallState.setStatus("current")
_MwPhoneCallFromIp_Type = IpAddress
_MwPhoneCallFromIp_Object = MibTableColumn
mwPhoneCallFromIp = _MwPhoneCallFromIp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 7),
    _MwPhoneCallFromIp_Type()
)
mwPhoneCallFromIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallFromIp.setStatus("current")
_MwPhoneCallFromAp_Type = Integer32
_MwPhoneCallFromAp_Object = MibTableColumn
mwPhoneCallFromAp = _MwPhoneCallFromAp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 8),
    _MwPhoneCallFromAp_Type()
)
mwPhoneCallFromAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallFromAp.setStatus("current")
_MwPhoneCallFromMac_Type = MacAddress
_MwPhoneCallFromMac_Object = MibTableColumn
mwPhoneCallFromMac = _MwPhoneCallFromMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 9),
    _MwPhoneCallFromMac_Type()
)
mwPhoneCallFromMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallFromMac.setStatus("current")
_MwPhoneCallToApName_Type = DisplayString
_MwPhoneCallToApName_Object = MibTableColumn
mwPhoneCallToApName = _MwPhoneCallToApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 10),
    _MwPhoneCallToApName_Type()
)
mwPhoneCallToApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallToApName.setStatus("current")
_MwPhoneCallToFlowtag_Type = Integer32
_MwPhoneCallToFlowtag_Object = MibTableColumn
mwPhoneCallToFlowtag = _MwPhoneCallToFlowtag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 11),
    _MwPhoneCallToFlowtag_Type()
)
mwPhoneCallToFlowtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallToFlowtag.setStatus("current")
_MwPhoneCallToPending_Type = MwlOnOffSwitch
_MwPhoneCallToPending_Object = MibTableColumn
mwPhoneCallToPending = _MwPhoneCallToPending_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 12),
    _MwPhoneCallToPending_Type()
)
mwPhoneCallToPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallToPending.setStatus("current")
_MwPhoneCallFromApName_Type = DisplayString
_MwPhoneCallFromApName_Object = MibTableColumn
mwPhoneCallFromApName = _MwPhoneCallFromApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 13),
    _MwPhoneCallFromApName_Type()
)
mwPhoneCallFromApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallFromApName.setStatus("current")
_MwPhoneCallToUsername_Type = DisplayString
_MwPhoneCallToUsername_Object = MibTableColumn
mwPhoneCallToUsername = _MwPhoneCallToUsername_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 14),
    _MwPhoneCallToUsername_Type()
)
mwPhoneCallToUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallToUsername.setStatus("current")
_MwPhoneCallFromFlowtag_Type = Integer32
_MwPhoneCallFromFlowtag_Object = MibTableColumn
mwPhoneCallFromFlowtag = _MwPhoneCallFromFlowtag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 15),
    _MwPhoneCallFromFlowtag_Type()
)
mwPhoneCallFromFlowtag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallFromFlowtag.setStatus("current")
_MwPhoneCallFromPending_Type = MwlOnOffSwitch
_MwPhoneCallFromPending_Object = MibTableColumn
mwPhoneCallFromPending = _MwPhoneCallFromPending_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 16),
    _MwPhoneCallFromPending_Type()
)
mwPhoneCallFromPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallFromPending.setStatus("current")
_MwPhoneCallFromUsername_Type = DisplayString
_MwPhoneCallFromUsername_Object = MibTableColumn
mwPhoneCallFromUsername = _MwPhoneCallFromUsername_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 2, 1, 17),
    _MwPhoneCallFromUsername_Type()
)
mwPhoneCallFromUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPhoneCallFromUsername.setStatus("current")
_MwVoiceStatusTable_Object = MibTable
mwVoiceStatusTable = _MwVoiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    mwVoiceStatusTable.setStatus("current")
_MwVoiceStatusEntry_Object = MibTableRow
mwVoiceStatusEntry = _MwVoiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1)
)
mwVoiceStatusEntry.setIndexNames(
    (0, "MERU-VOICE-STATISTICS-MIB", "mwVoiceStatusTableIndex"),
)
if mibBuilder.loadTexts:
    mwVoiceStatusEntry.setStatus("current")
_MwVoiceStatusTableIndex_Type = Integer32
_MwVoiceStatusTableIndex_Object = MibTableColumn
mwVoiceStatusTableIndex = _MwVoiceStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 1),
    _MwVoiceStatusTableIndex_Type()
)
mwVoiceStatusTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwVoiceStatusTableIndex.setStatus("current")
_MwVoiceStatusAp_Type = Integer32
_MwVoiceStatusAp_Object = MibTableColumn
mwVoiceStatusAp = _MwVoiceStatusAp_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 2),
    _MwVoiceStatusAp_Type()
)
mwVoiceStatusAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVoiceStatusAp.setStatus("current")
_MwVoiceStatusApName_Type = DisplayString
_MwVoiceStatusApName_Object = MibTableColumn
mwVoiceStatusApName = _MwVoiceStatusApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 3),
    _MwVoiceStatusApName_Type()
)
mwVoiceStatusApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVoiceStatusApName.setStatus("current")
_MwVoiceStatusPhoneCount_Type = Unsigned32
_MwVoiceStatusPhoneCount_Object = MibTableColumn
mwVoiceStatusPhoneCount = _MwVoiceStatusPhoneCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 4),
    _MwVoiceStatusPhoneCount_Type()
)
mwVoiceStatusPhoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVoiceStatusPhoneCount.setStatus("current")
_MwVoiceStatusRejectCount_Type = Counter64
_MwVoiceStatusRejectCount_Object = MibTableColumn
mwVoiceStatusRejectCount = _MwVoiceStatusRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 5),
    _MwVoiceStatusRejectCount_Type()
)
mwVoiceStatusRejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVoiceStatusRejectCount.setStatus("current")
_MwVoiceStatusActiveCallCount_Type = Unsigned32
_MwVoiceStatusActiveCallCount_Object = MibTableColumn
mwVoiceStatusActiveCallCount = _MwVoiceStatusActiveCallCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 6),
    _MwVoiceStatusActiveCallCount_Type()
)
mwVoiceStatusActiveCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVoiceStatusActiveCallCount.setStatus("current")
_MwVoiceStatusPendingCallCount_Type = Unsigned32
_MwVoiceStatusPendingCallCount_Object = MibTableColumn
mwVoiceStatusPendingCallCount = _MwVoiceStatusPendingCallCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 3, 3, 1, 7),
    _MwVoiceStatusPendingCallCount_Type()
)
mwVoiceStatusPendingCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVoiceStatusPendingCallCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-VOICE-STATISTICS-MIB",
    **{"mwVoiceStatistics": mwVoiceStatistics,
       "mwPhoneTable": mwPhoneTable,
       "mwPhoneEntry": mwPhoneEntry,
       "mwPhoneTableIndex": mwPhoneTableIndex,
       "mwPhoneIp": mwPhoneIp,
       "mwPhoneAp": mwPhoneAp,
       "mwPhoneMac": mwPhoneMac,
       "mwPhoneType": mwPhoneType,
       "mwPhoneApName": mwPhoneApName,
       "mwPhoneServer": mwPhoneServer,
       "mwPhoneUsername": mwPhoneUsername,
       "mwPhoneTransport": mwPhoneTransport,
       "mwPhoneDeviceType": mwPhoneDeviceType,
       "mwPhoneCallTable": mwPhoneCallTable,
       "mwPhoneCallEntry": mwPhoneCallEntry,
       "mwPhoneCallTableIndex": mwPhoneCallTableIndex,
       "mwPhoneCallToIp": mwPhoneCallToIp,
       "mwPhoneCallToAp": mwPhoneCallToAp,
       "mwPhoneCallType": mwPhoneCallType,
       "mwPhoneCallToMac": mwPhoneCallToMac,
       "mwPhoneCallState": mwPhoneCallState,
       "mwPhoneCallFromIp": mwPhoneCallFromIp,
       "mwPhoneCallFromAp": mwPhoneCallFromAp,
       "mwPhoneCallFromMac": mwPhoneCallFromMac,
       "mwPhoneCallToApName": mwPhoneCallToApName,
       "mwPhoneCallToFlowtag": mwPhoneCallToFlowtag,
       "mwPhoneCallToPending": mwPhoneCallToPending,
       "mwPhoneCallFromApName": mwPhoneCallFromApName,
       "mwPhoneCallToUsername": mwPhoneCallToUsername,
       "mwPhoneCallFromFlowtag": mwPhoneCallFromFlowtag,
       "mwPhoneCallFromPending": mwPhoneCallFromPending,
       "mwPhoneCallFromUsername": mwPhoneCallFromUsername,
       "mwVoiceStatusTable": mwVoiceStatusTable,
       "mwVoiceStatusEntry": mwVoiceStatusEntry,
       "mwVoiceStatusTableIndex": mwVoiceStatusTableIndex,
       "mwVoiceStatusAp": mwVoiceStatusAp,
       "mwVoiceStatusApName": mwVoiceStatusApName,
       "mwVoiceStatusPhoneCount": mwVoiceStatusPhoneCount,
       "mwVoiceStatusRejectCount": mwVoiceStatusRejectCount,
       "mwVoiceStatusActiveCallCount": mwVoiceStatusActiveCallCount,
       "mwVoiceStatusPendingCallCount": mwVoiceStatusPendingCallCount}
)
