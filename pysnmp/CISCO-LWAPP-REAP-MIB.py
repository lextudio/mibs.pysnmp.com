# SNMP MIB module (CISCO-LWAPP-REAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-REAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:54 2024
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

(cLApSysMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApSysMacAddress")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappReapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517)
)
ciscoLwappReapMIB.setRevisions(
        ("2010-10-06 00:00",
         "2010-02-06 00:00",
         "2007-11-01 00:00",
         "2007-04-19 00:00",
         "2006-04-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappReapMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappReapMIBNotifs = _CiscoLwappReapMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 0)
)
_CiscoLwappReapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappReapMIBObjects = _CiscoLwappReapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1)
)
_CiscoLwappReapWlanConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapWlanConfig = _CiscoLwappReapWlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1)
)
_CLReapWlanConfigTable_Object = MibTable
cLReapWlanConfigTable = _CLReapWlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLReapWlanConfigTable.setStatus("current")
_CLReapWlanConfigEntry_Object = MibTableRow
cLReapWlanConfigEntry = _CLReapWlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1)
)
cLReapWlanConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapWlanConfigEntry.setStatus("current")


class _CLReapWlanEnLocalSwitching_Type(TruthValue):
    """Custom type cLReapWlanEnLocalSwitching based on TruthValue"""


_CLReapWlanEnLocalSwitching_Object = MibTableColumn
cLReapWlanEnLocalSwitching = _CLReapWlanEnLocalSwitching_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 1),
    _CLReapWlanEnLocalSwitching_Type()
)
cLReapWlanEnLocalSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanEnLocalSwitching.setStatus("current")


class _CLReapWlanClientIpLearnEnable_Type(TruthValue):
    """Custom type cLReapWlanClientIpLearnEnable based on TruthValue"""


_CLReapWlanClientIpLearnEnable_Object = MibTableColumn
cLReapWlanClientIpLearnEnable = _CLReapWlanClientIpLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 2),
    _CLReapWlanClientIpLearnEnable_Type()
)
cLReapWlanClientIpLearnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanClientIpLearnEnable.setStatus("current")


class _CLReapWlanApAuth_Type(TruthValue):
    """Custom type cLReapWlanApAuth based on TruthValue"""


_CLReapWlanApAuth_Object = MibTableColumn
cLReapWlanApAuth = _CLReapWlanApAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 1, 1, 1, 3),
    _CLReapWlanApAuth_Type()
)
cLReapWlanApAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapWlanApAuth.setStatus("current")
_CiscoLwappReapApConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapApConfig = _CiscoLwappReapApConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2)
)
_CLReapApConfigTable_Object = MibTable
cLReapApConfigTable = _CLReapApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLReapApConfigTable.setStatus("current")
_CLReapApConfigEntry_Object = MibTableRow
cLReapApConfigEntry = _CLReapApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1)
)
cLReapApConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLReapApConfigEntry.setStatus("current")


class _CLReapApNativeVlanId_Type(Unsigned32):
    """Custom type cLReapApNativeVlanId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CLReapApNativeVlanId_Type.__name__ = "Unsigned32"
_CLReapApNativeVlanId_Object = MibTableColumn
cLReapApNativeVlanId = _CLReapApNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 1),
    _CLReapApNativeVlanId_Type()
)
cLReapApNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapApNativeVlanId.setStatus("current")


class _CLReapApVlanEnable_Type(TruthValue):
    """Custom type cLReapApVlanEnable based on TruthValue"""


_CLReapApVlanEnable_Object = MibTableColumn
cLReapApVlanEnable = _CLReapApVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 2),
    _CLReapApVlanEnable_Type()
)
cLReapApVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapApVlanEnable.setStatus("current")


class _CLReapHomeApEnable_Type(TruthValue):
    """Custom type cLReapHomeApEnable based on TruthValue"""


_CLReapHomeApEnable_Object = MibTableColumn
cLReapHomeApEnable = _CLReapHomeApEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 3),
    _CLReapHomeApEnable_Type()
)
cLReapHomeApEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapHomeApEnable.setStatus("current")


class _CLReapApLeastLatencyJoinEnable_Type(TruthValue):
    """Custom type cLReapApLeastLatencyJoinEnable based on TruthValue"""


_CLReapApLeastLatencyJoinEnable_Object = MibTableColumn
cLReapApLeastLatencyJoinEnable = _CLReapApLeastLatencyJoinEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 4),
    _CLReapApLeastLatencyJoinEnable_Type()
)
cLReapApLeastLatencyJoinEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapApLeastLatencyJoinEnable.setStatus("current")


class _CLReapHomeApLocalSsidReset_Type(TruthValue):
    """Custom type cLReapHomeApLocalSsidReset based on TruthValue"""


_CLReapHomeApLocalSsidReset_Object = MibTableColumn
cLReapHomeApLocalSsidReset = _CLReapHomeApLocalSsidReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 1, 1, 5),
    _CLReapHomeApLocalSsidReset_Type()
)
cLReapHomeApLocalSsidReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapHomeApLocalSsidReset.setStatus("current")
_CLReapApVlanIdTable_Object = MibTable
cLReapApVlanIdTable = _CLReapApVlanIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cLReapApVlanIdTable.setStatus("current")
_CLReapApVlanIdEntry_Object = MibTableRow
cLReapApVlanIdEntry = _CLReapApVlanIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 2, 1)
)
cLReapApVlanIdEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLReapApVlanIdEntry.setStatus("current")


class _CLReapApVlanId_Type(Unsigned32):
    """Custom type cLReapApVlanId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CLReapApVlanId_Type.__name__ = "Unsigned32"
_CLReapApVlanId_Object = MibTableColumn
cLReapApVlanId = _CLReapApVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 2, 2, 1, 1),
    _CLReapApVlanId_Type()
)
cLReapApVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLReapApVlanId.setStatus("current")
_CiscoLwappReapGroupConfig_ObjectIdentity = ObjectIdentity
ciscoLwappReapGroupConfig = _CiscoLwappReapGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3)
)
_CLReapGroupConfigTable_Object = MibTable
cLReapGroupConfigTable = _CLReapGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLReapGroupConfigTable.setStatus("current")
_CLReapGroupConfigEntry_Object = MibTableRow
cLReapGroupConfigEntry = _CLReapGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1)
)
cLReapGroupConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
)
if mibBuilder.loadTexts:
    cLReapGroupConfigEntry.setStatus("current")
_CLReapGroupName_Type = SnmpAdminString
_CLReapGroupName_Object = MibTableColumn
cLReapGroupName = _CLReapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 1),
    _CLReapGroupName_Type()
)
cLReapGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapGroupName.setStatus("current")


class _CLReapGroupPrimaryRadiusIndex_Type(Unsigned32):
    """Custom type cLReapGroupPrimaryRadiusIndex based on Unsigned32"""
    defaultValue = 0


_CLReapGroupPrimaryRadiusIndex_Object = MibTableColumn
cLReapGroupPrimaryRadiusIndex = _CLReapGroupPrimaryRadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 2),
    _CLReapGroupPrimaryRadiusIndex_Type()
)
cLReapGroupPrimaryRadiusIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupPrimaryRadiusIndex.setStatus("current")


class _CLReapGroupSecondaryRadiusIndex_Type(Unsigned32):
    """Custom type cLReapGroupSecondaryRadiusIndex based on Unsigned32"""
    defaultValue = 0


_CLReapGroupSecondaryRadiusIndex_Object = MibTableColumn
cLReapGroupSecondaryRadiusIndex = _CLReapGroupSecondaryRadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 3),
    _CLReapGroupSecondaryRadiusIndex_Type()
)
cLReapGroupSecondaryRadiusIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupSecondaryRadiusIndex.setStatus("current")
_CLReapGroupStorageType_Type = StorageType
_CLReapGroupStorageType_Object = MibTableColumn
cLReapGroupStorageType = _CLReapGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 4),
    _CLReapGroupStorageType_Type()
)
cLReapGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupStorageType.setStatus("current")
_CLReapGroupRowStatus_Type = RowStatus
_CLReapGroupRowStatus_Object = MibTableColumn
cLReapGroupRowStatus = _CLReapGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 5),
    _CLReapGroupRowStatus_Type()
)
cLReapGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRowStatus.setStatus("current")


class _CLReapGroupRadiusPacTimeout_Type(Unsigned32):
    """Custom type cLReapGroupRadiusPacTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4095),
    )


_CLReapGroupRadiusPacTimeout_Type.__name__ = "Unsigned32"
_CLReapGroupRadiusPacTimeout_Object = MibTableColumn
cLReapGroupRadiusPacTimeout = _CLReapGroupRadiusPacTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 6),
    _CLReapGroupRadiusPacTimeout_Type()
)
cLReapGroupRadiusPacTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusPacTimeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    cLReapGroupRadiusPacTimeout.setUnits("days")


class _CLReapGroupRadiusAuthorityId_Type(OctetString):
    """Custom type cLReapGroupRadiusAuthorityId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupRadiusAuthorityId_Type.__name__ = "OctetString"
_CLReapGroupRadiusAuthorityId_Object = MibTableColumn
cLReapGroupRadiusAuthorityId = _CLReapGroupRadiusAuthorityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 7),
    _CLReapGroupRadiusAuthorityId_Type()
)
cLReapGroupRadiusAuthorityId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusAuthorityId.setStatus("current")


class _CLReapGroupRadiusAuthorityInfo_Type(OctetString):
    """Custom type cLReapGroupRadiusAuthorityInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLReapGroupRadiusAuthorityInfo_Type.__name__ = "OctetString"
_CLReapGroupRadiusAuthorityInfo_Object = MibTableColumn
cLReapGroupRadiusAuthorityInfo = _CLReapGroupRadiusAuthorityInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 8),
    _CLReapGroupRadiusAuthorityInfo_Type()
)
cLReapGroupRadiusAuthorityInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusAuthorityInfo.setStatus("current")


class _CLReapGroupRadiusServerKey_Type(OctetString):
    """Custom type cLReapGroupRadiusServerKey based on OctetString"""
    defaultValue = OctetString("****")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLReapGroupRadiusServerKey_Type.__name__ = "OctetString"
_CLReapGroupRadiusServerKey_Object = MibTableColumn
cLReapGroupRadiusServerKey = _CLReapGroupRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 9),
    _CLReapGroupRadiusServerKey_Type()
)
cLReapGroupRadiusServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusServerKey.setStatus("current")


class _CLReapGroupRadiusIgnoreKey_Type(TruthValue):
    """Custom type cLReapGroupRadiusIgnoreKey based on TruthValue"""


_CLReapGroupRadiusIgnoreKey_Object = MibTableColumn
cLReapGroupRadiusIgnoreKey = _CLReapGroupRadiusIgnoreKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 10),
    _CLReapGroupRadiusIgnoreKey_Type()
)
cLReapGroupRadiusIgnoreKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusIgnoreKey.setStatus("current")


class _CLReapGroupRadiusEnable_Type(TruthValue):
    """Custom type cLReapGroupRadiusEnable based on TruthValue"""


_CLReapGroupRadiusEnable_Object = MibTableColumn
cLReapGroupRadiusEnable = _CLReapGroupRadiusEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 11),
    _CLReapGroupRadiusEnable_Type()
)
cLReapGroupRadiusEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusEnable.setStatus("current")


class _CLReapGroupRadiusLeapEnable_Type(TruthValue):
    """Custom type cLReapGroupRadiusLeapEnable based on TruthValue"""


_CLReapGroupRadiusLeapEnable_Object = MibTableColumn
cLReapGroupRadiusLeapEnable = _CLReapGroupRadiusLeapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 12),
    _CLReapGroupRadiusLeapEnable_Type()
)
cLReapGroupRadiusLeapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusLeapEnable.setStatus("current")


class _CLReapGroupRadiusEapFastEnable_Type(TruthValue):
    """Custom type cLReapGroupRadiusEapFastEnable based on TruthValue"""


_CLReapGroupRadiusEapFastEnable_Object = MibTableColumn
cLReapGroupRadiusEapFastEnable = _CLReapGroupRadiusEapFastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 13),
    _CLReapGroupRadiusEapFastEnable_Type()
)
cLReapGroupRadiusEapFastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusEapFastEnable.setStatus("current")


class _CLReapGroupRadiusPacTimeoutCtrl_Type(Unsigned32):
    """Custom type cLReapGroupRadiusPacTimeoutCtrl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CLReapGroupRadiusPacTimeoutCtrl_Type.__name__ = "Unsigned32"
_CLReapGroupRadiusPacTimeoutCtrl_Object = MibTableColumn
cLReapGroupRadiusPacTimeoutCtrl = _CLReapGroupRadiusPacTimeoutCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 1, 1, 14),
    _CLReapGroupRadiusPacTimeoutCtrl_Type()
)
cLReapGroupRadiusPacTimeoutCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupRadiusPacTimeoutCtrl.setStatus("current")
if mibBuilder.loadTexts:
    cLReapGroupRadiusPacTimeoutCtrl.setUnits("seconds")
_CLReapGroupApConfigTable_Object = MibTable
cLReapGroupApConfigTable = _CLReapGroupApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cLReapGroupApConfigTable.setStatus("current")
_CLReapGroupApConfigEntry_Object = MibTableRow
cLReapGroupApConfigEntry = _CLReapGroupApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 2, 1)
)
cLReapGroupApConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLReapGroupApConfigEntry.setStatus("current")
_CLReapGroupApStorageType_Type = StorageType
_CLReapGroupApStorageType_Object = MibTableColumn
cLReapGroupApStorageType = _CLReapGroupApStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 2, 1, 1),
    _CLReapGroupApStorageType_Type()
)
cLReapGroupApStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupApStorageType.setStatus("current")
_CLReapGroupApRowStatus_Type = RowStatus
_CLReapGroupApRowStatus_Object = MibTableColumn
cLReapGroupApRowStatus = _CLReapGroupApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 2, 1, 2),
    _CLReapGroupApRowStatus_Type()
)
cLReapGroupApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupApRowStatus.setStatus("current")
_CLReapGroupUserConfigTable_Object = MibTable
cLReapGroupUserConfigTable = _CLReapGroupUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cLReapGroupUserConfigTable.setStatus("current")
_CLReapGroupUserConfigEntry_Object = MibTableRow
cLReapGroupUserConfigEntry = _CLReapGroupUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3, 1)
)
cLReapGroupUserConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupName"),
    (0, "CISCO-LWAPP-REAP-MIB", "cLReapGroupUserName"),
)
if mibBuilder.loadTexts:
    cLReapGroupUserConfigEntry.setStatus("current")


class _CLReapGroupUserName_Type(SnmpAdminString):
    """Custom type cLReapGroupUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_CLReapGroupUserName_Type.__name__ = "SnmpAdminString"
_CLReapGroupUserName_Object = MibTableColumn
cLReapGroupUserName = _CLReapGroupUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3, 1, 1),
    _CLReapGroupUserName_Type()
)
cLReapGroupUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLReapGroupUserName.setStatus("current")


class _CLReapGroupUserPassword_Type(SnmpAdminString):
    """Custom type cLReapGroupUserPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLReapGroupUserPassword_Type.__name__ = "SnmpAdminString"
_CLReapGroupUserPassword_Object = MibTableColumn
cLReapGroupUserPassword = _CLReapGroupUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3, 1, 2),
    _CLReapGroupUserPassword_Type()
)
cLReapGroupUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupUserPassword.setStatus("current")
_CLReapGroupUserStorageType_Type = StorageType
_CLReapGroupUserStorageType_Object = MibTableColumn
cLReapGroupUserStorageType = _CLReapGroupUserStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3, 1, 3),
    _CLReapGroupUserStorageType_Type()
)
cLReapGroupUserStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupUserStorageType.setStatus("current")
_CLReapGroupUserRowStatus_Type = RowStatus
_CLReapGroupUserRowStatus_Object = MibTableColumn
cLReapGroupUserRowStatus = _CLReapGroupUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 1, 3, 3, 1, 4),
    _CLReapGroupUserRowStatus_Type()
)
cLReapGroupUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLReapGroupUserRowStatus.setStatus("current")
_CiscoLwappReapMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappReapMIBConform = _CiscoLwappReapMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2)
)
_CiscoLwappReapMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappReapMIBCompliances = _CiscoLwappReapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1)
)
_CiscoLwappReapMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappReapMIBGroups = _CiscoLwappReapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2)
)

# Managed Objects groups

ciscoLwappReapWlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 1)
)
ciscoLwappReapWlanConfigGroup.setObjects(
    ("CISCO-LWAPP-REAP-MIB", "cLReapWlanEnLocalSwitching")
)
if mibBuilder.loadTexts:
    ciscoLwappReapWlanConfigGroup.setStatus("current")

ciscoLwappReapApConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 2)
)
ciscoLwappReapApConfigGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapApNativeVlanId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApVlanId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApVlanEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapApConfigGroup.setStatus("current")

ciscoLwappReapGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 3)
)
ciscoLwappReapGroupConfigGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapGroupPrimaryRadiusIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupSecondaryRadiusIndex"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupStorageType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRowStatus"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApStorageType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupApRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapGroupConfigGroup.setStatus("current")

ciscoLwappReapGroupConfigRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 4)
)
ciscoLwappReapGroupConfigRadiusGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusPacTimeout"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusAuthorityId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusAuthorityInfo"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusServerKey"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusIgnoreKey"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusLeapEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusEapFastEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapGroupConfigRadiusGroup.setStatus("deprecated")

ciscoLwappReapGroupConfigUserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 5)
)
ciscoLwappReapGroupConfigUserAuthGroup.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapGroupUserPassword"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupUserStorageType"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupUserRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapGroupConfigUserAuthGroup.setStatus("current")

ciscoLwappReapApConfigGroupHomeAp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 6)
)
ciscoLwappReapApConfigGroupHomeAp.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapHomeApEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapApLeastLatencyJoinEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapWlanClientIpLearnEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapHomeApLocalSsidReset"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapApConfigGroupHomeAp.setStatus("current")

ciscoLwappReapGroupConfigRadiusGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 7)
)
ciscoLwappReapGroupConfigRadiusGroup1.setObjects(
      *(("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusAuthorityId"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusAuthorityInfo"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusServerKey"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusIgnoreKey"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusLeapEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusEapFastEnable"),
        ("CISCO-LWAPP-REAP-MIB", "cLReapGroupRadiusPacTimeoutCtrl"))
)
if mibBuilder.loadTexts:
    ciscoLwappReapGroupConfigRadiusGroup1.setStatus("current")

ciscoLwappReapWlanConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 2, 8)
)
ciscoLwappReapWlanConfigGroupSup1.setObjects(
    ("CISCO-LWAPP-REAP-MIB", "cLReapWlanApAuth")
)
if mibBuilder.loadTexts:
    ciscoLwappReapWlanConfigGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappReapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoLwappReapMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 517, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoLwappReapMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-REAP-MIB",
    **{"ciscoLwappReapMIB": ciscoLwappReapMIB,
       "ciscoLwappReapMIBNotifs": ciscoLwappReapMIBNotifs,
       "ciscoLwappReapMIBObjects": ciscoLwappReapMIBObjects,
       "ciscoLwappReapWlanConfig": ciscoLwappReapWlanConfig,
       "cLReapWlanConfigTable": cLReapWlanConfigTable,
       "cLReapWlanConfigEntry": cLReapWlanConfigEntry,
       "cLReapWlanEnLocalSwitching": cLReapWlanEnLocalSwitching,
       "cLReapWlanClientIpLearnEnable": cLReapWlanClientIpLearnEnable,
       "cLReapWlanApAuth": cLReapWlanApAuth,
       "ciscoLwappReapApConfig": ciscoLwappReapApConfig,
       "cLReapApConfigTable": cLReapApConfigTable,
       "cLReapApConfigEntry": cLReapApConfigEntry,
       "cLReapApNativeVlanId": cLReapApNativeVlanId,
       "cLReapApVlanEnable": cLReapApVlanEnable,
       "cLReapHomeApEnable": cLReapHomeApEnable,
       "cLReapApLeastLatencyJoinEnable": cLReapApLeastLatencyJoinEnable,
       "cLReapHomeApLocalSsidReset": cLReapHomeApLocalSsidReset,
       "cLReapApVlanIdTable": cLReapApVlanIdTable,
       "cLReapApVlanIdEntry": cLReapApVlanIdEntry,
       "cLReapApVlanId": cLReapApVlanId,
       "ciscoLwappReapGroupConfig": ciscoLwappReapGroupConfig,
       "cLReapGroupConfigTable": cLReapGroupConfigTable,
       "cLReapGroupConfigEntry": cLReapGroupConfigEntry,
       "cLReapGroupName": cLReapGroupName,
       "cLReapGroupPrimaryRadiusIndex": cLReapGroupPrimaryRadiusIndex,
       "cLReapGroupSecondaryRadiusIndex": cLReapGroupSecondaryRadiusIndex,
       "cLReapGroupStorageType": cLReapGroupStorageType,
       "cLReapGroupRowStatus": cLReapGroupRowStatus,
       "cLReapGroupRadiusPacTimeout": cLReapGroupRadiusPacTimeout,
       "cLReapGroupRadiusAuthorityId": cLReapGroupRadiusAuthorityId,
       "cLReapGroupRadiusAuthorityInfo": cLReapGroupRadiusAuthorityInfo,
       "cLReapGroupRadiusServerKey": cLReapGroupRadiusServerKey,
       "cLReapGroupRadiusIgnoreKey": cLReapGroupRadiusIgnoreKey,
       "cLReapGroupRadiusEnable": cLReapGroupRadiusEnable,
       "cLReapGroupRadiusLeapEnable": cLReapGroupRadiusLeapEnable,
       "cLReapGroupRadiusEapFastEnable": cLReapGroupRadiusEapFastEnable,
       "cLReapGroupRadiusPacTimeoutCtrl": cLReapGroupRadiusPacTimeoutCtrl,
       "cLReapGroupApConfigTable": cLReapGroupApConfigTable,
       "cLReapGroupApConfigEntry": cLReapGroupApConfigEntry,
       "cLReapGroupApStorageType": cLReapGroupApStorageType,
       "cLReapGroupApRowStatus": cLReapGroupApRowStatus,
       "cLReapGroupUserConfigTable": cLReapGroupUserConfigTable,
       "cLReapGroupUserConfigEntry": cLReapGroupUserConfigEntry,
       "cLReapGroupUserName": cLReapGroupUserName,
       "cLReapGroupUserPassword": cLReapGroupUserPassword,
       "cLReapGroupUserStorageType": cLReapGroupUserStorageType,
       "cLReapGroupUserRowStatus": cLReapGroupUserRowStatus,
       "ciscoLwappReapMIBConform": ciscoLwappReapMIBConform,
       "ciscoLwappReapMIBCompliances": ciscoLwappReapMIBCompliances,
       "ciscoLwappReapMIBCompliance": ciscoLwappReapMIBCompliance,
       "ciscoLwappReapMIBComplianceRev1": ciscoLwappReapMIBComplianceRev1,
       "ciscoLwappReapMIBComplianceRev2": ciscoLwappReapMIBComplianceRev2,
       "ciscoLwappReapMIBComplianceRev3": ciscoLwappReapMIBComplianceRev3,
       "ciscoLwappReapMIBComplianceRev4": ciscoLwappReapMIBComplianceRev4,
       "ciscoLwappReapMIBComplianceRev5": ciscoLwappReapMIBComplianceRev5,
       "ciscoLwappReapMIBGroups": ciscoLwappReapMIBGroups,
       "ciscoLwappReapWlanConfigGroup": ciscoLwappReapWlanConfigGroup,
       "ciscoLwappReapApConfigGroup": ciscoLwappReapApConfigGroup,
       "ciscoLwappReapGroupConfigGroup": ciscoLwappReapGroupConfigGroup,
       "ciscoLwappReapGroupConfigRadiusGroup": ciscoLwappReapGroupConfigRadiusGroup,
       "ciscoLwappReapGroupConfigUserAuthGroup": ciscoLwappReapGroupConfigUserAuthGroup,
       "ciscoLwappReapApConfigGroupHomeAp": ciscoLwappReapApConfigGroupHomeAp,
       "ciscoLwappReapGroupConfigRadiusGroup1": ciscoLwappReapGroupConfigRadiusGroup1,
       "ciscoLwappReapWlanConfigGroupSup1": ciscoLwappReapWlanConfigGroupSup1}
)
