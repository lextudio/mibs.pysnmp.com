# SNMP MIB module (CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:31 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoVlanList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoVlanList")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoResilientEthernetProtocolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 601)
)
ciscoResilientEthernetProtocolMIB.setRevisions(
        ("2011-01-11 00:00",
         "2010-10-27 00:00",
         "2007-05-22 00:00",
         "2007-02-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RepPortType(Integer32, TextualConvention):
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
        *(("edge", 2),
          ("edgeNoNeighbor", 4),
          ("edgeNoNeighborPrimary", 5),
          ("edgePrimary", 3),
          ("notEdge", 1))
    )



class RepSegmentId(Unsigned32, TextualConvention):
    status = "current"


class RepSegmentList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoRepMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoRepMIBNotifs = _CiscoRepMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 0)
)
_CiscoRepMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRepMIBObjects = _CiscoRepMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1)
)
_CrepGlobalInfo_ObjectIdentity = ObjectIdentity
crepGlobalInfo = _CrepGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 1)
)
_CrepVersion_Type = Integer32
_CrepVersion_Object = MibScalar
crepVersion = _CrepVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 1, 1),
    _CrepVersion_Type()
)
crepVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepVersion.setStatus("current")


class _CrepAdminVlan_Type(VlanId):
    """Custom type crepAdminVlan based on VlanId"""
    defaultValue = 1


_CrepAdminVlan_Object = MibScalar
crepAdminVlan = _CrepAdminVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 1, 2),
    _CrepAdminVlan_Type()
)
crepAdminVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crepAdminVlan.setStatus("current")
_CrepNotifsEnable_Type = TruthValue
_CrepNotifsEnable_Object = MibScalar
crepNotifsEnable = _CrepNotifsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 1, 3),
    _CrepNotifsEnable_Type()
)
crepNotifsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crepNotifsEnable.setStatus("current")


class _CrepGlobalRepNotifsRate_Type(Unsigned32):
    """Custom type crepGlobalRepNotifsRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CrepGlobalRepNotifsRate_Type.__name__ = "Unsigned32"
_CrepGlobalRepNotifsRate_Object = MibScalar
crepGlobalRepNotifsRate = _CrepGlobalRepNotifsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 1, 4),
    _CrepGlobalRepNotifsRate_Type()
)
crepGlobalRepNotifsRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crepGlobalRepNotifsRate.setStatus("current")
if mibBuilder.loadTexts:
    crepGlobalRepNotifsRate.setUnits("notifications per second")
_CrepMinSegmentId_Type = RepSegmentId
_CrepMinSegmentId_Object = MibScalar
crepMinSegmentId = _CrepMinSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 1, 5),
    _CrepMinSegmentId_Type()
)
crepMinSegmentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepMinSegmentId.setStatus("current")
_CrepMaxSegmentId_Type = RepSegmentId
_CrepMaxSegmentId_Object = MibScalar
crepMaxSegmentId = _CrepMaxSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 1, 6),
    _CrepMaxSegmentId_Type()
)
crepMaxSegmentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepMaxSegmentId.setStatus("current")
_CrepInterfaceConfig_ObjectIdentity = ObjectIdentity
crepInterfaceConfig = _CrepInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2)
)
_CrepInterfaceConfigTable_Object = MibTable
crepInterfaceConfigTable = _CrepInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1)
)
if mibBuilder.loadTexts:
    crepInterfaceConfigTable.setStatus("current")
_CrepInterfaceConfigEntry_Object = MibTableRow
crepInterfaceConfigEntry = _CrepInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1)
)
crepInterfaceConfigEntry.setIndexNames(
    (0, "CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfIndex"),
)
if mibBuilder.loadTexts:
    crepInterfaceConfigEntry.setStatus("current")
_CrepIfIndex_Type = InterfaceIndex
_CrepIfIndex_Object = MibTableColumn
crepIfIndex = _CrepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 1),
    _CrepIfIndex_Type()
)
crepIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crepIfIndex.setStatus("current")
_CrepIfSegmentId_Type = RepSegmentId
_CrepIfSegmentId_Object = MibTableColumn
crepIfSegmentId = _CrepIfSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 2),
    _CrepIfSegmentId_Type()
)
crepIfSegmentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepIfSegmentId.setStatus("current")


class _CrepIfOperStatus_Type(Integer32):
    """Custom type crepIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("flapping", 6),
          ("initDown", 2),
          ("noNeighbour", 3),
          ("none", 1),
          ("oneWay", 4),
          ("twoWay", 5),
          ("unknown", 8),
          ("wait", 7))
    )


_CrepIfOperStatus_Type.__name__ = "Integer32"
_CrepIfOperStatus_Object = MibTableColumn
crepIfOperStatus = _CrepIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 3),
    _CrepIfOperStatus_Type()
)
crepIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepIfOperStatus.setStatus("current")


class _CrepIfPortRole_Type(Integer32):
    """Custom type crepIfPortRole based on Integer32"""
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
        *(("alternatePort", 2),
          ("failedPort", 1),
          ("failedPortLogicalOpen", 5),
          ("failedPortNoNeighbor", 4),
          ("openPort", 3))
    )


_CrepIfPortRole_Type.__name__ = "Integer32"
_CrepIfPortRole_Object = MibTableColumn
crepIfPortRole = _CrepIfPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 4),
    _CrepIfPortRole_Type()
)
crepIfPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepIfPortRole.setStatus("current")


class _CrepIfPortID_Type(OctetString):
    """Custom type crepIfPortID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CrepIfPortID_Type.__name__ = "OctetString"
_CrepIfPortID_Object = MibTableColumn
crepIfPortID = _CrepIfPortID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 5),
    _CrepIfPortID_Type()
)
crepIfPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepIfPortID.setStatus("current")


class _CrepIfAdminEdgePortType_Type(RepPortType):
    """Custom type crepIfAdminEdgePortType based on RepPortType"""


_CrepIfAdminEdgePortType_Object = MibTableColumn
crepIfAdminEdgePortType = _CrepIfAdminEdgePortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 6),
    _CrepIfAdminEdgePortType_Type()
)
crepIfAdminEdgePortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepIfAdminEdgePortType.setStatus("current")
_CrepIfOperEdgePortType_Type = RepPortType
_CrepIfOperEdgePortType_Object = MibTableColumn
crepIfOperEdgePortType = _CrepIfOperEdgePortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 7),
    _CrepIfOperEdgePortType_Type()
)
crepIfOperEdgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepIfOperEdgePortType.setStatus("current")


class _CrepIfPreferredConfig_Type(TruthValue):
    """Custom type crepIfPreferredConfig based on TruthValue"""


_CrepIfPreferredConfig_Object = MibTableColumn
crepIfPreferredConfig = _CrepIfPreferredConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 8),
    _CrepIfPreferredConfig_Type()
)
crepIfPreferredConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepIfPreferredConfig.setStatus("current")
_CrepifBlockedVlans1k_Type = CiscoVlanList
_CrepifBlockedVlans1k_Object = MibTableColumn
crepifBlockedVlans1k = _CrepifBlockedVlans1k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 9),
    _CrepifBlockedVlans1k_Type()
)
crepifBlockedVlans1k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepifBlockedVlans1k.setStatus("current")
_CrepifBlockedVlans2k_Type = CiscoVlanList
_CrepifBlockedVlans2k_Object = MibTableColumn
crepifBlockedVlans2k = _CrepifBlockedVlans2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 10),
    _CrepifBlockedVlans2k_Type()
)
crepifBlockedVlans2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepifBlockedVlans2k.setStatus("current")
_CrepifBlockedVlans3k_Type = CiscoVlanList
_CrepifBlockedVlans3k_Object = MibTableColumn
crepifBlockedVlans3k = _CrepifBlockedVlans3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 11),
    _CrepifBlockedVlans3k_Type()
)
crepifBlockedVlans3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepifBlockedVlans3k.setStatus("current")
_CrepifBlockedVlans4k_Type = CiscoVlanList
_CrepifBlockedVlans4k_Object = MibTableColumn
crepifBlockedVlans4k = _CrepifBlockedVlans4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 12),
    _CrepifBlockedVlans4k_Type()
)
crepifBlockedVlans4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepifBlockedVlans4k.setStatus("current")


class _CrepLoadBalanceBlockPortType_Type(Integer32):
    """Custom type crepLoadBalanceBlockPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("offset", 2),
          ("portId", 3),
          ("prefFlag", 4))
    )


_CrepLoadBalanceBlockPortType_Type.__name__ = "Integer32"
_CrepLoadBalanceBlockPortType_Object = MibTableColumn
crepLoadBalanceBlockPortType = _CrepLoadBalanceBlockPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 13),
    _CrepLoadBalanceBlockPortType_Type()
)
crepLoadBalanceBlockPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepLoadBalanceBlockPortType.setStatus("current")


class _CrepBlockPortNumInfo_Type(Integer32):
    """Custom type crepBlockPortNumInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-256, 256),
    )


_CrepBlockPortNumInfo_Type.__name__ = "Integer32"
_CrepBlockPortNumInfo_Object = MibTableColumn
crepBlockPortNumInfo = _CrepBlockPortNumInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 14),
    _CrepBlockPortNumInfo_Type()
)
crepBlockPortNumInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepBlockPortNumInfo.setStatus("current")


class _CrepBlockPortIdInfo_Type(OctetString):
    """Custom type crepBlockPortIdInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CrepBlockPortIdInfo_Type.__name__ = "OctetString"
_CrepBlockPortIdInfo_Object = MibTableColumn
crepBlockPortIdInfo = _CrepBlockPortIdInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 15),
    _CrepBlockPortIdInfo_Type()
)
crepBlockPortIdInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepBlockPortIdInfo.setStatus("current")


class _CrepIfPreemptDelayTimer_Type(Integer32):
    """Custom type crepIfPreemptDelayTimer based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_CrepIfPreemptDelayTimer_Type.__name__ = "Integer32"
_CrepIfPreemptDelayTimer_Object = MibTableColumn
crepIfPreemptDelayTimer = _CrepIfPreemptDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 16),
    _CrepIfPreemptDelayTimer_Type()
)
crepIfPreemptDelayTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepIfPreemptDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    crepIfPreemptDelayTimer.setUnits("delay in seconds")


class _CrepIfStcnPropagateToSTP_Type(TruthValue):
    """Custom type crepIfStcnPropagateToSTP based on TruthValue"""


_CrepIfStcnPropagateToSTP_Object = MibTableColumn
crepIfStcnPropagateToSTP = _CrepIfStcnPropagateToSTP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 17),
    _CrepIfStcnPropagateToSTP_Type()
)
crepIfStcnPropagateToSTP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepIfStcnPropagateToSTP.setStatus("current")
_CrepIfStcnPropagateToOtherSegs_Type = RepSegmentList
_CrepIfStcnPropagateToOtherSegs_Object = MibTableColumn
crepIfStcnPropagateToOtherSegs = _CrepIfStcnPropagateToOtherSegs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 18),
    _CrepIfStcnPropagateToOtherSegs_Type()
)
crepIfStcnPropagateToOtherSegs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepIfStcnPropagateToOtherSegs.setStatus("current")


class _CrepIfStcnPropagateToIf_Type(InterfaceIndexOrZero):
    """Custom type crepIfStcnPropagateToIf based on InterfaceIndexOrZero"""
    defaultValue = 0


_CrepIfStcnPropagateToIf_Object = MibTableColumn
crepIfStcnPropagateToIf = _CrepIfStcnPropagateToIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 19),
    _CrepIfStcnPropagateToIf_Type()
)
crepIfStcnPropagateToIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepIfStcnPropagateToIf.setStatus("current")
_CrepIfConfigRowStatus_Type = RowStatus
_CrepIfConfigRowStatus_Object = MibTableColumn
crepIfConfigRowStatus = _CrepIfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 1, 1, 20),
    _CrepIfConfigRowStatus_Type()
)
crepIfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    crepIfConfigRowStatus.setStatus("current")
_CrepInterfaceStatsTable_Object = MibTable
crepInterfaceStatsTable = _CrepInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2)
)
if mibBuilder.loadTexts:
    crepInterfaceStatsTable.setStatus("current")
_CrepInterfaceStatsEntry_Object = MibTableRow
crepInterfaceStatsEntry = _CrepInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    crepInterfaceStatsEntry.setStatus("current")
_CrepCounterDiscontinuityTime_Type = TimeStamp
_CrepCounterDiscontinuityTime_Object = MibTableColumn
crepCounterDiscontinuityTime = _CrepCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 1),
    _CrepCounterDiscontinuityTime_Type()
)
crepCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepCounterDiscontinuityTime.setStatus("current")
_CrepLslRxPdus_Type = Counter32
_CrepLslRxPdus_Object = MibTableColumn
crepLslRxPdus = _CrepLslRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 2),
    _CrepLslRxPdus_Type()
)
crepLslRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepLslRxPdus.setStatus("current")
_CrepLslTxPdus_Type = Counter32
_CrepLslTxPdus_Object = MibTableColumn
crepLslTxPdus = _CrepLslTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 3),
    _CrepLslTxPdus_Type()
)
crepLslTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepLslTxPdus.setStatus("current")
_CrepHflRxPdus_Type = Counter32
_CrepHflRxPdus_Object = MibTableColumn
crepHflRxPdus = _CrepHflRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 4),
    _CrepHflRxPdus_Type()
)
crepHflRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepHflRxPdus.setStatus("current")
_CrepHflTxPdus_Type = Counter32
_CrepHflTxPdus_Object = MibTableColumn
crepHflTxPdus = _CrepHflTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 5),
    _CrepHflTxPdus_Type()
)
crepHflTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepHflTxPdus.setStatus("current")
_CrepBpaTlvRxPackets_Type = Counter32
_CrepBpaTlvRxPackets_Object = MibTableColumn
crepBpaTlvRxPackets = _CrepBpaTlvRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 6),
    _CrepBpaTlvRxPackets_Type()
)
crepBpaTlvRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepBpaTlvRxPackets.setStatus("current")
_CrepBpaTlvTxPackets_Type = Counter32
_CrepBpaTlvTxPackets_Object = MibTableColumn
crepBpaTlvTxPackets = _CrepBpaTlvTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 7),
    _CrepBpaTlvTxPackets_Type()
)
crepBpaTlvTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepBpaTlvTxPackets.setStatus("current")
_CrepBpaStcnLslRxPackets_Type = Counter32
_CrepBpaStcnLslRxPackets_Object = MibTableColumn
crepBpaStcnLslRxPackets = _CrepBpaStcnLslRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 8),
    _CrepBpaStcnLslRxPackets_Type()
)
crepBpaStcnLslRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepBpaStcnLslRxPackets.setStatus("current")
_CrepBpaStcnLslTxPackets_Type = Counter32
_CrepBpaStcnLslTxPackets_Object = MibTableColumn
crepBpaStcnLslTxPackets = _CrepBpaStcnLslTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 9),
    _CrepBpaStcnLslTxPackets_Type()
)
crepBpaStcnLslTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepBpaStcnLslTxPackets.setStatus("current")
_CrepBpaStcnHflRxPackets_Type = Counter32
_CrepBpaStcnHflRxPackets_Object = MibTableColumn
crepBpaStcnHflRxPackets = _CrepBpaStcnHflRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 10),
    _CrepBpaStcnHflRxPackets_Type()
)
crepBpaStcnHflRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepBpaStcnHflRxPackets.setStatus("current")
_CrepBpaStcnHflTxPackets_Type = Counter32
_CrepBpaStcnHflTxPackets_Object = MibTableColumn
crepBpaStcnHflTxPackets = _CrepBpaStcnHflTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 11),
    _CrepBpaStcnHflTxPackets_Type()
)
crepBpaStcnHflTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepBpaStcnHflTxPackets.setStatus("current")
_CrepEpaElectionTlvRxPackets_Type = Counter32
_CrepEpaElectionTlvRxPackets_Object = MibTableColumn
crepEpaElectionTlvRxPackets = _CrepEpaElectionTlvRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 12),
    _CrepEpaElectionTlvRxPackets_Type()
)
crepEpaElectionTlvRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepEpaElectionTlvRxPackets.setStatus("current")
_CrepEpaElectionTlvTxPackets_Type = Counter32
_CrepEpaElectionTlvTxPackets_Object = MibTableColumn
crepEpaElectionTlvTxPackets = _CrepEpaElectionTlvTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 13),
    _CrepEpaElectionTlvTxPackets_Type()
)
crepEpaElectionTlvTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepEpaElectionTlvTxPackets.setStatus("current")
_CrepEpaCommandTlvRxPackets_Type = Counter32
_CrepEpaCommandTlvRxPackets_Object = MibTableColumn
crepEpaCommandTlvRxPackets = _CrepEpaCommandTlvRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 14),
    _CrepEpaCommandTlvRxPackets_Type()
)
crepEpaCommandTlvRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepEpaCommandTlvRxPackets.setStatus("current")
_CrepEpaCommandTlvTxPackets_Type = Counter32
_CrepEpaCommandTlvTxPackets_Object = MibTableColumn
crepEpaCommandTlvTxPackets = _CrepEpaCommandTlvTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 15),
    _CrepEpaCommandTlvTxPackets_Type()
)
crepEpaCommandTlvTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepEpaCommandTlvTxPackets.setStatus("current")
_CrepEpaInfoTlvRxPackets_Type = Counter32
_CrepEpaInfoTlvRxPackets_Object = MibTableColumn
crepEpaInfoTlvRxPackets = _CrepEpaInfoTlvRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 16),
    _CrepEpaInfoTlvRxPackets_Type()
)
crepEpaInfoTlvRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepEpaInfoTlvRxPackets.setStatus("current")
_CrepEpaInfoTlvTxPackets_Type = Counter32
_CrepEpaInfoTlvTxPackets_Object = MibTableColumn
crepEpaInfoTlvTxPackets = _CrepEpaInfoTlvTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 2, 2, 1, 17),
    _CrepEpaInfoTlvTxPackets_Type()
)
crepEpaInfoTlvTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepEpaInfoTlvTxPackets.setStatus("current")
_CrepSegmentConfig_ObjectIdentity = ObjectIdentity
crepSegmentConfig = _CrepSegmentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 3)
)
_CrepSegmentTable_Object = MibTable
crepSegmentTable = _CrepSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 3, 1)
)
if mibBuilder.loadTexts:
    crepSegmentTable.setStatus("current")
_CrepSegmentEntry_Object = MibTableRow
crepSegmentEntry = _CrepSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 3, 1, 1)
)
crepSegmentEntry.setIndexNames(
    (0, "CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepSegmentId"),
)
if mibBuilder.loadTexts:
    crepSegmentEntry.setStatus("current")
_CrepSegmentId_Type = RepSegmentId
_CrepSegmentId_Object = MibTableColumn
crepSegmentId = _CrepSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 3, 1, 1, 1),
    _CrepSegmentId_Type()
)
crepSegmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crepSegmentId.setStatus("current")
_CrepSegmentInterface1_Type = InterfaceIndex
_CrepSegmentInterface1_Object = MibTableColumn
crepSegmentInterface1 = _CrepSegmentInterface1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 3, 1, 1, 2),
    _CrepSegmentInterface1_Type()
)
crepSegmentInterface1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepSegmentInterface1.setStatus("current")
_CrepSegmentInterface2_Type = InterfaceIndexOrZero
_CrepSegmentInterface2_Object = MibTableColumn
crepSegmentInterface2 = _CrepSegmentInterface2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 3, 1, 1, 3),
    _CrepSegmentInterface2_Type()
)
crepSegmentInterface2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepSegmentInterface2.setStatus("current")
_CrepSegmentComplete_Type = TruthValue
_CrepSegmentComplete_Object = MibTableColumn
crepSegmentComplete = _CrepSegmentComplete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 3, 1, 1, 4),
    _CrepSegmentComplete_Type()
)
crepSegmentComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepSegmentComplete.setStatus("current")
_CrepSegmentPreempt_Type = TruthValue
_CrepSegmentPreempt_Object = MibTableColumn
crepSegmentPreempt = _CrepSegmentPreempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 3, 1, 1, 5),
    _CrepSegmentPreempt_Type()
)
crepSegmentPreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crepSegmentPreempt.setStatus("current")


class _CrepSegmentPreemptStatus_Type(Integer32):
    """Custom type crepSegmentPreemptStatus based on Integer32"""
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
        *(("none", 1),
          ("preemptFailure", 3),
          ("preemptSuccessful", 2),
          ("preemptTrigger", 4),
          ("preemptTriggerFailure", 5))
    )


_CrepSegmentPreemptStatus_Type.__name__ = "Integer32"
_CrepSegmentPreemptStatus_Object = MibTableColumn
crepSegmentPreemptStatus = _CrepSegmentPreemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 1, 3, 1, 1, 6),
    _CrepSegmentPreemptStatus_Type()
)
crepSegmentPreemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crepSegmentPreemptStatus.setStatus("current")
_CiscoRepMIBConform_ObjectIdentity = ObjectIdentity
ciscoRepMIBConform = _CiscoRepMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 2)
)
_CiscoRepMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoRepMIBCompliances = _CiscoRepMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 2, 1)
)
_CiscoRepMIBGroups_ObjectIdentity = ObjectIdentity
ciscoRepMIBGroups = _CiscoRepMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 2, 2)
)
crepInterfaceConfigEntry.registerAugmentions(
    ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB",
     "crepInterfaceStatsEntry")
)
crepInterfaceStatsEntry.setIndexNames(*crepInterfaceConfigEntry.getIndexNames())

# Managed Objects groups

ciscoRepGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 2, 2, 1)
)
ciscoRepGlobalGroup.setObjects(
      *(("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepVersion"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepAdminVlan"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepNotifsEnable"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepGlobalRepNotifsRate"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepMinSegmentId"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepMaxSegmentId"))
)
if mibBuilder.loadTexts:
    ciscoRepGlobalGroup.setStatus("current")

ciscoRepInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 2, 2, 2)
)
ciscoRepInterfaceGroup.setObjects(
      *(("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfSegmentId"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfOperStatus"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfPortRole"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfPortID"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfAdminEdgePortType"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfOperEdgePortType"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfPreferredConfig"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepifBlockedVlans1k"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepifBlockedVlans2k"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepifBlockedVlans3k"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepifBlockedVlans4k"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepLoadBalanceBlockPortType"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepBlockPortNumInfo"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepBlockPortIdInfo"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfPreemptDelayTimer"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfStcnPropagateToSTP"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfStcnPropagateToOtherSegs"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfStcnPropagateToIf"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfConfigRowStatus"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepCounterDiscontinuityTime"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepLslRxPdus"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepLslTxPdus"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepHflRxPdus"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepHflTxPdus"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepBpaTlvRxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepBpaTlvTxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepBpaStcnLslRxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepBpaStcnLslTxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepBpaStcnHflRxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepBpaStcnHflTxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepEpaElectionTlvRxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepEpaElectionTlvTxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepEpaCommandTlvRxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepEpaCommandTlvTxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepEpaInfoTlvRxPackets"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepEpaInfoTlvTxPackets"))
)
if mibBuilder.loadTexts:
    ciscoRepInterfaceGroup.setStatus("current")

ciscoRepSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 2, 2, 4)
)
ciscoRepSegmentGroup.setObjects(
      *(("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepSegmentInterface1"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepSegmentInterface2"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepSegmentComplete"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepSegmentPreempt"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepSegmentPreemptStatus"))
)
if mibBuilder.loadTexts:
    ciscoRepSegmentGroup.setStatus("current")


# Notification objects

crepLinkStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 0, 1)
)
crepLinkStatus.setObjects(
      *(("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfSegmentId"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfOperStatus"))
)
if mibBuilder.loadTexts:
    crepLinkStatus.setStatus(
        "current"
    )

crepPreemptionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 0, 2)
)
crepPreemptionStatus.setObjects(
    ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepSegmentPreemptStatus")
)
if mibBuilder.loadTexts:
    crepPreemptionStatus.setStatus(
        "current"
    )

crepPortRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 0, 3)
)
crepPortRoleChange.setObjects(
      *(("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfSegmentId"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepIfPortRole"))
)
if mibBuilder.loadTexts:
    crepPortRoleChange.setStatus(
        "current"
    )


# Notifications groups

ciscoRepNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 2, 2, 3)
)
ciscoRepNotificationGroup.setObjects(
      *(("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepLinkStatus"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepPreemptionStatus"),
        ("CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB", "crepPortRoleChange"))
)
if mibBuilder.loadTexts:
    ciscoRepNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoRepMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 601, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRepMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RESILIENT-ETHERNET-PROTOCOL-MIB",
    **{"RepPortType": RepPortType,
       "RepSegmentId": RepSegmentId,
       "RepSegmentList": RepSegmentList,
       "ciscoResilientEthernetProtocolMIB": ciscoResilientEthernetProtocolMIB,
       "ciscoRepMIBNotifs": ciscoRepMIBNotifs,
       "crepLinkStatus": crepLinkStatus,
       "crepPreemptionStatus": crepPreemptionStatus,
       "crepPortRoleChange": crepPortRoleChange,
       "ciscoRepMIBObjects": ciscoRepMIBObjects,
       "crepGlobalInfo": crepGlobalInfo,
       "crepVersion": crepVersion,
       "crepAdminVlan": crepAdminVlan,
       "crepNotifsEnable": crepNotifsEnable,
       "crepGlobalRepNotifsRate": crepGlobalRepNotifsRate,
       "crepMinSegmentId": crepMinSegmentId,
       "crepMaxSegmentId": crepMaxSegmentId,
       "crepInterfaceConfig": crepInterfaceConfig,
       "crepInterfaceConfigTable": crepInterfaceConfigTable,
       "crepInterfaceConfigEntry": crepInterfaceConfigEntry,
       "crepIfIndex": crepIfIndex,
       "crepIfSegmentId": crepIfSegmentId,
       "crepIfOperStatus": crepIfOperStatus,
       "crepIfPortRole": crepIfPortRole,
       "crepIfPortID": crepIfPortID,
       "crepIfAdminEdgePortType": crepIfAdminEdgePortType,
       "crepIfOperEdgePortType": crepIfOperEdgePortType,
       "crepIfPreferredConfig": crepIfPreferredConfig,
       "crepifBlockedVlans1k": crepifBlockedVlans1k,
       "crepifBlockedVlans2k": crepifBlockedVlans2k,
       "crepifBlockedVlans3k": crepifBlockedVlans3k,
       "crepifBlockedVlans4k": crepifBlockedVlans4k,
       "crepLoadBalanceBlockPortType": crepLoadBalanceBlockPortType,
       "crepBlockPortNumInfo": crepBlockPortNumInfo,
       "crepBlockPortIdInfo": crepBlockPortIdInfo,
       "crepIfPreemptDelayTimer": crepIfPreemptDelayTimer,
       "crepIfStcnPropagateToSTP": crepIfStcnPropagateToSTP,
       "crepIfStcnPropagateToOtherSegs": crepIfStcnPropagateToOtherSegs,
       "crepIfStcnPropagateToIf": crepIfStcnPropagateToIf,
       "crepIfConfigRowStatus": crepIfConfigRowStatus,
       "crepInterfaceStatsTable": crepInterfaceStatsTable,
       "crepInterfaceStatsEntry": crepInterfaceStatsEntry,
       "crepCounterDiscontinuityTime": crepCounterDiscontinuityTime,
       "crepLslRxPdus": crepLslRxPdus,
       "crepLslTxPdus": crepLslTxPdus,
       "crepHflRxPdus": crepHflRxPdus,
       "crepHflTxPdus": crepHflTxPdus,
       "crepBpaTlvRxPackets": crepBpaTlvRxPackets,
       "crepBpaTlvTxPackets": crepBpaTlvTxPackets,
       "crepBpaStcnLslRxPackets": crepBpaStcnLslRxPackets,
       "crepBpaStcnLslTxPackets": crepBpaStcnLslTxPackets,
       "crepBpaStcnHflRxPackets": crepBpaStcnHflRxPackets,
       "crepBpaStcnHflTxPackets": crepBpaStcnHflTxPackets,
       "crepEpaElectionTlvRxPackets": crepEpaElectionTlvRxPackets,
       "crepEpaElectionTlvTxPackets": crepEpaElectionTlvTxPackets,
       "crepEpaCommandTlvRxPackets": crepEpaCommandTlvRxPackets,
       "crepEpaCommandTlvTxPackets": crepEpaCommandTlvTxPackets,
       "crepEpaInfoTlvRxPackets": crepEpaInfoTlvRxPackets,
       "crepEpaInfoTlvTxPackets": crepEpaInfoTlvTxPackets,
       "crepSegmentConfig": crepSegmentConfig,
       "crepSegmentTable": crepSegmentTable,
       "crepSegmentEntry": crepSegmentEntry,
       "crepSegmentId": crepSegmentId,
       "crepSegmentInterface1": crepSegmentInterface1,
       "crepSegmentInterface2": crepSegmentInterface2,
       "crepSegmentComplete": crepSegmentComplete,
       "crepSegmentPreempt": crepSegmentPreempt,
       "crepSegmentPreemptStatus": crepSegmentPreemptStatus,
       "ciscoRepMIBConform": ciscoRepMIBConform,
       "ciscoRepMIBCompliances": ciscoRepMIBCompliances,
       "ciscoRepMIBCompliance": ciscoRepMIBCompliance,
       "ciscoRepMIBGroups": ciscoRepMIBGroups,
       "ciscoRepGlobalGroup": ciscoRepGlobalGroup,
       "ciscoRepInterfaceGroup": ciscoRepInterfaceGroup,
       "ciscoRepNotificationGroup": ciscoRepNotificationGroup,
       "ciscoRepSegmentGroup": ciscoRepSegmentGroup}
)
