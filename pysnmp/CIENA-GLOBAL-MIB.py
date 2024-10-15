# SNMP MIB module (CIENA-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-GLOBAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:56 2024
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

(cienaCommon,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCommon")

(CienaGlobalSeverity,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalSeverity")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaGlobal = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaGlobalSeverity_Type = CienaGlobalSeverity
_CienaGlobalSeverity_Object = MibScalar
cienaGlobalSeverity = _CienaGlobalSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 1),
    _CienaGlobalSeverity_Type()
)
cienaGlobalSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaGlobalSeverity.setStatus("current")
_CienaGlobalMacAddress_Type = MacAddress
_CienaGlobalMacAddress_Object = MibScalar
cienaGlobalMacAddress = _CienaGlobalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1, 3, 2),
    _CienaGlobalMacAddress_Type()
)
cienaGlobalMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaGlobalMacAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-GLOBAL-MIB",
    **{"cienaGlobal": cienaGlobal,
       "cienaGlobalSeverity": cienaGlobalSeverity,
       "cienaGlobalMacAddress": cienaGlobalMacAddress}
)
