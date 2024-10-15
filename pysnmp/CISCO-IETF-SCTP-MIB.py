# SNMP MIB module (CISCO-IETF-SCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-SCTP-MIB
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

cSctpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 75)
)
cSctpMIB.setRevisions(
        ("2001-08-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InetPortNumber(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CSctpObjects_ObjectIdentity = ObjectIdentity
cSctpObjects = _CSctpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1)
)
_CSctpScalars_ObjectIdentity = ObjectIdentity
cSctpScalars = _CSctpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1)
)


class _CSctpRtoAlgorithm_Type(Integer32):
    """Custom type cSctpRtoAlgorithm based on Integer32"""
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


_CSctpRtoAlgorithm_Type.__name__ = "Integer32"
_CSctpRtoAlgorithm_Object = MibScalar
cSctpRtoAlgorithm = _CSctpRtoAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 1),
    _CSctpRtoAlgorithm_Type()
)
cSctpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpRtoAlgorithm.setStatus("current")
_CSctpRtoMin_Type = Unsigned32
_CSctpRtoMin_Object = MibScalar
cSctpRtoMin = _CSctpRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 2),
    _CSctpRtoMin_Type()
)
cSctpRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpRtoMin.setStatus("current")
if mibBuilder.loadTexts:
    cSctpRtoMin.setUnits("milliseconds")
_CSctpRtoMax_Type = Unsigned32
_CSctpRtoMax_Object = MibScalar
cSctpRtoMax = _CSctpRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 3),
    _CSctpRtoMax_Type()
)
cSctpRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    cSctpRtoMax.setUnits("milliseconds")
_CSctpRtoInitial_Type = Unsigned32
_CSctpRtoInitial_Object = MibScalar
cSctpRtoInitial = _CSctpRtoInitial_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 4),
    _CSctpRtoInitial_Type()
)
cSctpRtoInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpRtoInitial.setStatus("current")
if mibBuilder.loadTexts:
    cSctpRtoInitial.setUnits("milliseconds")
_CSctpMaxAssoc_Type = Unsigned32
_CSctpMaxAssoc_Object = MibScalar
cSctpMaxAssoc = _CSctpMaxAssoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 5),
    _CSctpMaxAssoc_Type()
)
cSctpMaxAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpMaxAssoc.setStatus("current")
_CSctpValCookieLife_Type = Unsigned32
_CSctpValCookieLife_Object = MibScalar
cSctpValCookieLife = _CSctpValCookieLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 6),
    _CSctpValCookieLife_Type()
)
cSctpValCookieLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpValCookieLife.setStatus("current")
if mibBuilder.loadTexts:
    cSctpValCookieLife.setUnits("milliseconds")
_CSctpMaxInitRetr_Type = Unsigned32
_CSctpMaxInitRetr_Object = MibScalar
cSctpMaxInitRetr = _CSctpMaxInitRetr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 7),
    _CSctpMaxInitRetr_Type()
)
cSctpMaxInitRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpMaxInitRetr.setStatus("current")
_CSctpCurrEstab_Type = Gauge32
_CSctpCurrEstab_Object = MibScalar
cSctpCurrEstab = _CSctpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 8),
    _CSctpCurrEstab_Type()
)
cSctpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpCurrEstab.setStatus("current")
_CSctpActiveEstabs_Type = Counter64
_CSctpActiveEstabs_Object = MibScalar
cSctpActiveEstabs = _CSctpActiveEstabs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 9),
    _CSctpActiveEstabs_Type()
)
cSctpActiveEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpActiveEstabs.setStatus("current")
_CSctpPassiveEstabs_Type = Counter64
_CSctpPassiveEstabs_Object = MibScalar
cSctpPassiveEstabs = _CSctpPassiveEstabs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 10),
    _CSctpPassiveEstabs_Type()
)
cSctpPassiveEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpPassiveEstabs.setStatus("current")
_CSctpAborteds_Type = Counter64
_CSctpAborteds_Object = MibScalar
cSctpAborteds = _CSctpAborteds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 11),
    _CSctpAborteds_Type()
)
cSctpAborteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAborteds.setStatus("current")
_CSctpShutdowns_Type = Counter64
_CSctpShutdowns_Object = MibScalar
cSctpShutdowns = _CSctpShutdowns_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 12),
    _CSctpShutdowns_Type()
)
cSctpShutdowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpShutdowns.setStatus("current")
_CSctpStatOutOfBlues_Type = Counter64
_CSctpStatOutOfBlues_Object = MibScalar
cSctpStatOutOfBlues = _CSctpStatOutOfBlues_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 13),
    _CSctpStatOutOfBlues_Type()
)
cSctpStatOutOfBlues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatOutOfBlues.setStatus("current")
_CSctpStatChecksumErrors_Type = Counter64
_CSctpStatChecksumErrors_Object = MibScalar
cSctpStatChecksumErrors = _CSctpStatChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 14),
    _CSctpStatChecksumErrors_Type()
)
cSctpStatChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatChecksumErrors.setStatus("current")
_CSctpStatSentCtrlChunks_Type = Counter64
_CSctpStatSentCtrlChunks_Object = MibScalar
cSctpStatSentCtrlChunks = _CSctpStatSentCtrlChunks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 15),
    _CSctpStatSentCtrlChunks_Type()
)
cSctpStatSentCtrlChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatSentCtrlChunks.setStatus("current")
_CSctpStatSentOrderChunks_Type = Counter64
_CSctpStatSentOrderChunks_Object = MibScalar
cSctpStatSentOrderChunks = _CSctpStatSentOrderChunks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 16),
    _CSctpStatSentOrderChunks_Type()
)
cSctpStatSentOrderChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatSentOrderChunks.setStatus("current")
_CSctpStatSentUnorderChunks_Type = Counter64
_CSctpStatSentUnorderChunks_Object = MibScalar
cSctpStatSentUnorderChunks = _CSctpStatSentUnorderChunks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 17),
    _CSctpStatSentUnorderChunks_Type()
)
cSctpStatSentUnorderChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatSentUnorderChunks.setStatus("current")
_CSctpStatRecCtrlChunks_Type = Counter64
_CSctpStatRecCtrlChunks_Object = MibScalar
cSctpStatRecCtrlChunks = _CSctpStatRecCtrlChunks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 18),
    _CSctpStatRecCtrlChunks_Type()
)
cSctpStatRecCtrlChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatRecCtrlChunks.setStatus("current")
_CSctpStatRecOrderChunks_Type = Counter64
_CSctpStatRecOrderChunks_Object = MibScalar
cSctpStatRecOrderChunks = _CSctpStatRecOrderChunks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 19),
    _CSctpStatRecOrderChunks_Type()
)
cSctpStatRecOrderChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatRecOrderChunks.setStatus("current")
_CSctpStatRecUnorderChunks_Type = Counter64
_CSctpStatRecUnorderChunks_Object = MibScalar
cSctpStatRecUnorderChunks = _CSctpStatRecUnorderChunks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 20),
    _CSctpStatRecUnorderChunks_Type()
)
cSctpStatRecUnorderChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatRecUnorderChunks.setStatus("current")
_CSctpStatFragmentedUsrMessages_Type = Counter64
_CSctpStatFragmentedUsrMessages_Object = MibScalar
cSctpStatFragmentedUsrMessages = _CSctpStatFragmentedUsrMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 21),
    _CSctpStatFragmentedUsrMessages_Type()
)
cSctpStatFragmentedUsrMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatFragmentedUsrMessages.setStatus("current")
_CSctpStatReassembledUsrMessages_Type = Counter64
_CSctpStatReassembledUsrMessages_Object = MibScalar
cSctpStatReassembledUsrMessages = _CSctpStatReassembledUsrMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 22),
    _CSctpStatReassembledUsrMessages_Type()
)
cSctpStatReassembledUsrMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatReassembledUsrMessages.setStatus("current")
_CSctpStatSentSCTPPacks_Type = Counter64
_CSctpStatSentSCTPPacks_Object = MibScalar
cSctpStatSentSCTPPacks = _CSctpStatSentSCTPPacks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 23),
    _CSctpStatSentSCTPPacks_Type()
)
cSctpStatSentSCTPPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatSentSCTPPacks.setStatus("current")
_CSctpStatRecSCTPPacks_Type = Counter64
_CSctpStatRecSCTPPacks_Object = MibScalar
cSctpStatRecSCTPPacks = _CSctpStatRecSCTPPacks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 1, 24),
    _CSctpStatRecSCTPPacks_Type()
)
cSctpStatRecSCTPPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpStatRecSCTPPacks.setStatus("current")
_CSctpTables_ObjectIdentity = ObjectIdentity
cSctpTables = _CSctpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2)
)
_CSctpAssocTable_Object = MibTable
cSctpAssocTable = _CSctpAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cSctpAssocTable.setStatus("current")
_CSctpAssocEntry_Object = MibTableRow
cSctpAssocEntry = _CSctpAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1)
)
cSctpAssocEntry.setIndexNames(
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocId"),
)
if mibBuilder.loadTexts:
    cSctpAssocEntry.setStatus("current")
_CSctpAssocId_Type = Unsigned32
_CSctpAssocId_Object = MibTableColumn
cSctpAssocId = _CSctpAssocId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 1),
    _CSctpAssocId_Type()
)
cSctpAssocId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSctpAssocId.setStatus("current")


class _CSctpAssocRemHostName_Type(OctetString):
    """Custom type cSctpAssocRemHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CSctpAssocRemHostName_Type.__name__ = "OctetString"
_CSctpAssocRemHostName_Object = MibTableColumn
cSctpAssocRemHostName = _CSctpAssocRemHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 2),
    _CSctpAssocRemHostName_Type()
)
cSctpAssocRemHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemHostName.setStatus("current")
_CSctpAssocLocalSCTPPort_Type = InetPortNumber
_CSctpAssocLocalSCTPPort_Object = MibTableColumn
cSctpAssocLocalSCTPPort = _CSctpAssocLocalSCTPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 3),
    _CSctpAssocLocalSCTPPort_Type()
)
cSctpAssocLocalSCTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocLocalSCTPPort.setStatus("current")
_CSctpAssocRemSCTPPort_Type = InetPortNumber
_CSctpAssocRemSCTPPort_Object = MibTableColumn
cSctpAssocRemSCTPPort = _CSctpAssocRemSCTPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 4),
    _CSctpAssocRemSCTPPort_Type()
)
cSctpAssocRemSCTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemSCTPPort.setStatus("current")
_CSctpAssocRemPrimaryAddressType_Type = InetAddressType
_CSctpAssocRemPrimaryAddressType_Object = MibTableColumn
cSctpAssocRemPrimaryAddressType = _CSctpAssocRemPrimaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 5),
    _CSctpAssocRemPrimaryAddressType_Type()
)
cSctpAssocRemPrimaryAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemPrimaryAddressType.setStatus("current")
_CSctpAssocRemPrimaryAddress_Type = InetAddress
_CSctpAssocRemPrimaryAddress_Object = MibTableColumn
cSctpAssocRemPrimaryAddress = _CSctpAssocRemPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 6),
    _CSctpAssocRemPrimaryAddress_Type()
)
cSctpAssocRemPrimaryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemPrimaryAddress.setStatus("current")
_CSctpAssocHeartBeatTimer_Type = Unsigned32
_CSctpAssocHeartBeatTimer_Object = MibTableColumn
cSctpAssocHeartBeatTimer = _CSctpAssocHeartBeatTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 8),
    _CSctpAssocHeartBeatTimer_Type()
)
cSctpAssocHeartBeatTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocHeartBeatTimer.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocHeartBeatTimer.setUnits("milliseconds")


class _CSctpAssocState_Type(Integer32):
    """Custom type cSctpAssocState based on Integer32"""
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


_CSctpAssocState_Type.__name__ = "Integer32"
_CSctpAssocState_Object = MibTableColumn
cSctpAssocState = _CSctpAssocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 9),
    _CSctpAssocState_Type()
)
cSctpAssocState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cSctpAssocState.setStatus("current")
_CSctpAssocInStreams_Type = Unsigned32
_CSctpAssocInStreams_Object = MibTableColumn
cSctpAssocInStreams = _CSctpAssocInStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 10),
    _CSctpAssocInStreams_Type()
)
cSctpAssocInStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocInStreams.setStatus("current")
_CSctpAssocOutStreams_Type = Unsigned32
_CSctpAssocOutStreams_Object = MibTableColumn
cSctpAssocOutStreams = _CSctpAssocOutStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 11),
    _CSctpAssocOutStreams_Type()
)
cSctpAssocOutStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocOutStreams.setStatus("current")
_CSctpAssocMaxRetr_Type = Unsigned32
_CSctpAssocMaxRetr_Object = MibTableColumn
cSctpAssocMaxRetr = _CSctpAssocMaxRetr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 12),
    _CSctpAssocMaxRetr_Type()
)
cSctpAssocMaxRetr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocMaxRetr.setStatus("current")
_CSctpAssocT1expireds_Type = Counter64
_CSctpAssocT1expireds_Object = MibTableColumn
cSctpAssocT1expireds = _CSctpAssocT1expireds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 13),
    _CSctpAssocT1expireds_Type()
)
cSctpAssocT1expireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocT1expireds.setStatus("current")
_CSctpAssocT2expireds_Type = Counter64
_CSctpAssocT2expireds_Object = MibTableColumn
cSctpAssocT2expireds = _CSctpAssocT2expireds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 14),
    _CSctpAssocT2expireds_Type()
)
cSctpAssocT2expireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocT2expireds.setStatus("current")
_CSctpAssocRtxChunks_Type = Counter64
_CSctpAssocRtxChunks_Object = MibTableColumn
cSctpAssocRtxChunks = _CSctpAssocRtxChunks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 15),
    _CSctpAssocRtxChunks_Type()
)
cSctpAssocRtxChunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRtxChunks.setStatus("current")
_CSctpAssocStartTime_Type = TimeStamp
_CSctpAssocStartTime_Object = MibTableColumn
cSctpAssocStartTime = _CSctpAssocStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 2, 1, 17),
    _CSctpAssocStartTime_Type()
)
cSctpAssocStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocStartTime.setStatus("current")
_CSctpAssocLocalAddressTable_Object = MibTable
cSctpAssocLocalAddressTable = _CSctpAssocLocalAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cSctpAssocLocalAddressTable.setStatus("current")
_CSctpAssocLocalAddressEntry_Object = MibTableRow
cSctpAssocLocalAddressEntry = _CSctpAssocLocalAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 3, 1)
)
cSctpAssocLocalAddressEntry.setIndexNames(
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocId"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocLocalAddressIPType"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocLocalAddressIP"),
)
if mibBuilder.loadTexts:
    cSctpAssocLocalAddressEntry.setStatus("current")
_CSctpAssocLocalAddressIPType_Type = InetAddressType
_CSctpAssocLocalAddressIPType_Object = MibTableColumn
cSctpAssocLocalAddressIPType = _CSctpAssocLocalAddressIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 3, 1, 1),
    _CSctpAssocLocalAddressIPType_Type()
)
cSctpAssocLocalAddressIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSctpAssocLocalAddressIPType.setStatus("current")
_CSctpAssocLocalAddressIP_Type = InetAddress
_CSctpAssocLocalAddressIP_Object = MibTableColumn
cSctpAssocLocalAddressIP = _CSctpAssocLocalAddressIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 3, 1, 2),
    _CSctpAssocLocalAddressIP_Type()
)
cSctpAssocLocalAddressIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSctpAssocLocalAddressIP.setStatus("current")
_CSctpAssocLocalAddressStartTime_Type = TimeStamp
_CSctpAssocLocalAddressStartTime_Object = MibTableColumn
cSctpAssocLocalAddressStartTime = _CSctpAssocLocalAddressStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 3, 1, 3),
    _CSctpAssocLocalAddressStartTime_Type()
)
cSctpAssocLocalAddressStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocLocalAddressStartTime.setStatus("current")
_CSctpAssocRemAddressTable_Object = MibTable
cSctpAssocRemAddressTable = _CSctpAssocRemAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cSctpAssocRemAddressTable.setStatus("current")
_CSctpAssocRemAddressEntry_Object = MibTableRow
cSctpAssocRemAddressEntry = _CSctpAssocRemAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 4, 1)
)
cSctpAssocRemAddressEntry.setIndexNames(
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocId"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressIPType"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressIP"),
)
if mibBuilder.loadTexts:
    cSctpAssocRemAddressEntry.setStatus("current")
_CSctpAssocRemAddressIPType_Type = InetAddressType
_CSctpAssocRemAddressIPType_Object = MibTableColumn
cSctpAssocRemAddressIPType = _CSctpAssocRemAddressIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 4, 1, 1),
    _CSctpAssocRemAddressIPType_Type()
)
cSctpAssocRemAddressIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressIPType.setStatus("current")
_CSctpAssocRemAddressIP_Type = InetAddress
_CSctpAssocRemAddressIP_Object = MibTableColumn
cSctpAssocRemAddressIP = _CSctpAssocRemAddressIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 4, 1, 2),
    _CSctpAssocRemAddressIP_Type()
)
cSctpAssocRemAddressIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressIP.setStatus("current")


class _CSctpAssocRemAddressStatus_Type(Integer32):
    """Custom type cSctpAssocRemAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_CSctpAssocRemAddressStatus_Type.__name__ = "Integer32"
_CSctpAssocRemAddressStatus_Object = MibTableColumn
cSctpAssocRemAddressStatus = _CSctpAssocRemAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 4, 1, 3),
    _CSctpAssocRemAddressStatus_Type()
)
cSctpAssocRemAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressStatus.setStatus("current")


class _CSctpAssocRemAddressHBFlag_Type(Integer32):
    """Custom type cSctpAssocRemAddressHBFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("inactive", 1))
    )


_CSctpAssocRemAddressHBFlag_Type.__name__ = "Integer32"
_CSctpAssocRemAddressHBFlag_Object = MibTableColumn
cSctpAssocRemAddressHBFlag = _CSctpAssocRemAddressHBFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 4, 1, 4),
    _CSctpAssocRemAddressHBFlag_Type()
)
cSctpAssocRemAddressHBFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressHBFlag.setStatus("current")
_CSctpAssocRemAddressRTO_Type = Unsigned32
_CSctpAssocRemAddressRTO_Object = MibTableColumn
cSctpAssocRemAddressRTO = _CSctpAssocRemAddressRTO_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 4, 1, 5),
    _CSctpAssocRemAddressRTO_Type()
)
cSctpAssocRemAddressRTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressRTO.setStatus("current")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressRTO.setUnits("milliseconds")
_CSctpAssocRemAddressMaxPathRtx_Type = Unsigned32
_CSctpAssocRemAddressMaxPathRtx_Object = MibTableColumn
cSctpAssocRemAddressMaxPathRtx = _CSctpAssocRemAddressMaxPathRtx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 4, 1, 6),
    _CSctpAssocRemAddressMaxPathRtx_Type()
)
cSctpAssocRemAddressMaxPathRtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressMaxPathRtx.setStatus("current")
_CSctpAssocRemAddressRtx_Type = Counter64
_CSctpAssocRemAddressRtx_Object = MibTableColumn
cSctpAssocRemAddressRtx = _CSctpAssocRemAddressRtx_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 4, 1, 7),
    _CSctpAssocRemAddressRtx_Type()
)
cSctpAssocRemAddressRtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressRtx.setStatus("current")
_CSctpAssocRemAddressStartTime_Type = TimeStamp
_CSctpAssocRemAddressStartTime_Object = MibTableColumn
cSctpAssocRemAddressStartTime = _CSctpAssocRemAddressStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 4, 1, 8),
    _CSctpAssocRemAddressStartTime_Type()
)
cSctpAssocRemAddressStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpAssocRemAddressStartTime.setStatus("current")
_CSctpLookupLocalPortTable_Object = MibTable
cSctpLookupLocalPortTable = _CSctpLookupLocalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cSctpLookupLocalPortTable.setStatus("current")
_CSctpLookupLocalPortEntry_Object = MibTableRow
cSctpLookupLocalPortEntry = _CSctpLookupLocalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 5, 1)
)
cSctpLookupLocalPortEntry.setIndexNames(
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocLocalSCTPPort"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocId"),
)
if mibBuilder.loadTexts:
    cSctpLookupLocalPortEntry.setStatus("current")
_CSctpLookupLocalPortStartTime_Type = TimeStamp
_CSctpLookupLocalPortStartTime_Object = MibTableColumn
cSctpLookupLocalPortStartTime = _CSctpLookupLocalPortStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 5, 1, 1),
    _CSctpLookupLocalPortStartTime_Type()
)
cSctpLookupLocalPortStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpLookupLocalPortStartTime.setStatus("current")
_CSctpLookupRemPortTable_Object = MibTable
cSctpLookupRemPortTable = _CSctpLookupRemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cSctpLookupRemPortTable.setStatus("current")
_CSctpLookupRemPortEntry_Object = MibTableRow
cSctpLookupRemPortEntry = _CSctpLookupRemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 6, 1)
)
cSctpLookupRemPortEntry.setIndexNames(
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocRemSCTPPort"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocId"),
)
if mibBuilder.loadTexts:
    cSctpLookupRemPortEntry.setStatus("current")
_CSctpLookupRemPortStartTime_Type = TimeStamp
_CSctpLookupRemPortStartTime_Object = MibTableColumn
cSctpLookupRemPortStartTime = _CSctpLookupRemPortStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 6, 1, 1),
    _CSctpLookupRemPortStartTime_Type()
)
cSctpLookupRemPortStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpLookupRemPortStartTime.setStatus("current")
_CSctpLookupRemHostNameTable_Object = MibTable
cSctpLookupRemHostNameTable = _CSctpLookupRemHostNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cSctpLookupRemHostNameTable.setStatus("current")
_CSctpLookupRemHostNameEntry_Object = MibTableRow
cSctpLookupRemHostNameEntry = _CSctpLookupRemHostNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 7, 1)
)
cSctpLookupRemHostNameEntry.setIndexNames(
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocRemHostName"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocId"),
)
if mibBuilder.loadTexts:
    cSctpLookupRemHostNameEntry.setStatus("current")
_CSctpLookupRemHostNameStartTime_Type = TimeStamp
_CSctpLookupRemHostNameStartTime_Object = MibTableColumn
cSctpLookupRemHostNameStartTime = _CSctpLookupRemHostNameStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 7, 1, 1),
    _CSctpLookupRemHostNameStartTime_Type()
)
cSctpLookupRemHostNameStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpLookupRemHostNameStartTime.setStatus("current")
_CSctpLookupRemPrimIPAddrTable_Object = MibTable
cSctpLookupRemPrimIPAddrTable = _CSctpLookupRemPrimIPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cSctpLookupRemPrimIPAddrTable.setStatus("current")
_CSctpLookupRemPrimIPAddrEntry_Object = MibTableRow
cSctpLookupRemPrimIPAddrEntry = _CSctpLookupRemPrimIPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 8, 1)
)
cSctpLookupRemPrimIPAddrEntry.setIndexNames(
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocRemPrimaryAddressType"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocRemPrimaryAddress"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocId"),
)
if mibBuilder.loadTexts:
    cSctpLookupRemPrimIPAddrEntry.setStatus("current")
_CSctpLookupRemPrimIPAddrStartTime_Type = TimeStamp
_CSctpLookupRemPrimIPAddrStartTime_Object = MibTableColumn
cSctpLookupRemPrimIPAddrStartTime = _CSctpLookupRemPrimIPAddrStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 8, 1, 1),
    _CSctpLookupRemPrimIPAddrStartTime_Type()
)
cSctpLookupRemPrimIPAddrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpLookupRemPrimIPAddrStartTime.setStatus("current")
_CSctpLookupRemIPAddrTable_Object = MibTable
cSctpLookupRemIPAddrTable = _CSctpLookupRemIPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cSctpLookupRemIPAddrTable.setStatus("current")
_CSctpLookupRemIPAddrEntry_Object = MibTableRow
cSctpLookupRemIPAddrEntry = _CSctpLookupRemIPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 9, 1)
)
cSctpLookupRemIPAddrEntry.setIndexNames(
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressIPType"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressIP"),
    (0, "CISCO-IETF-SCTP-MIB", "cSctpAssocId"),
)
if mibBuilder.loadTexts:
    cSctpLookupRemIPAddrEntry.setStatus("current")
_CSctpLookupRemIPAddrStartTime_Type = TimeStamp
_CSctpLookupRemIPAddrStartTime_Object = MibTableColumn
cSctpLookupRemIPAddrStartTime = _CSctpLookupRemIPAddrStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 1, 2, 9, 1, 1),
    _CSctpLookupRemIPAddrStartTime_Type()
)
cSctpLookupRemIPAddrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cSctpLookupRemIPAddrStartTime.setStatus("current")
_CSctpConformance_ObjectIdentity = ObjectIdentity
cSctpConformance = _CSctpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 2)
)
_CSctpGroups_ObjectIdentity = ObjectIdentity
cSctpGroups = _CSctpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 2, 1)
)
_CSctpCompliances_ObjectIdentity = ObjectIdentity
cSctpCompliances = _CSctpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 2, 2)
)

# Managed Objects groups

cSctpGeneralVariablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 2, 1, 1)
)
cSctpGeneralVariablesGroup.setObjects(
      *(("CISCO-IETF-SCTP-MIB", "cSctpRtoAlgorithm"),
        ("CISCO-IETF-SCTP-MIB", "cSctpRtoMin"),
        ("CISCO-IETF-SCTP-MIB", "cSctpRtoMax"),
        ("CISCO-IETF-SCTP-MIB", "cSctpRtoInitial"),
        ("CISCO-IETF-SCTP-MIB", "cSctpMaxAssoc"),
        ("CISCO-IETF-SCTP-MIB", "cSctpValCookieLife"),
        ("CISCO-IETF-SCTP-MIB", "cSctpMaxInitRetr"))
)
if mibBuilder.loadTexts:
    cSctpGeneralVariablesGroup.setStatus("current")

cSctpStateStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 2, 1, 2)
)
cSctpStateStatGroup.setObjects(
      *(("CISCO-IETF-SCTP-MIB", "cSctpCurrEstab"),
        ("CISCO-IETF-SCTP-MIB", "cSctpActiveEstabs"),
        ("CISCO-IETF-SCTP-MIB", "cSctpPassiveEstabs"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAborteds"),
        ("CISCO-IETF-SCTP-MIB", "cSctpShutdowns"))
)
if mibBuilder.loadTexts:
    cSctpStateStatGroup.setStatus("current")

cSctpOtherStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 2, 1, 3)
)
cSctpOtherStatGroup.setObjects(
      *(("CISCO-IETF-SCTP-MIB", "cSctpStatOutOfBlues"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatChecksumErrors"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatSentCtrlChunks"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatSentOrderChunks"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatSentUnorderChunks"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatRecCtrlChunks"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatRecOrderChunks"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatRecUnorderChunks"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatFragmentedUsrMessages"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatReassembledUsrMessages"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatSentSCTPPacks"),
        ("CISCO-IETF-SCTP-MIB", "cSctpStatRecSCTPPacks"))
)
if mibBuilder.loadTexts:
    cSctpOtherStatGroup.setStatus("current")

cSctpAssocTablesVariablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 2, 1, 4)
)
cSctpAssocTablesVariablesGroup.setObjects(
      *(("CISCO-IETF-SCTP-MIB", "cSctpAssocRemHostName"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocLocalSCTPPort"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocRemSCTPPort"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocRemPrimaryAddressType"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocRemPrimaryAddress"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocHeartBeatTimer"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocState"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocInStreams"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocOutStreams"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocMaxRetr"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocT1expireds"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocT2expireds"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocRtxChunks"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocStartTime"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocLocalAddressStartTime"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressStatus"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressHBFlag"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressRTO"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressMaxPathRtx"),
        ("CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressStartTime"))
)
if mibBuilder.loadTexts:
    cSctpAssocTablesVariablesGroup.setStatus("current")

cSctpAssocStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 2, 1, 5)
)
cSctpAssocStatGroup.setObjects(
    ("CISCO-IETF-SCTP-MIB", "cSctpAssocRemAddressRtx")
)
if mibBuilder.loadTexts:
    cSctpAssocStatGroup.setStatus("current")

cSctpInverseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 2, 1, 6)
)
cSctpInverseGroup.setObjects(
      *(("CISCO-IETF-SCTP-MIB", "cSctpLookupLocalPortStartTime"),
        ("CISCO-IETF-SCTP-MIB", "cSctpLookupRemPortStartTime"),
        ("CISCO-IETF-SCTP-MIB", "cSctpLookupRemHostNameStartTime"),
        ("CISCO-IETF-SCTP-MIB", "cSctpLookupRemPrimIPAddrStartTime"),
        ("CISCO-IETF-SCTP-MIB", "cSctpLookupRemIPAddrStartTime"))
)
if mibBuilder.loadTexts:
    cSctpInverseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cSctpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 75, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cSctpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-SCTP-MIB",
    **{"InetPortNumber": InetPortNumber,
       "cSctpMIB": cSctpMIB,
       "cSctpObjects": cSctpObjects,
       "cSctpScalars": cSctpScalars,
       "cSctpRtoAlgorithm": cSctpRtoAlgorithm,
       "cSctpRtoMin": cSctpRtoMin,
       "cSctpRtoMax": cSctpRtoMax,
       "cSctpRtoInitial": cSctpRtoInitial,
       "cSctpMaxAssoc": cSctpMaxAssoc,
       "cSctpValCookieLife": cSctpValCookieLife,
       "cSctpMaxInitRetr": cSctpMaxInitRetr,
       "cSctpCurrEstab": cSctpCurrEstab,
       "cSctpActiveEstabs": cSctpActiveEstabs,
       "cSctpPassiveEstabs": cSctpPassiveEstabs,
       "cSctpAborteds": cSctpAborteds,
       "cSctpShutdowns": cSctpShutdowns,
       "cSctpStatOutOfBlues": cSctpStatOutOfBlues,
       "cSctpStatChecksumErrors": cSctpStatChecksumErrors,
       "cSctpStatSentCtrlChunks": cSctpStatSentCtrlChunks,
       "cSctpStatSentOrderChunks": cSctpStatSentOrderChunks,
       "cSctpStatSentUnorderChunks": cSctpStatSentUnorderChunks,
       "cSctpStatRecCtrlChunks": cSctpStatRecCtrlChunks,
       "cSctpStatRecOrderChunks": cSctpStatRecOrderChunks,
       "cSctpStatRecUnorderChunks": cSctpStatRecUnorderChunks,
       "cSctpStatFragmentedUsrMessages": cSctpStatFragmentedUsrMessages,
       "cSctpStatReassembledUsrMessages": cSctpStatReassembledUsrMessages,
       "cSctpStatSentSCTPPacks": cSctpStatSentSCTPPacks,
       "cSctpStatRecSCTPPacks": cSctpStatRecSCTPPacks,
       "cSctpTables": cSctpTables,
       "cSctpAssocTable": cSctpAssocTable,
       "cSctpAssocEntry": cSctpAssocEntry,
       "cSctpAssocId": cSctpAssocId,
       "cSctpAssocRemHostName": cSctpAssocRemHostName,
       "cSctpAssocLocalSCTPPort": cSctpAssocLocalSCTPPort,
       "cSctpAssocRemSCTPPort": cSctpAssocRemSCTPPort,
       "cSctpAssocRemPrimaryAddressType": cSctpAssocRemPrimaryAddressType,
       "cSctpAssocRemPrimaryAddress": cSctpAssocRemPrimaryAddress,
       "cSctpAssocHeartBeatTimer": cSctpAssocHeartBeatTimer,
       "cSctpAssocState": cSctpAssocState,
       "cSctpAssocInStreams": cSctpAssocInStreams,
       "cSctpAssocOutStreams": cSctpAssocOutStreams,
       "cSctpAssocMaxRetr": cSctpAssocMaxRetr,
       "cSctpAssocT1expireds": cSctpAssocT1expireds,
       "cSctpAssocT2expireds": cSctpAssocT2expireds,
       "cSctpAssocRtxChunks": cSctpAssocRtxChunks,
       "cSctpAssocStartTime": cSctpAssocStartTime,
       "cSctpAssocLocalAddressTable": cSctpAssocLocalAddressTable,
       "cSctpAssocLocalAddressEntry": cSctpAssocLocalAddressEntry,
       "cSctpAssocLocalAddressIPType": cSctpAssocLocalAddressIPType,
       "cSctpAssocLocalAddressIP": cSctpAssocLocalAddressIP,
       "cSctpAssocLocalAddressStartTime": cSctpAssocLocalAddressStartTime,
       "cSctpAssocRemAddressTable": cSctpAssocRemAddressTable,
       "cSctpAssocRemAddressEntry": cSctpAssocRemAddressEntry,
       "cSctpAssocRemAddressIPType": cSctpAssocRemAddressIPType,
       "cSctpAssocRemAddressIP": cSctpAssocRemAddressIP,
       "cSctpAssocRemAddressStatus": cSctpAssocRemAddressStatus,
       "cSctpAssocRemAddressHBFlag": cSctpAssocRemAddressHBFlag,
       "cSctpAssocRemAddressRTO": cSctpAssocRemAddressRTO,
       "cSctpAssocRemAddressMaxPathRtx": cSctpAssocRemAddressMaxPathRtx,
       "cSctpAssocRemAddressRtx": cSctpAssocRemAddressRtx,
       "cSctpAssocRemAddressStartTime": cSctpAssocRemAddressStartTime,
       "cSctpLookupLocalPortTable": cSctpLookupLocalPortTable,
       "cSctpLookupLocalPortEntry": cSctpLookupLocalPortEntry,
       "cSctpLookupLocalPortStartTime": cSctpLookupLocalPortStartTime,
       "cSctpLookupRemPortTable": cSctpLookupRemPortTable,
       "cSctpLookupRemPortEntry": cSctpLookupRemPortEntry,
       "cSctpLookupRemPortStartTime": cSctpLookupRemPortStartTime,
       "cSctpLookupRemHostNameTable": cSctpLookupRemHostNameTable,
       "cSctpLookupRemHostNameEntry": cSctpLookupRemHostNameEntry,
       "cSctpLookupRemHostNameStartTime": cSctpLookupRemHostNameStartTime,
       "cSctpLookupRemPrimIPAddrTable": cSctpLookupRemPrimIPAddrTable,
       "cSctpLookupRemPrimIPAddrEntry": cSctpLookupRemPrimIPAddrEntry,
       "cSctpLookupRemPrimIPAddrStartTime": cSctpLookupRemPrimIPAddrStartTime,
       "cSctpLookupRemIPAddrTable": cSctpLookupRemIPAddrTable,
       "cSctpLookupRemIPAddrEntry": cSctpLookupRemIPAddrEntry,
       "cSctpLookupRemIPAddrStartTime": cSctpLookupRemIPAddrStartTime,
       "cSctpConformance": cSctpConformance,
       "cSctpGroups": cSctpGroups,
       "cSctpGeneralVariablesGroup": cSctpGeneralVariablesGroup,
       "cSctpStateStatGroup": cSctpStateStatGroup,
       "cSctpOtherStatGroup": cSctpOtherStatGroup,
       "cSctpAssocTablesVariablesGroup": cSctpAssocTablesVariablesGroup,
       "cSctpAssocStatGroup": cSctpAssocStatGroup,
       "cSctpInverseGroup": cSctpInverseGroup,
       "cSctpCompliances": cSctpCompliances,
       "cSctpCompliance": cSctpCompliance}
)
