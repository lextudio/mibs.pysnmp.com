# SNMP MIB module (CISCO-DLSW-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DLSW-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:10 2024
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

(DlciNumber,) = mibBuilder.importSymbols(
    "CISCO-FRAME-RELAY-MIB",
    "DlciNumber")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SAPType,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "SAPType")

(DlcType,
 LFSize,
 MacAddressNC,
 TAddress,
 dlswCircuitEntry,
 dlswCircuitState,
 dlswIfEntry,
 dlswTConnConfigEntry,
 dlswTConnConfigIndex,
 dlswTConnOperEntry,
 dlswTConnOperState,
 dlswTConnTcpConfigEntry) = mibBuilder.importSymbols(
    "DLSW-MIB",
    "DlcType",
    "LFSize",
    "MacAddressNC",
    "TAddress",
    "dlswCircuitEntry",
    "dlswCircuitState",
    "dlswIfEntry",
    "dlswTConnConfigEntry",
    "dlswTConnConfigIndex",
    "dlswTConnOperEntry",
    "dlswTConnOperState",
    "dlswTConnTcpConfigEntry")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDlswExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74)
)
ciscoDlswExtMIB.setRevisions(
        ("1997-03-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TDomainType(Integer32, TextualConvention):
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
        *(("directFrameRelay", 4),
          ("directHdlc", 3),
          ("fst", 2),
          ("llc2", 5),
          ("tcp", 1))
    )



class Cost(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )



class KeepaliveInterval(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )



class TCPQueueMax(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 2000),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDlswExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDlswExtMIBObjects = _CiscoDlswExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1)
)
_CdeDomains_ObjectIdentity = ObjectIdentity
cdeDomains = _CdeDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1)
)
_CdeFSTDomain_ObjectIdentity = ObjectIdentity
cdeFSTDomain = _CdeFSTDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 1)
)
_CdeDirectHdlcDomain_ObjectIdentity = ObjectIdentity
cdeDirectHdlcDomain = _CdeDirectHdlcDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 2)
)
_CdeDirectFrameRelayDomain_ObjectIdentity = ObjectIdentity
cdeDirectFrameRelayDomain = _CdeDirectFrameRelayDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 3)
)
_CdeLlc2Domain_ObjectIdentity = ObjectIdentity
cdeLlc2Domain = _CdeLlc2Domain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 4)
)
_CdeNode_ObjectIdentity = ObjectIdentity
cdeNode = _CdeNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2)
)


class _CdeNodeTAddr_Type(TAddress):
    """Custom type cdeNodeTAddr based on TAddress"""
    defaultHexValue = ""


_CdeNodeTAddr_Object = MibScalar
cdeNodeTAddr = _CdeNodeTAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 1),
    _CdeNodeTAddr_Type()
)
cdeNodeTAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodeTAddr.setStatus("current")


class _CdeNodeGroup_Type(Integer32):
    """Custom type cdeNodeGroup based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdeNodeGroup_Type.__name__ = "Integer32"
_CdeNodeGroup_Object = MibScalar
cdeNodeGroup = _CdeNodeGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 2),
    _CdeNodeGroup_Type()
)
cdeNodeGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodeGroup.setStatus("current")


class _CdeNodeBorder_Type(TruthValue):
    """Custom type cdeNodeBorder based on TruthValue"""


_CdeNodeBorder_Object = MibScalar
cdeNodeBorder = _CdeNodeBorder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 3),
    _CdeNodeBorder_Type()
)
cdeNodeBorder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodeBorder.setStatus("current")


class _CdeNodeCost_Type(Cost):
    """Custom type cdeNodeCost based on Cost"""
    defaultValue = 3


_CdeNodeCost_Object = MibScalar
cdeNodeCost = _CdeNodeCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 4),
    _CdeNodeCost_Type()
)
cdeNodeCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodeCost.setStatus("current")


class _CdeNodeKeepaliveInterval_Type(KeepaliveInterval):
    """Custom type cdeNodeKeepaliveInterval based on KeepaliveInterval"""
    defaultValue = 30


_CdeNodeKeepaliveInterval_Object = MibScalar
cdeNodeKeepaliveInterval = _CdeNodeKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 5),
    _CdeNodeKeepaliveInterval_Type()
)
cdeNodeKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodeKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdeNodeKeepaliveInterval.setUnits("Seconds")


class _CdeNodePassiveConnect_Type(TruthValue):
    """Custom type cdeNodePassiveConnect based on TruthValue"""


_CdeNodePassiveConnect_Object = MibScalar
cdeNodePassiveConnect = _CdeNodePassiveConnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 6),
    _CdeNodePassiveConnect_Type()
)
cdeNodePassiveConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePassiveConnect.setStatus("current")


class _CdeNodeBiuSegment_Type(TruthValue):
    """Custom type cdeNodeBiuSegment based on TruthValue"""


_CdeNodeBiuSegment_Object = MibScalar
cdeNodeBiuSegment = _CdeNodeBiuSegment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 7),
    _CdeNodeBiuSegment_Type()
)
cdeNodeBiuSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodeBiuSegment.setStatus("current")


class _CdeNodeInitPacingWindow_Type(Integer32):
    """Custom type cdeNodeInitPacingWindow based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_CdeNodeInitPacingWindow_Type.__name__ = "Integer32"
_CdeNodeInitPacingWindow_Object = MibScalar
cdeNodeInitPacingWindow = _CdeNodeInitPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 8),
    _CdeNodeInitPacingWindow_Type()
)
cdeNodeInitPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodeInitPacingWindow.setStatus("current")
if mibBuilder.loadTexts:
    cdeNodeInitPacingWindow.setUnits("packets")


class _CdeNodeMaxPacingWindow_Type(Integer32):
    """Custom type cdeNodeMaxPacingWindow based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_CdeNodeMaxPacingWindow_Type.__name__ = "Integer32"
_CdeNodeMaxPacingWindow_Object = MibScalar
cdeNodeMaxPacingWindow = _CdeNodeMaxPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 9),
    _CdeNodeMaxPacingWindow_Type()
)
cdeNodeMaxPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodeMaxPacingWindow.setStatus("current")
if mibBuilder.loadTexts:
    cdeNodeMaxPacingWindow.setUnits("packets")


class _CdeNodePromiscuous_Type(TruthValue):
    """Custom type cdeNodePromiscuous based on TruthValue"""


_CdeNodePromiscuous_Object = MibScalar
cdeNodePromiscuous = _CdeNodePromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 10),
    _CdeNodePromiscuous_Type()
)
cdeNodePromiscuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePromiscuous.setStatus("current")


class _CdeNodePromPeerDefaultsCost_Type(Cost):
    """Custom type cdeNodePromPeerDefaultsCost based on Cost"""
    defaultValue = 3


_CdeNodePromPeerDefaultsCost_Object = MibScalar
cdeNodePromPeerDefaultsCost = _CdeNodePromPeerDefaultsCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 11),
    _CdeNodePromPeerDefaultsCost_Type()
)
cdeNodePromPeerDefaultsCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePromPeerDefaultsCost.setStatus("current")


class _CdeNodePromPeerDefaultsDestMac_Type(MacAddressNC):
    """Custom type cdeNodePromPeerDefaultsDestMac based on MacAddressNC"""
    defaultHexValue = ""


_CdeNodePromPeerDefaultsDestMac_Object = MibScalar
cdeNodePromPeerDefaultsDestMac = _CdeNodePromPeerDefaultsDestMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 12),
    _CdeNodePromPeerDefaultsDestMac_Type()
)
cdeNodePromPeerDefaultsDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePromPeerDefaultsDestMac.setStatus("current")


class _CdeNodePromPeerDefaultsKeepaliveInterval_Type(KeepaliveInterval):
    """Custom type cdeNodePromPeerDefaultsKeepaliveInterval based on KeepaliveInterval"""
    defaultValue = 30


_CdeNodePromPeerDefaultsKeepaliveInterval_Object = MibScalar
cdeNodePromPeerDefaultsKeepaliveInterval = _CdeNodePromPeerDefaultsKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 13),
    _CdeNodePromPeerDefaultsKeepaliveInterval_Type()
)
cdeNodePromPeerDefaultsKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePromPeerDefaultsKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdeNodePromPeerDefaultsKeepaliveInterval.setUnits("Seconds")


class _CdeNodePromPeerDefaultsLFSize_Type(LFSize):
    """Custom type cdeNodePromPeerDefaultsLFSize based on LFSize"""


_CdeNodePromPeerDefaultsLFSize_Object = MibScalar
cdeNodePromPeerDefaultsLFSize = _CdeNodePromPeerDefaultsLFSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 14),
    _CdeNodePromPeerDefaultsLFSize_Type()
)
cdeNodePromPeerDefaultsLFSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePromPeerDefaultsLFSize.setStatus("current")
if mibBuilder.loadTexts:
    cdeNodePromPeerDefaultsLFSize.setUnits("bytes")


class _CdeNodePromPeerDefaultsTCPQueueMax_Type(TCPQueueMax):
    """Custom type cdeNodePromPeerDefaultsTCPQueueMax based on TCPQueueMax"""
    defaultValue = 200


_CdeNodePromPeerDefaultsTCPQueueMax_Object = MibScalar
cdeNodePromPeerDefaultsTCPQueueMax = _CdeNodePromPeerDefaultsTCPQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 15),
    _CdeNodePromPeerDefaultsTCPQueueMax_Type()
)
cdeNodePromPeerDefaultsTCPQueueMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePromPeerDefaultsTCPQueueMax.setStatus("current")
if mibBuilder.loadTexts:
    cdeNodePromPeerDefaultsTCPQueueMax.setUnits("packets")


class _CdeNodePeerOnDemandDefaultsCost_Type(Cost):
    """Custom type cdeNodePeerOnDemandDefaultsCost based on Cost"""
    defaultValue = 3


_CdeNodePeerOnDemandDefaultsCost_Object = MibScalar
cdeNodePeerOnDemandDefaultsCost = _CdeNodePeerOnDemandDefaultsCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 16),
    _CdeNodePeerOnDemandDefaultsCost_Type()
)
cdeNodePeerOnDemandDefaultsCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePeerOnDemandDefaultsCost.setStatus("current")


class _CdeNodePeerOnDemandDefaultsFst_Type(TruthValue):
    """Custom type cdeNodePeerOnDemandDefaultsFst based on TruthValue"""


_CdeNodePeerOnDemandDefaultsFst_Object = MibScalar
cdeNodePeerOnDemandDefaultsFst = _CdeNodePeerOnDemandDefaultsFst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 17),
    _CdeNodePeerOnDemandDefaultsFst_Type()
)
cdeNodePeerOnDemandDefaultsFst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePeerOnDemandDefaultsFst.setStatus("current")


class _CdeNodePeerOnDemandDefaultsInactivityInterval_Type(Integer32):
    """Custom type cdeNodePeerOnDemandDefaultsInactivityInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CdeNodePeerOnDemandDefaultsInactivityInterval_Type.__name__ = "Integer32"
_CdeNodePeerOnDemandDefaultsInactivityInterval_Object = MibScalar
cdeNodePeerOnDemandDefaultsInactivityInterval = _CdeNodePeerOnDemandDefaultsInactivityInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 18),
    _CdeNodePeerOnDemandDefaultsInactivityInterval_Type()
)
cdeNodePeerOnDemandDefaultsInactivityInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePeerOnDemandDefaultsInactivityInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdeNodePeerOnDemandDefaultsInactivityInterval.setUnits("Minutes")


class _CdeNodePeerOnDemandDefaultsKeepaliveInterval_Type(KeepaliveInterval):
    """Custom type cdeNodePeerOnDemandDefaultsKeepaliveInterval based on KeepaliveInterval"""
    defaultValue = 30


_CdeNodePeerOnDemandDefaultsKeepaliveInterval_Object = MibScalar
cdeNodePeerOnDemandDefaultsKeepaliveInterval = _CdeNodePeerOnDemandDefaultsKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 19),
    _CdeNodePeerOnDemandDefaultsKeepaliveInterval_Type()
)
cdeNodePeerOnDemandDefaultsKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePeerOnDemandDefaultsKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdeNodePeerOnDemandDefaultsKeepaliveInterval.setUnits("Seconds")


class _CdeNodePeerOnDemandDefaultsLFSize_Type(LFSize):
    """Custom type cdeNodePeerOnDemandDefaultsLFSize based on LFSize"""


_CdeNodePeerOnDemandDefaultsLFSize_Object = MibScalar
cdeNodePeerOnDemandDefaultsLFSize = _CdeNodePeerOnDemandDefaultsLFSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 20),
    _CdeNodePeerOnDemandDefaultsLFSize_Type()
)
cdeNodePeerOnDemandDefaultsLFSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePeerOnDemandDefaultsLFSize.setStatus("current")


class _CdeNodePeerOnDemandDefaultsPriority_Type(TruthValue):
    """Custom type cdeNodePeerOnDemandDefaultsPriority based on TruthValue"""


_CdeNodePeerOnDemandDefaultsPriority_Object = MibScalar
cdeNodePeerOnDemandDefaultsPriority = _CdeNodePeerOnDemandDefaultsPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 21),
    _CdeNodePeerOnDemandDefaultsPriority_Type()
)
cdeNodePeerOnDemandDefaultsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePeerOnDemandDefaultsPriority.setStatus("current")


class _CdeNodePeerOnDemandDefaultsTCPQueueMax_Type(TCPQueueMax):
    """Custom type cdeNodePeerOnDemandDefaultsTCPQueueMax based on TCPQueueMax"""
    defaultValue = 200


_CdeNodePeerOnDemandDefaultsTCPQueueMax_Object = MibScalar
cdeNodePeerOnDemandDefaultsTCPQueueMax = _CdeNodePeerOnDemandDefaultsTCPQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 22),
    _CdeNodePeerOnDemandDefaultsTCPQueueMax_Type()
)
cdeNodePeerOnDemandDefaultsTCPQueueMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeNodePeerOnDemandDefaultsTCPQueueMax.setStatus("current")
if mibBuilder.loadTexts:
    cdeNodePeerOnDemandDefaultsTCPQueueMax.setUnits("packets")
_CdeTConn_ObjectIdentity = ObjectIdentity
cdeTConn = _CdeTConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3)
)
_CdeTConnConfigTable_Object = MibTable
cdeTConnConfigTable = _CdeTConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cdeTConnConfigTable.setStatus("current")
_CdeTConnConfigEntry_Object = MibTableRow
cdeTConnConfigEntry = _CdeTConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cdeTConnConfigEntry.setStatus("current")


class _CdeTConnConfigTDomainType_Type(TDomainType):
    """Custom type cdeTConnConfigTDomainType based on TDomainType"""


_CdeTConnConfigTDomainType_Object = MibTableColumn
cdeTConnConfigTDomainType = _CdeTConnConfigTDomainType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 1),
    _CdeTConnConfigTDomainType_Type()
)
cdeTConnConfigTDomainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigTDomainType.setStatus("current")


class _CdeTConnConfigLocalAck_Type(TruthValue):
    """Custom type cdeTConnConfigLocalAck based on TruthValue"""


_CdeTConnConfigLocalAck_Object = MibTableColumn
cdeTConnConfigLocalAck = _CdeTConnConfigLocalAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 2),
    _CdeTConnConfigLocalAck_Type()
)
cdeTConnConfigLocalAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigLocalAck.setStatus("current")


class _CdeTConnConfigCost_Type(Cost):
    """Custom type cdeTConnConfigCost based on Cost"""
    defaultValue = 3


_CdeTConnConfigCost_Object = MibTableColumn
cdeTConnConfigCost = _CdeTConnConfigCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 3),
    _CdeTConnConfigCost_Type()
)
cdeTConnConfigCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigCost.setStatus("current")


class _CdeTConnConfigLFSize_Type(LFSize):
    """Custom type cdeTConnConfigLFSize based on LFSize"""


_CdeTConnConfigLFSize_Object = MibTableColumn
cdeTConnConfigLFSize = _CdeTConnConfigLFSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 4),
    _CdeTConnConfigLFSize_Type()
)
cdeTConnConfigLFSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigLFSize.setStatus("current")


class _CdeTConnConfigKeepaliveInterval_Type(KeepaliveInterval):
    """Custom type cdeTConnConfigKeepaliveInterval based on KeepaliveInterval"""
    defaultValue = 30


_CdeTConnConfigKeepaliveInterval_Object = MibTableColumn
cdeTConnConfigKeepaliveInterval = _CdeTConnConfigKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 5),
    _CdeTConnConfigKeepaliveInterval_Type()
)
cdeTConnConfigKeepaliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdeTConnConfigKeepaliveInterval.setUnits("Seconds")


class _CdeTConnConfigBackup_Type(TruthValue):
    """Custom type cdeTConnConfigBackup based on TruthValue"""


_CdeTConnConfigBackup_Object = MibTableColumn
cdeTConnConfigBackup = _CdeTConnConfigBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 6),
    _CdeTConnConfigBackup_Type()
)
cdeTConnConfigBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigBackup.setStatus("current")


class _CdeTConnConfigBackupTAddr_Type(TAddress):
    """Custom type cdeTConnConfigBackupTAddr based on TAddress"""
    defaultHexValue = ""


_CdeTConnConfigBackupTAddr_Object = MibTableColumn
cdeTConnConfigBackupTAddr = _CdeTConnConfigBackupTAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 7),
    _CdeTConnConfigBackupTAddr_Type()
)
cdeTConnConfigBackupTAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigBackupTAddr.setStatus("current")


class _CdeTConnConfigBackupLinger_Type(TruthValue):
    """Custom type cdeTConnConfigBackupLinger based on TruthValue"""


_CdeTConnConfigBackupLinger_Object = MibTableColumn
cdeTConnConfigBackupLinger = _CdeTConnConfigBackupLinger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 8),
    _CdeTConnConfigBackupLinger_Type()
)
cdeTConnConfigBackupLinger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigBackupLinger.setStatus("current")


class _CdeTConnConfigBackupLingerInterval_Type(Integer32):
    """Custom type cdeTConnConfigBackupLingerInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CdeTConnConfigBackupLingerInterval_Type.__name__ = "Integer32"
_CdeTConnConfigBackupLingerInterval_Object = MibTableColumn
cdeTConnConfigBackupLingerInterval = _CdeTConnConfigBackupLingerInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 9),
    _CdeTConnConfigBackupLingerInterval_Type()
)
cdeTConnConfigBackupLingerInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigBackupLingerInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdeTConnConfigBackupLingerInterval.setUnits("Minutes")


class _CdeTConnConfigPriority_Type(TruthValue):
    """Custom type cdeTConnConfigPriority based on TruthValue"""


_CdeTConnConfigPriority_Object = MibTableColumn
cdeTConnConfigPriority = _CdeTConnConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 10),
    _CdeTConnConfigPriority_Type()
)
cdeTConnConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigPriority.setStatus("current")


class _CdeTConnConfigDestMac_Type(MacAddressNC):
    """Custom type cdeTConnConfigDestMac based on MacAddressNC"""
    defaultHexValue = ""


_CdeTConnConfigDestMac_Object = MibTableColumn
cdeTConnConfigDestMac = _CdeTConnConfigDestMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 11),
    _CdeTConnConfigDestMac_Type()
)
cdeTConnConfigDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigDestMac.setStatus("current")


class _CdeTConnConfigDynamic_Type(TruthValue):
    """Custom type cdeTConnConfigDynamic based on TruthValue"""


_CdeTConnConfigDynamic_Object = MibTableColumn
cdeTConnConfigDynamic = _CdeTConnConfigDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 12),
    _CdeTConnConfigDynamic_Type()
)
cdeTConnConfigDynamic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigDynamic.setStatus("current")


class _CdeTConnConfigDynamicNoLlc_Type(Integer32):
    """Custom type cdeTConnConfigDynamicNoLlc based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CdeTConnConfigDynamicNoLlc_Type.__name__ = "Integer32"
_CdeTConnConfigDynamicNoLlc_Object = MibTableColumn
cdeTConnConfigDynamicNoLlc = _CdeTConnConfigDynamicNoLlc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 13),
    _CdeTConnConfigDynamicNoLlc_Type()
)
cdeTConnConfigDynamicNoLlc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigDynamicNoLlc.setStatus("current")
if mibBuilder.loadTexts:
    cdeTConnConfigDynamicNoLlc.setUnits("Minutes")


class _CdeTConnConfigDynamicInactivityInterval_Type(Integer32):
    """Custom type cdeTConnConfigDynamicInactivityInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_CdeTConnConfigDynamicInactivityInterval_Type.__name__ = "Integer32"
_CdeTConnConfigDynamicInactivityInterval_Object = MibTableColumn
cdeTConnConfigDynamicInactivityInterval = _CdeTConnConfigDynamicInactivityInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 14),
    _CdeTConnConfigDynamicInactivityInterval_Type()
)
cdeTConnConfigDynamicInactivityInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnConfigDynamicInactivityInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdeTConnConfigDynamicInactivityInterval.setUnits("Minutes")
_CdeTConnOperTable_Object = MibTable
cdeTConnOperTable = _CdeTConnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cdeTConnOperTable.setStatus("current")
_CdeTConnOperEntry_Object = MibTableRow
cdeTConnOperEntry = _CdeTConnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cdeTConnOperEntry.setStatus("current")


class _CdeTConnOperPartnerCost_Type(Cost):
    """Custom type cdeTConnOperPartnerCost based on Cost"""
    defaultValue = 3


_CdeTConnOperPartnerCost_Object = MibTableColumn
cdeTConnOperPartnerCost = _CdeTConnOperPartnerCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 1),
    _CdeTConnOperPartnerCost_Type()
)
cdeTConnOperPartnerCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeTConnOperPartnerCost.setStatus("current")
_CdeTConnOperPartnerPriority_Type = TruthValue
_CdeTConnOperPartnerPriority_Object = MibTableColumn
cdeTConnOperPartnerPriority = _CdeTConnOperPartnerPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 2),
    _CdeTConnOperPartnerPriority_Type()
)
cdeTConnOperPartnerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeTConnOperPartnerPriority.setStatus("current")
_CdeTConnOperPartnerBorderPeer_Type = TruthValue
_CdeTConnOperPartnerBorderPeer_Object = MibTableColumn
cdeTConnOperPartnerBorderPeer = _CdeTConnOperPartnerBorderPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 3),
    _CdeTConnOperPartnerBorderPeer_Type()
)
cdeTConnOperPartnerBorderPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeTConnOperPartnerBorderPeer.setStatus("current")


class _CdeTConnOperPartnerGroupNum_Type(Integer32):
    """Custom type cdeTConnOperPartnerGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdeTConnOperPartnerGroupNum_Type.__name__ = "Integer32"
_CdeTConnOperPartnerGroupNum_Object = MibTableColumn
cdeTConnOperPartnerGroupNum = _CdeTConnOperPartnerGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 4),
    _CdeTConnOperPartnerGroupNum_Type()
)
cdeTConnOperPartnerGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeTConnOperPartnerGroupNum.setStatus("current")
_CdeTConnOperTDomainType_Type = TDomainType
_CdeTConnOperTDomainType_Object = MibTableColumn
cdeTConnOperTDomainType = _CdeTConnOperTDomainType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 5),
    _CdeTConnOperTDomainType_Type()
)
cdeTConnOperTDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeTConnOperTDomainType.setStatus("current")
_CdeTConnSpecific_ObjectIdentity = ObjectIdentity
cdeTConnSpecific = _CdeTConnSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3)
)
_CdeTConnTcp_ObjectIdentity = ObjectIdentity
cdeTConnTcp = _CdeTConnTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1)
)
_CdeTConnTcpConfigTable_Object = MibTable
cdeTConnTcpConfigTable = _CdeTConnTcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cdeTConnTcpConfigTable.setStatus("current")
_CdeTConnTcpConfigEntry_Object = MibTableRow
cdeTConnTcpConfigEntry = _CdeTConnTcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdeTConnTcpConfigEntry.setStatus("current")


class _CdeTConnTcpConfigQueueMax_Type(TCPQueueMax):
    """Custom type cdeTConnTcpConfigQueueMax based on TCPQueueMax"""
    defaultValue = 200


_CdeTConnTcpConfigQueueMax_Object = MibTableColumn
cdeTConnTcpConfigQueueMax = _CdeTConnTcpConfigQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1, 1, 1, 1),
    _CdeTConnTcpConfigQueueMax_Type()
)
cdeTConnTcpConfigQueueMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnTcpConfigQueueMax.setStatus("current")
if mibBuilder.loadTexts:
    cdeTConnTcpConfigQueueMax.setUnits("packets")
_CdeTConnDirect_ObjectIdentity = ObjectIdentity
cdeTConnDirect = _CdeTConnDirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2)
)
_CdeTConnDirectConfigTable_Object = MibTable
cdeTConnDirectConfigTable = _CdeTConnDirectConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cdeTConnDirectConfigTable.setStatus("current")
_CdeTConnDirectConfigEntry_Object = MibTableRow
cdeTConnDirectConfigEntry = _CdeTConnDirectConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1)
)
cdeTConnDirectConfigEntry.setIndexNames(
    (0, "DLSW-MIB", "dlswTConnConfigIndex"),
)
if mibBuilder.loadTexts:
    cdeTConnDirectConfigEntry.setStatus("current")
_CdeTConnDirectConfigIfIndex_Type = InterfaceIndex
_CdeTConnDirectConfigIfIndex_Object = MibTableColumn
cdeTConnDirectConfigIfIndex = _CdeTConnDirectConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1, 1),
    _CdeTConnDirectConfigIfIndex_Type()
)
cdeTConnDirectConfigIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnDirectConfigIfIndex.setStatus("current")


class _CdeTConnDirectConfigMediaEncap_Type(Integer32):
    """Custom type cdeTConnDirectConfigMediaEncap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("directFrameRelay", 2),
          ("directHdlc", 1),
          ("llc2", 3))
    )


_CdeTConnDirectConfigMediaEncap_Type.__name__ = "Integer32"
_CdeTConnDirectConfigMediaEncap_Object = MibTableColumn
cdeTConnDirectConfigMediaEncap = _CdeTConnDirectConfigMediaEncap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1, 2),
    _CdeTConnDirectConfigMediaEncap_Type()
)
cdeTConnDirectConfigMediaEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnDirectConfigMediaEncap.setStatus("current")


class _CdeTConnDirectConfigFrameRelayDlci_Type(DlciNumber):
    """Custom type cdeTConnDirectConfigFrameRelayDlci based on DlciNumber"""
    defaultValue = 0


_CdeTConnDirectConfigFrameRelayDlci_Object = MibTableColumn
cdeTConnDirectConfigFrameRelayDlci = _CdeTConnDirectConfigFrameRelayDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1, 3),
    _CdeTConnDirectConfigFrameRelayDlci_Type()
)
cdeTConnDirectConfigFrameRelayDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdeTConnDirectConfigFrameRelayDlci.setStatus("current")
_CdeInterface_ObjectIdentity = ObjectIdentity
cdeInterface = _CdeInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4)
)
_CdeIfTable_Object = MibTable
cdeIfTable = _CdeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdeIfTable.setStatus("current")
_CdeIfEntry_Object = MibTableRow
cdeIfEntry = _CdeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cdeIfEntry.setStatus("current")
_CdeIfType_Type = DlcType
_CdeIfType_Object = MibTableColumn
cdeIfType = _CdeIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4, 1, 1, 1),
    _CdeIfType_Type()
)
cdeIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeIfType.setStatus("current")
_CdeCircuit_ObjectIdentity = ObjectIdentity
cdeCircuit = _CdeCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5)
)
_CdeCircuitTable_Object = MibTable
cdeCircuitTable = _CdeCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cdeCircuitTable.setStatus("current")
_CdeCircuitEntry_Object = MibTableRow
cdeCircuitEntry = _CdeCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    cdeCircuitEntry.setStatus("current")


class _CdeCircuitS1Name_Type(DisplayString):
    """Custom type cdeCircuitS1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CdeCircuitS1Name_Type.__name__ = "DisplayString"
_CdeCircuitS1Name_Object = MibTableColumn
cdeCircuitS1Name = _CdeCircuitS1Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 1),
    _CdeCircuitS1Name_Type()
)
cdeCircuitS1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeCircuitS1Name.setStatus("current")


class _CdeCircuitS2Name_Type(DisplayString):
    """Custom type cdeCircuitS2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_CdeCircuitS2Name_Type.__name__ = "DisplayString"
_CdeCircuitS2Name_Object = MibTableColumn
cdeCircuitS2Name = _CdeCircuitS2Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 2),
    _CdeCircuitS2Name_Type()
)
cdeCircuitS2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeCircuitS2Name.setStatus("current")


class _CdeCircuitS1IdBlock_Type(DisplayString):
    """Custom type cdeCircuitS1IdBlock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_CdeCircuitS1IdBlock_Type.__name__ = "DisplayString"
_CdeCircuitS1IdBlock_Object = MibTableColumn
cdeCircuitS1IdBlock = _CdeCircuitS1IdBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 3),
    _CdeCircuitS1IdBlock_Type()
)
cdeCircuitS1IdBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeCircuitS1IdBlock.setStatus("current")


class _CdeCircuitS1IdNum_Type(DisplayString):
    """Custom type cdeCircuitS1IdNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CdeCircuitS1IdNum_Type.__name__ = "DisplayString"
_CdeCircuitS1IdNum_Object = MibTableColumn
cdeCircuitS1IdNum = _CdeCircuitS1IdNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 4),
    _CdeCircuitS1IdNum_Type()
)
cdeCircuitS1IdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeCircuitS1IdNum.setStatus("current")
_CdeFast_ObjectIdentity = ObjectIdentity
cdeFast = _CdeFast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6)
)
_CdeFastTable_Object = MibTable
cdeFastTable = _CdeFastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cdeFastTable.setStatus("current")
_CdeFastEntry_Object = MibTableRow
cdeFastEntry = _CdeFastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1)
)
cdeFastEntry.setIndexNames(
    (0, "CISCO-DLSW-EXT-MIB", "cdeFastS1Mac"),
    (0, "CISCO-DLSW-EXT-MIB", "cdeFastS1Sap"),
    (0, "CISCO-DLSW-EXT-MIB", "cdeFastS2Mac"),
    (0, "CISCO-DLSW-EXT-MIB", "cdeFastS2Sap"),
)
if mibBuilder.loadTexts:
    cdeFastEntry.setStatus("current")
_CdeFastS1Mac_Type = MacAddressNC
_CdeFastS1Mac_Object = MibTableColumn
cdeFastS1Mac = _CdeFastS1Mac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 1),
    _CdeFastS1Mac_Type()
)
cdeFastS1Mac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdeFastS1Mac.setStatus("current")
_CdeFastS1Sap_Type = SAPType
_CdeFastS1Sap_Object = MibTableColumn
cdeFastS1Sap = _CdeFastS1Sap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 2),
    _CdeFastS1Sap_Type()
)
cdeFastS1Sap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdeFastS1Sap.setStatus("current")
_CdeFastS2Mac_Type = MacAddressNC
_CdeFastS2Mac_Object = MibTableColumn
cdeFastS2Mac = _CdeFastS2Mac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 3),
    _CdeFastS2Mac_Type()
)
cdeFastS2Mac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdeFastS2Mac.setStatus("current")
_CdeFastS2Sap_Type = SAPType
_CdeFastS2Sap_Object = MibTableColumn
cdeFastS2Sap = _CdeFastS2Sap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 4),
    _CdeFastS2Sap_Type()
)
cdeFastS2Sap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdeFastS2Sap.setStatus("current")
_CdeFastS1IfIndex_Type = InterfaceIndex
_CdeFastS1IfIndex_Object = MibTableColumn
cdeFastS1IfIndex = _CdeFastS1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 5),
    _CdeFastS1IfIndex_Type()
)
cdeFastS1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeFastS1IfIndex.setStatus("current")


class _CdeFastS1RouteInfo_Type(OctetString):
    """Custom type cdeFastS1RouteInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CdeFastS1RouteInfo_Type.__name__ = "OctetString"
_CdeFastS1RouteInfo_Object = MibTableColumn
cdeFastS1RouteInfo = _CdeFastS1RouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 6),
    _CdeFastS1RouteInfo_Type()
)
cdeFastS1RouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeFastS1RouteInfo.setStatus("current")


class _CdeFastS1CacheId_Type(OctetString):
    """Custom type cdeFastS1CacheId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CdeFastS1CacheId_Type.__name__ = "OctetString"
_CdeFastS1CacheId_Object = MibTableColumn
cdeFastS1CacheId = _CdeFastS1CacheId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 7),
    _CdeFastS1CacheId_Type()
)
cdeFastS1CacheId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeFastS1CacheId.setStatus("current")
_CdeFastS2TDomain_Type = ObjectIdentifier
_CdeFastS2TDomain_Object = MibTableColumn
cdeFastS2TDomain = _CdeFastS2TDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 8),
    _CdeFastS2TDomain_Type()
)
cdeFastS2TDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeFastS2TDomain.setStatus("current")
_CdeFastS2TAddress_Type = TAddress
_CdeFastS2TAddress_Object = MibTableColumn
cdeFastS2TAddress = _CdeFastS2TAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 9),
    _CdeFastS2TAddress_Type()
)
cdeFastS2TAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeFastS2TAddress.setStatus("current")


class _CdeFastS2CacheId_Type(OctetString):
    """Custom type cdeFastS2CacheId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CdeFastS2CacheId_Type.__name__ = "OctetString"
_CdeFastS2CacheId_Object = MibTableColumn
cdeFastS2CacheId = _CdeFastS2CacheId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 10),
    _CdeFastS2CacheId_Type()
)
cdeFastS2CacheId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeFastS2CacheId.setStatus("current")


class _CdeFastOrigin_Type(Integer32):
    """Custom type cdeFastOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_CdeFastOrigin_Type.__name__ = "Integer32"
_CdeFastOrigin_Object = MibTableColumn
cdeFastOrigin = _CdeFastOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 11),
    _CdeFastOrigin_Type()
)
cdeFastOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeFastOrigin.setStatus("current")
_CdeFastTimeToLive_Type = TimeTicks
_CdeFastTimeToLive_Object = MibTableColumn
cdeFastTimeToLive = _CdeFastTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 12),
    _CdeFastTimeToLive_Type()
)
cdeFastTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdeFastTimeToLive.setStatus("current")
if mibBuilder.loadTexts:
    cdeFastTimeToLive.setUnits("hundredths of a second")
_CdeTrapControl_ObjectIdentity = ObjectIdentity
cdeTrapControl = _CdeTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 7)
)


class _CdeTrapCntlTConn_Type(TruthValue):
    """Custom type cdeTrapCntlTConn based on TruthValue"""


_CdeTrapCntlTConn_Object = MibScalar
cdeTrapCntlTConn = _CdeTrapCntlTConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 7, 1),
    _CdeTrapCntlTConn_Type()
)
cdeTrapCntlTConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeTrapCntlTConn.setStatus("current")


class _CdeTrapCntlCircuit_Type(TruthValue):
    """Custom type cdeTrapCntlCircuit based on TruthValue"""


_CdeTrapCntlCircuit_Object = MibScalar
cdeTrapCntlCircuit = _CdeTrapCntlCircuit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 7, 2),
    _CdeTrapCntlCircuit_Type()
)
cdeTrapCntlCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdeTrapCntlCircuit.setStatus("current")
_CdeTrapsPrefix_ObjectIdentity = ObjectIdentity
cdeTrapsPrefix = _CdeTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 2)
)
_CdeTraps_ObjectIdentity = ObjectIdentity
cdeTraps = _CdeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 2, 0)
)
_CdeMIBConformance_ObjectIdentity = ObjectIdentity
cdeMIBConformance = _CdeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3)
)
_CdeMIBCompliances_ObjectIdentity = ObjectIdentity
cdeMIBCompliances = _CdeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 1)
)
_CdeMIBGroups_ObjectIdentity = ObjectIdentity
cdeMIBGroups = _CdeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2)
)
dlswTConnConfigEntry.registerAugmentions(
    ("CISCO-DLSW-EXT-MIB",
     "cdeTConnConfigEntry")
)
cdeTConnConfigEntry.setIndexNames(*dlswTConnConfigEntry.getIndexNames())
dlswTConnOperEntry.registerAugmentions(
    ("CISCO-DLSW-EXT-MIB",
     "cdeTConnOperEntry")
)
cdeTConnOperEntry.setIndexNames(*dlswTConnOperEntry.getIndexNames())
dlswTConnTcpConfigEntry.registerAugmentions(
    ("CISCO-DLSW-EXT-MIB",
     "cdeTConnTcpConfigEntry")
)
cdeTConnTcpConfigEntry.setIndexNames(*dlswTConnTcpConfigEntry.getIndexNames())
dlswIfEntry.registerAugmentions(
    ("CISCO-DLSW-EXT-MIB",
     "cdeIfEntry")
)
cdeIfEntry.setIndexNames(*dlswIfEntry.getIndexNames())
dlswCircuitEntry.registerAugmentions(
    ("CISCO-DLSW-EXT-MIB",
     "cdeCircuitEntry")
)
cdeCircuitEntry.setIndexNames(*dlswCircuitEntry.getIndexNames())

# Managed Objects groups

cdeMIBNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 1)
)
cdeMIBNodeGroup.setObjects(
      *(("CISCO-DLSW-EXT-MIB", "cdeNodeTAddr"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodeGroup"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodeBorder"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodeCost"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodeKeepaliveInterval"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePassiveConnect"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodeBiuSegment"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodeInitPacingWindow"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodeMaxPacingWindow"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePromiscuous"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePromPeerDefaultsCost"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePromPeerDefaultsDestMac"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePromPeerDefaultsKeepaliveInterval"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePromPeerDefaultsLFSize"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePromPeerDefaultsTCPQueueMax"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsCost"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsFst"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsInactivityInterval"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsKeepaliveInterval"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsLFSize"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsPriority"),
        ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsTCPQueueMax"))
)
if mibBuilder.loadTexts:
    cdeMIBNodeGroup.setStatus("current")

cdeMIBTConnConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 2)
)
cdeMIBTConnConfigGroup.setObjects(
      *(("CISCO-DLSW-EXT-MIB", "cdeTConnConfigTDomainType"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigLocalAck"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigCost"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigLFSize"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigKeepaliveInterval"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigBackup"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigBackupTAddr"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigBackupLinger"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigBackupLingerInterval"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigPriority"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigDestMac"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigDynamic"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigDynamicNoLlc"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigDynamicInactivityInterval"))
)
if mibBuilder.loadTexts:
    cdeMIBTConnConfigGroup.setStatus("current")

cdeMIBTConnOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 3)
)
cdeMIBTConnOperGroup.setObjects(
      *(("CISCO-DLSW-EXT-MIB", "cdeTConnOperPartnerCost"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnOperPartnerPriority"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnOperPartnerBorderPeer"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnOperPartnerGroupNum"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnOperTDomainType"))
)
if mibBuilder.loadTexts:
    cdeMIBTConnOperGroup.setStatus("current")

cdeMIBTConnTcpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 4)
)
cdeMIBTConnTcpConfigGroup.setObjects(
    ("CISCO-DLSW-EXT-MIB", "cdeTConnTcpConfigQueueMax")
)
if mibBuilder.loadTexts:
    cdeMIBTConnTcpConfigGroup.setStatus("current")

cdeMIBTConnDirectConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 5)
)
cdeMIBTConnDirectConfigGroup.setObjects(
      *(("CISCO-DLSW-EXT-MIB", "cdeTConnDirectConfigIfIndex"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnDirectConfigMediaEncap"),
        ("CISCO-DLSW-EXT-MIB", "cdeTConnDirectConfigFrameRelayDlci"))
)
if mibBuilder.loadTexts:
    cdeMIBTConnDirectConfigGroup.setStatus("current")

cdeMIBInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 6)
)
cdeMIBInterfaceGroup.setObjects(
    ("CISCO-DLSW-EXT-MIB", "cdeIfType")
)
if mibBuilder.loadTexts:
    cdeMIBInterfaceGroup.setStatus("current")

cdeMIBCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 7)
)
cdeMIBCircuitGroup.setObjects(
      *(("CISCO-DLSW-EXT-MIB", "cdeCircuitS1Name"),
        ("CISCO-DLSW-EXT-MIB", "cdeCircuitS2Name"),
        ("CISCO-DLSW-EXT-MIB", "cdeCircuitS1IdBlock"),
        ("CISCO-DLSW-EXT-MIB", "cdeCircuitS1IdNum"))
)
if mibBuilder.loadTexts:
    cdeMIBCircuitGroup.setStatus("current")

cdeMIBFastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 8)
)
cdeMIBFastGroup.setObjects(
      *(("CISCO-DLSW-EXT-MIB", "cdeFastS1IfIndex"),
        ("CISCO-DLSW-EXT-MIB", "cdeFastS1RouteInfo"),
        ("CISCO-DLSW-EXT-MIB", "cdeFastS1CacheId"),
        ("CISCO-DLSW-EXT-MIB", "cdeFastS2TDomain"),
        ("CISCO-DLSW-EXT-MIB", "cdeFastS2TAddress"),
        ("CISCO-DLSW-EXT-MIB", "cdeFastS2CacheId"),
        ("CISCO-DLSW-EXT-MIB", "cdeFastOrigin"),
        ("CISCO-DLSW-EXT-MIB", "cdeFastTimeToLive"))
)
if mibBuilder.loadTexts:
    cdeMIBFastGroup.setStatus("current")

cdeTrapControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 9)
)
cdeTrapControlGroup.setObjects(
      *(("CISCO-DLSW-EXT-MIB", "cdeTrapCntlTConn"),
        ("CISCO-DLSW-EXT-MIB", "cdeTrapCntlCircuit"))
)
if mibBuilder.loadTexts:
    cdeTrapControlGroup.setStatus("current")


# Notification objects

cdeTrapTConnUpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 2, 0, 1)
)
cdeTrapTConnUpDown.setObjects(
    ("DLSW-MIB", "dlswTConnOperState")
)
if mibBuilder.loadTexts:
    cdeTrapTConnUpDown.setStatus(
        "current"
    )

cdeTrapCircuitUpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 2, 0, 2)
)
cdeTrapCircuitUpDown.setObjects(
    ("DLSW-MIB", "dlswCircuitState")
)
if mibBuilder.loadTexts:
    cdeTrapCircuitUpDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

cdeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cdeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DLSW-EXT-MIB",
    **{"TDomainType": TDomainType,
       "Cost": Cost,
       "KeepaliveInterval": KeepaliveInterval,
       "TCPQueueMax": TCPQueueMax,
       "ciscoDlswExtMIB": ciscoDlswExtMIB,
       "ciscoDlswExtMIBObjects": ciscoDlswExtMIBObjects,
       "cdeDomains": cdeDomains,
       "cdeFSTDomain": cdeFSTDomain,
       "cdeDirectHdlcDomain": cdeDirectHdlcDomain,
       "cdeDirectFrameRelayDomain": cdeDirectFrameRelayDomain,
       "cdeLlc2Domain": cdeLlc2Domain,
       "cdeNode": cdeNode,
       "cdeNodeTAddr": cdeNodeTAddr,
       "cdeNodeGroup": cdeNodeGroup,
       "cdeNodeBorder": cdeNodeBorder,
       "cdeNodeCost": cdeNodeCost,
       "cdeNodeKeepaliveInterval": cdeNodeKeepaliveInterval,
       "cdeNodePassiveConnect": cdeNodePassiveConnect,
       "cdeNodeBiuSegment": cdeNodeBiuSegment,
       "cdeNodeInitPacingWindow": cdeNodeInitPacingWindow,
       "cdeNodeMaxPacingWindow": cdeNodeMaxPacingWindow,
       "cdeNodePromiscuous": cdeNodePromiscuous,
       "cdeNodePromPeerDefaultsCost": cdeNodePromPeerDefaultsCost,
       "cdeNodePromPeerDefaultsDestMac": cdeNodePromPeerDefaultsDestMac,
       "cdeNodePromPeerDefaultsKeepaliveInterval": cdeNodePromPeerDefaultsKeepaliveInterval,
       "cdeNodePromPeerDefaultsLFSize": cdeNodePromPeerDefaultsLFSize,
       "cdeNodePromPeerDefaultsTCPQueueMax": cdeNodePromPeerDefaultsTCPQueueMax,
       "cdeNodePeerOnDemandDefaultsCost": cdeNodePeerOnDemandDefaultsCost,
       "cdeNodePeerOnDemandDefaultsFst": cdeNodePeerOnDemandDefaultsFst,
       "cdeNodePeerOnDemandDefaultsInactivityInterval": cdeNodePeerOnDemandDefaultsInactivityInterval,
       "cdeNodePeerOnDemandDefaultsKeepaliveInterval": cdeNodePeerOnDemandDefaultsKeepaliveInterval,
       "cdeNodePeerOnDemandDefaultsLFSize": cdeNodePeerOnDemandDefaultsLFSize,
       "cdeNodePeerOnDemandDefaultsPriority": cdeNodePeerOnDemandDefaultsPriority,
       "cdeNodePeerOnDemandDefaultsTCPQueueMax": cdeNodePeerOnDemandDefaultsTCPQueueMax,
       "cdeTConn": cdeTConn,
       "cdeTConnConfigTable": cdeTConnConfigTable,
       "cdeTConnConfigEntry": cdeTConnConfigEntry,
       "cdeTConnConfigTDomainType": cdeTConnConfigTDomainType,
       "cdeTConnConfigLocalAck": cdeTConnConfigLocalAck,
       "cdeTConnConfigCost": cdeTConnConfigCost,
       "cdeTConnConfigLFSize": cdeTConnConfigLFSize,
       "cdeTConnConfigKeepaliveInterval": cdeTConnConfigKeepaliveInterval,
       "cdeTConnConfigBackup": cdeTConnConfigBackup,
       "cdeTConnConfigBackupTAddr": cdeTConnConfigBackupTAddr,
       "cdeTConnConfigBackupLinger": cdeTConnConfigBackupLinger,
       "cdeTConnConfigBackupLingerInterval": cdeTConnConfigBackupLingerInterval,
       "cdeTConnConfigPriority": cdeTConnConfigPriority,
       "cdeTConnConfigDestMac": cdeTConnConfigDestMac,
       "cdeTConnConfigDynamic": cdeTConnConfigDynamic,
       "cdeTConnConfigDynamicNoLlc": cdeTConnConfigDynamicNoLlc,
       "cdeTConnConfigDynamicInactivityInterval": cdeTConnConfigDynamicInactivityInterval,
       "cdeTConnOperTable": cdeTConnOperTable,
       "cdeTConnOperEntry": cdeTConnOperEntry,
       "cdeTConnOperPartnerCost": cdeTConnOperPartnerCost,
       "cdeTConnOperPartnerPriority": cdeTConnOperPartnerPriority,
       "cdeTConnOperPartnerBorderPeer": cdeTConnOperPartnerBorderPeer,
       "cdeTConnOperPartnerGroupNum": cdeTConnOperPartnerGroupNum,
       "cdeTConnOperTDomainType": cdeTConnOperTDomainType,
       "cdeTConnSpecific": cdeTConnSpecific,
       "cdeTConnTcp": cdeTConnTcp,
       "cdeTConnTcpConfigTable": cdeTConnTcpConfigTable,
       "cdeTConnTcpConfigEntry": cdeTConnTcpConfigEntry,
       "cdeTConnTcpConfigQueueMax": cdeTConnTcpConfigQueueMax,
       "cdeTConnDirect": cdeTConnDirect,
       "cdeTConnDirectConfigTable": cdeTConnDirectConfigTable,
       "cdeTConnDirectConfigEntry": cdeTConnDirectConfigEntry,
       "cdeTConnDirectConfigIfIndex": cdeTConnDirectConfigIfIndex,
       "cdeTConnDirectConfigMediaEncap": cdeTConnDirectConfigMediaEncap,
       "cdeTConnDirectConfigFrameRelayDlci": cdeTConnDirectConfigFrameRelayDlci,
       "cdeInterface": cdeInterface,
       "cdeIfTable": cdeIfTable,
       "cdeIfEntry": cdeIfEntry,
       "cdeIfType": cdeIfType,
       "cdeCircuit": cdeCircuit,
       "cdeCircuitTable": cdeCircuitTable,
       "cdeCircuitEntry": cdeCircuitEntry,
       "cdeCircuitS1Name": cdeCircuitS1Name,
       "cdeCircuitS2Name": cdeCircuitS2Name,
       "cdeCircuitS1IdBlock": cdeCircuitS1IdBlock,
       "cdeCircuitS1IdNum": cdeCircuitS1IdNum,
       "cdeFast": cdeFast,
       "cdeFastTable": cdeFastTable,
       "cdeFastEntry": cdeFastEntry,
       "cdeFastS1Mac": cdeFastS1Mac,
       "cdeFastS1Sap": cdeFastS1Sap,
       "cdeFastS2Mac": cdeFastS2Mac,
       "cdeFastS2Sap": cdeFastS2Sap,
       "cdeFastS1IfIndex": cdeFastS1IfIndex,
       "cdeFastS1RouteInfo": cdeFastS1RouteInfo,
       "cdeFastS1CacheId": cdeFastS1CacheId,
       "cdeFastS2TDomain": cdeFastS2TDomain,
       "cdeFastS2TAddress": cdeFastS2TAddress,
       "cdeFastS2CacheId": cdeFastS2CacheId,
       "cdeFastOrigin": cdeFastOrigin,
       "cdeFastTimeToLive": cdeFastTimeToLive,
       "cdeTrapControl": cdeTrapControl,
       "cdeTrapCntlTConn": cdeTrapCntlTConn,
       "cdeTrapCntlCircuit": cdeTrapCntlCircuit,
       "cdeTrapsPrefix": cdeTrapsPrefix,
       "cdeTraps": cdeTraps,
       "cdeTrapTConnUpDown": cdeTrapTConnUpDown,
       "cdeTrapCircuitUpDown": cdeTrapCircuitUpDown,
       "cdeMIBConformance": cdeMIBConformance,
       "cdeMIBCompliances": cdeMIBCompliances,
       "cdeMIBCompliance": cdeMIBCompliance,
       "cdeMIBGroups": cdeMIBGroups,
       "cdeMIBNodeGroup": cdeMIBNodeGroup,
       "cdeMIBTConnConfigGroup": cdeMIBTConnConfigGroup,
       "cdeMIBTConnOperGroup": cdeMIBTConnOperGroup,
       "cdeMIBTConnTcpConfigGroup": cdeMIBTConnTcpConfigGroup,
       "cdeMIBTConnDirectConfigGroup": cdeMIBTConnDirectConfigGroup,
       "cdeMIBInterfaceGroup": cdeMIBInterfaceGroup,
       "cdeMIBCircuitGroup": cdeMIBCircuitGroup,
       "cdeMIBFastGroup": cdeMIBFastGroup,
       "cdeTrapControlGroup": cdeTrapControlGroup}
)
