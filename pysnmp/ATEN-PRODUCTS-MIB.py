# SNMP MIB module (ATEN-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATEN-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:41 2024
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

(atenProducts,) = mibBuilder.importSymbols(
    "ATEN-SMI",
    "atenProducts")

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

_Public_ObjectIdentity = ObjectIdentity
public = _Public_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 1)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 2)
)
_Overip_ObjectIdentity = ObjectIdentity
overip = _Overip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3)
)
_Kvmoverip_ObjectIdentity = ObjectIdentity
kvmoverip = _Kvmoverip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 1)
)
_Poweroverip_ObjectIdentity = ObjectIdentity
poweroverip = _Poweroverip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2)
)
_Pn9108_ObjectIdentity = ObjectIdentity
pn9108 = _Pn9108_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 1)
)
_Serialoverip_ObjectIdentity = ObjectIdentity
serialoverip = _Serialoverip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 3)
)
_Sn0116a_ObjectIdentity = ObjectIdentity
sn0116a = _Sn0116a_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 1)
)
_Sn3101_ObjectIdentity = ObjectIdentity
sn3101 = _Sn3101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2)
)
_Kvm_ObjectIdentity = ObjectIdentity
kvm = _Kvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 4)
)
_Video_ObjectIdentity = ObjectIdentity
video = _Video_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 5)
)
_Usb_ObjectIdentity = ObjectIdentity
usb = _Usb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 6)
)
_Firewire_ObjectIdentity = ObjectIdentity
firewire = _Firewire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21317, 1, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATEN-PRODUCTS-MIB",
    **{"public": public,
       "software": software,
       "overip": overip,
       "kvmoverip": kvmoverip,
       "poweroverip": poweroverip,
       "pn9108": pn9108,
       "serialoverip": serialoverip,
       "sn0116a": sn0116a,
       "sn3101": sn3101,
       "kvm": kvm,
       "video": video,
       "usb": usb,
       "firewire": firewire}
)
