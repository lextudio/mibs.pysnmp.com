# SNMP MIB module (HP-SWITCH-PL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SWITCH-PL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:01 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetElement_ObjectIdentity = ObjectIdentity
netElement = _NetElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7)
)
_HpEtherSwitch_ObjectIdentity = ObjectIdentity
hpEtherSwitch = _HpEtherSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11)
)
_HpSwitchProliant_ObjectIdentity = ObjectIdentity
hpSwitchProliant = _HpSwitchProliant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33)
)
_HpSwitchModuleBladetype2_ObjectIdentity = ObjectIdentity
hpSwitchModuleBladetype2 = _HpSwitchModuleBladetype2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1)
)
_HpSwitchBladeType2_Products_ObjectIdentity = ObjectIdentity
hpSwitchBladeType2_Products = _HpSwitchBladeType2_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 1)
)
_HpSwitchBladeType2_Mgmt_ObjectIdentity = ObjectIdentity
hpSwitchBladeType2_Mgmt = _HpSwitchBladeType2_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2)
)
_HpSwitchModuleBladetype4_ObjectIdentity = ObjectIdentity
hpSwitchModuleBladetype4 = _HpSwitchModuleBladetype4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 4)
)
_HpSwitchBladeType4_Products_ObjectIdentity = ObjectIdentity
hpSwitchBladeType4_Products = _HpSwitchBladeType4_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 4, 1)
)
_HpSwitchBladeType4_Mgmt_ObjectIdentity = ObjectIdentity
hpSwitchBladeType4_Mgmt = _HpSwitchBladeType4_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 4, 2)
)
_HpSwitchModuleBladetype5_ObjectIdentity = ObjectIdentity
hpSwitchModuleBladetype5 = _HpSwitchModuleBladetype5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 5)
)
_HpSwitchBladeType5_Products_ObjectIdentity = ObjectIdentity
hpSwitchBladeType5_Products = _HpSwitchBladeType5_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 5, 1)
)
_HpSwitchBladeType5_Mgmt_ObjectIdentity = ObjectIdentity
hpSwitchBladeType5_Mgmt = _HpSwitchBladeType5_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 5, 2)
)
_HpSwitchModuleBladetype6_ObjectIdentity = ObjectIdentity
hpSwitchModuleBladetype6 = _HpSwitchModuleBladetype6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 6)
)
_HpSwitchBladeType6_Products_ObjectIdentity = ObjectIdentity
hpSwitchBladeType6_Products = _HpSwitchBladeType6_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 6, 1)
)
_HpSwitchBladeType6_Mgmt_ObjectIdentity = ObjectIdentity
hpSwitchBladeType6_Mgmt = _HpSwitchBladeType6_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 6, 2)
)
_HpSwitchModuleBladetype7_ObjectIdentity = ObjectIdentity
hpSwitchModuleBladetype7 = _HpSwitchModuleBladetype7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 7)
)
_HpSwitchBladeType7_Products_ObjectIdentity = ObjectIdentity
hpSwitchBladeType7_Products = _HpSwitchBladeType7_Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 7, 1)
)
_HpSwitchBladeType7_Mgmt_ObjectIdentity = ObjectIdentity
hpSwitchBladeType7_Mgmt = _HpSwitchBladeType7_Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 7, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SWITCH-PL-MIB",
    **{"hp": hp,
       "nm": nm,
       "system": system,
       "netElement": netElement,
       "hpEtherSwitch": hpEtherSwitch,
       "hpSwitchProliant": hpSwitchProliant,
       "hpSwitchModuleBladetype2": hpSwitchModuleBladetype2,
       "hpSwitchBladeType2-Products": hpSwitchBladeType2_Products,
       "hpSwitchBladeType2-Mgmt": hpSwitchBladeType2_Mgmt,
       "hpSwitchModuleBladetype4": hpSwitchModuleBladetype4,
       "hpSwitchBladeType4-Products": hpSwitchBladeType4_Products,
       "hpSwitchBladeType4-Mgmt": hpSwitchBladeType4_Mgmt,
       "hpSwitchModuleBladetype5": hpSwitchModuleBladetype5,
       "hpSwitchBladeType5-Products": hpSwitchBladeType5_Products,
       "hpSwitchBladeType5-Mgmt": hpSwitchBladeType5_Mgmt,
       "hpSwitchModuleBladetype6": hpSwitchModuleBladetype6,
       "hpSwitchBladeType6-Products": hpSwitchBladeType6_Products,
       "hpSwitchBladeType6-Mgmt": hpSwitchBladeType6_Mgmt,
       "hpSwitchModuleBladetype7": hpSwitchModuleBladetype7,
       "hpSwitchBladeType7-Products": hpSwitchBladeType7_Products,
       "hpSwitchBladeType7-Mgmt": hpSwitchBladeType7_Mgmt}
)
