# SNMP MIB module (HPSVRMGMT-OID) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPSVRMGMT-OID
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:32 2024
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

hpEmbeddedServerMgt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7)
)
hpEmbeddedServerMgt.setRevisions(
        ("2007-07-09 00:00",
         "2010-04-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_HpSysMgt_ObjectIdentity = ObjectIdentity
hpSysMgt = _HpSysMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5)
)
_HpChassisMgmtProc_ObjectIdentity = ObjectIdentity
hpChassisMgmtProc = _HpChassisMgmtProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 1)
)
_HpBladeMgmtCard_ObjectIdentity = ObjectIdentity
hpBladeMgmtCard = _HpBladeMgmtCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hpBladeMgmtCard.setStatus("current")
_HpOnboardAdministrator_ObjectIdentity = ObjectIdentity
hpOnboardAdministrator = _HpOnboardAdministrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hpOnboardAdministrator.setStatus("current")
_HpBladeMgmtProc_ObjectIdentity = ObjectIdentity
hpBladeMgmtProc = _HpBladeMgmtProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 2)
)
_HpBHMgmtProc_ObjectIdentity = ObjectIdentity
hpBHMgmtProc = _HpBHMgmtProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hpBHMgmtProc.setStatus("current")
_HpServerMgmtProc_ObjectIdentity = ObjectIdentity
hpServerMgmtProc = _HpServerMgmtProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 3)
)
_HpServerGSP_ObjectIdentity = ObjectIdentity
hpServerGSP = _HpServerGSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 3, 1)
)
if mibBuilder.loadTexts:
    hpServerGSP.setStatus("current")
_HpServerMP_ObjectIdentity = ObjectIdentity
hpServerMP = _HpServerMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 3, 2)
)
if mibBuilder.loadTexts:
    hpServerMP.setStatus("current")
_HpServeriLO3_ObjectIdentity = ObjectIdentity
hpServeriLO3 = _HpServeriLO3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 3, 3)
)
if mibBuilder.loadTexts:
    hpServeriLO3.setStatus("current")
_HpPartitionSvrMgmtProc_ObjectIdentity = ObjectIdentity
hpPartitionSvrMgmtProc = _HpPartitionSvrMgmtProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 4)
)
_HpHiMPartGSP_ObjectIdentity = ObjectIdentity
hpHiMPartGSP = _HpHiMPartGSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 4, 1)
)
if mibBuilder.loadTexts:
    hpHiMPartGSP.setStatus("current")
_HpMidMPartMP_ObjectIdentity = ObjectIdentity
hpMidMPartMP = _HpMidMPartMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 4, 2)
)
if mibBuilder.loadTexts:
    hpMidMPartMP.setStatus("current")
_HpHiMPartArchMP_ObjectIdentity = ObjectIdentity
hpHiMPartArchMP = _HpHiMPartArchMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 4, 3)
)
if mibBuilder.loadTexts:
    hpHiMPartArchMP.setStatus("current")
_HpMidMPartArchMP_ObjectIdentity = ObjectIdentity
hpMidMPartArchMP = _HpMidMPartArchMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 4, 4)
)
if mibBuilder.loadTexts:
    hpMidMPartArchMP.setStatus("current")
_HpModuleMgmtProc_ObjectIdentity = ObjectIdentity
hpModuleMgmtProc = _HpModuleMgmtProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5)
)
_HpVCEthernetModule_ObjectIdentity = ObjectIdentity
hpVCEthernetModule = _HpVCEthernetModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 1)
)
if mibBuilder.loadTexts:
    hpVCEthernetModule.setStatus("current")
_HpVC10G24PortFlexFabricCmdr_ObjectIdentity = ObjectIdentity
hpVC10G24PortFlexFabricCmdr = _HpVC10G24PortFlexFabricCmdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 3)
)
if mibBuilder.loadTexts:
    hpVC10G24PortFlexFabricCmdr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPSVRMGMT-OID",
    **{"hp": hp,
       "hpSysMgt": hpSysMgt,
       "hpEmbeddedServerMgt": hpEmbeddedServerMgt,
       "hpChassisMgmtProc": hpChassisMgmtProc,
       "hpBladeMgmtCard": hpBladeMgmtCard,
       "hpOnboardAdministrator": hpOnboardAdministrator,
       "hpBladeMgmtProc": hpBladeMgmtProc,
       "hpBHMgmtProc": hpBHMgmtProc,
       "hpServerMgmtProc": hpServerMgmtProc,
       "hpServerGSP": hpServerGSP,
       "hpServerMP": hpServerMP,
       "hpServeriLO3": hpServeriLO3,
       "hpPartitionSvrMgmtProc": hpPartitionSvrMgmtProc,
       "hpHiMPartGSP": hpHiMPartGSP,
       "hpMidMPartMP": hpMidMPartMP,
       "hpHiMPartArchMP": hpHiMPartArchMP,
       "hpMidMPartArchMP": hpMidMPartArchMP,
       "hpModuleMgmtProc": hpModuleMgmtProc,
       "hpVCEthernetModule": hpVCEthernetModule,
       "hpVC10G24PortFlexFabricCmdr": hpVC10G24PortFlexFabricCmdr}
)
