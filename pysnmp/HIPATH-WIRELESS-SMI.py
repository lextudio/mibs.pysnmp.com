# SNMP MIB module (HIPATH-WIRELESS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIPATH-WIRELESS-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:29 2024
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

hiPathWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15)
)
hiPathWireless.setRevisions(
        ("2005-07-21 02:37",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Siemens_ObjectIdentity = ObjectIdentity
siemens = _Siemens_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329)
)
_HiPathWirelessProducts_ObjectIdentity = ObjectIdentity
hiPathWirelessProducts = _HiPathWirelessProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 1)
)
if mibBuilder.loadTexts:
    hiPathWirelessProducts.setStatus("current")
_HiPathWirelessMgmt_ObjectIdentity = ObjectIdentity
hiPathWirelessMgmt = _HiPathWirelessMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3)
)
if mibBuilder.loadTexts:
    hiPathWirelessMgmt.setStatus("current")
_HiPathWirelessDevelopment_ObjectIdentity = ObjectIdentity
hiPathWirelessDevelopment = _HiPathWirelessDevelopment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 4)
)
if mibBuilder.loadTexts:
    hiPathWirelessDevelopment.setStatus("current")
_HiPathWirelessModules_ObjectIdentity = ObjectIdentity
hiPathWirelessModules = _HiPathWirelessModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 5)
)
if mibBuilder.loadTexts:
    hiPathWirelessModules.setStatus("current")
_HiPathWirelessHWM_ObjectIdentity = ObjectIdentity
hiPathWirelessHWM = _HiPathWirelessHWM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 6)
)
if mibBuilder.loadTexts:
    hiPathWirelessHWM.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIPATH-WIRELESS-SMI",
    **{"siemens": siemens,
       "hiPathWireless": hiPathWireless,
       "hiPathWirelessProducts": hiPathWirelessProducts,
       "hiPathWirelessMgmt": hiPathWirelessMgmt,
       "hiPathWirelessDevelopment": hiPathWirelessDevelopment,
       "hiPathWirelessModules": hiPathWirelessModules,
       "hiPathWirelessHWM": hiPathWirelessHWM}
)
