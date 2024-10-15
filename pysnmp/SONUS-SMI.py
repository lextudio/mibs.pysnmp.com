# SNMP MIB module (SONUS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:49 2024
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

sonus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusProducts_ObjectIdentity = ObjectIdentity
sonusProducts = _SonusProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 1)
)
if mibBuilder.loadTexts:
    sonusProducts.setStatus("current")
_SonusGSXProducts_ObjectIdentity = ObjectIdentity
sonusGSXProducts = _SonusGSXProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 1, 1)
)
if mibBuilder.loadTexts:
    sonusGSXProducts.setStatus("current")
_SonusGSX9000_ObjectIdentity = ObjectIdentity
sonusGSX9000 = _SonusGSX9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sonusGSX9000.setStatus("current")
_SonusGSX9000HD_ObjectIdentity = ObjectIdentity
sonusGSX9000HD = _SonusGSX9000HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusGSX9000HD.setStatus("current")
_SonusPSXProducts_ObjectIdentity = ObjectIdentity
sonusPSXProducts = _SonusPSXProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 1, 2)
)
if mibBuilder.loadTexts:
    sonusPSXProducts.setStatus("current")
_SonusPSX6000_ObjectIdentity = ObjectIdentity
sonusPSX6000 = _SonusPSX6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sonusPSX6000.setStatus("current")
_SonusSGXProducts_ObjectIdentity = ObjectIdentity
sonusSGXProducts = _SonusSGXProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 1, 3)
)
if mibBuilder.loadTexts:
    sonusSGXProducts.setStatus("current")
_SonusSGX2000_ObjectIdentity = ObjectIdentity
sonusSGX2000 = _SonusSGX2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sonusSGX2000.setStatus("current")
_SonusMgmt_ObjectIdentity = ObjectIdentity
sonusMgmt = _SonusMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2)
)
if mibBuilder.loadTexts:
    sonusMgmt.setStatus("current")
_SonusSystemMIBs_ObjectIdentity = ObjectIdentity
sonusSystemMIBs = _SonusSystemMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1)
)
if mibBuilder.loadTexts:
    sonusSystemMIBs.setStatus("current")
_SonusResourcesMIBs_ObjectIdentity = ObjectIdentity
sonusResourcesMIBs = _SonusResourcesMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2)
)
if mibBuilder.loadTexts:
    sonusResourcesMIBs.setStatus("current")
_SonusPacketMIBs_ObjectIdentity = ObjectIdentity
sonusPacketMIBs = _SonusPacketMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3)
)
if mibBuilder.loadTexts:
    sonusPacketMIBs.setStatus("current")
_SonusCircuitMIBs_ObjectIdentity = ObjectIdentity
sonusCircuitMIBs = _SonusCircuitMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 4)
)
if mibBuilder.loadTexts:
    sonusCircuitMIBs.setStatus("current")
_SonusServicesMIBs_ObjectIdentity = ObjectIdentity
sonusServicesMIBs = _SonusServicesMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5)
)
if mibBuilder.loadTexts:
    sonusServicesMIBs.setStatus("current")
_SonusSignallingMIBs_ObjectIdentity = ObjectIdentity
sonusSignallingMIBs = _SonusSignallingMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6)
)
if mibBuilder.loadTexts:
    sonusSignallingMIBs.setStatus("current")
_SonusToolsMIBs_ObjectIdentity = ObjectIdentity
sonusToolsMIBs = _SonusToolsMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 7)
)
if mibBuilder.loadTexts:
    sonusToolsMIBs.setStatus("current")
_SonusModules_ObjectIdentity = ObjectIdentity
sonusModules = _SonusModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 3)
)
if mibBuilder.loadTexts:
    sonusModules.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-SMI",
    **{"sonus": sonus,
       "sonusProducts": sonusProducts,
       "sonusGSXProducts": sonusGSXProducts,
       "sonusGSX9000": sonusGSX9000,
       "sonusGSX9000HD": sonusGSX9000HD,
       "sonusPSXProducts": sonusPSXProducts,
       "sonusPSX6000": sonusPSX6000,
       "sonusSGXProducts": sonusSGXProducts,
       "sonusSGX2000": sonusSGX2000,
       "sonusMgmt": sonusMgmt,
       "sonusSystemMIBs": sonusSystemMIBs,
       "sonusResourcesMIBs": sonusResourcesMIBs,
       "sonusPacketMIBs": sonusPacketMIBs,
       "sonusCircuitMIBs": sonusCircuitMIBs,
       "sonusServicesMIBs": sonusServicesMIBs,
       "sonusSignallingMIBs": sonusSignallingMIBs,
       "sonusToolsMIBs": sonusToolsMIBs,
       "sonusModules": sonusModules}
)
