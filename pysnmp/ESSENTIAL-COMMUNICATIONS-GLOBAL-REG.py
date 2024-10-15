# SNMP MIB module (ESSENTIAL-COMMUNICATIONS-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ESSENTIAL-COMMUNICATIONS-GLOBAL-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:51 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EssentialCommunications_ObjectIdentity = ObjectIdentity
essentialCommunications = _EssentialCommunications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159)
)
_EcRoot_ObjectIdentity = ObjectIdentity
ecRoot = _EcRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1)
)
_EcRegistration_ObjectIdentity = ObjectIdentity
ecRegistration = _EcRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 1)
)
_EcModules_ObjectIdentity = ObjectIdentity
ecModules = _EcModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 1, 1)
)
_EcNICReg_ObjectIdentity = ObjectIdentity
ecNICReg = _EcNICReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 1, 2)
)
_EcMICReg_ObjectIdentity = ObjectIdentity
ecMICReg = _EcMICReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 1, 3)
)
_PmicHIPPIReg_ObjectIdentity = ObjectIdentity
pmicHIPPIReg = _PmicHIPPIReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 1, 3, 1)
)
_SmicHIPPISWLReg_ObjectIdentity = ObjectIdentity
smicHIPPISWLReg = _SmicHIPPISWLReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 1, 3, 2)
)
_SmicHIPPILWLReg_ObjectIdentity = ObjectIdentity
smicHIPPILWLReg = _SmicHIPPILWLReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 1, 3, 3)
)
_EcSwitchReg_ObjectIdentity = ObjectIdentity
ecSwitchReg = _EcSwitchReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 1, 4)
)
_EcEPS16Reg_ObjectIdentity = ObjectIdentity
ecEPS16Reg = _EcEPS16Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 1, 4, 1)
)
_EcGeneric_ObjectIdentity = ObjectIdentity
ecGeneric = _EcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 2)
)
_EcProducts_ObjectIdentity = ObjectIdentity
ecProducts = _EcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 3)
)
_EcAgentProfiles_ObjectIdentity = ObjectIdentity
ecAgentProfiles = _EcAgentProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 4)
)
_EcRequirements_ObjectIdentity = ObjectIdentity
ecRequirements = _EcRequirements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 5)
)
_EcExperimental_ObjectIdentity = ObjectIdentity
ecExperimental = _EcExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2159, 1, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESSENTIAL-COMMUNICATIONS-GLOBAL-REG",
    **{"essentialCommunications": essentialCommunications,
       "ecRoot": ecRoot,
       "ecRegistration": ecRegistration,
       "ecModules": ecModules,
       "ecNICReg": ecNICReg,
       "ecMICReg": ecMICReg,
       "pmicHIPPIReg": pmicHIPPIReg,
       "smicHIPPISWLReg": smicHIPPISWLReg,
       "smicHIPPILWLReg": smicHIPPILWLReg,
       "ecSwitchReg": ecSwitchReg,
       "ecEPS16Reg": ecEPS16Reg,
       "ecGeneric": ecGeneric,
       "ecProducts": ecProducts,
       "ecAgentProfiles": ecAgentProfiles,
       "ecRequirements": ecRequirements,
       "ecExperimental": ecExperimental}
)
