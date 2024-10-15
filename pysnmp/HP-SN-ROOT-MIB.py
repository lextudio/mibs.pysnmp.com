# SNMP MIB module (HP-SN-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:40 2024
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
_HpSwitch_ObjectIdentity = ObjectIdentity
hpSwitch = _HpSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1)
)
_SnChassis_ObjectIdentity = ObjectIdentity
snChassis = _SnChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1)
)
_SnAgentSys_ObjectIdentity = ObjectIdentity
snAgentSys = _SnAgentSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2)
)
_SnSwitch_ObjectIdentity = ObjectIdentity
snSwitch = _SnSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 3)
)
_SnL4_ObjectIdentity = ObjectIdentity
snL4 = _SnL4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 4)
)
_SnStack_ObjectIdentity = ObjectIdentity
snStack = _SnStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2)
)
_SnIpx_ObjectIdentity = ObjectIdentity
snIpx = _SnIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 1)
)
_SnIp_ObjectIdentity = ObjectIdentity
snIp = _SnIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 2)
)
_SnRip_ObjectIdentity = ObjectIdentity
snRip = _SnRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 3)
)
_SnOspf_ObjectIdentity = ObjectIdentity
snOspf = _SnOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 4)
)
_SnDvmrp_ObjectIdentity = ObjectIdentity
snDvmrp = _SnDvmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 5)
)
_SnIgmp_ObjectIdentity = ObjectIdentity
snIgmp = _SnIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 6)
)
_SnFsrp_ObjectIdentity = ObjectIdentity
snFsrp = _SnFsrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 7)
)
_SnGblRt_ObjectIdentity = ObjectIdentity
snGblRt = _SnGblRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 8)
)
_SnPim_ObjectIdentity = ObjectIdentity
snPim = _SnPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 9)
)
_SnAppleTalk_ObjectIdentity = ObjectIdentity
snAppleTalk = _SnAppleTalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 10)
)
_SnBgp4_ObjectIdentity = ObjectIdentity
snBgp4 = _SnBgp4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11)
)
_SnVrrp_ObjectIdentity = ObjectIdentity
snVrrp = _SnVrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 12)
)
_SnLoopbackIf_ObjectIdentity = ObjectIdentity
snLoopbackIf = _SnLoopbackIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 13)
)
_SnPOS_ObjectIdentity = ObjectIdentity
snPOS = _SnPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14)
)
_HpSwitch9308_ObjectIdentity = ObjectIdentity
hpSwitch9308 = _HpSwitch9308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 13)
)
_HpSwitch9304_ObjectIdentity = ObjectIdentity
hpSwitch9304 = _HpSwitch9304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 14)
)
_HpSwitch6308_ObjectIdentity = ObjectIdentity
hpSwitch6308 = _HpSwitch6308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 15)
)
_HpSwitch6208_ObjectIdentity = ObjectIdentity
hpSwitch6208 = _HpSwitch6208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 16)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-ROOT-MIB",
    **{"hp": hp,
       "nm": nm,
       "system": system,
       "netElement": netElement,
       "hpEtherSwitch": hpEtherSwitch,
       "hpSwitch": hpSwitch,
       "switch": switch,
       "snChassis": snChassis,
       "snAgentSys": snAgentSys,
       "snSwitch": snSwitch,
       "snL4": snL4,
       "snStack": snStack,
       "router": router,
       "snIpx": snIpx,
       "snIp": snIp,
       "snRip": snRip,
       "snOspf": snOspf,
       "snDvmrp": snDvmrp,
       "snIgmp": snIgmp,
       "snFsrp": snFsrp,
       "snGblRt": snGblRt,
       "snPim": snPim,
       "snAppleTalk": snAppleTalk,
       "snBgp4": snBgp4,
       "snVrrp": snVrrp,
       "snLoopbackIf": snLoopbackIf,
       "snPOS": snPOS,
       "hpSwitch9308": hpSwitch9308,
       "hpSwitch9304": hpSwitch9304,
       "hpSwitch6308": hpSwitch6308,
       "hpSwitch6208": hpSwitch6208}
)
