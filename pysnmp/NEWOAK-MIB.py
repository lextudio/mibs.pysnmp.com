# SNMP MIB module (NEWOAK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NEWOAK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:58 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

contivity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1)
)
contivity.setRevisions(
        ("1900-05-12 20:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Newoak_ObjectIdentity = ObjectIdentity
newoak = _Newoak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505)
)
_VpnRouter2000_ObjectIdentity = ObjectIdentity
vpnRouter2000 = _VpnRouter2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 2)
)
_VpnRouter1000_ObjectIdentity = ObjectIdentity
vpnRouter1000 = _VpnRouter1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 3)
)
_VpnRouter4500_ObjectIdentity = ObjectIdentity
vpnRouter4500 = _VpnRouter4500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 4)
)
_VpnRouter15XX_ObjectIdentity = ObjectIdentity
vpnRouter15XX = _VpnRouter15XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 5)
)
_VpnRouter2500_ObjectIdentity = ObjectIdentity
vpnRouter2500 = _VpnRouter2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 6)
)
_VpnRouter1600_ObjectIdentity = ObjectIdentity
vpnRouter1600 = _VpnRouter1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 7)
)
_VpnRouter2600_ObjectIdentity = ObjectIdentity
vpnRouter2600 = _VpnRouter2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 8)
)
_VpnRouter4600_ObjectIdentity = ObjectIdentity
vpnRouter4600 = _VpnRouter4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 9)
)
_VpnRouter600_ObjectIdentity = ObjectIdentity
vpnRouter600 = _VpnRouter600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 600)
)
_VpnRouter1010_ObjectIdentity = ObjectIdentity
vpnRouter1010 = _VpnRouter1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1010)
)
_VpnRouter1050_ObjectIdentity = ObjectIdentity
vpnRouter1050 = _VpnRouter1050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1050)
)
_VpnRouter1100_ObjectIdentity = ObjectIdentity
vpnRouter1100 = _VpnRouter1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1100)
)
_VpnRouter1700_ObjectIdentity = ObjectIdentity
vpnRouter1700 = _VpnRouter1700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1700)
)
_VpnRouter1740_ObjectIdentity = ObjectIdentity
vpnRouter1740 = _VpnRouter1740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1740)
)
_VpnRouter1750_ObjectIdentity = ObjectIdentity
vpnRouter1750 = _VpnRouter1750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1750)
)
_VpnRouter2700_ObjectIdentity = ObjectIdentity
vpnRouter2700 = _VpnRouter2700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 2700)
)
_VpnRouter2750_ObjectIdentity = ObjectIdentity
vpnRouter2750 = _VpnRouter2750_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 2750)
)
_VpnRouter5000_ObjectIdentity = ObjectIdentity
vpnRouter5000 = _VpnRouter5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 5000)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWOAK-MIB",
    **{"newoak": newoak,
       "contivity": contivity,
       "vpnRouter2000": vpnRouter2000,
       "vpnRouter1000": vpnRouter1000,
       "vpnRouter4500": vpnRouter4500,
       "vpnRouter15XX": vpnRouter15XX,
       "vpnRouter2500": vpnRouter2500,
       "vpnRouter1600": vpnRouter1600,
       "vpnRouter2600": vpnRouter2600,
       "vpnRouter4600": vpnRouter4600,
       "vpnRouter600": vpnRouter600,
       "vpnRouter1010": vpnRouter1010,
       "vpnRouter1050": vpnRouter1050,
       "vpnRouter1100": vpnRouter1100,
       "vpnRouter1700": vpnRouter1700,
       "vpnRouter1740": vpnRouter1740,
       "vpnRouter1750": vpnRouter1750,
       "vpnRouter2700": vpnRouter2700,
       "vpnRouter2750": vpnRouter2750,
       "vpnRouter5000": vpnRouter5000}
)
