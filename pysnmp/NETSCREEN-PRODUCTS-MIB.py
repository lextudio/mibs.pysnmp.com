# SNMP MIB module (NETSCREEN-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:50 2024
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

(netscreenProducts,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenProducts")

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

netscreenProductsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 0)
)
netscreenProductsMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2004-01-20 00:00",
         "2000-08-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetscreenGeneric_ObjectIdentity = ObjectIdentity
netscreenGeneric = _NetscreenGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 1)
)
_NetscreenNs5_ObjectIdentity = ObjectIdentity
netscreenNs5 = _NetscreenNs5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 2)
)
_NetscreenNs10_ObjectIdentity = ObjectIdentity
netscreenNs10 = _NetscreenNs10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 3)
)
_NetscreenNs100_ObjectIdentity = ObjectIdentity
netscreenNs100 = _NetscreenNs100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 4)
)
_NetscreenNs1000_ObjectIdentity = ObjectIdentity
netscreenNs1000 = _NetscreenNs1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 5)
)
_NetscreenNs500_ObjectIdentity = ObjectIdentity
netscreenNs500 = _NetscreenNs500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 6)
)
_NetscreenNs50_ObjectIdentity = ObjectIdentity
netscreenNs50 = _NetscreenNs50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 7)
)
_NetscreenNs25_ObjectIdentity = ObjectIdentity
netscreenNs25 = _NetscreenNs25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 8)
)
_NetscreenNs204_ObjectIdentity = ObjectIdentity
netscreenNs204 = _NetscreenNs204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 9)
)
_NetscreenNs208_ObjectIdentity = ObjectIdentity
netscreenNs208 = _NetscreenNs208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 10)
)
_NetscreenNs5XT_ObjectIdentity = ObjectIdentity
netscreenNs5XT = _NetscreenNs5XT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 11)
)
_NetscreenNs5XP_ObjectIdentity = ObjectIdentity
netscreenNs5XP = _NetscreenNs5XP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 12)
)
_NetscreenNs5000_ObjectIdentity = ObjectIdentity
netscreenNs5000 = _NetscreenNs5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 13)
)
_NetscreenNs5GT_ObjectIdentity = ObjectIdentity
netscreenNs5GT = _NetscreenNs5GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 14)
)
_NetscreenHardwareSecurityClient_ObjectIdentity = ObjectIdentity
netscreenHardwareSecurityClient = _NetscreenHardwareSecurityClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 15)
)
_NetscreenISG2000_ObjectIdentity = ObjectIdentity
netscreenISG2000 = _NetscreenISG2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 16)
)
_Netscreen_5GT_ADSL_AnnexA_ObjectIdentity = ObjectIdentity
netscreen_5GT_ADSL_AnnexA = _Netscreen_5GT_ADSL_AnnexA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 17)
)
_Netscreen_5GT_ADSL_AnnexB_ObjectIdentity = ObjectIdentity
netscreen_5GT_ADSL_AnnexB = _Netscreen_5GT_ADSL_AnnexB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 19)
)
_Netscreen_5GT_WLAN_ObjectIdentity = ObjectIdentity
netscreen_5GT_WLAN = _Netscreen_5GT_WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 21)
)
_Netscreen_5GT_ADSL_AnnexA_WLAN_ObjectIdentity = ObjectIdentity
netscreen_5GT_ADSL_AnnexA_WLAN = _Netscreen_5GT_ADSL_AnnexA_WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 23)
)
_Netscreen_5GT_ADSL_AnnexB_WLAN_ObjectIdentity = ObjectIdentity
netscreen_5GT_ADSL_AnnexB_WLAN = _Netscreen_5GT_ADSL_AnnexB_WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 25)
)
_NetscreenISG1000_ObjectIdentity = ObjectIdentity
netscreenISG1000 = _NetscreenISG1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 28)
)
_NetscreenSSG5_ObjectIdentity = ObjectIdentity
netscreenSSG5 = _NetscreenSSG5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 29)
)
_NetscreenSSG5_ISDN_ObjectIdentity = ObjectIdentity
netscreenSSG5_ISDN = _NetscreenSSG5_ISDN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 30)
)
_NetscreenSSG5_v92_ObjectIdentity = ObjectIdentity
netscreenSSG5_v92 = _NetscreenSSG5_v92_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 31)
)
_NetscreenSSG5_Serial_WLAN_ObjectIdentity = ObjectIdentity
netscreenSSG5_Serial_WLAN = _NetscreenSSG5_Serial_WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 32)
)
_NetscreenSSG5_ISDN_WLAN_ObjectIdentity = ObjectIdentity
netscreenSSG5_ISDN_WLAN = _NetscreenSSG5_ISDN_WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 33)
)
_NetscreenSSG5_v92_WLAN_ObjectIdentity = ObjectIdentity
netscreenSSG5_v92_WLAN = _NetscreenSSG5_v92_WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 34)
)
_NetscreenSSG20_ObjectIdentity = ObjectIdentity
netscreenSSG20 = _NetscreenSSG20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 35)
)
_NetscreenSSG20_WLAN_ObjectIdentity = ObjectIdentity
netscreenSSG20_WLAN = _NetscreenSSG20_WLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 36)
)
_NetscreenSSG520_ObjectIdentity = ObjectIdentity
netscreenSSG520 = _NetscreenSSG520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 50)
)
_NetscreenSSG550_ObjectIdentity = ObjectIdentity
netscreenSSG550 = _NetscreenSSG550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 51)
)
_NetscreenSSG140_ObjectIdentity = ObjectIdentity
netscreenSSG140 = _NetscreenSSG140_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 52)
)
_NetscreenSSG320_ObjectIdentity = ObjectIdentity
netscreenSSG320 = _NetscreenSSG320_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 54)
)
_NetscreenSSG350_ObjectIdentity = ObjectIdentity
netscreenSSG350 = _NetscreenSSG350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1, 55)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-PRODUCTS-MIB",
    **{"netscreenProductsMibModule": netscreenProductsMibModule,
       "netscreenGeneric": netscreenGeneric,
       "netscreenNs5": netscreenNs5,
       "netscreenNs10": netscreenNs10,
       "netscreenNs100": netscreenNs100,
       "netscreenNs1000": netscreenNs1000,
       "netscreenNs500": netscreenNs500,
       "netscreenNs50": netscreenNs50,
       "netscreenNs25": netscreenNs25,
       "netscreenNs204": netscreenNs204,
       "netscreenNs208": netscreenNs208,
       "netscreenNs5XT": netscreenNs5XT,
       "netscreenNs5XP": netscreenNs5XP,
       "netscreenNs5000": netscreenNs5000,
       "netscreenNs5GT": netscreenNs5GT,
       "netscreenHardwareSecurityClient": netscreenHardwareSecurityClient,
       "netscreenISG2000": netscreenISG2000,
       "netscreen-5GT-ADSL-AnnexA": netscreen_5GT_ADSL_AnnexA,
       "netscreen-5GT-ADSL-AnnexB": netscreen_5GT_ADSL_AnnexB,
       "netscreen-5GT-WLAN": netscreen_5GT_WLAN,
       "netscreen-5GT-ADSL-AnnexA-WLAN": netscreen_5GT_ADSL_AnnexA_WLAN,
       "netscreen-5GT-ADSL-AnnexB-WLAN": netscreen_5GT_ADSL_AnnexB_WLAN,
       "netscreenISG1000": netscreenISG1000,
       "netscreenSSG5": netscreenSSG5,
       "netscreenSSG5-ISDN": netscreenSSG5_ISDN,
       "netscreenSSG5-v92": netscreenSSG5_v92,
       "netscreenSSG5-Serial-WLAN": netscreenSSG5_Serial_WLAN,
       "netscreenSSG5-ISDN-WLAN": netscreenSSG5_ISDN_WLAN,
       "netscreenSSG5-v92-WLAN": netscreenSSG5_v92_WLAN,
       "netscreenSSG20": netscreenSSG20,
       "netscreenSSG20-WLAN": netscreenSSG20_WLAN,
       "netscreenSSG520": netscreenSSG520,
       "netscreenSSG550": netscreenSSG550,
       "netscreenSSG140": netscreenSSG140,
       "netscreenSSG320": netscreenSSG320,
       "netscreenSSG350": netscreenSSG350}
)
