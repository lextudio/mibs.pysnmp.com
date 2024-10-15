# SNMP MIB module (Juniper-UNI-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-UNI-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:57 2024
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

juniperUni = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874)
)
juniperUni.setRevisions(
        ("2003-07-30 19:03",
         "2002-11-13 20:14",
         "2001-06-01 21:46",
         "2000-06-01 14:30",
         "2000-05-24 04:00",
         "1999-12-13 19:36",
         "1999-11-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniProducts_ObjectIdentity = ObjectIdentity
juniProducts = _JuniProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1)
)
_JuniperUniMibs_ObjectIdentity = ObjectIdentity
juniperUniMibs = _JuniperUniMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2)
)
if mibBuilder.loadTexts:
    juniperUniMibs.setStatus("current")
_UsVoiceMibs_ObjectIdentity = ObjectIdentity
usVoiceMibs = _UsVoiceMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 1)
)
_JuniMibs_ObjectIdentity = ObjectIdentity
juniMibs = _JuniMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2)
)
_JuniperUniExperiment_ObjectIdentity = ObjectIdentity
juniperUniExperiment = _JuniperUniExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3)
)
if mibBuilder.loadTexts:
    juniperUniExperiment.setStatus("current")
_UsVoiceExperiment_ObjectIdentity = ObjectIdentity
usVoiceExperiment = _UsVoiceExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 1)
)
_JuniExperiment_ObjectIdentity = ObjectIdentity
juniExperiment = _JuniExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2)
)
_JuniperUniAdmin_ObjectIdentity = ObjectIdentity
juniperUniAdmin = _JuniperUniAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4)
)
if mibBuilder.loadTexts:
    juniperUniAdmin.setStatus("current")
_UsVoiceAdmin_ObjectIdentity = ObjectIdentity
usVoiceAdmin = _UsVoiceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 1)
)
_JuniAdmin_ObjectIdentity = ObjectIdentity
juniAdmin = _JuniAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2)
)
_JuniAgentCapability_ObjectIdentity = ObjectIdentity
juniAgentCapability = _JuniAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5)
)
if mibBuilder.loadTexts:
    juniAgentCapability.setStatus("current")
_UsVoiceAgents_ObjectIdentity = ObjectIdentity
usVoiceAgents = _UsVoiceAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 1)
)
_JuniAgents_ObjectIdentity = ObjectIdentity
juniAgents = _JuniAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2)
)
_JuniNetMgmtProducts_ObjectIdentity = ObjectIdentity
juniNetMgmtProducts = _JuniNetMgmtProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 6)
)
if mibBuilder.loadTexts:
    juniNetMgmtProducts.setStatus("current")
_JuniSdxMibs_ObjectIdentity = ObjectIdentity
juniSdxMibs = _JuniSdxMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 6, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-UNI-SMI",
    **{"juniperUni": juniperUni,
       "juniProducts": juniProducts,
       "juniperUniMibs": juniperUniMibs,
       "usVoiceMibs": usVoiceMibs,
       "juniMibs": juniMibs,
       "juniperUniExperiment": juniperUniExperiment,
       "usVoiceExperiment": usVoiceExperiment,
       "juniExperiment": juniExperiment,
       "juniperUniAdmin": juniperUniAdmin,
       "usVoiceAdmin": usVoiceAdmin,
       "juniAdmin": juniAdmin,
       "juniAgentCapability": juniAgentCapability,
       "usVoiceAgents": usVoiceAgents,
       "juniAgents": juniAgents,
       "juniNetMgmtProducts": juniNetMgmtProducts,
       "juniSdxMibs": juniSdxMibs}
)
