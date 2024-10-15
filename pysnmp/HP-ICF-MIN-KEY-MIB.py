# SNMP MIB module (HP-ICF-MIN-KEY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-MIN-KEY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:47 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpicfMinKeyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132)
)
hpicfMinKeyMIB.setRevisions(
        ("2016-06-22 09:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfMinKeyObjects_ObjectIdentity = ObjectIdentity
hpicfMinKeyObjects = _HpicfMinKeyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0)
)
_HpicfMinKeyConfigObjects_ObjectIdentity = ObjectIdentity
hpicfMinKeyConfigObjects = _HpicfMinKeyConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1)
)
_HpicfMinKeyTable_Object = MibTable
hpicfMinKeyTable = _HpicfMinKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfMinKeyTable.setStatus("current")
_HpicfMinKeyEntry_Object = MibTableRow
hpicfMinKeyEntry = _HpicfMinKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1)
)
hpicfMinKeyEntry.setIndexNames(
    (0, "HP-ICF-MIN-KEY-MIB", "hpicfMinKeyType"),
)
if mibBuilder.loadTexts:
    hpicfMinKeyEntry.setStatus("current")


class _HpicfMinKeyType_Type(Integer32):
    """Custom type hpicfMinKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rsa", 1)
    )


_HpicfMinKeyType_Type.__name__ = "Integer32"
_HpicfMinKeyType_Object = MibTableColumn
hpicfMinKeyType = _HpicfMinKeyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 1),
    _HpicfMinKeyType_Type()
)
hpicfMinKeyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMinKeyType.setStatus("current")


class _HpicfMinKeySize_Type(Integer32):
    """Custom type hpicfMinKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("minBit1024", 1),
          ("minBit2048", 2))
    )


_HpicfMinKeySize_Type.__name__ = "Integer32"
_HpicfMinKeySize_Object = MibTableColumn
hpicfMinKeySize = _HpicfMinKeySize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 2),
    _HpicfMinKeySize_Type()
)
hpicfMinKeySize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfMinKeySize.setStatus("current")
_HpicfMinKeyRowStatus_Type = RowStatus
_HpicfMinKeyRowStatus_Object = MibTableColumn
hpicfMinKeyRowStatus = _HpicfMinKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 0, 1, 1, 1, 3),
    _HpicfMinKeyRowStatus_Type()
)
hpicfMinKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfMinKeyRowStatus.setStatus("current")
_HpicfMinKeyConformance_ObjectIdentity = ObjectIdentity
hpicfMinKeyConformance = _HpicfMinKeyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1)
)
_HpicfMinKeyCompliances_ObjectIdentity = ObjectIdentity
hpicfMinKeyCompliances = _HpicfMinKeyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 1)
)
_HpicfMinKeyGroups_ObjectIdentity = ObjectIdentity
hpicfMinKeyGroups = _HpicfMinKeyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 2)
)

# Managed Objects groups

hpicfMinKeyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 2, 1)
)
hpicfMinKeyConfigGroup.setObjects(
      *(("HP-ICF-MIN-KEY-MIB", "hpicfMinKeySize"),
        ("HP-ICF-MIN-KEY-MIB", "hpicfMinKeyRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfMinKeyConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfMinKeyCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfMinKeyCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-MIN-KEY-MIB",
    **{"hpicfMinKeyMIB": hpicfMinKeyMIB,
       "hpicfMinKeyObjects": hpicfMinKeyObjects,
       "hpicfMinKeyConfigObjects": hpicfMinKeyConfigObjects,
       "hpicfMinKeyTable": hpicfMinKeyTable,
       "hpicfMinKeyEntry": hpicfMinKeyEntry,
       "hpicfMinKeyType": hpicfMinKeyType,
       "hpicfMinKeySize": hpicfMinKeySize,
       "hpicfMinKeyRowStatus": hpicfMinKeyRowStatus,
       "hpicfMinKeyConformance": hpicfMinKeyConformance,
       "hpicfMinKeyCompliances": hpicfMinKeyCompliances,
       "hpicfMinKeyCompliance1": hpicfMinKeyCompliance1,
       "hpicfMinKeyGroups": hpicfMinKeyGroups,
       "hpicfMinKeyConfigGroup": hpicfMinKeyConfigGroup}
)
