# SNMP MIB module (ENTERASYS-NAC-APPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-NAC-APPLIANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:16 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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

etsysNacApplianceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73)
)
etsysNacApplianceMIB.setRevisions(
        ("2010-03-09 13:03",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysNacApplianceObjects_ObjectIdentity = ObjectIdentity
etsysNacApplianceObjects = _EtsysNacApplianceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1)
)
_EtsysNacApplAuthenticationRequests_Type = Counter64
_EtsysNacApplAuthenticationRequests_Object = MibScalar
etsysNacApplAuthenticationRequests = _EtsysNacApplAuthenticationRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 1),
    _EtsysNacApplAuthenticationRequests_Type()
)
etsysNacApplAuthenticationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplAuthenticationRequests.setStatus("current")
_EtsysNacApplAuthenticationSuccesses_Type = Counter64
_EtsysNacApplAuthenticationSuccesses_Object = MibScalar
etsysNacApplAuthenticationSuccesses = _EtsysNacApplAuthenticationSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 2),
    _EtsysNacApplAuthenticationSuccesses_Type()
)
etsysNacApplAuthenticationSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplAuthenticationSuccesses.setStatus("current")
_EtsysNacApplAuthenticationFailures_Type = Counter64
_EtsysNacApplAuthenticationFailures_Object = MibScalar
etsysNacApplAuthenticationFailures = _EtsysNacApplAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 3),
    _EtsysNacApplAuthenticationFailures_Type()
)
etsysNacApplAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplAuthenticationFailures.setStatus("current")
_EtsysNacApplRadiusChallenges_Type = Counter64
_EtsysNacApplRadiusChallenges_Object = MibScalar
etsysNacApplRadiusChallenges = _EtsysNacApplRadiusChallenges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 4),
    _EtsysNacApplRadiusChallenges_Type()
)
etsysNacApplRadiusChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplRadiusChallenges.setStatus("current")
_EtsysNacApplAuthenticationInvalidRequests_Type = Counter64
_EtsysNacApplAuthenticationInvalidRequests_Object = MibScalar
etsysNacApplAuthenticationInvalidRequests = _EtsysNacApplAuthenticationInvalidRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 5),
    _EtsysNacApplAuthenticationInvalidRequests_Type()
)
etsysNacApplAuthenticationInvalidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplAuthenticationInvalidRequests.setStatus("current")
_EtsysNacApplAuthenticationDuplicateRequests_Type = Counter64
_EtsysNacApplAuthenticationDuplicateRequests_Object = MibScalar
etsysNacApplAuthenticationDuplicateRequests = _EtsysNacApplAuthenticationDuplicateRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 6),
    _EtsysNacApplAuthenticationDuplicateRequests_Type()
)
etsysNacApplAuthenticationDuplicateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplAuthenticationDuplicateRequests.setStatus("current")
_EtsysNacApplAuthenticationMalformedRequests_Type = Counter64
_EtsysNacApplAuthenticationMalformedRequests_Object = MibScalar
etsysNacApplAuthenticationMalformedRequests = _EtsysNacApplAuthenticationMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 7),
    _EtsysNacApplAuthenticationMalformedRequests_Type()
)
etsysNacApplAuthenticationMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplAuthenticationMalformedRequests.setStatus("current")
_EtsysNacApplAuthenticationBadRequests_Type = Counter64
_EtsysNacApplAuthenticationBadRequests_Object = MibScalar
etsysNacApplAuthenticationBadRequests = _EtsysNacApplAuthenticationBadRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 8),
    _EtsysNacApplAuthenticationBadRequests_Type()
)
etsysNacApplAuthenticationBadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplAuthenticationBadRequests.setStatus("current")
_EtsysNacApplAuthenticationDroppedPackets_Type = Counter64
_EtsysNacApplAuthenticationDroppedPackets_Object = MibScalar
etsysNacApplAuthenticationDroppedPackets = _EtsysNacApplAuthenticationDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 9),
    _EtsysNacApplAuthenticationDroppedPackets_Type()
)
etsysNacApplAuthenticationDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplAuthenticationDroppedPackets.setStatus("current")
_EtsysNacApplAuthenticationUnknownTypes_Type = Counter64
_EtsysNacApplAuthenticationUnknownTypes_Object = MibScalar
etsysNacApplAuthenticationUnknownTypes = _EtsysNacApplAuthenticationUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 10),
    _EtsysNacApplAuthenticationUnknownTypes_Type()
)
etsysNacApplAuthenticationUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplAuthenticationUnknownTypes.setStatus("current")
_EtsysNacApplAssessmentRequests_Type = Counter64
_EtsysNacApplAssessmentRequests_Object = MibScalar
etsysNacApplAssessmentRequests = _EtsysNacApplAssessmentRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 11),
    _EtsysNacApplAssessmentRequests_Type()
)
etsysNacApplAssessmentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplAssessmentRequests.setStatus("current")
_EtsysNacApplCaptivePortalRequests_Type = Counter64
_EtsysNacApplCaptivePortalRequests_Object = MibScalar
etsysNacApplCaptivePortalRequests = _EtsysNacApplCaptivePortalRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 12),
    _EtsysNacApplCaptivePortalRequests_Type()
)
etsysNacApplCaptivePortalRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplCaptivePortalRequests.setStatus("current")
_EtsysNacApplContactLostSwitches_Type = Counter64
_EtsysNacApplContactLostSwitches_Object = MibScalar
etsysNacApplContactLostSwitches = _EtsysNacApplContactLostSwitches_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 13),
    _EtsysNacApplContactLostSwitches_Type()
)
etsysNacApplContactLostSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplContactLostSwitches.setStatus("current")
_EtsysNacApplIPResolutionFailures_Type = Counter64
_EtsysNacApplIPResolutionFailures_Object = MibScalar
etsysNacApplIPResolutionFailures = _EtsysNacApplIPResolutionFailures_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 14),
    _EtsysNacApplIPResolutionFailures_Type()
)
etsysNacApplIPResolutionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplIPResolutionFailures.setStatus("current")
_EtsysNacApplIPResolutionTimeouts_Type = Counter64
_EtsysNacApplIPResolutionTimeouts_Object = MibScalar
etsysNacApplIPResolutionTimeouts = _EtsysNacApplIPResolutionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 15),
    _EtsysNacApplIPResolutionTimeouts_Type()
)
etsysNacApplIPResolutionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplIPResolutionTimeouts.setStatus("current")
_EtsysNacApplConnectedAgents_Type = Counter64
_EtsysNacApplConnectedAgents_Object = MibScalar
etsysNacApplConnectedAgents = _EtsysNacApplConnectedAgents_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 1, 16),
    _EtsysNacApplConnectedAgents_Type()
)
etsysNacApplConnectedAgents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNacApplConnectedAgents.setStatus("current")
_EtsysNacApplianceMIBConformance_ObjectIdentity = ObjectIdentity
etsysNacApplianceMIBConformance = _EtsysNacApplianceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 2)
)
_EtsysNacApplianceMIBGroups_ObjectIdentity = ObjectIdentity
etsysNacApplianceMIBGroups = _EtsysNacApplianceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 2, 1)
)
_EtsysNacApplianceMIBCompliances_ObjectIdentity = ObjectIdentity
etsysNacApplianceMIBCompliances = _EtsysNacApplianceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 2, 2)
)

# Managed Objects groups

etsysNacApplianceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 2, 1, 1)
)
etsysNacApplianceMIBGroup.setObjects(
      *(("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplAuthenticationRequests"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplAuthenticationSuccesses"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplAuthenticationFailures"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplRadiusChallenges"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplAuthenticationInvalidRequests"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplAuthenticationDuplicateRequests"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplAuthenticationMalformedRequests"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplAuthenticationBadRequests"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplAuthenticationDroppedPackets"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplAuthenticationUnknownTypes"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplAssessmentRequests"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplCaptivePortalRequests"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplContactLostSwitches"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplIPResolutionFailures"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplIPResolutionTimeouts"),
        ("ENTERASYS-NAC-APPLIANCE-MIB", "etsysNacApplConnectedAgents"))
)
if mibBuilder.loadTexts:
    etsysNacApplianceMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysNacApplianceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 73, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysNacApplianceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-NAC-APPLIANCE-MIB",
    **{"etsysNacApplianceMIB": etsysNacApplianceMIB,
       "etsysNacApplianceObjects": etsysNacApplianceObjects,
       "etsysNacApplAuthenticationRequests": etsysNacApplAuthenticationRequests,
       "etsysNacApplAuthenticationSuccesses": etsysNacApplAuthenticationSuccesses,
       "etsysNacApplAuthenticationFailures": etsysNacApplAuthenticationFailures,
       "etsysNacApplRadiusChallenges": etsysNacApplRadiusChallenges,
       "etsysNacApplAuthenticationInvalidRequests": etsysNacApplAuthenticationInvalidRequests,
       "etsysNacApplAuthenticationDuplicateRequests": etsysNacApplAuthenticationDuplicateRequests,
       "etsysNacApplAuthenticationMalformedRequests": etsysNacApplAuthenticationMalformedRequests,
       "etsysNacApplAuthenticationBadRequests": etsysNacApplAuthenticationBadRequests,
       "etsysNacApplAuthenticationDroppedPackets": etsysNacApplAuthenticationDroppedPackets,
       "etsysNacApplAuthenticationUnknownTypes": etsysNacApplAuthenticationUnknownTypes,
       "etsysNacApplAssessmentRequests": etsysNacApplAssessmentRequests,
       "etsysNacApplCaptivePortalRequests": etsysNacApplCaptivePortalRequests,
       "etsysNacApplContactLostSwitches": etsysNacApplContactLostSwitches,
       "etsysNacApplIPResolutionFailures": etsysNacApplIPResolutionFailures,
       "etsysNacApplIPResolutionTimeouts": etsysNacApplIPResolutionTimeouts,
       "etsysNacApplConnectedAgents": etsysNacApplConnectedAgents,
       "etsysNacApplianceMIBConformance": etsysNacApplianceMIBConformance,
       "etsysNacApplianceMIBGroups": etsysNacApplianceMIBGroups,
       "etsysNacApplianceMIBGroup": etsysNacApplianceMIBGroup,
       "etsysNacApplianceMIBCompliances": etsysNacApplianceMIBCompliances,
       "etsysNacApplianceMIBCompliance": etsysNacApplianceMIBCompliance}
)
