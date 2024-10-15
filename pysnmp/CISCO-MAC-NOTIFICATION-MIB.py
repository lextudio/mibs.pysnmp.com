# SNMP MIB module (CISCO-MAC-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MAC-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:13 2024
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

(Percent,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Percent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DisplayString,
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoMacNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215)
)
ciscoMacNotificationMIB.setRevisions(
        ("2007-06-11 00:00",
         "2003-03-21 00:00",
         "2001-10-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMacNotificationMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMacNotificationMIBObjects = _CiscoMacNotificationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1)
)
_CmnGlobalObjects_ObjectIdentity = ObjectIdentity
cmnGlobalObjects = _CmnGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1)
)
_CmnGlobalFeatureEnabled_Type = TruthValue
_CmnGlobalFeatureEnabled_Object = MibScalar
cmnGlobalFeatureEnabled = _CmnGlobalFeatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 1),
    _CmnGlobalFeatureEnabled_Type()
)
cmnGlobalFeatureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnGlobalFeatureEnabled.setStatus("current")


class _CmnNotificationInterval_Type(Unsigned32):
    """Custom type cmnNotificationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CmnNotificationInterval_Type.__name__ = "Unsigned32"
_CmnNotificationInterval_Object = MibScalar
cmnNotificationInterval = _CmnNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 2),
    _CmnNotificationInterval_Type()
)
cmnNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmnNotificationInterval.setUnits("seconds")
_CmnMacAddressesLearnt_Type = Counter32
_CmnMacAddressesLearnt_Object = MibScalar
cmnMacAddressesLearnt = _CmnMacAddressesLearnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 3),
    _CmnMacAddressesLearnt_Type()
)
cmnMacAddressesLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnMacAddressesLearnt.setStatus("current")
_CmnMacAddressesRemoved_Type = Counter32
_CmnMacAddressesRemoved_Object = MibScalar
cmnMacAddressesRemoved = _CmnMacAddressesRemoved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 4),
    _CmnMacAddressesRemoved_Type()
)
cmnMacAddressesRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnMacAddressesRemoved.setStatus("current")


class _CmnNotificationsEnabled_Type(TruthValue):
    """Custom type cmnNotificationsEnabled based on TruthValue"""


_CmnNotificationsEnabled_Object = MibScalar
cmnNotificationsEnabled = _CmnNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 5),
    _CmnNotificationsEnabled_Type()
)
cmnNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnNotificationsEnabled.setStatus("current")
_CmnNotificationsSent_Type = Counter32
_CmnNotificationsSent_Object = MibScalar
cmnNotificationsSent = _CmnNotificationsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 6),
    _CmnNotificationsSent_Type()
)
cmnNotificationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnNotificationsSent.setStatus("current")


class _CmnHistTableMaxLength_Type(Unsigned32):
    """Custom type cmnHistTableMaxLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CmnHistTableMaxLength_Type.__name__ = "Unsigned32"
_CmnHistTableMaxLength_Object = MibScalar
cmnHistTableMaxLength = _CmnHistTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 7),
    _CmnHistTableMaxLength_Type()
)
cmnHistTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnHistTableMaxLength.setStatus("current")
if mibBuilder.loadTexts:
    cmnHistTableMaxLength.setUnits("entries")
_CmnHistoryTable_Object = MibTable
cmnHistoryTable = _CmnHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cmnHistoryTable.setStatus("current")
_CmnHistoryEntry_Object = MibTableRow
cmnHistoryEntry = _CmnHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 8, 1)
)
cmnHistoryEntry.setIndexNames(
    (0, "CISCO-MAC-NOTIFICATION-MIB", "cmnHistIndex"),
)
if mibBuilder.loadTexts:
    cmnHistoryEntry.setStatus("current")


class _CmnHistIndex_Type(Unsigned32):
    """Custom type cmnHistIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CmnHistIndex_Type.__name__ = "Unsigned32"
_CmnHistIndex_Object = MibTableColumn
cmnHistIndex = _CmnHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 8, 1, 1),
    _CmnHistIndex_Type()
)
cmnHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmnHistIndex.setStatus("current")


class _CmnHistMacChangedMsg_Type(OctetString):
    """Custom type cmnHistMacChangedMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_CmnHistMacChangedMsg_Type.__name__ = "OctetString"
_CmnHistMacChangedMsg_Object = MibTableColumn
cmnHistMacChangedMsg = _CmnHistMacChangedMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 8, 1, 2),
    _CmnHistMacChangedMsg_Type()
)
cmnHistMacChangedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnHistMacChangedMsg.setStatus("current")
_CmnHistTimestamp_Type = TimeStamp
_CmnHistTimestamp_Object = MibTableColumn
cmnHistTimestamp = _CmnHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 1, 8, 1, 3),
    _CmnHistTimestamp_Type()
)
cmnHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnHistTimestamp.setStatus("current")
_CmnInterfaceObjects_ObjectIdentity = ObjectIdentity
cmnInterfaceObjects = _CmnInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 2)
)
_CmnIfConfigTable_Object = MibTable
cmnIfConfigTable = _CmnIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmnIfConfigTable.setStatus("current")
_CmnIfConfigEntry_Object = MibTableRow
cmnIfConfigEntry = _CmnIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 2, 1, 1)
)
cmnIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmnIfConfigEntry.setStatus("current")


class _CmnMacAddrLearntEnable_Type(TruthValue):
    """Custom type cmnMacAddrLearntEnable based on TruthValue"""


_CmnMacAddrLearntEnable_Object = MibTableColumn
cmnMacAddrLearntEnable = _CmnMacAddrLearntEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 2, 1, 1, 1),
    _CmnMacAddrLearntEnable_Type()
)
cmnMacAddrLearntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnMacAddrLearntEnable.setStatus("current")


class _CmnMacAddrRemovedEnable_Type(TruthValue):
    """Custom type cmnMacAddrRemovedEnable based on TruthValue"""


_CmnMacAddrRemovedEnable_Object = MibTableColumn
cmnMacAddrRemovedEnable = _CmnMacAddrRemovedEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 2, 1, 1, 2),
    _CmnMacAddrRemovedEnable_Type()
)
cmnMacAddrRemovedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnMacAddrRemovedEnable.setStatus("current")
_CmnMACMoveObjects_ObjectIdentity = ObjectIdentity
cmnMACMoveObjects = _CmnMACMoveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3)
)
_CmnMACMoveFeatureEnabled_Type = TruthValue
_CmnMACMoveFeatureEnabled_Object = MibScalar
cmnMACMoveFeatureEnabled = _CmnMACMoveFeatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 1),
    _CmnMACMoveFeatureEnabled_Type()
)
cmnMACMoveFeatureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnMACMoveFeatureEnabled.setStatus("current")
_CmnMACMoveNotificationsEnabled_Type = TruthValue
_CmnMACMoveNotificationsEnabled_Object = MibScalar
cmnMACMoveNotificationsEnabled = _CmnMACMoveNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 2),
    _CmnMACMoveNotificationsEnabled_Type()
)
cmnMACMoveNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnMACMoveNotificationsEnabled.setStatus("current")
_CmnMACMoveAddress_Type = MacAddress
_CmnMACMoveAddress_Object = MibScalar
cmnMACMoveAddress = _CmnMACMoveAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 3),
    _CmnMACMoveAddress_Type()
)
cmnMACMoveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnMACMoveAddress.setStatus("current")
_CmnMACMoveVlanNumber_Type = VlanIndex
_CmnMACMoveVlanNumber_Object = MibScalar
cmnMACMoveVlanNumber = _CmnMACMoveVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 4),
    _CmnMACMoveVlanNumber_Type()
)
cmnMACMoveVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnMACMoveVlanNumber.setStatus("current")


class _CmnMACMoveFromPortId_Type(Integer32):
    """Custom type cmnMACMoveFromPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmnMACMoveFromPortId_Type.__name__ = "Integer32"
_CmnMACMoveFromPortId_Object = MibScalar
cmnMACMoveFromPortId = _CmnMACMoveFromPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 5),
    _CmnMACMoveFromPortId_Type()
)
cmnMACMoveFromPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnMACMoveFromPortId.setStatus("current")


class _CmnMACMoveToPortId_Type(Integer32):
    """Custom type cmnMACMoveToPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmnMACMoveToPortId_Type.__name__ = "Integer32"
_CmnMACMoveToPortId_Object = MibScalar
cmnMACMoveToPortId = _CmnMACMoveToPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 6),
    _CmnMACMoveToPortId_Type()
)
cmnMACMoveToPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnMACMoveToPortId.setStatus("current")
_CmnMACMoveTime_Type = TimeStamp
_CmnMACMoveTime_Object = MibScalar
cmnMACMoveTime = _CmnMACMoveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 3, 7),
    _CmnMACMoveTime_Type()
)
cmnMACMoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnMACMoveTime.setStatus("current")
_CmnMACThresholdObjects_ObjectIdentity = ObjectIdentity
cmnMACThresholdObjects = _CmnMACThresholdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4)
)
_CmnMACThresholdFeatureEnabled_Type = TruthValue
_CmnMACThresholdFeatureEnabled_Object = MibScalar
cmnMACThresholdFeatureEnabled = _CmnMACThresholdFeatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 1),
    _CmnMACThresholdFeatureEnabled_Type()
)
cmnMACThresholdFeatureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnMACThresholdFeatureEnabled.setStatus("current")
_CmnMACThresholdLimit_Type = Percent
_CmnMACThresholdLimit_Object = MibScalar
cmnMACThresholdLimit = _CmnMACThresholdLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 2),
    _CmnMACThresholdLimit_Type()
)
cmnMACThresholdLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnMACThresholdLimit.setStatus("current")
_CmnMACThresholdInterval_Type = Unsigned32
_CmnMACThresholdInterval_Object = MibScalar
cmnMACThresholdInterval = _CmnMACThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 3),
    _CmnMACThresholdInterval_Type()
)
cmnMACThresholdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnMACThresholdInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmnMACThresholdInterval.setUnits("seconds")
_CmnMACThresholdNotifEnabled_Type = TruthValue
_CmnMACThresholdNotifEnabled_Object = MibScalar
cmnMACThresholdNotifEnabled = _CmnMACThresholdNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 4),
    _CmnMACThresholdNotifEnabled_Type()
)
cmnMACThresholdNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnMACThresholdNotifEnabled.setStatus("current")
_CmnUtilizationTable_Object = MibTable
cmnUtilizationTable = _CmnUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cmnUtilizationTable.setStatus("current")
_CmnUtilizationEntry_Object = MibTableRow
cmnUtilizationEntry = _CmnUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 5, 1)
)
cmnUtilizationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cmnUtilizationEntry.setStatus("current")
_CmnUtilizationEntries_Type = Unsigned32
_CmnUtilizationEntries_Object = MibTableColumn
cmnUtilizationEntries = _CmnUtilizationEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 5, 1, 1),
    _CmnUtilizationEntries_Type()
)
cmnUtilizationEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnUtilizationEntries.setStatus("current")
_CmnUtilizationUtilization_Type = Percent
_CmnUtilizationUtilization_Object = MibTableColumn
cmnUtilizationUtilization = _CmnUtilizationUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 5, 1, 2),
    _CmnUtilizationUtilization_Type()
)
cmnUtilizationUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnUtilizationUtilization.setStatus("current")
_CmnUtilizationTimeStamp_Type = TimeStamp
_CmnUtilizationTimeStamp_Object = MibTableColumn
cmnUtilizationTimeStamp = _CmnUtilizationTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 1, 4, 5, 1, 3),
    _CmnUtilizationTimeStamp_Type()
)
cmnUtilizationTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnUtilizationTimeStamp.setStatus("current")
_CmnMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cmnMIBNotificationPrefix = _CmnMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 2)
)
_CmnMIBNotifications_ObjectIdentity = ObjectIdentity
cmnMIBNotifications = _CmnMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 2, 0)
)
_CmnMIBConformance_ObjectIdentity = ObjectIdentity
cmnMIBConformance = _CmnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3)
)
_CmnMIBCompliances_ObjectIdentity = ObjectIdentity
cmnMIBCompliances = _CmnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 1)
)
_CmnMIBGroups_ObjectIdentity = ObjectIdentity
cmnMIBGroups = _CmnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2)
)

# Managed Objects groups

cmnGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 1)
)
cmnGlobalGroup.setObjects(
      *(("CISCO-MAC-NOTIFICATION-MIB", "cmnGlobalFeatureEnabled"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnNotificationInterval"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMacAddressesLearnt"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMacAddressesRemoved"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnNotificationsEnabled"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnHistTableMaxLength"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnHistMacChangedMsg"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnHistTimestamp"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnNotificationsSent"))
)
if mibBuilder.loadTexts:
    cmnGlobalGroup.setStatus("current")

cmnInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 2)
)
cmnInterfaceGroup.setObjects(
      *(("CISCO-MAC-NOTIFICATION-MIB", "cmnMacAddrLearntEnable"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMacAddrRemovedEnable"))
)
if mibBuilder.loadTexts:
    cmnInterfaceGroup.setStatus("current")

cmnMACMoveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 5)
)
cmnMACMoveGroup.setObjects(
      *(("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveFeatureEnabled"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveNotificationsEnabled"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveAddress"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveVlanNumber"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveFromPortId"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveToPortId"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveTime"))
)
if mibBuilder.loadTexts:
    cmnMACMoveGroup.setStatus("current")

cmnMACThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 6)
)
cmnMACThresholdGroup.setObjects(
      *(("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdFeatureEnabled"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdLimit"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdInterval"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdNotifEnabled"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnUtilizationEntries"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnUtilizationUtilization"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnUtilizationTimeStamp"))
)
if mibBuilder.loadTexts:
    cmnMACThresholdGroup.setStatus("current")


# Notification objects

cmnMacChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 2, 0, 1)
)
cmnMacChangedNotification.setObjects(
      *(("CISCO-MAC-NOTIFICATION-MIB", "cmnHistMacChangedMsg"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnHistTimestamp"))
)
if mibBuilder.loadTexts:
    cmnMacChangedNotification.setStatus(
        "current"
    )

cmnMacMoveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 2, 0, 2)
)
cmnMacMoveNotification.setObjects(
      *(("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveAddress"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveVlanNumber"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveFromPortId"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveToPortId"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACMoveTime"))
)
if mibBuilder.loadTexts:
    cmnMacMoveNotification.setStatus(
        "current"
    )

cmnMacThresholdExceedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 2, 0, 3)
)
cmnMacThresholdExceedNotif.setObjects(
      *(("CISCO-MAC-NOTIFICATION-MIB", "cmnUtilizationUtilization"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnMACThresholdLimit"),
        ("CISCO-MAC-NOTIFICATION-MIB", "cmnUtilizationTimeStamp"))
)
if mibBuilder.loadTexts:
    cmnMacThresholdExceedNotif.setStatus(
        "current"
    )


# Notifications groups

cmnNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 3)
)
cmnNotificationGroup.setObjects(
    ("CISCO-MAC-NOTIFICATION-MIB", "cmnMacChangedNotification")
)
if mibBuilder.loadTexts:
    cmnNotificationGroup.setStatus(
        "current"
    )

cmnMACMoveNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 7)
)
cmnMACMoveNotifGroup.setObjects(
    ("CISCO-MAC-NOTIFICATION-MIB", "cmnMacMoveNotification")
)
if mibBuilder.loadTexts:
    cmnMACMoveNotifGroup.setStatus(
        "current"
    )

cmnMACThresholdNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 2, 8)
)
cmnMACThresholdNotifGroup.setObjects(
    ("CISCO-MAC-NOTIFICATION-MIB", "cmnMacThresholdExceedNotif")
)
if mibBuilder.loadTexts:
    cmnMACThresholdNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cmnMIBCompliance.setStatus(
        "deprecated"
    )

cmnMIBComplianceVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 215, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cmnMIBComplianceVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MAC-NOTIFICATION-MIB",
    **{"ciscoMacNotificationMIB": ciscoMacNotificationMIB,
       "ciscoMacNotificationMIBObjects": ciscoMacNotificationMIBObjects,
       "cmnGlobalObjects": cmnGlobalObjects,
       "cmnGlobalFeatureEnabled": cmnGlobalFeatureEnabled,
       "cmnNotificationInterval": cmnNotificationInterval,
       "cmnMacAddressesLearnt": cmnMacAddressesLearnt,
       "cmnMacAddressesRemoved": cmnMacAddressesRemoved,
       "cmnNotificationsEnabled": cmnNotificationsEnabled,
       "cmnNotificationsSent": cmnNotificationsSent,
       "cmnHistTableMaxLength": cmnHistTableMaxLength,
       "cmnHistoryTable": cmnHistoryTable,
       "cmnHistoryEntry": cmnHistoryEntry,
       "cmnHistIndex": cmnHistIndex,
       "cmnHistMacChangedMsg": cmnHistMacChangedMsg,
       "cmnHistTimestamp": cmnHistTimestamp,
       "cmnInterfaceObjects": cmnInterfaceObjects,
       "cmnIfConfigTable": cmnIfConfigTable,
       "cmnIfConfigEntry": cmnIfConfigEntry,
       "cmnMacAddrLearntEnable": cmnMacAddrLearntEnable,
       "cmnMacAddrRemovedEnable": cmnMacAddrRemovedEnable,
       "cmnMACMoveObjects": cmnMACMoveObjects,
       "cmnMACMoveFeatureEnabled": cmnMACMoveFeatureEnabled,
       "cmnMACMoveNotificationsEnabled": cmnMACMoveNotificationsEnabled,
       "cmnMACMoveAddress": cmnMACMoveAddress,
       "cmnMACMoveVlanNumber": cmnMACMoveVlanNumber,
       "cmnMACMoveFromPortId": cmnMACMoveFromPortId,
       "cmnMACMoveToPortId": cmnMACMoveToPortId,
       "cmnMACMoveTime": cmnMACMoveTime,
       "cmnMACThresholdObjects": cmnMACThresholdObjects,
       "cmnMACThresholdFeatureEnabled": cmnMACThresholdFeatureEnabled,
       "cmnMACThresholdLimit": cmnMACThresholdLimit,
       "cmnMACThresholdInterval": cmnMACThresholdInterval,
       "cmnMACThresholdNotifEnabled": cmnMACThresholdNotifEnabled,
       "cmnUtilizationTable": cmnUtilizationTable,
       "cmnUtilizationEntry": cmnUtilizationEntry,
       "cmnUtilizationEntries": cmnUtilizationEntries,
       "cmnUtilizationUtilization": cmnUtilizationUtilization,
       "cmnUtilizationTimeStamp": cmnUtilizationTimeStamp,
       "cmnMIBNotificationPrefix": cmnMIBNotificationPrefix,
       "cmnMIBNotifications": cmnMIBNotifications,
       "cmnMacChangedNotification": cmnMacChangedNotification,
       "cmnMacMoveNotification": cmnMacMoveNotification,
       "cmnMacThresholdExceedNotif": cmnMacThresholdExceedNotif,
       "cmnMIBConformance": cmnMIBConformance,
       "cmnMIBCompliances": cmnMIBCompliances,
       "cmnMIBCompliance": cmnMIBCompliance,
       "cmnMIBComplianceVer1": cmnMIBComplianceVer1,
       "cmnMIBGroups": cmnMIBGroups,
       "cmnGlobalGroup": cmnGlobalGroup,
       "cmnInterfaceGroup": cmnInterfaceGroup,
       "cmnNotificationGroup": cmnNotificationGroup,
       "cmnMACMoveGroup": cmnMACMoveGroup,
       "cmnMACThresholdGroup": cmnMACThresholdGroup,
       "cmnMACMoveNotifGroup": cmnMACMoveNotifGroup,
       "cmnMACThresholdNotifGroup": cmnMACThresholdNotifGroup}
)
