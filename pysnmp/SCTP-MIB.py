# SNMP MIB module (SCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:10 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

sctpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 104)
)
sctpMIB.setRevisions(
        ("2004-09-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SctpObjects_ObjectIdentity = ObjectIdentity
sctpObjects = _SctpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 104, 1)
)
_SctpStats_ObjectIdentity = ObjectIdentity
sctpStats = _SctpStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 104, 1, 1)
)
_SctpCurrEstab_Type = Gauge32
_SctpCurrEstab_Object = MibScalar
sctpCurrEstab = _SctpCurrEstab_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 1),
    _SctpCurrEstab_Type()
)
sctpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpCurrEstab.setStatus("current")
_SctpActiveEstabs_Type = Counter32
_SctpActiveEstabs_Object = MibScalar
sctpActiveEstabs = _SctpActiveEstabs_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 2),
    _SctpActiveEstabs_Type()
)
sctpActiveEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpActiveEstabs.setStatus("current")
_SctpPassiveEstabs_Type = Counter32
_SctpPassiveEstabs_Object = MibScalar
sctpPassiveEstabs = _SctpPassiveEstabs_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 3),
    _SctpPassiveEstabs_Type()
)
sctpPassiveEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpPassiveEstabs.setStatus("current")
_SctpAborteds_Type = Counter32
_SctpAborteds_Object = MibScalar
sctpAborteds = _SctpAborteds_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 4),
    _SctpAborteds_Type()
)
sctpAborteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAborteds.setStatus("current")
_SctpShutdowns_Type = Counter32
_SctpShutdowns_Object = MibScalar
sctpShutdowns = _SctpShutdowns_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 5),
    _SctpShutdowns_Type()
)
sctpShutdowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpShutdowns.setStatus("current")
_SctpOutOfBlues_Type = Counter32
_SctpOutOfBlues_Object = MibScalar
sctpOutOfBlues = _SctpOutOfBlues_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 6),
    _SctpOutOfBlues_Type()
)
sctpOutOfBlues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpOutOfBlues.setStatus("current")
_SctpChecksumErrors_Type = Counter32
_SctpChecksumErrors_Object = MibScalar
sctpChecksumErrors = _SctpChecksumErrors_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 7),
    _SctpChecksumErrors_Type()
)
sctpChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpChecksumErrors.setStatus("current")
_SctpOutCtrlChunks_Type = Counter64
_SctpOutCtrlChunks_Object = MibScalar
sctpOutCtrlChunks = _SctpOutCtrlChunks_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 8),
    _SctpOutCtrlChunks_Type()
)
sctpOutCtrlChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpOutCtrlChunks.setStatus("current")
_SctpOutOrderChunks_Type = Counter64
_SctpOutOrderChunks_Object = MibScalar
sctpOutOrderChunks = _SctpOutOrderChunks_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 9),
    _SctpOutOrderChunks_Type()
)
sctpOutOrderChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpOutOrderChunks.setStatus("current")
_SctpOutUnorderChunks_Type = Counter64
_SctpOutUnorderChunks_Object = MibScalar
sctpOutUnorderChunks = _SctpOutUnorderChunks_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 10),
    _SctpOutUnorderChunks_Type()
)
sctpOutUnorderChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpOutUnorderChunks.setStatus("current")
_SctpInCtrlChunks_Type = Counter64
_SctpInCtrlChunks_Object = MibScalar
sctpInCtrlChunks = _SctpInCtrlChunks_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 11),
    _SctpInCtrlChunks_Type()
)
sctpInCtrlChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpInCtrlChunks.setStatus("current")
_SctpInOrderChunks_Type = Counter64
_SctpInOrderChunks_Object = MibScalar
sctpInOrderChunks = _SctpInOrderChunks_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 12),
    _SctpInOrderChunks_Type()
)
sctpInOrderChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpInOrderChunks.setStatus("current")
_SctpInUnorderChunks_Type = Counter64
_SctpInUnorderChunks_Object = MibScalar
sctpInUnorderChunks = _SctpInUnorderChunks_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 13),
    _SctpInUnorderChunks_Type()
)
sctpInUnorderChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpInUnorderChunks.setStatus("current")
_SctpFragUsrMsgs_Type = Counter64
_SctpFragUsrMsgs_Object = MibScalar
sctpFragUsrMsgs = _SctpFragUsrMsgs_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 14),
    _SctpFragUsrMsgs_Type()
)
sctpFragUsrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpFragUsrMsgs.setStatus("current")
_SctpReasmUsrMsgs_Type = Counter64
_SctpReasmUsrMsgs_Object = MibScalar
sctpReasmUsrMsgs = _SctpReasmUsrMsgs_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 15),
    _SctpReasmUsrMsgs_Type()
)
sctpReasmUsrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpReasmUsrMsgs.setStatus("current")
_SctpOutSCTPPacks_Type = Counter64
_SctpOutSCTPPacks_Object = MibScalar
sctpOutSCTPPacks = _SctpOutSCTPPacks_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 16),
    _SctpOutSCTPPacks_Type()
)
sctpOutSCTPPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpOutSCTPPacks.setStatus("current")
_SctpInSCTPPacks_Type = Counter64
_SctpInSCTPPacks_Object = MibScalar
sctpInSCTPPacks = _SctpInSCTPPacks_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 17),
    _SctpInSCTPPacks_Type()
)
sctpInSCTPPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpInSCTPPacks.setStatus("current")
_SctpDiscontinuityTime_Type = TimeStamp
_SctpDiscontinuityTime_Object = MibScalar
sctpDiscontinuityTime = _SctpDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 1, 18),
    _SctpDiscontinuityTime_Type()
)
sctpDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpDiscontinuityTime.setStatus("current")
_SctpParams_ObjectIdentity = ObjectIdentity
sctpParams = _SctpParams_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 104, 1, 2)
)


class _SctpRtoAlgorithm_Type(Integer32):
    """Custom type sctpRtoAlgorithm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("vanj", 2))
    )


_SctpRtoAlgorithm_Type.__name__ = "Integer32"
_SctpRtoAlgorithm_Object = MibScalar
sctpRtoAlgorithm = _SctpRtoAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 2, 1),
    _SctpRtoAlgorithm_Type()
)
sctpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpRtoAlgorithm.setStatus("current")


class _SctpRtoMin_Type(Unsigned32):
    """Custom type sctpRtoMin based on Unsigned32"""
    defaultValue = 1000


_SctpRtoMin_Object = MibScalar
sctpRtoMin = _SctpRtoMin_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 2, 2),
    _SctpRtoMin_Type()
)
sctpRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpRtoMin.setStatus("current")
if mibBuilder.loadTexts:
    sctpRtoMin.setUnits("milliseconds")


class _SctpRtoMax_Type(Unsigned32):
    """Custom type sctpRtoMax based on Unsigned32"""
    defaultValue = 60000


_SctpRtoMax_Object = MibScalar
sctpRtoMax = _SctpRtoMax_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 2, 3),
    _SctpRtoMax_Type()
)
sctpRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    sctpRtoMax.setUnits("milliseconds")


class _SctpRtoInitial_Type(Unsigned32):
    """Custom type sctpRtoInitial based on Unsigned32"""
    defaultValue = 3000


_SctpRtoInitial_Object = MibScalar
sctpRtoInitial = _SctpRtoInitial_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 2, 4),
    _SctpRtoInitial_Type()
)
sctpRtoInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpRtoInitial.setStatus("current")
if mibBuilder.loadTexts:
    sctpRtoInitial.setUnits("milliseconds")


class _SctpMaxAssocs_Type(Integer32):
    """Custom type sctpMaxAssocs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SctpMaxAssocs_Type.__name__ = "Integer32"
_SctpMaxAssocs_Object = MibScalar
sctpMaxAssocs = _SctpMaxAssocs_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 2, 5),
    _SctpMaxAssocs_Type()
)
sctpMaxAssocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpMaxAssocs.setStatus("current")


class _SctpValCookieLife_Type(Unsigned32):
    """Custom type sctpValCookieLife based on Unsigned32"""
    defaultValue = 60000


_SctpValCookieLife_Object = MibScalar
sctpValCookieLife = _SctpValCookieLife_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 2, 6),
    _SctpValCookieLife_Type()
)
sctpValCookieLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpValCookieLife.setStatus("current")
if mibBuilder.loadTexts:
    sctpValCookieLife.setUnits("milliseconds")


class _SctpMaxInitRetr_Type(Unsigned32):
    """Custom type sctpMaxInitRetr based on Unsigned32"""
    defaultValue = 8


_SctpMaxInitRetr_Object = MibScalar
sctpMaxInitRetr = _SctpMaxInitRetr_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 2, 7),
    _SctpMaxInitRetr_Type()
)
sctpMaxInitRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpMaxInitRetr.setStatus("current")
_SctpAssocTable_Object = MibTable
sctpAssocTable = _SctpAssocTable_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3)
)
if mibBuilder.loadTexts:
    sctpAssocTable.setStatus("current")
_SctpAssocEntry_Object = MibTableRow
sctpAssocEntry = _SctpAssocEntry_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1)
)
sctpAssocEntry.setIndexNames(
    (0, "SCTP-MIB", "sctpAssocId"),
)
if mibBuilder.loadTexts:
    sctpAssocEntry.setStatus("current")


class _SctpAssocId_Type(Unsigned32):
    """Custom type sctpAssocId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SctpAssocId_Type.__name__ = "Unsigned32"
_SctpAssocId_Object = MibTableColumn
sctpAssocId = _SctpAssocId_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 1),
    _SctpAssocId_Type()
)
sctpAssocId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sctpAssocId.setStatus("current")


class _SctpAssocRemHostName_Type(OctetString):
    """Custom type sctpAssocRemHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SctpAssocRemHostName_Type.__name__ = "OctetString"
_SctpAssocRemHostName_Object = MibTableColumn
sctpAssocRemHostName = _SctpAssocRemHostName_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 2),
    _SctpAssocRemHostName_Type()
)
sctpAssocRemHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRemHostName.setStatus("current")


class _SctpAssocLocalPort_Type(InetPortNumber):
    """Custom type sctpAssocLocalPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SctpAssocLocalPort_Type.__name__ = "InetPortNumber"
_SctpAssocLocalPort_Object = MibTableColumn
sctpAssocLocalPort = _SctpAssocLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 3),
    _SctpAssocLocalPort_Type()
)
sctpAssocLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocLocalPort.setStatus("current")


class _SctpAssocRemPort_Type(InetPortNumber):
    """Custom type sctpAssocRemPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SctpAssocRemPort_Type.__name__ = "InetPortNumber"
_SctpAssocRemPort_Object = MibTableColumn
sctpAssocRemPort = _SctpAssocRemPort_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 4),
    _SctpAssocRemPort_Type()
)
sctpAssocRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRemPort.setStatus("current")
_SctpAssocRemPrimAddrType_Type = InetAddressType
_SctpAssocRemPrimAddrType_Object = MibTableColumn
sctpAssocRemPrimAddrType = _SctpAssocRemPrimAddrType_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 5),
    _SctpAssocRemPrimAddrType_Type()
)
sctpAssocRemPrimAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRemPrimAddrType.setStatus("current")
_SctpAssocRemPrimAddr_Type = InetAddress
_SctpAssocRemPrimAddr_Object = MibTableColumn
sctpAssocRemPrimAddr = _SctpAssocRemPrimAddr_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 6),
    _SctpAssocRemPrimAddr_Type()
)
sctpAssocRemPrimAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRemPrimAddr.setStatus("current")


class _SctpAssocHeartBeatInterval_Type(Unsigned32):
    """Custom type sctpAssocHeartBeatInterval based on Unsigned32"""
    defaultValue = 30000


_SctpAssocHeartBeatInterval_Object = MibTableColumn
sctpAssocHeartBeatInterval = _SctpAssocHeartBeatInterval_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 7),
    _SctpAssocHeartBeatInterval_Type()
)
sctpAssocHeartBeatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocHeartBeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    sctpAssocHeartBeatInterval.setUnits("milliseconds")


class _SctpAssocState_Type(Integer32):
    """Custom type sctpAssocState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("cookieEchoed", 3),
          ("cookieWait", 2),
          ("deleteTCB", 9),
          ("established", 4),
          ("shutdownAckSent", 8),
          ("shutdownPending", 5),
          ("shutdownReceived", 7),
          ("shutdownSent", 6))
    )


_SctpAssocState_Type.__name__ = "Integer32"
_SctpAssocState_Object = MibTableColumn
sctpAssocState = _SctpAssocState_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 8),
    _SctpAssocState_Type()
)
sctpAssocState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sctpAssocState.setStatus("current")


class _SctpAssocInStreams_Type(Unsigned32):
    """Custom type sctpAssocInStreams based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SctpAssocInStreams_Type.__name__ = "Unsigned32"
_SctpAssocInStreams_Object = MibTableColumn
sctpAssocInStreams = _SctpAssocInStreams_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 9),
    _SctpAssocInStreams_Type()
)
sctpAssocInStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocInStreams.setStatus("current")


class _SctpAssocOutStreams_Type(Unsigned32):
    """Custom type sctpAssocOutStreams based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SctpAssocOutStreams_Type.__name__ = "Unsigned32"
_SctpAssocOutStreams_Object = MibTableColumn
sctpAssocOutStreams = _SctpAssocOutStreams_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 10),
    _SctpAssocOutStreams_Type()
)
sctpAssocOutStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocOutStreams.setStatus("current")


class _SctpAssocMaxRetr_Type(Unsigned32):
    """Custom type sctpAssocMaxRetr based on Unsigned32"""
    defaultValue = 10


_SctpAssocMaxRetr_Object = MibTableColumn
sctpAssocMaxRetr = _SctpAssocMaxRetr_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 11),
    _SctpAssocMaxRetr_Type()
)
sctpAssocMaxRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocMaxRetr.setStatus("current")
_SctpAssocPrimProcess_Type = Unsigned32
_SctpAssocPrimProcess_Object = MibTableColumn
sctpAssocPrimProcess = _SctpAssocPrimProcess_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 12),
    _SctpAssocPrimProcess_Type()
)
sctpAssocPrimProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocPrimProcess.setStatus("current")
_SctpAssocT1expireds_Type = Counter32
_SctpAssocT1expireds_Object = MibTableColumn
sctpAssocT1expireds = _SctpAssocT1expireds_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 13),
    _SctpAssocT1expireds_Type()
)
sctpAssocT1expireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocT1expireds.setStatus("current")
_SctpAssocT2expireds_Type = Counter32
_SctpAssocT2expireds_Object = MibTableColumn
sctpAssocT2expireds = _SctpAssocT2expireds_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 14),
    _SctpAssocT2expireds_Type()
)
sctpAssocT2expireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocT2expireds.setStatus("current")
_SctpAssocRtxChunks_Type = Counter32
_SctpAssocRtxChunks_Object = MibTableColumn
sctpAssocRtxChunks = _SctpAssocRtxChunks_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 15),
    _SctpAssocRtxChunks_Type()
)
sctpAssocRtxChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRtxChunks.setStatus("current")
_SctpAssocStartTime_Type = TimeStamp
_SctpAssocStartTime_Object = MibTableColumn
sctpAssocStartTime = _SctpAssocStartTime_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 16),
    _SctpAssocStartTime_Type()
)
sctpAssocStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocStartTime.setStatus("current")
_SctpAssocDiscontinuityTime_Type = TimeStamp
_SctpAssocDiscontinuityTime_Object = MibTableColumn
sctpAssocDiscontinuityTime = _SctpAssocDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 3, 1, 17),
    _SctpAssocDiscontinuityTime_Type()
)
sctpAssocDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocDiscontinuityTime.setStatus("current")
_SctpAssocLocalAddrTable_Object = MibTable
sctpAssocLocalAddrTable = _SctpAssocLocalAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 4)
)
if mibBuilder.loadTexts:
    sctpAssocLocalAddrTable.setStatus("current")
_SctpAssocLocalAddrEntry_Object = MibTableRow
sctpAssocLocalAddrEntry = _SctpAssocLocalAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 4, 1)
)
sctpAssocLocalAddrEntry.setIndexNames(
    (0, "SCTP-MIB", "sctpAssocId"),
    (0, "SCTP-MIB", "sctpAssocLocalAddrType"),
    (0, "SCTP-MIB", "sctpAssocLocalAddr"),
)
if mibBuilder.loadTexts:
    sctpAssocLocalAddrEntry.setStatus("current")
_SctpAssocLocalAddrType_Type = InetAddressType
_SctpAssocLocalAddrType_Object = MibTableColumn
sctpAssocLocalAddrType = _SctpAssocLocalAddrType_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 4, 1, 1),
    _SctpAssocLocalAddrType_Type()
)
sctpAssocLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sctpAssocLocalAddrType.setStatus("current")
_SctpAssocLocalAddr_Type = InetAddress
_SctpAssocLocalAddr_Object = MibTableColumn
sctpAssocLocalAddr = _SctpAssocLocalAddr_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 4, 1, 2),
    _SctpAssocLocalAddr_Type()
)
sctpAssocLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sctpAssocLocalAddr.setStatus("current")
_SctpAssocLocalAddrStartTime_Type = TimeStamp
_SctpAssocLocalAddrStartTime_Object = MibTableColumn
sctpAssocLocalAddrStartTime = _SctpAssocLocalAddrStartTime_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 4, 1, 3),
    _SctpAssocLocalAddrStartTime_Type()
)
sctpAssocLocalAddrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocLocalAddrStartTime.setStatus("current")
_SctpAssocRemAddrTable_Object = MibTable
sctpAssocRemAddrTable = _SctpAssocRemAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 5)
)
if mibBuilder.loadTexts:
    sctpAssocRemAddrTable.setStatus("current")
_SctpAssocRemAddrEntry_Object = MibTableRow
sctpAssocRemAddrEntry = _SctpAssocRemAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 5, 1)
)
sctpAssocRemAddrEntry.setIndexNames(
    (0, "SCTP-MIB", "sctpAssocId"),
    (0, "SCTP-MIB", "sctpAssocRemAddrType"),
    (0, "SCTP-MIB", "sctpAssocRemAddr"),
)
if mibBuilder.loadTexts:
    sctpAssocRemAddrEntry.setStatus("current")
_SctpAssocRemAddrType_Type = InetAddressType
_SctpAssocRemAddrType_Object = MibTableColumn
sctpAssocRemAddrType = _SctpAssocRemAddrType_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 1),
    _SctpAssocRemAddrType_Type()
)
sctpAssocRemAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sctpAssocRemAddrType.setStatus("current")
_SctpAssocRemAddr_Type = InetAddress
_SctpAssocRemAddr_Object = MibTableColumn
sctpAssocRemAddr = _SctpAssocRemAddr_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 2),
    _SctpAssocRemAddr_Type()
)
sctpAssocRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sctpAssocRemAddr.setStatus("current")
_SctpAssocRemAddrActive_Type = TruthValue
_SctpAssocRemAddrActive_Object = MibTableColumn
sctpAssocRemAddrActive = _SctpAssocRemAddrActive_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 3),
    _SctpAssocRemAddrActive_Type()
)
sctpAssocRemAddrActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRemAddrActive.setStatus("current")
_SctpAssocRemAddrHBActive_Type = TruthValue
_SctpAssocRemAddrHBActive_Object = MibTableColumn
sctpAssocRemAddrHBActive = _SctpAssocRemAddrHBActive_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 4),
    _SctpAssocRemAddrHBActive_Type()
)
sctpAssocRemAddrHBActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRemAddrHBActive.setStatus("current")
_SctpAssocRemAddrRTO_Type = Unsigned32
_SctpAssocRemAddrRTO_Object = MibTableColumn
sctpAssocRemAddrRTO = _SctpAssocRemAddrRTO_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 5),
    _SctpAssocRemAddrRTO_Type()
)
sctpAssocRemAddrRTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRemAddrRTO.setStatus("current")
if mibBuilder.loadTexts:
    sctpAssocRemAddrRTO.setUnits("milliseconds")


class _SctpAssocRemAddrMaxPathRtx_Type(Unsigned32):
    """Custom type sctpAssocRemAddrMaxPathRtx based on Unsigned32"""
    defaultValue = 5


_SctpAssocRemAddrMaxPathRtx_Object = MibTableColumn
sctpAssocRemAddrMaxPathRtx = _SctpAssocRemAddrMaxPathRtx_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 6),
    _SctpAssocRemAddrMaxPathRtx_Type()
)
sctpAssocRemAddrMaxPathRtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRemAddrMaxPathRtx.setStatus("current")
_SctpAssocRemAddrRtx_Type = Counter32
_SctpAssocRemAddrRtx_Object = MibTableColumn
sctpAssocRemAddrRtx = _SctpAssocRemAddrRtx_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 7),
    _SctpAssocRemAddrRtx_Type()
)
sctpAssocRemAddrRtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRemAddrRtx.setStatus("current")
_SctpAssocRemAddrStartTime_Type = TimeStamp
_SctpAssocRemAddrStartTime_Object = MibTableColumn
sctpAssocRemAddrStartTime = _SctpAssocRemAddrStartTime_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 5, 1, 8),
    _SctpAssocRemAddrStartTime_Type()
)
sctpAssocRemAddrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpAssocRemAddrStartTime.setStatus("current")
_SctpLookupLocalPortTable_Object = MibTable
sctpLookupLocalPortTable = _SctpLookupLocalPortTable_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 6)
)
if mibBuilder.loadTexts:
    sctpLookupLocalPortTable.setStatus("current")
_SctpLookupLocalPortEntry_Object = MibTableRow
sctpLookupLocalPortEntry = _SctpLookupLocalPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 6, 1)
)
sctpLookupLocalPortEntry.setIndexNames(
    (0, "SCTP-MIB", "sctpAssocLocalPort"),
    (0, "SCTP-MIB", "sctpAssocId"),
)
if mibBuilder.loadTexts:
    sctpLookupLocalPortEntry.setStatus("current")
_SctpLookupLocalPortStartTime_Type = TimeStamp
_SctpLookupLocalPortStartTime_Object = MibTableColumn
sctpLookupLocalPortStartTime = _SctpLookupLocalPortStartTime_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 6, 1, 1),
    _SctpLookupLocalPortStartTime_Type()
)
sctpLookupLocalPortStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpLookupLocalPortStartTime.setStatus("current")
_SctpLookupRemPortTable_Object = MibTable
sctpLookupRemPortTable = _SctpLookupRemPortTable_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 7)
)
if mibBuilder.loadTexts:
    sctpLookupRemPortTable.setStatus("current")
_SctpLookupRemPortEntry_Object = MibTableRow
sctpLookupRemPortEntry = _SctpLookupRemPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 7, 1)
)
sctpLookupRemPortEntry.setIndexNames(
    (0, "SCTP-MIB", "sctpAssocRemPort"),
    (0, "SCTP-MIB", "sctpAssocId"),
)
if mibBuilder.loadTexts:
    sctpLookupRemPortEntry.setStatus("current")
_SctpLookupRemPortStartTime_Type = TimeStamp
_SctpLookupRemPortStartTime_Object = MibTableColumn
sctpLookupRemPortStartTime = _SctpLookupRemPortStartTime_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 7, 1, 1),
    _SctpLookupRemPortStartTime_Type()
)
sctpLookupRemPortStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpLookupRemPortStartTime.setStatus("current")
_SctpLookupRemHostNameTable_Object = MibTable
sctpLookupRemHostNameTable = _SctpLookupRemHostNameTable_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 8)
)
if mibBuilder.loadTexts:
    sctpLookupRemHostNameTable.setStatus("current")
_SctpLookupRemHostNameEntry_Object = MibTableRow
sctpLookupRemHostNameEntry = _SctpLookupRemHostNameEntry_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 8, 1)
)
sctpLookupRemHostNameEntry.setIndexNames(
    (0, "SCTP-MIB", "sctpAssocRemHostName"),
    (0, "SCTP-MIB", "sctpAssocId"),
)
if mibBuilder.loadTexts:
    sctpLookupRemHostNameEntry.setStatus("current")
_SctpLookupRemHostNameStartTime_Type = TimeStamp
_SctpLookupRemHostNameStartTime_Object = MibTableColumn
sctpLookupRemHostNameStartTime = _SctpLookupRemHostNameStartTime_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 8, 1, 1),
    _SctpLookupRemHostNameStartTime_Type()
)
sctpLookupRemHostNameStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpLookupRemHostNameStartTime.setStatus("current")
_SctpLookupRemPrimIPAddrTable_Object = MibTable
sctpLookupRemPrimIPAddrTable = _SctpLookupRemPrimIPAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 9)
)
if mibBuilder.loadTexts:
    sctpLookupRemPrimIPAddrTable.setStatus("current")
_SctpLookupRemPrimIPAddrEntry_Object = MibTableRow
sctpLookupRemPrimIPAddrEntry = _SctpLookupRemPrimIPAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 9, 1)
)
sctpLookupRemPrimIPAddrEntry.setIndexNames(
    (0, "SCTP-MIB", "sctpAssocRemPrimAddrType"),
    (0, "SCTP-MIB", "sctpAssocRemPrimAddr"),
    (0, "SCTP-MIB", "sctpAssocId"),
)
if mibBuilder.loadTexts:
    sctpLookupRemPrimIPAddrEntry.setStatus("current")
_SctpLookupRemPrimIPAddrStartTime_Type = TimeStamp
_SctpLookupRemPrimIPAddrStartTime_Object = MibTableColumn
sctpLookupRemPrimIPAddrStartTime = _SctpLookupRemPrimIPAddrStartTime_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 9, 1, 1),
    _SctpLookupRemPrimIPAddrStartTime_Type()
)
sctpLookupRemPrimIPAddrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpLookupRemPrimIPAddrStartTime.setStatus("current")
_SctpLookupRemIPAddrTable_Object = MibTable
sctpLookupRemIPAddrTable = _SctpLookupRemIPAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 10)
)
if mibBuilder.loadTexts:
    sctpLookupRemIPAddrTable.setStatus("current")
_SctpLookupRemIPAddrEntry_Object = MibTableRow
sctpLookupRemIPAddrEntry = _SctpLookupRemIPAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 10, 1)
)
sctpLookupRemIPAddrEntry.setIndexNames(
    (0, "SCTP-MIB", "sctpAssocRemAddrType"),
    (0, "SCTP-MIB", "sctpAssocRemAddr"),
    (0, "SCTP-MIB", "sctpAssocId"),
)
if mibBuilder.loadTexts:
    sctpLookupRemIPAddrEntry.setStatus("current")
_SctpLookupRemIPAddrStartTime_Type = TimeStamp
_SctpLookupRemIPAddrStartTime_Object = MibTableColumn
sctpLookupRemIPAddrStartTime = _SctpLookupRemIPAddrStartTime_Object(
    (1, 3, 6, 1, 2, 1, 104, 1, 10, 1, 1),
    _SctpLookupRemIPAddrStartTime_Type()
)
sctpLookupRemIPAddrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctpLookupRemIPAddrStartTime.setStatus("current")
_SctpMibConformance_ObjectIdentity = ObjectIdentity
sctpMibConformance = _SctpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 104, 2)
)
_SctpMibCompliances_ObjectIdentity = ObjectIdentity
sctpMibCompliances = _SctpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 104, 2, 1)
)
_SctpMibGroups_ObjectIdentity = ObjectIdentity
sctpMibGroups = _SctpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 104, 2, 2)
)

# Managed Objects groups

sctpLayerParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 104, 2, 2, 1)
)
sctpLayerParamsGroup.setObjects(
      *(("SCTP-MIB", "sctpRtoAlgorithm"),
        ("SCTP-MIB", "sctpRtoMin"),
        ("SCTP-MIB", "sctpRtoMax"),
        ("SCTP-MIB", "sctpRtoInitial"),
        ("SCTP-MIB", "sctpMaxAssocs"),
        ("SCTP-MIB", "sctpValCookieLife"),
        ("SCTP-MIB", "sctpMaxInitRetr"))
)
if mibBuilder.loadTexts:
    sctpLayerParamsGroup.setStatus("current")

sctpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 104, 2, 2, 2)
)
sctpStatsGroup.setObjects(
      *(("SCTP-MIB", "sctpCurrEstab"),
        ("SCTP-MIB", "sctpActiveEstabs"),
        ("SCTP-MIB", "sctpPassiveEstabs"),
        ("SCTP-MIB", "sctpAborteds"),
        ("SCTP-MIB", "sctpShutdowns"),
        ("SCTP-MIB", "sctpOutOfBlues"),
        ("SCTP-MIB", "sctpChecksumErrors"),
        ("SCTP-MIB", "sctpOutCtrlChunks"),
        ("SCTP-MIB", "sctpOutOrderChunks"),
        ("SCTP-MIB", "sctpOutUnorderChunks"),
        ("SCTP-MIB", "sctpInCtrlChunks"),
        ("SCTP-MIB", "sctpInOrderChunks"),
        ("SCTP-MIB", "sctpInUnorderChunks"),
        ("SCTP-MIB", "sctpFragUsrMsgs"),
        ("SCTP-MIB", "sctpReasmUsrMsgs"),
        ("SCTP-MIB", "sctpOutSCTPPacks"),
        ("SCTP-MIB", "sctpInSCTPPacks"),
        ("SCTP-MIB", "sctpDiscontinuityTime"),
        ("SCTP-MIB", "sctpAssocT1expireds"),
        ("SCTP-MIB", "sctpAssocT2expireds"),
        ("SCTP-MIB", "sctpAssocRtxChunks"),
        ("SCTP-MIB", "sctpAssocRemAddrRtx"))
)
if mibBuilder.loadTexts:
    sctpStatsGroup.setStatus("current")

sctpPerAssocParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 104, 2, 2, 3)
)
sctpPerAssocParamsGroup.setObjects(
      *(("SCTP-MIB", "sctpAssocRemHostName"),
        ("SCTP-MIB", "sctpAssocLocalPort"),
        ("SCTP-MIB", "sctpAssocRemPort"),
        ("SCTP-MIB", "sctpAssocRemPrimAddrType"),
        ("SCTP-MIB", "sctpAssocRemPrimAddr"),
        ("SCTP-MIB", "sctpAssocHeartBeatInterval"),
        ("SCTP-MIB", "sctpAssocState"),
        ("SCTP-MIB", "sctpAssocInStreams"),
        ("SCTP-MIB", "sctpAssocOutStreams"),
        ("SCTP-MIB", "sctpAssocMaxRetr"),
        ("SCTP-MIB", "sctpAssocPrimProcess"),
        ("SCTP-MIB", "sctpAssocStartTime"),
        ("SCTP-MIB", "sctpAssocDiscontinuityTime"),
        ("SCTP-MIB", "sctpAssocLocalAddrStartTime"),
        ("SCTP-MIB", "sctpAssocRemAddrActive"),
        ("SCTP-MIB", "sctpAssocRemAddrHBActive"),
        ("SCTP-MIB", "sctpAssocRemAddrRTO"),
        ("SCTP-MIB", "sctpAssocRemAddrMaxPathRtx"),
        ("SCTP-MIB", "sctpAssocRemAddrStartTime"))
)
if mibBuilder.loadTexts:
    sctpPerAssocParamsGroup.setStatus("current")

sctpPerAssocStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 104, 2, 2, 4)
)
sctpPerAssocStatsGroup.setObjects(
      *(("SCTP-MIB", "sctpAssocT1expireds"),
        ("SCTP-MIB", "sctpAssocT2expireds"),
        ("SCTP-MIB", "sctpAssocRtxChunks"),
        ("SCTP-MIB", "sctpAssocRemAddrRtx"))
)
if mibBuilder.loadTexts:
    sctpPerAssocStatsGroup.setStatus("current")

sctpInverseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 104, 2, 2, 5)
)
sctpInverseGroup.setObjects(
      *(("SCTP-MIB", "sctpLookupLocalPortStartTime"),
        ("SCTP-MIB", "sctpLookupRemPortStartTime"),
        ("SCTP-MIB", "sctpLookupRemHostNameStartTime"),
        ("SCTP-MIB", "sctpLookupRemPrimIPAddrStartTime"),
        ("SCTP-MIB", "sctpLookupRemIPAddrStartTime"))
)
if mibBuilder.loadTexts:
    sctpInverseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sctpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 104, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sctpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTP-MIB",
    **{"sctpMIB": sctpMIB,
       "sctpObjects": sctpObjects,
       "sctpStats": sctpStats,
       "sctpCurrEstab": sctpCurrEstab,
       "sctpActiveEstabs": sctpActiveEstabs,
       "sctpPassiveEstabs": sctpPassiveEstabs,
       "sctpAborteds": sctpAborteds,
       "sctpShutdowns": sctpShutdowns,
       "sctpOutOfBlues": sctpOutOfBlues,
       "sctpChecksumErrors": sctpChecksumErrors,
       "sctpOutCtrlChunks": sctpOutCtrlChunks,
       "sctpOutOrderChunks": sctpOutOrderChunks,
       "sctpOutUnorderChunks": sctpOutUnorderChunks,
       "sctpInCtrlChunks": sctpInCtrlChunks,
       "sctpInOrderChunks": sctpInOrderChunks,
       "sctpInUnorderChunks": sctpInUnorderChunks,
       "sctpFragUsrMsgs": sctpFragUsrMsgs,
       "sctpReasmUsrMsgs": sctpReasmUsrMsgs,
       "sctpOutSCTPPacks": sctpOutSCTPPacks,
       "sctpInSCTPPacks": sctpInSCTPPacks,
       "sctpDiscontinuityTime": sctpDiscontinuityTime,
       "sctpParams": sctpParams,
       "sctpRtoAlgorithm": sctpRtoAlgorithm,
       "sctpRtoMin": sctpRtoMin,
       "sctpRtoMax": sctpRtoMax,
       "sctpRtoInitial": sctpRtoInitial,
       "sctpMaxAssocs": sctpMaxAssocs,
       "sctpValCookieLife": sctpValCookieLife,
       "sctpMaxInitRetr": sctpMaxInitRetr,
       "sctpAssocTable": sctpAssocTable,
       "sctpAssocEntry": sctpAssocEntry,
       "sctpAssocId": sctpAssocId,
       "sctpAssocRemHostName": sctpAssocRemHostName,
       "sctpAssocLocalPort": sctpAssocLocalPort,
       "sctpAssocRemPort": sctpAssocRemPort,
       "sctpAssocRemPrimAddrType": sctpAssocRemPrimAddrType,
       "sctpAssocRemPrimAddr": sctpAssocRemPrimAddr,
       "sctpAssocHeartBeatInterval": sctpAssocHeartBeatInterval,
       "sctpAssocState": sctpAssocState,
       "sctpAssocInStreams": sctpAssocInStreams,
       "sctpAssocOutStreams": sctpAssocOutStreams,
       "sctpAssocMaxRetr": sctpAssocMaxRetr,
       "sctpAssocPrimProcess": sctpAssocPrimProcess,
       "sctpAssocT1expireds": sctpAssocT1expireds,
       "sctpAssocT2expireds": sctpAssocT2expireds,
       "sctpAssocRtxChunks": sctpAssocRtxChunks,
       "sctpAssocStartTime": sctpAssocStartTime,
       "sctpAssocDiscontinuityTime": sctpAssocDiscontinuityTime,
       "sctpAssocLocalAddrTable": sctpAssocLocalAddrTable,
       "sctpAssocLocalAddrEntry": sctpAssocLocalAddrEntry,
       "sctpAssocLocalAddrType": sctpAssocLocalAddrType,
       "sctpAssocLocalAddr": sctpAssocLocalAddr,
       "sctpAssocLocalAddrStartTime": sctpAssocLocalAddrStartTime,
       "sctpAssocRemAddrTable": sctpAssocRemAddrTable,
       "sctpAssocRemAddrEntry": sctpAssocRemAddrEntry,
       "sctpAssocRemAddrType": sctpAssocRemAddrType,
       "sctpAssocRemAddr": sctpAssocRemAddr,
       "sctpAssocRemAddrActive": sctpAssocRemAddrActive,
       "sctpAssocRemAddrHBActive": sctpAssocRemAddrHBActive,
       "sctpAssocRemAddrRTO": sctpAssocRemAddrRTO,
       "sctpAssocRemAddrMaxPathRtx": sctpAssocRemAddrMaxPathRtx,
       "sctpAssocRemAddrRtx": sctpAssocRemAddrRtx,
       "sctpAssocRemAddrStartTime": sctpAssocRemAddrStartTime,
       "sctpLookupLocalPortTable": sctpLookupLocalPortTable,
       "sctpLookupLocalPortEntry": sctpLookupLocalPortEntry,
       "sctpLookupLocalPortStartTime": sctpLookupLocalPortStartTime,
       "sctpLookupRemPortTable": sctpLookupRemPortTable,
       "sctpLookupRemPortEntry": sctpLookupRemPortEntry,
       "sctpLookupRemPortStartTime": sctpLookupRemPortStartTime,
       "sctpLookupRemHostNameTable": sctpLookupRemHostNameTable,
       "sctpLookupRemHostNameEntry": sctpLookupRemHostNameEntry,
       "sctpLookupRemHostNameStartTime": sctpLookupRemHostNameStartTime,
       "sctpLookupRemPrimIPAddrTable": sctpLookupRemPrimIPAddrTable,
       "sctpLookupRemPrimIPAddrEntry": sctpLookupRemPrimIPAddrEntry,
       "sctpLookupRemPrimIPAddrStartTime": sctpLookupRemPrimIPAddrStartTime,
       "sctpLookupRemIPAddrTable": sctpLookupRemIPAddrTable,
       "sctpLookupRemIPAddrEntry": sctpLookupRemIPAddrEntry,
       "sctpLookupRemIPAddrStartTime": sctpLookupRemIPAddrStartTime,
       "sctpMibConformance": sctpMibConformance,
       "sctpMibCompliances": sctpMibCompliances,
       "sctpMibCompliance": sctpMibCompliance,
       "sctpMibGroups": sctpMibGroups,
       "sctpLayerParamsGroup": sctpLayerParamsGroup,
       "sctpStatsGroup": sctpStatsGroup,
       "sctpPerAssocParamsGroup": sctpPerAssocParamsGroup,
       "sctpPerAssocStatsGroup": sctpPerAssocStatsGroup,
       "sctpInverseGroup": sctpInverseGroup}
)
