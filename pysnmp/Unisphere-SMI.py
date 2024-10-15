# SNMP MIB module (Unisphere-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:59 2024
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

unisphere = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874)
)
unisphere.setRevisions(
        ("2001-06-01 21:46",
         "2000-06-01 14:30",
         "2000-05-24 04:00",
         "1999-12-13 19:36",
         "1999-11-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsProducts_ObjectIdentity = ObjectIdentity
usProducts = _UsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 1)
)
_UsMibs_ObjectIdentity = ObjectIdentity
usMibs = _UsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2)
)
_UsVoiceMibs_ObjectIdentity = ObjectIdentity
usVoiceMibs = _UsVoiceMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 1)
)
_UsDataMibs_ObjectIdentity = ObjectIdentity
usDataMibs = _UsDataMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2)
)
_UsExperiment_ObjectIdentity = ObjectIdentity
usExperiment = _UsExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3)
)
_UsVoiceExperiment_ObjectIdentity = ObjectIdentity
usVoiceExperiment = _UsVoiceExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 1)
)
_UsDataExperiment_ObjectIdentity = ObjectIdentity
usDataExperiment = _UsDataExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2)
)
_UsAdmin_ObjectIdentity = ObjectIdentity
usAdmin = _UsAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4)
)
_UsVoiceAdmin_ObjectIdentity = ObjectIdentity
usVoiceAdmin = _UsVoiceAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 1)
)
_UsDataAdmin_ObjectIdentity = ObjectIdentity
usDataAdmin = _UsDataAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 4, 2)
)
_UsAgentCapability_ObjectIdentity = ObjectIdentity
usAgentCapability = _UsAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5)
)
_UsVoiceAgents_ObjectIdentity = ObjectIdentity
usVoiceAgents = _UsVoiceAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 1)
)
_UsDataAgents_ObjectIdentity = ObjectIdentity
usDataAgents = _UsDataAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2)
)
_UsNetMgmtProducts_ObjectIdentity = ObjectIdentity
usNetMgmtProducts = _UsNetMgmtProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 6)
)
_UsUmcMib_ObjectIdentity = ObjectIdentity
usUmcMib = _UsUmcMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 6, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-SMI",
    **{"unisphere": unisphere,
       "usProducts": usProducts,
       "usMibs": usMibs,
       "usVoiceMibs": usVoiceMibs,
       "usDataMibs": usDataMibs,
       "usExperiment": usExperiment,
       "usVoiceExperiment": usVoiceExperiment,
       "usDataExperiment": usDataExperiment,
       "usAdmin": usAdmin,
       "usVoiceAdmin": usVoiceAdmin,
       "usDataAdmin": usDataAdmin,
       "usAgentCapability": usAgentCapability,
       "usVoiceAgents": usVoiceAgents,
       "usDataAgents": usDataAgents,
       "usNetMgmtProducts": usNetMgmtProducts,
       "usUmcMib": usUmcMib}
)
