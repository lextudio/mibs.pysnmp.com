# SNMP MIB module (ACC-ISDN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-ISDN
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:28 2024
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

(accTrapLogSeqNum,
 accTrapLogSeverityType) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum",
    "accTrapLogSeverityType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccIsdn_ObjectIdentity = ObjectIdentity
accIsdn = _AccIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36)
)
_AccIsdnDsl_ObjectIdentity = ObjectIdentity
accIsdnDsl = _AccIsdnDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 1)
)


class _AccIsdnDslIndex_Type(Integer32):
    """Custom type accIsdnDslIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccIsdnDslIndex_Type.__name__ = "Integer32"
_AccIsdnDslIndex_Object = MibScalar
accIsdnDslIndex = _AccIsdnDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 1, 1),
    _AccIsdnDslIndex_Type()
)
accIsdnDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnDslIndex.setStatus("deprecated")
_AccIsdnSubTable_Object = MibTable
accIsdnSubTable = _AccIsdnSubTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2)
)
if mibBuilder.loadTexts:
    accIsdnSubTable.setStatus("deprecated")
_AccIsdnSubEntry_Object = MibTableRow
accIsdnSubEntry = _AccIsdnSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1)
)
accIsdnSubEntry.setIndexNames(
    (0, "ACC-ISDN", "accIsdnDslIndex"),
)
if mibBuilder.loadTexts:
    accIsdnSubEntry.setStatus("deprecated")


class _AccIsdnSubSwitchType_Type(Integer32):
    """Custom type accIsdnSubSwitchType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("bri-1tr6", 8),
          ("bri-5ess", 2),
          ("bri-ccitt", 10),
          ("bri-dms100", 3),
          ("bri-kdd", 6),
          ("bri-net3", 1),
          ("bri-ni1", 9),
          ("bri-ntt", 7),
          ("bri-vn2", 4),
          ("bri-vn3", 5))
    )


_AccIsdnSubSwitchType_Type.__name__ = "Integer32"
_AccIsdnSubSwitchType_Object = MibTableColumn
accIsdnSubSwitchType = _AccIsdnSubSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1, 1),
    _AccIsdnSubSwitchType_Type()
)
accIsdnSubSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSubSwitchType.setStatus("deprecated")


class _AccIsdnSubChannelMode_Type(Integer32):
    """Custom type accIsdnSubChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cm-1b-plus-d", 1),
          ("cm-1h-plus-d", 3),
          ("cm-2b-plus-d", 2))
    )


_AccIsdnSubChannelMode_Type.__name__ = "Integer32"
_AccIsdnSubChannelMode_Object = MibTableColumn
accIsdnSubChannelMode = _AccIsdnSubChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1, 2),
    _AccIsdnSubChannelMode_Type()
)
accIsdnSubChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSubChannelMode.setStatus("deprecated")


class _AccIsdnSubAdminStatus_Type(Integer32):
    """Custom type accIsdnSubAdminStatus based on Integer32"""
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


_AccIsdnSubAdminStatus_Type.__name__ = "Integer32"
_AccIsdnSubAdminStatus_Object = MibTableColumn
accIsdnSubAdminStatus = _AccIsdnSubAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1, 3),
    _AccIsdnSubAdminStatus_Type()
)
accIsdnSubAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSubAdminStatus.setStatus("deprecated")


class _AccIsdnSubDiagLevel_Type(Integer32):
    """Custom type accIsdnSubDiagLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AccIsdnSubDiagLevel_Type.__name__ = "Integer32"
_AccIsdnSubDiagLevel_Object = MibTableColumn
accIsdnSubDiagLevel = _AccIsdnSubDiagLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1, 4),
    _AccIsdnSubDiagLevel_Type()
)
accIsdnSubDiagLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSubDiagLevel.setStatus("deprecated")


class _AccIsdnSubManualTei_Type(Integer32):
    """Custom type accIsdnSubManualTei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AccIsdnSubManualTei_Type.__name__ = "Integer32"
_AccIsdnSubManualTei_Object = MibTableColumn
accIsdnSubManualTei = _AccIsdnSubManualTei_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1, 5),
    _AccIsdnSubManualTei_Type()
)
accIsdnSubManualTei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSubManualTei.setStatus("deprecated")
_AccIsdnStatTable_Object = MibTable
accIsdnStatTable = _AccIsdnStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3)
)
if mibBuilder.loadTexts:
    accIsdnStatTable.setStatus("deprecated")
_AccIsdnStatEntry_Object = MibTableRow
accIsdnStatEntry = _AccIsdnStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1)
)
accIsdnStatEntry.setIndexNames(
    (0, "ACC-ISDN", "accIsdnDslIndex"),
)
if mibBuilder.loadTexts:
    accIsdnStatEntry.setStatus("deprecated")
_AccIsdnStatHdlcInPackets_Type = Counter32
_AccIsdnStatHdlcInPackets_Object = MibTableColumn
accIsdnStatHdlcInPackets = _AccIsdnStatHdlcInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 1),
    _AccIsdnStatHdlcInPackets_Type()
)
accIsdnStatHdlcInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcInPackets.setStatus("deprecated")
_AccIsdnStatHdlcInOctets_Type = Counter32
_AccIsdnStatHdlcInOctets_Object = MibTableColumn
accIsdnStatHdlcInOctets = _AccIsdnStatHdlcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 2),
    _AccIsdnStatHdlcInOctets_Type()
)
accIsdnStatHdlcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcInOctets.setStatus("deprecated")
_AccIsdnStatHdlcInErrors_Type = Counter32
_AccIsdnStatHdlcInErrors_Object = MibTableColumn
accIsdnStatHdlcInErrors = _AccIsdnStatHdlcInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 3),
    _AccIsdnStatHdlcInErrors_Type()
)
accIsdnStatHdlcInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcInErrors.setStatus("deprecated")
_AccIsdnStatHdlcInDiscs_Type = Counter32
_AccIsdnStatHdlcInDiscs_Object = MibTableColumn
accIsdnStatHdlcInDiscs = _AccIsdnStatHdlcInDiscs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 4),
    _AccIsdnStatHdlcInDiscs_Type()
)
accIsdnStatHdlcInDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcInDiscs.setStatus("deprecated")
_AccIsdnStatHdlcOutPackets_Type = Counter32
_AccIsdnStatHdlcOutPackets_Object = MibTableColumn
accIsdnStatHdlcOutPackets = _AccIsdnStatHdlcOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 5),
    _AccIsdnStatHdlcOutPackets_Type()
)
accIsdnStatHdlcOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcOutPackets.setStatus("deprecated")
_AccIsdnStatHdlcOutOctets_Type = Counter32
_AccIsdnStatHdlcOutOctets_Object = MibTableColumn
accIsdnStatHdlcOutOctets = _AccIsdnStatHdlcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 6),
    _AccIsdnStatHdlcOutOctets_Type()
)
accIsdnStatHdlcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcOutOctets.setStatus("deprecated")
_AccIsdnStatHdlcOutErrors_Type = Counter32
_AccIsdnStatHdlcOutErrors_Object = MibTableColumn
accIsdnStatHdlcOutErrors = _AccIsdnStatHdlcOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 7),
    _AccIsdnStatHdlcOutErrors_Type()
)
accIsdnStatHdlcOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcOutErrors.setStatus("deprecated")
_AccIsdnStatHdlcOutDiscs_Type = Counter32
_AccIsdnStatHdlcOutDiscs_Object = MibTableColumn
accIsdnStatHdlcOutDiscs = _AccIsdnStatHdlcOutDiscs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 8),
    _AccIsdnStatHdlcOutDiscs_Type()
)
accIsdnStatHdlcOutDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcOutDiscs.setStatus("deprecated")
_AccIsdnStatLapdUnsolicResps_Type = Counter32
_AccIsdnStatLapdUnsolicResps_Object = MibTableColumn
accIsdnStatLapdUnsolicResps = _AccIsdnStatLapdUnsolicResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 9),
    _AccIsdnStatLapdUnsolicResps_Type()
)
accIsdnStatLapdUnsolicResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdUnsolicResps.setStatus("deprecated")
_AccIsdnStatLapdPeerSabmes_Type = Counter32
_AccIsdnStatLapdPeerSabmes_Object = MibTableColumn
accIsdnStatLapdPeerSabmes = _AccIsdnStatLapdPeerSabmes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 10),
    _AccIsdnStatLapdPeerSabmes_Type()
)
accIsdnStatLapdPeerSabmes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdPeerSabmes.setStatus("deprecated")
_AccIsdnStatLapdN200Errors_Type = Counter32
_AccIsdnStatLapdN200Errors_Object = MibTableColumn
accIsdnStatLapdN200Errors = _AccIsdnStatLapdN200Errors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 11),
    _AccIsdnStatLapdN200Errors_Type()
)
accIsdnStatLapdN200Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdN200Errors.setStatus("deprecated")
_AccIsdnStatLapdNrSeqErrors_Type = Counter32
_AccIsdnStatLapdNrSeqErrors_Object = MibTableColumn
accIsdnStatLapdNrSeqErrors = _AccIsdnStatLapdNrSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 12),
    _AccIsdnStatLapdNrSeqErrors_Type()
)
accIsdnStatLapdNrSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdNrSeqErrors.setStatus("deprecated")
_AccIsdnStatLapdRecvdFrmrs_Type = Counter32
_AccIsdnStatLapdRecvdFrmrs_Object = MibTableColumn
accIsdnStatLapdRecvdFrmrs = _AccIsdnStatLapdRecvdFrmrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 13),
    _AccIsdnStatLapdRecvdFrmrs_Type()
)
accIsdnStatLapdRecvdFrmrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdRecvdFrmrs.setStatus("deprecated")
_AccIsdnStatLapdCntlErrors_Type = Counter32
_AccIsdnStatLapdCntlErrors_Object = MibTableColumn
accIsdnStatLapdCntlErrors = _AccIsdnStatLapdCntlErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 14),
    _AccIsdnStatLapdCntlErrors_Type()
)
accIsdnStatLapdCntlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdCntlErrors.setStatus("deprecated")
_AccIsdnStatLapdInfoErrors_Type = Counter32
_AccIsdnStatLapdInfoErrors_Object = MibTableColumn
accIsdnStatLapdInfoErrors = _AccIsdnStatLapdInfoErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 15),
    _AccIsdnStatLapdInfoErrors_Type()
)
accIsdnStatLapdInfoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdInfoErrors.setStatus("deprecated")
_AccIsdnStatLapdWrongSizes_Type = Counter32
_AccIsdnStatLapdWrongSizes_Object = MibTableColumn
accIsdnStatLapdWrongSizes = _AccIsdnStatLapdWrongSizes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 16),
    _AccIsdnStatLapdWrongSizes_Type()
)
accIsdnStatLapdWrongSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdWrongSizes.setStatus("deprecated")
_AccIsdnStatLapdN201Errors_Type = Counter32
_AccIsdnStatLapdN201Errors_Object = MibTableColumn
accIsdnStatLapdN201Errors = _AccIsdnStatLapdN201Errors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 17),
    _AccIsdnStatLapdN201Errors_Type()
)
accIsdnStatLapdN201Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdN201Errors.setStatus("deprecated")
_AccIsdnStatCallsOriginateds_Type = Counter32
_AccIsdnStatCallsOriginateds_Object = MibTableColumn
accIsdnStatCallsOriginateds = _AccIsdnStatCallsOriginateds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 18),
    _AccIsdnStatCallsOriginateds_Type()
)
accIsdnStatCallsOriginateds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsOriginateds.setStatus("deprecated")
_AccIsdnStatCallsOfferreds_Type = Counter32
_AccIsdnStatCallsOfferreds_Object = MibTableColumn
accIsdnStatCallsOfferreds = _AccIsdnStatCallsOfferreds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 19),
    _AccIsdnStatCallsOfferreds_Type()
)
accIsdnStatCallsOfferreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsOfferreds.setStatus("deprecated")
_AccIsdnStatCallsAnswereds_Type = Counter32
_AccIsdnStatCallsAnswereds_Object = MibTableColumn
accIsdnStatCallsAnswereds = _AccIsdnStatCallsAnswereds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 20),
    _AccIsdnStatCallsAnswereds_Type()
)
accIsdnStatCallsAnswereds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsAnswereds.setStatus("deprecated")
_AccIsdnStatCallsAccepteds_Type = Counter32
_AccIsdnStatCallsAccepteds_Object = MibTableColumn
accIsdnStatCallsAccepteds = _AccIsdnStatCallsAccepteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 21),
    _AccIsdnStatCallsAccepteds_Type()
)
accIsdnStatCallsAccepteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsAccepteds.setStatus("deprecated")
_AccIsdnStatCallsCompleteds_Type = Counter32
_AccIsdnStatCallsCompleteds_Object = MibTableColumn
accIsdnStatCallsCompleteds = _AccIsdnStatCallsCompleteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 22),
    _AccIsdnStatCallsCompleteds_Type()
)
accIsdnStatCallsCompleteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsCompleteds.setStatus("deprecated")
_AccIsdnStatCallsCleareds_Type = Counter32
_AccIsdnStatCallsCleareds_Object = MibTableColumn
accIsdnStatCallsCleareds = _AccIsdnStatCallsCleareds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 23),
    _AccIsdnStatCallsCleareds_Type()
)
accIsdnStatCallsCleareds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsCleareds.setStatus("deprecated")


class _AccIsdnStatDslOperStatus_Type(Integer32):
    """Custom type accIsdnStatDslOperStatus based on Integer32"""
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
        *(("activated", 3),
          ("established", 4),
          ("inactive", 1),
          ("waiting", 2))
    )


_AccIsdnStatDslOperStatus_Type.__name__ = "Integer32"
_AccIsdnStatDslOperStatus_Object = MibTableColumn
accIsdnStatDslOperStatus = _AccIsdnStatDslOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 24),
    _AccIsdnStatDslOperStatus_Type()
)
accIsdnStatDslOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatDslOperStatus.setStatus("deprecated")


class _AccIsdnStatLastCauses_Type(Integer32):
    """Custom type accIsdnStatLastCauses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnStatLastCauses_Type.__name__ = "Integer32"
_AccIsdnStatLastCauses_Object = MibTableColumn
accIsdnStatLastCauses = _AccIsdnStatLastCauses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 25),
    _AccIsdnStatLastCauses_Type()
)
accIsdnStatLastCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLastCauses.setStatus("deprecated")
_AccIsdnCallTable_Object = MibTable
accIsdnCallTable = _AccIsdnCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4)
)
if mibBuilder.loadTexts:
    accIsdnCallTable.setStatus("deprecated")
_AccIsdnCallEntry_Object = MibTableRow
accIsdnCallEntry = _AccIsdnCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1)
)
accIsdnCallEntry.setIndexNames(
    (0, "ACC-ISDN", "accIsdnCallDslIndex"),
    (0, "ACC-ISDN", "accIsdnCallIdentifier"),
)
if mibBuilder.loadTexts:
    accIsdnCallEntry.setStatus("deprecated")


class _AccIsdnCallIdentifier_Type(Integer32):
    """Custom type accIsdnCallIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AccIsdnCallIdentifier_Type.__name__ = "Integer32"
_AccIsdnCallIdentifier_Object = MibTableColumn
accIsdnCallIdentifier = _AccIsdnCallIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 1),
    _AccIsdnCallIdentifier_Type()
)
accIsdnCallIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallIdentifier.setStatus("deprecated")


class _AccIsdnCallReference_Type(Integer32):
    """Custom type accIsdnCallReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AccIsdnCallReference_Type.__name__ = "Integer32"
_AccIsdnCallReference_Object = MibTableColumn
accIsdnCallReference = _AccIsdnCallReference_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 2),
    _AccIsdnCallReference_Type()
)
accIsdnCallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallReference.setStatus("deprecated")


class _AccIsdnCallChannelId_Type(Integer32):
    """Custom type accIsdnCallChannelId based on Integer32"""
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
        *(("b1", 2),
          ("b2", 3),
          ("h0", 4),
          ("none", 1))
    )


_AccIsdnCallChannelId_Type.__name__ = "Integer32"
_AccIsdnCallChannelId_Object = MibTableColumn
accIsdnCallChannelId = _AccIsdnCallChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 3),
    _AccIsdnCallChannelId_Type()
)
accIsdnCallChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallChannelId.setStatus("deprecated")


class _AccIsdnCallIfIndex_Type(Integer32):
    """Custom type accIsdnCallIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("j1", 1),
          ("j2", 2))
    )


_AccIsdnCallIfIndex_Type.__name__ = "Integer32"
_AccIsdnCallIfIndex_Object = MibTableColumn
accIsdnCallIfIndex = _AccIsdnCallIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 4),
    _AccIsdnCallIfIndex_Type()
)
accIsdnCallIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallIfIndex.setStatus("deprecated")


class _AccIsdnCallInfoRate_Type(Integer32):
    """Custom type accIsdnCallInfoRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              17,
              18,
              20,
              22,
              24)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("r-1536k", 22),
          ("r-1920k", 24),
          ("r-2x64k", 18),
          ("r-384k", 20),
          ("r-64k", 17))
    )


_AccIsdnCallInfoRate_Type.__name__ = "Integer32"
_AccIsdnCallInfoRate_Object = MibTableColumn
accIsdnCallInfoRate = _AccIsdnCallInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 5),
    _AccIsdnCallInfoRate_Type()
)
accIsdnCallInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallInfoRate.setStatus("deprecated")


class _AccIsdnCallState_Type(Integer32):
    """Custom type accIsdnCallState based on Integer32"""
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
        *(("connected", 6),
          ("disconnected", 1),
          ("incoming", 2),
          ("outgoing", 3),
          ("releaseing", 5),
          ("routing", 4))
    )


_AccIsdnCallState_Type.__name__ = "Integer32"
_AccIsdnCallState_Object = MibTableColumn
accIsdnCallState = _AccIsdnCallState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 6),
    _AccIsdnCallState_Type()
)
accIsdnCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallState.setStatus("deprecated")


class _AccIsdnCallCause_Type(Integer32):
    """Custom type accIsdnCallCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnCallCause_Type.__name__ = "Integer32"
_AccIsdnCallCause_Object = MibTableColumn
accIsdnCallCause = _AccIsdnCallCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 7),
    _AccIsdnCallCause_Type()
)
accIsdnCallCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallCause.setStatus("deprecated")


class _AccIsdnCallOrigin_Type(Integer32):
    """Custom type accIsdnCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network", 3),
          ("none", 1),
          ("terminal", 2))
    )


_AccIsdnCallOrigin_Type.__name__ = "Integer32"
_AccIsdnCallOrigin_Object = MibTableColumn
accIsdnCallOrigin = _AccIsdnCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 8),
    _AccIsdnCallOrigin_Type()
)
accIsdnCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallOrigin.setStatus("deprecated")
_AccIsdnCallAddress_Type = OctetString
_AccIsdnCallAddress_Object = MibTableColumn
accIsdnCallAddress = _AccIsdnCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 9),
    _AccIsdnCallAddress_Type()
)
accIsdnCallAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallAddress.setStatus("deprecated")


class _AccIsdnCallDslIndex_Type(Integer32):
    """Custom type accIsdnCallDslIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccIsdnCallDslIndex_Type.__name__ = "Integer32"
_AccIsdnCallDslIndex_Object = MibTableColumn
accIsdnCallDslIndex = _AccIsdnCallDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 10),
    _AccIsdnCallDslIndex_Type()
)
accIsdnCallDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallDslIndex.setStatus("deprecated")
_AccIsdnTest_ObjectIdentity = ObjectIdentity
accIsdnTest = _AccIsdnTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5)
)


class _AccIsdnTestIfIndex_Type(Integer32):
    """Custom type accIsdnTestIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("j1", 1),
          ("j2", 2))
    )


_AccIsdnTestIfIndex_Type.__name__ = "Integer32"
_AccIsdnTestIfIndex_Object = MibScalar
accIsdnTestIfIndex = _AccIsdnTestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 1),
    _AccIsdnTestIfIndex_Type()
)
accIsdnTestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnTestIfIndex.setStatus("mandatory")
_AccIsdnTestAddress_Type = OctetString
_AccIsdnTestAddress_Object = MibScalar
accIsdnTestAddress = _AccIsdnTestAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 2),
    _AccIsdnTestAddress_Type()
)
accIsdnTestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnTestAddress.setStatus("mandatory")


class _AccIsdnTestCommand_Type(Integer32):
    """Custom type accIsdnTestCommand based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("activate", 10),
          ("call", 5),
          ("clear", 6),
          ("deactivate", 11),
          ("disconnect", 7),
          ("display", 12),
          ("ignore", 4),
          ("loop", 8),
          ("normal", 1),
          ("reject", 3),
          ("unloop", 9))
    )


_AccIsdnTestCommand_Type.__name__ = "Integer32"
_AccIsdnTestCommand_Object = MibScalar
accIsdnTestCommand = _AccIsdnTestCommand_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 3),
    _AccIsdnTestCommand_Type()
)
accIsdnTestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnTestCommand.setStatus("mandatory")


class _AccIsdnTestRouting_Type(Integer32):
    """Custom type accIsdnTestRouting based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("activate", 8),
          ("boff", 16),
          ("bon", 15),
          ("call", 5),
          ("clear", 6),
          ("deactivate", 9),
          ("disconnect", 7),
          ("display", 12),
          ("ignore", 4),
          ("loop4", 10),
          ("normal", 1),
          ("ones", 13),
          ("reject", 3),
          ("reset", 11),
          ("zeros", 14))
    )


_AccIsdnTestRouting_Type.__name__ = "Integer32"
_AccIsdnTestRouting_Object = MibScalar
accIsdnTestRouting = _AccIsdnTestRouting_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 4),
    _AccIsdnTestRouting_Type()
)
accIsdnTestRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnTestRouting.setStatus("mandatory")


class _AccIsdnTestRegName_Type(Integer32):
    """Custom type accIsdnTestRegName based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("br0", 16),
          ("br1", 17),
          ("br10", 26),
          ("br11", 27),
          ("br12", 28),
          ("br13", 29),
          ("br14", 30),
          ("br15", 31),
          ("br2", 18),
          ("br3", 19),
          ("br4", 20),
          ("br5", 21),
          ("br6", 22),
          ("br7", 23),
          ("br8", 24),
          ("br9", 25),
          ("nr0", 0),
          ("nr1", 1),
          ("nr2", 2),
          ("nr3", 3),
          ("nr4", 4),
          ("nr5", 5),
          ("nr6", 6))
    )


_AccIsdnTestRegName_Type.__name__ = "Integer32"
_AccIsdnTestRegName_Object = MibScalar
accIsdnTestRegName = _AccIsdnTestRegName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 5),
    _AccIsdnTestRegName_Type()
)
accIsdnTestRegName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnTestRegName.setStatus("mandatory")


class _AccIsdnTestRegValue_Type(Integer32):
    """Custom type accIsdnTestRegValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnTestRegValue_Type.__name__ = "Integer32"
_AccIsdnTestRegValue_Object = MibScalar
accIsdnTestRegValue = _AccIsdnTestRegValue_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 6),
    _AccIsdnTestRegValue_Type()
)
accIsdnTestRegValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnTestRegValue.setStatus("mandatory")


class _AccwIsdnTestBChanMode_Type(Integer32):
    """Custom type accwIsdnTestBChanMode based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("activate", 8),
          ("boff", 16),
          ("bon", 15),
          ("call", 5),
          ("clear", 6),
          ("deactivate", 9),
          ("disconnect", 7),
          ("display", 12),
          ("ignore", 4),
          ("loop4", 10),
          ("normal", 1),
          ("ones", 13),
          ("reject", 3),
          ("reset", 11),
          ("zeros", 14))
    )


_AccwIsdnTestBChanMode_Type.__name__ = "Integer32"
_AccwIsdnTestBChanMode_Object = MibScalar
accwIsdnTestBChanMode = _AccwIsdnTestBChanMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 7),
    _AccwIsdnTestBChanMode_Type()
)
accwIsdnTestBChanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accwIsdnTestBChanMode.setStatus("mandatory")
_AccwIsdnTestOptions_Type = Integer32
_AccwIsdnTestOptions_Object = MibScalar
accwIsdnTestOptions = _AccwIsdnTestOptions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 8),
    _AccwIsdnTestOptions_Type()
)
accwIsdnTestOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accwIsdnTestOptions.setStatus("mandatory")
_AccIsdnxSubTable_Object = MibTable
accIsdnxSubTable = _AccIsdnxSubTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6)
)
if mibBuilder.loadTexts:
    accIsdnxSubTable.setStatus("mandatory")
_AccIsdnxSubEntry_Object = MibTableRow
accIsdnxSubEntry = _AccIsdnxSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1)
)
accIsdnxSubEntry.setIndexNames(
    (0, "ACC-ISDN", "accIsdnxSubDslIndex"),
)
if mibBuilder.loadTexts:
    accIsdnxSubEntry.setStatus("mandatory")
_AccIsdnxSubDslIndex_Type = Integer32
_AccIsdnxSubDslIndex_Object = MibTableColumn
accIsdnxSubDslIndex = _AccIsdnxSubDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 1),
    _AccIsdnxSubDslIndex_Type()
)
accIsdnxSubDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxSubDslIndex.setStatus("mandatory")


class _AccIsdnxSubSwitchType_Type(Integer32):
    """Custom type accIsdnxSubSwitchType based on Integer32"""
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
              26)
        )
    )
    namedValues = NamedValues(
        *(("bri-1tr6", 8),
          ("bri-5ess", 2),
          ("bri-auto-na", 26),
          ("bri-ccitt", 10),
          ("bri-dms100", 3),
          ("bri-kdd", 6),
          ("bri-net3", 1),
          ("bri-ni1", 9),
          ("bri-ni2", 13),
          ("bri-ntt", 7),
          ("bri-tad2", 11),
          ("bri-ts013", 12),
          ("bri-vn2", 4),
          ("bri-vn3", 5),
          ("pri-1tr6", 21),
          ("pri-4ess", 14),
          ("pri-5ess", 15),
          ("pri-ccitt", 22),
          ("pri-dms100", 16),
          ("pri-kdd", 19),
          ("pri-net5", 17),
          ("pri-ni2", 25),
          ("pri-ntt", 20),
          ("pri-tad30", 23),
          ("pri-ts014", 24),
          ("pri-vn3", 18))
    )


_AccIsdnxSubSwitchType_Type.__name__ = "Integer32"
_AccIsdnxSubSwitchType_Object = MibTableColumn
accIsdnxSubSwitchType = _AccIsdnxSubSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 2),
    _AccIsdnxSubSwitchType_Type()
)
accIsdnxSubSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubSwitchType.setStatus("mandatory")


class _AccIsdnxSubChanConfig_Type(Integer32):
    """Custom type accIsdnxSubChanConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccIsdnxSubChanConfig_Type.__name__ = "Integer32"
_AccIsdnxSubChanConfig_Object = MibTableColumn
accIsdnxSubChanConfig = _AccIsdnxSubChanConfig_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 3),
    _AccIsdnxSubChanConfig_Type()
)
accIsdnxSubChanConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubChanConfig.setStatus("mandatory")


class _AccIsdnxSubAdminStatus_Type(Integer32):
    """Custom type accIsdnxSubAdminStatus based on Integer32"""
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
          ("drain", 3),
          ("enabled", 1))
    )


_AccIsdnxSubAdminStatus_Type.__name__ = "Integer32"
_AccIsdnxSubAdminStatus_Object = MibTableColumn
accIsdnxSubAdminStatus = _AccIsdnxSubAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 4),
    _AccIsdnxSubAdminStatus_Type()
)
accIsdnxSubAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubAdminStatus.setStatus("mandatory")


class _AccIsdnxSubDiagLevel_Type(Integer32):
    """Custom type accIsdnxSubDiagLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_AccIsdnxSubDiagLevel_Type.__name__ = "Integer32"
_AccIsdnxSubDiagLevel_Object = MibTableColumn
accIsdnxSubDiagLevel = _AccIsdnxSubDiagLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 5),
    _AccIsdnxSubDiagLevel_Type()
)
accIsdnxSubDiagLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubDiagLevel.setStatus("mandatory")


class _AccIsdnxSubManualTei_Type(Integer32):
    """Custom type accIsdnxSubManualTei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AccIsdnxSubManualTei_Type.__name__ = "Integer32"
_AccIsdnxSubManualTei_Object = MibTableColumn
accIsdnxSubManualTei = _AccIsdnxSubManualTei_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 6),
    _AccIsdnxSubManualTei_Type()
)
accIsdnxSubManualTei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubManualTei.setStatus("mandatory")


class _AccIsdnxSubOperStatus_Type(Integer32):
    """Custom type accIsdnxSubOperStatus based on Integer32"""
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
        *(("activated", 2),
          ("deactivated", 1),
          ("engaged", 4),
          ("established", 3))
    )


_AccIsdnxSubOperStatus_Type.__name__ = "Integer32"
_AccIsdnxSubOperStatus_Object = MibTableColumn
accIsdnxSubOperStatus = _AccIsdnxSubOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 7),
    _AccIsdnxSubOperStatus_Type()
)
accIsdnxSubOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubOperStatus.setStatus("mandatory")


class _AccIsdnxSubNumNfas_Type(Integer32):
    """Custom type accIsdnxSubNumNfas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnxSubNumNfas_Type.__name__ = "Integer32"
_AccIsdnxSubNumNfas_Object = MibTableColumn
accIsdnxSubNumNfas = _AccIsdnxSubNumNfas_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 8),
    _AccIsdnxSubNumNfas_Type()
)
accIsdnxSubNumNfas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxSubNumNfas.setStatus("mandatory")


class _AccIsdnxSubLastCause_Type(Integer32):
    """Custom type accIsdnxSubLastCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnxSubLastCause_Type.__name__ = "Integer32"
_AccIsdnxSubLastCause_Object = MibTableColumn
accIsdnxSubLastCause = _AccIsdnxSubLastCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 9),
    _AccIsdnxSubLastCause_Type()
)
accIsdnxSubLastCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxSubLastCause.setStatus("mandatory")


class _AccIsdnxSubSubaddrType_Type(Integer32):
    """Custom type accIsdnxSubSubaddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nsap", 1),
          ("user", 2))
    )


_AccIsdnxSubSubaddrType_Type.__name__ = "Integer32"
_AccIsdnxSubSubaddrType_Object = MibTableColumn
accIsdnxSubSubaddrType = _AccIsdnxSubSubaddrType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 10),
    _AccIsdnxSubSubaddrType_Type()
)
accIsdnxSubSubaddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubSubaddrType.setStatus("mandatory")


class _AccIsdnxSubVoiceOption_Type(Integer32):
    """Custom type accIsdnxSubVoiceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccIsdnxSubVoiceOption_Type.__name__ = "Integer32"
_AccIsdnxSubVoiceOption_Object = MibTableColumn
accIsdnxSubVoiceOption = _AccIsdnxSubVoiceOption_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 11),
    _AccIsdnxSubVoiceOption_Type()
)
accIsdnxSubVoiceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubVoiceOption.setStatus("mandatory")


class _AccIsdnxSubCliOption_Type(Integer32):
    """Custom type accIsdnxSubCliOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccIsdnxSubCliOption_Type.__name__ = "Integer32"
_AccIsdnxSubCliOption_Object = MibTableColumn
accIsdnxSubCliOption = _AccIsdnxSubCliOption_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 12),
    _AccIsdnxSubCliOption_Type()
)
accIsdnxSubCliOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubCliOption.setStatus("mandatory")


class _AccIsdnxSubEncodingMethod_Type(Integer32):
    """Custom type accIsdnxSubEncodingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a-law", 1),
          ("mu-law", 2))
    )


_AccIsdnxSubEncodingMethod_Type.__name__ = "Integer32"
_AccIsdnxSubEncodingMethod_Object = MibTableColumn
accIsdnxSubEncodingMethod = _AccIsdnxSubEncodingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 13),
    _AccIsdnxSubEncodingMethod_Type()
)
accIsdnxSubEncodingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxSubEncodingMethod.setStatus("mandatory")


class _AccIsdnxSubDialingMethod_Type(Integer32):
    """Custom type accIsdnxSubDialingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enbloc", 2),
          ("overlap", 1))
    )


_AccIsdnxSubDialingMethod_Type.__name__ = "Integer32"
_AccIsdnxSubDialingMethod_Object = MibTableColumn
accIsdnxSubDialingMethod = _AccIsdnxSubDialingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 14),
    _AccIsdnxSubDialingMethod_Type()
)
accIsdnxSubDialingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxSubDialingMethod.setStatus("mandatory")


class _AccIsdnxSubAutoSpid_Type(Integer32):
    """Custom type accIsdnxSubAutoSpid based on Integer32"""
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


_AccIsdnxSubAutoSpid_Type.__name__ = "Integer32"
_AccIsdnxSubAutoSpid_Object = MibTableColumn
accIsdnxSubAutoSpid = _AccIsdnxSubAutoSpid_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 19),
    _AccIsdnxSubAutoSpid_Type()
)
accIsdnxSubAutoSpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubAutoSpid.setStatus("mandatory")


class _AccIsdnxSubAutoSwitch_Type(Integer32):
    """Custom type accIsdnxSubAutoSwitch based on Integer32"""
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
        *(("bri-5ess", 4),
          ("bri-dms100", 5),
          ("bri-ni1", 3),
          ("manual", 2),
          ("unknown", 1))
    )


_AccIsdnxSubAutoSwitch_Type.__name__ = "Integer32"
_AccIsdnxSubAutoSwitch_Object = MibTableColumn
accIsdnxSubAutoSwitch = _AccIsdnxSubAutoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 20),
    _AccIsdnxSubAutoSwitch_Type()
)
accIsdnxSubAutoSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxSubAutoSwitch.setStatus("mandatory")
_AccIsdnxStatTable_Object = MibTable
accIsdnxStatTable = _AccIsdnxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7)
)
if mibBuilder.loadTexts:
    accIsdnxStatTable.setStatus("mandatory")
_AccIsdnxStatEntry_Object = MibTableRow
accIsdnxStatEntry = _AccIsdnxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1)
)
accIsdnxStatEntry.setIndexNames(
    (0, "ACC-ISDN", "accIsdnxStatDslIndex"),
)
if mibBuilder.loadTexts:
    accIsdnxStatEntry.setStatus("mandatory")
_AccIsdnxStatDslIndex_Type = Integer32
_AccIsdnxStatDslIndex_Object = MibTableColumn
accIsdnxStatDslIndex = _AccIsdnxStatDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 1),
    _AccIsdnxStatDslIndex_Type()
)
accIsdnxStatDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatDslIndex.setStatus("mandatory")
_AccIsdnxStatHdlcInPackets_Type = Counter32
_AccIsdnxStatHdlcInPackets_Object = MibTableColumn
accIsdnxStatHdlcInPackets = _AccIsdnxStatHdlcInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 2),
    _AccIsdnxStatHdlcInPackets_Type()
)
accIsdnxStatHdlcInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcInPackets.setStatus("mandatory")
_AccIsdnxStatHdlcInOctets_Type = Counter32
_AccIsdnxStatHdlcInOctets_Object = MibTableColumn
accIsdnxStatHdlcInOctets = _AccIsdnxStatHdlcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 3),
    _AccIsdnxStatHdlcInOctets_Type()
)
accIsdnxStatHdlcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcInOctets.setStatus("mandatory")
_AccIsdnxStatHdlcInErrors_Type = Counter32
_AccIsdnxStatHdlcInErrors_Object = MibTableColumn
accIsdnxStatHdlcInErrors = _AccIsdnxStatHdlcInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 4),
    _AccIsdnxStatHdlcInErrors_Type()
)
accIsdnxStatHdlcInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcInErrors.setStatus("mandatory")
_AccIsdnxStatHdlcInDiscards_Type = Counter32
_AccIsdnxStatHdlcInDiscards_Object = MibTableColumn
accIsdnxStatHdlcInDiscards = _AccIsdnxStatHdlcInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 5),
    _AccIsdnxStatHdlcInDiscards_Type()
)
accIsdnxStatHdlcInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcInDiscards.setStatus("mandatory")
_AccIsdnxStatHdlcOutPackets_Type = Counter32
_AccIsdnxStatHdlcOutPackets_Object = MibTableColumn
accIsdnxStatHdlcOutPackets = _AccIsdnxStatHdlcOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 6),
    _AccIsdnxStatHdlcOutPackets_Type()
)
accIsdnxStatHdlcOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcOutPackets.setStatus("mandatory")
_AccIsdnxStatHdlcOutOctets_Type = Counter32
_AccIsdnxStatHdlcOutOctets_Object = MibTableColumn
accIsdnxStatHdlcOutOctets = _AccIsdnxStatHdlcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 7),
    _AccIsdnxStatHdlcOutOctets_Type()
)
accIsdnxStatHdlcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcOutOctets.setStatus("mandatory")
_AccIsdnxStatHdlcOutErrors_Type = Counter32
_AccIsdnxStatHdlcOutErrors_Object = MibTableColumn
accIsdnxStatHdlcOutErrors = _AccIsdnxStatHdlcOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 8),
    _AccIsdnxStatHdlcOutErrors_Type()
)
accIsdnxStatHdlcOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcOutErrors.setStatus("mandatory")
_AccIsdnxStatHdlcOutDiscards_Type = Counter32
_AccIsdnxStatHdlcOutDiscards_Object = MibTableColumn
accIsdnxStatHdlcOutDiscards = _AccIsdnxStatHdlcOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 9),
    _AccIsdnxStatHdlcOutDiscards_Type()
)
accIsdnxStatHdlcOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcOutDiscards.setStatus("mandatory")
_AccIsdnxStatLapdUnsolicResps_Type = Counter32
_AccIsdnxStatLapdUnsolicResps_Object = MibTableColumn
accIsdnxStatLapdUnsolicResps = _AccIsdnxStatLapdUnsolicResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 10),
    _AccIsdnxStatLapdUnsolicResps_Type()
)
accIsdnxStatLapdUnsolicResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdUnsolicResps.setStatus("mandatory")
_AccIsdnxStatLapdPeerSabmes_Type = Counter32
_AccIsdnxStatLapdPeerSabmes_Object = MibTableColumn
accIsdnxStatLapdPeerSabmes = _AccIsdnxStatLapdPeerSabmes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 11),
    _AccIsdnxStatLapdPeerSabmes_Type()
)
accIsdnxStatLapdPeerSabmes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdPeerSabmes.setStatus("mandatory")
_AccIsdnxStatLapdN200Errors_Type = Counter32
_AccIsdnxStatLapdN200Errors_Object = MibTableColumn
accIsdnxStatLapdN200Errors = _AccIsdnxStatLapdN200Errors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 12),
    _AccIsdnxStatLapdN200Errors_Type()
)
accIsdnxStatLapdN200Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdN200Errors.setStatus("mandatory")
_AccIsdnxStatLapdNrSeqErrors_Type = Counter32
_AccIsdnxStatLapdNrSeqErrors_Object = MibTableColumn
accIsdnxStatLapdNrSeqErrors = _AccIsdnxStatLapdNrSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 13),
    _AccIsdnxStatLapdNrSeqErrors_Type()
)
accIsdnxStatLapdNrSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdNrSeqErrors.setStatus("mandatory")
_AccIsdnxStatLapdRecvdFrmrs_Type = Counter32
_AccIsdnxStatLapdRecvdFrmrs_Object = MibTableColumn
accIsdnxStatLapdRecvdFrmrs = _AccIsdnxStatLapdRecvdFrmrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 14),
    _AccIsdnxStatLapdRecvdFrmrs_Type()
)
accIsdnxStatLapdRecvdFrmrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdRecvdFrmrs.setStatus("mandatory")
_AccIsdnxStatLapdCntlErrors_Type = Counter32
_AccIsdnxStatLapdCntlErrors_Object = MibTableColumn
accIsdnxStatLapdCntlErrors = _AccIsdnxStatLapdCntlErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 15),
    _AccIsdnxStatLapdCntlErrors_Type()
)
accIsdnxStatLapdCntlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdCntlErrors.setStatus("mandatory")
_AccIsdnxStatLapdInfoErrors_Type = Counter32
_AccIsdnxStatLapdInfoErrors_Object = MibTableColumn
accIsdnxStatLapdInfoErrors = _AccIsdnxStatLapdInfoErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 16),
    _AccIsdnxStatLapdInfoErrors_Type()
)
accIsdnxStatLapdInfoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdInfoErrors.setStatus("mandatory")
_AccIsdnxStatLapdWrongSizes_Type = Counter32
_AccIsdnxStatLapdWrongSizes_Object = MibTableColumn
accIsdnxStatLapdWrongSizes = _AccIsdnxStatLapdWrongSizes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 17),
    _AccIsdnxStatLapdWrongSizes_Type()
)
accIsdnxStatLapdWrongSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdWrongSizes.setStatus("mandatory")
_AccIsdnxStatLapdN201Errors_Type = Counter32
_AccIsdnxStatLapdN201Errors_Object = MibTableColumn
accIsdnxStatLapdN201Errors = _AccIsdnxStatLapdN201Errors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 18),
    _AccIsdnxStatLapdN201Errors_Type()
)
accIsdnxStatLapdN201Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdN201Errors.setStatus("mandatory")
_AccIsdnxStatCallOriginateds_Type = Counter32
_AccIsdnxStatCallOriginateds_Object = MibTableColumn
accIsdnxStatCallOriginateds = _AccIsdnxStatCallOriginateds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 19),
    _AccIsdnxStatCallOriginateds_Type()
)
accIsdnxStatCallOriginateds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallOriginateds.setStatus("mandatory")
_AccIsdnxStatCallOfferreds_Type = Counter32
_AccIsdnxStatCallOfferreds_Object = MibTableColumn
accIsdnxStatCallOfferreds = _AccIsdnxStatCallOfferreds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 20),
    _AccIsdnxStatCallOfferreds_Type()
)
accIsdnxStatCallOfferreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallOfferreds.setStatus("mandatory")
_AccIsdnxStatCallRouteds_Type = Counter32
_AccIsdnxStatCallRouteds_Object = MibTableColumn
accIsdnxStatCallRouteds = _AccIsdnxStatCallRouteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 21),
    _AccIsdnxStatCallRouteds_Type()
)
accIsdnxStatCallRouteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallRouteds.setStatus("mandatory")
_AccIsdnxStatCallAccepteds_Type = Counter32
_AccIsdnxStatCallAccepteds_Object = MibTableColumn
accIsdnxStatCallAccepteds = _AccIsdnxStatCallAccepteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 22),
    _AccIsdnxStatCallAccepteds_Type()
)
accIsdnxStatCallAccepteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallAccepteds.setStatus("mandatory")
_AccIsdnxStatCallCompleteds_Type = Counter32
_AccIsdnxStatCallCompleteds_Object = MibTableColumn
accIsdnxStatCallCompleteds = _AccIsdnxStatCallCompleteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 23),
    _AccIsdnxStatCallCompleteds_Type()
)
accIsdnxStatCallCompleteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallCompleteds.setStatus("mandatory")
_AccIsdnxStatCallCleareds_Type = Counter32
_AccIsdnxStatCallCleareds_Object = MibTableColumn
accIsdnxStatCallCleareds = _AccIsdnxStatCallCleareds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 24),
    _AccIsdnxStatCallCleareds_Type()
)
accIsdnxStatCallCleareds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallCleareds.setStatus("mandatory")
_AccIsdnxCallTable_Object = MibTable
accIsdnxCallTable = _AccIsdnxCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8)
)
if mibBuilder.loadTexts:
    accIsdnxCallTable.setStatus("mandatory")
_AccIsdnxCallEntry_Object = MibTableRow
accIsdnxCallEntry = _AccIsdnxCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1)
)
accIsdnxCallEntry.setIndexNames(
    (0, "ACC-ISDN", "accIsdnxCallDslIndex"),
    (0, "ACC-ISDN", "accIsdnxCallReference"),
    (0, "ACC-ISDN", "accIsdnxCallOrigin"),
)
if mibBuilder.loadTexts:
    accIsdnxCallEntry.setStatus("mandatory")
_AccIsdnxCallDslIndex_Type = Integer32
_AccIsdnxCallDslIndex_Object = MibTableColumn
accIsdnxCallDslIndex = _AccIsdnxCallDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 1),
    _AccIsdnxCallDslIndex_Type()
)
accIsdnxCallDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallDslIndex.setStatus("mandatory")


class _AccIsdnxCallReference_Type(Integer32):
    """Custom type accIsdnxCallReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AccIsdnxCallReference_Type.__name__ = "Integer32"
_AccIsdnxCallReference_Object = MibTableColumn
accIsdnxCallReference = _AccIsdnxCallReference_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 2),
    _AccIsdnxCallReference_Type()
)
accIsdnxCallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallReference.setStatus("mandatory")


class _AccIsdnxCallOrigin_Type(Integer32):
    """Custom type accIsdnxCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network", 3),
          ("none", 1),
          ("terminal", 2))
    )


_AccIsdnxCallOrigin_Type.__name__ = "Integer32"
_AccIsdnxCallOrigin_Object = MibTableColumn
accIsdnxCallOrigin = _AccIsdnxCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 3),
    _AccIsdnxCallOrigin_Type()
)
accIsdnxCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallOrigin.setStatus("mandatory")
_AccIsdnxCallCircuitIndex_Type = Integer32
_AccIsdnxCallCircuitIndex_Object = MibTableColumn
accIsdnxCallCircuitIndex = _AccIsdnxCallCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 4),
    _AccIsdnxCallCircuitIndex_Type()
)
accIsdnxCallCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallCircuitIndex.setStatus("mandatory")


class _AccIsdnxCallInfoRate_Type(Integer32):
    """Custom type accIsdnxCallInfoRate based on Integer32"""
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
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("info-rate-10x64k", 10),
          ("info-rate-11x64k", 11),
          ("info-rate-12x64k", 12),
          ("info-rate-13x64k", 13),
          ("info-rate-14x64k", 14),
          ("info-rate-15x64k", 15),
          ("info-rate-16x64k", 16),
          ("info-rate-17x64k", 17),
          ("info-rate-18x64k", 18),
          ("info-rate-19x64k", 19),
          ("info-rate-1x64k", 1),
          ("info-rate-20x64k", 20),
          ("info-rate-21x64k", 21),
          ("info-rate-22x64k", 22),
          ("info-rate-23x64k", 23),
          ("info-rate-24x64k", 24),
          ("info-rate-25x64k", 25),
          ("info-rate-26x64k", 26),
          ("info-rate-27x64k", 27),
          ("info-rate-28x64k", 28),
          ("info-rate-29x64k", 29),
          ("info-rate-2x64k", 2),
          ("info-rate-30x64k", 30),
          ("info-rate-31x64k", 31),
          ("info-rate-3x64k", 3),
          ("info-rate-4x64k", 4),
          ("info-rate-5x64k", 5),
          ("info-rate-6x64k", 6),
          ("info-rate-7x64k", 7),
          ("info-rate-8x64k", 8),
          ("info-rate-9x64k", 9),
          ("packet", 32))
    )


_AccIsdnxCallInfoRate_Type.__name__ = "Integer32"
_AccIsdnxCallInfoRate_Object = MibTableColumn
accIsdnxCallInfoRate = _AccIsdnxCallInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 5),
    _AccIsdnxCallInfoRate_Type()
)
accIsdnxCallInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallInfoRate.setStatus("mandatory")


class _AccIsdnxCallState_Type(Integer32):
    """Custom type accIsdnxCallState based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("connecting", 8),
          ("delivered", 5),
          ("discon-ind", 12),
          ("discon-req", 11),
          ("idle", 1),
          ("incoming", 9),
          ("initiated", 2),
          ("outgoing", 4),
          ("overlap-recv", 16),
          ("overlap-send", 3),
          ("present", 6),
          ("received", 7),
          ("release", 15),
          ("resume", 14),
          ("suspend", 13))
    )


_AccIsdnxCallState_Type.__name__ = "Integer32"
_AccIsdnxCallState_Object = MibTableColumn
accIsdnxCallState = _AccIsdnxCallState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 6),
    _AccIsdnxCallState_Type()
)
accIsdnxCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallState.setStatus("mandatory")


class _AccIsdnxCallCause_Type(Integer32):
    """Custom type accIsdnxCallCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnxCallCause_Type.__name__ = "Integer32"
_AccIsdnxCallCause_Object = MibTableColumn
accIsdnxCallCause = _AccIsdnxCallCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 7),
    _AccIsdnxCallCause_Type()
)
accIsdnxCallCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallCause.setStatus("mandatory")
_AccIsdnxCallAddress_Type = OctetString
_AccIsdnxCallAddress_Object = MibTableColumn
accIsdnxCallAddress = _AccIsdnxCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 8),
    _AccIsdnxCallAddress_Type()
)
accIsdnxCallAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallAddress.setStatus("mandatory")


class _AccIsdnxCallInfoType_Type(Integer32):
    """Custom type accIsdnxCallInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("info-type-cm56", 2),
          ("info-type-cmd", 1),
          ("info-type-cmv", 3))
    )


_AccIsdnxCallInfoType_Type.__name__ = "Integer32"
_AccIsdnxCallInfoType_Object = MibTableColumn
accIsdnxCallInfoType = _AccIsdnxCallInfoType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 9),
    _AccIsdnxCallInfoType_Type()
)
accIsdnxCallInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallInfoType.setStatus("mandatory")
_AccIsdnxCallSlotMap_Type = Integer32
_AccIsdnxCallSlotMap_Object = MibTableColumn
accIsdnxCallSlotMap = _AccIsdnxCallSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 10),
    _AccIsdnxCallSlotMap_Type()
)
accIsdnxCallSlotMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallSlotMap.setStatus("mandatory")
_AccIsdnSpidTable_Object = MibTable
accIsdnSpidTable = _AccIsdnSpidTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 9)
)
if mibBuilder.loadTexts:
    accIsdnSpidTable.setStatus("mandatory")
_AccIsdnSpidEntry_Object = MibTableRow
accIsdnSpidEntry = _AccIsdnSpidEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 9, 1)
)
accIsdnSpidEntry.setIndexNames(
    (0, "ACC-ISDN", "accIsdnSpidIndex"),
)
if mibBuilder.loadTexts:
    accIsdnSpidEntry.setStatus("mandatory")
_AccIsdnSpidIndex_Type = Integer32
_AccIsdnSpidIndex_Object = MibTableColumn
accIsdnSpidIndex = _AccIsdnSpidIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 9, 1, 1),
    _AccIsdnSpidIndex_Type()
)
accIsdnSpidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnSpidIndex.setStatus("mandatory")
_AccIsdnSpidValue_Type = DisplayString
_AccIsdnSpidValue_Object = MibTableColumn
accIsdnSpidValue = _AccIsdnSpidValue_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 9, 1, 2),
    _AccIsdnSpidValue_Type()
)
accIsdnSpidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSpidValue.setStatus("mandatory")
_AccIsdnTerm_ObjectIdentity = ObjectIdentity
accIsdnTerm = _AccIsdnTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 10)
)


class _AccIsdnxTermination_Type(Integer32):
    """Custom type accIsdnxTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccIsdnxTermination_Type.__name__ = "Integer32"
_AccIsdnxTermination_Object = MibScalar
accIsdnxTermination = _AccIsdnxTermination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 10, 1),
    _AccIsdnxTermination_Type()
)
accIsdnxTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxTermination.setStatus("mandatory")
_AccIsdnxCurrCalls_Type = Integer32
_AccIsdnxCurrCalls_Object = MibScalar
accIsdnxCurrCalls = _AccIsdnxCurrCalls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 11),
    _AccIsdnxCurrCalls_Type()
)
accIsdnxCurrCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCurrCalls.setStatus("mandatory")
_AccIsdnTraps_ObjectIdentity = ObjectIdentity
accIsdnTraps = _AccIsdnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12)
)
_AccIsdnTrapMsg_Type = DisplayString
_AccIsdnTrapMsg_Object = MibScalar
accIsdnTrapMsg = _AccIsdnTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 1),
    _AccIsdnTrapMsg_Type()
)
accIsdnTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accIsdnOutGoingCallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 1)
)
accIsdnOutGoingCallTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnOutGoingCallTrap.setStatus(
        ""
    )

accIsdnCallResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 2)
)
accIsdnCallResetTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnCallResetTrap.setStatus(
        ""
    )

accIsdnConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 3)
)
accIsdnConnectTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnConnectTrap.setStatus(
        ""
    )

accIsdnStaleDialCntxtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 4)
)
accIsdnStaleDialCntxtTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnStaleDialCntxtTrap.setStatus(
        ""
    )

accIsdnIncomingCallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 5)
)
accIsdnIncomingCallTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnIncomingCallTrap.setStatus(
        ""
    )

accIsdnCallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 6)
)
accIsdnCallTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnCallTrap.setStatus(
        ""
    )

accIsdnApplTmrExpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 7)
)
accIsdnApplTmrExpTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnApplTmrExpTrap.setStatus(
        ""
    )

accIsdnApplTmrExpInClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 8)
)
accIsdnApplTmrExpInClearTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnApplTmrExpInClearTrap.setStatus(
        ""
    )

accIsdnChannelRestrtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 9)
)
accIsdnChannelRestrtTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnChannelRestrtTrap.setStatus(
        ""
    )

accIsdnDataLnkRelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 10)
)
accIsdnDataLnkRelTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnDataLnkRelTrap.setStatus(
        ""
    )

accIsdnDataLnkEstTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 11)
)
accIsdnDataLnkEstTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeverityType"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnDataLnkEstTrap.setStatus(
        ""
    )

accIsdnConfigStackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 12)
)
accIsdnConfigStackTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnConfigStackTrap.setStatus(
        ""
    )

accIsdnSubscriberLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 13)
)
accIsdnSubscriberLoopTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnSubscriberLoopTrap.setStatus(
        ""
    )

accIsdnRegisterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 14)
)
accIsdnRegisterTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnRegisterTrap.setStatus(
        ""
    )

accIsdnTrmnlRegErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 15)
)
accIsdnTrmnlRegErrTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnTrmnlRegErrTrap.setStatus(
        ""
    )

accIsdnTrmnlRegTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 16)
)
accIsdnTrmnlRegTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnTrmnlRegTrap.setStatus(
        ""
    )

accIsdnAwaitDatalnkEstTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 17)
)
accIsdnAwaitDatalnkEstTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnAwaitDatalnkEstTrap.setStatus(
        ""
    )

accIsdnDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 18)
)
accIsdnDisconnectTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnDisconnectTrap.setStatus(
        ""
    )

accIsdnOutGoingCallFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 19)
)
accIsdnOutGoingCallFailTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnOutGoingCallFailTrap.setStatus(
        ""
    )

accIsdnTrap20 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 20)
)
accIsdnTrap20.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnTrap20.setStatus(
        ""
    )

accIsdnModuleErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 21)
)
accIsdnModuleErrTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnModuleErrTrap.setStatus(
        ""
    )

accIsdnTrap22 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 22)
)
accIsdnTrap22.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnTrap22.setStatus(
        ""
    )

accIsdnNfasIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 23)
)
accIsdnNfasIntfTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnNfasIntfTrap.setStatus(
        ""
    )

accIsdnNoSpidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 24)
)
accIsdnNoSpidTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnNoSpidTrap.setStatus(
        ""
    )

accIsdnSpidConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 25)
)
accIsdnSpidConflictTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnSpidConflictTrap.setStatus(
        ""
    )

accIsdnInvSpidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 26)
)
accIsdnInvSpidTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnInvSpidTrap.setStatus(
        ""
    )

accIsdnSwBldTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 27)
)
accIsdnSwBldTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnSwBldTrap.setStatus(
        ""
    )

accIsdnParametersTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 28)
)
accIsdnParametersTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnParametersTrap.setStatus(
        ""
    )

accIsdnSwitchTypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 29)
)
accIsdnSwitchTypeTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnSwitchTypeTrap.setStatus(
        ""
    )

accIsdnManyIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 30)
)
accIsdnManyIntfTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnManyIntfTrap.setStatus(
        ""
    )

accIsdnPriGroupRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 31)
)
accIsdnPriGroupRangeTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnPriGroupRangeTrap.setStatus(
        ""
    )

accIsdnNfasIntfPriTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 32)
)
accIsdnNfasIntfPriTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnNfasIntfPriTrap.setStatus(
        ""
    )

accIsdnManyNFASIntfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 33)
)
accIsdnManyNFASIntfTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnManyNFASIntfTrap.setStatus(
        ""
    )

accIsdnPriGroupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 34)
)
accIsdnPriGroupTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnPriGroupTrap.setStatus(
        ""
    )

accIsdnTrap35 = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 35)
)
accIsdnTrap35.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnTrap35.setStatus(
        ""
    )

accIsdnNoSrvcProIFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 36)
)
accIsdnNoSrvcProIFTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnNoSrvcProIFTrap.setStatus(
        ""
    )

accIsdnNTBldIncmptblHWTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 37)
)
accIsdnNTBldIncmptblHWTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnNTBldIncmptblHWTrap.setStatus(
        ""
    )

accIsdnRcvdSpidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 38)
)
accIsdnRcvdSpidTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-ISDN", "accIsdnSpidValue"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnRcvdSpidTrap.setStatus(
        ""
    )

accIsdnRcvdSpidsNWTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 39)
)
accIsdnRcvdSpidsNWTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-ISDN", "accIsdnSpidValue"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnRcvdSpidsNWTrap.setStatus(
        ""
    )

accIsdnAutoSpidFldTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 40)
)
accIsdnAutoSpidFldTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnAutoSpidFldTrap.setStatus(
        ""
    )

accIsdnAutoSpidSccdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 41)
)
accIsdnAutoSpidSccdTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnAutoSpidSccdTrap.setStatus(
        ""
    )

accIsdnAutoSpidFld1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 42)
)
accIsdnAutoSpidFld1Trap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnAutoSpidFld1Trap.setStatus(
        ""
    )

accIsdnAutoSwtchSccdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 43)
)
accIsdnAutoSwtchSccdTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnAutoSwtchSccdTrap.setStatus(
        ""
    )

accIsdnAutoSwtchFldTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 44)
)
accIsdnAutoSwtchFldTrap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnAutoSwtchFldTrap.setStatus(
        ""
    )

accIsdnAutoSwtchFld1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 12, 0, 45)
)
accIsdnAutoSwtchFld1Trap.setObjects(
      *(("ACC-ISDN", "accIsdnTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIsdnAutoSwtchFld1Trap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-ISDN",
    **{"accIsdn": accIsdn,
       "accIsdnDsl": accIsdnDsl,
       "accIsdnDslIndex": accIsdnDslIndex,
       "accIsdnSubTable": accIsdnSubTable,
       "accIsdnSubEntry": accIsdnSubEntry,
       "accIsdnSubSwitchType": accIsdnSubSwitchType,
       "accIsdnSubChannelMode": accIsdnSubChannelMode,
       "accIsdnSubAdminStatus": accIsdnSubAdminStatus,
       "accIsdnSubDiagLevel": accIsdnSubDiagLevel,
       "accIsdnSubManualTei": accIsdnSubManualTei,
       "accIsdnStatTable": accIsdnStatTable,
       "accIsdnStatEntry": accIsdnStatEntry,
       "accIsdnStatHdlcInPackets": accIsdnStatHdlcInPackets,
       "accIsdnStatHdlcInOctets": accIsdnStatHdlcInOctets,
       "accIsdnStatHdlcInErrors": accIsdnStatHdlcInErrors,
       "accIsdnStatHdlcInDiscs": accIsdnStatHdlcInDiscs,
       "accIsdnStatHdlcOutPackets": accIsdnStatHdlcOutPackets,
       "accIsdnStatHdlcOutOctets": accIsdnStatHdlcOutOctets,
       "accIsdnStatHdlcOutErrors": accIsdnStatHdlcOutErrors,
       "accIsdnStatHdlcOutDiscs": accIsdnStatHdlcOutDiscs,
       "accIsdnStatLapdUnsolicResps": accIsdnStatLapdUnsolicResps,
       "accIsdnStatLapdPeerSabmes": accIsdnStatLapdPeerSabmes,
       "accIsdnStatLapdN200Errors": accIsdnStatLapdN200Errors,
       "accIsdnStatLapdNrSeqErrors": accIsdnStatLapdNrSeqErrors,
       "accIsdnStatLapdRecvdFrmrs": accIsdnStatLapdRecvdFrmrs,
       "accIsdnStatLapdCntlErrors": accIsdnStatLapdCntlErrors,
       "accIsdnStatLapdInfoErrors": accIsdnStatLapdInfoErrors,
       "accIsdnStatLapdWrongSizes": accIsdnStatLapdWrongSizes,
       "accIsdnStatLapdN201Errors": accIsdnStatLapdN201Errors,
       "accIsdnStatCallsOriginateds": accIsdnStatCallsOriginateds,
       "accIsdnStatCallsOfferreds": accIsdnStatCallsOfferreds,
       "accIsdnStatCallsAnswereds": accIsdnStatCallsAnswereds,
       "accIsdnStatCallsAccepteds": accIsdnStatCallsAccepteds,
       "accIsdnStatCallsCompleteds": accIsdnStatCallsCompleteds,
       "accIsdnStatCallsCleareds": accIsdnStatCallsCleareds,
       "accIsdnStatDslOperStatus": accIsdnStatDslOperStatus,
       "accIsdnStatLastCauses": accIsdnStatLastCauses,
       "accIsdnCallTable": accIsdnCallTable,
       "accIsdnCallEntry": accIsdnCallEntry,
       "accIsdnCallIdentifier": accIsdnCallIdentifier,
       "accIsdnCallReference": accIsdnCallReference,
       "accIsdnCallChannelId": accIsdnCallChannelId,
       "accIsdnCallIfIndex": accIsdnCallIfIndex,
       "accIsdnCallInfoRate": accIsdnCallInfoRate,
       "accIsdnCallState": accIsdnCallState,
       "accIsdnCallCause": accIsdnCallCause,
       "accIsdnCallOrigin": accIsdnCallOrigin,
       "accIsdnCallAddress": accIsdnCallAddress,
       "accIsdnCallDslIndex": accIsdnCallDslIndex,
       "accIsdnTest": accIsdnTest,
       "accIsdnTestIfIndex": accIsdnTestIfIndex,
       "accIsdnTestAddress": accIsdnTestAddress,
       "accIsdnTestCommand": accIsdnTestCommand,
       "accIsdnTestRouting": accIsdnTestRouting,
       "accIsdnTestRegName": accIsdnTestRegName,
       "accIsdnTestRegValue": accIsdnTestRegValue,
       "accwIsdnTestBChanMode": accwIsdnTestBChanMode,
       "accwIsdnTestOptions": accwIsdnTestOptions,
       "accIsdnxSubTable": accIsdnxSubTable,
       "accIsdnxSubEntry": accIsdnxSubEntry,
       "accIsdnxSubDslIndex": accIsdnxSubDslIndex,
       "accIsdnxSubSwitchType": accIsdnxSubSwitchType,
       "accIsdnxSubChanConfig": accIsdnxSubChanConfig,
       "accIsdnxSubAdminStatus": accIsdnxSubAdminStatus,
       "accIsdnxSubDiagLevel": accIsdnxSubDiagLevel,
       "accIsdnxSubManualTei": accIsdnxSubManualTei,
       "accIsdnxSubOperStatus": accIsdnxSubOperStatus,
       "accIsdnxSubNumNfas": accIsdnxSubNumNfas,
       "accIsdnxSubLastCause": accIsdnxSubLastCause,
       "accIsdnxSubSubaddrType": accIsdnxSubSubaddrType,
       "accIsdnxSubVoiceOption": accIsdnxSubVoiceOption,
       "accIsdnxSubCliOption": accIsdnxSubCliOption,
       "accIsdnxSubEncodingMethod": accIsdnxSubEncodingMethod,
       "accIsdnxSubDialingMethod": accIsdnxSubDialingMethod,
       "accIsdnxSubAutoSpid": accIsdnxSubAutoSpid,
       "accIsdnxSubAutoSwitch": accIsdnxSubAutoSwitch,
       "accIsdnxStatTable": accIsdnxStatTable,
       "accIsdnxStatEntry": accIsdnxStatEntry,
       "accIsdnxStatDslIndex": accIsdnxStatDslIndex,
       "accIsdnxStatHdlcInPackets": accIsdnxStatHdlcInPackets,
       "accIsdnxStatHdlcInOctets": accIsdnxStatHdlcInOctets,
       "accIsdnxStatHdlcInErrors": accIsdnxStatHdlcInErrors,
       "accIsdnxStatHdlcInDiscards": accIsdnxStatHdlcInDiscards,
       "accIsdnxStatHdlcOutPackets": accIsdnxStatHdlcOutPackets,
       "accIsdnxStatHdlcOutOctets": accIsdnxStatHdlcOutOctets,
       "accIsdnxStatHdlcOutErrors": accIsdnxStatHdlcOutErrors,
       "accIsdnxStatHdlcOutDiscards": accIsdnxStatHdlcOutDiscards,
       "accIsdnxStatLapdUnsolicResps": accIsdnxStatLapdUnsolicResps,
       "accIsdnxStatLapdPeerSabmes": accIsdnxStatLapdPeerSabmes,
       "accIsdnxStatLapdN200Errors": accIsdnxStatLapdN200Errors,
       "accIsdnxStatLapdNrSeqErrors": accIsdnxStatLapdNrSeqErrors,
       "accIsdnxStatLapdRecvdFrmrs": accIsdnxStatLapdRecvdFrmrs,
       "accIsdnxStatLapdCntlErrors": accIsdnxStatLapdCntlErrors,
       "accIsdnxStatLapdInfoErrors": accIsdnxStatLapdInfoErrors,
       "accIsdnxStatLapdWrongSizes": accIsdnxStatLapdWrongSizes,
       "accIsdnxStatLapdN201Errors": accIsdnxStatLapdN201Errors,
       "accIsdnxStatCallOriginateds": accIsdnxStatCallOriginateds,
       "accIsdnxStatCallOfferreds": accIsdnxStatCallOfferreds,
       "accIsdnxStatCallRouteds": accIsdnxStatCallRouteds,
       "accIsdnxStatCallAccepteds": accIsdnxStatCallAccepteds,
       "accIsdnxStatCallCompleteds": accIsdnxStatCallCompleteds,
       "accIsdnxStatCallCleareds": accIsdnxStatCallCleareds,
       "accIsdnxCallTable": accIsdnxCallTable,
       "accIsdnxCallEntry": accIsdnxCallEntry,
       "accIsdnxCallDslIndex": accIsdnxCallDslIndex,
       "accIsdnxCallReference": accIsdnxCallReference,
       "accIsdnxCallOrigin": accIsdnxCallOrigin,
       "accIsdnxCallCircuitIndex": accIsdnxCallCircuitIndex,
       "accIsdnxCallInfoRate": accIsdnxCallInfoRate,
       "accIsdnxCallState": accIsdnxCallState,
       "accIsdnxCallCause": accIsdnxCallCause,
       "accIsdnxCallAddress": accIsdnxCallAddress,
       "accIsdnxCallInfoType": accIsdnxCallInfoType,
       "accIsdnxCallSlotMap": accIsdnxCallSlotMap,
       "accIsdnSpidTable": accIsdnSpidTable,
       "accIsdnSpidEntry": accIsdnSpidEntry,
       "accIsdnSpidIndex": accIsdnSpidIndex,
       "accIsdnSpidValue": accIsdnSpidValue,
       "accIsdnTerm": accIsdnTerm,
       "accIsdnxTermination": accIsdnxTermination,
       "accIsdnxCurrCalls": accIsdnxCurrCalls,
       "accIsdnTraps": accIsdnTraps,
       "accIsdnOutGoingCallTrap": accIsdnOutGoingCallTrap,
       "accIsdnCallResetTrap": accIsdnCallResetTrap,
       "accIsdnConnectTrap": accIsdnConnectTrap,
       "accIsdnStaleDialCntxtTrap": accIsdnStaleDialCntxtTrap,
       "accIsdnIncomingCallTrap": accIsdnIncomingCallTrap,
       "accIsdnCallTrap": accIsdnCallTrap,
       "accIsdnApplTmrExpTrap": accIsdnApplTmrExpTrap,
       "accIsdnApplTmrExpInClearTrap": accIsdnApplTmrExpInClearTrap,
       "accIsdnChannelRestrtTrap": accIsdnChannelRestrtTrap,
       "accIsdnDataLnkRelTrap": accIsdnDataLnkRelTrap,
       "accIsdnDataLnkEstTrap": accIsdnDataLnkEstTrap,
       "accIsdnConfigStackTrap": accIsdnConfigStackTrap,
       "accIsdnSubscriberLoopTrap": accIsdnSubscriberLoopTrap,
       "accIsdnRegisterTrap": accIsdnRegisterTrap,
       "accIsdnTrmnlRegErrTrap": accIsdnTrmnlRegErrTrap,
       "accIsdnTrmnlRegTrap": accIsdnTrmnlRegTrap,
       "accIsdnAwaitDatalnkEstTrap": accIsdnAwaitDatalnkEstTrap,
       "accIsdnDisconnectTrap": accIsdnDisconnectTrap,
       "accIsdnOutGoingCallFailTrap": accIsdnOutGoingCallFailTrap,
       "accIsdnTrap20": accIsdnTrap20,
       "accIsdnModuleErrTrap": accIsdnModuleErrTrap,
       "accIsdnTrap22": accIsdnTrap22,
       "accIsdnNfasIntfTrap": accIsdnNfasIntfTrap,
       "accIsdnNoSpidTrap": accIsdnNoSpidTrap,
       "accIsdnSpidConflictTrap": accIsdnSpidConflictTrap,
       "accIsdnInvSpidTrap": accIsdnInvSpidTrap,
       "accIsdnSwBldTrap": accIsdnSwBldTrap,
       "accIsdnParametersTrap": accIsdnParametersTrap,
       "accIsdnSwitchTypeTrap": accIsdnSwitchTypeTrap,
       "accIsdnManyIntfTrap": accIsdnManyIntfTrap,
       "accIsdnPriGroupRangeTrap": accIsdnPriGroupRangeTrap,
       "accIsdnNfasIntfPriTrap": accIsdnNfasIntfPriTrap,
       "accIsdnManyNFASIntfTrap": accIsdnManyNFASIntfTrap,
       "accIsdnPriGroupTrap": accIsdnPriGroupTrap,
       "accIsdnTrap35": accIsdnTrap35,
       "accIsdnNoSrvcProIFTrap": accIsdnNoSrvcProIFTrap,
       "accIsdnNTBldIncmptblHWTrap": accIsdnNTBldIncmptblHWTrap,
       "accIsdnRcvdSpidTrap": accIsdnRcvdSpidTrap,
       "accIsdnRcvdSpidsNWTrap": accIsdnRcvdSpidsNWTrap,
       "accIsdnAutoSpidFldTrap": accIsdnAutoSpidFldTrap,
       "accIsdnAutoSpidSccdTrap": accIsdnAutoSpidSccdTrap,
       "accIsdnAutoSpidFld1Trap": accIsdnAutoSpidFld1Trap,
       "accIsdnAutoSwtchSccdTrap": accIsdnAutoSwtchSccdTrap,
       "accIsdnAutoSwtchFldTrap": accIsdnAutoSwtchFldTrap,
       "accIsdnAutoSwtchFld1Trap": accIsdnAutoSwtchFld1Trap,
       "accIsdnTrapMsg": accIsdnTrapMsg}
)
