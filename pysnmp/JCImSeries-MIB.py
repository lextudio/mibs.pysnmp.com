# SNMP MIB module (JCImSeries-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JCImSeries-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:36 2024
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

(mSeries,) = mibBuilder.importSymbols(
    "JCIControlsGroup-MIB",
    "mSeries")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jcimSeriesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OpcTypes_ObjectIdentity = ObjectIdentity
opcTypes = _OpcTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2)
)


class _OpcSeverity_Type(Integer32):
    """Custom type opcSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_OpcSeverity_Type.__name__ = "Integer32"
_OpcSeverity_Object = MibScalar
opcSeverity = _OpcSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 1),
    _OpcSeverity_Type()
)
opcSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcSeverity.setStatus("current")
_OpcSource_Type = DisplayString
_OpcSource_Object = MibScalar
opcSource = _OpcSource_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 2),
    _OpcSource_Type()
)
opcSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcSource.setStatus("current")
_OpcTimeStamp_Type = DisplayString
_OpcTimeStamp_Object = MibScalar
opcTimeStamp = _OpcTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 3),
    _OpcTimeStamp_Type()
)
opcTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcTimeStamp.setStatus("current")
_OpcMessage_Type = DisplayString
_OpcMessage_Object = MibScalar
opcMessage = _OpcMessage_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 4),
    _OpcMessage_Type()
)
opcMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcMessage.setStatus("current")
_OpcEventCategory_Type = DisplayString
_OpcEventCategory_Object = MibScalar
opcEventCategory = _OpcEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 5),
    _OpcEventCategory_Type()
)
opcEventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcEventCategory.setStatus("current")
_OpcEventCategoryText_Type = DisplayString
_OpcEventCategoryText_Object = MibScalar
opcEventCategoryText = _OpcEventCategoryText_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 6),
    _OpcEventCategoryText_Type()
)
opcEventCategoryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcEventCategoryText.setStatus("current")


class _OpcEventType_Type(Integer32):
    """Custom type opcEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("conditionEvent", 4),
          ("simpleEvent", 1),
          ("trackingEvent", 2))
    )


_OpcEventType_Type.__name__ = "Integer32"
_OpcEventType_Object = MibScalar
opcEventType = _OpcEventType_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 7),
    _OpcEventType_Type()
)
opcEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcEventType.setStatus("current")
_OpcEventTypeText_Type = DisplayString
_OpcEventTypeText_Object = MibScalar
opcEventTypeText = _OpcEventTypeText_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 8),
    _OpcEventTypeText_Type()
)
opcEventTypeText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcEventTypeText.setStatus("current")
_OpcCondition_Type = DisplayString
_OpcCondition_Object = MibScalar
opcCondition = _OpcCondition_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 20),
    _OpcCondition_Type()
)
opcCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcCondition.setStatus("current")
_OpcSubCondition_Type = DisplayString
_OpcSubCondition_Object = MibScalar
opcSubCondition = _OpcSubCondition_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 21),
    _OpcSubCondition_Type()
)
opcSubCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcSubCondition.setStatus("current")
_OpcActiveTime_Type = DisplayString
_OpcActiveTime_Object = MibScalar
opcActiveTime = _OpcActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 22),
    _OpcActiveTime_Type()
)
opcActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcActiveTime.setStatus("current")


class _OpcQuality_Type(Integer32):
    """Custom type opcQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OpcQuality_Type.__name__ = "Integer32"
_OpcQuality_Object = MibScalar
opcQuality = _OpcQuality_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 23),
    _OpcQuality_Type()
)
opcQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcQuality.setStatus("current")
_OpcQualityText_Type = DisplayString
_OpcQualityText_Object = MibScalar
opcQualityText = _OpcQualityText_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 24),
    _OpcQualityText_Type()
)
opcQualityText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcQualityText.setStatus("current")


class _OpcNewState_Type(Integer32):
    """Custom type opcNewState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("opcConditionAcked", 4),
          ("opcConditionActive", 2),
          ("opcConditionEnabled", 1))
    )


_OpcNewState_Type.__name__ = "Integer32"
_OpcNewState_Object = MibScalar
opcNewState = _OpcNewState_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 25),
    _OpcNewState_Type()
)
opcNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcNewState.setStatus("current")
_OpcNewStateText_Type = DisplayString
_OpcNewStateText_Object = MibScalar
opcNewStateText = _OpcNewStateText_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 26),
    _OpcNewStateText_Type()
)
opcNewStateText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcNewStateText.setStatus("current")


class _OpcAckRequired_Type(Integer32):
    """Custom type opcAckRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_OpcAckRequired_Type.__name__ = "Integer32"
_OpcAckRequired_Object = MibScalar
opcAckRequired = _OpcAckRequired_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 27),
    _OpcAckRequired_Type()
)
opcAckRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcAckRequired.setStatus("current")
_OpcAckRequiredText_Type = DisplayString
_OpcAckRequiredText_Object = MibScalar
opcAckRequiredText = _OpcAckRequiredText_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 28),
    _OpcAckRequiredText_Type()
)
opcAckRequiredText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcAckRequiredText.setStatus("current")
_OpcCookie_Type = Integer32
_OpcCookie_Object = MibScalar
opcCookie = _OpcCookie_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 29),
    _OpcCookie_Type()
)
opcCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcCookie.setStatus("current")
_OpcChangeMaskText_Type = DisplayString
_OpcChangeMaskText_Object = MibScalar
opcChangeMaskText = _OpcChangeMaskText_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 30),
    _OpcChangeMaskText_Type()
)
opcChangeMaskText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcChangeMaskText.setStatus("current")
_OpcActorID_Type = DisplayString
_OpcActorID_Object = MibScalar
opcActorID = _OpcActorID_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 31),
    _OpcActorID_Type()
)
opcActorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcActorID.setStatus("current")


class _OpcChangeMask_Type(Integer32):
    """Custom type opcChangeMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_OpcChangeMask_Type.__name__ = "Integer32"
_OpcChangeMask_Object = MibScalar
opcChangeMask = _OpcChangeMask_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 32),
    _OpcChangeMask_Type()
)
opcChangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opcChangeMask.setStatus("current")
_OriginalDate_Type = DisplayString
_OriginalDate_Object = MibScalar
originalDate = _OriginalDate_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 40),
    _OriginalDate_Type()
)
originalDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    originalDate.setStatus("current")
_OriginalTime_Type = DisplayString
_OriginalTime_Object = MibScalar
originalTime = _OriginalTime_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 41),
    _OriginalTime_Type()
)
originalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    originalTime.setStatus("current")
_NetworkName_Type = DisplayString
_NetworkName_Object = MibScalar
networkName = _NetworkName_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 43),
    _NetworkName_Type()
)
networkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkName.setStatus("current")
_NcmName_Type = DisplayString
_NcmName_Object = MibScalar
ncmName = _NcmName_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 44),
    _NcmName_Type()
)
ncmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmName.setStatus("current")
_SystemID_Type = DisplayString
_SystemID_Object = MibScalar
systemID = _SystemID_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 45),
    _SystemID_Type()
)
systemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemID.setStatus("current")
_Id_Type = DisplayString
_Id_Object = MibScalar
id = _Id_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 46),
    _Id_Type()
)
id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    id.setStatus("current")
_ExpandedID_Type = DisplayString
_ExpandedID_Object = MibScalar
expandedID = _ExpandedID_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 47),
    _ExpandedID_Type()
)
expandedID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expandedID.setStatus("current")
_Presentvalue_Type = DisplayString
_Presentvalue_Object = MibScalar
presentvalue = _Presentvalue_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 48),
    _Presentvalue_Type()
)
presentvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    presentvalue.setStatus("current")
_Units_Type = DisplayString
_Units_Object = MibScalar
units = _Units_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 49),
    _Units_Type()
)
units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    units.setStatus("current")
_ReportType_Type = DisplayString
_ReportType_Object = MibScalar
reportType = _ReportType_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 50),
    _ReportType_Type()
)
reportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportType.setStatus("current")
_AlarmType_Type = DisplayString
_AlarmType_Object = MibScalar
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 51),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_Availattribute1_Type = DisplayString
_Availattribute1_Object = MibScalar
availattribute1 = _Availattribute1_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 52),
    _Availattribute1_Type()
)
availattribute1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availattribute1.setStatus("current")
_AlarmPriority_Type = DisplayString
_AlarmPriority_Object = MibScalar
alarmPriority = _AlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 53),
    _AlarmPriority_Type()
)
alarmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmPriority.setStatus("current")
_FeatureStatus_Type = DisplayString
_FeatureStatus_Object = MibScalar
featureStatus = _FeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 60),
    _FeatureStatus_Type()
)
featureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featureStatus.setStatus("current")
_ReportDate_Type = DisplayString
_ReportDate_Object = MibScalar
reportDate = _ReportDate_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 61),
    _ReportDate_Type()
)
reportDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportDate.setStatus("current")
_ReportTime_Type = DisplayString
_ReportTime_Object = MibScalar
reportTime = _ReportTime_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 62),
    _ReportTime_Type()
)
reportTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reportTime.setStatus("current")


class _TransactionType_Type(Integer32):
    """Custom type transactionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("feature", 3),
          ("logonLogoff", 1),
          ("object", 2))
    )


_TransactionType_Type.__name__ = "Integer32"
_TransactionType_Object = MibScalar
transactionType = _TransactionType_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 63),
    _TransactionType_Type()
)
transactionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionType.setStatus("current")
_TransactionTypeText_Type = DisplayString
_TransactionTypeText_Object = MibScalar
transactionTypeText = _TransactionTypeText_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 64),
    _TransactionTypeText_Type()
)
transactionTypeText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionTypeText.setStatus("current")
_Location_Type = DisplayString
_Location_Object = MibScalar
location = _Location_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 65),
    _Location_Type()
)
location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    location.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 66),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_UserID_Type = DisplayString
_UserID_Object = MibScalar
userID = _UserID_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 67),
    _UserID_Type()
)
userID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userID.setStatus("current")
_AccssLevel_Type = DisplayString
_AccssLevel_Object = MibScalar
accssLevel = _AccssLevel_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 68),
    _AccssLevel_Type()
)
accssLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accssLevel.setStatus("current")
_TransactionText_Type = DisplayString
_TransactionText_Object = MibScalar
transactionText = _TransactionText_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 69),
    _TransactionText_Type()
)
transactionText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionText.setStatus("current")
_FirstName_Type = DisplayString
_FirstName_Object = MibScalar
firstName = _FirstName_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 70),
    _FirstName_Type()
)
firstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firstName.setStatus("current")
_LastName_Type = DisplayString
_LastName_Object = MibScalar
lastName = _LastName_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 71),
    _LastName_Type()
)
lastName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastName.setStatus("current")
_SpclText_Type = DisplayString
_SpclText_Object = MibScalar
spclText = _SpclText_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 72),
    _SpclText_Type()
)
spclText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spclText.setStatus("current")
_CardNumber_Type = DisplayString
_CardNumber_Object = MibScalar
cardNumber = _CardNumber_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 73),
    _CardNumber_Type()
)
cardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardNumber.setStatus("current")
_DeviceTimePresent_Type = DisplayString
_DeviceTimePresent_Object = MibScalar
deviceTimePresent = _DeviceTimePresent_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 74),
    _DeviceTimePresent_Type()
)
deviceTimePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTimePresent.setStatus("current")
_EsjAckComment_Type = DisplayString
_EsjAckComment_Object = MibScalar
esjAckComment = _EsjAckComment_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 75),
    _EsjAckComment_Type()
)
esjAckComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esjAckComment.setStatus("current")
_PropertyValue_Type = DisplayString
_PropertyValue_Object = MibScalar
propertyValue = _PropertyValue_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 100),
    _PropertyValue_Type()
)
propertyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propertyValue.setStatus("current")
_Unit_Type = DisplayString
_Unit_Object = MibScalar
unit = _Unit_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 101),
    _Unit_Type()
)
unit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unit.setStatus("current")
_PropertyName_Type = DisplayString
_PropertyName_Object = MibScalar
propertyName = _PropertyName_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 102),
    _PropertyName_Type()
)
propertyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    propertyName.setStatus("current")
_FromState_Type = DisplayString
_FromState_Object = MibScalar
fromState = _FromState_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 103),
    _FromState_Type()
)
fromState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fromState.setStatus("current")
_VendorIdentifier_Type = DisplayString
_VendorIdentifier_Object = MibScalar
vendorIdentifier = _VendorIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 104),
    _VendorIdentifier_Type()
)
vendorIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorIdentifier.setStatus("current")
_Areas_Type = DisplayString
_Areas_Object = MibScalar
areas = _Areas_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 105),
    _Areas_Type()
)
areas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    areas.setStatus("current")
_BacnetEventType_Type = DisplayString
_BacnetEventType_Object = MibScalar
bacnetEventType = _BacnetEventType_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 106),
    _BacnetEventType_Type()
)
bacnetEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bacnetEventType.setStatus("current")
_AckComment_Type = DisplayString
_AckComment_Object = MibScalar
ackComment = _AckComment_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 107),
    _AckComment_Type()
)
ackComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ackComment.setStatus("current")
_CompleteAcknowledge_Type = DisplayString
_CompleteAcknowledge_Object = MibScalar
completeAcknowledge = _CompleteAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 108),
    _CompleteAcknowledge_Type()
)
completeAcknowledge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    completeAcknowledge.setStatus("current")
_BadgeNumber_Type = DisplayString
_BadgeNumber_Object = MibScalar
badgeNumber = _BadgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 109),
    _BadgeNumber_Type()
)
badgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    badgeNumber.setStatus("current")
_BadgeTrace_Type = DisplayString
_BadgeTrace_Object = MibScalar
badgeTrace = _BadgeTrace_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 110),
    _BadgeTrace_Type()
)
badgeTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    badgeTrace.setStatus("current")
_IssueLevel_Type = DisplayString
_IssueLevel_Object = MibScalar
issueLevel = _IssueLevel_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 111),
    _IssueLevel_Type()
)
issueLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issueLevel.setStatus("current")
_TimedOverride_Type = DisplayString
_TimedOverride_Object = MibScalar
timedOverride = _TimedOverride_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 112),
    _TimedOverride_Type()
)
timedOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timedOverride.setStatus("current")
_FacilityCode_Type = DisplayString
_FacilityCode_Object = MibScalar
facilityCode = _FacilityCode_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 113),
    _FacilityCode_Type()
)
facilityCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityCode.setStatus("current")
_Direction_Type = DisplayString
_Direction_Object = MibScalar
direction = _Direction_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 114),
    _Direction_Type()
)
direction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    direction.setStatus("current")
_FunctionKey_Type = DisplayString
_FunctionKey_Object = MibScalar
functionKey = _FunctionKey_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 115),
    _FunctionKey_Type()
)
functionKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    functionKey.setStatus("current")
_BarcodeAttach_Type = DisplayString
_BarcodeAttach_Object = MibScalar
barcodeAttach = _BarcodeAttach_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 116),
    _BarcodeAttach_Type()
)
barcodeAttach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    barcodeAttach.setStatus("current")
_TerminalName_Type = DisplayString
_TerminalName_Object = MibScalar
terminalName = _TerminalName_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 117),
    _TerminalName_Type()
)
terminalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminalName.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 118),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_AuditItemName_Type = DisplayString
_AuditItemName_Object = MibScalar
auditItemName = _AuditItemName_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 119),
    _AuditItemName_Type()
)
auditItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditItemName.setStatus("current")
_PegasysEventName_Type = DisplayString
_PegasysEventName_Object = MibScalar
pegasysEventName = _PegasysEventName_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 120),
    _PegasysEventName_Type()
)
pegasysEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pegasysEventName.setStatus("current")
_ErrorLogType_Type = DisplayString
_ErrorLogType_Object = MibScalar
errorLogType = _ErrorLogType_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 121),
    _ErrorLogType_Type()
)
errorLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorLogType.setStatus("current")
_TriggerCode_Type = DisplayString
_TriggerCode_Object = MibScalar
triggerCode = _TriggerCode_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 122),
    _TriggerCode_Type()
)
triggerCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerCode.setStatus("current")
_TriggerText_Type = DisplayString
_TriggerText_Object = MibScalar
triggerText = _TriggerText_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 123),
    _TriggerText_Type()
)
triggerText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerText.setStatus("current")
_TriggerValue_Type = DisplayString
_TriggerValue_Object = MibScalar
triggerValue = _TriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 124),
    _TriggerValue_Type()
)
triggerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triggerValue.setStatus("current")
_Reliability_Type = DisplayString
_Reliability_Object = MibScalar
reliability = _Reliability_Object(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 2, 125),
    _Reliability_Type()
)
reliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reliability.setStatus("current")
_OpcTraps_ObjectIdentity = ObjectIdentity
opcTraps = _OpcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3)
)
_OpcN1Traps_ObjectIdentity = ObjectIdentity
opcN1Traps = _OpcN1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1)
)
_OpcBacnetTraps_ObjectIdentity = ObjectIdentity
opcBacnetTraps = _OpcBacnetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2)
)
_OpcStandardTraps_ObjectIdentity = ObjectIdentity
opcStandardTraps = _OpcStandardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 3)
)

# Managed Objects groups


# Notification objects

n1HvacActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 1)
)
n1HvacActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1HvacActiveConditionalEvent.setStatus(
        "current"
    )

n1HvacInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 2)
)
n1HvacInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1HvacInactiveConditionalEvent.setStatus(
        "current"
    )

n1HvacConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 3)
)
n1HvacConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "esjAckComment"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1HvacConditionalEventAcknowledged.setStatus(
        "current"
    )

n1FireActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 4)
)
n1FireActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1FireActiveConditionalEvent.setStatus(
        "current"
    )

n1FireInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 5)
)
n1FireInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1FireInactiveConditionalEvent.setStatus(
        "current"
    )

n1FireConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 6)
)
n1FireConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "esjAckComment"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1FireConditionalEventAcknowledged.setStatus(
        "current"
    )

n1ServicesActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 7)
)
n1ServicesActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1ServicesActiveConditionalEvent.setStatus(
        "current"
    )

n1ServicesInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 8)
)
n1ServicesInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1ServicesInactiveConditionalEvent.setStatus(
        "current"
    )

n1ServicesConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 9)
)
n1ServicesConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "esjAckComment"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1ServicesConditionalEventAcknowledged.setStatus(
        "current"
    )

n1SecurityActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 10)
)
n1SecurityActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1SecurityActiveConditionalEvent.setStatus(
        "current"
    )

n1SecurityInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 11)
)
n1SecurityInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "lastName"),
        ("JCImSeries-MIB", "firstName"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "cardNumber"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "featureStatus"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1SecurityInactiveConditionalEvent.setStatus(
        "current"
    )

n1SecurityConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 12)
)
n1SecurityConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "lastName"),
        ("JCImSeries-MIB", "firstName"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "cardNumber"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "featureStatus"),
        ("JCImSeries-MIB", "esjAckComment"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1SecurityConditionalEventAcknowledged.setStatus(
        "current"
    )

n1AdminActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 13)
)
n1AdminActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1AdminActiveConditionalEvent.setStatus(
        "current"
    )

n1AdminInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 14)
)
n1AdminInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1AdminInactiveConditionalEvent.setStatus(
        "current"
    )

n1AdminConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 15)
)
n1AdminConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "esjAckComment"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1AdminConditionalEventAcknowledged.setStatus(
        "current"
    )

n1GeneralActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 16)
)
n1GeneralActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1GeneralActiveConditionalEvent.setStatus(
        "current"
    )

n1GeneralInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 17)
)
n1GeneralInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1GeneralInactiveConditionalEvent.setStatus(
        "current"
    )

n1GeneralConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 18)
)
n1GeneralConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "esjAckComment"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1GeneralConditionalEventAcknowledged.setStatus(
        "current"
    )

n1HvacSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 19)
)
n1HvacSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1HvacSimpleEvent.setStatus(
        "current"
    )

n1FireSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 20)
)
n1FireSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1FireSimpleEvent.setStatus(
        "current"
    )

n1ServicesSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 21)
)
n1ServicesSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1ServicesSimpleEvent.setStatus(
        "current"
    )

n1SecuritySimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 22)
)
n1SecuritySimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1SecuritySimpleEvent.setStatus(
        "current"
    )

n1AdminSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 23)
)
n1AdminSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1AdminSimpleEvent.setStatus(
        "current"
    )

n1GeneralSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 24)
)
n1GeneralSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1GeneralSimpleEvent.setStatus(
        "current"
    )

n1HvacTrackingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 25)
)
n1HvacTrackingEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "originalDate"),
        ("JCImSeries-MIB", "originalTime"),
        ("JCImSeries-MIB", "featureStatus"),
        ("JCImSeries-MIB", "reportDate"),
        ("JCImSeries-MIB", "reportTime"),
        ("JCImSeries-MIB", "location"),
        ("JCImSeries-MIB", "deviceName"),
        ("JCImSeries-MIB", "userID"),
        ("JCImSeries-MIB", "accssLevel"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1HvacTrackingEvent.setStatus(
        "current"
    )

n1FireTrackingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 26)
)
n1FireTrackingEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "featureStatus"),
        ("JCImSeries-MIB", "reportDate"),
        ("JCImSeries-MIB", "reportTime"),
        ("JCImSeries-MIB", "location"),
        ("JCImSeries-MIB", "deviceName"),
        ("JCImSeries-MIB", "userID"),
        ("JCImSeries-MIB", "accssLevel"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1FireTrackingEvent.setStatus(
        "current"
    )

n1ServicesTrackingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 27)
)
n1ServicesTrackingEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "originalDate"),
        ("JCImSeries-MIB", "originalTime"),
        ("JCImSeries-MIB", "featureStatus"),
        ("JCImSeries-MIB", "reportDate"),
        ("JCImSeries-MIB", "reportTime"),
        ("JCImSeries-MIB", "location"),
        ("JCImSeries-MIB", "deviceName"),
        ("JCImSeries-MIB", "userID"),
        ("JCImSeries-MIB", "accssLevel"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1ServicesTrackingEvent.setStatus(
        "current"
    )

n1SecurityTrackingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 28)
)
n1SecurityTrackingEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "lastName"),
        ("JCImSeries-MIB", "firstName"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "cardNumber"),
        ("JCImSeries-MIB", "featureStatus"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1SecurityTrackingEvent.setStatus(
        "current"
    )

n1AdminTrackingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 29)
)
n1AdminTrackingEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "originalDate"),
        ("JCImSeries-MIB", "originalTime"),
        ("JCImSeries-MIB", "featureStatus"),
        ("JCImSeries-MIB", "reportDate"),
        ("JCImSeries-MIB", "reportTime"),
        ("JCImSeries-MIB", "location"),
        ("JCImSeries-MIB", "deviceName"),
        ("JCImSeries-MIB", "userID"),
        ("JCImSeries-MIB", "accssLevel"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1AdminTrackingEvent.setStatus(
        "current"
    )

n1GeneralTrackingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 1, 0, 30)
)
n1GeneralTrackingEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "presentvalue"),
        ("JCImSeries-MIB", "units"),
        ("JCImSeries-MIB", "spclText"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "expandedID"),
        ("JCImSeries-MIB", "originalDate"),
        ("JCImSeries-MIB", "originalTime"),
        ("JCImSeries-MIB", "featureStatus"),
        ("JCImSeries-MIB", "reportDate"),
        ("JCImSeries-MIB", "reportTime"),
        ("JCImSeries-MIB", "location"),
        ("JCImSeries-MIB", "deviceName"),
        ("JCImSeries-MIB", "userID"),
        ("JCImSeries-MIB", "accssLevel"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    n1GeneralTrackingEvent.setStatus(
        "current"
    )

bacnetDeviceFailureActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 1)
)
bacnetDeviceFailureActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetDeviceFailureActiveConditionalEvent.setStatus(
        "current"
    )

bacnetDeviceFailureInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 2)
)
bacnetDeviceFailureInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetDeviceFailureInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetDeviceFailureConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 3)
)
bacnetDeviceFailureConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetDeviceFailureConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetHvacActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 4)
)
bacnetHvacActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetHvacActiveConditionalEvent.setStatus(
        "current"
    )

bacnetHvacInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 5)
)
bacnetHvacInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetHvacInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetHvacConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 6)
)
bacnetHvacConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetHvacConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetFireActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 7)
)
bacnetFireActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetFireActiveConditionalEvent.setStatus(
        "current"
    )

bacnetFireInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 8)
)
bacnetFireInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetFireInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetFireConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 9)
)
bacnetFireConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetFireConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetSecurityActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 10)
)
bacnetSecurityActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetSecurityActiveConditionalEvent.setStatus(
        "current"
    )

bacnetSecurityInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 11)
)
bacnetSecurityInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetSecurityInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetSecurityConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 12)
)
bacnetSecurityConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetSecurityConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetServicesActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 13)
)
bacnetServicesActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetServicesActiveConditionalEvent.setStatus(
        "current"
    )

bacnetServicesInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 14)
)
bacnetServicesInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetServicesInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetServicesConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 15)
)
bacnetServicesConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetServicesConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetAdminActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 16)
)
bacnetAdminActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetAdminActiveConditionalEvent.setStatus(
        "current"
    )

bacnetAdminInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 17)
)
bacnetAdminInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetAdminInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetAdminConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 18)
)
bacnetAdminConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetAdminConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetGeneralAlarmActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 19)
)
bacnetGeneralAlarmActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetGeneralAlarmActiveConditionalEvent.setStatus(
        "current"
    )

bacnetGeneralAlarmInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 20)
)
bacnetGeneralAlarmInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetGeneralAlarmInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetGeneralAlarmConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 21)
)
bacnetGeneralAlarmConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetGeneralAlarmConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetGeneralEventActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 22)
)
bacnetGeneralEventActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetGeneralEventActiveConditionalEvent.setStatus(
        "current"
    )

bacnetGeneralEventInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 23)
)
bacnetGeneralEventInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetGeneralEventInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetGeneralEventConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 24)
)
bacnetGeneralEventConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "deviceTimePresent"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetGeneralEventConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetPanelEventActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 25)
)
bacnetPanelEventActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "terminalName"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetPanelEventActiveConditionalEvent.setStatus(
        "current"
    )

bacnetPanelEventInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 26)
)
bacnetPanelEventInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "terminalName"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetPanelEventInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetPanelEventConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 27)
)
bacnetPanelEventConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "terminalName"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetPanelEventConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetPanelHWStatusActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 28)
)
bacnetPanelHWStatusActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "terminalName"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetPanelHWStatusActiveConditionalEvent.setStatus(
        "current"
    )

bacnetPanelHWStatusInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 29)
)
bacnetPanelHWStatusInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "terminalName"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetPanelHWStatusInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetPanelHWStatusConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 30)
)
bacnetPanelHWStatusConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "terminalName"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetPanelHWStatusConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetHostLogActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 31)
)
bacnetHostLogActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "userName"),
        ("JCImSeries-MIB", "auditItemName"),
        ("JCImSeries-MIB", "pegasysEventName"),
        ("JCImSeries-MIB", "errorLogType"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetHostLogActiveConditionalEvent.setStatus(
        "current"
    )

bacnetHostLogInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 32)
)
bacnetHostLogInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "userName"),
        ("JCImSeries-MIB", "auditItemName"),
        ("JCImSeries-MIB", "pegasysEventName"),
        ("JCImSeries-MIB", "errorLogType"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetHostLogInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetHostLogConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 33)
)
bacnetHostLogConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "userName"),
        ("JCImSeries-MIB", "auditItemName"),
        ("JCImSeries-MIB", "pegasysEventName"),
        ("JCImSeries-MIB", "errorLogType"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetHostLogConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetOutputPointStatusActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 34)
)
bacnetOutputPointStatusActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetOutputPointStatusActiveConditionalEvent.setStatus(
        "current"
    )

bacnetOutputPointStatusInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 35)
)
bacnetOutputPointStatusInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetOutputPointStatusInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetOutputPointStatusConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 36)
)
bacnetOutputPointStatusConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetOutputPointStatusConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetInputPointStatusActiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 37)
)
bacnetInputPointStatusActiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetInputPointStatusActiveConditionalEvent.setStatus(
        "current"
    )

bacnetInputPointStatusInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 38)
)
bacnetInputPointStatusInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetInputPointStatusInactiveConditionalEvent.setStatus(
        "current"
    )

bacnetInputPointStatusConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 39)
)
bacnetInputPointStatusConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "ackComment"),
        ("JCImSeries-MIB", "completeAcknowledge"),
        ("JCImSeries-MIB", "reliability"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetInputPointStatusConditionalEventAcknowledged.setStatus(
        "current"
    )

bacnetHvacSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 40)
)
bacnetHvacSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetHvacSimpleEvent.setStatus(
        "current"
    )

bacnetFireSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 41)
)
bacnetFireSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetFireSimpleEvent.setStatus(
        "current"
    )

bacnetSecuritySimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 42)
)
bacnetSecuritySimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetSecuritySimpleEvent.setStatus(
        "current"
    )

bacnetServicesSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 43)
)
bacnetServicesSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetServicesSimpleEvent.setStatus(
        "current"
    )

bacnetAdminSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 44)
)
bacnetAdminSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "propertyName"),
        ("JCImSeries-MIB", "unit"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetAdminSimpleEvent.setStatus(
        "current"
    )

bacnetAccessGrantSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 45)
)
bacnetAccessGrantSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "badgeTrace"),
        ("JCImSeries-MIB", "badgeNumber"),
        ("JCImSeries-MIB", "lastName"),
        ("JCImSeries-MIB", "firstName"),
        ("JCImSeries-MIB", "issueLevel"),
        ("JCImSeries-MIB", "timedOverride"),
        ("JCImSeries-MIB", "facilityCode"),
        ("JCImSeries-MIB", "direction"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetAccessGrantSimpleEvent.setStatus(
        "current"
    )

bacnetAccessDenySimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 46)
)
bacnetAccessDenySimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "badgeTrace"),
        ("JCImSeries-MIB", "badgeNumber"),
        ("JCImSeries-MIB", "lastName"),
        ("JCImSeries-MIB", "firstName"),
        ("JCImSeries-MIB", "issueLevel"),
        ("JCImSeries-MIB", "timedOverride"),
        ("JCImSeries-MIB", "facilityCode"),
        ("JCImSeries-MIB", "direction"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetAccessDenySimpleEvent.setStatus(
        "current"
    )

bacnetCardTraceSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 47)
)
bacnetCardTraceSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "badgeTrace"),
        ("JCImSeries-MIB", "badgeNumber"),
        ("JCImSeries-MIB", "lastName"),
        ("JCImSeries-MIB", "firstName"),
        ("JCImSeries-MIB", "issueLevel"),
        ("JCImSeries-MIB", "timedOverride"),
        ("JCImSeries-MIB", "facilityCode"),
        ("JCImSeries-MIB", "direction"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetCardTraceSimpleEvent.setStatus(
        "current"
    )

bacnetTAAccessGrantSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 48)
)
bacnetTAAccessGrantSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "badgeTrace"),
        ("JCImSeries-MIB", "badgeNumber"),
        ("JCImSeries-MIB", "lastName"),
        ("JCImSeries-MIB", "firstName"),
        ("JCImSeries-MIB", "timedOverride"),
        ("JCImSeries-MIB", "direction"),
        ("JCImSeries-MIB", "functionKey"),
        ("JCImSeries-MIB", "barcodeAttach"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetTAAccessGrantSimpleEvent.setStatus(
        "current"
    )

bacnetOutputPointStatusSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 49)
)
bacnetOutputPointStatusSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetOutputPointStatusSimpleEvent.setStatus(
        "current"
    )

bacnetInputPointStatusSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 50)
)
bacnetInputPointStatusSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "propertyValue"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetInputPointStatusSimpleEvent.setStatus(
        "current"
    )

bacnetAuditSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 51)
)
bacnetAuditSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "userName"),
        ("JCImSeries-MIB", "auditItemName"),
        ("JCImSeries-MIB", "pegasysEventName"),
        ("JCImSeries-MIB", "errorLogType"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetAuditSimpleEvent.setStatus(
        "current"
    )

bacnetHostEventSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 52)
)
bacnetHostEventSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "userName"),
        ("JCImSeries-MIB", "auditItemName"),
        ("JCImSeries-MIB", "pegasysEventName"),
        ("JCImSeries-MIB", "errorLogType"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetHostEventSimpleEvent.setStatus(
        "current"
    )

bacnetHostLogSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 53)
)
bacnetHostLogSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "userName"),
        ("JCImSeries-MIB", "auditItemName"),
        ("JCImSeries-MIB", "pegasysEventName"),
        ("JCImSeries-MIB", "errorLogType"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetHostLogSimpleEvent.setStatus(
        "current"
    )

bacnetHostLogicSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 54)
)
bacnetHostLogicSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "triggerCode"),
        ("JCImSeries-MIB", "triggerText"),
        ("JCImSeries-MIB", "triggerValue"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetHostLogicSimpleEvent.setStatus(
        "current"
    )

bacnetPanelEventSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 55)
)
bacnetPanelEventSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "terminalName"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetPanelEventSimpleEvent.setStatus(
        "current"
    )

bacnetPanelHWStatusSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 56)
)
bacnetPanelHWStatusSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "bacnetEventType"),
        ("JCImSeries-MIB", "vendorIdentifier"),
        ("JCImSeries-MIB", "areas"),
        ("JCImSeries-MIB", "fromState"),
        ("JCImSeries-MIB", "terminalName"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetPanelHWStatusSimpleEvent.setStatus(
        "current"
    )

bacnetCommErrorSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 57)
)
bacnetCommErrorSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetCommErrorSimpleEvent.setStatus(
        "current"
    )

bacnetGeneralSimpleEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 2, 0, 58)
)
bacnetGeneralSimpleEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    bacnetGeneralSimpleEvent.setStatus(
        "current"
    )

opcStandardActiveGeneralConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 3, 0, 1)
)
opcStandardActiveGeneralConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    opcStandardActiveGeneralConditionalEvent.setStatus(
        "current"
    )

opcStandardInactiveConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 3, 0, 2)
)
opcStandardInactiveConditionalEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    opcStandardInactiveConditionalEvent.setStatus(
        "current"
    )

opcStandardGeneralConditionalEventAcknowledged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 3, 0, 3)
)
opcStandardGeneralConditionalEventAcknowledged.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcSubCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcActorID"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    opcStandardGeneralConditionalEventAcknowledged.setStatus(
        "current"
    )

opcStandardSimpleNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 3, 0, 4)
)
opcStandardSimpleNotification.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    opcStandardSimpleNotification.setStatus(
        "current"
    )

opcStandardTrackingEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4399, 2, 1, 10, 3, 3, 0, 5)
)
opcStandardTrackingEvent.setObjects(
      *(("JCImSeries-MIB", "opcSeverity"),
        ("JCImSeries-MIB", "opcCondition"),
        ("JCImSeries-MIB", "opcSource"),
        ("JCImSeries-MIB", "opcMessage"),
        ("JCImSeries-MIB", "opcTimeStamp"),
        ("JCImSeries-MIB", "opcEventTypeText"),
        ("JCImSeries-MIB", "opcEventCategoryText"),
        ("JCImSeries-MIB", "opcActiveTime"),
        ("JCImSeries-MIB", "opcQualityText"),
        ("JCImSeries-MIB", "opcNewStateText"),
        ("JCImSeries-MIB", "opcChangeMaskText"),
        ("JCImSeries-MIB", "opcAckRequired"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    opcStandardTrackingEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JCImSeries-MIB",
    **{"jcimSeriesMIB": jcimSeriesMIB,
       "opcTypes": opcTypes,
       "opcSeverity": opcSeverity,
       "opcSource": opcSource,
       "opcTimeStamp": opcTimeStamp,
       "opcMessage": opcMessage,
       "opcEventCategory": opcEventCategory,
       "opcEventCategoryText": opcEventCategoryText,
       "opcEventType": opcEventType,
       "opcEventTypeText": opcEventTypeText,
       "opcCondition": opcCondition,
       "opcSubCondition": opcSubCondition,
       "opcActiveTime": opcActiveTime,
       "opcQuality": opcQuality,
       "opcQualityText": opcQualityText,
       "opcNewState": opcNewState,
       "opcNewStateText": opcNewStateText,
       "opcAckRequired": opcAckRequired,
       "opcAckRequiredText": opcAckRequiredText,
       "opcCookie": opcCookie,
       "opcChangeMaskText": opcChangeMaskText,
       "opcActorID": opcActorID,
       "opcChangeMask": opcChangeMask,
       "originalDate": originalDate,
       "originalTime": originalTime,
       "networkName": networkName,
       "ncmName": ncmName,
       "systemID": systemID,
       "id": id,
       "expandedID": expandedID,
       "presentvalue": presentvalue,
       "units": units,
       "reportType": reportType,
       "alarmType": alarmType,
       "availattribute1": availattribute1,
       "alarmPriority": alarmPriority,
       "featureStatus": featureStatus,
       "reportDate": reportDate,
       "reportTime": reportTime,
       "transactionType": transactionType,
       "transactionTypeText": transactionTypeText,
       "location": location,
       "deviceName": deviceName,
       "userID": userID,
       "accssLevel": accssLevel,
       "transactionText": transactionText,
       "firstName": firstName,
       "lastName": lastName,
       "spclText": spclText,
       "cardNumber": cardNumber,
       "deviceTimePresent": deviceTimePresent,
       "esjAckComment": esjAckComment,
       "propertyValue": propertyValue,
       "unit": unit,
       "propertyName": propertyName,
       "fromState": fromState,
       "vendorIdentifier": vendorIdentifier,
       "areas": areas,
       "bacnetEventType": bacnetEventType,
       "ackComment": ackComment,
       "completeAcknowledge": completeAcknowledge,
       "badgeNumber": badgeNumber,
       "badgeTrace": badgeTrace,
       "issueLevel": issueLevel,
       "timedOverride": timedOverride,
       "facilityCode": facilityCode,
       "direction": direction,
       "functionKey": functionKey,
       "barcodeAttach": barcodeAttach,
       "terminalName": terminalName,
       "userName": userName,
       "auditItemName": auditItemName,
       "pegasysEventName": pegasysEventName,
       "errorLogType": errorLogType,
       "triggerCode": triggerCode,
       "triggerText": triggerText,
       "triggerValue": triggerValue,
       "reliability": reliability,
       "opcTraps": opcTraps,
       "opcN1Traps": opcN1Traps,
       "n1HvacActiveConditionalEvent": n1HvacActiveConditionalEvent,
       "n1HvacInactiveConditionalEvent": n1HvacInactiveConditionalEvent,
       "n1HvacConditionalEventAcknowledged": n1HvacConditionalEventAcknowledged,
       "n1FireActiveConditionalEvent": n1FireActiveConditionalEvent,
       "n1FireInactiveConditionalEvent": n1FireInactiveConditionalEvent,
       "n1FireConditionalEventAcknowledged": n1FireConditionalEventAcknowledged,
       "n1ServicesActiveConditionalEvent": n1ServicesActiveConditionalEvent,
       "n1ServicesInactiveConditionalEvent": n1ServicesInactiveConditionalEvent,
       "n1ServicesConditionalEventAcknowledged": n1ServicesConditionalEventAcknowledged,
       "n1SecurityActiveConditionalEvent": n1SecurityActiveConditionalEvent,
       "n1SecurityInactiveConditionalEvent": n1SecurityInactiveConditionalEvent,
       "n1SecurityConditionalEventAcknowledged": n1SecurityConditionalEventAcknowledged,
       "n1AdminActiveConditionalEvent": n1AdminActiveConditionalEvent,
       "n1AdminInactiveConditionalEvent": n1AdminInactiveConditionalEvent,
       "n1AdminConditionalEventAcknowledged": n1AdminConditionalEventAcknowledged,
       "n1GeneralActiveConditionalEvent": n1GeneralActiveConditionalEvent,
       "n1GeneralInactiveConditionalEvent": n1GeneralInactiveConditionalEvent,
       "n1GeneralConditionalEventAcknowledged": n1GeneralConditionalEventAcknowledged,
       "n1HvacSimpleEvent": n1HvacSimpleEvent,
       "n1FireSimpleEvent": n1FireSimpleEvent,
       "n1ServicesSimpleEvent": n1ServicesSimpleEvent,
       "n1SecuritySimpleEvent": n1SecuritySimpleEvent,
       "n1AdminSimpleEvent": n1AdminSimpleEvent,
       "n1GeneralSimpleEvent": n1GeneralSimpleEvent,
       "n1HvacTrackingEvent": n1HvacTrackingEvent,
       "n1FireTrackingEvent": n1FireTrackingEvent,
       "n1ServicesTrackingEvent": n1ServicesTrackingEvent,
       "n1SecurityTrackingEvent": n1SecurityTrackingEvent,
       "n1AdminTrackingEvent": n1AdminTrackingEvent,
       "n1GeneralTrackingEvent": n1GeneralTrackingEvent,
       "opcBacnetTraps": opcBacnetTraps,
       "bacnetDeviceFailureActiveConditionalEvent": bacnetDeviceFailureActiveConditionalEvent,
       "bacnetDeviceFailureInactiveConditionalEvent": bacnetDeviceFailureInactiveConditionalEvent,
       "bacnetDeviceFailureConditionalEventAcknowledged": bacnetDeviceFailureConditionalEventAcknowledged,
       "bacnetHvacActiveConditionalEvent": bacnetHvacActiveConditionalEvent,
       "bacnetHvacInactiveConditionalEvent": bacnetHvacInactiveConditionalEvent,
       "bacnetHvacConditionalEventAcknowledged": bacnetHvacConditionalEventAcknowledged,
       "bacnetFireActiveConditionalEvent": bacnetFireActiveConditionalEvent,
       "bacnetFireInactiveConditionalEvent": bacnetFireInactiveConditionalEvent,
       "bacnetFireConditionalEventAcknowledged": bacnetFireConditionalEventAcknowledged,
       "bacnetSecurityActiveConditionalEvent": bacnetSecurityActiveConditionalEvent,
       "bacnetSecurityInactiveConditionalEvent": bacnetSecurityInactiveConditionalEvent,
       "bacnetSecurityConditionalEventAcknowledged": bacnetSecurityConditionalEventAcknowledged,
       "bacnetServicesActiveConditionalEvent": bacnetServicesActiveConditionalEvent,
       "bacnetServicesInactiveConditionalEvent": bacnetServicesInactiveConditionalEvent,
       "bacnetServicesConditionalEventAcknowledged": bacnetServicesConditionalEventAcknowledged,
       "bacnetAdminActiveConditionalEvent": bacnetAdminActiveConditionalEvent,
       "bacnetAdminInactiveConditionalEvent": bacnetAdminInactiveConditionalEvent,
       "bacnetAdminConditionalEventAcknowledged": bacnetAdminConditionalEventAcknowledged,
       "bacnetGeneralAlarmActiveConditionalEvent": bacnetGeneralAlarmActiveConditionalEvent,
       "bacnetGeneralAlarmInactiveConditionalEvent": bacnetGeneralAlarmInactiveConditionalEvent,
       "bacnetGeneralAlarmConditionalEventAcknowledged": bacnetGeneralAlarmConditionalEventAcknowledged,
       "bacnetGeneralEventActiveConditionalEvent": bacnetGeneralEventActiveConditionalEvent,
       "bacnetGeneralEventInactiveConditionalEvent": bacnetGeneralEventInactiveConditionalEvent,
       "bacnetGeneralEventConditionalEventAcknowledged": bacnetGeneralEventConditionalEventAcknowledged,
       "bacnetPanelEventActiveConditionalEvent": bacnetPanelEventActiveConditionalEvent,
       "bacnetPanelEventInactiveConditionalEvent": bacnetPanelEventInactiveConditionalEvent,
       "bacnetPanelEventConditionalEventAcknowledged": bacnetPanelEventConditionalEventAcknowledged,
       "bacnetPanelHWStatusActiveConditionalEvent": bacnetPanelHWStatusActiveConditionalEvent,
       "bacnetPanelHWStatusInactiveConditionalEvent": bacnetPanelHWStatusInactiveConditionalEvent,
       "bacnetPanelHWStatusConditionalEventAcknowledged": bacnetPanelHWStatusConditionalEventAcknowledged,
       "bacnetHostLogActiveConditionalEvent": bacnetHostLogActiveConditionalEvent,
       "bacnetHostLogInactiveConditionalEvent": bacnetHostLogInactiveConditionalEvent,
       "bacnetHostLogConditionalEventAcknowledged": bacnetHostLogConditionalEventAcknowledged,
       "bacnetOutputPointStatusActiveConditionalEvent": bacnetOutputPointStatusActiveConditionalEvent,
       "bacnetOutputPointStatusInactiveConditionalEvent": bacnetOutputPointStatusInactiveConditionalEvent,
       "bacnetOutputPointStatusConditionalEventAcknowledged": bacnetOutputPointStatusConditionalEventAcknowledged,
       "bacnetInputPointStatusActiveConditionalEvent": bacnetInputPointStatusActiveConditionalEvent,
       "bacnetInputPointStatusInactiveConditionalEvent": bacnetInputPointStatusInactiveConditionalEvent,
       "bacnetInputPointStatusConditionalEventAcknowledged": bacnetInputPointStatusConditionalEventAcknowledged,
       "bacnetHvacSimpleEvent": bacnetHvacSimpleEvent,
       "bacnetFireSimpleEvent": bacnetFireSimpleEvent,
       "bacnetSecuritySimpleEvent": bacnetSecuritySimpleEvent,
       "bacnetServicesSimpleEvent": bacnetServicesSimpleEvent,
       "bacnetAdminSimpleEvent": bacnetAdminSimpleEvent,
       "bacnetAccessGrantSimpleEvent": bacnetAccessGrantSimpleEvent,
       "bacnetAccessDenySimpleEvent": bacnetAccessDenySimpleEvent,
       "bacnetCardTraceSimpleEvent": bacnetCardTraceSimpleEvent,
       "bacnetTAAccessGrantSimpleEvent": bacnetTAAccessGrantSimpleEvent,
       "bacnetOutputPointStatusSimpleEvent": bacnetOutputPointStatusSimpleEvent,
       "bacnetInputPointStatusSimpleEvent": bacnetInputPointStatusSimpleEvent,
       "bacnetAuditSimpleEvent": bacnetAuditSimpleEvent,
       "bacnetHostEventSimpleEvent": bacnetHostEventSimpleEvent,
       "bacnetHostLogSimpleEvent": bacnetHostLogSimpleEvent,
       "bacnetHostLogicSimpleEvent": bacnetHostLogicSimpleEvent,
       "bacnetPanelEventSimpleEvent": bacnetPanelEventSimpleEvent,
       "bacnetPanelHWStatusSimpleEvent": bacnetPanelHWStatusSimpleEvent,
       "bacnetCommErrorSimpleEvent": bacnetCommErrorSimpleEvent,
       "bacnetGeneralSimpleEvent": bacnetGeneralSimpleEvent,
       "opcStandardTraps": opcStandardTraps,
       "opcStandardActiveGeneralConditionalEvent": opcStandardActiveGeneralConditionalEvent,
       "opcStandardInactiveConditionalEvent": opcStandardInactiveConditionalEvent,
       "opcStandardGeneralConditionalEventAcknowledged": opcStandardGeneralConditionalEventAcknowledged,
       "opcStandardSimpleNotification": opcStandardSimpleNotification,
       "opcStandardTrackingEvent": opcStandardTrackingEvent}
)
