# SNMP MIB module (HH3C-LswRSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswRSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:00 2024
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

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

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

hh3cLswRstpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6)
)
hh3cLswRstpMib.setRevisions(
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

_Hh3cLswRstpMibObject_ObjectIdentity = ObjectIdentity
hh3cLswRstpMibObject = _Hh3cLswRstpMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1)
)
_Hh3cRstpEventsV2_ObjectIdentity = ObjectIdentity
hh3cRstpEventsV2 = _Hh3cRstpEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 0)
)
if mibBuilder.loadTexts:
    hh3cRstpEventsV2.setStatus("current")
_Hh3cdot1dStpStatus_Type = EnabledStatus
_Hh3cdot1dStpStatus_Object = MibScalar
hh3cdot1dStpStatus = _Hh3cdot1dStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 1),
    _Hh3cdot1dStpStatus_Type()
)
hh3cdot1dStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpStatus.setStatus("current")


class _Hh3cdot1dStpForceVersion_Type(Integer32):
    """Custom type hh3cdot1dStpForceVersion based on Integer32"""
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


_Hh3cdot1dStpForceVersion_Type.__name__ = "Integer32"
_Hh3cdot1dStpForceVersion_Object = MibScalar
hh3cdot1dStpForceVersion = _Hh3cdot1dStpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 2),
    _Hh3cdot1dStpForceVersion_Type()
)
hh3cdot1dStpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpForceVersion.setStatus("current")


class _Hh3cdot1dStpDiameter_Type(Integer32):
    """Custom type hh3cdot1dStpDiameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Hh3cdot1dStpDiameter_Type.__name__ = "Integer32"
_Hh3cdot1dStpDiameter_Object = MibScalar
hh3cdot1dStpDiameter = _Hh3cdot1dStpDiameter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 3),
    _Hh3cdot1dStpDiameter_Type()
)
hh3cdot1dStpDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpDiameter.setStatus("current")
_Hh3cdot1dStpRootBridgeAddress_Type = MacAddress
_Hh3cdot1dStpRootBridgeAddress_Object = MibScalar
hh3cdot1dStpRootBridgeAddress = _Hh3cdot1dStpRootBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 4),
    _Hh3cdot1dStpRootBridgeAddress_Type()
)
hh3cdot1dStpRootBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpRootBridgeAddress.setStatus("current")
_Hh3cdot1dStpPortXTable_Object = MibTable
hh3cdot1dStpPortXTable = _Hh3cdot1dStpPortXTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cdot1dStpPortXTable.setStatus("current")
_Hh3cdot1dStpPortXEntry_Object = MibTableRow
hh3cdot1dStpPortXEntry = _Hh3cdot1dStpPortXEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cdot1dStpPortXEntry.setStatus("current")
_Hh3cdot1dStpPortStatus_Type = EnabledStatus
_Hh3cdot1dStpPortStatus_Object = MibTableColumn
hh3cdot1dStpPortStatus = _Hh3cdot1dStpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 1),
    _Hh3cdot1dStpPortStatus_Type()
)
hh3cdot1dStpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpPortStatus.setStatus("current")
_Hh3cdot1dStpPortEdgeport_Type = TruthValue
_Hh3cdot1dStpPortEdgeport_Object = MibTableColumn
hh3cdot1dStpPortEdgeport = _Hh3cdot1dStpPortEdgeport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 2),
    _Hh3cdot1dStpPortEdgeport_Type()
)
hh3cdot1dStpPortEdgeport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpPortEdgeport.setStatus("current")


class _Hh3cdot1dStpPortPointToPoint_Type(Integer32):
    """Custom type hh3cdot1dStpPortPointToPoint based on Integer32"""
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


_Hh3cdot1dStpPortPointToPoint_Type.__name__ = "Integer32"
_Hh3cdot1dStpPortPointToPoint_Object = MibTableColumn
hh3cdot1dStpPortPointToPoint = _Hh3cdot1dStpPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 3),
    _Hh3cdot1dStpPortPointToPoint_Type()
)
hh3cdot1dStpPortPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpPortPointToPoint.setStatus("current")
_Hh3cdot1dStpMcheck_Type = TruthValue
_Hh3cdot1dStpMcheck_Object = MibTableColumn
hh3cdot1dStpMcheck = _Hh3cdot1dStpMcheck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 4),
    _Hh3cdot1dStpMcheck_Type()
)
hh3cdot1dStpMcheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpMcheck.setStatus("current")


class _Hh3cdot1dStpTransLimit_Type(Integer32):
    """Custom type hh3cdot1dStpTransLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cdot1dStpTransLimit_Type.__name__ = "Integer32"
_Hh3cdot1dStpTransLimit_Object = MibTableColumn
hh3cdot1dStpTransLimit = _Hh3cdot1dStpTransLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 5),
    _Hh3cdot1dStpTransLimit_Type()
)
hh3cdot1dStpTransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpTransLimit.setStatus("current")
_Hh3cdot1dStpRXStpBPDU_Type = Counter32
_Hh3cdot1dStpRXStpBPDU_Object = MibTableColumn
hh3cdot1dStpRXStpBPDU = _Hh3cdot1dStpRXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 6),
    _Hh3cdot1dStpRXStpBPDU_Type()
)
hh3cdot1dStpRXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpRXStpBPDU.setStatus("current")
_Hh3cdot1dStpTXStpBPDU_Type = Counter32
_Hh3cdot1dStpTXStpBPDU_Object = MibTableColumn
hh3cdot1dStpTXStpBPDU = _Hh3cdot1dStpTXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 7),
    _Hh3cdot1dStpTXStpBPDU_Type()
)
hh3cdot1dStpTXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpTXStpBPDU.setStatus("current")
_Hh3cdot1dStpRXTCNBPDU_Type = Counter32
_Hh3cdot1dStpRXTCNBPDU_Object = MibTableColumn
hh3cdot1dStpRXTCNBPDU = _Hh3cdot1dStpRXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 8),
    _Hh3cdot1dStpRXTCNBPDU_Type()
)
hh3cdot1dStpRXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpRXTCNBPDU.setStatus("current")
_Hh3cdot1dStpTXTCNBPDU_Type = Counter32
_Hh3cdot1dStpTXTCNBPDU_Object = MibTableColumn
hh3cdot1dStpTXTCNBPDU = _Hh3cdot1dStpTXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 9),
    _Hh3cdot1dStpTXTCNBPDU_Type()
)
hh3cdot1dStpTXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpTXTCNBPDU.setStatus("current")
_Hh3cdot1dStpRXRSTPBPDU_Type = Counter32
_Hh3cdot1dStpRXRSTPBPDU_Object = MibTableColumn
hh3cdot1dStpRXRSTPBPDU = _Hh3cdot1dStpRXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 10),
    _Hh3cdot1dStpRXRSTPBPDU_Type()
)
hh3cdot1dStpRXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpRXRSTPBPDU.setStatus("current")
_Hh3cdot1dStpTXRSTPBPDU_Type = Counter32
_Hh3cdot1dStpTXRSTPBPDU_Object = MibTableColumn
hh3cdot1dStpTXRSTPBPDU = _Hh3cdot1dStpTXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 11),
    _Hh3cdot1dStpTXRSTPBPDU_Type()
)
hh3cdot1dStpTXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpTXRSTPBPDU.setStatus("current")


class _Hh3cdot1dStpClearStatistics_Type(Integer32):
    """Custom type hh3cdot1dStpClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_Hh3cdot1dStpClearStatistics_Type.__name__ = "Integer32"
_Hh3cdot1dStpClearStatistics_Object = MibTableColumn
hh3cdot1dStpClearStatistics = _Hh3cdot1dStpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 12),
    _Hh3cdot1dStpClearStatistics_Type()
)
hh3cdot1dStpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpClearStatistics.setStatus("current")


class _Hh3cdot1dSetStpDefaultPortCost_Type(Integer32):
    """Custom type hh3cdot1dSetStpDefaultPortCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_Hh3cdot1dSetStpDefaultPortCost_Type.__name__ = "Integer32"
_Hh3cdot1dSetStpDefaultPortCost_Object = MibTableColumn
hh3cdot1dSetStpDefaultPortCost = _Hh3cdot1dSetStpDefaultPortCost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 13),
    _Hh3cdot1dSetStpDefaultPortCost_Type()
)
hh3cdot1dSetStpDefaultPortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dSetStpDefaultPortCost.setStatus("current")
_Hh3cdot1dStpRootGuard_Type = EnabledStatus
_Hh3cdot1dStpRootGuard_Object = MibTableColumn
hh3cdot1dStpRootGuard = _Hh3cdot1dStpRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 14),
    _Hh3cdot1dStpRootGuard_Type()
)
hh3cdot1dStpRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpRootGuard.setStatus("current")
_Hh3cdot1dStpLoopGuard_Type = EnabledStatus
_Hh3cdot1dStpLoopGuard_Object = MibTableColumn
hh3cdot1dStpLoopGuard = _Hh3cdot1dStpLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 15),
    _Hh3cdot1dStpLoopGuard_Type()
)
hh3cdot1dStpLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpLoopGuard.setStatus("current")


class _Hh3cdot1dStpPortBlockedReason_Type(Integer32):
    """Custom type hh3cdot1dStpPortBlockedReason based on Integer32"""
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


_Hh3cdot1dStpPortBlockedReason_Type.__name__ = "Integer32"
_Hh3cdot1dStpPortBlockedReason_Object = MibTableColumn
hh3cdot1dStpPortBlockedReason = _Hh3cdot1dStpPortBlockedReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 16),
    _Hh3cdot1dStpPortBlockedReason_Type()
)
hh3cdot1dStpPortBlockedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpPortBlockedReason.setStatus("current")
_Hh3cdot1dStpRXTCBPDU_Type = Counter32
_Hh3cdot1dStpRXTCBPDU_Object = MibTableColumn
hh3cdot1dStpRXTCBPDU = _Hh3cdot1dStpRXTCBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 17),
    _Hh3cdot1dStpRXTCBPDU_Type()
)
hh3cdot1dStpRXTCBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpRXTCBPDU.setStatus("current")


class _Hh3cdot1dStpPortSendingBPDUType_Type(Integer32):
    """Custom type hh3cdot1dStpPortSendingBPDUType based on Integer32"""
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


_Hh3cdot1dStpPortSendingBPDUType_Type.__name__ = "Integer32"
_Hh3cdot1dStpPortSendingBPDUType_Object = MibTableColumn
hh3cdot1dStpPortSendingBPDUType = _Hh3cdot1dStpPortSendingBPDUType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 18),
    _Hh3cdot1dStpPortSendingBPDUType_Type()
)
hh3cdot1dStpPortSendingBPDUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpPortSendingBPDUType.setStatus("current")


class _Hh3cdot1dStpOperPortPointToPoint_Type(Integer32):
    """Custom type hh3cdot1dStpOperPortPointToPoint based on Integer32"""
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


_Hh3cdot1dStpOperPortPointToPoint_Type.__name__ = "Integer32"
_Hh3cdot1dStpOperPortPointToPoint_Object = MibTableColumn
hh3cdot1dStpOperPortPointToPoint = _Hh3cdot1dStpOperPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 5, 1, 19),
    _Hh3cdot1dStpOperPortPointToPoint_Type()
)
hh3cdot1dStpOperPortPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dStpOperPortPointToPoint.setStatus("current")
_Hh3cDot1dStpBpduGuard_Type = EnabledStatus
_Hh3cDot1dStpBpduGuard_Object = MibScalar
hh3cDot1dStpBpduGuard = _Hh3cDot1dStpBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 6),
    _Hh3cDot1dStpBpduGuard_Type()
)
hh3cDot1dStpBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot1dStpBpduGuard.setStatus("current")


class _Hh3cDot1dStpRootType_Type(Integer32):
    """Custom type hh3cDot1dStpRootType based on Integer32"""
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


_Hh3cDot1dStpRootType_Type.__name__ = "Integer32"
_Hh3cDot1dStpRootType_Object = MibScalar
hh3cDot1dStpRootType = _Hh3cDot1dStpRootType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 7),
    _Hh3cDot1dStpRootType_Type()
)
hh3cDot1dStpRootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot1dStpRootType.setStatus("current")


class _Hh3cDot1dTimeOutFactor_Type(Integer32):
    """Custom type hh3cDot1dTimeOutFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 7),
    )


_Hh3cDot1dTimeOutFactor_Type.__name__ = "Integer32"
_Hh3cDot1dTimeOutFactor_Object = MibScalar
hh3cDot1dTimeOutFactor = _Hh3cDot1dTimeOutFactor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 8),
    _Hh3cDot1dTimeOutFactor_Type()
)
hh3cDot1dTimeOutFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot1dTimeOutFactor.setStatus("current")


class _Hh3cDot1dStpPathCostStandard_Type(Integer32):
    """Custom type hh3cDot1dStpPathCostStandard based on Integer32"""
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


_Hh3cDot1dStpPathCostStandard_Type.__name__ = "Integer32"
_Hh3cDot1dStpPathCostStandard_Object = MibScalar
hh3cDot1dStpPathCostStandard = _Hh3cDot1dStpPathCostStandard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 9),
    _Hh3cDot1dStpPathCostStandard_Type()
)
hh3cDot1dStpPathCostStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot1dStpPathCostStandard.setStatus("current")
_Hh3cdot1dStpIgnoredVlanTable_Object = MibTable
hh3cdot1dStpIgnoredVlanTable = _Hh3cdot1dStpIgnoredVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cdot1dStpIgnoredVlanTable.setStatus("current")
_Hh3cdot1dStpIgnoredVlanEntry_Object = MibTableRow
hh3cdot1dStpIgnoredVlanEntry = _Hh3cdot1dStpIgnoredVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 10, 1)
)
hh3cdot1dStpIgnoredVlanEntry.setIndexNames(
    (0, "HH3C-LswRSTP-MIB", "hh3cdot1dVlan"),
)
if mibBuilder.loadTexts:
    hh3cdot1dStpIgnoredVlanEntry.setStatus("current")


class _Hh3cdot1dVlan_Type(Integer32):
    """Custom type hh3cdot1dVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cdot1dVlan_Type.__name__ = "Integer32"
_Hh3cdot1dVlan_Object = MibTableColumn
hh3cdot1dVlan = _Hh3cdot1dVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 10, 1, 1),
    _Hh3cdot1dVlan_Type()
)
hh3cdot1dVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1dVlan.setStatus("current")


class _Hh3cdot1dStpIgnore_Type(Integer32):
    """Custom type hh3cdot1dStpIgnore based on Integer32"""
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


_Hh3cdot1dStpIgnore_Type.__name__ = "Integer32"
_Hh3cdot1dStpIgnore_Object = MibTableColumn
hh3cdot1dStpIgnore = _Hh3cdot1dStpIgnore_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 10, 1, 2),
    _Hh3cdot1dStpIgnore_Type()
)
hh3cdot1dStpIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1dStpIgnore.setStatus("current")
dot1dStpPortEntry.registerAugmentions(
    ("HH3C-LswRSTP-MIB",
     "hh3cdot1dStpPortXEntry")
)
hh3cdot1dStpPortXEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hh3cRstpBpduGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 0, 1)
)
hh3cRstpBpduGuarded.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    hh3cRstpBpduGuarded.setStatus(
        "current"
    )

hh3cRstpRootGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 0, 2)
)
hh3cRstpRootGuarded.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    hh3cRstpRootGuarded.setStatus(
        "current"
    )

hh3cRstpBridgeLostRootPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 0, 3)
)
if mibBuilder.loadTexts:
    hh3cRstpBridgeLostRootPrimary.setStatus(
        "current"
    )

hh3cRstpLoopGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 6, 1, 0, 4)
)
hh3cRstpLoopGuarded.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    hh3cRstpLoopGuarded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswRSTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hh3cLswRstpMib": hh3cLswRstpMib,
       "hh3cLswRstpMibObject": hh3cLswRstpMibObject,
       "hh3cRstpEventsV2": hh3cRstpEventsV2,
       "hh3cRstpBpduGuarded": hh3cRstpBpduGuarded,
       "hh3cRstpRootGuarded": hh3cRstpRootGuarded,
       "hh3cRstpBridgeLostRootPrimary": hh3cRstpBridgeLostRootPrimary,
       "hh3cRstpLoopGuarded": hh3cRstpLoopGuarded,
       "hh3cdot1dStpStatus": hh3cdot1dStpStatus,
       "hh3cdot1dStpForceVersion": hh3cdot1dStpForceVersion,
       "hh3cdot1dStpDiameter": hh3cdot1dStpDiameter,
       "hh3cdot1dStpRootBridgeAddress": hh3cdot1dStpRootBridgeAddress,
       "hh3cdot1dStpPortXTable": hh3cdot1dStpPortXTable,
       "hh3cdot1dStpPortXEntry": hh3cdot1dStpPortXEntry,
       "hh3cdot1dStpPortStatus": hh3cdot1dStpPortStatus,
       "hh3cdot1dStpPortEdgeport": hh3cdot1dStpPortEdgeport,
       "hh3cdot1dStpPortPointToPoint": hh3cdot1dStpPortPointToPoint,
       "hh3cdot1dStpMcheck": hh3cdot1dStpMcheck,
       "hh3cdot1dStpTransLimit": hh3cdot1dStpTransLimit,
       "hh3cdot1dStpRXStpBPDU": hh3cdot1dStpRXStpBPDU,
       "hh3cdot1dStpTXStpBPDU": hh3cdot1dStpTXStpBPDU,
       "hh3cdot1dStpRXTCNBPDU": hh3cdot1dStpRXTCNBPDU,
       "hh3cdot1dStpTXTCNBPDU": hh3cdot1dStpTXTCNBPDU,
       "hh3cdot1dStpRXRSTPBPDU": hh3cdot1dStpRXRSTPBPDU,
       "hh3cdot1dStpTXRSTPBPDU": hh3cdot1dStpTXRSTPBPDU,
       "hh3cdot1dStpClearStatistics": hh3cdot1dStpClearStatistics,
       "hh3cdot1dSetStpDefaultPortCost": hh3cdot1dSetStpDefaultPortCost,
       "hh3cdot1dStpRootGuard": hh3cdot1dStpRootGuard,
       "hh3cdot1dStpLoopGuard": hh3cdot1dStpLoopGuard,
       "hh3cdot1dStpPortBlockedReason": hh3cdot1dStpPortBlockedReason,
       "hh3cdot1dStpRXTCBPDU": hh3cdot1dStpRXTCBPDU,
       "hh3cdot1dStpPortSendingBPDUType": hh3cdot1dStpPortSendingBPDUType,
       "hh3cdot1dStpOperPortPointToPoint": hh3cdot1dStpOperPortPointToPoint,
       "hh3cDot1dStpBpduGuard": hh3cDot1dStpBpduGuard,
       "hh3cDot1dStpRootType": hh3cDot1dStpRootType,
       "hh3cDot1dTimeOutFactor": hh3cDot1dTimeOutFactor,
       "hh3cDot1dStpPathCostStandard": hh3cDot1dStpPathCostStandard,
       "hh3cdot1dStpIgnoredVlanTable": hh3cdot1dStpIgnoredVlanTable,
       "hh3cdot1dStpIgnoredVlanEntry": hh3cdot1dStpIgnoredVlanEntry,
       "hh3cdot1dVlan": hh3cdot1dVlan,
       "hh3cdot1dStpIgnore": hh3cdot1dStpIgnore}
)
