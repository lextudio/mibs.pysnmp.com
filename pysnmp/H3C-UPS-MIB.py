# SNMP MIB module (H3C-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-UPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:37 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cUps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 82)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cActionType(Integer32, TextualConvention):
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

_H3cUpsMibObjects_ObjectIdentity = ObjectIdentity
h3cUpsMibObjects = _H3cUpsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1)
)
_H3cUpsConfigEnable_Type = H3cActionType
_H3cUpsConfigEnable_Object = MibScalar
h3cUpsConfigEnable = _H3cUpsConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 1),
    _H3cUpsConfigEnable_Type()
)
h3cUpsConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cUpsConfigEnable.setStatus("current")
_H3cUpsConfigTable_Object = MibTable
h3cUpsConfigTable = _H3cUpsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2)
)
if mibBuilder.loadTexts:
    h3cUpsConfigTable.setStatus("current")
_H3cUpsConfigEntry_Object = MibTableRow
h3cUpsConfigEntry = _H3cUpsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1)
)
h3cUpsConfigEntry.setIndexNames(
    (0, "H3C-UPS-MIB", "h3cUpsIndex"),
)
if mibBuilder.loadTexts:
    h3cUpsConfigEntry.setStatus("current")
_H3cUpsIndex_Type = Integer32
_H3cUpsIndex_Object = MibTableColumn
h3cUpsIndex = _H3cUpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 1),
    _H3cUpsIndex_Type()
)
h3cUpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cUpsIndex.setStatus("current")


class _H3cUpsType_Type(Integer32):
    """Custom type h3cUpsType based on Integer32"""
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


_H3cUpsType_Type.__name__ = "Integer32"
_H3cUpsType_Object = MibTableColumn
h3cUpsType = _H3cUpsType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 2),
    _H3cUpsType_Type()
)
h3cUpsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cUpsType.setStatus("current")
_H3cUpsIpAddress_Type = InetAddress
_H3cUpsIpAddress_Object = MibTableColumn
h3cUpsIpAddress = _H3cUpsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 3),
    _H3cUpsIpAddress_Type()
)
h3cUpsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cUpsIpAddress.setStatus("current")
_H3cUpsIpAddressType_Type = InetAddressType
_H3cUpsIpAddressType_Object = MibTableColumn
h3cUpsIpAddressType = _H3cUpsIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 82, 1, 2, 1, 4),
    _H3cUpsIpAddressType_Type()
)
h3cUpsIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cUpsIpAddressType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-UPS-MIB",
    **{"H3cActionType": H3cActionType,
       "h3cUps": h3cUps,
       "h3cUpsMibObjects": h3cUpsMibObjects,
       "h3cUpsConfigEnable": h3cUpsConfigEnable,
       "h3cUpsConfigTable": h3cUpsConfigTable,
       "h3cUpsConfigEntry": h3cUpsConfigEntry,
       "h3cUpsIndex": h3cUpsIndex,
       "h3cUpsType": h3cUpsType,
       "h3cUpsIpAddress": h3cUpsIpAddress,
       "h3cUpsIpAddressType": h3cUpsIpAddressType}
)
