# SNMP MIB module (CASA-ENTITY-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CASA-ENTITY-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:39 2024
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

(casa,) = mibBuilder.importSymbols(
    "CASA-MIB",
    "casa")

(entPhysicalEntry,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalEntry")

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

casaModuleCpuMemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CasaMgmt_ObjectIdentity = ObjectIdentity
casaMgmt = _CasaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10)
)
_CasaModuleCpuMemObjects_ObjectIdentity = ObjectIdentity
casaModuleCpuMemObjects = _CasaModuleCpuMemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 1)
)
_CasaModuleCpuMemTable_Object = MibTable
casaModuleCpuMemTable = _CasaModuleCpuMemTable_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1)
)
if mibBuilder.loadTexts:
    casaModuleCpuMemTable.setStatus("current")
_CasaModuleCpuMemEntry_Object = MibTableRow
casaModuleCpuMemEntry = _CasaModuleCpuMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    casaModuleCpuMemEntry.setStatus("current")
_CasaModuleTotalAllocatableMem_Type = Unsigned32
_CasaModuleTotalAllocatableMem_Object = MibTableColumn
casaModuleTotalAllocatableMem = _CasaModuleTotalAllocatableMem_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 1),
    _CasaModuleTotalAllocatableMem_Type()
)
casaModuleTotalAllocatableMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaModuleTotalAllocatableMem.setStatus("current")
if mibBuilder.loadTexts:
    casaModuleTotalAllocatableMem.setUnits("KBytes")
_CasaModuleTotalMemAllocated_Type = Unsigned32
_CasaModuleTotalMemAllocated_Object = MibTableColumn
casaModuleTotalMemAllocated = _CasaModuleTotalMemAllocated_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 2),
    _CasaModuleTotalMemAllocated_Type()
)
casaModuleTotalMemAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaModuleTotalMemAllocated.setStatus("current")
if mibBuilder.loadTexts:
    casaModuleTotalMemAllocated.setUnits("KBytes")
_CasaModuleTotalFreeMem_Type = Unsigned32
_CasaModuleTotalFreeMem_Object = MibTableColumn
casaModuleTotalFreeMem = _CasaModuleTotalFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 3),
    _CasaModuleTotalFreeMem_Type()
)
casaModuleTotalFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaModuleTotalFreeMem.setStatus("current")
if mibBuilder.loadTexts:
    casaModuleTotalFreeMem.setUnits("KBytes")
_CasaModuleTotalCpuUtilization_Type = Unsigned32
_CasaModuleTotalCpuUtilization_Object = MibTableColumn
casaModuleTotalCpuUtilization = _CasaModuleTotalCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 4),
    _CasaModuleTotalCpuUtilization_Type()
)
casaModuleTotalCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casaModuleTotalCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    casaModuleTotalCpuUtilization.setUnits("%")
_CasaCmtsCpuMemGroups_ObjectIdentity = ObjectIdentity
casaCmtsCpuMemGroups = _CasaCmtsCpuMemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 2)
)
_CasaCmtsCpuMemCompliances_ObjectIdentity = ObjectIdentity
casaCmtsCpuMemCompliances = _CasaCmtsCpuMemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 3)
)
entPhysicalEntry.registerAugmentions(
    ("CASA-ENTITY-EXT-MIB",
     "casaModuleCpuMemEntry")
)
casaModuleCpuMemEntry.setIndexNames(*entPhysicalEntry.getIndexNames())

# Managed Objects groups

casaCmtsCpuMemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 2, 1)
)
casaCmtsCpuMemGroup.setObjects(
      *(("CASA-ENTITY-EXT-MIB", "casaModuleTotalAllocatableMem"),
        ("CASA-ENTITY-EXT-MIB", "casaModuleTotalMemAllocated"),
        ("CASA-ENTITY-EXT-MIB", "casaModuleTotalFreeMem"),
        ("CASA-ENTITY-EXT-MIB", "casaModuleTotalCpuUtilization"))
)
if mibBuilder.loadTexts:
    casaCmtsCpuMemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

casaCmtsCpuMemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20858, 10, 13, 3, 1)
)
if mibBuilder.loadTexts:
    casaCmtsCpuMemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CASA-ENTITY-EXT-MIB",
    **{"casaMgmt": casaMgmt,
       "casaModuleCpuMemMib": casaModuleCpuMemMib,
       "casaModuleCpuMemObjects": casaModuleCpuMemObjects,
       "casaModuleCpuMemTable": casaModuleCpuMemTable,
       "casaModuleCpuMemEntry": casaModuleCpuMemEntry,
       "casaModuleTotalAllocatableMem": casaModuleTotalAllocatableMem,
       "casaModuleTotalMemAllocated": casaModuleTotalMemAllocated,
       "casaModuleTotalFreeMem": casaModuleTotalFreeMem,
       "casaModuleTotalCpuUtilization": casaModuleTotalCpuUtilization,
       "casaCmtsCpuMemGroups": casaCmtsCpuMemGroups,
       "casaCmtsCpuMemGroup": casaCmtsCpuMemGroup,
       "casaCmtsCpuMemCompliances": casaCmtsCpuMemCompliances,
       "casaCmtsCpuMemCompliance": casaCmtsCpuMemCompliance}
)
