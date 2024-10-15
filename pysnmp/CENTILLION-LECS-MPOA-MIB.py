# SNMP MIB module (CENTILLION-LECS-MPOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-LECS-MPOA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:08 2024
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

(atmLane,) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "atmLane")

(lecsConfIndex,) = mibBuilder.importSymbols(
    "LAN-EMULATION-ELAN-MIB",
    "lecsConfIndex")

(AtmConfigAddr,
 InternetworkAddrType,
 MpcIndex,
 MpsIndex) = mibBuilder.importSymbols(
    "MPOA-MIB",
    "AtmConfigAddr",
    "InternetworkAddrType",
    "MpcIndex",
    "MpsIndex")

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

(RowStatus,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "RowStatus",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnLecsMpoaGroup_ObjectIdentity = ObjectIdentity
cnLecsMpoaGroup = _CnLecsMpoaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6)
)
_CnLecsMpoaMpcTable_Object = MibTable
cnLecsMpoaMpcTable = _CnLecsMpoaMpcTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    cnLecsMpoaMpcTable.setStatus("mandatory")
_CnLecsMpoaMpcEntry_Object = MibTableRow
cnLecsMpoaMpcEntry = _CnLecsMpoaMpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1)
)
cnLecsMpoaMpcEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
    (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpcIndex"),
)
if mibBuilder.loadTexts:
    cnLecsMpoaMpcEntry.setStatus("mandatory")
_CnLecsMpoaMpcIndex_Type = MpcIndex
_CnLecsMpoaMpcIndex_Object = MibTableColumn
cnLecsMpoaMpcIndex = _CnLecsMpoaMpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 1),
    _CnLecsMpoaMpcIndex_Type()
)
cnLecsMpoaMpcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcIndex.setStatus("mandatory")
_CnLecsMpoaMpcRowStatus_Type = RowStatus
_CnLecsMpoaMpcRowStatus_Object = MibTableColumn
cnLecsMpoaMpcRowStatus = _CnLecsMpoaMpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 2),
    _CnLecsMpoaMpcRowStatus_Type()
)
cnLecsMpoaMpcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcRowStatus.setStatus("mandatory")
_CnLecsMpoaMpcCtrlAtmAddr_Type = AtmConfigAddr
_CnLecsMpoaMpcCtrlAtmAddr_Object = MibTableColumn
cnLecsMpoaMpcCtrlAtmAddr = _CnLecsMpoaMpcCtrlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 3),
    _CnLecsMpoaMpcCtrlAtmAddr_Type()
)
cnLecsMpoaMpcCtrlAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcCtrlAtmAddr.setStatus("mandatory")


class _CnLecsMpoaMpcSCSetupFrameCount_Type(Integer32):
    """Custom type cnLecsMpoaMpcSCSetupFrameCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CnLecsMpoaMpcSCSetupFrameCount_Type.__name__ = "Integer32"
_CnLecsMpoaMpcSCSetupFrameCount_Object = MibTableColumn
cnLecsMpoaMpcSCSetupFrameCount = _CnLecsMpoaMpcSCSetupFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 4),
    _CnLecsMpoaMpcSCSetupFrameCount_Type()
)
cnLecsMpoaMpcSCSetupFrameCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcSCSetupFrameCount.setStatus("mandatory")


class _CnLecsMpoaMpcSCSetupFrameTime_Type(Integer32):
    """Custom type cnLecsMpoaMpcSCSetupFrameTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CnLecsMpoaMpcSCSetupFrameTime_Type.__name__ = "Integer32"
_CnLecsMpoaMpcSCSetupFrameTime_Object = MibTableColumn
cnLecsMpoaMpcSCSetupFrameTime = _CnLecsMpoaMpcSCSetupFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 5),
    _CnLecsMpoaMpcSCSetupFrameTime_Type()
)
cnLecsMpoaMpcSCSetupFrameTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcSCSetupFrameTime.setStatus("mandatory")


class _CnLecsMpoaMpcInitialRetryTime_Type(Integer32):
    """Custom type cnLecsMpoaMpcInitialRetryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CnLecsMpoaMpcInitialRetryTime_Type.__name__ = "Integer32"
_CnLecsMpoaMpcInitialRetryTime_Object = MibTableColumn
cnLecsMpoaMpcInitialRetryTime = _CnLecsMpoaMpcInitialRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 6),
    _CnLecsMpoaMpcInitialRetryTime_Type()
)
cnLecsMpoaMpcInitialRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcInitialRetryTime.setStatus("mandatory")


class _CnLecsMpoaMpcRetryTimeMaximum_Type(Integer32):
    """Custom type cnLecsMpoaMpcRetryTimeMaximum based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CnLecsMpoaMpcRetryTimeMaximum_Type.__name__ = "Integer32"
_CnLecsMpoaMpcRetryTimeMaximum_Object = MibTableColumn
cnLecsMpoaMpcRetryTimeMaximum = _CnLecsMpoaMpcRetryTimeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 7),
    _CnLecsMpoaMpcRetryTimeMaximum_Type()
)
cnLecsMpoaMpcRetryTimeMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcRetryTimeMaximum.setStatus("mandatory")


class _CnLecsMpoaMpcHoldDownTime_Type(Integer32):
    """Custom type cnLecsMpoaMpcHoldDownTime based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1200),
    )


_CnLecsMpoaMpcHoldDownTime_Type.__name__ = "Integer32"
_CnLecsMpoaMpcHoldDownTime_Object = MibTableColumn
cnLecsMpoaMpcHoldDownTime = _CnLecsMpoaMpcHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 8),
    _CnLecsMpoaMpcHoldDownTime_Type()
)
cnLecsMpoaMpcHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcHoldDownTime.setStatus("mandatory")


class _CnLecsMpoaMpcDefaultTLV_Type(TruthValue):
    """Custom type cnLecsMpoaMpcDefaultTLV based on TruthValue"""


_CnLecsMpoaMpcDefaultTLV_Object = MibTableColumn
cnLecsMpoaMpcDefaultTLV = _CnLecsMpoaMpcDefaultTLV_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 1, 1, 9),
    _CnLecsMpoaMpcDefaultTLV_Type()
)
cnLecsMpoaMpcDefaultTLV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcDefaultTLV.setStatus("mandatory")
_CnLecsMpoaMpsTable_Object = MibTable
cnLecsMpoaMpsTable = _CnLecsMpoaMpsTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2)
)
if mibBuilder.loadTexts:
    cnLecsMpoaMpsTable.setStatus("mandatory")
_CnLecsMpoaMpsEntry_Object = MibTableRow
cnLecsMpoaMpsEntry = _CnLecsMpoaMpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1)
)
cnLecsMpoaMpsEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
    (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpsIndex"),
)
if mibBuilder.loadTexts:
    cnLecsMpoaMpsEntry.setStatus("mandatory")
_CnLecsMpoaMpsIndex_Type = MpsIndex
_CnLecsMpoaMpsIndex_Object = MibTableColumn
cnLecsMpoaMpsIndex = _CnLecsMpoaMpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 1),
    _CnLecsMpoaMpsIndex_Type()
)
cnLecsMpoaMpsIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsIndex.setStatus("mandatory")
_CnLecsMpoaMpsRowStatus_Type = RowStatus
_CnLecsMpoaMpsRowStatus_Object = MibTableColumn
cnLecsMpoaMpsRowStatus = _CnLecsMpoaMpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 2),
    _CnLecsMpoaMpsRowStatus_Type()
)
cnLecsMpoaMpsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsRowStatus.setStatus("mandatory")
_CnLecsMpoaMpsCtrlAtmAddr_Type = AtmConfigAddr
_CnLecsMpoaMpsCtrlAtmAddr_Object = MibTableColumn
cnLecsMpoaMpsCtrlAtmAddr = _CnLecsMpoaMpsCtrlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 3),
    _CnLecsMpoaMpsCtrlAtmAddr_Type()
)
cnLecsMpoaMpsCtrlAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsCtrlAtmAddr.setStatus("mandatory")


class _CnLecsMpoaMpsKeepAliveTime_Type(Integer32):
    """Custom type cnLecsMpoaMpsKeepAliveTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CnLecsMpoaMpsKeepAliveTime_Type.__name__ = "Integer32"
_CnLecsMpoaMpsKeepAliveTime_Object = MibTableColumn
cnLecsMpoaMpsKeepAliveTime = _CnLecsMpoaMpsKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 4),
    _CnLecsMpoaMpsKeepAliveTime_Type()
)
cnLecsMpoaMpsKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsKeepAliveTime.setStatus("mandatory")


class _CnLecsMpoaMpsKeepAliveLifeTime_Type(Integer32):
    """Custom type cnLecsMpoaMpsKeepAliveLifeTime based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_CnLecsMpoaMpsKeepAliveLifeTime_Type.__name__ = "Integer32"
_CnLecsMpoaMpsKeepAliveLifeTime_Object = MibTableColumn
cnLecsMpoaMpsKeepAliveLifeTime = _CnLecsMpoaMpsKeepAliveLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 5),
    _CnLecsMpoaMpsKeepAliveLifeTime_Type()
)
cnLecsMpoaMpsKeepAliveLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsKeepAliveLifeTime.setStatus("mandatory")


class _CnLecsMpoaMpsInitialRetryTime_Type(Integer32):
    """Custom type cnLecsMpoaMpsInitialRetryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CnLecsMpoaMpsInitialRetryTime_Type.__name__ = "Integer32"
_CnLecsMpoaMpsInitialRetryTime_Object = MibTableColumn
cnLecsMpoaMpsInitialRetryTime = _CnLecsMpoaMpsInitialRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 6),
    _CnLecsMpoaMpsInitialRetryTime_Type()
)
cnLecsMpoaMpsInitialRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsInitialRetryTime.setStatus("mandatory")


class _CnLecsMpoaMpsRetryTimeMaximum_Type(Integer32):
    """Custom type cnLecsMpoaMpsRetryTimeMaximum based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CnLecsMpoaMpsRetryTimeMaximum_Type.__name__ = "Integer32"
_CnLecsMpoaMpsRetryTimeMaximum_Object = MibTableColumn
cnLecsMpoaMpsRetryTimeMaximum = _CnLecsMpoaMpsRetryTimeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 7),
    _CnLecsMpoaMpsRetryTimeMaximum_Type()
)
cnLecsMpoaMpsRetryTimeMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsRetryTimeMaximum.setStatus("mandatory")


class _CnLecsMpoaMpsGiveupTime_Type(Integer32):
    """Custom type cnLecsMpoaMpsGiveupTime based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_CnLecsMpoaMpsGiveupTime_Type.__name__ = "Integer32"
_CnLecsMpoaMpsGiveupTime_Object = MibTableColumn
cnLecsMpoaMpsGiveupTime = _CnLecsMpoaMpsGiveupTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 8),
    _CnLecsMpoaMpsGiveupTime_Type()
)
cnLecsMpoaMpsGiveupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsGiveupTime.setStatus("mandatory")


class _CnLecsMpoaMpsDefaultHoldingTime_Type(Integer32):
    """Custom type cnLecsMpoaMpsDefaultHoldingTime based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_CnLecsMpoaMpsDefaultHoldingTime_Type.__name__ = "Integer32"
_CnLecsMpoaMpsDefaultHoldingTime_Object = MibTableColumn
cnLecsMpoaMpsDefaultHoldingTime = _CnLecsMpoaMpsDefaultHoldingTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 9),
    _CnLecsMpoaMpsDefaultHoldingTime_Type()
)
cnLecsMpoaMpsDefaultHoldingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsDefaultHoldingTime.setStatus("mandatory")


class _CnLecsMpoaMpsDefaultTLV_Type(TruthValue):
    """Custom type cnLecsMpoaMpsDefaultTLV based on TruthValue"""


_CnLecsMpoaMpsDefaultTLV_Object = MibTableColumn
cnLecsMpoaMpsDefaultTLV = _CnLecsMpoaMpsDefaultTLV_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 2, 1, 10),
    _CnLecsMpoaMpsDefaultTLV_Type()
)
cnLecsMpoaMpsDefaultTLV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsDefaultTLV.setStatus("mandatory")
_CnLecsMpoaMpcProtocolTable_Object = MibTable
cnLecsMpoaMpcProtocolTable = _CnLecsMpoaMpcProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3)
)
if mibBuilder.loadTexts:
    cnLecsMpoaMpcProtocolTable.setStatus("mandatory")
_CnLecsMpoaMpcProtocolEntry_Object = MibTableRow
cnLecsMpoaMpcProtocolEntry = _CnLecsMpoaMpcProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3, 1)
)
cnLecsMpoaMpcProtocolEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
    (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpcProtocolIndex"),
    (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpcFlowDetectProtocol"),
)
if mibBuilder.loadTexts:
    cnLecsMpoaMpcProtocolEntry.setStatus("mandatory")
_CnLecsMpoaMpcProtocolIndex_Type = MpcIndex
_CnLecsMpoaMpcProtocolIndex_Object = MibTableColumn
cnLecsMpoaMpcProtocolIndex = _CnLecsMpoaMpcProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3, 1, 1),
    _CnLecsMpoaMpcProtocolIndex_Type()
)
cnLecsMpoaMpcProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcProtocolIndex.setStatus("mandatory")
_CnLecsMpoaMpcFlowDetectProtocol_Type = InternetworkAddrType
_CnLecsMpoaMpcFlowDetectProtocol_Object = MibTableColumn
cnLecsMpoaMpcFlowDetectProtocol = _CnLecsMpoaMpcFlowDetectProtocol_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3, 1, 2),
    _CnLecsMpoaMpcFlowDetectProtocol_Type()
)
cnLecsMpoaMpcFlowDetectProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcFlowDetectProtocol.setStatus("mandatory")
_CnLecsMpoaMpcProtocolRowStatus_Type = RowStatus
_CnLecsMpoaMpcProtocolRowStatus_Object = MibTableColumn
cnLecsMpoaMpcProtocolRowStatus = _CnLecsMpoaMpcProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3, 1, 3),
    _CnLecsMpoaMpcProtocolRowStatus_Type()
)
cnLecsMpoaMpcProtocolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcProtocolRowStatus.setStatus("mandatory")
_CnLecsMpoaMpcProtocolEnable_Type = TruthValue
_CnLecsMpoaMpcProtocolEnable_Object = MibTableColumn
cnLecsMpoaMpcProtocolEnable = _CnLecsMpoaMpcProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 3, 1, 4),
    _CnLecsMpoaMpcProtocolEnable_Type()
)
cnLecsMpoaMpcProtocolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpcProtocolEnable.setStatus("mandatory")
_CnLecsMpoaMpsProtocolTable_Object = MibTable
cnLecsMpoaMpsProtocolTable = _CnLecsMpoaMpsProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4)
)
if mibBuilder.loadTexts:
    cnLecsMpoaMpsProtocolTable.setStatus("mandatory")
_CnLecsMpoaMpsProtocolEntry_Object = MibTableRow
cnLecsMpoaMpsProtocolEntry = _CnLecsMpoaMpsProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4, 1)
)
cnLecsMpoaMpsProtocolEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
    (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpsProtocolIndex"),
    (0, "CENTILLION-LECS-MPOA-MIB", "cnLecsMpoaMpsInternetworkLayerProtocol"),
)
if mibBuilder.loadTexts:
    cnLecsMpoaMpsProtocolEntry.setStatus("mandatory")
_CnLecsMpoaMpsProtocolIndex_Type = MpsIndex
_CnLecsMpoaMpsProtocolIndex_Object = MibTableColumn
cnLecsMpoaMpsProtocolIndex = _CnLecsMpoaMpsProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4, 1, 1),
    _CnLecsMpoaMpsProtocolIndex_Type()
)
cnLecsMpoaMpsProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsProtocolIndex.setStatus("mandatory")
_CnLecsMpoaMpsInternetworkLayerProtocol_Type = InternetworkAddrType
_CnLecsMpoaMpsInternetworkLayerProtocol_Object = MibTableColumn
cnLecsMpoaMpsInternetworkLayerProtocol = _CnLecsMpoaMpsInternetworkLayerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4, 1, 2),
    _CnLecsMpoaMpsInternetworkLayerProtocol_Type()
)
cnLecsMpoaMpsInternetworkLayerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsInternetworkLayerProtocol.setStatus("mandatory")
_CnLecsMpoaMpsProtocolRowStatus_Type = RowStatus
_CnLecsMpoaMpsProtocolRowStatus_Object = MibTableColumn
cnLecsMpoaMpsProtocolRowStatus = _CnLecsMpoaMpsProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4, 1, 3),
    _CnLecsMpoaMpsProtocolRowStatus_Type()
)
cnLecsMpoaMpsProtocolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsProtocolRowStatus.setStatus("mandatory")
_CnLecsMpoaMpsProtocolEnable_Type = TruthValue
_CnLecsMpoaMpsProtocolEnable_Object = MibTableColumn
cnLecsMpoaMpsProtocolEnable = _CnLecsMpoaMpsProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 2, 3, 6, 4, 1, 4),
    _CnLecsMpoaMpsProtocolEnable_Type()
)
cnLecsMpoaMpsProtocolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnLecsMpoaMpsProtocolEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-LECS-MPOA-MIB",
    **{"cnLecsMpoaGroup": cnLecsMpoaGroup,
       "cnLecsMpoaMpcTable": cnLecsMpoaMpcTable,
       "cnLecsMpoaMpcEntry": cnLecsMpoaMpcEntry,
       "cnLecsMpoaMpcIndex": cnLecsMpoaMpcIndex,
       "cnLecsMpoaMpcRowStatus": cnLecsMpoaMpcRowStatus,
       "cnLecsMpoaMpcCtrlAtmAddr": cnLecsMpoaMpcCtrlAtmAddr,
       "cnLecsMpoaMpcSCSetupFrameCount": cnLecsMpoaMpcSCSetupFrameCount,
       "cnLecsMpoaMpcSCSetupFrameTime": cnLecsMpoaMpcSCSetupFrameTime,
       "cnLecsMpoaMpcInitialRetryTime": cnLecsMpoaMpcInitialRetryTime,
       "cnLecsMpoaMpcRetryTimeMaximum": cnLecsMpoaMpcRetryTimeMaximum,
       "cnLecsMpoaMpcHoldDownTime": cnLecsMpoaMpcHoldDownTime,
       "cnLecsMpoaMpcDefaultTLV": cnLecsMpoaMpcDefaultTLV,
       "cnLecsMpoaMpsTable": cnLecsMpoaMpsTable,
       "cnLecsMpoaMpsEntry": cnLecsMpoaMpsEntry,
       "cnLecsMpoaMpsIndex": cnLecsMpoaMpsIndex,
       "cnLecsMpoaMpsRowStatus": cnLecsMpoaMpsRowStatus,
       "cnLecsMpoaMpsCtrlAtmAddr": cnLecsMpoaMpsCtrlAtmAddr,
       "cnLecsMpoaMpsKeepAliveTime": cnLecsMpoaMpsKeepAliveTime,
       "cnLecsMpoaMpsKeepAliveLifeTime": cnLecsMpoaMpsKeepAliveLifeTime,
       "cnLecsMpoaMpsInitialRetryTime": cnLecsMpoaMpsInitialRetryTime,
       "cnLecsMpoaMpsRetryTimeMaximum": cnLecsMpoaMpsRetryTimeMaximum,
       "cnLecsMpoaMpsGiveupTime": cnLecsMpoaMpsGiveupTime,
       "cnLecsMpoaMpsDefaultHoldingTime": cnLecsMpoaMpsDefaultHoldingTime,
       "cnLecsMpoaMpsDefaultTLV": cnLecsMpoaMpsDefaultTLV,
       "cnLecsMpoaMpcProtocolTable": cnLecsMpoaMpcProtocolTable,
       "cnLecsMpoaMpcProtocolEntry": cnLecsMpoaMpcProtocolEntry,
       "cnLecsMpoaMpcProtocolIndex": cnLecsMpoaMpcProtocolIndex,
       "cnLecsMpoaMpcFlowDetectProtocol": cnLecsMpoaMpcFlowDetectProtocol,
       "cnLecsMpoaMpcProtocolRowStatus": cnLecsMpoaMpcProtocolRowStatus,
       "cnLecsMpoaMpcProtocolEnable": cnLecsMpoaMpcProtocolEnable,
       "cnLecsMpoaMpsProtocolTable": cnLecsMpoaMpsProtocolTable,
       "cnLecsMpoaMpsProtocolEntry": cnLecsMpoaMpsProtocolEntry,
       "cnLecsMpoaMpsProtocolIndex": cnLecsMpoaMpsProtocolIndex,
       "cnLecsMpoaMpsInternetworkLayerProtocol": cnLecsMpoaMpsInternetworkLayerProtocol,
       "cnLecsMpoaMpsProtocolRowStatus": cnLecsMpoaMpsProtocolRowStatus,
       "cnLecsMpoaMpsProtocolEnable": cnLecsMpoaMpsProtocolEnable}
)
