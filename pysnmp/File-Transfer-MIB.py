# SNMP MIB module (File-Transfer-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/File-Transfer-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:46 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniFT_ObjectIdentity = ObjectIdentity
sniFT = _SniFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18)
)
_SniFTStartandStop_ObjectIdentity = ObjectIdentity
sniFTStartandStop = _SniFTStartandStop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 1)
)


class _FtStartandStop_Type(Integer32):
    """Custom type ftStartandStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 4),
          ("on", 3),
          ("start", 1),
          ("stop", 2),
          ("undefined", 255))
    )


_FtStartandStop_Type.__name__ = "Integer32"
_FtStartandStop_Object = MibScalar
ftStartandStop = _FtStartandStop_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 1, 1),
    _FtStartandStop_Type()
)
ftStartandStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftStartandStop.setStatus("mandatory")


class _FtStartandStopFTAM_Type(Integer32):
    """Custom type ftStartandStopFTAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-yet", 5),
          ("off", 4),
          ("on", 3),
          ("start", 1),
          ("stop", 2),
          ("undefined", 255))
    )


_FtStartandStopFTAM_Type.__name__ = "Integer32"
_FtStartandStopFTAM_Object = MibScalar
ftStartandStopFTAM = _FtStartandStopFTAM_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 1, 2),
    _FtStartandStopFTAM_Type()
)
ftStartandStopFTAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftStartandStopFTAM.setStatus("mandatory")
_SniFTSysParam_ObjectIdentity = ObjectIdentity
sniFTSysParam = _SniFTSysParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2)
)


class _FtSysparVersion_Type(DisplayString):
    """Custom type ftSysparVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FtSysparVersion_Type.__name__ = "DisplayString"
_FtSysparVersion_Object = MibScalar
ftSysparVersion = _FtSysparVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 1),
    _FtSysparVersion_Type()
)
ftSysparVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftSysparVersion.setStatus("mandatory")


class _FtSysparTransportUnitSize_Type(Integer32):
    """Custom type ftSysparTransportUnitSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 32767),
    )


_FtSysparTransportUnitSize_Type.__name__ = "Integer32"
_FtSysparTransportUnitSize_Object = MibScalar
ftSysparTransportUnitSize = _FtSysparTransportUnitSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 2),
    _FtSysparTransportUnitSize_Type()
)
ftSysparTransportUnitSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparTransportUnitSize.setStatus("mandatory")


class _FtSysparTaskLimit_Type(Integer32):
    """Custom type ftSysparTaskLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FtSysparTaskLimit_Type.__name__ = "Integer32"
_FtSysparTaskLimit_Object = MibScalar
ftSysparTaskLimit = _FtSysparTaskLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 3),
    _FtSysparTaskLimit_Type()
)
ftSysparTaskLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparTaskLimit.setStatus("mandatory")


class _FtSysparConnectionLimit_Type(Integer32):
    """Custom type ftSysparConnectionLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FtSysparConnectionLimit_Type.__name__ = "Integer32"
_FtSysparConnectionLimit_Object = MibScalar
ftSysparConnectionLimit = _FtSysparConnectionLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 4),
    _FtSysparConnectionLimit_Type()
)
ftSysparConnectionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparConnectionLimit.setStatus("mandatory")


class _FtSysparRequestWaitLevel_Type(Integer32):
    """Custom type ftSysparRequestWaitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2500),
    )


_FtSysparRequestWaitLevel_Type.__name__ = "Integer32"
_FtSysparRequestWaitLevel_Object = MibScalar
ftSysparRequestWaitLevel = _FtSysparRequestWaitLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 5),
    _FtSysparRequestWaitLevel_Type()
)
ftSysparRequestWaitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparRequestWaitLevel.setStatus("mandatory")


class _FtSysparPartnerCheck_Type(Integer32):
    """Custom type ftSysparPartnerCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("std", 1),
          ("transport-address", 2))
    )


_FtSysparPartnerCheck_Type.__name__ = "Integer32"
_FtSysparPartnerCheck_Object = MibScalar
ftSysparPartnerCheck = _FtSysparPartnerCheck_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 6),
    _FtSysparPartnerCheck_Type()
)
ftSysparPartnerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparPartnerCheck.setStatus("mandatory")


class _FtSysparMaxOSP_Type(Integer32):
    """Custom type ftSysparMaxOSP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FtSysparMaxOSP_Type.__name__ = "Integer32"
_FtSysparMaxOSP_Object = MibScalar
ftSysparMaxOSP = _FtSysparMaxOSP_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 7),
    _FtSysparMaxOSP_Type()
)
ftSysparMaxOSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparMaxOSP.setStatus("mandatory")


class _FtSysparMaxISP_Type(Integer32):
    """Custom type ftSysparMaxISP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FtSysparMaxISP_Type.__name__ = "Integer32"
_FtSysparMaxISP_Object = MibScalar
ftSysparMaxISP = _FtSysparMaxISP_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 8),
    _FtSysparMaxISP_Type()
)
ftSysparMaxISP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparMaxISP.setStatus("mandatory")


class _FtSysparProcessorName_Type(DisplayString):
    """Custom type ftSysparProcessorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FtSysparProcessorName_Type.__name__ = "DisplayString"
_FtSysparProcessorName_Object = MibScalar
ftSysparProcessorName = _FtSysparProcessorName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 9),
    _FtSysparProcessorName_Type()
)
ftSysparProcessorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparProcessorName.setStatus("mandatory")


class _FtSysparStationName_Type(DisplayString):
    """Custom type ftSysparStationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FtSysparStationName_Type.__name__ = "DisplayString"
_FtSysparStationName_Object = MibScalar
ftSysparStationName = _FtSysparStationName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 10),
    _FtSysparStationName_Type()
)
ftSysparStationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparStationName.setStatus("mandatory")


class _FtSysparCode_Type(Integer32):
    """Custom type ftSysparCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              7,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("iso8859-1", 1),
          ("iso8859-2", 2),
          ("iso8859-5", 5),
          ("iso8859-6", 6),
          ("iso8859-7", 7),
          ("iso8859-9", 9),
          ("undefined", 255))
    )


_FtSysparCode_Type.__name__ = "Integer32"
_FtSysparCode_Object = MibScalar
ftSysparCode = _FtSysparCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 11),
    _FtSysparCode_Type()
)
ftSysparCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparCode.setStatus("mandatory")


class _FtSysparMaxInboundReqs_Type(Integer32):
    """Custom type ftSysparMaxInboundReqs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_FtSysparMaxInboundReqs_Type.__name__ = "Integer32"
_FtSysparMaxInboundReqs_Object = MibScalar
ftSysparMaxInboundReqs = _FtSysparMaxInboundReqs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 12),
    _FtSysparMaxInboundReqs_Type()
)
ftSysparMaxInboundReqs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparMaxInboundReqs.setStatus("mandatory")


class _FtSysparMaxLifeTime_Type(Integer32):
    """Custom type ftSysparMaxLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_FtSysparMaxLifeTime_Type.__name__ = "Integer32"
_FtSysparMaxLifeTime_Object = MibScalar
ftSysparMaxLifeTime = _FtSysparMaxLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 2, 13),
    _FtSysparMaxLifeTime_Type()
)
ftSysparMaxLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftSysparMaxLifeTime.setStatus("mandatory")
_SniFTEncryptKey_ObjectIdentity = ObjectIdentity
sniFTEncryptKey = _SniFTEncryptKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 3)
)


class _FtEncryptKey_Type(Integer32):
    """Custom type ftEncryptKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("create-new-key", 1)
    )


_FtEncryptKey_Type.__name__ = "Integer32"
_FtEncryptKey_Object = MibScalar
ftEncryptKey = _FtEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 3, 1),
    _FtEncryptKey_Type()
)
ftEncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftEncryptKey.setStatus("mandatory")
_SniFTStatistics_ObjectIdentity = ObjectIdentity
sniFTStatistics = _SniFTStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 4)
)
_FtStatSuspend_Type = Integer32
_FtStatSuspend_Object = MibScalar
ftStatSuspend = _FtStatSuspend_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 4, 1),
    _FtStatSuspend_Type()
)
ftStatSuspend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftStatSuspend.setStatus("mandatory")
_FtStatLocked_Type = Integer32
_FtStatLocked_Object = MibScalar
ftStatLocked = _FtStatLocked_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 4, 2),
    _FtStatLocked_Type()
)
ftStatLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftStatLocked.setStatus("mandatory")
_FtStatWait_Type = Integer32
_FtStatWait_Object = MibScalar
ftStatWait = _FtStatWait_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 4, 3),
    _FtStatWait_Type()
)
ftStatWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftStatWait.setStatus("mandatory")
_FtStatActive_Type = Integer32
_FtStatActive_Object = MibScalar
ftStatActive = _FtStatActive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 4, 4),
    _FtStatActive_Type()
)
ftStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftStatActive.setStatus("mandatory")
_FtStatCanceled_Type = Integer32
_FtStatCanceled_Object = MibScalar
ftStatCanceled = _FtStatCanceled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 4, 5),
    _FtStatCanceled_Type()
)
ftStatCanceled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftStatCanceled.setStatus("mandatory")
_FtStatFinished_Type = Integer32
_FtStatFinished_Object = MibScalar
ftStatFinished = _FtStatFinished_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 4, 6),
    _FtStatFinished_Type()
)
ftStatFinished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftStatFinished.setStatus("mandatory")
_FtStatHold_Type = Integer32
_FtStatHold_Object = MibScalar
ftStatHold = _FtStatHold_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 4, 7),
    _FtStatHold_Type()
)
ftStatHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftStatHold.setStatus("mandatory")
_FtStatLocalReqs_Type = Integer32
_FtStatLocalReqs_Object = MibScalar
ftStatLocalReqs = _FtStatLocalReqs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 4, 8),
    _FtStatLocalReqs_Type()
)
ftStatLocalReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftStatLocalReqs.setStatus("mandatory")
_FtStatRemoteReqs_Type = Integer32
_FtStatRemoteReqs_Object = MibScalar
ftStatRemoteReqs = _FtStatRemoteReqs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 4, 9),
    _FtStatRemoteReqs_Type()
)
ftStatRemoteReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftStatRemoteReqs.setStatus("mandatory")
_SniFTDiagnostics_ObjectIdentity = ObjectIdentity
sniFTDiagnostics = _SniFTDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 5)
)


class _FtDiagStatus_Type(Integer32):
    """Custom type ftDiagStatus based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              255)
        )
    )
    namedValues = NamedValues(
        *(("mmnn", 27),
          ("mmns", 29),
          ("mmsn", 28),
          ("mmss", 30),
          ("mnn", 4),
          ("mns", 13),
          ("msn", 12),
          ("mss", 14),
          ("nnn", 5),
          ("nns", 16),
          ("nsn", 15),
          ("nss", 17),
          ("off", 1),
          ("on", 18),
          ("pmnn", 23),
          ("pmns", 25),
          ("pmsn", 24),
          ("pmss", 26),
          ("pnn", 3),
          ("pns", 10),
          ("psn", 9),
          ("pss", 11),
          ("smnn", 19),
          ("smns", 21),
          ("smsn", 20),
          ("smss", 22),
          ("snn", 2),
          ("sns", 7),
          ("ssn", 6),
          ("sss", 8),
          ("undefined", 255))
    )


_FtDiagStatus_Type.__name__ = "Integer32"
_FtDiagStatus_Object = MibScalar
ftDiagStatus = _FtDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 5, 1),
    _FtDiagStatus_Type()
)
ftDiagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftDiagStatus.setStatus("mandatory")
_SniFTTraps_ObjectIdentity = ObjectIdentity
sniFTTraps = _SniFTTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6)
)
_SniFTPollInterval_ObjectIdentity = ObjectIdentity
sniFTPollInterval = _SniFTPollInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 7)
)
_FtPollInterval_Type = Integer32
_FtPollInterval_Object = MibScalar
ftPollInterval = _FtPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 7, 1),
    _FtPollInterval_Type()
)
ftPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftPollInterval.setStatus("mandatory")
_SniFTPartners_ObjectIdentity = ObjectIdentity
sniFTPartners = _SniFTPartners_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 8)
)
_FtPartnerTable_Object = MibTable
ftPartnerTable = _FtPartnerTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 8, 1)
)
if mibBuilder.loadTexts:
    ftPartnerTable.setStatus("mandatory")
_FtPartnerEntry_Object = MibTableRow
ftPartnerEntry = _FtPartnerEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 8, 1, 1)
)
ftPartnerEntry.setIndexNames(
    (0, "File-Transfer-MIB", "ftPartnerName"),
)
if mibBuilder.loadTexts:
    ftPartnerEntry.setStatus("mandatory")


class _FtPartnerName_Type(DisplayString):
    """Custom type ftPartnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FtPartnerName_Type.__name__ = "DisplayString"
_FtPartnerName_Object = MibTableColumn
ftPartnerName = _FtPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 8, 1, 1, 1),
    _FtPartnerName_Type()
)
ftPartnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPartnerName.setStatus("mandatory")


class _FtPartnerType_Type(Integer32):
    """Custom type ftPartnerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftam", 2),
          ("openft", 1))
    )


_FtPartnerType_Type.__name__ = "Integer32"
_FtPartnerType_Object = MibTableColumn
ftPartnerType = _FtPartnerType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 8, 1, 1, 2),
    _FtPartnerType_Type()
)
ftPartnerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPartnerType.setStatus("mandatory")


class _FtPartnerState_Type(Integer32):
    """Custom type ftPartnerState based on Integer32"""
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
        *(("act", 1),
          ("adeact", 6),
          ("ainact", 7),
          ("inact", 2),
          ("lunk", 4),
          ("nocon", 3),
          ("runk", 5))
    )


_FtPartnerState_Type.__name__ = "Integer32"
_FtPartnerState_Object = MibTableColumn
ftPartnerState = _FtPartnerState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 8, 1, 1, 3),
    _FtPartnerState_Type()
)
ftPartnerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftPartnerState.setStatus("mandatory")


class _FtPartnerNetworkAddr_Type(DisplayString):
    """Custom type ftPartnerNetworkAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FtPartnerNetworkAddr_Type.__name__ = "DisplayString"
_FtPartnerNetworkAddr_Object = MibTableColumn
ftPartnerNetworkAddr = _FtPartnerNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 8, 1, 1, 4),
    _FtPartnerNetworkAddr_Type()
)
ftPartnerNetworkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPartnerNetworkAddr.setStatus("mandatory")


class _FtPartnerTransportSel_Type(DisplayString):
    """Custom type ftPartnerTransportSel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_FtPartnerTransportSel_Type.__name__ = "DisplayString"
_FtPartnerTransportSel_Object = MibTableColumn
ftPartnerTransportSel = _FtPartnerTransportSel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 8, 1, 1, 5),
    _FtPartnerTransportSel_Type()
)
ftPartnerTransportSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPartnerTransportSel.setStatus("mandatory")


class _FtPartnerSessionSel_Type(DisplayString):
    """Custom type ftPartnerSessionSel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_FtPartnerSessionSel_Type.__name__ = "DisplayString"
_FtPartnerSessionSel_Object = MibTableColumn
ftPartnerSessionSel = _FtPartnerSessionSel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 8, 1, 1, 6),
    _FtPartnerSessionSel_Type()
)
ftPartnerSessionSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPartnerSessionSel.setStatus("mandatory")


class _FtPartnerPresentationSel_Type(DisplayString):
    """Custom type ftPartnerPresentationSel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_FtPartnerPresentationSel_Type.__name__ = "DisplayString"
_FtPartnerPresentationSel_Object = MibTableColumn
ftPartnerPresentationSel = _FtPartnerPresentationSel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 8, 1, 1, 7),
    _FtPartnerPresentationSel_Type()
)
ftPartnerPresentationSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftPartnerPresentationSel.setStatus("mandatory")
_SniFTTrapData_ObjectIdentity = ObjectIdentity
sniFTTrapData = _SniFTTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 9)
)
_FtRequestID_Type = Integer32
_FtRequestID_Object = MibScalar
ftRequestID = _FtRequestID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 9, 1),
    _FtRequestID_Type()
)
ftRequestID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ftRequestID.setStatus("mandatory")


class _FtRequestInitiator_Type(Integer32):
    """Custom type ftRequestInitiator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_FtRequestInitiator_Type.__name__ = "Integer32"
_FtRequestInitiator_Object = MibScalar
ftRequestInitiator = _FtRequestInitiator_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 9, 2),
    _FtRequestInitiator_Type()
)
ftRequestInitiator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ftRequestInitiator.setStatus("mandatory")


class _FtRequestPartnerName_Type(DisplayString):
    """Custom type ftRequestPartnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FtRequestPartnerName_Type.__name__ = "DisplayString"
_FtRequestPartnerName_Object = MibScalar
ftRequestPartnerName = _FtRequestPartnerName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 9, 3),
    _FtRequestPartnerName_Type()
)
ftRequestPartnerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ftRequestPartnerName.setStatus("mandatory")


class _FtRequestUserID_Type(DisplayString):
    """Custom type ftRequestUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FtRequestUserID_Type.__name__ = "DisplayString"
_FtRequestUserID_Object = MibScalar
ftRequestUserID = _FtRequestUserID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 9, 4),
    _FtRequestUserID_Type()
)
ftRequestUserID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ftRequestUserID.setStatus("mandatory")


class _FtRequestFileName_Type(DisplayString):
    """Custom type ftRequestFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 221),
    )


_FtRequestFileName_Type.__name__ = "DisplayString"
_FtRequestFileName_Object = MibScalar
ftRequestFileName = _FtRequestFileName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 9, 5),
    _FtRequestFileName_Type()
)
ftRequestFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ftRequestFileName.setStatus("mandatory")


class _FtRequestError_Type(DisplayString):
    """Custom type ftRequestError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_FtRequestError_Type.__name__ = "DisplayString"
_FtRequestError_Object = MibScalar
ftRequestError = _FtRequestError_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 9, 6),
    _FtRequestError_Type()
)
ftRequestError.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ftRequestError.setStatus("mandatory")
_SniFTTrapSwitches_ObjectIdentity = ObjectIdentity
sniFTTrapSwitches = _SniFTTrapSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 10)
)


class _FtTrapsSubsystemState_Type(Integer32):
    """Custom type ftTrapsSubsystemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FtTrapsSubsystemState_Type.__name__ = "Integer32"
_FtTrapsSubsystemState_Object = MibScalar
ftTrapsSubsystemState = _FtTrapsSubsystemState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 10, 1),
    _FtTrapsSubsystemState_Type()
)
ftTrapsSubsystemState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftTrapsSubsystemState.setStatus("mandatory")


class _FtTrapsFTState_Type(Integer32):
    """Custom type ftTrapsFTState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FtTrapsFTState_Type.__name__ = "Integer32"
_FtTrapsFTState_Object = MibScalar
ftTrapsFTState = _FtTrapsFTState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 10, 2),
    _FtTrapsFTState_Type()
)
ftTrapsFTState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftTrapsFTState.setStatus("mandatory")


class _FtTrapsPartState_Type(Integer32):
    """Custom type ftTrapsPartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FtTrapsPartState_Type.__name__ = "Integer32"
_FtTrapsPartState_Object = MibScalar
ftTrapsPartState = _FtTrapsPartState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 10, 3),
    _FtTrapsPartState_Type()
)
ftTrapsPartState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftTrapsPartState.setStatus("mandatory")


class _FtTrapsPartnerUnreachable_Type(Integer32):
    """Custom type ftTrapsPartnerUnreachable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FtTrapsPartnerUnreachable_Type.__name__ = "Integer32"
_FtTrapsPartnerUnreachable_Object = MibScalar
ftTrapsPartnerUnreachable = _FtTrapsPartnerUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 10, 4),
    _FtTrapsPartnerUnreachable_Type()
)
ftTrapsPartnerUnreachable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftTrapsPartnerUnreachable.setStatus("mandatory")


class _FtTrapsRequestQueueState_Type(Integer32):
    """Custom type ftTrapsRequestQueueState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FtTrapsRequestQueueState_Type.__name__ = "Integer32"
_FtTrapsRequestQueueState_Object = MibScalar
ftTrapsRequestQueueState = _FtTrapsRequestQueueState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 10, 5),
    _FtTrapsRequestQueueState_Type()
)
ftTrapsRequestQueueState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftTrapsRequestQueueState.setStatus("mandatory")


class _FtTrapsTransSucc_Type(Integer32):
    """Custom type ftTrapsTransSucc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FtTrapsTransSucc_Type.__name__ = "Integer32"
_FtTrapsTransSucc_Object = MibScalar
ftTrapsTransSucc = _FtTrapsTransSucc_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 10, 6),
    _FtTrapsTransSucc_Type()
)
ftTrapsTransSucc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftTrapsTransSucc.setStatus("mandatory")


class _FtTrapsTransFail_Type(Integer32):
    """Custom type ftTrapsTransFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FtTrapsTransFail_Type.__name__ = "Integer32"
_FtTrapsTransFail_Object = MibScalar
ftTrapsTransFail = _FtTrapsTransFail_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 10, 7),
    _FtTrapsTransFail_Type()
)
ftTrapsTransFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftTrapsTransFail.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ftStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 1)
)
if mibBuilder.loadTexts:
    ftStopTrap.setStatus(
        ""
    )

ftMaxRequestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 2)
)
if mibBuilder.loadTexts:
    ftMaxRequestTrap.setStatus(
        ""
    )

ftErrorLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 3)
)
if mibBuilder.loadTexts:
    ftErrorLimitTrap.setStatus(
        ""
    )

ftPartnerStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 4)
)
ftPartnerStateTrap.setObjects(
      *(("File-Transfer-MIB", "ftPartnerName"),
        ("File-Transfer-MIB", "ftPartnerState"))
)
if mibBuilder.loadTexts:
    ftPartnerStateTrap.setStatus(
        ""
    )

ftPartnerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 5)
)
ftPartnerUnreachableTrap.setObjects(
    ("File-Transfer-MIB", "ftPartnerName")
)
if mibBuilder.loadTexts:
    ftPartnerUnreachableTrap.setStatus(
        ""
    )

ftStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 6)
)
if mibBuilder.loadTexts:
    ftStartTrap.setStatus(
        ""
    )

ftRequestQueueUpperLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 7)
)
if mibBuilder.loadTexts:
    ftRequestQueueUpperLimitTrap.setStatus(
        ""
    )

ftRequestQueueLowerLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 8)
)
if mibBuilder.loadTexts:
    ftRequestQueueLowerLimitTrap.setStatus(
        ""
    )

ftRequestSuccessfulTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 9)
)
ftRequestSuccessfulTrap.setObjects(
      *(("File-Transfer-MIB", "ftRequestInitiator"),
        ("File-Transfer-MIB", "ftRequestID"),
        ("File-Transfer-MIB", "ftRequestPartnerName"),
        ("File-Transfer-MIB", "ftRequestUserID"),
        ("File-Transfer-MIB", "ftRequestFileName"))
)
if mibBuilder.loadTexts:
    ftRequestSuccessfulTrap.setStatus(
        ""
    )

ftRequestErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 10)
)
ftRequestErrorTrap.setObjects(
      *(("File-Transfer-MIB", "ftRequestInitiator"),
        ("File-Transfer-MIB", "ftRequestID"),
        ("File-Transfer-MIB", "ftRequestPartnerName"),
        ("File-Transfer-MIB", "ftRequestUserID"),
        ("File-Transfer-MIB", "ftRequestFileName"),
        ("File-Transfer-MIB", "ftRequestError"))
)
if mibBuilder.loadTexts:
    ftRequestErrorTrap.setStatus(
        ""
    )

ftSubsystemStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 11)
)
if mibBuilder.loadTexts:
    ftSubsystemStartTrap.setStatus(
        ""
    )

ftSubsystemStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 18, 6, 0, 12)
)
if mibBuilder.loadTexts:
    ftSubsystemStopTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "File-Transfer-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniFT": sniFT,
       "sniFTStartandStop": sniFTStartandStop,
       "ftStartandStop": ftStartandStop,
       "ftStartandStopFTAM": ftStartandStopFTAM,
       "sniFTSysParam": sniFTSysParam,
       "ftSysparVersion": ftSysparVersion,
       "ftSysparTransportUnitSize": ftSysparTransportUnitSize,
       "ftSysparTaskLimit": ftSysparTaskLimit,
       "ftSysparConnectionLimit": ftSysparConnectionLimit,
       "ftSysparRequestWaitLevel": ftSysparRequestWaitLevel,
       "ftSysparPartnerCheck": ftSysparPartnerCheck,
       "ftSysparMaxOSP": ftSysparMaxOSP,
       "ftSysparMaxISP": ftSysparMaxISP,
       "ftSysparProcessorName": ftSysparProcessorName,
       "ftSysparStationName": ftSysparStationName,
       "ftSysparCode": ftSysparCode,
       "ftSysparMaxInboundReqs": ftSysparMaxInboundReqs,
       "ftSysparMaxLifeTime": ftSysparMaxLifeTime,
       "sniFTEncryptKey": sniFTEncryptKey,
       "ftEncryptKey": ftEncryptKey,
       "sniFTStatistics": sniFTStatistics,
       "ftStatSuspend": ftStatSuspend,
       "ftStatLocked": ftStatLocked,
       "ftStatWait": ftStatWait,
       "ftStatActive": ftStatActive,
       "ftStatCanceled": ftStatCanceled,
       "ftStatFinished": ftStatFinished,
       "ftStatHold": ftStatHold,
       "ftStatLocalReqs": ftStatLocalReqs,
       "ftStatRemoteReqs": ftStatRemoteReqs,
       "sniFTDiagnostics": sniFTDiagnostics,
       "ftDiagStatus": ftDiagStatus,
       "sniFTTraps": sniFTTraps,
       "ftStopTrap": ftStopTrap,
       "ftMaxRequestTrap": ftMaxRequestTrap,
       "ftErrorLimitTrap": ftErrorLimitTrap,
       "ftPartnerStateTrap": ftPartnerStateTrap,
       "ftPartnerUnreachableTrap": ftPartnerUnreachableTrap,
       "ftStartTrap": ftStartTrap,
       "ftRequestQueueUpperLimitTrap": ftRequestQueueUpperLimitTrap,
       "ftRequestQueueLowerLimitTrap": ftRequestQueueLowerLimitTrap,
       "ftRequestSuccessfulTrap": ftRequestSuccessfulTrap,
       "ftRequestErrorTrap": ftRequestErrorTrap,
       "ftSubsystemStartTrap": ftSubsystemStartTrap,
       "ftSubsystemStopTrap": ftSubsystemStopTrap,
       "sniFTPollInterval": sniFTPollInterval,
       "ftPollInterval": ftPollInterval,
       "sniFTPartners": sniFTPartners,
       "ftPartnerTable": ftPartnerTable,
       "ftPartnerEntry": ftPartnerEntry,
       "ftPartnerName": ftPartnerName,
       "ftPartnerType": ftPartnerType,
       "ftPartnerState": ftPartnerState,
       "ftPartnerNetworkAddr": ftPartnerNetworkAddr,
       "ftPartnerTransportSel": ftPartnerTransportSel,
       "ftPartnerSessionSel": ftPartnerSessionSel,
       "ftPartnerPresentationSel": ftPartnerPresentationSel,
       "sniFTTrapData": sniFTTrapData,
       "ftRequestID": ftRequestID,
       "ftRequestInitiator": ftRequestInitiator,
       "ftRequestPartnerName": ftRequestPartnerName,
       "ftRequestUserID": ftRequestUserID,
       "ftRequestFileName": ftRequestFileName,
       "ftRequestError": ftRequestError,
       "sniFTTrapSwitches": sniFTTrapSwitches,
       "ftTrapsSubsystemState": ftTrapsSubsystemState,
       "ftTrapsFTState": ftTrapsFTState,
       "ftTrapsPartState": ftTrapsPartState,
       "ftTrapsPartnerUnreachable": ftTrapsPartnerUnreachable,
       "ftTrapsRequestQueueState": ftTrapsRequestQueueState,
       "ftTrapsTransSucc": ftTrapsTransSucc,
       "ftTrapsTransFail": ftTrapsTransFail}
)
