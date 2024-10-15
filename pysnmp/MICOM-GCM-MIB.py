# SNMP MIB module (MICOM-GCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-GCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:42 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

(mcmSysAsciiTimeOfDay,) = mibBuilder.importSymbols(
    "MICOM-SYS-MIB",
    "mcmSysAsciiTimeOfDay")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Micom_gcm_ObjectIdentity = ObjectIdentity
micom_gcm = _Micom_gcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25)
)
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1)
)
_McmGcmGlobalCfgGroup_ObjectIdentity = ObjectIdentity
mcmGcmGlobalCfgGroup = _McmGcmGlobalCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 1)
)


class _McmGcmGlobalCfgAdminStatus_Type(Integer32):
    """Custom type mcmGcmGlobalCfgAdminStatus based on Integer32"""
    defaultValue = 1

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


_McmGcmGlobalCfgAdminStatus_Type.__name__ = "Integer32"
_McmGcmGlobalCfgAdminStatus_Object = MibScalar
mcmGcmGlobalCfgAdminStatus = _McmGcmGlobalCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 1, 1),
    _McmGcmGlobalCfgAdminStatus_Type()
)
mcmGcmGlobalCfgAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmGlobalCfgAdminStatus.setStatus("mandatory")


class _McmGcmGlobalCfgTraps_Type(Integer32):
    """Custom type mcmGcmGlobalCfgTraps based on Integer32"""
    defaultValue = 2

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


_McmGcmGlobalCfgTraps_Type.__name__ = "Integer32"
_McmGcmGlobalCfgTraps_Object = MibScalar
mcmGcmGlobalCfgTraps = _McmGcmGlobalCfgTraps_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 1, 2),
    _McmGcmGlobalCfgTraps_Type()
)
mcmGcmGlobalCfgTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmGlobalCfgTraps.setStatus("mandatory")


class _McmGcmGlobalCfgAutoActSelMode_Type(Integer32):
    """Custom type mcmGcmGlobalCfgAutoActSelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("hwCfgAutoSelect", 1))
    )


_McmGcmGlobalCfgAutoActSelMode_Type.__name__ = "Integer32"
_McmGcmGlobalCfgAutoActSelMode_Object = MibScalar
mcmGcmGlobalCfgAutoActSelMode = _McmGcmGlobalCfgAutoActSelMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 1, 3),
    _McmGcmGlobalCfgAutoActSelMode_Type()
)
mcmGcmGlobalCfgAutoActSelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmGlobalCfgAutoActSelMode.setStatus("mandatory")
_McmGcmLinkTable_Object = MibTable
mcmGcmLinkTable = _McmGcmLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2)
)
if mibBuilder.loadTexts:
    mcmGcmLinkTable.setStatus("mandatory")
_McmGcmLinkEntry_Object = MibTableRow
mcmGcmLinkEntry = _McmGcmLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1)
)
mcmGcmLinkEntry.setIndexNames(
    (0, "MICOM-GCM-MIB", "mcmGcmLinkIndex"),
)
if mibBuilder.loadTexts:
    mcmGcmLinkEntry.setStatus("mandatory")


class _McmGcmLinkIndex_Type(Integer32):
    """Custom type mcmGcmLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmGcmLinkIndex_Type.__name__ = "Integer32"
_McmGcmLinkIndex_Object = MibTableColumn
mcmGcmLinkIndex = _McmGcmLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1, 1),
    _McmGcmLinkIndex_Type()
)
mcmGcmLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmLinkIndex.setStatus("mandatory")


class _McmGcmLinkUnitIndex_Type(Integer32):
    """Custom type mcmGcmLinkUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_McmGcmLinkUnitIndex_Type.__name__ = "Integer32"
_McmGcmLinkUnitIndex_Object = MibTableColumn
mcmGcmLinkUnitIndex = _McmGcmLinkUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1, 2),
    _McmGcmLinkUnitIndex_Type()
)
mcmGcmLinkUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmLinkUnitIndex.setStatus("mandatory")


class _McmGcmLinkName_Type(DisplayString):
    """Custom type mcmGcmLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_McmGcmLinkName_Type.__name__ = "DisplayString"
_McmGcmLinkName_Object = MibTableColumn
mcmGcmLinkName = _McmGcmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1, 3),
    _McmGcmLinkName_Type()
)
mcmGcmLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmLinkName.setStatus("mandatory")


class _McmGcmLinkSigType_Type(Integer32):
    """Custom type mcmGcmLinkSigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 2),
          ("reserved", 1),
          ("unusedEver-up", 3))
    )


_McmGcmLinkSigType_Type.__name__ = "Integer32"
_McmGcmLinkSigType_Object = MibTableColumn
mcmGcmLinkSigType = _McmGcmLinkSigType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1, 4),
    _McmGcmLinkSigType_Type()
)
mcmGcmLinkSigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmLinkSigType.setStatus("mandatory")


class _McmGcmLinkSigPcmIndex_Type(Integer32):
    """Custom type mcmGcmLinkSigPcmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_McmGcmLinkSigPcmIndex_Type.__name__ = "Integer32"
_McmGcmLinkSigPcmIndex_Object = MibTableColumn
mcmGcmLinkSigPcmIndex = _McmGcmLinkSigPcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1, 5),
    _McmGcmLinkSigPcmIndex_Type()
)
mcmGcmLinkSigPcmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmLinkSigPcmIndex.setStatus("mandatory")


class _McmGcmLinkSigOperStatus_Type(Integer32):
    """Custom type mcmGcmLinkSigOperStatus based on Integer32"""
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
        *(("activating", 7),
          ("active", 8),
          ("cfg-error", 1),
          ("deferred", 5),
          ("disconnecting", 9),
          ("enable-wait", 4),
          ("ever-up", 10),
          ("inactive", 3),
          ("info-wait", 2),
          ("protocol-down", 6))
    )


_McmGcmLinkSigOperStatus_Type.__name__ = "Integer32"
_McmGcmLinkSigOperStatus_Object = MibTableColumn
mcmGcmLinkSigOperStatus = _McmGcmLinkSigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1, 6),
    _McmGcmLinkSigOperStatus_Type()
)
mcmGcmLinkSigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmLinkSigOperStatus.setStatus("mandatory")


class _McmGcmLinkProtoType_Type(Integer32):
    """Custom type mcmGcmLinkProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 2),
          ("reserved", 1))
    )


_McmGcmLinkProtoType_Type.__name__ = "Integer32"
_McmGcmLinkProtoType_Object = MibTableColumn
mcmGcmLinkProtoType = _McmGcmLinkProtoType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1, 7),
    _McmGcmLinkProtoType_Type()
)
mcmGcmLinkProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmLinkProtoType.setStatus("mandatory")


class _McmGcmLinkProtoPcmIndex_Type(Integer32):
    """Custom type mcmGcmLinkProtoPcmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_McmGcmLinkProtoPcmIndex_Type.__name__ = "Integer32"
_McmGcmLinkProtoPcmIndex_Object = MibTableColumn
mcmGcmLinkProtoPcmIndex = _McmGcmLinkProtoPcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1, 8),
    _McmGcmLinkProtoPcmIndex_Type()
)
mcmGcmLinkProtoPcmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmLinkProtoPcmIndex.setStatus("mandatory")


class _McmGcmLinkProtoStatus_Type(Integer32):
    """Custom type mcmGcmLinkProtoStatus based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("activating", 7),
          ("active", 10),
          ("cfg-error", 1),
          ("deferred", 5),
          ("disconnecting", 11),
          ("enable-wait", 4),
          ("ever-up", 12),
          ("inactive", 3),
          ("info-wait", 2),
          ("protocol-down", 6),
          ("switching", 9),
          ("wait-switch", 8))
    )


_McmGcmLinkProtoStatus_Type.__name__ = "Integer32"
_McmGcmLinkProtoStatus_Object = MibTableColumn
mcmGcmLinkProtoStatus = _McmGcmLinkProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1, 9),
    _McmGcmLinkProtoStatus_Type()
)
mcmGcmLinkProtoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmLinkProtoStatus.setStatus("mandatory")


class _McmGcmLinkVoiceCalls_Type(Integer32):
    """Custom type mcmGcmLinkVoiceCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmGcmLinkVoiceCalls_Type.__name__ = "Integer32"
_McmGcmLinkVoiceCalls_Object = MibTableColumn
mcmGcmLinkVoiceCalls = _McmGcmLinkVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 2, 1, 10),
    _McmGcmLinkVoiceCalls_Type()
)
mcmGcmLinkVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmLinkVoiceCalls.setStatus("mandatory")
_McmGcmUnitTable_Object = MibTable
mcmGcmUnitTable = _McmGcmUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3)
)
if mibBuilder.loadTexts:
    mcmGcmUnitTable.setStatus("mandatory")
_McmGcmUnitEntry_Object = MibTableRow
mcmGcmUnitEntry = _McmGcmUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1)
)
mcmGcmUnitEntry.setIndexNames(
    (0, "MICOM-GCM-MIB", "mcmGcmUnitIndex"),
)
if mibBuilder.loadTexts:
    mcmGcmUnitEntry.setStatus("mandatory")


class _McmGcmUnitIndex_Type(Integer32):
    """Custom type mcmGcmUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_McmGcmUnitIndex_Type.__name__ = "Integer32"
_McmGcmUnitIndex_Object = MibTableColumn
mcmGcmUnitIndex = _McmGcmUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 1),
    _McmGcmUnitIndex_Type()
)
mcmGcmUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitIndex.setStatus("mandatory")


class _McmGcmUnitName_Type(DisplayString):
    """Custom type mcmGcmUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_McmGcmUnitName_Type.__name__ = "DisplayString"
_McmGcmUnitName_Object = MibTableColumn
mcmGcmUnitName = _McmGcmUnitName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 2),
    _McmGcmUnitName_Type()
)
mcmGcmUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitName.setStatus("mandatory")


class _McmGcmUnitAdminStatus_Type(Integer32):
    """Custom type mcmGcmUnitAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_McmGcmUnitAdminStatus_Type.__name__ = "Integer32"
_McmGcmUnitAdminStatus_Object = MibTableColumn
mcmGcmUnitAdminStatus = _McmGcmUnitAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 3),
    _McmGcmUnitAdminStatus_Type()
)
mcmGcmUnitAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitAdminStatus.setStatus("mandatory")


class _McmGcmUnitTimerAdminStatus_Type(Integer32):
    """Custom type mcmGcmUnitTimerAdminStatus based on Integer32"""
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


_McmGcmUnitTimerAdminStatus_Type.__name__ = "Integer32"
_McmGcmUnitTimerAdminStatus_Object = MibTableColumn
mcmGcmUnitTimerAdminStatus = _McmGcmUnitTimerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 4),
    _McmGcmUnitTimerAdminStatus_Type()
)
mcmGcmUnitTimerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitTimerAdminStatus.setStatus("mandatory")


class _McmGcmUnitSwitchType_Type(Integer32):
    """Custom type mcmGcmUnitSwitchType based on Integer32"""
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
        *(("fast-switch", 1),
          ("manual-switch-backup", 3),
          ("manual-switching", 4),
          ("voice-switch", 2))
    )


_McmGcmUnitSwitchType_Type.__name__ = "Integer32"
_McmGcmUnitSwitchType_Object = MibTableColumn
mcmGcmUnitSwitchType = _McmGcmUnitSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 5),
    _McmGcmUnitSwitchType_Type()
)
mcmGcmUnitSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitSwitchType.setStatus("mandatory")


class _McmGcmUnitSwitchDelay_Type(Integer32):
    """Custom type mcmGcmUnitSwitchDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmGcmUnitSwitchDelay_Type.__name__ = "Integer32"
_McmGcmUnitSwitchDelay_Object = MibTableColumn
mcmGcmUnitSwitchDelay = _McmGcmUnitSwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 6),
    _McmGcmUnitSwitchDelay_Type()
)
mcmGcmUnitSwitchDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitSwitchDelay.setStatus("deprecated")


class _McmGcmUnitPrimaryLinkIndex_Type(Integer32):
    """Custom type mcmGcmUnitPrimaryLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmGcmUnitPrimaryLinkIndex_Type.__name__ = "Integer32"
_McmGcmUnitPrimaryLinkIndex_Object = MibTableColumn
mcmGcmUnitPrimaryLinkIndex = _McmGcmUnitPrimaryLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 7),
    _McmGcmUnitPrimaryLinkIndex_Type()
)
mcmGcmUnitPrimaryLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitPrimaryLinkIndex.setStatus("mandatory")


class _McmGcmUnitBackupRemainTime_Type(Integer32):
    """Custom type mcmGcmUnitBackupRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmGcmUnitBackupRemainTime_Type.__name__ = "Integer32"
_McmGcmUnitBackupRemainTime_Object = MibTableColumn
mcmGcmUnitBackupRemainTime = _McmGcmUnitBackupRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 8),
    _McmGcmUnitBackupRemainTime_Type()
)
mcmGcmUnitBackupRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitBackupRemainTime.setStatus("mandatory")


class _McmGcmUnitBackupSwitchDelay_Type(Integer32):
    """Custom type mcmGcmUnitBackupSwitchDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmGcmUnitBackupSwitchDelay_Type.__name__ = "Integer32"
_McmGcmUnitBackupSwitchDelay_Object = MibTableColumn
mcmGcmUnitBackupSwitchDelay = _McmGcmUnitBackupSwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 9),
    _McmGcmUnitBackupSwitchDelay_Type()
)
mcmGcmUnitBackupSwitchDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitBackupSwitchDelay.setStatus("mandatory")


class _McmGcmUnitPrimarySwitchDelay_Type(Integer32):
    """Custom type mcmGcmUnitPrimarySwitchDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmGcmUnitPrimarySwitchDelay_Type.__name__ = "Integer32"
_McmGcmUnitPrimarySwitchDelay_Object = MibTableColumn
mcmGcmUnitPrimarySwitchDelay = _McmGcmUnitPrimarySwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 10),
    _McmGcmUnitPrimarySwitchDelay_Type()
)
mcmGcmUnitPrimarySwitchDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitPrimarySwitchDelay.setStatus("mandatory")


class _McmGcmUnitRegionalLinkIndex_Type(Integer32):
    """Custom type mcmGcmUnitRegionalLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmGcmUnitRegionalLinkIndex_Type.__name__ = "Integer32"
_McmGcmUnitRegionalLinkIndex_Object = MibTableColumn
mcmGcmUnitRegionalLinkIndex = _McmGcmUnitRegionalLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 11),
    _McmGcmUnitRegionalLinkIndex_Type()
)
mcmGcmUnitRegionalLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitRegionalLinkIndex.setStatus("mandatory")


class _McmGcmUnitModeCfg_Type(Integer32):
    """Custom type mcmGcmUnitModeCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("branch-node", 1),
          ("central-site-node", 3),
          ("regional-node", 2))
    )


_McmGcmUnitModeCfg_Type.__name__ = "Integer32"
_McmGcmUnitModeCfg_Object = MibTableColumn
mcmGcmUnitModeCfg = _McmGcmUnitModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 12),
    _McmGcmUnitModeCfg_Type()
)
mcmGcmUnitModeCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitModeCfg.setStatus("mandatory")


class _McmGcmUnitPriLinkFailMonStatus_Type(Integer32):
    """Custom type mcmGcmUnitPriLinkFailMonStatus based on Integer32"""
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


_McmGcmUnitPriLinkFailMonStatus_Type.__name__ = "Integer32"
_McmGcmUnitPriLinkFailMonStatus_Object = MibTableColumn
mcmGcmUnitPriLinkFailMonStatus = _McmGcmUnitPriLinkFailMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 13),
    _McmGcmUnitPriLinkFailMonStatus_Type()
)
mcmGcmUnitPriLinkFailMonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitPriLinkFailMonStatus.setStatus("mandatory")


class _McmGcmUnitPriLinkFailMonDurMin_Type(Integer32):
    """Custom type mcmGcmUnitPriLinkFailMonDurMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmGcmUnitPriLinkFailMonDurMin_Type.__name__ = "Integer32"
_McmGcmUnitPriLinkFailMonDurMin_Object = MibTableColumn
mcmGcmUnitPriLinkFailMonDurMin = _McmGcmUnitPriLinkFailMonDurMin_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 14),
    _McmGcmUnitPriLinkFailMonDurMin_Type()
)
mcmGcmUnitPriLinkFailMonDurMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitPriLinkFailMonDurMin.setStatus("mandatory")


class _McmGcmUnitPriLinkFailMonThrshld_Type(Integer32):
    """Custom type mcmGcmUnitPriLinkFailMonThrshld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmGcmUnitPriLinkFailMonThrshld_Type.__name__ = "Integer32"
_McmGcmUnitPriLinkFailMonThrshld_Object = MibTableColumn
mcmGcmUnitPriLinkFailMonThrshld = _McmGcmUnitPriLinkFailMonThrshld_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 15),
    _McmGcmUnitPriLinkFailMonThrshld_Type()
)
mcmGcmUnitPriLinkFailMonThrshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitPriLinkFailMonThrshld.setStatus("mandatory")


class _McmGcmUnitPriLinkFailMonCount_Type(Integer32):
    """Custom type mcmGcmUnitPriLinkFailMonCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmGcmUnitPriLinkFailMonCount_Type.__name__ = "Integer32"
_McmGcmUnitPriLinkFailMonCount_Object = MibTableColumn
mcmGcmUnitPriLinkFailMonCount = _McmGcmUnitPriLinkFailMonCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 16),
    _McmGcmUnitPriLinkFailMonCount_Type()
)
mcmGcmUnitPriLinkFailMonCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmUnitPriLinkFailMonCount.setStatus("mandatory")


class _McmGcmUnitCmd_Type(Integer32):
    """Custom type mcmGcmUnitCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch-to-backup", 2),
          ("switch-to-primary", 1))
    )


_McmGcmUnitCmd_Type.__name__ = "Integer32"
_McmGcmUnitCmd_Object = MibTableColumn
mcmGcmUnitCmd = _McmGcmUnitCmd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 3, 1, 17),
    _McmGcmUnitCmd_Type()
)
mcmGcmUnitCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmGcmUnitCmd.setStatus("mandatory")
_McmGcmBackupCfgTable_Object = MibTable
mcmGcmBackupCfgTable = _McmGcmBackupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 4)
)
if mibBuilder.loadTexts:
    mcmGcmBackupCfgTable.setStatus("mandatory")
_McmGcmBackupCfgEntry_Object = MibTableRow
mcmGcmBackupCfgEntry = _McmGcmBackupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 4, 1)
)
mcmGcmBackupCfgEntry.setIndexNames(
    (0, "MICOM-GCM-MIB", "mcmGcmBackupCfgIndex"),
)
if mibBuilder.loadTexts:
    mcmGcmBackupCfgEntry.setStatus("mandatory")


class _McmGcmBackupCfgIndex_Type(Integer32):
    """Custom type mcmGcmBackupCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmGcmBackupCfgIndex_Type.__name__ = "Integer32"
_McmGcmBackupCfgIndex_Object = MibTableColumn
mcmGcmBackupCfgIndex = _McmGcmBackupCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 4, 1, 1),
    _McmGcmBackupCfgIndex_Type()
)
mcmGcmBackupCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmBackupCfgIndex.setStatus("mandatory")


class _McmGcmBackupCfgUnitIndex_Type(Integer32):
    """Custom type mcmGcmBackupCfgUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_McmGcmBackupCfgUnitIndex_Type.__name__ = "Integer32"
_McmGcmBackupCfgUnitIndex_Object = MibTableColumn
mcmGcmBackupCfgUnitIndex = _McmGcmBackupCfgUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 4, 1, 2),
    _McmGcmBackupCfgUnitIndex_Type()
)
mcmGcmBackupCfgUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmBackupCfgUnitIndex.setStatus("mandatory")


class _McmGcmBackupCfgLinkIndex_Type(Integer32):
    """Custom type mcmGcmBackupCfgLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmGcmBackupCfgLinkIndex_Type.__name__ = "Integer32"
_McmGcmBackupCfgLinkIndex_Object = MibTableColumn
mcmGcmBackupCfgLinkIndex = _McmGcmBackupCfgLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 4, 1, 3),
    _McmGcmBackupCfgLinkIndex_Type()
)
mcmGcmBackupCfgLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmBackupCfgLinkIndex.setStatus("mandatory")
_McmGcmTimerTable_Object = MibTable
mcmGcmTimerTable = _McmGcmTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5)
)
if mibBuilder.loadTexts:
    mcmGcmTimerTable.setStatus("mandatory")
_McmGcmTimerEntry_Object = MibTableRow
mcmGcmTimerEntry = _McmGcmTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1)
)
mcmGcmTimerEntry.setIndexNames(
    (0, "MICOM-GCM-MIB", "mcmGcmTimerIndex"),
)
if mibBuilder.loadTexts:
    mcmGcmTimerEntry.setStatus("mandatory")


class _McmGcmTimerIndex_Type(Integer32):
    """Custom type mcmGcmTimerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmGcmTimerIndex_Type.__name__ = "Integer32"
_McmGcmTimerIndex_Object = MibTableColumn
mcmGcmTimerIndex = _McmGcmTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 1),
    _McmGcmTimerIndex_Type()
)
mcmGcmTimerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerIndex.setStatus("mandatory")


class _McmGcmTimerUnitIndex_Type(Integer32):
    """Custom type mcmGcmTimerUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_McmGcmTimerUnitIndex_Type.__name__ = "Integer32"
_McmGcmTimerUnitIndex_Object = MibTableColumn
mcmGcmTimerUnitIndex = _McmGcmTimerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 2),
    _McmGcmTimerUnitIndex_Type()
)
mcmGcmTimerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerUnitIndex.setStatus("mandatory")


class _McmGcmTimerInactStartHr_Type(Integer32):
    """Custom type mcmGcmTimerInactStartHr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_McmGcmTimerInactStartHr_Type.__name__ = "Integer32"
_McmGcmTimerInactStartHr_Object = MibTableColumn
mcmGcmTimerInactStartHr = _McmGcmTimerInactStartHr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 3),
    _McmGcmTimerInactStartHr_Type()
)
mcmGcmTimerInactStartHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactStartHr.setStatus("mandatory")


class _McmGcmTimerInactStartMin_Type(Integer32):
    """Custom type mcmGcmTimerInactStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_McmGcmTimerInactStartMin_Type.__name__ = "Integer32"
_McmGcmTimerInactStartMin_Object = MibTableColumn
mcmGcmTimerInactStartMin = _McmGcmTimerInactStartMin_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 4),
    _McmGcmTimerInactStartMin_Type()
)
mcmGcmTimerInactStartMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactStartMin.setStatus("mandatory")


class _McmGcmTimerInactDurationHr_Type(Integer32):
    """Custom type mcmGcmTimerInactDurationHr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 167),
    )


_McmGcmTimerInactDurationHr_Type.__name__ = "Integer32"
_McmGcmTimerInactDurationHr_Object = MibTableColumn
mcmGcmTimerInactDurationHr = _McmGcmTimerInactDurationHr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 5),
    _McmGcmTimerInactDurationHr_Type()
)
mcmGcmTimerInactDurationHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactDurationHr.setStatus("mandatory")


class _McmGcmTimerInactDurationMin_Type(Integer32):
    """Custom type mcmGcmTimerInactDurationMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_McmGcmTimerInactDurationMin_Type.__name__ = "Integer32"
_McmGcmTimerInactDurationMin_Object = MibTableColumn
mcmGcmTimerInactDurationMin = _McmGcmTimerInactDurationMin_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 6),
    _McmGcmTimerInactDurationMin_Type()
)
mcmGcmTimerInactDurationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactDurationMin.setStatus("mandatory")


class _McmGcmTimerInactMonday_Type(Integer32):
    """Custom type mcmGcmTimerInactMonday based on Integer32"""
    defaultValue = 2

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


_McmGcmTimerInactMonday_Type.__name__ = "Integer32"
_McmGcmTimerInactMonday_Object = MibTableColumn
mcmGcmTimerInactMonday = _McmGcmTimerInactMonday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 7),
    _McmGcmTimerInactMonday_Type()
)
mcmGcmTimerInactMonday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactMonday.setStatus("mandatory")


class _McmGcmTimerInactTuesday_Type(Integer32):
    """Custom type mcmGcmTimerInactTuesday based on Integer32"""
    defaultValue = 2

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


_McmGcmTimerInactTuesday_Type.__name__ = "Integer32"
_McmGcmTimerInactTuesday_Object = MibTableColumn
mcmGcmTimerInactTuesday = _McmGcmTimerInactTuesday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 8),
    _McmGcmTimerInactTuesday_Type()
)
mcmGcmTimerInactTuesday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactTuesday.setStatus("mandatory")


class _McmGcmTimerInactWednesday_Type(Integer32):
    """Custom type mcmGcmTimerInactWednesday based on Integer32"""
    defaultValue = 2

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


_McmGcmTimerInactWednesday_Type.__name__ = "Integer32"
_McmGcmTimerInactWednesday_Object = MibTableColumn
mcmGcmTimerInactWednesday = _McmGcmTimerInactWednesday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 9),
    _McmGcmTimerInactWednesday_Type()
)
mcmGcmTimerInactWednesday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactWednesday.setStatus("mandatory")


class _McmGcmTimerInactThursday_Type(Integer32):
    """Custom type mcmGcmTimerInactThursday based on Integer32"""
    defaultValue = 2

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


_McmGcmTimerInactThursday_Type.__name__ = "Integer32"
_McmGcmTimerInactThursday_Object = MibTableColumn
mcmGcmTimerInactThursday = _McmGcmTimerInactThursday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 10),
    _McmGcmTimerInactThursday_Type()
)
mcmGcmTimerInactThursday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactThursday.setStatus("mandatory")


class _McmGcmTimerInactFriday_Type(Integer32):
    """Custom type mcmGcmTimerInactFriday based on Integer32"""
    defaultValue = 2

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


_McmGcmTimerInactFriday_Type.__name__ = "Integer32"
_McmGcmTimerInactFriday_Object = MibTableColumn
mcmGcmTimerInactFriday = _McmGcmTimerInactFriday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 11),
    _McmGcmTimerInactFriday_Type()
)
mcmGcmTimerInactFriday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactFriday.setStatus("mandatory")


class _McmGcmTimerInactSaturday_Type(Integer32):
    """Custom type mcmGcmTimerInactSaturday based on Integer32"""
    defaultValue = 2

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


_McmGcmTimerInactSaturday_Type.__name__ = "Integer32"
_McmGcmTimerInactSaturday_Object = MibTableColumn
mcmGcmTimerInactSaturday = _McmGcmTimerInactSaturday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 12),
    _McmGcmTimerInactSaturday_Type()
)
mcmGcmTimerInactSaturday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactSaturday.setStatus("mandatory")


class _McmGcmTimerInactSunday_Type(Integer32):
    """Custom type mcmGcmTimerInactSunday based on Integer32"""
    defaultValue = 2

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


_McmGcmTimerInactSunday_Type.__name__ = "Integer32"
_McmGcmTimerInactSunday_Object = MibTableColumn
mcmGcmTimerInactSunday = _McmGcmTimerInactSunday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 13),
    _McmGcmTimerInactSunday_Type()
)
mcmGcmTimerInactSunday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactSunday.setStatus("mandatory")


class _McmGcmTimerInactPeriodic_Type(Integer32):
    """Custom type mcmGcmTimerInactPeriodic based on Integer32"""
    defaultValue = 2

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


_McmGcmTimerInactPeriodic_Type.__name__ = "Integer32"
_McmGcmTimerInactPeriodic_Object = MibTableColumn
mcmGcmTimerInactPeriodic = _McmGcmTimerInactPeriodic_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 5, 1, 14),
    _McmGcmTimerInactPeriodic_Type()
)
mcmGcmTimerInactPeriodic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmTimerInactPeriodic.setStatus("mandatory")
_NvmGcmGlobalCfgGroup_ObjectIdentity = ObjectIdentity
nvmGcmGlobalCfgGroup = _NvmGcmGlobalCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 6)
)


class _NvmGcmGlobalCfgAdminStatus_Type(Integer32):
    """Custom type nvmGcmGlobalCfgAdminStatus based on Integer32"""
    defaultValue = 1

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


_NvmGcmGlobalCfgAdminStatus_Type.__name__ = "Integer32"
_NvmGcmGlobalCfgAdminStatus_Object = MibScalar
nvmGcmGlobalCfgAdminStatus = _NvmGcmGlobalCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 6, 1),
    _NvmGcmGlobalCfgAdminStatus_Type()
)
nvmGcmGlobalCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmGlobalCfgAdminStatus.setStatus("mandatory")


class _NvmGcmGlobalCfgTraps_Type(Integer32):
    """Custom type nvmGcmGlobalCfgTraps based on Integer32"""
    defaultValue = 2

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


_NvmGcmGlobalCfgTraps_Type.__name__ = "Integer32"
_NvmGcmGlobalCfgTraps_Object = MibScalar
nvmGcmGlobalCfgTraps = _NvmGcmGlobalCfgTraps_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 6, 2),
    _NvmGcmGlobalCfgTraps_Type()
)
nvmGcmGlobalCfgTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmGlobalCfgTraps.setStatus("mandatory")


class _NvmGcmGlobalCfgAutoActSelMode_Type(Integer32):
    """Custom type nvmGcmGlobalCfgAutoActSelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("hwCfgAutoSelect", 1))
    )


_NvmGcmGlobalCfgAutoActSelMode_Type.__name__ = "Integer32"
_NvmGcmGlobalCfgAutoActSelMode_Object = MibScalar
nvmGcmGlobalCfgAutoActSelMode = _NvmGcmGlobalCfgAutoActSelMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 6, 3),
    _NvmGcmGlobalCfgAutoActSelMode_Type()
)
nvmGcmGlobalCfgAutoActSelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmGlobalCfgAutoActSelMode.setStatus("mandatory")
_NvmGcmLinkTable_Object = MibTable
nvmGcmLinkTable = _NvmGcmLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 7)
)
if mibBuilder.loadTexts:
    nvmGcmLinkTable.setStatus("mandatory")
_NvmGcmLinkEntry_Object = MibTableRow
nvmGcmLinkEntry = _NvmGcmLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 7, 1)
)
nvmGcmLinkEntry.setIndexNames(
    (0, "MICOM-GCM-MIB", "nvmGcmLinkIndex"),
)
if mibBuilder.loadTexts:
    nvmGcmLinkEntry.setStatus("mandatory")


class _NvmGcmLinkIndex_Type(Integer32):
    """Custom type nvmGcmLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmGcmLinkIndex_Type.__name__ = "Integer32"
_NvmGcmLinkIndex_Object = MibTableColumn
nvmGcmLinkIndex = _NvmGcmLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 7, 1, 1),
    _NvmGcmLinkIndex_Type()
)
nvmGcmLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmGcmLinkIndex.setStatus("mandatory")


class _NvmGcmLinkUnitIndex_Type(Integer32):
    """Custom type nvmGcmLinkUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NvmGcmLinkUnitIndex_Type.__name__ = "Integer32"
_NvmGcmLinkUnitIndex_Object = MibTableColumn
nvmGcmLinkUnitIndex = _NvmGcmLinkUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 7, 1, 2),
    _NvmGcmLinkUnitIndex_Type()
)
nvmGcmLinkUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmGcmLinkUnitIndex.setStatus("mandatory")


class _NvmGcmLinkName_Type(DisplayString):
    """Custom type nvmGcmLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NvmGcmLinkName_Type.__name__ = "DisplayString"
_NvmGcmLinkName_Object = MibTableColumn
nvmGcmLinkName = _NvmGcmLinkName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 7, 1, 3),
    _NvmGcmLinkName_Type()
)
nvmGcmLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmLinkName.setStatus("mandatory")


class _NvmGcmLinkSigType_Type(Integer32):
    """Custom type nvmGcmLinkSigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 2),
          ("reserved", 1),
          ("unusedEver-up", 3))
    )


_NvmGcmLinkSigType_Type.__name__ = "Integer32"
_NvmGcmLinkSigType_Object = MibTableColumn
nvmGcmLinkSigType = _NvmGcmLinkSigType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 7, 1, 4),
    _NvmGcmLinkSigType_Type()
)
nvmGcmLinkSigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmLinkSigType.setStatus("mandatory")


class _NvmGcmLinkSigPcmIndex_Type(Integer32):
    """Custom type nvmGcmLinkSigPcmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NvmGcmLinkSigPcmIndex_Type.__name__ = "Integer32"
_NvmGcmLinkSigPcmIndex_Object = MibTableColumn
nvmGcmLinkSigPcmIndex = _NvmGcmLinkSigPcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 7, 1, 5),
    _NvmGcmLinkSigPcmIndex_Type()
)
nvmGcmLinkSigPcmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmLinkSigPcmIndex.setStatus("mandatory")


class _NvmGcmLinkProtoType_Type(Integer32):
    """Custom type nvmGcmLinkProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 2),
          ("reserved", 1))
    )


_NvmGcmLinkProtoType_Type.__name__ = "Integer32"
_NvmGcmLinkProtoType_Object = MibTableColumn
nvmGcmLinkProtoType = _NvmGcmLinkProtoType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 7, 1, 6),
    _NvmGcmLinkProtoType_Type()
)
nvmGcmLinkProtoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmLinkProtoType.setStatus("mandatory")


class _NvmGcmLinkProtoPcmIndex_Type(Integer32):
    """Custom type nvmGcmLinkProtoPcmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NvmGcmLinkProtoPcmIndex_Type.__name__ = "Integer32"
_NvmGcmLinkProtoPcmIndex_Object = MibTableColumn
nvmGcmLinkProtoPcmIndex = _NvmGcmLinkProtoPcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 7, 1, 7),
    _NvmGcmLinkProtoPcmIndex_Type()
)
nvmGcmLinkProtoPcmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmLinkProtoPcmIndex.setStatus("mandatory")


class _NvmGcmLinkRowStatus_Type(Integer32):
    """Custom type nvmGcmLinkRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("add", 1),
          ("delete", 2))
    )


_NvmGcmLinkRowStatus_Type.__name__ = "Integer32"
_NvmGcmLinkRowStatus_Object = MibTableColumn
nvmGcmLinkRowStatus = _NvmGcmLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 7, 1, 8),
    _NvmGcmLinkRowStatus_Type()
)
nvmGcmLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmLinkRowStatus.setStatus("mandatory")
_NvmGcmUnitTable_Object = MibTable
nvmGcmUnitTable = _NvmGcmUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8)
)
if mibBuilder.loadTexts:
    nvmGcmUnitTable.setStatus("mandatory")
_NvmGcmUnitEntry_Object = MibTableRow
nvmGcmUnitEntry = _NvmGcmUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1)
)
nvmGcmUnitEntry.setIndexNames(
    (0, "MICOM-GCM-MIB", "nvmGcmUnitIndex"),
)
if mibBuilder.loadTexts:
    nvmGcmUnitEntry.setStatus("mandatory")


class _NvmGcmUnitIndex_Type(Integer32):
    """Custom type nvmGcmUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NvmGcmUnitIndex_Type.__name__ = "Integer32"
_NvmGcmUnitIndex_Object = MibTableColumn
nvmGcmUnitIndex = _NvmGcmUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 1),
    _NvmGcmUnitIndex_Type()
)
nvmGcmUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmGcmUnitIndex.setStatus("mandatory")


class _NvmGcmUnitName_Type(DisplayString):
    """Custom type nvmGcmUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_NvmGcmUnitName_Type.__name__ = "DisplayString"
_NvmGcmUnitName_Object = MibTableColumn
nvmGcmUnitName = _NvmGcmUnitName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 2),
    _NvmGcmUnitName_Type()
)
nvmGcmUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitName.setStatus("mandatory")


class _NvmGcmUnitAdminStatus_Type(Integer32):
    """Custom type nvmGcmUnitAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_NvmGcmUnitAdminStatus_Type.__name__ = "Integer32"
_NvmGcmUnitAdminStatus_Object = MibTableColumn
nvmGcmUnitAdminStatus = _NvmGcmUnitAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 3),
    _NvmGcmUnitAdminStatus_Type()
)
nvmGcmUnitAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitAdminStatus.setStatus("mandatory")


class _NvmGcmUnitTimerAdminStatus_Type(Integer32):
    """Custom type nvmGcmUnitTimerAdminStatus based on Integer32"""
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


_NvmGcmUnitTimerAdminStatus_Type.__name__ = "Integer32"
_NvmGcmUnitTimerAdminStatus_Object = MibTableColumn
nvmGcmUnitTimerAdminStatus = _NvmGcmUnitTimerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 4),
    _NvmGcmUnitTimerAdminStatus_Type()
)
nvmGcmUnitTimerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitTimerAdminStatus.setStatus("mandatory")


class _NvmGcmUnitSwitchType_Type(Integer32):
    """Custom type nvmGcmUnitSwitchType based on Integer32"""
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
        *(("fast-switch", 1),
          ("manual-switch-backup", 3),
          ("manual-switching", 4),
          ("voice-switch", 2))
    )


_NvmGcmUnitSwitchType_Type.__name__ = "Integer32"
_NvmGcmUnitSwitchType_Object = MibTableColumn
nvmGcmUnitSwitchType = _NvmGcmUnitSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 5),
    _NvmGcmUnitSwitchType_Type()
)
nvmGcmUnitSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitSwitchType.setStatus("mandatory")


class _NvmGcmUnitSwitchDelay_Type(Integer32):
    """Custom type nvmGcmUnitSwitchDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmGcmUnitSwitchDelay_Type.__name__ = "Integer32"
_NvmGcmUnitSwitchDelay_Object = MibTableColumn
nvmGcmUnitSwitchDelay = _NvmGcmUnitSwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 6),
    _NvmGcmUnitSwitchDelay_Type()
)
nvmGcmUnitSwitchDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitSwitchDelay.setStatus("deprecated")


class _NvmGcmUnitPrimaryLinkIndex_Type(Integer32):
    """Custom type nvmGcmUnitPrimaryLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmGcmUnitPrimaryLinkIndex_Type.__name__ = "Integer32"
_NvmGcmUnitPrimaryLinkIndex_Object = MibTableColumn
nvmGcmUnitPrimaryLinkIndex = _NvmGcmUnitPrimaryLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 7),
    _NvmGcmUnitPrimaryLinkIndex_Type()
)
nvmGcmUnitPrimaryLinkIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitPrimaryLinkIndex.setStatus("mandatory")


class _NvmGcmUnitBackupRemainTime_Type(Integer32):
    """Custom type nvmGcmUnitBackupRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmGcmUnitBackupRemainTime_Type.__name__ = "Integer32"
_NvmGcmUnitBackupRemainTime_Object = MibTableColumn
nvmGcmUnitBackupRemainTime = _NvmGcmUnitBackupRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 8),
    _NvmGcmUnitBackupRemainTime_Type()
)
nvmGcmUnitBackupRemainTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitBackupRemainTime.setStatus("mandatory")


class _NvmGcmUnitBackupSwitchDelay_Type(Integer32):
    """Custom type nvmGcmUnitBackupSwitchDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmGcmUnitBackupSwitchDelay_Type.__name__ = "Integer32"
_NvmGcmUnitBackupSwitchDelay_Object = MibTableColumn
nvmGcmUnitBackupSwitchDelay = _NvmGcmUnitBackupSwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 9),
    _NvmGcmUnitBackupSwitchDelay_Type()
)
nvmGcmUnitBackupSwitchDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitBackupSwitchDelay.setStatus("mandatory")


class _NvmGcmUnitPrimarySwitchDelay_Type(Integer32):
    """Custom type nvmGcmUnitPrimarySwitchDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmGcmUnitPrimarySwitchDelay_Type.__name__ = "Integer32"
_NvmGcmUnitPrimarySwitchDelay_Object = MibTableColumn
nvmGcmUnitPrimarySwitchDelay = _NvmGcmUnitPrimarySwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 10),
    _NvmGcmUnitPrimarySwitchDelay_Type()
)
nvmGcmUnitPrimarySwitchDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitPrimarySwitchDelay.setStatus("mandatory")


class _NvmGcmUnitRegionalLinkIndex_Type(Integer32):
    """Custom type nvmGcmUnitRegionalLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmGcmUnitRegionalLinkIndex_Type.__name__ = "Integer32"
_NvmGcmUnitRegionalLinkIndex_Object = MibTableColumn
nvmGcmUnitRegionalLinkIndex = _NvmGcmUnitRegionalLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 11),
    _NvmGcmUnitRegionalLinkIndex_Type()
)
nvmGcmUnitRegionalLinkIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitRegionalLinkIndex.setStatus("mandatory")


class _NvmGcmUnitModeCfg_Type(Integer32):
    """Custom type nvmGcmUnitModeCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("branch-node", 1),
          ("central-site-node", 3),
          ("regional-node", 2))
    )


_NvmGcmUnitModeCfg_Type.__name__ = "Integer32"
_NvmGcmUnitModeCfg_Object = MibTableColumn
nvmGcmUnitModeCfg = _NvmGcmUnitModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 12),
    _NvmGcmUnitModeCfg_Type()
)
nvmGcmUnitModeCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitModeCfg.setStatus("mandatory")


class _NvmGcmUnitPriLinkFailMonStatus_Type(Integer32):
    """Custom type nvmGcmUnitPriLinkFailMonStatus based on Integer32"""
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


_NvmGcmUnitPriLinkFailMonStatus_Type.__name__ = "Integer32"
_NvmGcmUnitPriLinkFailMonStatus_Object = MibTableColumn
nvmGcmUnitPriLinkFailMonStatus = _NvmGcmUnitPriLinkFailMonStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 13),
    _NvmGcmUnitPriLinkFailMonStatus_Type()
)
nvmGcmUnitPriLinkFailMonStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitPriLinkFailMonStatus.setStatus("mandatory")


class _NvmGcmUnitPriLinkFailMonDurMin_Type(Integer32):
    """Custom type nvmGcmUnitPriLinkFailMonDurMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmGcmUnitPriLinkFailMonDurMin_Type.__name__ = "Integer32"
_NvmGcmUnitPriLinkFailMonDurMin_Object = MibTableColumn
nvmGcmUnitPriLinkFailMonDurMin = _NvmGcmUnitPriLinkFailMonDurMin_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 14),
    _NvmGcmUnitPriLinkFailMonDurMin_Type()
)
nvmGcmUnitPriLinkFailMonDurMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitPriLinkFailMonDurMin.setStatus("mandatory")


class _NvmGcmUnitPriLinkFailMonThrshld_Type(Integer32):
    """Custom type nvmGcmUnitPriLinkFailMonThrshld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmGcmUnitPriLinkFailMonThrshld_Type.__name__ = "Integer32"
_NvmGcmUnitPriLinkFailMonThrshld_Object = MibTableColumn
nvmGcmUnitPriLinkFailMonThrshld = _NvmGcmUnitPriLinkFailMonThrshld_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 8, 1, 15),
    _NvmGcmUnitPriLinkFailMonThrshld_Type()
)
nvmGcmUnitPriLinkFailMonThrshld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmUnitPriLinkFailMonThrshld.setStatus("mandatory")
_NvmGcmBackupCfgTable_Object = MibTable
nvmGcmBackupCfgTable = _NvmGcmBackupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 9)
)
if mibBuilder.loadTexts:
    nvmGcmBackupCfgTable.setStatus("mandatory")
_NvmGcmBackupCfgEntry_Object = MibTableRow
nvmGcmBackupCfgEntry = _NvmGcmBackupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 9, 1)
)
nvmGcmBackupCfgEntry.setIndexNames(
    (0, "MICOM-GCM-MIB", "nvmGcmBackupCfgIndex"),
)
if mibBuilder.loadTexts:
    nvmGcmBackupCfgEntry.setStatus("mandatory")


class _NvmGcmBackupCfgIndex_Type(Integer32):
    """Custom type nvmGcmBackupCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmGcmBackupCfgIndex_Type.__name__ = "Integer32"
_NvmGcmBackupCfgIndex_Object = MibTableColumn
nvmGcmBackupCfgIndex = _NvmGcmBackupCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 9, 1, 1),
    _NvmGcmBackupCfgIndex_Type()
)
nvmGcmBackupCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmGcmBackupCfgIndex.setStatus("mandatory")


class _NvmGcmBackupCfgUnitIndex_Type(Integer32):
    """Custom type nvmGcmBackupCfgUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NvmGcmBackupCfgUnitIndex_Type.__name__ = "Integer32"
_NvmGcmBackupCfgUnitIndex_Object = MibTableColumn
nvmGcmBackupCfgUnitIndex = _NvmGcmBackupCfgUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 9, 1, 2),
    _NvmGcmBackupCfgUnitIndex_Type()
)
nvmGcmBackupCfgUnitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmBackupCfgUnitIndex.setStatus("mandatory")


class _NvmGcmBackupCfgLinkIndex_Type(Integer32):
    """Custom type nvmGcmBackupCfgLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmGcmBackupCfgLinkIndex_Type.__name__ = "Integer32"
_NvmGcmBackupCfgLinkIndex_Object = MibTableColumn
nvmGcmBackupCfgLinkIndex = _NvmGcmBackupCfgLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 9, 1, 3),
    _NvmGcmBackupCfgLinkIndex_Type()
)
nvmGcmBackupCfgLinkIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmBackupCfgLinkIndex.setStatus("mandatory")


class _NvmGcmBackupCfgLinkRowStatus_Type(Integer32):
    """Custom type nvmGcmBackupCfgLinkRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("add", 1),
          ("delete", 2))
    )


_NvmGcmBackupCfgLinkRowStatus_Type.__name__ = "Integer32"
_NvmGcmBackupCfgLinkRowStatus_Object = MibTableColumn
nvmGcmBackupCfgLinkRowStatus = _NvmGcmBackupCfgLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 9, 1, 4),
    _NvmGcmBackupCfgLinkRowStatus_Type()
)
nvmGcmBackupCfgLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmBackupCfgLinkRowStatus.setStatus("mandatory")
_NvmGcmTimerTable_Object = MibTable
nvmGcmTimerTable = _NvmGcmTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10)
)
if mibBuilder.loadTexts:
    nvmGcmTimerTable.setStatus("mandatory")
_NvmGcmTimerEntry_Object = MibTableRow
nvmGcmTimerEntry = _NvmGcmTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1)
)
nvmGcmTimerEntry.setIndexNames(
    (0, "MICOM-GCM-MIB", "nvmGcmTimerIndex"),
)
if mibBuilder.loadTexts:
    nvmGcmTimerEntry.setStatus("mandatory")


class _NvmGcmTimerIndex_Type(Integer32):
    """Custom type nvmGcmTimerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmGcmTimerIndex_Type.__name__ = "Integer32"
_NvmGcmTimerIndex_Object = MibTableColumn
nvmGcmTimerIndex = _NvmGcmTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 1),
    _NvmGcmTimerIndex_Type()
)
nvmGcmTimerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmGcmTimerIndex.setStatus("mandatory")


class _NvmGcmTimerUnitIndex_Type(Integer32):
    """Custom type nvmGcmTimerUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NvmGcmTimerUnitIndex_Type.__name__ = "Integer32"
_NvmGcmTimerUnitIndex_Object = MibTableColumn
nvmGcmTimerUnitIndex = _NvmGcmTimerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 2),
    _NvmGcmTimerUnitIndex_Type()
)
nvmGcmTimerUnitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerUnitIndex.setStatus("mandatory")


class _NvmGcmTimerInactStartHr_Type(Integer32):
    """Custom type nvmGcmTimerInactStartHr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_NvmGcmTimerInactStartHr_Type.__name__ = "Integer32"
_NvmGcmTimerInactStartHr_Object = MibTableColumn
nvmGcmTimerInactStartHr = _NvmGcmTimerInactStartHr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 3),
    _NvmGcmTimerInactStartHr_Type()
)
nvmGcmTimerInactStartHr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactStartHr.setStatus("mandatory")


class _NvmGcmTimerInactStartMin_Type(Integer32):
    """Custom type nvmGcmTimerInactStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_NvmGcmTimerInactStartMin_Type.__name__ = "Integer32"
_NvmGcmTimerInactStartMin_Object = MibTableColumn
nvmGcmTimerInactStartMin = _NvmGcmTimerInactStartMin_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 4),
    _NvmGcmTimerInactStartMin_Type()
)
nvmGcmTimerInactStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactStartMin.setStatus("mandatory")


class _NvmGcmTimerInactDurationHr_Type(Integer32):
    """Custom type nvmGcmTimerInactDurationHr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 167),
    )


_NvmGcmTimerInactDurationHr_Type.__name__ = "Integer32"
_NvmGcmTimerInactDurationHr_Object = MibTableColumn
nvmGcmTimerInactDurationHr = _NvmGcmTimerInactDurationHr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 5),
    _NvmGcmTimerInactDurationHr_Type()
)
nvmGcmTimerInactDurationHr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactDurationHr.setStatus("mandatory")


class _NvmGcmTimerInactDurationMin_Type(Integer32):
    """Custom type nvmGcmTimerInactDurationMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_NvmGcmTimerInactDurationMin_Type.__name__ = "Integer32"
_NvmGcmTimerInactDurationMin_Object = MibTableColumn
nvmGcmTimerInactDurationMin = _NvmGcmTimerInactDurationMin_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 6),
    _NvmGcmTimerInactDurationMin_Type()
)
nvmGcmTimerInactDurationMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactDurationMin.setStatus("mandatory")


class _NvmGcmTimerInactMonday_Type(Integer32):
    """Custom type nvmGcmTimerInactMonday based on Integer32"""
    defaultValue = 2

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


_NvmGcmTimerInactMonday_Type.__name__ = "Integer32"
_NvmGcmTimerInactMonday_Object = MibTableColumn
nvmGcmTimerInactMonday = _NvmGcmTimerInactMonday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 7),
    _NvmGcmTimerInactMonday_Type()
)
nvmGcmTimerInactMonday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactMonday.setStatus("mandatory")


class _NvmGcmTimerInactTuesday_Type(Integer32):
    """Custom type nvmGcmTimerInactTuesday based on Integer32"""
    defaultValue = 2

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


_NvmGcmTimerInactTuesday_Type.__name__ = "Integer32"
_NvmGcmTimerInactTuesday_Object = MibTableColumn
nvmGcmTimerInactTuesday = _NvmGcmTimerInactTuesday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 8),
    _NvmGcmTimerInactTuesday_Type()
)
nvmGcmTimerInactTuesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactTuesday.setStatus("mandatory")


class _NvmGcmTimerInactWednesday_Type(Integer32):
    """Custom type nvmGcmTimerInactWednesday based on Integer32"""
    defaultValue = 2

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


_NvmGcmTimerInactWednesday_Type.__name__ = "Integer32"
_NvmGcmTimerInactWednesday_Object = MibTableColumn
nvmGcmTimerInactWednesday = _NvmGcmTimerInactWednesday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 9),
    _NvmGcmTimerInactWednesday_Type()
)
nvmGcmTimerInactWednesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactWednesday.setStatus("mandatory")


class _NvmGcmTimerInactThursday_Type(Integer32):
    """Custom type nvmGcmTimerInactThursday based on Integer32"""
    defaultValue = 2

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


_NvmGcmTimerInactThursday_Type.__name__ = "Integer32"
_NvmGcmTimerInactThursday_Object = MibTableColumn
nvmGcmTimerInactThursday = _NvmGcmTimerInactThursday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 10),
    _NvmGcmTimerInactThursday_Type()
)
nvmGcmTimerInactThursday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactThursday.setStatus("mandatory")


class _NvmGcmTimerInactFriday_Type(Integer32):
    """Custom type nvmGcmTimerInactFriday based on Integer32"""
    defaultValue = 2

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


_NvmGcmTimerInactFriday_Type.__name__ = "Integer32"
_NvmGcmTimerInactFriday_Object = MibTableColumn
nvmGcmTimerInactFriday = _NvmGcmTimerInactFriday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 11),
    _NvmGcmTimerInactFriday_Type()
)
nvmGcmTimerInactFriday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactFriday.setStatus("mandatory")


class _NvmGcmTimerInactSaturday_Type(Integer32):
    """Custom type nvmGcmTimerInactSaturday based on Integer32"""
    defaultValue = 2

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


_NvmGcmTimerInactSaturday_Type.__name__ = "Integer32"
_NvmGcmTimerInactSaturday_Object = MibTableColumn
nvmGcmTimerInactSaturday = _NvmGcmTimerInactSaturday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 12),
    _NvmGcmTimerInactSaturday_Type()
)
nvmGcmTimerInactSaturday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactSaturday.setStatus("mandatory")


class _NvmGcmTimerInactSunday_Type(Integer32):
    """Custom type nvmGcmTimerInactSunday based on Integer32"""
    defaultValue = 2

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


_NvmGcmTimerInactSunday_Type.__name__ = "Integer32"
_NvmGcmTimerInactSunday_Object = MibTableColumn
nvmGcmTimerInactSunday = _NvmGcmTimerInactSunday_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 13),
    _NvmGcmTimerInactSunday_Type()
)
nvmGcmTimerInactSunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactSunday.setStatus("mandatory")


class _NvmGcmTimerInactPeriodic_Type(Integer32):
    """Custom type nvmGcmTimerInactPeriodic based on Integer32"""
    defaultValue = 2

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


_NvmGcmTimerInactPeriodic_Type.__name__ = "Integer32"
_NvmGcmTimerInactPeriodic_Object = MibTableColumn
nvmGcmTimerInactPeriodic = _NvmGcmTimerInactPeriodic_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 14),
    _NvmGcmTimerInactPeriodic_Type()
)
nvmGcmTimerInactPeriodic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerInactPeriodic.setStatus("mandatory")


class _NvmGcmTimerRowStatus_Type(Integer32):
    """Custom type nvmGcmTimerRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("add", 1),
          ("delete", 2))
    )


_NvmGcmTimerRowStatus_Type.__name__ = "Integer32"
_NvmGcmTimerRowStatus_Object = MibTableColumn
nvmGcmTimerRowStatus = _NvmGcmTimerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 1, 10, 1, 15),
    _NvmGcmTimerRowStatus_Type()
)
nvmGcmTimerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmGcmTimerRowStatus.setStatus("mandatory")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 2)
)
_McmGcmHwStatusTable_Object = MibTable
mcmGcmHwStatusTable = _McmGcmHwStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 2, 1)
)
if mibBuilder.loadTexts:
    mcmGcmHwStatusTable.setStatus("mandatory")
_McmGcmHwStatusEntry_Object = MibTableRow
mcmGcmHwStatusEntry = _McmGcmHwStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 2, 1, 1)
)
mcmGcmHwStatusEntry.setIndexNames(
    (0, "MICOM-GCM-MIB", "mcmGcmHwStatusIndex"),
)
if mibBuilder.loadTexts:
    mcmGcmHwStatusEntry.setStatus("mandatory")


class _McmGcmHwStatusIndex_Type(Integer32):
    """Custom type mcmGcmHwStatusIndex based on Integer32"""
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
        *(("everDown", 1),
          ("everUp", 2),
          ("frBackup", 6),
          ("frPrimary", 5),
          ("isdnBackup", 4),
          ("isdnPrimary", 3))
    )


_McmGcmHwStatusIndex_Type.__name__ = "Integer32"
_McmGcmHwStatusIndex_Object = MibTableColumn
mcmGcmHwStatusIndex = _McmGcmHwStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 2, 1, 1, 1),
    _McmGcmHwStatusIndex_Type()
)
mcmGcmHwStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmHwStatusIndex.setStatus("mandatory")


class _McmGcmHwStatusDesc_Type(DisplayString):
    """Custom type mcmGcmHwStatusDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_McmGcmHwStatusDesc_Type.__name__ = "DisplayString"
_McmGcmHwStatusDesc_Object = MibTableColumn
mcmGcmHwStatusDesc = _McmGcmHwStatusDesc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 2, 1, 1, 2),
    _McmGcmHwStatusDesc_Type()
)
mcmGcmHwStatusDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmHwStatusDesc.setStatus("mandatory")


class _McmGcmHwStatusOperStatus_Type(Integer32):
    """Custom type mcmGcmHwStatusOperStatus based on Integer32"""
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
        *(("disable-req", 6),
          ("down", 4),
          ("enable-req", 5),
          ("ever-down", 1),
          ("ever-up", 3),
          ("link-error", 7),
          ("up", 2))
    )


_McmGcmHwStatusOperStatus_Type.__name__ = "Integer32"
_McmGcmHwStatusOperStatus_Object = MibTableColumn
mcmGcmHwStatusOperStatus = _McmGcmHwStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 2, 1, 1, 3),
    _McmGcmHwStatusOperStatus_Type()
)
mcmGcmHwStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmHwStatusOperStatus.setStatus("mandatory")


class _McmGcmHwStatusActiveLink_Type(Integer32):
    """Custom type mcmGcmHwStatusActiveLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmGcmHwStatusActiveLink_Type.__name__ = "Integer32"
_McmGcmHwStatusActiveLink_Object = MibTableColumn
mcmGcmHwStatusActiveLink = _McmGcmHwStatusActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 2, 1, 1, 4),
    _McmGcmHwStatusActiveLink_Type()
)
mcmGcmHwStatusActiveLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmGcmHwStatusActiveLink.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmGCMPriLinkDownCausedByPhysicalConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 1)
)
mcmGCMPriLinkDownCausedByPhysicalConnection.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGCMPriLinkDownCausedByPhysicalConnection.setStatus(
        ""
    )

mcmGCMPriLinkDownCausedByProtocolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 2)
)
mcmGCMPriLinkDownCausedByProtocolFailure.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGCMPriLinkDownCausedByProtocolFailure.setStatus(
        ""
    )

mcmGcmPriLinkDownCausedByGcmTimerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 3)
)
mcmGcmPriLinkDownCausedByGcmTimerEvent.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmTimerIndex"))
)
if mibBuilder.loadTexts:
    mcmGcmPriLinkDownCausedByGcmTimerEvent.setStatus(
        ""
    )

mcmGcmPriLinkDownCausedByUnknownSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 4)
)
mcmGcmPriLinkDownCausedByUnknownSource.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGcmPriLinkDownCausedByUnknownSource.setStatus(
        ""
    )

mcmGCMBakLinkDownCausedByPhysicalConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 5)
)
mcmGCMBakLinkDownCausedByPhysicalConnection.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGCMBakLinkDownCausedByPhysicalConnection.setStatus(
        ""
    )

mcmGCMBakLinkDownCausedByProtocolFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 6)
)
mcmGCMBakLinkDownCausedByProtocolFailure.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGCMBakLinkDownCausedByProtocolFailure.setStatus(
        ""
    )

mcmGcmBakLinkDownCausedByGcmTimerEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 7)
)
mcmGcmBakLinkDownCausedByGcmTimerEvent.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmTimerIndex"))
)
if mibBuilder.loadTexts:
    mcmGcmBakLinkDownCausedByGcmTimerEvent.setStatus(
        ""
    )

mcmGcmBakLinkDownCausedByUnknownSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 8)
)
mcmGcmBakLinkDownCausedByUnknownSource.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGcmBakLinkDownCausedByUnknownSource.setStatus(
        ""
    )

mcmGcmPriLinkEst = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 9)
)
mcmGcmPriLinkEst.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGcmPriLinkEst.setStatus(
        ""
    )

mcmGcmBakLinkEst = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 10)
)
mcmGcmBakLinkEst.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGcmBakLinkEst.setStatus(
        ""
    )

mcmGcmPriLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 11)
)
mcmGcmPriLinkUp.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGcmPriLinkUp.setStatus(
        ""
    )

mcmGcmBakLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 12)
)
mcmGcmBakLinkUp.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGcmBakLinkUp.setStatus(
        ""
    )

mcmGcmRegionalLinkEst = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 13)
)
mcmGcmRegionalLinkEst.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGcmRegionalLinkEst.setStatus(
        ""
    )

mcmGcmRegionalLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 25, 0, 14)
)
mcmGcmRegionalLinkDown.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-GCM-MIB", "mcmGcmLinkIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkName"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkSigPcmIndex"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoType"),
        ("MICOM-GCM-MIB", "mcmGcmLinkProtoPcmIndex"))
)
if mibBuilder.loadTexts:
    mcmGcmRegionalLinkDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-GCM-MIB",
    **{"micom-gcm": micom_gcm,
       "mcmGCMPriLinkDownCausedByPhysicalConnection": mcmGCMPriLinkDownCausedByPhysicalConnection,
       "mcmGCMPriLinkDownCausedByProtocolFailure": mcmGCMPriLinkDownCausedByProtocolFailure,
       "mcmGcmPriLinkDownCausedByGcmTimerEvent": mcmGcmPriLinkDownCausedByGcmTimerEvent,
       "mcmGcmPriLinkDownCausedByUnknownSource": mcmGcmPriLinkDownCausedByUnknownSource,
       "mcmGCMBakLinkDownCausedByPhysicalConnection": mcmGCMBakLinkDownCausedByPhysicalConnection,
       "mcmGCMBakLinkDownCausedByProtocolFailure": mcmGCMBakLinkDownCausedByProtocolFailure,
       "mcmGcmBakLinkDownCausedByGcmTimerEvent": mcmGcmBakLinkDownCausedByGcmTimerEvent,
       "mcmGcmBakLinkDownCausedByUnknownSource": mcmGcmBakLinkDownCausedByUnknownSource,
       "mcmGcmPriLinkEst": mcmGcmPriLinkEst,
       "mcmGcmBakLinkEst": mcmGcmBakLinkEst,
       "mcmGcmPriLinkUp": mcmGcmPriLinkUp,
       "mcmGcmBakLinkUp": mcmGcmBakLinkUp,
       "mcmGcmRegionalLinkEst": mcmGcmRegionalLinkEst,
       "mcmGcmRegionalLinkDown": mcmGcmRegionalLinkDown,
       "configuration": configuration,
       "mcmGcmGlobalCfgGroup": mcmGcmGlobalCfgGroup,
       "mcmGcmGlobalCfgAdminStatus": mcmGcmGlobalCfgAdminStatus,
       "mcmGcmGlobalCfgTraps": mcmGcmGlobalCfgTraps,
       "mcmGcmGlobalCfgAutoActSelMode": mcmGcmGlobalCfgAutoActSelMode,
       "mcmGcmLinkTable": mcmGcmLinkTable,
       "mcmGcmLinkEntry": mcmGcmLinkEntry,
       "mcmGcmLinkIndex": mcmGcmLinkIndex,
       "mcmGcmLinkUnitIndex": mcmGcmLinkUnitIndex,
       "mcmGcmLinkName": mcmGcmLinkName,
       "mcmGcmLinkSigType": mcmGcmLinkSigType,
       "mcmGcmLinkSigPcmIndex": mcmGcmLinkSigPcmIndex,
       "mcmGcmLinkSigOperStatus": mcmGcmLinkSigOperStatus,
       "mcmGcmLinkProtoType": mcmGcmLinkProtoType,
       "mcmGcmLinkProtoPcmIndex": mcmGcmLinkProtoPcmIndex,
       "mcmGcmLinkProtoStatus": mcmGcmLinkProtoStatus,
       "mcmGcmLinkVoiceCalls": mcmGcmLinkVoiceCalls,
       "mcmGcmUnitTable": mcmGcmUnitTable,
       "mcmGcmUnitEntry": mcmGcmUnitEntry,
       "mcmGcmUnitIndex": mcmGcmUnitIndex,
       "mcmGcmUnitName": mcmGcmUnitName,
       "mcmGcmUnitAdminStatus": mcmGcmUnitAdminStatus,
       "mcmGcmUnitTimerAdminStatus": mcmGcmUnitTimerAdminStatus,
       "mcmGcmUnitSwitchType": mcmGcmUnitSwitchType,
       "mcmGcmUnitSwitchDelay": mcmGcmUnitSwitchDelay,
       "mcmGcmUnitPrimaryLinkIndex": mcmGcmUnitPrimaryLinkIndex,
       "mcmGcmUnitBackupRemainTime": mcmGcmUnitBackupRemainTime,
       "mcmGcmUnitBackupSwitchDelay": mcmGcmUnitBackupSwitchDelay,
       "mcmGcmUnitPrimarySwitchDelay": mcmGcmUnitPrimarySwitchDelay,
       "mcmGcmUnitRegionalLinkIndex": mcmGcmUnitRegionalLinkIndex,
       "mcmGcmUnitModeCfg": mcmGcmUnitModeCfg,
       "mcmGcmUnitPriLinkFailMonStatus": mcmGcmUnitPriLinkFailMonStatus,
       "mcmGcmUnitPriLinkFailMonDurMin": mcmGcmUnitPriLinkFailMonDurMin,
       "mcmGcmUnitPriLinkFailMonThrshld": mcmGcmUnitPriLinkFailMonThrshld,
       "mcmGcmUnitPriLinkFailMonCount": mcmGcmUnitPriLinkFailMonCount,
       "mcmGcmUnitCmd": mcmGcmUnitCmd,
       "mcmGcmBackupCfgTable": mcmGcmBackupCfgTable,
       "mcmGcmBackupCfgEntry": mcmGcmBackupCfgEntry,
       "mcmGcmBackupCfgIndex": mcmGcmBackupCfgIndex,
       "mcmGcmBackupCfgUnitIndex": mcmGcmBackupCfgUnitIndex,
       "mcmGcmBackupCfgLinkIndex": mcmGcmBackupCfgLinkIndex,
       "mcmGcmTimerTable": mcmGcmTimerTable,
       "mcmGcmTimerEntry": mcmGcmTimerEntry,
       "mcmGcmTimerIndex": mcmGcmTimerIndex,
       "mcmGcmTimerUnitIndex": mcmGcmTimerUnitIndex,
       "mcmGcmTimerInactStartHr": mcmGcmTimerInactStartHr,
       "mcmGcmTimerInactStartMin": mcmGcmTimerInactStartMin,
       "mcmGcmTimerInactDurationHr": mcmGcmTimerInactDurationHr,
       "mcmGcmTimerInactDurationMin": mcmGcmTimerInactDurationMin,
       "mcmGcmTimerInactMonday": mcmGcmTimerInactMonday,
       "mcmGcmTimerInactTuesday": mcmGcmTimerInactTuesday,
       "mcmGcmTimerInactWednesday": mcmGcmTimerInactWednesday,
       "mcmGcmTimerInactThursday": mcmGcmTimerInactThursday,
       "mcmGcmTimerInactFriday": mcmGcmTimerInactFriday,
       "mcmGcmTimerInactSaturday": mcmGcmTimerInactSaturday,
       "mcmGcmTimerInactSunday": mcmGcmTimerInactSunday,
       "mcmGcmTimerInactPeriodic": mcmGcmTimerInactPeriodic,
       "nvmGcmGlobalCfgGroup": nvmGcmGlobalCfgGroup,
       "nvmGcmGlobalCfgAdminStatus": nvmGcmGlobalCfgAdminStatus,
       "nvmGcmGlobalCfgTraps": nvmGcmGlobalCfgTraps,
       "nvmGcmGlobalCfgAutoActSelMode": nvmGcmGlobalCfgAutoActSelMode,
       "nvmGcmLinkTable": nvmGcmLinkTable,
       "nvmGcmLinkEntry": nvmGcmLinkEntry,
       "nvmGcmLinkIndex": nvmGcmLinkIndex,
       "nvmGcmLinkUnitIndex": nvmGcmLinkUnitIndex,
       "nvmGcmLinkName": nvmGcmLinkName,
       "nvmGcmLinkSigType": nvmGcmLinkSigType,
       "nvmGcmLinkSigPcmIndex": nvmGcmLinkSigPcmIndex,
       "nvmGcmLinkProtoType": nvmGcmLinkProtoType,
       "nvmGcmLinkProtoPcmIndex": nvmGcmLinkProtoPcmIndex,
       "nvmGcmLinkRowStatus": nvmGcmLinkRowStatus,
       "nvmGcmUnitTable": nvmGcmUnitTable,
       "nvmGcmUnitEntry": nvmGcmUnitEntry,
       "nvmGcmUnitIndex": nvmGcmUnitIndex,
       "nvmGcmUnitName": nvmGcmUnitName,
       "nvmGcmUnitAdminStatus": nvmGcmUnitAdminStatus,
       "nvmGcmUnitTimerAdminStatus": nvmGcmUnitTimerAdminStatus,
       "nvmGcmUnitSwitchType": nvmGcmUnitSwitchType,
       "nvmGcmUnitSwitchDelay": nvmGcmUnitSwitchDelay,
       "nvmGcmUnitPrimaryLinkIndex": nvmGcmUnitPrimaryLinkIndex,
       "nvmGcmUnitBackupRemainTime": nvmGcmUnitBackupRemainTime,
       "nvmGcmUnitBackupSwitchDelay": nvmGcmUnitBackupSwitchDelay,
       "nvmGcmUnitPrimarySwitchDelay": nvmGcmUnitPrimarySwitchDelay,
       "nvmGcmUnitRegionalLinkIndex": nvmGcmUnitRegionalLinkIndex,
       "nvmGcmUnitModeCfg": nvmGcmUnitModeCfg,
       "nvmGcmUnitPriLinkFailMonStatus": nvmGcmUnitPriLinkFailMonStatus,
       "nvmGcmUnitPriLinkFailMonDurMin": nvmGcmUnitPriLinkFailMonDurMin,
       "nvmGcmUnitPriLinkFailMonThrshld": nvmGcmUnitPriLinkFailMonThrshld,
       "nvmGcmBackupCfgTable": nvmGcmBackupCfgTable,
       "nvmGcmBackupCfgEntry": nvmGcmBackupCfgEntry,
       "nvmGcmBackupCfgIndex": nvmGcmBackupCfgIndex,
       "nvmGcmBackupCfgUnitIndex": nvmGcmBackupCfgUnitIndex,
       "nvmGcmBackupCfgLinkIndex": nvmGcmBackupCfgLinkIndex,
       "nvmGcmBackupCfgLinkRowStatus": nvmGcmBackupCfgLinkRowStatus,
       "nvmGcmTimerTable": nvmGcmTimerTable,
       "nvmGcmTimerEntry": nvmGcmTimerEntry,
       "nvmGcmTimerIndex": nvmGcmTimerIndex,
       "nvmGcmTimerUnitIndex": nvmGcmTimerUnitIndex,
       "nvmGcmTimerInactStartHr": nvmGcmTimerInactStartHr,
       "nvmGcmTimerInactStartMin": nvmGcmTimerInactStartMin,
       "nvmGcmTimerInactDurationHr": nvmGcmTimerInactDurationHr,
       "nvmGcmTimerInactDurationMin": nvmGcmTimerInactDurationMin,
       "nvmGcmTimerInactMonday": nvmGcmTimerInactMonday,
       "nvmGcmTimerInactTuesday": nvmGcmTimerInactTuesday,
       "nvmGcmTimerInactWednesday": nvmGcmTimerInactWednesday,
       "nvmGcmTimerInactThursday": nvmGcmTimerInactThursday,
       "nvmGcmTimerInactFriday": nvmGcmTimerInactFriday,
       "nvmGcmTimerInactSaturday": nvmGcmTimerInactSaturday,
       "nvmGcmTimerInactSunday": nvmGcmTimerInactSunday,
       "nvmGcmTimerInactPeriodic": nvmGcmTimerInactPeriodic,
       "nvmGcmTimerRowStatus": nvmGcmTimerRowStatus,
       "status": status,
       "mcmGcmHwStatusTable": mcmGcmHwStatusTable,
       "mcmGcmHwStatusEntry": mcmGcmHwStatusEntry,
       "mcmGcmHwStatusIndex": mcmGcmHwStatusIndex,
       "mcmGcmHwStatusDesc": mcmGcmHwStatusDesc,
       "mcmGcmHwStatusOperStatus": mcmGcmHwStatusOperStatus,
       "mcmGcmHwStatusActiveLink": mcmGcmHwStatusActiveLink}
)
