# SNMP MIB module (NOKIA-ALCHEMYOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-ALCHEMYOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:31 2024
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

(nokiaAlchemyOS,) = mibBuilder.importSymbols(
    "NOKIA-OID-REGISTRATION-MIB",
    "nokiaAlchemyOS")

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

_AlchemyOSProducts_ObjectIdentity = ObjectIdentity
alchemyOSProducts = _AlchemyOSProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 1)
)
if mibBuilder.loadTexts:
    alchemyOSProducts.setStatus("current")
_AlchemyOSMgmt_ObjectIdentity = ObjectIdentity
alchemyOSMgmt = _AlchemyOSMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2)
)
if mibBuilder.loadTexts:
    alchemyOSMgmt.setStatus("current")
_CryptoCluster_ObjectIdentity = ObjectIdentity
cryptoCluster = _CryptoCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 1)
)
if mibBuilder.loadTexts:
    cryptoCluster.setStatus("current")
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 2)
)
if mibBuilder.loadTexts:
    hardware.setStatus("current")
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 2, 3)
)
if mibBuilder.loadTexts:
    firewall.setStatus("current")
_AlchemyOSExperiment_ObjectIdentity = ObjectIdentity
alchemyOSExperiment = _AlchemyOSExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 3)
)
if mibBuilder.loadTexts:
    alchemyOSExperiment.setStatus("current")
_AlchemyOSAdmin_ObjectIdentity = ObjectIdentity
alchemyOSAdmin = _AlchemyOSAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 4)
)
if mibBuilder.loadTexts:
    alchemyOSAdmin.setStatus("current")
_AlchemyOSModules_ObjectIdentity = ObjectIdentity
alchemyOSModules = _AlchemyOSModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 5)
)
if mibBuilder.loadTexts:
    alchemyOSModules.setStatus("current")
_AlchemyOSTraps_ObjectIdentity = ObjectIdentity
alchemyOSTraps = _AlchemyOSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 94, 1, 45, 6)
)
if mibBuilder.loadTexts:
    alchemyOSTraps.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-ALCHEMYOS-MIB",
    **{"alchemyOSProducts": alchemyOSProducts,
       "alchemyOSMgmt": alchemyOSMgmt,
       "cryptoCluster": cryptoCluster,
       "hardware": hardware,
       "firewall": firewall,
       "alchemyOSExperiment": alchemyOSExperiment,
       "alchemyOSAdmin": alchemyOSAdmin,
       "alchemyOSModules": alchemyOSModules,
       "alchemyOSTraps": alchemyOSTraps}
)
