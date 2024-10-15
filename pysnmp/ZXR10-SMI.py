# SNMP MIB module (ZXR10-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:50 2024
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

zte = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
zte.setRevisions(
        ("2005-04-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
if mibBuilder.loadTexts:
    zxr10.setStatus("current")
_Zxr10TCP_ObjectIdentity = ObjectIdentity
zxr10TCP = _Zxr10TCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 68)
)
if mibBuilder.loadTexts:
    zxr10TCP.setStatus("current")
_Zxr10protocol_ObjectIdentity = ObjectIdentity
zxr10protocol = _Zxr10protocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 101)
)
if mibBuilder.loadTexts:
    zxr10protocol.setStatus("current")
_Zxr10interfaces_ObjectIdentity = ObjectIdentity
zxr10interfaces = _Zxr10interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103)
)
if mibBuilder.loadTexts:
    zxr10interfaces.setStatus("current")
_Zxr10L2vpn_ObjectIdentity = ObjectIdentity
zxr10L2vpn = _Zxr10L2vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 104)
)
if mibBuilder.loadTexts:
    zxr10L2vpn.setStatus("current")
_Zxr10L3vpn_ObjectIdentity = ObjectIdentity
zxr10L3vpn = _Zxr10L3vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 105)
)
if mibBuilder.loadTexts:
    zxr10L3vpn.setStatus("current")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 302)
)
if mibBuilder.loadTexts:
    alarm.setStatus("current")
_Zxr10MplsTe_ObjectIdentity = ObjectIdentity
zxr10MplsTe = _Zxr10MplsTe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 315)
)
if mibBuilder.loadTexts:
    zxr10MplsTe.setStatus("current")
_Zxr10MplsTeFrr_ObjectIdentity = ObjectIdentity
zxr10MplsTeFrr = _Zxr10MplsTeFrr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 316)
)
if mibBuilder.loadTexts:
    zxr10MplsTeFrr.setStatus("current")
_Zxr10MplsOam_ObjectIdentity = ObjectIdentity
zxr10MplsOam = _Zxr10MplsOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 317)
)
if mibBuilder.loadTexts:
    zxr10MplsOam.setStatus("current")
_MplsTeStaticLsp_ObjectIdentity = ObjectIdentity
mplsTeStaticLsp = _MplsTeStaticLsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 320)
)
if mibBuilder.loadTexts:
    mplsTeStaticLsp.setStatus("current")
_Zxr10RosngMIB_ObjectIdentity = ObjectIdentity
zxr10RosngMIB = _Zxr10RosngMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 6000)
)
if mibBuilder.loadTexts:
    zxr10RosngMIB.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-SMI",
    **{"zte": zte,
       "zxr10": zxr10,
       "zxr10TCP": zxr10TCP,
       "zxr10protocol": zxr10protocol,
       "zxr10interfaces": zxr10interfaces,
       "zxr10L2vpn": zxr10L2vpn,
       "zxr10L3vpn": zxr10L3vpn,
       "alarm": alarm,
       "zxr10MplsTe": zxr10MplsTe,
       "zxr10MplsTeFrr": zxr10MplsTeFrr,
       "zxr10MplsOam": zxr10MplsOam,
       "mplsTeStaticLsp": mplsTeStaticLsp,
       "zxr10RosngMIB": zxr10RosngMIB}
)
