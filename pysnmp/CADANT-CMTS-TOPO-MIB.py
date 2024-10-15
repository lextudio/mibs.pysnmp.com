# SNMP MIB module (CADANT-CMTS-TOPO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-TOPO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:53 2024
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

(cadIfMacDomainIfIndex,) = mibBuilder.importSymbols(
    "CADANT-CMTS-LAYER2CMTS-MIB",
    "cadIfMacDomainIfIndex")

(cadTopology,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadTopology")

(PrimaryState,) = mibBuilder.importSymbols(
    "CADANT-TC",
    "PrimaryState")

(clabTopoFiberNodeCfgEntry,
 clabTopoFiberNodeCfgNodeName) = mibBuilder.importSymbols(
    "CLAB-TOPO-MIB",
    "clabTopoFiberNodeCfgEntry",
    "clabTopoFiberNodeCfgNodeName")

(ChSetId,
 IfDirection,
 docsIf3DsChSetEntry,
 docsIf3MdNodeStatusEntry,
 docsIf3UsChSetEntry) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "ChSetId",
    "IfDirection",
    "docsIf3DsChSetEntry",
    "docsIf3MdNodeStatusEntry",
    "docsIf3UsChSetEntry")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

cadTopologyMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1)
)
cadTopologyMib.setRevisions(
        ("2014-02-24 00:00",
         "2008-08-14 00:00",
         "2008-04-09 00:00",
         "2007-06-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadTopologyMibObjects_ObjectIdentity = ObjectIdentity
cadTopologyMibObjects = _CadTopologyMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1)
)
_CadFiberNodeStatusTable_Object = MibTable
cadFiberNodeStatusTable = _CadFiberNodeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cadFiberNodeStatusTable.setStatus("current")
_CadFiberNodeStatusEntry_Object = MibTableRow
cadFiberNodeStatusEntry = _CadFiberNodeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cadFiberNodeStatusEntry.setStatus("current")
_CadFiberNodeOperStatus_Type = PrimaryState
_CadFiberNodeOperStatus_Object = MibTableColumn
cadFiberNodeOperStatus = _CadFiberNodeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 1),
    _CadFiberNodeOperStatus_Type()
)
cadFiberNodeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeOperStatus.setStatus("current")
_CadFiberNodeNumOther_Type = Integer32
_CadFiberNodeNumOther_Object = MibTableColumn
cadFiberNodeNumOther = _CadFiberNodeNumOther_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 11),
    _CadFiberNodeNumOther_Type()
)
cadFiberNodeNumOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumOther.setStatus("deprecated")
_CadFiberNodeNumInitRanging_Type = Integer32
_CadFiberNodeNumInitRanging_Object = MibTableColumn
cadFiberNodeNumInitRanging = _CadFiberNodeNumInitRanging_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 12),
    _CadFiberNodeNumInitRanging_Type()
)
cadFiberNodeNumInitRanging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumInitRanging.setStatus("deprecated")
_CadFiberNodeNumRangingComplete_Type = Integer32
_CadFiberNodeNumRangingComplete_Object = MibTableColumn
cadFiberNodeNumRangingComplete = _CadFiberNodeNumRangingComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 13),
    _CadFiberNodeNumRangingComplete_Type()
)
cadFiberNodeNumRangingComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumRangingComplete.setStatus("deprecated")
_CadFiberNodeNumStartEae_Type = Integer32
_CadFiberNodeNumStartEae_Object = MibTableColumn
cadFiberNodeNumStartEae = _CadFiberNodeNumStartEae_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 14),
    _CadFiberNodeNumStartEae_Type()
)
cadFiberNodeNumStartEae.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumStartEae.setStatus("deprecated")
_CadFiberNodeNumStartDhcpv4_Type = Integer32
_CadFiberNodeNumStartDhcpv4_Object = MibTableColumn
cadFiberNodeNumStartDhcpv4 = _CadFiberNodeNumStartDhcpv4_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 15),
    _CadFiberNodeNumStartDhcpv4_Type()
)
cadFiberNodeNumStartDhcpv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumStartDhcpv4.setStatus("deprecated")
_CadFiberNodeNumStartDhcpv6_Type = Integer32
_CadFiberNodeNumStartDhcpv6_Object = MibTableColumn
cadFiberNodeNumStartDhcpv6 = _CadFiberNodeNumStartDhcpv6_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 16),
    _CadFiberNodeNumStartDhcpv6_Type()
)
cadFiberNodeNumStartDhcpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumStartDhcpv6.setStatus("deprecated")
_CadFiberNodeNumDhcpv4Complete_Type = Integer32
_CadFiberNodeNumDhcpv4Complete_Object = MibTableColumn
cadFiberNodeNumDhcpv4Complete = _CadFiberNodeNumDhcpv4Complete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 17),
    _CadFiberNodeNumDhcpv4Complete_Type()
)
cadFiberNodeNumDhcpv4Complete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumDhcpv4Complete.setStatus("deprecated")
_CadFiberNodeNumDhcpv6Complete_Type = Integer32
_CadFiberNodeNumDhcpv6Complete_Object = MibTableColumn
cadFiberNodeNumDhcpv6Complete = _CadFiberNodeNumDhcpv6Complete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 18),
    _CadFiberNodeNumDhcpv6Complete_Type()
)
cadFiberNodeNumDhcpv6Complete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumDhcpv6Complete.setStatus("deprecated")
_CadFiberNodeNumStartCfgFileDownload_Type = Integer32
_CadFiberNodeNumStartCfgFileDownload_Object = MibTableColumn
cadFiberNodeNumStartCfgFileDownload = _CadFiberNodeNumStartCfgFileDownload_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 19),
    _CadFiberNodeNumStartCfgFileDownload_Type()
)
cadFiberNodeNumStartCfgFileDownload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumStartCfgFileDownload.setStatus("deprecated")
_CadFiberNodeNumCfgFileDownloadComplete_Type = Integer32
_CadFiberNodeNumCfgFileDownloadComplete_Object = MibTableColumn
cadFiberNodeNumCfgFileDownloadComplete = _CadFiberNodeNumCfgFileDownloadComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 20),
    _CadFiberNodeNumCfgFileDownloadComplete_Type()
)
cadFiberNodeNumCfgFileDownloadComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumCfgFileDownloadComplete.setStatus("deprecated")
_CadFiberNodeNumStartRegistration_Type = Integer32
_CadFiberNodeNumStartRegistration_Object = MibTableColumn
cadFiberNodeNumStartRegistration = _CadFiberNodeNumStartRegistration_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 21),
    _CadFiberNodeNumStartRegistration_Type()
)
cadFiberNodeNumStartRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumStartRegistration.setStatus("deprecated")
_CadFiberNodeNumRegistrationComplete_Type = Integer32
_CadFiberNodeNumRegistrationComplete_Object = MibTableColumn
cadFiberNodeNumRegistrationComplete = _CadFiberNodeNumRegistrationComplete_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 22),
    _CadFiberNodeNumRegistrationComplete_Type()
)
cadFiberNodeNumRegistrationComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumRegistrationComplete.setStatus("deprecated")
_CadFiberNodeNumOperational_Type = Integer32
_CadFiberNodeNumOperational_Object = MibTableColumn
cadFiberNodeNumOperational = _CadFiberNodeNumOperational_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 23),
    _CadFiberNodeNumOperational_Type()
)
cadFiberNodeNumOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumOperational.setStatus("deprecated")
_CadFiberNodeNumBpiInit_Type = Integer32
_CadFiberNodeNumBpiInit_Object = MibTableColumn
cadFiberNodeNumBpiInit = _CadFiberNodeNumBpiInit_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 24),
    _CadFiberNodeNumBpiInit_Type()
)
cadFiberNodeNumBpiInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumBpiInit.setStatus("deprecated")
_CadFiberNodeNumForwardingDisabled_Type = Integer32
_CadFiberNodeNumForwardingDisabled_Object = MibTableColumn
cadFiberNodeNumForwardingDisabled = _CadFiberNodeNumForwardingDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 25),
    _CadFiberNodeNumForwardingDisabled_Type()
)
cadFiberNodeNumForwardingDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumForwardingDisabled.setStatus("deprecated")
_CadFiberNodeNumRfMuteAll_Type = Integer32
_CadFiberNodeNumRfMuteAll_Object = MibTableColumn
cadFiberNodeNumRfMuteAll = _CadFiberNodeNumRfMuteAll_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 26),
    _CadFiberNodeNumRfMuteAll_Type()
)
cadFiberNodeNumRfMuteAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumRfMuteAll.setStatus("deprecated")
_CadFiberNodeNumTotal_Type = Integer32
_CadFiberNodeNumTotal_Object = MibTableColumn
cadFiberNodeNumTotal = _CadFiberNodeNumTotal_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 27),
    _CadFiberNodeNumTotal_Type()
)
cadFiberNodeNumTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumTotal.setStatus("deprecated")
_CadFiberNodeNumRangingAborted_Type = Integer32
_CadFiberNodeNumRangingAborted_Object = MibTableColumn
cadFiberNodeNumRangingAborted = _CadFiberNodeNumRangingAborted_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 28),
    _CadFiberNodeNumRangingAborted_Type()
)
cadFiberNodeNumRangingAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumRangingAborted.setStatus("deprecated")
_CadFiberNodeNumRangFlaps_Type = Integer32
_CadFiberNodeNumRangFlaps_Object = MibTableColumn
cadFiberNodeNumRangFlaps = _CadFiberNodeNumRangFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 29),
    _CadFiberNodeNumRangFlaps_Type()
)
cadFiberNodeNumRangFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumRangFlaps.setStatus("deprecated")
_CadFiberNodeNumProvFlaps_Type = Integer32
_CadFiberNodeNumProvFlaps_Object = MibTableColumn
cadFiberNodeNumProvFlaps = _CadFiberNodeNumProvFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 30),
    _CadFiberNodeNumProvFlaps_Type()
)
cadFiberNodeNumProvFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumProvFlaps.setStatus("deprecated")
_CadFiberNodeNumRegFlaps_Type = Integer32
_CadFiberNodeNumRegFlaps_Object = MibTableColumn
cadFiberNodeNumRegFlaps = _CadFiberNodeNumRegFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 1, 1, 31),
    _CadFiberNodeNumRegFlaps_Type()
)
cadFiberNodeNumRegFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadFiberNodeNumRegFlaps.setStatus("deprecated")
_CadChlFnTable_Object = MibTable
cadChlFnTable = _CadChlFnTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cadChlFnTable.setStatus("current")
_CadChlFnEntry_Object = MibTableRow
cadChlFnEntry = _CadChlFnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 2, 1)
)
cadChlFnEntry.setIndexNames(
    (0, "CADANT-CMTS-LAYER2CMTS-MIB", "cadIfMacDomainIfIndex"),
    (0, "CLAB-TOPO-MIB", "clabTopoFiberNodeCfgNodeName"),
    (0, "CADANT-CMTS-TOPO-MIB", "cadChlIfIndex"),
)
if mibBuilder.loadTexts:
    cadChlFnEntry.setStatus("current")
_CadChlIfIndex_Type = InterfaceIndex
_CadChlIfIndex_Object = MibTableColumn
cadChlIfIndex = _CadChlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 2, 1, 1),
    _CadChlIfIndex_Type()
)
cadChlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadChlIfIndex.setStatus("current")
_CadChlFnIfDirection_Type = IfDirection
_CadChlFnIfDirection_Object = MibTableColumn
cadChlFnIfDirection = _CadChlFnIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 2, 1, 2),
    _CadChlFnIfDirection_Type()
)
cadChlFnIfDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadChlFnIfDirection.setStatus("current")


class _CadChlFnMdUsOrDsSgId_Type(Unsigned32):
    """Custom type cadChlFnMdUsOrDsSgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadChlFnMdUsOrDsSgId_Type.__name__ = "Unsigned32"
_CadChlFnMdUsOrDsSgId_Object = MibTableColumn
cadChlFnMdUsOrDsSgId = _CadChlFnMdUsOrDsSgId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 2, 1, 3),
    _CadChlFnMdUsOrDsSgId_Type()
)
cadChlFnMdUsOrDsSgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadChlFnMdUsOrDsSgId.setStatus("current")
_CadChlFnUsOrDsPhysChlIfIndex_Type = InterfaceIndexOrZero
_CadChlFnUsOrDsPhysChlIfIndex_Object = MibTableColumn
cadChlFnUsOrDsPhysChlIfIndex = _CadChlFnUsOrDsPhysChlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 2, 1, 4),
    _CadChlFnUsOrDsPhysChlIfIndex_Type()
)
cadChlFnUsOrDsPhysChlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadChlFnUsOrDsPhysChlIfIndex.setStatus("current")


class _CadChlFnChlId_Type(Unsigned32):
    """Custom type cadChlFnChlId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadChlFnChlId_Type.__name__ = "Unsigned32"
_CadChlFnChlId_Object = MibTableColumn
cadChlFnChlId = _CadChlFnChlId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 105, 1, 1, 2, 1, 5),
    _CadChlFnChlId_Type()
)
cadChlFnChlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadChlFnChlId.setStatus("current")
clabTopoFiberNodeCfgEntry.registerAugmentions(
    ("CADANT-CMTS-TOPO-MIB",
     "cadFiberNodeStatusEntry")
)
cadFiberNodeStatusEntry.setIndexNames(*clabTopoFiberNodeCfgEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-TOPO-MIB",
    **{"cadTopologyMib": cadTopologyMib,
       "cadTopologyMibObjects": cadTopologyMibObjects,
       "cadFiberNodeStatusTable": cadFiberNodeStatusTable,
       "cadFiberNodeStatusEntry": cadFiberNodeStatusEntry,
       "cadFiberNodeOperStatus": cadFiberNodeOperStatus,
       "cadFiberNodeNumOther": cadFiberNodeNumOther,
       "cadFiberNodeNumInitRanging": cadFiberNodeNumInitRanging,
       "cadFiberNodeNumRangingComplete": cadFiberNodeNumRangingComplete,
       "cadFiberNodeNumStartEae": cadFiberNodeNumStartEae,
       "cadFiberNodeNumStartDhcpv4": cadFiberNodeNumStartDhcpv4,
       "cadFiberNodeNumStartDhcpv6": cadFiberNodeNumStartDhcpv6,
       "cadFiberNodeNumDhcpv4Complete": cadFiberNodeNumDhcpv4Complete,
       "cadFiberNodeNumDhcpv6Complete": cadFiberNodeNumDhcpv6Complete,
       "cadFiberNodeNumStartCfgFileDownload": cadFiberNodeNumStartCfgFileDownload,
       "cadFiberNodeNumCfgFileDownloadComplete": cadFiberNodeNumCfgFileDownloadComplete,
       "cadFiberNodeNumStartRegistration": cadFiberNodeNumStartRegistration,
       "cadFiberNodeNumRegistrationComplete": cadFiberNodeNumRegistrationComplete,
       "cadFiberNodeNumOperational": cadFiberNodeNumOperational,
       "cadFiberNodeNumBpiInit": cadFiberNodeNumBpiInit,
       "cadFiberNodeNumForwardingDisabled": cadFiberNodeNumForwardingDisabled,
       "cadFiberNodeNumRfMuteAll": cadFiberNodeNumRfMuteAll,
       "cadFiberNodeNumTotal": cadFiberNodeNumTotal,
       "cadFiberNodeNumRangingAborted": cadFiberNodeNumRangingAborted,
       "cadFiberNodeNumRangFlaps": cadFiberNodeNumRangFlaps,
       "cadFiberNodeNumProvFlaps": cadFiberNodeNumProvFlaps,
       "cadFiberNodeNumRegFlaps": cadFiberNodeNumRegFlaps,
       "cadChlFnTable": cadChlFnTable,
       "cadChlFnEntry": cadChlFnEntry,
       "cadChlIfIndex": cadChlIfIndex,
       "cadChlFnIfDirection": cadChlFnIfDirection,
       "cadChlFnMdUsOrDsSgId": cadChlFnMdUsOrDsSgId,
       "cadChlFnUsOrDsPhysChlIfIndex": cadChlFnUsOrDsPhysChlIfIndex,
       "cadChlFnChlId": cadChlFnChlId}
)
