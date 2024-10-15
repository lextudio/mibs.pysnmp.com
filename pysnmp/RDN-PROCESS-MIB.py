# SNMP MIB module (RDN-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-PROCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:12 2024
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

(rdnChassis,) = mibBuilder.importSymbols(
    "RDN-CHASSIS-MIB",
    "rdnChassis")

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

rdnProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20)
)
rdnProcessMIB.setRevisions(
        ("2008-08-08 00:00",
         "2003-11-05 00:00",
         "2003-03-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RdnTaskPriorityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 4),
          ("normal", 3),
          ("notAssigned", 5))
    )



# MIB Managed Objects in the order of their OIDs

_RdnProcessMIBObjects_ObjectIdentity = ObjectIdentity
rdnProcessMIBObjects = _RdnProcessMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1)
)
_RdnCPUTotalTable_Object = MibTable
rdnCPUTotalTable = _RdnCPUTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    rdnCPUTotalTable.setStatus("current")
_RdnCPUTotalEntry_Object = MibTableRow
rdnCPUTotalEntry = _RdnCPUTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1, 1)
)
rdnCPUTotalEntry.setIndexNames(
    (0, "RDN-PROCESS-MIB", "rdnSlotSnmpIndex"),
    (0, "RDN-PROCESS-MIB", "rdnCPUIndex"),
)
if mibBuilder.loadTexts:
    rdnCPUTotalEntry.setStatus("current")


class _RdnSlotSnmpIndex_Type(Integer32):
    """Custom type rdnSlotSnmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RdnSlotSnmpIndex_Type.__name__ = "Integer32"
_RdnSlotSnmpIndex_Object = MibTableColumn
rdnSlotSnmpIndex = _RdnSlotSnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1, 1, 1),
    _RdnSlotSnmpIndex_Type()
)
rdnSlotSnmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnSlotSnmpIndex.setStatus("current")
_RdnCPUIndex_Type = Unsigned32
_RdnCPUIndex_Object = MibTableColumn
rdnCPUIndex = _RdnCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1, 1, 2),
    _RdnCPUIndex_Type()
)
rdnCPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCPUIndex.setStatus("current")


class _RdnCPUType_Type(DisplayString):
    """Custom type rdnCPUType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RdnCPUType_Type.__name__ = "DisplayString"
_RdnCPUType_Object = MibTableColumn
rdnCPUType = _RdnCPUType_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1, 1, 3),
    _RdnCPUType_Type()
)
rdnCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCPUType.setStatus("current")
_RdnTotalAllocatableMem_Type = Unsigned32
_RdnTotalAllocatableMem_Object = MibTableColumn
rdnTotalAllocatableMem = _RdnTotalAllocatableMem_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1, 1, 4),
    _RdnTotalAllocatableMem_Type()
)
rdnTotalAllocatableMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTotalAllocatableMem.setStatus("current")
if mibBuilder.loadTexts:
    rdnTotalAllocatableMem.setUnits("byte")
_RdnTotalMemAllocated_Type = Unsigned32
_RdnTotalMemAllocated_Object = MibTableColumn
rdnTotalMemAllocated = _RdnTotalMemAllocated_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1, 1, 5),
    _RdnTotalMemAllocated_Type()
)
rdnTotalMemAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTotalMemAllocated.setStatus("current")
if mibBuilder.loadTexts:
    rdnTotalMemAllocated.setUnits("byte")
_RdnTotalFreeMem_Type = Unsigned32
_RdnTotalFreeMem_Object = MibTableColumn
rdnTotalFreeMem = _RdnTotalFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1, 1, 6),
    _RdnTotalFreeMem_Type()
)
rdnTotalFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTotalFreeMem.setStatus("current")
if mibBuilder.loadTexts:
    rdnTotalFreeMem.setUnits("byte")


class _RdnTotalCPUUtilization5Sec_Type(Unsigned32):
    """Custom type rdnTotalCPUUtilization5Sec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RdnTotalCPUUtilization5Sec_Type.__name__ = "Unsigned32"
_RdnTotalCPUUtilization5Sec_Object = MibTableColumn
rdnTotalCPUUtilization5Sec = _RdnTotalCPUUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1, 1, 7),
    _RdnTotalCPUUtilization5Sec_Type()
)
rdnTotalCPUUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTotalCPUUtilization5Sec.setStatus("current")
if mibBuilder.loadTexts:
    rdnTotalCPUUtilization5Sec.setUnits("1/100")


class _RdnTotalCPUUtilization1Min_Type(Unsigned32):
    """Custom type rdnTotalCPUUtilization1Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RdnTotalCPUUtilization1Min_Type.__name__ = "Unsigned32"
_RdnTotalCPUUtilization1Min_Object = MibTableColumn
rdnTotalCPUUtilization1Min = _RdnTotalCPUUtilization1Min_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1, 1, 8),
    _RdnTotalCPUUtilization1Min_Type()
)
rdnTotalCPUUtilization1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTotalCPUUtilization1Min.setStatus("current")
if mibBuilder.loadTexts:
    rdnTotalCPUUtilization1Min.setUnits("1/100")


class _RdnTotalCPUUtilization5Min_Type(Unsigned32):
    """Custom type rdnTotalCPUUtilization5Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RdnTotalCPUUtilization5Min_Type.__name__ = "Unsigned32"
_RdnTotalCPUUtilization5Min_Object = MibTableColumn
rdnTotalCPUUtilization5Min = _RdnTotalCPUUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 1, 1, 9),
    _RdnTotalCPUUtilization5Min_Type()
)
rdnTotalCPUUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTotalCPUUtilization5Min.setStatus("current")
if mibBuilder.loadTexts:
    rdnTotalCPUUtilization5Min.setUnits("1/100")
_RdnTaskTable_Object = MibTable
rdnTaskTable = _RdnTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    rdnTaskTable.setStatus("current")
_RdnTaskEntry_Object = MibTableRow
rdnTaskEntry = _RdnTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 2, 1)
)
rdnTaskEntry.setIndexNames(
    (0, "RDN-PROCESS-MIB", "rdnSlotSnmpIndex"),
    (0, "RDN-PROCESS-MIB", "rdnCPUIndex"),
    (0, "RDN-PROCESS-MIB", "rdnTaskId"),
)
if mibBuilder.loadTexts:
    rdnTaskEntry.setStatus("current")
_RdnTaskId_Type = Unsigned32
_RdnTaskId_Object = MibTableColumn
rdnTaskId = _RdnTaskId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 2, 1, 1),
    _RdnTaskId_Type()
)
rdnTaskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTaskId.setStatus("current")


class _RdnTaskName_Type(DisplayString):
    """Custom type rdnTaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RdnTaskName_Type.__name__ = "DisplayString"
_RdnTaskName_Object = MibTableColumn
rdnTaskName = _RdnTaskName_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 2, 1, 2),
    _RdnTaskName_Type()
)
rdnTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTaskName.setStatus("current")
_RdnTaskPriority_Type = RdnTaskPriorityType
_RdnTaskPriority_Object = MibTableColumn
rdnTaskPriority = _RdnTaskPriority_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 2, 1, 3),
    _RdnTaskPriority_Type()
)
rdnTaskPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTaskPriority.setStatus("current")
_RdnTaskMemAllocated_Type = Unsigned32
_RdnTaskMemAllocated_Object = MibTableColumn
rdnTaskMemAllocated = _RdnTaskMemAllocated_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 2, 1, 4),
    _RdnTaskMemAllocated_Type()
)
rdnTaskMemAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTaskMemAllocated.setStatus("current")
if mibBuilder.loadTexts:
    rdnTaskMemAllocated.setUnits("byte")


class _RdnTaskUtil5Sec_Type(Unsigned32):
    """Custom type rdnTaskUtil5Sec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RdnTaskUtil5Sec_Type.__name__ = "Unsigned32"
_RdnTaskUtil5Sec_Object = MibTableColumn
rdnTaskUtil5Sec = _RdnTaskUtil5Sec_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 2, 1, 5),
    _RdnTaskUtil5Sec_Type()
)
rdnTaskUtil5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTaskUtil5Sec.setStatus("current")
if mibBuilder.loadTexts:
    rdnTaskUtil5Sec.setUnits("1/100")


class _RdnTaskUtil1Min_Type(Unsigned32):
    """Custom type rdnTaskUtil1Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RdnTaskUtil1Min_Type.__name__ = "Unsigned32"
_RdnTaskUtil1Min_Object = MibTableColumn
rdnTaskUtil1Min = _RdnTaskUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 2, 1, 6),
    _RdnTaskUtil1Min_Type()
)
rdnTaskUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTaskUtil1Min.setStatus("current")
if mibBuilder.loadTexts:
    rdnTaskUtil1Min.setUnits("1/100")


class _RdnTaskUtil5Min_Type(Unsigned32):
    """Custom type rdnTaskUtil5Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RdnTaskUtil5Min_Type.__name__ = "Unsigned32"
_RdnTaskUtil5Min_Object = MibTableColumn
rdnTaskUtil5Min = _RdnTaskUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 1, 2, 1, 7),
    _RdnTaskUtil5Min_Type()
)
rdnTaskUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnTaskUtil5Min.setStatus("current")
if mibBuilder.loadTexts:
    rdnTaskUtil5Min.setUnits("1/100")
_RdnProcessMIBNotifPrefix_ObjectIdentity = ObjectIdentity
rdnProcessMIBNotifPrefix = _RdnProcessMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 2)
)
_RdnProcessMIBNotifs_ObjectIdentity = ObjectIdentity
rdnProcessMIBNotifs = _RdnProcessMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 2, 0)
)
_RdnProcessMIBConformance_ObjectIdentity = ObjectIdentity
rdnProcessMIBConformance = _RdnProcessMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 3)
)
_RdnProcessCompliances_ObjectIdentity = ObjectIdentity
rdnProcessCompliances = _RdnProcessCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 3, 1)
)
_RdnProcessGroups_ObjectIdentity = ObjectIdentity
rdnProcessGroups = _RdnProcessGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 3, 2)
)

# Managed Objects groups

rdnCPUTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 3, 2, 1)
)
rdnCPUTotalGroup.setObjects(
      *(("RDN-PROCESS-MIB", "rdnCPUType"),
        ("RDN-PROCESS-MIB", "rdnTotalAllocatableMem"),
        ("RDN-PROCESS-MIB", "rdnTotalMemAllocated"),
        ("RDN-PROCESS-MIB", "rdnTotalFreeMem"),
        ("RDN-PROCESS-MIB", "rdnTotalCPUUtilization5Sec"),
        ("RDN-PROCESS-MIB", "rdnTotalCPUUtilization1Min"),
        ("RDN-PROCESS-MIB", "rdnTotalCPUUtilization5Min"))
)
if mibBuilder.loadTexts:
    rdnCPUTotalGroup.setStatus("current")

rdnTaskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 3, 2, 2)
)
rdnTaskGroup.setObjects(
      *(("RDN-PROCESS-MIB", "rdnTaskId"),
        ("RDN-PROCESS-MIB", "rdnTaskName"),
        ("RDN-PROCESS-MIB", "rdnTaskPriority"),
        ("RDN-PROCESS-MIB", "rdnTaskMemAllocated"),
        ("RDN-PROCESS-MIB", "rdnTaskUtil5Sec"),
        ("RDN-PROCESS-MIB", "rdnTaskUtil1Min"),
        ("RDN-PROCESS-MIB", "rdnTaskUtil5Min"))
)
if mibBuilder.loadTexts:
    rdnTaskGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rdnProcessMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4981, 1, 20, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rdnProcessMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-PROCESS-MIB",
    **{"RdnTaskPriorityType": RdnTaskPriorityType,
       "rdnProcessMIB": rdnProcessMIB,
       "rdnProcessMIBObjects": rdnProcessMIBObjects,
       "rdnCPUTotalTable": rdnCPUTotalTable,
       "rdnCPUTotalEntry": rdnCPUTotalEntry,
       "rdnSlotSnmpIndex": rdnSlotSnmpIndex,
       "rdnCPUIndex": rdnCPUIndex,
       "rdnCPUType": rdnCPUType,
       "rdnTotalAllocatableMem": rdnTotalAllocatableMem,
       "rdnTotalMemAllocated": rdnTotalMemAllocated,
       "rdnTotalFreeMem": rdnTotalFreeMem,
       "rdnTotalCPUUtilization5Sec": rdnTotalCPUUtilization5Sec,
       "rdnTotalCPUUtilization1Min": rdnTotalCPUUtilization1Min,
       "rdnTotalCPUUtilization5Min": rdnTotalCPUUtilization5Min,
       "rdnTaskTable": rdnTaskTable,
       "rdnTaskEntry": rdnTaskEntry,
       "rdnTaskId": rdnTaskId,
       "rdnTaskName": rdnTaskName,
       "rdnTaskPriority": rdnTaskPriority,
       "rdnTaskMemAllocated": rdnTaskMemAllocated,
       "rdnTaskUtil5Sec": rdnTaskUtil5Sec,
       "rdnTaskUtil1Min": rdnTaskUtil1Min,
       "rdnTaskUtil5Min": rdnTaskUtil5Min,
       "rdnProcessMIBNotifPrefix": rdnProcessMIBNotifPrefix,
       "rdnProcessMIBNotifs": rdnProcessMIBNotifs,
       "rdnProcessMIBConformance": rdnProcessMIBConformance,
       "rdnProcessCompliances": rdnProcessCompliances,
       "rdnProcessMIBCompliance": rdnProcessMIBCompliance,
       "rdnProcessGroups": rdnProcessGroups,
       "rdnCPUTotalGroup": rdnCPUTotalGroup,
       "rdnTaskGroup": rdnTaskGroup}
)
