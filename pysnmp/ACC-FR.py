# SNMP MIB module (ACC-FR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-FR
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:17 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccFr_ObjectIdentity = ObjectIdentity
accFr = _AccFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20)
)
_AccFrAtTable_Object = MibTable
accFrAtTable = _AccFrAtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    accFrAtTable.setStatus("mandatory")
_AccFrAtEntry_Object = MibTableRow
accFrAtEntry = _AccFrAtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1, 1)
)
accFrAtEntry.setIndexNames(
    (0, "ACC-FR", "accFrAtIfIndex"),
    (0, "ACC-FR", "accFrIpAddress"),
)
if mibBuilder.loadTexts:
    accFrAtEntry.setStatus("mandatory")
_AccFrAtIfIndex_Type = Integer32
_AccFrAtIfIndex_Object = MibTableColumn
accFrAtIfIndex = _AccFrAtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1, 1, 1),
    _AccFrAtIfIndex_Type()
)
accFrAtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrAtIfIndex.setStatus("mandatory")
_AccFrIpAddress_Type = IpAddress
_AccFrIpAddress_Object = MibTableColumn
accFrIpAddress = _AccFrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1, 1, 2),
    _AccFrIpAddress_Type()
)
accFrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrIpAddress.setStatus("mandatory")
_AccFrDLCI_Type = Integer32
_AccFrDLCI_Object = MibTableColumn
accFrDLCI = _AccFrDLCI_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1, 1, 3),
    _AccFrDLCI_Type()
)
accFrDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDLCI.setStatus("mandatory")


class _AccFrStatus_Type(Integer32):
    """Custom type accFrStatus based on Integer32"""
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
        *(("confirm-pending", 3),
          ("dynamic", 2),
          ("not-connected", 4),
          ("permanent", 1))
    )


_AccFrStatus_Type.__name__ = "Integer32"
_AccFrStatus_Object = MibTableColumn
accFrStatus = _AccFrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1, 1, 4),
    _AccFrStatus_Type()
)
accFrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrStatus.setStatus("mandatory")
_AccFrStatTable_Object = MibTable
accFrStatTable = _AccFrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2)
)
if mibBuilder.loadTexts:
    accFrStatTable.setStatus("mandatory")
_AccFrStatEntry_Object = MibTableRow
accFrStatEntry = _AccFrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1)
)
accFrStatEntry.setIndexNames(
    (0, "ACC-FR", "accFrIndex"),
)
if mibBuilder.loadTexts:
    accFrStatEntry.setStatus("mandatory")
_AccFrIndex_Type = Integer32
_AccFrIndex_Object = MibTableColumn
accFrIndex = _AccFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 1),
    _AccFrIndex_Type()
)
accFrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrIndex.setStatus("mandatory")
_AccFrStatRcvDrops_Type = Counter32
_AccFrStatRcvDrops_Object = MibTableColumn
accFrStatRcvDrops = _AccFrStatRcvDrops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 2),
    _AccFrStatRcvDrops_Type()
)
accFrStatRcvDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatRcvDrops.setStatus("mandatory")
_AccFrStatShorts_Type = Counter32
_AccFrStatShorts_Object = MibTableColumn
accFrStatShorts = _AccFrStatShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 3),
    _AccFrStatShorts_Type()
)
accFrStatShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatShorts.setStatus("mandatory")
_AccFrStatIllDlcis_Type = Counter32
_AccFrStatIllDlcis_Object = MibTableColumn
accFrStatIllDlcis = _AccFrStatIllDlcis_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 4),
    _AccFrStatIllDlcis_Type()
)
accFrStatIllDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatIllDlcis.setStatus("mandatory")
_AccFrStatUnkDlcis_Type = Counter32
_AccFrStatUnkDlcis_Object = MibTableColumn
accFrStatUnkDlcis = _AccFrStatUnkDlcis_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 5),
    _AccFrStatUnkDlcis_Type()
)
accFrStatUnkDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatUnkDlcis.setStatus("mandatory")
_AccFrStatUnkProtos_Type = Counter32
_AccFrStatUnkProtos_Object = MibTableColumn
accFrStatUnkProtos = _AccFrStatUnkProtos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 6),
    _AccFrStatUnkProtos_Type()
)
accFrStatUnkProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatUnkProtos.setStatus("mandatory")
_AccFrStatRsrvDlcis_Type = Counter32
_AccFrStatRsrvDlcis_Object = MibTableColumn
accFrStatRsrvDlcis = _AccFrStatRsrvDlcis_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 7),
    _AccFrStatRsrvDlcis_Type()
)
accFrStatRsrvDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatRsrvDlcis.setStatus("mandatory")
_AccFrStatXmtDrops_Type = Counter32
_AccFrStatXmtDrops_Object = MibTableColumn
accFrStatXmtDrops = _AccFrStatXmtDrops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 8),
    _AccFrStatXmtDrops_Type()
)
accFrStatXmtDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatXmtDrops.setStatus("mandatory")
_AccFrStatErrTime_Type = TimeTicks
_AccFrStatErrTime_Object = MibTableColumn
accFrStatErrTime = _AccFrStatErrTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 9),
    _AccFrStatErrTime_Type()
)
accFrStatErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatErrTime.setStatus("mandatory")


class _AccFrStatErrType_Type(Integer32):
    """Custom type accFrStatErrType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("dlcmiProtoErr", 11),
          ("dlcmiSequenceErr", 13),
          ("dlcmiUnknownIE", 12),
          ("dlcmiUnknownRpt", 14),
          ("illDlci", 3),
          ("illegalDLCI", 10),
          ("rcvDrop", 1),
          ("receiveLong", 9),
          ("rsrvDlci", 6),
          ("short", 2),
          ("unkDlci", 4),
          ("unkProto", 5),
          ("unknownError", 8),
          ("xmtDrop", 7))
    )


_AccFrStatErrType_Type.__name__ = "Integer32"
_AccFrStatErrType_Object = MibTableColumn
accFrStatErrType = _AccFrStatErrType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 10),
    _AccFrStatErrType_Type()
)
accFrStatErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatErrType.setStatus("mandatory")
_AccFrStatErrDlci_Type = Integer32
_AccFrStatErrDlci_Object = MibTableColumn
accFrStatErrDlci = _AccFrStatErrDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 11),
    _AccFrStatErrDlci_Type()
)
accFrStatErrDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatErrDlci.setStatus("mandatory")
_AccFrStatErrProto_Type = Integer32
_AccFrStatErrProto_Object = MibTableColumn
accFrStatErrProto = _AccFrStatErrProto_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 12),
    _AccFrStatErrProto_Type()
)
accFrStatErrProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatErrProto.setStatus("mandatory")


class _AccFrLinkState_Type(Integer32):
    """Custom type accFrLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("idle", 3),
          ("up", 2))
    )


_AccFrLinkState_Type.__name__ = "Integer32"
_AccFrLinkState_Object = MibTableColumn
accFrLinkState = _AccFrLinkState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 13),
    _AccFrLinkState_Type()
)
accFrLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrLinkState.setStatus("mandatory")
_AccFrStatUnks_Type = Counter32
_AccFrStatUnks_Object = MibTableColumn
accFrStatUnks = _AccFrStatUnks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 14),
    _AccFrStatUnks_Type()
)
accFrStatUnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatUnks.setStatus("mandatory")
_AccFrStatRcvLongs_Type = Counter32
_AccFrStatRcvLongs_Object = MibTableColumn
accFrStatRcvLongs = _AccFrStatRcvLongs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 15),
    _AccFrStatRcvLongs_Type()
)
accFrStatRcvLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatRcvLongs.setStatus("mandatory")
_AccFrStatIlgDlcis_Type = Counter32
_AccFrStatIlgDlcis_Object = MibTableColumn
accFrStatIlgDlcis = _AccFrStatIlgDlcis_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 16),
    _AccFrStatIlgDlcis_Type()
)
accFrStatIlgDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatIlgDlcis.setStatus("mandatory")
_AccFrStatProtoErrs_Type = Counter32
_AccFrStatProtoErrs_Object = MibTableColumn
accFrStatProtoErrs = _AccFrStatProtoErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 17),
    _AccFrStatProtoErrs_Type()
)
accFrStatProtoErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatProtoErrs.setStatus("mandatory")
_AccFrStatUnkIes_Type = Counter32
_AccFrStatUnkIes_Object = MibTableColumn
accFrStatUnkIes = _AccFrStatUnkIes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 18),
    _AccFrStatUnkIes_Type()
)
accFrStatUnkIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatUnkIes.setStatus("mandatory")
_AccFrStatSeqErrs_Type = Counter32
_AccFrStatSeqErrs_Object = MibTableColumn
accFrStatSeqErrs = _AccFrStatSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 19),
    _AccFrStatSeqErrs_Type()
)
accFrStatSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatSeqErrs.setStatus("mandatory")
_AccFrStatUnkRpts_Type = Counter32
_AccFrStatUnkRpts_Object = MibTableColumn
accFrStatUnkRpts = _AccFrStatUnkRpts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 20),
    _AccFrStatUnkRpts_Type()
)
accFrStatUnkRpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatUnkRpts.setStatus("mandatory")
_AccFrParmTable_Object = MibTable
accFrParmTable = _AccFrParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3)
)
if mibBuilder.loadTexts:
    accFrParmTable.setStatus("mandatory")
_AccFrParmEntry_Object = MibTableRow
accFrParmEntry = _AccFrParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1)
)
accFrParmEntry.setIndexNames(
    (0, "ACC-FR", "accFrParmIndex"),
)
if mibBuilder.loadTexts:
    accFrParmEntry.setStatus("mandatory")
_AccFrParmIndex_Type = Integer32
_AccFrParmIndex_Object = MibTableColumn
accFrParmIndex = _AccFrParmIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 1),
    _AccFrParmIndex_Type()
)
accFrParmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrParmIndex.setStatus("mandatory")


class _AccFrParmAddrFmt_Type(Integer32):
    """Custom type accFrParmAddrFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("draft-q922", 2),
          ("q921", 1),
          ("q922", 3))
    )


_AccFrParmAddrFmt_Type.__name__ = "Integer32"
_AccFrParmAddrFmt_Object = MibTableColumn
accFrParmAddrFmt = _AccFrParmAddrFmt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 2),
    _AccFrParmAddrFmt_Type()
)
accFrParmAddrFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrParmAddrFmt.setStatus("mandatory")


class _AccFrParmAddrLen_Type(Integer32):
    """Custom type accFrParmAddrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_AccFrParmAddrLen_Type.__name__ = "Integer32"
_AccFrParmAddrLen_Object = MibTableColumn
accFrParmAddrLen = _AccFrParmAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 3),
    _AccFrParmAddrLen_Type()
)
accFrParmAddrLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrParmAddrLen.setStatus("mandatory")


class _AccFrParmEncap_Type(Integer32):
    """Custom type accFrParmEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("early", 1),
          ("ietf", 2))
    )


_AccFrParmEncap_Type.__name__ = "Integer32"
_AccFrParmEncap_Object = MibTableColumn
accFrParmEncap = _AccFrParmEncap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 4),
    _AccFrParmEncap_Type()
)
accFrParmEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrParmEncap.setStatus("mandatory")


class _AccFrDlcmiState_Type(Integer32):
    """Custom type accFrDlcmiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexd", 3),
          ("lmi", 2),
          ("off", 1))
    )


_AccFrDlcmiState_Type.__name__ = "Integer32"
_AccFrDlcmiState_Object = MibTableColumn
accFrDlcmiState = _AccFrDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 5),
    _AccFrDlcmiState_Type()
)
accFrDlcmiState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiState.setStatus("mandatory")


class _AccFrDlcmiPollInt_Type(Integer32):
    """Custom type accFrDlcmiPollInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AccFrDlcmiPollInt_Type.__name__ = "Integer32"
_AccFrDlcmiPollInt_Object = MibTableColumn
accFrDlcmiPollInt = _AccFrDlcmiPollInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 6),
    _AccFrDlcmiPollInt_Type()
)
accFrDlcmiPollInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiPollInt.setStatus("mandatory")


class _AccFrDlcmiFullStatEnq_Type(Integer32):
    """Custom type accFrDlcmiFullStatEnq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccFrDlcmiFullStatEnq_Type.__name__ = "Integer32"
_AccFrDlcmiFullStatEnq_Object = MibTableColumn
accFrDlcmiFullStatEnq = _AccFrDlcmiFullStatEnq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 7),
    _AccFrDlcmiFullStatEnq_Type()
)
accFrDlcmiFullStatEnq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiFullStatEnq.setStatus("mandatory")


class _AccFrDlcmiErrThres_Type(Integer32):
    """Custom type accFrDlcmiErrThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AccFrDlcmiErrThres_Type.__name__ = "Integer32"
_AccFrDlcmiErrThres_Object = MibTableColumn
accFrDlcmiErrThres = _AccFrDlcmiErrThres_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 8),
    _AccFrDlcmiErrThres_Type()
)
accFrDlcmiErrThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiErrThres.setStatus("mandatory")


class _AccFrDlcmiMonEvents_Type(Integer32):
    """Custom type accFrDlcmiMonEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AccFrDlcmiMonEvents_Type.__name__ = "Integer32"
_AccFrDlcmiMonEvents_Object = MibTableColumn
accFrDlcmiMonEvents = _AccFrDlcmiMonEvents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 9),
    _AccFrDlcmiMonEvents_Type()
)
accFrDlcmiMonEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiMonEvents.setStatus("mandatory")


class _AccFrDlcmiType_Type(Integer32):
    """Custom type accFrDlcmiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_AccFrDlcmiType_Type.__name__ = "Integer32"
_AccFrDlcmiType_Object = MibTableColumn
accFrDlcmiType = _AccFrDlcmiType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 10),
    _AccFrDlcmiType_Type()
)
accFrDlcmiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiType.setStatus("mandatory")


class _AccFrDlcmiIdleTimer_Type(Integer32):
    """Custom type accFrDlcmiIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccFrDlcmiIdleTimer_Type.__name__ = "Integer32"
_AccFrDlcmiIdleTimer_Object = MibTableColumn
accFrDlcmiIdleTimer = _AccFrDlcmiIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 11),
    _AccFrDlcmiIdleTimer_Type()
)
accFrDlcmiIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiIdleTimer.setStatus("mandatory")
_AccFrCktTable_Object = MibTable
accFrCktTable = _AccFrCktTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4)
)
if mibBuilder.loadTexts:
    accFrCktTable.setStatus("mandatory")
_AccFrCktEntry_Object = MibTableRow
accFrCktEntry = _AccFrCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1)
)
accFrCktEntry.setIndexNames(
    (0, "ACC-FR", "accFrCktIfIndex"),
    (0, "ACC-FR", "accFrCktDlci"),
)
if mibBuilder.loadTexts:
    accFrCktEntry.setStatus("mandatory")
_AccFrCktIfIndex_Type = Integer32
_AccFrCktIfIndex_Object = MibTableColumn
accFrCktIfIndex = _AccFrCktIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 1),
    _AccFrCktIfIndex_Type()
)
accFrCktIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktIfIndex.setStatus("mandatory")
_AccFrCktDlci_Type = Integer32
_AccFrCktDlci_Object = MibTableColumn
accFrCktDlci = _AccFrCktDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 2),
    _AccFrCktDlci_Type()
)
accFrCktDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktDlci.setStatus("mandatory")


class _AccFrCktState_Type(Integer32):
    """Custom type accFrCktState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_AccFrCktState_Type.__name__ = "Integer32"
_AccFrCktState_Object = MibTableColumn
accFrCktState = _AccFrCktState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 3),
    _AccFrCktState_Type()
)
accFrCktState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktState.setStatus("mandatory")
_AccFrCktFECNrcvds_Type = Counter32
_AccFrCktFECNrcvds_Object = MibTableColumn
accFrCktFECNrcvds = _AccFrCktFECNrcvds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 4),
    _AccFrCktFECNrcvds_Type()
)
accFrCktFECNrcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktFECNrcvds.setStatus("mandatory")
_AccFrCktBECNrcvds_Type = Counter32
_AccFrCktBECNrcvds_Object = MibTableColumn
accFrCktBECNrcvds = _AccFrCktBECNrcvds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 5),
    _AccFrCktBECNrcvds_Type()
)
accFrCktBECNrcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktBECNrcvds.setStatus("mandatory")
_AccFrCktFrameXmts_Type = Counter32
_AccFrCktFrameXmts_Object = MibTableColumn
accFrCktFrameXmts = _AccFrCktFrameXmts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 6),
    _AccFrCktFrameXmts_Type()
)
accFrCktFrameXmts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktFrameXmts.setStatus("mandatory")
_AccFrCktOctetXmts_Type = Counter32
_AccFrCktOctetXmts_Object = MibTableColumn
accFrCktOctetXmts = _AccFrCktOctetXmts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 7),
    _AccFrCktOctetXmts_Type()
)
accFrCktOctetXmts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktOctetXmts.setStatus("mandatory")
_AccFrCktFrameRcvs_Type = Counter32
_AccFrCktFrameRcvs_Object = MibTableColumn
accFrCktFrameRcvs = _AccFrCktFrameRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 8),
    _AccFrCktFrameRcvs_Type()
)
accFrCktFrameRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktFrameRcvs.setStatus("mandatory")
_AccFrCktOctetRcvs_Type = Counter32
_AccFrCktOctetRcvs_Object = MibTableColumn
accFrCktOctetRcvs = _AccFrCktOctetRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 9),
    _AccFrCktOctetRcvs_Type()
)
accFrCktOctetRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktOctetRcvs.setStatus("mandatory")
_AccFrCktCreateTime_Type = TimeTicks
_AccFrCktCreateTime_Object = MibTableColumn
accFrCktCreateTime = _AccFrCktCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 10),
    _AccFrCktCreateTime_Type()
)
accFrCktCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktCreateTime.setStatus("mandatory")
_AccFrCktChangeTime_Type = TimeTicks
_AccFrCktChangeTime_Object = MibTableColumn
accFrCktChangeTime = _AccFrCktChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 11),
    _AccFrCktChangeTime_Type()
)
accFrCktChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktChangeTime.setStatus("mandatory")


class _AccFfrCktLoop_Type(Integer32):
    """Custom type accFfrCktLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 2),
          ("normal", 1))
    )


_AccFfrCktLoop_Type.__name__ = "Integer32"
_AccFfrCktLoop_Object = MibTableColumn
accFfrCktLoop = _AccFfrCktLoop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 12),
    _AccFfrCktLoop_Type()
)
accFfrCktLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrCktLoop.setStatus("mandatory")
_AccFfrSwitchParameterTable_Object = MibTable
accFfrSwitchParameterTable = _AccFfrSwitchParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5)
)
if mibBuilder.loadTexts:
    accFfrSwitchParameterTable.setStatus("mandatory")
_AccFfrSwitchParameterEntry_Object = MibTableRow
accFfrSwitchParameterEntry = _AccFfrSwitchParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1)
)
accFfrSwitchParameterEntry.setIndexNames(
    (0, "ACC-FR", "accFfrSwitchIfindex1"),
    (0, "ACC-FR", "accFfrSwitchDlci1"),
)
if mibBuilder.loadTexts:
    accFfrSwitchParameterEntry.setStatus("mandatory")
_AccFfrSwitchIfindex1_Type = Integer32
_AccFfrSwitchIfindex1_Object = MibTableColumn
accFfrSwitchIfindex1 = _AccFfrSwitchIfindex1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1, 1),
    _AccFfrSwitchIfindex1_Type()
)
accFfrSwitchIfindex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrSwitchIfindex1.setStatus("mandatory")
_AccFfrSwitchDlci1_Type = Integer32
_AccFfrSwitchDlci1_Object = MibTableColumn
accFfrSwitchDlci1 = _AccFfrSwitchDlci1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1, 2),
    _AccFfrSwitchDlci1_Type()
)
accFfrSwitchDlci1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrSwitchDlci1.setStatus("mandatory")
_AccFfrSwitchIfindex2_Type = Integer32
_AccFfrSwitchIfindex2_Object = MibTableColumn
accFfrSwitchIfindex2 = _AccFfrSwitchIfindex2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1, 3),
    _AccFfrSwitchIfindex2_Type()
)
accFfrSwitchIfindex2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrSwitchIfindex2.setStatus("mandatory")
_AccFfrSwitchDlci2_Type = Integer32
_AccFfrSwitchDlci2_Object = MibTableColumn
accFfrSwitchDlci2 = _AccFfrSwitchDlci2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1, 4),
    _AccFfrSwitchDlci2_Type()
)
accFfrSwitchDlci2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrSwitchDlci2.setStatus("mandatory")


class _AccFfrSwitchStatus_Type(Integer32):
    """Custom type accFfrSwitchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 128),
          ("disable", 2),
          ("enable", 1))
    )


_AccFfrSwitchStatus_Type.__name__ = "Integer32"
_AccFfrSwitchStatus_Object = MibTableColumn
accFfrSwitchStatus = _AccFfrSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1, 5),
    _AccFfrSwitchStatus_Type()
)
accFfrSwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrSwitchStatus.setStatus("mandatory")
_AccVFRTable_Object = MibTable
accVFRTable = _AccVFRTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 6)
)
if mibBuilder.loadTexts:
    accVFRTable.setStatus("mandatory")
_AccVFRTableEntry_Object = MibTableRow
accVFRTableEntry = _AccVFRTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 6, 1)
)
accVFRTableEntry.setIndexNames(
    (0, "ACC-FR", "accVFRVirtualPort"),
    (0, "ACC-FR", "accVFRPhysicalPort"),
    (0, "ACC-FR", "accVFRDlci"),
)
if mibBuilder.loadTexts:
    accVFRTableEntry.setStatus("mandatory")
_AccVFRVirtualPort_Type = Integer32
_AccVFRVirtualPort_Object = MibTableColumn
accVFRVirtualPort = _AccVFRVirtualPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 6, 1, 1),
    _AccVFRVirtualPort_Type()
)
accVFRVirtualPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accVFRVirtualPort.setStatus("mandatory")
_AccVFRPhysicalPort_Type = Integer32
_AccVFRPhysicalPort_Object = MibTableColumn
accVFRPhysicalPort = _AccVFRPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 6, 1, 2),
    _AccVFRPhysicalPort_Type()
)
accVFRPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accVFRPhysicalPort.setStatus("mandatory")
_AccVFRDlci_Type = Integer32
_AccVFRDlci_Object = MibTableColumn
accVFRDlci = _AccVFRDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 6, 1, 3),
    _AccVFRDlci_Type()
)
accVFRDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accVFRDlci.setStatus("mandatory")


class _AccVFRStatus_Type(Integer32):
    """Custom type accVFRStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccVFRStatus_Type.__name__ = "Integer32"
_AccVFRStatus_Object = MibTableColumn
accVFRStatus = _AccVFRStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 6, 1, 4),
    _AccVFRStatus_Type()
)
accVFRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accVFRStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-FR",
    **{"accFr": accFr,
       "accFrAtTable": accFrAtTable,
       "accFrAtEntry": accFrAtEntry,
       "accFrAtIfIndex": accFrAtIfIndex,
       "accFrIpAddress": accFrIpAddress,
       "accFrDLCI": accFrDLCI,
       "accFrStatus": accFrStatus,
       "accFrStatTable": accFrStatTable,
       "accFrStatEntry": accFrStatEntry,
       "accFrIndex": accFrIndex,
       "accFrStatRcvDrops": accFrStatRcvDrops,
       "accFrStatShorts": accFrStatShorts,
       "accFrStatIllDlcis": accFrStatIllDlcis,
       "accFrStatUnkDlcis": accFrStatUnkDlcis,
       "accFrStatUnkProtos": accFrStatUnkProtos,
       "accFrStatRsrvDlcis": accFrStatRsrvDlcis,
       "accFrStatXmtDrops": accFrStatXmtDrops,
       "accFrStatErrTime": accFrStatErrTime,
       "accFrStatErrType": accFrStatErrType,
       "accFrStatErrDlci": accFrStatErrDlci,
       "accFrStatErrProto": accFrStatErrProto,
       "accFrLinkState": accFrLinkState,
       "accFrStatUnks": accFrStatUnks,
       "accFrStatRcvLongs": accFrStatRcvLongs,
       "accFrStatIlgDlcis": accFrStatIlgDlcis,
       "accFrStatProtoErrs": accFrStatProtoErrs,
       "accFrStatUnkIes": accFrStatUnkIes,
       "accFrStatSeqErrs": accFrStatSeqErrs,
       "accFrStatUnkRpts": accFrStatUnkRpts,
       "accFrParmTable": accFrParmTable,
       "accFrParmEntry": accFrParmEntry,
       "accFrParmIndex": accFrParmIndex,
       "accFrParmAddrFmt": accFrParmAddrFmt,
       "accFrParmAddrLen": accFrParmAddrLen,
       "accFrParmEncap": accFrParmEncap,
       "accFrDlcmiState": accFrDlcmiState,
       "accFrDlcmiPollInt": accFrDlcmiPollInt,
       "accFrDlcmiFullStatEnq": accFrDlcmiFullStatEnq,
       "accFrDlcmiErrThres": accFrDlcmiErrThres,
       "accFrDlcmiMonEvents": accFrDlcmiMonEvents,
       "accFrDlcmiType": accFrDlcmiType,
       "accFrDlcmiIdleTimer": accFrDlcmiIdleTimer,
       "accFrCktTable": accFrCktTable,
       "accFrCktEntry": accFrCktEntry,
       "accFrCktIfIndex": accFrCktIfIndex,
       "accFrCktDlci": accFrCktDlci,
       "accFrCktState": accFrCktState,
       "accFrCktFECNrcvds": accFrCktFECNrcvds,
       "accFrCktBECNrcvds": accFrCktBECNrcvds,
       "accFrCktFrameXmts": accFrCktFrameXmts,
       "accFrCktOctetXmts": accFrCktOctetXmts,
       "accFrCktFrameRcvs": accFrCktFrameRcvs,
       "accFrCktOctetRcvs": accFrCktOctetRcvs,
       "accFrCktCreateTime": accFrCktCreateTime,
       "accFrCktChangeTime": accFrCktChangeTime,
       "accFfrCktLoop": accFfrCktLoop,
       "accFfrSwitchParameterTable": accFfrSwitchParameterTable,
       "accFfrSwitchParameterEntry": accFfrSwitchParameterEntry,
       "accFfrSwitchIfindex1": accFfrSwitchIfindex1,
       "accFfrSwitchDlci1": accFfrSwitchDlci1,
       "accFfrSwitchIfindex2": accFfrSwitchIfindex2,
       "accFfrSwitchDlci2": accFfrSwitchDlci2,
       "accFfrSwitchStatus": accFfrSwitchStatus,
       "accVFRTable": accVFRTable,
       "accVFRTableEntry": accVFRTableEntry,
       "accVFRVirtualPort": accVFRVirtualPort,
       "accVFRPhysicalPort": accVFRPhysicalPort,
       "accVFRDlci": accVFRDlci,
       "accVFRStatus": accVFRStatus}
)
