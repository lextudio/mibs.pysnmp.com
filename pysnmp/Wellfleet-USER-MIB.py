# SNMP MIB module (Wellfleet-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-USER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:22 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfUserServicesGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfUserServicesGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfUserAccess_ObjectIdentity = ObjectIdentity
wfUserAccess = _WfUserAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1)
)


class _WfUserAccessDelete_Type(Integer32):
    """Custom type wfUserAccessDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfUserAccessDelete_Type.__name__ = "Integer32"
_WfUserAccessDelete_Object = MibScalar
wfUserAccessDelete = _WfUserAccessDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 1),
    _WfUserAccessDelete_Type()
)
wfUserAccessDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessDelete.setStatus("mandatory")


class _WfUserAccessConfig_Type(Integer32):
    """Custom type wfUserAccessConfig based on Integer32"""
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


_WfUserAccessConfig_Type.__name__ = "Integer32"
_WfUserAccessConfig_Object = MibScalar
wfUserAccessConfig = _WfUserAccessConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 2),
    _WfUserAccessConfig_Type()
)
wfUserAccessConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessConfig.setStatus("mandatory")


class _WfUserAccessRadius_Type(Integer32):
    """Custom type wfUserAccessRadius based on Integer32"""
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


_WfUserAccessRadius_Type.__name__ = "Integer32"
_WfUserAccessRadius_Object = MibScalar
wfUserAccessRadius = _WfUserAccessRadius_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 3),
    _WfUserAccessRadius_Type()
)
wfUserAccessRadius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessRadius.setStatus("mandatory")


class _WfUserAccessMaxLogin_Type(Integer32):
    """Custom type wfUserAccessMaxLogin based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfUserAccessMaxLogin_Type.__name__ = "Integer32"
_WfUserAccessMaxLogin_Object = MibScalar
wfUserAccessMaxLogin = _WfUserAccessMaxLogin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 4),
    _WfUserAccessMaxLogin_Type()
)
wfUserAccessMaxLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessMaxLogin.setStatus("mandatory")


class _WfUserAccessMinLogin_Type(Integer32):
    """Custom type wfUserAccessMinLogin based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfUserAccessMinLogin_Type.__name__ = "Integer32"
_WfUserAccessMinLogin_Object = MibScalar
wfUserAccessMinLogin = _WfUserAccessMinLogin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 5),
    _WfUserAccessMinLogin_Type()
)
wfUserAccessMinLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessMinLogin.setStatus("mandatory")


class _WfUserAccessMaxGroup_Type(Integer32):
    """Custom type wfUserAccessMaxGroup based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfUserAccessMaxGroup_Type.__name__ = "Integer32"
_WfUserAccessMaxGroup_Object = MibScalar
wfUserAccessMaxGroup = _WfUserAccessMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 6),
    _WfUserAccessMaxGroup_Type()
)
wfUserAccessMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessMaxGroup.setStatus("mandatory")


class _WfUserAccessMinGroup_Type(Integer32):
    """Custom type wfUserAccessMinGroup based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfUserAccessMinGroup_Type.__name__ = "Integer32"
_WfUserAccessMinGroup_Object = MibScalar
wfUserAccessMinGroup = _WfUserAccessMinGroup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 7),
    _WfUserAccessMinGroup_Type()
)
wfUserAccessMinGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessMinGroup.setStatus("mandatory")


class _WfUserAccessMaxPassword_Type(Integer32):
    """Custom type wfUserAccessMaxPassword based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfUserAccessMaxPassword_Type.__name__ = "Integer32"
_WfUserAccessMaxPassword_Object = MibScalar
wfUserAccessMaxPassword = _WfUserAccessMaxPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 8),
    _WfUserAccessMaxPassword_Type()
)
wfUserAccessMaxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessMaxPassword.setStatus("mandatory")


class _WfUserAccessMinPassword_Type(Integer32):
    """Custom type wfUserAccessMinPassword based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfUserAccessMinPassword_Type.__name__ = "Integer32"
_WfUserAccessMinPassword_Object = MibScalar
wfUserAccessMinPassword = _WfUserAccessMinPassword_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 9),
    _WfUserAccessMinPassword_Type()
)
wfUserAccessMinPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessMinPassword.setStatus("mandatory")


class _WfUserManagerLock_Type(Integer32):
    """Custom type wfUserManagerLock based on Integer32"""
    defaultValue = 2

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
          ("serverwait", 3))
    )


_WfUserManagerLock_Type.__name__ = "Integer32"
_WfUserManagerLock_Object = MibScalar
wfUserManagerLock = _WfUserManagerLock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 10),
    _WfUserManagerLock_Type()
)
wfUserManagerLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserManagerLock.setStatus("mandatory")


class _WfUserAccessRadiusAcctEnable_Type(Integer32):
    """Custom type wfUserAccessRadiusAcctEnable based on Integer32"""
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


_WfUserAccessRadiusAcctEnable_Type.__name__ = "Integer32"
_WfUserAccessRadiusAcctEnable_Object = MibScalar
wfUserAccessRadiusAcctEnable = _WfUserAccessRadiusAcctEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 1, 11),
    _WfUserAccessRadiusAcctEnable_Type()
)
wfUserAccessRadiusAcctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessRadiusAcctEnable.setStatus("mandatory")
_WfUserAccessNameTable_Object = MibTable
wfUserAccessNameTable = _WfUserAccessNameTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2)
)
if mibBuilder.loadTexts:
    wfUserAccessNameTable.setStatus("mandatory")
_WfUserAccessNameEntry_Object = MibTableRow
wfUserAccessNameEntry = _WfUserAccessNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1)
)
wfUserAccessNameEntry.setIndexNames(
    (0, "Wellfleet-USER-MIB", "wfUserAccessNameId"),
)
if mibBuilder.loadTexts:
    wfUserAccessNameEntry.setStatus("mandatory")


class _WfUserAccessNameDelete_Type(Integer32):
    """Custom type wfUserAccessNameDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfUserAccessNameDelete_Type.__name__ = "Integer32"
_WfUserAccessNameDelete_Object = MibTableColumn
wfUserAccessNameDelete = _WfUserAccessNameDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 1),
    _WfUserAccessNameDelete_Type()
)
wfUserAccessNameDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessNameDelete.setStatus("mandatory")


class _WfUserAccessNameDisable_Type(Integer32):
    """Custom type wfUserAccessNameDisable based on Integer32"""
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


_WfUserAccessNameDisable_Type.__name__ = "Integer32"
_WfUserAccessNameDisable_Object = MibTableColumn
wfUserAccessNameDisable = _WfUserAccessNameDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 2),
    _WfUserAccessNameDisable_Type()
)
wfUserAccessNameDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessNameDisable.setStatus("mandatory")
_WfUserAccessNameId_Type = DisplayString
_WfUserAccessNameId_Object = MibTableColumn
wfUserAccessNameId = _WfUserAccessNameId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 3),
    _WfUserAccessNameId_Type()
)
wfUserAccessNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessNameId.setStatus("mandatory")
_WfUserAccessNameName_Type = DisplayString
_WfUserAccessNameName_Object = MibTableColumn
wfUserAccessNameName = _WfUserAccessNameName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 4),
    _WfUserAccessNameName_Type()
)
wfUserAccessNameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessNameName.setStatus("mandatory")
_WfUserAccessNamePasswd_Type = DisplayString
_WfUserAccessNamePasswd_Object = MibTableColumn
wfUserAccessNamePasswd = _WfUserAccessNamePasswd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 5),
    _WfUserAccessNamePasswd_Type()
)
wfUserAccessNamePasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessNamePasswd.setStatus("mandatory")
_WfUserAccessNameGroups_Type = Integer32
_WfUserAccessNameGroups_Object = MibTableColumn
wfUserAccessNameGroups = _WfUserAccessNameGroups_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 6),
    _WfUserAccessNameGroups_Type()
)
wfUserAccessNameGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessNameGroups.setStatus("mandatory")


class _WfUserAccessNameAudit_Type(Integer32):
    """Custom type wfUserAccessNameAudit based on Integer32"""
    defaultValue = 1


_WfUserAccessNameAudit_Object = MibTableColumn
wfUserAccessNameAudit = _WfUserAccessNameAudit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 7),
    _WfUserAccessNameAudit_Type()
)
wfUserAccessNameAudit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessNameAudit.setStatus("mandatory")
_WfUserAccessNameScript_Type = DisplayString
_WfUserAccessNameScript_Object = MibTableColumn
wfUserAccessNameScript = _WfUserAccessNameScript_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 2, 1, 8),
    _WfUserAccessNameScript_Type()
)
wfUserAccessNameScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessNameScript.setStatus("mandatory")
_WfUserAccessActiveTable_Object = MibTable
wfUserAccessActiveTable = _WfUserAccessActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3)
)
if mibBuilder.loadTexts:
    wfUserAccessActiveTable.setStatus("mandatory")
_WfUserAccessActiveEntry_Object = MibTableRow
wfUserAccessActiveEntry = _WfUserAccessActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1)
)
wfUserAccessActiveEntry.setIndexNames(
    (0, "Wellfleet-USER-MIB", "wfUserAccessActiveLoginAddress"),
    (0, "Wellfleet-USER-MIB", "wfUserAccessActivePort"),
)
if mibBuilder.loadTexts:
    wfUserAccessActiveEntry.setStatus("mandatory")


class _WfUserAccessActiveDelete_Type(Integer32):
    """Custom type wfUserAccessActiveDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfUserAccessActiveDelete_Type.__name__ = "Integer32"
_WfUserAccessActiveDelete_Object = MibTableColumn
wfUserAccessActiveDelete = _WfUserAccessActiveDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 1),
    _WfUserAccessActiveDelete_Type()
)
wfUserAccessActiveDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessActiveDelete.setStatus("mandatory")


class _WfUserAccessActiveDisable_Type(Integer32):
    """Custom type wfUserAccessActiveDisable based on Integer32"""
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


_WfUserAccessActiveDisable_Type.__name__ = "Integer32"
_WfUserAccessActiveDisable_Object = MibTableColumn
wfUserAccessActiveDisable = _WfUserAccessActiveDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 2),
    _WfUserAccessActiveDisable_Type()
)
wfUserAccessActiveDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessActiveDisable.setStatus("mandatory")
_WfUserAccessActiveId_Type = DisplayString
_WfUserAccessActiveId_Object = MibTableColumn
wfUserAccessActiveId = _WfUserAccessActiveId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 3),
    _WfUserAccessActiveId_Type()
)
wfUserAccessActiveId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveId.setStatus("mandatory")
_WfUserAccessActiveLoginAddress_Type = IpAddress
_WfUserAccessActiveLoginAddress_Object = MibTableColumn
wfUserAccessActiveLoginAddress = _WfUserAccessActiveLoginAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 4),
    _WfUserAccessActiveLoginAddress_Type()
)
wfUserAccessActiveLoginAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveLoginAddress.setStatus("mandatory")
_WfUserAccessActivePort_Type = Integer32
_WfUserAccessActivePort_Object = MibTableColumn
wfUserAccessActivePort = _WfUserAccessActivePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 5),
    _WfUserAccessActivePort_Type()
)
wfUserAccessActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActivePort.setStatus("mandatory")


class _WfUserAccessActiveState_Type(Integer32):
    """Custom type wfUserAccessActiveState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("config", 2),
          ("ftp", 3))
    )


_WfUserAccessActiveState_Type.__name__ = "Integer32"
_WfUserAccessActiveState_Object = MibTableColumn
wfUserAccessActiveState = _WfUserAccessActiveState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 6),
    _WfUserAccessActiveState_Type()
)
wfUserAccessActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveState.setStatus("mandatory")
_WfUserAccessActiveCmd_Type = DisplayString
_WfUserAccessActiveCmd_Object = MibTableColumn
wfUserAccessActiveCmd = _WfUserAccessActiveCmd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 7),
    _WfUserAccessActiveCmd_Type()
)
wfUserAccessActiveCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveCmd.setStatus("mandatory")


class _WfUserAccessActiveLastCmdTime_Type(Integer32):
    """Custom type wfUserAccessActiveLastCmdTime based on Integer32"""
    defaultValue = 0


_WfUserAccessActiveLastCmdTime_Object = MibTableColumn
wfUserAccessActiveLastCmdTime = _WfUserAccessActiveLastCmdTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 8),
    _WfUserAccessActiveLastCmdTime_Type()
)
wfUserAccessActiveLastCmdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveLastCmdTime.setStatus("mandatory")
_WfUserAccessActiveLoginTime_Type = Counter32
_WfUserAccessActiveLoginTime_Object = MibTableColumn
wfUserAccessActiveLoginTime = _WfUserAccessActiveLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 9),
    _WfUserAccessActiveLoginTime_Type()
)
wfUserAccessActiveLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveLoginTime.setStatus("mandatory")
_WfUserAccessActiveAcctInOctets_Type = Counter32
_WfUserAccessActiveAcctInOctets_Object = MibTableColumn
wfUserAccessActiveAcctInOctets = _WfUserAccessActiveAcctInOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 10),
    _WfUserAccessActiveAcctInOctets_Type()
)
wfUserAccessActiveAcctInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveAcctInOctets.setStatus("mandatory")
_WfUserAccessActiveAcctOutOctets_Type = Counter32
_WfUserAccessActiveAcctOutOctets_Object = MibTableColumn
wfUserAccessActiveAcctOutOctets = _WfUserAccessActiveAcctOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 11),
    _WfUserAccessActiveAcctOutOctets_Type()
)
wfUserAccessActiveAcctOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveAcctOutOctets.setStatus("mandatory")


class _WfUserAccessActiveAcctAccessType_Type(Integer32):
    """Custom type wfUserAccessActiveAcctAccessType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("ftp", 3),
          ("telnet", 2))
    )


_WfUserAccessActiveAcctAccessType_Type.__name__ = "Integer32"
_WfUserAccessActiveAcctAccessType_Object = MibTableColumn
wfUserAccessActiveAcctAccessType = _WfUserAccessActiveAcctAccessType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 12),
    _WfUserAccessActiveAcctAccessType_Type()
)
wfUserAccessActiveAcctAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveAcctAccessType.setStatus("mandatory")


class _WfUserAccessActiveAcctTermCause_Type(Integer32):
    """Custom type wfUserAccessActiveAcctTermCause based on Integer32"""
    defaultValue = 0


_WfUserAccessActiveAcctTermCause_Object = MibTableColumn
wfUserAccessActiveAcctTermCause = _WfUserAccessActiveAcctTermCause_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 13),
    _WfUserAccessActiveAcctTermCause_Type()
)
wfUserAccessActiveAcctTermCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveAcctTermCause.setStatus("mandatory")


class _WfUserAccessActiveAcctServiceType_Type(Integer32):
    """Custom type wfUserAccessActiveAcctServiceType based on Integer32"""
    defaultValue = 0


_WfUserAccessActiveAcctServiceType_Object = MibTableColumn
wfUserAccessActiveAcctServiceType = _WfUserAccessActiveAcctServiceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 14),
    _WfUserAccessActiveAcctServiceType_Type()
)
wfUserAccessActiveAcctServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveAcctServiceType.setStatus("mandatory")


class _WfUserAccessActiveAcctNasPortType_Type(Integer32):
    """Custom type wfUserAccessActiveAcctNasPortType based on Integer32"""
    defaultValue = 0


_WfUserAccessActiveAcctNasPortType_Object = MibTableColumn
wfUserAccessActiveAcctNasPortType = _WfUserAccessActiveAcctNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 15),
    _WfUserAccessActiveAcctNasPortType_Type()
)
wfUserAccessActiveAcctNasPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveAcctNasPortType.setStatus("mandatory")


class _WfUserAccessActiveAcctPriv_Type(Integer32):
    """Custom type wfUserAccessActiveAcctPriv based on Integer32"""
    defaultValue = 0


_WfUserAccessActiveAcctPriv_Object = MibTableColumn
wfUserAccessActiveAcctPriv = _WfUserAccessActiveAcctPriv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 3, 1, 16),
    _WfUserAccessActiveAcctPriv_Type()
)
wfUserAccessActiveAcctPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessActiveAcctPriv.setStatus("mandatory")
_WfUserAccessGroupTable_Object = MibTable
wfUserAccessGroupTable = _WfUserAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4)
)
if mibBuilder.loadTexts:
    wfUserAccessGroupTable.setStatus("mandatory")
_WfUserAccessGroupEntry_Object = MibTableRow
wfUserAccessGroupEntry = _WfUserAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1)
)
wfUserAccessGroupEntry.setIndexNames(
    (0, "Wellfleet-USER-MIB", "wfUserAccessGroupNumber"),
)
if mibBuilder.loadTexts:
    wfUserAccessGroupEntry.setStatus("mandatory")


class _WfUserAccessGroupDelete_Type(Integer32):
    """Custom type wfUserAccessGroupDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfUserAccessGroupDelete_Type.__name__ = "Integer32"
_WfUserAccessGroupDelete_Object = MibTableColumn
wfUserAccessGroupDelete = _WfUserAccessGroupDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 1),
    _WfUserAccessGroupDelete_Type()
)
wfUserAccessGroupDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessGroupDelete.setStatus("mandatory")


class _WfUserAccessGroupDisable_Type(Integer32):
    """Custom type wfUserAccessGroupDisable based on Integer32"""
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


_WfUserAccessGroupDisable_Type.__name__ = "Integer32"
_WfUserAccessGroupDisable_Object = MibTableColumn
wfUserAccessGroupDisable = _WfUserAccessGroupDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 2),
    _WfUserAccessGroupDisable_Type()
)
wfUserAccessGroupDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessGroupDisable.setStatus("mandatory")
_WfUserAccessGroupNumber_Type = Integer32
_WfUserAccessGroupNumber_Object = MibTableColumn
wfUserAccessGroupNumber = _WfUserAccessGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 3),
    _WfUserAccessGroupNumber_Type()
)
wfUserAccessGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserAccessGroupNumber.setStatus("mandatory")
_WfUserAccessGroupName_Type = DisplayString
_WfUserAccessGroupName_Object = MibTableColumn
wfUserAccessGroupName = _WfUserAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 4),
    _WfUserAccessGroupName_Type()
)
wfUserAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessGroupName.setStatus("mandatory")


class _WfUserAccessGroupPriv_Type(Integer32):
    """Custom type wfUserAccessGroupPriv based on Integer32"""
    defaultValue = 2


_WfUserAccessGroupPriv_Object = MibTableColumn
wfUserAccessGroupPriv = _WfUserAccessGroupPriv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 5),
    _WfUserAccessGroupPriv_Type()
)
wfUserAccessGroupPriv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessGroupPriv.setStatus("mandatory")


class _WfUserAccessGroupAudit_Type(Integer32):
    """Custom type wfUserAccessGroupAudit based on Integer32"""
    defaultValue = 2


_WfUserAccessGroupAudit_Object = MibTableColumn
wfUserAccessGroupAudit = _WfUserAccessGroupAudit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 4, 1, 6),
    _WfUserAccessGroupAudit_Type()
)
wfUserAccessGroupAudit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAccessGroupAudit.setStatus("mandatory")
_WfUserAudit_ObjectIdentity = ObjectIdentity
wfUserAudit = _WfUserAudit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 5)
)


class _WfUserAuditDelete_Type(Integer32):
    """Custom type wfUserAuditDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfUserAuditDelete_Type.__name__ = "Integer32"
_WfUserAuditDelete_Object = MibScalar
wfUserAuditDelete = _WfUserAuditDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 5, 1),
    _WfUserAuditDelete_Type()
)
wfUserAuditDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAuditDelete.setStatus("mandatory")


class _WfUserAuditDisable_Type(Integer32):
    """Custom type wfUserAuditDisable based on Integer32"""
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


_WfUserAuditDisable_Type.__name__ = "Integer32"
_WfUserAuditDisable_Object = MibScalar
wfUserAuditDisable = _WfUserAuditDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 5, 2),
    _WfUserAuditDisable_Type()
)
wfUserAuditDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAuditDisable.setStatus("mandatory")


class _WfUserAuditlevel_Type(Integer32):
    """Custom type wfUserAuditlevel based on Integer32"""
    defaultValue = 1


_WfUserAuditlevel_Object = MibScalar
wfUserAuditlevel = _WfUserAuditlevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 5, 3),
    _WfUserAuditlevel_Type()
)
wfUserAuditlevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserAuditlevel.setStatus("mandatory")
_WfUserBccLock_ObjectIdentity = ObjectIdentity
wfUserBccLock = _WfUserBccLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6)
)


class _WfUserBccLockDelete_Type(Integer32):
    """Custom type wfUserBccLockDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfUserBccLockDelete_Type.__name__ = "Integer32"
_WfUserBccLockDelete_Object = MibScalar
wfUserBccLockDelete = _WfUserBccLockDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6, 1),
    _WfUserBccLockDelete_Type()
)
wfUserBccLockDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserBccLockDelete.setStatus("mandatory")


class _WfUserBccLockId_Type(Integer32):
    """Custom type wfUserBccLockId based on Integer32"""
    defaultValue = 0


_WfUserBccLockId_Object = MibScalar
wfUserBccLockId = _WfUserBccLockId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6, 2),
    _WfUserBccLockId_Type()
)
wfUserBccLockId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserBccLockId.setStatus("mandatory")


class _WfUserBccLockTimer_Type(Integer32):
    """Custom type wfUserBccLockTimer based on Integer32"""
    defaultValue = 0


_WfUserBccLockTimer_Object = MibScalar
wfUserBccLockTimer = _WfUserBccLockTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6, 3),
    _WfUserBccLockTimer_Type()
)
wfUserBccLockTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserBccLockTimer.setStatus("mandatory")


class _WfUserBccLockAddress_Type(Integer32):
    """Custom type wfUserBccLockAddress based on Integer32"""
    defaultValue = 0


_WfUserBccLockAddress_Object = MibScalar
wfUserBccLockAddress = _WfUserBccLockAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6, 4),
    _WfUserBccLockAddress_Type()
)
wfUserBccLockAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserBccLockAddress.setStatus("mandatory")


class _WfUserBccLockPort_Type(Integer32):
    """Custom type wfUserBccLockPort based on Integer32"""
    defaultValue = 0


_WfUserBccLockPort_Object = MibScalar
wfUserBccLockPort = _WfUserBccLockPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 6, 5),
    _WfUserBccLockPort_Type()
)
wfUserBccLockPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserBccLockPort.setStatus("mandatory")
_WfUserBccConfig_ObjectIdentity = ObjectIdentity
wfUserBccConfig = _WfUserBccConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 7)
)


class _WfUserBccConfigDelete_Type(Integer32):
    """Custom type wfUserBccConfigDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfUserBccConfigDelete_Type.__name__ = "Integer32"
_WfUserBccConfigDelete_Object = MibScalar
wfUserBccConfigDelete = _WfUserBccConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 7, 1),
    _WfUserBccConfigDelete_Type()
)
wfUserBccConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserBccConfigDelete.setStatus("mandatory")


class _WfUserBccConfigDefaultShell_Type(Integer32):
    """Custom type wfUserBccConfigDefaultShell based on Integer32"""
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


_WfUserBccConfigDefaultShell_Type.__name__ = "Integer32"
_WfUserBccConfigDefaultShell_Object = MibScalar
wfUserBccConfigDefaultShell = _WfUserBccConfigDefaultShell_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 22, 7, 2),
    _WfUserBccConfigDefaultShell_Type()
)
wfUserBccConfigDefaultShell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUserBccConfigDefaultShell.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-USER-MIB",
    **{"wfUserAccess": wfUserAccess,
       "wfUserAccessDelete": wfUserAccessDelete,
       "wfUserAccessConfig": wfUserAccessConfig,
       "wfUserAccessRadius": wfUserAccessRadius,
       "wfUserAccessMaxLogin": wfUserAccessMaxLogin,
       "wfUserAccessMinLogin": wfUserAccessMinLogin,
       "wfUserAccessMaxGroup": wfUserAccessMaxGroup,
       "wfUserAccessMinGroup": wfUserAccessMinGroup,
       "wfUserAccessMaxPassword": wfUserAccessMaxPassword,
       "wfUserAccessMinPassword": wfUserAccessMinPassword,
       "wfUserManagerLock": wfUserManagerLock,
       "wfUserAccessRadiusAcctEnable": wfUserAccessRadiusAcctEnable,
       "wfUserAccessNameTable": wfUserAccessNameTable,
       "wfUserAccessNameEntry": wfUserAccessNameEntry,
       "wfUserAccessNameDelete": wfUserAccessNameDelete,
       "wfUserAccessNameDisable": wfUserAccessNameDisable,
       "wfUserAccessNameId": wfUserAccessNameId,
       "wfUserAccessNameName": wfUserAccessNameName,
       "wfUserAccessNamePasswd": wfUserAccessNamePasswd,
       "wfUserAccessNameGroups": wfUserAccessNameGroups,
       "wfUserAccessNameAudit": wfUserAccessNameAudit,
       "wfUserAccessNameScript": wfUserAccessNameScript,
       "wfUserAccessActiveTable": wfUserAccessActiveTable,
       "wfUserAccessActiveEntry": wfUserAccessActiveEntry,
       "wfUserAccessActiveDelete": wfUserAccessActiveDelete,
       "wfUserAccessActiveDisable": wfUserAccessActiveDisable,
       "wfUserAccessActiveId": wfUserAccessActiveId,
       "wfUserAccessActiveLoginAddress": wfUserAccessActiveLoginAddress,
       "wfUserAccessActivePort": wfUserAccessActivePort,
       "wfUserAccessActiveState": wfUserAccessActiveState,
       "wfUserAccessActiveCmd": wfUserAccessActiveCmd,
       "wfUserAccessActiveLastCmdTime": wfUserAccessActiveLastCmdTime,
       "wfUserAccessActiveLoginTime": wfUserAccessActiveLoginTime,
       "wfUserAccessActiveAcctInOctets": wfUserAccessActiveAcctInOctets,
       "wfUserAccessActiveAcctOutOctets": wfUserAccessActiveAcctOutOctets,
       "wfUserAccessActiveAcctAccessType": wfUserAccessActiveAcctAccessType,
       "wfUserAccessActiveAcctTermCause": wfUserAccessActiveAcctTermCause,
       "wfUserAccessActiveAcctServiceType": wfUserAccessActiveAcctServiceType,
       "wfUserAccessActiveAcctNasPortType": wfUserAccessActiveAcctNasPortType,
       "wfUserAccessActiveAcctPriv": wfUserAccessActiveAcctPriv,
       "wfUserAccessGroupTable": wfUserAccessGroupTable,
       "wfUserAccessGroupEntry": wfUserAccessGroupEntry,
       "wfUserAccessGroupDelete": wfUserAccessGroupDelete,
       "wfUserAccessGroupDisable": wfUserAccessGroupDisable,
       "wfUserAccessGroupNumber": wfUserAccessGroupNumber,
       "wfUserAccessGroupName": wfUserAccessGroupName,
       "wfUserAccessGroupPriv": wfUserAccessGroupPriv,
       "wfUserAccessGroupAudit": wfUserAccessGroupAudit,
       "wfUserAudit": wfUserAudit,
       "wfUserAuditDelete": wfUserAuditDelete,
       "wfUserAuditDisable": wfUserAuditDisable,
       "wfUserAuditlevel": wfUserAuditlevel,
       "wfUserBccLock": wfUserBccLock,
       "wfUserBccLockDelete": wfUserBccLockDelete,
       "wfUserBccLockId": wfUserBccLockId,
       "wfUserBccLockTimer": wfUserBccLockTimer,
       "wfUserBccLockAddress": wfUserBccLockAddress,
       "wfUserBccLockPort": wfUserBccLockPort,
       "wfUserBccConfig": wfUserBccConfig,
       "wfUserBccConfigDelete": wfUserBccConfigDelete,
       "wfUserBccConfigDefaultShell": wfUserBccConfigDefaultShell}
)
