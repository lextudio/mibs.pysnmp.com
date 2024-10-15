# SNMP MIB module (PNNI-MOB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PNNI-MOB-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:08 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PnniAtmAddr,
 PnniLevel,
 PnniNodeId,
 PnniNodeIndex,
 PnniPeerGroupId,
 pnniIfEntry,
 pnniNodeEntry,
 pnniNodeIndex) = mibBuilder.importSymbols(
    "PNNI-MIB",
    "PnniAtmAddr",
    "PnniLevel",
    "PnniNodeId",
    "PnniNodeIndex",
    "PnniPeerGroupId",
    "pnniIfEntry",
    "pnniNodeEntry",
    "pnniNodeIndex")

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

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pnniMobExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2)
)
pnniMobExtMIB.setRevisions(
        ("1999-02-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PnniOnhlIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfPnni_ObjectIdentity = ObjectIdentity
atmfPnni = _AtmfPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4)
)
_PnniMobExtMIBObjects_ObjectIdentity = ObjectIdentity
pnniMobExtMIBObjects = _PnniMobExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1)
)
_PnniMobExtBaseGroup_ObjectIdentity = ObjectIdentity
pnniMobExtBaseGroup = _PnniMobExtBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 1)
)


class _PnniMobExtVersion_Type(Integer32):
    """Custom type pnniMobExtVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("version1point0", 2))
    )


_PnniMobExtVersion_Type.__name__ = "Integer32"
_PnniMobExtVersion_Object = MibScalar
pnniMobExtVersion = _PnniMobExtVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 1, 1),
    _PnniMobExtVersion_Type()
)
pnniMobExtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMobExtVersion.setStatus("current")
_PnniMobileSwitchGroup_ObjectIdentity = ObjectIdentity
pnniMobileSwitchGroup = _PnniMobileSwitchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2)
)
_PnniMSMobileIfTable_Object = MibTable
pnniMSMobileIfTable = _PnniMSMobileIfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pnniMSMobileIfTable.setStatus("current")
_PnniMSMobileIfEntry_Object = MibTableRow
pnniMSMobileIfEntry = _PnniMSMobileIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pnniMSMobileIfEntry.setStatus("current")


class _PnniIfMobilityEnabled_Type(TruthValue):
    """Custom type pnniIfMobilityEnabled based on TruthValue"""


_PnniIfMobilityEnabled_Object = MibTableColumn
pnniIfMobilityEnabled = _PnniIfMobilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 1, 1, 1),
    _PnniIfMobilityEnabled_Type()
)
pnniIfMobilityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniIfMobilityEnabled.setStatus("current")
_PnniMSMobileLgnGroup_ObjectIdentity = ObjectIdentity
pnniMSMobileLgnGroup = _PnniMSMobileLgnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 2)
)
_PnniMobileLgnIndex_Type = PnniNodeIndex
_PnniMobileLgnIndex_Object = MibScalar
pnniMobileLgnIndex = _PnniMobileLgnIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 2, 1),
    _PnniMobileLgnIndex_Type()
)
pnniMobileLgnIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMobileLgnIndex.setStatus("current")
_PnniMobileLgnMinLevel_Type = PnniLevel
_PnniMobileLgnMinLevel_Object = MibScalar
pnniMobileLgnMinLevel = _PnniMobileLgnMinLevel_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 2, 2),
    _PnniMobileLgnMinLevel_Type()
)
pnniMobileLgnMinLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniMobileLgnMinLevel.setStatus("current")
_PnniMobileLgnMaxLevel_Type = PnniLevel
_PnniMobileLgnMaxLevel_Object = MibScalar
pnniMobileLgnMaxLevel = _PnniMobileLgnMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 2, 3),
    _PnniMobileLgnMaxLevel_Type()
)
pnniMobileLgnMaxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniMobileLgnMaxLevel.setStatus("current")
_PnniMSOnhlTable_Object = MibTable
pnniMSOnhlTable = _PnniMSOnhlTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pnniMSOnhlTable.setStatus("current")
_PnniMSOnhlEntry_Object = MibTableRow
pnniMSOnhlEntry = _PnniMSOnhlEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 3, 1)
)
pnniMSOnhlEntry.setIndexNames(
    (0, "PNNI-MOB-EXT-MIB", "pnniOnhlIndex"),
    (0, "PNNI-MOB-EXT-MIB", "pnniOnhlLevel"),
)
if mibBuilder.loadTexts:
    pnniMSOnhlEntry.setStatus("current")
_PnniOnhlIndex_Type = PnniOnhlIndex
_PnniOnhlIndex_Object = MibTableColumn
pnniOnhlIndex = _PnniOnhlIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 3, 1, 1),
    _PnniOnhlIndex_Type()
)
pnniOnhlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniOnhlIndex.setStatus("current")
_PnniOnhlLevel_Type = PnniLevel
_PnniOnhlLevel_Object = MibTableColumn
pnniOnhlLevel = _PnniOnhlLevel_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 3, 1, 2),
    _PnniOnhlLevel_Type()
)
pnniOnhlLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnniOnhlLevel.setStatus("current")
_PnniOnhlPeerGroupId_Type = PnniPeerGroupId
_PnniOnhlPeerGroupId_Object = MibTableColumn
pnniOnhlPeerGroupId = _PnniOnhlPeerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 3, 1, 3),
    _PnniOnhlPeerGroupId_Type()
)
pnniOnhlPeerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniOnhlPeerGroupId.setStatus("current")
_PnniOnhlNodeId_Type = PnniNodeId
_PnniOnhlNodeId_Object = MibTableColumn
pnniOnhlNodeId = _PnniOnhlNodeId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 3, 1, 4),
    _PnniOnhlNodeId_Type()
)
pnniOnhlNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniOnhlNodeId.setStatus("current")
_PnniOnhlAtmAddr_Type = PnniAtmAddr
_PnniOnhlAtmAddr_Object = MibTableColumn
pnniOnhlAtmAddr = _PnniOnhlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 3, 1, 5),
    _PnniOnhlAtmAddr_Type()
)
pnniOnhlAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniOnhlAtmAddr.setStatus("current")
_PnniMSNodeTable_Object = MibTable
pnniMSNodeTable = _PnniMSNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    pnniMSNodeTable.setStatus("current")
_PnniMSNodeEntry_Object = MibTableRow
pnniMSNodeEntry = _PnniMSNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    pnniMSNodeEntry.setStatus("current")
_PnniOutputOnhlIndex_Type = PnniOnhlIndex
_PnniOutputOnhlIndex_Object = MibTableColumn
pnniOutputOnhlIndex = _PnniOutputOnhlIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 4, 1, 1),
    _PnniOutputOnhlIndex_Type()
)
pnniOutputOnhlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniOutputOnhlIndex.setStatus("current")
_PnniOutputOnhlTimeStamp_Type = TimeStamp
_PnniOutputOnhlTimeStamp_Object = MibTableColumn
pnniOutputOnhlTimeStamp = _PnniOutputOnhlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 4, 1, 2),
    _PnniOutputOnhlTimeStamp_Type()
)
pnniOutputOnhlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniOutputOnhlTimeStamp.setStatus("current")
_PnniDecisionProcessTimeStamp_Type = TimeStamp
_PnniDecisionProcessTimeStamp_Object = MibTableColumn
pnniDecisionProcessTimeStamp = _PnniDecisionProcessTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 4, 1, 3),
    _PnniDecisionProcessTimeStamp_Type()
)
pnniDecisionProcessTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniDecisionProcessTimeStamp.setStatus("current")
_PnniDecisionProcessCount_Type = Counter32
_PnniDecisionProcessCount_Object = MibTableColumn
pnniDecisionProcessCount = _PnniDecisionProcessCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 4, 1, 4),
    _PnniDecisionProcessCount_Type()
)
pnniDecisionProcessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniDecisionProcessCount.setStatus("current")
_PnniMSInputOnhlTable_Object = MibTable
pnniMSInputOnhlTable = _PnniMSInputOnhlTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    pnniMSInputOnhlTable.setStatus("current")
_PnniMSInputOnhlEntry_Object = MibTableRow
pnniMSInputOnhlEntry = _PnniMSInputOnhlEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 5, 1)
)
pnniMSInputOnhlEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MOB-EXT-MIB", "pnniOnhlIndex"),
)
if mibBuilder.loadTexts:
    pnniMSInputOnhlEntry.setStatus("current")
_PnniInputOnhlTimeStamp_Type = TimeStamp
_PnniInputOnhlTimeStamp_Object = MibTableColumn
pnniInputOnhlTimeStamp = _PnniInputOnhlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 5, 1, 1),
    _PnniInputOnhlTimeStamp_Type()
)
pnniInputOnhlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniInputOnhlTimeStamp.setStatus("current")


class _PnniInputOnhlSourceType_Type(Integer32):
    """Custom type pnniInputOnhlSourceType based on Integer32"""
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
        *(("localNode", 3),
          ("mobileInterface", 1),
          ("nodalInformationGroup", 2),
          ("undefined", 0))
    )


_PnniInputOnhlSourceType_Type.__name__ = "Integer32"
_PnniInputOnhlSourceType_Object = MibTableColumn
pnniInputOnhlSourceType = _PnniInputOnhlSourceType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 5, 1, 2),
    _PnniInputOnhlSourceType_Type()
)
pnniInputOnhlSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniInputOnhlSourceType.setStatus("current")
_PnniInputOnhlNodeIdSource_Type = PnniNodeId
_PnniInputOnhlNodeIdSource_Object = MibTableColumn
pnniInputOnhlNodeIdSource = _PnniInputOnhlNodeIdSource_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 5, 1, 3),
    _PnniInputOnhlNodeIdSource_Type()
)
pnniInputOnhlNodeIdSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniInputOnhlNodeIdSource.setStatus("current")
_PnniInputOnhlMobileIfSource_Type = InterfaceIndex
_PnniInputOnhlMobileIfSource_Object = MibTableColumn
pnniInputOnhlMobileIfSource = _PnniInputOnhlMobileIfSource_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 5, 1, 4),
    _PnniInputOnhlMobileIfSource_Type()
)
pnniInputOnhlMobileIfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniInputOnhlMobileIfSource.setStatus("current")
_PnniInputOnhlNodeIndexSource_Type = PnniNodeIndex
_PnniInputOnhlNodeIndexSource_Object = MibTableColumn
pnniInputOnhlNodeIndexSource = _PnniInputOnhlNodeIndexSource_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 2, 5, 1, 5),
    _PnniInputOnhlNodeIndexSource_Type()
)
pnniInputOnhlNodeIndexSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnniInputOnhlNodeIndexSource.setStatus("current")
_PnniAccessPointGroup_ObjectIdentity = ObjectIdentity
pnniAccessPointGroup = _PnniAccessPointGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 3)
)
_PnniAPMobileIfTable_Object = MibTable
pnniAPMobileIfTable = _PnniAPMobileIfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pnniAPMobileIfTable.setStatus("current")
_PnniAPMobileIfEntry_Object = MibTableRow
pnniAPMobileIfEntry = _PnniAPMobileIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pnniAPMobileIfEntry.setStatus("current")


class _PnniAPMobileIfNhlLevelFilter_Type(PnniLevel):
    """Custom type pnniAPMobileIfNhlLevelFilter based on PnniLevel"""
    defaultValue = 0


_PnniAPMobileIfNhlLevelFilter_Object = MibTableColumn
pnniAPMobileIfNhlLevelFilter = _PnniAPMobileIfNhlLevelFilter_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 1, 3, 1, 1, 1),
    _PnniAPMobileIfNhlLevelFilter_Type()
)
pnniAPMobileIfNhlLevelFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pnniAPMobileIfNhlLevelFilter.setStatus("current")
_PnniMobExtMIBConformance_ObjectIdentity = ObjectIdentity
pnniMobExtMIBConformance = _PnniMobExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2)
)
_PnniMobExtMIBCompliances_ObjectIdentity = ObjectIdentity
pnniMobExtMIBCompliances = _PnniMobExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2, 1)
)
_PnniMobExtMIBGroups_ObjectIdentity = ObjectIdentity
pnniMobExtMIBGroups = _PnniMobExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2, 2)
)
pnniIfEntry.registerAugmentions(
    ("PNNI-MOB-EXT-MIB",
     "pnniMSMobileIfEntry")
)
pnniMSMobileIfEntry.setIndexNames(*pnniIfEntry.getIndexNames())
pnniNodeEntry.registerAugmentions(
    ("PNNI-MOB-EXT-MIB",
     "pnniMSNodeEntry")
)
pnniMSNodeEntry.setIndexNames(*pnniNodeEntry.getIndexNames())
pnniIfEntry.registerAugmentions(
    ("PNNI-MOB-EXT-MIB",
     "pnniAPMobileIfEntry")
)
pnniAPMobileIfEntry.setIndexNames(*pnniIfEntry.getIndexNames())

# Managed Objects groups

pnniMobExtMinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2, 2, 1)
)
pnniMobExtMinGroup.setObjects(
    ("PNNI-MOB-EXT-MIB", "pnniMobExtVersion")
)
if mibBuilder.loadTexts:
    pnniMobExtMinGroup.setStatus("current")

pnniIfMSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2, 2, 2)
)
pnniIfMSGroup.setObjects(
    ("PNNI-MOB-EXT-MIB", "pnniIfMobilityEnabled")
)
if mibBuilder.loadTexts:
    pnniIfMSGroup.setStatus("current")

pnniMobileLgnMSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2, 2, 3)
)
pnniMobileLgnMSGroup.setObjects(
      *(("PNNI-MOB-EXT-MIB", "pnniMobileLgnIndex"),
        ("PNNI-MOB-EXT-MIB", "pnniMobileLgnMinLevel"),
        ("PNNI-MOB-EXT-MIB", "pnniMobileLgnMaxLevel"))
)
if mibBuilder.loadTexts:
    pnniMobileLgnMSGroup.setStatus("current")

pnniOnhlMSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2, 2, 4)
)
pnniOnhlMSGroup.setObjects(
      *(("PNNI-MOB-EXT-MIB", "pnniOnhlNodeId"),
        ("PNNI-MOB-EXT-MIB", "pnniOnhlAtmAddr"),
        ("PNNI-MOB-EXT-MIB", "pnniOnhlPeerGroupId"))
)
if mibBuilder.loadTexts:
    pnniOnhlMSGroup.setStatus("current")

pnniNodeMSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2, 2, 5)
)
pnniNodeMSGroup.setObjects(
      *(("PNNI-MOB-EXT-MIB", "pnniOutputOnhlIndex"),
        ("PNNI-MOB-EXT-MIB", "pnniOutputOnhlTimeStamp"),
        ("PNNI-MOB-EXT-MIB", "pnniDecisionProcessTimeStamp"),
        ("PNNI-MOB-EXT-MIB", "pnniDecisionProcessCount"))
)
if mibBuilder.loadTexts:
    pnniNodeMSGroup.setStatus("current")

pnniInputOnhlMSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2, 2, 6)
)
pnniInputOnhlMSGroup.setObjects(
      *(("PNNI-MOB-EXT-MIB", "pnniInputOnhlTimeStamp"),
        ("PNNI-MOB-EXT-MIB", "pnniInputOnhlSourceType"),
        ("PNNI-MOB-EXT-MIB", "pnniInputOnhlNodeIdSource"),
        ("PNNI-MOB-EXT-MIB", "pnniInputOnhlMobileIfSource"),
        ("PNNI-MOB-EXT-MIB", "pnniInputOnhlNodeIndexSource"))
)
if mibBuilder.loadTexts:
    pnniInputOnhlMSGroup.setStatus("current")

pnniMobileIfAPOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2, 2, 7)
)
pnniMobileIfAPOptionalGroup.setObjects(
    ("PNNI-MOB-EXT-MIB", "pnniAPMobileIfNhlLevelFilter")
)
if mibBuilder.loadTexts:
    pnniMobileIfAPOptionalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pnniMobExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 4, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pnniMobExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PNNI-MOB-EXT-MIB",
    **{"PnniOnhlIndex": PnniOnhlIndex,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfPnni": atmfPnni,
       "pnniMobExtMIB": pnniMobExtMIB,
       "pnniMobExtMIBObjects": pnniMobExtMIBObjects,
       "pnniMobExtBaseGroup": pnniMobExtBaseGroup,
       "pnniMobExtVersion": pnniMobExtVersion,
       "pnniMobileSwitchGroup": pnniMobileSwitchGroup,
       "pnniMSMobileIfTable": pnniMSMobileIfTable,
       "pnniMSMobileIfEntry": pnniMSMobileIfEntry,
       "pnniIfMobilityEnabled": pnniIfMobilityEnabled,
       "pnniMSMobileLgnGroup": pnniMSMobileLgnGroup,
       "pnniMobileLgnIndex": pnniMobileLgnIndex,
       "pnniMobileLgnMinLevel": pnniMobileLgnMinLevel,
       "pnniMobileLgnMaxLevel": pnniMobileLgnMaxLevel,
       "pnniMSOnhlTable": pnniMSOnhlTable,
       "pnniMSOnhlEntry": pnniMSOnhlEntry,
       "pnniOnhlIndex": pnniOnhlIndex,
       "pnniOnhlLevel": pnniOnhlLevel,
       "pnniOnhlPeerGroupId": pnniOnhlPeerGroupId,
       "pnniOnhlNodeId": pnniOnhlNodeId,
       "pnniOnhlAtmAddr": pnniOnhlAtmAddr,
       "pnniMSNodeTable": pnniMSNodeTable,
       "pnniMSNodeEntry": pnniMSNodeEntry,
       "pnniOutputOnhlIndex": pnniOutputOnhlIndex,
       "pnniOutputOnhlTimeStamp": pnniOutputOnhlTimeStamp,
       "pnniDecisionProcessTimeStamp": pnniDecisionProcessTimeStamp,
       "pnniDecisionProcessCount": pnniDecisionProcessCount,
       "pnniMSInputOnhlTable": pnniMSInputOnhlTable,
       "pnniMSInputOnhlEntry": pnniMSInputOnhlEntry,
       "pnniInputOnhlTimeStamp": pnniInputOnhlTimeStamp,
       "pnniInputOnhlSourceType": pnniInputOnhlSourceType,
       "pnniInputOnhlNodeIdSource": pnniInputOnhlNodeIdSource,
       "pnniInputOnhlMobileIfSource": pnniInputOnhlMobileIfSource,
       "pnniInputOnhlNodeIndexSource": pnniInputOnhlNodeIndexSource,
       "pnniAccessPointGroup": pnniAccessPointGroup,
       "pnniAPMobileIfTable": pnniAPMobileIfTable,
       "pnniAPMobileIfEntry": pnniAPMobileIfEntry,
       "pnniAPMobileIfNhlLevelFilter": pnniAPMobileIfNhlLevelFilter,
       "pnniMobExtMIBConformance": pnniMobExtMIBConformance,
       "pnniMobExtMIBCompliances": pnniMobExtMIBCompliances,
       "pnniMobExtMIBCompliance": pnniMobExtMIBCompliance,
       "pnniMobExtMIBGroups": pnniMobExtMIBGroups,
       "pnniMobExtMinGroup": pnniMobExtMinGroup,
       "pnniIfMSGroup": pnniIfMSGroup,
       "pnniMobileLgnMSGroup": pnniMobileLgnMSGroup,
       "pnniOnhlMSGroup": pnniOnhlMSGroup,
       "pnniNodeMSGroup": pnniNodeMSGroup,
       "pnniInputOnhlMSGroup": pnniInputOnhlMSGroup,
       "pnniMobileIfAPOptionalGroup": pnniMobileIfAPOptionalGroup}
)
