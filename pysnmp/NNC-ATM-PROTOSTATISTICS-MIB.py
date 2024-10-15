# SNMP MIB module (NNC-ATM-PROTOSTATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNC-ATM-PROTOSTATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:10 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(NncExtCounter64,
 nncExtensions) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "NncExtCounter64",
    "nncExtensions")

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

nncAtmProtoStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 54)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncAtmProtoObjects_ObjectIdentity = ObjectIdentity
nncAtmProtoObjects = _NncAtmProtoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1)
)
_NncAtmProtoCurrTable_Object = MibTable
nncAtmProtoCurrTable = _NncAtmProtoCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 1)
)
if mibBuilder.loadTexts:
    nncAtmProtoCurrTable.setStatus("current")
_NncAtmProtoCurrEntry_Object = MibTableRow
nncAtmProtoCurrEntry = _NncAtmProtoCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 1, 1)
)
nncAtmProtoCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncAtmProtoCurrEntry.setStatus("current")
_NncAtmProtoCurrValidInCells_Type = NncExtCounter64
_NncAtmProtoCurrValidInCells_Object = MibTableColumn
nncAtmProtoCurrValidInCells = _NncAtmProtoCurrValidInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 1, 1, 1),
    _NncAtmProtoCurrValidInCells_Type()
)
nncAtmProtoCurrValidInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoCurrValidInCells.setStatus("current")
_NncAtmProtoCurrCorrHeaderInCells_Type = NncExtCounter64
_NncAtmProtoCurrCorrHeaderInCells_Object = MibTableColumn
nncAtmProtoCurrCorrHeaderInCells = _NncAtmProtoCurrCorrHeaderInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 1, 1, 2),
    _NncAtmProtoCurrCorrHeaderInCells_Type()
)
nncAtmProtoCurrCorrHeaderInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoCurrCorrHeaderInCells.setStatus("current")
_NncAtmProtoCurrDisHECInCells_Type = NncExtCounter64
_NncAtmProtoCurrDisHECInCells_Object = MibTableColumn
nncAtmProtoCurrDisHECInCells = _NncAtmProtoCurrDisHECInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 1, 1, 3),
    _NncAtmProtoCurrDisHECInCells_Type()
)
nncAtmProtoCurrDisHECInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoCurrDisHECInCells.setStatus("current")
_NncAtmProtoCurrDisInvalidVPIVCIInCells_Type = NncExtCounter64
_NncAtmProtoCurrDisInvalidVPIVCIInCells_Object = MibTableColumn
nncAtmProtoCurrDisInvalidVPIVCIInCells = _NncAtmProtoCurrDisInvalidVPIVCIInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 1, 1, 4),
    _NncAtmProtoCurrDisInvalidVPIVCIInCells_Type()
)
nncAtmProtoCurrDisInvalidVPIVCIInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoCurrDisInvalidVPIVCIInCells.setStatus("current")
_NncAtmProtoCurrOutCells_Type = NncExtCounter64
_NncAtmProtoCurrOutCells_Object = MibTableColumn
nncAtmProtoCurrOutCells = _NncAtmProtoCurrOutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 1, 1, 5),
    _NncAtmProtoCurrOutCells_Type()
)
nncAtmProtoCurrOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoCurrOutCells.setStatus("current")
_NncAtmProtoHistTable_Object = MibTable
nncAtmProtoHistTable = _NncAtmProtoHistTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 2)
)
if mibBuilder.loadTexts:
    nncAtmProtoHistTable.setStatus("current")
_NncAtmProtoHistEntry_Object = MibTableRow
nncAtmProtoHistEntry = _NncAtmProtoHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 2, 1)
)
nncAtmProtoHistEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoHistIndex"),
)
if mibBuilder.loadTexts:
    nncAtmProtoHistEntry.setStatus("current")


class _NncAtmProtoHistIndex_Type(Integer32):
    """Custom type nncAtmProtoHistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncAtmProtoHistIndex_Type.__name__ = "Integer32"
_NncAtmProtoHistIndex_Object = MibTableColumn
nncAtmProtoHistIndex = _NncAtmProtoHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 2, 1, 1),
    _NncAtmProtoHistIndex_Type()
)
nncAtmProtoHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncAtmProtoHistIndex.setStatus("current")
_NncAtmProtoHistValidInCells_Type = NncExtCounter64
_NncAtmProtoHistValidInCells_Object = MibTableColumn
nncAtmProtoHistValidInCells = _NncAtmProtoHistValidInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 2, 1, 2),
    _NncAtmProtoHistValidInCells_Type()
)
nncAtmProtoHistValidInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoHistValidInCells.setStatus("current")
_NncAtmProtoHistCorrHeaderInCells_Type = NncExtCounter64
_NncAtmProtoHistCorrHeaderInCells_Object = MibTableColumn
nncAtmProtoHistCorrHeaderInCells = _NncAtmProtoHistCorrHeaderInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 2, 1, 3),
    _NncAtmProtoHistCorrHeaderInCells_Type()
)
nncAtmProtoHistCorrHeaderInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoHistCorrHeaderInCells.setStatus("current")
_NncAtmProtoHistDisHECInCells_Type = NncExtCounter64
_NncAtmProtoHistDisHECInCells_Object = MibTableColumn
nncAtmProtoHistDisHECInCells = _NncAtmProtoHistDisHECInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 2, 1, 4),
    _NncAtmProtoHistDisHECInCells_Type()
)
nncAtmProtoHistDisHECInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoHistDisHECInCells.setStatus("current")
_NncAtmProtoHistDisInvalidVPIVCIInCells_Type = NncExtCounter64
_NncAtmProtoHistDisInvalidVPIVCIInCells_Object = MibTableColumn
nncAtmProtoHistDisInvalidVPIVCIInCells = _NncAtmProtoHistDisInvalidVPIVCIInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 2, 1, 5),
    _NncAtmProtoHistDisInvalidVPIVCIInCells_Type()
)
nncAtmProtoHistDisInvalidVPIVCIInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoHistDisInvalidVPIVCIInCells.setStatus("current")
_NncAtmProtoHistOutCells_Type = NncExtCounter64
_NncAtmProtoHistOutCells_Object = MibTableColumn
nncAtmProtoHistOutCells = _NncAtmProtoHistOutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 2, 1, 6),
    _NncAtmProtoHistOutCells_Type()
)
nncAtmProtoHistOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoHistOutCells.setStatus("current")
_NncAtmProtoTotalTable_Object = MibTable
nncAtmProtoTotalTable = _NncAtmProtoTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 3)
)
if mibBuilder.loadTexts:
    nncAtmProtoTotalTable.setStatus("current")
_NncAtmProtoTotalEntry_Object = MibTableRow
nncAtmProtoTotalEntry = _NncAtmProtoTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 3, 1)
)
nncAtmProtoTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncAtmProtoTotalEntry.setStatus("current")


class _NncAtmProtoTotalValidIntervals_Type(Integer32):
    """Custom type nncAtmProtoTotalValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncAtmProtoTotalValidIntervals_Type.__name__ = "Integer32"
_NncAtmProtoTotalValidIntervals_Object = MibTableColumn
nncAtmProtoTotalValidIntervals = _NncAtmProtoTotalValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 3, 1, 1),
    _NncAtmProtoTotalValidIntervals_Type()
)
nncAtmProtoTotalValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoTotalValidIntervals.setStatus("current")
_NncAtmProtoTotalValidInCells_Type = NncExtCounter64
_NncAtmProtoTotalValidInCells_Object = MibTableColumn
nncAtmProtoTotalValidInCells = _NncAtmProtoTotalValidInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 3, 1, 2),
    _NncAtmProtoTotalValidInCells_Type()
)
nncAtmProtoTotalValidInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoTotalValidInCells.setStatus("current")
_NncAtmProtoTotalCorrHeaderInCells_Type = NncExtCounter64
_NncAtmProtoTotalCorrHeaderInCells_Object = MibTableColumn
nncAtmProtoTotalCorrHeaderInCells = _NncAtmProtoTotalCorrHeaderInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 3, 1, 3),
    _NncAtmProtoTotalCorrHeaderInCells_Type()
)
nncAtmProtoTotalCorrHeaderInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoTotalCorrHeaderInCells.setStatus("current")
_NncAtmProtoTotalDisHECInCells_Type = NncExtCounter64
_NncAtmProtoTotalDisHECInCells_Object = MibTableColumn
nncAtmProtoTotalDisHECInCells = _NncAtmProtoTotalDisHECInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 3, 1, 4),
    _NncAtmProtoTotalDisHECInCells_Type()
)
nncAtmProtoTotalDisHECInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoTotalDisHECInCells.setStatus("current")
_NncAtmProtoTotalDisInvalidVPIVCIInCells_Type = NncExtCounter64
_NncAtmProtoTotalDisInvalidVPIVCIInCells_Object = MibTableColumn
nncAtmProtoTotalDisInvalidVPIVCIInCells = _NncAtmProtoTotalDisInvalidVPIVCIInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 3, 1, 5),
    _NncAtmProtoTotalDisInvalidVPIVCIInCells_Type()
)
nncAtmProtoTotalDisInvalidVPIVCIInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoTotalDisInvalidVPIVCIInCells.setStatus("current")
_NncAtmProtoTotalOutCells_Type = NncExtCounter64
_NncAtmProtoTotalOutCells_Object = MibTableColumn
nncAtmProtoTotalOutCells = _NncAtmProtoTotalOutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 3, 1, 6),
    _NncAtmProtoTotalOutCells_Type()
)
nncAtmProtoTotalOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoTotalOutCells.setStatus("current")
_NncAtmProtoRawTable_Object = MibTable
nncAtmProtoRawTable = _NncAtmProtoRawTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 4)
)
if mibBuilder.loadTexts:
    nncAtmProtoRawTable.setStatus("current")
_NncAtmProtoRawEntry_Object = MibTableRow
nncAtmProtoRawEntry = _NncAtmProtoRawEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 4, 1)
)
nncAtmProtoRawEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncAtmProtoRawEntry.setStatus("current")
_NncAtmProtoRawValidInCells_Type = Counter32
_NncAtmProtoRawValidInCells_Object = MibTableColumn
nncAtmProtoRawValidInCells = _NncAtmProtoRawValidInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 4, 1, 1),
    _NncAtmProtoRawValidInCells_Type()
)
nncAtmProtoRawValidInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoRawValidInCells.setStatus("current")
_NncAtmProtoRawCorrHeaderInCells_Type = Counter32
_NncAtmProtoRawCorrHeaderInCells_Object = MibTableColumn
nncAtmProtoRawCorrHeaderInCells = _NncAtmProtoRawCorrHeaderInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 4, 1, 2),
    _NncAtmProtoRawCorrHeaderInCells_Type()
)
nncAtmProtoRawCorrHeaderInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoRawCorrHeaderInCells.setStatus("current")
_NncAtmProtoRawDisHECInCells_Type = Counter32
_NncAtmProtoRawDisHECInCells_Object = MibTableColumn
nncAtmProtoRawDisHECInCells = _NncAtmProtoRawDisHECInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 4, 1, 3),
    _NncAtmProtoRawDisHECInCells_Type()
)
nncAtmProtoRawDisHECInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoRawDisHECInCells.setStatus("current")
_NncAtmProtoRawDisInvalidVPIVCIInCells_Type = Counter32
_NncAtmProtoRawDisInvalidVPIVCIInCells_Object = MibTableColumn
nncAtmProtoRawDisInvalidVPIVCIInCells = _NncAtmProtoRawDisInvalidVPIVCIInCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 4, 1, 4),
    _NncAtmProtoRawDisInvalidVPIVCIInCells_Type()
)
nncAtmProtoRawDisInvalidVPIVCIInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoRawDisInvalidVPIVCIInCells.setStatus("current")
_NncAtmProtoRawOutCells_Type = Counter32
_NncAtmProtoRawOutCells_Object = MibTableColumn
nncAtmProtoRawOutCells = _NncAtmProtoRawOutCells_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 1, 4, 1, 5),
    _NncAtmProtoRawOutCells_Type()
)
nncAtmProtoRawOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncAtmProtoRawOutCells.setStatus("current")
_NncAtmProtoGroups_ObjectIdentity = ObjectIdentity
nncAtmProtoGroups = _NncAtmProtoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 2)
)
_NncAtmProtoCompliances_ObjectIdentity = ObjectIdentity
nncAtmProtoCompliances = _NncAtmProtoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 3)
)

# Managed Objects groups

nncAtmProtoCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 2, 1)
)
nncAtmProtoCurrGroup.setObjects(
      *(("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoCurrValidInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoCurrCorrHeaderInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoCurrDisHECInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoCurrDisInvalidVPIVCIInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoCurrOutCells"))
)
if mibBuilder.loadTexts:
    nncAtmProtoCurrGroup.setStatus("current")

nncAtmProtoHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 2, 2)
)
nncAtmProtoHistGroup.setObjects(
      *(("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoHistIndex"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoHistValidInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoHistCorrHeaderInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoHistDisHECInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoHistDisInvalidVPIVCIInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoHistOutCells"))
)
if mibBuilder.loadTexts:
    nncAtmProtoHistGroup.setStatus("current")

nncAtmProtoTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 2, 3)
)
nncAtmProtoTotalGroup.setObjects(
      *(("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoTotalValidIntervals"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoTotalValidInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoTotalCorrHeaderInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoTotalDisHECInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoTotalDisInvalidVPIVCIInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoTotalOutCells"))
)
if mibBuilder.loadTexts:
    nncAtmProtoTotalGroup.setStatus("current")

nncAtmProtoRawGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 2, 4)
)
nncAtmProtoRawGroup.setObjects(
      *(("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoRawValidInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoRawCorrHeaderInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoRawDisHECInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoRawDisInvalidVPIVCIInCells"),
        ("NNC-ATM-PROTOSTATISTICS-MIB", "nncAtmProtoRawOutCells"))
)
if mibBuilder.loadTexts:
    nncAtmProtoRawGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncAtmProtoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 54, 3, 1)
)
if mibBuilder.loadTexts:
    nncAtmProtoCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNC-ATM-PROTOSTATISTICS-MIB",
    **{"nncAtmProtoStatistics": nncAtmProtoStatistics,
       "nncAtmProtoObjects": nncAtmProtoObjects,
       "nncAtmProtoCurrTable": nncAtmProtoCurrTable,
       "nncAtmProtoCurrEntry": nncAtmProtoCurrEntry,
       "nncAtmProtoCurrValidInCells": nncAtmProtoCurrValidInCells,
       "nncAtmProtoCurrCorrHeaderInCells": nncAtmProtoCurrCorrHeaderInCells,
       "nncAtmProtoCurrDisHECInCells": nncAtmProtoCurrDisHECInCells,
       "nncAtmProtoCurrDisInvalidVPIVCIInCells": nncAtmProtoCurrDisInvalidVPIVCIInCells,
       "nncAtmProtoCurrOutCells": nncAtmProtoCurrOutCells,
       "nncAtmProtoHistTable": nncAtmProtoHistTable,
       "nncAtmProtoHistEntry": nncAtmProtoHistEntry,
       "nncAtmProtoHistIndex": nncAtmProtoHistIndex,
       "nncAtmProtoHistValidInCells": nncAtmProtoHistValidInCells,
       "nncAtmProtoHistCorrHeaderInCells": nncAtmProtoHistCorrHeaderInCells,
       "nncAtmProtoHistDisHECInCells": nncAtmProtoHistDisHECInCells,
       "nncAtmProtoHistDisInvalidVPIVCIInCells": nncAtmProtoHistDisInvalidVPIVCIInCells,
       "nncAtmProtoHistOutCells": nncAtmProtoHistOutCells,
       "nncAtmProtoTotalTable": nncAtmProtoTotalTable,
       "nncAtmProtoTotalEntry": nncAtmProtoTotalEntry,
       "nncAtmProtoTotalValidIntervals": nncAtmProtoTotalValidIntervals,
       "nncAtmProtoTotalValidInCells": nncAtmProtoTotalValidInCells,
       "nncAtmProtoTotalCorrHeaderInCells": nncAtmProtoTotalCorrHeaderInCells,
       "nncAtmProtoTotalDisHECInCells": nncAtmProtoTotalDisHECInCells,
       "nncAtmProtoTotalDisInvalidVPIVCIInCells": nncAtmProtoTotalDisInvalidVPIVCIInCells,
       "nncAtmProtoTotalOutCells": nncAtmProtoTotalOutCells,
       "nncAtmProtoRawTable": nncAtmProtoRawTable,
       "nncAtmProtoRawEntry": nncAtmProtoRawEntry,
       "nncAtmProtoRawValidInCells": nncAtmProtoRawValidInCells,
       "nncAtmProtoRawCorrHeaderInCells": nncAtmProtoRawCorrHeaderInCells,
       "nncAtmProtoRawDisHECInCells": nncAtmProtoRawDisHECInCells,
       "nncAtmProtoRawDisInvalidVPIVCIInCells": nncAtmProtoRawDisInvalidVPIVCIInCells,
       "nncAtmProtoRawOutCells": nncAtmProtoRawOutCells,
       "nncAtmProtoGroups": nncAtmProtoGroups,
       "nncAtmProtoCurrGroup": nncAtmProtoCurrGroup,
       "nncAtmProtoHistGroup": nncAtmProtoHistGroup,
       "nncAtmProtoTotalGroup": nncAtmProtoTotalGroup,
       "nncAtmProtoRawGroup": nncAtmProtoRawGroup,
       "nncAtmProtoCompliances": nncAtmProtoCompliances,
       "nncAtmProtoCompliance": nncAtmProtoCompliance}
)
