# SNMP MIB module (TERAWAVE-teraMau-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraMau-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:17 2024
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
_TeraMauTable_Object = MibTable
teraMauTable = _TeraMauTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 18)
)
if mibBuilder.loadTexts:
    teraMauTable.setStatus("mandatory")
_TeraMauTableEntry_Object = MibTableRow
teraMauTableEntry = _TeraMauTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 18, 1)
)
teraMauTableEntry.setIndexNames(
    (0, "TERAWAVE-teraMau-MIB", "ifMauIfIndex"),
    (0, "TERAWAVE-teraMau-MIB", "ifMauIndex"),
)
if mibBuilder.loadTexts:
    teraMauTableEntry.setStatus("mandatory")


class _TeraMauLinkState_Type(Integer32):
    """Custom type teraMauLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TeraMauLinkState_Type.__name__ = "Integer32"
_TeraMauLinkState_Object = MibTableColumn
teraMauLinkState = _TeraMauLinkState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 18, 1, 1),
    _TeraMauLinkState_Type()
)
teraMauLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraMauLinkState.setStatus("mandatory")


class _TeraMauDuplexMode_Type(Integer32):
    """Custom type teraMauDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fDX", 1),
          ("hDX", 2))
    )


_TeraMauDuplexMode_Type.__name__ = "Integer32"
_TeraMauDuplexMode_Object = MibTableColumn
teraMauDuplexMode = _TeraMauDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 4513, 18, 1, 2),
    _TeraMauDuplexMode_Type()
)
teraMauDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraMauDuplexMode.setStatus("mandatory")


class _TeraMauSpeed_Type(Integer32):
    """Custom type teraMauSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mbps10", 2),
          ("mbps100", 1))
    )


_TeraMauSpeed_Type.__name__ = "Integer32"
_TeraMauSpeed_Object = MibTableColumn
teraMauSpeed = _TeraMauSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4513, 18, 1, 3),
    _TeraMauSpeed_Type()
)
teraMauSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraMauSpeed.setStatus("mandatory")


class _TeraMauPauseHighThreshold_Type(Integer32):
    """Custom type teraMauPauseHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TeraMauPauseHighThreshold_Type.__name__ = "Integer32"
_TeraMauPauseHighThreshold_Object = MibTableColumn
teraMauPauseHighThreshold = _TeraMauPauseHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4513, 18, 1, 4),
    _TeraMauPauseHighThreshold_Type()
)
teraMauPauseHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraMauPauseHighThreshold.setStatus("mandatory")


class _TeraMauPauseLowThreshold_Type(Integer32):
    """Custom type teraMauPauseLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TeraMauPauseLowThreshold_Type.__name__ = "Integer32"
_TeraMauPauseLowThreshold_Object = MibTableColumn
teraMauPauseLowThreshold = _TeraMauPauseLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4513, 18, 1, 5),
    _TeraMauPauseLowThreshold_Type()
)
teraMauPauseLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraMauPauseLowThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraMau-MIB",
    **{"terawave": terawave,
       "teraMauTable": teraMauTable,
       "teraMauTableEntry": teraMauTableEntry,
       "teraMauLinkState": teraMauLinkState,
       "teraMauDuplexMode": teraMauDuplexMode,
       "teraMauSpeed": teraMauSpeed,
       "teraMauPauseHighThreshold": teraMauPauseHighThreshold,
       "teraMauPauseLowThreshold": teraMauPauseLowThreshold}
)
