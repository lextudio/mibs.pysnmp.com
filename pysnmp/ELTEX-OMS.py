# SNMP MIB module (ELTEX-OMS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-OMS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:14 2024
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

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

(DisplayString,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eltexOMS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 4)
)
eltexOMS.setRevisions(
        ("2009-11-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OMSCmdGroup(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("binary", 3),
          ("pattern", 1),
          ("private", 2))
    )



# MIB Managed Objects in the order of their OIDs



class _OmsOUI_Type(DisplayString):
    """Custom type omsOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_OmsOUI_Type.__name__ = "DisplayString"
_OmsOUI_Object = MibScalar
omsOUI = _OmsOUI_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 1),
    _OmsOUI_Type()
)
omsOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsOUI.setStatus("current")


class _OmsProductClass_Type(DisplayString):
    """Custom type omsProductClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OmsProductClass_Type.__name__ = "DisplayString"
_OmsProductClass_Object = MibScalar
omsProductClass = _OmsProductClass_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 2),
    _OmsProductClass_Type()
)
omsProductClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsProductClass.setStatus("current")


class _OmsSerialNumber_Type(DisplayString):
    """Custom type omsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OmsSerialNumber_Type.__name__ = "DisplayString"
_OmsSerialNumber_Object = MibScalar
omsSerialNumber = _OmsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 3),
    _OmsSerialNumber_Type()
)
omsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsSerialNumber.setStatus("current")
_OmsActiveAlarms_Type = Unsigned32
_OmsActiveAlarms_Object = MibScalar
omsActiveAlarms = _OmsActiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 4),
    _OmsActiveAlarms_Type()
)
omsActiveAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omsActiveAlarms.setStatus("current")


class _OmsFwRev_Type(DisplayString):
    """Custom type omsFwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OmsFwRev_Type.__name__ = "DisplayString"
_OmsFwRev_Object = MibScalar
omsFwRev = _OmsFwRev_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 5),
    _OmsFwRev_Type()
)
omsFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsFwRev.setStatus("current")
_OmsCommands_ObjectIdentity = ObjectIdentity
omsCommands = _OmsCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10)
)


class _CmdFileOperationPatternCfg_Type(DisplayString):
    """Custom type cmdFileOperationPatternCfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmdFileOperationPatternCfg_Type.__name__ = "DisplayString"
_CmdFileOperationPatternCfg_Object = MibScalar
cmdFileOperationPatternCfg = _CmdFileOperationPatternCfg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 1),
    _CmdFileOperationPatternCfg_Type()
)
cmdFileOperationPatternCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdFileOperationPatternCfg.setStatus("current")


class _CmdFileOperationPrivateCfg_Type(DisplayString):
    """Custom type cmdFileOperationPrivateCfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmdFileOperationPrivateCfg_Type.__name__ = "DisplayString"
_CmdFileOperationPrivateCfg_Object = MibScalar
cmdFileOperationPrivateCfg = _CmdFileOperationPrivateCfg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 2),
    _CmdFileOperationPrivateCfg_Type()
)
cmdFileOperationPrivateCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdFileOperationPrivateCfg.setStatus("current")


class _CmdFileOperationBinaryCfg_Type(DisplayString):
    """Custom type cmdFileOperationBinaryCfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmdFileOperationBinaryCfg_Type.__name__ = "DisplayString"
_CmdFileOperationBinaryCfg_Object = MibScalar
cmdFileOperationBinaryCfg = _CmdFileOperationBinaryCfg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 3),
    _CmdFileOperationBinaryCfg_Type()
)
cmdFileOperationBinaryCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdFileOperationBinaryCfg.setStatus("current")
_CmdOMSCapabilitiesTable_Object = MibTable
cmdOMSCapabilitiesTable = _CmdOMSCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 4)
)
if mibBuilder.loadTexts:
    cmdOMSCapabilitiesTable.setStatus("current")
_CmdOMSCapabilitiesEntry_Object = MibTableRow
cmdOMSCapabilitiesEntry = _CmdOMSCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 4, 1)
)
cmdOMSCapabilitiesEntry.setIndexNames(
    (0, "ELTEX-OMS", "cmdOMSCapabilitiesEntryID"),
)
if mibBuilder.loadTexts:
    cmdOMSCapabilitiesEntry.setStatus("current")


class _CmdOMSCapabilitiesEntryID_Type(Integer32):
    """Custom type cmdOMSCapabilitiesEntryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_CmdOMSCapabilitiesEntryID_Type.__name__ = "Integer32"
_CmdOMSCapabilitiesEntryID_Object = MibTableColumn
cmdOMSCapabilitiesEntryID = _CmdOMSCapabilitiesEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 4, 1, 1),
    _CmdOMSCapabilitiesEntryID_Type()
)
cmdOMSCapabilitiesEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdOMSCapabilitiesEntryID.setStatus("current")
_CmdOMSCapabilitiesCmdGroup_Type = OMSCmdGroup
_CmdOMSCapabilitiesCmdGroup_Object = MibTableColumn
cmdOMSCapabilitiesCmdGroup = _CmdOMSCapabilitiesCmdGroup_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 4, 1, 2),
    _CmdOMSCapabilitiesCmdGroup_Type()
)
cmdOMSCapabilitiesCmdGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdOMSCapabilitiesCmdGroup.setStatus("current")


class _CmdOMSCapabilitiesCmdName_Type(DisplayString):
    """Custom type cmdOMSCapabilitiesCmdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmdOMSCapabilitiesCmdName_Type.__name__ = "DisplayString"
_CmdOMSCapabilitiesCmdName_Object = MibTableColumn
cmdOMSCapabilitiesCmdName = _CmdOMSCapabilitiesCmdName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 4, 1, 3),
    _CmdOMSCapabilitiesCmdName_Type()
)
cmdOMSCapabilitiesCmdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdOMSCapabilitiesCmdName.setStatus("current")
_CmdOMSCapabilitiesParseParameters_Type = TruthValue
_CmdOMSCapabilitiesParseParameters_Object = MibTableColumn
cmdOMSCapabilitiesParseParameters = _CmdOMSCapabilitiesParseParameters_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 4, 1, 4),
    _CmdOMSCapabilitiesParseParameters_Type()
)
cmdOMSCapabilitiesParseParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdOMSCapabilitiesParseParameters.setStatus("current")
_CmdOMSCapabilitiesRebootOnSuccess_Type = TruthValue
_CmdOMSCapabilitiesRebootOnSuccess_Object = MibTableColumn
cmdOMSCapabilitiesRebootOnSuccess = _CmdOMSCapabilitiesRebootOnSuccess_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 4, 1, 5),
    _CmdOMSCapabilitiesRebootOnSuccess_Type()
)
cmdOMSCapabilitiesRebootOnSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdOMSCapabilitiesRebootOnSuccess.setStatus("current")


class _CmdOMSCapabilitiesDescription_Type(DisplayString):
    """Custom type cmdOMSCapabilitiesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmdOMSCapabilitiesDescription_Type.__name__ = "DisplayString"
_CmdOMSCapabilitiesDescription_Object = MibTableColumn
cmdOMSCapabilitiesDescription = _CmdOMSCapabilitiesDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 10, 4, 1, 6),
    _CmdOMSCapabilitiesDescription_Type()
)
cmdOMSCapabilitiesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdOMSCapabilitiesDescription.setStatus("current")


class _OmsLinuxVersion_Type(DisplayString):
    """Custom type omsLinuxVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OmsLinuxVersion_Type.__name__ = "DisplayString"
_OmsLinuxVersion_Object = MibScalar
omsLinuxVersion = _OmsLinuxVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 11),
    _OmsLinuxVersion_Type()
)
omsLinuxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsLinuxVersion.setStatus("current")


class _OmsFirmwareVersion_Type(DisplayString):
    """Custom type omsFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OmsFirmwareVersion_Type.__name__ = "DisplayString"
_OmsFirmwareVersion_Object = MibScalar
omsFirmwareVersion = _OmsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 12),
    _OmsFirmwareVersion_Type()
)
omsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsFirmwareVersion.setStatus("current")


class _OmsBPUVersion_Type(DisplayString):
    """Custom type omsBPUVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OmsBPUVersion_Type.__name__ = "DisplayString"
_OmsBPUVersion_Object = MibScalar
omsBPUVersion = _OmsBPUVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 13),
    _OmsBPUVersion_Type()
)
omsBPUVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsBPUVersion.setStatus("current")


class _OmsFactoryType_Type(DisplayString):
    """Custom type omsFactoryType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OmsFactoryType_Type.__name__ = "DisplayString"
_OmsFactoryType_Object = MibScalar
omsFactoryType = _OmsFactoryType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 14),
    _OmsFactoryType_Type()
)
omsFactoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsFactoryType.setStatus("current")


class _OmsFactoryMAC_Type(DisplayString):
    """Custom type omsFactoryMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OmsFactoryMAC_Type.__name__ = "DisplayString"
_OmsFactoryMAC_Object = MibScalar
omsFactoryMAC = _OmsFactoryMAC_Object(
    (1, 3, 6, 1, 4, 1, 35265, 4, 15),
    _OmsFactoryMAC_Type()
)
omsFactoryMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsFactoryMAC.setStatus("current")

# Managed Objects groups

omsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 4, 200)
)
omsGroup.setObjects(
      *(("ELTEX-OMS", "omsOUI"),
        ("ELTEX-OMS", "omsProductClass"),
        ("ELTEX-OMS", "omsSerialNumber"),
        ("ELTEX-OMS", "omsActiveAlarms"),
        ("ELTEX-OMS", "omsFwRev"),
        ("ELTEX-OMS", "cmdFileOperationPatternCfg"),
        ("ELTEX-OMS", "cmdFileOperationPrivateCfg"),
        ("ELTEX-OMS", "cmdFileOperationBinaryCfg"),
        ("ELTEX-OMS", "cmdOMSCapabilitiesEntryID"),
        ("ELTEX-OMS", "cmdOMSCapabilitiesCmdGroup"),
        ("ELTEX-OMS", "cmdOMSCapabilitiesCmdName"),
        ("ELTEX-OMS", "cmdOMSCapabilitiesParseParameters"),
        ("ELTEX-OMS", "cmdOMSCapabilitiesRebootOnSuccess"),
        ("ELTEX-OMS", "cmdOMSCapabilitiesDescription"),
        ("ELTEX-OMS", "omsLinuxVersion"),
        ("ELTEX-OMS", "omsFirmwareVersion"),
        ("ELTEX-OMS", "omsBPUVersion"),
        ("ELTEX-OMS", "omsFactoryType"),
        ("ELTEX-OMS", "omsFactoryMAC"))
)
if mibBuilder.loadTexts:
    omsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-OMS",
    **{"OMSCmdGroup": OMSCmdGroup,
       "eltexOMS": eltexOMS,
       "omsOUI": omsOUI,
       "omsProductClass": omsProductClass,
       "omsSerialNumber": omsSerialNumber,
       "omsActiveAlarms": omsActiveAlarms,
       "omsFwRev": omsFwRev,
       "omsCommands": omsCommands,
       "cmdFileOperationPatternCfg": cmdFileOperationPatternCfg,
       "cmdFileOperationPrivateCfg": cmdFileOperationPrivateCfg,
       "cmdFileOperationBinaryCfg": cmdFileOperationBinaryCfg,
       "cmdOMSCapabilitiesTable": cmdOMSCapabilitiesTable,
       "cmdOMSCapabilitiesEntry": cmdOMSCapabilitiesEntry,
       "cmdOMSCapabilitiesEntryID": cmdOMSCapabilitiesEntryID,
       "cmdOMSCapabilitiesCmdGroup": cmdOMSCapabilitiesCmdGroup,
       "cmdOMSCapabilitiesCmdName": cmdOMSCapabilitiesCmdName,
       "cmdOMSCapabilitiesParseParameters": cmdOMSCapabilitiesParseParameters,
       "cmdOMSCapabilitiesRebootOnSuccess": cmdOMSCapabilitiesRebootOnSuccess,
       "cmdOMSCapabilitiesDescription": cmdOMSCapabilitiesDescription,
       "omsLinuxVersion": omsLinuxVersion,
       "omsFirmwareVersion": omsFirmwareVersion,
       "omsBPUVersion": omsBPUVersion,
       "omsFactoryType": omsFactoryType,
       "omsFactoryMAC": omsFactoryMAC,
       "omsGroup": omsGroup}
)
