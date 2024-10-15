# SNMP MIB module (APPACCELERATION-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPACCELERATION-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:26 2024
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

(appAccelerationModules,
 appAccelerationProducts) = mibBuilder.importSymbols(
    "APPACCELERATION-SMI",
    "appAccelerationModules",
    "appAccelerationProducts")

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

appAccelerationProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Orbital5500_ObjectIdentity = ObjectIdentity
orbital5500 = _Orbital5500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 1)
)
_OrbitalLC_ObjectIdentity = ObjectIdentity
orbitalLC = _OrbitalLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 2)
)
_Repeater6500_ObjectIdentity = ObjectIdentity
Repeater6500 = _Repeater6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 3)
)
_Repeater6800_ObjectIdentity = ObjectIdentity
Repeater6800 = _Repeater6800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 4)
)
_Repeater8800_ObjectIdentity = ObjectIdentity
Repeater8800 = _Repeater8800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 5)
)
_Repeater8500_ObjectIdentity = ObjectIdentity
Repeater8500 = _Repeater8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 6)
)
_Dp104a_ObjectIdentity = ObjectIdentity
dp104a = _Dp104a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 7)
)
_Repeater8810_ObjectIdentity = ObjectIdentity
Repeater8810 = _Repeater8810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 8)
)
_Repeater8510_ObjectIdentity = ObjectIdentity
Repeater8510 = _Repeater8510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 9)
)
_Repeater6510_ObjectIdentity = ObjectIdentity
Repeater6510 = _Repeater6510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 10)
)
_Repeater6810_ObjectIdentity = ObjectIdentity
Repeater6810 = _Repeater6810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 11)
)
_CloudBridge_ObjectIdentity = ObjectIdentity
CloudBridge = _CloudBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 12)
)
_CloudBridge700_ObjectIdentity = ObjectIdentity
CloudBridge700 = _CloudBridge700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 13)
)
_CloudBridgeVPX_ObjectIdentity = ObjectIdentity
CloudBridgeVPX = _CloudBridgeVPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 14)
)
_CloudBridgeSDX_ObjectIdentity = ObjectIdentity
CloudBridgeSDX = _CloudBridgeSDX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 15)
)
_CloudBridge2000_ObjectIdentity = ObjectIdentity
CloudBridge2000 = _CloudBridge2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 16)
)
_CloudBridge3000_ObjectIdentity = ObjectIdentity
CloudBridge3000 = _CloudBridge3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 1, 2, 17)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPACCELERATION-PRODUCTS-MIB",
    **{"appAccelerationProductsMIB": appAccelerationProductsMIB,
       "orbital5500": orbital5500,
       "orbitalLC": orbitalLC,
       "Repeater6500": Repeater6500,
       "Repeater6800": Repeater6800,
       "Repeater8800": Repeater8800,
       "Repeater8500": Repeater8500,
       "dp104a": dp104a,
       "Repeater8810": Repeater8810,
       "Repeater8510": Repeater8510,
       "Repeater6510": Repeater6510,
       "Repeater6810": Repeater6810,
       "CloudBridge": CloudBridge,
       "CloudBridge700": CloudBridge700,
       "CloudBridgeVPX": CloudBridgeVPX,
       "CloudBridgeSDX": CloudBridgeSDX,
       "CloudBridge2000": CloudBridge2000,
       "CloudBridge3000": CloudBridge3000}
)
