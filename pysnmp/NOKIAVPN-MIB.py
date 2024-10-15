# SNMP MIB module (NOKIAVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIAVPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:45 2024
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

(nokiaVPN,) = mibBuilder.importSymbols(
    "NOKIA-OID-REGISTRATION-MIB",
    "nokiaVPN")

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

_NokiaVPNProducts_ObjectIdentity = ObjectIdentity
nokiaVPNProducts = _NokiaVPNProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1)
)
if mibBuilder.loadTexts:
    nokiaVPNProducts.setStatus("current")
_NokiaHardwareUnknown_ObjectIdentity = ObjectIdentity
nokiaHardwareUnknown = _NokiaHardwareUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 1)
)
if mibBuilder.loadTexts:
    nokiaHardwareUnknown.setStatus("current")
_NokiaCryptoCluster500_ObjectIdentity = ObjectIdentity
nokiaCryptoCluster500 = _NokiaCryptoCluster500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 4)
)
if mibBuilder.loadTexts:
    nokiaCryptoCluster500.setStatus("current")
_NokiaCryptoCluster5010_ObjectIdentity = ObjectIdentity
nokiaCryptoCluster5010 = _NokiaCryptoCluster5010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 5)
)
if mibBuilder.loadTexts:
    nokiaCryptoCluster5010.setStatus("current")
_NokiaCryptoCluster501_ObjectIdentity = ObjectIdentity
nokiaCryptoCluster501 = _NokiaCryptoCluster501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 8)
)
if mibBuilder.loadTexts:
    nokiaCryptoCluster501.setStatus("current")
_NokiaCryptoCluster5000_ObjectIdentity = ObjectIdentity
nokiaCryptoCluster5000 = _NokiaCryptoCluster5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 10)
)
if mibBuilder.loadTexts:
    nokiaCryptoCluster5000.setStatus("current")
_NokiaCryptoCluster2500_ObjectIdentity = ObjectIdentity
nokiaCryptoCluster2500 = _NokiaCryptoCluster2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 11)
)
if mibBuilder.loadTexts:
    nokiaCryptoCluster2500.setStatus("current")
_NokiaCryptoCluster2501_ObjectIdentity = ObjectIdentity
nokiaCryptoCluster2501 = _NokiaCryptoCluster2501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 12)
)
if mibBuilder.loadTexts:
    nokiaCryptoCluster2501.setStatus("current")
_NokiaCryptoCluster5200_ObjectIdentity = ObjectIdentity
nokiaCryptoCluster5200 = _NokiaCryptoCluster5200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 15)
)
if mibBuilder.loadTexts:
    nokiaCryptoCluster5200.setStatus("current")
_NokiaCryptoCluster5205_ObjectIdentity = ObjectIdentity
nokiaCryptoCluster5205 = _NokiaCryptoCluster5205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 16)
)
if mibBuilder.loadTexts:
    nokiaCryptoCluster5205.setStatus("current")
_NokiaCA200_ObjectIdentity = ObjectIdentity
nokiaCA200 = _NokiaCA200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 18)
)
if mibBuilder.loadTexts:
    nokiaCA200.setStatus("current")
_NokiaCA600_ObjectIdentity = ObjectIdentity
nokiaCA600 = _NokiaCA600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 19)
)
if mibBuilder.loadTexts:
    nokiaCA600.setStatus("current")
_NokiaCryptoCluster100_ObjectIdentity = ObjectIdentity
nokiaCryptoCluster100 = _NokiaCryptoCluster100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 1, 20)
)
if mibBuilder.loadTexts:
    nokiaCryptoCluster100.setStatus("current")
_NokiaVPNMgmt_ObjectIdentity = ObjectIdentity
nokiaVPNMgmt = _NokiaVPNMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2)
)
if mibBuilder.loadTexts:
    nokiaVPNMgmt.setStatus("current")
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 1)
)
if mibBuilder.loadTexts:
    ipsec.setStatus("current")
_Vpn_ObjectIdentity = ObjectIdentity
vpn = _Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 2)
)
if mibBuilder.loadTexts:
    vpn.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 2, 3)
)
if mibBuilder.loadTexts:
    config.setStatus("current")
_NokiaVPNExperiment_ObjectIdentity = ObjectIdentity
nokiaVPNExperiment = _NokiaVPNExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 3)
)
if mibBuilder.loadTexts:
    nokiaVPNExperiment.setStatus("current")
_NokiaVPNAdmin_ObjectIdentity = ObjectIdentity
nokiaVPNAdmin = _NokiaVPNAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 4)
)
if mibBuilder.loadTexts:
    nokiaVPNAdmin.setStatus("current")
_NokiaVPNModules_ObjectIdentity = ObjectIdentity
nokiaVPNModules = _NokiaVPNModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 5)
)
if mibBuilder.loadTexts:
    nokiaVPNModules.setStatus("current")
_NokiaVPNTraps_ObjectIdentity = ObjectIdentity
nokiaVPNTraps = _NokiaVPNTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 41, 6)
)
if mibBuilder.loadTexts:
    nokiaVPNTraps.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIAVPN-MIB",
    **{"nokiaVPNProducts": nokiaVPNProducts,
       "nokiaHardwareUnknown": nokiaHardwareUnknown,
       "nokiaCryptoCluster500": nokiaCryptoCluster500,
       "nokiaCryptoCluster5010": nokiaCryptoCluster5010,
       "nokiaCryptoCluster501": nokiaCryptoCluster501,
       "nokiaCryptoCluster5000": nokiaCryptoCluster5000,
       "nokiaCryptoCluster2500": nokiaCryptoCluster2500,
       "nokiaCryptoCluster2501": nokiaCryptoCluster2501,
       "nokiaCryptoCluster5200": nokiaCryptoCluster5200,
       "nokiaCryptoCluster5205": nokiaCryptoCluster5205,
       "nokiaCA200": nokiaCA200,
       "nokiaCA600": nokiaCA600,
       "nokiaCryptoCluster100": nokiaCryptoCluster100,
       "nokiaVPNMgmt": nokiaVPNMgmt,
       "ipsec": ipsec,
       "vpn": vpn,
       "config": config,
       "nokiaVPNExperiment": nokiaVPNExperiment,
       "nokiaVPNAdmin": nokiaVPNAdmin,
       "nokiaVPNModules": nokiaVPNModules,
       "nokiaVPNTraps": nokiaVPNTraps}
)
