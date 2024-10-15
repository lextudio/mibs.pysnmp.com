# SNMP MIB module (CISCO-CABLE-ADMISSION-CTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CABLE-ADMISSION-CTRL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:31 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

ciscoCableAdmCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 450)
)
ciscoCableAdmCtrlMIB.setRevisions(
        ("2006-10-25 00:00",
         "2005-05-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class NonZeroPercent(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TenthPercent(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class CcacSchedulingType(Integer32, TextualConvention):
    status = "deprecated"
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
        *(("bestEffort", 2),
          ("nonRealTimePollingService", 3),
          ("realTimePollingService", 4),
          ("undefined", 1),
          ("unsolictedGrantService", 6),
          ("unsolictedGrantServiceWithAD", 5))
    )



class CcacApplicationBucketType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class QoSServiceClassNameOrNull(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )



class CcacMonitoredEvent(Bits, TextualConvention):
    status = "current"


class CcacSysRscMonitoredType(Integer32, TextualConvention):
    status = "current"
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
        *(("cpu1Min", 2),
          ("cpu5Sec", 1),
          ("ioMem", 4),
          ("procMem", 3),
          ("totalMem", 5))
    )



class CcacDSTrafficMonitoredType(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("voice", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCableAdmCtrlMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCableAdmCtrlMIBNotifs = _CiscoCableAdmCtrlMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 0)
)
_CiscoCableAdmCtrlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCableAdmCtrlMIBObjects = _CiscoCableAdmCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1)
)
_CcacObjects_ObjectIdentity = ObjectIdentity
ccacObjects = _CcacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 1)
)


class _CcacNotifyEnable_Type(TruthValue):
    """Custom type ccacNotifyEnable based on TruthValue"""


_CcacNotifyEnable_Object = MibScalar
ccacNotifyEnable = _CcacNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 1, 1),
    _CcacNotifyEnable_Type()
)
ccacNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacNotifyEnable.setStatus("current")


class _CcacEventMonitoring_Type(CcacMonitoredEvent):
    """Custom type ccacEventMonitoring based on CcacMonitoredEvent"""
    defaultBinValue = "0"


_CcacEventMonitoring_Object = MibScalar
ccacEventMonitoring = _CcacEventMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 1, 2),
    _CcacEventMonitoring_Type()
)
ccacEventMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacEventMonitoring.setStatus("current")
_CcacConfigObjects_ObjectIdentity = ObjectIdentity
ccacConfigObjects = _CcacConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2)
)
_CcacSysRscConfigTable_Object = MibTable
ccacSysRscConfigTable = _CcacSysRscConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccacSysRscConfigTable.setStatus("current")
_CcacSysRscConfigEntry_Object = MibTableRow
ccacSysRscConfigEntry = _CcacSysRscConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 1, 1)
)
ccacSysRscConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscConfigResourceType"),
)
if mibBuilder.loadTexts:
    ccacSysRscConfigEntry.setStatus("current")
_CcacSysRscConfigResourceType_Type = CcacSysRscMonitoredType
_CcacSysRscConfigResourceType_Object = MibTableColumn
ccacSysRscConfigResourceType = _CcacSysRscConfigResourceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 1, 1, 1),
    _CcacSysRscConfigResourceType_Type()
)
ccacSysRscConfigResourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacSysRscConfigResourceType.setStatus("current")
_CcacSysRscConfigStatus_Type = RowStatus
_CcacSysRscConfigStatus_Object = MibTableColumn
ccacSysRscConfigStatus = _CcacSysRscConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 1, 1, 2),
    _CcacSysRscConfigStatus_Type()
)
ccacSysRscConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacSysRscConfigStatus.setStatus("current")
_CcacSysRscConfigMinorThreshold_Type = NonZeroPercent
_CcacSysRscConfigMinorThreshold_Object = MibTableColumn
ccacSysRscConfigMinorThreshold = _CcacSysRscConfigMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 1, 1, 3),
    _CcacSysRscConfigMinorThreshold_Type()
)
ccacSysRscConfigMinorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacSysRscConfigMinorThreshold.setStatus("current")
_CcacSysRscConfigMajorThreshold_Type = NonZeroPercent
_CcacSysRscConfigMajorThreshold_Object = MibTableColumn
ccacSysRscConfigMajorThreshold = _CcacSysRscConfigMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 1, 1, 4),
    _CcacSysRscConfigMajorThreshold_Type()
)
ccacSysRscConfigMajorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacSysRscConfigMajorThreshold.setStatus("current")
_CcacSysRscConfigCritThreshold_Type = NonZeroPercent
_CcacSysRscConfigCritThreshold_Object = MibTableColumn
ccacSysRscConfigCritThreshold = _CcacSysRscConfigCritThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 1, 1, 5),
    _CcacSysRscConfigCritThreshold_Type()
)
ccacSysRscConfigCritThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacSysRscConfigCritThreshold.setStatus("current")
_CcacUsConfigTable_Object = MibTable
ccacUsConfigTable = _CcacUsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccacUsConfigTable.setStatus("deprecated")
_CcacUsConfigEntry_Object = MibTableRow
ccacUsConfigEntry = _CcacUsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 2, 1)
)
ccacUsConfigEntry.setIndexNames(
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigIfIndex"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigSchedType"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigServiceClassName"),
)
if mibBuilder.loadTexts:
    ccacUsConfigEntry.setStatus("deprecated")
_CcacUsConfigIfIndex_Type = InterfaceIndexOrZero
_CcacUsConfigIfIndex_Object = MibTableColumn
ccacUsConfigIfIndex = _CcacUsConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 2, 1, 1),
    _CcacUsConfigIfIndex_Type()
)
ccacUsConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacUsConfigIfIndex.setStatus("deprecated")
_CcacUsConfigSchedType_Type = CcacSchedulingType
_CcacUsConfigSchedType_Object = MibTableColumn
ccacUsConfigSchedType = _CcacUsConfigSchedType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 2, 1, 2),
    _CcacUsConfigSchedType_Type()
)
ccacUsConfigSchedType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacUsConfigSchedType.setStatus("deprecated")
_CcacUsConfigServiceClassName_Type = QoSServiceClassNameOrNull
_CcacUsConfigServiceClassName_Object = MibTableColumn
ccacUsConfigServiceClassName = _CcacUsConfigServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 2, 1, 3),
    _CcacUsConfigServiceClassName_Type()
)
ccacUsConfigServiceClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacUsConfigServiceClassName.setStatus("deprecated")
_CcacUsConfigStatus_Type = RowStatus
_CcacUsConfigStatus_Object = MibTableColumn
ccacUsConfigStatus = _CcacUsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 2, 1, 4),
    _CcacUsConfigStatus_Type()
)
ccacUsConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigStatus.setStatus("deprecated")
_CcacUsConfigMinorThreshold_Type = NonZeroPercent
_CcacUsConfigMinorThreshold_Object = MibTableColumn
ccacUsConfigMinorThreshold = _CcacUsConfigMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 2, 1, 5),
    _CcacUsConfigMinorThreshold_Type()
)
ccacUsConfigMinorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigMinorThreshold.setStatus("deprecated")
_CcacUsConfigMajorThreshold_Type = NonZeroPercent
_CcacUsConfigMajorThreshold_Object = MibTableColumn
ccacUsConfigMajorThreshold = _CcacUsConfigMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 2, 1, 6),
    _CcacUsConfigMajorThreshold_Type()
)
ccacUsConfigMajorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigMajorThreshold.setStatus("deprecated")
_CcacUsConfigExclusivePercent_Type = NonZeroPercent
_CcacUsConfigExclusivePercent_Object = MibTableColumn
ccacUsConfigExclusivePercent = _CcacUsConfigExclusivePercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 2, 1, 7),
    _CcacUsConfigExclusivePercent_Type()
)
ccacUsConfigExclusivePercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigExclusivePercent.setStatus("deprecated")
_CcacUsConfigNonExclusivePercent_Type = Percent
_CcacUsConfigNonExclusivePercent_Object = MibTableColumn
ccacUsConfigNonExclusivePercent = _CcacUsConfigNonExclusivePercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 2, 1, 8),
    _CcacUsConfigNonExclusivePercent_Type()
)
ccacUsConfigNonExclusivePercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigNonExclusivePercent.setStatus("deprecated")
_CcacDsConfigTable_Object = MibTable
ccacDsConfigTable = _CcacDsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ccacDsConfigTable.setStatus("deprecated")
_CcacDsConfigEntry_Object = MibTableRow
ccacDsConfigEntry = _CcacDsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 3, 1)
)
ccacDsConfigEntry.setIndexNames(
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigIfIndex"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigTrafficType"),
)
if mibBuilder.loadTexts:
    ccacDsConfigEntry.setStatus("deprecated")
_CcacDsConfigIfIndex_Type = InterfaceIndexOrZero
_CcacDsConfigIfIndex_Object = MibTableColumn
ccacDsConfigIfIndex = _CcacDsConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 3, 1, 1),
    _CcacDsConfigIfIndex_Type()
)
ccacDsConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacDsConfigIfIndex.setStatus("deprecated")
_CcacDsConfigTrafficType_Type = CcacDSTrafficMonitoredType
_CcacDsConfigTrafficType_Object = MibTableColumn
ccacDsConfigTrafficType = _CcacDsConfigTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 3, 1, 2),
    _CcacDsConfigTrafficType_Type()
)
ccacDsConfigTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacDsConfigTrafficType.setStatus("deprecated")
_CcacDsConfigStatus_Type = RowStatus
_CcacDsConfigStatus_Object = MibTableColumn
ccacDsConfigStatus = _CcacDsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 3, 1, 3),
    _CcacDsConfigStatus_Type()
)
ccacDsConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigStatus.setStatus("deprecated")
_CcacDsConfigMinorThreshold_Type = NonZeroPercent
_CcacDsConfigMinorThreshold_Object = MibTableColumn
ccacDsConfigMinorThreshold = _CcacDsConfigMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 3, 1, 4),
    _CcacDsConfigMinorThreshold_Type()
)
ccacDsConfigMinorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigMinorThreshold.setStatus("deprecated")
_CcacDsConfigMajorThreshold_Type = NonZeroPercent
_CcacDsConfigMajorThreshold_Object = MibTableColumn
ccacDsConfigMajorThreshold = _CcacDsConfigMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 3, 1, 5),
    _CcacDsConfigMajorThreshold_Type()
)
ccacDsConfigMajorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigMajorThreshold.setStatus("deprecated")
_CcacDsConfigExclusivePercent_Type = NonZeroPercent
_CcacDsConfigExclusivePercent_Object = MibTableColumn
ccacDsConfigExclusivePercent = _CcacDsConfigExclusivePercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 3, 1, 6),
    _CcacDsConfigExclusivePercent_Type()
)
ccacDsConfigExclusivePercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigExclusivePercent.setStatus("deprecated")
_CcacDsConfigNonExclusivePercent_Type = Percent
_CcacDsConfigNonExclusivePercent_Object = MibTableColumn
ccacDsConfigNonExclusivePercent = _CcacDsConfigNonExclusivePercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 3, 1, 7),
    _CcacDsConfigNonExclusivePercent_Type()
)
ccacDsConfigNonExclusivePercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigNonExclusivePercent.setStatus("deprecated")
_CcacUsConfigRevTable_Object = MibTable
ccacUsConfigRevTable = _CcacUsConfigRevTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ccacUsConfigRevTable.setStatus("current")
_CcacUsConfigRevEntry_Object = MibTableRow
ccacUsConfigRevEntry = _CcacUsConfigRevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4, 1)
)
ccacUsConfigRevEntry.setIndexNames(
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigRevIfIndex"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigRevAppBucketIndex"),
)
if mibBuilder.loadTexts:
    ccacUsConfigRevEntry.setStatus("current")
_CcacUsConfigRevIfIndex_Type = InterfaceIndexOrZero
_CcacUsConfigRevIfIndex_Object = MibTableColumn
ccacUsConfigRevIfIndex = _CcacUsConfigRevIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4, 1, 1),
    _CcacUsConfigRevIfIndex_Type()
)
ccacUsConfigRevIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacUsConfigRevIfIndex.setStatus("current")
_CcacUsConfigRevAppBucketIndex_Type = CcacApplicationBucketType
_CcacUsConfigRevAppBucketIndex_Object = MibTableColumn
ccacUsConfigRevAppBucketIndex = _CcacUsConfigRevAppBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4, 1, 2),
    _CcacUsConfigRevAppBucketIndex_Type()
)
ccacUsConfigRevAppBucketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacUsConfigRevAppBucketIndex.setStatus("current")
_CcacUsConfigRevAppBucketName_Type = SnmpAdminString
_CcacUsConfigRevAppBucketName_Object = MibTableColumn
ccacUsConfigRevAppBucketName = _CcacUsConfigRevAppBucketName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4, 1, 3),
    _CcacUsConfigRevAppBucketName_Type()
)
ccacUsConfigRevAppBucketName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigRevAppBucketName.setStatus("current")
_CcacUsConfigRevMinorThreshold_Type = NonZeroPercent
_CcacUsConfigRevMinorThreshold_Object = MibTableColumn
ccacUsConfigRevMinorThreshold = _CcacUsConfigRevMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4, 1, 4),
    _CcacUsConfigRevMinorThreshold_Type()
)
ccacUsConfigRevMinorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigRevMinorThreshold.setStatus("current")
_CcacUsConfigRevMajorThreshold_Type = NonZeroPercent
_CcacUsConfigRevMajorThreshold_Object = MibTableColumn
ccacUsConfigRevMajorThreshold = _CcacUsConfigRevMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4, 1, 5),
    _CcacUsConfigRevMajorThreshold_Type()
)
ccacUsConfigRevMajorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigRevMajorThreshold.setStatus("current")
_CcacUsConfigRevExclusivePercent_Type = NonZeroPercent
_CcacUsConfigRevExclusivePercent_Object = MibTableColumn
ccacUsConfigRevExclusivePercent = _CcacUsConfigRevExclusivePercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4, 1, 6),
    _CcacUsConfigRevExclusivePercent_Type()
)
ccacUsConfigRevExclusivePercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigRevExclusivePercent.setStatus("current")
_CcacUsConfigRevNonExclusivePercent_Type = Percent
_CcacUsConfigRevNonExclusivePercent_Object = MibTableColumn
ccacUsConfigRevNonExclusivePercent = _CcacUsConfigRevNonExclusivePercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4, 1, 7),
    _CcacUsConfigRevNonExclusivePercent_Type()
)
ccacUsConfigRevNonExclusivePercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigRevNonExclusivePercent.setStatus("current")


class _CcacUsConfigRevStorageType_Type(StorageType):
    """Custom type ccacUsConfigRevStorageType based on StorageType"""


_CcacUsConfigRevStorageType_Object = MibTableColumn
ccacUsConfigRevStorageType = _CcacUsConfigRevStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4, 1, 8),
    _CcacUsConfigRevStorageType_Type()
)
ccacUsConfigRevStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigRevStorageType.setStatus("current")
_CcacUsConfigRevStatus_Type = RowStatus
_CcacUsConfigRevStatus_Object = MibTableColumn
ccacUsConfigRevStatus = _CcacUsConfigRevStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 4, 1, 9),
    _CcacUsConfigRevStatus_Type()
)
ccacUsConfigRevStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacUsConfigRevStatus.setStatus("current")
_CcacDsConfigRevTable_Object = MibTable
ccacDsConfigRevTable = _CcacDsConfigRevTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ccacDsConfigRevTable.setStatus("current")
_CcacDsConfigRevEntry_Object = MibTableRow
ccacDsConfigRevEntry = _CcacDsConfigRevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5, 1)
)
ccacDsConfigRevEntry.setIndexNames(
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigRevIfIndex"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigRevAppBucketIndex"),
)
if mibBuilder.loadTexts:
    ccacDsConfigRevEntry.setStatus("current")
_CcacDsConfigRevIfIndex_Type = InterfaceIndexOrZero
_CcacDsConfigRevIfIndex_Object = MibTableColumn
ccacDsConfigRevIfIndex = _CcacDsConfigRevIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5, 1, 1),
    _CcacDsConfigRevIfIndex_Type()
)
ccacDsConfigRevIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacDsConfigRevIfIndex.setStatus("current")
_CcacDsConfigRevAppBucketIndex_Type = CcacApplicationBucketType
_CcacDsConfigRevAppBucketIndex_Object = MibTableColumn
ccacDsConfigRevAppBucketIndex = _CcacDsConfigRevAppBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5, 1, 2),
    _CcacDsConfigRevAppBucketIndex_Type()
)
ccacDsConfigRevAppBucketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacDsConfigRevAppBucketIndex.setStatus("current")
_CcacDsConfigRevAppBucketName_Type = SnmpAdminString
_CcacDsConfigRevAppBucketName_Object = MibTableColumn
ccacDsConfigRevAppBucketName = _CcacDsConfigRevAppBucketName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5, 1, 3),
    _CcacDsConfigRevAppBucketName_Type()
)
ccacDsConfigRevAppBucketName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigRevAppBucketName.setStatus("current")
_CcacDsConfigRevMinorThreshold_Type = NonZeroPercent
_CcacDsConfigRevMinorThreshold_Object = MibTableColumn
ccacDsConfigRevMinorThreshold = _CcacDsConfigRevMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5, 1, 4),
    _CcacDsConfigRevMinorThreshold_Type()
)
ccacDsConfigRevMinorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigRevMinorThreshold.setStatus("current")
_CcacDsConfigRevMajorThreshold_Type = NonZeroPercent
_CcacDsConfigRevMajorThreshold_Object = MibTableColumn
ccacDsConfigRevMajorThreshold = _CcacDsConfigRevMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5, 1, 5),
    _CcacDsConfigRevMajorThreshold_Type()
)
ccacDsConfigRevMajorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigRevMajorThreshold.setStatus("current")
_CcacDsConfigRevExclusivePercent_Type = NonZeroPercent
_CcacDsConfigRevExclusivePercent_Object = MibTableColumn
ccacDsConfigRevExclusivePercent = _CcacDsConfigRevExclusivePercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5, 1, 6),
    _CcacDsConfigRevExclusivePercent_Type()
)
ccacDsConfigRevExclusivePercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigRevExclusivePercent.setStatus("current")
_CcacDsConfigRevNonExclusivePercent_Type = Percent
_CcacDsConfigRevNonExclusivePercent_Object = MibTableColumn
ccacDsConfigRevNonExclusivePercent = _CcacDsConfigRevNonExclusivePercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5, 1, 7),
    _CcacDsConfigRevNonExclusivePercent_Type()
)
ccacDsConfigRevNonExclusivePercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigRevNonExclusivePercent.setStatus("current")


class _CcacDsConfigRevStorageType_Type(StorageType):
    """Custom type ccacDsConfigRevStorageType based on StorageType"""


_CcacDsConfigRevStorageType_Object = MibTableColumn
ccacDsConfigRevStorageType = _CcacDsConfigRevStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5, 1, 8),
    _CcacDsConfigRevStorageType_Type()
)
ccacDsConfigRevStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigRevStorageType.setStatus("current")
_CcacDsConfigRevStatus_Type = RowStatus
_CcacDsConfigRevStatus_Object = MibTableColumn
ccacDsConfigRevStatus = _CcacDsConfigRevStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 2, 5, 1, 9),
    _CcacDsConfigRevStatus_Type()
)
ccacDsConfigRevStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccacDsConfigRevStatus.setStatus("current")
_CcacStatObjects_ObjectIdentity = ObjectIdentity
ccacStatObjects = _CcacStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3)
)
_CcacSysRscTable_Object = MibTable
ccacSysRscTable = _CcacSysRscTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccacSysRscTable.setStatus("current")
_CcacSysRscEntry_Object = MibTableRow
ccacSysRscEntry = _CcacSysRscEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 1, 1)
)
ccacSysRscEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscType"),
)
if mibBuilder.loadTexts:
    ccacSysRscEntry.setStatus("current")
_CcacSysRscType_Type = CcacSysRscMonitoredType
_CcacSysRscType_Object = MibTableColumn
ccacSysRscType = _CcacSysRscType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 1, 1, 1),
    _CcacSysRscType_Type()
)
ccacSysRscType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacSysRscType.setStatus("current")
_CcacSysRscUtilization_Type = Percent
_CcacSysRscUtilization_Object = MibTableColumn
ccacSysRscUtilization = _CcacSysRscUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 1, 1, 2),
    _CcacSysRscUtilization_Type()
)
ccacSysRscUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRscUtilization.setStatus("current")
_CcacSysRscMinorCrosses_Type = Counter32
_CcacSysRscMinorCrosses_Object = MibTableColumn
ccacSysRscMinorCrosses = _CcacSysRscMinorCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 1, 1, 3),
    _CcacSysRscMinorCrosses_Type()
)
ccacSysRscMinorCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRscMinorCrosses.setStatus("current")
_CcacSysRscMajorCrosses_Type = Counter32
_CcacSysRscMajorCrosses_Object = MibTableColumn
ccacSysRscMajorCrosses = _CcacSysRscMajorCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 1, 1, 4),
    _CcacSysRscMajorCrosses_Type()
)
ccacSysRscMajorCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRscMajorCrosses.setStatus("current")
_CcacSysRscCriticalCrosses_Type = Counter32
_CcacSysRscCriticalCrosses_Object = MibTableColumn
ccacSysRscCriticalCrosses = _CcacSysRscCriticalCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 1, 1, 5),
    _CcacSysRscCriticalCrosses_Type()
)
ccacSysRscCriticalCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRscCriticalCrosses.setStatus("current")
_CcacSysRscCountersDscTime_Type = TimeStamp
_CcacSysRscCountersDscTime_Object = MibTableColumn
ccacSysRscCountersDscTime = _CcacSysRscCountersDscTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 1, 1, 6),
    _CcacSysRscCountersDscTime_Type()
)
ccacSysRscCountersDscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacSysRscCountersDscTime.setStatus("current")
_CcacUsTable_Object = MibTable
ccacUsTable = _CcacUsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ccacUsTable.setStatus("deprecated")
_CcacUsEntry_Object = MibTableRow
ccacUsEntry = _CcacUsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 2, 1)
)
ccacUsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsSchedType"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsServiceClassName"),
)
if mibBuilder.loadTexts:
    ccacUsEntry.setStatus("deprecated")
_CcacUsSchedType_Type = CcacSchedulingType
_CcacUsSchedType_Object = MibTableColumn
ccacUsSchedType = _CcacUsSchedType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 2, 1, 1),
    _CcacUsSchedType_Type()
)
ccacUsSchedType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacUsSchedType.setStatus("deprecated")
_CcacUsServiceClassName_Type = QoSServiceClassNameOrNull
_CcacUsServiceClassName_Object = MibTableColumn
ccacUsServiceClassName = _CcacUsServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 2, 1, 2),
    _CcacUsServiceClassName_Type()
)
ccacUsServiceClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacUsServiceClassName.setStatus("deprecated")
_CcacUsUtilization_Type = Percent
_CcacUsUtilization_Object = MibTableColumn
ccacUsUtilization = _CcacUsUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 2, 1, 3),
    _CcacUsUtilization_Type()
)
ccacUsUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacUsUtilization.setStatus("deprecated")
_CcacUsMinorCrosses_Type = Counter32
_CcacUsMinorCrosses_Object = MibTableColumn
ccacUsMinorCrosses = _CcacUsMinorCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 2, 1, 4),
    _CcacUsMinorCrosses_Type()
)
ccacUsMinorCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacUsMinorCrosses.setStatus("deprecated")
_CcacUsMajorCrosses_Type = Counter32
_CcacUsMajorCrosses_Object = MibTableColumn
ccacUsMajorCrosses = _CcacUsMajorCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 2, 1, 5),
    _CcacUsMajorCrosses_Type()
)
ccacUsMajorCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacUsMajorCrosses.setStatus("deprecated")
_CcacUsExclusiveCrosses_Type = Counter32
_CcacUsExclusiveCrosses_Object = MibTableColumn
ccacUsExclusiveCrosses = _CcacUsExclusiveCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 2, 1, 6),
    _CcacUsExclusiveCrosses_Type()
)
ccacUsExclusiveCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacUsExclusiveCrosses.setStatus("deprecated")
_CcacUsCountersDscTime_Type = TimeStamp
_CcacUsCountersDscTime_Object = MibTableColumn
ccacUsCountersDscTime = _CcacUsCountersDscTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 2, 1, 7),
    _CcacUsCountersDscTime_Type()
)
ccacUsCountersDscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacUsCountersDscTime.setStatus("deprecated")
_CcacDsTable_Object = MibTable
ccacDsTable = _CcacDsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ccacDsTable.setStatus("deprecated")
_CcacDsEntry_Object = MibTableRow
ccacDsEntry = _CcacDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 3, 1)
)
ccacDsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsTrafficType"),
)
if mibBuilder.loadTexts:
    ccacDsEntry.setStatus("deprecated")
_CcacDsTrafficType_Type = CcacDSTrafficMonitoredType
_CcacDsTrafficType_Object = MibTableColumn
ccacDsTrafficType = _CcacDsTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 3, 1, 1),
    _CcacDsTrafficType_Type()
)
ccacDsTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacDsTrafficType.setStatus("deprecated")
_CcacDsUtilization_Type = Percent
_CcacDsUtilization_Object = MibTableColumn
ccacDsUtilization = _CcacDsUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 3, 1, 2),
    _CcacDsUtilization_Type()
)
ccacDsUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacDsUtilization.setStatus("deprecated")
_CcacDsMinorCrosses_Type = Counter32
_CcacDsMinorCrosses_Object = MibTableColumn
ccacDsMinorCrosses = _CcacDsMinorCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 3, 1, 3),
    _CcacDsMinorCrosses_Type()
)
ccacDsMinorCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacDsMinorCrosses.setStatus("deprecated")
_CcacDsMajorCrosses_Type = Counter32
_CcacDsMajorCrosses_Object = MibTableColumn
ccacDsMajorCrosses = _CcacDsMajorCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 3, 1, 4),
    _CcacDsMajorCrosses_Type()
)
ccacDsMajorCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacDsMajorCrosses.setStatus("deprecated")
_CcacDsExclusiveCrosses_Type = Counter32
_CcacDsExclusiveCrosses_Object = MibTableColumn
ccacDsExclusiveCrosses = _CcacDsExclusiveCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 3, 1, 5),
    _CcacDsExclusiveCrosses_Type()
)
ccacDsExclusiveCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacDsExclusiveCrosses.setStatus("deprecated")
_CcacDsCountersDscTime_Type = TimeStamp
_CcacDsCountersDscTime_Object = MibTableColumn
ccacDsCountersDscTime = _CcacDsCountersDscTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 3, 1, 6),
    _CcacDsCountersDscTime_Type()
)
ccacDsCountersDscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacDsCountersDscTime.setStatus("deprecated")
_CcacUsRevTable_Object = MibTable
ccacUsRevTable = _CcacUsRevTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ccacUsRevTable.setStatus("current")
_CcacUsRevEntry_Object = MibTableRow
ccacUsRevEntry = _CcacUsRevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 4, 1)
)
ccacUsRevEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsRevAppBucketIndex"),
)
if mibBuilder.loadTexts:
    ccacUsRevEntry.setStatus("current")
_CcacUsRevAppBucketIndex_Type = CcacApplicationBucketType
_CcacUsRevAppBucketIndex_Object = MibTableColumn
ccacUsRevAppBucketIndex = _CcacUsRevAppBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 4, 1, 1),
    _CcacUsRevAppBucketIndex_Type()
)
ccacUsRevAppBucketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacUsRevAppBucketIndex.setStatus("current")
_CcacUsRevUtilization_Type = TenthPercent
_CcacUsRevUtilization_Object = MibTableColumn
ccacUsRevUtilization = _CcacUsRevUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 4, 1, 2),
    _CcacUsRevUtilization_Type()
)
ccacUsRevUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacUsRevUtilization.setStatus("current")
_CcacUsRevMinorCrosses_Type = Counter32
_CcacUsRevMinorCrosses_Object = MibTableColumn
ccacUsRevMinorCrosses = _CcacUsRevMinorCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 4, 1, 3),
    _CcacUsRevMinorCrosses_Type()
)
ccacUsRevMinorCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacUsRevMinorCrosses.setStatus("current")
_CcacUsRevMajorCrosses_Type = Counter32
_CcacUsRevMajorCrosses_Object = MibTableColumn
ccacUsRevMajorCrosses = _CcacUsRevMajorCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 4, 1, 4),
    _CcacUsRevMajorCrosses_Type()
)
ccacUsRevMajorCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacUsRevMajorCrosses.setStatus("current")
_CcacUsRevExclusiveCrosses_Type = Counter32
_CcacUsRevExclusiveCrosses_Object = MibTableColumn
ccacUsRevExclusiveCrosses = _CcacUsRevExclusiveCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 4, 1, 5),
    _CcacUsRevExclusiveCrosses_Type()
)
ccacUsRevExclusiveCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacUsRevExclusiveCrosses.setStatus("current")
_CcacUsRevCountersDscTime_Type = TimeStamp
_CcacUsRevCountersDscTime_Object = MibTableColumn
ccacUsRevCountersDscTime = _CcacUsRevCountersDscTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 4, 1, 6),
    _CcacUsRevCountersDscTime_Type()
)
ccacUsRevCountersDscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacUsRevCountersDscTime.setStatus("current")
_CcacDsRevTable_Object = MibTable
ccacDsRevTable = _CcacDsRevTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 5)
)
if mibBuilder.loadTexts:
    ccacDsRevTable.setStatus("current")
_CcacDsRevEntry_Object = MibTableRow
ccacDsRevEntry = _CcacDsRevEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 5, 1)
)
ccacDsRevEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsRevAppBucketIndex"),
)
if mibBuilder.loadTexts:
    ccacDsRevEntry.setStatus("current")
_CcacDsRevAppBucketIndex_Type = CcacApplicationBucketType
_CcacDsRevAppBucketIndex_Object = MibTableColumn
ccacDsRevAppBucketIndex = _CcacDsRevAppBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 5, 1, 1),
    _CcacDsRevAppBucketIndex_Type()
)
ccacDsRevAppBucketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacDsRevAppBucketIndex.setStatus("current")
_CcacDsRevUtilization_Type = TenthPercent
_CcacDsRevUtilization_Object = MibTableColumn
ccacDsRevUtilization = _CcacDsRevUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 5, 1, 2),
    _CcacDsRevUtilization_Type()
)
ccacDsRevUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacDsRevUtilization.setStatus("current")
_CcacDsRevMinorCrosses_Type = Counter32
_CcacDsRevMinorCrosses_Object = MibTableColumn
ccacDsRevMinorCrosses = _CcacDsRevMinorCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 5, 1, 3),
    _CcacDsRevMinorCrosses_Type()
)
ccacDsRevMinorCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacDsRevMinorCrosses.setStatus("current")
_CcacDsRevMajorCrosses_Type = Counter32
_CcacDsRevMajorCrosses_Object = MibTableColumn
ccacDsRevMajorCrosses = _CcacDsRevMajorCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 5, 1, 4),
    _CcacDsRevMajorCrosses_Type()
)
ccacDsRevMajorCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacDsRevMajorCrosses.setStatus("current")
_CcacDsRevExclusiveCrosses_Type = Counter32
_CcacDsRevExclusiveCrosses_Object = MibTableColumn
ccacDsRevExclusiveCrosses = _CcacDsRevExclusiveCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 5, 1, 5),
    _CcacDsRevExclusiveCrosses_Type()
)
ccacDsRevExclusiveCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacDsRevExclusiveCrosses.setStatus("current")
_CcacDsRevCountersDscTime_Type = TimeStamp
_CcacDsRevCountersDscTime_Object = MibTableColumn
ccacDsRevCountersDscTime = _CcacDsRevCountersDscTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 3, 5, 1, 6),
    _CcacDsRevCountersDscTime_Type()
)
ccacDsRevCountersDscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacDsRevCountersDscTime.setStatus("current")
_CcacEventHistory_ObjectIdentity = ObjectIdentity
ccacEventHistory = _CcacEventHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4)
)


class _CcacEventHistTableSize_Type(Unsigned32):
    """Custom type ccacEventHistTableSize based on Unsigned32"""
    defaultValue = 10


_CcacEventHistTableSize_Object = MibScalar
ccacEventHistTableSize = _CcacEventHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4, 1),
    _CcacEventHistTableSize_Type()
)
ccacEventHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccacEventHistTableSize.setStatus("current")
_CcacEventHistLastIndex_Type = Unsigned32
_CcacEventHistLastIndex_Object = MibScalar
ccacEventHistLastIndex = _CcacEventHistLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4, 2),
    _CcacEventHistLastIndex_Type()
)
ccacEventHistLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacEventHistLastIndex.setStatus("current")
_CcacEventHistoryTable_Object = MibTable
ccacEventHistoryTable = _CcacEventHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ccacEventHistoryTable.setStatus("current")
_CcacEventHistoryEntry_Object = MibTableRow
ccacEventHistoryEntry = _CcacEventHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4, 3, 1)
)
ccacEventHistoryEntry.setIndexNames(
    (0, "CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventHistoryIndex"),
)
if mibBuilder.loadTexts:
    ccacEventHistoryEntry.setStatus("current")
_CcacEventHistoryIndex_Type = Unsigned32
_CcacEventHistoryIndex_Object = MibTableColumn
ccacEventHistoryIndex = _CcacEventHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4, 3, 1, 1),
    _CcacEventHistoryIndex_Type()
)
ccacEventHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccacEventHistoryIndex.setStatus("current")
_CcacEventThreshObjectInstance_Type = VariablePointer
_CcacEventThreshObjectInstance_Object = MibTableColumn
ccacEventThreshObjectInstance = _CcacEventThreshObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4, 3, 1, 2),
    _CcacEventThreshObjectInstance_Type()
)
ccacEventThreshObjectInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacEventThreshObjectInstance.setStatus("current")
_CcacEventTypeChecked_Type = CcacMonitoredEvent
_CcacEventTypeChecked_Object = MibTableColumn
ccacEventTypeChecked = _CcacEventTypeChecked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4, 3, 1, 3),
    _CcacEventTypeChecked_Type()
)
ccacEventTypeChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacEventTypeChecked.setStatus("current")
_CcacEventResourceUtilization_Type = Unsigned32
_CcacEventResourceUtilization_Object = MibTableColumn
ccacEventResourceUtilization = _CcacEventResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4, 3, 1, 4),
    _CcacEventResourceUtilization_Type()
)
ccacEventResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacEventResourceUtilization.setStatus("current")
_CcacEventThreshCrosses_Type = Unsigned32
_CcacEventThreshCrosses_Object = MibTableColumn
ccacEventThreshCrosses = _CcacEventThreshCrosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4, 3, 1, 5),
    _CcacEventThreshCrosses_Type()
)
ccacEventThreshCrosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacEventThreshCrosses.setStatus("current")
_CcacEventTimeStamp_Type = TimeStamp
_CcacEventTimeStamp_Object = MibTableColumn
ccacEventTimeStamp = _CcacEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 1, 4, 3, 1, 6),
    _CcacEventTimeStamp_Type()
)
ccacEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccacEventTimeStamp.setStatus("current")
_CiscoCableAdmCtrlMIBConform_ObjectIdentity = ObjectIdentity
ciscoCableAdmCtrlMIBConform = _CiscoCableAdmCtrlMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2)
)
_CiscoCableAdmCtrlCompliances_ObjectIdentity = ObjectIdentity
ciscoCableAdmCtrlCompliances = _CiscoCableAdmCtrlCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2, 1)
)
_CiscoCableAdmCtrlMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCableAdmCtrlMIBGroups = _CiscoCableAdmCtrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2, 2)
)

# Managed Objects groups

ciscoCableAdmCtrlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2, 2, 1)
)
ciscoCableAdmCtrlConfigGroup.setObjects(
      *(("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacNotifyEnable"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventMonitoring"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscConfigStatus"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscConfigMinorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscConfigMajorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscConfigCritThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigStatus"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigMinorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigMajorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigExclusivePercent"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigNonExclusivePercent"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigStatus"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigMinorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigMajorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigExclusivePercent"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigNonExclusivePercent"))
)
if mibBuilder.loadTexts:
    ciscoCableAdmCtrlConfigGroup.setStatus("deprecated")

ciscoCableAdmCtrlStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2, 2, 2)
)
ciscoCableAdmCtrlStatGroup.setObjects(
      *(("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscUtilization"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscMinorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscMajorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscCountersDscTime"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscCriticalCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsUtilization"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsMinorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsMajorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsExclusiveCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsCountersDscTime"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsUtilization"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsMinorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsMajorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsExclusiveCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsCountersDscTime"))
)
if mibBuilder.loadTexts:
    ciscoCableAdmCtrlStatGroup.setStatus("deprecated")

ciscoCableAdmCtrlEventHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2, 2, 3)
)
ciscoCableAdmCtrlEventHistGroup.setObjects(
      *(("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventHistTableSize"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventHistLastIndex"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventThreshObjectInstance"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventTypeChecked"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventResourceUtilization"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventThreshCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoCableAdmCtrlEventHistGroup.setStatus("current")

ciscoCableAdmCtrlConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2, 2, 5)
)
ciscoCableAdmCtrlConfigGroupRev1.setObjects(
      *(("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacNotifyEnable"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventMonitoring"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscConfigStatus"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscConfigMinorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscConfigMajorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscConfigCritThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigRevAppBucketName"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigRevStatus"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigRevMinorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigRevMajorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigRevExclusivePercent"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigRevNonExclusivePercent"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsConfigRevStorageType"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigRevStatus"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigRevMinorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigRevMajorThreshold"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigRevExclusivePercent"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigRevNonExclusivePercent"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigRevAppBucketName"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsConfigRevStorageType"))
)
if mibBuilder.loadTexts:
    ciscoCableAdmCtrlConfigGroupRev1.setStatus("current")

ciscoCableAdmCtrlStatGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2, 2, 6)
)
ciscoCableAdmCtrlStatGroupRev1.setObjects(
      *(("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscUtilization"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscMinorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscMajorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscCountersDscTime"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacSysRscCriticalCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsRevUtilization"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsRevMinorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsRevMajorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsRevExclusiveCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacUsRevCountersDscTime"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsRevUtilization"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsRevMinorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsRevMajorCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsRevExclusiveCrosses"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacDsRevCountersDscTime"))
)
if mibBuilder.loadTexts:
    ciscoCableAdmCtrlStatGroupRev1.setStatus("current")


# Notification objects

ccacNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 0, 1)
)
ccacNotification.setObjects(
      *(("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventThreshObjectInstance"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventTypeChecked"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventResourceUtilization"),
        ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacEventThreshCrosses"))
)
if mibBuilder.loadTexts:
    ccacNotification.setStatus(
        "current"
    )


# Notifications groups

ciscoCableAdmCtrlNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2, 2, 4)
)
ciscoCableAdmCtrlNotifGroup.setObjects(
    ("CISCO-CABLE-ADMISSION-CTRL-MIB", "ccacNotification")
)
if mibBuilder.loadTexts:
    ciscoCableAdmCtrlNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCableAdmCtrlCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCableAdmCtrlCompliance.setStatus(
        "deprecated"
    )

ciscoCableAdmCtrlComplianceRev = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 450, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCableAdmCtrlComplianceRev.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-ADMISSION-CTRL-MIB",
    **{"Percent": Percent,
       "NonZeroPercent": NonZeroPercent,
       "TenthPercent": TenthPercent,
       "CcacSchedulingType": CcacSchedulingType,
       "CcacApplicationBucketType": CcacApplicationBucketType,
       "QoSServiceClassNameOrNull": QoSServiceClassNameOrNull,
       "CcacMonitoredEvent": CcacMonitoredEvent,
       "CcacSysRscMonitoredType": CcacSysRscMonitoredType,
       "CcacDSTrafficMonitoredType": CcacDSTrafficMonitoredType,
       "ciscoCableAdmCtrlMIB": ciscoCableAdmCtrlMIB,
       "ciscoCableAdmCtrlMIBNotifs": ciscoCableAdmCtrlMIBNotifs,
       "ccacNotification": ccacNotification,
       "ciscoCableAdmCtrlMIBObjects": ciscoCableAdmCtrlMIBObjects,
       "ccacObjects": ccacObjects,
       "ccacNotifyEnable": ccacNotifyEnable,
       "ccacEventMonitoring": ccacEventMonitoring,
       "ccacConfigObjects": ccacConfigObjects,
       "ccacSysRscConfigTable": ccacSysRscConfigTable,
       "ccacSysRscConfigEntry": ccacSysRscConfigEntry,
       "ccacSysRscConfigResourceType": ccacSysRscConfigResourceType,
       "ccacSysRscConfigStatus": ccacSysRscConfigStatus,
       "ccacSysRscConfigMinorThreshold": ccacSysRscConfigMinorThreshold,
       "ccacSysRscConfigMajorThreshold": ccacSysRscConfigMajorThreshold,
       "ccacSysRscConfigCritThreshold": ccacSysRscConfigCritThreshold,
       "ccacUsConfigTable": ccacUsConfigTable,
       "ccacUsConfigEntry": ccacUsConfigEntry,
       "ccacUsConfigIfIndex": ccacUsConfigIfIndex,
       "ccacUsConfigSchedType": ccacUsConfigSchedType,
       "ccacUsConfigServiceClassName": ccacUsConfigServiceClassName,
       "ccacUsConfigStatus": ccacUsConfigStatus,
       "ccacUsConfigMinorThreshold": ccacUsConfigMinorThreshold,
       "ccacUsConfigMajorThreshold": ccacUsConfigMajorThreshold,
       "ccacUsConfigExclusivePercent": ccacUsConfigExclusivePercent,
       "ccacUsConfigNonExclusivePercent": ccacUsConfigNonExclusivePercent,
       "ccacDsConfigTable": ccacDsConfigTable,
       "ccacDsConfigEntry": ccacDsConfigEntry,
       "ccacDsConfigIfIndex": ccacDsConfigIfIndex,
       "ccacDsConfigTrafficType": ccacDsConfigTrafficType,
       "ccacDsConfigStatus": ccacDsConfigStatus,
       "ccacDsConfigMinorThreshold": ccacDsConfigMinorThreshold,
       "ccacDsConfigMajorThreshold": ccacDsConfigMajorThreshold,
       "ccacDsConfigExclusivePercent": ccacDsConfigExclusivePercent,
       "ccacDsConfigNonExclusivePercent": ccacDsConfigNonExclusivePercent,
       "ccacUsConfigRevTable": ccacUsConfigRevTable,
       "ccacUsConfigRevEntry": ccacUsConfigRevEntry,
       "ccacUsConfigRevIfIndex": ccacUsConfigRevIfIndex,
       "ccacUsConfigRevAppBucketIndex": ccacUsConfigRevAppBucketIndex,
       "ccacUsConfigRevAppBucketName": ccacUsConfigRevAppBucketName,
       "ccacUsConfigRevMinorThreshold": ccacUsConfigRevMinorThreshold,
       "ccacUsConfigRevMajorThreshold": ccacUsConfigRevMajorThreshold,
       "ccacUsConfigRevExclusivePercent": ccacUsConfigRevExclusivePercent,
       "ccacUsConfigRevNonExclusivePercent": ccacUsConfigRevNonExclusivePercent,
       "ccacUsConfigRevStorageType": ccacUsConfigRevStorageType,
       "ccacUsConfigRevStatus": ccacUsConfigRevStatus,
       "ccacDsConfigRevTable": ccacDsConfigRevTable,
       "ccacDsConfigRevEntry": ccacDsConfigRevEntry,
       "ccacDsConfigRevIfIndex": ccacDsConfigRevIfIndex,
       "ccacDsConfigRevAppBucketIndex": ccacDsConfigRevAppBucketIndex,
       "ccacDsConfigRevAppBucketName": ccacDsConfigRevAppBucketName,
       "ccacDsConfigRevMinorThreshold": ccacDsConfigRevMinorThreshold,
       "ccacDsConfigRevMajorThreshold": ccacDsConfigRevMajorThreshold,
       "ccacDsConfigRevExclusivePercent": ccacDsConfigRevExclusivePercent,
       "ccacDsConfigRevNonExclusivePercent": ccacDsConfigRevNonExclusivePercent,
       "ccacDsConfigRevStorageType": ccacDsConfigRevStorageType,
       "ccacDsConfigRevStatus": ccacDsConfigRevStatus,
       "ccacStatObjects": ccacStatObjects,
       "ccacSysRscTable": ccacSysRscTable,
       "ccacSysRscEntry": ccacSysRscEntry,
       "ccacSysRscType": ccacSysRscType,
       "ccacSysRscUtilization": ccacSysRscUtilization,
       "ccacSysRscMinorCrosses": ccacSysRscMinorCrosses,
       "ccacSysRscMajorCrosses": ccacSysRscMajorCrosses,
       "ccacSysRscCriticalCrosses": ccacSysRscCriticalCrosses,
       "ccacSysRscCountersDscTime": ccacSysRscCountersDscTime,
       "ccacUsTable": ccacUsTable,
       "ccacUsEntry": ccacUsEntry,
       "ccacUsSchedType": ccacUsSchedType,
       "ccacUsServiceClassName": ccacUsServiceClassName,
       "ccacUsUtilization": ccacUsUtilization,
       "ccacUsMinorCrosses": ccacUsMinorCrosses,
       "ccacUsMajorCrosses": ccacUsMajorCrosses,
       "ccacUsExclusiveCrosses": ccacUsExclusiveCrosses,
       "ccacUsCountersDscTime": ccacUsCountersDscTime,
       "ccacDsTable": ccacDsTable,
       "ccacDsEntry": ccacDsEntry,
       "ccacDsTrafficType": ccacDsTrafficType,
       "ccacDsUtilization": ccacDsUtilization,
       "ccacDsMinorCrosses": ccacDsMinorCrosses,
       "ccacDsMajorCrosses": ccacDsMajorCrosses,
       "ccacDsExclusiveCrosses": ccacDsExclusiveCrosses,
       "ccacDsCountersDscTime": ccacDsCountersDscTime,
       "ccacUsRevTable": ccacUsRevTable,
       "ccacUsRevEntry": ccacUsRevEntry,
       "ccacUsRevAppBucketIndex": ccacUsRevAppBucketIndex,
       "ccacUsRevUtilization": ccacUsRevUtilization,
       "ccacUsRevMinorCrosses": ccacUsRevMinorCrosses,
       "ccacUsRevMajorCrosses": ccacUsRevMajorCrosses,
       "ccacUsRevExclusiveCrosses": ccacUsRevExclusiveCrosses,
       "ccacUsRevCountersDscTime": ccacUsRevCountersDscTime,
       "ccacDsRevTable": ccacDsRevTable,
       "ccacDsRevEntry": ccacDsRevEntry,
       "ccacDsRevAppBucketIndex": ccacDsRevAppBucketIndex,
       "ccacDsRevUtilization": ccacDsRevUtilization,
       "ccacDsRevMinorCrosses": ccacDsRevMinorCrosses,
       "ccacDsRevMajorCrosses": ccacDsRevMajorCrosses,
       "ccacDsRevExclusiveCrosses": ccacDsRevExclusiveCrosses,
       "ccacDsRevCountersDscTime": ccacDsRevCountersDscTime,
       "ccacEventHistory": ccacEventHistory,
       "ccacEventHistTableSize": ccacEventHistTableSize,
       "ccacEventHistLastIndex": ccacEventHistLastIndex,
       "ccacEventHistoryTable": ccacEventHistoryTable,
       "ccacEventHistoryEntry": ccacEventHistoryEntry,
       "ccacEventHistoryIndex": ccacEventHistoryIndex,
       "ccacEventThreshObjectInstance": ccacEventThreshObjectInstance,
       "ccacEventTypeChecked": ccacEventTypeChecked,
       "ccacEventResourceUtilization": ccacEventResourceUtilization,
       "ccacEventThreshCrosses": ccacEventThreshCrosses,
       "ccacEventTimeStamp": ccacEventTimeStamp,
       "ciscoCableAdmCtrlMIBConform": ciscoCableAdmCtrlMIBConform,
       "ciscoCableAdmCtrlCompliances": ciscoCableAdmCtrlCompliances,
       "ciscoCableAdmCtrlCompliance": ciscoCableAdmCtrlCompliance,
       "ciscoCableAdmCtrlComplianceRev": ciscoCableAdmCtrlComplianceRev,
       "ciscoCableAdmCtrlMIBGroups": ciscoCableAdmCtrlMIBGroups,
       "ciscoCableAdmCtrlConfigGroup": ciscoCableAdmCtrlConfigGroup,
       "ciscoCableAdmCtrlStatGroup": ciscoCableAdmCtrlStatGroup,
       "ciscoCableAdmCtrlEventHistGroup": ciscoCableAdmCtrlEventHistGroup,
       "ciscoCableAdmCtrlNotifGroup": ciscoCableAdmCtrlNotifGroup,
       "ciscoCableAdmCtrlConfigGroupRev1": ciscoCableAdmCtrlConfigGroupRev1,
       "ciscoCableAdmCtrlStatGroupRev1": ciscoCableAdmCtrlStatGroupRev1}
)
