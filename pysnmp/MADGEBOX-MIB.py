# SNMP MIB module (MADGEBOX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MADGEBOX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:57 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Madge_ObjectIdentity = ObjectIdentity
madge = _Madge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494)
)
_MadgeBox_ObjectIdentity = ObjectIdentity
madgeBox = _MadgeBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 10)
)
_MadgeConfig_ObjectIdentity = ObjectIdentity
madgeConfig = _MadgeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 10, 1)
)
_MadgeConfigIPAddress_Type = IpAddress
_MadgeConfigIPAddress_Object = MibScalar
madgeConfigIPAddress = _MadgeConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 1),
    _MadgeConfigIPAddress_Type()
)
madgeConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigIPAddress.setStatus("mandatory")
_MadgeConfigIPGateway_Type = IpAddress
_MadgeConfigIPGateway_Object = MibScalar
madgeConfigIPGateway = _MadgeConfigIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 2),
    _MadgeConfigIPGateway_Type()
)
madgeConfigIPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigIPGateway.setStatus("mandatory")
_MadgeConfigIPSubnetMask_Type = IpAddress
_MadgeConfigIPSubnetMask_Object = MibScalar
madgeConfigIPSubnetMask = _MadgeConfigIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 3),
    _MadgeConfigIPSubnetMask_Type()
)
madgeConfigIPSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigIPSubnetMask.setStatus("mandatory")
_MadgeConfigSerialNumber_Type = MacAddress
_MadgeConfigSerialNumber_Object = MibScalar
madgeConfigSerialNumber = _MadgeConfigSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 4),
    _MadgeConfigSerialNumber_Type()
)
madgeConfigSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeConfigSerialNumber.setStatus("mandatory")


class _MadgeConfigMCodeVersion_Type(OctetString):
    """Custom type madgeConfigMCodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MadgeConfigMCodeVersion_Type.__name__ = "OctetString"
_MadgeConfigMCodeVersion_Object = MibScalar
madgeConfigMCodeVersion = _MadgeConfigMCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 5),
    _MadgeConfigMCodeVersion_Type()
)
madgeConfigMCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeConfigMCodeVersion.setStatus("mandatory")


class _MadgeConfigBCodeVersion_Type(OctetString):
    """Custom type madgeConfigBCodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MadgeConfigBCodeVersion_Type.__name__ = "OctetString"
_MadgeConfigBCodeVersion_Object = MibScalar
madgeConfigBCodeVersion = _MadgeConfigBCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 6),
    _MadgeConfigBCodeVersion_Type()
)
madgeConfigBCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeConfigBCodeVersion.setStatus("mandatory")
_MadgeConfigMCodeFilename_Type = DisplayString
_MadgeConfigMCodeFilename_Object = MibScalar
madgeConfigMCodeFilename = _MadgeConfigMCodeFilename_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 7),
    _MadgeConfigMCodeFilename_Type()
)
madgeConfigMCodeFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeConfigMCodeFilename.setStatus("mandatory")


class _MadgeConfigDeviceHealth_Type(Integer32):
    """Custom type madgeConfigDeviceHealth based on Integer32"""
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
        *(("critical", 4),
          ("degraded", 3),
          ("normal", 1),
          ("warning", 2))
    )


_MadgeConfigDeviceHealth_Type.__name__ = "Integer32"
_MadgeConfigDeviceHealth_Object = MibScalar
madgeConfigDeviceHealth = _MadgeConfigDeviceHealth_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 8),
    _MadgeConfigDeviceHealth_Type()
)
madgeConfigDeviceHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeConfigDeviceHealth.setStatus("mandatory")


class _MadgeConfigAdminStatus_Type(Integer32):
    """Custom type madgeConfigAdminStatus based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("erase-config", 5),
          ("erase-flash", 6),
          ("halt", 11),
          ("identify", 3),
          ("normal", 1),
          ("reboot", 2),
          ("rpl-ipx", 9),
          ("rpl-llc", 10),
          ("snapshot", 14),
          ("test", 4),
          ("tftp-ip", 7),
          ("tftp-ipx", 8),
          ("up-tftp-ip", 12),
          ("up-tftp-ipx", 13))
    )


_MadgeConfigAdminStatus_Type.__name__ = "Integer32"
_MadgeConfigAdminStatus_Object = MibScalar
madgeConfigAdminStatus = _MadgeConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 9),
    _MadgeConfigAdminStatus_Type()
)
madgeConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigAdminStatus.setStatus("mandatory")


class _MadgeConfigPassword_Type(DisplayString):
    """Custom type madgeConfigPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MadgeConfigPassword_Type.__name__ = "DisplayString"
_MadgeConfigPassword_Object = MibScalar
madgeConfigPassword = _MadgeConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 10),
    _MadgeConfigPassword_Type()
)
madgeConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigPassword.setStatus("mandatory")
_MadgeConfigLinkTest_Type = Integer32
_MadgeConfigLinkTest_Object = MibScalar
madgeConfigLinkTest = _MadgeConfigLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 11),
    _MadgeConfigLinkTest_Type()
)
madgeConfigLinkTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigLinkTest.setStatus("mandatory")


class _MadgeConfigOperStatus_Type(Integer32):
    """Custom type madgeConfigOperStatus based on Integer32"""
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
        *(("downloading", 5),
          ("identify", 3),
          ("normal", 1),
          ("reboot", 2),
          ("test", 4),
          ("uploading", 6))
    )


_MadgeConfigOperStatus_Type.__name__ = "Integer32"
_MadgeConfigOperStatus_Object = MibScalar
madgeConfigOperStatus = _MadgeConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 12),
    _MadgeConfigOperStatus_Type()
)
madgeConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeConfigOperStatus.setStatus("mandatory")
_MadgeConfigEraseFlashVersion_Type = Integer32
_MadgeConfigEraseFlashVersion_Object = MibScalar
madgeConfigEraseFlashVersion = _MadgeConfigEraseFlashVersion_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 13),
    _MadgeConfigEraseFlashVersion_Type()
)
madgeConfigEraseFlashVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigEraseFlashVersion.setStatus("mandatory")
_MadgeConfigDefaultFlashVersion_Type = Integer32
_MadgeConfigDefaultFlashVersion_Object = MibScalar
madgeConfigDefaultFlashVersion = _MadgeConfigDefaultFlashVersion_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 14),
    _MadgeConfigDefaultFlashVersion_Type()
)
madgeConfigDefaultFlashVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigDefaultFlashVersion.setStatus("mandatory")


class _MadgeConfigReadPassword_Type(DisplayString):
    """Custom type madgeConfigReadPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MadgeConfigReadPassword_Type.__name__ = "DisplayString"
_MadgeConfigReadPassword_Object = MibScalar
madgeConfigReadPassword = _MadgeConfigReadPassword_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 15),
    _MadgeConfigReadPassword_Type()
)
madgeConfigReadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigReadPassword.setStatus("optional")
_MadgeConfigSnapshotName_Type = DisplayString
_MadgeConfigSnapshotName_Object = MibScalar
madgeConfigSnapshotName = _MadgeConfigSnapshotName_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 16),
    _MadgeConfigSnapshotName_Type()
)
madgeConfigSnapshotName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigSnapshotName.setStatus("mandatory")
_MadgeConfigDefaultSnapshot_Type = Integer32
_MadgeConfigDefaultSnapshot_Object = MibScalar
madgeConfigDefaultSnapshot = _MadgeConfigDefaultSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 17),
    _MadgeConfigDefaultSnapshot_Type()
)
madgeConfigDefaultSnapshot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigDefaultSnapshot.setStatus("mandatory")
_MadgeConfigPasswordTableSize_Type = Integer32
_MadgeConfigPasswordTableSize_Object = MibScalar
madgeConfigPasswordTableSize = _MadgeConfigPasswordTableSize_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 20),
    _MadgeConfigPasswordTableSize_Type()
)
madgeConfigPasswordTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeConfigPasswordTableSize.setStatus("mandatory")
_MadgeConfigPasswordTable_Object = MibTable
madgeConfigPasswordTable = _MadgeConfigPasswordTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 21)
)
if mibBuilder.loadTexts:
    madgeConfigPasswordTable.setStatus("mandatory")
_MadgeConfigPasswordEntry_Object = MibTableRow
madgeConfigPasswordEntry = _MadgeConfigPasswordEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 21, 1)
)
madgeConfigPasswordEntry.setIndexNames(
    (0, "MADGEBOX-MIB", "madgeConfigPasswordIndex"),
)
if mibBuilder.loadTexts:
    madgeConfigPasswordEntry.setStatus("mandatory")
_MadgeConfigPasswordIndex_Type = Integer32
_MadgeConfigPasswordIndex_Object = MibTableColumn
madgeConfigPasswordIndex = _MadgeConfigPasswordIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 21, 1, 1),
    _MadgeConfigPasswordIndex_Type()
)
madgeConfigPasswordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeConfigPasswordIndex.setStatus("mandatory")


class _MadgeConfigPasswordRead_Type(DisplayString):
    """Custom type madgeConfigPasswordRead based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MadgeConfigPasswordRead_Type.__name__ = "DisplayString"
_MadgeConfigPasswordRead_Object = MibTableColumn
madgeConfigPasswordRead = _MadgeConfigPasswordRead_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 21, 1, 2),
    _MadgeConfigPasswordRead_Type()
)
madgeConfigPasswordRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigPasswordRead.setStatus("mandatory")


class _MadgeConfigPasswordWrite_Type(DisplayString):
    """Custom type madgeConfigPasswordWrite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MadgeConfigPasswordWrite_Type.__name__ = "DisplayString"
_MadgeConfigPasswordWrite_Object = MibTableColumn
madgeConfigPasswordWrite = _MadgeConfigPasswordWrite_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 21, 1, 3),
    _MadgeConfigPasswordWrite_Type()
)
madgeConfigPasswordWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigPasswordWrite.setStatus("mandatory")


class _MadgeConfigPasswordComment_Type(DisplayString):
    """Custom type madgeConfigPasswordComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MadgeConfigPasswordComment_Type.__name__ = "DisplayString"
_MadgeConfigPasswordComment_Object = MibTableColumn
madgeConfigPasswordComment = _MadgeConfigPasswordComment_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 1, 21, 1, 4),
    _MadgeConfigPasswordComment_Type()
)
madgeConfigPasswordComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeConfigPasswordComment.setStatus("mandatory")
_MadgeSecure_ObjectIdentity = ObjectIdentity
madgeSecure = _MadgeSecure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 10, 2)
)
_MadgeSecureCurrentTableSize_Type = Integer32
_MadgeSecureCurrentTableSize_Object = MibScalar
madgeSecureCurrentTableSize = _MadgeSecureCurrentTableSize_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 1),
    _MadgeSecureCurrentTableSize_Type()
)
madgeSecureCurrentTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeSecureCurrentTableSize.setStatus("mandatory")
_MadgeSecureCurrentTimeout_Type = Integer32
_MadgeSecureCurrentTimeout_Object = MibScalar
madgeSecureCurrentTimeout = _MadgeSecureCurrentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 2),
    _MadgeSecureCurrentTimeout_Type()
)
madgeSecureCurrentTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeSecureCurrentTimeout.setStatus("mandatory")
_MadgeSecureCurrentTable_Object = MibTable
madgeSecureCurrentTable = _MadgeSecureCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 3)
)
if mibBuilder.loadTexts:
    madgeSecureCurrentTable.setStatus("mandatory")
_MadgeSecureCurrentEntry_Object = MibTableRow
madgeSecureCurrentEntry = _MadgeSecureCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 3, 1)
)
madgeSecureCurrentEntry.setIndexNames(
    (0, "MADGEBOX-MIB", "madgeSecureCurrentIndex"),
)
if mibBuilder.loadTexts:
    madgeSecureCurrentEntry.setStatus("mandatory")
_MadgeSecureCurrentIndex_Type = Integer32
_MadgeSecureCurrentIndex_Object = MibTableColumn
madgeSecureCurrentIndex = _MadgeSecureCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 3, 1, 1),
    _MadgeSecureCurrentIndex_Type()
)
madgeSecureCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeSecureCurrentIndex.setStatus("mandatory")


class _MadgeSecureCurrentType_Type(Integer32):
    """Custom type madgeSecureCurrentType based on Integer32"""
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
        *(("ip-address", 2),
          ("ipx-address", 3),
          ("mac-address", 4),
          ("not-used", 1))
    )


_MadgeSecureCurrentType_Type.__name__ = "Integer32"
_MadgeSecureCurrentType_Object = MibTableColumn
madgeSecureCurrentType = _MadgeSecureCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 3, 1, 2),
    _MadgeSecureCurrentType_Type()
)
madgeSecureCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeSecureCurrentType.setStatus("mandatory")
_MadgeSecureCurrentAddress_Type = OctetString
_MadgeSecureCurrentAddress_Object = MibTableColumn
madgeSecureCurrentAddress = _MadgeSecureCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 3, 1, 3),
    _MadgeSecureCurrentAddress_Type()
)
madgeSecureCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeSecureCurrentAddress.setStatus("mandatory")
_MadgeSecureCurrentUpdateTime_Type = Integer32
_MadgeSecureCurrentUpdateTime_Object = MibTableColumn
madgeSecureCurrentUpdateTime = _MadgeSecureCurrentUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 3, 1, 4),
    _MadgeSecureCurrentUpdateTime_Type()
)
madgeSecureCurrentUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeSecureCurrentUpdateTime.setStatus("mandatory")
_MadgeSecureCurrentIPAddress_Type = IpAddress
_MadgeSecureCurrentIPAddress_Object = MibTableColumn
madgeSecureCurrentIPAddress = _MadgeSecureCurrentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 3, 1, 5),
    _MadgeSecureCurrentIPAddress_Type()
)
madgeSecureCurrentIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeSecureCurrentIPAddress.setStatus("mandatory")


class _MadgeSecureAllowedEnabled_Type(Integer32):
    """Custom type madgeSecureAllowedEnabled based on Integer32"""
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


_MadgeSecureAllowedEnabled_Type.__name__ = "Integer32"
_MadgeSecureAllowedEnabled_Object = MibScalar
madgeSecureAllowedEnabled = _MadgeSecureAllowedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 4),
    _MadgeSecureAllowedEnabled_Type()
)
madgeSecureAllowedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeSecureAllowedEnabled.setStatus("mandatory")
_MadgeSecureAllowedTableSize_Type = Integer32
_MadgeSecureAllowedTableSize_Object = MibScalar
madgeSecureAllowedTableSize = _MadgeSecureAllowedTableSize_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 5),
    _MadgeSecureAllowedTableSize_Type()
)
madgeSecureAllowedTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeSecureAllowedTableSize.setStatus("mandatory")
_MadgeSecureAllowedTable_Object = MibTable
madgeSecureAllowedTable = _MadgeSecureAllowedTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 6)
)
if mibBuilder.loadTexts:
    madgeSecureAllowedTable.setStatus("mandatory")
_MadgeSecureAllowedEntry_Object = MibTableRow
madgeSecureAllowedEntry = _MadgeSecureAllowedEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 6, 1)
)
madgeSecureAllowedEntry.setIndexNames(
    (0, "MADGEBOX-MIB", "madgeSecureAllowedIndex"),
)
if mibBuilder.loadTexts:
    madgeSecureAllowedEntry.setStatus("mandatory")
_MadgeSecureAllowedIndex_Type = Integer32
_MadgeSecureAllowedIndex_Object = MibTableColumn
madgeSecureAllowedIndex = _MadgeSecureAllowedIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 6, 1, 1),
    _MadgeSecureAllowedIndex_Type()
)
madgeSecureAllowedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeSecureAllowedIndex.setStatus("mandatory")


class _MadgeSecureAllowedType_Type(Integer32):
    """Custom type madgeSecureAllowedType based on Integer32"""
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
        *(("ip-address", 2),
          ("ipx-address", 3),
          ("mac-address", 4),
          ("not-used", 1))
    )


_MadgeSecureAllowedType_Type.__name__ = "Integer32"
_MadgeSecureAllowedType_Object = MibTableColumn
madgeSecureAllowedType = _MadgeSecureAllowedType_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 6, 1, 2),
    _MadgeSecureAllowedType_Type()
)
madgeSecureAllowedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeSecureAllowedType.setStatus("mandatory")
_MadgeSecureAllowedAddress_Type = OctetString
_MadgeSecureAllowedAddress_Object = MibTableColumn
madgeSecureAllowedAddress = _MadgeSecureAllowedAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 6, 1, 3),
    _MadgeSecureAllowedAddress_Type()
)
madgeSecureAllowedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeSecureAllowedAddress.setStatus("mandatory")
_MadgeSecureAllowedIPAddress_Type = IpAddress
_MadgeSecureAllowedIPAddress_Object = MibTableColumn
madgeSecureAllowedIPAddress = _MadgeSecureAllowedIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 6, 1, 4),
    _MadgeSecureAllowedIPAddress_Type()
)
madgeSecureAllowedIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeSecureAllowedIPAddress.setStatus("mandatory")


class _MadgeSecureTrapDestEnabled_Type(Integer32):
    """Custom type madgeSecureTrapDestEnabled based on Integer32"""
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


_MadgeSecureTrapDestEnabled_Type.__name__ = "Integer32"
_MadgeSecureTrapDestEnabled_Object = MibScalar
madgeSecureTrapDestEnabled = _MadgeSecureTrapDestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 7),
    _MadgeSecureTrapDestEnabled_Type()
)
madgeSecureTrapDestEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeSecureTrapDestEnabled.setStatus("mandatory")
_MadgeSecureTrapDestTableSize_Type = Integer32
_MadgeSecureTrapDestTableSize_Object = MibScalar
madgeSecureTrapDestTableSize = _MadgeSecureTrapDestTableSize_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 8),
    _MadgeSecureTrapDestTableSize_Type()
)
madgeSecureTrapDestTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeSecureTrapDestTableSize.setStatus("mandatory")
_MadgeSecureTrapDestTable_Object = MibTable
madgeSecureTrapDestTable = _MadgeSecureTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 9)
)
if mibBuilder.loadTexts:
    madgeSecureTrapDestTable.setStatus("mandatory")
_MadgeSecureTrapDestEntry_Object = MibTableRow
madgeSecureTrapDestEntry = _MadgeSecureTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 9, 1)
)
madgeSecureTrapDestEntry.setIndexNames(
    (0, "MADGEBOX-MIB", "madgeSecureTrapDestIndex"),
)
if mibBuilder.loadTexts:
    madgeSecureTrapDestEntry.setStatus("mandatory")
_MadgeSecureTrapDestIndex_Type = Integer32
_MadgeSecureTrapDestIndex_Object = MibTableColumn
madgeSecureTrapDestIndex = _MadgeSecureTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 9, 1, 1),
    _MadgeSecureTrapDestIndex_Type()
)
madgeSecureTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeSecureTrapDestIndex.setStatus("mandatory")


class _MadgeSecureTrapDestType_Type(Integer32):
    """Custom type madgeSecureTrapDestType based on Integer32"""
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
        *(("ip-address", 2),
          ("ipx-address", 3),
          ("mac-address", 4),
          ("not-used", 1))
    )


_MadgeSecureTrapDestType_Type.__name__ = "Integer32"
_MadgeSecureTrapDestType_Object = MibTableColumn
madgeSecureTrapDestType = _MadgeSecureTrapDestType_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 9, 1, 2),
    _MadgeSecureTrapDestType_Type()
)
madgeSecureTrapDestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeSecureTrapDestType.setStatus("mandatory")
_MadgeSecureTrapDestAddress_Type = OctetString
_MadgeSecureTrapDestAddress_Object = MibTableColumn
madgeSecureTrapDestAddress = _MadgeSecureTrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 9, 1, 3),
    _MadgeSecureTrapDestAddress_Type()
)
madgeSecureTrapDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeSecureTrapDestAddress.setStatus("mandatory")
_MadgeSecureTrapDestIPAddress_Type = IpAddress
_MadgeSecureTrapDestIPAddress_Object = MibTableColumn
madgeSecureTrapDestIPAddress = _MadgeSecureTrapDestIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 2, 9, 1, 4),
    _MadgeSecureTrapDestIPAddress_Type()
)
madgeSecureTrapDestIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeSecureTrapDestIPAddress.setStatus("mandatory")
_MadgeDownload_ObjectIdentity = ObjectIdentity
madgeDownload = _MadgeDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 10, 3)
)
_MadgeDownloadIPAddress_Type = IpAddress
_MadgeDownloadIPAddress_Object = MibScalar
madgeDownloadIPAddress = _MadgeDownloadIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 3, 1),
    _MadgeDownloadIPAddress_Type()
)
madgeDownloadIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeDownloadIPAddress.setStatus("mandatory")
_MadgeDownloadIPGateway_Type = IpAddress
_MadgeDownloadIPGateway_Object = MibScalar
madgeDownloadIPGateway = _MadgeDownloadIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 3, 2),
    _MadgeDownloadIPGateway_Type()
)
madgeDownloadIPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeDownloadIPGateway.setStatus("mandatory")


class _MadgeDownloadIPXAddress_Type(OctetString):
    """Custom type madgeDownloadIPXAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_MadgeDownloadIPXAddress_Type.__name__ = "OctetString"
_MadgeDownloadIPXAddress_Object = MibScalar
madgeDownloadIPXAddress = _MadgeDownloadIPXAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 3, 3),
    _MadgeDownloadIPXAddress_Type()
)
madgeDownloadIPXAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeDownloadIPXAddress.setStatus("mandatory")
_MadgeDownloadNodeAddress_Type = MacAddress
_MadgeDownloadNodeAddress_Object = MibScalar
madgeDownloadNodeAddress = _MadgeDownloadNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 3, 4),
    _MadgeDownloadNodeAddress_Type()
)
madgeDownloadNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeDownloadNodeAddress.setStatus("mandatory")
_MadgeDownloadFileName_Type = DisplayString
_MadgeDownloadFileName_Object = MibScalar
madgeDownloadFileName = _MadgeDownloadFileName_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 3, 5),
    _MadgeDownloadFileName_Type()
)
madgeDownloadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeDownloadFileName.setStatus("mandatory")
_MadgeDownloadDestination_Type = Integer32
_MadgeDownloadDestination_Object = MibScalar
madgeDownloadDestination = _MadgeDownloadDestination_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 3, 6),
    _MadgeDownloadDestination_Type()
)
madgeDownloadDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeDownloadDestination.setStatus("mandatory")


class _MadgeDownloadState_Type(Integer32):
    """Custom type madgeDownloadState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("rpl-running-ipx", 9),
          ("rpl-running-llc", 11),
          ("rpl-waiting-ipx", 8),
          ("rpl-waiting-llc", 10),
          ("running-xmodem", 7),
          ("tftp-running-ip", 3),
          ("tftp-running-ipx", 5),
          ("tftp-waiting-ip", 2),
          ("tftp-waiting-ipx", 4),
          ("waiting-xmodem", 6))
    )


_MadgeDownloadState_Type.__name__ = "Integer32"
_MadgeDownloadState_Object = MibScalar
madgeDownloadState = _MadgeDownloadState_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 3, 7),
    _MadgeDownloadState_Type()
)
madgeDownloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeDownloadState.setStatus("mandatory")


class _MadgeDownloadFailureCode_Type(Integer32):
    """Custom type madgeDownloadFailureCode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107)
        )
    )
    namedValues = NamedValues(
        *(("access-violation", 102),
          ("busy", 3),
          ("cancelled", 5),
          ("config-error", 2),
          ("file-already-exists", 106),
          ("file-not-found", 101),
          ("file-too-big", 7),
          ("flash-write-error", 9),
          ("illegal-operation", 104),
          ("incompatible-file", 6),
          ("no-error", 1),
          ("no-such-user", 107),
          ("out-of-memory", 103),
          ("protocol-error", 8),
          ("timeout", 4),
          ("undefined-error", 100),
          ("unknown-transfer-id", 105))
    )


_MadgeDownloadFailureCode_Type.__name__ = "Integer32"
_MadgeDownloadFailureCode_Object = MibScalar
madgeDownloadFailureCode = _MadgeDownloadFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 3, 8),
    _MadgeDownloadFailureCode_Type()
)
madgeDownloadFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeDownloadFailureCode.setStatus("mandatory")


class _MadgeDownloadStatusText_Type(DisplayString):
    """Custom type madgeDownloadStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MadgeDownloadStatusText_Type.__name__ = "DisplayString"
_MadgeDownloadStatusText_Object = MibScalar
madgeDownloadStatusText = _MadgeDownloadStatusText_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 3, 9),
    _MadgeDownloadStatusText_Type()
)
madgeDownloadStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeDownloadStatusText.setStatus("mandatory")
_MadgeDownloadSize_Type = Integer32
_MadgeDownloadSize_Object = MibScalar
madgeDownloadSize = _MadgeDownloadSize_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 3, 10),
    _MadgeDownloadSize_Type()
)
madgeDownloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeDownloadSize.setStatus("mandatory")
_MadgeIP_ObjectIdentity = ObjectIdentity
madgeIP = _MadgeIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 10, 4)
)
_MadgeIPCurrentAddress_Type = IpAddress
_MadgeIPCurrentAddress_Object = MibScalar
madgeIPCurrentAddress = _MadgeIPCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 4, 1),
    _MadgeIPCurrentAddress_Type()
)
madgeIPCurrentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeIPCurrentAddress.setStatus("mandatory")
_MadgeIPCurrentGateway_Type = IpAddress
_MadgeIPCurrentGateway_Object = MibScalar
madgeIPCurrentGateway = _MadgeIPCurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 4, 2),
    _MadgeIPCurrentGateway_Type()
)
madgeIPCurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeIPCurrentGateway.setStatus("mandatory")
_MadgeIPCurrentSubnetMask_Type = IpAddress
_MadgeIPCurrentSubnetMask_Object = MibScalar
madgeIPCurrentSubnetMask = _MadgeIPCurrentSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 4, 3),
    _MadgeIPCurrentSubnetMask_Type()
)
madgeIPCurrentSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeIPCurrentSubnetMask.setStatus("mandatory")


class _MadgeIPDiscoveryMethod_Type(Integer32):
    """Custom type madgeIPDiscoveryMethod based on Integer32"""
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
        *(("not-discovered", 1),
          ("via-bootp", 3),
          ("via-config", 2),
          ("via-dhcp", 5),
          ("via-rarp", 4))
    )


_MadgeIPDiscoveryMethod_Type.__name__ = "Integer32"
_MadgeIPDiscoveryMethod_Object = MibScalar
madgeIPDiscoveryMethod = _MadgeIPDiscoveryMethod_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 4, 4),
    _MadgeIPDiscoveryMethod_Type()
)
madgeIPDiscoveryMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeIPDiscoveryMethod.setStatus("mandatory")


class _MadgeIPBootpEnabled_Type(Integer32):
    """Custom type madgeIPBootpEnabled based on Integer32"""
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
          ("enabled", 1),
          ("not-supported", 3))
    )


_MadgeIPBootpEnabled_Type.__name__ = "Integer32"
_MadgeIPBootpEnabled_Object = MibScalar
madgeIPBootpEnabled = _MadgeIPBootpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 4, 5),
    _MadgeIPBootpEnabled_Type()
)
madgeIPBootpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeIPBootpEnabled.setStatus("mandatory")


class _MadgeIPRarpEnabled_Type(Integer32):
    """Custom type madgeIPRarpEnabled based on Integer32"""
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
          ("enabled", 1),
          ("not-supported", 3))
    )


_MadgeIPRarpEnabled_Type.__name__ = "Integer32"
_MadgeIPRarpEnabled_Object = MibScalar
madgeIPRarpEnabled = _MadgeIPRarpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 4, 6),
    _MadgeIPRarpEnabled_Type()
)
madgeIPRarpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeIPRarpEnabled.setStatus("mandatory")


class _MadgeIPDHCPEnabled_Type(Integer32):
    """Custom type madgeIPDHCPEnabled based on Integer32"""
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
          ("enabled", 1),
          ("not-supported", 3))
    )


_MadgeIPDHCPEnabled_Type.__name__ = "Integer32"
_MadgeIPDHCPEnabled_Object = MibScalar
madgeIPDHCPEnabled = _MadgeIPDHCPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 4, 7),
    _MadgeIPDHCPEnabled_Type()
)
madgeIPDHCPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeIPDHCPEnabled.setStatus("mandatory")
_MadgeVersion_ObjectIdentity = ObjectIdentity
madgeVersion = _MadgeVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 10, 5)
)
_MadgeVersionTable_Object = MibTable
madgeVersionTable = _MadgeVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 5, 1)
)
if mibBuilder.loadTexts:
    madgeVersionTable.setStatus("mandatory")
_MadgeVersionEntry_Object = MibTableRow
madgeVersionEntry = _MadgeVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 5, 1, 1)
)
madgeVersionEntry.setIndexNames(
    (0, "MADGEBOX-MIB", "madgeVersionIndex"),
)
if mibBuilder.loadTexts:
    madgeVersionEntry.setStatus("mandatory")
_MadgeVersionIndex_Type = Integer32
_MadgeVersionIndex_Object = MibTableColumn
madgeVersionIndex = _MadgeVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 5, 1, 1, 1),
    _MadgeVersionIndex_Type()
)
madgeVersionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    madgeVersionIndex.setStatus("mandatory")


class _MadgeVersionDescription_Type(DisplayString):
    """Custom type madgeVersionDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MadgeVersionDescription_Type.__name__ = "DisplayString"
_MadgeVersionDescription_Object = MibTableColumn
madgeVersionDescription = _MadgeVersionDescription_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 5, 1, 1, 2),
    _MadgeVersionDescription_Type()
)
madgeVersionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeVersionDescription.setStatus("mandatory")


class _MadgeVersionLocation_Type(DisplayString):
    """Custom type madgeVersionLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MadgeVersionLocation_Type.__name__ = "DisplayString"
_MadgeVersionLocation_Object = MibTableColumn
madgeVersionLocation = _MadgeVersionLocation_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 5, 1, 1, 3),
    _MadgeVersionLocation_Type()
)
madgeVersionLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeVersionLocation.setStatus("mandatory")


class _MadgeVersionNumber_Type(OctetString):
    """Custom type madgeVersionNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_MadgeVersionNumber_Type.__name__ = "OctetString"
_MadgeVersionNumber_Object = MibTableColumn
madgeVersionNumber = _MadgeVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 5, 1, 1, 4),
    _MadgeVersionNumber_Type()
)
madgeVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeVersionNumber.setStatus("mandatory")


class _MadgeVersionType_Type(Integer32):
    """Custom type madgeVersionType based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("boot-fixed", 2),
          ("boot-updateable", 3),
          ("flash", 1),
          ("hardware-fixed", 4),
          ("hardware-upgradeable", 5),
          ("other", 6),
          ("sw-config", 8),
          ("sw-image", 9),
          ("sw-running", 7),
          ("unknown", 20))
    )


_MadgeVersionType_Type.__name__ = "Integer32"
_MadgeVersionType_Object = MibTableColumn
madgeVersionType = _MadgeVersionType_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 5, 1, 1, 5),
    _MadgeVersionType_Type()
)
madgeVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeVersionType.setStatus("mandatory")
_MadgeVersionCount_Type = Integer32
_MadgeVersionCount_Object = MibScalar
madgeVersionCount = _MadgeVersionCount_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 5, 2),
    _MadgeVersionCount_Type()
)
madgeVersionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeVersionCount.setStatus("mandatory")
_MadgeTrap_ObjectIdentity = ObjectIdentity
madgeTrap = _MadgeTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 10, 6)
)
_MadgeTrapTable_Object = MibTable
madgeTrapTable = _MadgeTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 1)
)
if mibBuilder.loadTexts:
    madgeTrapTable.setStatus("mandatory")
_MadgeTrapEntry_Object = MibTableRow
madgeTrapEntry = _MadgeTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 1, 1)
)
madgeTrapEntry.setIndexNames(
    (0, "MADGEBOX-MIB", "madgeTrapIndex"),
)
if mibBuilder.loadTexts:
    madgeTrapEntry.setStatus("mandatory")
_MadgeTrapIndex_Type = Integer32
_MadgeTrapIndex_Object = MibTableColumn
madgeTrapIndex = _MadgeTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 1, 1, 1),
    _MadgeTrapIndex_Type()
)
madgeTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    madgeTrapIndex.setStatus("mandatory")


class _MadgeTrapDescription_Type(DisplayString):
    """Custom type madgeTrapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MadgeTrapDescription_Type.__name__ = "DisplayString"
_MadgeTrapDescription_Object = MibTableColumn
madgeTrapDescription = _MadgeTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 1, 1, 2),
    _MadgeTrapDescription_Type()
)
madgeTrapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeTrapDescription.setStatus("mandatory")
_MadgeTrapEnterprise_Type = ObjectIdentifier
_MadgeTrapEnterprise_Object = MibTableColumn
madgeTrapEnterprise = _MadgeTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 1, 1, 3),
    _MadgeTrapEnterprise_Type()
)
madgeTrapEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeTrapEnterprise.setStatus("mandatory")
_MadgeTrapSpecificTrap_Type = Integer32
_MadgeTrapSpecificTrap_Object = MibTableColumn
madgeTrapSpecificTrap = _MadgeTrapSpecificTrap_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 1, 1, 4),
    _MadgeTrapSpecificTrap_Type()
)
madgeTrapSpecificTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeTrapSpecificTrap.setStatus("mandatory")


class _MadgeTrapSeverity_Type(Integer32):
    """Custom type madgeTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("informational", 6),
          ("major", 3),
          ("minor", 4),
          ("unknown", 1),
          ("warning", 5))
    )


_MadgeTrapSeverity_Type.__name__ = "Integer32"
_MadgeTrapSeverity_Object = MibTableColumn
madgeTrapSeverity = _MadgeTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 1, 1, 5),
    _MadgeTrapSeverity_Type()
)
madgeTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeTrapSeverity.setStatus("mandatory")


class _MadgeTrapEnable_Type(Integer32):
    """Custom type madgeTrapEnable based on Integer32"""
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


_MadgeTrapEnable_Type.__name__ = "Integer32"
_MadgeTrapEnable_Object = MibTableColumn
madgeTrapEnable = _MadgeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 1, 1, 6),
    _MadgeTrapEnable_Type()
)
madgeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeTrapEnable.setStatus("mandatory")


class _MadgeTrapEnableDefault_Type(Integer32):
    """Custom type madgeTrapEnableDefault based on Integer32"""
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


_MadgeTrapEnableDefault_Type.__name__ = "Integer32"
_MadgeTrapEnableDefault_Object = MibTableColumn
madgeTrapEnableDefault = _MadgeTrapEnableDefault_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 1, 1, 7),
    _MadgeTrapEnableDefault_Type()
)
madgeTrapEnableDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeTrapEnableDefault.setStatus("mandatory")
_MadgeTrapCounter_Type = Integer32
_MadgeTrapCounter_Object = MibTableColumn
madgeTrapCounter = _MadgeTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 1, 1, 8),
    _MadgeTrapCounter_Type()
)
madgeTrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeTrapCounter.setStatus("mandatory")


class _MadgeTrapEnableAll_Type(Integer32):
    """Custom type madgeTrapEnableAll based on Integer32"""
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


_MadgeTrapEnableAll_Type.__name__ = "Integer32"
_MadgeTrapEnableAll_Object = MibScalar
madgeTrapEnableAll = _MadgeTrapEnableAll_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 2),
    _MadgeTrapEnableAll_Type()
)
madgeTrapEnableAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeTrapEnableAll.setStatus("mandatory")


class _MadgeTrapResetCounters_Type(Integer32):
    """Custom type madgeTrapResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2),
          ("resetting", 3))
    )


_MadgeTrapResetCounters_Type.__name__ = "Integer32"
_MadgeTrapResetCounters_Object = MibScalar
madgeTrapResetCounters = _MadgeTrapResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 3),
    _MadgeTrapResetCounters_Type()
)
madgeTrapResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeTrapResetCounters.setStatus("mandatory")


class _MadgeTrapDefaultAll_Type(Integer32):
    """Custom type madgeTrapDefaultAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2),
          ("resetting", 3))
    )


_MadgeTrapDefaultAll_Type.__name__ = "Integer32"
_MadgeTrapDefaultAll_Object = MibScalar
madgeTrapDefaultAll = _MadgeTrapDefaultAll_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 4),
    _MadgeTrapDefaultAll_Type()
)
madgeTrapDefaultAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeTrapDefaultAll.setStatus("mandatory")


class _MadgeTrapMessage_Type(DisplayString):
    """Custom type madgeTrapMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MadgeTrapMessage_Type.__name__ = "DisplayString"
_MadgeTrapMessage_Object = MibScalar
madgeTrapMessage = _MadgeTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 6, 5),
    _MadgeTrapMessage_Type()
)
madgeTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeTrapMessage.setStatus("optional")
_MadgeUpload_ObjectIdentity = ObjectIdentity
madgeUpload = _MadgeUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 10, 7)
)
_MadgeUploadIPAddress_Type = IpAddress
_MadgeUploadIPAddress_Object = MibScalar
madgeUploadIPAddress = _MadgeUploadIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 7, 1),
    _MadgeUploadIPAddress_Type()
)
madgeUploadIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeUploadIPAddress.setStatus("mandatory")
_MadgeUploadIPGateway_Type = IpAddress
_MadgeUploadIPGateway_Object = MibScalar
madgeUploadIPGateway = _MadgeUploadIPGateway_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 7, 2),
    _MadgeUploadIPGateway_Type()
)
madgeUploadIPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeUploadIPGateway.setStatus("mandatory")


class _MadgeUploadIPXAddress_Type(OctetString):
    """Custom type madgeUploadIPXAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_MadgeUploadIPXAddress_Type.__name__ = "OctetString"
_MadgeUploadIPXAddress_Object = MibScalar
madgeUploadIPXAddress = _MadgeUploadIPXAddress_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 7, 3),
    _MadgeUploadIPXAddress_Type()
)
madgeUploadIPXAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeUploadIPXAddress.setStatus("mandatory")
_MadgeUploadFileName_Type = DisplayString
_MadgeUploadFileName_Object = MibScalar
madgeUploadFileName = _MadgeUploadFileName_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 7, 4),
    _MadgeUploadFileName_Type()
)
madgeUploadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeUploadFileName.setStatus("mandatory")
_MadgeUploadSource_Type = Integer32
_MadgeUploadSource_Object = MibScalar
madgeUploadSource = _MadgeUploadSource_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 7, 5),
    _MadgeUploadSource_Type()
)
madgeUploadSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeUploadSource.setStatus("mandatory")


class _MadgeUploadState_Type(Integer32):
    """Custom type madgeUploadState based on Integer32"""
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
        *(("idle", 1),
          ("tftp-running-ip", 3),
          ("tftp-running-ipx", 5),
          ("tftp-waiting-ip", 2),
          ("tftp-waiting-ipx", 4))
    )


_MadgeUploadState_Type.__name__ = "Integer32"
_MadgeUploadState_Object = MibScalar
madgeUploadState = _MadgeUploadState_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 7, 6),
    _MadgeUploadState_Type()
)
madgeUploadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeUploadState.setStatus("mandatory")


class _MadgeUploadFailureCode_Type(Integer32):
    """Custom type madgeUploadFailureCode based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107)
        )
    )
    namedValues = NamedValues(
        *(("access-violation", 102),
          ("busy", 3),
          ("cancelled", 5),
          ("config-error", 2),
          ("file-already-exists", 106),
          ("file-not-found", 101),
          ("file-too-big", 7),
          ("flash-write-error", 9),
          ("illegal-operation", 104),
          ("incompatible-file", 6),
          ("no-error", 1),
          ("no-such-user", 107),
          ("out-of-memory", 103),
          ("protocol-error", 8),
          ("timeout", 4),
          ("undefined-error", 100),
          ("unknown-transfer-id", 105))
    )


_MadgeUploadFailureCode_Type.__name__ = "Integer32"
_MadgeUploadFailureCode_Object = MibScalar
madgeUploadFailureCode = _MadgeUploadFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 7, 7),
    _MadgeUploadFailureCode_Type()
)
madgeUploadFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeUploadFailureCode.setStatus("mandatory")


class _MadgeUploadStatusText_Type(DisplayString):
    """Custom type madgeUploadStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MadgeUploadStatusText_Type.__name__ = "DisplayString"
_MadgeUploadStatusText_Object = MibScalar
madgeUploadStatusText = _MadgeUploadStatusText_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 7, 8),
    _MadgeUploadStatusText_Type()
)
madgeUploadStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeUploadStatusText.setStatus("mandatory")
_MadgeUploadSize_Type = Integer32
_MadgeUploadSize_Object = MibScalar
madgeUploadSize = _MadgeUploadSize_Object(
    (1, 3, 6, 1, 4, 1, 494, 10, 7, 9),
    _MadgeUploadSize_Type()
)
madgeUploadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeUploadSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MADGEBOX-MIB",
    **{"DisplayString": DisplayString,
       "MacAddress": MacAddress,
       "madge": madge,
       "madgeBox": madgeBox,
       "madgeConfig": madgeConfig,
       "madgeConfigIPAddress": madgeConfigIPAddress,
       "madgeConfigIPGateway": madgeConfigIPGateway,
       "madgeConfigIPSubnetMask": madgeConfigIPSubnetMask,
       "madgeConfigSerialNumber": madgeConfigSerialNumber,
       "madgeConfigMCodeVersion": madgeConfigMCodeVersion,
       "madgeConfigBCodeVersion": madgeConfigBCodeVersion,
       "madgeConfigMCodeFilename": madgeConfigMCodeFilename,
       "madgeConfigDeviceHealth": madgeConfigDeviceHealth,
       "madgeConfigAdminStatus": madgeConfigAdminStatus,
       "madgeConfigPassword": madgeConfigPassword,
       "madgeConfigLinkTest": madgeConfigLinkTest,
       "madgeConfigOperStatus": madgeConfigOperStatus,
       "madgeConfigEraseFlashVersion": madgeConfigEraseFlashVersion,
       "madgeConfigDefaultFlashVersion": madgeConfigDefaultFlashVersion,
       "madgeConfigReadPassword": madgeConfigReadPassword,
       "madgeConfigSnapshotName": madgeConfigSnapshotName,
       "madgeConfigDefaultSnapshot": madgeConfigDefaultSnapshot,
       "madgeConfigPasswordTableSize": madgeConfigPasswordTableSize,
       "madgeConfigPasswordTable": madgeConfigPasswordTable,
       "madgeConfigPasswordEntry": madgeConfigPasswordEntry,
       "madgeConfigPasswordIndex": madgeConfigPasswordIndex,
       "madgeConfigPasswordRead": madgeConfigPasswordRead,
       "madgeConfigPasswordWrite": madgeConfigPasswordWrite,
       "madgeConfigPasswordComment": madgeConfigPasswordComment,
       "madgeSecure": madgeSecure,
       "madgeSecureCurrentTableSize": madgeSecureCurrentTableSize,
       "madgeSecureCurrentTimeout": madgeSecureCurrentTimeout,
       "madgeSecureCurrentTable": madgeSecureCurrentTable,
       "madgeSecureCurrentEntry": madgeSecureCurrentEntry,
       "madgeSecureCurrentIndex": madgeSecureCurrentIndex,
       "madgeSecureCurrentType": madgeSecureCurrentType,
       "madgeSecureCurrentAddress": madgeSecureCurrentAddress,
       "madgeSecureCurrentUpdateTime": madgeSecureCurrentUpdateTime,
       "madgeSecureCurrentIPAddress": madgeSecureCurrentIPAddress,
       "madgeSecureAllowedEnabled": madgeSecureAllowedEnabled,
       "madgeSecureAllowedTableSize": madgeSecureAllowedTableSize,
       "madgeSecureAllowedTable": madgeSecureAllowedTable,
       "madgeSecureAllowedEntry": madgeSecureAllowedEntry,
       "madgeSecureAllowedIndex": madgeSecureAllowedIndex,
       "madgeSecureAllowedType": madgeSecureAllowedType,
       "madgeSecureAllowedAddress": madgeSecureAllowedAddress,
       "madgeSecureAllowedIPAddress": madgeSecureAllowedIPAddress,
       "madgeSecureTrapDestEnabled": madgeSecureTrapDestEnabled,
       "madgeSecureTrapDestTableSize": madgeSecureTrapDestTableSize,
       "madgeSecureTrapDestTable": madgeSecureTrapDestTable,
       "madgeSecureTrapDestEntry": madgeSecureTrapDestEntry,
       "madgeSecureTrapDestIndex": madgeSecureTrapDestIndex,
       "madgeSecureTrapDestType": madgeSecureTrapDestType,
       "madgeSecureTrapDestAddress": madgeSecureTrapDestAddress,
       "madgeSecureTrapDestIPAddress": madgeSecureTrapDestIPAddress,
       "madgeDownload": madgeDownload,
       "madgeDownloadIPAddress": madgeDownloadIPAddress,
       "madgeDownloadIPGateway": madgeDownloadIPGateway,
       "madgeDownloadIPXAddress": madgeDownloadIPXAddress,
       "madgeDownloadNodeAddress": madgeDownloadNodeAddress,
       "madgeDownloadFileName": madgeDownloadFileName,
       "madgeDownloadDestination": madgeDownloadDestination,
       "madgeDownloadState": madgeDownloadState,
       "madgeDownloadFailureCode": madgeDownloadFailureCode,
       "madgeDownloadStatusText": madgeDownloadStatusText,
       "madgeDownloadSize": madgeDownloadSize,
       "madgeIP": madgeIP,
       "madgeIPCurrentAddress": madgeIPCurrentAddress,
       "madgeIPCurrentGateway": madgeIPCurrentGateway,
       "madgeIPCurrentSubnetMask": madgeIPCurrentSubnetMask,
       "madgeIPDiscoveryMethod": madgeIPDiscoveryMethod,
       "madgeIPBootpEnabled": madgeIPBootpEnabled,
       "madgeIPRarpEnabled": madgeIPRarpEnabled,
       "madgeIPDHCPEnabled": madgeIPDHCPEnabled,
       "madgeVersion": madgeVersion,
       "madgeVersionTable": madgeVersionTable,
       "madgeVersionEntry": madgeVersionEntry,
       "madgeVersionIndex": madgeVersionIndex,
       "madgeVersionDescription": madgeVersionDescription,
       "madgeVersionLocation": madgeVersionLocation,
       "madgeVersionNumber": madgeVersionNumber,
       "madgeVersionType": madgeVersionType,
       "madgeVersionCount": madgeVersionCount,
       "madgeTrap": madgeTrap,
       "madgeTrapTable": madgeTrapTable,
       "madgeTrapEntry": madgeTrapEntry,
       "madgeTrapIndex": madgeTrapIndex,
       "madgeTrapDescription": madgeTrapDescription,
       "madgeTrapEnterprise": madgeTrapEnterprise,
       "madgeTrapSpecificTrap": madgeTrapSpecificTrap,
       "madgeTrapSeverity": madgeTrapSeverity,
       "madgeTrapEnable": madgeTrapEnable,
       "madgeTrapEnableDefault": madgeTrapEnableDefault,
       "madgeTrapCounter": madgeTrapCounter,
       "madgeTrapEnableAll": madgeTrapEnableAll,
       "madgeTrapResetCounters": madgeTrapResetCounters,
       "madgeTrapDefaultAll": madgeTrapDefaultAll,
       "madgeTrapMessage": madgeTrapMessage,
       "madgeUpload": madgeUpload,
       "madgeUploadIPAddress": madgeUploadIPAddress,
       "madgeUploadIPGateway": madgeUploadIPGateway,
       "madgeUploadIPXAddress": madgeUploadIPXAddress,
       "madgeUploadFileName": madgeUploadFileName,
       "madgeUploadSource": madgeUploadSource,
       "madgeUploadState": madgeUploadState,
       "madgeUploadFailureCode": madgeUploadFailureCode,
       "madgeUploadStatusText": madgeUploadStatusText,
       "madgeUploadSize": madgeUploadSize}
)
