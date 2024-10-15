# SNMP MIB module (CISCO-UNIFIED-COMPUTING-TRIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-TRIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:27 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsPolicyPolicyOwner,
 CucsTrigAdminState,
 CucsTrigDay,
 CucsTrigOperState,
 CucsTrigTokenOperState,
 CucsTrigTrigOperState,
 CucsTrigTriggeredState) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsPolicyPolicyOwner",
    "CucsTrigAdminState",
    "CucsTrigDay",
    "CucsTrigOperState",
    "CucsTrigTokenOperState",
    "CucsTrigTrigOperState",
    "CucsTrigTriggeredState")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsTrigObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsTrigAbsWindowTable_Object = MibTable
cucsTrigAbsWindowTable = _CucsTrigAbsWindowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1)
)
if mibBuilder.loadTexts:
    cucsTrigAbsWindowTable.setStatus("current")
_CucsTrigAbsWindowEntry_Object = MibTableRow
cucsTrigAbsWindowEntry = _CucsTrigAbsWindowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1)
)
cucsTrigAbsWindowEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigAbsWindowInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTrigAbsWindowEntry.setStatus("current")
_CucsTrigAbsWindowInstanceId_Type = CucsManagedObjectId
_CucsTrigAbsWindowInstanceId_Object = MibTableColumn
cucsTrigAbsWindowInstanceId = _CucsTrigAbsWindowInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 1),
    _CucsTrigAbsWindowInstanceId_Type()
)
cucsTrigAbsWindowInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowInstanceId.setStatus("current")
_CucsTrigAbsWindowDn_Type = CucsManagedObjectDn
_CucsTrigAbsWindowDn_Object = MibTableColumn
cucsTrigAbsWindowDn = _CucsTrigAbsWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 2),
    _CucsTrigAbsWindowDn_Type()
)
cucsTrigAbsWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowDn.setStatus("current")
_CucsTrigAbsWindowRn_Type = SnmpAdminString
_CucsTrigAbsWindowRn_Object = MibTableColumn
cucsTrigAbsWindowRn = _CucsTrigAbsWindowRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 3),
    _CucsTrigAbsWindowRn_Type()
)
cucsTrigAbsWindowRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowRn.setStatus("current")
_CucsTrigAbsWindowConcurCap_Type = Gauge32
_CucsTrigAbsWindowConcurCap_Object = MibTableColumn
cucsTrigAbsWindowConcurCap = _CucsTrigAbsWindowConcurCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 4),
    _CucsTrigAbsWindowConcurCap_Type()
)
cucsTrigAbsWindowConcurCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowConcurCap.setStatus("current")
_CucsTrigAbsWindowDate_Type = DateAndTime
_CucsTrigAbsWindowDate_Object = MibTableColumn
cucsTrigAbsWindowDate = _CucsTrigAbsWindowDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 5),
    _CucsTrigAbsWindowDate_Type()
)
cucsTrigAbsWindowDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowDate.setStatus("current")
_CucsTrigAbsWindowJobCount_Type = Gauge32
_CucsTrigAbsWindowJobCount_Object = MibTableColumn
cucsTrigAbsWindowJobCount = _CucsTrigAbsWindowJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 6),
    _CucsTrigAbsWindowJobCount_Type()
)
cucsTrigAbsWindowJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowJobCount.setStatus("current")
_CucsTrigAbsWindowName_Type = SnmpAdminString
_CucsTrigAbsWindowName_Object = MibTableColumn
cucsTrigAbsWindowName = _CucsTrigAbsWindowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 7),
    _CucsTrigAbsWindowName_Type()
)
cucsTrigAbsWindowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowName.setStatus("current")
_CucsTrigAbsWindowProcBreak_Type = SnmpAdminString
_CucsTrigAbsWindowProcBreak_Object = MibTableColumn
cucsTrigAbsWindowProcBreak = _CucsTrigAbsWindowProcBreak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 8),
    _CucsTrigAbsWindowProcBreak_Type()
)
cucsTrigAbsWindowProcBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowProcBreak.setStatus("current")
_CucsTrigAbsWindowProcCap_Type = Gauge32
_CucsTrigAbsWindowProcCap_Object = MibTableColumn
cucsTrigAbsWindowProcCap = _CucsTrigAbsWindowProcCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 9),
    _CucsTrigAbsWindowProcCap_Type()
)
cucsTrigAbsWindowProcCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowProcCap.setStatus("current")
_CucsTrigAbsWindowTimeCap_Type = SnmpAdminString
_CucsTrigAbsWindowTimeCap_Object = MibTableColumn
cucsTrigAbsWindowTimeCap = _CucsTrigAbsWindowTimeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 10),
    _CucsTrigAbsWindowTimeCap_Type()
)
cucsTrigAbsWindowTimeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowTimeCap.setStatus("current")
_CucsTrigAbsWindowTimeCapped_Type = TruthValue
_CucsTrigAbsWindowTimeCapped_Object = MibTableColumn
cucsTrigAbsWindowTimeCapped = _CucsTrigAbsWindowTimeCapped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 1, 1, 12),
    _CucsTrigAbsWindowTimeCapped_Type()
)
cucsTrigAbsWindowTimeCapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigAbsWindowTimeCapped.setStatus("current")
_CucsTrigMetaTable_Object = MibTable
cucsTrigMetaTable = _CucsTrigMetaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2)
)
if mibBuilder.loadTexts:
    cucsTrigMetaTable.setStatus("current")
_CucsTrigMetaEntry_Object = MibTableRow
cucsTrigMetaEntry = _CucsTrigMetaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1)
)
cucsTrigMetaEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigMetaInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTrigMetaEntry.setStatus("current")
_CucsTrigMetaInstanceId_Type = CucsManagedObjectId
_CucsTrigMetaInstanceId_Object = MibTableColumn
cucsTrigMetaInstanceId = _CucsTrigMetaInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 1),
    _CucsTrigMetaInstanceId_Type()
)
cucsTrigMetaInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTrigMetaInstanceId.setStatus("current")
_CucsTrigMetaDn_Type = CucsManagedObjectDn
_CucsTrigMetaDn_Object = MibTableColumn
cucsTrigMetaDn = _CucsTrigMetaDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 2),
    _CucsTrigMetaDn_Type()
)
cucsTrigMetaDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaDn.setStatus("current")
_CucsTrigMetaRn_Type = SnmpAdminString
_CucsTrigMetaRn_Object = MibTableColumn
cucsTrigMetaRn = _CucsTrigMetaRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 3),
    _CucsTrigMetaRn_Type()
)
cucsTrigMetaRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaRn.setStatus("current")
_CucsTrigMetaAdminState_Type = CucsTrigAdminState
_CucsTrigMetaAdminState_Object = MibTableColumn
cucsTrigMetaAdminState = _CucsTrigMetaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 4),
    _CucsTrigMetaAdminState_Type()
)
cucsTrigMetaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaAdminState.setStatus("current")
_CucsTrigMetaDescr_Type = SnmpAdminString
_CucsTrigMetaDescr_Object = MibTableColumn
cucsTrigMetaDescr = _CucsTrigMetaDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 5),
    _CucsTrigMetaDescr_Type()
)
cucsTrigMetaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaDescr.setStatus("current")
_CucsTrigMetaIntId_Type = SnmpAdminString
_CucsTrigMetaIntId_Object = MibTableColumn
cucsTrigMetaIntId = _CucsTrigMetaIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 6),
    _CucsTrigMetaIntId_Type()
)
cucsTrigMetaIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaIntId.setStatus("current")
_CucsTrigMetaJobCount_Type = Gauge32
_CucsTrigMetaJobCount_Object = MibTableColumn
cucsTrigMetaJobCount = _CucsTrigMetaJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 7),
    _CucsTrigMetaJobCount_Type()
)
cucsTrigMetaJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaJobCount.setStatus("current")
_CucsTrigMetaName_Type = SnmpAdminString
_CucsTrigMetaName_Object = MibTableColumn
cucsTrigMetaName = _CucsTrigMetaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 8),
    _CucsTrigMetaName_Type()
)
cucsTrigMetaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaName.setStatus("current")
_CucsTrigMetaOperState_Type = CucsTrigOperState
_CucsTrigMetaOperState_Object = MibTableColumn
cucsTrigMetaOperState = _CucsTrigMetaOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 9),
    _CucsTrigMetaOperState_Type()
)
cucsTrigMetaOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaOperState.setStatus("current")
_CucsTrigMetaSchedName_Type = SnmpAdminString
_CucsTrigMetaSchedName_Object = MibTableColumn
cucsTrigMetaSchedName = _CucsTrigMetaSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 10),
    _CucsTrigMetaSchedName_Type()
)
cucsTrigMetaSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaSchedName.setStatus("current")
_CucsTrigMetaTrigTime_Type = DateAndTime
_CucsTrigMetaTrigTime_Object = MibTableColumn
cucsTrigMetaTrigTime = _CucsTrigMetaTrigTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 11),
    _CucsTrigMetaTrigTime_Type()
)
cucsTrigMetaTrigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaTrigTime.setStatus("current")
_CucsTrigMetaWindowDn_Type = SnmpAdminString
_CucsTrigMetaWindowDn_Object = MibTableColumn
cucsTrigMetaWindowDn = _CucsTrigMetaWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 12),
    _CucsTrigMetaWindowDn_Type()
)
cucsTrigMetaWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaWindowDn.setStatus("current")
_CucsTrigMetaPolicyLevel_Type = Gauge32
_CucsTrigMetaPolicyLevel_Object = MibTableColumn
cucsTrigMetaPolicyLevel = _CucsTrigMetaPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 13),
    _CucsTrigMetaPolicyLevel_Type()
)
cucsTrigMetaPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaPolicyLevel.setStatus("current")
_CucsTrigMetaPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsTrigMetaPolicyOwner_Object = MibTableColumn
cucsTrigMetaPolicyOwner = _CucsTrigMetaPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 2, 1, 14),
    _CucsTrigMetaPolicyOwner_Type()
)
cucsTrigMetaPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigMetaPolicyOwner.setStatus("current")
_CucsTrigRecurrWindowTable_Object = MibTable
cucsTrigRecurrWindowTable = _CucsTrigRecurrWindowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3)
)
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowTable.setStatus("current")
_CucsTrigRecurrWindowEntry_Object = MibTableRow
cucsTrigRecurrWindowEntry = _CucsTrigRecurrWindowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1)
)
cucsTrigRecurrWindowEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigRecurrWindowInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowEntry.setStatus("current")
_CucsTrigRecurrWindowInstanceId_Type = CucsManagedObjectId
_CucsTrigRecurrWindowInstanceId_Object = MibTableColumn
cucsTrigRecurrWindowInstanceId = _CucsTrigRecurrWindowInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 1),
    _CucsTrigRecurrWindowInstanceId_Type()
)
cucsTrigRecurrWindowInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowInstanceId.setStatus("current")
_CucsTrigRecurrWindowDn_Type = CucsManagedObjectDn
_CucsTrigRecurrWindowDn_Object = MibTableColumn
cucsTrigRecurrWindowDn = _CucsTrigRecurrWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 2),
    _CucsTrigRecurrWindowDn_Type()
)
cucsTrigRecurrWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowDn.setStatus("current")
_CucsTrigRecurrWindowRn_Type = SnmpAdminString
_CucsTrigRecurrWindowRn_Object = MibTableColumn
cucsTrigRecurrWindowRn = _CucsTrigRecurrWindowRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 3),
    _CucsTrigRecurrWindowRn_Type()
)
cucsTrigRecurrWindowRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowRn.setStatus("current")
_CucsTrigRecurrWindowConcurCap_Type = Gauge32
_CucsTrigRecurrWindowConcurCap_Object = MibTableColumn
cucsTrigRecurrWindowConcurCap = _CucsTrigRecurrWindowConcurCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 4),
    _CucsTrigRecurrWindowConcurCap_Type()
)
cucsTrigRecurrWindowConcurCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowConcurCap.setStatus("current")
_CucsTrigRecurrWindowDay_Type = CucsTrigDay
_CucsTrigRecurrWindowDay_Object = MibTableColumn
cucsTrigRecurrWindowDay = _CucsTrigRecurrWindowDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 5),
    _CucsTrigRecurrWindowDay_Type()
)
cucsTrigRecurrWindowDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowDay.setStatus("current")
_CucsTrigRecurrWindowHour_Type = Gauge32
_CucsTrigRecurrWindowHour_Object = MibTableColumn
cucsTrigRecurrWindowHour = _CucsTrigRecurrWindowHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 6),
    _CucsTrigRecurrWindowHour_Type()
)
cucsTrigRecurrWindowHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowHour.setStatus("current")
_CucsTrigRecurrWindowJobCount_Type = Gauge32
_CucsTrigRecurrWindowJobCount_Object = MibTableColumn
cucsTrigRecurrWindowJobCount = _CucsTrigRecurrWindowJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 7),
    _CucsTrigRecurrWindowJobCount_Type()
)
cucsTrigRecurrWindowJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowJobCount.setStatus("current")
_CucsTrigRecurrWindowMinute_Type = Gauge32
_CucsTrigRecurrWindowMinute_Object = MibTableColumn
cucsTrigRecurrWindowMinute = _CucsTrigRecurrWindowMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 8),
    _CucsTrigRecurrWindowMinute_Type()
)
cucsTrigRecurrWindowMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowMinute.setStatus("current")
_CucsTrigRecurrWindowName_Type = SnmpAdminString
_CucsTrigRecurrWindowName_Object = MibTableColumn
cucsTrigRecurrWindowName = _CucsTrigRecurrWindowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 9),
    _CucsTrigRecurrWindowName_Type()
)
cucsTrigRecurrWindowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowName.setStatus("current")
_CucsTrigRecurrWindowProcBreak_Type = SnmpAdminString
_CucsTrigRecurrWindowProcBreak_Object = MibTableColumn
cucsTrigRecurrWindowProcBreak = _CucsTrigRecurrWindowProcBreak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 10),
    _CucsTrigRecurrWindowProcBreak_Type()
)
cucsTrigRecurrWindowProcBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowProcBreak.setStatus("current")
_CucsTrigRecurrWindowProcCap_Type = Gauge32
_CucsTrigRecurrWindowProcCap_Object = MibTableColumn
cucsTrigRecurrWindowProcCap = _CucsTrigRecurrWindowProcCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 11),
    _CucsTrigRecurrWindowProcCap_Type()
)
cucsTrigRecurrWindowProcCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowProcCap.setStatus("current")
_CucsTrigRecurrWindowTimeCap_Type = SnmpAdminString
_CucsTrigRecurrWindowTimeCap_Object = MibTableColumn
cucsTrigRecurrWindowTimeCap = _CucsTrigRecurrWindowTimeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 12),
    _CucsTrigRecurrWindowTimeCap_Type()
)
cucsTrigRecurrWindowTimeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowTimeCap.setStatus("current")
_CucsTrigRecurrWindowTimeCapped_Type = TruthValue
_CucsTrigRecurrWindowTimeCapped_Object = MibTableColumn
cucsTrigRecurrWindowTimeCapped = _CucsTrigRecurrWindowTimeCapped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 3, 1, 14),
    _CucsTrigRecurrWindowTimeCapped_Type()
)
cucsTrigRecurrWindowTimeCapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigRecurrWindowTimeCapped.setStatus("current")
_CucsTrigSchedTable_Object = MibTable
cucsTrigSchedTable = _CucsTrigSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4)
)
if mibBuilder.loadTexts:
    cucsTrigSchedTable.setStatus("current")
_CucsTrigSchedEntry_Object = MibTableRow
cucsTrigSchedEntry = _CucsTrigSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1)
)
cucsTrigSchedEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigSchedInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTrigSchedEntry.setStatus("current")
_CucsTrigSchedInstanceId_Type = CucsManagedObjectId
_CucsTrigSchedInstanceId_Object = MibTableColumn
cucsTrigSchedInstanceId = _CucsTrigSchedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 1),
    _CucsTrigSchedInstanceId_Type()
)
cucsTrigSchedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTrigSchedInstanceId.setStatus("current")
_CucsTrigSchedDn_Type = CucsManagedObjectDn
_CucsTrigSchedDn_Object = MibTableColumn
cucsTrigSchedDn = _CucsTrigSchedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 2),
    _CucsTrigSchedDn_Type()
)
cucsTrigSchedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigSchedDn.setStatus("current")
_CucsTrigSchedRn_Type = SnmpAdminString
_CucsTrigSchedRn_Object = MibTableColumn
cucsTrigSchedRn = _CucsTrigSchedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 3),
    _CucsTrigSchedRn_Type()
)
cucsTrigSchedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigSchedRn.setStatus("current")
_CucsTrigSchedAdminState_Type = CucsTrigAdminState
_CucsTrigSchedAdminState_Object = MibTableColumn
cucsTrigSchedAdminState = _CucsTrigSchedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 4),
    _CucsTrigSchedAdminState_Type()
)
cucsTrigSchedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigSchedAdminState.setStatus("current")
_CucsTrigSchedDescr_Type = SnmpAdminString
_CucsTrigSchedDescr_Object = MibTableColumn
cucsTrigSchedDescr = _CucsTrigSchedDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 5),
    _CucsTrigSchedDescr_Type()
)
cucsTrigSchedDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigSchedDescr.setStatus("current")
_CucsTrigSchedIntId_Type = SnmpAdminString
_CucsTrigSchedIntId_Object = MibTableColumn
cucsTrigSchedIntId = _CucsTrigSchedIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 6),
    _CucsTrigSchedIntId_Type()
)
cucsTrigSchedIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigSchedIntId.setStatus("current")
_CucsTrigSchedName_Type = SnmpAdminString
_CucsTrigSchedName_Object = MibTableColumn
cucsTrigSchedName = _CucsTrigSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 7),
    _CucsTrigSchedName_Type()
)
cucsTrigSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigSchedName.setStatus("current")
_CucsTrigSchedOperState_Type = CucsTrigOperState
_CucsTrigSchedOperState_Object = MibTableColumn
cucsTrigSchedOperState = _CucsTrigSchedOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 8),
    _CucsTrigSchedOperState_Type()
)
cucsTrigSchedOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigSchedOperState.setStatus("current")
_CucsTrigSchedFlgInitialActive_Type = TruthValue
_CucsTrigSchedFlgInitialActive_Object = MibTableColumn
cucsTrigSchedFlgInitialActive = _CucsTrigSchedFlgInitialActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 9),
    _CucsTrigSchedFlgInitialActive_Type()
)
cucsTrigSchedFlgInitialActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigSchedFlgInitialActive.setStatus("current")
_CucsTrigSchedPolicyLevel_Type = Gauge32
_CucsTrigSchedPolicyLevel_Object = MibTableColumn
cucsTrigSchedPolicyLevel = _CucsTrigSchedPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 10),
    _CucsTrigSchedPolicyLevel_Type()
)
cucsTrigSchedPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigSchedPolicyLevel.setStatus("current")
_CucsTrigSchedPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsTrigSchedPolicyOwner_Object = MibTableColumn
cucsTrigSchedPolicyOwner = _CucsTrigSchedPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 4, 1, 11),
    _CucsTrigSchedPolicyOwner_Type()
)
cucsTrigSchedPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigSchedPolicyOwner.setStatus("current")
_CucsTrigTestTable_Object = MibTable
cucsTrigTestTable = _CucsTrigTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5)
)
if mibBuilder.loadTexts:
    cucsTrigTestTable.setStatus("current")
_CucsTrigTestEntry_Object = MibTableRow
cucsTrigTestEntry = _CucsTrigTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1)
)
cucsTrigTestEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigTestInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTrigTestEntry.setStatus("current")
_CucsTrigTestInstanceId_Type = CucsManagedObjectId
_CucsTrigTestInstanceId_Object = MibTableColumn
cucsTrigTestInstanceId = _CucsTrigTestInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 1),
    _CucsTrigTestInstanceId_Type()
)
cucsTrigTestInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTrigTestInstanceId.setStatus("current")
_CucsTrigTestDn_Type = CucsManagedObjectDn
_CucsTrigTestDn_Object = MibTableColumn
cucsTrigTestDn = _CucsTrigTestDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 2),
    _CucsTrigTestDn_Type()
)
cucsTrigTestDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestDn.setStatus("current")
_CucsTrigTestRn_Type = SnmpAdminString
_CucsTrigTestRn_Object = MibTableColumn
cucsTrigTestRn = _CucsTrigTestRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 3),
    _CucsTrigTestRn_Type()
)
cucsTrigTestRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestRn.setStatus("current")
_CucsTrigTestAdminState_Type = CucsTrigAdminState
_CucsTrigTestAdminState_Object = MibTableColumn
cucsTrigTestAdminState = _CucsTrigTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 4),
    _CucsTrigTestAdminState_Type()
)
cucsTrigTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestAdminState.setStatus("current")
_CucsTrigTestCreationDate_Type = DateAndTime
_CucsTrigTestCreationDate_Object = MibTableColumn
cucsTrigTestCreationDate = _CucsTrigTestCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 5),
    _CucsTrigTestCreationDate_Type()
)
cucsTrigTestCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestCreationDate.setStatus("current")
_CucsTrigTestDescr_Type = SnmpAdminString
_CucsTrigTestDescr_Object = MibTableColumn
cucsTrigTestDescr = _CucsTrigTestDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 6),
    _CucsTrigTestDescr_Type()
)
cucsTrigTestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestDescr.setStatus("current")
_CucsTrigTestIntId_Type = SnmpAdminString
_CucsTrigTestIntId_Object = MibTableColumn
cucsTrigTestIntId = _CucsTrigTestIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 7),
    _CucsTrigTestIntId_Type()
)
cucsTrigTestIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestIntId.setStatus("current")
_CucsTrigTestName_Type = SnmpAdminString
_CucsTrigTestName_Object = MibTableColumn
cucsTrigTestName = _CucsTrigTestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 8),
    _CucsTrigTestName_Type()
)
cucsTrigTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestName.setStatus("current")
_CucsTrigTestScheduler_Type = SnmpAdminString
_CucsTrigTestScheduler_Object = MibTableColumn
cucsTrigTestScheduler = _CucsTrigTestScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 9),
    _CucsTrigTestScheduler_Type()
)
cucsTrigTestScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestScheduler.setStatus("current")
_CucsTrigTestAutoDelete_Type = TruthValue
_CucsTrigTestAutoDelete_Object = MibTableColumn
cucsTrigTestAutoDelete = _CucsTrigTestAutoDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 10),
    _CucsTrigTestAutoDelete_Type()
)
cucsTrigTestAutoDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestAutoDelete.setStatus("current")
_CucsTrigTestIgnoreCap_Type = TruthValue
_CucsTrigTestIgnoreCap_Object = MibTableColumn
cucsTrigTestIgnoreCap = _CucsTrigTestIgnoreCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 11),
    _CucsTrigTestIgnoreCap_Type()
)
cucsTrigTestIgnoreCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestIgnoreCap.setStatus("current")
_CucsTrigTestOperScheduler_Type = SnmpAdminString
_CucsTrigTestOperScheduler_Object = MibTableColumn
cucsTrigTestOperScheduler = _CucsTrigTestOperScheduler_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 12),
    _CucsTrigTestOperScheduler_Type()
)
cucsTrigTestOperScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestOperScheduler.setStatus("current")
_CucsTrigTestOperState_Type = CucsTrigTrigOperState
_CucsTrigTestOperState_Object = MibTableColumn
cucsTrigTestOperState = _CucsTrigTestOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 13),
    _CucsTrigTestOperState_Type()
)
cucsTrigTestOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestOperState.setStatus("current")
_CucsTrigTestPolicyLevel_Type = Gauge32
_CucsTrigTestPolicyLevel_Object = MibTableColumn
cucsTrigTestPolicyLevel = _CucsTrigTestPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 14),
    _CucsTrigTestPolicyLevel_Type()
)
cucsTrigTestPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestPolicyLevel.setStatus("current")
_CucsTrigTestPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsTrigTestPolicyOwner_Object = MibTableColumn
cucsTrigTestPolicyOwner = _CucsTrigTestPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 5, 1, 15),
    _CucsTrigTestPolicyOwner_Type()
)
cucsTrigTestPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTestPolicyOwner.setStatus("current")
_CucsTrigTriggeredTable_Object = MibTable
cucsTrigTriggeredTable = _CucsTrigTriggeredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6)
)
if mibBuilder.loadTexts:
    cucsTrigTriggeredTable.setStatus("current")
_CucsTrigTriggeredEntry_Object = MibTableRow
cucsTrigTriggeredEntry = _CucsTrigTriggeredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1)
)
cucsTrigTriggeredEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigTriggeredInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTrigTriggeredEntry.setStatus("current")
_CucsTrigTriggeredInstanceId_Type = CucsManagedObjectId
_CucsTrigTriggeredInstanceId_Object = MibTableColumn
cucsTrigTriggeredInstanceId = _CucsTrigTriggeredInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 1),
    _CucsTrigTriggeredInstanceId_Type()
)
cucsTrigTriggeredInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTrigTriggeredInstanceId.setStatus("current")
_CucsTrigTriggeredDn_Type = CucsManagedObjectDn
_CucsTrigTriggeredDn_Object = MibTableColumn
cucsTrigTriggeredDn = _CucsTrigTriggeredDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 2),
    _CucsTrigTriggeredDn_Type()
)
cucsTrigTriggeredDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTriggeredDn.setStatus("current")
_CucsTrigTriggeredRn_Type = SnmpAdminString
_CucsTrigTriggeredRn_Object = MibTableColumn
cucsTrigTriggeredRn = _CucsTrigTriggeredRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 3),
    _CucsTrigTriggeredRn_Type()
)
cucsTrigTriggeredRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTriggeredRn.setStatus("current")
_CucsTrigTriggeredJobCount_Type = Gauge32
_CucsTrigTriggeredJobCount_Object = MibTableColumn
cucsTrigTriggeredJobCount = _CucsTrigTriggeredJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 4),
    _CucsTrigTriggeredJobCount_Type()
)
cucsTrigTriggeredJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTriggeredJobCount.setStatus("current")
_CucsTrigTriggeredOperState_Type = CucsTrigTriggeredState
_CucsTrigTriggeredOperState_Object = MibTableColumn
cucsTrigTriggeredOperState = _CucsTrigTriggeredOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 5),
    _CucsTrigTriggeredOperState_Type()
)
cucsTrigTriggeredOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTriggeredOperState.setStatus("current")
_CucsTrigTriggeredOrder_Type = Gauge32
_CucsTrigTriggeredOrder_Object = MibTableColumn
cucsTrigTriggeredOrder = _CucsTrigTriggeredOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 6),
    _CucsTrigTriggeredOrder_Type()
)
cucsTrigTriggeredOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTriggeredOrder.setStatus("current")
_CucsTrigTriggeredTrDn_Type = SnmpAdminString
_CucsTrigTriggeredTrDn_Object = MibTableColumn
cucsTrigTriggeredTrDn = _CucsTrigTriggeredTrDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 7),
    _CucsTrigTriggeredTrDn_Type()
)
cucsTrigTriggeredTrDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTriggeredTrDn.setStatus("current")
_CucsTrigTriggeredTrId_Type = Gauge32
_CucsTrigTriggeredTrId_Object = MibTableColumn
cucsTrigTriggeredTrId = _CucsTrigTriggeredTrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 6, 1, 8),
    _CucsTrigTriggeredTrId_Type()
)
cucsTrigTriggeredTrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigTriggeredTrId.setStatus("current")
_CucsTrigClientTokenTable_Object = MibTable
cucsTrigClientTokenTable = _CucsTrigClientTokenTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7)
)
if mibBuilder.loadTexts:
    cucsTrigClientTokenTable.setStatus("current")
_CucsTrigClientTokenEntry_Object = MibTableRow
cucsTrigClientTokenEntry = _CucsTrigClientTokenEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1)
)
cucsTrigClientTokenEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigClientTokenInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTrigClientTokenEntry.setStatus("current")
_CucsTrigClientTokenInstanceId_Type = CucsManagedObjectId
_CucsTrigClientTokenInstanceId_Object = MibTableColumn
cucsTrigClientTokenInstanceId = _CucsTrigClientTokenInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 1),
    _CucsTrigClientTokenInstanceId_Type()
)
cucsTrigClientTokenInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTrigClientTokenInstanceId.setStatus("current")
_CucsTrigClientTokenDn_Type = CucsManagedObjectDn
_CucsTrigClientTokenDn_Object = MibTableColumn
cucsTrigClientTokenDn = _CucsTrigClientTokenDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 2),
    _CucsTrigClientTokenDn_Type()
)
cucsTrigClientTokenDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigClientTokenDn.setStatus("current")
_CucsTrigClientTokenRn_Type = SnmpAdminString
_CucsTrigClientTokenRn_Object = MibTableColumn
cucsTrigClientTokenRn = _CucsTrigClientTokenRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 3),
    _CucsTrigClientTokenRn_Type()
)
cucsTrigClientTokenRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigClientTokenRn.setStatus("current")
_CucsTrigClientTokenActivityTs_Type = DateAndTime
_CucsTrigClientTokenActivityTs_Object = MibTableColumn
cucsTrigClientTokenActivityTs = _CucsTrigClientTokenActivityTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 4),
    _CucsTrigClientTokenActivityTs_Type()
)
cucsTrigClientTokenActivityTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigClientTokenActivityTs.setStatus("current")
_CucsTrigClientTokenId_Type = Unsigned64
_CucsTrigClientTokenId_Object = MibTableColumn
cucsTrigClientTokenId = _CucsTrigClientTokenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 5),
    _CucsTrigClientTokenId_Type()
)
cucsTrigClientTokenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigClientTokenId.setStatus("current")
_CucsTrigClientTokenOperState_Type = CucsTrigTokenOperState
_CucsTrigClientTokenOperState_Object = MibTableColumn
cucsTrigClientTokenOperState = _CucsTrigClientTokenOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 7, 1, 6),
    _CucsTrigClientTokenOperState_Type()
)
cucsTrigClientTokenOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigClientTokenOperState.setStatus("current")
_CucsTrigLocalAbsWindowTable_Object = MibTable
cucsTrigLocalAbsWindowTable = _CucsTrigLocalAbsWindowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8)
)
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowTable.setStatus("current")
_CucsTrigLocalAbsWindowEntry_Object = MibTableRow
cucsTrigLocalAbsWindowEntry = _CucsTrigLocalAbsWindowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1)
)
cucsTrigLocalAbsWindowEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigLocalAbsWindowInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowEntry.setStatus("current")
_CucsTrigLocalAbsWindowInstanceId_Type = CucsManagedObjectId
_CucsTrigLocalAbsWindowInstanceId_Object = MibTableColumn
cucsTrigLocalAbsWindowInstanceId = _CucsTrigLocalAbsWindowInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 1),
    _CucsTrigLocalAbsWindowInstanceId_Type()
)
cucsTrigLocalAbsWindowInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowInstanceId.setStatus("current")
_CucsTrigLocalAbsWindowDn_Type = CucsManagedObjectDn
_CucsTrigLocalAbsWindowDn_Object = MibTableColumn
cucsTrigLocalAbsWindowDn = _CucsTrigLocalAbsWindowDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 2),
    _CucsTrigLocalAbsWindowDn_Type()
)
cucsTrigLocalAbsWindowDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowDn.setStatus("current")
_CucsTrigLocalAbsWindowRn_Type = SnmpAdminString
_CucsTrigLocalAbsWindowRn_Object = MibTableColumn
cucsTrigLocalAbsWindowRn = _CucsTrigLocalAbsWindowRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 3),
    _CucsTrigLocalAbsWindowRn_Type()
)
cucsTrigLocalAbsWindowRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowRn.setStatus("current")
_CucsTrigLocalAbsWindowConcurCap_Type = Gauge32
_CucsTrigLocalAbsWindowConcurCap_Object = MibTableColumn
cucsTrigLocalAbsWindowConcurCap = _CucsTrigLocalAbsWindowConcurCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 4),
    _CucsTrigLocalAbsWindowConcurCap_Type()
)
cucsTrigLocalAbsWindowConcurCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowConcurCap.setStatus("current")
_CucsTrigLocalAbsWindowDate_Type = DateAndTime
_CucsTrigLocalAbsWindowDate_Object = MibTableColumn
cucsTrigLocalAbsWindowDate = _CucsTrigLocalAbsWindowDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 5),
    _CucsTrigLocalAbsWindowDate_Type()
)
cucsTrigLocalAbsWindowDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowDate.setStatus("current")
_CucsTrigLocalAbsWindowJobCount_Type = Gauge32
_CucsTrigLocalAbsWindowJobCount_Object = MibTableColumn
cucsTrigLocalAbsWindowJobCount = _CucsTrigLocalAbsWindowJobCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 6),
    _CucsTrigLocalAbsWindowJobCount_Type()
)
cucsTrigLocalAbsWindowJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowJobCount.setStatus("current")
_CucsTrigLocalAbsWindowName_Type = SnmpAdminString
_CucsTrigLocalAbsWindowName_Object = MibTableColumn
cucsTrigLocalAbsWindowName = _CucsTrigLocalAbsWindowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 7),
    _CucsTrigLocalAbsWindowName_Type()
)
cucsTrigLocalAbsWindowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowName.setStatus("current")
_CucsTrigLocalAbsWindowProcBreak_Type = SnmpAdminString
_CucsTrigLocalAbsWindowProcBreak_Object = MibTableColumn
cucsTrigLocalAbsWindowProcBreak = _CucsTrigLocalAbsWindowProcBreak_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 8),
    _CucsTrigLocalAbsWindowProcBreak_Type()
)
cucsTrigLocalAbsWindowProcBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowProcBreak.setStatus("current")
_CucsTrigLocalAbsWindowProcCap_Type = Gauge32
_CucsTrigLocalAbsWindowProcCap_Object = MibTableColumn
cucsTrigLocalAbsWindowProcCap = _CucsTrigLocalAbsWindowProcCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 9),
    _CucsTrigLocalAbsWindowProcCap_Type()
)
cucsTrigLocalAbsWindowProcCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowProcCap.setStatus("current")
_CucsTrigLocalAbsWindowTimeCap_Type = SnmpAdminString
_CucsTrigLocalAbsWindowTimeCap_Object = MibTableColumn
cucsTrigLocalAbsWindowTimeCap = _CucsTrigLocalAbsWindowTimeCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 10),
    _CucsTrigLocalAbsWindowTimeCap_Type()
)
cucsTrigLocalAbsWindowTimeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowTimeCap.setStatus("current")
_CucsTrigLocalAbsWindowTimeCapped_Type = TruthValue
_CucsTrigLocalAbsWindowTimeCapped_Object = MibTableColumn
cucsTrigLocalAbsWindowTimeCapped = _CucsTrigLocalAbsWindowTimeCapped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 8, 1, 12),
    _CucsTrigLocalAbsWindowTimeCapped_Type()
)
cucsTrigLocalAbsWindowTimeCapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalAbsWindowTimeCapped.setStatus("current")
_CucsTrigLocalSchedTable_Object = MibTable
cucsTrigLocalSchedTable = _CucsTrigLocalSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9)
)
if mibBuilder.loadTexts:
    cucsTrigLocalSchedTable.setStatus("current")
_CucsTrigLocalSchedEntry_Object = MibTableRow
cucsTrigLocalSchedEntry = _CucsTrigLocalSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1)
)
cucsTrigLocalSchedEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-TRIG-MIB", "cucsTrigLocalSchedInstanceId"),
)
if mibBuilder.loadTexts:
    cucsTrigLocalSchedEntry.setStatus("current")
_CucsTrigLocalSchedInstanceId_Type = CucsManagedObjectId
_CucsTrigLocalSchedInstanceId_Object = MibTableColumn
cucsTrigLocalSchedInstanceId = _CucsTrigLocalSchedInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 1),
    _CucsTrigLocalSchedInstanceId_Type()
)
cucsTrigLocalSchedInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedInstanceId.setStatus("current")
_CucsTrigLocalSchedDn_Type = CucsManagedObjectDn
_CucsTrigLocalSchedDn_Object = MibTableColumn
cucsTrigLocalSchedDn = _CucsTrigLocalSchedDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 2),
    _CucsTrigLocalSchedDn_Type()
)
cucsTrigLocalSchedDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedDn.setStatus("current")
_CucsTrigLocalSchedRn_Type = SnmpAdminString
_CucsTrigLocalSchedRn_Object = MibTableColumn
cucsTrigLocalSchedRn = _CucsTrigLocalSchedRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 3),
    _CucsTrigLocalSchedRn_Type()
)
cucsTrigLocalSchedRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedRn.setStatus("current")
_CucsTrigLocalSchedAdminState_Type = CucsTrigAdminState
_CucsTrigLocalSchedAdminState_Object = MibTableColumn
cucsTrigLocalSchedAdminState = _CucsTrigLocalSchedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 4),
    _CucsTrigLocalSchedAdminState_Type()
)
cucsTrigLocalSchedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedAdminState.setStatus("current")
_CucsTrigLocalSchedDescr_Type = SnmpAdminString
_CucsTrigLocalSchedDescr_Object = MibTableColumn
cucsTrigLocalSchedDescr = _CucsTrigLocalSchedDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 5),
    _CucsTrigLocalSchedDescr_Type()
)
cucsTrigLocalSchedDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedDescr.setStatus("current")
_CucsTrigLocalSchedFlgInitialActive_Type = TruthValue
_CucsTrigLocalSchedFlgInitialActive_Object = MibTableColumn
cucsTrigLocalSchedFlgInitialActive = _CucsTrigLocalSchedFlgInitialActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 6),
    _CucsTrigLocalSchedFlgInitialActive_Type()
)
cucsTrigLocalSchedFlgInitialActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedFlgInitialActive.setStatus("current")
_CucsTrigLocalSchedIntId_Type = SnmpAdminString
_CucsTrigLocalSchedIntId_Object = MibTableColumn
cucsTrigLocalSchedIntId = _CucsTrigLocalSchedIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 7),
    _CucsTrigLocalSchedIntId_Type()
)
cucsTrigLocalSchedIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedIntId.setStatus("current")
_CucsTrigLocalSchedName_Type = SnmpAdminString
_CucsTrigLocalSchedName_Object = MibTableColumn
cucsTrigLocalSchedName = _CucsTrigLocalSchedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 8),
    _CucsTrigLocalSchedName_Type()
)
cucsTrigLocalSchedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedName.setStatus("current")
_CucsTrigLocalSchedOperState_Type = CucsTrigOperState
_CucsTrigLocalSchedOperState_Object = MibTableColumn
cucsTrigLocalSchedOperState = _CucsTrigLocalSchedOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 9),
    _CucsTrigLocalSchedOperState_Type()
)
cucsTrigLocalSchedOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedOperState.setStatus("current")
_CucsTrigLocalSchedPolicyLevel_Type = Gauge32
_CucsTrigLocalSchedPolicyLevel_Object = MibTableColumn
cucsTrigLocalSchedPolicyLevel = _CucsTrigLocalSchedPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 10),
    _CucsTrigLocalSchedPolicyLevel_Type()
)
cucsTrigLocalSchedPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedPolicyLevel.setStatus("current")
_CucsTrigLocalSchedPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsTrigLocalSchedPolicyOwner_Object = MibTableColumn
cucsTrigLocalSchedPolicyOwner = _CucsTrigLocalSchedPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 50, 9, 1, 11),
    _CucsTrigLocalSchedPolicyOwner_Type()
)
cucsTrigLocalSchedPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsTrigLocalSchedPolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-TRIG-MIB",
    **{"cucsTrigObjects": cucsTrigObjects,
       "cucsTrigAbsWindowTable": cucsTrigAbsWindowTable,
       "cucsTrigAbsWindowEntry": cucsTrigAbsWindowEntry,
       "cucsTrigAbsWindowInstanceId": cucsTrigAbsWindowInstanceId,
       "cucsTrigAbsWindowDn": cucsTrigAbsWindowDn,
       "cucsTrigAbsWindowRn": cucsTrigAbsWindowRn,
       "cucsTrigAbsWindowConcurCap": cucsTrigAbsWindowConcurCap,
       "cucsTrigAbsWindowDate": cucsTrigAbsWindowDate,
       "cucsTrigAbsWindowJobCount": cucsTrigAbsWindowJobCount,
       "cucsTrigAbsWindowName": cucsTrigAbsWindowName,
       "cucsTrigAbsWindowProcBreak": cucsTrigAbsWindowProcBreak,
       "cucsTrigAbsWindowProcCap": cucsTrigAbsWindowProcCap,
       "cucsTrigAbsWindowTimeCap": cucsTrigAbsWindowTimeCap,
       "cucsTrigAbsWindowTimeCapped": cucsTrigAbsWindowTimeCapped,
       "cucsTrigMetaTable": cucsTrigMetaTable,
       "cucsTrigMetaEntry": cucsTrigMetaEntry,
       "cucsTrigMetaInstanceId": cucsTrigMetaInstanceId,
       "cucsTrigMetaDn": cucsTrigMetaDn,
       "cucsTrigMetaRn": cucsTrigMetaRn,
       "cucsTrigMetaAdminState": cucsTrigMetaAdminState,
       "cucsTrigMetaDescr": cucsTrigMetaDescr,
       "cucsTrigMetaIntId": cucsTrigMetaIntId,
       "cucsTrigMetaJobCount": cucsTrigMetaJobCount,
       "cucsTrigMetaName": cucsTrigMetaName,
       "cucsTrigMetaOperState": cucsTrigMetaOperState,
       "cucsTrigMetaSchedName": cucsTrigMetaSchedName,
       "cucsTrigMetaTrigTime": cucsTrigMetaTrigTime,
       "cucsTrigMetaWindowDn": cucsTrigMetaWindowDn,
       "cucsTrigMetaPolicyLevel": cucsTrigMetaPolicyLevel,
       "cucsTrigMetaPolicyOwner": cucsTrigMetaPolicyOwner,
       "cucsTrigRecurrWindowTable": cucsTrigRecurrWindowTable,
       "cucsTrigRecurrWindowEntry": cucsTrigRecurrWindowEntry,
       "cucsTrigRecurrWindowInstanceId": cucsTrigRecurrWindowInstanceId,
       "cucsTrigRecurrWindowDn": cucsTrigRecurrWindowDn,
       "cucsTrigRecurrWindowRn": cucsTrigRecurrWindowRn,
       "cucsTrigRecurrWindowConcurCap": cucsTrigRecurrWindowConcurCap,
       "cucsTrigRecurrWindowDay": cucsTrigRecurrWindowDay,
       "cucsTrigRecurrWindowHour": cucsTrigRecurrWindowHour,
       "cucsTrigRecurrWindowJobCount": cucsTrigRecurrWindowJobCount,
       "cucsTrigRecurrWindowMinute": cucsTrigRecurrWindowMinute,
       "cucsTrigRecurrWindowName": cucsTrigRecurrWindowName,
       "cucsTrigRecurrWindowProcBreak": cucsTrigRecurrWindowProcBreak,
       "cucsTrigRecurrWindowProcCap": cucsTrigRecurrWindowProcCap,
       "cucsTrigRecurrWindowTimeCap": cucsTrigRecurrWindowTimeCap,
       "cucsTrigRecurrWindowTimeCapped": cucsTrigRecurrWindowTimeCapped,
       "cucsTrigSchedTable": cucsTrigSchedTable,
       "cucsTrigSchedEntry": cucsTrigSchedEntry,
       "cucsTrigSchedInstanceId": cucsTrigSchedInstanceId,
       "cucsTrigSchedDn": cucsTrigSchedDn,
       "cucsTrigSchedRn": cucsTrigSchedRn,
       "cucsTrigSchedAdminState": cucsTrigSchedAdminState,
       "cucsTrigSchedDescr": cucsTrigSchedDescr,
       "cucsTrigSchedIntId": cucsTrigSchedIntId,
       "cucsTrigSchedName": cucsTrigSchedName,
       "cucsTrigSchedOperState": cucsTrigSchedOperState,
       "cucsTrigSchedFlgInitialActive": cucsTrigSchedFlgInitialActive,
       "cucsTrigSchedPolicyLevel": cucsTrigSchedPolicyLevel,
       "cucsTrigSchedPolicyOwner": cucsTrigSchedPolicyOwner,
       "cucsTrigTestTable": cucsTrigTestTable,
       "cucsTrigTestEntry": cucsTrigTestEntry,
       "cucsTrigTestInstanceId": cucsTrigTestInstanceId,
       "cucsTrigTestDn": cucsTrigTestDn,
       "cucsTrigTestRn": cucsTrigTestRn,
       "cucsTrigTestAdminState": cucsTrigTestAdminState,
       "cucsTrigTestCreationDate": cucsTrigTestCreationDate,
       "cucsTrigTestDescr": cucsTrigTestDescr,
       "cucsTrigTestIntId": cucsTrigTestIntId,
       "cucsTrigTestName": cucsTrigTestName,
       "cucsTrigTestScheduler": cucsTrigTestScheduler,
       "cucsTrigTestAutoDelete": cucsTrigTestAutoDelete,
       "cucsTrigTestIgnoreCap": cucsTrigTestIgnoreCap,
       "cucsTrigTestOperScheduler": cucsTrigTestOperScheduler,
       "cucsTrigTestOperState": cucsTrigTestOperState,
       "cucsTrigTestPolicyLevel": cucsTrigTestPolicyLevel,
       "cucsTrigTestPolicyOwner": cucsTrigTestPolicyOwner,
       "cucsTrigTriggeredTable": cucsTrigTriggeredTable,
       "cucsTrigTriggeredEntry": cucsTrigTriggeredEntry,
       "cucsTrigTriggeredInstanceId": cucsTrigTriggeredInstanceId,
       "cucsTrigTriggeredDn": cucsTrigTriggeredDn,
       "cucsTrigTriggeredRn": cucsTrigTriggeredRn,
       "cucsTrigTriggeredJobCount": cucsTrigTriggeredJobCount,
       "cucsTrigTriggeredOperState": cucsTrigTriggeredOperState,
       "cucsTrigTriggeredOrder": cucsTrigTriggeredOrder,
       "cucsTrigTriggeredTrDn": cucsTrigTriggeredTrDn,
       "cucsTrigTriggeredTrId": cucsTrigTriggeredTrId,
       "cucsTrigClientTokenTable": cucsTrigClientTokenTable,
       "cucsTrigClientTokenEntry": cucsTrigClientTokenEntry,
       "cucsTrigClientTokenInstanceId": cucsTrigClientTokenInstanceId,
       "cucsTrigClientTokenDn": cucsTrigClientTokenDn,
       "cucsTrigClientTokenRn": cucsTrigClientTokenRn,
       "cucsTrigClientTokenActivityTs": cucsTrigClientTokenActivityTs,
       "cucsTrigClientTokenId": cucsTrigClientTokenId,
       "cucsTrigClientTokenOperState": cucsTrigClientTokenOperState,
       "cucsTrigLocalAbsWindowTable": cucsTrigLocalAbsWindowTable,
       "cucsTrigLocalAbsWindowEntry": cucsTrigLocalAbsWindowEntry,
       "cucsTrigLocalAbsWindowInstanceId": cucsTrigLocalAbsWindowInstanceId,
       "cucsTrigLocalAbsWindowDn": cucsTrigLocalAbsWindowDn,
       "cucsTrigLocalAbsWindowRn": cucsTrigLocalAbsWindowRn,
       "cucsTrigLocalAbsWindowConcurCap": cucsTrigLocalAbsWindowConcurCap,
       "cucsTrigLocalAbsWindowDate": cucsTrigLocalAbsWindowDate,
       "cucsTrigLocalAbsWindowJobCount": cucsTrigLocalAbsWindowJobCount,
       "cucsTrigLocalAbsWindowName": cucsTrigLocalAbsWindowName,
       "cucsTrigLocalAbsWindowProcBreak": cucsTrigLocalAbsWindowProcBreak,
       "cucsTrigLocalAbsWindowProcCap": cucsTrigLocalAbsWindowProcCap,
       "cucsTrigLocalAbsWindowTimeCap": cucsTrigLocalAbsWindowTimeCap,
       "cucsTrigLocalAbsWindowTimeCapped": cucsTrigLocalAbsWindowTimeCapped,
       "cucsTrigLocalSchedTable": cucsTrigLocalSchedTable,
       "cucsTrigLocalSchedEntry": cucsTrigLocalSchedEntry,
       "cucsTrigLocalSchedInstanceId": cucsTrigLocalSchedInstanceId,
       "cucsTrigLocalSchedDn": cucsTrigLocalSchedDn,
       "cucsTrigLocalSchedRn": cucsTrigLocalSchedRn,
       "cucsTrigLocalSchedAdminState": cucsTrigLocalSchedAdminState,
       "cucsTrigLocalSchedDescr": cucsTrigLocalSchedDescr,
       "cucsTrigLocalSchedFlgInitialActive": cucsTrigLocalSchedFlgInitialActive,
       "cucsTrigLocalSchedIntId": cucsTrigLocalSchedIntId,
       "cucsTrigLocalSchedName": cucsTrigLocalSchedName,
       "cucsTrigLocalSchedOperState": cucsTrigLocalSchedOperState,
       "cucsTrigLocalSchedPolicyLevel": cucsTrigLocalSchedPolicyLevel,
       "cucsTrigLocalSchedPolicyOwner": cucsTrigLocalSchedPolicyOwner}
)
