# SNMP MIB module (CISCO-LICENSE-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LICENSE-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:59 2024
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

(PhysicalIndexOrZero,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndexOrZero",
    "entPhysicalIndex")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLicenseMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 543)
)
ciscoLicenseMgmtMIB.setRevisions(
        ("2012-04-19 00:00",
         "2011-04-19 00:00",
         "2008-11-21 00:00",
         "2006-10-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClmgmtLicenseIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class ClmgmtLicenseIndexOrZero(Unsigned32, TextualConvention):
    status = "current"


class ClmgmtLicenseTransferProtocol(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 4),
          ("http", 6),
          ("local", 2),
          ("none", 1),
          ("rcp", 5),
          ("scp", 7),
          ("sftp", 8),
          ("tftp", 3))
    )



class ClmgmtLicenseActionState(Integer32, TextualConvention):
    status = "current"
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
        *(("failed", 6),
          ("inProgress", 3),
          ("none", 1),
          ("partiallySuccessful", 5),
          ("pending", 2),
          ("successful", 4))
    )



class ClmgmtLicenseActionFailCause(Integer32, TextualConvention):
    status = "current"
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("fileServerNotReachable", 4),
          ("generalFailure", 2),
          ("invalidLicenseBackupFile", 20),
          ("invalidLicenseCount", 11),
          ("invalidLicenseEULAFile", 22),
          ("invalidLicenseFile", 7),
          ("invalidLicenseFilePath", 6),
          ("invalidLicenseLine", 8),
          ("invalidLicensePeriod", 12),
          ("invalidLicenseStore", 14),
          ("invalidPermissionTicket", 17),
          ("invalidPermissionTicketFile", 16),
          ("invalidRehostTicket", 19),
          ("invalidRehostTicketFile", 18),
          ("licenseAlreadyExists", 9),
          ("licenseClearInProgress", 21),
          ("licenseInUse", 13),
          ("licenseNotValidForDevice", 10),
          ("licenseStorageFull", 15),
          ("none", 1),
          ("transferProtocolNotSupported", 3),
          ("unrecognizedEntPhysicalIndex", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLicenseMgmtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLicenseMgmtMIBNotifs = _CiscoLicenseMgmtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0)
)
_CiscoLicenseMgmtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLicenseMgmtMIBObjects = _CiscoLicenseMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1)
)
_ClmgmtLicenseConfiguration_ObjectIdentity = ObjectIdentity
clmgmtLicenseConfiguration = _ClmgmtLicenseConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1)
)


class _ClmgmtNextFreeLicenseActionIndex_Type(Unsigned32):
    """Custom type clmgmtNextFreeLicenseActionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ClmgmtNextFreeLicenseActionIndex_Type.__name__ = "Unsigned32"
_ClmgmtNextFreeLicenseActionIndex_Object = MibScalar
clmgmtNextFreeLicenseActionIndex = _ClmgmtNextFreeLicenseActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 1),
    _ClmgmtNextFreeLicenseActionIndex_Type()
)
clmgmtNextFreeLicenseActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtNextFreeLicenseActionIndex.setStatus("current")
_ClmgmtLicenseActionTable_Object = MibTable
clmgmtLicenseActionTable = _ClmgmtLicenseActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2)
)
if mibBuilder.loadTexts:
    clmgmtLicenseActionTable.setStatus("current")
_ClmgmtLicenseActionEntry_Object = MibTableRow
clmgmtLicenseActionEntry = _ClmgmtLicenseActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1)
)
clmgmtLicenseActionEntry.setIndexNames(
    (0, "CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseActionIndex"),
)
if mibBuilder.loadTexts:
    clmgmtLicenseActionEntry.setStatus("current")


class _ClmgmtLicenseActionIndex_Type(Unsigned32):
    """Custom type clmgmtLicenseActionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ClmgmtLicenseActionIndex_Type.__name__ = "Unsigned32"
_ClmgmtLicenseActionIndex_Object = MibTableColumn
clmgmtLicenseActionIndex = _ClmgmtLicenseActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 1),
    _ClmgmtLicenseActionIndex_Type()
)
clmgmtLicenseActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmgmtLicenseActionIndex.setStatus("current")


class _ClmgmtLicenseActionEntPhysicalIndex_Type(PhysicalIndexOrZero):
    """Custom type clmgmtLicenseActionEntPhysicalIndex based on PhysicalIndexOrZero"""
    defaultValue = 0


_ClmgmtLicenseActionEntPhysicalIndex_Object = MibTableColumn
clmgmtLicenseActionEntPhysicalIndex = _ClmgmtLicenseActionEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 2),
    _ClmgmtLicenseActionEntPhysicalIndex_Type()
)
clmgmtLicenseActionEntPhysicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseActionEntPhysicalIndex.setStatus("current")


class _ClmgmtLicenseActionTransferProtocol_Type(ClmgmtLicenseTransferProtocol):
    """Custom type clmgmtLicenseActionTransferProtocol based on ClmgmtLicenseTransferProtocol"""


_ClmgmtLicenseActionTransferProtocol_Object = MibTableColumn
clmgmtLicenseActionTransferProtocol = _ClmgmtLicenseActionTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 3),
    _ClmgmtLicenseActionTransferProtocol_Type()
)
clmgmtLicenseActionTransferProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseActionTransferProtocol.setStatus("current")


class _ClmgmtLicenseServerAddressType_Type(InetAddressType):
    """Custom type clmgmtLicenseServerAddressType based on InetAddressType"""


_ClmgmtLicenseServerAddressType_Object = MibTableColumn
clmgmtLicenseServerAddressType = _ClmgmtLicenseServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 4),
    _ClmgmtLicenseServerAddressType_Type()
)
clmgmtLicenseServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseServerAddressType.setStatus("current")
_ClmgmtLicenseServerAddress_Type = InetAddress
_ClmgmtLicenseServerAddress_Object = MibTableColumn
clmgmtLicenseServerAddress = _ClmgmtLicenseServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 5),
    _ClmgmtLicenseServerAddress_Type()
)
clmgmtLicenseServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseServerAddress.setStatus("current")


class _ClmgmtLicenseServerUsername_Type(SnmpAdminString):
    """Custom type clmgmtLicenseServerUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_ClmgmtLicenseServerUsername_Type.__name__ = "SnmpAdminString"
_ClmgmtLicenseServerUsername_Object = MibTableColumn
clmgmtLicenseServerUsername = _ClmgmtLicenseServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 6),
    _ClmgmtLicenseServerUsername_Type()
)
clmgmtLicenseServerUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseServerUsername.setStatus("current")


class _ClmgmtLicenseServerPassword_Type(SnmpAdminString):
    """Custom type clmgmtLicenseServerPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_ClmgmtLicenseServerPassword_Type.__name__ = "SnmpAdminString"
_ClmgmtLicenseServerPassword_Object = MibTableColumn
clmgmtLicenseServerPassword = _ClmgmtLicenseServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 7),
    _ClmgmtLicenseServerPassword_Type()
)
clmgmtLicenseServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseServerPassword.setStatus("current")


class _ClmgmtLicenseFile_Type(SnmpAdminString):
    """Custom type clmgmtLicenseFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClmgmtLicenseFile_Type.__name__ = "SnmpAdminString"
_ClmgmtLicenseFile_Object = MibTableColumn
clmgmtLicenseFile = _ClmgmtLicenseFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 8),
    _ClmgmtLicenseFile_Type()
)
clmgmtLicenseFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseFile.setStatus("current")


class _ClmgmtLicenseStore_Type(Unsigned32):
    """Custom type clmgmtLicenseStore based on Unsigned32"""
    defaultValue = 0


_ClmgmtLicenseStore_Object = MibTableColumn
clmgmtLicenseStore = _ClmgmtLicenseStore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 9),
    _ClmgmtLicenseStore_Type()
)
clmgmtLicenseStore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseStore.setStatus("current")


class _ClmgmtLicenseActionLicenseIndex_Type(ClmgmtLicenseIndexOrZero):
    """Custom type clmgmtLicenseActionLicenseIndex based on ClmgmtLicenseIndexOrZero"""
    defaultValue = 0


_ClmgmtLicenseActionLicenseIndex_Object = MibTableColumn
clmgmtLicenseActionLicenseIndex = _ClmgmtLicenseActionLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 10),
    _ClmgmtLicenseActionLicenseIndex_Type()
)
clmgmtLicenseActionLicenseIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseActionLicenseIndex.setStatus("current")


class _ClmgmtLicensePermissionTicketFile_Type(SnmpAdminString):
    """Custom type clmgmtLicensePermissionTicketFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClmgmtLicensePermissionTicketFile_Type.__name__ = "SnmpAdminString"
_ClmgmtLicensePermissionTicketFile_Object = MibTableColumn
clmgmtLicensePermissionTicketFile = _ClmgmtLicensePermissionTicketFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 11),
    _ClmgmtLicensePermissionTicketFile_Type()
)
clmgmtLicensePermissionTicketFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicensePermissionTicketFile.setStatus("current")


class _ClmgmtLicenseRehostTicketFile_Type(SnmpAdminString):
    """Custom type clmgmtLicenseRehostTicketFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClmgmtLicenseRehostTicketFile_Type.__name__ = "SnmpAdminString"
_ClmgmtLicenseRehostTicketFile_Object = MibTableColumn
clmgmtLicenseRehostTicketFile = _ClmgmtLicenseRehostTicketFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 12),
    _ClmgmtLicenseRehostTicketFile_Type()
)
clmgmtLicenseRehostTicketFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseRehostTicketFile.setStatus("current")


class _ClmgmtLicenseBackupFile_Type(SnmpAdminString):
    """Custom type clmgmtLicenseBackupFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClmgmtLicenseBackupFile_Type.__name__ = "SnmpAdminString"
_ClmgmtLicenseBackupFile_Object = MibTableColumn
clmgmtLicenseBackupFile = _ClmgmtLicenseBackupFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 13),
    _ClmgmtLicenseBackupFile_Type()
)
clmgmtLicenseBackupFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseBackupFile.setStatus("current")


class _ClmgmtLicenseStopOnFailure_Type(TruthValue):
    """Custom type clmgmtLicenseStopOnFailure based on TruthValue"""


_ClmgmtLicenseStopOnFailure_Object = MibTableColumn
clmgmtLicenseStopOnFailure = _ClmgmtLicenseStopOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 14),
    _ClmgmtLicenseStopOnFailure_Type()
)
clmgmtLicenseStopOnFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseStopOnFailure.setStatus("current")


class _ClmgmtLicenseAction_Type(Integer32):
    """Custom type clmgmtLicenseAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("backup", 6),
          ("clear", 3),
          ("generateEULA", 7),
          ("install", 2),
          ("noOp", 1),
          ("processPermissionTicket", 4),
          ("regenerateLastRehostTicket", 5))
    )


_ClmgmtLicenseAction_Type.__name__ = "Integer32"
_ClmgmtLicenseAction_Object = MibTableColumn
clmgmtLicenseAction = _ClmgmtLicenseAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 15),
    _ClmgmtLicenseAction_Type()
)
clmgmtLicenseAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseAction.setStatus("current")
_ClmgmtLicenseActionState_Type = ClmgmtLicenseActionState
_ClmgmtLicenseActionState_Object = MibTableColumn
clmgmtLicenseActionState = _ClmgmtLicenseActionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 16),
    _ClmgmtLicenseActionState_Type()
)
clmgmtLicenseActionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseActionState.setStatus("current")
_ClmgmtLicenseJobQPosition_Type = Unsigned32
_ClmgmtLicenseJobQPosition_Object = MibTableColumn
clmgmtLicenseJobQPosition = _ClmgmtLicenseJobQPosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 17),
    _ClmgmtLicenseJobQPosition_Type()
)
clmgmtLicenseJobQPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseJobQPosition.setStatus("current")
_ClmgmtLicenseActionFailCause_Type = ClmgmtLicenseActionFailCause
_ClmgmtLicenseActionFailCause_Object = MibTableColumn
clmgmtLicenseActionFailCause = _ClmgmtLicenseActionFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 18),
    _ClmgmtLicenseActionFailCause_Type()
)
clmgmtLicenseActionFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseActionFailCause.setStatus("current")


class _ClmgmtLicenseActionStorageType_Type(StorageType):
    """Custom type clmgmtLicenseActionStorageType based on StorageType"""


_ClmgmtLicenseActionStorageType_Object = MibTableColumn
clmgmtLicenseActionStorageType = _ClmgmtLicenseActionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 19),
    _ClmgmtLicenseActionStorageType_Type()
)
clmgmtLicenseActionStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseActionStorageType.setStatus("current")
_ClmgmtLicenseActionRowStatus_Type = RowStatus
_ClmgmtLicenseActionRowStatus_Object = MibTableColumn
clmgmtLicenseActionRowStatus = _ClmgmtLicenseActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 20),
    _ClmgmtLicenseActionRowStatus_Type()
)
clmgmtLicenseActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseActionRowStatus.setStatus("current")


class _ClmgmtLicenseAcceptEULA_Type(TruthValue):
    """Custom type clmgmtLicenseAcceptEULA based on TruthValue"""


_ClmgmtLicenseAcceptEULA_Object = MibTableColumn
clmgmtLicenseAcceptEULA = _ClmgmtLicenseAcceptEULA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 21),
    _ClmgmtLicenseAcceptEULA_Type()
)
clmgmtLicenseAcceptEULA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseAcceptEULA.setStatus("current")


class _ClmgmtLicenseEULAFile_Type(SnmpAdminString):
    """Custom type clmgmtLicenseEULAFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClmgmtLicenseEULAFile_Type.__name__ = "SnmpAdminString"
_ClmgmtLicenseEULAFile_Object = MibTableColumn
clmgmtLicenseEULAFile = _ClmgmtLicenseEULAFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 2, 1, 22),
    _ClmgmtLicenseEULAFile_Type()
)
clmgmtLicenseEULAFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtLicenseEULAFile.setStatus("current")
_ClmgmtLicenseActionResultTable_Object = MibTable
clmgmtLicenseActionResultTable = _ClmgmtLicenseActionResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 3)
)
if mibBuilder.loadTexts:
    clmgmtLicenseActionResultTable.setStatus("current")
_ClmgmtLicenseActionResultEntry_Object = MibTableRow
clmgmtLicenseActionResultEntry = _ClmgmtLicenseActionResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 3, 1)
)
clmgmtLicenseActionResultEntry.setIndexNames(
    (0, "CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseActionIndex"),
    (0, "CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseNumber"),
)
if mibBuilder.loadTexts:
    clmgmtLicenseActionResultEntry.setStatus("current")


class _ClmgmtLicenseNumber_Type(Unsigned32):
    """Custom type clmgmtLicenseNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ClmgmtLicenseNumber_Type.__name__ = "Unsigned32"
_ClmgmtLicenseNumber_Object = MibTableColumn
clmgmtLicenseNumber = _ClmgmtLicenseNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 3, 1, 1),
    _ClmgmtLicenseNumber_Type()
)
clmgmtLicenseNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmgmtLicenseNumber.setStatus("current")
_ClmgmtLicenseIndivActionState_Type = ClmgmtLicenseActionState
_ClmgmtLicenseIndivActionState_Object = MibTableColumn
clmgmtLicenseIndivActionState = _ClmgmtLicenseIndivActionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 3, 1, 2),
    _ClmgmtLicenseIndivActionState_Type()
)
clmgmtLicenseIndivActionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseIndivActionState.setStatus("current")
_ClmgmtLicenseIndivActionFailCause_Type = ClmgmtLicenseActionFailCause
_ClmgmtLicenseIndivActionFailCause_Object = MibTableColumn
clmgmtLicenseIndivActionFailCause = _ClmgmtLicenseIndivActionFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 1, 3, 1, 3),
    _ClmgmtLicenseIndivActionFailCause_Type()
)
clmgmtLicenseIndivActionFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseIndivActionFailCause.setStatus("current")
_ClmgmtLicenseInformation_ObjectIdentity = ObjectIdentity
clmgmtLicenseInformation = _ClmgmtLicenseInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2)
)
_ClmgmtLicenseStoreInfoTable_Object = MibTable
clmgmtLicenseStoreInfoTable = _ClmgmtLicenseStoreInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clmgmtLicenseStoreInfoTable.setStatus("current")
_ClmgmtLicenseStoreInfoEntry_Object = MibTableRow
clmgmtLicenseStoreInfoEntry = _ClmgmtLicenseStoreInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 1, 1)
)
clmgmtLicenseStoreInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseStoreIndex"),
)
if mibBuilder.loadTexts:
    clmgmtLicenseStoreInfoEntry.setStatus("current")


class _ClmgmtLicenseStoreIndex_Type(Unsigned32):
    """Custom type clmgmtLicenseStoreIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ClmgmtLicenseStoreIndex_Type.__name__ = "Unsigned32"
_ClmgmtLicenseStoreIndex_Object = MibTableColumn
clmgmtLicenseStoreIndex = _ClmgmtLicenseStoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 1, 1, 1),
    _ClmgmtLicenseStoreIndex_Type()
)
clmgmtLicenseStoreIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmgmtLicenseStoreIndex.setStatus("current")


class _ClmgmtLicenseStoreName_Type(SnmpAdminString):
    """Custom type clmgmtLicenseStoreName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClmgmtLicenseStoreName_Type.__name__ = "SnmpAdminString"
_ClmgmtLicenseStoreName_Object = MibTableColumn
clmgmtLicenseStoreName = _ClmgmtLicenseStoreName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 1, 1, 2),
    _ClmgmtLicenseStoreName_Type()
)
clmgmtLicenseStoreName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseStoreName.setStatus("current")
_ClmgmtLicenseStoreTotalSize_Type = Unsigned32
_ClmgmtLicenseStoreTotalSize_Object = MibTableColumn
clmgmtLicenseStoreTotalSize = _ClmgmtLicenseStoreTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 1, 1, 3),
    _ClmgmtLicenseStoreTotalSize_Type()
)
clmgmtLicenseStoreTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseStoreTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    clmgmtLicenseStoreTotalSize.setUnits("bytes")
_ClmgmtLicenseStoreSizeRemaining_Type = Unsigned32
_ClmgmtLicenseStoreSizeRemaining_Object = MibTableColumn
clmgmtLicenseStoreSizeRemaining = _ClmgmtLicenseStoreSizeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 1, 1, 4),
    _ClmgmtLicenseStoreSizeRemaining_Type()
)
clmgmtLicenseStoreSizeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseStoreSizeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    clmgmtLicenseStoreSizeRemaining.setUnits("bytes")
_ClmgmtLicenseDeviceInfoTable_Object = MibTable
clmgmtLicenseDeviceInfoTable = _ClmgmtLicenseDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 2)
)
if mibBuilder.loadTexts:
    clmgmtLicenseDeviceInfoTable.setStatus("current")
_ClmgmtLicenseDeviceInfoEntry_Object = MibTableRow
clmgmtLicenseDeviceInfoEntry = _ClmgmtLicenseDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 2, 1)
)
clmgmtLicenseDeviceInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    clmgmtLicenseDeviceInfoEntry.setStatus("current")


class _ClmgmtDefaultLicenseStore_Type(Unsigned32):
    """Custom type clmgmtDefaultLicenseStore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ClmgmtDefaultLicenseStore_Type.__name__ = "Unsigned32"
_ClmgmtDefaultLicenseStore_Object = MibTableColumn
clmgmtDefaultLicenseStore = _ClmgmtDefaultLicenseStore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 2, 1, 1),
    _ClmgmtDefaultLicenseStore_Type()
)
clmgmtDefaultLicenseStore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtDefaultLicenseStore.setStatus("current")
_ClmgmtLicenseInfoTable_Object = MibTable
clmgmtLicenseInfoTable = _ClmgmtLicenseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3)
)
if mibBuilder.loadTexts:
    clmgmtLicenseInfoTable.setStatus("current")
_ClmgmtLicenseInfoEntry_Object = MibTableRow
clmgmtLicenseInfoEntry = _ClmgmtLicenseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1)
)
clmgmtLicenseInfoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseStoreUsed"),
    (0, "CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseIndex"),
)
if mibBuilder.loadTexts:
    clmgmtLicenseInfoEntry.setStatus("current")


class _ClmgmtLicenseStoreUsed_Type(Unsigned32):
    """Custom type clmgmtLicenseStoreUsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ClmgmtLicenseStoreUsed_Type.__name__ = "Unsigned32"
_ClmgmtLicenseStoreUsed_Object = MibTableColumn
clmgmtLicenseStoreUsed = _ClmgmtLicenseStoreUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 1),
    _ClmgmtLicenseStoreUsed_Type()
)
clmgmtLicenseStoreUsed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmgmtLicenseStoreUsed.setStatus("current")
_ClmgmtLicenseIndex_Type = ClmgmtLicenseIndex
_ClmgmtLicenseIndex_Object = MibTableColumn
clmgmtLicenseIndex = _ClmgmtLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 2),
    _ClmgmtLicenseIndex_Type()
)
clmgmtLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmgmtLicenseIndex.setStatus("current")


class _ClmgmtLicenseFeatureName_Type(SnmpAdminString):
    """Custom type clmgmtLicenseFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ClmgmtLicenseFeatureName_Type.__name__ = "SnmpAdminString"
_ClmgmtLicenseFeatureName_Object = MibTableColumn
clmgmtLicenseFeatureName = _ClmgmtLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 3),
    _ClmgmtLicenseFeatureName_Type()
)
clmgmtLicenseFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseFeatureName.setStatus("current")


class _ClmgmtLicenseFeatureVersion_Type(SnmpAdminString):
    """Custom type clmgmtLicenseFeatureVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ClmgmtLicenseFeatureVersion_Type.__name__ = "SnmpAdminString"
_ClmgmtLicenseFeatureVersion_Object = MibTableColumn
clmgmtLicenseFeatureVersion = _ClmgmtLicenseFeatureVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 4),
    _ClmgmtLicenseFeatureVersion_Type()
)
clmgmtLicenseFeatureVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseFeatureVersion.setStatus("current")


class _ClmgmtLicenseType_Type(Integer32):
    """Custom type clmgmtLicenseType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("demo", 1),
          ("evalRightToUse", 8),
          ("evaluationSubscription", 6),
          ("extension", 2),
          ("extensionSubscription", 7),
          ("gracePeriod", 3),
          ("paidSubscription", 5),
          ("permanent", 4),
          ("permanentRightToUse", 10),
          ("rightToUse", 9))
    )


_ClmgmtLicenseType_Type.__name__ = "Integer32"
_ClmgmtLicenseType_Object = MibTableColumn
clmgmtLicenseType = _ClmgmtLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 5),
    _ClmgmtLicenseType_Type()
)
clmgmtLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseType.setStatus("current")
_ClmgmtLicenseCounted_Type = TruthValue
_ClmgmtLicenseCounted_Object = MibTableColumn
clmgmtLicenseCounted = _ClmgmtLicenseCounted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 6),
    _ClmgmtLicenseCounted_Type()
)
clmgmtLicenseCounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseCounted.setStatus("current")
_ClmgmtLicenseValidityPeriod_Type = Unsigned32
_ClmgmtLicenseValidityPeriod_Object = MibTableColumn
clmgmtLicenseValidityPeriod = _ClmgmtLicenseValidityPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 7),
    _ClmgmtLicenseValidityPeriod_Type()
)
clmgmtLicenseValidityPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseValidityPeriod.setStatus("current")
if mibBuilder.loadTexts:
    clmgmtLicenseValidityPeriod.setUnits("seconds")
_ClmgmtLicenseValidityPeriodRemaining_Type = Unsigned32
_ClmgmtLicenseValidityPeriodRemaining_Object = MibTableColumn
clmgmtLicenseValidityPeriodRemaining = _ClmgmtLicenseValidityPeriodRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 8),
    _ClmgmtLicenseValidityPeriodRemaining_Type()
)
clmgmtLicenseValidityPeriodRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseValidityPeriodRemaining.setStatus("current")
if mibBuilder.loadTexts:
    clmgmtLicenseValidityPeriodRemaining.setUnits("seconds")
_ClmgmtLicenseExpiredPeriod_Type = Unsigned32
_ClmgmtLicenseExpiredPeriod_Object = MibTableColumn
clmgmtLicenseExpiredPeriod = _ClmgmtLicenseExpiredPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 9),
    _ClmgmtLicenseExpiredPeriod_Type()
)
clmgmtLicenseExpiredPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseExpiredPeriod.setStatus("current")
if mibBuilder.loadTexts:
    clmgmtLicenseExpiredPeriod.setUnits("seconds")
_ClmgmtLicenseMaxUsageCount_Type = Unsigned32
_ClmgmtLicenseMaxUsageCount_Object = MibTableColumn
clmgmtLicenseMaxUsageCount = _ClmgmtLicenseMaxUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 10),
    _ClmgmtLicenseMaxUsageCount_Type()
)
clmgmtLicenseMaxUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseMaxUsageCount.setStatus("current")
_ClmgmtLicenseUsageCountRemaining_Type = Unsigned32
_ClmgmtLicenseUsageCountRemaining_Object = MibTableColumn
clmgmtLicenseUsageCountRemaining = _ClmgmtLicenseUsageCountRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 11),
    _ClmgmtLicenseUsageCountRemaining_Type()
)
clmgmtLicenseUsageCountRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseUsageCountRemaining.setStatus("current")
_ClmgmtLicenseEULAStatus_Type = TruthValue
_ClmgmtLicenseEULAStatus_Object = MibTableColumn
clmgmtLicenseEULAStatus = _ClmgmtLicenseEULAStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 12),
    _ClmgmtLicenseEULAStatus_Type()
)
clmgmtLicenseEULAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseEULAStatus.setStatus("current")


class _ClmgmtLicenseComments_Type(SnmpAdminString):
    """Custom type clmgmtLicenseComments based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClmgmtLicenseComments_Type.__name__ = "SnmpAdminString"
_ClmgmtLicenseComments_Object = MibTableColumn
clmgmtLicenseComments = _ClmgmtLicenseComments_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 13),
    _ClmgmtLicenseComments_Type()
)
clmgmtLicenseComments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmgmtLicenseComments.setStatus("current")


class _ClmgmtLicenseStatus_Type(Integer32):
    """Custom type clmgmtLicenseStatus based on Integer32"""
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
        *(("expiredInUse", 4),
          ("expiredNotInUse", 5),
          ("inUse", 3),
          ("inactive", 1),
          ("notInUse", 2),
          ("usageCountConsumed", 6))
    )


_ClmgmtLicenseStatus_Type.__name__ = "Integer32"
_ClmgmtLicenseStatus_Object = MibTableColumn
clmgmtLicenseStatus = _ClmgmtLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 14),
    _ClmgmtLicenseStatus_Type()
)
clmgmtLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseStatus.setStatus("current")
_ClmgmtLicenseStartDate_Type = DateAndTime
_ClmgmtLicenseStartDate_Object = MibTableColumn
clmgmtLicenseStartDate = _ClmgmtLicenseStartDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 15),
    _ClmgmtLicenseStartDate_Type()
)
clmgmtLicenseStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseStartDate.setStatus("current")
_ClmgmtLicenseEndDate_Type = DateAndTime
_ClmgmtLicenseEndDate_Object = MibTableColumn
clmgmtLicenseEndDate = _ClmgmtLicenseEndDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 16),
    _ClmgmtLicenseEndDate_Type()
)
clmgmtLicenseEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicenseEndDate.setStatus("current")
_ClmgmtLicensePeriodUsed_Type = Unsigned32
_ClmgmtLicensePeriodUsed_Object = MibTableColumn
clmgmtLicensePeriodUsed = _ClmgmtLicensePeriodUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 3, 1, 17),
    _ClmgmtLicensePeriodUsed_Type()
)
clmgmtLicensePeriodUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtLicensePeriodUsed.setStatus("current")
if mibBuilder.loadTexts:
    clmgmtLicensePeriodUsed.setUnits("seconds")
_ClmgmtLicensableFeatureTable_Object = MibTable
clmgmtLicensableFeatureTable = _ClmgmtLicensableFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 4)
)
if mibBuilder.loadTexts:
    clmgmtLicensableFeatureTable.setStatus("current")
_ClmgmtLicensableFeatureEntry_Object = MibTableRow
clmgmtLicensableFeatureEntry = _ClmgmtLicensableFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 4, 1)
)
clmgmtLicensableFeatureEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureIndex"),
)
if mibBuilder.loadTexts:
    clmgmtLicensableFeatureEntry.setStatus("current")


class _ClmgmtFeatureIndex_Type(Unsigned32):
    """Custom type clmgmtFeatureIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ClmgmtFeatureIndex_Type.__name__ = "Unsigned32"
_ClmgmtFeatureIndex_Object = MibTableColumn
clmgmtFeatureIndex = _ClmgmtFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 4, 1, 1),
    _ClmgmtFeatureIndex_Type()
)
clmgmtFeatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmgmtFeatureIndex.setStatus("current")


class _ClmgmtFeatureName_Type(SnmpAdminString):
    """Custom type clmgmtFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ClmgmtFeatureName_Type.__name__ = "SnmpAdminString"
_ClmgmtFeatureName_Object = MibTableColumn
clmgmtFeatureName = _ClmgmtFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 4, 1, 2),
    _ClmgmtFeatureName_Type()
)
clmgmtFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtFeatureName.setStatus("current")


class _ClmgmtFeatureVersion_Type(SnmpAdminString):
    """Custom type clmgmtFeatureVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClmgmtFeatureVersion_Type.__name__ = "SnmpAdminString"
_ClmgmtFeatureVersion_Object = MibTableColumn
clmgmtFeatureVersion = _ClmgmtFeatureVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 4, 1, 3),
    _ClmgmtFeatureVersion_Type()
)
clmgmtFeatureVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtFeatureVersion.setStatus("current")
_ClmgmtFeatureValidityPeriodRemaining_Type = Unsigned32
_ClmgmtFeatureValidityPeriodRemaining_Object = MibTableColumn
clmgmtFeatureValidityPeriodRemaining = _ClmgmtFeatureValidityPeriodRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 4, 1, 4),
    _ClmgmtFeatureValidityPeriodRemaining_Type()
)
clmgmtFeatureValidityPeriodRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtFeatureValidityPeriodRemaining.setStatus("current")
if mibBuilder.loadTexts:
    clmgmtFeatureValidityPeriodRemaining.setUnits("seconds")


class _ClmgmtFeatureWhatIsCounted_Type(SnmpAdminString):
    """Custom type clmgmtFeatureWhatIsCounted based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ClmgmtFeatureWhatIsCounted_Type.__name__ = "SnmpAdminString"
_ClmgmtFeatureWhatIsCounted_Object = MibTableColumn
clmgmtFeatureWhatIsCounted = _ClmgmtFeatureWhatIsCounted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 4, 1, 5),
    _ClmgmtFeatureWhatIsCounted_Type()
)
clmgmtFeatureWhatIsCounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtFeatureWhatIsCounted.setStatus("current")
_ClmgmtFeatureStartDate_Type = DateAndTime
_ClmgmtFeatureStartDate_Object = MibTableColumn
clmgmtFeatureStartDate = _ClmgmtFeatureStartDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 4, 1, 6),
    _ClmgmtFeatureStartDate_Type()
)
clmgmtFeatureStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtFeatureStartDate.setStatus("current")
_ClmgmtFeatureEndDate_Type = DateAndTime
_ClmgmtFeatureEndDate_Object = MibTableColumn
clmgmtFeatureEndDate = _ClmgmtFeatureEndDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 4, 1, 7),
    _ClmgmtFeatureEndDate_Type()
)
clmgmtFeatureEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtFeatureEndDate.setStatus("current")
_ClmgmtFeaturePeriodUsed_Type = Unsigned32
_ClmgmtFeaturePeriodUsed_Object = MibTableColumn
clmgmtFeaturePeriodUsed = _ClmgmtFeaturePeriodUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 2, 4, 1, 8),
    _ClmgmtFeaturePeriodUsed_Type()
)
clmgmtFeaturePeriodUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtFeaturePeriodUsed.setStatus("current")
if mibBuilder.loadTexts:
    clmgmtFeaturePeriodUsed.setUnits("seconds")
_ClmgmtLicenseDeviceInformation_ObjectIdentity = ObjectIdentity
clmgmtLicenseDeviceInformation = _ClmgmtLicenseDeviceInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3)
)
_ClmgmtNextFreeDevCredExportActionIndex_Type = Unsigned32
_ClmgmtNextFreeDevCredExportActionIndex_Object = MibScalar
clmgmtNextFreeDevCredExportActionIndex = _ClmgmtNextFreeDevCredExportActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 1),
    _ClmgmtNextFreeDevCredExportActionIndex_Type()
)
clmgmtNextFreeDevCredExportActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtNextFreeDevCredExportActionIndex.setStatus("current")
_ClmgmtDevCredExportActionTable_Object = MibTable
clmgmtDevCredExportActionTable = _ClmgmtDevCredExportActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2)
)
if mibBuilder.loadTexts:
    clmgmtDevCredExportActionTable.setStatus("current")
_ClmgmtDevCredExportActionEntry_Object = MibTableRow
clmgmtDevCredExportActionEntry = _ClmgmtDevCredExportActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1)
)
clmgmtDevCredExportActionEntry.setIndexNames(
    (0, "CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredExportActionIndex"),
)
if mibBuilder.loadTexts:
    clmgmtDevCredExportActionEntry.setStatus("current")


class _ClmgmtDevCredExportActionIndex_Type(Unsigned32):
    """Custom type clmgmtDevCredExportActionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ClmgmtDevCredExportActionIndex_Type.__name__ = "Unsigned32"
_ClmgmtDevCredExportActionIndex_Object = MibTableColumn
clmgmtDevCredExportActionIndex = _ClmgmtDevCredExportActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 1),
    _ClmgmtDevCredExportActionIndex_Type()
)
clmgmtDevCredExportActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmgmtDevCredExportActionIndex.setStatus("current")


class _ClmgmtDevCredEntPhysicalIndex_Type(PhysicalIndexOrZero):
    """Custom type clmgmtDevCredEntPhysicalIndex based on PhysicalIndexOrZero"""
    defaultValue = 0


_ClmgmtDevCredEntPhysicalIndex_Object = MibTableColumn
clmgmtDevCredEntPhysicalIndex = _ClmgmtDevCredEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 2),
    _ClmgmtDevCredEntPhysicalIndex_Type()
)
clmgmtDevCredEntPhysicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtDevCredEntPhysicalIndex.setStatus("current")


class _ClmgmtDevCredTransferProtocol_Type(ClmgmtLicenseTransferProtocol):
    """Custom type clmgmtDevCredTransferProtocol based on ClmgmtLicenseTransferProtocol"""


_ClmgmtDevCredTransferProtocol_Object = MibTableColumn
clmgmtDevCredTransferProtocol = _ClmgmtDevCredTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 3),
    _ClmgmtDevCredTransferProtocol_Type()
)
clmgmtDevCredTransferProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtDevCredTransferProtocol.setStatus("current")


class _ClmgmtDevCredServerAddressType_Type(InetAddressType):
    """Custom type clmgmtDevCredServerAddressType based on InetAddressType"""


_ClmgmtDevCredServerAddressType_Object = MibTableColumn
clmgmtDevCredServerAddressType = _ClmgmtDevCredServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 4),
    _ClmgmtDevCredServerAddressType_Type()
)
clmgmtDevCredServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtDevCredServerAddressType.setStatus("current")
_ClmgmtDevCredServerAddress_Type = InetAddress
_ClmgmtDevCredServerAddress_Object = MibTableColumn
clmgmtDevCredServerAddress = _ClmgmtDevCredServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 5),
    _ClmgmtDevCredServerAddress_Type()
)
clmgmtDevCredServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtDevCredServerAddress.setStatus("current")


class _ClmgmtDevCredServerUsername_Type(SnmpAdminString):
    """Custom type clmgmtDevCredServerUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_ClmgmtDevCredServerUsername_Type.__name__ = "SnmpAdminString"
_ClmgmtDevCredServerUsername_Object = MibTableColumn
clmgmtDevCredServerUsername = _ClmgmtDevCredServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 6),
    _ClmgmtDevCredServerUsername_Type()
)
clmgmtDevCredServerUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtDevCredServerUsername.setStatus("current")


class _ClmgmtDevCredServerPassword_Type(SnmpAdminString):
    """Custom type clmgmtDevCredServerPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_ClmgmtDevCredServerPassword_Type.__name__ = "SnmpAdminString"
_ClmgmtDevCredServerPassword_Object = MibTableColumn
clmgmtDevCredServerPassword = _ClmgmtDevCredServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 7),
    _ClmgmtDevCredServerPassword_Type()
)
clmgmtDevCredServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtDevCredServerPassword.setStatus("current")


class _ClmgmtDevCredExportFile_Type(SnmpAdminString):
    """Custom type clmgmtDevCredExportFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClmgmtDevCredExportFile_Type.__name__ = "SnmpAdminString"
_ClmgmtDevCredExportFile_Object = MibTableColumn
clmgmtDevCredExportFile = _ClmgmtDevCredExportFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 8),
    _ClmgmtDevCredExportFile_Type()
)
clmgmtDevCredExportFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtDevCredExportFile.setStatus("current")


class _ClmgmtDevCredCommand_Type(Integer32):
    """Custom type clmgmtDevCredCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("getDeviceCredentials", 2),
          ("noOp", 1))
    )


_ClmgmtDevCredCommand_Type.__name__ = "Integer32"
_ClmgmtDevCredCommand_Object = MibTableColumn
clmgmtDevCredCommand = _ClmgmtDevCredCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 9),
    _ClmgmtDevCredCommand_Type()
)
clmgmtDevCredCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtDevCredCommand.setStatus("current")
_ClmgmtDevCredCommandState_Type = ClmgmtLicenseActionState
_ClmgmtDevCredCommandState_Object = MibTableColumn
clmgmtDevCredCommandState = _ClmgmtDevCredCommandState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 10),
    _ClmgmtDevCredCommandState_Type()
)
clmgmtDevCredCommandState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtDevCredCommandState.setStatus("current")


class _ClmgmtDevCredCommandFailCause_Type(Integer32):
    """Custom type clmgmtDevCredCommandFailCause based on Integer32"""
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
        *(("fileServerNotReachable", 4),
          ("invalidFile", 6),
          ("none", 1),
          ("transferProtocolNotSupported", 3),
          ("unknownError", 2),
          ("unrecognizedEntPhysicalIndex", 5))
    )


_ClmgmtDevCredCommandFailCause_Type.__name__ = "Integer32"
_ClmgmtDevCredCommandFailCause_Object = MibTableColumn
clmgmtDevCredCommandFailCause = _ClmgmtDevCredCommandFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 11),
    _ClmgmtDevCredCommandFailCause_Type()
)
clmgmtDevCredCommandFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmgmtDevCredCommandFailCause.setStatus("current")


class _ClmgmtDevCredStorageType_Type(StorageType):
    """Custom type clmgmtDevCredStorageType based on StorageType"""


_ClmgmtDevCredStorageType_Object = MibTableColumn
clmgmtDevCredStorageType = _ClmgmtDevCredStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 12),
    _ClmgmtDevCredStorageType_Type()
)
clmgmtDevCredStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtDevCredStorageType.setStatus("current")
_ClmgmtDevCredRowStatus_Type = RowStatus
_ClmgmtDevCredRowStatus_Object = MibTableColumn
clmgmtDevCredRowStatus = _ClmgmtDevCredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 3, 2, 1, 13),
    _ClmgmtDevCredRowStatus_Type()
)
clmgmtDevCredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clmgmtDevCredRowStatus.setStatus("current")
_ClmgmtLicenseNotifObjects_ObjectIdentity = ObjectIdentity
clmgmtLicenseNotifObjects = _ClmgmtLicenseNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 4)
)


class _ClmgmtLicenseUsageNotifEnable_Type(TruthValue):
    """Custom type clmgmtLicenseUsageNotifEnable based on TruthValue"""


_ClmgmtLicenseUsageNotifEnable_Object = MibScalar
clmgmtLicenseUsageNotifEnable = _ClmgmtLicenseUsageNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 4, 1),
    _ClmgmtLicenseUsageNotifEnable_Type()
)
clmgmtLicenseUsageNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmgmtLicenseUsageNotifEnable.setStatus("current")


class _ClmgmtLicenseDeploymentNotifEnable_Type(TruthValue):
    """Custom type clmgmtLicenseDeploymentNotifEnable based on TruthValue"""


_ClmgmtLicenseDeploymentNotifEnable_Object = MibScalar
clmgmtLicenseDeploymentNotifEnable = _ClmgmtLicenseDeploymentNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 4, 2),
    _ClmgmtLicenseDeploymentNotifEnable_Type()
)
clmgmtLicenseDeploymentNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmgmtLicenseDeploymentNotifEnable.setStatus("current")


class _ClmgmtLicenseErrorNotifEnable_Type(TruthValue):
    """Custom type clmgmtLicenseErrorNotifEnable based on TruthValue"""


_ClmgmtLicenseErrorNotifEnable_Object = MibScalar
clmgmtLicenseErrorNotifEnable = _ClmgmtLicenseErrorNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 1, 4, 3),
    _ClmgmtLicenseErrorNotifEnable_Type()
)
clmgmtLicenseErrorNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmgmtLicenseErrorNotifEnable.setStatus("current")
_CiscoLicenseMgmtMIBConform_ObjectIdentity = ObjectIdentity
ciscoLicenseMgmtMIBConform = _CiscoLicenseMgmtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2)
)
_CiscoLicenseMgmtCompliances_ObjectIdentity = ObjectIdentity
ciscoLicenseMgmtCompliances = _CiscoLicenseMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 1)
)
_CiscoLicenseMgmtGroups_ObjectIdentity = ObjectIdentity
ciscoLicenseMgmtGroups = _CiscoLicenseMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2)
)

# Managed Objects groups

clmgmtLicenseDeploymentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 1)
)
clmgmtLicenseDeploymentGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtNextFreeLicenseActionIndex"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseActionEntPhysicalIndex"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseActionTransferProtocol"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseServerAddressType"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseServerAddress"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseServerUsername"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseServerPassword"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFile"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseStore"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseActionLicenseIndex"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicensePermissionTicketFile"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseRehostTicketFile"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseBackupFile"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseStopOnFailure"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseAction"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseActionState"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseJobQPosition"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseActionFailCause"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseActionStorageType"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseActionRowStatus"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseIndivActionState"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseIndivActionFailCause"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseAcceptEULA"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseEULAFile"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseDeploymentGroup.setStatus("current")

clmgmtLicenseStoreInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 2)
)
clmgmtLicenseStoreInformationGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseStoreName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseStoreTotalSize"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseStoreSizeRemaining"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseStoreInformationGroup.setStatus("current")

clmgmtLicenseDeviceInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 3)
)
clmgmtLicenseDeviceInformationGroup.setObjects(
    ("CISCO-LICENSE-MGMT-MIB", "clmgmtDefaultLicenseStore")
)
if mibBuilder.loadTexts:
    clmgmtLicenseDeviceInformationGroup.setStatus("current")

clmgmtLicenseInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 4)
)
clmgmtLicenseInformationGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseType"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseCounted"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseValidityPeriod"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseValidityPeriodRemaining"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseExpiredPeriod"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseMaxUsageCount"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseUsageCountRemaining"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseEULAStatus"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseComments"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseStatus"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseInformationGroup.setStatus("current")

clmgmtLicensableFeatureInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 5)
)
clmgmtLicensableFeatureInformationGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureValidityPeriodRemaining"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureWhatIsCounted"))
)
if mibBuilder.loadTexts:
    clmgmtLicensableFeatureInformationGroup.setStatus("current")

clmgmtLicenseDevCredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 6)
)
clmgmtLicenseDevCredGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtNextFreeDevCredExportActionIndex"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredEntPhysicalIndex"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredTransferProtocol"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredServerAddressType"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredServerAddress"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredServerUsername"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredServerPassword"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredExportFile"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredCommand"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredCommandState"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredCommandFailCause"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredStorageType"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtDevCredRowStatus"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseDevCredGroup.setStatus("current")

clmgmtLicenseNotificationEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 7)
)
clmgmtLicenseNotificationEnableGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseUsageNotifEnable"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseDeploymentNotifEnable"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseErrorNotifEnable"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseNotificationEnableGroup.setStatus("current")

clmgmtLicenseSubscriptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 11)
)
clmgmtLicenseSubscriptionGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseStartDate"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseEndDate"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureStartDate"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureEndDate"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseSubscriptionGroup.setStatus("current")

clmgmtLicenseRTUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 13)
)
clmgmtLicenseRTUGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicensePeriodUsed"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeaturePeriodUsed"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseRTUGroup.setStatus("current")


# Notification objects

clmgmtLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 1)
)
clmgmtLicenseExpired.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureVersion"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseExpired.setStatus(
        "current"
    )

clmgmtLicenseExpiryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 2)
)
clmgmtLicenseExpiryWarning.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureValidityPeriodRemaining"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseExpiryWarning.setStatus(
        "current"
    )

clmgmtLicenseUsageCountExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 3)
)
clmgmtLicenseUsageCountExceeded.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseMaxUsageCount"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureWhatIsCounted"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseComments"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseUsageCountExceeded.setStatus(
        "current"
    )

clmgmtLicenseUsageCountAboutToExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 4)
)
clmgmtLicenseUsageCountAboutToExceed.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseMaxUsageCount"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseUsageCountRemaining"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureWhatIsCounted"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseComments"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseUsageCountAboutToExceed.setStatus(
        "current"
    )

clmgmtLicenseInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 5)
)
clmgmtLicenseInstalled.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseType"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseComments"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseInstalled.setStatus(
        "current"
    )

clmgmtLicenseCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 6)
)
clmgmtLicenseCleared.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseType"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseComments"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseCleared.setStatus(
        "current"
    )

clmgmtLicenseRevoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 7)
)
clmgmtLicenseRevoked.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseType"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseComments"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseRevoked.setStatus(
        "current"
    )

clmgmtLicenseEULAAccepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 8)
)
clmgmtLicenseEULAAccepted.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureVersion"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseEULAAccepted.setStatus(
        "current"
    )

clmgmtLicenseNotEnforced = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 9)
)
clmgmtLicenseNotEnforced.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureVersion"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseNotEnforced.setStatus(
        "current"
    )

clmgmtLicenseSubscriptionExpiryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 10)
)
clmgmtLicenseSubscriptionExpiryWarning.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureEndDate"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseSubscriptionExpiryWarning.setStatus(
        "current"
    )

clmgmtLicenseSubscriptionExtExpiryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 11)
)
clmgmtLicenseSubscriptionExtExpiryWarning.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureEndDate"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseSubscriptionExtExpiryWarning.setStatus(
        "current"
    )

clmgmtLicenseSubscriptionExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 12)
)
clmgmtLicenseSubscriptionExpired.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureEndDate"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseSubscriptionExpired.setStatus(
        "current"
    )

clmgmtLicenseEvalRTUTransitionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 13)
)
clmgmtLicenseEvalRTUTransitionWarning.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureVersion"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureValidityPeriodRemaining"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseEvalRTUTransitionWarning.setStatus(
        "current"
    )

clmgmtLicenseEvalRTUTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 0, 14)
)
clmgmtLicenseEvalRTUTransition.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureName"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtFeatureVersion"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseEvalRTUTransition.setStatus(
        "current"
    )


# Notifications groups

clmgmtLicenseUsageNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 8)
)
clmgmtLicenseUsageNotifGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseExpired"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseExpiryWarning"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseUsageCountExceeded"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseUsageCountAboutToExceed"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseUsageNotifGroup.setStatus(
        "current"
    )

clmgmtLicenseDeploymentNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 9)
)
clmgmtLicenseDeploymentNotifGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseInstalled"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseCleared"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseRevoked"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseEULAAccepted"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseDeploymentNotifGroup.setStatus(
        "current"
    )

clmgmtLicenseErrorNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 10)
)
clmgmtLicenseErrorNotifGroup.setObjects(
    ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseNotEnforced")
)
if mibBuilder.loadTexts:
    clmgmtLicenseErrorNotifGroup.setStatus(
        "current"
    )

clmgmtLicenseSubscriptionUsageNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 12)
)
clmgmtLicenseSubscriptionUsageNotifGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseSubscriptionExpiryWarning"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseSubscriptionExtExpiryWarning"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseSubscriptionExpired"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseSubscriptionUsageNotifGroup.setStatus(
        "current"
    )

clmgmtLicenseRTUUsageNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 2, 14)
)
clmgmtLicenseRTUUsageNotifGroup.setObjects(
      *(("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseEvalRTUTransitionWarning"),
        ("CISCO-LICENSE-MGMT-MIB", "clmgmtLicenseEvalRTUTransition"))
)
if mibBuilder.loadTexts:
    clmgmtLicenseRTUUsageNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLicenseMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLicenseMgmtCompliance.setStatus(
        "deprecated"
    )

ciscoLicenseMgmtComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 543, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLicenseMgmtComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LICENSE-MGMT-MIB",
    **{"ClmgmtLicenseIndex": ClmgmtLicenseIndex,
       "ClmgmtLicenseIndexOrZero": ClmgmtLicenseIndexOrZero,
       "ClmgmtLicenseTransferProtocol": ClmgmtLicenseTransferProtocol,
       "ClmgmtLicenseActionState": ClmgmtLicenseActionState,
       "ClmgmtLicenseActionFailCause": ClmgmtLicenseActionFailCause,
       "ciscoLicenseMgmtMIB": ciscoLicenseMgmtMIB,
       "ciscoLicenseMgmtMIBNotifs": ciscoLicenseMgmtMIBNotifs,
       "clmgmtLicenseExpired": clmgmtLicenseExpired,
       "clmgmtLicenseExpiryWarning": clmgmtLicenseExpiryWarning,
       "clmgmtLicenseUsageCountExceeded": clmgmtLicenseUsageCountExceeded,
       "clmgmtLicenseUsageCountAboutToExceed": clmgmtLicenseUsageCountAboutToExceed,
       "clmgmtLicenseInstalled": clmgmtLicenseInstalled,
       "clmgmtLicenseCleared": clmgmtLicenseCleared,
       "clmgmtLicenseRevoked": clmgmtLicenseRevoked,
       "clmgmtLicenseEULAAccepted": clmgmtLicenseEULAAccepted,
       "clmgmtLicenseNotEnforced": clmgmtLicenseNotEnforced,
       "clmgmtLicenseSubscriptionExpiryWarning": clmgmtLicenseSubscriptionExpiryWarning,
       "clmgmtLicenseSubscriptionExtExpiryWarning": clmgmtLicenseSubscriptionExtExpiryWarning,
       "clmgmtLicenseSubscriptionExpired": clmgmtLicenseSubscriptionExpired,
       "clmgmtLicenseEvalRTUTransitionWarning": clmgmtLicenseEvalRTUTransitionWarning,
       "clmgmtLicenseEvalRTUTransition": clmgmtLicenseEvalRTUTransition,
       "ciscoLicenseMgmtMIBObjects": ciscoLicenseMgmtMIBObjects,
       "clmgmtLicenseConfiguration": clmgmtLicenseConfiguration,
       "clmgmtNextFreeLicenseActionIndex": clmgmtNextFreeLicenseActionIndex,
       "clmgmtLicenseActionTable": clmgmtLicenseActionTable,
       "clmgmtLicenseActionEntry": clmgmtLicenseActionEntry,
       "clmgmtLicenseActionIndex": clmgmtLicenseActionIndex,
       "clmgmtLicenseActionEntPhysicalIndex": clmgmtLicenseActionEntPhysicalIndex,
       "clmgmtLicenseActionTransferProtocol": clmgmtLicenseActionTransferProtocol,
       "clmgmtLicenseServerAddressType": clmgmtLicenseServerAddressType,
       "clmgmtLicenseServerAddress": clmgmtLicenseServerAddress,
       "clmgmtLicenseServerUsername": clmgmtLicenseServerUsername,
       "clmgmtLicenseServerPassword": clmgmtLicenseServerPassword,
       "clmgmtLicenseFile": clmgmtLicenseFile,
       "clmgmtLicenseStore": clmgmtLicenseStore,
       "clmgmtLicenseActionLicenseIndex": clmgmtLicenseActionLicenseIndex,
       "clmgmtLicensePermissionTicketFile": clmgmtLicensePermissionTicketFile,
       "clmgmtLicenseRehostTicketFile": clmgmtLicenseRehostTicketFile,
       "clmgmtLicenseBackupFile": clmgmtLicenseBackupFile,
       "clmgmtLicenseStopOnFailure": clmgmtLicenseStopOnFailure,
       "clmgmtLicenseAction": clmgmtLicenseAction,
       "clmgmtLicenseActionState": clmgmtLicenseActionState,
       "clmgmtLicenseJobQPosition": clmgmtLicenseJobQPosition,
       "clmgmtLicenseActionFailCause": clmgmtLicenseActionFailCause,
       "clmgmtLicenseActionStorageType": clmgmtLicenseActionStorageType,
       "clmgmtLicenseActionRowStatus": clmgmtLicenseActionRowStatus,
       "clmgmtLicenseAcceptEULA": clmgmtLicenseAcceptEULA,
       "clmgmtLicenseEULAFile": clmgmtLicenseEULAFile,
       "clmgmtLicenseActionResultTable": clmgmtLicenseActionResultTable,
       "clmgmtLicenseActionResultEntry": clmgmtLicenseActionResultEntry,
       "clmgmtLicenseNumber": clmgmtLicenseNumber,
       "clmgmtLicenseIndivActionState": clmgmtLicenseIndivActionState,
       "clmgmtLicenseIndivActionFailCause": clmgmtLicenseIndivActionFailCause,
       "clmgmtLicenseInformation": clmgmtLicenseInformation,
       "clmgmtLicenseStoreInfoTable": clmgmtLicenseStoreInfoTable,
       "clmgmtLicenseStoreInfoEntry": clmgmtLicenseStoreInfoEntry,
       "clmgmtLicenseStoreIndex": clmgmtLicenseStoreIndex,
       "clmgmtLicenseStoreName": clmgmtLicenseStoreName,
       "clmgmtLicenseStoreTotalSize": clmgmtLicenseStoreTotalSize,
       "clmgmtLicenseStoreSizeRemaining": clmgmtLicenseStoreSizeRemaining,
       "clmgmtLicenseDeviceInfoTable": clmgmtLicenseDeviceInfoTable,
       "clmgmtLicenseDeviceInfoEntry": clmgmtLicenseDeviceInfoEntry,
       "clmgmtDefaultLicenseStore": clmgmtDefaultLicenseStore,
       "clmgmtLicenseInfoTable": clmgmtLicenseInfoTable,
       "clmgmtLicenseInfoEntry": clmgmtLicenseInfoEntry,
       "clmgmtLicenseStoreUsed": clmgmtLicenseStoreUsed,
       "clmgmtLicenseIndex": clmgmtLicenseIndex,
       "clmgmtLicenseFeatureName": clmgmtLicenseFeatureName,
       "clmgmtLicenseFeatureVersion": clmgmtLicenseFeatureVersion,
       "clmgmtLicenseType": clmgmtLicenseType,
       "clmgmtLicenseCounted": clmgmtLicenseCounted,
       "clmgmtLicenseValidityPeriod": clmgmtLicenseValidityPeriod,
       "clmgmtLicenseValidityPeriodRemaining": clmgmtLicenseValidityPeriodRemaining,
       "clmgmtLicenseExpiredPeriod": clmgmtLicenseExpiredPeriod,
       "clmgmtLicenseMaxUsageCount": clmgmtLicenseMaxUsageCount,
       "clmgmtLicenseUsageCountRemaining": clmgmtLicenseUsageCountRemaining,
       "clmgmtLicenseEULAStatus": clmgmtLicenseEULAStatus,
       "clmgmtLicenseComments": clmgmtLicenseComments,
       "clmgmtLicenseStatus": clmgmtLicenseStatus,
       "clmgmtLicenseStartDate": clmgmtLicenseStartDate,
       "clmgmtLicenseEndDate": clmgmtLicenseEndDate,
       "clmgmtLicensePeriodUsed": clmgmtLicensePeriodUsed,
       "clmgmtLicensableFeatureTable": clmgmtLicensableFeatureTable,
       "clmgmtLicensableFeatureEntry": clmgmtLicensableFeatureEntry,
       "clmgmtFeatureIndex": clmgmtFeatureIndex,
       "clmgmtFeatureName": clmgmtFeatureName,
       "clmgmtFeatureVersion": clmgmtFeatureVersion,
       "clmgmtFeatureValidityPeriodRemaining": clmgmtFeatureValidityPeriodRemaining,
       "clmgmtFeatureWhatIsCounted": clmgmtFeatureWhatIsCounted,
       "clmgmtFeatureStartDate": clmgmtFeatureStartDate,
       "clmgmtFeatureEndDate": clmgmtFeatureEndDate,
       "clmgmtFeaturePeriodUsed": clmgmtFeaturePeriodUsed,
       "clmgmtLicenseDeviceInformation": clmgmtLicenseDeviceInformation,
       "clmgmtNextFreeDevCredExportActionIndex": clmgmtNextFreeDevCredExportActionIndex,
       "clmgmtDevCredExportActionTable": clmgmtDevCredExportActionTable,
       "clmgmtDevCredExportActionEntry": clmgmtDevCredExportActionEntry,
       "clmgmtDevCredExportActionIndex": clmgmtDevCredExportActionIndex,
       "clmgmtDevCredEntPhysicalIndex": clmgmtDevCredEntPhysicalIndex,
       "clmgmtDevCredTransferProtocol": clmgmtDevCredTransferProtocol,
       "clmgmtDevCredServerAddressType": clmgmtDevCredServerAddressType,
       "clmgmtDevCredServerAddress": clmgmtDevCredServerAddress,
       "clmgmtDevCredServerUsername": clmgmtDevCredServerUsername,
       "clmgmtDevCredServerPassword": clmgmtDevCredServerPassword,
       "clmgmtDevCredExportFile": clmgmtDevCredExportFile,
       "clmgmtDevCredCommand": clmgmtDevCredCommand,
       "clmgmtDevCredCommandState": clmgmtDevCredCommandState,
       "clmgmtDevCredCommandFailCause": clmgmtDevCredCommandFailCause,
       "clmgmtDevCredStorageType": clmgmtDevCredStorageType,
       "clmgmtDevCredRowStatus": clmgmtDevCredRowStatus,
       "clmgmtLicenseNotifObjects": clmgmtLicenseNotifObjects,
       "clmgmtLicenseUsageNotifEnable": clmgmtLicenseUsageNotifEnable,
       "clmgmtLicenseDeploymentNotifEnable": clmgmtLicenseDeploymentNotifEnable,
       "clmgmtLicenseErrorNotifEnable": clmgmtLicenseErrorNotifEnable,
       "ciscoLicenseMgmtMIBConform": ciscoLicenseMgmtMIBConform,
       "ciscoLicenseMgmtCompliances": ciscoLicenseMgmtCompliances,
       "ciscoLicenseMgmtCompliance": ciscoLicenseMgmtCompliance,
       "ciscoLicenseMgmtComplianceRev1": ciscoLicenseMgmtComplianceRev1,
       "ciscoLicenseMgmtGroups": ciscoLicenseMgmtGroups,
       "clmgmtLicenseDeploymentGroup": clmgmtLicenseDeploymentGroup,
       "clmgmtLicenseStoreInformationGroup": clmgmtLicenseStoreInformationGroup,
       "clmgmtLicenseDeviceInformationGroup": clmgmtLicenseDeviceInformationGroup,
       "clmgmtLicenseInformationGroup": clmgmtLicenseInformationGroup,
       "clmgmtLicensableFeatureInformationGroup": clmgmtLicensableFeatureInformationGroup,
       "clmgmtLicenseDevCredGroup": clmgmtLicenseDevCredGroup,
       "clmgmtLicenseNotificationEnableGroup": clmgmtLicenseNotificationEnableGroup,
       "clmgmtLicenseUsageNotifGroup": clmgmtLicenseUsageNotifGroup,
       "clmgmtLicenseDeploymentNotifGroup": clmgmtLicenseDeploymentNotifGroup,
       "clmgmtLicenseErrorNotifGroup": clmgmtLicenseErrorNotifGroup,
       "clmgmtLicenseSubscriptionGroup": clmgmtLicenseSubscriptionGroup,
       "clmgmtLicenseSubscriptionUsageNotifGroup": clmgmtLicenseSubscriptionUsageNotifGroup,
       "clmgmtLicenseRTUGroup": clmgmtLicenseRTUGroup,
       "clmgmtLicenseRTUUsageNotifGroup": clmgmtLicenseRTUUsageNotifGroup}
)
