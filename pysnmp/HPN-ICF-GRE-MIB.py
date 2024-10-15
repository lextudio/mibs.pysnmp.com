# SNMP MIB module (HPN-ICF-GRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-GRE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:29 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfGre = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54)
)
hpnicfGre.setRevisions(
        ("2005-06-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfGreObjects_ObjectIdentity = ObjectIdentity
hpnicfGreObjects = _HpnicfGreObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1)
)
_HpnicfGreTable_Object = MibTable
hpnicfGreTable = _HpnicfGreTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfGreTable.setStatus("current")
_HpnicfGreEntry_Object = MibTableRow
hpnicfGreEntry = _HpnicfGreEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1, 1, 1)
)
hpnicfGreEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfGreEntry.setStatus("current")
_HpnicfGreKeyValue_Type = Unsigned32
_HpnicfGreKeyValue_Object = MibTableColumn
hpnicfGreKeyValue = _HpnicfGreKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1, 1, 1, 1),
    _HpnicfGreKeyValue_Type()
)
hpnicfGreKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfGreKeyValue.setStatus("current")


class _HpnicfGreKey_Type(Integer32):
    """Custom type hpnicfGreKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpnicfGreKey_Type.__name__ = "Integer32"
_HpnicfGreKey_Object = MibTableColumn
hpnicfGreKey = _HpnicfGreKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1, 1, 1, 2),
    _HpnicfGreKey_Type()
)
hpnicfGreKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfGreKey.setStatus("current")


class _HpnicfGreChecksum_Type(Integer32):
    """Custom type hpnicfGreChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpnicfGreChecksum_Type.__name__ = "Integer32"
_HpnicfGreChecksum_Object = MibTableColumn
hpnicfGreChecksum = _HpnicfGreChecksum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 54, 1, 1, 1, 3),
    _HpnicfGreChecksum_Type()
)
hpnicfGreChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfGreChecksum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-GRE-MIB",
    **{"hpnicfGre": hpnicfGre,
       "hpnicfGreObjects": hpnicfGreObjects,
       "hpnicfGreTable": hpnicfGreTable,
       "hpnicfGreEntry": hpnicfGreEntry,
       "hpnicfGreKeyValue": hpnicfGreKeyValue,
       "hpnicfGreKey": hpnicfGreKey,
       "hpnicfGreChecksum": hpnicfGreChecksum}
)
