# SNMP MIB module (HUAWEI-LswRSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LswRSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:45 2024
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

(dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPort",
    "dot1dStpPortEntry")

(lswCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "lswCommon")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwLswRstpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6)
)
hwLswRstpMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwLswRstpMibObject_ObjectIdentity = ObjectIdentity
hwLswRstpMibObject = _HwLswRstpMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1)
)
_HwRstpEventsV2_ObjectIdentity = ObjectIdentity
hwRstpEventsV2 = _HwRstpEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 0)
)
if mibBuilder.loadTexts:
    hwRstpEventsV2.setStatus("current")
_Hwdot1dStpStatus_Type = EnabledStatus
_Hwdot1dStpStatus_Object = MibScalar
hwdot1dStpStatus = _Hwdot1dStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 1),
    _Hwdot1dStpStatus_Type()
)
hwdot1dStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpStatus.setStatus("current")


class _Hwdot1dStpForceVersion_Type(Integer32):
    """Custom type hwdot1dStpForceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stp", 0))
    )


_Hwdot1dStpForceVersion_Type.__name__ = "Integer32"
_Hwdot1dStpForceVersion_Object = MibScalar
hwdot1dStpForceVersion = _Hwdot1dStpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 2),
    _Hwdot1dStpForceVersion_Type()
)
hwdot1dStpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpForceVersion.setStatus("current")


class _Hwdot1dStpDiameter_Type(Integer32):
    """Custom type hwdot1dStpDiameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Hwdot1dStpDiameter_Type.__name__ = "Integer32"
_Hwdot1dStpDiameter_Object = MibScalar
hwdot1dStpDiameter = _Hwdot1dStpDiameter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 3),
    _Hwdot1dStpDiameter_Type()
)
hwdot1dStpDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpDiameter.setStatus("current")
_Hwdot1dStpRootBridgeAddress_Type = MacAddress
_Hwdot1dStpRootBridgeAddress_Object = MibScalar
hwdot1dStpRootBridgeAddress = _Hwdot1dStpRootBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 4),
    _Hwdot1dStpRootBridgeAddress_Type()
)
hwdot1dStpRootBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpRootBridgeAddress.setStatus("current")
_Hwdot1dStpPortXTable_Object = MibTable
hwdot1dStpPortXTable = _Hwdot1dStpPortXTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    hwdot1dStpPortXTable.setStatus("current")
_Hwdot1dStpPortXEntry_Object = MibTableRow
hwdot1dStpPortXEntry = _Hwdot1dStpPortXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwdot1dStpPortXEntry.setStatus("current")
_Hwdot1dStpPortStatus_Type = EnabledStatus
_Hwdot1dStpPortStatus_Object = MibTableColumn
hwdot1dStpPortStatus = _Hwdot1dStpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 1),
    _Hwdot1dStpPortStatus_Type()
)
hwdot1dStpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpPortStatus.setStatus("current")
_Hwdot1dStpPortEdgeport_Type = TruthValue
_Hwdot1dStpPortEdgeport_Object = MibTableColumn
hwdot1dStpPortEdgeport = _Hwdot1dStpPortEdgeport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 2),
    _Hwdot1dStpPortEdgeport_Type()
)
hwdot1dStpPortEdgeport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpPortEdgeport.setStatus("current")


class _Hwdot1dStpPortPointToPoint_Type(Integer32):
    """Custom type hwdot1dStpPortPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("forceFalse", 2),
          ("forceTrue", 1))
    )


_Hwdot1dStpPortPointToPoint_Type.__name__ = "Integer32"
_Hwdot1dStpPortPointToPoint_Object = MibTableColumn
hwdot1dStpPortPointToPoint = _Hwdot1dStpPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 3),
    _Hwdot1dStpPortPointToPoint_Type()
)
hwdot1dStpPortPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpPortPointToPoint.setStatus("current")
_Hwdot1dStpMcheck_Type = TruthValue
_Hwdot1dStpMcheck_Object = MibTableColumn
hwdot1dStpMcheck = _Hwdot1dStpMcheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 4),
    _Hwdot1dStpMcheck_Type()
)
hwdot1dStpMcheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpMcheck.setStatus("current")


class _Hwdot1dStpTransLimit_Type(Integer32):
    """Custom type hwdot1dStpTransLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hwdot1dStpTransLimit_Type.__name__ = "Integer32"
_Hwdot1dStpTransLimit_Object = MibTableColumn
hwdot1dStpTransLimit = _Hwdot1dStpTransLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 5),
    _Hwdot1dStpTransLimit_Type()
)
hwdot1dStpTransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpTransLimit.setStatus("current")
_Hwdot1dStpRXStpBPDU_Type = Counter32
_Hwdot1dStpRXStpBPDU_Object = MibTableColumn
hwdot1dStpRXStpBPDU = _Hwdot1dStpRXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 6),
    _Hwdot1dStpRXStpBPDU_Type()
)
hwdot1dStpRXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpRXStpBPDU.setStatus("current")
_Hwdot1dStpTXStpBPDU_Type = Counter32
_Hwdot1dStpTXStpBPDU_Object = MibTableColumn
hwdot1dStpTXStpBPDU = _Hwdot1dStpTXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 7),
    _Hwdot1dStpTXStpBPDU_Type()
)
hwdot1dStpTXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpTXStpBPDU.setStatus("current")
_Hwdot1dStpRXTCNBPDU_Type = Counter32
_Hwdot1dStpRXTCNBPDU_Object = MibTableColumn
hwdot1dStpRXTCNBPDU = _Hwdot1dStpRXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 8),
    _Hwdot1dStpRXTCNBPDU_Type()
)
hwdot1dStpRXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpRXTCNBPDU.setStatus("current")
_Hwdot1dStpTXTCNBPDU_Type = Counter32
_Hwdot1dStpTXTCNBPDU_Object = MibTableColumn
hwdot1dStpTXTCNBPDU = _Hwdot1dStpTXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 9),
    _Hwdot1dStpTXTCNBPDU_Type()
)
hwdot1dStpTXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpTXTCNBPDU.setStatus("current")
_Hwdot1dStpRXRSTPBPDU_Type = Counter32
_Hwdot1dStpRXRSTPBPDU_Object = MibTableColumn
hwdot1dStpRXRSTPBPDU = _Hwdot1dStpRXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 10),
    _Hwdot1dStpRXRSTPBPDU_Type()
)
hwdot1dStpRXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpRXRSTPBPDU.setStatus("current")
_Hwdot1dStpTXRSTPBPDU_Type = Counter32
_Hwdot1dStpTXRSTPBPDU_Object = MibTableColumn
hwdot1dStpTXRSTPBPDU = _Hwdot1dStpTXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 11),
    _Hwdot1dStpTXRSTPBPDU_Type()
)
hwdot1dStpTXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpTXRSTPBPDU.setStatus("current")


class _Hwdot1dStpClearStatistics_Type(Integer32):
    """Custom type hwdot1dStpClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_Hwdot1dStpClearStatistics_Type.__name__ = "Integer32"
_Hwdot1dStpClearStatistics_Object = MibTableColumn
hwdot1dStpClearStatistics = _Hwdot1dStpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 12),
    _Hwdot1dStpClearStatistics_Type()
)
hwdot1dStpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpClearStatistics.setStatus("current")


class _Hwdot1dSetStpDefaultPortCost_Type(Integer32):
    """Custom type hwdot1dSetStpDefaultPortCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_Hwdot1dSetStpDefaultPortCost_Type.__name__ = "Integer32"
_Hwdot1dSetStpDefaultPortCost_Object = MibTableColumn
hwdot1dSetStpDefaultPortCost = _Hwdot1dSetStpDefaultPortCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 13),
    _Hwdot1dSetStpDefaultPortCost_Type()
)
hwdot1dSetStpDefaultPortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dSetStpDefaultPortCost.setStatus("current")
_Hwdot1dStpRootGuard_Type = EnabledStatus
_Hwdot1dStpRootGuard_Object = MibTableColumn
hwdot1dStpRootGuard = _Hwdot1dStpRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 14),
    _Hwdot1dStpRootGuard_Type()
)
hwdot1dStpRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpRootGuard.setStatus("current")
_Hwdot1dStpLoopGuard_Type = EnabledStatus
_Hwdot1dStpLoopGuard_Object = MibTableColumn
hwdot1dStpLoopGuard = _Hwdot1dStpLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 15),
    _Hwdot1dStpLoopGuard_Type()
)
hwdot1dStpLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpLoopGuard.setStatus("current")


class _Hwdot1dStpPortBlockedReason_Type(Integer32):
    """Custom type hwdot1dStpPortBlockedReason based on Integer32"""
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
        *(("blockForBPDUGuard", 4),
          ("blockForLoopGuard", 5),
          ("blockForProtocol", 2),
          ("blockForRootGuard", 3),
          ("notBlock", 1))
    )


_Hwdot1dStpPortBlockedReason_Type.__name__ = "Integer32"
_Hwdot1dStpPortBlockedReason_Object = MibTableColumn
hwdot1dStpPortBlockedReason = _Hwdot1dStpPortBlockedReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 16),
    _Hwdot1dStpPortBlockedReason_Type()
)
hwdot1dStpPortBlockedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpPortBlockedReason.setStatus("current")
_Hwdot1dStpRXTCBPDU_Type = Counter32
_Hwdot1dStpRXTCBPDU_Object = MibTableColumn
hwdot1dStpRXTCBPDU = _Hwdot1dStpRXTCBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 17),
    _Hwdot1dStpRXTCBPDU_Type()
)
hwdot1dStpRXTCBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpRXTCBPDU.setStatus("current")


class _Hwdot1dStpPortSendingBPDUType_Type(Integer32):
    """Custom type hwdot1dStpPortSendingBPDUType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stp", 0))
    )


_Hwdot1dStpPortSendingBPDUType_Type.__name__ = "Integer32"
_Hwdot1dStpPortSendingBPDUType_Object = MibTableColumn
hwdot1dStpPortSendingBPDUType = _Hwdot1dStpPortSendingBPDUType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 18),
    _Hwdot1dStpPortSendingBPDUType_Type()
)
hwdot1dStpPortSendingBPDUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpPortSendingBPDUType.setStatus("current")


class _Hwdot1dStpOperPortPointToPoint_Type(Integer32):
    """Custom type hwdot1dStpOperPortPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Hwdot1dStpOperPortPointToPoint_Type.__name__ = "Integer32"
_Hwdot1dStpOperPortPointToPoint_Object = MibTableColumn
hwdot1dStpOperPortPointToPoint = _Hwdot1dStpOperPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 5, 1, 19),
    _Hwdot1dStpOperPortPointToPoint_Type()
)
hwdot1dStpOperPortPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dStpOperPortPointToPoint.setStatus("current")
_HwDot1dStpBpduGuard_Type = EnabledStatus
_HwDot1dStpBpduGuard_Object = MibScalar
hwDot1dStpBpduGuard = _HwDot1dStpBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 6),
    _HwDot1dStpBpduGuard_Type()
)
hwDot1dStpBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1dStpBpduGuard.setStatus("current")


class _HwDot1dStpRootType_Type(Integer32):
    """Custom type hwDot1dStpRootType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_HwDot1dStpRootType_Type.__name__ = "Integer32"
_HwDot1dStpRootType_Object = MibScalar
hwDot1dStpRootType = _HwDot1dStpRootType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 7),
    _HwDot1dStpRootType_Type()
)
hwDot1dStpRootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1dStpRootType.setStatus("current")


class _HwDot1dTimeOutFactor_Type(Integer32):
    """Custom type hwDot1dTimeOutFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 7),
    )


_HwDot1dTimeOutFactor_Type.__name__ = "Integer32"
_HwDot1dTimeOutFactor_Object = MibScalar
hwDot1dTimeOutFactor = _HwDot1dTimeOutFactor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 8),
    _HwDot1dTimeOutFactor_Type()
)
hwDot1dTimeOutFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1dTimeOutFactor.setStatus("current")


class _HwDot1dStpPathCostStandard_Type(Integer32):
    """Custom type hwDot1dStpPathCostStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d-1998", 1),
          ("dot1t", 2),
          ("legacy", 3))
    )


_HwDot1dStpPathCostStandard_Type.__name__ = "Integer32"
_HwDot1dStpPathCostStandard_Object = MibScalar
hwDot1dStpPathCostStandard = _HwDot1dStpPathCostStandard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 9),
    _HwDot1dStpPathCostStandard_Type()
)
hwDot1dStpPathCostStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDot1dStpPathCostStandard.setStatus("current")
_Hwdot1dStpIgnoredVlanTable_Object = MibTable
hwdot1dStpIgnoredVlanTable = _Hwdot1dStpIgnoredVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 10)
)
if mibBuilder.loadTexts:
    hwdot1dStpIgnoredVlanTable.setStatus("current")
_Hwdot1dStpIgnoredVlanEntry_Object = MibTableRow
hwdot1dStpIgnoredVlanEntry = _Hwdot1dStpIgnoredVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 10, 1)
)
hwdot1dStpIgnoredVlanEntry.setIndexNames(
    (0, "HUAWEI-LswRSTP-MIB", "hwdot1dVlan"),
)
if mibBuilder.loadTexts:
    hwdot1dStpIgnoredVlanEntry.setStatus("current")


class _Hwdot1dVlan_Type(Integer32):
    """Custom type hwdot1dVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hwdot1dVlan_Type.__name__ = "Integer32"
_Hwdot1dVlan_Object = MibTableColumn
hwdot1dVlan = _Hwdot1dVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 10, 1, 1),
    _Hwdot1dVlan_Type()
)
hwdot1dVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1dVlan.setStatus("current")


class _Hwdot1dStpIgnore_Type(Integer32):
    """Custom type hwdot1dStpIgnore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Hwdot1dStpIgnore_Type.__name__ = "Integer32"
_Hwdot1dStpIgnore_Object = MibTableColumn
hwdot1dStpIgnore = _Hwdot1dStpIgnore_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 10, 1, 2),
    _Hwdot1dStpIgnore_Type()
)
hwdot1dStpIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1dStpIgnore.setStatus("current")
dot1dStpPortEntry.registerAugmentions(
    ("HUAWEI-LswRSTP-MIB",
     "hwdot1dStpPortXEntry")
)
hwdot1dStpPortXEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hwRstpBpduGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 0, 1)
)
hwRstpBpduGuarded.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    hwRstpBpduGuarded.setStatus(
        "current"
    )

hwRstpRootGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 0, 2)
)
hwRstpRootGuarded.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    hwRstpRootGuarded.setStatus(
        "current"
    )

hwRstpBridgeLostRootPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 0, 3)
)
if mibBuilder.loadTexts:
    hwRstpBridgeLostRootPrimary.setStatus(
        "current"
    )

hwRstpLoopGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 6, 1, 0, 4)
)
hwRstpLoopGuarded.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    hwRstpLoopGuarded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LswRSTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hwLswRstpMib": hwLswRstpMib,
       "hwLswRstpMibObject": hwLswRstpMibObject,
       "hwRstpEventsV2": hwRstpEventsV2,
       "hwRstpBpduGuarded": hwRstpBpduGuarded,
       "hwRstpRootGuarded": hwRstpRootGuarded,
       "hwRstpBridgeLostRootPrimary": hwRstpBridgeLostRootPrimary,
       "hwRstpLoopGuarded": hwRstpLoopGuarded,
       "hwdot1dStpStatus": hwdot1dStpStatus,
       "hwdot1dStpForceVersion": hwdot1dStpForceVersion,
       "hwdot1dStpDiameter": hwdot1dStpDiameter,
       "hwdot1dStpRootBridgeAddress": hwdot1dStpRootBridgeAddress,
       "hwdot1dStpPortXTable": hwdot1dStpPortXTable,
       "hwdot1dStpPortXEntry": hwdot1dStpPortXEntry,
       "hwdot1dStpPortStatus": hwdot1dStpPortStatus,
       "hwdot1dStpPortEdgeport": hwdot1dStpPortEdgeport,
       "hwdot1dStpPortPointToPoint": hwdot1dStpPortPointToPoint,
       "hwdot1dStpMcheck": hwdot1dStpMcheck,
       "hwdot1dStpTransLimit": hwdot1dStpTransLimit,
       "hwdot1dStpRXStpBPDU": hwdot1dStpRXStpBPDU,
       "hwdot1dStpTXStpBPDU": hwdot1dStpTXStpBPDU,
       "hwdot1dStpRXTCNBPDU": hwdot1dStpRXTCNBPDU,
       "hwdot1dStpTXTCNBPDU": hwdot1dStpTXTCNBPDU,
       "hwdot1dStpRXRSTPBPDU": hwdot1dStpRXRSTPBPDU,
       "hwdot1dStpTXRSTPBPDU": hwdot1dStpTXRSTPBPDU,
       "hwdot1dStpClearStatistics": hwdot1dStpClearStatistics,
       "hwdot1dSetStpDefaultPortCost": hwdot1dSetStpDefaultPortCost,
       "hwdot1dStpRootGuard": hwdot1dStpRootGuard,
       "hwdot1dStpLoopGuard": hwdot1dStpLoopGuard,
       "hwdot1dStpPortBlockedReason": hwdot1dStpPortBlockedReason,
       "hwdot1dStpRXTCBPDU": hwdot1dStpRXTCBPDU,
       "hwdot1dStpPortSendingBPDUType": hwdot1dStpPortSendingBPDUType,
       "hwdot1dStpOperPortPointToPoint": hwdot1dStpOperPortPointToPoint,
       "hwDot1dStpBpduGuard": hwDot1dStpBpduGuard,
       "hwDot1dStpRootType": hwDot1dStpRootType,
       "hwDot1dTimeOutFactor": hwDot1dTimeOutFactor,
       "hwDot1dStpPathCostStandard": hwDot1dStpPathCostStandard,
       "hwdot1dStpIgnoredVlanTable": hwdot1dStpIgnoredVlanTable,
       "hwdot1dStpIgnoredVlanEntry": hwdot1dStpIgnoredVlanEntry,
       "hwdot1dVlan": hwdot1dVlan,
       "hwdot1dStpIgnore": hwdot1dStpIgnore}
)
