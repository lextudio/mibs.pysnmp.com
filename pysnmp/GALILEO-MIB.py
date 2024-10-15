# SNMP MIB module (GALILEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GALILEO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:38 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(rlGalileo,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rlGalileo")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class RlPolicyGalileoDebugGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridged", 1),
          ("routedIp", 2),
          ("routedIpx", 3))
    )



class RlPolicySimpleGalMibProfileType(Integer32, TextualConvention):
    status = "current"
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
        *(("bandwidthGuarantee", 2),
          ("minBandwidth", 1),
          ("minDelay", 3),
          ("minDelayPerSession", 4))
    )



class RlPolicySimpleGalMibPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boundary", 1),
          ("interior", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlGalMibVersion_Type = Integer32
_RlGalMibVersion_Object = MibScalar
rlGalMibVersion = _RlGalMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 1),
    _RlGalMibVersion_Type()
)
rlGalMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGalMibVersion.setStatus("mandatory")


class _RlGalMode_Type(Integer32):
    """Custom type rlGalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("extended", 2))
    )


_RlGalMode_Type.__name__ = "Integer32"
_RlGalMode_Object = MibScalar
rlGalMode = _RlGalMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 2),
    _RlGalMode_Type()
)
rlGalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGalMode.setStatus("mandatory")


class _RlGalModeAfterReset_Type(Integer32):
    """Custom type rlGalModeAfterReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("extended", 2))
    )


_RlGalModeAfterReset_Type.__name__ = "Integer32"
_RlGalModeAfterReset_Object = MibScalar
rlGalModeAfterReset = _RlGalModeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 3),
    _RlGalModeAfterReset_Type()
)
rlGalModeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGalModeAfterReset.setStatus("mandatory")
_RlPolicyGalileoDebugTuning_ObjectIdentity = ObjectIdentity
rlPolicyGalileoDebugTuning = _RlPolicyGalileoDebugTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 56, 4)
)


class _RlPolicyGalileoTuningOverProvisioning_Type(Integer32):
    """Custom type rlPolicyGalileoTuningOverProvisioning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("minorOverProvisioning", 2),
          ("overProvisioning", 1),
          ("underProvisioning", 3))
    )


_RlPolicyGalileoTuningOverProvisioning_Type.__name__ = "Integer32"
_RlPolicyGalileoTuningOverProvisioning_Object = MibScalar
rlPolicyGalileoTuningOverProvisioning = _RlPolicyGalileoTuningOverProvisioning_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 4, 1),
    _RlPolicyGalileoTuningOverProvisioning_Type()
)
rlPolicyGalileoTuningOverProvisioning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoTuningOverProvisioning.setStatus("mandatory")


class _RlPolicyGalileoTuningExtremConditionBurstSize_Type(Integer32):
    """Custom type rlPolicyGalileoTuningExtremConditionBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maxMtu", 2),
          ("zero", 1))
    )


_RlPolicyGalileoTuningExtremConditionBurstSize_Type.__name__ = "Integer32"
_RlPolicyGalileoTuningExtremConditionBurstSize_Object = MibScalar
rlPolicyGalileoTuningExtremConditionBurstSize = _RlPolicyGalileoTuningExtremConditionBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 4, 2),
    _RlPolicyGalileoTuningExtremConditionBurstSize_Type()
)
rlPolicyGalileoTuningExtremConditionBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoTuningExtremConditionBurstSize.setStatus("mandatory")
_RlPolicyGalileoTuningOverrideOutOfProfileDropPrecedence_Type = TruthValue
_RlPolicyGalileoTuningOverrideOutOfProfileDropPrecedence_Object = MibScalar
rlPolicyGalileoTuningOverrideOutOfProfileDropPrecedence = _RlPolicyGalileoTuningOverrideOutOfProfileDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 4, 3),
    _RlPolicyGalileoTuningOverrideOutOfProfileDropPrecedence_Type()
)
rlPolicyGalileoTuningOverrideOutOfProfileDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoTuningOverrideOutOfProfileDropPrecedence.setStatus("mandatory")
_RlCosFftAgingTimeout_Type = Integer32
_RlCosFftAgingTimeout_Object = MibScalar
rlCosFftAgingTimeout = _RlCosFftAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 5),
    _RlCosFftAgingTimeout_Type()
)
rlCosFftAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCosFftAgingTimeout.setStatus("mandatory")
_RlCosFftPollingInterval_Type = Integer32
_RlCosFftPollingInterval_Object = MibScalar
rlCosFftPollingInterval = _RlCosFftPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 6),
    _RlCosFftPollingInterval_Type()
)
rlCosFftPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCosFftPollingInterval.setStatus("mandatory")
_RlPolicyGalileoDebug_ObjectIdentity = ObjectIdentity
rlPolicyGalileoDebug = _RlPolicyGalileoDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 56, 7)
)
_RlPolicyGalileoDebugFcogTable_Object = MibTable
rlPolicyGalileoDebugFcogTable = _RlPolicyGalileoDebugFcogTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1)
)
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFcogTable.setStatus("mandatory")
_RlPolicyGalileoDebugFcogEntry_Object = MibTableRow
rlPolicyGalileoDebugFcogEntry = _RlPolicyGalileoDebugFcogEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1)
)
rlPolicyGalileoDebugFcogEntry.setIndexNames(
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFcogType"),
)
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFcogEntry.setStatus("mandatory")
_RlPolicyGalileoDebugFcogType_Type = RlPolicyGalileoDebugGroupType
_RlPolicyGalileoDebugFcogType_Object = MibTableColumn
rlPolicyGalileoDebugFcogType = _RlPolicyGalileoDebugFcogType_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 1),
    _RlPolicyGalileoDebugFcogType_Type()
)
rlPolicyGalileoDebugFcogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFcogType.setStatus("mandatory")


class _RlPolicyGalileoDebugL2SrcAddr_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugL2SrcAddr based on TruthValue"""


_RlPolicyGalileoDebugL2SrcAddr_Object = MibTableColumn
rlPolicyGalileoDebugL2SrcAddr = _RlPolicyGalileoDebugL2SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 2),
    _RlPolicyGalileoDebugL2SrcAddr_Type()
)
rlPolicyGalileoDebugL2SrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugL2SrcAddr.setStatus("mandatory")


class _RlPolicyGalileoDebugL2DstAddr_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugL2DstAddr based on TruthValue"""


_RlPolicyGalileoDebugL2DstAddr_Object = MibTableColumn
rlPolicyGalileoDebugL2DstAddr = _RlPolicyGalileoDebugL2DstAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 3),
    _RlPolicyGalileoDebugL2DstAddr_Type()
)
rlPolicyGalileoDebugL2DstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugL2DstAddr.setStatus("mandatory")


class _RlPolicyGalileoDebugVlanId_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugVlanId based on TruthValue"""


_RlPolicyGalileoDebugVlanId_Object = MibTableColumn
rlPolicyGalileoDebugVlanId = _RlPolicyGalileoDebugVlanId_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 4),
    _RlPolicyGalileoDebugVlanId_Type()
)
rlPolicyGalileoDebugVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugVlanId.setStatus("mandatory")


class _RlPolicyGalileoDebugInport_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugInport based on TruthValue"""


_RlPolicyGalileoDebugInport_Object = MibTableColumn
rlPolicyGalileoDebugInport = _RlPolicyGalileoDebugInport_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 5),
    _RlPolicyGalileoDebugInport_Type()
)
rlPolicyGalileoDebugInport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugInport.setStatus("mandatory")


class _RlPolicyGalileoDebugIpxDstNet_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugIpxDstNet based on TruthValue"""


_RlPolicyGalileoDebugIpxDstNet_Object = MibTableColumn
rlPolicyGalileoDebugIpxDstNet = _RlPolicyGalileoDebugIpxDstNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 6),
    _RlPolicyGalileoDebugIpxDstNet_Type()
)
rlPolicyGalileoDebugIpxDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugIpxDstNet.setStatus("mandatory")


class _RlPolicyGalileoDebugIpxDstNode_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugIpxDstNode based on TruthValue"""


_RlPolicyGalileoDebugIpxDstNode_Object = MibTableColumn
rlPolicyGalileoDebugIpxDstNode = _RlPolicyGalileoDebugIpxDstNode_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 7),
    _RlPolicyGalileoDebugIpxDstNode_Type()
)
rlPolicyGalileoDebugIpxDstNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugIpxDstNode.setStatus("mandatory")


class _RlPolicyGalileoDebugIpSrcAddr_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugIpSrcAddr based on TruthValue"""


_RlPolicyGalileoDebugIpSrcAddr_Object = MibTableColumn
rlPolicyGalileoDebugIpSrcAddr = _RlPolicyGalileoDebugIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 8),
    _RlPolicyGalileoDebugIpSrcAddr_Type()
)
rlPolicyGalileoDebugIpSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugIpSrcAddr.setStatus("mandatory")


class _RlPolicyGalileoDebugIpDstAddr_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugIpDstAddr based on TruthValue"""


_RlPolicyGalileoDebugIpDstAddr_Object = MibTableColumn
rlPolicyGalileoDebugIpDstAddr = _RlPolicyGalileoDebugIpDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 9),
    _RlPolicyGalileoDebugIpDstAddr_Type()
)
rlPolicyGalileoDebugIpDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugIpDstAddr.setStatus("mandatory")


class _RlPolicyGalileoDebugIpProtocol_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugIpProtocol based on TruthValue"""


_RlPolicyGalileoDebugIpProtocol_Object = MibTableColumn
rlPolicyGalileoDebugIpProtocol = _RlPolicyGalileoDebugIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 10),
    _RlPolicyGalileoDebugIpProtocol_Type()
)
rlPolicyGalileoDebugIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugIpProtocol.setStatus("mandatory")


class _RlPolicyGalileoDebugIpSrcPort_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugIpSrcPort based on TruthValue"""


_RlPolicyGalileoDebugIpSrcPort_Object = MibTableColumn
rlPolicyGalileoDebugIpSrcPort = _RlPolicyGalileoDebugIpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 11),
    _RlPolicyGalileoDebugIpSrcPort_Type()
)
rlPolicyGalileoDebugIpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugIpSrcPort.setStatus("mandatory")


class _RlPolicyGalileoDebugIpDstPort_Type(TruthValue):
    """Custom type rlPolicyGalileoDebugIpDstPort based on TruthValue"""


_RlPolicyGalileoDebugIpDstPort_Object = MibTableColumn
rlPolicyGalileoDebugIpDstPort = _RlPolicyGalileoDebugIpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 12),
    _RlPolicyGalileoDebugIpDstPort_Type()
)
rlPolicyGalileoDebugIpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugIpDstPort.setStatus("mandatory")
_RlPolicyGalileoDebugStatus_Type = RowStatus
_RlPolicyGalileoDebugStatus_Object = MibTableColumn
rlPolicyGalileoDebugStatus = _RlPolicyGalileoDebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 1, 1, 13),
    _RlPolicyGalileoDebugStatus_Type()
)
rlPolicyGalileoDebugStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugStatus.setStatus("mandatory")
_RlPolicyGalileoDebugFlowTable_Object = MibTable
rlPolicyGalileoDebugFlowTable = _RlPolicyGalileoDebugFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2)
)
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowTable.setStatus("mandatory")
_RlPolicyGalileoDebugFlowTableEntry_Object = MibTableRow
rlPolicyGalileoDebugFlowTableEntry = _RlPolicyGalileoDebugFlowTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1)
)
rlPolicyGalileoDebugFlowTableEntry.setIndexNames(
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowType"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowRxIfIndex"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowL2SrcAddr"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowL2DstAddr"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowVlanId"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowIpxDstNet"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowIpxDstNode"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowIpSrcAddr"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowIpDstAddr"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowIpProtocol"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowIpSrcPort"),
    (0, "GALILEO-MIB", "rlPolicyGalileoDebugFlowIpDstPort"),
)
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowTableEntry.setStatus("mandatory")
_RlPolicyGalileoDebugFlowType_Type = RlPolicyGalileoDebugGroupType
_RlPolicyGalileoDebugFlowType_Object = MibTableColumn
rlPolicyGalileoDebugFlowType = _RlPolicyGalileoDebugFlowType_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 1),
    _RlPolicyGalileoDebugFlowType_Type()
)
rlPolicyGalileoDebugFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowType.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRxIfIndex_Type = Integer32
_RlPolicyGalileoDebugFlowRxIfIndex_Object = MibTableColumn
rlPolicyGalileoDebugFlowRxIfIndex = _RlPolicyGalileoDebugFlowRxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 2),
    _RlPolicyGalileoDebugFlowRxIfIndex_Type()
)
rlPolicyGalileoDebugFlowRxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRxIfIndex.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowL2SrcAddr_Type(OctetString):
    """Custom type rlPolicyGalileoDebugFlowL2SrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicyGalileoDebugFlowL2SrcAddr_Type.__name__ = "OctetString"
_RlPolicyGalileoDebugFlowL2SrcAddr_Object = MibTableColumn
rlPolicyGalileoDebugFlowL2SrcAddr = _RlPolicyGalileoDebugFlowL2SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 3),
    _RlPolicyGalileoDebugFlowL2SrcAddr_Type()
)
rlPolicyGalileoDebugFlowL2SrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowL2SrcAddr.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowL2DstAddr_Type(OctetString):
    """Custom type rlPolicyGalileoDebugFlowL2DstAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicyGalileoDebugFlowL2DstAddr_Type.__name__ = "OctetString"
_RlPolicyGalileoDebugFlowL2DstAddr_Object = MibTableColumn
rlPolicyGalileoDebugFlowL2DstAddr = _RlPolicyGalileoDebugFlowL2DstAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 4),
    _RlPolicyGalileoDebugFlowL2DstAddr_Type()
)
rlPolicyGalileoDebugFlowL2DstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowL2DstAddr.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowVlanId_Type(Integer32):
    """Custom type rlPolicyGalileoDebugFlowVlanId based on Integer32"""
    defaultValue = 0


_RlPolicyGalileoDebugFlowVlanId_Object = MibTableColumn
rlPolicyGalileoDebugFlowVlanId = _RlPolicyGalileoDebugFlowVlanId_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 5),
    _RlPolicyGalileoDebugFlowVlanId_Type()
)
rlPolicyGalileoDebugFlowVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowVlanId.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowIpxDstNet_Type(OctetString):
    """Custom type rlPolicyGalileoDebugFlowIpxDstNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlPolicyGalileoDebugFlowIpxDstNet_Type.__name__ = "OctetString"
_RlPolicyGalileoDebugFlowIpxDstNet_Object = MibTableColumn
rlPolicyGalileoDebugFlowIpxDstNet = _RlPolicyGalileoDebugFlowIpxDstNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 6),
    _RlPolicyGalileoDebugFlowIpxDstNet_Type()
)
rlPolicyGalileoDebugFlowIpxDstNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowIpxDstNet.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowIpxDstNode_Type(OctetString):
    """Custom type rlPolicyGalileoDebugFlowIpxDstNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicyGalileoDebugFlowIpxDstNode_Type.__name__ = "OctetString"
_RlPolicyGalileoDebugFlowIpxDstNode_Object = MibTableColumn
rlPolicyGalileoDebugFlowIpxDstNode = _RlPolicyGalileoDebugFlowIpxDstNode_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 7),
    _RlPolicyGalileoDebugFlowIpxDstNode_Type()
)
rlPolicyGalileoDebugFlowIpxDstNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowIpxDstNode.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowIpSrcAddr_Type(OctetString):
    """Custom type rlPolicyGalileoDebugFlowIpSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlPolicyGalileoDebugFlowIpSrcAddr_Type.__name__ = "OctetString"
_RlPolicyGalileoDebugFlowIpSrcAddr_Object = MibTableColumn
rlPolicyGalileoDebugFlowIpSrcAddr = _RlPolicyGalileoDebugFlowIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 8),
    _RlPolicyGalileoDebugFlowIpSrcAddr_Type()
)
rlPolicyGalileoDebugFlowIpSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowIpSrcAddr.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowIpDstAddr_Type(OctetString):
    """Custom type rlPolicyGalileoDebugFlowIpDstAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlPolicyGalileoDebugFlowIpDstAddr_Type.__name__ = "OctetString"
_RlPolicyGalileoDebugFlowIpDstAddr_Object = MibTableColumn
rlPolicyGalileoDebugFlowIpDstAddr = _RlPolicyGalileoDebugFlowIpDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 9),
    _RlPolicyGalileoDebugFlowIpDstAddr_Type()
)
rlPolicyGalileoDebugFlowIpDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowIpDstAddr.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowIpProtocol_Type(Integer32):
    """Custom type rlPolicyGalileoDebugFlowIpProtocol based on Integer32"""
    defaultValue = 0


_RlPolicyGalileoDebugFlowIpProtocol_Object = MibTableColumn
rlPolicyGalileoDebugFlowIpProtocol = _RlPolicyGalileoDebugFlowIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 10),
    _RlPolicyGalileoDebugFlowIpProtocol_Type()
)
rlPolicyGalileoDebugFlowIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowIpProtocol.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowIpSrcPort_Type(OctetString):
    """Custom type rlPolicyGalileoDebugFlowIpSrcPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_RlPolicyGalileoDebugFlowIpSrcPort_Type.__name__ = "OctetString"
_RlPolicyGalileoDebugFlowIpSrcPort_Object = MibTableColumn
rlPolicyGalileoDebugFlowIpSrcPort = _RlPolicyGalileoDebugFlowIpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 11),
    _RlPolicyGalileoDebugFlowIpSrcPort_Type()
)
rlPolicyGalileoDebugFlowIpSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowIpSrcPort.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowIpDstPort_Type(OctetString):
    """Custom type rlPolicyGalileoDebugFlowIpDstPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_RlPolicyGalileoDebugFlowIpDstPort_Type.__name__ = "OctetString"
_RlPolicyGalileoDebugFlowIpDstPort_Object = MibTableColumn
rlPolicyGalileoDebugFlowIpDstPort = _RlPolicyGalileoDebugFlowIpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 12),
    _RlPolicyGalileoDebugFlowIpDstPort_Type()
)
rlPolicyGalileoDebugFlowIpDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowIpDstPort.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRetValid_Type = TruthValue
_RlPolicyGalileoDebugFlowRetValid_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetValid = _RlPolicyGalileoDebugFlowRetValid_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 13),
    _RlPolicyGalileoDebugFlowRetValid_Type()
)
rlPolicyGalileoDebugFlowRetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetValid.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRetStatic_Type = TruthValue
_RlPolicyGalileoDebugFlowRetStatic_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetStatic = _RlPolicyGalileoDebugFlowRetStatic_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 14),
    _RlPolicyGalileoDebugFlowRetStatic_Type()
)
rlPolicyGalileoDebugFlowRetStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetStatic.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRetAging_Type = TruthValue
_RlPolicyGalileoDebugFlowRetAging_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetAging = _RlPolicyGalileoDebugFlowRetAging_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 15),
    _RlPolicyGalileoDebugFlowRetAging_Type()
)
rlPolicyGalileoDebugFlowRetAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetAging.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowRetCmd_Type(Integer32):
    """Custom type rlPolicyGalileoDebugFlowRetCmd based on Integer32"""
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
        *(("drop", 1),
          ("dropAndTrap", 2),
          ("permit", 3),
          ("permitAndTrap", 4))
    )


_RlPolicyGalileoDebugFlowRetCmd_Type.__name__ = "Integer32"
_RlPolicyGalileoDebugFlowRetCmd_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetCmd = _RlPolicyGalileoDebugFlowRetCmd_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 16),
    _RlPolicyGalileoDebugFlowRetCmd_Type()
)
rlPolicyGalileoDebugFlowRetCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetCmd.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRetPrio_Type = Integer32
_RlPolicyGalileoDebugFlowRetPrio_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetPrio = _RlPolicyGalileoDebugFlowRetPrio_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 17),
    _RlPolicyGalileoDebugFlowRetPrio_Type()
)
rlPolicyGalileoDebugFlowRetPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetPrio.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowRetInProfileDis_Type(Integer32):
    """Custom type rlPolicyGalileoDebugFlowRetInProfileDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("high", 2),
          ("low", 1))
    )


_RlPolicyGalileoDebugFlowRetInProfileDis_Type.__name__ = "Integer32"
_RlPolicyGalileoDebugFlowRetInProfileDis_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetInProfileDis = _RlPolicyGalileoDebugFlowRetInProfileDis_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 18),
    _RlPolicyGalileoDebugFlowRetInProfileDis_Type()
)
rlPolicyGalileoDebugFlowRetInProfileDis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetInProfileDis.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRetVpt_Type = Integer32
_RlPolicyGalileoDebugFlowRetVpt_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetVpt = _RlPolicyGalileoDebugFlowRetVpt_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 19),
    _RlPolicyGalileoDebugFlowRetVpt_Type()
)
rlPolicyGalileoDebugFlowRetVpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetVpt.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRetChangeTos_Type = TruthValue
_RlPolicyGalileoDebugFlowRetChangeTos_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetChangeTos = _RlPolicyGalileoDebugFlowRetChangeTos_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 20),
    _RlPolicyGalileoDebugFlowRetChangeTos_Type()
)
rlPolicyGalileoDebugFlowRetChangeTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetChangeTos.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRetNewTos_Type = Integer32
_RlPolicyGalileoDebugFlowRetNewTos_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetNewTos = _RlPolicyGalileoDebugFlowRetNewTos_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 21),
    _RlPolicyGalileoDebugFlowRetNewTos_Type()
)
rlPolicyGalileoDebugFlowRetNewTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetNewTos.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRetVlanId_Type = Integer32
_RlPolicyGalileoDebugFlowRetVlanId_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetVlanId = _RlPolicyGalileoDebugFlowRetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 22),
    _RlPolicyGalileoDebugFlowRetVlanId_Type()
)
rlPolicyGalileoDebugFlowRetVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetVlanId.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRetInIfIndex_Type = Integer32
_RlPolicyGalileoDebugFlowRetInIfIndex_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetInIfIndex = _RlPolicyGalileoDebugFlowRetInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 23),
    _RlPolicyGalileoDebugFlowRetInIfIndex_Type()
)
rlPolicyGalileoDebugFlowRetInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetInIfIndex.setStatus("mandatory")
_RlPolicyGalileoDebugFlowRetEnableMeter_Type = TruthValue
_RlPolicyGalileoDebugFlowRetEnableMeter_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetEnableMeter = _RlPolicyGalileoDebugFlowRetEnableMeter_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 24),
    _RlPolicyGalileoDebugFlowRetEnableMeter_Type()
)
rlPolicyGalileoDebugFlowRetEnableMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetEnableMeter.setStatus("mandatory")


class _RlPolicyGalileoDebugFlowRetOutProfileDis_Type(Integer32):
    """Custom type rlPolicyGalileoDebugFlowRetOutProfileDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("high", 2),
          ("low", 1))
    )


_RlPolicyGalileoDebugFlowRetOutProfileDis_Type.__name__ = "Integer32"
_RlPolicyGalileoDebugFlowRetOutProfileDis_Object = MibTableColumn
rlPolicyGalileoDebugFlowRetOutProfileDis = _RlPolicyGalileoDebugFlowRetOutProfileDis_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 7, 2, 1, 25),
    _RlPolicyGalileoDebugFlowRetOutProfileDis_Type()
)
rlPolicyGalileoDebugFlowRetOutProfileDis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoDebugFlowRetOutProfileDis.setStatus("mandatory")
_RlPolicyGalileoFcuFwdCpuCounter_Type = Integer32
_RlPolicyGalileoFcuFwdCpuCounter_Object = MibScalar
rlPolicyGalileoFcuFwdCpuCounter = _RlPolicyGalileoFcuFwdCpuCounter_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 8),
    _RlPolicyGalileoFcuFwdCpuCounter_Type()
)
rlPolicyGalileoFcuFwdCpuCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicyGalileoFcuFwdCpuCounter.setStatus("mandatory")
_RlPolicySimpleGalMib_ObjectIdentity = ObjectIdentity
rlPolicySimpleGalMib = _RlPolicySimpleGalMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 56, 9)
)
_RlPolicySimpleGalMibVersion_Type = Integer32
_RlPolicySimpleGalMibVersion_Object = MibScalar
rlPolicySimpleGalMibVersion = _RlPolicySimpleGalMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 1),
    _RlPolicySimpleGalMibVersion_Type()
)
rlPolicySimpleGalMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibVersion.setStatus("mandatory")


class _RlPolicySimpleGalMibPortTypeSupport_Type(OctetString):
    """Custom type rlPolicySimpleGalMibPortTypeSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlPolicySimpleGalMibPortTypeSupport_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibPortTypeSupport_Object = MibScalar
rlPolicySimpleGalMibPortTypeSupport = _RlPolicySimpleGalMibPortTypeSupport_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 2),
    _RlPolicySimpleGalMibPortTypeSupport_Type()
)
rlPolicySimpleGalMibPortTypeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibPortTypeSupport.setStatus("mandatory")


class _RlPolicySimpleGalMibRecalculateRules_Type(Integer32):
    """Custom type rlPolicySimpleGalMibRecalculateRules based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("recalculate", 1)
    )


_RlPolicySimpleGalMibRecalculateRules_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibRecalculateRules_Object = MibScalar
rlPolicySimpleGalMibRecalculateRules = _RlPolicySimpleGalMibRecalculateRules_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 3),
    _RlPolicySimpleGalMibRecalculateRules_Type()
)
rlPolicySimpleGalMibRecalculateRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibRecalculateRules.setStatus("mandatory")


class _RlPolicySimpleGalMibPolicyEnable_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibPolicyEnable based on TruthValue"""


_RlPolicySimpleGalMibPolicyEnable_Object = MibScalar
rlPolicySimpleGalMibPolicyEnable = _RlPolicySimpleGalMibPolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 4),
    _RlPolicySimpleGalMibPolicyEnable_Type()
)
rlPolicySimpleGalMibPolicyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibPolicyEnable.setStatus("mandatory")
_RlPolicySimpleGalMibProfileTable_Object = MibTable
rlPolicySimpleGalMibProfileTable = _RlPolicySimpleGalMibProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5)
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibProfileTable.setStatus("mandatory")
_RlPolicySimpleGalMibProfileEntry_Object = MibTableRow
rlPolicySimpleGalMibProfileEntry = _RlPolicySimpleGalMibProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1)
)
rlPolicySimpleGalMibProfileEntry.setIndexNames(
    (0, "GALILEO-MIB", "rlPolicySimpleGalMibIndex"),
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibProfileEntry.setStatus("mandatory")


class _RlPolicySimpleGalMibIndex_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicySimpleGalMibIndex_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIndex_Object = MibTableColumn
rlPolicySimpleGalMibIndex = _RlPolicySimpleGalMibIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1, 1),
    _RlPolicySimpleGalMibIndex_Type()
)
rlPolicySimpleGalMibIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIndex.setStatus("mandatory")


class _RlPolicySimpleGalMibDescription_Type(DisplayString):
    """Custom type rlPolicySimpleGalMibDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RlPolicySimpleGalMibDescription_Type.__name__ = "DisplayString"
_RlPolicySimpleGalMibDescription_Object = MibTableColumn
rlPolicySimpleGalMibDescription = _RlPolicySimpleGalMibDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1, 2),
    _RlPolicySimpleGalMibDescription_Type()
)
rlPolicySimpleGalMibDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibDescription.setStatus("mandatory")
_RlPolicySimpleGalMibProfileType_Type = RlPolicySimpleGalMibProfileType
_RlPolicySimpleGalMibProfileType_Object = MibTableColumn
rlPolicySimpleGalMibProfileType = _RlPolicySimpleGalMibProfileType_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1, 3),
    _RlPolicySimpleGalMibProfileType_Type()
)
rlPolicySimpleGalMibProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibProfileType.setStatus("mandatory")


class _RlPolicySimpleGalMibRate_Type(Integer32):
    """Custom type rlPolicySimpleGalMibRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicySimpleGalMibRate_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibRate_Object = MibTableColumn
rlPolicySimpleGalMibRate = _RlPolicySimpleGalMibRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1, 4),
    _RlPolicySimpleGalMibRate_Type()
)
rlPolicySimpleGalMibRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibRate.setStatus("mandatory")


class _RlPolicySimpleGalMibBurstSize_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPolicySimpleGalMibBurstSize_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBurstSize_Object = MibTableColumn
rlPolicySimpleGalMibBurstSize = _RlPolicySimpleGalMibBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1, 5),
    _RlPolicySimpleGalMibBurstSize_Type()
)
rlPolicySimpleGalMibBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBurstSize.setStatus("mandatory")


class _RlPolicySimpleGalMibMaxSession_Type(Integer32):
    """Custom type rlPolicySimpleGalMibMaxSession based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicySimpleGalMibMaxSession_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibMaxSession_Object = MibTableColumn
rlPolicySimpleGalMibMaxSession = _RlPolicySimpleGalMibMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1, 6),
    _RlPolicySimpleGalMibMaxSession_Type()
)
rlPolicySimpleGalMibMaxSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibMaxSession.setStatus("mandatory")


class _RlPolicySimpleGalMibNewVpt_Type(Integer32):
    """Custom type rlPolicySimpleGalMibNewVpt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlPolicySimpleGalMibNewVpt_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibNewVpt_Object = MibTableColumn
rlPolicySimpleGalMibNewVpt = _RlPolicySimpleGalMibNewVpt_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1, 7),
    _RlPolicySimpleGalMibNewVpt_Type()
)
rlPolicySimpleGalMibNewVpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibNewVpt.setStatus("mandatory")


class _RlPolicySimpleGalMibChangeTosOrDscp_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibChangeTosOrDscp based on TruthValue"""


_RlPolicySimpleGalMibChangeTosOrDscp_Object = MibTableColumn
rlPolicySimpleGalMibChangeTosOrDscp = _RlPolicySimpleGalMibChangeTosOrDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1, 8),
    _RlPolicySimpleGalMibChangeTosOrDscp_Type()
)
rlPolicySimpleGalMibChangeTosOrDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibChangeTosOrDscp.setStatus("mandatory")


class _RlPolicySimpleGalMibNewTosOrDscp_Type(Integer32):
    """Custom type rlPolicySimpleGalMibNewTosOrDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlPolicySimpleGalMibNewTosOrDscp_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibNewTosOrDscp_Object = MibTableColumn
rlPolicySimpleGalMibNewTosOrDscp = _RlPolicySimpleGalMibNewTosOrDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1, 9),
    _RlPolicySimpleGalMibNewTosOrDscp_Type()
)
rlPolicySimpleGalMibNewTosOrDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibNewTosOrDscp.setStatus("mandatory")
_RlPolicySimpleGalMibStatus_Type = RowStatus
_RlPolicySimpleGalMibStatus_Object = MibTableColumn
rlPolicySimpleGalMibStatus = _RlPolicySimpleGalMibStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 5, 1, 10),
    _RlPolicySimpleGalMibStatus_Type()
)
rlPolicySimpleGalMibStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibStatus.setStatus("mandatory")
_RlPolicySimpleGalMibIpFcogTable_Object = MibTable
rlPolicySimpleGalMibIpFcogTable = _RlPolicySimpleGalMibIpFcogTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 6)
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpFcogTable.setStatus("mandatory")
_RlPolicySimpleGalMibIpFcogEntry_Object = MibTableRow
rlPolicySimpleGalMibIpFcogEntry = _RlPolicySimpleGalMibIpFcogEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 6, 1)
)
rlPolicySimpleGalMibIpFcogEntry.setIndexNames(
    (0, "GALILEO-MIB", "rlPolicySimpleGalMibIpFcogPortType"),
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpFcogEntry.setStatus("mandatory")
_RlPolicySimpleGalMibIpFcogPortType_Type = RlPolicySimpleGalMibPortType
_RlPolicySimpleGalMibIpFcogPortType_Object = MibTableColumn
rlPolicySimpleGalMibIpFcogPortType = _RlPolicySimpleGalMibIpFcogPortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 6, 1, 1),
    _RlPolicySimpleGalMibIpFcogPortType_Type()
)
rlPolicySimpleGalMibIpFcogPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpFcogPortType.setStatus("mandatory")


class _RlPolicySimpleGalMibIpFcogTosOrDscp_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibIpFcogTosOrDscp based on TruthValue"""


_RlPolicySimpleGalMibIpFcogTosOrDscp_Object = MibTableColumn
rlPolicySimpleGalMibIpFcogTosOrDscp = _RlPolicySimpleGalMibIpFcogTosOrDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 6, 1, 2),
    _RlPolicySimpleGalMibIpFcogTosOrDscp_Type()
)
rlPolicySimpleGalMibIpFcogTosOrDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpFcogTosOrDscp.setStatus("mandatory")


class _RlPolicySimpleGalMibIpFcogProtocol_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibIpFcogProtocol based on TruthValue"""


_RlPolicySimpleGalMibIpFcogProtocol_Object = MibTableColumn
rlPolicySimpleGalMibIpFcogProtocol = _RlPolicySimpleGalMibIpFcogProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 6, 1, 3),
    _RlPolicySimpleGalMibIpFcogProtocol_Type()
)
rlPolicySimpleGalMibIpFcogProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpFcogProtocol.setStatus("mandatory")


class _RlPolicySimpleGalMibIpFcogSrcIpMask_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpFcogSrcIpMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RlPolicySimpleGalMibIpFcogSrcIpMask_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpFcogSrcIpMask_Object = MibTableColumn
rlPolicySimpleGalMibIpFcogSrcIpMask = _RlPolicySimpleGalMibIpFcogSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 6, 1, 4),
    _RlPolicySimpleGalMibIpFcogSrcIpMask_Type()
)
rlPolicySimpleGalMibIpFcogSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpFcogSrcIpMask.setStatus("mandatory")


class _RlPolicySimpleGalMibIpFcogDstIpMask_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpFcogDstIpMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RlPolicySimpleGalMibIpFcogDstIpMask_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpFcogDstIpMask_Object = MibTableColumn
rlPolicySimpleGalMibIpFcogDstIpMask = _RlPolicySimpleGalMibIpFcogDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 6, 1, 5),
    _RlPolicySimpleGalMibIpFcogDstIpMask_Type()
)
rlPolicySimpleGalMibIpFcogDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpFcogDstIpMask.setStatus("mandatory")


class _RlPolicySimpleGalMibIpFcogSrcPort_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibIpFcogSrcPort based on TruthValue"""


_RlPolicySimpleGalMibIpFcogSrcPort_Object = MibTableColumn
rlPolicySimpleGalMibIpFcogSrcPort = _RlPolicySimpleGalMibIpFcogSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 6, 1, 6),
    _RlPolicySimpleGalMibIpFcogSrcPort_Type()
)
rlPolicySimpleGalMibIpFcogSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpFcogSrcPort.setStatus("mandatory")


class _RlPolicySimpleGalMibIpFcogDstPort_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibIpFcogDstPort based on TruthValue"""


_RlPolicySimpleGalMibIpFcogDstPort_Object = MibTableColumn
rlPolicySimpleGalMibIpFcogDstPort = _RlPolicySimpleGalMibIpFcogDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 6, 1, 7),
    _RlPolicySimpleGalMibIpFcogDstPort_Type()
)
rlPolicySimpleGalMibIpFcogDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpFcogDstPort.setStatus("mandatory")


class _RlPolicySimpleGalMibIpFcogInIfIndex_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibIpFcogInIfIndex based on TruthValue"""


_RlPolicySimpleGalMibIpFcogInIfIndex_Object = MibTableColumn
rlPolicySimpleGalMibIpFcogInIfIndex = _RlPolicySimpleGalMibIpFcogInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 6, 1, 8),
    _RlPolicySimpleGalMibIpFcogInIfIndex_Type()
)
rlPolicySimpleGalMibIpFcogInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpFcogInIfIndex.setStatus("mandatory")
_RlPolicySimpleGalMibIpRulesTable_Object = MibTable
rlPolicySimpleGalMibIpRulesTable = _RlPolicySimpleGalMibIpRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7)
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesTable.setStatus("mandatory")
_RlPolicySimpleGalMibIpRulesEntry_Object = MibTableRow
rlPolicySimpleGalMibIpRulesEntry = _RlPolicySimpleGalMibIpRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1)
)
rlPolicySimpleGalMibIpRulesEntry.setIndexNames(
    (0, "GALILEO-MIB", "rlPolicySimpleGalMibIpRulesPortType"),
    (0, "GALILEO-MIB", "rlPolicySimpleGalMibIpRulesIndex"),
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesEntry.setStatus("mandatory")
_RlPolicySimpleGalMibIpRulesPortType_Type = RlPolicySimpleGalMibPortType
_RlPolicySimpleGalMibIpRulesPortType_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesPortType = _RlPolicySimpleGalMibIpRulesPortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 1),
    _RlPolicySimpleGalMibIpRulesPortType_Type()
)
rlPolicySimpleGalMibIpRulesPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesPortType.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesIndex_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpRulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicySimpleGalMibIpRulesIndex_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpRulesIndex_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesIndex = _RlPolicySimpleGalMibIpRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 2),
    _RlPolicySimpleGalMibIpRulesIndex_Type()
)
rlPolicySimpleGalMibIpRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesIndex.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesDescription_Type(DisplayString):
    """Custom type rlPolicySimpleGalMibIpRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RlPolicySimpleGalMibIpRulesDescription_Type.__name__ = "DisplayString"
_RlPolicySimpleGalMibIpRulesDescription_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesDescription = _RlPolicySimpleGalMibIpRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 3),
    _RlPolicySimpleGalMibIpRulesDescription_Type()
)
rlPolicySimpleGalMibIpRulesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesDescription.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesTosOrDscp_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpRulesTosOrDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlPolicySimpleGalMibIpRulesTosOrDscp_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpRulesTosOrDscp_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesTosOrDscp = _RlPolicySimpleGalMibIpRulesTosOrDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 4),
    _RlPolicySimpleGalMibIpRulesTosOrDscp_Type()
)
rlPolicySimpleGalMibIpRulesTosOrDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesTosOrDscp.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesProtocol_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpRulesProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlPolicySimpleGalMibIpRulesProtocol_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpRulesProtocol_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesProtocol = _RlPolicySimpleGalMibIpRulesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 5),
    _RlPolicySimpleGalMibIpRulesProtocol_Type()
)
rlPolicySimpleGalMibIpRulesProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesProtocol.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesSrcIp_Type(IpAddress):
    """Custom type rlPolicySimpleGalMibIpRulesSrcIp based on IpAddress"""
    defaultHexValue = "00000000"


_RlPolicySimpleGalMibIpRulesSrcIp_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesSrcIp = _RlPolicySimpleGalMibIpRulesSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 6),
    _RlPolicySimpleGalMibIpRulesSrcIp_Type()
)
rlPolicySimpleGalMibIpRulesSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesSrcIp.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesSrcIpMask_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpRulesSrcIpMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RlPolicySimpleGalMibIpRulesSrcIpMask_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpRulesSrcIpMask_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesSrcIpMask = _RlPolicySimpleGalMibIpRulesSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 7),
    _RlPolicySimpleGalMibIpRulesSrcIpMask_Type()
)
rlPolicySimpleGalMibIpRulesSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesSrcIpMask.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesDstIp_Type(IpAddress):
    """Custom type rlPolicySimpleGalMibIpRulesDstIp based on IpAddress"""
    defaultHexValue = "00000000"


_RlPolicySimpleGalMibIpRulesDstIp_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesDstIp = _RlPolicySimpleGalMibIpRulesDstIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 8),
    _RlPolicySimpleGalMibIpRulesDstIp_Type()
)
rlPolicySimpleGalMibIpRulesDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesDstIp.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesDstIpMask_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpRulesDstIpMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RlPolicySimpleGalMibIpRulesDstIpMask_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpRulesDstIpMask_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesDstIpMask = _RlPolicySimpleGalMibIpRulesDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 9),
    _RlPolicySimpleGalMibIpRulesDstIpMask_Type()
)
rlPolicySimpleGalMibIpRulesDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesDstIpMask.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesSrcPort_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpRulesSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicySimpleGalMibIpRulesSrcPort_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpRulesSrcPort_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesSrcPort = _RlPolicySimpleGalMibIpRulesSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 10),
    _RlPolicySimpleGalMibIpRulesSrcPort_Type()
)
rlPolicySimpleGalMibIpRulesSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesSrcPort.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesDstPort_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpRulesDstPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicySimpleGalMibIpRulesDstPort_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpRulesDstPort_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesDstPort = _RlPolicySimpleGalMibIpRulesDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 11),
    _RlPolicySimpleGalMibIpRulesDstPort_Type()
)
rlPolicySimpleGalMibIpRulesDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesDstPort.setStatus("mandatory")
_RlPolicySimpleGalMibIpRulesInIfIndexList_Type = PortList
_RlPolicySimpleGalMibIpRulesInIfIndexList_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesInIfIndexList = _RlPolicySimpleGalMibIpRulesInIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 12),
    _RlPolicySimpleGalMibIpRulesInIfIndexList_Type()
)
rlPolicySimpleGalMibIpRulesInIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesInIfIndexList.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesCondition_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpRulesCondition based on Integer32"""
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
        *(("bigger", 3),
          ("equal", 1),
          ("notEqual", 2),
          ("smaller", 4))
    )


_RlPolicySimpleGalMibIpRulesCondition_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpRulesCondition_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesCondition = _RlPolicySimpleGalMibIpRulesCondition_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 13),
    _RlPolicySimpleGalMibIpRulesCondition_Type()
)
rlPolicySimpleGalMibIpRulesCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesCondition.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesAction_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpRulesAction based on Integer32"""
    defaultValue = 4

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
        *(("block", 1),
          ("blockAndTrap", 2),
          ("permit", 4),
          ("permitAndTrap", 3))
    )


_RlPolicySimpleGalMibIpRulesAction_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpRulesAction_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesAction = _RlPolicySimpleGalMibIpRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 14),
    _RlPolicySimpleGalMibIpRulesAction_Type()
)
rlPolicySimpleGalMibIpRulesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesAction.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesProfilePointer_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpRulesProfilePointer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPolicySimpleGalMibIpRulesProfilePointer_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpRulesProfilePointer_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesProfilePointer = _RlPolicySimpleGalMibIpRulesProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 15),
    _RlPolicySimpleGalMibIpRulesProfilePointer_Type()
)
rlPolicySimpleGalMibIpRulesProfilePointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesProfilePointer.setStatus("mandatory")
_RlPolicySimpleGalMibIpRulesOutIfIndexList_Type = PortList
_RlPolicySimpleGalMibIpRulesOutIfIndexList_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesOutIfIndexList = _RlPolicySimpleGalMibIpRulesOutIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 16),
    _RlPolicySimpleGalMibIpRulesOutIfIndexList_Type()
)
rlPolicySimpleGalMibIpRulesOutIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesOutIfIndexList.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesBitsUsed_Type(OctetString):
    """Custom type rlPolicySimpleGalMibIpRulesBitsUsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlPolicySimpleGalMibIpRulesBitsUsed_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibIpRulesBitsUsed_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesBitsUsed = _RlPolicySimpleGalMibIpRulesBitsUsed_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 17),
    _RlPolicySimpleGalMibIpRulesBitsUsed_Type()
)
rlPolicySimpleGalMibIpRulesBitsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesBitsUsed.setStatus("mandatory")


class _RlPolicySimpleGalMibIpRulesErrorDescrip_Type(DisplayString):
    """Custom type rlPolicySimpleGalMibIpRulesErrorDescrip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlPolicySimpleGalMibIpRulesErrorDescrip_Type.__name__ = "DisplayString"
_RlPolicySimpleGalMibIpRulesErrorDescrip_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesErrorDescrip = _RlPolicySimpleGalMibIpRulesErrorDescrip_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 18),
    _RlPolicySimpleGalMibIpRulesErrorDescrip_Type()
)
rlPolicySimpleGalMibIpRulesErrorDescrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesErrorDescrip.setStatus("mandatory")
_RlPolicySimpleGalMibIpRulesStatus_Type = RowStatus
_RlPolicySimpleGalMibIpRulesStatus_Object = MibTableColumn
rlPolicySimpleGalMibIpRulesStatus = _RlPolicySimpleGalMibIpRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 7, 1, 19),
    _RlPolicySimpleGalMibIpRulesStatus_Type()
)
rlPolicySimpleGalMibIpRulesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpRulesStatus.setStatus("mandatory")
_RlPolicySimpleGalMibIpxFcogTable_Object = MibTable
rlPolicySimpleGalMibIpxFcogTable = _RlPolicySimpleGalMibIpxFcogTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 8)
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxFcogTable.setStatus("mandatory")
_RlPolicySimpleGalMibIpxFcogEntry_Object = MibTableRow
rlPolicySimpleGalMibIpxFcogEntry = _RlPolicySimpleGalMibIpxFcogEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 8, 1)
)
rlPolicySimpleGalMibIpxFcogEntry.setIndexNames(
    (0, "GALILEO-MIB", "rlPolicySimpleGalMibIpxFcogIndex"),
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxFcogEntry.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxFcogIndex_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpxFcogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RlPolicySimpleGalMibIpxFcogIndex_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpxFcogIndex_Object = MibTableColumn
rlPolicySimpleGalMibIpxFcogIndex = _RlPolicySimpleGalMibIpxFcogIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 8, 1, 1),
    _RlPolicySimpleGalMibIpxFcogIndex_Type()
)
rlPolicySimpleGalMibIpxFcogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxFcogIndex.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxFcogDstNet_Type(OctetString):
    """Custom type rlPolicySimpleGalMibIpxFcogDstNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlPolicySimpleGalMibIpxFcogDstNet_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibIpxFcogDstNet_Object = MibTableColumn
rlPolicySimpleGalMibIpxFcogDstNet = _RlPolicySimpleGalMibIpxFcogDstNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 8, 1, 2),
    _RlPolicySimpleGalMibIpxFcogDstNet_Type()
)
rlPolicySimpleGalMibIpxFcogDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxFcogDstNet.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxFcogDstNode_Type(OctetString):
    """Custom type rlPolicySimpleGalMibIpxFcogDstNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicySimpleGalMibIpxFcogDstNode_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibIpxFcogDstNode_Object = MibTableColumn
rlPolicySimpleGalMibIpxFcogDstNode = _RlPolicySimpleGalMibIpxFcogDstNode_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 8, 1, 3),
    _RlPolicySimpleGalMibIpxFcogDstNode_Type()
)
rlPolicySimpleGalMibIpxFcogDstNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxFcogDstNode.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxFcogDstSocket_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibIpxFcogDstSocket based on TruthValue"""


_RlPolicySimpleGalMibIpxFcogDstSocket_Object = MibTableColumn
rlPolicySimpleGalMibIpxFcogDstSocket = _RlPolicySimpleGalMibIpxFcogDstSocket_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 8, 1, 4),
    _RlPolicySimpleGalMibIpxFcogDstSocket_Type()
)
rlPolicySimpleGalMibIpxFcogDstSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxFcogDstSocket.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxFcogSrcNet_Type(OctetString):
    """Custom type rlPolicySimpleGalMibIpxFcogSrcNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlPolicySimpleGalMibIpxFcogSrcNet_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibIpxFcogSrcNet_Object = MibTableColumn
rlPolicySimpleGalMibIpxFcogSrcNet = _RlPolicySimpleGalMibIpxFcogSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 8, 1, 5),
    _RlPolicySimpleGalMibIpxFcogSrcNet_Type()
)
rlPolicySimpleGalMibIpxFcogSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxFcogSrcNet.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxFcogSrcNode_Type(OctetString):
    """Custom type rlPolicySimpleGalMibIpxFcogSrcNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicySimpleGalMibIpxFcogSrcNode_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibIpxFcogSrcNode_Object = MibTableColumn
rlPolicySimpleGalMibIpxFcogSrcNode = _RlPolicySimpleGalMibIpxFcogSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 8, 1, 6),
    _RlPolicySimpleGalMibIpxFcogSrcNode_Type()
)
rlPolicySimpleGalMibIpxFcogSrcNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxFcogSrcNode.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxFcogSrcSocket_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibIpxFcogSrcSocket based on TruthValue"""


_RlPolicySimpleGalMibIpxFcogSrcSocket_Object = MibTableColumn
rlPolicySimpleGalMibIpxFcogSrcSocket = _RlPolicySimpleGalMibIpxFcogSrcSocket_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 8, 1, 7),
    _RlPolicySimpleGalMibIpxFcogSrcSocket_Type()
)
rlPolicySimpleGalMibIpxFcogSrcSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxFcogSrcSocket.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxFcogInIfIndex_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibIpxFcogInIfIndex based on TruthValue"""


_RlPolicySimpleGalMibIpxFcogInIfIndex_Object = MibTableColumn
rlPolicySimpleGalMibIpxFcogInIfIndex = _RlPolicySimpleGalMibIpxFcogInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 8, 1, 8),
    _RlPolicySimpleGalMibIpxFcogInIfIndex_Type()
)
rlPolicySimpleGalMibIpxFcogInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxFcogInIfIndex.setStatus("mandatory")
_RlPolicySimpleGalMibIpxRulesTable_Object = MibTable
rlPolicySimpleGalMibIpxRulesTable = _RlPolicySimpleGalMibIpxRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9)
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesTable.setStatus("mandatory")
_RlPolicySimpleGalMibIpxRulesEntry_Object = MibTableRow
rlPolicySimpleGalMibIpxRulesEntry = _RlPolicySimpleGalMibIpxRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1)
)
rlPolicySimpleGalMibIpxRulesEntry.setIndexNames(
    (0, "GALILEO-MIB", "rlPolicySimpleGalMibIpxRulesIndex"),
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesEntry.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesIndex_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpxRulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicySimpleGalMibIpxRulesIndex_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpxRulesIndex_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesIndex = _RlPolicySimpleGalMibIpxRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 1),
    _RlPolicySimpleGalMibIpxRulesIndex_Type()
)
rlPolicySimpleGalMibIpxRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesIndex.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesDescription_Type(DisplayString):
    """Custom type rlPolicySimpleGalMibIpxRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RlPolicySimpleGalMibIpxRulesDescription_Type.__name__ = "DisplayString"
_RlPolicySimpleGalMibIpxRulesDescription_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesDescription = _RlPolicySimpleGalMibIpxRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 2),
    _RlPolicySimpleGalMibIpxRulesDescription_Type()
)
rlPolicySimpleGalMibIpxRulesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesDescription.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesDstNet_Type(OctetString):
    """Custom type rlPolicySimpleGalMibIpxRulesDstNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlPolicySimpleGalMibIpxRulesDstNet_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibIpxRulesDstNet_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesDstNet = _RlPolicySimpleGalMibIpxRulesDstNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 3),
    _RlPolicySimpleGalMibIpxRulesDstNet_Type()
)
rlPolicySimpleGalMibIpxRulesDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesDstNet.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesDstNode_Type(OctetString):
    """Custom type rlPolicySimpleGalMibIpxRulesDstNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicySimpleGalMibIpxRulesDstNode_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibIpxRulesDstNode_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesDstNode = _RlPolicySimpleGalMibIpxRulesDstNode_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 4),
    _RlPolicySimpleGalMibIpxRulesDstNode_Type()
)
rlPolicySimpleGalMibIpxRulesDstNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesDstNode.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesDstSocket_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpxRulesDstSocket based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicySimpleGalMibIpxRulesDstSocket_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpxRulesDstSocket_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesDstSocket = _RlPolicySimpleGalMibIpxRulesDstSocket_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 5),
    _RlPolicySimpleGalMibIpxRulesDstSocket_Type()
)
rlPolicySimpleGalMibIpxRulesDstSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesDstSocket.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesSrcNet_Type(OctetString):
    """Custom type rlPolicySimpleGalMibIpxRulesSrcNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlPolicySimpleGalMibIpxRulesSrcNet_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibIpxRulesSrcNet_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesSrcNet = _RlPolicySimpleGalMibIpxRulesSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 6),
    _RlPolicySimpleGalMibIpxRulesSrcNet_Type()
)
rlPolicySimpleGalMibIpxRulesSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesSrcNet.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesSrcNode_Type(OctetString):
    """Custom type rlPolicySimpleGalMibIpxRulesSrcNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicySimpleGalMibIpxRulesSrcNode_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibIpxRulesSrcNode_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesSrcNode = _RlPolicySimpleGalMibIpxRulesSrcNode_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 7),
    _RlPolicySimpleGalMibIpxRulesSrcNode_Type()
)
rlPolicySimpleGalMibIpxRulesSrcNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesSrcNode.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesSrcSocket_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpxRulesSrcSocket based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicySimpleGalMibIpxRulesSrcSocket_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpxRulesSrcSocket_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesSrcSocket = _RlPolicySimpleGalMibIpxRulesSrcSocket_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 8),
    _RlPolicySimpleGalMibIpxRulesSrcSocket_Type()
)
rlPolicySimpleGalMibIpxRulesSrcSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesSrcSocket.setStatus("mandatory")
_RlPolicySimpleGalMibIpxRulesInIfIndexList_Type = PortList
_RlPolicySimpleGalMibIpxRulesInIfIndexList_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesInIfIndexList = _RlPolicySimpleGalMibIpxRulesInIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 9),
    _RlPolicySimpleGalMibIpxRulesInIfIndexList_Type()
)
rlPolicySimpleGalMibIpxRulesInIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesInIfIndexList.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesCondition_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpxRulesCondition based on Integer32"""
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
        *(("bigger", 3),
          ("equal", 1),
          ("notEqual", 2),
          ("smaller", 4))
    )


_RlPolicySimpleGalMibIpxRulesCondition_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpxRulesCondition_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesCondition = _RlPolicySimpleGalMibIpxRulesCondition_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 10),
    _RlPolicySimpleGalMibIpxRulesCondition_Type()
)
rlPolicySimpleGalMibIpxRulesCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesCondition.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesAction_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpxRulesAction based on Integer32"""
    defaultValue = 4

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
        *(("block", 1),
          ("blockAndTrap", 2),
          ("permit", 4),
          ("permitAndTrap", 3))
    )


_RlPolicySimpleGalMibIpxRulesAction_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpxRulesAction_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesAction = _RlPolicySimpleGalMibIpxRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 11),
    _RlPolicySimpleGalMibIpxRulesAction_Type()
)
rlPolicySimpleGalMibIpxRulesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesAction.setStatus("mandatory")


class _RlPolicySimpleGalMibIpxRulesProfilePointer_Type(Integer32):
    """Custom type rlPolicySimpleGalMibIpxRulesProfilePointer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPolicySimpleGalMibIpxRulesProfilePointer_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibIpxRulesProfilePointer_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesProfilePointer = _RlPolicySimpleGalMibIpxRulesProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 12),
    _RlPolicySimpleGalMibIpxRulesProfilePointer_Type()
)
rlPolicySimpleGalMibIpxRulesProfilePointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesProfilePointer.setStatus("mandatory")
_RlPolicySimpleGalMibIpxRulesOutIfIndexList_Type = PortList
_RlPolicySimpleGalMibIpxRulesOutIfIndexList_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesOutIfIndexList = _RlPolicySimpleGalMibIpxRulesOutIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 13),
    _RlPolicySimpleGalMibIpxRulesOutIfIndexList_Type()
)
rlPolicySimpleGalMibIpxRulesOutIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesOutIfIndexList.setStatus("mandatory")
_RlPolicySimpleGalMibIpxRulesStatus_Type = RowStatus
_RlPolicySimpleGalMibIpxRulesStatus_Object = MibTableColumn
rlPolicySimpleGalMibIpxRulesStatus = _RlPolicySimpleGalMibIpxRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 9, 1, 14),
    _RlPolicySimpleGalMibIpxRulesStatus_Type()
)
rlPolicySimpleGalMibIpxRulesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibIpxRulesStatus.setStatus("mandatory")
_RlPolicySimpleGalMibBridgeFcogTable_Object = MibTable
rlPolicySimpleGalMibBridgeFcogTable = _RlPolicySimpleGalMibBridgeFcogTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10)
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogTable.setStatus("mandatory")
_RlPolicySimpleGalMibBridgeFcogEntry_Object = MibTableRow
rlPolicySimpleGalMibBridgeFcogEntry = _RlPolicySimpleGalMibBridgeFcogEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1)
)
rlPolicySimpleGalMibBridgeFcogEntry.setIndexNames(
    (0, "GALILEO-MIB", "rlPolicySimpleGalMibBridgeFcogIndex"),
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogEntry.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogIndex_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeFcogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RlPolicySimpleGalMibBridgeFcogIndex_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeFcogIndex_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogIndex = _RlPolicySimpleGalMibBridgeFcogIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 1),
    _RlPolicySimpleGalMibBridgeFcogIndex_Type()
)
rlPolicySimpleGalMibBridgeFcogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogIndex.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogDstMac_Type(OctetString):
    """Custom type rlPolicySimpleGalMibBridgeFcogDstMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicySimpleGalMibBridgeFcogDstMac_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibBridgeFcogDstMac_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogDstMac = _RlPolicySimpleGalMibBridgeFcogDstMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 2),
    _RlPolicySimpleGalMibBridgeFcogDstMac_Type()
)
rlPolicySimpleGalMibBridgeFcogDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogDstMac.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogSrcMac_Type(OctetString):
    """Custom type rlPolicySimpleGalMibBridgeFcogSrcMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicySimpleGalMibBridgeFcogSrcMac_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibBridgeFcogSrcMac_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogSrcMac = _RlPolicySimpleGalMibBridgeFcogSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 3),
    _RlPolicySimpleGalMibBridgeFcogSrcMac_Type()
)
rlPolicySimpleGalMibBridgeFcogSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogSrcMac.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogVid_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibBridgeFcogVid based on TruthValue"""


_RlPolicySimpleGalMibBridgeFcogVid_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogVid = _RlPolicySimpleGalMibBridgeFcogVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 4),
    _RlPolicySimpleGalMibBridgeFcogVid_Type()
)
rlPolicySimpleGalMibBridgeFcogVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogVid.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogInIfIndex_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibBridgeFcogInIfIndex based on TruthValue"""


_RlPolicySimpleGalMibBridgeFcogInIfIndex_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogInIfIndex = _RlPolicySimpleGalMibBridgeFcogInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 5),
    _RlPolicySimpleGalMibBridgeFcogInIfIndex_Type()
)
rlPolicySimpleGalMibBridgeFcogInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogInIfIndex.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogEthType_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibBridgeFcogEthType based on TruthValue"""


_RlPolicySimpleGalMibBridgeFcogEthType_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogEthType = _RlPolicySimpleGalMibBridgeFcogEthType_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 6),
    _RlPolicySimpleGalMibBridgeFcogEthType_Type()
)
rlPolicySimpleGalMibBridgeFcogEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogEthType.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogIpTosOrDscp_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibBridgeFcogIpTosOrDscp based on TruthValue"""


_RlPolicySimpleGalMibBridgeFcogIpTosOrDscp_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogIpTosOrDscp = _RlPolicySimpleGalMibBridgeFcogIpTosOrDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 7),
    _RlPolicySimpleGalMibBridgeFcogIpTosOrDscp_Type()
)
rlPolicySimpleGalMibBridgeFcogIpTosOrDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogIpTosOrDscp.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogIpProtocol_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibBridgeFcogIpProtocol based on TruthValue"""


_RlPolicySimpleGalMibBridgeFcogIpProtocol_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogIpProtocol = _RlPolicySimpleGalMibBridgeFcogIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 8),
    _RlPolicySimpleGalMibBridgeFcogIpProtocol_Type()
)
rlPolicySimpleGalMibBridgeFcogIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogIpProtocol.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogIpSrcIpMask_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeFcogIpSrcIpMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RlPolicySimpleGalMibBridgeFcogIpSrcIpMask_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeFcogIpSrcIpMask_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogIpSrcIpMask = _RlPolicySimpleGalMibBridgeFcogIpSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 9),
    _RlPolicySimpleGalMibBridgeFcogIpSrcIpMask_Type()
)
rlPolicySimpleGalMibBridgeFcogIpSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogIpSrcIpMask.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogIpDstIpMask_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeFcogIpDstIpMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RlPolicySimpleGalMibBridgeFcogIpDstIpMask_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeFcogIpDstIpMask_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogIpDstIpMask = _RlPolicySimpleGalMibBridgeFcogIpDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 10),
    _RlPolicySimpleGalMibBridgeFcogIpDstIpMask_Type()
)
rlPolicySimpleGalMibBridgeFcogIpDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogIpDstIpMask.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogIpSrcPort_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibBridgeFcogIpSrcPort based on TruthValue"""


_RlPolicySimpleGalMibBridgeFcogIpSrcPort_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogIpSrcPort = _RlPolicySimpleGalMibBridgeFcogIpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 11),
    _RlPolicySimpleGalMibBridgeFcogIpSrcPort_Type()
)
rlPolicySimpleGalMibBridgeFcogIpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogIpSrcPort.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeFcogIpDstPort_Type(TruthValue):
    """Custom type rlPolicySimpleGalMibBridgeFcogIpDstPort based on TruthValue"""


_RlPolicySimpleGalMibBridgeFcogIpDstPort_Object = MibTableColumn
rlPolicySimpleGalMibBridgeFcogIpDstPort = _RlPolicySimpleGalMibBridgeFcogIpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 10, 1, 12),
    _RlPolicySimpleGalMibBridgeFcogIpDstPort_Type()
)
rlPolicySimpleGalMibBridgeFcogIpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeFcogIpDstPort.setStatus("mandatory")
_RlPolicySimpleGalMibBridgeRulesTable_Object = MibTable
rlPolicySimpleGalMibBridgeRulesTable = _RlPolicySimpleGalMibBridgeRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11)
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesTable.setStatus("mandatory")
_RlPolicySimpleGalMibBridgeRulesEntry_Object = MibTableRow
rlPolicySimpleGalMibBridgeRulesEntry = _RlPolicySimpleGalMibBridgeRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1)
)
rlPolicySimpleGalMibBridgeRulesEntry.setIndexNames(
    (0, "GALILEO-MIB", "rlPolicySimpleGalMibBridgeRulesIndex"),
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesEntry.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesIndex_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeRulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicySimpleGalMibBridgeRulesIndex_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeRulesIndex_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesIndex = _RlPolicySimpleGalMibBridgeRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 1),
    _RlPolicySimpleGalMibBridgeRulesIndex_Type()
)
rlPolicySimpleGalMibBridgeRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesIndex.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesDescription_Type(DisplayString):
    """Custom type rlPolicySimpleGalMibBridgeRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_RlPolicySimpleGalMibBridgeRulesDescription_Type.__name__ = "DisplayString"
_RlPolicySimpleGalMibBridgeRulesDescription_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesDescription = _RlPolicySimpleGalMibBridgeRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 2),
    _RlPolicySimpleGalMibBridgeRulesDescription_Type()
)
rlPolicySimpleGalMibBridgeRulesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesDescription.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesDstMac_Type(OctetString):
    """Custom type rlPolicySimpleGalMibBridgeRulesDstMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicySimpleGalMibBridgeRulesDstMac_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibBridgeRulesDstMac_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesDstMac = _RlPolicySimpleGalMibBridgeRulesDstMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 3),
    _RlPolicySimpleGalMibBridgeRulesDstMac_Type()
)
rlPolicySimpleGalMibBridgeRulesDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesDstMac.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesSrcMac_Type(OctetString):
    """Custom type rlPolicySimpleGalMibBridgeRulesSrcMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RlPolicySimpleGalMibBridgeRulesSrcMac_Type.__name__ = "OctetString"
_RlPolicySimpleGalMibBridgeRulesSrcMac_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesSrcMac = _RlPolicySimpleGalMibBridgeRulesSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 4),
    _RlPolicySimpleGalMibBridgeRulesSrcMac_Type()
)
rlPolicySimpleGalMibBridgeRulesSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesSrcMac.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesVid_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeRulesVid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlPolicySimpleGalMibBridgeRulesVid_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeRulesVid_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesVid = _RlPolicySimpleGalMibBridgeRulesVid_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 5),
    _RlPolicySimpleGalMibBridgeRulesVid_Type()
)
rlPolicySimpleGalMibBridgeRulesVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesVid.setStatus("mandatory")
_RlPolicySimpleGalMibBridgeRulesInIfIndexList_Type = PortList
_RlPolicySimpleGalMibBridgeRulesInIfIndexList_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesInIfIndexList = _RlPolicySimpleGalMibBridgeRulesInIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 6),
    _RlPolicySimpleGalMibBridgeRulesInIfIndexList_Type()
)
rlPolicySimpleGalMibBridgeRulesInIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesInIfIndexList.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesEthType_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeRulesEthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicySimpleGalMibBridgeRulesEthType_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeRulesEthType_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesEthType = _RlPolicySimpleGalMibBridgeRulesEthType_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 7),
    _RlPolicySimpleGalMibBridgeRulesEthType_Type()
)
rlPolicySimpleGalMibBridgeRulesEthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesEthType.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesIpTosOrDscp_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeRulesIpTosOrDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlPolicySimpleGalMibBridgeRulesIpTosOrDscp_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeRulesIpTosOrDscp_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesIpTosOrDscp = _RlPolicySimpleGalMibBridgeRulesIpTosOrDscp_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 8),
    _RlPolicySimpleGalMibBridgeRulesIpTosOrDscp_Type()
)
rlPolicySimpleGalMibBridgeRulesIpTosOrDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesIpTosOrDscp.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesIpProtocol_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeRulesIpProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlPolicySimpleGalMibBridgeRulesIpProtocol_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeRulesIpProtocol_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesIpProtocol = _RlPolicySimpleGalMibBridgeRulesIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 9),
    _RlPolicySimpleGalMibBridgeRulesIpProtocol_Type()
)
rlPolicySimpleGalMibBridgeRulesIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesIpProtocol.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesIpSrcIp_Type(IpAddress):
    """Custom type rlPolicySimpleGalMibBridgeRulesIpSrcIp based on IpAddress"""
    defaultHexValue = "00000000"


_RlPolicySimpleGalMibBridgeRulesIpSrcIp_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesIpSrcIp = _RlPolicySimpleGalMibBridgeRulesIpSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 10),
    _RlPolicySimpleGalMibBridgeRulesIpSrcIp_Type()
)
rlPolicySimpleGalMibBridgeRulesIpSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesIpSrcIp.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesIpDstIp_Type(IpAddress):
    """Custom type rlPolicySimpleGalMibBridgeRulesIpDstIp based on IpAddress"""
    defaultHexValue = "00000000"


_RlPolicySimpleGalMibBridgeRulesIpDstIp_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesIpDstIp = _RlPolicySimpleGalMibBridgeRulesIpDstIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 11),
    _RlPolicySimpleGalMibBridgeRulesIpDstIp_Type()
)
rlPolicySimpleGalMibBridgeRulesIpDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesIpDstIp.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesIpSrcPort_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeRulesIpSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicySimpleGalMibBridgeRulesIpSrcPort_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeRulesIpSrcPort_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesIpSrcPort = _RlPolicySimpleGalMibBridgeRulesIpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 12),
    _RlPolicySimpleGalMibBridgeRulesIpSrcPort_Type()
)
rlPolicySimpleGalMibBridgeRulesIpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesIpSrcPort.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesIpDstPort_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeRulesIpDstPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlPolicySimpleGalMibBridgeRulesIpDstPort_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeRulesIpDstPort_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesIpDstPort = _RlPolicySimpleGalMibBridgeRulesIpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 13),
    _RlPolicySimpleGalMibBridgeRulesIpDstPort_Type()
)
rlPolicySimpleGalMibBridgeRulesIpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesIpDstPort.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesCondition_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeRulesCondition based on Integer32"""
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
        *(("bigger", 3),
          ("equal", 1),
          ("notEqual", 2),
          ("smaller", 4))
    )


_RlPolicySimpleGalMibBridgeRulesCondition_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeRulesCondition_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesCondition = _RlPolicySimpleGalMibBridgeRulesCondition_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 14),
    _RlPolicySimpleGalMibBridgeRulesCondition_Type()
)
rlPolicySimpleGalMibBridgeRulesCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesCondition.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesAction_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeRulesAction based on Integer32"""
    defaultValue = 4

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
        *(("block", 1),
          ("blockAndTrap", 2),
          ("permit", 4),
          ("permitAndTrap", 3))
    )


_RlPolicySimpleGalMibBridgeRulesAction_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeRulesAction_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesAction = _RlPolicySimpleGalMibBridgeRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 15),
    _RlPolicySimpleGalMibBridgeRulesAction_Type()
)
rlPolicySimpleGalMibBridgeRulesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesAction.setStatus("mandatory")


class _RlPolicySimpleGalMibBridgeRulesProfilePointer_Type(Integer32):
    """Custom type rlPolicySimpleGalMibBridgeRulesProfilePointer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPolicySimpleGalMibBridgeRulesProfilePointer_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibBridgeRulesProfilePointer_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesProfilePointer = _RlPolicySimpleGalMibBridgeRulesProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 16),
    _RlPolicySimpleGalMibBridgeRulesProfilePointer_Type()
)
rlPolicySimpleGalMibBridgeRulesProfilePointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesProfilePointer.setStatus("mandatory")
_RlPolicySimpleGalMibBridgeRulesOutIfIndexList_Type = PortList
_RlPolicySimpleGalMibBridgeRulesOutIfIndexList_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesOutIfIndexList = _RlPolicySimpleGalMibBridgeRulesOutIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 17),
    _RlPolicySimpleGalMibBridgeRulesOutIfIndexList_Type()
)
rlPolicySimpleGalMibBridgeRulesOutIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesOutIfIndexList.setStatus("mandatory")
_RlPolicySimpleGalMibBridgeRulesStatus_Type = RowStatus
_RlPolicySimpleGalMibBridgeRulesStatus_Object = MibTableColumn
rlPolicySimpleGalMibBridgeRulesStatus = _RlPolicySimpleGalMibBridgeRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 11, 1, 18),
    _RlPolicySimpleGalMibBridgeRulesStatus_Type()
)
rlPolicySimpleGalMibBridgeRulesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibBridgeRulesStatus.setStatus("mandatory")
_RlPolicySimpleGalMibPortTable_Object = MibTable
rlPolicySimpleGalMibPortTable = _RlPolicySimpleGalMibPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 12)
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibPortTable.setStatus("mandatory")
_RlPolicySimpleGalMibPortEntry_Object = MibTableRow
rlPolicySimpleGalMibPortEntry = _RlPolicySimpleGalMibPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 12, 1)
)
rlPolicySimpleGalMibPortEntry.setIndexNames(
    (0, "GALILEO-MIB", "rlPolicySimpleGalMibPortIfIndex"),
)
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibPortEntry.setStatus("mandatory")


class _RlPolicySimpleGalMibPortIfIndex_Type(Integer32):
    """Custom type rlPolicySimpleGalMibPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlPolicySimpleGalMibPortIfIndex_Type.__name__ = "Integer32"
_RlPolicySimpleGalMibPortIfIndex_Object = MibTableColumn
rlPolicySimpleGalMibPortIfIndex = _RlPolicySimpleGalMibPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 12, 1, 1),
    _RlPolicySimpleGalMibPortIfIndex_Type()
)
rlPolicySimpleGalMibPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibPortIfIndex.setStatus("mandatory")


class _RlPolicySimpleGalMibPortType_Type(RlPolicySimpleGalMibPortType):
    """Custom type rlPolicySimpleGalMibPortType based on RlPolicySimpleGalMibPortType"""


_RlPolicySimpleGalMibPortType_Object = MibTableColumn
rlPolicySimpleGalMibPortType = _RlPolicySimpleGalMibPortType_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 9, 12, 1, 2),
    _RlPolicySimpleGalMibPortType_Type()
)
rlPolicySimpleGalMibPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPolicySimpleGalMibPortType.setStatus("mandatory")


class _RlGalPolicyMode_Type(Integer32):
    """Custom type rlGalPolicyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridged", 1),
          ("routedIp", 2))
    )


_RlGalPolicyMode_Type.__name__ = "Integer32"
_RlGalPolicyMode_Object = MibScalar
rlGalPolicyMode = _RlGalPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 56, 10),
    _RlGalPolicyMode_Type()
)
rlGalPolicyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGalPolicyMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GALILEO-MIB",
    **{"RlPolicyGalileoDebugGroupType": RlPolicyGalileoDebugGroupType,
       "RlPolicySimpleGalMibProfileType": RlPolicySimpleGalMibProfileType,
       "RlPolicySimpleGalMibPortType": RlPolicySimpleGalMibPortType,
       "rlGalMibVersion": rlGalMibVersion,
       "rlGalMode": rlGalMode,
       "rlGalModeAfterReset": rlGalModeAfterReset,
       "rlPolicyGalileoDebugTuning": rlPolicyGalileoDebugTuning,
       "rlPolicyGalileoTuningOverProvisioning": rlPolicyGalileoTuningOverProvisioning,
       "rlPolicyGalileoTuningExtremConditionBurstSize": rlPolicyGalileoTuningExtremConditionBurstSize,
       "rlPolicyGalileoTuningOverrideOutOfProfileDropPrecedence": rlPolicyGalileoTuningOverrideOutOfProfileDropPrecedence,
       "rlCosFftAgingTimeout": rlCosFftAgingTimeout,
       "rlCosFftPollingInterval": rlCosFftPollingInterval,
       "rlPolicyGalileoDebug": rlPolicyGalileoDebug,
       "rlPolicyGalileoDebugFcogTable": rlPolicyGalileoDebugFcogTable,
       "rlPolicyGalileoDebugFcogEntry": rlPolicyGalileoDebugFcogEntry,
       "rlPolicyGalileoDebugFcogType": rlPolicyGalileoDebugFcogType,
       "rlPolicyGalileoDebugL2SrcAddr": rlPolicyGalileoDebugL2SrcAddr,
       "rlPolicyGalileoDebugL2DstAddr": rlPolicyGalileoDebugL2DstAddr,
       "rlPolicyGalileoDebugVlanId": rlPolicyGalileoDebugVlanId,
       "rlPolicyGalileoDebugInport": rlPolicyGalileoDebugInport,
       "rlPolicyGalileoDebugIpxDstNet": rlPolicyGalileoDebugIpxDstNet,
       "rlPolicyGalileoDebugIpxDstNode": rlPolicyGalileoDebugIpxDstNode,
       "rlPolicyGalileoDebugIpSrcAddr": rlPolicyGalileoDebugIpSrcAddr,
       "rlPolicyGalileoDebugIpDstAddr": rlPolicyGalileoDebugIpDstAddr,
       "rlPolicyGalileoDebugIpProtocol": rlPolicyGalileoDebugIpProtocol,
       "rlPolicyGalileoDebugIpSrcPort": rlPolicyGalileoDebugIpSrcPort,
       "rlPolicyGalileoDebugIpDstPort": rlPolicyGalileoDebugIpDstPort,
       "rlPolicyGalileoDebugStatus": rlPolicyGalileoDebugStatus,
       "rlPolicyGalileoDebugFlowTable": rlPolicyGalileoDebugFlowTable,
       "rlPolicyGalileoDebugFlowTableEntry": rlPolicyGalileoDebugFlowTableEntry,
       "rlPolicyGalileoDebugFlowType": rlPolicyGalileoDebugFlowType,
       "rlPolicyGalileoDebugFlowRxIfIndex": rlPolicyGalileoDebugFlowRxIfIndex,
       "rlPolicyGalileoDebugFlowL2SrcAddr": rlPolicyGalileoDebugFlowL2SrcAddr,
       "rlPolicyGalileoDebugFlowL2DstAddr": rlPolicyGalileoDebugFlowL2DstAddr,
       "rlPolicyGalileoDebugFlowVlanId": rlPolicyGalileoDebugFlowVlanId,
       "rlPolicyGalileoDebugFlowIpxDstNet": rlPolicyGalileoDebugFlowIpxDstNet,
       "rlPolicyGalileoDebugFlowIpxDstNode": rlPolicyGalileoDebugFlowIpxDstNode,
       "rlPolicyGalileoDebugFlowIpSrcAddr": rlPolicyGalileoDebugFlowIpSrcAddr,
       "rlPolicyGalileoDebugFlowIpDstAddr": rlPolicyGalileoDebugFlowIpDstAddr,
       "rlPolicyGalileoDebugFlowIpProtocol": rlPolicyGalileoDebugFlowIpProtocol,
       "rlPolicyGalileoDebugFlowIpSrcPort": rlPolicyGalileoDebugFlowIpSrcPort,
       "rlPolicyGalileoDebugFlowIpDstPort": rlPolicyGalileoDebugFlowIpDstPort,
       "rlPolicyGalileoDebugFlowRetValid": rlPolicyGalileoDebugFlowRetValid,
       "rlPolicyGalileoDebugFlowRetStatic": rlPolicyGalileoDebugFlowRetStatic,
       "rlPolicyGalileoDebugFlowRetAging": rlPolicyGalileoDebugFlowRetAging,
       "rlPolicyGalileoDebugFlowRetCmd": rlPolicyGalileoDebugFlowRetCmd,
       "rlPolicyGalileoDebugFlowRetPrio": rlPolicyGalileoDebugFlowRetPrio,
       "rlPolicyGalileoDebugFlowRetInProfileDis": rlPolicyGalileoDebugFlowRetInProfileDis,
       "rlPolicyGalileoDebugFlowRetVpt": rlPolicyGalileoDebugFlowRetVpt,
       "rlPolicyGalileoDebugFlowRetChangeTos": rlPolicyGalileoDebugFlowRetChangeTos,
       "rlPolicyGalileoDebugFlowRetNewTos": rlPolicyGalileoDebugFlowRetNewTos,
       "rlPolicyGalileoDebugFlowRetVlanId": rlPolicyGalileoDebugFlowRetVlanId,
       "rlPolicyGalileoDebugFlowRetInIfIndex": rlPolicyGalileoDebugFlowRetInIfIndex,
       "rlPolicyGalileoDebugFlowRetEnableMeter": rlPolicyGalileoDebugFlowRetEnableMeter,
       "rlPolicyGalileoDebugFlowRetOutProfileDis": rlPolicyGalileoDebugFlowRetOutProfileDis,
       "rlPolicyGalileoFcuFwdCpuCounter": rlPolicyGalileoFcuFwdCpuCounter,
       "rlPolicySimpleGalMib": rlPolicySimpleGalMib,
       "rlPolicySimpleGalMibVersion": rlPolicySimpleGalMibVersion,
       "rlPolicySimpleGalMibPortTypeSupport": rlPolicySimpleGalMibPortTypeSupport,
       "rlPolicySimpleGalMibRecalculateRules": rlPolicySimpleGalMibRecalculateRules,
       "rlPolicySimpleGalMibPolicyEnable": rlPolicySimpleGalMibPolicyEnable,
       "rlPolicySimpleGalMibProfileTable": rlPolicySimpleGalMibProfileTable,
       "rlPolicySimpleGalMibProfileEntry": rlPolicySimpleGalMibProfileEntry,
       "rlPolicySimpleGalMibIndex": rlPolicySimpleGalMibIndex,
       "rlPolicySimpleGalMibDescription": rlPolicySimpleGalMibDescription,
       "rlPolicySimpleGalMibProfileType": rlPolicySimpleGalMibProfileType,
       "rlPolicySimpleGalMibRate": rlPolicySimpleGalMibRate,
       "rlPolicySimpleGalMibBurstSize": rlPolicySimpleGalMibBurstSize,
       "rlPolicySimpleGalMibMaxSession": rlPolicySimpleGalMibMaxSession,
       "rlPolicySimpleGalMibNewVpt": rlPolicySimpleGalMibNewVpt,
       "rlPolicySimpleGalMibChangeTosOrDscp": rlPolicySimpleGalMibChangeTosOrDscp,
       "rlPolicySimpleGalMibNewTosOrDscp": rlPolicySimpleGalMibNewTosOrDscp,
       "rlPolicySimpleGalMibStatus": rlPolicySimpleGalMibStatus,
       "rlPolicySimpleGalMibIpFcogTable": rlPolicySimpleGalMibIpFcogTable,
       "rlPolicySimpleGalMibIpFcogEntry": rlPolicySimpleGalMibIpFcogEntry,
       "rlPolicySimpleGalMibIpFcogPortType": rlPolicySimpleGalMibIpFcogPortType,
       "rlPolicySimpleGalMibIpFcogTosOrDscp": rlPolicySimpleGalMibIpFcogTosOrDscp,
       "rlPolicySimpleGalMibIpFcogProtocol": rlPolicySimpleGalMibIpFcogProtocol,
       "rlPolicySimpleGalMibIpFcogSrcIpMask": rlPolicySimpleGalMibIpFcogSrcIpMask,
       "rlPolicySimpleGalMibIpFcogDstIpMask": rlPolicySimpleGalMibIpFcogDstIpMask,
       "rlPolicySimpleGalMibIpFcogSrcPort": rlPolicySimpleGalMibIpFcogSrcPort,
       "rlPolicySimpleGalMibIpFcogDstPort": rlPolicySimpleGalMibIpFcogDstPort,
       "rlPolicySimpleGalMibIpFcogInIfIndex": rlPolicySimpleGalMibIpFcogInIfIndex,
       "rlPolicySimpleGalMibIpRulesTable": rlPolicySimpleGalMibIpRulesTable,
       "rlPolicySimpleGalMibIpRulesEntry": rlPolicySimpleGalMibIpRulesEntry,
       "rlPolicySimpleGalMibIpRulesPortType": rlPolicySimpleGalMibIpRulesPortType,
       "rlPolicySimpleGalMibIpRulesIndex": rlPolicySimpleGalMibIpRulesIndex,
       "rlPolicySimpleGalMibIpRulesDescription": rlPolicySimpleGalMibIpRulesDescription,
       "rlPolicySimpleGalMibIpRulesTosOrDscp": rlPolicySimpleGalMibIpRulesTosOrDscp,
       "rlPolicySimpleGalMibIpRulesProtocol": rlPolicySimpleGalMibIpRulesProtocol,
       "rlPolicySimpleGalMibIpRulesSrcIp": rlPolicySimpleGalMibIpRulesSrcIp,
       "rlPolicySimpleGalMibIpRulesSrcIpMask": rlPolicySimpleGalMibIpRulesSrcIpMask,
       "rlPolicySimpleGalMibIpRulesDstIp": rlPolicySimpleGalMibIpRulesDstIp,
       "rlPolicySimpleGalMibIpRulesDstIpMask": rlPolicySimpleGalMibIpRulesDstIpMask,
       "rlPolicySimpleGalMibIpRulesSrcPort": rlPolicySimpleGalMibIpRulesSrcPort,
       "rlPolicySimpleGalMibIpRulesDstPort": rlPolicySimpleGalMibIpRulesDstPort,
       "rlPolicySimpleGalMibIpRulesInIfIndexList": rlPolicySimpleGalMibIpRulesInIfIndexList,
       "rlPolicySimpleGalMibIpRulesCondition": rlPolicySimpleGalMibIpRulesCondition,
       "rlPolicySimpleGalMibIpRulesAction": rlPolicySimpleGalMibIpRulesAction,
       "rlPolicySimpleGalMibIpRulesProfilePointer": rlPolicySimpleGalMibIpRulesProfilePointer,
       "rlPolicySimpleGalMibIpRulesOutIfIndexList": rlPolicySimpleGalMibIpRulesOutIfIndexList,
       "rlPolicySimpleGalMibIpRulesBitsUsed": rlPolicySimpleGalMibIpRulesBitsUsed,
       "rlPolicySimpleGalMibIpRulesErrorDescrip": rlPolicySimpleGalMibIpRulesErrorDescrip,
       "rlPolicySimpleGalMibIpRulesStatus": rlPolicySimpleGalMibIpRulesStatus,
       "rlPolicySimpleGalMibIpxFcogTable": rlPolicySimpleGalMibIpxFcogTable,
       "rlPolicySimpleGalMibIpxFcogEntry": rlPolicySimpleGalMibIpxFcogEntry,
       "rlPolicySimpleGalMibIpxFcogIndex": rlPolicySimpleGalMibIpxFcogIndex,
       "rlPolicySimpleGalMibIpxFcogDstNet": rlPolicySimpleGalMibIpxFcogDstNet,
       "rlPolicySimpleGalMibIpxFcogDstNode": rlPolicySimpleGalMibIpxFcogDstNode,
       "rlPolicySimpleGalMibIpxFcogDstSocket": rlPolicySimpleGalMibIpxFcogDstSocket,
       "rlPolicySimpleGalMibIpxFcogSrcNet": rlPolicySimpleGalMibIpxFcogSrcNet,
       "rlPolicySimpleGalMibIpxFcogSrcNode": rlPolicySimpleGalMibIpxFcogSrcNode,
       "rlPolicySimpleGalMibIpxFcogSrcSocket": rlPolicySimpleGalMibIpxFcogSrcSocket,
       "rlPolicySimpleGalMibIpxFcogInIfIndex": rlPolicySimpleGalMibIpxFcogInIfIndex,
       "rlPolicySimpleGalMibIpxRulesTable": rlPolicySimpleGalMibIpxRulesTable,
       "rlPolicySimpleGalMibIpxRulesEntry": rlPolicySimpleGalMibIpxRulesEntry,
       "rlPolicySimpleGalMibIpxRulesIndex": rlPolicySimpleGalMibIpxRulesIndex,
       "rlPolicySimpleGalMibIpxRulesDescription": rlPolicySimpleGalMibIpxRulesDescription,
       "rlPolicySimpleGalMibIpxRulesDstNet": rlPolicySimpleGalMibIpxRulesDstNet,
       "rlPolicySimpleGalMibIpxRulesDstNode": rlPolicySimpleGalMibIpxRulesDstNode,
       "rlPolicySimpleGalMibIpxRulesDstSocket": rlPolicySimpleGalMibIpxRulesDstSocket,
       "rlPolicySimpleGalMibIpxRulesSrcNet": rlPolicySimpleGalMibIpxRulesSrcNet,
       "rlPolicySimpleGalMibIpxRulesSrcNode": rlPolicySimpleGalMibIpxRulesSrcNode,
       "rlPolicySimpleGalMibIpxRulesSrcSocket": rlPolicySimpleGalMibIpxRulesSrcSocket,
       "rlPolicySimpleGalMibIpxRulesInIfIndexList": rlPolicySimpleGalMibIpxRulesInIfIndexList,
       "rlPolicySimpleGalMibIpxRulesCondition": rlPolicySimpleGalMibIpxRulesCondition,
       "rlPolicySimpleGalMibIpxRulesAction": rlPolicySimpleGalMibIpxRulesAction,
       "rlPolicySimpleGalMibIpxRulesProfilePointer": rlPolicySimpleGalMibIpxRulesProfilePointer,
       "rlPolicySimpleGalMibIpxRulesOutIfIndexList": rlPolicySimpleGalMibIpxRulesOutIfIndexList,
       "rlPolicySimpleGalMibIpxRulesStatus": rlPolicySimpleGalMibIpxRulesStatus,
       "rlPolicySimpleGalMibBridgeFcogTable": rlPolicySimpleGalMibBridgeFcogTable,
       "rlPolicySimpleGalMibBridgeFcogEntry": rlPolicySimpleGalMibBridgeFcogEntry,
       "rlPolicySimpleGalMibBridgeFcogIndex": rlPolicySimpleGalMibBridgeFcogIndex,
       "rlPolicySimpleGalMibBridgeFcogDstMac": rlPolicySimpleGalMibBridgeFcogDstMac,
       "rlPolicySimpleGalMibBridgeFcogSrcMac": rlPolicySimpleGalMibBridgeFcogSrcMac,
       "rlPolicySimpleGalMibBridgeFcogVid": rlPolicySimpleGalMibBridgeFcogVid,
       "rlPolicySimpleGalMibBridgeFcogInIfIndex": rlPolicySimpleGalMibBridgeFcogInIfIndex,
       "rlPolicySimpleGalMibBridgeFcogEthType": rlPolicySimpleGalMibBridgeFcogEthType,
       "rlPolicySimpleGalMibBridgeFcogIpTosOrDscp": rlPolicySimpleGalMibBridgeFcogIpTosOrDscp,
       "rlPolicySimpleGalMibBridgeFcogIpProtocol": rlPolicySimpleGalMibBridgeFcogIpProtocol,
       "rlPolicySimpleGalMibBridgeFcogIpSrcIpMask": rlPolicySimpleGalMibBridgeFcogIpSrcIpMask,
       "rlPolicySimpleGalMibBridgeFcogIpDstIpMask": rlPolicySimpleGalMibBridgeFcogIpDstIpMask,
       "rlPolicySimpleGalMibBridgeFcogIpSrcPort": rlPolicySimpleGalMibBridgeFcogIpSrcPort,
       "rlPolicySimpleGalMibBridgeFcogIpDstPort": rlPolicySimpleGalMibBridgeFcogIpDstPort,
       "rlPolicySimpleGalMibBridgeRulesTable": rlPolicySimpleGalMibBridgeRulesTable,
       "rlPolicySimpleGalMibBridgeRulesEntry": rlPolicySimpleGalMibBridgeRulesEntry,
       "rlPolicySimpleGalMibBridgeRulesIndex": rlPolicySimpleGalMibBridgeRulesIndex,
       "rlPolicySimpleGalMibBridgeRulesDescription": rlPolicySimpleGalMibBridgeRulesDescription,
       "rlPolicySimpleGalMibBridgeRulesDstMac": rlPolicySimpleGalMibBridgeRulesDstMac,
       "rlPolicySimpleGalMibBridgeRulesSrcMac": rlPolicySimpleGalMibBridgeRulesSrcMac,
       "rlPolicySimpleGalMibBridgeRulesVid": rlPolicySimpleGalMibBridgeRulesVid,
       "rlPolicySimpleGalMibBridgeRulesInIfIndexList": rlPolicySimpleGalMibBridgeRulesInIfIndexList,
       "rlPolicySimpleGalMibBridgeRulesEthType": rlPolicySimpleGalMibBridgeRulesEthType,
       "rlPolicySimpleGalMibBridgeRulesIpTosOrDscp": rlPolicySimpleGalMibBridgeRulesIpTosOrDscp,
       "rlPolicySimpleGalMibBridgeRulesIpProtocol": rlPolicySimpleGalMibBridgeRulesIpProtocol,
       "rlPolicySimpleGalMibBridgeRulesIpSrcIp": rlPolicySimpleGalMibBridgeRulesIpSrcIp,
       "rlPolicySimpleGalMibBridgeRulesIpDstIp": rlPolicySimpleGalMibBridgeRulesIpDstIp,
       "rlPolicySimpleGalMibBridgeRulesIpSrcPort": rlPolicySimpleGalMibBridgeRulesIpSrcPort,
       "rlPolicySimpleGalMibBridgeRulesIpDstPort": rlPolicySimpleGalMibBridgeRulesIpDstPort,
       "rlPolicySimpleGalMibBridgeRulesCondition": rlPolicySimpleGalMibBridgeRulesCondition,
       "rlPolicySimpleGalMibBridgeRulesAction": rlPolicySimpleGalMibBridgeRulesAction,
       "rlPolicySimpleGalMibBridgeRulesProfilePointer": rlPolicySimpleGalMibBridgeRulesProfilePointer,
       "rlPolicySimpleGalMibBridgeRulesOutIfIndexList": rlPolicySimpleGalMibBridgeRulesOutIfIndexList,
       "rlPolicySimpleGalMibBridgeRulesStatus": rlPolicySimpleGalMibBridgeRulesStatus,
       "rlPolicySimpleGalMibPortTable": rlPolicySimpleGalMibPortTable,
       "rlPolicySimpleGalMibPortEntry": rlPolicySimpleGalMibPortEntry,
       "rlPolicySimpleGalMibPortIfIndex": rlPolicySimpleGalMibPortIfIndex,
       "rlPolicySimpleGalMibPortType": rlPolicySimpleGalMibPortType,
       "rlGalPolicyMode": rlGalPolicyMode}
)
