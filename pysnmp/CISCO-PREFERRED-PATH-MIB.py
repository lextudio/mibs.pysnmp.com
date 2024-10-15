# SNMP MIB module (CISCO-PREFERRED-PATH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PREFERRED-PATH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:04 2024
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

(FcAddressId,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddressId",
    "VsanIndex")

(notifyVsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "notifyVsanIndex")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

ciscoPrefPathMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 592)
)
ciscoPrefPathMIB.setRevisions(
        ("2006-10-26 14:44",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoPrefPathFcAddrMask(Integer32, TextualConvention):
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
        *(("domain", 3),
          ("domainArea", 2),
          ("full", 1),
          ("noMask", 4))
    )



class CiscoPrefPathStatus(Integer32, TextualConvention):
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
        *(("active", 2),
          ("changed", 5),
          ("deleted", 4),
          ("pending", 3),
          ("unknown", 1))
    )



class CiscoPrefPathIvrNextHopVsanId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )



class CiscoPrefPathPreferenceLevel(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPrefPathMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPrefPathMIBNotifs = _CiscoPrefPathMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 0)
)
_CiscoPrefPathMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPrefPathMIBObjects = _CiscoPrefPathMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1)
)
_CiscoPrefPathConfiguration_ObjectIdentity = ObjectIdentity
ciscoPrefPathConfiguration = _CiscoPrefPathConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1)
)
_CPrefPathRouteMapTable_Object = MibTable
cPrefPathRouteMapTable = _CPrefPathRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapTable.setStatus("current")
_CPrefPathRouteMapEntry_Object = MibTableRow
cPrefPathRouteMapEntry = _CPrefPathRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1)
)
cPrefPathRouteMapEntry.setIndexNames(
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"),
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapEntry.setStatus("current")
_CPrefPathRouteMapVsanIndex_Type = VsanIndex
_CPrefPathRouteMapVsanIndex_Object = MibTableColumn
cPrefPathRouteMapVsanIndex = _CPrefPathRouteMapVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 1),
    _CPrefPathRouteMapVsanIndex_Type()
)
cPrefPathRouteMapVsanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPrefPathRouteMapVsanIndex.setStatus("current")


class _CPrefPathRouteMapRouteIndex_Type(Unsigned32):
    """Custom type cPrefPathRouteMapRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CPrefPathRouteMapRouteIndex_Type.__name__ = "Unsigned32"
_CPrefPathRouteMapRouteIndex_Object = MibTableColumn
cPrefPathRouteMapRouteIndex = _CPrefPathRouteMapRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 2),
    _CPrefPathRouteMapRouteIndex_Type()
)
cPrefPathRouteMapRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPrefPathRouteMapRouteIndex.setStatus("current")


class _CPrefPathRouteMapIntfPrefStrict_Type(TruthValue):
    """Custom type cPrefPathRouteMapIntfPrefStrict based on TruthValue"""


_CPrefPathRouteMapIntfPrefStrict_Object = MibTableColumn
cPrefPathRouteMapIntfPrefStrict = _CPrefPathRouteMapIntfPrefStrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 3),
    _CPrefPathRouteMapIntfPrefStrict_Type()
)
cPrefPathRouteMapIntfPrefStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPrefPathRouteMapIntfPrefStrict.setStatus("current")


class _CPrefPathRouteMapRouteActive_Type(TruthValue):
    """Custom type cPrefPathRouteMapRouteActive based on TruthValue"""


_CPrefPathRouteMapRouteActive_Object = MibTableColumn
cPrefPathRouteMapRouteActive = _CPrefPathRouteMapRouteActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 4),
    _CPrefPathRouteMapRouteActive_Type()
)
cPrefPathRouteMapRouteActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPrefPathRouteMapRouteActive.setStatus("current")


class _CPrefPathRouteMapActive_Type(TruthValue):
    """Custom type cPrefPathRouteMapActive based on TruthValue"""


_CPrefPathRouteMapActive_Object = MibTableColumn
cPrefPathRouteMapActive = _CPrefPathRouteMapActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 5),
    _CPrefPathRouteMapActive_Type()
)
cPrefPathRouteMapActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPrefPathRouteMapActive.setStatus("deprecated")


class _CPrefPathRouteMapStorageType_Type(StorageType):
    """Custom type cPrefPathRouteMapStorageType based on StorageType"""


_CPrefPathRouteMapStorageType_Object = MibTableColumn
cPrefPathRouteMapStorageType = _CPrefPathRouteMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 6),
    _CPrefPathRouteMapStorageType_Type()
)
cPrefPathRouteMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPrefPathRouteMapStorageType.setStatus("current")
_CPrefPathRouteMapRowStatus_Type = RowStatus
_CPrefPathRouteMapRowStatus_Object = MibTableColumn
cPrefPathRouteMapRowStatus = _CPrefPathRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 1, 1, 7),
    _CPrefPathRouteMapRowStatus_Type()
)
cPrefPathRouteMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPrefPathRouteMapRowStatus.setStatus("current")
_CPrefPathRouteMapGlobalTable_Object = MibTable
cPrefPathRouteMapGlobalTable = _CPrefPathRouteMapGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapGlobalTable.setStatus("current")
_CPrefPathRouteMapGlobalEntry_Object = MibTableRow
cPrefPathRouteMapGlobalEntry = _CPrefPathRouteMapGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 2, 1)
)
cPrefPathRouteMapGlobalEntry.setIndexNames(
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"),
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapGlobalEntry.setStatus("current")


class _CPrefPathRouteMapGlobalActive_Type(Integer32):
    """Custom type cPrefPathRouteMapGlobalActive based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("none", 3),
          ("partial", 2))
    )


_CPrefPathRouteMapGlobalActive_Type.__name__ = "Integer32"
_CPrefPathRouteMapGlobalActive_Object = MibTableColumn
cPrefPathRouteMapGlobalActive = _CPrefPathRouteMapGlobalActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 2, 1, 1),
    _CPrefPathRouteMapGlobalActive_Type()
)
cPrefPathRouteMapGlobalActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPrefPathRouteMapGlobalActive.setStatus("current")
_CPrefPathRouteMapMatchTable_Object = MibTable
cPrefPathRouteMapMatchTable = _CPrefPathRouteMapMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapMatchTable.setStatus("current")
_CPrefPathRouteMapMatchEntry_Object = MibTableRow
cPrefPathRouteMapMatchEntry = _CPrefPathRouteMapMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1)
)
cPrefPathRouteMapMatchEntry.setIndexNames(
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcAddr"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcAddrMask"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcIntf"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchDstAddr"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchDstAddrMask"),
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapMatchEntry.setStatus("current")
_CPrefPathRMapMatchSrcAddr_Type = FcAddressId
_CPrefPathRMapMatchSrcAddr_Object = MibTableColumn
cPrefPathRMapMatchSrcAddr = _CPrefPathRMapMatchSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 1),
    _CPrefPathRMapMatchSrcAddr_Type()
)
cPrefPathRMapMatchSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPrefPathRMapMatchSrcAddr.setStatus("current")
_CPrefPathRMapMatchSrcAddrMask_Type = CiscoPrefPathFcAddrMask
_CPrefPathRMapMatchSrcAddrMask_Object = MibTableColumn
cPrefPathRMapMatchSrcAddrMask = _CPrefPathRMapMatchSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 2),
    _CPrefPathRMapMatchSrcAddrMask_Type()
)
cPrefPathRMapMatchSrcAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPrefPathRMapMatchSrcAddrMask.setStatus("current")
_CPrefPathRMapMatchSrcIntf_Type = InterfaceIndexOrZero
_CPrefPathRMapMatchSrcIntf_Object = MibTableColumn
cPrefPathRMapMatchSrcIntf = _CPrefPathRMapMatchSrcIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 3),
    _CPrefPathRMapMatchSrcIntf_Type()
)
cPrefPathRMapMatchSrcIntf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPrefPathRMapMatchSrcIntf.setStatus("current")
_CPrefPathRMapMatchDstAddr_Type = FcAddressId
_CPrefPathRMapMatchDstAddr_Object = MibTableColumn
cPrefPathRMapMatchDstAddr = _CPrefPathRMapMatchDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 4),
    _CPrefPathRMapMatchDstAddr_Type()
)
cPrefPathRMapMatchDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPrefPathRMapMatchDstAddr.setStatus("current")
_CPrefPathRMapMatchDstAddrMask_Type = CiscoPrefPathFcAddrMask
_CPrefPathRMapMatchDstAddrMask_Object = MibTableColumn
cPrefPathRMapMatchDstAddrMask = _CPrefPathRMapMatchDstAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 5),
    _CPrefPathRMapMatchDstAddrMask_Type()
)
cPrefPathRMapMatchDstAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPrefPathRMapMatchDstAddrMask.setStatus("current")
_CPrefPathRMapMatchRowStatus_Type = RowStatus
_CPrefPathRMapMatchRowStatus_Object = MibTableColumn
cPrefPathRMapMatchRowStatus = _CPrefPathRMapMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 3, 1, 6),
    _CPrefPathRMapMatchRowStatus_Type()
)
cPrefPathRMapMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPrefPathRMapMatchRowStatus.setStatus("current")
_CPrefPathRouteMapSetTable_Object = MibTable
cPrefPathRouteMapSetTable = _CPrefPathRouteMapSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapSetTable.setStatus("current")
_CPrefPathRouteMapSetEntry_Object = MibTableRow
cPrefPathRouteMapSetEntry = _CPrefPathRouteMapSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4, 1)
)
cPrefPathRouteMapSetEntry.setIndexNames(
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIntfPref"),
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapSetEntry.setStatus("current")
_CPrefPathRMapSetIntfPref_Type = CiscoPrefPathPreferenceLevel
_CPrefPathRMapSetIntfPref_Object = MibTableColumn
cPrefPathRMapSetIntfPref = _CPrefPathRMapSetIntfPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4, 1, 1),
    _CPrefPathRMapSetIntfPref_Type()
)
cPrefPathRMapSetIntfPref.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPrefPathRMapSetIntfPref.setStatus("current")
_CPrefPathRMapSetIntf_Type = InterfaceIndex
_CPrefPathRMapSetIntf_Object = MibTableColumn
cPrefPathRMapSetIntf = _CPrefPathRMapSetIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4, 1, 2),
    _CPrefPathRMapSetIntf_Type()
)
cPrefPathRMapSetIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPrefPathRMapSetIntf.setStatus("current")


class _CPrefPathRMapSetIvrNextHopVsanId_Type(CiscoPrefPathIvrNextHopVsanId):
    """Custom type cPrefPathRMapSetIvrNextHopVsanId based on CiscoPrefPathIvrNextHopVsanId"""
    defaultValue = 0


_CPrefPathRMapSetIvrNextHopVsanId_Object = MibTableColumn
cPrefPathRMapSetIvrNextHopVsanId = _CPrefPathRMapSetIvrNextHopVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4, 1, 3),
    _CPrefPathRMapSetIvrNextHopVsanId_Type()
)
cPrefPathRMapSetIvrNextHopVsanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPrefPathRMapSetIvrNextHopVsanId.setStatus("current")
_CPrefPathRMapSetRowStatus_Type = RowStatus
_CPrefPathRMapSetRowStatus_Object = MibTableColumn
cPrefPathRMapSetRowStatus = _CPrefPathRMapSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 4, 1, 4),
    _CPrefPathRMapSetRowStatus_Type()
)
cPrefPathRMapSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPrefPathRMapSetRowStatus.setStatus("current")
_CPrefPathHwFailureNotifEnable_Type = TruthValue
_CPrefPathHwFailureNotifEnable_Object = MibScalar
cPrefPathHwFailureNotifEnable = _CPrefPathHwFailureNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 1, 5),
    _CPrefPathHwFailureNotifEnable_Type()
)
cPrefPathHwFailureNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cPrefPathHwFailureNotifEnable.setStatus("current")
_CiscoPrefPathInformation_ObjectIdentity = ObjectIdentity
ciscoPrefPathInformation = _CiscoPrefPathInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2)
)
_CPrefPathRouteMapInfoTable_Object = MibTable
cPrefPathRouteMapInfoTable = _CPrefPathRouteMapInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapInfoTable.setStatus("current")
_CPrefPathRouteMapInfoEntry_Object = MibTableRow
cPrefPathRouteMapInfoEntry = _CPrefPathRouteMapInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 1, 1)
)
cPrefPathRouteMapInfoEntry.setIndexNames(
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"),
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapInfoEntry.setStatus("current")
_CPrefPathRMapSelectedPref_Type = CiscoPrefPathPreferenceLevel
_CPrefPathRMapSelectedPref_Object = MibTableColumn
cPrefPathRMapSelectedPref = _CPrefPathRMapSelectedPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 1, 1, 1),
    _CPrefPathRMapSelectedPref_Type()
)
cPrefPathRMapSelectedPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPrefPathRMapSelectedPref.setStatus("current")
_CPrefPathRMapSelectedIntf_Type = InterfaceIndex
_CPrefPathRMapSelectedIntf_Object = MibTableColumn
cPrefPathRMapSelectedIntf = _CPrefPathRMapSelectedIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 1, 1, 2),
    _CPrefPathRMapSelectedIntf_Type()
)
cPrefPathRMapSelectedIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPrefPathRMapSelectedIntf.setStatus("current")
_CPrefPathRMapSelIvrNextHopVsanId_Type = CiscoPrefPathIvrNextHopVsanId
_CPrefPathRMapSelIvrNextHopVsanId_Object = MibTableColumn
cPrefPathRMapSelIvrNextHopVsanId = _CPrefPathRMapSelIvrNextHopVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 1, 1, 3),
    _CPrefPathRMapSelIvrNextHopVsanId_Type()
)
cPrefPathRMapSelIvrNextHopVsanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPrefPathRMapSelIvrNextHopVsanId.setStatus("current")
_CPrefPathRouteMapMatchInfoTable_Object = MibTable
cPrefPathRouteMapMatchInfoTable = _CPrefPathRouteMapMatchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapMatchInfoTable.setStatus("current")
_CPrefPathRouteMapMatchInfoEntry_Object = MibTableRow
cPrefPathRouteMapMatchInfoEntry = _CPrefPathRouteMapMatchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 2, 1)
)
cPrefPathRouteMapMatchInfoEntry.setIndexNames(
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcAddr"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcAddrMask"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchSrcIntf"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchDstAddr"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchDstAddrMask"),
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapMatchInfoEntry.setStatus("current")
_CPrefPathRMapMatchStatus_Type = CiscoPrefPathStatus
_CPrefPathRMapMatchStatus_Object = MibTableColumn
cPrefPathRMapMatchStatus = _CPrefPathRMapMatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 2, 1, 1),
    _CPrefPathRMapMatchStatus_Type()
)
cPrefPathRMapMatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPrefPathRMapMatchStatus.setStatus("current")
_CPrefPathRouteMapSetInfoTable_Object = MibTable
cPrefPathRouteMapSetInfoTable = _CPrefPathRouteMapSetInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapSetInfoTable.setStatus("current")
_CPrefPathRouteMapSetInfoEntry_Object = MibTableRow
cPrefPathRouteMapSetInfoEntry = _CPrefPathRouteMapSetInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 3, 1)
)
cPrefPathRouteMapSetInfoEntry.setIndexNames(
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapVsanIndex"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteIndex"),
    (0, "CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIntfPref"),
)
if mibBuilder.loadTexts:
    cPrefPathRouteMapSetInfoEntry.setStatus("current")
_CPrefPathRouteMapSetInfoIntf_Type = InterfaceIndex
_CPrefPathRouteMapSetInfoIntf_Object = MibTableColumn
cPrefPathRouteMapSetInfoIntf = _CPrefPathRouteMapSetInfoIntf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 3, 1, 1),
    _CPrefPathRouteMapSetInfoIntf_Type()
)
cPrefPathRouteMapSetInfoIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPrefPathRouteMapSetInfoIntf.setStatus("current")
_CPrefPathRouteMapSetInfoIvrNextHopVId_Type = CiscoPrefPathIvrNextHopVsanId
_CPrefPathRouteMapSetInfoIvrNextHopVId_Object = MibTableColumn
cPrefPathRouteMapSetInfoIvrNextHopVId = _CPrefPathRouteMapSetInfoIvrNextHopVId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 3, 1, 2),
    _CPrefPathRouteMapSetInfoIvrNextHopVId_Type()
)
cPrefPathRouteMapSetInfoIvrNextHopVId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPrefPathRouteMapSetInfoIvrNextHopVId.setStatus("current")
_CPrefPathRouteMapSetStatus_Type = CiscoPrefPathStatus
_CPrefPathRouteMapSetStatus_Object = MibTableColumn
cPrefPathRouteMapSetStatus = _CPrefPathRouteMapSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 1, 2, 3, 1, 3),
    _CPrefPathRouteMapSetStatus_Type()
)
cPrefPathRouteMapSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPrefPathRouteMapSetStatus.setStatus("current")
_CiscoPrefPathMIBConform_ObjectIdentity = ObjectIdentity
ciscoPrefPathMIBConform = _CiscoPrefPathMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 2)
)
_CiscoPrefPathMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPrefPathMIBCompliances = _CiscoPrefPathMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 1)
)
_CiscoPrefPathMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPrefPathMIBGroups = _CiscoPrefPathMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2)
)

# Managed Objects groups

ciscoPrefPathConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2, 1)
)
ciscoPrefPathConfigGroup.setObjects(
      *(("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIntf"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIvrNextHopVsanId"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapIntfPrefStrict"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteActive"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapActive"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapStorageType"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRowStatus"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchRowStatus"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoPrefPathConfigGroup.setStatus("deprecated")

ciscoPrefPathInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2, 2)
)
ciscoPrefPathInfoGroup.setObjects(
      *(("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSelectedPref"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSelectedIntf"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSelIvrNextHopVsanId"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchStatus"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapSetInfoIntf"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapSetInfoIvrNextHopVId"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapSetStatus"))
)
if mibBuilder.loadTexts:
    ciscoPrefPathInfoGroup.setStatus("current")

ciscoPrefPathNotifyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2, 4)
)
ciscoPrefPathNotifyConfigGroup.setObjects(
    ("CISCO-PREFERRED-PATH-MIB", "cPrefPathHwFailureNotifEnable")
)
if mibBuilder.loadTexts:
    ciscoPrefPathNotifyConfigGroup.setStatus("current")

ciscoPrefPathConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2, 5)
)
ciscoPrefPathConfigGroupRev1.setObjects(
      *(("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapGlobalActive"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIntf"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetIvrNextHopVsanId"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapIntfPrefStrict"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRouteActive"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapStorageType"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRouteMapRowStatus"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapMatchRowStatus"),
        ("CISCO-PREFERRED-PATH-MIB", "cPrefPathRMapSetRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoPrefPathConfigGroupRev1.setStatus("current")


# Notification objects

ciscoPrefPathHWFailureNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 0, 1)
)
ciscoPrefPathHWFailureNotify.setObjects(
    ("CISCO-VSAN-MIB", "notifyVsanIndex")
)
if mibBuilder.loadTexts:
    ciscoPrefPathHWFailureNotify.setStatus(
        "current"
    )


# Notifications groups

ciscoPrefPathNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 2, 3)
)
ciscoPrefPathNotifyGroup.setObjects(
    ("CISCO-PREFERRED-PATH-MIB", "ciscoPrefPathHWFailureNotify")
)
if mibBuilder.loadTexts:
    ciscoPrefPathNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoPrefPathMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPrefPathMIBCompliance.setStatus(
        "deprecated"
    )

ciscoPrefPathMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 592, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPrefPathMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PREFERRED-PATH-MIB",
    **{"CiscoPrefPathFcAddrMask": CiscoPrefPathFcAddrMask,
       "CiscoPrefPathStatus": CiscoPrefPathStatus,
       "CiscoPrefPathIvrNextHopVsanId": CiscoPrefPathIvrNextHopVsanId,
       "CiscoPrefPathPreferenceLevel": CiscoPrefPathPreferenceLevel,
       "ciscoPrefPathMIB": ciscoPrefPathMIB,
       "ciscoPrefPathMIBNotifs": ciscoPrefPathMIBNotifs,
       "ciscoPrefPathHWFailureNotify": ciscoPrefPathHWFailureNotify,
       "ciscoPrefPathMIBObjects": ciscoPrefPathMIBObjects,
       "ciscoPrefPathConfiguration": ciscoPrefPathConfiguration,
       "cPrefPathRouteMapTable": cPrefPathRouteMapTable,
       "cPrefPathRouteMapEntry": cPrefPathRouteMapEntry,
       "cPrefPathRouteMapVsanIndex": cPrefPathRouteMapVsanIndex,
       "cPrefPathRouteMapRouteIndex": cPrefPathRouteMapRouteIndex,
       "cPrefPathRouteMapIntfPrefStrict": cPrefPathRouteMapIntfPrefStrict,
       "cPrefPathRouteMapRouteActive": cPrefPathRouteMapRouteActive,
       "cPrefPathRouteMapActive": cPrefPathRouteMapActive,
       "cPrefPathRouteMapStorageType": cPrefPathRouteMapStorageType,
       "cPrefPathRouteMapRowStatus": cPrefPathRouteMapRowStatus,
       "cPrefPathRouteMapGlobalTable": cPrefPathRouteMapGlobalTable,
       "cPrefPathRouteMapGlobalEntry": cPrefPathRouteMapGlobalEntry,
       "cPrefPathRouteMapGlobalActive": cPrefPathRouteMapGlobalActive,
       "cPrefPathRouteMapMatchTable": cPrefPathRouteMapMatchTable,
       "cPrefPathRouteMapMatchEntry": cPrefPathRouteMapMatchEntry,
       "cPrefPathRMapMatchSrcAddr": cPrefPathRMapMatchSrcAddr,
       "cPrefPathRMapMatchSrcAddrMask": cPrefPathRMapMatchSrcAddrMask,
       "cPrefPathRMapMatchSrcIntf": cPrefPathRMapMatchSrcIntf,
       "cPrefPathRMapMatchDstAddr": cPrefPathRMapMatchDstAddr,
       "cPrefPathRMapMatchDstAddrMask": cPrefPathRMapMatchDstAddrMask,
       "cPrefPathRMapMatchRowStatus": cPrefPathRMapMatchRowStatus,
       "cPrefPathRouteMapSetTable": cPrefPathRouteMapSetTable,
       "cPrefPathRouteMapSetEntry": cPrefPathRouteMapSetEntry,
       "cPrefPathRMapSetIntfPref": cPrefPathRMapSetIntfPref,
       "cPrefPathRMapSetIntf": cPrefPathRMapSetIntf,
       "cPrefPathRMapSetIvrNextHopVsanId": cPrefPathRMapSetIvrNextHopVsanId,
       "cPrefPathRMapSetRowStatus": cPrefPathRMapSetRowStatus,
       "cPrefPathHwFailureNotifEnable": cPrefPathHwFailureNotifEnable,
       "ciscoPrefPathInformation": ciscoPrefPathInformation,
       "cPrefPathRouteMapInfoTable": cPrefPathRouteMapInfoTable,
       "cPrefPathRouteMapInfoEntry": cPrefPathRouteMapInfoEntry,
       "cPrefPathRMapSelectedPref": cPrefPathRMapSelectedPref,
       "cPrefPathRMapSelectedIntf": cPrefPathRMapSelectedIntf,
       "cPrefPathRMapSelIvrNextHopVsanId": cPrefPathRMapSelIvrNextHopVsanId,
       "cPrefPathRouteMapMatchInfoTable": cPrefPathRouteMapMatchInfoTable,
       "cPrefPathRouteMapMatchInfoEntry": cPrefPathRouteMapMatchInfoEntry,
       "cPrefPathRMapMatchStatus": cPrefPathRMapMatchStatus,
       "cPrefPathRouteMapSetInfoTable": cPrefPathRouteMapSetInfoTable,
       "cPrefPathRouteMapSetInfoEntry": cPrefPathRouteMapSetInfoEntry,
       "cPrefPathRouteMapSetInfoIntf": cPrefPathRouteMapSetInfoIntf,
       "cPrefPathRouteMapSetInfoIvrNextHopVId": cPrefPathRouteMapSetInfoIvrNextHopVId,
       "cPrefPathRouteMapSetStatus": cPrefPathRouteMapSetStatus,
       "ciscoPrefPathMIBConform": ciscoPrefPathMIBConform,
       "ciscoPrefPathMIBCompliances": ciscoPrefPathMIBCompliances,
       "ciscoPrefPathMIBCompliance": ciscoPrefPathMIBCompliance,
       "ciscoPrefPathMIBComplianceRev1": ciscoPrefPathMIBComplianceRev1,
       "ciscoPrefPathMIBGroups": ciscoPrefPathMIBGroups,
       "ciscoPrefPathConfigGroup": ciscoPrefPathConfigGroup,
       "ciscoPrefPathInfoGroup": ciscoPrefPathInfoGroup,
       "ciscoPrefPathNotifyGroup": ciscoPrefPathNotifyGroup,
       "ciscoPrefPathNotifyConfigGroup": ciscoPrefPathNotifyConfigGroup,
       "ciscoPrefPathConfigGroupRev1": ciscoPrefPathConfigGroupRev1}
)
