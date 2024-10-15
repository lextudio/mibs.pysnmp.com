# SNMP MIB module (HUAWEI-BRAS-COPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-COPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:57 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

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

hwBRASCops = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwCopsGroupObject_ObjectIdentity = ObjectIdentity
hwCopsGroupObject = _HwCopsGroupObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1)
)
_HwCopsGroupTable_Object = MibTable
hwCopsGroupTable = _HwCopsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hwCopsGroupTable.setStatus("current")
_HwCopsGroupEntry_Object = MibTableRow
hwCopsGroupEntry = _HwCopsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1)
)
hwCopsGroupEntry.setIndexNames(
    (0, "HUAWEI-BRAS-COPS-MIB", "hwCopsGroupIndex"),
)
if mibBuilder.loadTexts:
    hwCopsGroupEntry.setStatus("current")


class _HwCopsGroupIndex_Type(Integer32):
    """Custom type hwCopsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwCopsGroupIndex_Type.__name__ = "Integer32"
_HwCopsGroupIndex_Object = MibTableColumn
hwCopsGroupIndex = _HwCopsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1, 1),
    _HwCopsGroupIndex_Type()
)
hwCopsGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCopsGroupIndex.setStatus("current")


class _HwCopsGroupName_Type(OctetString):
    """Custom type hwCopsGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwCopsGroupName_Type.__name__ = "OctetString"
_HwCopsGroupName_Object = MibTableColumn
hwCopsGroupName = _HwCopsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1, 2),
    _HwCopsGroupName_Type()
)
hwCopsGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCopsGroupName.setStatus("current")


class _HwCopsGroupClientType_Type(Integer32):
    """Custom type hwCopsGroupClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_HwCopsGroupClientType_Type.__name__ = "Integer32"
_HwCopsGroupClientType_Object = MibTableColumn
hwCopsGroupClientType = _HwCopsGroupClientType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1, 3),
    _HwCopsGroupClientType_Type()
)
hwCopsGroupClientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCopsGroupClientType.setStatus("current")


class _HwCopsGroupIfActive_Type(Integer32):
    """Custom type hwCopsGroupIfActive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwCopsGroupIfActive_Type.__name__ = "Integer32"
_HwCopsGroupIfActive_Object = MibTableColumn
hwCopsGroupIfActive = _HwCopsGroupIfActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1, 4),
    _HwCopsGroupIfActive_Type()
)
hwCopsGroupIfActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsGroupIfActive.setStatus("current")


class _HwCopsGroupFlowKeepingTime_Type(Integer32):
    """Custom type hwCopsGroupFlowKeepingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwCopsGroupFlowKeepingTime_Type.__name__ = "Integer32"
_HwCopsGroupFlowKeepingTime_Object = MibTableColumn
hwCopsGroupFlowKeepingTime = _HwCopsGroupFlowKeepingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1, 5),
    _HwCopsGroupFlowKeepingTime_Type()
)
hwCopsGroupFlowKeepingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsGroupFlowKeepingTime.setStatus("current")


class _HwCopsGroupSecret_Type(OctetString):
    """Custom type hwCopsGroupSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwCopsGroupSecret_Type.__name__ = "OctetString"
_HwCopsGroupSecret_Object = MibTableColumn
hwCopsGroupSecret = _HwCopsGroupSecret_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1, 6),
    _HwCopsGroupSecret_Type()
)
hwCopsGroupSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsGroupSecret.setStatus("current")


class _HwCopsGroupPepid_Type(OctetString):
    """Custom type hwCopsGroupPepid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwCopsGroupPepid_Type.__name__ = "OctetString"
_HwCopsGroupPepid_Object = MibTableColumn
hwCopsGroupPepid = _HwCopsGroupPepid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1, 7),
    _HwCopsGroupPepid_Type()
)
hwCopsGroupPepid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsGroupPepid.setStatus("current")
_HwCopsGroupRowStatus_Type = RowStatus
_HwCopsGroupRowStatus_Object = MibTableColumn
hwCopsGroupRowStatus = _HwCopsGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1, 8),
    _HwCopsGroupRowStatus_Type()
)
hwCopsGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCopsGroupRowStatus.setStatus("current")


class _HwCopsGroupSrcIf_Type(OctetString):
    """Custom type hwCopsGroupSrcIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwCopsGroupSrcIf_Type.__name__ = "OctetString"
_HwCopsGroupSrcIf_Object = MibTableColumn
hwCopsGroupSrcIf = _HwCopsGroupSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1, 9),
    _HwCopsGroupSrcIf_Type()
)
hwCopsGroupSrcIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsGroupSrcIf.setStatus("current")


class _HwCopsGroupClientOption82Info_Type(TruthValue):
    """Custom type hwCopsGroupClientOption82Info based on TruthValue"""


_HwCopsGroupClientOption82Info_Object = MibTableColumn
hwCopsGroupClientOption82Info = _HwCopsGroupClientOption82Info_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 1, 1, 10),
    _HwCopsGroupClientOption82Info_Type()
)
hwCopsGroupClientOption82Info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsGroupClientOption82Info.setStatus("current")
_HwCopsServerTable_Object = MibTable
hwCopsServerTable = _HwCopsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hwCopsServerTable.setStatus("current")
_HwCopsServerEntry_Object = MibTableRow
hwCopsServerEntry = _HwCopsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2, 1)
)
hwCopsServerEntry.setIndexNames(
    (0, "HUAWEI-BRAS-COPS-MIB", "hwCopsServerGroupIndex"),
    (0, "HUAWEI-BRAS-COPS-MIB", "hwCopsGroupServerIndex"),
)
if mibBuilder.loadTexts:
    hwCopsServerEntry.setStatus("current")


class _HwCopsServerGroupIndex_Type(Integer32):
    """Custom type hwCopsServerGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwCopsServerGroupIndex_Type.__name__ = "Integer32"
_HwCopsServerGroupIndex_Object = MibTableColumn
hwCopsServerGroupIndex = _HwCopsServerGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2, 1, 1),
    _HwCopsServerGroupIndex_Type()
)
hwCopsServerGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCopsServerGroupIndex.setStatus("current")


class _HwCopsGroupServerIndex_Type(Integer32):
    """Custom type hwCopsGroupServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwCopsGroupServerIndex_Type.__name__ = "Integer32"
_HwCopsGroupServerIndex_Object = MibTableColumn
hwCopsGroupServerIndex = _HwCopsGroupServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2, 1, 2),
    _HwCopsGroupServerIndex_Type()
)
hwCopsGroupServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCopsGroupServerIndex.setStatus("current")


class _HwCopsServerVpnInstance_Type(OctetString):
    """Custom type hwCopsServerVpnInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwCopsServerVpnInstance_Type.__name__ = "OctetString"
_HwCopsServerVpnInstance_Object = MibTableColumn
hwCopsServerVpnInstance = _HwCopsServerVpnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2, 1, 3),
    _HwCopsServerVpnInstance_Type()
)
hwCopsServerVpnInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsServerVpnInstance.setStatus("current")
_HwCopsServerIp_Type = IpAddress
_HwCopsServerIp_Object = MibTableColumn
hwCopsServerIp = _HwCopsServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2, 1, 4),
    _HwCopsServerIp_Type()
)
hwCopsServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsServerIp.setStatus("current")


class _HwCopsServerPort_Type(Integer32):
    """Custom type hwCopsServerPort based on Integer32"""
    defaultValue = 3288

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwCopsServerPort_Type.__name__ = "Integer32"
_HwCopsServerPort_Object = MibTableColumn
hwCopsServerPort = _HwCopsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2, 1, 5),
    _HwCopsServerPort_Type()
)
hwCopsServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsServerPort.setStatus("current")


class _HwCopsServerWeight_Type(Integer32):
    """Custom type hwCopsServerWeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwCopsServerWeight_Type.__name__ = "Integer32"
_HwCopsServerWeight_Object = MibTableColumn
hwCopsServerWeight = _HwCopsServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2, 1, 6),
    _HwCopsServerWeight_Type()
)
hwCopsServerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsServerWeight.setStatus("current")


class _HwCopsServerClientPort_Type(Integer32):
    """Custom type hwCopsServerClientPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwCopsServerClientPort_Type.__name__ = "Integer32"
_HwCopsServerClientPort_Object = MibTableColumn
hwCopsServerClientPort = _HwCopsServerClientPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2, 1, 7),
    _HwCopsServerClientPort_Type()
)
hwCopsServerClientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsServerClientPort.setStatus("current")
_HwCopsServerRowStatus_Type = RowStatus
_HwCopsServerRowStatus_Object = MibTableColumn
hwCopsServerRowStatus = _HwCopsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2, 1, 8),
    _HwCopsServerRowStatus_Type()
)
hwCopsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCopsServerRowStatus.setStatus("current")


class _HwCopsServerSecret_Type(OctetString):
    """Custom type hwCopsServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwCopsServerSecret_Type.__name__ = "OctetString"
_HwCopsServerSecret_Object = MibTableColumn
hwCopsServerSecret = _HwCopsServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 2, 1, 9),
    _HwCopsServerSecret_Type()
)
hwCopsServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsServerSecret.setStatus("current")
_HwCopsConfigTable_ObjectIdentity = ObjectIdentity
hwCopsConfigTable = _HwCopsConfigTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 3)
)


class _HwCopsConfigOpenTimeout_Type(Integer32):
    """Custom type hwCopsConfigOpenTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwCopsConfigOpenTimeout_Type.__name__ = "Integer32"
_HwCopsConfigOpenTimeout_Object = MibScalar
hwCopsConfigOpenTimeout = _HwCopsConfigOpenTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 3, 1),
    _HwCopsConfigOpenTimeout_Type()
)
hwCopsConfigOpenTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsConfigOpenTimeout.setStatus("current")
_HwCopsConfigKaTimeout_Type = Integer32
_HwCopsConfigKaTimeout_Object = MibScalar
hwCopsConfigKaTimeout = _HwCopsConfigKaTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 3, 2),
    _HwCopsConfigKaTimeout_Type()
)
hwCopsConfigKaTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCopsConfigKaTimeout.setStatus("current")
_HwCopsConfigSrcIfDesc_Type = OctetString
_HwCopsConfigSrcIfDesc_Object = MibScalar
hwCopsConfigSrcIfDesc = _HwCopsConfigSrcIfDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 1, 3, 3),
    _HwCopsConfigSrcIfDesc_Type()
)
hwCopsConfigSrcIfDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCopsConfigSrcIfDesc.setStatus("current")
_HwCopsConformance_ObjectIdentity = ObjectIdentity
hwCopsConformance = _HwCopsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 2)
)
_HwCopsCompliances_ObjectIdentity = ObjectIdentity
hwCopsCompliances = _HwCopsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 2, 1)
)
_HwCopsObjectGroups_ObjectIdentity = ObjectIdentity
hwCopsObjectGroups = _HwCopsObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 2, 2)
)

# Managed Objects groups

hwCopsGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 2, 2, 1)
)
hwCopsGroupGroup.setObjects(
      *(("HUAWEI-BRAS-COPS-MIB", "hwCopsGroupName"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsGroupClientType"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsGroupIfActive"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsGroupFlowKeepingTime"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsGroupSecret"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsGroupPepid"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsGroupRowStatus"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsGroupSrcIf"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsGroupClientOption82Info"))
)
if mibBuilder.loadTexts:
    hwCopsGroupGroup.setStatus("current")

hwCopsServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 2, 2, 2)
)
hwCopsServerGroup.setObjects(
      *(("HUAWEI-BRAS-COPS-MIB", "hwCopsServerIp"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsServerPort"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsServerWeight"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsServerVpnInstance"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsServerClientPort"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsServerRowStatus"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsServerSecret"))
)
if mibBuilder.loadTexts:
    hwCopsServerGroup.setStatus("current")

hwCopsConfigTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 2, 2, 3)
)
hwCopsConfigTableGroup.setObjects(
      *(("HUAWEI-BRAS-COPS-MIB", "hwCopsConfigOpenTimeout"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsConfigKaTimeout"),
        ("HUAWEI-BRAS-COPS-MIB", "hwCopsConfigSrcIfDesc"))
)
if mibBuilder.loadTexts:
    hwCopsConfigTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwCopsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwCopsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-COPS-MIB",
    **{"hwBRASCops": hwBRASCops,
       "hwCopsGroupObject": hwCopsGroupObject,
       "hwCopsGroupTable": hwCopsGroupTable,
       "hwCopsGroupEntry": hwCopsGroupEntry,
       "hwCopsGroupIndex": hwCopsGroupIndex,
       "hwCopsGroupName": hwCopsGroupName,
       "hwCopsGroupClientType": hwCopsGroupClientType,
       "hwCopsGroupIfActive": hwCopsGroupIfActive,
       "hwCopsGroupFlowKeepingTime": hwCopsGroupFlowKeepingTime,
       "hwCopsGroupSecret": hwCopsGroupSecret,
       "hwCopsGroupPepid": hwCopsGroupPepid,
       "hwCopsGroupRowStatus": hwCopsGroupRowStatus,
       "hwCopsGroupSrcIf": hwCopsGroupSrcIf,
       "hwCopsGroupClientOption82Info": hwCopsGroupClientOption82Info,
       "hwCopsServerTable": hwCopsServerTable,
       "hwCopsServerEntry": hwCopsServerEntry,
       "hwCopsServerGroupIndex": hwCopsServerGroupIndex,
       "hwCopsGroupServerIndex": hwCopsGroupServerIndex,
       "hwCopsServerVpnInstance": hwCopsServerVpnInstance,
       "hwCopsServerIp": hwCopsServerIp,
       "hwCopsServerPort": hwCopsServerPort,
       "hwCopsServerWeight": hwCopsServerWeight,
       "hwCopsServerClientPort": hwCopsServerClientPort,
       "hwCopsServerRowStatus": hwCopsServerRowStatus,
       "hwCopsServerSecret": hwCopsServerSecret,
       "hwCopsConfigTable": hwCopsConfigTable,
       "hwCopsConfigOpenTimeout": hwCopsConfigOpenTimeout,
       "hwCopsConfigKaTimeout": hwCopsConfigKaTimeout,
       "hwCopsConfigSrcIfDesc": hwCopsConfigSrcIfDesc,
       "hwCopsConformance": hwCopsConformance,
       "hwCopsCompliances": hwCopsCompliances,
       "hwCopsCompliance": hwCopsCompliance,
       "hwCopsObjectGroups": hwCopsObjectGroups,
       "hwCopsGroupGroup": hwCopsGroupGroup,
       "hwCopsServerGroup": hwCopsServerGroup,
       "hwCopsConfigTableGroup": hwCopsConfigTableGroup}
)
