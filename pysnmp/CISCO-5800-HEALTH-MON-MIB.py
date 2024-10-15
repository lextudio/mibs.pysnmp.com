# SNMP MIB module (CISCO-5800-HEALTH-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-5800-HEALTH-MON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:18 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cisco5800HealthMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cisco5800HealthMonObjects_ObjectIdentity = ObjectIdentity
cisco5800HealthMonObjects = _Cisco5800HealthMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1)
)
_CiscoHealthMonStatusTable_Object = MibTable
ciscoHealthMonStatusTable = _CiscoHealthMonStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoHealthMonStatusTable.setStatus("current")
_CiscoHealthMonStatusEntry_Object = MibTableRow
ciscoHealthMonStatusEntry = _CiscoHealthMonStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 1, 1)
)
ciscoHealthMonStatusEntry.setIndexNames(
    (0, "CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonStatusIndex"),
    (0, "CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonStatusType"),
)
if mibBuilder.loadTexts:
    ciscoHealthMonStatusEntry.setStatus("current")


class _CiscoHealthMonStatusIndex_Type(Integer32):
    """Custom type ciscoHealthMonStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoHealthMonStatusIndex_Type.__name__ = "Integer32"
_CiscoHealthMonStatusIndex_Object = MibTableColumn
ciscoHealthMonStatusIndex = _CiscoHealthMonStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 1, 1, 1),
    _CiscoHealthMonStatusIndex_Type()
)
ciscoHealthMonStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoHealthMonStatusIndex.setStatus("current")


class _CiscoHealthMonStatusType_Type(Integer32):
    """Custom type ciscoHealthMonStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CiscoHealthMonStatusType_Type.__name__ = "Integer32"
_CiscoHealthMonStatusType_Object = MibTableColumn
ciscoHealthMonStatusType = _CiscoHealthMonStatusType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 1, 1, 2),
    _CiscoHealthMonStatusType_Type()
)
ciscoHealthMonStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonStatusType.setStatus("current")
_CiscoHealthMonShelfId_Type = Integer32
_CiscoHealthMonShelfId_Object = MibTableColumn
ciscoHealthMonShelfId = _CiscoHealthMonShelfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 1, 1, 3),
    _CiscoHealthMonShelfId_Type()
)
ciscoHealthMonShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonShelfId.setStatus("current")
_CiscoHealthMonAddress_Type = IpAddress
_CiscoHealthMonAddress_Object = MibTableColumn
ciscoHealthMonAddress = _CiscoHealthMonAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 1, 1, 4),
    _CiscoHealthMonAddress_Type()
)
ciscoHealthMonAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonAddress.setStatus("current")


class _CiscoHealthMonDescr_Type(DisplayString):
    """Custom type ciscoHealthMonDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiscoHealthMonDescr_Type.__name__ = "DisplayString"
_CiscoHealthMonDescr_Object = MibTableColumn
ciscoHealthMonDescr = _CiscoHealthMonDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 1, 1, 5),
    _CiscoHealthMonDescr_Type()
)
ciscoHealthMonDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonDescr.setStatus("current")
_CiscoHealthMonValue_Type = Gauge32
_CiscoHealthMonValue_Object = MibTableColumn
ciscoHealthMonValue = _CiscoHealthMonValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 1, 1, 6),
    _CiscoHealthMonValue_Type()
)
ciscoHealthMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonValue.setStatus("current")


class _CiscoHealthMonThreshold_Type(Integer32):
    """Custom type ciscoHealthMonThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CiscoHealthMonThreshold_Type.__name__ = "Integer32"
_CiscoHealthMonThreshold_Object = MibTableColumn
ciscoHealthMonThreshold = _CiscoHealthMonThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 1, 1, 7),
    _CiscoHealthMonThreshold_Type()
)
ciscoHealthMonThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonThreshold.setStatus("current")
_CiscoHealthMonThresholdExceedCount_Type = Integer32
_CiscoHealthMonThresholdExceedCount_Object = MibTableColumn
ciscoHealthMonThresholdExceedCount = _CiscoHealthMonThresholdExceedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 1, 1, 8),
    _CiscoHealthMonThresholdExceedCount_Type()
)
ciscoHealthMonThresholdExceedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonThresholdExceedCount.setStatus("current")
_CiscoHealthMonCountTable_Object = MibTable
ciscoHealthMonCountTable = _CiscoHealthMonCountTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoHealthMonCountTable.setStatus("current")
_CiscoHealthMonCountEntry_Object = MibTableRow
ciscoHealthMonCountEntry = _CiscoHealthMonCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1)
)
ciscoHealthMonCountEntry.setIndexNames(
    (0, "CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonCountIndex"),
)
if mibBuilder.loadTexts:
    ciscoHealthMonCountEntry.setStatus("current")


class _CiscoHealthMonCountIndex_Type(Integer32):
    """Custom type ciscoHealthMonCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CiscoHealthMonCountIndex_Type.__name__ = "Integer32"
_CiscoHealthMonCountIndex_Object = MibTableColumn
ciscoHealthMonCountIndex = _CiscoHealthMonCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 1),
    _CiscoHealthMonCountIndex_Type()
)
ciscoHealthMonCountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoHealthMonCountIndex.setStatus("current")
_CiscoHealthMonT1E1LinesUp_Type = Gauge32
_CiscoHealthMonT1E1LinesUp_Object = MibTableColumn
ciscoHealthMonT1E1LinesUp = _CiscoHealthMonT1E1LinesUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 2),
    _CiscoHealthMonT1E1LinesUp_Type()
)
ciscoHealthMonT1E1LinesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonT1E1LinesUp.setStatus("current")
_CiscoHealthMonT1E1LinesDown_Type = Gauge32
_CiscoHealthMonT1E1LinesDown_Object = MibTableColumn
ciscoHealthMonT1E1LinesDown = _CiscoHealthMonT1E1LinesDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 3),
    _CiscoHealthMonT1E1LinesDown_Type()
)
ciscoHealthMonT1E1LinesDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonT1E1LinesDown.setStatus("current")
_CiscoHealthMonActiveDS0_Type = Gauge32
_CiscoHealthMonActiveDS0_Object = MibTableColumn
ciscoHealthMonActiveDS0 = _CiscoHealthMonActiveDS0_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 4),
    _CiscoHealthMonActiveDS0_Type()
)
ciscoHealthMonActiveDS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonActiveDS0.setStatus("current")
_CiscoHealthMonTotalDS0_Type = Gauge32
_CiscoHealthMonTotalDS0_Object = MibTableColumn
ciscoHealthMonTotalDS0 = _CiscoHealthMonTotalDS0_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 5),
    _CiscoHealthMonTotalDS0_Type()
)
ciscoHealthMonTotalDS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonTotalDS0.setStatus("current")
_CiscoHealthMonTotalModems_Type = Gauge32
_CiscoHealthMonTotalModems_Object = MibTableColumn
ciscoHealthMonTotalModems = _CiscoHealthMonTotalModems_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 6),
    _CiscoHealthMonTotalModems_Type()
)
ciscoHealthMonTotalModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonTotalModems.setStatus("current")
_CiscoHealthMonModemsInUse_Type = Gauge32
_CiscoHealthMonModemsInUse_Object = MibTableColumn
ciscoHealthMonModemsInUse = _CiscoHealthMonModemsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 7),
    _CiscoHealthMonModemsInUse_Type()
)
ciscoHealthMonModemsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonModemsInUse.setStatus("current")
_CiscoHealthMonUnavailableModems_Type = Gauge32
_CiscoHealthMonUnavailableModems_Object = MibTableColumn
ciscoHealthMonUnavailableModems = _CiscoHealthMonUnavailableModems_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 8),
    _CiscoHealthMonUnavailableModems_Type()
)
ciscoHealthMonUnavailableModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonUnavailableModems.setStatus("current")
_CiscoHealthMonIOMemUsed_Type = Gauge32
_CiscoHealthMonIOMemUsed_Object = MibTableColumn
ciscoHealthMonIOMemUsed = _CiscoHealthMonIOMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 9),
    _CiscoHealthMonIOMemUsed_Type()
)
ciscoHealthMonIOMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonIOMemUsed.setStatus("current")
if mibBuilder.loadTexts:
    ciscoHealthMonIOMemUsed.setUnits("bytes")
_CiscoHealthMonIOMemFree_Type = Gauge32
_CiscoHealthMonIOMemFree_Object = MibTableColumn
ciscoHealthMonIOMemFree = _CiscoHealthMonIOMemFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 10),
    _CiscoHealthMonIOMemFree_Type()
)
ciscoHealthMonIOMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonIOMemFree.setStatus("current")
if mibBuilder.loadTexts:
    ciscoHealthMonIOMemFree.setUnits("bytes")


class _CiscoHealthMonCPUavgBusy5_Type(Integer32):
    """Custom type ciscoHealthMonCPUavgBusy5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CiscoHealthMonCPUavgBusy5_Type.__name__ = "Integer32"
_CiscoHealthMonCPUavgBusy5_Object = MibTableColumn
ciscoHealthMonCPUavgBusy5 = _CiscoHealthMonCPUavgBusy5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 11),
    _CiscoHealthMonCPUavgBusy5_Type()
)
ciscoHealthMonCPUavgBusy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonCPUavgBusy5.setStatus("current")
_CiscoHealthMonUtilEgressInOctet_Type = Counter32
_CiscoHealthMonUtilEgressInOctet_Object = MibTableColumn
ciscoHealthMonUtilEgressInOctet = _CiscoHealthMonUtilEgressInOctet_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 12),
    _CiscoHealthMonUtilEgressInOctet_Type()
)
ciscoHealthMonUtilEgressInOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonUtilEgressInOctet.setStatus("current")
_CiscoHealthMonUtilEgressOutOctet_Type = Counter32
_CiscoHealthMonUtilEgressOutOctet_Object = MibTableColumn
ciscoHealthMonUtilEgressOutOctet = _CiscoHealthMonUtilEgressOutOctet_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 13),
    _CiscoHealthMonUtilEgressOutOctet_Type()
)
ciscoHealthMonUtilEgressOutOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonUtilEgressOutOctet.setStatus("current")


class _CiscoHealthMonShelfLastUpdate_Type(DisplayString):
    """Custom type ciscoHealthMonShelfLastUpdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiscoHealthMonShelfLastUpdate_Type.__name__ = "DisplayString"
_CiscoHealthMonShelfLastUpdate_Object = MibTableColumn
ciscoHealthMonShelfLastUpdate = _CiscoHealthMonShelfLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 2, 1, 14),
    _CiscoHealthMonShelfLastUpdate_Type()
)
ciscoHealthMonShelfLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonShelfLastUpdate.setStatus("current")
_CiscoHealthMonNumShelves_Type = Integer32
_CiscoHealthMonNumShelves_Object = MibScalar
ciscoHealthMonNumShelves = _CiscoHealthMonNumShelves_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 3),
    _CiscoHealthMonNumShelves_Type()
)
ciscoHealthMonNumShelves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonNumShelves.setStatus("current")
_CiscoHealthMonNumT1E1LinesUp_Type = Gauge32
_CiscoHealthMonNumT1E1LinesUp_Object = MibScalar
ciscoHealthMonNumT1E1LinesUp = _CiscoHealthMonNumT1E1LinesUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 4),
    _CiscoHealthMonNumT1E1LinesUp_Type()
)
ciscoHealthMonNumT1E1LinesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonNumT1E1LinesUp.setStatus("current")
_CiscoHealthMonNumT1E1LinesDown_Type = Gauge32
_CiscoHealthMonNumT1E1LinesDown_Object = MibScalar
ciscoHealthMonNumT1E1LinesDown = _CiscoHealthMonNumT1E1LinesDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 5),
    _CiscoHealthMonNumT1E1LinesDown_Type()
)
ciscoHealthMonNumT1E1LinesDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonNumT1E1LinesDown.setStatus("current")
_CiscoHealthMonNumActiveDS0_Type = Gauge32
_CiscoHealthMonNumActiveDS0_Object = MibScalar
ciscoHealthMonNumActiveDS0 = _CiscoHealthMonNumActiveDS0_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 6),
    _CiscoHealthMonNumActiveDS0_Type()
)
ciscoHealthMonNumActiveDS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonNumActiveDS0.setStatus("current")
_CiscoHealthMonNumTotalDS0_Type = Gauge32
_CiscoHealthMonNumTotalDS0_Object = MibScalar
ciscoHealthMonNumTotalDS0 = _CiscoHealthMonNumTotalDS0_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 7),
    _CiscoHealthMonNumTotalDS0_Type()
)
ciscoHealthMonNumTotalDS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonNumTotalDS0.setStatus("current")
_CiscoHealthMonNumTotalModems_Type = Gauge32
_CiscoHealthMonNumTotalModems_Object = MibScalar
ciscoHealthMonNumTotalModems = _CiscoHealthMonNumTotalModems_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 8),
    _CiscoHealthMonNumTotalModems_Type()
)
ciscoHealthMonNumTotalModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonNumTotalModems.setStatus("current")
_CiscoHealthMonNumModemsInUse_Type = Gauge32
_CiscoHealthMonNumModemsInUse_Object = MibScalar
ciscoHealthMonNumModemsInUse = _CiscoHealthMonNumModemsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 9),
    _CiscoHealthMonNumModemsInUse_Type()
)
ciscoHealthMonNumModemsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonNumModemsInUse.setStatus("current")
_CiscoHealthMonNumUnavailableModems_Type = Gauge32
_CiscoHealthMonNumUnavailableModems_Object = MibScalar
ciscoHealthMonNumUnavailableModems = _CiscoHealthMonNumUnavailableModems_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 1, 10),
    _CiscoHealthMonNumUnavailableModems_Type()
)
ciscoHealthMonNumUnavailableModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoHealthMonNumUnavailableModems.setStatus("current")
_CiscoHealthMonMIBNotificationEnables_ObjectIdentity = ObjectIdentity
ciscoHealthMonMIBNotificationEnables = _CiscoHealthMonMIBNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 2)
)


class _CiscoHealthMonEnableNotification_Type(TruthValue):
    """Custom type ciscoHealthMonEnableNotification based on TruthValue"""


_CiscoHealthMonEnableNotification_Object = MibScalar
ciscoHealthMonEnableNotification = _CiscoHealthMonEnableNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 2, 1),
    _CiscoHealthMonEnableNotification_Type()
)
ciscoHealthMonEnableNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoHealthMonEnableNotification.setStatus("current")
_CiscoHealthMonMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoHealthMonMIBNotificationPrefix = _CiscoHealthMonMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 3)
)
_CiscoHealthMonMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoHealthMonMIBNotifications = _CiscoHealthMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 3, 0)
)
_Cisco5800HealthMonMIBConformance_ObjectIdentity = ObjectIdentity
cisco5800HealthMonMIBConformance = _Cisco5800HealthMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 4)
)
_Cisco5800HealthMonMIBCompliances_ObjectIdentity = ObjectIdentity
cisco5800HealthMonMIBCompliances = _Cisco5800HealthMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 4, 1)
)
_Cisco5800HealthMonMIBGroups_ObjectIdentity = ObjectIdentity
cisco5800HealthMonMIBGroups = _Cisco5800HealthMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 4, 2)
)

# Managed Objects groups

cisco5800HealthMonMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 4, 2, 1)
)
cisco5800HealthMonMIBGroup.setObjects(
      *(("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonStatusType"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonShelfId"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonAddress"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonDescr"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonValue"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonThreshold"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonThresholdExceedCount"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonT1E1LinesUp"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonT1E1LinesDown"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonActiveDS0"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonTotalDS0"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonTotalModems"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonModemsInUse"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonUnavailableModems"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonIOMemUsed"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonIOMemFree"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonCPUavgBusy5"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonUtilEgressInOctet"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonUtilEgressOutOctet"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonShelfLastUpdate"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonNumShelves"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonNumT1E1LinesUp"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonNumT1E1LinesDown"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonNumActiveDS0"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonNumTotalDS0"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonNumTotalModems"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonNumModemsInUse"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonNumUnavailableModems"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonEnableNotification"))
)
if mibBuilder.loadTexts:
    cisco5800HealthMonMIBGroup.setStatus("current")


# Notification objects

ciscoHealthMonNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 3, 0, 1)
)
ciscoHealthMonNotification.setObjects(
      *(("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonStatusType"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonShelfId"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonAddress"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonDescr"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonValue"),
        ("CISCO-5800-HEALTH-MON-MIB", "ciscoHealthMonThreshold"))
)
if mibBuilder.loadTexts:
    ciscoHealthMonNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

cisco5800HealthMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 28, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cisco5800HealthMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-5800-HEALTH-MON-MIB",
    **{"cisco5800HealthMonMIB": cisco5800HealthMonMIB,
       "cisco5800HealthMonObjects": cisco5800HealthMonObjects,
       "ciscoHealthMonStatusTable": ciscoHealthMonStatusTable,
       "ciscoHealthMonStatusEntry": ciscoHealthMonStatusEntry,
       "ciscoHealthMonStatusIndex": ciscoHealthMonStatusIndex,
       "ciscoHealthMonStatusType": ciscoHealthMonStatusType,
       "ciscoHealthMonShelfId": ciscoHealthMonShelfId,
       "ciscoHealthMonAddress": ciscoHealthMonAddress,
       "ciscoHealthMonDescr": ciscoHealthMonDescr,
       "ciscoHealthMonValue": ciscoHealthMonValue,
       "ciscoHealthMonThreshold": ciscoHealthMonThreshold,
       "ciscoHealthMonThresholdExceedCount": ciscoHealthMonThresholdExceedCount,
       "ciscoHealthMonCountTable": ciscoHealthMonCountTable,
       "ciscoHealthMonCountEntry": ciscoHealthMonCountEntry,
       "ciscoHealthMonCountIndex": ciscoHealthMonCountIndex,
       "ciscoHealthMonT1E1LinesUp": ciscoHealthMonT1E1LinesUp,
       "ciscoHealthMonT1E1LinesDown": ciscoHealthMonT1E1LinesDown,
       "ciscoHealthMonActiveDS0": ciscoHealthMonActiveDS0,
       "ciscoHealthMonTotalDS0": ciscoHealthMonTotalDS0,
       "ciscoHealthMonTotalModems": ciscoHealthMonTotalModems,
       "ciscoHealthMonModemsInUse": ciscoHealthMonModemsInUse,
       "ciscoHealthMonUnavailableModems": ciscoHealthMonUnavailableModems,
       "ciscoHealthMonIOMemUsed": ciscoHealthMonIOMemUsed,
       "ciscoHealthMonIOMemFree": ciscoHealthMonIOMemFree,
       "ciscoHealthMonCPUavgBusy5": ciscoHealthMonCPUavgBusy5,
       "ciscoHealthMonUtilEgressInOctet": ciscoHealthMonUtilEgressInOctet,
       "ciscoHealthMonUtilEgressOutOctet": ciscoHealthMonUtilEgressOutOctet,
       "ciscoHealthMonShelfLastUpdate": ciscoHealthMonShelfLastUpdate,
       "ciscoHealthMonNumShelves": ciscoHealthMonNumShelves,
       "ciscoHealthMonNumT1E1LinesUp": ciscoHealthMonNumT1E1LinesUp,
       "ciscoHealthMonNumT1E1LinesDown": ciscoHealthMonNumT1E1LinesDown,
       "ciscoHealthMonNumActiveDS0": ciscoHealthMonNumActiveDS0,
       "ciscoHealthMonNumTotalDS0": ciscoHealthMonNumTotalDS0,
       "ciscoHealthMonNumTotalModems": ciscoHealthMonNumTotalModems,
       "ciscoHealthMonNumModemsInUse": ciscoHealthMonNumModemsInUse,
       "ciscoHealthMonNumUnavailableModems": ciscoHealthMonNumUnavailableModems,
       "ciscoHealthMonMIBNotificationEnables": ciscoHealthMonMIBNotificationEnables,
       "ciscoHealthMonEnableNotification": ciscoHealthMonEnableNotification,
       "ciscoHealthMonMIBNotificationPrefix": ciscoHealthMonMIBNotificationPrefix,
       "ciscoHealthMonMIBNotifications": ciscoHealthMonMIBNotifications,
       "ciscoHealthMonNotification": ciscoHealthMonNotification,
       "cisco5800HealthMonMIBConformance": cisco5800HealthMonMIBConformance,
       "cisco5800HealthMonMIBCompliances": cisco5800HealthMonMIBCompliances,
       "cisco5800HealthMonMIBCompliance": cisco5800HealthMonMIBCompliance,
       "cisco5800HealthMonMIBGroups": cisco5800HealthMonMIBGroups,
       "cisco5800HealthMonMIBGroup": cisco5800HealthMonMIBGroup}
)
