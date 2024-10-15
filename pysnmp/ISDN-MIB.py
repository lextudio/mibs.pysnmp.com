# SNMP MIB module (ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:09 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

isdnMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IsdnSignalingProtocol(Integer32, TextualConvention):
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("cornet", 20),
          ("dass2", 4),
          ("dms100", 7),
          ("dms250", 8),
          ("dss1", 2),
          ("ess4", 5),
          ("ess5", 6),
          ("etsi", 3),
          ("ins1500", 18),
          ("ins64", 17),
          ("itr6", 19),
          ("kdd", 16),
          ("ni1", 9),
          ("ni2", 10),
          ("ni3", 11),
          ("other", 1),
          ("qsig", 23),
          ("swissnet2", 24),
          ("swissnet3", 25),
          ("ts013", 21),
          ("ts014", 22),
          ("vn2", 12),
          ("vn3", 13),
          ("vn4", 14),
          ("vn6", 15))
    )



# MIB Managed Objects in the order of their OIDs

_IsdnMibObjects_ObjectIdentity = ObjectIdentity
isdnMibObjects = _IsdnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 1)
)
_IsdnBasicRateGroup_ObjectIdentity = ObjectIdentity
isdnBasicRateGroup = _IsdnBasicRateGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 1)
)
_IsdnBasicRateTable_Object = MibTable
isdnBasicRateTable = _IsdnBasicRateTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    isdnBasicRateTable.setStatus("current")
_IsdnBasicRateEntry_Object = MibTableRow
isdnBasicRateEntry = _IsdnBasicRateEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1)
)
isdnBasicRateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    isdnBasicRateEntry.setStatus("current")


class _IsdnBasicRateIfType_Type(Integer32):
    """Custom type isdnBasicRateIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              76)
        )
    )
    namedValues = NamedValues(
        *(("isdns", 75),
          ("isdnu", 76))
    )


_IsdnBasicRateIfType_Type.__name__ = "Integer32"
_IsdnBasicRateIfType_Object = MibTableColumn
isdnBasicRateIfType = _IsdnBasicRateIfType_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 1),
    _IsdnBasicRateIfType_Type()
)
isdnBasicRateIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnBasicRateIfType.setStatus("current")


class _IsdnBasicRateLineTopology_Type(Integer32):
    """Custom type isdnBasicRateLineTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pointToMultipoint", 2),
          ("pointToPoint", 1))
    )


_IsdnBasicRateLineTopology_Type.__name__ = "Integer32"
_IsdnBasicRateLineTopology_Object = MibTableColumn
isdnBasicRateLineTopology = _IsdnBasicRateLineTopology_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 2),
    _IsdnBasicRateLineTopology_Type()
)
isdnBasicRateLineTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnBasicRateLineTopology.setStatus("current")


class _IsdnBasicRateIfMode_Type(Integer32):
    """Custom type isdnBasicRateIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nt", 2),
          ("te", 1))
    )


_IsdnBasicRateIfMode_Type.__name__ = "Integer32"
_IsdnBasicRateIfMode_Object = MibTableColumn
isdnBasicRateIfMode = _IsdnBasicRateIfMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 3),
    _IsdnBasicRateIfMode_Type()
)
isdnBasicRateIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnBasicRateIfMode.setStatus("current")


class _IsdnBasicRateSignalMode_Type(Integer32):
    """Custom type isdnBasicRateSignalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IsdnBasicRateSignalMode_Type.__name__ = "Integer32"
_IsdnBasicRateSignalMode_Object = MibTableColumn
isdnBasicRateSignalMode = _IsdnBasicRateSignalMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 4),
    _IsdnBasicRateSignalMode_Type()
)
isdnBasicRateSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnBasicRateSignalMode.setStatus("current")
_IsdnBearerGroup_ObjectIdentity = ObjectIdentity
isdnBearerGroup = _IsdnBearerGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2)
)
_IsdnBearerTable_Object = MibTable
isdnBearerTable = _IsdnBearerTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    isdnBearerTable.setStatus("current")
_IsdnBearerEntry_Object = MibTableRow
isdnBearerEntry = _IsdnBearerEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1)
)
isdnBearerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    isdnBearerEntry.setStatus("current")


class _IsdnBearerChannelType_Type(Integer32):
    """Custom type isdnBearerChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialup", 1),
          ("leased", 2))
    )


_IsdnBearerChannelType_Type.__name__ = "Integer32"
_IsdnBearerChannelType_Object = MibTableColumn
isdnBearerChannelType = _IsdnBearerChannelType_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 1),
    _IsdnBearerChannelType_Type()
)
isdnBearerChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnBearerChannelType.setStatus("current")


class _IsdnBearerOperStatus_Type(Integer32):
    """Custom type isdnBearerOperStatus based on Integer32"""
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
        *(("active", 4),
          ("connected", 3),
          ("connecting", 2),
          ("idle", 1))
    )


_IsdnBearerOperStatus_Type.__name__ = "Integer32"
_IsdnBearerOperStatus_Object = MibTableColumn
isdnBearerOperStatus = _IsdnBearerOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 2),
    _IsdnBearerOperStatus_Type()
)
isdnBearerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnBearerOperStatus.setStatus("current")


class _IsdnBearerChannelNumber_Type(Integer32):
    """Custom type isdnBearerChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IsdnBearerChannelNumber_Type.__name__ = "Integer32"
_IsdnBearerChannelNumber_Object = MibTableColumn
isdnBearerChannelNumber = _IsdnBearerChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 3),
    _IsdnBearerChannelNumber_Type()
)
isdnBearerChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnBearerChannelNumber.setStatus("current")
_IsdnBearerPeerAddress_Type = DisplayString
_IsdnBearerPeerAddress_Object = MibTableColumn
isdnBearerPeerAddress = _IsdnBearerPeerAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 4),
    _IsdnBearerPeerAddress_Type()
)
isdnBearerPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnBearerPeerAddress.setStatus("current")
_IsdnBearerPeerSubAddress_Type = DisplayString
_IsdnBearerPeerSubAddress_Object = MibTableColumn
isdnBearerPeerSubAddress = _IsdnBearerPeerSubAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 5),
    _IsdnBearerPeerSubAddress_Type()
)
isdnBearerPeerSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnBearerPeerSubAddress.setStatus("current")


class _IsdnBearerCallOrigin_Type(Integer32):
    """Custom type isdnBearerCallOrigin based on Integer32"""
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
        *(("answer", 3),
          ("callback", 4),
          ("originate", 2),
          ("unknown", 1))
    )


_IsdnBearerCallOrigin_Type.__name__ = "Integer32"
_IsdnBearerCallOrigin_Object = MibTableColumn
isdnBearerCallOrigin = _IsdnBearerCallOrigin_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 6),
    _IsdnBearerCallOrigin_Type()
)
isdnBearerCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnBearerCallOrigin.setStatus("current")


class _IsdnBearerInfoType_Type(Integer32):
    """Custom type isdnBearerInfoType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("audio31", 6),
          ("audio7", 7),
          ("packetSwitched", 9),
          ("restrictedDigital", 5),
          ("speech", 2),
          ("unknown", 1),
          ("unrestrictedDigital", 3),
          ("unrestrictedDigital56", 4),
          ("video", 8))
    )


_IsdnBearerInfoType_Type.__name__ = "Integer32"
_IsdnBearerInfoType_Object = MibTableColumn
isdnBearerInfoType = _IsdnBearerInfoType_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 7),
    _IsdnBearerInfoType_Type()
)
isdnBearerInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnBearerInfoType.setStatus("current")
_IsdnBearerMultirate_Type = TruthValue
_IsdnBearerMultirate_Object = MibTableColumn
isdnBearerMultirate = _IsdnBearerMultirate_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 8),
    _IsdnBearerMultirate_Type()
)
isdnBearerMultirate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnBearerMultirate.setStatus("current")
_IsdnBearerCallSetupTime_Type = TimeStamp
_IsdnBearerCallSetupTime_Object = MibTableColumn
isdnBearerCallSetupTime = _IsdnBearerCallSetupTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 9),
    _IsdnBearerCallSetupTime_Type()
)
isdnBearerCallSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnBearerCallSetupTime.setStatus("current")
_IsdnBearerCallConnectTime_Type = TimeStamp
_IsdnBearerCallConnectTime_Object = MibTableColumn
isdnBearerCallConnectTime = _IsdnBearerCallConnectTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 10),
    _IsdnBearerCallConnectTime_Type()
)
isdnBearerCallConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnBearerCallConnectTime.setStatus("current")
_IsdnBearerChargedUnits_Type = Gauge32
_IsdnBearerChargedUnits_Object = MibTableColumn
isdnBearerChargedUnits = _IsdnBearerChargedUnits_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 11),
    _IsdnBearerChargedUnits_Type()
)
isdnBearerChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnBearerChargedUnits.setStatus("current")
_IsdnSignalingGroup_ObjectIdentity = ObjectIdentity
isdnSignalingGroup = _IsdnSignalingGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3)
)
_IsdnSignalingGetIndex_Type = TestAndIncr
_IsdnSignalingGetIndex_Object = MibScalar
isdnSignalingGetIndex = _IsdnSignalingGetIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 1),
    _IsdnSignalingGetIndex_Type()
)
isdnSignalingGetIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnSignalingGetIndex.setStatus("current")
_IsdnSignalingTable_Object = MibTable
isdnSignalingTable = _IsdnSignalingTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2)
)
if mibBuilder.loadTexts:
    isdnSignalingTable.setStatus("current")
_IsdnSignalingEntry_Object = MibTableRow
isdnSignalingEntry = _IsdnSignalingEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1)
)
isdnSignalingEntry.setIndexNames(
    (0, "ISDN-MIB", "isdnSignalingIndex"),
)
if mibBuilder.loadTexts:
    isdnSignalingEntry.setStatus("current")


class _IsdnSignalingIndex_Type(Integer32):
    """Custom type isdnSignalingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsdnSignalingIndex_Type.__name__ = "Integer32"
_IsdnSignalingIndex_Object = MibTableColumn
isdnSignalingIndex = _IsdnSignalingIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 1),
    _IsdnSignalingIndex_Type()
)
isdnSignalingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnSignalingIndex.setStatus("current")
_IsdnSignalingIfIndex_Type = InterfaceIndex
_IsdnSignalingIfIndex_Object = MibTableColumn
isdnSignalingIfIndex = _IsdnSignalingIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 2),
    _IsdnSignalingIfIndex_Type()
)
isdnSignalingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSignalingIfIndex.setStatus("current")
_IsdnSignalingProtocol_Type = IsdnSignalingProtocol
_IsdnSignalingProtocol_Object = MibTableColumn
isdnSignalingProtocol = _IsdnSignalingProtocol_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 3),
    _IsdnSignalingProtocol_Type()
)
isdnSignalingProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnSignalingProtocol.setStatus("current")
_IsdnSignalingCallingAddress_Type = DisplayString
_IsdnSignalingCallingAddress_Object = MibTableColumn
isdnSignalingCallingAddress = _IsdnSignalingCallingAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 4),
    _IsdnSignalingCallingAddress_Type()
)
isdnSignalingCallingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnSignalingCallingAddress.setStatus("current")
_IsdnSignalingSubAddress_Type = DisplayString
_IsdnSignalingSubAddress_Object = MibTableColumn
isdnSignalingSubAddress = _IsdnSignalingSubAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 5),
    _IsdnSignalingSubAddress_Type()
)
isdnSignalingSubAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnSignalingSubAddress.setStatus("current")


class _IsdnSignalingBchannelCount_Type(Integer32):
    """Custom type isdnSignalingBchannelCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnSignalingBchannelCount_Type.__name__ = "Integer32"
_IsdnSignalingBchannelCount_Object = MibTableColumn
isdnSignalingBchannelCount = _IsdnSignalingBchannelCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 6),
    _IsdnSignalingBchannelCount_Type()
)
isdnSignalingBchannelCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnSignalingBchannelCount.setStatus("current")


class _IsdnSignalingInfoTrapEnable_Type(Integer32):
    """Custom type isdnSignalingInfoTrapEnable based on Integer32"""
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


_IsdnSignalingInfoTrapEnable_Type.__name__ = "Integer32"
_IsdnSignalingInfoTrapEnable_Object = MibTableColumn
isdnSignalingInfoTrapEnable = _IsdnSignalingInfoTrapEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 7),
    _IsdnSignalingInfoTrapEnable_Type()
)
isdnSignalingInfoTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnSignalingInfoTrapEnable.setStatus("current")
_IsdnSignalingStatus_Type = RowStatus
_IsdnSignalingStatus_Object = MibTableColumn
isdnSignalingStatus = _IsdnSignalingStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 8),
    _IsdnSignalingStatus_Type()
)
isdnSignalingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnSignalingStatus.setStatus("current")
_IsdnSignalingStatsTable_Object = MibTable
isdnSignalingStatsTable = _IsdnSignalingStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3)
)
if mibBuilder.loadTexts:
    isdnSignalingStatsTable.setStatus("current")
_IsdnSignalingStatsEntry_Object = MibTableRow
isdnSignalingStatsEntry = _IsdnSignalingStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    isdnSignalingStatsEntry.setStatus("current")
_IsdnSigStatsInCalls_Type = Counter32
_IsdnSigStatsInCalls_Object = MibTableColumn
isdnSigStatsInCalls = _IsdnSigStatsInCalls_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 1),
    _IsdnSigStatsInCalls_Type()
)
isdnSigStatsInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigStatsInCalls.setStatus("current")
_IsdnSigStatsInConnected_Type = Counter32
_IsdnSigStatsInConnected_Object = MibTableColumn
isdnSigStatsInConnected = _IsdnSigStatsInConnected_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 2),
    _IsdnSigStatsInConnected_Type()
)
isdnSigStatsInConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigStatsInConnected.setStatus("current")
_IsdnSigStatsOutCalls_Type = Counter32
_IsdnSigStatsOutCalls_Object = MibTableColumn
isdnSigStatsOutCalls = _IsdnSigStatsOutCalls_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 3),
    _IsdnSigStatsOutCalls_Type()
)
isdnSigStatsOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigStatsOutCalls.setStatus("current")
_IsdnSigStatsOutConnected_Type = Counter32
_IsdnSigStatsOutConnected_Object = MibTableColumn
isdnSigStatsOutConnected = _IsdnSigStatsOutConnected_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 4),
    _IsdnSigStatsOutConnected_Type()
)
isdnSigStatsOutConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigStatsOutConnected.setStatus("current")
_IsdnSigStatsChargedUnits_Type = Counter32
_IsdnSigStatsChargedUnits_Object = MibTableColumn
isdnSigStatsChargedUnits = _IsdnSigStatsChargedUnits_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 5),
    _IsdnSigStatsChargedUnits_Type()
)
isdnSigStatsChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigStatsChargedUnits.setStatus("current")
_IsdnLapdTable_Object = MibTable
isdnLapdTable = _IsdnLapdTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4)
)
if mibBuilder.loadTexts:
    isdnLapdTable.setStatus("current")
_IsdnLapdEntry_Object = MibTableRow
isdnLapdEntry = _IsdnLapdEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1)
)
isdnLapdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    isdnLapdEntry.setStatus("current")
_IsdnLapdPrimaryChannel_Type = TruthValue
_IsdnLapdPrimaryChannel_Object = MibTableColumn
isdnLapdPrimaryChannel = _IsdnLapdPrimaryChannel_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 1),
    _IsdnLapdPrimaryChannel_Type()
)
isdnLapdPrimaryChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnLapdPrimaryChannel.setStatus("current")


class _IsdnLapdOperStatus_Type(Integer32):
    """Custom type isdnLapdOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("l1Active", 2),
          ("l2Active", 3))
    )


_IsdnLapdOperStatus_Type.__name__ = "Integer32"
_IsdnLapdOperStatus_Object = MibTableColumn
isdnLapdOperStatus = _IsdnLapdOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 2),
    _IsdnLapdOperStatus_Type()
)
isdnLapdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLapdOperStatus.setStatus("current")
_IsdnLapdPeerSabme_Type = Counter32
_IsdnLapdPeerSabme_Object = MibTableColumn
isdnLapdPeerSabme = _IsdnLapdPeerSabme_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 3),
    _IsdnLapdPeerSabme_Type()
)
isdnLapdPeerSabme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLapdPeerSabme.setStatus("current")
_IsdnLapdRecvdFrmr_Type = Counter32
_IsdnLapdRecvdFrmr_Object = MibTableColumn
isdnLapdRecvdFrmr = _IsdnLapdRecvdFrmr_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 4),
    _IsdnLapdRecvdFrmr_Type()
)
isdnLapdRecvdFrmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnLapdRecvdFrmr.setStatus("current")
_IsdnEndpointGroup_ObjectIdentity = ObjectIdentity
isdnEndpointGroup = _IsdnEndpointGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4)
)
_IsdnEndpointGetIndex_Type = TestAndIncr
_IsdnEndpointGetIndex_Object = MibScalar
isdnEndpointGetIndex = _IsdnEndpointGetIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 1),
    _IsdnEndpointGetIndex_Type()
)
isdnEndpointGetIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnEndpointGetIndex.setStatus("current")
_IsdnEndpointTable_Object = MibTable
isdnEndpointTable = _IsdnEndpointTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2)
)
if mibBuilder.loadTexts:
    isdnEndpointTable.setStatus("current")
_IsdnEndpointEntry_Object = MibTableRow
isdnEndpointEntry = _IsdnEndpointEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1)
)
isdnEndpointEntry.setIndexNames(
    (0, "ISDN-MIB", "isdnEndpointIndex"),
)
if mibBuilder.loadTexts:
    isdnEndpointEntry.setStatus("current")


class _IsdnEndpointIndex_Type(Integer32):
    """Custom type isdnEndpointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsdnEndpointIndex_Type.__name__ = "Integer32"
_IsdnEndpointIndex_Object = MibTableColumn
isdnEndpointIndex = _IsdnEndpointIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 1),
    _IsdnEndpointIndex_Type()
)
isdnEndpointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnEndpointIndex.setStatus("current")
_IsdnEndpointIfIndex_Type = InterfaceIndex
_IsdnEndpointIfIndex_Object = MibTableColumn
isdnEndpointIfIndex = _IsdnEndpointIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 2),
    _IsdnEndpointIfIndex_Type()
)
isdnEndpointIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnEndpointIfIndex.setStatus("current")
_IsdnEndpointIfType_Type = IANAifType
_IsdnEndpointIfType_Object = MibTableColumn
isdnEndpointIfType = _IsdnEndpointIfType_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 3),
    _IsdnEndpointIfType_Type()
)
isdnEndpointIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnEndpointIfType.setStatus("current")


class _IsdnEndpointTeiType_Type(Integer32):
    """Custom type isdnEndpointTeiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_IsdnEndpointTeiType_Type.__name__ = "Integer32"
_IsdnEndpointTeiType_Object = MibTableColumn
isdnEndpointTeiType = _IsdnEndpointTeiType_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 4),
    _IsdnEndpointTeiType_Type()
)
isdnEndpointTeiType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnEndpointTeiType.setStatus("current")


class _IsdnEndpointTeiValue_Type(Integer32):
    """Custom type isdnEndpointTeiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsdnEndpointTeiValue_Type.__name__ = "Integer32"
_IsdnEndpointTeiValue_Object = MibTableColumn
isdnEndpointTeiValue = _IsdnEndpointTeiValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 5),
    _IsdnEndpointTeiValue_Type()
)
isdnEndpointTeiValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnEndpointTeiValue.setStatus("current")
_IsdnEndpointSpid_Type = DisplayString
_IsdnEndpointSpid_Object = MibTableColumn
isdnEndpointSpid = _IsdnEndpointSpid_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 6),
    _IsdnEndpointSpid_Type()
)
isdnEndpointSpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnEndpointSpid.setStatus("current")
_IsdnEndpointStatus_Type = RowStatus
_IsdnEndpointStatus_Object = MibTableColumn
isdnEndpointStatus = _IsdnEndpointStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 7),
    _IsdnEndpointStatus_Type()
)
isdnEndpointStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnEndpointStatus.setStatus("current")
_IsdnDirectoryGroup_ObjectIdentity = ObjectIdentity
isdnDirectoryGroup = _IsdnDirectoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 5)
)
_IsdnDirectoryTable_Object = MibTable
isdnDirectoryTable = _IsdnDirectoryTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1)
)
if mibBuilder.loadTexts:
    isdnDirectoryTable.setStatus("current")
_IsdnDirectoryEntry_Object = MibTableRow
isdnDirectoryEntry = _IsdnDirectoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1)
)
isdnDirectoryEntry.setIndexNames(
    (0, "ISDN-MIB", "isdnDirectoryIndex"),
)
if mibBuilder.loadTexts:
    isdnDirectoryEntry.setStatus("current")


class _IsdnDirectoryIndex_Type(Integer32):
    """Custom type isdnDirectoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsdnDirectoryIndex_Type.__name__ = "Integer32"
_IsdnDirectoryIndex_Object = MibTableColumn
isdnDirectoryIndex = _IsdnDirectoryIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 1),
    _IsdnDirectoryIndex_Type()
)
isdnDirectoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnDirectoryIndex.setStatus("current")
_IsdnDirectoryNumber_Type = DisplayString
_IsdnDirectoryNumber_Object = MibTableColumn
isdnDirectoryNumber = _IsdnDirectoryNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 2),
    _IsdnDirectoryNumber_Type()
)
isdnDirectoryNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnDirectoryNumber.setStatus("current")


class _IsdnDirectorySigIndex_Type(Integer32):
    """Custom type isdnDirectorySigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IsdnDirectorySigIndex_Type.__name__ = "Integer32"
_IsdnDirectorySigIndex_Object = MibTableColumn
isdnDirectorySigIndex = _IsdnDirectorySigIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 3),
    _IsdnDirectorySigIndex_Type()
)
isdnDirectorySigIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnDirectorySigIndex.setStatus("current")
_IsdnDirectoryStatus_Type = RowStatus
_IsdnDirectoryStatus_Object = MibTableColumn
isdnDirectoryStatus = _IsdnDirectoryStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 4),
    _IsdnDirectoryStatus_Type()
)
isdnDirectoryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    isdnDirectoryStatus.setStatus("current")
_IsdnMibTrapPrefix_ObjectIdentity = ObjectIdentity
isdnMibTrapPrefix = _IsdnMibTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 2)
)
_IsdnMibConformance_ObjectIdentity = ObjectIdentity
isdnMibConformance = _IsdnMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 2)
)
_IsdnMibTraps_ObjectIdentity = ObjectIdentity
isdnMibTraps = _IsdnMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 0)
)
_IsdnMibCompliances_ObjectIdentity = ObjectIdentity
isdnMibCompliances = _IsdnMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 1)
)
_IsdnMibGroups_ObjectIdentity = ObjectIdentity
isdnMibGroups = _IsdnMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 2)
)
isdnSignalingEntry.registerAugmentions(
    ("ISDN-MIB",
     "isdnSignalingStatsEntry")
)
isdnSignalingStatsEntry.setIndexNames(*isdnSignalingEntry.getIndexNames())

# Managed Objects groups

isdnMibBasicRateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 1)
)
isdnMibBasicRateGroup.setObjects(
      *(("ISDN-MIB", "isdnBasicRateIfType"),
        ("ISDN-MIB", "isdnBasicRateLineTopology"),
        ("ISDN-MIB", "isdnBasicRateIfMode"),
        ("ISDN-MIB", "isdnBasicRateSignalMode"))
)
if mibBuilder.loadTexts:
    isdnMibBasicRateGroup.setStatus("current")

isdnMibBearerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 2)
)
isdnMibBearerGroup.setObjects(
      *(("ISDN-MIB", "isdnBearerChannelType"),
        ("ISDN-MIB", "isdnBearerOperStatus"),
        ("ISDN-MIB", "isdnBearerChannelNumber"),
        ("ISDN-MIB", "isdnBearerPeerAddress"),
        ("ISDN-MIB", "isdnBearerPeerSubAddress"),
        ("ISDN-MIB", "isdnBearerCallOrigin"),
        ("ISDN-MIB", "isdnBearerInfoType"),
        ("ISDN-MIB", "isdnBearerMultirate"),
        ("ISDN-MIB", "isdnBearerCallSetupTime"),
        ("ISDN-MIB", "isdnBearerCallConnectTime"),
        ("ISDN-MIB", "isdnBearerChargedUnits"))
)
if mibBuilder.loadTexts:
    isdnMibBearerGroup.setStatus("current")

isdnMibSignalingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 3)
)
isdnMibSignalingGroup.setObjects(
      *(("ISDN-MIB", "isdnSignalingGetIndex"),
        ("ISDN-MIB", "isdnSignalingIfIndex"),
        ("ISDN-MIB", "isdnSignalingProtocol"),
        ("ISDN-MIB", "isdnSignalingCallingAddress"),
        ("ISDN-MIB", "isdnSignalingSubAddress"),
        ("ISDN-MIB", "isdnSignalingBchannelCount"),
        ("ISDN-MIB", "isdnSignalingInfoTrapEnable"),
        ("ISDN-MIB", "isdnSignalingStatus"),
        ("ISDN-MIB", "isdnSigStatsInCalls"),
        ("ISDN-MIB", "isdnSigStatsInConnected"),
        ("ISDN-MIB", "isdnSigStatsOutCalls"),
        ("ISDN-MIB", "isdnSigStatsOutConnected"),
        ("ISDN-MIB", "isdnSigStatsChargedUnits"),
        ("ISDN-MIB", "isdnLapdPrimaryChannel"),
        ("ISDN-MIB", "isdnLapdOperStatus"),
        ("ISDN-MIB", "isdnLapdPeerSabme"),
        ("ISDN-MIB", "isdnLapdRecvdFrmr"))
)
if mibBuilder.loadTexts:
    isdnMibSignalingGroup.setStatus("current")

isdnMibEndpointGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 4)
)
isdnMibEndpointGroup.setObjects(
      *(("ISDN-MIB", "isdnEndpointGetIndex"),
        ("ISDN-MIB", "isdnEndpointIfIndex"),
        ("ISDN-MIB", "isdnEndpointIfType"),
        ("ISDN-MIB", "isdnEndpointTeiType"),
        ("ISDN-MIB", "isdnEndpointTeiValue"),
        ("ISDN-MIB", "isdnEndpointSpid"),
        ("ISDN-MIB", "isdnEndpointStatus"))
)
if mibBuilder.loadTexts:
    isdnMibEndpointGroup.setStatus("current")

isdnMibDirectoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 5)
)
isdnMibDirectoryGroup.setObjects(
      *(("ISDN-MIB", "isdnDirectoryNumber"),
        ("ISDN-MIB", "isdnDirectorySigIndex"),
        ("ISDN-MIB", "isdnDirectoryStatus"))
)
if mibBuilder.loadTexts:
    isdnMibDirectoryGroup.setStatus("current")


# Notification objects

isdnMibCallInformation = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 0, 1)
)
isdnMibCallInformation.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ISDN-MIB", "isdnBearerOperStatus"),
        ("ISDN-MIB", "isdnBearerPeerAddress"),
        ("ISDN-MIB", "isdnBearerPeerSubAddress"),
        ("ISDN-MIB", "isdnBearerCallSetupTime"),
        ("ISDN-MIB", "isdnBearerInfoType"),
        ("ISDN-MIB", "isdnBearerCallOrigin"))
)
if mibBuilder.loadTexts:
    isdnMibCallInformation.setStatus(
        "current"
    )


# Notifications groups

isdnMibNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 2, 6)
)
isdnMibNotificationsGroup.setObjects(
    ("ISDN-MIB", "isdnMibCallInformation")
)
if mibBuilder.loadTexts:
    isdnMibNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

isdnMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 20, 2, 1, 1)
)
if mibBuilder.loadTexts:
    isdnMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISDN-MIB",
    **{"IsdnSignalingProtocol": IsdnSignalingProtocol,
       "isdnMib": isdnMib,
       "isdnMibObjects": isdnMibObjects,
       "isdnBasicRateGroup": isdnBasicRateGroup,
       "isdnBasicRateTable": isdnBasicRateTable,
       "isdnBasicRateEntry": isdnBasicRateEntry,
       "isdnBasicRateIfType": isdnBasicRateIfType,
       "isdnBasicRateLineTopology": isdnBasicRateLineTopology,
       "isdnBasicRateIfMode": isdnBasicRateIfMode,
       "isdnBasicRateSignalMode": isdnBasicRateSignalMode,
       "isdnBearerGroup": isdnBearerGroup,
       "isdnBearerTable": isdnBearerTable,
       "isdnBearerEntry": isdnBearerEntry,
       "isdnBearerChannelType": isdnBearerChannelType,
       "isdnBearerOperStatus": isdnBearerOperStatus,
       "isdnBearerChannelNumber": isdnBearerChannelNumber,
       "isdnBearerPeerAddress": isdnBearerPeerAddress,
       "isdnBearerPeerSubAddress": isdnBearerPeerSubAddress,
       "isdnBearerCallOrigin": isdnBearerCallOrigin,
       "isdnBearerInfoType": isdnBearerInfoType,
       "isdnBearerMultirate": isdnBearerMultirate,
       "isdnBearerCallSetupTime": isdnBearerCallSetupTime,
       "isdnBearerCallConnectTime": isdnBearerCallConnectTime,
       "isdnBearerChargedUnits": isdnBearerChargedUnits,
       "isdnSignalingGroup": isdnSignalingGroup,
       "isdnSignalingGetIndex": isdnSignalingGetIndex,
       "isdnSignalingTable": isdnSignalingTable,
       "isdnSignalingEntry": isdnSignalingEntry,
       "isdnSignalingIndex": isdnSignalingIndex,
       "isdnSignalingIfIndex": isdnSignalingIfIndex,
       "isdnSignalingProtocol": isdnSignalingProtocol,
       "isdnSignalingCallingAddress": isdnSignalingCallingAddress,
       "isdnSignalingSubAddress": isdnSignalingSubAddress,
       "isdnSignalingBchannelCount": isdnSignalingBchannelCount,
       "isdnSignalingInfoTrapEnable": isdnSignalingInfoTrapEnable,
       "isdnSignalingStatus": isdnSignalingStatus,
       "isdnSignalingStatsTable": isdnSignalingStatsTable,
       "isdnSignalingStatsEntry": isdnSignalingStatsEntry,
       "isdnSigStatsInCalls": isdnSigStatsInCalls,
       "isdnSigStatsInConnected": isdnSigStatsInConnected,
       "isdnSigStatsOutCalls": isdnSigStatsOutCalls,
       "isdnSigStatsOutConnected": isdnSigStatsOutConnected,
       "isdnSigStatsChargedUnits": isdnSigStatsChargedUnits,
       "isdnLapdTable": isdnLapdTable,
       "isdnLapdEntry": isdnLapdEntry,
       "isdnLapdPrimaryChannel": isdnLapdPrimaryChannel,
       "isdnLapdOperStatus": isdnLapdOperStatus,
       "isdnLapdPeerSabme": isdnLapdPeerSabme,
       "isdnLapdRecvdFrmr": isdnLapdRecvdFrmr,
       "isdnEndpointGroup": isdnEndpointGroup,
       "isdnEndpointGetIndex": isdnEndpointGetIndex,
       "isdnEndpointTable": isdnEndpointTable,
       "isdnEndpointEntry": isdnEndpointEntry,
       "isdnEndpointIndex": isdnEndpointIndex,
       "isdnEndpointIfIndex": isdnEndpointIfIndex,
       "isdnEndpointIfType": isdnEndpointIfType,
       "isdnEndpointTeiType": isdnEndpointTeiType,
       "isdnEndpointTeiValue": isdnEndpointTeiValue,
       "isdnEndpointSpid": isdnEndpointSpid,
       "isdnEndpointStatus": isdnEndpointStatus,
       "isdnDirectoryGroup": isdnDirectoryGroup,
       "isdnDirectoryTable": isdnDirectoryTable,
       "isdnDirectoryEntry": isdnDirectoryEntry,
       "isdnDirectoryIndex": isdnDirectoryIndex,
       "isdnDirectoryNumber": isdnDirectoryNumber,
       "isdnDirectorySigIndex": isdnDirectorySigIndex,
       "isdnDirectoryStatus": isdnDirectoryStatus,
       "isdnMibTrapPrefix": isdnMibTrapPrefix,
       "isdnMibConformance": isdnMibConformance,
       "isdnMibTraps": isdnMibTraps,
       "isdnMibCallInformation": isdnMibCallInformation,
       "isdnMibCompliances": isdnMibCompliances,
       "isdnMibCompliance": isdnMibCompliance,
       "isdnMibGroups": isdnMibGroups,
       "isdnMibBasicRateGroup": isdnMibBasicRateGroup,
       "isdnMibBearerGroup": isdnMibBearerGroup,
       "isdnMibSignalingGroup": isdnMibSignalingGroup,
       "isdnMibEndpointGroup": isdnMibEndpointGroup,
       "isdnMibDirectoryGroup": isdnMibDirectoryGroup,
       "isdnMibNotificationsGroup": isdnMibNotificationsGroup}
)
