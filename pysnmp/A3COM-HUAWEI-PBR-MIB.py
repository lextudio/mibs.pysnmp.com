# SNMP MIB module (A3COM-HUAWEI-PBR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-PBR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:47 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cPBR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113)
)
h3cPBR.setRevisions(
        ("2010-12-10 15:58",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cPBRObjects_ObjectIdentity = ObjectIdentity
h3cPBRObjects = _H3cPBRObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1)
)
_H3cPBRGlobal_ObjectIdentity = ObjectIdentity
h3cPBRGlobal = _H3cPBRGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 1)
)


class _H3cPBRNexthopTrapEnabled_Type(TruthValue):
    """Custom type h3cPBRNexthopTrapEnabled based on TruthValue"""


_H3cPBRNexthopTrapEnabled_Object = MibScalar
h3cPBRNexthopTrapEnabled = _H3cPBRNexthopTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 1, 1),
    _H3cPBRNexthopTrapEnabled_Type()
)
h3cPBRNexthopTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPBRNexthopTrapEnabled.setStatus("current")
_H3cPBRMibTrap_ObjectIdentity = ObjectIdentity
h3cPBRMibTrap = _H3cPBRMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2)
)
_H3cPBRTrapObjects_ObjectIdentity = ObjectIdentity
h3cPBRTrapObjects = _H3cPBRTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 1)
)
_H3cPBRNexthopAddrType_Type = InetAddressType
_H3cPBRNexthopAddrType_Object = MibScalar
h3cPBRNexthopAddrType = _H3cPBRNexthopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 1, 1),
    _H3cPBRNexthopAddrType_Type()
)
h3cPBRNexthopAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPBRNexthopAddrType.setStatus("current")
_H3cPBRNexthopAddr_Type = InetAddress
_H3cPBRNexthopAddr_Object = MibScalar
h3cPBRNexthopAddr = _H3cPBRNexthopAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 1, 2),
    _H3cPBRNexthopAddr_Type()
)
h3cPBRNexthopAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPBRNexthopAddr.setStatus("current")
_H3cPBRTraps_ObjectIdentity = ObjectIdentity
h3cPBRTraps = _H3cPBRTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 2)
)
_H3cPBRTrapsPrefix_ObjectIdentity = ObjectIdentity
h3cPBRTrapsPrefix = _H3cPBRTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cPBRNexthopFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 113, 1, 2, 2, 0, 1)
)
h3cPBRNexthopFailedTrap.setObjects(
      *(("A3COM-HUAWEI-PBR-MIB", "h3cPBRNexthopAddrType"),
        ("A3COM-HUAWEI-PBR-MIB", "h3cPBRNexthopAddr"))
)
if mibBuilder.loadTexts:
    h3cPBRNexthopFailedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-PBR-MIB",
    **{"h3cPBR": h3cPBR,
       "h3cPBRObjects": h3cPBRObjects,
       "h3cPBRGlobal": h3cPBRGlobal,
       "h3cPBRNexthopTrapEnabled": h3cPBRNexthopTrapEnabled,
       "h3cPBRMibTrap": h3cPBRMibTrap,
       "h3cPBRTrapObjects": h3cPBRTrapObjects,
       "h3cPBRNexthopAddrType": h3cPBRNexthopAddrType,
       "h3cPBRNexthopAddr": h3cPBRNexthopAddr,
       "h3cPBRTraps": h3cPBRTraps,
       "h3cPBRTrapsPrefix": h3cPBRTrapsPrefix,
       "h3cPBRNexthopFailedTrap": h3cPBRNexthopFailedTrap}
)
