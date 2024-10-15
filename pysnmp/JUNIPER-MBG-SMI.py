# SNMP MIB module (JUNIPER-MBG-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MBG-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:42 2024
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

(jnxJunosSpace,
 jnxMobileGatewayMibRoot) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxJunosSpace",
    "jnxMobileGatewayMibRoot")

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

_JnxJunosSpaceMobility_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobility = _JnxJunosSpaceMobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2)
)
_JnxJunosSpaceMobilityNotifications_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobilityNotifications = _JnxJunosSpaceMobilityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 1)
)
_JnxJunosSpaceMobilityObjects_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobilityObjects = _JnxJunosSpaceMobilityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 2)
)
_JnxJunosSpaceMobilityNotificationvars_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobilityNotificationvars = _JnxJunosSpaceMobilityNotificationvars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 2, 1)
)
_JnxJunosSpaceMobilityMCM_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobilityMCM = _JnxJunosSpaceMobilityMCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 3)
)
_JnxJunosSpaceMobilityMTM_ObjectIdentity = ObjectIdentity
jnxJunosSpaceMobilityMTM = _JnxJunosSpaceMobilityMTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1, 3, 2, 4)
)
_JnxMobileGatewayPgwGgsn_ObjectIdentity = ObjectIdentity
jnxMobileGatewayPgwGgsn = _JnxMobileGatewayPgwGgsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1)
)
_JnxMobileGatewaySgw_ObjectIdentity = ObjectIdentity
jnxMobileGatewaySgw = _JnxMobileGatewaySgw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MBG-SMI",
    **{"jnxJunosSpaceMobility": jnxJunosSpaceMobility,
       "jnxJunosSpaceMobilityNotifications": jnxJunosSpaceMobilityNotifications,
       "jnxJunosSpaceMobilityObjects": jnxJunosSpaceMobilityObjects,
       "jnxJunosSpaceMobilityNotificationvars": jnxJunosSpaceMobilityNotificationvars,
       "jnxJunosSpaceMobilityMCM": jnxJunosSpaceMobilityMCM,
       "jnxJunosSpaceMobilityMTM": jnxJunosSpaceMobilityMTM,
       "jnxMobileGatewayPgwGgsn": jnxMobileGatewayPgwGgsn,
       "jnxMobileGatewaySgw": jnxMobileGatewaySgw}
)
