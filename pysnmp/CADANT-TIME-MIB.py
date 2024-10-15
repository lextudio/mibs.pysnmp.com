# SNMP MIB module (CADANT-TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-TIME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:14 2024
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

(cadSystem,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadSystem")

(CadDouble,) = mibBuilder.importSymbols(
    "CADANT-TC",
    "CadDouble")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadTimeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2)
)
cadTimeMib.setRevisions(
        ("2015-10-19 00:00",
         "2011-02-07 00:00",
         "2006-03-07 00:00",
         "2005-07-26 00:00",
         "2003-09-11 00:00",
         "2003-04-29 00:00",
         "2002-10-28 00:00",
         "2002-10-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadClock_ObjectIdentity = ObjectIdentity
cadClock = _CadClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 1)
)


class _CadTimeZone_Type(DisplayString):
    """Custom type cadTimeZone based on DisplayString"""
    defaultValue = OctetString("GMT")


_CadTimeZone_Object = MibScalar
cadTimeZone = _CadTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 1, 1),
    _CadTimeZone_Type()
)
cadTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadTimeZone.setStatus("current")


class _CadIsDST_Type(TruthValue):
    """Custom type cadIsDST based on TruthValue"""


_CadIsDST_Object = MibScalar
cadIsDST = _CadIsDST_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 1, 2),
    _CadIsDST_Type()
)
cadIsDST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIsDST.setStatus("current")
_CadTZAbbrev_Type = DisplayString
_CadTZAbbrev_Object = MibScalar
cadTZAbbrev = _CadTZAbbrev_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 1, 3),
    _CadTZAbbrev_Type()
)
cadTZAbbrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadTZAbbrev.setStatus("current")
_CadLocalDateAndTime_Type = DateAndTime
_CadLocalDateAndTime_Object = MibScalar
cadLocalDateAndTime = _CadLocalDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 1, 4),
    _CadLocalDateAndTime_Type()
)
cadLocalDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLocalDateAndTime.setStatus("current")
_CadLocalTime_Type = Unsigned32
_CadLocalTime_Object = MibScalar
cadLocalTime = _CadLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 1, 5),
    _CadLocalTime_Type()
)
cadLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadLocalTime.setStatus("current")
_CadUTCtime_Type = Unsigned32
_CadUTCtime_Object = MibScalar
cadUTCtime = _CadUTCtime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 1, 6),
    _CadUTCtime_Type()
)
cadUTCtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadUTCtime.setStatus("current")


class _CadNetTimeSyncProto_Type(Integer32):
    """Custom type cadNetTimeSyncProto based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ntp", 2),
          ("tod", 1))
    )


_CadNetTimeSyncProto_Type.__name__ = "Integer32"
_CadNetTimeSyncProto_Object = MibScalar
cadNetTimeSyncProto = _CadNetTimeSyncProto_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 1, 7),
    _CadNetTimeSyncProto_Type()
)
cadNetTimeSyncProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadNetTimeSyncProto.setStatus("current")
_CadTod_ObjectIdentity = ObjectIdentity
cadTod = _CadTod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 2)
)


class _CadTodServerIpAddress_Type(IpAddress):
    """Custom type cadTodServerIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_CadTodServerIpAddress_Object = MibScalar
cadTodServerIpAddress = _CadTodServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 2, 1),
    _CadTodServerIpAddress_Type()
)
cadTodServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadTodServerIpAddress.setStatus("current")


class _CadTodServerConnType_Type(Integer32):
    """Custom type cadTodServerConnType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_CadTodServerConnType_Type.__name__ = "Integer32"
_CadTodServerConnType_Object = MibScalar
cadTodServerConnType = _CadTodServerConnType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 2, 2),
    _CadTodServerConnType_Type()
)
cadTodServerConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadTodServerConnType.setStatus("current")
_CadNtp_ObjectIdentity = ObjectIdentity
cadNtp = _CadNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3)
)


class _CadNtpVersionDefault_Type(Integer32):
    """Custom type cadNtpVersionDefault based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_CadNtpVersionDefault_Type.__name__ = "Integer32"
_CadNtpVersionDefault_Object = MibScalar
cadNtpVersionDefault = _CadNtpVersionDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 1),
    _CadNtpVersionDefault_Type()
)
cadNtpVersionDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadNtpVersionDefault.setStatus("current")


class _CadNtpAuthenticate_Type(TruthValue):
    """Custom type cadNtpAuthenticate based on TruthValue"""


_CadNtpAuthenticate_Object = MibScalar
cadNtpAuthenticate = _CadNtpAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 2),
    _CadNtpAuthenticate_Type()
)
cadNtpAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadNtpAuthenticate.setStatus("current")
_CadNtpClockDrift_Type = CadDouble
_CadNtpClockDrift_Object = MibScalar
cadNtpClockDrift = _CadNtpClockDrift_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 3),
    _CadNtpClockDrift_Type()
)
cadNtpClockDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadNtpClockDrift.setStatus("current")
_CadNtpSource_ObjectIdentity = ObjectIdentity
cadNtpSource = _CadNtpSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10)
)


class _CadNtpSourceMinPollDefault_Type(Integer32):
    """Custom type cadNtpSourceMinPollDefault based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 11),
    )


_CadNtpSourceMinPollDefault_Type.__name__ = "Integer32"
_CadNtpSourceMinPollDefault_Object = MibScalar
cadNtpSourceMinPollDefault = _CadNtpSourceMinPollDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 1),
    _CadNtpSourceMinPollDefault_Type()
)
cadNtpSourceMinPollDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadNtpSourceMinPollDefault.setStatus("current")


class _CadNtpSourceMaxPollDefault_Type(Integer32):
    """Custom type cadNtpSourceMaxPollDefault based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 11),
    )


_CadNtpSourceMaxPollDefault_Type.__name__ = "Integer32"
_CadNtpSourceMaxPollDefault_Object = MibScalar
cadNtpSourceMaxPollDefault = _CadNtpSourceMaxPollDefault_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 2),
    _CadNtpSourceMaxPollDefault_Type()
)
cadNtpSourceMaxPollDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadNtpSourceMaxPollDefault.setStatus("current")
_CadNtpSourceTable_Object = MibTable
cadNtpSourceTable = _CadNtpSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10)
)
if mibBuilder.loadTexts:
    cadNtpSourceTable.setStatus("current")
_CadNtpSourceEntry_Object = MibTableRow
cadNtpSourceEntry = _CadNtpSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1)
)
cadNtpSourceEntry.setIndexNames(
    (0, "CADANT-TIME-MIB", "cadNtpSourceIpAddress"),
)
if mibBuilder.loadTexts:
    cadNtpSourceEntry.setStatus("current")
_CadNtpSourceIpAddress_Type = IpAddress
_CadNtpSourceIpAddress_Object = MibTableColumn
cadNtpSourceIpAddress = _CadNtpSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1, 1),
    _CadNtpSourceIpAddress_Type()
)
cadNtpSourceIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadNtpSourceIpAddress.setStatus("current")


class _CadNtpSourceType_Type(Integer32):
    """Custom type cadNtpSourceType based on Integer32"""
    defaultValue = 1

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
        *(("broadcastServer", 2),
          ("manycastPeer", 6),
          ("manycastServer", 4),
          ("multicastServer", 3),
          ("unicastPeer", 5),
          ("unicastServer", 1))
    )


_CadNtpSourceType_Type.__name__ = "Integer32"
_CadNtpSourceType_Object = MibTableColumn
cadNtpSourceType = _CadNtpSourceType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1, 2),
    _CadNtpSourceType_Type()
)
cadNtpSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpSourceType.setStatus("current")


class _CadNtpSourceBurstEnabled_Type(TruthValue):
    """Custom type cadNtpSourceBurstEnabled based on TruthValue"""


_CadNtpSourceBurstEnabled_Object = MibTableColumn
cadNtpSourceBurstEnabled = _CadNtpSourceBurstEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1, 3),
    _CadNtpSourceBurstEnabled_Type()
)
cadNtpSourceBurstEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpSourceBurstEnabled.setStatus("current")


class _CadNtpSourcePreferred_Type(TruthValue):
    """Custom type cadNtpSourcePreferred based on TruthValue"""


_CadNtpSourcePreferred_Object = MibTableColumn
cadNtpSourcePreferred = _CadNtpSourcePreferred_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1, 4),
    _CadNtpSourcePreferred_Type()
)
cadNtpSourcePreferred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpSourcePreferred.setStatus("current")


class _CadNtpSourceAuthKeyId_Type(Unsigned32):
    """Custom type cadNtpSourceAuthKeyId based on Unsigned32"""
    defaultValue = 0


_CadNtpSourceAuthKeyId_Object = MibTableColumn
cadNtpSourceAuthKeyId = _CadNtpSourceAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1, 5),
    _CadNtpSourceAuthKeyId_Type()
)
cadNtpSourceAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpSourceAuthKeyId.setStatus("current")


class _CadNtpSourceMinPoll_Type(Integer32):
    """Custom type cadNtpSourceMinPoll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 11),
    )


_CadNtpSourceMinPoll_Type.__name__ = "Integer32"
_CadNtpSourceMinPoll_Object = MibTableColumn
cadNtpSourceMinPoll = _CadNtpSourceMinPoll_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1, 6),
    _CadNtpSourceMinPoll_Type()
)
cadNtpSourceMinPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpSourceMinPoll.setStatus("current")


class _CadNtpSourceMaxPoll_Type(Integer32):
    """Custom type cadNtpSourceMaxPoll based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 11),
    )


_CadNtpSourceMaxPoll_Type.__name__ = "Integer32"
_CadNtpSourceMaxPoll_Object = MibTableColumn
cadNtpSourceMaxPoll = _CadNtpSourceMaxPoll_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1, 7),
    _CadNtpSourceMaxPoll_Type()
)
cadNtpSourceMaxPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpSourceMaxPoll.setStatus("current")


class _CadNtpSourceVersion_Type(Integer32):
    """Custom type cadNtpSourceVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4),
    )


_CadNtpSourceVersion_Type.__name__ = "Integer32"
_CadNtpSourceVersion_Object = MibTableColumn
cadNtpSourceVersion = _CadNtpSourceVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1, 8),
    _CadNtpSourceVersion_Type()
)
cadNtpSourceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpSourceVersion.setStatus("current")


class _CadNtpSourceTtl_Type(Integer32):
    """Custom type cadNtpSourceTtl based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CadNtpSourceTtl_Type.__name__ = "Integer32"
_CadNtpSourceTtl_Object = MibTableColumn
cadNtpSourceTtl = _CadNtpSourceTtl_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1, 9),
    _CadNtpSourceTtl_Type()
)
cadNtpSourceTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpSourceTtl.setStatus("current")


class _CadNtpSourceRowStatus_Type(RowStatus):
    """Custom type cadNtpSourceRowStatus based on RowStatus"""


_CadNtpSourceRowStatus_Object = MibTableColumn
cadNtpSourceRowStatus = _CadNtpSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 10, 10, 1, 10),
    _CadNtpSourceRowStatus_Type()
)
cadNtpSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpSourceRowStatus.setStatus("current")
_CadNtpAuthKeyTable_Object = MibTable
cadNtpAuthKeyTable = _CadNtpAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 30)
)
if mibBuilder.loadTexts:
    cadNtpAuthKeyTable.setStatus("current")
_CadNtpAuthKeyEntry_Object = MibTableRow
cadNtpAuthKeyEntry = _CadNtpAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 30, 1)
)
cadNtpAuthKeyEntry.setIndexNames(
    (0, "CADANT-TIME-MIB", "cadNtpAuthKeyId"),
)
if mibBuilder.loadTexts:
    cadNtpAuthKeyEntry.setStatus("current")


class _CadNtpAuthKeyId_Type(Unsigned32):
    """Custom type cadNtpAuthKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_CadNtpAuthKeyId_Type.__name__ = "Unsigned32"
_CadNtpAuthKeyId_Object = MibTableColumn
cadNtpAuthKeyId = _CadNtpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 30, 1, 1),
    _CadNtpAuthKeyId_Type()
)
cadNtpAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadNtpAuthKeyId.setStatus("current")


class _CadNtpAuthKeyType_Type(Integer32):
    """Custom type cadNtpAuthKeyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("md5", 1)
    )


_CadNtpAuthKeyType_Type.__name__ = "Integer32"
_CadNtpAuthKeyType_Object = MibTableColumn
cadNtpAuthKeyType = _CadNtpAuthKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 30, 1, 2),
    _CadNtpAuthKeyType_Type()
)
cadNtpAuthKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpAuthKeyType.setStatus("current")


class _CadNtpAuthKeyValue_Type(DisplayString):
    """Custom type cadNtpAuthKeyValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CadNtpAuthKeyValue_Type.__name__ = "DisplayString"
_CadNtpAuthKeyValue_Object = MibTableColumn
cadNtpAuthKeyValue = _CadNtpAuthKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 30, 1, 3),
    _CadNtpAuthKeyValue_Type()
)
cadNtpAuthKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpAuthKeyValue.setStatus("current")


class _CadNtpAuthKeyRowStatus_Type(RowStatus):
    """Custom type cadNtpAuthKeyRowStatus based on RowStatus"""


_CadNtpAuthKeyRowStatus_Object = MibTableColumn
cadNtpAuthKeyRowStatus = _CadNtpAuthKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 5, 2, 3, 30, 1, 4),
    _CadNtpAuthKeyRowStatus_Type()
)
cadNtpAuthKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadNtpAuthKeyRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-TIME-MIB",
    **{"cadTimeMib": cadTimeMib,
       "cadClock": cadClock,
       "cadTimeZone": cadTimeZone,
       "cadIsDST": cadIsDST,
       "cadTZAbbrev": cadTZAbbrev,
       "cadLocalDateAndTime": cadLocalDateAndTime,
       "cadLocalTime": cadLocalTime,
       "cadUTCtime": cadUTCtime,
       "cadNetTimeSyncProto": cadNetTimeSyncProto,
       "cadTod": cadTod,
       "cadTodServerIpAddress": cadTodServerIpAddress,
       "cadTodServerConnType": cadTodServerConnType,
       "cadNtp": cadNtp,
       "cadNtpVersionDefault": cadNtpVersionDefault,
       "cadNtpAuthenticate": cadNtpAuthenticate,
       "cadNtpClockDrift": cadNtpClockDrift,
       "cadNtpSource": cadNtpSource,
       "cadNtpSourceMinPollDefault": cadNtpSourceMinPollDefault,
       "cadNtpSourceMaxPollDefault": cadNtpSourceMaxPollDefault,
       "cadNtpSourceTable": cadNtpSourceTable,
       "cadNtpSourceEntry": cadNtpSourceEntry,
       "cadNtpSourceIpAddress": cadNtpSourceIpAddress,
       "cadNtpSourceType": cadNtpSourceType,
       "cadNtpSourceBurstEnabled": cadNtpSourceBurstEnabled,
       "cadNtpSourcePreferred": cadNtpSourcePreferred,
       "cadNtpSourceAuthKeyId": cadNtpSourceAuthKeyId,
       "cadNtpSourceMinPoll": cadNtpSourceMinPoll,
       "cadNtpSourceMaxPoll": cadNtpSourceMaxPoll,
       "cadNtpSourceVersion": cadNtpSourceVersion,
       "cadNtpSourceTtl": cadNtpSourceTtl,
       "cadNtpSourceRowStatus": cadNtpSourceRowStatus,
       "cadNtpAuthKeyTable": cadNtpAuthKeyTable,
       "cadNtpAuthKeyEntry": cadNtpAuthKeyEntry,
       "cadNtpAuthKeyId": cadNtpAuthKeyId,
       "cadNtpAuthKeyType": cadNtpAuthKeyType,
       "cadNtpAuthKeyValue": cadNtpAuthKeyValue,
       "cadNtpAuthKeyRowStatus": cadNtpAuthKeyRowStatus}
)
