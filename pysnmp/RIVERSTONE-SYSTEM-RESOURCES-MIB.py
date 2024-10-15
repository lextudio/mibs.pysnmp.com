# SNMP MIB module (RIVERSTONE-SYSTEM-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-SYSTEM-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:56 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RIVERSTONE-SMI-MIB",
    "riverstoneMibs")

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

rsSystemResourcesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281)
)
rsSystemResourcesMIB.setRevisions(
        ("2004-09-14 13:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsSystemUtilization_ObjectIdentity = ObjectIdentity
rsSystemUtilization = _RsSystemUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5)
)
if mibBuilder.loadTexts:
    rsSystemUtilization.setStatus("current")
_RsCpuUtl_ObjectIdentity = ObjectIdentity
rsCpuUtl = _RsCpuUtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 5)
)
if mibBuilder.loadTexts:
    rsCpuUtl.setStatus("current")
_RsUtlCPUTable_Object = MibTable
rsUtlCPUTable = _RsUtlCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 5, 1)
)
if mibBuilder.loadTexts:
    rsUtlCPUTable.setStatus("current")
_RsUtlCPUEntry_Object = MibTableRow
rsUtlCPUEntry = _RsUtlCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 5, 1, 1)
)
rsUtlCPUEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    rsUtlCPUEntry.setStatus("current")


class _RsUtlCPUSystemUtilization5Sec_Type(Unsigned32):
    """Custom type rsUtlCPUSystemUtilization5Sec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsUtlCPUSystemUtilization5Sec_Type.__name__ = "Unsigned32"
_RsUtlCPUSystemUtilization5Sec_Object = MibTableColumn
rsUtlCPUSystemUtilization5Sec = _RsUtlCPUSystemUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 5, 1, 1, 1),
    _RsUtlCPUSystemUtilization5Sec_Type()
)
rsUtlCPUSystemUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlCPUSystemUtilization5Sec.setStatus("current")


class _RsUtlCPUUserUtilization5Sec_Type(Unsigned32):
    """Custom type rsUtlCPUUserUtilization5Sec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsUtlCPUUserUtilization5Sec_Type.__name__ = "Unsigned32"
_RsUtlCPUUserUtilization5Sec_Object = MibTableColumn
rsUtlCPUUserUtilization5Sec = _RsUtlCPUUserUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 5, 1, 1, 2),
    _RsUtlCPUUserUtilization5Sec_Type()
)
rsUtlCPUUserUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlCPUUserUtilization5Sec.setStatus("current")


class _RsUtlCPUSystemUtilization60Sec_Type(Unsigned32):
    """Custom type rsUtlCPUSystemUtilization60Sec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsUtlCPUSystemUtilization60Sec_Type.__name__ = "Unsigned32"
_RsUtlCPUSystemUtilization60Sec_Object = MibTableColumn
rsUtlCPUSystemUtilization60Sec = _RsUtlCPUSystemUtilization60Sec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 5, 1, 1, 3),
    _RsUtlCPUSystemUtilization60Sec_Type()
)
rsUtlCPUSystemUtilization60Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlCPUSystemUtilization60Sec.setStatus("current")


class _RsUtlCPUUserUtilization60Sec_Type(Unsigned32):
    """Custom type rsUtlCPUUserUtilization60Sec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsUtlCPUUserUtilization60Sec_Type.__name__ = "Unsigned32"
_RsUtlCPUUserUtilization60Sec_Object = MibTableColumn
rsUtlCPUUserUtilization60Sec = _RsUtlCPUUserUtilization60Sec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 5, 1, 1, 4),
    _RsUtlCPUUserUtilization60Sec_Type()
)
rsUtlCPUUserUtilization60Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlCPUUserUtilization60Sec.setStatus("current")


class _RsUtlCPUSystemUtilization5Min_Type(Unsigned32):
    """Custom type rsUtlCPUSystemUtilization5Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsUtlCPUSystemUtilization5Min_Type.__name__ = "Unsigned32"
_RsUtlCPUSystemUtilization5Min_Object = MibTableColumn
rsUtlCPUSystemUtilization5Min = _RsUtlCPUSystemUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 5, 1, 1, 5),
    _RsUtlCPUSystemUtilization5Min_Type()
)
rsUtlCPUSystemUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlCPUSystemUtilization5Min.setStatus("current")


class _RsUtlCPUUserUtilization5Min_Type(Unsigned32):
    """Custom type rsUtlCPUUserUtilization5Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsUtlCPUUserUtilization5Min_Type.__name__ = "Unsigned32"
_RsUtlCPUUserUtilization5Min_Object = MibTableColumn
rsUtlCPUUserUtilization5Min = _RsUtlCPUUserUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 5, 1, 1, 6),
    _RsUtlCPUUserUtilization5Min_Type()
)
rsUtlCPUUserUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlCPUUserUtilization5Min.setStatus("current")
_RsMemory_ObjectIdentity = ObjectIdentity
rsMemory = _RsMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 10)
)
if mibBuilder.loadTexts:
    rsMemory.setStatus("current")
_RsUtlMemoryTable_Object = MibTable
rsUtlMemoryTable = _RsUtlMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 10, 1)
)
if mibBuilder.loadTexts:
    rsUtlMemoryTable.setStatus("current")
_RsUtlMemoryEntry_Object = MibTableRow
rsUtlMemoryEntry = _RsUtlMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 10, 1, 1)
)
rsUtlMemoryEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    rsUtlMemoryEntry.setStatus("current")
_RsUtlMemoryActivePages5Sec_Type = Unsigned32
_RsUtlMemoryActivePages5Sec_Object = MibTableColumn
rsUtlMemoryActivePages5Sec = _RsUtlMemoryActivePages5Sec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 10, 1, 1, 1),
    _RsUtlMemoryActivePages5Sec_Type()
)
rsUtlMemoryActivePages5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlMemoryActivePages5Sec.setStatus("current")
_RsUtlMemoryFreePages5Sec_Type = Unsigned32
_RsUtlMemoryFreePages5Sec_Object = MibTableColumn
rsUtlMemoryFreePages5Sec = _RsUtlMemoryFreePages5Sec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 10, 1, 1, 2),
    _RsUtlMemoryFreePages5Sec_Type()
)
rsUtlMemoryFreePages5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlMemoryFreePages5Sec.setStatus("current")
_RsUtlMemoryActivePages60Sec_Type = Unsigned32
_RsUtlMemoryActivePages60Sec_Object = MibTableColumn
rsUtlMemoryActivePages60Sec = _RsUtlMemoryActivePages60Sec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 10, 1, 1, 3),
    _RsUtlMemoryActivePages60Sec_Type()
)
rsUtlMemoryActivePages60Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlMemoryActivePages60Sec.setStatus("current")
_RsUtlMemoryFreePages60Sec_Type = Unsigned32
_RsUtlMemoryFreePages60Sec_Object = MibTableColumn
rsUtlMemoryFreePages60Sec = _RsUtlMemoryFreePages60Sec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 10, 1, 1, 4),
    _RsUtlMemoryFreePages60Sec_Type()
)
rsUtlMemoryFreePages60Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlMemoryFreePages60Sec.setStatus("current")
_RsUtlMemoryActivePages5Min_Type = Unsigned32
_RsUtlMemoryActivePages5Min_Object = MibTableColumn
rsUtlMemoryActivePages5Min = _RsUtlMemoryActivePages5Min_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 10, 1, 1, 5),
    _RsUtlMemoryActivePages5Min_Type()
)
rsUtlMemoryActivePages5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlMemoryActivePages5Min.setStatus("current")
_RsUtlMemoryFreePages5Min_Type = Unsigned32
_RsUtlMemoryFreePages5Min_Object = MibTableColumn
rsUtlMemoryFreePages5Min = _RsUtlMemoryFreePages5Min_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 10, 1, 1, 6),
    _RsUtlMemoryFreePages5Min_Type()
)
rsUtlMemoryFreePages5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUtlMemoryFreePages5Min.setStatus("current")


class _RsUtlSamplingRate_Type(Unsigned32):
    """Custom type rsUtlSamplingRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_RsUtlSamplingRate_Type.__name__ = "Unsigned32"
_RsUtlSamplingRate_Object = MibScalar
rsUtlSamplingRate = _RsUtlSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 25),
    _RsUtlSamplingRate_Type()
)
rsUtlSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsUtlSamplingRate.setStatus("current")
_RsUtlConformance_ObjectIdentity = ObjectIdentity
rsUtlConformance = _RsUtlConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 35)
)
if mibBuilder.loadTexts:
    rsUtlConformance.setStatus("current")
_RsUtlCompliances_ObjectIdentity = ObjectIdentity
rsUtlCompliances = _RsUtlCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 35, 1)
)
_RsUtlGroups_ObjectIdentity = ObjectIdentity
rsUtlGroups = _RsUtlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 35, 2)
)

# Managed Objects groups

rsUtlConfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 35, 2, 1)
)
rsUtlConfGroupV1.setObjects(
      *(("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlMemoryActivePages5Sec"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlMemoryFreePages5Sec"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlCPUSystemUtilization5Sec"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlCPUUserUtilization5Sec"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlCPUSystemUtilization60Sec"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlCPUUserUtilization60Sec"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlCPUSystemUtilization5Min"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlCPUUserUtilization5Min"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlMemoryActivePages60Sec"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlMemoryFreePages60Sec"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlMemoryActivePages5Min"),
        ("RIVERSTONE-SYSTEM-RESOURCES-MIB", "rsUtlMemoryFreePages5Min"))
)
if mibBuilder.loadTexts:
    rsUtlConfGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsUtlComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 281, 5, 35, 1, 1)
)
if mibBuilder.loadTexts:
    rsUtlComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-SYSTEM-RESOURCES-MIB",
    **{"rsSystemResourcesMIB": rsSystemResourcesMIB,
       "rsSystemUtilization": rsSystemUtilization,
       "rsCpuUtl": rsCpuUtl,
       "rsUtlCPUTable": rsUtlCPUTable,
       "rsUtlCPUEntry": rsUtlCPUEntry,
       "rsUtlCPUSystemUtilization5Sec": rsUtlCPUSystemUtilization5Sec,
       "rsUtlCPUUserUtilization5Sec": rsUtlCPUUserUtilization5Sec,
       "rsUtlCPUSystemUtilization60Sec": rsUtlCPUSystemUtilization60Sec,
       "rsUtlCPUUserUtilization60Sec": rsUtlCPUUserUtilization60Sec,
       "rsUtlCPUSystemUtilization5Min": rsUtlCPUSystemUtilization5Min,
       "rsUtlCPUUserUtilization5Min": rsUtlCPUUserUtilization5Min,
       "rsMemory": rsMemory,
       "rsUtlMemoryTable": rsUtlMemoryTable,
       "rsUtlMemoryEntry": rsUtlMemoryEntry,
       "rsUtlMemoryActivePages5Sec": rsUtlMemoryActivePages5Sec,
       "rsUtlMemoryFreePages5Sec": rsUtlMemoryFreePages5Sec,
       "rsUtlMemoryActivePages60Sec": rsUtlMemoryActivePages60Sec,
       "rsUtlMemoryFreePages60Sec": rsUtlMemoryFreePages60Sec,
       "rsUtlMemoryActivePages5Min": rsUtlMemoryActivePages5Min,
       "rsUtlMemoryFreePages5Min": rsUtlMemoryFreePages5Min,
       "rsUtlSamplingRate": rsUtlSamplingRate,
       "rsUtlConformance": rsUtlConformance,
       "rsUtlCompliances": rsUtlCompliances,
       "rsUtlComplianceV1": rsUtlComplianceV1,
       "rsUtlGroups": rsUtlGroups,
       "rsUtlConfGroupV1": rsUtlConfGroupV1}
)
