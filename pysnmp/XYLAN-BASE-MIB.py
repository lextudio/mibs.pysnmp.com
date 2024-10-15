# SNMP MIB module (XYLAN-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:35 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfLanEmulation_ObjectIdentity = ObjectIdentity
atmfLanEmulation = _AtmfLanEmulation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3)
)
_AtmfPnni_ObjectIdentity = ObjectIdentity
atmfPnni = _AtmfPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4)
)
_AtmfMpoa_ObjectIdentity = ObjectIdentity
atmfMpoa = _AtmfMpoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8)
)
_MpoaMIB_ObjectIdentity = ObjectIdentity
mpoaMIB = _MpoaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1)
)
_MpoaMIBObjects_ObjectIdentity = ObjectIdentity
mpoaMIBObjects = _MpoaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1)
)
_Xylan_ObjectIdentity = ObjectIdentity
xylan = _Xylan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800)
)
_XylanMgmt_ObjectIdentity = ObjectIdentity
xylanMgmt = _XylanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 1)
)
_XylanMib_ObjectIdentity = ObjectIdentity
xylanMib = _XylanMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 1, 1)
)
_XylanArch_ObjectIdentity = ObjectIdentity
xylanArch = _XylanArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2)
)
_XylanChassis_ObjectIdentity = ObjectIdentity
xylanChassis = _XylanChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 1)
)
_XylanVlanArch_ObjectIdentity = ObjectIdentity
xylanVlanArch = _XylanVlanArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 2)
)
_XylanVportArch_ObjectIdentity = ObjectIdentity
xylanVportArch = _XylanVportArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3)
)
_XylanAtmArch_ObjectIdentity = ObjectIdentity
xylanAtmArch = _XylanAtmArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 4)
)
_XylanTrapArch_ObjectIdentity = ObjectIdentity
xylanTrapArch = _XylanTrapArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 5)
)
_XylanIpxArch_ObjectIdentity = ObjectIdentity
xylanIpxArch = _XylanIpxArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 6)
)
_XylanWsmArch_ObjectIdentity = ObjectIdentity
xylanWsmArch = _XylanWsmArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 7)
)
_XylanFrArch_ObjectIdentity = ObjectIdentity
xylanFrArch = _XylanFrArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 8)
)
_XylanCsmArch_ObjectIdentity = ObjectIdentity
xylanCsmArch = _XylanCsmArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 9)
)
_XylanVapArch_ObjectIdentity = ObjectIdentity
xylanVapArch = _XylanVapArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 10)
)
_XylanPportArch_ObjectIdentity = ObjectIdentity
xylanPportArch = _XylanPportArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 11)
)
_XylanFwArch_ObjectIdentity = ObjectIdentity
xylanFwArch = _XylanFwArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 12)
)
_XylanIpArch_ObjectIdentity = ObjectIdentity
xylanIpArch = _XylanIpArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 13)
)
_XylanIpmsArch_ObjectIdentity = ObjectIdentity
xylanIpmsArch = _XylanIpmsArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 14)
)
_XylanAVLArch_ObjectIdentity = ObjectIdentity
xylanAVLArch = _XylanAVLArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 15)
)
_XylanBackupArch_ObjectIdentity = ObjectIdentity
xylanBackupArch = _XylanBackupArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 16)
)
_XylanPppArch_ObjectIdentity = ObjectIdentity
xylanPppArch = _XylanPppArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 17)
)
_XylanHealthArch_ObjectIdentity = ObjectIdentity
xylanHealthArch = _XylanHealthArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 18)
)
_XylanTsmArch_ObjectIdentity = ObjectIdentity
xylanTsmArch = _XylanTsmArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 19)
)
_XylanXIPArch_ObjectIdentity = ObjectIdentity
xylanXIPArch = _XylanXIPArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 20)
)
_XylanAscCArch_ObjectIdentity = ObjectIdentity
xylanAscCArch = _XylanAscCArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 21)
)
_XylanFltArch_ObjectIdentity = ObjectIdentity
xylanFltArch = _XylanFltArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 22)
)
_XylanSonetArch_ObjectIdentity = ObjectIdentity
xylanSonetArch = _XylanSonetArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 23)
)
_XylanSrtbArch_ObjectIdentity = ObjectIdentity
xylanSrtbArch = _XylanSrtbArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 24)
)
_XylanM013Arch_ObjectIdentity = ObjectIdentity
xylanM013Arch = _XylanM013Arch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25)
)
_XylanVsmArch_ObjectIdentity = ObjectIdentity
xylanVsmArch = _XylanVsmArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 26)
)
_XylanNtpArch_ObjectIdentity = ObjectIdentity
xylanNtpArch = _XylanNtpArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 27)
)
_XylanOamArch_ObjectIdentity = ObjectIdentity
xylanOamArch = _XylanOamArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 28)
)
_XylanHrexArch_ObjectIdentity = ObjectIdentity
xylanHrexArch = _XylanHrexArch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 31)
)
_XylanProduct_ObjectIdentity = ObjectIdentity
xylanProduct = _XylanProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3)
)
_XylanHardware_ObjectIdentity = ObjectIdentity
xylanHardware = _XylanHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1)
)
_XylanSwitchDevice_ObjectIdentity = ObjectIdentity
xylanSwitchDevice = _XylanSwitchDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1)
)
_Omniswitch5_ObjectIdentity = ObjectIdentity
omniswitch5 = _Omniswitch5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1)
)
_Omniswitch9_ObjectIdentity = ObjectIdentity
omniswitch9 = _Omniswitch9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2)
)
_PizzaSwitch_ObjectIdentity = ObjectIdentity
pizzaSwitch = _PizzaSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3)
)
_MicroSwitch_ObjectIdentity = ObjectIdentity
microSwitch = _MicroSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4)
)
_Omnicell5_ObjectIdentity = ObjectIdentity
omnicell5 = _Omnicell5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 5)
)
_Omnicell9_ObjectIdentity = ObjectIdentity
omnicell9 = _Omnicell9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 6)
)
_PizzaPort_ObjectIdentity = ObjectIdentity
pizzaPort = _PizzaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 7)
)
_OmniStack1024_ObjectIdentity = ObjectIdentity
omniStack1024 = _OmniStack1024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 8)
)
_OmniStack6024_ObjectIdentity = ObjectIdentity
omniStack6024 = _OmniStack6024_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 9)
)
_XylanSoftware_ObjectIdentity = ObjectIdentity
xylanSoftware = _XylanSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2)
)
_XylanPnni_ObjectIdentity = ObjectIdentity
xylanPnni = _XylanPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1)
)
_XylanGated_ObjectIdentity = ObjectIdentity
xylanGated = _XylanGated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 2)
)
_XylanMrouted_ObjectIdentity = ObjectIdentity
xylanMrouted = _XylanMrouted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 3)
)
_XylanNHRP_ObjectIdentity = ObjectIdentity
xylanNHRP = _XylanNHRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 4)
)
_XylanPolicy_ObjectIdentity = ObjectIdentity
xylanPolicy = _XylanPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-BASE-MIB",
    **{"atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfLanEmulation": atmfLanEmulation,
       "atmfPnni": atmfPnni,
       "atmfMpoa": atmfMpoa,
       "mpoaMIB": mpoaMIB,
       "mpoaMIBObjects": mpoaMIBObjects,
       "xylan": xylan,
       "xylanMgmt": xylanMgmt,
       "xylanMib": xylanMib,
       "xylanArch": xylanArch,
       "xylanChassis": xylanChassis,
       "xylanVlanArch": xylanVlanArch,
       "xylanVportArch": xylanVportArch,
       "xylanAtmArch": xylanAtmArch,
       "xylanTrapArch": xylanTrapArch,
       "xylanIpxArch": xylanIpxArch,
       "xylanWsmArch": xylanWsmArch,
       "xylanFrArch": xylanFrArch,
       "xylanCsmArch": xylanCsmArch,
       "xylanVapArch": xylanVapArch,
       "xylanPportArch": xylanPportArch,
       "xylanFwArch": xylanFwArch,
       "xylanIpArch": xylanIpArch,
       "xylanIpmsArch": xylanIpmsArch,
       "xylanAVLArch": xylanAVLArch,
       "xylanBackupArch": xylanBackupArch,
       "xylanPppArch": xylanPppArch,
       "xylanHealthArch": xylanHealthArch,
       "xylanTsmArch": xylanTsmArch,
       "xylanXIPArch": xylanXIPArch,
       "xylanAscCArch": xylanAscCArch,
       "xylanFltArch": xylanFltArch,
       "xylanSonetArch": xylanSonetArch,
       "xylanSrtbArch": xylanSrtbArch,
       "xylanM013Arch": xylanM013Arch,
       "xylanVsmArch": xylanVsmArch,
       "xylanNtpArch": xylanNtpArch,
       "xylanOamArch": xylanOamArch,
       "xylanHrexArch": xylanHrexArch,
       "xylanProduct": xylanProduct,
       "xylanHardware": xylanHardware,
       "xylanSwitchDevice": xylanSwitchDevice,
       "omniswitch5": omniswitch5,
       "omniswitch9": omniswitch9,
       "pizzaSwitch": pizzaSwitch,
       "microSwitch": microSwitch,
       "omnicell5": omnicell5,
       "omnicell9": omnicell9,
       "pizzaPort": pizzaPort,
       "omniStack1024": omniStack1024,
       "omniStack6024": omniStack6024,
       "xylanSoftware": xylanSoftware,
       "xylanPnni": xylanPnni,
       "xylanGated": xylanGated,
       "xylanMrouted": xylanMrouted,
       "xylanNHRP": xylanNHRP,
       "xylanPolicy": xylanPolicy}
)
