# SNMP MIB module (BIANCA-BRICK-POTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-POTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:38 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Pots_ObjectIdentity = ObjectIdentity
pots = _Pots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 14)
)
_PotsIfTable_Object = MibTable
potsIfTable = _PotsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 14, 1)
)
if mibBuilder.loadTexts:
    potsIfTable.setStatus("mandatory")
_PotsIfEntry_Object = MibTableRow
potsIfEntry = _PotsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 14, 1, 1)
)
potsIfEntry.setIndexNames(
    (0, "BIANCA-BRICK-POTS-MIB", "potsSlot"),
    (0, "BIANCA-BRICK-POTS-MIB", "potsUnit"),
)
if mibBuilder.loadTexts:
    potsIfEntry.setStatus("mandatory")


class _PotsSlot_Type(Integer32):
    """Custom type potsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PotsSlot_Type.__name__ = "Integer32"
_PotsSlot_Object = MibTableColumn
potsSlot = _PotsSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 14, 1, 1, 1),
    _PotsSlot_Type()
)
potsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsSlot.setStatus("mandatory")


class _PotsUnit_Type(Integer32):
    """Custom type potsUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PotsUnit_Type.__name__ = "Integer32"
_PotsUnit_Object = MibTableColumn
potsUnit = _PotsUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 14, 1, 1, 2),
    _PotsUnit_Type()
)
potsUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsUnit.setStatus("mandatory")


class _PotsType_Type(Integer32):
    """Custom type potsType based on Integer32"""
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
        *(("any", 1),
          ("disable", 5),
          ("fax", 2),
          ("modem", 4),
          ("telephony", 3))
    )


_PotsType_Type.__name__ = "Integer32"
_PotsType_Object = MibTableColumn
potsType = _PotsType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 14, 1, 1, 3),
    _PotsType_Type()
)
potsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potsType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-POTS-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "pots": pots,
       "potsIfTable": potsIfTable,
       "potsIfEntry": potsIfEntry,
       "potsSlot": potsSlot,
       "potsUnit": potsUnit,
       "potsType": potsType}
)
