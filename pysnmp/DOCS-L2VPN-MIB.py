# SNMP MIB module (DOCS-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-L2VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:02 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(docsIfCmtsCmStatusIndex,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsCmStatusIndex")

(docsQosPktClassId,
 docsQosServiceFlowId) = mibBuilder.importSymbols(
    "DOCS-QOS-MIB",
    "docsQosPktClassId",
    "docsQosServiceFlowId")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(dot1qFdbId,
 dot1qTpFdbAddress,
 dot1qTpGroupAddress,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qFdbId",
    "dot1qTpFdbAddress",
    "dot1qTpGroupAddress",
    "dot1qVlanIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsL2vpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8)
)
docsL2vpnMIB.setRevisions(
        ("2006-03-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DocsL2vpnIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class DocsL2vpnIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class DocsNsiEncapSubtype(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021ad", 3),
          ("ieee8021q", 2),
          ("l2tpv3", 5),
          ("mpls", 4),
          ("other", 1))
    )



class DocsNsiEncapValue(OctetString, TextualConvention):
    status = "current"


class DocsL2vpnIfList(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_DocsL2vpnMIBNotifications_ObjectIdentity = ObjectIdentity
docsL2vpnMIBNotifications = _DocsL2vpnMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 0)
)
_DocsL2vpnMIBObjects_ObjectIdentity = ObjectIdentity
docsL2vpnMIBObjects = _DocsL2vpnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1)
)
_DocsL2vpnIdToIndexTable_Object = MibTable
docsL2vpnIdToIndexTable = _DocsL2vpnIdToIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    docsL2vpnIdToIndexTable.setStatus("current")
_DocsL2vpnIdToIndexEntry_Object = MibTableRow
docsL2vpnIdToIndexEntry = _DocsL2vpnIdToIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 1, 1)
)
docsL2vpnIdToIndexEntry.setIndexNames(
    (0, "DOCS-L2VPN-MIB", "docsL2vpnId"),
)
if mibBuilder.loadTexts:
    docsL2vpnIdToIndexEntry.setStatus("current")
_DocsL2vpnId_Type = DocsL2vpnIdentifier
_DocsL2vpnId_Object = MibTableColumn
docsL2vpnId = _DocsL2vpnId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 1, 1, 1),
    _DocsL2vpnId_Type()
)
docsL2vpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsL2vpnId.setStatus("current")
_DocsL2vpnIdToIndexIdx_Type = DocsL2vpnIndex
_DocsL2vpnIdToIndexIdx_Object = MibTableColumn
docsL2vpnIdToIndexIdx = _DocsL2vpnIdToIndexIdx_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 1, 1, 2),
    _DocsL2vpnIdToIndexIdx_Type()
)
docsL2vpnIdToIndexIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnIdToIndexIdx.setStatus("current")
_DocsL2vpnIndexToIdTable_Object = MibTable
docsL2vpnIndexToIdTable = _DocsL2vpnIndexToIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    docsL2vpnIndexToIdTable.setStatus("current")
_DocsL2vpnIndexToIdEntry_Object = MibTableRow
docsL2vpnIndexToIdEntry = _DocsL2vpnIndexToIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 2, 1)
)
docsL2vpnIndexToIdEntry.setIndexNames(
    (0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"),
)
if mibBuilder.loadTexts:
    docsL2vpnIndexToIdEntry.setStatus("current")
_DocsL2vpnIdx_Type = DocsL2vpnIndex
_DocsL2vpnIdx_Object = MibTableColumn
docsL2vpnIdx = _DocsL2vpnIdx_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 2, 1, 1),
    _DocsL2vpnIdx_Type()
)
docsL2vpnIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsL2vpnIdx.setStatus("current")
_DocsL2vpnIndexToIdId_Type = DocsL2vpnIdentifier
_DocsL2vpnIndexToIdId_Object = MibTableColumn
docsL2vpnIndexToIdId = _DocsL2vpnIndexToIdId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 2, 1, 2),
    _DocsL2vpnIndexToIdId_Type()
)
docsL2vpnIndexToIdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnIndexToIdId.setStatus("current")
_DocsL2vpnCmTable_Object = MibTable
docsL2vpnCmTable = _DocsL2vpnCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    docsL2vpnCmTable.setStatus("current")
_DocsL2vpnCmEntry_Object = MibTableRow
docsL2vpnCmEntry = _DocsL2vpnCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3, 1)
)
docsL2vpnCmEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    docsL2vpnCmEntry.setStatus("current")
_DocsL2vpnCmCompliantCapability_Type = TruthValue
_DocsL2vpnCmCompliantCapability_Object = MibTableColumn
docsL2vpnCmCompliantCapability = _DocsL2vpnCmCompliantCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3, 1, 1),
    _DocsL2vpnCmCompliantCapability_Type()
)
docsL2vpnCmCompliantCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnCmCompliantCapability.setStatus("current")
_DocsL2vpnCmDutFilteringCapability_Type = TruthValue
_DocsL2vpnCmDutFilteringCapability_Object = MibTableColumn
docsL2vpnCmDutFilteringCapability = _DocsL2vpnCmDutFilteringCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3, 1, 2),
    _DocsL2vpnCmDutFilteringCapability_Type()
)
docsL2vpnCmDutFilteringCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnCmDutFilteringCapability.setStatus("current")
_DocsL2vpnCmDutCMIM_Type = DocsL2vpnIfList
_DocsL2vpnCmDutCMIM_Object = MibTableColumn
docsL2vpnCmDutCMIM = _DocsL2vpnCmDutCMIM_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3, 1, 3),
    _DocsL2vpnCmDutCMIM_Type()
)
docsL2vpnCmDutCMIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnCmDutCMIM.setStatus("current")
_DocsL2vpnCmDhcpSnooping_Type = DocsL2vpnIfList
_DocsL2vpnCmDhcpSnooping_Object = MibTableColumn
docsL2vpnCmDhcpSnooping = _DocsL2vpnCmDhcpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3, 1, 4),
    _DocsL2vpnCmDhcpSnooping_Type()
)
docsL2vpnCmDhcpSnooping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnCmDhcpSnooping.setStatus("current")
_DocsL2vpnVpnCmTable_Object = MibTable
docsL2vpnVpnCmTable = _DocsL2vpnVpnCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 4)
)
if mibBuilder.loadTexts:
    docsL2vpnVpnCmTable.setStatus("current")
_DocsL2vpnVpnCmEntry_Object = MibTableRow
docsL2vpnVpnCmEntry = _DocsL2vpnVpnCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 4, 1)
)
docsL2vpnVpnCmEntry.setIndexNames(
    (0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"),
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    docsL2vpnVpnCmEntry.setStatus("current")
_DocsL2vpnVpnCmCMIM_Type = DocsL2vpnIfList
_DocsL2vpnVpnCmCMIM_Object = MibTableColumn
docsL2vpnVpnCmCMIM = _DocsL2vpnVpnCmCMIM_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 4, 1, 1),
    _DocsL2vpnVpnCmCMIM_Type()
)
docsL2vpnVpnCmCMIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnVpnCmCMIM.setStatus("current")


class _DocsL2vpnVpnCmIndividualSAId_Type(Integer32):
    """Custom type docsL2vpnVpnCmIndividualSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DocsL2vpnVpnCmIndividualSAId_Type.__name__ = "Integer32"
_DocsL2vpnVpnCmIndividualSAId_Object = MibTableColumn
docsL2vpnVpnCmIndividualSAId = _DocsL2vpnVpnCmIndividualSAId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 4, 1, 2),
    _DocsL2vpnVpnCmIndividualSAId_Type()
)
docsL2vpnVpnCmIndividualSAId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnVpnCmIndividualSAId.setStatus("current")
_DocsL2vpnVpnCmVendorSpecific_Type = OctetString
_DocsL2vpnVpnCmVendorSpecific_Object = MibTableColumn
docsL2vpnVpnCmVendorSpecific = _DocsL2vpnVpnCmVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 4, 1, 3),
    _DocsL2vpnVpnCmVendorSpecific_Type()
)
docsL2vpnVpnCmVendorSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnVpnCmVendorSpecific.setStatus("current")
_DocsL2vpnVpnCmStatsTable_Object = MibTable
docsL2vpnVpnCmStatsTable = _DocsL2vpnVpnCmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5)
)
if mibBuilder.loadTexts:
    docsL2vpnVpnCmStatsTable.setStatus("current")
_DocsL2vpnVpnCmStatsEntry_Object = MibTableRow
docsL2vpnVpnCmStatsEntry = _DocsL2vpnVpnCmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1)
)
docsL2vpnVpnCmStatsEntry.setIndexNames(
    (0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"),
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    docsL2vpnVpnCmStatsEntry.setStatus("current")
_DocsL2vpnVpnCmStatsUpstreamPkts_Type = Counter32
_DocsL2vpnVpnCmStatsUpstreamPkts_Object = MibTableColumn
docsL2vpnVpnCmStatsUpstreamPkts = _DocsL2vpnVpnCmStatsUpstreamPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 1),
    _DocsL2vpnVpnCmStatsUpstreamPkts_Type()
)
docsL2vpnVpnCmStatsUpstreamPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnVpnCmStatsUpstreamPkts.setStatus("current")
_DocsL2vpnVpnCmStatsUpstreamBytes_Type = Counter32
_DocsL2vpnVpnCmStatsUpstreamBytes_Object = MibTableColumn
docsL2vpnVpnCmStatsUpstreamBytes = _DocsL2vpnVpnCmStatsUpstreamBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 2),
    _DocsL2vpnVpnCmStatsUpstreamBytes_Type()
)
docsL2vpnVpnCmStatsUpstreamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnVpnCmStatsUpstreamBytes.setStatus("current")
_DocsL2vpnVpnCmStatsUpstreamDiscards_Type = Counter32
_DocsL2vpnVpnCmStatsUpstreamDiscards_Object = MibTableColumn
docsL2vpnVpnCmStatsUpstreamDiscards = _DocsL2vpnVpnCmStatsUpstreamDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 3),
    _DocsL2vpnVpnCmStatsUpstreamDiscards_Type()
)
docsL2vpnVpnCmStatsUpstreamDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnVpnCmStatsUpstreamDiscards.setStatus("current")
_DocsL2vpnVpnCmStatsDownstreamPkts_Type = Counter32
_DocsL2vpnVpnCmStatsDownstreamPkts_Object = MibTableColumn
docsL2vpnVpnCmStatsDownstreamPkts = _DocsL2vpnVpnCmStatsDownstreamPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 4),
    _DocsL2vpnVpnCmStatsDownstreamPkts_Type()
)
docsL2vpnVpnCmStatsDownstreamPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnVpnCmStatsDownstreamPkts.setStatus("current")
_DocsL2vpnVpnCmStatsDownstreamBytes_Type = Counter32
_DocsL2vpnVpnCmStatsDownstreamBytes_Object = MibTableColumn
docsL2vpnVpnCmStatsDownstreamBytes = _DocsL2vpnVpnCmStatsDownstreamBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 5),
    _DocsL2vpnVpnCmStatsDownstreamBytes_Type()
)
docsL2vpnVpnCmStatsDownstreamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnVpnCmStatsDownstreamBytes.setStatus("current")
_DocsL2vpnVpnCmStatsDownstreamDiscards_Type = Counter32
_DocsL2vpnVpnCmStatsDownstreamDiscards_Object = MibTableColumn
docsL2vpnVpnCmStatsDownstreamDiscards = _DocsL2vpnVpnCmStatsDownstreamDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 6),
    _DocsL2vpnVpnCmStatsDownstreamDiscards_Type()
)
docsL2vpnVpnCmStatsDownstreamDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnVpnCmStatsDownstreamDiscards.setStatus("current")
_DocsL2vpnPortStatusTable_Object = MibTable
docsL2vpnPortStatusTable = _DocsL2vpnPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 6)
)
if mibBuilder.loadTexts:
    docsL2vpnPortStatusTable.setStatus("current")
_DocsL2vpnPortStatusEntry_Object = MibTableRow
docsL2vpnPortStatusEntry = _DocsL2vpnPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 6, 1)
)
docsL2vpnPortStatusEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"),
)
if mibBuilder.loadTexts:
    docsL2vpnPortStatusEntry.setStatus("current")


class _DocsL2vpnPortStatusGroupSAId_Type(Integer32):
    """Custom type docsL2vpnPortStatusGroupSAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DocsL2vpnPortStatusGroupSAId_Type.__name__ = "Integer32"
_DocsL2vpnPortStatusGroupSAId_Object = MibTableColumn
docsL2vpnPortStatusGroupSAId = _DocsL2vpnPortStatusGroupSAId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 6, 1, 1),
    _DocsL2vpnPortStatusGroupSAId_Type()
)
docsL2vpnPortStatusGroupSAId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnPortStatusGroupSAId.setStatus("current")
_DocsL2vpnSfStatusTable_Object = MibTable
docsL2vpnSfStatusTable = _DocsL2vpnSfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 7)
)
if mibBuilder.loadTexts:
    docsL2vpnSfStatusTable.setStatus("current")
_DocsL2vpnSfStatusEntry_Object = MibTableRow
docsL2vpnSfStatusEntry = _DocsL2vpnSfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 7, 1)
)
docsL2vpnSfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS-MIB", "docsQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsL2vpnSfStatusEntry.setStatus("current")
_DocsL2vpnSfStatusL2vpnId_Type = OctetString
_DocsL2vpnSfStatusL2vpnId_Object = MibTableColumn
docsL2vpnSfStatusL2vpnId = _DocsL2vpnSfStatusL2vpnId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 7, 1, 1),
    _DocsL2vpnSfStatusL2vpnId_Type()
)
docsL2vpnSfStatusL2vpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnSfStatusL2vpnId.setStatus("current")


class _DocsL2vpnSfStatusIngressUserPriority_Type(Unsigned32):
    """Custom type docsL2vpnSfStatusIngressUserPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsL2vpnSfStatusIngressUserPriority_Type.__name__ = "Unsigned32"
_DocsL2vpnSfStatusIngressUserPriority_Object = MibTableColumn
docsL2vpnSfStatusIngressUserPriority = _DocsL2vpnSfStatusIngressUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 7, 1, 2),
    _DocsL2vpnSfStatusIngressUserPriority_Type()
)
docsL2vpnSfStatusIngressUserPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnSfStatusIngressUserPriority.setStatus("current")
_DocsL2vpnSfStatusVendorSpecific_Type = OctetString
_DocsL2vpnSfStatusVendorSpecific_Object = MibTableColumn
docsL2vpnSfStatusVendorSpecific = _DocsL2vpnSfStatusVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 7, 1, 3),
    _DocsL2vpnSfStatusVendorSpecific_Type()
)
docsL2vpnSfStatusVendorSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnSfStatusVendorSpecific.setStatus("current")
_DocsL2vpnPktClassTable_Object = MibTable
docsL2vpnPktClassTable = _DocsL2vpnPktClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8)
)
if mibBuilder.loadTexts:
    docsL2vpnPktClassTable.setStatus("current")
_DocsL2vpnPktClassEntry_Object = MibTableRow
docsL2vpnPktClassEntry = _DocsL2vpnPktClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1)
)
docsL2vpnPktClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS-MIB", "docsQosServiceFlowId"),
    (0, "DOCS-QOS-MIB", "docsQosPktClassId"),
)
if mibBuilder.loadTexts:
    docsL2vpnPktClassEntry.setStatus("current")
_DocsL2vpnPktClassL2vpnId_Type = DocsL2vpnIdentifier
_DocsL2vpnPktClassL2vpnId_Object = MibTableColumn
docsL2vpnPktClassL2vpnId = _DocsL2vpnPktClassL2vpnId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1, 1),
    _DocsL2vpnPktClassL2vpnId_Type()
)
docsL2vpnPktClassL2vpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnPktClassL2vpnId.setStatus("current")


class _DocsL2vpnPktClassUserPriRangeLow_Type(Unsigned32):
    """Custom type docsL2vpnPktClassUserPriRangeLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsL2vpnPktClassUserPriRangeLow_Type.__name__ = "Unsigned32"
_DocsL2vpnPktClassUserPriRangeLow_Object = MibTableColumn
docsL2vpnPktClassUserPriRangeLow = _DocsL2vpnPktClassUserPriRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1, 2),
    _DocsL2vpnPktClassUserPriRangeLow_Type()
)
docsL2vpnPktClassUserPriRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnPktClassUserPriRangeLow.setStatus("current")


class _DocsL2vpnPktClassUserPriRangeHigh_Type(Unsigned32):
    """Custom type docsL2vpnPktClassUserPriRangeHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsL2vpnPktClassUserPriRangeHigh_Type.__name__ = "Unsigned32"
_DocsL2vpnPktClassUserPriRangeHigh_Object = MibTableColumn
docsL2vpnPktClassUserPriRangeHigh = _DocsL2vpnPktClassUserPriRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1, 3),
    _DocsL2vpnPktClassUserPriRangeHigh_Type()
)
docsL2vpnPktClassUserPriRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnPktClassUserPriRangeHigh.setStatus("current")
_DocsL2vpnPktClassCMIM_Type = DocsL2vpnIfList
_DocsL2vpnPktClassCMIM_Object = MibTableColumn
docsL2vpnPktClassCMIM = _DocsL2vpnPktClassCMIM_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1, 4),
    _DocsL2vpnPktClassCMIM_Type()
)
docsL2vpnPktClassCMIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnPktClassCMIM.setStatus("current")
_DocsL2vpnPktClassVendorSpecific_Type = OctetString
_DocsL2vpnPktClassVendorSpecific_Object = MibTableColumn
docsL2vpnPktClassVendorSpecific = _DocsL2vpnPktClassVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1, 5),
    _DocsL2vpnPktClassVendorSpecific_Type()
)
docsL2vpnPktClassVendorSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnPktClassVendorSpecific.setStatus("current")
_DocsL2vpnCmNsiTable_Object = MibTable
docsL2vpnCmNsiTable = _DocsL2vpnCmNsiTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9)
)
if mibBuilder.loadTexts:
    docsL2vpnCmNsiTable.setStatus("current")
_DocsL2vpnCmNsiEntry_Object = MibTableRow
docsL2vpnCmNsiEntry = _DocsL2vpnCmNsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1)
)
docsL2vpnCmNsiEntry.setIndexNames(
    (0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"),
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    docsL2vpnCmNsiEntry.setStatus("current")
_DocsL2vpnCmNsiEncapSubtype_Type = DocsNsiEncapSubtype
_DocsL2vpnCmNsiEncapSubtype_Object = MibTableColumn
docsL2vpnCmNsiEncapSubtype = _DocsL2vpnCmNsiEncapSubtype_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1, 1),
    _DocsL2vpnCmNsiEncapSubtype_Type()
)
docsL2vpnCmNsiEncapSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnCmNsiEncapSubtype.setStatus("current")
_DocsL2vpnCmNsiEncapValue_Type = DocsNsiEncapValue
_DocsL2vpnCmNsiEncapValue_Object = MibTableColumn
docsL2vpnCmNsiEncapValue = _DocsL2vpnCmNsiEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1, 2),
    _DocsL2vpnCmNsiEncapValue_Type()
)
docsL2vpnCmNsiEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnCmNsiEncapValue.setStatus("current")
_DocsL2vpnCmNsiAGI_Type = OctetString
_DocsL2vpnCmNsiAGI_Object = MibTableColumn
docsL2vpnCmNsiAGI = _DocsL2vpnCmNsiAGI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1, 3),
    _DocsL2vpnCmNsiAGI_Type()
)
docsL2vpnCmNsiAGI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnCmNsiAGI.setStatus("current")
_DocsL2vpnCmNsiSAII_Type = OctetString
_DocsL2vpnCmNsiSAII_Object = MibTableColumn
docsL2vpnCmNsiSAII = _DocsL2vpnCmNsiSAII_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1, 4),
    _DocsL2vpnCmNsiSAII_Type()
)
docsL2vpnCmNsiSAII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnCmNsiSAII.setStatus("current")
_DocsL2vpnCmNsiTAII_Type = OctetString
_DocsL2vpnCmNsiTAII_Object = MibTableColumn
docsL2vpnCmNsiTAII = _DocsL2vpnCmNsiTAII_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1, 5),
    _DocsL2vpnCmNsiTAII_Type()
)
docsL2vpnCmNsiTAII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnCmNsiTAII.setStatus("current")
_DocsL2vpnCmVpnCpeTable_Object = MibTable
docsL2vpnCmVpnCpeTable = _DocsL2vpnCmVpnCpeTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 10)
)
if mibBuilder.loadTexts:
    docsL2vpnCmVpnCpeTable.setStatus("current")
_DocsL2vpnCmVpnCpeEntry_Object = MibTableRow
docsL2vpnCmVpnCpeEntry = _DocsL2vpnCmVpnCpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 10, 1)
)
docsL2vpnCmVpnCpeEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
    (0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"),
    (0, "DOCS-L2VPN-MIB", "docsL2vpnCmVpnCpeMacAddress"),
)
if mibBuilder.loadTexts:
    docsL2vpnCmVpnCpeEntry.setStatus("current")
_DocsL2vpnCmVpnCpeMacAddress_Type = MacAddress
_DocsL2vpnCmVpnCpeMacAddress_Object = MibTableColumn
docsL2vpnCmVpnCpeMacAddress = _DocsL2vpnCmVpnCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 10, 1, 1),
    _DocsL2vpnCmVpnCpeMacAddress_Type()
)
docsL2vpnCmVpnCpeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnCmVpnCpeMacAddress.setStatus("current")
_DocsL2vpnVpnCmCpeTable_Object = MibTable
docsL2vpnVpnCmCpeTable = _DocsL2vpnVpnCmCpeTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 11)
)
if mibBuilder.loadTexts:
    docsL2vpnVpnCmCpeTable.setStatus("current")
_DocsL2vpnVpnCmCpeEntry_Object = MibTableRow
docsL2vpnVpnCmCpeEntry = _DocsL2vpnVpnCmCpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 11, 1)
)
docsL2vpnVpnCmCpeEntry.setIndexNames(
    (0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"),
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
    (0, "DOCS-L2VPN-MIB", "docsL2vpnVpnCmCpeMacAddress"),
)
if mibBuilder.loadTexts:
    docsL2vpnVpnCmCpeEntry.setStatus("current")
_DocsL2vpnVpnCmCpeMacAddress_Type = MacAddress
_DocsL2vpnVpnCmCpeMacAddress_Object = MibTableColumn
docsL2vpnVpnCmCpeMacAddress = _DocsL2vpnVpnCmCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 11, 1, 1),
    _DocsL2vpnVpnCmCpeMacAddress_Type()
)
docsL2vpnVpnCmCpeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnVpnCmCpeMacAddress.setStatus("current")
_DocsL2vpnDot1qTpFdbExtTable_Object = MibTable
docsL2vpnDot1qTpFdbExtTable = _DocsL2vpnDot1qTpFdbExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 12)
)
if mibBuilder.loadTexts:
    docsL2vpnDot1qTpFdbExtTable.setStatus("current")
_DocsL2vpnDot1qTpFdbExtEntry_Object = MibTableRow
docsL2vpnDot1qTpFdbExtEntry = _DocsL2vpnDot1qTpFdbExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 12, 1)
)
docsL2vpnDot1qTpFdbExtEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
    (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"),
)
if mibBuilder.loadTexts:
    docsL2vpnDot1qTpFdbExtEntry.setStatus("current")
_DocsL2vpnDot1qTpFdbExtTransmitPkts_Type = Counter32
_DocsL2vpnDot1qTpFdbExtTransmitPkts_Object = MibTableColumn
docsL2vpnDot1qTpFdbExtTransmitPkts = _DocsL2vpnDot1qTpFdbExtTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 12, 1, 1),
    _DocsL2vpnDot1qTpFdbExtTransmitPkts_Type()
)
docsL2vpnDot1qTpFdbExtTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnDot1qTpFdbExtTransmitPkts.setStatus("current")
_DocsL2vpnDot1qTpFdbExtReceivePkts_Type = Counter32
_DocsL2vpnDot1qTpFdbExtReceivePkts_Object = MibTableColumn
docsL2vpnDot1qTpFdbExtReceivePkts = _DocsL2vpnDot1qTpFdbExtReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 12, 1, 2),
    _DocsL2vpnDot1qTpFdbExtReceivePkts_Type()
)
docsL2vpnDot1qTpFdbExtReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnDot1qTpFdbExtReceivePkts.setStatus("current")
_DocsL2vpnDot1qTpGroupExtTable_Object = MibTable
docsL2vpnDot1qTpGroupExtTable = _DocsL2vpnDot1qTpGroupExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 13)
)
if mibBuilder.loadTexts:
    docsL2vpnDot1qTpGroupExtTable.setStatus("current")
_DocsL2vpnDot1qTpGroupExtEntry_Object = MibTableRow
docsL2vpnDot1qTpGroupExtEntry = _DocsL2vpnDot1qTpGroupExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 13, 1)
)
docsL2vpnDot1qTpGroupExtEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qTpGroupAddress"),
)
if mibBuilder.loadTexts:
    docsL2vpnDot1qTpGroupExtEntry.setStatus("current")
_DocsL2vpnDot1qTpGroupExtTransmitPkts_Type = Counter32
_DocsL2vpnDot1qTpGroupExtTransmitPkts_Object = MibTableColumn
docsL2vpnDot1qTpGroupExtTransmitPkts = _DocsL2vpnDot1qTpGroupExtTransmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 13, 1, 1),
    _DocsL2vpnDot1qTpGroupExtTransmitPkts_Type()
)
docsL2vpnDot1qTpGroupExtTransmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnDot1qTpGroupExtTransmitPkts.setStatus("current")
_DocsL2vpnDot1qTpGroupExtReceivePkts_Type = Counter32
_DocsL2vpnDot1qTpGroupExtReceivePkts_Object = MibTableColumn
docsL2vpnDot1qTpGroupExtReceivePkts = _DocsL2vpnDot1qTpGroupExtReceivePkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 13, 1, 2),
    _DocsL2vpnDot1qTpGroupExtReceivePkts_Type()
)
docsL2vpnDot1qTpGroupExtReceivePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsL2vpnDot1qTpGroupExtReceivePkts.setStatus("current")
_DocsL2vpnConformance_ObjectIdentity = ObjectIdentity
docsL2vpnConformance = _DocsL2vpnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2)
)
_DocsL2vpnCompliances_ObjectIdentity = ObjectIdentity
docsL2vpnCompliances = _DocsL2vpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 1)
)
_DocsL2vpnGroups_ObjectIdentity = ObjectIdentity
docsL2vpnGroups = _DocsL2vpnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 2)
)

# Managed Objects groups

docsL2vpnBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 2, 1)
)
docsL2vpnBaseGroup.setObjects(
      *(("DOCS-L2VPN-MIB", "docsL2vpnIdToIndexIdx"),
        ("DOCS-L2VPN-MIB", "docsL2vpnIndexToIdId"),
        ("DOCS-L2VPN-MIB", "docsL2vpnCmCompliantCapability"),
        ("DOCS-L2VPN-MIB", "docsL2vpnCmDutFilteringCapability"),
        ("DOCS-L2VPN-MIB", "docsL2vpnCmDutCMIM"),
        ("DOCS-L2VPN-MIB", "docsL2vpnCmDhcpSnooping"),
        ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmCMIM"),
        ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmVendorSpecific"),
        ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmIndividualSAId"),
        ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsUpstreamPkts"),
        ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsUpstreamBytes"),
        ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsUpstreamDiscards"),
        ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsDownstreamPkts"),
        ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsDownstreamBytes"),
        ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsDownstreamDiscards"),
        ("DOCS-L2VPN-MIB", "docsL2vpnPortStatusGroupSAId"),
        ("DOCS-L2VPN-MIB", "docsL2vpnSfStatusL2vpnId"),
        ("DOCS-L2VPN-MIB", "docsL2vpnSfStatusIngressUserPriority"),
        ("DOCS-L2VPN-MIB", "docsL2vpnSfStatusVendorSpecific"),
        ("DOCS-L2VPN-MIB", "docsL2vpnPktClassL2vpnId"),
        ("DOCS-L2VPN-MIB", "docsL2vpnPktClassUserPriRangeLow"),
        ("DOCS-L2VPN-MIB", "docsL2vpnPktClassUserPriRangeHigh"),
        ("DOCS-L2VPN-MIB", "docsL2vpnPktClassCMIM"),
        ("DOCS-L2VPN-MIB", "docsL2vpnPktClassVendorSpecific"))
)
if mibBuilder.loadTexts:
    docsL2vpnBaseGroup.setStatus("current")

docsL2vpnPointToPointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 2, 2)
)
docsL2vpnPointToPointGroup.setObjects(
      *(("DOCS-L2VPN-MIB", "docsL2vpnCmNsiEncapSubtype"),
        ("DOCS-L2VPN-MIB", "docsL2vpnCmNsiEncapValue"),
        ("DOCS-L2VPN-MIB", "docsL2vpnCmNsiAGI"),
        ("DOCS-L2VPN-MIB", "docsL2vpnCmNsiSAII"),
        ("DOCS-L2VPN-MIB", "docsL2vpnCmNsiTAII"))
)
if mibBuilder.loadTexts:
    docsL2vpnPointToPointGroup.setStatus("current")

docsL2vpnMultipointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 2, 3)
)
docsL2vpnMultipointGroup.setObjects(
      *(("DOCS-L2VPN-MIB", "docsL2vpnCmVpnCpeMacAddress"),
        ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmCpeMacAddress"),
        ("DOCS-L2VPN-MIB", "docsL2vpnDot1qTpFdbExtTransmitPkts"),
        ("DOCS-L2VPN-MIB", "docsL2vpnDot1qTpFdbExtReceivePkts"),
        ("DOCS-L2VPN-MIB", "docsL2vpnDot1qTpGroupExtTransmitPkts"),
        ("DOCS-L2VPN-MIB", "docsL2vpnDot1qTpGroupExtReceivePkts"))
)
if mibBuilder.loadTexts:
    docsL2vpnMultipointGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsL2vpnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsL2vpnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-L2VPN-MIB",
    **{"DocsL2vpnIdentifier": DocsL2vpnIdentifier,
       "DocsL2vpnIndex": DocsL2vpnIndex,
       "DocsNsiEncapSubtype": DocsNsiEncapSubtype,
       "DocsNsiEncapValue": DocsNsiEncapValue,
       "DocsL2vpnIfList": DocsL2vpnIfList,
       "docsL2vpnMIB": docsL2vpnMIB,
       "docsL2vpnMIBNotifications": docsL2vpnMIBNotifications,
       "docsL2vpnMIBObjects": docsL2vpnMIBObjects,
       "docsL2vpnIdToIndexTable": docsL2vpnIdToIndexTable,
       "docsL2vpnIdToIndexEntry": docsL2vpnIdToIndexEntry,
       "docsL2vpnId": docsL2vpnId,
       "docsL2vpnIdToIndexIdx": docsL2vpnIdToIndexIdx,
       "docsL2vpnIndexToIdTable": docsL2vpnIndexToIdTable,
       "docsL2vpnIndexToIdEntry": docsL2vpnIndexToIdEntry,
       "docsL2vpnIdx": docsL2vpnIdx,
       "docsL2vpnIndexToIdId": docsL2vpnIndexToIdId,
       "docsL2vpnCmTable": docsL2vpnCmTable,
       "docsL2vpnCmEntry": docsL2vpnCmEntry,
       "docsL2vpnCmCompliantCapability": docsL2vpnCmCompliantCapability,
       "docsL2vpnCmDutFilteringCapability": docsL2vpnCmDutFilteringCapability,
       "docsL2vpnCmDutCMIM": docsL2vpnCmDutCMIM,
       "docsL2vpnCmDhcpSnooping": docsL2vpnCmDhcpSnooping,
       "docsL2vpnVpnCmTable": docsL2vpnVpnCmTable,
       "docsL2vpnVpnCmEntry": docsL2vpnVpnCmEntry,
       "docsL2vpnVpnCmCMIM": docsL2vpnVpnCmCMIM,
       "docsL2vpnVpnCmIndividualSAId": docsL2vpnVpnCmIndividualSAId,
       "docsL2vpnVpnCmVendorSpecific": docsL2vpnVpnCmVendorSpecific,
       "docsL2vpnVpnCmStatsTable": docsL2vpnVpnCmStatsTable,
       "docsL2vpnVpnCmStatsEntry": docsL2vpnVpnCmStatsEntry,
       "docsL2vpnVpnCmStatsUpstreamPkts": docsL2vpnVpnCmStatsUpstreamPkts,
       "docsL2vpnVpnCmStatsUpstreamBytes": docsL2vpnVpnCmStatsUpstreamBytes,
       "docsL2vpnVpnCmStatsUpstreamDiscards": docsL2vpnVpnCmStatsUpstreamDiscards,
       "docsL2vpnVpnCmStatsDownstreamPkts": docsL2vpnVpnCmStatsDownstreamPkts,
       "docsL2vpnVpnCmStatsDownstreamBytes": docsL2vpnVpnCmStatsDownstreamBytes,
       "docsL2vpnVpnCmStatsDownstreamDiscards": docsL2vpnVpnCmStatsDownstreamDiscards,
       "docsL2vpnPortStatusTable": docsL2vpnPortStatusTable,
       "docsL2vpnPortStatusEntry": docsL2vpnPortStatusEntry,
       "docsL2vpnPortStatusGroupSAId": docsL2vpnPortStatusGroupSAId,
       "docsL2vpnSfStatusTable": docsL2vpnSfStatusTable,
       "docsL2vpnSfStatusEntry": docsL2vpnSfStatusEntry,
       "docsL2vpnSfStatusL2vpnId": docsL2vpnSfStatusL2vpnId,
       "docsL2vpnSfStatusIngressUserPriority": docsL2vpnSfStatusIngressUserPriority,
       "docsL2vpnSfStatusVendorSpecific": docsL2vpnSfStatusVendorSpecific,
       "docsL2vpnPktClassTable": docsL2vpnPktClassTable,
       "docsL2vpnPktClassEntry": docsL2vpnPktClassEntry,
       "docsL2vpnPktClassL2vpnId": docsL2vpnPktClassL2vpnId,
       "docsL2vpnPktClassUserPriRangeLow": docsL2vpnPktClassUserPriRangeLow,
       "docsL2vpnPktClassUserPriRangeHigh": docsL2vpnPktClassUserPriRangeHigh,
       "docsL2vpnPktClassCMIM": docsL2vpnPktClassCMIM,
       "docsL2vpnPktClassVendorSpecific": docsL2vpnPktClassVendorSpecific,
       "docsL2vpnCmNsiTable": docsL2vpnCmNsiTable,
       "docsL2vpnCmNsiEntry": docsL2vpnCmNsiEntry,
       "docsL2vpnCmNsiEncapSubtype": docsL2vpnCmNsiEncapSubtype,
       "docsL2vpnCmNsiEncapValue": docsL2vpnCmNsiEncapValue,
       "docsL2vpnCmNsiAGI": docsL2vpnCmNsiAGI,
       "docsL2vpnCmNsiSAII": docsL2vpnCmNsiSAII,
       "docsL2vpnCmNsiTAII": docsL2vpnCmNsiTAII,
       "docsL2vpnCmVpnCpeTable": docsL2vpnCmVpnCpeTable,
       "docsL2vpnCmVpnCpeEntry": docsL2vpnCmVpnCpeEntry,
       "docsL2vpnCmVpnCpeMacAddress": docsL2vpnCmVpnCpeMacAddress,
       "docsL2vpnVpnCmCpeTable": docsL2vpnVpnCmCpeTable,
       "docsL2vpnVpnCmCpeEntry": docsL2vpnVpnCmCpeEntry,
       "docsL2vpnVpnCmCpeMacAddress": docsL2vpnVpnCmCpeMacAddress,
       "docsL2vpnDot1qTpFdbExtTable": docsL2vpnDot1qTpFdbExtTable,
       "docsL2vpnDot1qTpFdbExtEntry": docsL2vpnDot1qTpFdbExtEntry,
       "docsL2vpnDot1qTpFdbExtTransmitPkts": docsL2vpnDot1qTpFdbExtTransmitPkts,
       "docsL2vpnDot1qTpFdbExtReceivePkts": docsL2vpnDot1qTpFdbExtReceivePkts,
       "docsL2vpnDot1qTpGroupExtTable": docsL2vpnDot1qTpGroupExtTable,
       "docsL2vpnDot1qTpGroupExtEntry": docsL2vpnDot1qTpGroupExtEntry,
       "docsL2vpnDot1qTpGroupExtTransmitPkts": docsL2vpnDot1qTpGroupExtTransmitPkts,
       "docsL2vpnDot1qTpGroupExtReceivePkts": docsL2vpnDot1qTpGroupExtReceivePkts,
       "docsL2vpnConformance": docsL2vpnConformance,
       "docsL2vpnCompliances": docsL2vpnCompliances,
       "docsL2vpnCompliance": docsL2vpnCompliance,
       "docsL2vpnGroups": docsL2vpnGroups,
       "docsL2vpnBaseGroup": docsL2vpnBaseGroup,
       "docsL2vpnPointToPointGroup": docsL2vpnPointToPointGroup,
       "docsL2vpnMultipointGroup": docsL2vpnMultipointGroup}
)
