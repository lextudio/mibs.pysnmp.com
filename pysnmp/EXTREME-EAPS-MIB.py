# SNMP MIB module (EXTREME-EAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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


# MODULE-IDENTITY

extremeEaps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeEapsTable_Object = MibTable
extremeEapsTable = _ExtremeEapsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1)
)
if mibBuilder.loadTexts:
    extremeEapsTable.setStatus("current")
_ExtremeEapsEntry_Object = MibTableRow
extremeEapsEntry = _ExtremeEapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1)
)
extremeEapsEntry.setIndexNames(
    (0, "EXTREME-EAPS-MIB", "extremeEapsName"),
)
if mibBuilder.loadTexts:
    extremeEapsEntry.setStatus("current")


class _ExtremeEapsName_Type(DisplayString):
    """Custom type extremeEapsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeEapsName_Type.__name__ = "DisplayString"
_ExtremeEapsName_Object = MibTableColumn
extremeEapsName = _ExtremeEapsName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 1),
    _ExtremeEapsName_Type()
)
extremeEapsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsName.setStatus("current")


class _ExtremeEapsMode_Type(Integer32):
    """Custom type extremeEapsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("master", 1),
          ("transit", 2))
    )


_ExtremeEapsMode_Type.__name__ = "Integer32"
_ExtremeEapsMode_Object = MibTableColumn
extremeEapsMode = _ExtremeEapsMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 2),
    _ExtremeEapsMode_Type()
)
extremeEapsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsMode.setStatus("current")


class _ExtremeEapsState_Type(Integer32):
    """Custom type extremeEapsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("failed", 2),
          ("idle", 0),
          ("init", 6),
          ("linkdown", 4),
          ("linksup", 3),
          ("preforwarding", 5))
    )


_ExtremeEapsState_Type.__name__ = "Integer32"
_ExtremeEapsState_Object = MibTableColumn
extremeEapsState = _ExtremeEapsState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 1, 1, 3),
    _ExtremeEapsState_Type()
)
extremeEapsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsState.setStatus("current")


class _ExtremeEapsPrevState_Type(Integer32):
    """Custom type extremeEapsPrevState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("failed", 2),
          ("idle", 0),
          ("init", 6),
          ("linkdown", 4),
          ("linksup", 3),
          ("preforwarding", 5))
    )


_ExtremeEapsPrevState_Type.__name__ = "Integer32"
_ExtremeEapsPrevState_Object = MibScalar
extremeEapsPrevState = _ExtremeEapsPrevState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 18, 2),
    _ExtremeEapsPrevState_Type()
)
extremeEapsPrevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEapsPrevState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-EAPS-MIB",
    **{"extremeEaps": extremeEaps,
       "extremeEapsTable": extremeEapsTable,
       "extremeEapsEntry": extremeEapsEntry,
       "extremeEapsName": extremeEapsName,
       "extremeEapsMode": extremeEapsMode,
       "extremeEapsState": extremeEapsState,
       "extremeEapsPrevState": extremeEapsPrevState}
)
