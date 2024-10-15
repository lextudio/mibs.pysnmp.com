# SNMP MIB module (NETAL-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETAL-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:27 2024
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

networkAlchemy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2972)
)
networkAlchemy.setRevisions(
        ("2000-10-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetalProducts_ObjectIdentity = ObjectIdentity
netalProducts = _NetalProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 1)
)
if mibBuilder.loadTexts:
    netalProducts.setStatus("current")
_NetalMgmt_ObjectIdentity = ObjectIdentity
netalMgmt = _NetalMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 2)
)
if mibBuilder.loadTexts:
    netalMgmt.setStatus("current")
_CryptoCluster_ObjectIdentity = ObjectIdentity
cryptoCluster = _CryptoCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 2, 1)
)
if mibBuilder.loadTexts:
    cryptoCluster.setStatus("current")
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 2, 2)
)
if mibBuilder.loadTexts:
    ipsec.setStatus("current")
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 2, 3)
)
if mibBuilder.loadTexts:
    hardware.setStatus("current")
_Vpn_ObjectIdentity = ObjectIdentity
vpn = _Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4)
)
if mibBuilder.loadTexts:
    vpn.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 2, 5)
)
if mibBuilder.loadTexts:
    config.setStatus("current")
_NetalExperiment_ObjectIdentity = ObjectIdentity
netalExperiment = _NetalExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 3)
)
if mibBuilder.loadTexts:
    netalExperiment.setStatus("current")
_NetalAdmin_ObjectIdentity = ObjectIdentity
netalAdmin = _NetalAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 4)
)
if mibBuilder.loadTexts:
    netalAdmin.setStatus("current")
_NetalModules_ObjectIdentity = ObjectIdentity
netalModules = _NetalModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 5)
)
if mibBuilder.loadTexts:
    netalModules.setStatus("current")
_NetalTraps_ObjectIdentity = ObjectIdentity
netalTraps = _NetalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 6)
)
if mibBuilder.loadTexts:
    netalTraps.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETAL-SMI",
    **{"networkAlchemy": networkAlchemy,
       "netalProducts": netalProducts,
       "netalMgmt": netalMgmt,
       "cryptoCluster": cryptoCluster,
       "ipsec": ipsec,
       "hardware": hardware,
       "vpn": vpn,
       "config": config,
       "netalExperiment": netalExperiment,
       "netalAdmin": netalAdmin,
       "netalModules": netalModules,
       "netalTraps": netalTraps}
)
