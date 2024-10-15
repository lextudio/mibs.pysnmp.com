# SNMP MIB module (ENTERASYS-RESOURCE-UTILIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-RESOURCE-UTILIZATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:28 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etsysResourceUtilizationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49)
)
etsysResourceUtilizationMIB.setRevisions(
        ("2009-11-02 15:41",
         "2004-11-30 16:33")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ResourceStorageType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("flash", 3),
          ("other", 1),
          ("ram", 2),
          ("usbFlash", 4))
    )



class ResourceUtilization(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



# MIB Managed Objects in the order of their OIDs

_EtsysResourceUtilizationObjects_ObjectIdentity = ObjectIdentity
etsysResourceUtilizationObjects = _EtsysResourceUtilizationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1)
)
_EtsysResourceUtilizationNotifications_ObjectIdentity = ObjectIdentity
etsysResourceUtilizationNotifications = _EtsysResourceUtilizationNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 0)
)
_EtsysResourceCpu_ObjectIdentity = ObjectIdentity
etsysResourceCpu = _EtsysResourceCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1)
)
_EtsysResourceCpuTable_Object = MibTable
etsysResourceCpuTable = _EtsysResourceCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysResourceCpuTable.setStatus("current")
_EtsysResourceCpuEntry_Object = MibTableRow
etsysResourceCpuEntry = _EtsysResourceCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1)
)
etsysResourceCpuEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuId"),
)
if mibBuilder.loadTexts:
    etsysResourceCpuEntry.setStatus("current")
_EtsysResourceCpuId_Type = Unsigned32
_EtsysResourceCpuId_Object = MibTableColumn
etsysResourceCpuId = _EtsysResourceCpuId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 1),
    _EtsysResourceCpuId_Type()
)
etsysResourceCpuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysResourceCpuId.setStatus("current")
_EtsysResourceCpuLoad5sec_Type = ResourceUtilization
_EtsysResourceCpuLoad5sec_Object = MibTableColumn
etsysResourceCpuLoad5sec = _EtsysResourceCpuLoad5sec_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 2),
    _EtsysResourceCpuLoad5sec_Type()
)
etsysResourceCpuLoad5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceCpuLoad5sec.setStatus("current")
_EtsysResourceCpuLoad1min_Type = ResourceUtilization
_EtsysResourceCpuLoad1min_Object = MibTableColumn
etsysResourceCpuLoad1min = _EtsysResourceCpuLoad1min_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 3),
    _EtsysResourceCpuLoad1min_Type()
)
etsysResourceCpuLoad1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceCpuLoad1min.setStatus("current")
_EtsysResourceCpuLoad5min_Type = ResourceUtilization
_EtsysResourceCpuLoad5min_Object = MibTableColumn
etsysResourceCpuLoad5min = _EtsysResourceCpuLoad5min_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 1, 1, 1, 4),
    _EtsysResourceCpuLoad5min_Type()
)
etsysResourceCpuLoad5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceCpuLoad5min.setStatus("current")
_EtsysResourceProcess_ObjectIdentity = ObjectIdentity
etsysResourceProcess = _EtsysResourceProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2)
)
_EtsysResourceProcessTable_Object = MibTable
etsysResourceProcessTable = _EtsysResourceProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysResourceProcessTable.setStatus("current")
_EtsysResourceProcessEntry_Object = MibTableRow
etsysResourceProcessEntry = _EtsysResourceProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1)
)
etsysResourceProcessEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuId"),
    (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessID"),
)
if mibBuilder.loadTexts:
    etsysResourceProcessEntry.setStatus("current")
_EtsysResourceProcessID_Type = Unsigned32
_EtsysResourceProcessID_Object = MibTableColumn
etsysResourceProcessID = _EtsysResourceProcessID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 1),
    _EtsysResourceProcessID_Type()
)
etsysResourceProcessID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysResourceProcessID.setStatus("current")
_EtsysResourceProcessName_Type = SnmpAdminString
_EtsysResourceProcessName_Object = MibTableColumn
etsysResourceProcessName = _EtsysResourceProcessName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 2),
    _EtsysResourceProcessName_Type()
)
etsysResourceProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceProcessName.setStatus("current")
_EtsysResourceProcessLoad5sec_Type = ResourceUtilization
_EtsysResourceProcessLoad5sec_Object = MibTableColumn
etsysResourceProcessLoad5sec = _EtsysResourceProcessLoad5sec_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 3),
    _EtsysResourceProcessLoad5sec_Type()
)
etsysResourceProcessLoad5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceProcessLoad5sec.setStatus("current")
_EtsysResourceProcessLoad1min_Type = ResourceUtilization
_EtsysResourceProcessLoad1min_Object = MibTableColumn
etsysResourceProcessLoad1min = _EtsysResourceProcessLoad1min_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 4),
    _EtsysResourceProcessLoad1min_Type()
)
etsysResourceProcessLoad1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceProcessLoad1min.setStatus("current")
_EtsysResourceProcessLoad5min_Type = ResourceUtilization
_EtsysResourceProcessLoad5min_Object = MibTableColumn
etsysResourceProcessLoad5min = _EtsysResourceProcessLoad5min_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 2, 1, 1, 5),
    _EtsysResourceProcessLoad5min_Type()
)
etsysResourceProcessLoad5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceProcessLoad5min.setStatus("current")
_EtsysResourceStorage_ObjectIdentity = ObjectIdentity
etsysResourceStorage = _EtsysResourceStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3)
)
_EtsysResourceStorageTable_Object = MibTable
etsysResourceStorageTable = _EtsysResourceStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysResourceStorageTable.setStatus("current")
_EtsysResourceStorageEntry_Object = MibTableRow
etsysResourceStorageEntry = _EtsysResourceStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1)
)
etsysResourceStorageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageType"),
    (0, "ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageTypeID"),
)
if mibBuilder.loadTexts:
    etsysResourceStorageEntry.setStatus("current")
_EtsysResourceStorageType_Type = ResourceStorageType
_EtsysResourceStorageType_Object = MibTableColumn
etsysResourceStorageType = _EtsysResourceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 1),
    _EtsysResourceStorageType_Type()
)
etsysResourceStorageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysResourceStorageType.setStatus("current")
_EtsysResourceStorageTypeID_Type = Unsigned32
_EtsysResourceStorageTypeID_Object = MibTableColumn
etsysResourceStorageTypeID = _EtsysResourceStorageTypeID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 2),
    _EtsysResourceStorageTypeID_Type()
)
etsysResourceStorageTypeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysResourceStorageTypeID.setStatus("current")
_EtsysResourceStorageDescr_Type = SnmpAdminString
_EtsysResourceStorageDescr_Object = MibTableColumn
etsysResourceStorageDescr = _EtsysResourceStorageDescr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 3),
    _EtsysResourceStorageDescr_Type()
)
etsysResourceStorageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceStorageDescr.setStatus("current")
_EtsysResourceStorageSize_Type = Unsigned32
_EtsysResourceStorageSize_Object = MibTableColumn
etsysResourceStorageSize = _EtsysResourceStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 4),
    _EtsysResourceStorageSize_Type()
)
etsysResourceStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceStorageSize.setStatus("current")
_EtsysResourceStorageAvailable_Type = Unsigned32
_EtsysResourceStorageAvailable_Object = MibTableColumn
etsysResourceStorageAvailable = _EtsysResourceStorageAvailable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 3, 1, 1, 5),
    _EtsysResourceStorageAvailable_Type()
)
etsysResourceStorageAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceStorageAvailable.setStatus("current")
_EtsysResourceScalars_ObjectIdentity = ObjectIdentity
etsysResourceScalars = _EtsysResourceScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 4)
)


class _EtsysResource1minThreshold_Type(ResourceUtilization):
    """Custom type etsysResource1minThreshold based on ResourceUtilization"""
    defaultValue = 800


_EtsysResource1minThreshold_Object = MibScalar
etsysResource1minThreshold = _EtsysResource1minThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 4, 1),
    _EtsysResource1minThreshold_Type()
)
etsysResource1minThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysResource1minThreshold.setStatus("current")
_EtsysResourceUtilizationConformance_ObjectIdentity = ObjectIdentity
etsysResourceUtilizationConformance = _EtsysResourceUtilizationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2)
)
_EtsysResourceUtilizationGroups_ObjectIdentity = ObjectIdentity
etsysResourceUtilizationGroups = _EtsysResourceUtilizationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1)
)
_EtsysResourceUtilizationCompliances_ObjectIdentity = ObjectIdentity
etsysResourceUtilizationCompliances = _EtsysResourceUtilizationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 2)
)

# Managed Objects groups

etsysResourceUtilizationCpuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 1)
)
etsysResourceUtilizationCpuGroup.setObjects(
      *(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad5sec"),
        ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad1min"),
        ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad5min"))
)
if mibBuilder.loadTexts:
    etsysResourceUtilizationCpuGroup.setStatus("current")

etsysResourceUtilizationProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 2)
)
etsysResourceUtilizationProcessGroup.setObjects(
      *(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessName"),
        ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessLoad5sec"),
        ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessLoad1min"),
        ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceProcessLoad5min"))
)
if mibBuilder.loadTexts:
    etsysResourceUtilizationProcessGroup.setStatus("current")

etsysResourceUtilizationStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 3)
)
etsysResourceUtilizationStorageGroup.setObjects(
      *(("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageDescr"),
        ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageSize"),
        ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceStorageAvailable"))
)
if mibBuilder.loadTexts:
    etsysResourceUtilizationStorageGroup.setStatus("current")

etsysResourceUtilizationScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 5)
)
etsysResourceUtilizationScalarsGroup.setObjects(
    ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResource1minThreshold")
)
if mibBuilder.loadTexts:
    etsysResourceUtilizationScalarsGroup.setStatus("current")


# Notification objects

etsysResourceCpuLoad1minThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 1, 0, 1)
)
etsysResourceCpuLoad1minThresholdExceeded.setObjects(
    ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad1min")
)
if mibBuilder.loadTexts:
    etsysResourceCpuLoad1minThresholdExceeded.setStatus(
        "current"
    )


# Notifications groups

etsysResourceUtilizationNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 1, 4)
)
etsysResourceUtilizationNotificationGroup.setObjects(
    ("ENTERASYS-RESOURCE-UTILIZATION-MIB", "etsysResourceCpuLoad1minThresholdExceeded")
)
if mibBuilder.loadTexts:
    etsysResourceUtilizationNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysResourceUtilizationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 49, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysResourceUtilizationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-RESOURCE-UTILIZATION-MIB",
    **{"ResourceStorageType": ResourceStorageType,
       "ResourceUtilization": ResourceUtilization,
       "etsysResourceUtilizationMIB": etsysResourceUtilizationMIB,
       "etsysResourceUtilizationObjects": etsysResourceUtilizationObjects,
       "etsysResourceUtilizationNotifications": etsysResourceUtilizationNotifications,
       "etsysResourceCpuLoad1minThresholdExceeded": etsysResourceCpuLoad1minThresholdExceeded,
       "etsysResourceCpu": etsysResourceCpu,
       "etsysResourceCpuTable": etsysResourceCpuTable,
       "etsysResourceCpuEntry": etsysResourceCpuEntry,
       "etsysResourceCpuId": etsysResourceCpuId,
       "etsysResourceCpuLoad5sec": etsysResourceCpuLoad5sec,
       "etsysResourceCpuLoad1min": etsysResourceCpuLoad1min,
       "etsysResourceCpuLoad5min": etsysResourceCpuLoad5min,
       "etsysResourceProcess": etsysResourceProcess,
       "etsysResourceProcessTable": etsysResourceProcessTable,
       "etsysResourceProcessEntry": etsysResourceProcessEntry,
       "etsysResourceProcessID": etsysResourceProcessID,
       "etsysResourceProcessName": etsysResourceProcessName,
       "etsysResourceProcessLoad5sec": etsysResourceProcessLoad5sec,
       "etsysResourceProcessLoad1min": etsysResourceProcessLoad1min,
       "etsysResourceProcessLoad5min": etsysResourceProcessLoad5min,
       "etsysResourceStorage": etsysResourceStorage,
       "etsysResourceStorageTable": etsysResourceStorageTable,
       "etsysResourceStorageEntry": etsysResourceStorageEntry,
       "etsysResourceStorageType": etsysResourceStorageType,
       "etsysResourceStorageTypeID": etsysResourceStorageTypeID,
       "etsysResourceStorageDescr": etsysResourceStorageDescr,
       "etsysResourceStorageSize": etsysResourceStorageSize,
       "etsysResourceStorageAvailable": etsysResourceStorageAvailable,
       "etsysResourceScalars": etsysResourceScalars,
       "etsysResource1minThreshold": etsysResource1minThreshold,
       "etsysResourceUtilizationConformance": etsysResourceUtilizationConformance,
       "etsysResourceUtilizationGroups": etsysResourceUtilizationGroups,
       "etsysResourceUtilizationCpuGroup": etsysResourceUtilizationCpuGroup,
       "etsysResourceUtilizationProcessGroup": etsysResourceUtilizationProcessGroup,
       "etsysResourceUtilizationStorageGroup": etsysResourceUtilizationStorageGroup,
       "etsysResourceUtilizationNotificationGroup": etsysResourceUtilizationNotificationGroup,
       "etsysResourceUtilizationScalarsGroup": etsysResourceUtilizationScalarsGroup,
       "etsysResourceUtilizationCompliances": etsysResourceUtilizationCompliances,
       "etsysResourceUtilizationCompliance": etsysResourceUtilizationCompliance}
)
