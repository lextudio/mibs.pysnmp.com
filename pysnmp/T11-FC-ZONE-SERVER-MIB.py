# SNMP MIB module (T11-FC-ZONE-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-ZONE-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:21 2024
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

(FcDomainIdOrZero,
 FcNameIdOrZero,
 fcmInstanceIndex,
 fcmSwitchIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcDomainIdOrZero",
    "FcNameIdOrZero",
    "fcmInstanceIndex",
    "fcmSwitchIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(t11FamLocalSwitchWwn,) = mibBuilder.importSymbols(
    "T11-FC-FABRIC-ADDR-MGR-MIB",
    "t11FamLocalSwitchWwn")

(T11NsGs4RejectReasonCode,) = mibBuilder.importSymbols(
    "T11-FC-NAME-SERVER-MIB",
    "T11NsGs4RejectReasonCode")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11ZoneServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 160)
)
t11ZoneServerMIB.setRevisions(
        ("2007-06-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class T11ZsZoneMemberType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class T11ZsRejectReasonExplanation(Integer32, TextualConvention):
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
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("aliasExists", 18),
          ("aliasUnknown", 21),
          ("basicZoningCmdsNotSupported", 24),
          ("capabilityNotSupported", 12),
          ("cmitInProcess", 28),
          ("consistencyChecksFailed", 31),
          ("deactivateZoneSetFailed", 10),
          ("enhancedZoningCmdsNotSupported", 15),
          ("hardEnforcementFailed", 29),
          ("incorrectPayloadLen", 8),
          ("invalidZoneSetDefinition", 14),
          ("noAdditionalExplanation", 2),
          ("noZoneSetActive", 5),
          ("other", 1),
          ("reqNotSupported", 11),
          ("requestInProcess", 27),
          ("tooLargeZoneSet", 9),
          ("unableEnhancedMode", 23),
          ("unresolvedReferences", 30),
          ("zoneAliasTypeUnknown", 22),
          ("zoneAttribObjectExists", 25),
          ("zoneAttribObjectUnknown", 26),
          ("zoneExists", 17),
          ("zoneMemberIDTypeNotSupp", 13),
          ("zoneNameUnknown", 6),
          ("zoneSetExists", 16),
          ("zoneSetNameUnknown", 4),
          ("zoneSetUnknown", 19),
          ("zoneStateUnknown", 7),
          ("zoneUnknown", 20),
          ("zonesNotSupported", 3))
    )



class T11ZoningName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



# MIB Managed Objects in the order of their OIDs

_T11ZsMIBNotifications_ObjectIdentity = ObjectIdentity
t11ZsMIBNotifications = _T11ZsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 160, 0)
)
_T11ZsMIBObjects_ObjectIdentity = ObjectIdentity
t11ZsMIBObjects = _T11ZsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 160, 1)
)
_T11ZsConfiguration_ObjectIdentity = ObjectIdentity
t11ZsConfiguration = _T11ZsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 160, 1, 1)
)
_T11ZsServerTable_Object = MibTable
t11ZsServerTable = _T11ZsServerTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11ZsServerTable.setStatus("current")
_T11ZsServerEntry_Object = MibTableRow
t11ZsServerEntry = _T11ZsServerEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1)
)
t11ZsServerEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
)
if mibBuilder.loadTexts:
    t11ZsServerEntry.setStatus("current")
_T11ZsServerFabricIndex_Type = T11FabricIndex
_T11ZsServerFabricIndex_Object = MibTableColumn
t11ZsServerFabricIndex = _T11ZsServerFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 1),
    _T11ZsServerFabricIndex_Type()
)
t11ZsServerFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsServerFabricIndex.setStatus("current")


class _T11ZsServerCapabilityObject_Type(Bits):
    """Custom type t11ZsServerCapabilityObject based on Bits"""
    namedValues = NamedValues(
        *(("activateDirect", 2),
          ("enhancedMode", 0),
          ("hardZoning", 3),
          ("zoneSetDb", 1))
    )

_T11ZsServerCapabilityObject_Type.__name__ = "Bits"
_T11ZsServerCapabilityObject_Object = MibTableColumn
t11ZsServerCapabilityObject = _T11ZsServerCapabilityObject_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 2),
    _T11ZsServerCapabilityObject_Type()
)
t11ZsServerCapabilityObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsServerCapabilityObject.setStatus("current")


class _T11ZsServerDatabaseStorageType_Type(StorageType):
    """Custom type t11ZsServerDatabaseStorageType based on StorageType"""


_T11ZsServerDatabaseStorageType_Object = MibTableColumn
t11ZsServerDatabaseStorageType = _T11ZsServerDatabaseStorageType_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 3),
    _T11ZsServerDatabaseStorageType_Type()
)
t11ZsServerDatabaseStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsServerDatabaseStorageType.setStatus("current")


class _T11ZsServerDistribute_Type(Integer32):
    """Custom type t11ZsServerDistribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("zoneSetDb", 2))
    )


_T11ZsServerDistribute_Type.__name__ = "Integer32"
_T11ZsServerDistribute_Object = MibTableColumn
t11ZsServerDistribute = _T11ZsServerDistribute_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 4),
    _T11ZsServerDistribute_Type()
)
t11ZsServerDistribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsServerDistribute.setStatus("current")


class _T11ZsServerCommit_Type(Integer32):
    """Custom type t11ZsServerCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commitZoneChanges", 1),
          ("noop", 2))
    )


_T11ZsServerCommit_Type.__name__ = "Integer32"
_T11ZsServerCommit_Object = MibTableColumn
t11ZsServerCommit = _T11ZsServerCommit_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 5),
    _T11ZsServerCommit_Type()
)
t11ZsServerCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsServerCommit.setStatus("current")


class _T11ZsServerResult_Type(Integer32):
    """Custom type t11ZsServerResult based on Integer32"""
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
        *(("inProgress", 2),
          ("none", 1),
          ("otherFailure", 5),
          ("rejectFailure", 4),
          ("success", 3))
    )


_T11ZsServerResult_Type.__name__ = "Integer32"
_T11ZsServerResult_Object = MibTableColumn
t11ZsServerResult = _T11ZsServerResult_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 6),
    _T11ZsServerResult_Type()
)
t11ZsServerResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsServerResult.setStatus("current")
_T11ZsServerReasonCode_Type = T11NsGs4RejectReasonCode
_T11ZsServerReasonCode_Object = MibTableColumn
t11ZsServerReasonCode = _T11ZsServerReasonCode_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 7),
    _T11ZsServerReasonCode_Type()
)
t11ZsServerReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsServerReasonCode.setStatus("current")


class _T11ZsServerReasonCodeExp_Type(OctetString):
    """Custom type t11ZsServerReasonCodeExp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_T11ZsServerReasonCodeExp_Type.__name__ = "OctetString"
_T11ZsServerReasonCodeExp_Object = MibTableColumn
t11ZsServerReasonCodeExp = _T11ZsServerReasonCodeExp_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 8),
    _T11ZsServerReasonCodeExp_Type()
)
t11ZsServerReasonCodeExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsServerReasonCodeExp.setStatus("current")


class _T11ZsServerReasonVendorCode_Type(OctetString):
    """Custom type t11ZsServerReasonVendorCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_T11ZsServerReasonVendorCode_Type.__name__ = "OctetString"
_T11ZsServerReasonVendorCode_Object = MibTableColumn
t11ZsServerReasonVendorCode = _T11ZsServerReasonVendorCode_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 9),
    _T11ZsServerReasonVendorCode_Type()
)
t11ZsServerReasonVendorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsServerReasonVendorCode.setStatus("current")
_T11ZsServerLastChange_Type = TimeStamp
_T11ZsServerLastChange_Object = MibTableColumn
t11ZsServerLastChange = _T11ZsServerLastChange_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 10),
    _T11ZsServerLastChange_Type()
)
t11ZsServerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsServerLastChange.setStatus("current")
_T11ZsServerHardZoning_Type = TruthValue
_T11ZsServerHardZoning_Object = MibTableColumn
t11ZsServerHardZoning = _T11ZsServerHardZoning_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 11),
    _T11ZsServerHardZoning_Type()
)
t11ZsServerHardZoning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsServerHardZoning.setStatus("current")


class _T11ZsServerReadFromDatabase_Type(Integer32):
    """Custom type t11ZsServerReadFromDatabase based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("committedDB", 1),
          ("copyDB", 2))
    )


_T11ZsServerReadFromDatabase_Type.__name__ = "Integer32"
_T11ZsServerReadFromDatabase_Object = MibTableColumn
t11ZsServerReadFromDatabase = _T11ZsServerReadFromDatabase_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 12),
    _T11ZsServerReadFromDatabase_Type()
)
t11ZsServerReadFromDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsServerReadFromDatabase.setStatus("current")


class _T11ZsServerOperationMode_Type(Integer32):
    """Custom type t11ZsServerOperationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("enhanced", 2))
    )


_T11ZsServerOperationMode_Type.__name__ = "Integer32"
_T11ZsServerOperationMode_Object = MibTableColumn
t11ZsServerOperationMode = _T11ZsServerOperationMode_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 13),
    _T11ZsServerOperationMode_Type()
)
t11ZsServerOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsServerOperationMode.setStatus("current")


class _T11ZsServerChangeModeResult_Type(Integer32):
    """Custom type t11ZsServerChangeModeResult based on Integer32"""
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
        *(("failure", 2),
          ("inProgress", 3),
          ("none", 4),
          ("success", 1))
    )


_T11ZsServerChangeModeResult_Type.__name__ = "Integer32"
_T11ZsServerChangeModeResult_Object = MibTableColumn
t11ZsServerChangeModeResult = _T11ZsServerChangeModeResult_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 14),
    _T11ZsServerChangeModeResult_Type()
)
t11ZsServerChangeModeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsServerChangeModeResult.setStatus("current")


class _T11ZsServerDefaultZoneSetting_Type(Integer32):
    """Custom type t11ZsServerDefaultZoneSetting based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_T11ZsServerDefaultZoneSetting_Type.__name__ = "Integer32"
_T11ZsServerDefaultZoneSetting_Object = MibTableColumn
t11ZsServerDefaultZoneSetting = _T11ZsServerDefaultZoneSetting_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 15),
    _T11ZsServerDefaultZoneSetting_Type()
)
t11ZsServerDefaultZoneSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsServerDefaultZoneSetting.setStatus("current")


class _T11ZsServerMergeControlSetting_Type(Integer32):
    """Custom type t11ZsServerMergeControlSetting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("restrict", 2))
    )


_T11ZsServerMergeControlSetting_Type.__name__ = "Integer32"
_T11ZsServerMergeControlSetting_Object = MibTableColumn
t11ZsServerMergeControlSetting = _T11ZsServerMergeControlSetting_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 16),
    _T11ZsServerMergeControlSetting_Type()
)
t11ZsServerMergeControlSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsServerMergeControlSetting.setStatus("current")
_T11ZsServerDefZoneBroadcast_Type = TruthValue
_T11ZsServerDefZoneBroadcast_Object = MibTableColumn
t11ZsServerDefZoneBroadcast = _T11ZsServerDefZoneBroadcast_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 1, 1, 17),
    _T11ZsServerDefZoneBroadcast_Type()
)
t11ZsServerDefZoneBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsServerDefZoneBroadcast.setStatus("current")
_T11ZsSetTable_Object = MibTable
t11ZsSetTable = _T11ZsSetTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 2)
)
if mibBuilder.loadTexts:
    t11ZsSetTable.setStatus("current")
_T11ZsSetEntry_Object = MibTableRow
t11ZsSetEntry = _T11ZsSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 2, 1)
)
t11ZsSetEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsSetIndex"),
)
if mibBuilder.loadTexts:
    t11ZsSetEntry.setStatus("current")


class _T11ZsSetIndex_Type(Unsigned32):
    """Custom type t11ZsSetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11ZsSetIndex_Type.__name__ = "Unsigned32"
_T11ZsSetIndex_Object = MibTableColumn
t11ZsSetIndex = _T11ZsSetIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 2, 1, 1),
    _T11ZsSetIndex_Type()
)
t11ZsSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsSetIndex.setStatus("current")
_T11ZsSetName_Type = T11ZoningName
_T11ZsSetName_Object = MibTableColumn
t11ZsSetName = _T11ZsSetName_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 2, 1, 2),
    _T11ZsSetName_Type()
)
t11ZsSetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsSetName.setStatus("current")
_T11ZsSetRowStatus_Type = RowStatus
_T11ZsSetRowStatus_Object = MibTableColumn
t11ZsSetRowStatus = _T11ZsSetRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 2, 1, 3),
    _T11ZsSetRowStatus_Type()
)
t11ZsSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsSetRowStatus.setStatus("current")
_T11ZsZoneTable_Object = MibTable
t11ZsZoneTable = _T11ZsZoneTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 3)
)
if mibBuilder.loadTexts:
    t11ZsZoneTable.setStatus("current")
_T11ZsZoneEntry_Object = MibTableRow
t11ZsZoneEntry = _T11ZsZoneEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 3, 1)
)
t11ZsZoneEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsZoneIndex"),
)
if mibBuilder.loadTexts:
    t11ZsZoneEntry.setStatus("current")


class _T11ZsZoneIndex_Type(Unsigned32):
    """Custom type t11ZsZoneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11ZsZoneIndex_Type.__name__ = "Unsigned32"
_T11ZsZoneIndex_Object = MibTableColumn
t11ZsZoneIndex = _T11ZsZoneIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 3, 1, 1),
    _T11ZsZoneIndex_Type()
)
t11ZsZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsZoneIndex.setStatus("current")
_T11ZsZoneName_Type = T11ZoningName
_T11ZsZoneName_Object = MibTableColumn
t11ZsZoneName = _T11ZsZoneName_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 3, 1, 2),
    _T11ZsZoneName_Type()
)
t11ZsZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsZoneName.setStatus("current")


class _T11ZsZoneAttribBlock_Type(Unsigned32):
    """Custom type t11ZsZoneAttribBlock based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11ZsZoneAttribBlock_Type.__name__ = "Unsigned32"
_T11ZsZoneAttribBlock_Object = MibTableColumn
t11ZsZoneAttribBlock = _T11ZsZoneAttribBlock_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 3, 1, 3),
    _T11ZsZoneAttribBlock_Type()
)
t11ZsZoneAttribBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsZoneAttribBlock.setStatus("current")
_T11ZsZoneRowStatus_Type = RowStatus
_T11ZsZoneRowStatus_Object = MibTableColumn
t11ZsZoneRowStatus = _T11ZsZoneRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 3, 1, 4),
    _T11ZsZoneRowStatus_Type()
)
t11ZsZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsZoneRowStatus.setStatus("current")
_T11ZsSetZoneTable_Object = MibTable
t11ZsSetZoneTable = _T11ZsSetZoneTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 4)
)
if mibBuilder.loadTexts:
    t11ZsSetZoneTable.setStatus("current")
_T11ZsSetZoneEntry_Object = MibTableRow
t11ZsSetZoneEntry = _T11ZsSetZoneEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 4, 1)
)
t11ZsSetZoneEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsSetIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsZoneIndex"),
)
if mibBuilder.loadTexts:
    t11ZsSetZoneEntry.setStatus("current")
_T11ZsSetZoneRowStatus_Type = RowStatus
_T11ZsSetZoneRowStatus_Object = MibTableColumn
t11ZsSetZoneRowStatus = _T11ZsSetZoneRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 4, 1, 1),
    _T11ZsSetZoneRowStatus_Type()
)
t11ZsSetZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsSetZoneRowStatus.setStatus("current")
_T11ZsAliasTable_Object = MibTable
t11ZsAliasTable = _T11ZsAliasTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 5)
)
if mibBuilder.loadTexts:
    t11ZsAliasTable.setStatus("current")
_T11ZsAliasEntry_Object = MibTableRow
t11ZsAliasEntry = _T11ZsAliasEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 5, 1)
)
t11ZsAliasEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsAliasIndex"),
)
if mibBuilder.loadTexts:
    t11ZsAliasEntry.setStatus("current")


class _T11ZsAliasIndex_Type(Unsigned32):
    """Custom type t11ZsAliasIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11ZsAliasIndex_Type.__name__ = "Unsigned32"
_T11ZsAliasIndex_Object = MibTableColumn
t11ZsAliasIndex = _T11ZsAliasIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 5, 1, 1),
    _T11ZsAliasIndex_Type()
)
t11ZsAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsAliasIndex.setStatus("current")
_T11ZsAliasName_Type = T11ZoningName
_T11ZsAliasName_Object = MibTableColumn
t11ZsAliasName = _T11ZsAliasName_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 5, 1, 2),
    _T11ZsAliasName_Type()
)
t11ZsAliasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsAliasName.setStatus("current")
_T11ZsAliasRowStatus_Type = RowStatus
_T11ZsAliasRowStatus_Object = MibTableColumn
t11ZsAliasRowStatus = _T11ZsAliasRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 5, 1, 3),
    _T11ZsAliasRowStatus_Type()
)
t11ZsAliasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsAliasRowStatus.setStatus("current")
_T11ZsZoneMemberTable_Object = MibTable
t11ZsZoneMemberTable = _T11ZsZoneMemberTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 6)
)
if mibBuilder.loadTexts:
    t11ZsZoneMemberTable.setStatus("current")
_T11ZsZoneMemberEntry_Object = MibTableRow
t11ZsZoneMemberEntry = _T11ZsZoneMemberEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 6, 1)
)
t11ZsZoneMemberEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsZoneMemberParentType"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsZoneMemberParentIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    t11ZsZoneMemberEntry.setStatus("current")


class _T11ZsZoneMemberParentType_Type(Integer32):
    """Custom type t11ZsZoneMemberParentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alias", 2),
          ("zone", 1))
    )


_T11ZsZoneMemberParentType_Type.__name__ = "Integer32"
_T11ZsZoneMemberParentType_Object = MibTableColumn
t11ZsZoneMemberParentType = _T11ZsZoneMemberParentType_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 6, 1, 1),
    _T11ZsZoneMemberParentType_Type()
)
t11ZsZoneMemberParentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsZoneMemberParentType.setStatus("current")


class _T11ZsZoneMemberParentIndex_Type(Unsigned32):
    """Custom type t11ZsZoneMemberParentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11ZsZoneMemberParentIndex_Type.__name__ = "Unsigned32"
_T11ZsZoneMemberParentIndex_Object = MibTableColumn
t11ZsZoneMemberParentIndex = _T11ZsZoneMemberParentIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 6, 1, 2),
    _T11ZsZoneMemberParentIndex_Type()
)
t11ZsZoneMemberParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsZoneMemberParentIndex.setStatus("current")


class _T11ZsZoneMemberIndex_Type(Unsigned32):
    """Custom type t11ZsZoneMemberIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11ZsZoneMemberIndex_Type.__name__ = "Unsigned32"
_T11ZsZoneMemberIndex_Object = MibTableColumn
t11ZsZoneMemberIndex = _T11ZsZoneMemberIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 6, 1, 3),
    _T11ZsZoneMemberIndex_Type()
)
t11ZsZoneMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsZoneMemberIndex.setStatus("current")
_T11ZsZoneMemberFormat_Type = T11ZsZoneMemberType
_T11ZsZoneMemberFormat_Object = MibTableColumn
t11ZsZoneMemberFormat = _T11ZsZoneMemberFormat_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 6, 1, 4),
    _T11ZsZoneMemberFormat_Type()
)
t11ZsZoneMemberFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsZoneMemberFormat.setStatus("current")


class _T11ZsZoneMemberID_Type(OctetString):
    """Custom type t11ZsZoneMemberID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_T11ZsZoneMemberID_Type.__name__ = "OctetString"
_T11ZsZoneMemberID_Object = MibTableColumn
t11ZsZoneMemberID = _T11ZsZoneMemberID_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 6, 1, 5),
    _T11ZsZoneMemberID_Type()
)
t11ZsZoneMemberID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsZoneMemberID.setStatus("current")
_T11ZsZoneMemberRowStatus_Type = RowStatus
_T11ZsZoneMemberRowStatus_Object = MibTableColumn
t11ZsZoneMemberRowStatus = _T11ZsZoneMemberRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 6, 1, 6),
    _T11ZsZoneMemberRowStatus_Type()
)
t11ZsZoneMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsZoneMemberRowStatus.setStatus("current")
_T11ZsAttribBlockTable_Object = MibTable
t11ZsAttribBlockTable = _T11ZsAttribBlockTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 7)
)
if mibBuilder.loadTexts:
    t11ZsAttribBlockTable.setStatus("current")
_T11ZsAttribBlockEntry_Object = MibTableRow
t11ZsAttribBlockEntry = _T11ZsAttribBlockEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 7, 1)
)
t11ZsAttribBlockEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsAttribBlockIndex"),
)
if mibBuilder.loadTexts:
    t11ZsAttribBlockEntry.setStatus("current")


class _T11ZsAttribBlockIndex_Type(Unsigned32):
    """Custom type t11ZsAttribBlockIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11ZsAttribBlockIndex_Type.__name__ = "Unsigned32"
_T11ZsAttribBlockIndex_Object = MibTableColumn
t11ZsAttribBlockIndex = _T11ZsAttribBlockIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 7, 1, 1),
    _T11ZsAttribBlockIndex_Type()
)
t11ZsAttribBlockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsAttribBlockIndex.setStatus("current")
_T11ZsAttribBlockName_Type = T11ZoningName
_T11ZsAttribBlockName_Object = MibTableColumn
t11ZsAttribBlockName = _T11ZsAttribBlockName_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 7, 1, 2),
    _T11ZsAttribBlockName_Type()
)
t11ZsAttribBlockName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsAttribBlockName.setStatus("current")
_T11ZsAttribBlockRowStatus_Type = RowStatus
_T11ZsAttribBlockRowStatus_Object = MibTableColumn
t11ZsAttribBlockRowStatus = _T11ZsAttribBlockRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 7, 1, 3),
    _T11ZsAttribBlockRowStatus_Type()
)
t11ZsAttribBlockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsAttribBlockRowStatus.setStatus("current")
_T11ZsAttribTable_Object = MibTable
t11ZsAttribTable = _T11ZsAttribTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 8)
)
if mibBuilder.loadTexts:
    t11ZsAttribTable.setStatus("current")
_T11ZsAttribEntry_Object = MibTableRow
t11ZsAttribEntry = _T11ZsAttribEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 8, 1)
)
t11ZsAttribEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsAttribBlockIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsAttribIndex"),
)
if mibBuilder.loadTexts:
    t11ZsAttribEntry.setStatus("current")


class _T11ZsAttribIndex_Type(Unsigned32):
    """Custom type t11ZsAttribIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11ZsAttribIndex_Type.__name__ = "Unsigned32"
_T11ZsAttribIndex_Object = MibTableColumn
t11ZsAttribIndex = _T11ZsAttribIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 8, 1, 1),
    _T11ZsAttribIndex_Type()
)
t11ZsAttribIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsAttribIndex.setStatus("current")


class _T11ZsAttribType_Type(Unsigned32):
    """Custom type t11ZsAttribType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T11ZsAttribType_Type.__name__ = "Unsigned32"
_T11ZsAttribType_Object = MibTableColumn
t11ZsAttribType = _T11ZsAttribType_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 8, 1, 2),
    _T11ZsAttribType_Type()
)
t11ZsAttribType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsAttribType.setStatus("current")


class _T11ZsAttribValue_Type(OctetString):
    """Custom type t11ZsAttribValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 252),
    )


_T11ZsAttribValue_Type.__name__ = "OctetString"
_T11ZsAttribValue_Object = MibTableColumn
t11ZsAttribValue = _T11ZsAttribValue_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 8, 1, 3),
    _T11ZsAttribValue_Type()
)
t11ZsAttribValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsAttribValue.setStatus("current")
_T11ZsAttribRowStatus_Type = RowStatus
_T11ZsAttribRowStatus_Object = MibTableColumn
t11ZsAttribRowStatus = _T11ZsAttribRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 8, 1, 4),
    _T11ZsAttribRowStatus_Type()
)
t11ZsAttribRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11ZsAttribRowStatus.setStatus("current")
_T11ZsActivateTable_Object = MibTable
t11ZsActivateTable = _T11ZsActivateTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 9)
)
if mibBuilder.loadTexts:
    t11ZsActivateTable.setStatus("current")
_T11ZsActivateEntry_Object = MibTableRow
t11ZsActivateEntry = _T11ZsActivateEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 9, 1)
)
t11ZsActivateEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
)
if mibBuilder.loadTexts:
    t11ZsActivateEntry.setStatus("current")


class _T11ZsActivateRequest_Type(Unsigned32):
    """Custom type t11ZsActivateRequest based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11ZsActivateRequest_Type.__name__ = "Unsigned32"
_T11ZsActivateRequest_Object = MibTableColumn
t11ZsActivateRequest = _T11ZsActivateRequest_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 9, 1, 1),
    _T11ZsActivateRequest_Type()
)
t11ZsActivateRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsActivateRequest.setStatus("current")


class _T11ZsActivateDeactivate_Type(Integer32):
    """Custom type t11ZsActivateDeactivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deactivate", 1),
          ("noop", 2))
    )


_T11ZsActivateDeactivate_Type.__name__ = "Integer32"
_T11ZsActivateDeactivate_Object = MibTableColumn
t11ZsActivateDeactivate = _T11ZsActivateDeactivate_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 9, 1, 2),
    _T11ZsActivateDeactivate_Type()
)
t11ZsActivateDeactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsActivateDeactivate.setStatus("current")


class _T11ZsActivateResult_Type(Integer32):
    """Custom type t11ZsActivateResult based on Integer32"""
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
        *(("activateFailure", 2),
          ("activateSuccess", 1),
          ("deactivateFailure", 4),
          ("deactivateSuccess", 3),
          ("inProgress", 5),
          ("none", 6))
    )


_T11ZsActivateResult_Type.__name__ = "Integer32"
_T11ZsActivateResult_Object = MibTableColumn
t11ZsActivateResult = _T11ZsActivateResult_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 9, 1, 3),
    _T11ZsActivateResult_Type()
)
t11ZsActivateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActivateResult.setStatus("current")


class _T11ZsActivateFailCause_Type(SnmpAdminString):
    """Custom type t11ZsActivateFailCause based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_T11ZsActivateFailCause_Type.__name__ = "SnmpAdminString"
_T11ZsActivateFailCause_Object = MibTableColumn
t11ZsActivateFailCause = _T11ZsActivateFailCause_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 9, 1, 4),
    _T11ZsActivateFailCause_Type()
)
t11ZsActivateFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActivateFailCause.setStatus("current")
_T11ZsActivateFailDomainId_Type = FcDomainIdOrZero
_T11ZsActivateFailDomainId_Object = MibTableColumn
t11ZsActivateFailDomainId = _T11ZsActivateFailDomainId_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 9, 1, 5),
    _T11ZsActivateFailDomainId_Type()
)
t11ZsActivateFailDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActivateFailDomainId.setStatus("current")
_T11ZsActiveTable_Object = MibTable
t11ZsActiveTable = _T11ZsActiveTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 10)
)
if mibBuilder.loadTexts:
    t11ZsActiveTable.setStatus("current")
_T11ZsActiveEntry_Object = MibTableRow
t11ZsActiveEntry = _T11ZsActiveEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 10, 1)
)
t11ZsActiveEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
)
if mibBuilder.loadTexts:
    t11ZsActiveEntry.setStatus("current")
_T11ZsActiveZoneSetName_Type = T11ZoningName
_T11ZsActiveZoneSetName_Object = MibTableColumn
t11ZsActiveZoneSetName = _T11ZsActiveZoneSetName_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 10, 1, 1),
    _T11ZsActiveZoneSetName_Type()
)
t11ZsActiveZoneSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActiveZoneSetName.setStatus("current")
_T11ZsActiveActivateTime_Type = TimeStamp
_T11ZsActiveActivateTime_Object = MibTableColumn
t11ZsActiveActivateTime = _T11ZsActiveActivateTime_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 10, 1, 2),
    _T11ZsActiveActivateTime_Type()
)
t11ZsActiveActivateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActiveActivateTime.setStatus("current")
_T11ZsActiveZoneTable_Object = MibTable
t11ZsActiveZoneTable = _T11ZsActiveZoneTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 11)
)
if mibBuilder.loadTexts:
    t11ZsActiveZoneTable.setStatus("current")
_T11ZsActiveZoneEntry_Object = MibTableRow
t11ZsActiveZoneEntry = _T11ZsActiveZoneEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 11, 1)
)
t11ZsActiveZoneEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneIndex"),
)
if mibBuilder.loadTexts:
    t11ZsActiveZoneEntry.setStatus("current")


class _T11ZsActiveZoneIndex_Type(Unsigned32):
    """Custom type t11ZsActiveZoneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11ZsActiveZoneIndex_Type.__name__ = "Unsigned32"
_T11ZsActiveZoneIndex_Object = MibTableColumn
t11ZsActiveZoneIndex = _T11ZsActiveZoneIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 11, 1, 1),
    _T11ZsActiveZoneIndex_Type()
)
t11ZsActiveZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsActiveZoneIndex.setStatus("current")
_T11ZsActiveZoneName_Type = T11ZoningName
_T11ZsActiveZoneName_Object = MibTableColumn
t11ZsActiveZoneName = _T11ZsActiveZoneName_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 11, 1, 2),
    _T11ZsActiveZoneName_Type()
)
t11ZsActiveZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActiveZoneName.setStatus("current")
_T11ZsActiveZoneBroadcastZoning_Type = TruthValue
_T11ZsActiveZoneBroadcastZoning_Object = MibTableColumn
t11ZsActiveZoneBroadcastZoning = _T11ZsActiveZoneBroadcastZoning_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 11, 1, 3),
    _T11ZsActiveZoneBroadcastZoning_Type()
)
t11ZsActiveZoneBroadcastZoning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActiveZoneBroadcastZoning.setStatus("current")
_T11ZsActiveZoneHardZoning_Type = TruthValue
_T11ZsActiveZoneHardZoning_Object = MibTableColumn
t11ZsActiveZoneHardZoning = _T11ZsActiveZoneHardZoning_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 11, 1, 4),
    _T11ZsActiveZoneHardZoning_Type()
)
t11ZsActiveZoneHardZoning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActiveZoneHardZoning.setStatus("current")
_T11ZsActiveZoneMemberTable_Object = MibTable
t11ZsActiveZoneMemberTable = _T11ZsActiveZoneMemberTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 12)
)
if mibBuilder.loadTexts:
    t11ZsActiveZoneMemberTable.setStatus("current")
_T11ZsActiveZoneMemberEntry_Object = MibTableRow
t11ZsActiveZoneMemberEntry = _T11ZsActiveZoneMemberEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 12, 1)
)
t11ZsActiveZoneMemberEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    t11ZsActiveZoneMemberEntry.setStatus("current")


class _T11ZsActiveZoneMemberIndex_Type(Unsigned32):
    """Custom type t11ZsActiveZoneMemberIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11ZsActiveZoneMemberIndex_Type.__name__ = "Unsigned32"
_T11ZsActiveZoneMemberIndex_Object = MibTableColumn
t11ZsActiveZoneMemberIndex = _T11ZsActiveZoneMemberIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 12, 1, 1),
    _T11ZsActiveZoneMemberIndex_Type()
)
t11ZsActiveZoneMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsActiveZoneMemberIndex.setStatus("current")
_T11ZsActiveZoneMemberFormat_Type = T11ZsZoneMemberType
_T11ZsActiveZoneMemberFormat_Object = MibTableColumn
t11ZsActiveZoneMemberFormat = _T11ZsActiveZoneMemberFormat_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 12, 1, 2),
    _T11ZsActiveZoneMemberFormat_Type()
)
t11ZsActiveZoneMemberFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActiveZoneMemberFormat.setStatus("current")


class _T11ZsActiveZoneMemberID_Type(OctetString):
    """Custom type t11ZsActiveZoneMemberID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_T11ZsActiveZoneMemberID_Type.__name__ = "OctetString"
_T11ZsActiveZoneMemberID_Object = MibTableColumn
t11ZsActiveZoneMemberID = _T11ZsActiveZoneMemberID_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 12, 1, 3),
    _T11ZsActiveZoneMemberID_Type()
)
t11ZsActiveZoneMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActiveZoneMemberID.setStatus("current")
_T11ZsActiveAttribTable_Object = MibTable
t11ZsActiveAttribTable = _T11ZsActiveAttribTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 13)
)
if mibBuilder.loadTexts:
    t11ZsActiveAttribTable.setStatus("current")
_T11ZsActiveAttribEntry_Object = MibTableRow
t11ZsActiveAttribEntry = _T11ZsActiveAttribEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 13, 1)
)
t11ZsActiveAttribEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveAttribIndex"),
)
if mibBuilder.loadTexts:
    t11ZsActiveAttribEntry.setStatus("current")


class _T11ZsActiveAttribIndex_Type(Unsigned32):
    """Custom type t11ZsActiveAttribIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11ZsActiveAttribIndex_Type.__name__ = "Unsigned32"
_T11ZsActiveAttribIndex_Object = MibTableColumn
t11ZsActiveAttribIndex = _T11ZsActiveAttribIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 13, 1, 1),
    _T11ZsActiveAttribIndex_Type()
)
t11ZsActiveAttribIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11ZsActiveAttribIndex.setStatus("current")


class _T11ZsActiveAttribType_Type(Unsigned32):
    """Custom type t11ZsActiveAttribType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T11ZsActiveAttribType_Type.__name__ = "Unsigned32"
_T11ZsActiveAttribType_Object = MibTableColumn
t11ZsActiveAttribType = _T11ZsActiveAttribType_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 13, 1, 2),
    _T11ZsActiveAttribType_Type()
)
t11ZsActiveAttribType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActiveAttribType.setStatus("current")


class _T11ZsActiveAttribValue_Type(OctetString):
    """Custom type t11ZsActiveAttribValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )


_T11ZsActiveAttribValue_Type.__name__ = "OctetString"
_T11ZsActiveAttribValue_Object = MibTableColumn
t11ZsActiveAttribValue = _T11ZsActiveAttribValue_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 13, 1, 3),
    _T11ZsActiveAttribValue_Type()
)
t11ZsActiveAttribValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsActiveAttribValue.setStatus("current")
_T11ZsNotifyControlTable_Object = MibTable
t11ZsNotifyControlTable = _T11ZsNotifyControlTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14)
)
if mibBuilder.loadTexts:
    t11ZsNotifyControlTable.setStatus("current")
_T11ZsNotifyControlEntry_Object = MibTableRow
t11ZsNotifyControlEntry = _T11ZsNotifyControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1)
)
t11ZsNotifyControlEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
)
if mibBuilder.loadTexts:
    t11ZsNotifyControlEntry.setStatus("current")
_T11ZsNotifyRequestRejectEnable_Type = TruthValue
_T11ZsNotifyRequestRejectEnable_Object = MibTableColumn
t11ZsNotifyRequestRejectEnable = _T11ZsNotifyRequestRejectEnable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1, 1),
    _T11ZsNotifyRequestRejectEnable_Type()
)
t11ZsNotifyRequestRejectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsNotifyRequestRejectEnable.setStatus("current")
_T11ZsNotifyMergeFailureEnable_Type = TruthValue
_T11ZsNotifyMergeFailureEnable_Object = MibTableColumn
t11ZsNotifyMergeFailureEnable = _T11ZsNotifyMergeFailureEnable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1, 2),
    _T11ZsNotifyMergeFailureEnable_Type()
)
t11ZsNotifyMergeFailureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsNotifyMergeFailureEnable.setStatus("current")
_T11ZsNotifyMergeSuccessEnable_Type = TruthValue
_T11ZsNotifyMergeSuccessEnable_Object = MibTableColumn
t11ZsNotifyMergeSuccessEnable = _T11ZsNotifyMergeSuccessEnable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1, 3),
    _T11ZsNotifyMergeSuccessEnable_Type()
)
t11ZsNotifyMergeSuccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsNotifyMergeSuccessEnable.setStatus("current")
_T11ZsNotifyDefZoneChangeEnable_Type = TruthValue
_T11ZsNotifyDefZoneChangeEnable_Object = MibTableColumn
t11ZsNotifyDefZoneChangeEnable = _T11ZsNotifyDefZoneChangeEnable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1, 4),
    _T11ZsNotifyDefZoneChangeEnable_Type()
)
t11ZsNotifyDefZoneChangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsNotifyDefZoneChangeEnable.setStatus("current")
_T11ZsNotifyActivateEnable_Type = TruthValue
_T11ZsNotifyActivateEnable_Object = MibTableColumn
t11ZsNotifyActivateEnable = _T11ZsNotifyActivateEnable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1, 5),
    _T11ZsNotifyActivateEnable_Type()
)
t11ZsNotifyActivateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11ZsNotifyActivateEnable.setStatus("current")


class _T11ZsRejectCtCommandString_Type(OctetString):
    """Custom type t11ZsRejectCtCommandString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_T11ZsRejectCtCommandString_Type.__name__ = "OctetString"
_T11ZsRejectCtCommandString_Object = MibTableColumn
t11ZsRejectCtCommandString = _T11ZsRejectCtCommandString_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1, 6),
    _T11ZsRejectCtCommandString_Type()
)
t11ZsRejectCtCommandString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsRejectCtCommandString.setStatus("current")
_T11ZsRejectRequestSource_Type = FcNameIdOrZero
_T11ZsRejectRequestSource_Object = MibTableColumn
t11ZsRejectRequestSource = _T11ZsRejectRequestSource_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1, 7),
    _T11ZsRejectRequestSource_Type()
)
t11ZsRejectRequestSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsRejectRequestSource.setStatus("current")
_T11ZsRejectReasonCode_Type = T11NsGs4RejectReasonCode
_T11ZsRejectReasonCode_Object = MibTableColumn
t11ZsRejectReasonCode = _T11ZsRejectReasonCode_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1, 8),
    _T11ZsRejectReasonCode_Type()
)
t11ZsRejectReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsRejectReasonCode.setStatus("current")
_T11ZsRejectReasonCodeExp_Type = T11ZsRejectReasonExplanation
_T11ZsRejectReasonCodeExp_Object = MibTableColumn
t11ZsRejectReasonCodeExp = _T11ZsRejectReasonCodeExp_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1, 9),
    _T11ZsRejectReasonCodeExp_Type()
)
t11ZsRejectReasonCodeExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsRejectReasonCodeExp.setStatus("current")


class _T11ZsRejectReasonVendorCode_Type(OctetString):
    """Custom type t11ZsRejectReasonVendorCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T11ZsRejectReasonVendorCode_Type.__name__ = "OctetString"
_T11ZsRejectReasonVendorCode_Object = MibTableColumn
t11ZsRejectReasonVendorCode = _T11ZsRejectReasonVendorCode_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 14, 1, 10),
    _T11ZsRejectReasonVendorCode_Type()
)
t11ZsRejectReasonVendorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsRejectReasonVendorCode.setStatus("current")


class _T11ZsFabricIndex_Type(Unsigned32):
    """Custom type t11ZsFabricIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_T11ZsFabricIndex_Type.__name__ = "Unsigned32"
_T11ZsFabricIndex_Object = MibScalar
t11ZsFabricIndex = _T11ZsFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 1, 15),
    _T11ZsFabricIndex_Type()
)
t11ZsFabricIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    t11ZsFabricIndex.setStatus("current")
_T11ZsStatistics_ObjectIdentity = ObjectIdentity
t11ZsStatistics = _T11ZsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 160, 1, 2)
)
_T11ZsStatsTable_Object = MibTable
t11ZsStatsTable = _T11ZsStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11ZsStatsTable.setStatus("current")
_T11ZsStatsEntry_Object = MibTableRow
t11ZsStatsEntry = _T11ZsStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1)
)
t11ZsStatsEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsServerFabricIndex"),
)
if mibBuilder.loadTexts:
    t11ZsStatsEntry.setStatus("current")
_T11ZsOutMergeRequests_Type = Counter32
_T11ZsOutMergeRequests_Object = MibTableColumn
t11ZsOutMergeRequests = _T11ZsOutMergeRequests_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1, 1),
    _T11ZsOutMergeRequests_Type()
)
t11ZsOutMergeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsOutMergeRequests.setStatus("current")
_T11ZsInMergeAccepts_Type = Counter32
_T11ZsInMergeAccepts_Object = MibTableColumn
t11ZsInMergeAccepts = _T11ZsInMergeAccepts_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1, 2),
    _T11ZsInMergeAccepts_Type()
)
t11ZsInMergeAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsInMergeAccepts.setStatus("current")
_T11ZsInMergeRequests_Type = Counter32
_T11ZsInMergeRequests_Object = MibTableColumn
t11ZsInMergeRequests = _T11ZsInMergeRequests_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1, 3),
    _T11ZsInMergeRequests_Type()
)
t11ZsInMergeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsInMergeRequests.setStatus("current")
_T11ZsOutMergeAccepts_Type = Counter32
_T11ZsOutMergeAccepts_Object = MibTableColumn
t11ZsOutMergeAccepts = _T11ZsOutMergeAccepts_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1, 4),
    _T11ZsOutMergeAccepts_Type()
)
t11ZsOutMergeAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsOutMergeAccepts.setStatus("current")
_T11ZsOutChangeRequests_Type = Counter32
_T11ZsOutChangeRequests_Object = MibTableColumn
t11ZsOutChangeRequests = _T11ZsOutChangeRequests_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1, 5),
    _T11ZsOutChangeRequests_Type()
)
t11ZsOutChangeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsOutChangeRequests.setStatus("current")
_T11ZsInChangeAccepts_Type = Counter32
_T11ZsInChangeAccepts_Object = MibTableColumn
t11ZsInChangeAccepts = _T11ZsInChangeAccepts_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1, 6),
    _T11ZsInChangeAccepts_Type()
)
t11ZsInChangeAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsInChangeAccepts.setStatus("current")
_T11ZsInChangeRequests_Type = Counter32
_T11ZsInChangeRequests_Object = MibTableColumn
t11ZsInChangeRequests = _T11ZsInChangeRequests_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1, 7),
    _T11ZsInChangeRequests_Type()
)
t11ZsInChangeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsInChangeRequests.setStatus("current")
_T11ZsOutChangeAccepts_Type = Counter32
_T11ZsOutChangeAccepts_Object = MibTableColumn
t11ZsOutChangeAccepts = _T11ZsOutChangeAccepts_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1, 8),
    _T11ZsOutChangeAccepts_Type()
)
t11ZsOutChangeAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsOutChangeAccepts.setStatus("current")
_T11ZsInZsRequests_Type = Counter32
_T11ZsInZsRequests_Object = MibTableColumn
t11ZsInZsRequests = _T11ZsInZsRequests_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1, 9),
    _T11ZsInZsRequests_Type()
)
t11ZsInZsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsInZsRequests.setStatus("current")
_T11ZsOutZsRejects_Type = Counter32
_T11ZsOutZsRejects_Object = MibTableColumn
t11ZsOutZsRejects = _T11ZsOutZsRejects_Object(
    (1, 3, 6, 1, 2, 1, 160, 1, 2, 1, 1, 10),
    _T11ZsOutZsRejects_Type()
)
t11ZsOutZsRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11ZsOutZsRejects.setStatus("current")
_T11ZsMIBConformance_ObjectIdentity = ObjectIdentity
t11ZsMIBConformance = _T11ZsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 160, 2)
)
_T11ZsMIBCompliances_ObjectIdentity = ObjectIdentity
t11ZsMIBCompliances = _T11ZsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 160, 2, 1)
)
_T11ZsMIBGroups_ObjectIdentity = ObjectIdentity
t11ZsMIBGroups = _T11ZsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 160, 2, 2)
)

# Managed Objects groups

t11ZsBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 160, 2, 2, 1)
)
t11ZsBasicGroup.setObjects(
      *(("T11-FC-ZONE-SERVER-MIB", "t11ZsServerCapabilityObject"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerDatabaseStorageType"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerDistribute"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerResult"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerReasonCode"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerReasonCodeExp"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerReasonVendorCode"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerLastChange"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerHardZoning"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerReadFromDatabase"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerOperationMode"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsSetName"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsSetRowStatus"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsZoneName"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsZoneAttribBlock"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsZoneRowStatus"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsSetZoneRowStatus"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsZoneMemberFormat"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsZoneMemberID"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsZoneMemberRowStatus"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneSetName"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActiveActivateTime"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneName"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneMemberFormat"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneMemberID"))
)
if mibBuilder.loadTexts:
    t11ZsBasicGroup.setStatus("current")

t11ZsEnhancedModeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 160, 2, 2, 2)
)
t11ZsEnhancedModeGroup.setObjects(
      *(("T11-FC-ZONE-SERVER-MIB", "t11ZsServerCommit"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerChangeModeResult"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerDefaultZoneSetting"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerMergeControlSetting"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerDefZoneBroadcast"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsAliasName"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsAliasRowStatus"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsAttribBlockName"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsAttribBlockRowStatus"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsAttribType"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsAttribValue"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsAttribRowStatus"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneBroadcastZoning"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneHardZoning"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActiveAttribType"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActiveAttribValue"))
)
if mibBuilder.loadTexts:
    t11ZsEnhancedModeGroup.setStatus("current")

t11ZsStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 160, 2, 2, 3)
)
t11ZsStatisticsGroup.setObjects(
      *(("T11-FC-ZONE-SERVER-MIB", "t11ZsOutMergeRequests"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsInMergeAccepts"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsInMergeRequests"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsOutMergeAccepts"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsOutChangeRequests"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsInChangeAccepts"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsInChangeRequests"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsOutChangeAccepts"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsInZsRequests"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsOutZsRejects"))
)
if mibBuilder.loadTexts:
    t11ZsStatisticsGroup.setStatus("current")

t11ZsNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 160, 2, 2, 4)
)
t11ZsNotificationControlGroup.setObjects(
      *(("T11-FC-ZONE-SERVER-MIB", "t11ZsNotifyRequestRejectEnable"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsNotifyMergeFailureEnable"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsNotifyMergeSuccessEnable"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsNotifyDefZoneChangeEnable"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsNotifyActivateEnable"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsRejectCtCommandString"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsRejectRequestSource"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsRejectReasonCode"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsRejectReasonCodeExp"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsRejectReasonVendorCode"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsFabricIndex"))
)
if mibBuilder.loadTexts:
    t11ZsNotificationControlGroup.setStatus("current")

t11ZsActivateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 160, 2, 2, 5)
)
t11ZsActivateGroup.setObjects(
      *(("T11-FC-ZONE-SERVER-MIB", "t11ZsActivateRequest"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActivateDeactivate"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActivateResult"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActivateFailCause"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActivateFailDomainId"))
)
if mibBuilder.loadTexts:
    t11ZsActivateGroup.setStatus("current")


# Notification objects

t11ZsRequestRejectNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 160, 0, 1)
)
t11ZsRequestRejectNotify.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsRejectRequestSource"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsRejectCtCommandString"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsRejectReasonCode"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsRejectReasonCodeExp"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsRejectReasonVendorCode"))
)
if mibBuilder.loadTexts:
    t11ZsRequestRejectNotify.setStatus(
        "current"
    )

t11ZsMergeFailureNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 160, 0, 2)
)
t11ZsMergeFailureNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsFabricIndex"))
)
if mibBuilder.loadTexts:
    t11ZsMergeFailureNotify.setStatus(
        "current"
    )

t11ZsMergeSuccessNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 160, 0, 3)
)
t11ZsMergeSuccessNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsFabricIndex"))
)
if mibBuilder.loadTexts:
    t11ZsMergeSuccessNotify.setStatus(
        "current"
    )

t11ZsDefZoneChangeNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 160, 0, 4)
)
t11ZsDefZoneChangeNotify.setObjects(
    ("T11-FC-ZONE-SERVER-MIB", "t11ZsServerDefaultZoneSetting")
)
if mibBuilder.loadTexts:
    t11ZsDefZoneChangeNotify.setStatus(
        "current"
    )

t11ZsActivateNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 160, 0, 5)
)
t11ZsActivateNotify.setObjects(
      *(("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamLocalSwitchWwn"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActivateResult"))
)
if mibBuilder.loadTexts:
    t11ZsActivateNotify.setStatus(
        "current"
    )


# Notifications groups

t11ZsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 160, 2, 2, 6)
)
t11ZsNotificationGroup.setObjects(
      *(("T11-FC-ZONE-SERVER-MIB", "t11ZsRequestRejectNotify"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsMergeFailureNotify"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsMergeSuccessNotify"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsDefZoneChangeNotify"),
        ("T11-FC-ZONE-SERVER-MIB", "t11ZsActivateNotify"))
)
if mibBuilder.loadTexts:
    t11ZsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

t11ZsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 160, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11ZsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-ZONE-SERVER-MIB",
    **{"T11ZsZoneMemberType": T11ZsZoneMemberType,
       "T11ZsRejectReasonExplanation": T11ZsRejectReasonExplanation,
       "T11ZoningName": T11ZoningName,
       "t11ZoneServerMIB": t11ZoneServerMIB,
       "t11ZsMIBNotifications": t11ZsMIBNotifications,
       "t11ZsRequestRejectNotify": t11ZsRequestRejectNotify,
       "t11ZsMergeFailureNotify": t11ZsMergeFailureNotify,
       "t11ZsMergeSuccessNotify": t11ZsMergeSuccessNotify,
       "t11ZsDefZoneChangeNotify": t11ZsDefZoneChangeNotify,
       "t11ZsActivateNotify": t11ZsActivateNotify,
       "t11ZsMIBObjects": t11ZsMIBObjects,
       "t11ZsConfiguration": t11ZsConfiguration,
       "t11ZsServerTable": t11ZsServerTable,
       "t11ZsServerEntry": t11ZsServerEntry,
       "t11ZsServerFabricIndex": t11ZsServerFabricIndex,
       "t11ZsServerCapabilityObject": t11ZsServerCapabilityObject,
       "t11ZsServerDatabaseStorageType": t11ZsServerDatabaseStorageType,
       "t11ZsServerDistribute": t11ZsServerDistribute,
       "t11ZsServerCommit": t11ZsServerCommit,
       "t11ZsServerResult": t11ZsServerResult,
       "t11ZsServerReasonCode": t11ZsServerReasonCode,
       "t11ZsServerReasonCodeExp": t11ZsServerReasonCodeExp,
       "t11ZsServerReasonVendorCode": t11ZsServerReasonVendorCode,
       "t11ZsServerLastChange": t11ZsServerLastChange,
       "t11ZsServerHardZoning": t11ZsServerHardZoning,
       "t11ZsServerReadFromDatabase": t11ZsServerReadFromDatabase,
       "t11ZsServerOperationMode": t11ZsServerOperationMode,
       "t11ZsServerChangeModeResult": t11ZsServerChangeModeResult,
       "t11ZsServerDefaultZoneSetting": t11ZsServerDefaultZoneSetting,
       "t11ZsServerMergeControlSetting": t11ZsServerMergeControlSetting,
       "t11ZsServerDefZoneBroadcast": t11ZsServerDefZoneBroadcast,
       "t11ZsSetTable": t11ZsSetTable,
       "t11ZsSetEntry": t11ZsSetEntry,
       "t11ZsSetIndex": t11ZsSetIndex,
       "t11ZsSetName": t11ZsSetName,
       "t11ZsSetRowStatus": t11ZsSetRowStatus,
       "t11ZsZoneTable": t11ZsZoneTable,
       "t11ZsZoneEntry": t11ZsZoneEntry,
       "t11ZsZoneIndex": t11ZsZoneIndex,
       "t11ZsZoneName": t11ZsZoneName,
       "t11ZsZoneAttribBlock": t11ZsZoneAttribBlock,
       "t11ZsZoneRowStatus": t11ZsZoneRowStatus,
       "t11ZsSetZoneTable": t11ZsSetZoneTable,
       "t11ZsSetZoneEntry": t11ZsSetZoneEntry,
       "t11ZsSetZoneRowStatus": t11ZsSetZoneRowStatus,
       "t11ZsAliasTable": t11ZsAliasTable,
       "t11ZsAliasEntry": t11ZsAliasEntry,
       "t11ZsAliasIndex": t11ZsAliasIndex,
       "t11ZsAliasName": t11ZsAliasName,
       "t11ZsAliasRowStatus": t11ZsAliasRowStatus,
       "t11ZsZoneMemberTable": t11ZsZoneMemberTable,
       "t11ZsZoneMemberEntry": t11ZsZoneMemberEntry,
       "t11ZsZoneMemberParentType": t11ZsZoneMemberParentType,
       "t11ZsZoneMemberParentIndex": t11ZsZoneMemberParentIndex,
       "t11ZsZoneMemberIndex": t11ZsZoneMemberIndex,
       "t11ZsZoneMemberFormat": t11ZsZoneMemberFormat,
       "t11ZsZoneMemberID": t11ZsZoneMemberID,
       "t11ZsZoneMemberRowStatus": t11ZsZoneMemberRowStatus,
       "t11ZsAttribBlockTable": t11ZsAttribBlockTable,
       "t11ZsAttribBlockEntry": t11ZsAttribBlockEntry,
       "t11ZsAttribBlockIndex": t11ZsAttribBlockIndex,
       "t11ZsAttribBlockName": t11ZsAttribBlockName,
       "t11ZsAttribBlockRowStatus": t11ZsAttribBlockRowStatus,
       "t11ZsAttribTable": t11ZsAttribTable,
       "t11ZsAttribEntry": t11ZsAttribEntry,
       "t11ZsAttribIndex": t11ZsAttribIndex,
       "t11ZsAttribType": t11ZsAttribType,
       "t11ZsAttribValue": t11ZsAttribValue,
       "t11ZsAttribRowStatus": t11ZsAttribRowStatus,
       "t11ZsActivateTable": t11ZsActivateTable,
       "t11ZsActivateEntry": t11ZsActivateEntry,
       "t11ZsActivateRequest": t11ZsActivateRequest,
       "t11ZsActivateDeactivate": t11ZsActivateDeactivate,
       "t11ZsActivateResult": t11ZsActivateResult,
       "t11ZsActivateFailCause": t11ZsActivateFailCause,
       "t11ZsActivateFailDomainId": t11ZsActivateFailDomainId,
       "t11ZsActiveTable": t11ZsActiveTable,
       "t11ZsActiveEntry": t11ZsActiveEntry,
       "t11ZsActiveZoneSetName": t11ZsActiveZoneSetName,
       "t11ZsActiveActivateTime": t11ZsActiveActivateTime,
       "t11ZsActiveZoneTable": t11ZsActiveZoneTable,
       "t11ZsActiveZoneEntry": t11ZsActiveZoneEntry,
       "t11ZsActiveZoneIndex": t11ZsActiveZoneIndex,
       "t11ZsActiveZoneName": t11ZsActiveZoneName,
       "t11ZsActiveZoneBroadcastZoning": t11ZsActiveZoneBroadcastZoning,
       "t11ZsActiveZoneHardZoning": t11ZsActiveZoneHardZoning,
       "t11ZsActiveZoneMemberTable": t11ZsActiveZoneMemberTable,
       "t11ZsActiveZoneMemberEntry": t11ZsActiveZoneMemberEntry,
       "t11ZsActiveZoneMemberIndex": t11ZsActiveZoneMemberIndex,
       "t11ZsActiveZoneMemberFormat": t11ZsActiveZoneMemberFormat,
       "t11ZsActiveZoneMemberID": t11ZsActiveZoneMemberID,
       "t11ZsActiveAttribTable": t11ZsActiveAttribTable,
       "t11ZsActiveAttribEntry": t11ZsActiveAttribEntry,
       "t11ZsActiveAttribIndex": t11ZsActiveAttribIndex,
       "t11ZsActiveAttribType": t11ZsActiveAttribType,
       "t11ZsActiveAttribValue": t11ZsActiveAttribValue,
       "t11ZsNotifyControlTable": t11ZsNotifyControlTable,
       "t11ZsNotifyControlEntry": t11ZsNotifyControlEntry,
       "t11ZsNotifyRequestRejectEnable": t11ZsNotifyRequestRejectEnable,
       "t11ZsNotifyMergeFailureEnable": t11ZsNotifyMergeFailureEnable,
       "t11ZsNotifyMergeSuccessEnable": t11ZsNotifyMergeSuccessEnable,
       "t11ZsNotifyDefZoneChangeEnable": t11ZsNotifyDefZoneChangeEnable,
       "t11ZsNotifyActivateEnable": t11ZsNotifyActivateEnable,
       "t11ZsRejectCtCommandString": t11ZsRejectCtCommandString,
       "t11ZsRejectRequestSource": t11ZsRejectRequestSource,
       "t11ZsRejectReasonCode": t11ZsRejectReasonCode,
       "t11ZsRejectReasonCodeExp": t11ZsRejectReasonCodeExp,
       "t11ZsRejectReasonVendorCode": t11ZsRejectReasonVendorCode,
       "t11ZsFabricIndex": t11ZsFabricIndex,
       "t11ZsStatistics": t11ZsStatistics,
       "t11ZsStatsTable": t11ZsStatsTable,
       "t11ZsStatsEntry": t11ZsStatsEntry,
       "t11ZsOutMergeRequests": t11ZsOutMergeRequests,
       "t11ZsInMergeAccepts": t11ZsInMergeAccepts,
       "t11ZsInMergeRequests": t11ZsInMergeRequests,
       "t11ZsOutMergeAccepts": t11ZsOutMergeAccepts,
       "t11ZsOutChangeRequests": t11ZsOutChangeRequests,
       "t11ZsInChangeAccepts": t11ZsInChangeAccepts,
       "t11ZsInChangeRequests": t11ZsInChangeRequests,
       "t11ZsOutChangeAccepts": t11ZsOutChangeAccepts,
       "t11ZsInZsRequests": t11ZsInZsRequests,
       "t11ZsOutZsRejects": t11ZsOutZsRejects,
       "t11ZsMIBConformance": t11ZsMIBConformance,
       "t11ZsMIBCompliances": t11ZsMIBCompliances,
       "t11ZsMIBCompliance": t11ZsMIBCompliance,
       "t11ZsMIBGroups": t11ZsMIBGroups,
       "t11ZsBasicGroup": t11ZsBasicGroup,
       "t11ZsEnhancedModeGroup": t11ZsEnhancedModeGroup,
       "t11ZsStatisticsGroup": t11ZsStatisticsGroup,
       "t11ZsNotificationControlGroup": t11ZsNotificationControlGroup,
       "t11ZsActivateGroup": t11ZsActivateGroup,
       "t11ZsNotificationGroup": t11ZsNotificationGroup}
)
