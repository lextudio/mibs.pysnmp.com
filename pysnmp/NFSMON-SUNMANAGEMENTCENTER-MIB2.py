# SNMP MIB module (NFSMON-SUNMANAGEMENTCENTER-MIB2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NFSMON-SUNMANAGEMENTCENTER-MIB2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:24 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nfsmon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27)
)
nfsmon.setRevisions(
        ("1999-07-20 15:05",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Sunsymon_ObjectIdentity = ObjectIdentity
sunsymon = _Sunsymon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2)
)
_NfsmFileTable_Object = MibTable
nfsmFileTable = _NfsmFileTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1, 1)
)
if mibBuilder.loadTexts:
    nfsmFileTable.setStatus("current")
_NfsmFileEntry_Object = MibTableRow
nfsmFileEntry = _NfsmFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1, 1, 1)
)
nfsmFileEntry.setIndexNames(
    (0, "NFSMON-SUNMANAGEMENTCENTER-MIB2", "nfsmFileSystemEntryIndex"),
)
if mibBuilder.loadTexts:
    nfsmFileEntry.setStatus("current")
_NfsmFileSystemName_Type = DisplayString
_NfsmFileSystemName_Object = MibTableColumn
nfsmFileSystemName = _NfsmFileSystemName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1, 1, 1, 1),
    _NfsmFileSystemName_Type()
)
nfsmFileSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsmFileSystemName.setStatus("current")
_NfsmFileSystemSize_Type = Integer32
_NfsmFileSystemSize_Object = MibTableColumn
nfsmFileSystemSize = _NfsmFileSystemSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1, 1, 1, 2),
    _NfsmFileSystemSize_Type()
)
nfsmFileSystemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsmFileSystemSize.setStatus("current")
if mibBuilder.loadTexts:
    nfsmFileSystemSize.setUnits("KB")
_NfsmFileSystemUsedSpace_Type = Integer32
_NfsmFileSystemUsedSpace_Object = MibTableColumn
nfsmFileSystemUsedSpace = _NfsmFileSystemUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1, 1, 1, 3),
    _NfsmFileSystemUsedSpace_Type()
)
nfsmFileSystemUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsmFileSystemUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    nfsmFileSystemUsedSpace.setUnits("KB")
_NfsmFileSystemAvailSpace_Type = Integer32
_NfsmFileSystemAvailSpace_Object = MibTableColumn
nfsmFileSystemAvailSpace = _NfsmFileSystemAvailSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1, 1, 1, 4),
    _NfsmFileSystemAvailSpace_Type()
)
nfsmFileSystemAvailSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsmFileSystemAvailSpace.setStatus("current")
if mibBuilder.loadTexts:
    nfsmFileSystemAvailSpace.setUnits("KB")
_NfsmFileSystemPctUsedSpace_Type = DisplayString
_NfsmFileSystemPctUsedSpace_Object = MibTableColumn
nfsmFileSystemPctUsedSpace = _NfsmFileSystemPctUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1, 1, 1, 5),
    _NfsmFileSystemPctUsedSpace_Type()
)
nfsmFileSystemPctUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsmFileSystemPctUsedSpace.setStatus("current")
if mibBuilder.loadTexts:
    nfsmFileSystemPctUsedSpace.setUnits("%")
_NfsmFileSystemPctUsedSpaceRate_Type = DisplayString
_NfsmFileSystemPctUsedSpaceRate_Object = MibTableColumn
nfsmFileSystemPctUsedSpaceRate = _NfsmFileSystemPctUsedSpaceRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1, 1, 1, 6),
    _NfsmFileSystemPctUsedSpaceRate_Type()
)
nfsmFileSystemPctUsedSpaceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsmFileSystemPctUsedSpaceRate.setStatus("current")
if mibBuilder.loadTexts:
    nfsmFileSystemPctUsedSpaceRate.setUnits("%/sec")
_NfsmFileSystemMountPoint_Type = DisplayString
_NfsmFileSystemMountPoint_Object = MibTableColumn
nfsmFileSystemMountPoint = _NfsmFileSystemMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1, 1, 1, 7),
    _NfsmFileSystemMountPoint_Type()
)
nfsmFileSystemMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsmFileSystemMountPoint.setStatus("current")
_NfsmFileSystemEntryIndex_Type = DisplayString
_NfsmFileSystemEntryIndex_Object = MibTableColumn
nfsmFileSystemEntryIndex = _NfsmFileSystemEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1, 1, 1, 8),
    _NfsmFileSystemEntryIndex_Type()
)
nfsmFileSystemEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsmFileSystemEntryIndex.setStatus("current")

# Managed Objects groups

nfsmFileSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27, 1)
)
nfsmFileSystemGroup.setObjects(
      *(("NFSMON-SUNMANAGEMENTCENTER-MIB2", "nfsmFileSystemName"),
        ("NFSMON-SUNMANAGEMENTCENTER-MIB2", "nfsmFileSystemSize"),
        ("NFSMON-SUNMANAGEMENTCENTER-MIB2", "nfsmFileSystemUsedSpace"),
        ("NFSMON-SUNMANAGEMENTCENTER-MIB2", "nfsmFileSystemAvailSpace"),
        ("NFSMON-SUNMANAGEMENTCENTER-MIB2", "nfsmFileSystemPctUsedSpace"),
        ("NFSMON-SUNMANAGEMENTCENTER-MIB2", "nfsmFileSystemPctUsedSpaceRate"),
        ("NFSMON-SUNMANAGEMENTCENTER-MIB2", "nfsmFileSystemMountPoint"),
        ("NFSMON-SUNMANAGEMENTCENTER-MIB2", "nfsmFileSystemEntryIndex"))
)
if mibBuilder.loadTexts:
    nfsmFileSystemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NFSMON-SUNMANAGEMENTCENTER-MIB2",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "modules": modules,
       "nfsmon": nfsmon,
       "nfsmFileSystemGroup": nfsmFileSystemGroup,
       "nfsmFileTable": nfsmFileTable,
       "nfsmFileEntry": nfsmFileEntry,
       "nfsmFileSystemName": nfsmFileSystemName,
       "nfsmFileSystemSize": nfsmFileSystemSize,
       "nfsmFileSystemUsedSpace": nfsmFileSystemUsedSpace,
       "nfsmFileSystemAvailSpace": nfsmFileSystemAvailSpace,
       "nfsmFileSystemPctUsedSpace": nfsmFileSystemPctUsedSpace,
       "nfsmFileSystemPctUsedSpaceRate": nfsmFileSystemPctUsedSpaceRate,
       "nfsmFileSystemMountPoint": nfsmFileSystemMountPoint,
       "nfsmFileSystemEntryIndex": nfsmFileSystemEntryIndex}
)
