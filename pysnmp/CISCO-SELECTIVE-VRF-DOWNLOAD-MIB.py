# SNMP MIB module (CISCO-SELECTIVE-VRF-DOWNLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SELECTIVE-VRF-DOWNLOAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:05 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(MplsL3VpnName,) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "MplsL3VpnName")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSelectiveVrfDownloadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 775)
)
ciscoSelectiveVrfDownloadMIB.setRevisions(
        ("2011-06-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SVDEntityRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("core", 3),
          ("customer", 4),
          ("invalid", 1),
          ("noInterest", 5),
          ("standard", 2),
          ("vpnOnlyCustomer", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSelectiveVrfDownloadMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSelectiveVrfDownloadMIBNotifs = _CiscoSelectiveVrfDownloadMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 0)
)
_CiscoSelectiveVrfDownloadMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSelectiveVrfDownloadMIBObjects = _CiscoSelectiveVrfDownloadMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1)
)


class _CsvdAdminEnable_Type(TruthValue):
    """Custom type csvdAdminEnable based on TruthValue"""


_CsvdAdminEnable_Object = MibScalar
csvdAdminEnable = _CsvdAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 1),
    _CsvdAdminEnable_Type()
)
csvdAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csvdAdminEnable.setStatus("current")
_CsvdOperEnable_Type = TruthValue
_CsvdOperEnable_Object = MibScalar
csvdOperEnable = _CsvdOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 2),
    _CsvdOperEnable_Type()
)
csvdOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdOperEnable.setStatus("current")


class _CsvdEntityRoleChangeNotificationEnable_Type(TruthValue):
    """Custom type csvdEntityRoleChangeNotificationEnable based on TruthValue"""


_CsvdEntityRoleChangeNotificationEnable_Object = MibScalar
csvdEntityRoleChangeNotificationEnable = _CsvdEntityRoleChangeNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 3),
    _CsvdEntityRoleChangeNotificationEnable_Type()
)
csvdEntityRoleChangeNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csvdEntityRoleChangeNotificationEnable.setStatus("current")
_CsvdCounterDiscontinuityTime_Type = TimeStamp
_CsvdCounterDiscontinuityTime_Object = MibScalar
csvdCounterDiscontinuityTime = _CsvdCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 4),
    _CsvdCounterDiscontinuityTime_Type()
)
csvdCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdCounterDiscontinuityTime.setStatus("current")
_CsvdStateTable_Object = MibTable
csvdStateTable = _CsvdStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 5)
)
if mibBuilder.loadTexts:
    csvdStateTable.setStatus("current")
_CsvdStateEntry_Object = MibTableRow
csvdStateEntry = _CsvdStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 5, 1)
)
csvdStateEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdStateAFI"),
)
if mibBuilder.loadTexts:
    csvdStateEntry.setStatus("current")
_CsvdStateAFI_Type = AddressFamilyNumbers
_CsvdStateAFI_Object = MibTableColumn
csvdStateAFI = _CsvdStateAFI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 5, 1, 1),
    _CsvdStateAFI_Type()
)
csvdStateAFI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csvdStateAFI.setStatus("current")
_CsvdStateEntityRole_Type = SVDEntityRole
_CsvdStateEntityRole_Object = MibTableColumn
csvdStateEntityRole = _CsvdStateEntityRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 5, 1, 2),
    _CsvdStateEntityRole_Type()
)
csvdStateEntityRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csvdStateEntityRole.setStatus("current")
_CsvdStateEntityRoleLastChange_Type = TimeStamp
_CsvdStateEntityRoleLastChange_Object = MibTableColumn
csvdStateEntityRoleLastChange = _CsvdStateEntityRoleLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 5, 1, 3),
    _CsvdStateEntityRoleLastChange_Type()
)
csvdStateEntityRoleLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdStateEntityRoleLastChange.setStatus("current")
_CsvdStateEntityRoleTransitions_Type = Counter32
_CsvdStateEntityRoleTransitions_Object = MibTableColumn
csvdStateEntityRoleTransitions = _CsvdStateEntityRoleTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 5, 1, 4),
    _CsvdStateEntityRoleTransitions_Type()
)
csvdStateEntityRoleTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdStateEntityRoleTransitions.setStatus("current")
_CsvdRoleHistory_ObjectIdentity = ObjectIdentity
csvdRoleHistory = _CsvdRoleHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 6)
)


class _CsvdRoleHistorySize_Type(Unsigned32):
    """Custom type csvdRoleHistorySize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CsvdRoleHistorySize_Type.__name__ = "Unsigned32"
_CsvdRoleHistorySize_Object = MibScalar
csvdRoleHistorySize = _CsvdRoleHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 6, 1),
    _CsvdRoleHistorySize_Type()
)
csvdRoleHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csvdRoleHistorySize.setStatus("current")


class _CsvdRoleHistoryLastIndex_Type(Unsigned32):
    """Custom type csvdRoleHistoryLastIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CsvdRoleHistoryLastIndex_Type.__name__ = "Unsigned32"
_CsvdRoleHistoryLastIndex_Object = MibScalar
csvdRoleHistoryLastIndex = _CsvdRoleHistoryLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 6, 2),
    _CsvdRoleHistoryLastIndex_Type()
)
csvdRoleHistoryLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdRoleHistoryLastIndex.setStatus("current")
_CsvdRoleHistoryTable_Object = MibTable
csvdRoleHistoryTable = _CsvdRoleHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 6, 3)
)
if mibBuilder.loadTexts:
    csvdRoleHistoryTable.setStatus("current")
_CsvdRoleHistoryEntry_Object = MibTableRow
csvdRoleHistoryEntry = _CsvdRoleHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 6, 3, 1)
)
csvdRoleHistoryEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdStateAFI"),
    (0, "CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdRoleHistoryIndex"),
)
if mibBuilder.loadTexts:
    csvdRoleHistoryEntry.setStatus("current")


class _CsvdRoleHistoryIndex_Type(Unsigned32):
    """Custom type csvdRoleHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CsvdRoleHistoryIndex_Type.__name__ = "Unsigned32"
_CsvdRoleHistoryIndex_Object = MibTableColumn
csvdRoleHistoryIndex = _CsvdRoleHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 6, 3, 1, 1),
    _CsvdRoleHistoryIndex_Type()
)
csvdRoleHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csvdRoleHistoryIndex.setStatus("current")
_CsvdRoleHistoryRole_Type = SVDEntityRole
_CsvdRoleHistoryRole_Object = MibTableColumn
csvdRoleHistoryRole = _CsvdRoleHistoryRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 6, 3, 1, 2),
    _CsvdRoleHistoryRole_Type()
)
csvdRoleHistoryRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdRoleHistoryRole.setStatus("current")
_CsvdRoleHistoryRoleChangeTime_Type = TimeStamp
_CsvdRoleHistoryRoleChangeTime_Object = MibTableColumn
csvdRoleHistoryRoleChangeTime = _CsvdRoleHistoryRoleChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 6, 3, 1, 3),
    _CsvdRoleHistoryRoleChangeTime_Type()
)
csvdRoleHistoryRoleChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdRoleHistoryRoleChangeTime.setStatus("current")
_CsvdVrfTable_Object = MibTable
csvdVrfTable = _CsvdVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 7)
)
if mibBuilder.loadTexts:
    csvdVrfTable.setStatus("current")
_CsvdVrfEntry_Object = MibTableRow
csvdVrfEntry = _CsvdVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 7, 1)
)
csvdVrfEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdStateAFI"),
    (0, "CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdVrfName"),
)
if mibBuilder.loadTexts:
    csvdVrfEntry.setStatus("current")
_CsvdVrfName_Type = MplsL3VpnName
_CsvdVrfName_Object = MibTableColumn
csvdVrfName = _CsvdVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 7, 1, 1),
    _CsvdVrfName_Type()
)
csvdVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csvdVrfName.setStatus("current")
_CsvdPrefixCount_Type = Gauge32
_CsvdPrefixCount_Object = MibTableColumn
csvdPrefixCount = _CsvdPrefixCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 7, 1, 2),
    _CsvdPrefixCount_Type()
)
csvdPrefixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdPrefixCount.setStatus("current")
_CsvdLocalPrefixCount_Type = Gauge32
_CsvdLocalPrefixCount_Object = MibTableColumn
csvdLocalPrefixCount = _CsvdLocalPrefixCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 7, 1, 3),
    _CsvdLocalPrefixCount_Type()
)
csvdLocalPrefixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdLocalPrefixCount.setStatus("current")
_CsvdRemotePrefixCount_Type = Gauge32
_CsvdRemotePrefixCount_Object = MibTableColumn
csvdRemotePrefixCount = _CsvdRemotePrefixCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 7, 1, 4),
    _CsvdRemotePrefixCount_Type()
)
csvdRemotePrefixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdRemotePrefixCount.setStatus("current")


class _CsvdTableConvergedFlag_Type(TruthValue):
    """Custom type csvdTableConvergedFlag based on TruthValue"""


_CsvdTableConvergedFlag_Object = MibTableColumn
csvdTableConvergedFlag = _CsvdTableConvergedFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 1, 7, 1, 5),
    _CsvdTableConvergedFlag_Type()
)
csvdTableConvergedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csvdTableConvergedFlag.setStatus("current")
_CiscoSelectiveVrfDownloadMIBConform_ObjectIdentity = ObjectIdentity
ciscoSelectiveVrfDownloadMIBConform = _CiscoSelectiveVrfDownloadMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 2)
)
_CsvdMIBCompliances_ObjectIdentity = ObjectIdentity
csvdMIBCompliances = _CsvdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 2, 1)
)
_CsvdMIBGroups_ObjectIdentity = ObjectIdentity
csvdMIBGroups = _CsvdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 2, 2)
)

# Managed Objects groups

csvdMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 2, 2, 1)
)
csvdMIBGroup.setObjects(
      *(("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdAdminEnable"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdOperEnable"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdCounterDiscontinuityTime"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdStateEntityRole"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdStateEntityRoleLastChange"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdStateEntityRoleTransitions"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdRoleHistorySize"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdRoleHistoryLastIndex"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdRoleHistoryRole"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdRoleHistoryRoleChangeTime"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdPrefixCount"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdLocalPrefixCount"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdRemotePrefixCount"),
        ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdTableConvergedFlag"))
)
if mibBuilder.loadTexts:
    csvdMIBGroup.setStatus("current")

csvdMIBNotificationEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 2, 2, 2)
)
csvdMIBNotificationEnableGroup.setObjects(
    ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdEntityRoleChangeNotificationEnable")
)
if mibBuilder.loadTexts:
    csvdMIBNotificationEnableGroup.setStatus("current")


# Notification objects

csvdEntityRoleChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 0, 1)
)
csvdEntityRoleChangeNotification.setObjects(
    ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdStateEntityRole")
)
if mibBuilder.loadTexts:
    csvdEntityRoleChangeNotification.setStatus(
        "current"
    )


# Notifications groups

csvdMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 2, 2, 3)
)
csvdMIBNotificationGroup.setObjects(
    ("CISCO-SELECTIVE-VRF-DOWNLOAD-MIB", "csvdEntityRoleChangeNotification")
)
if mibBuilder.loadTexts:
    csvdMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

csvdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 775, 2, 1, 1)
)
if mibBuilder.loadTexts:
    csvdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SELECTIVE-VRF-DOWNLOAD-MIB",
    **{"SVDEntityRole": SVDEntityRole,
       "ciscoSelectiveVrfDownloadMIB": ciscoSelectiveVrfDownloadMIB,
       "ciscoSelectiveVrfDownloadMIBNotifs": ciscoSelectiveVrfDownloadMIBNotifs,
       "csvdEntityRoleChangeNotification": csvdEntityRoleChangeNotification,
       "ciscoSelectiveVrfDownloadMIBObjects": ciscoSelectiveVrfDownloadMIBObjects,
       "csvdAdminEnable": csvdAdminEnable,
       "csvdOperEnable": csvdOperEnable,
       "csvdEntityRoleChangeNotificationEnable": csvdEntityRoleChangeNotificationEnable,
       "csvdCounterDiscontinuityTime": csvdCounterDiscontinuityTime,
       "csvdStateTable": csvdStateTable,
       "csvdStateEntry": csvdStateEntry,
       "csvdStateAFI": csvdStateAFI,
       "csvdStateEntityRole": csvdStateEntityRole,
       "csvdStateEntityRoleLastChange": csvdStateEntityRoleLastChange,
       "csvdStateEntityRoleTransitions": csvdStateEntityRoleTransitions,
       "csvdRoleHistory": csvdRoleHistory,
       "csvdRoleHistorySize": csvdRoleHistorySize,
       "csvdRoleHistoryLastIndex": csvdRoleHistoryLastIndex,
       "csvdRoleHistoryTable": csvdRoleHistoryTable,
       "csvdRoleHistoryEntry": csvdRoleHistoryEntry,
       "csvdRoleHistoryIndex": csvdRoleHistoryIndex,
       "csvdRoleHistoryRole": csvdRoleHistoryRole,
       "csvdRoleHistoryRoleChangeTime": csvdRoleHistoryRoleChangeTime,
       "csvdVrfTable": csvdVrfTable,
       "csvdVrfEntry": csvdVrfEntry,
       "csvdVrfName": csvdVrfName,
       "csvdPrefixCount": csvdPrefixCount,
       "csvdLocalPrefixCount": csvdLocalPrefixCount,
       "csvdRemotePrefixCount": csvdRemotePrefixCount,
       "csvdTableConvergedFlag": csvdTableConvergedFlag,
       "ciscoSelectiveVrfDownloadMIBConform": ciscoSelectiveVrfDownloadMIBConform,
       "csvdMIBCompliances": csvdMIBCompliances,
       "csvdMIBCompliance": csvdMIBCompliance,
       "csvdMIBGroups": csvdMIBGroups,
       "csvdMIBGroup": csvdMIBGroup,
       "csvdMIBNotificationEnableGroup": csvdMIBNotificationEnableGroup,
       "csvdMIBNotificationGroup": csvdMIBNotificationGroup}
)
