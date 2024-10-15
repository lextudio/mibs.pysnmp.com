# SNMP MIB module (Netgear-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Netgear-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:09 2024
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



class AgentPortMask(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Netgear_ObjectIdentity = ObjectIdentity
netgear = _Netgear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526)
)
_ManagedSwitch_ObjectIdentity = ObjectIdentity
managedSwitch = _ManagedSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1)
)
_Fsm726s_ObjectIdentity = ObjectIdentity
fsm726s = _Fsm726s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 1)
)
_Fsm750s_ObjectIdentity = ObjectIdentity
fsm750s = _Fsm750s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 2)
)
_Gsm712_ObjectIdentity = ObjectIdentity
gsm712 = _Gsm712_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 3)
)
_Fsm726_ObjectIdentity = ObjectIdentity
fsm726 = _Fsm726_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 4)
)
_Gsm712f_ObjectIdentity = ObjectIdentity
gsm712f = _Gsm712f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 5)
)
_Gsm7312_ObjectIdentity = ObjectIdentity
gsm7312 = _Gsm7312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 6)
)
_Gsm7324_ObjectIdentity = ObjectIdentity
gsm7324 = _Gsm7324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 7)
)
_Gsm7224_ObjectIdentity = ObjectIdentity
gsm7224 = _Gsm7224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 8)
)
_Fsm7326p_ObjectIdentity = ObjectIdentity
fsm7326p = _Fsm7326p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9)
)
_Fsm726v2_ObjectIdentity = ObjectIdentity
fsm726v2 = _Fsm726v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 10)
)
_Carrier_ObjectIdentity = ObjectIdentity
carrier = _Carrier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 3)
)
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4)
)
_Me103_ObjectIdentity = ObjectIdentity
me103 = _Me103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 1)
)
_Wg302_ObjectIdentity = ObjectIdentity
wg302 = _Wg302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 2)
)
_Wg102_ObjectIdentity = ObjectIdentity
wg102 = _Wg102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3)
)
_Wag302_ObjectIdentity = ObjectIdentity
wag302 = _Wag302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 4)
)
_Wag102_ObjectIdentity = ObjectIdentity
wag102 = _Wag102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 5)
)
_Rps_ObjectIdentity = ObjectIdentity
rps = _Rps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 5)
)
_Wlanswitch_ObjectIdentity = ObjectIdentity
wlanswitch = _Wlanswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 6)
)
_Wls538_ObjectIdentity = ObjectIdentity
wls538 = _Wls538_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 6, 1)
)
_Ng7000managedswitch_ObjectIdentity = ObjectIdentity
ng7000managedswitch = _Ng7000managedswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10)
)
_Ng700smartswitch_ObjectIdentity = ObjectIdentity
ng700smartswitch = _Ng700smartswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11)
)
_Ngrouter_ObjectIdentity = ObjectIdentity
ngrouter = _Ngrouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 12)
)
_Ngfirewall_ObjectIdentity = ObjectIdentity
ngfirewall = _Ngfirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 13)
)
_Ngap_ObjectIdentity = ObjectIdentity
ngap = _Ngap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 14)
)
_Ngwlan_ObjectIdentity = ObjectIdentity
ngwlan = _Ngwlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 15)
)
_Ng9000chassisswitch_ObjectIdentity = ObjectIdentity
ng9000chassisswitch = _Ng9000chassisswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 16)
)
_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100)
)
_Stackswitch_ObjectIdentity = ObjectIdentity
stackswitch = _Stackswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1)
)
_Fsm7328s_ObjectIdentity = ObjectIdentity
fsm7328s = _Fsm7328s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 1)
)
_Fsm7352s_ObjectIdentity = ObjectIdentity
fsm7352s = _Fsm7352s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 2)
)
_Gsm7328s_ObjectIdentity = ObjectIdentity
gsm7328s = _Gsm7328s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 3)
)
_Gsm7352s_ObjectIdentity = ObjectIdentity
gsm7352s = _Gsm7352s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 4)
)
_Fsm7352sp_ObjectIdentity = ObjectIdentity
fsm7352sp = _Fsm7352sp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 5)
)
_Fsm7328sp_ObjectIdentity = ObjectIdentity
fsm7328sp = _Fsm7328sp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 1, 6)
)
_L2switch_ObjectIdentity = ObjectIdentity
l2switch = _L2switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 2)
)
_Gsm7248_ObjectIdentity = ObjectIdentity
gsm7248 = _Gsm7248_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 2, 1)
)
_Gsm7212_ObjectIdentity = ObjectIdentity
gsm7212 = _Gsm7212_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 2, 2)
)
_L3switch_ObjectIdentity = ObjectIdentity
l3switch = _L3switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3)
)
_Gsm7312v2_ObjectIdentity = ObjectIdentity
gsm7312v2 = _Gsm7312v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 1)
)
_Gsm7324v2_ObjectIdentity = ObjectIdentity
gsm7324v2 = _Gsm7324v2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 2)
)
_Xsm7312_ObjectIdentity = ObjectIdentity
xsm7312 = _Xsm7312_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 3)
)
_Gsm7324p_ObjectIdentity = ObjectIdentity
gsm7324p = _Gsm7324p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 3, 4)
)
_Smartswitch_ObjectIdentity = ObjectIdentity
smartswitch = _Smartswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4)
)
_Gs748t_ObjectIdentity = ObjectIdentity
gs748t = _Gs748t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 1)
)
_Fs726t_ObjectIdentity = ObjectIdentity
fs726t = _Fs726t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 2)
)
_Gs716t_ObjectIdentity = ObjectIdentity
gs716t = _Gs716t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 3)
)
_Fs750t_ObjectIdentity = ObjectIdentity
fs750t = _Fs750t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 4)
)
_Gs724t_ObjectIdentity = ObjectIdentity
gs724t = _Gs724t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 5)
)
_Fs726tp_ObjectIdentity = ObjectIdentity
fs726tp = _Fs726tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 4, 6)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 5)
)
_Fvx538_ObjectIdentity = ObjectIdentity
fvx538 = _Fvx538_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 5, 1)
)
_Fvs338_ObjectIdentity = ObjectIdentity
fvs338 = _Fvs338_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 5, 2)
)
_Fvg318_ObjectIdentity = ObjectIdentity
fvg318 = _Fvg318_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 5, 3)
)
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 6)
)
_Fwag114_ObjectIdentity = ObjectIdentity
fwag114 = _Fwag114_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 6, 3)
)
_Accesspoint_ObjectIdentity = ObjectIdentity
accesspoint = _Accesspoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 7)
)
_WirelessLAN_ObjectIdentity = ObjectIdentity
wirelessLAN = _WirelessLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 8)
)
_Chassisswitch_ObjectIdentity = ObjectIdentity
chassisswitch = _Chassisswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 9)
)
_Gcm9000_ObjectIdentity = ObjectIdentity
gcm9000 = _Gcm9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 100, 9, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Netgear-MIB",
    **{"AgentPortMask": AgentPortMask,
       "netgear": netgear,
       "managedSwitch": managedSwitch,
       "fsm726s": fsm726s,
       "fsm750s": fsm750s,
       "gsm712": gsm712,
       "fsm726": fsm726,
       "gsm712f": gsm712f,
       "gsm7312": gsm7312,
       "gsm7324": gsm7324,
       "gsm7224": gsm7224,
       "fsm7326p": fsm7326p,
       "fsm726v2": fsm726v2,
       "carrier": carrier,
       "wireless": wireless,
       "me103": me103,
       "wg302": wg302,
       "wg102": wg102,
       "wag302": wag302,
       "wag102": wag102,
       "rps": rps,
       "wlanswitch": wlanswitch,
       "wls538": wls538,
       "ng7000managedswitch": ng7000managedswitch,
       "ng700smartswitch": ng700smartswitch,
       "ngrouter": ngrouter,
       "ngfirewall": ngfirewall,
       "ngap": ngap,
       "ngwlan": ngwlan,
       "ng9000chassisswitch": ng9000chassisswitch,
       "productID": productID,
       "stackswitch": stackswitch,
       "fsm7328s": fsm7328s,
       "fsm7352s": fsm7352s,
       "gsm7328s": gsm7328s,
       "gsm7352s": gsm7352s,
       "fsm7352sp": fsm7352sp,
       "fsm7328sp": fsm7328sp,
       "l2switch": l2switch,
       "gsm7248": gsm7248,
       "gsm7212": gsm7212,
       "l3switch": l3switch,
       "gsm7312v2": gsm7312v2,
       "gsm7324v2": gsm7324v2,
       "xsm7312": xsm7312,
       "gsm7324p": gsm7324p,
       "smartswitch": smartswitch,
       "gs748t": gs748t,
       "fs726t": fs726t,
       "gs716t": gs716t,
       "fs750t": fs750t,
       "gs724t": gs724t,
       "fs726tp": fs726tp,
       "router": router,
       "fvx538": fvx538,
       "fvs338": fvs338,
       "fvg318": fvg318,
       "firewall": firewall,
       "fwag114": fwag114,
       "accesspoint": accesspoint,
       "wirelessLAN": wirelessLAN,
       "chassisswitch": chassisswitch,
       "gcm9000": gcm9000}
)
