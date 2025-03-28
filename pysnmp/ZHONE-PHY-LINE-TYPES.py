# SNMP MIB module (ZHONE-PHY-LINE-TYPES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-PHY-LINE-TYPES
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:38 2024
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(zhoneModules,
 zhonePhysical,
 zhoneShelfIndex,
 zhoneSlotIndex) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhonePhysical",
    "zhoneShelfIndex",
    "zhoneSlotIndex")


# MODULE-IDENTITY

phyZhoneLineTypes = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 1)
)
phyZhoneLineTypes.setRevisions(
        ("2003-05-27 11:55",
         "2003-02-11 11:23")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneLineTypes_ObjectIdentity = ObjectIdentity
zhoneLineTypes = _ZhoneLineTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 11)
)
if mibBuilder.loadTexts:
    zhoneLineTypes.setStatus("current")
_UlcTable_Object = MibTable
ulcTable = _UlcTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 11, 1)
)
if mibBuilder.loadTexts:
    ulcTable.setStatus("current")
_UlcEntry_Object = MibTableRow
ulcEntry = _UlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 11, 1, 1)
)
ulcEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
    (0, "ZHONE-PHY-LINE-TYPES", "ulcPortIndex"),
)
if mibBuilder.loadTexts:
    ulcEntry.setStatus("current")


class _UlcPortIndex_Type(Integer32):
    """Custom type ulcPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_UlcPortIndex_Type.__name__ = "Integer32"
_UlcPortIndex_Object = MibTableColumn
ulcPortIndex = _UlcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 11, 1, 1, 1),
    _UlcPortIndex_Type()
)
ulcPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ulcPortIndex.setStatus("current")


class _UlcPortType_Type(Integer32):
    """Custom type ulcPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ebs", 3),
          ("isdn", 2),
          ("pots", 1))
    )


_UlcPortType_Type.__name__ = "Integer32"
_UlcPortType_Object = MibTableColumn
ulcPortType = _UlcPortType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 11, 1, 1, 2),
    _UlcPortType_Type()
)
ulcPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulcPortType.setStatus("current")


class _UlcTrapEnable_Type(Integer32):
    """Custom type ulcTrapEnable based on Integer32"""
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


_UlcTrapEnable_Type.__name__ = "Integer32"
_UlcTrapEnable_Object = MibTableColumn
ulcTrapEnable = _UlcTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 11, 1, 1, 3),
    _UlcTrapEnable_Type()
)
ulcTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulcTrapEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-PHY-LINE-TYPES",
    **{"zhoneLineTypes": zhoneLineTypes,
       "ulcTable": ulcTable,
       "ulcEntry": ulcEntry,
       "ulcPortIndex": ulcPortIndex,
       "ulcPortType": ulcPortType,
       "ulcTrapEnable": ulcTrapEnable,
       "phyZhoneLineTypes": phyZhoneLineTypes}
)
