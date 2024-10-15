# SNMP MIB module (CISCO-THREAT-MITIGATION-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-THREAT-MITIGATION-SERVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:42 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoThreatMitigationServiceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 603)
)
ciscoThreatMitigationServiceMIB.setRevisions(
        ("2007-01-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CTmsConsumerState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class CTmsConsumerRegistrationStatus(Integer32, TextualConvention):
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
        *(("notRegistered", 1),
          ("registered", 3),
          ("registrationFailed", 4),
          ("registrationRequestSent", 2))
    )



class CTmsThreatStatus(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("activationFailed", 6),
          ("active", 2),
          ("created", 4),
          ("deleted", 8),
          ("inactivationFailed", 7),
          ("inactive", 3),
          ("pending", 5),
          ("unknown", 1))
    )



class CTmsActionType(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aclDrop", 2),
          ("fpmDrop", 3),
          ("ignore", 1),
          ("localException", 7),
          ("police", 5),
          ("quarantine", 8),
          ("redirect", 4),
          ("setIPDscp", 6))
    )



class CTmsActionParamIdType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("be", 4),
          ("bir", 3),
          ("cir", 2),
          ("dscpVal", 6),
          ("nexthop", 5),
          ("noParams", 1),
          ("vlanId", 7))
    )



class CTmsActionParamType(Integer32, TextualConvention):
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
        *(("networkAddress", 2),
          ("string", 3),
          ("unsigned", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoTmsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTmsMIBNotifs = _CiscoTmsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 0)
)
_CiscoTmsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTmsMIBObjects = _CiscoTmsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1)
)
_CiTmsConsumerGlobals_ObjectIdentity = ObjectIdentity
ciTmsConsumerGlobals = _CiTmsConsumerGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 1)
)


class _CiTmsActiveThreats_Type(Unsigned32):
    """Custom type ciTmsActiveThreats based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiTmsActiveThreats_Type.__name__ = "Unsigned32"
_CiTmsActiveThreats_Object = MibScalar
ciTmsActiveThreats = _CiTmsActiveThreats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 1, 1),
    _CiTmsActiveThreats_Type()
)
ciTmsActiveThreats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsActiveThreats.setStatus("current")


class _CiTmsInActiveThreats_Type(Unsigned32):
    """Custom type ciTmsInActiveThreats based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiTmsInActiveThreats_Type.__name__ = "Unsigned32"
_CiTmsInActiveThreats_Object = MibScalar
ciTmsInActiveThreats = _CiTmsInActiveThreats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 1, 2),
    _CiTmsInActiveThreats_Type()
)
ciTmsInActiveThreats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsInActiveThreats.setStatus("current")
_CiTmsConsumerDeviceId_Type = SnmpAdminString
_CiTmsConsumerDeviceId_Object = MibScalar
ciTmsConsumerDeviceId = _CiTmsConsumerDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 1, 3),
    _CiTmsConsumerDeviceId_Type()
)
ciTmsConsumerDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciTmsConsumerDeviceId.setStatus("current")


class _CiTmsGroupsMaxEntries_Type(Unsigned32):
    """Custom type ciTmsGroupsMaxEntries based on Unsigned32"""
    defaultValue = 32767

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiTmsGroupsMaxEntries_Type.__name__ = "Unsigned32"
_CiTmsGroupsMaxEntries_Object = MibScalar
ciTmsGroupsMaxEntries = _CiTmsGroupsMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 1, 4),
    _CiTmsGroupsMaxEntries_Type()
)
ciTmsGroupsMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciTmsGroupsMaxEntries.setStatus("current")


class _CiTmsThreatsMaxEntries_Type(Unsigned32):
    """Custom type ciTmsThreatsMaxEntries based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiTmsThreatsMaxEntries_Type.__name__ = "Unsigned32"
_CiTmsThreatsMaxEntries_Object = MibScalar
ciTmsThreatsMaxEntries = _CiTmsThreatsMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 1, 5),
    _CiTmsThreatsMaxEntries_Type()
)
ciTmsThreatsMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciTmsThreatsMaxEntries.setStatus("current")


class _CiTmsThreatActionMaxEntries_Type(Unsigned32):
    """Custom type ciTmsThreatActionMaxEntries based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiTmsThreatActionMaxEntries_Type.__name__ = "Unsigned32"
_CiTmsThreatActionMaxEntries_Object = MibScalar
ciTmsThreatActionMaxEntries = _CiTmsThreatActionMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 1, 6),
    _CiTmsThreatActionMaxEntries_Type()
)
ciTmsThreatActionMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciTmsThreatActionMaxEntries.setStatus("current")


class _CiTmsInterfaceMaxEntries_Type(Unsigned32):
    """Custom type ciTmsInterfaceMaxEntries based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiTmsInterfaceMaxEntries_Type.__name__ = "Unsigned32"
_CiTmsInterfaceMaxEntries_Object = MibScalar
ciTmsInterfaceMaxEntries = _CiTmsInterfaceMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 1, 7),
    _CiTmsInterfaceMaxEntries_Type()
)
ciTmsInterfaceMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciTmsInterfaceMaxEntries.setStatus("current")
_CiTmsConsumerState_Type = CTmsConsumerState
_CiTmsConsumerState_Object = MibScalar
ciTmsConsumerState = _CiTmsConsumerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 1, 8),
    _CiTmsConsumerState_Type()
)
ciTmsConsumerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciTmsConsumerState.setStatus("current")
_CiTmsConsumerGroup_ObjectIdentity = ObjectIdentity
ciTmsConsumerGroup = _CiTmsConsumerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 2)
)
_CiTmsGroupTable_Object = MibTable
ciTmsGroupTable = _CiTmsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciTmsGroupTable.setStatus("current")
_CiTmsGroupEntry_Object = MibTableRow
ciTmsGroupEntry = _CiTmsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 2, 1, 1)
)
ciTmsGroupEntry.setIndexNames(
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsGroupId"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsControllerIpType"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsControllerIp"),
)
if mibBuilder.loadTexts:
    ciTmsGroupEntry.setStatus("current")


class _CiTmsGroupId_Type(Unsigned32):
    """Custom type ciTmsGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiTmsGroupId_Type.__name__ = "Unsigned32"
_CiTmsGroupId_Object = MibTableColumn
ciTmsGroupId = _CiTmsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 2, 1, 1, 1),
    _CiTmsGroupId_Type()
)
ciTmsGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciTmsGroupId.setStatus("current")
_CiTmsControllerIpType_Type = InetAddressType
_CiTmsControllerIpType_Object = MibTableColumn
ciTmsControllerIpType = _CiTmsControllerIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 2, 1, 1, 2),
    _CiTmsControllerIpType_Type()
)
ciTmsControllerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciTmsControllerIpType.setStatus("current")
_CiTmsControllerIp_Type = InetAddress
_CiTmsControllerIp_Object = MibTableColumn
ciTmsControllerIp = _CiTmsControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 2, 1, 1, 3),
    _CiTmsControllerIp_Type()
)
ciTmsControllerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciTmsControllerIp.setStatus("current")
_CiTmsGroupConsumerRegStatus_Type = CTmsConsumerRegistrationStatus
_CiTmsGroupConsumerRegStatus_Object = MibTableColumn
ciTmsGroupConsumerRegStatus = _CiTmsGroupConsumerRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 2, 1, 1, 4),
    _CiTmsGroupConsumerRegStatus_Type()
)
ciTmsGroupConsumerRegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsGroupConsumerRegStatus.setStatus("current")


class _CiTmsGroupNotifEnable_Type(TruthValue):
    """Custom type ciTmsGroupNotifEnable based on TruthValue"""


_CiTmsGroupNotifEnable_Object = MibTableColumn
ciTmsGroupNotifEnable = _CiTmsGroupNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 2, 1, 1, 5),
    _CiTmsGroupNotifEnable_Type()
)
ciTmsGroupNotifEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciTmsGroupNotifEnable.setStatus("current")


class _CiTmsGroupStorageType_Type(StorageType):
    """Custom type ciTmsGroupStorageType based on StorageType"""


_CiTmsGroupStorageType_Object = MibTableColumn
ciTmsGroupStorageType = _CiTmsGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 2, 1, 1, 6),
    _CiTmsGroupStorageType_Type()
)
ciTmsGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciTmsGroupStorageType.setStatus("current")
_CiTmsGroupRowStatus_Type = RowStatus
_CiTmsGroupRowStatus_Object = MibTableColumn
ciTmsGroupRowStatus = _CiTmsGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 2, 1, 1, 7),
    _CiTmsGroupRowStatus_Type()
)
ciTmsGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciTmsGroupRowStatus.setStatus("current")
_CiTmsConsumerThreat_ObjectIdentity = ObjectIdentity
ciTmsConsumerThreat = _CiTmsConsumerThreat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3)
)
_CiTmsThreatTable_Object = MibTable
ciTmsThreatTable = _CiTmsThreatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciTmsThreatTable.setStatus("current")
_CiTmsThreatEntry_Object = MibTableRow
ciTmsThreatEntry = _CiTmsThreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1, 1)
)
ciTmsThreatEntry.setIndexNames(
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatOwner"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatId"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsGroupId"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsControllerIpType"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsControllerIp"),
)
if mibBuilder.loadTexts:
    ciTmsThreatEntry.setStatus("current")


class _CiTmsThreatOwner_Type(Unsigned32):
    """Custom type ciTmsThreatOwner based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiTmsThreatOwner_Type.__name__ = "Unsigned32"
_CiTmsThreatOwner_Object = MibTableColumn
ciTmsThreatOwner = _CiTmsThreatOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1, 1, 1),
    _CiTmsThreatOwner_Type()
)
ciTmsThreatOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciTmsThreatOwner.setStatus("current")


class _CiTmsThreatId_Type(Unsigned32):
    """Custom type ciTmsThreatId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiTmsThreatId_Type.__name__ = "Unsigned32"
_CiTmsThreatId_Object = MibTableColumn
ciTmsThreatId = _CiTmsThreatId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1, 1, 2),
    _CiTmsThreatId_Type()
)
ciTmsThreatId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciTmsThreatId.setStatus("current")


class _CiTmsThreatVer_Type(Unsigned32):
    """Custom type ciTmsThreatVer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiTmsThreatVer_Type.__name__ = "Unsigned32"
_CiTmsThreatVer_Object = MibTableColumn
ciTmsThreatVer = _CiTmsThreatVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1, 1, 3),
    _CiTmsThreatVer_Type()
)
ciTmsThreatVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatVer.setStatus("current")
_CiTmsThreatStatus_Type = CTmsThreatStatus
_CiTmsThreatStatus_Object = MibTableColumn
ciTmsThreatStatus = _CiTmsThreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1, 1, 4),
    _CiTmsThreatStatus_Type()
)
ciTmsThreatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatStatus.setStatus("current")
_CiTmsThreatClass_Type = SnmpAdminString
_CiTmsThreatClass_Object = MibTableColumn
ciTmsThreatClass = _CiTmsThreatClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1, 1, 5),
    _CiTmsThreatClass_Type()
)
ciTmsThreatClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatClass.setStatus("current")
_CiTmsThreatName_Type = SnmpAdminString
_CiTmsThreatName_Object = MibTableColumn
ciTmsThreatName = _CiTmsThreatName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1, 1, 6),
    _CiTmsThreatName_Type()
)
ciTmsThreatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatName.setStatus("current")
_CiTmsThreatActiveTimeDuration_Type = DateAndTime
_CiTmsThreatActiveTimeDuration_Object = MibTableColumn
ciTmsThreatActiveTimeDuration = _CiTmsThreatActiveTimeDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1, 1, 7),
    _CiTmsThreatActiveTimeDuration_Type()
)
ciTmsThreatActiveTimeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatActiveTimeDuration.setStatus("current")


class _CiTmsThreatPriority_Type(Unsigned32):
    """Custom type ciTmsThreatPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CiTmsThreatPriority_Type.__name__ = "Unsigned32"
_CiTmsThreatPriority_Object = MibTableColumn
ciTmsThreatPriority = _CiTmsThreatPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1, 1, 8),
    _CiTmsThreatPriority_Type()
)
ciTmsThreatPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatPriority.setStatus("current")
_CiTmsThreatTcdf_Type = SnmpAdminString
_CiTmsThreatTcdf_Object = MibTableColumn
ciTmsThreatTcdf = _CiTmsThreatTcdf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 1, 1, 9),
    _CiTmsThreatTcdf_Type()
)
ciTmsThreatTcdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatTcdf.setStatus("current")
_CiTmsThreatActionTable_Object = MibTable
ciTmsThreatActionTable = _CiTmsThreatActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ciTmsThreatActionTable.setStatus("current")
_CiTmsThreatActionEntry_Object = MibTableRow
ciTmsThreatActionEntry = _CiTmsThreatActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 2, 1)
)
ciTmsThreatActionEntry.setIndexNames(
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatOwner"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatId"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsGroupId"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsControllerIpType"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsControllerIp"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatAction"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActionParamId"),
)
if mibBuilder.loadTexts:
    ciTmsThreatActionEntry.setStatus("current")
_CiTmsThreatAction_Type = CTmsActionType
_CiTmsThreatAction_Object = MibTableColumn
ciTmsThreatAction = _CiTmsThreatAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 2, 1, 1),
    _CiTmsThreatAction_Type()
)
ciTmsThreatAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciTmsThreatAction.setStatus("current")
_CiTmsThreatActionParamId_Type = CTmsActionParamIdType
_CiTmsThreatActionParamId_Object = MibTableColumn
ciTmsThreatActionParamId = _CiTmsThreatActionParamId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 2, 1, 2),
    _CiTmsThreatActionParamId_Type()
)
ciTmsThreatActionParamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciTmsThreatActionParamId.setStatus("current")
_CiTmsThreatActionParamType_Type = CTmsActionParamType
_CiTmsThreatActionParamType_Object = MibTableColumn
ciTmsThreatActionParamType = _CiTmsThreatActionParamType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 2, 1, 3),
    _CiTmsThreatActionParamType_Type()
)
ciTmsThreatActionParamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatActionParamType.setStatus("current")


class _CiTmsThreatActionParamLength_Type(Unsigned32):
    """Custom type ciTmsThreatActionParamLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiTmsThreatActionParamLength_Type.__name__ = "Unsigned32"
_CiTmsThreatActionParamLength_Object = MibTableColumn
ciTmsThreatActionParamLength = _CiTmsThreatActionParamLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 2, 1, 4),
    _CiTmsThreatActionParamLength_Type()
)
ciTmsThreatActionParamLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatActionParamLength.setStatus("current")
_CiTmsThreatActionParamValue_Type = SnmpAdminString
_CiTmsThreatActionParamValue_Object = MibTableColumn
ciTmsThreatActionParamValue = _CiTmsThreatActionParamValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 2, 1, 5),
    _CiTmsThreatActionParamValue_Type()
)
ciTmsThreatActionParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatActionParamValue.setStatus("current")
_CiTmsThreatActionFailReason_Type = SnmpAdminString
_CiTmsThreatActionFailReason_Object = MibTableColumn
ciTmsThreatActionFailReason = _CiTmsThreatActionFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 2, 1, 6),
    _CiTmsThreatActionFailReason_Type()
)
ciTmsThreatActionFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciTmsThreatActionFailReason.setStatus("current")
_CiTmsThreatInterfaceTable_Object = MibTable
ciTmsThreatInterfaceTable = _CiTmsThreatInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ciTmsThreatInterfaceTable.setStatus("current")
_CiTmsThreatInterfaceEntry_Object = MibTableRow
ciTmsThreatInterfaceEntry = _CiTmsThreatInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 3, 1)
)
ciTmsThreatInterfaceEntry.setIndexNames(
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatId"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatOwner"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsGroupId"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsControllerIpType"),
    (0, "CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsControllerIp"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciTmsThreatInterfaceEntry.setStatus("current")
_CiThreatInterfaceMitigationApplied_Type = TruthValue
_CiThreatInterfaceMitigationApplied_Object = MibTableColumn
ciThreatInterfaceMitigationApplied = _CiThreatInterfaceMitigationApplied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 3, 3, 1, 1),
    _CiThreatInterfaceMitigationApplied_Type()
)
ciThreatInterfaceMitigationApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciThreatInterfaceMitigationApplied.setStatus("current")
_CiTiTmsConsumerNotifs_ObjectIdentity = ObjectIdentity
ciTiTmsConsumerNotifs = _CiTiTmsConsumerNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 4)
)


class _CiTmsConsStateChangeNotifEnable_Type(TruthValue):
    """Custom type ciTmsConsStateChangeNotifEnable based on TruthValue"""


_CiTmsConsStateChangeNotifEnable_Object = MibScalar
ciTmsConsStateChangeNotifEnable = _CiTmsConsStateChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 1, 4, 1),
    _CiTmsConsStateChangeNotifEnable_Type()
)
ciTmsConsStateChangeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciTmsConsStateChangeNotifEnable.setStatus("current")
_CiscoTmsMIBConform_ObjectIdentity = ObjectIdentity
ciscoTmsMIBConform = _CiscoTmsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 2)
)
_CiscoTmsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTmsMIBCompliances = _CiscoTmsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 2, 1)
)
_CiscoTmsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTmsMIBGroups = _CiscoTmsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 2, 2)
)

# Managed Objects groups

ciscoTmsConsumerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 2, 2, 1)
)
ciscoTmsConsumerGroup.setObjects(
      *(("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsConsumerDeviceId"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsGroupsMaxEntries"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatsMaxEntries"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActionMaxEntries"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsInterfaceMaxEntries"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsConsumerState"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsConsStateChangeNotifEnable"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsGroupConsumerRegStatus"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsGroupNotifEnable"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsGroupStorageType"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoTmsConsumerGroup.setStatus("current")

ciscoTmsThreatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 2, 2, 2)
)
ciscoTmsThreatGroup.setObjects(
      *(("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsActiveThreats"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsInActiveThreats"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatVer"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatStatus"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatClass"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatName"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActiveTimeDuration"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatPriority"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatTcdf"))
)
if mibBuilder.loadTexts:
    ciscoTmsThreatGroup.setStatus("current")

ciscoTmsThreatActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 2, 2, 3)
)
ciscoTmsThreatActionGroup.setObjects(
      *(("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActionParamType"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActionParamLength"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActionParamValue"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActionFailReason"))
)
if mibBuilder.loadTexts:
    ciscoTmsThreatActionGroup.setStatus("current")

ciscoTmsThreatInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 2, 2, 4)
)
ciscoTmsThreatInterfaceGroup.setObjects(
    ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciThreatInterfaceMitigationApplied")
)
if mibBuilder.loadTexts:
    ciscoTmsThreatInterfaceGroup.setStatus("current")


# Notification objects

ciscoTmsConsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 0, 1)
)
ciscoTmsConsStateChange.setObjects(
    ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsConsumerState")
)
if mibBuilder.loadTexts:
    ciscoTmsConsStateChange.setStatus(
        "current"
    )

ciscoTmsControllerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 0, 2)
)
ciscoTmsControllerUnreachable.setObjects(
    ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsGroupConsumerRegStatus")
)
if mibBuilder.loadTexts:
    ciscoTmsControllerUnreachable.setStatus(
        "current"
    )

ciscoTmsThreatStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 0, 3)
)
ciscoTmsThreatStatusChange.setObjects(
      *(("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatVer"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatStatus"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatPriority"))
)
if mibBuilder.loadTexts:
    ciscoTmsThreatStatusChange.setStatus(
        "current"
    )

ciscoTmsMitigationActionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 0, 4)
)
ciscoTmsMitigationActionFailed.setObjects(
      *(("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActionParamType"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActionParamLength"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActionParamValue"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciTmsThreatActionFailReason"))
)
if mibBuilder.loadTexts:
    ciscoTmsMitigationActionFailed.setStatus(
        "current"
    )


# Notifications groups

ciscoTmsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 2, 2, 5)
)
ciscoTmsNotificationGroup.setObjects(
      *(("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciscoTmsConsStateChange"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciscoTmsControllerUnreachable"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciscoTmsThreatStatusChange"),
        ("CISCO-THREAT-MITIGATION-SERVICE-MIB", "ciscoTmsMitigationActionFailed"))
)
if mibBuilder.loadTexts:
    ciscoTmsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTmsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 603, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTmsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-THREAT-MITIGATION-SERVICE-MIB",
    **{"CTmsConsumerState": CTmsConsumerState,
       "CTmsConsumerRegistrationStatus": CTmsConsumerRegistrationStatus,
       "CTmsThreatStatus": CTmsThreatStatus,
       "CTmsActionType": CTmsActionType,
       "CTmsActionParamIdType": CTmsActionParamIdType,
       "CTmsActionParamType": CTmsActionParamType,
       "ciscoThreatMitigationServiceMIB": ciscoThreatMitigationServiceMIB,
       "ciscoTmsMIBNotifs": ciscoTmsMIBNotifs,
       "ciscoTmsConsStateChange": ciscoTmsConsStateChange,
       "ciscoTmsControllerUnreachable": ciscoTmsControllerUnreachable,
       "ciscoTmsThreatStatusChange": ciscoTmsThreatStatusChange,
       "ciscoTmsMitigationActionFailed": ciscoTmsMitigationActionFailed,
       "ciscoTmsMIBObjects": ciscoTmsMIBObjects,
       "ciTmsConsumerGlobals": ciTmsConsumerGlobals,
       "ciTmsActiveThreats": ciTmsActiveThreats,
       "ciTmsInActiveThreats": ciTmsInActiveThreats,
       "ciTmsConsumerDeviceId": ciTmsConsumerDeviceId,
       "ciTmsGroupsMaxEntries": ciTmsGroupsMaxEntries,
       "ciTmsThreatsMaxEntries": ciTmsThreatsMaxEntries,
       "ciTmsThreatActionMaxEntries": ciTmsThreatActionMaxEntries,
       "ciTmsInterfaceMaxEntries": ciTmsInterfaceMaxEntries,
       "ciTmsConsumerState": ciTmsConsumerState,
       "ciTmsConsumerGroup": ciTmsConsumerGroup,
       "ciTmsGroupTable": ciTmsGroupTable,
       "ciTmsGroupEntry": ciTmsGroupEntry,
       "ciTmsGroupId": ciTmsGroupId,
       "ciTmsControllerIpType": ciTmsControllerIpType,
       "ciTmsControllerIp": ciTmsControllerIp,
       "ciTmsGroupConsumerRegStatus": ciTmsGroupConsumerRegStatus,
       "ciTmsGroupNotifEnable": ciTmsGroupNotifEnable,
       "ciTmsGroupStorageType": ciTmsGroupStorageType,
       "ciTmsGroupRowStatus": ciTmsGroupRowStatus,
       "ciTmsConsumerThreat": ciTmsConsumerThreat,
       "ciTmsThreatTable": ciTmsThreatTable,
       "ciTmsThreatEntry": ciTmsThreatEntry,
       "ciTmsThreatOwner": ciTmsThreatOwner,
       "ciTmsThreatId": ciTmsThreatId,
       "ciTmsThreatVer": ciTmsThreatVer,
       "ciTmsThreatStatus": ciTmsThreatStatus,
       "ciTmsThreatClass": ciTmsThreatClass,
       "ciTmsThreatName": ciTmsThreatName,
       "ciTmsThreatActiveTimeDuration": ciTmsThreatActiveTimeDuration,
       "ciTmsThreatPriority": ciTmsThreatPriority,
       "ciTmsThreatTcdf": ciTmsThreatTcdf,
       "ciTmsThreatActionTable": ciTmsThreatActionTable,
       "ciTmsThreatActionEntry": ciTmsThreatActionEntry,
       "ciTmsThreatAction": ciTmsThreatAction,
       "ciTmsThreatActionParamId": ciTmsThreatActionParamId,
       "ciTmsThreatActionParamType": ciTmsThreatActionParamType,
       "ciTmsThreatActionParamLength": ciTmsThreatActionParamLength,
       "ciTmsThreatActionParamValue": ciTmsThreatActionParamValue,
       "ciTmsThreatActionFailReason": ciTmsThreatActionFailReason,
       "ciTmsThreatInterfaceTable": ciTmsThreatInterfaceTable,
       "ciTmsThreatInterfaceEntry": ciTmsThreatInterfaceEntry,
       "ciThreatInterfaceMitigationApplied": ciThreatInterfaceMitigationApplied,
       "ciTiTmsConsumerNotifs": ciTiTmsConsumerNotifs,
       "ciTmsConsStateChangeNotifEnable": ciTmsConsStateChangeNotifEnable,
       "ciscoTmsMIBConform": ciscoTmsMIBConform,
       "ciscoTmsMIBCompliances": ciscoTmsMIBCompliances,
       "ciscoTmsMIBCompliance": ciscoTmsMIBCompliance,
       "ciscoTmsMIBGroups": ciscoTmsMIBGroups,
       "ciscoTmsConsumerGroup": ciscoTmsConsumerGroup,
       "ciscoTmsThreatGroup": ciscoTmsThreatGroup,
       "ciscoTmsThreatActionGroup": ciscoTmsThreatActionGroup,
       "ciscoTmsThreatInterfaceGroup": ciscoTmsThreatInterfaceGroup,
       "ciscoTmsNotificationGroup": ciscoTmsNotificationGroup}
)
