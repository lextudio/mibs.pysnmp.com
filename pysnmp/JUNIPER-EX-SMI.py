# SNMP MIB module (JUNIPER-EX-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-EX-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:47 2024
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

(jnxExMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxExMibRoot")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxExSwitching_ObjectIdentity = ObjectIdentity
jnxExSwitching = _JnxExSwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1)
)
_JnxExAnalyzer_ObjectIdentity = ObjectIdentity
jnxExAnalyzer = _JnxExAnalyzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 1)
)
_JnxExSecureAccessPort_ObjectIdentity = ObjectIdentity
jnxExSecureAccessPort = _JnxExSecureAccessPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2)
)
_JnxExPaeExtension_ObjectIdentity = ObjectIdentity
jnxExPaeExtension = _JnxExPaeExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 3)
)
_JnxExVirtualChassis_ObjectIdentity = ObjectIdentity
jnxExVirtualChassis = _JnxExVirtualChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 4)
)
_JnxExVlan_ObjectIdentity = ObjectIdentity
jnxExVlan = _JnxExVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5)
)
_JnxRPS_ObjectIdentity = ObjectIdentity
jnxRPS = _JnxRPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6)
)
_JnxMacNotificationRoot_ObjectIdentity = ObjectIdentity
jnxMacNotificationRoot = _JnxMacNotificationRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-EX-SMI",
    **{"jnxExSwitching": jnxExSwitching,
       "jnxExAnalyzer": jnxExAnalyzer,
       "jnxExSecureAccessPort": jnxExSecureAccessPort,
       "jnxExPaeExtension": jnxExPaeExtension,
       "jnxExVirtualChassis": jnxExVirtualChassis,
       "jnxExVlan": jnxExVlan,
       "jnxRPS": jnxRPS,
       "jnxMacNotificationRoot": jnxMacNotificationRoot}
)
