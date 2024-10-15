# SNMP MIB module (MAIPU-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MAIPU-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:59 2024
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

maipu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651)
)
maipu.setRevisions(
        ("1901-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpProducts_ObjectIdentity = ObjectIdentity
mpProducts = _MpProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 1)
)
if mibBuilder.loadTexts:
    mpProducts.setStatus("current")
_MpTrapObject_ObjectIdentity = ObjectIdentity
mpTrapObject = _MpTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 2)
)
if mibBuilder.loadTexts:
    mpTrapObject.setStatus("current")
_MpMgmt_ObjectIdentity = ObjectIdentity
mpMgmt = _MpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3)
)
if mibBuilder.loadTexts:
    mpMgmt.setStatus("current")
_MpExperiment_ObjectIdentity = ObjectIdentity
mpExperiment = _MpExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 4)
)
if mibBuilder.loadTexts:
    mpExperiment.setStatus("current")
_MpSecurity_ObjectIdentity = ObjectIdentity
mpSecurity = _MpSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 5)
)
if mibBuilder.loadTexts:
    mpSecurity.setStatus("current")
_MpMgmt2_ObjectIdentity = ObjectIdentity
mpMgmt2 = _MpMgmt2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6)
)
if mibBuilder.loadTexts:
    mpMgmt2.setStatus("current")
_MpSystem_ObjectIdentity = ObjectIdentity
mpSystem = _MpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 1)
)
if mibBuilder.loadTexts:
    mpSystem.setStatus("current")
_MpRouterTech_ObjectIdentity = ObjectIdentity
mpRouterTech = _MpRouterTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 2)
)
if mibBuilder.loadTexts:
    mpRouterTech.setStatus("current")
_MpSwitchTech_ObjectIdentity = ObjectIdentity
mpSwitchTech = _MpSwitchTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 3)
)
if mibBuilder.loadTexts:
    mpSwitchTech.setStatus("current")
_MpVoipTech_ObjectIdentity = ObjectIdentity
mpVoipTech = _MpVoipTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 4)
)
if mibBuilder.loadTexts:
    mpVoipTech.setStatus("current")
_MpSecurityTech_ObjectIdentity = ObjectIdentity
mpSecurityTech = _MpSecurityTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 5)
)
if mibBuilder.loadTexts:
    mpSecurityTech.setStatus("current")
_MpApp_ObjectIdentity = ObjectIdentity
mpApp = _MpApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 6)
)
if mibBuilder.loadTexts:
    mpApp.setStatus("current")
_MpOtherSys_ObjectIdentity = ObjectIdentity
mpOtherSys = _MpOtherSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 6, 7)
)
if mibBuilder.loadTexts:
    mpOtherSys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-SMI",
    **{"maipu": maipu,
       "mpProducts": mpProducts,
       "mpTrapObject": mpTrapObject,
       "mpMgmt": mpMgmt,
       "mpExperiment": mpExperiment,
       "mpSecurity": mpSecurity,
       "mpMgmt2": mpMgmt2,
       "mpSystem": mpSystem,
       "mpRouterTech": mpRouterTech,
       "mpSwitchTech": mpSwitchTech,
       "mpVoipTech": mpVoipTech,
       "mpSecurityTech": mpSecurityTech,
       "mpApp": mpApp,
       "mpOtherSys": mpOtherSys}
)
