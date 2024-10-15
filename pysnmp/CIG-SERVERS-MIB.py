# SNMP MIB module (CIG-SERVERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIG-SERVERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:14 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

cigServers = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Avaya_ObjectIdentity = ObjectIdentity
avaya = _Avaya_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2)
)
_Lsg_ObjectIdentity = ObjectIdentity
lsg = _Lsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1)
)
_CigTftpServers_ObjectIdentity = ObjectIdentity
cigTftpServers = _CigTftpServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1)
)
_CigTftpServersNotification_ObjectIdentity = ObjectIdentity
cigTftpServersNotification = _CigTftpServersNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 0)
)
_CigTftpServersGenConfig_ObjectIdentity = ObjectIdentity
cigTftpServersGenConfig = _CigTftpServersGenConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 1)
)


class _CigTftpServersMode_Type(TruthValue):
    """Custom type cigTftpServersMode based on TruthValue"""


_CigTftpServersMode_Object = MibScalar
cigTftpServersMode = _CigTftpServersMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 1, 1),
    _CigTftpServersMode_Type()
)
cigTftpServersMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigTftpServersMode.setStatus("current")


class _CigTftpServersResetStatCounters_Type(Integer32):
    """Custom type cigTftpServersResetStatCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_CigTftpServersResetStatCounters_Type.__name__ = "Integer32"
_CigTftpServersResetStatCounters_Object = MibScalar
cigTftpServersResetStatCounters = _CigTftpServersResetStatCounters_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 1, 2),
    _CigTftpServersResetStatCounters_Type()
)
cigTftpServersResetStatCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigTftpServersResetStatCounters.setStatus("current")
_CigTftpServersMemoryAllocation_ObjectIdentity = ObjectIdentity
cigTftpServersMemoryAllocation = _CigTftpServersMemoryAllocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 2)
)


class _CigTftpServersTotalBytesUsedInNvram_Type(Unsigned32):
    """Custom type cigTftpServersTotalBytesUsedInNvram based on Unsigned32"""
    defaultValue = 0


_CigTftpServersTotalBytesUsedInNvram_Object = MibScalar
cigTftpServersTotalBytesUsedInNvram = _CigTftpServersTotalBytesUsedInNvram_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 2, 1),
    _CigTftpServersTotalBytesUsedInNvram_Type()
)
cigTftpServersTotalBytesUsedInNvram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersTotalBytesUsedInNvram.setStatus("current")


class _CigTftpServersTotalBytesCapacityInNvram_Type(Unsigned32):
    """Custom type cigTftpServersTotalBytesCapacityInNvram based on Unsigned32"""
    defaultValue = 131072


_CigTftpServersTotalBytesCapacityInNvram_Object = MibScalar
cigTftpServersTotalBytesCapacityInNvram = _CigTftpServersTotalBytesCapacityInNvram_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 2, 2),
    _CigTftpServersTotalBytesCapacityInNvram_Type()
)
cigTftpServersTotalBytesCapacityInNvram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersTotalBytesCapacityInNvram.setStatus("current")


class _CigTftpServersTotalBytesUsedInRam_Type(Unsigned32):
    """Custom type cigTftpServersTotalBytesUsedInRam based on Unsigned32"""
    defaultValue = 0


_CigTftpServersTotalBytesUsedInRam_Object = MibScalar
cigTftpServersTotalBytesUsedInRam = _CigTftpServersTotalBytesUsedInRam_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 2, 3),
    _CigTftpServersTotalBytesUsedInRam_Type()
)
cigTftpServersTotalBytesUsedInRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersTotalBytesUsedInRam.setStatus("current")


class _CigTftpServersTotalBytesCapacityInRam_Type(Unsigned32):
    """Custom type cigTftpServersTotalBytesCapacityInRam based on Unsigned32"""
    defaultValue = 20971520


_CigTftpServersTotalBytesCapacityInRam_Object = MibScalar
cigTftpServersTotalBytesCapacityInRam = _CigTftpServersTotalBytesCapacityInRam_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 2, 4),
    _CigTftpServersTotalBytesCapacityInRam_Type()
)
cigTftpServersTotalBytesCapacityInRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersTotalBytesCapacityInRam.setStatus("current")
_CigTftpServersGenStats_ObjectIdentity = ObjectIdentity
cigTftpServersGenStats = _CigTftpServersGenStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3)
)


class _CigTftpServersSuccessfulDownloads_Type(Unsigned32):
    """Custom type cigTftpServersSuccessfulDownloads based on Unsigned32"""
    defaultValue = 0


_CigTftpServersSuccessfulDownloads_Object = MibScalar
cigTftpServersSuccessfulDownloads = _CigTftpServersSuccessfulDownloads_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 1),
    _CigTftpServersSuccessfulDownloads_Type()
)
cigTftpServersSuccessfulDownloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersSuccessfulDownloads.setStatus("current")


class _CigTftpServersNotDefinedErrors_Type(Unsigned32):
    """Custom type cigTftpServersNotDefinedErrors based on Unsigned32"""
    defaultValue = 0


_CigTftpServersNotDefinedErrors_Object = MibScalar
cigTftpServersNotDefinedErrors = _CigTftpServersNotDefinedErrors_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 2),
    _CigTftpServersNotDefinedErrors_Type()
)
cigTftpServersNotDefinedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersNotDefinedErrors.setStatus("current")


class _CigTftpServersFileNotFoundErrors_Type(Unsigned32):
    """Custom type cigTftpServersFileNotFoundErrors based on Unsigned32"""
    defaultValue = 0


_CigTftpServersFileNotFoundErrors_Object = MibScalar
cigTftpServersFileNotFoundErrors = _CigTftpServersFileNotFoundErrors_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 3),
    _CigTftpServersFileNotFoundErrors_Type()
)
cigTftpServersFileNotFoundErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersFileNotFoundErrors.setStatus("current")


class _CigTftpServersAccessViolationErrors_Type(Unsigned32):
    """Custom type cigTftpServersAccessViolationErrors based on Unsigned32"""
    defaultValue = 0


_CigTftpServersAccessViolationErrors_Object = MibScalar
cigTftpServersAccessViolationErrors = _CigTftpServersAccessViolationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 4),
    _CigTftpServersAccessViolationErrors_Type()
)
cigTftpServersAccessViolationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersAccessViolationErrors.setStatus("current")


class _CigTftpServersDiskFullErrors_Type(Unsigned32):
    """Custom type cigTftpServersDiskFullErrors based on Unsigned32"""
    defaultValue = 0


_CigTftpServersDiskFullErrors_Object = MibScalar
cigTftpServersDiskFullErrors = _CigTftpServersDiskFullErrors_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 5),
    _CigTftpServersDiskFullErrors_Type()
)
cigTftpServersDiskFullErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersDiskFullErrors.setStatus("current")


class _CigTftpServersIllegalTFTPOperationErrors_Type(Unsigned32):
    """Custom type cigTftpServersIllegalTFTPOperationErrors based on Unsigned32"""
    defaultValue = 0


_CigTftpServersIllegalTFTPOperationErrors_Object = MibScalar
cigTftpServersIllegalTFTPOperationErrors = _CigTftpServersIllegalTFTPOperationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 6),
    _CigTftpServersIllegalTFTPOperationErrors_Type()
)
cigTftpServersIllegalTFTPOperationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersIllegalTFTPOperationErrors.setStatus("current")


class _CigTftpServersUnknownTransferIdErrors_Type(Unsigned32):
    """Custom type cigTftpServersUnknownTransferIdErrors based on Unsigned32"""
    defaultValue = 0


_CigTftpServersUnknownTransferIdErrors_Object = MibScalar
cigTftpServersUnknownTransferIdErrors = _CigTftpServersUnknownTransferIdErrors_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 7),
    _CigTftpServersUnknownTransferIdErrors_Type()
)
cigTftpServersUnknownTransferIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersUnknownTransferIdErrors.setStatus("current")


class _CigTftpServersFileAlreadyExistsErrors_Type(Unsigned32):
    """Custom type cigTftpServersFileAlreadyExistsErrors based on Unsigned32"""
    defaultValue = 0


_CigTftpServersFileAlreadyExistsErrors_Object = MibScalar
cigTftpServersFileAlreadyExistsErrors = _CigTftpServersFileAlreadyExistsErrors_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 8),
    _CigTftpServersFileAlreadyExistsErrors_Type()
)
cigTftpServersFileAlreadyExistsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersFileAlreadyExistsErrors.setStatus("current")


class _CigTftpServersNoSuchUserErrors_Type(Unsigned32):
    """Custom type cigTftpServersNoSuchUserErrors based on Unsigned32"""
    defaultValue = 0


_CigTftpServersNoSuchUserErrors_Object = MibScalar
cigTftpServersNoSuchUserErrors = _CigTftpServersNoSuchUserErrors_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 9),
    _CigTftpServersNoSuchUserErrors_Type()
)
cigTftpServersNoSuchUserErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersNoSuchUserErrors.setStatus("current")


class _CigTftpServersDownloadTimeouts_Type(Unsigned32):
    """Custom type cigTftpServersDownloadTimeouts based on Unsigned32"""
    defaultValue = 0


_CigTftpServersDownloadTimeouts_Object = MibScalar
cigTftpServersDownloadTimeouts = _CigTftpServersDownloadTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 10),
    _CigTftpServersDownloadTimeouts_Type()
)
cigTftpServersDownloadTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigTftpServersDownloadTimeouts.setStatus("current")
_CigTftpServersNotificationPacket_ObjectIdentity = ObjectIdentity
cigTftpServersNotificationPacket = _CigTftpServersNotificationPacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 4)
)


class _CigTftpServersNotificationClientIpAddr_Type(IpAddress):
    """Custom type cigTftpServersNotificationClientIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_CigTftpServersNotificationClientIpAddr_Object = MibScalar
cigTftpServersNotificationClientIpAddr = _CigTftpServersNotificationClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 4, 1),
    _CigTftpServersNotificationClientIpAddr_Type()
)
cigTftpServersNotificationClientIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cigTftpServersNotificationClientIpAddr.setStatus("current")


class _CigTftpServersNotificationFilename_Type(DisplayString):
    """Custom type cigTftpServersNotificationFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CigTftpServersNotificationFilename_Type.__name__ = "DisplayString"
_CigTftpServersNotificationFilename_Object = MibScalar
cigTftpServersNotificationFilename = _CigTftpServersNotificationFilename_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 4, 2),
    _CigTftpServersNotificationFilename_Type()
)
cigTftpServersNotificationFilename.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cigTftpServersNotificationFilename.setStatus("current")


class _CigTftpServersNotificationErrorString_Type(DisplayString):
    """Custom type cigTftpServersNotificationErrorString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CigTftpServersNotificationErrorString_Type.__name__ = "DisplayString"
_CigTftpServersNotificationErrorString_Object = MibScalar
cigTftpServersNotificationErrorString = _CigTftpServersNotificationErrorString_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 4, 3),
    _CigTftpServersNotificationErrorString_Type()
)
cigTftpServersNotificationErrorString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cigTftpServersNotificationErrorString.setStatus("current")
_CigDhcpServers_ObjectIdentity = ObjectIdentity
cigDhcpServers = _CigDhcpServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2)
)
_CigDhcpServersNotification_ObjectIdentity = ObjectIdentity
cigDhcpServersNotification = _CigDhcpServersNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 0)
)
_CigDhcpServersGenConfig_ObjectIdentity = ObjectIdentity
cigDhcpServersGenConfig = _CigDhcpServersGenConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 1)
)


class _CigDhcpServersMode_Type(TruthValue):
    """Custom type cigDhcpServersMode based on TruthValue"""


_CigDhcpServersMode_Object = MibScalar
cigDhcpServersMode = _CigDhcpServersMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 1, 1),
    _CigDhcpServersMode_Type()
)
cigDhcpServersMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersMode.setStatus("current")


class _CigDhcpServersResetStatCounters_Type(Integer32):
    """Custom type cigDhcpServersResetStatCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_CigDhcpServersResetStatCounters_Type.__name__ = "Integer32"
_CigDhcpServersResetStatCounters_Object = MibScalar
cigDhcpServersResetStatCounters = _CigDhcpServersResetStatCounters_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 1, 2),
    _CigDhcpServersResetStatCounters_Type()
)
cigDhcpServersResetStatCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersResetStatCounters.setStatus("current")


class _CigDhcpServersPingDetectionMode_Type(TruthValue):
    """Custom type cigDhcpServersPingDetectionMode based on TruthValue"""


_CigDhcpServersPingDetectionMode_Object = MibScalar
cigDhcpServersPingDetectionMode = _CigDhcpServersPingDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 1, 3),
    _CigDhcpServersPingDetectionMode_Type()
)
cigDhcpServersPingDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPingDetectionMode.setStatus("current")


class _CigDhcpServersPingDetectionTimeout_Type(Unsigned32):
    """Custom type cigDhcpServersPingDetectionTimeout based on Unsigned32"""
    defaultValue = 500


_CigDhcpServersPingDetectionTimeout_Object = MibScalar
cigDhcpServersPingDetectionTimeout = _CigDhcpServersPingDetectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 1, 4),
    _CigDhcpServersPingDetectionTimeout_Type()
)
cigDhcpServersPingDetectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPingDetectionTimeout.setStatus("current")
_CigDhcpServersPool_ObjectIdentity = ObjectIdentity
cigDhcpServersPool = _CigDhcpServersPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2)
)
_CigDhcpServersPoolTable_Object = MibTable
cigDhcpServersPoolTable = _CigDhcpServersPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cigDhcpServersPoolTable.setStatus("current")
_CigDhcpServersPoolEntry_Object = MibTableRow
cigDhcpServersPoolEntry = _CigDhcpServersPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1)
)
cigDhcpServersPoolEntry.setIndexNames(
    (0, "CIG-SERVERS-MIB", "cigDhcpServersPoolIndex"),
)
if mibBuilder.loadTexts:
    cigDhcpServersPoolEntry.setStatus("current")
_CigDhcpServersPoolIndex_Type = Integer32
_CigDhcpServersPoolIndex_Object = MibTableColumn
cigDhcpServersPoolIndex = _CigDhcpServersPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 1),
    _CigDhcpServersPoolIndex_Type()
)
cigDhcpServersPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersPoolIndex.setStatus("current")


class _CigDhcpServersPoolStartIPAddr_Type(IpAddress):
    """Custom type cigDhcpServersPoolStartIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_CigDhcpServersPoolStartIPAddr_Object = MibTableColumn
cigDhcpServersPoolStartIPAddr = _CigDhcpServersPoolStartIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 2),
    _CigDhcpServersPoolStartIPAddr_Type()
)
cigDhcpServersPoolStartIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolStartIPAddr.setStatus("current")


class _CigDhcpServersPoolEndIPAddr_Type(IpAddress):
    """Custom type cigDhcpServersPoolEndIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_CigDhcpServersPoolEndIPAddr_Object = MibTableColumn
cigDhcpServersPoolEndIPAddr = _CigDhcpServersPoolEndIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 3),
    _CigDhcpServersPoolEndIPAddr_Type()
)
cigDhcpServersPoolEndIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolEndIPAddr.setStatus("current")


class _CigDhcpServersPoolMode_Type(TruthValue):
    """Custom type cigDhcpServersPoolMode based on TruthValue"""


_CigDhcpServersPoolMode_Object = MibTableColumn
cigDhcpServersPoolMode = _CigDhcpServersPoolMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 4),
    _CigDhcpServersPoolMode_Type()
)
cigDhcpServersPoolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolMode.setStatus("current")


class _CigDhcpServersPoolName_Type(DisplayString):
    """Custom type cigDhcpServersPoolName based on DisplayString"""
    defaultValue = OctetString("Dhcp Pool #")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CigDhcpServersPoolName_Type.__name__ = "DisplayString"
_CigDhcpServersPoolName_Object = MibTableColumn
cigDhcpServersPoolName = _CigDhcpServersPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 5),
    _CigDhcpServersPoolName_Type()
)
cigDhcpServersPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolName.setStatus("current")


class _CigDhcpServersPoolClientID_Type(OctetString):
    """Custom type cigDhcpServersPoolClientID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CigDhcpServersPoolClientID_Type.__name__ = "OctetString"
_CigDhcpServersPoolClientID_Object = MibTableColumn
cigDhcpServersPoolClientID = _CigDhcpServersPoolClientID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 6),
    _CigDhcpServersPoolClientID_Type()
)
cigDhcpServersPoolClientID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolClientID.setStatus("current")


class _CigDhcpServersPoolLeaseTime_Type(Unsigned32):
    """Custom type cigDhcpServersPoolLeaseTime based on Unsigned32"""
    defaultValue = 691200


_CigDhcpServersPoolLeaseTime_Object = MibTableColumn
cigDhcpServersPoolLeaseTime = _CigDhcpServersPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 7),
    _CigDhcpServersPoolLeaseTime_Type()
)
cigDhcpServersPoolLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolLeaseTime.setStatus("current")


class _CigDhcpServersPoolBootFile_Type(DisplayString):
    """Custom type cigDhcpServersPoolBootFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CigDhcpServersPoolBootFile_Type.__name__ = "DisplayString"
_CigDhcpServersPoolBootFile_Object = MibTableColumn
cigDhcpServersPoolBootFile = _CigDhcpServersPoolBootFile_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 8),
    _CigDhcpServersPoolBootFile_Type()
)
cigDhcpServersPoolBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolBootFile.setStatus("current")


class _CigDhcpServersPoolNextServer_Type(IpAddress):
    """Custom type cigDhcpServersPoolNextServer based on IpAddress"""
    defaultHexValue = "00000000"


_CigDhcpServersPoolNextServer_Object = MibTableColumn
cigDhcpServersPoolNextServer = _CigDhcpServersPoolNextServer_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 9),
    _CigDhcpServersPoolNextServer_Type()
)
cigDhcpServersPoolNextServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolNextServer.setStatus("current")


class _CigDhcpServersPoolSubnetMask_Type(IpAddress):
    """Custom type cigDhcpServersPoolSubnetMask based on IpAddress"""
    defaultHexValue = "ffffff00"


_CigDhcpServersPoolSubnetMask_Object = MibTableColumn
cigDhcpServersPoolSubnetMask = _CigDhcpServersPoolSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 10),
    _CigDhcpServersPoolSubnetMask_Type()
)
cigDhcpServersPoolSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolSubnetMask.setStatus("current")


class _CigDhcpServersPoolDefaultGateway_Type(DisplayString):
    """Custom type cigDhcpServersPoolDefaultGateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 145),
    )


_CigDhcpServersPoolDefaultGateway_Type.__name__ = "DisplayString"
_CigDhcpServersPoolDefaultGateway_Object = MibTableColumn
cigDhcpServersPoolDefaultGateway = _CigDhcpServersPoolDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 11),
    _CigDhcpServersPoolDefaultGateway_Type()
)
cigDhcpServersPoolDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolDefaultGateway.setStatus("current")


class _CigDhcpServersPoolDnsServer_Type(DisplayString):
    """Custom type cigDhcpServersPoolDnsServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 145),
    )


_CigDhcpServersPoolDnsServer_Type.__name__ = "DisplayString"
_CigDhcpServersPoolDnsServer_Object = MibTableColumn
cigDhcpServersPoolDnsServer = _CigDhcpServersPoolDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 12),
    _CigDhcpServersPoolDnsServer_Type()
)
cigDhcpServersPoolDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolDnsServer.setStatus("current")


class _CigDhcpServersPoolDomainName_Type(DisplayString):
    """Custom type cigDhcpServersPoolDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CigDhcpServersPoolDomainName_Type.__name__ = "DisplayString"
_CigDhcpServersPoolDomainName_Object = MibTableColumn
cigDhcpServersPoolDomainName = _CigDhcpServersPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 13),
    _CigDhcpServersPoolDomainName_Type()
)
cigDhcpServersPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolDomainName.setStatus("current")


class _CigDhcpServersPoolServerName_Type(DisplayString):
    """Custom type cigDhcpServersPoolServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CigDhcpServersPoolServerName_Type.__name__ = "DisplayString"
_CigDhcpServersPoolServerName_Object = MibTableColumn
cigDhcpServersPoolServerName = _CigDhcpServersPoolServerName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 14),
    _CigDhcpServersPoolServerName_Type()
)
cigDhcpServersPoolServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolServerName.setStatus("current")
_CigDhcpServersPoolRowStatus_Type = RowStatus
_CigDhcpServersPoolRowStatus_Object = MibTableColumn
cigDhcpServersPoolRowStatus = _CigDhcpServersPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 15),
    _CigDhcpServersPoolRowStatus_Type()
)
cigDhcpServersPoolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersPoolRowStatus.setStatus("current")
_CigDhcpServersPoolGenOptionTable_Object = MibTable
cigDhcpServersPoolGenOptionTable = _CigDhcpServersPoolGenOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cigDhcpServersPoolGenOptionTable.setStatus("current")
_CigDhcpServersPoolGenOptionEntry_Object = MibTableRow
cigDhcpServersPoolGenOptionEntry = _CigDhcpServersPoolGenOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1)
)
cigDhcpServersPoolGenOptionEntry.setIndexNames(
    (0, "CIG-SERVERS-MIB", "cigDhcpServersOptionPoolIndex"),
    (0, "CIG-SERVERS-MIB", "cigDhcpServersOptionIndex"),
)
if mibBuilder.loadTexts:
    cigDhcpServersPoolGenOptionEntry.setStatus("current")
_CigDhcpServersOptionPoolIndex_Type = Integer32
_CigDhcpServersOptionPoolIndex_Object = MibTableColumn
cigDhcpServersOptionPoolIndex = _CigDhcpServersOptionPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 1),
    _CigDhcpServersOptionPoolIndex_Type()
)
cigDhcpServersOptionPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersOptionPoolIndex.setStatus("current")
_CigDhcpServersOptionIndex_Type = Integer32
_CigDhcpServersOptionIndex_Object = MibTableColumn
cigDhcpServersOptionIndex = _CigDhcpServersOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 2),
    _CigDhcpServersOptionIndex_Type()
)
cigDhcpServersOptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersOptionIndex.setStatus("current")


class _CigDhcpServersOptionName_Type(DisplayString):
    """Custom type cigDhcpServersOptionName based on DisplayString"""
    defaultValue = OctetString("Option #")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CigDhcpServersOptionName_Type.__name__ = "DisplayString"
_CigDhcpServersOptionName_Object = MibTableColumn
cigDhcpServersOptionName = _CigDhcpServersOptionName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 3),
    _CigDhcpServersOptionName_Type()
)
cigDhcpServersOptionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersOptionName.setStatus("current")


class _CigDhcpServersOptionType_Type(Integer32):
    """Custom type cigDhcpServersOptionType based on Integer32"""
    defaultValue = 2

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
        *(("ascii", 1),
          ("hex", 2),
          ("integer", 4),
          ("ipAddresses", 3),
          ("word", 5))
    )


_CigDhcpServersOptionType_Type.__name__ = "Integer32"
_CigDhcpServersOptionType_Object = MibTableColumn
cigDhcpServersOptionType = _CigDhcpServersOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 4),
    _CigDhcpServersOptionType_Type()
)
cigDhcpServersOptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersOptionType.setStatus("current")


class _CigDhcpServersOptionValue_Type(OctetString):
    """Custom type cigDhcpServersOptionValue based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CigDhcpServersOptionValue_Type.__name__ = "OctetString"
_CigDhcpServersOptionValue_Object = MibTableColumn
cigDhcpServersOptionValue = _CigDhcpServersOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 5),
    _CigDhcpServersOptionValue_Type()
)
cigDhcpServersOptionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersOptionValue.setStatus("current")
_CigDhcpServersOptionRowStatus_Type = RowStatus
_CigDhcpServersOptionRowStatus_Object = MibTableColumn
cigDhcpServersOptionRowStatus = _CigDhcpServersOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 6),
    _CigDhcpServersOptionRowStatus_Type()
)
cigDhcpServersOptionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersOptionRowStatus.setStatus("current")
_CigDhcpServersPoolVendorSpecificOptionTable_Object = MibTable
cigDhcpServersPoolVendorSpecificOptionTable = _CigDhcpServersPoolVendorSpecificOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cigDhcpServersPoolVendorSpecificOptionTable.setStatus("current")
_CigDhcpServersPoolVendorSpecificOptionEntry_Object = MibTableRow
cigDhcpServersPoolVendorSpecificOptionEntry = _CigDhcpServersPoolVendorSpecificOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1)
)
cigDhcpServersPoolVendorSpecificOptionEntry.setIndexNames(
    (0, "CIG-SERVERS-MIB", "cigDhcpServersVendorSpecificOptionPoolIndex"),
    (0, "CIG-SERVERS-MIB", "cigDhcpServersVendorSpecificOptionIndex"),
)
if mibBuilder.loadTexts:
    cigDhcpServersPoolVendorSpecificOptionEntry.setStatus("current")
_CigDhcpServersVendorSpecificOptionPoolIndex_Type = Integer32
_CigDhcpServersVendorSpecificOptionPoolIndex_Object = MibTableColumn
cigDhcpServersVendorSpecificOptionPoolIndex = _CigDhcpServersVendorSpecificOptionPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 1),
    _CigDhcpServersVendorSpecificOptionPoolIndex_Type()
)
cigDhcpServersVendorSpecificOptionPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersVendorSpecificOptionPoolIndex.setStatus("current")
_CigDhcpServersVendorSpecificOptionIndex_Type = Integer32
_CigDhcpServersVendorSpecificOptionIndex_Object = MibTableColumn
cigDhcpServersVendorSpecificOptionIndex = _CigDhcpServersVendorSpecificOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 2),
    _CigDhcpServersVendorSpecificOptionIndex_Type()
)
cigDhcpServersVendorSpecificOptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersVendorSpecificOptionIndex.setStatus("current")


class _CigDhcpServersVendorSpecificOptionName_Type(DisplayString):
    """Custom type cigDhcpServersVendorSpecificOptionName based on DisplayString"""
    defaultValue = OctetString("Vendor Specific Option #")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CigDhcpServersVendorSpecificOptionName_Type.__name__ = "DisplayString"
_CigDhcpServersVendorSpecificOptionName_Object = MibTableColumn
cigDhcpServersVendorSpecificOptionName = _CigDhcpServersVendorSpecificOptionName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 3),
    _CigDhcpServersVendorSpecificOptionName_Type()
)
cigDhcpServersVendorSpecificOptionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersVendorSpecificOptionName.setStatus("current")


class _CigDhcpServersVendorSpecificClassIdentifier_Type(DisplayString):
    """Custom type cigDhcpServersVendorSpecificClassIdentifier based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CigDhcpServersVendorSpecificClassIdentifier_Type.__name__ = "DisplayString"
_CigDhcpServersVendorSpecificClassIdentifier_Object = MibTableColumn
cigDhcpServersVendorSpecificClassIdentifier = _CigDhcpServersVendorSpecificClassIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 4),
    _CigDhcpServersVendorSpecificClassIdentifier_Type()
)
cigDhcpServersVendorSpecificClassIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersVendorSpecificClassIdentifier.setStatus("current")


class _CigDhcpServersVendorSpecificOptionType_Type(Integer32):
    """Custom type cigDhcpServersVendorSpecificOptionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2))
    )


_CigDhcpServersVendorSpecificOptionType_Type.__name__ = "Integer32"
_CigDhcpServersVendorSpecificOptionType_Object = MibTableColumn
cigDhcpServersVendorSpecificOptionType = _CigDhcpServersVendorSpecificOptionType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 5),
    _CigDhcpServersVendorSpecificOptionType_Type()
)
cigDhcpServersVendorSpecificOptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersVendorSpecificOptionType.setStatus("current")


class _CigDhcpServersVendorSpecificOptionValue_Type(OctetString):
    """Custom type cigDhcpServersVendorSpecificOptionValue based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CigDhcpServersVendorSpecificOptionValue_Type.__name__ = "OctetString"
_CigDhcpServersVendorSpecificOptionValue_Object = MibTableColumn
cigDhcpServersVendorSpecificOptionValue = _CigDhcpServersVendorSpecificOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 6),
    _CigDhcpServersVendorSpecificOptionValue_Type()
)
cigDhcpServersVendorSpecificOptionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersVendorSpecificOptionValue.setStatus("current")
_CigDhcpServersVendorSpecificOptionRowStatus_Type = RowStatus
_CigDhcpServersVendorSpecificOptionRowStatus_Object = MibTableColumn
cigDhcpServersVendorSpecificOptionRowStatus = _CigDhcpServersVendorSpecificOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 7),
    _CigDhcpServersVendorSpecificOptionRowStatus_Type()
)
cigDhcpServersVendorSpecificOptionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpServersVendorSpecificOptionRowStatus.setStatus("current")
_CigDhcpServersGenStats_ObjectIdentity = ObjectIdentity
cigDhcpServersGenStats = _CigDhcpServersGenStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3)
)


class _CigDhcpServersBootRequests_Type(Unsigned32):
    """Custom type cigDhcpServersBootRequests based on Unsigned32"""
    defaultValue = 0


_CigDhcpServersBootRequests_Object = MibScalar
cigDhcpServersBootRequests = _CigDhcpServersBootRequests_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 1),
    _CigDhcpServersBootRequests_Type()
)
cigDhcpServersBootRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersBootRequests.setStatus("current")


class _CigDhcpServersDhcpDiscovers_Type(Unsigned32):
    """Custom type cigDhcpServersDhcpDiscovers based on Unsigned32"""
    defaultValue = 0


_CigDhcpServersDhcpDiscovers_Object = MibScalar
cigDhcpServersDhcpDiscovers = _CigDhcpServersDhcpDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 2),
    _CigDhcpServersDhcpDiscovers_Type()
)
cigDhcpServersDhcpDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersDhcpDiscovers.setStatus("current")


class _CigDhcpServersDhcpRequests_Type(Unsigned32):
    """Custom type cigDhcpServersDhcpRequests based on Unsigned32"""
    defaultValue = 0


_CigDhcpServersDhcpRequests_Object = MibScalar
cigDhcpServersDhcpRequests = _CigDhcpServersDhcpRequests_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 3),
    _CigDhcpServersDhcpRequests_Type()
)
cigDhcpServersDhcpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersDhcpRequests.setStatus("current")


class _CigDhcpServersDhcpDeclines_Type(Unsigned32):
    """Custom type cigDhcpServersDhcpDeclines based on Unsigned32"""
    defaultValue = 0


_CigDhcpServersDhcpDeclines_Object = MibScalar
cigDhcpServersDhcpDeclines = _CigDhcpServersDhcpDeclines_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 4),
    _CigDhcpServersDhcpDeclines_Type()
)
cigDhcpServersDhcpDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersDhcpDeclines.setStatus("current")


class _CigDhcpServersDhcpReleases_Type(Unsigned32):
    """Custom type cigDhcpServersDhcpReleases based on Unsigned32"""
    defaultValue = 0


_CigDhcpServersDhcpReleases_Object = MibScalar
cigDhcpServersDhcpReleases = _CigDhcpServersDhcpReleases_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 5),
    _CigDhcpServersDhcpReleases_Type()
)
cigDhcpServersDhcpReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersDhcpReleases.setStatus("current")


class _CigDhcpServersDhcpInforms_Type(Unsigned32):
    """Custom type cigDhcpServersDhcpInforms based on Unsigned32"""
    defaultValue = 0


_CigDhcpServersDhcpInforms_Object = MibScalar
cigDhcpServersDhcpInforms = _CigDhcpServersDhcpInforms_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 6),
    _CigDhcpServersDhcpInforms_Type()
)
cigDhcpServersDhcpInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersDhcpInforms.setStatus("current")


class _CigDhcpServersBootReplies_Type(Unsigned32):
    """Custom type cigDhcpServersBootReplies based on Unsigned32"""
    defaultValue = 0


_CigDhcpServersBootReplies_Object = MibScalar
cigDhcpServersBootReplies = _CigDhcpServersBootReplies_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 7),
    _CigDhcpServersBootReplies_Type()
)
cigDhcpServersBootReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersBootReplies.setStatus("current")


class _CigDhcpServersDhcpOffers_Type(Unsigned32):
    """Custom type cigDhcpServersDhcpOffers based on Unsigned32"""
    defaultValue = 0


_CigDhcpServersDhcpOffers_Object = MibScalar
cigDhcpServersDhcpOffers = _CigDhcpServersDhcpOffers_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 8),
    _CigDhcpServersDhcpOffers_Type()
)
cigDhcpServersDhcpOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersDhcpOffers.setStatus("current")


class _CigDhcpServersDhcpAcks_Type(Unsigned32):
    """Custom type cigDhcpServersDhcpAcks based on Unsigned32"""
    defaultValue = 0


_CigDhcpServersDhcpAcks_Object = MibScalar
cigDhcpServersDhcpAcks = _CigDhcpServersDhcpAcks_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 9),
    _CigDhcpServersDhcpAcks_Type()
)
cigDhcpServersDhcpAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersDhcpAcks.setStatus("current")


class _CigDhcpServersDhcpNacks_Type(Unsigned32):
    """Custom type cigDhcpServersDhcpNacks based on Unsigned32"""
    defaultValue = 0


_CigDhcpServersDhcpNacks_Object = MibScalar
cigDhcpServersDhcpNacks = _CigDhcpServersDhcpNacks_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 10),
    _CigDhcpServersDhcpNacks_Type()
)
cigDhcpServersDhcpNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpServersDhcpNacks.setStatus("current")
_CigDhcpServersNotificationPacket_ObjectIdentity = ObjectIdentity
cigDhcpServersNotificationPacket = _CigDhcpServersNotificationPacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4)
)


class _CigDhcpServersNotificationIpAddr_Type(IpAddress):
    """Custom type cigDhcpServersNotificationIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_CigDhcpServersNotificationIpAddr_Object = MibScalar
cigDhcpServersNotificationIpAddr = _CigDhcpServersNotificationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4, 1),
    _CigDhcpServersNotificationIpAddr_Type()
)
cigDhcpServersNotificationIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cigDhcpServersNotificationIpAddr.setStatus("current")


class _CigDhcpServersNotificationClientIdentifier_Type(OctetString):
    """Custom type cigDhcpServersNotificationClientIdentifier based on OctetString"""
    defaultHexValue = "01000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CigDhcpServersNotificationClientIdentifier_Type.__name__ = "OctetString"
_CigDhcpServersNotificationClientIdentifier_Object = MibScalar
cigDhcpServersNotificationClientIdentifier = _CigDhcpServersNotificationClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4, 2),
    _CigDhcpServersNotificationClientIdentifier_Type()
)
cigDhcpServersNotificationClientIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cigDhcpServersNotificationClientIdentifier.setStatus("current")


class _CigDhcpServersNotificationClientHostName_Type(OctetString):
    """Custom type cigDhcpServersNotificationClientHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CigDhcpServersNotificationClientHostName_Type.__name__ = "OctetString"
_CigDhcpServersNotificationClientHostName_Object = MibScalar
cigDhcpServersNotificationClientHostName = _CigDhcpServersNotificationClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4, 3),
    _CigDhcpServersNotificationClientHostName_Type()
)
cigDhcpServersNotificationClientHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cigDhcpServersNotificationClientHostName.setStatus("current")


class _CigDhcpServersNotificationConflictDetectionMethod_Type(Integer32):
    """Custom type cigDhcpServersNotificationConflictDetectionMethod based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("gratuitousArp", 2),
          ("notSupported", 255),
          ("ping", 1))
    )


_CigDhcpServersNotificationConflictDetectionMethod_Type.__name__ = "Integer32"
_CigDhcpServersNotificationConflictDetectionMethod_Object = MibScalar
cigDhcpServersNotificationConflictDetectionMethod = _CigDhcpServersNotificationConflictDetectionMethod_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4, 4),
    _CigDhcpServersNotificationConflictDetectionMethod_Type()
)
cigDhcpServersNotificationConflictDetectionMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cigDhcpServersNotificationConflictDetectionMethod.setStatus("current")


class _CigDhcpServersNotificationPoolNetwork_Type(IpAddress):
    """Custom type cigDhcpServersNotificationPoolNetwork based on IpAddress"""
    defaultHexValue = "00000000"


_CigDhcpServersNotificationPoolNetwork_Object = MibScalar
cigDhcpServersNotificationPoolNetwork = _CigDhcpServersNotificationPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4, 5),
    _CigDhcpServersNotificationPoolNetwork_Type()
)
cigDhcpServersNotificationPoolNetwork.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cigDhcpServersNotificationPoolNetwork.setStatus("current")

# Managed Objects groups


# Notification objects

cigTftpServersDownloadFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 0, 1)
)
cigTftpServersDownloadFailureTrap.setObjects(
      *(("CIG-SERVERS-MIB", "cigTftpServersNotificationClientIpAddr"),
        ("CIG-SERVERS-MIB", "cigTftpServersNotificationFilename"),
        ("CIG-SERVERS-MIB", "cigTftpServersNotificationErrorString"))
)
if mibBuilder.loadTexts:
    cigTftpServersDownloadFailureTrap.setStatus(
        "current"
    )

cigTftpServersUploadFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 0, 2)
)
cigTftpServersUploadFailureTrap.setObjects(
      *(("CIG-SERVERS-MIB", "cigTftpServersNotificationClientIpAddr"),
        ("CIG-SERVERS-MIB", "cigTftpServersNotificationFilename"),
        ("CIG-SERVERS-MIB", "cigTftpServersNotificationErrorString"))
)
if mibBuilder.loadTexts:
    cigTftpServersUploadFailureTrap.setStatus(
        "current"
    )

cigDhcpServersClientConflictDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 0, 1)
)
cigDhcpServersClientConflictDetectionTrap.setObjects(
      *(("CIG-SERVERS-MIB", "cigDhcpServersNotificationIpAddr"),
        ("CIG-SERVERS-MIB", "cigDhcpServersNotificationClientHostName"),
        ("CIG-SERVERS-MIB", "cigDhcpServersNotificationClientIdentifier"),
        ("CIG-SERVERS-MIB", "cigDhcpServersNotificationConflictDetectionMethod"))
)
if mibBuilder.loadTexts:
    cigDhcpServersClientConflictDetectionTrap.setStatus(
        "current"
    )

cigDhcpServersServerNacksTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 0, 2)
)
cigDhcpServersServerNacksTrap.setObjects(
      *(("CIG-SERVERS-MIB", "cigDhcpServersNotificationIpAddr"),
        ("CIG-SERVERS-MIB", "cigDhcpServersNotificationClientIdentifier"))
)
if mibBuilder.loadTexts:
    cigDhcpServersServerNacksTrap.setStatus(
        "current"
    )

cigDhcpServersNoIpAddressLeft = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 0, 3)
)
cigDhcpServersNoIpAddressLeft.setObjects(
      *(("CIG-SERVERS-MIB", "cigDhcpServersNotificationClientIdentifier"),
        ("CIG-SERVERS-MIB", "cigDhcpServersNotificationPoolNetwork"))
)
if mibBuilder.loadTexts:
    cigDhcpServersNoIpAddressLeft.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIG-SERVERS-MIB",
    **{"avaya": avaya,
       "mibs": mibs,
       "lsg": lsg,
       "cigServers": cigServers,
       "cigTftpServers": cigTftpServers,
       "cigTftpServersNotification": cigTftpServersNotification,
       "cigTftpServersDownloadFailureTrap": cigTftpServersDownloadFailureTrap,
       "cigTftpServersUploadFailureTrap": cigTftpServersUploadFailureTrap,
       "cigTftpServersGenConfig": cigTftpServersGenConfig,
       "cigTftpServersMode": cigTftpServersMode,
       "cigTftpServersResetStatCounters": cigTftpServersResetStatCounters,
       "cigTftpServersMemoryAllocation": cigTftpServersMemoryAllocation,
       "cigTftpServersTotalBytesUsedInNvram": cigTftpServersTotalBytesUsedInNvram,
       "cigTftpServersTotalBytesCapacityInNvram": cigTftpServersTotalBytesCapacityInNvram,
       "cigTftpServersTotalBytesUsedInRam": cigTftpServersTotalBytesUsedInRam,
       "cigTftpServersTotalBytesCapacityInRam": cigTftpServersTotalBytesCapacityInRam,
       "cigTftpServersGenStats": cigTftpServersGenStats,
       "cigTftpServersSuccessfulDownloads": cigTftpServersSuccessfulDownloads,
       "cigTftpServersNotDefinedErrors": cigTftpServersNotDefinedErrors,
       "cigTftpServersFileNotFoundErrors": cigTftpServersFileNotFoundErrors,
       "cigTftpServersAccessViolationErrors": cigTftpServersAccessViolationErrors,
       "cigTftpServersDiskFullErrors": cigTftpServersDiskFullErrors,
       "cigTftpServersIllegalTFTPOperationErrors": cigTftpServersIllegalTFTPOperationErrors,
       "cigTftpServersUnknownTransferIdErrors": cigTftpServersUnknownTransferIdErrors,
       "cigTftpServersFileAlreadyExistsErrors": cigTftpServersFileAlreadyExistsErrors,
       "cigTftpServersNoSuchUserErrors": cigTftpServersNoSuchUserErrors,
       "cigTftpServersDownloadTimeouts": cigTftpServersDownloadTimeouts,
       "cigTftpServersNotificationPacket": cigTftpServersNotificationPacket,
       "cigTftpServersNotificationClientIpAddr": cigTftpServersNotificationClientIpAddr,
       "cigTftpServersNotificationFilename": cigTftpServersNotificationFilename,
       "cigTftpServersNotificationErrorString": cigTftpServersNotificationErrorString,
       "cigDhcpServers": cigDhcpServers,
       "cigDhcpServersNotification": cigDhcpServersNotification,
       "cigDhcpServersClientConflictDetectionTrap": cigDhcpServersClientConflictDetectionTrap,
       "cigDhcpServersServerNacksTrap": cigDhcpServersServerNacksTrap,
       "cigDhcpServersNoIpAddressLeft": cigDhcpServersNoIpAddressLeft,
       "cigDhcpServersGenConfig": cigDhcpServersGenConfig,
       "cigDhcpServersMode": cigDhcpServersMode,
       "cigDhcpServersResetStatCounters": cigDhcpServersResetStatCounters,
       "cigDhcpServersPingDetectionMode": cigDhcpServersPingDetectionMode,
       "cigDhcpServersPingDetectionTimeout": cigDhcpServersPingDetectionTimeout,
       "cigDhcpServersPool": cigDhcpServersPool,
       "cigDhcpServersPoolTable": cigDhcpServersPoolTable,
       "cigDhcpServersPoolEntry": cigDhcpServersPoolEntry,
       "cigDhcpServersPoolIndex": cigDhcpServersPoolIndex,
       "cigDhcpServersPoolStartIPAddr": cigDhcpServersPoolStartIPAddr,
       "cigDhcpServersPoolEndIPAddr": cigDhcpServersPoolEndIPAddr,
       "cigDhcpServersPoolMode": cigDhcpServersPoolMode,
       "cigDhcpServersPoolName": cigDhcpServersPoolName,
       "cigDhcpServersPoolClientID": cigDhcpServersPoolClientID,
       "cigDhcpServersPoolLeaseTime": cigDhcpServersPoolLeaseTime,
       "cigDhcpServersPoolBootFile": cigDhcpServersPoolBootFile,
       "cigDhcpServersPoolNextServer": cigDhcpServersPoolNextServer,
       "cigDhcpServersPoolSubnetMask": cigDhcpServersPoolSubnetMask,
       "cigDhcpServersPoolDefaultGateway": cigDhcpServersPoolDefaultGateway,
       "cigDhcpServersPoolDnsServer": cigDhcpServersPoolDnsServer,
       "cigDhcpServersPoolDomainName": cigDhcpServersPoolDomainName,
       "cigDhcpServersPoolServerName": cigDhcpServersPoolServerName,
       "cigDhcpServersPoolRowStatus": cigDhcpServersPoolRowStatus,
       "cigDhcpServersPoolGenOptionTable": cigDhcpServersPoolGenOptionTable,
       "cigDhcpServersPoolGenOptionEntry": cigDhcpServersPoolGenOptionEntry,
       "cigDhcpServersOptionPoolIndex": cigDhcpServersOptionPoolIndex,
       "cigDhcpServersOptionIndex": cigDhcpServersOptionIndex,
       "cigDhcpServersOptionName": cigDhcpServersOptionName,
       "cigDhcpServersOptionType": cigDhcpServersOptionType,
       "cigDhcpServersOptionValue": cigDhcpServersOptionValue,
       "cigDhcpServersOptionRowStatus": cigDhcpServersOptionRowStatus,
       "cigDhcpServersPoolVendorSpecificOptionTable": cigDhcpServersPoolVendorSpecificOptionTable,
       "cigDhcpServersPoolVendorSpecificOptionEntry": cigDhcpServersPoolVendorSpecificOptionEntry,
       "cigDhcpServersVendorSpecificOptionPoolIndex": cigDhcpServersVendorSpecificOptionPoolIndex,
       "cigDhcpServersVendorSpecificOptionIndex": cigDhcpServersVendorSpecificOptionIndex,
       "cigDhcpServersVendorSpecificOptionName": cigDhcpServersVendorSpecificOptionName,
       "cigDhcpServersVendorSpecificClassIdentifier": cigDhcpServersVendorSpecificClassIdentifier,
       "cigDhcpServersVendorSpecificOptionType": cigDhcpServersVendorSpecificOptionType,
       "cigDhcpServersVendorSpecificOptionValue": cigDhcpServersVendorSpecificOptionValue,
       "cigDhcpServersVendorSpecificOptionRowStatus": cigDhcpServersVendorSpecificOptionRowStatus,
       "cigDhcpServersGenStats": cigDhcpServersGenStats,
       "cigDhcpServersBootRequests": cigDhcpServersBootRequests,
       "cigDhcpServersDhcpDiscovers": cigDhcpServersDhcpDiscovers,
       "cigDhcpServersDhcpRequests": cigDhcpServersDhcpRequests,
       "cigDhcpServersDhcpDeclines": cigDhcpServersDhcpDeclines,
       "cigDhcpServersDhcpReleases": cigDhcpServersDhcpReleases,
       "cigDhcpServersDhcpInforms": cigDhcpServersDhcpInforms,
       "cigDhcpServersBootReplies": cigDhcpServersBootReplies,
       "cigDhcpServersDhcpOffers": cigDhcpServersDhcpOffers,
       "cigDhcpServersDhcpAcks": cigDhcpServersDhcpAcks,
       "cigDhcpServersDhcpNacks": cigDhcpServersDhcpNacks,
       "cigDhcpServersNotificationPacket": cigDhcpServersNotificationPacket,
       "cigDhcpServersNotificationIpAddr": cigDhcpServersNotificationIpAddr,
       "cigDhcpServersNotificationClientIdentifier": cigDhcpServersNotificationClientIdentifier,
       "cigDhcpServersNotificationClientHostName": cigDhcpServersNotificationClientHostName,
       "cigDhcpServersNotificationConflictDetectionMethod": cigDhcpServersNotificationConflictDetectionMethod,
       "cigDhcpServersNotificationPoolNetwork": cigDhcpServersNotificationPoolNetwork}
)
