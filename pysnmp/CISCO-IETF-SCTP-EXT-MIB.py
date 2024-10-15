# SNMP MIB module (CISCO-IETF-SCTP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-SCTP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:02 2024
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

(cSctpAssocEntry,
 cSctpAssocRemAddressEntry,
 cSctpAssocRemAddressStatus) = mibBuilder.importSymbols(
    "CISCO-IETF-SCTP-MIB",
    "cSctpAssocEntry",
    "cSctpAssocRemAddressEntry",
    "cSctpAssocRemAddressStatus")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cSctpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 76)
)
cSctpExtMIB.setRevisions(
        ("2001-11-09 00:00",
         "2001-08-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CSctpExtNotifications_ObjectIdentity = ObjectIdentity
cSctpExtNotifications = _CSctpExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 0)
)
_CSctpExtObjects_ObjectIdentity = ObjectIdentity
cSctpExtObjects = _CSctpExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1)
)
_CSctpScalarsExt_ObjectIdentity = ObjectIdentity
cSctpScalarsExt = _CSctpScalarsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1)
)
_CSctpStatRtxChucks_Type = Counter32
_CSctpStatRtxChucks_Object = MibScalar
cSctpStatRtxChucks = _CSctpStatRtxChucks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 1),
    _CSctpStatRtxChucks_Type()
)
cSctpStatRtxChucks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatRtxChucks.setStatus("current")
if mibBuilder.loadTexts:
    cSctpStatRtxChucks.setUnits("chunks")
_CSctpStatRtxChucksFast_Type = Counter32
_CSctpStatRtxChucksFast_Object = MibScalar
cSctpStatRtxChucksFast = _CSctpStatRtxChucksFast_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 2),
    _CSctpStatRtxChucksFast_Type()
)
cSctpStatRtxChucksFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatRtxChucksFast.setStatus("current")
if mibBuilder.loadTexts:
    cSctpStatRtxChucksFast.setUnits("chunks")
_CSctpStatDestAddressFailures_Type = Counter32
_CSctpStatDestAddressFailures_Object = MibScalar
cSctpStatDestAddressFailures = _CSctpStatDestAddressFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 3),
    _CSctpStatDestAddressFailures_Type()
)
cSctpStatDestAddressFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatDestAddressFailures.setStatus("current")


class _CSctpCtrlPurgeTimeout_Type(Unsigned32):
    """Custom type cSctpCtrlPurgeTimeout based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 3000000),
    )


_CSctpCtrlPurgeTimeout_Type.__name__ = "Unsigned32"
_CSctpCtrlPurgeTimeout_Object = MibScalar
cSctpCtrlPurgeTimeout = _CSctpCtrlPurgeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 4),
    _CSctpCtrlPurgeTimeout_Type()
)
cSctpCtrlPurgeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSctpCtrlPurgeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cSctpCtrlPurgeTimeout.setUnits("seconds")


class _CSctpCtrlMaxHeld_Type(Unsigned32):
    """Custom type cSctpCtrlMaxHeld based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 10000),
    )


_CSctpCtrlMaxHeld_Type.__name__ = "Unsigned32"
_CSctpCtrlMaxHeld_Object = MibScalar
cSctpCtrlMaxHeld = _CSctpCtrlMaxHeld_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 5),
    _CSctpCtrlMaxHeld_Type()
)
cSctpCtrlMaxHeld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSctpCtrlMaxHeld.setStatus("current")
if mibBuilder.loadTexts:
    cSctpCtrlMaxHeld.setUnits("association TCBs")


class _CSctpAddressStateNotifEnabled_Type(TruthValue):
    """Custom type cSctpAddressStateNotifEnabled based on TruthValue"""


_CSctpAddressStateNotifEnabled_Object = MibScalar
cSctpAddressStateNotifEnabled = _CSctpAddressStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 1, 6),
    _CSctpAddressStateNotifEnabled_Type()
)
cSctpAddressStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSctpAddressStateNotifEnabled.setStatus("current")
_CSctpExtTables_ObjectIdentity = ObjectIdentity
cSctpExtTables = _CSctpExtTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2)
)
_CSctpAssocExtTable_Object = MibTable
cSctpAssocExtTable = _CSctpAssocExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cSctpAssocExtTable.setStatus("current")
_CSctpAssocExtEntry_Object = MibTableRow
cSctpAssocExtEntry = _CSctpAssocExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cSctpAssocExtEntry.setStatus("current")
_CSctpAssocExtRtoMin_Type = Unsigned32
_CSctpAssocExtRtoMin_Object = MibTableColumn
cSctpAssocExtRtoMin = _CSctpAssocExtRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 1),
    _CSctpAssocExtRtoMin_Type()
)
cSctpAssocExtRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtRtoMin.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtRtoMin.setUnits("milliseconds")
_CSctpAssocExtRtoMax_Type = Unsigned32
_CSctpAssocExtRtoMax_Object = MibTableColumn
cSctpAssocExtRtoMax = _CSctpAssocExtRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 2),
    _CSctpAssocExtRtoMax_Type()
)
cSctpAssocExtRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtRtoMax.setUnits("milliseconds")
_CSctpAssocExtRtoInitial_Type = Unsigned32
_CSctpAssocExtRtoInitial_Object = MibTableColumn
cSctpAssocExtRtoInitial = _CSctpAssocExtRtoInitial_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 3),
    _CSctpAssocExtRtoInitial_Type()
)
cSctpAssocExtRtoInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtRtoInitial.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtRtoInitial.setUnits("milliseconds")
_CSctpAssocExtValCookieLife_Type = Unsigned32
_CSctpAssocExtValCookieLife_Object = MibTableColumn
cSctpAssocExtValCookieLife = _CSctpAssocExtValCookieLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 4),
    _CSctpAssocExtValCookieLife_Type()
)
cSctpAssocExtValCookieLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtValCookieLife.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtValCookieLife.setUnits("milliseconds")
_CSctpAssocExtMaxInitRetr_Type = Unsigned32
_CSctpAssocExtMaxInitRetr_Object = MibTableColumn
cSctpAssocExtMaxInitRetr = _CSctpAssocExtMaxInitRetr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 5),
    _CSctpAssocExtMaxInitRetr_Type()
)
cSctpAssocExtMaxInitRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtMaxInitRetr.setStatus("current")


class _CSctpAssocExtMTU_Type(Unsigned32):
    """Custom type cSctpAssocExtMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(37, 65535),
    )


_CSctpAssocExtMTU_Type.__name__ = "Unsigned32"
_CSctpAssocExtMTU_Object = MibTableColumn
cSctpAssocExtMTU = _CSctpAssocExtMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 6),
    _CSctpAssocExtMTU_Type()
)
cSctpAssocExtMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtMTU.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtMTU.setUnits("bytes")


class _CSctpAssocExtLocRecWnd_Type(Unsigned32):
    """Custom type cSctpAssocExtLocRecWnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CSctpAssocExtLocRecWnd_Type.__name__ = "Unsigned32"
_CSctpAssocExtLocRecWnd_Object = MibTableColumn
cSctpAssocExtLocRecWnd = _CSctpAssocExtLocRecWnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 7),
    _CSctpAssocExtLocRecWnd_Type()
)
cSctpAssocExtLocRecWnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtLocRecWnd.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtLocRecWnd.setUnits("bytes")


class _CSctpAssocExtLocRecWndLowMark_Type(Gauge32):
    """Custom type cSctpAssocExtLocRecWndLowMark based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CSctpAssocExtLocRecWndLowMark_Type.__name__ = "Gauge32"
_CSctpAssocExtLocRecWndLowMark_Object = MibTableColumn
cSctpAssocExtLocRecWndLowMark = _CSctpAssocExtLocRecWndLowMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 8),
    _CSctpAssocExtLocRecWndLowMark_Type()
)
cSctpAssocExtLocRecWndLowMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtLocRecWndLowMark.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtLocRecWndLowMark.setUnits("bytes")
_CSctpAssocExtLocRecWndZeroCnt_Type = Counter32
_CSctpAssocExtLocRecWndZeroCnt_Object = MibTableColumn
cSctpAssocExtLocRecWndZeroCnt = _CSctpAssocExtLocRecWndZeroCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 9),
    _CSctpAssocExtLocRecWndZeroCnt_Type()
)
cSctpAssocExtLocRecWndZeroCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtLocRecWndZeroCnt.setStatus("current")


class _CSctpAssocExtRemRecWnd_Type(Unsigned32):
    """Custom type cSctpAssocExtRemRecWnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CSctpAssocExtRemRecWnd_Type.__name__ = "Unsigned32"
_CSctpAssocExtRemRecWnd_Object = MibTableColumn
cSctpAssocExtRemRecWnd = _CSctpAssocExtRemRecWnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 10),
    _CSctpAssocExtRemRecWnd_Type()
)
cSctpAssocExtRemRecWnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtRemRecWnd.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtRemRecWnd.setUnits("bytes")


class _CSctpAssocExtRemRecWndLowMark_Type(Gauge32):
    """Custom type cSctpAssocExtRemRecWndLowMark based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CSctpAssocExtRemRecWndLowMark_Type.__name__ = "Gauge32"
_CSctpAssocExtRemRecWndLowMark_Object = MibTableColumn
cSctpAssocExtRemRecWndLowMark = _CSctpAssocExtRemRecWndLowMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 11),
    _CSctpAssocExtRemRecWndLowMark_Type()
)
cSctpAssocExtRemRecWndLowMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtRemRecWndLowMark.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtRemRecWndLowMark.setUnits("bytes")
_CSctpAssocExtRemRecWndZeroCnt_Type = Counter32
_CSctpAssocExtRemRecWndZeroCnt_Object = MibTableColumn
cSctpAssocExtRemRecWndZeroCnt = _CSctpAssocExtRemRecWndZeroCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 12),
    _CSctpAssocExtRemRecWndZeroCnt_Type()
)
cSctpAssocExtRemRecWndZeroCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtRemRecWndZeroCnt.setStatus("current")


class _CSctpAssocExtUlpQueued_Type(Gauge32):
    """Custom type cSctpAssocExtUlpQueued based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CSctpAssocExtUlpQueued_Type.__name__ = "Gauge32"
_CSctpAssocExtUlpQueued_Object = MibTableColumn
cSctpAssocExtUlpQueued = _CSctpAssocExtUlpQueued_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 13),
    _CSctpAssocExtUlpQueued_Type()
)
cSctpAssocExtUlpQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtUlpQueued.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtUlpQueued.setUnits("datagrams")


class _CSctpAssocExtUlpQueuedHW_Type(Gauge32):
    """Custom type cSctpAssocExtUlpQueuedHW based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CSctpAssocExtUlpQueuedHW_Type.__name__ = "Gauge32"
_CSctpAssocExtUlpQueuedHW_Object = MibTableColumn
cSctpAssocExtUlpQueuedHW = _CSctpAssocExtUlpQueuedHW_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 14),
    _CSctpAssocExtUlpQueuedHW_Type()
)
cSctpAssocExtUlpQueuedHW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSctpAssocExtUlpQueuedHW.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtUlpQueuedHW.setUnits("datagrams")
_CSctpAssocExtUlpQueuedRT_Type = TimeStamp
_CSctpAssocExtUlpQueuedRT_Object = MibTableColumn
cSctpAssocExtUlpQueuedRT = _CSctpAssocExtUlpQueuedRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 15),
    _CSctpAssocExtUlpQueuedRT_Type()
)
cSctpAssocExtUlpQueuedRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtUlpQueuedRT.setStatus("current")
_CSctpAssocExtChunksRecControl_Type = Counter32
_CSctpAssocExtChunksRecControl_Object = MibTableColumn
cSctpAssocExtChunksRecControl = _CSctpAssocExtChunksRecControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 16),
    _CSctpAssocExtChunksRecControl_Type()
)
cSctpAssocExtChunksRecControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksRecControl.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksRecControl.setUnits("chunks")
_CSctpAssocExtChunksRecOrdered_Type = Counter32
_CSctpAssocExtChunksRecOrdered_Object = MibTableColumn
cSctpAssocExtChunksRecOrdered = _CSctpAssocExtChunksRecOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 17),
    _CSctpAssocExtChunksRecOrdered_Type()
)
cSctpAssocExtChunksRecOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksRecOrdered.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksRecOrdered.setUnits("chunks")
_CSctpAssocExtChunksRecUnOrdered_Type = Counter32
_CSctpAssocExtChunksRecUnOrdered_Object = MibTableColumn
cSctpAssocExtChunksRecUnOrdered = _CSctpAssocExtChunksRecUnOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 18),
    _CSctpAssocExtChunksRecUnOrdered_Type()
)
cSctpAssocExtChunksRecUnOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksRecUnOrdered.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksRecUnOrdered.setUnits("chunks")
_CSctpAssocExtChunksSentControl_Type = Counter32
_CSctpAssocExtChunksSentControl_Object = MibTableColumn
cSctpAssocExtChunksSentControl = _CSctpAssocExtChunksSentControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 19),
    _CSctpAssocExtChunksSentControl_Type()
)
cSctpAssocExtChunksSentControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksSentControl.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksSentControl.setUnits("chunks")
_CSctpAssocExtChunksSentOrdered_Type = Counter32
_CSctpAssocExtChunksSentOrdered_Object = MibTableColumn
cSctpAssocExtChunksSentOrdered = _CSctpAssocExtChunksSentOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 20),
    _CSctpAssocExtChunksSentOrdered_Type()
)
cSctpAssocExtChunksSentOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksSentOrdered.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksSentOrdered.setUnits("chunks")
_CSctpAssocExtChunksSentUnOrdered_Type = Counter32
_CSctpAssocExtChunksSentUnOrdered_Object = MibTableColumn
cSctpAssocExtChunksSentUnOrdered = _CSctpAssocExtChunksSentUnOrdered_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 21),
    _CSctpAssocExtChunksSentUnOrdered_Type()
)
cSctpAssocExtChunksSentUnOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksSentUnOrdered.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtChunksSentUnOrdered.setUnits("chunks")
_CSctpAssocExtDatagramsRec_Type = Counter32
_CSctpAssocExtDatagramsRec_Object = MibTableColumn
cSctpAssocExtDatagramsRec = _CSctpAssocExtDatagramsRec_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 22),
    _CSctpAssocExtDatagramsRec_Type()
)
cSctpAssocExtDatagramsRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtDatagramsRec.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtDatagramsRec.setUnits("datagrams")
_CSctpAssocExtDatagramsSent_Type = Counter32
_CSctpAssocExtDatagramsSent_Object = MibTableColumn
cSctpAssocExtDatagramsSent = _CSctpAssocExtDatagramsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 23),
    _CSctpAssocExtDatagramsSent_Type()
)
cSctpAssocExtDatagramsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtDatagramsSent.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtDatagramsSent.setUnits("datagrams")
_CSctpAssocExtEffectiveAddrType_Type = InetAddressType
_CSctpAssocExtEffectiveAddrType_Object = MibTableColumn
cSctpAssocExtEffectiveAddrType = _CSctpAssocExtEffectiveAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 24),
    _CSctpAssocExtEffectiveAddrType_Type()
)
cSctpAssocExtEffectiveAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtEffectiveAddrType.setStatus("current")
_CSctpAssocExtEffectiveAddress_Type = InetAddress
_CSctpAssocExtEffectiveAddress_Object = MibTableColumn
cSctpAssocExtEffectiveAddress = _CSctpAssocExtEffectiveAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 25),
    _CSctpAssocExtEffectiveAddress_Type()
)
cSctpAssocExtEffectiveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtEffectiveAddress.setStatus("current")
_CSctpAssocExtRtxChunksFast_Type = Counter32
_CSctpAssocExtRtxChunksFast_Object = MibTableColumn
cSctpAssocExtRtxChunksFast = _CSctpAssocExtRtxChunksFast_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 26),
    _CSctpAssocExtRtxChunksFast_Type()
)
cSctpAssocExtRtxChunksFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtRtxChunksFast.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtRtxChunksFast.setUnits("chunks")
_CSctpAssocExtBundleFlag_Type = TruthValue
_CSctpAssocExtBundleFlag_Object = MibTableColumn
cSctpAssocExtBundleFlag = _CSctpAssocExtBundleFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 27),
    _CSctpAssocExtBundleFlag_Type()
)
cSctpAssocExtBundleFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtBundleFlag.setStatus("current")


class _CSctpAssocExtBundleTimeout_Type(Unsigned32):
    """Custom type cSctpAssocExtBundleTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_CSctpAssocExtBundleTimeout_Type.__name__ = "Unsigned32"
_CSctpAssocExtBundleTimeout_Object = MibTableColumn
cSctpAssocExtBundleTimeout = _CSctpAssocExtBundleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 1, 1, 28),
    _CSctpAssocExtBundleTimeout_Type()
)
cSctpAssocExtBundleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocExtBundleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocExtBundleTimeout.setUnits("milliseconds")
_CSctpAssocRemAddressExtTable_Object = MibTable
cSctpAssocRemAddressExtTable = _CSctpAssocRemAddressExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cSctpAssocRemAddressExtTable.setStatus("current")
_CSctpAssocRemAddressExtEntry_Object = MibTableRow
cSctpAssocRemAddressExtEntry = _CSctpAssocRemAddressExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cSctpAssocRemAddressExtEntry.setStatus("current")
_CSctpAssocRemAddressFailedCnt_Type = Counter32
_CSctpAssocRemAddressFailedCnt_Object = MibTableColumn
cSctpAssocRemAddressFailedCnt = _CSctpAssocRemAddressFailedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 2, 1, 1),
    _CSctpAssocRemAddressFailedCnt_Type()
)
cSctpAssocRemAddressFailedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressFailedCnt.setStatus("current")


class _CSctpAssocRemAddressSRTT_Type(Unsigned32):
    """Custom type cSctpAssocRemAddressSRTT based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CSctpAssocRemAddressSRTT_Type.__name__ = "Unsigned32"
_CSctpAssocRemAddressSRTT_Object = MibTableColumn
cSctpAssocRemAddressSRTT = _CSctpAssocRemAddressSRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 1, 2, 2, 1, 2),
    _CSctpAssocRemAddressSRTT_Type()
)
cSctpAssocRemAddressSRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressSRTT.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressSRTT.setUnits("milliseconds")
_CSctpExtConformance_ObjectIdentity = ObjectIdentity
cSctpExtConformance = _CSctpExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3)
)
_CSctpExtCompliances_ObjectIdentity = ObjectIdentity
cSctpExtCompliances = _CSctpExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 1)
)
_CSctpExtGroups_ObjectIdentity = ObjectIdentity
cSctpExtGroups = _CSctpExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2)
)
cSctpAssocEntry.registerAugmentions(
    ("CISCO-IETF-SCTP-EXT-MIB",
     "cSctpAssocExtEntry")
)
cSctpAssocExtEntry.setIndexNames(*cSctpAssocEntry.getIndexNames())
cSctpAssocRemAddressEntry.registerAugmentions(
    ("CISCO-IETF-SCTP-EXT-MIB",
     "cSctpAssocRemAddressExtEntry")
)
cSctpAssocRemAddressExtEntry.setIndexNames(*cSctpAssocRemAddressEntry.getIndexNames())

# Managed Objects groups

cSctpExtStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 1)
)
cSctpExtStatGroup.setObjects(
      *(("CISCO-IETF-SCTP-EXT-MIB", "cSctpStatRtxChucks"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpStatRtxChucksFast"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpStatDestAddressFailures"))
)
if mibBuilder.loadTexts:
    cSctpExtStatGroup.setStatus("current")

cSctpExtCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 2)
)
cSctpExtCtrlGroup.setObjects(
      *(("CISCO-IETF-SCTP-EXT-MIB", "cSctpCtrlPurgeTimeout"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpCtrlMaxHeld"))
)
if mibBuilder.loadTexts:
    cSctpExtCtrlGroup.setStatus("deprecated")

cSctpExtAssocCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 3)
)
cSctpExtAssocCtrlGroup.setObjects(
      *(("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRtoMin"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRtoMax"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRtoInitial"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtValCookieLife"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtMaxInitRetr"))
)
if mibBuilder.loadTexts:
    cSctpExtAssocCtrlGroup.setStatus("current")

cSctpExtAssocStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 4)
)
cSctpExtAssocStatGroup.setObjects(
      *(("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtMTU"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWnd"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWndLowMark"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWndZeroCnt"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWnd"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWndLowMark"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWndZeroCnt"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueued"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueuedHW"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueuedRT"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecControl"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecOrdered"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecUnOrdered"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentControl"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentOrdered"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentUnOrdered"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtDatagramsRec"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtDatagramsSent"))
)
if mibBuilder.loadTexts:
    cSctpExtAssocStatGroup.setStatus("deprecated")

cSctpExtAssocRemAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 5)
)
cSctpExtAssocRemAddrGroup.setObjects(
      *(("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocRemAddressFailedCnt"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocRemAddressSRTT"))
)
if mibBuilder.loadTexts:
    cSctpExtAssocRemAddrGroup.setStatus("current")

cSctpExtCtrlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 7)
)
cSctpExtCtrlGroupRev1.setObjects(
      *(("CISCO-IETF-SCTP-EXT-MIB", "cSctpCtrlPurgeTimeout"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpCtrlMaxHeld"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAddressStateNotifEnabled"))
)
if mibBuilder.loadTexts:
    cSctpExtCtrlGroupRev1.setStatus("current")

cSctpExtAssocStatGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 8)
)
cSctpExtAssocStatGroupRev1.setObjects(
      *(("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtMTU"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWnd"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWndLowMark"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtLocRecWndZeroCnt"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWnd"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWndLowMark"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRemRecWndZeroCnt"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueued"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueuedHW"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtUlpQueuedRT"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecControl"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecOrdered"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksRecUnOrdered"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentControl"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentOrdered"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtChunksSentUnOrdered"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtDatagramsRec"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtDatagramsSent"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtEffectiveAddrType"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtEffectiveAddress"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtRtxChunksFast"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtBundleTimeout"),
        ("CISCO-IETF-SCTP-EXT-MIB", "cSctpAssocExtBundleFlag"))
)
if mibBuilder.loadTexts:
    cSctpExtAssocStatGroupRev1.setStatus("current")


# Notification objects

cSctpExtDestAddressStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 0, 1)
)
cSctpExtDestAddressStateChange.setObjects(
    ("CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressStatus")
)
if mibBuilder.loadTexts:
    cSctpExtDestAddressStateChange.setStatus(
        "current"
    )


# Notifications groups

cSctpExtAssocNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 2, 6)
)
cSctpExtAssocNotificationsGroup.setObjects(
    ("CISCO-IETF-SCTP-EXT-MIB", "cSctpExtDestAddressStateChange")
)
if mibBuilder.loadTexts:
    cSctpExtAssocNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cSctpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cSctpExtCompliance.setStatus(
        "deprecated"
    )

cSctpExtComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 76, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cSctpExtComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-SCTP-EXT-MIB",
    **{"cSctpExtMIB": cSctpExtMIB,
       "cSctpExtNotifications": cSctpExtNotifications,
       "cSctpExtDestAddressStateChange": cSctpExtDestAddressStateChange,
       "cSctpExtObjects": cSctpExtObjects,
       "cSctpScalarsExt": cSctpScalarsExt,
       "cSctpStatRtxChucks": cSctpStatRtxChucks,
       "cSctpStatRtxChucksFast": cSctpStatRtxChucksFast,
       "cSctpStatDestAddressFailures": cSctpStatDestAddressFailures,
       "cSctpCtrlPurgeTimeout": cSctpCtrlPurgeTimeout,
       "cSctpCtrlMaxHeld": cSctpCtrlMaxHeld,
       "cSctpAddressStateNotifEnabled": cSctpAddressStateNotifEnabled,
       "cSctpExtTables": cSctpExtTables,
       "cSctpAssocExtTable": cSctpAssocExtTable,
       "cSctpAssocExtEntry": cSctpAssocExtEntry,
       "cSctpAssocExtRtoMin": cSctpAssocExtRtoMin,
       "cSctpAssocExtRtoMax": cSctpAssocExtRtoMax,
       "cSctpAssocExtRtoInitial": cSctpAssocExtRtoInitial,
       "cSctpAssocExtValCookieLife": cSctpAssocExtValCookieLife,
       "cSctpAssocExtMaxInitRetr": cSctpAssocExtMaxInitRetr,
       "cSctpAssocExtMTU": cSctpAssocExtMTU,
       "cSctpAssocExtLocRecWnd": cSctpAssocExtLocRecWnd,
       "cSctpAssocExtLocRecWndLowMark": cSctpAssocExtLocRecWndLowMark,
       "cSctpAssocExtLocRecWndZeroCnt": cSctpAssocExtLocRecWndZeroCnt,
       "cSctpAssocExtRemRecWnd": cSctpAssocExtRemRecWnd,
       "cSctpAssocExtRemRecWndLowMark": cSctpAssocExtRemRecWndLowMark,
       "cSctpAssocExtRemRecWndZeroCnt": cSctpAssocExtRemRecWndZeroCnt,
       "cSctpAssocExtUlpQueued": cSctpAssocExtUlpQueued,
       "cSctpAssocExtUlpQueuedHW": cSctpAssocExtUlpQueuedHW,
       "cSctpAssocExtUlpQueuedRT": cSctpAssocExtUlpQueuedRT,
       "cSctpAssocExtChunksRecControl": cSctpAssocExtChunksRecControl,
       "cSctpAssocExtChunksRecOrdered": cSctpAssocExtChunksRecOrdered,
       "cSctpAssocExtChunksRecUnOrdered": cSctpAssocExtChunksRecUnOrdered,
       "cSctpAssocExtChunksSentControl": cSctpAssocExtChunksSentControl,
       "cSctpAssocExtChunksSentOrdered": cSctpAssocExtChunksSentOrdered,
       "cSctpAssocExtChunksSentUnOrdered": cSctpAssocExtChunksSentUnOrdered,
       "cSctpAssocExtDatagramsRec": cSctpAssocExtDatagramsRec,
       "cSctpAssocExtDatagramsSent": cSctpAssocExtDatagramsSent,
       "cSctpAssocExtEffectiveAddrType": cSctpAssocExtEffectiveAddrType,
       "cSctpAssocExtEffectiveAddress": cSctpAssocExtEffectiveAddress,
       "cSctpAssocExtRtxChunksFast": cSctpAssocExtRtxChunksFast,
       "cSctpAssocExtBundleFlag": cSctpAssocExtBundleFlag,
       "cSctpAssocExtBundleTimeout": cSctpAssocExtBundleTimeout,
       "cSctpAssocRemAddressExtTable": cSctpAssocRemAddressExtTable,
       "cSctpAssocRemAddressExtEntry": cSctpAssocRemAddressExtEntry,
       "cSctpAssocRemAddressFailedCnt": cSctpAssocRemAddressFailedCnt,
       "cSctpAssocRemAddressSRTT": cSctpAssocRemAddressSRTT,
       "cSctpExtConformance": cSctpExtConformance,
       "cSctpExtCompliances": cSctpExtCompliances,
       "cSctpExtCompliance": cSctpExtCompliance,
       "cSctpExtComplianceRev1": cSctpExtComplianceRev1,
       "cSctpExtGroups": cSctpExtGroups,
       "cSctpExtStatGroup": cSctpExtStatGroup,
       "cSctpExtCtrlGroup": cSctpExtCtrlGroup,
       "cSctpExtAssocCtrlGroup": cSctpExtAssocCtrlGroup,
       "cSctpExtAssocStatGroup": cSctpExtAssocStatGroup,
       "cSctpExtAssocRemAddrGroup": cSctpExtAssocRemAddrGroup,
       "cSctpExtAssocNotificationsGroup": cSctpExtAssocNotificationsGroup,
       "cSctpExtCtrlGroupRev1": cSctpExtCtrlGroupRev1,
       "cSctpExtAssocStatGroupRev1": cSctpExtAssocStatGroupRev1}
)
