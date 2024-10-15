# SNMP MIB module (HPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:31 2024
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

(SnaControlPointName,) = mibBuilder.importSymbols(
    "APPN-MIB",
    "SnaControlPointName")

(snanauMIB,) = mibBuilder.importSymbols(
    "SNA-NAU-MIB",
    "snanauMIB")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hprMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HprNceTypes(Bits, TextualConvention):
    status = "current"


class HprRtpCounter(Counter32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HprObjects_ObjectIdentity = ObjectIdentity
hprObjects = _HprObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6, 1)
)
_HprGlobal_ObjectIdentity = ObjectIdentity
hprGlobal = _HprGlobal_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 1)
)
_HprNodeCpName_Type = SnaControlPointName
_HprNodeCpName_Object = MibScalar
hprNodeCpName = _HprNodeCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 1, 1),
    _HprNodeCpName_Type()
)
hprNodeCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprNodeCpName.setStatus("current")


class _HprOperatorPathSwitchSupport_Type(Integer32):
    """Custom type hprOperatorPathSwitchSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("switchToPathSupported", 3),
          ("switchTriggerSupported", 2))
    )


_HprOperatorPathSwitchSupport_Type.__name__ = "Integer32"
_HprOperatorPathSwitchSupport_Object = MibScalar
hprOperatorPathSwitchSupport = _HprOperatorPathSwitchSupport_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 1, 2),
    _HprOperatorPathSwitchSupport_Type()
)
hprOperatorPathSwitchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprOperatorPathSwitchSupport.setStatus("current")
_HprAnrRouting_ObjectIdentity = ObjectIdentity
hprAnrRouting = _HprAnrRouting_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2)
)
_HprAnrsAssigned_Type = Counter32
_HprAnrsAssigned_Object = MibScalar
hprAnrsAssigned = _HprAnrsAssigned_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 1),
    _HprAnrsAssigned_Type()
)
hprAnrsAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprAnrsAssigned.setStatus("current")
if mibBuilder.loadTexts:
    hprAnrsAssigned.setUnits("ANR labels")


class _HprAnrCounterState_Type(Integer32):
    """Custom type hprAnrCounterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_HprAnrCounterState_Type.__name__ = "Integer32"
_HprAnrCounterState_Object = MibScalar
hprAnrCounterState = _HprAnrCounterState_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 2),
    _HprAnrCounterState_Type()
)
hprAnrCounterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hprAnrCounterState.setStatus("current")
_HprAnrCounterStateTime_Type = DateAndTime
_HprAnrCounterStateTime_Object = MibScalar
hprAnrCounterStateTime = _HprAnrCounterStateTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 3),
    _HprAnrCounterStateTime_Type()
)
hprAnrCounterStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprAnrCounterStateTime.setStatus("current")
_HprAnrRoutingTable_Object = MibTable
hprAnrRoutingTable = _HprAnrRoutingTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hprAnrRoutingTable.setStatus("current")
_HprAnrRoutingEntry_Object = MibTableRow
hprAnrRoutingEntry = _HprAnrRoutingEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1)
)
hprAnrRoutingEntry.setIndexNames(
    (0, "HPR-MIB", "hprAnrLabel"),
)
if mibBuilder.loadTexts:
    hprAnrRoutingEntry.setStatus("current")


class _HprAnrLabel_Type(OctetString):
    """Custom type hprAnrLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HprAnrLabel_Type.__name__ = "OctetString"
_HprAnrLabel_Object = MibTableColumn
hprAnrLabel = _HprAnrLabel_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 1),
    _HprAnrLabel_Type()
)
hprAnrLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprAnrLabel.setStatus("current")


class _HprAnrType_Type(Integer32):
    """Custom type hprAnrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nce", 1),
          ("tg", 2))
    )


_HprAnrType_Type.__name__ = "Integer32"
_HprAnrType_Object = MibTableColumn
hprAnrType = _HprAnrType_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 2),
    _HprAnrType_Type()
)
hprAnrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprAnrType.setStatus("current")


class _HprAnrOutTgDest_Type(DisplayString):
    """Custom type hprAnrOutTgDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 17),
    )


_HprAnrOutTgDest_Type.__name__ = "DisplayString"
_HprAnrOutTgDest_Object = MibTableColumn
hprAnrOutTgDest = _HprAnrOutTgDest_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 3),
    _HprAnrOutTgDest_Type()
)
hprAnrOutTgDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprAnrOutTgDest.setStatus("current")


class _HprAnrOutTgNum_Type(Integer32):
    """Custom type hprAnrOutTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HprAnrOutTgNum_Type.__name__ = "Integer32"
_HprAnrOutTgNum_Object = MibTableColumn
hprAnrOutTgNum = _HprAnrOutTgNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 4),
    _HprAnrOutTgNum_Type()
)
hprAnrOutTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprAnrOutTgNum.setStatus("current")
_HprAnrPacketsReceived_Type = Counter32
_HprAnrPacketsReceived_Object = MibTableColumn
hprAnrPacketsReceived = _HprAnrPacketsReceived_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 5),
    _HprAnrPacketsReceived_Type()
)
hprAnrPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprAnrPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    hprAnrPacketsReceived.setUnits("ANR packets")
_HprAnrCounterDisconTime_Type = TimeStamp
_HprAnrCounterDisconTime_Object = MibTableColumn
hprAnrCounterDisconTime = _HprAnrCounterDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 2, 4, 1, 6),
    _HprAnrCounterDisconTime_Type()
)
hprAnrCounterDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprAnrCounterDisconTime.setStatus("current")
_HprTransportUser_ObjectIdentity = ObjectIdentity
hprTransportUser = _HprTransportUser_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 3)
)
_HprNceTable_Object = MibTable
hprNceTable = _HprNceTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hprNceTable.setStatus("current")
_HprNceEntry_Object = MibTableRow
hprNceEntry = _HprNceEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1, 1)
)
hprNceEntry.setIndexNames(
    (0, "HPR-MIB", "hprNceId"),
)
if mibBuilder.loadTexts:
    hprNceEntry.setStatus("current")


class _HprNceId_Type(OctetString):
    """Custom type hprNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HprNceId_Type.__name__ = "OctetString"
_HprNceId_Object = MibTableColumn
hprNceId = _HprNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1, 1, 1),
    _HprNceId_Type()
)
hprNceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprNceId.setStatus("current")
_HprNceType_Type = HprNceTypes
_HprNceType_Object = MibTableColumn
hprNceType = _HprNceType_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1, 1, 2),
    _HprNceType_Type()
)
hprNceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprNceType.setStatus("current")
_HprNceDefault_Type = HprNceTypes
_HprNceDefault_Object = MibTableColumn
hprNceDefault = _HprNceDefault_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1, 1, 3),
    _HprNceDefault_Type()
)
hprNceDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprNceDefault.setStatus("current")


class _HprNceInstanceId_Type(OctetString):
    """Custom type hprNceInstanceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HprNceInstanceId_Type.__name__ = "OctetString"
_HprNceInstanceId_Object = MibTableColumn
hprNceInstanceId = _HprNceInstanceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 3, 1, 1, 4),
    _HprNceInstanceId_Type()
)
hprNceInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprNceInstanceId.setStatus("current")
_HprRtp_ObjectIdentity = ObjectIdentity
hprRtp = _HprRtp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4)
)
_HprRtpGlobe_ObjectIdentity = ObjectIdentity
hprRtpGlobe = _HprRtpGlobe_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 1)
)
_HprRtpGlobeConnSetups_Type = Counter32
_HprRtpGlobeConnSetups_Object = MibScalar
hprRtpGlobeConnSetups = _HprRtpGlobeConnSetups_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 1, 1),
    _HprRtpGlobeConnSetups_Type()
)
hprRtpGlobeConnSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpGlobeConnSetups.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpGlobeConnSetups.setUnits("RTP connection setups")


class _HprRtpGlobeCtrState_Type(Integer32):
    """Custom type hprRtpGlobeCtrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_HprRtpGlobeCtrState_Type.__name__ = "Integer32"
_HprRtpGlobeCtrState_Object = MibScalar
hprRtpGlobeCtrState = _HprRtpGlobeCtrState_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 1, 2),
    _HprRtpGlobeCtrState_Type()
)
hprRtpGlobeCtrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hprRtpGlobeCtrState.setStatus("current")
_HprRtpGlobeCtrStateTime_Type = DateAndTime
_HprRtpGlobeCtrStateTime_Object = MibScalar
hprRtpGlobeCtrStateTime = _HprRtpGlobeCtrStateTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 1, 3),
    _HprRtpGlobeCtrStateTime_Type()
)
hprRtpGlobeCtrStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpGlobeCtrStateTime.setStatus("current")
_HprRtpTable_Object = MibTable
hprRtpTable = _HprRtpTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hprRtpTable.setStatus("current")
_HprRtpEntry_Object = MibTableRow
hprRtpEntry = _HprRtpEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1)
)
hprRtpEntry.setIndexNames(
    (0, "HPR-MIB", "hprRtpLocNceId"),
    (0, "HPR-MIB", "hprRtpLocTcid"),
)
if mibBuilder.loadTexts:
    hprRtpEntry.setStatus("current")


class _HprRtpLocNceId_Type(OctetString):
    """Custom type hprRtpLocNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HprRtpLocNceId_Type.__name__ = "OctetString"
_HprRtpLocNceId_Object = MibTableColumn
hprRtpLocNceId = _HprRtpLocNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 1),
    _HprRtpLocNceId_Type()
)
hprRtpLocNceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprRtpLocNceId.setStatus("current")


class _HprRtpLocTcid_Type(OctetString):
    """Custom type hprRtpLocTcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HprRtpLocTcid_Type.__name__ = "OctetString"
_HprRtpLocTcid_Object = MibTableColumn
hprRtpLocTcid = _HprRtpLocTcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 2),
    _HprRtpLocTcid_Type()
)
hprRtpLocTcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprRtpLocTcid.setStatus("current")
_HprRtpRemCpName_Type = SnaControlPointName
_HprRtpRemCpName_Object = MibTableColumn
hprRtpRemCpName = _HprRtpRemCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 3),
    _HprRtpRemCpName_Type()
)
hprRtpRemCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpRemCpName.setStatus("current")


class _HprRtpRemNceId_Type(OctetString):
    """Custom type hprRtpRemNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HprRtpRemNceId_Type.__name__ = "OctetString"
_HprRtpRemNceId_Object = MibTableColumn
hprRtpRemNceId = _HprRtpRemNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 4),
    _HprRtpRemNceId_Type()
)
hprRtpRemNceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpRemNceId.setStatus("current")


class _HprRtpRemTcid_Type(OctetString):
    """Custom type hprRtpRemTcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HprRtpRemTcid_Type.__name__ = "OctetString"
_HprRtpRemTcid_Object = MibTableColumn
hprRtpRemTcid = _HprRtpRemTcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 5),
    _HprRtpRemTcid_Type()
)
hprRtpRemTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpRemTcid.setStatus("current")


class _HprRtpPathSwitchTrigger_Type(Integer32):
    """Custom type hprRtpPathSwitchTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("switchPathNow", 2))
    )


_HprRtpPathSwitchTrigger_Type.__name__ = "Integer32"
_HprRtpPathSwitchTrigger_Object = MibTableColumn
hprRtpPathSwitchTrigger = _HprRtpPathSwitchTrigger_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 6),
    _HprRtpPathSwitchTrigger_Type()
)
hprRtpPathSwitchTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hprRtpPathSwitchTrigger.setStatus("current")


class _HprRtpRscv_Type(OctetString):
    """Custom type hprRtpRscv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HprRtpRscv_Type.__name__ = "OctetString"
_HprRtpRscv_Object = MibTableColumn
hprRtpRscv = _HprRtpRscv_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 7),
    _HprRtpRscv_Type()
)
hprRtpRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpRscv.setStatus("current")


class _HprRtpTopic_Type(DisplayString):
    """Custom type hprRtpTopic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HprRtpTopic_Type.__name__ = "DisplayString"
_HprRtpTopic_Object = MibTableColumn
hprRtpTopic = _HprRtpTopic_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 8),
    _HprRtpTopic_Type()
)
hprRtpTopic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpTopic.setStatus("current")


class _HprRtpState_Type(Integer32):
    """Custom type hprRtpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("other", 99),
          ("rtpCalling", 2),
          ("rtpConnected", 3),
          ("rtpDisconnecting", 5),
          ("rtpListening", 1),
          ("rtpPathSwitching", 4))
    )


_HprRtpState_Type.__name__ = "Integer32"
_HprRtpState_Object = MibTableColumn
hprRtpState = _HprRtpState_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 9),
    _HprRtpState_Type()
)
hprRtpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpState.setStatus("current")
_HprRtpUpTime_Type = TimeTicks
_HprRtpUpTime_Object = MibTableColumn
hprRtpUpTime = _HprRtpUpTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 10),
    _HprRtpUpTime_Type()
)
hprRtpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpUpTime.setUnits("1/100ths of a second")
_HprRtpLivenessTimer_Type = Unsigned32
_HprRtpLivenessTimer_Object = MibTableColumn
hprRtpLivenessTimer = _HprRtpLivenessTimer_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 11),
    _HprRtpLivenessTimer_Type()
)
hprRtpLivenessTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpLivenessTimer.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpLivenessTimer.setUnits("1/100ths of a second")
_HprRtpShortReqTimer_Type = Unsigned32
_HprRtpShortReqTimer_Object = MibTableColumn
hprRtpShortReqTimer = _HprRtpShortReqTimer_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 12),
    _HprRtpShortReqTimer_Type()
)
hprRtpShortReqTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpShortReqTimer.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpShortReqTimer.setUnits("1/100ths of a second")
_HprRtpPathSwTimer_Type = Unsigned32
_HprRtpPathSwTimer_Object = MibTableColumn
hprRtpPathSwTimer = _HprRtpPathSwTimer_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 13),
    _HprRtpPathSwTimer_Type()
)
hprRtpPathSwTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpPathSwTimer.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpPathSwTimer.setUnits("1/100ths of a second")
_HprRtpLivenessTimeouts_Type = HprRtpCounter
_HprRtpLivenessTimeouts_Object = MibTableColumn
hprRtpLivenessTimeouts = _HprRtpLivenessTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 14),
    _HprRtpLivenessTimeouts_Type()
)
hprRtpLivenessTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpLivenessTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpLivenessTimeouts.setUnits("liveness timeouts")
_HprRtpShortReqTimeouts_Type = HprRtpCounter
_HprRtpShortReqTimeouts_Object = MibTableColumn
hprRtpShortReqTimeouts = _HprRtpShortReqTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 15),
    _HprRtpShortReqTimeouts_Type()
)
hprRtpShortReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpShortReqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpShortReqTimeouts.setUnits("short request timeouts")
_HprRtpMaxSendRate_Type = Gauge32
_HprRtpMaxSendRate_Object = MibTableColumn
hprRtpMaxSendRate = _HprRtpMaxSendRate_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 16),
    _HprRtpMaxSendRate_Type()
)
hprRtpMaxSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpMaxSendRate.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpMaxSendRate.setUnits("bytes per second")
_HprRtpMinSendRate_Type = Gauge32
_HprRtpMinSendRate_Object = MibTableColumn
hprRtpMinSendRate = _HprRtpMinSendRate_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 17),
    _HprRtpMinSendRate_Type()
)
hprRtpMinSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpMinSendRate.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpMinSendRate.setUnits("bytes per second")
_HprRtpCurSendRate_Type = Gauge32
_HprRtpCurSendRate_Object = MibTableColumn
hprRtpCurSendRate = _HprRtpCurSendRate_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 18),
    _HprRtpCurSendRate_Type()
)
hprRtpCurSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpCurSendRate.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpCurSendRate.setUnits("bytes per second")
_HprRtpSmRdTripDelay_Type = Gauge32
_HprRtpSmRdTripDelay_Object = MibTableColumn
hprRtpSmRdTripDelay = _HprRtpSmRdTripDelay_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 19),
    _HprRtpSmRdTripDelay_Type()
)
hprRtpSmRdTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpSmRdTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpSmRdTripDelay.setUnits("1/1000ths of a second")
_HprRtpSendPackets_Type = HprRtpCounter
_HprRtpSendPackets_Object = MibTableColumn
hprRtpSendPackets = _HprRtpSendPackets_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 20),
    _HprRtpSendPackets_Type()
)
hprRtpSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpSendPackets.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpSendPackets.setUnits("RTP packets")
_HprRtpRecvPackets_Type = HprRtpCounter
_HprRtpRecvPackets_Object = MibTableColumn
hprRtpRecvPackets = _HprRtpRecvPackets_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 21),
    _HprRtpRecvPackets_Type()
)
hprRtpRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpRecvPackets.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpRecvPackets.setUnits("RTP packets")
_HprRtpSendBytes_Type = HprRtpCounter
_HprRtpSendBytes_Object = MibTableColumn
hprRtpSendBytes = _HprRtpSendBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 22),
    _HprRtpSendBytes_Type()
)
hprRtpSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpSendBytes.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpSendBytes.setUnits("bytes")
_HprRtpRecvBytes_Type = HprRtpCounter
_HprRtpRecvBytes_Object = MibTableColumn
hprRtpRecvBytes = _HprRtpRecvBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 23),
    _HprRtpRecvBytes_Type()
)
hprRtpRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpRecvBytes.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpRecvBytes.setUnits("bytes")
_HprRtpRetrPackets_Type = HprRtpCounter
_HprRtpRetrPackets_Object = MibTableColumn
hprRtpRetrPackets = _HprRtpRetrPackets_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 24),
    _HprRtpRetrPackets_Type()
)
hprRtpRetrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpRetrPackets.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpRetrPackets.setUnits("RTP packets")
_HprRtpPacketsDiscarded_Type = HprRtpCounter
_HprRtpPacketsDiscarded_Object = MibTableColumn
hprRtpPacketsDiscarded = _HprRtpPacketsDiscarded_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 25),
    _HprRtpPacketsDiscarded_Type()
)
hprRtpPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpPacketsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpPacketsDiscarded.setUnits("RTP packets")
_HprRtpDetectGaps_Type = HprRtpCounter
_HprRtpDetectGaps_Object = MibTableColumn
hprRtpDetectGaps = _HprRtpDetectGaps_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 26),
    _HprRtpDetectGaps_Type()
)
hprRtpDetectGaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpDetectGaps.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpDetectGaps.setUnits("gaps")
_HprRtpRateReqSends_Type = HprRtpCounter
_HprRtpRateReqSends_Object = MibTableColumn
hprRtpRateReqSends = _HprRtpRateReqSends_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 27),
    _HprRtpRateReqSends_Type()
)
hprRtpRateReqSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpRateReqSends.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpRateReqSends.setUnits("rate requests")
_HprRtpOkErrPathSws_Type = HprRtpCounter
_HprRtpOkErrPathSws_Object = MibTableColumn
hprRtpOkErrPathSws = _HprRtpOkErrPathSws_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 28),
    _HprRtpOkErrPathSws_Type()
)
hprRtpOkErrPathSws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpOkErrPathSws.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpOkErrPathSws.setUnits("path switch attempts")
_HprRtpBadErrPathSws_Type = HprRtpCounter
_HprRtpBadErrPathSws_Object = MibTableColumn
hprRtpBadErrPathSws = _HprRtpBadErrPathSws_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 29),
    _HprRtpBadErrPathSws_Type()
)
hprRtpBadErrPathSws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpBadErrPathSws.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpBadErrPathSws.setUnits("path switch attempts")
_HprRtpOkOpPathSws_Type = HprRtpCounter
_HprRtpOkOpPathSws_Object = MibTableColumn
hprRtpOkOpPathSws = _HprRtpOkOpPathSws_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 30),
    _HprRtpOkOpPathSws_Type()
)
hprRtpOkOpPathSws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpOkOpPathSws.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpOkOpPathSws.setUnits("path switches")
_HprRtpBadOpPathSws_Type = HprRtpCounter
_HprRtpBadOpPathSws_Object = MibTableColumn
hprRtpBadOpPathSws = _HprRtpBadOpPathSws_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 31),
    _HprRtpBadOpPathSws_Type()
)
hprRtpBadOpPathSws.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpBadOpPathSws.setStatus("current")
if mibBuilder.loadTexts:
    hprRtpBadOpPathSws.setUnits("path switches")
_HprRtpCounterDisconTime_Type = TimeStamp
_HprRtpCounterDisconTime_Object = MibTableColumn
hprRtpCounterDisconTime = _HprRtpCounterDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 2, 1, 32),
    _HprRtpCounterDisconTime_Type()
)
hprRtpCounterDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpCounterDisconTime.setStatus("current")
_HprRtpStatusTable_Object = MibTable
hprRtpStatusTable = _HprRtpStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hprRtpStatusTable.setStatus("current")
_HprRtpStatusEntry_Object = MibTableRow
hprRtpStatusEntry = _HprRtpStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1)
)
hprRtpStatusEntry.setIndexNames(
    (0, "HPR-MIB", "hprRtpStatusLocNceId"),
    (0, "HPR-MIB", "hprRtpStatusLocTcid"),
    (0, "HPR-MIB", "hprRtpStatusIndex"),
)
if mibBuilder.loadTexts:
    hprRtpStatusEntry.setStatus("current")


class _HprRtpStatusLocNceId_Type(OctetString):
    """Custom type hprRtpStatusLocNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HprRtpStatusLocNceId_Type.__name__ = "OctetString"
_HprRtpStatusLocNceId_Object = MibTableColumn
hprRtpStatusLocNceId = _HprRtpStatusLocNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 1),
    _HprRtpStatusLocNceId_Type()
)
hprRtpStatusLocNceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprRtpStatusLocNceId.setStatus("current")


class _HprRtpStatusLocTcid_Type(OctetString):
    """Custom type hprRtpStatusLocTcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HprRtpStatusLocTcid_Type.__name__ = "OctetString"
_HprRtpStatusLocTcid_Object = MibTableColumn
hprRtpStatusLocTcid = _HprRtpStatusLocTcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 2),
    _HprRtpStatusLocTcid_Type()
)
hprRtpStatusLocTcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprRtpStatusLocTcid.setStatus("current")


class _HprRtpStatusIndex_Type(Unsigned32):
    """Custom type hprRtpStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HprRtpStatusIndex_Type.__name__ = "Unsigned32"
_HprRtpStatusIndex_Object = MibTableColumn
hprRtpStatusIndex = _HprRtpStatusIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 3),
    _HprRtpStatusIndex_Type()
)
hprRtpStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hprRtpStatusIndex.setStatus("current")
_HprRtpStatusStartTime_Type = DateAndTime
_HprRtpStatusStartTime_Object = MibTableColumn
hprRtpStatusStartTime = _HprRtpStatusStartTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 4),
    _HprRtpStatusStartTime_Type()
)
hprRtpStatusStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpStatusStartTime.setStatus("current")
_HprRtpStatusEndTime_Type = DateAndTime
_HprRtpStatusEndTime_Object = MibTableColumn
hprRtpStatusEndTime = _HprRtpStatusEndTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 5),
    _HprRtpStatusEndTime_Type()
)
hprRtpStatusEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpStatusEndTime.setStatus("current")
_HprRtpStatusRemCpName_Type = SnaControlPointName
_HprRtpStatusRemCpName_Object = MibTableColumn
hprRtpStatusRemCpName = _HprRtpStatusRemCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 6),
    _HprRtpStatusRemCpName_Type()
)
hprRtpStatusRemCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpStatusRemCpName.setStatus("current")


class _HprRtpStatusRemNceId_Type(OctetString):
    """Custom type hprRtpStatusRemNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HprRtpStatusRemNceId_Type.__name__ = "OctetString"
_HprRtpStatusRemNceId_Object = MibTableColumn
hprRtpStatusRemNceId = _HprRtpStatusRemNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 7),
    _HprRtpStatusRemNceId_Type()
)
hprRtpStatusRemNceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpStatusRemNceId.setStatus("current")


class _HprRtpStatusRemTcid_Type(OctetString):
    """Custom type hprRtpStatusRemTcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HprRtpStatusRemTcid_Type.__name__ = "OctetString"
_HprRtpStatusRemTcid_Object = MibTableColumn
hprRtpStatusRemTcid = _HprRtpStatusRemTcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 8),
    _HprRtpStatusRemTcid_Type()
)
hprRtpStatusRemTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpStatusRemTcid.setStatus("current")


class _HprRtpStatusNewRscv_Type(OctetString):
    """Custom type hprRtpStatusNewRscv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HprRtpStatusNewRscv_Type.__name__ = "OctetString"
_HprRtpStatusNewRscv_Object = MibTableColumn
hprRtpStatusNewRscv = _HprRtpStatusNewRscv_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 9),
    _HprRtpStatusNewRscv_Type()
)
hprRtpStatusNewRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpStatusNewRscv.setStatus("current")


class _HprRtpStatusOldRscv_Type(OctetString):
    """Custom type hprRtpStatusOldRscv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HprRtpStatusOldRscv_Type.__name__ = "OctetString"
_HprRtpStatusOldRscv_Object = MibTableColumn
hprRtpStatusOldRscv = _HprRtpStatusOldRscv_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 10),
    _HprRtpStatusOldRscv_Type()
)
hprRtpStatusOldRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpStatusOldRscv.setStatus("current")


class _HprRtpStatusCause_Type(Integer32):
    """Custom type hprRtpStatusCause based on Integer32"""
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
        *(("locLinkFail", 3),
          ("operRequest", 5),
          ("other", 1),
          ("remLinkFail", 4),
          ("rtpConnFail", 2))
    )


_HprRtpStatusCause_Type.__name__ = "Integer32"
_HprRtpStatusCause_Object = MibTableColumn
hprRtpStatusCause = _HprRtpStatusCause_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 11),
    _HprRtpStatusCause_Type()
)
hprRtpStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpStatusCause.setStatus("current")


class _HprRtpStatusLastAttemptResult_Type(Integer32):
    """Custom type hprRtpStatusLastAttemptResult based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("backoutRouteSetupReply", 6),
          ("directorySearchFailed", 3),
          ("initiatorMoving", 2),
          ("negativeRouteSetupReply", 5),
          ("otherUnsuccessful", 8),
          ("rscvCalculationFailed", 4),
          ("successful", 1),
          ("timeoutDuringFirstAttempt", 7))
    )


_HprRtpStatusLastAttemptResult_Type.__name__ = "Integer32"
_HprRtpStatusLastAttemptResult_Object = MibTableColumn
hprRtpStatusLastAttemptResult = _HprRtpStatusLastAttemptResult_Object(
    (1, 3, 6, 1, 2, 1, 34, 6, 1, 4, 3, 1, 12),
    _HprRtpStatusLastAttemptResult_Type()
)
hprRtpStatusLastAttemptResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hprRtpStatusLastAttemptResult.setStatus("current")
_HprConformance_ObjectIdentity = ObjectIdentity
hprConformance = _HprConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6, 2)
)
_HprCompliances_ObjectIdentity = ObjectIdentity
hprCompliances = _HprCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6, 2, 1)
)
_HprGroups_ObjectIdentity = ObjectIdentity
hprGroups = _HprGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 6, 2, 2)
)

# Managed Objects groups

hprGlobalConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 1)
)
hprGlobalConfGroup.setObjects(
      *(("HPR-MIB", "hprNodeCpName"),
        ("HPR-MIB", "hprOperatorPathSwitchSupport"))
)
if mibBuilder.loadTexts:
    hprGlobalConfGroup.setStatus("current")

hprAnrRoutingConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 2)
)
hprAnrRoutingConfGroup.setObjects(
      *(("HPR-MIB", "hprAnrsAssigned"),
        ("HPR-MIB", "hprAnrCounterState"),
        ("HPR-MIB", "hprAnrCounterStateTime"),
        ("HPR-MIB", "hprAnrType"),
        ("HPR-MIB", "hprAnrOutTgDest"),
        ("HPR-MIB", "hprAnrOutTgNum"),
        ("HPR-MIB", "hprAnrPacketsReceived"),
        ("HPR-MIB", "hprAnrCounterDisconTime"))
)
if mibBuilder.loadTexts:
    hprAnrRoutingConfGroup.setStatus("current")

hprTransportUserConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 3)
)
hprTransportUserConfGroup.setObjects(
      *(("HPR-MIB", "hprNceType"),
        ("HPR-MIB", "hprNceDefault"),
        ("HPR-MIB", "hprNceInstanceId"))
)
if mibBuilder.loadTexts:
    hprTransportUserConfGroup.setStatus("current")

hprRtpConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 4)
)
hprRtpConfGroup.setObjects(
      *(("HPR-MIB", "hprRtpGlobeConnSetups"),
        ("HPR-MIB", "hprRtpGlobeCtrState"),
        ("HPR-MIB", "hprRtpGlobeCtrStateTime"),
        ("HPR-MIB", "hprRtpRemCpName"),
        ("HPR-MIB", "hprRtpRemNceId"),
        ("HPR-MIB", "hprRtpRemTcid"),
        ("HPR-MIB", "hprRtpPathSwitchTrigger"),
        ("HPR-MIB", "hprRtpRscv"),
        ("HPR-MIB", "hprRtpTopic"),
        ("HPR-MIB", "hprRtpState"),
        ("HPR-MIB", "hprRtpUpTime"),
        ("HPR-MIB", "hprRtpLivenessTimer"),
        ("HPR-MIB", "hprRtpShortReqTimer"),
        ("HPR-MIB", "hprRtpPathSwTimer"),
        ("HPR-MIB", "hprRtpLivenessTimeouts"),
        ("HPR-MIB", "hprRtpShortReqTimeouts"),
        ("HPR-MIB", "hprRtpMaxSendRate"),
        ("HPR-MIB", "hprRtpMinSendRate"),
        ("HPR-MIB", "hprRtpCurSendRate"),
        ("HPR-MIB", "hprRtpSmRdTripDelay"),
        ("HPR-MIB", "hprRtpSendPackets"),
        ("HPR-MIB", "hprRtpRecvPackets"),
        ("HPR-MIB", "hprRtpSendBytes"),
        ("HPR-MIB", "hprRtpRecvBytes"),
        ("HPR-MIB", "hprRtpRetrPackets"),
        ("HPR-MIB", "hprRtpPacketsDiscarded"),
        ("HPR-MIB", "hprRtpDetectGaps"),
        ("HPR-MIB", "hprRtpRateReqSends"),
        ("HPR-MIB", "hprRtpOkErrPathSws"),
        ("HPR-MIB", "hprRtpBadErrPathSws"),
        ("HPR-MIB", "hprRtpOkOpPathSws"),
        ("HPR-MIB", "hprRtpBadOpPathSws"),
        ("HPR-MIB", "hprRtpCounterDisconTime"),
        ("HPR-MIB", "hprRtpStatusStartTime"),
        ("HPR-MIB", "hprRtpStatusEndTime"),
        ("HPR-MIB", "hprRtpStatusRemNceId"),
        ("HPR-MIB", "hprRtpStatusRemTcid"),
        ("HPR-MIB", "hprRtpStatusRemCpName"),
        ("HPR-MIB", "hprRtpStatusNewRscv"),
        ("HPR-MIB", "hprRtpStatusOldRscv"),
        ("HPR-MIB", "hprRtpStatusCause"),
        ("HPR-MIB", "hprRtpStatusLastAttemptResult"))
)
if mibBuilder.loadTexts:
    hprRtpConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hprCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hprCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPR-MIB",
    **{"HprNceTypes": HprNceTypes,
       "HprRtpCounter": HprRtpCounter,
       "hprMIB": hprMIB,
       "hprObjects": hprObjects,
       "hprGlobal": hprGlobal,
       "hprNodeCpName": hprNodeCpName,
       "hprOperatorPathSwitchSupport": hprOperatorPathSwitchSupport,
       "hprAnrRouting": hprAnrRouting,
       "hprAnrsAssigned": hprAnrsAssigned,
       "hprAnrCounterState": hprAnrCounterState,
       "hprAnrCounterStateTime": hprAnrCounterStateTime,
       "hprAnrRoutingTable": hprAnrRoutingTable,
       "hprAnrRoutingEntry": hprAnrRoutingEntry,
       "hprAnrLabel": hprAnrLabel,
       "hprAnrType": hprAnrType,
       "hprAnrOutTgDest": hprAnrOutTgDest,
       "hprAnrOutTgNum": hprAnrOutTgNum,
       "hprAnrPacketsReceived": hprAnrPacketsReceived,
       "hprAnrCounterDisconTime": hprAnrCounterDisconTime,
       "hprTransportUser": hprTransportUser,
       "hprNceTable": hprNceTable,
       "hprNceEntry": hprNceEntry,
       "hprNceId": hprNceId,
       "hprNceType": hprNceType,
       "hprNceDefault": hprNceDefault,
       "hprNceInstanceId": hprNceInstanceId,
       "hprRtp": hprRtp,
       "hprRtpGlobe": hprRtpGlobe,
       "hprRtpGlobeConnSetups": hprRtpGlobeConnSetups,
       "hprRtpGlobeCtrState": hprRtpGlobeCtrState,
       "hprRtpGlobeCtrStateTime": hprRtpGlobeCtrStateTime,
       "hprRtpTable": hprRtpTable,
       "hprRtpEntry": hprRtpEntry,
       "hprRtpLocNceId": hprRtpLocNceId,
       "hprRtpLocTcid": hprRtpLocTcid,
       "hprRtpRemCpName": hprRtpRemCpName,
       "hprRtpRemNceId": hprRtpRemNceId,
       "hprRtpRemTcid": hprRtpRemTcid,
       "hprRtpPathSwitchTrigger": hprRtpPathSwitchTrigger,
       "hprRtpRscv": hprRtpRscv,
       "hprRtpTopic": hprRtpTopic,
       "hprRtpState": hprRtpState,
       "hprRtpUpTime": hprRtpUpTime,
       "hprRtpLivenessTimer": hprRtpLivenessTimer,
       "hprRtpShortReqTimer": hprRtpShortReqTimer,
       "hprRtpPathSwTimer": hprRtpPathSwTimer,
       "hprRtpLivenessTimeouts": hprRtpLivenessTimeouts,
       "hprRtpShortReqTimeouts": hprRtpShortReqTimeouts,
       "hprRtpMaxSendRate": hprRtpMaxSendRate,
       "hprRtpMinSendRate": hprRtpMinSendRate,
       "hprRtpCurSendRate": hprRtpCurSendRate,
       "hprRtpSmRdTripDelay": hprRtpSmRdTripDelay,
       "hprRtpSendPackets": hprRtpSendPackets,
       "hprRtpRecvPackets": hprRtpRecvPackets,
       "hprRtpSendBytes": hprRtpSendBytes,
       "hprRtpRecvBytes": hprRtpRecvBytes,
       "hprRtpRetrPackets": hprRtpRetrPackets,
       "hprRtpPacketsDiscarded": hprRtpPacketsDiscarded,
       "hprRtpDetectGaps": hprRtpDetectGaps,
       "hprRtpRateReqSends": hprRtpRateReqSends,
       "hprRtpOkErrPathSws": hprRtpOkErrPathSws,
       "hprRtpBadErrPathSws": hprRtpBadErrPathSws,
       "hprRtpOkOpPathSws": hprRtpOkOpPathSws,
       "hprRtpBadOpPathSws": hprRtpBadOpPathSws,
       "hprRtpCounterDisconTime": hprRtpCounterDisconTime,
       "hprRtpStatusTable": hprRtpStatusTable,
       "hprRtpStatusEntry": hprRtpStatusEntry,
       "hprRtpStatusLocNceId": hprRtpStatusLocNceId,
       "hprRtpStatusLocTcid": hprRtpStatusLocTcid,
       "hprRtpStatusIndex": hprRtpStatusIndex,
       "hprRtpStatusStartTime": hprRtpStatusStartTime,
       "hprRtpStatusEndTime": hprRtpStatusEndTime,
       "hprRtpStatusRemCpName": hprRtpStatusRemCpName,
       "hprRtpStatusRemNceId": hprRtpStatusRemNceId,
       "hprRtpStatusRemTcid": hprRtpStatusRemTcid,
       "hprRtpStatusNewRscv": hprRtpStatusNewRscv,
       "hprRtpStatusOldRscv": hprRtpStatusOldRscv,
       "hprRtpStatusCause": hprRtpStatusCause,
       "hprRtpStatusLastAttemptResult": hprRtpStatusLastAttemptResult,
       "hprConformance": hprConformance,
       "hprCompliances": hprCompliances,
       "hprCompliance": hprCompliance,
       "hprGroups": hprGroups,
       "hprGlobalConfGroup": hprGlobalConfGroup,
       "hprAnrRoutingConfGroup": hprAnrRoutingConfGroup,
       "hprTransportUserConfGroup": hprTransportUserConfGroup,
       "hprRtpConfGroup": hprRtpConfGroup}
)
