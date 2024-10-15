# SNMP MIB module (Dell-LAN-SYSMNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dell-LAN-SYSMNG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:34:35 2024
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

(dellLanCommon,) = mibBuilder.importSymbols(
    "Dell-Vendor-MIB",
    "dellLanCommon")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dellLanSystemMng = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DellLanMngInfServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("allType", 0),
          ("http", 3),
          ("https", 4),
          ("snmp", 2),
          ("sntp", 6),
          ("ssh", 5),
          ("telnet", 1))
    )



class DellLanMngInfActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 0))
    )



# MIB Managed Objects in the order of their OIDs

_DellLanMngIfGroup_ObjectIdentity = ObjectIdentity
dellLanMngIfGroup = _DellLanMngIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1)
)
_DellLanMngInfEnable_Type = TruthValue
_DellLanMngInfEnable_Object = MibScalar
dellLanMngInfEnable = _DellLanMngInfEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 1),
    _DellLanMngInfEnable_Type()
)
dellLanMngInfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanMngInfEnable.setStatus("current")


class _DellLanMngInfActiveListName_Type(DisplayString):
    """Custom type dellLanMngInfActiveListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DellLanMngInfActiveListName_Type.__name__ = "DisplayString"
_DellLanMngInfActiveListName_Object = MibScalar
dellLanMngInfActiveListName = _DellLanMngInfActiveListName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 2),
    _DellLanMngInfActiveListName_Type()
)
dellLanMngInfActiveListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanMngInfActiveListName.setStatus("current")
_DellLanMngInfListTable_Object = MibTable
dellLanMngInfListTable = _DellLanMngInfListTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    dellLanMngInfListTable.setStatus("current")
_DellLanMngInfListEntry_Object = MibTableRow
dellLanMngInfListEntry = _DellLanMngInfListEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1)
)
dellLanMngInfListEntry.setIndexNames(
    (0, "Dell-LAN-SYSMNG-MIB", "dellLanMngInfListName"),
    (0, "Dell-LAN-SYSMNG-MIB", "dellLanMngInfListPriority"),
)
if mibBuilder.loadTexts:
    dellLanMngInfListEntry.setStatus("current")


class _DellLanMngInfListName_Type(DisplayString):
    """Custom type dellLanMngInfListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DellLanMngInfListName_Type.__name__ = "DisplayString"
_DellLanMngInfListName_Object = MibTableColumn
dellLanMngInfListName = _DellLanMngInfListName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 1),
    _DellLanMngInfListName_Type()
)
dellLanMngInfListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanMngInfListName.setStatus("current")


class _DellLanMngInfListPriority_Type(Unsigned32):
    """Custom type dellLanMngInfListPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DellLanMngInfListPriority_Type.__name__ = "Unsigned32"
_DellLanMngInfListPriority_Object = MibTableColumn
dellLanMngInfListPriority = _DellLanMngInfListPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 2),
    _DellLanMngInfListPriority_Type()
)
dellLanMngInfListPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanMngInfListPriority.setStatus("current")
_DellLanMngInfListIfIndex_Type = Unsigned32
_DellLanMngInfListIfIndex_Object = MibTableColumn
dellLanMngInfListIfIndex = _DellLanMngInfListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 3),
    _DellLanMngInfListIfIndex_Type()
)
dellLanMngInfListIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanMngInfListIfIndex.setStatus("current")
_DellLanMngInfListIpAddr_Type = IpAddress
_DellLanMngInfListIpAddr_Object = MibTableColumn
dellLanMngInfListIpAddr = _DellLanMngInfListIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 4),
    _DellLanMngInfListIpAddr_Type()
)
dellLanMngInfListIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanMngInfListIpAddr.setStatus("current")
_DellLanMngInfListIpNetMask_Type = IpAddress
_DellLanMngInfListIpNetMask_Object = MibTableColumn
dellLanMngInfListIpNetMask = _DellLanMngInfListIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 5),
    _DellLanMngInfListIpNetMask_Type()
)
dellLanMngInfListIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanMngInfListIpNetMask.setStatus("current")
_DellLanMngInfListService_Type = DellLanMngInfServiceType
_DellLanMngInfListService_Object = MibTableColumn
dellLanMngInfListService = _DellLanMngInfListService_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 6),
    _DellLanMngInfListService_Type()
)
dellLanMngInfListService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanMngInfListService.setStatus("current")
_DellLanMngInfListAction_Type = DellLanMngInfActionType
_DellLanMngInfListAction_Object = MibTableColumn
dellLanMngInfListAction = _DellLanMngInfListAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 7),
    _DellLanMngInfListAction_Type()
)
dellLanMngInfListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanMngInfListAction.setStatus("current")
_DellLanMngInfListRowStatus_Type = RowStatus
_DellLanMngInfListRowStatus_Object = MibTableColumn
dellLanMngInfListRowStatus = _DellLanMngInfListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 8),
    _DellLanMngInfListRowStatus_Type()
)
dellLanMngInfListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanMngInfListRowStatus.setStatus("current")
_DellLanMngInfListVlanId_Type = Unsigned32
_DellLanMngInfListVlanId_Object = MibTableColumn
dellLanMngInfListVlanId = _DellLanMngInfListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 1, 3, 1, 9),
    _DellLanMngInfListVlanId_Type()
)
dellLanMngInfListVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanMngInfListVlanId.setStatus("current")
_DellLanFileSysGroup_ObjectIdentity = ObjectIdentity
dellLanFileSysGroup = _DellLanFileSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2)
)
_DellLanFSMaxSize_Type = Integer32
_DellLanFSMaxSize_Object = MibScalar
dellLanFSMaxSize = _DellLanFSMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 1),
    _DellLanFSMaxSize_Type()
)
dellLanFSMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanFSMaxSize.setStatus("current")
_DellLanFSAvailableSize_Type = Integer32
_DellLanFSAvailableSize_Object = MibScalar
dellLanFSAvailableSize = _DellLanFSAvailableSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 2),
    _DellLanFSAvailableSize_Type()
)
dellLanFSAvailableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanFSAvailableSize.setStatus("current")
_DellLanFileTable_Object = MibTable
dellLanFileTable = _DellLanFileTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    dellLanFileTable.setStatus("current")
_DellLanFileEntry_Object = MibTableRow
dellLanFileEntry = _DellLanFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1)
)
dellLanFileEntry.setIndexNames(
    (0, "Dell-LAN-SYSMNG-MIB", "dellLanFileName"),
)
if mibBuilder.loadTexts:
    dellLanFileEntry.setStatus("current")


class _DellLanFileName_Type(DisplayString):
    """Custom type dellLanFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DellLanFileName_Type.__name__ = "DisplayString"
_DellLanFileName_Object = MibTableColumn
dellLanFileName = _DellLanFileName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 1),
    _DellLanFileName_Type()
)
dellLanFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanFileName.setStatus("current")


class _DellLanFilePermission_Type(Integer32):
    """Custom type dellLanFilePermission based on Integer32"""
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
        *(("noReadNoWrite", 4),
          ("readWrite", 3),
          ("readonly", 1),
          ("writeonly", 2))
    )


_DellLanFilePermission_Type.__name__ = "Integer32"
_DellLanFilePermission_Object = MibTableColumn
dellLanFilePermission = _DellLanFilePermission_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 2),
    _DellLanFilePermission_Type()
)
dellLanFilePermission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanFilePermission.setStatus("current")


class _DellLanFilePriority_Type(Integer32):
    """Custom type dellLanFilePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DellLanFilePriority_Type.__name__ = "Integer32"
_DellLanFilePriority_Object = MibTableColumn
dellLanFilePriority = _DellLanFilePriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 3),
    _DellLanFilePriority_Type()
)
dellLanFilePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanFilePriority.setStatus("current")
_DellLanFileSize_Type = Integer32
_DellLanFileSize_Object = MibTableColumn
dellLanFileSize = _DellLanFileSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 4),
    _DellLanFileSize_Type()
)
dellLanFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanFileSize.setStatus("current")


class _DellLanFileType_Type(Integer32):
    """Custom type dellLanFileType based on Integer32"""
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
        *(("activeImg", 5),
          ("config", 2),
          ("image", 1),
          ("log", 3),
          ("sys", 4))
    )


_DellLanFileType_Type.__name__ = "Integer32"
_DellLanFileType_Object = MibTableColumn
dellLanFileType = _DellLanFileType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 5),
    _DellLanFileType_Type()
)
dellLanFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanFileType.setStatus("current")
_DellLanFileModificationDate_Type = DisplayString
_DellLanFileModificationDate_Object = MibTableColumn
dellLanFileModificationDate = _DellLanFileModificationDate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 6),
    _DellLanFileModificationDate_Type()
)
dellLanFileModificationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanFileModificationDate.setStatus("current")
_DellLanFileModificationTime_Type = DisplayString
_DellLanFileModificationTime_Object = MibTableColumn
dellLanFileModificationTime = _DellLanFileModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 7),
    _DellLanFileModificationTime_Type()
)
dellLanFileModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanFileModificationTime.setStatus("current")


class _DellLanFileDescription_Type(DisplayString):
    """Custom type dellLanFileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DellLanFileDescription_Type.__name__ = "DisplayString"
_DellLanFileDescription_Object = MibTableColumn
dellLanFileDescription = _DellLanFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 3, 1, 8),
    _DellLanFileDescription_Type()
)
dellLanFileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanFileDescription.setStatus("current")
_DellLanFileActionTable_Object = MibTable
dellLanFileActionTable = _DellLanFileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    dellLanFileActionTable.setStatus("current")
_DellLanFileActionEntry_Object = MibTableRow
dellLanFileActionEntry = _DellLanFileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1)
)
dellLanFileActionEntry.setIndexNames(
    (0, "Dell-LAN-SYSMNG-MIB", "dellLanFileActionIndex"),
)
if mibBuilder.loadTexts:
    dellLanFileActionEntry.setStatus("current")
_DellLanFileActionIndex_Type = Integer32
_DellLanFileActionIndex_Object = MibTableColumn
dellLanFileActionIndex = _DellLanFileActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 1),
    _DellLanFileActionIndex_Type()
)
dellLanFileActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanFileActionIndex.setStatus("current")
_DellLanFileActionSourceFile_Type = DisplayString
_DellLanFileActionSourceFile_Object = MibTableColumn
dellLanFileActionSourceFile = _DellLanFileActionSourceFile_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 2),
    _DellLanFileActionSourceFile_Type()
)
dellLanFileActionSourceFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanFileActionSourceFile.setStatus("current")
_DellLanFileActionDestFile_Type = DisplayString
_DellLanFileActionDestFile_Object = MibTableColumn
dellLanFileActionDestFile = _DellLanFileActionDestFile_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 3),
    _DellLanFileActionDestFile_Type()
)
dellLanFileActionDestFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanFileActionDestFile.setStatus("current")
_DellLanFileActionForceAction_Type = TruthValue
_DellLanFileActionForceAction_Object = MibTableColumn
dellLanFileActionForceAction = _DellLanFileActionForceAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 4),
    _DellLanFileActionForceAction_Type()
)
dellLanFileActionForceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanFileActionForceAction.setStatus("current")


class _DellLanFileActionCommand_Type(Integer32):
    """Custom type dellLanFileActionCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copy", 2),
          ("delete", 3))
    )


_DellLanFileActionCommand_Type.__name__ = "Integer32"
_DellLanFileActionCommand_Object = MibTableColumn
dellLanFileActionCommand = _DellLanFileActionCommand_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 5),
    _DellLanFileActionCommand_Type()
)
dellLanFileActionCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanFileActionCommand.setStatus("current")


class _DellLanFileActionResultCode_Type(Integer32):
    """Custom type dellLanFileActionResultCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("fileNotFound", 2),
          ("fileSystemFull", 6),
          ("incompatFileType", 10),
          ("invalidCmd", 3),
          ("invalidDest", 11),
          ("overwriteFailed", 8),
          ("overwriteNotRequested", 7),
          ("permissionDenied", 9),
          ("statusPending", 1),
          ("success", 0),
          ("tftpServerConnectFailed", 5),
          ("unknownError", 4))
    )


_DellLanFileActionResultCode_Type.__name__ = "Integer32"
_DellLanFileActionResultCode_Object = MibTableColumn
dellLanFileActionResultCode = _DellLanFileActionResultCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 2, 4, 1, 6),
    _DellLanFileActionResultCode_Type()
)
dellLanFileActionResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellLanFileActionResultCode.setStatus("current")
_DellLanSysMngGroup_ObjectIdentity = ObjectIdentity
dellLanSysMngGroup = _DellLanSysMngGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 3)
)
_DellLanSysActionReload_Type = Integer32
_DellLanSysActionReload_Object = MibScalar
dellLanSysActionReload = _DellLanSysActionReload_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 3, 1),
    _DellLanSysActionReload_Type()
)
dellLanSysActionReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanSysActionReload.setStatus("current")
_DellLanSysActionSetActiveImage_Type = DisplayString
_DellLanSysActionSetActiveImage_Object = MibScalar
dellLanSysActionSetActiveImage = _DellLanSysActionSetActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 1, 2, 3, 2),
    _DellLanSysActionSetActiveImage_Type()
)
dellLanSysActionSetActiveImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellLanSysActionSetActiveImage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dell-LAN-SYSMNG-MIB",
    **{"DellLanMngInfServiceType": DellLanMngInfServiceType,
       "DellLanMngInfActionType": DellLanMngInfActionType,
       "dellLanSystemMng": dellLanSystemMng,
       "dellLanMngIfGroup": dellLanMngIfGroup,
       "dellLanMngInfEnable": dellLanMngInfEnable,
       "dellLanMngInfActiveListName": dellLanMngInfActiveListName,
       "dellLanMngInfListTable": dellLanMngInfListTable,
       "dellLanMngInfListEntry": dellLanMngInfListEntry,
       "dellLanMngInfListName": dellLanMngInfListName,
       "dellLanMngInfListPriority": dellLanMngInfListPriority,
       "dellLanMngInfListIfIndex": dellLanMngInfListIfIndex,
       "dellLanMngInfListIpAddr": dellLanMngInfListIpAddr,
       "dellLanMngInfListIpNetMask": dellLanMngInfListIpNetMask,
       "dellLanMngInfListService": dellLanMngInfListService,
       "dellLanMngInfListAction": dellLanMngInfListAction,
       "dellLanMngInfListRowStatus": dellLanMngInfListRowStatus,
       "dellLanMngInfListVlanId": dellLanMngInfListVlanId,
       "dellLanFileSysGroup": dellLanFileSysGroup,
       "dellLanFSMaxSize": dellLanFSMaxSize,
       "dellLanFSAvailableSize": dellLanFSAvailableSize,
       "dellLanFileTable": dellLanFileTable,
       "dellLanFileEntry": dellLanFileEntry,
       "dellLanFileName": dellLanFileName,
       "dellLanFilePermission": dellLanFilePermission,
       "dellLanFilePriority": dellLanFilePriority,
       "dellLanFileSize": dellLanFileSize,
       "dellLanFileType": dellLanFileType,
       "dellLanFileModificationDate": dellLanFileModificationDate,
       "dellLanFileModificationTime": dellLanFileModificationTime,
       "dellLanFileDescription": dellLanFileDescription,
       "dellLanFileActionTable": dellLanFileActionTable,
       "dellLanFileActionEntry": dellLanFileActionEntry,
       "dellLanFileActionIndex": dellLanFileActionIndex,
       "dellLanFileActionSourceFile": dellLanFileActionSourceFile,
       "dellLanFileActionDestFile": dellLanFileActionDestFile,
       "dellLanFileActionForceAction": dellLanFileActionForceAction,
       "dellLanFileActionCommand": dellLanFileActionCommand,
       "dellLanFileActionResultCode": dellLanFileActionResultCode,
       "dellLanSysMngGroup": dellLanSysMngGroup,
       "dellLanSysActionReload": dellLanSysActionReload,
       "dellLanSysActionSetActiveImage": dellLanSysActionSetActiveImage}
)
