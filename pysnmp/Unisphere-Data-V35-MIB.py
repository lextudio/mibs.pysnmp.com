# SNMP MIB module (Unisphere-Data-V35-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-V35-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:47 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdV35MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59)
)
usdV35MIB.setRevisions(
        ("2002-02-08 16:25",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdV35Objects_ObjectIdentity = ObjectIdentity
usdV35Objects = _UsdV35Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1)
)
_UsdV35IfTable_Object = MibTable
usdV35IfTable = _UsdV35IfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2)
)
if mibBuilder.loadTexts:
    usdV35IfTable.setStatus("current")
_UsdV35IfEntry_Object = MibTableRow
usdV35IfEntry = _UsdV35IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1)
)
usdV35IfEntry.setIndexNames(
    (0, "Unisphere-Data-V35-MIB", "usdV35IfIndex"),
)
if mibBuilder.loadTexts:
    usdV35IfEntry.setStatus("current")
_UsdV35IfIndex_Type = InterfaceIndex
_UsdV35IfIndex_Object = MibTableColumn
usdV35IfIndex = _UsdV35IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 1),
    _UsdV35IfIndex_Type()
)
usdV35IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdV35IfIndex.setStatus("current")


class _UsdV35IfType_Type(Integer32):
    """Custom type usdV35IfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interfaceTypeNoCable", 2),
          ("v35", 1),
          ("x21", 0))
    )


_UsdV35IfType_Type.__name__ = "Integer32"
_UsdV35IfType_Object = MibTableColumn
usdV35IfType = _UsdV35IfType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 2),
    _UsdV35IfType_Type()
)
usdV35IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdV35IfType.setStatus("current")


class _UsdV35IfMode_Type(Integer32):
    """Custom type usdV35IfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 0),
          ("interfaceModeNoCable", 2))
    )


_UsdV35IfMode_Type.__name__ = "Integer32"
_UsdV35IfMode_Object = MibTableColumn
usdV35IfMode = _UsdV35IfMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 3),
    _UsdV35IfMode_Type()
)
usdV35IfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdV35IfMode.setStatus("current")


class _UsdV35IfClockRate_Type(Unsigned32):
    """Custom type usdV35IfClockRate based on Unsigned32"""
    defaultValue = 2048000


_UsdV35IfClockRate_Object = MibTableColumn
usdV35IfClockRate = _UsdV35IfClockRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 4),
    _UsdV35IfClockRate_Type()
)
usdV35IfClockRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdV35IfClockRate.setStatus("current")
if mibBuilder.loadTexts:
    usdV35IfClockRate.setUnits("hertz")


class _UsdV35IfNrzEncoding_Type(Integer32):
    """Custom type usdV35IfNrzEncoding based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 1),
          ("normal", 0))
    )


_UsdV35IfNrzEncoding_Type.__name__ = "Integer32"
_UsdV35IfNrzEncoding_Object = MibTableColumn
usdV35IfNrzEncoding = _UsdV35IfNrzEncoding_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 5),
    _UsdV35IfNrzEncoding_Type()
)
usdV35IfNrzEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdV35IfNrzEncoding.setStatus("current")


class _UsdV35IfTxClock_Type(Integer32):
    """Custom type usdV35IfTxClock based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 1),
          ("normal", 0))
    )


_UsdV35IfTxClock_Type.__name__ = "Integer32"
_UsdV35IfTxClock_Object = MibTableColumn
usdV35IfTxClock = _UsdV35IfTxClock_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 6),
    _UsdV35IfTxClock_Type()
)
usdV35IfTxClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdV35IfTxClock.setStatus("current")


class _UsdV35IfIgnoreDcd_Type(Integer32):
    """Custom type usdV35IfIgnoreDcd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcdIgnored", 1),
          ("ignoredNone", 0),
          ("linkStateIgnored", 2))
    )


_UsdV35IfIgnoreDcd_Type.__name__ = "Integer32"
_UsdV35IfIgnoreDcd_Object = MibTableColumn
usdV35IfIgnoreDcd = _UsdV35IfIgnoreDcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 7),
    _UsdV35IfIgnoreDcd_Type()
)
usdV35IfIgnoreDcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdV35IfIgnoreDcd.setStatus("current")


class _UsdV35IfLoopback_Type(Integer32):
    """Custom type usdV35IfLoopback based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 1),
          ("none", 0))
    )


_UsdV35IfLoopback_Type.__name__ = "Integer32"
_UsdV35IfLoopback_Object = MibTableColumn
usdV35IfLoopback = _UsdV35IfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 8),
    _UsdV35IfLoopback_Type()
)
usdV35IfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdV35IfLoopback.setStatus("current")
_UsdV35Conformance_ObjectIdentity = ObjectIdentity
usdV35Conformance = _UsdV35Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4)
)
_UsdV35Compliances_ObjectIdentity = ObjectIdentity
usdV35Compliances = _UsdV35Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 1)
)
_UsdV35Groups_ObjectIdentity = ObjectIdentity
usdV35Groups = _UsdV35Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 2)
)

# Managed Objects groups

usdV35Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 2, 1)
)
usdV35Group.setObjects(
      *(("Unisphere-Data-V35-MIB", "usdV35IfType"),
        ("Unisphere-Data-V35-MIB", "usdV35IfMode"),
        ("Unisphere-Data-V35-MIB", "usdV35IfClockRate"),
        ("Unisphere-Data-V35-MIB", "usdV35IfNrzEncoding"),
        ("Unisphere-Data-V35-MIB", "usdV35IfTxClock"),
        ("Unisphere-Data-V35-MIB", "usdV35IfIgnoreDcd"),
        ("Unisphere-Data-V35-MIB", "usdV35IfLoopback"))
)
if mibBuilder.loadTexts:
    usdV35Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdV35Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdV35Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-V35-MIB",
    **{"usdV35MIB": usdV35MIB,
       "usdV35Objects": usdV35Objects,
       "usdV35IfTable": usdV35IfTable,
       "usdV35IfEntry": usdV35IfEntry,
       "usdV35IfIndex": usdV35IfIndex,
       "usdV35IfType": usdV35IfType,
       "usdV35IfMode": usdV35IfMode,
       "usdV35IfClockRate": usdV35IfClockRate,
       "usdV35IfNrzEncoding": usdV35IfNrzEncoding,
       "usdV35IfTxClock": usdV35IfTxClock,
       "usdV35IfIgnoreDcd": usdV35IfIgnoreDcd,
       "usdV35IfLoopback": usdV35IfLoopback,
       "usdV35Conformance": usdV35Conformance,
       "usdV35Compliances": usdV35Compliances,
       "usdV35Compliance": usdV35Compliance,
       "usdV35Groups": usdV35Groups,
       "usdV35Group": usdV35Group}
)
