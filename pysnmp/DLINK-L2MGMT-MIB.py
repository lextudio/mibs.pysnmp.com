# SNMP MIB module (DLINK-L2MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-L2MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:48 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swDlinkL2Mgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 2)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_SwPortTrunkPackage_ObjectIdentity = ObjectIdentity
swPortTrunkPackage = _SwPortTrunkPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 1)
)
_SwPortTrunkMaxEntries_Type = Integer32
_SwPortTrunkMaxEntries_Object = MibScalar
swPortTrunkMaxEntries = _SwPortTrunkMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 1, 1),
    _SwPortTrunkMaxEntries_Type()
)
swPortTrunkMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMaxEntries.setStatus("current")
_SwPortTrunkMaxPortMembers_Type = Integer32
_SwPortTrunkMaxPortMembers_Object = MibScalar
swPortTrunkMaxPortMembers = _SwPortTrunkMaxPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 1, 2),
    _SwPortTrunkMaxPortMembers_Type()
)
swPortTrunkMaxPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMaxPortMembers.setStatus("current")
_SwPortTrunkTable_Object = MibTable
swPortTrunkTable = _SwPortTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 1, 3)
)
if mibBuilder.loadTexts:
    swPortTrunkTable.setStatus("current")
_SwPortTrunkEntry_Object = MibTableRow
swPortTrunkEntry = _SwPortTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 1, 3, 1)
)
swPortTrunkEntry.setIndexNames(
    (0, "DLINK-L2MGMT-MIB", "swPortTrunkIndex"),
)
if mibBuilder.loadTexts:
    swPortTrunkEntry.setStatus("current")
_SwPortTrunkIndex_Type = Integer32
_SwPortTrunkIndex_Object = MibTableColumn
swPortTrunkIndex = _SwPortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 1, 3, 1, 1),
    _SwPortTrunkIndex_Type()
)
swPortTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkIndex.setStatus("current")


class _SwPortTrunkName_Type(DisplayString):
    """Custom type swPortTrunkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwPortTrunkName_Type.__name__ = "DisplayString"
_SwPortTrunkName_Object = MibTableColumn
swPortTrunkName = _SwPortTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 1, 3, 1, 2),
    _SwPortTrunkName_Type()
)
swPortTrunkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkName.setStatus("current")
_SwPortTrunkMasterPort_Type = Integer32
_SwPortTrunkMasterPort_Object = MibTableColumn
swPortTrunkMasterPort = _SwPortTrunkMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 1, 3, 1, 3),
    _SwPortTrunkMasterPort_Type()
)
swPortTrunkMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMasterPort.setStatus("current")
_SwPortTrunkPortList_Type = PortList
_SwPortTrunkPortList_Object = MibTableColumn
swPortTrunkPortList = _SwPortTrunkPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 1, 3, 1, 4),
    _SwPortTrunkPortList_Type()
)
swPortTrunkPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkPortList.setStatus("current")
_SwPortTrunkState_Type = RowStatus
_SwPortTrunkState_Object = MibTableColumn
swPortTrunkState = _SwPortTrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 1, 3, 1, 5),
    _SwPortTrunkState_Type()
)
swPortTrunkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkState.setStatus("current")
_SwPortMirrorPackage_ObjectIdentity = ObjectIdentity
swPortMirrorPackage = _SwPortMirrorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 2)
)
_SwPortMirrorMaxEntries_Type = Integer32
_SwPortMirrorMaxEntries_Object = MibScalar
swPortMirrorMaxEntries = _SwPortMirrorMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 2, 1),
    _SwPortMirrorMaxEntries_Type()
)
swPortMirrorMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortMirrorMaxEntries.setStatus("current")
_SwPortMirrorCtrlTable_Object = MibTable
swPortMirrorCtrlTable = _SwPortMirrorCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 2, 2)
)
if mibBuilder.loadTexts:
    swPortMirrorCtrlTable.setStatus("current")
_SwPortMirrorCtrlEntry_Object = MibTableRow
swPortMirrorCtrlEntry = _SwPortMirrorCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 2, 2, 1)
)
swPortMirrorCtrlEntry.setIndexNames(
    (0, "DLINK-L2MGMT-MIB", "swPortMirrorIndex"),
)
if mibBuilder.loadTexts:
    swPortMirrorCtrlEntry.setStatus("current")
_SwPortMirrorIndex_Type = Integer32
_SwPortMirrorIndex_Object = MibTableColumn
swPortMirrorIndex = _SwPortMirrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 2, 2, 1, 1),
    _SwPortMirrorIndex_Type()
)
swPortMirrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortMirrorIndex.setStatus("current")
_SwPortMirrorSourcePort_Type = Integer32
_SwPortMirrorSourcePort_Object = MibTableColumn
swPortMirrorSourcePort = _SwPortMirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 2, 2, 1, 2),
    _SwPortMirrorSourcePort_Type()
)
swPortMirrorSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortMirrorSourcePort.setStatus("current")
_SwPortMirrorTargetPort_Type = Integer32
_SwPortMirrorTargetPort_Object = MibTableColumn
swPortMirrorTargetPort = _SwPortMirrorTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 2, 2, 1, 3),
    _SwPortMirrorTargetPort_Type()
)
swPortMirrorTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortMirrorTargetPort.setStatus("current")


class _SwPortMirrorDirection_Type(Integer32):
    """Custom type swPortMirrorDirection based on Integer32"""
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
        *(("both", 4),
          ("egress", 3),
          ("ingress", 2),
          ("other", 1))
    )


_SwPortMirrorDirection_Type.__name__ = "Integer32"
_SwPortMirrorDirection_Object = MibTableColumn
swPortMirrorDirection = _SwPortMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 2, 2, 1, 4),
    _SwPortMirrorDirection_Type()
)
swPortMirrorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortMirrorDirection.setStatus("current")
_SwPortMirrorState_Type = RowStatus
_SwPortMirrorState_Object = MibTableColumn
swPortMirrorState = _SwPortMirrorState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 2, 2, 1, 5),
    _SwPortMirrorState_Type()
)
swPortMirrorState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortMirrorState.setStatus("current")
_SwIGMPPackage_ObjectIdentity = ObjectIdentity
swIGMPPackage = _SwIGMPPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3)
)


class _SwIGMPCtrlStatus_Type(Integer32):
    """Custom type swIGMPCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwIGMPCtrlStatus_Type.__name__ = "Integer32"
_SwIGMPCtrlStatus_Object = MibScalar
swIGMPCtrlStatus = _SwIGMPCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 1),
    _SwIGMPCtrlStatus_Type()
)
swIGMPCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPCtrlStatus.setStatus("current")
_SwIGMPCtrlMaxEntries_Type = Integer32
_SwIGMPCtrlMaxEntries_Object = MibScalar
swIGMPCtrlMaxEntries = _SwIGMPCtrlMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 2),
    _SwIGMPCtrlMaxEntries_Type()
)
swIGMPCtrlMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPCtrlMaxEntries.setStatus("current")
_SwIGMPCtrlTable_Object = MibTable
swIGMPCtrlTable = _SwIGMPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 3)
)
if mibBuilder.loadTexts:
    swIGMPCtrlTable.setStatus("current")
_SwIGMPCtrlEntry_Object = MibTableRow
swIGMPCtrlEntry = _SwIGMPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 3, 1)
)
swIGMPCtrlEntry.setIndexNames(
    (0, "DLINK-L2MGMT-MIB", "swIGMPCtrlVid"),
)
if mibBuilder.loadTexts:
    swIGMPCtrlEntry.setStatus("current")
_SwIGMPCtrlVid_Type = Integer32
_SwIGMPCtrlVid_Object = MibTableColumn
swIGMPCtrlVid = _SwIGMPCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 3, 1, 1),
    _SwIGMPCtrlVid_Type()
)
swIGMPCtrlVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIGMPCtrlVid.setStatus("current")


class _SwIGMPQueryInterval_Type(Integer32):
    """Custom type swIGMPQueryInterval based on Integer32"""
    defaultValue = 125


_SwIGMPQueryInterval_Object = MibTableColumn
swIGMPQueryInterval = _SwIGMPQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 3, 1, 2),
    _SwIGMPQueryInterval_Type()
)
swIGMPQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIGMPQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    swIGMPQueryInterval.setUnits("seconds")


class _SwIGMPQueryMaxResponseTime_Type(Integer32):
    """Custom type swIGMPQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SwIGMPQueryMaxResponseTime_Type.__name__ = "Integer32"
_SwIGMPQueryMaxResponseTime_Object = MibTableColumn
swIGMPQueryMaxResponseTime = _SwIGMPQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 3, 1, 3),
    _SwIGMPQueryMaxResponseTime_Type()
)
swIGMPQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIGMPQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    swIGMPQueryMaxResponseTime.setUnits("seconds")


class _SwIGMPRobustness_Type(Integer32):
    """Custom type swIGMPRobustness based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwIGMPRobustness_Type.__name__ = "Integer32"
_SwIGMPRobustness_Object = MibTableColumn
swIGMPRobustness = _SwIGMPRobustness_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 3, 1, 4),
    _SwIGMPRobustness_Type()
)
swIGMPRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIGMPRobustness.setStatus("current")


class _SwIGMPCtrlTimer_Type(Integer32):
    """Custom type swIGMPCtrlTimer based on Integer32"""
    defaultValue = 300


_SwIGMPCtrlTimer_Object = MibTableColumn
swIGMPCtrlTimer = _SwIGMPCtrlTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 3, 1, 5),
    _SwIGMPCtrlTimer_Type()
)
swIGMPCtrlTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPCtrlTimer.setStatus("current")


class _SwIGMPQuerierVersion_Type(Integer32):
    """Custom type swIGMPQuerierVersion based on Integer32"""
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
        *(("other", 1),
          ("v0Querier", 2),
          ("v1Querier", 3),
          ("v2Querier", 4))
    )


_SwIGMPQuerierVersion_Type.__name__ = "Integer32"
_SwIGMPQuerierVersion_Object = MibTableColumn
swIGMPQuerierVersion = _SwIGMPQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 3, 1, 6),
    _SwIGMPQuerierVersion_Type()
)
swIGMPQuerierVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIGMPQuerierVersion.setStatus("current")
_SwIGMPCtrlState_Type = RowStatus
_SwIGMPCtrlState_Object = MibTableColumn
swIGMPCtrlState = _SwIGMPCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 3, 1, 7),
    _SwIGMPCtrlState_Type()
)
swIGMPCtrlState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIGMPCtrlState.setStatus("current")
_SwIGMPIfnoMaxEntries_Type = Integer32
_SwIGMPIfnoMaxEntries_Object = MibScalar
swIGMPIfnoMaxEntries = _SwIGMPIfnoMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 4),
    _SwIGMPIfnoMaxEntries_Type()
)
swIGMPIfnoMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPIfnoMaxEntries.setStatus("current")
_SwIGMPInfoTable_Object = MibTable
swIGMPInfoTable = _SwIGMPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 5)
)
if mibBuilder.loadTexts:
    swIGMPInfoTable.setStatus("current")
_SwIGMPInfoEntry_Object = MibTableRow
swIGMPInfoEntry = _SwIGMPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 5, 1)
)
swIGMPInfoEntry.setIndexNames(
    (0, "DLINK-L2MGMT-MIB", "swIGMPInfoVid"),
)
if mibBuilder.loadTexts:
    swIGMPInfoEntry.setStatus("current")
_SwIGMPInfoVid_Type = Integer32
_SwIGMPInfoVid_Object = MibTableColumn
swIGMPInfoVid = _SwIGMPInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 5, 1, 1),
    _SwIGMPInfoVid_Type()
)
swIGMPInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoVid.setStatus("current")
_SwIGMPInfoQueryCount_Type = Integer32
_SwIGMPInfoQueryCount_Object = MibTableColumn
swIGMPInfoQueryCount = _SwIGMPInfoQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 5, 1, 2),
    _SwIGMPInfoQueryCount_Type()
)
swIGMPInfoQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoQueryCount.setStatus("current")
_SwIGMPInfoTxQueryCount_Type = Integer32
_SwIGMPInfoTxQueryCount_Object = MibTableColumn
swIGMPInfoTxQueryCount = _SwIGMPInfoTxQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 5, 1, 3),
    _SwIGMPInfoTxQueryCount_Type()
)
swIGMPInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoTxQueryCount.setStatus("current")
_SwIGMPTableMaxEntries_Type = Integer32
_SwIGMPTableMaxEntries_Object = MibScalar
swIGMPTableMaxEntries = _SwIGMPTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 6),
    _SwIGMPTableMaxEntries_Type()
)
swIGMPTableMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPTableMaxEntries.setStatus("current")
_SwIGMPTable_Object = MibTable
swIGMPTable = _SwIGMPTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 7)
)
if mibBuilder.loadTexts:
    swIGMPTable.setStatus("current")
_SwIGMPEntry_Object = MibTableRow
swIGMPEntry = _SwIGMPEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 7, 1)
)
swIGMPEntry.setIndexNames(
    (0, "DLINK-L2MGMT-MIB", "swIGMPVid"),
    (0, "DLINK-L2MGMT-MIB", "swIGMPGroupIpAddr"),
)
if mibBuilder.loadTexts:
    swIGMPEntry.setStatus("current")
_SwIGMPVid_Type = Integer32
_SwIGMPVid_Object = MibTableColumn
swIGMPVid = _SwIGMPVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 7, 1, 1),
    _SwIGMPVid_Type()
)
swIGMPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPVid.setStatus("current")
_SwIGMPGroupIpAddr_Type = IpAddress
_SwIGMPGroupIpAddr_Object = MibTableColumn
swIGMPGroupIpAddr = _SwIGMPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 7, 1, 2),
    _SwIGMPGroupIpAddr_Type()
)
swIGMPGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPGroupIpAddr.setStatus("current")
_SwIGMPMacAddr_Type = MacAddress
_SwIGMPMacAddr_Object = MibTableColumn
swIGMPMacAddr = _SwIGMPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 7, 1, 3),
    _SwIGMPMacAddr_Type()
)
swIGMPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPMacAddr.setStatus("current")
_SwIGMPPortMap_Type = PortList
_SwIGMPPortMap_Object = MibTableColumn
swIGMPPortMap = _SwIGMPPortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 7, 1, 4),
    _SwIGMPPortMap_Type()
)
swIGMPPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPPortMap.setStatus("current")
_SwIGMPIpGroupReportCount_Type = Integer32
_SwIGMPIpGroupReportCount_Object = MibTableColumn
swIGMPIpGroupReportCount = _SwIGMPIpGroupReportCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 2, 3, 7, 1, 5),
    _SwIGMPIpGroupReportCount_Type()
)
swIGMPIpGroupReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPIpGroupReportCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-L2MGMT-MIB",
    **{"MacAddress": MacAddress,
       "PortList": PortList,
       "swDlinkL2Mgmt": swDlinkL2Mgmt,
       "swPortTrunkPackage": swPortTrunkPackage,
       "swPortTrunkMaxEntries": swPortTrunkMaxEntries,
       "swPortTrunkMaxPortMembers": swPortTrunkMaxPortMembers,
       "swPortTrunkTable": swPortTrunkTable,
       "swPortTrunkEntry": swPortTrunkEntry,
       "swPortTrunkIndex": swPortTrunkIndex,
       "swPortTrunkName": swPortTrunkName,
       "swPortTrunkMasterPort": swPortTrunkMasterPort,
       "swPortTrunkPortList": swPortTrunkPortList,
       "swPortTrunkState": swPortTrunkState,
       "swPortMirrorPackage": swPortMirrorPackage,
       "swPortMirrorMaxEntries": swPortMirrorMaxEntries,
       "swPortMirrorCtrlTable": swPortMirrorCtrlTable,
       "swPortMirrorCtrlEntry": swPortMirrorCtrlEntry,
       "swPortMirrorIndex": swPortMirrorIndex,
       "swPortMirrorSourcePort": swPortMirrorSourcePort,
       "swPortMirrorTargetPort": swPortMirrorTargetPort,
       "swPortMirrorDirection": swPortMirrorDirection,
       "swPortMirrorState": swPortMirrorState,
       "swIGMPPackage": swIGMPPackage,
       "swIGMPCtrlStatus": swIGMPCtrlStatus,
       "swIGMPCtrlMaxEntries": swIGMPCtrlMaxEntries,
       "swIGMPCtrlTable": swIGMPCtrlTable,
       "swIGMPCtrlEntry": swIGMPCtrlEntry,
       "swIGMPCtrlVid": swIGMPCtrlVid,
       "swIGMPQueryInterval": swIGMPQueryInterval,
       "swIGMPQueryMaxResponseTime": swIGMPQueryMaxResponseTime,
       "swIGMPRobustness": swIGMPRobustness,
       "swIGMPCtrlTimer": swIGMPCtrlTimer,
       "swIGMPQuerierVersion": swIGMPQuerierVersion,
       "swIGMPCtrlState": swIGMPCtrlState,
       "swIGMPIfnoMaxEntries": swIGMPIfnoMaxEntries,
       "swIGMPInfoTable": swIGMPInfoTable,
       "swIGMPInfoEntry": swIGMPInfoEntry,
       "swIGMPInfoVid": swIGMPInfoVid,
       "swIGMPInfoQueryCount": swIGMPInfoQueryCount,
       "swIGMPInfoTxQueryCount": swIGMPInfoTxQueryCount,
       "swIGMPTableMaxEntries": swIGMPTableMaxEntries,
       "swIGMPTable": swIGMPTable,
       "swIGMPEntry": swIGMPEntry,
       "swIGMPVid": swIGMPVid,
       "swIGMPGroupIpAddr": swIGMPGroupIpAddr,
       "swIGMPMacAddr": swIGMPMacAddr,
       "swIGMPPortMap": swIGMPPortMap,
       "swIGMPIpGroupReportCount": swIGMPIpGroupReportCount}
)
