# SNMP MIB module (DLINK-3100-TIMESYNCHRONIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-TIMESYNCHRONIZATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:26 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlTimeSynchronization = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92)
)
rlTimeSynchronization.setRevisions(
        ("2009-06-18 00:24",
         "2007-09-06 00:24",
         "2003-11-23 00:24")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NTPTimeStamp(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class NTPSignedTimeValue(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d.2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class NTPStratum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class RlTimeSyncMethod(Integer32, TextualConvention):
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
        *(("none", 1),
          ("ntp", 3),
          ("sntp", 2))
    )



class RlDaylightSavingTimeMode(Integer32, TextualConvention):
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
        *(("date", 2),
          ("none", 3),
          ("recurring", 1))
    )



class RlSntpNtpSyncType(Integer32, TextualConvention):
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
        *(("anycast", 3),
          ("broadcast", 4),
          ("none", 1),
          ("unicast", 2))
    )



class RlSntpNtpSyncEntryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primaryPollSrv", 1),
          ("syncSrv", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlTimeSyncMethodMode_ObjectIdentity = ObjectIdentity
rlTimeSyncMethodMode = _RlTimeSyncMethodMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1)
)
_RlTimeSyncMibVersion_Type = Integer32
_RlTimeSyncMibVersion_Object = MibScalar
rlTimeSyncMibVersion = _RlTimeSyncMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 1),
    _RlTimeSyncMibVersion_Type()
)
rlTimeSyncMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTimeSyncMibVersion.setStatus("current")


class _RndTimeSyncManagedTime_Type(DisplayString):
    """Custom type rndTimeSyncManagedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RndTimeSyncManagedTime_Type.__name__ = "DisplayString"
_RndTimeSyncManagedTime_Object = MibScalar
rndTimeSyncManagedTime = _RndTimeSyncManagedTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 2),
    _RndTimeSyncManagedTime_Type()
)
rndTimeSyncManagedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndTimeSyncManagedTime.setStatus("current")


class _RndTimeSyncManagedDate_Type(DisplayString):
    """Custom type rndTimeSyncManagedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RndTimeSyncManagedDate_Type.__name__ = "DisplayString"
_RndTimeSyncManagedDate_Object = MibScalar
rndTimeSyncManagedDate = _RndTimeSyncManagedDate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 3),
    _RndTimeSyncManagedDate_Type()
)
rndTimeSyncManagedDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndTimeSyncManagedDate.setStatus("current")


class _RndTimeSyncManagedDateTime_Type(DisplayString):
    """Custom type rndTimeSyncManagedDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_RndTimeSyncManagedDateTime_Type.__name__ = "DisplayString"
_RndTimeSyncManagedDateTime_Object = MibScalar
rndTimeSyncManagedDateTime = _RndTimeSyncManagedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 4),
    _RndTimeSyncManagedDateTime_Type()
)
rndTimeSyncManagedDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndTimeSyncManagedDateTime.setStatus("current")


class _RlTimeSyncMethod_Type(RlTimeSyncMethod):
    """Custom type rlTimeSyncMethod based on RlTimeSyncMethod"""


_RlTimeSyncMethod_Object = MibScalar
rlTimeSyncMethod = _RlTimeSyncMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 5),
    _RlTimeSyncMethod_Type()
)
rlTimeSyncMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeSyncMethod.setStatus("current")


class _RlTimeZone_Type(DisplayString):
    """Custom type rlTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_RlTimeZone_Type.__name__ = "DisplayString"
_RlTimeZone_Object = MibScalar
rlTimeZone = _RlTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 6),
    _RlTimeZone_Type()
)
rlTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZone.setStatus("current")


class _RlTimeZoneCode_Type(DisplayString):
    """Custom type rlTimeZoneCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RlTimeZoneCode_Type.__name__ = "DisplayString"
_RlTimeZoneCode_Object = MibScalar
rlTimeZoneCode = _RlTimeZoneCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 7),
    _RlTimeZoneCode_Type()
)
rlTimeZoneCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneCode.setStatus("current")


class _RlDaylightSavingTimeMode_Type(RlDaylightSavingTimeMode):
    """Custom type rlDaylightSavingTimeMode based on RlDaylightSavingTimeMode"""


_RlDaylightSavingTimeMode_Object = MibScalar
rlDaylightSavingTimeMode = _RlDaylightSavingTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 8),
    _RlDaylightSavingTimeMode_Type()
)
rlDaylightSavingTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDaylightSavingTimeMode.setStatus("current")


class _RlDaylightSavingTimeStart_Type(OctetString):
    """Custom type rlDaylightSavingTimeStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_RlDaylightSavingTimeStart_Type.__name__ = "OctetString"
_RlDaylightSavingTimeStart_Object = MibScalar
rlDaylightSavingTimeStart = _RlDaylightSavingTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 9),
    _RlDaylightSavingTimeStart_Type()
)
rlDaylightSavingTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDaylightSavingTimeStart.setStatus("current")


class _RlDaylightSavingTimeEnd_Type(OctetString):
    """Custom type rlDaylightSavingTimeEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_RlDaylightSavingTimeEnd_Type.__name__ = "OctetString"
_RlDaylightSavingTimeEnd_Object = MibScalar
rlDaylightSavingTimeEnd = _RlDaylightSavingTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 10),
    _RlDaylightSavingTimeEnd_Type()
)
rlDaylightSavingTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDaylightSavingTimeEnd.setStatus("current")


class _RlDaylightSavingTimeOffset_Type(Integer32):
    """Custom type rlDaylightSavingTimeOffset based on Integer32"""
    defaultValue = 60


_RlDaylightSavingTimeOffset_Object = MibScalar
rlDaylightSavingTimeOffset = _RlDaylightSavingTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 11),
    _RlDaylightSavingTimeOffset_Type()
)
rlDaylightSavingTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDaylightSavingTimeOffset.setStatus("current")


class _RlDaylightSavingTimeCode_Type(DisplayString):
    """Custom type rlDaylightSavingTimeCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RlDaylightSavingTimeCode_Type.__name__ = "DisplayString"
_RlDaylightSavingTimeCode_Object = MibScalar
rlDaylightSavingTimeCode = _RlDaylightSavingTimeCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 12),
    _RlDaylightSavingTimeCode_Type()
)
rlDaylightSavingTimeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDaylightSavingTimeCode.setStatus("current")
_RlTZDSTOffset_Type = Integer32
_RlTZDSTOffset_Object = MibScalar
rlTZDSTOffset = _RlTZDSTOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 13),
    _RlTZDSTOffset_Type()
)
rlTZDSTOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTZDSTOffset.setStatus("current")


class _RlTimeZoneName_Type(DisplayString):
    """Custom type rlTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RlTimeZoneName_Type.__name__ = "DisplayString"
_RlTimeZoneName_Object = MibScalar
rlTimeZoneName = _RlTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 14),
    _RlTimeZoneName_Type()
)
rlTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneName.setStatus("current")
_RlTimeZoneTable_Object = MibTable
rlTimeZoneTable = _RlTimeZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15)
)
if mibBuilder.loadTexts:
    rlTimeZoneTable.setStatus("current")
_RlTimeZoneEntry_Object = MibTableRow
rlTimeZoneEntry = _RlTimeZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1)
)
rlTimeZoneEntry.setIndexNames(
    (0, "DLINK-3100-TIMESYNCHRONIZATION-MIB", "rlTimeZoneIndex"),
)
if mibBuilder.loadTexts:
    rlTimeZoneEntry.setStatus("current")


class _RlTimeZoneIndex_Type(Integer32):
    """Custom type rlTimeZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RlTimeZoneIndex_Type.__name__ = "Integer32"
_RlTimeZoneIndex_Object = MibTableColumn
rlTimeZoneIndex = _RlTimeZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 1),
    _RlTimeZoneIndex_Type()
)
rlTimeZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTimeZoneIndex.setStatus("current")


class _RlTimeZoneTimeSyncMethod_Type(RlTimeSyncMethod):
    """Custom type rlTimeZoneTimeSyncMethod based on RlTimeSyncMethod"""


_RlTimeZoneTimeSyncMethod_Object = MibTableColumn
rlTimeZoneTimeSyncMethod = _RlTimeZoneTimeSyncMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 2),
    _RlTimeZoneTimeSyncMethod_Type()
)
rlTimeZoneTimeSyncMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneTimeSyncMethod.setStatus("current")


class _RlTimeZoneTimeZoneOffset_Type(DisplayString):
    """Custom type rlTimeZoneTimeZoneOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_RlTimeZoneTimeZoneOffset_Type.__name__ = "DisplayString"
_RlTimeZoneTimeZoneOffset_Object = MibTableColumn
rlTimeZoneTimeZoneOffset = _RlTimeZoneTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 3),
    _RlTimeZoneTimeZoneOffset_Type()
)
rlTimeZoneTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneTimeZoneOffset.setStatus("current")


class _RlTimeZoneTimeZoneCode_Type(DisplayString):
    """Custom type rlTimeZoneTimeZoneCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RlTimeZoneTimeZoneCode_Type.__name__ = "DisplayString"
_RlTimeZoneTimeZoneCode_Object = MibTableColumn
rlTimeZoneTimeZoneCode = _RlTimeZoneTimeZoneCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 4),
    _RlTimeZoneTimeZoneCode_Type()
)
rlTimeZoneTimeZoneCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneTimeZoneCode.setStatus("current")


class _RlTimeZoneDaylightSavingTimeMode_Type(RlDaylightSavingTimeMode):
    """Custom type rlTimeZoneDaylightSavingTimeMode based on RlDaylightSavingTimeMode"""


_RlTimeZoneDaylightSavingTimeMode_Object = MibTableColumn
rlTimeZoneDaylightSavingTimeMode = _RlTimeZoneDaylightSavingTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 5),
    _RlTimeZoneDaylightSavingTimeMode_Type()
)
rlTimeZoneDaylightSavingTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneDaylightSavingTimeMode.setStatus("current")


class _RlTimeZoneDaylightSavingTimeStart_Type(OctetString):
    """Custom type rlTimeZoneDaylightSavingTimeStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_RlTimeZoneDaylightSavingTimeStart_Type.__name__ = "OctetString"
_RlTimeZoneDaylightSavingTimeStart_Object = MibTableColumn
rlTimeZoneDaylightSavingTimeStart = _RlTimeZoneDaylightSavingTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 6),
    _RlTimeZoneDaylightSavingTimeStart_Type()
)
rlTimeZoneDaylightSavingTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneDaylightSavingTimeStart.setStatus("current")


class _RlTimeZoneDaylightSavingTimeEnd_Type(OctetString):
    """Custom type rlTimeZoneDaylightSavingTimeEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_RlTimeZoneDaylightSavingTimeEnd_Type.__name__ = "OctetString"
_RlTimeZoneDaylightSavingTimeEnd_Object = MibTableColumn
rlTimeZoneDaylightSavingTimeEnd = _RlTimeZoneDaylightSavingTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 7),
    _RlTimeZoneDaylightSavingTimeEnd_Type()
)
rlTimeZoneDaylightSavingTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneDaylightSavingTimeEnd.setStatus("current")


class _RlTimeZoneDaylightSavingTimeOffset_Type(Integer32):
    """Custom type rlTimeZoneDaylightSavingTimeOffset based on Integer32"""
    defaultValue = 60


_RlTimeZoneDaylightSavingTimeOffset_Object = MibTableColumn
rlTimeZoneDaylightSavingTimeOffset = _RlTimeZoneDaylightSavingTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 8),
    _RlTimeZoneDaylightSavingTimeOffset_Type()
)
rlTimeZoneDaylightSavingTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneDaylightSavingTimeOffset.setStatus("current")


class _RlTimeZoneDaylightSavingTimeCode_Type(DisplayString):
    """Custom type rlTimeZoneDaylightSavingTimeCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RlTimeZoneDaylightSavingTimeCode_Type.__name__ = "DisplayString"
_RlTimeZoneDaylightSavingTimeCode_Object = MibTableColumn
rlTimeZoneDaylightSavingTimeCode = _RlTimeZoneDaylightSavingTimeCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 9),
    _RlTimeZoneDaylightSavingTimeCode_Type()
)
rlTimeZoneDaylightSavingTimeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneDaylightSavingTimeCode.setStatus("current")
_RlTimeZoneTZDSTOffset_Type = Integer32
_RlTimeZoneTZDSTOffset_Object = MibTableColumn
rlTimeZoneTZDSTOffset = _RlTimeZoneTZDSTOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 10),
    _RlTimeZoneTZDSTOffset_Type()
)
rlTimeZoneTZDSTOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTimeZoneTZDSTOffset.setStatus("current")


class _RlTimeZoneTimeZoneName_Type(DisplayString):
    """Custom type rlTimeZoneTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RlTimeZoneTimeZoneName_Type.__name__ = "DisplayString"
_RlTimeZoneTimeZoneName_Object = MibTableColumn
rlTimeZoneTimeZoneName = _RlTimeZoneTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 11),
    _RlTimeZoneTimeZoneName_Type()
)
rlTimeZoneTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneTimeZoneName.setStatus("current")


class _RlTimeZoneDataType_Type(Integer32):
    """Custom type rlTimeZoneDataType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_RlTimeZoneDataType_Type.__name__ = "Integer32"
_RlTimeZoneDataType_Object = MibTableColumn
rlTimeZoneDataType = _RlTimeZoneDataType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 12),
    _RlTimeZoneDataType_Type()
)
rlTimeZoneDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTimeZoneDataType.setStatus("current")


class _RlTimeZoneDataSourceIfIndex_Type(Integer32):
    """Custom type rlTimeZoneDataSourceIfIndex based on Integer32"""
    defaultValue = 0


_RlTimeZoneDataSourceIfIndex_Object = MibTableColumn
rlTimeZoneDataSourceIfIndex = _RlTimeZoneDataSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 15, 1, 13),
    _RlTimeZoneDataSourceIfIndex_Type()
)
rlTimeZoneDataSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeZoneDataSourceIfIndex.setStatus("current")


class _RlClockStatus_Type(Integer32):
    """Custom type rlClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("manuallySet", 2),
          ("synchronizedBySntp", 3))
    )


_RlClockStatus_Type.__name__ = "Integer32"
_RlClockStatus_Object = MibScalar
rlClockStatus = _RlClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 16),
    _RlClockStatus_Type()
)
rlClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlClockStatus.setStatus("current")
_RlDhcpTimezoneOptionEnabled_Type = TruthValue
_RlDhcpTimezoneOptionEnabled_Object = MibScalar
rlDhcpTimezoneOptionEnabled = _RlDhcpTimezoneOptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 1, 17),
    _RlDhcpTimezoneOptionEnabled_Type()
)
rlDhcpTimezoneOptionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpTimezoneOptionEnabled.setStatus("current")
_RlSntpNtpClient_ObjectIdentity = ObjectIdentity
rlSntpNtpClient = _RlSntpNtpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2)
)
_RlSntpNtpConfig_ObjectIdentity = ObjectIdentity
rlSntpNtpConfig = _RlSntpNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1)
)
_RlSntpNtpMibVersion_Type = Integer32
_RlSntpNtpMibVersion_Object = MibScalar
rlSntpNtpMibVersion = _RlSntpNtpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 1),
    _RlSntpNtpMibVersion_Type()
)
rlSntpNtpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpMibVersion.setStatus("current")


class _RlSntpNtpConfigMode_Type(Integer32):
    """Custom type rlSntpNtpConfigMode based on Integer32"""
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
        *(("anycast", 3),
          ("anycastMulticast", 7),
          ("multicast", 4),
          ("none", 1),
          ("unicast", 2),
          ("unicastAnycast", 5),
          ("unicastAnycastMulticast", 8),
          ("unicastMulticast", 6))
    )


_RlSntpNtpConfigMode_Type.__name__ = "Integer32"
_RlSntpNtpConfigMode_Object = MibScalar
rlSntpNtpConfigMode = _RlSntpNtpConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 2),
    _RlSntpNtpConfigMode_Type()
)
rlSntpNtpConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigMode.setStatus("current")
_RlSntpNtpConfigSysStratum_Type = NTPStratum
_RlSntpNtpConfigSysStratum_Object = MibScalar
rlSntpNtpConfigSysStratum = _RlSntpNtpConfigSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 3),
    _RlSntpNtpConfigSysStratum_Type()
)
rlSntpNtpConfigSysStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSysStratum.setStatus("current")


class _RlSntpNtpConfigPollInterval_Type(Integer32):
    """Custom type rlSntpNtpConfigPollInterval based on Integer32"""
    defaultValue = 1024


_RlSntpNtpConfigPollInterval_Object = MibScalar
rlSntpNtpConfigPollInterval = _RlSntpNtpConfigPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 4),
    _RlSntpNtpConfigPollInterval_Type()
)
rlSntpNtpConfigPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpNtpConfigPollInterval.setStatus("current")
_RlSntpNtpConfigPrimaryPollSrvAddr_Type = IpAddress
_RlSntpNtpConfigPrimaryPollSrvAddr_Object = MibScalar
rlSntpNtpConfigPrimaryPollSrvAddr = _RlSntpNtpConfigPrimaryPollSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 5),
    _RlSntpNtpConfigPrimaryPollSrvAddr_Type()
)
rlSntpNtpConfigPrimaryPollSrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigPrimaryPollSrvAddr.setStatus("current")
_RlSntpNtpConfigPrimaryPollSrvMrid_Type = Integer32
_RlSntpNtpConfigPrimaryPollSrvMrid_Object = MibScalar
rlSntpNtpConfigPrimaryPollSrvMrid = _RlSntpNtpConfigPrimaryPollSrvMrid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 6),
    _RlSntpNtpConfigPrimaryPollSrvMrid_Type()
)
rlSntpNtpConfigPrimaryPollSrvMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigPrimaryPollSrvMrid.setStatus("current")
_RlSntpNtpConfigPrimaryPollSrvIfIndex_Type = Integer32
_RlSntpNtpConfigPrimaryPollSrvIfIndex_Object = MibScalar
rlSntpNtpConfigPrimaryPollSrvIfIndex = _RlSntpNtpConfigPrimaryPollSrvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 7),
    _RlSntpNtpConfigPrimaryPollSrvIfIndex_Type()
)
rlSntpNtpConfigPrimaryPollSrvIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigPrimaryPollSrvIfIndex.setStatus("current")
_RlSntpNtpConfigPrimaryPollSrvStratum_Type = NTPStratum
_RlSntpNtpConfigPrimaryPollSrvStratum_Object = MibScalar
rlSntpNtpConfigPrimaryPollSrvStratum = _RlSntpNtpConfigPrimaryPollSrvStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 8),
    _RlSntpNtpConfigPrimaryPollSrvStratum_Type()
)
rlSntpNtpConfigPrimaryPollSrvStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigPrimaryPollSrvStratum.setStatus("current")
_RlSntpNtpConfigSyncSrvAddr_Type = IpAddress
_RlSntpNtpConfigSyncSrvAddr_Object = MibScalar
rlSntpNtpConfigSyncSrvAddr = _RlSntpNtpConfigSyncSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 9),
    _RlSntpNtpConfigSyncSrvAddr_Type()
)
rlSntpNtpConfigSyncSrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSyncSrvAddr.setStatus("current")
_RlSntpNtpConfigSyncSrvMrid_Type = Integer32
_RlSntpNtpConfigSyncSrvMrid_Object = MibScalar
rlSntpNtpConfigSyncSrvMrid = _RlSntpNtpConfigSyncSrvMrid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 10),
    _RlSntpNtpConfigSyncSrvMrid_Type()
)
rlSntpNtpConfigSyncSrvMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSyncSrvMrid.setStatus("current")
_RlSntpNtpConfigSyncSrvIfIndex_Type = Integer32
_RlSntpNtpConfigSyncSrvIfIndex_Object = MibScalar
rlSntpNtpConfigSyncSrvIfIndex = _RlSntpNtpConfigSyncSrvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 11),
    _RlSntpNtpConfigSyncSrvIfIndex_Type()
)
rlSntpNtpConfigSyncSrvIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSyncSrvIfIndex.setStatus("current")


class _RlSntpNtpConfigSyncSrvType_Type(RlSntpNtpSyncType):
    """Custom type rlSntpNtpConfigSyncSrvType based on RlSntpNtpSyncType"""


_RlSntpNtpConfigSyncSrvType_Object = MibScalar
rlSntpNtpConfigSyncSrvType = _RlSntpNtpConfigSyncSrvType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 12),
    _RlSntpNtpConfigSyncSrvType_Type()
)
rlSntpNtpConfigSyncSrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSyncSrvType.setStatus("current")
_RlSntpNtpConfigSyncSrvStratum_Type = NTPStratum
_RlSntpNtpConfigSyncSrvStratum_Object = MibScalar
rlSntpNtpConfigSyncSrvStratum = _RlSntpNtpConfigSyncSrvStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 13),
    _RlSntpNtpConfigSyncSrvStratum_Type()
)
rlSntpNtpConfigSyncSrvStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSyncSrvStratum.setStatus("current")
_RlSntpNtpConfigRetryTimeout_Type = Integer32
_RlSntpNtpConfigRetryTimeout_Object = MibScalar
rlSntpNtpConfigRetryTimeout = _RlSntpNtpConfigRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 14),
    _RlSntpNtpConfigRetryTimeout_Type()
)
rlSntpNtpConfigRetryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigRetryTimeout.setStatus("current")
_RlSntpNtpConfigRetryCnt_Type = Integer32
_RlSntpNtpConfigRetryCnt_Object = MibScalar
rlSntpNtpConfigRetryCnt = _RlSntpNtpConfigRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 15),
    _RlSntpNtpConfigRetryCnt_Type()
)
rlSntpNtpConfigRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigRetryCnt.setStatus("current")
_RlSntpNtpConfigSrvTable_Object = MibTable
rlSntpNtpConfigSrvTable = _RlSntpNtpConfigSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 16)
)
if mibBuilder.loadTexts:
    rlSntpNtpConfigSrvTable.setStatus("current")
_RlSntpNtpConfigSrvEntry_Object = MibTableRow
rlSntpNtpConfigSrvEntry = _RlSntpNtpConfigSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 16, 1)
)
rlSntpNtpConfigSrvEntry.setIndexNames(
    (0, "DLINK-3100-TIMESYNCHRONIZATION-MIB", "rlSntpNtpConfigSrvEntryType"),
)
if mibBuilder.loadTexts:
    rlSntpNtpConfigSrvEntry.setStatus("current")
_RlSntpNtpConfigSrvEntryType_Type = RlSntpNtpSyncEntryType
_RlSntpNtpConfigSrvEntryType_Object = MibTableColumn
rlSntpNtpConfigSrvEntryType = _RlSntpNtpConfigSrvEntryType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 16, 1, 1),
    _RlSntpNtpConfigSrvEntryType_Type()
)
rlSntpNtpConfigSrvEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSrvEntryType.setStatus("current")
_RlSntpNtpConfigSrvInetAddressType_Type = InetAddressType
_RlSntpNtpConfigSrvInetAddressType_Object = MibTableColumn
rlSntpNtpConfigSrvInetAddressType = _RlSntpNtpConfigSrvInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 16, 1, 2),
    _RlSntpNtpConfigSrvInetAddressType_Type()
)
rlSntpNtpConfigSrvInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSrvInetAddressType.setStatus("current")
_RlSntpNtpConfigSrvInetAddress_Type = InetAddress
_RlSntpNtpConfigSrvInetAddress_Object = MibTableColumn
rlSntpNtpConfigSrvInetAddress = _RlSntpNtpConfigSrvInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 16, 1, 3),
    _RlSntpNtpConfigSrvInetAddress_Type()
)
rlSntpNtpConfigSrvInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSrvInetAddress.setStatus("current")
_RlSntpNtpConfigSrvMrid_Type = Integer32
_RlSntpNtpConfigSrvMrid_Object = MibTableColumn
rlSntpNtpConfigSrvMrid = _RlSntpNtpConfigSrvMrid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 16, 1, 4),
    _RlSntpNtpConfigSrvMrid_Type()
)
rlSntpNtpConfigSrvMrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSrvMrid.setStatus("current")
_RlSntpNtpConfigSrvIfIndex_Type = Integer32
_RlSntpNtpConfigSrvIfIndex_Object = MibTableColumn
rlSntpNtpConfigSrvIfIndex = _RlSntpNtpConfigSrvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 16, 1, 5),
    _RlSntpNtpConfigSrvIfIndex_Type()
)
rlSntpNtpConfigSrvIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSrvIfIndex.setStatus("current")
_RlSntpNtpConfigSrvSyncType_Type = RlSntpNtpSyncType
_RlSntpNtpConfigSrvSyncType_Object = MibTableColumn
rlSntpNtpConfigSrvSyncType = _RlSntpNtpConfigSrvSyncType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 16, 1, 6),
    _RlSntpNtpConfigSrvSyncType_Type()
)
rlSntpNtpConfigSrvSyncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSrvSyncType.setStatus("current")
_RlSntpNtpConfigSrvStratum_Type = NTPStratum
_RlSntpNtpConfigSrvStratum_Object = MibTableColumn
rlSntpNtpConfigSrvStratum = _RlSntpNtpConfigSrvStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 1, 16, 1, 7),
    _RlSntpNtpConfigSrvStratum_Type()
)
rlSntpNtpConfigSrvStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpNtpConfigSrvStratum.setStatus("current")
_RlSntpConfig_ObjectIdentity = ObjectIdentity
rlSntpConfig = _RlSntpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2)
)


class _RlSntpClientMode_Type(Integer32):
    """Custom type rlSntpClientMode based on Integer32"""
    defaultValue = 1

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
          ("none", 1),
          ("passive", 3))
    )


_RlSntpClientMode_Type.__name__ = "Integer32"
_RlSntpClientMode_Object = MibScalar
rlSntpClientMode = _RlSntpClientMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 1),
    _RlSntpClientMode_Type()
)
rlSntpClientMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpClientMode.setStatus("current")


class _RlSntpUnicastAdminState_Type(Integer32):
    """Custom type rlSntpUnicastAdminState based on Integer32"""
    defaultValue = 2

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


_RlSntpUnicastAdminState_Type.__name__ = "Integer32"
_RlSntpUnicastAdminState_Object = MibScalar
rlSntpUnicastAdminState = _RlSntpUnicastAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 2),
    _RlSntpUnicastAdminState_Type()
)
rlSntpUnicastAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpUnicastAdminState.setStatus("current")


class _RlSntpBroadcastAdminState_Type(Integer32):
    """Custom type rlSntpBroadcastAdminState based on Integer32"""
    defaultValue = 2

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


_RlSntpBroadcastAdminState_Type.__name__ = "Integer32"
_RlSntpBroadcastAdminState_Object = MibScalar
rlSntpBroadcastAdminState = _RlSntpBroadcastAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 3),
    _RlSntpBroadcastAdminState_Type()
)
rlSntpBroadcastAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastAdminState.setStatus("current")


class _RlSntpAnycastAdminState_Type(Integer32):
    """Custom type rlSntpAnycastAdminState based on Integer32"""
    defaultValue = 2

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


_RlSntpAnycastAdminState_Type.__name__ = "Integer32"
_RlSntpAnycastAdminState_Object = MibScalar
rlSntpAnycastAdminState = _RlSntpAnycastAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 4),
    _RlSntpAnycastAdminState_Type()
)
rlSntpAnycastAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAnycastAdminState.setStatus("current")


class _RlSntpUnicastPollState_Type(TruthValue):
    """Custom type rlSntpUnicastPollState based on TruthValue"""


_RlSntpUnicastPollState_Object = MibScalar
rlSntpUnicastPollState = _RlSntpUnicastPollState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 5),
    _RlSntpUnicastPollState_Type()
)
rlSntpUnicastPollState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpUnicastPollState.setStatus("current")


class _RlSntpBroadcastPollState_Type(TruthValue):
    """Custom type rlSntpBroadcastPollState based on TruthValue"""


_RlSntpBroadcastPollState_Object = MibScalar
rlSntpBroadcastPollState = _RlSntpBroadcastPollState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 6),
    _RlSntpBroadcastPollState_Type()
)
rlSntpBroadcastPollState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastPollState.setStatus("current")


class _RlSntpAnycastPollState_Type(TruthValue):
    """Custom type rlSntpAnycastPollState based on TruthValue"""


_RlSntpAnycastPollState_Object = MibScalar
rlSntpAnycastPollState = _RlSntpAnycastPollState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 7),
    _RlSntpAnycastPollState_Type()
)
rlSntpAnycastPollState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAnycastPollState.setStatus("current")


class _RlSntpAuthenticationState_Type(Integer32):
    """Custom type rlSntpAuthenticationState based on Integer32"""
    defaultValue = 2

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


_RlSntpAuthenticationState_Type.__name__ = "Integer32"
_RlSntpAuthenticationState_Object = MibScalar
rlSntpAuthenticationState = _RlSntpAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 8),
    _RlSntpAuthenticationState_Type()
)
rlSntpAuthenticationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAuthenticationState.setStatus("current")


class _RlTimeValidFlag_Type(TruthValue):
    """Custom type rlTimeValidFlag based on TruthValue"""


_RlTimeValidFlag_Object = MibScalar
rlTimeValidFlag = _RlTimeValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 9),
    _RlTimeValidFlag_Type()
)
rlTimeValidFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTimeValidFlag.setStatus("current")
_RlSntpConfigBroadcastTable_Object = MibTable
rlSntpConfigBroadcastTable = _RlSntpConfigBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10)
)
if mibBuilder.loadTexts:
    rlSntpConfigBroadcastTable.setStatus("current")
_RlSntpBroadcastEntry_Object = MibTableRow
rlSntpBroadcastEntry = _RlSntpBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1)
)
rlSntpBroadcastEntry.setIndexNames(
    (0, "DLINK-3100-TIMESYNCHRONIZATION-MIB", "rlSntpBroadcastIfIndex"),
)
if mibBuilder.loadTexts:
    rlSntpBroadcastEntry.setStatus("current")
_RlSntpBroadcastIfIndex_Type = Integer32
_RlSntpBroadcastIfIndex_Object = MibTableColumn
rlSntpBroadcastIfIndex = _RlSntpBroadcastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 1),
    _RlSntpBroadcastIfIndex_Type()
)
rlSntpBroadcastIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpBroadcastIfIndex.setStatus("current")


class _RlSntpBroadcastIfAdminState_Type(Integer32):
    """Custom type rlSntpBroadcastIfAdminState based on Integer32"""
    defaultValue = 2

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


_RlSntpBroadcastIfAdminState_Type.__name__ = "Integer32"
_RlSntpBroadcastIfAdminState_Object = MibTableColumn
rlSntpBroadcastIfAdminState = _RlSntpBroadcastIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 2),
    _RlSntpBroadcastIfAdminState_Type()
)
rlSntpBroadcastIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastIfAdminState.setStatus("current")


class _RlSntpBroadcastMode_Type(Integer32):
    """Custom type rlSntpBroadcastMode based on Integer32"""
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
        *(("none", 1),
          ("receive", 2),
          ("receiveSend", 4),
          ("send", 3))
    )


_RlSntpBroadcastMode_Type.__name__ = "Integer32"
_RlSntpBroadcastMode_Object = MibTableColumn
rlSntpBroadcastMode = _RlSntpBroadcastMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 3),
    _RlSntpBroadcastMode_Type()
)
rlSntpBroadcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastMode.setStatus("current")


class _RlSntpBroadcastPolled_Type(TruthValue):
    """Custom type rlSntpBroadcastPolled based on TruthValue"""


_RlSntpBroadcastPolled_Object = MibTableColumn
rlSntpBroadcastPolled = _RlSntpBroadcastPolled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 4),
    _RlSntpBroadcastPolled_Type()
)
rlSntpBroadcastPolled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastPolled.setStatus("current")
_RlSntpBroadcastAddress_Type = IpAddress
_RlSntpBroadcastAddress_Object = MibTableColumn
rlSntpBroadcastAddress = _RlSntpBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 5),
    _RlSntpBroadcastAddress_Type()
)
rlSntpBroadcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastAddress.setStatus("current")
_RlSntpBroadcastStratum_Type = NTPStratum
_RlSntpBroadcastStratum_Object = MibTableColumn
rlSntpBroadcastStratum = _RlSntpBroadcastStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 6),
    _RlSntpBroadcastStratum_Type()
)
rlSntpBroadcastStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastStratum.setStatus("current")
_RlSntpBroadcastLastResp_Type = NTPTimeStamp
_RlSntpBroadcastLastResp_Object = MibTableColumn
rlSntpBroadcastLastResp = _RlSntpBroadcastLastResp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 7),
    _RlSntpBroadcastLastResp_Type()
)
rlSntpBroadcastLastResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastLastResp.setStatus("current")


class _RlSntpBroadcastStatus_Type(Integer32):
    """Custom type rlSntpBroadcastStatus based on Integer32"""
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
        *(("down", 4),
          ("inProcess", 2),
          ("unknown", 1),
          ("up", 3))
    )


_RlSntpBroadcastStatus_Type.__name__ = "Integer32"
_RlSntpBroadcastStatus_Object = MibTableColumn
rlSntpBroadcastStatus = _RlSntpBroadcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 8),
    _RlSntpBroadcastStatus_Type()
)
rlSntpBroadcastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastStatus.setStatus("current")
_RlSntpBroadcastOffset_Type = NTPTimeStamp
_RlSntpBroadcastOffset_Object = MibTableColumn
rlSntpBroadcastOffset = _RlSntpBroadcastOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 9),
    _RlSntpBroadcastOffset_Type()
)
rlSntpBroadcastOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastOffset.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpBroadcastOffset.setUnits("seconds")
_RlSntpBroadcastDelay_Type = NTPSignedTimeValue
_RlSntpBroadcastDelay_Object = MibTableColumn
rlSntpBroadcastDelay = _RlSntpBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 10),
    _RlSntpBroadcastDelay_Type()
)
rlSntpBroadcastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpBroadcastDelay.setUnits("seconds")
_RlSntpBroadcastRowStatus_Type = RowStatus
_RlSntpBroadcastRowStatus_Object = MibTableColumn
rlSntpBroadcastRowStatus = _RlSntpBroadcastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 10, 1, 11),
    _RlSntpBroadcastRowStatus_Type()
)
rlSntpBroadcastRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastRowStatus.setStatus("current")
_RlSntpConfigAnycastTable_Object = MibTable
rlSntpConfigAnycastTable = _RlSntpConfigAnycastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 11)
)
if mibBuilder.loadTexts:
    rlSntpConfigAnycastTable.setStatus("current")
_RlSntpAnycastEntry_Object = MibTableRow
rlSntpAnycastEntry = _RlSntpAnycastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 11, 1)
)
rlSntpAnycastEntry.setIndexNames(
    (0, "DLINK-3100-TIMESYNCHRONIZATION-MIB", "rlSntpAnycastIfIndex"),
)
if mibBuilder.loadTexts:
    rlSntpAnycastEntry.setStatus("current")
_RlSntpAnycastIfIndex_Type = Integer32
_RlSntpAnycastIfIndex_Object = MibTableColumn
rlSntpAnycastIfIndex = _RlSntpAnycastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 11, 1, 1),
    _RlSntpAnycastIfIndex_Type()
)
rlSntpAnycastIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpAnycastIfIndex.setStatus("current")
_RlSntpAnycastAddress_Type = IpAddress
_RlSntpAnycastAddress_Object = MibTableColumn
rlSntpAnycastAddress = _RlSntpAnycastAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 11, 1, 2),
    _RlSntpAnycastAddress_Type()
)
rlSntpAnycastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastAddress.setStatus("current")
_RlSntpAnycastStratum_Type = NTPStratum
_RlSntpAnycastStratum_Object = MibTableColumn
rlSntpAnycastStratum = _RlSntpAnycastStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 11, 1, 3),
    _RlSntpAnycastStratum_Type()
)
rlSntpAnycastStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastStratum.setStatus("current")
_RlSntpAnycastLastResp_Type = NTPTimeStamp
_RlSntpAnycastLastResp_Object = MibTableColumn
rlSntpAnycastLastResp = _RlSntpAnycastLastResp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 11, 1, 4),
    _RlSntpAnycastLastResp_Type()
)
rlSntpAnycastLastResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastLastResp.setStatus("current")


class _RlSntpAnycastStatus_Type(Integer32):
    """Custom type rlSntpAnycastStatus based on Integer32"""
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
        *(("down", 4),
          ("inProcess", 2),
          ("unknown", 1),
          ("up", 3))
    )


_RlSntpAnycastStatus_Type.__name__ = "Integer32"
_RlSntpAnycastStatus_Object = MibTableColumn
rlSntpAnycastStatus = _RlSntpAnycastStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 11, 1, 5),
    _RlSntpAnycastStatus_Type()
)
rlSntpAnycastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastStatus.setStatus("current")
_RlSntpAnycastOffset_Type = NTPTimeStamp
_RlSntpAnycastOffset_Object = MibTableColumn
rlSntpAnycastOffset = _RlSntpAnycastOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 11, 1, 6),
    _RlSntpAnycastOffset_Type()
)
rlSntpAnycastOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastOffset.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpAnycastOffset.setUnits("seconds")
_RlSntpAnycastDelay_Type = NTPSignedTimeValue
_RlSntpAnycastDelay_Object = MibTableColumn
rlSntpAnycastDelay = _RlSntpAnycastDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 11, 1, 7),
    _RlSntpAnycastDelay_Type()
)
rlSntpAnycastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpAnycastDelay.setUnits("seconds")
_RlSntpAnycastRowStatus_Type = RowStatus
_RlSntpAnycastRowStatus_Object = MibTableColumn
rlSntpAnycastRowStatus = _RlSntpAnycastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 11, 1, 8),
    _RlSntpAnycastRowStatus_Type()
)
rlSntpAnycastRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAnycastRowStatus.setStatus("current")
_RlSntpConfigServerTable_Object = MibTable
rlSntpConfigServerTable = _RlSntpConfigServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12)
)
if mibBuilder.loadTexts:
    rlSntpConfigServerTable.setStatus("current")
_RlSntpServerEntry_Object = MibTableRow
rlSntpServerEntry = _RlSntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12, 1)
)
rlSntpServerEntry.setIndexNames(
    (0, "DLINK-3100-TIMESYNCHRONIZATION-MIB", "rlSntpServerAddress"),
)
if mibBuilder.loadTexts:
    rlSntpServerEntry.setStatus("current")
_RlSntpServerAddress_Type = IpAddress
_RlSntpServerAddress_Object = MibTableColumn
rlSntpServerAddress = _RlSntpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12, 1, 1),
    _RlSntpServerAddress_Type()
)
rlSntpServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpServerAddress.setStatus("current")


class _RlSntpServerPolled_Type(TruthValue):
    """Custom type rlSntpServerPolled based on TruthValue"""


_RlSntpServerPolled_Object = MibTableColumn
rlSntpServerPolled = _RlSntpServerPolled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12, 1, 2),
    _RlSntpServerPolled_Type()
)
rlSntpServerPolled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpServerPolled.setStatus("current")
_RlSntpServerStratum_Type = NTPStratum
_RlSntpServerStratum_Object = MibTableColumn
rlSntpServerStratum = _RlSntpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12, 1, 3),
    _RlSntpServerStratum_Type()
)
rlSntpServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerStratum.setStatus("current")
_RlSntpServerLastResp_Type = NTPTimeStamp
_RlSntpServerLastResp_Object = MibTableColumn
rlSntpServerLastResp = _RlSntpServerLastResp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12, 1, 4),
    _RlSntpServerLastResp_Type()
)
rlSntpServerLastResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerLastResp.setStatus("current")


class _RlSntpServerStatus_Type(Integer32):
    """Custom type rlSntpServerStatus based on Integer32"""
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
        *(("down", 4),
          ("inProcess", 2),
          ("unknown", 1),
          ("up", 3))
    )


_RlSntpServerStatus_Type.__name__ = "Integer32"
_RlSntpServerStatus_Object = MibTableColumn
rlSntpServerStatus = _RlSntpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12, 1, 5),
    _RlSntpServerStatus_Type()
)
rlSntpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerStatus.setStatus("current")
_RlSntpServersOffset_Type = NTPTimeStamp
_RlSntpServersOffset_Object = MibTableColumn
rlSntpServersOffset = _RlSntpServersOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12, 1, 6),
    _RlSntpServersOffset_Type()
)
rlSntpServersOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServersOffset.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpServersOffset.setUnits("seconds")
_RlSntpServersDelay_Type = NTPSignedTimeValue
_RlSntpServersDelay_Object = MibTableColumn
rlSntpServersDelay = _RlSntpServersDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12, 1, 7),
    _RlSntpServersDelay_Type()
)
rlSntpServersDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServersDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpServersDelay.setUnits("seconds")
_RlSntpServersKeyIdentifier_Type = Unsigned32
_RlSntpServersKeyIdentifier_Object = MibTableColumn
rlSntpServersKeyIdentifier = _RlSntpServersKeyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12, 1, 8),
    _RlSntpServersKeyIdentifier_Type()
)
rlSntpServersKeyIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpServersKeyIdentifier.setStatus("current")
_RlSntpServerRowStatus_Type = RowStatus
_RlSntpServerRowStatus_Object = MibTableColumn
rlSntpServerRowStatus = _RlSntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 12, 1, 9),
    _RlSntpServerRowStatus_Type()
)
rlSntpServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpServerRowStatus.setStatus("current")
_RlSntpConfigAuthenticationTable_Object = MibTable
rlSntpConfigAuthenticationTable = _RlSntpConfigAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 13)
)
if mibBuilder.loadTexts:
    rlSntpConfigAuthenticationTable.setStatus("current")
_RlSntpAuthenticationEntry_Object = MibTableRow
rlSntpAuthenticationEntry = _RlSntpAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 13, 1)
)
rlSntpAuthenticationEntry.setIndexNames(
    (0, "DLINK-3100-TIMESYNCHRONIZATION-MIB", "rlSntpAuthenticationKeyID"),
)
if mibBuilder.loadTexts:
    rlSntpAuthenticationEntry.setStatus("current")


class _RlSntpAuthenticationKeyID_Type(Unsigned32):
    """Custom type rlSntpAuthenticationKeyID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlSntpAuthenticationKeyID_Type.__name__ = "Unsigned32"
_RlSntpAuthenticationKeyID_Object = MibTableColumn
rlSntpAuthenticationKeyID = _RlSntpAuthenticationKeyID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 13, 1, 1),
    _RlSntpAuthenticationKeyID_Type()
)
rlSntpAuthenticationKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAuthenticationKeyID.setStatus("current")


class _RlSntpAuthenticationKeyValue_Type(DisplayString):
    """Custom type rlSntpAuthenticationKeyValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_RlSntpAuthenticationKeyValue_Type.__name__ = "DisplayString"
_RlSntpAuthenticationKeyValue_Object = MibTableColumn
rlSntpAuthenticationKeyValue = _RlSntpAuthenticationKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 13, 1, 2),
    _RlSntpAuthenticationKeyValue_Type()
)
rlSntpAuthenticationKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAuthenticationKeyValue.setStatus("current")


class _RlSntpAuthenticationKeyState_Type(Integer32):
    """Custom type rlSntpAuthenticationKeyState based on Integer32"""
    defaultValue = 2

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


_RlSntpAuthenticationKeyState_Type.__name__ = "Integer32"
_RlSntpAuthenticationKeyState_Object = MibTableColumn
rlSntpAuthenticationKeyState = _RlSntpAuthenticationKeyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 13, 1, 3),
    _RlSntpAuthenticationKeyState_Type()
)
rlSntpAuthenticationKeyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAuthenticationKeyState.setStatus("current")
_RlSntpAuthenticationRowStatus_Type = RowStatus
_RlSntpAuthenticationRowStatus_Object = MibTableColumn
rlSntpAuthenticationRowStatus = _RlSntpAuthenticationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 13, 1, 4),
    _RlSntpAuthenticationRowStatus_Type()
)
rlSntpAuthenticationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAuthenticationRowStatus.setStatus("current")


class _RlSntpPort_Type(Integer32):
    """Custom type rlSntpPort based on Integer32"""
    defaultValue = 123

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlSntpPort_Type.__name__ = "Integer32"
_RlSntpPort_Object = MibScalar
rlSntpPort = _RlSntpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 14),
    _RlSntpPort_Type()
)
rlSntpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpPort.setStatus("current")
_RlSntpConfigBroadcastInetTable_Object = MibTable
rlSntpConfigBroadcastInetTable = _RlSntpConfigBroadcastInetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15)
)
if mibBuilder.loadTexts:
    rlSntpConfigBroadcastInetTable.setStatus("current")
_RlSntpBroadcastInetEntry_Object = MibTableRow
rlSntpBroadcastInetEntry = _RlSntpBroadcastInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1)
)
rlSntpBroadcastInetEntry.setIndexNames(
    (0, "DLINK-3100-TIMESYNCHRONIZATION-MIB", "rlSntpBroadcastInetIfIndex"),
)
if mibBuilder.loadTexts:
    rlSntpBroadcastInetEntry.setStatus("current")
_RlSntpBroadcastInetIfIndex_Type = Integer32
_RlSntpBroadcastInetIfIndex_Object = MibTableColumn
rlSntpBroadcastInetIfIndex = _RlSntpBroadcastInetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 1),
    _RlSntpBroadcastInetIfIndex_Type()
)
rlSntpBroadcastInetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetIfIndex.setStatus("current")


class _RlSntpBroadcastInetIfAdminState_Type(Integer32):
    """Custom type rlSntpBroadcastInetIfAdminState based on Integer32"""
    defaultValue = 2

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


_RlSntpBroadcastInetIfAdminState_Type.__name__ = "Integer32"
_RlSntpBroadcastInetIfAdminState_Object = MibTableColumn
rlSntpBroadcastInetIfAdminState = _RlSntpBroadcastInetIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 2),
    _RlSntpBroadcastInetIfAdminState_Type()
)
rlSntpBroadcastInetIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetIfAdminState.setStatus("current")


class _RlSntpBroadcastInetMode_Type(Integer32):
    """Custom type rlSntpBroadcastInetMode based on Integer32"""
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
        *(("none", 1),
          ("receive", 2),
          ("receiveSend", 4),
          ("send", 3))
    )


_RlSntpBroadcastInetMode_Type.__name__ = "Integer32"
_RlSntpBroadcastInetMode_Object = MibTableColumn
rlSntpBroadcastInetMode = _RlSntpBroadcastInetMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 3),
    _RlSntpBroadcastInetMode_Type()
)
rlSntpBroadcastInetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetMode.setStatus("current")


class _RlSntpBroadcastInetPolled_Type(TruthValue):
    """Custom type rlSntpBroadcastInetPolled based on TruthValue"""


_RlSntpBroadcastInetPolled_Object = MibTableColumn
rlSntpBroadcastInetPolled = _RlSntpBroadcastInetPolled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 4),
    _RlSntpBroadcastInetPolled_Type()
)
rlSntpBroadcastInetPolled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetPolled.setStatus("current")
_RlSntpBroadcastInetAddressType_Type = InetAddressType
_RlSntpBroadcastInetAddressType_Object = MibTableColumn
rlSntpBroadcastInetAddressType = _RlSntpBroadcastInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 5),
    _RlSntpBroadcastInetAddressType_Type()
)
rlSntpBroadcastInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetAddressType.setStatus("current")
_RlSntpBroadcastInetAddress_Type = InetAddress
_RlSntpBroadcastInetAddress_Object = MibTableColumn
rlSntpBroadcastInetAddress = _RlSntpBroadcastInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 6),
    _RlSntpBroadcastInetAddress_Type()
)
rlSntpBroadcastInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetAddress.setStatus("current")
_RlSntpBroadcastInetStratum_Type = NTPStratum
_RlSntpBroadcastInetStratum_Object = MibTableColumn
rlSntpBroadcastInetStratum = _RlSntpBroadcastInetStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 7),
    _RlSntpBroadcastInetStratum_Type()
)
rlSntpBroadcastInetStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetStratum.setStatus("current")
_RlSntpBroadcastInetLastResp_Type = NTPTimeStamp
_RlSntpBroadcastInetLastResp_Object = MibTableColumn
rlSntpBroadcastInetLastResp = _RlSntpBroadcastInetLastResp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 8),
    _RlSntpBroadcastInetLastResp_Type()
)
rlSntpBroadcastInetLastResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetLastResp.setStatus("current")


class _RlSntpBroadcastInetStatus_Type(Integer32):
    """Custom type rlSntpBroadcastInetStatus based on Integer32"""
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
        *(("down", 4),
          ("inProcess", 2),
          ("unknown", 1),
          ("up", 3))
    )


_RlSntpBroadcastInetStatus_Type.__name__ = "Integer32"
_RlSntpBroadcastInetStatus_Object = MibTableColumn
rlSntpBroadcastInetStatus = _RlSntpBroadcastInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 9),
    _RlSntpBroadcastInetStatus_Type()
)
rlSntpBroadcastInetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetStatus.setStatus("current")
_RlSntpBroadcastInetOffset_Type = NTPTimeStamp
_RlSntpBroadcastInetOffset_Object = MibTableColumn
rlSntpBroadcastInetOffset = _RlSntpBroadcastInetOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 10),
    _RlSntpBroadcastInetOffset_Type()
)
rlSntpBroadcastInetOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetOffset.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetOffset.setUnits("seconds")
_RlSntpBroadcastInetDelay_Type = NTPSignedTimeValue
_RlSntpBroadcastInetDelay_Object = MibTableColumn
rlSntpBroadcastInetDelay = _RlSntpBroadcastInetDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 11),
    _RlSntpBroadcastInetDelay_Type()
)
rlSntpBroadcastInetDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetDelay.setUnits("seconds")
_RlSntpBroadcastInetRowStatus_Type = RowStatus
_RlSntpBroadcastInetRowStatus_Object = MibTableColumn
rlSntpBroadcastInetRowStatus = _RlSntpBroadcastInetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 15, 1, 12),
    _RlSntpBroadcastInetRowStatus_Type()
)
rlSntpBroadcastInetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpBroadcastInetRowStatus.setStatus("current")
_RlSntpConfigAnycastInetTable_Object = MibTable
rlSntpConfigAnycastInetTable = _RlSntpConfigAnycastInetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16)
)
if mibBuilder.loadTexts:
    rlSntpConfigAnycastInetTable.setStatus("current")
_RlSntpAnycastInetEntry_Object = MibTableRow
rlSntpAnycastInetEntry = _RlSntpAnycastInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16, 1)
)
rlSntpAnycastInetEntry.setIndexNames(
    (0, "DLINK-3100-TIMESYNCHRONIZATION-MIB", "rlSntpAnycastInetIfIndex"),
)
if mibBuilder.loadTexts:
    rlSntpAnycastInetEntry.setStatus("current")
_RlSntpAnycastInetIfIndex_Type = Integer32
_RlSntpAnycastInetIfIndex_Object = MibTableColumn
rlSntpAnycastInetIfIndex = _RlSntpAnycastInetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16, 1, 1),
    _RlSntpAnycastInetIfIndex_Type()
)
rlSntpAnycastInetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpAnycastInetIfIndex.setStatus("current")
_RlSntpAnycastInetAddressType_Type = InetAddressType
_RlSntpAnycastInetAddressType_Object = MibTableColumn
rlSntpAnycastInetAddressType = _RlSntpAnycastInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16, 1, 2),
    _RlSntpAnycastInetAddressType_Type()
)
rlSntpAnycastInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastInetAddressType.setStatus("current")
_RlSntpAnycastInetAddress_Type = InetAddress
_RlSntpAnycastInetAddress_Object = MibTableColumn
rlSntpAnycastInetAddress = _RlSntpAnycastInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16, 1, 3),
    _RlSntpAnycastInetAddress_Type()
)
rlSntpAnycastInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastInetAddress.setStatus("current")
_RlSntpAnycastInetStratum_Type = NTPStratum
_RlSntpAnycastInetStratum_Object = MibTableColumn
rlSntpAnycastInetStratum = _RlSntpAnycastInetStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16, 1, 4),
    _RlSntpAnycastInetStratum_Type()
)
rlSntpAnycastInetStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastInetStratum.setStatus("current")
_RlSntpAnycastInetLastResp_Type = NTPTimeStamp
_RlSntpAnycastInetLastResp_Object = MibTableColumn
rlSntpAnycastInetLastResp = _RlSntpAnycastInetLastResp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16, 1, 5),
    _RlSntpAnycastInetLastResp_Type()
)
rlSntpAnycastInetLastResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastInetLastResp.setStatus("current")


class _RlSntpAnycastInetStatus_Type(Integer32):
    """Custom type rlSntpAnycastInetStatus based on Integer32"""
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
        *(("down", 4),
          ("inProcess", 2),
          ("unknown", 1),
          ("up", 3))
    )


_RlSntpAnycastInetStatus_Type.__name__ = "Integer32"
_RlSntpAnycastInetStatus_Object = MibTableColumn
rlSntpAnycastInetStatus = _RlSntpAnycastInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16, 1, 6),
    _RlSntpAnycastInetStatus_Type()
)
rlSntpAnycastInetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastInetStatus.setStatus("current")
_RlSntpAnycastInetOffset_Type = NTPTimeStamp
_RlSntpAnycastInetOffset_Object = MibTableColumn
rlSntpAnycastInetOffset = _RlSntpAnycastInetOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16, 1, 7),
    _RlSntpAnycastInetOffset_Type()
)
rlSntpAnycastInetOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastInetOffset.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpAnycastInetOffset.setUnits("seconds")
_RlSntpAnycastInetDelay_Type = NTPSignedTimeValue
_RlSntpAnycastInetDelay_Object = MibTableColumn
rlSntpAnycastInetDelay = _RlSntpAnycastInetDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16, 1, 8),
    _RlSntpAnycastInetDelay_Type()
)
rlSntpAnycastInetDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpAnycastInetDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpAnycastInetDelay.setUnits("seconds")
_RlSntpAnycastInetRowStatus_Type = RowStatus
_RlSntpAnycastInetRowStatus_Object = MibTableColumn
rlSntpAnycastInetRowStatus = _RlSntpAnycastInetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 16, 1, 9),
    _RlSntpAnycastInetRowStatus_Type()
)
rlSntpAnycastInetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpAnycastInetRowStatus.setStatus("current")
_RlSntpConfigServerInetTable_Object = MibTable
rlSntpConfigServerInetTable = _RlSntpConfigServerInetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17)
)
if mibBuilder.loadTexts:
    rlSntpConfigServerInetTable.setStatus("current")
_RlSntpServerInetEntry_Object = MibTableRow
rlSntpServerInetEntry = _RlSntpServerInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1)
)
rlSntpServerInetEntry.setIndexNames(
    (0, "DLINK-3100-TIMESYNCHRONIZATION-MIB", "rlSntpServerInetAddressType"),
    (0, "DLINK-3100-TIMESYNCHRONIZATION-MIB", "rlSntpServerInetAddress"),
)
if mibBuilder.loadTexts:
    rlSntpServerInetEntry.setStatus("current")
_RlSntpServerInetAddressType_Type = InetAddressType
_RlSntpServerInetAddressType_Object = MibTableColumn
rlSntpServerInetAddressType = _RlSntpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1, 1),
    _RlSntpServerInetAddressType_Type()
)
rlSntpServerInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpServerInetAddressType.setStatus("current")
_RlSntpServerInetAddress_Type = InetAddress
_RlSntpServerInetAddress_Object = MibTableColumn
rlSntpServerInetAddress = _RlSntpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1, 2),
    _RlSntpServerInetAddress_Type()
)
rlSntpServerInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSntpServerInetAddress.setStatus("current")


class _RlSntpServerInetPolled_Type(TruthValue):
    """Custom type rlSntpServerInetPolled based on TruthValue"""


_RlSntpServerInetPolled_Object = MibTableColumn
rlSntpServerInetPolled = _RlSntpServerInetPolled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1, 3),
    _RlSntpServerInetPolled_Type()
)
rlSntpServerInetPolled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpServerInetPolled.setStatus("current")
_RlSntpServerInetStratum_Type = NTPStratum
_RlSntpServerInetStratum_Object = MibTableColumn
rlSntpServerInetStratum = _RlSntpServerInetStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1, 4),
    _RlSntpServerInetStratum_Type()
)
rlSntpServerInetStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerInetStratum.setStatus("current")
_RlSntpServerInetLastResp_Type = NTPTimeStamp
_RlSntpServerInetLastResp_Object = MibTableColumn
rlSntpServerInetLastResp = _RlSntpServerInetLastResp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1, 5),
    _RlSntpServerInetLastResp_Type()
)
rlSntpServerInetLastResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerInetLastResp.setStatus("current")


class _RlSntpServerInetStatus_Type(Integer32):
    """Custom type rlSntpServerInetStatus based on Integer32"""
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
        *(("down", 4),
          ("inProcess", 2),
          ("unknown", 1),
          ("up", 3))
    )


_RlSntpServerInetStatus_Type.__name__ = "Integer32"
_RlSntpServerInetStatus_Object = MibTableColumn
rlSntpServerInetStatus = _RlSntpServerInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1, 6),
    _RlSntpServerInetStatus_Type()
)
rlSntpServerInetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerInetStatus.setStatus("current")
_RlSntpServerInetOffset_Type = NTPTimeStamp
_RlSntpServerInetOffset_Object = MibTableColumn
rlSntpServerInetOffset = _RlSntpServerInetOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1, 7),
    _RlSntpServerInetOffset_Type()
)
rlSntpServerInetOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerInetOffset.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpServerInetOffset.setUnits("seconds")
_RlSntpServerInetDelay_Type = NTPSignedTimeValue
_RlSntpServerInetDelay_Object = MibTableColumn
rlSntpServerInetDelay = _RlSntpServerInetDelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1, 8),
    _RlSntpServerInetDelay_Type()
)
rlSntpServerInetDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSntpServerInetDelay.setStatus("current")
if mibBuilder.loadTexts:
    rlSntpServerInetDelay.setUnits("seconds")
_RlSntpServerInetKeyIdentifier_Type = Unsigned32
_RlSntpServerInetKeyIdentifier_Object = MibTableColumn
rlSntpServerInetKeyIdentifier = _RlSntpServerInetKeyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1, 9),
    _RlSntpServerInetKeyIdentifier_Type()
)
rlSntpServerInetKeyIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpServerInetKeyIdentifier.setStatus("current")
_RlSntpServerInetRowStatus_Type = RowStatus
_RlSntpServerInetRowStatus_Object = MibTableColumn
rlSntpServerInetRowStatus = _RlSntpServerInetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 2, 17, 1, 10),
    _RlSntpServerInetRowStatus_Type()
)
rlSntpServerInetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSntpServerInetRowStatus.setStatus("current")
_RlNtpConfig_ObjectIdentity = ObjectIdentity
rlNtpConfig = _RlNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 92, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-TIMESYNCHRONIZATION-MIB",
    **{"NTPTimeStamp": NTPTimeStamp,
       "NTPSignedTimeValue": NTPSignedTimeValue,
       "NTPStratum": NTPStratum,
       "RlTimeSyncMethod": RlTimeSyncMethod,
       "RlDaylightSavingTimeMode": RlDaylightSavingTimeMode,
       "RlSntpNtpSyncType": RlSntpNtpSyncType,
       "RlSntpNtpSyncEntryType": RlSntpNtpSyncEntryType,
       "rlTimeSynchronization": rlTimeSynchronization,
       "rlTimeSyncMethodMode": rlTimeSyncMethodMode,
       "rlTimeSyncMibVersion": rlTimeSyncMibVersion,
       "rndTimeSyncManagedTime": rndTimeSyncManagedTime,
       "rndTimeSyncManagedDate": rndTimeSyncManagedDate,
       "rndTimeSyncManagedDateTime": rndTimeSyncManagedDateTime,
       "rlTimeSyncMethod": rlTimeSyncMethod,
       "rlTimeZone": rlTimeZone,
       "rlTimeZoneCode": rlTimeZoneCode,
       "rlDaylightSavingTimeMode": rlDaylightSavingTimeMode,
       "rlDaylightSavingTimeStart": rlDaylightSavingTimeStart,
       "rlDaylightSavingTimeEnd": rlDaylightSavingTimeEnd,
       "rlDaylightSavingTimeOffset": rlDaylightSavingTimeOffset,
       "rlDaylightSavingTimeCode": rlDaylightSavingTimeCode,
       "rlTZDSTOffset": rlTZDSTOffset,
       "rlTimeZoneName": rlTimeZoneName,
       "rlTimeZoneTable": rlTimeZoneTable,
       "rlTimeZoneEntry": rlTimeZoneEntry,
       "rlTimeZoneIndex": rlTimeZoneIndex,
       "rlTimeZoneTimeSyncMethod": rlTimeZoneTimeSyncMethod,
       "rlTimeZoneTimeZoneOffset": rlTimeZoneTimeZoneOffset,
       "rlTimeZoneTimeZoneCode": rlTimeZoneTimeZoneCode,
       "rlTimeZoneDaylightSavingTimeMode": rlTimeZoneDaylightSavingTimeMode,
       "rlTimeZoneDaylightSavingTimeStart": rlTimeZoneDaylightSavingTimeStart,
       "rlTimeZoneDaylightSavingTimeEnd": rlTimeZoneDaylightSavingTimeEnd,
       "rlTimeZoneDaylightSavingTimeOffset": rlTimeZoneDaylightSavingTimeOffset,
       "rlTimeZoneDaylightSavingTimeCode": rlTimeZoneDaylightSavingTimeCode,
       "rlTimeZoneTZDSTOffset": rlTimeZoneTZDSTOffset,
       "rlTimeZoneTimeZoneName": rlTimeZoneTimeZoneName,
       "rlTimeZoneDataType": rlTimeZoneDataType,
       "rlTimeZoneDataSourceIfIndex": rlTimeZoneDataSourceIfIndex,
       "rlClockStatus": rlClockStatus,
       "rlDhcpTimezoneOptionEnabled": rlDhcpTimezoneOptionEnabled,
       "rlSntpNtpClient": rlSntpNtpClient,
       "rlSntpNtpConfig": rlSntpNtpConfig,
       "rlSntpNtpMibVersion": rlSntpNtpMibVersion,
       "rlSntpNtpConfigMode": rlSntpNtpConfigMode,
       "rlSntpNtpConfigSysStratum": rlSntpNtpConfigSysStratum,
       "rlSntpNtpConfigPollInterval": rlSntpNtpConfigPollInterval,
       "rlSntpNtpConfigPrimaryPollSrvAddr": rlSntpNtpConfigPrimaryPollSrvAddr,
       "rlSntpNtpConfigPrimaryPollSrvMrid": rlSntpNtpConfigPrimaryPollSrvMrid,
       "rlSntpNtpConfigPrimaryPollSrvIfIndex": rlSntpNtpConfigPrimaryPollSrvIfIndex,
       "rlSntpNtpConfigPrimaryPollSrvStratum": rlSntpNtpConfigPrimaryPollSrvStratum,
       "rlSntpNtpConfigSyncSrvAddr": rlSntpNtpConfigSyncSrvAddr,
       "rlSntpNtpConfigSyncSrvMrid": rlSntpNtpConfigSyncSrvMrid,
       "rlSntpNtpConfigSyncSrvIfIndex": rlSntpNtpConfigSyncSrvIfIndex,
       "rlSntpNtpConfigSyncSrvType": rlSntpNtpConfigSyncSrvType,
       "rlSntpNtpConfigSyncSrvStratum": rlSntpNtpConfigSyncSrvStratum,
       "rlSntpNtpConfigRetryTimeout": rlSntpNtpConfigRetryTimeout,
       "rlSntpNtpConfigRetryCnt": rlSntpNtpConfigRetryCnt,
       "rlSntpNtpConfigSrvTable": rlSntpNtpConfigSrvTable,
       "rlSntpNtpConfigSrvEntry": rlSntpNtpConfigSrvEntry,
       "rlSntpNtpConfigSrvEntryType": rlSntpNtpConfigSrvEntryType,
       "rlSntpNtpConfigSrvInetAddressType": rlSntpNtpConfigSrvInetAddressType,
       "rlSntpNtpConfigSrvInetAddress": rlSntpNtpConfigSrvInetAddress,
       "rlSntpNtpConfigSrvMrid": rlSntpNtpConfigSrvMrid,
       "rlSntpNtpConfigSrvIfIndex": rlSntpNtpConfigSrvIfIndex,
       "rlSntpNtpConfigSrvSyncType": rlSntpNtpConfigSrvSyncType,
       "rlSntpNtpConfigSrvStratum": rlSntpNtpConfigSrvStratum,
       "rlSntpConfig": rlSntpConfig,
       "rlSntpClientMode": rlSntpClientMode,
       "rlSntpUnicastAdminState": rlSntpUnicastAdminState,
       "rlSntpBroadcastAdminState": rlSntpBroadcastAdminState,
       "rlSntpAnycastAdminState": rlSntpAnycastAdminState,
       "rlSntpUnicastPollState": rlSntpUnicastPollState,
       "rlSntpBroadcastPollState": rlSntpBroadcastPollState,
       "rlSntpAnycastPollState": rlSntpAnycastPollState,
       "rlSntpAuthenticationState": rlSntpAuthenticationState,
       "rlTimeValidFlag": rlTimeValidFlag,
       "rlSntpConfigBroadcastTable": rlSntpConfigBroadcastTable,
       "rlSntpBroadcastEntry": rlSntpBroadcastEntry,
       "rlSntpBroadcastIfIndex": rlSntpBroadcastIfIndex,
       "rlSntpBroadcastIfAdminState": rlSntpBroadcastIfAdminState,
       "rlSntpBroadcastMode": rlSntpBroadcastMode,
       "rlSntpBroadcastPolled": rlSntpBroadcastPolled,
       "rlSntpBroadcastAddress": rlSntpBroadcastAddress,
       "rlSntpBroadcastStratum": rlSntpBroadcastStratum,
       "rlSntpBroadcastLastResp": rlSntpBroadcastLastResp,
       "rlSntpBroadcastStatus": rlSntpBroadcastStatus,
       "rlSntpBroadcastOffset": rlSntpBroadcastOffset,
       "rlSntpBroadcastDelay": rlSntpBroadcastDelay,
       "rlSntpBroadcastRowStatus": rlSntpBroadcastRowStatus,
       "rlSntpConfigAnycastTable": rlSntpConfigAnycastTable,
       "rlSntpAnycastEntry": rlSntpAnycastEntry,
       "rlSntpAnycastIfIndex": rlSntpAnycastIfIndex,
       "rlSntpAnycastAddress": rlSntpAnycastAddress,
       "rlSntpAnycastStratum": rlSntpAnycastStratum,
       "rlSntpAnycastLastResp": rlSntpAnycastLastResp,
       "rlSntpAnycastStatus": rlSntpAnycastStatus,
       "rlSntpAnycastOffset": rlSntpAnycastOffset,
       "rlSntpAnycastDelay": rlSntpAnycastDelay,
       "rlSntpAnycastRowStatus": rlSntpAnycastRowStatus,
       "rlSntpConfigServerTable": rlSntpConfigServerTable,
       "rlSntpServerEntry": rlSntpServerEntry,
       "rlSntpServerAddress": rlSntpServerAddress,
       "rlSntpServerPolled": rlSntpServerPolled,
       "rlSntpServerStratum": rlSntpServerStratum,
       "rlSntpServerLastResp": rlSntpServerLastResp,
       "rlSntpServerStatus": rlSntpServerStatus,
       "rlSntpServersOffset": rlSntpServersOffset,
       "rlSntpServersDelay": rlSntpServersDelay,
       "rlSntpServersKeyIdentifier": rlSntpServersKeyIdentifier,
       "rlSntpServerRowStatus": rlSntpServerRowStatus,
       "rlSntpConfigAuthenticationTable": rlSntpConfigAuthenticationTable,
       "rlSntpAuthenticationEntry": rlSntpAuthenticationEntry,
       "rlSntpAuthenticationKeyID": rlSntpAuthenticationKeyID,
       "rlSntpAuthenticationKeyValue": rlSntpAuthenticationKeyValue,
       "rlSntpAuthenticationKeyState": rlSntpAuthenticationKeyState,
       "rlSntpAuthenticationRowStatus": rlSntpAuthenticationRowStatus,
       "rlSntpPort": rlSntpPort,
       "rlSntpConfigBroadcastInetTable": rlSntpConfigBroadcastInetTable,
       "rlSntpBroadcastInetEntry": rlSntpBroadcastInetEntry,
       "rlSntpBroadcastInetIfIndex": rlSntpBroadcastInetIfIndex,
       "rlSntpBroadcastInetIfAdminState": rlSntpBroadcastInetIfAdminState,
       "rlSntpBroadcastInetMode": rlSntpBroadcastInetMode,
       "rlSntpBroadcastInetPolled": rlSntpBroadcastInetPolled,
       "rlSntpBroadcastInetAddressType": rlSntpBroadcastInetAddressType,
       "rlSntpBroadcastInetAddress": rlSntpBroadcastInetAddress,
       "rlSntpBroadcastInetStratum": rlSntpBroadcastInetStratum,
       "rlSntpBroadcastInetLastResp": rlSntpBroadcastInetLastResp,
       "rlSntpBroadcastInetStatus": rlSntpBroadcastInetStatus,
       "rlSntpBroadcastInetOffset": rlSntpBroadcastInetOffset,
       "rlSntpBroadcastInetDelay": rlSntpBroadcastInetDelay,
       "rlSntpBroadcastInetRowStatus": rlSntpBroadcastInetRowStatus,
       "rlSntpConfigAnycastInetTable": rlSntpConfigAnycastInetTable,
       "rlSntpAnycastInetEntry": rlSntpAnycastInetEntry,
       "rlSntpAnycastInetIfIndex": rlSntpAnycastInetIfIndex,
       "rlSntpAnycastInetAddressType": rlSntpAnycastInetAddressType,
       "rlSntpAnycastInetAddress": rlSntpAnycastInetAddress,
       "rlSntpAnycastInetStratum": rlSntpAnycastInetStratum,
       "rlSntpAnycastInetLastResp": rlSntpAnycastInetLastResp,
       "rlSntpAnycastInetStatus": rlSntpAnycastInetStatus,
       "rlSntpAnycastInetOffset": rlSntpAnycastInetOffset,
       "rlSntpAnycastInetDelay": rlSntpAnycastInetDelay,
       "rlSntpAnycastInetRowStatus": rlSntpAnycastInetRowStatus,
       "rlSntpConfigServerInetTable": rlSntpConfigServerInetTable,
       "rlSntpServerInetEntry": rlSntpServerInetEntry,
       "rlSntpServerInetAddressType": rlSntpServerInetAddressType,
       "rlSntpServerInetAddress": rlSntpServerInetAddress,
       "rlSntpServerInetPolled": rlSntpServerInetPolled,
       "rlSntpServerInetStratum": rlSntpServerInetStratum,
       "rlSntpServerInetLastResp": rlSntpServerInetLastResp,
       "rlSntpServerInetStatus": rlSntpServerInetStatus,
       "rlSntpServerInetOffset": rlSntpServerInetOffset,
       "rlSntpServerInetDelay": rlSntpServerInetDelay,
       "rlSntpServerInetKeyIdentifier": rlSntpServerInetKeyIdentifier,
       "rlSntpServerInetRowStatus": rlSntpServerInetRowStatus,
       "rlNtpConfig": rlNtpConfig}
)
