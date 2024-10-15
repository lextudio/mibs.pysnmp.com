# SNMP MIB module (REDLINE-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDLINE-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:31 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(redlineSystem,) = mibBuilder.importSymbols(
    "REDLINE-MIB",
    "redlineSystem")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

redlineSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1)
)
redlineSystemMib.setRevisions(
        ("2005-03-31 15:43",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RedlineSystemSystemObjects_ObjectIdentity = ObjectIdentity
redlineSystemSystemObjects = _RedlineSystemSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1)
)


class _RedlineSystemSerialNumber_Type(DisplayString):
    """Custom type redlineSystemSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemSerialNumber_Type.__name__ = "DisplayString"
_RedlineSystemSerialNumber_Object = MibScalar
redlineSystemSerialNumber = _RedlineSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 1),
    _RedlineSystemSerialNumber_Type()
)
redlineSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemSerialNumber.setStatus("current")
_RedlineSystemSysControl_ObjectIdentity = ObjectIdentity
redlineSystemSysControl = _RedlineSystemSysControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 2)
)


class _RedlineSystemSystemReboot_Type(Integer32):
    """Custom type redlineSystemSystemReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reboot", 2))
    )


_RedlineSystemSystemReboot_Type.__name__ = "Integer32"
_RedlineSystemSystemReboot_Object = MibScalar
redlineSystemSystemReboot = _RedlineSystemSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 2, 1),
    _RedlineSystemSystemReboot_Type()
)
redlineSystemSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemSystemReboot.setStatus("current")
_RedlineSystemSysDhcpObjects_ObjectIdentity = ObjectIdentity
redlineSystemSysDhcpObjects = _RedlineSystemSysDhcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 3)
)
_RedlineSystemDHCPServerIpAddressType_Type = InetAddressType
_RedlineSystemDHCPServerIpAddressType_Object = MibScalar
redlineSystemDHCPServerIpAddressType = _RedlineSystemDHCPServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 3, 1),
    _RedlineSystemDHCPServerIpAddressType_Type()
)
redlineSystemDHCPServerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemDHCPServerIpAddressType.setStatus("current")
_RedlineSystemDHCPServerIpAddress_Type = InetAddress
_RedlineSystemDHCPServerIpAddress_Object = MibScalar
redlineSystemDHCPServerIpAddress = _RedlineSystemDHCPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 3, 2),
    _RedlineSystemDHCPServerIpAddress_Type()
)
redlineSystemDHCPServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemDHCPServerIpAddress.setStatus("current")
_RedlineSystemSysIpObjects_ObjectIdentity = ObjectIdentity
redlineSystemSysIpObjects = _RedlineSystemSysIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 4)
)
_RedlineSystemIpAddressType_Type = InetAddressType
_RedlineSystemIpAddressType_Object = MibScalar
redlineSystemIpAddressType = _RedlineSystemIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 4, 1),
    _RedlineSystemIpAddressType_Type()
)
redlineSystemIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemIpAddressType.setStatus("current")
_RedlineSystemIpAddress_Type = InetAddress
_RedlineSystemIpAddress_Object = MibScalar
redlineSystemIpAddress = _RedlineSystemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 4, 2),
    _RedlineSystemIpAddress_Type()
)
redlineSystemIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemIpAddress.setStatus("current")
_RedlineSystemSubnetMaskAddressType_Type = InetAddressType
_RedlineSystemSubnetMaskAddressType_Object = MibScalar
redlineSystemSubnetMaskAddressType = _RedlineSystemSubnetMaskAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 4, 3),
    _RedlineSystemSubnetMaskAddressType_Type()
)
redlineSystemSubnetMaskAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemSubnetMaskAddressType.setStatus("current")
_RedlineSystemSubnetMask_Type = InetAddress
_RedlineSystemSubnetMask_Object = MibScalar
redlineSystemSubnetMask = _RedlineSystemSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 4, 4),
    _RedlineSystemSubnetMask_Type()
)
redlineSystemSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemSubnetMask.setStatus("current")
_RedlineSystemDefGatewayAddressType_Type = InetAddressType
_RedlineSystemDefGatewayAddressType_Object = MibScalar
redlineSystemDefGatewayAddressType = _RedlineSystemDefGatewayAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 4, 5),
    _RedlineSystemDefGatewayAddressType_Type()
)
redlineSystemDefGatewayAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemDefGatewayAddressType.setStatus("current")
_RedlineSystemDefGatewayAddress_Type = InetAddress
_RedlineSystemDefGatewayAddress_Object = MibScalar
redlineSystemDefGatewayAddress = _RedlineSystemDefGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 4, 6),
    _RedlineSystemDefGatewayAddress_Type()
)
redlineSystemDefGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemDefGatewayAddress.setStatus("current")
_RedlineSystemSysSyslogObjects_ObjectIdentity = ObjectIdentity
redlineSystemSysSyslogObjects = _RedlineSystemSysSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 5)
)
_RedlineSystemSyslogServerIpAddressType_Type = InetAddressType
_RedlineSystemSyslogServerIpAddressType_Object = MibScalar
redlineSystemSyslogServerIpAddressType = _RedlineSystemSyslogServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 5, 1),
    _RedlineSystemSyslogServerIpAddressType_Type()
)
redlineSystemSyslogServerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemSyslogServerIpAddressType.setStatus("current")
_RedlineSystemSyslogServerIpAddress_Type = InetAddress
_RedlineSystemSyslogServerIpAddress_Object = MibScalar
redlineSystemSyslogServerIpAddress = _RedlineSystemSyslogServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 1, 5, 2),
    _RedlineSystemSyslogServerIpAddress_Type()
)
redlineSystemSyslogServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemSyslogServerIpAddress.setStatus("current")
_RedlineSystemSoftwareObjects_ObjectIdentity = ObjectIdentity
redlineSystemSoftwareObjects = _RedlineSystemSoftwareObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2)
)


class _RedlineSystemSwActiveVersion_Type(DisplayString):
    """Custom type redlineSystemSwActiveVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemSwActiveVersion_Type.__name__ = "DisplayString"
_RedlineSystemSwActiveVersion_Object = MibScalar
redlineSystemSwActiveVersion = _RedlineSystemSwActiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 1),
    _RedlineSystemSwActiveVersion_Type()
)
redlineSystemSwActiveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemSwActiveVersion.setStatus("current")


class _RedlineSystemSwAlternateVersion_Type(DisplayString):
    """Custom type redlineSystemSwAlternateVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemSwAlternateVersion_Type.__name__ = "DisplayString"
_RedlineSystemSwAlternateVersion_Object = MibScalar
redlineSystemSwAlternateVersion = _RedlineSystemSwAlternateVersion_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 2),
    _RedlineSystemSwAlternateVersion_Type()
)
redlineSystemSwAlternateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemSwAlternateVersion.setStatus("current")


class _RedlineSystemSwActivateAlternate_Type(Integer32):
    """Custom type redlineSystemSwActivateAlternate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("noop", 1))
    )


_RedlineSystemSwActivateAlternate_Type.__name__ = "Integer32"
_RedlineSystemSwActivateAlternate_Object = MibScalar
redlineSystemSwActivateAlternate = _RedlineSystemSwActivateAlternate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 3),
    _RedlineSystemSwActivateAlternate_Type()
)
redlineSystemSwActivateAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemSwActivateAlternate.setStatus("current")
_RedlineSystemSwSyncAlternateTable_Object = MibTable
redlineSystemSwSyncAlternateTable = _RedlineSystemSwSyncAlternateTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    redlineSystemSwSyncAlternateTable.setStatus("current")
_RedlineSystemSwSyncAlternateEntry_Object = MibTableRow
redlineSystemSwSyncAlternateEntry = _RedlineSystemSwSyncAlternateEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 4, 1)
)
redlineSystemSwSyncAlternateEntry.setIndexNames(
    (0, "REDLINE-SYSTEM-MIB", "redlineSystemSwSyncAlternateIndex"),
)
if mibBuilder.loadTexts:
    redlineSystemSwSyncAlternateEntry.setStatus("current")


class _RedlineSystemSwSyncAlternateIndex_Type(Integer32):
    """Custom type redlineSystemSwSyncAlternateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RedlineSystemSwSyncAlternateIndex_Type.__name__ = "Integer32"
_RedlineSystemSwSyncAlternateIndex_Object = MibTableColumn
redlineSystemSwSyncAlternateIndex = _RedlineSystemSwSyncAlternateIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 4, 1, 1),
    _RedlineSystemSwSyncAlternateIndex_Type()
)
redlineSystemSwSyncAlternateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineSystemSwSyncAlternateIndex.setStatus("current")


class _RedlineSystemSwSyncAlternate_Type(Integer32):
    """Custom type redlineSystemSwSyncAlternate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("synchronizeAlternate", 2))
    )


_RedlineSystemSwSyncAlternate_Type.__name__ = "Integer32"
_RedlineSystemSwSyncAlternate_Object = MibTableColumn
redlineSystemSwSyncAlternate = _RedlineSystemSwSyncAlternate_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 4, 1, 2),
    _RedlineSystemSwSyncAlternate_Type()
)
redlineSystemSwSyncAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemSwSyncAlternate.setStatus("current")


class _RedlineSystemSwSyncAlternateStatus_Type(Integer32):
    """Custom type redlineSystemSwSyncAlternateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("inProgress", 1),
          ("success", 2))
    )


_RedlineSystemSwSyncAlternateStatus_Type.__name__ = "Integer32"
_RedlineSystemSwSyncAlternateStatus_Object = MibTableColumn
redlineSystemSwSyncAlternateStatus = _RedlineSystemSwSyncAlternateStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 4, 1, 3),
    _RedlineSystemSwSyncAlternateStatus_Type()
)
redlineSystemSwSyncAlternateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemSwSyncAlternateStatus.setStatus("current")
_RedlineSystemSwSyncAlternateTimeEnded_Type = DateAndTime
_RedlineSystemSwSyncAlternateTimeEnded_Object = MibTableColumn
redlineSystemSwSyncAlternateTimeEnded = _RedlineSystemSwSyncAlternateTimeEnded_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 4, 1, 4),
    _RedlineSystemSwSyncAlternateTimeEnded_Type()
)
redlineSystemSwSyncAlternateTimeEnded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemSwSyncAlternateTimeEnded.setStatus("current")
_RedlineSystemSwDownloadTable_Object = MibTable
redlineSystemSwDownloadTable = _RedlineSystemSwDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    redlineSystemSwDownloadTable.setStatus("current")
_RedlineSystemSwDownloadEntry_Object = MibTableRow
redlineSystemSwDownloadEntry = _RedlineSystemSwDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5, 1)
)
redlineSystemSwDownloadEntry.setIndexNames(
    (0, "REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadIndex"),
)
if mibBuilder.loadTexts:
    redlineSystemSwDownloadEntry.setStatus("current")


class _RedlineSystemSwDownloadIndex_Type(Integer32):
    """Custom type redlineSystemSwDownloadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RedlineSystemSwDownloadIndex_Type.__name__ = "Integer32"
_RedlineSystemSwDownloadIndex_Object = MibTableColumn
redlineSystemSwDownloadIndex = _RedlineSystemSwDownloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5, 1, 1),
    _RedlineSystemSwDownloadIndex_Type()
)
redlineSystemSwDownloadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineSystemSwDownloadIndex.setStatus("current")
_RedlineSystemSwDownloadFtpAddressType_Type = InetAddressType
_RedlineSystemSwDownloadFtpAddressType_Object = MibTableColumn
redlineSystemSwDownloadFtpAddressType = _RedlineSystemSwDownloadFtpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5, 1, 2),
    _RedlineSystemSwDownloadFtpAddressType_Type()
)
redlineSystemSwDownloadFtpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemSwDownloadFtpAddressType.setStatus("current")
_RedlineSystemSwDownloadFtpAddress_Type = InetAddress
_RedlineSystemSwDownloadFtpAddress_Object = MibTableColumn
redlineSystemSwDownloadFtpAddress = _RedlineSystemSwDownloadFtpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5, 1, 3),
    _RedlineSystemSwDownloadFtpAddress_Type()
)
redlineSystemSwDownloadFtpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemSwDownloadFtpAddress.setStatus("current")


class _RedlineSystemSwDownloadFtpUser_Type(DisplayString):
    """Custom type redlineSystemSwDownloadFtpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemSwDownloadFtpUser_Type.__name__ = "DisplayString"
_RedlineSystemSwDownloadFtpUser_Object = MibTableColumn
redlineSystemSwDownloadFtpUser = _RedlineSystemSwDownloadFtpUser_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5, 1, 4),
    _RedlineSystemSwDownloadFtpUser_Type()
)
redlineSystemSwDownloadFtpUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemSwDownloadFtpUser.setStatus("current")


class _RedlineSystemSwDownloadFtpPassword_Type(DisplayString):
    """Custom type redlineSystemSwDownloadFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemSwDownloadFtpPassword_Type.__name__ = "DisplayString"
_RedlineSystemSwDownloadFtpPassword_Object = MibTableColumn
redlineSystemSwDownloadFtpPassword = _RedlineSystemSwDownloadFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5, 1, 5),
    _RedlineSystemSwDownloadFtpPassword_Type()
)
redlineSystemSwDownloadFtpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemSwDownloadFtpPassword.setStatus("current")


class _RedlineSystemSwDownloadFtpFile_Type(DisplayString):
    """Custom type redlineSystemSwDownloadFtpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RedlineSystemSwDownloadFtpFile_Type.__name__ = "DisplayString"
_RedlineSystemSwDownloadFtpFile_Object = MibTableColumn
redlineSystemSwDownloadFtpFile = _RedlineSystemSwDownloadFtpFile_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5, 1, 6),
    _RedlineSystemSwDownloadFtpFile_Type()
)
redlineSystemSwDownloadFtpFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemSwDownloadFtpFile.setStatus("current")


class _RedlineSystemSwDownloadStatus_Type(Integer32):
    """Custom type redlineSystemSwDownloadStatus based on Integer32"""
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
        *(("commit", 3),
          ("download", 1),
          ("failed", 5),
          ("success", 4),
          ("validate", 2))
    )


_RedlineSystemSwDownloadStatus_Type.__name__ = "Integer32"
_RedlineSystemSwDownloadStatus_Object = MibTableColumn
redlineSystemSwDownloadStatus = _RedlineSystemSwDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5, 1, 7),
    _RedlineSystemSwDownloadStatus_Type()
)
redlineSystemSwDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemSwDownloadStatus.setStatus("current")
_RedlineSystemSwDownloadTimeEnded_Type = DateAndTime
_RedlineSystemSwDownloadTimeEnded_Object = MibTableColumn
redlineSystemSwDownloadTimeEnded = _RedlineSystemSwDownloadTimeEnded_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5, 1, 8),
    _RedlineSystemSwDownloadTimeEnded_Type()
)
redlineSystemSwDownloadTimeEnded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemSwDownloadTimeEnded.setStatus("current")


class _RedlineSystemSwDownloadFailureReason_Type(DisplayString):
    """Custom type redlineSystemSwDownloadFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RedlineSystemSwDownloadFailureReason_Type.__name__ = "DisplayString"
_RedlineSystemSwDownloadFailureReason_Object = MibTableColumn
redlineSystemSwDownloadFailureReason = _RedlineSystemSwDownloadFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 2, 5, 1, 9),
    _RedlineSystemSwDownloadFailureReason_Type()
)
redlineSystemSwDownloadFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemSwDownloadFailureReason.setStatus("current")
_RedlineSystemConfigurationObjects_ObjectIdentity = ObjectIdentity
redlineSystemConfigurationObjects = _RedlineSystemConfigurationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3)
)
_RedlineSystemConfigBackupTable_Object = MibTable
redlineSystemConfigBackupTable = _RedlineSystemConfigBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    redlineSystemConfigBackupTable.setStatus("current")
_RedlineSystemConfigBackupEntry_Object = MibTableRow
redlineSystemConfigBackupEntry = _RedlineSystemConfigBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1, 1)
)
redlineSystemConfigBackupEntry.setIndexNames(
    (0, "REDLINE-SYSTEM-MIB", "redlineSystemConfigBackupIndex"),
)
if mibBuilder.loadTexts:
    redlineSystemConfigBackupEntry.setStatus("current")


class _RedlineSystemConfigBackupIndex_Type(Integer32):
    """Custom type redlineSystemConfigBackupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RedlineSystemConfigBackupIndex_Type.__name__ = "Integer32"
_RedlineSystemConfigBackupIndex_Object = MibTableColumn
redlineSystemConfigBackupIndex = _RedlineSystemConfigBackupIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1, 1, 1),
    _RedlineSystemConfigBackupIndex_Type()
)
redlineSystemConfigBackupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineSystemConfigBackupIndex.setStatus("current")


class _RedlineSystemConfigBackupConfigType_Type(Integer32):
    """Custom type redlineSystemConfigBackupConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("alternate", 2))
    )


_RedlineSystemConfigBackupConfigType_Type.__name__ = "Integer32"
_RedlineSystemConfigBackupConfigType_Object = MibTableColumn
redlineSystemConfigBackupConfigType = _RedlineSystemConfigBackupConfigType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1, 1, 2),
    _RedlineSystemConfigBackupConfigType_Type()
)
redlineSystemConfigBackupConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigBackupConfigType.setStatus("current")
_RedlineSystemConfigBackupFtpAddressType_Type = InetAddressType
_RedlineSystemConfigBackupFtpAddressType_Object = MibTableColumn
redlineSystemConfigBackupFtpAddressType = _RedlineSystemConfigBackupFtpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1, 1, 3),
    _RedlineSystemConfigBackupFtpAddressType_Type()
)
redlineSystemConfigBackupFtpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigBackupFtpAddressType.setStatus("current")
_RedlineSystemConfigBackupFtpAddress_Type = InetAddress
_RedlineSystemConfigBackupFtpAddress_Object = MibTableColumn
redlineSystemConfigBackupFtpAddress = _RedlineSystemConfigBackupFtpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1, 1, 4),
    _RedlineSystemConfigBackupFtpAddress_Type()
)
redlineSystemConfigBackupFtpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigBackupFtpAddress.setStatus("current")


class _RedlineSystemConfigBackupFtpUser_Type(DisplayString):
    """Custom type redlineSystemConfigBackupFtpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemConfigBackupFtpUser_Type.__name__ = "DisplayString"
_RedlineSystemConfigBackupFtpUser_Object = MibTableColumn
redlineSystemConfigBackupFtpUser = _RedlineSystemConfigBackupFtpUser_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1, 1, 5),
    _RedlineSystemConfigBackupFtpUser_Type()
)
redlineSystemConfigBackupFtpUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigBackupFtpUser.setStatus("current")


class _RedlineSystemConfigBackupFtpPassword_Type(DisplayString):
    """Custom type redlineSystemConfigBackupFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemConfigBackupFtpPassword_Type.__name__ = "DisplayString"
_RedlineSystemConfigBackupFtpPassword_Object = MibTableColumn
redlineSystemConfigBackupFtpPassword = _RedlineSystemConfigBackupFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1, 1, 6),
    _RedlineSystemConfigBackupFtpPassword_Type()
)
redlineSystemConfigBackupFtpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigBackupFtpPassword.setStatus("current")


class _RedlineSystemConfigBackupFtpFile_Type(DisplayString):
    """Custom type redlineSystemConfigBackupFtpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RedlineSystemConfigBackupFtpFile_Type.__name__ = "DisplayString"
_RedlineSystemConfigBackupFtpFile_Object = MibTableColumn
redlineSystemConfigBackupFtpFile = _RedlineSystemConfigBackupFtpFile_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1, 1, 7),
    _RedlineSystemConfigBackupFtpFile_Type()
)
redlineSystemConfigBackupFtpFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigBackupFtpFile.setStatus("current")


class _RedlineSystemConfigBackupStatus_Type(Integer32):
    """Custom type redlineSystemConfigBackupStatus based on Integer32"""
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
        *(("backup", 1),
          ("commit", 2),
          ("failed", 5),
          ("success", 4),
          ("upload", 3))
    )


_RedlineSystemConfigBackupStatus_Type.__name__ = "Integer32"
_RedlineSystemConfigBackupStatus_Object = MibTableColumn
redlineSystemConfigBackupStatus = _RedlineSystemConfigBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1, 1, 8),
    _RedlineSystemConfigBackupStatus_Type()
)
redlineSystemConfigBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemConfigBackupStatus.setStatus("current")


class _RedlineSystemConfigBackupFailureReason_Type(DisplayString):
    """Custom type redlineSystemConfigBackupFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RedlineSystemConfigBackupFailureReason_Type.__name__ = "DisplayString"
_RedlineSystemConfigBackupFailureReason_Object = MibTableColumn
redlineSystemConfigBackupFailureReason = _RedlineSystemConfigBackupFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 1, 1, 9),
    _RedlineSystemConfigBackupFailureReason_Type()
)
redlineSystemConfigBackupFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemConfigBackupFailureReason.setStatus("current")
_RedlineSystemConfigRestoreTable_Object = MibTable
redlineSystemConfigRestoreTable = _RedlineSystemConfigRestoreTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreTable.setStatus("current")
_RedlineSystemConfigRestoreEntry_Object = MibTableRow
redlineSystemConfigRestoreEntry = _RedlineSystemConfigRestoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2, 1)
)
redlineSystemConfigRestoreEntry.setIndexNames(
    (0, "REDLINE-SYSTEM-MIB", "redlineSystemConfigRestoreIndex"),
)
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreEntry.setStatus("current")


class _RedlineSystemConfigRestoreIndex_Type(Integer32):
    """Custom type redlineSystemConfigRestoreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RedlineSystemConfigRestoreIndex_Type.__name__ = "Integer32"
_RedlineSystemConfigRestoreIndex_Object = MibTableColumn
redlineSystemConfigRestoreIndex = _RedlineSystemConfigRestoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2, 1, 1),
    _RedlineSystemConfigRestoreIndex_Type()
)
redlineSystemConfigRestoreIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreIndex.setStatus("current")


class _RedlineSystemConfigRestoreConfigType_Type(Integer32):
    """Custom type redlineSystemConfigRestoreConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("alternate", 2))
    )


_RedlineSystemConfigRestoreConfigType_Type.__name__ = "Integer32"
_RedlineSystemConfigRestoreConfigType_Object = MibTableColumn
redlineSystemConfigRestoreConfigType = _RedlineSystemConfigRestoreConfigType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2, 1, 2),
    _RedlineSystemConfigRestoreConfigType_Type()
)
redlineSystemConfigRestoreConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreConfigType.setStatus("current")
_RedlineSystemConfigRestoreFtpAddressType_Type = InetAddressType
_RedlineSystemConfigRestoreFtpAddressType_Object = MibTableColumn
redlineSystemConfigRestoreFtpAddressType = _RedlineSystemConfigRestoreFtpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2, 1, 3),
    _RedlineSystemConfigRestoreFtpAddressType_Type()
)
redlineSystemConfigRestoreFtpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreFtpAddressType.setStatus("current")
_RedlineSystemConfigRestoreFtpAddress_Type = InetAddress
_RedlineSystemConfigRestoreFtpAddress_Object = MibTableColumn
redlineSystemConfigRestoreFtpAddress = _RedlineSystemConfigRestoreFtpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2, 1, 4),
    _RedlineSystemConfigRestoreFtpAddress_Type()
)
redlineSystemConfigRestoreFtpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreFtpAddress.setStatus("current")


class _RedlineSystemConfigRestoreFtpUser_Type(DisplayString):
    """Custom type redlineSystemConfigRestoreFtpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemConfigRestoreFtpUser_Type.__name__ = "DisplayString"
_RedlineSystemConfigRestoreFtpUser_Object = MibTableColumn
redlineSystemConfigRestoreFtpUser = _RedlineSystemConfigRestoreFtpUser_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2, 1, 5),
    _RedlineSystemConfigRestoreFtpUser_Type()
)
redlineSystemConfigRestoreFtpUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreFtpUser.setStatus("current")


class _RedlineSystemConfigRestoreFtpPassword_Type(DisplayString):
    """Custom type redlineSystemConfigRestoreFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemConfigRestoreFtpPassword_Type.__name__ = "DisplayString"
_RedlineSystemConfigRestoreFtpPassword_Object = MibTableColumn
redlineSystemConfigRestoreFtpPassword = _RedlineSystemConfigRestoreFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2, 1, 6),
    _RedlineSystemConfigRestoreFtpPassword_Type()
)
redlineSystemConfigRestoreFtpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreFtpPassword.setStatus("current")


class _RedlineSystemConfigRestoreFtpFile_Type(DisplayString):
    """Custom type redlineSystemConfigRestoreFtpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RedlineSystemConfigRestoreFtpFile_Type.__name__ = "DisplayString"
_RedlineSystemConfigRestoreFtpFile_Object = MibTableColumn
redlineSystemConfigRestoreFtpFile = _RedlineSystemConfigRestoreFtpFile_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2, 1, 7),
    _RedlineSystemConfigRestoreFtpFile_Type()
)
redlineSystemConfigRestoreFtpFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreFtpFile.setStatus("current")


class _RedlineSystemConfigRestoreStatus_Type(Integer32):
    """Custom type redlineSystemConfigRestoreStatus based on Integer32"""
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
        *(("download", 2),
          ("failed", 5),
          ("restore", 1),
          ("success", 4),
          ("write", 3))
    )


_RedlineSystemConfigRestoreStatus_Type.__name__ = "Integer32"
_RedlineSystemConfigRestoreStatus_Object = MibTableColumn
redlineSystemConfigRestoreStatus = _RedlineSystemConfigRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2, 1, 8),
    _RedlineSystemConfigRestoreStatus_Type()
)
redlineSystemConfigRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreStatus.setStatus("current")


class _RedlineSystemConfigRestoreFailureReason_Type(DisplayString):
    """Custom type redlineSystemConfigRestoreFailureReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RedlineSystemConfigRestoreFailureReason_Type.__name__ = "DisplayString"
_RedlineSystemConfigRestoreFailureReason_Object = MibTableColumn
redlineSystemConfigRestoreFailureReason = _RedlineSystemConfigRestoreFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 3, 2, 1, 9),
    _RedlineSystemConfigRestoreFailureReason_Type()
)
redlineSystemConfigRestoreFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineSystemConfigRestoreFailureReason.setStatus("current")
_RedlineSystemNotificationObjects_ObjectIdentity = ObjectIdentity
redlineSystemNotificationObjects = _RedlineSystemNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4)
)
_RedlineSystemTrapControl_ObjectIdentity = ObjectIdentity
redlineSystemTrapControl = _RedlineSystemTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1)
)
_RedlineSystemTrapReceiverTable_Object = MibTable
redlineSystemTrapReceiverTable = _RedlineSystemTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    redlineSystemTrapReceiverTable.setStatus("current")
_RedlineSystemTrapReceiverEntry_Object = MibTableRow
redlineSystemTrapReceiverEntry = _RedlineSystemTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 1, 1)
)
redlineSystemTrapReceiverEntry.setIndexNames(
    (0, "REDLINE-SYSTEM-MIB", "redlineSystemTrapReceiverIndex"),
)
if mibBuilder.loadTexts:
    redlineSystemTrapReceiverEntry.setStatus("current")
_RedlineSystemTrapReceiverIndex_Type = Unsigned32
_RedlineSystemTrapReceiverIndex_Object = MibTableColumn
redlineSystemTrapReceiverIndex = _RedlineSystemTrapReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 1, 1, 1),
    _RedlineSystemTrapReceiverIndex_Type()
)
redlineSystemTrapReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineSystemTrapReceiverIndex.setStatus("current")
_RedlineSystemTrapReceiverAddressType_Type = InetAddressType
_RedlineSystemTrapReceiverAddressType_Object = MibTableColumn
redlineSystemTrapReceiverAddressType = _RedlineSystemTrapReceiverAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 1, 1, 2),
    _RedlineSystemTrapReceiverAddressType_Type()
)
redlineSystemTrapReceiverAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemTrapReceiverAddressType.setStatus("current")
_RedlineSystemTrapReceiverAddress_Type = InetAddress
_RedlineSystemTrapReceiverAddress_Object = MibTableColumn
redlineSystemTrapReceiverAddress = _RedlineSystemTrapReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 1, 1, 3),
    _RedlineSystemTrapReceiverAddress_Type()
)
redlineSystemTrapReceiverAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemTrapReceiverAddress.setStatus("current")


class _RedlineSystemTrapReceiverPort_Type(InetPortNumber):
    """Custom type redlineSystemTrapReceiverPort based on InetPortNumber"""
    defaultValue = 162

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RedlineSystemTrapReceiverPort_Type.__name__ = "InetPortNumber"
_RedlineSystemTrapReceiverPort_Object = MibTableColumn
redlineSystemTrapReceiverPort = _RedlineSystemTrapReceiverPort_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 1, 1, 4),
    _RedlineSystemTrapReceiverPort_Type()
)
redlineSystemTrapReceiverPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemTrapReceiverPort.setStatus("current")


class _RedlineSystemTrapReceiverCommunity_Type(DisplayString):
    """Custom type redlineSystemTrapReceiverCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemTrapReceiverCommunity_Type.__name__ = "DisplayString"
_RedlineSystemTrapReceiverCommunity_Object = MibTableColumn
redlineSystemTrapReceiverCommunity = _RedlineSystemTrapReceiverCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 1, 1, 5),
    _RedlineSystemTrapReceiverCommunity_Type()
)
redlineSystemTrapReceiverCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemTrapReceiverCommunity.setStatus("current")
_RedlineSystemTrapReceiverStatus_Type = RowStatus
_RedlineSystemTrapReceiverStatus_Object = MibTableColumn
redlineSystemTrapReceiverStatus = _RedlineSystemTrapReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 1, 1, 6),
    _RedlineSystemTrapReceiverStatus_Type()
)
redlineSystemTrapReceiverStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemTrapReceiverStatus.setStatus("current")
_RedlineSystemTrapActivationTable_Object = MibTable
redlineSystemTrapActivationTable = _RedlineSystemTrapActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    redlineSystemTrapActivationTable.setStatus("current")
_RedlineSystemTrapActivationEntry_Object = MibTableRow
redlineSystemTrapActivationEntry = _RedlineSystemTrapActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 2, 1)
)
redlineSystemTrapActivationEntry.setIndexNames(
    (1, "REDLINE-SYSTEM-MIB", "redlineSystemTrapObjectID"),
)
if mibBuilder.loadTexts:
    redlineSystemTrapActivationEntry.setStatus("current")
_RedlineSystemTrapObjectID_Type = ObjectIdentifier
_RedlineSystemTrapObjectID_Object = MibTableColumn
redlineSystemTrapObjectID = _RedlineSystemTrapObjectID_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 2, 1, 1),
    _RedlineSystemTrapObjectID_Type()
)
redlineSystemTrapObjectID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineSystemTrapObjectID.setStatus("current")


class _RedlineSystemTrapEnable_Type(Integer32):
    """Custom type redlineSystemTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RedlineSystemTrapEnable_Type.__name__ = "Integer32"
_RedlineSystemTrapEnable_Object = MibTableColumn
redlineSystemTrapEnable = _RedlineSystemTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 2, 1, 2),
    _RedlineSystemTrapEnable_Type()
)
redlineSystemTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemTrapEnable.setStatus("current")


class _RedlineSystemPingTrapTrigger_Type(Integer32):
    """Custom type redlineSystemPingTrapTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("ping", 2))
    )


_RedlineSystemPingTrapTrigger_Type.__name__ = "Integer32"
_RedlineSystemPingTrapTrigger_Object = MibScalar
redlineSystemPingTrapTrigger = _RedlineSystemPingTrapTrigger_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 1, 999),
    _RedlineSystemPingTrapTrigger_Type()
)
redlineSystemPingTrapTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineSystemPingTrapTrigger.setStatus("current")
_RedlineSystemTrapObjects_ObjectIdentity = ObjectIdentity
redlineSystemTrapObjects = _RedlineSystemTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 2)
)


class _RedlineSystemSwDownloadProgress_Type(Integer32):
    """Custom type redlineSystemSwDownloadProgress based on Integer32"""
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
        *(("committed", 4),
          ("downloaded", 2),
          ("failed", 5),
          ("initiated", 1),
          ("validated", 3))
    )


_RedlineSystemSwDownloadProgress_Type.__name__ = "Integer32"
_RedlineSystemSwDownloadProgress_Object = MibScalar
redlineSystemSwDownloadProgress = _RedlineSystemSwDownloadProgress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 2, 1),
    _RedlineSystemSwDownloadProgress_Type()
)
redlineSystemSwDownloadProgress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    redlineSystemSwDownloadProgress.setStatus("current")
_RedlineSystemTrapDefinitions_ObjectIdentity = ObjectIdentity
redlineSystemTrapDefinitions = _RedlineSystemTrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 3)
)
_RedlineSystemAccessControlObjects_ObjectIdentity = ObjectIdentity
redlineSystemAccessControlObjects = _RedlineSystemAccessControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 5)
)
_RedlineSystemAccessCtrlTable_Object = MibTable
redlineSystemAccessCtrlTable = _RedlineSystemAccessCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 5, 5)
)
if mibBuilder.loadTexts:
    redlineSystemAccessCtrlTable.setStatus("current")
_RedlineSystemAccessCtrlEntry_Object = MibTableRow
redlineSystemAccessCtrlEntry = _RedlineSystemAccessCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 5, 5, 1)
)
redlineSystemAccessCtrlEntry.setIndexNames(
    (0, "REDLINE-SYSTEM-MIB", "redlineSystemAccessCtrlIndex"),
)
if mibBuilder.loadTexts:
    redlineSystemAccessCtrlEntry.setStatus("current")


class _RedlineSystemAccessCtrlIndex_Type(Unsigned32):
    """Custom type redlineSystemAccessCtrlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RedlineSystemAccessCtrlIndex_Type.__name__ = "Unsigned32"
_RedlineSystemAccessCtrlIndex_Object = MibTableColumn
redlineSystemAccessCtrlIndex = _RedlineSystemAccessCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 5, 5, 1, 1),
    _RedlineSystemAccessCtrlIndex_Type()
)
redlineSystemAccessCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineSystemAccessCtrlIndex.setStatus("current")
_RedlineSystemAccessCtrlManagerIpAddrType_Type = InetAddressType
_RedlineSystemAccessCtrlManagerIpAddrType_Object = MibTableColumn
redlineSystemAccessCtrlManagerIpAddrType = _RedlineSystemAccessCtrlManagerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 5, 5, 1, 2),
    _RedlineSystemAccessCtrlManagerIpAddrType_Type()
)
redlineSystemAccessCtrlManagerIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemAccessCtrlManagerIpAddrType.setStatus("current")
_RedlineSystemAccessCtrlManagerIpAddr_Type = InetAddress
_RedlineSystemAccessCtrlManagerIpAddr_Object = MibTableColumn
redlineSystemAccessCtrlManagerIpAddr = _RedlineSystemAccessCtrlManagerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 5, 5, 1, 3),
    _RedlineSystemAccessCtrlManagerIpAddr_Type()
)
redlineSystemAccessCtrlManagerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemAccessCtrlManagerIpAddr.setStatus("current")


class _RedlineSystemAccessCtrlReadCommunity_Type(DisplayString):
    """Custom type redlineSystemAccessCtrlReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemAccessCtrlReadCommunity_Type.__name__ = "DisplayString"
_RedlineSystemAccessCtrlReadCommunity_Object = MibTableColumn
redlineSystemAccessCtrlReadCommunity = _RedlineSystemAccessCtrlReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 5, 5, 1, 4),
    _RedlineSystemAccessCtrlReadCommunity_Type()
)
redlineSystemAccessCtrlReadCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemAccessCtrlReadCommunity.setStatus("current")


class _RedlineSystemAccessCtrlWriteCommunity_Type(DisplayString):
    """Custom type redlineSystemAccessCtrlWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineSystemAccessCtrlWriteCommunity_Type.__name__ = "DisplayString"
_RedlineSystemAccessCtrlWriteCommunity_Object = MibTableColumn
redlineSystemAccessCtrlWriteCommunity = _RedlineSystemAccessCtrlWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 5, 5, 1, 5),
    _RedlineSystemAccessCtrlWriteCommunity_Type()
)
redlineSystemAccessCtrlWriteCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemAccessCtrlWriteCommunity.setStatus("current")
_RedlineSystemAccessCtrlStatus_Type = RowStatus
_RedlineSystemAccessCtrlStatus_Object = MibTableColumn
redlineSystemAccessCtrlStatus = _RedlineSystemAccessCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 5, 5, 1, 6),
    _RedlineSystemAccessCtrlStatus_Type()
)
redlineSystemAccessCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    redlineSystemAccessCtrlStatus.setStatus("current")
_RedlineSystemConformance_ObjectIdentity = ObjectIdentity
redlineSystemConformance = _RedlineSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 6)
)
_RedlineSystemGroups_ObjectIdentity = ObjectIdentity
redlineSystemGroups = _RedlineSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 6, 1)
)
_RedlineSystemCompls_ObjectIdentity = ObjectIdentity
redlineSystemCompls = _RedlineSystemCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 6, 2)
)

# Managed Objects groups

redlineSystemBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 6, 1, 1)
)
redlineSystemBasicGroup.setObjects(
      *(("REDLINE-SYSTEM-MIB", "redlineSystemSystemReboot"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSerialNumber"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemTrapReceiverCommunity"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemTrapReceiverStatus"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemPingTrapTrigger"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadFtpAddress"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadFtpUser"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadFtpPassword"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadFtpFile"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadStatus"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadFailureReason"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadTimeEnded"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadFtpAddressType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwActiveVersion"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwAlternateVersion"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwActivateAlternate"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemTrapReceiverAddressType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemTrapReceiverAddress"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemTrapReceiverPort"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemTrapEnable"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwSyncAlternate"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwSyncAlternateStatus"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemDHCPServerIpAddressType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemDHCPServerIpAddress"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemIpAddressType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemIpAddress"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSubnetMaskAddressType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSubnetMask"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemDefGatewayAddressType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemDefGatewayAddress"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSyslogServerIpAddressType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSyslogServerIpAddress"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadProgress"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigBackupConfigType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigBackupFtpAddressType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigBackupFtpAddress"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigBackupFtpUser"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigBackupFtpPassword"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigBackupFtpFile"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigBackupStatus"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigBackupFailureReason"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigRestoreConfigType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigRestoreFtpAddressType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigRestoreFtpAddress"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigRestoreFtpUser"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigRestoreFtpPassword"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigRestoreFtpFile"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigRestoreStatus"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemConfigRestoreFailureReason"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemAccessCtrlManagerIpAddrType"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemAccessCtrlManagerIpAddr"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemAccessCtrlReadCommunity"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemAccessCtrlWriteCommunity"))
)
if mibBuilder.loadTexts:
    redlineSystemBasicGroup.setStatus("current")


# Notification objects

redlineSWUpgradeStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 3, 1)
)
redlineSWUpgradeStatusTrap.setObjects(
    ("REDLINE-SYSTEM-MIB", "redlineSystemSwDownloadProgress")
)
if mibBuilder.loadTexts:
    redlineSWUpgradeStatusTrap.setStatus(
        "current"
    )

redlineSystemPingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 4, 3, 999)
)
if mibBuilder.loadTexts:
    redlineSystemPingTrap.setStatus(
        "current"
    )


# Notifications groups

redlineSystemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 6, 1, 2)
)
redlineSystemNotificationGroup.setObjects(
      *(("REDLINE-SYSTEM-MIB", "redlineSWUpgradeStatusTrap"),
        ("REDLINE-SYSTEM-MIB", "redlineSystemPingTrap"))
)
if mibBuilder.loadTexts:
    redlineSystemNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

redlineSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    redlineSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDLINE-SYSTEM-MIB",
    **{"redlineSystemMib": redlineSystemMib,
       "redlineSystemSystemObjects": redlineSystemSystemObjects,
       "redlineSystemSerialNumber": redlineSystemSerialNumber,
       "redlineSystemSysControl": redlineSystemSysControl,
       "redlineSystemSystemReboot": redlineSystemSystemReboot,
       "redlineSystemSysDhcpObjects": redlineSystemSysDhcpObjects,
       "redlineSystemDHCPServerIpAddressType": redlineSystemDHCPServerIpAddressType,
       "redlineSystemDHCPServerIpAddress": redlineSystemDHCPServerIpAddress,
       "redlineSystemSysIpObjects": redlineSystemSysIpObjects,
       "redlineSystemIpAddressType": redlineSystemIpAddressType,
       "redlineSystemIpAddress": redlineSystemIpAddress,
       "redlineSystemSubnetMaskAddressType": redlineSystemSubnetMaskAddressType,
       "redlineSystemSubnetMask": redlineSystemSubnetMask,
       "redlineSystemDefGatewayAddressType": redlineSystemDefGatewayAddressType,
       "redlineSystemDefGatewayAddress": redlineSystemDefGatewayAddress,
       "redlineSystemSysSyslogObjects": redlineSystemSysSyslogObjects,
       "redlineSystemSyslogServerIpAddressType": redlineSystemSyslogServerIpAddressType,
       "redlineSystemSyslogServerIpAddress": redlineSystemSyslogServerIpAddress,
       "redlineSystemSoftwareObjects": redlineSystemSoftwareObjects,
       "redlineSystemSwActiveVersion": redlineSystemSwActiveVersion,
       "redlineSystemSwAlternateVersion": redlineSystemSwAlternateVersion,
       "redlineSystemSwActivateAlternate": redlineSystemSwActivateAlternate,
       "redlineSystemSwSyncAlternateTable": redlineSystemSwSyncAlternateTable,
       "redlineSystemSwSyncAlternateEntry": redlineSystemSwSyncAlternateEntry,
       "redlineSystemSwSyncAlternateIndex": redlineSystemSwSyncAlternateIndex,
       "redlineSystemSwSyncAlternate": redlineSystemSwSyncAlternate,
       "redlineSystemSwSyncAlternateStatus": redlineSystemSwSyncAlternateStatus,
       "redlineSystemSwSyncAlternateTimeEnded": redlineSystemSwSyncAlternateTimeEnded,
       "redlineSystemSwDownloadTable": redlineSystemSwDownloadTable,
       "redlineSystemSwDownloadEntry": redlineSystemSwDownloadEntry,
       "redlineSystemSwDownloadIndex": redlineSystemSwDownloadIndex,
       "redlineSystemSwDownloadFtpAddressType": redlineSystemSwDownloadFtpAddressType,
       "redlineSystemSwDownloadFtpAddress": redlineSystemSwDownloadFtpAddress,
       "redlineSystemSwDownloadFtpUser": redlineSystemSwDownloadFtpUser,
       "redlineSystemSwDownloadFtpPassword": redlineSystemSwDownloadFtpPassword,
       "redlineSystemSwDownloadFtpFile": redlineSystemSwDownloadFtpFile,
       "redlineSystemSwDownloadStatus": redlineSystemSwDownloadStatus,
       "redlineSystemSwDownloadTimeEnded": redlineSystemSwDownloadTimeEnded,
       "redlineSystemSwDownloadFailureReason": redlineSystemSwDownloadFailureReason,
       "redlineSystemConfigurationObjects": redlineSystemConfigurationObjects,
       "redlineSystemConfigBackupTable": redlineSystemConfigBackupTable,
       "redlineSystemConfigBackupEntry": redlineSystemConfigBackupEntry,
       "redlineSystemConfigBackupIndex": redlineSystemConfigBackupIndex,
       "redlineSystemConfigBackupConfigType": redlineSystemConfigBackupConfigType,
       "redlineSystemConfigBackupFtpAddressType": redlineSystemConfigBackupFtpAddressType,
       "redlineSystemConfigBackupFtpAddress": redlineSystemConfigBackupFtpAddress,
       "redlineSystemConfigBackupFtpUser": redlineSystemConfigBackupFtpUser,
       "redlineSystemConfigBackupFtpPassword": redlineSystemConfigBackupFtpPassword,
       "redlineSystemConfigBackupFtpFile": redlineSystemConfigBackupFtpFile,
       "redlineSystemConfigBackupStatus": redlineSystemConfigBackupStatus,
       "redlineSystemConfigBackupFailureReason": redlineSystemConfigBackupFailureReason,
       "redlineSystemConfigRestoreTable": redlineSystemConfigRestoreTable,
       "redlineSystemConfigRestoreEntry": redlineSystemConfigRestoreEntry,
       "redlineSystemConfigRestoreIndex": redlineSystemConfigRestoreIndex,
       "redlineSystemConfigRestoreConfigType": redlineSystemConfigRestoreConfigType,
       "redlineSystemConfigRestoreFtpAddressType": redlineSystemConfigRestoreFtpAddressType,
       "redlineSystemConfigRestoreFtpAddress": redlineSystemConfigRestoreFtpAddress,
       "redlineSystemConfigRestoreFtpUser": redlineSystemConfigRestoreFtpUser,
       "redlineSystemConfigRestoreFtpPassword": redlineSystemConfigRestoreFtpPassword,
       "redlineSystemConfigRestoreFtpFile": redlineSystemConfigRestoreFtpFile,
       "redlineSystemConfigRestoreStatus": redlineSystemConfigRestoreStatus,
       "redlineSystemConfigRestoreFailureReason": redlineSystemConfigRestoreFailureReason,
       "redlineSystemNotificationObjects": redlineSystemNotificationObjects,
       "redlineSystemTrapControl": redlineSystemTrapControl,
       "redlineSystemTrapReceiverTable": redlineSystemTrapReceiverTable,
       "redlineSystemTrapReceiverEntry": redlineSystemTrapReceiverEntry,
       "redlineSystemTrapReceiverIndex": redlineSystemTrapReceiverIndex,
       "redlineSystemTrapReceiverAddressType": redlineSystemTrapReceiverAddressType,
       "redlineSystemTrapReceiverAddress": redlineSystemTrapReceiverAddress,
       "redlineSystemTrapReceiverPort": redlineSystemTrapReceiverPort,
       "redlineSystemTrapReceiverCommunity": redlineSystemTrapReceiverCommunity,
       "redlineSystemTrapReceiverStatus": redlineSystemTrapReceiverStatus,
       "redlineSystemTrapActivationTable": redlineSystemTrapActivationTable,
       "redlineSystemTrapActivationEntry": redlineSystemTrapActivationEntry,
       "redlineSystemTrapObjectID": redlineSystemTrapObjectID,
       "redlineSystemTrapEnable": redlineSystemTrapEnable,
       "redlineSystemPingTrapTrigger": redlineSystemPingTrapTrigger,
       "redlineSystemTrapObjects": redlineSystemTrapObjects,
       "redlineSystemSwDownloadProgress": redlineSystemSwDownloadProgress,
       "redlineSystemTrapDefinitions": redlineSystemTrapDefinitions,
       "redlineSWUpgradeStatusTrap": redlineSWUpgradeStatusTrap,
       "redlineSystemPingTrap": redlineSystemPingTrap,
       "redlineSystemAccessControlObjects": redlineSystemAccessControlObjects,
       "redlineSystemAccessCtrlTable": redlineSystemAccessCtrlTable,
       "redlineSystemAccessCtrlEntry": redlineSystemAccessCtrlEntry,
       "redlineSystemAccessCtrlIndex": redlineSystemAccessCtrlIndex,
       "redlineSystemAccessCtrlManagerIpAddrType": redlineSystemAccessCtrlManagerIpAddrType,
       "redlineSystemAccessCtrlManagerIpAddr": redlineSystemAccessCtrlManagerIpAddr,
       "redlineSystemAccessCtrlReadCommunity": redlineSystemAccessCtrlReadCommunity,
       "redlineSystemAccessCtrlWriteCommunity": redlineSystemAccessCtrlWriteCommunity,
       "redlineSystemAccessCtrlStatus": redlineSystemAccessCtrlStatus,
       "redlineSystemConformance": redlineSystemConformance,
       "redlineSystemGroups": redlineSystemGroups,
       "redlineSystemBasicGroup": redlineSystemBasicGroup,
       "redlineSystemNotificationGroup": redlineSystemNotificationGroup,
       "redlineSystemCompls": redlineSystemCompls,
       "redlineSystemCompliance": redlineSystemCompliance}
)
