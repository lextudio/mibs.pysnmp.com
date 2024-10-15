# SNMP MIB module (Unisphere-Data-MIBs) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-MIBs
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:14 2024
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

(usMibs,) = mibBuilder.importSymbols(
    "Unisphere-SMI",
    "usMibs")


# MODULE-IDENTITY

usDataMibs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2)
)
usDataMibs.setRevisions(
        ("2002-06-04 14:37",
         "2002-05-31 14:33",
         "2001-11-30 14:12",
         "2000-12-27 15:50",
         "2000-11-22 00:00",
         "2000-09-19 15:40",
         "1999-12-15 15:44",
         "1999-11-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdTextualConventions_ObjectIdentity = ObjectIdentity
usdTextualConventions = _UsdTextualConventions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 1)
)
_UsdSystemMIB_ObjectIdentity = ObjectIdentity
usdSystemMIB = _UsdSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 2)
)
_UsdIfMIB_ObjectIdentity = ObjectIdentity
usdIfMIB = _UsdIfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3)
)
_UsdDs3MIB_ObjectIdentity = ObjectIdentity
usdDs3MIB = _UsdDs3MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 4)
)
_UsdDs1MIB_ObjectIdentity = ObjectIdentity
usdDs1MIB = _UsdDs1MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 5)
)
_UsdFt1MIB_ObjectIdentity = ObjectIdentity
usdFt1MIB = _UsdFt1MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 6)
)
_UsdSonetMIB_ObjectIdentity = ObjectIdentity
usdSonetMIB = _UsdSonetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 7)
)
_UsdAtmMIB_ObjectIdentity = ObjectIdentity
usdAtmMIB = _UsdAtmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8)
)
_UsdHdlcMIB_ObjectIdentity = ObjectIdentity
usdHdlcMIB = _UsdHdlcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 9)
)
_UsdFrameRelayMIB_ObjectIdentity = ObjectIdentity
usdFrameRelayMIB = _UsdFrameRelayMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10)
)
_UsdPppMIB_ObjectIdentity = ObjectIdentity
usdPppMIB = _UsdPppMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11)
)
_UsdIpMIB_ObjectIdentity = ObjectIdentity
usdIpMIB = _UsdIpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 12)
)
_UsdIpPolicyMIB_ObjectIdentity = ObjectIdentity
usdIpPolicyMIB = _UsdIpPolicyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 13)
)
_UsdOspfMIB_ObjectIdentity = ObjectIdentity
usdOspfMIB = _UsdOspfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14)
)
_UsdSlepMIBS_ObjectIdentity = ObjectIdentity
usdSlepMIBS = _UsdSlepMIBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15)
)
_UsdSnmpMIB_ObjectIdentity = ObjectIdentity
usdSnmpMIB = _UsdSnmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16)
)
_UsdERXSysMIB_ObjectIdentity = ObjectIdentity
usdERXSysMIB = _UsdERXSysMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17)
)
_UsdPPPoEMIB_ObjectIdentity = ObjectIdentity
usdPPPoEMIB = _UsdPPPoEMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18)
)
_UsdRadiusClientMIB_ObjectIdentity = ObjectIdentity
usdRadiusClientMIB = _UsdRadiusClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19)
)
_UsdAaaMIB_ObjectIdentity = ObjectIdentity
usdAaaMIB = _UsdAaaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20)
)
_UsdAddressPoolMIB_ObjectIdentity = ObjectIdentity
usdAddressPoolMIB = _UsdAddressPoolMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 21)
)
_UsdDhcpMIB_ObjectIdentity = ObjectIdentity
usdDhcpMIB = _UsdDhcpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22)
)
_UsdFileXferMIB_ObjectIdentity = ObjectIdentity
usdFileXferMIB = _UsdFileXferMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 23)
)
_UsdAcctngMIB_ObjectIdentity = ObjectIdentity
usdAcctngMIB = _UsdAcctngMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 24)
)
_UsdProfileMIB_ObjectIdentity = ObjectIdentity
usdProfileMIB = _UsdProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25)
)
_UsdIpProfileMIB_ObjectIdentity = ObjectIdentity
usdIpProfileMIB = _UsdIpProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 26)
)
_UsdPolicyMIB_ObjectIdentity = ObjectIdentity
usdPolicyMIB = _UsdPolicyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27)
)
_UsdLogMIB_ObjectIdentity = ObjectIdentity
usdLogMIB = _UsdLogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 28)
)
_UsdBgpMIB_ObjectIdentity = ObjectIdentity
usdBgpMIB = _UsdBgpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29)
)
_UsdCliMIB_ObjectIdentity = ObjectIdentity
usdCliMIB = _UsdCliMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 30)
)
_UsdBridgeEthernetMIB_ObjectIdentity = ObjectIdentity
usdBridgeEthernetMIB = _UsdBridgeEthernetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31)
)
_UsdRouterMIB_ObjectIdentity = ObjectIdentity
usdRouterMIB = _UsdRouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32)
)
_UsdHostMIB_ObjectIdentity = ObjectIdentity
usdHostMIB = _UsdHostMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 33)
)
_UsdEthernetMIB_ObjectIdentity = ObjectIdentity
usdEthernetMIB = _UsdEthernetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 34)
)
_UsdL2tpMIB_ObjectIdentity = ObjectIdentity
usdL2tpMIB = _UsdL2tpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35)
)
_UsdSscClientMIB_ObjectIdentity = ObjectIdentity
usdSscClientMIB = _UsdSscClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 36)
)
_UsdCopsProtocolMIB_ObjectIdentity = ObjectIdentity
usdCopsProtocolMIB = _UsdCopsProtocolMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 37)
)
_UsdIsisMIB_ObjectIdentity = ObjectIdentity
usdIsisMIB = _UsdIsisMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 38)
)
_UsdPingMIB_ObjectIdentity = ObjectIdentity
usdPingMIB = _UsdPingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 39)
)
_UsdIgmpMIB_ObjectIdentity = ObjectIdentity
usdIgmpMIB = _UsdIgmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 40)
)
_UsdTraceRouteMIB_ObjectIdentity = ObjectIdentity
usdTraceRouteMIB = _UsdTraceRouteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 41)
)
_UsdLookupMIB_ObjectIdentity = ObjectIdentity
usdLookupMIB = _UsdLookupMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 42)
)
_UsdPimMIB_ObjectIdentity = ObjectIdentity
usdPimMIB = _UsdPimMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43)
)
_UsdDvmrpMIB_ObjectIdentity = ObjectIdentity
usdDvmrpMIB = _UsdDvmrpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 44)
)
_UsdPppProfileMIB_ObjectIdentity = ObjectIdentity
usdPppProfileMIB = _UsdPppProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 45)
)
_UsdPppoeProfileMIB_ObjectIdentity = ObjectIdentity
usdPppoeProfileMIB = _UsdPppoeProfileMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 46)
)
_UsdDnsMIB_ObjectIdentity = ObjectIdentity
usdDnsMIB = _UsdDnsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47)
)
_UsdAutoConfMIB_ObjectIdentity = ObjectIdentity
usdAutoConfMIB = _UsdAutoConfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48)
)
_UsdSubscriberMIB_ObjectIdentity = ObjectIdentity
usdSubscriberMIB = _UsdSubscriberMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49)
)
_UsdSmdsMIB_ObjectIdentity = ObjectIdentity
usdSmdsMIB = _UsdSmdsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 50)
)
_UsdIpTunnelMIB_ObjectIdentity = ObjectIdentity
usdIpTunnelMIB = _UsdIpTunnelMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51)
)
_UsdCbfMIB_ObjectIdentity = ObjectIdentity
usdCbfMIB = _UsdCbfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 52)
)
_UsdL2fMIB_ObjectIdentity = ObjectIdentity
usdL2fMIB = _UsdL2fMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53)
)
_UsdMplsMIB_ObjectIdentity = ObjectIdentity
usdMplsMIB = _UsdMplsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 54)
)
_UsdMrxSystemMIB_ObjectIdentity = ObjectIdentity
usdMrxSystemMIB = _UsdMrxSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 55)
)
_UsdSysClockMIB_ObjectIdentity = ObjectIdentity
usdSysClockMIB = _UsdSysClockMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 56)
)
_UsdQosMIB_ObjectIdentity = ObjectIdentity
usdQosMIB = _UsdQosMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 57)
)
_UsdV35MIB_ObjectIdentity = ObjectIdentity
usdV35MIB = _UsdV35MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 59)
)
_UsdL2tpDialoutMIB_ObjectIdentity = ObjectIdentity
usdL2tpDialoutMIB = _UsdL2tpDialoutMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 62)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-MIBs",
    **{"usDataMibs": usDataMibs,
       "usdTextualConventions": usdTextualConventions,
       "usdSystemMIB": usdSystemMIB,
       "usdIfMIB": usdIfMIB,
       "usdDs3MIB": usdDs3MIB,
       "usdDs1MIB": usdDs1MIB,
       "usdFt1MIB": usdFt1MIB,
       "usdSonetMIB": usdSonetMIB,
       "usdAtmMIB": usdAtmMIB,
       "usdHdlcMIB": usdHdlcMIB,
       "usdFrameRelayMIB": usdFrameRelayMIB,
       "usdPppMIB": usdPppMIB,
       "usdIpMIB": usdIpMIB,
       "usdIpPolicyMIB": usdIpPolicyMIB,
       "usdOspfMIB": usdOspfMIB,
       "usdSlepMIBS": usdSlepMIBS,
       "usdSnmpMIB": usdSnmpMIB,
       "usdERXSysMIB": usdERXSysMIB,
       "usdPPPoEMIB": usdPPPoEMIB,
       "usdRadiusClientMIB": usdRadiusClientMIB,
       "usdAaaMIB": usdAaaMIB,
       "usdAddressPoolMIB": usdAddressPoolMIB,
       "usdDhcpMIB": usdDhcpMIB,
       "usdFileXferMIB": usdFileXferMIB,
       "usdAcctngMIB": usdAcctngMIB,
       "usdProfileMIB": usdProfileMIB,
       "usdIpProfileMIB": usdIpProfileMIB,
       "usdPolicyMIB": usdPolicyMIB,
       "usdLogMIB": usdLogMIB,
       "usdBgpMIB": usdBgpMIB,
       "usdCliMIB": usdCliMIB,
       "usdBridgeEthernetMIB": usdBridgeEthernetMIB,
       "usdRouterMIB": usdRouterMIB,
       "usdHostMIB": usdHostMIB,
       "usdEthernetMIB": usdEthernetMIB,
       "usdL2tpMIB": usdL2tpMIB,
       "usdSscClientMIB": usdSscClientMIB,
       "usdCopsProtocolMIB": usdCopsProtocolMIB,
       "usdIsisMIB": usdIsisMIB,
       "usdPingMIB": usdPingMIB,
       "usdIgmpMIB": usdIgmpMIB,
       "usdTraceRouteMIB": usdTraceRouteMIB,
       "usdLookupMIB": usdLookupMIB,
       "usdPimMIB": usdPimMIB,
       "usdDvmrpMIB": usdDvmrpMIB,
       "usdPppProfileMIB": usdPppProfileMIB,
       "usdPppoeProfileMIB": usdPppoeProfileMIB,
       "usdDnsMIB": usdDnsMIB,
       "usdAutoConfMIB": usdAutoConfMIB,
       "usdSubscriberMIB": usdSubscriberMIB,
       "usdSmdsMIB": usdSmdsMIB,
       "usdIpTunnelMIB": usdIpTunnelMIB,
       "usdCbfMIB": usdCbfMIB,
       "usdL2fMIB": usdL2fMIB,
       "usdMplsMIB": usdMplsMIB,
       "usdMrxSystemMIB": usdMrxSystemMIB,
       "usdSysClockMIB": usdSysClockMIB,
       "usdQosMIB": usdQosMIB,
       "usdV35MIB": usdV35MIB,
       "usdL2tpDialoutMIB": usdL2tpDialoutMIB}
)
