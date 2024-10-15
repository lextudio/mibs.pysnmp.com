# SNMP MIB module (AcGateway) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AcGateway
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:01 2024
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

(acBoardMibs,
 acGeneric,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acGateway = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GwConfiguration_ObjectIdentity = ObjectIdentity
gwConfiguration = _GwConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1)
)
_ChannelsSetting_ObjectIdentity = ObjectIdentity
channelsSetting = _ChannelsSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1)
)


class _ChannelsSettingSelectMode_Type(Integer32):
    """Custom type channelsSettingSelectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ascendingAlways", 2),
          ("byDestPhoneNumber", 0),
          ("byDestinationPhoneNumberCyclicAscending", 5),
          ("bySourcePhoneNumber", 6),
          ("cyclicAscending", 1),
          ("cyclicDescending", 3),
          ("descendingAlways", 4),
          ("trunkCyclicAscending", 7))
    )


_ChannelsSettingSelectMode_Type.__name__ = "Integer32"
_ChannelsSettingSelectMode_Object = MibScalar
channelsSettingSelectMode = _ChannelsSettingSelectMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 1),
    _ChannelsSettingSelectMode_Type()
)
channelsSettingSelectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelsSettingSelectMode.setStatus("current")
_ChannelsTable_Object = MibTable
channelsTable = _ChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21)
)
if mibBuilder.loadTexts:
    channelsTable.setStatus("current")
_ChannelsEntry_Object = MibTableRow
channelsEntry = _ChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1)
)
channelsEntry.setIndexNames(
    (0, "AcGateway", "channelsIndex"),
)
if mibBuilder.loadTexts:
    channelsEntry.setStatus("current")


class _ChannelsIndex_Type(Unsigned32):
    """Custom type channelsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChannelsIndex_Type.__name__ = "Unsigned32"
_ChannelsIndex_Object = MibTableColumn
channelsIndex = _ChannelsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 1),
    _ChannelsIndex_Type()
)
channelsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelsIndex.setStatus("current")
_ChannelsRowStatus_Type = RowStatus
_ChannelsRowStatus_Object = MibTableColumn
channelsRowStatus = _ChannelsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 2),
    _ChannelsRowStatus_Type()
)
channelsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelsRowStatus.setStatus("current")


class _ChannelsAction_Type(Integer32):
    """Custom type channelsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ChannelsAction_Type.__name__ = "Integer32"
_ChannelsAction_Object = MibTableColumn
channelsAction = _ChannelsAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 3),
    _ChannelsAction_Type()
)
channelsAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelsAction.setStatus("current")


class _ChannelsActionResult_Type(Integer32):
    """Custom type channelsActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ChannelsActionResult_Type.__name__ = "Integer32"
_ChannelsActionResult_Object = MibTableColumn
channelsActionResult = _ChannelsActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 4),
    _ChannelsActionResult_Type()
)
channelsActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelsActionResult.setStatus("current")


class _ChannelsTrunkID_Type(Unsigned32):
    """Custom type channelsTrunkID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelsTrunkID_Type.__name__ = "Unsigned32"
_ChannelsTrunkID_Object = MibTableColumn
channelsTrunkID = _ChannelsTrunkID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 5),
    _ChannelsTrunkID_Type()
)
channelsTrunkID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelsTrunkID.setStatus("current")


class _ChannelsStartingCh_Type(Unsigned32):
    """Custom type channelsStartingCh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2016),
    )


_ChannelsStartingCh_Type.__name__ = "Unsigned32"
_ChannelsStartingCh_Object = MibTableColumn
channelsStartingCh = _ChannelsStartingCh_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 6),
    _ChannelsStartingCh_Type()
)
channelsStartingCh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelsStartingCh.setStatus("current")


class _ChannelsLastCh_Type(Unsigned32):
    """Custom type channelsLastCh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2016),
    )


_ChannelsLastCh_Type.__name__ = "Unsigned32"
_ChannelsLastCh_Object = MibTableColumn
channelsLastCh = _ChannelsLastCh_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 7),
    _ChannelsLastCh_Type()
)
channelsLastCh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelsLastCh.setStatus("current")


class _ChannelsStartingPhoneNum_Type(SnmpAdminString):
    """Custom type channelsStartingPhoneNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_ChannelsStartingPhoneNum_Type.__name__ = "SnmpAdminString"
_ChannelsStartingPhoneNum_Object = MibTableColumn
channelsStartingPhoneNum = _ChannelsStartingPhoneNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 8),
    _ChannelsStartingPhoneNum_Type()
)
channelsStartingPhoneNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelsStartingPhoneNum.setStatus("current")


class _ChannelsTrunkGroupID_Type(Unsigned32):
    """Custom type channelsTrunkGroupID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelsTrunkGroupID_Type.__name__ = "Unsigned32"
_ChannelsTrunkGroupID_Object = MibTableColumn
channelsTrunkGroupID = _ChannelsTrunkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 9),
    _ChannelsTrunkGroupID_Type()
)
channelsTrunkGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelsTrunkGroupID.setStatus("current")


class _ChannelsProfileID_Type(Unsigned32):
    """Custom type channelsProfileID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ChannelsProfileID_Type.__name__ = "Unsigned32"
_ChannelsProfileID_Object = MibTableColumn
channelsProfileID = _ChannelsProfileID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 10),
    _ChannelsProfileID_Type()
)
channelsProfileID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelsProfileID.setStatus("current")


class _ChannelsLastTrunkID_Type(Unsigned32):
    """Custom type channelsLastTrunkID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelsLastTrunkID_Type.__name__ = "Unsigned32"
_ChannelsLastTrunkID_Object = MibTableColumn
channelsLastTrunkID = _ChannelsLastTrunkID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 11),
    _ChannelsLastTrunkID_Type()
)
channelsLastTrunkID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelsLastTrunkID.setStatus("current")


class _ChannelsModule_Type(Unsigned32):
    """Custom type channelsModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelsModule_Type.__name__ = "Unsigned32"
_ChannelsModule_Object = MibTableColumn
channelsModule = _ChannelsModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 21, 1, 12),
    _ChannelsModule_Type()
)
channelsModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    channelsModule.setStatus("current")
_TrunkGroupSettingsTable_Object = MibTable
trunkGroupSettingsTable = _TrunkGroupSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    trunkGroupSettingsTable.setStatus("current")
_TrunkGroupSettingsEntry_Object = MibTableRow
trunkGroupSettingsEntry = _TrunkGroupSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1)
)
trunkGroupSettingsEntry.setIndexNames(
    (0, "AcGateway", "trunkGroupSettingsIndex"),
)
if mibBuilder.loadTexts:
    trunkGroupSettingsEntry.setStatus("current")


class _TrunkGroupSettingsIndex_Type(Unsigned32):
    """Custom type trunkGroupSettingsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TrunkGroupSettingsIndex_Type.__name__ = "Unsigned32"
_TrunkGroupSettingsIndex_Object = MibTableColumn
trunkGroupSettingsIndex = _TrunkGroupSettingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 1),
    _TrunkGroupSettingsIndex_Type()
)
trunkGroupSettingsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkGroupSettingsIndex.setStatus("current")
_TrunkGroupSettingsRowStatus_Type = RowStatus
_TrunkGroupSettingsRowStatus_Object = MibTableColumn
trunkGroupSettingsRowStatus = _TrunkGroupSettingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 2),
    _TrunkGroupSettingsRowStatus_Type()
)
trunkGroupSettingsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupSettingsRowStatus.setStatus("current")


class _TrunkGroupSettingsAction_Type(Integer32):
    """Custom type trunkGroupSettingsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_TrunkGroupSettingsAction_Type.__name__ = "Integer32"
_TrunkGroupSettingsAction_Object = MibTableColumn
trunkGroupSettingsAction = _TrunkGroupSettingsAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 3),
    _TrunkGroupSettingsAction_Type()
)
trunkGroupSettingsAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupSettingsAction.setStatus("current")


class _TrunkGroupSettingsActionResult_Type(Integer32):
    """Custom type trunkGroupSettingsActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_TrunkGroupSettingsActionResult_Type.__name__ = "Integer32"
_TrunkGroupSettingsActionResult_Object = MibTableColumn
trunkGroupSettingsActionResult = _TrunkGroupSettingsActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 4),
    _TrunkGroupSettingsActionResult_Type()
)
trunkGroupSettingsActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGroupSettingsActionResult.setStatus("current")


class _TrunkGroupSettingsTrunkGroupID_Type(Unsigned32):
    """Custom type trunkGroupSettingsTrunkGroupID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TrunkGroupSettingsTrunkGroupID_Type.__name__ = "Unsigned32"
_TrunkGroupSettingsTrunkGroupID_Object = MibTableColumn
trunkGroupSettingsTrunkGroupID = _TrunkGroupSettingsTrunkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 5),
    _TrunkGroupSettingsTrunkGroupID_Type()
)
trunkGroupSettingsTrunkGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupSettingsTrunkGroupID.setStatus("current")


class _TrunkGroupSettingsChannelSelectMode_Type(Integer32):
    """Custom type trunkGroupSettingsChannelSelectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ascendingAlways", 2),
          ("byPhoneNumber", 0),
          ("byPhoneNumberCyclicAscending", 5),
          ("bySourcePhoneNumber", 6),
          ("cyclicAscending", 1),
          ("cyclicDescending", 3),
          ("descendingAlways", 4),
          ("trunkAndChannelCyclicAscending", 8),
          ("trunkCyclicAscending", 7),
          ("valueNotSet", 255))
    )


_TrunkGroupSettingsChannelSelectMode_Type.__name__ = "Integer32"
_TrunkGroupSettingsChannelSelectMode_Object = MibTableColumn
trunkGroupSettingsChannelSelectMode = _TrunkGroupSettingsChannelSelectMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 6),
    _TrunkGroupSettingsChannelSelectMode_Type()
)
trunkGroupSettingsChannelSelectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupSettingsChannelSelectMode.setStatus("current")


class _TrunkGroupSettingsRegistrationMode_Type(Integer32):
    """Custom type trunkGroupSettingsRegistrationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("doNotRegister", 4),
          ("notApplicable", 2),
          ("perAccount", 5),
          ("perEndpoint", 0),
          ("perGateway", 1),
          ("valueNotSet", 255))
    )


_TrunkGroupSettingsRegistrationMode_Type.__name__ = "Integer32"
_TrunkGroupSettingsRegistrationMode_Object = MibTableColumn
trunkGroupSettingsRegistrationMode = _TrunkGroupSettingsRegistrationMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 7),
    _TrunkGroupSettingsRegistrationMode_Type()
)
trunkGroupSettingsRegistrationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupSettingsRegistrationMode.setStatus("current")


class _TrunkGroupSettingsGatewayName_Type(SnmpAdminString):
    """Custom type trunkGroupSettingsGatewayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_TrunkGroupSettingsGatewayName_Type.__name__ = "SnmpAdminString"
_TrunkGroupSettingsGatewayName_Object = MibTableColumn
trunkGroupSettingsGatewayName = _TrunkGroupSettingsGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 8),
    _TrunkGroupSettingsGatewayName_Type()
)
trunkGroupSettingsGatewayName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupSettingsGatewayName.setStatus("current")


class _TrunkGroupSettingsContactUser_Type(SnmpAdminString):
    """Custom type trunkGroupSettingsContactUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TrunkGroupSettingsContactUser_Type.__name__ = "SnmpAdminString"
_TrunkGroupSettingsContactUser_Object = MibTableColumn
trunkGroupSettingsContactUser = _TrunkGroupSettingsContactUser_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 9),
    _TrunkGroupSettingsContactUser_Type()
)
trunkGroupSettingsContactUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupSettingsContactUser.setStatus("current")


class _TrunkGroupSettingsServingIPGroup_Type(Integer32):
    """Custom type trunkGroupSettingsServingIPGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_TrunkGroupSettingsServingIPGroup_Type.__name__ = "Integer32"
_TrunkGroupSettingsServingIPGroup_Object = MibTableColumn
trunkGroupSettingsServingIPGroup = _TrunkGroupSettingsServingIPGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 10),
    _TrunkGroupSettingsServingIPGroup_Type()
)
trunkGroupSettingsServingIPGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupSettingsServingIPGroup.setStatus("current")


class _TrunkGroupSettingsMwiInterrogationType_Type(Integer32):
    """Custom type trunkGroupSettingsMwiInterrogationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("notConfigured", 255),
          ("resultNotUsed", 2),
          ("useActivateOnly", 1),
          ("useResult", 3))
    )


_TrunkGroupSettingsMwiInterrogationType_Type.__name__ = "Integer32"
_TrunkGroupSettingsMwiInterrogationType_Object = MibTableColumn
trunkGroupSettingsMwiInterrogationType = _TrunkGroupSettingsMwiInterrogationType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 1, 22, 1, 11),
    _TrunkGroupSettingsMwiInterrogationType_Type()
)
trunkGroupSettingsMwiInterrogationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkGroupSettingsMwiInterrogationType.setStatus("current")
_ManipulationAndRouting_ObjectIdentity = ObjectIdentity
manipulationAndRouting = _ManipulationAndRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2)
)


class _ManipulationAndRoutingModeTel2Ip_Type(Integer32):
    """Custom type manipulationAndRoutingModeTel2Ip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("routeAfterMap", 1),
          ("routeBeforeMap", 0))
    )


_ManipulationAndRoutingModeTel2Ip_Type.__name__ = "Integer32"
_ManipulationAndRoutingModeTel2Ip_Object = MibScalar
manipulationAndRoutingModeTel2Ip = _ManipulationAndRoutingModeTel2Ip_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 1),
    _ManipulationAndRoutingModeTel2Ip_Type()
)
manipulationAndRoutingModeTel2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingModeTel2Ip.setStatus("current")


class _ManipulationAndRoutingModeIp2Tel_Type(Integer32):
    """Custom type manipulationAndRoutingModeIp2Tel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("routeAfterMap", 1),
          ("routeBeforeMap", 0))
    )


_ManipulationAndRoutingModeIp2Tel_Type.__name__ = "Integer32"
_ManipulationAndRoutingModeIp2Tel_Object = MibScalar
manipulationAndRoutingModeIp2Tel = _ManipulationAndRoutingModeIp2Tel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 2),
    _ManipulationAndRoutingModeIp2Tel_Type()
)
manipulationAndRoutingModeIp2Tel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingModeIp2Tel.setStatus("current")


class _ManipulationAndRoutingFilterCalls2Ip_Type(Integer32):
    """Custom type manipulationAndRoutingFilterCalls2Ip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ManipulationAndRoutingFilterCalls2Ip_Type.__name__ = "Integer32"
_ManipulationAndRoutingFilterCalls2Ip_Object = MibScalar
manipulationAndRoutingFilterCalls2Ip = _ManipulationAndRoutingFilterCalls2Ip_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 3),
    _ManipulationAndRoutingFilterCalls2Ip_Type()
)
manipulationAndRoutingFilterCalls2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingFilterCalls2Ip.setStatus("current")


class _ManipulationAndRoutingAltRoutingTel2IpEnable_Type(Integer32):
    """Custom type manipulationAndRoutingAltRoutingTel2IpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("statusOnly", 2))
    )


_ManipulationAndRoutingAltRoutingTel2IpEnable_Type.__name__ = "Integer32"
_ManipulationAndRoutingAltRoutingTel2IpEnable_Object = MibScalar
manipulationAndRoutingAltRoutingTel2IpEnable = _ManipulationAndRoutingAltRoutingTel2IpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 4),
    _ManipulationAndRoutingAltRoutingTel2IpEnable_Type()
)
manipulationAndRoutingAltRoutingTel2IpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingAltRoutingTel2IpEnable.setStatus("current")


class _ManipulationAndRoutingAltRoutingTel2IpMode_Type(Integer32):
    """Custom type manipulationAndRoutingAltRoutingTel2IpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("conn", 1),
          ("none", 0),
          ("qos", 2))
    )


_ManipulationAndRoutingAltRoutingTel2IpMode_Type.__name__ = "Integer32"
_ManipulationAndRoutingAltRoutingTel2IpMode_Object = MibScalar
manipulationAndRoutingAltRoutingTel2IpMode = _ManipulationAndRoutingAltRoutingTel2IpMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 5),
    _ManipulationAndRoutingAltRoutingTel2IpMode_Type()
)
manipulationAndRoutingAltRoutingTel2IpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingAltRoutingTel2IpMode.setStatus("current")


class _ManipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall_Type(Unsigned32):
    """Custom type manipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ManipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall_Type.__name__ = "Unsigned32"
_ManipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall_Object = MibScalar
manipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall = _ManipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 6),
    _ManipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall_Type()
)
manipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall.setStatus("current")


class _ManipulationAndRoutingPreferRouteTable_Type(Integer32):
    """Custom type manipulationAndRoutingPreferRouteTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ManipulationAndRoutingPreferRouteTable_Type.__name__ = "Integer32"
_ManipulationAndRoutingPreferRouteTable_Object = MibScalar
manipulationAndRoutingPreferRouteTable = _ManipulationAndRoutingPreferRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 7),
    _ManipulationAndRoutingPreferRouteTable_Type()
)
manipulationAndRoutingPreferRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingPreferRouteTable.setStatus("current")


class _ManipulationAndRoutingRedundantRoutingMode_Type(Integer32):
    """Custom type manipulationAndRoutingRedundantRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("proxy", 2),
          ("routingTable", 1))
    )


_ManipulationAndRoutingRedundantRoutingMode_Type.__name__ = "Integer32"
_ManipulationAndRoutingRedundantRoutingMode_Object = MibScalar
manipulationAndRoutingRedundantRoutingMode = _ManipulationAndRoutingRedundantRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 8),
    _ManipulationAndRoutingRedundantRoutingMode_Type()
)
manipulationAndRoutingRedundantRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingRedundantRoutingMode.setStatus("current")


class _ManipulationAndRoutingAltRoutingTel2IpConnMethod_Type(Integer32):
    """Custom type manipulationAndRoutingAltRoutingTel2IpConnMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("options", 1),
          ("ping", 0))
    )


_ManipulationAndRoutingAltRoutingTel2IpConnMethod_Type.__name__ = "Integer32"
_ManipulationAndRoutingAltRoutingTel2IpConnMethod_Object = MibScalar
manipulationAndRoutingAltRoutingTel2IpConnMethod = _ManipulationAndRoutingAltRoutingTel2IpConnMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 9),
    _ManipulationAndRoutingAltRoutingTel2IpConnMethod_Type()
)
manipulationAndRoutingAltRoutingTel2IpConnMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingAltRoutingTel2IpConnMethod.setStatus("current")


class _ManipulationAndRoutingSIPReRoutingMode_Type(Integer32):
    """Custom type manipulationAndRoutingSIPReRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sendInviteToProxy", 1),
          ("standardMode", 0),
          ("useRoutingTable", 2))
    )


_ManipulationAndRoutingSIPReRoutingMode_Type.__name__ = "Integer32"
_ManipulationAndRoutingSIPReRoutingMode_Object = MibScalar
manipulationAndRoutingSIPReRoutingMode = _ManipulationAndRoutingSIPReRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 10),
    _ManipulationAndRoutingSIPReRoutingMode_Type()
)
manipulationAndRoutingSIPReRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingSIPReRoutingMode.setStatus("current")


class _ManipulationAndRoutingAltRoutingToneDuration_Type(Unsigned32):
    """Custom type manipulationAndRoutingAltRoutingToneDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_ManipulationAndRoutingAltRoutingToneDuration_Type.__name__ = "Unsigned32"
_ManipulationAndRoutingAltRoutingToneDuration_Object = MibScalar
manipulationAndRoutingAltRoutingToneDuration = _ManipulationAndRoutingAltRoutingToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 11),
    _ManipulationAndRoutingAltRoutingToneDuration_Type()
)
manipulationAndRoutingAltRoutingToneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingAltRoutingToneDuration.setStatus("current")


class _ManipulationAndRoutingAltRoutingTel2IpKeepAliveTime_Type(Unsigned32):
    """Custom type manipulationAndRoutingAltRoutingTel2IpKeepAliveTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2000000),
    )


_ManipulationAndRoutingAltRoutingTel2IpKeepAliveTime_Type.__name__ = "Unsigned32"
_ManipulationAndRoutingAltRoutingTel2IpKeepAliveTime_Object = MibScalar
manipulationAndRoutingAltRoutingTel2IpKeepAliveTime = _ManipulationAndRoutingAltRoutingTel2IpKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 12),
    _ManipulationAndRoutingAltRoutingTel2IpKeepAliveTime_Type()
)
manipulationAndRoutingAltRoutingTel2IpKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAndRoutingAltRoutingTel2IpKeepAliveTime.setStatus("current")
_Routing_ObjectIdentity = ObjectIdentity
routing = _Routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20)
)
_Tel2IPRoutingTable_Object = MibTable
tel2IPRoutingTable = _Tel2IPRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1)
)
if mibBuilder.loadTexts:
    tel2IPRoutingTable.setStatus("current")
_Tel2IPRoutingEntry_Object = MibTableRow
tel2IPRoutingEntry = _Tel2IPRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1)
)
tel2IPRoutingEntry.setIndexNames(
    (0, "AcGateway", "tel2IPRoutingIndex"),
)
if mibBuilder.loadTexts:
    tel2IPRoutingEntry.setStatus("current")


class _Tel2IPRoutingIndex_Type(Unsigned32):
    """Custom type tel2IPRoutingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_Tel2IPRoutingIndex_Type.__name__ = "Unsigned32"
_Tel2IPRoutingIndex_Object = MibTableColumn
tel2IPRoutingIndex = _Tel2IPRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 1),
    _Tel2IPRoutingIndex_Type()
)
tel2IPRoutingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tel2IPRoutingIndex.setStatus("current")
_Tel2IPRoutingRowStatus_Type = RowStatus
_Tel2IPRoutingRowStatus_Object = MibTableColumn
tel2IPRoutingRowStatus = _Tel2IPRoutingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 2),
    _Tel2IPRoutingRowStatus_Type()
)
tel2IPRoutingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingRowStatus.setStatus("current")


class _Tel2IPRoutingAction_Type(Integer32):
    """Custom type tel2IPRoutingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_Tel2IPRoutingAction_Type.__name__ = "Integer32"
_Tel2IPRoutingAction_Object = MibTableColumn
tel2IPRoutingAction = _Tel2IPRoutingAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 3),
    _Tel2IPRoutingAction_Type()
)
tel2IPRoutingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tel2IPRoutingAction.setStatus("current")


class _Tel2IPRoutingActionResult_Type(Integer32):
    """Custom type tel2IPRoutingActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_Tel2IPRoutingActionResult_Type.__name__ = "Integer32"
_Tel2IPRoutingActionResult_Object = MibTableColumn
tel2IPRoutingActionResult = _Tel2IPRoutingActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 4),
    _Tel2IPRoutingActionResult_Type()
)
tel2IPRoutingActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tel2IPRoutingActionResult.setStatus("current")


class _Tel2IPRoutingPrefix_Type(SnmpAdminString):
    """Custom type tel2IPRoutingPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Tel2IPRoutingPrefix_Type.__name__ = "SnmpAdminString"
_Tel2IPRoutingPrefix_Object = MibTableColumn
tel2IPRoutingPrefix = _Tel2IPRoutingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 5),
    _Tel2IPRoutingPrefix_Type()
)
tel2IPRoutingPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingPrefix.setStatus("current")


class _Tel2IPRoutingAddress_Type(SnmpAdminString):
    """Custom type tel2IPRoutingAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 69),
    )


_Tel2IPRoutingAddress_Type.__name__ = "SnmpAdminString"
_Tel2IPRoutingAddress_Object = MibTableColumn
tel2IPRoutingAddress = _Tel2IPRoutingAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 6),
    _Tel2IPRoutingAddress_Type()
)
tel2IPRoutingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingAddress.setStatus("current")


class _Tel2IPRoutingSrcPrefix_Type(SnmpAdminString):
    """Custom type tel2IPRoutingSrcPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Tel2IPRoutingSrcPrefix_Type.__name__ = "SnmpAdminString"
_Tel2IPRoutingSrcPrefix_Object = MibTableColumn
tel2IPRoutingSrcPrefix = _Tel2IPRoutingSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 7),
    _Tel2IPRoutingSrcPrefix_Type()
)
tel2IPRoutingSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingSrcPrefix.setStatus("current")


class _Tel2IPRoutingProfileID_Type(Integer32):
    """Custom type tel2IPRoutingProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_Tel2IPRoutingProfileID_Type.__name__ = "Integer32"
_Tel2IPRoutingProfileID_Object = MibTableColumn
tel2IPRoutingProfileID = _Tel2IPRoutingProfileID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 8),
    _Tel2IPRoutingProfileID_Type()
)
tel2IPRoutingProfileID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingProfileID.setStatus("current")


class _Tel2IPRoutingChargeCode_Type(Unsigned32):
    """Custom type tel2IPRoutingChargeCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Tel2IPRoutingChargeCode_Type.__name__ = "Unsigned32"
_Tel2IPRoutingChargeCode_Object = MibTableColumn
tel2IPRoutingChargeCode = _Tel2IPRoutingChargeCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 9),
    _Tel2IPRoutingChargeCode_Type()
)
tel2IPRoutingChargeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingChargeCode.setStatus("current")


class _Tel2IPRoutingDestPort_Type(Unsigned32):
    """Custom type tel2IPRoutingDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Tel2IPRoutingDestPort_Type.__name__ = "Unsigned32"
_Tel2IPRoutingDestPort_Object = MibTableColumn
tel2IPRoutingDestPort = _Tel2IPRoutingDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 10),
    _Tel2IPRoutingDestPort_Type()
)
tel2IPRoutingDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingDestPort.setStatus("current")


class _Tel2IPRoutingSourceIPGroupID_Type(Integer32):
    """Custom type tel2IPRoutingSourceIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_Tel2IPRoutingSourceIPGroupID_Type.__name__ = "Integer32"
_Tel2IPRoutingSourceIPGroupID_Object = MibTableColumn
tel2IPRoutingSourceIPGroupID = _Tel2IPRoutingSourceIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 11),
    _Tel2IPRoutingSourceIPGroupID_Type()
)
tel2IPRoutingSourceIPGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingSourceIPGroupID.setStatus("current")


class _Tel2IPRoutingDestHostPrefix_Type(SnmpAdminString):
    """Custom type tel2IPRoutingDestHostPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_Tel2IPRoutingDestHostPrefix_Type.__name__ = "SnmpAdminString"
_Tel2IPRoutingDestHostPrefix_Object = MibTableColumn
tel2IPRoutingDestHostPrefix = _Tel2IPRoutingDestHostPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 12),
    _Tel2IPRoutingDestHostPrefix_Type()
)
tel2IPRoutingDestHostPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingDestHostPrefix.setStatus("current")


class _Tel2IPRoutingDestIPGroupID_Type(Integer32):
    """Custom type tel2IPRoutingDestIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_Tel2IPRoutingDestIPGroupID_Type.__name__ = "Integer32"
_Tel2IPRoutingDestIPGroupID_Object = MibTableColumn
tel2IPRoutingDestIPGroupID = _Tel2IPRoutingDestIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 13),
    _Tel2IPRoutingDestIPGroupID_Type()
)
tel2IPRoutingDestIPGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingDestIPGroupID.setStatus("current")


class _Tel2IPRoutingSourceHostPrefix_Type(SnmpAdminString):
    """Custom type tel2IPRoutingSourceHostPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_Tel2IPRoutingSourceHostPrefix_Type.__name__ = "SnmpAdminString"
_Tel2IPRoutingSourceHostPrefix_Object = MibTableColumn
tel2IPRoutingSourceHostPrefix = _Tel2IPRoutingSourceHostPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 14),
    _Tel2IPRoutingSourceHostPrefix_Type()
)
tel2IPRoutingSourceHostPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingSourceHostPrefix.setStatus("current")


class _Tel2IPRoutingTransportType_Type(Integer32):
    """Custom type tel2IPRoutingTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", -1),
          ("tcp", 1),
          ("tls", 2),
          ("udp", 0))
    )


_Tel2IPRoutingTransportType_Type.__name__ = "Integer32"
_Tel2IPRoutingTransportType_Object = MibTableColumn
tel2IPRoutingTransportType = _Tel2IPRoutingTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 15),
    _Tel2IPRoutingTransportType_Type()
)
tel2IPRoutingTransportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingTransportType.setStatus("current")


class _Tel2IPRoutingSourceTrunkGroupID_Type(Integer32):
    """Custom type tel2IPRoutingSourceTrunkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99),
    )


_Tel2IPRoutingSourceTrunkGroupID_Type.__name__ = "Integer32"
_Tel2IPRoutingSourceTrunkGroupID_Object = MibTableColumn
tel2IPRoutingSourceTrunkGroupID = _Tel2IPRoutingSourceTrunkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 1, 1, 16),
    _Tel2IPRoutingSourceTrunkGroupID_Type()
)
tel2IPRoutingSourceTrunkGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tel2IPRoutingSourceTrunkGroupID.setStatus("current")
_IP2TelRoutingTable_Object = MibTable
iP2TelRoutingTable = _IP2TelRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2)
)
if mibBuilder.loadTexts:
    iP2TelRoutingTable.setStatus("current")
_IP2TelRoutingEntry_Object = MibTableRow
iP2TelRoutingEntry = _IP2TelRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1)
)
iP2TelRoutingEntry.setIndexNames(
    (0, "AcGateway", "iP2TelRoutingIndex"),
)
if mibBuilder.loadTexts:
    iP2TelRoutingEntry.setStatus("current")


class _IP2TelRoutingIndex_Type(Unsigned32):
    """Custom type iP2TelRoutingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 119),
    )


_IP2TelRoutingIndex_Type.__name__ = "Unsigned32"
_IP2TelRoutingIndex_Object = MibTableColumn
iP2TelRoutingIndex = _IP2TelRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 1),
    _IP2TelRoutingIndex_Type()
)
iP2TelRoutingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iP2TelRoutingIndex.setStatus("current")
_IP2TelRoutingRowStatus_Type = RowStatus
_IP2TelRoutingRowStatus_Object = MibTableColumn
iP2TelRoutingRowStatus = _IP2TelRoutingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 2),
    _IP2TelRoutingRowStatus_Type()
)
iP2TelRoutingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iP2TelRoutingRowStatus.setStatus("current")


class _IP2TelRoutingAction_Type(Integer32):
    """Custom type iP2TelRoutingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_IP2TelRoutingAction_Type.__name__ = "Integer32"
_IP2TelRoutingAction_Object = MibTableColumn
iP2TelRoutingAction = _IP2TelRoutingAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 3),
    _IP2TelRoutingAction_Type()
)
iP2TelRoutingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iP2TelRoutingAction.setStatus("current")


class _IP2TelRoutingActionResult_Type(Integer32):
    """Custom type iP2TelRoutingActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_IP2TelRoutingActionResult_Type.__name__ = "Integer32"
_IP2TelRoutingActionResult_Object = MibTableColumn
iP2TelRoutingActionResult = _IP2TelRoutingActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 4),
    _IP2TelRoutingActionResult_Type()
)
iP2TelRoutingActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iP2TelRoutingActionResult.setStatus("current")


class _IP2TelRoutingPrefix_Type(SnmpAdminString):
    """Custom type iP2TelRoutingPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IP2TelRoutingPrefix_Type.__name__ = "SnmpAdminString"
_IP2TelRoutingPrefix_Object = MibTableColumn
iP2TelRoutingPrefix = _IP2TelRoutingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 5),
    _IP2TelRoutingPrefix_Type()
)
iP2TelRoutingPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iP2TelRoutingPrefix.setStatus("current")


class _IP2TelRoutingTrunkGroupID_Type(Unsigned32):
    """Custom type iP2TelRoutingTrunkGroupID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_IP2TelRoutingTrunkGroupID_Type.__name__ = "Unsigned32"
_IP2TelRoutingTrunkGroupID_Object = MibTableColumn
iP2TelRoutingTrunkGroupID = _IP2TelRoutingTrunkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 6),
    _IP2TelRoutingTrunkGroupID_Type()
)
iP2TelRoutingTrunkGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iP2TelRoutingTrunkGroupID.setStatus("current")


class _IP2TelRoutingSrcPrefix_Type(SnmpAdminString):
    """Custom type iP2TelRoutingSrcPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_IP2TelRoutingSrcPrefix_Type.__name__ = "SnmpAdminString"
_IP2TelRoutingSrcPrefix_Object = MibTableColumn
iP2TelRoutingSrcPrefix = _IP2TelRoutingSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 7),
    _IP2TelRoutingSrcPrefix_Type()
)
iP2TelRoutingSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iP2TelRoutingSrcPrefix.setStatus("current")


class _IP2TelRoutingAddress_Type(SnmpAdminString):
    """Custom type iP2TelRoutingAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_IP2TelRoutingAddress_Type.__name__ = "SnmpAdminString"
_IP2TelRoutingAddress_Object = MibTableColumn
iP2TelRoutingAddress = _IP2TelRoutingAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 8),
    _IP2TelRoutingAddress_Type()
)
iP2TelRoutingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iP2TelRoutingAddress.setStatus("current")


class _IP2TelRoutingProfileID_Type(Unsigned32):
    """Custom type iP2TelRoutingProfileID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_IP2TelRoutingProfileID_Type.__name__ = "Unsigned32"
_IP2TelRoutingProfileID_Object = MibTableColumn
iP2TelRoutingProfileID = _IP2TelRoutingProfileID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 9),
    _IP2TelRoutingProfileID_Type()
)
iP2TelRoutingProfileID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iP2TelRoutingProfileID.setStatus("current")


class _IP2TelRoutingSourceIPGroupID_Type(Integer32):
    """Custom type iP2TelRoutingSourceIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_IP2TelRoutingSourceIPGroupID_Type.__name__ = "Integer32"
_IP2TelRoutingSourceIPGroupID_Object = MibTableColumn
iP2TelRoutingSourceIPGroupID = _IP2TelRoutingSourceIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 10),
    _IP2TelRoutingSourceIPGroupID_Type()
)
iP2TelRoutingSourceIPGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iP2TelRoutingSourceIPGroupID.setStatus("current")


class _IP2TelRoutingDestHostPrefix_Type(SnmpAdminString):
    """Custom type iP2TelRoutingDestHostPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_IP2TelRoutingDestHostPrefix_Type.__name__ = "SnmpAdminString"
_IP2TelRoutingDestHostPrefix_Object = MibTableColumn
iP2TelRoutingDestHostPrefix = _IP2TelRoutingDestHostPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 11),
    _IP2TelRoutingDestHostPrefix_Type()
)
iP2TelRoutingDestHostPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iP2TelRoutingDestHostPrefix.setStatus("current")


class _IP2TelRoutingSourceHostPrefix_Type(SnmpAdminString):
    """Custom type iP2TelRoutingSourceHostPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_IP2TelRoutingSourceHostPrefix_Type.__name__ = "SnmpAdminString"
_IP2TelRoutingSourceHostPrefix_Object = MibTableColumn
iP2TelRoutingSourceHostPrefix = _IP2TelRoutingSourceHostPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 2, 1, 12),
    _IP2TelRoutingSourceHostPrefix_Type()
)
iP2TelRoutingSourceHostPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iP2TelRoutingSourceHostPrefix.setStatus("current")
_DnsInfoTable_Object = MibTable
dnsInfoTable = _DnsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3)
)
if mibBuilder.loadTexts:
    dnsInfoTable.setStatus("current")
_DnsInfoEntry_Object = MibTableRow
dnsInfoEntry = _DnsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3, 1)
)
dnsInfoEntry.setIndexNames(
    (0, "AcGateway", "dnsInfoIndex"),
)
if mibBuilder.loadTexts:
    dnsInfoEntry.setStatus("current")


class _DnsInfoIndex_Type(Unsigned32):
    """Custom type dnsInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_DnsInfoIndex_Type.__name__ = "Unsigned32"
_DnsInfoIndex_Object = MibTableColumn
dnsInfoIndex = _DnsInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3, 1, 1),
    _DnsInfoIndex_Type()
)
dnsInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsInfoIndex.setStatus("current")
_DnsInfoRowStatus_Type = RowStatus
_DnsInfoRowStatus_Object = MibTableColumn
dnsInfoRowStatus = _DnsInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3, 1, 2),
    _DnsInfoRowStatus_Type()
)
dnsInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsInfoRowStatus.setStatus("current")


class _DnsInfoAction_Type(Integer32):
    """Custom type dnsInfoAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_DnsInfoAction_Type.__name__ = "Integer32"
_DnsInfoAction_Object = MibTableColumn
dnsInfoAction = _DnsInfoAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3, 1, 3),
    _DnsInfoAction_Type()
)
dnsInfoAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsInfoAction.setStatus("current")


class _DnsInfoActionResult_Type(Integer32):
    """Custom type dnsInfoActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_DnsInfoActionResult_Type.__name__ = "Integer32"
_DnsInfoActionResult_Object = MibTableColumn
dnsInfoActionResult = _DnsInfoActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3, 1, 4),
    _DnsInfoActionResult_Type()
)
dnsInfoActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsInfoActionResult.setStatus("current")


class _DnsInfoDomainName_Type(SnmpAdminString):
    """Custom type dnsInfoDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 69),
    )


_DnsInfoDomainName_Type.__name__ = "SnmpAdminString"
_DnsInfoDomainName_Object = MibTableColumn
dnsInfoDomainName = _DnsInfoDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3, 1, 5),
    _DnsInfoDomainName_Type()
)
dnsInfoDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsInfoDomainName.setStatus("current")


class _DnsInfoFirstIPAddress_Type(SnmpAdminString):
    """Custom type dnsInfoFirstIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DnsInfoFirstIPAddress_Type.__name__ = "SnmpAdminString"
_DnsInfoFirstIPAddress_Object = MibTableColumn
dnsInfoFirstIPAddress = _DnsInfoFirstIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3, 1, 6),
    _DnsInfoFirstIPAddress_Type()
)
dnsInfoFirstIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsInfoFirstIPAddress.setStatus("current")


class _DnsInfoSecondIPAddress_Type(SnmpAdminString):
    """Custom type dnsInfoSecondIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DnsInfoSecondIPAddress_Type.__name__ = "SnmpAdminString"
_DnsInfoSecondIPAddress_Object = MibTableColumn
dnsInfoSecondIPAddress = _DnsInfoSecondIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3, 1, 7),
    _DnsInfoSecondIPAddress_Type()
)
dnsInfoSecondIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsInfoSecondIPAddress.setStatus("current")


class _DnsInfoThirdIPAddress_Type(SnmpAdminString):
    """Custom type dnsInfoThirdIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DnsInfoThirdIPAddress_Type.__name__ = "SnmpAdminString"
_DnsInfoThirdIPAddress_Object = MibTableColumn
dnsInfoThirdIPAddress = _DnsInfoThirdIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3, 1, 8),
    _DnsInfoThirdIPAddress_Type()
)
dnsInfoThirdIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsInfoThirdIPAddress.setStatus("current")


class _DnsInfoFourthIPAddress_Type(SnmpAdminString):
    """Custom type dnsInfoFourthIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DnsInfoFourthIPAddress_Type.__name__ = "SnmpAdminString"
_DnsInfoFourthIPAddress_Object = MibTableColumn
dnsInfoFourthIPAddress = _DnsInfoFourthIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 3, 1, 9),
    _DnsInfoFourthIPAddress_Type()
)
dnsInfoFourthIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsInfoFourthIPAddress.setStatus("current")
_SrvInfoTable_Object = MibTable
srvInfoTable = _SrvInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4)
)
if mibBuilder.loadTexts:
    srvInfoTable.setStatus("current")
_SrvInfoEntry_Object = MibTableRow
srvInfoEntry = _SrvInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1)
)
srvInfoEntry.setIndexNames(
    (0, "AcGateway", "srvInfoIndex"),
)
if mibBuilder.loadTexts:
    srvInfoEntry.setStatus("current")


class _SrvInfoIndex_Type(Unsigned32):
    """Custom type srvInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_SrvInfoIndex_Type.__name__ = "Unsigned32"
_SrvInfoIndex_Object = MibTableColumn
srvInfoIndex = _SrvInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 1),
    _SrvInfoIndex_Type()
)
srvInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srvInfoIndex.setStatus("current")


class _SrvInfoRecordNum_Type(Unsigned32):
    """Custom type srvInfoRecordNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_SrvInfoRecordNum_Type.__name__ = "Unsigned32"
_SrvInfoRecordNum_Object = MibTableColumn
srvInfoRecordNum = _SrvInfoRecordNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 2),
    _SrvInfoRecordNum_Type()
)
srvInfoRecordNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srvInfoRecordNum.setStatus("current")
_SrvInfoRowStatus_Type = RowStatus
_SrvInfoRowStatus_Object = MibTableColumn
srvInfoRowStatus = _SrvInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 3),
    _SrvInfoRowStatus_Type()
)
srvInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoRowStatus.setStatus("current")


class _SrvInfoAction_Type(Integer32):
    """Custom type srvInfoAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SrvInfoAction_Type.__name__ = "Integer32"
_SrvInfoAction_Object = MibTableColumn
srvInfoAction = _SrvInfoAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 4),
    _SrvInfoAction_Type()
)
srvInfoAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvInfoAction.setStatus("current")


class _SrvInfoActionResult_Type(Integer32):
    """Custom type srvInfoActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SrvInfoActionResult_Type.__name__ = "Integer32"
_SrvInfoActionResult_Object = MibTableColumn
srvInfoActionResult = _SrvInfoActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 5),
    _SrvInfoActionResult_Type()
)
srvInfoActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srvInfoActionResult.setStatus("current")


class _SrvInfoInternalDomainName_Type(SnmpAdminString):
    """Custom type srvInfoInternalDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SrvInfoInternalDomainName_Type.__name__ = "SnmpAdminString"
_SrvInfoInternalDomainName_Object = MibTableColumn
srvInfoInternalDomainName = _SrvInfoInternalDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 6),
    _SrvInfoInternalDomainName_Type()
)
srvInfoInternalDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoInternalDomainName.setStatus("current")


class _SrvInfoTransportType_Type(Integer32):
    """Custom type srvInfoTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tCP", 1),
          ("tLS", 2),
          ("uDP", 0))
    )


_SrvInfoTransportType_Type.__name__ = "Integer32"
_SrvInfoTransportType_Object = MibTableColumn
srvInfoTransportType = _SrvInfoTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 7),
    _SrvInfoTransportType_Type()
)
srvInfoTransportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoTransportType.setStatus("current")


class _SrvInfoDNSName_Type(SnmpAdminString):
    """Custom type srvInfoDNSName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_SrvInfoDNSName_Type.__name__ = "SnmpAdminString"
_SrvInfoDNSName_Object = MibTableColumn
srvInfoDNSName = _SrvInfoDNSName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 8),
    _SrvInfoDNSName_Type()
)
srvInfoDNSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoDNSName.setStatus("current")


class _SrvInfoPriority_Type(Unsigned32):
    """Custom type srvInfoPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_SrvInfoPriority_Type.__name__ = "Unsigned32"
_SrvInfoPriority_Object = MibTableColumn
srvInfoPriority = _SrvInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 9),
    _SrvInfoPriority_Type()
)
srvInfoPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoPriority.setStatus("current")


class _SrvInfoWeight_Type(Unsigned32):
    """Custom type srvInfoWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_SrvInfoWeight_Type.__name__ = "Unsigned32"
_SrvInfoWeight_Object = MibTableColumn
srvInfoWeight = _SrvInfoWeight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 10),
    _SrvInfoWeight_Type()
)
srvInfoWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoWeight.setStatus("current")


class _SrvInfoPort_Type(Unsigned32):
    """Custom type srvInfoPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SrvInfoPort_Type.__name__ = "Unsigned32"
_SrvInfoPort_Object = MibTableColumn
srvInfoPort = _SrvInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 11),
    _SrvInfoPort_Type()
)
srvInfoPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoPort.setStatus("current")


class _SrvInfoDNSName2_Type(SnmpAdminString):
    """Custom type srvInfoDNSName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_SrvInfoDNSName2_Type.__name__ = "SnmpAdminString"
_SrvInfoDNSName2_Object = MibTableColumn
srvInfoDNSName2 = _SrvInfoDNSName2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 12),
    _SrvInfoDNSName2_Type()
)
srvInfoDNSName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoDNSName2.setStatus("current")


class _SrvInfoPriority2_Type(Unsigned32):
    """Custom type srvInfoPriority2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_SrvInfoPriority2_Type.__name__ = "Unsigned32"
_SrvInfoPriority2_Object = MibTableColumn
srvInfoPriority2 = _SrvInfoPriority2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 13),
    _SrvInfoPriority2_Type()
)
srvInfoPriority2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoPriority2.setStatus("current")


class _SrvInfoWeight2_Type(Unsigned32):
    """Custom type srvInfoWeight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_SrvInfoWeight2_Type.__name__ = "Unsigned32"
_SrvInfoWeight2_Object = MibTableColumn
srvInfoWeight2 = _SrvInfoWeight2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 14),
    _SrvInfoWeight2_Type()
)
srvInfoWeight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoWeight2.setStatus("current")


class _SrvInfoPort2_Type(Unsigned32):
    """Custom type srvInfoPort2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SrvInfoPort2_Type.__name__ = "Unsigned32"
_SrvInfoPort2_Object = MibTableColumn
srvInfoPort2 = _SrvInfoPort2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 15),
    _SrvInfoPort2_Type()
)
srvInfoPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoPort2.setStatus("current")


class _SrvInfoDNSName3_Type(SnmpAdminString):
    """Custom type srvInfoDNSName3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_SrvInfoDNSName3_Type.__name__ = "SnmpAdminString"
_SrvInfoDNSName3_Object = MibTableColumn
srvInfoDNSName3 = _SrvInfoDNSName3_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 16),
    _SrvInfoDNSName3_Type()
)
srvInfoDNSName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoDNSName3.setStatus("current")


class _SrvInfoPriority3_Type(Unsigned32):
    """Custom type srvInfoPriority3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_SrvInfoPriority3_Type.__name__ = "Unsigned32"
_SrvInfoPriority3_Object = MibTableColumn
srvInfoPriority3 = _SrvInfoPriority3_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 17),
    _SrvInfoPriority3_Type()
)
srvInfoPriority3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoPriority3.setStatus("current")


class _SrvInfoWeight3_Type(Unsigned32):
    """Custom type srvInfoWeight3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65000),
    )


_SrvInfoWeight3_Type.__name__ = "Unsigned32"
_SrvInfoWeight3_Object = MibTableColumn
srvInfoWeight3 = _SrvInfoWeight3_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 18),
    _SrvInfoWeight3_Type()
)
srvInfoWeight3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoWeight3.setStatus("current")


class _SrvInfoPort3_Type(Unsigned32):
    """Custom type srvInfoPort3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SrvInfoPort3_Type.__name__ = "Unsigned32"
_SrvInfoPort3_Object = MibTableColumn
srvInfoPort3 = _SrvInfoPort3_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 4, 1, 19),
    _SrvInfoPort3_Type()
)
srvInfoPort3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srvInfoPort3.setStatus("current")
_ForwardOnBusyTrunkDestTable_Object = MibTable
forwardOnBusyTrunkDestTable = _ForwardOnBusyTrunkDestTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 5)
)
if mibBuilder.loadTexts:
    forwardOnBusyTrunkDestTable.setStatus("current")
_ForwardOnBusyTrunkDestEntry_Object = MibTableRow
forwardOnBusyTrunkDestEntry = _ForwardOnBusyTrunkDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 5, 1)
)
forwardOnBusyTrunkDestEntry.setIndexNames(
    (0, "AcGateway", "forwardOnBusyTrunkDestIndex"),
)
if mibBuilder.loadTexts:
    forwardOnBusyTrunkDestEntry.setStatus("current")


class _ForwardOnBusyTrunkDestIndex_Type(Unsigned32):
    """Custom type forwardOnBusyTrunkDestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ForwardOnBusyTrunkDestIndex_Type.__name__ = "Unsigned32"
_ForwardOnBusyTrunkDestIndex_Object = MibTableColumn
forwardOnBusyTrunkDestIndex = _ForwardOnBusyTrunkDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 5, 1, 1),
    _ForwardOnBusyTrunkDestIndex_Type()
)
forwardOnBusyTrunkDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    forwardOnBusyTrunkDestIndex.setStatus("current")
_ForwardOnBusyTrunkDestRowStatus_Type = RowStatus
_ForwardOnBusyTrunkDestRowStatus_Object = MibTableColumn
forwardOnBusyTrunkDestRowStatus = _ForwardOnBusyTrunkDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 5, 1, 2),
    _ForwardOnBusyTrunkDestRowStatus_Type()
)
forwardOnBusyTrunkDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    forwardOnBusyTrunkDestRowStatus.setStatus("current")


class _ForwardOnBusyTrunkDestAction_Type(Integer32):
    """Custom type forwardOnBusyTrunkDestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ForwardOnBusyTrunkDestAction_Type.__name__ = "Integer32"
_ForwardOnBusyTrunkDestAction_Object = MibTableColumn
forwardOnBusyTrunkDestAction = _ForwardOnBusyTrunkDestAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 5, 1, 3),
    _ForwardOnBusyTrunkDestAction_Type()
)
forwardOnBusyTrunkDestAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardOnBusyTrunkDestAction.setStatus("current")


class _ForwardOnBusyTrunkDestActionResult_Type(Integer32):
    """Custom type forwardOnBusyTrunkDestActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ForwardOnBusyTrunkDestActionResult_Type.__name__ = "Integer32"
_ForwardOnBusyTrunkDestActionResult_Object = MibTableColumn
forwardOnBusyTrunkDestActionResult = _ForwardOnBusyTrunkDestActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 5, 1, 4),
    _ForwardOnBusyTrunkDestActionResult_Type()
)
forwardOnBusyTrunkDestActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardOnBusyTrunkDestActionResult.setStatus("current")


class _ForwardOnBusyTrunkDestTrunkGroupId_Type(Unsigned32):
    """Custom type forwardOnBusyTrunkDestTrunkGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_ForwardOnBusyTrunkDestTrunkGroupId_Type.__name__ = "Unsigned32"
_ForwardOnBusyTrunkDestTrunkGroupId_Object = MibTableColumn
forwardOnBusyTrunkDestTrunkGroupId = _ForwardOnBusyTrunkDestTrunkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 5, 1, 5),
    _ForwardOnBusyTrunkDestTrunkGroupId_Type()
)
forwardOnBusyTrunkDestTrunkGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    forwardOnBusyTrunkDestTrunkGroupId.setStatus("current")


class _ForwardOnBusyTrunkDestForwardDestination_Type(SnmpAdminString):
    """Custom type forwardOnBusyTrunkDestForwardDestination based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_ForwardOnBusyTrunkDestForwardDestination_Type.__name__ = "SnmpAdminString"
_ForwardOnBusyTrunkDestForwardDestination_Object = MibTableColumn
forwardOnBusyTrunkDestForwardDestination = _ForwardOnBusyTrunkDestForwardDestination_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 5, 1, 6),
    _ForwardOnBusyTrunkDestForwardDestination_Type()
)
forwardOnBusyTrunkDestForwardDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    forwardOnBusyTrunkDestForwardDestination.setStatus("current")
_AltRouteCause_ObjectIdentity = ObjectIdentity
altRouteCause = _AltRouteCause_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10)
)
_AltRouteCauseIP2TELTable_Object = MibTable
altRouteCauseIP2TELTable = _AltRouteCauseIP2TELTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 21)
)
if mibBuilder.loadTexts:
    altRouteCauseIP2TELTable.setStatus("current")
_AltRouteCauseIP2TELEntry_Object = MibTableRow
altRouteCauseIP2TELEntry = _AltRouteCauseIP2TELEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 21, 1)
)
altRouteCauseIP2TELEntry.setIndexNames(
    (0, "AcGateway", "altRouteCauseIP2TELIndex"),
)
if mibBuilder.loadTexts:
    altRouteCauseIP2TELEntry.setStatus("current")


class _AltRouteCauseIP2TELIndex_Type(Unsigned32):
    """Custom type altRouteCauseIP2TELIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AltRouteCauseIP2TELIndex_Type.__name__ = "Unsigned32"
_AltRouteCauseIP2TELIndex_Object = MibTableColumn
altRouteCauseIP2TELIndex = _AltRouteCauseIP2TELIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 21, 1, 1),
    _AltRouteCauseIP2TELIndex_Type()
)
altRouteCauseIP2TELIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    altRouteCauseIP2TELIndex.setStatus("current")
_AltRouteCauseIP2TELRowStatus_Type = RowStatus
_AltRouteCauseIP2TELRowStatus_Object = MibTableColumn
altRouteCauseIP2TELRowStatus = _AltRouteCauseIP2TELRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 21, 1, 2),
    _AltRouteCauseIP2TELRowStatus_Type()
)
altRouteCauseIP2TELRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    altRouteCauseIP2TELRowStatus.setStatus("current")


class _AltRouteCauseIP2TELAction_Type(Integer32):
    """Custom type altRouteCauseIP2TELAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_AltRouteCauseIP2TELAction_Type.__name__ = "Integer32"
_AltRouteCauseIP2TELAction_Object = MibTableColumn
altRouteCauseIP2TELAction = _AltRouteCauseIP2TELAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 21, 1, 3),
    _AltRouteCauseIP2TELAction_Type()
)
altRouteCauseIP2TELAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altRouteCauseIP2TELAction.setStatus("current")


class _AltRouteCauseIP2TELActionResult_Type(Integer32):
    """Custom type altRouteCauseIP2TELActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_AltRouteCauseIP2TELActionResult_Type.__name__ = "Integer32"
_AltRouteCauseIP2TELActionResult_Object = MibTableColumn
altRouteCauseIP2TELActionResult = _AltRouteCauseIP2TELActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 21, 1, 4),
    _AltRouteCauseIP2TELActionResult_Type()
)
altRouteCauseIP2TELActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altRouteCauseIP2TELActionResult.setStatus("current")


class _AltRouteCauseIP2TELReleaseCause_Type(Unsigned32):
    """Custom type altRouteCauseIP2TELReleaseCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 232),
    )


_AltRouteCauseIP2TELReleaseCause_Type.__name__ = "Unsigned32"
_AltRouteCauseIP2TELReleaseCause_Object = MibTableColumn
altRouteCauseIP2TELReleaseCause = _AltRouteCauseIP2TELReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 21, 1, 5),
    _AltRouteCauseIP2TELReleaseCause_Type()
)
altRouteCauseIP2TELReleaseCause.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    altRouteCauseIP2TELReleaseCause.setStatus("current")
_AltRouteCauseTEL2IPTable_Object = MibTable
altRouteCauseTEL2IPTable = _AltRouteCauseTEL2IPTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 22)
)
if mibBuilder.loadTexts:
    altRouteCauseTEL2IPTable.setStatus("current")
_AltRouteCauseTEL2IPEntry_Object = MibTableRow
altRouteCauseTEL2IPEntry = _AltRouteCauseTEL2IPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 22, 1)
)
altRouteCauseTEL2IPEntry.setIndexNames(
    (0, "AcGateway", "altRouteCauseTEL2IPIndex"),
)
if mibBuilder.loadTexts:
    altRouteCauseTEL2IPEntry.setStatus("current")


class _AltRouteCauseTEL2IPIndex_Type(Unsigned32):
    """Custom type altRouteCauseTEL2IPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AltRouteCauseTEL2IPIndex_Type.__name__ = "Unsigned32"
_AltRouteCauseTEL2IPIndex_Object = MibTableColumn
altRouteCauseTEL2IPIndex = _AltRouteCauseTEL2IPIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 22, 1, 1),
    _AltRouteCauseTEL2IPIndex_Type()
)
altRouteCauseTEL2IPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    altRouteCauseTEL2IPIndex.setStatus("current")
_AltRouteCauseTEL2IPRowStatus_Type = RowStatus
_AltRouteCauseTEL2IPRowStatus_Object = MibTableColumn
altRouteCauseTEL2IPRowStatus = _AltRouteCauseTEL2IPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 22, 1, 2),
    _AltRouteCauseTEL2IPRowStatus_Type()
)
altRouteCauseTEL2IPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    altRouteCauseTEL2IPRowStatus.setStatus("current")


class _AltRouteCauseTEL2IPAction_Type(Integer32):
    """Custom type altRouteCauseTEL2IPAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_AltRouteCauseTEL2IPAction_Type.__name__ = "Integer32"
_AltRouteCauseTEL2IPAction_Object = MibTableColumn
altRouteCauseTEL2IPAction = _AltRouteCauseTEL2IPAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 22, 1, 3),
    _AltRouteCauseTEL2IPAction_Type()
)
altRouteCauseTEL2IPAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altRouteCauseTEL2IPAction.setStatus("current")


class _AltRouteCauseTEL2IPActionResult_Type(Integer32):
    """Custom type altRouteCauseTEL2IPActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_AltRouteCauseTEL2IPActionResult_Type.__name__ = "Integer32"
_AltRouteCauseTEL2IPActionResult_Object = MibTableColumn
altRouteCauseTEL2IPActionResult = _AltRouteCauseTEL2IPActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 22, 1, 4),
    _AltRouteCauseTEL2IPActionResult_Type()
)
altRouteCauseTEL2IPActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altRouteCauseTEL2IPActionResult.setStatus("current")


class _AltRouteCauseTEL2IPReleaseCause_Type(Unsigned32):
    """Custom type altRouteCauseTEL2IPReleaseCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_AltRouteCauseTEL2IPReleaseCause_Type.__name__ = "Unsigned32"
_AltRouteCauseTEL2IPReleaseCause_Object = MibTableColumn
altRouteCauseTEL2IPReleaseCause = _AltRouteCauseTEL2IPReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 10, 22, 1, 5),
    _AltRouteCauseTEL2IPReleaseCause_Type()
)
altRouteCauseTEL2IPReleaseCause.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    altRouteCauseTEL2IPReleaseCause.setStatus("current")


class _RoutingEnableDigitDelivery2IP_Type(Integer32):
    """Custom type routingEnableDigitDelivery2IP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RoutingEnableDigitDelivery2IP_Type.__name__ = "Integer32"
_RoutingEnableDigitDelivery2IP_Object = MibScalar
routingEnableDigitDelivery2IP = _RoutingEnableDigitDelivery2IP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 21),
    _RoutingEnableDigitDelivery2IP_Type()
)
routingEnableDigitDelivery2IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingEnableDigitDelivery2IP.setStatus("current")


class _RoutingSourceIPAddressInput_Type(Integer32):
    """Custom type routingSourceIPAddressInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("layer3SourceIP", 1),
          ("notConfigured", -1),
          ("sIPContactHeader", 0))
    )


_RoutingSourceIPAddressInput_Type.__name__ = "Integer32"
_RoutingSourceIPAddressInput_Object = MibScalar
routingSourceIPAddressInput = _RoutingSourceIPAddressInput_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 20, 22),
    _RoutingSourceIPAddressInput_Type()
)
routingSourceIPAddressInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingSourceIPAddressInput.setStatus("current")
_Manipulation_ObjectIdentity = ObjectIdentity
manipulation = _Manipulation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21)
)


class _ManipulationRemovePrefix_Type(Integer32):
    """Custom type manipulationRemovePrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ManipulationRemovePrefix_Type.__name__ = "Integer32"
_ManipulationRemovePrefix_Object = MibScalar
manipulationRemovePrefix = _ManipulationRemovePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 1),
    _ManipulationRemovePrefix_Type()
)
manipulationRemovePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationRemovePrefix.setStatus("current")


class _ManipulationAddTrunkGroupAsPrefix_Type(Integer32):
    """Custom type manipulationAddTrunkGroupAsPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ManipulationAddTrunkGroupAsPrefix_Type.__name__ = "Integer32"
_ManipulationAddTrunkGroupAsPrefix_Object = MibScalar
manipulationAddTrunkGroupAsPrefix = _ManipulationAddTrunkGroupAsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 2),
    _ManipulationAddTrunkGroupAsPrefix_Type()
)
manipulationAddTrunkGroupAsPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAddTrunkGroupAsPrefix.setStatus("current")


class _ManipulationAddPortAsPrefix_Type(Integer32):
    """Custom type manipulationAddPortAsPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ManipulationAddPortAsPrefix_Type.__name__ = "Integer32"
_ManipulationAddPortAsPrefix_Object = MibScalar
manipulationAddPortAsPrefix = _ManipulationAddPortAsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 3),
    _ManipulationAddPortAsPrefix_Type()
)
manipulationAddPortAsPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAddPortAsPrefix.setStatus("current")


class _ManipulationReplaceEmptyDstWithPortNumber_Type(Integer32):
    """Custom type manipulationReplaceEmptyDstWithPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ManipulationReplaceEmptyDstWithPortNumber_Type.__name__ = "Integer32"
_ManipulationReplaceEmptyDstWithPortNumber_Object = MibScalar
manipulationReplaceEmptyDstWithPortNumber = _ManipulationReplaceEmptyDstWithPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 4),
    _ManipulationReplaceEmptyDstWithPortNumber_Type()
)
manipulationReplaceEmptyDstWithPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationReplaceEmptyDstWithPortNumber.setStatus("current")


class _ManipulationCIDNotification_Type(Integer32):
    """Custom type manipulationCIDNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ManipulationCIDNotification_Type.__name__ = "Integer32"
_ManipulationCIDNotification_Object = MibScalar
manipulationCIDNotification = _ManipulationCIDNotification_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 5),
    _ManipulationCIDNotification_Type()
)
manipulationCIDNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationCIDNotification.setStatus("current")


class _ManipulationUseSourceNumberAsDisplayName_Type(Integer32):
    """Custom type manipulationUseSourceNumberAsDisplayName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("overwrite", 2))
    )


_ManipulationUseSourceNumberAsDisplayName_Type.__name__ = "Integer32"
_ManipulationUseSourceNumberAsDisplayName_Object = MibScalar
manipulationUseSourceNumberAsDisplayName = _ManipulationUseSourceNumberAsDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 6),
    _ManipulationUseSourceNumberAsDisplayName_Type()
)
manipulationUseSourceNumberAsDisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationUseSourceNumberAsDisplayName.setStatus("current")


class _ManipulationAddNPIandTON2CalledNumber_Type(Integer32):
    """Custom type manipulationAddNPIandTON2CalledNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ManipulationAddNPIandTON2CalledNumber_Type.__name__ = "Integer32"
_ManipulationAddNPIandTON2CalledNumber_Object = MibScalar
manipulationAddNPIandTON2CalledNumber = _ManipulationAddNPIandTON2CalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 7),
    _ManipulationAddNPIandTON2CalledNumber_Type()
)
manipulationAddNPIandTON2CalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAddNPIandTON2CalledNumber.setStatus("current")


class _ManipulationAddNPIandTON2CallingNumber_Type(Integer32):
    """Custom type manipulationAddNPIandTON2CallingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ManipulationAddNPIandTON2CallingNumber_Type.__name__ = "Integer32"
_ManipulationAddNPIandTON2CallingNumber_Object = MibScalar
manipulationAddNPIandTON2CallingNumber = _ManipulationAddNPIandTON2CallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 8),
    _ManipulationAddNPIandTON2CallingNumber_Type()
)
manipulationAddNPIandTON2CallingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAddNPIandTON2CallingNumber.setStatus("current")


class _ManipulationUseDisplayNameAsSourceNumber_Type(Integer32):
    """Custom type manipulationUseDisplayNameAsSourceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ManipulationUseDisplayNameAsSourceNumber_Type.__name__ = "Integer32"
_ManipulationUseDisplayNameAsSourceNumber_Object = MibScalar
manipulationUseDisplayNameAsSourceNumber = _ManipulationUseDisplayNameAsSourceNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 9),
    _ManipulationUseDisplayNameAsSourceNumber_Type()
)
manipulationUseDisplayNameAsSourceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationUseDisplayNameAsSourceNumber.setStatus("current")


class _ManipulationAddPrefixToRedirectNumber_Type(SnmpAdminString):
    """Custom type manipulationAddPrefixToRedirectNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ManipulationAddPrefixToRedirectNumber_Type.__name__ = "SnmpAdminString"
_ManipulationAddPrefixToRedirectNumber_Object = MibScalar
manipulationAddPrefixToRedirectNumber = _ManipulationAddPrefixToRedirectNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 10),
    _ManipulationAddPrefixToRedirectNumber_Type()
)
manipulationAddPrefixToRedirectNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAddPrefixToRedirectNumber.setStatus("current")


class _ManipulationAddPhoneContextAsPrefix_Type(Integer32):
    """Custom type manipulationAddPhoneContextAsPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ManipulationAddPhoneContextAsPrefix_Type.__name__ = "Integer32"
_ManipulationAddPhoneContextAsPrefix_Object = MibScalar
manipulationAddPhoneContextAsPrefix = _ManipulationAddPhoneContextAsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 11),
    _ManipulationAddPhoneContextAsPrefix_Type()
)
manipulationAddPhoneContextAsPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAddPhoneContextAsPrefix.setStatus("current")


class _ManipulationBlindTransferAddPrefix_Type(Integer32):
    """Custom type manipulationBlindTransferAddPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ManipulationBlindTransferAddPrefix_Type.__name__ = "Integer32"
_ManipulationBlindTransferAddPrefix_Object = MibScalar
manipulationBlindTransferAddPrefix = _ManipulationBlindTransferAddPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 12),
    _ManipulationBlindTransferAddPrefix_Type()
)
manipulationBlindTransferAddPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationBlindTransferAddPrefix.setStatus("current")


class _ManipulationSourceMode_Type(Integer32):
    """Custom type manipulationSourceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fromAndPai", 0),
          ("fromOnly", 1))
    )


_ManipulationSourceMode_Type.__name__ = "Integer32"
_ManipulationSourceMode_Object = MibScalar
manipulationSourceMode = _ManipulationSourceMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 13),
    _ManipulationSourceMode_Type()
)
manipulationSourceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationSourceMode.setStatus("current")


class _ManipulationAddTrunkGroupAsPrefixToSource_Type(Integer32):
    """Custom type manipulationAddTrunkGroupAsPrefixToSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ManipulationAddTrunkGroupAsPrefixToSource_Type.__name__ = "Integer32"
_ManipulationAddTrunkGroupAsPrefixToSource_Object = MibScalar
manipulationAddTrunkGroupAsPrefixToSource = _ManipulationAddTrunkGroupAsPrefixToSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 14),
    _ManipulationAddTrunkGroupAsPrefixToSource_Type()
)
manipulationAddTrunkGroupAsPrefixToSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationAddTrunkGroupAsPrefixToSource.setStatus("current")


class _ManipulationSetTel2IpRedirectReason_Type(Integer32):
    """Custom type manipulationSetTel2IpRedirectReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              9,
              10,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("bust", 1),
          ("dTEOutOfOrder", 9),
          ("deflection", 4),
          ("forwardingDTE", 10),
          ("networkBusy", 3),
          ("noReply", 2),
          ("notConfigured", -1),
          ("pickUp", 14),
          ("systematicOrUnconditional", 15),
          ("transfer", 13),
          ("unknown", 0))
    )


_ManipulationSetTel2IpRedirectReason_Type.__name__ = "Integer32"
_ManipulationSetTel2IpRedirectReason_Object = MibScalar
manipulationSetTel2IpRedirectReason = _ManipulationSetTel2IpRedirectReason_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 15),
    _ManipulationSetTel2IpRedirectReason_Type()
)
manipulationSetTel2IpRedirectReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationSetTel2IpRedirectReason.setStatus("current")


class _ManipulationSetIp2TelRedirectReason_Type(Integer32):
    """Custom type manipulationSetIp2TelRedirectReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              9,
              10,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("bust", 1),
          ("dTEOutOfOrder", 9),
          ("deflection", 4),
          ("forwardingDTE", 10),
          ("networkBusy", 3),
          ("noReply", 2),
          ("notConfigured", -1),
          ("pickUp", 14),
          ("systematicOrUnconditional", 15),
          ("transfer", 13),
          ("unknown", 0))
    )


_ManipulationSetIp2TelRedirectReason_Type.__name__ = "Integer32"
_ManipulationSetIp2TelRedirectReason_Object = MibScalar
manipulationSetIp2TelRedirectReason = _ManipulationSetIp2TelRedirectReason_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 16),
    _ManipulationSetIp2TelRedirectReason_Type()
)
manipulationSetIp2TelRedirectReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationSetIp2TelRedirectReason.setStatus("current")


class _ManipulationSetIp2TelRedirectScreeningIndicator_Type(Integer32):
    """Custom type manipulationSetIp2TelRedirectScreeningIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkProvided", 3),
          ("notConfigured", -1),
          ("userFailed", 2),
          ("userPassed", 1),
          ("userProvided", 0))
    )


_ManipulationSetIp2TelRedirectScreeningIndicator_Type.__name__ = "Integer32"
_ManipulationSetIp2TelRedirectScreeningIndicator_Object = MibScalar
manipulationSetIp2TelRedirectScreeningIndicator = _ManipulationSetIp2TelRedirectScreeningIndicator_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 17),
    _ManipulationSetIp2TelRedirectScreeningIndicator_Type()
)
manipulationSetIp2TelRedirectScreeningIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    manipulationSetIp2TelRedirectScreeningIndicator.setStatus("current")
_DstIP2TELTable_Object = MibTable
dstIP2TELTable = _DstIP2TELTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21)
)
if mibBuilder.loadTexts:
    dstIP2TELTable.setStatus("current")
_DstIP2TELEntry_Object = MibTableRow
dstIP2TELEntry = _DstIP2TELEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1)
)
dstIP2TELEntry.setIndexNames(
    (0, "AcGateway", "dstIP2TELIndex"),
)
if mibBuilder.loadTexts:
    dstIP2TELEntry.setStatus("current")


class _DstIP2TELIndex_Type(Unsigned32):
    """Custom type dstIP2TELIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DstIP2TELIndex_Type.__name__ = "Unsigned32"
_DstIP2TELIndex_Object = MibTableColumn
dstIP2TELIndex = _DstIP2TELIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 1),
    _DstIP2TELIndex_Type()
)
dstIP2TELIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dstIP2TELIndex.setStatus("current")
_DstIP2TELRowStatus_Type = RowStatus
_DstIP2TELRowStatus_Object = MibTableColumn
dstIP2TELRowStatus = _DstIP2TELRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 2),
    _DstIP2TELRowStatus_Type()
)
dstIP2TELRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELRowStatus.setStatus("current")


class _DstIP2TELAction_Type(Integer32):
    """Custom type dstIP2TELAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_DstIP2TELAction_Type.__name__ = "Integer32"
_DstIP2TELAction_Object = MibTableColumn
dstIP2TELAction = _DstIP2TELAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 3),
    _DstIP2TELAction_Type()
)
dstIP2TELAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstIP2TELAction.setStatus("current")


class _DstIP2TELActionResult_Type(Integer32):
    """Custom type dstIP2TELActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_DstIP2TELActionResult_Type.__name__ = "Integer32"
_DstIP2TELActionResult_Object = MibTableColumn
dstIP2TELActionResult = _DstIP2TELActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 4),
    _DstIP2TELActionResult_Type()
)
dstIP2TELActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstIP2TELActionResult.setStatus("current")


class _DstIP2TELPrefix_Type(SnmpAdminString):
    """Custom type dstIP2TELPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_DstIP2TELPrefix_Type.__name__ = "SnmpAdminString"
_DstIP2TELPrefix_Object = MibTableColumn
dstIP2TELPrefix = _DstIP2TELPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 5),
    _DstIP2TELPrefix_Type()
)
dstIP2TELPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELPrefix.setStatus("current")


class _DstIP2TELNumOfStrippedDigits_Type(Unsigned32):
    """Custom type dstIP2TELNumOfStrippedDigits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_DstIP2TELNumOfStrippedDigits_Type.__name__ = "Unsigned32"
_DstIP2TELNumOfStrippedDigits_Object = MibTableColumn
dstIP2TELNumOfStrippedDigits = _DstIP2TELNumOfStrippedDigits_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 6),
    _DstIP2TELNumOfStrippedDigits_Type()
)
dstIP2TELNumOfStrippedDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELNumOfStrippedDigits.setStatus("current")


class _DstIP2TELPrefixToAdd_Type(SnmpAdminString):
    """Custom type dstIP2TELPrefixToAdd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_DstIP2TELPrefixToAdd_Type.__name__ = "SnmpAdminString"
_DstIP2TELPrefixToAdd_Object = MibTableColumn
dstIP2TELPrefixToAdd = _DstIP2TELPrefixToAdd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 7),
    _DstIP2TELPrefixToAdd_Type()
)
dstIP2TELPrefixToAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELPrefixToAdd.setStatus("current")


class _DstIP2TELNumOfDigitsToLeave_Type(Unsigned32):
    """Custom type dstIP2TELNumOfDigitsToLeave based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DstIP2TELNumOfDigitsToLeave_Type.__name__ = "Unsigned32"
_DstIP2TELNumOfDigitsToLeave_Object = MibTableColumn
dstIP2TELNumOfDigitsToLeave = _DstIP2TELNumOfDigitsToLeave_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 8),
    _DstIP2TELNumOfDigitsToLeave_Type()
)
dstIP2TELNumOfDigitsToLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELNumOfDigitsToLeave.setStatus("current")


class _DstIP2TELNumberPlan_Type(Integer32):
    """Custom type dstIP2TELNumberPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e164Public", 1),
          ("notConfigured", 255),
          ("private", 9),
          ("unknown", 0))
    )


_DstIP2TELNumberPlan_Type.__name__ = "Integer32"
_DstIP2TELNumberPlan_Object = MibTableColumn
dstIP2TELNumberPlan = _DstIP2TELNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 9),
    _DstIP2TELNumberPlan_Type()
)
dstIP2TELNumberPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELNumberPlan.setStatus("current")


class _DstIP2TELNumberType_Type(Integer32):
    """Custom type dstIP2TELNumberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 6),
          ("international-Level2Regional", 1),
          ("national-Level1Regional", 2),
          ("networkSpecific-NetworkPISN", 3),
          ("notConfigured", 255),
          ("subscriber-Level0Regional", 4),
          ("unknown", 0))
    )


_DstIP2TELNumberType_Type.__name__ = "Integer32"
_DstIP2TELNumberType_Object = MibTableColumn
dstIP2TELNumberType = _DstIP2TELNumberType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 10),
    _DstIP2TELNumberType_Type()
)
dstIP2TELNumberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELNumberType.setStatus("current")


class _DstIP2TELSourcePrefix_Type(SnmpAdminString):
    """Custom type dstIP2TELSourcePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_DstIP2TELSourcePrefix_Type.__name__ = "SnmpAdminString"
_DstIP2TELSourcePrefix_Object = MibTableColumn
dstIP2TELSourcePrefix = _DstIP2TELSourcePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 11),
    _DstIP2TELSourcePrefix_Type()
)
dstIP2TELSourcePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELSourcePrefix.setStatus("current")


class _DstIP2TELSourceIP_Type(SnmpAdminString):
    """Custom type dstIP2TELSourceIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DstIP2TELSourceIP_Type.__name__ = "SnmpAdminString"
_DstIP2TELSourceIP_Object = MibTableColumn
dstIP2TELSourceIP = _DstIP2TELSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 12),
    _DstIP2TELSourceIP_Type()
)
dstIP2TELSourceIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELSourceIP.setStatus("current")


class _DstIP2TELNumOfDigitsToRemFromRight_Type(Unsigned32):
    """Custom type dstIP2TELNumOfDigitsToRemFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_DstIP2TELNumOfDigitsToRemFromRight_Type.__name__ = "Unsigned32"
_DstIP2TELNumOfDigitsToRemFromRight_Object = MibTableColumn
dstIP2TELNumOfDigitsToRemFromRight = _DstIP2TELNumOfDigitsToRemFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 13),
    _DstIP2TELNumOfDigitsToRemFromRight_Type()
)
dstIP2TELNumOfDigitsToRemFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELNumOfDigitsToRemFromRight.setStatus("current")


class _DstIP2TELSuffix2Add_Type(SnmpAdminString):
    """Custom type dstIP2TELSuffix2Add based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_DstIP2TELSuffix2Add_Type.__name__ = "SnmpAdminString"
_DstIP2TELSuffix2Add_Object = MibTableColumn
dstIP2TELSuffix2Add = _DstIP2TELSuffix2Add_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 14),
    _DstIP2TELSuffix2Add_Type()
)
dstIP2TELSuffix2Add.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELSuffix2Add.setStatus("current")


class _DstIP2TELIsPresentationRestricted_Type(Unsigned32):
    """Custom type dstIP2TELIsPresentationRestricted based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DstIP2TELIsPresentationRestricted_Type.__name__ = "Unsigned32"
_DstIP2TELIsPresentationRestricted_Object = MibTableColumn
dstIP2TELIsPresentationRestricted = _DstIP2TELIsPresentationRestricted_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 21, 1, 15),
    _DstIP2TELIsPresentationRestricted_Type()
)
dstIP2TELIsPresentationRestricted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstIP2TELIsPresentationRestricted.setStatus("current")
_DstTEL2IPTable_Object = MibTable
dstTEL2IPTable = _DstTEL2IPTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22)
)
if mibBuilder.loadTexts:
    dstTEL2IPTable.setStatus("current")
_DstTEL2IPEntry_Object = MibTableRow
dstTEL2IPEntry = _DstTEL2IPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1)
)
dstTEL2IPEntry.setIndexNames(
    (0, "AcGateway", "dstTEL2IPIndex"),
)
if mibBuilder.loadTexts:
    dstTEL2IPEntry.setStatus("current")


class _DstTEL2IPIndex_Type(Unsigned32):
    """Custom type dstTEL2IPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 119),
    )


_DstTEL2IPIndex_Type.__name__ = "Unsigned32"
_DstTEL2IPIndex_Object = MibTableColumn
dstTEL2IPIndex = _DstTEL2IPIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 1),
    _DstTEL2IPIndex_Type()
)
dstTEL2IPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dstTEL2IPIndex.setStatus("current")
_DstTEL2IPRowStatus_Type = RowStatus
_DstTEL2IPRowStatus_Object = MibTableColumn
dstTEL2IPRowStatus = _DstTEL2IPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 2),
    _DstTEL2IPRowStatus_Type()
)
dstTEL2IPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPRowStatus.setStatus("current")


class _DstTEL2IPAction_Type(Integer32):
    """Custom type dstTEL2IPAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_DstTEL2IPAction_Type.__name__ = "Integer32"
_DstTEL2IPAction_Object = MibTableColumn
dstTEL2IPAction = _DstTEL2IPAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 3),
    _DstTEL2IPAction_Type()
)
dstTEL2IPAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstTEL2IPAction.setStatus("current")


class _DstTEL2IPActionResult_Type(Integer32):
    """Custom type dstTEL2IPActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_DstTEL2IPActionResult_Type.__name__ = "Integer32"
_DstTEL2IPActionResult_Object = MibTableColumn
dstTEL2IPActionResult = _DstTEL2IPActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 4),
    _DstTEL2IPActionResult_Type()
)
dstTEL2IPActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstTEL2IPActionResult.setStatus("current")


class _DstTEL2IPPrefix_Type(SnmpAdminString):
    """Custom type dstTEL2IPPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_DstTEL2IPPrefix_Type.__name__ = "SnmpAdminString"
_DstTEL2IPPrefix_Object = MibTableColumn
dstTEL2IPPrefix = _DstTEL2IPPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 5),
    _DstTEL2IPPrefix_Type()
)
dstTEL2IPPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPPrefix.setStatus("current")


class _DstTEL2IPNumOfStrippedDigits_Type(Unsigned32):
    """Custom type dstTEL2IPNumOfStrippedDigits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_DstTEL2IPNumOfStrippedDigits_Type.__name__ = "Unsigned32"
_DstTEL2IPNumOfStrippedDigits_Object = MibTableColumn
dstTEL2IPNumOfStrippedDigits = _DstTEL2IPNumOfStrippedDigits_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 6),
    _DstTEL2IPNumOfStrippedDigits_Type()
)
dstTEL2IPNumOfStrippedDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPNumOfStrippedDigits.setStatus("current")


class _DstTEL2IPPrefixToAdd_Type(SnmpAdminString):
    """Custom type dstTEL2IPPrefixToAdd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_DstTEL2IPPrefixToAdd_Type.__name__ = "SnmpAdminString"
_DstTEL2IPPrefixToAdd_Object = MibTableColumn
dstTEL2IPPrefixToAdd = _DstTEL2IPPrefixToAdd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 7),
    _DstTEL2IPPrefixToAdd_Type()
)
dstTEL2IPPrefixToAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPPrefixToAdd.setStatus("current")


class _DstTEL2IPNumOfDigitsToLeave_Type(Unsigned32):
    """Custom type dstTEL2IPNumOfDigitsToLeave based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DstTEL2IPNumOfDigitsToLeave_Type.__name__ = "Unsigned32"
_DstTEL2IPNumOfDigitsToLeave_Object = MibTableColumn
dstTEL2IPNumOfDigitsToLeave = _DstTEL2IPNumOfDigitsToLeave_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 8),
    _DstTEL2IPNumOfDigitsToLeave_Type()
)
dstTEL2IPNumOfDigitsToLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPNumOfDigitsToLeave.setStatus("current")


class _DstTEL2IPNumberPlan_Type(Integer32):
    """Custom type dstTEL2IPNumberPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e164Public", 1),
          ("notConfigured", 255),
          ("private", 9),
          ("unknown", 0))
    )


_DstTEL2IPNumberPlan_Type.__name__ = "Integer32"
_DstTEL2IPNumberPlan_Object = MibTableColumn
dstTEL2IPNumberPlan = _DstTEL2IPNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 9),
    _DstTEL2IPNumberPlan_Type()
)
dstTEL2IPNumberPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPNumberPlan.setStatus("current")


class _DstTEL2IPNumberType_Type(Integer32):
    """Custom type dstTEL2IPNumberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 6),
          ("international-Level2Regional", 1),
          ("national-Level1Regional", 2),
          ("networkSpecific-NetworkPISN", 3),
          ("notConfigured", 255),
          ("subscriber-Level0Regional", 4),
          ("unknown", 0))
    )


_DstTEL2IPNumberType_Type.__name__ = "Integer32"
_DstTEL2IPNumberType_Object = MibTableColumn
dstTEL2IPNumberType = _DstTEL2IPNumberType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 10),
    _DstTEL2IPNumberType_Type()
)
dstTEL2IPNumberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPNumberType.setStatus("current")


class _DstTEL2IPSourcePrefix_Type(SnmpAdminString):
    """Custom type dstTEL2IPSourcePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_DstTEL2IPSourcePrefix_Type.__name__ = "SnmpAdminString"
_DstTEL2IPSourcePrefix_Object = MibTableColumn
dstTEL2IPSourcePrefix = _DstTEL2IPSourcePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 11),
    _DstTEL2IPSourcePrefix_Type()
)
dstTEL2IPSourcePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPSourcePrefix.setStatus("current")


class _DstTEL2IPNumOfDigitsToRemFromRight_Type(Unsigned32):
    """Custom type dstTEL2IPNumOfDigitsToRemFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_DstTEL2IPNumOfDigitsToRemFromRight_Type.__name__ = "Unsigned32"
_DstTEL2IPNumOfDigitsToRemFromRight_Object = MibTableColumn
dstTEL2IPNumOfDigitsToRemFromRight = _DstTEL2IPNumOfDigitsToRemFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 12),
    _DstTEL2IPNumOfDigitsToRemFromRight_Type()
)
dstTEL2IPNumOfDigitsToRemFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPNumOfDigitsToRemFromRight.setStatus("current")


class _DstTEL2IPSuffix2Add_Type(SnmpAdminString):
    """Custom type dstTEL2IPSuffix2Add based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_DstTEL2IPSuffix2Add_Type.__name__ = "SnmpAdminString"
_DstTEL2IPSuffix2Add_Object = MibTableColumn
dstTEL2IPSuffix2Add = _DstTEL2IPSuffix2Add_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 13),
    _DstTEL2IPSuffix2Add_Type()
)
dstTEL2IPSuffix2Add.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPSuffix2Add.setStatus("current")


class _DstTEL2IPIsPresentationRestricted_Type(Unsigned32):
    """Custom type dstTEL2IPIsPresentationRestricted based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DstTEL2IPIsPresentationRestricted_Type.__name__ = "Unsigned32"
_DstTEL2IPIsPresentationRestricted_Object = MibTableColumn
dstTEL2IPIsPresentationRestricted = _DstTEL2IPIsPresentationRestricted_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 14),
    _DstTEL2IPIsPresentationRestricted_Type()
)
dstTEL2IPIsPresentationRestricted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPIsPresentationRestricted.setStatus("current")


class _DstTEL2IPSourceIPAddress_Type(SnmpAdminString):
    """Custom type dstTEL2IPSourceIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DstTEL2IPSourceIPAddress_Type.__name__ = "SnmpAdminString"
_DstTEL2IPSourceIPAddress_Object = MibTableColumn
dstTEL2IPSourceIPAddress = _DstTEL2IPSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 15),
    _DstTEL2IPSourceIPAddress_Type()
)
dstTEL2IPSourceIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPSourceIPAddress.setStatus("current")


class _DstTEL2IPSourceTrunkGroupID_Type(Integer32):
    """Custom type dstTEL2IPSourceTrunkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99),
    )


_DstTEL2IPSourceTrunkGroupID_Type.__name__ = "Integer32"
_DstTEL2IPSourceTrunkGroupID_Object = MibTableColumn
dstTEL2IPSourceTrunkGroupID = _DstTEL2IPSourceTrunkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 16),
    _DstTEL2IPSourceTrunkGroupID_Type()
)
dstTEL2IPSourceTrunkGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPSourceTrunkGroupID.setStatus("current")


class _DstTEL2IPSourceIPGroupID_Type(Integer32):
    """Custom type dstTEL2IPSourceIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8),
    )


_DstTEL2IPSourceIPGroupID_Type.__name__ = "Integer32"
_DstTEL2IPSourceIPGroupID_Object = MibTableColumn
dstTEL2IPSourceIPGroupID = _DstTEL2IPSourceIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 22, 1, 17),
    _DstTEL2IPSourceIPGroupID_Type()
)
dstTEL2IPSourceIPGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dstTEL2IPSourceIPGroupID.setStatus("current")
_SrcIP2TELTable_Object = MibTable
srcIP2TELTable = _SrcIP2TELTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23)
)
if mibBuilder.loadTexts:
    srcIP2TELTable.setStatus("current")
_SrcIP2TELEntry_Object = MibTableRow
srcIP2TELEntry = _SrcIP2TELEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1)
)
srcIP2TELEntry.setIndexNames(
    (0, "AcGateway", "srcIP2TELIndex"),
)
if mibBuilder.loadTexts:
    srcIP2TELEntry.setStatus("current")


class _SrcIP2TELIndex_Type(Unsigned32):
    """Custom type srcIP2TELIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_SrcIP2TELIndex_Type.__name__ = "Unsigned32"
_SrcIP2TELIndex_Object = MibTableColumn
srcIP2TELIndex = _SrcIP2TELIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 1),
    _SrcIP2TELIndex_Type()
)
srcIP2TELIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srcIP2TELIndex.setStatus("current")
_SrcIP2TELRowStatus_Type = RowStatus
_SrcIP2TELRowStatus_Object = MibTableColumn
srcIP2TELRowStatus = _SrcIP2TELRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 2),
    _SrcIP2TELRowStatus_Type()
)
srcIP2TELRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELRowStatus.setStatus("current")


class _SrcIP2TELAction_Type(Integer32):
    """Custom type srcIP2TELAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SrcIP2TELAction_Type.__name__ = "Integer32"
_SrcIP2TELAction_Object = MibTableColumn
srcIP2TELAction = _SrcIP2TELAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 3),
    _SrcIP2TELAction_Type()
)
srcIP2TELAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcIP2TELAction.setStatus("current")


class _SrcIP2TELActionResult_Type(Integer32):
    """Custom type srcIP2TELActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SrcIP2TELActionResult_Type.__name__ = "Integer32"
_SrcIP2TELActionResult_Object = MibTableColumn
srcIP2TELActionResult = _SrcIP2TELActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 4),
    _SrcIP2TELActionResult_Type()
)
srcIP2TELActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcIP2TELActionResult.setStatus("current")


class _SrcIP2TELPrefix_Type(SnmpAdminString):
    """Custom type srcIP2TELPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SrcIP2TELPrefix_Type.__name__ = "SnmpAdminString"
_SrcIP2TELPrefix_Object = MibTableColumn
srcIP2TELPrefix = _SrcIP2TELPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 5),
    _SrcIP2TELPrefix_Type()
)
srcIP2TELPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELPrefix.setStatus("current")


class _SrcIP2TELNumOfStrippedDigits_Type(Unsigned32):
    """Custom type srcIP2TELNumOfStrippedDigits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_SrcIP2TELNumOfStrippedDigits_Type.__name__ = "Unsigned32"
_SrcIP2TELNumOfStrippedDigits_Object = MibTableColumn
srcIP2TELNumOfStrippedDigits = _SrcIP2TELNumOfStrippedDigits_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 6),
    _SrcIP2TELNumOfStrippedDigits_Type()
)
srcIP2TELNumOfStrippedDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELNumOfStrippedDigits.setStatus("current")


class _SrcIP2TELPrefixToAdd_Type(SnmpAdminString):
    """Custom type srcIP2TELPrefixToAdd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SrcIP2TELPrefixToAdd_Type.__name__ = "SnmpAdminString"
_SrcIP2TELPrefixToAdd_Object = MibTableColumn
srcIP2TELPrefixToAdd = _SrcIP2TELPrefixToAdd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 7),
    _SrcIP2TELPrefixToAdd_Type()
)
srcIP2TELPrefixToAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELPrefixToAdd.setStatus("current")


class _SrcIP2TELNumOfDigitsToLeave_Type(Unsigned32):
    """Custom type srcIP2TELNumOfDigitsToLeave based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SrcIP2TELNumOfDigitsToLeave_Type.__name__ = "Unsigned32"
_SrcIP2TELNumOfDigitsToLeave_Object = MibTableColumn
srcIP2TELNumOfDigitsToLeave = _SrcIP2TELNumOfDigitsToLeave_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 8),
    _SrcIP2TELNumOfDigitsToLeave_Type()
)
srcIP2TELNumOfDigitsToLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELNumOfDigitsToLeave.setStatus("current")


class _SrcIP2TELNumberPlan_Type(Integer32):
    """Custom type srcIP2TELNumberPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e164Public", 1),
          ("notConfigured", 255),
          ("private", 9),
          ("unknown", 0))
    )


_SrcIP2TELNumberPlan_Type.__name__ = "Integer32"
_SrcIP2TELNumberPlan_Object = MibTableColumn
srcIP2TELNumberPlan = _SrcIP2TELNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 9),
    _SrcIP2TELNumberPlan_Type()
)
srcIP2TELNumberPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELNumberPlan.setStatus("current")


class _SrcIP2TELNumberType_Type(Integer32):
    """Custom type srcIP2TELNumberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 6),
          ("international-Level2Regional", 1),
          ("national-Level1Regional", 2),
          ("networkSpecific-NetworkPISN", 3),
          ("notConfigured", 255),
          ("subscriber-Level0Regional", 4),
          ("unknown", 0))
    )


_SrcIP2TELNumberType_Type.__name__ = "Integer32"
_SrcIP2TELNumberType_Object = MibTableColumn
srcIP2TELNumberType = _SrcIP2TELNumberType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 10),
    _SrcIP2TELNumberType_Type()
)
srcIP2TELNumberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELNumberType.setStatus("current")


class _SrcIP2TELDestPrefix_Type(SnmpAdminString):
    """Custom type srcIP2TELDestPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SrcIP2TELDestPrefix_Type.__name__ = "SnmpAdminString"
_SrcIP2TELDestPrefix_Object = MibTableColumn
srcIP2TELDestPrefix = _SrcIP2TELDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 11),
    _SrcIP2TELDestPrefix_Type()
)
srcIP2TELDestPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELDestPrefix.setStatus("current")


class _SrcIP2TELPresentation_Type(Integer32):
    """Custom type srcIP2TELPresentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("notBlocked", 0),
          ("notConfigured", 255))
    )


_SrcIP2TELPresentation_Type.__name__ = "Integer32"
_SrcIP2TELPresentation_Object = MibTableColumn
srcIP2TELPresentation = _SrcIP2TELPresentation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 12),
    _SrcIP2TELPresentation_Type()
)
srcIP2TELPresentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELPresentation.setStatus("current")


class _SrcIP2TELNumOfDigitsToRemFromRight_Type(Unsigned32):
    """Custom type srcIP2TELNumOfDigitsToRemFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_SrcIP2TELNumOfDigitsToRemFromRight_Type.__name__ = "Unsigned32"
_SrcIP2TELNumOfDigitsToRemFromRight_Object = MibTableColumn
srcIP2TELNumOfDigitsToRemFromRight = _SrcIP2TELNumOfDigitsToRemFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 13),
    _SrcIP2TELNumOfDigitsToRemFromRight_Type()
)
srcIP2TELNumOfDigitsToRemFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELNumOfDigitsToRemFromRight.setStatus("current")


class _SrcIP2TELSuffix2Add_Type(SnmpAdminString):
    """Custom type srcIP2TELSuffix2Add based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SrcIP2TELSuffix2Add_Type.__name__ = "SnmpAdminString"
_SrcIP2TELSuffix2Add_Object = MibTableColumn
srcIP2TELSuffix2Add = _SrcIP2TELSuffix2Add_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 14),
    _SrcIP2TELSuffix2Add_Type()
)
srcIP2TELSuffix2Add.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELSuffix2Add.setStatus("current")


class _SrcIP2TELSourceIPAddress_Type(SnmpAdminString):
    """Custom type srcIP2TELSourceIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SrcIP2TELSourceIPAddress_Type.__name__ = "SnmpAdminString"
_SrcIP2TELSourceIPAddress_Object = MibTableColumn
srcIP2TELSourceIPAddress = _SrcIP2TELSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 23, 1, 15),
    _SrcIP2TELSourceIPAddress_Type()
)
srcIP2TELSourceIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcIP2TELSourceIPAddress.setStatus("current")
_SrcTEL2IPTable_Object = MibTable
srcTEL2IPTable = _SrcTEL2IPTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24)
)
if mibBuilder.loadTexts:
    srcTEL2IPTable.setStatus("current")
_SrcTEL2IPEntry_Object = MibTableRow
srcTEL2IPEntry = _SrcTEL2IPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1)
)
srcTEL2IPEntry.setIndexNames(
    (0, "AcGateway", "srcTEL2IPIndex"),
)
if mibBuilder.loadTexts:
    srcTEL2IPEntry.setStatus("current")


class _SrcTEL2IPIndex_Type(Unsigned32):
    """Custom type srcTEL2IPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 119),
    )


_SrcTEL2IPIndex_Type.__name__ = "Unsigned32"
_SrcTEL2IPIndex_Object = MibTableColumn
srcTEL2IPIndex = _SrcTEL2IPIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 1),
    _SrcTEL2IPIndex_Type()
)
srcTEL2IPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    srcTEL2IPIndex.setStatus("current")
_SrcTEL2IPRowStatus_Type = RowStatus
_SrcTEL2IPRowStatus_Object = MibTableColumn
srcTEL2IPRowStatus = _SrcTEL2IPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 2),
    _SrcTEL2IPRowStatus_Type()
)
srcTEL2IPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPRowStatus.setStatus("current")


class _SrcTEL2IPAction_Type(Integer32):
    """Custom type srcTEL2IPAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SrcTEL2IPAction_Type.__name__ = "Integer32"
_SrcTEL2IPAction_Object = MibTableColumn
srcTEL2IPAction = _SrcTEL2IPAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 3),
    _SrcTEL2IPAction_Type()
)
srcTEL2IPAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcTEL2IPAction.setStatus("current")


class _SrcTEL2IPActionResult_Type(Integer32):
    """Custom type srcTEL2IPActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SrcTEL2IPActionResult_Type.__name__ = "Integer32"
_SrcTEL2IPActionResult_Object = MibTableColumn
srcTEL2IPActionResult = _SrcTEL2IPActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 4),
    _SrcTEL2IPActionResult_Type()
)
srcTEL2IPActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcTEL2IPActionResult.setStatus("current")


class _SrcTEL2IPPrefix_Type(SnmpAdminString):
    """Custom type srcTEL2IPPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SrcTEL2IPPrefix_Type.__name__ = "SnmpAdminString"
_SrcTEL2IPPrefix_Object = MibTableColumn
srcTEL2IPPrefix = _SrcTEL2IPPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 5),
    _SrcTEL2IPPrefix_Type()
)
srcTEL2IPPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPPrefix.setStatus("current")


class _SrcTEL2IPNumOfStrippedDigits_Type(Unsigned32):
    """Custom type srcTEL2IPNumOfStrippedDigits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_SrcTEL2IPNumOfStrippedDigits_Type.__name__ = "Unsigned32"
_SrcTEL2IPNumOfStrippedDigits_Object = MibTableColumn
srcTEL2IPNumOfStrippedDigits = _SrcTEL2IPNumOfStrippedDigits_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 6),
    _SrcTEL2IPNumOfStrippedDigits_Type()
)
srcTEL2IPNumOfStrippedDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPNumOfStrippedDigits.setStatus("current")


class _SrcTEL2IPPrefixToAdd_Type(SnmpAdminString):
    """Custom type srcTEL2IPPrefixToAdd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SrcTEL2IPPrefixToAdd_Type.__name__ = "SnmpAdminString"
_SrcTEL2IPPrefixToAdd_Object = MibTableColumn
srcTEL2IPPrefixToAdd = _SrcTEL2IPPrefixToAdd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 7),
    _SrcTEL2IPPrefixToAdd_Type()
)
srcTEL2IPPrefixToAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPPrefixToAdd.setStatus("current")


class _SrcTEL2IPNumOfDigitsToLeave_Type(Unsigned32):
    """Custom type srcTEL2IPNumOfDigitsToLeave based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SrcTEL2IPNumOfDigitsToLeave_Type.__name__ = "Unsigned32"
_SrcTEL2IPNumOfDigitsToLeave_Object = MibTableColumn
srcTEL2IPNumOfDigitsToLeave = _SrcTEL2IPNumOfDigitsToLeave_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 8),
    _SrcTEL2IPNumOfDigitsToLeave_Type()
)
srcTEL2IPNumOfDigitsToLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPNumOfDigitsToLeave.setStatus("current")


class _SrcTEL2IPNumberPlan_Type(Integer32):
    """Custom type srcTEL2IPNumberPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e164Public", 1),
          ("notConfigured", 255),
          ("private", 9),
          ("unknown", 0))
    )


_SrcTEL2IPNumberPlan_Type.__name__ = "Integer32"
_SrcTEL2IPNumberPlan_Object = MibTableColumn
srcTEL2IPNumberPlan = _SrcTEL2IPNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 9),
    _SrcTEL2IPNumberPlan_Type()
)
srcTEL2IPNumberPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPNumberPlan.setStatus("current")


class _SrcTEL2IPNumberType_Type(Integer32):
    """Custom type srcTEL2IPNumberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 6),
          ("international-Level2Regional", 1),
          ("national-Level1Regional", 2),
          ("networkSpecific-NetworkPISN", 3),
          ("notConfigured", 255),
          ("subscriber-Level0Regional", 4),
          ("unknown", 0))
    )


_SrcTEL2IPNumberType_Type.__name__ = "Integer32"
_SrcTEL2IPNumberType_Object = MibTableColumn
srcTEL2IPNumberType = _SrcTEL2IPNumberType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 10),
    _SrcTEL2IPNumberType_Type()
)
srcTEL2IPNumberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPNumberType.setStatus("current")


class _SrcTEL2IPDestPrefix_Type(SnmpAdminString):
    """Custom type srcTEL2IPDestPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SrcTEL2IPDestPrefix_Type.__name__ = "SnmpAdminString"
_SrcTEL2IPDestPrefix_Object = MibTableColumn
srcTEL2IPDestPrefix = _SrcTEL2IPDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 11),
    _SrcTEL2IPDestPrefix_Type()
)
srcTEL2IPDestPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPDestPrefix.setStatus("current")


class _SrcTEL2IPPresentation_Type(Integer32):
    """Custom type srcTEL2IPPresentation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("notBlocked", 0),
          ("notConfigured", 255))
    )


_SrcTEL2IPPresentation_Type.__name__ = "Integer32"
_SrcTEL2IPPresentation_Object = MibTableColumn
srcTEL2IPPresentation = _SrcTEL2IPPresentation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 12),
    _SrcTEL2IPPresentation_Type()
)
srcTEL2IPPresentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPPresentation.setStatus("current")


class _SrcTEL2IPNumOfDigitsToRemFromRight_Type(Unsigned32):
    """Custom type srcTEL2IPNumOfDigitsToRemFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_SrcTEL2IPNumOfDigitsToRemFromRight_Type.__name__ = "Unsigned32"
_SrcTEL2IPNumOfDigitsToRemFromRight_Object = MibTableColumn
srcTEL2IPNumOfDigitsToRemFromRight = _SrcTEL2IPNumOfDigitsToRemFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 13),
    _SrcTEL2IPNumOfDigitsToRemFromRight_Type()
)
srcTEL2IPNumOfDigitsToRemFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPNumOfDigitsToRemFromRight.setStatus("current")


class _SrcTEL2IPSuffix2Add_Type(SnmpAdminString):
    """Custom type srcTEL2IPSuffix2Add based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SrcTEL2IPSuffix2Add_Type.__name__ = "SnmpAdminString"
_SrcTEL2IPSuffix2Add_Object = MibTableColumn
srcTEL2IPSuffix2Add = _SrcTEL2IPSuffix2Add_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 14),
    _SrcTEL2IPSuffix2Add_Type()
)
srcTEL2IPSuffix2Add.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPSuffix2Add.setStatus("current")


class _SrcTEL2IPSourceIPAddress_Type(SnmpAdminString):
    """Custom type srcTEL2IPSourceIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SrcTEL2IPSourceIPAddress_Type.__name__ = "SnmpAdminString"
_SrcTEL2IPSourceIPAddress_Object = MibTableColumn
srcTEL2IPSourceIPAddress = _SrcTEL2IPSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 15),
    _SrcTEL2IPSourceIPAddress_Type()
)
srcTEL2IPSourceIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPSourceIPAddress.setStatus("current")


class _SrcTEL2IPSourceTrunkGroupID_Type(Integer32):
    """Custom type srcTEL2IPSourceTrunkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99),
    )


_SrcTEL2IPSourceTrunkGroupID_Type.__name__ = "Integer32"
_SrcTEL2IPSourceTrunkGroupID_Object = MibTableColumn
srcTEL2IPSourceTrunkGroupID = _SrcTEL2IPSourceTrunkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 16),
    _SrcTEL2IPSourceTrunkGroupID_Type()
)
srcTEL2IPSourceTrunkGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPSourceTrunkGroupID.setStatus("current")


class _SrcTEL2IPSourceIPGroupID_Type(Integer32):
    """Custom type srcTEL2IPSourceIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8),
    )


_SrcTEL2IPSourceIPGroupID_Type.__name__ = "Integer32"
_SrcTEL2IPSourceIPGroupID_Object = MibTableColumn
srcTEL2IPSourceIPGroupID = _SrcTEL2IPSourceIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 24, 1, 17),
    _SrcTEL2IPSourceIPGroupID_Type()
)
srcTEL2IPSourceIPGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srcTEL2IPSourceIPGroupID.setStatus("current")
_PhoneContextTable_Object = MibTable
phoneContextTable = _PhoneContextTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 25)
)
if mibBuilder.loadTexts:
    phoneContextTable.setStatus("current")
_PhoneContextEntry_Object = MibTableRow
phoneContextEntry = _PhoneContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 25, 1)
)
phoneContextEntry.setIndexNames(
    (0, "AcGateway", "phoneContextIndex"),
)
if mibBuilder.loadTexts:
    phoneContextEntry.setStatus("current")


class _PhoneContextIndex_Type(Unsigned32):
    """Custom type phoneContextIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_PhoneContextIndex_Type.__name__ = "Unsigned32"
_PhoneContextIndex_Object = MibTableColumn
phoneContextIndex = _PhoneContextIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 25, 1, 1),
    _PhoneContextIndex_Type()
)
phoneContextIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phoneContextIndex.setStatus("current")
_PhoneContextRowStatus_Type = RowStatus
_PhoneContextRowStatus_Object = MibTableColumn
phoneContextRowStatus = _PhoneContextRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 25, 1, 2),
    _PhoneContextRowStatus_Type()
)
phoneContextRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    phoneContextRowStatus.setStatus("current")


class _PhoneContextAction_Type(Integer32):
    """Custom type phoneContextAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_PhoneContextAction_Type.__name__ = "Integer32"
_PhoneContextAction_Object = MibTableColumn
phoneContextAction = _PhoneContextAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 25, 1, 3),
    _PhoneContextAction_Type()
)
phoneContextAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneContextAction.setStatus("current")


class _PhoneContextActionResult_Type(Integer32):
    """Custom type phoneContextActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_PhoneContextActionResult_Type.__name__ = "Integer32"
_PhoneContextActionResult_Object = MibTableColumn
phoneContextActionResult = _PhoneContextActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 25, 1, 4),
    _PhoneContextActionResult_Type()
)
phoneContextActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneContextActionResult.setStatus("current")


class _PhoneContextNPI_Type(Integer32):
    """Custom type phoneContextNPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              9)
        )
    )
    namedValues = NamedValues(
        *(("e164Public", 1),
          ("notConfigured", -1),
          ("private", 9),
          ("unknown", 0))
    )


_PhoneContextNPI_Type.__name__ = "Integer32"
_PhoneContextNPI_Object = MibTableColumn
phoneContextNPI = _PhoneContextNPI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 25, 1, 5),
    _PhoneContextNPI_Type()
)
phoneContextNPI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    phoneContextNPI.setStatus("current")


class _PhoneContextTON_Type(Integer32):
    """Custom type phoneContextTON based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 6),
          ("international-Level2Regional", 1),
          ("national-Level1Regional", 2),
          ("networkSpecific-NetworkPISN", 3),
          ("notConfigured", -1),
          ("subscriber-Level0Regional", 4),
          ("unknown", 0))
    )


_PhoneContextTON_Type.__name__ = "Integer32"
_PhoneContextTON_Object = MibTableColumn
phoneContextTON = _PhoneContextTON_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 25, 1, 6),
    _PhoneContextTON_Type()
)
phoneContextTON.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    phoneContextTON.setStatus("current")


class _PhoneContextPhoneContext_Type(SnmpAdminString):
    """Custom type phoneContextPhoneContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_PhoneContextPhoneContext_Type.__name__ = "SnmpAdminString"
_PhoneContextPhoneContext_Object = MibTableColumn
phoneContextPhoneContext = _PhoneContextPhoneContext_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 25, 1, 7),
    _PhoneContextPhoneContext_Type()
)
phoneContextPhoneContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    phoneContextPhoneContext.setStatus("current")
_RedirectNumberMapIp2TelTable_Object = MibTable
redirectNumberMapIp2TelTable = _RedirectNumberMapIp2TelTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26)
)
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelTable.setStatus("current")
_RedirectNumberMapIp2TelEntry_Object = MibTableRow
redirectNumberMapIp2TelEntry = _RedirectNumberMapIp2TelEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1)
)
redirectNumberMapIp2TelEntry.setIndexNames(
    (0, "AcGateway", "redirectNumberMapIp2TelIndex"),
)
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelEntry.setStatus("current")


class _RedirectNumberMapIp2TelIndex_Type(Unsigned32):
    """Custom type redirectNumberMapIp2TelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_RedirectNumberMapIp2TelIndex_Type.__name__ = "Unsigned32"
_RedirectNumberMapIp2TelIndex_Object = MibTableColumn
redirectNumberMapIp2TelIndex = _RedirectNumberMapIp2TelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 1),
    _RedirectNumberMapIp2TelIndex_Type()
)
redirectNumberMapIp2TelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelIndex.setStatus("current")
_RedirectNumberMapIp2TelRowStatus_Type = RowStatus
_RedirectNumberMapIp2TelRowStatus_Object = MibTableColumn
redirectNumberMapIp2TelRowStatus = _RedirectNumberMapIp2TelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 2),
    _RedirectNumberMapIp2TelRowStatus_Type()
)
redirectNumberMapIp2TelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelRowStatus.setStatus("current")


class _RedirectNumberMapIp2TelAction_Type(Integer32):
    """Custom type redirectNumberMapIp2TelAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_RedirectNumberMapIp2TelAction_Type.__name__ = "Integer32"
_RedirectNumberMapIp2TelAction_Object = MibTableColumn
redirectNumberMapIp2TelAction = _RedirectNumberMapIp2TelAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 3),
    _RedirectNumberMapIp2TelAction_Type()
)
redirectNumberMapIp2TelAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelAction.setStatus("current")


class _RedirectNumberMapIp2TelActionResult_Type(Integer32):
    """Custom type redirectNumberMapIp2TelActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_RedirectNumberMapIp2TelActionResult_Type.__name__ = "Integer32"
_RedirectNumberMapIp2TelActionResult_Object = MibTableColumn
redirectNumberMapIp2TelActionResult = _RedirectNumberMapIp2TelActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 4),
    _RedirectNumberMapIp2TelActionResult_Type()
)
redirectNumberMapIp2TelActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelActionResult.setStatus("current")


class _RedirectNumberMapIp2TelDestinationPrefix_Type(SnmpAdminString):
    """Custom type redirectNumberMapIp2TelDestinationPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RedirectNumberMapIp2TelDestinationPrefix_Type.__name__ = "SnmpAdminString"
_RedirectNumberMapIp2TelDestinationPrefix_Object = MibTableColumn
redirectNumberMapIp2TelDestinationPrefix = _RedirectNumberMapIp2TelDestinationPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 5),
    _RedirectNumberMapIp2TelDestinationPrefix_Type()
)
redirectNumberMapIp2TelDestinationPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelDestinationPrefix.setStatus("current")


class _RedirectNumberMapIp2TelRedirectPrefix_Type(SnmpAdminString):
    """Custom type redirectNumberMapIp2TelRedirectPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RedirectNumberMapIp2TelRedirectPrefix_Type.__name__ = "SnmpAdminString"
_RedirectNumberMapIp2TelRedirectPrefix_Object = MibTableColumn
redirectNumberMapIp2TelRedirectPrefix = _RedirectNumberMapIp2TelRedirectPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 6),
    _RedirectNumberMapIp2TelRedirectPrefix_Type()
)
redirectNumberMapIp2TelRedirectPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelRedirectPrefix.setStatus("current")


class _RedirectNumberMapIp2TelSourceAddress_Type(SnmpAdminString):
    """Custom type redirectNumberMapIp2TelSourceAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_RedirectNumberMapIp2TelSourceAddress_Type.__name__ = "SnmpAdminString"
_RedirectNumberMapIp2TelSourceAddress_Object = MibTableColumn
redirectNumberMapIp2TelSourceAddress = _RedirectNumberMapIp2TelSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 7),
    _RedirectNumberMapIp2TelSourceAddress_Type()
)
redirectNumberMapIp2TelSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelSourceAddress.setStatus("current")


class _RedirectNumberMapIp2TelNumberType_Type(Integer32):
    """Custom type redirectNumberMapIp2TelNumberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 6),
          ("international", 1),
          ("national", 2),
          ("networkSpecific", 3),
          ("notConfigured", 255),
          ("subscriber", 4),
          ("unknown", 0))
    )


_RedirectNumberMapIp2TelNumberType_Type.__name__ = "Integer32"
_RedirectNumberMapIp2TelNumberType_Object = MibTableColumn
redirectNumberMapIp2TelNumberType = _RedirectNumberMapIp2TelNumberType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 8),
    _RedirectNumberMapIp2TelNumberType_Type()
)
redirectNumberMapIp2TelNumberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelNumberType.setStatus("current")


class _RedirectNumberMapIp2TelNumberPlan_Type(Integer32):
    """Custom type redirectNumberMapIp2TelNumberPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e164Public", 1),
          ("notConfigured", 255),
          ("private", 9),
          ("unknown", 0))
    )


_RedirectNumberMapIp2TelNumberPlan_Type.__name__ = "Integer32"
_RedirectNumberMapIp2TelNumberPlan_Object = MibTableColumn
redirectNumberMapIp2TelNumberPlan = _RedirectNumberMapIp2TelNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 9),
    _RedirectNumberMapIp2TelNumberPlan_Type()
)
redirectNumberMapIp2TelNumberPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelNumberPlan.setStatus("current")


class _RedirectNumberMapIp2TelRemoveFromLeft_Type(Unsigned32):
    """Custom type redirectNumberMapIp2TelRemoveFromLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_RedirectNumberMapIp2TelRemoveFromLeft_Type.__name__ = "Unsigned32"
_RedirectNumberMapIp2TelRemoveFromLeft_Object = MibTableColumn
redirectNumberMapIp2TelRemoveFromLeft = _RedirectNumberMapIp2TelRemoveFromLeft_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 10),
    _RedirectNumberMapIp2TelRemoveFromLeft_Type()
)
redirectNumberMapIp2TelRemoveFromLeft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelRemoveFromLeft.setStatus("current")


class _RedirectNumberMapIp2TelRemoveFromRight_Type(Unsigned32):
    """Custom type redirectNumberMapIp2TelRemoveFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_RedirectNumberMapIp2TelRemoveFromRight_Type.__name__ = "Unsigned32"
_RedirectNumberMapIp2TelRemoveFromRight_Object = MibTableColumn
redirectNumberMapIp2TelRemoveFromRight = _RedirectNumberMapIp2TelRemoveFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 11),
    _RedirectNumberMapIp2TelRemoveFromRight_Type()
)
redirectNumberMapIp2TelRemoveFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelRemoveFromRight.setStatus("current")


class _RedirectNumberMapIp2TelLeaveFromRight_Type(Unsigned32):
    """Custom type redirectNumberMapIp2TelLeaveFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RedirectNumberMapIp2TelLeaveFromRight_Type.__name__ = "Unsigned32"
_RedirectNumberMapIp2TelLeaveFromRight_Object = MibTableColumn
redirectNumberMapIp2TelLeaveFromRight = _RedirectNumberMapIp2TelLeaveFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 12),
    _RedirectNumberMapIp2TelLeaveFromRight_Type()
)
redirectNumberMapIp2TelLeaveFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelLeaveFromRight.setStatus("current")


class _RedirectNumberMapIp2TelPrefixToAdd_Type(SnmpAdminString):
    """Custom type redirectNumberMapIp2TelPrefixToAdd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_RedirectNumberMapIp2TelPrefixToAdd_Type.__name__ = "SnmpAdminString"
_RedirectNumberMapIp2TelPrefixToAdd_Object = MibTableColumn
redirectNumberMapIp2TelPrefixToAdd = _RedirectNumberMapIp2TelPrefixToAdd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 13),
    _RedirectNumberMapIp2TelPrefixToAdd_Type()
)
redirectNumberMapIp2TelPrefixToAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelPrefixToAdd.setStatus("current")


class _RedirectNumberMapIp2TelSuffixToAdd_Type(SnmpAdminString):
    """Custom type redirectNumberMapIp2TelSuffixToAdd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_RedirectNumberMapIp2TelSuffixToAdd_Type.__name__ = "SnmpAdminString"
_RedirectNumberMapIp2TelSuffixToAdd_Object = MibTableColumn
redirectNumberMapIp2TelSuffixToAdd = _RedirectNumberMapIp2TelSuffixToAdd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 14),
    _RedirectNumberMapIp2TelSuffixToAdd_Type()
)
redirectNumberMapIp2TelSuffixToAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelSuffixToAdd.setStatus("current")


class _RedirectNumberMapIp2TelIsPresentationRestricted_Type(Integer32):
    """Custom type redirectNumberMapIp2TelIsPresentationRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 0),
          ("notConfigured", 255),
          ("restricted", 1))
    )


_RedirectNumberMapIp2TelIsPresentationRestricted_Type.__name__ = "Integer32"
_RedirectNumberMapIp2TelIsPresentationRestricted_Object = MibTableColumn
redirectNumberMapIp2TelIsPresentationRestricted = _RedirectNumberMapIp2TelIsPresentationRestricted_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 15),
    _RedirectNumberMapIp2TelIsPresentationRestricted_Type()
)
redirectNumberMapIp2TelIsPresentationRestricted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelIsPresentationRestricted.setStatus("current")


class _RedirectNumberMapIp2TelSrcTrunkGroupID_Type(Integer32):
    """Custom type redirectNumberMapIp2TelSrcTrunkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99),
    )


_RedirectNumberMapIp2TelSrcTrunkGroupID_Type.__name__ = "Integer32"
_RedirectNumberMapIp2TelSrcTrunkGroupID_Object = MibTableColumn
redirectNumberMapIp2TelSrcTrunkGroupID = _RedirectNumberMapIp2TelSrcTrunkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 16),
    _RedirectNumberMapIp2TelSrcTrunkGroupID_Type()
)
redirectNumberMapIp2TelSrcTrunkGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelSrcTrunkGroupID.setStatus("current")


class _RedirectNumberMapIp2TelSrcIPGroupID_Type(Integer32):
    """Custom type redirectNumberMapIp2TelSrcIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_RedirectNumberMapIp2TelSrcIPGroupID_Type.__name__ = "Integer32"
_RedirectNumberMapIp2TelSrcIPGroupID_Object = MibTableColumn
redirectNumberMapIp2TelSrcIPGroupID = _RedirectNumberMapIp2TelSrcIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 26, 1, 17),
    _RedirectNumberMapIp2TelSrcIPGroupID_Type()
)
redirectNumberMapIp2TelSrcIPGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapIp2TelSrcIPGroupID.setStatus("current")
_RedirectNumberMapTel2IpTable_Object = MibTable
redirectNumberMapTel2IpTable = _RedirectNumberMapTel2IpTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27)
)
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpTable.setStatus("current")
_RedirectNumberMapTel2IpEntry_Object = MibTableRow
redirectNumberMapTel2IpEntry = _RedirectNumberMapTel2IpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1)
)
redirectNumberMapTel2IpEntry.setIndexNames(
    (0, "AcGateway", "redirectNumberMapTel2IpIndex"),
)
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpEntry.setStatus("current")


class _RedirectNumberMapTel2IpIndex_Type(Unsigned32):
    """Custom type redirectNumberMapTel2IpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_RedirectNumberMapTel2IpIndex_Type.__name__ = "Unsigned32"
_RedirectNumberMapTel2IpIndex_Object = MibTableColumn
redirectNumberMapTel2IpIndex = _RedirectNumberMapTel2IpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 1),
    _RedirectNumberMapTel2IpIndex_Type()
)
redirectNumberMapTel2IpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpIndex.setStatus("current")
_RedirectNumberMapTel2IpRowStatus_Type = RowStatus
_RedirectNumberMapTel2IpRowStatus_Object = MibTableColumn
redirectNumberMapTel2IpRowStatus = _RedirectNumberMapTel2IpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 2),
    _RedirectNumberMapTel2IpRowStatus_Type()
)
redirectNumberMapTel2IpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpRowStatus.setStatus("current")


class _RedirectNumberMapTel2IpAction_Type(Integer32):
    """Custom type redirectNumberMapTel2IpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_RedirectNumberMapTel2IpAction_Type.__name__ = "Integer32"
_RedirectNumberMapTel2IpAction_Object = MibTableColumn
redirectNumberMapTel2IpAction = _RedirectNumberMapTel2IpAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 3),
    _RedirectNumberMapTel2IpAction_Type()
)
redirectNumberMapTel2IpAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpAction.setStatus("current")


class _RedirectNumberMapTel2IpActionResult_Type(Integer32):
    """Custom type redirectNumberMapTel2IpActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_RedirectNumberMapTel2IpActionResult_Type.__name__ = "Integer32"
_RedirectNumberMapTel2IpActionResult_Object = MibTableColumn
redirectNumberMapTel2IpActionResult = _RedirectNumberMapTel2IpActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 4),
    _RedirectNumberMapTel2IpActionResult_Type()
)
redirectNumberMapTel2IpActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpActionResult.setStatus("current")


class _RedirectNumberMapTel2IpDestinationPrefix_Type(SnmpAdminString):
    """Custom type redirectNumberMapTel2IpDestinationPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RedirectNumberMapTel2IpDestinationPrefix_Type.__name__ = "SnmpAdminString"
_RedirectNumberMapTel2IpDestinationPrefix_Object = MibTableColumn
redirectNumberMapTel2IpDestinationPrefix = _RedirectNumberMapTel2IpDestinationPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 5),
    _RedirectNumberMapTel2IpDestinationPrefix_Type()
)
redirectNumberMapTel2IpDestinationPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpDestinationPrefix.setStatus("current")


class _RedirectNumberMapTel2IpRedirectPrefix_Type(SnmpAdminString):
    """Custom type redirectNumberMapTel2IpRedirectPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RedirectNumberMapTel2IpRedirectPrefix_Type.__name__ = "SnmpAdminString"
_RedirectNumberMapTel2IpRedirectPrefix_Object = MibTableColumn
redirectNumberMapTel2IpRedirectPrefix = _RedirectNumberMapTel2IpRedirectPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 6),
    _RedirectNumberMapTel2IpRedirectPrefix_Type()
)
redirectNumberMapTel2IpRedirectPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpRedirectPrefix.setStatus("current")


class _RedirectNumberMapTel2IpSourceAddress_Type(SnmpAdminString):
    """Custom type redirectNumberMapTel2IpSourceAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_RedirectNumberMapTel2IpSourceAddress_Type.__name__ = "SnmpAdminString"
_RedirectNumberMapTel2IpSourceAddress_Object = MibTableColumn
redirectNumberMapTel2IpSourceAddress = _RedirectNumberMapTel2IpSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 7),
    _RedirectNumberMapTel2IpSourceAddress_Type()
)
redirectNumberMapTel2IpSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpSourceAddress.setStatus("current")


class _RedirectNumberMapTel2IpNumberType_Type(Unsigned32):
    """Custom type redirectNumberMapTel2IpNumberType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RedirectNumberMapTel2IpNumberType_Type.__name__ = "Unsigned32"
_RedirectNumberMapTel2IpNumberType_Object = MibTableColumn
redirectNumberMapTel2IpNumberType = _RedirectNumberMapTel2IpNumberType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 8),
    _RedirectNumberMapTel2IpNumberType_Type()
)
redirectNumberMapTel2IpNumberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpNumberType.setStatus("current")


class _RedirectNumberMapTel2IpNumberPlan_Type(Unsigned32):
    """Custom type redirectNumberMapTel2IpNumberPlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RedirectNumberMapTel2IpNumberPlan_Type.__name__ = "Unsigned32"
_RedirectNumberMapTel2IpNumberPlan_Object = MibTableColumn
redirectNumberMapTel2IpNumberPlan = _RedirectNumberMapTel2IpNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 9),
    _RedirectNumberMapTel2IpNumberPlan_Type()
)
redirectNumberMapTel2IpNumberPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpNumberPlan.setStatus("current")


class _RedirectNumberMapTel2IpRemoveFromLeft_Type(Unsigned32):
    """Custom type redirectNumberMapTel2IpRemoveFromLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_RedirectNumberMapTel2IpRemoveFromLeft_Type.__name__ = "Unsigned32"
_RedirectNumberMapTel2IpRemoveFromLeft_Object = MibTableColumn
redirectNumberMapTel2IpRemoveFromLeft = _RedirectNumberMapTel2IpRemoveFromLeft_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 10),
    _RedirectNumberMapTel2IpRemoveFromLeft_Type()
)
redirectNumberMapTel2IpRemoveFromLeft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpRemoveFromLeft.setStatus("current")


class _RedirectNumberMapTel2IpRemoveFromRight_Type(Unsigned32):
    """Custom type redirectNumberMapTel2IpRemoveFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 211),
    )


_RedirectNumberMapTel2IpRemoveFromRight_Type.__name__ = "Unsigned32"
_RedirectNumberMapTel2IpRemoveFromRight_Object = MibTableColumn
redirectNumberMapTel2IpRemoveFromRight = _RedirectNumberMapTel2IpRemoveFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 11),
    _RedirectNumberMapTel2IpRemoveFromRight_Type()
)
redirectNumberMapTel2IpRemoveFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpRemoveFromRight.setStatus("current")


class _RedirectNumberMapTel2IpLeaveFromRight_Type(Unsigned32):
    """Custom type redirectNumberMapTel2IpLeaveFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RedirectNumberMapTel2IpLeaveFromRight_Type.__name__ = "Unsigned32"
_RedirectNumberMapTel2IpLeaveFromRight_Object = MibTableColumn
redirectNumberMapTel2IpLeaveFromRight = _RedirectNumberMapTel2IpLeaveFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 12),
    _RedirectNumberMapTel2IpLeaveFromRight_Type()
)
redirectNumberMapTel2IpLeaveFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpLeaveFromRight.setStatus("current")


class _RedirectNumberMapTel2IpPrefixToAdd_Type(SnmpAdminString):
    """Custom type redirectNumberMapTel2IpPrefixToAdd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_RedirectNumberMapTel2IpPrefixToAdd_Type.__name__ = "SnmpAdminString"
_RedirectNumberMapTel2IpPrefixToAdd_Object = MibTableColumn
redirectNumberMapTel2IpPrefixToAdd = _RedirectNumberMapTel2IpPrefixToAdd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 13),
    _RedirectNumberMapTel2IpPrefixToAdd_Type()
)
redirectNumberMapTel2IpPrefixToAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpPrefixToAdd.setStatus("current")


class _RedirectNumberMapTel2IpSuffixToAdd_Type(SnmpAdminString):
    """Custom type redirectNumberMapTel2IpSuffixToAdd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_RedirectNumberMapTel2IpSuffixToAdd_Type.__name__ = "SnmpAdminString"
_RedirectNumberMapTel2IpSuffixToAdd_Object = MibTableColumn
redirectNumberMapTel2IpSuffixToAdd = _RedirectNumberMapTel2IpSuffixToAdd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 14),
    _RedirectNumberMapTel2IpSuffixToAdd_Type()
)
redirectNumberMapTel2IpSuffixToAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpSuffixToAdd.setStatus("current")


class _RedirectNumberMapTel2IpIsPresentationRestricted_Type(Integer32):
    """Custom type redirectNumberMapTel2IpIsPresentationRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 0),
          ("notConfigured", 255),
          ("restricted", 1))
    )


_RedirectNumberMapTel2IpIsPresentationRestricted_Type.__name__ = "Integer32"
_RedirectNumberMapTel2IpIsPresentationRestricted_Object = MibTableColumn
redirectNumberMapTel2IpIsPresentationRestricted = _RedirectNumberMapTel2IpIsPresentationRestricted_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 15),
    _RedirectNumberMapTel2IpIsPresentationRestricted_Type()
)
redirectNumberMapTel2IpIsPresentationRestricted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpIsPresentationRestricted.setStatus("current")


class _RedirectNumberMapTel2IpSrcTrunkGroupID_Type(Integer32):
    """Custom type redirectNumberMapTel2IpSrcTrunkGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99),
    )


_RedirectNumberMapTel2IpSrcTrunkGroupID_Type.__name__ = "Integer32"
_RedirectNumberMapTel2IpSrcTrunkGroupID_Object = MibTableColumn
redirectNumberMapTel2IpSrcTrunkGroupID = _RedirectNumberMapTel2IpSrcTrunkGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 16),
    _RedirectNumberMapTel2IpSrcTrunkGroupID_Type()
)
redirectNumberMapTel2IpSrcTrunkGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpSrcTrunkGroupID.setStatus("current")


class _RedirectNumberMapTel2IpSrcIPGroupID_Type(Integer32):
    """Custom type redirectNumberMapTel2IpSrcIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_RedirectNumberMapTel2IpSrcIPGroupID_Type.__name__ = "Integer32"
_RedirectNumberMapTel2IpSrcIPGroupID_Object = MibTableColumn
redirectNumberMapTel2IpSrcIPGroupID = _RedirectNumberMapTel2IpSrcIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 21, 27, 1, 17),
    _RedirectNumberMapTel2IpSrcIPGroupID_Type()
)
redirectNumberMapTel2IpSrcIPGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redirectNumberMapTel2IpSrcIPGroupID.setStatus("current")
_ConnectivityQos_ObjectIdentity = ObjectIdentity
connectivityQos = _ConnectivityQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 22)
)


class _ConnectivityQosMaxAllowedPL_Type(Unsigned32):
    """Custom type connectivityQosMaxAllowedPL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConnectivityQosMaxAllowedPL_Type.__name__ = "Unsigned32"
_ConnectivityQosMaxAllowedPL_Object = MibScalar
connectivityQosMaxAllowedPL = _ConnectivityQosMaxAllowedPL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 22, 1),
    _ConnectivityQosMaxAllowedPL_Type()
)
connectivityQosMaxAllowedPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectivityQosMaxAllowedPL.setStatus("current")


class _ConnectivityQosMaxAllowedDelay_Type(Unsigned32):
    """Custom type connectivityQosMaxAllowedDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ConnectivityQosMaxAllowedDelay_Type.__name__ = "Unsigned32"
_ConnectivityQosMaxAllowedDelay_Object = MibScalar
connectivityQosMaxAllowedDelay = _ConnectivityQosMaxAllowedDelay_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 22, 2),
    _ConnectivityQosMaxAllowedDelay_Type()
)
connectivityQosMaxAllowedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectivityQosMaxAllowedDelay.setStatus("current")


class _ConnectivityQosEffectivePeriod_Type(Unsigned32):
    """Custom type connectivityQosEffectivePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ConnectivityQosEffectivePeriod_Type.__name__ = "Unsigned32"
_ConnectivityQosEffectivePeriod_Object = MibScalar
connectivityQosEffectivePeriod = _ConnectivityQosEffectivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 22, 3),
    _ConnectivityQosEffectivePeriod_Type()
)
connectivityQosEffectivePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectivityQosEffectivePeriod.setStatus("current")


class _ConnectivityQosSamplesToAvarage_Type(Unsigned32):
    """Custom type connectivityQosSamplesToAvarage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConnectivityQosSamplesToAvarage_Type.__name__ = "Unsigned32"
_ConnectivityQosSamplesToAvarage_Object = MibScalar
connectivityQosSamplesToAvarage = _ConnectivityQosSamplesToAvarage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 2, 22, 4),
    _ConnectivityQosSamplesToAvarage_Type()
)
connectivityQosSamplesToAvarage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectivityQosSamplesToAvarage.setStatus("current")
_DigitalGW_ObjectIdentity = ObjectIdentity
digitalGW = _DigitalGW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3)
)


class _DigitalGWBChannelNegotiation_Type(Integer32):
    """Custom type digitalGWBChannelNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("no", 0),
          ("yes", 1))
    )


_DigitalGWBChannelNegotiation_Type.__name__ = "Integer32"
_DigitalGWBChannelNegotiation_Object = MibScalar
digitalGWBChannelNegotiation = _DigitalGWBChannelNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 1),
    _DigitalGWBChannelNegotiation_Type()
)
digitalGWBChannelNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWBChannelNegotiation.setStatus("current")


class _DigitalGWSwapRedirectNumber_Type(Integer32):
    """Custom type digitalGWSwapRedirectNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DigitalGWSwapRedirectNumber_Type.__name__ = "Integer32"
_DigitalGWSwapRedirectNumber_Object = MibScalar
digitalGWSwapRedirectNumber = _DigitalGWSwapRedirectNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 2),
    _DigitalGWSwapRedirectNumber_Type()
)
digitalGWSwapRedirectNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWSwapRedirectNumber.setStatus("current")


class _DigitalGWEnableTransferCap_Type(Integer32):
    """Custom type digitalGWEnableTransferCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DigitalGWEnableTransferCap_Type.__name__ = "Integer32"
_DigitalGWEnableTransferCap_Object = MibScalar
digitalGWEnableTransferCap = _DigitalGWEnableTransferCap_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 3),
    _DigitalGWEnableTransferCap_Type()
)
digitalGWEnableTransferCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWEnableTransferCap.setStatus("current")


class _DigitalGWR2Category_Type(Unsigned32):
    """Custom type digitalGWR2Category based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DigitalGWR2Category_Type.__name__ = "Unsigned32"
_DigitalGWR2Category_Object = MibScalar
digitalGWR2Category = _DigitalGWR2Category_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 4),
    _DigitalGWR2Category_Type()
)
digitalGWR2Category.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWR2Category.setStatus("current")


class _DigitalGWISDNRxOverlap_Type(Integer32):
    """Custom type digitalGWISDNRxOverlap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DigitalGWISDNRxOverlap_Type.__name__ = "Integer32"
_DigitalGWISDNRxOverlap_Object = MibScalar
digitalGWISDNRxOverlap = _DigitalGWISDNRxOverlap_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 5),
    _DigitalGWISDNRxOverlap_Type()
)
digitalGWISDNRxOverlap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWISDNRxOverlap.setStatus("obsolete")


class _DigitalGWCASSendHookFlash_Type(Integer32):
    """Custom type digitalGWCASSendHookFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWCASSendHookFlash_Type.__name__ = "Integer32"
_DigitalGWCASSendHookFlash_Object = MibScalar
digitalGWCASSendHookFlash = _DigitalGWCASSendHookFlash_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 6),
    _DigitalGWCASSendHookFlash_Type()
)
digitalGWCASSendHookFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWCASSendHookFlash.setStatus("current")


class _DigitalGWISDNTransferCapability_Type(Integer32):
    """Custom type digitalGWISDNTransferCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("audio", 3),
          ("data", 2),
          ("doNotOverwrite", -1),
          ("modem", 0),
          ("voice", 1))
    )


_DigitalGWISDNTransferCapability_Type.__name__ = "Integer32"
_DigitalGWISDNTransferCapability_Object = MibScalar
digitalGWISDNTransferCapability = _DigitalGWISDNTransferCapability_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 7),
    _DigitalGWISDNTransferCapability_Type()
)
digitalGWISDNTransferCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWISDNTransferCapability.setStatus("obsolete")


class _DigitalGWEnableTDMOverIp_Type(Integer32):
    """Custom type digitalGWEnableTDMOverIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWEnableTDMOverIp_Type.__name__ = "Integer32"
_DigitalGWEnableTDMOverIp_Object = MibScalar
digitalGWEnableTDMOverIp = _DigitalGWEnableTDMOverIp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 8),
    _DigitalGWEnableTDMOverIp_Type()
)
digitalGWEnableTDMOverIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWEnableTDMOverIp.setStatus("current")


class _DigitalGWTransparentCoderOnDataCall_Type(Integer32):
    """Custom type digitalGWTransparentCoderOnDataCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWTransparentCoderOnDataCall_Type.__name__ = "Integer32"
_DigitalGWTransparentCoderOnDataCall_Object = MibScalar
digitalGWTransparentCoderOnDataCall = _DigitalGWTransparentCoderOnDataCall_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 9),
    _DigitalGWTransparentCoderOnDataCall_Type()
)
digitalGWTransparentCoderOnDataCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWTransparentCoderOnDataCall.setStatus("current")


class _DigitalGWSupportRedirectInFacility_Type(Integer32):
    """Custom type digitalGWSupportRedirectInFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWSupportRedirectInFacility_Type.__name__ = "Integer32"
_DigitalGWSupportRedirectInFacility_Object = MibScalar
digitalGWSupportRedirectInFacility = _DigitalGWSupportRedirectInFacility_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 10),
    _DigitalGWSupportRedirectInFacility_Type()
)
digitalGWSupportRedirectInFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWSupportRedirectInFacility.setStatus("current")


class _DigitalGWPIForDisconnectMsg_Type(Integer32):
    """Custom type digitalGWPIForDisconnectMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8),
    )


_DigitalGWPIForDisconnectMsg_Type.__name__ = "Integer32"
_DigitalGWPIForDisconnectMsg_Object = MibScalar
digitalGWPIForDisconnectMsg = _DigitalGWPIForDisconnectMsg_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 11),
    _DigitalGWPIForDisconnectMsg_Type()
)
digitalGWPIForDisconnectMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWPIForDisconnectMsg.setStatus("obsolete")


class _DigitalGWConnectOnProgressInd_Type(Integer32):
    """Custom type digitalGWConnectOnProgressInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWConnectOnProgressInd_Type.__name__ = "Integer32"
_DigitalGWConnectOnProgressInd_Object = MibScalar
digitalGWConnectOnProgressInd = _DigitalGWConnectOnProgressInd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 12),
    _DigitalGWConnectOnProgressInd_Type()
)
digitalGWConnectOnProgressInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWConnectOnProgressInd.setStatus("current")


class _DigitalGWLocalISDNRBSource_Type(Integer32):
    """Custom type digitalGWLocalISDNRBSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 1),
          ("pbx", 0))
    )


_DigitalGWLocalISDNRBSource_Type.__name__ = "Integer32"
_DigitalGWLocalISDNRBSource_Object = MibScalar
digitalGWLocalISDNRBSource = _DigitalGWLocalISDNRBSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 13),
    _DigitalGWLocalISDNRBSource_Type()
)
digitalGWLocalISDNRBSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWLocalISDNRBSource.setStatus("obsolete")


class _DigitalGWEnableUuiTel2Ip_Type(Integer32):
    """Custom type digitalGWEnableUuiTel2Ip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWEnableUuiTel2Ip_Type.__name__ = "Integer32"
_DigitalGWEnableUuiTel2Ip_Object = MibScalar
digitalGWEnableUuiTel2Ip = _DigitalGWEnableUuiTel2Ip_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 14),
    _DigitalGWEnableUuiTel2Ip_Type()
)
digitalGWEnableUuiTel2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWEnableUuiTel2Ip.setStatus("current")


class _DigitalGWEnableUuiIp2Tel_Type(Integer32):
    """Custom type digitalGWEnableUuiIp2Tel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWEnableUuiIp2Tel_Type.__name__ = "Integer32"
_DigitalGWEnableUuiIp2Tel_Object = MibScalar
digitalGWEnableUuiIp2Tel = _DigitalGWEnableUuiIp2Tel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 15),
    _DigitalGWEnableUuiIp2Tel_Type()
)
digitalGWEnableUuiIp2Tel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWEnableUuiIp2Tel.setStatus("current")


class _DigitalGWSendISDNTransferOnConnect_Type(Integer32):
    """Custom type digitalGWSendISDNTransferOnConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWSendISDNTransferOnConnect_Type.__name__ = "Integer32"
_DigitalGWSendISDNTransferOnConnect_Object = MibScalar
digitalGWSendISDNTransferOnConnect = _DigitalGWSendISDNTransferOnConnect_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 16),
    _DigitalGWSendISDNTransferOnConnect_Type()
)
digitalGWSendISDNTransferOnConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWSendISDNTransferOnConnect.setStatus("current")


class _DigitalGWEnableISDNTunnelingTel2Ip_Type(Integer32):
    """Custom type digitalGWEnableISDNTunnelingTel2Ip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("usingBody", 2),
          ("usingHeader", 1))
    )


_DigitalGWEnableISDNTunnelingTel2Ip_Type.__name__ = "Integer32"
_DigitalGWEnableISDNTunnelingTel2Ip_Object = MibScalar
digitalGWEnableISDNTunnelingTel2Ip = _DigitalGWEnableISDNTunnelingTel2Ip_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 17),
    _DigitalGWEnableISDNTunnelingTel2Ip_Type()
)
digitalGWEnableISDNTunnelingTel2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWEnableISDNTunnelingTel2Ip.setStatus("current")


class _DigitalGWEnableISDNTunnelingIp2Tel_Type(Integer32):
    """Custom type digitalGWEnableISDNTunnelingIp2Tel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("usingBody", 2),
          ("usingHeader", 1))
    )


_DigitalGWEnableISDNTunnelingIp2Tel_Type.__name__ = "Integer32"
_DigitalGWEnableISDNTunnelingIp2Tel_Object = MibScalar
digitalGWEnableISDNTunnelingIp2Tel = _DigitalGWEnableISDNTunnelingIp2Tel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 18),
    _DigitalGWEnableISDNTunnelingIp2Tel_Type()
)
digitalGWEnableISDNTunnelingIp2Tel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWEnableISDNTunnelingIp2Tel.setStatus("current")


class _DigitalGWEnableCallingPartyCategory_Type(Integer32):
    """Custom type digitalGWEnableCallingPartyCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWEnableCallingPartyCategory_Type.__name__ = "Integer32"
_DigitalGWEnableCallingPartyCategory_Object = MibScalar
digitalGWEnableCallingPartyCategory = _DigitalGWEnableCallingPartyCategory_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 19),
    _DigitalGWEnableCallingPartyCategory_Type()
)
digitalGWEnableCallingPartyCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWEnableCallingPartyCategory.setStatus("current")
_IE_ObjectIdentity = ObjectIdentity
iE = _IE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 20)
)


class _IEAddIEInSetup_Type(SnmpAdminString):
    """Custom type iEAddIEInSetup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_IEAddIEInSetup_Type.__name__ = "SnmpAdminString"
_IEAddIEInSetup_Object = MibScalar
iEAddIEInSetup = _IEAddIEInSetup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 20, 1),
    _IEAddIEInSetup_Type()
)
iEAddIEInSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iEAddIEInSetup.setStatus("current")


class _IESendIEOnTG_Type(SnmpAdminString):
    """Custom type iESendIEOnTG based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_IESendIEOnTG_Type.__name__ = "SnmpAdminString"
_IESendIEOnTG_Object = MibScalar
iESendIEOnTG = _IESendIEOnTG_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 20, 2),
    _IESendIEOnTG_Type()
)
iESendIEOnTG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iESendIEOnTG.setStatus("current")
_ISDNRxOverlapTable_Object = MibTable
iSDNRxOverlapTable = _ISDNRxOverlapTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 21)
)
if mibBuilder.loadTexts:
    iSDNRxOverlapTable.setStatus("current")
_ISDNRxOverlapEntry_Object = MibTableRow
iSDNRxOverlapEntry = _ISDNRxOverlapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 21, 1)
)
iSDNRxOverlapEntry.setIndexNames(
    (0, "AcGateway", "iSDNRxOverlapIndex"),
)
if mibBuilder.loadTexts:
    iSDNRxOverlapEntry.setStatus("current")


class _ISDNRxOverlapIndex_Type(Unsigned32):
    """Custom type iSDNRxOverlapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ISDNRxOverlapIndex_Type.__name__ = "Unsigned32"
_ISDNRxOverlapIndex_Object = MibTableColumn
iSDNRxOverlapIndex = _ISDNRxOverlapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 21, 1, 1),
    _ISDNRxOverlapIndex_Type()
)
iSDNRxOverlapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iSDNRxOverlapIndex.setStatus("current")


class _ISDNRxOverlapEnable_Type(Integer32):
    """Custom type iSDNRxOverlapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localReceiving", 1),
          ("none", 0),
          ("throughSIP", 2))
    )


_ISDNRxOverlapEnable_Type.__name__ = "Integer32"
_ISDNRxOverlapEnable_Object = MibTableColumn
iSDNRxOverlapEnable = _ISDNRxOverlapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 21, 1, 2),
    _ISDNRxOverlapEnable_Type()
)
iSDNRxOverlapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iSDNRxOverlapEnable.setStatus("current")
_TrunkTransferTable_Object = MibTable
trunkTransferTable = _TrunkTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 22)
)
if mibBuilder.loadTexts:
    trunkTransferTable.setStatus("current")
_TrunkTransferEntry_Object = MibTableRow
trunkTransferEntry = _TrunkTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 22, 1)
)
trunkTransferEntry.setIndexNames(
    (0, "AcGateway", "trunkTransferIndex"),
)
if mibBuilder.loadTexts:
    trunkTransferEntry.setStatus("current")


class _TrunkTransferIndex_Type(Unsigned32):
    """Custom type trunkTransferIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_TrunkTransferIndex_Type.__name__ = "Unsigned32"
_TrunkTransferIndex_Object = MibTableColumn
trunkTransferIndex = _TrunkTransferIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 22, 1, 1),
    _TrunkTransferIndex_Type()
)
trunkTransferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkTransferIndex.setStatus("current")


class _TrunkTransferMode_Type(Integer32):
    """Custom type trunkTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("casNFA", 1),
          ("casNormal", 3),
          ("iSDN", 2),
          ("none", 0),
          ("qSIGPathReplacement", 5),
          ("qSIGSingleStep", 4))
    )


_TrunkTransferMode_Type.__name__ = "Integer32"
_TrunkTransferMode_Object = MibTableColumn
trunkTransferMode = _TrunkTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 22, 1, 2),
    _TrunkTransferMode_Type()
)
trunkTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkTransferMode.setStatus("current")
_ProgressIndicatorToISDNTable_Object = MibTable
progressIndicatorToISDNTable = _ProgressIndicatorToISDNTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 23)
)
if mibBuilder.loadTexts:
    progressIndicatorToISDNTable.setStatus("current")
_ProgressIndicatorToISDNEntry_Object = MibTableRow
progressIndicatorToISDNEntry = _ProgressIndicatorToISDNEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 23, 1)
)
progressIndicatorToISDNEntry.setIndexNames(
    (0, "AcGateway", "progressIndicatorToISDNIndex"),
)
if mibBuilder.loadTexts:
    progressIndicatorToISDNEntry.setStatus("current")


class _ProgressIndicatorToISDNIndex_Type(Unsigned32):
    """Custom type progressIndicatorToISDNIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ProgressIndicatorToISDNIndex_Type.__name__ = "Unsigned32"
_ProgressIndicatorToISDNIndex_Object = MibTableColumn
progressIndicatorToISDNIndex = _ProgressIndicatorToISDNIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 23, 1, 1),
    _ProgressIndicatorToISDNIndex_Type()
)
progressIndicatorToISDNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    progressIndicatorToISDNIndex.setStatus("current")


class _ProgressIndicatorToISDNValue_Type(Integer32):
    """Custom type progressIndicatorToISDNValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              8)
        )
    )
    namedValues = NamedValues(
        *(("localRB", 0),
          ("notSet", -1),
          ("remoteRB1", 1),
          ("remoteRB8", 8))
    )


_ProgressIndicatorToISDNValue_Type.__name__ = "Integer32"
_ProgressIndicatorToISDNValue_Object = MibTableColumn
progressIndicatorToISDNValue = _ProgressIndicatorToISDNValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 23, 1, 2),
    _ProgressIndicatorToISDNValue_Type()
)
progressIndicatorToISDNValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    progressIndicatorToISDNValue.setStatus("current")
_PlayRBToneToTrunkTable_Object = MibTable
playRBToneToTrunkTable = _PlayRBToneToTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 24)
)
if mibBuilder.loadTexts:
    playRBToneToTrunkTable.setStatus("current")
_PlayRBToneToTrunkEntry_Object = MibTableRow
playRBToneToTrunkEntry = _PlayRBToneToTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 24, 1)
)
playRBToneToTrunkEntry.setIndexNames(
    (0, "AcGateway", "playRBToneToTrunkIndex"),
)
if mibBuilder.loadTexts:
    playRBToneToTrunkEntry.setStatus("current")


class _PlayRBToneToTrunkIndex_Type(Unsigned32):
    """Custom type playRBToneToTrunkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_PlayRBToneToTrunkIndex_Type.__name__ = "Unsigned32"
_PlayRBToneToTrunkIndex_Object = MibTableColumn
playRBToneToTrunkIndex = _PlayRBToneToTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 24, 1, 1),
    _PlayRBToneToTrunkIndex_Type()
)
playRBToneToTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    playRBToneToTrunkIndex.setStatus("current")


class _PlayRBToneToTrunkValue_Type(Integer32):
    """Custom type playRBToneToTrunkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doNotPlay", 0),
          ("notConfigured", -1),
          ("playLocalUntilRemoteMediaArrives", 3),
          ("playOnLocal", 1),
          ("preferIp", 2))
    )


_PlayRBToneToTrunkValue_Type.__name__ = "Integer32"
_PlayRBToneToTrunkValue_Object = MibTableColumn
playRBToneToTrunkValue = _PlayRBToneToTrunkValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 24, 1, 2),
    _PlayRBToneToTrunkValue_Type()
)
playRBToneToTrunkValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    playRBToneToTrunkValue.setStatus("current")
_ISDNTransferCapabilityTable_Object = MibTable
iSDNTransferCapabilityTable = _ISDNTransferCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 25)
)
if mibBuilder.loadTexts:
    iSDNTransferCapabilityTable.setStatus("current")
_ISDNTransferCapabilityEntry_Object = MibTableRow
iSDNTransferCapabilityEntry = _ISDNTransferCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 25, 1)
)
iSDNTransferCapabilityEntry.setIndexNames(
    (0, "AcGateway", "iSDNTransferCapabilityIndex"),
)
if mibBuilder.loadTexts:
    iSDNTransferCapabilityEntry.setStatus("current")


class _ISDNTransferCapabilityIndex_Type(Unsigned32):
    """Custom type iSDNTransferCapabilityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_ISDNTransferCapabilityIndex_Type.__name__ = "Unsigned32"
_ISDNTransferCapabilityIndex_Object = MibTableColumn
iSDNTransferCapabilityIndex = _ISDNTransferCapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 25, 1, 1),
    _ISDNTransferCapabilityIndex_Type()
)
iSDNTransferCapabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iSDNTransferCapabilityIndex.setStatus("current")


class _ISDNTransferCapabilityValue_Type(Integer32):
    """Custom type iSDNTransferCapabilityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("audio", 3),
          ("data", 2),
          ("doNotOverwrite", -1),
          ("modem", 0),
          ("voice", 1))
    )


_ISDNTransferCapabilityValue_Type.__name__ = "Integer32"
_ISDNTransferCapabilityValue_Object = MibTableColumn
iSDNTransferCapabilityValue = _ISDNTransferCapabilityValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 25, 1, 2),
    _ISDNTransferCapabilityValue_Type()
)
iSDNTransferCapabilityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iSDNTransferCapabilityValue.setStatus("current")
_LocalISDNRBSourceTable_Object = MibTable
localISDNRBSourceTable = _LocalISDNRBSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 26)
)
if mibBuilder.loadTexts:
    localISDNRBSourceTable.setStatus("current")
_LocalISDNRBSourceEntry_Object = MibTableRow
localISDNRBSourceEntry = _LocalISDNRBSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 26, 1)
)
localISDNRBSourceEntry.setIndexNames(
    (0, "AcGateway", "localISDNRBSourceIndex"),
)
if mibBuilder.loadTexts:
    localISDNRBSourceEntry.setStatus("current")


class _LocalISDNRBSourceIndex_Type(Unsigned32):
    """Custom type localISDNRBSourceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_LocalISDNRBSourceIndex_Type.__name__ = "Unsigned32"
_LocalISDNRBSourceIndex_Object = MibTableColumn
localISDNRBSourceIndex = _LocalISDNRBSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 26, 1, 1),
    _LocalISDNRBSourceIndex_Type()
)
localISDNRBSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    localISDNRBSourceIndex.setStatus("current")


class _LocalISDNRBSourceValue_Type(Integer32):
    """Custom type localISDNRBSourceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 1),
          ("pbx", 0))
    )


_LocalISDNRBSourceValue_Type.__name__ = "Integer32"
_LocalISDNRBSourceValue_Object = MibTableColumn
localISDNRBSourceValue = _LocalISDNRBSourceValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 26, 1, 2),
    _LocalISDNRBSourceValue_Type()
)
localISDNRBSourceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localISDNRBSourceValue.setStatus("current")
_PIForDisconnectMsgTable_Object = MibTable
pIForDisconnectMsgTable = _PIForDisconnectMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 27)
)
if mibBuilder.loadTexts:
    pIForDisconnectMsgTable.setStatus("current")
_PIForDisconnectMsgEntry_Object = MibTableRow
pIForDisconnectMsgEntry = _PIForDisconnectMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 27, 1)
)
pIForDisconnectMsgEntry.setIndexNames(
    (0, "AcGateway", "pIForDisconnectMsgIndex"),
)
if mibBuilder.loadTexts:
    pIForDisconnectMsgEntry.setStatus("current")


class _PIForDisconnectMsgIndex_Type(Unsigned32):
    """Custom type pIForDisconnectMsgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_PIForDisconnectMsgIndex_Type.__name__ = "Unsigned32"
_PIForDisconnectMsgIndex_Object = MibTableColumn
pIForDisconnectMsgIndex = _PIForDisconnectMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 27, 1, 1),
    _PIForDisconnectMsgIndex_Type()
)
pIForDisconnectMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pIForDisconnectMsgIndex.setStatus("current")


class _PIForDisconnectMsgValue_Type(Integer32):
    """Custom type pIForDisconnectMsgValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8),
    )


_PIForDisconnectMsgValue_Type.__name__ = "Integer32"
_PIForDisconnectMsgValue_Object = MibTableColumn
pIForDisconnectMsgValue = _PIForDisconnectMsgValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 27, 1, 2),
    _PIForDisconnectMsgValue_Type()
)
pIForDisconnectMsgValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pIForDisconnectMsgValue.setStatus("current")
_PSTNAlertTimeoutTable_Object = MibTable
pSTNAlertTimeoutTable = _PSTNAlertTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 28)
)
if mibBuilder.loadTexts:
    pSTNAlertTimeoutTable.setStatus("current")
_PSTNAlertTimeoutEntry_Object = MibTableRow
pSTNAlertTimeoutEntry = _PSTNAlertTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 28, 1)
)
pSTNAlertTimeoutEntry.setIndexNames(
    (0, "AcGateway", "pSTNAlertTimeoutIndex"),
)
if mibBuilder.loadTexts:
    pSTNAlertTimeoutEntry.setStatus("current")


class _PSTNAlertTimeoutIndex_Type(Unsigned32):
    """Custom type pSTNAlertTimeoutIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_PSTNAlertTimeoutIndex_Type.__name__ = "Unsigned32"
_PSTNAlertTimeoutIndex_Object = MibTableColumn
pSTNAlertTimeoutIndex = _PSTNAlertTimeoutIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 28, 1, 1),
    _PSTNAlertTimeoutIndex_Type()
)
pSTNAlertTimeoutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pSTNAlertTimeoutIndex.setStatus("current")


class _PSTNAlertTimeoutValue_Type(Integer32):
    """Custom type pSTNAlertTimeoutValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_PSTNAlertTimeoutValue_Type.__name__ = "Integer32"
_PSTNAlertTimeoutValue_Object = MibTableColumn
pSTNAlertTimeoutValue = _PSTNAlertTimeoutValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 28, 1, 2),
    _PSTNAlertTimeoutValue_Type()
)
pSTNAlertTimeoutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pSTNAlertTimeoutValue.setStatus("current")
_Mlpp_ObjectIdentity = ObjectIdentity
mlpp = _Mlpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29)
)


class _MlppCallPriorityMode_Type(Integer32):
    """Custom type mlppCallPriorityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("mLPP", 1))
    )


_MlppCallPriorityMode_Type.__name__ = "Integer32"
_MlppCallPriorityMode_Object = MibScalar
mlppCallPriorityMode = _MlppCallPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 1),
    _MlppCallPriorityMode_Type()
)
mlppCallPriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppCallPriorityMode.setStatus("current")


class _MlppDefaultNamespace_Type(Integer32):
    """Custom type mlppDefaultNamespace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dOD", 2),
          ("dRSN", 3),
          ("dSN", 1))
    )


_MlppDefaultNamespace_Type.__name__ = "Integer32"
_MlppDefaultNamespace_Object = MibScalar
mlppDefaultNamespace = _MlppDefaultNamespace_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 2),
    _MlppDefaultNamespace_Type()
)
mlppDefaultNamespace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppDefaultNamespace.setStatus("current")


class _MlppDefaultCallPriority_Type(SnmpAdminString):
    """Custom type mlppDefaultCallPriority based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_MlppDefaultCallPriority_Type.__name__ = "SnmpAdminString"
_MlppDefaultCallPriority_Object = MibScalar
mlppDefaultCallPriority = _MlppDefaultCallPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 3),
    _MlppDefaultCallPriority_Type()
)
mlppDefaultCallPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppDefaultCallPriority.setStatus("current")


class _MlppDiffServ_Type(Unsigned32):
    """Custom type mlppDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MlppDiffServ_Type.__name__ = "Unsigned32"
_MlppDiffServ_Object = MibScalar
mlppDiffServ = _MlppDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 4),
    _MlppDiffServ_Type()
)
mlppDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppDiffServ.setStatus("current")


class _MlppPreemptionToneDuration_Type(Unsigned32):
    """Custom type mlppPreemptionToneDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_MlppPreemptionToneDuration_Type.__name__ = "Unsigned32"
_MlppPreemptionToneDuration_Object = MibScalar
mlppPreemptionToneDuration = _MlppPreemptionToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 5),
    _MlppPreemptionToneDuration_Type()
)
mlppPreemptionToneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppPreemptionToneDuration.setStatus("current")


class _MlppDefaultServiceDomain_Type(SnmpAdminString):
    """Custom type mlppDefaultServiceDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_MlppDefaultServiceDomain_Type.__name__ = "SnmpAdminString"
_MlppDefaultServiceDomain_Object = MibScalar
mlppDefaultServiceDomain = _MlppDefaultServiceDomain_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 6),
    _MlppDefaultServiceDomain_Type()
)
mlppDefaultServiceDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppDefaultServiceDomain.setStatus("current")


class _MlppNormalizedServiceDomain_Type(SnmpAdminString):
    """Custom type mlppNormalizedServiceDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_MlppNormalizedServiceDomain_Type.__name__ = "SnmpAdminString"
_MlppNormalizedServiceDomain_Object = MibScalar
mlppNormalizedServiceDomain = _MlppNormalizedServiceDomain_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 7),
    _MlppNormalizedServiceDomain_Type()
)
mlppNormalizedServiceDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppNormalizedServiceDomain.setStatus("current")


class _MlppRoutineRTPDSCP_Type(Integer32):
    """Custom type mlppRoutineRTPDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MlppRoutineRTPDSCP_Type.__name__ = "Integer32"
_MlppRoutineRTPDSCP_Object = MibScalar
mlppRoutineRTPDSCP = _MlppRoutineRTPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 8),
    _MlppRoutineRTPDSCP_Type()
)
mlppRoutineRTPDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppRoutineRTPDSCP.setStatus("current")


class _MlppPriorityRTPDSCP_Type(Integer32):
    """Custom type mlppPriorityRTPDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MlppPriorityRTPDSCP_Type.__name__ = "Integer32"
_MlppPriorityRTPDSCP_Object = MibScalar
mlppPriorityRTPDSCP = _MlppPriorityRTPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 9),
    _MlppPriorityRTPDSCP_Type()
)
mlppPriorityRTPDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppPriorityRTPDSCP.setStatus("current")


class _MlppImmediateRTPDSCP_Type(Integer32):
    """Custom type mlppImmediateRTPDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MlppImmediateRTPDSCP_Type.__name__ = "Integer32"
_MlppImmediateRTPDSCP_Object = MibScalar
mlppImmediateRTPDSCP = _MlppImmediateRTPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 10),
    _MlppImmediateRTPDSCP_Type()
)
mlppImmediateRTPDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppImmediateRTPDSCP.setStatus("current")


class _MlppFlashRTPDSCP_Type(Integer32):
    """Custom type mlppFlashRTPDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MlppFlashRTPDSCP_Type.__name__ = "Integer32"
_MlppFlashRTPDSCP_Object = MibScalar
mlppFlashRTPDSCP = _MlppFlashRTPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 11),
    _MlppFlashRTPDSCP_Type()
)
mlppFlashRTPDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppFlashRTPDSCP.setStatus("current")


class _MlppFlashOverRTPDSCP_Type(Integer32):
    """Custom type mlppFlashOverRTPDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MlppFlashOverRTPDSCP_Type.__name__ = "Integer32"
_MlppFlashOverRTPDSCP_Object = MibScalar
mlppFlashOverRTPDSCP = _MlppFlashOverRTPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 12),
    _MlppFlashOverRTPDSCP_Type()
)
mlppFlashOverRTPDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppFlashOverRTPDSCP.setStatus("current")


class _MlppFlashOverOverRTPDSCP_Type(Integer32):
    """Custom type mlppFlashOverOverRTPDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MlppFlashOverOverRTPDSCP_Type.__name__ = "Integer32"
_MlppFlashOverOverRTPDSCP_Object = MibScalar
mlppFlashOverOverRTPDSCP = _MlppFlashOverOverRTPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 13),
    _MlppFlashOverOverRTPDSCP_Type()
)
mlppFlashOverOverRTPDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppFlashOverOverRTPDSCP.setStatus("current")


class _MlppE911Behavior_Type(Integer32):
    """Custom type mlppE911Behavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("routineMode", 1),
          ("standardMode", 0))
    )


_MlppE911Behavior_Type.__name__ = "Integer32"
_MlppE911Behavior_Object = MibScalar
mlppE911Behavior = _MlppE911Behavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 29, 14),
    _MlppE911Behavior_Type()
)
mlppE911Behavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlppE911Behavior.setStatus("current")


class _DigitalGWPlayRBTOnISDNTransfer_Type(Integer32):
    """Custom type digitalGWPlayRBTOnISDNTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWPlayRBTOnISDNTransfer_Type.__name__ = "Integer32"
_DigitalGWPlayRBTOnISDNTransfer_Object = MibScalar
digitalGWPlayRBTOnISDNTransfer = _DigitalGWPlayRBTOnISDNTransfer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 3, 40),
    _DigitalGWPlayRBTOnISDNTransfer_Type()
)
digitalGWPlayRBTOnISDNTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWPlayRBTOnISDNTransfer.setStatus("current")
_AnalogGW_ObjectIdentity = ObjectIdentity
analogGW = _AnalogGW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4)
)


class _AnalogGWEnableReversalPolarity_Type(Integer32):
    """Custom type analogGWEnableReversalPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AnalogGWEnableReversalPolarity_Type.__name__ = "Integer32"
_AnalogGWEnableReversalPolarity_Object = MibScalar
analogGWEnableReversalPolarity = _AnalogGWEnableReversalPolarity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 1),
    _AnalogGWEnableReversalPolarity_Type()
)
analogGWEnableReversalPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogGWEnableReversalPolarity.setStatus("current")


class _AnalogGWEnableCurrentDisconnect_Type(Integer32):
    """Custom type analogGWEnableCurrentDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AnalogGWEnableCurrentDisconnect_Type.__name__ = "Integer32"
_AnalogGWEnableCurrentDisconnect_Object = MibScalar
analogGWEnableCurrentDisconnect = _AnalogGWEnableCurrentDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 2),
    _AnalogGWEnableCurrentDisconnect_Type()
)
analogGWEnableCurrentDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogGWEnableCurrentDisconnect.setStatus("current")


class _AnalogGWRegretTime_Type(Unsigned32):
    """Custom type analogGWRegretTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnalogGWRegretTime_Type.__name__ = "Unsigned32"
_AnalogGWRegretTime_Object = MibScalar
analogGWRegretTime = _AnalogGWRegretTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 3),
    _AnalogGWRegretTime_Type()
)
analogGWRegretTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogGWRegretTime.setStatus("current")


class _AnalogGWHotLineToneDuration_Type(Unsigned32):
    """Custom type analogGWHotLineToneDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AnalogGWHotLineToneDuration_Type.__name__ = "Unsigned32"
_AnalogGWHotLineToneDuration_Object = MibScalar
analogGWHotLineToneDuration = _AnalogGWHotLineToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 4),
    _AnalogGWHotLineToneDuration_Type()
)
analogGWHotLineToneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogGWHotLineToneDuration.setStatus("current")
_Fxs_ObjectIdentity = ObjectIdentity
fxs = _Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10)
)


class _FxsCutThrough_Type(Integer32):
    """Custom type fxsCutThrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FxsCutThrough_Type.__name__ = "Integer32"
_FxsCutThrough_Object = MibScalar
fxsCutThrough = _FxsCutThrough_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 1),
    _FxsCutThrough_Type()
)
fxsCutThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsCutThrough.setStatus("current")


class _FxsMeteringMode_Type(Integer32):
    """Custom type fxsMeteringMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("routingTable", 1))
    )


_FxsMeteringMode_Type.__name__ = "Integer32"
_FxsMeteringMode_Object = MibScalar
fxsMeteringMode = _FxsMeteringMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 2),
    _FxsMeteringMode_Type()
)
fxsMeteringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsMeteringMode.setStatus("current")


class _FxsFXSOOSBehavior_Type(Integer32):
    """Custom type fxsFXSOOSBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("currentDisconnect", 4),
          ("none", 0),
          ("polarityReversal", 2),
          ("reorderTone", 1))
    )


_FxsFXSOOSBehavior_Type.__name__ = "Integer32"
_FxsFXSOOSBehavior_Object = MibScalar
fxsFXSOOSBehavior = _FxsFXSOOSBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 3),
    _FxsFXSOOSBehavior_Type()
)
fxsFXSOOSBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsFXSOOSBehavior.setStatus("current")


class _FxsSetOOSOnRegistrationFail_Type(Integer32):
    """Custom type fxsSetOOSOnRegistrationFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FxsSetOOSOnRegistrationFail_Type.__name__ = "Integer32"
_FxsSetOOSOnRegistrationFail_Object = MibScalar
fxsSetOOSOnRegistrationFail = _FxsSetOOSOnRegistrationFail_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 4),
    _FxsSetOOSOnRegistrationFail_Type()
)
fxsSetOOSOnRegistrationFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsSetOOSOnRegistrationFail.setStatus("current")
_ChargeCodesTable_Object = MibTable
chargeCodesTable = _ChargeCodesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21)
)
if mibBuilder.loadTexts:
    chargeCodesTable.setStatus("current")
_ChargeCodesEntry_Object = MibTableRow
chargeCodesEntry = _ChargeCodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1)
)
chargeCodesEntry.setIndexNames(
    (0, "AcGateway", "chargeCodesIndex"),
)
if mibBuilder.loadTexts:
    chargeCodesEntry.setStatus("current")


class _ChargeCodesIndex_Type(Unsigned32):
    """Custom type chargeCodesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_ChargeCodesIndex_Type.__name__ = "Unsigned32"
_ChargeCodesIndex_Object = MibTableColumn
chargeCodesIndex = _ChargeCodesIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 1),
    _ChargeCodesIndex_Type()
)
chargeCodesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chargeCodesIndex.setStatus("current")
_ChargeCodesRowStatus_Type = RowStatus
_ChargeCodesRowStatus_Object = MibTableColumn
chargeCodesRowStatus = _ChargeCodesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 2),
    _ChargeCodesRowStatus_Type()
)
chargeCodesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesRowStatus.setStatus("current")


class _ChargeCodesAction_Type(Integer32):
    """Custom type chargeCodesAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ChargeCodesAction_Type.__name__ = "Integer32"
_ChargeCodesAction_Object = MibTableColumn
chargeCodesAction = _ChargeCodesAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 3),
    _ChargeCodesAction_Type()
)
chargeCodesAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeCodesAction.setStatus("current")


class _ChargeCodesActionResult_Type(Integer32):
    """Custom type chargeCodesActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ChargeCodesActionResult_Type.__name__ = "Integer32"
_ChargeCodesActionResult_Object = MibTableColumn
chargeCodesActionResult = _ChargeCodesActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 4),
    _ChargeCodesActionResult_Type()
)
chargeCodesActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeCodesActionResult.setStatus("current")


class _ChargeCodesPeriod1EndTime_Type(Unsigned32):
    """Custom type chargeCodesPeriod1EndTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChargeCodesPeriod1EndTime_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod1EndTime_Object = MibTableColumn
chargeCodesPeriod1EndTime = _ChargeCodesPeriod1EndTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 5),
    _ChargeCodesPeriod1EndTime_Type()
)
chargeCodesPeriod1EndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod1EndTime.setStatus("current")


class _ChargeCodesPeriod1PulseInterval_Type(Unsigned32):
    """Custom type chargeCodesPeriod1PulseInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_ChargeCodesPeriod1PulseInterval_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod1PulseInterval_Object = MibTableColumn
chargeCodesPeriod1PulseInterval = _ChargeCodesPeriod1PulseInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 6),
    _ChargeCodesPeriod1PulseInterval_Type()
)
chargeCodesPeriod1PulseInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod1PulseInterval.setStatus("current")


class _ChargeCodesPeriod1PulsesOnAnswer_Type(Unsigned32):
    """Custom type chargeCodesPeriod1PulsesOnAnswer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChargeCodesPeriod1PulsesOnAnswer_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod1PulsesOnAnswer_Object = MibTableColumn
chargeCodesPeriod1PulsesOnAnswer = _ChargeCodesPeriod1PulsesOnAnswer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 7),
    _ChargeCodesPeriod1PulsesOnAnswer_Type()
)
chargeCodesPeriod1PulsesOnAnswer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod1PulsesOnAnswer.setStatus("current")


class _ChargeCodesPeriod2EndTime_Type(Unsigned32):
    """Custom type chargeCodesPeriod2EndTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChargeCodesPeriod2EndTime_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod2EndTime_Object = MibTableColumn
chargeCodesPeriod2EndTime = _ChargeCodesPeriod2EndTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 8),
    _ChargeCodesPeriod2EndTime_Type()
)
chargeCodesPeriod2EndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod2EndTime.setStatus("current")


class _ChargeCodesPeriod2PulseInterval_Type(Unsigned32):
    """Custom type chargeCodesPeriod2PulseInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_ChargeCodesPeriod2PulseInterval_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod2PulseInterval_Object = MibTableColumn
chargeCodesPeriod2PulseInterval = _ChargeCodesPeriod2PulseInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 9),
    _ChargeCodesPeriod2PulseInterval_Type()
)
chargeCodesPeriod2PulseInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod2PulseInterval.setStatus("current")


class _ChargeCodesPeriod2PulsesOnAnswer_Type(Unsigned32):
    """Custom type chargeCodesPeriod2PulsesOnAnswer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChargeCodesPeriod2PulsesOnAnswer_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod2PulsesOnAnswer_Object = MibTableColumn
chargeCodesPeriod2PulsesOnAnswer = _ChargeCodesPeriod2PulsesOnAnswer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 10),
    _ChargeCodesPeriod2PulsesOnAnswer_Type()
)
chargeCodesPeriod2PulsesOnAnswer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod2PulsesOnAnswer.setStatus("current")


class _ChargeCodesPeriod3EndTime_Type(Unsigned32):
    """Custom type chargeCodesPeriod3EndTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChargeCodesPeriod3EndTime_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod3EndTime_Object = MibTableColumn
chargeCodesPeriod3EndTime = _ChargeCodesPeriod3EndTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 11),
    _ChargeCodesPeriod3EndTime_Type()
)
chargeCodesPeriod3EndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod3EndTime.setStatus("current")


class _ChargeCodesPeriod3PulseInterval_Type(Unsigned32):
    """Custom type chargeCodesPeriod3PulseInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_ChargeCodesPeriod3PulseInterval_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod3PulseInterval_Object = MibTableColumn
chargeCodesPeriod3PulseInterval = _ChargeCodesPeriod3PulseInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 12),
    _ChargeCodesPeriod3PulseInterval_Type()
)
chargeCodesPeriod3PulseInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod3PulseInterval.setStatus("current")


class _ChargeCodesPeriod3PulsesOnAnswer_Type(Unsigned32):
    """Custom type chargeCodesPeriod3PulsesOnAnswer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChargeCodesPeriod3PulsesOnAnswer_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod3PulsesOnAnswer_Object = MibTableColumn
chargeCodesPeriod3PulsesOnAnswer = _ChargeCodesPeriod3PulsesOnAnswer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 13),
    _ChargeCodesPeriod3PulsesOnAnswer_Type()
)
chargeCodesPeriod3PulsesOnAnswer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod3PulsesOnAnswer.setStatus("current")


class _ChargeCodesPeriod4EndTime_Type(Unsigned32):
    """Custom type chargeCodesPeriod4EndTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChargeCodesPeriod4EndTime_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod4EndTime_Object = MibTableColumn
chargeCodesPeriod4EndTime = _ChargeCodesPeriod4EndTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 14),
    _ChargeCodesPeriod4EndTime_Type()
)
chargeCodesPeriod4EndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod4EndTime.setStatus("current")


class _ChargeCodesPeriod4PulseInterval_Type(Unsigned32):
    """Custom type chargeCodesPeriod4PulseInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_ChargeCodesPeriod4PulseInterval_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod4PulseInterval_Object = MibTableColumn
chargeCodesPeriod4PulseInterval = _ChargeCodesPeriod4PulseInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 15),
    _ChargeCodesPeriod4PulseInterval_Type()
)
chargeCodesPeriod4PulseInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod4PulseInterval.setStatus("current")


class _ChargeCodesPeriod4PulsesOnAnswer_Type(Unsigned32):
    """Custom type chargeCodesPeriod4PulsesOnAnswer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChargeCodesPeriod4PulsesOnAnswer_Type.__name__ = "Unsigned32"
_ChargeCodesPeriod4PulsesOnAnswer_Object = MibTableColumn
chargeCodesPeriod4PulsesOnAnswer = _ChargeCodesPeriod4PulsesOnAnswer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 21, 1, 16),
    _ChargeCodesPeriod4PulsesOnAnswer_Type()
)
chargeCodesPeriod4PulsesOnAnswer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chargeCodesPeriod4PulsesOnAnswer.setStatus("current")
_ToneIndexTable_Object = MibTable
toneIndexTable = _ToneIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 22)
)
if mibBuilder.loadTexts:
    toneIndexTable.setStatus("current")
_ToneIndexEntry_Object = MibTableRow
toneIndexEntry = _ToneIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 22, 1)
)
toneIndexEntry.setIndexNames(
    (0, "AcGateway", "toneIndexIndex"),
)
if mibBuilder.loadTexts:
    toneIndexEntry.setStatus("current")


class _ToneIndexIndex_Type(Unsigned32):
    """Custom type toneIndexIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_ToneIndexIndex_Type.__name__ = "Unsigned32"
_ToneIndexIndex_Object = MibTableColumn
toneIndexIndex = _ToneIndexIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 22, 1, 1),
    _ToneIndexIndex_Type()
)
toneIndexIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    toneIndexIndex.setStatus("current")
_ToneIndexRowStatus_Type = RowStatus
_ToneIndexRowStatus_Object = MibTableColumn
toneIndexRowStatus = _ToneIndexRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 22, 1, 2),
    _ToneIndexRowStatus_Type()
)
toneIndexRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    toneIndexRowStatus.setStatus("current")


class _ToneIndexAction_Type(Integer32):
    """Custom type toneIndexAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ToneIndexAction_Type.__name__ = "Integer32"
_ToneIndexAction_Object = MibTableColumn
toneIndexAction = _ToneIndexAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 22, 1, 3),
    _ToneIndexAction_Type()
)
toneIndexAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toneIndexAction.setStatus("current")


class _ToneIndexActionResult_Type(Integer32):
    """Custom type toneIndexActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ToneIndexActionResult_Type.__name__ = "Integer32"
_ToneIndexActionResult_Object = MibTableColumn
toneIndexActionResult = _ToneIndexActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 22, 1, 4),
    _ToneIndexActionResult_Type()
)
toneIndexActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    toneIndexActionResult.setStatus("current")


class _ToneIndexFXSPortFirst_Type(Unsigned32):
    """Custom type toneIndexFXSPortFirst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_ToneIndexFXSPortFirst_Type.__name__ = "Unsigned32"
_ToneIndexFXSPortFirst_Object = MibTableColumn
toneIndexFXSPortFirst = _ToneIndexFXSPortFirst_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 22, 1, 5),
    _ToneIndexFXSPortFirst_Type()
)
toneIndexFXSPortFirst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    toneIndexFXSPortFirst.setStatus("current")


class _ToneIndexFXSPortLast_Type(Unsigned32):
    """Custom type toneIndexFXSPortLast based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_ToneIndexFXSPortLast_Type.__name__ = "Unsigned32"
_ToneIndexFXSPortLast_Object = MibTableColumn
toneIndexFXSPortLast = _ToneIndexFXSPortLast_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 22, 1, 6),
    _ToneIndexFXSPortLast_Type()
)
toneIndexFXSPortLast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    toneIndexFXSPortLast.setStatus("current")


class _ToneIndexSourcePrefix_Type(SnmpAdminString):
    """Custom type toneIndexSourcePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_ToneIndexSourcePrefix_Type.__name__ = "SnmpAdminString"
_ToneIndexSourcePrefix_Object = MibTableColumn
toneIndexSourcePrefix = _ToneIndexSourcePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 22, 1, 7),
    _ToneIndexSourcePrefix_Type()
)
toneIndexSourcePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    toneIndexSourcePrefix.setStatus("current")


class _ToneIndexPriorityIndex_Type(Unsigned32):
    """Custom type toneIndexPriorityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ToneIndexPriorityIndex_Type.__name__ = "Unsigned32"
_ToneIndexPriorityIndex_Object = MibTableColumn
toneIndexPriorityIndex = _ToneIndexPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 10, 22, 1, 8),
    _ToneIndexPriorityIndex_Type()
)
toneIndexPriorityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    toneIndexPriorityIndex.setStatus("current")
_Fxo_ObjectIdentity = ObjectIdentity
fxo = _Fxo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 11)
)


class _FxoIsTwoStageDial_Type(Integer32):
    """Custom type fxoIsTwoStageDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oneStage", 0),
          ("twoStages", 1))
    )


_FxoIsTwoStageDial_Type.__name__ = "Integer32"
_FxoIsTwoStageDial_Object = MibScalar
fxoIsTwoStageDial = _FxoIsTwoStageDial_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 11, 1),
    _FxoIsTwoStageDial_Type()
)
fxoIsTwoStageDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoIsTwoStageDial.setStatus("current")


class _FxoWaitForDialTone_Type(Integer32):
    """Custom type fxoWaitForDialTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FxoWaitForDialTone_Type.__name__ = "Integer32"
_FxoWaitForDialTone_Object = MibScalar
fxoWaitForDialTone = _FxoWaitForDialTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 11, 2),
    _FxoWaitForDialTone_Type()
)
fxoWaitForDialTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoWaitForDialTone.setStatus("current")


class _FxoWaitForDialTime_Type(Unsigned32):
    """Custom type fxoWaitForDialTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000000),
    )


_FxoWaitForDialTime_Type.__name__ = "Unsigned32"
_FxoWaitForDialTime_Object = MibScalar
fxoWaitForDialTime = _FxoWaitForDialTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 11, 3),
    _FxoWaitForDialTime_Type()
)
fxoWaitForDialTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoWaitForDialTime.setStatus("current")


class _FxoBetweenRingTime_Type(Unsigned32):
    """Custom type fxoBetweenRingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000000),
    )


_FxoBetweenRingTime_Type.__name__ = "Unsigned32"
_FxoBetweenRingTime_Object = MibScalar
fxoBetweenRingTime = _FxoBetweenRingTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 11, 4),
    _FxoBetweenRingTime_Type()
)
fxoBetweenRingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoBetweenRingTime.setStatus("current")


class _FxoEnableVoiceDetection_Type(Integer32):
    """Custom type fxoEnableVoiceDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FxoEnableVoiceDetection_Type.__name__ = "Integer32"
_FxoEnableVoiceDetection_Object = MibScalar
fxoEnableVoiceDetection = _FxoEnableVoiceDetection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 11, 5),
    _FxoEnableVoiceDetection_Type()
)
fxoEnableVoiceDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoEnableVoiceDetection.setStatus("current")


class _FxoRingsBeforeCallerID_Type(Unsigned32):
    """Custom type fxoRingsBeforeCallerID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FxoRingsBeforeCallerID_Type.__name__ = "Unsigned32"
_FxoRingsBeforeCallerID_Object = MibScalar
fxoRingsBeforeCallerID = _FxoRingsBeforeCallerID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 11, 6),
    _FxoRingsBeforeCallerID_Type()
)
fxoRingsBeforeCallerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoRingsBeforeCallerID.setStatus("current")


class _FxoGuardTimeBetweenCalls_Type(Unsigned32):
    """Custom type fxoGuardTimeBetweenCalls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FxoGuardTimeBetweenCalls_Type.__name__ = "Unsigned32"
_FxoGuardTimeBetweenCalls_Object = MibScalar
fxoGuardTimeBetweenCalls = _FxoGuardTimeBetweenCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 11, 7),
    _FxoGuardTimeBetweenCalls_Type()
)
fxoGuardTimeBetweenCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoGuardTimeBetweenCalls.setStatus("current")


class _FxoAutoDialPlayBusyTone_Type(Integer32):
    """Custom type fxoAutoDialPlayBusyTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FxoAutoDialPlayBusyTone_Type.__name__ = "Integer32"
_FxoAutoDialPlayBusyTone_Object = MibScalar
fxoAutoDialPlayBusyTone = _FxoAutoDialPlayBusyTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 11, 8),
    _FxoAutoDialPlayBusyTone_Type()
)
fxoAutoDialPlayBusyTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoAutoDialPlayBusyTone.setStatus("current")
_Dialing_ObjectIdentity = ObjectIdentity
dialing = _Dialing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12)
)


class _DialingMaxDigits_Type(Unsigned32):
    """Custom type dialingMaxDigits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 49),
    )


_DialingMaxDigits_Type.__name__ = "Unsigned32"
_DialingMaxDigits_Object = MibScalar
dialingMaxDigits = _DialingMaxDigits_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 1),
    _DialingMaxDigits_Type()
)
dialingMaxDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialingMaxDigits.setStatus("current")


class _DialingTimeBetweenDigits_Type(Unsigned32):
    """Custom type dialingTimeBetweenDigits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DialingTimeBetweenDigits_Type.__name__ = "Unsigned32"
_DialingTimeBetweenDigits_Object = MibScalar
dialingTimeBetweenDigits = _DialingTimeBetweenDigits_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 2),
    _DialingTimeBetweenDigits_Type()
)
dialingTimeBetweenDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialingTimeBetweenDigits.setStatus("current")


class _DialingIsSpecialDigits_Type(Integer32):
    """Custom type dialingIsSpecialDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DialingIsSpecialDigits_Type.__name__ = "Integer32"
_DialingIsSpecialDigits_Object = MibScalar
dialingIsSpecialDigits = _DialingIsSpecialDigits_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 3),
    _DialingIsSpecialDigits_Type()
)
dialingIsSpecialDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialingIsSpecialDigits.setStatus("current")


class _DialingDigitMapping_Type(SnmpAdminString):
    """Custom type dialingDigitMapping based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 152),
    )


_DialingDigitMapping_Type.__name__ = "SnmpAdminString"
_DialingDigitMapping_Object = MibScalar
dialingDigitMapping = _DialingDigitMapping_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 4),
    _DialingDigitMapping_Type()
)
dialingDigitMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialingDigitMapping.setStatus("current")


class _DialingEnableDigitDelivery_Type(Integer32):
    """Custom type dialingEnableDigitDelivery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DialingEnableDigitDelivery_Type.__name__ = "Integer32"
_DialingEnableDigitDelivery_Object = MibScalar
dialingEnableDigitDelivery = _DialingEnableDigitDelivery_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 5),
    _DialingEnableDigitDelivery_Type()
)
dialingEnableDigitDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialingEnableDigitDelivery.setStatus("current")


class _DialingDialPlanIndex_Type(Integer32):
    """Custom type dialingDialPlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_DialingDialPlanIndex_Type.__name__ = "Integer32"
_DialingDialPlanIndex_Object = MibScalar
dialingDialPlanIndex = _DialingDialPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 6),
    _DialingDialPlanIndex_Type()
)
dialingDialPlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialingDialPlanIndex.setStatus("current")
_AutoDialTable_Object = MibTable
autoDialTable = _AutoDialTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 21)
)
if mibBuilder.loadTexts:
    autoDialTable.setStatus("current")
_AutoDialEntry_Object = MibTableRow
autoDialEntry = _AutoDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 21, 1)
)
autoDialEntry.setIndexNames(
    (0, "AcGateway", "autoDialIndex"),
)
if mibBuilder.loadTexts:
    autoDialEntry.setStatus("current")


class _AutoDialIndex_Type(Unsigned32):
    """Custom type autoDialIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AutoDialIndex_Type.__name__ = "Unsigned32"
_AutoDialIndex_Object = MibTableColumn
autoDialIndex = _AutoDialIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 21, 1, 1),
    _AutoDialIndex_Type()
)
autoDialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoDialIndex.setStatus("current")


class _AutoDialIsUsed_Type(Integer32):
    """Custom type autoDialIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AutoDialIsUsed_Type.__name__ = "Integer32"
_AutoDialIsUsed_Object = MibTableColumn
autoDialIsUsed = _AutoDialIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 21, 1, 2),
    _AutoDialIsUsed_Type()
)
autoDialIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoDialIsUsed.setStatus("current")


class _AutoDialAction_Type(Integer32):
    """Custom type autoDialAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_AutoDialAction_Type.__name__ = "Integer32"
_AutoDialAction_Object = MibTableColumn
autoDialAction = _AutoDialAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 21, 1, 3),
    _AutoDialAction_Type()
)
autoDialAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoDialAction.setStatus("current")


class _AutoDialActionResult_Type(Integer32):
    """Custom type autoDialActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_AutoDialActionResult_Type.__name__ = "Integer32"
_AutoDialActionResult_Object = MibTableColumn
autoDialActionResult = _AutoDialActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 21, 1, 4),
    _AutoDialActionResult_Type()
)
autoDialActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoDialActionResult.setStatus("current")


class _AutoDialDestPhoneNumber_Type(SnmpAdminString):
    """Custom type autoDialDestPhoneNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AutoDialDestPhoneNumber_Type.__name__ = "SnmpAdminString"
_AutoDialDestPhoneNumber_Object = MibTableColumn
autoDialDestPhoneNumber = _AutoDialDestPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 21, 1, 5),
    _AutoDialDestPhoneNumber_Type()
)
autoDialDestPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoDialDestPhoneNumber.setStatus("current")


class _AutoDialType_Type(Integer32):
    """Custom type autoDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoDial", 1),
          ("delayHotLine", 2),
          ("none", 0))
    )


_AutoDialType_Type.__name__ = "Integer32"
_AutoDialType_Object = MibTableColumn
autoDialType = _AutoDialType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 21, 1, 6),
    _AutoDialType_Type()
)
autoDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoDialType.setStatus("current")


class _AutoDialModule_Type(Unsigned32):
    """Custom type autoDialModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AutoDialModule_Type.__name__ = "Unsigned32"
_AutoDialModule_Object = MibTableColumn
autoDialModule = _AutoDialModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 21, 1, 7),
    _AutoDialModule_Type()
)
autoDialModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoDialModule.setStatus("current")


class _AutoDialPort_Type(Unsigned32):
    """Custom type autoDialPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AutoDialPort_Type.__name__ = "Unsigned32"
_AutoDialPort_Object = MibTableColumn
autoDialPort = _AutoDialPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 12, 21, 1, 8),
    _AutoDialPort_Type()
)
autoDialPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoDialPort.setStatus("current")
_CallerID_ObjectIdentity = ObjectIdentity
callerID = _CallerID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13)
)


class _CallerIDEnable_Type(Integer32):
    """Custom type callerIDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CallerIDEnable_Type.__name__ = "Integer32"
_CallerIDEnable_Object = MibScalar
callerIDEnable = _CallerIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 1),
    _CallerIDEnable_Type()
)
callerIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callerIDEnable.setStatus("current")
_CallerDisplayTable_Object = MibTable
callerDisplayTable = _CallerDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 21)
)
if mibBuilder.loadTexts:
    callerDisplayTable.setStatus("current")
_CallerDisplayEntry_Object = MibTableRow
callerDisplayEntry = _CallerDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 21, 1)
)
callerDisplayEntry.setIndexNames(
    (0, "AcGateway", "callerDisplayIndex"),
)
if mibBuilder.loadTexts:
    callerDisplayEntry.setStatus("current")


class _CallerDisplayIndex_Type(Unsigned32):
    """Custom type callerDisplayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CallerDisplayIndex_Type.__name__ = "Unsigned32"
_CallerDisplayIndex_Object = MibTableColumn
callerDisplayIndex = _CallerDisplayIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 21, 1, 1),
    _CallerDisplayIndex_Type()
)
callerDisplayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerDisplayIndex.setStatus("current")


class _CallerDisplayIsUsed_Type(Integer32):
    """Custom type callerDisplayIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CallerDisplayIsUsed_Type.__name__ = "Integer32"
_CallerDisplayIsUsed_Object = MibTableColumn
callerDisplayIsUsed = _CallerDisplayIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 21, 1, 2),
    _CallerDisplayIsUsed_Type()
)
callerDisplayIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callerDisplayIsUsed.setStatus("current")


class _CallerDisplayAction_Type(Integer32):
    """Custom type callerDisplayAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_CallerDisplayAction_Type.__name__ = "Integer32"
_CallerDisplayAction_Object = MibTableColumn
callerDisplayAction = _CallerDisplayAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 21, 1, 3),
    _CallerDisplayAction_Type()
)
callerDisplayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerDisplayAction.setStatus("current")


class _CallerDisplayActionResult_Type(Integer32):
    """Custom type callerDisplayActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_CallerDisplayActionResult_Type.__name__ = "Integer32"
_CallerDisplayActionResult_Object = MibTableColumn
callerDisplayActionResult = _CallerDisplayActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 21, 1, 4),
    _CallerDisplayActionResult_Type()
)
callerDisplayActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerDisplayActionResult.setStatus("current")


class _CallerDisplayCallerDisplay_Type(SnmpAdminString):
    """Custom type callerDisplayCallerDisplay based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CallerDisplayCallerDisplay_Type.__name__ = "SnmpAdminString"
_CallerDisplayCallerDisplay_Object = MibTableColumn
callerDisplayCallerDisplay = _CallerDisplayCallerDisplay_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 21, 1, 5),
    _CallerDisplayCallerDisplay_Type()
)
callerDisplayCallerDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callerDisplayCallerDisplay.setStatus("current")


class _CallerDisplayRestriction_Type(Integer32):
    """Custom type callerDisplayRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("notBlocked", 0))
    )


_CallerDisplayRestriction_Type.__name__ = "Integer32"
_CallerDisplayRestriction_Object = MibTableColumn
callerDisplayRestriction = _CallerDisplayRestriction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 21, 1, 6),
    _CallerDisplayRestriction_Type()
)
callerDisplayRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callerDisplayRestriction.setStatus("current")


class _CallerDisplayModule_Type(Unsigned32):
    """Custom type callerDisplayModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CallerDisplayModule_Type.__name__ = "Unsigned32"
_CallerDisplayModule_Object = MibTableColumn
callerDisplayModule = _CallerDisplayModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 21, 1, 7),
    _CallerDisplayModule_Type()
)
callerDisplayModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerDisplayModule.setStatus("current")


class _CallerDisplayPort_Type(Unsigned32):
    """Custom type callerDisplayPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CallerDisplayPort_Type.__name__ = "Unsigned32"
_CallerDisplayPort_Object = MibTableColumn
callerDisplayPort = _CallerDisplayPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 21, 1, 8),
    _CallerDisplayPort_Type()
)
callerDisplayPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerDisplayPort.setStatus("current")
_CallerIDperPortTable_Object = MibTable
callerIDperPortTable = _CallerIDperPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 22)
)
if mibBuilder.loadTexts:
    callerIDperPortTable.setStatus("current")
_CallerIDperPortEntry_Object = MibTableRow
callerIDperPortEntry = _CallerIDperPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 22, 1)
)
callerIDperPortEntry.setIndexNames(
    (0, "AcGateway", "callerIDperPortIndex"),
)
if mibBuilder.loadTexts:
    callerIDperPortEntry.setStatus("current")


class _CallerIDperPortIndex_Type(Unsigned32):
    """Custom type callerIDperPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CallerIDperPortIndex_Type.__name__ = "Unsigned32"
_CallerIDperPortIndex_Object = MibTableColumn
callerIDperPortIndex = _CallerIDperPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 22, 1, 1),
    _CallerIDperPortIndex_Type()
)
callerIDperPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerIDperPortIndex.setStatus("current")


class _CallerIDperPortIsUsed_Type(Integer32):
    """Custom type callerIDperPortIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CallerIDperPortIsUsed_Type.__name__ = "Integer32"
_CallerIDperPortIsUsed_Object = MibTableColumn
callerIDperPortIsUsed = _CallerIDperPortIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 22, 1, 2),
    _CallerIDperPortIsUsed_Type()
)
callerIDperPortIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callerIDperPortIsUsed.setStatus("current")


class _CallerIDperPortAction_Type(Integer32):
    """Custom type callerIDperPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_CallerIDperPortAction_Type.__name__ = "Integer32"
_CallerIDperPortAction_Object = MibTableColumn
callerIDperPortAction = _CallerIDperPortAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 22, 1, 3),
    _CallerIDperPortAction_Type()
)
callerIDperPortAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerIDperPortAction.setStatus("current")


class _CallerIDperPortActionResult_Type(Integer32):
    """Custom type callerIDperPortActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_CallerIDperPortActionResult_Type.__name__ = "Integer32"
_CallerIDperPortActionResult_Object = MibTableColumn
callerIDperPortActionResult = _CallerIDperPortActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 22, 1, 4),
    _CallerIDperPortActionResult_Type()
)
callerIDperPortActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerIDperPortActionResult.setStatus("current")


class _CallerIDperPortEnable_Type(Integer32):
    """Custom type callerIDperPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("valueNotSet", 255))
    )


_CallerIDperPortEnable_Type.__name__ = "Integer32"
_CallerIDperPortEnable_Object = MibTableColumn
callerIDperPortEnable = _CallerIDperPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 22, 1, 5),
    _CallerIDperPortEnable_Type()
)
callerIDperPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callerIDperPortEnable.setStatus("current")


class _CallerIDperPortModule_Type(Unsigned32):
    """Custom type callerIDperPortModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CallerIDperPortModule_Type.__name__ = "Unsigned32"
_CallerIDperPortModule_Object = MibTableColumn
callerIDperPortModule = _CallerIDperPortModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 22, 1, 6),
    _CallerIDperPortModule_Type()
)
callerIDperPortModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerIDperPortModule.setStatus("current")


class _CallerIDperPortPort_Type(Unsigned32):
    """Custom type callerIDperPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CallerIDperPortPort_Type.__name__ = "Unsigned32"
_CallerIDperPortPort_Object = MibTableColumn
callerIDperPortPort = _CallerIDperPortPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 13, 22, 1, 7),
    _CallerIDperPortPort_Type()
)
callerIDperPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callerIDperPortPort.setStatus("current")
_KeypadFeatures_ObjectIdentity = ObjectIdentity
keypadFeatures = _KeypadFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14)
)


class _KeypadFeaturesCFUncond_Type(SnmpAdminString):
    """Custom type keypadFeaturesCFUncond based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesCFUncond_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesCFUncond_Object = MibScalar
keypadFeaturesCFUncond = _KeypadFeaturesCFUncond_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 1),
    _KeypadFeaturesCFUncond_Type()
)
keypadFeaturesCFUncond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesCFUncond.setStatus("current")


class _KeypadFeaturesCFDeact_Type(SnmpAdminString):
    """Custom type keypadFeaturesCFDeact based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesCFDeact_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesCFDeact_Object = MibScalar
keypadFeaturesCFDeact = _KeypadFeaturesCFDeact_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 2),
    _KeypadFeaturesCFDeact_Type()
)
keypadFeaturesCFDeact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesCFDeact.setStatus("current")


class _KeypadFeaturesCFNoAnswer_Type(SnmpAdminString):
    """Custom type keypadFeaturesCFNoAnswer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesCFNoAnswer_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesCFNoAnswer_Object = MibScalar
keypadFeaturesCFNoAnswer = _KeypadFeaturesCFNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 3),
    _KeypadFeaturesCFNoAnswer_Type()
)
keypadFeaturesCFNoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesCFNoAnswer.setStatus("current")


class _KeypadFeaturesCFBusy_Type(SnmpAdminString):
    """Custom type keypadFeaturesCFBusy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesCFBusy_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesCFBusy_Object = MibScalar
keypadFeaturesCFBusy = _KeypadFeaturesCFBusy_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 4),
    _KeypadFeaturesCFBusy_Type()
)
keypadFeaturesCFBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesCFBusy.setStatus("current")


class _KeypadFeaturesCLIR_Type(SnmpAdminString):
    """Custom type keypadFeaturesCLIR based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesCLIR_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesCLIR_Object = MibScalar
keypadFeaturesCLIR = _KeypadFeaturesCLIR_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 5),
    _KeypadFeaturesCLIR_Type()
)
keypadFeaturesCLIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesCLIR.setStatus("current")


class _KeypadFeaturesCLIRDeact_Type(SnmpAdminString):
    """Custom type keypadFeaturesCLIRDeact based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesCLIRDeact_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesCLIRDeact_Object = MibScalar
keypadFeaturesCLIRDeact = _KeypadFeaturesCLIRDeact_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 6),
    _KeypadFeaturesCLIRDeact_Type()
)
keypadFeaturesCLIRDeact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesCLIRDeact.setStatus("current")


class _KeypadFeaturesHotLine_Type(SnmpAdminString):
    """Custom type keypadFeaturesHotLine based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesHotLine_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesHotLine_Object = MibScalar
keypadFeaturesHotLine = _KeypadFeaturesHotLine_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 7),
    _KeypadFeaturesHotLine_Type()
)
keypadFeaturesHotLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesHotLine.setStatus("current")


class _KeypadFeaturesHotLineDeact_Type(SnmpAdminString):
    """Custom type keypadFeaturesHotLineDeact based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesHotLineDeact_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesHotLineDeact_Object = MibScalar
keypadFeaturesHotLineDeact = _KeypadFeaturesHotLineDeact_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 8),
    _KeypadFeaturesHotLineDeact_Type()
)
keypadFeaturesHotLineDeact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesHotLineDeact.setStatus("current")


class _KeypadFeaturesCFBusyOrNoAnswer_Type(SnmpAdminString):
    """Custom type keypadFeaturesCFBusyOrNoAnswer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesCFBusyOrNoAnswer_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesCFBusyOrNoAnswer_Object = MibScalar
keypadFeaturesCFBusyOrNoAnswer = _KeypadFeaturesCFBusyOrNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 9),
    _KeypadFeaturesCFBusyOrNoAnswer_Type()
)
keypadFeaturesCFBusyOrNoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesCFBusyOrNoAnswer.setStatus("current")


class _KeypadFeaturesCFDoNotDisturb_Type(SnmpAdminString):
    """Custom type keypadFeaturesCFDoNotDisturb based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesCFDoNotDisturb_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesCFDoNotDisturb_Object = MibScalar
keypadFeaturesCFDoNotDisturb = _KeypadFeaturesCFDoNotDisturb_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 10),
    _KeypadFeaturesCFDoNotDisturb_Type()
)
keypadFeaturesCFDoNotDisturb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesCFDoNotDisturb.setStatus("current")


class _KeypadFeaturesBlindTransfer_Type(SnmpAdminString):
    """Custom type keypadFeaturesBlindTransfer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesBlindTransfer_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesBlindTransfer_Object = MibScalar
keypadFeaturesBlindTransfer = _KeypadFeaturesBlindTransfer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 11),
    _KeypadFeaturesBlindTransfer_Type()
)
keypadFeaturesBlindTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesBlindTransfer.setStatus("current")


class _KeypadFeaturesKeypadFeaturesCW_Type(SnmpAdminString):
    """Custom type keypadFeaturesKeypadFeaturesCW based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesKeypadFeaturesCW_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesKeypadFeaturesCW_Object = MibScalar
keypadFeaturesKeypadFeaturesCW = _KeypadFeaturesKeypadFeaturesCW_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 12),
    _KeypadFeaturesKeypadFeaturesCW_Type()
)
keypadFeaturesKeypadFeaturesCW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesKeypadFeaturesCW.setStatus("current")


class _KeypadFeaturesKeypadFeaturesCWDeact_Type(SnmpAdminString):
    """Custom type keypadFeaturesKeypadFeaturesCWDeact based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesKeypadFeaturesCWDeact_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesKeypadFeaturesCWDeact_Object = MibScalar
keypadFeaturesKeypadFeaturesCWDeact = _KeypadFeaturesKeypadFeaturesCWDeact_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 13),
    _KeypadFeaturesKeypadFeaturesCWDeact_Type()
)
keypadFeaturesKeypadFeaturesCWDeact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesKeypadFeaturesCWDeact.setStatus("current")


class _KeypadFeaturesRejectAnonymousCall_Type(SnmpAdminString):
    """Custom type keypadFeaturesRejectAnonymousCall based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesRejectAnonymousCall_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesRejectAnonymousCall_Object = MibScalar
keypadFeaturesRejectAnonymousCall = _KeypadFeaturesRejectAnonymousCall_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 14),
    _KeypadFeaturesRejectAnonymousCall_Type()
)
keypadFeaturesRejectAnonymousCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesRejectAnonymousCall.setStatus("current")


class _KeypadFeaturesRejectAnonymousCallDeact_Type(SnmpAdminString):
    """Custom type keypadFeaturesRejectAnonymousCallDeact based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KeypadFeaturesRejectAnonymousCallDeact_Type.__name__ = "SnmpAdminString"
_KeypadFeaturesRejectAnonymousCallDeact_Object = MibScalar
keypadFeaturesRejectAnonymousCallDeact = _KeypadFeaturesRejectAnonymousCallDeact_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 14, 15),
    _KeypadFeaturesRejectAnonymousCallDeact_Type()
)
keypadFeaturesRejectAnonymousCallDeact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypadFeaturesRejectAnonymousCallDeact.setStatus("current")
_PortName_ObjectIdentity = ObjectIdentity
portName = _PortName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 15)
)
_NamesTable_Object = MibTable
namesTable = _NamesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 15, 21)
)
if mibBuilder.loadTexts:
    namesTable.setStatus("current")
_NamesEntry_Object = MibTableRow
namesEntry = _NamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 15, 21, 1)
)
namesEntry.setIndexNames(
    (0, "AcGateway", "namesIndex"),
)
if mibBuilder.loadTexts:
    namesEntry.setStatus("current")


class _NamesIndex_Type(Unsigned32):
    """Custom type namesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_NamesIndex_Type.__name__ = "Unsigned32"
_NamesIndex_Object = MibTableColumn
namesIndex = _NamesIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 15, 21, 1, 1),
    _NamesIndex_Type()
)
namesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namesIndex.setStatus("current")


class _NamesIsUsed_Type(Integer32):
    """Custom type namesIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NamesIsUsed_Type.__name__ = "Integer32"
_NamesIsUsed_Object = MibTableColumn
namesIsUsed = _NamesIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 15, 21, 1, 2),
    _NamesIsUsed_Type()
)
namesIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namesIsUsed.setStatus("current")


class _NamesAction_Type(Integer32):
    """Custom type namesAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_NamesAction_Type.__name__ = "Integer32"
_NamesAction_Object = MibTableColumn
namesAction = _NamesAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 15, 21, 1, 3),
    _NamesAction_Type()
)
namesAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namesAction.setStatus("current")


class _NamesActionResult_Type(Integer32):
    """Custom type namesActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_NamesActionResult_Type.__name__ = "Integer32"
_NamesActionResult_Object = MibTableColumn
namesActionResult = _NamesActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 15, 21, 1, 4),
    _NamesActionResult_Type()
)
namesActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namesActionResult.setStatus("current")


class _NamesPortName_Type(SnmpAdminString):
    """Custom type namesPortName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NamesPortName_Type.__name__ = "SnmpAdminString"
_NamesPortName_Object = MibTableColumn
namesPortName = _NamesPortName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 15, 21, 1, 5),
    _NamesPortName_Type()
)
namesPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namesPortName.setStatus("current")


class _NamesModule_Type(Unsigned32):
    """Custom type namesModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NamesModule_Type.__name__ = "Unsigned32"
_NamesModule_Object = MibTableColumn
namesModule = _NamesModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 15, 21, 1, 6),
    _NamesModule_Type()
)
namesModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namesModule.setStatus("current")


class _NamesPort_Type(Unsigned32):
    """Custom type namesPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NamesPort_Type.__name__ = "Unsigned32"
_NamesPort_Object = MibTableColumn
namesPort = _NamesPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 15, 21, 1, 7),
    _NamesPort_Type()
)
namesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    namesPort.setStatus("current")
_DID_ObjectIdentity = ObjectIdentity
dID = _DID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16)
)


class _DIDEnable_Type(Integer32):
    """Custom type dIDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DIDEnable_Type.__name__ = "Integer32"
_DIDEnable_Object = MibScalar
dIDEnable = _DIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 1),
    _DIDEnable_Type()
)
dIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIDEnable.setStatus("current")


class _DIDEnableWink_Type(Integer32):
    """Custom type dIDEnableWink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DIDEnableWink_Type.__name__ = "Integer32"
_DIDEnableWink_Object = MibScalar
dIDEnableWink = _DIDEnableWink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 2),
    _DIDEnableWink_Type()
)
dIDEnableWink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIDEnableWink.setStatus("current")


class _DIDDelayBeforeDidWink_Type(Unsigned32):
    """Custom type dIDDelayBeforeDidWink based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DIDDelayBeforeDidWink_Type.__name__ = "Unsigned32"
_DIDDelayBeforeDidWink_Object = MibScalar
dIDDelayBeforeDidWink = _DIDDelayBeforeDidWink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 3),
    _DIDDelayBeforeDidWink_Type()
)
dIDDelayBeforeDidWink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dIDDelayBeforeDidWink.setStatus("current")
_EnableDidPortTable_Object = MibTable
enableDidPortTable = _EnableDidPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 21)
)
if mibBuilder.loadTexts:
    enableDidPortTable.setStatus("current")
_EnableDidPortEntry_Object = MibTableRow
enableDidPortEntry = _EnableDidPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 21, 1)
)
enableDidPortEntry.setIndexNames(
    (0, "AcGateway", "enableDidPortIndex"),
)
if mibBuilder.loadTexts:
    enableDidPortEntry.setStatus("current")


class _EnableDidPortIndex_Type(Unsigned32):
    """Custom type enableDidPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_EnableDidPortIndex_Type.__name__ = "Unsigned32"
_EnableDidPortIndex_Object = MibTableColumn
enableDidPortIndex = _EnableDidPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 21, 1, 1),
    _EnableDidPortIndex_Type()
)
enableDidPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableDidPortIndex.setStatus("current")


class _EnableDidPortIsUsed_Type(Integer32):
    """Custom type enableDidPortIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EnableDidPortIsUsed_Type.__name__ = "Integer32"
_EnableDidPortIsUsed_Object = MibTableColumn
enableDidPortIsUsed = _EnableDidPortIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 21, 1, 2),
    _EnableDidPortIsUsed_Type()
)
enableDidPortIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableDidPortIsUsed.setStatus("current")


class _EnableDidPortAction_Type(Integer32):
    """Custom type enableDidPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_EnableDidPortAction_Type.__name__ = "Integer32"
_EnableDidPortAction_Object = MibTableColumn
enableDidPortAction = _EnableDidPortAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 21, 1, 3),
    _EnableDidPortAction_Type()
)
enableDidPortAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableDidPortAction.setStatus("current")


class _EnableDidPortActionResult_Type(Integer32):
    """Custom type enableDidPortActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_EnableDidPortActionResult_Type.__name__ = "Integer32"
_EnableDidPortActionResult_Object = MibTableColumn
enableDidPortActionResult = _EnableDidPortActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 21, 1, 4),
    _EnableDidPortActionResult_Type()
)
enableDidPortActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableDidPortActionResult.setStatus("current")


class _EnableDidPortEnable_Type(Integer32):
    """Custom type enableDidPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EnableDidPortEnable_Type.__name__ = "Integer32"
_EnableDidPortEnable_Object = MibTableColumn
enableDidPortEnable = _EnableDidPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 21, 1, 5),
    _EnableDidPortEnable_Type()
)
enableDidPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableDidPortEnable.setStatus("current")


class _EnableDidPortModule_Type(Unsigned32):
    """Custom type enableDidPortModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnableDidPortModule_Type.__name__ = "Unsigned32"
_EnableDidPortModule_Object = MibTableColumn
enableDidPortModule = _EnableDidPortModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 21, 1, 6),
    _EnableDidPortModule_Type()
)
enableDidPortModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableDidPortModule.setStatus("current")


class _EnableDidPortPort_Type(Unsigned32):
    """Custom type enableDidPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EnableDidPortPort_Type.__name__ = "Unsigned32"
_EnableDidPortPort_Object = MibTableColumn
enableDidPortPort = _EnableDidPortPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 16, 21, 1, 7),
    _EnableDidPortPort_Type()
)
enableDidPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableDidPortPort.setStatus("current")
_EnableCallWaitingPerPortTable_Object = MibTable
enableCallWaitingPerPortTable = _EnableCallWaitingPerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 21)
)
if mibBuilder.loadTexts:
    enableCallWaitingPerPortTable.setStatus("current")
_EnableCallWaitingPerPortEntry_Object = MibTableRow
enableCallWaitingPerPortEntry = _EnableCallWaitingPerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 21, 1)
)
enableCallWaitingPerPortEntry.setIndexNames(
    (0, "AcGateway", "enableCallWaitingPerPortIndex"),
)
if mibBuilder.loadTexts:
    enableCallWaitingPerPortEntry.setStatus("current")


class _EnableCallWaitingPerPortIndex_Type(Unsigned32):
    """Custom type enableCallWaitingPerPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_EnableCallWaitingPerPortIndex_Type.__name__ = "Unsigned32"
_EnableCallWaitingPerPortIndex_Object = MibTableColumn
enableCallWaitingPerPortIndex = _EnableCallWaitingPerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 21, 1, 1),
    _EnableCallWaitingPerPortIndex_Type()
)
enableCallWaitingPerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableCallWaitingPerPortIndex.setStatus("current")


class _EnableCallWaitingPerPortIsUsed_Type(Integer32):
    """Custom type enableCallWaitingPerPortIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EnableCallWaitingPerPortIsUsed_Type.__name__ = "Integer32"
_EnableCallWaitingPerPortIsUsed_Object = MibTableColumn
enableCallWaitingPerPortIsUsed = _EnableCallWaitingPerPortIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 21, 1, 2),
    _EnableCallWaitingPerPortIsUsed_Type()
)
enableCallWaitingPerPortIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableCallWaitingPerPortIsUsed.setStatus("current")


class _EnableCallWaitingPerPortModule_Type(Unsigned32):
    """Custom type enableCallWaitingPerPortModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnableCallWaitingPerPortModule_Type.__name__ = "Unsigned32"
_EnableCallWaitingPerPortModule_Object = MibTableColumn
enableCallWaitingPerPortModule = _EnableCallWaitingPerPortModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 21, 1, 3),
    _EnableCallWaitingPerPortModule_Type()
)
enableCallWaitingPerPortModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableCallWaitingPerPortModule.setStatus("current")


class _EnableCallWaitingPerPortPort_Type(Unsigned32):
    """Custom type enableCallWaitingPerPortPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EnableCallWaitingPerPortPort_Type.__name__ = "Unsigned32"
_EnableCallWaitingPerPortPort_Object = MibTableColumn
enableCallWaitingPerPortPort = _EnableCallWaitingPerPortPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 21, 1, 4),
    _EnableCallWaitingPerPortPort_Type()
)
enableCallWaitingPerPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableCallWaitingPerPortPort.setStatus("current")


class _EnableCallWaitingPerPortAction_Type(Integer32):
    """Custom type enableCallWaitingPerPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_EnableCallWaitingPerPortAction_Type.__name__ = "Integer32"
_EnableCallWaitingPerPortAction_Object = MibTableColumn
enableCallWaitingPerPortAction = _EnableCallWaitingPerPortAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 21, 1, 5),
    _EnableCallWaitingPerPortAction_Type()
)
enableCallWaitingPerPortAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableCallWaitingPerPortAction.setStatus("current")


class _EnableCallWaitingPerPortActionResult_Type(Integer32):
    """Custom type enableCallWaitingPerPortActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_EnableCallWaitingPerPortActionResult_Type.__name__ = "Integer32"
_EnableCallWaitingPerPortActionResult_Object = MibTableColumn
enableCallWaitingPerPortActionResult = _EnableCallWaitingPerPortActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 21, 1, 6),
    _EnableCallWaitingPerPortActionResult_Type()
)
enableCallWaitingPerPortActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enableCallWaitingPerPortActionResult.setStatus("current")


class _EnableCallWaitingPerPortEnable_Type(Integer32):
    """Custom type enableCallWaitingPerPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("valueNotSet", 255),
          ("yes", 1))
    )


_EnableCallWaitingPerPortEnable_Type.__name__ = "Integer32"
_EnableCallWaitingPerPortEnable_Object = MibTableColumn
enableCallWaitingPerPortEnable = _EnableCallWaitingPerPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 4, 21, 1, 7),
    _EnableCallWaitingPerPortEnable_Type()
)
enableCallWaitingPerPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableCallWaitingPerPortEnable.setStatus("current")
_MediaGW_ObjectIdentity = ObjectIdentity
mediaGW = _MediaGW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5)
)


class _MediaGWMediaChannels_Type(Unsigned32):
    """Custom type mediaGWMediaChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2016),
    )


_MediaGWMediaChannels_Type.__name__ = "Unsigned32"
_MediaGWMediaChannels_Object = MibScalar
mediaGWMediaChannels = _MediaGWMediaChannels_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 1),
    _MediaGWMediaChannels_Type()
)
mediaGWMediaChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaGWMediaChannels.setStatus("current")
_Conference_ObjectIdentity = ObjectIdentity
conference = _Conference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10)
)


class _ConferenceID_Type(SnmpAdminString):
    """Custom type conferenceID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConferenceID_Type.__name__ = "SnmpAdminString"
_ConferenceID_Object = MibScalar
conferenceID = _ConferenceID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10, 1),
    _ConferenceID_Type()
)
conferenceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conferenceID.setStatus("current")


class _ConferenceBipOnConference_Type(Integer32):
    """Custom type conferenceBipOnConference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ConferenceBipOnConference_Type.__name__ = "Integer32"
_ConferenceBipOnConference_Object = MibScalar
conferenceBipOnConference = _ConferenceBipOnConference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10, 2),
    _ConferenceBipOnConference_Type()
)
conferenceBipOnConference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conferenceBipOnConference.setStatus("current")


class _ConferenceEnableDTMFReporting_Type(Integer32):
    """Custom type conferenceEnableDTMFReporting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ConferenceEnableDTMFReporting_Type.__name__ = "Integer32"
_ConferenceEnableDTMFReporting_Object = MibScalar
conferenceEnableDTMFReporting = _ConferenceEnableDTMFReporting_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10, 3),
    _ConferenceEnableDTMFReporting_Type()
)
conferenceEnableDTMFReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conferenceEnableDTMFReporting.setStatus("current")


class _ConferenceEnableDTMFClamping_Type(Integer32):
    """Custom type conferenceEnableDTMFClamping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ConferenceEnableDTMFClamping_Type.__name__ = "Integer32"
_ConferenceEnableDTMFClamping_Object = MibScalar
conferenceEnableDTMFClamping = _ConferenceEnableDTMFClamping_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10, 4),
    _ConferenceEnableDTMFClamping_Type()
)
conferenceEnableDTMFClamping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conferenceEnableDTMFClamping.setStatus("current")


class _Conference3WayMode_Type(Integer32):
    """Custom type conference3WayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("audioCodesMediaServer", 0),
          ("noneAudioCodesMediaServer", 1),
          ("onBoard", 2))
    )


_Conference3WayMode_Type.__name__ = "Integer32"
_Conference3WayMode_Object = MibScalar
conference3WayMode = _Conference3WayMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10, 5),
    _Conference3WayMode_Type()
)
conference3WayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conference3WayMode.setStatus("current")


class _ConferenceMaxInBoardCalls_Type(Unsigned32):
    """Custom type conferenceMaxInBoardCalls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ConferenceMaxInBoardCalls_Type.__name__ = "Unsigned32"
_ConferenceMaxInBoardCalls_Object = MibScalar
conferenceMaxInBoardCalls = _ConferenceMaxInBoardCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10, 6),
    _ConferenceMaxInBoardCalls_Type()
)
conferenceMaxInBoardCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    conferenceMaxInBoardCalls.setStatus("current")
_AcTWCnonAllocateablePortsTable_Object = MibTable
acTWCnonAllocateablePortsTable = _AcTWCnonAllocateablePortsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10, 21)
)
if mibBuilder.loadTexts:
    acTWCnonAllocateablePortsTable.setStatus("current")
_AcTWCnonAllocateablePortsEntry_Object = MibTableRow
acTWCnonAllocateablePortsEntry = _AcTWCnonAllocateablePortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10, 21, 1)
)
acTWCnonAllocateablePortsEntry.setIndexNames(
    (0, "AcGateway", "acTWCnonAllocateablePortsIndex"),
)
if mibBuilder.loadTexts:
    acTWCnonAllocateablePortsEntry.setStatus("current")


class _AcTWCnonAllocateablePortsIndex_Type(Unsigned32):
    """Custom type acTWCnonAllocateablePortsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcTWCnonAllocateablePortsIndex_Type.__name__ = "Unsigned32"
_AcTWCnonAllocateablePortsIndex_Object = MibTableColumn
acTWCnonAllocateablePortsIndex = _AcTWCnonAllocateablePortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10, 21, 1, 1),
    _AcTWCnonAllocateablePortsIndex_Type()
)
acTWCnonAllocateablePortsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acTWCnonAllocateablePortsIndex.setStatus("current")


class _AcTWCnonAllocateablePortsNumber_Type(Unsigned32):
    """Custom type acTWCnonAllocateablePortsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AcTWCnonAllocateablePortsNumber_Type.__name__ = "Unsigned32"
_AcTWCnonAllocateablePortsNumber_Object = MibTableColumn
acTWCnonAllocateablePortsNumber = _AcTWCnonAllocateablePortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 10, 21, 1, 2),
    _AcTWCnonAllocateablePortsNumber_Type()
)
acTWCnonAllocateablePortsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTWCnonAllocateablePortsNumber.setStatus("current")
_Announcement_ObjectIdentity = ObjectIdentity
announcement = _Announcement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11)
)


class _AnnouncementID_Type(SnmpAdminString):
    """Custom type announcementID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnnouncementID_Type.__name__ = "SnmpAdminString"
_AnnouncementID_Object = MibScalar
announcementID = _AnnouncementID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 1),
    _AnnouncementID_Type()
)
announcementID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    announcementID.setStatus("current")


class _AnnouncementNumOfEndPoints_Type(Unsigned32):
    """Custom type announcementNumOfEndPoints based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_AnnouncementNumOfEndPoints_Type.__name__ = "Unsigned32"
_AnnouncementNumOfEndPoints_Object = MibScalar
announcementNumOfEndPoints = _AnnouncementNumOfEndPoints_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 2),
    _AnnouncementNumOfEndPoints_Type()
)
announcementNumOfEndPoints.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    announcementNumOfEndPoints.setStatus("current")


class _AnnouncementToneID_Type(SnmpAdminString):
    """Custom type announcementToneID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnnouncementToneID_Type.__name__ = "SnmpAdminString"
_AnnouncementToneID_Object = MibScalar
announcementToneID = _AnnouncementToneID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 3),
    _AnnouncementToneID_Type()
)
announcementToneID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    announcementToneID.setStatus("current")
_Streaming_ObjectIdentity = ObjectIdentity
streaming = _Streaming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10)
)


class _StreamingID_Type(SnmpAdminString):
    """Custom type streamingID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_StreamingID_Type.__name__ = "SnmpAdminString"
_StreamingID_Object = MibScalar
streamingID = _StreamingID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10, 1),
    _StreamingID_Type()
)
streamingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamingID.setStatus("current")


class _StreamingNumOfEndPoints_Type(Unsigned32):
    """Custom type streamingNumOfEndPoints based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_StreamingNumOfEndPoints_Type.__name__ = "Unsigned32"
_StreamingNumOfEndPoints_Object = MibScalar
streamingNumOfEndPoints = _StreamingNumOfEndPoints_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10, 2),
    _StreamingNumOfEndPoints_Type()
)
streamingNumOfEndPoints.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamingNumOfEndPoints.setStatus("current")


class _StreamingRecordScriptPath_Type(SnmpAdminString):
    """Custom type streamingRecordScriptPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StreamingRecordScriptPath_Type.__name__ = "SnmpAdminString"
_StreamingRecordScriptPath_Object = MibScalar
streamingRecordScriptPath = _StreamingRecordScriptPath_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10, 3),
    _StreamingRecordScriptPath_Type()
)
streamingRecordScriptPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamingRecordScriptPath.setStatus("obsolete")


class _StreamingMediaID_Type(SnmpAdminString):
    """Custom type streamingMediaID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_StreamingMediaID_Type.__name__ = "SnmpAdminString"
_StreamingMediaID_Object = MibScalar
streamingMediaID = _StreamingMediaID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10, 4),
    _StreamingMediaID_Type()
)
streamingMediaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamingMediaID.setStatus("current")


class _StreamingStopRecordingOnNoSpeachTimeout_Type(Integer32):
    """Custom type streamingStopRecordingOnNoSpeachTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000000),
    )


_StreamingStopRecordingOnNoSpeachTimeout_Type.__name__ = "Integer32"
_StreamingStopRecordingOnNoSpeachTimeout_Object = MibScalar
streamingStopRecordingOnNoSpeachTimeout = _StreamingStopRecordingOnNoSpeachTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10, 5),
    _StreamingStopRecordingOnNoSpeachTimeout_Type()
)
streamingStopRecordingOnNoSpeachTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamingStopRecordingOnNoSpeachTimeout.setStatus("current")


class _StreamingPlayFromID_Type(SnmpAdminString):
    """Custom type streamingPlayFromID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_StreamingPlayFromID_Type.__name__ = "SnmpAdminString"
_StreamingPlayFromID_Object = MibScalar
streamingPlayFromID = _StreamingPlayFromID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10, 6),
    _StreamingPlayFromID_Type()
)
streamingPlayFromID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamingPlayFromID.setStatus("current")


class _StreamingRecordToID_Type(SnmpAdminString):
    """Custom type streamingRecordToID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_StreamingRecordToID_Type.__name__ = "SnmpAdminString"
_StreamingRecordToID_Object = MibScalar
streamingRecordToID = _StreamingRecordToID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10, 7),
    _StreamingRecordToID_Type()
)
streamingRecordToID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamingRecordToID.setStatus("current")


class _StreamingNetAnnAnncID_Type(SnmpAdminString):
    """Custom type streamingNetAnnAnncID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_StreamingNetAnnAnncID_Type.__name__ = "SnmpAdminString"
_StreamingNetAnnAnncID_Object = MibScalar
streamingNetAnnAnncID = _StreamingNetAnnAnncID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10, 8),
    _StreamingNetAnnAnncID_Type()
)
streamingNetAnnAnncID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamingNetAnnAnncID.setStatus("current")


class _StreamingMscmlID_Type(SnmpAdminString):
    """Custom type streamingMscmlID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_StreamingMscmlID_Type.__name__ = "SnmpAdminString"
_StreamingMscmlID_Object = MibScalar
streamingMscmlID = _StreamingMscmlID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10, 9),
    _StreamingMscmlID_Type()
)
streamingMscmlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamingMscmlID.setStatus("current")


class _StreamingMonitorID_Type(SnmpAdminString):
    """Custom type streamingMonitorID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_StreamingMonitorID_Type.__name__ = "SnmpAdminString"
_StreamingMonitorID_Object = MibScalar
streamingMonitorID = _StreamingMonitorID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 11, 10, 10),
    _StreamingMonitorID_Type()
)
streamingMonitorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamingMonitorID.setStatus("current")
_Vxml_ObjectIdentity = ObjectIdentity
vxml = _Vxml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 12)
)


class _VxmlID_Type(SnmpAdminString):
    """Custom type vxmlID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VxmlID_Type.__name__ = "SnmpAdminString"
_VxmlID_Object = MibScalar
vxmlID = _VxmlID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 12, 1),
    _VxmlID_Type()
)
vxmlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vxmlID.setStatus("current")


class _VxmlNumOfEndPoints_Type(Unsigned32):
    """Custom type vxmlNumOfEndPoints based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_VxmlNumOfEndPoints_Type.__name__ = "Unsigned32"
_VxmlNumOfEndPoints_Object = MibScalar
vxmlNumOfEndPoints = _VxmlNumOfEndPoints_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 12, 2),
    _VxmlNumOfEndPoints_Type()
)
vxmlNumOfEndPoints.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vxmlNumOfEndPoints.setStatus("current")
_Calea_ObjectIdentity = ObjectIdentity
calea = _Calea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 13)
)


class _CaleaInterceptionDirection_Type(Integer32):
    """Custom type caleaInterceptionDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 0))
    )


_CaleaInterceptionDirection_Type.__name__ = "Integer32"
_CaleaInterceptionDirection_Object = MibScalar
caleaInterceptionDirection = _CaleaInterceptionDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 13, 1),
    _CaleaInterceptionDirection_Type()
)
caleaInterceptionDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    caleaInterceptionDirection.setStatus("current")
_Transcoding_ObjectIdentity = ObjectIdentity
transcoding = _Transcoding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 14)
)


class _TranscodingID_Type(SnmpAdminString):
    """Custom type transcodingID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TranscodingID_Type.__name__ = "SnmpAdminString"
_TranscodingID_Object = MibScalar
transcodingID = _TranscodingID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 5, 14, 1),
    _TranscodingID_Type()
)
transcodingID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcodingID.setStatus("current")
_Coders_ObjectIdentity = ObjectIdentity
coders = _Coders_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6)
)
_CodersTable_Object = MibTable
codersTable = _CodersTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    codersTable.setStatus("current")
_CodersEntry_Object = MibTableRow
codersEntry = _CodersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1, 1)
)
codersEntry.setIndexNames(
    (0, "AcGateway", "codersIndex"),
)
if mibBuilder.loadTexts:
    codersEntry.setStatus("current")


class _CodersIndex_Type(Unsigned32):
    """Custom type codersIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CodersIndex_Type.__name__ = "Unsigned32"
_CodersIndex_Object = MibTableColumn
codersIndex = _CodersIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1, 1, 1),
    _CodersIndex_Type()
)
codersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    codersIndex.setStatus("deprecated")
_CodersRowStatus_Type = RowStatus
_CodersRowStatus_Object = MibTableColumn
codersRowStatus = _CodersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1, 1, 2),
    _CodersRowStatus_Type()
)
codersRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersRowStatus.setStatus("deprecated")


class _CodersAction_Type(Integer32):
    """Custom type codersAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_CodersAction_Type.__name__ = "Integer32"
_CodersAction_Object = MibTableColumn
codersAction = _CodersAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1, 1, 3),
    _CodersAction_Type()
)
codersAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codersAction.setStatus("deprecated")


class _CodersActionResult_Type(Integer32):
    """Custom type codersActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_CodersActionResult_Type.__name__ = "Integer32"
_CodersActionResult_Object = MibTableColumn
codersActionResult = _CodersActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1, 1, 4),
    _CodersActionResult_Type()
)
codersActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codersActionResult.setStatus("deprecated")


class _CodersName_Type(Integer32):
    """Custom type codersName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
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
              17,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              99)
        )
    )
    namedValues = NamedValues(
        *(("aMR-WB", 34),
          ("amr", 23),
          ("eVRC", 22),
          ("eVRC-B", 32),
          ("eg711Alaw", 35),
          ("eg711Ulaw", 36),
          ("g711Alaw64k", 1),
          ("g711Alaw64k-VBD", 30),
          ("g711Ulaw64k", 2),
          ("g711Ulaw64k-VBD", 31),
          ("g722", 33),
          ("g7231", 0),
          ("g726", 5),
          ("g726r16", 6),
          ("g726r24", 7),
          ("g726r32", 8),
          ("g726r40", 9),
          ("g729", 3),
          ("g7291", 37),
          ("g729AnnexB", 17),
          ("gWTransparent", 14),
          ("gsm-fr", 24),
          ("gsm-ms", 25),
          ("gsmEfr", 26),
          ("iLBC", 27),
          ("invalideCoder", 99),
          ("ms-rta-nb", 39),
          ("netCoder6-4", 11),
          ("netCoder7-2", 12),
          ("netCoder8", 10),
          ("netCoder8-8", 13),
          ("qCELP", 28),
          ("t38", 29),
          ("v1501mr", 38))
    )


_CodersName_Type.__name__ = "Integer32"
_CodersName_Object = MibTableColumn
codersName = _CodersName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1, 1, 5),
    _CodersName_Type()
)
codersName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersName.setStatus("deprecated")


class _CodersInterval_Type(Unsigned32):
    """Custom type codersInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_CodersInterval_Type.__name__ = "Unsigned32"
_CodersInterval_Object = MibTableColumn
codersInterval = _CodersInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1, 1, 6),
    _CodersInterval_Type()
)
codersInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersInterval.setStatus("deprecated")


class _CodersRate_Type(Unsigned32):
    """Custom type codersRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_CodersRate_Type.__name__ = "Unsigned32"
_CodersRate_Object = MibTableColumn
codersRate = _CodersRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1, 1, 7),
    _CodersRate_Type()
)
codersRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersRate.setStatus("deprecated")


class _CodersPayloadType_Type(Unsigned32):
    """Custom type codersPayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CodersPayloadType_Type.__name__ = "Unsigned32"
_CodersPayloadType_Object = MibTableColumn
codersPayloadType = _CodersPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1, 1, 8),
    _CodersPayloadType_Type()
)
codersPayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersPayloadType.setStatus("deprecated")


class _CodersSilenceSuppression_Type(Integer32):
    """Custom type codersSilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("enableAdaptations", 2))
    )


_CodersSilenceSuppression_Type.__name__ = "Integer32"
_CodersSilenceSuppression_Object = MibTableColumn
codersSilenceSuppression = _CodersSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 1, 1, 9),
    _CodersSilenceSuppression_Type()
)
codersSilenceSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersSilenceSuppression.setStatus("deprecated")
_CodersGroup0Table_Object = MibTable
codersGroup0Table = _CodersGroup0Table_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    codersGroup0Table.setStatus("current")
_CodersGroup0Entry_Object = MibTableRow
codersGroup0Entry = _CodersGroup0Entry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2, 1)
)
codersGroup0Entry.setIndexNames(
    (0, "AcGateway", "codersGroup0Index"),
)
if mibBuilder.loadTexts:
    codersGroup0Entry.setStatus("current")


class _CodersGroup0Index_Type(Unsigned32):
    """Custom type codersGroup0Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CodersGroup0Index_Type.__name__ = "Unsigned32"
_CodersGroup0Index_Object = MibTableColumn
codersGroup0Index = _CodersGroup0Index_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2, 1, 1),
    _CodersGroup0Index_Type()
)
codersGroup0Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    codersGroup0Index.setStatus("current")
_CodersGroup0RowStatus_Type = RowStatus
_CodersGroup0RowStatus_Object = MibTableColumn
codersGroup0RowStatus = _CodersGroup0RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2, 1, 2),
    _CodersGroup0RowStatus_Type()
)
codersGroup0RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup0RowStatus.setStatus("current")


class _CodersGroup0Action_Type(Integer32):
    """Custom type codersGroup0Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_CodersGroup0Action_Type.__name__ = "Integer32"
_CodersGroup0Action_Object = MibTableColumn
codersGroup0Action = _CodersGroup0Action_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2, 1, 3),
    _CodersGroup0Action_Type()
)
codersGroup0Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup0Action.setStatus("current")


class _CodersGroup0ActionRes_Type(Integer32):
    """Custom type codersGroup0ActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_CodersGroup0ActionRes_Type.__name__ = "Integer32"
_CodersGroup0ActionRes_Object = MibTableColumn
codersGroup0ActionRes = _CodersGroup0ActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2, 1, 4),
    _CodersGroup0ActionRes_Type()
)
codersGroup0ActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codersGroup0ActionRes.setStatus("current")


class _CodersGroup0Name_Type(Integer32):
    """Custom type codersGroup0Name based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
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
              17,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              99)
        )
    )
    namedValues = NamedValues(
        *(("aMR-WB", 34),
          ("amr", 23),
          ("eVRC", 22),
          ("eVRC-B", 32),
          ("eg711Alaw", 35),
          ("eg711Ulaw", 36),
          ("g711Alaw64k", 1),
          ("g711Alaw64k-VBD", 30),
          ("g711Ulaw64k", 2),
          ("g711Ulaw64k-VBD", 31),
          ("g722", 33),
          ("g7231", 0),
          ("g726", 5),
          ("g726r16", 6),
          ("g726r24", 7),
          ("g726r32", 8),
          ("g726r40", 9),
          ("g729", 3),
          ("g7291", 37),
          ("g729AnnexB", 17),
          ("gWTransparent", 14),
          ("gsm-fr", 24),
          ("gsm-ms", 25),
          ("gsmEfr", 26),
          ("iLBC", 27),
          ("invalideCoder", 99),
          ("ms-rta-nb", 39),
          ("netCoder6-4", 11),
          ("netCoder7-2", 12),
          ("netCoder8", 10),
          ("netCoder8-8", 13),
          ("qCELP", 28),
          ("t38", 29),
          ("v1501mr", 38))
    )


_CodersGroup0Name_Type.__name__ = "Integer32"
_CodersGroup0Name_Object = MibTableColumn
codersGroup0Name = _CodersGroup0Name_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2, 1, 5),
    _CodersGroup0Name_Type()
)
codersGroup0Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup0Name.setStatus("current")


class _CodersGroup0PacketizationTime_Type(Unsigned32):
    """Custom type codersGroup0PacketizationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CodersGroup0PacketizationTime_Type.__name__ = "Unsigned32"
_CodersGroup0PacketizationTime_Object = MibTableColumn
codersGroup0PacketizationTime = _CodersGroup0PacketizationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2, 1, 6),
    _CodersGroup0PacketizationTime_Type()
)
codersGroup0PacketizationTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup0PacketizationTime.setStatus("current")


class _CodersGroup0Rate_Type(Unsigned32):
    """Custom type codersGroup0Rate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_CodersGroup0Rate_Type.__name__ = "Unsigned32"
_CodersGroup0Rate_Object = MibTableColumn
codersGroup0Rate = _CodersGroup0Rate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2, 1, 7),
    _CodersGroup0Rate_Type()
)
codersGroup0Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup0Rate.setStatus("current")


class _CodersGroup0PayloadType_Type(Integer32):
    """Custom type codersGroup0PayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_CodersGroup0PayloadType_Type.__name__ = "Integer32"
_CodersGroup0PayloadType_Object = MibTableColumn
codersGroup0PayloadType = _CodersGroup0PayloadType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2, 1, 8),
    _CodersGroup0PayloadType_Type()
)
codersGroup0PayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup0PayloadType.setStatus("current")


class _CodersGroup0SilenceSuppression_Type(Integer32):
    """Custom type codersGroup0SilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("enableAdaptations", 2))
    )


_CodersGroup0SilenceSuppression_Type.__name__ = "Integer32"
_CodersGroup0SilenceSuppression_Object = MibTableColumn
codersGroup0SilenceSuppression = _CodersGroup0SilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 2, 1, 9),
    _CodersGroup0SilenceSuppression_Type()
)
codersGroup0SilenceSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup0SilenceSuppression.setStatus("current")
_CodersGroup1Table_Object = MibTable
codersGroup1Table = _CodersGroup1Table_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    codersGroup1Table.setStatus("current")
_CodersGroup1Entry_Object = MibTableRow
codersGroup1Entry = _CodersGroup1Entry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3, 1)
)
codersGroup1Entry.setIndexNames(
    (0, "AcGateway", "codersGroup1Index"),
)
if mibBuilder.loadTexts:
    codersGroup1Entry.setStatus("current")


class _CodersGroup1Index_Type(Unsigned32):
    """Custom type codersGroup1Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CodersGroup1Index_Type.__name__ = "Unsigned32"
_CodersGroup1Index_Object = MibTableColumn
codersGroup1Index = _CodersGroup1Index_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3, 1, 1),
    _CodersGroup1Index_Type()
)
codersGroup1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    codersGroup1Index.setStatus("current")
_CodersGroup1RowStatus_Type = RowStatus
_CodersGroup1RowStatus_Object = MibTableColumn
codersGroup1RowStatus = _CodersGroup1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3, 1, 2),
    _CodersGroup1RowStatus_Type()
)
codersGroup1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup1RowStatus.setStatus("current")


class _CodersGroup1Action_Type(Integer32):
    """Custom type codersGroup1Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_CodersGroup1Action_Type.__name__ = "Integer32"
_CodersGroup1Action_Object = MibTableColumn
codersGroup1Action = _CodersGroup1Action_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3, 1, 3),
    _CodersGroup1Action_Type()
)
codersGroup1Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup1Action.setStatus("current")


class _CodersGroup1ActionRes_Type(Integer32):
    """Custom type codersGroup1ActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_CodersGroup1ActionRes_Type.__name__ = "Integer32"
_CodersGroup1ActionRes_Object = MibTableColumn
codersGroup1ActionRes = _CodersGroup1ActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3, 1, 4),
    _CodersGroup1ActionRes_Type()
)
codersGroup1ActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codersGroup1ActionRes.setStatus("current")


class _CodersGroup1Name_Type(Integer32):
    """Custom type codersGroup1Name based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
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
              17,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              99)
        )
    )
    namedValues = NamedValues(
        *(("aMR-WB", 34),
          ("amr", 23),
          ("eVRC", 22),
          ("eVRC-B", 32),
          ("eg711Alaw", 35),
          ("eg711Ulaw", 36),
          ("g711Alaw64k", 1),
          ("g711Alaw64k-VBD", 30),
          ("g711Ulaw64k", 2),
          ("g711Ulaw64k-VBD", 31),
          ("g722", 33),
          ("g7231", 0),
          ("g726", 5),
          ("g726r16", 6),
          ("g726r24", 7),
          ("g726r32", 8),
          ("g726r40", 9),
          ("g729", 3),
          ("g7291", 37),
          ("g729AnnexB", 17),
          ("gWTransparent", 14),
          ("gsm-fr", 24),
          ("gsm-ms", 25),
          ("gsmEfr", 26),
          ("iLBC", 27),
          ("invalideCoder", 99),
          ("ms-rta-nb", 39),
          ("netCoder6-4", 11),
          ("netCoder7-2", 12),
          ("netCoder8", 10),
          ("netCoder8-8", 13),
          ("qCELP", 28),
          ("t38", 29),
          ("v1501mr", 38))
    )


_CodersGroup1Name_Type.__name__ = "Integer32"
_CodersGroup1Name_Object = MibTableColumn
codersGroup1Name = _CodersGroup1Name_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3, 1, 5),
    _CodersGroup1Name_Type()
)
codersGroup1Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup1Name.setStatus("current")


class _CodersGroup1PacketizationTime_Type(Unsigned32):
    """Custom type codersGroup1PacketizationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CodersGroup1PacketizationTime_Type.__name__ = "Unsigned32"
_CodersGroup1PacketizationTime_Object = MibTableColumn
codersGroup1PacketizationTime = _CodersGroup1PacketizationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3, 1, 6),
    _CodersGroup1PacketizationTime_Type()
)
codersGroup1PacketizationTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup1PacketizationTime.setStatus("current")


class _CodersGroup1Rate_Type(Unsigned32):
    """Custom type codersGroup1Rate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_CodersGroup1Rate_Type.__name__ = "Unsigned32"
_CodersGroup1Rate_Object = MibTableColumn
codersGroup1Rate = _CodersGroup1Rate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3, 1, 7),
    _CodersGroup1Rate_Type()
)
codersGroup1Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup1Rate.setStatus("current")


class _CodersGroup1PayloadType_Type(Unsigned32):
    """Custom type codersGroup1PayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CodersGroup1PayloadType_Type.__name__ = "Unsigned32"
_CodersGroup1PayloadType_Object = MibTableColumn
codersGroup1PayloadType = _CodersGroup1PayloadType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3, 1, 8),
    _CodersGroup1PayloadType_Type()
)
codersGroup1PayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup1PayloadType.setStatus("current")


class _CodersGroup1SilenceSuppression_Type(Integer32):
    """Custom type codersGroup1SilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("enableAdaptations", 2))
    )


_CodersGroup1SilenceSuppression_Type.__name__ = "Integer32"
_CodersGroup1SilenceSuppression_Object = MibTableColumn
codersGroup1SilenceSuppression = _CodersGroup1SilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 3, 1, 9),
    _CodersGroup1SilenceSuppression_Type()
)
codersGroup1SilenceSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup1SilenceSuppression.setStatus("current")
_CodersGroup2Table_Object = MibTable
codersGroup2Table = _CodersGroup2Table_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    codersGroup2Table.setStatus("current")
_CodersGroup2Entry_Object = MibTableRow
codersGroup2Entry = _CodersGroup2Entry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4, 1)
)
codersGroup2Entry.setIndexNames(
    (0, "AcGateway", "codersGroup2Index"),
)
if mibBuilder.loadTexts:
    codersGroup2Entry.setStatus("current")


class _CodersGroup2Index_Type(Unsigned32):
    """Custom type codersGroup2Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CodersGroup2Index_Type.__name__ = "Unsigned32"
_CodersGroup2Index_Object = MibTableColumn
codersGroup2Index = _CodersGroup2Index_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4, 1, 1),
    _CodersGroup2Index_Type()
)
codersGroup2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    codersGroup2Index.setStatus("current")
_CodersGroup2RowStatus_Type = RowStatus
_CodersGroup2RowStatus_Object = MibTableColumn
codersGroup2RowStatus = _CodersGroup2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4, 1, 2),
    _CodersGroup2RowStatus_Type()
)
codersGroup2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup2RowStatus.setStatus("current")


class _CodersGroup2Action_Type(Integer32):
    """Custom type codersGroup2Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_CodersGroup2Action_Type.__name__ = "Integer32"
_CodersGroup2Action_Object = MibTableColumn
codersGroup2Action = _CodersGroup2Action_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4, 1, 3),
    _CodersGroup2Action_Type()
)
codersGroup2Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup2Action.setStatus("current")


class _CodersGroup2ActionRes_Type(Integer32):
    """Custom type codersGroup2ActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_CodersGroup2ActionRes_Type.__name__ = "Integer32"
_CodersGroup2ActionRes_Object = MibTableColumn
codersGroup2ActionRes = _CodersGroup2ActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4, 1, 4),
    _CodersGroup2ActionRes_Type()
)
codersGroup2ActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codersGroup2ActionRes.setStatus("current")


class _CodersGroup2Name_Type(Integer32):
    """Custom type codersGroup2Name based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
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
              17,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              99)
        )
    )
    namedValues = NamedValues(
        *(("aMR-WB", 34),
          ("amr", 23),
          ("eVRC", 22),
          ("eVRC-B", 32),
          ("eg711Alaw", 35),
          ("eg711Ulaw", 36),
          ("g711Alaw64k", 1),
          ("g711Alaw64k-VBD", 30),
          ("g711Ulaw64k", 2),
          ("g711Ulaw64k-VBD", 31),
          ("g722", 33),
          ("g7231", 0),
          ("g726", 5),
          ("g726r16", 6),
          ("g726r24", 7),
          ("g726r32", 8),
          ("g726r40", 9),
          ("g729", 3),
          ("g7291", 37),
          ("g729AnnexB", 17),
          ("gWTransparent", 14),
          ("gsm-fr", 24),
          ("gsm-ms", 25),
          ("gsmEfr", 26),
          ("iLBC", 27),
          ("invalideCoder", 99),
          ("ms-rta-nb", 39),
          ("netCoder6-4", 11),
          ("netCoder7-2", 12),
          ("netCoder8", 10),
          ("netCoder8-8", 13),
          ("qCELP", 28),
          ("t38", 29),
          ("v1501mr", 38))
    )


_CodersGroup2Name_Type.__name__ = "Integer32"
_CodersGroup2Name_Object = MibTableColumn
codersGroup2Name = _CodersGroup2Name_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4, 1, 5),
    _CodersGroup2Name_Type()
)
codersGroup2Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup2Name.setStatus("current")


class _CodersGroup2PacketizationTime_Type(Unsigned32):
    """Custom type codersGroup2PacketizationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CodersGroup2PacketizationTime_Type.__name__ = "Unsigned32"
_CodersGroup2PacketizationTime_Object = MibTableColumn
codersGroup2PacketizationTime = _CodersGroup2PacketizationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4, 1, 6),
    _CodersGroup2PacketizationTime_Type()
)
codersGroup2PacketizationTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup2PacketizationTime.setStatus("current")


class _CodersGroup2Rate_Type(Unsigned32):
    """Custom type codersGroup2Rate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_CodersGroup2Rate_Type.__name__ = "Unsigned32"
_CodersGroup2Rate_Object = MibTableColumn
codersGroup2Rate = _CodersGroup2Rate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4, 1, 7),
    _CodersGroup2Rate_Type()
)
codersGroup2Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup2Rate.setStatus("current")


class _CodersGroup2PayloadType_Type(Integer32):
    """Custom type codersGroup2PayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_CodersGroup2PayloadType_Type.__name__ = "Integer32"
_CodersGroup2PayloadType_Object = MibTableColumn
codersGroup2PayloadType = _CodersGroup2PayloadType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4, 1, 8),
    _CodersGroup2PayloadType_Type()
)
codersGroup2PayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup2PayloadType.setStatus("current")


class _CodersGroup2SilenceSuppression_Type(Integer32):
    """Custom type codersGroup2SilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("enableAdaptations", 2))
    )


_CodersGroup2SilenceSuppression_Type.__name__ = "Integer32"
_CodersGroup2SilenceSuppression_Object = MibTableColumn
codersGroup2SilenceSuppression = _CodersGroup2SilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 4, 1, 9),
    _CodersGroup2SilenceSuppression_Type()
)
codersGroup2SilenceSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup2SilenceSuppression.setStatus("current")
_CodersGroup3Table_Object = MibTable
codersGroup3Table = _CodersGroup3Table_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    codersGroup3Table.setStatus("current")
_CodersGroup3Entry_Object = MibTableRow
codersGroup3Entry = _CodersGroup3Entry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5, 1)
)
codersGroup3Entry.setIndexNames(
    (0, "AcGateway", "codersGroup3Index"),
)
if mibBuilder.loadTexts:
    codersGroup3Entry.setStatus("current")


class _CodersGroup3Index_Type(Unsigned32):
    """Custom type codersGroup3Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CodersGroup3Index_Type.__name__ = "Unsigned32"
_CodersGroup3Index_Object = MibTableColumn
codersGroup3Index = _CodersGroup3Index_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5, 1, 1),
    _CodersGroup3Index_Type()
)
codersGroup3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    codersGroup3Index.setStatus("current")
_CodersGroup3RowStatus_Type = RowStatus
_CodersGroup3RowStatus_Object = MibTableColumn
codersGroup3RowStatus = _CodersGroup3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5, 1, 2),
    _CodersGroup3RowStatus_Type()
)
codersGroup3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup3RowStatus.setStatus("current")


class _CodersGroup3Action_Type(Integer32):
    """Custom type codersGroup3Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_CodersGroup3Action_Type.__name__ = "Integer32"
_CodersGroup3Action_Object = MibTableColumn
codersGroup3Action = _CodersGroup3Action_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5, 1, 3),
    _CodersGroup3Action_Type()
)
codersGroup3Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup3Action.setStatus("current")


class _CodersGroup3ActionRes_Type(Integer32):
    """Custom type codersGroup3ActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_CodersGroup3ActionRes_Type.__name__ = "Integer32"
_CodersGroup3ActionRes_Object = MibTableColumn
codersGroup3ActionRes = _CodersGroup3ActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5, 1, 4),
    _CodersGroup3ActionRes_Type()
)
codersGroup3ActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codersGroup3ActionRes.setStatus("current")


class _CodersGroup3Name_Type(Integer32):
    """Custom type codersGroup3Name based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
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
              17,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              99)
        )
    )
    namedValues = NamedValues(
        *(("aMR-WB", 34),
          ("amr", 23),
          ("eVRC", 22),
          ("eVRC-B", 32),
          ("eg711Alaw", 35),
          ("eg711Ulaw", 36),
          ("g711Alaw64k", 1),
          ("g711Alaw64k-VBD", 30),
          ("g711Ulaw64k", 2),
          ("g711Ulaw64k-VBD", 31),
          ("g722", 33),
          ("g7231", 0),
          ("g726", 5),
          ("g726r16", 6),
          ("g726r24", 7),
          ("g726r32", 8),
          ("g726r40", 9),
          ("g729", 3),
          ("g7291", 37),
          ("g729AnnexB", 17),
          ("gWTransparent", 14),
          ("gsm-fr", 24),
          ("gsm-ms", 25),
          ("gsmEfr", 26),
          ("iLBC", 27),
          ("invalideCoder", 99),
          ("ms-rta-nb", 39),
          ("netCoder6-4", 11),
          ("netCoder7-2", 12),
          ("netCoder8", 10),
          ("netCoder8-8", 13),
          ("qCELP", 28),
          ("t38", 29),
          ("v1501mr", 38))
    )


_CodersGroup3Name_Type.__name__ = "Integer32"
_CodersGroup3Name_Object = MibTableColumn
codersGroup3Name = _CodersGroup3Name_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5, 1, 5),
    _CodersGroup3Name_Type()
)
codersGroup3Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup3Name.setStatus("current")


class _CodersGroup3PacketizationTime_Type(Unsigned32):
    """Custom type codersGroup3PacketizationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CodersGroup3PacketizationTime_Type.__name__ = "Unsigned32"
_CodersGroup3PacketizationTime_Object = MibTableColumn
codersGroup3PacketizationTime = _CodersGroup3PacketizationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5, 1, 6),
    _CodersGroup3PacketizationTime_Type()
)
codersGroup3PacketizationTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup3PacketizationTime.setStatus("current")


class _CodersGroup3Rate_Type(Unsigned32):
    """Custom type codersGroup3Rate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_CodersGroup3Rate_Type.__name__ = "Unsigned32"
_CodersGroup3Rate_Object = MibTableColumn
codersGroup3Rate = _CodersGroup3Rate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5, 1, 7),
    _CodersGroup3Rate_Type()
)
codersGroup3Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup3Rate.setStatus("current")


class _CodersGroup3PayloadType_Type(Integer32):
    """Custom type codersGroup3PayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_CodersGroup3PayloadType_Type.__name__ = "Integer32"
_CodersGroup3PayloadType_Object = MibTableColumn
codersGroup3PayloadType = _CodersGroup3PayloadType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5, 1, 8),
    _CodersGroup3PayloadType_Type()
)
codersGroup3PayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup3PayloadType.setStatus("current")


class _CodersGroup3SilenceSuppression_Type(Integer32):
    """Custom type codersGroup3SilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("enableAdaptations", 2))
    )


_CodersGroup3SilenceSuppression_Type.__name__ = "Integer32"
_CodersGroup3SilenceSuppression_Object = MibTableColumn
codersGroup3SilenceSuppression = _CodersGroup3SilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 5, 1, 9),
    _CodersGroup3SilenceSuppression_Type()
)
codersGroup3SilenceSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup3SilenceSuppression.setStatus("current")
_CodersGroup4Table_Object = MibTable
codersGroup4Table = _CodersGroup4Table_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    codersGroup4Table.setStatus("current")
_CodersGroup4Entry_Object = MibTableRow
codersGroup4Entry = _CodersGroup4Entry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6, 1)
)
codersGroup4Entry.setIndexNames(
    (0, "AcGateway", "codersGroup4Index"),
)
if mibBuilder.loadTexts:
    codersGroup4Entry.setStatus("current")


class _CodersGroup4Index_Type(Unsigned32):
    """Custom type codersGroup4Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CodersGroup4Index_Type.__name__ = "Unsigned32"
_CodersGroup4Index_Object = MibTableColumn
codersGroup4Index = _CodersGroup4Index_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6, 1, 1),
    _CodersGroup4Index_Type()
)
codersGroup4Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    codersGroup4Index.setStatus("current")
_CodersGroup4RowStatus_Type = RowStatus
_CodersGroup4RowStatus_Object = MibTableColumn
codersGroup4RowStatus = _CodersGroup4RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6, 1, 2),
    _CodersGroup4RowStatus_Type()
)
codersGroup4RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup4RowStatus.setStatus("current")


class _CodersGroup4Action_Type(Integer32):
    """Custom type codersGroup4Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_CodersGroup4Action_Type.__name__ = "Integer32"
_CodersGroup4Action_Object = MibTableColumn
codersGroup4Action = _CodersGroup4Action_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6, 1, 3),
    _CodersGroup4Action_Type()
)
codersGroup4Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup4Action.setStatus("current")


class _CodersGroup4ActionRes_Type(Integer32):
    """Custom type codersGroup4ActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_CodersGroup4ActionRes_Type.__name__ = "Integer32"
_CodersGroup4ActionRes_Object = MibTableColumn
codersGroup4ActionRes = _CodersGroup4ActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6, 1, 4),
    _CodersGroup4ActionRes_Type()
)
codersGroup4ActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codersGroup4ActionRes.setStatus("current")


class _CodersGroup4Name_Type(Integer32):
    """Custom type codersGroup4Name based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
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
              17,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              99)
        )
    )
    namedValues = NamedValues(
        *(("aMR-WB", 34),
          ("amr", 23),
          ("eVRC", 22),
          ("eVRC-B", 32),
          ("eg711Alaw", 35),
          ("eg711Ulaw", 36),
          ("g711Alaw64k", 1),
          ("g711Alaw64k-VBD", 30),
          ("g711Ulaw64k", 2),
          ("g711Ulaw64k-VBD", 31),
          ("g722", 33),
          ("g7231", 0),
          ("g726", 5),
          ("g726r16", 6),
          ("g726r24", 7),
          ("g726r32", 8),
          ("g726r40", 9),
          ("g729", 3),
          ("g7291", 37),
          ("g729AnnexB", 17),
          ("gWTransparent", 14),
          ("gsm-fr", 24),
          ("gsm-ms", 25),
          ("gsmEfr", 26),
          ("iLBC", 27),
          ("invalideCoder", 99),
          ("ms-rta-nb", 39),
          ("netCoder6-4", 11),
          ("netCoder7-2", 12),
          ("netCoder8", 10),
          ("netCoder8-8", 13),
          ("qCELP", 28),
          ("t38", 29),
          ("v1501mr", 38))
    )


_CodersGroup4Name_Type.__name__ = "Integer32"
_CodersGroup4Name_Object = MibTableColumn
codersGroup4Name = _CodersGroup4Name_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6, 1, 5),
    _CodersGroup4Name_Type()
)
codersGroup4Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup4Name.setStatus("current")


class _CodersGroup4PacketizationTime_Type(Unsigned32):
    """Custom type codersGroup4PacketizationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CodersGroup4PacketizationTime_Type.__name__ = "Unsigned32"
_CodersGroup4PacketizationTime_Object = MibTableColumn
codersGroup4PacketizationTime = _CodersGroup4PacketizationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6, 1, 6),
    _CodersGroup4PacketizationTime_Type()
)
codersGroup4PacketizationTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup4PacketizationTime.setStatus("current")


class _CodersGroup4Rate_Type(Unsigned32):
    """Custom type codersGroup4Rate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_CodersGroup4Rate_Type.__name__ = "Unsigned32"
_CodersGroup4Rate_Object = MibTableColumn
codersGroup4Rate = _CodersGroup4Rate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6, 1, 7),
    _CodersGroup4Rate_Type()
)
codersGroup4Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup4Rate.setStatus("current")


class _CodersGroup4PayloadType_Type(Integer32):
    """Custom type codersGroup4PayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_CodersGroup4PayloadType_Type.__name__ = "Integer32"
_CodersGroup4PayloadType_Object = MibTableColumn
codersGroup4PayloadType = _CodersGroup4PayloadType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6, 1, 8),
    _CodersGroup4PayloadType_Type()
)
codersGroup4PayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup4PayloadType.setStatus("current")


class _CodersGroup4SilenceSuppression_Type(Integer32):
    """Custom type codersGroup4SilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("enableAdaptations", 2))
    )


_CodersGroup4SilenceSuppression_Type.__name__ = "Integer32"
_CodersGroup4SilenceSuppression_Object = MibTableColumn
codersGroup4SilenceSuppression = _CodersGroup4SilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 6, 6, 1, 9),
    _CodersGroup4SilenceSuppression_Type()
)
codersGroup4SilenceSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    codersGroup4SilenceSuppression.setStatus("current")
_SupServices_ObjectIdentity = ObjectIdentity
supServices = _SupServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7)
)


class _SupServicesEnableHold_Type(Integer32):
    """Custom type supServicesEnableHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SupServicesEnableHold_Type.__name__ = "Integer32"
_SupServicesEnableHold_Object = MibScalar
supServicesEnableHold = _SupServicesEnableHold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 1),
    _SupServicesEnableHold_Type()
)
supServicesEnableHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesEnableHold.setStatus("current")


class _SupServicesNameID_Type(Integer32):
    """Custom type supServicesNameID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SupServicesNameID_Type.__name__ = "Integer32"
_SupServicesNameID_Object = MibScalar
supServicesNameID = _SupServicesNameID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 2),
    _SupServicesNameID_Type()
)
supServicesNameID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesNameID.setStatus("current")


class _SupServicesHoldFormat_Type(Integer32):
    """Custom type supServicesHoldFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("connectionIP", 0),
          ("sDPattributesSendonly", 1))
    )


_SupServicesHoldFormat_Type.__name__ = "Integer32"
_SupServicesHoldFormat_Object = MibScalar
supServicesHoldFormat = _SupServicesHoldFormat_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 3),
    _SupServicesHoldFormat_Type()
)
supServicesHoldFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesHoldFormat.setStatus("current")


class _SupServicesSendMeteringMessageToIP_Type(Integer32):
    """Custom type supServicesSendMeteringMessageToIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SupServicesSendMeteringMessageToIP_Type.__name__ = "Integer32"
_SupServicesSendMeteringMessageToIP_Object = MibScalar
supServicesSendMeteringMessageToIP = _SupServicesSendMeteringMessageToIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 4),
    _SupServicesSendMeteringMessageToIP_Type()
)
supServicesSendMeteringMessageToIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesSendMeteringMessageToIP.setStatus("current")


class _SupServicesHeldTimeout_Type(Integer32):
    """Custom type supServicesHeldTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2400),
    )


_SupServicesHeldTimeout_Type.__name__ = "Integer32"
_SupServicesHeldTimeout_Object = MibScalar
supServicesHeldTimeout = _SupServicesHeldTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 5),
    _SupServicesHeldTimeout_Type()
)
supServicesHeldTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesHeldTimeout.setStatus("current")


class _SupServicesHookFlashCode_Type(SnmpAdminString):
    """Custom type supServicesHookFlashCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_SupServicesHookFlashCode_Type.__name__ = "SnmpAdminString"
_SupServicesHookFlashCode_Object = MibScalar
supServicesHookFlashCode = _SupServicesHookFlashCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 6),
    _SupServicesHookFlashCode_Type()
)
supServicesHookFlashCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesHookFlashCode.setStatus("current")
_SupServicesCHRRTimeout_Type = Unsigned32
_SupServicesCHRRTimeout_Object = MibScalar
supServicesCHRRTimeout = _SupServicesCHRRTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 7),
    _SupServicesCHRRTimeout_Type()
)
supServicesCHRRTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesCHRRTimeout.setStatus("current")


class _SupServicesEnableHold2ISDN_Type(Integer32):
    """Custom type supServicesEnableHold2ISDN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SupServicesEnableHold2ISDN_Type.__name__ = "Integer32"
_SupServicesEnableHold2ISDN_Object = MibScalar
supServicesEnableHold2ISDN = _SupServicesEnableHold2ISDN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 8),
    _SupServicesEnableHold2ISDN_Type()
)
supServicesEnableHold2ISDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesEnableHold2ISDN.setStatus("current")


class _SupServicesEnableMOH_Type(Integer32):
    """Custom type supServicesEnableMOH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SupServicesEnableMOH_Type.__name__ = "Integer32"
_SupServicesEnableMOH_Object = MibScalar
supServicesEnableMOH = _SupServicesEnableMOH_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 9),
    _SupServicesEnableMOH_Type()
)
supServicesEnableMOH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesEnableMOH.setStatus("current")
_Transfer_ObjectIdentity = ObjectIdentity
transfer = _Transfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 10)
)


class _TransferEnable_Type(Integer32):
    """Custom type transferEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TransferEnable_Type.__name__ = "Integer32"
_TransferEnable_Object = MibScalar
transferEnable = _TransferEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 10, 1),
    _TransferEnable_Type()
)
transferEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferEnable.setStatus("current")


class _TransferXferPrefix_Type(SnmpAdminString):
    """Custom type transferXferPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_TransferXferPrefix_Type.__name__ = "SnmpAdminString"
_TransferXferPrefix_Object = MibScalar
transferXferPrefix = _TransferXferPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 10, 2),
    _TransferXferPrefix_Type()
)
transferXferPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferXferPrefix.setStatus("current")
_CallWaiting_ObjectIdentity = ObjectIdentity
callWaiting = _CallWaiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 11)
)


class _CallWaitingEnable_Type(Integer32):
    """Custom type callWaitingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CallWaitingEnable_Type.__name__ = "Integer32"
_CallWaitingEnable_Object = MibScalar
callWaitingEnable = _CallWaitingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 11, 1),
    _CallWaitingEnable_Type()
)
callWaitingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callWaitingEnable.setStatus("current")


class _CallWaitingNumberOfIndications_Type(Unsigned32):
    """Custom type callWaitingNumberOfIndications based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CallWaitingNumberOfIndications_Type.__name__ = "Unsigned32"
_CallWaitingNumberOfIndications_Object = MibScalar
callWaitingNumberOfIndications = _CallWaitingNumberOfIndications_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 11, 2),
    _CallWaitingNumberOfIndications_Type()
)
callWaitingNumberOfIndications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callWaitingNumberOfIndications.setStatus("current")


class _CallWaitingTimeBetweenIndications_Type(Unsigned32):
    """Custom type callWaitingTimeBetweenIndications based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CallWaitingTimeBetweenIndications_Type.__name__ = "Unsigned32"
_CallWaitingTimeBetweenIndications_Object = MibScalar
callWaitingTimeBetweenIndications = _CallWaitingTimeBetweenIndications_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 11, 3),
    _CallWaitingTimeBetweenIndications_Type()
)
callWaitingTimeBetweenIndications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callWaitingTimeBetweenIndications.setStatus("current")


class _CallWaitingWaitingBeepDuration_Type(Unsigned32):
    """Custom type callWaitingWaitingBeepDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_CallWaitingWaitingBeepDuration_Type.__name__ = "Unsigned32"
_CallWaitingWaitingBeepDuration_Object = MibScalar
callWaitingWaitingBeepDuration = _CallWaitingWaitingBeepDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 11, 4),
    _CallWaitingWaitingBeepDuration_Type()
)
callWaitingWaitingBeepDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callWaitingWaitingBeepDuration.setStatus("current")


class _CallWaitingTimeBeforeWaitingIndications_Type(Unsigned32):
    """Custom type callWaitingTimeBeforeWaitingIndications based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CallWaitingTimeBeforeWaitingIndications_Type.__name__ = "Unsigned32"
_CallWaitingTimeBeforeWaitingIndications_Object = MibScalar
callWaitingTimeBeforeWaitingIndications = _CallWaitingTimeBeforeWaitingIndications_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 11, 5),
    _CallWaitingTimeBeforeWaitingIndications_Type()
)
callWaitingTimeBeforeWaitingIndications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callWaitingTimeBeforeWaitingIndications.setStatus("current")
_ForwardSettings_ObjectIdentity = ObjectIdentity
forwardSettings = _ForwardSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12)
)


class _ForwardSettingsEnable_Type(Integer32):
    """Custom type forwardSettingsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ForwardSettingsEnable_Type.__name__ = "Integer32"
_ForwardSettingsEnable_Object = MibScalar
forwardSettingsEnable = _ForwardSettingsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 1),
    _ForwardSettingsEnable_Type()
)
forwardSettingsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardSettingsEnable.setStatus("current")
_ForwardTable_Object = MibTable
forwardTable = _ForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21)
)
if mibBuilder.loadTexts:
    forwardTable.setStatus("current")
_ForwardEntry_Object = MibTableRow
forwardEntry = _ForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21, 1)
)
forwardEntry.setIndexNames(
    (0, "AcGateway", "forwardIndex"),
)
if mibBuilder.loadTexts:
    forwardEntry.setStatus("current")


class _ForwardIndex_Type(Unsigned32):
    """Custom type forwardIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_ForwardIndex_Type.__name__ = "Unsigned32"
_ForwardIndex_Object = MibTableColumn
forwardIndex = _ForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21, 1, 1),
    _ForwardIndex_Type()
)
forwardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardIndex.setStatus("current")


class _ForwardIsUsed_Type(Integer32):
    """Custom type forwardIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ForwardIsUsed_Type.__name__ = "Integer32"
_ForwardIsUsed_Object = MibTableColumn
forwardIsUsed = _ForwardIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21, 1, 2),
    _ForwardIsUsed_Type()
)
forwardIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardIsUsed.setStatus("current")


class _ForwardAction_Type(Integer32):
    """Custom type forwardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ForwardAction_Type.__name__ = "Integer32"
_ForwardAction_Object = MibTableColumn
forwardAction = _ForwardAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21, 1, 3),
    _ForwardAction_Type()
)
forwardAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardAction.setStatus("current")


class _ForwardActionResult_Type(Integer32):
    """Custom type forwardActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ForwardActionResult_Type.__name__ = "Integer32"
_ForwardActionResult_Object = MibTableColumn
forwardActionResult = _ForwardActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21, 1, 4),
    _ForwardActionResult_Type()
)
forwardActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardActionResult.setStatus("current")


class _ForwardForwardType_Type(Integer32):
    """Custom type forwardForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("busyOrNoAnswer", 4),
          ("dontDisturb", 5),
          ("immediate", 2),
          ("noAnswer", 3),
          ("unknown", 0))
    )


_ForwardForwardType_Type.__name__ = "Integer32"
_ForwardForwardType_Object = MibTableColumn
forwardForwardType = _ForwardForwardType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21, 1, 5),
    _ForwardForwardType_Type()
)
forwardForwardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardForwardType.setStatus("current")


class _ForwardForwardedToNumber_Type(SnmpAdminString):
    """Custom type forwardForwardedToNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_ForwardForwardedToNumber_Type.__name__ = "SnmpAdminString"
_ForwardForwardedToNumber_Object = MibTableColumn
forwardForwardedToNumber = _ForwardForwardedToNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21, 1, 6),
    _ForwardForwardedToNumber_Type()
)
forwardForwardedToNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardForwardedToNumber.setStatus("current")


class _ForwardTimeForNoReply_Type(Unsigned32):
    """Custom type forwardTimeForNoReply based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_ForwardTimeForNoReply_Type.__name__ = "Unsigned32"
_ForwardTimeForNoReply_Object = MibTableColumn
forwardTimeForNoReply = _ForwardTimeForNoReply_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21, 1, 7),
    _ForwardTimeForNoReply_Type()
)
forwardTimeForNoReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardTimeForNoReply.setStatus("current")


class _ForwardModule_Type(Unsigned32):
    """Custom type forwardModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ForwardModule_Type.__name__ = "Unsigned32"
_ForwardModule_Object = MibTableColumn
forwardModule = _ForwardModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21, 1, 8),
    _ForwardModule_Type()
)
forwardModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardModule.setStatus("current")


class _ForwardPort_Type(Unsigned32):
    """Custom type forwardPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ForwardPort_Type.__name__ = "Unsigned32"
_ForwardPort_Object = MibTableColumn
forwardPort = _ForwardPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 12, 21, 1, 9),
    _ForwardPort_Type()
)
forwardPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardPort.setStatus("current")
_MWI_ObjectIdentity = ObjectIdentity
mWI = _MWI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 13)
)


class _MWIEnable_Type(Integer32):
    """Custom type mWIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MWIEnable_Type.__name__ = "Integer32"
_MWIEnable_Object = MibScalar
mWIEnable = _MWIEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 13, 1),
    _MWIEnable_Type()
)
mWIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mWIEnable.setStatus("current")


class _MWIAnalogLamp_Type(Integer32):
    """Custom type mWIAnalogLamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MWIAnalogLamp_Type.__name__ = "Integer32"
_MWIAnalogLamp_Object = MibScalar
mWIAnalogLamp = _MWIAnalogLamp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 13, 2),
    _MWIAnalogLamp_Type()
)
mWIAnalogLamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mWIAnalogLamp.setStatus("current")


class _MWIDisplay_Type(Integer32):
    """Custom type mWIDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MWIDisplay_Type.__name__ = "Integer32"
_MWIDisplay_Object = MibScalar
mWIDisplay = _MWIDisplay_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 13, 3),
    _MWIDisplay_Type()
)
mWIDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mWIDisplay.setStatus("current")


class _MWIServerIP_Type(SnmpAdminString):
    """Custom type mWIServerIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_MWIServerIP_Type.__name__ = "SnmpAdminString"
_MWIServerIP_Object = MibScalar
mWIServerIP = _MWIServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 13, 4),
    _MWIServerIP_Type()
)
mWIServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mWIServerIP.setStatus("current")


class _MWIExpirationTime_Type(Unsigned32):
    """Custom type mWIExpirationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000000),
    )


_MWIExpirationTime_Type.__name__ = "Unsigned32"
_MWIExpirationTime_Object = MibScalar
mWIExpirationTime = _MWIExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 13, 5),
    _MWIExpirationTime_Type()
)
mWIExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mWIExpirationTime.setStatus("current")


class _MWIServerTransportType_Type(Integer32):
    """Custom type mWIServerTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", -1),
          ("tCP", 1),
          ("tLS", 2),
          ("uDP", 0))
    )


_MWIServerTransportType_Type.__name__ = "Integer32"
_MWIServerTransportType_Object = MibScalar
mWIServerTransportType = _MWIServerTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 13, 6),
    _MWIServerTransportType_Type()
)
mWIServerTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mWIServerTransportType.setStatus("current")
_SupServicesConference_ObjectIdentity = ObjectIdentity
supServicesConference = _SupServicesConference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 14)
)


class _SupServicesConferenceEnable3Way_Type(Integer32):
    """Custom type supServicesConferenceEnable3Way based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SupServicesConferenceEnable3Way_Type.__name__ = "Integer32"
_SupServicesConferenceEnable3Way_Object = MibScalar
supServicesConferenceEnable3Way = _SupServicesConferenceEnable3Way_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 14, 1),
    _SupServicesConferenceEnable3Way_Type()
)
supServicesConferenceEnable3Way.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesConferenceEnable3Way.setStatus("current")


class _SupServicesConferenceEstablishCode_Type(SnmpAdminString):
    """Custom type supServicesConferenceEstablishCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_SupServicesConferenceEstablishCode_Type.__name__ = "SnmpAdminString"
_SupServicesConferenceEstablishCode_Object = MibScalar
supServicesConferenceEstablishCode = _SupServicesConferenceEstablishCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 14, 2),
    _SupServicesConferenceEstablishCode_Type()
)
supServicesConferenceEstablishCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesConferenceEstablishCode.setStatus("current")


class _SupServicesBlindTransferDisconnectTimeout_Type(Unsigned32):
    """Custom type supServicesBlindTransferDisconnectTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SupServicesBlindTransferDisconnectTimeout_Type.__name__ = "Unsigned32"
_SupServicesBlindTransferDisconnectTimeout_Object = MibScalar
supServicesBlindTransferDisconnectTimeout = _SupServicesBlindTransferDisconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 7, 30),
    _SupServicesBlindTransferDisconnectTimeout_Type()
)
supServicesBlindTransferDisconnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supServicesBlindTransferDisconnectTimeout.setStatus("current")
_Tones_ObjectIdentity = ObjectIdentity
tones = _Tones_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8)
)


class _TonesTimeForReorderTone_Type(Unsigned32):
    """Custom type tonesTimeForReorderTone based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TonesTimeForReorderTone_Type.__name__ = "Unsigned32"
_TonesTimeForReorderTone_Object = MibScalar
tonesTimeForReorderTone = _TonesTimeForReorderTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8, 1),
    _TonesTimeForReorderTone_Type()
)
tonesTimeForReorderTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonesTimeForReorderTone.setStatus("current")


class _TonesTimeForDialTone_Type(Unsigned32):
    """Custom type tonesTimeForDialTone based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TonesTimeForDialTone_Type.__name__ = "Unsigned32"
_TonesTimeForDialTone_Object = MibScalar
tonesTimeForDialTone = _TonesTimeForDialTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8, 2),
    _TonesTimeForDialTone_Type()
)
tonesTimeForDialTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonesTimeForDialTone.setStatus("current")


class _TonesPlayRBTone2Ip_Type(Integer32):
    """Custom type tonesPlayRBTone2Ip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TonesPlayRBTone2Ip_Type.__name__ = "Integer32"
_TonesPlayRBTone2Ip_Object = MibScalar
tonesPlayRBTone2Ip = _TonesPlayRBTone2Ip_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8, 3),
    _TonesPlayRBTone2Ip_Type()
)
tonesPlayRBTone2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonesPlayRBTone2Ip.setStatus("current")


class _TonesPlayRBTone2Tel_Type(Integer32):
    """Custom type tonesPlayRBTone2Tel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doNotPlay", 0),
          ("playLocalUntilRemoteMediaArrives", 3),
          ("playOnLocal", 1),
          ("preferIp", 2))
    )


_TonesPlayRBTone2Tel_Type.__name__ = "Integer32"
_TonesPlayRBTone2Tel_Object = MibScalar
tonesPlayRBTone2Tel = _TonesPlayRBTone2Tel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8, 4),
    _TonesPlayRBTone2Tel_Type()
)
tonesPlayRBTone2Tel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonesPlayRBTone2Tel.setStatus("current")


class _TonesStutterToneDuration_Type(Unsigned32):
    """Custom type tonesStutterToneDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_TonesStutterToneDuration_Type.__name__ = "Unsigned32"
_TonesStutterToneDuration_Object = MibScalar
tonesStutterToneDuration = _TonesStutterToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8, 5),
    _TonesStutterToneDuration_Type()
)
tonesStutterToneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonesStutterToneDuration.setStatus("current")


class _TonesPlayRBToneXferSuccess_Type(Integer32):
    """Custom type tonesPlayRBToneXferSuccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TonesPlayRBToneXferSuccess_Type.__name__ = "Integer32"
_TonesPlayRBToneXferSuccess_Object = MibScalar
tonesPlayRBToneXferSuccess = _TonesPlayRBToneXferSuccess_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8, 6),
    _TonesPlayRBToneXferSuccess_Type()
)
tonesPlayRBToneXferSuccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonesPlayRBToneXferSuccess.setStatus("current")


class _TonesFirstCallRBTId_Type(Integer32):
    """Custom type tonesFirstCallRBTId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_TonesFirstCallRBTId_Type.__name__ = "Integer32"
_TonesFirstCallRBTId_Object = MibScalar
tonesFirstCallRBTId = _TonesFirstCallRBTId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8, 7),
    _TonesFirstCallRBTId_Type()
)
tonesFirstCallRBTId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonesFirstCallRBTId.setStatus("current")


class _TonesPrecedenceRingingType_Type(Integer32):
    """Custom type tonesPrecedenceRingingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16),
    )


_TonesPrecedenceRingingType_Type.__name__ = "Integer32"
_TonesPrecedenceRingingType_Object = MibScalar
tonesPrecedenceRingingType = _TonesPrecedenceRingingType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8, 8),
    _TonesPrecedenceRingingType_Type()
)
tonesPrecedenceRingingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonesPrecedenceRingingType.setStatus("current")


class _TonesFirstCallWaitingToneID_Type(Integer32):
    """Custom type tonesFirstCallWaitingToneID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_TonesFirstCallWaitingToneID_Type.__name__ = "Integer32"
_TonesFirstCallWaitingToneID_Object = MibScalar
tonesFirstCallWaitingToneID = _TonesFirstCallWaitingToneID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8, 9),
    _TonesFirstCallWaitingToneID_Type()
)
tonesFirstCallWaitingToneID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonesFirstCallWaitingToneID.setStatus("current")


class _TonesEnableComfortTone_Type(Integer32):
    """Custom type tonesEnableComfortTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TonesEnableComfortTone_Type.__name__ = "Integer32"
_TonesEnableComfortTone_Object = MibScalar
tonesEnableComfortTone = _TonesEnableComfortTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 8, 10),
    _TonesEnableComfortTone_Type()
)
tonesEnableComfortTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tonesEnableComfortTone.setStatus("current")
_Logger_ObjectIdentity = ObjectIdentity
logger = _Logger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 9)
)


class _LoggerGwAppCdrReportLevel_Type(Integer32):
    """Custom type loggerGwAppCdrReportLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("connectAndEndCall", 3),
          ("endCall", 1),
          ("no", 0),
          ("startAndEndCall", 2),
          ("startConnectAndEndCall", 4))
    )


_LoggerGwAppCdrReportLevel_Type.__name__ = "Integer32"
_LoggerGwAppCdrReportLevel_Object = MibScalar
loggerGwAppCdrReportLevel = _LoggerGwAppCdrReportLevel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 9, 1),
    _LoggerGwAppCdrReportLevel_Type()
)
loggerGwAppCdrReportLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggerGwAppCdrReportLevel.setStatus("current")


class _LoggerGwDebugLevel_Type(Integer32):
    """Custom type loggerGwDebugLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("logLevel0", 0),
          ("logLevel1", 1),
          ("logLevel100", 100),
          ("logLevel2", 2),
          ("logLevel200", 200),
          ("logLevel3", 3),
          ("logLevel4", 4),
          ("logLevel5", 5))
    )


_LoggerGwDebugLevel_Type.__name__ = "Integer32"
_LoggerGwDebugLevel_Object = MibScalar
loggerGwDebugLevel = _LoggerGwDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 9, 2),
    _LoggerGwDebugLevel_Type()
)
loggerGwDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggerGwDebugLevel.setStatus("current")
_LoggerCDRSyslogServerIP_Type = IpAddress
_LoggerCDRSyslogServerIP_Object = MibScalar
loggerCDRSyslogServerIP = _LoggerCDRSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 9, 3),
    _LoggerCDRSyslogServerIP_Type()
)
loggerCDRSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loggerCDRSyslogServerIP.setStatus("current")
_ProgressIndicators_ObjectIdentity = ObjectIdentity
progressIndicators = _ProgressIndicators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 10)
)


class _ProgressIndicators2ISDN_Type(Integer32):
    """Custom type progressIndicators2ISDN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              8)
        )
    )
    namedValues = NamedValues(
        *(("localRB", 0),
          ("notSet", -1),
          ("remoteRB1", 1),
          ("remoteRB8", 8))
    )


_ProgressIndicators2ISDN_Type.__name__ = "Integer32"
_ProgressIndicators2ISDN_Object = MibScalar
progressIndicators2ISDN = _ProgressIndicators2ISDN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 10, 1),
    _ProgressIndicators2ISDN_Type()
)
progressIndicators2ISDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    progressIndicators2ISDN.setStatus("obsolete")


class _ProgressIndicators2IP_Type(Integer32):
    """Custom type progressIndicators2IP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              8)
        )
    )
    namedValues = NamedValues(
        *(("localRB", 0),
          ("notSet", -1),
          ("remoteRB1", 1),
          ("remoteRB8", 8))
    )


_ProgressIndicators2IP_Type.__name__ = "Integer32"
_ProgressIndicators2IP_Object = MibScalar
progressIndicators2IP = _ProgressIndicators2IP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 10, 2),
    _ProgressIndicators2IP_Type()
)
progressIndicators2IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    progressIndicators2IP.setStatus("current")
_ScreeningIndicators_ObjectIdentity = ObjectIdentity
screeningIndicators = _ScreeningIndicators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 10, 20)
)


class _ScreeningIndicators2Ip_Type(Integer32):
    """Custom type screeningIndicators2Ip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkProvided", 3),
          ("notOverwrited", -1),
          ("userFailed", 2),
          ("userPassed", 1),
          ("userProvided", 0))
    )


_ScreeningIndicators2Ip_Type.__name__ = "Integer32"
_ScreeningIndicators2Ip_Object = MibScalar
screeningIndicators2Ip = _ScreeningIndicators2Ip_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 10, 20, 1),
    _ScreeningIndicators2Ip_Type()
)
screeningIndicators2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    screeningIndicators2Ip.setStatus("current")


class _ScreeningIndicators2ISDN_Type(Integer32):
    """Custom type screeningIndicators2ISDN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkProvided", 3),
          ("notOverwrited", -1),
          ("userFailed", 2),
          ("userPassed", 1),
          ("userProvided", 0))
    )


_ScreeningIndicators2ISDN_Type.__name__ = "Integer32"
_ScreeningIndicators2ISDN_Object = MibScalar
screeningIndicators2ISDN = _ScreeningIndicators2ISDN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 10, 20, 2),
    _ScreeningIndicators2ISDN_Type()
)
screeningIndicators2ISDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    screeningIndicators2ISDN.setStatus("current")
_Misc_ObjectIdentity = ObjectIdentity
misc = _Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11)
)


class _MiscDisconnectOnBusyTone_Type(Integer32):
    """Custom type miscDisconnectOnBusyTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MiscDisconnectOnBusyTone_Type.__name__ = "Integer32"
_MiscDisconnectOnBusyTone_Object = MibScalar
miscDisconnectOnBusyTone = _MiscDisconnectOnBusyTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 1),
    _MiscDisconnectOnBusyTone_Type()
)
miscDisconnectOnBusyTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscDisconnectOnBusyTone.setStatus("current")


class _MiscDisconnectOnSilence_Type(Integer32):
    """Custom type miscDisconnectOnSilence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MiscDisconnectOnSilence_Type.__name__ = "Integer32"
_MiscDisconnectOnSilence_Object = MibScalar
miscDisconnectOnSilence = _MiscDisconnectOnSilence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 2),
    _MiscDisconnectOnSilence_Type()
)
miscDisconnectOnSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscDisconnectOnSilence.setStatus("current")


class _MiscEnableBusyOut_Type(Integer32):
    """Custom type miscEnableBusyOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MiscEnableBusyOut_Type.__name__ = "Integer32"
_MiscEnableBusyOut_Object = MibScalar
miscEnableBusyOut = _MiscEnableBusyOut_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 3),
    _MiscEnableBusyOut_Type()
)
miscEnableBusyOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscEnableBusyOut.setStatus("current")


class _MiscSecureCallsFromIp_Type(Integer32):
    """Custom type miscSecureCallsFromIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MiscSecureCallsFromIp_Type.__name__ = "Integer32"
_MiscSecureCallsFromIp_Object = MibScalar
miscSecureCallsFromIp = _MiscSecureCallsFromIp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 4),
    _MiscSecureCallsFromIp_Type()
)
miscSecureCallsFromIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscSecureCallsFromIp.setStatus("current")


class _MiscStaticNATIP_Type(SnmpAdminString):
    """Custom type miscStaticNATIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MiscStaticNATIP_Type.__name__ = "SnmpAdminString"
_MiscStaticNATIP_Object = MibScalar
miscStaticNATIP = _MiscStaticNATIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 5),
    _MiscStaticNATIP_Type()
)
miscStaticNATIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscStaticNATIP.setStatus("current")


class _MiscSilenceDisconnectTimeout_Type(Unsigned32):
    """Custom type miscSilenceDisconnectTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 28800),
    )


_MiscSilenceDisconnectTimeout_Type.__name__ = "Unsigned32"
_MiscSilenceDisconnectTimeout_Object = MibScalar
miscSilenceDisconnectTimeout = _MiscSilenceDisconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 6),
    _MiscSilenceDisconnectTimeout_Type()
)
miscSilenceDisconnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscSilenceDisconnectTimeout.setStatus("current")


class _MiscIsFaxUsed_Type(Integer32):
    """Custom type miscIsFaxUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallBack", 3),
          ("g711", 2),
          ("noFax", 0),
          ("t38", 1))
    )


_MiscIsFaxUsed_Type.__name__ = "Integer32"
_MiscIsFaxUsed_Object = MibScalar
miscIsFaxUsed = _MiscIsFaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 7),
    _MiscIsFaxUsed_Type()
)
miscIsFaxUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscIsFaxUsed.setStatus("current")


class _MiscDelayTime_Type(Unsigned32):
    """Custom type miscDelayTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_MiscDelayTime_Type.__name__ = "Unsigned32"
_MiscDelayTime_Object = MibScalar
miscDelayTime = _MiscDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 8),
    _MiscDelayTime_Type()
)
miscDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscDelayTime.setStatus("current")


class _MiscDetFaxOnAnswerTone_Type(Integer32):
    """Custom type miscDetFaxOnAnswerTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscDetFaxOnAnswerTone_Type.__name__ = "Integer32"
_MiscDetFaxOnAnswerTone_Object = MibScalar
miscDetFaxOnAnswerTone = _MiscDetFaxOnAnswerTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 9),
    _MiscDetFaxOnAnswerTone_Type()
)
miscDetFaxOnAnswerTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscDetFaxOnAnswerTone.setStatus("current")


class _MiscDefaultReleaseCause_Type(Unsigned32):
    """Custom type miscDefaultReleaseCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MiscDefaultReleaseCause_Type.__name__ = "Unsigned32"
_MiscDefaultReleaseCause_Object = MibScalar
miscDefaultReleaseCause = _MiscDefaultReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 10),
    _MiscDefaultReleaseCause_Type()
)
miscDefaultReleaseCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscDefaultReleaseCause.setStatus("current")


class _MiscT38UseRTPPort_Type(Integer32):
    """Custom type miscT38UseRTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscT38UseRTPPort_Type.__name__ = "Integer32"
_MiscT38UseRTPPort_Object = MibScalar
miscT38UseRTPPort = _MiscT38UseRTPPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 11),
    _MiscT38UseRTPPort_Type()
)
miscT38UseRTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscT38UseRTPPort.setStatus("current")


class _MiscRFC2833PayloadType_Type(Unsigned32):
    """Custom type miscRFC2833PayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_MiscRFC2833PayloadType_Type.__name__ = "Unsigned32"
_MiscRFC2833PayloadType_Object = MibScalar
miscRFC2833PayloadType = _MiscRFC2833PayloadType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 12),
    _MiscRFC2833PayloadType_Type()
)
miscRFC2833PayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscRFC2833PayloadType.setStatus("current")


class _MiscIsCiscoSceMode_Type(Integer32):
    """Custom type miscIsCiscoSceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscIsCiscoSceMode_Type.__name__ = "Integer32"
_MiscIsCiscoSceMode_Object = MibScalar
miscIsCiscoSceMode = _MiscIsCiscoSceMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 13),
    _MiscIsCiscoSceMode_Type()
)
miscIsCiscoSceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscIsCiscoSceMode.setStatus("current")


class _MiscDisconnectOnDialTone_Type(Integer32):
    """Custom type miscDisconnectOnDialTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscDisconnectOnDialTone_Type.__name__ = "Integer32"
_MiscDisconnectOnDialTone_Object = MibScalar
miscDisconnectOnDialTone = _MiscDisconnectOnDialTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 14),
    _MiscDisconnectOnDialTone_Type()
)
miscDisconnectOnDialTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscDisconnectOnDialTone.setStatus("current")


class _MiscEnableSemiAttendedTransfer_Type(Integer32):
    """Custom type miscEnableSemiAttendedTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscEnableSemiAttendedTransfer_Type.__name__ = "Integer32"
_MiscEnableSemiAttendedTransfer_Object = MibScalar
miscEnableSemiAttendedTransfer = _MiscEnableSemiAttendedTransfer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 15),
    _MiscEnableSemiAttendedTransfer_Type()
)
miscEnableSemiAttendedTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscEnableSemiAttendedTransfer.setStatus("obsolete")


class _MiscHookFlashCodeIP_Type(SnmpAdminString):
    """Custom type miscHookFlashCodeIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_MiscHookFlashCodeIP_Type.__name__ = "SnmpAdminString"
_MiscHookFlashCodeIP_Object = MibScalar
miscHookFlashCodeIP = _MiscHookFlashCodeIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 16),
    _MiscHookFlashCodeIP_Type()
)
miscHookFlashCodeIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscHookFlashCodeIP.setStatus("current")


class _MiscEnableFaxRerouting_Type(Integer32):
    """Custom type miscEnableFaxRerouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscEnableFaxRerouting_Type.__name__ = "Integer32"
_MiscEnableFaxRerouting_Object = MibScalar
miscEnableFaxRerouting = _MiscEnableFaxRerouting_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 17),
    _MiscEnableFaxRerouting_Type()
)
miscEnableFaxRerouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscEnableFaxRerouting.setStatus("current")


class _MiscT38MaxDatagramSize_Type(Unsigned32):
    """Custom type miscT38MaxDatagramSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(122, 1024),
    )


_MiscT38MaxDatagramSize_Type.__name__ = "Unsigned32"
_MiscT38MaxDatagramSize_Object = MibScalar
miscT38MaxDatagramSize = _MiscT38MaxDatagramSize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 18),
    _MiscT38MaxDatagramSize_Type()
)
miscT38MaxDatagramSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscT38MaxDatagramSize.setStatus("current")


class _MiscIsdnDisconnectOnBusyTone_Type(Integer32):
    """Custom type miscIsdnDisconnectOnBusyTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscIsdnDisconnectOnBusyTone_Type.__name__ = "Integer32"
_MiscIsdnDisconnectOnBusyTone_Object = MibScalar
miscIsdnDisconnectOnBusyTone = _MiscIsdnDisconnectOnBusyTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 19),
    _MiscIsdnDisconnectOnBusyTone_Type()
)
miscIsdnDisconnectOnBusyTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscIsdnDisconnectOnBusyTone.setStatus("current")


class _MiscFaxCNGMode_Type(Integer32):
    """Custom type miscFaxCNGMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscFaxCNGMode_Type.__name__ = "Integer32"
_MiscFaxCNGMode_Object = MibScalar
miscFaxCNGMode = _MiscFaxCNGMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 20),
    _MiscFaxCNGMode_Type()
)
miscFaxCNGMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscFaxCNGMode.setStatus("current")


class _MiscGracefulBusyOutTimeout_Type(Unsigned32):
    """Custom type miscGracefulBusyOutTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MiscGracefulBusyOutTimeout_Type.__name__ = "Unsigned32"
_MiscGracefulBusyOutTimeout_Object = MibScalar
miscGracefulBusyOutTimeout = _MiscGracefulBusyOutTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 21),
    _MiscGracefulBusyOutTimeout_Type()
)
miscGracefulBusyOutTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscGracefulBusyOutTimeout.setStatus("current")


class _MiscT38FaxMaxBufferSize_Type(Unsigned32):
    """Custom type miscT38FaxMaxBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1024),
    )


_MiscT38FaxMaxBufferSize_Type.__name__ = "Unsigned32"
_MiscT38FaxMaxBufferSize_Object = MibScalar
miscT38FaxMaxBufferSize = _MiscT38FaxMaxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 22),
    _MiscT38FaxMaxBufferSize_Type()
)
miscT38FaxMaxBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscT38FaxMaxBufferSize.setStatus("current")


class _MiscReliableConnectionPersistentMode_Type(Integer32):
    """Custom type miscReliableConnectionPersistentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscReliableConnectionPersistentMode_Type.__name__ = "Integer32"
_MiscReliableConnectionPersistentMode_Object = MibScalar
miscReliableConnectionPersistentMode = _MiscReliableConnectionPersistentMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 23),
    _MiscReliableConnectionPersistentMode_Type()
)
miscReliableConnectionPersistentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscReliableConnectionPersistentMode.setStatus("current")
_MiscWANIPAddress_Type = InetAddress
_MiscWANIPAddress_Object = MibScalar
miscWANIPAddress = _MiscWANIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 24),
    _MiscWANIPAddress_Type()
)
miscWANIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscWANIPAddress.setStatus("current")


class _MiscEnableDelayedOffer_Type(Integer32):
    """Custom type miscEnableDelayedOffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscEnableDelayedOffer_Type.__name__ = "Integer32"
_MiscEnableDelayedOffer_Object = MibScalar
miscEnableDelayedOffer = _MiscEnableDelayedOffer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 25),
    _MiscEnableDelayedOffer_Type()
)
miscEnableDelayedOffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscEnableDelayedOffer.setStatus("current")


class _MiscEnableNRTSubscription_Type(Integer32):
    """Custom type miscEnableNRTSubscription based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscEnableNRTSubscription_Type.__name__ = "Integer32"
_MiscEnableNRTSubscription_Object = MibScalar
miscEnableNRTSubscription = _MiscEnableNRTSubscription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 26),
    _MiscEnableNRTSubscription_Type()
)
miscEnableNRTSubscription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscEnableNRTSubscription.setStatus("current")


class _MiscASSubscribeIPGroupID_Type(Integer32):
    """Custom type miscASSubscribeIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65525),
    )


_MiscASSubscribeIPGroupID_Type.__name__ = "Integer32"
_MiscASSubscribeIPGroupID_Object = MibScalar
miscASSubscribeIPGroupID = _MiscASSubscribeIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 27),
    _MiscASSubscribeIPGroupID_Type()
)
miscASSubscribeIPGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscASSubscribeIPGroupID.setStatus("current")


class _MiscNRTSubscriptionRetryTime_Type(Unsigned32):
    """Custom type miscNRTSubscriptionRetryTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_MiscNRTSubscriptionRetryTime_Type.__name__ = "Unsigned32"
_MiscNRTSubscriptionRetryTime_Object = MibScalar
miscNRTSubscriptionRetryTime = _MiscNRTSubscriptionRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 28),
    _MiscNRTSubscriptionRetryTime_Type()
)
miscNRTSubscriptionRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscNRTSubscriptionRetryTime.setStatus("current")


class _MiscCallForwardRingToneID_Type(Unsigned32):
    """Custom type miscCallForwardRingToneID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65525),
    )


_MiscCallForwardRingToneID_Type.__name__ = "Unsigned32"
_MiscCallForwardRingToneID_Object = MibScalar
miscCallForwardRingToneID = _MiscCallForwardRingToneID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 29),
    _MiscCallForwardRingToneID_Type()
)
miscCallForwardRingToneID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscCallForwardRingToneID.setStatus("current")


class _MiscKeyCallPickup_Type(SnmpAdminString):
    """Custom type miscKeyCallPickup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MiscKeyCallPickup_Type.__name__ = "SnmpAdminString"
_MiscKeyCallPickup_Object = MibScalar
miscKeyCallPickup = _MiscKeyCallPickup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 30),
    _MiscKeyCallPickup_Type()
)
miscKeyCallPickup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscKeyCallPickup.setStatus("current")


class _MiscEnableRFC4117Transcoding_Type(Integer32):
    """Custom type miscEnableRFC4117Transcoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscEnableRFC4117Transcoding_Type.__name__ = "Integer32"
_MiscEnableRFC4117Transcoding_Object = MibScalar
miscEnableRFC4117Transcoding = _MiscEnableRFC4117Transcoding_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 31),
    _MiscEnableRFC4117Transcoding_Type()
)
miscEnableRFC4117Transcoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscEnableRFC4117Transcoding.setStatus("current")


class _MiscEnableSingleDSPTranscoding_Type(Integer32):
    """Custom type miscEnableSingleDSPTranscoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscEnableSingleDSPTranscoding_Type.__name__ = "Integer32"
_MiscEnableSingleDSPTranscoding_Object = MibScalar
miscEnableSingleDSPTranscoding = _MiscEnableSingleDSPTranscoding_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 32),
    _MiscEnableSingleDSPTranscoding_Type()
)
miscEnableSingleDSPTranscoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscEnableSingleDSPTranscoding.setStatus("current")


class _MiscEnableNetworkISDNTransfer_Type(Integer32):
    """Custom type miscEnableNetworkISDNTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MiscEnableNetworkISDNTransfer_Type.__name__ = "Integer32"
_MiscEnableNetworkISDNTransfer_Object = MibScalar
miscEnableNetworkISDNTransfer = _MiscEnableNetworkISDNTransfer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 33),
    _MiscEnableNetworkISDNTransfer_Type()
)
miscEnableNetworkISDNTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscEnableNetworkISDNTransfer.setStatus("current")


class _MiscLDAPocsNumberAttributeName_Type(SnmpAdminString):
    """Custom type miscLDAPocsNumberAttributeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_MiscLDAPocsNumberAttributeName_Type.__name__ = "SnmpAdminString"
_MiscLDAPocsNumberAttributeName_Object = MibScalar
miscLDAPocsNumberAttributeName = _MiscLDAPocsNumberAttributeName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 34),
    _MiscLDAPocsNumberAttributeName_Type()
)
miscLDAPocsNumberAttributeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscLDAPocsNumberAttributeName.setStatus("current")


class _MiscLDAPpbxNumberAttributeName_Type(SnmpAdminString):
    """Custom type miscLDAPpbxNumberAttributeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_MiscLDAPpbxNumberAttributeName_Type.__name__ = "SnmpAdminString"
_MiscLDAPpbxNumberAttributeName_Object = MibScalar
miscLDAPpbxNumberAttributeName = _MiscLDAPpbxNumberAttributeName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 35),
    _MiscLDAPpbxNumberAttributeName_Type()
)
miscLDAPpbxNumberAttributeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscLDAPpbxNumberAttributeName.setStatus("current")


class _MiscLDAPMobileNumberAttributeName_Type(SnmpAdminString):
    """Custom type miscLDAPMobileNumberAttributeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_MiscLDAPMobileNumberAttributeName_Type.__name__ = "SnmpAdminString"
_MiscLDAPMobileNumberAttributeName_Object = MibScalar
miscLDAPMobileNumberAttributeName = _MiscLDAPMobileNumberAttributeName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 11, 36),
    _MiscLDAPMobileNumberAttributeName_Type()
)
miscLDAPMobileNumberAttributeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscLDAPMobileNumberAttributeName.setStatus("current")
_ResourceManagement_ObjectIdentity = ObjectIdentity
resourceManagement = _ResourceManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 12)
)


class _ResourceManagementMaxActiveCalls_Type(Unsigned32):
    """Custom type resourceManagementMaxActiveCalls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2016),
    )


_ResourceManagementMaxActiveCalls_Type.__name__ = "Unsigned32"
_ResourceManagementMaxActiveCalls_Object = MibScalar
resourceManagementMaxActiveCalls = _ResourceManagementMaxActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 12, 1),
    _ResourceManagementMaxActiveCalls_Type()
)
resourceManagementMaxActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resourceManagementMaxActiveCalls.setStatus("current")


class _ResourceManagementIsSelfCheckAuditUsed_Type(Integer32):
    """Custom type resourceManagementIsSelfCheckAuditUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ResourceManagementIsSelfCheckAuditUsed_Type.__name__ = "Integer32"
_ResourceManagementIsSelfCheckAuditUsed_Object = MibScalar
resourceManagementIsSelfCheckAuditUsed = _ResourceManagementIsSelfCheckAuditUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 12, 2),
    _ResourceManagementIsSelfCheckAuditUsed_Type()
)
resourceManagementIsSelfCheckAuditUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resourceManagementIsSelfCheckAuditUsed.setStatus("current")


class _ResourceManagementRejectCallsOnOverload_Type(Integer32):
    """Custom type resourceManagementRejectCallsOnOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ResourceManagementRejectCallsOnOverload_Type.__name__ = "Integer32"
_ResourceManagementRejectCallsOnOverload_Object = MibScalar
resourceManagementRejectCallsOnOverload = _ResourceManagementRejectCallsOnOverload_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 12, 3),
    _ResourceManagementRejectCallsOnOverload_Type()
)
resourceManagementRejectCallsOnOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resourceManagementRejectCallsOnOverload.setStatus("obsolete")


class _ResourceManagementDisconnectOnBrokenConnection_Type(Integer32):
    """Custom type resourceManagementDisconnectOnBrokenConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ResourceManagementDisconnectOnBrokenConnection_Type.__name__ = "Integer32"
_ResourceManagementDisconnectOnBrokenConnection_Object = MibScalar
resourceManagementDisconnectOnBrokenConnection = _ResourceManagementDisconnectOnBrokenConnection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 12, 4),
    _ResourceManagementDisconnectOnBrokenConnection_Type()
)
resourceManagementDisconnectOnBrokenConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resourceManagementDisconnectOnBrokenConnection.setStatus("current")


class _ResourceManagementMaxCallDuration_Type(Unsigned32):
    """Custom type resourceManagementMaxCallDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35791),
    )


_ResourceManagementMaxCallDuration_Type.__name__ = "Unsigned32"
_ResourceManagementMaxCallDuration_Object = MibScalar
resourceManagementMaxCallDuration = _ResourceManagementMaxCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 12, 5),
    _ResourceManagementMaxCallDuration_Type()
)
resourceManagementMaxCallDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resourceManagementMaxCallDuration.setStatus("current")


class _ResourceManagementOverloadSensitivityLevel_Type(Integer32):
    """Custom type resourceManagementOverloadSensitivityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highUtil", 1),
          ("medUtil", 2),
          ("never", 0))
    )


_ResourceManagementOverloadSensitivityLevel_Type.__name__ = "Integer32"
_ResourceManagementOverloadSensitivityLevel_Object = MibScalar
resourceManagementOverloadSensitivityLevel = _ResourceManagementOverloadSensitivityLevel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 12, 6),
    _ResourceManagementOverloadSensitivityLevel_Type()
)
resourceManagementOverloadSensitivityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resourceManagementOverloadSensitivityLevel.setStatus("current")
_AMD_ObjectIdentity = ObjectIdentity
aMD = _AMD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 13)
)


class _AMDTimeOut_Type(Unsigned32):
    """Custom type aMDTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30000),
    )


_AMDTimeOut_Type.__name__ = "Unsigned32"
_AMDTimeOut_Object = MibScalar
aMDTimeOut = _AMDTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 13, 1),
    _AMDTimeOut_Type()
)
aMDTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aMDTimeOut.setStatus("current")
_Aaa_ObjectIdentity = ObjectIdentity
aaa = _Aaa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 14)
)


class _AaaIndications_Type(Integer32):
    """Custom type aaaIndications based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accountingOnly", 3),
          ("authorizeAndAuthenticate", 1),
          ("fullReport", 2),
          ("none", 0))
    )


_AaaIndications_Type.__name__ = "Integer32"
_AaaIndications_Object = MibScalar
aaaIndications = _AaaIndications_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 14, 1),
    _AaaIndications_Type()
)
aaaIndications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaIndications.setStatus("current")


class _AaaRadiusAccountingType_Type(Integer32):
    """Custom type aaaRadiusAccountingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connectAndRelease", 1),
          ("release", 0),
          ("setupAndRelease", 2))
    )


_AaaRadiusAccountingType_Type.__name__ = "Integer32"
_AaaRadiusAccountingType_Object = MibScalar
aaaRadiusAccountingType = _AaaRadiusAccountingType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 14, 2),
    _AaaRadiusAccountingType_Type()
)
aaaRadiusAccountingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadiusAccountingType.setStatus("current")
_Profile_ObjectIdentity = ObjectIdentity
profile = _Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15)
)
_IPProfileTable_Object = MibTable
iPProfileTable = _IPProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21)
)
if mibBuilder.loadTexts:
    iPProfileTable.setStatus("current")
_IPProfileEntry_Object = MibTableRow
iPProfileEntry = _IPProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1)
)
iPProfileEntry.setIndexNames(
    (0, "AcGateway", "iPProfileIndex"),
)
if mibBuilder.loadTexts:
    iPProfileEntry.setStatus("current")


class _IPProfileIndex_Type(Unsigned32):
    """Custom type iPProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_IPProfileIndex_Type.__name__ = "Unsigned32"
_IPProfileIndex_Object = MibTableColumn
iPProfileIndex = _IPProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 1),
    _IPProfileIndex_Type()
)
iPProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iPProfileIndex.setStatus("current")
_IPProfileRowStatus_Type = RowStatus
_IPProfileRowStatus_Object = MibTableColumn
iPProfileRowStatus = _IPProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 2),
    _IPProfileRowStatus_Type()
)
iPProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileRowStatus.setStatus("current")


class _IPProfileAction_Type(Integer32):
    """Custom type iPProfileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_IPProfileAction_Type.__name__ = "Integer32"
_IPProfileAction_Object = MibTableColumn
iPProfileAction = _IPProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 3),
    _IPProfileAction_Type()
)
iPProfileAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPProfileAction.setStatus("current")


class _IPProfileActionResult_Type(Integer32):
    """Custom type iPProfileActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_IPProfileActionResult_Type.__name__ = "Integer32"
_IPProfileActionResult_Object = MibTableColumn
iPProfileActionResult = _IPProfileActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 4),
    _IPProfileActionResult_Type()
)
iPProfileActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPProfileActionResult.setStatus("current")


class _IPProfilePreference_Type(Unsigned32):
    """Custom type iPProfilePreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_IPProfilePreference_Type.__name__ = "Unsigned32"
_IPProfilePreference_Object = MibTableColumn
iPProfilePreference = _IPProfilePreference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 5),
    _IPProfilePreference_Type()
)
iPProfilePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfilePreference.setStatus("current")


class _IPProfileProfileName_Type(SnmpAdminString):
    """Custom type iPProfileProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_IPProfileProfileName_Type.__name__ = "SnmpAdminString"
_IPProfileProfileName_Object = MibTableColumn
iPProfileProfileName = _IPProfileProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 6),
    _IPProfileProfileName_Type()
)
iPProfileProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileProfileName.setStatus("current")


class _IPProfileCodersGroupID_Type(Unsigned32):
    """Custom type iPProfileCodersGroupID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_IPProfileCodersGroupID_Type.__name__ = "Unsigned32"
_IPProfileCodersGroupID_Object = MibTableColumn
iPProfileCodersGroupID = _IPProfileCodersGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 7),
    _IPProfileCodersGroupID_Type()
)
iPProfileCodersGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileCodersGroupID.setStatus("current")


class _IPProfileFaxTransportMode_Type(Unsigned32):
    """Custom type iPProfileFaxTransportMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IPProfileFaxTransportMode_Type.__name__ = "Unsigned32"
_IPProfileFaxTransportMode_Object = MibTableColumn
iPProfileFaxTransportMode = _IPProfileFaxTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 8),
    _IPProfileFaxTransportMode_Type()
)
iPProfileFaxTransportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iPProfileFaxTransportMode.setStatus("obsolete")


class _IPProfileIsFaxUsed_Type(Integer32):
    """Custom type iPProfileIsFaxUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fallBack", 3),
          ("g711", 2),
          ("noFax", 0),
          ("notConfigured", 255),
          ("t38", 1))
    )


_IPProfileIsFaxUsed_Type.__name__ = "Integer32"
_IPProfileIsFaxUsed_Object = MibTableColumn
iPProfileIsFaxUsed = _IPProfileIsFaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 9),
    _IPProfileIsFaxUsed_Type()
)
iPProfileIsFaxUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileIsFaxUsed.setStatus("current")


class _IPProfileDJBufMinDelay_Type(Unsigned32):
    """Custom type iPProfileDJBufMinDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IPProfileDJBufMinDelay_Type.__name__ = "Unsigned32"
_IPProfileDJBufMinDelay_Object = MibTableColumn
iPProfileDJBufMinDelay = _IPProfileDJBufMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 10),
    _IPProfileDJBufMinDelay_Type()
)
iPProfileDJBufMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileDJBufMinDelay.setStatus("current")


class _IPProfileDJBufOptFactor_Type(Unsigned32):
    """Custom type iPProfileDJBufOptFactor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IPProfileDJBufOptFactor_Type.__name__ = "Unsigned32"
_IPProfileDJBufOptFactor_Object = MibTableColumn
iPProfileDJBufOptFactor = _IPProfileDJBufOptFactor_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 11),
    _IPProfileDJBufOptFactor_Type()
)
iPProfileDJBufOptFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileDJBufOptFactor.setStatus("current")


class _IPProfileIPDiffServ_Type(Unsigned32):
    """Custom type iPProfileIPDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IPProfileIPDiffServ_Type.__name__ = "Unsigned32"
_IPProfileIPDiffServ_Object = MibTableColumn
iPProfileIPDiffServ = _IPProfileIPDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 12),
    _IPProfileIPDiffServ_Type()
)
iPProfileIPDiffServ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileIPDiffServ.setStatus("current")


class _IPProfileSigIPDiffServ_Type(Unsigned32):
    """Custom type iPProfileSigIPDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IPProfileSigIPDiffServ_Type.__name__ = "Unsigned32"
_IPProfileSigIPDiffServ_Object = MibTableColumn
iPProfileSigIPDiffServ = _IPProfileSigIPDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 13),
    _IPProfileSigIPDiffServ_Type()
)
iPProfileSigIPDiffServ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileSigIPDiffServ.setStatus("current")


class _IPProfileSCE_Type(Integer32):
    """Custom type iPProfileSCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("enableWithoutAdaptation", 2),
          ("notConfigured", 255))
    )


_IPProfileSCE_Type.__name__ = "Integer32"
_IPProfileSCE_Object = MibTableColumn
iPProfileSCE = _IPProfileSCE_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 14),
    _IPProfileSCE_Type()
)
iPProfileSCE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileSCE.setStatus("current")


class _IPProfileRTPRedundancyDepth_Type(Unsigned32):
    """Custom type iPProfileRTPRedundancyDepth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IPProfileRTPRedundancyDepth_Type.__name__ = "Unsigned32"
_IPProfileRTPRedundancyDepth_Object = MibTableColumn
iPProfileRTPRedundancyDepth = _IPProfileRTPRedundancyDepth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 15),
    _IPProfileRTPRedundancyDepth_Type()
)
iPProfileRTPRedundancyDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileRTPRedundancyDepth.setStatus("current")


class _IPProfileRemoteBaseUDPPort_Type(Unsigned32):
    """Custom type iPProfileRemoteBaseUDPPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IPProfileRemoteBaseUDPPort_Type.__name__ = "Unsigned32"
_IPProfileRemoteBaseUDPPort_Object = MibTableColumn
iPProfileRemoteBaseUDPPort = _IPProfileRemoteBaseUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 16),
    _IPProfileRemoteBaseUDPPort_Type()
)
iPProfileRemoteBaseUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileRemoteBaseUDPPort.setStatus("current")


class _IPProfileCngDetectorMode_Type(Integer32):
    """Custom type iPProfileCngDetectorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("eventsOnly", 2),
          ("notConfigured", 255),
          ("relay", 1))
    )


_IPProfileCngDetectorMode_Type.__name__ = "Integer32"
_IPProfileCngDetectorMode_Object = MibTableColumn
iPProfileCngDetectorMode = _IPProfileCngDetectorMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 17),
    _IPProfileCngDetectorMode_Type()
)
iPProfileCngDetectorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileCngDetectorMode.setStatus("current")


class _IPProfileVxxModemTransportType_Type(Integer32):
    """Custom type iPProfileVxxModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enableBypass", 2),
          ("enableRelay", 1),
          ("eventsOnly", 3),
          ("notConfigured", 255))
    )


_IPProfileVxxModemTransportType_Type.__name__ = "Integer32"
_IPProfileVxxModemTransportType_Object = MibTableColumn
iPProfileVxxModemTransportType = _IPProfileVxxModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 18),
    _IPProfileVxxModemTransportType_Type()
)
iPProfileVxxModemTransportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileVxxModemTransportType.setStatus("current")


class _IPProfileNSEMode_Type(Integer32):
    """Custom type iPProfileNSEMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", 255))
    )


_IPProfileNSEMode_Type.__name__ = "Integer32"
_IPProfileNSEMode_Object = MibTableColumn
iPProfileNSEMode = _IPProfileNSEMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 19),
    _IPProfileNSEMode_Type()
)
iPProfileNSEMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileNSEMode.setStatus("current")


class _IPProfilePlayRingbackToneToIP_Type(Integer32):
    """Custom type iPProfilePlayRingbackToneToIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 255),
          ("notPlay", 0),
          ("play", 1))
    )


_IPProfilePlayRingbackToneToIP_Type.__name__ = "Integer32"
_IPProfilePlayRingbackToneToIP_Object = MibTableColumn
iPProfilePlayRingbackToneToIP = _IPProfilePlayRingbackToneToIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 20),
    _IPProfilePlayRingbackToneToIP_Type()
)
iPProfilePlayRingbackToneToIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfilePlayRingbackToneToIP.setStatus("current")


class _IPProfileEnableEarlyMedia_Type(Integer32):
    """Custom type iPProfileEnableEarlyMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", 255))
    )


_IPProfileEnableEarlyMedia_Type.__name__ = "Integer32"
_IPProfileEnableEarlyMedia_Object = MibTableColumn
iPProfileEnableEarlyMedia = _IPProfileEnableEarlyMedia_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 21),
    _IPProfileEnableEarlyMedia_Type()
)
iPProfileEnableEarlyMedia.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileEnableEarlyMedia.setStatus("current")


class _IPProfileProgressIndicatorToIP_Type(Integer32):
    """Custom type iPProfileProgressIndicatorToIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noPI", 0),
          ("notConfigured", 255),
          ("pI1", 1),
          ("pI8", 8))
    )


_IPProfileProgressIndicatorToIP_Type.__name__ = "Integer32"
_IPProfileProgressIndicatorToIP_Object = MibTableColumn
iPProfileProgressIndicatorToIP = _IPProfileProgressIndicatorToIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 22),
    _IPProfileProgressIndicatorToIP_Type()
)
iPProfileProgressIndicatorToIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileProgressIndicatorToIP.setStatus("current")


class _IPProfileECE_Type(Integer32):
    """Custom type iPProfileECE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", -1))
    )


_IPProfileECE_Type.__name__ = "Integer32"
_IPProfileECE_Object = MibTableColumn
iPProfileECE = _IPProfileECE_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 23),
    _IPProfileECE_Type()
)
iPProfileECE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileECE.setStatus("current")


class _IPProfileMediaSecurityBehavior_Type(Integer32):
    """Custom type iPProfileMediaSecurityBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mandatory", 1),
          ("notConfigured", -1),
          ("preferable", 0))
    )


_IPProfileMediaSecurityBehavior_Type.__name__ = "Integer32"
_IPProfileMediaSecurityBehavior_Object = MibTableColumn
iPProfileMediaSecurityBehavior = _IPProfileMediaSecurityBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 24),
    _IPProfileMediaSecurityBehavior_Type()
)
iPProfileMediaSecurityBehavior.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileMediaSecurityBehavior.setStatus("current")


class _IPProfileCallLimit_Type(Integer32):
    """Custom type iPProfileCallLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 200000),
    )


_IPProfileCallLimit_Type.__name__ = "Integer32"
_IPProfileCallLimit_Object = MibTableColumn
iPProfileCallLimit = _IPProfileCallLimit_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 25),
    _IPProfileCallLimit_Type()
)
iPProfileCallLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileCallLimit.setStatus("current")


class _IPProfileDisconnectOnBrokenConnection_Type(Integer32):
    """Custom type iPProfileDisconnectOnBrokenConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notConfigured", -1),
          ("yes", 1))
    )


_IPProfileDisconnectOnBrokenConnection_Type.__name__ = "Integer32"
_IPProfileDisconnectOnBrokenConnection_Object = MibTableColumn
iPProfileDisconnectOnBrokenConnection = _IPProfileDisconnectOnBrokenConnection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 26),
    _IPProfileDisconnectOnBrokenConnection_Type()
)
iPProfileDisconnectOnBrokenConnection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileDisconnectOnBrokenConnection.setStatus("current")


class _IPProfileCopyDest2RedirectNumber_Type(Integer32):
    """Custom type iPProfileCopyDest2RedirectNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("afterManipulation", 1),
          ("beforeManipulation", 2),
          ("disable", 0),
          ("notConfigured", -1))
    )


_IPProfileCopyDest2RedirectNumber_Type.__name__ = "Integer32"
_IPProfileCopyDest2RedirectNumber_Object = MibTableColumn
iPProfileCopyDest2RedirectNumber = _IPProfileCopyDest2RedirectNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 27),
    _IPProfileCopyDest2RedirectNumber_Type()
)
iPProfileCopyDest2RedirectNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileCopyDest2RedirectNumber.setStatus("current")


class _IPProfileAddIEInSetup_Type(SnmpAdminString):
    """Custom type iPProfileAddIEInSetup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 98),
    )


_IPProfileAddIEInSetup_Type.__name__ = "SnmpAdminString"
_IPProfileAddIEInSetup_Object = MibTableColumn
iPProfileAddIEInSetup = _IPProfileAddIEInSetup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 28),
    _IPProfileAddIEInSetup_Type()
)
iPProfileAddIEInSetup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileAddIEInSetup.setStatus("current")


class _IPProfileRxDTMFOption_Type(Integer32):
    """Custom type iPProfileRxDTMFOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("declareRFC2833InSDP", 1),
          ("notConfigured", -1),
          ("notDeclared", 0))
    )


_IPProfileRxDTMFOption_Type.__name__ = "Integer32"
_IPProfileRxDTMFOption_Object = MibTableColumn
iPProfileRxDTMFOption = _IPProfileRxDTMFOption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 29),
    _IPProfileRxDTMFOption_Type()
)
iPProfileRxDTMFOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileRxDTMFOption.setStatus("current")


class _IPProfileFirstTxDtmfOption_Type(Integer32):
    """Custom type iPProfileFirstTxDtmfOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("infoCisco", 3),
          ("infoKorea", 5),
          ("infoNortel", 1),
          ("notConfigured", -1),
          ("notSupported", 0),
          ("notify", 2),
          ("rFC2833", 4))
    )


_IPProfileFirstTxDtmfOption_Type.__name__ = "Integer32"
_IPProfileFirstTxDtmfOption_Object = MibTableColumn
iPProfileFirstTxDtmfOption = _IPProfileFirstTxDtmfOption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 30),
    _IPProfileFirstTxDtmfOption_Type()
)
iPProfileFirstTxDtmfOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileFirstTxDtmfOption.setStatus("current")


class _IPProfileSecondTxDtmfOption_Type(Integer32):
    """Custom type iPProfileSecondTxDtmfOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("infoCisco", 3),
          ("infoKorea", 5),
          ("infoNortel", 1),
          ("notConfigured", -1),
          ("notSupported", 0),
          ("notify", 2),
          ("rFC2833", 4))
    )


_IPProfileSecondTxDtmfOption_Type.__name__ = "Integer32"
_IPProfileSecondTxDtmfOption_Object = MibTableColumn
iPProfileSecondTxDtmfOption = _IPProfileSecondTxDtmfOption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 31),
    _IPProfileSecondTxDtmfOption_Type()
)
iPProfileSecondTxDtmfOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileSecondTxDtmfOption.setStatus("current")


class _IPProfileMediaIPVersionPreference_Type(Integer32):
    """Custom type iPProfileMediaIPVersionPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", -1),
          ("onlyIPv4", 0),
          ("onlyIPv6", 1),
          ("preferIPv4", 2),
          ("preferIPv6", 3))
    )


_IPProfileMediaIPVersionPreference_Type.__name__ = "Integer32"
_IPProfileMediaIPVersionPreference_Object = MibTableColumn
iPProfileMediaIPVersionPreference = _IPProfileMediaIPVersionPreference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 32),
    _IPProfileMediaIPVersionPreference_Type()
)
iPProfileMediaIPVersionPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileMediaIPVersionPreference.setStatus("current")


class _IPProfileSBCAllowedCodersGroupID_Type(Integer32):
    """Custom type iPProfileSBCAllowedCodersGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("codersGroup0", 0),
          ("codersGroup1", 1),
          ("codersGroup2", 2),
          ("codersGroup3", 3),
          ("codersGroup4", 4),
          ("notConfigured", -1))
    )


_IPProfileSBCAllowedCodersGroupID_Type.__name__ = "Integer32"
_IPProfileSBCAllowedCodersGroupID_Object = MibTableColumn
iPProfileSBCAllowedCodersGroupID = _IPProfileSBCAllowedCodersGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 33),
    _IPProfileSBCAllowedCodersGroupID_Type()
)
iPProfileSBCAllowedCodersGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileSBCAllowedCodersGroupID.setStatus("current")


class _IPProfileSBCAllowedCodersMode_Type(Integer32):
    """Custom type iPProfileSBCAllowedCodersMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preference", 1),
          ("restictionAndPreference", 2),
          ("restriction", 0))
    )


_IPProfileSBCAllowedCodersMode_Type.__name__ = "Integer32"
_IPProfileSBCAllowedCodersMode_Object = MibTableColumn
iPProfileSBCAllowedCodersMode = _IPProfileSBCAllowedCodersMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 34),
    _IPProfileSBCAllowedCodersMode_Type()
)
iPProfileSBCAllowedCodersMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileSBCAllowedCodersMode.setStatus("current")


class _IPProfileSBCMediaSecurityBehaviour_Type(Integer32):
    """Custom type iPProfileSBCMediaSecurityBehaviour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asIs", 0),
          ("both", 3),
          ("rtp", 2),
          ("srtp", 1))
    )


_IPProfileSBCMediaSecurityBehaviour_Type.__name__ = "Integer32"
_IPProfileSBCMediaSecurityBehaviour_Object = MibTableColumn
iPProfileSBCMediaSecurityBehaviour = _IPProfileSBCMediaSecurityBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 21, 1, 35),
    _IPProfileSBCMediaSecurityBehaviour_Type()
)
iPProfileSBCMediaSecurityBehaviour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPProfileSBCMediaSecurityBehaviour.setStatus("current")
_TelProfileTable_Object = MibTable
telProfileTable = _TelProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22)
)
if mibBuilder.loadTexts:
    telProfileTable.setStatus("current")
_TelProfileEntry_Object = MibTableRow
telProfileEntry = _TelProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1)
)
telProfileEntry.setIndexNames(
    (0, "AcGateway", "telProfileIndex"),
)
if mibBuilder.loadTexts:
    telProfileEntry.setStatus("current")


class _TelProfileIndex_Type(Unsigned32):
    """Custom type telProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TelProfileIndex_Type.__name__ = "Unsigned32"
_TelProfileIndex_Object = MibTableColumn
telProfileIndex = _TelProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 1),
    _TelProfileIndex_Type()
)
telProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    telProfileIndex.setStatus("current")
_TelProfileRowStatus_Type = RowStatus
_TelProfileRowStatus_Object = MibTableColumn
telProfileRowStatus = _TelProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 2),
    _TelProfileRowStatus_Type()
)
telProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileRowStatus.setStatus("current")


class _TelProfileAction_Type(Integer32):
    """Custom type telProfileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_TelProfileAction_Type.__name__ = "Integer32"
_TelProfileAction_Object = MibTableColumn
telProfileAction = _TelProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 3),
    _TelProfileAction_Type()
)
telProfileAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProfileAction.setStatus("current")


class _TelProfileActionResult_Type(Integer32):
    """Custom type telProfileActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_TelProfileActionResult_Type.__name__ = "Integer32"
_TelProfileActionResult_Object = MibTableColumn
telProfileActionResult = _TelProfileActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 4),
    _TelProfileActionResult_Type()
)
telProfileActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telProfileActionResult.setStatus("current")


class _TelProfilePreference_Type(Unsigned32):
    """Custom type telProfilePreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_TelProfilePreference_Type.__name__ = "Unsigned32"
_TelProfilePreference_Object = MibTableColumn
telProfilePreference = _TelProfilePreference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 5),
    _TelProfilePreference_Type()
)
telProfilePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfilePreference.setStatus("current")


class _TelProfileProfileName_Type(SnmpAdminString):
    """Custom type telProfileProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_TelProfileProfileName_Type.__name__ = "SnmpAdminString"
_TelProfileProfileName_Object = MibTableColumn
telProfileProfileName = _TelProfileProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 6),
    _TelProfileProfileName_Type()
)
telProfileProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileProfileName.setStatus("current")


class _TelProfileCodersGroupID_Type(Unsigned32):
    """Custom type telProfileCodersGroupID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_TelProfileCodersGroupID_Type.__name__ = "Unsigned32"
_TelProfileCodersGroupID_Object = MibTableColumn
telProfileCodersGroupID = _TelProfileCodersGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 7),
    _TelProfileCodersGroupID_Type()
)
telProfileCodersGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileCodersGroupID.setStatus("current")


class _TelProfileFaxTransportMode_Type(Unsigned32):
    """Custom type telProfileFaxTransportMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TelProfileFaxTransportMode_Type.__name__ = "Unsigned32"
_TelProfileFaxTransportMode_Object = MibTableColumn
telProfileFaxTransportMode = _TelProfileFaxTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 8),
    _TelProfileFaxTransportMode_Type()
)
telProfileFaxTransportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telProfileFaxTransportMode.setStatus("obsolete")


class _TelProfileIsFaxUsed_Type(Integer32):
    """Custom type telProfileIsFaxUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fallBack", 3),
          ("g711", 2),
          ("noFax", 0),
          ("notConfigured", 255),
          ("t38", 1))
    )


_TelProfileIsFaxUsed_Type.__name__ = "Integer32"
_TelProfileIsFaxUsed_Object = MibTableColumn
telProfileIsFaxUsed = _TelProfileIsFaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 9),
    _TelProfileIsFaxUsed_Type()
)
telProfileIsFaxUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileIsFaxUsed.setStatus("current")


class _TelProfileDJBufMinDelay_Type(Unsigned32):
    """Custom type telProfileDJBufMinDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelProfileDJBufMinDelay_Type.__name__ = "Unsigned32"
_TelProfileDJBufMinDelay_Object = MibTableColumn
telProfileDJBufMinDelay = _TelProfileDJBufMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 10),
    _TelProfileDJBufMinDelay_Type()
)
telProfileDJBufMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileDJBufMinDelay.setStatus("current")


class _TelProfileDJBufOptFactor_Type(Unsigned32):
    """Custom type telProfileDJBufOptFactor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelProfileDJBufOptFactor_Type.__name__ = "Unsigned32"
_TelProfileDJBufOptFactor_Object = MibTableColumn
telProfileDJBufOptFactor = _TelProfileDJBufOptFactor_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 11),
    _TelProfileDJBufOptFactor_Type()
)
telProfileDJBufOptFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileDJBufOptFactor.setStatus("current")


class _TelProfileIPDiffServ_Type(Unsigned32):
    """Custom type telProfileIPDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelProfileIPDiffServ_Type.__name__ = "Unsigned32"
_TelProfileIPDiffServ_Object = MibTableColumn
telProfileIPDiffServ = _TelProfileIPDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 12),
    _TelProfileIPDiffServ_Type()
)
telProfileIPDiffServ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileIPDiffServ.setStatus("current")


class _TelProfileSigIPDiffServ_Type(Unsigned32):
    """Custom type telProfileSigIPDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelProfileSigIPDiffServ_Type.__name__ = "Unsigned32"
_TelProfileSigIPDiffServ_Object = MibTableColumn
telProfileSigIPDiffServ = _TelProfileSigIPDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 13),
    _TelProfileSigIPDiffServ_Type()
)
telProfileSigIPDiffServ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileSigIPDiffServ.setStatus("current")


class _TelProfileVoiceVolume_Type(Integer32):
    """Custom type telProfileVoiceVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, 255),
    )


_TelProfileVoiceVolume_Type.__name__ = "Integer32"
_TelProfileVoiceVolume_Object = MibTableColumn
telProfileVoiceVolume = _TelProfileVoiceVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 14),
    _TelProfileVoiceVolume_Type()
)
telProfileVoiceVolume.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileVoiceVolume.setStatus("current")


class _TelProfileDTMFVolume_Type(Integer32):
    """Custom type telProfileDTMFVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-31, 255),
    )


_TelProfileDTMFVolume_Type.__name__ = "Integer32"
_TelProfileDTMFVolume_Object = MibTableColumn
telProfileDTMFVolume = _TelProfileDTMFVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 15),
    _TelProfileDTMFVolume_Type()
)
telProfileDTMFVolume.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileDTMFVolume.setStatus("current")


class _TelProfileInputGain_Type(Integer32):
    """Custom type telProfileInputGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, 255),
    )


_TelProfileInputGain_Type.__name__ = "Integer32"
_TelProfileInputGain_Object = MibTableColumn
telProfileInputGain = _TelProfileInputGain_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 16),
    _TelProfileInputGain_Type()
)
telProfileInputGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileInputGain.setStatus("current")


class _TelProfileEnableReversalPolarity_Type(Integer32):
    """Custom type telProfileEnableReversalPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notConfigured", 255),
          ("yes", 1))
    )


_TelProfileEnableReversalPolarity_Type.__name__ = "Integer32"
_TelProfileEnableReversalPolarity_Object = MibTableColumn
telProfileEnableReversalPolarity = _TelProfileEnableReversalPolarity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 17),
    _TelProfileEnableReversalPolarity_Type()
)
telProfileEnableReversalPolarity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileEnableReversalPolarity.setStatus("current")


class _TelProfileEnableCurrentDisconnect_Type(Integer32):
    """Custom type telProfileEnableCurrentDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notConfigured", 255),
          ("yes", 1))
    )


_TelProfileEnableCurrentDisconnect_Type.__name__ = "Integer32"
_TelProfileEnableCurrentDisconnect_Object = MibTableColumn
telProfileEnableCurrentDisconnect = _TelProfileEnableCurrentDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 18),
    _TelProfileEnableCurrentDisconnect_Type()
)
telProfileEnableCurrentDisconnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileEnableCurrentDisconnect.setStatus("current")


class _TelProfileEnableDigitDelivery_Type(Integer32):
    """Custom type telProfileEnableDigitDelivery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", 255))
    )


_TelProfileEnableDigitDelivery_Type.__name__ = "Integer32"
_TelProfileEnableDigitDelivery_Object = MibTableColumn
telProfileEnableDigitDelivery = _TelProfileEnableDigitDelivery_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 19),
    _TelProfileEnableDigitDelivery_Type()
)
telProfileEnableDigitDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileEnableDigitDelivery.setStatus("current")


class _TelProfileECE_Type(Integer32):
    """Custom type telProfileECE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", 255))
    )


_TelProfileECE_Type.__name__ = "Integer32"
_TelProfileECE_Object = MibTableColumn
telProfileECE = _TelProfileECE_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 20),
    _TelProfileECE_Type()
)
telProfileECE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileECE.setStatus("current")


class _TelProfileMWIanalogLamp_Type(Integer32):
    """Custom type telProfileMWIanalogLamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", 255))
    )


_TelProfileMWIanalogLamp_Type.__name__ = "Integer32"
_TelProfileMWIanalogLamp_Object = MibTableColumn
telProfileMWIanalogLamp = _TelProfileMWIanalogLamp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 21),
    _TelProfileMWIanalogLamp_Type()
)
telProfileMWIanalogLamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileMWIanalogLamp.setStatus("current")


class _TelProfileMWIDisplay_Type(Integer32):
    """Custom type telProfileMWIDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", 255))
    )


_TelProfileMWIDisplay_Type.__name__ = "Integer32"
_TelProfileMWIDisplay_Object = MibTableColumn
telProfileMWIDisplay = _TelProfileMWIDisplay_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 22),
    _TelProfileMWIDisplay_Type()
)
telProfileMWIDisplay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileMWIDisplay.setStatus("current")


class _TelProfileMaxFlashHookDetectionPeriod_Type(Unsigned32):
    """Custom type telProfileMaxFlashHookDetectionPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_TelProfileMaxFlashHookDetectionPeriod_Type.__name__ = "Unsigned32"
_TelProfileMaxFlashHookDetectionPeriod_Object = MibTableColumn
telProfileMaxFlashHookDetectionPeriod = _TelProfileMaxFlashHookDetectionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 23),
    _TelProfileMaxFlashHookDetectionPeriod_Type()
)
telProfileMaxFlashHookDetectionPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileMaxFlashHookDetectionPeriod.setStatus("current")


class _TelProfileEnableEarlyMedia_Type(Integer32):
    """Custom type telProfileEnableEarlyMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", 255))
    )


_TelProfileEnableEarlyMedia_Type.__name__ = "Integer32"
_TelProfileEnableEarlyMedia_Object = MibTableColumn
telProfileEnableEarlyMedia = _TelProfileEnableEarlyMedia_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 24),
    _TelProfileEnableEarlyMedia_Type()
)
telProfileEnableEarlyMedia.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileEnableEarlyMedia.setStatus("current")


class _TelProfileProgressIndicatorToIP_Type(Integer32):
    """Custom type telProfileProgressIndicatorToIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noPI", 0),
          ("notConfigured", 255),
          ("pI1", 1),
          ("pI8", 8))
    )


_TelProfileProgressIndicatorToIP_Type.__name__ = "Integer32"
_TelProfileProgressIndicatorToIP_Object = MibTableColumn
telProfileProgressIndicatorToIP = _TelProfileProgressIndicatorToIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 25),
    _TelProfileProgressIndicatorToIP_Type()
)
telProfileProgressIndicatorToIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileProgressIndicatorToIP.setStatus("current")


class _TelProfileTimeForReorderTone_Type(Unsigned32):
    """Custom type telProfileTimeForReorderTone based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelProfileTimeForReorderTone_Type.__name__ = "Unsigned32"
_TelProfileTimeForReorderTone_Object = MibTableColumn
telProfileTimeForReorderTone = _TelProfileTimeForReorderTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 26),
    _TelProfileTimeForReorderTone_Type()
)
telProfileTimeForReorderTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileTimeForReorderTone.setStatus("current")


class _TelProfileEnableDIDWink_Type(Integer32):
    """Custom type telProfileEnableDIDWink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", -1))
    )


_TelProfileEnableDIDWink_Type.__name__ = "Integer32"
_TelProfileEnableDIDWink_Object = MibTableColumn
telProfileEnableDIDWink = _TelProfileEnableDIDWink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 27),
    _TelProfileEnableDIDWink_Type()
)
telProfileEnableDIDWink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileEnableDIDWink.setStatus("current")


class _TelProfileIsTwoStageDial_Type(Integer32):
    """Custom type telProfileIsTwoStageDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", -1))
    )


_TelProfileIsTwoStageDial_Type.__name__ = "Integer32"
_TelProfileIsTwoStageDial_Object = MibTableColumn
telProfileIsTwoStageDial = _TelProfileIsTwoStageDial_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 28),
    _TelProfileIsTwoStageDial_Type()
)
telProfileIsTwoStageDial.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileIsTwoStageDial.setStatus("current")


class _TelProfileDisconnectOnBusyTone_Type(Integer32):
    """Custom type telProfileDisconnectOnBusyTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("notConfigured", -1),
          ("yes", 1))
    )


_TelProfileDisconnectOnBusyTone_Type.__name__ = "Integer32"
_TelProfileDisconnectOnBusyTone_Object = MibTableColumn
telProfileDisconnectOnBusyTone = _TelProfileDisconnectOnBusyTone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 29),
    _TelProfileDisconnectOnBusyTone_Type()
)
telProfileDisconnectOnBusyTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileDisconnectOnBusyTone.setStatus("current")


class _TelProfileEnableVoiceMailDelay_Type(Integer32):
    """Custom type telProfileEnableVoiceMailDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", -1))
    )


_TelProfileEnableVoiceMailDelay_Type.__name__ = "Integer32"
_TelProfileEnableVoiceMailDelay_Object = MibTableColumn
telProfileEnableVoiceMailDelay = _TelProfileEnableVoiceMailDelay_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 30),
    _TelProfileEnableVoiceMailDelay_Type()
)
telProfileEnableVoiceMailDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileEnableVoiceMailDelay.setStatus("current")


class _TelProfileDialPlanIndex_Type(Integer32):
    """Custom type telProfileDialPlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_TelProfileDialPlanIndex_Type.__name__ = "Integer32"
_TelProfileDialPlanIndex_Object = MibTableColumn
telProfileDialPlanIndex = _TelProfileDialPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 31),
    _TelProfileDialPlanIndex_Type()
)
telProfileDialPlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileDialPlanIndex.setStatus("current")


class _TelProfileEnable911PSAP_Type(Integer32):
    """Custom type telProfileEnable911PSAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", -1))
    )


_TelProfileEnable911PSAP_Type.__name__ = "Integer32"
_TelProfileEnable911PSAP_Object = MibTableColumn
telProfileEnable911PSAP = _TelProfileEnable911PSAP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 32),
    _TelProfileEnable911PSAP_Type()
)
telProfileEnable911PSAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileEnable911PSAP.setStatus("current")


class _TelProfileSwapTelToIpPhoneNumbers_Type(Integer32):
    """Custom type telProfileSwapTelToIpPhoneNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", -1))
    )


_TelProfileSwapTelToIpPhoneNumbers_Type.__name__ = "Integer32"
_TelProfileSwapTelToIpPhoneNumbers_Object = MibTableColumn
telProfileSwapTelToIpPhoneNumbers = _TelProfileSwapTelToIpPhoneNumbers_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 33),
    _TelProfileSwapTelToIpPhoneNumbers_Type()
)
telProfileSwapTelToIpPhoneNumbers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileSwapTelToIpPhoneNumbers.setStatus("current")


class _TelProfileEnableAGC_Type(Integer32):
    """Custom type telProfileEnableAGC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", -1))
    )


_TelProfileEnableAGC_Type.__name__ = "Integer32"
_TelProfileEnableAGC_Object = MibTableColumn
telProfileEnableAGC = _TelProfileEnableAGC_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 34),
    _TelProfileEnableAGC_Type()
)
telProfileEnableAGC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileEnableAGC.setStatus("current")


class _TelProfileECNlpMode_Type(Integer32):
    """Custom type telProfileECNlpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveNLP", 0),
          ("disabledNLP", 1),
          ("notConfigured", -1),
          ("silenceOutputNLP", 2))
    )


_TelProfileECNlpMode_Type.__name__ = "Integer32"
_TelProfileECNlpMode_Object = MibTableColumn
telProfileECNlpMode = _TelProfileECNlpMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 15, 22, 1, 35),
    _TelProfileECNlpMode_Type()
)
telProfileECNlpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    telProfileECNlpMode.setStatus("current")
_VoiceMail_ObjectIdentity = ObjectIdentity
voiceMail = _VoiceMail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16)
)


class _VoiceMailLineTransferMode_Type(Integer32):
    """Custom type voiceMailLineTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 0),
          ("pbxblindtransfer", 1),
          ("pbxsemisupervised", 2),
          ("pbxsupervisedtransfer", 3))
    )


_VoiceMailLineTransferMode_Type.__name__ = "Integer32"
_VoiceMailLineTransferMode_Object = MibScalar
voiceMailLineTransferMode = _VoiceMailLineTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 1),
    _VoiceMailLineTransferMode_Type()
)
voiceMailLineTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceMailLineTransferMode.setStatus("current")


class _VoiceMailInterface_Type(Integer32):
    """Custom type voiceMailInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("isdnsetup", 4),
          ("none", 0),
          ("qsig", 3),
          ("smdi", 2))
    )


_VoiceMailInterface_Type.__name__ = "Integer32"
_VoiceMailInterface_Object = MibScalar
voiceMailInterface = _VoiceMailInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 2),
    _VoiceMailInterface_Type()
)
voiceMailInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceMailInterface.setStatus("current")
_VmDigitPattern_ObjectIdentity = ObjectIdentity
vmDigitPattern = _VmDigitPattern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20)
)


class _VmDigitPatternNoReason_Type(SnmpAdminString):
    """Custom type vmDigitPatternNoReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternNoReason_Type.__name__ = "SnmpAdminString"
_VmDigitPatternNoReason_Object = MibScalar
vmDigitPatternNoReason = _VmDigitPatternNoReason_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 1),
    _VmDigitPatternNoReason_Type()
)
vmDigitPatternNoReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternNoReason.setStatus("current")


class _VmDigitPatternOnBusy_Type(SnmpAdminString):
    """Custom type vmDigitPatternOnBusy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternOnBusy_Type.__name__ = "SnmpAdminString"
_VmDigitPatternOnBusy_Object = MibScalar
vmDigitPatternOnBusy = _VmDigitPatternOnBusy_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 2),
    _VmDigitPatternOnBusy_Type()
)
vmDigitPatternOnBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternOnBusy.setStatus("current")


class _VmDigitPatternOnNoAnswer_Type(SnmpAdminString):
    """Custom type vmDigitPatternOnNoAnswer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternOnNoAnswer_Type.__name__ = "SnmpAdminString"
_VmDigitPatternOnNoAnswer_Object = MibScalar
vmDigitPatternOnNoAnswer = _VmDigitPatternOnNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 3),
    _VmDigitPatternOnNoAnswer_Type()
)
vmDigitPatternOnNoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternOnNoAnswer.setStatus("current")


class _VmDigitPatternOnDND_Type(SnmpAdminString):
    """Custom type vmDigitPatternOnDND based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternOnDND_Type.__name__ = "SnmpAdminString"
_VmDigitPatternOnDND_Object = MibScalar
vmDigitPatternOnDND = _VmDigitPatternOnDND_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 4),
    _VmDigitPatternOnDND_Type()
)
vmDigitPatternOnDND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternOnDND.setStatus("current")


class _VmDigitPatternInternalCall_Type(SnmpAdminString):
    """Custom type vmDigitPatternInternalCall based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternInternalCall_Type.__name__ = "SnmpAdminString"
_VmDigitPatternInternalCall_Object = MibScalar
vmDigitPatternInternalCall = _VmDigitPatternInternalCall_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 5),
    _VmDigitPatternInternalCall_Type()
)
vmDigitPatternInternalCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternInternalCall.setStatus("current")


class _VmDigitPatternExternalCall_Type(SnmpAdminString):
    """Custom type vmDigitPatternExternalCall based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternExternalCall_Type.__name__ = "SnmpAdminString"
_VmDigitPatternExternalCall_Object = MibScalar
vmDigitPatternExternalCall = _VmDigitPatternExternalCall_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 6),
    _VmDigitPatternExternalCall_Type()
)
vmDigitPatternExternalCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternExternalCall.setStatus("current")


class _VmDigitPatternDisconnectCode_Type(SnmpAdminString):
    """Custom type vmDigitPatternDisconnectCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_VmDigitPatternDisconnectCode_Type.__name__ = "SnmpAdminString"
_VmDigitPatternDisconnectCode_Object = MibScalar
vmDigitPatternDisconnectCode = _VmDigitPatternDisconnectCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 7),
    _VmDigitPatternDisconnectCode_Type()
)
vmDigitPatternDisconnectCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternDisconnectCode.setStatus("current")


class _VmDigitPatternConnectCode_Type(SnmpAdminString):
    """Custom type vmDigitPatternConnectCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VmDigitPatternConnectCode_Type.__name__ = "SnmpAdminString"
_VmDigitPatternConnectCode_Object = MibScalar
vmDigitPatternConnectCode = _VmDigitPatternConnectCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 8),
    _VmDigitPatternConnectCode_Type()
)
vmDigitPatternConnectCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternConnectCode.setStatus("current")


class _VmDigitPatternVmDigitPatternOnBusyExternal_Type(SnmpAdminString):
    """Custom type vmDigitPatternVmDigitPatternOnBusyExternal based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternVmDigitPatternOnBusyExternal_Type.__name__ = "SnmpAdminString"
_VmDigitPatternVmDigitPatternOnBusyExternal_Object = MibScalar
vmDigitPatternVmDigitPatternOnBusyExternal = _VmDigitPatternVmDigitPatternOnBusyExternal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 9),
    _VmDigitPatternVmDigitPatternOnBusyExternal_Type()
)
vmDigitPatternVmDigitPatternOnBusyExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternVmDigitPatternOnBusyExternal.setStatus("current")


class _VmDigitPatternVmDigitPatternOnNoAnswerExternal_Type(SnmpAdminString):
    """Custom type vmDigitPatternVmDigitPatternOnNoAnswerExternal based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternVmDigitPatternOnNoAnswerExternal_Type.__name__ = "SnmpAdminString"
_VmDigitPatternVmDigitPatternOnNoAnswerExternal_Object = MibScalar
vmDigitPatternVmDigitPatternOnNoAnswerExternal = _VmDigitPatternVmDigitPatternOnNoAnswerExternal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 10),
    _VmDigitPatternVmDigitPatternOnNoAnswerExternal_Type()
)
vmDigitPatternVmDigitPatternOnNoAnswerExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternVmDigitPatternOnNoAnswerExternal.setStatus("current")


class _VmDigitPatternVmDigitPatternOnDNDExternal_Type(SnmpAdminString):
    """Custom type vmDigitPatternVmDigitPatternOnDNDExternal based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternVmDigitPatternOnDNDExternal_Type.__name__ = "SnmpAdminString"
_VmDigitPatternVmDigitPatternOnDNDExternal_Object = MibScalar
vmDigitPatternVmDigitPatternOnDNDExternal = _VmDigitPatternVmDigitPatternOnDNDExternal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 11),
    _VmDigitPatternVmDigitPatternOnDNDExternal_Type()
)
vmDigitPatternVmDigitPatternOnDNDExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternVmDigitPatternOnDNDExternal.setStatus("current")


class _VmDigitPatternVmDigitPatternNoReasonExternal_Type(SnmpAdminString):
    """Custom type vmDigitPatternVmDigitPatternNoReasonExternal based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternVmDigitPatternNoReasonExternal_Type.__name__ = "SnmpAdminString"
_VmDigitPatternVmDigitPatternNoReasonExternal_Object = MibScalar
vmDigitPatternVmDigitPatternNoReasonExternal = _VmDigitPatternVmDigitPatternNoReasonExternal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 12),
    _VmDigitPatternVmDigitPatternNoReasonExternal_Type()
)
vmDigitPatternVmDigitPatternNoReasonExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternVmDigitPatternNoReasonExternal.setStatus("current")


class _VmDigitPatternDigitToIgnore_Type(SnmpAdminString):
    """Custom type vmDigitPatternDigitToIgnore based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmDigitPatternDigitToIgnore_Type.__name__ = "SnmpAdminString"
_VmDigitPatternDigitToIgnore_Object = MibScalar
vmDigitPatternDigitToIgnore = _VmDigitPatternDigitToIgnore_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 20, 13),
    _VmDigitPatternDigitToIgnore_Type()
)
vmDigitPatternDigitToIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmDigitPatternDigitToIgnore.setStatus("current")
_VmMWI_ObjectIdentity = ObjectIdentity
vmMWI = _VmMWI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 21)
)


class _VmMWIOnCode_Type(SnmpAdminString):
    """Custom type vmMWIOnCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_VmMWIOnCode_Type.__name__ = "SnmpAdminString"
_VmMWIOnCode_Object = MibScalar
vmMWIOnCode = _VmMWIOnCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 21, 1),
    _VmMWIOnCode_Type()
)
vmMWIOnCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmMWIOnCode.setStatus("current")


class _VmMWIOffCode_Type(SnmpAdminString):
    """Custom type vmMWIOffCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_VmMWIOffCode_Type.__name__ = "SnmpAdminString"
_VmMWIOffCode_Object = MibScalar
vmMWIOffCode = _VmMWIOffCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 21, 2),
    _VmMWIOffCode_Type()
)
vmMWIOffCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmMWIOffCode.setStatus("current")


class _VmMWISuffixCode_Type(SnmpAdminString):
    """Custom type vmMWISuffixCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_VmMWISuffixCode_Type.__name__ = "SnmpAdminString"
_VmMWISuffixCode_Object = MibScalar
vmMWISuffixCode = _VmMWISuffixCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 21, 3),
    _VmMWISuffixCode_Type()
)
vmMWISuffixCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmMWISuffixCode.setStatus("current")


class _VmMWISourceNumber_Type(SnmpAdminString):
    """Custom type vmMWISourceNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_VmMWISourceNumber_Type.__name__ = "SnmpAdminString"
_VmMWISourceNumber_Object = MibScalar
vmMWISourceNumber = _VmMWISourceNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 21, 4),
    _VmMWISourceNumber_Type()
)
vmMWISourceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmMWISourceNumber.setStatus("current")
_VmSMDI_ObjectIdentity = ObjectIdentity
vmSMDI = _VmSMDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 22)
)


class _VmSMDIEnable_Type(Integer32):
    """Custom type vmSMDIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_VmSMDIEnable_Type.__name__ = "Integer32"
_VmSMDIEnable_Object = MibScalar
vmSMDIEnable = _VmSMDIEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 22, 1),
    _VmSMDIEnable_Type()
)
vmSMDIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmSMDIEnable.setStatus("current")


class _VmSMDITimeOut_Type(Unsigned32):
    """Custom type vmSMDITimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120000),
    )


_VmSMDITimeOut_Type.__name__ = "Unsigned32"
_VmSMDITimeOut_Object = MibScalar
vmSMDITimeOut = _VmSMDITimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 16, 22, 2),
    _VmSMDITimeOut_Type()
)
vmSMDITimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmSMDITimeOut.setStatus("current")
_DigitalGWext_ObjectIdentity = ObjectIdentity
digitalGWext = _DigitalGWext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17)
)


class _DigitalGWextEnableQSIGTunneling_Type(Integer32):
    """Custom type digitalGWextEnableQSIGTunneling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWextEnableQSIGTunneling_Type.__name__ = "Integer32"
_DigitalGWextEnableQSIGTunneling_Object = MibScalar
digitalGWextEnableQSIGTunneling = _DigitalGWextEnableQSIGTunneling_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 1),
    _DigitalGWextEnableQSIGTunneling_Type()
)
digitalGWextEnableQSIGTunneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWextEnableQSIGTunneling.setStatus("current")


class _DigitalGWextRemoveCLIWhenRestricted_Type(Integer32):
    """Custom type digitalGWextRemoveCLIWhenRestricted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWextRemoveCLIWhenRestricted_Type.__name__ = "Integer32"
_DigitalGWextRemoveCLIWhenRestricted_Object = MibScalar
digitalGWextRemoveCLIWhenRestricted = _DigitalGWextRemoveCLIWhenRestricted_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 2),
    _DigitalGWextRemoveCLIWhenRestricted_Type()
)
digitalGWextRemoveCLIWhenRestricted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWextRemoveCLIWhenRestricted.setStatus("current")


class _DigitalGWextDefaultCauseMapISDN2IP_Type(Unsigned32):
    """Custom type digitalGWextDefaultCauseMapISDN2IP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DigitalGWextDefaultCauseMapISDN2IP_Type.__name__ = "Unsigned32"
_DigitalGWextDefaultCauseMapISDN2IP_Object = MibScalar
digitalGWextDefaultCauseMapISDN2IP = _DigitalGWextDefaultCauseMapISDN2IP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 3),
    _DigitalGWextDefaultCauseMapISDN2IP_Type()
)
digitalGWextDefaultCauseMapISDN2IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWextDefaultCauseMapISDN2IP.setStatus("current")


class _DigitalGWextISDNSubaddressFormat_Type(Integer32):
    """Custom type digitalGWextISDNSubaddressFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("bcd", 1),
          ("userSpecified", 2))
    )


_DigitalGWextISDNSubaddressFormat_Type.__name__ = "Integer32"
_DigitalGWextISDNSubaddressFormat_Object = MibScalar
digitalGWextISDNSubaddressFormat = _DigitalGWextISDNSubaddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 4),
    _DigitalGWextISDNSubaddressFormat_Type()
)
digitalGWextISDNSubaddressFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWextISDNSubaddressFormat.setStatus("current")


class _DigitalGWextEnableAoC_Type(Integer32):
    """Custom type digitalGWextEnableAoC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWextEnableAoC_Type.__name__ = "Integer32"
_DigitalGWextEnableAoC_Object = MibScalar
digitalGWextEnableAoC = _DigitalGWextEnableAoC_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 5),
    _DigitalGWextEnableAoC_Type()
)
digitalGWextEnableAoC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWextEnableAoC.setStatus("current")


class _DigitalGWextRemoveCallingName_Type(Integer32):
    """Custom type digitalGWextRemoveCallingName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DigitalGWextRemoveCallingName_Type.__name__ = "Integer32"
_DigitalGWextRemoveCallingName_Object = MibScalar
digitalGWextRemoveCallingName = _DigitalGWextRemoveCallingName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 6),
    _DigitalGWextRemoveCallingName_Type()
)
digitalGWextRemoveCallingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWextRemoveCallingName.setStatus("current")


class _DigitalGWextCopyDest2RedirectNumber_Type(Integer32):
    """Custom type digitalGWextCopyDest2RedirectNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("afterManipulation", 1),
          ("beforeManipulation", 2),
          ("disable", 0))
    )


_DigitalGWextCopyDest2RedirectNumber_Type.__name__ = "Integer32"
_DigitalGWextCopyDest2RedirectNumber_Object = MibScalar
digitalGWextCopyDest2RedirectNumber = _DigitalGWextCopyDest2RedirectNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 7),
    _DigitalGWextCopyDest2RedirectNumber_Type()
)
digitalGWextCopyDest2RedirectNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWextCopyDest2RedirectNumber.setStatus("current")


class _DigitalGWextTDMOverIPMinCallsForTrunkActivation_Type(Unsigned32):
    """Custom type digitalGWextTDMOverIPMinCallsForTrunkActivation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_DigitalGWextTDMOverIPMinCallsForTrunkActivation_Type.__name__ = "Unsigned32"
_DigitalGWextTDMOverIPMinCallsForTrunkActivation_Object = MibScalar
digitalGWextTDMOverIPMinCallsForTrunkActivation = _DigitalGWextTDMOverIPMinCallsForTrunkActivation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 8),
    _DigitalGWextTDMOverIPMinCallsForTrunkActivation_Type()
)
digitalGWextTDMOverIPMinCallsForTrunkActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalGWextTDMOverIPMinCallsForTrunkActivation.setStatus("current")
_RtpOnlyModeForTrunkTable_Object = MibTable
rtpOnlyModeForTrunkTable = _RtpOnlyModeForTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 21)
)
if mibBuilder.loadTexts:
    rtpOnlyModeForTrunkTable.setStatus("current")
_RtpOnlyModeForTrunkEntry_Object = MibTableRow
rtpOnlyModeForTrunkEntry = _RtpOnlyModeForTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 21, 1)
)
rtpOnlyModeForTrunkEntry.setIndexNames(
    (0, "AcGateway", "rtpOnlyModeForTrunkIndex"),
)
if mibBuilder.loadTexts:
    rtpOnlyModeForTrunkEntry.setStatus("current")


class _RtpOnlyModeForTrunkIndex_Type(Unsigned32):
    """Custom type rtpOnlyModeForTrunkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 84),
    )


_RtpOnlyModeForTrunkIndex_Type.__name__ = "Unsigned32"
_RtpOnlyModeForTrunkIndex_Object = MibTableColumn
rtpOnlyModeForTrunkIndex = _RtpOnlyModeForTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 21, 1, 1),
    _RtpOnlyModeForTrunkIndex_Type()
)
rtpOnlyModeForTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtpOnlyModeForTrunkIndex.setStatus("current")


class _RtpOnlyModeForTrunkRtpOnlyModeForTrunk_Type(Integer32):
    """Custom type rtpOnlyModeForTrunkRtpOnlyModeForTrunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("notConfigured", -1),
          ("receiveOnly", 3),
          ("transmitOnly", 2),
          ("transmitReceive", 1))
    )


_RtpOnlyModeForTrunkRtpOnlyModeForTrunk_Type.__name__ = "Integer32"
_RtpOnlyModeForTrunkRtpOnlyModeForTrunk_Object = MibTableColumn
rtpOnlyModeForTrunkRtpOnlyModeForTrunk = _RtpOnlyModeForTrunkRtpOnlyModeForTrunk_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 21, 1, 2),
    _RtpOnlyModeForTrunkRtpOnlyModeForTrunk_Type()
)
rtpOnlyModeForTrunkRtpOnlyModeForTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtpOnlyModeForTrunkRtpOnlyModeForTrunk.setStatus("current")
_AcBChannelNegotiationForTrunkTable_Object = MibTable
acBChannelNegotiationForTrunkTable = _AcBChannelNegotiationForTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 22)
)
if mibBuilder.loadTexts:
    acBChannelNegotiationForTrunkTable.setStatus("current")
_AcBChannelNegotiationForTrunkEntry_Object = MibTableRow
acBChannelNegotiationForTrunkEntry = _AcBChannelNegotiationForTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 22, 1)
)
acBChannelNegotiationForTrunkEntry.setIndexNames(
    (0, "AcGateway", "acBChannelNegotiationForTrunkIndex"),
)
if mibBuilder.loadTexts:
    acBChannelNegotiationForTrunkEntry.setStatus("current")


class _AcBChannelNegotiationForTrunkIndex_Type(Unsigned32):
    """Custom type acBChannelNegotiationForTrunkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcBChannelNegotiationForTrunkIndex_Type.__name__ = "Unsigned32"
_AcBChannelNegotiationForTrunkIndex_Object = MibTableColumn
acBChannelNegotiationForTrunkIndex = _AcBChannelNegotiationForTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 22, 1, 1),
    _AcBChannelNegotiationForTrunkIndex_Type()
)
acBChannelNegotiationForTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acBChannelNegotiationForTrunkIndex.setStatus("current")


class _AcBChannelNegotiationForTrunkMode_Type(Integer32):
    """Custom type acBChannelNegotiationForTrunkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("exclusive", 1),
          ("notConfigured", -1),
          ("preferred", 0))
    )


_AcBChannelNegotiationForTrunkMode_Type.__name__ = "Integer32"
_AcBChannelNegotiationForTrunkMode_Object = MibTableColumn
acBChannelNegotiationForTrunkMode = _AcBChannelNegotiationForTrunkMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 22, 1, 2),
    _AcBChannelNegotiationForTrunkMode_Type()
)
acBChannelNegotiationForTrunkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acBChannelNegotiationForTrunkMode.setStatus("current")
_AcDigitalOOSBehaviorForTrunkTable_Object = MibTable
acDigitalOOSBehaviorForTrunkTable = _AcDigitalOOSBehaviorForTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 23)
)
if mibBuilder.loadTexts:
    acDigitalOOSBehaviorForTrunkTable.setStatus("current")
_AcDigitalOOSBehaviorForTrunkEntry_Object = MibTableRow
acDigitalOOSBehaviorForTrunkEntry = _AcDigitalOOSBehaviorForTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 23, 1)
)
acDigitalOOSBehaviorForTrunkEntry.setIndexNames(
    (0, "AcGateway", "acDigitalOOSBehaviorForTrunkIndex"),
)
if mibBuilder.loadTexts:
    acDigitalOOSBehaviorForTrunkEntry.setStatus("current")


class _AcDigitalOOSBehaviorForTrunkIndex_Type(Unsigned32):
    """Custom type acDigitalOOSBehaviorForTrunkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcDigitalOOSBehaviorForTrunkIndex_Type.__name__ = "Unsigned32"
_AcDigitalOOSBehaviorForTrunkIndex_Object = MibTableColumn
acDigitalOOSBehaviorForTrunkIndex = _AcDigitalOOSBehaviorForTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 23, 1, 1),
    _AcDigitalOOSBehaviorForTrunkIndex_Type()
)
acDigitalOOSBehaviorForTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acDigitalOOSBehaviorForTrunkIndex.setStatus("current")


class _AcDigitalOOSBehaviorForTrunkValue_Type(Integer32):
    """Custom type acDigitalOOSBehaviorForTrunkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("block", 4),
          ("dChannel", 2),
          ("default", 0),
          ("notConfigured", -1),
          ("service", 1))
    )


_AcDigitalOOSBehaviorForTrunkValue_Type.__name__ = "Integer32"
_AcDigitalOOSBehaviorForTrunkValue_Object = MibTableColumn
acDigitalOOSBehaviorForTrunkValue = _AcDigitalOOSBehaviorForTrunkValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 23, 1, 2),
    _AcDigitalOOSBehaviorForTrunkValue_Type()
)
acDigitalOOSBehaviorForTrunkValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDigitalOOSBehaviorForTrunkValue.setStatus("current")
_AcRemoveCallingNameForTrunkTable_Object = MibTable
acRemoveCallingNameForTrunkTable = _AcRemoveCallingNameForTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 24)
)
if mibBuilder.loadTexts:
    acRemoveCallingNameForTrunkTable.setStatus("current")
_AcRemoveCallingNameForTrunkEntry_Object = MibTableRow
acRemoveCallingNameForTrunkEntry = _AcRemoveCallingNameForTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 24, 1)
)
acRemoveCallingNameForTrunkEntry.setIndexNames(
    (0, "AcGateway", "acRemoveCallingNameForTrunkIndex"),
)
if mibBuilder.loadTexts:
    acRemoveCallingNameForTrunkEntry.setStatus("current")


class _AcRemoveCallingNameForTrunkIndex_Type(Unsigned32):
    """Custom type acRemoveCallingNameForTrunkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcRemoveCallingNameForTrunkIndex_Type.__name__ = "Unsigned32"
_AcRemoveCallingNameForTrunkIndex_Object = MibTableColumn
acRemoveCallingNameForTrunkIndex = _AcRemoveCallingNameForTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 24, 1, 1),
    _AcRemoveCallingNameForTrunkIndex_Type()
)
acRemoveCallingNameForTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acRemoveCallingNameForTrunkIndex.setStatus("current")


class _AcRemoveCallingNameForTrunkMode_Type(Integer32):
    """Custom type acRemoveCallingNameForTrunkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notConfigured", -1))
    )


_AcRemoveCallingNameForTrunkMode_Type.__name__ = "Integer32"
_AcRemoveCallingNameForTrunkMode_Object = MibTableColumn
acRemoveCallingNameForTrunkMode = _AcRemoveCallingNameForTrunkMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 17, 24, 1, 2),
    _AcRemoveCallingNameForTrunkMode_Type()
)
acRemoveCallingNameForTrunkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acRemoveCallingNameForTrunkMode.setStatus("current")
_GwSecurity_ObjectIdentity = ObjectIdentity
gwSecurity = _GwSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 18)
)


class _GwSecurityMediaSecurityBehavior_Type(Integer32):
    """Custom type gwSecurityMediaSecurityBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mandatory", 1),
          ("preferable", 0))
    )


_GwSecurityMediaSecurityBehavior_Type.__name__ = "Integer32"
_GwSecurityMediaSecurityBehavior_Object = MibScalar
gwSecurityMediaSecurityBehavior = _GwSecurityMediaSecurityBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 18, 1),
    _GwSecurityMediaSecurityBehavior_Type()
)
gwSecurityMediaSecurityBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSecurityMediaSecurityBehavior.setStatus("current")


class _GwSecuritySIPSRequireClientCertificate_Type(Integer32):
    """Custom type gwSecuritySIPSRequireClientCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_GwSecuritySIPSRequireClientCertificate_Type.__name__ = "Integer32"
_GwSecuritySIPSRequireClientCertificate_Object = MibScalar
gwSecuritySIPSRequireClientCertificate = _GwSecuritySIPSRequireClientCertificate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 18, 2),
    _GwSecuritySIPSRequireClientCertificate_Type()
)
gwSecuritySIPSRequireClientCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSecuritySIPSRequireClientCertificate.setStatus("current")


class _GwSecurityTLSReHandshakeInterval_Type(Unsigned32):
    """Custom type gwSecurityTLSReHandshakeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_GwSecurityTLSReHandshakeInterval_Type.__name__ = "Unsigned32"
_GwSecurityTLSReHandshakeInterval_Object = MibScalar
gwSecurityTLSReHandshakeInterval = _GwSecurityTLSReHandshakeInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 18, 3),
    _GwSecurityTLSReHandshakeInterval_Type()
)
gwSecurityTLSReHandshakeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSecurityTLSReHandshakeInterval.setStatus("current")


class _GwSecurityPeerHostNameVerificationMode_Type(Integer32):
    """Custom type gwSecurityPeerHostNameVerificationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("serverAndClient", 2),
          ("serverOnly", 1))
    )


_GwSecurityPeerHostNameVerificationMode_Type.__name__ = "Integer32"
_GwSecurityPeerHostNameVerificationMode_Object = MibScalar
gwSecurityPeerHostNameVerificationMode = _GwSecurityPeerHostNameVerificationMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 18, 4),
    _GwSecurityPeerHostNameVerificationMode_Type()
)
gwSecurityPeerHostNameVerificationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSecurityPeerHostNameVerificationMode.setStatus("current")


class _GwSecurityVerifyServerCertificate_Type(Integer32):
    """Custom type gwSecurityVerifyServerCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_GwSecurityVerifyServerCertificate_Type.__name__ = "Integer32"
_GwSecurityVerifyServerCertificate_Object = MibScalar
gwSecurityVerifyServerCertificate = _GwSecurityVerifyServerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 18, 5),
    _GwSecurityVerifyServerCertificate_Type()
)
gwSecurityVerifyServerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSecurityVerifyServerCertificate.setStatus("current")


class _GwSecurityTLSRemoteSubjectName_Type(SnmpAdminString):
    """Custom type gwSecurityTLSRemoteSubjectName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_GwSecurityTLSRemoteSubjectName_Type.__name__ = "SnmpAdminString"
_GwSecurityTLSRemoteSubjectName_Object = MibScalar
gwSecurityTLSRemoteSubjectName = _GwSecurityTLSRemoteSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 18, 6),
    _GwSecurityTLSRemoteSubjectName_Type()
)
gwSecurityTLSRemoteSubjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSecurityTLSRemoteSubjectName.setStatus("current")


class _GwSecuritySRTPofferedSuites_Type(Integer32):
    """Custom type gwSecuritySRTPofferedSuites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aesCm128HmacShaOne32", 2),
          ("aesCm128HmacShaOne80", 1),
          ("all", 0))
    )


_GwSecuritySRTPofferedSuites_Type.__name__ = "Integer32"
_GwSecuritySRTPofferedSuites_Object = MibScalar
gwSecuritySRTPofferedSuites = _GwSecuritySRTPofferedSuites_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 18, 7),
    _GwSecuritySRTPofferedSuites_Type()
)
gwSecuritySRTPofferedSuites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSecuritySRTPofferedSuites.setStatus("current")
_AcGWRtcpXr_ObjectIdentity = ObjectIdentity
acGWRtcpXr = _AcGWRtcpXr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 19)
)


class _AcGWRtcpXrEscIP_Type(SnmpAdminString):
    """Custom type acGWRtcpXrEscIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_AcGWRtcpXrEscIP_Type.__name__ = "SnmpAdminString"
_AcGWRtcpXrEscIP_Object = MibScalar
acGWRtcpXrEscIP = _AcGWRtcpXrEscIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 19, 1),
    _AcGWRtcpXrEscIP_Type()
)
acGWRtcpXrEscIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGWRtcpXrEscIP.setStatus("current")


class _AcGWRtcpXrReportMode_Type(Integer32):
    """Custom type acGWRtcpXrReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("endCall", 1),
          ("endCallPeriodic", 2))
    )


_AcGWRtcpXrReportMode_Type.__name__ = "Integer32"
_AcGWRtcpXrReportMode_Object = MibScalar
acGWRtcpXrReportMode = _AcGWRtcpXrReportMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 19, 2),
    _AcGWRtcpXrReportMode_Type()
)
acGWRtcpXrReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGWRtcpXrReportMode.setStatus("current")


class _AcGWRtcpXrEscTransportType_Type(Integer32):
    """Custom type acGWRtcpXrEscTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", -1),
          ("tCP", 1),
          ("tLS", 2),
          ("uDP", 0))
    )


_AcGWRtcpXrEscTransportType_Type.__name__ = "Integer32"
_AcGWRtcpXrEscTransportType_Object = MibScalar
acGWRtcpXrEscTransportType = _AcGWRtcpXrEscTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 19, 3),
    _AcGWRtcpXrEscTransportType_Type()
)
acGWRtcpXrEscTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acGWRtcpXrEscTransportType.setStatus("current")
_AcTimers_ObjectIdentity = ObjectIdentity
acTimers = _AcTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 20)
)


class _AcTimersIPAlertTimeout_Type(Unsigned32):
    """Custom type acTimersIPAlertTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AcTimersIPAlertTimeout_Type.__name__ = "Unsigned32"
_AcTimersIPAlertTimeout_Object = MibScalar
acTimersIPAlertTimeout = _AcTimersIPAlertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 20, 1),
    _AcTimersIPAlertTimeout_Type()
)
acTimersIPAlertTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTimersIPAlertTimeout.setStatus("current")


class _AcTimersPSTNAlertTimeout_Type(Unsigned32):
    """Custom type acTimersPSTNAlertTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_AcTimersPSTNAlertTimeout_Type.__name__ = "Unsigned32"
_AcTimersPSTNAlertTimeout_Object = MibScalar
acTimersPSTNAlertTimeout = _AcTimersPSTNAlertTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 20, 2),
    _AcTimersPSTNAlertTimeout_Type()
)
acTimersPSTNAlertTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTimersPSTNAlertTimeout.setStatus("current")
_AcEmergency_ObjectIdentity = ObjectIdentity
acEmergency = _AcEmergency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 21)
)


class _AcEmergencyRegretTimeout_Type(Unsigned32):
    """Custom type acEmergencyRegretTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AcEmergencyRegretTimeout_Type.__name__ = "Unsigned32"
_AcEmergencyRegretTimeout_Object = MibScalar
acEmergencyRegretTimeout = _AcEmergencyRegretTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 21, 1),
    _AcEmergencyRegretTimeout_Type()
)
acEmergencyRegretTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEmergencyRegretTimeout.setStatus("current")
_AcEmergencyNumbersTable_Object = MibTable
acEmergencyNumbersTable = _AcEmergencyNumbersTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 21, 21)
)
if mibBuilder.loadTexts:
    acEmergencyNumbersTable.setStatus("current")
_AcEmergencyNumbersEntry_Object = MibTableRow
acEmergencyNumbersEntry = _AcEmergencyNumbersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 21, 21, 1)
)
acEmergencyNumbersEntry.setIndexNames(
    (0, "AcGateway", "acEmergencyNumbersIndex"),
)
if mibBuilder.loadTexts:
    acEmergencyNumbersEntry.setStatus("current")


class _AcEmergencyNumbersIndex_Type(Unsigned32):
    """Custom type acEmergencyNumbersIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AcEmergencyNumbersIndex_Type.__name__ = "Unsigned32"
_AcEmergencyNumbersIndex_Object = MibTableColumn
acEmergencyNumbersIndex = _AcEmergencyNumbersIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 21, 21, 1, 1),
    _AcEmergencyNumbersIndex_Type()
)
acEmergencyNumbersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acEmergencyNumbersIndex.setStatus("current")


class _AcEmergencyNumbersNumbers_Type(SnmpAdminString):
    """Custom type acEmergencyNumbersNumbers based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AcEmergencyNumbersNumbers_Type.__name__ = "SnmpAdminString"
_AcEmergencyNumbersNumbers_Object = MibTableColumn
acEmergencyNumbersNumbers = _AcEmergencyNumbersNumbers_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 21, 21, 1, 2),
    _AcEmergencyNumbersNumbers_Type()
)
acEmergencyNumbersNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEmergencyNumbersNumbers.setStatus("current")
_Accounts_ObjectIdentity = ObjectIdentity
accounts = _Accounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22)
)
_AccountTable_Object = MibTable
accountTable = _AccountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21)
)
if mibBuilder.loadTexts:
    accountTable.setStatus("current")
_AccountEntry_Object = MibTableRow
accountEntry = _AccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1)
)
accountEntry.setIndexNames(
    (0, "AcGateway", "accountIndex"),
)
if mibBuilder.loadTexts:
    accountEntry.setStatus("current")


class _AccountIndex_Type(Unsigned32):
    """Custom type accountIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AccountIndex_Type.__name__ = "Unsigned32"
_AccountIndex_Object = MibTableColumn
accountIndex = _AccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 1),
    _AccountIndex_Type()
)
accountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountIndex.setStatus("current")
_AccountRowStatus_Type = RowStatus
_AccountRowStatus_Object = MibTableColumn
accountRowStatus = _AccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 2),
    _AccountRowStatus_Type()
)
accountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accountRowStatus.setStatus("current")


class _AccountAction_Type(Integer32):
    """Custom type accountAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_AccountAction_Type.__name__ = "Integer32"
_AccountAction_Object = MibTableColumn
accountAction = _AccountAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 3),
    _AccountAction_Type()
)
accountAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountAction.setStatus("current")


class _AccountActionResult_Type(Integer32):
    """Custom type accountActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_AccountActionResult_Type.__name__ = "Integer32"
_AccountActionResult_Object = MibTableColumn
accountActionResult = _AccountActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 4),
    _AccountActionResult_Type()
)
accountActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountActionResult.setStatus("current")


class _AccountServedTrunkGroup_Type(Integer32):
    """Custom type accountServedTrunkGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AccountServedTrunkGroup_Type.__name__ = "Integer32"
_AccountServedTrunkGroup_Object = MibTableColumn
accountServedTrunkGroup = _AccountServedTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 5),
    _AccountServedTrunkGroup_Type()
)
accountServedTrunkGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accountServedTrunkGroup.setStatus("current")


class _AccountServedIPGroup_Type(Integer32):
    """Custom type accountServedIPGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_AccountServedIPGroup_Type.__name__ = "Integer32"
_AccountServedIPGroup_Object = MibTableColumn
accountServedIPGroup = _AccountServedIPGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 6),
    _AccountServedIPGroup_Type()
)
accountServedIPGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accountServedIPGroup.setStatus("current")


class _AccountServingIPGroup_Type(Integer32):
    """Custom type accountServingIPGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_AccountServingIPGroup_Type.__name__ = "Integer32"
_AccountServingIPGroup_Object = MibTableColumn
accountServingIPGroup = _AccountServingIPGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 7),
    _AccountServingIPGroup_Type()
)
accountServingIPGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accountServingIPGroup.setStatus("current")


class _AccountUsername_Type(SnmpAdminString):
    """Custom type accountUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AccountUsername_Type.__name__ = "SnmpAdminString"
_AccountUsername_Object = MibTableColumn
accountUsername = _AccountUsername_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 8),
    _AccountUsername_Type()
)
accountUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accountUsername.setStatus("current")


class _AccountPassword_Type(SnmpAdminString):
    """Custom type accountPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AccountPassword_Type.__name__ = "SnmpAdminString"
_AccountPassword_Object = MibTableColumn
accountPassword = _AccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 9),
    _AccountPassword_Type()
)
accountPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accountPassword.setStatus("current")


class _AccountHostName_Type(SnmpAdminString):
    """Custom type accountHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_AccountHostName_Type.__name__ = "SnmpAdminString"
_AccountHostName_Object = MibTableColumn
accountHostName = _AccountHostName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 10),
    _AccountHostName_Type()
)
accountHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accountHostName.setStatus("current")


class _AccountRegister_Type(Integer32):
    """Custom type accountRegister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AccountRegister_Type.__name__ = "Integer32"
_AccountRegister_Object = MibTableColumn
accountRegister = _AccountRegister_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 11),
    _AccountRegister_Type()
)
accountRegister.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accountRegister.setStatus("current")


class _AccountContactUser_Type(SnmpAdminString):
    """Custom type accountContactUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AccountContactUser_Type.__name__ = "SnmpAdminString"
_AccountContactUser_Object = MibTableColumn
accountContactUser = _AccountContactUser_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 22, 21, 1, 12),
    _AccountContactUser_Type()
)
accountContactUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accountContactUser.setStatus("current")
_IpGroups_ObjectIdentity = ObjectIdentity
ipGroups = _IpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23)
)
_IpGroupTable_Object = MibTable
ipGroupTable = _IpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21)
)
if mibBuilder.loadTexts:
    ipGroupTable.setStatus("current")
_IpGroupEntry_Object = MibTableRow
ipGroupEntry = _IpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1)
)
ipGroupEntry.setIndexNames(
    (0, "AcGateway", "ipGroupIndex"),
)
if mibBuilder.loadTexts:
    ipGroupEntry.setStatus("current")


class _IpGroupIndex_Type(Unsigned32):
    """Custom type ipGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_IpGroupIndex_Type.__name__ = "Unsigned32"
_IpGroupIndex_Object = MibTableColumn
ipGroupIndex = _IpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 1),
    _IpGroupIndex_Type()
)
ipGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGroupIndex.setStatus("current")
_IpGroupRowStatus_Type = RowStatus
_IpGroupRowStatus_Object = MibTableColumn
ipGroupRowStatus = _IpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 2),
    _IpGroupRowStatus_Type()
)
ipGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupRowStatus.setStatus("current")


class _IpGroupAction_Type(Integer32):
    """Custom type ipGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_IpGroupAction_Type.__name__ = "Integer32"
_IpGroupAction_Object = MibTableColumn
ipGroupAction = _IpGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 3),
    _IpGroupAction_Type()
)
ipGroupAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGroupAction.setStatus("current")


class _IpGroupActionResult_Type(Integer32):
    """Custom type ipGroupActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_IpGroupActionResult_Type.__name__ = "Integer32"
_IpGroupActionResult_Object = MibTableColumn
ipGroupActionResult = _IpGroupActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 4),
    _IpGroupActionResult_Type()
)
ipGroupActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipGroupActionResult.setStatus("current")


class _IpGroupType_Type(Integer32):
    """Custom type ipGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("server", 0),
          ("user", 1))
    )


_IpGroupType_Type.__name__ = "Integer32"
_IpGroupType_Object = MibTableColumn
ipGroupType = _IpGroupType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 5),
    _IpGroupType_Type()
)
ipGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupType.setStatus("current")


class _IpGroupDescription_Type(SnmpAdminString):
    """Custom type ipGroupDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_IpGroupDescription_Type.__name__ = "SnmpAdminString"
_IpGroupDescription_Object = MibTableColumn
ipGroupDescription = _IpGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 6),
    _IpGroupDescription_Type()
)
ipGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupDescription.setStatus("current")


class _IpGroupProxySetId_Type(Integer32):
    """Custom type ipGroupProxySetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_IpGroupProxySetId_Type.__name__ = "Integer32"
_IpGroupProxySetId_Object = MibTableColumn
ipGroupProxySetId = _IpGroupProxySetId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 7),
    _IpGroupProxySetId_Type()
)
ipGroupProxySetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupProxySetId.setStatus("current")


class _IpGroupSIPGroupName_Type(SnmpAdminString):
    """Custom type ipGroupSIPGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_IpGroupSIPGroupName_Type.__name__ = "SnmpAdminString"
_IpGroupSIPGroupName_Object = MibTableColumn
ipGroupSIPGroupName = _IpGroupSIPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 8),
    _IpGroupSIPGroupName_Type()
)
ipGroupSIPGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupSIPGroupName.setStatus("current")


class _IpGroupContactUser_Type(SnmpAdminString):
    """Custom type ipGroupContactUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_IpGroupContactUser_Type.__name__ = "SnmpAdminString"
_IpGroupContactUser_Object = MibTableColumn
ipGroupContactUser = _IpGroupContactUser_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 9),
    _IpGroupContactUser_Type()
)
ipGroupContactUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupContactUser.setStatus("current")


class _IpGroupEnableSurvivability_Type(Integer32):
    """Custom type ipGroupEnableSurvivability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysEnable", 2),
          ("disable", 0),
          ("enableIfNecessary", 1))
    )


_IpGroupEnableSurvivability_Type.__name__ = "Integer32"
_IpGroupEnableSurvivability_Object = MibTableColumn
ipGroupEnableSurvivability = _IpGroupEnableSurvivability_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 10),
    _IpGroupEnableSurvivability_Type()
)
ipGroupEnableSurvivability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupEnableSurvivability.setStatus("current")


class _IpGroupServingIPGroup_Type(Integer32):
    """Custom type ipGroupServingIPGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_IpGroupServingIPGroup_Type.__name__ = "Integer32"
_IpGroupServingIPGroup_Object = MibTableColumn
ipGroupServingIPGroup = _IpGroupServingIPGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 11),
    _IpGroupServingIPGroup_Type()
)
ipGroupServingIPGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupServingIPGroup.setStatus("current")


class _IpGroupSipReRoutingMode_Type(Integer32):
    """Custom type ipGroupSipReRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", -1),
          ("proxy", 1),
          ("routingTable", 2),
          ("standard", 0))
    )


_IpGroupSipReRoutingMode_Type.__name__ = "Integer32"
_IpGroupSipReRoutingMode_Object = MibTableColumn
ipGroupSipReRoutingMode = _IpGroupSipReRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 12),
    _IpGroupSipReRoutingMode_Type()
)
ipGroupSipReRoutingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupSipReRoutingMode.setStatus("current")


class _IpGroupAlwaysUseRouteTable_Type(Integer32):
    """Custom type ipGroupAlwaysUseRouteTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_IpGroupAlwaysUseRouteTable_Type.__name__ = "Integer32"
_IpGroupAlwaysUseRouteTable_Object = MibTableColumn
ipGroupAlwaysUseRouteTable = _IpGroupAlwaysUseRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 13),
    _IpGroupAlwaysUseRouteTable_Type()
)
ipGroupAlwaysUseRouteTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupAlwaysUseRouteTable.setStatus("current")


class _IpGroupRoutingMode_Type(Integer32):
    """Custom type ipGroupRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", -1),
          ("routeToRequestURI", 2),
          ("sendToServingIPGroup", 1),
          ("useRoutingTable", 0))
    )


_IpGroupRoutingMode_Type.__name__ = "Integer32"
_IpGroupRoutingMode_Object = MibTableColumn
ipGroupRoutingMode = _IpGroupRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 14),
    _IpGroupRoutingMode_Type()
)
ipGroupRoutingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupRoutingMode.setStatus("current")


class _IpGroupProfileId_Type(Unsigned32):
    """Custom type ipGroupProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_IpGroupProfileId_Type.__name__ = "Unsigned32"
_IpGroupProfileId_Object = MibTableColumn
ipGroupProfileId = _IpGroupProfileId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 15),
    _IpGroupProfileId_Type()
)
ipGroupProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupProfileId.setStatus("current")


class _IpGroupMediaRealm_Type(SnmpAdminString):
    """Custom type ipGroupMediaRealm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IpGroupMediaRealm_Type.__name__ = "SnmpAdminString"
_IpGroupMediaRealm_Object = MibTableColumn
ipGroupMediaRealm = _IpGroupMediaRealm_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 16),
    _IpGroupMediaRealm_Type()
)
ipGroupMediaRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupMediaRealm.setStatus("current")


class _IpGroupMaxNumOfRegUsers_Type(Integer32):
    """Custom type ipGroupMaxNumOfRegUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3000),
    )


_IpGroupMaxNumOfRegUsers_Type.__name__ = "Integer32"
_IpGroupMaxNumOfRegUsers_Object = MibTableColumn
ipGroupMaxNumOfRegUsers = _IpGroupMaxNumOfRegUsers_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 23, 21, 1, 17),
    _IpGroupMaxNumOfRegUsers_Type()
)
ipGroupMaxNumOfRegUsers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipGroupMaxNumOfRegUsers.setStatus("current")
_Sbc_ObjectIdentity = ObjectIdentity
sbc = _Sbc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24)
)


class _SbcEnable_Type(Integer32):
    """Custom type sbcEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SbcEnable_Type.__name__ = "Integer32"
_SbcEnable_Object = MibScalar
sbcEnable = _SbcEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 1),
    _SbcEnable_Type()
)
sbcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbcEnable.setStatus("deprecated")


class _SbcRegistrationTime_Type(Unsigned32):
    """Custom type sbcRegistrationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000000),
    )


_SbcRegistrationTime_Type.__name__ = "Unsigned32"
_SbcRegistrationTime_Object = MibScalar
sbcRegistrationTime = _SbcRegistrationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 2),
    _SbcRegistrationTime_Type()
)
sbcRegistrationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbcRegistrationTime.setStatus("current")


class _SbcEnableISBCApplication_Type(Integer32):
    """Custom type sbcEnableISBCApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SbcEnableISBCApplication_Type.__name__ = "Integer32"
_SbcEnableISBCApplication_Object = MibScalar
sbcEnableISBCApplication = _SbcEnableISBCApplication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 3),
    _SbcEnableISBCApplication_Type()
)
sbcEnableISBCApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbcEnableISBCApplication.setStatus("current")


class _SbcEnableIIP2IPApplication_Type(Integer32):
    """Custom type sbcEnableIIP2IPApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SbcEnableIIP2IPApplication_Type.__name__ = "Integer32"
_SbcEnableIIP2IPApplication_Object = MibScalar
sbcEnableIIP2IPApplication = _SbcEnableIIP2IPApplication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 4),
    _SbcEnableIIP2IPApplication_Type()
)
sbcEnableIIP2IPApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbcEnableIIP2IPApplication.setStatus("current")
_SbcClassificationTable_Object = MibTable
sbcClassificationTable = _SbcClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21)
)
if mibBuilder.loadTexts:
    sbcClassificationTable.setStatus("current")
_SbcClassificationEntry_Object = MibTableRow
sbcClassificationEntry = _SbcClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1)
)
sbcClassificationEntry.setIndexNames(
    (0, "AcGateway", "sbcClassificationIndex"),
)
if mibBuilder.loadTexts:
    sbcClassificationEntry.setStatus("current")


class _SbcClassificationIndex_Type(Unsigned32):
    """Custom type sbcClassificationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SbcClassificationIndex_Type.__name__ = "Unsigned32"
_SbcClassificationIndex_Object = MibTableColumn
sbcClassificationIndex = _SbcClassificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 1),
    _SbcClassificationIndex_Type()
)
sbcClassificationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcClassificationIndex.setStatus("current")
_SbcClassificationRowStatus_Type = RowStatus
_SbcClassificationRowStatus_Object = MibTableColumn
sbcClassificationRowStatus = _SbcClassificationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 2),
    _SbcClassificationRowStatus_Type()
)
sbcClassificationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcClassificationRowStatus.setStatus("current")


class _SbcClassificationAction_Type(Integer32):
    """Custom type sbcClassificationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcClassificationAction_Type.__name__ = "Integer32"
_SbcClassificationAction_Object = MibTableColumn
sbcClassificationAction = _SbcClassificationAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 3),
    _SbcClassificationAction_Type()
)
sbcClassificationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcClassificationAction.setStatus("current")


class _SbcClassificationActionResult_Type(Integer32):
    """Custom type sbcClassificationActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcClassificationActionResult_Type.__name__ = "Integer32"
_SbcClassificationActionResult_Object = MibTableColumn
sbcClassificationActionResult = _SbcClassificationActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 4),
    _SbcClassificationActionResult_Type()
)
sbcClassificationActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcClassificationActionResult.setStatus("current")


class _SbcClassificationSrcIPGroupId_Type(Integer32):
    """Custom type sbcClassificationSrcIPGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_SbcClassificationSrcIPGroupId_Type.__name__ = "Integer32"
_SbcClassificationSrcIPGroupId_Object = MibTableColumn
sbcClassificationSrcIPGroupId = _SbcClassificationSrcIPGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 5),
    _SbcClassificationSrcIPGroupId_Type()
)
sbcClassificationSrcIPGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcClassificationSrcIPGroupId.setStatus("current")


class _SbcClassificationSrcSRDId_Type(Integer32):
    """Custom type sbcClassificationSrcSRDId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4),
    )


_SbcClassificationSrcSRDId_Type.__name__ = "Integer32"
_SbcClassificationSrcSRDId_Object = MibTableColumn
sbcClassificationSrcSRDId = _SbcClassificationSrcSRDId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 6),
    _SbcClassificationSrcSRDId_Type()
)
sbcClassificationSrcSRDId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcClassificationSrcSRDId.setStatus("current")


class _SbcClassificationSrcAddress_Type(SnmpAdminString):
    """Custom type sbcClassificationSrcAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SbcClassificationSrcAddress_Type.__name__ = "SnmpAdminString"
_SbcClassificationSrcAddress_Object = MibTableColumn
sbcClassificationSrcAddress = _SbcClassificationSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 7),
    _SbcClassificationSrcAddress_Type()
)
sbcClassificationSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcClassificationSrcAddress.setStatus("current")


class _SbcClassificationSrcUsernamePrefix_Type(SnmpAdminString):
    """Custom type sbcClassificationSrcUsernamePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SbcClassificationSrcUsernamePrefix_Type.__name__ = "SnmpAdminString"
_SbcClassificationSrcUsernamePrefix_Object = MibTableColumn
sbcClassificationSrcUsernamePrefix = _SbcClassificationSrcUsernamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 8),
    _SbcClassificationSrcUsernamePrefix_Type()
)
sbcClassificationSrcUsernamePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcClassificationSrcUsernamePrefix.setStatus("current")


class _SbcClassificationSrcHost_Type(SnmpAdminString):
    """Custom type sbcClassificationSrcHost based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcClassificationSrcHost_Type.__name__ = "SnmpAdminString"
_SbcClassificationSrcHost_Object = MibTableColumn
sbcClassificationSrcHost = _SbcClassificationSrcHost_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 9),
    _SbcClassificationSrcHost_Type()
)
sbcClassificationSrcHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcClassificationSrcHost.setStatus("current")


class _SbcClassificationDestUsernamePrefix_Type(SnmpAdminString):
    """Custom type sbcClassificationDestUsernamePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SbcClassificationDestUsernamePrefix_Type.__name__ = "SnmpAdminString"
_SbcClassificationDestUsernamePrefix_Object = MibTableColumn
sbcClassificationDestUsernamePrefix = _SbcClassificationDestUsernamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 10),
    _SbcClassificationDestUsernamePrefix_Type()
)
sbcClassificationDestUsernamePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcClassificationDestUsernamePrefix.setStatus("current")


class _SbcClassificationDestHost_Type(SnmpAdminString):
    """Custom type sbcClassificationDestHost based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcClassificationDestHost_Type.__name__ = "SnmpAdminString"
_SbcClassificationDestHost_Object = MibTableColumn
sbcClassificationDestHost = _SbcClassificationDestHost_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 21, 1, 11),
    _SbcClassificationDestHost_Type()
)
sbcClassificationDestHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcClassificationDestHost.setStatus("current")
_SbcRoutingTable_Object = MibTable
sbcRoutingTable = _SbcRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22)
)
if mibBuilder.loadTexts:
    sbcRoutingTable.setStatus("current")
_SbcRoutingEntry_Object = MibTableRow
sbcRoutingEntry = _SbcRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1)
)
sbcRoutingEntry.setIndexNames(
    (0, "AcGateway", "sbcRoutingIndex"),
)
if mibBuilder.loadTexts:
    sbcRoutingEntry.setStatus("current")


class _SbcRoutingIndex_Type(Unsigned32):
    """Custom type sbcRoutingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 119),
    )


_SbcRoutingIndex_Type.__name__ = "Unsigned32"
_SbcRoutingIndex_Object = MibTableColumn
sbcRoutingIndex = _SbcRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 1),
    _SbcRoutingIndex_Type()
)
sbcRoutingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcRoutingIndex.setStatus("current")
_SbcRoutingRowStatus_Type = RowStatus
_SbcRoutingRowStatus_Object = MibTableColumn
sbcRoutingRowStatus = _SbcRoutingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 2),
    _SbcRoutingRowStatus_Type()
)
sbcRoutingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingRowStatus.setStatus("current")


class _SbcRoutingAction_Type(Integer32):
    """Custom type sbcRoutingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcRoutingAction_Type.__name__ = "Integer32"
_SbcRoutingAction_Object = MibTableColumn
sbcRoutingAction = _SbcRoutingAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 3),
    _SbcRoutingAction_Type()
)
sbcRoutingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcRoutingAction.setStatus("current")


class _SbcRoutingActionResult_Type(Integer32):
    """Custom type sbcRoutingActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcRoutingActionResult_Type.__name__ = "Integer32"
_SbcRoutingActionResult_Object = MibTableColumn
sbcRoutingActionResult = _SbcRoutingActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 4),
    _SbcRoutingActionResult_Type()
)
sbcRoutingActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcRoutingActionResult.setStatus("current")


class _SbcRoutingSrcIPGroupId_Type(Integer32):
    """Custom type sbcRoutingSrcIPGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_SbcRoutingSrcIPGroupId_Type.__name__ = "Integer32"
_SbcRoutingSrcIPGroupId_Object = MibTableColumn
sbcRoutingSrcIPGroupId = _SbcRoutingSrcIPGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 5),
    _SbcRoutingSrcIPGroupId_Type()
)
sbcRoutingSrcIPGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingSrcIPGroupId.setStatus("current")


class _SbcRoutingSrcUsernamePrefix_Type(SnmpAdminString):
    """Custom type sbcRoutingSrcUsernamePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SbcRoutingSrcUsernamePrefix_Type.__name__ = "SnmpAdminString"
_SbcRoutingSrcUsernamePrefix_Object = MibTableColumn
sbcRoutingSrcUsernamePrefix = _SbcRoutingSrcUsernamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 6),
    _SbcRoutingSrcUsernamePrefix_Type()
)
sbcRoutingSrcUsernamePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingSrcUsernamePrefix.setStatus("current")


class _SbcRoutingSrcHost_Type(SnmpAdminString):
    """Custom type sbcRoutingSrcHost based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcRoutingSrcHost_Type.__name__ = "SnmpAdminString"
_SbcRoutingSrcHost_Object = MibTableColumn
sbcRoutingSrcHost = _SbcRoutingSrcHost_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 7),
    _SbcRoutingSrcHost_Type()
)
sbcRoutingSrcHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingSrcHost.setStatus("current")


class _SbcRoutingDestUsernamePrefix_Type(SnmpAdminString):
    """Custom type sbcRoutingDestUsernamePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SbcRoutingDestUsernamePrefix_Type.__name__ = "SnmpAdminString"
_SbcRoutingDestUsernamePrefix_Object = MibTableColumn
sbcRoutingDestUsernamePrefix = _SbcRoutingDestUsernamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 8),
    _SbcRoutingDestUsernamePrefix_Type()
)
sbcRoutingDestUsernamePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingDestUsernamePrefix.setStatus("current")


class _SbcRoutingDestHost_Type(SnmpAdminString):
    """Custom type sbcRoutingDestHost based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcRoutingDestHost_Type.__name__ = "SnmpAdminString"
_SbcRoutingDestHost_Object = MibTableColumn
sbcRoutingDestHost = _SbcRoutingDestHost_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 9),
    _SbcRoutingDestHost_Type()
)
sbcRoutingDestHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingDestHost.setStatus("current")


class _SbcRoutingDestType_Type(Integer32):
    """Custom type sbcRoutingDestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dest", 1),
          ("enumTranslate", 3),
          ("ipGroup", 0),
          ("requestURI", 2))
    )


_SbcRoutingDestType_Type.__name__ = "Integer32"
_SbcRoutingDestType_Object = MibTableColumn
sbcRoutingDestType = _SbcRoutingDestType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 10),
    _SbcRoutingDestType_Type()
)
sbcRoutingDestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingDestType.setStatus("current")


class _SbcRoutingDestIPGroupId_Type(Integer32):
    """Custom type sbcRoutingDestIPGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_SbcRoutingDestIPGroupId_Type.__name__ = "Integer32"
_SbcRoutingDestIPGroupId_Object = MibTableColumn
sbcRoutingDestIPGroupId = _SbcRoutingDestIPGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 11),
    _SbcRoutingDestIPGroupId_Type()
)
sbcRoutingDestIPGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingDestIPGroupId.setStatus("current")


class _SbcRoutingDestSRDId_Type(Integer32):
    """Custom type sbcRoutingDestSRDId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4),
    )


_SbcRoutingDestSRDId_Type.__name__ = "Integer32"
_SbcRoutingDestSRDId_Object = MibTableColumn
sbcRoutingDestSRDId = _SbcRoutingDestSRDId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 12),
    _SbcRoutingDestSRDId_Type()
)
sbcRoutingDestSRDId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingDestSRDId.setStatus("current")


class _SbcRoutingDestAddress_Type(SnmpAdminString):
    """Custom type sbcRoutingDestAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SbcRoutingDestAddress_Type.__name__ = "SnmpAdminString"
_SbcRoutingDestAddress_Object = MibTableColumn
sbcRoutingDestAddress = _SbcRoutingDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 13),
    _SbcRoutingDestAddress_Type()
)
sbcRoutingDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingDestAddress.setStatus("current")


class _SbcRoutingDestPort_Type(Unsigned32):
    """Custom type sbcRoutingDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SbcRoutingDestPort_Type.__name__ = "Unsigned32"
_SbcRoutingDestPort_Object = MibTableColumn
sbcRoutingDestPort = _SbcRoutingDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 14),
    _SbcRoutingDestPort_Type()
)
sbcRoutingDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingDestPort.setStatus("current")


class _SbcRoutingDestTransportType_Type(Integer32):
    """Custom type sbcRoutingDestTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", -1),
          ("tcp", 1),
          ("tls", 2),
          ("udp", 0))
    )


_SbcRoutingDestTransportType_Type.__name__ = "Integer32"
_SbcRoutingDestTransportType_Object = MibTableColumn
sbcRoutingDestTransportType = _SbcRoutingDestTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 15),
    _SbcRoutingDestTransportType_Type()
)
sbcRoutingDestTransportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingDestTransportType.setStatus("current")


class _SbcRoutingAltRouteOptions_Type(Integer32):
    """Custom type sbcRoutingAltRouteOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("considerInputs", 2),
          ("ignoreInputs", 1),
          ("routeRow", 0))
    )


_SbcRoutingAltRouteOptions_Type.__name__ = "Integer32"
_SbcRoutingAltRouteOptions_Object = MibTableColumn
sbcRoutingAltRouteOptions = _SbcRoutingAltRouteOptions_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 16),
    _SbcRoutingAltRouteOptions_Type()
)
sbcRoutingAltRouteOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingAltRouteOptions.setStatus("current")


class _SbcRoutingRequestType_Type(Integer32):
    """Custom type sbcRoutingRequestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("invite", 1),
          ("inviteAndRegister", 4),
          ("inviteAndSubscribe", 5),
          ("register", 2),
          ("subscribe", 3))
    )


_SbcRoutingRequestType_Type.__name__ = "Integer32"
_SbcRoutingRequestType_Object = MibTableColumn
sbcRoutingRequestType = _SbcRoutingRequestType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 22, 1, 17),
    _SbcRoutingRequestType_Type()
)
sbcRoutingRequestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcRoutingRequestType.setStatus("current")
_SbcIP2IPInboundManipulationTable_Object = MibTable
sbcIP2IPInboundManipulationTable = _SbcIP2IPInboundManipulationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23)
)
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationTable.setStatus("current")
_SbcIP2IPInboundManipulationEntry_Object = MibTableRow
sbcIP2IPInboundManipulationEntry = _SbcIP2IPInboundManipulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1)
)
sbcIP2IPInboundManipulationEntry.setIndexNames(
    (0, "AcGateway", "sbcIP2IPInboundManipulationIndex"),
)
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationEntry.setStatus("current")


class _SbcIP2IPInboundManipulationIndex_Type(Unsigned32):
    """Custom type sbcIP2IPInboundManipulationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SbcIP2IPInboundManipulationIndex_Type.__name__ = "Unsigned32"
_SbcIP2IPInboundManipulationIndex_Object = MibTableColumn
sbcIP2IPInboundManipulationIndex = _SbcIP2IPInboundManipulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 1),
    _SbcIP2IPInboundManipulationIndex_Type()
)
sbcIP2IPInboundManipulationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationIndex.setStatus("current")
_SbcIP2IPInboundManipulationRowStatus_Type = RowStatus
_SbcIP2IPInboundManipulationRowStatus_Object = MibTableColumn
sbcIP2IPInboundManipulationRowStatus = _SbcIP2IPInboundManipulationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 2),
    _SbcIP2IPInboundManipulationRowStatus_Type()
)
sbcIP2IPInboundManipulationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationRowStatus.setStatus("current")


class _SbcIP2IPInboundManipulationAction_Type(Integer32):
    """Custom type sbcIP2IPInboundManipulationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcIP2IPInboundManipulationAction_Type.__name__ = "Integer32"
_SbcIP2IPInboundManipulationAction_Object = MibTableColumn
sbcIP2IPInboundManipulationAction = _SbcIP2IPInboundManipulationAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 3),
    _SbcIP2IPInboundManipulationAction_Type()
)
sbcIP2IPInboundManipulationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationAction.setStatus("current")


class _SbcIP2IPInboundManipulationActionResult_Type(Integer32):
    """Custom type sbcIP2IPInboundManipulationActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcIP2IPInboundManipulationActionResult_Type.__name__ = "Integer32"
_SbcIP2IPInboundManipulationActionResult_Object = MibTableColumn
sbcIP2IPInboundManipulationActionResult = _SbcIP2IPInboundManipulationActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 4),
    _SbcIP2IPInboundManipulationActionResult_Type()
)
sbcIP2IPInboundManipulationActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationActionResult.setStatus("current")


class _SbcIP2IPInboundManipulationIsAdditionalManipulation_Type(Integer32):
    """Custom type sbcIP2IPInboundManipulationIsAdditionalManipulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SbcIP2IPInboundManipulationIsAdditionalManipulation_Type.__name__ = "Integer32"
_SbcIP2IPInboundManipulationIsAdditionalManipulation_Object = MibTableColumn
sbcIP2IPInboundManipulationIsAdditionalManipulation = _SbcIP2IPInboundManipulationIsAdditionalManipulation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 5),
    _SbcIP2IPInboundManipulationIsAdditionalManipulation_Type()
)
sbcIP2IPInboundManipulationIsAdditionalManipulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationIsAdditionalManipulation.setStatus("current")


class _SbcIP2IPInboundManipulationManipulatedURI_Type(Integer32):
    """Custom type sbcIP2IPInboundManipulationManipulatedURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SbcIP2IPInboundManipulationManipulatedURI_Type.__name__ = "Integer32"
_SbcIP2IPInboundManipulationManipulatedURI_Object = MibTableColumn
sbcIP2IPInboundManipulationManipulatedURI = _SbcIP2IPInboundManipulationManipulatedURI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 6),
    _SbcIP2IPInboundManipulationManipulatedURI_Type()
)
sbcIP2IPInboundManipulationManipulatedURI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationManipulatedURI.setStatus("current")


class _SbcIP2IPInboundManipulationSrcIPGroupID_Type(Integer32):
    """Custom type sbcIP2IPInboundManipulationSrcIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_SbcIP2IPInboundManipulationSrcIPGroupID_Type.__name__ = "Integer32"
_SbcIP2IPInboundManipulationSrcIPGroupID_Object = MibTableColumn
sbcIP2IPInboundManipulationSrcIPGroupID = _SbcIP2IPInboundManipulationSrcIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 7),
    _SbcIP2IPInboundManipulationSrcIPGroupID_Type()
)
sbcIP2IPInboundManipulationSrcIPGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationSrcIPGroupID.setStatus("current")


class _SbcIP2IPInboundManipulationSrcUsernamePrefix_Type(SnmpAdminString):
    """Custom type sbcIP2IPInboundManipulationSrcUsernamePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SbcIP2IPInboundManipulationSrcUsernamePrefix_Type.__name__ = "SnmpAdminString"
_SbcIP2IPInboundManipulationSrcUsernamePrefix_Object = MibTableColumn
sbcIP2IPInboundManipulationSrcUsernamePrefix = _SbcIP2IPInboundManipulationSrcUsernamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 8),
    _SbcIP2IPInboundManipulationSrcUsernamePrefix_Type()
)
sbcIP2IPInboundManipulationSrcUsernamePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationSrcUsernamePrefix.setStatus("current")


class _SbcIP2IPInboundManipulationSrcHost_Type(SnmpAdminString):
    """Custom type sbcIP2IPInboundManipulationSrcHost based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcIP2IPInboundManipulationSrcHost_Type.__name__ = "SnmpAdminString"
_SbcIP2IPInboundManipulationSrcHost_Object = MibTableColumn
sbcIP2IPInboundManipulationSrcHost = _SbcIP2IPInboundManipulationSrcHost_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 9),
    _SbcIP2IPInboundManipulationSrcHost_Type()
)
sbcIP2IPInboundManipulationSrcHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationSrcHost.setStatus("current")


class _SbcIP2IPInboundManipulationDestUsernamePrefix_Type(SnmpAdminString):
    """Custom type sbcIP2IPInboundManipulationDestUsernamePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SbcIP2IPInboundManipulationDestUsernamePrefix_Type.__name__ = "SnmpAdminString"
_SbcIP2IPInboundManipulationDestUsernamePrefix_Object = MibTableColumn
sbcIP2IPInboundManipulationDestUsernamePrefix = _SbcIP2IPInboundManipulationDestUsernamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 10),
    _SbcIP2IPInboundManipulationDestUsernamePrefix_Type()
)
sbcIP2IPInboundManipulationDestUsernamePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationDestUsernamePrefix.setStatus("current")


class _SbcIP2IPInboundManipulationDestHost_Type(SnmpAdminString):
    """Custom type sbcIP2IPInboundManipulationDestHost based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcIP2IPInboundManipulationDestHost_Type.__name__ = "SnmpAdminString"
_SbcIP2IPInboundManipulationDestHost_Object = MibTableColumn
sbcIP2IPInboundManipulationDestHost = _SbcIP2IPInboundManipulationDestHost_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 11),
    _SbcIP2IPInboundManipulationDestHost_Type()
)
sbcIP2IPInboundManipulationDestHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationDestHost.setStatus("current")


class _SbcIP2IPInboundManipulationRemoveFromLeft_Type(Unsigned32):
    """Custom type sbcIP2IPInboundManipulationRemoveFromLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SbcIP2IPInboundManipulationRemoveFromLeft_Type.__name__ = "Unsigned32"
_SbcIP2IPInboundManipulationRemoveFromLeft_Object = MibTableColumn
sbcIP2IPInboundManipulationRemoveFromLeft = _SbcIP2IPInboundManipulationRemoveFromLeft_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 12),
    _SbcIP2IPInboundManipulationRemoveFromLeft_Type()
)
sbcIP2IPInboundManipulationRemoveFromLeft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationRemoveFromLeft.setStatus("current")


class _SbcIP2IPInboundManipulationRemoveFromRight_Type(Unsigned32):
    """Custom type sbcIP2IPInboundManipulationRemoveFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SbcIP2IPInboundManipulationRemoveFromRight_Type.__name__ = "Unsigned32"
_SbcIP2IPInboundManipulationRemoveFromRight_Object = MibTableColumn
sbcIP2IPInboundManipulationRemoveFromRight = _SbcIP2IPInboundManipulationRemoveFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 13),
    _SbcIP2IPInboundManipulationRemoveFromRight_Type()
)
sbcIP2IPInboundManipulationRemoveFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationRemoveFromRight.setStatus("current")


class _SbcIP2IPInboundManipulationLeaveFromRight_Type(Unsigned32):
    """Custom type sbcIP2IPInboundManipulationLeaveFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SbcIP2IPInboundManipulationLeaveFromRight_Type.__name__ = "Unsigned32"
_SbcIP2IPInboundManipulationLeaveFromRight_Object = MibTableColumn
sbcIP2IPInboundManipulationLeaveFromRight = _SbcIP2IPInboundManipulationLeaveFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 14),
    _SbcIP2IPInboundManipulationLeaveFromRight_Type()
)
sbcIP2IPInboundManipulationLeaveFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationLeaveFromRight.setStatus("current")


class _SbcIP2IPInboundManipulationPrefix2Add_Type(SnmpAdminString):
    """Custom type sbcIP2IPInboundManipulationPrefix2Add based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcIP2IPInboundManipulationPrefix2Add_Type.__name__ = "SnmpAdminString"
_SbcIP2IPInboundManipulationPrefix2Add_Object = MibTableColumn
sbcIP2IPInboundManipulationPrefix2Add = _SbcIP2IPInboundManipulationPrefix2Add_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 15),
    _SbcIP2IPInboundManipulationPrefix2Add_Type()
)
sbcIP2IPInboundManipulationPrefix2Add.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationPrefix2Add.setStatus("current")


class _SbcIP2IPInboundManipulationSuffix2Add_Type(SnmpAdminString):
    """Custom type sbcIP2IPInboundManipulationSuffix2Add based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcIP2IPInboundManipulationSuffix2Add_Type.__name__ = "SnmpAdminString"
_SbcIP2IPInboundManipulationSuffix2Add_Object = MibTableColumn
sbcIP2IPInboundManipulationSuffix2Add = _SbcIP2IPInboundManipulationSuffix2Add_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 16),
    _SbcIP2IPInboundManipulationSuffix2Add_Type()
)
sbcIP2IPInboundManipulationSuffix2Add.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationSuffix2Add.setStatus("current")


class _SbcIP2IPInboundManipulationRequestType_Type(Integer32):
    """Custom type sbcIP2IPInboundManipulationRequestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("invite", 1),
          ("inviteAndRegister", 4),
          ("inviteAndSubscribe", 5),
          ("register", 2),
          ("subscribe", 3))
    )


_SbcIP2IPInboundManipulationRequestType_Type.__name__ = "Integer32"
_SbcIP2IPInboundManipulationRequestType_Object = MibTableColumn
sbcIP2IPInboundManipulationRequestType = _SbcIP2IPInboundManipulationRequestType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 23, 1, 17),
    _SbcIP2IPInboundManipulationRequestType_Type()
)
sbcIP2IPInboundManipulationRequestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPInboundManipulationRequestType.setStatus("current")
_SbcIP2IPOutboundManipulationTable_Object = MibTable
sbcIP2IPOutboundManipulationTable = _SbcIP2IPOutboundManipulationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24)
)
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationTable.setStatus("current")
_SbcIP2IPOutboundManipulationEntry_Object = MibTableRow
sbcIP2IPOutboundManipulationEntry = _SbcIP2IPOutboundManipulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1)
)
sbcIP2IPOutboundManipulationEntry.setIndexNames(
    (0, "AcGateway", "sbcIP2IPOutboundManipulationIndex"),
)
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationEntry.setStatus("current")


class _SbcIP2IPOutboundManipulationIndex_Type(Unsigned32):
    """Custom type sbcIP2IPOutboundManipulationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SbcIP2IPOutboundManipulationIndex_Type.__name__ = "Unsigned32"
_SbcIP2IPOutboundManipulationIndex_Object = MibTableColumn
sbcIP2IPOutboundManipulationIndex = _SbcIP2IPOutboundManipulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 1),
    _SbcIP2IPOutboundManipulationIndex_Type()
)
sbcIP2IPOutboundManipulationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationIndex.setStatus("current")
_SbcIP2IPOutboundManipulationRowStatus_Type = RowStatus
_SbcIP2IPOutboundManipulationRowStatus_Object = MibTableColumn
sbcIP2IPOutboundManipulationRowStatus = _SbcIP2IPOutboundManipulationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 2),
    _SbcIP2IPOutboundManipulationRowStatus_Type()
)
sbcIP2IPOutboundManipulationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationRowStatus.setStatus("current")


class _SbcIP2IPOutboundManipulationAction_Type(Integer32):
    """Custom type sbcIP2IPOutboundManipulationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcIP2IPOutboundManipulationAction_Type.__name__ = "Integer32"
_SbcIP2IPOutboundManipulationAction_Object = MibTableColumn
sbcIP2IPOutboundManipulationAction = _SbcIP2IPOutboundManipulationAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 3),
    _SbcIP2IPOutboundManipulationAction_Type()
)
sbcIP2IPOutboundManipulationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationAction.setStatus("current")


class _SbcIP2IPOutboundManipulationActionResult_Type(Integer32):
    """Custom type sbcIP2IPOutboundManipulationActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcIP2IPOutboundManipulationActionResult_Type.__name__ = "Integer32"
_SbcIP2IPOutboundManipulationActionResult_Object = MibTableColumn
sbcIP2IPOutboundManipulationActionResult = _SbcIP2IPOutboundManipulationActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 4),
    _SbcIP2IPOutboundManipulationActionResult_Type()
)
sbcIP2IPOutboundManipulationActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationActionResult.setStatus("current")


class _SbcIP2IPOutboundManipulationIsAdditionalManipulation_Type(Integer32):
    """Custom type sbcIP2IPOutboundManipulationIsAdditionalManipulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SbcIP2IPOutboundManipulationIsAdditionalManipulation_Type.__name__ = "Integer32"
_SbcIP2IPOutboundManipulationIsAdditionalManipulation_Object = MibTableColumn
sbcIP2IPOutboundManipulationIsAdditionalManipulation = _SbcIP2IPOutboundManipulationIsAdditionalManipulation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 5),
    _SbcIP2IPOutboundManipulationIsAdditionalManipulation_Type()
)
sbcIP2IPOutboundManipulationIsAdditionalManipulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationIsAdditionalManipulation.setStatus("current")


class _SbcIP2IPOutboundManipulationManipulatedURI_Type(Integer32):
    """Custom type sbcIP2IPOutboundManipulationManipulatedURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SbcIP2IPOutboundManipulationManipulatedURI_Type.__name__ = "Integer32"
_SbcIP2IPOutboundManipulationManipulatedURI_Object = MibTableColumn
sbcIP2IPOutboundManipulationManipulatedURI = _SbcIP2IPOutboundManipulationManipulatedURI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 6),
    _SbcIP2IPOutboundManipulationManipulatedURI_Type()
)
sbcIP2IPOutboundManipulationManipulatedURI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationManipulatedURI.setStatus("current")


class _SbcIP2IPOutboundManipulationSrcIPGroupID_Type(Integer32):
    """Custom type sbcIP2IPOutboundManipulationSrcIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_SbcIP2IPOutboundManipulationSrcIPGroupID_Type.__name__ = "Integer32"
_SbcIP2IPOutboundManipulationSrcIPGroupID_Object = MibTableColumn
sbcIP2IPOutboundManipulationSrcIPGroupID = _SbcIP2IPOutboundManipulationSrcIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 7),
    _SbcIP2IPOutboundManipulationSrcIPGroupID_Type()
)
sbcIP2IPOutboundManipulationSrcIPGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationSrcIPGroupID.setStatus("current")


class _SbcIP2IPOutboundManipulationDestIPGroupID_Type(Integer32):
    """Custom type sbcIP2IPOutboundManipulationDestIPGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_SbcIP2IPOutboundManipulationDestIPGroupID_Type.__name__ = "Integer32"
_SbcIP2IPOutboundManipulationDestIPGroupID_Object = MibTableColumn
sbcIP2IPOutboundManipulationDestIPGroupID = _SbcIP2IPOutboundManipulationDestIPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 8),
    _SbcIP2IPOutboundManipulationDestIPGroupID_Type()
)
sbcIP2IPOutboundManipulationDestIPGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationDestIPGroupID.setStatus("current")


class _SbcIP2IPOutboundManipulationSrcUsernamePrefix_Type(SnmpAdminString):
    """Custom type sbcIP2IPOutboundManipulationSrcUsernamePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SbcIP2IPOutboundManipulationSrcUsernamePrefix_Type.__name__ = "SnmpAdminString"
_SbcIP2IPOutboundManipulationSrcUsernamePrefix_Object = MibTableColumn
sbcIP2IPOutboundManipulationSrcUsernamePrefix = _SbcIP2IPOutboundManipulationSrcUsernamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 9),
    _SbcIP2IPOutboundManipulationSrcUsernamePrefix_Type()
)
sbcIP2IPOutboundManipulationSrcUsernamePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationSrcUsernamePrefix.setStatus("current")


class _SbcIP2IPOutboundManipulationSrcHost_Type(SnmpAdminString):
    """Custom type sbcIP2IPOutboundManipulationSrcHost based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcIP2IPOutboundManipulationSrcHost_Type.__name__ = "SnmpAdminString"
_SbcIP2IPOutboundManipulationSrcHost_Object = MibTableColumn
sbcIP2IPOutboundManipulationSrcHost = _SbcIP2IPOutboundManipulationSrcHost_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 10),
    _SbcIP2IPOutboundManipulationSrcHost_Type()
)
sbcIP2IPOutboundManipulationSrcHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationSrcHost.setStatus("current")


class _SbcIP2IPOutboundManipulationDestUsernamePrefix_Type(SnmpAdminString):
    """Custom type sbcIP2IPOutboundManipulationDestUsernamePrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SbcIP2IPOutboundManipulationDestUsernamePrefix_Type.__name__ = "SnmpAdminString"
_SbcIP2IPOutboundManipulationDestUsernamePrefix_Object = MibTableColumn
sbcIP2IPOutboundManipulationDestUsernamePrefix = _SbcIP2IPOutboundManipulationDestUsernamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 11),
    _SbcIP2IPOutboundManipulationDestUsernamePrefix_Type()
)
sbcIP2IPOutboundManipulationDestUsernamePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationDestUsernamePrefix.setStatus("current")


class _SbcIP2IPOutboundManipulationDestHost_Type(SnmpAdminString):
    """Custom type sbcIP2IPOutboundManipulationDestHost based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcIP2IPOutboundManipulationDestHost_Type.__name__ = "SnmpAdminString"
_SbcIP2IPOutboundManipulationDestHost_Object = MibTableColumn
sbcIP2IPOutboundManipulationDestHost = _SbcIP2IPOutboundManipulationDestHost_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 12),
    _SbcIP2IPOutboundManipulationDestHost_Type()
)
sbcIP2IPOutboundManipulationDestHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationDestHost.setStatus("current")


class _SbcIP2IPOutboundManipulationRemoveFromLeft_Type(Unsigned32):
    """Custom type sbcIP2IPOutboundManipulationRemoveFromLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SbcIP2IPOutboundManipulationRemoveFromLeft_Type.__name__ = "Unsigned32"
_SbcIP2IPOutboundManipulationRemoveFromLeft_Object = MibTableColumn
sbcIP2IPOutboundManipulationRemoveFromLeft = _SbcIP2IPOutboundManipulationRemoveFromLeft_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 13),
    _SbcIP2IPOutboundManipulationRemoveFromLeft_Type()
)
sbcIP2IPOutboundManipulationRemoveFromLeft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationRemoveFromLeft.setStatus("current")


class _SbcIP2IPOutboundManipulationRemoveFromRight_Type(Unsigned32):
    """Custom type sbcIP2IPOutboundManipulationRemoveFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SbcIP2IPOutboundManipulationRemoveFromRight_Type.__name__ = "Unsigned32"
_SbcIP2IPOutboundManipulationRemoveFromRight_Object = MibTableColumn
sbcIP2IPOutboundManipulationRemoveFromRight = _SbcIP2IPOutboundManipulationRemoveFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 14),
    _SbcIP2IPOutboundManipulationRemoveFromRight_Type()
)
sbcIP2IPOutboundManipulationRemoveFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationRemoveFromRight.setStatus("current")


class _SbcIP2IPOutboundManipulationLeaveFromRight_Type(Unsigned32):
    """Custom type sbcIP2IPOutboundManipulationLeaveFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SbcIP2IPOutboundManipulationLeaveFromRight_Type.__name__ = "Unsigned32"
_SbcIP2IPOutboundManipulationLeaveFromRight_Object = MibTableColumn
sbcIP2IPOutboundManipulationLeaveFromRight = _SbcIP2IPOutboundManipulationLeaveFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 15),
    _SbcIP2IPOutboundManipulationLeaveFromRight_Type()
)
sbcIP2IPOutboundManipulationLeaveFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationLeaveFromRight.setStatus("current")


class _SbcIP2IPOutboundManipulationPrefix2Add_Type(SnmpAdminString):
    """Custom type sbcIP2IPOutboundManipulationPrefix2Add based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcIP2IPOutboundManipulationPrefix2Add_Type.__name__ = "SnmpAdminString"
_SbcIP2IPOutboundManipulationPrefix2Add_Object = MibTableColumn
sbcIP2IPOutboundManipulationPrefix2Add = _SbcIP2IPOutboundManipulationPrefix2Add_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 16),
    _SbcIP2IPOutboundManipulationPrefix2Add_Type()
)
sbcIP2IPOutboundManipulationPrefix2Add.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationPrefix2Add.setStatus("current")


class _SbcIP2IPOutboundManipulationSuffix2Add_Type(SnmpAdminString):
    """Custom type sbcIP2IPOutboundManipulationSuffix2Add based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcIP2IPOutboundManipulationSuffix2Add_Type.__name__ = "SnmpAdminString"
_SbcIP2IPOutboundManipulationSuffix2Add_Object = MibTableColumn
sbcIP2IPOutboundManipulationSuffix2Add = _SbcIP2IPOutboundManipulationSuffix2Add_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 17),
    _SbcIP2IPOutboundManipulationSuffix2Add_Type()
)
sbcIP2IPOutboundManipulationSuffix2Add.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationSuffix2Add.setStatus("current")


class _SbcIP2IPOutboundManipulationRequestType_Type(Integer32):
    """Custom type sbcIP2IPOutboundManipulationRequestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("invite", 1),
          ("inviteAndRegister", 4),
          ("inviteAndSubscribe", 5),
          ("register", 2),
          ("subscribe", 3))
    )


_SbcIP2IPOutboundManipulationRequestType_Type.__name__ = "Integer32"
_SbcIP2IPOutboundManipulationRequestType_Object = MibTableColumn
sbcIP2IPOutboundManipulationRequestType = _SbcIP2IPOutboundManipulationRequestType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 24, 1, 18),
    _SbcIP2IPOutboundManipulationRequestType_Type()
)
sbcIP2IPOutboundManipulationRequestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcIP2IPOutboundManipulationRequestType.setStatus("current")
_SbcAdmissionControlTable_Object = MibTable
sbcAdmissionControlTable = _SbcAdmissionControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25)
)
if mibBuilder.loadTexts:
    sbcAdmissionControlTable.setStatus("current")
_SbcAdmissionControlEntry_Object = MibTableRow
sbcAdmissionControlEntry = _SbcAdmissionControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1)
)
sbcAdmissionControlEntry.setIndexNames(
    (0, "AcGateway", "sbcAdmissionControlIndex"),
)
if mibBuilder.loadTexts:
    sbcAdmissionControlEntry.setStatus("current")


class _SbcAdmissionControlIndex_Type(Unsigned32):
    """Custom type sbcAdmissionControlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SbcAdmissionControlIndex_Type.__name__ = "Unsigned32"
_SbcAdmissionControlIndex_Object = MibTableColumn
sbcAdmissionControlIndex = _SbcAdmissionControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 1),
    _SbcAdmissionControlIndex_Type()
)
sbcAdmissionControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcAdmissionControlIndex.setStatus("current")
_SbcAdmissionControlRowStatus_Type = RowStatus
_SbcAdmissionControlRowStatus_Object = MibTableColumn
sbcAdmissionControlRowStatus = _SbcAdmissionControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 2),
    _SbcAdmissionControlRowStatus_Type()
)
sbcAdmissionControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcAdmissionControlRowStatus.setStatus("current")


class _SbcAdmissionControlAction_Type(Integer32):
    """Custom type sbcAdmissionControlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcAdmissionControlAction_Type.__name__ = "Integer32"
_SbcAdmissionControlAction_Object = MibTableColumn
sbcAdmissionControlAction = _SbcAdmissionControlAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 3),
    _SbcAdmissionControlAction_Type()
)
sbcAdmissionControlAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcAdmissionControlAction.setStatus("current")


class _SbcAdmissionControlActionResult_Type(Integer32):
    """Custom type sbcAdmissionControlActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcAdmissionControlActionResult_Type.__name__ = "Integer32"
_SbcAdmissionControlActionResult_Object = MibTableColumn
sbcAdmissionControlActionResult = _SbcAdmissionControlActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 4),
    _SbcAdmissionControlActionResult_Type()
)
sbcAdmissionControlActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcAdmissionControlActionResult.setStatus("current")


class _SbcAdmissionControlLimitType_Type(Integer32):
    """Custom type sbcAdmissionControlLimitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipGroup", 0),
          ("sRD", 1))
    )


_SbcAdmissionControlLimitType_Type.__name__ = "Integer32"
_SbcAdmissionControlLimitType_Object = MibTableColumn
sbcAdmissionControlLimitType = _SbcAdmissionControlLimitType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 5),
    _SbcAdmissionControlLimitType_Type()
)
sbcAdmissionControlLimitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcAdmissionControlLimitType.setStatus("current")


class _SbcAdmissionControlIpGroupID_Type(Integer32):
    """Custom type sbcAdmissionControlIpGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_SbcAdmissionControlIpGroupID_Type.__name__ = "Integer32"
_SbcAdmissionControlIpGroupID_Object = MibTableColumn
sbcAdmissionControlIpGroupID = _SbcAdmissionControlIpGroupID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 6),
    _SbcAdmissionControlIpGroupID_Type()
)
sbcAdmissionControlIpGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcAdmissionControlIpGroupID.setStatus("current")


class _SbcAdmissionControlSrdID_Type(Integer32):
    """Custom type sbcAdmissionControlSrdID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4),
    )


_SbcAdmissionControlSrdID_Type.__name__ = "Integer32"
_SbcAdmissionControlSrdID_Object = MibTableColumn
sbcAdmissionControlSrdID = _SbcAdmissionControlSrdID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 7),
    _SbcAdmissionControlSrdID_Type()
)
sbcAdmissionControlSrdID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcAdmissionControlSrdID.setStatus("current")


class _SbcAdmissionControlRequestType_Type(Integer32):
    """Custom type sbcAdmissionControlRequestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("invite", 1),
          ("other", 3),
          ("subscribe", 2))
    )


_SbcAdmissionControlRequestType_Type.__name__ = "Integer32"
_SbcAdmissionControlRequestType_Object = MibTableColumn
sbcAdmissionControlRequestType = _SbcAdmissionControlRequestType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 8),
    _SbcAdmissionControlRequestType_Type()
)
sbcAdmissionControlRequestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcAdmissionControlRequestType.setStatus("current")


class _SbcAdmissionControlRequestDirection_Type(Integer32):
    """Custom type sbcAdmissionControlRequestDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("in", 1),
          ("out", 2))
    )


_SbcAdmissionControlRequestDirection_Type.__name__ = "Integer32"
_SbcAdmissionControlRequestDirection_Object = MibTableColumn
sbcAdmissionControlRequestDirection = _SbcAdmissionControlRequestDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 9),
    _SbcAdmissionControlRequestDirection_Type()
)
sbcAdmissionControlRequestDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcAdmissionControlRequestDirection.setStatus("current")


class _SbcAdmissionControlLimit_Type(Integer32):
    """Custom type sbcAdmissionControlLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SbcAdmissionControlLimit_Type.__name__ = "Integer32"
_SbcAdmissionControlLimit_Object = MibTableColumn
sbcAdmissionControlLimit = _SbcAdmissionControlLimit_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 10),
    _SbcAdmissionControlLimit_Type()
)
sbcAdmissionControlLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcAdmissionControlLimit.setStatus("current")


class _SbcAdmissionControlLimitPerUser_Type(Integer32):
    """Custom type sbcAdmissionControlLimitPerUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SbcAdmissionControlLimitPerUser_Type.__name__ = "Integer32"
_SbcAdmissionControlLimitPerUser_Object = MibTableColumn
sbcAdmissionControlLimitPerUser = _SbcAdmissionControlLimitPerUser_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 25, 1, 11),
    _SbcAdmissionControlLimitPerUser_Type()
)
sbcAdmissionControlLimitPerUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcAdmissionControlLimitPerUser.setStatus("current")
_SbcMessageManipulationsTable_Object = MibTable
sbcMessageManipulationsTable = _SbcMessageManipulationsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26)
)
if mibBuilder.loadTexts:
    sbcMessageManipulationsTable.setStatus("current")
_SbcMessageManipulationsEntry_Object = MibTableRow
sbcMessageManipulationsEntry = _SbcMessageManipulationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1)
)
sbcMessageManipulationsEntry.setIndexNames(
    (0, "AcGateway", "sbcMessageManipulationsIndex"),
)
if mibBuilder.loadTexts:
    sbcMessageManipulationsEntry.setStatus("current")


class _SbcMessageManipulationsIndex_Type(Unsigned32):
    """Custom type sbcMessageManipulationsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_SbcMessageManipulationsIndex_Type.__name__ = "Unsigned32"
_SbcMessageManipulationsIndex_Object = MibTableColumn
sbcMessageManipulationsIndex = _SbcMessageManipulationsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 1),
    _SbcMessageManipulationsIndex_Type()
)
sbcMessageManipulationsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcMessageManipulationsIndex.setStatus("current")
_SbcMessageManipulationsRowStatus_Type = RowStatus
_SbcMessageManipulationsRowStatus_Object = MibTableColumn
sbcMessageManipulationsRowStatus = _SbcMessageManipulationsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 2),
    _SbcMessageManipulationsRowStatus_Type()
)
sbcMessageManipulationsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcMessageManipulationsRowStatus.setStatus("current")


class _SbcMessageManipulationsAction_Type(Integer32):
    """Custom type sbcMessageManipulationsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcMessageManipulationsAction_Type.__name__ = "Integer32"
_SbcMessageManipulationsAction_Object = MibTableColumn
sbcMessageManipulationsAction = _SbcMessageManipulationsAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 3),
    _SbcMessageManipulationsAction_Type()
)
sbcMessageManipulationsAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcMessageManipulationsAction.setStatus("current")


class _SbcMessageManipulationsActionResult_Type(Integer32):
    """Custom type sbcMessageManipulationsActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcMessageManipulationsActionResult_Type.__name__ = "Integer32"
_SbcMessageManipulationsActionResult_Object = MibTableColumn
sbcMessageManipulationsActionResult = _SbcMessageManipulationsActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 4),
    _SbcMessageManipulationsActionResult_Type()
)
sbcMessageManipulationsActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcMessageManipulationsActionResult.setStatus("current")


class _SbcMessageManipulationsManipulationSetID_Type(Unsigned32):
    """Custom type sbcMessageManipulationsManipulationSetID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SbcMessageManipulationsManipulationSetID_Type.__name__ = "Unsigned32"
_SbcMessageManipulationsManipulationSetID_Object = MibTableColumn
sbcMessageManipulationsManipulationSetID = _SbcMessageManipulationsManipulationSetID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 5),
    _SbcMessageManipulationsManipulationSetID_Type()
)
sbcMessageManipulationsManipulationSetID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcMessageManipulationsManipulationSetID.setStatus("current")


class _SbcMessageManipulationsMessageType_Type(SnmpAdminString):
    """Custom type sbcMessageManipulationsMessageType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SbcMessageManipulationsMessageType_Type.__name__ = "SnmpAdminString"
_SbcMessageManipulationsMessageType_Object = MibTableColumn
sbcMessageManipulationsMessageType = _SbcMessageManipulationsMessageType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 6),
    _SbcMessageManipulationsMessageType_Type()
)
sbcMessageManipulationsMessageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcMessageManipulationsMessageType.setStatus("current")


class _SbcMessageManipulationsCondition_Type(SnmpAdminString):
    """Custom type sbcMessageManipulationsCondition based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 199),
    )


_SbcMessageManipulationsCondition_Type.__name__ = "SnmpAdminString"
_SbcMessageManipulationsCondition_Object = MibTableColumn
sbcMessageManipulationsCondition = _SbcMessageManipulationsCondition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 7),
    _SbcMessageManipulationsCondition_Type()
)
sbcMessageManipulationsCondition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcMessageManipulationsCondition.setStatus("current")


class _SbcMessageManipulationsActionSubject_Type(SnmpAdminString):
    """Custom type sbcMessageManipulationsActionSubject based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_SbcMessageManipulationsActionSubject_Type.__name__ = "SnmpAdminString"
_SbcMessageManipulationsActionSubject_Object = MibTableColumn
sbcMessageManipulationsActionSubject = _SbcMessageManipulationsActionSubject_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 8),
    _SbcMessageManipulationsActionSubject_Type()
)
sbcMessageManipulationsActionSubject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcMessageManipulationsActionSubject.setStatus("current")


class _SbcMessageManipulationsActionType_Type(Integer32):
    """Custom type sbcMessageManipulationsActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("addPrefix", 3),
          ("addSuffix", 4),
          ("modify", 2),
          ("remove", 1),
          ("removePrefix", 6),
          ("removeSuffix", 5))
    )


_SbcMessageManipulationsActionType_Type.__name__ = "Integer32"
_SbcMessageManipulationsActionType_Object = MibTableColumn
sbcMessageManipulationsActionType = _SbcMessageManipulationsActionType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 9),
    _SbcMessageManipulationsActionType_Type()
)
sbcMessageManipulationsActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcMessageManipulationsActionType.setStatus("current")


class _SbcMessageManipulationsActionValue_Type(SnmpAdminString):
    """Custom type sbcMessageManipulationsActionValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 199),
    )


_SbcMessageManipulationsActionValue_Type.__name__ = "SnmpAdminString"
_SbcMessageManipulationsActionValue_Object = MibTableColumn
sbcMessageManipulationsActionValue = _SbcMessageManipulationsActionValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 10),
    _SbcMessageManipulationsActionValue_Type()
)
sbcMessageManipulationsActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcMessageManipulationsActionValue.setStatus("current")


class _SbcMessageManipulationsRowRole_Type(Integer32):
    """Custom type sbcMessageManipulationsRowRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("actionOnly", 1),
          ("matchAndAction", 0))
    )


_SbcMessageManipulationsRowRole_Type.__name__ = "Integer32"
_SbcMessageManipulationsRowRole_Object = MibTableColumn
sbcMessageManipulationsRowRole = _SbcMessageManipulationsRowRole_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 26, 1, 11),
    _SbcMessageManipulationsRowRole_Type()
)
sbcMessageManipulationsRowRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcMessageManipulationsRowRole.setStatus("current")
_SbcAlternativeRoutingReasonsTable_Object = MibTable
sbcAlternativeRoutingReasonsTable = _SbcAlternativeRoutingReasonsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 27)
)
if mibBuilder.loadTexts:
    sbcAlternativeRoutingReasonsTable.setStatus("current")
_SbcAlternativeRoutingReasonsEntry_Object = MibTableRow
sbcAlternativeRoutingReasonsEntry = _SbcAlternativeRoutingReasonsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 27, 1)
)
sbcAlternativeRoutingReasonsEntry.setIndexNames(
    (0, "AcGateway", "sbcAlternativeRoutingReasonsIndex"),
)
if mibBuilder.loadTexts:
    sbcAlternativeRoutingReasonsEntry.setStatus("current")


class _SbcAlternativeRoutingReasonsIndex_Type(Unsigned32):
    """Custom type sbcAlternativeRoutingReasonsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SbcAlternativeRoutingReasonsIndex_Type.__name__ = "Unsigned32"
_SbcAlternativeRoutingReasonsIndex_Object = MibTableColumn
sbcAlternativeRoutingReasonsIndex = _SbcAlternativeRoutingReasonsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 27, 1, 1),
    _SbcAlternativeRoutingReasonsIndex_Type()
)
sbcAlternativeRoutingReasonsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcAlternativeRoutingReasonsIndex.setStatus("current")
_SbcAlternativeRoutingReasonsRowStatus_Type = RowStatus
_SbcAlternativeRoutingReasonsRowStatus_Object = MibTableColumn
sbcAlternativeRoutingReasonsRowStatus = _SbcAlternativeRoutingReasonsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 27, 1, 2),
    _SbcAlternativeRoutingReasonsRowStatus_Type()
)
sbcAlternativeRoutingReasonsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcAlternativeRoutingReasonsRowStatus.setStatus("current")


class _SbcAlternativeRoutingReasonsAction_Type(Integer32):
    """Custom type sbcAlternativeRoutingReasonsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcAlternativeRoutingReasonsAction_Type.__name__ = "Integer32"
_SbcAlternativeRoutingReasonsAction_Object = MibTableColumn
sbcAlternativeRoutingReasonsAction = _SbcAlternativeRoutingReasonsAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 27, 1, 3),
    _SbcAlternativeRoutingReasonsAction_Type()
)
sbcAlternativeRoutingReasonsAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcAlternativeRoutingReasonsAction.setStatus("current")


class _SbcAlternativeRoutingReasonsActionResult_Type(Integer32):
    """Custom type sbcAlternativeRoutingReasonsActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SbcAlternativeRoutingReasonsActionResult_Type.__name__ = "Integer32"
_SbcAlternativeRoutingReasonsActionResult_Object = MibTableColumn
sbcAlternativeRoutingReasonsActionResult = _SbcAlternativeRoutingReasonsActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 27, 1, 4),
    _SbcAlternativeRoutingReasonsActionResult_Type()
)
sbcAlternativeRoutingReasonsActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbcAlternativeRoutingReasonsActionResult.setStatus("current")


class _SbcAlternativeRoutingReasonsReleaseCause_Type(Unsigned32):
    """Custom type sbcAlternativeRoutingReasonsReleaseCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_SbcAlternativeRoutingReasonsReleaseCause_Type.__name__ = "Unsigned32"
_SbcAlternativeRoutingReasonsReleaseCause_Object = MibTableColumn
sbcAlternativeRoutingReasonsReleaseCause = _SbcAlternativeRoutingReasonsReleaseCause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 24, 27, 1, 5),
    _SbcAlternativeRoutingReasonsReleaseCause_Type()
)
sbcAlternativeRoutingReasonsReleaseCause.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sbcAlternativeRoutingReasonsReleaseCause.setStatus("current")
_GwIPv6_ObjectIdentity = ObjectIdentity
gwIPv6 = _GwIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 25)
)


class _GwIPv6GwAppDualIPStackSDPMethod_Type(Integer32):
    """Custom type gwIPv6GwAppDualIPStackSDPMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aNAT", 1),
          ("nONE", 0))
    )


_GwIPv6GwAppDualIPStackSDPMethod_Type.__name__ = "Integer32"
_GwIPv6GwAppDualIPStackSDPMethod_Object = MibScalar
gwIPv6GwAppDualIPStackSDPMethod = _GwIPv6GwAppDualIPStackSDPMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 25, 1),
    _GwIPv6GwAppDualIPStackSDPMethod_Type()
)
gwIPv6GwAppDualIPStackSDPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwIPv6GwAppDualIPStackSDPMethod.setStatus("current")


class _GwIPv6GwAppPrimaryMediaInterface_Type(Integer32):
    """Custom type gwIPv6GwAppPrimaryMediaInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32),
    )


_GwIPv6GwAppPrimaryMediaInterface_Type.__name__ = "Integer32"
_GwIPv6GwAppPrimaryMediaInterface_Object = MibScalar
gwIPv6GwAppPrimaryMediaInterface = _GwIPv6GwAppPrimaryMediaInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 25, 2),
    _GwIPv6GwAppPrimaryMediaInterface_Type()
)
gwIPv6GwAppPrimaryMediaInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwIPv6GwAppPrimaryMediaInterface.setStatus("current")


class _GwIPv6GwAppSecondaryMediaInterface_Type(Integer32):
    """Custom type gwIPv6GwAppSecondaryMediaInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32),
    )


_GwIPv6GwAppSecondaryMediaInterface_Type.__name__ = "Integer32"
_GwIPv6GwAppSecondaryMediaInterface_Object = MibScalar
gwIPv6GwAppSecondaryMediaInterface = _GwIPv6GwAppSecondaryMediaInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 25, 3),
    _GwIPv6GwAppSecondaryMediaInterface_Type()
)
gwIPv6GwAppSecondaryMediaInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwIPv6GwAppSecondaryMediaInterface.setStatus("current")


class _GwIPv6MediaIPVersionPreference_Type(Integer32):
    """Custom type gwIPv6MediaIPVersionPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onlyIPv4", 0),
          ("onlyIPv6", 1),
          ("preferIPv4", 2),
          ("preferIPv6", 3))
    )


_GwIPv6MediaIPVersionPreference_Type.__name__ = "Integer32"
_GwIPv6MediaIPVersionPreference_Object = MibScalar
gwIPv6MediaIPVersionPreference = _GwIPv6MediaIPVersionPreference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 25, 4),
    _GwIPv6MediaIPVersionPreference_Type()
)
gwIPv6MediaIPVersionPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwIPv6MediaIPVersionPreference.setStatus("current")
_SrdSettings_ObjectIdentity = ObjectIdentity
srdSettings = _SrdSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26)
)
_SrdTable_Object = MibTable
srdTable = _SrdTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21)
)
if mibBuilder.loadTexts:
    srdTable.setStatus("current")
_SrdEntry_Object = MibTableRow
srdEntry = _SrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21, 1)
)
srdEntry.setIndexNames(
    (0, "AcGateway", "srdIndex"),
)
if mibBuilder.loadTexts:
    srdEntry.setStatus("current")


class _SrdIndex_Type(Unsigned32):
    """Custom type srdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SrdIndex_Type.__name__ = "Unsigned32"
_SrdIndex_Object = MibTableColumn
srdIndex = _SrdIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21, 1, 1),
    _SrdIndex_Type()
)
srdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srdIndex.setStatus("current")
_SrdRowStatus_Type = RowStatus
_SrdRowStatus_Object = MibTableColumn
srdRowStatus = _SrdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21, 1, 2),
    _SrdRowStatus_Type()
)
srdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srdRowStatus.setStatus("current")


class _SrdAction_Type(Integer32):
    """Custom type srdAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SrdAction_Type.__name__ = "Integer32"
_SrdAction_Object = MibTableColumn
srdAction = _SrdAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21, 1, 3),
    _SrdAction_Type()
)
srdAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srdAction.setStatus("current")


class _SrdActionResult_Type(Integer32):
    """Custom type srdActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SrdActionResult_Type.__name__ = "Integer32"
_SrdActionResult_Object = MibTableColumn
srdActionResult = _SrdActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21, 1, 4),
    _SrdActionResult_Type()
)
srdActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srdActionResult.setStatus("current")


class _SrdName_Type(SnmpAdminString):
    """Custom type srdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SrdName_Type.__name__ = "SnmpAdminString"
_SrdName_Object = MibTableColumn
srdName = _SrdName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21, 1, 5),
    _SrdName_Type()
)
srdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srdName.setStatus("current")


class _SrdMediaRealm_Type(SnmpAdminString):
    """Custom type srdMediaRealm based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_SrdMediaRealm_Type.__name__ = "SnmpAdminString"
_SrdMediaRealm_Object = MibTableColumn
srdMediaRealm = _SrdMediaRealm_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21, 1, 6),
    _SrdMediaRealm_Type()
)
srdMediaRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srdMediaRealm.setStatus("current")


class _SrdIntraSRDMediaAnchoring_Type(Integer32):
    """Custom type srdIntraSRDMediaAnchoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("anchorMedia", 0),
          ("dontAnchorMedia", 1))
    )


_SrdIntraSRDMediaAnchoring_Type.__name__ = "Integer32"
_SrdIntraSRDMediaAnchoring_Object = MibTableColumn
srdIntraSRDMediaAnchoring = _SrdIntraSRDMediaAnchoring_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21, 1, 7),
    _SrdIntraSRDMediaAnchoring_Type()
)
srdIntraSRDMediaAnchoring.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srdIntraSRDMediaAnchoring.setStatus("current")


class _SrdBlockUnRegUsers_Type(Integer32):
    """Custom type srdBlockUnRegUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SrdBlockUnRegUsers_Type.__name__ = "Integer32"
_SrdBlockUnRegUsers_Object = MibTableColumn
srdBlockUnRegUsers = _SrdBlockUnRegUsers_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21, 1, 8),
    _SrdBlockUnRegUsers_Type()
)
srdBlockUnRegUsers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srdBlockUnRegUsers.setStatus("current")


class _SrdMaxNumOfRegUsers_Type(Integer32):
    """Custom type srdMaxNumOfRegUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3000),
    )


_SrdMaxNumOfRegUsers_Type.__name__ = "Integer32"
_SrdMaxNumOfRegUsers_Object = MibTableColumn
srdMaxNumOfRegUsers = _SrdMaxNumOfRegUsers_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 26, 21, 1, 9),
    _SrdMaxNumOfRegUsers_Type()
)
srdMaxNumOfRegUsers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    srdMaxNumOfRegUsers.setStatus("current")
_SipInterfaceSettings_ObjectIdentity = ObjectIdentity
sipInterfaceSettings = _SipInterfaceSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27)
)
_SipInterfaceTable_Object = MibTable
sipInterfaceTable = _SipInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21)
)
if mibBuilder.loadTexts:
    sipInterfaceTable.setStatus("current")
_SipInterfaceEntry_Object = MibTableRow
sipInterfaceEntry = _SipInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1)
)
sipInterfaceEntry.setIndexNames(
    (0, "AcGateway", "sipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sipInterfaceEntry.setStatus("current")


class _SipInterfaceIndex_Type(Unsigned32):
    """Custom type sipInterfaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SipInterfaceIndex_Type.__name__ = "Unsigned32"
_SipInterfaceIndex_Object = MibTableColumn
sipInterfaceIndex = _SipInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1, 1),
    _SipInterfaceIndex_Type()
)
sipInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipInterfaceIndex.setStatus("current")
_SipInterfaceRowStatus_Type = RowStatus
_SipInterfaceRowStatus_Object = MibTableColumn
sipInterfaceRowStatus = _SipInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1, 2),
    _SipInterfaceRowStatus_Type()
)
sipInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipInterfaceRowStatus.setStatus("current")


class _SipInterfaceAction_Type(Integer32):
    """Custom type sipInterfaceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SipInterfaceAction_Type.__name__ = "Integer32"
_SipInterfaceAction_Object = MibTableColumn
sipInterfaceAction = _SipInterfaceAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1, 3),
    _SipInterfaceAction_Type()
)
sipInterfaceAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipInterfaceAction.setStatus("current")


class _SipInterfaceActionResult_Type(Integer32):
    """Custom type sipInterfaceActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SipInterfaceActionResult_Type.__name__ = "Integer32"
_SipInterfaceActionResult_Object = MibTableColumn
sipInterfaceActionResult = _SipInterfaceActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1, 4),
    _SipInterfaceActionResult_Type()
)
sipInterfaceActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipInterfaceActionResult.setStatus("current")


class _SipInterfaceNetworkInterface_Type(SnmpAdminString):
    """Custom type sipInterfaceNetworkInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SipInterfaceNetworkInterface_Type.__name__ = "SnmpAdminString"
_SipInterfaceNetworkInterface_Object = MibTableColumn
sipInterfaceNetworkInterface = _SipInterfaceNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1, 5),
    _SipInterfaceNetworkInterface_Type()
)
sipInterfaceNetworkInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipInterfaceNetworkInterface.setStatus("current")


class _SipInterfaceApplicationType_Type(Integer32):
    """Custom type sipInterfaceApplicationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gwIP2IP", 0),
          ("sas", 1),
          ("sbc", 2))
    )


_SipInterfaceApplicationType_Type.__name__ = "Integer32"
_SipInterfaceApplicationType_Object = MibTableColumn
sipInterfaceApplicationType = _SipInterfaceApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1, 6),
    _SipInterfaceApplicationType_Type()
)
sipInterfaceApplicationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipInterfaceApplicationType.setStatus("current")


class _SipInterfaceUDPPort_Type(Unsigned32):
    """Custom type sipInterfaceUDPPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_SipInterfaceUDPPort_Type.__name__ = "Unsigned32"
_SipInterfaceUDPPort_Object = MibTableColumn
sipInterfaceUDPPort = _SipInterfaceUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1, 7),
    _SipInterfaceUDPPort_Type()
)
sipInterfaceUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipInterfaceUDPPort.setStatus("current")


class _SipInterfaceTCPPort_Type(Unsigned32):
    """Custom type sipInterfaceTCPPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_SipInterfaceTCPPort_Type.__name__ = "Unsigned32"
_SipInterfaceTCPPort_Object = MibTableColumn
sipInterfaceTCPPort = _SipInterfaceTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1, 8),
    _SipInterfaceTCPPort_Type()
)
sipInterfaceTCPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipInterfaceTCPPort.setStatus("current")


class _SipInterfaceTLSPort_Type(Unsigned32):
    """Custom type sipInterfaceTLSPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_SipInterfaceTLSPort_Type.__name__ = "Unsigned32"
_SipInterfaceTLSPort_Object = MibTableColumn
sipInterfaceTLSPort = _SipInterfaceTLSPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1, 9),
    _SipInterfaceTLSPort_Type()
)
sipInterfaceTLSPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipInterfaceTLSPort.setStatus("current")


class _SipInterfaceSRD_Type(Unsigned32):
    """Custom type sipInterfaceSRD based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SipInterfaceSRD_Type.__name__ = "Unsigned32"
_SipInterfaceSRD_Object = MibTableColumn
sipInterfaceSRD = _SipInterfaceSRD_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 1, 27, 21, 1, 10),
    _SipInterfaceSRD_Type()
)
sipInterfaceSRD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipInterfaceSRD.setStatus("current")
_Sip_ObjectIdentity = ObjectIdentity
sip = _Sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2)
)
_SipProxy_ObjectIdentity = ObjectIdentity
sipProxy = _SipProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1)
)


class _SipProxyUsed_Type(Integer32):
    """Custom type sipProxyUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipProxyUsed_Type.__name__ = "Integer32"
_SipProxyUsed_Object = MibScalar
sipProxyUsed = _SipProxyUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 1),
    _SipProxyUsed_Type()
)
sipProxyUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyUsed.setStatus("current")


class _SipProxyEnableKeepAlive_Type(Integer32):
    """Custom type sipProxyEnableKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("usingOptions", 1),
          ("usingRegister", 2))
    )


_SipProxyEnableKeepAlive_Type.__name__ = "Integer32"
_SipProxyEnableKeepAlive_Object = MibScalar
sipProxyEnableKeepAlive = _SipProxyEnableKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 2),
    _SipProxyEnableKeepAlive_Type()
)
sipProxyEnableKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyEnableKeepAlive.setStatus("current")


class _SipProxyName_Type(SnmpAdminString):
    """Custom type sipProxyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SipProxyName_Type.__name__ = "SnmpAdminString"
_SipProxyName_Object = MibScalar
sipProxyName = _SipProxyName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 3),
    _SipProxyName_Type()
)
sipProxyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyName.setStatus("current")


class _SipProxyIsHotSwap_Type(Integer32):
    """Custom type sipProxyIsHotSwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipProxyIsHotSwap_Type.__name__ = "Integer32"
_SipProxyIsHotSwap_Object = MibScalar
sipProxyIsHotSwap = _SipProxyIsHotSwap_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 4),
    _SipProxyIsHotSwap_Type()
)
sipProxyIsHotSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyIsHotSwap.setStatus("current")


class _SipProxyHotSwapRtx_Type(Unsigned32):
    """Custom type sipProxyHotSwapRtx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SipProxyHotSwapRtx_Type.__name__ = "Unsigned32"
_SipProxyHotSwapRtx_Object = MibScalar
sipProxyHotSwapRtx = _SipProxyHotSwapRtx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 5),
    _SipProxyHotSwapRtx_Type()
)
sipProxyHotSwapRtx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyHotSwapRtx.setStatus("current")


class _SipProxyRedundancyMode_Type(Integer32):
    """Custom type sipProxyRedundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("homing", 1),
          ("parking", 0))
    )


_SipProxyRedundancyMode_Type.__name__ = "Integer32"
_SipProxyRedundancyMode_Object = MibScalar
sipProxyRedundancyMode = _SipProxyRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 6),
    _SipProxyRedundancyMode_Type()
)
sipProxyRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyRedundancyMode.setStatus("current")


class _SipProxyAlwaysUseRouteTable_Type(Integer32):
    """Custom type sipProxyAlwaysUseRouteTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipProxyAlwaysUseRouteTable_Type.__name__ = "Integer32"
_SipProxyAlwaysUseRouteTable_Object = MibScalar
sipProxyAlwaysUseRouteTable = _SipProxyAlwaysUseRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 7),
    _SipProxyAlwaysUseRouteTable_Type()
)
sipProxyAlwaysUseRouteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyAlwaysUseRouteTable.setStatus("current")


class _SipProxyAlwaysSendToProxy_Type(Integer32):
    """Custom type sipProxyAlwaysSendToProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipProxyAlwaysSendToProxy_Type.__name__ = "Integer32"
_SipProxyAlwaysSendToProxy_Object = MibScalar
sipProxyAlwaysSendToProxy = _SipProxyAlwaysSendToProxy_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 8),
    _SipProxyAlwaysSendToProxy_Type()
)
sipProxyAlwaysSendToProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyAlwaysSendToProxy.setStatus("current")


class _SipProxyKeepAliveTime_Type(Unsigned32):
    """Custom type sipProxyKeepAliveTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2000000),
    )


_SipProxyKeepAliveTime_Type.__name__ = "Unsigned32"
_SipProxyKeepAliveTime_Object = MibScalar
sipProxyKeepAliveTime = _SipProxyKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 9),
    _SipProxyKeepAliveTime_Type()
)
sipProxyKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyKeepAliveTime.setStatus("current")


class _SipProxyIsFallbackUsed_Type(Integer32):
    """Custom type sipProxyIsFallbackUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipProxyIsFallbackUsed_Type.__name__ = "Integer32"
_SipProxyIsFallbackUsed_Object = MibScalar
sipProxyIsFallbackUsed = _SipProxyIsFallbackUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 10),
    _SipProxyIsFallbackUsed_Type()
)
sipProxyIsFallbackUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyIsFallbackUsed.setStatus("current")


class _SipProxySendInviteToProxy_Type(Integer32):
    """Custom type sipProxySendInviteToProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipProxySendInviteToProxy_Type.__name__ = "Integer32"
_SipProxySendInviteToProxy_Object = MibScalar
sipProxySendInviteToProxy = _SipProxySendInviteToProxy_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 11),
    _SipProxySendInviteToProxy_Type()
)
sipProxySendInviteToProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxySendInviteToProxy.setStatus("current")


class _SipProxyIsTrustedProxy_Type(Integer32):
    """Custom type sipProxyIsTrustedProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipProxyIsTrustedProxy_Type.__name__ = "Integer32"
_SipProxyIsTrustedProxy_Object = MibScalar
sipProxyIsTrustedProxy = _SipProxyIsTrustedProxy_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 12),
    _SipProxyIsTrustedProxy_Type()
)
sipProxyIsTrustedProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyIsTrustedProxy.setStatus("current")


class _SipProxyUseGatewayNameForOptions_Type(Integer32):
    """Custom type sipProxyUseGatewayNameForOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipProxyUseGatewayNameForOptions_Type.__name__ = "Integer32"
_SipProxyUseGatewayNameForOptions_Object = MibScalar
sipProxyUseGatewayNameForOptions = _SipProxyUseGatewayNameForOptions_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 13),
    _SipProxyUseGatewayNameForOptions_Type()
)
sipProxyUseGatewayNameForOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyUseGatewayNameForOptions.setStatus("current")


class _SipProxyEnableSRVQuery_Type(Integer32):
    """Custom type sipProxyEnableSRVQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipProxyEnableSRVQuery_Type.__name__ = "Integer32"
_SipProxyEnableSRVQuery_Object = MibScalar
sipProxyEnableSRVQuery = _SipProxyEnableSRVQuery_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 14),
    _SipProxyEnableSRVQuery_Type()
)
sipProxyEnableSRVQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyEnableSRVQuery.setStatus("obsolete")


class _SipProxyDNSQueryType_Type(Integer32):
    """Custom type sipProxyDNSQueryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aRecord", 0),
          ("nAPTR", 2),
          ("sRV", 1))
    )


_SipProxyDNSQueryType_Type.__name__ = "Integer32"
_SipProxyDNSQueryType_Object = MibScalar
sipProxyDNSQueryType = _SipProxyDNSQueryType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 15),
    _SipProxyDNSQueryType_Type()
)
sipProxyDNSQueryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyDNSQueryType.setStatus("current")


class _SipProxyLoadBalancingMethod_Type(Integer32):
    """Custom type sipProxyLoadBalancingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("randomWeights", 2),
          ("roundRobin", 1))
    )


_SipProxyLoadBalancingMethod_Type.__name__ = "Integer32"
_SipProxyLoadBalancingMethod_Object = MibScalar
sipProxyLoadBalancingMethod = _SipProxyLoadBalancingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 16),
    _SipProxyLoadBalancingMethod_Type()
)
sipProxyLoadBalancingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyLoadBalancingMethod.setStatus("current")


class _SipProxyIPListRefreshTime_Type(Unsigned32):
    """Custom type sipProxyIPListRefreshTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2000000),
    )


_SipProxyIPListRefreshTime_Type.__name__ = "Unsigned32"
_SipProxyIPListRefreshTime_Object = MibScalar
sipProxyIPListRefreshTime = _SipProxyIPListRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 17),
    _SipProxyIPListRefreshTime_Type()
)
sipProxyIPListRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxyIPListRefreshTime.setStatus("current")
_ProxyIPTable_Object = MibTable
proxyIPTable = _ProxyIPTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 21)
)
if mibBuilder.loadTexts:
    proxyIPTable.setStatus("current")
_ProxyIPEntry_Object = MibTableRow
proxyIPEntry = _ProxyIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 21, 1)
)
proxyIPEntry.setIndexNames(
    (0, "AcGateway", "proxyIPIndex"),
)
if mibBuilder.loadTexts:
    proxyIPEntry.setStatus("current")


class _ProxyIPIndex_Type(Unsigned32):
    """Custom type proxyIPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ProxyIPIndex_Type.__name__ = "Unsigned32"
_ProxyIPIndex_Object = MibTableColumn
proxyIPIndex = _ProxyIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 21, 1, 1),
    _ProxyIPIndex_Type()
)
proxyIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyIPIndex.setStatus("current")
_ProxyIPRowStatus_Type = RowStatus
_ProxyIPRowStatus_Object = MibTableColumn
proxyIPRowStatus = _ProxyIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 21, 1, 2),
    _ProxyIPRowStatus_Type()
)
proxyIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    proxyIPRowStatus.setStatus("current")


class _ProxyIPAction_Type(Integer32):
    """Custom type proxyIPAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ProxyIPAction_Type.__name__ = "Integer32"
_ProxyIPAction_Object = MibTableColumn
proxyIPAction = _ProxyIPAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 21, 1, 3),
    _ProxyIPAction_Type()
)
proxyIPAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyIPAction.setStatus("current")


class _ProxyIPActionResult_Type(Integer32):
    """Custom type proxyIPActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_ProxyIPActionResult_Type.__name__ = "Integer32"
_ProxyIPActionResult_Object = MibTableColumn
proxyIPActionResult = _ProxyIPActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 21, 1, 4),
    _ProxyIPActionResult_Type()
)
proxyIPActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyIPActionResult.setStatus("current")


class _ProxyIPProxyIP_Type(SnmpAdminString):
    """Custom type proxyIPProxyIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_ProxyIPProxyIP_Type.__name__ = "SnmpAdminString"
_ProxyIPProxyIP_Object = MibTableColumn
proxyIPProxyIP = _ProxyIPProxyIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 21, 1, 5),
    _ProxyIPProxyIP_Type()
)
proxyIPProxyIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    proxyIPProxyIP.setStatus("current")
_SipProxySetTable_Object = MibTable
sipProxySetTable = _SipProxySetTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 22)
)
if mibBuilder.loadTexts:
    sipProxySetTable.setStatus("current")
_SipProxySetEntry_Object = MibTableRow
sipProxySetEntry = _SipProxySetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 22, 1)
)
sipProxySetEntry.setIndexNames(
    (0, "AcGateway", "sipProxySetIndex"),
)
if mibBuilder.loadTexts:
    sipProxySetEntry.setStatus("current")


class _SipProxySetIndex_Type(Unsigned32):
    """Custom type sipProxySetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SipProxySetIndex_Type.__name__ = "Unsigned32"
_SipProxySetIndex_Object = MibTableColumn
sipProxySetIndex = _SipProxySetIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 22, 1, 1),
    _SipProxySetIndex_Type()
)
sipProxySetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipProxySetIndex.setStatus("current")
_SipProxySetRowStatus_Type = RowStatus
_SipProxySetRowStatus_Object = MibTableColumn
sipProxySetRowStatus = _SipProxySetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 22, 1, 2),
    _SipProxySetRowStatus_Type()
)
sipProxySetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProxySetRowStatus.setStatus("current")


class _SipProxySetAction_Type(Integer32):
    """Custom type sipProxySetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SipProxySetAction_Type.__name__ = "Integer32"
_SipProxySetAction_Object = MibTableColumn
sipProxySetAction = _SipProxySetAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 22, 1, 3),
    _SipProxySetAction_Type()
)
sipProxySetAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipProxySetAction.setStatus("current")


class _SipProxySetActionResult_Type(Integer32):
    """Custom type sipProxySetActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SipProxySetActionResult_Type.__name__ = "Integer32"
_SipProxySetActionResult_Object = MibTableColumn
sipProxySetActionResult = _SipProxySetActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 22, 1, 4),
    _SipProxySetActionResult_Type()
)
sipProxySetActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipProxySetActionResult.setStatus("current")


class _SipProxySetEnableProxyKeepAlive_Type(Integer32):
    """Custom type sipProxySetEnableProxyKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("usingOptions", 1),
          ("usingRegister", 2))
    )


_SipProxySetEnableProxyKeepAlive_Type.__name__ = "Integer32"
_SipProxySetEnableProxyKeepAlive_Object = MibTableColumn
sipProxySetEnableProxyKeepAlive = _SipProxySetEnableProxyKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 22, 1, 5),
    _SipProxySetEnableProxyKeepAlive_Type()
)
sipProxySetEnableProxyKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProxySetEnableProxyKeepAlive.setStatus("current")


class _SipProxySetProxyKeepAliveTime_Type(Unsigned32):
    """Custom type sipProxySetProxyKeepAliveTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2000000),
    )


_SipProxySetProxyKeepAliveTime_Type.__name__ = "Unsigned32"
_SipProxySetProxyKeepAliveTime_Object = MibTableColumn
sipProxySetProxyKeepAliveTime = _SipProxySetProxyKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 22, 1, 6),
    _SipProxySetProxyKeepAliveTime_Type()
)
sipProxySetProxyKeepAliveTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProxySetProxyKeepAliveTime.setStatus("current")


class _SipProxySetProxyLoadBalancingMethod_Type(Integer32):
    """Custom type sipProxySetProxyLoadBalancingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("randomWeights", 2),
          ("roundRobin", 1))
    )


_SipProxySetProxyLoadBalancingMethod_Type.__name__ = "Integer32"
_SipProxySetProxyLoadBalancingMethod_Object = MibTableColumn
sipProxySetProxyLoadBalancingMethod = _SipProxySetProxyLoadBalancingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 22, 1, 7),
    _SipProxySetProxyLoadBalancingMethod_Type()
)
sipProxySetProxyLoadBalancingMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProxySetProxyLoadBalancingMethod.setStatus("current")


class _SipProxySetIsProxyHotSwap_Type(Integer32):
    """Custom type sipProxySetIsProxyHotSwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipProxySetIsProxyHotSwap_Type.__name__ = "Integer32"
_SipProxySetIsProxyHotSwap_Object = MibTableColumn
sipProxySetIsProxyHotSwap = _SipProxySetIsProxyHotSwap_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 1, 22, 1, 8),
    _SipProxySetIsProxyHotSwap_Type()
)
sipProxySetIsProxyHotSwap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProxySetIsProxyHotSwap.setStatus("current")
_SipDTMF_ObjectIdentity = ObjectIdentity
sipDTMF = _SipDTMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2)
)


class _SipDTMFIsHookFlashUsed_Type(Integer32):
    """Custom type sipDTMFIsHookFlashUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipDTMFIsHookFlashUsed_Type.__name__ = "Integer32"
_SipDTMFIsHookFlashUsed_Object = MibScalar
sipDTMFIsHookFlashUsed = _SipDTMFIsHookFlashUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 1),
    _SipDTMFIsHookFlashUsed_Type()
)
sipDTMFIsHookFlashUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDTMFIsHookFlashUsed.setStatus("obsolete")


class _SipDTMFIsDTMFUsed_Type(Integer32):
    """Custom type sipDTMFIsDTMFUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipDTMFIsDTMFUsed_Type.__name__ = "Integer32"
_SipDTMFIsDTMFUsed_Object = MibScalar
sipDTMFIsDTMFUsed = _SipDTMFIsDTMFUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 2),
    _SipDTMFIsDTMFUsed_Type()
)
sipDTMFIsDTMFUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDTMFIsDTMFUsed.setStatus("obsolete")


class _SipDTMFOutOfBandDtmfFormat_Type(Integer32):
    """Custom type sipDTMFOutOfBandDtmfFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("info-Cisco", 2),
          ("info-Nortel", 1),
          ("notify", 3))
    )


_SipDTMFOutOfBandDtmfFormat_Type.__name__ = "Integer32"
_SipDTMFOutOfBandDtmfFormat_Object = MibScalar
sipDTMFOutOfBandDtmfFormat = _SipDTMFOutOfBandDtmfFormat_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 3),
    _SipDTMFOutOfBandDtmfFormat_Type()
)
sipDTMFOutOfBandDtmfFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDTMFOutOfBandDtmfFormat.setStatus("obsolete")


class _SipDTMFDisableAutoMute_Type(Integer32):
    """Custom type sipDTMFDisableAutoMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipDTMFDisableAutoMute_Type.__name__ = "Integer32"
_SipDTMFDisableAutoMute_Object = MibScalar
sipDTMFDisableAutoMute = _SipDTMFDisableAutoMute_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 4),
    _SipDTMFDisableAutoMute_Type()
)
sipDTMFDisableAutoMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDTMFDisableAutoMute.setStatus("current")


class _SipDTMFRxDTMFOption_Type(Integer32):
    """Custom type sipDTMFRxDTMFOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noSupportRFC2833inSDP", 0),
          ("supportRFC2833inSDP", 3))
    )


_SipDTMFRxDTMFOption_Type.__name__ = "Integer32"
_SipDTMFRxDTMFOption_Object = MibScalar
sipDTMFRxDTMFOption = _SipDTMFRxDTMFOption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 5),
    _SipDTMFRxDTMFOption_Type()
)
sipDTMFRxDTMFOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDTMFRxDTMFOption.setStatus("current")


class _SipDTMFHookFlashOption_Type(Integer32):
    """Custom type sipDTMFHookFlashOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("iNFO", 1),
          ("infoLucent", 5),
          ("notSupported", 0),
          ("rFC2833", 4))
    )


_SipDTMFHookFlashOption_Type.__name__ = "Integer32"
_SipDTMFHookFlashOption_Object = MibScalar
sipDTMFHookFlashOption = _SipDTMFHookFlashOption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 6),
    _SipDTMFHookFlashOption_Type()
)
sipDTMFHookFlashOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDTMFHookFlashOption.setStatus("current")


class _SipDTMFUseDigitForSpecialDTMF_Type(Integer32):
    """Custom type sipDTMFUseDigitForSpecialDTMF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("numeric", 1),
          ("special", 0))
    )


_SipDTMFUseDigitForSpecialDTMF_Type.__name__ = "Integer32"
_SipDTMFUseDigitForSpecialDTMF_Object = MibScalar
sipDTMFUseDigitForSpecialDTMF = _SipDTMFUseDigitForSpecialDTMF_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 7),
    _SipDTMFUseDigitForSpecialDTMF_Type()
)
sipDTMFUseDigitForSpecialDTMF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDTMFUseDigitForSpecialDTMF.setStatus("current")


class _SipDTMFMinRoutingOverlapDigits_Type(Unsigned32):
    """Custom type sipDTMFMinRoutingOverlapDigits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_SipDTMFMinRoutingOverlapDigits_Type.__name__ = "Unsigned32"
_SipDTMFMinRoutingOverlapDigits_Object = MibScalar
sipDTMFMinRoutingOverlapDigits = _SipDTMFMinRoutingOverlapDigits_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 8),
    _SipDTMFMinRoutingOverlapDigits_Type()
)
sipDTMFMinRoutingOverlapDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDTMFMinRoutingOverlapDigits.setStatus("current")


class _SipDTMFISDNOverlapIPtoTelDialing_Type(Integer32):
    """Custom type sipDTMFISDNOverlapIPtoTelDialing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipDTMFISDNOverlapIPtoTelDialing_Type.__name__ = "Integer32"
_SipDTMFISDNOverlapIPtoTelDialing_Object = MibScalar
sipDTMFISDNOverlapIPtoTelDialing = _SipDTMFISDNOverlapIPtoTelDialing_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 9),
    _SipDTMFISDNOverlapIPtoTelDialing_Type()
)
sipDTMFISDNOverlapIPtoTelDialing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDTMFISDNOverlapIPtoTelDialing.setStatus("current")
_SipTxDTMFOptionTable_Object = MibTable
sipTxDTMFOptionTable = _SipTxDTMFOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 21)
)
if mibBuilder.loadTexts:
    sipTxDTMFOptionTable.setStatus("current")
_SipTxDTMFOptionEntry_Object = MibTableRow
sipTxDTMFOptionEntry = _SipTxDTMFOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 21, 1)
)
sipTxDTMFOptionEntry.setIndexNames(
    (0, "AcGateway", "sipTxDTMFOptionIndex"),
)
if mibBuilder.loadTexts:
    sipTxDTMFOptionEntry.setStatus("current")


class _SipTxDTMFOptionIndex_Type(Unsigned32):
    """Custom type sipTxDTMFOptionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SipTxDTMFOptionIndex_Type.__name__ = "Unsigned32"
_SipTxDTMFOptionIndex_Object = MibTableColumn
sipTxDTMFOptionIndex = _SipTxDTMFOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 21, 1, 1),
    _SipTxDTMFOptionIndex_Type()
)
sipTxDTMFOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipTxDTMFOptionIndex.setStatus("current")
_SipTxDTMFOptionRowStatus_Type = RowStatus
_SipTxDTMFOptionRowStatus_Object = MibTableColumn
sipTxDTMFOptionRowStatus = _SipTxDTMFOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 21, 1, 2),
    _SipTxDTMFOptionRowStatus_Type()
)
sipTxDTMFOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipTxDTMFOptionRowStatus.setStatus("current")


class _SipTxDTMFOptionAction_Type(Integer32):
    """Custom type sipTxDTMFOptionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SipTxDTMFOptionAction_Type.__name__ = "Integer32"
_SipTxDTMFOptionAction_Object = MibTableColumn
sipTxDTMFOptionAction = _SipTxDTMFOptionAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 21, 1, 3),
    _SipTxDTMFOptionAction_Type()
)
sipTxDTMFOptionAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTxDTMFOptionAction.setStatus("current")


class _SipTxDTMFOptionActionResult_Type(Integer32):
    """Custom type sipTxDTMFOptionActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SipTxDTMFOptionActionResult_Type.__name__ = "Integer32"
_SipTxDTMFOptionActionResult_Object = MibTableColumn
sipTxDTMFOptionActionResult = _SipTxDTMFOptionActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 21, 1, 4),
    _SipTxDTMFOptionActionResult_Type()
)
sipTxDTMFOptionActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipTxDTMFOptionActionResult.setStatus("current")


class _SipTxDTMFOptionValue_Type(Integer32):
    """Custom type sipTxDTMFOptionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ciscoINFO", 3),
          ("koreaTelecomINFO", 5),
          ("nOTIFY", 2),
          ("nortelINFO", 1),
          ("notSupported", 0),
          ("rFC2833", 4))
    )


_SipTxDTMFOptionValue_Type.__name__ = "Integer32"
_SipTxDTMFOptionValue_Object = MibTableColumn
sipTxDTMFOptionValue = _SipTxDTMFOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 2, 21, 1, 5),
    _SipTxDTMFOptionValue_Type()
)
sipTxDTMFOptionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipTxDTMFOptionValue.setStatus("current")
_SipPorts_ObjectIdentity = ObjectIdentity
sipPorts = _SipPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 3)
)


class _SipPortsDestinationPort_Type(Unsigned32):
    """Custom type sipPortsDestinationPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_SipPortsDestinationPort_Type.__name__ = "Unsigned32"
_SipPortsDestinationPort_Object = MibScalar
sipPortsDestinationPort = _SipPortsDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 3, 1),
    _SipPortsDestinationPort_Type()
)
sipPortsDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipPortsDestinationPort.setStatus("current")


class _SipPortsLocalSipPort_Type(Unsigned32):
    """Custom type sipPortsLocalSipPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_SipPortsLocalSipPort_Type.__name__ = "Unsigned32"
_SipPortsLocalSipPort_Object = MibScalar
sipPortsLocalSipPort = _SipPortsLocalSipPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 3, 2),
    _SipPortsLocalSipPort_Type()
)
sipPortsLocalSipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipPortsLocalSipPort.setStatus("current")


class _SipPortsTCPLocalSipPort_Type(Unsigned32):
    """Custom type sipPortsTCPLocalSipPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SipPortsTCPLocalSipPort_Type.__name__ = "Unsigned32"
_SipPortsTCPLocalSipPort_Object = MibScalar
sipPortsTCPLocalSipPort = _SipPortsTCPLocalSipPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 3, 3),
    _SipPortsTCPLocalSipPort_Type()
)
sipPortsTCPLocalSipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipPortsTCPLocalSipPort.setStatus("current")


class _SipPortsTLSLocalSipPort_Type(Unsigned32):
    """Custom type sipPortsTLSLocalSipPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SipPortsTLSLocalSipPort_Type.__name__ = "Unsigned32"
_SipPortsTLSLocalSipPort_Object = MibScalar
sipPortsTLSLocalSipPort = _SipPortsTLSLocalSipPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 3, 4),
    _SipPortsTLSLocalSipPort_Type()
)
sipPortsTLSLocalSipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipPortsTLSLocalSipPort.setStatus("current")
_SipAuth_ObjectIdentity = ObjectIdentity
sipAuth = _SipAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4)
)


class _SipAuthMode_Type(Integer32):
    """Custom type sipAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("perEP", 0),
          ("perFXSOnly", 3),
          ("perGW", 1))
    )


_SipAuthMode_Type.__name__ = "Integer32"
_SipAuthMode_Object = MibScalar
sipAuthMode = _SipAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 1),
    _SipAuthMode_Type()
)
sipAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipAuthMode.setStatus("current")


class _SipAuthUserName_Type(SnmpAdminString):
    """Custom type sipAuthUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SipAuthUserName_Type.__name__ = "SnmpAdminString"
_SipAuthUserName_Object = MibScalar
sipAuthUserName = _SipAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 2),
    _SipAuthUserName_Type()
)
sipAuthUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipAuthUserName.setStatus("current")


class _SipAuthPassword_Type(SnmpAdminString):
    """Custom type sipAuthPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SipAuthPassword_Type.__name__ = "SnmpAdminString"
_SipAuthPassword_Object = MibScalar
sipAuthPassword = _SipAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 3),
    _SipAuthPassword_Type()
)
sipAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipAuthPassword.setStatus("current")


class _SipAuthCnonce_Type(SnmpAdminString):
    """Custom type sipAuthCnonce based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SipAuthCnonce_Type.__name__ = "SnmpAdminString"
_SipAuthCnonce_Object = MibScalar
sipAuthCnonce = _SipAuthCnonce_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 4),
    _SipAuthCnonce_Type()
)
sipAuthCnonce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipAuthCnonce.setStatus("current")


class _SipAuthMutualAuthenticationMode_Type(Integer32):
    """Custom type sipAuthMutualAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mandatory", 1),
          ("optional", 0))
    )


_SipAuthMutualAuthenticationMode_Type.__name__ = "Integer32"
_SipAuthMutualAuthenticationMode_Object = MibScalar
sipAuthMutualAuthenticationMode = _SipAuthMutualAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 5),
    _SipAuthMutualAuthenticationMode_Type()
)
sipAuthMutualAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipAuthMutualAuthenticationMode.setStatus("current")


class _SipAuthChallengeCachingMode_Type(Integer32):
    """Custom type sipAuthChallengeCachingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullCaching", 2),
          ("inviteOnly", 1),
          ("noCaching", 0))
    )


_SipAuthChallengeCachingMode_Type.__name__ = "Integer32"
_SipAuthChallengeCachingMode_Object = MibScalar
sipAuthChallengeCachingMode = _SipAuthChallengeCachingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 6),
    _SipAuthChallengeCachingMode_Type()
)
sipAuthChallengeCachingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipAuthChallengeCachingMode.setStatus("current")
_AuthTable_Object = MibTable
authTable = _AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 21)
)
if mibBuilder.loadTexts:
    authTable.setStatus("current")
_AuthEntry_Object = MibTableRow
authEntry = _AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 21, 1)
)
authEntry.setIndexNames(
    (0, "AcGateway", "authIndex"),
)
if mibBuilder.loadTexts:
    authEntry.setStatus("current")


class _AuthIndex_Type(Unsigned32):
    """Custom type authIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AuthIndex_Type.__name__ = "Unsigned32"
_AuthIndex_Object = MibTableColumn
authIndex = _AuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 21, 1, 1),
    _AuthIndex_Type()
)
authIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authIndex.setStatus("current")


class _AuthIsUsed_Type(Integer32):
    """Custom type authIsUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AuthIsUsed_Type.__name__ = "Integer32"
_AuthIsUsed_Object = MibTableColumn
authIsUsed = _AuthIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 21, 1, 2),
    _AuthIsUsed_Type()
)
authIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authIsUsed.setStatus("current")


class _AuthAction_Type(Integer32):
    """Custom type authAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_AuthAction_Type.__name__ = "Integer32"
_AuthAction_Object = MibTableColumn
authAction = _AuthAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 21, 1, 3),
    _AuthAction_Type()
)
authAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authAction.setStatus("current")


class _AuthActionResult_Type(Integer32):
    """Custom type authActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_AuthActionResult_Type.__name__ = "Integer32"
_AuthActionResult_Object = MibTableColumn
authActionResult = _AuthActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 21, 1, 4),
    _AuthActionResult_Type()
)
authActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authActionResult.setStatus("current")


class _AuthUserID_Type(SnmpAdminString):
    """Custom type authUserID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AuthUserID_Type.__name__ = "SnmpAdminString"
_AuthUserID_Object = MibTableColumn
authUserID = _AuthUserID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 21, 1, 5),
    _AuthUserID_Type()
)
authUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserID.setStatus("current")


class _AuthUserPassword_Type(SnmpAdminString):
    """Custom type authUserPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AuthUserPassword_Type.__name__ = "SnmpAdminString"
_AuthUserPassword_Object = MibTableColumn
authUserPassword = _AuthUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 21, 1, 6),
    _AuthUserPassword_Type()
)
authUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authUserPassword.setStatus("current")


class _AuthModule_Type(Unsigned32):
    """Custom type authModule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AuthModule_Type.__name__ = "Unsigned32"
_AuthModule_Object = MibTableColumn
authModule = _AuthModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 21, 1, 7),
    _AuthModule_Type()
)
authModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authModule.setStatus("current")


class _AuthPort_Type(Unsigned32):
    """Custom type authPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AuthPort_Type.__name__ = "Unsigned32"
_AuthPort_Object = MibTableColumn
authPort = _AuthPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 4, 21, 1, 8),
    _AuthPort_Type()
)
authPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authPort.setStatus("current")
_SipRetransmission_ObjectIdentity = ObjectIdentity
sipRetransmission = _SipRetransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 5)
)


class _SipRetransmissionT1Rtx_Type(Unsigned32):
    """Custom type sipRetransmissionT1Rtx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4000),
    )


_SipRetransmissionT1Rtx_Type.__name__ = "Unsigned32"
_SipRetransmissionT1Rtx_Object = MibScalar
sipRetransmissionT1Rtx = _SipRetransmissionT1Rtx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 5, 1),
    _SipRetransmissionT1Rtx_Type()
)
sipRetransmissionT1Rtx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRetransmissionT1Rtx.setStatus("current")


class _SipRetransmissionT2Rtx_Type(Unsigned32):
    """Custom type sipRetransmissionT2Rtx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_SipRetransmissionT2Rtx_Type.__name__ = "Unsigned32"
_SipRetransmissionT2Rtx_Object = MibScalar
sipRetransmissionT2Rtx = _SipRetransmissionT2Rtx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 5, 2),
    _SipRetransmissionT2Rtx_Type()
)
sipRetransmissionT2Rtx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRetransmissionT2Rtx.setStatus("current")


class _SipRetransmissionSipMaxRtx_Type(Unsigned32):
    """Custom type sipRetransmissionSipMaxRtx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SipRetransmissionSipMaxRtx_Type.__name__ = "Unsigned32"
_SipRetransmissionSipMaxRtx_Object = MibScalar
sipRetransmissionSipMaxRtx = _SipRetransmissionSipMaxRtx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 5, 3),
    _SipRetransmissionSipMaxRtx_Type()
)
sipRetransmissionSipMaxRtx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRetransmissionSipMaxRtx.setStatus("current")


class _SipRetransmissionIsRtxEnable_Type(Integer32):
    """Custom type sipRetransmissionIsRtxEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipRetransmissionIsRtxEnable_Type.__name__ = "Integer32"
_SipRetransmissionIsRtxEnable_Object = MibScalar
sipRetransmissionIsRtxEnable = _SipRetransmissionIsRtxEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 5, 4),
    _SipRetransmissionIsRtxEnable_Type()
)
sipRetransmissionIsRtxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRetransmissionIsRtxEnable.setStatus("current")


class _SipRetransmissionEnablePTime_Type(Integer32):
    """Custom type sipRetransmissionEnablePTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipRetransmissionEnablePTime_Type.__name__ = "Integer32"
_SipRetransmissionEnablePTime_Object = MibScalar
sipRetransmissionEnablePTime = _SipRetransmissionEnablePTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 5, 5),
    _SipRetransmissionEnablePTime_Type()
)
sipRetransmissionEnablePTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRetransmissionEnablePTime.setStatus("current")


class _SipRetransmissionTCPTimeout_Type(Unsigned32):
    """Custom type sipRetransmissionTCPTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SipRetransmissionTCPTimeout_Type.__name__ = "Unsigned32"
_SipRetransmissionTCPTimeout_Object = MibScalar
sipRetransmissionTCPTimeout = _SipRetransmissionTCPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 5, 6),
    _SipRetransmissionTCPTimeout_Type()
)
sipRetransmissionTCPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRetransmissionTCPTimeout.setStatus("current")


class _SipRetransmissionRetryAfterTime_Type(Unsigned32):
    """Custom type sipRetransmissionRetryAfterTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SipRetransmissionRetryAfterTime_Type.__name__ = "Unsigned32"
_SipRetransmissionRetryAfterTime_Object = MibScalar
sipRetransmissionRetryAfterTime = _SipRetransmissionRetryAfterTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 5, 7),
    _SipRetransmissionRetryAfterTime_Type()
)
sipRetransmissionRetryAfterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRetransmissionRetryAfterTime.setStatus("current")
_SipRegistration_ObjectIdentity = ObjectIdentity
sipRegistration = _SipRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6)
)


class _SipRegistrationIsNeeded_Type(Integer32):
    """Custom type sipRegistrationIsNeeded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipRegistrationIsNeeded_Type.__name__ = "Integer32"
_SipRegistrationIsNeeded_Object = MibScalar
sipRegistrationIsNeeded = _SipRegistrationIsNeeded_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 1),
    _SipRegistrationIsNeeded_Type()
)
sipRegistrationIsNeeded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationIsNeeded.setStatus("current")


class _SipRegistrationIP_Type(SnmpAdminString):
    """Custom type sipRegistrationIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SipRegistrationIP_Type.__name__ = "SnmpAdminString"
_SipRegistrationIP_Object = MibScalar
sipRegistrationIP = _SipRegistrationIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 2),
    _SipRegistrationIP_Type()
)
sipRegistrationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationIP.setStatus("current")


class _SipRegistrationTime_Type(Unsigned32):
    """Custom type sipRegistrationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000000),
    )


_SipRegistrationTime_Type.__name__ = "Unsigned32"
_SipRegistrationTime_Object = MibScalar
sipRegistrationTime = _SipRegistrationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 3),
    _SipRegistrationTime_Type()
)
sipRegistrationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationTime.setStatus("current")


class _SipRegistrationRegistrationRetryTime_Type(Unsigned32):
    """Custom type sipRegistrationRegistrationRetryTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000000),
    )


_SipRegistrationRegistrationRetryTime_Type.__name__ = "Unsigned32"
_SipRegistrationRegistrationRetryTime_Object = MibScalar
sipRegistrationRegistrationRetryTime = _SipRegistrationRegistrationRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 4),
    _SipRegistrationRegistrationRetryTime_Type()
)
sipRegistrationRegistrationRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationRegistrationRetryTime.setStatus("current")


class _SipRegistrationRegistrarName_Type(SnmpAdminString):
    """Custom type sipRegistrationRegistrarName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SipRegistrationRegistrarName_Type.__name__ = "SnmpAdminString"
_SipRegistrationRegistrarName_Object = MibScalar
sipRegistrationRegistrarName = _SipRegistrationRegistrarName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 5),
    _SipRegistrationRegistrarName_Type()
)
sipRegistrationRegistrarName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationRegistrarName.setStatus("current")


class _SipRegistrationTimeDivider_Type(Unsigned32):
    """Custom type sipRegistrationTimeDivider based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 100),
    )


_SipRegistrationTimeDivider_Type.__name__ = "Unsigned32"
_SipRegistrationTimeDivider_Object = MibScalar
sipRegistrationTimeDivider = _SipRegistrationTimeDivider_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 6),
    _SipRegistrationTimeDivider_Type()
)
sipRegistrationTimeDivider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationTimeDivider.setStatus("current")


class _SipRegistrationName_Type(SnmpAdminString):
    """Custom type sipRegistrationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SipRegistrationName_Type.__name__ = "SnmpAdminString"
_SipRegistrationName_Object = MibScalar
sipRegistrationName = _SipRegistrationName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 7),
    _SipRegistrationName_Type()
)
sipRegistrationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationName.setStatus("current")


class _SipRegistrationRegisterOnInviteFailure_Type(Integer32):
    """Custom type sipRegistrationRegisterOnInviteFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipRegistrationRegisterOnInviteFailure_Type.__name__ = "Integer32"
_SipRegistrationRegisterOnInviteFailure_Object = MibScalar
sipRegistrationRegisterOnInviteFailure = _SipRegistrationRegisterOnInviteFailure_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 8),
    _SipRegistrationRegisterOnInviteFailure_Type()
)
sipRegistrationRegisterOnInviteFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationRegisterOnInviteFailure.setStatus("current")


class _SipRegistrationTimeThreshold_Type(Unsigned32):
    """Custom type sipRegistrationTimeThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_SipRegistrationTimeThreshold_Type.__name__ = "Unsigned32"
_SipRegistrationTimeThreshold_Object = MibScalar
sipRegistrationTimeThreshold = _SipRegistrationTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 9),
    _SipRegistrationTimeThreshold_Type()
)
sipRegistrationTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationTimeThreshold.setStatus("current")


class _SipRegistrationRegistrarTransportType_Type(Integer32):
    """Custom type sipRegistrationRegistrarTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", -1),
          ("tCP", 1),
          ("tLS", 2),
          ("uDP", 0))
    )


_SipRegistrationRegistrarTransportType_Type.__name__ = "Integer32"
_SipRegistrationRegistrarTransportType_Object = MibScalar
sipRegistrationRegistrarTransportType = _SipRegistrationRegistrarTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 10),
    _SipRegistrationRegistrarTransportType_Type()
)
sipRegistrationRegistrarTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationRegistrarTransportType.setStatus("current")


class _SipRegistrationReRegisterOnConnectionFailure_Type(Integer32):
    """Custom type sipRegistrationReRegisterOnConnectionFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipRegistrationReRegisterOnConnectionFailure_Type.__name__ = "Integer32"
_SipRegistrationReRegisterOnConnectionFailure_Object = MibScalar
sipRegistrationReRegisterOnConnectionFailure = _SipRegistrationReRegisterOnConnectionFailure_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 6, 11),
    _SipRegistrationReRegisterOnConnectionFailure_Type()
)
sipRegistrationReRegisterOnConnectionFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistrationReRegisterOnConnectionFailure.setStatus("current")
_SipMisc_ObjectIdentity = ObjectIdentity
sipMisc = _SipMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7)
)


class _SipMiscEnableEarlyMedia_Type(Integer32):
    """Custom type sipMiscEnableEarlyMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipMiscEnableEarlyMedia_Type.__name__ = "Integer32"
_SipMiscEnableEarlyMedia_Object = MibScalar
sipMiscEnableEarlyMedia = _SipMiscEnableEarlyMedia_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 1),
    _SipMiscEnableEarlyMedia_Type()
)
sipMiscEnableEarlyMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableEarlyMedia.setStatus("current")


class _SipMiscSipSessionExpires_Type(Unsigned32):
    """Custom type sipMiscSipSessionExpires based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999999),
    )


_SipMiscSipSessionExpires_Type.__name__ = "Unsigned32"
_SipMiscSipSessionExpires_Object = MibScalar
sipMiscSipSessionExpires = _SipMiscSipSessionExpires_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 2),
    _SipMiscSipSessionExpires_Type()
)
sipMiscSipSessionExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscSipSessionExpires.setStatus("current")


class _SipMiscIsUserPhone_Type(Integer32):
    """Custom type sipMiscIsUserPhone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipMiscIsUserPhone_Type.__name__ = "Integer32"
_SipMiscIsUserPhone_Object = MibScalar
sipMiscIsUserPhone = _SipMiscIsUserPhone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 3),
    _SipMiscIsUserPhone_Type()
)
sipMiscIsUserPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscIsUserPhone.setStatus("current")


class _SipMiscGatewayName_Type(SnmpAdminString):
    """Custom type sipMiscGatewayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SipMiscGatewayName_Type.__name__ = "SnmpAdminString"
_SipMiscGatewayName_Object = MibScalar
sipMiscGatewayName = _SipMiscGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 4),
    _SipMiscGatewayName_Type()
)
sipMiscGatewayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscGatewayName.setStatus("current")


class _SipMiscPrackMode_Type(Integer32):
    """Custom type sipMiscPrackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("required", 2),
          ("supported", 1))
    )


_SipMiscPrackMode_Type.__name__ = "Integer32"
_SipMiscPrackMode_Object = MibScalar
sipMiscPrackMode = _SipMiscPrackMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 5),
    _SipMiscPrackMode_Type()
)
sipMiscPrackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscPrackMode.setStatus("current")


class _SipMiscEnableRpiHeader_Type(Integer32):
    """Custom type sipMiscEnableRpiHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipMiscEnableRpiHeader_Type.__name__ = "Integer32"
_SipMiscEnableRpiHeader_Object = MibScalar
sipMiscEnableRpiHeader = _SipMiscEnableRpiHeader_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 6),
    _SipMiscEnableRpiHeader_Type()
)
sipMiscEnableRpiHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableRpiHeader.setStatus("current")


class _SipMiscXChannelHeader_Type(Integer32):
    """Custom type sipMiscXChannelHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscXChannelHeader_Type.__name__ = "Integer32"
_SipMiscXChannelHeader_Object = MibScalar
sipMiscXChannelHeader = _SipMiscXChannelHeader_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 7),
    _SipMiscXChannelHeader_Type()
)
sipMiscXChannelHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscXChannelHeader.setStatus("current")


class _SipMiscAssertedIDMode_Type(Integer32):
    """Custom type sipMiscAssertedIDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noHeaderAdded", 0),
          ("pAssertedIdRFC3325", 1),
          ("pPreferreddIdRFC3325", 2))
    )


_SipMiscAssertedIDMode_Type.__name__ = "Integer32"
_SipMiscAssertedIDMode_Object = MibScalar
sipMiscAssertedIDMode = _SipMiscAssertedIDMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 8),
    _SipMiscAssertedIDMode_Type()
)
sipMiscAssertedIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscAssertedIDMode.setStatus("current")


class _SipMiscIsUserPhoneInFrom_Type(Integer32):
    """Custom type sipMiscIsUserPhoneInFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscIsUserPhoneInFrom_Type.__name__ = "Integer32"
_SipMiscIsUserPhoneInFrom_Object = MibScalar
sipMiscIsUserPhoneInFrom = _SipMiscIsUserPhoneInFrom_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 9),
    _SipMiscIsUserPhoneInFrom_Type()
)
sipMiscIsUserPhoneInFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscIsUserPhoneInFrom.setStatus("current")


class _SipMiscAddTon2Rpi_Type(Integer32):
    """Custom type sipMiscAddTon2Rpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscAddTon2Rpi_Type.__name__ = "Integer32"
_SipMiscAddTon2Rpi_Object = MibScalar
sipMiscAddTon2Rpi = _SipMiscAddTon2Rpi_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 10),
    _SipMiscAddTon2Rpi_Type()
)
sipMiscAddTon2Rpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscAddTon2Rpi.setStatus("current")


class _SipMiscEnableCIC_Type(Integer32):
    """Custom type sipMiscEnableCIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SipMiscEnableCIC_Type.__name__ = "Integer32"
_SipMiscEnableCIC_Object = MibScalar
sipMiscEnableCIC = _SipMiscEnableCIC_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 11),
    _SipMiscEnableCIC_Type()
)
sipMiscEnableCIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableCIC.setStatus("current")


class _SipMiscTransportType_Type(Integer32):
    """Custom type sipMiscTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("tls", 2),
          ("udp", 0))
    )


_SipMiscTransportType_Type.__name__ = "Integer32"
_SipMiscTransportType_Object = MibScalar
sipMiscTransportType = _SipMiscTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 12),
    _SipMiscTransportType_Type()
)
sipMiscTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscTransportType.setStatus("current")


class _SipMiscISubNumberOfDigits_Type(Unsigned32):
    """Custom type sipMiscISubNumberOfDigits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36),
    )


_SipMiscISubNumberOfDigits_Type.__name__ = "Unsigned32"
_SipMiscISubNumberOfDigits_Object = MibScalar
sipMiscISubNumberOfDigits = _SipMiscISubNumberOfDigits_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 13),
    _SipMiscISubNumberOfDigits_Type()
)
sipMiscISubNumberOfDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscISubNumberOfDigits.setStatus("current")


class _SipMiscSIP183Behaviour_Type(Integer32):
    """Custom type sipMiscSIP183Behaviour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscSIP183Behaviour_Type.__name__ = "Integer32"
_SipMiscSIP183Behaviour_Object = MibScalar
sipMiscSIP183Behaviour = _SipMiscSIP183Behaviour_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 14),
    _SipMiscSIP183Behaviour_Type()
)
sipMiscSIP183Behaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscSIP183Behaviour.setStatus("current")


class _SipMiscUseToHeaderAsCalledNum_Type(Integer32):
    """Custom type sipMiscUseToHeaderAsCalledNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscUseToHeaderAsCalledNum_Type.__name__ = "Integer32"
_SipMiscUseToHeaderAsCalledNum_Object = MibScalar
sipMiscUseToHeaderAsCalledNum = _SipMiscUseToHeaderAsCalledNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 15),
    _SipMiscUseToHeaderAsCalledNum_Type()
)
sipMiscUseToHeaderAsCalledNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscUseToHeaderAsCalledNum.setStatus("current")


class _SipMiscEnableSIPS_Type(Integer32):
    """Custom type sipMiscEnableSIPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnableSIPS_Type.__name__ = "Integer32"
_SipMiscEnableSIPS_Object = MibScalar
sipMiscEnableSIPS = _SipMiscEnableSIPS_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 16),
    _SipMiscEnableSIPS_Type()
)
sipMiscEnableSIPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableSIPS.setStatus("current")


class _SipMiscEnableSRVQuery_Type(Integer32):
    """Custom type sipMiscEnableSRVQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnableSRVQuery_Type.__name__ = "Integer32"
_SipMiscEnableSRVQuery_Object = MibScalar
sipMiscEnableSRVQuery = _SipMiscEnableSRVQuery_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 17),
    _SipMiscEnableSRVQuery_Type()
)
sipMiscEnableSRVQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableSRVQuery.setStatus("obsolete")


class _SipMiscSubject_Type(SnmpAdminString):
    """Custom type sipMiscSubject based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SipMiscSubject_Type.__name__ = "SnmpAdminString"
_SipMiscSubject_Object = MibScalar
sipMiscSubject = _SipMiscSubject_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 18),
    _SipMiscSubject_Type()
)
sipMiscSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscSubject.setStatus("current")


class _SipMiscUseSIPTgrp_Type(Integer32):
    """Custom type sipMiscUseSIPTgrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("nortelHotline", 3),
          ("sendAndReceive", 2),
          ("sendOnly", 1))
    )


_SipMiscUseSIPTgrp_Type.__name__ = "Integer32"
_SipMiscUseSIPTgrp_Object = MibScalar
sipMiscUseSIPTgrp = _SipMiscUseSIPTgrp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 19),
    _SipMiscUseSIPTgrp_Type()
)
sipMiscUseSIPTgrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscUseSIPTgrp.setStatus("current")


class _SipMiscSend180ForCallWaiting_Type(Integer32):
    """Custom type sipMiscSend180ForCallWaiting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscSend180ForCallWaiting_Type.__name__ = "Integer32"
_SipMiscSend180ForCallWaiting_Object = MibScalar
sipMiscSend180ForCallWaiting = _SipMiscSend180ForCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 20),
    _SipMiscSend180ForCallWaiting_Type()
)
sipMiscSend180ForCallWaiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscSend180ForCallWaiting.setStatus("current")


class _SipMiscUserAgentDisplayInfo_Type(SnmpAdminString):
    """Custom type sipMiscUserAgentDisplayInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SipMiscUserAgentDisplayInfo_Type.__name__ = "SnmpAdminString"
_SipMiscUserAgentDisplayInfo_Object = MibScalar
sipMiscUserAgentDisplayInfo = _SipMiscUserAgentDisplayInfo_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 21),
    _SipMiscUserAgentDisplayInfo_Type()
)
sipMiscUserAgentDisplayInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscUserAgentDisplayInfo.setStatus("current")


class _SipMiscSessionExpiresMethod_Type(Integer32):
    """Custom type sipMiscSessionExpiresMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invite", 0),
          ("update", 1))
    )


_SipMiscSessionExpiresMethod_Type.__name__ = "Integer32"
_SipMiscSessionExpiresMethod_Object = MibScalar
sipMiscSessionExpiresMethod = _SipMiscSessionExpiresMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 22),
    _SipMiscSessionExpiresMethod_Type()
)
sipMiscSessionExpiresMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscSessionExpiresMethod.setStatus("current")


class _SipMiscEnableGRUU_Type(Integer32):
    """Custom type sipMiscEnableGRUU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnableGRUU_Type.__name__ = "Integer32"
_SipMiscEnableGRUU_Object = MibScalar
sipMiscEnableGRUU = _SipMiscEnableGRUU_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 23),
    _SipMiscEnableGRUU_Type()
)
sipMiscEnableGRUU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableGRUU.setStatus("current")


class _SipMiscDNSQueryType_Type(Integer32):
    """Custom type sipMiscDNSQueryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aRecord", 0),
          ("nAPTR", 2),
          ("sRV", 1))
    )


_SipMiscDNSQueryType_Type.__name__ = "Integer32"
_SipMiscDNSQueryType_Object = MibScalar
sipMiscDNSQueryType = _SipMiscDNSQueryType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 24),
    _SipMiscDNSQueryType_Type()
)
sipMiscDNSQueryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscDNSQueryType.setStatus("current")


class _SipMiscEnableHistoryInfo_Type(Integer32):
    """Custom type sipMiscEnableHistoryInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnableHistoryInfo_Type.__name__ = "Integer32"
_SipMiscEnableHistoryInfo_Object = MibScalar
sipMiscEnableHistoryInfo = _SipMiscEnableHistoryInfo_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 25),
    _SipMiscEnableHistoryInfo_Type()
)
sipMiscEnableHistoryInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableHistoryInfo.setStatus("current")


class _SipMiscEnableTCPConnectionReuse_Type(Integer32):
    """Custom type sipMiscEnableTCPConnectionReuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnableTCPConnectionReuse_Type.__name__ = "Integer32"
_SipMiscEnableTCPConnectionReuse_Object = MibScalar
sipMiscEnableTCPConnectionReuse = _SipMiscEnableTCPConnectionReuse_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 26),
    _SipMiscEnableTCPConnectionReuse_Type()
)
sipMiscEnableTCPConnectionReuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableTCPConnectionReuse.setStatus("current")


class _SipMiscComfortNoiseNegotiation_Type(Integer32):
    """Custom type sipMiscComfortNoiseNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscComfortNoiseNegotiation_Type.__name__ = "Integer32"
_SipMiscComfortNoiseNegotiation_Object = MibScalar
sipMiscComfortNoiseNegotiation = _SipMiscComfortNoiseNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 27),
    _SipMiscComfortNoiseNegotiation_Type()
)
sipMiscComfortNoiseNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscComfortNoiseNegotiation.setStatus("current")


class _SipMiscMultiPtimeFormat_Type(Integer32):
    """Custom type sipMiscMultiPtimeFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("packetCable", 1))
    )


_SipMiscMultiPtimeFormat_Type.__name__ = "Integer32"
_SipMiscMultiPtimeFormat_Object = MibScalar
sipMiscMultiPtimeFormat = _SipMiscMultiPtimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 28),
    _SipMiscMultiPtimeFormat_Type()
)
sipMiscMultiPtimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscMultiPtimeFormat.setStatus("current")


class _SipMiscRTPOnlyMode_Type(Integer32):
    """Custom type sipMiscRTPOnlyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("receiveOnly", 3),
          ("transmitNReceive", 1),
          ("transmitOnly", 2))
    )


_SipMiscRTPOnlyMode_Type.__name__ = "Integer32"
_SipMiscRTPOnlyMode_Object = MibScalar
sipMiscRTPOnlyMode = _SipMiscRTPOnlyMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 29),
    _SipMiscRTPOnlyMode_Type()
)
sipMiscRTPOnlyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscRTPOnlyMode.setStatus("current")


class _SipMiscEnableReasonHeader_Type(Integer32):
    """Custom type sipMiscEnableReasonHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnableReasonHeader_Type.__name__ = "Integer32"
_SipMiscEnableReasonHeader_Object = MibScalar
sipMiscEnableReasonHeader = _SipMiscEnableReasonHeader_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 30),
    _SipMiscEnableReasonHeader_Type()
)
sipMiscEnableReasonHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableReasonHeader.setStatus("current")


class _SipMisc3xxBehavior_Type(Integer32):
    """Custom type sipMisc3xxBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forward", 0),
          ("redirect", 1))
    )


_SipMisc3xxBehavior_Type.__name__ = "Integer32"
_SipMisc3xxBehavior_Object = MibScalar
sipMisc3xxBehavior = _SipMisc3xxBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 31),
    _SipMisc3xxBehavior_Type()
)
sipMisc3xxBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMisc3xxBehavior.setStatus("current")


class _SipMiscEnableSemiAttendedTransfer_Type(Integer32):
    """Custom type sipMiscEnableSemiAttendedTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnableSemiAttendedTransfer_Type.__name__ = "Integer32"
_SipMiscEnableSemiAttendedTransfer_Object = MibScalar
sipMiscEnableSemiAttendedTransfer = _SipMiscEnableSemiAttendedTransfer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 32),
    _SipMiscEnableSemiAttendedTransfer_Type()
)
sipMiscEnableSemiAttendedTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableSemiAttendedTransfer.setStatus("current")


class _SipMiscUseSIPURIForDiversionHeader_Type(Integer32):
    """Custom type sipMiscUseSIPURIForDiversionHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("tel", 0))
    )


_SipMiscUseSIPURIForDiversionHeader_Type.__name__ = "Integer32"
_SipMiscUseSIPURIForDiversionHeader_Object = MibScalar
sipMiscUseSIPURIForDiversionHeader = _SipMiscUseSIPURIForDiversionHeader_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 33),
    _SipMiscUseSIPURIForDiversionHeader_Type()
)
sipMiscUseSIPURIForDiversionHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscUseSIPURIForDiversionHeader.setStatus("current")


class _SipMiscEnableVMURI_Type(Integer32):
    """Custom type sipMiscEnableVMURI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnableVMURI_Type.__name__ = "Integer32"
_SipMiscEnableVMURI_Object = MibScalar
sipMiscEnableVMURI = _SipMiscEnableVMURI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 34),
    _SipMiscEnableVMURI_Type()
)
sipMiscEnableVMURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableVMURI.setStatus("current")


class _SipMiscEnablePChargingVector_Type(Integer32):
    """Custom type sipMiscEnablePChargingVector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnablePChargingVector_Type.__name__ = "Integer32"
_SipMiscEnablePChargingVector_Object = MibScalar
sipMiscEnablePChargingVector = _SipMiscEnablePChargingVector_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 35),
    _SipMiscEnablePChargingVector_Type()
)
sipMiscEnablePChargingVector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnablePChargingVector.setStatus("current")


class _SipMiscPAssertedUserName_Type(SnmpAdminString):
    """Custom type sipMiscPAssertedUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SipMiscPAssertedUserName_Type.__name__ = "SnmpAdminString"
_SipMiscPAssertedUserName_Object = MibScalar
sipMiscPAssertedUserName = _SipMiscPAssertedUserName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 36),
    _SipMiscPAssertedUserName_Type()
)
sipMiscPAssertedUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscPAssertedUserName.setStatus("current")


class _SipMiscSDPSessionOwner_Type(SnmpAdminString):
    """Custom type sipMiscSDPSessionOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_SipMiscSDPSessionOwner_Type.__name__ = "SnmpAdminString"
_SipMiscSDPSessionOwner_Object = MibScalar
sipMiscSDPSessionOwner = _SipMiscSDPSessionOwner_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 37),
    _SipMiscSDPSessionOwner_Type()
)
sipMiscSDPSessionOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscSDPSessionOwner.setStatus("current")


class _SipMiscResetOnINIFileDownload_Type(Integer32):
    """Custom type sipMiscResetOnINIFileDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscResetOnINIFileDownload_Type.__name__ = "Integer32"
_SipMiscResetOnINIFileDownload_Object = MibScalar
sipMiscResetOnINIFileDownload = _SipMiscResetOnINIFileDownload_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 38),
    _SipMiscResetOnINIFileDownload_Type()
)
sipMiscResetOnINIFileDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscResetOnINIFileDownload.setStatus("obsolete")


class _SipMiscSetDefaultOnIniFileProcess_Type(Unsigned32):
    """Custom type sipMiscSetDefaultOnIniFileProcess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SipMiscSetDefaultOnIniFileProcess_Type.__name__ = "Unsigned32"
_SipMiscSetDefaultOnIniFileProcess_Object = MibScalar
sipMiscSetDefaultOnIniFileProcess = _SipMiscSetDefaultOnIniFileProcess_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 39),
    _SipMiscSetDefaultOnIniFileProcess_Type()
)
sipMiscSetDefaultOnIniFileProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscSetDefaultOnIniFileProcess.setStatus("current")


class _SipMiscEnableContactRestriction_Type(Integer32):
    """Custom type sipMiscEnableContactRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnableContactRestriction_Type.__name__ = "Integer32"
_SipMiscEnableContactRestriction_Object = MibScalar
sipMiscEnableContactRestriction = _SipMiscEnableContactRestriction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 40),
    _SipMiscEnableContactRestriction_Type()
)
sipMiscEnableContactRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnableContactRestriction.setStatus("current")


class _SipMiscEnablePAssociatedURIHeader_Type(Integer32):
    """Custom type sipMiscEnablePAssociatedURIHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscEnablePAssociatedURIHeader_Type.__name__ = "Integer32"
_SipMiscEnablePAssociatedURIHeader_Object = MibScalar
sipMiscEnablePAssociatedURIHeader = _SipMiscEnablePAssociatedURIHeader_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 41),
    _SipMiscEnablePAssociatedURIHeader_Type()
)
sipMiscEnablePAssociatedURIHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscEnablePAssociatedURIHeader.setStatus("current")


class _SipMiscMinSE_Type(Unsigned32):
    """Custom type sipMiscMinSE based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_SipMiscMinSE_Type.__name__ = "Unsigned32"
_SipMiscMinSE_Object = MibScalar
sipMiscMinSE = _SipMiscMinSE_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 42),
    _SipMiscMinSE_Type()
)
sipMiscMinSE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscMinSE.setStatus("current")


class _SipMiscApplicationProfile_Type(Unsigned32):
    """Custom type sipMiscApplicationProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_SipMiscApplicationProfile_Type.__name__ = "Unsigned32"
_SipMiscApplicationProfile_Object = MibScalar
sipMiscApplicationProfile = _SipMiscApplicationProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 43),
    _SipMiscApplicationProfile_Type()
)
sipMiscApplicationProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscApplicationProfile.setStatus("current")


class _SipMiscOPTIONSUserPart_Type(SnmpAdminString):
    """Custom type sipMiscOPTIONSUserPart based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SipMiscOPTIONSUserPart_Type.__name__ = "SnmpAdminString"
_SipMiscOPTIONSUserPart_Object = MibScalar
sipMiscOPTIONSUserPart = _SipMiscOPTIONSUserPart_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 44),
    _SipMiscOPTIONSUserPart_Type()
)
sipMiscOPTIONSUserPart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscOPTIONSUserPart.setStatus("current")


class _SipMiscUseAORInReferToHeader_Type(Integer32):
    """Custom type sipMiscUseAORInReferToHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscUseAORInReferToHeader_Type.__name__ = "Integer32"
_SipMiscUseAORInReferToHeader_Object = MibScalar
sipMiscUseAORInReferToHeader = _SipMiscUseAORInReferToHeader_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 45),
    _SipMiscUseAORInReferToHeader_Type()
)
sipMiscUseAORInReferToHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscUseAORInReferToHeader.setStatus("current")


class _SipMiscForkingHandlingMode_Type(Integer32):
    """Custom type sipMiscForkingHandlingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("parallel", 1),
          ("sequential", 0))
    )


_SipMiscForkingHandlingMode_Type.__name__ = "Integer32"
_SipMiscForkingHandlingMode_Object = MibScalar
sipMiscForkingHandlingMode = _SipMiscForkingHandlingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 46),
    _SipMiscForkingHandlingMode_Type()
)
sipMiscForkingHandlingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscForkingHandlingMode.setStatus("current")


class _SipMiscOfferUnencryptedSRTCP_Type(Integer32):
    """Custom type sipMiscOfferUnencryptedSRTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipMiscOfferUnencryptedSRTCP_Type.__name__ = "Integer32"
_SipMiscOfferUnencryptedSRTCP_Object = MibScalar
sipMiscOfferUnencryptedSRTCP = _SipMiscOfferUnencryptedSRTCP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 47),
    _SipMiscOfferUnencryptedSRTCP_Type()
)
sipMiscOfferUnencryptedSRTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscOfferUnencryptedSRTCP.setStatus("obsolete")


class _SipMiscSourceNumberPreference_Type(SnmpAdminString):
    """Custom type sipMiscSourceNumberPreference based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SipMiscSourceNumberPreference_Type.__name__ = "SnmpAdminString"
_SipMiscSourceNumberPreference_Object = MibScalar
sipMiscSourceNumberPreference = _SipMiscSourceNumberPreference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 7, 48),
    _SipMiscSourceNumberPreference_Type()
)
sipMiscSourceNumberPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMiscSourceNumberPreference.setStatus("current")
_SipSubscribe_ObjectIdentity = ObjectIdentity
sipSubscribe = _SipSubscribe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 8)
)


class _SipSubscribeEnable_Type(Integer32):
    """Custom type sipSubscribeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipSubscribeEnable_Type.__name__ = "Integer32"
_SipSubscribeEnable_Object = MibScalar
sipSubscribeEnable = _SipSubscribeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 8, 1),
    _SipSubscribeEnable_Type()
)
sipSubscribeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSubscribeEnable.setStatus("current")


class _SipSubscribeRetryTime_Type(Unsigned32):
    """Custom type sipSubscribeRetryTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000000),
    )


_SipSubscribeRetryTime_Type.__name__ = "Unsigned32"
_SipSubscribeRetryTime_Object = MibScalar
sipSubscribeRetryTime = _SipSubscribeRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 8, 2),
    _SipSubscribeRetryTime_Type()
)
sipSubscribeRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSubscribeRetryTime.setStatus("current")


class _SipSubscribeEnableMWISubscription_Type(Integer32):
    """Custom type sipSubscribeEnableMWISubscription based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipSubscribeEnableMWISubscription_Type.__name__ = "Integer32"
_SipSubscribeEnableMWISubscription_Object = MibScalar
sipSubscribeEnableMWISubscription = _SipSubscribeEnableMWISubscription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 8, 3),
    _SipSubscribeEnableMWISubscription_Type()
)
sipSubscribeEnableMWISubscription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSubscribeEnableMWISubscription.setStatus("current")


class _SipSubscribeSubscriptionMode_Type(Integer32):
    """Custom type sipSubscribeSubscriptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("perEndpoint", 0),
          ("perGateway", 1))
    )


_SipSubscribeSubscriptionMode_Type.__name__ = "Integer32"
_SipSubscribeSubscriptionMode_Object = MibScalar
sipSubscribeSubscriptionMode = _SipSubscribeSubscriptionMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 8, 4),
    _SipSubscribeSubscriptionMode_Type()
)
sipSubscribeSubscriptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSubscribeSubscriptionMode.setStatus("current")
_SipDigitalGW_ObjectIdentity = ObjectIdentity
sipDigitalGW = _SipDigitalGW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9)
)
_CauseMapSIP2ISDNTable_Object = MibTable
causeMapSIP2ISDNTable = _CauseMapSIP2ISDNTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 21)
)
if mibBuilder.loadTexts:
    causeMapSIP2ISDNTable.setStatus("current")
_CauseMapSIP2ISDNEntry_Object = MibTableRow
causeMapSIP2ISDNEntry = _CauseMapSIP2ISDNEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 21, 1)
)
causeMapSIP2ISDNEntry.setIndexNames(
    (0, "AcGateway", "causeMapSIP2ISDNIndex"),
)
if mibBuilder.loadTexts:
    causeMapSIP2ISDNEntry.setStatus("current")


class _CauseMapSIP2ISDNIndex_Type(Unsigned32):
    """Custom type causeMapSIP2ISDNIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CauseMapSIP2ISDNIndex_Type.__name__ = "Unsigned32"
_CauseMapSIP2ISDNIndex_Object = MibTableColumn
causeMapSIP2ISDNIndex = _CauseMapSIP2ISDNIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 21, 1, 1),
    _CauseMapSIP2ISDNIndex_Type()
)
causeMapSIP2ISDNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    causeMapSIP2ISDNIndex.setStatus("current")
_CauseMapSIP2ISDNRowStatus_Type = RowStatus
_CauseMapSIP2ISDNRowStatus_Object = MibTableColumn
causeMapSIP2ISDNRowStatus = _CauseMapSIP2ISDNRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 21, 1, 2),
    _CauseMapSIP2ISDNRowStatus_Type()
)
causeMapSIP2ISDNRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    causeMapSIP2ISDNRowStatus.setStatus("current")


class _CauseMapSIP2ISDNAction_Type(Integer32):
    """Custom type causeMapSIP2ISDNAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_CauseMapSIP2ISDNAction_Type.__name__ = "Integer32"
_CauseMapSIP2ISDNAction_Object = MibTableColumn
causeMapSIP2ISDNAction = _CauseMapSIP2ISDNAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 21, 1, 3),
    _CauseMapSIP2ISDNAction_Type()
)
causeMapSIP2ISDNAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    causeMapSIP2ISDNAction.setStatus("current")


class _CauseMapSIP2ISDNActionResult_Type(Integer32):
    """Custom type causeMapSIP2ISDNActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_CauseMapSIP2ISDNActionResult_Type.__name__ = "Integer32"
_CauseMapSIP2ISDNActionResult_Object = MibTableColumn
causeMapSIP2ISDNActionResult = _CauseMapSIP2ISDNActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 21, 1, 4),
    _CauseMapSIP2ISDNActionResult_Type()
)
causeMapSIP2ISDNActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    causeMapSIP2ISDNActionResult.setStatus("current")


class _CauseMapSIP2ISDNSIPResponse_Type(Integer32):
    """Custom type causeMapSIP2ISDNSIPResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 700),
    )


_CauseMapSIP2ISDNSIPResponse_Type.__name__ = "Integer32"
_CauseMapSIP2ISDNSIPResponse_Object = MibTableColumn
causeMapSIP2ISDNSIPResponse = _CauseMapSIP2ISDNSIPResponse_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 21, 1, 5),
    _CauseMapSIP2ISDNSIPResponse_Type()
)
causeMapSIP2ISDNSIPResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    causeMapSIP2ISDNSIPResponse.setStatus("current")


class _CauseMapSIP2ISDNQ850Cause_Type(Integer32):
    """Custom type causeMapSIP2ISDNQ850Cause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_CauseMapSIP2ISDNQ850Cause_Type.__name__ = "Integer32"
_CauseMapSIP2ISDNQ850Cause_Object = MibTableColumn
causeMapSIP2ISDNQ850Cause = _CauseMapSIP2ISDNQ850Cause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 21, 1, 6),
    _CauseMapSIP2ISDNQ850Cause_Type()
)
causeMapSIP2ISDNQ850Cause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    causeMapSIP2ISDNQ850Cause.setStatus("current")
_CauseMapISDN2SIPTable_Object = MibTable
causeMapISDN2SIPTable = _CauseMapISDN2SIPTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 22)
)
if mibBuilder.loadTexts:
    causeMapISDN2SIPTable.setStatus("current")
_CauseMapISDN2SIPEntry_Object = MibTableRow
causeMapISDN2SIPEntry = _CauseMapISDN2SIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 22, 1)
)
causeMapISDN2SIPEntry.setIndexNames(
    (0, "AcGateway", "causeMapISDN2SIPIndex"),
)
if mibBuilder.loadTexts:
    causeMapISDN2SIPEntry.setStatus("current")


class _CauseMapISDN2SIPIndex_Type(Unsigned32):
    """Custom type causeMapISDN2SIPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CauseMapISDN2SIPIndex_Type.__name__ = "Unsigned32"
_CauseMapISDN2SIPIndex_Object = MibTableColumn
causeMapISDN2SIPIndex = _CauseMapISDN2SIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 22, 1, 1),
    _CauseMapISDN2SIPIndex_Type()
)
causeMapISDN2SIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    causeMapISDN2SIPIndex.setStatus("current")
_CauseMapISDN2SIPRowStatus_Type = RowStatus
_CauseMapISDN2SIPRowStatus_Object = MibTableColumn
causeMapISDN2SIPRowStatus = _CauseMapISDN2SIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 22, 1, 2),
    _CauseMapISDN2SIPRowStatus_Type()
)
causeMapISDN2SIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    causeMapISDN2SIPRowStatus.setStatus("current")


class _CauseMapISDN2SIPAction_Type(Integer32):
    """Custom type causeMapISDN2SIPAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_CauseMapISDN2SIPAction_Type.__name__ = "Integer32"
_CauseMapISDN2SIPAction_Object = MibTableColumn
causeMapISDN2SIPAction = _CauseMapISDN2SIPAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 22, 1, 3),
    _CauseMapISDN2SIPAction_Type()
)
causeMapISDN2SIPAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    causeMapISDN2SIPAction.setStatus("current")


class _CauseMapISDN2SIPActionResult_Type(Integer32):
    """Custom type causeMapISDN2SIPActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_CauseMapISDN2SIPActionResult_Type.__name__ = "Integer32"
_CauseMapISDN2SIPActionResult_Object = MibTableColumn
causeMapISDN2SIPActionResult = _CauseMapISDN2SIPActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 22, 1, 4),
    _CauseMapISDN2SIPActionResult_Type()
)
causeMapISDN2SIPActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    causeMapISDN2SIPActionResult.setStatus("current")


class _CauseMapISDN2SIPQ850Cause_Type(Integer32):
    """Custom type causeMapISDN2SIPQ850Cause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_CauseMapISDN2SIPQ850Cause_Type.__name__ = "Integer32"
_CauseMapISDN2SIPQ850Cause_Object = MibTableColumn
causeMapISDN2SIPQ850Cause = _CauseMapISDN2SIPQ850Cause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 22, 1, 5),
    _CauseMapISDN2SIPQ850Cause_Type()
)
causeMapISDN2SIPQ850Cause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    causeMapISDN2SIPQ850Cause.setStatus("current")


class _CauseMapISDN2SIPSIPResponse_Type(Integer32):
    """Custom type causeMapISDN2SIPSIPResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 700),
    )


_CauseMapISDN2SIPSIPResponse_Type.__name__ = "Integer32"
_CauseMapISDN2SIPSIPResponse_Object = MibTableColumn
causeMapISDN2SIPSIPResponse = _CauseMapISDN2SIPSIPResponse_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 9, 22, 1, 6),
    _CauseMapISDN2SIPSIPResponse_Type()
)
causeMapISDN2SIPSIPResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    causeMapISDN2SIPSIPResponse.setStatus("current")
_SipSAS_ObjectIdentity = ObjectIdentity
sipSAS = _SipSAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10)
)


class _SipSASEnable_Type(Integer32):
    """Custom type sipSASEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipSASEnable_Type.__name__ = "Integer32"
_SipSASEnable_Object = MibScalar
sipSASEnable = _SipSASEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 1),
    _SipSASEnable_Type()
)
sipSASEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASEnable.setStatus("current")


class _SipSASLocalSIPUdpPort_Type(Unsigned32):
    """Custom type sipSASLocalSIPUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_SipSASLocalSIPUdpPort_Type.__name__ = "Unsigned32"
_SipSASLocalSIPUdpPort_Object = MibScalar
sipSASLocalSIPUdpPort = _SipSASLocalSIPUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 2),
    _SipSASLocalSIPUdpPort_Type()
)
sipSASLocalSIPUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASLocalSIPUdpPort.setStatus("current")


class _SipSASDefaultGatewayIP_Type(SnmpAdminString):
    """Custom type sipSASDefaultGatewayIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_SipSASDefaultGatewayIP_Type.__name__ = "SnmpAdminString"
_SipSASDefaultGatewayIP_Object = MibScalar
sipSASDefaultGatewayIP = _SipSASDefaultGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 3),
    _SipSASDefaultGatewayIP_Type()
)
sipSASDefaultGatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASDefaultGatewayIP.setStatus("current")


class _SipSASLocalSIPTlsPort_Type(Unsigned32):
    """Custom type sipSASLocalSIPTlsPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_SipSASLocalSIPTlsPort_Type.__name__ = "Unsigned32"
_SipSASLocalSIPTlsPort_Object = MibScalar
sipSASLocalSIPTlsPort = _SipSASLocalSIPTlsPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 4),
    _SipSASLocalSIPTlsPort_Type()
)
sipSASLocalSIPTlsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASLocalSIPTlsPort.setStatus("current")


class _SipSASRegistrationTime_Type(Unsigned32):
    """Custom type sipSASRegistrationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_SipSASRegistrationTime_Type.__name__ = "Unsigned32"
_SipSASRegistrationTime_Object = MibScalar
sipSASRegistrationTime = _SipSASRegistrationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 5),
    _SipSASRegistrationTime_Type()
)
sipSASRegistrationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASRegistrationTime.setStatus("current")


class _SipSASShortNumberLength_Type(Unsigned32):
    """Custom type sipSASShortNumberLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SipSASShortNumberLength_Type.__name__ = "Unsigned32"
_SipSASShortNumberLength_Object = MibScalar
sipSASShortNumberLength = _SipSASShortNumberLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 6),
    _SipSASShortNumberLength_Type()
)
sipSASShortNumberLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASShortNumberLength.setStatus("deprecated")


class _SipSASLocalSIPTcpPort_Type(Unsigned32):
    """Custom type sipSASLocalSIPTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_SipSASLocalSIPTcpPort_Type.__name__ = "Unsigned32"
_SipSASLocalSIPTcpPort_Object = MibScalar
sipSASLocalSIPTcpPort = _SipSASLocalSIPTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 7),
    _SipSASLocalSIPTcpPort_Type()
)
sipSASLocalSIPTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASLocalSIPTcpPort.setStatus("current")


class _SipSASProxySet_Type(Unsigned32):
    """Custom type sipSASProxySet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SipSASProxySet_Type.__name__ = "Unsigned32"
_SipSASProxySet_Object = MibScalar
sipSASProxySet = _SipSASProxySet_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 8),
    _SipSASProxySet_Type()
)
sipSASProxySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASProxySet.setStatus("current")


class _SipSASRedundantProxySet_Type(Integer32):
    """Custom type sipSASRedundantProxySet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 5),
    )


_SipSASRedundantProxySet_Type.__name__ = "Integer32"
_SipSASRedundantProxySet_Object = MibScalar
sipSASRedundantProxySet = _SipSASRedundantProxySet_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 9),
    _SipSASRedundantProxySet_Type()
)
sipSASRedundantProxySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASRedundantProxySet.setStatus("current")


class _SipSASBindingMode_Type(Integer32):
    """Custom type sipSASBindingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uRI", 0),
          ("userPartOnly", 1))
    )


_SipSASBindingMode_Type.__name__ = "Integer32"
_SipSASBindingMode_Object = MibScalar
sipSASBindingMode = _SipSASBindingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 10),
    _SipSASBindingMode_Type()
)
sipSASBindingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASBindingMode.setStatus("current")


class _SipSASSurvivabilityMode_Type(Integer32):
    """Custom type sipSASSurvivabilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysEmergency", 1),
          ("ignoreRegister", 2),
          ("standard", 0))
    )


_SipSASSurvivabilityMode_Type.__name__ = "Integer32"
_SipSASSurvivabilityMode_Object = MibScalar
sipSASSurvivabilityMode = _SipSASSurvivabilityMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 11),
    _SipSASSurvivabilityMode_Type()
)
sipSASSurvivabilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASSurvivabilityMode.setStatus("current")


class _SipSASEnableENUM_Type(Integer32):
    """Custom type sipSASEnableENUM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipSASEnableENUM_Type.__name__ = "Integer32"
_SipSASEnableENUM_Object = MibScalar
sipSASEnableENUM = _SipSASEnableENUM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 12),
    _SipSASEnableENUM_Type()
)
sipSASEnableENUM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASEnableENUM.setStatus("current")


class _SipSASEnableRecordRoute_Type(Integer32):
    """Custom type sipSASEnableRecordRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SipSASEnableRecordRoute_Type.__name__ = "Integer32"
_SipSASEnableRecordRoute_Object = MibScalar
sipSASEnableRecordRoute = _SipSASEnableRecordRoute_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 13),
    _SipSASEnableRecordRoute_Type()
)
sipSASEnableRecordRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSASEnableRecordRoute.setStatus("current")
_SasRegistrationManipulationTable_Object = MibTable
sasRegistrationManipulationTable = _SasRegistrationManipulationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 21)
)
if mibBuilder.loadTexts:
    sasRegistrationManipulationTable.setStatus("current")
_SasRegistrationManipulationEntry_Object = MibTableRow
sasRegistrationManipulationEntry = _SasRegistrationManipulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 21, 1)
)
sasRegistrationManipulationEntry.setIndexNames(
    (0, "AcGateway", "sasRegistrationManipulationIndex"),
)
if mibBuilder.loadTexts:
    sasRegistrationManipulationEntry.setStatus("current")


class _SasRegistrationManipulationIndex_Type(Unsigned32):
    """Custom type sasRegistrationManipulationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_SasRegistrationManipulationIndex_Type.__name__ = "Unsigned32"
_SasRegistrationManipulationIndex_Object = MibTableColumn
sasRegistrationManipulationIndex = _SasRegistrationManipulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 21, 1, 1),
    _SasRegistrationManipulationIndex_Type()
)
sasRegistrationManipulationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sasRegistrationManipulationIndex.setStatus("current")
_SasRegistrationManipulationRowStatus_Type = RowStatus
_SasRegistrationManipulationRowStatus_Object = MibTableColumn
sasRegistrationManipulationRowStatus = _SasRegistrationManipulationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 21, 1, 2),
    _SasRegistrationManipulationRowStatus_Type()
)
sasRegistrationManipulationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sasRegistrationManipulationRowStatus.setStatus("current")


class _SasRegistrationManipulationAction_Type(Integer32):
    """Custom type sasRegistrationManipulationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SasRegistrationManipulationAction_Type.__name__ = "Integer32"
_SasRegistrationManipulationAction_Object = MibTableColumn
sasRegistrationManipulationAction = _SasRegistrationManipulationAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 21, 1, 3),
    _SasRegistrationManipulationAction_Type()
)
sasRegistrationManipulationAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasRegistrationManipulationAction.setStatus("current")


class _SasRegistrationManipulationActionResult_Type(Integer32):
    """Custom type sasRegistrationManipulationActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_SasRegistrationManipulationActionResult_Type.__name__ = "Integer32"
_SasRegistrationManipulationActionResult_Object = MibTableColumn
sasRegistrationManipulationActionResult = _SasRegistrationManipulationActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 21, 1, 4),
    _SasRegistrationManipulationActionResult_Type()
)
sasRegistrationManipulationActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasRegistrationManipulationActionResult.setStatus("current")


class _SasRegistrationManipulationRemoveFromRight_Type(Unsigned32):
    """Custom type sasRegistrationManipulationRemoveFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SasRegistrationManipulationRemoveFromRight_Type.__name__ = "Unsigned32"
_SasRegistrationManipulationRemoveFromRight_Object = MibTableColumn
sasRegistrationManipulationRemoveFromRight = _SasRegistrationManipulationRemoveFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 21, 1, 5),
    _SasRegistrationManipulationRemoveFromRight_Type()
)
sasRegistrationManipulationRemoveFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sasRegistrationManipulationRemoveFromRight.setStatus("current")


class _SasRegistrationManipulationLeaveFromRight_Type(Unsigned32):
    """Custom type sasRegistrationManipulationLeaveFromRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SasRegistrationManipulationLeaveFromRight_Type.__name__ = "Unsigned32"
_SasRegistrationManipulationLeaveFromRight_Object = MibTableColumn
sasRegistrationManipulationLeaveFromRight = _SasRegistrationManipulationLeaveFromRight_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 2, 10, 21, 1, 6),
    _SasRegistrationManipulationLeaveFromRight_Type()
)
sasRegistrationManipulationLeaveFromRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sasRegistrationManipulationLeaveFromRight.setStatus("current")
_H323_ObjectIdentity = ObjectIdentity
h323 = _H323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3)
)


class _H323SourceEncodType_Type(Integer32):
    """Custom type h323SourceEncodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e164", 0),
          ("h323-Id", 1),
          ("h323-IdAndE164", 2),
          ("nPIAndTON", 3),
          ("nPIAndTONAndH323-Id", 4))
    )


_H323SourceEncodType_Type.__name__ = "Integer32"
_H323SourceEncodType_Object = MibScalar
h323SourceEncodType = _H323SourceEncodType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 1),
    _H323SourceEncodType_Type()
)
h323SourceEncodType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323SourceEncodType.setStatus("obsolete")


class _H323DestEncodType_Type(Integer32):
    """Custom type h323DestEncodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e164", 0),
          ("h323-Id", 1),
          ("h323-IdAndE164", 2),
          ("nPIAndTON", 3),
          ("nPIAndTONAndH323-Id", 4))
    )


_H323DestEncodType_Type.__name__ = "Integer32"
_H323DestEncodType_Object = MibScalar
h323DestEncodType = _H323DestEncodType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 2),
    _H323DestEncodType_Type()
)
h323DestEncodType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DestEncodType.setStatus("obsolete")


class _H323H323IDString_Type(SnmpAdminString):
    """Custom type h323H323IDString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_H323H323IDString_Type.__name__ = "SnmpAdminString"
_H323H323IDString_Object = MibScalar
h323H323IDString = _H323H323IDString_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 3),
    _H323H323IDString_Type()
)
h323H323IDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323H323IDString.setStatus("obsolete")
_H323ConnectionModes_ObjectIdentity = ObjectIdentity
h323ConnectionModes = _H323ConnectionModes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 10)
)


class _H323ConnectionModesIsTunnelingUsed_Type(Integer32):
    """Custom type h323ConnectionModesIsTunnelingUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323ConnectionModesIsTunnelingUsed_Type.__name__ = "Integer32"
_H323ConnectionModesIsTunnelingUsed_Object = MibScalar
h323ConnectionModesIsTunnelingUsed = _H323ConnectionModesIsTunnelingUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 10, 1),
    _H323ConnectionModesIsTunnelingUsed_Type()
)
h323ConnectionModesIsTunnelingUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323ConnectionModesIsTunnelingUsed.setStatus("obsolete")
_FastStart_ObjectIdentity = ObjectIdentity
fastStart = _FastStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 10, 5)
)


class _FastStartIsFastConnectUsed_Type(Integer32):
    """Custom type fastStartIsFastConnectUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FastStartIsFastConnectUsed_Type.__name__ = "Integer32"
_FastStartIsFastConnectUsed_Object = MibScalar
fastStartIsFastConnectUsed = _FastStartIsFastConnectUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 10, 5, 1),
    _FastStartIsFastConnectUsed_Type()
)
fastStartIsFastConnectUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastStartIsFastConnectUsed.setStatus("obsolete")


class _FastStartOpenH245OnFS_Type(Unsigned32):
    """Custom type fastStartOpenH245OnFS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FastStartOpenH245OnFS_Type.__name__ = "Unsigned32"
_FastStartOpenH245OnFS_Object = MibScalar
fastStartOpenH245OnFS = _FastStartOpenH245OnFS_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 10, 5, 2),
    _FastStartOpenH245OnFS_Type()
)
fastStartOpenH245OnFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastStartOpenH245OnFS.setStatus("obsolete")


class _FastStartIsFSMediaInfoSendOnConnect_Type(Integer32):
    """Custom type fastStartIsFSMediaInfoSendOnConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FastStartIsFSMediaInfoSendOnConnect_Type.__name__ = "Integer32"
_FastStartIsFSMediaInfoSendOnConnect_Object = MibScalar
fastStartIsFSMediaInfoSendOnConnect = _FastStartIsFSMediaInfoSendOnConnect_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 10, 5, 3),
    _FastStartIsFSMediaInfoSendOnConnect_Type()
)
fastStartIsFSMediaInfoSendOnConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastStartIsFSMediaInfoSendOnConnect.setStatus("obsolete")


class _FastStartIsFSOpenMediaOnConnect_Type(Integer32):
    """Custom type fastStartIsFSOpenMediaOnConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FastStartIsFSOpenMediaOnConnect_Type.__name__ = "Integer32"
_FastStartIsFSOpenMediaOnConnect_Object = MibScalar
fastStartIsFSOpenMediaOnConnect = _FastStartIsFSOpenMediaOnConnect_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 10, 5, 4),
    _FastStartIsFSOpenMediaOnConnect_Type()
)
fastStartIsFSOpenMediaOnConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastStartIsFSOpenMediaOnConnect.setStatus("obsolete")
_H323GK_ObjectIdentity = ObjectIdentity
h323GK = _H323GK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11)
)


class _H323GKIsGateKeeperUsed_Type(Integer32):
    """Custom type h323GKIsGateKeeperUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323GKIsGateKeeperUsed_Type.__name__ = "Integer32"
_H323GKIsGateKeeperUsed_Object = MibScalar
h323GKIsGateKeeperUsed = _H323GKIsGateKeeperUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 1),
    _H323GKIsGateKeeperUsed_Type()
)
h323GKIsGateKeeperUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKIsGateKeeperUsed.setStatus("obsolete")


class _H323GKGwRegistrType_Type(Integer32):
    """Custom type h323GKGwRegistrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e164", 0),
          ("h323-Id", 1),
          ("h323-IdAndE164", 2),
          ("nPIAndTON", 3),
          ("nPIAndTONAndH323-Id", 4))
    )


_H323GKGwRegistrType_Type.__name__ = "Integer32"
_H323GKGwRegistrType_Object = MibScalar
h323GKGwRegistrType = _H323GKGwRegistrType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 2),
    _H323GKGwRegistrType_Type()
)
h323GKGwRegistrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKGwRegistrType.setStatus("obsolete")


class _H323GKIsGkFallbackUsed_Type(Integer32):
    """Custom type h323GKIsGkFallbackUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323GKIsGkFallbackUsed_Type.__name__ = "Integer32"
_H323GKIsGkFallbackUsed_Object = MibScalar
h323GKIsGkFallbackUsed = _H323GKIsGkFallbackUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 3),
    _H323GKIsGkFallbackUsed_Type()
)
h323GKIsGkFallbackUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKIsGkFallbackUsed.setStatus("obsolete")


class _H323GKCanMapAliases_Type(Integer32):
    """Custom type h323GKCanMapAliases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323GKCanMapAliases_Type.__name__ = "Integer32"
_H323GKCanMapAliases_Object = MibScalar
h323GKCanMapAliases = _H323GKCanMapAliases_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 4),
    _H323GKCanMapAliases_Type()
)
h323GKCanMapAliases.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKCanMapAliases.setStatus("obsolete")


class _H323GKResponseTimeout_Type(Unsigned32):
    """Custom type h323GKResponseTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_H323GKResponseTimeout_Type.__name__ = "Unsigned32"
_H323GKResponseTimeout_Object = MibScalar
h323GKResponseTimeout = _H323GKResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 5),
    _H323GKResponseTimeout_Type()
)
h323GKResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKResponseTimeout.setStatus("obsolete")


class _H323GKMaxRetries_Type(Unsigned32):
    """Custom type h323GKMaxRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_H323GKMaxRetries_Type.__name__ = "Unsigned32"
_H323GKMaxRetries_Object = MibScalar
h323GKMaxRetries = _H323GKMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 6),
    _H323GKMaxRetries_Type()
)
h323GKMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKMaxRetries.setStatus("obsolete")


class _H323GKRegistrationTime_Type(Unsigned32):
    """Custom type h323GKRegistrationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_H323GKRegistrationTime_Type.__name__ = "Unsigned32"
_H323GKRegistrationTime_Object = MibScalar
h323GKRegistrationTime = _H323GKRegistrationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 7),
    _H323GKRegistrationTime_Type()
)
h323GKRegistrationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKRegistrationTime.setStatus("obsolete")


class _H323GKIsTerminal_Type(Integer32):
    """Custom type h323GKIsTerminal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323GKIsTerminal_Type.__name__ = "Integer32"
_H323GKIsTerminal_Object = MibScalar
h323GKIsTerminal = _H323GKIsTerminal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 8),
    _H323GKIsTerminal_Type()
)
h323GKIsTerminal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKIsTerminal.setStatus("obsolete")


class _H323GKGatekeeperID_Type(SnmpAdminString):
    """Custom type h323GKGatekeeperID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_H323GKGatekeeperID_Type.__name__ = "SnmpAdminString"
_H323GKGatekeeperID_Object = MibScalar
h323GKGatekeeperID = _H323GKGatekeeperID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 9),
    _H323GKGatekeeperID_Type()
)
h323GKGatekeeperID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKGatekeeperID.setStatus("obsolete")


class _H323GKEnablePregrantARQ_Type(Integer32):
    """Custom type h323GKEnablePregrantARQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_H323GKEnablePregrantARQ_Type.__name__ = "Integer32"
_H323GKEnablePregrantARQ_Object = MibScalar
h323GKEnablePregrantARQ = _H323GKEnablePregrantARQ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 10),
    _H323GKEnablePregrantARQ_Type()
)
h323GKEnablePregrantARQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKEnablePregrantARQ.setStatus("obsolete")


class _H323GKRegister_Type(Integer32):
    """Custom type h323GKRegister based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_H323GKRegister_Type.__name__ = "Integer32"
_H323GKRegister_Object = MibScalar
h323GKRegister = _H323GKRegister_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 11),
    _H323GKRegister_Type()
)
h323GKRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKRegister.setStatus("current")


class _H323GKAlternativeGKUsed_Type(Integer32):
    """Custom type h323GKAlternativeGKUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_H323GKAlternativeGKUsed_Type.__name__ = "Integer32"
_H323GKAlternativeGKUsed_Object = MibScalar
h323GKAlternativeGKUsed = _H323GKAlternativeGKUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 12),
    _H323GKAlternativeGKUsed_Type()
)
h323GKAlternativeGKUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKAlternativeGKUsed.setStatus("obsolete")


class _H323GKUseRedundantGKOnRRJ_Type(Integer32):
    """Custom type h323GKUseRedundantGKOnRRJ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_H323GKUseRedundantGKOnRRJ_Type.__name__ = "Integer32"
_H323GKUseRedundantGKOnRRJ_Object = MibScalar
h323GKUseRedundantGKOnRRJ = _H323GKUseRedundantGKOnRRJ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 13),
    _H323GKUseRedundantGKOnRRJ_Type()
)
h323GKUseRedundantGKOnRRJ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKUseRedundantGKOnRRJ.setStatus("obsolete")


class _H323GKEnableGKAutoDiscovery_Type(Integer32):
    """Custom type h323GKEnableGKAutoDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_H323GKEnableGKAutoDiscovery_Type.__name__ = "Integer32"
_H323GKEnableGKAutoDiscovery_Object = MibScalar
h323GKEnableGKAutoDiscovery = _H323GKEnableGKAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 14),
    _H323GKEnableGKAutoDiscovery_Type()
)
h323GKEnableGKAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKEnableGKAutoDiscovery.setStatus("obsolete")
_H323GKGKAutoDiscoveryIP_Type = IpAddress
_H323GKGKAutoDiscoveryIP_Object = MibScalar
h323GKGKAutoDiscoveryIP = _H323GKGKAutoDiscoveryIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 15),
    _H323GKGKAutoDiscoveryIP_Type()
)
h323GKGKAutoDiscoveryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GKGKAutoDiscoveryIP.setStatus("obsolete")
_GkIPTable_Object = MibTable
gkIPTable = _GkIPTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 21)
)
if mibBuilder.loadTexts:
    gkIPTable.setStatus("obsolete")
_GkIPEntry_Object = MibTableRow
gkIPEntry = _GkIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 21, 1)
)
gkIPEntry.setIndexNames(
    (0, "AcGateway", "gkIPIndex"),
)
if mibBuilder.loadTexts:
    gkIPEntry.setStatus("obsolete")


class _GkIPIndex_Type(Unsigned32):
    """Custom type gkIPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_GkIPIndex_Type.__name__ = "Unsigned32"
_GkIPIndex_Object = MibTableColumn
gkIPIndex = _GkIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 21, 1, 1),
    _GkIPIndex_Type()
)
gkIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gkIPIndex.setStatus("obsolete")
_GkIPRowStatus_Type = RowStatus
_GkIPRowStatus_Object = MibTableColumn
gkIPRowStatus = _GkIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 21, 1, 2),
    _GkIPRowStatus_Type()
)
gkIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gkIPRowStatus.setStatus("obsolete")


class _GkIPAction_Type(Integer32):
    """Custom type gkIPAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_GkIPAction_Type.__name__ = "Integer32"
_GkIPAction_Object = MibTableColumn
gkIPAction = _GkIPAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 21, 1, 3),
    _GkIPAction_Type()
)
gkIPAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gkIPAction.setStatus("obsolete")


class _GkIPActionResult_Type(Integer32):
    """Custom type gkIPActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_GkIPActionResult_Type.__name__ = "Integer32"
_GkIPActionResult_Object = MibTableColumn
gkIPActionResult = _GkIPActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 21, 1, 4),
    _GkIPActionResult_Type()
)
gkIPActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gkIPActionResult.setStatus("obsolete")


class _GkIPGatekeeperIP_Type(SnmpAdminString):
    """Custom type gkIPGatekeeperIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_GkIPGatekeeperIP_Type.__name__ = "SnmpAdminString"
_GkIPGatekeeperIP_Object = MibTableColumn
gkIPGatekeeperIP = _GkIPGatekeeperIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 21, 1, 5),
    _GkIPGatekeeperIP_Type()
)
gkIPGatekeeperIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gkIPGatekeeperIP.setStatus("obsolete")


class _GkIPGateleeperID_Type(SnmpAdminString):
    """Custom type gkIPGateleeperID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GkIPGateleeperID_Type.__name__ = "SnmpAdminString"
_GkIPGateleeperID_Object = MibTableColumn
gkIPGateleeperID = _GkIPGateleeperID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 21, 1, 6),
    _GkIPGateleeperID_Type()
)
gkIPGateleeperID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gkIPGateleeperID.setStatus("obsolete")
_RegisterPrefixTable_Object = MibTable
registerPrefixTable = _RegisterPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 22)
)
if mibBuilder.loadTexts:
    registerPrefixTable.setStatus("obsolete")
_RegisterPrefixEntry_Object = MibTableRow
registerPrefixEntry = _RegisterPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 22, 1)
)
registerPrefixEntry.setIndexNames(
    (0, "AcGateway", "registerPrefixIndex"),
)
if mibBuilder.loadTexts:
    registerPrefixEntry.setStatus("obsolete")


class _RegisterPrefixIndex_Type(Unsigned32):
    """Custom type registerPrefixIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_RegisterPrefixIndex_Type.__name__ = "Unsigned32"
_RegisterPrefixIndex_Object = MibTableColumn
registerPrefixIndex = _RegisterPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 22, 1, 1),
    _RegisterPrefixIndex_Type()
)
registerPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    registerPrefixIndex.setStatus("obsolete")
_RegisterPrefixRowStatus_Type = RowStatus
_RegisterPrefixRowStatus_Object = MibTableColumn
registerPrefixRowStatus = _RegisterPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 22, 1, 2),
    _RegisterPrefixRowStatus_Type()
)
registerPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    registerPrefixRowStatus.setStatus("obsolete")


class _RegisterPrefixAction_Type(Integer32):
    """Custom type registerPrefixAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_RegisterPrefixAction_Type.__name__ = "Integer32"
_RegisterPrefixAction_Object = MibTableColumn
registerPrefixAction = _RegisterPrefixAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 22, 1, 3),
    _RegisterPrefixAction_Type()
)
registerPrefixAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registerPrefixAction.setStatus("obsolete")


class _RegisterPrefixActionResult_Type(Integer32):
    """Custom type registerPrefixActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_RegisterPrefixActionResult_Type.__name__ = "Integer32"
_RegisterPrefixActionResult_Object = MibTableColumn
registerPrefixActionResult = _RegisterPrefixActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 22, 1, 4),
    _RegisterPrefixActionResult_Type()
)
registerPrefixActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registerPrefixActionResult.setStatus("obsolete")


class _RegisterPrefixPrefix_Type(SnmpAdminString):
    """Custom type registerPrefixPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_RegisterPrefixPrefix_Type.__name__ = "SnmpAdminString"
_RegisterPrefixPrefix_Object = MibTableColumn
registerPrefixPrefix = _RegisterPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 22, 1, 5),
    _RegisterPrefixPrefix_Type()
)
registerPrefixPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    registerPrefixPrefix.setStatus("obsolete")


class _RegisterPrefixNumberPlan_Type(Integer32):
    """Custom type registerPrefixNumberPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              9)
        )
    )
    namedValues = NamedValues(
        *(("e164Public", 1),
          ("private", 9),
          ("unknown", 0))
    )


_RegisterPrefixNumberPlan_Type.__name__ = "Integer32"
_RegisterPrefixNumberPlan_Object = MibTableColumn
registerPrefixNumberPlan = _RegisterPrefixNumberPlan_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 22, 1, 6),
    _RegisterPrefixNumberPlan_Type()
)
registerPrefixNumberPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    registerPrefixNumberPlan.setStatus("obsolete")


class _RegisterPrefixNumberType_Type(Integer32):
    """Custom type registerPrefixNumberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abbreviated", 6),
          ("international-Level2Regional", 1),
          ("national-Level1Regional", 2),
          ("networkSpecific-NetworkPISN", 3),
          ("subscriber-Level0Regional", 4),
          ("unknown", 0))
    )


_RegisterPrefixNumberType_Type.__name__ = "Integer32"
_RegisterPrefixNumberType_Object = MibTableColumn
registerPrefixNumberType = _RegisterPrefixNumberType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 22, 1, 7),
    _RegisterPrefixNumberType_Type()
)
registerPrefixNumberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    registerPrefixNumberType.setStatus("obsolete")
_GkRedundancy_ObjectIdentity = ObjectIdentity
gkRedundancy = _GkRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 30)
)


class _GkRedundancyUsed_Type(Integer32):
    """Custom type gkRedundancyUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_GkRedundancyUsed_Type.__name__ = "Integer32"
_GkRedundancyUsed_Object = MibScalar
gkRedundancyUsed = _GkRedundancyUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 30, 1),
    _GkRedundancyUsed_Type()
)
gkRedundancyUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gkRedundancyUsed.setStatus("obsolete")


class _GkRedundancyTimeBetweenGKsLoops_Type(Unsigned32):
    """Custom type gkRedundancyTimeBetweenGKsLoops based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_GkRedundancyTimeBetweenGKsLoops_Type.__name__ = "Unsigned32"
_GkRedundancyTimeBetweenGKsLoops_Object = MibScalar
gkRedundancyTimeBetweenGKsLoops = _GkRedundancyTimeBetweenGKsLoops_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 30, 2),
    _GkRedundancyTimeBetweenGKsLoops_Type()
)
gkRedundancyTimeBetweenGKsLoops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gkRedundancyTimeBetweenGKsLoops.setStatus("obsolete")
_GkRAI_ObjectIdentity = ObjectIdentity
gkRAI = _GkRAI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 31)
)


class _GkRAIEnable_Type(Integer32):
    """Custom type gkRAIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_GkRAIEnable_Type.__name__ = "Integer32"
_GkRAIEnable_Object = MibScalar
gkRAIEnable = _GkRAIEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 31, 1),
    _GkRAIEnable_Type()
)
gkRAIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gkRAIEnable.setStatus("obsolete")


class _GkRAIHighThreshold_Type(Unsigned32):
    """Custom type gkRAIHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GkRAIHighThreshold_Type.__name__ = "Unsigned32"
_GkRAIHighThreshold_Object = MibScalar
gkRAIHighThreshold = _GkRAIHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 31, 2),
    _GkRAIHighThreshold_Type()
)
gkRAIHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gkRAIHighThreshold.setStatus("obsolete")


class _GkRAILowThreshold_Type(Unsigned32):
    """Custom type gkRAILowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GkRAILowThreshold_Type.__name__ = "Unsigned32"
_GkRAILowThreshold_Object = MibScalar
gkRAILowThreshold = _GkRAILowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 31, 3),
    _GkRAILowThreshold_Type()
)
gkRAILowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gkRAILowThreshold.setStatus("obsolete")


class _GkRAILoopTime_Type(Unsigned32):
    """Custom type gkRAILoopTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_GkRAILoopTime_Type.__name__ = "Unsigned32"
_GkRAILoopTime_Object = MibScalar
gkRAILoopTime = _GkRAILoopTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 11, 31, 4),
    _GkRAILoopTime_Type()
)
gkRAILoopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gkRAILoopTime.setStatus("obsolete")
_H323DTMF_ObjectIdentity = ObjectIdentity
h323DTMF = _H323DTMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 12)
)


class _H323DTMFHookFlashOption_Type(Integer32):
    """Custom type h323DTMFHookFlashOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("h245Signal", 2),
          ("h245UserInput", 1),
          ("none", 0),
          ("q931UserInfo", 3))
    )


_H323DTMFHookFlashOption_Type.__name__ = "Integer32"
_H323DTMFHookFlashOption_Object = MibScalar
h323DTMFHookFlashOption = _H323DTMFHookFlashOption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 12, 1),
    _H323DTMFHookFlashOption_Type()
)
h323DTMFHookFlashOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DTMFHookFlashOption.setStatus("obsolete")


class _H323DTMFRxDtmfOption_Type(Integer32):
    """Custom type h323DTMFRxDtmfOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 4),
          ("h245Signal", 2),
          ("h245UserInput", 1),
          ("none", 0),
          ("rFC2833", 3))
    )


_H323DTMFRxDtmfOption_Type.__name__ = "Integer32"
_H323DTMFRxDtmfOption_Object = MibScalar
h323DTMFRxDtmfOption = _H323DTMFRxDtmfOption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 12, 2),
    _H323DTMFRxDtmfOption_Type()
)
h323DTMFRxDtmfOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323DTMFRxDtmfOption.setStatus("obsolete")
_DTMFOptionsTable_Object = MibTable
dTMFOptionsTable = _DTMFOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 12, 21)
)
if mibBuilder.loadTexts:
    dTMFOptionsTable.setStatus("obsolete")
_DTMFOptionsEntry_Object = MibTableRow
dTMFOptionsEntry = _DTMFOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 12, 21, 1)
)
dTMFOptionsEntry.setIndexNames(
    (0, "AcGateway", "dTMFOptionsIndex"),
)
if mibBuilder.loadTexts:
    dTMFOptionsEntry.setStatus("obsolete")


class _DTMFOptionsIndex_Type(Unsigned32):
    """Custom type dTMFOptionsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DTMFOptionsIndex_Type.__name__ = "Unsigned32"
_DTMFOptionsIndex_Object = MibTableColumn
dTMFOptionsIndex = _DTMFOptionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 12, 21, 1, 1),
    _DTMFOptionsIndex_Type()
)
dTMFOptionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTMFOptionsIndex.setStatus("obsolete")
_DTMFOptionsRowStatus_Type = RowStatus
_DTMFOptionsRowStatus_Object = MibTableColumn
dTMFOptionsRowStatus = _DTMFOptionsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 12, 21, 1, 2),
    _DTMFOptionsRowStatus_Type()
)
dTMFOptionsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dTMFOptionsRowStatus.setStatus("obsolete")


class _DTMFOptionsAction_Type(Integer32):
    """Custom type dTMFOptionsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_DTMFOptionsAction_Type.__name__ = "Integer32"
_DTMFOptionsAction_Object = MibTableColumn
dTMFOptionsAction = _DTMFOptionsAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 12, 21, 1, 3),
    _DTMFOptionsAction_Type()
)
dTMFOptionsAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTMFOptionsAction.setStatus("obsolete")


class _DTMFOptionsActionResult_Type(Integer32):
    """Custom type dTMFOptionsActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("developmentImpending", 0)
    )


_DTMFOptionsActionResult_Type.__name__ = "Integer32"
_DTMFOptionsActionResult_Object = MibTableColumn
dTMFOptionsActionResult = _DTMFOptionsActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 12, 21, 1, 4),
    _DTMFOptionsActionResult_Type()
)
dTMFOptionsActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTMFOptionsActionResult.setStatus("obsolete")


class _DTMFOptionsTxDTMFOption_Type(Integer32):
    """Custom type dTMFOptionsTxDTMFOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("h245Signal", 2),
          ("h245UserInput", 1),
          ("none", 0),
          ("q931UserInfo", 3),
          ("rFC2833", 4))
    )


_DTMFOptionsTxDTMFOption_Type.__name__ = "Integer32"
_DTMFOptionsTxDTMFOption_Object = MibTableColumn
dTMFOptionsTxDTMFOption = _DTMFOptionsTxDTMFOption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 12, 21, 1, 5),
    _DTMFOptionsTxDTMFOption_Type()
)
dTMFOptionsTxDTMFOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dTMFOptionsTxDTMFOption.setStatus("obsolete")
_H323Ports_ObjectIdentity = ObjectIdentity
h323Ports = _H323Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 13)
)


class _H323PortsH225ListenPort_Type(Unsigned32):
    """Custom type h323PortsH225ListenPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H323PortsH225ListenPort_Type.__name__ = "Unsigned32"
_H323PortsH225ListenPort_Object = MibScalar
h323PortsH225ListenPort = _H323PortsH225ListenPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 13, 1),
    _H323PortsH225ListenPort_Type()
)
h323PortsH225ListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323PortsH225ListenPort.setStatus("obsolete")


class _H323PortsH225DialPort_Type(Unsigned32):
    """Custom type h323PortsH225DialPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H323PortsH225DialPort_Type.__name__ = "Unsigned32"
_H323PortsH225DialPort_Object = MibScalar
h323PortsH225DialPort = _H323PortsH225DialPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 13, 2),
    _H323PortsH225DialPort_Type()
)
h323PortsH225DialPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323PortsH225DialPort.setStatus("obsolete")


class _H323PortsH323BasePort_Type(Unsigned32):
    """Custom type h323PortsH323BasePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H323PortsH323BasePort_Type.__name__ = "Unsigned32"
_H323PortsH323BasePort_Object = MibScalar
h323PortsH323BasePort = _H323PortsH323BasePort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 13, 3),
    _H323PortsH323BasePort_Type()
)
h323PortsH323BasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323PortsH323BasePort.setStatus("obsolete")


class _H323PortsRasSourcePort_Type(Unsigned32):
    """Custom type h323PortsRasSourcePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H323PortsRasSourcePort_Type.__name__ = "Unsigned32"
_H323PortsRasSourcePort_Object = MibScalar
h323PortsRasSourcePort = _H323PortsRasSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 13, 4),
    _H323PortsRasSourcePort_Type()
)
h323PortsRasSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323PortsRasSourcePort.setStatus("obsolete")


class _H323PortsRasDestPort_Type(Unsigned32):
    """Custom type h323PortsRasDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H323PortsRasDestPort_Type.__name__ = "Unsigned32"
_H323PortsRasDestPort_Object = MibScalar
h323PortsRasDestPort = _H323PortsRasDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 13, 5),
    _H323PortsRasDestPort_Type()
)
h323PortsRasDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323PortsRasDestPort.setStatus("obsolete")
_H323Auth_ObjectIdentity = ObjectIdentity
h323Auth = _H323Auth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 14)
)


class _H323AuthEnableH235Security_Type(Integer32):
    """Custom type h323AuthEnableH235Security based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323AuthEnableH235Security_Type.__name__ = "Integer32"
_H323AuthEnableH235Security_Object = MibScalar
h323AuthEnableH235Security = _H323AuthEnableH235Security_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 14, 1),
    _H323AuthEnableH235Security_Type()
)
h323AuthEnableH235Security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AuthEnableH235Security.setStatus("obsolete")


class _H323AuthUserName_Type(SnmpAdminString):
    """Custom type h323AuthUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_H323AuthUserName_Type.__name__ = "SnmpAdminString"
_H323AuthUserName_Object = MibScalar
h323AuthUserName = _H323AuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 14, 2),
    _H323AuthUserName_Type()
)
h323AuthUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AuthUserName.setStatus("obsolete")


class _H323AuthPassword_Type(SnmpAdminString):
    """Custom type h323AuthPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_H323AuthPassword_Type.__name__ = "SnmpAdminString"
_H323AuthPassword_Object = MibScalar
h323AuthPassword = _H323AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 14, 3),
    _H323AuthPassword_Type()
)
h323AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323AuthPassword.setStatus("obsolete")
_H323Misc_ObjectIdentity = ObjectIdentity
h323Misc = _H323Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 15)
)


class _H323MiscIsSetupIncludeNum_Type(Integer32):
    """Custom type h323MiscIsSetupIncludeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323MiscIsSetupIncludeNum_Type.__name__ = "Integer32"
_H323MiscIsSetupIncludeNum_Object = MibScalar
h323MiscIsSetupIncludeNum = _H323MiscIsSetupIncludeNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 15, 1),
    _H323MiscIsSetupIncludeNum_Type()
)
h323MiscIsSetupIncludeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MiscIsSetupIncludeNum.setStatus("obsolete")


class _H323MiscIsSetupAckUsed_Type(Integer32):
    """Custom type h323MiscIsSetupAckUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323MiscIsSetupAckUsed_Type.__name__ = "Integer32"
_H323MiscIsSetupAckUsed_Object = MibScalar
h323MiscIsSetupAckUsed = _H323MiscIsSetupAckUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 15, 2),
    _H323MiscIsSetupAckUsed_Type()
)
h323MiscIsSetupAckUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MiscIsSetupAckUsed.setStatus("obsolete")


class _H323MiscH245InitTimeOut_Type(Unsigned32):
    """Custom type h323MiscH245InitTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000000),
    )


_H323MiscH245InitTimeOut_Type.__name__ = "Unsigned32"
_H323MiscH245InitTimeOut_Object = MibScalar
h323MiscH245InitTimeOut = _H323MiscH245InitTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 15, 3),
    _H323MiscH245InitTimeOut_Type()
)
h323MiscH245InitTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MiscH245InitTimeOut.setStatus("obsolete")


class _H323MiscEnableQ931Cause_Type(Integer32):
    """Custom type h323MiscEnableQ931Cause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323MiscEnableQ931Cause_Type.__name__ = "Integer32"
_H323MiscEnableQ931Cause_Object = MibScalar
h323MiscEnableQ931Cause = _H323MiscEnableQ931Cause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 15, 4),
    _H323MiscEnableQ931Cause_Type()
)
h323MiscEnableQ931Cause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MiscEnableQ931Cause.setStatus("obsolete")


class _H323MiscEnableQ931Multiplexing_Type(Integer32):
    """Custom type h323MiscEnableQ931Multiplexing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323MiscEnableQ931Multiplexing_Type.__name__ = "Integer32"
_H323MiscEnableQ931Multiplexing_Object = MibScalar
h323MiscEnableQ931Multiplexing = _H323MiscEnableQ931Multiplexing_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 15, 5),
    _H323MiscEnableQ931Multiplexing_Type()
)
h323MiscEnableQ931Multiplexing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MiscEnableQ931Multiplexing.setStatus("obsolete")


class _H323MiscSendChannelNonStandard_Type(Integer32):
    """Custom type h323MiscSendChannelNonStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_H323MiscSendChannelNonStandard_Type.__name__ = "Integer32"
_H323MiscSendChannelNonStandard_Object = MibScalar
h323MiscSendChannelNonStandard = _H323MiscSendChannelNonStandard_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 15, 6),
    _H323MiscSendChannelNonStandard_Type()
)
h323MiscSendChannelNonStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MiscSendChannelNonStandard.setStatus("obsolete")


class _H323MiscH245RoundTripTime_Type(Unsigned32):
    """Custom type h323MiscH245RoundTripTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_H323MiscH245RoundTripTime_Type.__name__ = "Unsigned32"
_H323MiscH245RoundTripTime_Object = MibScalar
h323MiscH245RoundTripTime = _H323MiscH245RoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 15, 7),
    _H323MiscH245RoundTripTime_Type()
)
h323MiscH245RoundTripTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MiscH245RoundTripTime.setStatus("obsolete")


class _H323MiscProgressBehavior_Type(Integer32):
    """Custom type h323MiscProgressBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alert", 0),
          ("progress", 1))
    )


_H323MiscProgressBehavior_Type.__name__ = "Integer32"
_H323MiscProgressBehavior_Object = MibScalar
h323MiscProgressBehavior = _H323MiscProgressBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 3, 1, 3, 15, 8),
    _H323MiscProgressBehavior_Type()
)
h323MiscProgressBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323MiscProgressBehavior.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AcGateway",
    **{"acGateway": acGateway,
       "gwConfiguration": gwConfiguration,
       "common": common,
       "channelsSetting": channelsSetting,
       "channelsSettingSelectMode": channelsSettingSelectMode,
       "channelsTable": channelsTable,
       "channelsEntry": channelsEntry,
       "channelsIndex": channelsIndex,
       "channelsRowStatus": channelsRowStatus,
       "channelsAction": channelsAction,
       "channelsActionResult": channelsActionResult,
       "channelsTrunkID": channelsTrunkID,
       "channelsStartingCh": channelsStartingCh,
       "channelsLastCh": channelsLastCh,
       "channelsStartingPhoneNum": channelsStartingPhoneNum,
       "channelsTrunkGroupID": channelsTrunkGroupID,
       "channelsProfileID": channelsProfileID,
       "channelsLastTrunkID": channelsLastTrunkID,
       "channelsModule": channelsModule,
       "trunkGroupSettingsTable": trunkGroupSettingsTable,
       "trunkGroupSettingsEntry": trunkGroupSettingsEntry,
       "trunkGroupSettingsIndex": trunkGroupSettingsIndex,
       "trunkGroupSettingsRowStatus": trunkGroupSettingsRowStatus,
       "trunkGroupSettingsAction": trunkGroupSettingsAction,
       "trunkGroupSettingsActionResult": trunkGroupSettingsActionResult,
       "trunkGroupSettingsTrunkGroupID": trunkGroupSettingsTrunkGroupID,
       "trunkGroupSettingsChannelSelectMode": trunkGroupSettingsChannelSelectMode,
       "trunkGroupSettingsRegistrationMode": trunkGroupSettingsRegistrationMode,
       "trunkGroupSettingsGatewayName": trunkGroupSettingsGatewayName,
       "trunkGroupSettingsContactUser": trunkGroupSettingsContactUser,
       "trunkGroupSettingsServingIPGroup": trunkGroupSettingsServingIPGroup,
       "trunkGroupSettingsMwiInterrogationType": trunkGroupSettingsMwiInterrogationType,
       "manipulationAndRouting": manipulationAndRouting,
       "manipulationAndRoutingModeTel2Ip": manipulationAndRoutingModeTel2Ip,
       "manipulationAndRoutingModeIp2Tel": manipulationAndRoutingModeIp2Tel,
       "manipulationAndRoutingFilterCalls2Ip": manipulationAndRoutingFilterCalls2Ip,
       "manipulationAndRoutingAltRoutingTel2IpEnable": manipulationAndRoutingAltRoutingTel2IpEnable,
       "manipulationAndRoutingAltRoutingTel2IpMode": manipulationAndRoutingAltRoutingTel2IpMode,
       "manipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall": manipulationAndRoutingAltRoutingTel2IpQosAllowTheNCall,
       "manipulationAndRoutingPreferRouteTable": manipulationAndRoutingPreferRouteTable,
       "manipulationAndRoutingRedundantRoutingMode": manipulationAndRoutingRedundantRoutingMode,
       "manipulationAndRoutingAltRoutingTel2IpConnMethod": manipulationAndRoutingAltRoutingTel2IpConnMethod,
       "manipulationAndRoutingSIPReRoutingMode": manipulationAndRoutingSIPReRoutingMode,
       "manipulationAndRoutingAltRoutingToneDuration": manipulationAndRoutingAltRoutingToneDuration,
       "manipulationAndRoutingAltRoutingTel2IpKeepAliveTime": manipulationAndRoutingAltRoutingTel2IpKeepAliveTime,
       "routing": routing,
       "tel2IPRoutingTable": tel2IPRoutingTable,
       "tel2IPRoutingEntry": tel2IPRoutingEntry,
       "tel2IPRoutingIndex": tel2IPRoutingIndex,
       "tel2IPRoutingRowStatus": tel2IPRoutingRowStatus,
       "tel2IPRoutingAction": tel2IPRoutingAction,
       "tel2IPRoutingActionResult": tel2IPRoutingActionResult,
       "tel2IPRoutingPrefix": tel2IPRoutingPrefix,
       "tel2IPRoutingAddress": tel2IPRoutingAddress,
       "tel2IPRoutingSrcPrefix": tel2IPRoutingSrcPrefix,
       "tel2IPRoutingProfileID": tel2IPRoutingProfileID,
       "tel2IPRoutingChargeCode": tel2IPRoutingChargeCode,
       "tel2IPRoutingDestPort": tel2IPRoutingDestPort,
       "tel2IPRoutingSourceIPGroupID": tel2IPRoutingSourceIPGroupID,
       "tel2IPRoutingDestHostPrefix": tel2IPRoutingDestHostPrefix,
       "tel2IPRoutingDestIPGroupID": tel2IPRoutingDestIPGroupID,
       "tel2IPRoutingSourceHostPrefix": tel2IPRoutingSourceHostPrefix,
       "tel2IPRoutingTransportType": tel2IPRoutingTransportType,
       "tel2IPRoutingSourceTrunkGroupID": tel2IPRoutingSourceTrunkGroupID,
       "iP2TelRoutingTable": iP2TelRoutingTable,
       "iP2TelRoutingEntry": iP2TelRoutingEntry,
       "iP2TelRoutingIndex": iP2TelRoutingIndex,
       "iP2TelRoutingRowStatus": iP2TelRoutingRowStatus,
       "iP2TelRoutingAction": iP2TelRoutingAction,
       "iP2TelRoutingActionResult": iP2TelRoutingActionResult,
       "iP2TelRoutingPrefix": iP2TelRoutingPrefix,
       "iP2TelRoutingTrunkGroupID": iP2TelRoutingTrunkGroupID,
       "iP2TelRoutingSrcPrefix": iP2TelRoutingSrcPrefix,
       "iP2TelRoutingAddress": iP2TelRoutingAddress,
       "iP2TelRoutingProfileID": iP2TelRoutingProfileID,
       "iP2TelRoutingSourceIPGroupID": iP2TelRoutingSourceIPGroupID,
       "iP2TelRoutingDestHostPrefix": iP2TelRoutingDestHostPrefix,
       "iP2TelRoutingSourceHostPrefix": iP2TelRoutingSourceHostPrefix,
       "dnsInfoTable": dnsInfoTable,
       "dnsInfoEntry": dnsInfoEntry,
       "dnsInfoIndex": dnsInfoIndex,
       "dnsInfoRowStatus": dnsInfoRowStatus,
       "dnsInfoAction": dnsInfoAction,
       "dnsInfoActionResult": dnsInfoActionResult,
       "dnsInfoDomainName": dnsInfoDomainName,
       "dnsInfoFirstIPAddress": dnsInfoFirstIPAddress,
       "dnsInfoSecondIPAddress": dnsInfoSecondIPAddress,
       "dnsInfoThirdIPAddress": dnsInfoThirdIPAddress,
       "dnsInfoFourthIPAddress": dnsInfoFourthIPAddress,
       "srvInfoTable": srvInfoTable,
       "srvInfoEntry": srvInfoEntry,
       "srvInfoIndex": srvInfoIndex,
       "srvInfoRecordNum": srvInfoRecordNum,
       "srvInfoRowStatus": srvInfoRowStatus,
       "srvInfoAction": srvInfoAction,
       "srvInfoActionResult": srvInfoActionResult,
       "srvInfoInternalDomainName": srvInfoInternalDomainName,
       "srvInfoTransportType": srvInfoTransportType,
       "srvInfoDNSName": srvInfoDNSName,
       "srvInfoPriority": srvInfoPriority,
       "srvInfoWeight": srvInfoWeight,
       "srvInfoPort": srvInfoPort,
       "srvInfoDNSName2": srvInfoDNSName2,
       "srvInfoPriority2": srvInfoPriority2,
       "srvInfoWeight2": srvInfoWeight2,
       "srvInfoPort2": srvInfoPort2,
       "srvInfoDNSName3": srvInfoDNSName3,
       "srvInfoPriority3": srvInfoPriority3,
       "srvInfoWeight3": srvInfoWeight3,
       "srvInfoPort3": srvInfoPort3,
       "forwardOnBusyTrunkDestTable": forwardOnBusyTrunkDestTable,
       "forwardOnBusyTrunkDestEntry": forwardOnBusyTrunkDestEntry,
       "forwardOnBusyTrunkDestIndex": forwardOnBusyTrunkDestIndex,
       "forwardOnBusyTrunkDestRowStatus": forwardOnBusyTrunkDestRowStatus,
       "forwardOnBusyTrunkDestAction": forwardOnBusyTrunkDestAction,
       "forwardOnBusyTrunkDestActionResult": forwardOnBusyTrunkDestActionResult,
       "forwardOnBusyTrunkDestTrunkGroupId": forwardOnBusyTrunkDestTrunkGroupId,
       "forwardOnBusyTrunkDestForwardDestination": forwardOnBusyTrunkDestForwardDestination,
       "altRouteCause": altRouteCause,
       "altRouteCauseIP2TELTable": altRouteCauseIP2TELTable,
       "altRouteCauseIP2TELEntry": altRouteCauseIP2TELEntry,
       "altRouteCauseIP2TELIndex": altRouteCauseIP2TELIndex,
       "altRouteCauseIP2TELRowStatus": altRouteCauseIP2TELRowStatus,
       "altRouteCauseIP2TELAction": altRouteCauseIP2TELAction,
       "altRouteCauseIP2TELActionResult": altRouteCauseIP2TELActionResult,
       "altRouteCauseIP2TELReleaseCause": altRouteCauseIP2TELReleaseCause,
       "altRouteCauseTEL2IPTable": altRouteCauseTEL2IPTable,
       "altRouteCauseTEL2IPEntry": altRouteCauseTEL2IPEntry,
       "altRouteCauseTEL2IPIndex": altRouteCauseTEL2IPIndex,
       "altRouteCauseTEL2IPRowStatus": altRouteCauseTEL2IPRowStatus,
       "altRouteCauseTEL2IPAction": altRouteCauseTEL2IPAction,
       "altRouteCauseTEL2IPActionResult": altRouteCauseTEL2IPActionResult,
       "altRouteCauseTEL2IPReleaseCause": altRouteCauseTEL2IPReleaseCause,
       "routingEnableDigitDelivery2IP": routingEnableDigitDelivery2IP,
       "routingSourceIPAddressInput": routingSourceIPAddressInput,
       "manipulation": manipulation,
       "manipulationRemovePrefix": manipulationRemovePrefix,
       "manipulationAddTrunkGroupAsPrefix": manipulationAddTrunkGroupAsPrefix,
       "manipulationAddPortAsPrefix": manipulationAddPortAsPrefix,
       "manipulationReplaceEmptyDstWithPortNumber": manipulationReplaceEmptyDstWithPortNumber,
       "manipulationCIDNotification": manipulationCIDNotification,
       "manipulationUseSourceNumberAsDisplayName": manipulationUseSourceNumberAsDisplayName,
       "manipulationAddNPIandTON2CalledNumber": manipulationAddNPIandTON2CalledNumber,
       "manipulationAddNPIandTON2CallingNumber": manipulationAddNPIandTON2CallingNumber,
       "manipulationUseDisplayNameAsSourceNumber": manipulationUseDisplayNameAsSourceNumber,
       "manipulationAddPrefixToRedirectNumber": manipulationAddPrefixToRedirectNumber,
       "manipulationAddPhoneContextAsPrefix": manipulationAddPhoneContextAsPrefix,
       "manipulationBlindTransferAddPrefix": manipulationBlindTransferAddPrefix,
       "manipulationSourceMode": manipulationSourceMode,
       "manipulationAddTrunkGroupAsPrefixToSource": manipulationAddTrunkGroupAsPrefixToSource,
       "manipulationSetTel2IpRedirectReason": manipulationSetTel2IpRedirectReason,
       "manipulationSetIp2TelRedirectReason": manipulationSetIp2TelRedirectReason,
       "manipulationSetIp2TelRedirectScreeningIndicator": manipulationSetIp2TelRedirectScreeningIndicator,
       "dstIP2TELTable": dstIP2TELTable,
       "dstIP2TELEntry": dstIP2TELEntry,
       "dstIP2TELIndex": dstIP2TELIndex,
       "dstIP2TELRowStatus": dstIP2TELRowStatus,
       "dstIP2TELAction": dstIP2TELAction,
       "dstIP2TELActionResult": dstIP2TELActionResult,
       "dstIP2TELPrefix": dstIP2TELPrefix,
       "dstIP2TELNumOfStrippedDigits": dstIP2TELNumOfStrippedDigits,
       "dstIP2TELPrefixToAdd": dstIP2TELPrefixToAdd,
       "dstIP2TELNumOfDigitsToLeave": dstIP2TELNumOfDigitsToLeave,
       "dstIP2TELNumberPlan": dstIP2TELNumberPlan,
       "dstIP2TELNumberType": dstIP2TELNumberType,
       "dstIP2TELSourcePrefix": dstIP2TELSourcePrefix,
       "dstIP2TELSourceIP": dstIP2TELSourceIP,
       "dstIP2TELNumOfDigitsToRemFromRight": dstIP2TELNumOfDigitsToRemFromRight,
       "dstIP2TELSuffix2Add": dstIP2TELSuffix2Add,
       "dstIP2TELIsPresentationRestricted": dstIP2TELIsPresentationRestricted,
       "dstTEL2IPTable": dstTEL2IPTable,
       "dstTEL2IPEntry": dstTEL2IPEntry,
       "dstTEL2IPIndex": dstTEL2IPIndex,
       "dstTEL2IPRowStatus": dstTEL2IPRowStatus,
       "dstTEL2IPAction": dstTEL2IPAction,
       "dstTEL2IPActionResult": dstTEL2IPActionResult,
       "dstTEL2IPPrefix": dstTEL2IPPrefix,
       "dstTEL2IPNumOfStrippedDigits": dstTEL2IPNumOfStrippedDigits,
       "dstTEL2IPPrefixToAdd": dstTEL2IPPrefixToAdd,
       "dstTEL2IPNumOfDigitsToLeave": dstTEL2IPNumOfDigitsToLeave,
       "dstTEL2IPNumberPlan": dstTEL2IPNumberPlan,
       "dstTEL2IPNumberType": dstTEL2IPNumberType,
       "dstTEL2IPSourcePrefix": dstTEL2IPSourcePrefix,
       "dstTEL2IPNumOfDigitsToRemFromRight": dstTEL2IPNumOfDigitsToRemFromRight,
       "dstTEL2IPSuffix2Add": dstTEL2IPSuffix2Add,
       "dstTEL2IPIsPresentationRestricted": dstTEL2IPIsPresentationRestricted,
       "dstTEL2IPSourceIPAddress": dstTEL2IPSourceIPAddress,
       "dstTEL2IPSourceTrunkGroupID": dstTEL2IPSourceTrunkGroupID,
       "dstTEL2IPSourceIPGroupID": dstTEL2IPSourceIPGroupID,
       "srcIP2TELTable": srcIP2TELTable,
       "srcIP2TELEntry": srcIP2TELEntry,
       "srcIP2TELIndex": srcIP2TELIndex,
       "srcIP2TELRowStatus": srcIP2TELRowStatus,
       "srcIP2TELAction": srcIP2TELAction,
       "srcIP2TELActionResult": srcIP2TELActionResult,
       "srcIP2TELPrefix": srcIP2TELPrefix,
       "srcIP2TELNumOfStrippedDigits": srcIP2TELNumOfStrippedDigits,
       "srcIP2TELPrefixToAdd": srcIP2TELPrefixToAdd,
       "srcIP2TELNumOfDigitsToLeave": srcIP2TELNumOfDigitsToLeave,
       "srcIP2TELNumberPlan": srcIP2TELNumberPlan,
       "srcIP2TELNumberType": srcIP2TELNumberType,
       "srcIP2TELDestPrefix": srcIP2TELDestPrefix,
       "srcIP2TELPresentation": srcIP2TELPresentation,
       "srcIP2TELNumOfDigitsToRemFromRight": srcIP2TELNumOfDigitsToRemFromRight,
       "srcIP2TELSuffix2Add": srcIP2TELSuffix2Add,
       "srcIP2TELSourceIPAddress": srcIP2TELSourceIPAddress,
       "srcTEL2IPTable": srcTEL2IPTable,
       "srcTEL2IPEntry": srcTEL2IPEntry,
       "srcTEL2IPIndex": srcTEL2IPIndex,
       "srcTEL2IPRowStatus": srcTEL2IPRowStatus,
       "srcTEL2IPAction": srcTEL2IPAction,
       "srcTEL2IPActionResult": srcTEL2IPActionResult,
       "srcTEL2IPPrefix": srcTEL2IPPrefix,
       "srcTEL2IPNumOfStrippedDigits": srcTEL2IPNumOfStrippedDigits,
       "srcTEL2IPPrefixToAdd": srcTEL2IPPrefixToAdd,
       "srcTEL2IPNumOfDigitsToLeave": srcTEL2IPNumOfDigitsToLeave,
       "srcTEL2IPNumberPlan": srcTEL2IPNumberPlan,
       "srcTEL2IPNumberType": srcTEL2IPNumberType,
       "srcTEL2IPDestPrefix": srcTEL2IPDestPrefix,
       "srcTEL2IPPresentation": srcTEL2IPPresentation,
       "srcTEL2IPNumOfDigitsToRemFromRight": srcTEL2IPNumOfDigitsToRemFromRight,
       "srcTEL2IPSuffix2Add": srcTEL2IPSuffix2Add,
       "srcTEL2IPSourceIPAddress": srcTEL2IPSourceIPAddress,
       "srcTEL2IPSourceTrunkGroupID": srcTEL2IPSourceTrunkGroupID,
       "srcTEL2IPSourceIPGroupID": srcTEL2IPSourceIPGroupID,
       "phoneContextTable": phoneContextTable,
       "phoneContextEntry": phoneContextEntry,
       "phoneContextIndex": phoneContextIndex,
       "phoneContextRowStatus": phoneContextRowStatus,
       "phoneContextAction": phoneContextAction,
       "phoneContextActionResult": phoneContextActionResult,
       "phoneContextNPI": phoneContextNPI,
       "phoneContextTON": phoneContextTON,
       "phoneContextPhoneContext": phoneContextPhoneContext,
       "redirectNumberMapIp2TelTable": redirectNumberMapIp2TelTable,
       "redirectNumberMapIp2TelEntry": redirectNumberMapIp2TelEntry,
       "redirectNumberMapIp2TelIndex": redirectNumberMapIp2TelIndex,
       "redirectNumberMapIp2TelRowStatus": redirectNumberMapIp2TelRowStatus,
       "redirectNumberMapIp2TelAction": redirectNumberMapIp2TelAction,
       "redirectNumberMapIp2TelActionResult": redirectNumberMapIp2TelActionResult,
       "redirectNumberMapIp2TelDestinationPrefix": redirectNumberMapIp2TelDestinationPrefix,
       "redirectNumberMapIp2TelRedirectPrefix": redirectNumberMapIp2TelRedirectPrefix,
       "redirectNumberMapIp2TelSourceAddress": redirectNumberMapIp2TelSourceAddress,
       "redirectNumberMapIp2TelNumberType": redirectNumberMapIp2TelNumberType,
       "redirectNumberMapIp2TelNumberPlan": redirectNumberMapIp2TelNumberPlan,
       "redirectNumberMapIp2TelRemoveFromLeft": redirectNumberMapIp2TelRemoveFromLeft,
       "redirectNumberMapIp2TelRemoveFromRight": redirectNumberMapIp2TelRemoveFromRight,
       "redirectNumberMapIp2TelLeaveFromRight": redirectNumberMapIp2TelLeaveFromRight,
       "redirectNumberMapIp2TelPrefixToAdd": redirectNumberMapIp2TelPrefixToAdd,
       "redirectNumberMapIp2TelSuffixToAdd": redirectNumberMapIp2TelSuffixToAdd,
       "redirectNumberMapIp2TelIsPresentationRestricted": redirectNumberMapIp2TelIsPresentationRestricted,
       "redirectNumberMapIp2TelSrcTrunkGroupID": redirectNumberMapIp2TelSrcTrunkGroupID,
       "redirectNumberMapIp2TelSrcIPGroupID": redirectNumberMapIp2TelSrcIPGroupID,
       "redirectNumberMapTel2IpTable": redirectNumberMapTel2IpTable,
       "redirectNumberMapTel2IpEntry": redirectNumberMapTel2IpEntry,
       "redirectNumberMapTel2IpIndex": redirectNumberMapTel2IpIndex,
       "redirectNumberMapTel2IpRowStatus": redirectNumberMapTel2IpRowStatus,
       "redirectNumberMapTel2IpAction": redirectNumberMapTel2IpAction,
       "redirectNumberMapTel2IpActionResult": redirectNumberMapTel2IpActionResult,
       "redirectNumberMapTel2IpDestinationPrefix": redirectNumberMapTel2IpDestinationPrefix,
       "redirectNumberMapTel2IpRedirectPrefix": redirectNumberMapTel2IpRedirectPrefix,
       "redirectNumberMapTel2IpSourceAddress": redirectNumberMapTel2IpSourceAddress,
       "redirectNumberMapTel2IpNumberType": redirectNumberMapTel2IpNumberType,
       "redirectNumberMapTel2IpNumberPlan": redirectNumberMapTel2IpNumberPlan,
       "redirectNumberMapTel2IpRemoveFromLeft": redirectNumberMapTel2IpRemoveFromLeft,
       "redirectNumberMapTel2IpRemoveFromRight": redirectNumberMapTel2IpRemoveFromRight,
       "redirectNumberMapTel2IpLeaveFromRight": redirectNumberMapTel2IpLeaveFromRight,
       "redirectNumberMapTel2IpPrefixToAdd": redirectNumberMapTel2IpPrefixToAdd,
       "redirectNumberMapTel2IpSuffixToAdd": redirectNumberMapTel2IpSuffixToAdd,
       "redirectNumberMapTel2IpIsPresentationRestricted": redirectNumberMapTel2IpIsPresentationRestricted,
       "redirectNumberMapTel2IpSrcTrunkGroupID": redirectNumberMapTel2IpSrcTrunkGroupID,
       "redirectNumberMapTel2IpSrcIPGroupID": redirectNumberMapTel2IpSrcIPGroupID,
       "connectivityQos": connectivityQos,
       "connectivityQosMaxAllowedPL": connectivityQosMaxAllowedPL,
       "connectivityQosMaxAllowedDelay": connectivityQosMaxAllowedDelay,
       "connectivityQosEffectivePeriod": connectivityQosEffectivePeriod,
       "connectivityQosSamplesToAvarage": connectivityQosSamplesToAvarage,
       "digitalGW": digitalGW,
       "digitalGWBChannelNegotiation": digitalGWBChannelNegotiation,
       "digitalGWSwapRedirectNumber": digitalGWSwapRedirectNumber,
       "digitalGWEnableTransferCap": digitalGWEnableTransferCap,
       "digitalGWR2Category": digitalGWR2Category,
       "digitalGWISDNRxOverlap": digitalGWISDNRxOverlap,
       "digitalGWCASSendHookFlash": digitalGWCASSendHookFlash,
       "digitalGWISDNTransferCapability": digitalGWISDNTransferCapability,
       "digitalGWEnableTDMOverIp": digitalGWEnableTDMOverIp,
       "digitalGWTransparentCoderOnDataCall": digitalGWTransparentCoderOnDataCall,
       "digitalGWSupportRedirectInFacility": digitalGWSupportRedirectInFacility,
       "digitalGWPIForDisconnectMsg": digitalGWPIForDisconnectMsg,
       "digitalGWConnectOnProgressInd": digitalGWConnectOnProgressInd,
       "digitalGWLocalISDNRBSource": digitalGWLocalISDNRBSource,
       "digitalGWEnableUuiTel2Ip": digitalGWEnableUuiTel2Ip,
       "digitalGWEnableUuiIp2Tel": digitalGWEnableUuiIp2Tel,
       "digitalGWSendISDNTransferOnConnect": digitalGWSendISDNTransferOnConnect,
       "digitalGWEnableISDNTunnelingTel2Ip": digitalGWEnableISDNTunnelingTel2Ip,
       "digitalGWEnableISDNTunnelingIp2Tel": digitalGWEnableISDNTunnelingIp2Tel,
       "digitalGWEnableCallingPartyCategory": digitalGWEnableCallingPartyCategory,
       "iE": iE,
       "iEAddIEInSetup": iEAddIEInSetup,
       "iESendIEOnTG": iESendIEOnTG,
       "iSDNRxOverlapTable": iSDNRxOverlapTable,
       "iSDNRxOverlapEntry": iSDNRxOverlapEntry,
       "iSDNRxOverlapIndex": iSDNRxOverlapIndex,
       "iSDNRxOverlapEnable": iSDNRxOverlapEnable,
       "trunkTransferTable": trunkTransferTable,
       "trunkTransferEntry": trunkTransferEntry,
       "trunkTransferIndex": trunkTransferIndex,
       "trunkTransferMode": trunkTransferMode,
       "progressIndicatorToISDNTable": progressIndicatorToISDNTable,
       "progressIndicatorToISDNEntry": progressIndicatorToISDNEntry,
       "progressIndicatorToISDNIndex": progressIndicatorToISDNIndex,
       "progressIndicatorToISDNValue": progressIndicatorToISDNValue,
       "playRBToneToTrunkTable": playRBToneToTrunkTable,
       "playRBToneToTrunkEntry": playRBToneToTrunkEntry,
       "playRBToneToTrunkIndex": playRBToneToTrunkIndex,
       "playRBToneToTrunkValue": playRBToneToTrunkValue,
       "iSDNTransferCapabilityTable": iSDNTransferCapabilityTable,
       "iSDNTransferCapabilityEntry": iSDNTransferCapabilityEntry,
       "iSDNTransferCapabilityIndex": iSDNTransferCapabilityIndex,
       "iSDNTransferCapabilityValue": iSDNTransferCapabilityValue,
       "localISDNRBSourceTable": localISDNRBSourceTable,
       "localISDNRBSourceEntry": localISDNRBSourceEntry,
       "localISDNRBSourceIndex": localISDNRBSourceIndex,
       "localISDNRBSourceValue": localISDNRBSourceValue,
       "pIForDisconnectMsgTable": pIForDisconnectMsgTable,
       "pIForDisconnectMsgEntry": pIForDisconnectMsgEntry,
       "pIForDisconnectMsgIndex": pIForDisconnectMsgIndex,
       "pIForDisconnectMsgValue": pIForDisconnectMsgValue,
       "pSTNAlertTimeoutTable": pSTNAlertTimeoutTable,
       "pSTNAlertTimeoutEntry": pSTNAlertTimeoutEntry,
       "pSTNAlertTimeoutIndex": pSTNAlertTimeoutIndex,
       "pSTNAlertTimeoutValue": pSTNAlertTimeoutValue,
       "mlpp": mlpp,
       "mlppCallPriorityMode": mlppCallPriorityMode,
       "mlppDefaultNamespace": mlppDefaultNamespace,
       "mlppDefaultCallPriority": mlppDefaultCallPriority,
       "mlppDiffServ": mlppDiffServ,
       "mlppPreemptionToneDuration": mlppPreemptionToneDuration,
       "mlppDefaultServiceDomain": mlppDefaultServiceDomain,
       "mlppNormalizedServiceDomain": mlppNormalizedServiceDomain,
       "mlppRoutineRTPDSCP": mlppRoutineRTPDSCP,
       "mlppPriorityRTPDSCP": mlppPriorityRTPDSCP,
       "mlppImmediateRTPDSCP": mlppImmediateRTPDSCP,
       "mlppFlashRTPDSCP": mlppFlashRTPDSCP,
       "mlppFlashOverRTPDSCP": mlppFlashOverRTPDSCP,
       "mlppFlashOverOverRTPDSCP": mlppFlashOverOverRTPDSCP,
       "mlppE911Behavior": mlppE911Behavior,
       "digitalGWPlayRBTOnISDNTransfer": digitalGWPlayRBTOnISDNTransfer,
       "analogGW": analogGW,
       "analogGWEnableReversalPolarity": analogGWEnableReversalPolarity,
       "analogGWEnableCurrentDisconnect": analogGWEnableCurrentDisconnect,
       "analogGWRegretTime": analogGWRegretTime,
       "analogGWHotLineToneDuration": analogGWHotLineToneDuration,
       "fxs": fxs,
       "fxsCutThrough": fxsCutThrough,
       "fxsMeteringMode": fxsMeteringMode,
       "fxsFXSOOSBehavior": fxsFXSOOSBehavior,
       "fxsSetOOSOnRegistrationFail": fxsSetOOSOnRegistrationFail,
       "chargeCodesTable": chargeCodesTable,
       "chargeCodesEntry": chargeCodesEntry,
       "chargeCodesIndex": chargeCodesIndex,
       "chargeCodesRowStatus": chargeCodesRowStatus,
       "chargeCodesAction": chargeCodesAction,
       "chargeCodesActionResult": chargeCodesActionResult,
       "chargeCodesPeriod1EndTime": chargeCodesPeriod1EndTime,
       "chargeCodesPeriod1PulseInterval": chargeCodesPeriod1PulseInterval,
       "chargeCodesPeriod1PulsesOnAnswer": chargeCodesPeriod1PulsesOnAnswer,
       "chargeCodesPeriod2EndTime": chargeCodesPeriod2EndTime,
       "chargeCodesPeriod2PulseInterval": chargeCodesPeriod2PulseInterval,
       "chargeCodesPeriod2PulsesOnAnswer": chargeCodesPeriod2PulsesOnAnswer,
       "chargeCodesPeriod3EndTime": chargeCodesPeriod3EndTime,
       "chargeCodesPeriod3PulseInterval": chargeCodesPeriod3PulseInterval,
       "chargeCodesPeriod3PulsesOnAnswer": chargeCodesPeriod3PulsesOnAnswer,
       "chargeCodesPeriod4EndTime": chargeCodesPeriod4EndTime,
       "chargeCodesPeriod4PulseInterval": chargeCodesPeriod4PulseInterval,
       "chargeCodesPeriod4PulsesOnAnswer": chargeCodesPeriod4PulsesOnAnswer,
       "toneIndexTable": toneIndexTable,
       "toneIndexEntry": toneIndexEntry,
       "toneIndexIndex": toneIndexIndex,
       "toneIndexRowStatus": toneIndexRowStatus,
       "toneIndexAction": toneIndexAction,
       "toneIndexActionResult": toneIndexActionResult,
       "toneIndexFXSPortFirst": toneIndexFXSPortFirst,
       "toneIndexFXSPortLast": toneIndexFXSPortLast,
       "toneIndexSourcePrefix": toneIndexSourcePrefix,
       "toneIndexPriorityIndex": toneIndexPriorityIndex,
       "fxo": fxo,
       "fxoIsTwoStageDial": fxoIsTwoStageDial,
       "fxoWaitForDialTone": fxoWaitForDialTone,
       "fxoWaitForDialTime": fxoWaitForDialTime,
       "fxoBetweenRingTime": fxoBetweenRingTime,
       "fxoEnableVoiceDetection": fxoEnableVoiceDetection,
       "fxoRingsBeforeCallerID": fxoRingsBeforeCallerID,
       "fxoGuardTimeBetweenCalls": fxoGuardTimeBetweenCalls,
       "fxoAutoDialPlayBusyTone": fxoAutoDialPlayBusyTone,
       "dialing": dialing,
       "dialingMaxDigits": dialingMaxDigits,
       "dialingTimeBetweenDigits": dialingTimeBetweenDigits,
       "dialingIsSpecialDigits": dialingIsSpecialDigits,
       "dialingDigitMapping": dialingDigitMapping,
       "dialingEnableDigitDelivery": dialingEnableDigitDelivery,
       "dialingDialPlanIndex": dialingDialPlanIndex,
       "autoDialTable": autoDialTable,
       "autoDialEntry": autoDialEntry,
       "autoDialIndex": autoDialIndex,
       "autoDialIsUsed": autoDialIsUsed,
       "autoDialAction": autoDialAction,
       "autoDialActionResult": autoDialActionResult,
       "autoDialDestPhoneNumber": autoDialDestPhoneNumber,
       "autoDialType": autoDialType,
       "autoDialModule": autoDialModule,
       "autoDialPort": autoDialPort,
       "callerID": callerID,
       "callerIDEnable": callerIDEnable,
       "callerDisplayTable": callerDisplayTable,
       "callerDisplayEntry": callerDisplayEntry,
       "callerDisplayIndex": callerDisplayIndex,
       "callerDisplayIsUsed": callerDisplayIsUsed,
       "callerDisplayAction": callerDisplayAction,
       "callerDisplayActionResult": callerDisplayActionResult,
       "callerDisplayCallerDisplay": callerDisplayCallerDisplay,
       "callerDisplayRestriction": callerDisplayRestriction,
       "callerDisplayModule": callerDisplayModule,
       "callerDisplayPort": callerDisplayPort,
       "callerIDperPortTable": callerIDperPortTable,
       "callerIDperPortEntry": callerIDperPortEntry,
       "callerIDperPortIndex": callerIDperPortIndex,
       "callerIDperPortIsUsed": callerIDperPortIsUsed,
       "callerIDperPortAction": callerIDperPortAction,
       "callerIDperPortActionResult": callerIDperPortActionResult,
       "callerIDperPortEnable": callerIDperPortEnable,
       "callerIDperPortModule": callerIDperPortModule,
       "callerIDperPortPort": callerIDperPortPort,
       "keypadFeatures": keypadFeatures,
       "keypadFeaturesCFUncond": keypadFeaturesCFUncond,
       "keypadFeaturesCFDeact": keypadFeaturesCFDeact,
       "keypadFeaturesCFNoAnswer": keypadFeaturesCFNoAnswer,
       "keypadFeaturesCFBusy": keypadFeaturesCFBusy,
       "keypadFeaturesCLIR": keypadFeaturesCLIR,
       "keypadFeaturesCLIRDeact": keypadFeaturesCLIRDeact,
       "keypadFeaturesHotLine": keypadFeaturesHotLine,
       "keypadFeaturesHotLineDeact": keypadFeaturesHotLineDeact,
       "keypadFeaturesCFBusyOrNoAnswer": keypadFeaturesCFBusyOrNoAnswer,
       "keypadFeaturesCFDoNotDisturb": keypadFeaturesCFDoNotDisturb,
       "keypadFeaturesBlindTransfer": keypadFeaturesBlindTransfer,
       "keypadFeaturesKeypadFeaturesCW": keypadFeaturesKeypadFeaturesCW,
       "keypadFeaturesKeypadFeaturesCWDeact": keypadFeaturesKeypadFeaturesCWDeact,
       "keypadFeaturesRejectAnonymousCall": keypadFeaturesRejectAnonymousCall,
       "keypadFeaturesRejectAnonymousCallDeact": keypadFeaturesRejectAnonymousCallDeact,
       "portName": portName,
       "namesTable": namesTable,
       "namesEntry": namesEntry,
       "namesIndex": namesIndex,
       "namesIsUsed": namesIsUsed,
       "namesAction": namesAction,
       "namesActionResult": namesActionResult,
       "namesPortName": namesPortName,
       "namesModule": namesModule,
       "namesPort": namesPort,
       "dID": dID,
       "dIDEnable": dIDEnable,
       "dIDEnableWink": dIDEnableWink,
       "dIDDelayBeforeDidWink": dIDDelayBeforeDidWink,
       "enableDidPortTable": enableDidPortTable,
       "enableDidPortEntry": enableDidPortEntry,
       "enableDidPortIndex": enableDidPortIndex,
       "enableDidPortIsUsed": enableDidPortIsUsed,
       "enableDidPortAction": enableDidPortAction,
       "enableDidPortActionResult": enableDidPortActionResult,
       "enableDidPortEnable": enableDidPortEnable,
       "enableDidPortModule": enableDidPortModule,
       "enableDidPortPort": enableDidPortPort,
       "enableCallWaitingPerPortTable": enableCallWaitingPerPortTable,
       "enableCallWaitingPerPortEntry": enableCallWaitingPerPortEntry,
       "enableCallWaitingPerPortIndex": enableCallWaitingPerPortIndex,
       "enableCallWaitingPerPortIsUsed": enableCallWaitingPerPortIsUsed,
       "enableCallWaitingPerPortModule": enableCallWaitingPerPortModule,
       "enableCallWaitingPerPortPort": enableCallWaitingPerPortPort,
       "enableCallWaitingPerPortAction": enableCallWaitingPerPortAction,
       "enableCallWaitingPerPortActionResult": enableCallWaitingPerPortActionResult,
       "enableCallWaitingPerPortEnable": enableCallWaitingPerPortEnable,
       "mediaGW": mediaGW,
       "mediaGWMediaChannels": mediaGWMediaChannels,
       "conference": conference,
       "conferenceID": conferenceID,
       "conferenceBipOnConference": conferenceBipOnConference,
       "conferenceEnableDTMFReporting": conferenceEnableDTMFReporting,
       "conferenceEnableDTMFClamping": conferenceEnableDTMFClamping,
       "conference3WayMode": conference3WayMode,
       "conferenceMaxInBoardCalls": conferenceMaxInBoardCalls,
       "acTWCnonAllocateablePortsTable": acTWCnonAllocateablePortsTable,
       "acTWCnonAllocateablePortsEntry": acTWCnonAllocateablePortsEntry,
       "acTWCnonAllocateablePortsIndex": acTWCnonAllocateablePortsIndex,
       "acTWCnonAllocateablePortsNumber": acTWCnonAllocateablePortsNumber,
       "announcement": announcement,
       "announcementID": announcementID,
       "announcementNumOfEndPoints": announcementNumOfEndPoints,
       "announcementToneID": announcementToneID,
       "streaming": streaming,
       "streamingID": streamingID,
       "streamingNumOfEndPoints": streamingNumOfEndPoints,
       "streamingRecordScriptPath": streamingRecordScriptPath,
       "streamingMediaID": streamingMediaID,
       "streamingStopRecordingOnNoSpeachTimeout": streamingStopRecordingOnNoSpeachTimeout,
       "streamingPlayFromID": streamingPlayFromID,
       "streamingRecordToID": streamingRecordToID,
       "streamingNetAnnAnncID": streamingNetAnnAnncID,
       "streamingMscmlID": streamingMscmlID,
       "streamingMonitorID": streamingMonitorID,
       "vxml": vxml,
       "vxmlID": vxmlID,
       "vxmlNumOfEndPoints": vxmlNumOfEndPoints,
       "calea": calea,
       "caleaInterceptionDirection": caleaInterceptionDirection,
       "transcoding": transcoding,
       "transcodingID": transcodingID,
       "coders": coders,
       "codersTable": codersTable,
       "codersEntry": codersEntry,
       "codersIndex": codersIndex,
       "codersRowStatus": codersRowStatus,
       "codersAction": codersAction,
       "codersActionResult": codersActionResult,
       "codersName": codersName,
       "codersInterval": codersInterval,
       "codersRate": codersRate,
       "codersPayloadType": codersPayloadType,
       "codersSilenceSuppression": codersSilenceSuppression,
       "codersGroup0Table": codersGroup0Table,
       "codersGroup0Entry": codersGroup0Entry,
       "codersGroup0Index": codersGroup0Index,
       "codersGroup0RowStatus": codersGroup0RowStatus,
       "codersGroup0Action": codersGroup0Action,
       "codersGroup0ActionRes": codersGroup0ActionRes,
       "codersGroup0Name": codersGroup0Name,
       "codersGroup0PacketizationTime": codersGroup0PacketizationTime,
       "codersGroup0Rate": codersGroup0Rate,
       "codersGroup0PayloadType": codersGroup0PayloadType,
       "codersGroup0SilenceSuppression": codersGroup0SilenceSuppression,
       "codersGroup1Table": codersGroup1Table,
       "codersGroup1Entry": codersGroup1Entry,
       "codersGroup1Index": codersGroup1Index,
       "codersGroup1RowStatus": codersGroup1RowStatus,
       "codersGroup1Action": codersGroup1Action,
       "codersGroup1ActionRes": codersGroup1ActionRes,
       "codersGroup1Name": codersGroup1Name,
       "codersGroup1PacketizationTime": codersGroup1PacketizationTime,
       "codersGroup1Rate": codersGroup1Rate,
       "codersGroup1PayloadType": codersGroup1PayloadType,
       "codersGroup1SilenceSuppression": codersGroup1SilenceSuppression,
       "codersGroup2Table": codersGroup2Table,
       "codersGroup2Entry": codersGroup2Entry,
       "codersGroup2Index": codersGroup2Index,
       "codersGroup2RowStatus": codersGroup2RowStatus,
       "codersGroup2Action": codersGroup2Action,
       "codersGroup2ActionRes": codersGroup2ActionRes,
       "codersGroup2Name": codersGroup2Name,
       "codersGroup2PacketizationTime": codersGroup2PacketizationTime,
       "codersGroup2Rate": codersGroup2Rate,
       "codersGroup2PayloadType": codersGroup2PayloadType,
       "codersGroup2SilenceSuppression": codersGroup2SilenceSuppression,
       "codersGroup3Table": codersGroup3Table,
       "codersGroup3Entry": codersGroup3Entry,
       "codersGroup3Index": codersGroup3Index,
       "codersGroup3RowStatus": codersGroup3RowStatus,
       "codersGroup3Action": codersGroup3Action,
       "codersGroup3ActionRes": codersGroup3ActionRes,
       "codersGroup3Name": codersGroup3Name,
       "codersGroup3PacketizationTime": codersGroup3PacketizationTime,
       "codersGroup3Rate": codersGroup3Rate,
       "codersGroup3PayloadType": codersGroup3PayloadType,
       "codersGroup3SilenceSuppression": codersGroup3SilenceSuppression,
       "codersGroup4Table": codersGroup4Table,
       "codersGroup4Entry": codersGroup4Entry,
       "codersGroup4Index": codersGroup4Index,
       "codersGroup4RowStatus": codersGroup4RowStatus,
       "codersGroup4Action": codersGroup4Action,
       "codersGroup4ActionRes": codersGroup4ActionRes,
       "codersGroup4Name": codersGroup4Name,
       "codersGroup4PacketizationTime": codersGroup4PacketizationTime,
       "codersGroup4Rate": codersGroup4Rate,
       "codersGroup4PayloadType": codersGroup4PayloadType,
       "codersGroup4SilenceSuppression": codersGroup4SilenceSuppression,
       "supServices": supServices,
       "supServicesEnableHold": supServicesEnableHold,
       "supServicesNameID": supServicesNameID,
       "supServicesHoldFormat": supServicesHoldFormat,
       "supServicesSendMeteringMessageToIP": supServicesSendMeteringMessageToIP,
       "supServicesHeldTimeout": supServicesHeldTimeout,
       "supServicesHookFlashCode": supServicesHookFlashCode,
       "supServicesCHRRTimeout": supServicesCHRRTimeout,
       "supServicesEnableHold2ISDN": supServicesEnableHold2ISDN,
       "supServicesEnableMOH": supServicesEnableMOH,
       "transfer": transfer,
       "transferEnable": transferEnable,
       "transferXferPrefix": transferXferPrefix,
       "callWaiting": callWaiting,
       "callWaitingEnable": callWaitingEnable,
       "callWaitingNumberOfIndications": callWaitingNumberOfIndications,
       "callWaitingTimeBetweenIndications": callWaitingTimeBetweenIndications,
       "callWaitingWaitingBeepDuration": callWaitingWaitingBeepDuration,
       "callWaitingTimeBeforeWaitingIndications": callWaitingTimeBeforeWaitingIndications,
       "forwardSettings": forwardSettings,
       "forwardSettingsEnable": forwardSettingsEnable,
       "forwardTable": forwardTable,
       "forwardEntry": forwardEntry,
       "forwardIndex": forwardIndex,
       "forwardIsUsed": forwardIsUsed,
       "forwardAction": forwardAction,
       "forwardActionResult": forwardActionResult,
       "forwardForwardType": forwardForwardType,
       "forwardForwardedToNumber": forwardForwardedToNumber,
       "forwardTimeForNoReply": forwardTimeForNoReply,
       "forwardModule": forwardModule,
       "forwardPort": forwardPort,
       "mWI": mWI,
       "mWIEnable": mWIEnable,
       "mWIAnalogLamp": mWIAnalogLamp,
       "mWIDisplay": mWIDisplay,
       "mWIServerIP": mWIServerIP,
       "mWIExpirationTime": mWIExpirationTime,
       "mWIServerTransportType": mWIServerTransportType,
       "supServicesConference": supServicesConference,
       "supServicesConferenceEnable3Way": supServicesConferenceEnable3Way,
       "supServicesConferenceEstablishCode": supServicesConferenceEstablishCode,
       "supServicesBlindTransferDisconnectTimeout": supServicesBlindTransferDisconnectTimeout,
       "tones": tones,
       "tonesTimeForReorderTone": tonesTimeForReorderTone,
       "tonesTimeForDialTone": tonesTimeForDialTone,
       "tonesPlayRBTone2Ip": tonesPlayRBTone2Ip,
       "tonesPlayRBTone2Tel": tonesPlayRBTone2Tel,
       "tonesStutterToneDuration": tonesStutterToneDuration,
       "tonesPlayRBToneXferSuccess": tonesPlayRBToneXferSuccess,
       "tonesFirstCallRBTId": tonesFirstCallRBTId,
       "tonesPrecedenceRingingType": tonesPrecedenceRingingType,
       "tonesFirstCallWaitingToneID": tonesFirstCallWaitingToneID,
       "tonesEnableComfortTone": tonesEnableComfortTone,
       "logger": logger,
       "loggerGwAppCdrReportLevel": loggerGwAppCdrReportLevel,
       "loggerGwDebugLevel": loggerGwDebugLevel,
       "loggerCDRSyslogServerIP": loggerCDRSyslogServerIP,
       "progressIndicators": progressIndicators,
       "progressIndicators2ISDN": progressIndicators2ISDN,
       "progressIndicators2IP": progressIndicators2IP,
       "screeningIndicators": screeningIndicators,
       "screeningIndicators2Ip": screeningIndicators2Ip,
       "screeningIndicators2ISDN": screeningIndicators2ISDN,
       "misc": misc,
       "miscDisconnectOnBusyTone": miscDisconnectOnBusyTone,
       "miscDisconnectOnSilence": miscDisconnectOnSilence,
       "miscEnableBusyOut": miscEnableBusyOut,
       "miscSecureCallsFromIp": miscSecureCallsFromIp,
       "miscStaticNATIP": miscStaticNATIP,
       "miscSilenceDisconnectTimeout": miscSilenceDisconnectTimeout,
       "miscIsFaxUsed": miscIsFaxUsed,
       "miscDelayTime": miscDelayTime,
       "miscDetFaxOnAnswerTone": miscDetFaxOnAnswerTone,
       "miscDefaultReleaseCause": miscDefaultReleaseCause,
       "miscT38UseRTPPort": miscT38UseRTPPort,
       "miscRFC2833PayloadType": miscRFC2833PayloadType,
       "miscIsCiscoSceMode": miscIsCiscoSceMode,
       "miscDisconnectOnDialTone": miscDisconnectOnDialTone,
       "miscEnableSemiAttendedTransfer": miscEnableSemiAttendedTransfer,
       "miscHookFlashCodeIP": miscHookFlashCodeIP,
       "miscEnableFaxRerouting": miscEnableFaxRerouting,
       "miscT38MaxDatagramSize": miscT38MaxDatagramSize,
       "miscIsdnDisconnectOnBusyTone": miscIsdnDisconnectOnBusyTone,
       "miscFaxCNGMode": miscFaxCNGMode,
       "miscGracefulBusyOutTimeout": miscGracefulBusyOutTimeout,
       "miscT38FaxMaxBufferSize": miscT38FaxMaxBufferSize,
       "miscReliableConnectionPersistentMode": miscReliableConnectionPersistentMode,
       "miscWANIPAddress": miscWANIPAddress,
       "miscEnableDelayedOffer": miscEnableDelayedOffer,
       "miscEnableNRTSubscription": miscEnableNRTSubscription,
       "miscASSubscribeIPGroupID": miscASSubscribeIPGroupID,
       "miscNRTSubscriptionRetryTime": miscNRTSubscriptionRetryTime,
       "miscCallForwardRingToneID": miscCallForwardRingToneID,
       "miscKeyCallPickup": miscKeyCallPickup,
       "miscEnableRFC4117Transcoding": miscEnableRFC4117Transcoding,
       "miscEnableSingleDSPTranscoding": miscEnableSingleDSPTranscoding,
       "miscEnableNetworkISDNTransfer": miscEnableNetworkISDNTransfer,
       "miscLDAPocsNumberAttributeName": miscLDAPocsNumberAttributeName,
       "miscLDAPpbxNumberAttributeName": miscLDAPpbxNumberAttributeName,
       "miscLDAPMobileNumberAttributeName": miscLDAPMobileNumberAttributeName,
       "resourceManagement": resourceManagement,
       "resourceManagementMaxActiveCalls": resourceManagementMaxActiveCalls,
       "resourceManagementIsSelfCheckAuditUsed": resourceManagementIsSelfCheckAuditUsed,
       "resourceManagementRejectCallsOnOverload": resourceManagementRejectCallsOnOverload,
       "resourceManagementDisconnectOnBrokenConnection": resourceManagementDisconnectOnBrokenConnection,
       "resourceManagementMaxCallDuration": resourceManagementMaxCallDuration,
       "resourceManagementOverloadSensitivityLevel": resourceManagementOverloadSensitivityLevel,
       "aMD": aMD,
       "aMDTimeOut": aMDTimeOut,
       "aaa": aaa,
       "aaaIndications": aaaIndications,
       "aaaRadiusAccountingType": aaaRadiusAccountingType,
       "profile": profile,
       "iPProfileTable": iPProfileTable,
       "iPProfileEntry": iPProfileEntry,
       "iPProfileIndex": iPProfileIndex,
       "iPProfileRowStatus": iPProfileRowStatus,
       "iPProfileAction": iPProfileAction,
       "iPProfileActionResult": iPProfileActionResult,
       "iPProfilePreference": iPProfilePreference,
       "iPProfileProfileName": iPProfileProfileName,
       "iPProfileCodersGroupID": iPProfileCodersGroupID,
       "iPProfileFaxTransportMode": iPProfileFaxTransportMode,
       "iPProfileIsFaxUsed": iPProfileIsFaxUsed,
       "iPProfileDJBufMinDelay": iPProfileDJBufMinDelay,
       "iPProfileDJBufOptFactor": iPProfileDJBufOptFactor,
       "iPProfileIPDiffServ": iPProfileIPDiffServ,
       "iPProfileSigIPDiffServ": iPProfileSigIPDiffServ,
       "iPProfileSCE": iPProfileSCE,
       "iPProfileRTPRedundancyDepth": iPProfileRTPRedundancyDepth,
       "iPProfileRemoteBaseUDPPort": iPProfileRemoteBaseUDPPort,
       "iPProfileCngDetectorMode": iPProfileCngDetectorMode,
       "iPProfileVxxModemTransportType": iPProfileVxxModemTransportType,
       "iPProfileNSEMode": iPProfileNSEMode,
       "iPProfilePlayRingbackToneToIP": iPProfilePlayRingbackToneToIP,
       "iPProfileEnableEarlyMedia": iPProfileEnableEarlyMedia,
       "iPProfileProgressIndicatorToIP": iPProfileProgressIndicatorToIP,
       "iPProfileECE": iPProfileECE,
       "iPProfileMediaSecurityBehavior": iPProfileMediaSecurityBehavior,
       "iPProfileCallLimit": iPProfileCallLimit,
       "iPProfileDisconnectOnBrokenConnection": iPProfileDisconnectOnBrokenConnection,
       "iPProfileCopyDest2RedirectNumber": iPProfileCopyDest2RedirectNumber,
       "iPProfileAddIEInSetup": iPProfileAddIEInSetup,
       "iPProfileRxDTMFOption": iPProfileRxDTMFOption,
       "iPProfileFirstTxDtmfOption": iPProfileFirstTxDtmfOption,
       "iPProfileSecondTxDtmfOption": iPProfileSecondTxDtmfOption,
       "iPProfileMediaIPVersionPreference": iPProfileMediaIPVersionPreference,
       "iPProfileSBCAllowedCodersGroupID": iPProfileSBCAllowedCodersGroupID,
       "iPProfileSBCAllowedCodersMode": iPProfileSBCAllowedCodersMode,
       "iPProfileSBCMediaSecurityBehaviour": iPProfileSBCMediaSecurityBehaviour,
       "telProfileTable": telProfileTable,
       "telProfileEntry": telProfileEntry,
       "telProfileIndex": telProfileIndex,
       "telProfileRowStatus": telProfileRowStatus,
       "telProfileAction": telProfileAction,
       "telProfileActionResult": telProfileActionResult,
       "telProfilePreference": telProfilePreference,
       "telProfileProfileName": telProfileProfileName,
       "telProfileCodersGroupID": telProfileCodersGroupID,
       "telProfileFaxTransportMode": telProfileFaxTransportMode,
       "telProfileIsFaxUsed": telProfileIsFaxUsed,
       "telProfileDJBufMinDelay": telProfileDJBufMinDelay,
       "telProfileDJBufOptFactor": telProfileDJBufOptFactor,
       "telProfileIPDiffServ": telProfileIPDiffServ,
       "telProfileSigIPDiffServ": telProfileSigIPDiffServ,
       "telProfileVoiceVolume": telProfileVoiceVolume,
       "telProfileDTMFVolume": telProfileDTMFVolume,
       "telProfileInputGain": telProfileInputGain,
       "telProfileEnableReversalPolarity": telProfileEnableReversalPolarity,
       "telProfileEnableCurrentDisconnect": telProfileEnableCurrentDisconnect,
       "telProfileEnableDigitDelivery": telProfileEnableDigitDelivery,
       "telProfileECE": telProfileECE,
       "telProfileMWIanalogLamp": telProfileMWIanalogLamp,
       "telProfileMWIDisplay": telProfileMWIDisplay,
       "telProfileMaxFlashHookDetectionPeriod": telProfileMaxFlashHookDetectionPeriod,
       "telProfileEnableEarlyMedia": telProfileEnableEarlyMedia,
       "telProfileProgressIndicatorToIP": telProfileProgressIndicatorToIP,
       "telProfileTimeForReorderTone": telProfileTimeForReorderTone,
       "telProfileEnableDIDWink": telProfileEnableDIDWink,
       "telProfileIsTwoStageDial": telProfileIsTwoStageDial,
       "telProfileDisconnectOnBusyTone": telProfileDisconnectOnBusyTone,
       "telProfileEnableVoiceMailDelay": telProfileEnableVoiceMailDelay,
       "telProfileDialPlanIndex": telProfileDialPlanIndex,
       "telProfileEnable911PSAP": telProfileEnable911PSAP,
       "telProfileSwapTelToIpPhoneNumbers": telProfileSwapTelToIpPhoneNumbers,
       "telProfileEnableAGC": telProfileEnableAGC,
       "telProfileECNlpMode": telProfileECNlpMode,
       "voiceMail": voiceMail,
       "voiceMailLineTransferMode": voiceMailLineTransferMode,
       "voiceMailInterface": voiceMailInterface,
       "vmDigitPattern": vmDigitPattern,
       "vmDigitPatternNoReason": vmDigitPatternNoReason,
       "vmDigitPatternOnBusy": vmDigitPatternOnBusy,
       "vmDigitPatternOnNoAnswer": vmDigitPatternOnNoAnswer,
       "vmDigitPatternOnDND": vmDigitPatternOnDND,
       "vmDigitPatternInternalCall": vmDigitPatternInternalCall,
       "vmDigitPatternExternalCall": vmDigitPatternExternalCall,
       "vmDigitPatternDisconnectCode": vmDigitPatternDisconnectCode,
       "vmDigitPatternConnectCode": vmDigitPatternConnectCode,
       "vmDigitPatternVmDigitPatternOnBusyExternal": vmDigitPatternVmDigitPatternOnBusyExternal,
       "vmDigitPatternVmDigitPatternOnNoAnswerExternal": vmDigitPatternVmDigitPatternOnNoAnswerExternal,
       "vmDigitPatternVmDigitPatternOnDNDExternal": vmDigitPatternVmDigitPatternOnDNDExternal,
       "vmDigitPatternVmDigitPatternNoReasonExternal": vmDigitPatternVmDigitPatternNoReasonExternal,
       "vmDigitPatternDigitToIgnore": vmDigitPatternDigitToIgnore,
       "vmMWI": vmMWI,
       "vmMWIOnCode": vmMWIOnCode,
       "vmMWIOffCode": vmMWIOffCode,
       "vmMWISuffixCode": vmMWISuffixCode,
       "vmMWISourceNumber": vmMWISourceNumber,
       "vmSMDI": vmSMDI,
       "vmSMDIEnable": vmSMDIEnable,
       "vmSMDITimeOut": vmSMDITimeOut,
       "digitalGWext": digitalGWext,
       "digitalGWextEnableQSIGTunneling": digitalGWextEnableQSIGTunneling,
       "digitalGWextRemoveCLIWhenRestricted": digitalGWextRemoveCLIWhenRestricted,
       "digitalGWextDefaultCauseMapISDN2IP": digitalGWextDefaultCauseMapISDN2IP,
       "digitalGWextISDNSubaddressFormat": digitalGWextISDNSubaddressFormat,
       "digitalGWextEnableAoC": digitalGWextEnableAoC,
       "digitalGWextRemoveCallingName": digitalGWextRemoveCallingName,
       "digitalGWextCopyDest2RedirectNumber": digitalGWextCopyDest2RedirectNumber,
       "digitalGWextTDMOverIPMinCallsForTrunkActivation": digitalGWextTDMOverIPMinCallsForTrunkActivation,
       "rtpOnlyModeForTrunkTable": rtpOnlyModeForTrunkTable,
       "rtpOnlyModeForTrunkEntry": rtpOnlyModeForTrunkEntry,
       "rtpOnlyModeForTrunkIndex": rtpOnlyModeForTrunkIndex,
       "rtpOnlyModeForTrunkRtpOnlyModeForTrunk": rtpOnlyModeForTrunkRtpOnlyModeForTrunk,
       "acBChannelNegotiationForTrunkTable": acBChannelNegotiationForTrunkTable,
       "acBChannelNegotiationForTrunkEntry": acBChannelNegotiationForTrunkEntry,
       "acBChannelNegotiationForTrunkIndex": acBChannelNegotiationForTrunkIndex,
       "acBChannelNegotiationForTrunkMode": acBChannelNegotiationForTrunkMode,
       "acDigitalOOSBehaviorForTrunkTable": acDigitalOOSBehaviorForTrunkTable,
       "acDigitalOOSBehaviorForTrunkEntry": acDigitalOOSBehaviorForTrunkEntry,
       "acDigitalOOSBehaviorForTrunkIndex": acDigitalOOSBehaviorForTrunkIndex,
       "acDigitalOOSBehaviorForTrunkValue": acDigitalOOSBehaviorForTrunkValue,
       "acRemoveCallingNameForTrunkTable": acRemoveCallingNameForTrunkTable,
       "acRemoveCallingNameForTrunkEntry": acRemoveCallingNameForTrunkEntry,
       "acRemoveCallingNameForTrunkIndex": acRemoveCallingNameForTrunkIndex,
       "acRemoveCallingNameForTrunkMode": acRemoveCallingNameForTrunkMode,
       "gwSecurity": gwSecurity,
       "gwSecurityMediaSecurityBehavior": gwSecurityMediaSecurityBehavior,
       "gwSecuritySIPSRequireClientCertificate": gwSecuritySIPSRequireClientCertificate,
       "gwSecurityTLSReHandshakeInterval": gwSecurityTLSReHandshakeInterval,
       "gwSecurityPeerHostNameVerificationMode": gwSecurityPeerHostNameVerificationMode,
       "gwSecurityVerifyServerCertificate": gwSecurityVerifyServerCertificate,
       "gwSecurityTLSRemoteSubjectName": gwSecurityTLSRemoteSubjectName,
       "gwSecuritySRTPofferedSuites": gwSecuritySRTPofferedSuites,
       "acGWRtcpXr": acGWRtcpXr,
       "acGWRtcpXrEscIP": acGWRtcpXrEscIP,
       "acGWRtcpXrReportMode": acGWRtcpXrReportMode,
       "acGWRtcpXrEscTransportType": acGWRtcpXrEscTransportType,
       "acTimers": acTimers,
       "acTimersIPAlertTimeout": acTimersIPAlertTimeout,
       "acTimersPSTNAlertTimeout": acTimersPSTNAlertTimeout,
       "acEmergency": acEmergency,
       "acEmergencyRegretTimeout": acEmergencyRegretTimeout,
       "acEmergencyNumbersTable": acEmergencyNumbersTable,
       "acEmergencyNumbersEntry": acEmergencyNumbersEntry,
       "acEmergencyNumbersIndex": acEmergencyNumbersIndex,
       "acEmergencyNumbersNumbers": acEmergencyNumbersNumbers,
       "accounts": accounts,
       "accountTable": accountTable,
       "accountEntry": accountEntry,
       "accountIndex": accountIndex,
       "accountRowStatus": accountRowStatus,
       "accountAction": accountAction,
       "accountActionResult": accountActionResult,
       "accountServedTrunkGroup": accountServedTrunkGroup,
       "accountServedIPGroup": accountServedIPGroup,
       "accountServingIPGroup": accountServingIPGroup,
       "accountUsername": accountUsername,
       "accountPassword": accountPassword,
       "accountHostName": accountHostName,
       "accountRegister": accountRegister,
       "accountContactUser": accountContactUser,
       "ipGroups": ipGroups,
       "ipGroupTable": ipGroupTable,
       "ipGroupEntry": ipGroupEntry,
       "ipGroupIndex": ipGroupIndex,
       "ipGroupRowStatus": ipGroupRowStatus,
       "ipGroupAction": ipGroupAction,
       "ipGroupActionResult": ipGroupActionResult,
       "ipGroupType": ipGroupType,
       "ipGroupDescription": ipGroupDescription,
       "ipGroupProxySetId": ipGroupProxySetId,
       "ipGroupSIPGroupName": ipGroupSIPGroupName,
       "ipGroupContactUser": ipGroupContactUser,
       "ipGroupEnableSurvivability": ipGroupEnableSurvivability,
       "ipGroupServingIPGroup": ipGroupServingIPGroup,
       "ipGroupSipReRoutingMode": ipGroupSipReRoutingMode,
       "ipGroupAlwaysUseRouteTable": ipGroupAlwaysUseRouteTable,
       "ipGroupRoutingMode": ipGroupRoutingMode,
       "ipGroupProfileId": ipGroupProfileId,
       "ipGroupMediaRealm": ipGroupMediaRealm,
       "ipGroupMaxNumOfRegUsers": ipGroupMaxNumOfRegUsers,
       "sbc": sbc,
       "sbcEnable": sbcEnable,
       "sbcRegistrationTime": sbcRegistrationTime,
       "sbcEnableISBCApplication": sbcEnableISBCApplication,
       "sbcEnableIIP2IPApplication": sbcEnableIIP2IPApplication,
       "sbcClassificationTable": sbcClassificationTable,
       "sbcClassificationEntry": sbcClassificationEntry,
       "sbcClassificationIndex": sbcClassificationIndex,
       "sbcClassificationRowStatus": sbcClassificationRowStatus,
       "sbcClassificationAction": sbcClassificationAction,
       "sbcClassificationActionResult": sbcClassificationActionResult,
       "sbcClassificationSrcIPGroupId": sbcClassificationSrcIPGroupId,
       "sbcClassificationSrcSRDId": sbcClassificationSrcSRDId,
       "sbcClassificationSrcAddress": sbcClassificationSrcAddress,
       "sbcClassificationSrcUsernamePrefix": sbcClassificationSrcUsernamePrefix,
       "sbcClassificationSrcHost": sbcClassificationSrcHost,
       "sbcClassificationDestUsernamePrefix": sbcClassificationDestUsernamePrefix,
       "sbcClassificationDestHost": sbcClassificationDestHost,
       "sbcRoutingTable": sbcRoutingTable,
       "sbcRoutingEntry": sbcRoutingEntry,
       "sbcRoutingIndex": sbcRoutingIndex,
       "sbcRoutingRowStatus": sbcRoutingRowStatus,
       "sbcRoutingAction": sbcRoutingAction,
       "sbcRoutingActionResult": sbcRoutingActionResult,
       "sbcRoutingSrcIPGroupId": sbcRoutingSrcIPGroupId,
       "sbcRoutingSrcUsernamePrefix": sbcRoutingSrcUsernamePrefix,
       "sbcRoutingSrcHost": sbcRoutingSrcHost,
       "sbcRoutingDestUsernamePrefix": sbcRoutingDestUsernamePrefix,
       "sbcRoutingDestHost": sbcRoutingDestHost,
       "sbcRoutingDestType": sbcRoutingDestType,
       "sbcRoutingDestIPGroupId": sbcRoutingDestIPGroupId,
       "sbcRoutingDestSRDId": sbcRoutingDestSRDId,
       "sbcRoutingDestAddress": sbcRoutingDestAddress,
       "sbcRoutingDestPort": sbcRoutingDestPort,
       "sbcRoutingDestTransportType": sbcRoutingDestTransportType,
       "sbcRoutingAltRouteOptions": sbcRoutingAltRouteOptions,
       "sbcRoutingRequestType": sbcRoutingRequestType,
       "sbcIP2IPInboundManipulationTable": sbcIP2IPInboundManipulationTable,
       "sbcIP2IPInboundManipulationEntry": sbcIP2IPInboundManipulationEntry,
       "sbcIP2IPInboundManipulationIndex": sbcIP2IPInboundManipulationIndex,
       "sbcIP2IPInboundManipulationRowStatus": sbcIP2IPInboundManipulationRowStatus,
       "sbcIP2IPInboundManipulationAction": sbcIP2IPInboundManipulationAction,
       "sbcIP2IPInboundManipulationActionResult": sbcIP2IPInboundManipulationActionResult,
       "sbcIP2IPInboundManipulationIsAdditionalManipulation": sbcIP2IPInboundManipulationIsAdditionalManipulation,
       "sbcIP2IPInboundManipulationManipulatedURI": sbcIP2IPInboundManipulationManipulatedURI,
       "sbcIP2IPInboundManipulationSrcIPGroupID": sbcIP2IPInboundManipulationSrcIPGroupID,
       "sbcIP2IPInboundManipulationSrcUsernamePrefix": sbcIP2IPInboundManipulationSrcUsernamePrefix,
       "sbcIP2IPInboundManipulationSrcHost": sbcIP2IPInboundManipulationSrcHost,
       "sbcIP2IPInboundManipulationDestUsernamePrefix": sbcIP2IPInboundManipulationDestUsernamePrefix,
       "sbcIP2IPInboundManipulationDestHost": sbcIP2IPInboundManipulationDestHost,
       "sbcIP2IPInboundManipulationRemoveFromLeft": sbcIP2IPInboundManipulationRemoveFromLeft,
       "sbcIP2IPInboundManipulationRemoveFromRight": sbcIP2IPInboundManipulationRemoveFromRight,
       "sbcIP2IPInboundManipulationLeaveFromRight": sbcIP2IPInboundManipulationLeaveFromRight,
       "sbcIP2IPInboundManipulationPrefix2Add": sbcIP2IPInboundManipulationPrefix2Add,
       "sbcIP2IPInboundManipulationSuffix2Add": sbcIP2IPInboundManipulationSuffix2Add,
       "sbcIP2IPInboundManipulationRequestType": sbcIP2IPInboundManipulationRequestType,
       "sbcIP2IPOutboundManipulationTable": sbcIP2IPOutboundManipulationTable,
       "sbcIP2IPOutboundManipulationEntry": sbcIP2IPOutboundManipulationEntry,
       "sbcIP2IPOutboundManipulationIndex": sbcIP2IPOutboundManipulationIndex,
       "sbcIP2IPOutboundManipulationRowStatus": sbcIP2IPOutboundManipulationRowStatus,
       "sbcIP2IPOutboundManipulationAction": sbcIP2IPOutboundManipulationAction,
       "sbcIP2IPOutboundManipulationActionResult": sbcIP2IPOutboundManipulationActionResult,
       "sbcIP2IPOutboundManipulationIsAdditionalManipulation": sbcIP2IPOutboundManipulationIsAdditionalManipulation,
       "sbcIP2IPOutboundManipulationManipulatedURI": sbcIP2IPOutboundManipulationManipulatedURI,
       "sbcIP2IPOutboundManipulationSrcIPGroupID": sbcIP2IPOutboundManipulationSrcIPGroupID,
       "sbcIP2IPOutboundManipulationDestIPGroupID": sbcIP2IPOutboundManipulationDestIPGroupID,
       "sbcIP2IPOutboundManipulationSrcUsernamePrefix": sbcIP2IPOutboundManipulationSrcUsernamePrefix,
       "sbcIP2IPOutboundManipulationSrcHost": sbcIP2IPOutboundManipulationSrcHost,
       "sbcIP2IPOutboundManipulationDestUsernamePrefix": sbcIP2IPOutboundManipulationDestUsernamePrefix,
       "sbcIP2IPOutboundManipulationDestHost": sbcIP2IPOutboundManipulationDestHost,
       "sbcIP2IPOutboundManipulationRemoveFromLeft": sbcIP2IPOutboundManipulationRemoveFromLeft,
       "sbcIP2IPOutboundManipulationRemoveFromRight": sbcIP2IPOutboundManipulationRemoveFromRight,
       "sbcIP2IPOutboundManipulationLeaveFromRight": sbcIP2IPOutboundManipulationLeaveFromRight,
       "sbcIP2IPOutboundManipulationPrefix2Add": sbcIP2IPOutboundManipulationPrefix2Add,
       "sbcIP2IPOutboundManipulationSuffix2Add": sbcIP2IPOutboundManipulationSuffix2Add,
       "sbcIP2IPOutboundManipulationRequestType": sbcIP2IPOutboundManipulationRequestType,
       "sbcAdmissionControlTable": sbcAdmissionControlTable,
       "sbcAdmissionControlEntry": sbcAdmissionControlEntry,
       "sbcAdmissionControlIndex": sbcAdmissionControlIndex,
       "sbcAdmissionControlRowStatus": sbcAdmissionControlRowStatus,
       "sbcAdmissionControlAction": sbcAdmissionControlAction,
       "sbcAdmissionControlActionResult": sbcAdmissionControlActionResult,
       "sbcAdmissionControlLimitType": sbcAdmissionControlLimitType,
       "sbcAdmissionControlIpGroupID": sbcAdmissionControlIpGroupID,
       "sbcAdmissionControlSrdID": sbcAdmissionControlSrdID,
       "sbcAdmissionControlRequestType": sbcAdmissionControlRequestType,
       "sbcAdmissionControlRequestDirection": sbcAdmissionControlRequestDirection,
       "sbcAdmissionControlLimit": sbcAdmissionControlLimit,
       "sbcAdmissionControlLimitPerUser": sbcAdmissionControlLimitPerUser,
       "sbcMessageManipulationsTable": sbcMessageManipulationsTable,
       "sbcMessageManipulationsEntry": sbcMessageManipulationsEntry,
       "sbcMessageManipulationsIndex": sbcMessageManipulationsIndex,
       "sbcMessageManipulationsRowStatus": sbcMessageManipulationsRowStatus,
       "sbcMessageManipulationsAction": sbcMessageManipulationsAction,
       "sbcMessageManipulationsActionResult": sbcMessageManipulationsActionResult,
       "sbcMessageManipulationsManipulationSetID": sbcMessageManipulationsManipulationSetID,
       "sbcMessageManipulationsMessageType": sbcMessageManipulationsMessageType,
       "sbcMessageManipulationsCondition": sbcMessageManipulationsCondition,
       "sbcMessageManipulationsActionSubject": sbcMessageManipulationsActionSubject,
       "sbcMessageManipulationsActionType": sbcMessageManipulationsActionType,
       "sbcMessageManipulationsActionValue": sbcMessageManipulationsActionValue,
       "sbcMessageManipulationsRowRole": sbcMessageManipulationsRowRole,
       "sbcAlternativeRoutingReasonsTable": sbcAlternativeRoutingReasonsTable,
       "sbcAlternativeRoutingReasonsEntry": sbcAlternativeRoutingReasonsEntry,
       "sbcAlternativeRoutingReasonsIndex": sbcAlternativeRoutingReasonsIndex,
       "sbcAlternativeRoutingReasonsRowStatus": sbcAlternativeRoutingReasonsRowStatus,
       "sbcAlternativeRoutingReasonsAction": sbcAlternativeRoutingReasonsAction,
       "sbcAlternativeRoutingReasonsActionResult": sbcAlternativeRoutingReasonsActionResult,
       "sbcAlternativeRoutingReasonsReleaseCause": sbcAlternativeRoutingReasonsReleaseCause,
       "gwIPv6": gwIPv6,
       "gwIPv6GwAppDualIPStackSDPMethod": gwIPv6GwAppDualIPStackSDPMethod,
       "gwIPv6GwAppPrimaryMediaInterface": gwIPv6GwAppPrimaryMediaInterface,
       "gwIPv6GwAppSecondaryMediaInterface": gwIPv6GwAppSecondaryMediaInterface,
       "gwIPv6MediaIPVersionPreference": gwIPv6MediaIPVersionPreference,
       "srdSettings": srdSettings,
       "srdTable": srdTable,
       "srdEntry": srdEntry,
       "srdIndex": srdIndex,
       "srdRowStatus": srdRowStatus,
       "srdAction": srdAction,
       "srdActionResult": srdActionResult,
       "srdName": srdName,
       "srdMediaRealm": srdMediaRealm,
       "srdIntraSRDMediaAnchoring": srdIntraSRDMediaAnchoring,
       "srdBlockUnRegUsers": srdBlockUnRegUsers,
       "srdMaxNumOfRegUsers": srdMaxNumOfRegUsers,
       "sipInterfaceSettings": sipInterfaceSettings,
       "sipInterfaceTable": sipInterfaceTable,
       "sipInterfaceEntry": sipInterfaceEntry,
       "sipInterfaceIndex": sipInterfaceIndex,
       "sipInterfaceRowStatus": sipInterfaceRowStatus,
       "sipInterfaceAction": sipInterfaceAction,
       "sipInterfaceActionResult": sipInterfaceActionResult,
       "sipInterfaceNetworkInterface": sipInterfaceNetworkInterface,
       "sipInterfaceApplicationType": sipInterfaceApplicationType,
       "sipInterfaceUDPPort": sipInterfaceUDPPort,
       "sipInterfaceTCPPort": sipInterfaceTCPPort,
       "sipInterfaceTLSPort": sipInterfaceTLSPort,
       "sipInterfaceSRD": sipInterfaceSRD,
       "sip": sip,
       "sipProxy": sipProxy,
       "sipProxyUsed": sipProxyUsed,
       "sipProxyEnableKeepAlive": sipProxyEnableKeepAlive,
       "sipProxyName": sipProxyName,
       "sipProxyIsHotSwap": sipProxyIsHotSwap,
       "sipProxyHotSwapRtx": sipProxyHotSwapRtx,
       "sipProxyRedundancyMode": sipProxyRedundancyMode,
       "sipProxyAlwaysUseRouteTable": sipProxyAlwaysUseRouteTable,
       "sipProxyAlwaysSendToProxy": sipProxyAlwaysSendToProxy,
       "sipProxyKeepAliveTime": sipProxyKeepAliveTime,
       "sipProxyIsFallbackUsed": sipProxyIsFallbackUsed,
       "sipProxySendInviteToProxy": sipProxySendInviteToProxy,
       "sipProxyIsTrustedProxy": sipProxyIsTrustedProxy,
       "sipProxyUseGatewayNameForOptions": sipProxyUseGatewayNameForOptions,
       "sipProxyEnableSRVQuery": sipProxyEnableSRVQuery,
       "sipProxyDNSQueryType": sipProxyDNSQueryType,
       "sipProxyLoadBalancingMethod": sipProxyLoadBalancingMethod,
       "sipProxyIPListRefreshTime": sipProxyIPListRefreshTime,
       "proxyIPTable": proxyIPTable,
       "proxyIPEntry": proxyIPEntry,
       "proxyIPIndex": proxyIPIndex,
       "proxyIPRowStatus": proxyIPRowStatus,
       "proxyIPAction": proxyIPAction,
       "proxyIPActionResult": proxyIPActionResult,
       "proxyIPProxyIP": proxyIPProxyIP,
       "sipProxySetTable": sipProxySetTable,
       "sipProxySetEntry": sipProxySetEntry,
       "sipProxySetIndex": sipProxySetIndex,
       "sipProxySetRowStatus": sipProxySetRowStatus,
       "sipProxySetAction": sipProxySetAction,
       "sipProxySetActionResult": sipProxySetActionResult,
       "sipProxySetEnableProxyKeepAlive": sipProxySetEnableProxyKeepAlive,
       "sipProxySetProxyKeepAliveTime": sipProxySetProxyKeepAliveTime,
       "sipProxySetProxyLoadBalancingMethod": sipProxySetProxyLoadBalancingMethod,
       "sipProxySetIsProxyHotSwap": sipProxySetIsProxyHotSwap,
       "sipDTMF": sipDTMF,
       "sipDTMFIsHookFlashUsed": sipDTMFIsHookFlashUsed,
       "sipDTMFIsDTMFUsed": sipDTMFIsDTMFUsed,
       "sipDTMFOutOfBandDtmfFormat": sipDTMFOutOfBandDtmfFormat,
       "sipDTMFDisableAutoMute": sipDTMFDisableAutoMute,
       "sipDTMFRxDTMFOption": sipDTMFRxDTMFOption,
       "sipDTMFHookFlashOption": sipDTMFHookFlashOption,
       "sipDTMFUseDigitForSpecialDTMF": sipDTMFUseDigitForSpecialDTMF,
       "sipDTMFMinRoutingOverlapDigits": sipDTMFMinRoutingOverlapDigits,
       "sipDTMFISDNOverlapIPtoTelDialing": sipDTMFISDNOverlapIPtoTelDialing,
       "sipTxDTMFOptionTable": sipTxDTMFOptionTable,
       "sipTxDTMFOptionEntry": sipTxDTMFOptionEntry,
       "sipTxDTMFOptionIndex": sipTxDTMFOptionIndex,
       "sipTxDTMFOptionRowStatus": sipTxDTMFOptionRowStatus,
       "sipTxDTMFOptionAction": sipTxDTMFOptionAction,
       "sipTxDTMFOptionActionResult": sipTxDTMFOptionActionResult,
       "sipTxDTMFOptionValue": sipTxDTMFOptionValue,
       "sipPorts": sipPorts,
       "sipPortsDestinationPort": sipPortsDestinationPort,
       "sipPortsLocalSipPort": sipPortsLocalSipPort,
       "sipPortsTCPLocalSipPort": sipPortsTCPLocalSipPort,
       "sipPortsTLSLocalSipPort": sipPortsTLSLocalSipPort,
       "sipAuth": sipAuth,
       "sipAuthMode": sipAuthMode,
       "sipAuthUserName": sipAuthUserName,
       "sipAuthPassword": sipAuthPassword,
       "sipAuthCnonce": sipAuthCnonce,
       "sipAuthMutualAuthenticationMode": sipAuthMutualAuthenticationMode,
       "sipAuthChallengeCachingMode": sipAuthChallengeCachingMode,
       "authTable": authTable,
       "authEntry": authEntry,
       "authIndex": authIndex,
       "authIsUsed": authIsUsed,
       "authAction": authAction,
       "authActionResult": authActionResult,
       "authUserID": authUserID,
       "authUserPassword": authUserPassword,
       "authModule": authModule,
       "authPort": authPort,
       "sipRetransmission": sipRetransmission,
       "sipRetransmissionT1Rtx": sipRetransmissionT1Rtx,
       "sipRetransmissionT2Rtx": sipRetransmissionT2Rtx,
       "sipRetransmissionSipMaxRtx": sipRetransmissionSipMaxRtx,
       "sipRetransmissionIsRtxEnable": sipRetransmissionIsRtxEnable,
       "sipRetransmissionEnablePTime": sipRetransmissionEnablePTime,
       "sipRetransmissionTCPTimeout": sipRetransmissionTCPTimeout,
       "sipRetransmissionRetryAfterTime": sipRetransmissionRetryAfterTime,
       "sipRegistration": sipRegistration,
       "sipRegistrationIsNeeded": sipRegistrationIsNeeded,
       "sipRegistrationIP": sipRegistrationIP,
       "sipRegistrationTime": sipRegistrationTime,
       "sipRegistrationRegistrationRetryTime": sipRegistrationRegistrationRetryTime,
       "sipRegistrationRegistrarName": sipRegistrationRegistrarName,
       "sipRegistrationTimeDivider": sipRegistrationTimeDivider,
       "sipRegistrationName": sipRegistrationName,
       "sipRegistrationRegisterOnInviteFailure": sipRegistrationRegisterOnInviteFailure,
       "sipRegistrationTimeThreshold": sipRegistrationTimeThreshold,
       "sipRegistrationRegistrarTransportType": sipRegistrationRegistrarTransportType,
       "sipRegistrationReRegisterOnConnectionFailure": sipRegistrationReRegisterOnConnectionFailure,
       "sipMisc": sipMisc,
       "sipMiscEnableEarlyMedia": sipMiscEnableEarlyMedia,
       "sipMiscSipSessionExpires": sipMiscSipSessionExpires,
       "sipMiscIsUserPhone": sipMiscIsUserPhone,
       "sipMiscGatewayName": sipMiscGatewayName,
       "sipMiscPrackMode": sipMiscPrackMode,
       "sipMiscEnableRpiHeader": sipMiscEnableRpiHeader,
       "sipMiscXChannelHeader": sipMiscXChannelHeader,
       "sipMiscAssertedIDMode": sipMiscAssertedIDMode,
       "sipMiscIsUserPhoneInFrom": sipMiscIsUserPhoneInFrom,
       "sipMiscAddTon2Rpi": sipMiscAddTon2Rpi,
       "sipMiscEnableCIC": sipMiscEnableCIC,
       "sipMiscTransportType": sipMiscTransportType,
       "sipMiscISubNumberOfDigits": sipMiscISubNumberOfDigits,
       "sipMiscSIP183Behaviour": sipMiscSIP183Behaviour,
       "sipMiscUseToHeaderAsCalledNum": sipMiscUseToHeaderAsCalledNum,
       "sipMiscEnableSIPS": sipMiscEnableSIPS,
       "sipMiscEnableSRVQuery": sipMiscEnableSRVQuery,
       "sipMiscSubject": sipMiscSubject,
       "sipMiscUseSIPTgrp": sipMiscUseSIPTgrp,
       "sipMiscSend180ForCallWaiting": sipMiscSend180ForCallWaiting,
       "sipMiscUserAgentDisplayInfo": sipMiscUserAgentDisplayInfo,
       "sipMiscSessionExpiresMethod": sipMiscSessionExpiresMethod,
       "sipMiscEnableGRUU": sipMiscEnableGRUU,
       "sipMiscDNSQueryType": sipMiscDNSQueryType,
       "sipMiscEnableHistoryInfo": sipMiscEnableHistoryInfo,
       "sipMiscEnableTCPConnectionReuse": sipMiscEnableTCPConnectionReuse,
       "sipMiscComfortNoiseNegotiation": sipMiscComfortNoiseNegotiation,
       "sipMiscMultiPtimeFormat": sipMiscMultiPtimeFormat,
       "sipMiscRTPOnlyMode": sipMiscRTPOnlyMode,
       "sipMiscEnableReasonHeader": sipMiscEnableReasonHeader,
       "sipMisc3xxBehavior": sipMisc3xxBehavior,
       "sipMiscEnableSemiAttendedTransfer": sipMiscEnableSemiAttendedTransfer,
       "sipMiscUseSIPURIForDiversionHeader": sipMiscUseSIPURIForDiversionHeader,
       "sipMiscEnableVMURI": sipMiscEnableVMURI,
       "sipMiscEnablePChargingVector": sipMiscEnablePChargingVector,
       "sipMiscPAssertedUserName": sipMiscPAssertedUserName,
       "sipMiscSDPSessionOwner": sipMiscSDPSessionOwner,
       "sipMiscResetOnINIFileDownload": sipMiscResetOnINIFileDownload,
       "sipMiscSetDefaultOnIniFileProcess": sipMiscSetDefaultOnIniFileProcess,
       "sipMiscEnableContactRestriction": sipMiscEnableContactRestriction,
       "sipMiscEnablePAssociatedURIHeader": sipMiscEnablePAssociatedURIHeader,
       "sipMiscMinSE": sipMiscMinSE,
       "sipMiscApplicationProfile": sipMiscApplicationProfile,
       "sipMiscOPTIONSUserPart": sipMiscOPTIONSUserPart,
       "sipMiscUseAORInReferToHeader": sipMiscUseAORInReferToHeader,
       "sipMiscForkingHandlingMode": sipMiscForkingHandlingMode,
       "sipMiscOfferUnencryptedSRTCP": sipMiscOfferUnencryptedSRTCP,
       "sipMiscSourceNumberPreference": sipMiscSourceNumberPreference,
       "sipSubscribe": sipSubscribe,
       "sipSubscribeEnable": sipSubscribeEnable,
       "sipSubscribeRetryTime": sipSubscribeRetryTime,
       "sipSubscribeEnableMWISubscription": sipSubscribeEnableMWISubscription,
       "sipSubscribeSubscriptionMode": sipSubscribeSubscriptionMode,
       "sipDigitalGW": sipDigitalGW,
       "causeMapSIP2ISDNTable": causeMapSIP2ISDNTable,
       "causeMapSIP2ISDNEntry": causeMapSIP2ISDNEntry,
       "causeMapSIP2ISDNIndex": causeMapSIP2ISDNIndex,
       "causeMapSIP2ISDNRowStatus": causeMapSIP2ISDNRowStatus,
       "causeMapSIP2ISDNAction": causeMapSIP2ISDNAction,
       "causeMapSIP2ISDNActionResult": causeMapSIP2ISDNActionResult,
       "causeMapSIP2ISDNSIPResponse": causeMapSIP2ISDNSIPResponse,
       "causeMapSIP2ISDNQ850Cause": causeMapSIP2ISDNQ850Cause,
       "causeMapISDN2SIPTable": causeMapISDN2SIPTable,
       "causeMapISDN2SIPEntry": causeMapISDN2SIPEntry,
       "causeMapISDN2SIPIndex": causeMapISDN2SIPIndex,
       "causeMapISDN2SIPRowStatus": causeMapISDN2SIPRowStatus,
       "causeMapISDN2SIPAction": causeMapISDN2SIPAction,
       "causeMapISDN2SIPActionResult": causeMapISDN2SIPActionResult,
       "causeMapISDN2SIPQ850Cause": causeMapISDN2SIPQ850Cause,
       "causeMapISDN2SIPSIPResponse": causeMapISDN2SIPSIPResponse,
       "sipSAS": sipSAS,
       "sipSASEnable": sipSASEnable,
       "sipSASLocalSIPUdpPort": sipSASLocalSIPUdpPort,
       "sipSASDefaultGatewayIP": sipSASDefaultGatewayIP,
       "sipSASLocalSIPTlsPort": sipSASLocalSIPTlsPort,
       "sipSASRegistrationTime": sipSASRegistrationTime,
       "sipSASShortNumberLength": sipSASShortNumberLength,
       "sipSASLocalSIPTcpPort": sipSASLocalSIPTcpPort,
       "sipSASProxySet": sipSASProxySet,
       "sipSASRedundantProxySet": sipSASRedundantProxySet,
       "sipSASBindingMode": sipSASBindingMode,
       "sipSASSurvivabilityMode": sipSASSurvivabilityMode,
       "sipSASEnableENUM": sipSASEnableENUM,
       "sipSASEnableRecordRoute": sipSASEnableRecordRoute,
       "sasRegistrationManipulationTable": sasRegistrationManipulationTable,
       "sasRegistrationManipulationEntry": sasRegistrationManipulationEntry,
       "sasRegistrationManipulationIndex": sasRegistrationManipulationIndex,
       "sasRegistrationManipulationRowStatus": sasRegistrationManipulationRowStatus,
       "sasRegistrationManipulationAction": sasRegistrationManipulationAction,
       "sasRegistrationManipulationActionResult": sasRegistrationManipulationActionResult,
       "sasRegistrationManipulationRemoveFromRight": sasRegistrationManipulationRemoveFromRight,
       "sasRegistrationManipulationLeaveFromRight": sasRegistrationManipulationLeaveFromRight,
       "h323": h323,
       "h323SourceEncodType": h323SourceEncodType,
       "h323DestEncodType": h323DestEncodType,
       "h323H323IDString": h323H323IDString,
       "h323ConnectionModes": h323ConnectionModes,
       "h323ConnectionModesIsTunnelingUsed": h323ConnectionModesIsTunnelingUsed,
       "fastStart": fastStart,
       "fastStartIsFastConnectUsed": fastStartIsFastConnectUsed,
       "fastStartOpenH245OnFS": fastStartOpenH245OnFS,
       "fastStartIsFSMediaInfoSendOnConnect": fastStartIsFSMediaInfoSendOnConnect,
       "fastStartIsFSOpenMediaOnConnect": fastStartIsFSOpenMediaOnConnect,
       "h323GK": h323GK,
       "h323GKIsGateKeeperUsed": h323GKIsGateKeeperUsed,
       "h323GKGwRegistrType": h323GKGwRegistrType,
       "h323GKIsGkFallbackUsed": h323GKIsGkFallbackUsed,
       "h323GKCanMapAliases": h323GKCanMapAliases,
       "h323GKResponseTimeout": h323GKResponseTimeout,
       "h323GKMaxRetries": h323GKMaxRetries,
       "h323GKRegistrationTime": h323GKRegistrationTime,
       "h323GKIsTerminal": h323GKIsTerminal,
       "h323GKGatekeeperID": h323GKGatekeeperID,
       "h323GKEnablePregrantARQ": h323GKEnablePregrantARQ,
       "h323GKRegister": h323GKRegister,
       "h323GKAlternativeGKUsed": h323GKAlternativeGKUsed,
       "h323GKUseRedundantGKOnRRJ": h323GKUseRedundantGKOnRRJ,
       "h323GKEnableGKAutoDiscovery": h323GKEnableGKAutoDiscovery,
       "h323GKGKAutoDiscoveryIP": h323GKGKAutoDiscoveryIP,
       "gkIPTable": gkIPTable,
       "gkIPEntry": gkIPEntry,
       "gkIPIndex": gkIPIndex,
       "gkIPRowStatus": gkIPRowStatus,
       "gkIPAction": gkIPAction,
       "gkIPActionResult": gkIPActionResult,
       "gkIPGatekeeperIP": gkIPGatekeeperIP,
       "gkIPGateleeperID": gkIPGateleeperID,
       "registerPrefixTable": registerPrefixTable,
       "registerPrefixEntry": registerPrefixEntry,
       "registerPrefixIndex": registerPrefixIndex,
       "registerPrefixRowStatus": registerPrefixRowStatus,
       "registerPrefixAction": registerPrefixAction,
       "registerPrefixActionResult": registerPrefixActionResult,
       "registerPrefixPrefix": registerPrefixPrefix,
       "registerPrefixNumberPlan": registerPrefixNumberPlan,
       "registerPrefixNumberType": registerPrefixNumberType,
       "gkRedundancy": gkRedundancy,
       "gkRedundancyUsed": gkRedundancyUsed,
       "gkRedundancyTimeBetweenGKsLoops": gkRedundancyTimeBetweenGKsLoops,
       "gkRAI": gkRAI,
       "gkRAIEnable": gkRAIEnable,
       "gkRAIHighThreshold": gkRAIHighThreshold,
       "gkRAILowThreshold": gkRAILowThreshold,
       "gkRAILoopTime": gkRAILoopTime,
       "h323DTMF": h323DTMF,
       "h323DTMFHookFlashOption": h323DTMFHookFlashOption,
       "h323DTMFRxDtmfOption": h323DTMFRxDtmfOption,
       "dTMFOptionsTable": dTMFOptionsTable,
       "dTMFOptionsEntry": dTMFOptionsEntry,
       "dTMFOptionsIndex": dTMFOptionsIndex,
       "dTMFOptionsRowStatus": dTMFOptionsRowStatus,
       "dTMFOptionsAction": dTMFOptionsAction,
       "dTMFOptionsActionResult": dTMFOptionsActionResult,
       "dTMFOptionsTxDTMFOption": dTMFOptionsTxDTMFOption,
       "h323Ports": h323Ports,
       "h323PortsH225ListenPort": h323PortsH225ListenPort,
       "h323PortsH225DialPort": h323PortsH225DialPort,
       "h323PortsH323BasePort": h323PortsH323BasePort,
       "h323PortsRasSourcePort": h323PortsRasSourcePort,
       "h323PortsRasDestPort": h323PortsRasDestPort,
       "h323Auth": h323Auth,
       "h323AuthEnableH235Security": h323AuthEnableH235Security,
       "h323AuthUserName": h323AuthUserName,
       "h323AuthPassword": h323AuthPassword,
       "h323Misc": h323Misc,
       "h323MiscIsSetupIncludeNum": h323MiscIsSetupIncludeNum,
       "h323MiscIsSetupAckUsed": h323MiscIsSetupAckUsed,
       "h323MiscH245InitTimeOut": h323MiscH245InitTimeOut,
       "h323MiscEnableQ931Cause": h323MiscEnableQ931Cause,
       "h323MiscEnableQ931Multiplexing": h323MiscEnableQ931Multiplexing,
       "h323MiscSendChannelNonStandard": h323MiscSendChannelNonStandard,
       "h323MiscH245RoundTripTime": h323MiscH245RoundTripTime,
       "h323MiscProgressBehavior": h323MiscProgressBehavior}
)
