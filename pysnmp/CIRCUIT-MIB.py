# SNMP MIB module (CIRCUIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIRCUIT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:17 2024
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

(circuit,
 coriolisMibs) = mibBuilder.importSymbols(
    "CORIOLIS-MIB",
    "circuit",
    "coriolisMibs")

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
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

circuitMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _CircuitLoadBalanceInterval_Type(Integer32):
    """Custom type circuitLoadBalanceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CircuitLoadBalanceInterval_Type.__name__ = "Integer32"
_CircuitLoadBalanceInterval_Object = MibScalar
circuitLoadBalanceInterval = _CircuitLoadBalanceInterval_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 2),
    _CircuitLoadBalanceInterval_Type()
)
circuitLoadBalanceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitLoadBalanceInterval.setStatus("current")


class _CircuitLoadBalanceNumPerInterval_Type(Integer32):
    """Custom type circuitLoadBalanceNumPerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CircuitLoadBalanceNumPerInterval_Type.__name__ = "Integer32"
_CircuitLoadBalanceNumPerInterval_Object = MibScalar
circuitLoadBalanceNumPerInterval = _CircuitLoadBalanceNumPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 3),
    _CircuitLoadBalanceNumPerInterval_Type()
)
circuitLoadBalanceNumPerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitLoadBalanceNumPerInterval.setStatus("current")
_CircuitOldIpAddrToSwap_Type = IpAddress
_CircuitOldIpAddrToSwap_Object = MibScalar
circuitOldIpAddrToSwap = _CircuitOldIpAddrToSwap_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 4),
    _CircuitOldIpAddrToSwap_Type()
)
circuitOldIpAddrToSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitOldIpAddrToSwap.setStatus("current")
_CircuitNewIpAddrToSwap_Type = IpAddress
_CircuitNewIpAddrToSwap_Object = MibScalar
circuitNewIpAddrToSwap = _CircuitNewIpAddrToSwap_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 5),
    _CircuitNewIpAddrToSwap_Type()
)
circuitNewIpAddrToSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitNewIpAddrToSwap.setStatus("current")
_CircuitEventInterval_Type = Unsigned32
_CircuitEventInterval_Object = MibScalar
circuitEventInterval = _CircuitEventInterval_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 6),
    _CircuitEventInterval_Type()
)
circuitEventInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitEventInterval.setStatus("current")


class _CircuitEventNumPerInterval_Type(Integer32):
    """Custom type circuitEventNumPerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CircuitEventNumPerInterval_Type.__name__ = "Integer32"
_CircuitEventNumPerInterval_Object = MibScalar
circuitEventNumPerInterval = _CircuitEventNumPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 7),
    _CircuitEventNumPerInterval_Type()
)
circuitEventNumPerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitEventNumPerInterval.setStatus("current")
_CircuitTable_Object = MibTable
circuitTable = _CircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8)
)
if mibBuilder.loadTexts:
    circuitTable.setStatus("current")
_CircuitEntry_Object = MibTableRow
circuitEntry = _CircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1)
)
circuitEntry.setIndexNames(
    (0, "CIRCUIT-MIB", "circuitSrcIpAddr"),
    (0, "CIRCUIT-MIB", "circuitSrcInterfaceNum"),
    (0, "CIRCUIT-MIB", "circuitSrcConnectionID"),
)
if mibBuilder.loadTexts:
    circuitEntry.setStatus("current")
_CircuitSrcIpAddr_Type = IpAddress
_CircuitSrcIpAddr_Object = MibTableColumn
circuitSrcIpAddr = _CircuitSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 1),
    _CircuitSrcIpAddr_Type()
)
circuitSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSrcIpAddr.setStatus("current")
_CircuitSrcInterfaceNum_Type = Unsigned32
_CircuitSrcInterfaceNum_Object = MibTableColumn
circuitSrcInterfaceNum = _CircuitSrcInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 2),
    _CircuitSrcInterfaceNum_Type()
)
circuitSrcInterfaceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSrcInterfaceNum.setStatus("current")
_CircuitSrcConnectionID_Type = Unsigned32
_CircuitSrcConnectionID_Object = MibTableColumn
circuitSrcConnectionID = _CircuitSrcConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 3),
    _CircuitSrcConnectionID_Type()
)
circuitSrcConnectionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitSrcConnectionID.setStatus("current")
_CircuitSrcDescString_Type = OctetString
_CircuitSrcDescString_Object = MibTableColumn
circuitSrcDescString = _CircuitSrcDescString_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 4),
    _CircuitSrcDescString_Type()
)
circuitSrcDescString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitSrcDescString.setStatus("current")
_CircuitDestIpAddr_Type = IpAddress
_CircuitDestIpAddr_Object = MibTableColumn
circuitDestIpAddr = _CircuitDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 5),
    _CircuitDestIpAddr_Type()
)
circuitDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitDestIpAddr.setStatus("current")
_CircuitDestInterfaceNum_Type = Unsigned32
_CircuitDestInterfaceNum_Object = MibTableColumn
circuitDestInterfaceNum = _CircuitDestInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 6),
    _CircuitDestInterfaceNum_Type()
)
circuitDestInterfaceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitDestInterfaceNum.setStatus("current")
_CircuitDestConnectionID_Type = Unsigned32
_CircuitDestConnectionID_Object = MibTableColumn
circuitDestConnectionID = _CircuitDestConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 7),
    _CircuitDestConnectionID_Type()
)
circuitDestConnectionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitDestConnectionID.setStatus("current")
_CircuitDestDescString_Type = OctetString
_CircuitDestDescString_Object = MibTableColumn
circuitDestDescString = _CircuitDestDescString_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 8),
    _CircuitDestDescString_Type()
)
circuitDestDescString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitDestDescString.setStatus("current")


class _CircuitName_Type(OctetString):
    """Custom type circuitName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CircuitName_Type.__name__ = "OctetString"
_CircuitName_Object = MibTableColumn
circuitName = _CircuitName_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 9),
    _CircuitName_Type()
)
circuitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitName.setStatus("current")
_CircuitID_Type = Unsigned32
_CircuitID_Object = MibTableColumn
circuitID = _CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 10),
    _CircuitID_Type()
)
circuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitID.setStatus("current")


class _CircuitRowStatus_Type(Integer32):
    """Custom type circuitRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_CircuitRowStatus_Type.__name__ = "Integer32"
_CircuitRowStatus_Object = MibTableColumn
circuitRowStatus = _CircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 11),
    _CircuitRowStatus_Type()
)
circuitRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitRowStatus.setStatus("current")
_CircuitReasonText_Type = DisplayString
_CircuitReasonText_Object = MibTableColumn
circuitReasonText = _CircuitReasonText_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 12),
    _CircuitReasonText_Type()
)
circuitReasonText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitReasonText.setStatus("current")
_CircuitFailLocIpAddr_Type = IpAddress
_CircuitFailLocIpAddr_Object = MibTableColumn
circuitFailLocIpAddr = _CircuitFailLocIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 13),
    _CircuitFailLocIpAddr_Type()
)
circuitFailLocIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitFailLocIpAddr.setStatus("current")


class _CircuitFailLocSlot1_Type(Integer32):
    """Custom type circuitFailLocSlot1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_CircuitFailLocSlot1_Type.__name__ = "Integer32"
_CircuitFailLocSlot1_Object = MibTableColumn
circuitFailLocSlot1 = _CircuitFailLocSlot1_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 14),
    _CircuitFailLocSlot1_Type()
)
circuitFailLocSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitFailLocSlot1.setStatus("current")


class _CircuitFailLocPort1_Type(Integer32):
    """Custom type circuitFailLocPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CircuitFailLocPort1_Type.__name__ = "Integer32"
_CircuitFailLocPort1_Object = MibTableColumn
circuitFailLocPort1 = _CircuitFailLocPort1_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 15),
    _CircuitFailLocPort1_Type()
)
circuitFailLocPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitFailLocPort1.setStatus("current")
_CircuitFailLocInterfaceNum1_Type = Unsigned32
_CircuitFailLocInterfaceNum1_Object = MibTableColumn
circuitFailLocInterfaceNum1 = _CircuitFailLocInterfaceNum1_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 16),
    _CircuitFailLocInterfaceNum1_Type()
)
circuitFailLocInterfaceNum1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitFailLocInterfaceNum1.setStatus("current")
_CircuitFailLocConnectionID1_Type = Unsigned32
_CircuitFailLocConnectionID1_Object = MibTableColumn
circuitFailLocConnectionID1 = _CircuitFailLocConnectionID1_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 17),
    _CircuitFailLocConnectionID1_Type()
)
circuitFailLocConnectionID1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitFailLocConnectionID1.setStatus("current")


class _CircuitFailLocSlot2_Type(Integer32):
    """Custom type circuitFailLocSlot2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_CircuitFailLocSlot2_Type.__name__ = "Integer32"
_CircuitFailLocSlot2_Object = MibTableColumn
circuitFailLocSlot2 = _CircuitFailLocSlot2_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 18),
    _CircuitFailLocSlot2_Type()
)
circuitFailLocSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitFailLocSlot2.setStatus("current")


class _CircuitFailLocPort2_Type(Integer32):
    """Custom type circuitFailLocPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CircuitFailLocPort2_Type.__name__ = "Integer32"
_CircuitFailLocPort2_Object = MibTableColumn
circuitFailLocPort2 = _CircuitFailLocPort2_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 19),
    _CircuitFailLocPort2_Type()
)
circuitFailLocPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitFailLocPort2.setStatus("current")
_CircuitFailLocInterfaceNum2_Type = Unsigned32
_CircuitFailLocInterfaceNum2_Object = MibTableColumn
circuitFailLocInterfaceNum2 = _CircuitFailLocInterfaceNum2_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 20),
    _CircuitFailLocInterfaceNum2_Type()
)
circuitFailLocInterfaceNum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitFailLocInterfaceNum2.setStatus("current")
_CircuitFailLocConnectionID2_Type = Unsigned32
_CircuitFailLocConnectionID2_Object = MibTableColumn
circuitFailLocConnectionID2 = _CircuitFailLocConnectionID2_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 21),
    _CircuitFailLocConnectionID2_Type()
)
circuitFailLocConnectionID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitFailLocConnectionID2.setStatus("current")


class _CircuitEndPoint1Protocol_Type(Integer32):
    """Custom type circuitEndPoint1Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atm", 3),
          ("axData", 5),
          ("axTdm", 6),
          ("ethernet", 1),
          ("frameRelay", 2),
          ("isl", 7),
          ("vt", 4))
    )


_CircuitEndPoint1Protocol_Type.__name__ = "Integer32"
_CircuitEndPoint1Protocol_Object = MibTableColumn
circuitEndPoint1Protocol = _CircuitEndPoint1Protocol_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 22),
    _CircuitEndPoint1Protocol_Type()
)
circuitEndPoint1Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitEndPoint1Protocol.setStatus("current")


class _CircuitFwdTDType_Type(Integer32):
    """Custom type circuitFwdTDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atm-cbr", 4),
          ("atm-vbr-nrt", 6),
          ("atm-vbr-rt", 5),
          ("atm-vbr-ubr", 7),
          ("ethernet", 1),
          ("frameRelay", 2),
          ("tdm", 3))
    )


_CircuitFwdTDType_Type.__name__ = "Integer32"
_CircuitFwdTDType_Object = MibTableColumn
circuitFwdTDType = _CircuitFwdTDType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 23),
    _CircuitFwdTDType_Type()
)
circuitFwdTDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitFwdTDType.setStatus("current")
_CircuitFwdTDParam1_Type = Unsigned32
_CircuitFwdTDParam1_Object = MibTableColumn
circuitFwdTDParam1 = _CircuitFwdTDParam1_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 24),
    _CircuitFwdTDParam1_Type()
)
circuitFwdTDParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitFwdTDParam1.setStatus("current")
_CircuitFwdTDParam2_Type = Unsigned32
_CircuitFwdTDParam2_Object = MibTableColumn
circuitFwdTDParam2 = _CircuitFwdTDParam2_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 25),
    _CircuitFwdTDParam2_Type()
)
circuitFwdTDParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitFwdTDParam2.setStatus("current")
_CircuitFwdTDParam3_Type = Unsigned32
_CircuitFwdTDParam3_Object = MibTableColumn
circuitFwdTDParam3 = _CircuitFwdTDParam3_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 26),
    _CircuitFwdTDParam3_Type()
)
circuitFwdTDParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitFwdTDParam3.setStatus("current")
_CircuitFwdTDParam4_Type = Unsigned32
_CircuitFwdTDParam4_Object = MibTableColumn
circuitFwdTDParam4 = _CircuitFwdTDParam4_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 27),
    _CircuitFwdTDParam4_Type()
)
circuitFwdTDParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitFwdTDParam4.setStatus("current")


class _CircuitEndPoint2Protocol_Type(Integer32):
    """Custom type circuitEndPoint2Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atm", 3),
          ("axData", 5),
          ("axTdm", 6),
          ("ethernet", 1),
          ("frameRelay", 2),
          ("isl", 7),
          ("vt", 4))
    )


_CircuitEndPoint2Protocol_Type.__name__ = "Integer32"
_CircuitEndPoint2Protocol_Object = MibTableColumn
circuitEndPoint2Protocol = _CircuitEndPoint2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 28),
    _CircuitEndPoint2Protocol_Type()
)
circuitEndPoint2Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitEndPoint2Protocol.setStatus("current")


class _CircuitBwdTDType_Type(Integer32):
    """Custom type circuitBwdTDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atm-cbr", 4),
          ("atm-vbr-nrt", 6),
          ("atm-vbr-rt", 5),
          ("atm-vbr-ubr", 7),
          ("ethernet", 1),
          ("frameRelay", 2),
          ("tdm", 3))
    )


_CircuitBwdTDType_Type.__name__ = "Integer32"
_CircuitBwdTDType_Object = MibTableColumn
circuitBwdTDType = _CircuitBwdTDType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 29),
    _CircuitBwdTDType_Type()
)
circuitBwdTDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitBwdTDType.setStatus("current")
_CircuitBwdTDParam1_Type = Unsigned32
_CircuitBwdTDParam1_Object = MibTableColumn
circuitBwdTDParam1 = _CircuitBwdTDParam1_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 30),
    _CircuitBwdTDParam1_Type()
)
circuitBwdTDParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitBwdTDParam1.setStatus("current")
_CircuitBwdTDParam2_Type = Unsigned32
_CircuitBwdTDParam2_Object = MibTableColumn
circuitBwdTDParam2 = _CircuitBwdTDParam2_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 31),
    _CircuitBwdTDParam2_Type()
)
circuitBwdTDParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitBwdTDParam2.setStatus("current")
_CircuitBwdTDParam3_Type = Unsigned32
_CircuitBwdTDParam3_Object = MibTableColumn
circuitBwdTDParam3 = _CircuitBwdTDParam3_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 32),
    _CircuitBwdTDParam3_Type()
)
circuitBwdTDParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitBwdTDParam3.setStatus("current")
_CircuitBwdTDParam4_Type = Unsigned32
_CircuitBwdTDParam4_Object = MibTableColumn
circuitBwdTDParam4 = _CircuitBwdTDParam4_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 33),
    _CircuitBwdTDParam4_Type()
)
circuitBwdTDParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitBwdTDParam4.setStatus("current")


class _CircuitClassOfService_Type(Integer32):
    """Custom type circuitClassOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CircuitClassOfService_Type.__name__ = "Integer32"
_CircuitClassOfService_Object = MibTableColumn
circuitClassOfService = _CircuitClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 34),
    _CircuitClassOfService_Type()
)
circuitClassOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitClassOfService.setStatus("current")


class _CircuitAdminState_Type(Integer32):
    """Custom type circuitAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledButNotUsed", 3))
    )


_CircuitAdminState_Type.__name__ = "Integer32"
_CircuitAdminState_Object = MibTableColumn
circuitAdminState = _CircuitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 35),
    _CircuitAdminState_Type()
)
circuitAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitAdminState.setStatus("current")


class _CircuitOperState_Type(Integer32):
    """Custom type circuitOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("test", 3),
          ("up", 1))
    )


_CircuitOperState_Type.__name__ = "Integer32"
_CircuitOperState_Object = MibTableColumn
circuitOperState = _CircuitOperState_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 36),
    _CircuitOperState_Type()
)
circuitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitOperState.setStatus("current")
_CircuitTimeSinceStatusChange_Type = Unsigned32
_CircuitTimeSinceStatusChange_Object = MibTableColumn
circuitTimeSinceStatusChange = _CircuitTimeSinceStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 37),
    _CircuitTimeSinceStatusChange_Type()
)
circuitTimeSinceStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTimeSinceStatusChange.setStatus("current")
_CircuitSetupPriority_Type = Unsigned32
_CircuitSetupPriority_Object = MibTableColumn
circuitSetupPriority = _CircuitSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 38),
    _CircuitSetupPriority_Type()
)
circuitSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitSetupPriority.setStatus("current")
_CircuitHoldPriority_Type = Unsigned32
_CircuitHoldPriority_Object = MibTableColumn
circuitHoldPriority = _CircuitHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 39),
    _CircuitHoldPriority_Type()
)
circuitHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitHoldPriority.setStatus("current")
_CircuitIsRedundancyReqd_Type = TruthValue
_CircuitIsRedundancyReqd_Object = MibTableColumn
circuitIsRedundancyReqd = _CircuitIsRedundancyReqd_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 40),
    _CircuitIsRedundancyReqd_Type()
)
circuitIsRedundancyReqd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitIsRedundancyReqd.setStatus("current")


class _CircuitPreferredEP1OptSlot_Type(Integer32):
    """Custom type circuitPreferredEP1OptSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_CircuitPreferredEP1OptSlot_Type.__name__ = "Integer32"
_CircuitPreferredEP1OptSlot_Object = MibTableColumn
circuitPreferredEP1OptSlot = _CircuitPreferredEP1OptSlot_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 41),
    _CircuitPreferredEP1OptSlot_Type()
)
circuitPreferredEP1OptSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPreferredEP1OptSlot.setStatus("current")


class _CircuitPreferredEP1OptPort_Type(Integer32):
    """Custom type circuitPreferredEP1OptPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CircuitPreferredEP1OptPort_Type.__name__ = "Integer32"
_CircuitPreferredEP1OptPort_Object = MibTableColumn
circuitPreferredEP1OptPort = _CircuitPreferredEP1OptPort_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 42),
    _CircuitPreferredEP1OptPort_Type()
)
circuitPreferredEP1OptPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPreferredEP1OptPort.setStatus("current")
_CircuitPreferredEP1OptVport_Type = Integer32
_CircuitPreferredEP1OptVport_Object = MibTableColumn
circuitPreferredEP1OptVport = _CircuitPreferredEP1OptVport_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 43),
    _CircuitPreferredEP1OptVport_Type()
)
circuitPreferredEP1OptVport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPreferredEP1OptVport.setStatus("current")


class _CircuitPreferredEP2OptSlot_Type(Integer32):
    """Custom type circuitPreferredEP2OptSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_CircuitPreferredEP2OptSlot_Type.__name__ = "Integer32"
_CircuitPreferredEP2OptSlot_Object = MibTableColumn
circuitPreferredEP2OptSlot = _CircuitPreferredEP2OptSlot_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 44),
    _CircuitPreferredEP2OptSlot_Type()
)
circuitPreferredEP2OptSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPreferredEP2OptSlot.setStatus("current")


class _CircuitPreferredEP2OptPort_Type(Integer32):
    """Custom type circuitPreferredEP2OptPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CircuitPreferredEP2OptPort_Type.__name__ = "Integer32"
_CircuitPreferredEP2OptPort_Object = MibTableColumn
circuitPreferredEP2OptPort = _CircuitPreferredEP2OptPort_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 45),
    _CircuitPreferredEP2OptPort_Type()
)
circuitPreferredEP2OptPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPreferredEP2OptPort.setStatus("current")
_CircuitPreferredEP2OptVport_Type = Integer32
_CircuitPreferredEP2OptVport_Object = MibTableColumn
circuitPreferredEP2OptVport = _CircuitPreferredEP2OptVport_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 46),
    _CircuitPreferredEP2OptVport_Type()
)
circuitPreferredEP2OptVport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitPreferredEP2OptVport.setStatus("current")


class _CircuitUseAlternateRing_Type(Integer32):
    """Custom type circuitUseAlternateRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CircuitUseAlternateRing_Type.__name__ = "Integer32"
_CircuitUseAlternateRing_Object = MibTableColumn
circuitUseAlternateRing = _CircuitUseAlternateRing_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 47),
    _CircuitUseAlternateRing_Type()
)
circuitUseAlternateRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    circuitUseAlternateRing.setStatus("current")
_CircuitInFrames_Type = Counter64
_CircuitInFrames_Object = MibTableColumn
circuitInFrames = _CircuitInFrames_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 48),
    _CircuitInFrames_Type()
)
circuitInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInFrames.setStatus("current")
_CircuitInDEFrames_Type = Counter64
_CircuitInDEFrames_Object = MibTableColumn
circuitInDEFrames = _CircuitInDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 49),
    _CircuitInDEFrames_Type()
)
circuitInDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInDEFrames.setStatus("current")
_CircuitInOctets_Type = Counter64
_CircuitInOctets_Object = MibTableColumn
circuitInOctets = _CircuitInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 50),
    _CircuitInOctets_Type()
)
circuitInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInOctets.setStatus("current")
_CircuitInDEOctets_Type = Counter64
_CircuitInDEOctets_Object = MibTableColumn
circuitInDEOctets = _CircuitInDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 51),
    _CircuitInDEOctets_Type()
)
circuitInDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInDEOctets.setStatus("current")
_CircuitInCLP0Cells_Type = Counter64
_CircuitInCLP0Cells_Object = MibTableColumn
circuitInCLP0Cells = _CircuitInCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 52),
    _CircuitInCLP0Cells_Type()
)
circuitInCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInCLP0Cells.setStatus("current")
_CircuitInCLP1Cells_Type = Counter64
_CircuitInCLP1Cells_Object = MibTableColumn
circuitInCLP1Cells = _CircuitInCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 53),
    _CircuitInCLP1Cells_Type()
)
circuitInCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInCLP1Cells.setStatus("current")
_CircuitInFramesDiscard_Type = Counter64
_CircuitInFramesDiscard_Object = MibTableColumn
circuitInFramesDiscard = _CircuitInFramesDiscard_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 54),
    _CircuitInFramesDiscard_Type()
)
circuitInFramesDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInFramesDiscard.setStatus("current")
_CircuitInDEFramesDiscard_Type = Counter64
_CircuitInDEFramesDiscard_Object = MibTableColumn
circuitInDEFramesDiscard = _CircuitInDEFramesDiscard_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 55),
    _CircuitInDEFramesDiscard_Type()
)
circuitInDEFramesDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInDEFramesDiscard.setStatus("current")
_CircuitInOctetsDiscard_Type = Counter64
_CircuitInOctetsDiscard_Object = MibTableColumn
circuitInOctetsDiscard = _CircuitInOctetsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 56),
    _CircuitInOctetsDiscard_Type()
)
circuitInOctetsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInOctetsDiscard.setStatus("current")
_CircuitInDEOctetsDiscard_Type = Counter64
_CircuitInDEOctetsDiscard_Object = MibTableColumn
circuitInDEOctetsDiscard = _CircuitInDEOctetsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 57),
    _CircuitInDEOctetsDiscard_Type()
)
circuitInDEOctetsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInDEOctetsDiscard.setStatus("current")
_CircuitInCLP0CellsDiscard_Type = Counter64
_CircuitInCLP0CellsDiscard_Object = MibTableColumn
circuitInCLP0CellsDiscard = _CircuitInCLP0CellsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 58),
    _CircuitInCLP0CellsDiscard_Type()
)
circuitInCLP0CellsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInCLP0CellsDiscard.setStatus("current")
_CircuitInCLP1CellsDiscard_Type = Counter64
_CircuitInCLP1CellsDiscard_Object = MibTableColumn
circuitInCLP1CellsDiscard = _CircuitInCLP1CellsDiscard_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 59),
    _CircuitInCLP1CellsDiscard_Type()
)
circuitInCLP1CellsDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInCLP1CellsDiscard.setStatus("current")
_CircuitInFramesTagged_Type = Counter64
_CircuitInFramesTagged_Object = MibTableColumn
circuitInFramesTagged = _CircuitInFramesTagged_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 60),
    _CircuitInFramesTagged_Type()
)
circuitInFramesTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInFramesTagged.setStatus("current")
_CircuitInOctetsTagged_Type = Counter64
_CircuitInOctetsTagged_Object = MibTableColumn
circuitInOctetsTagged = _CircuitInOctetsTagged_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 61),
    _CircuitInOctetsTagged_Type()
)
circuitInOctetsTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInOctetsTagged.setStatus("current")
_CircuitInCLP0CellsTagged_Type = Counter64
_CircuitInCLP0CellsTagged_Object = MibTableColumn
circuitInCLP0CellsTagged = _CircuitInCLP0CellsTagged_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 62),
    _CircuitInCLP0CellsTagged_Type()
)
circuitInCLP0CellsTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitInCLP0CellsTagged.setStatus("current")
_CircuitOutFrames_Type = Counter64
_CircuitOutFrames_Object = MibTableColumn
circuitOutFrames = _CircuitOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 63),
    _CircuitOutFrames_Type()
)
circuitOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitOutFrames.setStatus("current")
_CircuitOutDEFrames_Type = Counter64
_CircuitOutDEFrames_Object = MibTableColumn
circuitOutDEFrames = _CircuitOutDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 64),
    _CircuitOutDEFrames_Type()
)
circuitOutDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitOutDEFrames.setStatus("current")
_CircuitOutOctets_Type = Counter64
_CircuitOutOctets_Object = MibTableColumn
circuitOutOctets = _CircuitOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 65),
    _CircuitOutOctets_Type()
)
circuitOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitOutOctets.setStatus("current")
_CircuitOutDEOctets_Type = Counter64
_CircuitOutDEOctets_Object = MibTableColumn
circuitOutDEOctets = _CircuitOutDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 66),
    _CircuitOutDEOctets_Type()
)
circuitOutDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitOutDEOctets.setStatus("current")
_CircuitOutCLP0Cells_Type = Counter64
_CircuitOutCLP0Cells_Object = MibTableColumn
circuitOutCLP0Cells = _CircuitOutCLP0Cells_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 67),
    _CircuitOutCLP0Cells_Type()
)
circuitOutCLP0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitOutCLP0Cells.setStatus("current")
_CircuitOutCLP1Cells_Type = Counter64
_CircuitOutCLP1Cells_Object = MibTableColumn
circuitOutCLP1Cells = _CircuitOutCLP1Cells_Object(
    (1, 3, 6, 1, 4, 1, 5812, 6, 8, 1, 68),
    _CircuitOutCLP1Cells_Type()
)
circuitOutCLP1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitOutCLP1Cells.setStatus("current")

# Managed Objects groups


# Notification objects

circuitInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 24)
)
circuitInactive.setObjects(
    ("CIRCUIT-MIB", "circuitReasonText")
)
if mibBuilder.loadTexts:
    circuitInactive.setStatus(
        ""
    )

circuitActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 25)
)
circuitActive.setObjects(
    ("CIRCUIT-MIB", "circuitReasonText")
)
if mibBuilder.loadTexts:
    circuitActive.setStatus(
        ""
    )

circuitLoadBalancing = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 26)
)
circuitLoadBalancing.setObjects(
    ("CIRCUIT-MIB", "circuitReasonText")
)
if mibBuilder.loadTexts:
    circuitLoadBalancing.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIRCUIT-MIB",
    **{"circuitInactive": circuitInactive,
       "circuitActive": circuitActive,
       "circuitLoadBalancing": circuitLoadBalancing,
       "circuitMIB": circuitMIB,
       "circuitLoadBalanceInterval": circuitLoadBalanceInterval,
       "circuitLoadBalanceNumPerInterval": circuitLoadBalanceNumPerInterval,
       "circuitOldIpAddrToSwap": circuitOldIpAddrToSwap,
       "circuitNewIpAddrToSwap": circuitNewIpAddrToSwap,
       "circuitEventInterval": circuitEventInterval,
       "circuitEventNumPerInterval": circuitEventNumPerInterval,
       "circuitTable": circuitTable,
       "circuitEntry": circuitEntry,
       "circuitSrcIpAddr": circuitSrcIpAddr,
       "circuitSrcInterfaceNum": circuitSrcInterfaceNum,
       "circuitSrcConnectionID": circuitSrcConnectionID,
       "circuitSrcDescString": circuitSrcDescString,
       "circuitDestIpAddr": circuitDestIpAddr,
       "circuitDestInterfaceNum": circuitDestInterfaceNum,
       "circuitDestConnectionID": circuitDestConnectionID,
       "circuitDestDescString": circuitDestDescString,
       "circuitName": circuitName,
       "circuitID": circuitID,
       "circuitRowStatus": circuitRowStatus,
       "circuitReasonText": circuitReasonText,
       "circuitFailLocIpAddr": circuitFailLocIpAddr,
       "circuitFailLocSlot1": circuitFailLocSlot1,
       "circuitFailLocPort1": circuitFailLocPort1,
       "circuitFailLocInterfaceNum1": circuitFailLocInterfaceNum1,
       "circuitFailLocConnectionID1": circuitFailLocConnectionID1,
       "circuitFailLocSlot2": circuitFailLocSlot2,
       "circuitFailLocPort2": circuitFailLocPort2,
       "circuitFailLocInterfaceNum2": circuitFailLocInterfaceNum2,
       "circuitFailLocConnectionID2": circuitFailLocConnectionID2,
       "circuitEndPoint1Protocol": circuitEndPoint1Protocol,
       "circuitFwdTDType": circuitFwdTDType,
       "circuitFwdTDParam1": circuitFwdTDParam1,
       "circuitFwdTDParam2": circuitFwdTDParam2,
       "circuitFwdTDParam3": circuitFwdTDParam3,
       "circuitFwdTDParam4": circuitFwdTDParam4,
       "circuitEndPoint2Protocol": circuitEndPoint2Protocol,
       "circuitBwdTDType": circuitBwdTDType,
       "circuitBwdTDParam1": circuitBwdTDParam1,
       "circuitBwdTDParam2": circuitBwdTDParam2,
       "circuitBwdTDParam3": circuitBwdTDParam3,
       "circuitBwdTDParam4": circuitBwdTDParam4,
       "circuitClassOfService": circuitClassOfService,
       "circuitAdminState": circuitAdminState,
       "circuitOperState": circuitOperState,
       "circuitTimeSinceStatusChange": circuitTimeSinceStatusChange,
       "circuitSetupPriority": circuitSetupPriority,
       "circuitHoldPriority": circuitHoldPriority,
       "circuitIsRedundancyReqd": circuitIsRedundancyReqd,
       "circuitPreferredEP1OptSlot": circuitPreferredEP1OptSlot,
       "circuitPreferredEP1OptPort": circuitPreferredEP1OptPort,
       "circuitPreferredEP1OptVport": circuitPreferredEP1OptVport,
       "circuitPreferredEP2OptSlot": circuitPreferredEP2OptSlot,
       "circuitPreferredEP2OptPort": circuitPreferredEP2OptPort,
       "circuitPreferredEP2OptVport": circuitPreferredEP2OptVport,
       "circuitUseAlternateRing": circuitUseAlternateRing,
       "circuitInFrames": circuitInFrames,
       "circuitInDEFrames": circuitInDEFrames,
       "circuitInOctets": circuitInOctets,
       "circuitInDEOctets": circuitInDEOctets,
       "circuitInCLP0Cells": circuitInCLP0Cells,
       "circuitInCLP1Cells": circuitInCLP1Cells,
       "circuitInFramesDiscard": circuitInFramesDiscard,
       "circuitInDEFramesDiscard": circuitInDEFramesDiscard,
       "circuitInOctetsDiscard": circuitInOctetsDiscard,
       "circuitInDEOctetsDiscard": circuitInDEOctetsDiscard,
       "circuitInCLP0CellsDiscard": circuitInCLP0CellsDiscard,
       "circuitInCLP1CellsDiscard": circuitInCLP1CellsDiscard,
       "circuitInFramesTagged": circuitInFramesTagged,
       "circuitInOctetsTagged": circuitInOctetsTagged,
       "circuitInCLP0CellsTagged": circuitInCLP0CellsTagged,
       "circuitOutFrames": circuitOutFrames,
       "circuitOutDEFrames": circuitOutDEFrames,
       "circuitOutOctets": circuitOutOctets,
       "circuitOutDEOctets": circuitOutDEOctets,
       "circuitOutCLP0Cells": circuitOutCLP0Cells,
       "circuitOutCLP1Cells": circuitOutCLP1Cells}
)
