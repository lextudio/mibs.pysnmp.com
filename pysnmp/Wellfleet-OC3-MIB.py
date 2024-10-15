# SNMP MIB module (Wellfleet-OC3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-OC3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:49 2024
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

(wfSonetGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSonetGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfOc3ConfigTable_Object = MibTable
wfOc3ConfigTable = _WfOc3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 12)
)
if mibBuilder.loadTexts:
    wfOc3ConfigTable.setStatus("mandatory")
_WfOc3ConfigEntry_Object = MibTableRow
wfOc3ConfigEntry = _WfOc3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 12, 1)
)
wfOc3ConfigEntry.setIndexNames(
    (0, "Wellfleet-OC3-MIB", "wfOc3ConfigIndex"),
)
if mibBuilder.loadTexts:
    wfOc3ConfigEntry.setStatus("mandatory")


class _WfOc3ConfigDelete_Type(Integer32):
    """Custom type wfOc3ConfigDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfOc3ConfigDelete_Type.__name__ = "Integer32"
_WfOc3ConfigDelete_Object = MibTableColumn
wfOc3ConfigDelete = _WfOc3ConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 12, 1, 1),
    _WfOc3ConfigDelete_Type()
)
wfOc3ConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOc3ConfigDelete.setStatus("mandatory")
_WfOc3ConfigIndex_Type = Integer32
_WfOc3ConfigIndex_Object = MibTableColumn
wfOc3ConfigIndex = _WfOc3ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 12, 1, 2),
    _WfOc3ConfigIndex_Type()
)
wfOc3ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc3ConfigIndex.setStatus("mandatory")
_WfOc3ConfigType_Type = Integer32
_WfOc3ConfigType_Object = MibTableColumn
wfOc3ConfigType = _WfOc3ConfigType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 12, 1, 3),
    _WfOc3ConfigType_Type()
)
wfOc3ConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc3ConfigType.setStatus("mandatory")
_WfOc3ConfigTimeElapsed_Type = Integer32
_WfOc3ConfigTimeElapsed_Object = MibTableColumn
wfOc3ConfigTimeElapsed = _WfOc3ConfigTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 12, 1, 4),
    _WfOc3ConfigTimeElapsed_Type()
)
wfOc3ConfigTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc3ConfigTimeElapsed.setStatus("mandatory")
_WfOc3ConfigValidIntervals_Type = Integer32
_WfOc3ConfigValidIntervals_Object = MibTableColumn
wfOc3ConfigValidIntervals = _WfOc3ConfigValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 12, 1, 5),
    _WfOc3ConfigValidIntervals_Type()
)
wfOc3ConfigValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc3ConfigValidIntervals.setStatus("mandatory")


class _WfOc3ConfigLineCoding_Type(Integer32):
    """Custom type wfOc3ConfigLineCoding based on Integer32"""
    defaultValue = 4

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
        *(("b3zs", 2),
          ("cmi", 3),
          ("nrz", 4),
          ("other", 1),
          ("rz", 5))
    )


_WfOc3ConfigLineCoding_Type.__name__ = "Integer32"
_WfOc3ConfigLineCoding_Object = MibTableColumn
wfOc3ConfigLineCoding = _WfOc3ConfigLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 12, 1, 6),
    _WfOc3ConfigLineCoding_Type()
)
wfOc3ConfigLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOc3ConfigLineCoding.setStatus("mandatory")


class _WfOc3ConfigLineType_Type(Integer32):
    """Custom type wfOc3ConfigLineType based on Integer32"""
    defaultValue = 2

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
        *(("coax", 5),
          ("longsinglemode", 3),
          ("multimode", 4),
          ("other", 1),
          ("shortsinglemode", 2),
          ("utp", 6))
    )


_WfOc3ConfigLineType_Type.__name__ = "Integer32"
_WfOc3ConfigLineType_Object = MibTableColumn
wfOc3ConfigLineType = _WfOc3ConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 12, 1, 7),
    _WfOc3ConfigLineType_Type()
)
wfOc3ConfigLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfOc3ConfigLineType.setStatus("mandatory")
_WfOc3ConfigCircuitIdentifier_Type = DisplayString
_WfOc3ConfigCircuitIdentifier_Object = MibTableColumn
wfOc3ConfigCircuitIdentifier = _WfOc3ConfigCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 24, 12, 1, 8),
    _WfOc3ConfigCircuitIdentifier_Type()
)
wfOc3ConfigCircuitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOc3ConfigCircuitIdentifier.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-OC3-MIB",
    **{"wfOc3ConfigTable": wfOc3ConfigTable,
       "wfOc3ConfigEntry": wfOc3ConfigEntry,
       "wfOc3ConfigDelete": wfOc3ConfigDelete,
       "wfOc3ConfigIndex": wfOc3ConfigIndex,
       "wfOc3ConfigType": wfOc3ConfigType,
       "wfOc3ConfigTimeElapsed": wfOc3ConfigTimeElapsed,
       "wfOc3ConfigValidIntervals": wfOc3ConfigValidIntervals,
       "wfOc3ConfigLineCoding": wfOc3ConfigLineCoding,
       "wfOc3ConfigLineType": wfOc3ConfigLineType,
       "wfOc3ConfigCircuitIdentifier": wfOc3ConfigCircuitIdentifier}
)
