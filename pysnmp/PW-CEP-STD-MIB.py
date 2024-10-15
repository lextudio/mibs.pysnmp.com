# SNMP MIB module (PW-CEP-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PW-CEP-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:08 2024
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

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfTimeElapsed,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfTimeElapsed",
    "HCPerfValidIntervals")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(pwIndex,) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwIndex")

(PwCfgIndexOrzero,) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwCfgIndexOrzero")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pwCepStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 200)
)
pwCepStdMIB.setRevisions(
        ("2011-05-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PwCepSonetEbm(Unsigned32, TextualConvention):
    status = "current"


class PwCepSdhVc4Ebm(Unsigned32, TextualConvention):
    status = "current"


class PwCepSonetVtgMap(Unsigned32, TextualConvention):
    status = "current"


class PwCepFracAsyncMap(Integer32, TextualConvention):
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
        *(("ds3", 2),
          ("e3", 3),
          ("other", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PwCepObjects_ObjectIdentity = ObjectIdentity
pwCepObjects = _PwCepObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 200, 1)
)
_PwCepTable_Object = MibTable
pwCepTable = _PwCepTable_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1)
)
if mibBuilder.loadTexts:
    pwCepTable.setStatus("current")
_PwCepEntry_Object = MibTableRow
pwCepEntry = _PwCepEntry_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1, 1)
)
pwCepEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwCepEntry.setStatus("current")


class _PwCepType_Type(Integer32):
    """Custom type pwCepType based on Integer32"""
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
        *(("fracSpe", 3),
          ("spe", 1),
          ("vt", 2))
    )


_PwCepType_Type.__name__ = "Integer32"
_PwCepType_Object = MibTableColumn
pwCepType = _PwCepType_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1, 1, 1),
    _PwCepType_Type()
)
pwCepType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwCepType.setStatus("current")
_PwCepSonetIfIndex_Type = InterfaceIndexOrZero
_PwCepSonetIfIndex_Object = MibTableColumn
pwCepSonetIfIndex = _PwCepSonetIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1, 1, 2),
    _PwCepSonetIfIndex_Type()
)
pwCepSonetIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwCepSonetIfIndex.setStatus("current")


class _PwCepSonetConfigErrorOrStatus_Type(Bits):
    """Custom type pwCepSonetConfigErrorOrStatus based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("peerAsyncAsymmetric", 10),
          ("peerAsyncIncompatible", 6),
          ("peerDbaAsymmetric", 7),
          ("peerDbaIncompatible", 3),
          ("peerEbmAsymmetric", 8),
          ("peerEbmIncompatible", 4),
          ("peerRtpAsymmetric", 9),
          ("peerRtpIncompatible", 5),
          ("timeslotInUse", 1),
          ("timeslotMisuse", 2))
    )

_PwCepSonetConfigErrorOrStatus_Type.__name__ = "Bits"
_PwCepSonetConfigErrorOrStatus_Object = MibTableColumn
pwCepSonetConfigErrorOrStatus = _PwCepSonetConfigErrorOrStatus_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1, 1, 3),
    _PwCepSonetConfigErrorOrStatus_Type()
)
pwCepSonetConfigErrorOrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepSonetConfigErrorOrStatus.setStatus("current")
_PwCepCfgIndex_Type = PwCfgIndexOrzero
_PwCepCfgIndex_Object = MibTableColumn
pwCepCfgIndex = _PwCepCfgIndex_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1, 1, 4),
    _PwCepCfgIndex_Type()
)
pwCepCfgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwCepCfgIndex.setStatus("current")
_PwCepTimeElapsed_Type = HCPerfTimeElapsed
_PwCepTimeElapsed_Object = MibTableColumn
pwCepTimeElapsed = _PwCepTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1, 1, 5),
    _PwCepTimeElapsed_Type()
)
pwCepTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    pwCepTimeElapsed.setUnits("seconds")
_PwCepValidIntervals_Type = HCPerfValidIntervals
_PwCepValidIntervals_Object = MibTableColumn
pwCepValidIntervals = _PwCepValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1, 1, 6),
    _PwCepValidIntervals_Type()
)
pwCepValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepValidIntervals.setStatus("current")


class _PwCepIndications_Type(Bits):
    """Custom type pwCepIndications based on Bits"""
    namedValues = NamedValues(
        *(("badHdrStack", 7),
          ("cepAis", 6),
          ("cepFeFailure", 9),
          ("cepNeFailure", 8),
          ("cepRdi", 5),
          ("jtrBfrUnder", 2),
          ("lops", 4),
          ("missingPkt", 0),
          ("ooRngDropped", 1),
          ("pktMalformed", 3))
    )

_PwCepIndications_Type.__name__ = "Bits"
_PwCepIndications_Object = MibTableColumn
pwCepIndications = _PwCepIndications_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1, 1, 7),
    _PwCepIndications_Type()
)
pwCepIndications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwCepIndications.setStatus("current")
_PwCepLastEsTimeStamp_Type = TimeStamp
_PwCepLastEsTimeStamp_Object = MibTableColumn
pwCepLastEsTimeStamp = _PwCepLastEsTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1, 1, 8),
    _PwCepLastEsTimeStamp_Type()
)
pwCepLastEsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepLastEsTimeStamp.setStatus("current")
_PwCepPeerCepOption_Type = Unsigned32
_PwCepPeerCepOption_Object = MibTableColumn
pwCepPeerCepOption = _PwCepPeerCepOption_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 1, 1, 9),
    _PwCepPeerCepOption_Type()
)
pwCepPeerCepOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPeerCepOption.setStatus("current")
_PwCepCfgIndexNext_Type = PwCfgIndexOrzero
_PwCepCfgIndexNext_Object = MibScalar
pwCepCfgIndexNext = _PwCepCfgIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 2),
    _PwCepCfgIndexNext_Type()
)
pwCepCfgIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepCfgIndexNext.setStatus("current")
_PwCepCfgTable_Object = MibTable
pwCepCfgTable = _PwCepCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3)
)
if mibBuilder.loadTexts:
    pwCepCfgTable.setStatus("current")
_PwCepCfgEntry_Object = MibTableRow
pwCepCfgEntry = _PwCepCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1)
)
pwCepCfgEntry.setIndexNames(
    (0, "PW-CEP-STD-MIB", "pwCepCfgTableIndex"),
)
if mibBuilder.loadTexts:
    pwCepCfgEntry.setStatus("current")


class _PwCepCfgTableIndex_Type(Unsigned32):
    """Custom type pwCepCfgTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PwCepCfgTableIndex_Type.__name__ = "Unsigned32"
_PwCepCfgTableIndex_Object = MibTableColumn
pwCepCfgTableIndex = _PwCepCfgTableIndex_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 1),
    _PwCepCfgTableIndex_Type()
)
pwCepCfgTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwCepCfgTableIndex.setStatus("current")
_PwCepSonetPayloadLength_Type = Unsigned32
_PwCepSonetPayloadLength_Object = MibTableColumn
pwCepSonetPayloadLength = _PwCepSonetPayloadLength_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 2),
    _PwCepSonetPayloadLength_Type()
)
pwCepSonetPayloadLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepSonetPayloadLength.setStatus("current")


class _PwCepCfgMinPktLength_Type(Unsigned32):
    """Custom type pwCepCfgMinPktLength based on Unsigned32"""
    defaultValue = 0


_PwCepCfgMinPktLength_Object = MibTableColumn
pwCepCfgMinPktLength = _PwCepCfgMinPktLength_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 3),
    _PwCepCfgMinPktLength_Type()
)
pwCepCfgMinPktLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgMinPktLength.setStatus("current")
_PwCepCfgPktReorder_Type = TruthValue
_PwCepCfgPktReorder_Object = MibTableColumn
pwCepCfgPktReorder = _PwCepCfgPktReorder_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 4),
    _PwCepCfgPktReorder_Type()
)
pwCepCfgPktReorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepCfgPktReorder.setStatus("current")


class _PwCepCfgEnableDBA_Type(Bits):
    """Custom type pwCepCfgEnableDBA based on Bits"""
    namedValues = NamedValues(
        *(("ais", 0),
          ("unequipped", 1))
    )

_PwCepCfgEnableDBA_Type.__name__ = "Bits"
_PwCepCfgEnableDBA_Object = MibTableColumn
pwCepCfgEnableDBA = _PwCepCfgEnableDBA_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 5),
    _PwCepCfgEnableDBA_Type()
)
pwCepCfgEnableDBA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgEnableDBA.setStatus("current")


class _PwCepCfgRtpHdrSuppress_Type(TruthValue):
    """Custom type pwCepCfgRtpHdrSuppress based on TruthValue"""


_PwCepCfgRtpHdrSuppress_Object = MibTableColumn
pwCepCfgRtpHdrSuppress = _PwCepCfgRtpHdrSuppress_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 6),
    _PwCepCfgRtpHdrSuppress_Type()
)
pwCepCfgRtpHdrSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgRtpHdrSuppress.setStatus("current")
_PwCepCfgJtrBfrDepth_Type = Unsigned32
_PwCepCfgJtrBfrDepth_Object = MibTableColumn
pwCepCfgJtrBfrDepth = _PwCepCfgJtrBfrDepth_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 7),
    _PwCepCfgJtrBfrDepth_Type()
)
pwCepCfgJtrBfrDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgJtrBfrDepth.setStatus("current")
if mibBuilder.loadTexts:
    pwCepCfgJtrBfrDepth.setUnits("micro-seconds")


class _PwCepCfgConsecPktsInsync_Type(Unsigned32):
    """Custom type pwCepCfgConsecPktsInsync based on Unsigned32"""
    defaultValue = 2


_PwCepCfgConsecPktsInsync_Object = MibTableColumn
pwCepCfgConsecPktsInsync = _PwCepCfgConsecPktsInsync_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 8),
    _PwCepCfgConsecPktsInsync_Type()
)
pwCepCfgConsecPktsInsync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgConsecPktsInsync.setStatus("current")


class _PwCepCfgConsecMissingOutSync_Type(Unsigned32):
    """Custom type pwCepCfgConsecMissingOutSync based on Unsigned32"""
    defaultValue = 10


_PwCepCfgConsecMissingOutSync_Object = MibTableColumn
pwCepCfgConsecMissingOutSync = _PwCepCfgConsecMissingOutSync_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 9),
    _PwCepCfgConsecMissingOutSync_Type()
)
pwCepCfgConsecMissingOutSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgConsecMissingOutSync.setStatus("current")


class _PwCepCfgPktErrorPlayOutValue_Type(Unsigned32):
    """Custom type pwCepCfgPktErrorPlayOutValue based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PwCepCfgPktErrorPlayOutValue_Type.__name__ = "Unsigned32"
_PwCepCfgPktErrorPlayOutValue_Object = MibTableColumn
pwCepCfgPktErrorPlayOutValue = _PwCepCfgPktErrorPlayOutValue_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 10),
    _PwCepCfgPktErrorPlayOutValue_Type()
)
pwCepCfgPktErrorPlayOutValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgPktErrorPlayOutValue.setStatus("current")


class _PwCepCfgMissingPktsToSes_Type(Unsigned32):
    """Custom type pwCepCfgMissingPktsToSes based on Unsigned32"""
    defaultValue = 3


_PwCepCfgMissingPktsToSes_Object = MibTableColumn
pwCepCfgMissingPktsToSes = _PwCepCfgMissingPktsToSes_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 11),
    _PwCepCfgMissingPktsToSes_Type()
)
pwCepCfgMissingPktsToSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgMissingPktsToSes.setStatus("current")
if mibBuilder.loadTexts:
    pwCepCfgMissingPktsToSes.setUnits("seconds")


class _PwCepCfgSesToUas_Type(Unsigned32):
    """Custom type pwCepCfgSesToUas based on Unsigned32"""
    defaultValue = 10


_PwCepCfgSesToUas_Object = MibTableColumn
pwCepCfgSesToUas = _PwCepCfgSesToUas_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 12),
    _PwCepCfgSesToUas_Type()
)
pwCepCfgSesToUas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgSesToUas.setStatus("current")
if mibBuilder.loadTexts:
    pwCepCfgSesToUas.setUnits("seconds")


class _PwCepCfgSecsToExitUas_Type(Unsigned32):
    """Custom type pwCepCfgSecsToExitUas based on Unsigned32"""
    defaultValue = 10


_PwCepCfgSecsToExitUas_Object = MibTableColumn
pwCepCfgSecsToExitUas = _PwCepCfgSecsToExitUas_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 13),
    _PwCepCfgSecsToExitUas_Type()
)
pwCepCfgSecsToExitUas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgSecsToExitUas.setStatus("current")
if mibBuilder.loadTexts:
    pwCepCfgSecsToExitUas.setUnits("seconds")
_PwCepCfgName_Type = SnmpAdminString
_PwCepCfgName_Object = MibTableColumn
pwCepCfgName = _PwCepCfgName_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 14),
    _PwCepCfgName_Type()
)
pwCepCfgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgName.setStatus("current")
_PwCepCfgRowStatus_Type = RowStatus
_PwCepCfgRowStatus_Object = MibTableColumn
pwCepCfgRowStatus = _PwCepCfgRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 15),
    _PwCepCfgRowStatus_Type()
)
pwCepCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgRowStatus.setStatus("current")


class _PwCepCfgStorageType_Type(StorageType):
    """Custom type pwCepCfgStorageType based on StorageType"""


_PwCepCfgStorageType_Object = MibTableColumn
pwCepCfgStorageType = _PwCepCfgStorageType_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 3, 1, 16),
    _PwCepCfgStorageType_Type()
)
pwCepCfgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepCfgStorageType.setStatus("current")
_PwCepFracTable_Object = MibTable
pwCepFracTable = _PwCepFracTable_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4)
)
if mibBuilder.loadTexts:
    pwCepFracTable.setStatus("current")
_PwCepFracEntry_Object = MibTableRow
pwCepFracEntry = _PwCepFracEntry_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1)
)
pwCepFracEntry.setIndexNames(
    (0, "PW-CEP-STD-MIB", "pwCepFracIndex"),
)
if mibBuilder.loadTexts:
    pwCepFracEntry.setStatus("current")
_PwCepFracIndex_Type = InterfaceIndex
_PwCepFracIndex_Object = MibTableColumn
pwCepFracIndex = _PwCepFracIndex_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 1),
    _PwCepFracIndex_Type()
)
pwCepFracIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwCepFracIndex.setStatus("current")


class _PwCepFracMode_Type(Integer32):
    """Custom type pwCepFracMode based on Integer32"""
    defaultValue = 2

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
        *(("dynamic", 2),
          ("notApplicable", 1),
          ("static", 3),
          ("staticAsync", 5),
          ("staticWithEbm", 4))
    )


_PwCepFracMode_Type.__name__ = "Integer32"
_PwCepFracMode_Object = MibTableColumn
pwCepFracMode = _PwCepFracMode_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 2),
    _PwCepFracMode_Type()
)
pwCepFracMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracMode.setStatus("current")


class _PwCepFracConfigError_Type(Bits):
    """Custom type pwCepFracConfigError based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("vtgMapAsyncConflict", 2),
          ("vtgMapEbmConflict", 1))
    )

_PwCepFracConfigError_Type.__name__ = "Bits"
_PwCepFracConfigError_Object = MibTableColumn
pwCepFracConfigError = _PwCepFracConfigError_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 3),
    _PwCepFracConfigError_Type()
)
pwCepFracConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepFracConfigError.setStatus("current")


class _PwCepFracAsync_Type(PwCepFracAsyncMap):
    """Custom type pwCepFracAsync based on PwCepFracAsyncMap"""


_PwCepFracAsync_Object = MibTableColumn
pwCepFracAsync = _PwCepFracAsync_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 4),
    _PwCepFracAsync_Type()
)
pwCepFracAsync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracAsync.setStatus("current")
_PwCepFracVtgMap_Type = PwCepSonetVtgMap
_PwCepFracVtgMap_Object = MibTableColumn
pwCepFracVtgMap = _PwCepFracVtgMap_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 5),
    _PwCepFracVtgMap_Type()
)
pwCepFracVtgMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracVtgMap.setStatus("current")
_PwCepFracEbm_Type = PwCepSonetEbm
_PwCepFracEbm_Object = MibTableColumn
pwCepFracEbm = _PwCepFracEbm_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 6),
    _PwCepFracEbm_Type()
)
pwCepFracEbm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracEbm.setStatus("current")
_PwCepFracPeerEbm_Type = PwCepSonetEbm
_PwCepFracPeerEbm_Object = MibTableColumn
pwCepFracPeerEbm = _PwCepFracPeerEbm_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 7),
    _PwCepFracPeerEbm_Type()
)
pwCepFracPeerEbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepFracPeerEbm.setStatus("current")


class _PwCepFracSdhVc4Mode_Type(Integer32):
    """Custom type pwCepFracSdhVc4Mode based on Integer32"""
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
        *(("dynamic", 2),
          ("notApplicable", 1),
          ("static", 3),
          ("staticWithEbm", 4))
    )


_PwCepFracSdhVc4Mode_Type.__name__ = "Integer32"
_PwCepFracSdhVc4Mode_Object = MibTableColumn
pwCepFracSdhVc4Mode = _PwCepFracSdhVc4Mode_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 8),
    _PwCepFracSdhVc4Mode_Type()
)
pwCepFracSdhVc4Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4Mode.setStatus("current")


class _PwCepFracSdhVc4Tu3Map1_Type(PwCepFracAsyncMap):
    """Custom type pwCepFracSdhVc4Tu3Map1 based on PwCepFracAsyncMap"""


_PwCepFracSdhVc4Tu3Map1_Object = MibTableColumn
pwCepFracSdhVc4Tu3Map1 = _PwCepFracSdhVc4Tu3Map1_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 9),
    _PwCepFracSdhVc4Tu3Map1_Type()
)
pwCepFracSdhVc4Tu3Map1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4Tu3Map1.setStatus("current")


class _PwCepFracSdhVc4Tu3Map2_Type(PwCepFracAsyncMap):
    """Custom type pwCepFracSdhVc4Tu3Map2 based on PwCepFracAsyncMap"""


_PwCepFracSdhVc4Tu3Map2_Object = MibTableColumn
pwCepFracSdhVc4Tu3Map2 = _PwCepFracSdhVc4Tu3Map2_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 10),
    _PwCepFracSdhVc4Tu3Map2_Type()
)
pwCepFracSdhVc4Tu3Map2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4Tu3Map2.setStatus("current")


class _PwCepFracSdhVc4Tu3Map3_Type(PwCepFracAsyncMap):
    """Custom type pwCepFracSdhVc4Tu3Map3 based on PwCepFracAsyncMap"""


_PwCepFracSdhVc4Tu3Map3_Object = MibTableColumn
pwCepFracSdhVc4Tu3Map3 = _PwCepFracSdhVc4Tu3Map3_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 11),
    _PwCepFracSdhVc4Tu3Map3_Type()
)
pwCepFracSdhVc4Tu3Map3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4Tu3Map3.setStatus("current")
_PwCepFracSdhVc4Tug2Map1_Type = PwCepSonetVtgMap
_PwCepFracSdhVc4Tug2Map1_Object = MibTableColumn
pwCepFracSdhVc4Tug2Map1 = _PwCepFracSdhVc4Tug2Map1_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 12),
    _PwCepFracSdhVc4Tug2Map1_Type()
)
pwCepFracSdhVc4Tug2Map1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4Tug2Map1.setStatus("current")
_PwCepFracSdhVc4Tug2Map2_Type = PwCepSonetVtgMap
_PwCepFracSdhVc4Tug2Map2_Object = MibTableColumn
pwCepFracSdhVc4Tug2Map2 = _PwCepFracSdhVc4Tug2Map2_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 13),
    _PwCepFracSdhVc4Tug2Map2_Type()
)
pwCepFracSdhVc4Tug2Map2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4Tug2Map2.setStatus("current")
_PwCepFracSdhVc4Tug2Map3_Type = PwCepSonetVtgMap
_PwCepFracSdhVc4Tug2Map3_Object = MibTableColumn
pwCepFracSdhVc4Tug2Map3 = _PwCepFracSdhVc4Tug2Map3_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 14),
    _PwCepFracSdhVc4Tug2Map3_Type()
)
pwCepFracSdhVc4Tug2Map3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4Tug2Map3.setStatus("current")
_PwCepFracSdhVc4Ebm1_Type = PwCepSdhVc4Ebm
_PwCepFracSdhVc4Ebm1_Object = MibTableColumn
pwCepFracSdhVc4Ebm1 = _PwCepFracSdhVc4Ebm1_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 15),
    _PwCepFracSdhVc4Ebm1_Type()
)
pwCepFracSdhVc4Ebm1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4Ebm1.setStatus("current")
_PwCepFracSdhVc4Ebm2_Type = PwCepSdhVc4Ebm
_PwCepFracSdhVc4Ebm2_Object = MibTableColumn
pwCepFracSdhVc4Ebm2 = _PwCepFracSdhVc4Ebm2_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 16),
    _PwCepFracSdhVc4Ebm2_Type()
)
pwCepFracSdhVc4Ebm2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4Ebm2.setStatus("current")
_PwCepFracSdhVc4Ebm3_Type = PwCepSdhVc4Ebm
_PwCepFracSdhVc4Ebm3_Object = MibTableColumn
pwCepFracSdhVc4Ebm3 = _PwCepFracSdhVc4Ebm3_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 17),
    _PwCepFracSdhVc4Ebm3_Type()
)
pwCepFracSdhVc4Ebm3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4Ebm3.setStatus("current")
_PwCepFracSdhVc4PeerEbm1_Type = PwCepSdhVc4Ebm
_PwCepFracSdhVc4PeerEbm1_Object = MibTableColumn
pwCepFracSdhVc4PeerEbm1 = _PwCepFracSdhVc4PeerEbm1_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 18),
    _PwCepFracSdhVc4PeerEbm1_Type()
)
pwCepFracSdhVc4PeerEbm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4PeerEbm1.setStatus("current")
_PwCepFracSdhVc4PeerEbm2_Type = PwCepSdhVc4Ebm
_PwCepFracSdhVc4PeerEbm2_Object = MibTableColumn
pwCepFracSdhVc4PeerEbm2 = _PwCepFracSdhVc4PeerEbm2_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 19),
    _PwCepFracSdhVc4PeerEbm2_Type()
)
pwCepFracSdhVc4PeerEbm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4PeerEbm2.setStatus("current")
_PwCepFracSdhVc4PeerEbm3_Type = PwCepSdhVc4Ebm
_PwCepFracSdhVc4PeerEbm3_Object = MibTableColumn
pwCepFracSdhVc4PeerEbm3 = _PwCepFracSdhVc4PeerEbm3_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 20),
    _PwCepFracSdhVc4PeerEbm3_Type()
)
pwCepFracSdhVc4PeerEbm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepFracSdhVc4PeerEbm3.setStatus("current")
_PwCepFracRowStatus_Type = RowStatus
_PwCepFracRowStatus_Object = MibTableColumn
pwCepFracRowStatus = _PwCepFracRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 21),
    _PwCepFracRowStatus_Type()
)
pwCepFracRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracRowStatus.setStatus("current")


class _PwCepFracStorageType_Type(StorageType):
    """Custom type pwCepFracStorageType based on StorageType"""


_PwCepFracStorageType_Object = MibTableColumn
pwCepFracStorageType = _PwCepFracStorageType_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 4, 1, 22),
    _PwCepFracStorageType_Type()
)
pwCepFracStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepFracStorageType.setStatus("current")
_PwCepPerfCurrentTable_Object = MibTable
pwCepPerfCurrentTable = _PwCepPerfCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5)
)
if mibBuilder.loadTexts:
    pwCepPerfCurrentTable.setStatus("current")
_PwCepPerfCurrentEntry_Object = MibTableRow
pwCepPerfCurrentEntry = _PwCepPerfCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1)
)
pwCepPerfCurrentEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    pwCepPerfCurrentEntry.setStatus("current")
_PwCepPerfCurrentDbaInPacketsHC_Type = HCPerfCurrentCount
_PwCepPerfCurrentDbaInPacketsHC_Object = MibTableColumn
pwCepPerfCurrentDbaInPacketsHC = _PwCepPerfCurrentDbaInPacketsHC_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 1),
    _PwCepPerfCurrentDbaInPacketsHC_Type()
)
pwCepPerfCurrentDbaInPacketsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentDbaInPacketsHC.setStatus("current")
_PwCepPerfCurrentDbaOutPacketsHC_Type = HCPerfCurrentCount
_PwCepPerfCurrentDbaOutPacketsHC_Object = MibTableColumn
pwCepPerfCurrentDbaOutPacketsHC = _PwCepPerfCurrentDbaOutPacketsHC_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 2),
    _PwCepPerfCurrentDbaOutPacketsHC_Type()
)
pwCepPerfCurrentDbaOutPacketsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentDbaOutPacketsHC.setStatus("current")
_PwCepPerfCurrentInNegPtrAdjust_Type = PerfCurrentCount
_PwCepPerfCurrentInNegPtrAdjust_Object = MibTableColumn
pwCepPerfCurrentInNegPtrAdjust = _PwCepPerfCurrentInNegPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 3),
    _PwCepPerfCurrentInNegPtrAdjust_Type()
)
pwCepPerfCurrentInNegPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentInNegPtrAdjust.setStatus("current")
_PwCepPerfCurrentInPosPtrAdjust_Type = PerfCurrentCount
_PwCepPerfCurrentInPosPtrAdjust_Object = MibTableColumn
pwCepPerfCurrentInPosPtrAdjust = _PwCepPerfCurrentInPosPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 4),
    _PwCepPerfCurrentInPosPtrAdjust_Type()
)
pwCepPerfCurrentInPosPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentInPosPtrAdjust.setStatus("current")
_PwCepPerfCurrentInPtrAdjustSecs_Type = PerfCurrentCount
_PwCepPerfCurrentInPtrAdjustSecs_Object = MibTableColumn
pwCepPerfCurrentInPtrAdjustSecs = _PwCepPerfCurrentInPtrAdjustSecs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 5),
    _PwCepPerfCurrentInPtrAdjustSecs_Type()
)
pwCepPerfCurrentInPtrAdjustSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentInPtrAdjustSecs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfCurrentInPtrAdjustSecs.setUnits("seconds")
_PwCepPerfCurrentOutNegPtrAdjust_Type = PerfCurrentCount
_PwCepPerfCurrentOutNegPtrAdjust_Object = MibTableColumn
pwCepPerfCurrentOutNegPtrAdjust = _PwCepPerfCurrentOutNegPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 6),
    _PwCepPerfCurrentOutNegPtrAdjust_Type()
)
pwCepPerfCurrentOutNegPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentOutNegPtrAdjust.setStatus("current")
_PwCepPerfCurrentOutPosPtrAdjust_Type = PerfCurrentCount
_PwCepPerfCurrentOutPosPtrAdjust_Object = MibTableColumn
pwCepPerfCurrentOutPosPtrAdjust = _PwCepPerfCurrentOutPosPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 7),
    _PwCepPerfCurrentOutPosPtrAdjust_Type()
)
pwCepPerfCurrentOutPosPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentOutPosPtrAdjust.setStatus("current")
_PwCepPerfCurrentOutPtrAdjustSecs_Type = PerfCurrentCount
_PwCepPerfCurrentOutPtrAdjustSecs_Object = MibTableColumn
pwCepPerfCurrentOutPtrAdjustSecs = _PwCepPerfCurrentOutPtrAdjustSecs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 8),
    _PwCepPerfCurrentOutPtrAdjustSecs_Type()
)
pwCepPerfCurrentOutPtrAdjustSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentOutPtrAdjustSecs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfCurrentOutPtrAdjustSecs.setUnits("seconds")
_PwCepPerfCurrentAbsPtrAdjust_Type = Integer32
_PwCepPerfCurrentAbsPtrAdjust_Object = MibTableColumn
pwCepPerfCurrentAbsPtrAdjust = _PwCepPerfCurrentAbsPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 9),
    _PwCepPerfCurrentAbsPtrAdjust_Type()
)
pwCepPerfCurrentAbsPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentAbsPtrAdjust.setStatus("current")
_PwCepPerfCurrentMissingPkts_Type = PerfCurrentCount
_PwCepPerfCurrentMissingPkts_Object = MibTableColumn
pwCepPerfCurrentMissingPkts = _PwCepPerfCurrentMissingPkts_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 10),
    _PwCepPerfCurrentMissingPkts_Type()
)
pwCepPerfCurrentMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentMissingPkts.setStatus("current")
_PwCepPerfCurrentPktsOoseq_Type = PerfCurrentCount
_PwCepPerfCurrentPktsOoseq_Object = MibTableColumn
pwCepPerfCurrentPktsOoseq = _PwCepPerfCurrentPktsOoseq_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 11),
    _PwCepPerfCurrentPktsOoseq_Type()
)
pwCepPerfCurrentPktsOoseq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentPktsOoseq.setStatus("current")
_PwCepPerfCurrentPktsOoRngDropped_Type = PerfCurrentCount
_PwCepPerfCurrentPktsOoRngDropped_Object = MibTableColumn
pwCepPerfCurrentPktsOoRngDropped = _PwCepPerfCurrentPktsOoRngDropped_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 12),
    _PwCepPerfCurrentPktsOoRngDropped_Type()
)
pwCepPerfCurrentPktsOoRngDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentPktsOoRngDropped.setStatus("current")
_PwCepPerfCurrentJtrBfrUnderruns_Type = PerfCurrentCount
_PwCepPerfCurrentJtrBfrUnderruns_Object = MibTableColumn
pwCepPerfCurrentJtrBfrUnderruns = _PwCepPerfCurrentJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 13),
    _PwCepPerfCurrentJtrBfrUnderruns_Type()
)
pwCepPerfCurrentJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentJtrBfrUnderruns.setStatus("current")
_PwCepPerfCurrentPktsMalformed_Type = PerfCurrentCount
_PwCepPerfCurrentPktsMalformed_Object = MibTableColumn
pwCepPerfCurrentPktsMalformed = _PwCepPerfCurrentPktsMalformed_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 14),
    _PwCepPerfCurrentPktsMalformed_Type()
)
pwCepPerfCurrentPktsMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentPktsMalformed.setStatus("current")
_PwCepPerfCurrentSummaryErrors_Type = PerfCurrentCount
_PwCepPerfCurrentSummaryErrors_Object = MibTableColumn
pwCepPerfCurrentSummaryErrors = _PwCepPerfCurrentSummaryErrors_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 15),
    _PwCepPerfCurrentSummaryErrors_Type()
)
pwCepPerfCurrentSummaryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentSummaryErrors.setStatus("current")
_PwCepPerfCurrentESs_Type = PerfCurrentCount
_PwCepPerfCurrentESs_Object = MibTableColumn
pwCepPerfCurrentESs = _PwCepPerfCurrentESs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 16),
    _PwCepPerfCurrentESs_Type()
)
pwCepPerfCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentESs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfCurrentESs.setUnits("seconds")
_PwCepPerfCurrentSESs_Type = PerfCurrentCount
_PwCepPerfCurrentSESs_Object = MibTableColumn
pwCepPerfCurrentSESs = _PwCepPerfCurrentSESs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 17),
    _PwCepPerfCurrentSESs_Type()
)
pwCepPerfCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentSESs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfCurrentSESs.setUnits("seconds")
_PwCepPerfCurrentUASs_Type = PerfCurrentCount
_PwCepPerfCurrentUASs_Object = MibTableColumn
pwCepPerfCurrentUASs = _PwCepPerfCurrentUASs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 18),
    _PwCepPerfCurrentUASs_Type()
)
pwCepPerfCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentUASs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfCurrentUASs.setUnits("seconds")
_PwCepPerfCurrentFC_Type = PerfCurrentCount
_PwCepPerfCurrentFC_Object = MibTableColumn
pwCepPerfCurrentFC = _PwCepPerfCurrentFC_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 5, 1, 19),
    _PwCepPerfCurrentFC_Type()
)
pwCepPerfCurrentFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfCurrentFC.setStatus("current")
_PwCepPerfIntervalTable_Object = MibTable
pwCepPerfIntervalTable = _PwCepPerfIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6)
)
if mibBuilder.loadTexts:
    pwCepPerfIntervalTable.setStatus("current")
_PwCepPerfIntervalEntry_Object = MibTableRow
pwCepPerfIntervalEntry = _PwCepPerfIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1)
)
pwCepPerfIntervalEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-CEP-STD-MIB", "pwCepPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    pwCepPerfIntervalEntry.setStatus("current")


class _PwCepPerfIntervalNumber_Type(Integer32):
    """Custom type pwCepPerfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PwCepPerfIntervalNumber_Type.__name__ = "Integer32"
_PwCepPerfIntervalNumber_Object = MibTableColumn
pwCepPerfIntervalNumber = _PwCepPerfIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 1),
    _PwCepPerfIntervalNumber_Type()
)
pwCepPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwCepPerfIntervalNumber.setStatus("current")
_PwCepPerfIntervalValidData_Type = TruthValue
_PwCepPerfIntervalValidData_Object = MibTableColumn
pwCepPerfIntervalValidData = _PwCepPerfIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 2),
    _PwCepPerfIntervalValidData_Type()
)
pwCepPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalValidData.setStatus("current")


class _PwCepPerfIntervalReset_Type(Integer32):
    """Custom type pwCepPerfIntervalReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("reset", 1))
    )


_PwCepPerfIntervalReset_Type.__name__ = "Integer32"
_PwCepPerfIntervalReset_Object = MibTableColumn
pwCepPerfIntervalReset = _PwCepPerfIntervalReset_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 3),
    _PwCepPerfIntervalReset_Type()
)
pwCepPerfIntervalReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwCepPerfIntervalReset.setStatus("current")
_PwCepPerfIntervalTimeElapsed_Type = HCPerfTimeElapsed
_PwCepPerfIntervalTimeElapsed_Object = MibTableColumn
pwCepPerfIntervalTimeElapsed = _PwCepPerfIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 4),
    _PwCepPerfIntervalTimeElapsed_Type()
)
pwCepPerfIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfIntervalTimeElapsed.setUnits("seconds")
_PwCepPerfIntervalDbaInPacketsHC_Type = HCPerfIntervalCount
_PwCepPerfIntervalDbaInPacketsHC_Object = MibTableColumn
pwCepPerfIntervalDbaInPacketsHC = _PwCepPerfIntervalDbaInPacketsHC_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 5),
    _PwCepPerfIntervalDbaInPacketsHC_Type()
)
pwCepPerfIntervalDbaInPacketsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalDbaInPacketsHC.setStatus("current")
_PwCepPerfIntervalDbaOutPacketsHC_Type = HCPerfIntervalCount
_PwCepPerfIntervalDbaOutPacketsHC_Object = MibTableColumn
pwCepPerfIntervalDbaOutPacketsHC = _PwCepPerfIntervalDbaOutPacketsHC_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 6),
    _PwCepPerfIntervalDbaOutPacketsHC_Type()
)
pwCepPerfIntervalDbaOutPacketsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalDbaOutPacketsHC.setStatus("current")
_PwCepPerfIntervalInNegPtrAdjust_Type = PerfIntervalCount
_PwCepPerfIntervalInNegPtrAdjust_Object = MibTableColumn
pwCepPerfIntervalInNegPtrAdjust = _PwCepPerfIntervalInNegPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 7),
    _PwCepPerfIntervalInNegPtrAdjust_Type()
)
pwCepPerfIntervalInNegPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalInNegPtrAdjust.setStatus("current")
_PwCepPerfIntervalInPosPtrAdjust_Type = PerfIntervalCount
_PwCepPerfIntervalInPosPtrAdjust_Object = MibTableColumn
pwCepPerfIntervalInPosPtrAdjust = _PwCepPerfIntervalInPosPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 8),
    _PwCepPerfIntervalInPosPtrAdjust_Type()
)
pwCepPerfIntervalInPosPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalInPosPtrAdjust.setStatus("current")
_PwCepPerfIntervalInPtrAdjustSecs_Type = PerfIntervalCount
_PwCepPerfIntervalInPtrAdjustSecs_Object = MibTableColumn
pwCepPerfIntervalInPtrAdjustSecs = _PwCepPerfIntervalInPtrAdjustSecs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 9),
    _PwCepPerfIntervalInPtrAdjustSecs_Type()
)
pwCepPerfIntervalInPtrAdjustSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalInPtrAdjustSecs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfIntervalInPtrAdjustSecs.setUnits("seconds")
_PwCepPerfIntervalOutNegPtrAdjust_Type = PerfIntervalCount
_PwCepPerfIntervalOutNegPtrAdjust_Object = MibTableColumn
pwCepPerfIntervalOutNegPtrAdjust = _PwCepPerfIntervalOutNegPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 10),
    _PwCepPerfIntervalOutNegPtrAdjust_Type()
)
pwCepPerfIntervalOutNegPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalOutNegPtrAdjust.setStatus("current")
_PwCepPerfIntervalOutPosPtrAdjust_Type = PerfIntervalCount
_PwCepPerfIntervalOutPosPtrAdjust_Object = MibTableColumn
pwCepPerfIntervalOutPosPtrAdjust = _PwCepPerfIntervalOutPosPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 11),
    _PwCepPerfIntervalOutPosPtrAdjust_Type()
)
pwCepPerfIntervalOutPosPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalOutPosPtrAdjust.setStatus("current")
_PwCepPerfIntervalOutPtrAdjustSecs_Type = PerfIntervalCount
_PwCepPerfIntervalOutPtrAdjustSecs_Object = MibTableColumn
pwCepPerfIntervalOutPtrAdjustSecs = _PwCepPerfIntervalOutPtrAdjustSecs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 12),
    _PwCepPerfIntervalOutPtrAdjustSecs_Type()
)
pwCepPerfIntervalOutPtrAdjustSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalOutPtrAdjustSecs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfIntervalOutPtrAdjustSecs.setUnits("seconds")
_PwCepPerfIntervalAbsPtrAdjust_Type = Integer32
_PwCepPerfIntervalAbsPtrAdjust_Object = MibTableColumn
pwCepPerfIntervalAbsPtrAdjust = _PwCepPerfIntervalAbsPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 13),
    _PwCepPerfIntervalAbsPtrAdjust_Type()
)
pwCepPerfIntervalAbsPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalAbsPtrAdjust.setStatus("current")
_PwCepPerfIntervalMissingPkts_Type = PerfIntervalCount
_PwCepPerfIntervalMissingPkts_Object = MibTableColumn
pwCepPerfIntervalMissingPkts = _PwCepPerfIntervalMissingPkts_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 14),
    _PwCepPerfIntervalMissingPkts_Type()
)
pwCepPerfIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalMissingPkts.setStatus("current")
_PwCepPerfIntervalPktsOoseq_Type = PerfIntervalCount
_PwCepPerfIntervalPktsOoseq_Object = MibTableColumn
pwCepPerfIntervalPktsOoseq = _PwCepPerfIntervalPktsOoseq_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 15),
    _PwCepPerfIntervalPktsOoseq_Type()
)
pwCepPerfIntervalPktsOoseq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalPktsOoseq.setStatus("current")
_PwCepPerfIntervalPktsOoRngDropped_Type = PerfIntervalCount
_PwCepPerfIntervalPktsOoRngDropped_Object = MibTableColumn
pwCepPerfIntervalPktsOoRngDropped = _PwCepPerfIntervalPktsOoRngDropped_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 16),
    _PwCepPerfIntervalPktsOoRngDropped_Type()
)
pwCepPerfIntervalPktsOoRngDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalPktsOoRngDropped.setStatus("current")
_PwCepPerfIntervalJtrBfrUnderruns_Type = PerfIntervalCount
_PwCepPerfIntervalJtrBfrUnderruns_Object = MibTableColumn
pwCepPerfIntervalJtrBfrUnderruns = _PwCepPerfIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 17),
    _PwCepPerfIntervalJtrBfrUnderruns_Type()
)
pwCepPerfIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalJtrBfrUnderruns.setStatus("current")
_PwCepPerfIntervalPktsMalformed_Type = PerfIntervalCount
_PwCepPerfIntervalPktsMalformed_Object = MibTableColumn
pwCepPerfIntervalPktsMalformed = _PwCepPerfIntervalPktsMalformed_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 18),
    _PwCepPerfIntervalPktsMalformed_Type()
)
pwCepPerfIntervalPktsMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalPktsMalformed.setStatus("current")
_PwCepPerfIntervalSummaryErrors_Type = PerfIntervalCount
_PwCepPerfIntervalSummaryErrors_Object = MibTableColumn
pwCepPerfIntervalSummaryErrors = _PwCepPerfIntervalSummaryErrors_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 19),
    _PwCepPerfIntervalSummaryErrors_Type()
)
pwCepPerfIntervalSummaryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalSummaryErrors.setStatus("current")
_PwCepPerfIntervalESs_Type = PerfIntervalCount
_PwCepPerfIntervalESs_Object = MibTableColumn
pwCepPerfIntervalESs = _PwCepPerfIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 20),
    _PwCepPerfIntervalESs_Type()
)
pwCepPerfIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfIntervalESs.setUnits("seconds")
_PwCepPerfIntervalSESs_Type = PerfIntervalCount
_PwCepPerfIntervalSESs_Object = MibTableColumn
pwCepPerfIntervalSESs = _PwCepPerfIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 21),
    _PwCepPerfIntervalSESs_Type()
)
pwCepPerfIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalSESs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfIntervalSESs.setUnits("seconds")
_PwCepPerfIntervalUASs_Type = PerfIntervalCount
_PwCepPerfIntervalUASs_Object = MibTableColumn
pwCepPerfIntervalUASs = _PwCepPerfIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 22),
    _PwCepPerfIntervalUASs_Type()
)
pwCepPerfIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalUASs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerfIntervalUASs.setUnits("seconds")
_PwCepPerfIntervalFC_Type = PerfIntervalCount
_PwCepPerfIntervalFC_Object = MibTableColumn
pwCepPerfIntervalFC = _PwCepPerfIntervalFC_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 6, 1, 23),
    _PwCepPerfIntervalFC_Type()
)
pwCepPerfIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerfIntervalFC.setStatus("current")
_PwCepPerf1DayIntervalTable_Object = MibTable
pwCepPerf1DayIntervalTable = _PwCepPerf1DayIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7)
)
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalTable.setStatus("current")
_PwCepPerf1DayIntervalEntry_Object = MibTableRow
pwCepPerf1DayIntervalEntry = _PwCepPerf1DayIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1)
)
pwCepPerf1DayIntervalEntry.setIndexNames(
    (0, "PW-STD-MIB", "pwIndex"),
    (0, "PW-CEP-STD-MIB", "pwCepPerf1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalEntry.setStatus("current")


class _PwCepPerf1DayIntervalNumber_Type(Unsigned32):
    """Custom type pwCepPerf1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PwCepPerf1DayIntervalNumber_Type.__name__ = "Unsigned32"
_PwCepPerf1DayIntervalNumber_Object = MibTableColumn
pwCepPerf1DayIntervalNumber = _PwCepPerf1DayIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 1),
    _PwCepPerf1DayIntervalNumber_Type()
)
pwCepPerf1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalNumber.setStatus("current")
_PwCepPerf1DayIntervalValidData_Type = TruthValue
_PwCepPerf1DayIntervalValidData_Object = MibTableColumn
pwCepPerf1DayIntervalValidData = _PwCepPerf1DayIntervalValidData_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 2),
    _PwCepPerf1DayIntervalValidData_Type()
)
pwCepPerf1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalValidData.setStatus("current")
_PwCepPerf1DayIntervalMoniSecs_Type = HCPerfTimeElapsed
_PwCepPerf1DayIntervalMoniSecs_Object = MibTableColumn
pwCepPerf1DayIntervalMoniSecs = _PwCepPerf1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 3),
    _PwCepPerf1DayIntervalMoniSecs_Type()
)
pwCepPerf1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalMoniSecs.setUnits("seconds")
_PwCepPerf1DayIntervalDbaInPacketsHC_Type = Counter64
_PwCepPerf1DayIntervalDbaInPacketsHC_Object = MibTableColumn
pwCepPerf1DayIntervalDbaInPacketsHC = _PwCepPerf1DayIntervalDbaInPacketsHC_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 4),
    _PwCepPerf1DayIntervalDbaInPacketsHC_Type()
)
pwCepPerf1DayIntervalDbaInPacketsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalDbaInPacketsHC.setStatus("current")
_PwCepPerf1DayIntervalDbaOutPacketsHC_Type = Counter64
_PwCepPerf1DayIntervalDbaOutPacketsHC_Object = MibTableColumn
pwCepPerf1DayIntervalDbaOutPacketsHC = _PwCepPerf1DayIntervalDbaOutPacketsHC_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 5),
    _PwCepPerf1DayIntervalDbaOutPacketsHC_Type()
)
pwCepPerf1DayIntervalDbaOutPacketsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalDbaOutPacketsHC.setStatus("current")
_PwCepPerf1DayIntervalInNegPtrAdjust_Type = Counter32
_PwCepPerf1DayIntervalInNegPtrAdjust_Object = MibTableColumn
pwCepPerf1DayIntervalInNegPtrAdjust = _PwCepPerf1DayIntervalInNegPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 6),
    _PwCepPerf1DayIntervalInNegPtrAdjust_Type()
)
pwCepPerf1DayIntervalInNegPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalInNegPtrAdjust.setStatus("current")
_PwCepPerf1DayIntervalInPosPtrAdjust_Type = Counter32
_PwCepPerf1DayIntervalInPosPtrAdjust_Object = MibTableColumn
pwCepPerf1DayIntervalInPosPtrAdjust = _PwCepPerf1DayIntervalInPosPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 7),
    _PwCepPerf1DayIntervalInPosPtrAdjust_Type()
)
pwCepPerf1DayIntervalInPosPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalInPosPtrAdjust.setStatus("current")
_PwCepPerf1DayIntervalInPtrAdjustSecs_Type = Counter32
_PwCepPerf1DayIntervalInPtrAdjustSecs_Object = MibTableColumn
pwCepPerf1DayIntervalInPtrAdjustSecs = _PwCepPerf1DayIntervalInPtrAdjustSecs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 8),
    _PwCepPerf1DayIntervalInPtrAdjustSecs_Type()
)
pwCepPerf1DayIntervalInPtrAdjustSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalInPtrAdjustSecs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalInPtrAdjustSecs.setUnits("seconds")
_PwCepPerf1DayIntervalOutNegPtrAdjust_Type = Counter32
_PwCepPerf1DayIntervalOutNegPtrAdjust_Object = MibTableColumn
pwCepPerf1DayIntervalOutNegPtrAdjust = _PwCepPerf1DayIntervalOutNegPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 9),
    _PwCepPerf1DayIntervalOutNegPtrAdjust_Type()
)
pwCepPerf1DayIntervalOutNegPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalOutNegPtrAdjust.setStatus("current")
_PwCepPerf1DayIntervalOutPosPtrAdjust_Type = Counter32
_PwCepPerf1DayIntervalOutPosPtrAdjust_Object = MibTableColumn
pwCepPerf1DayIntervalOutPosPtrAdjust = _PwCepPerf1DayIntervalOutPosPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 10),
    _PwCepPerf1DayIntervalOutPosPtrAdjust_Type()
)
pwCepPerf1DayIntervalOutPosPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalOutPosPtrAdjust.setStatus("current")
_PwCepPerf1DayIntervalOutPtrAdjustSecs_Type = Counter32
_PwCepPerf1DayIntervalOutPtrAdjustSecs_Object = MibTableColumn
pwCepPerf1DayIntervalOutPtrAdjustSecs = _PwCepPerf1DayIntervalOutPtrAdjustSecs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 11),
    _PwCepPerf1DayIntervalOutPtrAdjustSecs_Type()
)
pwCepPerf1DayIntervalOutPtrAdjustSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalOutPtrAdjustSecs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalOutPtrAdjustSecs.setUnits("seconds")
_PwCepPerf1DayIntervalAbsPtrAdjust_Type = Integer32
_PwCepPerf1DayIntervalAbsPtrAdjust_Object = MibTableColumn
pwCepPerf1DayIntervalAbsPtrAdjust = _PwCepPerf1DayIntervalAbsPtrAdjust_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 12),
    _PwCepPerf1DayIntervalAbsPtrAdjust_Type()
)
pwCepPerf1DayIntervalAbsPtrAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalAbsPtrAdjust.setStatus("current")
_PwCepPerf1DayIntervalMissingPkts_Type = Counter32
_PwCepPerf1DayIntervalMissingPkts_Object = MibTableColumn
pwCepPerf1DayIntervalMissingPkts = _PwCepPerf1DayIntervalMissingPkts_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 13),
    _PwCepPerf1DayIntervalMissingPkts_Type()
)
pwCepPerf1DayIntervalMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalMissingPkts.setStatus("current")
_PwCepPerf1DayIntervalPktsOoseq_Type = Counter32
_PwCepPerf1DayIntervalPktsOoseq_Object = MibTableColumn
pwCepPerf1DayIntervalPktsOoseq = _PwCepPerf1DayIntervalPktsOoseq_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 14),
    _PwCepPerf1DayIntervalPktsOoseq_Type()
)
pwCepPerf1DayIntervalPktsOoseq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalPktsOoseq.setStatus("current")
_PwCepPerf1DayIntervalPktsOoRngDropped_Type = Counter32
_PwCepPerf1DayIntervalPktsOoRngDropped_Object = MibTableColumn
pwCepPerf1DayIntervalPktsOoRngDropped = _PwCepPerf1DayIntervalPktsOoRngDropped_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 15),
    _PwCepPerf1DayIntervalPktsOoRngDropped_Type()
)
pwCepPerf1DayIntervalPktsOoRngDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalPktsOoRngDropped.setStatus("current")
_PwCepPerf1DayIntervalJtrBfrUnderruns_Type = Counter32
_PwCepPerf1DayIntervalJtrBfrUnderruns_Object = MibTableColumn
pwCepPerf1DayIntervalJtrBfrUnderruns = _PwCepPerf1DayIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 16),
    _PwCepPerf1DayIntervalJtrBfrUnderruns_Type()
)
pwCepPerf1DayIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalJtrBfrUnderruns.setStatus("current")
_PwCepPerf1DayIntervalPktsMalformed_Type = Counter32
_PwCepPerf1DayIntervalPktsMalformed_Object = MibTableColumn
pwCepPerf1DayIntervalPktsMalformed = _PwCepPerf1DayIntervalPktsMalformed_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 17),
    _PwCepPerf1DayIntervalPktsMalformed_Type()
)
pwCepPerf1DayIntervalPktsMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalPktsMalformed.setStatus("current")
_PwCepPerf1DayIntervalSummaryErrors_Type = Counter32
_PwCepPerf1DayIntervalSummaryErrors_Object = MibTableColumn
pwCepPerf1DayIntervalSummaryErrors = _PwCepPerf1DayIntervalSummaryErrors_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 18),
    _PwCepPerf1DayIntervalSummaryErrors_Type()
)
pwCepPerf1DayIntervalSummaryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalSummaryErrors.setStatus("current")
_PwCepPerf1DayIntervalESs_Type = Counter32
_PwCepPerf1DayIntervalESs_Object = MibTableColumn
pwCepPerf1DayIntervalESs = _PwCepPerf1DayIntervalESs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 19),
    _PwCepPerf1DayIntervalESs_Type()
)
pwCepPerf1DayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalESs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalESs.setUnits("seconds")
_PwCepPerf1DayIntervalSESs_Type = Counter32
_PwCepPerf1DayIntervalSESs_Object = MibTableColumn
pwCepPerf1DayIntervalSESs = _PwCepPerf1DayIntervalSESs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 20),
    _PwCepPerf1DayIntervalSESs_Type()
)
pwCepPerf1DayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalSESs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalSESs.setUnits("seconds")
_PwCepPerf1DayIntervalUASs_Type = Counter32
_PwCepPerf1DayIntervalUASs_Object = MibTableColumn
pwCepPerf1DayIntervalUASs = _PwCepPerf1DayIntervalUASs_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 21),
    _PwCepPerf1DayIntervalUASs_Type()
)
pwCepPerf1DayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalUASs.setStatus("current")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalUASs.setUnits("seconds")
_PwCepPerf1DayIntervalFC_Type = Counter32
_PwCepPerf1DayIntervalFC_Object = MibTableColumn
pwCepPerf1DayIntervalFC = _PwCepPerf1DayIntervalFC_Object(
    (1, 3, 6, 1, 2, 1, 200, 1, 7, 1, 22),
    _PwCepPerf1DayIntervalFC_Type()
)
pwCepPerf1DayIntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalFC.setStatus("current")
_PwCepConformance_ObjectIdentity = ObjectIdentity
pwCepConformance = _PwCepConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 200, 2)
)
_PwCepGroups_ObjectIdentity = ObjectIdentity
pwCepGroups = _PwCepGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 200, 2, 1)
)
_PwCepCompliances_ObjectIdentity = ObjectIdentity
pwCepCompliances = _PwCepCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 200, 2, 2)
)

# Managed Objects groups

pwCepGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 200, 2, 1, 1)
)
pwCepGroup.setObjects(
      *(("PW-CEP-STD-MIB", "pwCepType"),
        ("PW-CEP-STD-MIB", "pwCepSonetIfIndex"),
        ("PW-CEP-STD-MIB", "pwCepSonetConfigErrorOrStatus"),
        ("PW-CEP-STD-MIB", "pwCepCfgIndex"),
        ("PW-CEP-STD-MIB", "pwCepTimeElapsed"),
        ("PW-CEP-STD-MIB", "pwCepValidIntervals"),
        ("PW-CEP-STD-MIB", "pwCepIndications"),
        ("PW-CEP-STD-MIB", "pwCepLastEsTimeStamp"))
)
if mibBuilder.loadTexts:
    pwCepGroup.setStatus("current")

pwCepSignalingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 200, 2, 1, 2)
)
pwCepSignalingGroup.setObjects(
    ("PW-CEP-STD-MIB", "pwCepPeerCepOption")
)
if mibBuilder.loadTexts:
    pwCepSignalingGroup.setStatus("current")

pwCepCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 200, 2, 1, 3)
)
pwCepCfgGroup.setObjects(
      *(("PW-CEP-STD-MIB", "pwCepCfgIndexNext"),
        ("PW-CEP-STD-MIB", "pwCepSonetPayloadLength"),
        ("PW-CEP-STD-MIB", "pwCepCfgMinPktLength"),
        ("PW-CEP-STD-MIB", "pwCepCfgPktReorder"),
        ("PW-CEP-STD-MIB", "pwCepCfgEnableDBA"),
        ("PW-CEP-STD-MIB", "pwCepCfgRtpHdrSuppress"),
        ("PW-CEP-STD-MIB", "pwCepCfgJtrBfrDepth"),
        ("PW-CEP-STD-MIB", "pwCepCfgConsecPktsInsync"),
        ("PW-CEP-STD-MIB", "pwCepCfgConsecMissingOutSync"),
        ("PW-CEP-STD-MIB", "pwCepCfgPktErrorPlayOutValue"),
        ("PW-CEP-STD-MIB", "pwCepCfgMissingPktsToSes"),
        ("PW-CEP-STD-MIB", "pwCepCfgSesToUas"),
        ("PW-CEP-STD-MIB", "pwCepCfgSecsToExitUas"),
        ("PW-CEP-STD-MIB", "pwCepCfgName"),
        ("PW-CEP-STD-MIB", "pwCepCfgRowStatus"),
        ("PW-CEP-STD-MIB", "pwCepCfgStorageType"))
)
if mibBuilder.loadTexts:
    pwCepCfgGroup.setStatus("current")

pwCepPerfCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 200, 2, 1, 4)
)
pwCepPerfCurrentGroup.setObjects(
      *(("PW-CEP-STD-MIB", "pwCepPerfCurrentDbaInPacketsHC"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentDbaOutPacketsHC"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentInNegPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentInPosPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentInPtrAdjustSecs"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentOutNegPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentOutPosPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentOutPtrAdjustSecs"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentAbsPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentMissingPkts"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentPktsOoseq"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentPktsOoRngDropped"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentJtrBfrUnderruns"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentPktsMalformed"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentSummaryErrors"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentESs"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentSESs"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentUASs"),
        ("PW-CEP-STD-MIB", "pwCepPerfCurrentFC"))
)
if mibBuilder.loadTexts:
    pwCepPerfCurrentGroup.setStatus("current")

pwCepPerfIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 200, 2, 1, 5)
)
pwCepPerfIntervalGroup.setObjects(
      *(("PW-CEP-STD-MIB", "pwCepPerfIntervalValidData"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalReset"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalTimeElapsed"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalDbaInPacketsHC"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalDbaOutPacketsHC"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalInNegPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalInPosPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalInPtrAdjustSecs"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalOutNegPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalOutPosPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalOutPtrAdjustSecs"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalAbsPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalMissingPkts"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalPktsOoseq"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalPktsOoRngDropped"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalJtrBfrUnderruns"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalPktsMalformed"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalSummaryErrors"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalESs"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalSESs"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalUASs"),
        ("PW-CEP-STD-MIB", "pwCepPerfIntervalFC"))
)
if mibBuilder.loadTexts:
    pwCepPerfIntervalGroup.setStatus("current")

pwCepPerf1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 200, 2, 1, 6)
)
pwCepPerf1DayIntervalGroup.setObjects(
      *(("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalValidData"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalMoniSecs"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalDbaInPacketsHC"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalDbaOutPacketsHC"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalInNegPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalInPosPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalInPtrAdjustSecs"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalOutNegPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalOutPosPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalOutPtrAdjustSecs"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalAbsPtrAdjust"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalMissingPkts"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalPktsOoseq"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalPktsOoRngDropped"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalJtrBfrUnderruns"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalPktsMalformed"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalSummaryErrors"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalESs"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalSESs"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalUASs"),
        ("PW-CEP-STD-MIB", "pwCepPerf1DayIntervalFC"))
)
if mibBuilder.loadTexts:
    pwCepPerf1DayIntervalGroup.setStatus("current")

pwCepFractionalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 200, 2, 1, 7)
)
pwCepFractionalGroup.setObjects(
      *(("PW-CEP-STD-MIB", "pwCepFracRowStatus"),
        ("PW-CEP-STD-MIB", "pwCepFracStorageType"))
)
if mibBuilder.loadTexts:
    pwCepFractionalGroup.setStatus("current")

pwCepFractionalSts1Vc3Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 200, 2, 1, 8)
)
pwCepFractionalSts1Vc3Group.setObjects(
      *(("PW-CEP-STD-MIB", "pwCepFracMode"),
        ("PW-CEP-STD-MIB", "pwCepFracConfigError"),
        ("PW-CEP-STD-MIB", "pwCepFracAsync"),
        ("PW-CEP-STD-MIB", "pwCepFracVtgMap"),
        ("PW-CEP-STD-MIB", "pwCepFracEbm"),
        ("PW-CEP-STD-MIB", "pwCepFracPeerEbm"))
)
if mibBuilder.loadTexts:
    pwCepFractionalSts1Vc3Group.setStatus("current")

pwCepFractionalVc4Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 200, 2, 1, 9)
)
pwCepFractionalVc4Group.setObjects(
      *(("PW-CEP-STD-MIB", "pwCepFracSdhVc4Mode"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4Tu3Map1"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4Tu3Map2"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4Tu3Map3"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4Tug2Map1"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4Tug2Map2"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4Tug2Map3"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4Ebm1"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4Ebm2"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4Ebm3"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4PeerEbm1"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4PeerEbm2"),
        ("PW-CEP-STD-MIB", "pwCepFracSdhVc4PeerEbm3"))
)
if mibBuilder.loadTexts:
    pwCepFractionalVc4Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pwCepModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 200, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pwCepModuleFullCompliance.setStatus(
        "current"
    )

pwCepModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 200, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pwCepModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PW-CEP-STD-MIB",
    **{"PwCepSonetEbm": PwCepSonetEbm,
       "PwCepSdhVc4Ebm": PwCepSdhVc4Ebm,
       "PwCepSonetVtgMap": PwCepSonetVtgMap,
       "PwCepFracAsyncMap": PwCepFracAsyncMap,
       "pwCepStdMIB": pwCepStdMIB,
       "pwCepObjects": pwCepObjects,
       "pwCepTable": pwCepTable,
       "pwCepEntry": pwCepEntry,
       "pwCepType": pwCepType,
       "pwCepSonetIfIndex": pwCepSonetIfIndex,
       "pwCepSonetConfigErrorOrStatus": pwCepSonetConfigErrorOrStatus,
       "pwCepCfgIndex": pwCepCfgIndex,
       "pwCepTimeElapsed": pwCepTimeElapsed,
       "pwCepValidIntervals": pwCepValidIntervals,
       "pwCepIndications": pwCepIndications,
       "pwCepLastEsTimeStamp": pwCepLastEsTimeStamp,
       "pwCepPeerCepOption": pwCepPeerCepOption,
       "pwCepCfgIndexNext": pwCepCfgIndexNext,
       "pwCepCfgTable": pwCepCfgTable,
       "pwCepCfgEntry": pwCepCfgEntry,
       "pwCepCfgTableIndex": pwCepCfgTableIndex,
       "pwCepSonetPayloadLength": pwCepSonetPayloadLength,
       "pwCepCfgMinPktLength": pwCepCfgMinPktLength,
       "pwCepCfgPktReorder": pwCepCfgPktReorder,
       "pwCepCfgEnableDBA": pwCepCfgEnableDBA,
       "pwCepCfgRtpHdrSuppress": pwCepCfgRtpHdrSuppress,
       "pwCepCfgJtrBfrDepth": pwCepCfgJtrBfrDepth,
       "pwCepCfgConsecPktsInsync": pwCepCfgConsecPktsInsync,
       "pwCepCfgConsecMissingOutSync": pwCepCfgConsecMissingOutSync,
       "pwCepCfgPktErrorPlayOutValue": pwCepCfgPktErrorPlayOutValue,
       "pwCepCfgMissingPktsToSes": pwCepCfgMissingPktsToSes,
       "pwCepCfgSesToUas": pwCepCfgSesToUas,
       "pwCepCfgSecsToExitUas": pwCepCfgSecsToExitUas,
       "pwCepCfgName": pwCepCfgName,
       "pwCepCfgRowStatus": pwCepCfgRowStatus,
       "pwCepCfgStorageType": pwCepCfgStorageType,
       "pwCepFracTable": pwCepFracTable,
       "pwCepFracEntry": pwCepFracEntry,
       "pwCepFracIndex": pwCepFracIndex,
       "pwCepFracMode": pwCepFracMode,
       "pwCepFracConfigError": pwCepFracConfigError,
       "pwCepFracAsync": pwCepFracAsync,
       "pwCepFracVtgMap": pwCepFracVtgMap,
       "pwCepFracEbm": pwCepFracEbm,
       "pwCepFracPeerEbm": pwCepFracPeerEbm,
       "pwCepFracSdhVc4Mode": pwCepFracSdhVc4Mode,
       "pwCepFracSdhVc4Tu3Map1": pwCepFracSdhVc4Tu3Map1,
       "pwCepFracSdhVc4Tu3Map2": pwCepFracSdhVc4Tu3Map2,
       "pwCepFracSdhVc4Tu3Map3": pwCepFracSdhVc4Tu3Map3,
       "pwCepFracSdhVc4Tug2Map1": pwCepFracSdhVc4Tug2Map1,
       "pwCepFracSdhVc4Tug2Map2": pwCepFracSdhVc4Tug2Map2,
       "pwCepFracSdhVc4Tug2Map3": pwCepFracSdhVc4Tug2Map3,
       "pwCepFracSdhVc4Ebm1": pwCepFracSdhVc4Ebm1,
       "pwCepFracSdhVc4Ebm2": pwCepFracSdhVc4Ebm2,
       "pwCepFracSdhVc4Ebm3": pwCepFracSdhVc4Ebm3,
       "pwCepFracSdhVc4PeerEbm1": pwCepFracSdhVc4PeerEbm1,
       "pwCepFracSdhVc4PeerEbm2": pwCepFracSdhVc4PeerEbm2,
       "pwCepFracSdhVc4PeerEbm3": pwCepFracSdhVc4PeerEbm3,
       "pwCepFracRowStatus": pwCepFracRowStatus,
       "pwCepFracStorageType": pwCepFracStorageType,
       "pwCepPerfCurrentTable": pwCepPerfCurrentTable,
       "pwCepPerfCurrentEntry": pwCepPerfCurrentEntry,
       "pwCepPerfCurrentDbaInPacketsHC": pwCepPerfCurrentDbaInPacketsHC,
       "pwCepPerfCurrentDbaOutPacketsHC": pwCepPerfCurrentDbaOutPacketsHC,
       "pwCepPerfCurrentInNegPtrAdjust": pwCepPerfCurrentInNegPtrAdjust,
       "pwCepPerfCurrentInPosPtrAdjust": pwCepPerfCurrentInPosPtrAdjust,
       "pwCepPerfCurrentInPtrAdjustSecs": pwCepPerfCurrentInPtrAdjustSecs,
       "pwCepPerfCurrentOutNegPtrAdjust": pwCepPerfCurrentOutNegPtrAdjust,
       "pwCepPerfCurrentOutPosPtrAdjust": pwCepPerfCurrentOutPosPtrAdjust,
       "pwCepPerfCurrentOutPtrAdjustSecs": pwCepPerfCurrentOutPtrAdjustSecs,
       "pwCepPerfCurrentAbsPtrAdjust": pwCepPerfCurrentAbsPtrAdjust,
       "pwCepPerfCurrentMissingPkts": pwCepPerfCurrentMissingPkts,
       "pwCepPerfCurrentPktsOoseq": pwCepPerfCurrentPktsOoseq,
       "pwCepPerfCurrentPktsOoRngDropped": pwCepPerfCurrentPktsOoRngDropped,
       "pwCepPerfCurrentJtrBfrUnderruns": pwCepPerfCurrentJtrBfrUnderruns,
       "pwCepPerfCurrentPktsMalformed": pwCepPerfCurrentPktsMalformed,
       "pwCepPerfCurrentSummaryErrors": pwCepPerfCurrentSummaryErrors,
       "pwCepPerfCurrentESs": pwCepPerfCurrentESs,
       "pwCepPerfCurrentSESs": pwCepPerfCurrentSESs,
       "pwCepPerfCurrentUASs": pwCepPerfCurrentUASs,
       "pwCepPerfCurrentFC": pwCepPerfCurrentFC,
       "pwCepPerfIntervalTable": pwCepPerfIntervalTable,
       "pwCepPerfIntervalEntry": pwCepPerfIntervalEntry,
       "pwCepPerfIntervalNumber": pwCepPerfIntervalNumber,
       "pwCepPerfIntervalValidData": pwCepPerfIntervalValidData,
       "pwCepPerfIntervalReset": pwCepPerfIntervalReset,
       "pwCepPerfIntervalTimeElapsed": pwCepPerfIntervalTimeElapsed,
       "pwCepPerfIntervalDbaInPacketsHC": pwCepPerfIntervalDbaInPacketsHC,
       "pwCepPerfIntervalDbaOutPacketsHC": pwCepPerfIntervalDbaOutPacketsHC,
       "pwCepPerfIntervalInNegPtrAdjust": pwCepPerfIntervalInNegPtrAdjust,
       "pwCepPerfIntervalInPosPtrAdjust": pwCepPerfIntervalInPosPtrAdjust,
       "pwCepPerfIntervalInPtrAdjustSecs": pwCepPerfIntervalInPtrAdjustSecs,
       "pwCepPerfIntervalOutNegPtrAdjust": pwCepPerfIntervalOutNegPtrAdjust,
       "pwCepPerfIntervalOutPosPtrAdjust": pwCepPerfIntervalOutPosPtrAdjust,
       "pwCepPerfIntervalOutPtrAdjustSecs": pwCepPerfIntervalOutPtrAdjustSecs,
       "pwCepPerfIntervalAbsPtrAdjust": pwCepPerfIntervalAbsPtrAdjust,
       "pwCepPerfIntervalMissingPkts": pwCepPerfIntervalMissingPkts,
       "pwCepPerfIntervalPktsOoseq": pwCepPerfIntervalPktsOoseq,
       "pwCepPerfIntervalPktsOoRngDropped": pwCepPerfIntervalPktsOoRngDropped,
       "pwCepPerfIntervalJtrBfrUnderruns": pwCepPerfIntervalJtrBfrUnderruns,
       "pwCepPerfIntervalPktsMalformed": pwCepPerfIntervalPktsMalformed,
       "pwCepPerfIntervalSummaryErrors": pwCepPerfIntervalSummaryErrors,
       "pwCepPerfIntervalESs": pwCepPerfIntervalESs,
       "pwCepPerfIntervalSESs": pwCepPerfIntervalSESs,
       "pwCepPerfIntervalUASs": pwCepPerfIntervalUASs,
       "pwCepPerfIntervalFC": pwCepPerfIntervalFC,
       "pwCepPerf1DayIntervalTable": pwCepPerf1DayIntervalTable,
       "pwCepPerf1DayIntervalEntry": pwCepPerf1DayIntervalEntry,
       "pwCepPerf1DayIntervalNumber": pwCepPerf1DayIntervalNumber,
       "pwCepPerf1DayIntervalValidData": pwCepPerf1DayIntervalValidData,
       "pwCepPerf1DayIntervalMoniSecs": pwCepPerf1DayIntervalMoniSecs,
       "pwCepPerf1DayIntervalDbaInPacketsHC": pwCepPerf1DayIntervalDbaInPacketsHC,
       "pwCepPerf1DayIntervalDbaOutPacketsHC": pwCepPerf1DayIntervalDbaOutPacketsHC,
       "pwCepPerf1DayIntervalInNegPtrAdjust": pwCepPerf1DayIntervalInNegPtrAdjust,
       "pwCepPerf1DayIntervalInPosPtrAdjust": pwCepPerf1DayIntervalInPosPtrAdjust,
       "pwCepPerf1DayIntervalInPtrAdjustSecs": pwCepPerf1DayIntervalInPtrAdjustSecs,
       "pwCepPerf1DayIntervalOutNegPtrAdjust": pwCepPerf1DayIntervalOutNegPtrAdjust,
       "pwCepPerf1DayIntervalOutPosPtrAdjust": pwCepPerf1DayIntervalOutPosPtrAdjust,
       "pwCepPerf1DayIntervalOutPtrAdjustSecs": pwCepPerf1DayIntervalOutPtrAdjustSecs,
       "pwCepPerf1DayIntervalAbsPtrAdjust": pwCepPerf1DayIntervalAbsPtrAdjust,
       "pwCepPerf1DayIntervalMissingPkts": pwCepPerf1DayIntervalMissingPkts,
       "pwCepPerf1DayIntervalPktsOoseq": pwCepPerf1DayIntervalPktsOoseq,
       "pwCepPerf1DayIntervalPktsOoRngDropped": pwCepPerf1DayIntervalPktsOoRngDropped,
       "pwCepPerf1DayIntervalJtrBfrUnderruns": pwCepPerf1DayIntervalJtrBfrUnderruns,
       "pwCepPerf1DayIntervalPktsMalformed": pwCepPerf1DayIntervalPktsMalformed,
       "pwCepPerf1DayIntervalSummaryErrors": pwCepPerf1DayIntervalSummaryErrors,
       "pwCepPerf1DayIntervalESs": pwCepPerf1DayIntervalESs,
       "pwCepPerf1DayIntervalSESs": pwCepPerf1DayIntervalSESs,
       "pwCepPerf1DayIntervalUASs": pwCepPerf1DayIntervalUASs,
       "pwCepPerf1DayIntervalFC": pwCepPerf1DayIntervalFC,
       "pwCepConformance": pwCepConformance,
       "pwCepGroups": pwCepGroups,
       "pwCepGroup": pwCepGroup,
       "pwCepSignalingGroup": pwCepSignalingGroup,
       "pwCepCfgGroup": pwCepCfgGroup,
       "pwCepPerfCurrentGroup": pwCepPerfCurrentGroup,
       "pwCepPerfIntervalGroup": pwCepPerfIntervalGroup,
       "pwCepPerf1DayIntervalGroup": pwCepPerf1DayIntervalGroup,
       "pwCepFractionalGroup": pwCepFractionalGroup,
       "pwCepFractionalSts1Vc3Group": pwCepFractionalSts1Vc3Group,
       "pwCepFractionalVc4Group": pwCepFractionalVc4Group,
       "pwCepCompliances": pwCepCompliances,
       "pwCepModuleFullCompliance": pwCepModuleFullCompliance,
       "pwCepModuleReadOnlyCompliance": pwCepModuleReadOnlyCompliance}
)
