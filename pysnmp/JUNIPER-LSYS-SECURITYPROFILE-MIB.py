# SNMP MIB module (JUNIPER-LSYS-SECURITYPROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-LSYS-SECURITYPROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:28 2024
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

(jnxLsysSecurityProfile,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxLsysSecurityProfile")

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

_JnxLsysSpZone_ObjectIdentity = ObjectIdentity
jnxLsysSpZone = _JnxLsysSpZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 1)
)
_JnxLsysSpScheduler_ObjectIdentity = ObjectIdentity
jnxLsysSpScheduler = _JnxLsysSpScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 2)
)
_JnxLsysSpPolicy_ObjectIdentity = ObjectIdentity
jnxLsysSpPolicy = _JnxLsysSpPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3)
)
_JnxLsysSpPolicywcnt_ObjectIdentity = ObjectIdentity
jnxLsysSpPolicywcnt = _JnxLsysSpPolicywcnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 4)
)
_JnxLsysSpFlowgate_ObjectIdentity = ObjectIdentity
jnxLsysSpFlowgate = _JnxLsysSpFlowgate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 5)
)
_JnxLsysSpFlowsess_ObjectIdentity = ObjectIdentity
jnxLsysSpFlowsess = _JnxLsysSpFlowsess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 6)
)
_JnxLsysSpAuthentry_ObjectIdentity = ObjectIdentity
jnxLsysSpAuthentry = _JnxLsysSpAuthentry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7)
)
_JnxLsysSpNATsrcpool_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcpool = _JnxLsysSpNATsrcpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8)
)
_JnxLsysSpNATdstpool_ObjectIdentity = ObjectIdentity
jnxLsysSpNATdstpool = _JnxLsysSpNATdstpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 9)
)
_JnxLsysSpNATsrcpatad_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcpatad = _JnxLsysSpNATsrcpatad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 10)
)
_JnxLsysSpNATsrcnopatad_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcnopatad = _JnxLsysSpNATsrcnopatad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11)
)
_JnxLsysSpNATsrcrule_ObjectIdentity = ObjectIdentity
jnxLsysSpNATsrcrule = _JnxLsysSpNATsrcrule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12)
)
_JnxLsysSpNATdstrule_ObjectIdentity = ObjectIdentity
jnxLsysSpNATdstrule = _JnxLsysSpNATdstrule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 13)
)
_JnxLsysSpNATstaticrule_ObjectIdentity = ObjectIdentity
jnxLsysSpNATstaticrule = _JnxLsysSpNATstaticrule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 14)
)
_JnxLsysSpNATconebind_ObjectIdentity = ObjectIdentity
jnxLsysSpNATconebind = _JnxLsysSpNATconebind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 15)
)
_JnxLsysSpNATpoipnum_ObjectIdentity = ObjectIdentity
jnxLsysSpNATpoipnum = _JnxLsysSpNATpoipnum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16)
)
_JnxLsysSpNATRuleRefPfx_ObjectIdentity = ObjectIdentity
jnxLsysSpNATRuleRefPfx = _JnxLsysSpNATRuleRefPfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 17)
)
_JnxLsysSpCPU_ObjectIdentity = ObjectIdentity
jnxLsysSpCPU = _JnxLsysSpCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 18)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    **{"jnxLsysSpZone": jnxLsysSpZone,
       "jnxLsysSpScheduler": jnxLsysSpScheduler,
       "jnxLsysSpPolicy": jnxLsysSpPolicy,
       "jnxLsysSpPolicywcnt": jnxLsysSpPolicywcnt,
       "jnxLsysSpFlowgate": jnxLsysSpFlowgate,
       "jnxLsysSpFlowsess": jnxLsysSpFlowsess,
       "jnxLsysSpAuthentry": jnxLsysSpAuthentry,
       "jnxLsysSpNATsrcpool": jnxLsysSpNATsrcpool,
       "jnxLsysSpNATdstpool": jnxLsysSpNATdstpool,
       "jnxLsysSpNATsrcpatad": jnxLsysSpNATsrcpatad,
       "jnxLsysSpNATsrcnopatad": jnxLsysSpNATsrcnopatad,
       "jnxLsysSpNATsrcrule": jnxLsysSpNATsrcrule,
       "jnxLsysSpNATdstrule": jnxLsysSpNATdstrule,
       "jnxLsysSpNATstaticrule": jnxLsysSpNATstaticrule,
       "jnxLsysSpNATconebind": jnxLsysSpNATconebind,
       "jnxLsysSpNATpoipnum": jnxLsysSpNATpoipnum,
       "jnxLsysSpNATRuleRefPfx": jnxLsysSpNATRuleRefPfx,
       "jnxLsysSpCPU": jnxLsysSpCPU}
)
