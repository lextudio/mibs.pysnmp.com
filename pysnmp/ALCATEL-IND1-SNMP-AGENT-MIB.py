# SNMP MIB module (ALCATEL-IND1-SNMP-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-SNMP-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:05 2024
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

(softentIND1SnmpAgt,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1SnmpAgt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

alcatelIND1SNMPAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1)
)
alcatelIND1SNMPAgentMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpAgtSecurityLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("authAll", 3),
          ("authSet", 2),
          ("noSec", 1),
          ("privAll", 5),
          ("privSet", 4),
          ("trapOnly", 6))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1SNMPAgentMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1SNMPAgentMIBObjects = _AlcatelIND1SNMPAgentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIBObjects.setStatus("current")
_SnmpAgtConfig_ObjectIdentity = ObjectIdentity
snmpAgtConfig = _SnmpAgtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1)
)


class _SnmpAgtSecurityLevel_Type(SnmpAgtSecurityLevel):
    """Custom type snmpAgtSecurityLevel based on SnmpAgtSecurityLevel"""


_SnmpAgtSecurityLevel_Object = MibScalar
snmpAgtSecurityLevel = _SnmpAgtSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1, 1),
    _SnmpAgtSecurityLevel_Type()
)
snmpAgtSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgtSecurityLevel.setStatus("current")


class _SnmpAgtCommunityMode_Type(Integer32):
    """Custom type snmpAgtCommunityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SnmpAgtCommunityMode_Type.__name__ = "Integer32"
_SnmpAgtCommunityMode_Object = MibScalar
snmpAgtCommunityMode = _SnmpAgtCommunityMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 1, 2),
    _SnmpAgtCommunityMode_Type()
)
snmpAgtCommunityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgtCommunityMode.setStatus("current")
_SnmpAgtCtlFiles_ObjectIdentity = ObjectIdentity
snmpAgtCtlFiles = _SnmpAgtCtlFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    snmpAgtCtlFiles.setStatus("current")


class _SnmpAgtSourceIpConfig_Type(Integer32):
    """Custom type snmpAgtSourceIpConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("ipInterface", 3),
          ("noLoopback0", 2))
    )


_SnmpAgtSourceIpConfig_Type.__name__ = "Integer32"
_SnmpAgtSourceIpConfig_Object = MibScalar
snmpAgtSourceIpConfig = _SnmpAgtSourceIpConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 4),
    _SnmpAgtSourceIpConfig_Type()
)
snmpAgtSourceIpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgtSourceIpConfig.setStatus("current")
_SnmpAgtSourceIp_Type = IpAddress
_SnmpAgtSourceIp_Object = MibScalar
snmpAgtSourceIp = _SnmpAgtSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 1, 5),
    _SnmpAgtSourceIp_Type()
)
snmpAgtSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgtSourceIp.setStatus("current")
_AlcatelIND1SNMPAgentMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1SNMPAgentMIBConformance = _AlcatelIND1SNMPAgentMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIBConformance.setStatus("current")
_AlcatelIND1SNMPAgentMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1SNMPAgentMIBGroups = _AlcatelIND1SNMPAgentMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIBGroups.setStatus("current")
_AlcatelIND1SNMPAgentMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1SNMPAgentMIBCompliances = _AlcatelIND1SNMPAgentMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIBCompliances.setStatus("current")

# Managed Objects groups

snmpAgtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 1, 1)
)
snmpAgtConfigGroup.setObjects(
      *(("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSecurityLevel"),
        ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtCommunityMode"),
        ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIp"),
        ("ALCATEL-IND1-SNMP-AGENT-MIB", "snmpAgtSourceIpConfig"))
)
if mibBuilder.loadTexts:
    snmpAgtConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1SNMPAgentMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1SNMPAgentMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-SNMP-AGENT-MIB",
    **{"SnmpAgtSecurityLevel": SnmpAgtSecurityLevel,
       "alcatelIND1SNMPAgentMIB": alcatelIND1SNMPAgentMIB,
       "alcatelIND1SNMPAgentMIBObjects": alcatelIND1SNMPAgentMIBObjects,
       "snmpAgtConfig": snmpAgtConfig,
       "snmpAgtSecurityLevel": snmpAgtSecurityLevel,
       "snmpAgtCommunityMode": snmpAgtCommunityMode,
       "snmpAgtCtlFiles": snmpAgtCtlFiles,
       "snmpAgtSourceIpConfig": snmpAgtSourceIpConfig,
       "snmpAgtSourceIp": snmpAgtSourceIp,
       "alcatelIND1SNMPAgentMIBConformance": alcatelIND1SNMPAgentMIBConformance,
       "alcatelIND1SNMPAgentMIBGroups": alcatelIND1SNMPAgentMIBGroups,
       "snmpAgtConfigGroup": snmpAgtConfigGroup,
       "alcatelIND1SNMPAgentMIBCompliances": alcatelIND1SNMPAgentMIBCompliances,
       "alcatelIND1SNMPAgentMIBCompliance": alcatelIND1SNMPAgentMIBCompliance}
)
