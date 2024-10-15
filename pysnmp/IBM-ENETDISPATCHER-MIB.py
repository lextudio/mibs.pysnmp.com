# SNMP MIB module (IBM-ENETDISPATCHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-ENETDISPATCHER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:28 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class Percentages(Integer32):
    """Custom type Percentages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )





class GaugeNeg1(Integer32):
    """Custom type GaugeNeg1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DispatcherMib_ObjectIdentity = ObjectIdentity
dispatcherMib = _DispatcherMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1)
)
_DispatcherMibTraps_ObjectIdentity = ObjectIdentity
dispatcherMibTraps = _DispatcherMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 0)
)
_DispatcherMibAdmin_ObjectIdentity = ObjectIdentity
dispatcherMibAdmin = _DispatcherMibAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 1)
)
_DispatcherMibObjects_ObjectIdentity = ObjectIdentity
dispatcherMibObjects = _DispatcherMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2)
)
_IndStatus_ObjectIdentity = ObjectIdentity
indStatus = _IndStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1)
)
_IndExecStatObjects_ObjectIdentity = ObjectIdentity
indExecStatObjects = _IndExecStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1)
)
_EsNonForAddr_Type = IpAddress
_EsNonForAddr_Object = MibScalar
esNonForAddr = _EsNonForAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 1),
    _EsNonForAddr_Type()
)
esNonForAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNonForAddr.setStatus("mandatory")
_EsVersion_Type = DisplayString
_EsVersion_Object = MibScalar
esVersion = _EsVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 2),
    _EsVersion_Type()
)
esVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esVersion.setStatus("mandatory")
_EsNumClust_Type = Gauge32
_EsNumClust_Object = MibScalar
esNumClust = _EsNumClust_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 3),
    _EsNumClust_Type()
)
esNumClust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumClust.setStatus("mandatory")
_EsTotalPkts_Type = Counter32
_EsTotalPkts_Object = MibScalar
esTotalPkts = _EsTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 4),
    _EsTotalPkts_Type()
)
esTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTotalPkts.setStatus("mandatory")
_EsTooShortPkts_Type = Counter32
_EsTooShortPkts_Object = MibScalar
esTooShortPkts = _EsTooShortPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 5),
    _EsTooShortPkts_Type()
)
esTooShortPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTooShortPkts.setStatus("mandatory")
_EsNonForPkts_Type = Counter32
_EsNonForPkts_Object = MibScalar
esNonForPkts = _EsNonForPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 6),
    _EsNonForPkts_Type()
)
esNonForPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNonForPkts.setStatus("mandatory")
_EsClstrDscrdPkts_Type = Counter32
_EsClstrDscrdPkts_Object = MibScalar
esClstrDscrdPkts = _EsClstrDscrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 7),
    _EsClstrDscrdPkts_Type()
)
esClstrDscrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esClstrDscrdPkts.setStatus("mandatory")
_EsClstrErrPkts_Type = Counter32
_EsClstrErrPkts_Object = MibScalar
esClstrErrPkts = _EsClstrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 8),
    _EsClstrErrPkts_Type()
)
esClstrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esClstrErrPkts.setStatus("mandatory")
_EsClstrLocalPkts_Type = Counter32
_EsClstrLocalPkts_Object = MibScalar
esClstrLocalPkts = _EsClstrLocalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 9),
    _EsClstrLocalPkts_Type()
)
esClstrLocalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esClstrLocalPkts.setStatus("mandatory")
_EsClstrOwnAddrPkts_Type = Counter32
_EsClstrOwnAddrPkts_Object = MibScalar
esClstrOwnAddrPkts = _EsClstrOwnAddrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 10),
    _EsClstrOwnAddrPkts_Type()
)
esClstrOwnAddrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esClstrOwnAddrPkts.setStatus("mandatory")
_EsClstrForPkts_Type = Counter32
_EsClstrForPkts_Object = MibScalar
esClstrForPkts = _EsClstrForPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 11),
    _EsClstrForPkts_Type()
)
esClstrForPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esClstrForPkts.setStatus("mandatory")
_EsForErrPkts_Type = Counter32
_EsForErrPkts_Object = MibScalar
esForErrPkts = _EsForErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 12),
    _EsForErrPkts_Type()
)
esForErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esForErrPkts.setStatus("mandatory")
_EsNotClstrPkts_Type = Counter32
_EsNotClstrPkts_Object = MibScalar
esNotClstrPkts = _EsNotClstrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 13),
    _EsNotClstrPkts_Type()
)
esNotClstrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNotClstrPkts.setStatus("mandatory")
_EsHashBkts_Type = Gauge32
_EsHashBkts_Object = MibScalar
esHashBkts = _EsHashBkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 14),
    _EsHashBkts_Type()
)
esHashBkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esHashBkts.setStatus("mandatory")
_EsStartTime_Type = Counter32
_EsStartTime_Object = MibScalar
esStartTime = _EsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 1, 15),
    _EsStartTime_Type()
)
esStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esStartTime.setStatus("mandatory")
_IndClstrStatTable_Object = MibTable
indClstrStatTable = _IndClstrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    indClstrStatTable.setStatus("mandatory")
_IndClstrStatEntry_Object = MibTableRow
indClstrStatEntry = _IndClstrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 2, 1)
)
indClstrStatEntry.setIndexNames(
    (0, "IBM-ENETDISPATCHER-MIB", "csAddr"),
)
if mibBuilder.loadTexts:
    indClstrStatEntry.setStatus("mandatory")
_CsAddr_Type = IpAddress
_CsAddr_Object = MibTableColumn
csAddr = _CsAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 2, 1, 1),
    _CsAddr_Type()
)
csAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csAddr.setStatus("mandatory")
_CsNumPorts_Type = Gauge32
_CsNumPorts_Object = MibTableColumn
csNumPorts = _CsNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 2, 1, 2),
    _CsNumPorts_Type()
)
csNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csNumPorts.setStatus("mandatory")
_CsActiveSYNs_Type = Counter32
_CsActiveSYNs_Object = MibTableColumn
csActiveSYNs = _CsActiveSYNs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 2, 1, 3),
    _CsActiveSYNs_Type()
)
csActiveSYNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csActiveSYNs.setStatus("mandatory")
_CsDroppedFINs_Type = Counter32
_CsDroppedFINs_Object = MibTableColumn
csDroppedFINs = _CsDroppedFINs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 2, 1, 4),
    _CsDroppedFINs_Type()
)
csDroppedFINs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csDroppedFINs.setStatus("mandatory")
_CsDroppedACKs_Type = Counter32
_CsDroppedACKs_Object = MibTableColumn
csDroppedACKs = _CsDroppedACKs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 2, 1, 5),
    _CsDroppedACKs_Type()
)
csDroppedACKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csDroppedACKs.setStatus("mandatory")
_CsDroppedRSTs_Type = Counter32
_CsDroppedRSTs_Object = MibTableColumn
csDroppedRSTs = _CsDroppedRSTs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 2, 1, 6),
    _CsDroppedRSTs_Type()
)
csDroppedRSTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csDroppedRSTs.setStatus("mandatory")
_CsDroppedPKTs_Type = Counter32
_CsDroppedPKTs_Object = MibTableColumn
csDroppedPKTs = _CsDroppedPKTs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 2, 1, 7),
    _CsDroppedPKTs_Type()
)
csDroppedPKTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csDroppedPKTs.setStatus("mandatory")
_CsNonExistingPKTs_Type = Counter32
_CsNonExistingPKTs_Object = MibTableColumn
csNonExistingPKTs = _CsNonExistingPKTs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 2, 1, 8),
    _CsNonExistingPKTs_Type()
)
csNonExistingPKTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csNonExistingPKTs.setStatus("deprecated")
_IndPortStatTable_Object = MibTable
indPortStatTable = _IndPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    indPortStatTable.setStatus("mandatory")
_IndPortStatEntry_Object = MibTableRow
indPortStatEntry = _IndPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 3, 1)
)
indPortStatEntry.setIndexNames(
    (0, "IBM-ENETDISPATCHER-MIB", "csAddr"),
    (0, "IBM-ENETDISPATCHER-MIB", "psNum"),
)
if mibBuilder.loadTexts:
    indPortStatEntry.setStatus("mandatory")


class _PsNum_Type(Integer32):
    """Custom type psNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PsNum_Type.__name__ = "Integer32"
_PsNum_Object = MibTableColumn
psNum = _PsNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 3, 1, 1),
    _PsNum_Type()
)
psNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psNum.setStatus("mandatory")
_PsNumServers_Type = Gauge32
_PsNumServers_Object = MibTableColumn
psNumServers = _PsNumServers_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 3, 1, 2),
    _PsNumServers_Type()
)
psNumServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psNumServers.setStatus("mandatory")
_PsNumNodesDown_Type = Gauge32
_PsNumNodesDown_Object = MibTableColumn
psNumNodesDown = _PsNumNodesDown_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 3, 1, 3),
    _PsNumNodesDown_Type()
)
psNumNodesDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psNumNodesDown.setStatus("mandatory")
_IndSrvrStatTable_Object = MibTable
indSrvrStatTable = _IndSrvrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    indSrvrStatTable.setStatus("mandatory")
_IndSrvrStatEntry_Object = MibTableRow
indSrvrStatEntry = _IndSrvrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1)
)
indSrvrStatEntry.setIndexNames(
    (0, "IBM-ENETDISPATCHER-MIB", "csAddr"),
    (0, "IBM-ENETDISPATCHER-MIB", "psNum"),
    (0, "IBM-ENETDISPATCHER-MIB", "ssAddr"),
)
if mibBuilder.loadTexts:
    indSrvrStatEntry.setStatus("mandatory")
_SsAddr_Type = IpAddress
_SsAddr_Object = MibTableColumn
ssAddr = _SsAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 1),
    _SsAddr_Type()
)
ssAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssAddr.setStatus("mandatory")
_SsActiveConns_Type = Gauge32
_SsActiveConns_Object = MibTableColumn
ssActiveConns = _SsActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 2),
    _SsActiveConns_Type()
)
ssActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssActiveConns.setStatus("mandatory")
_SsNewConns_Type = Gauge32
_SsNewConns_Object = MibTableColumn
ssNewConns = _SsNewConns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 3),
    _SsNewConns_Type()
)
ssNewConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNewConns.setStatus("mandatory")
_SsTotalConns_Type = Counter32
_SsTotalConns_Object = MibTableColumn
ssTotalConns = _SsTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 4),
    _SsTotalConns_Type()
)
ssTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssTotalConns.setStatus("mandatory")
_SsTotalTcpConns_Type = Counter32
_SsTotalTcpConns_Object = MibTableColumn
ssTotalTcpConns = _SsTotalTcpConns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 5),
    _SsTotalTcpConns_Type()
)
ssTotalTcpConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssTotalTcpConns.setStatus("mandatory")
_SsTotalUdpConns_Type = Counter32
_SsTotalUdpConns_Object = MibTableColumn
ssTotalUdpConns = _SsTotalUdpConns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 6),
    _SsTotalUdpConns_Type()
)
ssTotalUdpConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssTotalUdpConns.setStatus("mandatory")
_SsFinConns_Type = Gauge32
_SsFinConns_Object = MibTableColumn
ssFinConns = _SsFinConns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 7),
    _SsFinConns_Type()
)
ssFinConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssFinConns.setStatus("mandatory")
_SsCompleteConns_Type = Counter32
_SsCompleteConns_Object = MibTableColumn
ssCompleteConns = _SsCompleteConns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 8),
    _SsCompleteConns_Type()
)
ssCompleteConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCompleteConns.setStatus("mandatory")
_SsWeight_Type = GaugeNeg1
_SsWeight_Object = MibTableColumn
ssWeight = _SsWeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 9),
    _SsWeight_Type()
)
ssWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssWeight.setStatus("mandatory")
_SsSavedWeight_Type = GaugeNeg1
_SsSavedWeight_Object = MibTableColumn
ssSavedWeight = _SsSavedWeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 10),
    _SsSavedWeight_Type()
)
ssSavedWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSavedWeight.setStatus("mandatory")
_SsPortLoad_Type = GaugeNeg1
_SsPortLoad_Object = MibTableColumn
ssPortLoad = _SsPortLoad_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 11),
    _SsPortLoad_Type()
)
ssPortLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssPortLoad.setStatus("mandatory")
_SsSystemLoad_Type = Integer32
_SsSystemLoad_Object = MibTableColumn
ssSystemLoad = _SsSystemLoad_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 12),
    _SsSystemLoad_Type()
)
ssSystemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSystemLoad.setStatus("mandatory")
_SsActiveConnsWeight_Type = Integer32
_SsActiveConnsWeight_Object = MibTableColumn
ssActiveConnsWeight = _SsActiveConnsWeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 13),
    _SsActiveConnsWeight_Type()
)
ssActiveConnsWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssActiveConnsWeight.setStatus("mandatory")
_SsNewConnsWeight_Type = Integer32
_SsNewConnsWeight_Object = MibTableColumn
ssNewConnsWeight = _SsNewConnsWeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 14),
    _SsNewConnsWeight_Type()
)
ssNewConnsWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssNewConnsWeight.setStatus("mandatory")
_SsPortLoadWeight_Type = Integer32
_SsPortLoadWeight_Object = MibTableColumn
ssPortLoadWeight = _SsPortLoadWeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 15),
    _SsPortLoadWeight_Type()
)
ssPortLoadWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssPortLoadWeight.setStatus("mandatory")
_SsSystemLoadWeight_Type = Integer32
_SsSystemLoadWeight_Object = MibTableColumn
ssSystemLoadWeight = _SsSystemLoadWeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 4, 1, 16),
    _SsSystemLoadWeight_Type()
)
ssSystemLoadWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSystemLoadWeight.setStatus("mandatory")
_IndRulesStatTable_Object = MibTable
indRulesStatTable = _IndRulesStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    indRulesStatTable.setStatus("mandatory")
_IndRulesStatEntry_Object = MibTableRow
indRulesStatEntry = _IndRulesStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 5, 1)
)
indRulesStatEntry.setIndexNames(
    (0, "IBM-ENETDISPATCHER-MIB", "csAddr"),
    (0, "IBM-ENETDISPATCHER-MIB", "psNum"),
    (0, "IBM-ENETDISPATCHER-MIB", "rcIndex"),
)
if mibBuilder.loadTexts:
    indRulesStatEntry.setStatus("mandatory")
_RsTimesFired_Type = Counter32
_RsTimesFired_Object = MibTableColumn
rsTimesFired = _RsTimesFired_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 5, 1, 2),
    _RsTimesFired_Type()
)
rsTimesFired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTimesFired.setStatus("mandatory")
_RsNumSrvrs_Type = Gauge32
_RsNumSrvrs_Object = MibTableColumn
rsNumSrvrs = _RsNumSrvrs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 5, 1, 3),
    _RsNumSrvrs_Type()
)
rsNumSrvrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNumSrvrs.setStatus("mandatory")
_IndHiAvailStatObjects_ObjectIdentity = ObjectIdentity
indHiAvailStatObjects = _IndHiAvailStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 6)
)


class _HasPrimary_Type(Integer32):
    """Custom type hasPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("primary", 0))
    )


_HasPrimary_Type.__name__ = "Integer32"
_HasPrimary_Object = MibScalar
hasPrimary = _HasPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 6, 1),
    _HasPrimary_Type()
)
hasPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hasPrimary.setStatus("mandatory")


class _HasPort_Type(Integer32):
    """Custom type hasPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HasPort_Type.__name__ = "Integer32"
_HasPort_Object = MibScalar
hasPort = _HasPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 6, 2),
    _HasPort_Type()
)
hasPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hasPort.setStatus("mandatory")


class _HasState_Type(Integer32):
    """Custom type hasState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("elect", 5),
          ("idle", 0),
          ("listen", 1),
          ("noExec", 6),
          ("preempt", 4),
          ("standby", 3))
    )


_HasState_Type.__name__ = "Integer32"
_HasState_Object = MibScalar
hasState = _HasState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 6, 3),
    _HasState_Type()
)
hasState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hasState.setStatus("mandatory")


class _HasSubState_Type(Integer32):
    """Custom type hasSubState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSynchronized", 0),
          ("syncIn", 2),
          ("syncOut", 3),
          ("synchronized", 1))
    )


_HasSubState_Type.__name__ = "Integer32"
_HasSubState_Object = MibScalar
hasSubState = _HasSubState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 6, 4),
    _HasSubState_Type()
)
hasSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hasSubState.setStatus("mandatory")
_IndReachStatTable_Object = MibTable
indReachStatTable = _IndReachStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    indReachStatTable.setStatus("mandatory")
_IndReachStatEntry_Object = MibTableRow
indReachStatEntry = _IndReachStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 7, 1)
)
indReachStatEntry.setIndexNames(
    (0, "IBM-ENETDISPATCHER-MIB", "rsAddr"),
)
if mibBuilder.loadTexts:
    indReachStatEntry.setStatus("mandatory")
_RsAddr_Type = IpAddress
_RsAddr_Object = MibTableColumn
rsAddr = _RsAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 7, 1, 1),
    _RsAddr_Type()
)
rsAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsAddr.setStatus("mandatory")


class _RsPingAble_Type(Integer32):
    """Custom type rsPingAble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unknown", 0),
          ("unreachable", 2))
    )


_RsPingAble_Type.__name__ = "Integer32"
_RsPingAble_Object = MibTableColumn
rsPingAble = _RsPingAble_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 1, 7, 1, 2),
    _RsPingAble_Type()
)
rsPingAble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingAble.setStatus("mandatory")
_IndConfig_ObjectIdentity = ObjectIdentity
indConfig = _IndConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2)
)
_IndExecCnfgObjects_ObjectIdentity = ObjectIdentity
indExecCnfgObjects = _IndExecCnfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 1)
)
_IndClstrCnfgTable_ObjectIdentity = ObjectIdentity
indClstrCnfgTable = _IndClstrCnfgTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 2)
)
_IndPortCnfgTable_ObjectIdentity = ObjectIdentity
indPortCnfgTable = _IndPortCnfgTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 3)
)
_IndSrvrCnfgTable_ObjectIdentity = ObjectIdentity
indSrvrCnfgTable = _IndSrvrCnfgTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 4)
)
_IndRulesCnfgTable_Object = MibTable
indRulesCnfgTable = _IndRulesCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    indRulesCnfgTable.setStatus("mandatory")
_IndRulesCnfgEntry_Object = MibTableRow
indRulesCnfgEntry = _IndRulesCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 5, 1)
)
indRulesCnfgEntry.setIndexNames(
    (0, "IBM-ENETDISPATCHER-MIB", "csAddr"),
    (0, "IBM-ENETDISPATCHER-MIB", "psNum"),
    (0, "IBM-ENETDISPATCHER-MIB", "rcIndex"),
)
if mibBuilder.loadTexts:
    indRulesCnfgEntry.setStatus("mandatory")


class _RcIndex_Type(Integer32):
    """Custom type rcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RcIndex_Type.__name__ = "Integer32"
_RcIndex_Object = MibTableColumn
rcIndex = _RcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 5, 1, 1),
    _RcIndex_Type()
)
rcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIndex.setStatus("mandatory")
_RcName_Type = DisplayString
_RcName_Object = MibTableColumn
rcName = _RcName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 5, 1, 2),
    _RcName_Type()
)
rcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcName.setStatus("mandatory")


class _RcType_Type(Integer32):
    """Custom type rcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 5),
          ("connection", 4),
          ("ip", 1),
          ("port", 2),
          ("time", 3),
          ("true", 0))
    )


_RcType_Type.__name__ = "Integer32"
_RcType_Object = MibTableColumn
rcType = _RcType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 5, 1, 3),
    _RcType_Type()
)
rcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcType.setStatus("mandatory")
_RcBeginRange_Type = Integer32
_RcBeginRange_Object = MibTableColumn
rcBeginRange = _RcBeginRange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 5, 1, 4),
    _RcBeginRange_Type()
)
rcBeginRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcBeginRange.setStatus("mandatory")
_RcEndRange_Type = Integer32
_RcEndRange_Object = MibTableColumn
rcEndRange = _RcEndRange_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 5, 1, 5),
    _RcEndRange_Type()
)
rcEndRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEndRange.setStatus("mandatory")
_RcPriority_Type = Integer32
_RcPriority_Object = MibTableColumn
rcPriority = _RcPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 5, 1, 6),
    _RcPriority_Type()
)
rcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPriority.setStatus("mandatory")
_RcSrvrList_Type = DisplayString
_RcSrvrList_Object = MibTableColumn
rcSrvrList = _RcSrvrList_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 5, 1, 7),
    _RcSrvrList_Type()
)
rcSrvrList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSrvrList.setStatus("mandatory")
_IndHiAvailCnfgObjects_ObjectIdentity = ObjectIdentity
indHiAvailCnfgObjects = _IndHiAvailCnfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 6)
)
_IndReachCnfgTable_ObjectIdentity = ObjectIdentity
indReachCnfgTable = _IndReachCnfgTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 7)
)
_IndHrtBeatCnfgTable_Object = MibTable
indHrtBeatCnfgTable = _IndHrtBeatCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    indHrtBeatCnfgTable.setStatus("mandatory")
_IndHrtBeatCnfgEntry_Object = MibTableRow
indHrtBeatCnfgEntry = _IndHrtBeatCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 8, 1)
)
indHrtBeatCnfgEntry.setIndexNames(
    (0, "IBM-ENETDISPATCHER-MIB", "hbcSrcAddr"),
    (0, "IBM-ENETDISPATCHER-MIB", "hbcDestAddr"),
)
if mibBuilder.loadTexts:
    indHrtBeatCnfgEntry.setStatus("mandatory")
_HbcSrcAddr_Type = IpAddress
_HbcSrcAddr_Object = MibTableColumn
hbcSrcAddr = _HbcSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 8, 1, 1),
    _HbcSrcAddr_Type()
)
hbcSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hbcSrcAddr.setStatus("mandatory")
_HbcDestAddr_Type = IpAddress
_HbcDestAddr_Object = MibTableColumn
hbcDestAddr = _HbcDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 8, 1, 2),
    _HbcDestAddr_Type()
)
hbcDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hbcDestAddr.setStatus("mandatory")


class _HbcNumber_Type(Integer32):
    """Custom type hbcNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HbcNumber_Type.__name__ = "Integer32"
_HbcNumber_Object = MibTableColumn
hbcNumber = _HbcNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 8, 1, 3),
    _HbcNumber_Type()
)
hbcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbcNumber.setStatus("mandatory")
_IndAdvsrCnfgTable_Object = MibTable
indAdvsrCnfgTable = _IndAdvsrCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    indAdvsrCnfgTable.setStatus("mandatory")
_IndAdvsrCnfgEntry_Object = MibTableRow
indAdvsrCnfgEntry = _IndAdvsrCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 9, 1)
)
indAdvsrCnfgEntry.setIndexNames(
    (0, "IBM-ENETDISPATCHER-MIB", "acPort"),
)
if mibBuilder.loadTexts:
    indAdvsrCnfgEntry.setStatus("mandatory")


class _AcPort_Type(Integer32):
    """Custom type acPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPort_Type.__name__ = "Integer32"
_AcPort_Object = MibTableColumn
acPort = _AcPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 9, 1, 1),
    _AcPort_Type()
)
acPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPort.setStatus("mandatory")
_AcName_Type = DisplayString
_AcName_Object = MibTableColumn
acName = _AcName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 9, 1, 2),
    _AcName_Type()
)
acName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acName.setStatus("mandatory")
_AcVersion_Type = DisplayString
_AcVersion_Object = MibTableColumn
acVersion = _AcVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 9, 1, 3),
    _AcVersion_Type()
)
acVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acVersion.setStatus("mandatory")
_IndMngrCnfgObjects_ObjectIdentity = ObjectIdentity
indMngrCnfgObjects = _IndMngrCnfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 10)
)


class _McInterval_Type(Integer32):
    """Custom type mcInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_McInterval_Type.__name__ = "Integer32"
_McInterval_Object = MibScalar
mcInterval = _McInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 10, 1),
    _McInterval_Type()
)
mcInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcInterval.setStatus("mandatory")


class _McRefresh_Type(Integer32):
    """Custom type mcRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_McRefresh_Type.__name__ = "Integer32"
_McRefresh_Object = MibScalar
mcRefresh = _McRefresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 10, 2),
    _McRefresh_Type()
)
mcRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcRefresh.setStatus("mandatory")
_McActiveProp_Type = Percentages
_McActiveProp_Object = MibScalar
mcActiveProp = _McActiveProp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 10, 3),
    _McActiveProp_Type()
)
mcActiveProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcActiveProp.setStatus("mandatory")
_McNewProp_Type = Percentages
_McNewProp_Object = MibScalar
mcNewProp = _McNewProp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 10, 4),
    _McNewProp_Type()
)
mcNewProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcNewProp.setStatus("mandatory")
_McPortProp_Type = Percentages
_McPortProp_Object = MibScalar
mcPortProp = _McPortProp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 10, 5),
    _McPortProp_Type()
)
mcPortProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcPortProp.setStatus("mandatory")
_McSystemProp_Type = Percentages
_McSystemProp_Object = MibScalar
mcSystemProp = _McSystemProp_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 10, 6),
    _McSystemProp_Type()
)
mcSystemProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcSystemProp.setStatus("mandatory")
_McSensitivity_Type = Percentages
_McSensitivity_Object = MibScalar
mcSensitivity = _McSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 10, 7),
    _McSensitivity_Type()
)
mcSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcSensitivity.setStatus("mandatory")
_McSmoothing_Type = Percentages
_McSmoothing_Object = MibScalar
mcSmoothing = _McSmoothing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 10, 8),
    _McSmoothing_Type()
)
mcSmoothing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcSmoothing.setStatus("mandatory")
_McVersion_Type = DisplayString
_McVersion_Object = MibScalar
mcVersion = _McVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 10, 9),
    _McVersion_Type()
)
mcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcVersion.setStatus("mandatory")
_IndAllSrvrsCnfgTable_Object = MibTable
indAllSrvrsCnfgTable = _IndAllSrvrsCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 11)
)
if mibBuilder.loadTexts:
    indAllSrvrsCnfgTable.setStatus("mandatory")
_IndAllSrvrsCnfgEntry_Object = MibTableRow
indAllSrvrsCnfgEntry = _IndAllSrvrsCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 11, 1)
)
indAllSrvrsCnfgEntry.setIndexNames(
    (0, "IBM-ENETDISPATCHER-MIB", "ascAddr"),
)
if mibBuilder.loadTexts:
    indAllSrvrsCnfgEntry.setStatus("mandatory")
_AscAddr_Type = IpAddress
_AscAddr_Object = MibTableColumn
ascAddr = _AscAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 11, 1, 1),
    _AscAddr_Type()
)
ascAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ascAddr.setStatus("mandatory")
_AscQuiesced_Type = TruthValue
_AscQuiesced_Object = MibTableColumn
ascQuiesced = _AscQuiesced_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 11, 1, 2),
    _AscQuiesced_Type()
)
ascQuiesced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascQuiesced.setStatus("mandatory")
_AscInstances_Type = Gauge32
_AscInstances_Object = MibTableColumn
ascInstances = _AscInstances_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 2, 2, 11, 1, 3),
    _AscInstances_Type()
)
ascInstances.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascInstances.setStatus("mandatory")
_DispatcherMibConformance_ObjectIdentity = ObjectIdentity
dispatcherMibConformance = _DispatcherMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3)
)
_IndMibCompliances_ObjectIdentity = ObjectIdentity
indMibCompliances = _IndMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 1)
)
_IndMibCompliance_ObjectIdentity = ObjectIdentity
indMibCompliance = _IndMibCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 1, 1)
)
_IndMibGroups_ObjectIdentity = ObjectIdentity
indMibGroups = _IndMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2)
)
_IndMibStatGroups_ObjectIdentity = ObjectIdentity
indMibStatGroups = _IndMibStatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 1)
)
_IndMibExecStatGroup_ObjectIdentity = ObjectIdentity
indMibExecStatGroup = _IndMibExecStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 1, 1)
)
_IndMibClstrStatGroup_ObjectIdentity = ObjectIdentity
indMibClstrStatGroup = _IndMibClstrStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 1, 2)
)
_IndMibPortStatGroup_ObjectIdentity = ObjectIdentity
indMibPortStatGroup = _IndMibPortStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 1, 3)
)
_IndMibSrvrStatGroup_ObjectIdentity = ObjectIdentity
indMibSrvrStatGroup = _IndMibSrvrStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 1, 4)
)
_IndMibRulesStatGroup_ObjectIdentity = ObjectIdentity
indMibRulesStatGroup = _IndMibRulesStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 1, 5)
)
_IndMibHiAvailStatGroup_ObjectIdentity = ObjectIdentity
indMibHiAvailStatGroup = _IndMibHiAvailStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 1, 6)
)
_IndMibReachStatGroup_ObjectIdentity = ObjectIdentity
indMibReachStatGroup = _IndMibReachStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 1, 7)
)
_IndMibCnfgGroups_ObjectIdentity = ObjectIdentity
indMibCnfgGroups = _IndMibCnfgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 2)
)
_IndMibRulesCnfgGroup_ObjectIdentity = ObjectIdentity
indMibRulesCnfgGroup = _IndMibRulesCnfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 2, 5)
)
_IndMibHrtBeatCnfgGroup_ObjectIdentity = ObjectIdentity
indMibHrtBeatCnfgGroup = _IndMibHrtBeatCnfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 2, 8)
)
_IndMibAdvsrCnfgGroup_ObjectIdentity = ObjectIdentity
indMibAdvsrCnfgGroup = _IndMibAdvsrCnfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 2, 9)
)
_IndMibMngrCnfgGroup_ObjectIdentity = ObjectIdentity
indMibMngrCnfgGroup = _IndMibMngrCnfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 2, 10)
)
_IndMibAllSrvrsCnfgGroup_ObjectIdentity = ObjectIdentity
indMibAllSrvrsCnfgGroup = _IndMibAllSrvrsCnfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 3, 2, 2, 11)
)

# Managed Objects groups


# Notification objects

indHighAvailStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 0, 1)
)
indHighAvailStatus.setObjects(
    ("IBM-ENETDISPATCHER-MIB", "hasState")
)
if mibBuilder.loadTexts:
    indHighAvailStatus.setStatus(
        ""
    )

indSrvrGoneDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 144, 1, 0, 2)
)
indSrvrGoneDown.setObjects(
    ("IBM-ENETDISPATCHER-MIB", "ssActiveConns")
)
if mibBuilder.loadTexts:
    indSrvrGoneDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-ENETDISPATCHER-MIB",
    **{"Percentages": Percentages,
       "GaugeNeg1": GaugeNeg1,
       "dispatcherMib": dispatcherMib,
       "dispatcherMibTraps": dispatcherMibTraps,
       "indHighAvailStatus": indHighAvailStatus,
       "indSrvrGoneDown": indSrvrGoneDown,
       "dispatcherMibAdmin": dispatcherMibAdmin,
       "dispatcherMibObjects": dispatcherMibObjects,
       "indStatus": indStatus,
       "indExecStatObjects": indExecStatObjects,
       "esNonForAddr": esNonForAddr,
       "esVersion": esVersion,
       "esNumClust": esNumClust,
       "esTotalPkts": esTotalPkts,
       "esTooShortPkts": esTooShortPkts,
       "esNonForPkts": esNonForPkts,
       "esClstrDscrdPkts": esClstrDscrdPkts,
       "esClstrErrPkts": esClstrErrPkts,
       "esClstrLocalPkts": esClstrLocalPkts,
       "esClstrOwnAddrPkts": esClstrOwnAddrPkts,
       "esClstrForPkts": esClstrForPkts,
       "esForErrPkts": esForErrPkts,
       "esNotClstrPkts": esNotClstrPkts,
       "esHashBkts": esHashBkts,
       "esStartTime": esStartTime,
       "indClstrStatTable": indClstrStatTable,
       "indClstrStatEntry": indClstrStatEntry,
       "csAddr": csAddr,
       "csNumPorts": csNumPorts,
       "csActiveSYNs": csActiveSYNs,
       "csDroppedFINs": csDroppedFINs,
       "csDroppedACKs": csDroppedACKs,
       "csDroppedRSTs": csDroppedRSTs,
       "csDroppedPKTs": csDroppedPKTs,
       "csNonExistingPKTs": csNonExistingPKTs,
       "indPortStatTable": indPortStatTable,
       "indPortStatEntry": indPortStatEntry,
       "psNum": psNum,
       "psNumServers": psNumServers,
       "psNumNodesDown": psNumNodesDown,
       "indSrvrStatTable": indSrvrStatTable,
       "indSrvrStatEntry": indSrvrStatEntry,
       "ssAddr": ssAddr,
       "ssActiveConns": ssActiveConns,
       "ssNewConns": ssNewConns,
       "ssTotalConns": ssTotalConns,
       "ssTotalTcpConns": ssTotalTcpConns,
       "ssTotalUdpConns": ssTotalUdpConns,
       "ssFinConns": ssFinConns,
       "ssCompleteConns": ssCompleteConns,
       "ssWeight": ssWeight,
       "ssSavedWeight": ssSavedWeight,
       "ssPortLoad": ssPortLoad,
       "ssSystemLoad": ssSystemLoad,
       "ssActiveConnsWeight": ssActiveConnsWeight,
       "ssNewConnsWeight": ssNewConnsWeight,
       "ssPortLoadWeight": ssPortLoadWeight,
       "ssSystemLoadWeight": ssSystemLoadWeight,
       "indRulesStatTable": indRulesStatTable,
       "indRulesStatEntry": indRulesStatEntry,
       "rsTimesFired": rsTimesFired,
       "rsNumSrvrs": rsNumSrvrs,
       "indHiAvailStatObjects": indHiAvailStatObjects,
       "hasPrimary": hasPrimary,
       "hasPort": hasPort,
       "hasState": hasState,
       "hasSubState": hasSubState,
       "indReachStatTable": indReachStatTable,
       "indReachStatEntry": indReachStatEntry,
       "rsAddr": rsAddr,
       "rsPingAble": rsPingAble,
       "indConfig": indConfig,
       "indExecCnfgObjects": indExecCnfgObjects,
       "indClstrCnfgTable": indClstrCnfgTable,
       "indPortCnfgTable": indPortCnfgTable,
       "indSrvrCnfgTable": indSrvrCnfgTable,
       "indRulesCnfgTable": indRulesCnfgTable,
       "indRulesCnfgEntry": indRulesCnfgEntry,
       "rcIndex": rcIndex,
       "rcName": rcName,
       "rcType": rcType,
       "rcBeginRange": rcBeginRange,
       "rcEndRange": rcEndRange,
       "rcPriority": rcPriority,
       "rcSrvrList": rcSrvrList,
       "indHiAvailCnfgObjects": indHiAvailCnfgObjects,
       "indReachCnfgTable": indReachCnfgTable,
       "indHrtBeatCnfgTable": indHrtBeatCnfgTable,
       "indHrtBeatCnfgEntry": indHrtBeatCnfgEntry,
       "hbcSrcAddr": hbcSrcAddr,
       "hbcDestAddr": hbcDestAddr,
       "hbcNumber": hbcNumber,
       "indAdvsrCnfgTable": indAdvsrCnfgTable,
       "indAdvsrCnfgEntry": indAdvsrCnfgEntry,
       "acPort": acPort,
       "acName": acName,
       "acVersion": acVersion,
       "indMngrCnfgObjects": indMngrCnfgObjects,
       "mcInterval": mcInterval,
       "mcRefresh": mcRefresh,
       "mcActiveProp": mcActiveProp,
       "mcNewProp": mcNewProp,
       "mcPortProp": mcPortProp,
       "mcSystemProp": mcSystemProp,
       "mcSensitivity": mcSensitivity,
       "mcSmoothing": mcSmoothing,
       "mcVersion": mcVersion,
       "indAllSrvrsCnfgTable": indAllSrvrsCnfgTable,
       "indAllSrvrsCnfgEntry": indAllSrvrsCnfgEntry,
       "ascAddr": ascAddr,
       "ascQuiesced": ascQuiesced,
       "ascInstances": ascInstances,
       "dispatcherMibConformance": dispatcherMibConformance,
       "indMibCompliances": indMibCompliances,
       "indMibCompliance": indMibCompliance,
       "indMibGroups": indMibGroups,
       "indMibStatGroups": indMibStatGroups,
       "indMibExecStatGroup": indMibExecStatGroup,
       "indMibClstrStatGroup": indMibClstrStatGroup,
       "indMibPortStatGroup": indMibPortStatGroup,
       "indMibSrvrStatGroup": indMibSrvrStatGroup,
       "indMibRulesStatGroup": indMibRulesStatGroup,
       "indMibHiAvailStatGroup": indMibHiAvailStatGroup,
       "indMibReachStatGroup": indMibReachStatGroup,
       "indMibCnfgGroups": indMibCnfgGroups,
       "indMibRulesCnfgGroup": indMibRulesCnfgGroup,
       "indMibHrtBeatCnfgGroup": indMibHrtBeatCnfgGroup,
       "indMibAdvsrCnfgGroup": indMibAdvsrCnfgGroup,
       "indMibMngrCnfgGroup": indMibMngrCnfgGroup,
       "indMibAllSrvrsCnfgGroup": indMibAllSrvrsCnfgGroup}
)
