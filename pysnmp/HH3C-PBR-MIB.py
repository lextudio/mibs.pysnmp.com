# SNMP MIB module (HH3C-PBR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-PBR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:26 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cPBR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113)
)
hh3cPBR.setRevisions(
        ("2010-12-10 15:58",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cPBRObjects_ObjectIdentity = ObjectIdentity
hh3cPBRObjects = _Hh3cPBRObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1)
)
_Hh3cPBRGlobal_ObjectIdentity = ObjectIdentity
hh3cPBRGlobal = _Hh3cPBRGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 1)
)


class _Hh3cPBRNexthopTrapEnabled_Type(TruthValue):
    """Custom type hh3cPBRNexthopTrapEnabled based on TruthValue"""


_Hh3cPBRNexthopTrapEnabled_Object = MibScalar
hh3cPBRNexthopTrapEnabled = _Hh3cPBRNexthopTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 1, 1),
    _Hh3cPBRNexthopTrapEnabled_Type()
)
hh3cPBRNexthopTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPBRNexthopTrapEnabled.setStatus("current")
_Hh3cPBRMibTrap_ObjectIdentity = ObjectIdentity
hh3cPBRMibTrap = _Hh3cPBRMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2)
)
_Hh3cPBRTrapObjects_ObjectIdentity = ObjectIdentity
hh3cPBRTrapObjects = _Hh3cPBRTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 1)
)
_Hh3cPBRNexthopAddrType_Type = InetAddressType
_Hh3cPBRNexthopAddrType_Object = MibScalar
hh3cPBRNexthopAddrType = _Hh3cPBRNexthopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 1, 1),
    _Hh3cPBRNexthopAddrType_Type()
)
hh3cPBRNexthopAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPBRNexthopAddrType.setStatus("current")
_Hh3cPBRNexthopAddr_Type = InetAddress
_Hh3cPBRNexthopAddr_Object = MibScalar
hh3cPBRNexthopAddr = _Hh3cPBRNexthopAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 1, 2),
    _Hh3cPBRNexthopAddr_Type()
)
hh3cPBRNexthopAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPBRNexthopAddr.setStatus("current")
_Hh3cPBRTraps_ObjectIdentity = ObjectIdentity
hh3cPBRTraps = _Hh3cPBRTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 2)
)
_Hh3cPBRTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cPBRTrapsPrefix = _Hh3cPBRTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cPBRNexthopFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 113, 1, 2, 2, 0, 1)
)
hh3cPBRNexthopFailedTrap.setObjects(
      *(("HH3C-PBR-MIB", "hh3cPBRNexthopAddrType"),
        ("HH3C-PBR-MIB", "hh3cPBRNexthopAddr"))
)
if mibBuilder.loadTexts:
    hh3cPBRNexthopFailedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PBR-MIB",
    **{"hh3cPBR": hh3cPBR,
       "hh3cPBRObjects": hh3cPBRObjects,
       "hh3cPBRGlobal": hh3cPBRGlobal,
       "hh3cPBRNexthopTrapEnabled": hh3cPBRNexthopTrapEnabled,
       "hh3cPBRMibTrap": hh3cPBRMibTrap,
       "hh3cPBRTrapObjects": hh3cPBRTrapObjects,
       "hh3cPBRNexthopAddrType": hh3cPBRNexthopAddrType,
       "hh3cPBRNexthopAddr": hh3cPBRNexthopAddr,
       "hh3cPBRTraps": hh3cPBRTraps,
       "hh3cPBRTrapsPrefix": hh3cPBRTrapsPrefix,
       "hh3cPBRNexthopFailedTrap": hh3cPBRNexthopFailedTrap}
)
