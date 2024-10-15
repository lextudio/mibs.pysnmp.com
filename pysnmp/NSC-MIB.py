# SNMP MIB module (NSC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:25 2024
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

_Nsc_ObjectIdentity = ObjectIdentity
nsc = _Nsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10)
)
_NscExperimental_ObjectIdentity = ObjectIdentity
nscExperimental = _NscExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 1)
)
_NscMib_ObjectIdentity = ObjectIdentity
nscMib = _NscMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2)
)
_NscProducts_ObjectIdentity = ObjectIdentity
nscProducts = _NscProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1)
)
_NscDevices_ObjectIdentity = ObjectIdentity
nscDevices = _NscDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 1)
)
_NscObj_ObjectIdentity = ObjectIdentity
nscObj = _NscObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 1, 1)
)
_NscDevicesInstalled_ObjectIdentity = ObjectIdentity
nscDevicesInstalled = _NscDevicesInstalled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 1, 2)
)
_Nsc6600_ObjectIdentity = ObjectIdentity
nsc6600 = _Nsc6600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 2)
)
_NscDx_ObjectIdentity = ObjectIdentity
nscDx = _NscDx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 3)
)
_NscHippiSwitch_ObjectIdentity = ObjectIdentity
nscHippiSwitch = _NscHippiSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 4)
)
_NscHippiSonet_ObjectIdentity = ObjectIdentity
nscHippiSonet = _NscHippiSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5)
)
_NscErs_ObjectIdentity = ObjectIdentity
nscErs = _NscErs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 6)
)
_NscPenril_ObjectIdentity = ObjectIdentity
nscPenril = _NscPenril_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 7)
)
_NscServiceMultiplexer_ObjectIdentity = ObjectIdentity
nscServiceMultiplexer = _NscServiceMultiplexer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 8)
)
_NscBorderGuard_ObjectIdentity = ObjectIdentity
nscBorderGuard = _NscBorderGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 9)
)
_NscSecurityRouter_ObjectIdentity = ObjectIdentity
nscSecurityRouter = _NscSecurityRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 10)
)
_NscPrxy_ObjectIdentity = ObjectIdentity
nscPrxy = _NscPrxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 11)
)
_NscPrxyChan_ObjectIdentity = ObjectIdentity
nscPrxyChan = _NscPrxyChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 11, 1)
)
_NscPrxyPS_ObjectIdentity = ObjectIdentity
nscPrxyPS = _NscPrxyPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 12)
)
_NscOsx_ObjectIdentity = ObjectIdentity
nscOsx = _NscOsx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 13)
)
_NscBG1000_ObjectIdentity = ObjectIdentity
nscBG1000 = _NscBG1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 14)
)
_NscBG1000NSR_ObjectIdentity = ObjectIdentity
nscBG1000NSR = _NscBG1000NSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 14, 2)
)
_NscBG1000VPN_ObjectIdentity = ObjectIdentity
nscBG1000VPN = _NscBG1000VPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 14, 3)
)
_NscBG1000IDS_ObjectIdentity = ObjectIdentity
nscBG1000IDS = _NscBG1000IDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 14, 4)
)
_NscBG1000Sensor_ObjectIdentity = ObjectIdentity
nscBG1000Sensor = _NscBG1000Sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 14, 5)
)
_NscBG2000_ObjectIdentity = ObjectIdentity
nscBG2000 = _NscBG2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 15)
)
_NscBG2000NSR_ObjectIdentity = ObjectIdentity
nscBG2000NSR = _NscBG2000NSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 15, 2)
)
_NscBG2000VPN_ObjectIdentity = ObjectIdentity
nscBG2000VPN = _NscBG2000VPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 15, 3)
)
_NscBG2000IDS_ObjectIdentity = ObjectIdentity
nscBG2000IDS = _NscBG2000IDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 15, 4)
)
_NscBG2000Sensor_ObjectIdentity = ObjectIdentity
nscBG2000Sensor = _NscBG2000Sensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 15, 5)
)
_NscManagement_ObjectIdentity = ObjectIdentity
nscManagement = _NscManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2)
)
_NscSystem_ObjectIdentity = ObjectIdentity
nscSystem = _NscSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 1)
)
_NscTransmission_ObjectIdentity = ObjectIdentity
nscTransmission = _NscTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2)
)
_NscHippi_ObjectIdentity = ObjectIdentity
nscHippi = _NscHippi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 2, 1)
)
_NscProtocols_ObjectIdentity = ObjectIdentity
nscProtocols = _NscProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 3)
)
_NscIp_ObjectIdentity = ObjectIdentity
nscIp = _NscIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 3, 1)
)
_NscDecnet_ObjectIdentity = ObjectIdentity
nscDecnet = _NscDecnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 3, 2)
)
_NscAppletalk_ObjectIdentity = ObjectIdentity
nscAppletalk = _NscAppletalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 3, 3)
)
_NscIpx_ObjectIdentity = ObjectIdentity
nscIpx = _NscIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 3, 4)
)
_NscXns_ObjectIdentity = ObjectIdentity
nscXns = _NscXns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 3, 5)
)
_NscBridging_ObjectIdentity = ObjectIdentity
nscBridging = _NscBridging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 3, 6)
)
_NscOsi_ObjectIdentity = ObjectIdentity
nscOsi = _NscOsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 3, 7)
)
_NscVines_ObjectIdentity = ObjectIdentity
nscVines = _NscVines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 2, 3, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSC-MIB",
    **{"nsc": nsc,
       "nscExperimental": nscExperimental,
       "nscMib": nscMib,
       "nscProducts": nscProducts,
       "nscDevices": nscDevices,
       "nscObj": nscObj,
       "nscDevicesInstalled": nscDevicesInstalled,
       "nsc6600": nsc6600,
       "nscDx": nscDx,
       "nscHippiSwitch": nscHippiSwitch,
       "nscHippiSonet": nscHippiSonet,
       "nscErs": nscErs,
       "nscPenril": nscPenril,
       "nscServiceMultiplexer": nscServiceMultiplexer,
       "nscBorderGuard": nscBorderGuard,
       "nscSecurityRouter": nscSecurityRouter,
       "nscPrxy": nscPrxy,
       "nscPrxyChan": nscPrxyChan,
       "nscPrxyPS": nscPrxyPS,
       "nscOsx": nscOsx,
       "nscBG1000": nscBG1000,
       "nscBG1000NSR": nscBG1000NSR,
       "nscBG1000VPN": nscBG1000VPN,
       "nscBG1000IDS": nscBG1000IDS,
       "nscBG1000Sensor": nscBG1000Sensor,
       "nscBG2000": nscBG2000,
       "nscBG2000NSR": nscBG2000NSR,
       "nscBG2000VPN": nscBG2000VPN,
       "nscBG2000IDS": nscBG2000IDS,
       "nscBG2000Sensor": nscBG2000Sensor,
       "nscManagement": nscManagement,
       "nscSystem": nscSystem,
       "nscTransmission": nscTransmission,
       "nscHippi": nscHippi,
       "nscProtocols": nscProtocols,
       "nscIp": nscIp,
       "nscDecnet": nscDecnet,
       "nscAppletalk": nscAppletalk,
       "nscIpx": nscIpx,
       "nscXns": nscXns,
       "nscBridging": nscBridging,
       "nscOsi": nscOsi,
       "nscVines": nscVines}
)
