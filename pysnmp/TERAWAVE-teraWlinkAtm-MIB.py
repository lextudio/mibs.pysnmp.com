# SNMP MIB module (TERAWAVE-teraWlinkAtm-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraWlinkAtm-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:21 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraWaveLinkGroup_ObjectIdentity = ObjectIdentity
teraWaveLinkGroup = _TeraWaveLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 6)
)
_TeraWlinkAtm_Object = MibTable
teraWlinkAtm = _TeraWlinkAtm_Object(
    (1, 3, 6, 1, 4, 1, 4513, 6, 1)
)
if mibBuilder.loadTexts:
    teraWlinkAtm.setStatus("mandatory")
_TeraWlinkAtmEntry_Object = MibTableRow
teraWlinkAtmEntry = _TeraWlinkAtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 6, 1, 1)
)
teraWlinkAtmEntry.setIndexNames(
    (0, "TERAWAVE-teraWlinkAtm-MIB", "teraWlinkAtmIndex"),
)
if mibBuilder.loadTexts:
    teraWlinkAtmEntry.setStatus("mandatory")


class _TeraWlinkAtmIndex_Type(Integer32):
    """Custom type teraWlinkAtmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TeraWlinkAtmIndex_Type.__name__ = "Integer32"
_TeraWlinkAtmIndex_Object = MibTableColumn
teraWlinkAtmIndex = _TeraWlinkAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 1),
    _TeraWlinkAtmIndex_Type()
)
teraWlinkAtmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraWlinkAtmIndex.setStatus("mandatory")
_UTOPIACellDrops_Type = Counter32
_UTOPIACellDrops_Object = MibTableColumn
uTOPIACellDrops = _UTOPIACellDrops_Object(
    (1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 2),
    _UTOPIACellDrops_Type()
)
uTOPIACellDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uTOPIACellDrops.setStatus("mandatory")
_MisinsertedCells_Type = Counter32
_MisinsertedCells_Object = MibTableColumn
misinsertedCells = _MisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 3),
    _MisinsertedCells_Type()
)
misinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misinsertedCells.setStatus("mandatory")
_F4SegCells_Type = Counter32
_F4SegCells_Object = MibTableColumn
f4SegCells = _F4SegCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 4),
    _F4SegCells_Type()
)
f4SegCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4SegCells.setStatus("mandatory")
_F4EndToEndCells_Type = Counter32
_F4EndToEndCells_Object = MibTableColumn
f4EndToEndCells = _F4EndToEndCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 5),
    _F4EndToEndCells_Type()
)
f4EndToEndCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f4EndToEndCells.setStatus("mandatory")
_F5SegCells_Type = Counter32
_F5SegCells_Object = MibTableColumn
f5SegCells = _F5SegCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 6),
    _F5SegCells_Type()
)
f5SegCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5SegCells.setStatus("mandatory")
_F5EndToEndCells_Type = Counter32
_F5EndToEndCells_Object = MibTableColumn
f5EndToEndCells = _F5EndToEndCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 7),
    _F5EndToEndCells_Type()
)
f5EndToEndCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f5EndToEndCells.setStatus("mandatory")
_MisinsertedOAMCells_Type = Counter32
_MisinsertedOAMCells_Object = MibTableColumn
misinsertedOAMCells = _MisinsertedOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 4513, 6, 1, 1, 8),
    _MisinsertedOAMCells_Type()
)
misinsertedOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    misinsertedOAMCells.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraWlinkAtm-MIB",
    **{"terawave": terawave,
       "teraWaveLinkGroup": teraWaveLinkGroup,
       "teraWlinkAtm": teraWlinkAtm,
       "teraWlinkAtmEntry": teraWlinkAtmEntry,
       "teraWlinkAtmIndex": teraWlinkAtmIndex,
       "uTOPIACellDrops": uTOPIACellDrops,
       "misinsertedCells": misinsertedCells,
       "f4SegCells": f4SegCells,
       "f4EndToEndCells": f4EndToEndCells,
       "f5SegCells": f5SegCells,
       "f5EndToEndCells": f5EndToEndCells,
       "misinsertedOAMCells": misinsertedOAMCells}
)
