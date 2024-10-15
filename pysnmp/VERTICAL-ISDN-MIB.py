# SNMP MIB module (VERTICAL-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERTICAL-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:23 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EntryStatus,) = mibBuilder.importSymbols(
    "RFC1271-MIB",
    "EntryStatus")

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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "transmission")

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")

(vertical,) = mibBuilder.importSymbols(
    "VERTICALT1-E1-MIB",
    "vertical")


# MODULE-IDENTITY


# Types definitions



class IsdnSignalingProtocol(Integer32):
    """Custom type IsdnSignalingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              10,
              263)
        )
    )
    namedValues = NamedValues(
        *(("dms100", 7),
          ("dms100s100", 263),
          ("ess4", 5),
          ("ess5", 6),
          ("ni2", 10),
          ("other", 1))
    )





class TestAndIncr(Integer32):
    """Custom type TestAndIncr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VisdnMibObjects_ObjectIdentity = ObjectIdentity
visdnMibObjects = _VisdnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 5)
)
_VisdnBearerGroup_ObjectIdentity = ObjectIdentity
visdnBearerGroup = _VisdnBearerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2)
)
_VisdnBearerTable_Object = MibTable
visdnBearerTable = _VisdnBearerTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1)
)
if mibBuilder.loadTexts:
    visdnBearerTable.setStatus("mandatory")
_VisdnBearerEntry_Object = MibTableRow
visdnBearerEntry = _VisdnBearerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1)
)
visdnBearerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    visdnBearerEntry.setStatus("mandatory")


class _VisdnBearerChannelType_Type(Integer32):
    """Custom type visdnBearerChannelType based on Integer32"""
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


_VisdnBearerChannelType_Type.__name__ = "Integer32"
_VisdnBearerChannelType_Object = MibTableColumn
visdnBearerChannelType = _VisdnBearerChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 1),
    _VisdnBearerChannelType_Type()
)
visdnBearerChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerChannelType.setStatus("mandatory")


class _VisdnBearerOperStatus_Type(Integer32):
    """Custom type visdnBearerOperStatus based on Integer32"""
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


_VisdnBearerOperStatus_Type.__name__ = "Integer32"
_VisdnBearerOperStatus_Object = MibTableColumn
visdnBearerOperStatus = _VisdnBearerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 2),
    _VisdnBearerOperStatus_Type()
)
visdnBearerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerOperStatus.setStatus("mandatory")


class _VisdnBearerChannelNumber_Type(Integer32):
    """Custom type visdnBearerChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VisdnBearerChannelNumber_Type.__name__ = "Integer32"
_VisdnBearerChannelNumber_Object = MibTableColumn
visdnBearerChannelNumber = _VisdnBearerChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 3),
    _VisdnBearerChannelNumber_Type()
)
visdnBearerChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerChannelNumber.setStatus("mandatory")
_VisdnBearerPeerAddress_Type = DisplayString
_VisdnBearerPeerAddress_Object = MibTableColumn
visdnBearerPeerAddress = _VisdnBearerPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 4),
    _VisdnBearerPeerAddress_Type()
)
visdnBearerPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerPeerAddress.setStatus("mandatory")
_VisdnBearerPeerSubAddress_Type = DisplayString
_VisdnBearerPeerSubAddress_Object = MibTableColumn
visdnBearerPeerSubAddress = _VisdnBearerPeerSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 5),
    _VisdnBearerPeerSubAddress_Type()
)
visdnBearerPeerSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerPeerSubAddress.setStatus("mandatory")


class _VisdnBearerCallOrigin_Type(Integer32):
    """Custom type visdnBearerCallOrigin based on Integer32"""
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


_VisdnBearerCallOrigin_Type.__name__ = "Integer32"
_VisdnBearerCallOrigin_Object = MibTableColumn
visdnBearerCallOrigin = _VisdnBearerCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 6),
    _VisdnBearerCallOrigin_Type()
)
visdnBearerCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerCallOrigin.setStatus("mandatory")


class _VisdnBearerInfoType_Type(Integer32):
    """Custom type visdnBearerInfoType based on Integer32"""
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


_VisdnBearerInfoType_Type.__name__ = "Integer32"
_VisdnBearerInfoType_Object = MibTableColumn
visdnBearerInfoType = _VisdnBearerInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 7),
    _VisdnBearerInfoType_Type()
)
visdnBearerInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerInfoType.setStatus("mandatory")
_VisdnBearerMultirate_Type = TruthValue
_VisdnBearerMultirate_Object = MibTableColumn
visdnBearerMultirate = _VisdnBearerMultirate_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 8),
    _VisdnBearerMultirate_Type()
)
visdnBearerMultirate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerMultirate.setStatus("mandatory")
_VisdnBearerCallSetupTime_Type = TimeStamp
_VisdnBearerCallSetupTime_Object = MibTableColumn
visdnBearerCallSetupTime = _VisdnBearerCallSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 9),
    _VisdnBearerCallSetupTime_Type()
)
visdnBearerCallSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerCallSetupTime.setStatus("mandatory")
_VisdnBearerCallConnectTime_Type = TimeStamp
_VisdnBearerCallConnectTime_Object = MibTableColumn
visdnBearerCallConnectTime = _VisdnBearerCallConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 10),
    _VisdnBearerCallConnectTime_Type()
)
visdnBearerCallConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerCallConnectTime.setStatus("mandatory")
_VisdnBearerChargedUnits_Type = Gauge32
_VisdnBearerChargedUnits_Object = MibTableColumn
visdnBearerChargedUnits = _VisdnBearerChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 2, 1, 1, 11),
    _VisdnBearerChargedUnits_Type()
)
visdnBearerChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnBearerChargedUnits.setStatus("mandatory")
_VisdnSignalingGroup_ObjectIdentity = ObjectIdentity
visdnSignalingGroup = _VisdnSignalingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3)
)
_VisdnSignalingGetIndex_Type = TestAndIncr
_VisdnSignalingGetIndex_Object = MibScalar
visdnSignalingGetIndex = _VisdnSignalingGetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 1),
    _VisdnSignalingGetIndex_Type()
)
visdnSignalingGetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSignalingGetIndex.setStatus("mandatory")
_VisdnSignalingTable_Object = MibTable
visdnSignalingTable = _VisdnSignalingTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 2)
)
if mibBuilder.loadTexts:
    visdnSignalingTable.setStatus("mandatory")
_VisdnSignalingEntry_Object = MibTableRow
visdnSignalingEntry = _VisdnSignalingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 2, 1)
)
visdnSignalingEntry.setIndexNames(
    (0, "VERTICAL-ISDN-MIB", "visdnSignalingIndex"),
)
if mibBuilder.loadTexts:
    visdnSignalingEntry.setStatus("mandatory")


class _VisdnSignalingIndex_Type(Integer32):
    """Custom type visdnSignalingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VisdnSignalingIndex_Type.__name__ = "Integer32"
_VisdnSignalingIndex_Object = MibTableColumn
visdnSignalingIndex = _VisdnSignalingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 2, 1, 1),
    _VisdnSignalingIndex_Type()
)
visdnSignalingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    visdnSignalingIndex.setStatus("mandatory")


class _VisdnSignalingIfIndex_Type(Integer32):
    """Custom type visdnSignalingIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VisdnSignalingIfIndex_Type.__name__ = "Integer32"
_VisdnSignalingIfIndex_Object = MibTableColumn
visdnSignalingIfIndex = _VisdnSignalingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 2, 1, 2),
    _VisdnSignalingIfIndex_Type()
)
visdnSignalingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSignalingIfIndex.setStatus("mandatory")
_VisdnSignalingProtocol_Type = IsdnSignalingProtocol
_VisdnSignalingProtocol_Object = MibTableColumn
visdnSignalingProtocol = _VisdnSignalingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 2, 1, 3),
    _VisdnSignalingProtocol_Type()
)
visdnSignalingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSignalingProtocol.setStatus("mandatory")
_VisdnSignalingCallingAddress_Type = DisplayString
_VisdnSignalingCallingAddress_Object = MibTableColumn
visdnSignalingCallingAddress = _VisdnSignalingCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 2, 1, 4),
    _VisdnSignalingCallingAddress_Type()
)
visdnSignalingCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSignalingCallingAddress.setStatus("mandatory")
_VisdnSignalingSubAddress_Type = DisplayString
_VisdnSignalingSubAddress_Object = MibTableColumn
visdnSignalingSubAddress = _VisdnSignalingSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 2, 1, 5),
    _VisdnSignalingSubAddress_Type()
)
visdnSignalingSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSignalingSubAddress.setStatus("mandatory")


class _VisdnSignalingBchannelCount_Type(Integer32):
    """Custom type visdnSignalingBchannelCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VisdnSignalingBchannelCount_Type.__name__ = "Integer32"
_VisdnSignalingBchannelCount_Object = MibTableColumn
visdnSignalingBchannelCount = _VisdnSignalingBchannelCount_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 2, 1, 6),
    _VisdnSignalingBchannelCount_Type()
)
visdnSignalingBchannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSignalingBchannelCount.setStatus("mandatory")


class _VisdnSignalingInfoTrapEnable_Type(Integer32):
    """Custom type visdnSignalingInfoTrapEnable based on Integer32"""
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


_VisdnSignalingInfoTrapEnable_Type.__name__ = "Integer32"
_VisdnSignalingInfoTrapEnable_Object = MibTableColumn
visdnSignalingInfoTrapEnable = _VisdnSignalingInfoTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 2, 1, 7),
    _VisdnSignalingInfoTrapEnable_Type()
)
visdnSignalingInfoTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSignalingInfoTrapEnable.setStatus("mandatory")
_VisdnSignalingStatus_Type = EntryStatus
_VisdnSignalingStatus_Object = MibTableColumn
visdnSignalingStatus = _VisdnSignalingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 2, 1, 8),
    _VisdnSignalingStatus_Type()
)
visdnSignalingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSignalingStatus.setStatus("mandatory")
_VisdnSignalingStatsTable_Object = MibTable
visdnSignalingStatsTable = _VisdnSignalingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 3)
)
if mibBuilder.loadTexts:
    visdnSignalingStatsTable.setStatus("mandatory")
_VisdnSignalingStatsEntry_Object = MibTableRow
visdnSignalingStatsEntry = _VisdnSignalingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 3, 1)
)
visdnSignalingStatsEntry.setIndexNames(
    (0, "VERTICAL-ISDN-MIB", "visdnSignalingIndex"),
)
if mibBuilder.loadTexts:
    visdnSignalingStatsEntry.setStatus("mandatory")
_VisdnSigStatsInCalls_Type = Counter32
_VisdnSigStatsInCalls_Object = MibTableColumn
visdnSigStatsInCalls = _VisdnSigStatsInCalls_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 3, 1, 1),
    _VisdnSigStatsInCalls_Type()
)
visdnSigStatsInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSigStatsInCalls.setStatus("mandatory")
_VisdnSigStatsInConnected_Type = Counter32
_VisdnSigStatsInConnected_Object = MibTableColumn
visdnSigStatsInConnected = _VisdnSigStatsInConnected_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 3, 1, 2),
    _VisdnSigStatsInConnected_Type()
)
visdnSigStatsInConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSigStatsInConnected.setStatus("mandatory")
_VisdnSigStatsOutCalls_Type = Counter32
_VisdnSigStatsOutCalls_Object = MibTableColumn
visdnSigStatsOutCalls = _VisdnSigStatsOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 3, 1, 3),
    _VisdnSigStatsOutCalls_Type()
)
visdnSigStatsOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSigStatsOutCalls.setStatus("mandatory")
_VisdnSigStatsOutConnected_Type = Counter32
_VisdnSigStatsOutConnected_Object = MibTableColumn
visdnSigStatsOutConnected = _VisdnSigStatsOutConnected_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 3, 1, 4),
    _VisdnSigStatsOutConnected_Type()
)
visdnSigStatsOutConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSigStatsOutConnected.setStatus("mandatory")
_VisdnSigStatsChargedUnits_Type = Counter32
_VisdnSigStatsChargedUnits_Object = MibTableColumn
visdnSigStatsChargedUnits = _VisdnSigStatsChargedUnits_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 3, 1, 5),
    _VisdnSigStatsChargedUnits_Type()
)
visdnSigStatsChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnSigStatsChargedUnits.setStatus("mandatory")
_VisdnLapdTable_Object = MibTable
visdnLapdTable = _VisdnLapdTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 4)
)
if mibBuilder.loadTexts:
    visdnLapdTable.setStatus("mandatory")
_VisdnLapdEntry_Object = MibTableRow
visdnLapdEntry = _VisdnLapdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 4, 1)
)
visdnLapdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    visdnLapdEntry.setStatus("mandatory")
_VisdnLapdPrimaryChannel_Type = TruthValue
_VisdnLapdPrimaryChannel_Object = MibTableColumn
visdnLapdPrimaryChannel = _VisdnLapdPrimaryChannel_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 4, 1, 1),
    _VisdnLapdPrimaryChannel_Type()
)
visdnLapdPrimaryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnLapdPrimaryChannel.setStatus("mandatory")


class _VisdnLapdOperStatus_Type(Integer32):
    """Custom type visdnLapdOperStatus based on Integer32"""
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


_VisdnLapdOperStatus_Type.__name__ = "Integer32"
_VisdnLapdOperStatus_Object = MibTableColumn
visdnLapdOperStatus = _VisdnLapdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 4, 1, 2),
    _VisdnLapdOperStatus_Type()
)
visdnLapdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnLapdOperStatus.setStatus("mandatory")
_VisdnLapdPeerSabme_Type = Counter32
_VisdnLapdPeerSabme_Object = MibTableColumn
visdnLapdPeerSabme = _VisdnLapdPeerSabme_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 4, 1, 3),
    _VisdnLapdPeerSabme_Type()
)
visdnLapdPeerSabme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnLapdPeerSabme.setStatus("mandatory")
_VisdnLapdRecvdFrmr_Type = Counter32
_VisdnLapdRecvdFrmr_Object = MibTableColumn
visdnLapdRecvdFrmr = _VisdnLapdRecvdFrmr_Object(
    (1, 3, 6, 1, 4, 1, 2338, 5, 3, 4, 1, 4),
    _VisdnLapdRecvdFrmr_Type()
)
visdnLapdRecvdFrmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    visdnLapdRecvdFrmr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTICAL-ISDN-MIB",
    **{"IsdnSignalingProtocol": IsdnSignalingProtocol,
       "TestAndIncr": TestAndIncr,
       "TruthValue": TruthValue,
       "visdnMibObjects": visdnMibObjects,
       "visdnBearerGroup": visdnBearerGroup,
       "visdnBearerTable": visdnBearerTable,
       "visdnBearerEntry": visdnBearerEntry,
       "visdnBearerChannelType": visdnBearerChannelType,
       "visdnBearerOperStatus": visdnBearerOperStatus,
       "visdnBearerChannelNumber": visdnBearerChannelNumber,
       "visdnBearerPeerAddress": visdnBearerPeerAddress,
       "visdnBearerPeerSubAddress": visdnBearerPeerSubAddress,
       "visdnBearerCallOrigin": visdnBearerCallOrigin,
       "visdnBearerInfoType": visdnBearerInfoType,
       "visdnBearerMultirate": visdnBearerMultirate,
       "visdnBearerCallSetupTime": visdnBearerCallSetupTime,
       "visdnBearerCallConnectTime": visdnBearerCallConnectTime,
       "visdnBearerChargedUnits": visdnBearerChargedUnits,
       "visdnSignalingGroup": visdnSignalingGroup,
       "visdnSignalingGetIndex": visdnSignalingGetIndex,
       "visdnSignalingTable": visdnSignalingTable,
       "visdnSignalingEntry": visdnSignalingEntry,
       "visdnSignalingIndex": visdnSignalingIndex,
       "visdnSignalingIfIndex": visdnSignalingIfIndex,
       "visdnSignalingProtocol": visdnSignalingProtocol,
       "visdnSignalingCallingAddress": visdnSignalingCallingAddress,
       "visdnSignalingSubAddress": visdnSignalingSubAddress,
       "visdnSignalingBchannelCount": visdnSignalingBchannelCount,
       "visdnSignalingInfoTrapEnable": visdnSignalingInfoTrapEnable,
       "visdnSignalingStatus": visdnSignalingStatus,
       "visdnSignalingStatsTable": visdnSignalingStatsTable,
       "visdnSignalingStatsEntry": visdnSignalingStatsEntry,
       "visdnSigStatsInCalls": visdnSigStatsInCalls,
       "visdnSigStatsInConnected": visdnSigStatsInConnected,
       "visdnSigStatsOutCalls": visdnSigStatsOutCalls,
       "visdnSigStatsOutConnected": visdnSigStatsOutConnected,
       "visdnSigStatsChargedUnits": visdnSigStatsChargedUnits,
       "visdnLapdTable": visdnLapdTable,
       "visdnLapdEntry": visdnLapdEntry,
       "visdnLapdPrimaryChannel": visdnLapdPrimaryChannel,
       "visdnLapdOperStatus": visdnLapdOperStatus,
       "visdnLapdPeerSabme": visdnLapdPeerSabme,
       "visdnLapdRecvdFrmr": visdnLapdRecvdFrmr}
)
