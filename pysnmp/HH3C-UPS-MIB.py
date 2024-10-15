# SNMP MIB module (HH3C-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-UPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:12 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hh3cUps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 82)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("action", 1),
          ("invalid", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cUpsMibObjects_ObjectIdentity = ObjectIdentity
hh3cUpsMibObjects = _Hh3cUpsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 82, 1)
)
_Hh3cUpsConfigEnable_Type = Hh3cActionType
_Hh3cUpsConfigEnable_Object = MibScalar
hh3cUpsConfigEnable = _Hh3cUpsConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 1),
    _Hh3cUpsConfigEnable_Type()
)
hh3cUpsConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUpsConfigEnable.setStatus("current")
_Hh3cUpsConfigTable_Object = MibTable
hh3cUpsConfigTable = _Hh3cUpsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cUpsConfigTable.setStatus("current")
_Hh3cUpsConfigEntry_Object = MibTableRow
hh3cUpsConfigEntry = _Hh3cUpsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2, 1)
)
hh3cUpsConfigEntry.setIndexNames(
    (0, "HH3C-UPS-MIB", "hh3cUpsIndex"),
)
if mibBuilder.loadTexts:
    hh3cUpsConfigEntry.setStatus("current")
_Hh3cUpsIndex_Type = Integer32
_Hh3cUpsIndex_Object = MibTableColumn
hh3cUpsIndex = _Hh3cUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2, 1, 1),
    _Hh3cUpsIndex_Type()
)
hh3cUpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cUpsIndex.setStatus("current")


class _Hh3cUpsType_Type(Integer32):
    """Custom type hh3cUpsType based on Integer32"""
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
        *(("common", 3),
          ("emersonEth", 4),
          ("emersonUart", 1),
          ("liebert", 5),
          ("mge", 2))
    )


_Hh3cUpsType_Type.__name__ = "Integer32"
_Hh3cUpsType_Object = MibTableColumn
hh3cUpsType = _Hh3cUpsType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2, 1, 2),
    _Hh3cUpsType_Type()
)
hh3cUpsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cUpsType.setStatus("current")
_Hh3cUpsIpAddress_Type = InetAddress
_Hh3cUpsIpAddress_Object = MibTableColumn
hh3cUpsIpAddress = _Hh3cUpsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2, 1, 3),
    _Hh3cUpsIpAddress_Type()
)
hh3cUpsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUpsIpAddress.setStatus("current")
_Hh3cUpsIpAddressType_Type = InetAddressType
_Hh3cUpsIpAddressType_Object = MibTableColumn
hh3cUpsIpAddressType = _Hh3cUpsIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 82, 1, 2, 1, 4),
    _Hh3cUpsIpAddressType_Type()
)
hh3cUpsIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cUpsIpAddressType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-UPS-MIB",
    **{"Hh3cActionType": Hh3cActionType,
       "hh3cUps": hh3cUps,
       "hh3cUpsMibObjects": hh3cUpsMibObjects,
       "hh3cUpsConfigEnable": hh3cUpsConfigEnable,
       "hh3cUpsConfigTable": hh3cUpsConfigTable,
       "hh3cUpsConfigEntry": hh3cUpsConfigEntry,
       "hh3cUpsIndex": hh3cUpsIndex,
       "hh3cUpsType": hh3cUpsType,
       "hh3cUpsIpAddress": hh3cUpsIpAddress,
       "hh3cUpsIpAddressType": hh3cUpsIpAddressType}
)
