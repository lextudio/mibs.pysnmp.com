# SNMP MIB module (CISCO-VDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VDC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:37 2024
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

(Cisco2KVlanList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Cisco2KVlanList")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVdcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 774)
)
ciscoVdcMIB.setRevisions(
        ("2016-11-03 00:00",
         "2016-01-19 00:00",
         "2013-09-24 00:00",
         "2013-07-02 00:00",
         "2013-06-08 00:00",
         "2011-05-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoVdcHaPolicy(Integer32, TextualConvention):
    status = "current"
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
        *(("bringDown", 2),
          ("reload", 0),
          ("restart", 1),
          ("switchOver", 3))
    )



class CiscoVdcPercentOrMinusOne(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVdcMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVdcMIBNotifs = _CiscoVdcMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 0)
)
_CiscoVdcMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVdcMIBObjects = _CiscoVdcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1)
)
_CiscoVdcTable_Object = MibTable
ciscoVdcTable = _CiscoVdcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVdcTable.setStatus("current")
_CiscoVdcEntry_Object = MibTableRow
ciscoVdcEntry = _CiscoVdcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 1, 1)
)
ciscoVdcEntry.setIndexNames(
    (0, "CISCO-VDC-MIB", "ciscoVdcId"),
)
if mibBuilder.loadTexts:
    ciscoVdcEntry.setStatus("current")


class _CiscoVdcId_Type(Unsigned32):
    """Custom type ciscoVdcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_CiscoVdcId_Type.__name__ = "Unsigned32"
_CiscoVdcId_Object = MibTableColumn
ciscoVdcId = _CiscoVdcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 1, 1, 1),
    _CiscoVdcId_Type()
)
ciscoVdcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoVdcId.setStatus("current")


class _CiscoVdcName_Type(SnmpAdminString):
    """Custom type ciscoVdcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CiscoVdcName_Type.__name__ = "SnmpAdminString"
_CiscoVdcName_Object = MibTableColumn
ciscoVdcName = _CiscoVdcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 1, 1, 2),
    _CiscoVdcName_Type()
)
ciscoVdcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcName.setStatus("current")


class _CiscoVdcState_Type(Integer32):
    """Custom type ciscoVdcState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("configured", 4),
          ("creating", 5),
          ("deleting", 6),
          ("failed", 7),
          ("failing", 13),
          ("nonconfigured", 3),
          ("pending", 8),
          ("restarting", 10),
          ("resuming", 12),
          ("suspended", 2),
          ("suspending", 11),
          ("updating", 9))
    )


_CiscoVdcState_Type.__name__ = "Integer32"
_CiscoVdcState_Object = MibTableColumn
ciscoVdcState = _CiscoVdcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 1, 1, 3),
    _CiscoVdcState_Type()
)
ciscoVdcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcState.setStatus("current")


class _CiscoVdcFcoeCapable_Type(Integer32):
    """Custom type ciscoVdcFcoeCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 2),
          ("disallowed", 1),
          ("installed", 3))
    )


_CiscoVdcFcoeCapable_Type.__name__ = "Integer32"
_CiscoVdcFcoeCapable_Object = MibTableColumn
ciscoVdcFcoeCapable = _CiscoVdcFcoeCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 1, 1, 4),
    _CiscoVdcFcoeCapable_Type()
)
ciscoVdcFcoeCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcFcoeCapable.setStatus("current")
_CiscoVdcMac_Type = MacAddress
_CiscoVdcMac_Object = MibTableColumn
ciscoVdcMac = _CiscoVdcMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 1, 1, 5),
    _CiscoVdcMac_Type()
)
ciscoVdcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcMac.setStatus("current")
_CiscoVdcSwitchId_Type = MacAddress
_CiscoVdcSwitchId_Object = MibTableColumn
ciscoVdcSwitchId = _CiscoVdcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 1, 1, 6),
    _CiscoVdcSwitchId_Type()
)
ciscoVdcSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcSwitchId.setStatus("current")
_CiscoVdcRowStatus_Type = RowStatus
_CiscoVdcRowStatus_Object = MibTableColumn
ciscoVdcRowStatus = _CiscoVdcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 1, 1, 7),
    _CiscoVdcRowStatus_Type()
)
ciscoVdcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcRowStatus.setStatus("current")
_CiscoVdcStorageType_Type = StorageType
_CiscoVdcStorageType_Object = MibTableColumn
ciscoVdcStorageType = _CiscoVdcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 1, 1, 8),
    _CiscoVdcStorageType_Type()
)
ciscoVdcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcStorageType.setStatus("current")
_CiscoVdcGlobal_ObjectIdentity = ObjectIdentity
ciscoVdcGlobal = _CiscoVdcGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 2)
)
_CiscoVdcMaxNumberVdcAllowed_Type = Integer32
_CiscoVdcMaxNumberVdcAllowed_Object = MibScalar
ciscoVdcMaxNumberVdcAllowed = _CiscoVdcMaxNumberVdcAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 2, 1),
    _CiscoVdcMaxNumberVdcAllowed_Type()
)
ciscoVdcMaxNumberVdcAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcMaxNumberVdcAllowed.setStatus("current")
_CiscoVdcCombinedHostnameEnabled_Type = TruthValue
_CiscoVdcCombinedHostnameEnabled_Object = MibScalar
ciscoVdcCombinedHostnameEnabled = _CiscoVdcCombinedHostnameEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 2, 2),
    _CiscoVdcCombinedHostnameEnabled_Type()
)
ciscoVdcCombinedHostnameEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcCombinedHostnameEnabled.setStatus("current")
_CiscoVdcExt_ObjectIdentity = ObjectIdentity
ciscoVdcExt = _CiscoVdcExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3)
)
_CiscoVdcExtTable_Object = MibTable
ciscoVdcExtTable = _CiscoVdcExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoVdcExtTable.setStatus("current")
_CiscoVdcExtEntry_Object = MibTableRow
ciscoVdcExtEntry = _CiscoVdcExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1)
)
ciscoVdcExtEntry.setIndexNames(
    (0, "CISCO-VDC-MIB", "ciscoVdcId"),
)
if mibBuilder.loadTexts:
    ciscoVdcExtEntry.setStatus("current")


class _CiscoVdcSingleSupHaPolicy_Type(CiscoVdcHaPolicy):
    """Custom type ciscoVdcSingleSupHaPolicy based on CiscoVdcHaPolicy"""


_CiscoVdcSingleSupHaPolicy_Object = MibTableColumn
ciscoVdcSingleSupHaPolicy = _CiscoVdcSingleSupHaPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 1),
    _CiscoVdcSingleSupHaPolicy_Type()
)
ciscoVdcSingleSupHaPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcSingleSupHaPolicy.setStatus("current")


class _CiscoVdcDualSupHaPolicy_Type(CiscoVdcHaPolicy):
    """Custom type ciscoVdcDualSupHaPolicy based on CiscoVdcHaPolicy"""


_CiscoVdcDualSupHaPolicy_Object = MibTableColumn
ciscoVdcDualSupHaPolicy = _CiscoVdcDualSupHaPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 2),
    _CiscoVdcDualSupHaPolicy_Type()
)
ciscoVdcDualSupHaPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcDualSupHaPolicy.setStatus("current")
_CiscoVdcBootOrder_Type = Unsigned32
_CiscoVdcBootOrder_Object = MibTableColumn
ciscoVdcBootOrder = _CiscoVdcBootOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 3),
    _CiscoVdcBootOrder_Type()
)
ciscoVdcBootOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcBootOrder.setStatus("current")
_CiscoVdcTimeCreated_Type = DateAndTime
_CiscoVdcTimeCreated_Object = MibTableColumn
ciscoVdcTimeCreated = _CiscoVdcTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 4),
    _CiscoVdcTimeCreated_Type()
)
ciscoVdcTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcTimeCreated.setStatus("current")
_CiscoVdcReloadCount_Type = Gauge32
_CiscoVdcReloadCount_Object = MibTableColumn
ciscoVdcReloadCount = _CiscoVdcReloadCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 5),
    _CiscoVdcReloadCount_Type()
)
ciscoVdcReloadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcReloadCount.setStatus("current")
_CiscoVdcRestartCount_Type = Gauge32
_CiscoVdcRestartCount_Object = MibTableColumn
ciscoVdcRestartCount = _CiscoVdcRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 6),
    _CiscoVdcRestartCount_Type()
)
ciscoVdcRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcRestartCount.setStatus("current")
_CiscoVdcRestartTime_Type = DateAndTime
_CiscoVdcRestartTime_Object = MibTableColumn
ciscoVdcRestartTime = _CiscoVdcRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 7),
    _CiscoVdcRestartTime_Type()
)
ciscoVdcRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcRestartTime.setStatus("current")
_CiscoVdcRestartReason_Type = SnmpAdminString
_CiscoVdcRestartReason_Object = MibTableColumn
ciscoVdcRestartReason = _CiscoVdcRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 8),
    _CiscoVdcRestartReason_Type()
)
ciscoVdcRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcRestartReason.setStatus("current")


class _CiscoVdcType_Type(Integer32):
    """Custom type ciscoVdcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("ethernet", 2),
          ("storage", 3))
    )


_CiscoVdcType_Type.__name__ = "Integer32"
_CiscoVdcType_Object = MibTableColumn
ciscoVdcType = _CiscoVdcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 9),
    _CiscoVdcType_Type()
)
ciscoVdcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcType.setStatus("current")


class _CiscoVdcAdminStatus_Type(Integer32):
    """Custom type ciscoVdcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("suspended", 2))
    )


_CiscoVdcAdminStatus_Type.__name__ = "Integer32"
_CiscoVdcAdminStatus_Object = MibTableColumn
ciscoVdcAdminStatus = _CiscoVdcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 10),
    _CiscoVdcAdminStatus_Type()
)
ciscoVdcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcAdminStatus.setStatus("current")


class _CiscoVdcFromUnallocatedIntf_Type(Integer32):
    """Custom type ciscoVdcFromUnallocatedIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allocate", 2),
          ("noOp", 1))
    )


_CiscoVdcFromUnallocatedIntf_Type.__name__ = "Integer32"
_CiscoVdcFromUnallocatedIntf_Object = MibTableColumn
ciscoVdcFromUnallocatedIntf = _CiscoVdcFromUnallocatedIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 11),
    _CiscoVdcFromUnallocatedIntf_Type()
)
ciscoVdcFromUnallocatedIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcFromUnallocatedIntf.setStatus("current")


class _CiscoVdcFeatureSetList_Type(Bits):
    """Custom type ciscoVdcFeatureSetList based on Bits"""
    namedValues = NamedValues(
        *(("ethernet", 4),
          ("fabric", 6),
          ("fabricPath", 1),
          ("fcoe", 0),
          ("fcoeNpv", 7),
          ("fex", 2),
          ("mpls", 3),
          ("virtualization", 5))
    )

_CiscoVdcFeatureSetList_Type.__name__ = "Bits"
_CiscoVdcFeatureSetList_Object = MibTableColumn
ciscoVdcFeatureSetList = _CiscoVdcFeatureSetList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 12),
    _CiscoVdcFeatureSetList_Type()
)
ciscoVdcFeatureSetList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcFeatureSetList.setStatus("current")
_CiscoVdcResourceTemplate_Type = SnmpAdminString
_CiscoVdcResourceTemplate_Object = MibTableColumn
ciscoVdcResourceTemplate = _CiscoVdcResourceTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 13),
    _CiscoVdcResourceTemplate_Type()
)
ciscoVdcResourceTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcResourceTemplate.setStatus("current")


class _CiscoVdcModuleCapList_Type(Bits):
    """Custom type ciscoVdcModuleCapList based on Bits"""
    namedValues = NamedValues(
        *(("f1", 1),
          ("f2", 3),
          ("f2e", 6),
          ("f3", 7),
          ("fc", 5),
          ("m1", 0),
          ("m1xl", 2),
          ("m2xl", 4),
          ("m3", 8))
    )

_CiscoVdcModuleCapList_Type.__name__ = "Bits"
_CiscoVdcModuleCapList_Object = MibTableColumn
ciscoVdcModuleCapList = _CiscoVdcModuleCapList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 14),
    _CiscoVdcModuleCapList_Type()
)
ciscoVdcModuleCapList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcModuleCapList.setStatus("current")


class _CiscoVdcCpuPriority_Type(Integer32):
    """Custom type ciscoVdcCpuPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CiscoVdcCpuPriority_Type.__name__ = "Integer32"
_CiscoVdcCpuPriority_Object = MibTableColumn
ciscoVdcCpuPriority = _CiscoVdcCpuPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 15),
    _CiscoVdcCpuPriority_Type()
)
ciscoVdcCpuPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcCpuPriority.setStatus("current")
_CiscoVdcCpuSharePercent_Type = CiscoVdcPercentOrMinusOne
_CiscoVdcCpuSharePercent_Object = MibTableColumn
ciscoVdcCpuSharePercent = _CiscoVdcCpuSharePercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 3, 1, 1, 16),
    _CiscoVdcCpuSharePercent_Type()
)
ciscoVdcCpuSharePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcCpuSharePercent.setStatus("current")
_CiscoVdcResource_ObjectIdentity = ObjectIdentity
ciscoVdcResource = _CiscoVdcResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4)
)
_CiscoVdcGlobalResUsageTable_Object = MibTable
ciscoVdcGlobalResUsageTable = _CiscoVdcGlobalResUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ciscoVdcGlobalResUsageTable.setStatus("current")
_CiscoVdcGlobalResUsageEntry_Object = MibTableRow
ciscoVdcGlobalResUsageEntry = _CiscoVdcGlobalResUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 1, 1)
)
ciscoVdcGlobalResUsageEntry.setIndexNames(
    (0, "CISCO-VDC-MIB", "ciscoVdcGlobalResID"),
)
if mibBuilder.loadTexts:
    ciscoVdcGlobalResUsageEntry.setStatus("current")
_CiscoVdcGlobalResID_Type = Unsigned32
_CiscoVdcGlobalResID_Object = MibTableColumn
ciscoVdcGlobalResID = _CiscoVdcGlobalResID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 1, 1, 1),
    _CiscoVdcGlobalResID_Type()
)
ciscoVdcGlobalResID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoVdcGlobalResID.setStatus("current")
_CiscoVdcGlobalResName_Type = SnmpAdminString
_CiscoVdcGlobalResName_Object = MibTableColumn
ciscoVdcGlobalResName = _CiscoVdcGlobalResName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 1, 1, 2),
    _CiscoVdcGlobalResName_Type()
)
ciscoVdcGlobalResName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcGlobalResName.setStatus("current")
_CiscoVdcGlobalResUsed_Type = Unsigned32
_CiscoVdcGlobalResUsed_Object = MibTableColumn
ciscoVdcGlobalResUsed = _CiscoVdcGlobalResUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 1, 1, 3),
    _CiscoVdcGlobalResUsed_Type()
)
ciscoVdcGlobalResUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcGlobalResUsed.setStatus("current")
_CiscoVdcGlobalResUnused_Type = Unsigned32
_CiscoVdcGlobalResUnused_Object = MibTableColumn
ciscoVdcGlobalResUnused = _CiscoVdcGlobalResUnused_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 1, 1, 4),
    _CiscoVdcGlobalResUnused_Type()
)
ciscoVdcGlobalResUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcGlobalResUnused.setStatus("current")
_CiscoVdcGlobalResFree_Type = Unsigned32
_CiscoVdcGlobalResFree_Object = MibTableColumn
ciscoVdcGlobalResFree = _CiscoVdcGlobalResFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 1, 1, 5),
    _CiscoVdcGlobalResFree_Type()
)
ciscoVdcGlobalResFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcGlobalResFree.setStatus("current")
_CiscoVdcGlobalResAvail_Type = Unsigned32
_CiscoVdcGlobalResAvail_Object = MibTableColumn
ciscoVdcGlobalResAvail = _CiscoVdcGlobalResAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 1, 1, 6),
    _CiscoVdcGlobalResAvail_Type()
)
ciscoVdcGlobalResAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcGlobalResAvail.setStatus("current")
_CiscoVdcGlobalResTotal_Type = Unsigned32
_CiscoVdcGlobalResTotal_Object = MibTableColumn
ciscoVdcGlobalResTotal = _CiscoVdcGlobalResTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 1, 1, 7),
    _CiscoVdcGlobalResTotal_Type()
)
ciscoVdcGlobalResTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcGlobalResTotal.setStatus("current")
_CiscoVdcResUsageTable_Object = MibTable
ciscoVdcResUsageTable = _CiscoVdcResUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ciscoVdcResUsageTable.setStatus("current")
_CiscoVdcResUsageEntry_Object = MibTableRow
ciscoVdcResUsageEntry = _CiscoVdcResUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 2, 1)
)
ciscoVdcResUsageEntry.setIndexNames(
    (0, "CISCO-VDC-MIB", "ciscoVdcId"),
    (0, "CISCO-VDC-MIB", "ciscoVdcResID"),
)
if mibBuilder.loadTexts:
    ciscoVdcResUsageEntry.setStatus("current")
_CiscoVdcResID_Type = Unsigned32
_CiscoVdcResID_Object = MibTableColumn
ciscoVdcResID = _CiscoVdcResID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 2, 1, 1),
    _CiscoVdcResID_Type()
)
ciscoVdcResID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoVdcResID.setStatus("current")
_CiscoVdcResMin_Type = Unsigned32
_CiscoVdcResMin_Object = MibTableColumn
ciscoVdcResMin = _CiscoVdcResMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 2, 1, 2),
    _CiscoVdcResMin_Type()
)
ciscoVdcResMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcResMin.setStatus("current")
_CiscoVdcResMax_Type = Unsigned32
_CiscoVdcResMax_Object = MibTableColumn
ciscoVdcResMax = _CiscoVdcResMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 2, 1, 3),
    _CiscoVdcResMax_Type()
)
ciscoVdcResMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcResMax.setStatus("current")
_CiscoVdcResUsed_Type = Unsigned32
_CiscoVdcResUsed_Object = MibTableColumn
ciscoVdcResUsed = _CiscoVdcResUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 2, 1, 4),
    _CiscoVdcResUsed_Type()
)
ciscoVdcResUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcResUsed.setStatus("current")
_CiscoVdcResUnused_Type = Unsigned32
_CiscoVdcResUnused_Object = MibTableColumn
ciscoVdcResUnused = _CiscoVdcResUnused_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 2, 1, 5),
    _CiscoVdcResUnused_Type()
)
ciscoVdcResUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcResUnused.setStatus("current")
_CiscoVdcResAvail_Type = Unsigned32
_CiscoVdcResAvail_Object = MibTableColumn
ciscoVdcResAvail = _CiscoVdcResAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 2, 1, 6),
    _CiscoVdcResAvail_Type()
)
ciscoVdcResAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdcResAvail.setStatus("current")
_CiscoVdcResTemplateTable_Object = MibTable
ciscoVdcResTemplateTable = _CiscoVdcResTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ciscoVdcResTemplateTable.setStatus("current")
_CiscoVdcResTemplateEntry_Object = MibTableRow
ciscoVdcResTemplateEntry = _CiscoVdcResTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 3, 1)
)
ciscoVdcResTemplateEntry.setIndexNames(
    (0, "CISCO-VDC-MIB", "ciscoVdcResTemplateName"),
    (0, "CISCO-VDC-MIB", "ciscoVdcResTemplateResID"),
)
if mibBuilder.loadTexts:
    ciscoVdcResTemplateEntry.setStatus("current")
_CiscoVdcResTemplateName_Type = SnmpAdminString
_CiscoVdcResTemplateName_Object = MibTableColumn
ciscoVdcResTemplateName = _CiscoVdcResTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 3, 1, 1),
    _CiscoVdcResTemplateName_Type()
)
ciscoVdcResTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoVdcResTemplateName.setStatus("current")
_CiscoVdcResTemplateResID_Type = Unsigned32
_CiscoVdcResTemplateResID_Object = MibTableColumn
ciscoVdcResTemplateResID = _CiscoVdcResTemplateResID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 3, 1, 2),
    _CiscoVdcResTemplateResID_Type()
)
ciscoVdcResTemplateResID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoVdcResTemplateResID.setStatus("current")
_CiscoVdcResTemplateMin_Type = Unsigned32
_CiscoVdcResTemplateMin_Object = MibTableColumn
ciscoVdcResTemplateMin = _CiscoVdcResTemplateMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 3, 1, 3),
    _CiscoVdcResTemplateMin_Type()
)
ciscoVdcResTemplateMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoVdcResTemplateMin.setStatus("current")
_CiscoVdcResTemplateMax_Type = Unsigned32
_CiscoVdcResTemplateMax_Object = MibTableColumn
ciscoVdcResTemplateMax = _CiscoVdcResTemplateMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 3, 1, 4),
    _CiscoVdcResTemplateMax_Type()
)
ciscoVdcResTemplateMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoVdcResTemplateMax.setStatus("current")


class _CiscoVdcResTemplateStorageType_Type(StorageType):
    """Custom type ciscoVdcResTemplateStorageType based on StorageType"""


_CiscoVdcResTemplateStorageType_Object = MibTableColumn
ciscoVdcResTemplateStorageType = _CiscoVdcResTemplateStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 3, 1, 5),
    _CiscoVdcResTemplateStorageType_Type()
)
ciscoVdcResTemplateStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoVdcResTemplateStorageType.setStatus("current")
_CiscoVdcResTemplateStatus_Type = RowStatus
_CiscoVdcResTemplateStatus_Object = MibTableColumn
ciscoVdcResTemplateStatus = _CiscoVdcResTemplateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 4, 3, 1, 6),
    _CiscoVdcResTemplateStatus_Type()
)
ciscoVdcResTemplateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoVdcResTemplateStatus.setStatus("current")
_CiscoVdcInterface_ObjectIdentity = ObjectIdentity
ciscoVdcInterface = _CiscoVdcInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5)
)
_CiscoVdcIfMembershipTable_Object = MibTable
ciscoVdcIfMembershipTable = _CiscoVdcIfMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ciscoVdcIfMembershipTable.setStatus("current")
_CiscoVdcIfMembershipEntry_Object = MibTableRow
ciscoVdcIfMembershipEntry = _CiscoVdcIfMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 1, 1)
)
ciscoVdcIfMembershipEntry.setIndexNames(
    (0, "CISCO-VDC-MIB", "ciscoVdcId"),
    (0, "CISCO-VDC-MIB", "ciscoVdcIfMembershipifIndex"),
)
if mibBuilder.loadTexts:
    ciscoVdcIfMembershipEntry.setStatus("current")
_CiscoVdcIfMembershipifIndex_Type = InterfaceIndex
_CiscoVdcIfMembershipifIndex_Object = MibTableColumn
ciscoVdcIfMembershipifIndex = _CiscoVdcIfMembershipifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 1, 1, 1),
    _CiscoVdcIfMembershipifIndex_Type()
)
ciscoVdcIfMembershipifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoVdcIfMembershipifIndex.setStatus("current")


class _CiscoVdcIfMembershipStorageType_Type(StorageType):
    """Custom type ciscoVdcIfMembershipStorageType based on StorageType"""


_CiscoVdcIfMembershipStorageType_Object = MibTableColumn
ciscoVdcIfMembershipStorageType = _CiscoVdcIfMembershipStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 1, 1, 2),
    _CiscoVdcIfMembershipStorageType_Type()
)
ciscoVdcIfMembershipStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoVdcIfMembershipStorageType.setStatus("current")
_CiscoVdcIfMembershipStatus_Type = RowStatus
_CiscoVdcIfMembershipStatus_Object = MibTableColumn
ciscoVdcIfMembershipStatus = _CiscoVdcIfMembershipStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 1, 1, 3),
    _CiscoVdcIfMembershipStatus_Type()
)
ciscoVdcIfMembershipStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoVdcIfMembershipStatus.setStatus("current")
_CiscoVdcFCoEVlansTable_Object = MibTable
ciscoVdcFCoEVlansTable = _CiscoVdcFCoEVlansTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ciscoVdcFCoEVlansTable.setStatus("current")
_CiscoVdcFCoEVlansEntry_Object = MibTableRow
ciscoVdcFCoEVlansEntry = _CiscoVdcFCoEVlansEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 2, 1)
)
ciscoVdcFCoEVlansEntry.setIndexNames(
    (0, "CISCO-VDC-MIB", "ciscoVdcId"),
)
if mibBuilder.loadTexts:
    ciscoVdcFCoEVlansEntry.setStatus("current")
_CiscoVdcFCoEVlansFirst2K_Type = Cisco2KVlanList
_CiscoVdcFCoEVlansFirst2K_Object = MibTableColumn
ciscoVdcFCoEVlansFirst2K = _CiscoVdcFCoEVlansFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 2, 1, 1),
    _CiscoVdcFCoEVlansFirst2K_Type()
)
ciscoVdcFCoEVlansFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcFCoEVlansFirst2K.setStatus("current")
_CiscoVdcFCoEVlansSecond2K_Type = Cisco2KVlanList
_CiscoVdcFCoEVlansSecond2K_Object = MibTableColumn
ciscoVdcFCoEVlansSecond2K = _CiscoVdcFCoEVlansSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 2, 1, 2),
    _CiscoVdcFCoEVlansSecond2K_Type()
)
ciscoVdcFCoEVlansSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcFCoEVlansSecond2K.setStatus("current")
_CiscoVdcFCoEVlansFromVdc_Type = Unsigned32
_CiscoVdcFCoEVlansFromVdc_Object = MibTableColumn
ciscoVdcFCoEVlansFromVdc = _CiscoVdcFCoEVlansFromVdc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 2, 1, 3),
    _CiscoVdcFCoEVlansFromVdc_Type()
)
ciscoVdcFCoEVlansFromVdc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdcFCoEVlansFromVdc.setStatus("current")
_CiscoVdcSharedInterfaceTable_Object = MibTable
ciscoVdcSharedInterfaceTable = _CiscoVdcSharedInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ciscoVdcSharedInterfaceTable.setStatus("current")
_CiscoVdcSharedInterfaceEntry_Object = MibTableRow
ciscoVdcSharedInterfaceEntry = _CiscoVdcSharedInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 3, 1)
)
ciscoVdcSharedInterfaceEntry.setIndexNames(
    (0, "CISCO-VDC-MIB", "ciscoVdcId"),
    (0, "CISCO-VDC-MIB", "ciscoVdcSharedInterfaceifIndex"),
)
if mibBuilder.loadTexts:
    ciscoVdcSharedInterfaceEntry.setStatus("current")
_CiscoVdcSharedInterfaceifIndex_Type = InterfaceIndex
_CiscoVdcSharedInterfaceifIndex_Object = MibTableColumn
ciscoVdcSharedInterfaceifIndex = _CiscoVdcSharedInterfaceifIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 3, 1, 1),
    _CiscoVdcSharedInterfaceifIndex_Type()
)
ciscoVdcSharedInterfaceifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoVdcSharedInterfaceifIndex.setStatus("current")


class _CiscoVdcSharedInterfaceStorageType_Type(StorageType):
    """Custom type ciscoVdcSharedInterfaceStorageType based on StorageType"""


_CiscoVdcSharedInterfaceStorageType_Object = MibTableColumn
ciscoVdcSharedInterfaceStorageType = _CiscoVdcSharedInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 3, 1, 2),
    _CiscoVdcSharedInterfaceStorageType_Type()
)
ciscoVdcSharedInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoVdcSharedInterfaceStorageType.setStatus("current")
_CiscoVdcSharedInterfaceRowStatus_Type = RowStatus
_CiscoVdcSharedInterfaceRowStatus_Object = MibTableColumn
ciscoVdcSharedInterfaceRowStatus = _CiscoVdcSharedInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 1, 5, 3, 1, 3),
    _CiscoVdcSharedInterfaceRowStatus_Type()
)
ciscoVdcSharedInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoVdcSharedInterfaceRowStatus.setStatus("current")
_CiscoVdcMIBConform_ObjectIdentity = ObjectIdentity
ciscoVdcMIBConform = _CiscoVdcMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2)
)
_CiscoVdcMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVdcMIBCompliances = _CiscoVdcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 1)
)
_CiscoVdcMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVdcMIBGroups = _CiscoVdcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 2)
)

# Managed Objects groups

ciscoVdcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 2, 1)
)
ciscoVdcGroup.setObjects(
      *(("CISCO-VDC-MIB", "ciscoVdcName"),
        ("CISCO-VDC-MIB", "ciscoVdcState"),
        ("CISCO-VDC-MIB", "ciscoVdcFcoeCapable"),
        ("CISCO-VDC-MIB", "ciscoVdcMac"),
        ("CISCO-VDC-MIB", "ciscoVdcSwitchId"),
        ("CISCO-VDC-MIB", "ciscoVdcRowStatus"),
        ("CISCO-VDC-MIB", "ciscoVdcStorageType"))
)
if mibBuilder.loadTexts:
    ciscoVdcGroup.setStatus("current")

ciscoVdcExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 2, 2)
)
ciscoVdcExtGroup.setObjects(
      *(("CISCO-VDC-MIB", "ciscoVdcSingleSupHaPolicy"),
        ("CISCO-VDC-MIB", "ciscoVdcDualSupHaPolicy"),
        ("CISCO-VDC-MIB", "ciscoVdcBootOrder"),
        ("CISCO-VDC-MIB", "ciscoVdcTimeCreated"),
        ("CISCO-VDC-MIB", "ciscoVdcReloadCount"),
        ("CISCO-VDC-MIB", "ciscoVdcRestartCount"),
        ("CISCO-VDC-MIB", "ciscoVdcRestartTime"),
        ("CISCO-VDC-MIB", "ciscoVdcRestartReason"),
        ("CISCO-VDC-MIB", "ciscoVdcType"),
        ("CISCO-VDC-MIB", "ciscoVdcAdminStatus"),
        ("CISCO-VDC-MIB", "ciscoVdcFromUnallocatedIntf"),
        ("CISCO-VDC-MIB", "ciscoVdcFeatureSetList"),
        ("CISCO-VDC-MIB", "ciscoVdcResourceTemplate"),
        ("CISCO-VDC-MIB", "ciscoVdcModuleCapList"),
        ("CISCO-VDC-MIB", "ciscoVdcCpuPriority"),
        ("CISCO-VDC-MIB", "ciscoVdcCpuSharePercent"))
)
if mibBuilder.loadTexts:
    ciscoVdcExtGroup.setStatus("current")

ciscoVdcGlobalResUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 2, 3)
)
ciscoVdcGlobalResUsageGroup.setObjects(
      *(("CISCO-VDC-MIB", "ciscoVdcGlobalResName"),
        ("CISCO-VDC-MIB", "ciscoVdcGlobalResUsed"),
        ("CISCO-VDC-MIB", "ciscoVdcGlobalResUnused"),
        ("CISCO-VDC-MIB", "ciscoVdcGlobalResFree"),
        ("CISCO-VDC-MIB", "ciscoVdcGlobalResAvail"),
        ("CISCO-VDC-MIB", "ciscoVdcGlobalResTotal"))
)
if mibBuilder.loadTexts:
    ciscoVdcGlobalResUsageGroup.setStatus("current")

ciscoVdcResUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 2, 4)
)
ciscoVdcResUsageGroup.setObjects(
      *(("CISCO-VDC-MIB", "ciscoVdcResMin"),
        ("CISCO-VDC-MIB", "ciscoVdcResMax"),
        ("CISCO-VDC-MIB", "ciscoVdcResUsed"),
        ("CISCO-VDC-MIB", "ciscoVdcResUnused"),
        ("CISCO-VDC-MIB", "ciscoVdcResAvail"))
)
if mibBuilder.loadTexts:
    ciscoVdcResUsageGroup.setStatus("current")

ciscoVdcResTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 2, 5)
)
ciscoVdcResTemplateGroup.setObjects(
      *(("CISCO-VDC-MIB", "ciscoVdcResTemplateMin"),
        ("CISCO-VDC-MIB", "ciscoVdcResTemplateMax"),
        ("CISCO-VDC-MIB", "ciscoVdcResTemplateStatus"),
        ("CISCO-VDC-MIB", "ciscoVdcResTemplateStorageType"))
)
if mibBuilder.loadTexts:
    ciscoVdcResTemplateGroup.setStatus("current")

ciscoVdcGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 2, 6)
)
ciscoVdcGlobalGroup.setObjects(
      *(("CISCO-VDC-MIB", "ciscoVdcMaxNumberVdcAllowed"),
        ("CISCO-VDC-MIB", "ciscoVdcCombinedHostnameEnabled"))
)
if mibBuilder.loadTexts:
    ciscoVdcGlobalGroup.setStatus("current")

ciscoVdcIfMembershipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 2, 7)
)
ciscoVdcIfMembershipGroup.setObjects(
      *(("CISCO-VDC-MIB", "ciscoVdcIfMembershipStatus"),
        ("CISCO-VDC-MIB", "ciscoVdcIfMembershipStorageType"))
)
if mibBuilder.loadTexts:
    ciscoVdcIfMembershipGroup.setStatus("current")

ciscoVdcFCoEVlansGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 2, 8)
)
ciscoVdcFCoEVlansGroup.setObjects(
      *(("CISCO-VDC-MIB", "ciscoVdcFCoEVlansFirst2K"),
        ("CISCO-VDC-MIB", "ciscoVdcFCoEVlansSecond2K"),
        ("CISCO-VDC-MIB", "ciscoVdcFCoEVlansFromVdc"))
)
if mibBuilder.loadTexts:
    ciscoVdcFCoEVlansGroup.setStatus("current")

ciscoVdcSharedInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 2, 9)
)
ciscoVdcSharedInterfaceGroup.setObjects(
      *(("CISCO-VDC-MIB", "ciscoVdcSharedInterfaceRowStatus"),
        ("CISCO-VDC-MIB", "ciscoVdcSharedInterfaceStorageType"))
)
if mibBuilder.loadTexts:
    ciscoVdcSharedInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVdcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVdcMIBCompliance.setStatus(
        "deprecated"
    )

ciscoVdcMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 774, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoVdcMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VDC-MIB",
    **{"CiscoVdcHaPolicy": CiscoVdcHaPolicy,
       "CiscoVdcPercentOrMinusOne": CiscoVdcPercentOrMinusOne,
       "ciscoVdcMIB": ciscoVdcMIB,
       "ciscoVdcMIBNotifs": ciscoVdcMIBNotifs,
       "ciscoVdcMIBObjects": ciscoVdcMIBObjects,
       "ciscoVdcTable": ciscoVdcTable,
       "ciscoVdcEntry": ciscoVdcEntry,
       "ciscoVdcId": ciscoVdcId,
       "ciscoVdcName": ciscoVdcName,
       "ciscoVdcState": ciscoVdcState,
       "ciscoVdcFcoeCapable": ciscoVdcFcoeCapable,
       "ciscoVdcMac": ciscoVdcMac,
       "ciscoVdcSwitchId": ciscoVdcSwitchId,
       "ciscoVdcRowStatus": ciscoVdcRowStatus,
       "ciscoVdcStorageType": ciscoVdcStorageType,
       "ciscoVdcGlobal": ciscoVdcGlobal,
       "ciscoVdcMaxNumberVdcAllowed": ciscoVdcMaxNumberVdcAllowed,
       "ciscoVdcCombinedHostnameEnabled": ciscoVdcCombinedHostnameEnabled,
       "ciscoVdcExt": ciscoVdcExt,
       "ciscoVdcExtTable": ciscoVdcExtTable,
       "ciscoVdcExtEntry": ciscoVdcExtEntry,
       "ciscoVdcSingleSupHaPolicy": ciscoVdcSingleSupHaPolicy,
       "ciscoVdcDualSupHaPolicy": ciscoVdcDualSupHaPolicy,
       "ciscoVdcBootOrder": ciscoVdcBootOrder,
       "ciscoVdcTimeCreated": ciscoVdcTimeCreated,
       "ciscoVdcReloadCount": ciscoVdcReloadCount,
       "ciscoVdcRestartCount": ciscoVdcRestartCount,
       "ciscoVdcRestartTime": ciscoVdcRestartTime,
       "ciscoVdcRestartReason": ciscoVdcRestartReason,
       "ciscoVdcType": ciscoVdcType,
       "ciscoVdcAdminStatus": ciscoVdcAdminStatus,
       "ciscoVdcFromUnallocatedIntf": ciscoVdcFromUnallocatedIntf,
       "ciscoVdcFeatureSetList": ciscoVdcFeatureSetList,
       "ciscoVdcResourceTemplate": ciscoVdcResourceTemplate,
       "ciscoVdcModuleCapList": ciscoVdcModuleCapList,
       "ciscoVdcCpuPriority": ciscoVdcCpuPriority,
       "ciscoVdcCpuSharePercent": ciscoVdcCpuSharePercent,
       "ciscoVdcResource": ciscoVdcResource,
       "ciscoVdcGlobalResUsageTable": ciscoVdcGlobalResUsageTable,
       "ciscoVdcGlobalResUsageEntry": ciscoVdcGlobalResUsageEntry,
       "ciscoVdcGlobalResID": ciscoVdcGlobalResID,
       "ciscoVdcGlobalResName": ciscoVdcGlobalResName,
       "ciscoVdcGlobalResUsed": ciscoVdcGlobalResUsed,
       "ciscoVdcGlobalResUnused": ciscoVdcGlobalResUnused,
       "ciscoVdcGlobalResFree": ciscoVdcGlobalResFree,
       "ciscoVdcGlobalResAvail": ciscoVdcGlobalResAvail,
       "ciscoVdcGlobalResTotal": ciscoVdcGlobalResTotal,
       "ciscoVdcResUsageTable": ciscoVdcResUsageTable,
       "ciscoVdcResUsageEntry": ciscoVdcResUsageEntry,
       "ciscoVdcResID": ciscoVdcResID,
       "ciscoVdcResMin": ciscoVdcResMin,
       "ciscoVdcResMax": ciscoVdcResMax,
       "ciscoVdcResUsed": ciscoVdcResUsed,
       "ciscoVdcResUnused": ciscoVdcResUnused,
       "ciscoVdcResAvail": ciscoVdcResAvail,
       "ciscoVdcResTemplateTable": ciscoVdcResTemplateTable,
       "ciscoVdcResTemplateEntry": ciscoVdcResTemplateEntry,
       "ciscoVdcResTemplateName": ciscoVdcResTemplateName,
       "ciscoVdcResTemplateResID": ciscoVdcResTemplateResID,
       "ciscoVdcResTemplateMin": ciscoVdcResTemplateMin,
       "ciscoVdcResTemplateMax": ciscoVdcResTemplateMax,
       "ciscoVdcResTemplateStorageType": ciscoVdcResTemplateStorageType,
       "ciscoVdcResTemplateStatus": ciscoVdcResTemplateStatus,
       "ciscoVdcInterface": ciscoVdcInterface,
       "ciscoVdcIfMembershipTable": ciscoVdcIfMembershipTable,
       "ciscoVdcIfMembershipEntry": ciscoVdcIfMembershipEntry,
       "ciscoVdcIfMembershipifIndex": ciscoVdcIfMembershipifIndex,
       "ciscoVdcIfMembershipStorageType": ciscoVdcIfMembershipStorageType,
       "ciscoVdcIfMembershipStatus": ciscoVdcIfMembershipStatus,
       "ciscoVdcFCoEVlansTable": ciscoVdcFCoEVlansTable,
       "ciscoVdcFCoEVlansEntry": ciscoVdcFCoEVlansEntry,
       "ciscoVdcFCoEVlansFirst2K": ciscoVdcFCoEVlansFirst2K,
       "ciscoVdcFCoEVlansSecond2K": ciscoVdcFCoEVlansSecond2K,
       "ciscoVdcFCoEVlansFromVdc": ciscoVdcFCoEVlansFromVdc,
       "ciscoVdcSharedInterfaceTable": ciscoVdcSharedInterfaceTable,
       "ciscoVdcSharedInterfaceEntry": ciscoVdcSharedInterfaceEntry,
       "ciscoVdcSharedInterfaceifIndex": ciscoVdcSharedInterfaceifIndex,
       "ciscoVdcSharedInterfaceStorageType": ciscoVdcSharedInterfaceStorageType,
       "ciscoVdcSharedInterfaceRowStatus": ciscoVdcSharedInterfaceRowStatus,
       "ciscoVdcMIBConform": ciscoVdcMIBConform,
       "ciscoVdcMIBCompliances": ciscoVdcMIBCompliances,
       "ciscoVdcMIBCompliance": ciscoVdcMIBCompliance,
       "ciscoVdcMIBCompliance1": ciscoVdcMIBCompliance1,
       "ciscoVdcMIBGroups": ciscoVdcMIBGroups,
       "ciscoVdcGroup": ciscoVdcGroup,
       "ciscoVdcExtGroup": ciscoVdcExtGroup,
       "ciscoVdcGlobalResUsageGroup": ciscoVdcGlobalResUsageGroup,
       "ciscoVdcResUsageGroup": ciscoVdcResUsageGroup,
       "ciscoVdcResTemplateGroup": ciscoVdcResTemplateGroup,
       "ciscoVdcGlobalGroup": ciscoVdcGlobalGroup,
       "ciscoVdcIfMembershipGroup": ciscoVdcIfMembershipGroup,
       "ciscoVdcFCoEVlansGroup": ciscoVdcFCoEVlansGroup,
       "ciscoVdcSharedInterfaceGroup": ciscoVdcSharedInterfaceGroup}
)
