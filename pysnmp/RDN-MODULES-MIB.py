# SNMP MIB module (RDN-MODULES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-MODULES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:09 2024
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

(rdnDefinitions,) = mibBuilder.importSymbols(
    "RDN-DEFINITIONS-MIB",
    "rdnDefinitions")

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

rdnModules = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4)
)
rdnModules.setRevisions(
        ("2008-08-08 00:00",
         "2003-11-05 00:00",
         "2003-04-29 00:00",
         "2001-04-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnModulesUnknown_ObjectIdentity = ObjectIdentity
rdnModulesUnknown = _RdnModulesUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 0)
)
if mibBuilder.loadTexts:
    rdnModulesUnknown.setStatus("current")
_RdnModulesSrm_ObjectIdentity = ObjectIdentity
rdnModulesSrm = _RdnModulesSrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 1)
)
if mibBuilder.loadTexts:
    rdnModulesSrm.setStatus("current")
_RdnModulesCmts_ObjectIdentity = ObjectIdentity
rdnModulesCmts = _RdnModulesCmts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 2)
)
if mibBuilder.loadTexts:
    rdnModulesCmts.setStatus("current")
_RdnModulesHsim2_ObjectIdentity = ObjectIdentity
rdnModulesHsim2 = _RdnModulesHsim2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 3)
)
if mibBuilder.loadTexts:
    rdnModulesHsim2.setStatus("current")
_RdnModulesHsim2PosEth_ObjectIdentity = ObjectIdentity
rdnModulesHsim2PosEth = _RdnModulesHsim2PosEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 4)
)
if mibBuilder.loadTexts:
    rdnModulesHsim2PosEth.setStatus("current")
_RdnModulesHsim2Pos2_ObjectIdentity = ObjectIdentity
rdnModulesHsim2Pos2 = _RdnModulesHsim2Pos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 5)
)
if mibBuilder.loadTexts:
    rdnModulesHsim2Pos2.setStatus("current")
_RdnModulesHsim2PosOc48_ObjectIdentity = ObjectIdentity
rdnModulesHsim2PosOc48 = _RdnModulesHsim2PosOc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 6)
)
if mibBuilder.loadTexts:
    rdnModulesHsim2PosOc48.setStatus("current")
_RdnModulesHsim2PosDoc48_ObjectIdentity = ObjectIdentity
rdnModulesHsim2PosDoc48 = _RdnModulesHsim2PosDoc48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 7)
)
if mibBuilder.loadTexts:
    rdnModulesHsim2PosDoc48.setStatus("current")
_RdnModulesHsim2PosAtm_ObjectIdentity = ObjectIdentity
rdnModulesHsim2PosAtm = _RdnModulesHsim2PosAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 8)
)
if mibBuilder.loadTexts:
    rdnModulesHsim2PosAtm.setStatus("current")
_RdnModulesHsim2Eth8_ObjectIdentity = ObjectIdentity
rdnModulesHsim2Eth8 = _RdnModulesHsim2Eth8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 9)
)
if mibBuilder.loadTexts:
    rdnModulesHsim2Eth8.setStatus("current")
_RdnModulesHsim2Gige_ObjectIdentity = ObjectIdentity
rdnModulesHsim2Gige = _RdnModulesHsim2Gige_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 10)
)
if mibBuilder.loadTexts:
    rdnModulesHsim2Gige.setStatus("current")
_RdnModulesOsr_ObjectIdentity = ObjectIdentity
rdnModulesOsr = _RdnModulesOsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 11)
)
if mibBuilder.loadTexts:
    rdnModulesOsr.setStatus("current")
_RdnModulesBsr1000_ObjectIdentity = ObjectIdentity
rdnModulesBsr1000 = _RdnModulesBsr1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 12)
)
if mibBuilder.loadTexts:
    rdnModulesBsr1000.setStatus("current")
_RdnModulesHsim2GigeMM_ObjectIdentity = ObjectIdentity
rdnModulesHsim2GigeMM = _RdnModulesHsim2GigeMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 13)
)
if mibBuilder.loadTexts:
    rdnModulesHsim2GigeMM.setStatus("current")
_RdnModulesHsim4GigeEth8_ObjectIdentity = ObjectIdentity
rdnModulesHsim4GigeEth8 = _RdnModulesHsim4GigeEth8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 4, 15)
)
if mibBuilder.loadTexts:
    rdnModulesHsim4GigeEth8.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-MODULES-MIB",
    **{"rdnModules": rdnModules,
       "rdnModulesUnknown": rdnModulesUnknown,
       "rdnModulesSrm": rdnModulesSrm,
       "rdnModulesCmts": rdnModulesCmts,
       "rdnModulesHsim2": rdnModulesHsim2,
       "rdnModulesHsim2PosEth": rdnModulesHsim2PosEth,
       "rdnModulesHsim2Pos2": rdnModulesHsim2Pos2,
       "rdnModulesHsim2PosOc48": rdnModulesHsim2PosOc48,
       "rdnModulesHsim2PosDoc48": rdnModulesHsim2PosDoc48,
       "rdnModulesHsim2PosAtm": rdnModulesHsim2PosAtm,
       "rdnModulesHsim2Eth8": rdnModulesHsim2Eth8,
       "rdnModulesHsim2Gige": rdnModulesHsim2Gige,
       "rdnModulesOsr": rdnModulesOsr,
       "rdnModulesBsr1000": rdnModulesBsr1000,
       "rdnModulesHsim2GigeMM": rdnModulesHsim2GigeMM,
       "rdnModulesHsim4GigeEth8": rdnModulesHsim4GigeEth8}
)
