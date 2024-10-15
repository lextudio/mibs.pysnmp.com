# SNMP MIB module (JUNIPER-JS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JS-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:52 2024
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

(jnxJsMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxJsMibRoot")

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

_JnxJsSecurity_ObjectIdentity = ObjectIdentity
jnxJsSecurity = _JnxJsSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1)
)
_JnxJsIf_ObjectIdentity = ObjectIdentity
jnxJsIf = _JnxJsIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1)
)
_JnxJsAuth_ObjectIdentity = ObjectIdentity
jnxJsAuth = _JnxJsAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 2)
)
_JnxJsCertificates_ObjectIdentity = ObjectIdentity
jnxJsCertificates = _JnxJsCertificates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3)
)
_JnxJsPolicies_ObjectIdentity = ObjectIdentity
jnxJsPolicies = _JnxJsPolicies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 4)
)
_JnxJsIPSecVpn_ObjectIdentity = ObjectIdentity
jnxJsIPSecVpn = _JnxJsIPSecVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5)
)
_JnxJsNAT_ObjectIdentity = ObjectIdentity
jnxJsNAT = _JnxJsNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 7)
)
_JnxJsScreening_ObjectIdentity = ObjectIdentity
jnxJsScreening = _JnxJsScreening_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8)
)
_JnxJsDhcp_ObjectIdentity = ObjectIdentity
jnxJsDhcp = _JnxJsDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 9)
)
_JnxJsDnsRoot_ObjectIdentity = ObjectIdentity
jnxJsDnsRoot = _JnxJsDnsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 10)
)
_JnxJsIdpRoot_ObjectIdentity = ObjectIdentity
jnxJsIdpRoot = _JnxJsIdpRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 11)
)
_JnxJsSPUMonitoringRoot_ObjectIdentity = ObjectIdentity
jnxJsSPUMonitoringRoot = _JnxJsSPUMonitoringRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12)
)
_JnxJsUTMRoot_ObjectIdentity = ObjectIdentity
jnxJsUTMRoot = _JnxJsUTMRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 13)
)
_JnxJsChassisCluster_ObjectIdentity = ObjectIdentity
jnxJsChassisCluster = _JnxJsChassisCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 14)
)
_JnxVoip_ObjectIdentity = ObjectIdentity
jnxVoip = _JnxVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15)
)
_JnxJsPacketMirror_ObjectIdentity = ObjectIdentity
jnxJsPacketMirror = _JnxJsPacketMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 16)
)
_JnxLsysSecurityProfile_ObjectIdentity = ObjectIdentity
jnxLsysSecurityProfile = _JnxLsysSecurityProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-SMI",
    **{"jnxJsSecurity": jnxJsSecurity,
       "jnxJsIf": jnxJsIf,
       "jnxJsAuth": jnxJsAuth,
       "jnxJsCertificates": jnxJsCertificates,
       "jnxJsPolicies": jnxJsPolicies,
       "jnxJsIPSecVpn": jnxJsIPSecVpn,
       "jnxJsNAT": jnxJsNAT,
       "jnxJsScreening": jnxJsScreening,
       "jnxJsDhcp": jnxJsDhcp,
       "jnxJsDnsRoot": jnxJsDnsRoot,
       "jnxJsIdpRoot": jnxJsIdpRoot,
       "jnxJsSPUMonitoringRoot": jnxJsSPUMonitoringRoot,
       "jnxJsUTMRoot": jnxJsUTMRoot,
       "jnxJsChassisCluster": jnxJsChassisCluster,
       "jnxVoip": jnxVoip,
       "jnxJsPacketMirror": jnxJsPacketMirror,
       "jnxLsysSecurityProfile": jnxLsysSecurityProfile}
)
