# SNMP MIB module (SYNOPTICS-TOKENRING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNOPTICS-TOKENRING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:06 2024
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

(s3000TokenRing,) = mibBuilder.importSymbols(
    "SYNOPTICS-COMMON-MIB",
    "s3000TokenRing")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S3000TrBoard_ObjectIdentity = ObjectIdentity
s3000TrBoard = _S3000TrBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 2)
)
_S3TrCommonBoardTable_Object = MibTable
s3TrCommonBoardTable = _S3TrCommonBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    s3TrCommonBoardTable.setStatus("mandatory")
_S3TrCommonBoardEntry_Object = MibTableRow
s3TrCommonBoardEntry = _S3TrCommonBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 2, 2, 1)
)
s3TrCommonBoardEntry.setIndexNames(
    (0, "SYNOPTICS-TOKENRING-MIB", "s3TrCommonBoardIndex"),
)
if mibBuilder.loadTexts:
    s3TrCommonBoardEntry.setStatus("mandatory")
_S3TrCommonBoardIndex_Type = Integer32
_S3TrCommonBoardIndex_Object = MibTableColumn
s3TrCommonBoardIndex = _S3TrCommonBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 2, 2, 1, 1),
    _S3TrCommonBoardIndex_Type()
)
s3TrCommonBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrCommonBoardIndex.setStatus("mandatory")


class _S3TrCommonBoardRing1or2_Type(Integer32):
    """Custom type s3TrCommonBoardRing1or2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ring1", 2),
          ("ring2", 3))
    )


_S3TrCommonBoardRing1or2_Type.__name__ = "Integer32"
_S3TrCommonBoardRing1or2_Object = MibTableColumn
s3TrCommonBoardRing1or2 = _S3TrCommonBoardRing1or2_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 2, 2, 1, 2),
    _S3TrCommonBoardRing1or2_Type()
)
s3TrCommonBoardRing1or2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrCommonBoardRing1or2.setStatus("mandatory")


class _S3TrCommonBoardRingSpeed_Type(Integer32):
    """Custom type s3TrCommonBoardRingSpeed based on Integer32"""
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
        *(("other", 1),
          ("speed16M", 4),
          ("speed1M", 2),
          ("speed4M", 3))
    )


_S3TrCommonBoardRingSpeed_Type.__name__ = "Integer32"
_S3TrCommonBoardRingSpeed_Object = MibTableColumn
s3TrCommonBoardRingSpeed = _S3TrCommonBoardRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 2, 2, 1, 3),
    _S3TrCommonBoardRingSpeed_Type()
)
s3TrCommonBoardRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrCommonBoardRingSpeed.setStatus("mandatory")
_S3000TrPort_ObjectIdentity = ObjectIdentity
s3000TrPort = _S3000TrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3)
)
_S3TrPortTable_Object = MibTable
s3TrPortTable = _S3TrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    s3TrPortTable.setStatus("mandatory")
_S3TrPortEntry_Object = MibTableRow
s3TrPortEntry = _S3TrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1, 1)
)
s3TrPortEntry.setIndexNames(
    (0, "SYNOPTICS-TOKENRING-MIB", "s3TrPortBoardIndex"),
    (0, "SYNOPTICS-TOKENRING-MIB", "s3TrPortIndex"),
)
if mibBuilder.loadTexts:
    s3TrPortEntry.setStatus("mandatory")
_S3TrPortBoardIndex_Type = Integer32
_S3TrPortBoardIndex_Object = MibTableColumn
s3TrPortBoardIndex = _S3TrPortBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1, 1, 1),
    _S3TrPortBoardIndex_Type()
)
s3TrPortBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrPortBoardIndex.setStatus("mandatory")
_S3TrPortIndex_Type = Integer32
_S3TrPortIndex_Object = MibTableColumn
s3TrPortIndex = _S3TrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1, 1, 2),
    _S3TrPortIndex_Type()
)
s3TrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrPortIndex.setStatus("mandatory")


class _S3TrPortWrap_Type(Integer32):
    """Custom type s3TrPortWrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connect", 3),
          ("other", 1),
          ("wrap", 2))
    )


_S3TrPortWrap_Type.__name__ = "Integer32"
_S3TrPortWrap_Object = MibTableColumn
s3TrPortWrap = _S3TrPortWrap_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1, 1, 3),
    _S3TrPortWrap_Type()
)
s3TrPortWrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3TrPortWrap.setStatus("mandatory")


class _S3TrPortTestLatch_Type(Integer32):
    """Custom type s3TrPortTestLatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_S3TrPortTestLatch_Type.__name__ = "Integer32"
_S3TrPortTestLatch_Object = MibTableColumn
s3TrPortTestLatch = _S3TrPortTestLatch_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1, 1, 4),
    _S3TrPortTestLatch_Type()
)
s3TrPortTestLatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3TrPortTestLatch.setStatus("mandatory")


class _S3TrPortRelayStatus_Type(Integer32):
    """Custom type s3TrPortRelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_S3TrPortRelayStatus_Type.__name__ = "Integer32"
_S3TrPortRelayStatus_Object = MibTableColumn
s3TrPortRelayStatus = _S3TrPortRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1, 1, 5),
    _S3TrPortRelayStatus_Type()
)
s3TrPortRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrPortRelayStatus.setStatus("mandatory")


class _S3TrPortPhantomStatus_Type(Integer32):
    """Custom type s3TrPortPhantomStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_S3TrPortPhantomStatus_Type.__name__ = "Integer32"
_S3TrPortPhantomStatus_Object = MibTableColumn
s3TrPortPhantomStatus = _S3TrPortPhantomStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1, 1, 6),
    _S3TrPortPhantomStatus_Type()
)
s3TrPortPhantomStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrPortPhantomStatus.setStatus("mandatory")


class _S3TrPortPhantomChangeFlag_Type(Integer32):
    """Custom type s3TrPortPhantomChangeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("change", 3),
          ("noChange", 2),
          ("other", 1))
    )


_S3TrPortPhantomChangeFlag_Type.__name__ = "Integer32"
_S3TrPortPhantomChangeFlag_Object = MibTableColumn
s3TrPortPhantomChangeFlag = _S3TrPortPhantomChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1, 1, 7),
    _S3TrPortPhantomChangeFlag_Type()
)
s3TrPortPhantomChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrPortPhantomChangeFlag.setStatus("mandatory")


class _S3TrPortChgSyn2IBM_Type(Integer32):
    """Custom type s3TrPortChgSyn2IBM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ibm", 3),
          ("notSupported", 1),
          ("synoptics", 2))
    )


_S3TrPortChgSyn2IBM_Type.__name__ = "Integer32"
_S3TrPortChgSyn2IBM_Object = MibTableColumn
s3TrPortChgSyn2IBM = _S3TrPortChgSyn2IBM_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1, 1, 8),
    _S3TrPortChgSyn2IBM_Type()
)
s3TrPortChgSyn2IBM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3TrPortChgSyn2IBM.setStatus("mandatory")


class _S3TrPortStrap_Type(Integer32):
    """Custom type s3TrPortStrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ibm", 3),
          ("notSupported", 1),
          ("synoptics", 2))
    )


_S3TrPortStrap_Type.__name__ = "Integer32"
_S3TrPortStrap_Object = MibTableColumn
s3TrPortStrap = _S3TrPortStrap_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 3, 1, 1, 9),
    _S3TrPortStrap_Type()
)
s3TrPortStrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrPortStrap.setStatus("mandatory")
_S3000TrNmm_ObjectIdentity = ObjectIdentity
s3000TrNmm = _S3000TrNmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4)
)
_S3TrNmmFnNum_Type = Integer32
_S3TrNmmFnNum_Object = MibScalar
s3TrNmmFnNum = _S3TrNmmFnNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 1),
    _S3TrNmmFnNum_Type()
)
s3TrNmmFnNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3TrNmmFnNum.setStatus("mandatory")
_S3TrNmmRingNum_Type = Integer32
_S3TrNmmRingNum_Object = MibScalar
s3TrNmmRingNum = _S3TrNmmRingNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 2),
    _S3TrNmmRingNum_Type()
)
s3TrNmmRingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmRingNum.setStatus("mandatory")
_S3TrNmmSlotNum_Type = Integer32
_S3TrNmmSlotNum_Object = MibScalar
s3TrNmmSlotNum = _S3TrNmmSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 3),
    _S3TrNmmSlotNum_Type()
)
s3TrNmmSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmSlotNum.setStatus("deprecated")
_S3TrNmmFpuIdRev_Type = Integer32
_S3TrNmmFpuIdRev_Object = MibScalar
s3TrNmmFpuIdRev = _S3TrNmmFpuIdRev_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 4),
    _S3TrNmmFpuIdRev_Type()
)
s3TrNmmFpuIdRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmFpuIdRev.setStatus("mandatory")


class _S3TrNmmFpuStatus_Type(Integer32):
    """Custom type s3TrNmmFpuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notPresent", 1),
          ("operational", 3))
    )


_S3TrNmmFpuStatus_Type.__name__ = "Integer32"
_S3TrNmmFpuStatus_Object = MibScalar
s3TrNmmFpuStatus = _S3TrNmmFpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 5),
    _S3TrNmmFpuStatus_Type()
)
s3TrNmmFpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmFpuStatus.setStatus("mandatory")


class _S3TrNmmDramSize_Type(Integer32):
    """Custom type s3TrNmmDramSize based on Integer32"""
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
        *(("k512", 2),
          ("oneMeg", 3),
          ("other", 1),
          ("twoMeg", 4))
    )


_S3TrNmmDramSize_Type.__name__ = "Integer32"
_S3TrNmmDramSize_Object = MibScalar
s3TrNmmDramSize = _S3TrNmmDramSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 6),
    _S3TrNmmDramSize_Type()
)
s3TrNmmDramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmDramSize.setStatus("mandatory")


class _S3TrNmmEepromSize_Type(Integer32):
    """Custom type s3TrNmmEepromSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("k2kby8", 2),
          ("k8kby8", 3),
          ("other", 1))
    )


_S3TrNmmEepromSize_Type.__name__ = "Integer32"
_S3TrNmmEepromSize_Object = MibScalar
s3TrNmmEepromSize = _S3TrNmmEepromSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 7),
    _S3TrNmmEepromSize_Type()
)
s3TrNmmEepromSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmEepromSize.setStatus("mandatory")
_S3TrNmmGrpAddrFrmsRxOk_Type = Counter32
_S3TrNmmGrpAddrFrmsRxOk_Object = MibScalar
s3TrNmmGrpAddrFrmsRxOk = _S3TrNmmGrpAddrFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 8),
    _S3TrNmmGrpAddrFrmsRxOk_Type()
)
s3TrNmmGrpAddrFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmGrpAddrFrmsRxOk.setStatus("mandatory")


class _S3TrNmmRing1or2_Type(Integer32):
    """Custom type s3TrNmmRing1or2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ring1", 2),
          ("ring2", 3))
    )


_S3TrNmmRing1or2_Type.__name__ = "Integer32"
_S3TrNmmRing1or2_Object = MibScalar
s3TrNmmRing1or2 = _S3TrNmmRing1or2_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 9),
    _S3TrNmmRing1or2_Type()
)
s3TrNmmRing1or2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmRing1or2.setStatus("mandatory")


class _S3TrNmmRingSpeed_Type(Integer32):
    """Custom type s3TrNmmRingSpeed based on Integer32"""
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
        *(("other", 1),
          ("speed16M", 4),
          ("speed1M", 2),
          ("speed4M", 3))
    )


_S3TrNmmRingSpeed_Type.__name__ = "Integer32"
_S3TrNmmRingSpeed_Object = MibScalar
s3TrNmmRingSpeed = _S3TrNmmRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 10),
    _S3TrNmmRingSpeed_Type()
)
s3TrNmmRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmRingSpeed.setStatus("mandatory")


class _S3TrNmmHexDisplay_Type(OctetString):
    """Custom type s3TrNmmHexDisplay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_S3TrNmmHexDisplay_Type.__name__ = "OctetString"
_S3TrNmmHexDisplay_Object = MibScalar
s3TrNmmHexDisplay = _S3TrNmmHexDisplay_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 11),
    _S3TrNmmHexDisplay_Type()
)
s3TrNmmHexDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmHexDisplay.setStatus("mandatory")


class _S3TrNmmEpromSize_Type(Integer32):
    """Custom type s3TrNmmEpromSize based on Integer32"""
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
        *(("k128kby8", 7),
          ("k16kby8", 4),
          ("k256kby8", 8),
          ("k2kby8", 2),
          ("k32kby8", 5),
          ("k64kby8", 6),
          ("k8kby8", 3),
          ("other", 1))
    )


_S3TrNmmEpromSize_Type.__name__ = "Integer32"
_S3TrNmmEpromSize_Object = MibScalar
s3TrNmmEpromSize = _S3TrNmmEpromSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 4, 12),
    _S3TrNmmEpromSize_Type()
)
s3TrNmmEpromSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNmmEpromSize.setStatus("mandatory")
_S3000TrNode_ObjectIdentity = ObjectIdentity
s3000TrNode = _S3000TrNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5)
)
_S3TrNodeTable_Object = MibTable
s3TrNodeTable = _S3TrNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    s3TrNodeTable.setStatus("mandatory")
_S3TrNodeEntry_Object = MibTableRow
s3TrNodeEntry = _S3TrNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1)
)
s3TrNodeEntry.setIndexNames(
    (0, "SYNOPTICS-TOKENRING-MIB", "s3TrNodeEntMacAddress"),
)
if mibBuilder.loadTexts:
    s3TrNodeEntry.setStatus("mandatory")


class _S3TrNodeEntMacAddress_Type(OctetString):
    """Custom type s3TrNodeEntMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3TrNodeEntMacAddress_Type.__name__ = "OctetString"
_S3TrNodeEntMacAddress_Object = MibTableColumn
s3TrNodeEntMacAddress = _S3TrNodeEntMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 1),
    _S3TrNodeEntMacAddress_Type()
)
s3TrNodeEntMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntMacAddress.setStatus("mandatory")


class _S3TrNodeEntStatus_Type(Integer32):
    """Custom type s3TrNodeEntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beaconing", 1),
          ("notBeaconing", 2))
    )


_S3TrNodeEntStatus_Type.__name__ = "Integer32"
_S3TrNodeEntStatus_Object = MibTableColumn
s3TrNodeEntStatus = _S3TrNodeEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 4),
    _S3TrNodeEntStatus_Type()
)
s3TrNodeEntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntStatus.setStatus("mandatory")


class _S3TrNodeEntNodeStatus_Type(OctetString):
    """Custom type s3TrNodeEntNodeStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3TrNodeEntNodeStatus_Type.__name__ = "OctetString"
_S3TrNodeEntNodeStatus_Object = MibTableColumn
s3TrNodeEntNodeStatus = _S3TrNodeEntNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 5),
    _S3TrNodeEntNodeStatus_Type()
)
s3TrNodeEntNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntNodeStatus.setStatus("mandatory")
_S3TrNodeLineErrs_Type = Counter32
_S3TrNodeLineErrs_Object = MibTableColumn
s3TrNodeLineErrs = _S3TrNodeLineErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 6),
    _S3TrNodeLineErrs_Type()
)
s3TrNodeLineErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeLineErrs.setStatus("mandatory")
_S3TrNodeBurstErrs_Type = Counter32
_S3TrNodeBurstErrs_Object = MibTableColumn
s3TrNodeBurstErrs = _S3TrNodeBurstErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 7),
    _S3TrNodeBurstErrs_Type()
)
s3TrNodeBurstErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeBurstErrs.setStatus("mandatory")
_S3TrNodeAriFciErrs_Type = Counter32
_S3TrNodeAriFciErrs_Object = MibTableColumn
s3TrNodeAriFciErrs = _S3TrNodeAriFciErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 8),
    _S3TrNodeAriFciErrs_Type()
)
s3TrNodeAriFciErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeAriFciErrs.setStatus("mandatory")
_S3TrNodeLostFrames_Type = Counter32
_S3TrNodeLostFrames_Object = MibTableColumn
s3TrNodeLostFrames = _S3TrNodeLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 9),
    _S3TrNodeLostFrames_Type()
)
s3TrNodeLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeLostFrames.setStatus("mandatory")
_S3TrNodeRcvCongestErrs_Type = Counter32
_S3TrNodeRcvCongestErrs_Object = MibTableColumn
s3TrNodeRcvCongestErrs = _S3TrNodeRcvCongestErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 10),
    _S3TrNodeRcvCongestErrs_Type()
)
s3TrNodeRcvCongestErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeRcvCongestErrs.setStatus("mandatory")
_S3TrNodeFrmCopyErrs_Type = Counter32
_S3TrNodeFrmCopyErrs_Object = MibTableColumn
s3TrNodeFrmCopyErrs = _S3TrNodeFrmCopyErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 11),
    _S3TrNodeFrmCopyErrs_Type()
)
s3TrNodeFrmCopyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeFrmCopyErrs.setStatus("mandatory")
_S3TrNodeTokenErrs_Type = Counter32
_S3TrNodeTokenErrs_Object = MibTableColumn
s3TrNodeTokenErrs = _S3TrNodeTokenErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 12),
    _S3TrNodeTokenErrs_Type()
)
s3TrNodeTokenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeTokenErrs.setStatus("mandatory")
_S3TrNodeInternalErrs_Type = Counter32
_S3TrNodeInternalErrs_Object = MibTableColumn
s3TrNodeInternalErrs = _S3TrNodeInternalErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 13),
    _S3TrNodeInternalErrs_Type()
)
s3TrNodeInternalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeInternalErrs.setStatus("mandatory")
_S3TrNodeAbortTransErrs_Type = Counter32
_S3TrNodeAbortTransErrs_Object = MibTableColumn
s3TrNodeAbortTransErrs = _S3TrNodeAbortTransErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 14),
    _S3TrNodeAbortTransErrs_Type()
)
s3TrNodeAbortTransErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeAbortTransErrs.setStatus("mandatory")
_S3TrNodeFrequencyErrs_Type = Counter32
_S3TrNodeFrequencyErrs_Object = MibTableColumn
s3TrNodeFrequencyErrs = _S3TrNodeFrequencyErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 15),
    _S3TrNodeFrequencyErrs_Type()
)
s3TrNodeFrequencyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeFrequencyErrs.setStatus("mandatory")


class _S3TrNodeEntProductId_Type(OctetString):
    """Custom type s3TrNodeEntProductId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_S3TrNodeEntProductId_Type.__name__ = "OctetString"
_S3TrNodeEntProductId_Object = MibTableColumn
s3TrNodeEntProductId = _S3TrNodeEntProductId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 16),
    _S3TrNodeEntProductId_Type()
)
s3TrNodeEntProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntProductId.setStatus("mandatory")


class _S3TrNodeEntUna_Type(OctetString):
    """Custom type s3TrNodeEntUna based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3TrNodeEntUna_Type.__name__ = "OctetString"
_S3TrNodeEntUna_Object = MibTableColumn
s3TrNodeEntUna = _S3TrNodeEntUna_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 17),
    _S3TrNodeEntUna_Type()
)
s3TrNodeEntUna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntUna.setStatus("mandatory")


class _S3TrNodeEntNodeVersion_Type(OctetString):
    """Custom type s3TrNodeEntNodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_S3TrNodeEntNodeVersion_Type.__name__ = "OctetString"
_S3TrNodeEntNodeVersion_Object = MibTableColumn
s3TrNodeEntNodeVersion = _S3TrNodeEntNodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 18),
    _S3TrNodeEntNodeVersion_Type()
)
s3TrNodeEntNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntNodeVersion.setStatus("mandatory")


class _S3TrNodeEntPhysDrop_Type(OctetString):
    """Custom type s3TrNodeEntPhysDrop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_S3TrNodeEntPhysDrop_Type.__name__ = "OctetString"
_S3TrNodeEntPhysDrop_Object = MibTableColumn
s3TrNodeEntPhysDrop = _S3TrNodeEntPhysDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 19),
    _S3TrNodeEntPhysDrop_Type()
)
s3TrNodeEntPhysDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntPhysDrop.setStatus("mandatory")


class _S3TrNodeEntFuncAddr_Type(OctetString):
    """Custom type s3TrNodeEntFuncAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3TrNodeEntFuncAddr_Type.__name__ = "OctetString"
_S3TrNodeEntFuncAddr_Object = MibTableColumn
s3TrNodeEntFuncAddr = _S3TrNodeEntFuncAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 20),
    _S3TrNodeEntFuncAddr_Type()
)
s3TrNodeEntFuncAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntFuncAddr.setStatus("mandatory")


class _S3TrNodeEntAuthFuncClass_Type(OctetString):
    """Custom type s3TrNodeEntAuthFuncClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_S3TrNodeEntAuthFuncClass_Type.__name__ = "OctetString"
_S3TrNodeEntAuthFuncClass_Object = MibTableColumn
s3TrNodeEntAuthFuncClass = _S3TrNodeEntAuthFuncClass_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 21),
    _S3TrNodeEntAuthFuncClass_Type()
)
s3TrNodeEntAuthFuncClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntAuthFuncClass.setStatus("mandatory")


class _S3TrNodeEntAuthAccPriority_Type(OctetString):
    """Custom type s3TrNodeEntAuthAccPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_S3TrNodeEntAuthAccPriority_Type.__name__ = "OctetString"
_S3TrNodeEntAuthAccPriority_Object = MibTableColumn
s3TrNodeEntAuthAccPriority = _S3TrNodeEntAuthAccPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 22),
    _S3TrNodeEntAuthAccPriority_Type()
)
s3TrNodeEntAuthAccPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntAuthAccPriority.setStatus("mandatory")


class _S3TrNodeEntGrpAddr_Type(OctetString):
    """Custom type s3TrNodeEntGrpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3TrNodeEntGrpAddr_Type.__name__ = "OctetString"
_S3TrNodeEntGrpAddr_Object = MibTableColumn
s3TrNodeEntGrpAddr = _S3TrNodeEntGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 23),
    _S3TrNodeEntGrpAddr_Type()
)
s3TrNodeEntGrpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntGrpAddr.setStatus("mandatory")


class _S3TrNodeEntStationId_Type(OctetString):
    """Custom type s3TrNodeEntStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3TrNodeEntStationId_Type.__name__ = "OctetString"
_S3TrNodeEntStationId_Object = MibTableColumn
s3TrNodeEntStationId = _S3TrNodeEntStationId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 24),
    _S3TrNodeEntStationId_Type()
)
s3TrNodeEntStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntStationId.setStatus("mandatory")


class _S3TrNodeEntBeaconType_Type(Integer32):
    """Custom type s3TrNodeEntBeaconType based on Integer32"""
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
        *(("bit-streaming", 3),
          ("contention-streaming", 4),
          ("reconfiguration", 1),
          ("signal-loss", 2))
    )


_S3TrNodeEntBeaconType_Type.__name__ = "Integer32"
_S3TrNodeEntBeaconType_Object = MibTableColumn
s3TrNodeEntBeaconType = _S3TrNodeEntBeaconType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 25),
    _S3TrNodeEntBeaconType_Type()
)
s3TrNodeEntBeaconType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeEntBeaconType.setStatus("mandatory")
_S3TrNodeBeaconCnt_Type = Counter32
_S3TrNodeBeaconCnt_Object = MibTableColumn
s3TrNodeBeaconCnt = _S3TrNodeBeaconCnt_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 26),
    _S3TrNodeBeaconCnt_Type()
)
s3TrNodeBeaconCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeBeaconCnt.setStatus("mandatory")
_S3TrNodeLastBeaconTime_Type = TimeTicks
_S3TrNodeLastBeaconTime_Object = MibTableColumn
s3TrNodeLastBeaconTime = _S3TrNodeLastBeaconTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 27),
    _S3TrNodeLastBeaconTime_Type()
)
s3TrNodeLastBeaconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeLastBeaconTime.setStatus("mandatory")
_S3TrNodeLastInsertTime_Type = TimeTicks
_S3TrNodeLastInsertTime_Object = MibTableColumn
s3TrNodeLastInsertTime = _S3TrNodeLastInsertTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 28),
    _S3TrNodeLastInsertTime_Type()
)
s3TrNodeLastInsertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeLastInsertTime.setStatus("mandatory")
_S3TrNodeFirstInsertTime_Type = TimeTicks
_S3TrNodeFirstInsertTime_Object = MibTableColumn
s3TrNodeFirstInsertTime = _S3TrNodeFirstInsertTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 29),
    _S3TrNodeFirstInsertTime_Type()
)
s3TrNodeFirstInsertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeFirstInsertTime.setStatus("mandatory")
_S3TrNodeLastDeinsertTime_Type = TimeTicks
_S3TrNodeLastDeinsertTime_Object = MibTableColumn
s3TrNodeLastDeinsertTime = _S3TrNodeLastDeinsertTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 30),
    _S3TrNodeLastDeinsertTime_Type()
)
s3TrNodeLastDeinsertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrNodeLastDeinsertTime.setStatus("mandatory")


class _S3TrNodeRemoveStation_Type(Integer32):
    """Custom type s3TrNodeRemoveStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("remove", 2))
    )


_S3TrNodeRemoveStation_Type.__name__ = "Integer32"
_S3TrNodeRemoveStation_Object = MibTableColumn
s3TrNodeRemoveStation = _S3TrNodeRemoveStation_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 5, 1, 1, 31),
    _S3TrNodeRemoveStation_Type()
)
s3TrNodeRemoveStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3TrNodeRemoveStation.setStatus("mandatory")
_S3000TrRing_ObjectIdentity = ObjectIdentity
s3000TrRing = _S3000TrRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7)
)
_S3TrRingStats_ObjectIdentity = ObjectIdentity
s3TrRingStats = _S3TrRingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1)
)


class _S3TrRingStatus_Type(Integer32):
    """Custom type s3TrRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beaconing", 1),
          ("notbeaconing", 2))
    )


_S3TrRingStatus_Type.__name__ = "Integer32"
_S3TrRingStatus_Object = MibScalar
s3TrRingStatus = _S3TrRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 1),
    _S3TrRingStatus_Type()
)
s3TrRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingStatus.setStatus("mandatory")
_S3TrRingFrmsRxOk_Type = Counter32
_S3TrRingFrmsRxOk_Object = MibScalar
s3TrRingFrmsRxOk = _S3TrRingFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 2),
    _S3TrRingFrmsRxOk_Type()
)
s3TrRingFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingFrmsRxOk.setStatus("mandatory")
_S3TrRingOctetsRxOk_Type = Counter32
_S3TrRingOctetsRxOk_Object = MibScalar
s3TrRingOctetsRxOk = _S3TrRingOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 3),
    _S3TrRingOctetsRxOk_Type()
)
s3TrRingOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingOctetsRxOk.setStatus("mandatory")
_S3TrRingBcastFrmsRxOk_Type = Counter32
_S3TrRingBcastFrmsRxOk_Object = MibScalar
s3TrRingBcastFrmsRxOk = _S3TrRingBcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 4),
    _S3TrRingBcastFrmsRxOk_Type()
)
s3TrRingBcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingBcastFrmsRxOk.setStatus("mandatory")
_S3TrRingLineErrs_Type = Counter32
_S3TrRingLineErrs_Object = MibScalar
s3TrRingLineErrs = _S3TrRingLineErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 5),
    _S3TrRingLineErrs_Type()
)
s3TrRingLineErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingLineErrs.setStatus("mandatory")
_S3TrRingBurstErrs_Type = Counter32
_S3TrRingBurstErrs_Object = MibScalar
s3TrRingBurstErrs = _S3TrRingBurstErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 6),
    _S3TrRingBurstErrs_Type()
)
s3TrRingBurstErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingBurstErrs.setStatus("mandatory")
_S3TrRingAriFciErrs_Type = Counter32
_S3TrRingAriFciErrs_Object = MibScalar
s3TrRingAriFciErrs = _S3TrRingAriFciErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 7),
    _S3TrRingAriFciErrs_Type()
)
s3TrRingAriFciErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingAriFciErrs.setStatus("mandatory")
_S3TrRingLostFrames_Type = Counter32
_S3TrRingLostFrames_Object = MibScalar
s3TrRingLostFrames = _S3TrRingLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 8),
    _S3TrRingLostFrames_Type()
)
s3TrRingLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingLostFrames.setStatus("mandatory")
_S3TrRingRcvCongestErrs_Type = Counter32
_S3TrRingRcvCongestErrs_Object = MibScalar
s3TrRingRcvCongestErrs = _S3TrRingRcvCongestErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 9),
    _S3TrRingRcvCongestErrs_Type()
)
s3TrRingRcvCongestErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingRcvCongestErrs.setStatus("mandatory")
_S3TrRingFrmCopyErrs_Type = Counter32
_S3TrRingFrmCopyErrs_Object = MibScalar
s3TrRingFrmCopyErrs = _S3TrRingFrmCopyErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 10),
    _S3TrRingFrmCopyErrs_Type()
)
s3TrRingFrmCopyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingFrmCopyErrs.setStatus("mandatory")
_S3TrRingTokenErrs_Type = Counter32
_S3TrRingTokenErrs_Object = MibScalar
s3TrRingTokenErrs = _S3TrRingTokenErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 11),
    _S3TrRingTokenErrs_Type()
)
s3TrRingTokenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingTokenErrs.setStatus("mandatory")
_S3TrRingInternalErrs_Type = Counter32
_S3TrRingInternalErrs_Object = MibScalar
s3TrRingInternalErrs = _S3TrRingInternalErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 12),
    _S3TrRingInternalErrs_Type()
)
s3TrRingInternalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingInternalErrs.setStatus("mandatory")
_S3TrRingAbortTransErrs_Type = Counter32
_S3TrRingAbortTransErrs_Object = MibScalar
s3TrRingAbortTransErrs = _S3TrRingAbortTransErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 13),
    _S3TrRingAbortTransErrs_Type()
)
s3TrRingAbortTransErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingAbortTransErrs.setStatus("mandatory")
_S3TrRingFrequencyErrs_Type = Counter32
_S3TrRingFrequencyErrs_Object = MibScalar
s3TrRingFrequencyErrs = _S3TrRingFrequencyErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 14),
    _S3TrRingFrequencyErrs_Type()
)
s3TrRingFrequencyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingFrequencyErrs.setStatus("mandatory")
_S3TrRingBeaconCnt_Type = Counter32
_S3TrRingBeaconCnt_Object = MibScalar
s3TrRingBeaconCnt = _S3TrRingBeaconCnt_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 15),
    _S3TrRingBeaconCnt_Type()
)
s3TrRingBeaconCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingBeaconCnt.setStatus("mandatory")


class _S3TrRingBeaconType_Type(Integer32):
    """Custom type s3TrRingBeaconType based on Integer32"""
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
        *(("bit-streaming", 3),
          ("contention-streaming", 4),
          ("reconfiguration", 1),
          ("signal-loss", 2))
    )


_S3TrRingBeaconType_Type.__name__ = "Integer32"
_S3TrRingBeaconType_Object = MibScalar
s3TrRingBeaconType = _S3TrRingBeaconType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 16),
    _S3TrRingBeaconType_Type()
)
s3TrRingBeaconType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingBeaconType.setStatus("mandatory")
_S3TrRingLastBeaconTime_Type = TimeTicks
_S3TrRingLastBeaconTime_Object = MibScalar
s3TrRingLastBeaconTime = _S3TrRingLastBeaconTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 17),
    _S3TrRingLastBeaconTime_Type()
)
s3TrRingLastBeaconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingLastBeaconTime.setStatus("mandatory")


class _S3TrRingBeaconStation_Type(OctetString):
    """Custom type s3TrRingBeaconStation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3TrRingBeaconStation_Type.__name__ = "OctetString"
_S3TrRingBeaconStation_Object = MibScalar
s3TrRingBeaconStation = _S3TrRingBeaconStation_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 3, 7, 1, 18),
    _S3TrRingBeaconStation_Type()
)
s3TrRingBeaconStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3TrRingBeaconStation.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOPTICS-TOKENRING-MIB",
    **{"s3000TrBoard": s3000TrBoard,
       "s3TrCommonBoardTable": s3TrCommonBoardTable,
       "s3TrCommonBoardEntry": s3TrCommonBoardEntry,
       "s3TrCommonBoardIndex": s3TrCommonBoardIndex,
       "s3TrCommonBoardRing1or2": s3TrCommonBoardRing1or2,
       "s3TrCommonBoardRingSpeed": s3TrCommonBoardRingSpeed,
       "s3000TrPort": s3000TrPort,
       "s3TrPortTable": s3TrPortTable,
       "s3TrPortEntry": s3TrPortEntry,
       "s3TrPortBoardIndex": s3TrPortBoardIndex,
       "s3TrPortIndex": s3TrPortIndex,
       "s3TrPortWrap": s3TrPortWrap,
       "s3TrPortTestLatch": s3TrPortTestLatch,
       "s3TrPortRelayStatus": s3TrPortRelayStatus,
       "s3TrPortPhantomStatus": s3TrPortPhantomStatus,
       "s3TrPortPhantomChangeFlag": s3TrPortPhantomChangeFlag,
       "s3TrPortChgSyn2IBM": s3TrPortChgSyn2IBM,
       "s3TrPortStrap": s3TrPortStrap,
       "s3000TrNmm": s3000TrNmm,
       "s3TrNmmFnNum": s3TrNmmFnNum,
       "s3TrNmmRingNum": s3TrNmmRingNum,
       "s3TrNmmSlotNum": s3TrNmmSlotNum,
       "s3TrNmmFpuIdRev": s3TrNmmFpuIdRev,
       "s3TrNmmFpuStatus": s3TrNmmFpuStatus,
       "s3TrNmmDramSize": s3TrNmmDramSize,
       "s3TrNmmEepromSize": s3TrNmmEepromSize,
       "s3TrNmmGrpAddrFrmsRxOk": s3TrNmmGrpAddrFrmsRxOk,
       "s3TrNmmRing1or2": s3TrNmmRing1or2,
       "s3TrNmmRingSpeed": s3TrNmmRingSpeed,
       "s3TrNmmHexDisplay": s3TrNmmHexDisplay,
       "s3TrNmmEpromSize": s3TrNmmEpromSize,
       "s3000TrNode": s3000TrNode,
       "s3TrNodeTable": s3TrNodeTable,
       "s3TrNodeEntry": s3TrNodeEntry,
       "s3TrNodeEntMacAddress": s3TrNodeEntMacAddress,
       "s3TrNodeEntStatus": s3TrNodeEntStatus,
       "s3TrNodeEntNodeStatus": s3TrNodeEntNodeStatus,
       "s3TrNodeLineErrs": s3TrNodeLineErrs,
       "s3TrNodeBurstErrs": s3TrNodeBurstErrs,
       "s3TrNodeAriFciErrs": s3TrNodeAriFciErrs,
       "s3TrNodeLostFrames": s3TrNodeLostFrames,
       "s3TrNodeRcvCongestErrs": s3TrNodeRcvCongestErrs,
       "s3TrNodeFrmCopyErrs": s3TrNodeFrmCopyErrs,
       "s3TrNodeTokenErrs": s3TrNodeTokenErrs,
       "s3TrNodeInternalErrs": s3TrNodeInternalErrs,
       "s3TrNodeAbortTransErrs": s3TrNodeAbortTransErrs,
       "s3TrNodeFrequencyErrs": s3TrNodeFrequencyErrs,
       "s3TrNodeEntProductId": s3TrNodeEntProductId,
       "s3TrNodeEntUna": s3TrNodeEntUna,
       "s3TrNodeEntNodeVersion": s3TrNodeEntNodeVersion,
       "s3TrNodeEntPhysDrop": s3TrNodeEntPhysDrop,
       "s3TrNodeEntFuncAddr": s3TrNodeEntFuncAddr,
       "s3TrNodeEntAuthFuncClass": s3TrNodeEntAuthFuncClass,
       "s3TrNodeEntAuthAccPriority": s3TrNodeEntAuthAccPriority,
       "s3TrNodeEntGrpAddr": s3TrNodeEntGrpAddr,
       "s3TrNodeEntStationId": s3TrNodeEntStationId,
       "s3TrNodeEntBeaconType": s3TrNodeEntBeaconType,
       "s3TrNodeBeaconCnt": s3TrNodeBeaconCnt,
       "s3TrNodeLastBeaconTime": s3TrNodeLastBeaconTime,
       "s3TrNodeLastInsertTime": s3TrNodeLastInsertTime,
       "s3TrNodeFirstInsertTime": s3TrNodeFirstInsertTime,
       "s3TrNodeLastDeinsertTime": s3TrNodeLastDeinsertTime,
       "s3TrNodeRemoveStation": s3TrNodeRemoveStation,
       "s3000TrRing": s3000TrRing,
       "s3TrRingStats": s3TrRingStats,
       "s3TrRingStatus": s3TrRingStatus,
       "s3TrRingFrmsRxOk": s3TrRingFrmsRxOk,
       "s3TrRingOctetsRxOk": s3TrRingOctetsRxOk,
       "s3TrRingBcastFrmsRxOk": s3TrRingBcastFrmsRxOk,
       "s3TrRingLineErrs": s3TrRingLineErrs,
       "s3TrRingBurstErrs": s3TrRingBurstErrs,
       "s3TrRingAriFciErrs": s3TrRingAriFciErrs,
       "s3TrRingLostFrames": s3TrRingLostFrames,
       "s3TrRingRcvCongestErrs": s3TrRingRcvCongestErrs,
       "s3TrRingFrmCopyErrs": s3TrRingFrmCopyErrs,
       "s3TrRingTokenErrs": s3TrRingTokenErrs,
       "s3TrRingInternalErrs": s3TrRingInternalErrs,
       "s3TrRingAbortTransErrs": s3TrRingAbortTransErrs,
       "s3TrRingFrequencyErrs": s3TrRingFrequencyErrs,
       "s3TrRingBeaconCnt": s3TrRingBeaconCnt,
       "s3TrRingBeaconType": s3TrRingBeaconType,
       "s3TrRingLastBeaconTime": s3TrRingLastBeaconTime,
       "s3TrRingBeaconStation": s3TrRingBeaconStation}
)
