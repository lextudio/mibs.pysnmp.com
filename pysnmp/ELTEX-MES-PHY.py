# SNMP MIB module (ELTEX-MES-PHY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-PHY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:55 2024
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

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

eltMesPhy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90)
)
eltMesPhy.setRevisions(
        ("2014-01-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesPhyTest_ObjectIdentity = ObjectIdentity
eltMesPhyTest = _EltMesPhyTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1)
)
_EltPhyTdrTestTable_Object = MibTable
eltPhyTdrTestTable = _EltPhyTdrTestTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1)
)
if mibBuilder.loadTexts:
    eltPhyTdrTestTable.setStatus("current")
_EltPhyTdrTestEntry_Object = MibTableRow
eltPhyTdrTestEntry = _EltPhyTdrTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1, 1)
)
eltPhyTdrTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltPhyTdrTestEntry.setStatus("current")
_EltPhyTdrTestResultIsValid_Type = TruthValue
_EltPhyTdrTestResultIsValid_Object = MibTableColumn
eltPhyTdrTestResultIsValid = _EltPhyTdrTestResultIsValid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1, 1, 1),
    _EltPhyTdrTestResultIsValid_Type()
)
eltPhyTdrTestResultIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhyTdrTestResultIsValid.setStatus("current")


class _EltPhyTdrTestPair1Status_Type(Integer32):
    """Custom type eltPhyTdrTestPair1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("impedance-mismatch", 4),
          ("ok", 1),
          ("open", 2),
          ("short", 3),
          ("short-with-pair-1", 5),
          ("short-with-pair-2", 6),
          ("short-with-pair-3", 7),
          ("short-with-pair-4", 8),
          ("test-failed", 0))
    )


_EltPhyTdrTestPair1Status_Type.__name__ = "Integer32"
_EltPhyTdrTestPair1Status_Object = MibTableColumn
eltPhyTdrTestPair1Status = _EltPhyTdrTestPair1Status_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1, 1, 2),
    _EltPhyTdrTestPair1Status_Type()
)
eltPhyTdrTestPair1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhyTdrTestPair1Status.setStatus("current")


class _EltPhyTdrTestPair2Status_Type(Integer32):
    """Custom type eltPhyTdrTestPair2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("impedance-mismatch", 4),
          ("ok", 1),
          ("open", 2),
          ("short", 3),
          ("short-with-pair-1", 5),
          ("short-with-pair-2", 6),
          ("short-with-pair-3", 7),
          ("short-with-pair-4", 8),
          ("test-failed", 0))
    )


_EltPhyTdrTestPair2Status_Type.__name__ = "Integer32"
_EltPhyTdrTestPair2Status_Object = MibTableColumn
eltPhyTdrTestPair2Status = _EltPhyTdrTestPair2Status_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1, 1, 3),
    _EltPhyTdrTestPair2Status_Type()
)
eltPhyTdrTestPair2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhyTdrTestPair2Status.setStatus("current")


class _EltPhyTdrTestPair3Status_Type(Integer32):
    """Custom type eltPhyTdrTestPair3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("impedance-mismatch", 4),
          ("ok", 1),
          ("open", 2),
          ("short", 3),
          ("short-with-pair-1", 5),
          ("short-with-pair-2", 6),
          ("short-with-pair-3", 7),
          ("short-with-pair-4", 8),
          ("test-failed", 0))
    )


_EltPhyTdrTestPair3Status_Type.__name__ = "Integer32"
_EltPhyTdrTestPair3Status_Object = MibTableColumn
eltPhyTdrTestPair3Status = _EltPhyTdrTestPair3Status_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1, 1, 4),
    _EltPhyTdrTestPair3Status_Type()
)
eltPhyTdrTestPair3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhyTdrTestPair3Status.setStatus("current")


class _EltPhyTdrTestPair4Status_Type(Integer32):
    """Custom type eltPhyTdrTestPair4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("impedance-mismatch", 4),
          ("ok", 1),
          ("open", 2),
          ("short", 3),
          ("short-with-pair-1", 5),
          ("short-with-pair-2", 6),
          ("short-with-pair-3", 7),
          ("short-with-pair-4", 8),
          ("test-failed", 0))
    )


_EltPhyTdrTestPair4Status_Type.__name__ = "Integer32"
_EltPhyTdrTestPair4Status_Object = MibTableColumn
eltPhyTdrTestPair4Status = _EltPhyTdrTestPair4Status_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1, 1, 5),
    _EltPhyTdrTestPair4Status_Type()
)
eltPhyTdrTestPair4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhyTdrTestPair4Status.setStatus("current")
_EltPhyTdrTestPair1Length_Type = Integer32
_EltPhyTdrTestPair1Length_Object = MibTableColumn
eltPhyTdrTestPair1Length = _EltPhyTdrTestPair1Length_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1, 1, 6),
    _EltPhyTdrTestPair1Length_Type()
)
eltPhyTdrTestPair1Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhyTdrTestPair1Length.setStatus("current")
_EltPhyTdrTestPair2Length_Type = Integer32
_EltPhyTdrTestPair2Length_Object = MibTableColumn
eltPhyTdrTestPair2Length = _EltPhyTdrTestPair2Length_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1, 1, 7),
    _EltPhyTdrTestPair2Length_Type()
)
eltPhyTdrTestPair2Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhyTdrTestPair2Length.setStatus("current")
_EltPhyTdrTestPair3Length_Type = Integer32
_EltPhyTdrTestPair3Length_Object = MibTableColumn
eltPhyTdrTestPair3Length = _EltPhyTdrTestPair3Length_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1, 1, 8),
    _EltPhyTdrTestPair3Length_Type()
)
eltPhyTdrTestPair3Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhyTdrTestPair3Length.setStatus("current")
_EltPhyTdrTestPair4Length_Type = Integer32
_EltPhyTdrTestPair4Length_Object = MibTableColumn
eltPhyTdrTestPair4Length = _EltPhyTdrTestPair4Length_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 90, 1, 1, 1, 9),
    _EltPhyTdrTestPair4Length_Type()
)
eltPhyTdrTestPair4Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPhyTdrTestPair4Length.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-PHY",
    **{"eltMesPhy": eltMesPhy,
       "eltMesPhyTest": eltMesPhyTest,
       "eltPhyTdrTestTable": eltPhyTdrTestTable,
       "eltPhyTdrTestEntry": eltPhyTdrTestEntry,
       "eltPhyTdrTestResultIsValid": eltPhyTdrTestResultIsValid,
       "eltPhyTdrTestPair1Status": eltPhyTdrTestPair1Status,
       "eltPhyTdrTestPair2Status": eltPhyTdrTestPair2Status,
       "eltPhyTdrTestPair3Status": eltPhyTdrTestPair3Status,
       "eltPhyTdrTestPair4Status": eltPhyTdrTestPair4Status,
       "eltPhyTdrTestPair1Length": eltPhyTdrTestPair1Length,
       "eltPhyTdrTestPair2Length": eltPhyTdrTestPair2Length,
       "eltPhyTdrTestPair3Length": eltPhyTdrTestPair3Length,
       "eltPhyTdrTestPair4Length": eltPhyTdrTestPair4Length}
)
