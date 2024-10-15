# SNMP MIB module (CISCO-FLOW-CLONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FLOW-CLONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:39 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoFlowCloneMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 765)
)
ciscoFlowCloneMIB.setRevisions(
        ("2010-07-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CloneProfileIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CloneFlowIdentifier(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CloneProfilePointType(Integer32, TextualConvention):
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
        *(("interface", 4),
          ("none", 3),
          ("other", 1),
          ("unknown", 2))
    )



class CloneProfilePointIdentifier(InterfaceIndexOrZero, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoFlowCloneMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoFlowCloneMIBNotifications = _CiscoFlowCloneMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 0)
)
_CiscoFlowCloneMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFlowCloneMIBObjects = _CiscoFlowCloneMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1)
)
_CfcCloneProfiles_ObjectIdentity = ObjectIdentity
cfcCloneProfiles = _CfcCloneProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1)
)
_CfcCloneProfileIdNext_Type = CloneProfileIdentifier
_CfcCloneProfileIdNext_Object = MibScalar
cfcCloneProfileIdNext = _CfcCloneProfileIdNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 1),
    _CfcCloneProfileIdNext_Type()
)
cfcCloneProfileIdNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcCloneProfileIdNext.setStatus("current")
_CfcCloneProfileTable_Object = MibTable
cfcCloneProfileTable = _CfcCloneProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfcCloneProfileTable.setStatus("current")
_CfcCloneProfileEntry_Object = MibTableRow
cfcCloneProfileEntry = _CfcCloneProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1)
)
cfcCloneProfileEntry.setIndexNames(
    (0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"),
)
if mibBuilder.loadTexts:
    cfcCloneProfileEntry.setStatus("current")
_CfcCloneProfileId_Type = CloneProfileIdentifier
_CfcCloneProfileId_Object = MibTableColumn
cfcCloneProfileId = _CfcCloneProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 1),
    _CfcCloneProfileId_Type()
)
cfcCloneProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcCloneProfileId.setStatus("current")
_CfcCloneProfileStatus_Type = RowStatus
_CfcCloneProfileStatus_Object = MibTableColumn
cfcCloneProfileStatus = _CfcCloneProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 2),
    _CfcCloneProfileStatus_Type()
)
cfcCloneProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcCloneProfileStatus.setStatus("current")


class _CfcCloneProfileStorageType_Type(StorageType):
    """Custom type cfcCloneProfileStorageType based on StorageType"""


_CfcCloneProfileStorageType_Object = MibTableColumn
cfcCloneProfileStorageType = _CfcCloneProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 3),
    _CfcCloneProfileStorageType_Type()
)
cfcCloneProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcCloneProfileStorageType.setStatus("current")


class _CfcCloneProfileName_Type(SnmpAdminString):
    """Custom type cfcCloneProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CfcCloneProfileName_Type.__name__ = "SnmpAdminString"
_CfcCloneProfileName_Object = MibTableColumn
cfcCloneProfileName = _CfcCloneProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 4),
    _CfcCloneProfileName_Type()
)
cfcCloneProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcCloneProfileName.setStatus("current")
_CfcCloneProfileDescription_Type = SnmpAdminString
_CfcCloneProfileDescription_Object = MibTableColumn
cfcCloneProfileDescription = _CfcCloneProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 5),
    _CfcCloneProfileDescription_Type()
)
cfcCloneProfileDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcCloneProfileDescription.setStatus("current")
_CfcCloneProfileCreateTime_Type = TimeStamp
_CfcCloneProfileCreateTime_Object = MibTableColumn
cfcCloneProfileCreateTime = _CfcCloneProfileCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 6),
    _CfcCloneProfileCreateTime_Type()
)
cfcCloneProfileCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcCloneProfileCreateTime.setStatus("current")
_CfcCloneProfileFlowCount_Type = Gauge32
_CfcCloneProfileFlowCount_Object = MibTableColumn
cfcCloneProfileFlowCount = _CfcCloneProfileFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 7),
    _CfcCloneProfileFlowCount_Type()
)
cfcCloneProfileFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcCloneProfileFlowCount.setStatus("current")
if mibBuilder.loadTexts:
    cfcCloneProfileFlowCount.setUnits("traffic flows")


class _CfcCloneProfileFlowType_Type(Integer32):
    """Custom type cfcCloneProfileFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_CfcCloneProfileFlowType_Type.__name__ = "Integer32"
_CfcCloneProfileFlowType_Object = MibTableColumn
cfcCloneProfileFlowType = _CfcCloneProfileFlowType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 8),
    _CfcCloneProfileFlowType_Type()
)
cfcCloneProfileFlowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcCloneProfileFlowType.setStatus("current")


class _CfcCloneTargetType_Type(Integer32):
    """Custom type cfcCloneTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 3),
          ("other", 1),
          ("system", 2))
    )


_CfcCloneTargetType_Type.__name__ = "Integer32"
_CfcCloneTargetType_Object = MibTableColumn
cfcCloneTargetType = _CfcCloneTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 9),
    _CfcCloneTargetType_Type()
)
cfcCloneTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcCloneTargetType.setStatus("current")


class _CfcCloneTargetIfIndex_Type(Integer32):
    """Custom type cfcCloneTargetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CfcCloneTargetIfIndex_Type.__name__ = "Integer32"
_CfcCloneTargetIfIndex_Object = MibTableColumn
cfcCloneTargetIfIndex = _CfcCloneTargetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 10),
    _CfcCloneTargetIfIndex_Type()
)
cfcCloneTargetIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcCloneTargetIfIndex.setStatus("current")
_CfcCloneProfileEgressIfType_Type = CloneProfilePointType
_CfcCloneProfileEgressIfType_Object = MibTableColumn
cfcCloneProfileEgressIfType = _CfcCloneProfileEgressIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 11),
    _CfcCloneProfileEgressIfType_Type()
)
cfcCloneProfileEgressIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcCloneProfileEgressIfType.setStatus("current")
_CfcCloneProfileEgressIf_Type = CloneProfilePointIdentifier
_CfcCloneProfileEgressIf_Object = MibTableColumn
cfcCloneProfileEgressIf = _CfcCloneProfileEgressIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 12),
    _CfcCloneProfileEgressIf_Type()
)
cfcCloneProfileEgressIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcCloneProfileEgressIf.setStatus("current")
_CfcCloneProfileTableChanged_Type = TimeStamp
_CfcCloneProfileTableChanged_Object = MibScalar
cfcCloneProfileTableChanged = _CfcCloneProfileTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 3),
    _CfcCloneProfileTableChanged_Type()
)
cfcCloneProfileTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcCloneProfileTableChanged.setStatus("current")
_CfcFlows_ObjectIdentity = ObjectIdentity
cfcFlows = _CfcFlows_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2)
)
_CfcFlowIpTable_Object = MibTable
cfcFlowIpTable = _CfcFlowIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfcFlowIpTable.setStatus("current")
_CfcFlowIpEntry_Object = MibTableRow
cfcFlowIpEntry = _CfcFlowIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1)
)
cfcFlowIpEntry.setIndexNames(
    (0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"),
    (0, "CISCO-FLOW-CLONE-MIB", "cfcFlowIndex"),
)
if mibBuilder.loadTexts:
    cfcFlowIpEntry.setStatus("current")
_CfcFlowIndex_Type = CloneFlowIdentifier
_CfcFlowIndex_Object = MibTableColumn
cfcFlowIndex = _CfcFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 1),
    _CfcFlowIndex_Type()
)
cfcFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcFlowIndex.setStatus("current")
_CfcFlowIpStatus_Type = RowStatus
_CfcFlowIpStatus_Object = MibTableColumn
cfcFlowIpStatus = _CfcFlowIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 2),
    _CfcFlowIpStatus_Type()
)
cfcFlowIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcFlowIpStatus.setStatus("current")


class _CfcFlowIpStorageType_Type(StorageType):
    """Custom type cfcFlowIpStorageType based on StorageType"""


_CfcFlowIpStorageType_Object = MibTableColumn
cfcFlowIpStorageType = _CfcFlowIpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 3),
    _CfcFlowIpStorageType_Type()
)
cfcFlowIpStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcFlowIpStorageType.setStatus("current")
_CfcFlowIpAddrSrcType_Type = InetAddressType
_CfcFlowIpAddrSrcType_Object = MibTableColumn
cfcFlowIpAddrSrcType = _CfcFlowIpAddrSrcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 4),
    _CfcFlowIpAddrSrcType_Type()
)
cfcFlowIpAddrSrcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcFlowIpAddrSrcType.setStatus("current")
_CfcFlowIpAddrSrc_Type = InetAddress
_CfcFlowIpAddrSrc_Object = MibTableColumn
cfcFlowIpAddrSrc = _CfcFlowIpAddrSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 5),
    _CfcFlowIpAddrSrc_Type()
)
cfcFlowIpAddrSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcFlowIpAddrSrc.setStatus("current")
_CfcFlowIpAddrDstType_Type = InetAddressType
_CfcFlowIpAddrDstType_Object = MibTableColumn
cfcFlowIpAddrDstType = _CfcFlowIpAddrDstType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 6),
    _CfcFlowIpAddrDstType_Type()
)
cfcFlowIpAddrDstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcFlowIpAddrDstType.setStatus("current")
_CfcFlowIpAddrDst_Type = InetAddress
_CfcFlowIpAddrDst_Object = MibTableColumn
cfcFlowIpAddrDst = _CfcFlowIpAddrDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 7),
    _CfcFlowIpAddrDst_Type()
)
cfcFlowIpAddrDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcFlowIpAddrDst.setStatus("current")
_CfcFlowIpCreateTime_Type = TimeStamp
_CfcFlowIpCreateTime_Object = MibTableColumn
cfcFlowIpCreateTime = _CfcFlowIpCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 8),
    _CfcFlowIpCreateTime_Type()
)
cfcFlowIpCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFlowIpCreateTime.setStatus("current")
_CfcFlowStats_ObjectIdentity = ObjectIdentity
cfcFlowStats = _CfcFlowStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3)
)
_CfcFlowStatsTable_Object = MibTable
cfcFlowStatsTable = _CfcFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cfcFlowStatsTable.setStatus("current")
_CfcFlowStatsEntry_Object = MibTableRow
cfcFlowStatsEntry = _CfcFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1)
)
cfcFlowStatsEntry.setIndexNames(
    (0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"),
    (0, "CISCO-FLOW-CLONE-MIB", "cfcFlowIndex"),
)
if mibBuilder.loadTexts:
    cfcFlowStatsEntry.setStatus("current")
_CfcFlowPkts_Type = Counter64
_CfcFlowPkts_Object = MibTableColumn
cfcFlowPkts = _CfcFlowPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1, 1),
    _CfcFlowPkts_Type()
)
cfcFlowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFlowPkts.setStatus("current")
if mibBuilder.loadTexts:
    cfcFlowPkts.setUnits("packets")
_CfcFlowOctets_Type = Counter64
_CfcFlowOctets_Object = MibTableColumn
cfcFlowOctets = _CfcFlowOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1, 2),
    _CfcFlowOctets_Type()
)
cfcFlowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcFlowOctets.setStatus("current")
if mibBuilder.loadTexts:
    cfcFlowOctets.setUnits("octets")
_CiscoFlowCloneMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFlowCloneMIBConformance = _CiscoFlowCloneMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 2)
)
_CiscoFlowCloneMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFlowCloneMIBCompliances = _CiscoFlowCloneMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 1)
)
_CiscoFlowCloneMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFlowCloneMIBGroups = _CiscoFlowCloneMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2)
)

# Managed Objects groups

cfcCloneProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 1)
)
cfcCloneProfileGroup.setObjects(
      *(("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileIdNext"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileStatus"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileStorageType"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileName"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileDescription"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileCreateTime"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileFlowCount"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileFlowType"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneTargetType"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneTargetIfIndex"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileEgressIfType"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileEgressIf"),
        ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileTableChanged"))
)
if mibBuilder.loadTexts:
    cfcCloneProfileGroup.setStatus("current")

cfcFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 2)
)
cfcFlowGroup.setObjects(
      *(("CISCO-FLOW-CLONE-MIB", "cfcFlowIpStatus"),
        ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpStorageType"),
        ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrSrcType"),
        ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrSrc"),
        ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrDstType"),
        ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrDst"),
        ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpCreateTime"))
)
if mibBuilder.loadTexts:
    cfcFlowGroup.setStatus("current")

cfcFlowStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 3)
)
cfcFlowStatsGroup.setObjects(
      *(("CISCO-FLOW-CLONE-MIB", "cfcFlowPkts"),
        ("CISCO-FLOW-CLONE-MIB", "cfcFlowOctets"))
)
if mibBuilder.loadTexts:
    cfcFlowStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCloneFlowCompliance01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCloneFlowCompliance01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FLOW-CLONE-MIB",
    **{"CloneProfileIdentifier": CloneProfileIdentifier,
       "CloneFlowIdentifier": CloneFlowIdentifier,
       "CloneProfilePointType": CloneProfilePointType,
       "CloneProfilePointIdentifier": CloneProfilePointIdentifier,
       "ciscoFlowCloneMIB": ciscoFlowCloneMIB,
       "ciscoFlowCloneMIBNotifications": ciscoFlowCloneMIBNotifications,
       "ciscoFlowCloneMIBObjects": ciscoFlowCloneMIBObjects,
       "cfcCloneProfiles": cfcCloneProfiles,
       "cfcCloneProfileIdNext": cfcCloneProfileIdNext,
       "cfcCloneProfileTable": cfcCloneProfileTable,
       "cfcCloneProfileEntry": cfcCloneProfileEntry,
       "cfcCloneProfileId": cfcCloneProfileId,
       "cfcCloneProfileStatus": cfcCloneProfileStatus,
       "cfcCloneProfileStorageType": cfcCloneProfileStorageType,
       "cfcCloneProfileName": cfcCloneProfileName,
       "cfcCloneProfileDescription": cfcCloneProfileDescription,
       "cfcCloneProfileCreateTime": cfcCloneProfileCreateTime,
       "cfcCloneProfileFlowCount": cfcCloneProfileFlowCount,
       "cfcCloneProfileFlowType": cfcCloneProfileFlowType,
       "cfcCloneTargetType": cfcCloneTargetType,
       "cfcCloneTargetIfIndex": cfcCloneTargetIfIndex,
       "cfcCloneProfileEgressIfType": cfcCloneProfileEgressIfType,
       "cfcCloneProfileEgressIf": cfcCloneProfileEgressIf,
       "cfcCloneProfileTableChanged": cfcCloneProfileTableChanged,
       "cfcFlows": cfcFlows,
       "cfcFlowIpTable": cfcFlowIpTable,
       "cfcFlowIpEntry": cfcFlowIpEntry,
       "cfcFlowIndex": cfcFlowIndex,
       "cfcFlowIpStatus": cfcFlowIpStatus,
       "cfcFlowIpStorageType": cfcFlowIpStorageType,
       "cfcFlowIpAddrSrcType": cfcFlowIpAddrSrcType,
       "cfcFlowIpAddrSrc": cfcFlowIpAddrSrc,
       "cfcFlowIpAddrDstType": cfcFlowIpAddrDstType,
       "cfcFlowIpAddrDst": cfcFlowIpAddrDst,
       "cfcFlowIpCreateTime": cfcFlowIpCreateTime,
       "cfcFlowStats": cfcFlowStats,
       "cfcFlowStatsTable": cfcFlowStatsTable,
       "cfcFlowStatsEntry": cfcFlowStatsEntry,
       "cfcFlowPkts": cfcFlowPkts,
       "cfcFlowOctets": cfcFlowOctets,
       "ciscoFlowCloneMIBConformance": ciscoFlowCloneMIBConformance,
       "ciscoFlowCloneMIBCompliances": ciscoFlowCloneMIBCompliances,
       "ciscoCloneFlowCompliance01": ciscoCloneFlowCompliance01,
       "ciscoFlowCloneMIBGroups": ciscoFlowCloneMIBGroups,
       "cfcCloneProfileGroup": cfcCloneProfileGroup,
       "cfcFlowGroup": cfcFlowGroup,
       "cfcFlowStatsGroup": cfcFlowStatsGroup}
)
