# SNMP MIB module (ZYXEL-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:03 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelVlanSetup_ObjectIdentity = ObjectIdentity
zyxelVlanSetup = _ZyxelVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1)
)


class _ZyVlanType_Type(Integer32):
    """Custom type zyVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1Q", 1),
          ("portBased", 2))
    )


_ZyVlanType_Type.__name__ = "Integer32"
_ZyVlanType_Object = MibScalar
zyVlanType = _ZyVlanType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1, 1),
    _ZyVlanType_Type()
)
zyVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanType.setStatus("current")
_ZyVlanIngressCheckState_Type = EnabledStatus
_ZyVlanIngressCheckState_Object = MibScalar
zyVlanIngressCheckState = _ZyVlanIngressCheckState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 86, 1, 2),
    _ZyVlanIngressCheckState_Type()
)
zyVlanIngressCheckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanIngressCheckState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-VLAN-MIB",
    **{"zyxelVlan": zyxelVlan,
       "zyxelVlanSetup": zyxelVlanSetup,
       "zyVlanType": zyVlanType,
       "zyVlanIngressCheckState": zyVlanIngressCheckState}
)
