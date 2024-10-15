# SNMP MIB module (OneAccess-RoundTripTime-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OneAccess-RoundTripTime-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:54 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(oacExpIMManagement,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMManagement",
    "oacMIBModules")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

oacRttChkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223)
)
oacRttChkMIB.setRevisions(
        ("2011-07-29 00:00",
         "2011-06-15 00:00",
         "2010-07-08 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RttResponseSense(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("applicationSpecific", 10),
          ("busy", 5),
          ("disconnected", 2),
          ("dropped", 7),
          ("error", 16),
          ("notConnected", 6),
          ("ok", 1),
          ("overThreshold", 3),
          ("sequenceError", 8),
          ("timeout", 4),
          ("verifyError", 9))
    )



class OacRttRttType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("echo", 1),
          ("pathEcho", 2))
    )



class OacRttProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipIcmpEcho", 2),
          ("notApplicable", 1))
    )



class OacRttTargetAddress(OctetString, TextualConvention):
    status = "current"


class OacRttApplType(Integer32, TextualConvention):
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
        *(("dhcp", 11),
          ("dlsw", 10),
          ("dns", 8),
          ("echo", 1),
          ("fileIO", 3),
          ("ftp", 12),
          ("http", 7),
          ("jitter", 9),
          ("pathEcho", 2),
          ("script", 4),
          ("tcpConnect", 6),
          ("udpEcho", 5))
    )



class OacRttApplProtocol(Integer32, TextualConvention):
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("apolloEcho", 21),
          ("apolloEchoAppl", 22),
          ("appleTalkEcho", 9),
          ("appleTalkEchoAppl", 10),
          ("decNetEcho", 11),
          ("decNetEchoAppl", 12),
          ("dhcpAppl", 29),
          ("dlswAppl", 28),
          ("dnsAppl", 26),
          ("ftpAppl", 30),
          ("httpAppl", 25),
          ("ipIcmpEcho", 2),
          ("ipTcpConn", 24),
          ("ipUdpEchoAppl", 3),
          ("ipxEcho", 13),
          ("ipxEchoAppl", 14),
          ("isoClnsEcho", 15),
          ("isoClnsEchoAppl", 16),
          ("jitterAppl", 27),
          ("netbiosEchoAppl", 23),
          ("notApplicable", 1),
          ("snaLU0EchoAppl", 5),
          ("snaLU2EchoAppl", 6),
          ("snaLU62Echo", 7),
          ("snaLU62EchoAppl", 8),
          ("snaRUEcho", 4),
          ("vinesEcho", 17),
          ("vinesEchoAppl", 18),
          ("xnsEcho", 19),
          ("xnsEchoAppl", 20))
    )



# MIB Managed Objects in the order of their OIDs

_OacRttChkObj_ObjectIdentity = ObjectIdentity
oacRttChkObj = _OacRttChkObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1)
)
_OacRttControl_ObjectIdentity = ObjectIdentity
oacRttControl = _OacRttControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1)
)
_OacRttControlTable_Object = MibTable
oacRttControlTable = _OacRttControlTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 1)
)
if mibBuilder.loadTexts:
    oacRttControlTable.setStatus("current")
_OacRttControlEntry_Object = MibTableRow
oacRttControlEntry = _OacRttControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 1, 1)
)
oacRttControlEntry.setIndexNames(
    (0, "OneAccess-RoundTripTime-MIB", "oacRttControlIndex"),
)
if mibBuilder.loadTexts:
    oacRttControlEntry.setStatus("current")


class _OacRttControlIndex_Type(Integer32):
    """Custom type oacRttControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OacRttControlIndex_Type.__name__ = "Integer32"
_OacRttControlIndex_Object = MibTableColumn
oacRttControlIndex = _OacRttControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 1, 1, 1),
    _OacRttControlIndex_Type()
)
oacRttControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttControlIndex.setStatus("current")
_OacRttControlStatus_Type = RowStatus
_OacRttControlStatus_Object = MibTableColumn
oacRttControlStatus = _OacRttControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 1, 1, 2),
    _OacRttControlStatus_Type()
)
oacRttControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttControlStatus.setStatus("current")


class _OacRttControlTag_Type(DisplayString):
    """Custom type oacRttControlTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OacRttControlTag_Type.__name__ = "DisplayString"
_OacRttControlTag_Object = MibTableColumn
oacRttControlTag = _OacRttControlTag_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 1, 1, 3),
    _OacRttControlTag_Type()
)
oacRttControlTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttControlTag.setStatus("current")


class _OacRttControlFrequency_Type(Integer32):
    """Custom type oacRttControlFrequency based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_OacRttControlFrequency_Type.__name__ = "Integer32"
_OacRttControlFrequency_Object = MibTableColumn
oacRttControlFrequency = _OacRttControlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 1, 1, 4),
    _OacRttControlFrequency_Type()
)
oacRttControlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttControlFrequency.setStatus("current")
if mibBuilder.loadTexts:
    oacRttControlFrequency.setUnits("seconds")


class _OacRttControlRttType_Type(OacRttRttType):
    """Custom type oacRttControlRttType based on OacRttRttType"""


_OacRttControlRttType_Object = MibTableColumn
oacRttControlRttType = _OacRttControlRttType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 1, 1, 5),
    _OacRttControlRttType_Type()
)
oacRttControlRttType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttControlRttType.setStatus("current")


class _OacRttControlTimeout_Type(Integer32):
    """Custom type oacRttControlTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_OacRttControlTimeout_Type.__name__ = "Integer32"
_OacRttControlTimeout_Object = MibTableColumn
oacRttControlTimeout = _OacRttControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 1, 1, 6),
    _OacRttControlTimeout_Type()
)
oacRttControlTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttControlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    oacRttControlTimeout.setUnits("milliseconds")
_OacRttControlOwner_Type = OwnerString
_OacRttControlOwner_Object = MibTableColumn
oacRttControlOwner = _OacRttControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 1, 1, 7),
    _OacRttControlOwner_Type()
)
oacRttControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttControlOwner.setStatus("current")


class _OacRttControlThreshold_Type(Integer32):
    """Custom type oacRttControlThreshold based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttControlThreshold_Type.__name__ = "Integer32"
_OacRttControlThreshold_Object = MibTableColumn
oacRttControlThreshold = _OacRttControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 1, 1, 8),
    _OacRttControlThreshold_Type()
)
oacRttControlThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttControlThreshold.setStatus("current")
if mibBuilder.loadTexts:
    oacRttControlThreshold.setUnits("milliseconds")
_OacRttEchoTable_Object = MibTable
oacRttEchoTable = _OacRttEchoTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 2)
)
if mibBuilder.loadTexts:
    oacRttEchoTable.setStatus("current")
_OacRttEchoEntry_Object = MibTableRow
oacRttEchoEntry = _OacRttEchoEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 2, 1)
)
oacRttEchoEntry.setIndexNames(
    (0, "OneAccess-RoundTripTime-MIB", "oacRttControlIndex"),
)
if mibBuilder.loadTexts:
    oacRttEchoEntry.setStatus("current")
_OacRttEchoSourceAddress_Type = OacRttTargetAddress
_OacRttEchoSourceAddress_Object = MibTableColumn
oacRttEchoSourceAddress = _OacRttEchoSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 2, 1, 1),
    _OacRttEchoSourceAddress_Type()
)
oacRttEchoSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttEchoSourceAddress.setStatus("current")
_OacRttEchoTargetAddress_Type = OacRttTargetAddress
_OacRttEchoTargetAddress_Object = MibTableColumn
oacRttEchoTargetAddress = _OacRttEchoTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 2, 1, 2),
    _OacRttEchoTargetAddress_Type()
)
oacRttEchoTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttEchoTargetAddress.setStatus("current")


class _OacRttEchoPktDataRequestSize_Type(Integer32):
    """Custom type oacRttEchoPktDataRequestSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_OacRttEchoPktDataRequestSize_Type.__name__ = "Integer32"
_OacRttEchoPktDataRequestSize_Object = MibTableColumn
oacRttEchoPktDataRequestSize = _OacRttEchoPktDataRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 2, 1, 3),
    _OacRttEchoPktDataRequestSize_Type()
)
oacRttEchoPktDataRequestSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttEchoPktDataRequestSize.setStatus("current")
if mibBuilder.loadTexts:
    oacRttEchoPktDataRequestSize.setUnits("octets")


class _OacRttEchoPktDataResponseSize_Type(Integer32):
    """Custom type oacRttEchoPktDataResponseSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_OacRttEchoPktDataResponseSize_Type.__name__ = "Integer32"
_OacRttEchoPktDataResponseSize_Object = MibTableColumn
oacRttEchoPktDataResponseSize = _OacRttEchoPktDataResponseSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 2, 1, 4),
    _OacRttEchoPktDataResponseSize_Type()
)
oacRttEchoPktDataResponseSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttEchoPktDataResponseSize.setStatus("current")


class _OacRttEchoTOS_Type(Integer32):
    """Custom type oacRttEchoTOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OacRttEchoTOS_Type.__name__ = "Integer32"
_OacRttEchoTOS_Object = MibTableColumn
oacRttEchoTOS = _OacRttEchoTOS_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 2, 1, 5),
    _OacRttEchoTOS_Type()
)
oacRttEchoTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttEchoTOS.setStatus("current")


class _OacRttEchoProtocol_Type(OacRttProtocol):
    """Custom type oacRttEchoProtocol based on OacRttProtocol"""


_OacRttEchoProtocol_Object = MibTableColumn
oacRttEchoProtocol = _OacRttEchoProtocol_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 2, 1, 6),
    _OacRttEchoProtocol_Type()
)
oacRttEchoProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttEchoProtocol.setStatus("current")
_OacRttHistoryTable_Object = MibTable
oacRttHistoryTable = _OacRttHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 3)
)
if mibBuilder.loadTexts:
    oacRttHistoryTable.setStatus("current")
_OacRttHistoryEntry_Object = MibTableRow
oacRttHistoryEntry = _OacRttHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    oacRttHistoryEntry.setStatus("current")


class _OacRttHistoryNumBuckets_Type(Integer32):
    """Custom type oacRttHistoryNumBuckets based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_OacRttHistoryNumBuckets_Type.__name__ = "Integer32"
_OacRttHistoryNumBuckets_Object = MibTableColumn
oacRttHistoryNumBuckets = _OacRttHistoryNumBuckets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 3, 1, 1),
    _OacRttHistoryNumBuckets_Type()
)
oacRttHistoryNumBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttHistoryNumBuckets.setStatus("current")


class _OacRttHistoryFilter_Type(Integer32):
    """Custom type oacRttHistoryFilter based on Integer32"""
    defaultValue = 1

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
        *(("all", 2),
          ("failures", 4),
          ("none", 1),
          ("overThreshold", 3))
    )


_OacRttHistoryFilter_Type.__name__ = "Integer32"
_OacRttHistoryFilter_Object = MibTableColumn
oacRttHistoryFilter = _OacRttHistoryFilter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 3, 1, 2),
    _OacRttHistoryFilter_Type()
)
oacRttHistoryFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttHistoryFilter.setStatus("current")


class _OacRttHistoryNumLives_Type(Integer32):
    """Custom type oacRttHistoryNumLives based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OacRttHistoryNumLives_Type.__name__ = "Integer32"
_OacRttHistoryNumLives_Object = MibTableColumn
oacRttHistoryNumLives = _OacRttHistoryNumLives_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 3, 1, 3),
    _OacRttHistoryNumLives_Type()
)
oacRttHistoryNumLives.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttHistoryNumLives.setStatus("current")


class _OacRttHistoryNumSamples_Type(Integer32):
    """Custom type oacRttHistoryNumSamples based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_OacRttHistoryNumSamples_Type.__name__ = "Integer32"
_OacRttHistoryNumSamples_Object = MibTableColumn
oacRttHistoryNumSamples = _OacRttHistoryNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 3, 1, 4),
    _OacRttHistoryNumSamples_Type()
)
oacRttHistoryNumSamples.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttHistoryNumSamples.setStatus("current")
_OacRttSchedTable_Object = MibTable
oacRttSchedTable = _OacRttSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 4)
)
if mibBuilder.loadTexts:
    oacRttSchedTable.setStatus("current")
_OacRttSchedEntry_Object = MibTableRow
oacRttSchedEntry = _OacRttSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    oacRttSchedEntry.setStatus("current")


class _OacRttSchedRttStartTime_Type(TimeTicks):
    """Custom type oacRttSchedRttStartTime based on TimeTicks"""
    defaultValue = 0


_OacRttSchedRttStartTime_Object = MibTableColumn
oacRttSchedRttStartTime = _OacRttSchedRttStartTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 4, 1, 1),
    _OacRttSchedRttStartTime_Type()
)
oacRttSchedRttStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttSchedRttStartTime.setStatus("current")


class _OacRttSchedRttLife_Type(Integer32):
    """Custom type oacRttSchedRttLife based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttSchedRttLife_Type.__name__ = "Integer32"
_OacRttSchedRttLife_Object = MibTableColumn
oacRttSchedRttLife = _OacRttSchedRttLife_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 4, 1, 2),
    _OacRttSchedRttLife_Type()
)
oacRttSchedRttLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttSchedRttLife.setStatus("current")
if mibBuilder.loadTexts:
    oacRttSchedRttLife.setUnits("seconds")


class _OacRttSchedConceptRowAgeout_Type(Integer32):
    """Custom type oacRttSchedConceptRowAgeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2073600),
    )


_OacRttSchedConceptRowAgeout_Type.__name__ = "Integer32"
_OacRttSchedConceptRowAgeout_Object = MibTableColumn
oacRttSchedConceptRowAgeout = _OacRttSchedConceptRowAgeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 4, 1, 3),
    _OacRttSchedConceptRowAgeout_Type()
)
oacRttSchedConceptRowAgeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttSchedConceptRowAgeout.setStatus("current")
if mibBuilder.loadTexts:
    oacRttSchedConceptRowAgeout.setUnits("seconds")
_OacRttReactTable_Object = MibTable
oacRttReactTable = _OacRttReactTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 5)
)
if mibBuilder.loadTexts:
    oacRttReactTable.setStatus("current")
_OacRttReactEntry_Object = MibTableRow
oacRttReactEntry = _OacRttReactEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    oacRttReactEntry.setStatus("current")


class _OacRttReactActionType_Type(Integer32):
    """Custom type oacRttReactActionType based on Integer32"""
    defaultValue = 1

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
        *(("nmvtAndTrigger", 7),
          ("nmvtOnly", 3),
          ("none", 1),
          ("trapAndNmvt", 5),
          ("trapAndTrigger", 6),
          ("trapNmvtAndTrigger", 8),
          ("trapOnly", 2),
          ("triggerOnly", 4))
    )


_OacRttReactActionType_Type.__name__ = "Integer32"
_OacRttReactActionType_Object = MibTableColumn
oacRttReactActionType = _OacRttReactActionType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 5, 1, 1),
    _OacRttReactActionType_Type()
)
oacRttReactActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttReactActionType.setStatus("current")


class _OacRttReactThresholdType_Type(Integer32):
    """Custom type oacRttReactThresholdType based on Integer32"""
    defaultValue = 1

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
        *(("average", 5),
          ("consecutive", 3),
          ("immediate", 2),
          ("never", 1),
          ("xOfy", 4))
    )


_OacRttReactThresholdType_Type.__name__ = "Integer32"
_OacRttReactThresholdType_Object = MibTableColumn
oacRttReactThresholdType = _OacRttReactThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 5, 1, 2),
    _OacRttReactThresholdType_Type()
)
oacRttReactThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttReactThresholdType.setStatus("current")


class _OacRttReactThresholdCount_Type(Integer32):
    """Custom type oacRttReactThresholdCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OacRttReactThresholdCount_Type.__name__ = "Integer32"
_OacRttReactThresholdCount_Object = MibTableColumn
oacRttReactThresholdCount = _OacRttReactThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 5, 1, 3),
    _OacRttReactThresholdCount_Type()
)
oacRttReactThresholdCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttReactThresholdCount.setStatus("current")


class _OacRttReactThresholdCount2_Type(Integer32):
    """Custom type oacRttReactThresholdCount2 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OacRttReactThresholdCount2_Type.__name__ = "Integer32"
_OacRttReactThresholdCount2_Object = MibTableColumn
oacRttReactThresholdCount2 = _OacRttReactThresholdCount2_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 5, 1, 4),
    _OacRttReactThresholdCount2_Type()
)
oacRttReactThresholdCount2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttReactThresholdCount2.setStatus("current")


class _OacRttReactConnectionEnable_Type(TruthValue):
    """Custom type oacRttReactConnectionEnable based on TruthValue"""


_OacRttReactConnectionEnable_Object = MibTableColumn
oacRttReactConnectionEnable = _OacRttReactConnectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 5, 1, 5),
    _OacRttReactConnectionEnable_Type()
)
oacRttReactConnectionEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttReactConnectionEnable.setStatus("current")


class _OacRttReactVerifyErrorEnable_Type(TruthValue):
    """Custom type oacRttReactVerifyErrorEnable based on TruthValue"""


_OacRttReactVerifyErrorEnable_Object = MibTableColumn
oacRttReactVerifyErrorEnable = _OacRttReactVerifyErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 5, 1, 6),
    _OacRttReactVerifyErrorEnable_Type()
)
oacRttReactVerifyErrorEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttReactVerifyErrorEnable.setStatus("current")


class _OacRttReactThresholdFalling_Type(Integer32):
    """Custom type oacRttReactThresholdFalling based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttReactThresholdFalling_Type.__name__ = "Integer32"
_OacRttReactThresholdFalling_Object = MibTableColumn
oacRttReactThresholdFalling = _OacRttReactThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 5, 1, 7),
    _OacRttReactThresholdFalling_Type()
)
oacRttReactThresholdFalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttReactThresholdFalling.setStatus("current")
if mibBuilder.loadTexts:
    oacRttReactThresholdFalling.setUnits("milliseconds")


class _OacRttReactTimeoutEnable_Type(TruthValue):
    """Custom type oacRttReactTimeoutEnable based on TruthValue"""


_OacRttReactTimeoutEnable_Object = MibTableColumn
oacRttReactTimeoutEnable = _OacRttReactTimeoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 5, 1, 8),
    _OacRttReactTimeoutEnable_Type()
)
oacRttReactTimeoutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttReactTimeoutEnable.setStatus("current")
_OacRttStatisticsTable_Object = MibTable
oacRttStatisticsTable = _OacRttStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 6)
)
if mibBuilder.loadTexts:
    oacRttStatisticsTable.setStatus("current")
_OacRttStatisticsEntry_Object = MibTableRow
oacRttStatisticsEntry = _OacRttStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    oacRttStatisticsEntry.setStatus("current")


class _OacRttStatisticsNumDistBuckets_Type(Integer32):
    """Custom type oacRttStatisticsNumDistBuckets based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OacRttStatisticsNumDistBuckets_Type.__name__ = "Integer32"
_OacRttStatisticsNumDistBuckets_Object = MibTableColumn
oacRttStatisticsNumDistBuckets = _OacRttStatisticsNumDistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 6, 1, 1),
    _OacRttStatisticsNumDistBuckets_Type()
)
oacRttStatisticsNumDistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttStatisticsNumDistBuckets.setStatus("current")


class _OacRttStatisticsNumHops_Type(Integer32):
    """Custom type oacRttStatisticsNumHops based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_OacRttStatisticsNumHops_Type.__name__ = "Integer32"
_OacRttStatisticsNumHops_Object = MibTableColumn
oacRttStatisticsNumHops = _OacRttStatisticsNumHops_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 6, 1, 2),
    _OacRttStatisticsNumHops_Type()
)
oacRttStatisticsNumHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttStatisticsNumHops.setStatus("current")


class _OacRttStatisticsNumPaths_Type(Integer32):
    """Custom type oacRttStatisticsNumPaths based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_OacRttStatisticsNumPaths_Type.__name__ = "Integer32"
_OacRttStatisticsNumPaths_Object = MibTableColumn
oacRttStatisticsNumPaths = _OacRttStatisticsNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 6, 1, 3),
    _OacRttStatisticsNumPaths_Type()
)
oacRttStatisticsNumPaths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttStatisticsNumPaths.setStatus("current")


class _OacRttStatisticsDistInterval_Type(Integer32):
    """Custom type oacRttStatisticsDistInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OacRttStatisticsDistInterval_Type.__name__ = "Integer32"
_OacRttStatisticsDistInterval_Object = MibTableColumn
oacRttStatisticsDistInterval = _OacRttStatisticsDistInterval_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 6, 1, 4),
    _OacRttStatisticsDistInterval_Type()
)
oacRttStatisticsDistInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttStatisticsDistInterval.setStatus("current")
if mibBuilder.loadTexts:
    oacRttStatisticsDistInterval.setUnits("milliseconds")


class _OacRttStatisticsNumHourGroups_Type(Integer32):
    """Custom type oacRttStatisticsNumHourGroups based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_OacRttStatisticsNumHourGroups_Type.__name__ = "Integer32"
_OacRttStatisticsNumHourGroups_Object = MibTableColumn
oacRttStatisticsNumHourGroups = _OacRttStatisticsNumHourGroups_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 6, 1, 5),
    _OacRttStatisticsNumHourGroups_Type()
)
oacRttStatisticsNumHourGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttStatisticsNumHourGroups.setStatus("current")
_OacRttControlOperTable_Object = MibTable
oacRttControlOperTable = _OacRttControlOperTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7)
)
if mibBuilder.loadTexts:
    oacRttControlOperTable.setStatus("current")
_OacRttControlOperEntry_Object = MibTableRow
oacRttControlOperEntry = _OacRttControlOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    oacRttControlOperEntry.setStatus("current")


class _OacRttControlOperNumRtts_Type(Integer32):
    """Custom type oacRttControlOperNumRtts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttControlOperNumRtts_Type.__name__ = "Integer32"
_OacRttControlOperNumRtts_Object = MibTableColumn
oacRttControlOperNumRtts = _OacRttControlOperNumRtts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1, 1),
    _OacRttControlOperNumRtts_Type()
)
oacRttControlOperNumRtts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttControlOperNumRtts.setStatus("current")
_OacRttControlOperOctetsInUse_Type = Gauge32
_OacRttControlOperOctetsInUse_Object = MibTableColumn
oacRttControlOperOctetsInUse = _OacRttControlOperOctetsInUse_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1, 2),
    _OacRttControlOperOctetsInUse_Type()
)
oacRttControlOperOctetsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttControlOperOctetsInUse.setStatus("current")


class _OacRttControlOperDiagText_Type(DisplayString):
    """Custom type oacRttControlOperDiagText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_OacRttControlOperDiagText_Type.__name__ = "DisplayString"
_OacRttControlOperDiagText_Object = MibTableColumn
oacRttControlOperDiagText = _OacRttControlOperDiagText_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1, 3),
    _OacRttControlOperDiagText_Type()
)
oacRttControlOperDiagText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttControlOperDiagText.setStatus("current")


class _OacRttControlOperOverThresholdOccurred_Type(TruthValue):
    """Custom type oacRttControlOperOverThresholdOccurred based on TruthValue"""


_OacRttControlOperOverThresholdOccurred_Object = MibTableColumn
oacRttControlOperOverThresholdOccurred = _OacRttControlOperOverThresholdOccurred_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1, 4),
    _OacRttControlOperOverThresholdOccurred_Type()
)
oacRttControlOperOverThresholdOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttControlOperOverThresholdOccurred.setStatus("current")


class _OacRttControlOperState_Type(Integer32):
    """Custom type oacRttControlOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("immediateStop", 3),
          ("inactive", 5),
          ("orderlyStop", 2),
          ("pending", 4),
          ("reset", 1),
          ("restart", 7))
    )


_OacRttControlOperState_Type.__name__ = "Integer32"
_OacRttControlOperState_Object = MibTableColumn
oacRttControlOperState = _OacRttControlOperState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1, 5),
    _OacRttControlOperState_Type()
)
oacRttControlOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacRttControlOperState.setStatus("current")


class _OacRttControlOperTimeoutOccurred_Type(TruthValue):
    """Custom type oacRttControlOperTimeoutOccurred based on TruthValue"""


_OacRttControlOperTimeoutOccurred_Object = MibTableColumn
oacRttControlOperTimeoutOccurred = _OacRttControlOperTimeoutOccurred_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1, 6),
    _OacRttControlOperTimeoutOccurred_Type()
)
oacRttControlOperTimeoutOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttControlOperTimeoutOccurred.setStatus("current")


class _OacRttControlOperRttLife_Type(Integer32):
    """Custom type oacRttControlOperRttLife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttControlOperRttLife_Type.__name__ = "Integer32"
_OacRttControlOperRttLife_Object = MibTableColumn
oacRttControlOperRttLife = _OacRttControlOperRttLife_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1, 7),
    _OacRttControlOperRttLife_Type()
)
oacRttControlOperRttLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttControlOperRttLife.setStatus("current")
if mibBuilder.loadTexts:
    oacRttControlOperRttLife.setUnits("seconds")
_OacRttControlOperModificationTime_Type = TimeStamp
_OacRttControlOperModificationTime_Object = MibTableColumn
oacRttControlOperModificationTime = _OacRttControlOperModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1, 8),
    _OacRttControlOperModificationTime_Type()
)
oacRttControlOperModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttControlOperModificationTime.setStatus("current")


class _OacRttControlOperConnLostOccurred_Type(TruthValue):
    """Custom type oacRttControlOperConnLostOccurred based on TruthValue"""


_OacRttControlOperConnLostOccurred_Object = MibTableColumn
oacRttControlOperConnLostOccurred = _OacRttControlOperConnLostOccurred_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1, 9),
    _OacRttControlOperConnLostOccurred_Type()
)
oacRttControlOperConnLostOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttControlOperConnLostOccurred.setStatus("current")
_OacRttControlOperResetTime_Type = TimeStamp
_OacRttControlOperResetTime_Object = MibTableColumn
oacRttControlOperResetTime = _OacRttControlOperResetTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 7, 1, 10),
    _OacRttControlOperResetTime_Type()
)
oacRttControlOperResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttControlOperResetTime.setStatus("current")
_OacRttReactTriggerTable_Object = MibTable
oacRttReactTriggerTable = _OacRttReactTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 8)
)
if mibBuilder.loadTexts:
    oacRttReactTriggerTable.setStatus("current")
_OacRttReactTriggerEntry_Object = MibTableRow
oacRttReactTriggerEntry = _OacRttReactTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 8, 1)
)
oacRttReactTriggerEntry.setIndexNames(
    (0, "OneAccess-RoundTripTime-MIB", "oacRttControlIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttReactTriggerOacRttControlIndex"),
)
if mibBuilder.loadTexts:
    oacRttReactTriggerEntry.setStatus("current")


class _OacRttReactTriggerOacRttControlIndex_Type(Integer32):
    """Custom type oacRttReactTriggerOacRttControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OacRttReactTriggerOacRttControlIndex_Type.__name__ = "Integer32"
_OacRttReactTriggerOacRttControlIndex_Object = MibTableColumn
oacRttReactTriggerOacRttControlIndex = _OacRttReactTriggerOacRttControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 8, 1, 1),
    _OacRttReactTriggerOacRttControlIndex_Type()
)
oacRttReactTriggerOacRttControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttReactTriggerOacRttControlIndex.setStatus("current")


class _OacRttReactTriggerStatus_Type(RowStatus):
    """Custom type oacRttReactTriggerStatus based on RowStatus"""


_OacRttReactTriggerStatus_Object = MibTableColumn
oacRttReactTriggerStatus = _OacRttReactTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 8, 1, 2),
    _OacRttReactTriggerStatus_Type()
)
oacRttReactTriggerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacRttReactTriggerStatus.setStatus("current")
_OacRttReactTriggerOperTable_Object = MibTable
oacRttReactTriggerOperTable = _OacRttReactTriggerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 9)
)
if mibBuilder.loadTexts:
    oacRttReactTriggerOperTable.setStatus("current")
_OacRttReactTriggerOperEntry_Object = MibTableRow
oacRttReactTriggerOperEntry = _OacRttReactTriggerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    oacRttReactTriggerOperEntry.setStatus("current")


class _OacRttReactTriggerOperState_Type(Integer32):
    """Custom type oacRttReactTriggerOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("pending", 2))
    )


_OacRttReactTriggerOperState_Type.__name__ = "Integer32"
_OacRttReactTriggerOperState_Object = MibTableColumn
oacRttReactTriggerOperState = _OacRttReactTriggerOperState_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 9, 1, 1),
    _OacRttReactTriggerOperState_Type()
)
oacRttReactTriggerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttReactTriggerOperState.setStatus("current")
_OacRttLatestRttOperTable_Object = MibTable
oacRttLatestRttOperTable = _OacRttLatestRttOperTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 10)
)
if mibBuilder.loadTexts:
    oacRttLatestRttOperTable.setStatus("current")
_OacRttLatestRttOperEntry_Object = MibTableRow
oacRttLatestRttOperEntry = _OacRttLatestRttOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    oacRttLatestRttOperEntry.setStatus("current")
_OacRttLatestRttOperTime_Type = TimeStamp
_OacRttLatestRttOperTime_Object = MibTableColumn
oacRttLatestRttOperTime = _OacRttLatestRttOperTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 10, 1, 1),
    _OacRttLatestRttOperTime_Type()
)
oacRttLatestRttOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttLatestRttOperTime.setStatus("current")
_OacRttLatestRttOperSense_Type = RttResponseSense
_OacRttLatestRttOperSense_Object = MibTableColumn
oacRttLatestRttOperSense = _OacRttLatestRttOperSense_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 10, 1, 2),
    _OacRttLatestRttOperSense_Type()
)
oacRttLatestRttOperSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttLatestRttOperSense.setStatus("current")
_OacRttLatestRttOperSenseDescription_Type = DisplayString
_OacRttLatestRttOperSenseDescription_Object = MibTableColumn
oacRttLatestRttOperSenseDescription = _OacRttLatestRttOperSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 10, 1, 3),
    _OacRttLatestRttOperSenseDescription_Type()
)
oacRttLatestRttOperSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttLatestRttOperSenseDescription.setStatus("current")
_OacRttLatestRttOperAddress_Type = OacRttTargetAddress
_OacRttLatestRttOperAddress_Object = MibTableColumn
oacRttLatestRttOperAddress = _OacRttLatestRttOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 10, 1, 4),
    _OacRttLatestRttOperAddress_Type()
)
oacRttLatestRttOperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttLatestRttOperAddress.setStatus("current")
_OacRttLatestRttOperCompletionTime_Type = Gauge32
_OacRttLatestRttOperCompletionTime_Object = MibTableColumn
oacRttLatestRttOperCompletionTime = _OacRttLatestRttOperCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 10, 1, 5),
    _OacRttLatestRttOperCompletionTime_Type()
)
oacRttLatestRttOperCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttLatestRttOperCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    oacRttLatestRttOperCompletionTime.setUnits("milliseconds")


class _OacRttLatestRttOperApplSpecificSense_Type(Integer32):
    """Custom type oacRttLatestRttOperApplSpecificSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 2147483647),
    )


_OacRttLatestRttOperApplSpecificSense_Type.__name__ = "Integer32"
_OacRttLatestRttOperApplSpecificSense_Object = MibTableColumn
oacRttLatestRttOperApplSpecificSense = _OacRttLatestRttOperApplSpecificSense_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 1, 10, 1, 6),
    _OacRttLatestRttOperApplSpecificSense_Type()
)
oacRttLatestRttOperApplSpecificSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttLatestRttOperApplSpecificSense.setStatus("current")
_OacRttHistory_ObjectIdentity = ObjectIdentity
oacRttHistory = _OacRttHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2)
)
_OacRttHistoryCollectionTable_Object = MibTable
oacRttHistoryCollectionTable = _OacRttHistoryCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1)
)
if mibBuilder.loadTexts:
    oacRttHistoryCollectionTable.setStatus("current")
_OacRttHistoryCollectionEntry_Object = MibTableRow
oacRttHistoryCollectionEntry = _OacRttHistoryCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1, 1)
)
oacRttHistoryCollectionEntry.setIndexNames(
    (0, "OneAccess-RoundTripTime-MIB", "oacRttControlIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttHistoryCollectionLifeIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttHistoryCollectionBucketIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttHistoryCollectionSampleIndex"),
)
if mibBuilder.loadTexts:
    oacRttHistoryCollectionEntry.setStatus("current")


class _OacRttHistoryCollectionLifeIndex_Type(Integer32):
    """Custom type oacRttHistoryCollectionLifeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OacRttHistoryCollectionLifeIndex_Type.__name__ = "Integer32"
_OacRttHistoryCollectionLifeIndex_Object = MibTableColumn
oacRttHistoryCollectionLifeIndex = _OacRttHistoryCollectionLifeIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1, 1, 1),
    _OacRttHistoryCollectionLifeIndex_Type()
)
oacRttHistoryCollectionLifeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttHistoryCollectionLifeIndex.setStatus("current")


class _OacRttHistoryCollectionBucketIndex_Type(Integer32):
    """Custom type oacRttHistoryCollectionBucketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OacRttHistoryCollectionBucketIndex_Type.__name__ = "Integer32"
_OacRttHistoryCollectionBucketIndex_Object = MibTableColumn
oacRttHistoryCollectionBucketIndex = _OacRttHistoryCollectionBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1, 1, 2),
    _OacRttHistoryCollectionBucketIndex_Type()
)
oacRttHistoryCollectionBucketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttHistoryCollectionBucketIndex.setStatus("current")


class _OacRttHistoryCollectionSampleIndex_Type(Integer32):
    """Custom type oacRttHistoryCollectionSampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_OacRttHistoryCollectionSampleIndex_Type.__name__ = "Integer32"
_OacRttHistoryCollectionSampleIndex_Object = MibTableColumn
oacRttHistoryCollectionSampleIndex = _OacRttHistoryCollectionSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1, 1, 3),
    _OacRttHistoryCollectionSampleIndex_Type()
)
oacRttHistoryCollectionSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttHistoryCollectionSampleIndex.setStatus("current")


class _OacRttHistoryCollectionApplSpecificSense_Type(Integer32):
    """Custom type oacRttHistoryCollectionApplSpecificSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 2147483647),
    )


_OacRttHistoryCollectionApplSpecificSense_Type.__name__ = "Integer32"
_OacRttHistoryCollectionApplSpecificSense_Object = MibTableColumn
oacRttHistoryCollectionApplSpecificSense = _OacRttHistoryCollectionApplSpecificSense_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1, 1, 4),
    _OacRttHistoryCollectionApplSpecificSense_Type()
)
oacRttHistoryCollectionApplSpecificSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttHistoryCollectionApplSpecificSense.setStatus("current")
_OacRttHistoryCollectionAddress_Type = OacRttTargetAddress
_OacRttHistoryCollectionAddress_Object = MibTableColumn
oacRttHistoryCollectionAddress = _OacRttHistoryCollectionAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1, 1, 5),
    _OacRttHistoryCollectionAddress_Type()
)
oacRttHistoryCollectionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttHistoryCollectionAddress.setStatus("current")
_OacRttHistoryCollectionSampleTime_Type = TimeStamp
_OacRttHistoryCollectionSampleTime_Object = MibTableColumn
oacRttHistoryCollectionSampleTime = _OacRttHistoryCollectionSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1, 1, 6),
    _OacRttHistoryCollectionSampleTime_Type()
)
oacRttHistoryCollectionSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttHistoryCollectionSampleTime.setStatus("current")
_OacRttHistoryCollectionSense_Type = RttResponseSense
_OacRttHistoryCollectionSense_Object = MibTableColumn
oacRttHistoryCollectionSense = _OacRttHistoryCollectionSense_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1, 1, 7),
    _OacRttHistoryCollectionSense_Type()
)
oacRttHistoryCollectionSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttHistoryCollectionSense.setStatus("current")
_OacRttHistoryCollectionSenseDescription_Type = DisplayString
_OacRttHistoryCollectionSenseDescription_Object = MibTableColumn
oacRttHistoryCollectionSenseDescription = _OacRttHistoryCollectionSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1, 1, 8),
    _OacRttHistoryCollectionSenseDescription_Type()
)
oacRttHistoryCollectionSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttHistoryCollectionSenseDescription.setStatus("current")
_OacRttHistoryCollectionCompletionTime_Type = Gauge32
_OacRttHistoryCollectionCompletionTime_Object = MibTableColumn
oacRttHistoryCollectionCompletionTime = _OacRttHistoryCollectionCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 2, 1, 1, 9),
    _OacRttHistoryCollectionCompletionTime_Type()
)
oacRttHistoryCollectionCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttHistoryCollectionCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    oacRttHistoryCollectionCompletionTime.setUnits("milliseconds")
_OacRttStats_ObjectIdentity = ObjectIdentity
oacRttStats = _OacRttStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3)
)
_OacRttStatsCollectTable_Object = MibTable
oacRttStatsCollectTable = _OacRttStatsCollectTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 1)
)
if mibBuilder.loadTexts:
    oacRttStatsCollectTable.setStatus("current")
_OacRttStatsCollectEntry_Object = MibTableRow
oacRttStatsCollectEntry = _OacRttStatsCollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 1, 1)
)
oacRttStatsCollectEntry.setIndexNames(
    (0, "OneAccess-RoundTripTime-MIB", "oacRttControlIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttStatsCaptureStartTimeIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttStatsCapturePathIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttStatsCaptureHopIndex"),
)
if mibBuilder.loadTexts:
    oacRttStatsCollectEntry.setStatus("current")
_OacRttStatsCollectAddress_Type = OacRttTargetAddress
_OacRttStatsCollectAddress_Object = MibTableColumn
oacRttStatsCollectAddress = _OacRttStatsCollectAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 1, 1, 1),
    _OacRttStatsCollectAddress_Type()
)
oacRttStatsCollectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCollectAddress.setStatus("current")


class _OacRttStatsCollectNoConnections_Type(Integer32):
    """Custom type oacRttStatsCollectNoConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttStatsCollectNoConnections_Type.__name__ = "Integer32"
_OacRttStatsCollectNoConnections_Object = MibTableColumn
oacRttStatsCollectNoConnections = _OacRttStatsCollectNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 1, 1, 2),
    _OacRttStatsCollectNoConnections_Type()
)
oacRttStatsCollectNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCollectNoConnections.setStatus("current")


class _OacRttStatsCollectBusies_Type(Integer32):
    """Custom type oacRttStatsCollectBusies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttStatsCollectBusies_Type.__name__ = "Integer32"
_OacRttStatsCollectBusies_Object = MibTableColumn
oacRttStatsCollectBusies = _OacRttStatsCollectBusies_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 1, 1, 3),
    _OacRttStatsCollectBusies_Type()
)
oacRttStatsCollectBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCollectBusies.setStatus("current")


class _OacRttStatsCollectTimeouts_Type(Integer32):
    """Custom type oacRttStatsCollectTimeouts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttStatsCollectTimeouts_Type.__name__ = "Integer32"
_OacRttStatsCollectTimeouts_Object = MibTableColumn
oacRttStatsCollectTimeouts = _OacRttStatsCollectTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 1, 1, 4),
    _OacRttStatsCollectTimeouts_Type()
)
oacRttStatsCollectTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCollectTimeouts.setStatus("current")


class _OacRttStatsCollectSequenceErrors_Type(Integer32):
    """Custom type oacRttStatsCollectSequenceErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttStatsCollectSequenceErrors_Type.__name__ = "Integer32"
_OacRttStatsCollectSequenceErrors_Object = MibTableColumn
oacRttStatsCollectSequenceErrors = _OacRttStatsCollectSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 1, 1, 5),
    _OacRttStatsCollectSequenceErrors_Type()
)
oacRttStatsCollectSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCollectSequenceErrors.setStatus("current")


class _OacRttStatsCollectNumDisconnects_Type(Integer32):
    """Custom type oacRttStatsCollectNumDisconnects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttStatsCollectNumDisconnects_Type.__name__ = "Integer32"
_OacRttStatsCollectNumDisconnects_Object = MibTableColumn
oacRttStatsCollectNumDisconnects = _OacRttStatsCollectNumDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 1, 1, 6),
    _OacRttStatsCollectNumDisconnects_Type()
)
oacRttStatsCollectNumDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCollectNumDisconnects.setStatus("current")


class _OacRttStatsCollectVerifyErrors_Type(Integer32):
    """Custom type oacRttStatsCollectVerifyErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttStatsCollectVerifyErrors_Type.__name__ = "Integer32"
_OacRttStatsCollectVerifyErrors_Object = MibTableColumn
oacRttStatsCollectVerifyErrors = _OacRttStatsCollectVerifyErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 1, 1, 7),
    _OacRttStatsCollectVerifyErrors_Type()
)
oacRttStatsCollectVerifyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCollectVerifyErrors.setStatus("current")


class _OacRttStatsCollectDrops_Type(Integer32):
    """Custom type oacRttStatsCollectDrops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttStatsCollectDrops_Type.__name__ = "Integer32"
_OacRttStatsCollectDrops_Object = MibTableColumn
oacRttStatsCollectDrops = _OacRttStatsCollectDrops_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 1, 1, 8),
    _OacRttStatsCollectDrops_Type()
)
oacRttStatsCollectDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCollectDrops.setStatus("current")
_OacRttStatsCaptureTable_Object = MibTable
oacRttStatsCaptureTable = _OacRttStatsCaptureTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2)
)
if mibBuilder.loadTexts:
    oacRttStatsCaptureTable.setStatus("current")
_OacRttStatsCaptureEntry_Object = MibTableRow
oacRttStatsCaptureEntry = _OacRttStatsCaptureEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1)
)
oacRttStatsCaptureEntry.setIndexNames(
    (0, "OneAccess-RoundTripTime-MIB", "oacRttControlIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttStatsCaptureStartTimeIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttStatsCapturePathIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttStatsCaptureHopIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttStatsCaptureDistIndex"),
)
if mibBuilder.loadTexts:
    oacRttStatsCaptureEntry.setStatus("current")
_OacRttStatsCaptureStartTimeIndex_Type = TimeStamp
_OacRttStatsCaptureStartTimeIndex_Object = MibTableColumn
oacRttStatsCaptureStartTimeIndex = _OacRttStatsCaptureStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 1),
    _OacRttStatsCaptureStartTimeIndex_Type()
)
oacRttStatsCaptureStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttStatsCaptureStartTimeIndex.setStatus("current")


class _OacRttStatsCapturePathIndex_Type(Integer32):
    """Custom type oacRttStatsCapturePathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_OacRttStatsCapturePathIndex_Type.__name__ = "Integer32"
_OacRttStatsCapturePathIndex_Object = MibTableColumn
oacRttStatsCapturePathIndex = _OacRttStatsCapturePathIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 2),
    _OacRttStatsCapturePathIndex_Type()
)
oacRttStatsCapturePathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttStatsCapturePathIndex.setStatus("current")


class _OacRttStatsCaptureHopIndex_Type(Integer32):
    """Custom type oacRttStatsCaptureHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_OacRttStatsCaptureHopIndex_Type.__name__ = "Integer32"
_OacRttStatsCaptureHopIndex_Object = MibTableColumn
oacRttStatsCaptureHopIndex = _OacRttStatsCaptureHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 3),
    _OacRttStatsCaptureHopIndex_Type()
)
oacRttStatsCaptureHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttStatsCaptureHopIndex.setStatus("current")


class _OacRttStatsCaptureDistIndex_Type(Integer32):
    """Custom type oacRttStatsCaptureDistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OacRttStatsCaptureDistIndex_Type.__name__ = "Integer32"
_OacRttStatsCaptureDistIndex_Object = MibTableColumn
oacRttStatsCaptureDistIndex = _OacRttStatsCaptureDistIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 4),
    _OacRttStatsCaptureDistIndex_Type()
)
oacRttStatsCaptureDistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttStatsCaptureDistIndex.setStatus("current")
_OacRttStatsCaptureSumCompletionTime_Type = Gauge32
_OacRttStatsCaptureSumCompletionTime_Object = MibTableColumn
oacRttStatsCaptureSumCompletionTime = _OacRttStatsCaptureSumCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 5),
    _OacRttStatsCaptureSumCompletionTime_Type()
)
oacRttStatsCaptureSumCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCaptureSumCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    oacRttStatsCaptureSumCompletionTime.setUnits("milliseconds")
_OacRttStatsCaptureSumCompletionTime2Low_Type = Gauge32
_OacRttStatsCaptureSumCompletionTime2Low_Object = MibTableColumn
oacRttStatsCaptureSumCompletionTime2Low = _OacRttStatsCaptureSumCompletionTime2Low_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 6),
    _OacRttStatsCaptureSumCompletionTime2Low_Type()
)
oacRttStatsCaptureSumCompletionTime2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCaptureSumCompletionTime2Low.setStatus("current")
_OacRttStatsCaptureSumCompletionTime2High_Type = Gauge32
_OacRttStatsCaptureSumCompletionTime2High_Object = MibTableColumn
oacRttStatsCaptureSumCompletionTime2High = _OacRttStatsCaptureSumCompletionTime2High_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 7),
    _OacRttStatsCaptureSumCompletionTime2High_Type()
)
oacRttStatsCaptureSumCompletionTime2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCaptureSumCompletionTime2High.setStatus("current")
_OacRttStatsCaptureCompletionTimeMin_Type = Gauge32
_OacRttStatsCaptureCompletionTimeMin_Object = MibTableColumn
oacRttStatsCaptureCompletionTimeMin = _OacRttStatsCaptureCompletionTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 8),
    _OacRttStatsCaptureCompletionTimeMin_Type()
)
oacRttStatsCaptureCompletionTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCaptureCompletionTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    oacRttStatsCaptureCompletionTimeMin.setUnits("milliseconds")
_OacRttStatsCaptureCompletionTimeMax_Type = Gauge32
_OacRttStatsCaptureCompletionTimeMax_Object = MibTableColumn
oacRttStatsCaptureCompletionTimeMax = _OacRttStatsCaptureCompletionTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 9),
    _OacRttStatsCaptureCompletionTimeMax_Type()
)
oacRttStatsCaptureCompletionTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCaptureCompletionTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    oacRttStatsCaptureCompletionTimeMax.setUnits("milliseconds")


class _OacRttStatsCaptureOverThresholds_Type(Integer32):
    """Custom type oacRttStatsCaptureOverThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttStatsCaptureOverThresholds_Type.__name__ = "Integer32"
_OacRttStatsCaptureOverThresholds_Object = MibTableColumn
oacRttStatsCaptureOverThresholds = _OacRttStatsCaptureOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 10),
    _OacRttStatsCaptureOverThresholds_Type()
)
oacRttStatsCaptureOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCaptureOverThresholds.setStatus("current")


class _OacRttStatsCaptureCompletions_Type(Integer32):
    """Custom type oacRttStatsCaptureCompletions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttStatsCaptureCompletions_Type.__name__ = "Integer32"
_OacRttStatsCaptureCompletions_Object = MibTableColumn
oacRttStatsCaptureCompletions = _OacRttStatsCaptureCompletions_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 2, 1, 11),
    _OacRttStatsCaptureCompletions_Type()
)
oacRttStatsCaptureCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsCaptureCompletions.setStatus("current")
_OacRttStatsTotalsTable_Object = MibTable
oacRttStatsTotalsTable = _OacRttStatsTotalsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 3)
)
if mibBuilder.loadTexts:
    oacRttStatsTotalsTable.setStatus("current")
_OacRttStatsTotalsEntry_Object = MibTableRow
oacRttStatsTotalsEntry = _OacRttStatsTotalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 3, 1)
)
oacRttStatsTotalsEntry.setIndexNames(
    (0, "OneAccess-RoundTripTime-MIB", "oacRttControlIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttStatsCaptureStartTimeIndex"),
)
if mibBuilder.loadTexts:
    oacRttStatsTotalsEntry.setStatus("current")


class _OacRttStatsTotalsInitiations_Type(Integer32):
    """Custom type oacRttStatsTotalsInitiations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OacRttStatsTotalsInitiations_Type.__name__ = "Integer32"
_OacRttStatsTotalsInitiations_Object = MibTableColumn
oacRttStatsTotalsInitiations = _OacRttStatsTotalsInitiations_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 3, 1, 1),
    _OacRttStatsTotalsInitiations_Type()
)
oacRttStatsTotalsInitiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsTotalsInitiations.setStatus("current")
_OacRttStatsTotalsElapsedTime_Type = TimeInterval
_OacRttStatsTotalsElapsedTime_Object = MibTableColumn
oacRttStatsTotalsElapsedTime = _OacRttStatsTotalsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 3, 1, 2),
    _OacRttStatsTotalsElapsedTime_Type()
)
oacRttStatsTotalsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsTotalsElapsedTime.setStatus("current")
_OacRttStatsJitterHopTable_Object = MibTable
oacRttStatsJitterHopTable = _OacRttStatsJitterHopTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4)
)
if mibBuilder.loadTexts:
    oacRttStatsJitterHopTable.setStatus("current")
_OacRttStatsJitterHopEntry_Object = MibTableRow
oacRttStatsJitterHopEntry = _OacRttStatsJitterHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1)
)
oacRttStatsJitterHopEntry.setIndexNames(
    (0, "OneAccess-RoundTripTime-MIB", "oacRttControlIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttStatsJitterPathIndex"),
    (0, "OneAccess-RoundTripTime-MIB", "oacRttStatsJitterHopIndex"),
)
if mibBuilder.loadTexts:
    oacRttStatsJitterHopEntry.setStatus("current")


class _OacRttStatsJitterPathIndex_Type(Integer32):
    """Custom type oacRttStatsJitterPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OacRttStatsJitterPathIndex_Type.__name__ = "Integer32"
_OacRttStatsJitterPathIndex_Object = MibTableColumn
oacRttStatsJitterPathIndex = _OacRttStatsJitterPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 1),
    _OacRttStatsJitterPathIndex_Type()
)
oacRttStatsJitterPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttStatsJitterPathIndex.setStatus("current")


class _OacRttStatsJitterHopIndex_Type(Integer32):
    """Custom type oacRttStatsJitterHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OacRttStatsJitterHopIndex_Type.__name__ = "Integer32"
_OacRttStatsJitterHopIndex_Object = MibTableColumn
oacRttStatsJitterHopIndex = _OacRttStatsJitterHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 2),
    _OacRttStatsJitterHopIndex_Type()
)
oacRttStatsJitterHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopIndex.setStatus("current")
_OacRttStatsJitterHopIpAddress_Type = InetAddress
_OacRttStatsJitterHopIpAddress_Object = MibTableColumn
oacRttStatsJitterHopIpAddress = _OacRttStatsJitterHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 3),
    _OacRttStatsJitterHopIpAddress_Type()
)
oacRttStatsJitterHopIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopIpAddress.setStatus("current")
_OacRttStatsJitterHopRTT_Type = Integer32
_OacRttStatsJitterHopRTT_Object = MibTableColumn
oacRttStatsJitterHopRTT = _OacRttStatsJitterHopRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 4),
    _OacRttStatsJitterHopRTT_Type()
)
oacRttStatsJitterHopRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopRTT.setStatus("current")
_OacRttStatsJitterHopPacketLoss_Type = Integer32
_OacRttStatsJitterHopPacketLoss_Object = MibTableColumn
oacRttStatsJitterHopPacketLoss = _OacRttStatsJitterHopPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 5),
    _OacRttStatsJitterHopPacketLoss_Type()
)
oacRttStatsJitterHopPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopPacketLoss.setStatus("current")
_OacRttStatsJitterHopJitter_Type = Integer32
_OacRttStatsJitterHopJitter_Object = MibTableColumn
oacRttStatsJitterHopJitter = _OacRttStatsJitterHopJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 6),
    _OacRttStatsJitterHopJitter_Type()
)
oacRttStatsJitterHopJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopJitter.setStatus("current")
_OacRttStatsJitterHopMinRTT_Type = Integer32
_OacRttStatsJitterHopMinRTT_Object = MibTableColumn
oacRttStatsJitterHopMinRTT = _OacRttStatsJitterHopMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 7),
    _OacRttStatsJitterHopMinRTT_Type()
)
oacRttStatsJitterHopMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopMinRTT.setStatus("current")
_OacRttStatsJitterHopMaxRTT_Type = Integer32
_OacRttStatsJitterHopMaxRTT_Object = MibTableColumn
oacRttStatsJitterHopMaxRTT = _OacRttStatsJitterHopMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 8),
    _OacRttStatsJitterHopMaxRTT_Type()
)
oacRttStatsJitterHopMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopMaxRTT.setStatus("current")
_OacRttStatsJitterHopSumRTT_Type = Integer32
_OacRttStatsJitterHopSumRTT_Object = MibTableColumn
oacRttStatsJitterHopSumRTT = _OacRttStatsJitterHopSumRTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 9),
    _OacRttStatsJitterHopSumRTT_Type()
)
oacRttStatsJitterHopSumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopSumRTT.setStatus("current")
_OacRttStatsJitterHopSum2RTT_Type = Integer32
_OacRttStatsJitterHopSum2RTT_Object = MibTableColumn
oacRttStatsJitterHopSum2RTT = _OacRttStatsJitterHopSum2RTT_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 10),
    _OacRttStatsJitterHopSum2RTT_Type()
)
oacRttStatsJitterHopSum2RTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopSum2RTT.setStatus("current")
_OacRttStatsJitterHopMinPosJitter_Type = Integer32
_OacRttStatsJitterHopMinPosJitter_Object = MibTableColumn
oacRttStatsJitterHopMinPosJitter = _OacRttStatsJitterHopMinPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 11),
    _OacRttStatsJitterHopMinPosJitter_Type()
)
oacRttStatsJitterHopMinPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopMinPosJitter.setStatus("current")
_OacRttStatsJitterHopMaxPosJitter_Type = Integer32
_OacRttStatsJitterHopMaxPosJitter_Object = MibTableColumn
oacRttStatsJitterHopMaxPosJitter = _OacRttStatsJitterHopMaxPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 12),
    _OacRttStatsJitterHopMaxPosJitter_Type()
)
oacRttStatsJitterHopMaxPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopMaxPosJitter.setStatus("current")
_OacRttStatsJitterHopSumPos_Type = Integer32
_OacRttStatsJitterHopSumPos_Object = MibTableColumn
oacRttStatsJitterHopSumPos = _OacRttStatsJitterHopSumPos_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 13),
    _OacRttStatsJitterHopSumPos_Type()
)
oacRttStatsJitterHopSumPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopSumPos.setStatus("current")
_OacRttStatsJitterHopSum2Pos_Type = Integer32
_OacRttStatsJitterHopSum2Pos_Object = MibTableColumn
oacRttStatsJitterHopSum2Pos = _OacRttStatsJitterHopSum2Pos_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 14),
    _OacRttStatsJitterHopSum2Pos_Type()
)
oacRttStatsJitterHopSum2Pos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopSum2Pos.setStatus("current")
_OacRttStatsJitterHopMinNegJitter_Type = Integer32
_OacRttStatsJitterHopMinNegJitter_Object = MibTableColumn
oacRttStatsJitterHopMinNegJitter = _OacRttStatsJitterHopMinNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 15),
    _OacRttStatsJitterHopMinNegJitter_Type()
)
oacRttStatsJitterHopMinNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopMinNegJitter.setStatus("current")
_OacRttStatsJitterHopMaxNegJitter_Type = Integer32
_OacRttStatsJitterHopMaxNegJitter_Object = MibTableColumn
oacRttStatsJitterHopMaxNegJitter = _OacRttStatsJitterHopMaxNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 16),
    _OacRttStatsJitterHopMaxNegJitter_Type()
)
oacRttStatsJitterHopMaxNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopMaxNegJitter.setStatus("current")
_OacRttStatsJitterHopSumNeg_Type = Integer32
_OacRttStatsJitterHopSumNeg_Object = MibTableColumn
oacRttStatsJitterHopSumNeg = _OacRttStatsJitterHopSumNeg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 17),
    _OacRttStatsJitterHopSumNeg_Type()
)
oacRttStatsJitterHopSumNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopSumNeg.setStatus("current")
_OacRttStatsJitterHopSum2Neg_Type = Integer32
_OacRttStatsJitterHopSum2Neg_Object = MibTableColumn
oacRttStatsJitterHopSum2Neg = _OacRttStatsJitterHopSum2Neg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 18),
    _OacRttStatsJitterHopSum2Neg_Type()
)
oacRttStatsJitterHopSum2Neg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopSum2Neg.setStatus("current")
_OacRttStatsJitterHopOutOfSequence_Type = Integer32
_OacRttStatsJitterHopOutOfSequence_Object = MibTableColumn
oacRttStatsJitterHopOutOfSequence = _OacRttStatsJitterHopOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 19),
    _OacRttStatsJitterHopOutOfSequence_Type()
)
oacRttStatsJitterHopOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopOutOfSequence.setStatus("current")
_OacRttStatsJitterHopDiscardedSamples_Type = Integer32
_OacRttStatsJitterHopDiscardedSamples_Object = MibTableColumn
oacRttStatsJitterHopDiscardedSamples = _OacRttStatsJitterHopDiscardedSamples_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 3, 4, 1, 20),
    _OacRttStatsJitterHopDiscardedSamples_Type()
)
oacRttStatsJitterHopDiscardedSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttStatsJitterHopDiscardedSamples.setStatus("current")
_OacRttAppl_ObjectIdentity = ObjectIdentity
oacRttAppl = _OacRttAppl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 4)
)
_OacRttApplVersion_Type = DisplayString
_OacRttApplVersion_Object = MibScalar
oacRttApplVersion = _OacRttApplVersion_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 4, 1),
    _OacRttApplVersion_Type()
)
oacRttApplVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttApplVersion.setStatus("current")
_OacRttApplSuppRttTypesTable_Object = MibTable
oacRttApplSuppRttTypesTable = _OacRttApplSuppRttTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 4, 2)
)
if mibBuilder.loadTexts:
    oacRttApplSuppRttTypesTable.setStatus("current")
_OacRttApplSuppRttTypesEntry_Object = MibTableRow
oacRttApplSuppRttTypesEntry = _OacRttApplSuppRttTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 4, 2, 1)
)
oacRttApplSuppRttTypesEntry.setIndexNames(
    (0, "OneAccess-RoundTripTime-MIB", "oacRttApplSuppRttTypes"),
)
if mibBuilder.loadTexts:
    oacRttApplSuppRttTypesEntry.setStatus("current")
_OacRttApplSuppRttTypes_Type = OacRttApplType
_OacRttApplSuppRttTypes_Object = MibTableColumn
oacRttApplSuppRttTypes = _OacRttApplSuppRttTypes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 4, 2, 1, 1),
    _OacRttApplSuppRttTypes_Type()
)
oacRttApplSuppRttTypes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttApplSuppRttTypes.setStatus("current")
_OacRttApplSuppRttTypesValid_Type = TruthValue
_OacRttApplSuppRttTypesValid_Object = MibTableColumn
oacRttApplSuppRttTypesValid = _OacRttApplSuppRttTypesValid_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 4, 2, 1, 2),
    _OacRttApplSuppRttTypesValid_Type()
)
oacRttApplSuppRttTypesValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttApplSuppRttTypesValid.setStatus("current")
_OacRttApplSuppProtocolsTable_Object = MibTable
oacRttApplSuppProtocolsTable = _OacRttApplSuppProtocolsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 4, 3)
)
if mibBuilder.loadTexts:
    oacRttApplSuppProtocolsTable.setStatus("current")
_OacRttApplSuppProtocolsEntry_Object = MibTableRow
oacRttApplSuppProtocolsEntry = _OacRttApplSuppProtocolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 4, 3, 1)
)
oacRttApplSuppProtocolsEntry.setIndexNames(
    (0, "OneAccess-RoundTripTime-MIB", "oacRttApplSuppProtocols"),
)
if mibBuilder.loadTexts:
    oacRttApplSuppProtocolsEntry.setStatus("current")
_OacRttApplSuppProtocols_Type = OacRttApplProtocol
_OacRttApplSuppProtocols_Object = MibTableColumn
oacRttApplSuppProtocols = _OacRttApplSuppProtocols_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 4, 3, 1, 1),
    _OacRttApplSuppProtocols_Type()
)
oacRttApplSuppProtocols.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacRttApplSuppProtocols.setStatus("current")
_OacRttApplSuppProtocolsValid_Type = TruthValue
_OacRttApplSuppProtocolsValid_Object = MibTableColumn
oacRttApplSuppProtocolsValid = _OacRttApplSuppProtocolsValid_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 1, 4, 3, 1, 2),
    _OacRttApplSuppProtocolsValid_Type()
)
oacRttApplSuppProtocolsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacRttApplSuppProtocolsValid.setStatus("current")
_OacRttNotificationsPrefix_ObjectIdentity = ObjectIdentity
oacRttNotificationsPrefix = _OacRttNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 2)
)
_OacRttNotifications_ObjectIdentity = ObjectIdentity
oacRttNotifications = _OacRttNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 2, 0)
)
oacRttControlEntry.registerAugmentions(
    ("OneAccess-RoundTripTime-MIB",
     "oacRttHistoryEntry")
)
oacRttHistoryEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttControlEntry.registerAugmentions(
    ("OneAccess-RoundTripTime-MIB",
     "oacRttSchedEntry")
)
oacRttSchedEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttControlEntry.registerAugmentions(
    ("OneAccess-RoundTripTime-MIB",
     "oacRttReactEntry")
)
oacRttReactEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttControlEntry.registerAugmentions(
    ("OneAccess-RoundTripTime-MIB",
     "oacRttStatisticsEntry")
)
oacRttStatisticsEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttControlEntry.registerAugmentions(
    ("OneAccess-RoundTripTime-MIB",
     "oacRttControlOperEntry")
)
oacRttControlOperEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttReactTriggerEntry.registerAugmentions(
    ("OneAccess-RoundTripTime-MIB",
     "oacRttReactTriggerOperEntry")
)
oacRttReactTriggerOperEntry.setIndexNames(*oacRttReactTriggerEntry.getIndexNames())
oacRttControlEntry.registerAugmentions(
    ("OneAccess-RoundTripTime-MIB",
     "oacRttLatestRttOperEntry")
)
oacRttLatestRttOperEntry.setIndexNames(*oacRttControlEntry.getIndexNames())

# Managed Objects groups


# Notification objects

oacRttConnectionChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 2, 0, 1)
)
oacRttConnectionChangeNotification.setObjects(
      *(("OneAccess-RoundTripTime-MIB", "oacRttControlTag"),
        ("OneAccess-RoundTripTime-MIB", "oacRttHistoryCollectionAddress"),
        ("OneAccess-RoundTripTime-MIB", "oacRttControlOperConnLostOccurred"))
)
if mibBuilder.loadTexts:
    oacRttConnectionChangeNotification.setStatus(
        "current"
    )

oacRttTimeoutNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 2, 0, 2)
)
oacRttTimeoutNotification.setObjects(
      *(("OneAccess-RoundTripTime-MIB", "oacRttControlTag"),
        ("OneAccess-RoundTripTime-MIB", "oacRttHistoryCollectionAddress"),
        ("OneAccess-RoundTripTime-MIB", "oacRttControlOperTimeoutOccurred"))
)
if mibBuilder.loadTexts:
    oacRttTimeoutNotification.setStatus(
        "current"
    )

oacRttThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1223, 2, 0, 3)
)
oacRttThresholdNotification.setObjects(
      *(("OneAccess-RoundTripTime-MIB", "oacRttControlTag"),
        ("OneAccess-RoundTripTime-MIB", "oacRttHistoryCollectionAddress"),
        ("OneAccess-RoundTripTime-MIB", "oacRttControlOperOverThresholdOccurred"))
)
if mibBuilder.loadTexts:
    oacRttThresholdNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OneAccess-RoundTripTime-MIB",
    **{"RttResponseSense": RttResponseSense,
       "OacRttRttType": OacRttRttType,
       "OacRttProtocol": OacRttProtocol,
       "OacRttTargetAddress": OacRttTargetAddress,
       "OacRttApplType": OacRttApplType,
       "OacRttApplProtocol": OacRttApplProtocol,
       "oacRttChkMIB": oacRttChkMIB,
       "oacRttChkObj": oacRttChkObj,
       "oacRttControl": oacRttControl,
       "oacRttControlTable": oacRttControlTable,
       "oacRttControlEntry": oacRttControlEntry,
       "oacRttControlIndex": oacRttControlIndex,
       "oacRttControlStatus": oacRttControlStatus,
       "oacRttControlTag": oacRttControlTag,
       "oacRttControlFrequency": oacRttControlFrequency,
       "oacRttControlRttType": oacRttControlRttType,
       "oacRttControlTimeout": oacRttControlTimeout,
       "oacRttControlOwner": oacRttControlOwner,
       "oacRttControlThreshold": oacRttControlThreshold,
       "oacRttEchoTable": oacRttEchoTable,
       "oacRttEchoEntry": oacRttEchoEntry,
       "oacRttEchoSourceAddress": oacRttEchoSourceAddress,
       "oacRttEchoTargetAddress": oacRttEchoTargetAddress,
       "oacRttEchoPktDataRequestSize": oacRttEchoPktDataRequestSize,
       "oacRttEchoPktDataResponseSize": oacRttEchoPktDataResponseSize,
       "oacRttEchoTOS": oacRttEchoTOS,
       "oacRttEchoProtocol": oacRttEchoProtocol,
       "oacRttHistoryTable": oacRttHistoryTable,
       "oacRttHistoryEntry": oacRttHistoryEntry,
       "oacRttHistoryNumBuckets": oacRttHistoryNumBuckets,
       "oacRttHistoryFilter": oacRttHistoryFilter,
       "oacRttHistoryNumLives": oacRttHistoryNumLives,
       "oacRttHistoryNumSamples": oacRttHistoryNumSamples,
       "oacRttSchedTable": oacRttSchedTable,
       "oacRttSchedEntry": oacRttSchedEntry,
       "oacRttSchedRttStartTime": oacRttSchedRttStartTime,
       "oacRttSchedRttLife": oacRttSchedRttLife,
       "oacRttSchedConceptRowAgeout": oacRttSchedConceptRowAgeout,
       "oacRttReactTable": oacRttReactTable,
       "oacRttReactEntry": oacRttReactEntry,
       "oacRttReactActionType": oacRttReactActionType,
       "oacRttReactThresholdType": oacRttReactThresholdType,
       "oacRttReactThresholdCount": oacRttReactThresholdCount,
       "oacRttReactThresholdCount2": oacRttReactThresholdCount2,
       "oacRttReactConnectionEnable": oacRttReactConnectionEnable,
       "oacRttReactVerifyErrorEnable": oacRttReactVerifyErrorEnable,
       "oacRttReactThresholdFalling": oacRttReactThresholdFalling,
       "oacRttReactTimeoutEnable": oacRttReactTimeoutEnable,
       "oacRttStatisticsTable": oacRttStatisticsTable,
       "oacRttStatisticsEntry": oacRttStatisticsEntry,
       "oacRttStatisticsNumDistBuckets": oacRttStatisticsNumDistBuckets,
       "oacRttStatisticsNumHops": oacRttStatisticsNumHops,
       "oacRttStatisticsNumPaths": oacRttStatisticsNumPaths,
       "oacRttStatisticsDistInterval": oacRttStatisticsDistInterval,
       "oacRttStatisticsNumHourGroups": oacRttStatisticsNumHourGroups,
       "oacRttControlOperTable": oacRttControlOperTable,
       "oacRttControlOperEntry": oacRttControlOperEntry,
       "oacRttControlOperNumRtts": oacRttControlOperNumRtts,
       "oacRttControlOperOctetsInUse": oacRttControlOperOctetsInUse,
       "oacRttControlOperDiagText": oacRttControlOperDiagText,
       "oacRttControlOperOverThresholdOccurred": oacRttControlOperOverThresholdOccurred,
       "oacRttControlOperState": oacRttControlOperState,
       "oacRttControlOperTimeoutOccurred": oacRttControlOperTimeoutOccurred,
       "oacRttControlOperRttLife": oacRttControlOperRttLife,
       "oacRttControlOperModificationTime": oacRttControlOperModificationTime,
       "oacRttControlOperConnLostOccurred": oacRttControlOperConnLostOccurred,
       "oacRttControlOperResetTime": oacRttControlOperResetTime,
       "oacRttReactTriggerTable": oacRttReactTriggerTable,
       "oacRttReactTriggerEntry": oacRttReactTriggerEntry,
       "oacRttReactTriggerOacRttControlIndex": oacRttReactTriggerOacRttControlIndex,
       "oacRttReactTriggerStatus": oacRttReactTriggerStatus,
       "oacRttReactTriggerOperTable": oacRttReactTriggerOperTable,
       "oacRttReactTriggerOperEntry": oacRttReactTriggerOperEntry,
       "oacRttReactTriggerOperState": oacRttReactTriggerOperState,
       "oacRttLatestRttOperTable": oacRttLatestRttOperTable,
       "oacRttLatestRttOperEntry": oacRttLatestRttOperEntry,
       "oacRttLatestRttOperTime": oacRttLatestRttOperTime,
       "oacRttLatestRttOperSense": oacRttLatestRttOperSense,
       "oacRttLatestRttOperSenseDescription": oacRttLatestRttOperSenseDescription,
       "oacRttLatestRttOperAddress": oacRttLatestRttOperAddress,
       "oacRttLatestRttOperCompletionTime": oacRttLatestRttOperCompletionTime,
       "oacRttLatestRttOperApplSpecificSense": oacRttLatestRttOperApplSpecificSense,
       "oacRttHistory": oacRttHistory,
       "oacRttHistoryCollectionTable": oacRttHistoryCollectionTable,
       "oacRttHistoryCollectionEntry": oacRttHistoryCollectionEntry,
       "oacRttHistoryCollectionLifeIndex": oacRttHistoryCollectionLifeIndex,
       "oacRttHistoryCollectionBucketIndex": oacRttHistoryCollectionBucketIndex,
       "oacRttHistoryCollectionSampleIndex": oacRttHistoryCollectionSampleIndex,
       "oacRttHistoryCollectionApplSpecificSense": oacRttHistoryCollectionApplSpecificSense,
       "oacRttHistoryCollectionAddress": oacRttHistoryCollectionAddress,
       "oacRttHistoryCollectionSampleTime": oacRttHistoryCollectionSampleTime,
       "oacRttHistoryCollectionSense": oacRttHistoryCollectionSense,
       "oacRttHistoryCollectionSenseDescription": oacRttHistoryCollectionSenseDescription,
       "oacRttHistoryCollectionCompletionTime": oacRttHistoryCollectionCompletionTime,
       "oacRttStats": oacRttStats,
       "oacRttStatsCollectTable": oacRttStatsCollectTable,
       "oacRttStatsCollectEntry": oacRttStatsCollectEntry,
       "oacRttStatsCollectAddress": oacRttStatsCollectAddress,
       "oacRttStatsCollectNoConnections": oacRttStatsCollectNoConnections,
       "oacRttStatsCollectBusies": oacRttStatsCollectBusies,
       "oacRttStatsCollectTimeouts": oacRttStatsCollectTimeouts,
       "oacRttStatsCollectSequenceErrors": oacRttStatsCollectSequenceErrors,
       "oacRttStatsCollectNumDisconnects": oacRttStatsCollectNumDisconnects,
       "oacRttStatsCollectVerifyErrors": oacRttStatsCollectVerifyErrors,
       "oacRttStatsCollectDrops": oacRttStatsCollectDrops,
       "oacRttStatsCaptureTable": oacRttStatsCaptureTable,
       "oacRttStatsCaptureEntry": oacRttStatsCaptureEntry,
       "oacRttStatsCaptureStartTimeIndex": oacRttStatsCaptureStartTimeIndex,
       "oacRttStatsCapturePathIndex": oacRttStatsCapturePathIndex,
       "oacRttStatsCaptureHopIndex": oacRttStatsCaptureHopIndex,
       "oacRttStatsCaptureDistIndex": oacRttStatsCaptureDistIndex,
       "oacRttStatsCaptureSumCompletionTime": oacRttStatsCaptureSumCompletionTime,
       "oacRttStatsCaptureSumCompletionTime2Low": oacRttStatsCaptureSumCompletionTime2Low,
       "oacRttStatsCaptureSumCompletionTime2High": oacRttStatsCaptureSumCompletionTime2High,
       "oacRttStatsCaptureCompletionTimeMin": oacRttStatsCaptureCompletionTimeMin,
       "oacRttStatsCaptureCompletionTimeMax": oacRttStatsCaptureCompletionTimeMax,
       "oacRttStatsCaptureOverThresholds": oacRttStatsCaptureOverThresholds,
       "oacRttStatsCaptureCompletions": oacRttStatsCaptureCompletions,
       "oacRttStatsTotalsTable": oacRttStatsTotalsTable,
       "oacRttStatsTotalsEntry": oacRttStatsTotalsEntry,
       "oacRttStatsTotalsInitiations": oacRttStatsTotalsInitiations,
       "oacRttStatsTotalsElapsedTime": oacRttStatsTotalsElapsedTime,
       "oacRttStatsJitterHopTable": oacRttStatsJitterHopTable,
       "oacRttStatsJitterHopEntry": oacRttStatsJitterHopEntry,
       "oacRttStatsJitterPathIndex": oacRttStatsJitterPathIndex,
       "oacRttStatsJitterHopIndex": oacRttStatsJitterHopIndex,
       "oacRttStatsJitterHopIpAddress": oacRttStatsJitterHopIpAddress,
       "oacRttStatsJitterHopRTT": oacRttStatsJitterHopRTT,
       "oacRttStatsJitterHopPacketLoss": oacRttStatsJitterHopPacketLoss,
       "oacRttStatsJitterHopJitter": oacRttStatsJitterHopJitter,
       "oacRttStatsJitterHopMinRTT": oacRttStatsJitterHopMinRTT,
       "oacRttStatsJitterHopMaxRTT": oacRttStatsJitterHopMaxRTT,
       "oacRttStatsJitterHopSumRTT": oacRttStatsJitterHopSumRTT,
       "oacRttStatsJitterHopSum2RTT": oacRttStatsJitterHopSum2RTT,
       "oacRttStatsJitterHopMinPosJitter": oacRttStatsJitterHopMinPosJitter,
       "oacRttStatsJitterHopMaxPosJitter": oacRttStatsJitterHopMaxPosJitter,
       "oacRttStatsJitterHopSumPos": oacRttStatsJitterHopSumPos,
       "oacRttStatsJitterHopSum2Pos": oacRttStatsJitterHopSum2Pos,
       "oacRttStatsJitterHopMinNegJitter": oacRttStatsJitterHopMinNegJitter,
       "oacRttStatsJitterHopMaxNegJitter": oacRttStatsJitterHopMaxNegJitter,
       "oacRttStatsJitterHopSumNeg": oacRttStatsJitterHopSumNeg,
       "oacRttStatsJitterHopSum2Neg": oacRttStatsJitterHopSum2Neg,
       "oacRttStatsJitterHopOutOfSequence": oacRttStatsJitterHopOutOfSequence,
       "oacRttStatsJitterHopDiscardedSamples": oacRttStatsJitterHopDiscardedSamples,
       "oacRttAppl": oacRttAppl,
       "oacRttApplVersion": oacRttApplVersion,
       "oacRttApplSuppRttTypesTable": oacRttApplSuppRttTypesTable,
       "oacRttApplSuppRttTypesEntry": oacRttApplSuppRttTypesEntry,
       "oacRttApplSuppRttTypes": oacRttApplSuppRttTypes,
       "oacRttApplSuppRttTypesValid": oacRttApplSuppRttTypesValid,
       "oacRttApplSuppProtocolsTable": oacRttApplSuppProtocolsTable,
       "oacRttApplSuppProtocolsEntry": oacRttApplSuppProtocolsEntry,
       "oacRttApplSuppProtocols": oacRttApplSuppProtocols,
       "oacRttApplSuppProtocolsValid": oacRttApplSuppProtocolsValid,
       "oacRttNotificationsPrefix": oacRttNotificationsPrefix,
       "oacRttNotifications": oacRttNotifications,
       "oacRttConnectionChangeNotification": oacRttConnectionChangeNotification,
       "oacRttTimeoutNotification": oacRttTimeoutNotification,
       "oacRttThresholdNotification": oacRttThresholdNotification}
)
