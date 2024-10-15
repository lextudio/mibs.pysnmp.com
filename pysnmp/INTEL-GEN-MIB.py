# SNMP MIB module (INTEL-GEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-GEN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:31 2024
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

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_SysProducts_ObjectIdentity = ObjectIdentity
sysProducts = _SysProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5)
)
_Switches_ObjectIdentity = ObjectIdentity
switches = _Switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1)
)
_Express10_ObjectIdentity = ObjectIdentity
express10 = _Express10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 1)
)
_Express10plus_ObjectIdentity = ObjectIdentity
express10plus = _Express10plus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 2)
)
_Express100fx_ObjectIdentity = ObjectIdentity
express100fx = _Express100fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 3)
)
_Express550t_ObjectIdentity = ObjectIdentity
express550t = _Express550t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 4)
)
_Express550f_ObjectIdentity = ObjectIdentity
express550f = _Express550f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 5)
)
_Express510t_ObjectIdentity = ObjectIdentity
express510t = _Express510t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 6)
)
_Express520t_ObjectIdentity = ObjectIdentity
express520t = _Express520t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 7)
)
_ExpressGigaSwitch_ObjectIdentity = ObjectIdentity
expressGigaSwitch = _ExpressGigaSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 8)
)
_Express460t_16_ObjectIdentity = ObjectIdentity
express460t_16 = _Express460t_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 9)
)
_Express460t_24_ObjectIdentity = ObjectIdentity
express460t_24 = _Express460t_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 10)
)
_Nstructure560t_ObjectIdentity = ObjectIdentity
nstructure560t = _Nstructure560t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 11)
)
_Nstructure560tr_ObjectIdentity = ObjectIdentity
nstructure560tr = _Nstructure560tr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 13)
)
_Nstructure560fr_ObjectIdentity = ObjectIdentity
nstructure560fr = _Nstructure560fr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 1, 14)
)
_Routers_ObjectIdentity = ObjectIdentity
routers = _Routers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2)
)
_Express9100_ObjectIdentity = ObjectIdentity
express9100 = _Express9100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 1)
)
_Express920x_ObjectIdentity = ObjectIdentity
express920x = _Express920x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 2)
)
_Express9300_ObjectIdentity = ObjectIdentity
express9300 = _Express9300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 3)
)
_Express9400_ObjectIdentity = ObjectIdentity
express9400 = _Express9400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 4)
)
_Express8100st_ObjectIdentity = ObjectIdentity
express8100st = _Express8100st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 5)
)
_Express8100u_ObjectIdentity = ObjectIdentity
express8100u = _Express8100u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 6)
)
_Express8100x_ObjectIdentity = ObjectIdentity
express8100x = _Express8100x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 7)
)
_Express8100fr_ObjectIdentity = ObjectIdentity
express8100fr = _Express8100fr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 8)
)
_Express9520st_ObjectIdentity = ObjectIdentity
express9520st = _Express9520st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 9)
)
_Express9520u_ObjectIdentity = ObjectIdentity
express9520u = _Express9520u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 10)
)
_Express9510st_ObjectIdentity = ObjectIdentity
express9510st = _Express9510st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 11)
)
_Express9510u_ObjectIdentity = ObjectIdentity
express9510u = _Express9510u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 12)
)
_Express9515st_ObjectIdentity = ObjectIdentity
express9515st = _Express9515st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 13)
)
_Express9515u_ObjectIdentity = ObjectIdentity
express9515u = _Express9515u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 14)
)
_Express9525st_ObjectIdentity = ObjectIdentity
express9525st = _Express9525st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 15)
)
_Express9525u_ObjectIdentity = ObjectIdentity
express9525u = _Express9525u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 16)
)
_Express8210_ObjectIdentity = ObjectIdentity
express8210 = _Express8210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 17)
)
_Express8220_ObjectIdentity = ObjectIdentity
express8220 = _Express8220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 18)
)
_Express9530_ObjectIdentity = ObjectIdentity
express9530 = _Express9530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 19)
)
_Express9535_ObjectIdentity = ObjectIdentity
express9535 = _Express9535_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 20)
)
_Express9545st_ObjectIdentity = ObjectIdentity
express9545st = _Express9545st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 21)
)
_Express9545u_ObjectIdentity = ObjectIdentity
express9545u = _Express9545u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 22)
)
_Express8100wV4_ObjectIdentity = ObjectIdentity
express8100wV4 = _Express8100wV4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 23)
)
_Express8100stV4_ObjectIdentity = ObjectIdentity
express8100stV4 = _Express8100stV4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 27)
)
_Express8100uV4_ObjectIdentity = ObjectIdentity
express8100uV4 = _Express8100uV4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 2, 28)
)
_Hubs_ObjectIdentity = ObjectIdentity
hubs = _Hubs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 3)
)
_Express110_12_ObjectIdentity = ObjectIdentity
express110_12 = _Express110_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 3, 1)
)
_Express110_24_ObjectIdentity = ObjectIdentity
express110_24 = _Express110_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 3, 2)
)
_Express210_12_ObjectIdentity = ObjectIdentity
express210_12 = _Express210_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 3, 3)
)
_Express210_24_ObjectIdentity = ObjectIdentity
express210_24 = _Express210_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 3, 4)
)
_Express220_12_ObjectIdentity = ObjectIdentity
express220_12 = _Express220_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 3, 5)
)
_Express220_24_ObjectIdentity = ObjectIdentity
express220_24 = _Express220_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 3, 6)
)
_Express330_16_ObjectIdentity = ObjectIdentity
express330_16 = _Express330_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 3, 7)
)
_Express330_24_ObjectIdentity = ObjectIdentity
express330_24 = _Express330_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 3, 8)
)
_Stacks_ObjectIdentity = ObjectIdentity
stacks = _Stacks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 4)
)
_Nstructure560_ObjectIdentity = ObjectIdentity
nstructure560 = _Nstructure560_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 4, 1)
)
_Nstructure560s_ObjectIdentity = ObjectIdentity
nstructure560s = _Nstructure560s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 4, 1, 1)
)
_Nstructure560l3s_ObjectIdentity = ObjectIdentity
nstructure560l3s = _Nstructure560l3s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 5, 4, 1, 2)
)
_Mib2ext_ObjectIdentity = ObjectIdentity
mib2ext = _Mib2ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 1)
)


class _SysVendorName_Type(DisplayString):
    """Custom type sysVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_SysVendorName_Type.__name__ = "DisplayString"
_SysVendorName_Object = MibScalar
sysVendorName = _SysVendorName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 1),
    _SysVendorName_Type()
)
sysVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVendorName.setStatus("mandatory")


class _SysProductName_Type(DisplayString):
    """Custom type sysProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_SysProductName_Type.__name__ = "DisplayString"
_SysProductName_Object = MibScalar
sysProductName = _SysProductName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 2),
    _SysProductName_Type()
)
sysProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductName.setStatus("mandatory")


class _SysProductSubType_Type(DisplayString):
    """Custom type sysProductSubType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_SysProductSubType_Type.__name__ = "DisplayString"
_SysProductSubType_Object = MibScalar
sysProductSubType = _SysProductSubType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 3),
    _SysProductSubType_Type()
)
sysProductSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductSubType.setStatus("mandatory")


class _SysMibVersion_Type(DisplayString):
    """Custom type sysMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SysMibVersion_Type.__name__ = "DisplayString"
_SysMibVersion_Object = MibScalar
sysMibVersion = _SysMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 4),
    _SysMibVersion_Type()
)
sysMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMibVersion.setStatus("mandatory")
_SysTimeOfDay_Type = Integer32
_SysTimeOfDay_Object = MibScalar
sysTimeOfDay = _SysTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 5),
    _SysTimeOfDay_Type()
)
sysTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeOfDay.setStatus("mandatory")


class _SysSystemDate_Type(OctetString):
    """Custom type sysSystemDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_SysSystemDate_Type.__name__ = "OctetString"
_SysSystemDate_Object = MibScalar
sysSystemDate = _SysSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 6),
    _SysSystemDate_Type()
)
sysSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSystemDate.setStatus("optional")


class _SysReset_Type(Integer32):
    """Custom type sysReset based on Integer32"""
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
        *(("resetCold", 1),
          ("resetStackCold", 3),
          ("resetStackWarm", 4),
          ("resetWarm", 2))
    )


_SysReset_Type.__name__ = "Integer32"
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 7),
    _SysReset_Type()
)
sysReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sysReset.setStatus("mandatory")
_SysConfTable_Object = MibTable
sysConfTable = _SysConfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 8)
)
if mibBuilder.loadTexts:
    sysConfTable.setStatus("mandatory")
_SysConfEntry_Object = MibTableRow
sysConfEntry = _SysConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 8, 1)
)
sysConfEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    sysConfEntry.setStatus("mandatory")


class _ConfStatus_Type(Integer32):
    """Custom type confStatus based on Integer32"""
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
        *(("changed", 4),
          ("default", 2),
          ("loaded", 3),
          ("saved", 5),
          ("unknown", 1))
    )


_ConfStatus_Type.__name__ = "Integer32"
_ConfStatus_Object = MibTableColumn
confStatus = _ConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 8, 1, 1),
    _ConfStatus_Type()
)
confStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confStatus.setStatus("mandatory")


class _ConfName_Type(OctetString):
    """Custom type confName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ConfName_Type.__name__ = "OctetString"
_ConfName_Object = MibTableColumn
confName = _ConfName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 8, 1, 2),
    _ConfName_Type()
)
confName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confName.setStatus("mandatory")
_ConfTime_Type = Integer32
_ConfTime_Object = MibTableColumn
confTime = _ConfTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 8, 1, 3),
    _ConfTime_Type()
)
confTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confTime.setStatus("mandatory")
_ConfTftpIp_Type = IpAddress
_ConfTftpIp_Object = MibTableColumn
confTftpIp = _ConfTftpIp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 8, 1, 4),
    _ConfTftpIp_Type()
)
confTftpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confTftpIp.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 8, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")


class _SysConfChange_Type(Integer32):
    """Custom type sysConfChange based on Integer32"""
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
        *(("createBackupConf", 4),
          ("createDefBackupConf", 5),
          ("createStackBackupConf", 7),
          ("stackCreateDefBackupConf", 14),
          ("stackTftpUploadKeepAlive", 11),
          ("stackTftpUploadLock", 8),
          ("stackTftpUploadUnlockActivate", 9),
          ("stackTftpUploadUnlockCancel", 10),
          ("stackUseDefaultConf", 12),
          ("stackUseDefaultConfKeepIp", 13),
          ("useBackupConf", 3),
          ("useDefaultConf", 1),
          ("useDefaultConfKeepIp", 2),
          ("useStackBackupConf", 6))
    )


_SysConfChange_Type.__name__ = "Integer32"
_SysConfChange_Object = MibScalar
sysConfChange = _SysConfChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 9),
    _SysConfChange_Type()
)
sysConfChange.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sysConfChange.setStatus("mandatory")
_SysLogTable_Object = MibTable
sysLogTable = _SysLogTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 10)
)
if mibBuilder.loadTexts:
    sysLogTable.setStatus("mandatory")
_SysLogEntry_Object = MibTableRow
sysLogEntry = _SysLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 10, 1)
)
sysLogEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "logType"),
)
if mibBuilder.loadTexts:
    sysLogEntry.setStatus("mandatory")


class _LogType_Type(Integer32):
    """Custom type logType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("logError", 2),
          ("logSystem", 1))
    )


_LogType_Type.__name__ = "Integer32"
_LogType_Object = MibTableColumn
logType = _LogType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 10, 1, 1),
    _LogType_Type()
)
logType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logType.setStatus("mandatory")
_LogEntries_Type = Integer32
_LogEntries_Object = MibTableColumn
logEntries = _LogEntries_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 10, 1, 2),
    _LogEntries_Type()
)
logEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logEntries.setStatus("mandatory")


class _LogFileName_Type(DisplayString):
    """Custom type logFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_LogFileName_Type.__name__ = "DisplayString"
_LogFileName_Object = MibTableColumn
logFileName = _LogFileName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 10, 1, 3),
    _LogFileName_Type()
)
logFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFileName.setStatus("mandatory")
_LogLastChanged_Type = TimeTicks
_LogLastChanged_Object = MibTableColumn
logLastChanged = _LogLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 10, 1, 4),
    _LogLastChanged_Type()
)
logLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logLastChanged.setStatus("mandatory")
_SysConfRollbackTimeout_Type = Integer32
_SysConfRollbackTimeout_Object = MibScalar
sysConfRollbackTimeout = _SysConfRollbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 11),
    _SysConfRollbackTimeout_Type()
)
sysConfRollbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfRollbackTimeout.setStatus("mandatory")


class _SysConfChangeLastResponse_Type(Integer32):
    """Custom type sysConfChangeLastResponse based on Integer32"""
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
              16,
              17,
              99)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefaultOperationFailed", 12),
          ("flashOperationFailed", 4),
          ("flashOperationNothingToLoad", 5),
          ("internalError", 17),
          ("intraStackCommunicationError", 16),
          ("noEditingRightsLocalParm", 3),
          ("noEditingRightsVlan", 2),
          ("notReady", 99),
          ("stackMemberRejectsOperation", 13),
          ("success", 1),
          ("tftpOperationFailed", 6),
          ("tftpOperationMgtTimeout", 11),
          ("tftpOperationMissingNvpFile", 10),
          ("tftpOperationMissingParmFile", 9),
          ("tftpOperationNoLock", 7),
          ("tftpOperationStackMemberMissingParmFile", 8))
    )


_SysConfChangeLastResponse_Type.__name__ = "Integer32"
_SysConfChangeLastResponse_Object = MibScalar
sysConfChangeLastResponse = _SysConfChangeLastResponse_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 12),
    _SysConfChangeLastResponse_Type()
)
sysConfChangeLastResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfChangeLastResponse.setStatus("mandatory")
_SysLocalMangementTimeout_Type = Integer32
_SysLocalMangementTimeout_Object = MibScalar
sysLocalMangementTimeout = _SysLocalMangementTimeout_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 1, 13),
    _SysLocalMangementTimeout_Type()
)
sysLocalMangementTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocalMangementTimeout.setStatus("mandatory")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 2)
)
_IpConfTable_Object = MibTable
ipConfTable = _IpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 1)
)
if mibBuilder.loadTexts:
    ipConfTable.setStatus("mandatory")
_IpConfEntry_Object = MibTableRow
ipConfEntry = _IpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 1, 1)
)
ipConfEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    ipConfEntry.setStatus("mandatory")


class _IpAddressAssignment_Type(Integer32):
    """Custom type ipAddressAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("fixed", 1))
    )


_IpAddressAssignment_Type.__name__ = "Integer32"
_IpAddressAssignment_Object = MibTableColumn
ipAddressAssignment = _IpAddressAssignment_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 1, 1, 1),
    _IpAddressAssignment_Type()
)
ipAddressAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddressAssignment.setStatus("mandatory")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibTableColumn
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 1, 1, 2),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("mandatory")
_IpSubNetMask_Type = IpAddress
_IpSubNetMask_Object = MibTableColumn
ipSubNetMask = _IpSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 1, 1, 3),
    _IpSubNetMask_Type()
)
ipSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSubNetMask.setStatus("mandatory")
_IpRouterAddress_Type = IpAddress
_IpRouterAddress_Object = MibTableColumn
ipRouterAddress = _IpRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 1, 1, 4),
    _IpRouterAddress_Type()
)
ipRouterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouterAddress.setStatus("mandatory")
_IpBroadcastAddress_Type = IpAddress
_IpBroadcastAddress_Object = MibTableColumn
ipBroadcastAddress = _IpBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 1, 1, 5),
    _IpBroadcastAddress_Type()
)
ipBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBroadcastAddress.setStatus("mandatory")
_IpBootpServerAddress_Type = IpAddress
_IpBootpServerAddress_Object = MibTableColumn
ipBootpServerAddress = _IpBootpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 1, 1, 6),
    _IpBootpServerAddress_Type()
)
ipBootpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBootpServerAddress.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 1, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")


class _IpConf2Activate_Type(Integer32):
    """Custom type ipConf2Activate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_IpConf2Activate_Type.__name__ = "Integer32"
_IpConf2Activate_Object = MibScalar
ipConf2Activate = _IpConf2Activate_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 2),
    _IpConf2Activate_Type()
)
ipConf2Activate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ipConf2Activate.setStatus("mandatory")
_IpModuleConfTable_Object = MibTable
ipModuleConfTable = _IpModuleConfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3)
)
if mibBuilder.loadTexts:
    ipModuleConfTable.setStatus("optional")
_IpModuleConfEntry_Object = MibTableRow
ipModuleConfEntry = _IpModuleConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3, 1)
)
ipModuleConfEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "ipModuleChassisIndex"),
    (0, "INTEL-GEN-MIB", "ipModuleModuleIndex"),
    (0, "INTEL-GEN-MIB", "ipModuleConfigIndex"),
)
if mibBuilder.loadTexts:
    ipModuleConfEntry.setStatus("mandatory")
_IpModuleChassisIndex_Type = Integer32
_IpModuleChassisIndex_Object = MibTableColumn
ipModuleChassisIndex = _IpModuleChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3, 1, 1),
    _IpModuleChassisIndex_Type()
)
ipModuleChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipModuleChassisIndex.setStatus("mandatory")
_IpModuleModuleIndex_Type = Integer32
_IpModuleModuleIndex_Object = MibTableColumn
ipModuleModuleIndex = _IpModuleModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3, 1, 2),
    _IpModuleModuleIndex_Type()
)
ipModuleModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipModuleModuleIndex.setStatus("mandatory")
_IpModuleConfigIndex_Type = Integer32
_IpModuleConfigIndex_Object = MibTableColumn
ipModuleConfigIndex = _IpModuleConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3, 1, 3),
    _IpModuleConfigIndex_Type()
)
ipModuleConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipModuleConfigIndex.setStatus("mandatory")


class _IpModuleAddressAssignment_Type(Integer32):
    """Custom type ipModuleAddressAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("fixed", 1))
    )


_IpModuleAddressAssignment_Type.__name__ = "Integer32"
_IpModuleAddressAssignment_Object = MibTableColumn
ipModuleAddressAssignment = _IpModuleAddressAssignment_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3, 1, 4),
    _IpModuleAddressAssignment_Type()
)
ipModuleAddressAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipModuleAddressAssignment.setStatus("mandatory")
_IpModuleAddress_Type = IpAddress
_IpModuleAddress_Object = MibTableColumn
ipModuleAddress = _IpModuleAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3, 1, 5),
    _IpModuleAddress_Type()
)
ipModuleAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipModuleAddress.setStatus("mandatory")
_IpModuleSubNetMask_Type = IpAddress
_IpModuleSubNetMask_Object = MibTableColumn
ipModuleSubNetMask = _IpModuleSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3, 1, 6),
    _IpModuleSubNetMask_Type()
)
ipModuleSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipModuleSubNetMask.setStatus("mandatory")
_IpModuleRouterAddress_Type = IpAddress
_IpModuleRouterAddress_Object = MibTableColumn
ipModuleRouterAddress = _IpModuleRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3, 1, 7),
    _IpModuleRouterAddress_Type()
)
ipModuleRouterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipModuleRouterAddress.setStatus("mandatory")
_IpModuleBroadcastAddress_Type = IpAddress
_IpModuleBroadcastAddress_Object = MibTableColumn
ipModuleBroadcastAddress = _IpModuleBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3, 1, 8),
    _IpModuleBroadcastAddress_Type()
)
ipModuleBroadcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipModuleBroadcastAddress.setStatus("mandatory")
_IpModuleBootpServerAddress_Type = IpAddress
_IpModuleBootpServerAddress_Object = MibTableColumn
ipModuleBootpServerAddress = _IpModuleBootpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 3, 1, 9),
    _IpModuleBootpServerAddress_Type()
)
ipModuleBootpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipModuleBootpServerAddress.setStatus("mandatory")


class _IpModuleConf2Activate_Type(Integer32):
    """Custom type ipModuleConf2Activate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_IpModuleConf2Activate_Type.__name__ = "Integer32"
_IpModuleConf2Activate_Object = MibScalar
ipModuleConf2Activate = _IpModuleConf2Activate_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 4),
    _IpModuleConf2Activate_Type()
)
ipModuleConf2Activate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ipModuleConf2Activate.setStatus("optional")


class _IpModuleConf2Confirm_Type(Integer32):
    """Custom type ipModuleConf2Confirm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("confirm", 1)
    )


_IpModuleConf2Confirm_Type.__name__ = "Integer32"
_IpModuleConf2Confirm_Object = MibScalar
ipModuleConf2Confirm = _IpModuleConf2Confirm_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 2, 5),
    _IpModuleConf2Confirm_Type()
)
ipModuleConf2Confirm.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ipModuleConf2Confirm.setStatus("optional")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 3)
)
_SnmpAuthMaxEntries_Type = Integer32
_SnmpAuthMaxEntries_Object = MibScalar
snmpAuthMaxEntries = _SnmpAuthMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 1),
    _SnmpAuthMaxEntries_Type()
)
snmpAuthMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAuthMaxEntries.setStatus("mandatory")
_SnmpAuthTableLastChange_Type = TimeTicks
_SnmpAuthTableLastChange_Object = MibScalar
snmpAuthTableLastChange = _SnmpAuthTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 2),
    _SnmpAuthTableLastChange_Type()
)
snmpAuthTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAuthTableLastChange.setStatus("mandatory")
_SnmpAuthTable_Object = MibTable
snmpAuthTable = _SnmpAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 3)
)
if mibBuilder.loadTexts:
    snmpAuthTable.setStatus("mandatory")
_SnmpAuthEntry_Object = MibTableRow
snmpAuthEntry = _SnmpAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 3, 1)
)
snmpAuthEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "authNumber"),
)
if mibBuilder.loadTexts:
    snmpAuthEntry.setStatus("mandatory")
_AuthNumber_Type = Integer32
_AuthNumber_Object = MibTableColumn
authNumber = _AuthNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 3, 1, 1),
    _AuthNumber_Type()
)
authNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authNumber.setStatus("mandatory")


class _AuthProtocolAccessIpCommunity_Type(OctetString):
    """Custom type authProtocolAccessIpCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 41),
    )


_AuthProtocolAccessIpCommunity_Type.__name__ = "OctetString"
_AuthProtocolAccessIpCommunity_Object = MibTableColumn
authProtocolAccessIpCommunity = _AuthProtocolAccessIpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 3, 1, 2),
    _AuthProtocolAccessIpCommunity_Type()
)
authProtocolAccessIpCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authProtocolAccessIpCommunity.setStatus("mandatory")


class _AuthDelete_Type(Integer32):
    """Custom type authDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_AuthDelete_Type.__name__ = "Integer32"
_AuthDelete_Object = MibTableColumn
authDelete = _AuthDelete_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 3, 1, 3),
    _AuthDelete_Type()
)
authDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    authDelete.setStatus("mandatory")
_SnmpTrapMaxEntries_Type = Integer32
_SnmpTrapMaxEntries_Object = MibScalar
snmpTrapMaxEntries = _SnmpTrapMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 4),
    _SnmpTrapMaxEntries_Type()
)
snmpTrapMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapMaxEntries.setStatus("mandatory")
_SnmpTrapTable_Object = MibTable
snmpTrapTable = _SnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 5)
)
if mibBuilder.loadTexts:
    snmpTrapTable.setStatus("mandatory")
_SnmpTrapEntry_Object = MibTableRow
snmpTrapEntry = _SnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 5, 1)
)
snmpTrapEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "trapNumber"),
)
if mibBuilder.loadTexts:
    snmpTrapEntry.setStatus("mandatory")
_TrapNumber_Type = Integer32
_TrapNumber_Object = MibTableColumn
trapNumber = _TrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 5, 1, 1),
    _TrapNumber_Type()
)
trapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNumber.setStatus("mandatory")


class _TrapIpAndGroupAndCommunity_Type(OctetString):
    """Custom type trapIpAndGroupAndCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 39),
    )


_TrapIpAndGroupAndCommunity_Type.__name__ = "OctetString"
_TrapIpAndGroupAndCommunity_Object = MibTableColumn
trapIpAndGroupAndCommunity = _TrapIpAndGroupAndCommunity_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 5, 1, 2),
    _TrapIpAndGroupAndCommunity_Type()
)
trapIpAndGroupAndCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIpAndGroupAndCommunity.setStatus("mandatory")


class _TrapDelete_Type(Integer32):
    """Custom type trapDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_TrapDelete_Type.__name__ = "Integer32"
_TrapDelete_Object = MibTableColumn
trapDelete = _TrapDelete_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 5, 1, 3),
    _TrapDelete_Type()
)
trapDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    trapDelete.setStatus("mandatory")
_SnmpAccessTable_Object = MibTable
snmpAccessTable = _SnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 6)
)
if mibBuilder.loadTexts:
    snmpAccessTable.setStatus("mandatory")
_SnmpAccessEntry_Object = MibTableRow
snmpAccessEntry = _SnmpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 6, 1)
)
snmpAccessEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "pysmiFakeCol3"),
)
if mibBuilder.loadTexts:
    snmpAccessEntry.setStatus("mandatory")
_SnmpAccessIP_Type = IpAddress
_SnmpAccessIP_Object = MibTableColumn
snmpAccessIP = _SnmpAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 6, 1, 1),
    _SnmpAccessIP_Type()
)
snmpAccessIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAccessIP.setStatus("mandatory")
_SnmpAccessTime_Type = Integer32
_SnmpAccessTime_Object = MibTableColumn
snmpAccessTime = _SnmpAccessTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 6, 1, 2),
    _SnmpAccessTime_Type()
)
snmpAccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAccessTime.setStatus("mandatory")


class _SnmpAccessProtocol_Type(Integer32):
    """Custom type snmpAccessProtocol based on Integer32"""
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
        *(("ftp", 5),
          ("http", 3),
          ("snmp", 1),
          ("telnet", 2),
          ("tftp", 4))
    )


_SnmpAccessProtocol_Type.__name__ = "Integer32"
_SnmpAccessProtocol_Object = MibTableColumn
snmpAccessProtocol = _SnmpAccessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 6, 1, 3),
    _SnmpAccessProtocol_Type()
)
snmpAccessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAccessProtocol.setStatus("mandatory")


class _SnmpAccessType_Type(Integer32):
    """Custom type snmpAccessType based on Integer32"""
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
        *(("noAccess", 1),
          ("readOnly", 2),
          ("readOnlySecureSNMPObjects", 5),
          ("readWrite", 4),
          ("readWriteSecureSNMPObjects", 6),
          ("writeOnly", 3))
    )


_SnmpAccessType_Type.__name__ = "Integer32"
_SnmpAccessType_Object = MibTableColumn
snmpAccessType = _SnmpAccessType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 6, 1, 4),
    _SnmpAccessType_Type()
)
snmpAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAccessType.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 6, 1, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")
_Hw_ObjectIdentity = ObjectIdentity
hw = _Hw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7)
)
_Stack_ObjectIdentity = ObjectIdentity
stack = _Stack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 1)
)


class _StackClass_Type(Integer32):
    """Custom type stackClass based on Integer32"""
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
        *(("chassis", 2),
          ("multiagentstack", 3),
          ("singleagentstack", 4),
          ("standalone", 1))
    )


_StackClass_Type.__name__ = "Integer32"
_StackClass_Object = MibScalar
stackClass = _StackClass_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 1, 1),
    _StackClass_Type()
)
stackClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackClass.setStatus("mandatory")
_StackMaxChassis_Type = Integer32
_StackMaxChassis_Object = MibScalar
stackMaxChassis = _StackMaxChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 1, 2),
    _StackMaxChassis_Type()
)
stackMaxChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackMaxChassis.setStatus("mandatory")
_StackChassis_Type = Integer32
_StackChassis_Object = MibScalar
stackChassis = _StackChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 1, 3),
    _StackChassis_Type()
)
stackChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackChassis.setStatus("mandatory")
_StackAgentChassis_Type = Integer32
_StackAgentChassis_Object = MibScalar
stackAgentChassis = _StackAgentChassis_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 1, 4),
    _StackAgentChassis_Type()
)
stackAgentChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackAgentChassis.setStatus("mandatory")
_StackAgentModule_Type = Integer32
_StackAgentModule_Object = MibScalar
stackAgentModule = _StackAgentModule_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 1, 5),
    _StackAgentModule_Type()
)
stackAgentModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackAgentModule.setStatus("mandatory")


class _StackUserAssignedName_Type(DisplayString):
    """Custom type stackUserAssignedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_StackUserAssignedName_Type.__name__ = "DisplayString"
_StackUserAssignedName_Object = MibScalar
stackUserAssignedName = _StackUserAssignedName_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 1, 6),
    _StackUserAssignedName_Type()
)
stackUserAssignedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackUserAssignedName.setStatus("mandatory")


class _StackID_Type(OctetString):
    """Custom type stackID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_StackID_Type.__name__ = "OctetString"
_StackID_Object = MibScalar
stackID = _StackID_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 1, 7),
    _StackID_Type()
)
stackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackID.setStatus("optional")


class _StackTopology_Type(Integer32):
    """Custom type stackTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chain", 1),
          ("star", 2),
          ("tree", 3))
    )


_StackTopology_Type.__name__ = "Integer32"
_StackTopology_Object = MibScalar
stackTopology = _StackTopology_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 1, 8),
    _StackTopology_Type()
)
stackTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackTopology.setStatus("optional")


class _StackMultiAgentDefultChassisModule_Type(OctetString):
    """Custom type stackMultiAgentDefultChassisModule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_StackMultiAgentDefultChassisModule_Type.__name__ = "OctetString"
_StackMultiAgentDefultChassisModule_Object = MibScalar
stackMultiAgentDefultChassisModule = _StackMultiAgentDefultChassisModule_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 1, 9),
    _StackMultiAgentDefultChassisModule_Type()
)
stackMultiAgentDefultChassisModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackMultiAgentDefultChassisModule.setStatus("mandatory")
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 2)
)
_ChassisTable_Object = MibTable
chassisTable = _ChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 1)
)
if mibBuilder.loadTexts:
    chassisTable.setStatus("mandatory")
_ChassisEntry_Object = MibTableRow
chassisEntry = _ChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 1, 1)
)
chassisEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "chassisIndex"),
)
if mibBuilder.loadTexts:
    chassisEntry.setStatus("mandatory")
_ChassisIndex_Type = Integer32
_ChassisIndex_Object = MibTableColumn
chassisIndex = _ChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 1, 1, 1),
    _ChassisIndex_Type()
)
chassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIndex.setStatus("mandatory")


class _ChassisType_Type(Integer32):
    """Custom type chassisType based on Integer32"""
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
        *(("campus8fx", 3),
          ("campus8tx", 2),
          ("desktop16tx", 8),
          ("desktop24tx", 4),
          ("stackable12tx", 5),
          ("stackable16tx", 7),
          ("stackable24tx", 6),
          ("unavailable", 1))
    )


_ChassisType_Type.__name__ = "Integer32"
_ChassisType_Object = MibTableColumn
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 1, 1, 2),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("mandatory")
_ChassisMaxModules_Type = Integer32
_ChassisMaxModules_Object = MibTableColumn
chassisMaxModules = _ChassisMaxModules_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 1, 1, 3),
    _ChassisMaxModules_Type()
)
chassisMaxModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMaxModules.setStatus("mandatory")
_ChassisModules_Type = Integer32
_ChassisModules_Object = MibTableColumn
chassisModules = _ChassisModules_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 1, 1, 4),
    _ChassisModules_Type()
)
chassisModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisModules.setStatus("mandatory")


class _ChassisUserAssignedType_Type(DisplayString):
    """Custom type chassisUserAssignedType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ChassisUserAssignedType_Type.__name__ = "DisplayString"
_ChassisUserAssignedType_Object = MibTableColumn
chassisUserAssignedType = _ChassisUserAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 1, 1, 5),
    _ChassisUserAssignedType_Type()
)
chassisUserAssignedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisUserAssignedType.setStatus("mandatory")


class _ChassisUserAssignedNumber_Type(DisplayString):
    """Custom type chassisUserAssignedNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ChassisUserAssignedNumber_Type.__name__ = "DisplayString"
_ChassisUserAssignedNumber_Object = MibTableColumn
chassisUserAssignedNumber = _ChassisUserAssignedNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 1, 1, 6),
    _ChassisUserAssignedNumber_Type()
)
chassisUserAssignedNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisUserAssignedNumber.setStatus("mandatory")


class _ChassisUserAssignedName_Type(DisplayString):
    """Custom type chassisUserAssignedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ChassisUserAssignedName_Type.__name__ = "DisplayString"
_ChassisUserAssignedName_Object = MibTableColumn
chassisUserAssignedName = _ChassisUserAssignedName_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 1, 1, 7),
    _ChassisUserAssignedName_Type()
)
chassisUserAssignedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisUserAssignedName.setStatus("mandatory")
_ChassisMaxPSUs_Type = Integer32
_ChassisMaxPSUs_Object = MibTableColumn
chassisMaxPSUs = _ChassisMaxPSUs_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 1, 1, 8),
    _ChassisMaxPSUs_Type()
)
chassisMaxPSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMaxPSUs.setStatus("mandatory")
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 3)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("mandatory")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1)
)
moduleEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "moduleChassisIndex"),
    (0, "INTEL-GEN-MIB", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("mandatory")
_ModuleChassisIndex_Type = Integer32
_ModuleChassisIndex_Object = MibTableColumn
moduleChassisIndex = _ModuleChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 1),
    _ModuleChassisIndex_Type()
)
moduleChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleChassisIndex.setStatus("mandatory")
_ModuleIndex_Type = Integer32
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 2),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("mandatory")


class _ModuleType_Type(Integer32):
    """Custom type moduleType based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("express110bridge", 23),
          ("express110management", 22),
          ("express110managementWithRMON", 24),
          ("express110p12", 20),
          ("express110p24", 21),
          ("express210p12", 25),
          ("express210p24", 26),
          ("express220p12", 27),
          ("express220p24", 28),
          ("express300fxuplink", 33),
          ("express300management", 31),
          ("express300txuplink", 32),
          ("express330p16", 29),
          ("express330p24", 30),
          ("express460tp16", 34),
          ("express460tp24", 35),
          ("express510t", 4),
          ("express550f", 3),
          ("express550t", 2),
          ("express8100fr", 8),
          ("express8100st", 5),
          ("express8100u", 6),
          ("express8100x", 7),
          ("nstructure560fr", 39),
          ("nstructure560t", 36),
          ("nstructure560tr", 38),
          ("unavailable", 1))
    )


_ModuleType_Type.__name__ = "Integer32"
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 3),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("mandatory")
_ModuleFirstPort_Type = Integer32
_ModuleFirstPort_Object = MibTableColumn
moduleFirstPort = _ModuleFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 4),
    _ModuleFirstPort_Type()
)
moduleFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFirstPort.setStatus("mandatory")
_ModuleNumberOfPorts_Type = Integer32
_ModuleNumberOfPorts_Object = MibTableColumn
moduleNumberOfPorts = _ModuleNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 5),
    _ModuleNumberOfPorts_Type()
)
moduleNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumberOfPorts.setStatus("mandatory")
_ModuleMaxMediaModules_Type = Integer32
_ModuleMaxMediaModules_Object = MibTableColumn
moduleMaxMediaModules = _ModuleMaxMediaModules_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 6),
    _ModuleMaxMediaModules_Type()
)
moduleMaxMediaModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleMaxMediaModules.setStatus("mandatory")


class _ModuleUserAssignedType_Type(DisplayString):
    """Custom type moduleUserAssignedType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ModuleUserAssignedType_Type.__name__ = "DisplayString"
_ModuleUserAssignedType_Object = MibTableColumn
moduleUserAssignedType = _ModuleUserAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 7),
    _ModuleUserAssignedType_Type()
)
moduleUserAssignedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleUserAssignedType.setStatus("mandatory")


class _ModuleUserAssignedNumber_Type(DisplayString):
    """Custom type moduleUserAssignedNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ModuleUserAssignedNumber_Type.__name__ = "DisplayString"
_ModuleUserAssignedNumber_Object = MibTableColumn
moduleUserAssignedNumber = _ModuleUserAssignedNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 8),
    _ModuleUserAssignedNumber_Type()
)
moduleUserAssignedNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleUserAssignedNumber.setStatus("mandatory")


class _ModuleUserAssignedName_Type(DisplayString):
    """Custom type moduleUserAssignedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ModuleUserAssignedName_Type.__name__ = "DisplayString"
_ModuleUserAssignedName_Object = MibTableColumn
moduleUserAssignedName = _ModuleUserAssignedName_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 9),
    _ModuleUserAssignedName_Type()
)
moduleUserAssignedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleUserAssignedName.setStatus("mandatory")
_ModuleRAM_Type = Integer32
_ModuleRAM_Object = MibTableColumn
moduleRAM = _ModuleRAM_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 10),
    _ModuleRAM_Type()
)
moduleRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleRAM.setStatus("mandatory")
_ModuleEPROM_Type = Integer32
_ModuleEPROM_Object = MibTableColumn
moduleEPROM = _ModuleEPROM_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 11),
    _ModuleEPROM_Type()
)
moduleEPROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEPROM.setStatus("mandatory")
_ModuleFLASHPROM_Type = Integer32
_ModuleFLASHPROM_Object = MibTableColumn
moduleFLASHPROM = _ModuleFLASHPROM_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 12),
    _ModuleFLASHPROM_Type()
)
moduleFLASHPROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFLASHPROM.setStatus("mandatory")


class _ModuleLEDInfo_Type(OctetString):
    """Custom type moduleLEDInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_ModuleLEDInfo_Type.__name__ = "OctetString"
_ModuleLEDInfo_Object = MibTableColumn
moduleLEDInfo = _ModuleLEDInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 13),
    _ModuleLEDInfo_Type()
)
moduleLEDInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleLEDInfo.setStatus("mandatory")
_ModuleAllPortType_Type = OctetString
_ModuleAllPortType_Object = MibTableColumn
moduleAllPortType = _ModuleAllPortType_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 14),
    _ModuleAllPortType_Type()
)
moduleAllPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAllPortType.setStatus("mandatory")
_ModuleAllPortLEDInfo_Type = OctetString
_ModuleAllPortLEDInfo_Object = MibTableColumn
moduleAllPortLEDInfo = _ModuleAllPortLEDInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 15),
    _ModuleAllPortLEDInfo_Type()
)
moduleAllPortLEDInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAllPortLEDInfo.setStatus("mandatory")
_ModuleAllPortStatus_Type = OctetString
_ModuleAllPortStatus_Object = MibTableColumn
moduleAllPortStatus = _ModuleAllPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 16),
    _ModuleAllPortStatus_Type()
)
moduleAllPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAllPortStatus.setStatus("mandatory")
_ModuleLastPortChange_Type = TimeTicks
_ModuleLastPortChange_Object = MibTableColumn
moduleLastPortChange = _ModuleLastPortChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 17),
    _ModuleLastPortChange_Type()
)
moduleLastPortChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleLastPortChange.setStatus("mandatory")


class _ModuleMacAddress_Type(OctetString):
    """Custom type moduleMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ModuleMacAddress_Type.__name__ = "OctetString"
_ModuleMacAddress_Object = MibTableColumn
moduleMacAddress = _ModuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 18),
    _ModuleMacAddress_Type()
)
moduleMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleMacAddress.setStatus("mandatory")
_ModuleIpAddress_Type = IpAddress
_ModuleIpAddress_Object = MibTableColumn
moduleIpAddress = _ModuleIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 19),
    _ModuleIpAddress_Type()
)
moduleIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIpAddress.setStatus("mandatory")


class _ModuleSerialNumber_Type(DisplayString):
    """Custom type moduleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModuleSerialNumber_Type.__name__ = "DisplayString"
_ModuleSerialNumber_Object = MibTableColumn
moduleSerialNumber = _ModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 20),
    _ModuleSerialNumber_Type()
)
moduleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSerialNumber.setStatus("mandatory")
_ModuleVersion_Type = Integer32
_ModuleVersion_Object = MibTableColumn
moduleVersion = _ModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 21),
    _ModuleVersion_Type()
)
moduleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVersion.setStatus("mandatory")


class _ModuleSwStatus_Type(Integer32):
    """Custom type moduleSwStatus based on Integer32"""
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
        *(("approved", 4),
          ("experimental", 5),
          ("nosoftware", 2),
          ("notsupported", 1),
          ("unavailable", 3))
    )


_ModuleSwStatus_Type.__name__ = "Integer32"
_ModuleSwStatus_Object = MibTableColumn
moduleSwStatus = _ModuleSwStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 22),
    _ModuleSwStatus_Type()
)
moduleSwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSwStatus.setStatus("mandatory")


class _ModuleSwName_Type(OctetString):
    """Custom type moduleSwName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ModuleSwName_Type.__name__ = "OctetString"
_ModuleSwName_Object = MibTableColumn
moduleSwName = _ModuleSwName_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 23),
    _ModuleSwName_Type()
)
moduleSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwName.setStatus("mandatory")
_ModuleSwDescription_Type = DisplayString
_ModuleSwDescription_Object = MibTableColumn
moduleSwDescription = _ModuleSwDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 24),
    _ModuleSwDescription_Type()
)
moduleSwDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwDescription.setStatus("mandatory")
_ModuleSwLoadTime_Type = Integer32
_ModuleSwLoadTime_Object = MibTableColumn
moduleSwLoadTime = _ModuleSwLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 25),
    _ModuleSwLoadTime_Type()
)
moduleSwLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwLoadTime.setStatus("mandatory")
_ModuleSwTftpIp_Type = IpAddress
_ModuleSwTftpIp_Object = MibTableColumn
moduleSwTftpIp = _ModuleSwTftpIp_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 26),
    _ModuleSwTftpIp_Type()
)
moduleSwTftpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwTftpIp.setStatus("mandatory")


class _ModuleBackupSwStatus_Type(Integer32):
    """Custom type moduleBackupSwStatus based on Integer32"""
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
        *(("approved", 4),
          ("experimental", 5),
          ("nosoftware", 2),
          ("notsupported", 1),
          ("unavailable", 3))
    )


_ModuleBackupSwStatus_Type.__name__ = "Integer32"
_ModuleBackupSwStatus_Object = MibTableColumn
moduleBackupSwStatus = _ModuleBackupSwStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 27),
    _ModuleBackupSwStatus_Type()
)
moduleBackupSwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSwStatus.setStatus("mandatory")


class _ModuleBackupSwName_Type(OctetString):
    """Custom type moduleBackupSwName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ModuleBackupSwName_Type.__name__ = "OctetString"
_ModuleBackupSwName_Object = MibTableColumn
moduleBackupSwName = _ModuleBackupSwName_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 28),
    _ModuleBackupSwName_Type()
)
moduleBackupSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSwName.setStatus("mandatory")
_ModuleBackupSwDescription_Type = DisplayString
_ModuleBackupSwDescription_Object = MibTableColumn
moduleBackupSwDescription = _ModuleBackupSwDescription_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 29),
    _ModuleBackupSwDescription_Type()
)
moduleBackupSwDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSwDescription.setStatus("mandatory")
_ModuleBackupSwLoadTime_Type = Integer32
_ModuleBackupSwLoadTime_Object = MibTableColumn
moduleBackupSwLoadTime = _ModuleBackupSwLoadTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 30),
    _ModuleBackupSwLoadTime_Type()
)
moduleBackupSwLoadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSwLoadTime.setStatus("mandatory")
_ModuleBackupSwTftpIp_Type = IpAddress
_ModuleBackupSwTftpIp_Object = MibTableColumn
moduleBackupSwTftpIp = _ModuleBackupSwTftpIp_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 31),
    _ModuleBackupSwTftpIp_Type()
)
moduleBackupSwTftpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSwTftpIp.setStatus("mandatory")


class _ModuleSwTftpIpAndSwName_Type(OctetString):
    """Custom type moduleSwTftpIpAndSwName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 260),
    )


_ModuleSwTftpIpAndSwName_Type.__name__ = "OctetString"
_ModuleSwTftpIpAndSwName_Object = MibTableColumn
moduleSwTftpIpAndSwName = _ModuleSwTftpIpAndSwName_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 32),
    _ModuleSwTftpIpAndSwName_Type()
)
moduleSwTftpIpAndSwName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleSwTftpIpAndSwName.setStatus("mandatory")


class _ModuleSwUpdateResult_Type(Integer32):
    """Custom type moduleSwUpdateResult based on Integer32"""
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
        *(("errorMoreFlash", 7),
          ("errorMoreRAM", 8),
          ("errorNoSoftware", 5),
          ("errorNoTftpServer", 4),
          ("errorSoftwareMismatch", 6),
          ("errorUnknown", 3),
          ("noError", 1),
          ("swUpdateRunning", 2))
    )


_ModuleSwUpdateResult_Type.__name__ = "Integer32"
_ModuleSwUpdateResult_Object = MibTableColumn
moduleSwUpdateResult = _ModuleSwUpdateResult_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 33),
    _ModuleSwUpdateResult_Type()
)
moduleSwUpdateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwUpdateResult.setStatus("mandatory")


class _ModuleSpecificObject_Type(OctetString):
    """Custom type moduleSpecificObject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ModuleSpecificObject_Type.__name__ = "OctetString"
_ModuleSpecificObject_Object = MibTableColumn
moduleSpecificObject = _ModuleSpecificObject_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 34),
    _ModuleSpecificObject_Type()
)
moduleSpecificObject.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    moduleSpecificObject.setStatus("mandatory")


class _ModuleTemperatureStatus_Type(Integer32):
    """Custom type moduleTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("high", 2),
          ("normal", 1),
          ("unavailable", 99))
    )


_ModuleTemperatureStatus_Type.__name__ = "Integer32"
_ModuleTemperatureStatus_Object = MibTableColumn
moduleTemperatureStatus = _ModuleTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 35),
    _ModuleTemperatureStatus_Type()
)
moduleTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTemperatureStatus.setStatus("optional")
_ModuleBootSectionVersion_Type = Integer32
_ModuleBootSectionVersion_Object = MibTableColumn
moduleBootSectionVersion = _ModuleBootSectionVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 1, 1, 36),
    _ModuleBootSectionVersion_Type()
)
moduleBootSectionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBootSectionVersion.setStatus("mandatory")
_Mediamodules_ObjectIdentity = ObjectIdentity
mediamodules = _Mediamodules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 4)
)
_MediaModuleTable_Object = MibTable
mediaModuleTable = _MediaModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 1)
)
if mibBuilder.loadTexts:
    mediaModuleTable.setStatus("mandatory")
_MediaModuleEntry_Object = MibTableRow
mediaModuleEntry = _MediaModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 1, 1)
)
mediaModuleEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "mediaModuleChassisIndex"),
    (0, "INTEL-GEN-MIB", "mediaModuleModuleIndex"),
    (0, "INTEL-GEN-MIB", "mediaModuleIndex"),
)
if mibBuilder.loadTexts:
    mediaModuleEntry.setStatus("mandatory")
_MediaModuleChassisIndex_Type = Integer32
_MediaModuleChassisIndex_Object = MibTableColumn
mediaModuleChassisIndex = _MediaModuleChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 1, 1, 1),
    _MediaModuleChassisIndex_Type()
)
mediaModuleChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaModuleChassisIndex.setStatus("mandatory")
_MediaModuleModuleIndex_Type = Integer32
_MediaModuleModuleIndex_Object = MibTableColumn
mediaModuleModuleIndex = _MediaModuleModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 1, 1, 2),
    _MediaModuleModuleIndex_Type()
)
mediaModuleModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaModuleModuleIndex.setStatus("mandatory")
_MediaModuleIndex_Type = Integer32
_MediaModuleIndex_Object = MibTableColumn
mediaModuleIndex = _MediaModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 1, 1, 3),
    _MediaModuleIndex_Type()
)
mediaModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaModuleIndex.setStatus("mandatory")


class _MediaModuleType_Type(Integer32):
    """Custom type mediaModuleType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("mediaModule1000bt", 13),
          ("mediaModule1atmmm", 9),
          ("mediaModule1atmsm", 10),
          ("mediaModule1atmutp", 11),
          ("mediaModule1lx", 12),
          ("mediaModule1lxSMM", 8),
          ("mediaModule1sx", 5),
          ("mediaModule1sxSMM", 7),
          ("mediaModule2fx", 3),
          ("mediaModule4tx", 2),
          ("mediaModuleMMM", 6),
          ("mediaModuleSMM", 4),
          ("unavailable", 1))
    )


_MediaModuleType_Type.__name__ = "Integer32"
_MediaModuleType_Object = MibTableColumn
mediaModuleType = _MediaModuleType_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 1, 1, 4),
    _MediaModuleType_Type()
)
mediaModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaModuleType.setStatus("mandatory")
_MediaModuleFirstPort_Type = Integer32
_MediaModuleFirstPort_Object = MibTableColumn
mediaModuleFirstPort = _MediaModuleFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 1, 1, 5),
    _MediaModuleFirstPort_Type()
)
mediaModuleFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaModuleFirstPort.setStatus("mandatory")
_MediaModuleNumberOfPorts_Type = Integer32
_MediaModuleNumberOfPorts_Object = MibTableColumn
mediaModuleNumberOfPorts = _MediaModuleNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 1, 1, 6),
    _MediaModuleNumberOfPorts_Type()
)
mediaModuleNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaModuleNumberOfPorts.setStatus("mandatory")
_MediaModuleVersion_Type = Integer32
_MediaModuleVersion_Object = MibTableColumn
mediaModuleVersion = _MediaModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 1, 1, 7),
    _MediaModuleVersion_Type()
)
mediaModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaModuleVersion.setStatus("mandatory")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 5)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1)
)
portEntry.setIndexNames(
    (0, "INTEL-GEN-MIB", "portChassisIndex"),
    (0, "INTEL-GEN-MIB", "portModuleIndex"),
    (0, "INTEL-GEN-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortChassisIndex_Type = Integer32
_PortChassisIndex_Object = MibTableColumn
portChassisIndex = _PortChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 1),
    _PortChassisIndex_Type()
)
portChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChassisIndex.setStatus("mandatory")
_PortModuleIndex_Type = Integer32
_PortModuleIndex_Object = MibTableColumn
portModuleIndex = _PortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 2),
    _PortModuleIndex_Type()
)
portModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleIndex.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 3),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")
_PortMediaModuleIndex_Type = Integer32
_PortMediaModuleIndex_Object = MibTableColumn
portMediaModuleIndex = _PortMediaModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 4),
    _PortMediaModuleIndex_Type()
)
portMediaModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaModuleIndex.setStatus("mandatory")
_PortIfIndex_Type = Integer32
_PortIfIndex_Object = MibTableColumn
portIfIndex = _PortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 5),
    _PortIfIndex_Type()
)
portIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIfIndex.setStatus("mandatory")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("console", 16),
          ("core", 6),
          ("csu", 15),
          ("fomm", 2),
          ("fosm", 3),
          ("gigabaselx", 18),
          ("gigabasesx", 17),
          ("gigabasesxlx", 10),
          ("gigabaset", 19),
          ("hundredbasefx", 5),
          ("hundredbasetx", 4),
          ("isdnST", 9),
          ("isdnU", 8),
          ("oc3mm", 12),
          ("oc3sm", 13),
          ("serialwan", 7),
          ("tenbasetx", 11),
          ("tpfd", 1),
          ("utp5", 14))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 6),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("mandatory")
_PortStatus_Type = Integer32
_PortStatus_Object = MibTableColumn
portStatus = _PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 7),
    _PortStatus_Type()
)
portStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatus.setStatus("mandatory")
_PortLEDInfo_Type = OctetString
_PortLEDInfo_Object = MibTableColumn
portLEDInfo = _PortLEDInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 8),
    _PortLEDInfo_Type()
)
portLEDInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLEDInfo.setStatus("mandatory")
_PortTimeSinceLastStateChange_Type = TimeTicks
_PortTimeSinceLastStateChange_Object = MibTableColumn
portTimeSinceLastStateChange = _PortTimeSinceLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 9),
    _PortTimeSinceLastStateChange_Type()
)
portTimeSinceLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTimeSinceLastStateChange.setStatus("mandatory")


class _PortResetAllCounters_Type(Integer32):
    """Custom type portResetAllCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 2),
          ("reset", 1))
    )


_PortResetAllCounters_Type.__name__ = "Integer32"
_PortResetAllCounters_Object = MibTableColumn
portResetAllCounters = _PortResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 10),
    _PortResetAllCounters_Type()
)
portResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portResetAllCounters.setStatus("mandatory")


class _PortReset_Type(Integer32):
    """Custom type portReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("holdinreset", 3),
          ("notreset", 2),
          ("reset", 1))
    )


_PortReset_Type.__name__ = "Integer32"
_PortReset_Object = MibTableColumn
portReset = _PortReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 11),
    _PortReset_Type()
)
portReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReset.setStatus("mandatory")


class _PortLastErrorID_Type(Integer32):
    """Custom type portLastErrorID based on Integer32"""
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
        *(("badPhy", 2),
          ("jabberSeen", 5),
          ("noError", 1),
          ("partition", 6),
          ("polarity", 3),
          ("reserved1", 7),
          ("reserved2", 8),
          ("wrongSpeedLP", 4))
    )


_PortLastErrorID_Type.__name__ = "Integer32"
_PortLastErrorID_Object = MibTableColumn
portLastErrorID = _PortLastErrorID_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 12),
    _PortLastErrorID_Type()
)
portLastErrorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLastErrorID.setStatus("mandatory")


class _PortUserAssignedName_Type(DisplayString):
    """Custom type portUserAssignedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortUserAssignedName_Type.__name__ = "DisplayString"
_PortUserAssignedName_Object = MibTableColumn
portUserAssignedName = _PortUserAssignedName_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 5, 1, 1, 13),
    _PortUserAssignedName_Type()
)
portUserAssignedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portUserAssignedName.setStatus("mandatory")
_Stackext_ObjectIdentity = ObjectIdentity
stackext = _Stackext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 11)
)
_Chassisext_ObjectIdentity = ObjectIdentity
chassisext = _Chassisext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 12)
)
_Modulesext_ObjectIdentity = ObjectIdentity
modulesext = _Modulesext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 13)
)
_Mediamodulesext_ObjectIdentity = ObjectIdentity
mediamodulesext = _Mediamodulesext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 14)
)
_Portsext_ObjectIdentity = ObjectIdentity
portsext = _Portsext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 15)
)

# Managed Objects groups


# Notification objects

snmpAuthViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 0, 1)
)
snmpAuthViolation.setObjects(
      *(("INTEL-GEN-MIB", "snmpAccessIP"),
        ("INTEL-GEN-MIB", "snmpAccessTime"),
        ("INTEL-GEN-MIB", "snmpAccessProtocol"),
        ("INTEL-GEN-MIB", "snmpAccessType"))
)
if mibBuilder.loadTexts:
    snmpAuthViolation.setStatus(
        ""
    )

snmpLoginViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 3, 0, 2)
)
snmpLoginViolation.setObjects(
      *(("INTEL-GEN-MIB", "snmpAccessIP"),
        ("INTEL-GEN-MIB", "snmpAccessTime"),
        ("INTEL-GEN-MIB", "snmpAccessProtocol"),
        ("INTEL-GEN-MIB", "snmpAccessType"))
)
if mibBuilder.loadTexts:
    snmpLoginViolation.setStatus(
        ""
    )

chassisInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 0, 1)
)
chassisInserted.setObjects(
    ("INTEL-GEN-MIB", "chassisIndex")
)
if mibBuilder.loadTexts:
    chassisInserted.setStatus(
        ""
    )

chassisRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 7, 2, 0, 2)
)
chassisRemoved.setObjects(
    ("INTEL-GEN-MIB", "chassisIndex")
)
if mibBuilder.loadTexts:
    chassisRemoved.setStatus(
        ""
    )

moduleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 0, 1)
)
moduleInserted.setObjects(
      *(("INTEL-GEN-MIB", "moduleChassisIndex"),
        ("INTEL-GEN-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    moduleInserted.setStatus(
        ""
    )

moduleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 0, 2)
)
moduleRemoved.setObjects(
      *(("INTEL-GEN-MIB", "moduleChassisIndex"),
        ("INTEL-GEN-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    moduleRemoved.setStatus(
        ""
    )

moduleTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 7, 3, 0, 3)
)
moduleTemperatureEvent.setObjects(
      *(("INTEL-GEN-MIB", "moduleTemperatureStatus"),
        ("INTEL-GEN-MIB", "moduleChassisIndex"),
        ("INTEL-GEN-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    moduleTemperatureEvent.setStatus(
        ""
    )

mediaModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 0, 1)
)
mediaModuleInserted.setObjects(
      *(("INTEL-GEN-MIB", "moduleChassisIndex"),
        ("INTEL-GEN-MIB", "moduleIndex"),
        ("INTEL-GEN-MIB", "mediaModuleIndex"))
)
if mibBuilder.loadTexts:
    mediaModuleInserted.setStatus(
        ""
    )

mediaModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 7, 4, 0, 2)
)
mediaModuleRemoved.setObjects(
      *(("INTEL-GEN-MIB", "moduleChassisIndex"),
        ("INTEL-GEN-MIB", "moduleIndex"),
        ("INTEL-GEN-MIB", "mediaModuleIndex"))
)
if mibBuilder.loadTexts:
    mediaModuleRemoved.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-GEN-MIB",
    **{"intel": intel,
       "sysProducts": sysProducts,
       "switches": switches,
       "express10": express10,
       "express10plus": express10plus,
       "express100fx": express100fx,
       "express550t": express550t,
       "express550f": express550f,
       "express510t": express510t,
       "express520t": express520t,
       "expressGigaSwitch": expressGigaSwitch,
       "express460t-16": express460t_16,
       "express460t-24": express460t_24,
       "nstructure560t": nstructure560t,
       "nstructure560tr": nstructure560tr,
       "nstructure560fr": nstructure560fr,
       "routers": routers,
       "express9100": express9100,
       "express920x": express920x,
       "express9300": express9300,
       "express9400": express9400,
       "express8100st": express8100st,
       "express8100u": express8100u,
       "express8100x": express8100x,
       "express8100fr": express8100fr,
       "express9520st": express9520st,
       "express9520u": express9520u,
       "express9510st": express9510st,
       "express9510u": express9510u,
       "express9515st": express9515st,
       "express9515u": express9515u,
       "express9525st": express9525st,
       "express9525u": express9525u,
       "express8210": express8210,
       "express8220": express8220,
       "express9530": express9530,
       "express9535": express9535,
       "express9545st": express9545st,
       "express9545u": express9545u,
       "express8100wV4": express8100wV4,
       "express8100stV4": express8100stV4,
       "express8100uV4": express8100uV4,
       "hubs": hubs,
       "express110-12": express110_12,
       "express110-24": express110_24,
       "express210-12": express210_12,
       "express210-24": express210_24,
       "express220-12": express220_12,
       "express220-24": express220_24,
       "express330-16": express330_16,
       "express330-24": express330_24,
       "stacks": stacks,
       "nstructure560": nstructure560,
       "nstructure560s": nstructure560s,
       "nstructure560l3s": nstructure560l3s,
       "mib2ext": mib2ext,
       "system": system,
       "sysVendorName": sysVendorName,
       "sysProductName": sysProductName,
       "sysProductSubType": sysProductSubType,
       "sysMibVersion": sysMibVersion,
       "sysTimeOfDay": sysTimeOfDay,
       "sysSystemDate": sysSystemDate,
       "sysReset": sysReset,
       "sysConfTable": sysConfTable,
       "sysConfEntry": sysConfEntry,
       "confStatus": confStatus,
       "confName": confName,
       "confTime": confTime,
       "confTftpIp": confTftpIp,
       "pysmiFakeCol1": pysmiFakeCol1,
       "sysConfChange": sysConfChange,
       "sysLogTable": sysLogTable,
       "sysLogEntry": sysLogEntry,
       "logType": logType,
       "logEntries": logEntries,
       "logFileName": logFileName,
       "logLastChanged": logLastChanged,
       "sysConfRollbackTimeout": sysConfRollbackTimeout,
       "sysConfChangeLastResponse": sysConfChangeLastResponse,
       "sysLocalMangementTimeout": sysLocalMangementTimeout,
       "ip": ip,
       "ipConfTable": ipConfTable,
       "ipConfEntry": ipConfEntry,
       "ipAddressAssignment": ipAddressAssignment,
       "ipAddress": ipAddress,
       "ipSubNetMask": ipSubNetMask,
       "ipRouterAddress": ipRouterAddress,
       "ipBroadcastAddress": ipBroadcastAddress,
       "ipBootpServerAddress": ipBootpServerAddress,
       "pysmiFakeCol2": pysmiFakeCol2,
       "ipConf2Activate": ipConf2Activate,
       "ipModuleConfTable": ipModuleConfTable,
       "ipModuleConfEntry": ipModuleConfEntry,
       "ipModuleChassisIndex": ipModuleChassisIndex,
       "ipModuleModuleIndex": ipModuleModuleIndex,
       "ipModuleConfigIndex": ipModuleConfigIndex,
       "ipModuleAddressAssignment": ipModuleAddressAssignment,
       "ipModuleAddress": ipModuleAddress,
       "ipModuleSubNetMask": ipModuleSubNetMask,
       "ipModuleRouterAddress": ipModuleRouterAddress,
       "ipModuleBroadcastAddress": ipModuleBroadcastAddress,
       "ipModuleBootpServerAddress": ipModuleBootpServerAddress,
       "ipModuleConf2Activate": ipModuleConf2Activate,
       "ipModuleConf2Confirm": ipModuleConf2Confirm,
       "snmp": snmp,
       "snmpAuthViolation": snmpAuthViolation,
       "snmpLoginViolation": snmpLoginViolation,
       "snmpAuthMaxEntries": snmpAuthMaxEntries,
       "snmpAuthTableLastChange": snmpAuthTableLastChange,
       "snmpAuthTable": snmpAuthTable,
       "snmpAuthEntry": snmpAuthEntry,
       "authNumber": authNumber,
       "authProtocolAccessIpCommunity": authProtocolAccessIpCommunity,
       "authDelete": authDelete,
       "snmpTrapMaxEntries": snmpTrapMaxEntries,
       "snmpTrapTable": snmpTrapTable,
       "snmpTrapEntry": snmpTrapEntry,
       "trapNumber": trapNumber,
       "trapIpAndGroupAndCommunity": trapIpAndGroupAndCommunity,
       "trapDelete": trapDelete,
       "snmpAccessTable": snmpAccessTable,
       "snmpAccessEntry": snmpAccessEntry,
       "snmpAccessIP": snmpAccessIP,
       "snmpAccessTime": snmpAccessTime,
       "snmpAccessProtocol": snmpAccessProtocol,
       "snmpAccessType": snmpAccessType,
       "pysmiFakeCol3": pysmiFakeCol3,
       "hw": hw,
       "stack": stack,
       "stackClass": stackClass,
       "stackMaxChassis": stackMaxChassis,
       "stackChassis": stackChassis,
       "stackAgentChassis": stackAgentChassis,
       "stackAgentModule": stackAgentModule,
       "stackUserAssignedName": stackUserAssignedName,
       "stackID": stackID,
       "stackTopology": stackTopology,
       "stackMultiAgentDefultChassisModule": stackMultiAgentDefultChassisModule,
       "chassis": chassis,
       "chassisInserted": chassisInserted,
       "chassisRemoved": chassisRemoved,
       "chassisTable": chassisTable,
       "chassisEntry": chassisEntry,
       "chassisIndex": chassisIndex,
       "chassisType": chassisType,
       "chassisMaxModules": chassisMaxModules,
       "chassisModules": chassisModules,
       "chassisUserAssignedType": chassisUserAssignedType,
       "chassisUserAssignedNumber": chassisUserAssignedNumber,
       "chassisUserAssignedName": chassisUserAssignedName,
       "chassisMaxPSUs": chassisMaxPSUs,
       "modules": modules,
       "moduleInserted": moduleInserted,
       "moduleRemoved": moduleRemoved,
       "moduleTemperatureEvent": moduleTemperatureEvent,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleChassisIndex": moduleChassisIndex,
       "moduleIndex": moduleIndex,
       "moduleType": moduleType,
       "moduleFirstPort": moduleFirstPort,
       "moduleNumberOfPorts": moduleNumberOfPorts,
       "moduleMaxMediaModules": moduleMaxMediaModules,
       "moduleUserAssignedType": moduleUserAssignedType,
       "moduleUserAssignedNumber": moduleUserAssignedNumber,
       "moduleUserAssignedName": moduleUserAssignedName,
       "moduleRAM": moduleRAM,
       "moduleEPROM": moduleEPROM,
       "moduleFLASHPROM": moduleFLASHPROM,
       "moduleLEDInfo": moduleLEDInfo,
       "moduleAllPortType": moduleAllPortType,
       "moduleAllPortLEDInfo": moduleAllPortLEDInfo,
       "moduleAllPortStatus": moduleAllPortStatus,
       "moduleLastPortChange": moduleLastPortChange,
       "moduleMacAddress": moduleMacAddress,
       "moduleIpAddress": moduleIpAddress,
       "moduleSerialNumber": moduleSerialNumber,
       "moduleVersion": moduleVersion,
       "moduleSwStatus": moduleSwStatus,
       "moduleSwName": moduleSwName,
       "moduleSwDescription": moduleSwDescription,
       "moduleSwLoadTime": moduleSwLoadTime,
       "moduleSwTftpIp": moduleSwTftpIp,
       "moduleBackupSwStatus": moduleBackupSwStatus,
       "moduleBackupSwName": moduleBackupSwName,
       "moduleBackupSwDescription": moduleBackupSwDescription,
       "moduleBackupSwLoadTime": moduleBackupSwLoadTime,
       "moduleBackupSwTftpIp": moduleBackupSwTftpIp,
       "moduleSwTftpIpAndSwName": moduleSwTftpIpAndSwName,
       "moduleSwUpdateResult": moduleSwUpdateResult,
       "moduleSpecificObject": moduleSpecificObject,
       "moduleTemperatureStatus": moduleTemperatureStatus,
       "moduleBootSectionVersion": moduleBootSectionVersion,
       "mediamodules": mediamodules,
       "mediaModuleInserted": mediaModuleInserted,
       "mediaModuleRemoved": mediaModuleRemoved,
       "mediaModuleTable": mediaModuleTable,
       "mediaModuleEntry": mediaModuleEntry,
       "mediaModuleChassisIndex": mediaModuleChassisIndex,
       "mediaModuleModuleIndex": mediaModuleModuleIndex,
       "mediaModuleIndex": mediaModuleIndex,
       "mediaModuleType": mediaModuleType,
       "mediaModuleFirstPort": mediaModuleFirstPort,
       "mediaModuleNumberOfPorts": mediaModuleNumberOfPorts,
       "mediaModuleVersion": mediaModuleVersion,
       "ports": ports,
       "portTable": portTable,
       "portEntry": portEntry,
       "portChassisIndex": portChassisIndex,
       "portModuleIndex": portModuleIndex,
       "portIndex": portIndex,
       "portMediaModuleIndex": portMediaModuleIndex,
       "portIfIndex": portIfIndex,
       "portType": portType,
       "portStatus": portStatus,
       "portLEDInfo": portLEDInfo,
       "portTimeSinceLastStateChange": portTimeSinceLastStateChange,
       "portResetAllCounters": portResetAllCounters,
       "portReset": portReset,
       "portLastErrorID": portLastErrorID,
       "portUserAssignedName": portUserAssignedName,
       "stackext": stackext,
       "chassisext": chassisext,
       "modulesext": modulesext,
       "mediamodulesext": mediamodulesext,
       "portsext": portsext}
)
