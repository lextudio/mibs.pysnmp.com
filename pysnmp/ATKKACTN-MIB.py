# SNMP MIB module (ATKKACTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATKKACTN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:46 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlliedTelesyn_ObjectIdentity = ObjectIdentity
alliedTelesyn = _AlliedTelesyn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_RepeaterMib_ObjectIdentity = ObjectIdentity
repeaterMib = _RepeaterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1)
)
_NewRepeaterMib_ObjectIdentity = ObjectIdentity
newRepeaterMib = _NewRepeaterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20)
)
_AcctonHubMIB_ObjectIdentity = ObjectIdentity
acctonHubMIB = _AcctonHubMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3)
)
_AcctonCommon_ObjectIdentity = ObjectIdentity
acctonCommon = _AcctonCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1)
)
_Accsystem_ObjectIdentity = ObjectIdentity
accsystem = _Accsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 1)
)
_MajorVer_Type = Integer32
_MajorVer_Object = MibScalar
majorVer = _MajorVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 1, 1),
    _MajorVer_Type()
)
majorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    majorVer.setStatus("mandatory")
_MinorVer_Type = Integer32
_MinorVer_Object = MibScalar
minorVer = _MinorVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 1, 2),
    _MinorVer_Type()
)
minorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minorVer.setStatus("mandatory")
_HardwareVer_Type = Integer32
_HardwareVer_Object = MibScalar
hardwareVer = _HardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 1, 3),
    _HardwareVer_Type()
)
hardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVer.setStatus("mandatory")
_CommunityMgt_ObjectIdentity = ObjectIdentity
communityMgt = _CommunityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 2)
)
_CommunityStringSize_Type = Integer32
_CommunityStringSize_Object = MibScalar
communityStringSize = _CommunityStringSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 2, 1),
    _CommunityStringSize_Type()
)
communityStringSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communityStringSize.setStatus("mandatory")
_CommunityTableSize_Type = Integer32
_CommunityTableSize_Object = MibScalar
communityTableSize = _CommunityTableSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 2, 2),
    _CommunityTableSize_Type()
)
communityTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communityTableSize.setStatus("mandatory")
_CommunityTable_Object = MibTable
communityTable = _CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    communityTable.setStatus("mandatory")
_CommunityEntry_Object = MibTableRow
communityEntry = _CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 2, 3, 1)
)
communityEntry.setIndexNames(
    (0, "ATKKACTN-MIB", "communityIndex"),
)
if mibBuilder.loadTexts:
    communityEntry.setStatus("mandatory")
_CommunityIndex_Type = Integer32
_CommunityIndex_Object = MibTableColumn
communityIndex = _CommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 2, 3, 1, 1),
    _CommunityIndex_Type()
)
communityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communityIndex.setStatus("mandatory")
_CommunityString_Type = DisplayString
_CommunityString_Object = MibTableColumn
communityString = _CommunityString_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 2, 3, 1, 2),
    _CommunityString_Type()
)
communityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityString.setStatus("mandatory")


class _CommunityAccessMode_Type(Integer32):
    """Custom type communityAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_CommunityAccessMode_Type.__name__ = "Integer32"
_CommunityAccessMode_Object = MibTableColumn
communityAccessMode = _CommunityAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 2, 3, 1, 3),
    _CommunityAccessMode_Type()
)
communityAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityAccessMode.setStatus("mandatory")
_CommunityStatus_Type = Integer32
_CommunityStatus_Object = MibTableColumn
communityStatus = _CommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 2, 3, 1, 4),
    _CommunityStatus_Type()
)
communityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityStatus.setStatus("mandatory")
_TrapManagerMgt_ObjectIdentity = ObjectIdentity
trapManagerMgt = _TrapManagerMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 3)
)
_TrapManagerTableSize_Type = Integer32
_TrapManagerTableSize_Object = MibScalar
trapManagerTableSize = _TrapManagerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 3, 1),
    _TrapManagerTableSize_Type()
)
trapManagerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapManagerTableSize.setStatus("mandatory")
_TrapManagerTable_Object = MibTable
trapManagerTable = _TrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    trapManagerTable.setStatus("mandatory")
_TrapManagerEntry_Object = MibTableRow
trapManagerEntry = _TrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 3, 2, 1)
)
trapManagerEntry.setIndexNames(
    (0, "ATKKACTN-MIB", "trapMgrIndex"),
)
if mibBuilder.loadTexts:
    trapManagerEntry.setStatus("mandatory")
_TrapMgrIndex_Type = Integer32
_TrapMgrIndex_Object = MibTableColumn
trapMgrIndex = _TrapMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 3, 2, 1, 1),
    _TrapMgrIndex_Type()
)
trapMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMgrIndex.setStatus("mandatory")
_TrapMgrCommunityIndex_Type = Integer32
_TrapMgrCommunityIndex_Object = MibTableColumn
trapMgrCommunityIndex = _TrapMgrCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 3, 2, 1, 2),
    _TrapMgrCommunityIndex_Type()
)
trapMgrCommunityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapMgrCommunityIndex.setStatus("mandatory")
_TrapMgrIpaddress_Type = IpAddress
_TrapMgrIpaddress_Object = MibTableColumn
trapMgrIpaddress = _TrapMgrIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 3, 2, 1, 3),
    _TrapMgrIpaddress_Type()
)
trapMgrIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapMgrIpaddress.setStatus("mandatory")


class _TrapMgrEntryStatus_Type(Integer32):
    """Custom type trapMgrEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("underChange", 1),
          ("valid", 2))
    )


_TrapMgrEntryStatus_Type.__name__ = "Integer32"
_TrapMgrEntryStatus_Object = MibTableColumn
trapMgrEntryStatus = _TrapMgrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 3, 2, 1, 4),
    _TrapMgrEntryStatus_Type()
)
trapMgrEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapMgrEntryStatus.setStatus("mandatory")
_DownloadMgt_ObjectIdentity = ObjectIdentity
downloadMgt = _DownloadMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 4)
)
_DownloadServerIP_Type = IpAddress
_DownloadServerIP_Object = MibScalar
downloadServerIP = _DownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 4, 1),
    _DownloadServerIP_Type()
)
downloadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadServerIP.setStatus("mandatory")
_DownloadFilename_Type = DisplayString
_DownloadFilename_Object = MibScalar
downloadFilename = _DownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 4, 2),
    _DownloadFilename_Type()
)
downloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadFilename.setStatus("mandatory")


class _DownloadMode_Type(Integer32):
    """Custom type downloadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanant", 1),
          ("temporary", 2))
    )


_DownloadMode_Type.__name__ = "Integer32"
_DownloadMode_Object = MibScalar
downloadMode = _DownloadMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 4, 3),
    _DownloadMode_Type()
)
downloadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadMode.setStatus("mandatory")


class _DownloadAction_Type(Integer32):
    """Custom type downloadAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRun", 2),
          ("run", 1))
    )


_DownloadAction_Type.__name__ = "Integer32"
_DownloadAction_Object = MibScalar
downloadAction = _DownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 4, 4),
    _DownloadAction_Type()
)
downloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadAction.setStatus("mandatory")
_Restart_Type = Integer32
_Restart_Object = MibScalar
restart = _Restart_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 5),
    _Restart_Type()
)
restart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restart.setStatus("mandatory")
_Acctest_ObjectIdentity = ObjectIdentity
acctest = _Acctest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 6)
)


class _TestTrap_Type(Integer32):
    """Custom type testTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("test", 1)
    )


_TestTrap_Type.__name__ = "Integer32"
_TestTrap_Object = MibScalar
testTrap = _TestTrap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 6, 1),
    _TestTrap_Type()
)
testTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    testTrap.setStatus("mandatory")
_IpxtrapManagerMgt_ObjectIdentity = ObjectIdentity
ipxtrapManagerMgt = _IpxtrapManagerMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 7)
)
_IpxtrapManagerTableSize_Type = Integer32
_IpxtrapManagerTableSize_Object = MibScalar
ipxtrapManagerTableSize = _IpxtrapManagerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 7, 1),
    _IpxtrapManagerTableSize_Type()
)
ipxtrapManagerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxtrapManagerTableSize.setStatus("mandatory")
_IpxtrapManagerTable_Object = MibTable
ipxtrapManagerTable = _IpxtrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ipxtrapManagerTable.setStatus("mandatory")
_IpxtrapManagerEntry_Object = MibTableRow
ipxtrapManagerEntry = _IpxtrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 7, 2, 1)
)
ipxtrapManagerEntry.setIndexNames(
    (0, "ATKKACTN-MIB", "ipxtrapMgrIndex"),
)
if mibBuilder.loadTexts:
    ipxtrapManagerEntry.setStatus("mandatory")
_IpxtrapMgrIndex_Type = Integer32
_IpxtrapMgrIndex_Object = MibTableColumn
ipxtrapMgrIndex = _IpxtrapMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 7, 2, 1, 1),
    _IpxtrapMgrIndex_Type()
)
ipxtrapMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxtrapMgrIndex.setStatus("mandatory")
_IpxtrapMgrCommunityIndex_Type = Integer32
_IpxtrapMgrCommunityIndex_Object = MibTableColumn
ipxtrapMgrCommunityIndex = _IpxtrapMgrCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 7, 2, 1, 2),
    _IpxtrapMgrCommunityIndex_Type()
)
ipxtrapMgrCommunityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxtrapMgrCommunityIndex.setStatus("mandatory")


class _IpxtrapMgrNetNumber_Type(OctetString):
    """Custom type ipxtrapMgrNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxtrapMgrNetNumber_Type.__name__ = "OctetString"
_IpxtrapMgrNetNumber_Object = MibTableColumn
ipxtrapMgrNetNumber = _IpxtrapMgrNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 7, 2, 1, 3),
    _IpxtrapMgrNetNumber_Type()
)
ipxtrapMgrNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxtrapMgrNetNumber.setStatus("mandatory")
_IpxtrapMgrNode_Type = PhysAddress
_IpxtrapMgrNode_Object = MibTableColumn
ipxtrapMgrNode = _IpxtrapMgrNode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 7, 2, 1, 4),
    _IpxtrapMgrNode_Type()
)
ipxtrapMgrNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxtrapMgrNode.setStatus("mandatory")


class _IpxtrapMgrEntryStatus_Type(Integer32):
    """Custom type ipxtrapMgrEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpxtrapMgrEntryStatus_Type.__name__ = "Integer32"
_IpxtrapMgrEntryStatus_Object = MibTableColumn
ipxtrapMgrEntryStatus = _IpxtrapMgrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 1, 20, 3, 1, 7, 2, 1, 5),
    _IpxtrapMgrEntryStatus_Type()
)
ipxtrapMgrEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxtrapMgrEntryStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATKKACTN-MIB",
    **{"alliedTelesyn": alliedTelesyn,
       "products": products,
       "mibObject": mibObject,
       "repeaterMib": repeaterMib,
       "newRepeaterMib": newRepeaterMib,
       "acctonHubMIB": acctonHubMIB,
       "acctonCommon": acctonCommon,
       "accsystem": accsystem,
       "majorVer": majorVer,
       "minorVer": minorVer,
       "hardwareVer": hardwareVer,
       "communityMgt": communityMgt,
       "communityStringSize": communityStringSize,
       "communityTableSize": communityTableSize,
       "communityTable": communityTable,
       "communityEntry": communityEntry,
       "communityIndex": communityIndex,
       "communityString": communityString,
       "communityAccessMode": communityAccessMode,
       "communityStatus": communityStatus,
       "trapManagerMgt": trapManagerMgt,
       "trapManagerTableSize": trapManagerTableSize,
       "trapManagerTable": trapManagerTable,
       "trapManagerEntry": trapManagerEntry,
       "trapMgrIndex": trapMgrIndex,
       "trapMgrCommunityIndex": trapMgrCommunityIndex,
       "trapMgrIpaddress": trapMgrIpaddress,
       "trapMgrEntryStatus": trapMgrEntryStatus,
       "downloadMgt": downloadMgt,
       "downloadServerIP": downloadServerIP,
       "downloadFilename": downloadFilename,
       "downloadMode": downloadMode,
       "downloadAction": downloadAction,
       "restart": restart,
       "acctest": acctest,
       "testTrap": testTrap,
       "ipxtrapManagerMgt": ipxtrapManagerMgt,
       "ipxtrapManagerTableSize": ipxtrapManagerTableSize,
       "ipxtrapManagerTable": ipxtrapManagerTable,
       "ipxtrapManagerEntry": ipxtrapManagerEntry,
       "ipxtrapMgrIndex": ipxtrapMgrIndex,
       "ipxtrapMgrCommunityIndex": ipxtrapMgrCommunityIndex,
       "ipxtrapMgrNetNumber": ipxtrapMgrNetNumber,
       "ipxtrapMgrNode": ipxtrapMgrNode,
       "ipxtrapMgrEntryStatus": ipxtrapMgrEntryStatus}
)
