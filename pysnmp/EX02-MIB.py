# SNMP MIB module (EX02-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EX02-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:01 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ex01Module = ModuleIdentity(
    (1, 3, 6, 1, 3, 1194)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ex01Test_ObjectIdentity = ObjectIdentity
ex01Test = _Ex01Test_ObjectIdentity(
    (1, 3, 6, 1, 3, 1195)
)
_ATable_Object = MibTable
aTable = _ATable_Object(
    (1, 3, 6, 1, 3, 1195, 1)
)
if mibBuilder.loadTexts:
    aTable.setStatus("current")
_AEntry_Object = MibTableRow
aEntry = _AEntry_Object(
    (1, 3, 6, 1, 3, 1195, 1, 1)
)
aEntry.setIndexNames(
    (0, "EX02-MIB", "aIndex"),
)
if mibBuilder.loadTexts:
    aEntry.setStatus("current")


class _AIndex_Type(Integer32):
    """Custom type aIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blue", 3),
          ("green", 2),
          ("red", 1))
    )


_AIndex_Type.__name__ = "Integer32"
_AIndex_Object = MibTableColumn
aIndex = _AIndex_Object(
    (1, 3, 6, 1, 3, 1195, 1, 1, 1),
    _AIndex_Type()
)
aIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aIndex.setStatus("current")


class _AOct1_Type(OctetString):
    """Custom type aOct1 based on OctetString"""
    defaultValue = OctetString("a default value")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AOct1_Type.__name__ = "OctetString"
_AOct1_Object = MibTableColumn
aOct1 = _AOct1_Object(
    (1, 3, 6, 1, 3, 1195, 1, 1, 2),
    _AOct1_Type()
)
aOct1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aOct1.setStatus("current")


class _AOct2_Type(OctetString):
    """Custom type aOct2 based on OctetString"""
    defaultHexValue = "0a23bc"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AOct2_Type.__name__ = "OctetString"
_AOct2_Object = MibTableColumn
aOct2 = _AOct2_Object(
    (1, 3, 6, 1, 3, 1195, 1, 1, 3),
    _AOct2_Type()
)
aOct2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aOct2.setStatus("current")


class _AInt1_Type(Integer32):
    """Custom type aInt1 based on Integer32"""
    defaultBinValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AInt1_Type.__name__ = "Integer32"
_AInt1_Object = MibTableColumn
aInt1 = _AInt1_Object(
    (1, 3, 6, 1, 3, 1195, 1, 1, 4),
    _AInt1_Type()
)
aInt1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aInt1.setStatus("current")

# Managed Objects groups

oG = ObjectGroup(
    (1, 3, 6, 1, 3, 1194, 1)
)
oG.setObjects(
      *(("EX02-MIB", "aOct1"),
        ("EX02-MIB", "aOct2"),
        ("EX02-MIB", "aInt1"))
)
if mibBuilder.loadTexts:
    oG.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EX02-MIB",
    **{"ex01Module": ex01Module,
       "oG": oG,
       "ex01Test": ex01Test,
       "aTable": aTable,
       "aEntry": aEntry,
       "aIndex": aIndex,
       "aOct1": aOct1,
       "aOct2": aOct2,
       "aInt1": aInt1}
)
