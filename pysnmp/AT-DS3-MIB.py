# SNMP MIB module (AT-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:04 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ds3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109)
)
ds3.setRevisions(
        ("2006-06-28 12:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ds3Traps_ObjectIdentity = ObjectIdentity
ds3Traps = _Ds3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 0)
)
_Ds3TrapTable_Object = MibTable
ds3TrapTable = _Ds3TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1)
)
if mibBuilder.loadTexts:
    ds3TrapTable.setStatus("current")
_Ds3TrapEntry_Object = MibTableRow
ds3TrapEntry = _Ds3TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1, 1)
)
ds3TrapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ds3TrapEntry.setStatus("current")


class _Ds3TcaTrapEnable_Type(Integer32):
    """Custom type ds3TcaTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Ds3TcaTrapEnable_Type.__name__ = "Integer32"
_Ds3TcaTrapEnable_Object = MibTableColumn
ds3TcaTrapEnable = _Ds3TcaTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1, 1, 1),
    _Ds3TcaTrapEnable_Type()
)
ds3TcaTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds3TcaTrapEnable.setStatus("current")


class _Ds3TrapError_Type(Integer32):
    """Custom type ds3TrapError based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ds3CCVs", 9),
          ("ds3CESs", 10),
          ("ds3CSESs", 11),
          ("ds3LCVs", 6),
          ("ds3LESs", 8),
          ("ds3NoError", 1),
          ("ds3PCVs", 7),
          ("ds3PES", 2),
          ("ds3PSES", 3),
          ("ds3SEFs", 4),
          ("ds3UAS", 5))
    )


_Ds3TrapError_Type.__name__ = "Integer32"
_Ds3TrapError_Object = MibTableColumn
ds3TrapError = _Ds3TrapError_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1, 1, 2),
    _Ds3TrapError_Type()
)
ds3TrapError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TrapError.setStatus("current")


class _Ds3TrapLoc_Type(Integer32):
    """Custom type ds3TrapLoc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds3Far", 3),
          ("ds3Near", 2),
          ("ds3NoLoc", 1))
    )


_Ds3TrapLoc_Type.__name__ = "Integer32"
_Ds3TrapLoc_Object = MibTableColumn
ds3TrapLoc = _Ds3TrapLoc_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1, 1, 3),
    _Ds3TrapLoc_Type()
)
ds3TrapLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TrapLoc.setStatus("current")


class _Ds3TrapInterval_Type(Integer32):
    """Custom type ds3TrapInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds3Fifteen", 2),
          ("ds3NoInt", 1),
          ("ds3Twentyfour", 3))
    )


_Ds3TrapInterval_Type.__name__ = "Integer32"
_Ds3TrapInterval_Object = MibTableColumn
ds3TrapInterval = _Ds3TrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 1, 1, 4),
    _Ds3TrapInterval_Type()
)
ds3TrapInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds3TrapInterval.setStatus("current")

# Managed Objects groups


# Notification objects

tcaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 109, 0, 1)
)
tcaTrap.setObjects(
      *(("AT-DS3-MIB", "ds3TrapError"),
        ("AT-DS3-MIB", "ds3TrapLoc"),
        ("AT-DS3-MIB", "ds3TrapInterval"))
)
if mibBuilder.loadTexts:
    tcaTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-DS3-MIB",
    **{"ds3": ds3,
       "ds3Traps": ds3Traps,
       "tcaTrap": tcaTrap,
       "ds3TrapTable": ds3TrapTable,
       "ds3TrapEntry": ds3TrapEntry,
       "ds3TcaTrapEnable": ds3TcaTrapEnable,
       "ds3TrapError": ds3TrapError,
       "ds3TrapLoc": ds3TrapLoc,
       "ds3TrapInterval": ds3TrapInterval}
)
