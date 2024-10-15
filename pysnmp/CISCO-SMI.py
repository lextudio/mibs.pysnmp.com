# SNMP MIB module (CISCO-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:00 2024
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

cisco = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9)
)
cisco.setRevisions(
        ("2016-01-15 00:00",
         "2012-08-29 00:00",
         "2009-02-03 00:00",
         "2002-03-21 00:00",
         "2001-05-22 00:00",
         "2000-11-01 22:46",
         "2000-01-11 00:00",
         "1997-04-09 00:00",
         "1995-05-16 00:00",
         "1994-04-26 20:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoProducts_ObjectIdentity = ObjectIdentity
ciscoProducts = _CiscoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ciscoProducts.setStatus("current")
_Local_ObjectIdentity = ObjectIdentity
local = _Local_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2)
)
if mibBuilder.loadTexts:
    local.setStatus("current")
_Temporary_ObjectIdentity = ObjectIdentity
temporary = _Temporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3)
)
if mibBuilder.loadTexts:
    temporary.setStatus("current")
_Pakmon_ObjectIdentity = ObjectIdentity
pakmon = _Pakmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 4)
)
if mibBuilder.loadTexts:
    pakmon.setStatus("current")
_Workgroup_ObjectIdentity = ObjectIdentity
workgroup = _Workgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5)
)
if mibBuilder.loadTexts:
    workgroup.setStatus("current")
_OtherEnterprises_ObjectIdentity = ObjectIdentity
otherEnterprises = _OtherEnterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6)
)
if mibBuilder.loadTexts:
    otherEnterprises.setStatus("current")
_CiscoSB_ObjectIdentity = ObjectIdentity
ciscoSB = _CiscoSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1)
)
if mibBuilder.loadTexts:
    ciscoSB.setStatus("current")
_CiscoSMB_ObjectIdentity = ObjectIdentity
ciscoSMB = _CiscoSMB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 2)
)
if mibBuilder.loadTexts:
    ciscoSMB.setStatus("current")
_CiscoAgentCapability_ObjectIdentity = ObjectIdentity
ciscoAgentCapability = _CiscoAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7)
)
if mibBuilder.loadTexts:
    ciscoAgentCapability.setStatus("current")
_CiscoConfig_ObjectIdentity = ObjectIdentity
ciscoConfig = _CiscoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 8)
)
if mibBuilder.loadTexts:
    ciscoConfig.setStatus("current")
_CiscoMgmt_ObjectIdentity = ObjectIdentity
ciscoMgmt = _CiscoMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9)
)
if mibBuilder.loadTexts:
    ciscoMgmt.setStatus("current")
_CiscoExperiment_ObjectIdentity = ObjectIdentity
ciscoExperiment = _CiscoExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10)
)
if mibBuilder.loadTexts:
    ciscoExperiment.setStatus("current")
_CiscoAdmin_ObjectIdentity = ObjectIdentity
ciscoAdmin = _CiscoAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11)
)
if mibBuilder.loadTexts:
    ciscoAdmin.setStatus("current")
_CiscoProxy_ObjectIdentity = ObjectIdentity
ciscoProxy = _CiscoProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 1)
)
if mibBuilder.loadTexts:
    ciscoProxy.setStatus("current")
_CiscoPartyProxy_ObjectIdentity = ObjectIdentity
ciscoPartyProxy = _CiscoPartyProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 1, 1)
)
_CiscoContextProxy_ObjectIdentity = ObjectIdentity
ciscoContextProxy = _CiscoContextProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 1, 2)
)
_CiscoRptrGroupObjectID_ObjectIdentity = ObjectIdentity
ciscoRptrGroupObjectID = _CiscoRptrGroupObjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 2)
)
if mibBuilder.loadTexts:
    ciscoRptrGroupObjectID.setStatus("current")
_CiscoUnknownRptrGroup_ObjectIdentity = ObjectIdentity
ciscoUnknownRptrGroup = _CiscoUnknownRptrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoUnknownRptrGroup.setStatus("current")
_Cisco2505RptrGroup_ObjectIdentity = ObjectIdentity
cisco2505RptrGroup = _Cisco2505RptrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 2, 2)
)
if mibBuilder.loadTexts:
    cisco2505RptrGroup.setStatus("current")
_Cisco2507RptrGroup_ObjectIdentity = ObjectIdentity
cisco2507RptrGroup = _Cisco2507RptrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 2, 3)
)
if mibBuilder.loadTexts:
    cisco2507RptrGroup.setStatus("current")
_Cisco2516RptrGroup_ObjectIdentity = ObjectIdentity
cisco2516RptrGroup = _Cisco2516RptrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 2, 4)
)
if mibBuilder.loadTexts:
    cisco2516RptrGroup.setStatus("current")
_CiscoWsx5020RptrGroup_ObjectIdentity = ObjectIdentity
ciscoWsx5020RptrGroup = _CiscoWsx5020RptrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 2, 5)
)
if mibBuilder.loadTexts:
    ciscoWsx5020RptrGroup.setStatus("current")
_CiscoChipSets_ObjectIdentity = ObjectIdentity
ciscoChipSets = _CiscoChipSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 3)
)
if mibBuilder.loadTexts:
    ciscoChipSets.setStatus("current")
_CiscoChipSetSaint1_ObjectIdentity = ObjectIdentity
ciscoChipSetSaint1 = _CiscoChipSetSaint1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoChipSetSaint1.setStatus("current")
_CiscoChipSetSaint2_ObjectIdentity = ObjectIdentity
ciscoChipSetSaint2 = _CiscoChipSetSaint2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 3, 2)
)
if mibBuilder.loadTexts:
    ciscoChipSetSaint2.setStatus("current")
_CiscoChipSetSaint3_ObjectIdentity = ObjectIdentity
ciscoChipSetSaint3 = _CiscoChipSetSaint3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 3, 3)
)
if mibBuilder.loadTexts:
    ciscoChipSetSaint3.setStatus("current")
_CiscoChipSetSaint4_ObjectIdentity = ObjectIdentity
ciscoChipSetSaint4 = _CiscoChipSetSaint4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 11, 3, 4)
)
if mibBuilder.loadTexts:
    ciscoChipSetSaint4.setStatus("current")
_CiscoModules_ObjectIdentity = ObjectIdentity
ciscoModules = _CiscoModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12)
)
if mibBuilder.loadTexts:
    ciscoModules.setStatus("current")
_Lightstream_ObjectIdentity = ObjectIdentity
lightstream = _Lightstream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 13)
)
if mibBuilder.loadTexts:
    lightstream.setStatus("current")
_Ciscoworks_ObjectIdentity = ObjectIdentity
ciscoworks = _Ciscoworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 14)
)
if mibBuilder.loadTexts:
    ciscoworks.setStatus("current")
_Newport_ObjectIdentity = ObjectIdentity
newport = _Newport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 15)
)
if mibBuilder.loadTexts:
    newport.setStatus("current")
_CiscoPartnerProducts_ObjectIdentity = ObjectIdentity
ciscoPartnerProducts = _CiscoPartnerProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 16)
)
if mibBuilder.loadTexts:
    ciscoPartnerProducts.setStatus("current")
_CiscoPolicy_ObjectIdentity = ObjectIdentity
ciscoPolicy = _CiscoPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 17)
)
if mibBuilder.loadTexts:
    ciscoPolicy.setStatus("current")
_CiscoPIB_ObjectIdentity = ObjectIdentity
ciscoPIB = _CiscoPIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 17, 2)
)
if mibBuilder.loadTexts:
    ciscoPIB.setStatus("current")
_CiscoPolicyAuto_ObjectIdentity = ObjectIdentity
ciscoPolicyAuto = _CiscoPolicyAuto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 18)
)
if mibBuilder.loadTexts:
    ciscoPolicyAuto.setStatus("current")
_CiscoPibToMib_ObjectIdentity = ObjectIdentity
ciscoPibToMib = _CiscoPibToMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 18, 2)
)
if mibBuilder.loadTexts:
    ciscoPibToMib.setStatus("current")
_CiscoDomains_ObjectIdentity = ObjectIdentity
ciscoDomains = _CiscoDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19)
)
if mibBuilder.loadTexts:
    ciscoDomains.setStatus("current")
_CiscoTDomains_ObjectIdentity = ObjectIdentity
ciscoTDomains = _CiscoTDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999)
)
_CiscoTDomainUdpIpv4_ObjectIdentity = ObjectIdentity
ciscoTDomainUdpIpv4 = _CiscoTDomainUdpIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 1)
)
if mibBuilder.loadTexts:
    ciscoTDomainUdpIpv4.setStatus("current")
_CiscoTDomainUdpIpv6_ObjectIdentity = ObjectIdentity
ciscoTDomainUdpIpv6 = _CiscoTDomainUdpIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 2)
)
if mibBuilder.loadTexts:
    ciscoTDomainUdpIpv6.setStatus("current")
_CiscoTDomainTcpIpv4_ObjectIdentity = ObjectIdentity
ciscoTDomainTcpIpv4 = _CiscoTDomainTcpIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 3)
)
if mibBuilder.loadTexts:
    ciscoTDomainTcpIpv4.setStatus("current")
_CiscoTDomainTcpIpv6_ObjectIdentity = ObjectIdentity
ciscoTDomainTcpIpv6 = _CiscoTDomainTcpIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 4)
)
if mibBuilder.loadTexts:
    ciscoTDomainTcpIpv6.setStatus("current")
_CiscoTDomainLocal_ObjectIdentity = ObjectIdentity
ciscoTDomainLocal = _CiscoTDomainLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 5)
)
if mibBuilder.loadTexts:
    ciscoTDomainLocal.setStatus("current")
_CiscoTDomainClns_ObjectIdentity = ObjectIdentity
ciscoTDomainClns = _CiscoTDomainClns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 6)
)
if mibBuilder.loadTexts:
    ciscoTDomainClns.setStatus("current")
_CiscoTDomainCons_ObjectIdentity = ObjectIdentity
ciscoTDomainCons = _CiscoTDomainCons_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 7)
)
if mibBuilder.loadTexts:
    ciscoTDomainCons.setStatus("current")
_CiscoTDomainDdp_ObjectIdentity = ObjectIdentity
ciscoTDomainDdp = _CiscoTDomainDdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 8)
)
if mibBuilder.loadTexts:
    ciscoTDomainDdp.setStatus("current")
_CiscoTDomainIpx_ObjectIdentity = ObjectIdentity
ciscoTDomainIpx = _CiscoTDomainIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 9)
)
if mibBuilder.loadTexts:
    ciscoTDomainIpx.setStatus("current")
_CiscoTDomainSctpIpv4_ObjectIdentity = ObjectIdentity
ciscoTDomainSctpIpv4 = _CiscoTDomainSctpIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 10)
)
if mibBuilder.loadTexts:
    ciscoTDomainSctpIpv4.setStatus("current")
_CiscoTDomainSctpIpv6_ObjectIdentity = ObjectIdentity
ciscoTDomainSctpIpv6 = _CiscoTDomainSctpIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 19, 99999, 11)
)
if mibBuilder.loadTexts:
    ciscoTDomainSctpIpv6.setStatus("current")
_CiscoCIB_ObjectIdentity = ObjectIdentity
ciscoCIB = _CiscoCIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 20)
)
if mibBuilder.loadTexts:
    ciscoCIB.setStatus("current")
_CiscoCibMmiGroup_ObjectIdentity = ObjectIdentity
ciscoCibMmiGroup = _CiscoCibMmiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 20, 1)
)
if mibBuilder.loadTexts:
    ciscoCibMmiGroup.setStatus("current")
_CiscoCibProvGroup_ObjectIdentity = ObjectIdentity
ciscoCibProvGroup = _CiscoCibProvGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 20, 2)
)
if mibBuilder.loadTexts:
    ciscoCibProvGroup.setStatus("current")
_CiscoPKI_ObjectIdentity = ObjectIdentity
ciscoPKI = _CiscoPKI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 21)
)
if mibBuilder.loadTexts:
    ciscoPKI.setStatus("current")
_CiscoLDAP_ObjectIdentity = ObjectIdentity
ciscoLDAP = _CiscoLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 22)
)
if mibBuilder.loadTexts:
    ciscoLDAP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SMI",
    **{"cisco": cisco,
       "ciscoProducts": ciscoProducts,
       "local": local,
       "temporary": temporary,
       "pakmon": pakmon,
       "workgroup": workgroup,
       "otherEnterprises": otherEnterprises,
       "ciscoSB": ciscoSB,
       "ciscoSMB": ciscoSMB,
       "ciscoAgentCapability": ciscoAgentCapability,
       "ciscoConfig": ciscoConfig,
       "ciscoMgmt": ciscoMgmt,
       "ciscoExperiment": ciscoExperiment,
       "ciscoAdmin": ciscoAdmin,
       "ciscoProxy": ciscoProxy,
       "ciscoPartyProxy": ciscoPartyProxy,
       "ciscoContextProxy": ciscoContextProxy,
       "ciscoRptrGroupObjectID": ciscoRptrGroupObjectID,
       "ciscoUnknownRptrGroup": ciscoUnknownRptrGroup,
       "cisco2505RptrGroup": cisco2505RptrGroup,
       "cisco2507RptrGroup": cisco2507RptrGroup,
       "cisco2516RptrGroup": cisco2516RptrGroup,
       "ciscoWsx5020RptrGroup": ciscoWsx5020RptrGroup,
       "ciscoChipSets": ciscoChipSets,
       "ciscoChipSetSaint1": ciscoChipSetSaint1,
       "ciscoChipSetSaint2": ciscoChipSetSaint2,
       "ciscoChipSetSaint3": ciscoChipSetSaint3,
       "ciscoChipSetSaint4": ciscoChipSetSaint4,
       "ciscoModules": ciscoModules,
       "lightstream": lightstream,
       "ciscoworks": ciscoworks,
       "newport": newport,
       "ciscoPartnerProducts": ciscoPartnerProducts,
       "ciscoPolicy": ciscoPolicy,
       "ciscoPIB": ciscoPIB,
       "ciscoPolicyAuto": ciscoPolicyAuto,
       "ciscoPibToMib": ciscoPibToMib,
       "ciscoDomains": ciscoDomains,
       "ciscoTDomains": ciscoTDomains,
       "ciscoTDomainUdpIpv4": ciscoTDomainUdpIpv4,
       "ciscoTDomainUdpIpv6": ciscoTDomainUdpIpv6,
       "ciscoTDomainTcpIpv4": ciscoTDomainTcpIpv4,
       "ciscoTDomainTcpIpv6": ciscoTDomainTcpIpv6,
       "ciscoTDomainLocal": ciscoTDomainLocal,
       "ciscoTDomainClns": ciscoTDomainClns,
       "ciscoTDomainCons": ciscoTDomainCons,
       "ciscoTDomainDdp": ciscoTDomainDdp,
       "ciscoTDomainIpx": ciscoTDomainIpx,
       "ciscoTDomainSctpIpv4": ciscoTDomainSctpIpv4,
       "ciscoTDomainSctpIpv6": ciscoTDomainSctpIpv6,
       "ciscoCIB": ciscoCIB,
       "ciscoCibMmiGroup": ciscoCibMmiGroup,
       "ciscoCibProvGroup": ciscoCibProvGroup,
       "ciscoPKI": ciscoPKI,
       "ciscoLDAP": ciscoLDAP}
)
