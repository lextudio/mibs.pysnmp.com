# SNMP MIB module (CISCO-TELEPRESENCE-CALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TELEPRESENCE-CALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:37 2024
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

(QosLayer2Cos,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "QosLayer2Cos")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Unsigned64,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned64")

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

ciscoTelepresenceCallMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644)
)
ciscoTelepresenceCallMIB.setRevisions(
        ("2014-07-24 00:00",
         "2012-11-08 00:00",
         "2012-04-20 00:00",
         "2012-01-11 00:00",
         "2011-05-16 00:00",
         "2011-02-04 00:00",
         "2011-01-31 00:00",
         "2009-10-21 00:00",
         "2008-09-17 00:00",
         "2008-01-23 00:00",
         "2007-12-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CtpcE164Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "32t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class CtpcStreamMediaType(Integer32, TextualConvention):
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
        *(("audio", 2),
          ("content", 3),
          ("video", 1))
    )



class CtpcStreamSourceType(Integer32, TextualConvention):
    status = "current"
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("auxiliary1", 4),
          ("auxiliary2", 8),
          ("auxiliary3", 15),
          ("auxiliary4", 16),
          ("center", 9),
          ("left", 10),
          ("legacyCtr", 12),
          ("legacyLeft", 13),
          ("legacyRight", 14),
          ("other", 17),
          ("priCodec", 2),
          ("priLegacy", 6),
          ("right", 11),
          ("secCodec1", 1),
          ("secCodec2", 3),
          ("secLegacy1", 5),
          ("secLegacy2", 7))
    )



class CtpcStateCode(Integer32, TextualConvention):
    status = "current"
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("answer", 15),
          ("busy", 17),
          ("inLocalConference", 11),
          ("inProgress", 8),
          ("invalidNumber", 5),
          ("localHold", 13),
          ("noAnswer", 7),
          ("noDialTone", 4),
          ("noMgmtSysConn", 3),
          ("other", 2),
          ("pause", 18),
          ("playback", 19),
          ("recording", 20),
          ("remoteHold", 9),
          ("resume", 16),
          ("ringing", 6),
          ("shareLineActive", 10),
          ("terminatedNormally", 14),
          ("terminatedbyError", 12),
          ("unknown", 1))
    )



class CtpcStatMonitoredAttribute(Integer32, TextualConvention):
    status = "current"
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
        *(("authFailurePacket", 4),
          ("jitter", 2),
          ("latency", 1),
          ("packetLoss", 3))
    )



class CtpcStatMonitoredAttributeUnit(Integer32, TextualConvention):
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
        *(("micropercent", 2),
          ("milliseconds", 1),
          ("packets", 3))
    )



class CtpcStatAlarmMode(Integer32, TextualConvention):
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
        *(("fallingAlarm", 2),
          ("risingAlarm", 1),
          ("risingOrFallingAlarm", 3))
    )



class CtpcStatThreshCrossedType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallingThreshold", 2),
          ("risingThreshold", 1))
    )



class CtpcAttributes(Bits, TextualConvention):
    status = "current"


class CtpcRemoteDeviceType(Integer32, TextualConvention):
    status = "current"
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
        *(("audioDevice", 3),
          ("highDefinitionLegacyDevice", 5),
          ("other", 2),
          ("singleTelepresence", 6),
          ("telepresenceMultipointSwitch", 8),
          ("telepresenceRecordingServer", 9),
          ("telepresenceTranscodingDevice", 10),
          ("tripleTelepresence", 7),
          ("unknown", 1),
          ("videoLegacyDevice", 4))
    )



class CtpcCodecType(Integer32, TextualConvention):
    status = "current"
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
        *(("aaclc", 3),
          ("aacld", 4),
          ("aacldLatm", 13),
          ("g711A", 5),
          ("g711U", 6),
          ("g722", 7),
          ("g7221", 8),
          ("g728", 9),
          ("g729", 10),
          ("h263", 11),
          ("h264", 12),
          ("h265", 14),
          ("other", 2),
          ("unknown", 1))
    )



class CtpcMgmtSysConnStatusCode(Integer32, TextualConvention):
    status = "current"
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
        *(("internalError", 3),
          ("notRegister", 4),
          ("other", 2),
          ("registered", 5),
          ("registraionFailure", 6),
          ("unknown", 1))
    )



class CtpcCallTerminationCode(Integer32, TextualConvention):
    status = "current"
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
        *(("incall", 12),
          ("incompatibleRemoteEndPt", 9),
          ("internalError", 3),
          ("localDisconnected", 4),
          ("mediaNegotiationFailure", 7),
          ("networkCongestion", 6),
          ("other", 2),
          ("remoteDisconnected", 5),
          ("remoteTerminatedWithError", 11),
          ("securityConfigMismatched", 8),
          ("serviceUnavailable", 10),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoTelepresenceCallMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTelepresenceCallMIBNotifs = _CiscoTelepresenceCallMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 0)
)
_CiscoTelepresenceCallMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTelepresenceCallMIBObjects = _CiscoTelepresenceCallMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1)
)
_CtpcObjects_ObjectIdentity = ObjectIdentity
ctpcObjects = _CtpcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 1)
)


class _CtpcStatNotifyEnable_Type(TruthValue):
    """Custom type ctpcStatNotifyEnable based on TruthValue"""


_CtpcStatNotifyEnable_Object = MibScalar
ctpcStatNotifyEnable = _CtpcStatNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 1, 1),
    _CtpcStatNotifyEnable_Type()
)
ctpcStatNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpcStatNotifyEnable.setStatus("current")


class _CtpcMgmtSysConnNotifyEnable_Type(TruthValue):
    """Custom type ctpcMgmtSysConnNotifyEnable based on TruthValue"""


_CtpcMgmtSysConnNotifyEnable_Object = MibScalar
ctpcMgmtSysConnNotifyEnable = _CtpcMgmtSysConnNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 1, 2),
    _CtpcMgmtSysConnNotifyEnable_Type()
)
ctpcMgmtSysConnNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpcMgmtSysConnNotifyEnable.setStatus("current")
_CtpcInfoObjects_ObjectIdentity = ObjectIdentity
ctpcInfoObjects = _CtpcInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2)
)
_CtpcLocalAddrType_Type = InetAddressType
_CtpcLocalAddrType_Object = MibScalar
ctpcLocalAddrType = _CtpcLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 1),
    _CtpcLocalAddrType_Type()
)
ctpcLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcLocalAddrType.setStatus("current")
_CtpcLocalAddr_Type = InetAddress
_CtpcLocalAddr_Object = MibScalar
ctpcLocalAddr = _CtpcLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 2),
    _CtpcLocalAddr_Type()
)
ctpcLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcLocalAddr.setStatus("current")
_CtpcLocalDirNumTable_Object = MibTable
ctpcLocalDirNumTable = _CtpcLocalDirNumTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ctpcLocalDirNumTable.setStatus("current")
_CtpcLocalDirNumEntry_Object = MibTableRow
ctpcLocalDirNumEntry = _CtpcLocalDirNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 3, 1)
)
ctpcLocalDirNumEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcLocalDirNumIndex"),
)
if mibBuilder.loadTexts:
    ctpcLocalDirNumEntry.setStatus("current")
_CtpcLocalDirNumIndex_Type = Unsigned32
_CtpcLocalDirNumIndex_Object = MibTableColumn
ctpcLocalDirNumIndex = _CtpcLocalDirNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 3, 1, 1),
    _CtpcLocalDirNumIndex_Type()
)
ctpcLocalDirNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpcLocalDirNumIndex.setStatus("current")
_CtpcLocalDirNum_Type = CtpcE164Address
_CtpcLocalDirNum_Object = MibTableColumn
ctpcLocalDirNum = _CtpcLocalDirNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 3, 1, 2),
    _CtpcLocalDirNum_Type()
)
ctpcLocalDirNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcLocalDirNum.setStatus("current")
_CtpcExtNumberMask_Type = SnmpAdminString
_CtpcExtNumberMask_Object = MibTableColumn
ctpcExtNumberMask = _CtpcExtNumberMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 3, 1, 3),
    _CtpcExtNumberMask_Type()
)
ctpcExtNumberMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcExtNumberMask.setStatus("current")


class _CtpcMode_Type(Integer32):
    """Custom type ctpcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgmtSys", 2),
          ("noMgmtSys", 1))
    )


_CtpcMode_Type.__name__ = "Integer32"
_CtpcMode_Object = MibScalar
ctpcMode = _CtpcMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 4),
    _CtpcMode_Type()
)
ctpcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMode.setStatus("current")
_CtpcActiveMgmtSysIndex_Type = Unsigned32
_CtpcActiveMgmtSysIndex_Object = MibScalar
ctpcActiveMgmtSysIndex = _CtpcActiveMgmtSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 5),
    _CtpcActiveMgmtSysIndex_Type()
)
ctpcActiveMgmtSysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcActiveMgmtSysIndex.setStatus("current")
_CtpcMgmtSysTable_Object = MibTable
ctpcMgmtSysTable = _CtpcMgmtSysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ctpcMgmtSysTable.setStatus("current")
_CtpcMgmtSysEntry_Object = MibTableRow
ctpcMgmtSysEntry = _CtpcMgmtSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 6, 1)
)
ctpcMgmtSysEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysIndex"),
)
if mibBuilder.loadTexts:
    ctpcMgmtSysEntry.setStatus("current")


class _CtpcMgmtSysIndex_Type(Unsigned32):
    """Custom type ctpcMgmtSysIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CtpcMgmtSysIndex_Type.__name__ = "Unsigned32"
_CtpcMgmtSysIndex_Object = MibTableColumn
ctpcMgmtSysIndex = _CtpcMgmtSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 6, 1, 1),
    _CtpcMgmtSysIndex_Type()
)
ctpcMgmtSysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpcMgmtSysIndex.setStatus("current")
_CtpcMgmtSysAddrType_Type = InetAddressType
_CtpcMgmtSysAddrType_Object = MibTableColumn
ctpcMgmtSysAddrType = _CtpcMgmtSysAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 6, 1, 2),
    _CtpcMgmtSysAddrType_Type()
)
ctpcMgmtSysAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMgmtSysAddrType.setStatus("current")
_CtpcMgmtSysAddr_Type = InetAddress
_CtpcMgmtSysAddr_Object = MibTableColumn
ctpcMgmtSysAddr = _CtpcMgmtSysAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 6, 1, 3),
    _CtpcMgmtSysAddr_Type()
)
ctpcMgmtSysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMgmtSysAddr.setStatus("current")
_CtpcMgmtSysConnStatus_Type = CtpcMgmtSysConnStatusCode
_CtpcMgmtSysConnStatus_Object = MibTableColumn
ctpcMgmtSysConnStatus = _CtpcMgmtSysConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 6, 1, 4),
    _CtpcMgmtSysConnStatus_Type()
)
ctpcMgmtSysConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMgmtSysConnStatus.setStatus("current")
_CtpcMgmtSysSIPRespCode_Type = Unsigned32
_CtpcMgmtSysSIPRespCode_Object = MibTableColumn
ctpcMgmtSysSIPRespCode = _CtpcMgmtSysSIPRespCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 6, 1, 5),
    _CtpcMgmtSysSIPRespCode_Type()
)
ctpcMgmtSysSIPRespCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMgmtSysSIPRespCode.setStatus("current")
_CtpcTxDscpTelepresenceConfigured_Type = Dscp
_CtpcTxDscpTelepresenceConfigured_Object = MibScalar
ctpcTxDscpTelepresenceConfigured = _CtpcTxDscpTelepresenceConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 7),
    _CtpcTxDscpTelepresenceConfigured_Type()
)
ctpcTxDscpTelepresenceConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxDscpTelepresenceConfigured.setStatus("current")
_CtpcTxDscpAudioConfigured_Type = Dscp
_CtpcTxDscpAudioConfigured_Object = MibScalar
ctpcTxDscpAudioConfigured = _CtpcTxDscpAudioConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 2, 8),
    _CtpcTxDscpAudioConfigured_Type()
)
ctpcTxDscpAudioConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxDscpAudioConfigured.setStatus("current")
_CtpcStatMonitorObjects_ObjectIdentity = ObjectIdentity
ctpcStatMonitorObjects = _CtpcStatMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 3)
)
_CtpcStatMonitoredTable_Object = MibTable
ctpcStatMonitoredTable = _CtpcStatMonitoredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctpcStatMonitoredTable.setStatus("current")
_CtpcStatMonitoredEntry_Object = MibTableRow
ctpcStatMonitoredEntry = _CtpcStatMonitoredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 3, 1, 1)
)
ctpcStatMonitoredEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatMonitoredType"),
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatMonitoredStreamType"),
)
if mibBuilder.loadTexts:
    ctpcStatMonitoredEntry.setStatus("current")
_CtpcStatMonitoredType_Type = CtpcStatMonitoredAttribute
_CtpcStatMonitoredType_Object = MibTableColumn
ctpcStatMonitoredType = _CtpcStatMonitoredType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 3, 1, 1, 1),
    _CtpcStatMonitoredType_Type()
)
ctpcStatMonitoredType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpcStatMonitoredType.setStatus("current")


class _CtpcStatMonitoredStreamType_Type(Integer32):
    """Custom type ctpcStatMonitoredStreamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("audio", 2),
          ("video", 1))
    )


_CtpcStatMonitoredStreamType_Type.__name__ = "Integer32"
_CtpcStatMonitoredStreamType_Object = MibTableColumn
ctpcStatMonitoredStreamType = _CtpcStatMonitoredStreamType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 3, 1, 1, 2),
    _CtpcStatMonitoredStreamType_Type()
)
ctpcStatMonitoredStreamType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpcStatMonitoredStreamType.setStatus("current")
_CtpcStatMonitoredUnit_Type = CtpcStatMonitoredAttributeUnit
_CtpcStatMonitoredUnit_Object = MibTableColumn
ctpcStatMonitoredUnit = _CtpcStatMonitoredUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 3, 1, 1, 3),
    _CtpcStatMonitoredUnit_Type()
)
ctpcStatMonitoredUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStatMonitoredUnit.setStatus("current")
_CtpcStatRisingThreshold_Type = Unsigned32
_CtpcStatRisingThreshold_Object = MibTableColumn
ctpcStatRisingThreshold = _CtpcStatRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 3, 1, 1, 4),
    _CtpcStatRisingThreshold_Type()
)
ctpcStatRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcStatRisingThreshold.setStatus("current")
_CtpcStatFallingThreshold_Type = Unsigned32
_CtpcStatFallingThreshold_Object = MibTableColumn
ctpcStatFallingThreshold = _CtpcStatFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 3, 1, 1, 5),
    _CtpcStatFallingThreshold_Type()
)
ctpcStatFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcStatFallingThreshold.setStatus("current")


class _CtpcStatStartupAlarm_Type(CtpcStatAlarmMode):
    """Custom type ctpcStatStartupAlarm based on CtpcStatAlarmMode"""


_CtpcStatStartupAlarm_Object = MibTableColumn
ctpcStatStartupAlarm = _CtpcStatStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 3, 1, 1, 6),
    _CtpcStatStartupAlarm_Type()
)
ctpcStatStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcStatStartupAlarm.setStatus("current")
_CtpcStatMonitoredStatus_Type = RowStatus
_CtpcStatMonitoredStatus_Object = MibTableColumn
ctpcStatMonitoredStatus = _CtpcStatMonitoredStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 3, 1, 1, 7),
    _CtpcStatMonitoredStatus_Type()
)
ctpcStatMonitoredStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcStatMonitoredStatus.setStatus("current")
_CtpcStatObjects_ObjectIdentity = ObjectIdentity
ctpcStatObjects = _CtpcStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4)
)
_CtpcStatOverallCalls_Type = Unsigned32
_CtpcStatOverallCalls_Object = MibScalar
ctpcStatOverallCalls = _CtpcStatOverallCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 1),
    _CtpcStatOverallCalls_Type()
)
ctpcStatOverallCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStatOverallCalls.setStatus("current")
_CtpcStatOverallCallTime_Type = Unsigned32
_CtpcStatOverallCallTime_Object = MibScalar
ctpcStatOverallCallTime = _CtpcStatOverallCallTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 2),
    _CtpcStatOverallCallTime_Type()
)
ctpcStatOverallCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStatOverallCallTime.setStatus("current")
if mibBuilder.loadTexts:
    ctpcStatOverallCallTime.setUnits("seconds")
_CtpcStatTotalCalls_Type = Unsigned32
_CtpcStatTotalCalls_Object = MibScalar
ctpcStatTotalCalls = _CtpcStatTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 3),
    _CtpcStatTotalCalls_Type()
)
ctpcStatTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStatTotalCalls.setStatus("current")
_CtpcStatTotalCallTime_Type = Unsigned32
_CtpcStatTotalCallTime_Object = MibScalar
ctpcStatTotalCallTime = _CtpcStatTotalCallTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 4),
    _CtpcStatTotalCallTime_Type()
)
ctpcStatTotalCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStatTotalCallTime.setStatus("current")
if mibBuilder.loadTexts:
    ctpcStatTotalCallTime.setUnits("seconds")


class _CtpcSamplePeriod_Type(Unsigned32):
    """Custom type ctpcSamplePeriod based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CtpcSamplePeriod_Type.__name__ = "Unsigned32"
_CtpcSamplePeriod_Object = MibScalar
ctpcSamplePeriod = _CtpcSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 5),
    _CtpcSamplePeriod_Type()
)
ctpcSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpcSamplePeriod.setStatus("current")
if mibBuilder.loadTexts:
    ctpcSamplePeriod.setUnits("seconds")


class _CtpcTableSize_Type(Integer32):
    """Custom type ctpcTableSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500),
    )


_CtpcTableSize_Type.__name__ = "Integer32"
_CtpcTableSize_Object = MibScalar
ctpcTableSize = _CtpcTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 6),
    _CtpcTableSize_Type()
)
ctpcTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpcTableSize.setStatus("current")


class _CtpcTableLastIndex_Type(Unsigned32):
    """Custom type ctpcTableLastIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CtpcTableLastIndex_Type.__name__ = "Unsigned32"
_CtpcTableLastIndex_Object = MibScalar
ctpcTableLastIndex = _CtpcTableLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 7),
    _CtpcTableLastIndex_Type()
)
ctpcTableLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTableLastIndex.setStatus("current")
_CtpcTable_Object = MibTable
ctpcTable = _CtpcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8)
)
if mibBuilder.loadTexts:
    ctpcTable.setStatus("current")
_CtpcEntry_Object = MibTableRow
ctpcEntry = _CtpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1)
)
ctpcEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcIndex"),
)
if mibBuilder.loadTexts:
    ctpcEntry.setStatus("current")


class _CtpcIndex_Type(Unsigned32):
    """Custom type ctpcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CtpcIndex_Type.__name__ = "Unsigned32"
_CtpcIndex_Object = MibTableColumn
ctpcIndex = _CtpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 1),
    _CtpcIndex_Type()
)
ctpcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpcIndex.setStatus("current")
_CtpcRemoteDirNum_Type = CtpcE164Address
_CtpcRemoteDirNum_Object = MibTableColumn
ctpcRemoteDirNum = _CtpcRemoteDirNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 2),
    _CtpcRemoteDirNum_Type()
)
ctpcRemoteDirNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcRemoteDirNum.setStatus("current")


class _CtpcLocalSIPCallId_Type(SnmpAdminString):
    """Custom type ctpcLocalSIPCallId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtpcLocalSIPCallId_Type.__name__ = "SnmpAdminString"
_CtpcLocalSIPCallId_Object = MibTableColumn
ctpcLocalSIPCallId = _CtpcLocalSIPCallId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 3),
    _CtpcLocalSIPCallId_Type()
)
ctpcLocalSIPCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcLocalSIPCallId.setStatus("current")
_CtpcTxDestAddrType_Type = InetAddressType
_CtpcTxDestAddrType_Object = MibTableColumn
ctpcTxDestAddrType = _CtpcTxDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 4),
    _CtpcTxDestAddrType_Type()
)
ctpcTxDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxDestAddrType.setStatus("current")
_CtpcTxDestAddr_Type = InetAddress
_CtpcTxDestAddr_Object = MibTableColumn
ctpcTxDestAddr = _CtpcTxDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 5),
    _CtpcTxDestAddr_Type()
)
ctpcTxDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxDestAddr.setStatus("current")
_CtpcStartDateAndTime_Type = DateAndTime
_CtpcStartDateAndTime_Object = MibTableColumn
ctpcStartDateAndTime = _CtpcStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 6),
    _CtpcStartDateAndTime_Type()
)
ctpcStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStartDateAndTime.setStatus("current")
_CtpcDuration_Type = Unsigned32
_CtpcDuration_Object = MibTableColumn
ctpcDuration = _CtpcDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 7),
    _CtpcDuration_Type()
)
ctpcDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcDuration.setStatus("current")
if mibBuilder.loadTexts:
    ctpcDuration.setUnits("seconds")


class _CtpcType_Type(Integer32):
    """Custom type ctpcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("audioOnly", 2),
          ("audioVideo", 1),
          ("unknown", 3))
    )


_CtpcType_Type.__name__ = "Integer32"
_CtpcType_Object = MibTableColumn
ctpcType = _CtpcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 8),
    _CtpcType_Type()
)
ctpcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcType.setStatus("current")


class _CtpcSecurity_Type(Integer32):
    """Custom type ctpcSecurity based on Integer32"""
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
        *(("authenticated", 2),
          ("nonSecured", 1),
          ("secured", 3),
          ("unknown", 4))
    )


_CtpcSecurity_Type.__name__ = "Integer32"
_CtpcSecurity_Object = MibTableColumn
ctpcSecurity = _CtpcSecurity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 9),
    _CtpcSecurity_Type()
)
ctpcSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcSecurity.setStatus("current")


class _CtpcDirection_Type(Integer32):
    """Custom type ctpcDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2),
          ("unknown", 3))
    )


_CtpcDirection_Type.__name__ = "Integer32"
_CtpcDirection_Object = MibTableColumn
ctpcDirection = _CtpcDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 10),
    _CtpcDirection_Type()
)
ctpcDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcDirection.setStatus("current")
_CtpcState_Type = CtpcStateCode
_CtpcState_Object = MibTableColumn
ctpcState = _CtpcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 11),
    _CtpcState_Type()
)
ctpcState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcState.setStatus("current")
_CtpcInitialBitRate_Type = Unsigned32
_CtpcInitialBitRate_Object = MibTableColumn
ctpcInitialBitRate = _CtpcInitialBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 12),
    _CtpcInitialBitRate_Type()
)
ctpcInitialBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcInitialBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ctpcInitialBitRate.setUnits("kbps")
_CtpcLatestBitRate_Type = Unsigned32
_CtpcLatestBitRate_Object = MibTableColumn
ctpcLatestBitRate = _CtpcLatestBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 13),
    _CtpcLatestBitRate_Type()
)
ctpcLatestBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcLatestBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ctpcLatestBitRate.setUnits("kbps")
_CtpcRowStatus_Type = RowStatus
_CtpcRowStatus_Object = MibTableColumn
ctpcRowStatus = _CtpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 14),
    _CtpcRowStatus_Type()
)
ctpcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcRowStatus.setStatus("current")
_CtpcAttributes_Type = CtpcAttributes
_CtpcAttributes_Object = MibTableColumn
ctpcAttributes = _CtpcAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 15),
    _CtpcAttributes_Type()
)
ctpcAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcAttributes.setStatus("current")
_CtpcRemoteDevice_Type = CtpcRemoteDeviceType
_CtpcRemoteDevice_Object = MibTableColumn
ctpcRemoteDevice = _CtpcRemoteDevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 16),
    _CtpcRemoteDevice_Type()
)
ctpcRemoteDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRemoteDevice.setStatus("current")
_CtpcCallTermReason_Type = CtpcCallTerminationCode
_CtpcCallTermReason_Object = MibTableColumn
ctpcCallTermReason = _CtpcCallTermReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 8, 1, 17),
    _CtpcCallTermReason_Type()
)
ctpcCallTermReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcCallTermReason.setStatus("current")
_CtpcStatStreamTypeTable_Object = MibTable
ctpcStatStreamTypeTable = _CtpcStatStreamTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9)
)
if mibBuilder.loadTexts:
    ctpcStatStreamTypeTable.setStatus("current")
_CtpcStatStreamTypeEntry_Object = MibTableRow
ctpcStatStreamTypeEntry = _CtpcStatStreamTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1)
)
ctpcStatStreamTypeEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcIndex"),
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcStreamType"),
)
if mibBuilder.loadTexts:
    ctpcStatStreamTypeEntry.setStatus("current")
_CtpcStreamType_Type = CtpcStreamMediaType
_CtpcStreamType_Object = MibTableColumn
ctpcStreamType = _CtpcStreamType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 1),
    _CtpcStreamType_Type()
)
ctpcStreamType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpcStreamType.setStatus("current")
_CtpcAvgPeriodLatency_Type = Gauge32
_CtpcAvgPeriodLatency_Object = MibTableColumn
ctpcAvgPeriodLatency = _CtpcAvgPeriodLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 2),
    _CtpcAvgPeriodLatency_Type()
)
ctpcAvgPeriodLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcAvgPeriodLatency.setStatus("current")
if mibBuilder.loadTexts:
    ctpcAvgPeriodLatency.setUnits("milliseconds")
_CtpcAvgCallLatency_Type = Gauge32
_CtpcAvgCallLatency_Object = MibTableColumn
ctpcAvgCallLatency = _CtpcAvgCallLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 3),
    _CtpcAvgCallLatency_Type()
)
ctpcAvgCallLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcAvgCallLatency.setStatus("current")
if mibBuilder.loadTexts:
    ctpcAvgCallLatency.setUnits("milliseconds")
_CtpcMaxPeriodLatency_Type = Gauge32
_CtpcMaxPeriodLatency_Object = MibTableColumn
ctpcMaxPeriodLatency = _CtpcMaxPeriodLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 4),
    _CtpcMaxPeriodLatency_Type()
)
ctpcMaxPeriodLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMaxPeriodLatency.setStatus("current")
if mibBuilder.loadTexts:
    ctpcMaxPeriodLatency.setUnits("milliseconds")
_CtpcMaxCallLatency_Type = Gauge32
_CtpcMaxCallLatency_Object = MibTableColumn
ctpcMaxCallLatency = _CtpcMaxCallLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 5),
    _CtpcMaxCallLatency_Type()
)
ctpcMaxCallLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMaxCallLatency.setStatus("current")
if mibBuilder.loadTexts:
    ctpcMaxCallLatency.setUnits("milliseconds")
_CtpcMaxCallLatencyRecTime_Type = Unsigned32
_CtpcMaxCallLatencyRecTime_Object = MibTableColumn
ctpcMaxCallLatencyRecTime = _CtpcMaxCallLatencyRecTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 6),
    _CtpcMaxCallLatencyRecTime_Type()
)
ctpcMaxCallLatencyRecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMaxCallLatencyRecTime.setStatus("current")
if mibBuilder.loadTexts:
    ctpcMaxCallLatencyRecTime.setUnits("seconds")
_CtpcMediaSrcPort_Type = Unsigned32
_CtpcMediaSrcPort_Object = MibTableColumn
ctpcMediaSrcPort = _CtpcMediaSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 7),
    _CtpcMediaSrcPort_Type()
)
ctpcMediaSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMediaSrcPort.setStatus("current")
_CtpcMediaDestPort_Type = Unsigned32
_CtpcMediaDestPort_Object = MibTableColumn
ctpcMediaDestPort = _CtpcMediaDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 8),
    _CtpcMediaDestPort_Type()
)
ctpcMediaDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMediaDestPort.setStatus("current")
_CtpcRxDscpCurrent_Type = Dscp
_CtpcRxDscpCurrent_Object = MibTableColumn
ctpcRxDscpCurrent = _CtpcRxDscpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 9),
    _CtpcRxDscpCurrent_Type()
)
ctpcRxDscpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxDscpCurrent.setStatus("current")
_CtpcRxDscpPrevious_Type = Dscp
_CtpcRxDscpPrevious_Object = MibTableColumn
ctpcRxDscpPrevious = _CtpcRxDscpPrevious_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 10),
    _CtpcRxDscpPrevious_Type()
)
ctpcRxDscpPrevious.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxDscpPrevious.setStatus("current")
_CtpcRxCoSCurrent_Type = QosLayer2Cos
_CtpcRxCoSCurrent_Object = MibTableColumn
ctpcRxCoSCurrent = _CtpcRxCoSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 11),
    _CtpcRxCoSCurrent_Type()
)
ctpcRxCoSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxCoSCurrent.setStatus("current")
_CtpcRxCoSPrevious_Type = QosLayer2Cos
_CtpcRxCoSPrevious_Object = MibTableColumn
ctpcRxCoSPrevious = _CtpcRxCoSPrevious_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 9, 1, 12),
    _CtpcRxCoSPrevious_Type()
)
ctpcRxCoSPrevious.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxCoSPrevious.setStatus("current")
_CtpcStatStreamSourceTable_Object = MibTable
ctpcStatStreamSourceTable = _CtpcStatStreamSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10)
)
if mibBuilder.loadTexts:
    ctpcStatStreamSourceTable.setStatus("current")
_CtpcStatStreamSourceEntry_Object = MibTableRow
ctpcStatStreamSourceEntry = _CtpcStatStreamSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1)
)
ctpcStatStreamSourceEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcIndex"),
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcStreamType"),
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcStreamSource"),
)
if mibBuilder.loadTexts:
    ctpcStatStreamSourceEntry.setStatus("current")
_CtpcStreamSource_Type = CtpcStreamSourceType
_CtpcStreamSource_Object = MibTableColumn
ctpcStreamSource = _CtpcStreamSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 1),
    _CtpcStreamSource_Type()
)
ctpcStreamSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpcStreamSource.setStatus("current")
_CtpcTxActive_Type = TruthValue
_CtpcTxActive_Object = MibTableColumn
ctpcTxActive = _CtpcTxActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 2),
    _CtpcTxActive_Type()
)
ctpcTxActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxActive.setStatus("current")
_CtpcTxTotalBytes_Type = Counter64
_CtpcTxTotalBytes_Object = MibTableColumn
ctpcTxTotalBytes = _CtpcTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 3),
    _CtpcTxTotalBytes_Type()
)
ctpcTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxTotalBytes.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxTotalBytes.setUnits("bytes")
_CtpcTxTotalPackets_Type = Counter64
_CtpcTxTotalPackets_Object = MibTableColumn
ctpcTxTotalPackets = _CtpcTxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 4),
    _CtpcTxTotalPackets_Type()
)
ctpcTxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxTotalPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxTotalPackets.setUnits("packets")
_CtpcTxLostPackets_Type = Counter64
_CtpcTxLostPackets_Object = MibTableColumn
ctpcTxLostPackets = _CtpcTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 5),
    _CtpcTxLostPackets_Type()
)
ctpcTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxLostPackets.setUnits("packets")


class _CtpcTxPeriodLostPackets_Type(Gauge32):
    """Custom type ctpcTxPeriodLostPackets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CtpcTxPeriodLostPackets_Type.__name__ = "Gauge32"
_CtpcTxPeriodLostPackets_Object = MibTableColumn
ctpcTxPeriodLostPackets = _CtpcTxPeriodLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 6),
    _CtpcTxPeriodLostPackets_Type()
)
ctpcTxPeriodLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxPeriodLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxPeriodLostPackets.setUnits("micropercent")


class _CtpcTxCallLostPackets_Type(Gauge32):
    """Custom type ctpcTxCallLostPackets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CtpcTxCallLostPackets_Type.__name__ = "Gauge32"
_CtpcTxCallLostPackets_Object = MibTableColumn
ctpcTxCallLostPackets = _CtpcTxCallLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 7),
    _CtpcTxCallLostPackets_Type()
)
ctpcTxCallLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxCallLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxCallLostPackets.setUnits("micropercent")
_CtpcTxIDRPackets_Type = Counter64
_CtpcTxIDRPackets_Object = MibTableColumn
ctpcTxIDRPackets = _CtpcTxIDRPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 8),
    _CtpcTxIDRPackets_Type()
)
ctpcTxIDRPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxIDRPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxIDRPackets.setUnits("packets")
_CtpcTxShapingWindow_Type = Gauge32
_CtpcTxShapingWindow_Object = MibTableColumn
ctpcTxShapingWindow = _CtpcTxShapingWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 9),
    _CtpcTxShapingWindow_Type()
)
ctpcTxShapingWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxShapingWindow.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxShapingWindow.setUnits("milliseconds")
_CtpcRxActive_Type = TruthValue
_CtpcRxActive_Object = MibTableColumn
ctpcRxActive = _CtpcRxActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 10),
    _CtpcRxActive_Type()
)
ctpcRxActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxActive.setStatus("current")
_CtpcRxTotalBytes_Type = Counter64
_CtpcRxTotalBytes_Object = MibTableColumn
ctpcRxTotalBytes = _CtpcRxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 11),
    _CtpcRxTotalBytes_Type()
)
ctpcRxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxTotalBytes.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxTotalBytes.setUnits("bytes")
_CtpcRxTotalPackets_Type = Counter64
_CtpcRxTotalPackets_Object = MibTableColumn
ctpcRxTotalPackets = _CtpcRxTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 12),
    _CtpcRxTotalPackets_Type()
)
ctpcRxTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxTotalPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxTotalPackets.setUnits("packets")
_CtpcRxLostPackets_Type = Counter64
_CtpcRxLostPackets_Object = MibTableColumn
ctpcRxLostPackets = _CtpcRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 13),
    _CtpcRxLostPackets_Type()
)
ctpcRxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxLostPackets.setUnits("packets")


class _CtpcRxPeriodLostPackets_Type(Gauge32):
    """Custom type ctpcRxPeriodLostPackets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CtpcRxPeriodLostPackets_Type.__name__ = "Gauge32"
_CtpcRxPeriodLostPackets_Object = MibTableColumn
ctpcRxPeriodLostPackets = _CtpcRxPeriodLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 14),
    _CtpcRxPeriodLostPackets_Type()
)
ctpcRxPeriodLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxPeriodLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxPeriodLostPackets.setUnits("micropercent")


class _CtpcRxCallLostPackets_Type(Gauge32):
    """Custom type ctpcRxCallLostPackets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CtpcRxCallLostPackets_Type.__name__ = "Gauge32"
_CtpcRxCallLostPackets_Object = MibTableColumn
ctpcRxCallLostPackets = _CtpcRxCallLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 15),
    _CtpcRxCallLostPackets_Type()
)
ctpcRxCallLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxCallLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxCallLostPackets.setUnits("micropercent")
_CtpcRxOutOfOrderPackets_Type = Counter64
_CtpcRxOutOfOrderPackets_Object = MibTableColumn
ctpcRxOutOfOrderPackets = _CtpcRxOutOfOrderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 16),
    _CtpcRxOutOfOrderPackets_Type()
)
ctpcRxOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxOutOfOrderPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxOutOfOrderPackets.setUnits("packets")
_CtpcRxDuplicatePackets_Type = Counter64
_CtpcRxDuplicatePackets_Object = MibTableColumn
ctpcRxDuplicatePackets = _CtpcRxDuplicatePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 17),
    _CtpcRxDuplicatePackets_Type()
)
ctpcRxDuplicatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxDuplicatePackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxDuplicatePackets.setUnits("packets")
_CtpcRxLatePackets_Type = Counter64
_CtpcRxLatePackets_Object = MibTableColumn
ctpcRxLatePackets = _CtpcRxLatePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 18),
    _CtpcRxLatePackets_Type()
)
ctpcRxLatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxLatePackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxLatePackets.setUnits("packets")
_CtpcRxIDRPackets_Type = Counter64
_CtpcRxIDRPackets_Object = MibTableColumn
ctpcRxIDRPackets = _CtpcRxIDRPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 19),
    _CtpcRxIDRPackets_Type()
)
ctpcRxIDRPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxIDRPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxIDRPackets.setUnits("packets")
_CtpcRxShapingWindow_Type = Gauge32
_CtpcRxShapingWindow_Object = MibTableColumn
ctpcRxShapingWindow = _CtpcRxShapingWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 20),
    _CtpcRxShapingWindow_Type()
)
ctpcRxShapingWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxShapingWindow.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxShapingWindow.setUnits("milliseconds")
_CtpcRxCallAuthFailure_Type = Counter64
_CtpcRxCallAuthFailure_Object = MibTableColumn
ctpcRxCallAuthFailure = _CtpcRxCallAuthFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 21),
    _CtpcRxCallAuthFailure_Type()
)
ctpcRxCallAuthFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxCallAuthFailure.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxCallAuthFailure.setUnits("packets")
_CtpcAvgPeriodJitter_Type = Unsigned64
_CtpcAvgPeriodJitter_Object = MibTableColumn
ctpcAvgPeriodJitter = _CtpcAvgPeriodJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 22),
    _CtpcAvgPeriodJitter_Type()
)
ctpcAvgPeriodJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcAvgPeriodJitter.setStatus("current")
if mibBuilder.loadTexts:
    ctpcAvgPeriodJitter.setUnits("milliseconds")
_CtpcAvgCallJitter_Type = Unsigned64
_CtpcAvgCallJitter_Object = MibTableColumn
ctpcAvgCallJitter = _CtpcAvgCallJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 23),
    _CtpcAvgCallJitter_Type()
)
ctpcAvgCallJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcAvgCallJitter.setStatus("current")
if mibBuilder.loadTexts:
    ctpcAvgCallJitter.setUnits("milliseconds")
_CtpcMaxPeriodJitter_Type = Unsigned64
_CtpcMaxPeriodJitter_Object = MibTableColumn
ctpcMaxPeriodJitter = _CtpcMaxPeriodJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 24),
    _CtpcMaxPeriodJitter_Type()
)
ctpcMaxPeriodJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMaxPeriodJitter.setStatus("current")
if mibBuilder.loadTexts:
    ctpcMaxPeriodJitter.setUnits("milliseconds")
_CtpcMaxCallJitter_Type = Unsigned64
_CtpcMaxCallJitter_Object = MibTableColumn
ctpcMaxCallJitter = _CtpcMaxCallJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 25),
    _CtpcMaxCallJitter_Type()
)
ctpcMaxCallJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMaxCallJitter.setStatus("current")
if mibBuilder.loadTexts:
    ctpcMaxCallJitter.setUnits("milliseconds")
_CtpcMaxCallJitterRecTime_Type = Unsigned32
_CtpcMaxCallJitterRecTime_Object = MibTableColumn
ctpcMaxCallJitterRecTime = _CtpcMaxCallJitterRecTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 26),
    _CtpcMaxCallJitterRecTime_Type()
)
ctpcMaxCallJitterRecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMaxCallJitterRecTime.setStatus("current")
if mibBuilder.loadTexts:
    ctpcMaxCallJitterRecTime.setUnits("seconds")
_CtpcTxCodec_Type = CtpcCodecType
_CtpcTxCodec_Object = MibTableColumn
ctpcTxCodec = _CtpcTxCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 27),
    _CtpcTxCodec_Type()
)
ctpcTxCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxCodec.setStatus("current")
_CtpcTxFrameRate_Type = Unsigned32
_CtpcTxFrameRate_Object = MibTableColumn
ctpcTxFrameRate = _CtpcTxFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 28),
    _CtpcTxFrameRate_Type()
)
ctpcTxFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxFrameRate.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxFrameRate.setUnits("millifps")
_CtpcRxCodec_Type = CtpcCodecType
_CtpcRxCodec_Object = MibTableColumn
ctpcRxCodec = _CtpcRxCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 29),
    _CtpcRxCodec_Type()
)
ctpcRxCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxCodec.setStatus("current")
_CtpcRxFrameRate_Type = Unsigned32
_CtpcRxFrameRate_Object = MibTableColumn
ctpcRxFrameRate = _CtpcRxFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 30),
    _CtpcRxFrameRate_Type()
)
ctpcRxFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxFrameRate.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxFrameRate.setUnits("millifps")


class _CtpcTxVideoHorzPixels_Type(Gauge32):
    """Custom type ctpcTxVideoHorzPixels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtpcTxVideoHorzPixels_Type.__name__ = "Gauge32"
_CtpcTxVideoHorzPixels_Object = MibTableColumn
ctpcTxVideoHorzPixels = _CtpcTxVideoHorzPixels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 31),
    _CtpcTxVideoHorzPixels_Type()
)
ctpcTxVideoHorzPixels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxVideoHorzPixels.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxVideoHorzPixels.setUnits("pixels")


class _CtpcTxVideoVertPixels_Type(Gauge32):
    """Custom type ctpcTxVideoVertPixels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtpcTxVideoVertPixels_Type.__name__ = "Gauge32"
_CtpcTxVideoVertPixels_Object = MibTableColumn
ctpcTxVideoVertPixels = _CtpcTxVideoVertPixels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 32),
    _CtpcTxVideoVertPixels_Type()
)
ctpcTxVideoVertPixels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxVideoVertPixels.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxVideoVertPixels.setUnits("pixels")


class _CtpcRxVideoHorzPixels_Type(Gauge32):
    """Custom type ctpcRxVideoHorzPixels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtpcRxVideoHorzPixels_Type.__name__ = "Gauge32"
_CtpcRxVideoHorzPixels_Object = MibTableColumn
ctpcRxVideoHorzPixels = _CtpcRxVideoHorzPixels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 33),
    _CtpcRxVideoHorzPixels_Type()
)
ctpcRxVideoHorzPixels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxVideoHorzPixels.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxVideoHorzPixels.setUnits("pixels")


class _CtpcRxVideoVertPixels_Type(Gauge32):
    """Custom type ctpcRxVideoVertPixels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CtpcRxVideoVertPixels_Type.__name__ = "Gauge32"
_CtpcRxVideoVertPixels_Object = MibTableColumn
ctpcRxVideoVertPixels = _CtpcRxVideoVertPixels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 34),
    _CtpcRxVideoVertPixels_Type()
)
ctpcRxVideoVertPixels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxVideoVertPixels.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxVideoVertPixels.setUnits("pixels")
_CtpcTxCallBitRate_Type = Gauge32
_CtpcTxCallBitRate_Object = MibTableColumn
ctpcTxCallBitRate = _CtpcTxCallBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 35),
    _CtpcTxCallBitRate_Type()
)
ctpcTxCallBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxCallBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxCallBitRate.setUnits("Kbps")
_CtpcTxPeriodBitRate_Type = Gauge32
_CtpcTxPeriodBitRate_Object = MibTableColumn
ctpcTxPeriodBitRate = _CtpcTxPeriodBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 36),
    _CtpcTxPeriodBitRate_Type()
)
ctpcTxPeriodBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTxPeriodBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTxPeriodBitRate.setUnits("Kbps")
_CtpcRxCallBitRate_Type = Gauge32
_CtpcRxCallBitRate_Object = MibTableColumn
ctpcRxCallBitRate = _CtpcRxCallBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 37),
    _CtpcRxCallBitRate_Type()
)
ctpcRxCallBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxCallBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxCallBitRate.setUnits("Kbps")
_CtpcRxPeriodBitRate_Type = Gauge32
_CtpcRxPeriodBitRate_Object = MibTableColumn
ctpcRxPeriodBitRate = _CtpcRxPeriodBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 38),
    _CtpcRxPeriodBitRate_Type()
)
ctpcRxPeriodBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxPeriodBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxPeriodBitRate.setUnits("Kbps")


class _CtpcRxMaxPeriodLostPackets_Type(Gauge32):
    """Custom type ctpcRxMaxPeriodLostPackets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CtpcRxMaxPeriodLostPackets_Type.__name__ = "Gauge32"
_CtpcRxMaxPeriodLostPackets_Object = MibTableColumn
ctpcRxMaxPeriodLostPackets = _CtpcRxMaxPeriodLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 39),
    _CtpcRxMaxPeriodLostPackets_Type()
)
ctpcRxMaxPeriodLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxMaxPeriodLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxMaxPeriodLostPackets.setUnits("micropercent")


class _CtpcRxMaxCallLostPackets_Type(Gauge32):
    """Custom type ctpcRxMaxCallLostPackets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_CtpcRxMaxCallLostPackets_Type.__name__ = "Gauge32"
_CtpcRxMaxCallLostPackets_Object = MibTableColumn
ctpcRxMaxCallLostPackets = _CtpcRxMaxCallLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 40),
    _CtpcRxMaxCallLostPackets_Type()
)
ctpcRxMaxCallLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxMaxCallLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxMaxCallLostPackets.setUnits("micropercent")
_CtpcRxMaxCallLostPacketsRecTime_Type = Gauge32
_CtpcRxMaxCallLostPacketsRecTime_Object = MibTableColumn
ctpcRxMaxCallLostPacketsRecTime = _CtpcRxMaxCallLostPacketsRecTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 4, 10, 1, 41),
    _CtpcRxMaxCallLostPacketsRecTime_Type()
)
ctpcRxMaxCallLostPacketsRecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcRxMaxCallLostPacketsRecTime.setStatus("current")
if mibBuilder.loadTexts:
    ctpcRxMaxCallLostPacketsRecTime.setUnits("seconds")
_CtpcStatEventHistory_ObjectIdentity = ObjectIdentity
ctpcStatEventHistory = _CtpcStatEventHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 5)
)


class _CtpcStatEventHistTableSize_Type(Unsigned32):
    """Custom type ctpcStatEventHistTableSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CtpcStatEventHistTableSize_Type.__name__ = "Unsigned32"
_CtpcStatEventHistTableSize_Object = MibScalar
ctpcStatEventHistTableSize = _CtpcStatEventHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 5, 1),
    _CtpcStatEventHistTableSize_Type()
)
ctpcStatEventHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpcStatEventHistTableSize.setStatus("current")


class _CtpcStatEventHistLastIndex_Type(Unsigned32):
    """Custom type ctpcStatEventHistLastIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CtpcStatEventHistLastIndex_Type.__name__ = "Unsigned32"
_CtpcStatEventHistLastIndex_Object = MibScalar
ctpcStatEventHistLastIndex = _CtpcStatEventHistLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 5, 2),
    _CtpcStatEventHistLastIndex_Type()
)
ctpcStatEventHistLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStatEventHistLastIndex.setStatus("current")
_CtpcStatEventHistoryTable_Object = MibTable
ctpcStatEventHistoryTable = _CtpcStatEventHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ctpcStatEventHistoryTable.setStatus("current")
_CtpcStatEventHistoryEntry_Object = MibTableRow
ctpcStatEventHistoryEntry = _CtpcStatEventHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 5, 3, 1)
)
ctpcStatEventHistoryEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatEventHistoryIndex"),
)
if mibBuilder.loadTexts:
    ctpcStatEventHistoryEntry.setStatus("current")


class _CtpcStatEventHistoryIndex_Type(Unsigned32):
    """Custom type ctpcStatEventHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CtpcStatEventHistoryIndex_Type.__name__ = "Unsigned32"
_CtpcStatEventHistoryIndex_Object = MibTableColumn
ctpcStatEventHistoryIndex = _CtpcStatEventHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 5, 3, 1, 1),
    _CtpcStatEventHistoryIndex_Type()
)
ctpcStatEventHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpcStatEventHistoryIndex.setStatus("current")
_CtpcStatEventMonObjectInst_Type = VariablePointer
_CtpcStatEventMonObjectInst_Object = MibTableColumn
ctpcStatEventMonObjectInst = _CtpcStatEventMonObjectInst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 5, 3, 1, 2),
    _CtpcStatEventMonObjectInst_Type()
)
ctpcStatEventMonObjectInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStatEventMonObjectInst.setStatus("current")
_CtpcStatEventCrossedValue_Type = Unsigned64
_CtpcStatEventCrossedValue_Object = MibTableColumn
ctpcStatEventCrossedValue = _CtpcStatEventCrossedValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 5, 3, 1, 3),
    _CtpcStatEventCrossedValue_Type()
)
ctpcStatEventCrossedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStatEventCrossedValue.setStatus("current")
_CtpcStatEventCrossedType_Type = CtpcStatThreshCrossedType
_CtpcStatEventCrossedType_Object = MibTableColumn
ctpcStatEventCrossedType = _CtpcStatEventCrossedType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 5, 3, 1, 4),
    _CtpcStatEventCrossedType_Type()
)
ctpcStatEventCrossedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStatEventCrossedType.setStatus("current")
_CtpcStatEventTimeStamp_Type = TimeTicks
_CtpcStatEventTimeStamp_Object = MibTableColumn
ctpcStatEventTimeStamp = _CtpcStatEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 5, 3, 1, 5),
    _CtpcStatEventTimeStamp_Type()
)
ctpcStatEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcStatEventTimeStamp.setStatus("current")
_CtpcMgmtSysConnEventHistory_ObjectIdentity = ObjectIdentity
ctpcMgmtSysConnEventHistory = _CtpcMgmtSysConnEventHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 6)
)


class _CtpcMgmtSysConnEventHistTableSize_Type(Unsigned32):
    """Custom type ctpcMgmtSysConnEventHistTableSize based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CtpcMgmtSysConnEventHistTableSize_Type.__name__ = "Unsigned32"
_CtpcMgmtSysConnEventHistTableSize_Object = MibScalar
ctpcMgmtSysConnEventHistTableSize = _CtpcMgmtSysConnEventHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 6, 1),
    _CtpcMgmtSysConnEventHistTableSize_Type()
)
ctpcMgmtSysConnEventHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctpcMgmtSysConnEventHistTableSize.setStatus("current")


class _CtpcMgmtSysConnEventHistLastIndex_Type(Unsigned32):
    """Custom type ctpcMgmtSysConnEventHistLastIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CtpcMgmtSysConnEventHistLastIndex_Type.__name__ = "Unsigned32"
_CtpcMgmtSysConnEventHistLastIndex_Object = MibScalar
ctpcMgmtSysConnEventHistLastIndex = _CtpcMgmtSysConnEventHistLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 6, 2),
    _CtpcMgmtSysConnEventHistLastIndex_Type()
)
ctpcMgmtSysConnEventHistLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMgmtSysConnEventHistLastIndex.setStatus("current")
_CtpcMgmtSysConnEventHistoryTable_Object = MibTable
ctpcMgmtSysConnEventHistoryTable = _CtpcMgmtSysConnEventHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 6, 3)
)
if mibBuilder.loadTexts:
    ctpcMgmtSysConnEventHistoryTable.setStatus("current")
_CtpcMgmtSysConnEventHistoryEntry_Object = MibTableRow
ctpcMgmtSysConnEventHistoryEntry = _CtpcMgmtSysConnEventHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 6, 3, 1)
)
ctpcMgmtSysConnEventHistoryEntry.setIndexNames(
    (0, "CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnEventHistoryIndex"),
)
if mibBuilder.loadTexts:
    ctpcMgmtSysConnEventHistoryEntry.setStatus("current")


class _CtpcMgmtSysConnEventHistoryIndex_Type(Unsigned32):
    """Custom type ctpcMgmtSysConnEventHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CtpcMgmtSysConnEventHistoryIndex_Type.__name__ = "Unsigned32"
_CtpcMgmtSysConnEventHistoryIndex_Object = MibTableColumn
ctpcMgmtSysConnEventHistoryIndex = _CtpcMgmtSysConnEventHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 6, 3, 1, 1),
    _CtpcMgmtSysConnEventHistoryIndex_Type()
)
ctpcMgmtSysConnEventHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpcMgmtSysConnEventHistoryIndex.setStatus("current")
_CtpcMgmtSysConnEventStatus_Type = CtpcMgmtSysConnStatusCode
_CtpcMgmtSysConnEventStatus_Object = MibTableColumn
ctpcMgmtSysConnEventStatus = _CtpcMgmtSysConnEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 6, 3, 1, 2),
    _CtpcMgmtSysConnEventStatus_Type()
)
ctpcMgmtSysConnEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMgmtSysConnEventStatus.setStatus("current")
_CtpcMgmtSysConnEventSIPRespCode_Type = Unsigned32
_CtpcMgmtSysConnEventSIPRespCode_Object = MibTableColumn
ctpcMgmtSysConnEventSIPRespCode = _CtpcMgmtSysConnEventSIPRespCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 6, 3, 1, 3),
    _CtpcMgmtSysConnEventSIPRespCode_Type()
)
ctpcMgmtSysConnEventSIPRespCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMgmtSysConnEventSIPRespCode.setStatus("current")
_CtpcMgmtSysConnEventTimeStamp_Type = TimeTicks
_CtpcMgmtSysConnEventTimeStamp_Object = MibTableColumn
ctpcMgmtSysConnEventTimeStamp = _CtpcMgmtSysConnEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 1, 6, 3, 1, 4),
    _CtpcMgmtSysConnEventTimeStamp_Type()
)
ctpcMgmtSysConnEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcMgmtSysConnEventTimeStamp.setStatus("current")
_CiscoTelepresenceCallMIBConform_ObjectIdentity = ObjectIdentity
ciscoTelepresenceCallMIBConform = _CiscoTelepresenceCallMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2)
)
_CiscoTpCallMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTpCallMIBCompliances = _CiscoTpCallMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 1)
)
_CiscoTpCallMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTpCallMIBGroups = _CiscoTpCallMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2)
)

# Managed Objects groups

ciscoTpCallConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 1)
)
ciscoTpCallConfigurationGroup.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatNotifyEnable"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnNotifyEnable"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatMonitoredUnit"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatRisingThreshold"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatFallingThreshold"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatStartupAlarm"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatMonitoredStatus"))
)
if mibBuilder.loadTexts:
    ciscoTpCallConfigurationGroup.setStatus("current")

ciscoTpCallInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 2)
)
ciscoTpCallInformationGroup.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcLocalDirNum"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcLocalAddrType"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcLocalAddr"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcActiveMgmtSysIndex"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMode"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysAddrType"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysAddr"))
)
if mibBuilder.loadTexts:
    ciscoTpCallInformationGroup.setStatus("current")

ciscoTpCallStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 3)
)
ciscoTpCallStatisticsGroup.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatOverallCalls"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatOverallCallTime"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatTotalCalls"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatTotalCallTime"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcSamplePeriod"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTableSize"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTableLastIndex"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRemoteDirNum"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcLocalSIPCallId"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxDestAddrType"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxDestAddr"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStartDateAndTime"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcDuration"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcType"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcSecurity"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcDirection"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcState"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcInitialBitRate"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcLatestBitRate"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRowStatus"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcAvgPeriodLatency"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcAvgCallLatency"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMaxPeriodLatency"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMaxCallLatency"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMaxCallLatencyRecTime"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxActive"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxTotalBytes"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxTotalPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxLostPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxPeriodLostPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxCallLostPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxIDRPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxShapingWindow"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxActive"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxTotalBytes"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxTotalPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxLostPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxPeriodLostPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxCallLostPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxOutOfOrderPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxDuplicatePackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxLatePackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxIDRPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxShapingWindow"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxCallAuthFailure"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcAvgPeriodJitter"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcAvgCallJitter"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMaxPeriodJitter"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMaxCallJitter"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMaxCallJitterRecTime"))
)
if mibBuilder.loadTexts:
    ciscoTpCallStatisticsGroup.setStatus("current")

ciscoTpCallEventHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 4)
)
ciscoTpCallEventHistoryGroup.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatEventHistTableSize"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatEventHistLastIndex"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatEventMonObjectInst"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatEventCrossedValue"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatEventCrossedType"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatEventTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoTpCallEventHistoryGroup.setStatus("current")

ciscoTpCallMgmtSysConnEventHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 6)
)
ciscoTpCallMgmtSysConnEventHistGroup.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnEventHistTableSize"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnEventHistLastIndex"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnEventStatus"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnEventSIPRespCode"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnEventTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoTpCallMgmtSysConnEventHistGroup.setStatus("current")

ciscoTpCallInformationGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 7)
)
ciscoTpCallInformationGroupSup1.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnStatus"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysSIPRespCode"))
)
if mibBuilder.loadTexts:
    ciscoTpCallInformationGroupSup1.setStatus("current")

ciscoTpCallStatisticsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 8)
)
ciscoTpCallStatisticsGroupSup1.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcAttributes"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRemoteDevice"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxCodec"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxFrameRate"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxCodec"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxFrameRate"))
)
if mibBuilder.loadTexts:
    ciscoTpCallStatisticsGroupSup1.setStatus("current")

ciscoTpCallStatisticsGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 10)
)
ciscoTpCallStatisticsGroupSup2.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcCallTermReason"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMediaSrcPort"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMediaDestPort"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxVideoHorzPixels"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxVideoVertPixels"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxVideoHorzPixels"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxVideoVertPixels"))
)
if mibBuilder.loadTexts:
    ciscoTpCallStatisticsGroupSup2.setStatus("current")

ciscoTpCallStatisticsGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 11)
)
ciscoTpCallStatisticsGroupSup3.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxCallBitRate"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxPeriodBitRate"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxCallBitRate"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxPeriodBitRate"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxMaxPeriodLostPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxMaxCallLostPackets"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxMaxCallLostPacketsRecTime"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxDscpTelepresenceConfigured"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcTxDscpAudioConfigured"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxDscpCurrent"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxDscpPrevious"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxCoSCurrent"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcRxCoSPrevious"))
)
if mibBuilder.loadTexts:
    ciscoTpCallStatisticsGroupSup3.setStatus("current")

ciscoTpCallInformationGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 12)
)
ciscoTpCallInformationGroupSup2.setObjects(
    ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcExtNumberMask")
)
if mibBuilder.loadTexts:
    ciscoTpCallInformationGroupSup2.setStatus("current")


# Notification objects

ctpcMgmtSysConnFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 0, 1)
)
ctpcMgmtSysConnFailNotification.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysAddrType"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysAddr"))
)
if mibBuilder.loadTexts:
    ctpcMgmtSysConnFailNotification.setStatus(
        "deprecated"
    )

ctpcStatNotificaion = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 0, 2)
)
ctpcStatNotificaion.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatEventMonObjectInst"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatEventCrossedValue"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatEventCrossedType"))
)
if mibBuilder.loadTexts:
    ctpcStatNotificaion.setStatus(
        "current"
    )

ctpcMgmtSysConnEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 0, 3)
)
ctpcMgmtSysConnEventNotification.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysAddrType"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysAddr"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnStatus"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysSIPRespCode"))
)
if mibBuilder.loadTexts:
    ctpcMgmtSysConnEventNotification.setStatus(
        "current"
    )


# Notifications groups

ciscoTpCallNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 5)
)
ciscoTpCallNotificationGroup.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnFailNotification"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatNotificaion"))
)
if mibBuilder.loadTexts:
    ciscoTpCallNotificationGroup.setStatus(
        "obsolete"
    )

ciscoTpCallNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 2, 9)
)
ciscoTpCallNotificationGroupRev1.setObjects(
      *(("CISCO-TELEPRESENCE-CALL-MIB", "ctpcMgmtSysConnEventNotification"),
        ("CISCO-TELEPRESENCE-CALL-MIB", "ctpcStatNotificaion"))
)
if mibBuilder.loadTexts:
    ciscoTpCallNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTpCallMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTpCallMIBCompliance.setStatus(
        "deprecated"
    )

ciscoTpCallMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoTpCallMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoTpCallMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoTpCallMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoTpCallMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoTpCallMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoTpCallMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoTpCallMIBComplianceRev4.setStatus(
        "current"
    )

ciscoTpCallMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 644, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoTpCallMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TELEPRESENCE-CALL-MIB",
    **{"CtpcE164Address": CtpcE164Address,
       "CtpcStreamMediaType": CtpcStreamMediaType,
       "CtpcStreamSourceType": CtpcStreamSourceType,
       "CtpcStateCode": CtpcStateCode,
       "CtpcStatMonitoredAttribute": CtpcStatMonitoredAttribute,
       "CtpcStatMonitoredAttributeUnit": CtpcStatMonitoredAttributeUnit,
       "CtpcStatAlarmMode": CtpcStatAlarmMode,
       "CtpcStatThreshCrossedType": CtpcStatThreshCrossedType,
       "CtpcAttributes": CtpcAttributes,
       "CtpcRemoteDeviceType": CtpcRemoteDeviceType,
       "CtpcCodecType": CtpcCodecType,
       "CtpcMgmtSysConnStatusCode": CtpcMgmtSysConnStatusCode,
       "CtpcCallTerminationCode": CtpcCallTerminationCode,
       "ciscoTelepresenceCallMIB": ciscoTelepresenceCallMIB,
       "ciscoTelepresenceCallMIBNotifs": ciscoTelepresenceCallMIBNotifs,
       "ctpcMgmtSysConnFailNotification": ctpcMgmtSysConnFailNotification,
       "ctpcStatNotificaion": ctpcStatNotificaion,
       "ctpcMgmtSysConnEventNotification": ctpcMgmtSysConnEventNotification,
       "ciscoTelepresenceCallMIBObjects": ciscoTelepresenceCallMIBObjects,
       "ctpcObjects": ctpcObjects,
       "ctpcStatNotifyEnable": ctpcStatNotifyEnable,
       "ctpcMgmtSysConnNotifyEnable": ctpcMgmtSysConnNotifyEnable,
       "ctpcInfoObjects": ctpcInfoObjects,
       "ctpcLocalAddrType": ctpcLocalAddrType,
       "ctpcLocalAddr": ctpcLocalAddr,
       "ctpcLocalDirNumTable": ctpcLocalDirNumTable,
       "ctpcLocalDirNumEntry": ctpcLocalDirNumEntry,
       "ctpcLocalDirNumIndex": ctpcLocalDirNumIndex,
       "ctpcLocalDirNum": ctpcLocalDirNum,
       "ctpcExtNumberMask": ctpcExtNumberMask,
       "ctpcMode": ctpcMode,
       "ctpcActiveMgmtSysIndex": ctpcActiveMgmtSysIndex,
       "ctpcMgmtSysTable": ctpcMgmtSysTable,
       "ctpcMgmtSysEntry": ctpcMgmtSysEntry,
       "ctpcMgmtSysIndex": ctpcMgmtSysIndex,
       "ctpcMgmtSysAddrType": ctpcMgmtSysAddrType,
       "ctpcMgmtSysAddr": ctpcMgmtSysAddr,
       "ctpcMgmtSysConnStatus": ctpcMgmtSysConnStatus,
       "ctpcMgmtSysSIPRespCode": ctpcMgmtSysSIPRespCode,
       "ctpcTxDscpTelepresenceConfigured": ctpcTxDscpTelepresenceConfigured,
       "ctpcTxDscpAudioConfigured": ctpcTxDscpAudioConfigured,
       "ctpcStatMonitorObjects": ctpcStatMonitorObjects,
       "ctpcStatMonitoredTable": ctpcStatMonitoredTable,
       "ctpcStatMonitoredEntry": ctpcStatMonitoredEntry,
       "ctpcStatMonitoredType": ctpcStatMonitoredType,
       "ctpcStatMonitoredStreamType": ctpcStatMonitoredStreamType,
       "ctpcStatMonitoredUnit": ctpcStatMonitoredUnit,
       "ctpcStatRisingThreshold": ctpcStatRisingThreshold,
       "ctpcStatFallingThreshold": ctpcStatFallingThreshold,
       "ctpcStatStartupAlarm": ctpcStatStartupAlarm,
       "ctpcStatMonitoredStatus": ctpcStatMonitoredStatus,
       "ctpcStatObjects": ctpcStatObjects,
       "ctpcStatOverallCalls": ctpcStatOverallCalls,
       "ctpcStatOverallCallTime": ctpcStatOverallCallTime,
       "ctpcStatTotalCalls": ctpcStatTotalCalls,
       "ctpcStatTotalCallTime": ctpcStatTotalCallTime,
       "ctpcSamplePeriod": ctpcSamplePeriod,
       "ctpcTableSize": ctpcTableSize,
       "ctpcTableLastIndex": ctpcTableLastIndex,
       "ctpcTable": ctpcTable,
       "ctpcEntry": ctpcEntry,
       "ctpcIndex": ctpcIndex,
       "ctpcRemoteDirNum": ctpcRemoteDirNum,
       "ctpcLocalSIPCallId": ctpcLocalSIPCallId,
       "ctpcTxDestAddrType": ctpcTxDestAddrType,
       "ctpcTxDestAddr": ctpcTxDestAddr,
       "ctpcStartDateAndTime": ctpcStartDateAndTime,
       "ctpcDuration": ctpcDuration,
       "ctpcType": ctpcType,
       "ctpcSecurity": ctpcSecurity,
       "ctpcDirection": ctpcDirection,
       "ctpcState": ctpcState,
       "ctpcInitialBitRate": ctpcInitialBitRate,
       "ctpcLatestBitRate": ctpcLatestBitRate,
       "ctpcRowStatus": ctpcRowStatus,
       "ctpcAttributes": ctpcAttributes,
       "ctpcRemoteDevice": ctpcRemoteDevice,
       "ctpcCallTermReason": ctpcCallTermReason,
       "ctpcStatStreamTypeTable": ctpcStatStreamTypeTable,
       "ctpcStatStreamTypeEntry": ctpcStatStreamTypeEntry,
       "ctpcStreamType": ctpcStreamType,
       "ctpcAvgPeriodLatency": ctpcAvgPeriodLatency,
       "ctpcAvgCallLatency": ctpcAvgCallLatency,
       "ctpcMaxPeriodLatency": ctpcMaxPeriodLatency,
       "ctpcMaxCallLatency": ctpcMaxCallLatency,
       "ctpcMaxCallLatencyRecTime": ctpcMaxCallLatencyRecTime,
       "ctpcMediaSrcPort": ctpcMediaSrcPort,
       "ctpcMediaDestPort": ctpcMediaDestPort,
       "ctpcRxDscpCurrent": ctpcRxDscpCurrent,
       "ctpcRxDscpPrevious": ctpcRxDscpPrevious,
       "ctpcRxCoSCurrent": ctpcRxCoSCurrent,
       "ctpcRxCoSPrevious": ctpcRxCoSPrevious,
       "ctpcStatStreamSourceTable": ctpcStatStreamSourceTable,
       "ctpcStatStreamSourceEntry": ctpcStatStreamSourceEntry,
       "ctpcStreamSource": ctpcStreamSource,
       "ctpcTxActive": ctpcTxActive,
       "ctpcTxTotalBytes": ctpcTxTotalBytes,
       "ctpcTxTotalPackets": ctpcTxTotalPackets,
       "ctpcTxLostPackets": ctpcTxLostPackets,
       "ctpcTxPeriodLostPackets": ctpcTxPeriodLostPackets,
       "ctpcTxCallLostPackets": ctpcTxCallLostPackets,
       "ctpcTxIDRPackets": ctpcTxIDRPackets,
       "ctpcTxShapingWindow": ctpcTxShapingWindow,
       "ctpcRxActive": ctpcRxActive,
       "ctpcRxTotalBytes": ctpcRxTotalBytes,
       "ctpcRxTotalPackets": ctpcRxTotalPackets,
       "ctpcRxLostPackets": ctpcRxLostPackets,
       "ctpcRxPeriodLostPackets": ctpcRxPeriodLostPackets,
       "ctpcRxCallLostPackets": ctpcRxCallLostPackets,
       "ctpcRxOutOfOrderPackets": ctpcRxOutOfOrderPackets,
       "ctpcRxDuplicatePackets": ctpcRxDuplicatePackets,
       "ctpcRxLatePackets": ctpcRxLatePackets,
       "ctpcRxIDRPackets": ctpcRxIDRPackets,
       "ctpcRxShapingWindow": ctpcRxShapingWindow,
       "ctpcRxCallAuthFailure": ctpcRxCallAuthFailure,
       "ctpcAvgPeriodJitter": ctpcAvgPeriodJitter,
       "ctpcAvgCallJitter": ctpcAvgCallJitter,
       "ctpcMaxPeriodJitter": ctpcMaxPeriodJitter,
       "ctpcMaxCallJitter": ctpcMaxCallJitter,
       "ctpcMaxCallJitterRecTime": ctpcMaxCallJitterRecTime,
       "ctpcTxCodec": ctpcTxCodec,
       "ctpcTxFrameRate": ctpcTxFrameRate,
       "ctpcRxCodec": ctpcRxCodec,
       "ctpcRxFrameRate": ctpcRxFrameRate,
       "ctpcTxVideoHorzPixels": ctpcTxVideoHorzPixels,
       "ctpcTxVideoVertPixels": ctpcTxVideoVertPixels,
       "ctpcRxVideoHorzPixels": ctpcRxVideoHorzPixels,
       "ctpcRxVideoVertPixels": ctpcRxVideoVertPixels,
       "ctpcTxCallBitRate": ctpcTxCallBitRate,
       "ctpcTxPeriodBitRate": ctpcTxPeriodBitRate,
       "ctpcRxCallBitRate": ctpcRxCallBitRate,
       "ctpcRxPeriodBitRate": ctpcRxPeriodBitRate,
       "ctpcRxMaxPeriodLostPackets": ctpcRxMaxPeriodLostPackets,
       "ctpcRxMaxCallLostPackets": ctpcRxMaxCallLostPackets,
       "ctpcRxMaxCallLostPacketsRecTime": ctpcRxMaxCallLostPacketsRecTime,
       "ctpcStatEventHistory": ctpcStatEventHistory,
       "ctpcStatEventHistTableSize": ctpcStatEventHistTableSize,
       "ctpcStatEventHistLastIndex": ctpcStatEventHistLastIndex,
       "ctpcStatEventHistoryTable": ctpcStatEventHistoryTable,
       "ctpcStatEventHistoryEntry": ctpcStatEventHistoryEntry,
       "ctpcStatEventHistoryIndex": ctpcStatEventHistoryIndex,
       "ctpcStatEventMonObjectInst": ctpcStatEventMonObjectInst,
       "ctpcStatEventCrossedValue": ctpcStatEventCrossedValue,
       "ctpcStatEventCrossedType": ctpcStatEventCrossedType,
       "ctpcStatEventTimeStamp": ctpcStatEventTimeStamp,
       "ctpcMgmtSysConnEventHistory": ctpcMgmtSysConnEventHistory,
       "ctpcMgmtSysConnEventHistTableSize": ctpcMgmtSysConnEventHistTableSize,
       "ctpcMgmtSysConnEventHistLastIndex": ctpcMgmtSysConnEventHistLastIndex,
       "ctpcMgmtSysConnEventHistoryTable": ctpcMgmtSysConnEventHistoryTable,
       "ctpcMgmtSysConnEventHistoryEntry": ctpcMgmtSysConnEventHistoryEntry,
       "ctpcMgmtSysConnEventHistoryIndex": ctpcMgmtSysConnEventHistoryIndex,
       "ctpcMgmtSysConnEventStatus": ctpcMgmtSysConnEventStatus,
       "ctpcMgmtSysConnEventSIPRespCode": ctpcMgmtSysConnEventSIPRespCode,
       "ctpcMgmtSysConnEventTimeStamp": ctpcMgmtSysConnEventTimeStamp,
       "ciscoTelepresenceCallMIBConform": ciscoTelepresenceCallMIBConform,
       "ciscoTpCallMIBCompliances": ciscoTpCallMIBCompliances,
       "ciscoTpCallMIBCompliance": ciscoTpCallMIBCompliance,
       "ciscoTpCallMIBComplianceRev1": ciscoTpCallMIBComplianceRev1,
       "ciscoTpCallMIBComplianceRev2": ciscoTpCallMIBComplianceRev2,
       "ciscoTpCallMIBComplianceRev3": ciscoTpCallMIBComplianceRev3,
       "ciscoTpCallMIBComplianceRev4": ciscoTpCallMIBComplianceRev4,
       "ciscoTpCallMIBComplianceRev5": ciscoTpCallMIBComplianceRev5,
       "ciscoTpCallMIBGroups": ciscoTpCallMIBGroups,
       "ciscoTpCallConfigurationGroup": ciscoTpCallConfigurationGroup,
       "ciscoTpCallInformationGroup": ciscoTpCallInformationGroup,
       "ciscoTpCallStatisticsGroup": ciscoTpCallStatisticsGroup,
       "ciscoTpCallEventHistoryGroup": ciscoTpCallEventHistoryGroup,
       "ciscoTpCallNotificationGroup": ciscoTpCallNotificationGroup,
       "ciscoTpCallMgmtSysConnEventHistGroup": ciscoTpCallMgmtSysConnEventHistGroup,
       "ciscoTpCallInformationGroupSup1": ciscoTpCallInformationGroupSup1,
       "ciscoTpCallStatisticsGroupSup1": ciscoTpCallStatisticsGroupSup1,
       "ciscoTpCallNotificationGroupRev1": ciscoTpCallNotificationGroupRev1,
       "ciscoTpCallStatisticsGroupSup2": ciscoTpCallStatisticsGroupSup2,
       "ciscoTpCallStatisticsGroupSup3": ciscoTpCallStatisticsGroupSup3,
       "ciscoTpCallInformationGroupSup2": ciscoTpCallInformationGroupSup2}
)
