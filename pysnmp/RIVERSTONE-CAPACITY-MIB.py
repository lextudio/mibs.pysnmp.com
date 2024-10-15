# SNMP MIB module (RIVERSTONE-CAPACITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-CAPACITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:42 2024
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

rsCapacityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270)
)
rsCapacityMIB.setRevisions(
        ("2003-04-04 13:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsCpu_ObjectIdentity = ObjectIdentity
rsCpu = _RsCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 5)
)
if mibBuilder.loadTexts:
    rsCpu.setStatus("current")
_RsCapCPUTable_Object = MibTable
rsCapCPUTable = _RsCapCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1)
)
if mibBuilder.loadTexts:
    rsCapCPUTable.setStatus("current")
_RsCapCPUEntry_Object = MibTableRow
rsCapCPUEntry = _RsCapCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1, 1)
)
rsCapCPUEntry.setIndexNames(
    (0, "RIVERSTONE-CAPACITY-MIB", "rsCapCPUModuleIndex"),
)
if mibBuilder.loadTexts:
    rsCapCPUEntry.setStatus("current")
_RsCapCPUModuleIndex_Type = Unsigned32
_RsCapCPUModuleIndex_Object = MibTableColumn
rsCapCPUModuleIndex = _RsCapCPUModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1, 1, 1),
    _RsCapCPUModuleIndex_Type()
)
rsCapCPUModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsCapCPUModuleIndex.setStatus("current")


class _RsCapCPUCurrentUtilization5Sec_Type(Unsigned32):
    """Custom type rsCapCPUCurrentUtilization5Sec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsCapCPUCurrentUtilization5Sec_Type.__name__ = "Unsigned32"
_RsCapCPUCurrentUtilization5Sec_Object = MibTableColumn
rsCapCPUCurrentUtilization5Sec = _RsCapCPUCurrentUtilization5Sec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1, 1, 2),
    _RsCapCPUCurrentUtilization5Sec_Type()
)
rsCapCPUCurrentUtilization5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCapCPUCurrentUtilization5Sec.setStatus("current")


class _RsCapCPUCurrentUtilization60Sec_Type(Unsigned32):
    """Custom type rsCapCPUCurrentUtilization60Sec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsCapCPUCurrentUtilization60Sec_Type.__name__ = "Unsigned32"
_RsCapCPUCurrentUtilization60Sec_Object = MibTableColumn
rsCapCPUCurrentUtilization60Sec = _RsCapCPUCurrentUtilization60Sec_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1, 1, 3),
    _RsCapCPUCurrentUtilization60Sec_Type()
)
rsCapCPUCurrentUtilization60Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCapCPUCurrentUtilization60Sec.setStatus("current")


class _RsCapCPUCurrentUtilization5Min_Type(Unsigned32):
    """Custom type rsCapCPUCurrentUtilization5Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsCapCPUCurrentUtilization5Min_Type.__name__ = "Unsigned32"
_RsCapCPUCurrentUtilization5Min_Object = MibTableColumn
rsCapCPUCurrentUtilization5Min = _RsCapCPUCurrentUtilization5Min_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 5, 1, 1, 4),
    _RsCapCPUCurrentUtilization5Min_Type()
)
rsCapCPUCurrentUtilization5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsCapCPUCurrentUtilization5Min.setStatus("current")
_RsCapConformance_ObjectIdentity = ObjectIdentity
rsCapConformance = _RsCapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 35)
)
if mibBuilder.loadTexts:
    rsCapConformance.setStatus("current")
_RsCapCompliances_ObjectIdentity = ObjectIdentity
rsCapCompliances = _RsCapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 35, 1)
)
_RsCapGroups_ObjectIdentity = ObjectIdentity
rsCapGroups = _RsCapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 35, 2)
)

# Managed Objects groups

rsCapConfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 35, 2, 1)
)
rsCapConfGroupV1.setObjects(
      *(("RIVERSTONE-CAPACITY-MIB", "rsCapCPUCurrentUtilization5Sec"),
        ("RIVERSTONE-CAPACITY-MIB", "rsCapCPUCurrentUtilization60Sec"),
        ("RIVERSTONE-CAPACITY-MIB", "rsCapCPUCurrentUtilization5Min"))
)
if mibBuilder.loadTexts:
    rsCapConfGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsCapComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 270, 35, 1, 1)
)
if mibBuilder.loadTexts:
    rsCapComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-CAPACITY-MIB",
    **{"rsCapacityMIB": rsCapacityMIB,
       "rsCpu": rsCpu,
       "rsCapCPUTable": rsCapCPUTable,
       "rsCapCPUEntry": rsCapCPUEntry,
       "rsCapCPUModuleIndex": rsCapCPUModuleIndex,
       "rsCapCPUCurrentUtilization5Sec": rsCapCPUCurrentUtilization5Sec,
       "rsCapCPUCurrentUtilization60Sec": rsCapCPUCurrentUtilization60Sec,
       "rsCapCPUCurrentUtilization5Min": rsCapCPUCurrentUtilization5Min,
       "rsCapConformance": rsCapConformance,
       "rsCapCompliances": rsCapCompliances,
       "rsCapComplianceV1": rsCapComplianceV1,
       "rsCapGroups": rsCapGroups,
       "rsCapConfGroupV1": rsCapConfGroupV1}
)
