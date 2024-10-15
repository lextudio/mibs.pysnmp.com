# SNMP MIB module (Juniper-V35-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-V35-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:35 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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

juniV35MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59)
)
juniV35MIB.setRevisions(
        ("2002-09-16 21:44",
         "2002-02-08 16:25")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniV35Objects_ObjectIdentity = ObjectIdentity
juniV35Objects = _JuniV35Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1)
)
_JuniV35IfTable_Object = MibTable
juniV35IfTable = _JuniV35IfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2)
)
if mibBuilder.loadTexts:
    juniV35IfTable.setStatus("current")
_JuniV35IfEntry_Object = MibTableRow
juniV35IfEntry = _JuniV35IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1)
)
juniV35IfEntry.setIndexNames(
    (0, "Juniper-V35-MIB", "juniV35IfIndex"),
)
if mibBuilder.loadTexts:
    juniV35IfEntry.setStatus("current")
_JuniV35IfIndex_Type = InterfaceIndex
_JuniV35IfIndex_Object = MibTableColumn
juniV35IfIndex = _JuniV35IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 1),
    _JuniV35IfIndex_Type()
)
juniV35IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniV35IfIndex.setStatus("current")


class _JuniV35IfType_Type(Integer32):
    """Custom type juniV35IfType based on Integer32"""
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


_JuniV35IfType_Type.__name__ = "Integer32"
_JuniV35IfType_Object = MibTableColumn
juniV35IfType = _JuniV35IfType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 2),
    _JuniV35IfType_Type()
)
juniV35IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniV35IfType.setStatus("current")


class _JuniV35IfMode_Type(Integer32):
    """Custom type juniV35IfMode based on Integer32"""
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


_JuniV35IfMode_Type.__name__ = "Integer32"
_JuniV35IfMode_Object = MibTableColumn
juniV35IfMode = _JuniV35IfMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 3),
    _JuniV35IfMode_Type()
)
juniV35IfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniV35IfMode.setStatus("current")


class _JuniV35IfClockRate_Type(Unsigned32):
    """Custom type juniV35IfClockRate based on Unsigned32"""
    defaultValue = 2048000


_JuniV35IfClockRate_Object = MibTableColumn
juniV35IfClockRate = _JuniV35IfClockRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 4),
    _JuniV35IfClockRate_Type()
)
juniV35IfClockRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniV35IfClockRate.setStatus("current")
if mibBuilder.loadTexts:
    juniV35IfClockRate.setUnits("hertz")


class _JuniV35IfNrzEncoding_Type(Integer32):
    """Custom type juniV35IfNrzEncoding based on Integer32"""
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


_JuniV35IfNrzEncoding_Type.__name__ = "Integer32"
_JuniV35IfNrzEncoding_Object = MibTableColumn
juniV35IfNrzEncoding = _JuniV35IfNrzEncoding_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 5),
    _JuniV35IfNrzEncoding_Type()
)
juniV35IfNrzEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniV35IfNrzEncoding.setStatus("current")


class _JuniV35IfTxClock_Type(Integer32):
    """Custom type juniV35IfTxClock based on Integer32"""
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


_JuniV35IfTxClock_Type.__name__ = "Integer32"
_JuniV35IfTxClock_Object = MibTableColumn
juniV35IfTxClock = _JuniV35IfTxClock_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 6),
    _JuniV35IfTxClock_Type()
)
juniV35IfTxClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniV35IfTxClock.setStatus("current")


class _JuniV35IfIgnoreDcd_Type(Integer32):
    """Custom type juniV35IfIgnoreDcd based on Integer32"""
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


_JuniV35IfIgnoreDcd_Type.__name__ = "Integer32"
_JuniV35IfIgnoreDcd_Object = MibTableColumn
juniV35IfIgnoreDcd = _JuniV35IfIgnoreDcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 7),
    _JuniV35IfIgnoreDcd_Type()
)
juniV35IfIgnoreDcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniV35IfIgnoreDcd.setStatus("current")


class _JuniV35IfLoopback_Type(Integer32):
    """Custom type juniV35IfLoopback based on Integer32"""
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


_JuniV35IfLoopback_Type.__name__ = "Integer32"
_JuniV35IfLoopback_Object = MibTableColumn
juniV35IfLoopback = _JuniV35IfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 1, 2, 1, 8),
    _JuniV35IfLoopback_Type()
)
juniV35IfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniV35IfLoopback.setStatus("current")
_JuniV35Conformance_ObjectIdentity = ObjectIdentity
juniV35Conformance = _JuniV35Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4)
)
_JuniV35Compliances_ObjectIdentity = ObjectIdentity
juniV35Compliances = _JuniV35Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 1)
)
_JuniV35Groups_ObjectIdentity = ObjectIdentity
juniV35Groups = _JuniV35Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 2)
)

# Managed Objects groups

juniV35Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 2, 1)
)
juniV35Group.setObjects(
      *(("Juniper-V35-MIB", "juniV35IfType"),
        ("Juniper-V35-MIB", "juniV35IfMode"),
        ("Juniper-V35-MIB", "juniV35IfClockRate"),
        ("Juniper-V35-MIB", "juniV35IfNrzEncoding"),
        ("Juniper-V35-MIB", "juniV35IfTxClock"),
        ("Juniper-V35-MIB", "juniV35IfIgnoreDcd"),
        ("Juniper-V35-MIB", "juniV35IfLoopback"))
)
if mibBuilder.loadTexts:
    juniV35Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniV35Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniV35Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-V35-MIB",
    **{"juniV35MIB": juniV35MIB,
       "juniV35Objects": juniV35Objects,
       "juniV35IfTable": juniV35IfTable,
       "juniV35IfEntry": juniV35IfEntry,
       "juniV35IfIndex": juniV35IfIndex,
       "juniV35IfType": juniV35IfType,
       "juniV35IfMode": juniV35IfMode,
       "juniV35IfClockRate": juniV35IfClockRate,
       "juniV35IfNrzEncoding": juniV35IfNrzEncoding,
       "juniV35IfTxClock": juniV35IfTxClock,
       "juniV35IfIgnoreDcd": juniV35IfIgnoreDcd,
       "juniV35IfLoopback": juniV35IfLoopback,
       "juniV35Conformance": juniV35Conformance,
       "juniV35Compliances": juniV35Compliances,
       "juniV35Compliance": juniV35Compliance,
       "juniV35Groups": juniV35Groups,
       "juniV35Group": juniV35Group}
)
