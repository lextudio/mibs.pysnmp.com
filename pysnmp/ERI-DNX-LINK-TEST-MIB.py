# SNMP MIB module (ERI-DNX-LINK-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-LINK-TEST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:25 2024
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

(DataSwitch,
 DecisionType,
 LinkPortAddress,
 OneByteField,
 dnx) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "DataSwitch",
    "DecisionType",
    "LinkPortAddress",
    "OneByteField",
    "dnx")

(eriMibs,) = mibBuilder.importSymbols(
    "ERI-ROOT-SMI",
    "eriMibs")

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


# MODULE-IDENTITY

eriDNXLinkTestMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 8)
)
eriDNXLinkTestMIB.setRevisions(
        ("2003-07-16 00:00",
         "2002-04-08 00:00",
         "2002-01-30 00:00",
         "2001-12-14 00:00",
         "2001-10-16 00:00",
         "2001-08-17 00:00",
         "2001-07-18 00:00",
         "2001-06-18 00:00",
         "2001-05-22 00:00",
         "2001-03-01 00:00",
         "2000-12-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UserDefFormat(IpAddress, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Diagnostics_ObjectIdentity = ObjectIdentity
diagnostics = _Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5)
)
_Dsx1Test_ObjectIdentity = ObjectIdentity
dsx1Test = _Dsx1Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1)
)
_Dsx1TestTable_Object = MibTable
dsx1TestTable = _Dsx1TestTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dsx1TestTable.setStatus("current")
_Dsx1TestEntry_Object = MibTableRow
dsx1TestEntry = _Dsx1TestEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1)
)
dsx1TestEntry.setIndexNames(
    (0, "ERI-DNX-LINK-TEST-MIB", "dsx1TestLinkAddr"),
)
if mibBuilder.loadTexts:
    dsx1TestEntry.setStatus("current")
_Dsx1TestLinkAddr_Type = LinkPortAddress
_Dsx1TestLinkAddr_Object = MibTableColumn
dsx1TestLinkAddr = _Dsx1TestLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 1),
    _Dsx1TestLinkAddr_Type()
)
dsx1TestLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestLinkAddr.setStatus("current")
_Dsx1TestResrcId_Type = Integer32
_Dsx1TestResrcId_Object = MibTableColumn
dsx1TestResrcId = _Dsx1TestResrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 2),
    _Dsx1TestResrcId_Type()
)
dsx1TestResrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestResrcId.setStatus("current")


class _Dsx1TestLinkState_Type(Integer32):
    """Custom type dsx1TestLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              8,
              32,
              64,
              2048,
              4096,
              65535,
              2097152,
              4194304,
              6291456,
              8388608,
              1073741824,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ais", 8),
          ("cfa", 4096),
          ("errors", 2147483647),
          ("lof", 32),
          ("los", 64),
          ("ok", 0),
          ("oos", 65535),
          ("red", 2048),
          ("rxSlip", 4194304),
          ("sef", 8388608),
          ("slip", 6291456),
          ("txSlip", 2097152),
          ("underTest", 1073741824),
          ("yel", 2))
    )


_Dsx1TestLinkState_Type.__name__ = "Integer32"
_Dsx1TestLinkState_Object = MibTableColumn
dsx1TestLinkState = _Dsx1TestLinkState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 3),
    _Dsx1TestLinkState_Type()
)
dsx1TestLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestLinkState.setStatus("current")


class _Dsx1TestLinkLoop_Type(Integer32):
    """Custom type dsx1TestLinkLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              12,
              16,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("allLine", 16),
          ("allLocal", 12),
          ("analog", 5),
          ("line", 3),
          ("local", 1),
          ("loopDwnReq", 75),
          ("loopUpReq", 74),
          ("off", 0),
          ("payload", 4),
          ("remote", 2),
          ("remoteLine", 7),
          ("smartjack", 6),
          ("user-defined", 8))
    )


_Dsx1TestLinkLoop_Type.__name__ = "Integer32"
_Dsx1TestLinkLoop_Object = MibTableColumn
dsx1TestLinkLoop = _Dsx1TestLinkLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 4),
    _Dsx1TestLinkLoop_Type()
)
dsx1TestLinkLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TestLinkLoop.setStatus("current")


class _Dsx1TestBackplnLoop_Type(Integer32):
    """Custom type dsx1TestBackplnLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("loopBackplane", 21),
          ("loopOffBackplane", 20))
    )


_Dsx1TestBackplnLoop_Type.__name__ = "Integer32"
_Dsx1TestBackplnLoop_Object = MibTableColumn
dsx1TestBackplnLoop = _Dsx1TestBackplnLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 5),
    _Dsx1TestBackplnLoop_Type()
)
dsx1TestBackplnLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TestBackplnLoop.setStatus("current")


class _Dsx1TestBertState_Type(Integer32):
    """Custom type dsx1TestBertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              51,
              52,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              80,
              81,
              82,
              83,
              84,
              85,
              86)
        )
    )
    namedValues = NamedValues(
        *(("all-2047", 70),
          ("all-ones", 51),
          ("all-zeros", 52),
          ("bertOff", 50),
          ("framed-1-in-8", 85),
          ("framed-2-11th-with7zeros", 65),
          ("framed-2-15th", 62),
          ("framed-2-15th-invert", 86),
          ("framed-2-15th-with7zeros", 66),
          ("framed-2-20th", 63),
          ("framed-2-23rd", 64),
          ("framed-2-23rd-with14zeros", 68),
          ("framed-2047", 61),
          ("framed-3-in-24", 69),
          ("framed-QRSS", 67),
          ("system-2047", 71),
          ("system-framed-2-15", 82),
          ("system-framed-2-15th-invert", 80),
          ("system-framed-2-20", 83),
          ("system-framed-2047", 81),
          ("system-framed-QRSS", 84))
    )


_Dsx1TestBertState_Type.__name__ = "Integer32"
_Dsx1TestBertState_Object = MibTableColumn
dsx1TestBertState = _Dsx1TestBertState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 6),
    _Dsx1TestBertState_Type()
)
dsx1TestBertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TestBertState.setStatus("current")
_Dsx1TestDuration_Type = Integer32
_Dsx1TestDuration_Object = MibTableColumn
dsx1TestDuration = _Dsx1TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 7),
    _Dsx1TestDuration_Type()
)
dsx1TestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestDuration.setStatus("current")


class _Dsx1TestBitErrs_Type(Unsigned32):
    """Custom type dsx1TestBitErrs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Dsx1TestBitErrs_Type.__name__ = "Unsigned32"
_Dsx1TestBitErrs_Object = MibTableColumn
dsx1TestBitErrs = _Dsx1TestBitErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 8),
    _Dsx1TestBitErrs_Type()
)
dsx1TestBitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestBitErrs.setStatus("current")
_Dsx1TestESs_Type = Counter32
_Dsx1TestESs_Object = MibTableColumn
dsx1TestESs = _Dsx1TestESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 9),
    _Dsx1TestESs_Type()
)
dsx1TestESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestESs.setStatus("current")
_Dsx1TestRemoteESs_Type = Counter32
_Dsx1TestRemoteESs_Object = MibTableColumn
dsx1TestRemoteESs = _Dsx1TestRemoteESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 10),
    _Dsx1TestRemoteESs_Type()
)
dsx1TestRemoteESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestRemoteESs.setStatus("current")
_Dsx1TestErrFreeSecs_Type = Counter32
_Dsx1TestErrFreeSecs_Object = MibTableColumn
dsx1TestErrFreeSecs = _Dsx1TestErrFreeSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 11),
    _Dsx1TestErrFreeSecs_Type()
)
dsx1TestErrFreeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestErrFreeSecs.setStatus("current")
_Dsx1TestSESs_Type = Counter32
_Dsx1TestSESs_Object = MibTableColumn
dsx1TestSESs = _Dsx1TestSESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 12),
    _Dsx1TestSESs_Type()
)
dsx1TestSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestSESs.setStatus("current")
_Dsx1TestUASs_Type = Counter32
_Dsx1TestUASs_Object = MibTableColumn
dsx1TestUASs = _Dsx1TestUASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 13),
    _Dsx1TestUASs_Type()
)
dsx1TestUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestUASs.setStatus("current")
_Dsx1TestASs_Type = Counter32
_Dsx1TestASs_Object = MibTableColumn
dsx1TestASs = _Dsx1TestASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 14),
    _Dsx1TestASs_Type()
)
dsx1TestASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestASs.setStatus("current")
_Dsx1TestESNonUASs_Type = Counter32
_Dsx1TestESNonUASs_Object = MibTableColumn
dsx1TestESNonUASs = _Dsx1TestESNonUASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 15),
    _Dsx1TestESNonUASs_Type()
)
dsx1TestESNonUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestESNonUASs.setStatus("current")


class _Dsx1TestSevereError_Type(Integer32):
    """Custom type dsx1TestSevereError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dsx1TestSevereError_Type.__name__ = "Integer32"
_Dsx1TestSevereError_Object = MibTableColumn
dsx1TestSevereError = _Dsx1TestSevereError_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 16),
    _Dsx1TestSevereError_Type()
)
dsx1TestSevereError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TestSevereError.setStatus("current")
_Dsx1TestBitSpeed_Type = Integer32
_Dsx1TestBitSpeed_Object = MibTableColumn
dsx1TestBitSpeed = _Dsx1TestBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 17),
    _Dsx1TestBitSpeed_Type()
)
dsx1TestBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TestBitSpeed.setStatus("current")


class _Dsx1TestCmdStatus_Type(Integer32):
    """Custom type dsx1TestCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              14,
              16,
              101,
              114,
              116,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-successful", 114),
          ("clearErrors", 14),
          ("err-field-cannot-be-set", 206),
          ("err-general-test-error", 200),
          ("err-invalid-bert-type", 203),
          ("err-invalid-command", 208),
          ("err-invalid-loop-type", 202),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-invalid-user-defined-loop", 209),
          ("err-link-in-E1-mode", 210),
          ("err-link-in-clear-mode", 204),
          ("err-link-not-connected", 207),
          ("err-link-not-in-service", 201),
          ("err-link-not-in-test", 211),
          ("err-snmp-parse-failed", 500),
          ("err-test-in-progress", 205),
          ("insert-successful", 116),
          ("insertError", 16),
          ("ready-for-command", 0),
          ("update-successful", 101),
          ("updateTest", 1))
    )


_Dsx1TestCmdStatus_Type.__name__ = "Integer32"
_Dsx1TestCmdStatus_Object = MibTableColumn
dsx1TestCmdStatus = _Dsx1TestCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 18),
    _Dsx1TestCmdStatus_Type()
)
dsx1TestCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TestCmdStatus.setStatus("current")


class _Dsx1TestInsErrMode_Type(Integer32):
    """Custom type dsx1TestInsErrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ais-unframed-all-ones", 16),
          ("allErrors", 9),
          ("bert-error", 3),
          ("bit-slip", 4),
          ("cas-multiframe", 1),
          ("crc", 6),
          ("fas-inverted", 12),
          ("fbit", 7),
          ("frame-alignment", 5),
          ("line-code-violation", 8),
          ("multiframe", 2),
          ("nfas-bit2-inverted", 13),
          ("not-applicable", 0),
          ("rai", 14),
          ("ts16-ais", 15),
          ("ybit", 11),
          ("yellow-alarm", 10))
    )


_Dsx1TestInsErrMode_Type.__name__ = "Integer32"
_Dsx1TestInsErrMode_Object = MibTableColumn
dsx1TestInsErrMode = _Dsx1TestInsErrMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 19),
    _Dsx1TestInsErrMode_Type()
)
dsx1TestInsErrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TestInsErrMode.setStatus("current")
_Dsx1TestUsrLoopUnframed_Type = DecisionType
_Dsx1TestUsrLoopUnframed_Object = MibTableColumn
dsx1TestUsrLoopUnframed = _Dsx1TestUsrLoopUnframed_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 20),
    _Dsx1TestUsrLoopUnframed_Type()
)
dsx1TestUsrLoopUnframed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TestUsrLoopUnframed.setStatus("current")
_Dsx1TestUsrDefLoop_Type = UserDefFormat
_Dsx1TestUsrDefLoop_Object = MibTableColumn
dsx1TestUsrDefLoop = _Dsx1TestUsrDefLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 1, 1, 1, 21),
    _Dsx1TestUsrDefLoop_Type()
)
dsx1TestUsrDefLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TestUsrDefLoop.setStatus("current")
_HsTest_ObjectIdentity = ObjectIdentity
hsTest = _HsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2)
)
_HsTestTable_Object = MibTable
hsTestTable = _HsTestTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hsTestTable.setStatus("current")
_HsTestEntry_Object = MibTableRow
hsTestEntry = _HsTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1)
)
hsTestEntry.setIndexNames(
    (0, "ERI-DNX-LINK-TEST-MIB", "hsTestLinkAddr"),
)
if mibBuilder.loadTexts:
    hsTestEntry.setStatus("current")
_HsTestLinkAddr_Type = LinkPortAddress
_HsTestLinkAddr_Object = MibTableColumn
hsTestLinkAddr = _HsTestLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 1),
    _HsTestLinkAddr_Type()
)
hsTestLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestLinkAddr.setStatus("current")
_HsTestResrcId_Type = Integer32
_HsTestResrcId_Object = MibTableColumn
hsTestResrcId = _HsTestResrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 2),
    _HsTestResrcId_Type()
)
hsTestResrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestResrcId.setStatus("current")


class _HsTestLinkState_Type(Integer32):
    """Custom type hsTestLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              8,
              16,
              255,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("carrierDrop", 16),
          ("clkEdgeErr", 8),
          ("fifo", 6),
          ("noConn", 255),
          ("ok", 0),
          ("oos", 65535),
          ("rxFifo", 2),
          ("txFifo", 4))
    )


_HsTestLinkState_Type.__name__ = "Integer32"
_HsTestLinkState_Object = MibTableColumn
hsTestLinkState = _HsTestLinkState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 3),
    _HsTestLinkState_Type()
)
hsTestLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestLinkState.setStatus("current")


class _HsTestLocalLoop_Type(Integer32):
    """Custom type hsTestLocalLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("off", 0))
    )


_HsTestLocalLoop_Type.__name__ = "Integer32"
_HsTestLocalLoop_Object = MibTableColumn
hsTestLocalLoop = _HsTestLocalLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 4),
    _HsTestLocalLoop_Type()
)
hsTestLocalLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsTestLocalLoop.setStatus("current")


class _HsTestRemoteLoop_Type(Integer32):
    """Custom type hsTestRemoteLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("loopDwnReq", 75),
          ("loopUpReq", 74),
          ("off", 10),
          ("remote", 11))
    )


_HsTestRemoteLoop_Type.__name__ = "Integer32"
_HsTestRemoteLoop_Object = MibTableColumn
hsTestRemoteLoop = _HsTestRemoteLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 5),
    _HsTestRemoteLoop_Type()
)
hsTestRemoteLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsTestRemoteLoop.setStatus("current")


class _HsTestBackplnLoop_Type(Integer32):
    """Custom type hsTestBackplnLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("loopBackplane", 21),
          ("loopOffBackplane", 20))
    )


_HsTestBackplnLoop_Type.__name__ = "Integer32"
_HsTestBackplnLoop_Object = MibTableColumn
hsTestBackplnLoop = _HsTestBackplnLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 6),
    _HsTestBackplnLoop_Type()
)
hsTestBackplnLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsTestBackplnLoop.setStatus("current")


class _HsTestBertState_Type(Integer32):
    """Custom type hsTestBertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              51,
              52,
              76,
              77,
              78,
              79)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 51),
          ("allZeros", 52),
          ("bert2047", 77),
          ("bert511", 78),
          ("bertOCU", 79),
          ("bertOff", 50),
          ("bertQRSS", 76))
    )


_HsTestBertState_Type.__name__ = "Integer32"
_HsTestBertState_Object = MibTableColumn
hsTestBertState = _HsTestBertState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 7),
    _HsTestBertState_Type()
)
hsTestBertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsTestBertState.setStatus("current")
_HsTestDuration_Type = Integer32
_HsTestDuration_Object = MibTableColumn
hsTestDuration = _HsTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 8),
    _HsTestDuration_Type()
)
hsTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestDuration.setStatus("current")
_HsTestLocESs_Type = Counter32
_HsTestLocESs_Object = MibTableColumn
hsTestLocESs = _HsTestLocESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 9),
    _HsTestLocESs_Type()
)
hsTestLocESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestLocESs.setStatus("current")
_HsTestRemESs_Type = Counter32
_HsTestRemESs_Object = MibTableColumn
hsTestRemESs = _HsTestRemESs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 10),
    _HsTestRemESs_Type()
)
hsTestRemESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestRemESs.setStatus("current")
_HsTestBitSpeed_Type = Integer32
_HsTestBitSpeed_Object = MibTableColumn
hsTestBitSpeed = _HsTestBitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 11),
    _HsTestBitSpeed_Type()
)
hsTestBitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestBitSpeed.setStatus("current")


class _HsTestCmdStatus_Type(Integer32):
    """Custom type hsTestCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              14,
              16,
              101,
              114,
              116,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-successful", 114),
          ("clearErrors", 14),
          ("err-field-cannot-be-set", 206),
          ("err-general-test-error", 200),
          ("err-invalid-bert-type", 203),
          ("err-invalid-loop-type", 202),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-link-not-connected", 204),
          ("err-link-not-in-service", 201),
          ("err-snmp-parse-failed", 500),
          ("err-test-in-progress", 205),
          ("insert-successful", 116),
          ("insertError", 16),
          ("ready-for-command", 0),
          ("update-successful", 101),
          ("updateTest", 1))
    )


_HsTestCmdStatus_Type.__name__ = "Integer32"
_HsTestCmdStatus_Object = MibTableColumn
hsTestCmdStatus = _HsTestCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 12),
    _HsTestCmdStatus_Type()
)
hsTestCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hsTestCmdStatus.setStatus("current")
_HsTestLocEFSs_Type = Counter32
_HsTestLocEFSs_Object = MibTableColumn
hsTestLocEFSs = _HsTestLocEFSs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 13),
    _HsTestLocEFSs_Type()
)
hsTestLocEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestLocEFSs.setStatus("current")
_HsTestLocUASs_Type = Counter32
_HsTestLocUASs_Object = MibTableColumn
hsTestLocUASs = _HsTestLocUASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 14),
    _HsTestLocUASs_Type()
)
hsTestLocUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestLocUASs.setStatus("current")
_HsTestLocASs_Type = Counter32
_HsTestLocASs_Object = MibTableColumn
hsTestLocASs = _HsTestLocASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 15),
    _HsTestLocASs_Type()
)
hsTestLocASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestLocASs.setStatus("current")
_HsTestLocESNonUASs_Type = Counter32
_HsTestLocESNonUASs_Object = MibTableColumn
hsTestLocESNonUASs = _HsTestLocESNonUASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 16),
    _HsTestLocESNonUASs_Type()
)
hsTestLocESNonUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestLocESNonUASs.setStatus("current")
_HsTestRemEFSs_Type = Counter32
_HsTestRemEFSs_Object = MibTableColumn
hsTestRemEFSs = _HsTestRemEFSs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 17),
    _HsTestRemEFSs_Type()
)
hsTestRemEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestRemEFSs.setStatus("current")
_HsTestRemUASs_Type = Counter32
_HsTestRemUASs_Object = MibTableColumn
hsTestRemUASs = _HsTestRemUASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 18),
    _HsTestRemUASs_Type()
)
hsTestRemUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestRemUASs.setStatus("current")
_HsTestRemASs_Type = Counter32
_HsTestRemASs_Object = MibTableColumn
hsTestRemASs = _HsTestRemASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 19),
    _HsTestRemASs_Type()
)
hsTestRemASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestRemASs.setStatus("current")
_HsTestRemESNonUASs_Type = Counter32
_HsTestRemESNonUASs_Object = MibTableColumn
hsTestRemESNonUASs = _HsTestRemESNonUASs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 2, 1, 1, 20),
    _HsTestRemESNonUASs_Type()
)
hsTestRemESNonUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsTestRemESNonUASs.setStatus("current")
_Dsx1Status_ObjectIdentity = ObjectIdentity
dsx1Status = _Dsx1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3)
)
_Dsx1StatusTable_Object = MibTable
dsx1StatusTable = _Dsx1StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1)
)
if mibBuilder.loadTexts:
    dsx1StatusTable.setStatus("current")
_Dsx1StatusEntry_Object = MibTableRow
dsx1StatusEntry = _Dsx1StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1)
)
dsx1StatusEntry.setIndexNames(
    (0, "ERI-DNX-LINK-TEST-MIB", "dsx1StatusAddr"),
)
if mibBuilder.loadTexts:
    dsx1StatusEntry.setStatus("current")
_Dsx1StatusAddr_Type = LinkPortAddress
_Dsx1StatusAddr_Object = MibTableColumn
dsx1StatusAddr = _Dsx1StatusAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 1),
    _Dsx1StatusAddr_Type()
)
dsx1StatusAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusAddr.setStatus("current")
_Dsx1StatusResrcId_Type = Integer32
_Dsx1StatusResrcId_Object = MibTableColumn
dsx1StatusResrcId = _Dsx1StatusResrcId_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 2),
    _Dsx1StatusResrcId_Type()
)
dsx1StatusResrcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusResrcId.setStatus("current")


class _Dsx1StatusState_Type(Integer32):
    """Custom type dsx1StatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              8,
              32,
              64,
              2048,
              4096,
              65535,
              2097152,
              4194304,
              6291456,
              8388608,
              1073741824,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ais", 8),
          ("cfa", 4096),
          ("errors", 2147483647),
          ("lof", 32),
          ("los", 64),
          ("ok", 0),
          ("oos", 65535),
          ("red", 2048),
          ("rxSlip", 4194304),
          ("sef", 8388608),
          ("slip", 6291456),
          ("txSlip", 2097152),
          ("underTest", 1073741824),
          ("yel", 2))
    )


_Dsx1StatusState_Type.__name__ = "Integer32"
_Dsx1StatusState_Object = MibTableColumn
dsx1StatusState = _Dsx1StatusState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 3),
    _Dsx1StatusState_Type()
)
dsx1StatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusState.setStatus("current")
_Dsx1StatusRedAlrmErrs_Type = Counter32
_Dsx1StatusRedAlrmErrs_Object = MibTableColumn
dsx1StatusRedAlrmErrs = _Dsx1StatusRedAlrmErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 4),
    _Dsx1StatusRedAlrmErrs_Type()
)
dsx1StatusRedAlrmErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusRedAlrmErrs.setStatus("current")
_Dsx1StatusRAIErrs_Type = Counter32
_Dsx1StatusRAIErrs_Object = MibTableColumn
dsx1StatusRAIErrs = _Dsx1StatusRAIErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 5),
    _Dsx1StatusRAIErrs_Type()
)
dsx1StatusRAIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusRAIErrs.setStatus("current")
_Dsx1StatusMFRAIErrs_Type = Counter32
_Dsx1StatusMFRAIErrs_Object = MibTableColumn
dsx1StatusMFRAIErrs = _Dsx1StatusMFRAIErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 6),
    _Dsx1StatusMFRAIErrs_Type()
)
dsx1StatusMFRAIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusMFRAIErrs.setStatus("current")
_Dsx1StatusLOSErrs_Type = Counter32
_Dsx1StatusLOSErrs_Object = MibTableColumn
dsx1StatusLOSErrs = _Dsx1StatusLOSErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 7),
    _Dsx1StatusLOSErrs_Type()
)
dsx1StatusLOSErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusLOSErrs.setStatus("current")
_Dsx1StatusAISErrs_Type = Counter32
_Dsx1StatusAISErrs_Object = MibTableColumn
dsx1StatusAISErrs = _Dsx1StatusAISErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 8),
    _Dsx1StatusAISErrs_Type()
)
dsx1StatusAISErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusAISErrs.setStatus("current")
_Dsx1StatusOOFErrs_Type = Counter32
_Dsx1StatusOOFErrs_Object = MibTableColumn
dsx1StatusOOFErrs = _Dsx1StatusOOFErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 9),
    _Dsx1StatusOOFErrs_Type()
)
dsx1StatusOOFErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusOOFErrs.setStatus("current")
_Dsx1StatusSEFErrs_Type = Counter32
_Dsx1StatusSEFErrs_Object = MibTableColumn
dsx1StatusSEFErrs = _Dsx1StatusSEFErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 10),
    _Dsx1StatusSEFErrs_Type()
)
dsx1StatusSEFErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusSEFErrs.setStatus("current")
_Dsx1StatusTransSlipErrs_Type = Counter32
_Dsx1StatusTransSlipErrs_Object = MibTableColumn
dsx1StatusTransSlipErrs = _Dsx1StatusTransSlipErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 11),
    _Dsx1StatusTransSlipErrs_Type()
)
dsx1StatusTransSlipErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusTransSlipErrs.setStatus("current")
_Dsx1StatusRecvSlipErrs_Type = Counter32
_Dsx1StatusRecvSlipErrs_Object = MibTableColumn
dsx1StatusRecvSlipErrs = _Dsx1StatusRecvSlipErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 12),
    _Dsx1StatusRecvSlipErrs_Type()
)
dsx1StatusRecvSlipErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusRecvSlipErrs.setStatus("current")
_Dsx1StatusCRCErrs_Type = Counter32
_Dsx1StatusCRCErrs_Object = MibTableColumn
dsx1StatusCRCErrs = _Dsx1StatusCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 13),
    _Dsx1StatusCRCErrs_Type()
)
dsx1StatusCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusCRCErrs.setStatus("current")
_Dsx1StatusBPVErrs_Type = Counter32
_Dsx1StatusBPVErrs_Object = MibTableColumn
dsx1StatusBPVErrs = _Dsx1StatusBPVErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 14),
    _Dsx1StatusBPVErrs_Type()
)
dsx1StatusBPVErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusBPVErrs.setStatus("current")
_Dsx1StatusFrameBitErrs_Type = Counter32
_Dsx1StatusFrameBitErrs_Object = MibTableColumn
dsx1StatusFrameBitErrs = _Dsx1StatusFrameBitErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 15),
    _Dsx1StatusFrameBitErrs_Type()
)
dsx1StatusFrameBitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusFrameBitErrs.setStatus("current")
_Dsx1StatusFarEndBlockErrs_Type = Counter32
_Dsx1StatusFarEndBlockErrs_Object = MibTableColumn
dsx1StatusFarEndBlockErrs = _Dsx1StatusFarEndBlockErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 16),
    _Dsx1StatusFarEndBlockErrs_Type()
)
dsx1StatusFarEndBlockErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusFarEndBlockErrs.setStatus("current")
_Dsx1StatusTrunkCondition_Type = DataSwitch
_Dsx1StatusTrunkCondition_Object = MibTableColumn
dsx1StatusTrunkCondition = _Dsx1StatusTrunkCondition_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 17),
    _Dsx1StatusTrunkCondition_Type()
)
dsx1StatusTrunkCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusTrunkCondition.setStatus("current")


class _Dsx1StatusInsErrMode_Type(Integer32):
    """Custom type dsx1StatusInsErrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ais-unframed-all-ones", 16),
          ("allErrors", 9),
          ("bert-error", 3),
          ("bit-slip", 4),
          ("cas-multiframe", 1),
          ("crc", 6),
          ("fas-inverted", 12),
          ("fbit", 7),
          ("frame-alignment", 5),
          ("line-code-violation", 8),
          ("multiframe", 2),
          ("nfas-bit2-inverted", 13),
          ("not-applicable", 0),
          ("rai", 14),
          ("ts16-ais", 15),
          ("ybit", 11),
          ("yellow-alarm", 10))
    )


_Dsx1StatusInsErrMode_Type.__name__ = "Integer32"
_Dsx1StatusInsErrMode_Object = MibTableColumn
dsx1StatusInsErrMode = _Dsx1StatusInsErrMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 18),
    _Dsx1StatusInsErrMode_Type()
)
dsx1StatusInsErrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1StatusInsErrMode.setStatus("current")


class _Dsx1StatusCmdStatus_Type(Integer32):
    """Custom type dsx1StatusCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              14,
              16,
              101,
              114,
              116,
              200,
              201,
              204,
              205,
              206,
              207,
              208,
              211,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-successful", 114),
          ("clearErrors", 14),
          ("err-field-cannot-be-set", 206),
          ("err-general-status-error", 200),
          ("err-invalid-command", 208),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-link-in-clear-mode", 204),
          ("err-link-not-connected", 207),
          ("err-link-not-in-service", 201),
          ("err-link-not-in-test", 211),
          ("err-snmp-parse-failed", 500),
          ("err-test-in-progress", 205),
          ("insert-successful", 116),
          ("insertError", 16),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )


_Dsx1StatusCmdStatus_Type.__name__ = "Integer32"
_Dsx1StatusCmdStatus_Object = MibTableColumn
dsx1StatusCmdStatus = _Dsx1StatusCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 19),
    _Dsx1StatusCmdStatus_Type()
)
dsx1StatusCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1StatusCmdStatus.setStatus("current")
_Dsx1StatusRcvNationalBits_Type = OneByteField
_Dsx1StatusRcvNationalBits_Object = MibTableColumn
dsx1StatusRcvNationalBits = _Dsx1StatusRcvNationalBits_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 5, 3, 1, 1, 20),
    _Dsx1StatusRcvNationalBits_Type()
)
dsx1StatusRcvNationalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1StatusRcvNationalBits.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-LINK-TEST-MIB",
    **{"UserDefFormat": UserDefFormat,
       "diagnostics": diagnostics,
       "dsx1Test": dsx1Test,
       "dsx1TestTable": dsx1TestTable,
       "dsx1TestEntry": dsx1TestEntry,
       "dsx1TestLinkAddr": dsx1TestLinkAddr,
       "dsx1TestResrcId": dsx1TestResrcId,
       "dsx1TestLinkState": dsx1TestLinkState,
       "dsx1TestLinkLoop": dsx1TestLinkLoop,
       "dsx1TestBackplnLoop": dsx1TestBackplnLoop,
       "dsx1TestBertState": dsx1TestBertState,
       "dsx1TestDuration": dsx1TestDuration,
       "dsx1TestBitErrs": dsx1TestBitErrs,
       "dsx1TestESs": dsx1TestESs,
       "dsx1TestRemoteESs": dsx1TestRemoteESs,
       "dsx1TestErrFreeSecs": dsx1TestErrFreeSecs,
       "dsx1TestSESs": dsx1TestSESs,
       "dsx1TestUASs": dsx1TestUASs,
       "dsx1TestASs": dsx1TestASs,
       "dsx1TestESNonUASs": dsx1TestESNonUASs,
       "dsx1TestSevereError": dsx1TestSevereError,
       "dsx1TestBitSpeed": dsx1TestBitSpeed,
       "dsx1TestCmdStatus": dsx1TestCmdStatus,
       "dsx1TestInsErrMode": dsx1TestInsErrMode,
       "dsx1TestUsrLoopUnframed": dsx1TestUsrLoopUnframed,
       "dsx1TestUsrDefLoop": dsx1TestUsrDefLoop,
       "hsTest": hsTest,
       "hsTestTable": hsTestTable,
       "hsTestEntry": hsTestEntry,
       "hsTestLinkAddr": hsTestLinkAddr,
       "hsTestResrcId": hsTestResrcId,
       "hsTestLinkState": hsTestLinkState,
       "hsTestLocalLoop": hsTestLocalLoop,
       "hsTestRemoteLoop": hsTestRemoteLoop,
       "hsTestBackplnLoop": hsTestBackplnLoop,
       "hsTestBertState": hsTestBertState,
       "hsTestDuration": hsTestDuration,
       "hsTestLocESs": hsTestLocESs,
       "hsTestRemESs": hsTestRemESs,
       "hsTestBitSpeed": hsTestBitSpeed,
       "hsTestCmdStatus": hsTestCmdStatus,
       "hsTestLocEFSs": hsTestLocEFSs,
       "hsTestLocUASs": hsTestLocUASs,
       "hsTestLocASs": hsTestLocASs,
       "hsTestLocESNonUASs": hsTestLocESNonUASs,
       "hsTestRemEFSs": hsTestRemEFSs,
       "hsTestRemUASs": hsTestRemUASs,
       "hsTestRemASs": hsTestRemASs,
       "hsTestRemESNonUASs": hsTestRemESNonUASs,
       "dsx1Status": dsx1Status,
       "dsx1StatusTable": dsx1StatusTable,
       "dsx1StatusEntry": dsx1StatusEntry,
       "dsx1StatusAddr": dsx1StatusAddr,
       "dsx1StatusResrcId": dsx1StatusResrcId,
       "dsx1StatusState": dsx1StatusState,
       "dsx1StatusRedAlrmErrs": dsx1StatusRedAlrmErrs,
       "dsx1StatusRAIErrs": dsx1StatusRAIErrs,
       "dsx1StatusMFRAIErrs": dsx1StatusMFRAIErrs,
       "dsx1StatusLOSErrs": dsx1StatusLOSErrs,
       "dsx1StatusAISErrs": dsx1StatusAISErrs,
       "dsx1StatusOOFErrs": dsx1StatusOOFErrs,
       "dsx1StatusSEFErrs": dsx1StatusSEFErrs,
       "dsx1StatusTransSlipErrs": dsx1StatusTransSlipErrs,
       "dsx1StatusRecvSlipErrs": dsx1StatusRecvSlipErrs,
       "dsx1StatusCRCErrs": dsx1StatusCRCErrs,
       "dsx1StatusBPVErrs": dsx1StatusBPVErrs,
       "dsx1StatusFrameBitErrs": dsx1StatusFrameBitErrs,
       "dsx1StatusFarEndBlockErrs": dsx1StatusFarEndBlockErrs,
       "dsx1StatusTrunkCondition": dsx1StatusTrunkCondition,
       "dsx1StatusInsErrMode": dsx1StatusInsErrMode,
       "dsx1StatusCmdStatus": dsx1StatusCmdStatus,
       "dsx1StatusRcvNationalBits": dsx1StatusRcvNationalBits,
       "eriDNXLinkTestMIB": eriDNXLinkTestMIB}
)
