# SNMP MIB module (SNMPv2-USEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMPv2-USEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:23 2024
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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

usecMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )



# MIB Managed Objects in the order of their OIDs

_UsecMIBObjects_ObjectIdentity = ObjectIdentity
usecMIBObjects = _UsecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 6, 1)
)
_UsecAgent_ObjectIdentity = ObjectIdentity
usecAgent = _UsecAgent_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 6, 1, 1)
)
_AgentID_Type = AgentID
_AgentID_Object = MibScalar
agentID = _AgentID_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 1, 1),
    _AgentID_Type()
)
agentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentID.setStatus("current")
_AgentBoots_Type = Unsigned32
_AgentBoots_Object = MibScalar
agentBoots = _AgentBoots_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 1, 2),
    _AgentBoots_Type()
)
agentBoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBoots.setStatus("current")


class _AgentTime_Type(Unsigned32):
    """Custom type agentTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentTime_Type.__name__ = "Unsigned32"
_AgentTime_Object = MibScalar
agentTime = _AgentTime_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 1, 3),
    _AgentTime_Type()
)
agentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTime.setStatus("current")
if mibBuilder.loadTexts:
    agentTime.setUnits("seconds")


class _AgentSize_Type(Integer32):
    """Custom type agentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 65507),
    )


_AgentSize_Type.__name__ = "Integer32"
_AgentSize_Object = MibScalar
agentSize = _AgentSize_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 1, 4),
    _AgentSize_Type()
)
agentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSize.setStatus("current")
_UsecStats_ObjectIdentity = ObjectIdentity
usecStats = _UsecStats_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 6, 1, 2)
)
_UsecStatsUnsupportedQoS_Type = Counter32
_UsecStatsUnsupportedQoS_Object = MibScalar
usecStatsUnsupportedQoS = _UsecStatsUnsupportedQoS_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 2, 1),
    _UsecStatsUnsupportedQoS_Type()
)
usecStatsUnsupportedQoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usecStatsUnsupportedQoS.setStatus("current")
_UsecStatsNotInWindows_Type = Counter32
_UsecStatsNotInWindows_Object = MibScalar
usecStatsNotInWindows = _UsecStatsNotInWindows_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 2, 2),
    _UsecStatsNotInWindows_Type()
)
usecStatsNotInWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usecStatsNotInWindows.setStatus("current")
_UsecStatsUnknownUserNames_Type = Counter32
_UsecStatsUnknownUserNames_Object = MibScalar
usecStatsUnknownUserNames = _UsecStatsUnknownUserNames_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 2, 3),
    _UsecStatsUnknownUserNames_Type()
)
usecStatsUnknownUserNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usecStatsUnknownUserNames.setStatus("current")
_UsecStatsWrongDigestValues_Type = Counter32
_UsecStatsWrongDigestValues_Object = MibScalar
usecStatsWrongDigestValues = _UsecStatsWrongDigestValues_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 2, 4),
    _UsecStatsWrongDigestValues_Type()
)
usecStatsWrongDigestValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usecStatsWrongDigestValues.setStatus("current")
_UsecStatsUnknownContexts_Type = Counter32
_UsecStatsUnknownContexts_Object = MibScalar
usecStatsUnknownContexts = _UsecStatsUnknownContexts_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 2, 5),
    _UsecStatsUnknownContexts_Type()
)
usecStatsUnknownContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usecStatsUnknownContexts.setStatus("current")
_UsecStatsBadParameters_Type = Counter32
_UsecStatsBadParameters_Object = MibScalar
usecStatsBadParameters = _UsecStatsBadParameters_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 2, 6),
    _UsecStatsBadParameters_Type()
)
usecStatsBadParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usecStatsBadParameters.setStatus("current")
_UsecStatsUnauthorizedOperations_Type = Counter32
_UsecStatsUnauthorizedOperations_Object = MibScalar
usecStatsUnauthorizedOperations = _UsecStatsUnauthorizedOperations_Object(
    (1, 3, 6, 1, 6, 3, 6, 1, 2, 7),
    _UsecStatsUnauthorizedOperations_Type()
)
usecStatsUnauthorizedOperations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usecStatsUnauthorizedOperations.setStatus("current")
_UsecMIBConformance_ObjectIdentity = ObjectIdentity
usecMIBConformance = _UsecMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 6, 2)
)
_UsecMIBCompliances_ObjectIdentity = ObjectIdentity
usecMIBCompliances = _UsecMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 6, 2, 1)
)
_UsecMIBGroups_ObjectIdentity = ObjectIdentity
usecMIBGroups = _UsecMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 6, 2, 2)
)

# Managed Objects groups

usecBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 6, 2, 2, 1)
)
usecBasicGroup.setObjects(
      *(("SNMPv2-USEC-MIB", "agentID"),
        ("SNMPv2-USEC-MIB", "agentBoots"),
        ("SNMPv2-USEC-MIB", "agentTime"),
        ("SNMPv2-USEC-MIB", "agentSize"))
)
if mibBuilder.loadTexts:
    usecBasicGroup.setStatus("current")

usecStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 6, 2, 2, 2)
)
usecStatsGroup.setObjects(
      *(("SNMPv2-USEC-MIB", "usecStatsUnsupportedQoS"),
        ("SNMPv2-USEC-MIB", "usecStatsNotInWindows"),
        ("SNMPv2-USEC-MIB", "usecStatsUnknownUserNames"),
        ("SNMPv2-USEC-MIB", "usecStatsWrongDigestValues"),
        ("SNMPv2-USEC-MIB", "usecStatsUnknownContexts"),
        ("SNMPv2-USEC-MIB", "usecStatsBadParameters"),
        ("SNMPv2-USEC-MIB", "usecStatsUnauthorizedOperations"))
)
if mibBuilder.loadTexts:
    usecStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usecMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usecMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMPv2-USEC-MIB",
    **{"AgentID": AgentID,
       "usecMIB": usecMIB,
       "usecMIBObjects": usecMIBObjects,
       "usecAgent": usecAgent,
       "agentID": agentID,
       "agentBoots": agentBoots,
       "agentTime": agentTime,
       "agentSize": agentSize,
       "usecStats": usecStats,
       "usecStatsUnsupportedQoS": usecStatsUnsupportedQoS,
       "usecStatsNotInWindows": usecStatsNotInWindows,
       "usecStatsUnknownUserNames": usecStatsUnknownUserNames,
       "usecStatsWrongDigestValues": usecStatsWrongDigestValues,
       "usecStatsUnknownContexts": usecStatsUnknownContexts,
       "usecStatsBadParameters": usecStatsBadParameters,
       "usecStatsUnauthorizedOperations": usecStatsUnauthorizedOperations,
       "usecMIBConformance": usecMIBConformance,
       "usecMIBCompliances": usecMIBCompliances,
       "usecMIBCompliance": usecMIBCompliance,
       "usecMIBGroups": usecMIBGroups,
       "usecBasicGroup": usecBasicGroup,
       "usecStatsGroup": usecStatsGroup}
)
