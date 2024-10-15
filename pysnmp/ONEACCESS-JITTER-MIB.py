# SNMP MIB module (ONEACCESS-JITTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-JITTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:57 2024
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

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(oacExpIMManagement,
 oacMIBModules,
 oacRequirements) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMManagement",
    "oacMIBModules",
    "oacRequirements")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

oacJitterMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 2000)
)
oacJitterMIBModule.setRevisions(
        ("2011-10-27 00:00",
         "2010-07-08 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OacJitterControlJitterType(Integer32, TextualConvention):
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
        *(("jitter-ICMP-TIMESTAMP", 1),
          ("jitter-UDP-PING", 2),
          ("jitter-UDP-PING-TIMESTAMP", 3))
    )



class OacJitterResponseSense(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("applicationSpecific", 10),
          ("busy", 5),
          ("disconnected", 2),
          ("dropped", 7),
          ("error", 16),
          ("noStatisticsAvailable", 11),
          ("notConnected", 6),
          ("ok", 1),
          ("overThreshold", 3),
          ("sequenceError", 8),
          ("timeout", 4),
          ("verifyError", 9))
    )



# MIB Managed Objects in the order of their OIDs

_OacJitterConformance_ObjectIdentity = ObjectIdentity
oacJitterConformance = _OacJitterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 2000)
)
_OacJitterGroups_ObjectIdentity = ObjectIdentity
oacJitterGroups = _OacJitterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 2000, 1)
)
_OacJitterCompliances_ObjectIdentity = ObjectIdentity
oacJitterCompliances = _OacJitterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 2000, 2)
)
_OacExpIMJitter_ObjectIdentity = ObjectIdentity
oacExpIMJitter = _OacExpIMJitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5)
)
_OacJitterObjects_ObjectIdentity = ObjectIdentity
oacJitterObjects = _OacJitterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1)
)
_OacJitterControlTable_Object = MibTable
oacJitterControlTable = _OacJitterControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1)
)
if mibBuilder.loadTexts:
    oacJitterControlTable.setStatus("current")
_OacJitterControlEntry_Object = MibTableRow
oacJitterControlEntry = _OacJitterControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1)
)
oacJitterControlEntry.setIndexNames(
    (0, "ONEACCESS-JITTER-MIB", "oacJitterControlIndex"),
)
if mibBuilder.loadTexts:
    oacJitterControlEntry.setStatus("current")


class _OacJitterControlIndex_Type(Integer32):
    """Custom type oacJitterControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OacJitterControlIndex_Type.__name__ = "Integer32"
_OacJitterControlIndex_Object = MibTableColumn
oacJitterControlIndex = _OacJitterControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 1),
    _OacJitterControlIndex_Type()
)
oacJitterControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacJitterControlIndex.setStatus("current")
_OacJitterControlOwner_Type = OwnerString
_OacJitterControlOwner_Object = MibTableColumn
oacJitterControlOwner = _OacJitterControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 2),
    _OacJitterControlOwner_Type()
)
oacJitterControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlOwner.setStatus("current")


class _OacJitterControlType_Type(OacJitterControlJitterType):
    """Custom type oacJitterControlType based on OacJitterControlJitterType"""


_OacJitterControlType_Object = MibTableColumn
oacJitterControlType = _OacJitterControlType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 3),
    _OacJitterControlType_Type()
)
oacJitterControlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlType.setStatus("current")


class _OacJitterControlFrequency_Type(Integer32):
    """Custom type oacJitterControlFrequency based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_OacJitterControlFrequency_Type.__name__ = "Integer32"
_OacJitterControlFrequency_Object = MibTableColumn
oacJitterControlFrequency = _OacJitterControlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 4),
    _OacJitterControlFrequency_Type()
)
oacJitterControlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlFrequency.setStatus("current")
if mibBuilder.loadTexts:
    oacJitterControlFrequency.setUnits("seconds")


class _OacJitterControlTimeout_Type(Integer32):
    """Custom type oacJitterControlTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_OacJitterControlTimeout_Type.__name__ = "Integer32"
_OacJitterControlTimeout_Object = MibTableColumn
oacJitterControlTimeout = _OacJitterControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 5),
    _OacJitterControlTimeout_Type()
)
oacJitterControlTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    oacJitterControlTimeout.setUnits("milliseconds")
_OacJitterControlTargetAddress_Type = InetAddress
_OacJitterControlTargetAddress_Object = MibTableColumn
oacJitterControlTargetAddress = _OacJitterControlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 6),
    _OacJitterControlTargetAddress_Type()
)
oacJitterControlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlTargetAddress.setStatus("current")
_OacJitterControlTargetPort_Type = Integer32
_OacJitterControlTargetPort_Object = MibTableColumn
oacJitterControlTargetPort = _OacJitterControlTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 7),
    _OacJitterControlTargetPort_Type()
)
oacJitterControlTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlTargetPort.setStatus("current")
_OacJitterControlSourceAddress_Type = InetAddress
_OacJitterControlSourceAddress_Object = MibTableColumn
oacJitterControlSourceAddress = _OacJitterControlSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 8),
    _OacJitterControlSourceAddress_Type()
)
oacJitterControlSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlSourceAddress.setStatus("current")
_OacJitterControlInterval_Type = Integer32
_OacJitterControlInterval_Object = MibTableColumn
oacJitterControlInterval = _OacJitterControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 9),
    _OacJitterControlInterval_Type()
)
oacJitterControlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlInterval.setStatus("current")
if mibBuilder.loadTexts:
    oacJitterControlInterval.setUnits("milliseconds")


class _OacJitterControlPktDataRequestSize_Type(Integer32):
    """Custom type oacJitterControlPktDataRequestSize based on Integer32"""
    defaultValue = 32


_OacJitterControlPktDataRequestSize_Object = MibTableColumn
oacJitterControlPktDataRequestSize = _OacJitterControlPktDataRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 10),
    _OacJitterControlPktDataRequestSize_Type()
)
oacJitterControlPktDataRequestSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlPktDataRequestSize.setStatus("current")
if mibBuilder.loadTexts:
    oacJitterControlPktDataRequestSize.setUnits("bytes")


class _OacJitterControlPacketCount_Type(Integer32):
    """Custom type oacJitterControlPacketCount based on Integer32"""
    defaultValue = 10


_OacJitterControlPacketCount_Object = MibTableColumn
oacJitterControlPacketCount = _OacJitterControlPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 11),
    _OacJitterControlPacketCount_Type()
)
oacJitterControlPacketCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlPacketCount.setStatus("current")


class _OacJitterControlTos_Type(Integer32):
    """Custom type oacJitterControlTos based on Integer32"""
    defaultValue = 0


_OacJitterControlTos_Object = MibTableColumn
oacJitterControlTos = _OacJitterControlTos_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 12),
    _OacJitterControlTos_Type()
)
oacJitterControlTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlTos.setStatus("current")
_OacJitterControlStatus_Type = RowStatus
_OacJitterControlStatus_Object = MibTableColumn
oacJitterControlStatus = _OacJitterControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 13),
    _OacJitterControlStatus_Type()
)
oacJitterControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacJitterControlStatus.setStatus("current")


class _OacJitterControlVrfName_Type(OctetString):
    """Custom type oacJitterControlVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacJitterControlVrfName_Type.__name__ = "OctetString"
_OacJitterControlVrfName_Object = MibTableColumn
oacJitterControlVrfName = _OacJitterControlVrfName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 1, 1, 14),
    _OacJitterControlVrfName_Type()
)
oacJitterControlVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacJitterControlVrfName.setStatus("current")
_OacJitterStatsTable_Object = MibTable
oacJitterStatsTable = _OacJitterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2)
)
if mibBuilder.loadTexts:
    oacJitterStatsTable.setStatus("current")
_OacJitterStatsEntry_Object = MibTableRow
oacJitterStatsEntry = _OacJitterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1)
)
oacJitterStatsEntry.setIndexNames(
    (0, "ONEACCESS-JITTER-MIB", "oacJitterControlIndex"),
)
if mibBuilder.loadTexts:
    oacJitterStatsEntry.setStatus("current")
_OacJitterStatsCompleted_Type = OacJitterResponseSense
_OacJitterStatsCompleted_Object = MibTableColumn
oacJitterStatsCompleted = _OacJitterStatsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 2),
    _OacJitterStatsCompleted_Type()
)
oacJitterStatsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsCompleted.setStatus("current")
_OacJitterStatsTime_Type = DateAndTime
_OacJitterStatsTime_Object = MibTableColumn
oacJitterStatsTime = _OacJitterStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 3),
    _OacJitterStatsTime_Type()
)
oacJitterStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsTime.setStatus("current")


class _OacJitterStatsNumRTT_Type(Integer32):
    """Custom type oacJitterStatsNumRTT based on Integer32"""
    defaultValue = 0


_OacJitterStatsNumRTT_Object = MibTableColumn
oacJitterStatsNumRTT = _OacJitterStatsNumRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 4),
    _OacJitterStatsNumRTT_Type()
)
oacJitterStatsNumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsNumRTT.setStatus("current")
_OacJitterStatsPacketRecv_Type = Integer32
_OacJitterStatsPacketRecv_Object = MibTableColumn
oacJitterStatsPacketRecv = _OacJitterStatsPacketRecv_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 5),
    _OacJitterStatsPacketRecv_Type()
)
oacJitterStatsPacketRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsPacketRecv.setStatus("current")
_OacJitterStatsAvgRTT_Type = Integer32
_OacJitterStatsAvgRTT_Object = MibTableColumn
oacJitterStatsAvgRTT = _OacJitterStatsAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 6),
    _OacJitterStatsAvgRTT_Type()
)
oacJitterStatsAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsAvgRTT.setStatus("current")
_OacJitterStatsSumRTT_Type = Integer32
_OacJitterStatsSumRTT_Object = MibTableColumn
oacJitterStatsSumRTT = _OacJitterStatsSumRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 7),
    _OacJitterStatsSumRTT_Type()
)
oacJitterStatsSumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSumRTT.setStatus("current")
_OacJitterStatsMinRTT_Type = Integer32
_OacJitterStatsMinRTT_Object = MibTableColumn
oacJitterStatsMinRTT = _OacJitterStatsMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 8),
    _OacJitterStatsMinRTT_Type()
)
oacJitterStatsMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsMinRTT.setStatus("current")
_OacJitterStatsMaxRTT_Type = Integer32
_OacJitterStatsMaxRTT_Object = MibTableColumn
oacJitterStatsMaxRTT = _OacJitterStatsMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 9),
    _OacJitterStatsMaxRTT_Type()
)
oacJitterStatsMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsMaxRTT.setStatus("current")
_OacJitterStatsSumPosJitter_Type = Integer32
_OacJitterStatsSumPosJitter_Object = MibTableColumn
oacJitterStatsSumPosJitter = _OacJitterStatsSumPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 10),
    _OacJitterStatsSumPosJitter_Type()
)
oacJitterStatsSumPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSumPosJitter.setStatus("current")
_OacJitterStatsNumPosJitter_Type = Integer32
_OacJitterStatsNumPosJitter_Object = MibTableColumn
oacJitterStatsNumPosJitter = _OacJitterStatsNumPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 11),
    _OacJitterStatsNumPosJitter_Type()
)
oacJitterStatsNumPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsNumPosJitter.setStatus("current")
_OacJitterStatsSumNegJitter_Type = Integer32
_OacJitterStatsSumNegJitter_Object = MibTableColumn
oacJitterStatsSumNegJitter = _OacJitterStatsSumNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 12),
    _OacJitterStatsSumNegJitter_Type()
)
oacJitterStatsSumNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSumNegJitter.setStatus("current")
_OacJitterStatsNumNegJitter_Type = Integer32
_OacJitterStatsNumNegJitter_Object = MibTableColumn
oacJitterStatsNumNegJitter = _OacJitterStatsNumNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 13),
    _OacJitterStatsNumNegJitter_Type()
)
oacJitterStatsNumNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsNumNegJitter.setStatus("current")
_OacJitterStatsSumPosSD_Type = Integer32
_OacJitterStatsSumPosSD_Object = MibTableColumn
oacJitterStatsSumPosSD = _OacJitterStatsSumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 14),
    _OacJitterStatsSumPosSD_Type()
)
oacJitterStatsSumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSumPosSD.setStatus("current")
_OacJitterStatsNumPosSD_Type = Integer32
_OacJitterStatsNumPosSD_Object = MibTableColumn
oacJitterStatsNumPosSD = _OacJitterStatsNumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 15),
    _OacJitterStatsNumPosSD_Type()
)
oacJitterStatsNumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsNumPosSD.setStatus("current")
_OacJitterStatsSumNegSD_Type = Integer32
_OacJitterStatsSumNegSD_Object = MibTableColumn
oacJitterStatsSumNegSD = _OacJitterStatsSumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 16),
    _OacJitterStatsSumNegSD_Type()
)
oacJitterStatsSumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSumNegSD.setStatus("current")
_OacJitterStatsNumNegSD_Type = Integer32
_OacJitterStatsNumNegSD_Object = MibTableColumn
oacJitterStatsNumNegSD = _OacJitterStatsNumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 17),
    _OacJitterStatsNumNegSD_Type()
)
oacJitterStatsNumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsNumNegSD.setStatus("current")
_OacJitterStatsSumPosDS_Type = Integer32
_OacJitterStatsSumPosDS_Object = MibTableColumn
oacJitterStatsSumPosDS = _OacJitterStatsSumPosDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 18),
    _OacJitterStatsSumPosDS_Type()
)
oacJitterStatsSumPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSumPosDS.setStatus("current")
_OacJitterStatsNumPosDS_Type = Integer32
_OacJitterStatsNumPosDS_Object = MibTableColumn
oacJitterStatsNumPosDS = _OacJitterStatsNumPosDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 19),
    _OacJitterStatsNumPosDS_Type()
)
oacJitterStatsNumPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsNumPosDS.setStatus("current")
_OacJitterStatsSumNegDS_Type = Integer32
_OacJitterStatsSumNegDS_Object = MibTableColumn
oacJitterStatsSumNegDS = _OacJitterStatsSumNegDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 20),
    _OacJitterStatsSumNegDS_Type()
)
oacJitterStatsSumNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSumNegDS.setStatus("current")
_OacJitterStatsNumNegDS_Type = Integer32
_OacJitterStatsNumNegDS_Object = MibTableColumn
oacJitterStatsNumNegDS = _OacJitterStatsNumNegDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 21),
    _OacJitterStatsNumNegDS_Type()
)
oacJitterStatsNumNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsNumNegDS.setStatus("current")


class _OacJitterStatsPacketLossSD_Type(Integer32):
    """Custom type oacJitterStatsPacketLossSD based on Integer32"""
    defaultValue = 0


_OacJitterStatsPacketLossSD_Object = MibTableColumn
oacJitterStatsPacketLossSD = _OacJitterStatsPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 22),
    _OacJitterStatsPacketLossSD_Type()
)
oacJitterStatsPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsPacketLossSD.setStatus("current")


class _OacJitterStatsPacketLossDS_Type(Integer32):
    """Custom type oacJitterStatsPacketLossDS based on Integer32"""
    defaultValue = 0


_OacJitterStatsPacketLossDS_Object = MibTableColumn
oacJitterStatsPacketLossDS = _OacJitterStatsPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 23),
    _OacJitterStatsPacketLossDS_Type()
)
oacJitterStatsPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsPacketLossDS.setStatus("current")


class _OacJitterStatsPacketOutOfSequence_Type(Integer32):
    """Custom type oacJitterStatsPacketOutOfSequence based on Integer32"""
    defaultValue = 0


_OacJitterStatsPacketOutOfSequence_Object = MibTableColumn
oacJitterStatsPacketOutOfSequence = _OacJitterStatsPacketOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 24),
    _OacJitterStatsPacketOutOfSequence_Type()
)
oacJitterStatsPacketOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsPacketOutOfSequence.setStatus("current")


class _OacJitterStatsPacketLateArrival_Type(Integer32):
    """Custom type oacJitterStatsPacketLateArrival based on Integer32"""
    defaultValue = 0


_OacJitterStatsPacketLateArrival_Object = MibTableColumn
oacJitterStatsPacketLateArrival = _OacJitterStatsPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 25),
    _OacJitterStatsPacketLateArrival_Type()
)
oacJitterStatsPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsPacketLateArrival.setStatus("current")


class _OacJitterStatsPacketLoss_Type(Integer32):
    """Custom type oacJitterStatsPacketLoss based on Integer32"""
    defaultValue = 0


_OacJitterStatsPacketLoss_Object = MibTableColumn
oacJitterStatsPacketLoss = _OacJitterStatsPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 26),
    _OacJitterStatsPacketLoss_Type()
)
oacJitterStatsPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsPacketLoss.setStatus("current")
_OacJitterStatsMaxPosSD_Type = Integer32
_OacJitterStatsMaxPosSD_Object = MibTableColumn
oacJitterStatsMaxPosSD = _OacJitterStatsMaxPosSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 27),
    _OacJitterStatsMaxPosSD_Type()
)
oacJitterStatsMaxPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsMaxPosSD.setStatus("current")
_OacJitterStatsMaxNegSD_Type = Integer32
_OacJitterStatsMaxNegSD_Object = MibTableColumn
oacJitterStatsMaxNegSD = _OacJitterStatsMaxNegSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 28),
    _OacJitterStatsMaxNegSD_Type()
)
oacJitterStatsMaxNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsMaxNegSD.setStatus("current")
_OacJitterStatsMaxPosDS_Type = Integer32
_OacJitterStatsMaxPosDS_Object = MibTableColumn
oacJitterStatsMaxPosDS = _OacJitterStatsMaxPosDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 29),
    _OacJitterStatsMaxPosDS_Type()
)
oacJitterStatsMaxPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsMaxPosDS.setStatus("current")
_OacJitterStatsMaxNegDS_Type = Integer32
_OacJitterStatsMaxNegDS_Object = MibTableColumn
oacJitterStatsMaxNegDS = _OacJitterStatsMaxNegDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 30),
    _OacJitterStatsMaxNegDS_Type()
)
oacJitterStatsMaxNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsMaxNegDS.setStatus("current")
_OacJitterStatsSum2PosSD_Type = Integer32
_OacJitterStatsSum2PosSD_Object = MibTableColumn
oacJitterStatsSum2PosSD = _OacJitterStatsSum2PosSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 31),
    _OacJitterStatsSum2PosSD_Type()
)
oacJitterStatsSum2PosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSum2PosSD.setStatus("current")
_OacJitterStatsSum2NegSD_Type = Integer32
_OacJitterStatsSum2NegSD_Object = MibTableColumn
oacJitterStatsSum2NegSD = _OacJitterStatsSum2NegSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 32),
    _OacJitterStatsSum2NegSD_Type()
)
oacJitterStatsSum2NegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSum2NegSD.setStatus("current")
_OacJitterStatsSum2PosDS_Type = Integer32
_OacJitterStatsSum2PosDS_Object = MibTableColumn
oacJitterStatsSum2PosDS = _OacJitterStatsSum2PosDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 33),
    _OacJitterStatsSum2PosDS_Type()
)
oacJitterStatsSum2PosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSum2PosDS.setStatus("current")
_OacJitterStatsSum2NegDS_Type = Integer32
_OacJitterStatsSum2NegDS_Object = MibTableColumn
oacJitterStatsSum2NegDS = _OacJitterStatsSum2NegDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 34),
    _OacJitterStatsSum2NegDS_Type()
)
oacJitterStatsSum2NegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsSum2NegDS.setStatus("current")
_OacJitterStatsDeviationSD_Type = Integer32
_OacJitterStatsDeviationSD_Object = MibTableColumn
oacJitterStatsDeviationSD = _OacJitterStatsDeviationSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 35),
    _OacJitterStatsDeviationSD_Type()
)
oacJitterStatsDeviationSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsDeviationSD.setStatus("current")
_OacJitterStatsDeviationDS_Type = Integer32
_OacJitterStatsDeviationDS_Object = MibTableColumn
oacJitterStatsDeviationDS = _OacJitterStatsDeviationDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 2, 1, 36),
    _OacJitterStatsDeviationDS_Type()
)
oacJitterStatsDeviationDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsDeviationDS.setStatus("current")
_OacJitterStatsHistoryTable_Object = MibTable
oacJitterStatsHistoryTable = _OacJitterStatsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3)
)
if mibBuilder.loadTexts:
    oacJitterStatsHistoryTable.setStatus("current")
_OacJitterStatsHistoryEntry_Object = MibTableRow
oacJitterStatsHistoryEntry = _OacJitterStatsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1)
)
oacJitterStatsHistoryEntry.setIndexNames(
    (0, "ONEACCESS-JITTER-MIB", "oacJitterControlIndex"),
    (0, "ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryIndex"),
)
if mibBuilder.loadTexts:
    oacJitterStatsHistoryEntry.setStatus("current")
_OacJitterStatsHistoryIndex_Type = Integer32
_OacJitterStatsHistoryIndex_Object = MibTableColumn
oacJitterStatsHistoryIndex = _OacJitterStatsHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 1),
    _OacJitterStatsHistoryIndex_Type()
)
oacJitterStatsHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryIndex.setStatus("current")
_OacJitterStatsHistoryCompleted_Type = OacJitterResponseSense
_OacJitterStatsHistoryCompleted_Object = MibTableColumn
oacJitterStatsHistoryCompleted = _OacJitterStatsHistoryCompleted_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 2),
    _OacJitterStatsHistoryCompleted_Type()
)
oacJitterStatsHistoryCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryCompleted.setStatus("current")
_OacJitterStatsHistoryTime_Type = DateAndTime
_OacJitterStatsHistoryTime_Object = MibTableColumn
oacJitterStatsHistoryTime = _OacJitterStatsHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 3),
    _OacJitterStatsHistoryTime_Type()
)
oacJitterStatsHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryTime.setStatus("current")


class _OacJitterStatsHistoryNumRTT_Type(Integer32):
    """Custom type oacJitterStatsHistoryNumRTT based on Integer32"""
    defaultValue = 0


_OacJitterStatsHistoryNumRTT_Object = MibTableColumn
oacJitterStatsHistoryNumRTT = _OacJitterStatsHistoryNumRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 4),
    _OacJitterStatsHistoryNumRTT_Type()
)
oacJitterStatsHistoryNumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryNumRTT.setStatus("current")
_OacJitterStatsHistoryPacketRecv_Type = Integer32
_OacJitterStatsHistoryPacketRecv_Object = MibTableColumn
oacJitterStatsHistoryPacketRecv = _OacJitterStatsHistoryPacketRecv_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 5),
    _OacJitterStatsHistoryPacketRecv_Type()
)
oacJitterStatsHistoryPacketRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryPacketRecv.setStatus("current")
_OacJitterStatsHistoryAvgRTT_Type = Integer32
_OacJitterStatsHistoryAvgRTT_Object = MibTableColumn
oacJitterStatsHistoryAvgRTT = _OacJitterStatsHistoryAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 6),
    _OacJitterStatsHistoryAvgRTT_Type()
)
oacJitterStatsHistoryAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryAvgRTT.setStatus("current")
_OacJitterStatsHistorySumRTT_Type = Integer32
_OacJitterStatsHistorySumRTT_Object = MibTableColumn
oacJitterStatsHistorySumRTT = _OacJitterStatsHistorySumRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 7),
    _OacJitterStatsHistorySumRTT_Type()
)
oacJitterStatsHistorySumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySumRTT.setStatus("current")
_OacJitterStatsHistoryMinRTT_Type = Integer32
_OacJitterStatsHistoryMinRTT_Object = MibTableColumn
oacJitterStatsHistoryMinRTT = _OacJitterStatsHistoryMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 8),
    _OacJitterStatsHistoryMinRTT_Type()
)
oacJitterStatsHistoryMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryMinRTT.setStatus("current")
_OacJitterStatsHistoryMaxRTT_Type = Integer32
_OacJitterStatsHistoryMaxRTT_Object = MibTableColumn
oacJitterStatsHistoryMaxRTT = _OacJitterStatsHistoryMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 9),
    _OacJitterStatsHistoryMaxRTT_Type()
)
oacJitterStatsHistoryMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryMaxRTT.setStatus("current")
_OacJitterStatsHistorySumPosJitter_Type = Integer32
_OacJitterStatsHistorySumPosJitter_Object = MibTableColumn
oacJitterStatsHistorySumPosJitter = _OacJitterStatsHistorySumPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 10),
    _OacJitterStatsHistorySumPosJitter_Type()
)
oacJitterStatsHistorySumPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySumPosJitter.setStatus("current")
_OacJitterStatsHistoryNumPosJitter_Type = Integer32
_OacJitterStatsHistoryNumPosJitter_Object = MibTableColumn
oacJitterStatsHistoryNumPosJitter = _OacJitterStatsHistoryNumPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 11),
    _OacJitterStatsHistoryNumPosJitter_Type()
)
oacJitterStatsHistoryNumPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryNumPosJitter.setStatus("current")
_OacJitterStatsHistorySumNegJitter_Type = Integer32
_OacJitterStatsHistorySumNegJitter_Object = MibTableColumn
oacJitterStatsHistorySumNegJitter = _OacJitterStatsHistorySumNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 12),
    _OacJitterStatsHistorySumNegJitter_Type()
)
oacJitterStatsHistorySumNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySumNegJitter.setStatus("current")
_OacJitterStatsHistoryNumNegJitter_Type = Integer32
_OacJitterStatsHistoryNumNegJitter_Object = MibTableColumn
oacJitterStatsHistoryNumNegJitter = _OacJitterStatsHistoryNumNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 13),
    _OacJitterStatsHistoryNumNegJitter_Type()
)
oacJitterStatsHistoryNumNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryNumNegJitter.setStatus("current")
_OacJitterStatsHistorySumPosSD_Type = Integer32
_OacJitterStatsHistorySumPosSD_Object = MibTableColumn
oacJitterStatsHistorySumPosSD = _OacJitterStatsHistorySumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 14),
    _OacJitterStatsHistorySumPosSD_Type()
)
oacJitterStatsHistorySumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySumPosSD.setStatus("current")
_OacJitterStatsHistoryNumPosSD_Type = Integer32
_OacJitterStatsHistoryNumPosSD_Object = MibTableColumn
oacJitterStatsHistoryNumPosSD = _OacJitterStatsHistoryNumPosSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 15),
    _OacJitterStatsHistoryNumPosSD_Type()
)
oacJitterStatsHistoryNumPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryNumPosSD.setStatus("current")
_OacJitterStatsHistorySumNegSD_Type = Integer32
_OacJitterStatsHistorySumNegSD_Object = MibTableColumn
oacJitterStatsHistorySumNegSD = _OacJitterStatsHistorySumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 16),
    _OacJitterStatsHistorySumNegSD_Type()
)
oacJitterStatsHistorySumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySumNegSD.setStatus("current")
_OacJitterStatsHistoryNumNegSD_Type = Integer32
_OacJitterStatsHistoryNumNegSD_Object = MibTableColumn
oacJitterStatsHistoryNumNegSD = _OacJitterStatsHistoryNumNegSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 17),
    _OacJitterStatsHistoryNumNegSD_Type()
)
oacJitterStatsHistoryNumNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryNumNegSD.setStatus("current")
_OacJitterStatsHistorySumPosDS_Type = Integer32
_OacJitterStatsHistorySumPosDS_Object = MibTableColumn
oacJitterStatsHistorySumPosDS = _OacJitterStatsHistorySumPosDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 18),
    _OacJitterStatsHistorySumPosDS_Type()
)
oacJitterStatsHistorySumPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySumPosDS.setStatus("current")
_OacJitterStatsHistoryNumPosDS_Type = Integer32
_OacJitterStatsHistoryNumPosDS_Object = MibTableColumn
oacJitterStatsHistoryNumPosDS = _OacJitterStatsHistoryNumPosDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 19),
    _OacJitterStatsHistoryNumPosDS_Type()
)
oacJitterStatsHistoryNumPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryNumPosDS.setStatus("current")
_OacJitterStatsHistorySumNegDS_Type = Integer32
_OacJitterStatsHistorySumNegDS_Object = MibTableColumn
oacJitterStatsHistorySumNegDS = _OacJitterStatsHistorySumNegDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 20),
    _OacJitterStatsHistorySumNegDS_Type()
)
oacJitterStatsHistorySumNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySumNegDS.setStatus("current")
_OacJitterStatsHistoryNumNegDS_Type = Integer32
_OacJitterStatsHistoryNumNegDS_Object = MibTableColumn
oacJitterStatsHistoryNumNegDS = _OacJitterStatsHistoryNumNegDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 21),
    _OacJitterStatsHistoryNumNegDS_Type()
)
oacJitterStatsHistoryNumNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryNumNegDS.setStatus("current")


class _OacJitterStatsHistoryPacketLossSD_Type(Integer32):
    """Custom type oacJitterStatsHistoryPacketLossSD based on Integer32"""
    defaultValue = 0


_OacJitterStatsHistoryPacketLossSD_Object = MibTableColumn
oacJitterStatsHistoryPacketLossSD = _OacJitterStatsHistoryPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 22),
    _OacJitterStatsHistoryPacketLossSD_Type()
)
oacJitterStatsHistoryPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryPacketLossSD.setStatus("current")


class _OacJitterStatsHistoryPacketLossDS_Type(Integer32):
    """Custom type oacJitterStatsHistoryPacketLossDS based on Integer32"""
    defaultValue = 0


_OacJitterStatsHistoryPacketLossDS_Object = MibTableColumn
oacJitterStatsHistoryPacketLossDS = _OacJitterStatsHistoryPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 23),
    _OacJitterStatsHistoryPacketLossDS_Type()
)
oacJitterStatsHistoryPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryPacketLossDS.setStatus("current")


class _OacJitterStatsHistoryPacketOutOfSequence_Type(Integer32):
    """Custom type oacJitterStatsHistoryPacketOutOfSequence based on Integer32"""
    defaultValue = 0


_OacJitterStatsHistoryPacketOutOfSequence_Object = MibTableColumn
oacJitterStatsHistoryPacketOutOfSequence = _OacJitterStatsHistoryPacketOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 24),
    _OacJitterStatsHistoryPacketOutOfSequence_Type()
)
oacJitterStatsHistoryPacketOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryPacketOutOfSequence.setStatus("current")


class _OacJitterStatsHistoryPacketLateArrival_Type(Integer32):
    """Custom type oacJitterStatsHistoryPacketLateArrival based on Integer32"""
    defaultValue = 0


_OacJitterStatsHistoryPacketLateArrival_Object = MibTableColumn
oacJitterStatsHistoryPacketLateArrival = _OacJitterStatsHistoryPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 25),
    _OacJitterStatsHistoryPacketLateArrival_Type()
)
oacJitterStatsHistoryPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryPacketLateArrival.setStatus("current")


class _OacJitterStatsHistoryPacketLoss_Type(Integer32):
    """Custom type oacJitterStatsHistoryPacketLoss based on Integer32"""
    defaultValue = 0


_OacJitterStatsHistoryPacketLoss_Object = MibTableColumn
oacJitterStatsHistoryPacketLoss = _OacJitterStatsHistoryPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 26),
    _OacJitterStatsHistoryPacketLoss_Type()
)
oacJitterStatsHistoryPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryPacketLoss.setStatus("current")
_OacJitterStatsHistoryMaxPosSD_Type = Integer32
_OacJitterStatsHistoryMaxPosSD_Object = MibTableColumn
oacJitterStatsHistoryMaxPosSD = _OacJitterStatsHistoryMaxPosSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 27),
    _OacJitterStatsHistoryMaxPosSD_Type()
)
oacJitterStatsHistoryMaxPosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryMaxPosSD.setStatus("current")
_OacJitterStatsHistoryMaxNegSD_Type = Integer32
_OacJitterStatsHistoryMaxNegSD_Object = MibTableColumn
oacJitterStatsHistoryMaxNegSD = _OacJitterStatsHistoryMaxNegSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 28),
    _OacJitterStatsHistoryMaxNegSD_Type()
)
oacJitterStatsHistoryMaxNegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryMaxNegSD.setStatus("current")
_OacJitterStatsHistoryMaxPosDS_Type = Integer32
_OacJitterStatsHistoryMaxPosDS_Object = MibTableColumn
oacJitterStatsHistoryMaxPosDS = _OacJitterStatsHistoryMaxPosDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 29),
    _OacJitterStatsHistoryMaxPosDS_Type()
)
oacJitterStatsHistoryMaxPosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryMaxPosDS.setStatus("current")
_OacJitterStatsHistoryMaxNegDS_Type = Integer32
_OacJitterStatsHistoryMaxNegDS_Object = MibTableColumn
oacJitterStatsHistoryMaxNegDS = _OacJitterStatsHistoryMaxNegDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 30),
    _OacJitterStatsHistoryMaxNegDS_Type()
)
oacJitterStatsHistoryMaxNegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryMaxNegDS.setStatus("current")
_OacJitterStatsHistorySum2PosSD_Type = Integer32
_OacJitterStatsHistorySum2PosSD_Object = MibTableColumn
oacJitterStatsHistorySum2PosSD = _OacJitterStatsHistorySum2PosSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 31),
    _OacJitterStatsHistorySum2PosSD_Type()
)
oacJitterStatsHistorySum2PosSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySum2PosSD.setStatus("current")
_OacJitterStatsHistorySum2NegSD_Type = Integer32
_OacJitterStatsHistorySum2NegSD_Object = MibTableColumn
oacJitterStatsHistorySum2NegSD = _OacJitterStatsHistorySum2NegSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 32),
    _OacJitterStatsHistorySum2NegSD_Type()
)
oacJitterStatsHistorySum2NegSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySum2NegSD.setStatus("current")
_OacJitterStatsHistorySum2PosDS_Type = Integer32
_OacJitterStatsHistorySum2PosDS_Object = MibTableColumn
oacJitterStatsHistorySum2PosDS = _OacJitterStatsHistorySum2PosDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 33),
    _OacJitterStatsHistorySum2PosDS_Type()
)
oacJitterStatsHistorySum2PosDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySum2PosDS.setStatus("current")
_OacJitterStatsHistorySum2NegDS_Type = Integer32
_OacJitterStatsHistorySum2NegDS_Object = MibTableColumn
oacJitterStatsHistorySum2NegDS = _OacJitterStatsHistorySum2NegDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 34),
    _OacJitterStatsHistorySum2NegDS_Type()
)
oacJitterStatsHistorySum2NegDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistorySum2NegDS.setStatus("current")
_OacJitterStatsHistoryDeviationSD_Type = Integer32
_OacJitterStatsHistoryDeviationSD_Object = MibTableColumn
oacJitterStatsHistoryDeviationSD = _OacJitterStatsHistoryDeviationSD_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 35),
    _OacJitterStatsHistoryDeviationSD_Type()
)
oacJitterStatsHistoryDeviationSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryDeviationSD.setStatus("current")
_OacJitterStatsHistoryDeviationDS_Type = Integer32
_OacJitterStatsHistoryDeviationDS_Object = MibTableColumn
oacJitterStatsHistoryDeviationDS = _OacJitterStatsHistoryDeviationDS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 5, 1, 3, 1, 36),
    _OacJitterStatsHistoryDeviationDS_Type()
)
oacJitterStatsHistoryDeviationDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacJitterStatsHistoryDeviationDS.setStatus("current")

# Managed Objects groups

oacJitterGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 5, 2000, 1, 1)
)
oacJitterGeneralGroup.setObjects(
      *(("ONEACCESS-JITTER-MIB", "oacJitterControlOwner"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlType"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlFrequency"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlTimeout"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlStatus"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlTargetAddress"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlTargetPort"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlSourceAddress"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlInterval"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlPktDataRequestSize"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlPacketCount"),
        ("ONEACCESS-JITTER-MIB", "oacJitterControlTos"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsCompleted"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsTime"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsNumRTT"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsPacketRecv"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsAvgRTT"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSumRTT"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsMinRTT"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsMaxRTT"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSumPosJitter"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsNumPosJitter"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSumNegJitter"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsNumNegJitter"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSumPosSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsNumPosSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsMaxPosSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSumNegSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsNumNegSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsMaxNegSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSumPosDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsNumPosDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsMaxPosDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSumNegDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsNumNegDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsMaxNegDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSum2PosSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSum2NegSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSum2PosDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsSum2NegDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsDeviationSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsDeviationDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsPacketLossSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsPacketLossDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsPacketOutOfSequence"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsPacketLateArrival"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsPacketLoss"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryCompleted"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryTime"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryNumRTT"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryPacketRecv"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryAvgRTT"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySumRTT"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryMinRTT"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryMaxRTT"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySumPosJitter"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryNumPosJitter"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySumNegJitter"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryNumNegJitter"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySumPosSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryNumPosSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySumNegSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryNumNegSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySumPosDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryNumPosDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySumNegDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryNumNegDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryPacketLossSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryPacketLossDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryPacketOutOfSequence"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryPacketLateArrival"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryPacketLoss"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryMaxPosSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryMaxNegSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryMaxPosDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryMaxNegDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySum2PosSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySum2NegSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySum2PosDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistorySum2NegDS"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryDeviationSD"),
        ("ONEACCESS-JITTER-MIB", "oacJitterStatsHistoryDeviationDS"))
)
if mibBuilder.loadTexts:
    oacJitterGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oacJitterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 5, 2000, 2, 1)
)
if mibBuilder.loadTexts:
    oacJitterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-JITTER-MIB",
    **{"OacJitterControlJitterType": OacJitterControlJitterType,
       "OacJitterResponseSense": OacJitterResponseSense,
       "oacJitterMIBModule": oacJitterMIBModule,
       "oacJitterConformance": oacJitterConformance,
       "oacJitterGroups": oacJitterGroups,
       "oacJitterGeneralGroup": oacJitterGeneralGroup,
       "oacJitterCompliances": oacJitterCompliances,
       "oacJitterCompliance": oacJitterCompliance,
       "oacExpIMJitter": oacExpIMJitter,
       "oacJitterObjects": oacJitterObjects,
       "oacJitterControlTable": oacJitterControlTable,
       "oacJitterControlEntry": oacJitterControlEntry,
       "oacJitterControlIndex": oacJitterControlIndex,
       "oacJitterControlOwner": oacJitterControlOwner,
       "oacJitterControlType": oacJitterControlType,
       "oacJitterControlFrequency": oacJitterControlFrequency,
       "oacJitterControlTimeout": oacJitterControlTimeout,
       "oacJitterControlTargetAddress": oacJitterControlTargetAddress,
       "oacJitterControlTargetPort": oacJitterControlTargetPort,
       "oacJitterControlSourceAddress": oacJitterControlSourceAddress,
       "oacJitterControlInterval": oacJitterControlInterval,
       "oacJitterControlPktDataRequestSize": oacJitterControlPktDataRequestSize,
       "oacJitterControlPacketCount": oacJitterControlPacketCount,
       "oacJitterControlTos": oacJitterControlTos,
       "oacJitterControlStatus": oacJitterControlStatus,
       "oacJitterControlVrfName": oacJitterControlVrfName,
       "oacJitterStatsTable": oacJitterStatsTable,
       "oacJitterStatsEntry": oacJitterStatsEntry,
       "oacJitterStatsCompleted": oacJitterStatsCompleted,
       "oacJitterStatsTime": oacJitterStatsTime,
       "oacJitterStatsNumRTT": oacJitterStatsNumRTT,
       "oacJitterStatsPacketRecv": oacJitterStatsPacketRecv,
       "oacJitterStatsAvgRTT": oacJitterStatsAvgRTT,
       "oacJitterStatsSumRTT": oacJitterStatsSumRTT,
       "oacJitterStatsMinRTT": oacJitterStatsMinRTT,
       "oacJitterStatsMaxRTT": oacJitterStatsMaxRTT,
       "oacJitterStatsSumPosJitter": oacJitterStatsSumPosJitter,
       "oacJitterStatsNumPosJitter": oacJitterStatsNumPosJitter,
       "oacJitterStatsSumNegJitter": oacJitterStatsSumNegJitter,
       "oacJitterStatsNumNegJitter": oacJitterStatsNumNegJitter,
       "oacJitterStatsSumPosSD": oacJitterStatsSumPosSD,
       "oacJitterStatsNumPosSD": oacJitterStatsNumPosSD,
       "oacJitterStatsSumNegSD": oacJitterStatsSumNegSD,
       "oacJitterStatsNumNegSD": oacJitterStatsNumNegSD,
       "oacJitterStatsSumPosDS": oacJitterStatsSumPosDS,
       "oacJitterStatsNumPosDS": oacJitterStatsNumPosDS,
       "oacJitterStatsSumNegDS": oacJitterStatsSumNegDS,
       "oacJitterStatsNumNegDS": oacJitterStatsNumNegDS,
       "oacJitterStatsPacketLossSD": oacJitterStatsPacketLossSD,
       "oacJitterStatsPacketLossDS": oacJitterStatsPacketLossDS,
       "oacJitterStatsPacketOutOfSequence": oacJitterStatsPacketOutOfSequence,
       "oacJitterStatsPacketLateArrival": oacJitterStatsPacketLateArrival,
       "oacJitterStatsPacketLoss": oacJitterStatsPacketLoss,
       "oacJitterStatsMaxPosSD": oacJitterStatsMaxPosSD,
       "oacJitterStatsMaxNegSD": oacJitterStatsMaxNegSD,
       "oacJitterStatsMaxPosDS": oacJitterStatsMaxPosDS,
       "oacJitterStatsMaxNegDS": oacJitterStatsMaxNegDS,
       "oacJitterStatsSum2PosSD": oacJitterStatsSum2PosSD,
       "oacJitterStatsSum2NegSD": oacJitterStatsSum2NegSD,
       "oacJitterStatsSum2PosDS": oacJitterStatsSum2PosDS,
       "oacJitterStatsSum2NegDS": oacJitterStatsSum2NegDS,
       "oacJitterStatsDeviationSD": oacJitterStatsDeviationSD,
       "oacJitterStatsDeviationDS": oacJitterStatsDeviationDS,
       "oacJitterStatsHistoryTable": oacJitterStatsHistoryTable,
       "oacJitterStatsHistoryEntry": oacJitterStatsHistoryEntry,
       "oacJitterStatsHistoryIndex": oacJitterStatsHistoryIndex,
       "oacJitterStatsHistoryCompleted": oacJitterStatsHistoryCompleted,
       "oacJitterStatsHistoryTime": oacJitterStatsHistoryTime,
       "oacJitterStatsHistoryNumRTT": oacJitterStatsHistoryNumRTT,
       "oacJitterStatsHistoryPacketRecv": oacJitterStatsHistoryPacketRecv,
       "oacJitterStatsHistoryAvgRTT": oacJitterStatsHistoryAvgRTT,
       "oacJitterStatsHistorySumRTT": oacJitterStatsHistorySumRTT,
       "oacJitterStatsHistoryMinRTT": oacJitterStatsHistoryMinRTT,
       "oacJitterStatsHistoryMaxRTT": oacJitterStatsHistoryMaxRTT,
       "oacJitterStatsHistorySumPosJitter": oacJitterStatsHistorySumPosJitter,
       "oacJitterStatsHistoryNumPosJitter": oacJitterStatsHistoryNumPosJitter,
       "oacJitterStatsHistorySumNegJitter": oacJitterStatsHistorySumNegJitter,
       "oacJitterStatsHistoryNumNegJitter": oacJitterStatsHistoryNumNegJitter,
       "oacJitterStatsHistorySumPosSD": oacJitterStatsHistorySumPosSD,
       "oacJitterStatsHistoryNumPosSD": oacJitterStatsHistoryNumPosSD,
       "oacJitterStatsHistorySumNegSD": oacJitterStatsHistorySumNegSD,
       "oacJitterStatsHistoryNumNegSD": oacJitterStatsHistoryNumNegSD,
       "oacJitterStatsHistorySumPosDS": oacJitterStatsHistorySumPosDS,
       "oacJitterStatsHistoryNumPosDS": oacJitterStatsHistoryNumPosDS,
       "oacJitterStatsHistorySumNegDS": oacJitterStatsHistorySumNegDS,
       "oacJitterStatsHistoryNumNegDS": oacJitterStatsHistoryNumNegDS,
       "oacJitterStatsHistoryPacketLossSD": oacJitterStatsHistoryPacketLossSD,
       "oacJitterStatsHistoryPacketLossDS": oacJitterStatsHistoryPacketLossDS,
       "oacJitterStatsHistoryPacketOutOfSequence": oacJitterStatsHistoryPacketOutOfSequence,
       "oacJitterStatsHistoryPacketLateArrival": oacJitterStatsHistoryPacketLateArrival,
       "oacJitterStatsHistoryPacketLoss": oacJitterStatsHistoryPacketLoss,
       "oacJitterStatsHistoryMaxPosSD": oacJitterStatsHistoryMaxPosSD,
       "oacJitterStatsHistoryMaxNegSD": oacJitterStatsHistoryMaxNegSD,
       "oacJitterStatsHistoryMaxPosDS": oacJitterStatsHistoryMaxPosDS,
       "oacJitterStatsHistoryMaxNegDS": oacJitterStatsHistoryMaxNegDS,
       "oacJitterStatsHistorySum2PosSD": oacJitterStatsHistorySum2PosSD,
       "oacJitterStatsHistorySum2NegSD": oacJitterStatsHistorySum2NegSD,
       "oacJitterStatsHistorySum2PosDS": oacJitterStatsHistorySum2PosDS,
       "oacJitterStatsHistorySum2NegDS": oacJitterStatsHistorySum2NegDS,
       "oacJitterStatsHistoryDeviationSD": oacJitterStatsHistoryDeviationSD,
       "oacJitterStatsHistoryDeviationDS": oacJitterStatsHistoryDeviationDS}
)
