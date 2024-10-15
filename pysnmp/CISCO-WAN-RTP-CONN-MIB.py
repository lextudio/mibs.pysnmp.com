# SNMP MIB module (CISCO-WAN-RTP-CONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-RTP-CONN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:00 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWanRtpConnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 20)
)
ciscoWanRtpConnMIB.setRevisions(
        ("2005-04-12 00:00",
         "2003-10-20 00:00",
         "2003-05-23 00:00",
         "2002-05-20 00:00",
         "2001-11-28 00:00",
         "2001-03-15 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWanRtpConnMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanRtpConnMIBObjects = _CiscoWanRtpConnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1)
)
_VismRtpConnGrp_ObjectIdentity = ObjectIdentity
vismRtpConnGrp = _VismRtpConnGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1)
)
_VismRtpConnGrpTable_Object = MibTable
vismRtpConnGrpTable = _VismRtpConnGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vismRtpConnGrpTable.setStatus("current")
_VismRtpConnGrpEntry_Object = MibTableRow
vismRtpConnGrpEntry = _VismRtpConnGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1)
)
vismRtpConnGrpEntry.setIndexNames(
    (0, "CISCO-WAN-RTP-CONN-MIB", "vismRtpConnNum"),
)
if mibBuilder.loadTexts:
    vismRtpConnGrpEntry.setStatus("current")


class _VismRtpConnNum_Type(Integer32):
    """Custom type vismRtpConnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_VismRtpConnNum_Type.__name__ = "Integer32"
_VismRtpConnNum_Object = MibTableColumn
vismRtpConnNum = _VismRtpConnNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 1),
    _VismRtpConnNum_Type()
)
vismRtpConnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vismRtpConnNum.setStatus("current")


class _VismRtpEndptNum_Type(Integer32):
    """Custom type vismRtpEndptNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_VismRtpEndptNum_Type.__name__ = "Integer32"
_VismRtpEndptNum_Object = MibTableColumn
vismRtpEndptNum = _VismRtpEndptNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 2),
    _VismRtpEndptNum_Type()
)
vismRtpEndptNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpEndptNum.setStatus("current")


class _VismRtpLocPort_Type(Integer32):
    """Custom type vismRtpLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(49648, 50142),
    )


_VismRtpLocPort_Type.__name__ = "Integer32"
_VismRtpLocPort_Object = MibTableColumn
vismRtpLocPort = _VismRtpLocPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 3),
    _VismRtpLocPort_Type()
)
vismRtpLocPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpLocPort.setStatus("current")
_VismRtpRmtIp_Type = IpAddress
_VismRtpRmtIp_Object = MibTableColumn
vismRtpRmtIp = _VismRtpRmtIp_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 4),
    _VismRtpRmtIp_Type()
)
vismRtpRmtIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpRmtIp.setStatus("current")


class _VismRtpRmtPort_Type(Integer32):
    """Custom type vismRtpRmtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16384, 50142),
    )


_VismRtpRmtPort_Type.__name__ = "Integer32"
_VismRtpRmtPort_Object = MibTableColumn
vismRtpRmtPort = _VismRtpRmtPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 5),
    _VismRtpRmtPort_Type()
)
vismRtpRmtPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpRmtPort.setStatus("current")


class _VismRtpConnMode_Type(Integer32):
    """Custom type vismRtpConnMode based on Integer32"""
    defaultValue = 3

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
        *(("inactive", 4),
          ("rcvOnly", 2),
          ("sendAndRcv", 3),
          ("sendOnly", 1))
    )


_VismRtpConnMode_Type.__name__ = "Integer32"
_VismRtpConnMode_Object = MibTableColumn
vismRtpConnMode = _VismRtpConnMode_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 6),
    _VismRtpConnMode_Type()
)
vismRtpConnMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpConnMode.setStatus("current")


class _VismRtpBearerTos_Type(Integer32):
    """Custom type vismRtpBearerTos based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismRtpBearerTos_Type.__name__ = "Integer32"
_VismRtpBearerTos_Object = MibTableColumn
vismRtpBearerTos = _VismRtpBearerTos_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 7),
    _VismRtpBearerTos_Type()
)
vismRtpBearerTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpBearerTos.setStatus("current")


class _VismRtpCodecType_Type(Integer32):
    """Custom type vismRtpCodecType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 6),
          ("g711a", 2),
          ("g711u", 1),
          ("g723ah", 12),
          ("g723al", 14),
          ("g723h", 11),
          ("g723l", 13),
          ("g726r16000", 7),
          ("g726r24000", 8),
          ("g726r32000", 3),
          ("g726r40000", 9),
          ("g729a", 4),
          ("g729ab", 5),
          ("lossless", 15))
    )


_VismRtpCodecType_Type.__name__ = "Integer32"
_VismRtpCodecType_Object = MibTableColumn
vismRtpCodecType = _VismRtpCodecType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 8),
    _VismRtpCodecType_Type()
)
vismRtpCodecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpCodecType.setStatus("current")


class _VismRtpPktPeriod_Type(Integer32):
    """Custom type vismRtpPktPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              60)
        )
    )
    namedValues = NamedValues(
        *(("fourtyms", 40),
          ("sixtyms", 60),
          ("tenms", 10),
          ("thirtyms", 30),
          ("twentyms", 20))
    )


_VismRtpPktPeriod_Type.__name__ = "Integer32"
_VismRtpPktPeriod_Object = MibTableColumn
vismRtpPktPeriod = _VismRtpPktPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 9),
    _VismRtpPktPeriod_Type()
)
vismRtpPktPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpPktPeriod.setStatus("current")


class _VismRtpVadTimer_Type(Integer32):
    """Custom type vismRtpVadTimer based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 65535),
    )


_VismRtpVadTimer_Type.__name__ = "Integer32"
_VismRtpVadTimer_Object = MibTableColumn
vismRtpVadTimer = _VismRtpVadTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 10),
    _VismRtpVadTimer_Type()
)
vismRtpVadTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpVadTimer.setStatus("current")


class _VismRtpEcanEnable_Type(TruthValue):
    """Custom type vismRtpEcanEnable based on TruthValue"""


_VismRtpEcanEnable_Object = MibTableColumn
vismRtpEcanEnable = _VismRtpEcanEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 11),
    _VismRtpEcanEnable_Type()
)
vismRtpEcanEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpEcanEnable.setStatus("current")
_VismRtpTriRedundancy_Type = TruthValue
_VismRtpTriRedundancy_Object = MibTableColumn
vismRtpTriRedundancy = _VismRtpTriRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 12),
    _VismRtpTriRedundancy_Type()
)
vismRtpTriRedundancy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpTriRedundancy.setStatus("current")


class _VismRtpDtmfTransport_Type(TruthValue):
    """Custom type vismRtpDtmfTransport based on TruthValue"""


_VismRtpDtmfTransport_Object = MibTableColumn
vismRtpDtmfTransport = _VismRtpDtmfTransport_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 13),
    _VismRtpDtmfTransport_Type()
)
vismRtpDtmfTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpDtmfTransport.setStatus("current")
_VismRtpCasTransport_Type = TruthValue
_VismRtpCasTransport_Object = MibTableColumn
vismRtpCasTransport = _VismRtpCasTransport_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 14),
    _VismRtpCasTransport_Type()
)
vismRtpCasTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpCasTransport.setStatus("current")


class _VismRtpVad_Type(TruthValue):
    """Custom type vismRtpVad based on TruthValue"""


_VismRtpVad_Object = MibTableColumn
vismRtpVad = _VismRtpVad_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 15),
    _VismRtpVad_Type()
)
vismRtpVad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpVad.setStatus("current")


class _VismRtpICSEnable_Type(TruthValue):
    """Custom type vismRtpICSEnable based on TruthValue"""


_VismRtpICSEnable_Object = MibTableColumn
vismRtpICSEnable = _VismRtpICSEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 16),
    _VismRtpICSEnable_Type()
)
vismRtpICSEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpICSEnable.setStatus("current")


class _VismRtpConnAlarmState_Type(Integer32):
    """Custom type vismRtpConnAlarmState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("failed", 2))
    )


_VismRtpConnAlarmState_Type.__name__ = "Integer32"
_VismRtpConnAlarmState_Object = MibTableColumn
vismRtpConnAlarmState = _VismRtpConnAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 17),
    _VismRtpConnAlarmState_Type()
)
vismRtpConnAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRtpConnAlarmState.setStatus("current")
_VismRtpRowStatus_Type = RowStatus
_VismRtpRowStatus_Object = MibTableColumn
vismRtpRowStatus = _VismRtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 18),
    _VismRtpRowStatus_Type()
)
vismRtpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpRowStatus.setStatus("current")


class _VismRtpLcn_Type(Integer32):
    """Custom type vismRtpLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_VismRtpLcn_Type.__name__ = "Integer32"
_VismRtpLcn_Object = MibTableColumn
vismRtpLcn = _VismRtpLcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 19),
    _VismRtpLcn_Type()
)
vismRtpLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRtpLcn.setStatus("current")


class _VismRtpFailReason_Type(Integer32):
    """Custom type vismRtpFailReason based on Integer32"""
    defaultValue = 4

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
        *(("both", 3),
          ("highLevel", 2),
          ("notFail", 4),
          ("self", 1))
    )


_VismRtpFailReason_Type.__name__ = "Integer32"
_VismRtpFailReason_Object = MibTableColumn
vismRtpFailReason = _VismRtpFailReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 20),
    _VismRtpFailReason_Type()
)
vismRtpFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRtpFailReason.setStatus("current")


class _VismRtpPayloadType_Type(Integer32):
    """Custom type vismRtpPayloadType based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_VismRtpPayloadType_Type.__name__ = "Integer32"
_VismRtpPayloadType_Object = MibTableColumn
vismRtpPayloadType = _VismRtpPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 1, 1, 1, 21),
    _VismRtpPayloadType_Type()
)
vismRtpPayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vismRtpPayloadType.setStatus("current")
_VismRtpBearerStatsGrp_ObjectIdentity = ObjectIdentity
vismRtpBearerStatsGrp = _VismRtpBearerStatsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2)
)
_VismRtpBearerStatsTable_Object = MibTable
vismRtpBearerStatsTable = _VismRtpBearerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vismRtpBearerStatsTable.setStatus("current")
_VismRtpBearerStatsEntry_Object = MibTableRow
vismRtpBearerStatsEntry = _VismRtpBearerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1)
)
vismRtpBearerStatsEntry.setIndexNames(
    (0, "CISCO-WAN-RTP-CONN-MIB", "vismRtpConnNum"),
)
if mibBuilder.loadTexts:
    vismRtpBearerStatsEntry.setStatus("current")
_VismRtpPktsSent_Type = Counter32
_VismRtpPktsSent_Object = MibTableColumn
vismRtpPktsSent = _VismRtpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 1),
    _VismRtpPktsSent_Type()
)
vismRtpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRtpPktsSent.setStatus("current")
_VismRtpPktsRcv_Type = Counter32
_VismRtpPktsRcv_Object = MibTableColumn
vismRtpPktsRcv = _VismRtpPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 2),
    _VismRtpPktsRcv_Type()
)
vismRtpPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRtpPktsRcv.setStatus("current")
_VismRtpOctsSent_Type = Counter32
_VismRtpOctsSent_Object = MibTableColumn
vismRtpOctsSent = _VismRtpOctsSent_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 3),
    _VismRtpOctsSent_Type()
)
vismRtpOctsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRtpOctsSent.setStatus("current")
_VismRtpOctsRcv_Type = Counter32
_VismRtpOctsRcv_Object = MibTableColumn
vismRtpOctsRcv = _VismRtpOctsRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 4),
    _VismRtpOctsRcv_Type()
)
vismRtpOctsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRtpOctsRcv.setStatus("current")
_VismRtpPktsLost_Type = Counter32
_VismRtpPktsLost_Object = MibTableColumn
vismRtpPktsLost = _VismRtpPktsLost_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 5),
    _VismRtpPktsLost_Type()
)
vismRtpPktsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRtpPktsLost.setStatus("current")
_VismRtpCntsCleared_Type = TruthValue
_VismRtpCntsCleared_Object = MibTableColumn
vismRtpCntsCleared = _VismRtpCntsCleared_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 6),
    _VismRtpCntsCleared_Type()
)
vismRtpCntsCleared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismRtpCntsCleared.setStatus("current")
_VismRtpInterArrivalJitter_Type = Unsigned32
_VismRtpInterArrivalJitter_Object = MibTableColumn
vismRtpInterArrivalJitter = _VismRtpInterArrivalJitter_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 7),
    _VismRtpInterArrivalJitter_Type()
)
vismRtpInterArrivalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRtpInterArrivalJitter.setStatus("current")
if mibBuilder.loadTexts:
    vismRtpInterArrivalJitter.setUnits("milliseconds")
_VismRtpLatency_Type = Unsigned32
_VismRtpLatency_Object = MibTableColumn
vismRtpLatency = _VismRtpLatency_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 1, 2, 1, 1, 8),
    _VismRtpLatency_Type()
)
vismRtpLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismRtpLatency.setStatus("current")
if mibBuilder.loadTexts:
    vismRtpLatency.setUnits("milliseconds")
_VismRtpConnNotificationPrefix_ObjectIdentity = ObjectIdentity
vismRtpConnNotificationPrefix = _VismRtpConnNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 2)
)
_VismRtpConnNotifications_ObjectIdentity = ObjectIdentity
vismRtpConnNotifications = _VismRtpConnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 2, 0)
)
_VismRtpConnMIBConformance_ObjectIdentity = ObjectIdentity
vismRtpConnMIBConformance = _VismRtpConnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 3)
)
_VismRtpConnMIBCompliances_ObjectIdentity = ObjectIdentity
vismRtpConnMIBCompliances = _VismRtpConnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 1)
)
_VismRtpConnMIBGroups_ObjectIdentity = ObjectIdentity
vismRtpConnMIBGroups = _VismRtpConnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 2)
)

# Managed Objects groups

vismRtpConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 2, 1)
)
vismRtpConnGroup.setObjects(
      *(("CISCO-WAN-RTP-CONN-MIB", "vismRtpEndptNum"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpLocPort"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpRmtIp"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpRmtPort"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpConnMode"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpBearerTos"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpCodecType"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpPktPeriod"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpVadTimer"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpEcanEnable"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpTriRedundancy"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpDtmfTransport"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpCasTransport"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpVad"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpICSEnable"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpConnAlarmState"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpRowStatus"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpLcn"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpFailReason"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpPayloadType"))
)
if mibBuilder.loadTexts:
    vismRtpConnGroup.setStatus("current")

vismRtpBearerStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 2, 2)
)
vismRtpBearerStatsGroup.setObjects(
      *(("CISCO-WAN-RTP-CONN-MIB", "vismRtpPktsSent"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpPktsRcv"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpOctsSent"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpOctsRcv"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpPktsLost"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpCntsCleared"))
)
if mibBuilder.loadTexts:
    vismRtpBearerStatsGroup.setStatus("current")

vismRtpBearerStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 2, 3)
)
vismRtpBearerStatsGroupSup1.setObjects(
      *(("CISCO-WAN-RTP-CONN-MIB", "vismRtpInterArrivalJitter"),
        ("CISCO-WAN-RTP-CONN-MIB", "vismRtpLatency"))
)
if mibBuilder.loadTexts:
    vismRtpBearerStatsGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vismRtpConnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vismRtpConnMIBCompliance.setStatus(
        "deprecated"
    )

vismRtpConnMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 20, 3, 1, 2)
)
if mibBuilder.loadTexts:
    vismRtpConnMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-RTP-CONN-MIB",
    **{"ciscoWanRtpConnMIB": ciscoWanRtpConnMIB,
       "ciscoWanRtpConnMIBObjects": ciscoWanRtpConnMIBObjects,
       "vismRtpConnGrp": vismRtpConnGrp,
       "vismRtpConnGrpTable": vismRtpConnGrpTable,
       "vismRtpConnGrpEntry": vismRtpConnGrpEntry,
       "vismRtpConnNum": vismRtpConnNum,
       "vismRtpEndptNum": vismRtpEndptNum,
       "vismRtpLocPort": vismRtpLocPort,
       "vismRtpRmtIp": vismRtpRmtIp,
       "vismRtpRmtPort": vismRtpRmtPort,
       "vismRtpConnMode": vismRtpConnMode,
       "vismRtpBearerTos": vismRtpBearerTos,
       "vismRtpCodecType": vismRtpCodecType,
       "vismRtpPktPeriod": vismRtpPktPeriod,
       "vismRtpVadTimer": vismRtpVadTimer,
       "vismRtpEcanEnable": vismRtpEcanEnable,
       "vismRtpTriRedundancy": vismRtpTriRedundancy,
       "vismRtpDtmfTransport": vismRtpDtmfTransport,
       "vismRtpCasTransport": vismRtpCasTransport,
       "vismRtpVad": vismRtpVad,
       "vismRtpICSEnable": vismRtpICSEnable,
       "vismRtpConnAlarmState": vismRtpConnAlarmState,
       "vismRtpRowStatus": vismRtpRowStatus,
       "vismRtpLcn": vismRtpLcn,
       "vismRtpFailReason": vismRtpFailReason,
       "vismRtpPayloadType": vismRtpPayloadType,
       "vismRtpBearerStatsGrp": vismRtpBearerStatsGrp,
       "vismRtpBearerStatsTable": vismRtpBearerStatsTable,
       "vismRtpBearerStatsEntry": vismRtpBearerStatsEntry,
       "vismRtpPktsSent": vismRtpPktsSent,
       "vismRtpPktsRcv": vismRtpPktsRcv,
       "vismRtpOctsSent": vismRtpOctsSent,
       "vismRtpOctsRcv": vismRtpOctsRcv,
       "vismRtpPktsLost": vismRtpPktsLost,
       "vismRtpCntsCleared": vismRtpCntsCleared,
       "vismRtpInterArrivalJitter": vismRtpInterArrivalJitter,
       "vismRtpLatency": vismRtpLatency,
       "vismRtpConnNotificationPrefix": vismRtpConnNotificationPrefix,
       "vismRtpConnNotifications": vismRtpConnNotifications,
       "vismRtpConnMIBConformance": vismRtpConnMIBConformance,
       "vismRtpConnMIBCompliances": vismRtpConnMIBCompliances,
       "vismRtpConnMIBCompliance": vismRtpConnMIBCompliance,
       "vismRtpConnMIBComplianceRev1": vismRtpConnMIBComplianceRev1,
       "vismRtpConnMIBGroups": vismRtpConnMIBGroups,
       "vismRtpConnGroup": vismRtpConnGroup,
       "vismRtpBearerStatsGroup": vismRtpBearerStatsGroup,
       "vismRtpBearerStatsGroupSup1": vismRtpBearerStatsGroupSup1}
)
