# SNMP MIB module (CISCO-ATM-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:06 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(BulkConfigResult,
 ConfigIterator) = mibBuilder.importSymbols(
    "CISCO-TC",
    "BulkConfigResult",
    "ConfigIterator")

(CiscoAal2ProfileNumber,
 CiscoAal2ProfileType) = mibBuilder.importSymbols(
    "CISCO-VOICE-AALX-PROFILE-MIB",
    "CiscoAal2ProfileNumber",
    "CiscoAal2ProfileType")

(CvcCoderTypeRate,
 CvcSpeechCoderRate) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcCoderTypeRate",
    "CvcSpeechCoderRate")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoAtmTrunkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351)
)
ciscoAtmTrunkMIB.setRevisions(
        ("2003-07-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Counter32SinceReset(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CAtmTrunkMIBNotifications_ObjectIdentity = ObjectIdentity
cAtmTrunkMIBNotifications = _CAtmTrunkMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 0)
)
_CAtmTrunkMIBObjects_ObjectIdentity = ObjectIdentity
cAtmTrunkMIBObjects = _CAtmTrunkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1)
)
_CAtmTrunkCidConfig_ObjectIdentity = ObjectIdentity
cAtmTrunkCidConfig = _CAtmTrunkCidConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1)
)
_CatmtCidTable_Object = MibTable
catmtCidTable = _CatmtCidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1)
)
if mibBuilder.loadTexts:
    catmtCidTable.setStatus("current")
_CatmtCidEntry_Object = MibTableRow
catmtCidEntry = _CatmtCidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1)
)
catmtCidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtCidVpi"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtCidVci"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtCid"),
)
if mibBuilder.loadTexts:
    catmtCidEntry.setStatus("current")


class _CatmtCidVpi_Type(Unsigned32):
    """Custom type catmtCidVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CatmtCidVpi_Type.__name__ = "Unsigned32"
_CatmtCidVpi_Object = MibTableColumn
catmtCidVpi = _CatmtCidVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 1),
    _CatmtCidVpi_Type()
)
catmtCidVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catmtCidVpi.setStatus("current")


class _CatmtCidVci_Type(Unsigned32):
    """Custom type catmtCidVci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CatmtCidVci_Type.__name__ = "Unsigned32"
_CatmtCidVci_Object = MibTableColumn
catmtCidVci = _CatmtCidVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 2),
    _CatmtCidVci_Type()
)
catmtCidVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catmtCidVci.setStatus("current")


class _CatmtCid_Type(Integer32):
    """Custom type catmtCid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 255),
    )


_CatmtCid_Type.__name__ = "Integer32"
_CatmtCid_Object = MibTableColumn
catmtCid = _CatmtCid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 3),
    _CatmtCid_Type()
)
catmtCid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catmtCid.setStatus("current")
_CatmtCidDs1_Type = InterfaceIndex
_CatmtCidDs1_Object = MibTableColumn
catmtCidDs1 = _CatmtCidDs1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 4),
    _CatmtCidDs1_Type()
)
catmtCidDs1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidDs1.setStatus("current")


class _CatmtCidDs0GroupIndex_Type(Integer32):
    """Custom type catmtCidDs0GroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CatmtCidDs0GroupIndex_Type.__name__ = "Integer32"
_CatmtCidDs0GroupIndex_Object = MibTableColumn
catmtCidDs0GroupIndex = _CatmtCidDs0GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 5),
    _CatmtCidDs0GroupIndex_Type()
)
catmtCidDs0GroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidDs0GroupIndex.setStatus("current")
_CatmtCidProfileType_Type = CiscoAal2ProfileType
_CatmtCidProfileType_Object = MibTableColumn
catmtCidProfileType = _CatmtCidProfileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 6),
    _CatmtCidProfileType_Type()
)
catmtCidProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidProfileType.setStatus("current")
_CatmtCidProfileNumber_Type = CiscoAal2ProfileNumber
_CatmtCidProfileNumber_Object = MibTableColumn
catmtCidProfileNumber = _CatmtCidProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 7),
    _CatmtCidProfileNumber_Type()
)
catmtCidProfileNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidProfileNumber.setStatus("current")
_CatmtCidVoiceCodec_Type = CvcSpeechCoderRate
_CatmtCidVoiceCodec_Object = MibTableColumn
catmtCidVoiceCodec = _CatmtCidVoiceCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 8),
    _CatmtCidVoiceCodec_Type()
)
catmtCidVoiceCodec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidVoiceCodec.setStatus("current")
_CatmtCidVBDCodec_Type = CvcCoderTypeRate
_CatmtCidVBDCodec_Object = MibTableColumn
catmtCidVBDCodec = _CatmtCidVBDCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 9),
    _CatmtCidVBDCodec_Type()
)
catmtCidVBDCodec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidVBDCodec.setStatus("current")


class _CatmtCidNx64Enable_Type(TruthValue):
    """Custom type catmtCidNx64Enable based on TruthValue"""


_CatmtCidNx64Enable_Object = MibTableColumn
catmtCidNx64Enable = _CatmtCidNx64Enable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 10),
    _CatmtCidNx64Enable_Type()
)
catmtCidNx64Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidNx64Enable.setStatus("current")


class _CatmtCidNx64Profile_Type(Integer32):
    """Custom type catmtCidNx64Profile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CatmtCidNx64Profile_Type.__name__ = "Integer32"
_CatmtCidNx64Profile_Object = MibTableColumn
catmtCidNx64Profile = _CatmtCidNx64Profile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 11),
    _CatmtCidNx64Profile_Type()
)
catmtCidNx64Profile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidNx64Profile.setStatus("current")


class _CatmtCidStateBitMap_Type(Bits):
    """Custom type catmtCidStateBitMap based on Bits"""
    namedValues = NamedValues(
        *(("aal2ConnAIS", 4),
          ("aal2ConnRDI", 5),
          ("extAIS", 2),
          ("extRAI", 3),
          ("lineAlarm", 6),
          ("pvcAdminDown", 0),
          ("pvcFailure", 1))
    )

_CatmtCidStateBitMap_Type.__name__ = "Bits"
_CatmtCidStateBitMap_Object = MibTableColumn
catmtCidStateBitMap = _CatmtCidStateBitMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 12),
    _CatmtCidStateBitMap_Type()
)
catmtCidStateBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidStateBitMap.setStatus("current")


class _CatmtCidRepetition_Type(ConfigIterator):
    """Custom type catmtCidRepetition based on ConfigIterator"""
    defaultValue = 1


_CatmtCidRepetition_Object = MibTableColumn
catmtCidRepetition = _CatmtCidRepetition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 13),
    _CatmtCidRepetition_Type()
)
catmtCidRepetition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidRepetition.setStatus("current")
_CatmtCidRepetitionOwner_Type = OwnerString
_CatmtCidRepetitionOwner_Object = MibTableColumn
catmtCidRepetitionOwner = _CatmtCidRepetitionOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 14),
    _CatmtCidRepetitionOwner_Type()
)
catmtCidRepetitionOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidRepetitionOwner.setStatus("current")
_CatmtCidRepetitionResult_Type = BulkConfigResult
_CatmtCidRepetitionResult_Object = MibTableColumn
catmtCidRepetitionResult = _CatmtCidRepetitionResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 15),
    _CatmtCidRepetitionResult_Type()
)
catmtCidRepetitionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidRepetitionResult.setStatus("current")
_CatmtCidRowStatus_Type = RowStatus
_CatmtCidRowStatus_Object = MibTableColumn
catmtCidRowStatus = _CatmtCidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 1, 1, 1, 16),
    _CatmtCidRowStatus_Type()
)
catmtCidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtCidRowStatus.setStatus("current")
_CAtmTrunkCidConnStats_ObjectIdentity = ObjectIdentity
cAtmTrunkCidConnStats = _CAtmTrunkCidConnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2)
)
_CatmtCidStatsTable_Object = MibTable
catmtCidStatsTable = _CatmtCidStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1)
)
if mibBuilder.loadTexts:
    catmtCidStatsTable.setStatus("current")
_CatmtCidStatsEntry_Object = MibTableRow
catmtCidStatsEntry = _CatmtCidStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1)
)
catmtCidStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtCidVpi"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtCidVci"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtCid"),
)
if mibBuilder.loadTexts:
    catmtCidStatsEntry.setStatus("current")
_CatmtCidSentPackets_Type = Counter32SinceReset
_CatmtCidSentPackets_Object = MibTableColumn
catmtCidSentPackets = _CatmtCidSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 1),
    _CatmtCidSentPackets_Type()
)
catmtCidSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    catmtCidSentPackets.setUnits("packets")
_CatmtCidRcvdPackets_Type = Counter32SinceReset
_CatmtCidRcvdPackets_Object = MibTableColumn
catmtCidRcvdPackets = _CatmtCidRcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 2),
    _CatmtCidRcvdPackets_Type()
)
catmtCidRcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidRcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    catmtCidRcvdPackets.setUnits("packets")
_CatmtCidSentOctets_Type = Counter32SinceReset
_CatmtCidSentOctets_Object = MibTableColumn
catmtCidSentOctets = _CatmtCidSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 3),
    _CatmtCidSentOctets_Type()
)
catmtCidSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidSentOctets.setStatus("current")
if mibBuilder.loadTexts:
    catmtCidSentOctets.setUnits("bytes")
_CatmtCidRcvdOctets_Type = Counter32SinceReset
_CatmtCidRcvdOctets_Object = MibTableColumn
catmtCidRcvdOctets = _CatmtCidRcvdOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 4),
    _CatmtCidRcvdOctets_Type()
)
catmtCidRcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidRcvdOctets.setStatus("current")
if mibBuilder.loadTexts:
    catmtCidRcvdOctets.setUnits("bytes")
_CatmtCidLostPackets_Type = Counter32SinceReset
_CatmtCidLostPackets_Object = MibTableColumn
catmtCidLostPackets = _CatmtCidLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 5),
    _CatmtCidLostPackets_Type()
)
catmtCidLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    catmtCidLostPackets.setUnits("packets")


class _CatmtCidJitter_Type(Gauge32):
    """Custom type catmtCidJitter based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CatmtCidJitter_Type.__name__ = "Gauge32"
_CatmtCidJitter_Object = MibTableColumn
catmtCidJitter = _CatmtCidJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 6),
    _CatmtCidJitter_Type()
)
catmtCidJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidJitter.setStatus("current")
if mibBuilder.loadTexts:
    catmtCidJitter.setUnits("milliseconds")
_CatmtCidExtAISCnts_Type = Counter32SinceReset
_CatmtCidExtAISCnts_Object = MibTableColumn
catmtCidExtAISCnts = _CatmtCidExtAISCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 7),
    _CatmtCidExtAISCnts_Type()
)
catmtCidExtAISCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidExtAISCnts.setStatus("current")
_CatmtCidExtRAICnts_Type = Counter32SinceReset
_CatmtCidExtRAICnts_Object = MibTableColumn
catmtCidExtRAICnts = _CatmtCidExtRAICnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 8),
    _CatmtCidExtRAICnts_Type()
)
catmtCidExtRAICnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidExtRAICnts.setStatus("current")
_CatmtCidConnAISCnts_Type = Counter32SinceReset
_CatmtCidConnAISCnts_Object = MibTableColumn
catmtCidConnAISCnts = _CatmtCidConnAISCnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 9),
    _CatmtCidConnAISCnts_Type()
)
catmtCidConnAISCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidConnAISCnts.setStatus("current")
_CatmtCidConnRDICnts_Type = Counter32SinceReset
_CatmtCidConnRDICnts_Object = MibTableColumn
catmtCidConnRDICnts = _CatmtCidConnRDICnts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 10),
    _CatmtCidConnRDICnts_Type()
)
catmtCidConnRDICnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidConnRDICnts.setStatus("current")
_CatmtCidNx64FramesTxToTDM_Type = Counter32SinceReset
_CatmtCidNx64FramesTxToTDM_Object = MibTableColumn
catmtCidNx64FramesTxToTDM = _CatmtCidNx64FramesTxToTDM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 11),
    _CatmtCidNx64FramesTxToTDM_Type()
)
catmtCidNx64FramesTxToTDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidNx64FramesTxToTDM.setStatus("current")
_CatmtCidNx64FramesRxFromTDM_Type = Counter32SinceReset
_CatmtCidNx64FramesRxFromTDM_Object = MibTableColumn
catmtCidNx64FramesRxFromTDM = _CatmtCidNx64FramesRxFromTDM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 12),
    _CatmtCidNx64FramesRxFromTDM_Type()
)
catmtCidNx64FramesRxFromTDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidNx64FramesRxFromTDM.setStatus("current")
_CatmtCidNx64EncBytesTxToTDM_Type = Counter32SinceReset
_CatmtCidNx64EncBytesTxToTDM_Object = MibTableColumn
catmtCidNx64EncBytesTxToTDM = _CatmtCidNx64EncBytesTxToTDM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 13),
    _CatmtCidNx64EncBytesTxToTDM_Type()
)
catmtCidNx64EncBytesTxToTDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidNx64EncBytesTxToTDM.setStatus("current")
_CatmtCidNx64EncBytesRxFromTDM_Type = Counter32SinceReset
_CatmtCidNx64EncBytesRxFromTDM_Object = MibTableColumn
catmtCidNx64EncBytesRxFromTDM = _CatmtCidNx64EncBytesRxFromTDM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 14),
    _CatmtCidNx64EncBytesRxFromTDM_Type()
)
catmtCidNx64EncBytesRxFromTDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidNx64EncBytesRxFromTDM.setStatus("current")
_CatmtCidNx64InvalidFCSFrames_Type = Counter32SinceReset
_CatmtCidNx64InvalidFCSFrames_Object = MibTableColumn
catmtCidNx64InvalidFCSFrames = _CatmtCidNx64InvalidFCSFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 15),
    _CatmtCidNx64InvalidFCSFrames_Type()
)
catmtCidNx64InvalidFCSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidNx64InvalidFCSFrames.setStatus("current")
_CatmtCidNx64AbortSeqFrames_Type = Counter32SinceReset
_CatmtCidNx64AbortSeqFrames_Object = MibTableColumn
catmtCidNx64AbortSeqFrames = _CatmtCidNx64AbortSeqFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 16),
    _CatmtCidNx64AbortSeqFrames_Type()
)
catmtCidNx64AbortSeqFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidNx64AbortSeqFrames.setStatus("current")
_CatmtCidNx64InvalidShortFrames_Type = Counter32SinceReset
_CatmtCidNx64InvalidShortFrames_Object = MibTableColumn
catmtCidNx64InvalidShortFrames = _CatmtCidNx64InvalidShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 17),
    _CatmtCidNx64InvalidShortFrames_Type()
)
catmtCidNx64InvalidShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidNx64InvalidShortFrames.setStatus("current")
_CatmtCidNx64InvalidLongFrames_Type = Counter32SinceReset
_CatmtCidNx64InvalidLongFrames_Object = MibTableColumn
catmtCidNx64InvalidLongFrames = _CatmtCidNx64InvalidLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 18),
    _CatmtCidNx64InvalidLongFrames_Type()
)
catmtCidNx64InvalidLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidNx64InvalidLongFrames.setStatus("current")
_CatmtCidNx64NoByteAlignErrorFrames_Type = Counter32SinceReset
_CatmtCidNx64NoByteAlignErrorFrames_Object = MibTableColumn
catmtCidNx64NoByteAlignErrorFrames = _CatmtCidNx64NoByteAlignErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 19),
    _CatmtCidNx64NoByteAlignErrorFrames_Type()
)
catmtCidNx64NoByteAlignErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidNx64NoByteAlignErrorFrames.setStatus("current")
_CatmtCidNx64RASTimeOutFrames_Type = Counter32SinceReset
_CatmtCidNx64RASTimeOutFrames_Object = MibTableColumn
catmtCidNx64RASTimeOutFrames = _CatmtCidNx64RASTimeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 20),
    _CatmtCidNx64RASTimeOutFrames_Type()
)
catmtCidNx64RASTimeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidNx64RASTimeOutFrames.setStatus("current")
_CatmtCidLastResetTime_Type = TimeStamp
_CatmtCidLastResetTime_Object = MibTableColumn
catmtCidLastResetTime = _CatmtCidLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 21),
    _CatmtCidLastResetTime_Type()
)
catmtCidLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtCidLastResetTime.setStatus("current")
_CatmtCidCounterClear_Type = TruthValue
_CatmtCidCounterClear_Object = MibTableColumn
catmtCidCounterClear = _CatmtCidCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 2, 1, 1, 22),
    _CatmtCidCounterClear_Type()
)
catmtCidCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmtCidCounterClear.setStatus("current")
_CAtmTrunkAal1Config_ObjectIdentity = ObjectIdentity
cAtmTrunkAal1Config = _CAtmTrunkAal1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 3)
)
_CatmtAal1Table_Object = MibTable
catmtAal1Table = _CatmtAal1Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 3, 1)
)
if mibBuilder.loadTexts:
    catmtAal1Table.setStatus("current")
_CatmtAal1Entry_Object = MibTableRow
catmtAal1Entry = _CatmtAal1Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 3, 1, 1)
)
catmtAal1Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtAal1Vpi"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtAal1Vci"),
)
if mibBuilder.loadTexts:
    catmtAal1Entry.setStatus("current")


class _CatmtAal1Vpi_Type(Unsigned32):
    """Custom type catmtAal1Vpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CatmtAal1Vpi_Type.__name__ = "Unsigned32"
_CatmtAal1Vpi_Object = MibTableColumn
catmtAal1Vpi = _CatmtAal1Vpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 3, 1, 1, 1),
    _CatmtAal1Vpi_Type()
)
catmtAal1Vpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catmtAal1Vpi.setStatus("current")


class _CatmtAal1Vci_Type(Unsigned32):
    """Custom type catmtAal1Vci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CatmtAal1Vci_Type.__name__ = "Unsigned32"
_CatmtAal1Vci_Object = MibTableColumn
catmtAal1Vci = _CatmtAal1Vci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 3, 1, 1, 2),
    _CatmtAal1Vci_Type()
)
catmtAal1Vci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catmtAal1Vci.setStatus("current")
_CatmtAal1Ds1_Type = InterfaceIndex
_CatmtAal1Ds1_Object = MibTableColumn
catmtAal1Ds1 = _CatmtAal1Ds1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 3, 1, 1, 3),
    _CatmtAal1Ds1_Type()
)
catmtAal1Ds1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtAal1Ds1.setStatus("current")


class _CatmtAal1Ds0GroupIndex_Type(Integer32):
    """Custom type catmtAal1Ds0GroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CatmtAal1Ds0GroupIndex_Type.__name__ = "Integer32"
_CatmtAal1Ds0GroupIndex_Object = MibTableColumn
catmtAal1Ds0GroupIndex = _CatmtAal1Ds0GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 3, 1, 1, 4),
    _CatmtAal1Ds0GroupIndex_Type()
)
catmtAal1Ds0GroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtAal1Ds0GroupIndex.setStatus("current")


class _CatmtAal1Nx64Profile_Type(Integer32):
    """Custom type catmtAal1Nx64Profile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CatmtAal1Nx64Profile_Type.__name__ = "Integer32"
_CatmtAal1Nx64Profile_Object = MibTableColumn
catmtAal1Nx64Profile = _CatmtAal1Nx64Profile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 3, 1, 1, 5),
    _CatmtAal1Nx64Profile_Type()
)
catmtAal1Nx64Profile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtAal1Nx64Profile.setStatus("current")
_CatmtAal1RowStatus_Type = RowStatus
_CatmtAal1RowStatus_Object = MibTableColumn
catmtAal1RowStatus = _CatmtAal1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 3, 1, 1, 6),
    _CatmtAal1RowStatus_Type()
)
catmtAal1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtAal1RowStatus.setStatus("current")
_CAtmTrunkAal1ConnStats_ObjectIdentity = ObjectIdentity
cAtmTrunkAal1ConnStats = _CAtmTrunkAal1ConnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 4)
)
_CatmtAal1StatsTable_Object = MibTable
catmtAal1StatsTable = _CatmtAal1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 4, 1)
)
if mibBuilder.loadTexts:
    catmtAal1StatsTable.setStatus("current")
_CatmtAal1StatsEntry_Object = MibTableRow
catmtAal1StatsEntry = _CatmtAal1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 4, 1, 1)
)
catmtAal1StatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtAal1Vpi"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtAal1Vci"),
)
if mibBuilder.loadTexts:
    catmtAal1StatsEntry.setStatus("current")
_CatmtAal1TxCells_Type = Counter32SinceReset
_CatmtAal1TxCells_Object = MibTableColumn
catmtAal1TxCells = _CatmtAal1TxCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 4, 1, 1, 1),
    _CatmtAal1TxCells_Type()
)
catmtAal1TxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal1TxCells.setStatus("current")
_CatmtAal1RxCells_Type = Counter32SinceReset
_CatmtAal1RxCells_Object = MibTableColumn
catmtAal1RxCells = _CatmtAal1RxCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 4, 1, 1, 2),
    _CatmtAal1RxCells_Type()
)
catmtAal1RxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal1RxCells.setStatus("current")
_CatmtAal1TxPayloadBytes_Type = Counter32SinceReset
_CatmtAal1TxPayloadBytes_Object = MibTableColumn
catmtAal1TxPayloadBytes = _CatmtAal1TxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 4, 1, 1, 3),
    _CatmtAal1TxPayloadBytes_Type()
)
catmtAal1TxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal1TxPayloadBytes.setStatus("current")
_CatmtAal1RxPayloadBytes_Type = Counter32SinceReset
_CatmtAal1RxPayloadBytes_Object = MibTableColumn
catmtAal1RxPayloadBytes = _CatmtAal1RxPayloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 4, 1, 1, 4),
    _CatmtAal1RxPayloadBytes_Type()
)
catmtAal1RxPayloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal1RxPayloadBytes.setStatus("current")
_CatmtAal1Jitter_Type = Gauge32
_CatmtAal1Jitter_Object = MibTableColumn
catmtAal1Jitter = _CatmtAal1Jitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 4, 1, 1, 5),
    _CatmtAal1Jitter_Type()
)
catmtAal1Jitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal1Jitter.setStatus("current")
_CatmtAal1LastResetTime_Type = TimeStamp
_CatmtAal1LastResetTime_Object = MibTableColumn
catmtAal1LastResetTime = _CatmtAal1LastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 4, 1, 1, 6),
    _CatmtAal1LastResetTime_Type()
)
catmtAal1LastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal1LastResetTime.setStatus("current")
_CatmtAal1CounterClear_Type = TruthValue
_CatmtAal1CounterClear_Object = MibTableColumn
catmtAal1CounterClear = _CatmtAal1CounterClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 4, 1, 1, 7),
    _CatmtAal1CounterClear_Type()
)
catmtAal1CounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmtAal1CounterClear.setStatus("current")
_CAtmTrunkAal5Config_ObjectIdentity = ObjectIdentity
cAtmTrunkAal5Config = _CAtmTrunkAal5Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 5)
)
_CatmtAal5Table_Object = MibTable
catmtAal5Table = _CatmtAal5Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 5, 1)
)
if mibBuilder.loadTexts:
    catmtAal5Table.setStatus("current")
_CatmtAal5Entry_Object = MibTableRow
catmtAal5Entry = _CatmtAal5Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 5, 1, 1)
)
catmtAal5Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtAal5Vpi"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtAal5Vci"),
)
if mibBuilder.loadTexts:
    catmtAal5Entry.setStatus("current")


class _CatmtAal5Vpi_Type(Unsigned32):
    """Custom type catmtAal5Vpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CatmtAal5Vpi_Type.__name__ = "Unsigned32"
_CatmtAal5Vpi_Object = MibTableColumn
catmtAal5Vpi = _CatmtAal5Vpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 5, 1, 1, 1),
    _CatmtAal5Vpi_Type()
)
catmtAal5Vpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catmtAal5Vpi.setStatus("current")


class _CatmtAal5Vci_Type(Unsigned32):
    """Custom type catmtAal5Vci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CatmtAal5Vci_Type.__name__ = "Unsigned32"
_CatmtAal5Vci_Object = MibTableColumn
catmtAal5Vci = _CatmtAal5Vci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 5, 1, 1, 2),
    _CatmtAal5Vci_Type()
)
catmtAal5Vci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    catmtAal5Vci.setStatus("current")
_CatmtAal5Ds1_Type = InterfaceIndex
_CatmtAal5Ds1_Object = MibTableColumn
catmtAal5Ds1 = _CatmtAal5Ds1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 5, 1, 1, 3),
    _CatmtAal5Ds1_Type()
)
catmtAal5Ds1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtAal5Ds1.setStatus("current")


class _CatmtAal5Ds0GroupIndex_Type(Integer32):
    """Custom type catmtAal5Ds0GroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_CatmtAal5Ds0GroupIndex_Type.__name__ = "Integer32"
_CatmtAal5Ds0GroupIndex_Object = MibTableColumn
catmtAal5Ds0GroupIndex = _CatmtAal5Ds0GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 5, 1, 1, 4),
    _CatmtAal5Ds0GroupIndex_Type()
)
catmtAal5Ds0GroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtAal5Ds0GroupIndex.setStatus("current")


class _CatmtAal5Nx64Profile_Type(Integer32):
    """Custom type catmtAal5Nx64Profile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CatmtAal5Nx64Profile_Type.__name__ = "Integer32"
_CatmtAal5Nx64Profile_Object = MibTableColumn
catmtAal5Nx64Profile = _CatmtAal5Nx64Profile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 5, 1, 1, 5),
    _CatmtAal5Nx64Profile_Type()
)
catmtAal5Nx64Profile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtAal5Nx64Profile.setStatus("current")
_CatmtAal5RowStatus_Type = RowStatus
_CatmtAal5RowStatus_Object = MibTableColumn
catmtAal5RowStatus = _CatmtAal5RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 5, 1, 1, 6),
    _CatmtAal5RowStatus_Type()
)
catmtAal5RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    catmtAal5RowStatus.setStatus("current")
_CAtmTrunkAal5ConnStats_ObjectIdentity = ObjectIdentity
cAtmTrunkAal5ConnStats = _CAtmTrunkAal5ConnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6)
)
_CatmtAal5StatsTable_Object = MibTable
catmtAal5StatsTable = _CatmtAal5StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1)
)
if mibBuilder.loadTexts:
    catmtAal5StatsTable.setStatus("current")
_CatmtAal5StatsEntry_Object = MibTableRow
catmtAal5StatsEntry = _CatmtAal5StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1)
)
catmtAal5StatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtAal5Vpi"),
    (0, "CISCO-ATM-TRUNK-MIB", "catmtAal5Vci"),
)
if mibBuilder.loadTexts:
    catmtAal5StatsEntry.setStatus("current")
_CatmtAal5SentPackets_Type = Counter32SinceReset
_CatmtAal5SentPackets_Object = MibTableColumn
catmtAal5SentPackets = _CatmtAal5SentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 1),
    _CatmtAal5SentPackets_Type()
)
catmtAal5SentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5SentPackets.setStatus("current")
if mibBuilder.loadTexts:
    catmtAal5SentPackets.setUnits("packets")
_CatmtAal5RcvdPackets_Type = Counter32SinceReset
_CatmtAal5RcvdPackets_Object = MibTableColumn
catmtAal5RcvdPackets = _CatmtAal5RcvdPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 2),
    _CatmtAal5RcvdPackets_Type()
)
catmtAal5RcvdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5RcvdPackets.setStatus("current")
if mibBuilder.loadTexts:
    catmtAal5RcvdPackets.setUnits("packets")
_CatmtAal5SentOctets_Type = Counter32SinceReset
_CatmtAal5SentOctets_Object = MibTableColumn
catmtAal5SentOctets = _CatmtAal5SentOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 3),
    _CatmtAal5SentOctets_Type()
)
catmtAal5SentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5SentOctets.setStatus("current")
if mibBuilder.loadTexts:
    catmtAal5SentOctets.setUnits("bytes")
_CatmtAal5RcvdOctets_Type = Counter32SinceReset
_CatmtAal5RcvdOctets_Object = MibTableColumn
catmtAal5RcvdOctets = _CatmtAal5RcvdOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 4),
    _CatmtAal5RcvdOctets_Type()
)
catmtAal5RcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5RcvdOctets.setStatus("current")
if mibBuilder.loadTexts:
    catmtAal5RcvdOctets.setUnits("bytes")
_CatmtAal5FramesTxToTDM_Type = Counter32SinceReset
_CatmtAal5FramesTxToTDM_Object = MibTableColumn
catmtAal5FramesTxToTDM = _CatmtAal5FramesTxToTDM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 5),
    _CatmtAal5FramesTxToTDM_Type()
)
catmtAal5FramesTxToTDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5FramesTxToTDM.setStatus("current")
_CatmtAal5FramesRxFromTDM_Type = Counter32SinceReset
_CatmtAal5FramesRxFromTDM_Object = MibTableColumn
catmtAal5FramesRxFromTDM = _CatmtAal5FramesRxFromTDM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 6),
    _CatmtAal5FramesRxFromTDM_Type()
)
catmtAal5FramesRxFromTDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5FramesRxFromTDM.setStatus("current")
_CatmtAal5EncBytesTxToTDM_Type = Counter32SinceReset
_CatmtAal5EncBytesTxToTDM_Object = MibTableColumn
catmtAal5EncBytesTxToTDM = _CatmtAal5EncBytesTxToTDM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 7),
    _CatmtAal5EncBytesTxToTDM_Type()
)
catmtAal5EncBytesTxToTDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5EncBytesTxToTDM.setStatus("current")
_CatmtAal5EncBytesRxFromTDM_Type = Counter32SinceReset
_CatmtAal5EncBytesRxFromTDM_Object = MibTableColumn
catmtAal5EncBytesRxFromTDM = _CatmtAal5EncBytesRxFromTDM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 8),
    _CatmtAal5EncBytesRxFromTDM_Type()
)
catmtAal5EncBytesRxFromTDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5EncBytesRxFromTDM.setStatus("current")
_CatmtAal5InvalidFCSFrames_Type = Counter32SinceReset
_CatmtAal5InvalidFCSFrames_Object = MibTableColumn
catmtAal5InvalidFCSFrames = _CatmtAal5InvalidFCSFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 9),
    _CatmtAal5InvalidFCSFrames_Type()
)
catmtAal5InvalidFCSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5InvalidFCSFrames.setStatus("current")
_CatmtAal5AbortSeqFrames_Type = Counter32SinceReset
_CatmtAal5AbortSeqFrames_Object = MibTableColumn
catmtAal5AbortSeqFrames = _CatmtAal5AbortSeqFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 10),
    _CatmtAal5AbortSeqFrames_Type()
)
catmtAal5AbortSeqFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5AbortSeqFrames.setStatus("current")
_CatmtAal5InvalidShortFrames_Type = Counter32SinceReset
_CatmtAal5InvalidShortFrames_Object = MibTableColumn
catmtAal5InvalidShortFrames = _CatmtAal5InvalidShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 11),
    _CatmtAal5InvalidShortFrames_Type()
)
catmtAal5InvalidShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5InvalidShortFrames.setStatus("current")
_CatmtAal5InvalidLongFrames_Type = Counter32SinceReset
_CatmtAal5InvalidLongFrames_Object = MibTableColumn
catmtAal5InvalidLongFrames = _CatmtAal5InvalidLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 12),
    _CatmtAal5InvalidLongFrames_Type()
)
catmtAal5InvalidLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5InvalidLongFrames.setStatus("current")
_CatmtAal5NoByteAlignErrorFrames_Type = Counter32SinceReset
_CatmtAal5NoByteAlignErrorFrames_Object = MibTableColumn
catmtAal5NoByteAlignErrorFrames = _CatmtAal5NoByteAlignErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 13),
    _CatmtAal5NoByteAlignErrorFrames_Type()
)
catmtAal5NoByteAlignErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5NoByteAlignErrorFrames.setStatus("current")
_CatmtAal5LastResetTime_Type = TimeStamp
_CatmtAal5LastResetTime_Object = MibTableColumn
catmtAal5LastResetTime = _CatmtAal5LastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 14),
    _CatmtAal5LastResetTime_Type()
)
catmtAal5LastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catmtAal5LastResetTime.setStatus("current")
_CatmtAal5CounterClear_Type = TruthValue
_CatmtAal5CounterClear_Object = MibTableColumn
catmtAal5CounterClear = _CatmtAal5CounterClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 1, 6, 1, 1, 15),
    _CatmtAal5CounterClear_Type()
)
catmtAal5CounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catmtAal5CounterClear.setStatus("current")
_CAtmTrunkMIBConformance_ObjectIdentity = ObjectIdentity
cAtmTrunkMIBConformance = _CAtmTrunkMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 2)
)
_CAtmTrunkMIBCompliances_ObjectIdentity = ObjectIdentity
cAtmTrunkMIBCompliances = _CAtmTrunkMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 2, 1)
)
_CAtmTrunkMIBGroups_ObjectIdentity = ObjectIdentity
cAtmTrunkMIBGroups = _CAtmTrunkMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 2, 2)
)

# Managed Objects groups

cAtmTrunkCidMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 2, 2, 1)
)
cAtmTrunkCidMIBGroup.setObjects(
      *(("CISCO-ATM-TRUNK-MIB", "catmtCidDs1"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidDs0GroupIndex"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidProfileType"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidProfileNumber"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidVoiceCodec"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidVBDCodec"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64Enable"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64Profile"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidStateBitMap"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidRepetition"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidRepetitionOwner"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidRepetitionResult"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidRowStatus"))
)
if mibBuilder.loadTexts:
    cAtmTrunkCidMIBGroup.setStatus("current")

cAtmTrunkAal1MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 2, 2, 2)
)
cAtmTrunkAal1MIBGroup.setObjects(
      *(("CISCO-ATM-TRUNK-MIB", "catmtAal1Ds1"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal1Ds0GroupIndex"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal1Nx64Profile"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal1RowStatus"))
)
if mibBuilder.loadTexts:
    cAtmTrunkAal1MIBGroup.setStatus("current")

cAtmTrunkAal5MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 2, 2, 3)
)
cAtmTrunkAal5MIBGroup.setObjects(
      *(("CISCO-ATM-TRUNK-MIB", "catmtAal5Ds1"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5Ds0GroupIndex"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5Nx64Profile"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5RowStatus"))
)
if mibBuilder.loadTexts:
    cAtmTrunkAal5MIBGroup.setStatus("current")

cAtmTrunkCidConnStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 2, 2, 4)
)
cAtmTrunkCidConnStatsMIBGroup.setObjects(
      *(("CISCO-ATM-TRUNK-MIB", "catmtCidSentPackets"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidRcvdPackets"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidSentOctets"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidRcvdOctets"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidLostPackets"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidJitter"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidExtAISCnts"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidExtRAICnts"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidConnAISCnts"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidConnRDICnts"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64FramesTxToTDM"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64FramesRxFromTDM"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64EncBytesTxToTDM"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64EncBytesRxFromTDM"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64InvalidFCSFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64AbortSeqFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64InvalidShortFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64InvalidLongFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64NoByteAlignErrorFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidNx64RASTimeOutFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidLastResetTime"),
        ("CISCO-ATM-TRUNK-MIB", "catmtCidCounterClear"))
)
if mibBuilder.loadTexts:
    cAtmTrunkCidConnStatsMIBGroup.setStatus("current")

cAtmTrunkAal1ConnStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 2, 2, 5)
)
cAtmTrunkAal1ConnStatsMIBGroup.setObjects(
      *(("CISCO-ATM-TRUNK-MIB", "catmtAal1TxCells"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal1RxCells"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal1TxPayloadBytes"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal1RxPayloadBytes"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal1Jitter"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal1LastResetTime"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal1CounterClear"))
)
if mibBuilder.loadTexts:
    cAtmTrunkAal1ConnStatsMIBGroup.setStatus("current")

cAtmTrunkAal5ConnStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 2, 2, 6)
)
cAtmTrunkAal5ConnStatsMIBGroup.setObjects(
      *(("CISCO-ATM-TRUNK-MIB", "catmtAal5SentPackets"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5RcvdPackets"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5SentOctets"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5RcvdOctets"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5FramesTxToTDM"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5FramesRxFromTDM"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5EncBytesTxToTDM"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5EncBytesRxFromTDM"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5InvalidFCSFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5AbortSeqFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5InvalidShortFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5InvalidLongFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5NoByteAlignErrorFrames"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5LastResetTime"),
        ("CISCO-ATM-TRUNK-MIB", "catmtAal5CounterClear"))
)
if mibBuilder.loadTexts:
    cAtmTrunkAal5ConnStatsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cAtmTrunkMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 351, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cAtmTrunkMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-TRUNK-MIB",
    **{"Counter32SinceReset": Counter32SinceReset,
       "ciscoAtmTrunkMIB": ciscoAtmTrunkMIB,
       "cAtmTrunkMIBNotifications": cAtmTrunkMIBNotifications,
       "cAtmTrunkMIBObjects": cAtmTrunkMIBObjects,
       "cAtmTrunkCidConfig": cAtmTrunkCidConfig,
       "catmtCidTable": catmtCidTable,
       "catmtCidEntry": catmtCidEntry,
       "catmtCidVpi": catmtCidVpi,
       "catmtCidVci": catmtCidVci,
       "catmtCid": catmtCid,
       "catmtCidDs1": catmtCidDs1,
       "catmtCidDs0GroupIndex": catmtCidDs0GroupIndex,
       "catmtCidProfileType": catmtCidProfileType,
       "catmtCidProfileNumber": catmtCidProfileNumber,
       "catmtCidVoiceCodec": catmtCidVoiceCodec,
       "catmtCidVBDCodec": catmtCidVBDCodec,
       "catmtCidNx64Enable": catmtCidNx64Enable,
       "catmtCidNx64Profile": catmtCidNx64Profile,
       "catmtCidStateBitMap": catmtCidStateBitMap,
       "catmtCidRepetition": catmtCidRepetition,
       "catmtCidRepetitionOwner": catmtCidRepetitionOwner,
       "catmtCidRepetitionResult": catmtCidRepetitionResult,
       "catmtCidRowStatus": catmtCidRowStatus,
       "cAtmTrunkCidConnStats": cAtmTrunkCidConnStats,
       "catmtCidStatsTable": catmtCidStatsTable,
       "catmtCidStatsEntry": catmtCidStatsEntry,
       "catmtCidSentPackets": catmtCidSentPackets,
       "catmtCidRcvdPackets": catmtCidRcvdPackets,
       "catmtCidSentOctets": catmtCidSentOctets,
       "catmtCidRcvdOctets": catmtCidRcvdOctets,
       "catmtCidLostPackets": catmtCidLostPackets,
       "catmtCidJitter": catmtCidJitter,
       "catmtCidExtAISCnts": catmtCidExtAISCnts,
       "catmtCidExtRAICnts": catmtCidExtRAICnts,
       "catmtCidConnAISCnts": catmtCidConnAISCnts,
       "catmtCidConnRDICnts": catmtCidConnRDICnts,
       "catmtCidNx64FramesTxToTDM": catmtCidNx64FramesTxToTDM,
       "catmtCidNx64FramesRxFromTDM": catmtCidNx64FramesRxFromTDM,
       "catmtCidNx64EncBytesTxToTDM": catmtCidNx64EncBytesTxToTDM,
       "catmtCidNx64EncBytesRxFromTDM": catmtCidNx64EncBytesRxFromTDM,
       "catmtCidNx64InvalidFCSFrames": catmtCidNx64InvalidFCSFrames,
       "catmtCidNx64AbortSeqFrames": catmtCidNx64AbortSeqFrames,
       "catmtCidNx64InvalidShortFrames": catmtCidNx64InvalidShortFrames,
       "catmtCidNx64InvalidLongFrames": catmtCidNx64InvalidLongFrames,
       "catmtCidNx64NoByteAlignErrorFrames": catmtCidNx64NoByteAlignErrorFrames,
       "catmtCidNx64RASTimeOutFrames": catmtCidNx64RASTimeOutFrames,
       "catmtCidLastResetTime": catmtCidLastResetTime,
       "catmtCidCounterClear": catmtCidCounterClear,
       "cAtmTrunkAal1Config": cAtmTrunkAal1Config,
       "catmtAal1Table": catmtAal1Table,
       "catmtAal1Entry": catmtAal1Entry,
       "catmtAal1Vpi": catmtAal1Vpi,
       "catmtAal1Vci": catmtAal1Vci,
       "catmtAal1Ds1": catmtAal1Ds1,
       "catmtAal1Ds0GroupIndex": catmtAal1Ds0GroupIndex,
       "catmtAal1Nx64Profile": catmtAal1Nx64Profile,
       "catmtAal1RowStatus": catmtAal1RowStatus,
       "cAtmTrunkAal1ConnStats": cAtmTrunkAal1ConnStats,
       "catmtAal1StatsTable": catmtAal1StatsTable,
       "catmtAal1StatsEntry": catmtAal1StatsEntry,
       "catmtAal1TxCells": catmtAal1TxCells,
       "catmtAal1RxCells": catmtAal1RxCells,
       "catmtAal1TxPayloadBytes": catmtAal1TxPayloadBytes,
       "catmtAal1RxPayloadBytes": catmtAal1RxPayloadBytes,
       "catmtAal1Jitter": catmtAal1Jitter,
       "catmtAal1LastResetTime": catmtAal1LastResetTime,
       "catmtAal1CounterClear": catmtAal1CounterClear,
       "cAtmTrunkAal5Config": cAtmTrunkAal5Config,
       "catmtAal5Table": catmtAal5Table,
       "catmtAal5Entry": catmtAal5Entry,
       "catmtAal5Vpi": catmtAal5Vpi,
       "catmtAal5Vci": catmtAal5Vci,
       "catmtAal5Ds1": catmtAal5Ds1,
       "catmtAal5Ds0GroupIndex": catmtAal5Ds0GroupIndex,
       "catmtAal5Nx64Profile": catmtAal5Nx64Profile,
       "catmtAal5RowStatus": catmtAal5RowStatus,
       "cAtmTrunkAal5ConnStats": cAtmTrunkAal5ConnStats,
       "catmtAal5StatsTable": catmtAal5StatsTable,
       "catmtAal5StatsEntry": catmtAal5StatsEntry,
       "catmtAal5SentPackets": catmtAal5SentPackets,
       "catmtAal5RcvdPackets": catmtAal5RcvdPackets,
       "catmtAal5SentOctets": catmtAal5SentOctets,
       "catmtAal5RcvdOctets": catmtAal5RcvdOctets,
       "catmtAal5FramesTxToTDM": catmtAal5FramesTxToTDM,
       "catmtAal5FramesRxFromTDM": catmtAal5FramesRxFromTDM,
       "catmtAal5EncBytesTxToTDM": catmtAal5EncBytesTxToTDM,
       "catmtAal5EncBytesRxFromTDM": catmtAal5EncBytesRxFromTDM,
       "catmtAal5InvalidFCSFrames": catmtAal5InvalidFCSFrames,
       "catmtAal5AbortSeqFrames": catmtAal5AbortSeqFrames,
       "catmtAal5InvalidShortFrames": catmtAal5InvalidShortFrames,
       "catmtAal5InvalidLongFrames": catmtAal5InvalidLongFrames,
       "catmtAal5NoByteAlignErrorFrames": catmtAal5NoByteAlignErrorFrames,
       "catmtAal5LastResetTime": catmtAal5LastResetTime,
       "catmtAal5CounterClear": catmtAal5CounterClear,
       "cAtmTrunkMIBConformance": cAtmTrunkMIBConformance,
       "cAtmTrunkMIBCompliances": cAtmTrunkMIBCompliances,
       "cAtmTrunkMIBCompliance": cAtmTrunkMIBCompliance,
       "cAtmTrunkMIBGroups": cAtmTrunkMIBGroups,
       "cAtmTrunkCidMIBGroup": cAtmTrunkCidMIBGroup,
       "cAtmTrunkAal1MIBGroup": cAtmTrunkAal1MIBGroup,
       "cAtmTrunkAal5MIBGroup": cAtmTrunkAal5MIBGroup,
       "cAtmTrunkCidConnStatsMIBGroup": cAtmTrunkCidConnStatsMIBGroup,
       "cAtmTrunkAal1ConnStatsMIBGroup": cAtmTrunkAal1ConnStatsMIBGroup,
       "cAtmTrunkAal5ConnStatsMIBGroup": cAtmTrunkAal5ConnStatsMIBGroup}
)
