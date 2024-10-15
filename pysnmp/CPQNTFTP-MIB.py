# SNMP MIB module (CPQNTFTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQNTFTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:32 2024
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

(CpqnRowStatus,) = mibBuilder.importSymbols(
    "CPQNUNIF-MIB",
    "CpqnRowStatus")

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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_CpqnCommon_ObjectIdentity = ObjectIdentity
cpqnCommon = _CpqnCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 121)
)
_CpqnTftpConfig_ObjectIdentity = ObjectIdentity
cpqnTftpConfig = _CpqnTftpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 121, 9)
)


class _CpqnTftpInitiate_Type(Integer32):
    """Custom type cpqnTftpInitiate based on Integer32"""
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
        *(("initiate-transfer", 3),
          ("initiate-transfer-reset", 4),
          ("no-transfer-ipr", 1),
          ("transfer-in-progress", 2))
    )


_CpqnTftpInitiate_Type.__name__ = "Integer32"
_CpqnTftpInitiate_Object = MibScalar
cpqnTftpInitiate = _CpqnTftpInitiate_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 1),
    _CpqnTftpInitiate_Type()
)
cpqnTftpInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnTftpInitiate.setStatus("mandatory")


class _CpqnTftpCanDldAfterBoot_Type(Integer32):
    """Custom type cpqnTftpCanDldAfterBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("can-dld-after-boot", 1),
          ("cannot-dld-after-boot", 2))
    )


_CpqnTftpCanDldAfterBoot_Type.__name__ = "Integer32"
_CpqnTftpCanDldAfterBoot_Object = MibScalar
cpqnTftpCanDldAfterBoot = _CpqnTftpCanDldAfterBoot_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 2),
    _CpqnTftpCanDldAfterBoot_Type()
)
cpqnTftpCanDldAfterBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnTftpCanDldAfterBoot.setStatus("mandatory")


class _CpqnTftpCanSendTrap_Type(Integer32):
    """Custom type cpqnTftpCanSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("can-send-tftp-trap", 1),
          ("cannot-send-tftp-trap", 2))
    )


_CpqnTftpCanSendTrap_Type.__name__ = "Integer32"
_CpqnTftpCanSendTrap_Object = MibScalar
cpqnTftpCanSendTrap = _CpqnTftpCanSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 3),
    _CpqnTftpCanSendTrap_Type()
)
cpqnTftpCanSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnTftpCanSendTrap.setStatus("mandatory")


class _CpqnTftpTrapEnableStatus_Type(Integer32):
    """Custom type cpqnTftpTrapEnableStatus based on Integer32"""
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
        *(("cfg-file-traps", 4),
          ("disabled", 2),
          ("enabled", 1),
          ("os-file-traps", 3))
    )


_CpqnTftpTrapEnableStatus_Type.__name__ = "Integer32"
_CpqnTftpTrapEnableStatus_Object = MibScalar
cpqnTftpTrapEnableStatus = _CpqnTftpTrapEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 4),
    _CpqnTftpTrapEnableStatus_Type()
)
cpqnTftpTrapEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnTftpTrapEnableStatus.setStatus("mandatory")
_CpqnTftpTable_Object = MibTable
cpqnTftpTable = _CpqnTftpTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 5)
)
if mibBuilder.loadTexts:
    cpqnTftpTable.setStatus("mandatory")
_CpqnTftpEntry_Object = MibTableRow
cpqnTftpEntry = _CpqnTftpEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1)
)
cpqnTftpEntry.setIndexNames(
    (0, "CPQNTFTP-MIB", "cpqnTftpFileType"),
)
if mibBuilder.loadTexts:
    cpqnTftpEntry.setStatus("mandatory")


class _CpqnTftpFileType_Type(Integer32):
    """Custom type cpqnTftpFileType based on Integer32"""
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
        *(("agent", 6),
          ("atm-ulfw", 8),
          ("boot", 2),
          ("config", 5),
          ("entire-file", 1),
          ("fddi-ulfw", 7),
          ("run-time", 3),
          ("sblock-ext", 4))
    )


_CpqnTftpFileType_Type.__name__ = "Integer32"
_CpqnTftpFileType_Object = MibTableColumn
cpqnTftpFileType = _CpqnTftpFileType_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 1),
    _CpqnTftpFileType_Type()
)
cpqnTftpFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnTftpFileType.setStatus("mandatory")
_CpqnTftpRowStatus_Type = CpqnRowStatus
_CpqnTftpRowStatus_Object = MibTableColumn
cpqnTftpRowStatus = _CpqnTftpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 2),
    _CpqnTftpRowStatus_Type()
)
cpqnTftpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnTftpRowStatus.setStatus("mandatory")


class _CpqnTftpPathname_Type(DisplayString):
    """Custom type cpqnTftpPathname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CpqnTftpPathname_Type.__name__ = "DisplayString"
_CpqnTftpPathname_Object = MibTableColumn
cpqnTftpPathname = _CpqnTftpPathname_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 3),
    _CpqnTftpPathname_Type()
)
cpqnTftpPathname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnTftpPathname.setStatus("mandatory")
_CpqnTftpServerIp_Type = IpAddress
_CpqnTftpServerIp_Object = MibTableColumn
cpqnTftpServerIp = _CpqnTftpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 4),
    _CpqnTftpServerIp_Type()
)
cpqnTftpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnTftpServerIp.setStatus("mandatory")


class _CpqnNewFileVersion_Type(DisplayString):
    """Custom type cpqnNewFileVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 12),
    )


_CpqnNewFileVersion_Type.__name__ = "DisplayString"
_CpqnNewFileVersion_Object = MibTableColumn
cpqnNewFileVersion = _CpqnNewFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 5),
    _CpqnNewFileVersion_Type()
)
cpqnNewFileVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnNewFileVersion.setStatus("mandatory")


class _CpqnTftpTransferState_Type(Integer32):
    """Custom type cpqnTftpTransferState based on Integer32"""
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
        *(("download", 2),
          ("download-afterboot", 3),
          ("no-download-ipr", 1),
          ("upload-to-nms", 4))
    )


_CpqnTftpTransferState_Type.__name__ = "Integer32"
_CpqnTftpTransferState_Object = MibTableColumn
cpqnTftpTransferState = _CpqnTftpTransferState_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 6),
    _CpqnTftpTransferState_Type()
)
cpqnTftpTransferState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqnTftpTransferState.setStatus("mandatory")


class _CpqnTftpTransferLastErr_Type(Integer32):
    """Custom type cpqnTftpTransferLastErr based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("disk-full", 9),
          ("download-failed", 3),
          ("file-exists", 12),
          ("file-not-found", 7),
          ("hardware-error", 15),
          ("illegal-tftp-op", 10),
          ("invalid-access", 8),
          ("invalid-version", 14),
          ("no-error", 1),
          ("no-such-user", 13),
          ("route-not-found", 6),
          ("tftp-timeout", 5),
          ("transfer-in-progress", 2),
          ("unk-xfer-id", 11),
          ("upload-failed", 4))
    )


_CpqnTftpTransferLastErr_Type.__name__ = "Integer32"
_CpqnTftpTransferLastErr_Object = MibTableColumn
cpqnTftpTransferLastErr = _CpqnTftpTransferLastErr_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 7),
    _CpqnTftpTransferLastErr_Type()
)
cpqnTftpTransferLastErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnTftpTransferLastErr.setStatus("mandatory")
_CpqnTftpErrorText_Type = DisplayString
_CpqnTftpErrorText_Object = MibTableColumn
cpqnTftpErrorText = _CpqnTftpErrorText_Object(
    (1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 8),
    _CpqnTftpErrorText_Type()
)
cpqnTftpErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqnTftpErrorText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqnTftpTransferInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 121, 0, 1)
)
cpqnTftpTransferInitiated.setObjects(
      *(("CPQNTFTP-MIB", "cpqnTftpFileType"),
        ("CPQNTFTP-MIB", "cpqnTftpPathname"),
        ("CPQNTFTP-MIB", "cpqnTftpTransferState"))
)
if mibBuilder.loadTexts:
    cpqnTftpTransferInitiated.setStatus(
        ""
    )

cpqnTftpTransferCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 121, 0, 2)
)
cpqnTftpTransferCompleted.setObjects(
      *(("CPQNTFTP-MIB", "cpqnTftpFileType"),
        ("CPQNTFTP-MIB", "cpqnTftpPathname"),
        ("CPQNTFTP-MIB", "cpqnTftpTransferState"),
        ("CPQNTFTP-MIB", "cpqnTftpTransferLastErr"))
)
if mibBuilder.loadTexts:
    cpqnTftpTransferCompleted.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQNTFTP-MIB",
    **{"compaq": compaq,
       "cpqnCommon": cpqnCommon,
       "cpqnTftpTransferInitiated": cpqnTftpTransferInitiated,
       "cpqnTftpTransferCompleted": cpqnTftpTransferCompleted,
       "cpqnTftpConfig": cpqnTftpConfig,
       "cpqnTftpInitiate": cpqnTftpInitiate,
       "cpqnTftpCanDldAfterBoot": cpqnTftpCanDldAfterBoot,
       "cpqnTftpCanSendTrap": cpqnTftpCanSendTrap,
       "cpqnTftpTrapEnableStatus": cpqnTftpTrapEnableStatus,
       "cpqnTftpTable": cpqnTftpTable,
       "cpqnTftpEntry": cpqnTftpEntry,
       "cpqnTftpFileType": cpqnTftpFileType,
       "cpqnTftpRowStatus": cpqnTftpRowStatus,
       "cpqnTftpPathname": cpqnTftpPathname,
       "cpqnTftpServerIp": cpqnTftpServerIp,
       "cpqnNewFileVersion": cpqnNewFileVersion,
       "cpqnTftpTransferState": cpqnTftpTransferState,
       "cpqnTftpTransferLastErr": cpqnTftpTransferLastErr,
       "cpqnTftpErrorText": cpqnTftpErrorText}
)
