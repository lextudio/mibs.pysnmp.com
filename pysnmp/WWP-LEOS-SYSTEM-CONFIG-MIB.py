# SNMP MIB module (WWP-LEOS-SYSTEM-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-SYSTEM-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:10 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosSystemConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12)
)
wwpLeosSystemConfigMIB.setRevisions(
        ("2012-09-19 00:00",
         "2012-07-06 00:00",
         "2012-06-27 00:00",
         "2012-04-16 00:00",
         "2011-11-05 00:00",
         "2011-07-05 00:00",
         "2002-03-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FileName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosSystemConfigMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosSystemConfigMIBObjects = _WwpLeosSystemConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1)
)
_WwpLeosSystemConfigAttr_ObjectIdentity = ObjectIdentity
wwpLeosSystemConfigAttr = _WwpLeosSystemConfigAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1)
)
_WwpLeosSystemConfigDefaultGateway_Type = IpAddress
_WwpLeosSystemConfigDefaultGateway_Object = MibScalar
wwpLeosSystemConfigDefaultGateway = _WwpLeosSystemConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 1),
    _WwpLeosSystemConfigDefaultGateway_Type()
)
wwpLeosSystemConfigDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigDefaultGateway.setStatus("current")
_WwpLeosSystemConfigBootCmdFile_Type = FileName
_WwpLeosSystemConfigBootCmdFile_Object = MibScalar
wwpLeosSystemConfigBootCmdFile = _WwpLeosSystemConfigBootCmdFile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 2),
    _WwpLeosSystemConfigBootCmdFile_Type()
)
wwpLeosSystemConfigBootCmdFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBootCmdFile.setStatus("current")
_WwpLeosSystemConfigBootCfgFile_Type = FileName
_WwpLeosSystemConfigBootCfgFile_Object = MibScalar
wwpLeosSystemConfigBootCfgFile = _WwpLeosSystemConfigBootCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 3),
    _WwpLeosSystemConfigBootCfgFile_Type()
)
wwpLeosSystemConfigBootCfgFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBootCfgFile.setStatus("current")
_WwpLeosSystemClockDateTime_Type = DateAndTime
_WwpLeosSystemClockDateTime_Object = MibScalar
wwpLeosSystemClockDateTime = _WwpLeosSystemClockDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 4),
    _WwpLeosSystemClockDateTime_Type()
)
wwpLeosSystemClockDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemClockDateTime.setStatus("current")
_WwpLeosSystemConfigSavePermFile_Type = FileName
_WwpLeosSystemConfigSavePermFile_Object = MibScalar
wwpLeosSystemConfigSavePermFile = _WwpLeosSystemConfigSavePermFile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 5),
    _WwpLeosSystemConfigSavePermFile_Type()
)
wwpLeosSystemConfigSavePermFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigSavePermFile.setStatus("current")
_WwpLeosSystemConfigLastFileNameReset_Type = TruthValue
_WwpLeosSystemConfigLastFileNameReset_Object = MibScalar
wwpLeosSystemConfigLastFileNameReset = _WwpLeosSystemConfigLastFileNameReset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 6),
    _WwpLeosSystemConfigLastFileNameReset_Type()
)
wwpLeosSystemConfigLastFileNameReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigLastFileNameReset.setStatus("current")


class _WwpLeosSystemServiceMode_Type(Integer32):
    """Custom type wwpLeosSystemServiceMode based on Integer32"""
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
        *(("aoam", 3),
          ("mpls", 1),
          ("none", 0),
          ("pbt", 2))
    )


_WwpLeosSystemServiceMode_Type.__name__ = "Integer32"
_WwpLeosSystemServiceMode_Object = MibScalar
wwpLeosSystemServiceMode = _WwpLeosSystemServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 7),
    _WwpLeosSystemServiceMode_Type()
)
wwpLeosSystemServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemServiceMode.setStatus("current")
_WwpLeosSystemConfigBackupGateway_Type = IpAddress
_WwpLeosSystemConfigBackupGateway_Object = MibScalar
wwpLeosSystemConfigBackupGateway = _WwpLeosSystemConfigBackupGateway_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 8),
    _WwpLeosSystemConfigBackupGateway_Type()
)
wwpLeosSystemConfigBackupGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBackupGateway.setStatus("current")
_WwpLeosSystemConfigCustomerCfgFile_Type = FileName
_WwpLeosSystemConfigCustomerCfgFile_Object = MibScalar
wwpLeosSystemConfigCustomerCfgFile = _WwpLeosSystemConfigCustomerCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 9),
    _WwpLeosSystemConfigCustomerCfgFile_Type()
)
wwpLeosSystemConfigCustomerCfgFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigCustomerCfgFile.setStatus("current")
_WwpLeosSystemConfigDefaultGatewayTable_Object = MibTable
wwpLeosSystemConfigDefaultGatewayTable = _WwpLeosSystemConfigDefaultGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wwpLeosSystemConfigDefaultGatewayTable.setStatus("current")
_WwpLeosSystemConfigDefaultGatewayEntry_Object = MibTableRow
wwpLeosSystemConfigDefaultGatewayEntry = _WwpLeosSystemConfigDefaultGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 10, 1)
)
wwpLeosSystemConfigDefaultGatewayEntry.setIndexNames(
    (0, "WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigDefaultGatewayIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosSystemConfigDefaultGatewayEntry.setStatus("current")


class _WwpLeosSystemConfigDefaultGatewayIndex_Type(Integer32):
    """Custom type wwpLeosSystemConfigDefaultGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WwpLeosSystemConfigDefaultGatewayIndex_Type.__name__ = "Integer32"
_WwpLeosSystemConfigDefaultGatewayIndex_Object = MibTableColumn
wwpLeosSystemConfigDefaultGatewayIndex = _WwpLeosSystemConfigDefaultGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 10, 1, 1),
    _WwpLeosSystemConfigDefaultGatewayIndex_Type()
)
wwpLeosSystemConfigDefaultGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigDefaultGatewayIndex.setStatus("current")
_WwpLeosSystemConfigDefaultGatewayInetAddrType_Type = InetAddressType
_WwpLeosSystemConfigDefaultGatewayInetAddrType_Object = MibTableColumn
wwpLeosSystemConfigDefaultGatewayInetAddrType = _WwpLeosSystemConfigDefaultGatewayInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 10, 1, 2),
    _WwpLeosSystemConfigDefaultGatewayInetAddrType_Type()
)
wwpLeosSystemConfigDefaultGatewayInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigDefaultGatewayInetAddrType.setStatus("current")
_WwpLeosSystemConfigDefaultGatewayInetAddress_Type = InetAddress
_WwpLeosSystemConfigDefaultGatewayInetAddress_Object = MibTableColumn
wwpLeosSystemConfigDefaultGatewayInetAddress = _WwpLeosSystemConfigDefaultGatewayInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 10, 1, 3),
    _WwpLeosSystemConfigDefaultGatewayInetAddress_Type()
)
wwpLeosSystemConfigDefaultGatewayInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigDefaultGatewayInetAddress.setStatus("current")
_WwpLeosSystemConfigDefaultGatewayInterfaceName_Type = DisplayString
_WwpLeosSystemConfigDefaultGatewayInterfaceName_Object = MibTableColumn
wwpLeosSystemConfigDefaultGatewayInterfaceName = _WwpLeosSystemConfigDefaultGatewayInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 10, 1, 4),
    _WwpLeosSystemConfigDefaultGatewayInterfaceName_Type()
)
wwpLeosSystemConfigDefaultGatewayInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigDefaultGatewayInterfaceName.setStatus("current")
_WwpLeosSystemConfigDefaultGatewayMetric_Type = Integer32
_WwpLeosSystemConfigDefaultGatewayMetric_Object = MibTableColumn
wwpLeosSystemConfigDefaultGatewayMetric = _WwpLeosSystemConfigDefaultGatewayMetric_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 10, 1, 5),
    _WwpLeosSystemConfigDefaultGatewayMetric_Type()
)
wwpLeosSystemConfigDefaultGatewayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigDefaultGatewayMetric.setStatus("current")
_WwpLeosSystemConfigDefaultGatewayStatus_Type = RowStatus
_WwpLeosSystemConfigDefaultGatewayStatus_Object = MibTableColumn
wwpLeosSystemConfigDefaultGatewayStatus = _WwpLeosSystemConfigDefaultGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 10, 1, 6),
    _WwpLeosSystemConfigDefaultGatewayStatus_Type()
)
wwpLeosSystemConfigDefaultGatewayStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigDefaultGatewayStatus.setStatus("current")
_WwpLeosSystemConfigBackupGatewayTable_Object = MibTable
wwpLeosSystemConfigBackupGatewayTable = _WwpLeosSystemConfigBackupGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 11)
)
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBackupGatewayTable.setStatus("current")
_WwpLeosSystemConfigBackupGatewayEntry_Object = MibTableRow
wwpLeosSystemConfigBackupGatewayEntry = _WwpLeosSystemConfigBackupGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 11, 1)
)
wwpLeosSystemConfigBackupGatewayEntry.setIndexNames(
    (0, "WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigBackupGatewayIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBackupGatewayEntry.setStatus("current")


class _WwpLeosSystemConfigBackupGatewayIndex_Type(Integer32):
    """Custom type wwpLeosSystemConfigBackupGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WwpLeosSystemConfigBackupGatewayIndex_Type.__name__ = "Integer32"
_WwpLeosSystemConfigBackupGatewayIndex_Object = MibTableColumn
wwpLeosSystemConfigBackupGatewayIndex = _WwpLeosSystemConfigBackupGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 11, 1, 1),
    _WwpLeosSystemConfigBackupGatewayIndex_Type()
)
wwpLeosSystemConfigBackupGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBackupGatewayIndex.setStatus("current")
_WwpLeosSystemConfigBackupGatewayInetAddrType_Type = InetAddressType
_WwpLeosSystemConfigBackupGatewayInetAddrType_Object = MibTableColumn
wwpLeosSystemConfigBackupGatewayInetAddrType = _WwpLeosSystemConfigBackupGatewayInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 11, 1, 2),
    _WwpLeosSystemConfigBackupGatewayInetAddrType_Type()
)
wwpLeosSystemConfigBackupGatewayInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBackupGatewayInetAddrType.setStatus("current")
_WwpLeosSystemConfigBackupGatewayInetAddress_Type = InetAddress
_WwpLeosSystemConfigBackupGatewayInetAddress_Object = MibTableColumn
wwpLeosSystemConfigBackupGatewayInetAddress = _WwpLeosSystemConfigBackupGatewayInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 11, 1, 3),
    _WwpLeosSystemConfigBackupGatewayInetAddress_Type()
)
wwpLeosSystemConfigBackupGatewayInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBackupGatewayInetAddress.setStatus("current")
_WwpLeosSystemConfigBackupGatewayInterfaceName_Type = DisplayString
_WwpLeosSystemConfigBackupGatewayInterfaceName_Object = MibTableColumn
wwpLeosSystemConfigBackupGatewayInterfaceName = _WwpLeosSystemConfigBackupGatewayInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 11, 1, 4),
    _WwpLeosSystemConfigBackupGatewayInterfaceName_Type()
)
wwpLeosSystemConfigBackupGatewayInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBackupGatewayInterfaceName.setStatus("current")
_WwpLeosSystemConfigBackupGatewayMetric_Type = Integer32
_WwpLeosSystemConfigBackupGatewayMetric_Object = MibTableColumn
wwpLeosSystemConfigBackupGatewayMetric = _WwpLeosSystemConfigBackupGatewayMetric_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 11, 1, 5),
    _WwpLeosSystemConfigBackupGatewayMetric_Type()
)
wwpLeosSystemConfigBackupGatewayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBackupGatewayMetric.setStatus("current")
_WwpLeosSystemConfigBackupGatewayStatus_Type = RowStatus
_WwpLeosSystemConfigBackupGatewayStatus_Object = MibTableColumn
wwpLeosSystemConfigBackupGatewayStatus = _WwpLeosSystemConfigBackupGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 1, 11, 1, 6),
    _WwpLeosSystemConfigBackupGatewayStatus_Type()
)
wwpLeosSystemConfigBackupGatewayStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigBackupGatewayStatus.setStatus("current")
_WwpLeosSystemConfig_ObjectIdentity = ObjectIdentity
wwpLeosSystemConfig = _WwpLeosSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 2)
)
_WwpLeosSystemConfigSaveFileName_Type = FileName
_WwpLeosSystemConfigSaveFileName_Object = MibScalar
wwpLeosSystemConfigSaveFileName = _WwpLeosSystemConfigSaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 2, 1),
    _WwpLeosSystemConfigSaveFileName_Type()
)
wwpLeosSystemConfigSaveFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigSaveFileName.setStatus("current")


class _WwpLeosSystemConfigControl_Type(Integer32):
    """Custom type wwpLeosSystemConfigControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mfgDefaultCfg", 2),
          ("none", 0),
          ("save", 1))
    )


_WwpLeosSystemConfigControl_Type.__name__ = "Integer32"
_WwpLeosSystemConfigControl_Object = MibScalar
wwpLeosSystemConfigControl = _WwpLeosSystemConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 2, 2),
    _WwpLeosSystemConfigControl_Type()
)
wwpLeosSystemConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigControl.setStatus("current")
_WwpLeosSystemConfigFilepath_Type = FileName
_WwpLeosSystemConfigFilepath_Object = MibScalar
wwpLeosSystemConfigFilepath = _WwpLeosSystemConfigFilepath_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 2, 3),
    _WwpLeosSystemConfigFilepath_Type()
)
wwpLeosSystemConfigFilepath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigFilepath.setStatus("current")
_WwpLeosSystemConfigFileTable_Object = MibTable
wwpLeosSystemConfigFileTable = _WwpLeosSystemConfigFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wwpLeosSystemConfigFileTable.setStatus("current")
_WwpLeosSystemConfigFileEntry_Object = MibTableRow
wwpLeosSystemConfigFileEntry = _WwpLeosSystemConfigFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 2, 4, 1)
)
wwpLeosSystemConfigFileEntry.setIndexNames(
    (0, "WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigFileIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosSystemConfigFileEntry.setStatus("current")


class _WwpLeosSystemConfigFileIndex_Type(Integer32):
    """Custom type wwpLeosSystemConfigFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemConfigFileIndex_Type.__name__ = "Integer32"
_WwpLeosSystemConfigFileIndex_Object = MibTableColumn
wwpLeosSystemConfigFileIndex = _WwpLeosSystemConfigFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 2, 4, 1, 1),
    _WwpLeosSystemConfigFileIndex_Type()
)
wwpLeosSystemConfigFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigFileIndex.setStatus("current")
_WwpLeosSystemConfigFileName_Type = FileName
_WwpLeosSystemConfigFileName_Object = MibTableColumn
wwpLeosSystemConfigFileName = _WwpLeosSystemConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 2, 4, 1, 2),
    _WwpLeosSystemConfigFileName_Type()
)
wwpLeosSystemConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigFileName.setStatus("current")


class _WwpLeosSystemConfigActivateFile_Type(Integer32):
    """Custom type wwpLeosSystemConfigActivateFile based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loadCfg", 1),
          ("none", 3),
          ("resetToCfg", 2))
    )


_WwpLeosSystemConfigActivateFile_Type.__name__ = "Integer32"
_WwpLeosSystemConfigActivateFile_Object = MibTableColumn
wwpLeosSystemConfigActivateFile = _WwpLeosSystemConfigActivateFile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 2, 4, 1, 3),
    _WwpLeosSystemConfigActivateFile_Type()
)
wwpLeosSystemConfigActivateFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigActivateFile.setStatus("current")
_WwpLeosSystemTelnet_ObjectIdentity = ObjectIdentity
wwpLeosSystemTelnet = _WwpLeosSystemTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 3)
)


class _WwpLeosTelnetMaxBaseUserSessions_Type(Integer32):
    """Custom type wwpLeosTelnetMaxBaseUserSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WwpLeosTelnetMaxBaseUserSessions_Type.__name__ = "Integer32"
_WwpLeosTelnetMaxBaseUserSessions_Object = MibScalar
wwpLeosTelnetMaxBaseUserSessions = _WwpLeosTelnetMaxBaseUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 3, 1),
    _WwpLeosTelnetMaxBaseUserSessions_Type()
)
wwpLeosTelnetMaxBaseUserSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTelnetMaxBaseUserSessions.setStatus("current")


class _WwpLeosTelnetMaxSuperUserSessions_Type(Integer32):
    """Custom type wwpLeosTelnetMaxSuperUserSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WwpLeosTelnetMaxSuperUserSessions_Type.__name__ = "Integer32"
_WwpLeosTelnetMaxSuperUserSessions_Object = MibScalar
wwpLeosTelnetMaxSuperUserSessions = _WwpLeosTelnetMaxSuperUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 3, 2),
    _WwpLeosTelnetMaxSuperUserSessions_Type()
)
wwpLeosTelnetMaxSuperUserSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTelnetMaxSuperUserSessions.setStatus("current")


class _WwpLeosTelnetMaxAdminUserSessions_Type(Integer32):
    """Custom type wwpLeosTelnetMaxAdminUserSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WwpLeosTelnetMaxAdminUserSessions_Type.__name__ = "Integer32"
_WwpLeosTelnetMaxAdminUserSessions_Object = MibScalar
wwpLeosTelnetMaxAdminUserSessions = _WwpLeosTelnetMaxAdminUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 3, 3),
    _WwpLeosTelnetMaxAdminUserSessions_Type()
)
wwpLeosTelnetMaxAdminUserSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTelnetMaxAdminUserSessions.setStatus("current")
_WwpLeosSystemCpuLoadQuery_ObjectIdentity = ObjectIdentity
wwpLeosSystemCpuLoadQuery = _WwpLeosSystemCpuLoadQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7)
)


class _WwpLeosSystemCpuLoad1Min_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemCpuLoad1Min_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad1Min_Object = MibScalar
wwpLeosSystemCpuLoad1Min = _WwpLeosSystemCpuLoad1Min_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 1),
    _WwpLeosSystemCpuLoad1Min_Type()
)
wwpLeosSystemCpuLoad1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad1Min.setStatus("current")


class _WwpLeosSystemCpuLoad10Min_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad10Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemCpuLoad10Min_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad10Min_Object = MibScalar
wwpLeosSystemCpuLoad10Min = _WwpLeosSystemCpuLoad10Min_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 2),
    _WwpLeosSystemCpuLoad10Min_Type()
)
wwpLeosSystemCpuLoad10Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad10Min.setStatus("current")


class _WwpLeosSystemCpuLoad15Min_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemCpuLoad15Min_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad15Min_Object = MibScalar
wwpLeosSystemCpuLoad15Min = _WwpLeosSystemCpuLoad15Min_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 3),
    _WwpLeosSystemCpuLoad15Min_Type()
)
wwpLeosSystemCpuLoad15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad15Min.setStatus("current")


class _WwpLeosSystemCpuLoad5Min_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemCpuLoad5Min_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad5Min_Object = MibScalar
wwpLeosSystemCpuLoad5Min = _WwpLeosSystemCpuLoad5Min_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 4),
    _WwpLeosSystemCpuLoad5Min_Type()
)
wwpLeosSystemCpuLoad5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad5Min.setStatus("current")


class _WwpLeosSystemCpuLoad1MinMinimum_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad1MinMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemCpuLoad1MinMinimum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad1MinMinimum_Object = MibScalar
wwpLeosSystemCpuLoad1MinMinimum = _WwpLeosSystemCpuLoad1MinMinimum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 5),
    _WwpLeosSystemCpuLoad1MinMinimum_Type()
)
wwpLeosSystemCpuLoad1MinMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad1MinMinimum.setStatus("current")


class _WwpLeosSystemCpuLoad1MinMaximum_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad1MinMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemCpuLoad1MinMaximum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad1MinMaximum_Object = MibScalar
wwpLeosSystemCpuLoad1MinMaximum = _WwpLeosSystemCpuLoad1MinMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 6),
    _WwpLeosSystemCpuLoad1MinMaximum_Type()
)
wwpLeosSystemCpuLoad1MinMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad1MinMaximum.setStatus("current")


class _WwpLeosSystemCpuLoad1MinState_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad1MinState based on Integer32"""
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
        *(("degraded", 3),
          ("faulted", 4),
          ("normal", 1),
          ("warning", 2))
    )


_WwpLeosSystemCpuLoad1MinState_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad1MinState_Object = MibScalar
wwpLeosSystemCpuLoad1MinState = _WwpLeosSystemCpuLoad1MinState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 7),
    _WwpLeosSystemCpuLoad1MinState_Type()
)
wwpLeosSystemCpuLoad1MinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad1MinState.setStatus("current")


class _WwpLeosSystemCpuLoad15MinMinimum_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad15MinMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemCpuLoad15MinMinimum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad15MinMinimum_Object = MibScalar
wwpLeosSystemCpuLoad15MinMinimum = _WwpLeosSystemCpuLoad15MinMinimum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 8),
    _WwpLeosSystemCpuLoad15MinMinimum_Type()
)
wwpLeosSystemCpuLoad15MinMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad15MinMinimum.setStatus("current")


class _WwpLeosSystemCpuLoad15MinMaximum_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad15MinMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemCpuLoad15MinMaximum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad15MinMaximum_Object = MibScalar
wwpLeosSystemCpuLoad15MinMaximum = _WwpLeosSystemCpuLoad15MinMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 9),
    _WwpLeosSystemCpuLoad15MinMaximum_Type()
)
wwpLeosSystemCpuLoad15MinMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad15MinMaximum.setStatus("current")


class _WwpLeosSystemCpuLoad15MinState_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad15MinState based on Integer32"""
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
        *(("degraded", 3),
          ("faulted", 4),
          ("normal", 1),
          ("warning", 2))
    )


_WwpLeosSystemCpuLoad15MinState_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad15MinState_Object = MibScalar
wwpLeosSystemCpuLoad15MinState = _WwpLeosSystemCpuLoad15MinState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 10),
    _WwpLeosSystemCpuLoad15MinState_Type()
)
wwpLeosSystemCpuLoad15MinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad15MinState.setStatus("current")


class _WwpLeosSystemCpuLoad5MinMinimum_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad5MinMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemCpuLoad5MinMinimum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad5MinMinimum_Object = MibScalar
wwpLeosSystemCpuLoad5MinMinimum = _WwpLeosSystemCpuLoad5MinMinimum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 11),
    _WwpLeosSystemCpuLoad5MinMinimum_Type()
)
wwpLeosSystemCpuLoad5MinMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad5MinMinimum.setStatus("current")


class _WwpLeosSystemCpuLoad5MinMaximum_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad5MinMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemCpuLoad5MinMaximum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad5MinMaximum_Object = MibScalar
wwpLeosSystemCpuLoad5MinMaximum = _WwpLeosSystemCpuLoad5MinMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 12),
    _WwpLeosSystemCpuLoad5MinMaximum_Type()
)
wwpLeosSystemCpuLoad5MinMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad5MinMaximum.setStatus("current")


class _WwpLeosSystemCpuLoad5MinState_Type(Integer32):
    """Custom type wwpLeosSystemCpuLoad5MinState based on Integer32"""
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
        *(("degraded", 3),
          ("faulted", 4),
          ("normal", 1),
          ("warning", 2))
    )


_WwpLeosSystemCpuLoad5MinState_Type.__name__ = "Integer32"
_WwpLeosSystemCpuLoad5MinState_Object = MibScalar
wwpLeosSystemCpuLoad5MinState = _WwpLeosSystemCpuLoad5MinState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 7, 13),
    _WwpLeosSystemCpuLoad5MinState_Type()
)
wwpLeosSystemCpuLoad5MinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuLoad5MinState.setStatus("current")
_WwpLeosSystemConfigNotif_ObjectIdentity = ObjectIdentity
wwpLeosSystemConfigNotif = _WwpLeosSystemConfigNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 8)
)
_WwpLeosSystemConfigNotifTable_Object = MibTable
wwpLeosSystemConfigNotifTable = _WwpLeosSystemConfigNotifTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 8, 1)
)
if mibBuilder.loadTexts:
    wwpLeosSystemConfigNotifTable.setStatus("current")
_WwpLeosSystemConfigNotifEntry_Object = MibTableRow
wwpLeosSystemConfigNotifEntry = _WwpLeosSystemConfigNotifEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 8, 1, 1)
)
wwpLeosSystemConfigNotifEntry.setIndexNames(
    (0, "WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigFileIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosSystemConfigNotifEntry.setStatus("current")


class _WwpLeosSystemConfigErrLineNum_Type(Integer32):
    """Custom type wwpLeosSystemConfigErrLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosSystemConfigErrLineNum_Type.__name__ = "Integer32"
_WwpLeosSystemConfigErrLineNum_Object = MibTableColumn
wwpLeosSystemConfigErrLineNum = _WwpLeosSystemConfigErrLineNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 8, 1, 1, 1),
    _WwpLeosSystemConfigErrLineNum_Type()
)
wwpLeosSystemConfigErrLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigErrLineNum.setStatus("current")
_WwpLeosSystemConfigErrStr_Type = DisplayString
_WwpLeosSystemConfigErrStr_Object = MibTableColumn
wwpLeosSystemConfigErrStr = _WwpLeosSystemConfigErrStr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 8, 1, 1, 2),
    _WwpLeosSystemConfigErrStr_Type()
)
wwpLeosSystemConfigErrStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigErrStr.setStatus("current")


class _WwpLeosSystemConfigErrLinesTotal_Type(Integer32):
    """Custom type wwpLeosSystemConfigErrLinesTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosSystemConfigErrLinesTotal_Type.__name__ = "Integer32"
_WwpLeosSystemConfigErrLinesTotal_Object = MibTableColumn
wwpLeosSystemConfigErrLinesTotal = _WwpLeosSystemConfigErrLinesTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 8, 1, 1, 3),
    _WwpLeosSystemConfigErrLinesTotal_Type()
)
wwpLeosSystemConfigErrLinesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemConfigErrLinesTotal.setStatus("current")
_WwpLeosSystemMemoryUsageQuery_ObjectIdentity = ObjectIdentity
wwpLeosSystemMemoryUsageQuery = _WwpLeosSystemMemoryUsageQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 9)
)
_WwpLeosSystemMemoryUsageTable_Object = MibTable
wwpLeosSystemMemoryUsageTable = _WwpLeosSystemMemoryUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 9, 1)
)
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageTable.setStatus("current")
_WwpLeosSystemMemoryUsageEntry_Object = MibTableRow
wwpLeosSystemMemoryUsageEntry = _WwpLeosSystemMemoryUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 9, 1, 1)
)
wwpLeosSystemMemoryUsageEntry.setIndexNames(
    (0, "WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemMemoryUsagePoolIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageEntry.setStatus("current")


class _WwpLeosSystemMemoryUsagePoolIndex_Type(Integer32):
    """Custom type wwpLeosSystemMemoryUsagePoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global-heap", 2),
          ("malloc-heap", 3),
          ("ose-pool-1", 1))
    )


_WwpLeosSystemMemoryUsagePoolIndex_Type.__name__ = "Integer32"
_WwpLeosSystemMemoryUsagePoolIndex_Object = MibTableColumn
wwpLeosSystemMemoryUsagePoolIndex = _WwpLeosSystemMemoryUsagePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 9, 1, 1, 1),
    _WwpLeosSystemMemoryUsagePoolIndex_Type()
)
wwpLeosSystemMemoryUsagePoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsagePoolIndex.setStatus("current")
_WwpLeosSystemMemoryUsageMemoryTotal_Type = Unsigned32
_WwpLeosSystemMemoryUsageMemoryTotal_Object = MibTableColumn
wwpLeosSystemMemoryUsageMemoryTotal = _WwpLeosSystemMemoryUsageMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 9, 1, 1, 2),
    _WwpLeosSystemMemoryUsageMemoryTotal_Type()
)
wwpLeosSystemMemoryUsageMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageMemoryTotal.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageMemoryTotal.setUnits("bytes")
_WwpLeosSystemMemoryUsageMemoryLWM_Type = Unsigned32
_WwpLeosSystemMemoryUsageMemoryLWM_Object = MibTableColumn
wwpLeosSystemMemoryUsageMemoryLWM = _WwpLeosSystemMemoryUsageMemoryLWM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 9, 1, 1, 3),
    _WwpLeosSystemMemoryUsageMemoryLWM_Type()
)
wwpLeosSystemMemoryUsageMemoryLWM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageMemoryLWM.setStatus("current")
_WwpLeosSystemMemoryUsageMemoryFree_Type = Unsigned32
_WwpLeosSystemMemoryUsageMemoryFree_Object = MibTableColumn
wwpLeosSystemMemoryUsageMemoryFree = _WwpLeosSystemMemoryUsageMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 9, 1, 1, 4),
    _WwpLeosSystemMemoryUsageMemoryFree_Type()
)
wwpLeosSystemMemoryUsageMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageMemoryFree.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageMemoryFree.setUnits("bytes")


class _WwpLeosSystemMemoryUsageStatus_Type(Integer32):
    """Custom type wwpLeosSystemMemoryUsageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lowMemory", 2),
          ("normal", 1),
          ("notSupported", 3))
    )


_WwpLeosSystemMemoryUsageStatus_Type.__name__ = "Integer32"
_WwpLeosSystemMemoryUsageStatus_Object = MibTableColumn
wwpLeosSystemMemoryUsageStatus = _WwpLeosSystemMemoryUsageStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 9, 1, 1, 5),
    _WwpLeosSystemMemoryUsageStatus_Type()
)
wwpLeosSystemMemoryUsageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageStatus.setStatus("current")
_WwpLeosSystemMemoryUsageMemoryUsed_Type = Unsigned32
_WwpLeosSystemMemoryUsageMemoryUsed_Object = MibTableColumn
wwpLeosSystemMemoryUsageMemoryUsed = _WwpLeosSystemMemoryUsageMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 9, 1, 1, 6),
    _WwpLeosSystemMemoryUsageMemoryUsed_Type()
)
wwpLeosSystemMemoryUsageMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageMemoryUsed.setUnits("bytes")
_WwpLeosSystemMemoryUsageMemoryAvailable_Type = Unsigned32
_WwpLeosSystemMemoryUsageMemoryAvailable_Object = MibTableColumn
wwpLeosSystemMemoryUsageMemoryAvailable = _WwpLeosSystemMemoryUsageMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 9, 1, 1, 7),
    _WwpLeosSystemMemoryUsageMemoryAvailable_Type()
)
wwpLeosSystemMemoryUsageMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageMemoryAvailable.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUsageMemoryAvailable.setUnits("bytes")
_WwpLeosSystemXFtp_ObjectIdentity = ObjectIdentity
wwpLeosSystemXFtp = _WwpLeosSystemXFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10)
)


class _WwpLeosSystemXFtpMode_Type(Integer32):
    """Custom type wwpLeosSystemXFtpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("sftp", 3),
          ("tftp", 1))
    )


_WwpLeosSystemXFtpMode_Type.__name__ = "Integer32"
_WwpLeosSystemXFtpMode_Object = MibScalar
wwpLeosSystemXFtpMode = _WwpLeosSystemXFtpMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 1),
    _WwpLeosSystemXFtpMode_Type()
)
wwpLeosSystemXFtpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpMode.setStatus("current")
_WwpLeosSystemXFtpServer_Type = DisplayString
_WwpLeosSystemXFtpServer_Object = MibScalar
wwpLeosSystemXFtpServer = _WwpLeosSystemXFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 2),
    _WwpLeosSystemXFtpServer_Type()
)
wwpLeosSystemXFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpServer.setStatus("current")


class _WwpLeosSystemXFtpUserName_Type(DisplayString):
    """Custom type wwpLeosSystemXFtpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpLeosSystemXFtpUserName_Type.__name__ = "DisplayString"
_WwpLeosSystemXFtpUserName_Object = MibScalar
wwpLeosSystemXFtpUserName = _WwpLeosSystemXFtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 3),
    _WwpLeosSystemXFtpUserName_Type()
)
wwpLeosSystemXFtpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpUserName.setStatus("current")


class _WwpLeosSystemXFtpPasswd_Type(DisplayString):
    """Custom type wwpLeosSystemXFtpPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WwpLeosSystemXFtpPasswd_Type.__name__ = "DisplayString"
_WwpLeosSystemXFtpPasswd_Object = MibScalar
wwpLeosSystemXFtpPasswd = _WwpLeosSystemXFtpPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 4),
    _WwpLeosSystemXFtpPasswd_Type()
)
wwpLeosSystemXFtpPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpPasswd.setStatus("current")


class _WwpLeosSystemXFtpNumOfRetries_Type(Integer32):
    """Custom type wwpLeosSystemXFtpNumOfRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosSystemXFtpNumOfRetries_Type.__name__ = "Integer32"
_WwpLeosSystemXFtpNumOfRetries_Object = MibScalar
wwpLeosSystemXFtpNumOfRetries = _WwpLeosSystemXFtpNumOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 5),
    _WwpLeosSystemXFtpNumOfRetries_Type()
)
wwpLeosSystemXFtpNumOfRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpNumOfRetries.setStatus("current")


class _WwpLeosSystemXFtpRetryInterval_Type(Integer32):
    """Custom type wwpLeosSystemXFtpRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_WwpLeosSystemXFtpRetryInterval_Type.__name__ = "Integer32"
_WwpLeosSystemXFtpRetryInterval_Object = MibScalar
wwpLeosSystemXFtpRetryInterval = _WwpLeosSystemXFtpRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 6),
    _WwpLeosSystemXFtpRetryInterval_Type()
)
wwpLeosSystemXFtpRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpRetryInterval.setStatus("current")


class _WwpLeosSystemXFtpConnectionTimeout_Type(Integer32):
    """Custom type wwpLeosSystemXFtpConnectionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemXFtpConnectionTimeout_Type.__name__ = "Integer32"
_WwpLeosSystemXFtpConnectionTimeout_Object = MibScalar
wwpLeosSystemXFtpConnectionTimeout = _WwpLeosSystemXFtpConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 7),
    _WwpLeosSystemXFtpConnectionTimeout_Type()
)
wwpLeosSystemXFtpConnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpConnectionTimeout.setStatus("current")
_WwpLeosSystemXFtpTFtpServerTable_Object = MibTable
wwpLeosSystemXFtpTFtpServerTable = _WwpLeosSystemXFtpTFtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 8)
)
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpTFtpServerTable.setStatus("current")
_WwpLeosSystemXFtpTFtpServerEntry_Object = MibTableRow
wwpLeosSystemXFtpTFtpServerEntry = _WwpLeosSystemXFtpTFtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 8, 1)
)
wwpLeosSystemXFtpTFtpServerEntry.setIndexNames(
    (0, "WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemXFtpTFtpServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpTFtpServerEntry.setStatus("current")


class _WwpLeosSystemXFtpTFtpServerIndex_Type(Integer32):
    """Custom type wwpLeosSystemXFtpTFtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosSystemXFtpTFtpServerIndex_Type.__name__ = "Integer32"
_WwpLeosSystemXFtpTFtpServerIndex_Object = MibTableColumn
wwpLeosSystemXFtpTFtpServerIndex = _WwpLeosSystemXFtpTFtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 8, 1, 1),
    _WwpLeosSystemXFtpTFtpServerIndex_Type()
)
wwpLeosSystemXFtpTFtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpTFtpServerIndex.setStatus("current")
_WwpLeosSystemXFtpTFtpServerHostName_Type = DisplayString
_WwpLeosSystemXFtpTFtpServerHostName_Object = MibTableColumn
wwpLeosSystemXFtpTFtpServerHostName = _WwpLeosSystemXFtpTFtpServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 8, 1, 2),
    _WwpLeosSystemXFtpTFtpServerHostName_Type()
)
wwpLeosSystemXFtpTFtpServerHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpTFtpServerHostName.setStatus("current")
_WwpLeosSystemXFtpTFtpServerRowStatus_Type = RowStatus
_WwpLeosSystemXFtpTFtpServerRowStatus_Object = MibTableColumn
wwpLeosSystemXFtpTFtpServerRowStatus = _WwpLeosSystemXFtpTFtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 8, 1, 6),
    _WwpLeosSystemXFtpTFtpServerRowStatus_Type()
)
wwpLeosSystemXFtpTFtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpTFtpServerRowStatus.setStatus("current")
_WwpLeosSystemXFtpFtpServerTable_Object = MibTable
wwpLeosSystemXFtpFtpServerTable = _WwpLeosSystemXFtpFtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 9)
)
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpFtpServerTable.setStatus("current")
_WwpLeosSystemXFtpFtpServerEntry_Object = MibTableRow
wwpLeosSystemXFtpFtpServerEntry = _WwpLeosSystemXFtpFtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 9, 1)
)
wwpLeosSystemXFtpFtpServerEntry.setIndexNames(
    (0, "WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemXFtpFtpServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpFtpServerEntry.setStatus("current")


class _WwpLeosSystemXFtpFtpServerIndex_Type(Integer32):
    """Custom type wwpLeosSystemXFtpFtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosSystemXFtpFtpServerIndex_Type.__name__ = "Integer32"
_WwpLeosSystemXFtpFtpServerIndex_Object = MibTableColumn
wwpLeosSystemXFtpFtpServerIndex = _WwpLeosSystemXFtpFtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 9, 1, 1),
    _WwpLeosSystemXFtpFtpServerIndex_Type()
)
wwpLeosSystemXFtpFtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpFtpServerIndex.setStatus("current")
_WwpLeosSystemXFtpFtpServerHostName_Type = DisplayString
_WwpLeosSystemXFtpFtpServerHostName_Object = MibTableColumn
wwpLeosSystemXFtpFtpServerHostName = _WwpLeosSystemXFtpFtpServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 9, 1, 2),
    _WwpLeosSystemXFtpFtpServerHostName_Type()
)
wwpLeosSystemXFtpFtpServerHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpFtpServerHostName.setStatus("current")
_WwpLeosSystemXFtpFtpServerUserName_Type = DisplayString
_WwpLeosSystemXFtpFtpServerUserName_Object = MibTableColumn
wwpLeosSystemXFtpFtpServerUserName = _WwpLeosSystemXFtpFtpServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 9, 1, 3),
    _WwpLeosSystemXFtpFtpServerUserName_Type()
)
wwpLeosSystemXFtpFtpServerUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpFtpServerUserName.setStatus("current")
_WwpLeosSystemXFtpFtpServerPassword_Type = DisplayString
_WwpLeosSystemXFtpFtpServerPassword_Object = MibTableColumn
wwpLeosSystemXFtpFtpServerPassword = _WwpLeosSystemXFtpFtpServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 9, 1, 4),
    _WwpLeosSystemXFtpFtpServerPassword_Type()
)
wwpLeosSystemXFtpFtpServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpFtpServerPassword.setStatus("current")
_WwpLeosSystemXFtpFtpServerSecret_Type = DisplayString
_WwpLeosSystemXFtpFtpServerSecret_Object = MibTableColumn
wwpLeosSystemXFtpFtpServerSecret = _WwpLeosSystemXFtpFtpServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 9, 1, 5),
    _WwpLeosSystemXFtpFtpServerSecret_Type()
)
wwpLeosSystemXFtpFtpServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpFtpServerSecret.setStatus("current")
_WwpLeosSystemXFtpFtpServerRowStatus_Type = RowStatus
_WwpLeosSystemXFtpFtpServerRowStatus_Object = MibTableColumn
wwpLeosSystemXFtpFtpServerRowStatus = _WwpLeosSystemXFtpFtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 9, 1, 6),
    _WwpLeosSystemXFtpFtpServerRowStatus_Type()
)
wwpLeosSystemXFtpFtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpFtpServerRowStatus.setStatus("current")
_WwpLeosSystemXFtpSFtpServerTable_Object = MibTable
wwpLeosSystemXFtpSFtpServerTable = _WwpLeosSystemXFtpSFtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 10)
)
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpSFtpServerTable.setStatus("current")
_WwpLeosSystemXFtpSFtpServerEntry_Object = MibTableRow
wwpLeosSystemXFtpSFtpServerEntry = _WwpLeosSystemXFtpSFtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 10, 1)
)
wwpLeosSystemXFtpSFtpServerEntry.setIndexNames(
    (0, "WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemXFtpSFtpServerIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpSFtpServerEntry.setStatus("current")


class _WwpLeosSystemXFtpSFtpServerIndex_Type(Integer32):
    """Custom type wwpLeosSystemXFtpSFtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosSystemXFtpSFtpServerIndex_Type.__name__ = "Integer32"
_WwpLeosSystemXFtpSFtpServerIndex_Object = MibTableColumn
wwpLeosSystemXFtpSFtpServerIndex = _WwpLeosSystemXFtpSFtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 10, 1, 1),
    _WwpLeosSystemXFtpSFtpServerIndex_Type()
)
wwpLeosSystemXFtpSFtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpSFtpServerIndex.setStatus("current")
_WwpLeosSystemXFtpSFtpServerHostName_Type = DisplayString
_WwpLeosSystemXFtpSFtpServerHostName_Object = MibTableColumn
wwpLeosSystemXFtpSFtpServerHostName = _WwpLeosSystemXFtpSFtpServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 10, 1, 2),
    _WwpLeosSystemXFtpSFtpServerHostName_Type()
)
wwpLeosSystemXFtpSFtpServerHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpSFtpServerHostName.setStatus("current")
_WwpLeosSystemXFtpSFtpServerUserName_Type = DisplayString
_WwpLeosSystemXFtpSFtpServerUserName_Object = MibTableColumn
wwpLeosSystemXFtpSFtpServerUserName = _WwpLeosSystemXFtpSFtpServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 10, 1, 3),
    _WwpLeosSystemXFtpSFtpServerUserName_Type()
)
wwpLeosSystemXFtpSFtpServerUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpSFtpServerUserName.setStatus("current")
_WwpLeosSystemXFtpSFtpServerPassword_Type = DisplayString
_WwpLeosSystemXFtpSFtpServerPassword_Object = MibTableColumn
wwpLeosSystemXFtpSFtpServerPassword = _WwpLeosSystemXFtpSFtpServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 10, 1, 4),
    _WwpLeosSystemXFtpSFtpServerPassword_Type()
)
wwpLeosSystemXFtpSFtpServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpSFtpServerPassword.setStatus("current")
_WwpLeosSystemXFtpSFtpServerSecret_Type = DisplayString
_WwpLeosSystemXFtpSFtpServerSecret_Object = MibTableColumn
wwpLeosSystemXFtpSFtpServerSecret = _WwpLeosSystemXFtpSFtpServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 10, 1, 5),
    _WwpLeosSystemXFtpSFtpServerSecret_Type()
)
wwpLeosSystemXFtpSFtpServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpSFtpServerSecret.setStatus("current")
_WwpLeosSystemXFtpSFtpServerRowStatus_Type = RowStatus
_WwpLeosSystemXFtpSFtpServerRowStatus_Object = MibTableColumn
wwpLeosSystemXFtpSFtpServerRowStatus = _WwpLeosSystemXFtpSFtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 10, 10, 1, 6),
    _WwpLeosSystemXFtpSFtpServerRowStatus_Type()
)
wwpLeosSystemXFtpSFtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosSystemXFtpSFtpServerRowStatus.setStatus("current")
_WwpLeosSystemCpuUtilization_ObjectIdentity = ObjectIdentity
wwpLeosSystemCpuUtilization = _WwpLeosSystemCpuUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11)
)


class _WwpLeosSystemCpuUtilizationLast5Seconds_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast5Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemCpuUtilizationLast5Seconds_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast5Seconds_Object = MibScalar
wwpLeosSystemCpuUtilizationLast5Seconds = _WwpLeosSystemCpuUtilizationLast5Seconds_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 1),
    _WwpLeosSystemCpuUtilizationLast5Seconds_Type()
)
wwpLeosSystemCpuUtilizationLast5Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast5Seconds.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast5SecondsMinimum_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast5SecondsMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemCpuUtilizationLast5SecondsMinimum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast5SecondsMinimum_Object = MibScalar
wwpLeosSystemCpuUtilizationLast5SecondsMinimum = _WwpLeosSystemCpuUtilizationLast5SecondsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 2),
    _WwpLeosSystemCpuUtilizationLast5SecondsMinimum_Type()
)
wwpLeosSystemCpuUtilizationLast5SecondsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast5SecondsMinimum.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast5SecondsMaximum_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast5SecondsMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemCpuUtilizationLast5SecondsMaximum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast5SecondsMaximum_Object = MibScalar
wwpLeosSystemCpuUtilizationLast5SecondsMaximum = _WwpLeosSystemCpuUtilizationLast5SecondsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 3),
    _WwpLeosSystemCpuUtilizationLast5SecondsMaximum_Type()
)
wwpLeosSystemCpuUtilizationLast5SecondsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast5SecondsMaximum.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast5SecondsState_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast5SecondsState based on Integer32"""
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
        *(("degraded", 3),
          ("faulted", 4),
          ("normal", 1),
          ("warning", 2))
    )


_WwpLeosSystemCpuUtilizationLast5SecondsState_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast5SecondsState_Object = MibScalar
wwpLeosSystemCpuUtilizationLast5SecondsState = _WwpLeosSystemCpuUtilizationLast5SecondsState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 4),
    _WwpLeosSystemCpuUtilizationLast5SecondsState_Type()
)
wwpLeosSystemCpuUtilizationLast5SecondsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast5SecondsState.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast10Seconds_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast10Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemCpuUtilizationLast10Seconds_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast10Seconds_Object = MibScalar
wwpLeosSystemCpuUtilizationLast10Seconds = _WwpLeosSystemCpuUtilizationLast10Seconds_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 5),
    _WwpLeosSystemCpuUtilizationLast10Seconds_Type()
)
wwpLeosSystemCpuUtilizationLast10Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast10Seconds.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast10SecondsMinimum_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast10SecondsMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemCpuUtilizationLast10SecondsMinimum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast10SecondsMinimum_Object = MibScalar
wwpLeosSystemCpuUtilizationLast10SecondsMinimum = _WwpLeosSystemCpuUtilizationLast10SecondsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 6),
    _WwpLeosSystemCpuUtilizationLast10SecondsMinimum_Type()
)
wwpLeosSystemCpuUtilizationLast10SecondsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast10SecondsMinimum.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast10SecondsMaximum_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast10SecondsMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemCpuUtilizationLast10SecondsMaximum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast10SecondsMaximum_Object = MibScalar
wwpLeosSystemCpuUtilizationLast10SecondsMaximum = _WwpLeosSystemCpuUtilizationLast10SecondsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 7),
    _WwpLeosSystemCpuUtilizationLast10SecondsMaximum_Type()
)
wwpLeosSystemCpuUtilizationLast10SecondsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast10SecondsMaximum.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast10SecondsState_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast10SecondsState based on Integer32"""
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
        *(("degraded", 3),
          ("faulted", 4),
          ("normal", 1),
          ("warning", 2))
    )


_WwpLeosSystemCpuUtilizationLast10SecondsState_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast10SecondsState_Object = MibScalar
wwpLeosSystemCpuUtilizationLast10SecondsState = _WwpLeosSystemCpuUtilizationLast10SecondsState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 8),
    _WwpLeosSystemCpuUtilizationLast10SecondsState_Type()
)
wwpLeosSystemCpuUtilizationLast10SecondsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast10SecondsState.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast60Seconds_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast60Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemCpuUtilizationLast60Seconds_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast60Seconds_Object = MibScalar
wwpLeosSystemCpuUtilizationLast60Seconds = _WwpLeosSystemCpuUtilizationLast60Seconds_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 9),
    _WwpLeosSystemCpuUtilizationLast60Seconds_Type()
)
wwpLeosSystemCpuUtilizationLast60Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast60Seconds.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast60SecondsMinimum_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast60SecondsMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemCpuUtilizationLast60SecondsMinimum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast60SecondsMinimum_Object = MibScalar
wwpLeosSystemCpuUtilizationLast60SecondsMinimum = _WwpLeosSystemCpuUtilizationLast60SecondsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 10),
    _WwpLeosSystemCpuUtilizationLast60SecondsMinimum_Type()
)
wwpLeosSystemCpuUtilizationLast60SecondsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast60SecondsMinimum.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast60SecondsMaximum_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast60SecondsMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemCpuUtilizationLast60SecondsMaximum_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast60SecondsMaximum_Object = MibScalar
wwpLeosSystemCpuUtilizationLast60SecondsMaximum = _WwpLeosSystemCpuUtilizationLast60SecondsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 11),
    _WwpLeosSystemCpuUtilizationLast60SecondsMaximum_Type()
)
wwpLeosSystemCpuUtilizationLast60SecondsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast60SecondsMaximum.setStatus("current")


class _WwpLeosSystemCpuUtilizationLast60SecondsState_Type(Integer32):
    """Custom type wwpLeosSystemCpuUtilizationLast60SecondsState based on Integer32"""
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
        *(("degraded", 3),
          ("faulted", 4),
          ("normal", 1),
          ("warning", 2))
    )


_WwpLeosSystemCpuUtilizationLast60SecondsState_Type.__name__ = "Integer32"
_WwpLeosSystemCpuUtilizationLast60SecondsState_Object = MibScalar
wwpLeosSystemCpuUtilizationLast60SecondsState = _WwpLeosSystemCpuUtilizationLast60SecondsState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 11, 12),
    _WwpLeosSystemCpuUtilizationLast60SecondsState_Type()
)
wwpLeosSystemCpuUtilizationLast60SecondsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilizationLast60SecondsState.setStatus("current")
_WwpLeosSystemFileSystemUtilization_ObjectIdentity = ObjectIdentity
wwpLeosSystemFileSystemUtilization = _WwpLeosSystemFileSystemUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 12)
)


class _WwpLeosSystemFileSystemUtilizationTmpfsCurrent_Type(Integer32):
    """Custom type wwpLeosSystemFileSystemUtilizationTmpfsCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemFileSystemUtilizationTmpfsCurrent_Type.__name__ = "Integer32"
_WwpLeosSystemFileSystemUtilizationTmpfsCurrent_Object = MibScalar
wwpLeosSystemFileSystemUtilizationTmpfsCurrent = _WwpLeosSystemFileSystemUtilizationTmpfsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 12, 1),
    _WwpLeosSystemFileSystemUtilizationTmpfsCurrent_Type()
)
wwpLeosSystemFileSystemUtilizationTmpfsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemFileSystemUtilizationTmpfsCurrent.setStatus("current")


class _WwpLeosSystemFileSystemUtilizationTmpfsMinimum_Type(Integer32):
    """Custom type wwpLeosSystemFileSystemUtilizationTmpfsMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemFileSystemUtilizationTmpfsMinimum_Type.__name__ = "Integer32"
_WwpLeosSystemFileSystemUtilizationTmpfsMinimum_Object = MibScalar
wwpLeosSystemFileSystemUtilizationTmpfsMinimum = _WwpLeosSystemFileSystemUtilizationTmpfsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 12, 2),
    _WwpLeosSystemFileSystemUtilizationTmpfsMinimum_Type()
)
wwpLeosSystemFileSystemUtilizationTmpfsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemFileSystemUtilizationTmpfsMinimum.setStatus("current")


class _WwpLeosSystemFileSystemUtilizationTmpfsMaximum_Type(Integer32):
    """Custom type wwpLeosSystemFileSystemUtilizationTmpfsMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemFileSystemUtilizationTmpfsMaximum_Type.__name__ = "Integer32"
_WwpLeosSystemFileSystemUtilizationTmpfsMaximum_Object = MibScalar
wwpLeosSystemFileSystemUtilizationTmpfsMaximum = _WwpLeosSystemFileSystemUtilizationTmpfsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 12, 3),
    _WwpLeosSystemFileSystemUtilizationTmpfsMaximum_Type()
)
wwpLeosSystemFileSystemUtilizationTmpfsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemFileSystemUtilizationTmpfsMaximum.setStatus("current")


class _WwpLeosSystemFileSystemUtilizationTmpfsState_Type(Integer32):
    """Custom type wwpLeosSystemFileSystemUtilizationTmpfsState based on Integer32"""
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
        *(("degraded", 3),
          ("faulted", 4),
          ("normal", 1),
          ("warning", 2))
    )


_WwpLeosSystemFileSystemUtilizationTmpfsState_Type.__name__ = "Integer32"
_WwpLeosSystemFileSystemUtilizationTmpfsState_Object = MibScalar
wwpLeosSystemFileSystemUtilizationTmpfsState = _WwpLeosSystemFileSystemUtilizationTmpfsState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 12, 4),
    _WwpLeosSystemFileSystemUtilizationTmpfsState_Type()
)
wwpLeosSystemFileSystemUtilizationTmpfsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemFileSystemUtilizationTmpfsState.setStatus("current")


class _WwpLeosSystemFileSystemUtilizationSysfsCurrent_Type(Integer32):
    """Custom type wwpLeosSystemFileSystemUtilizationSysfsCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemFileSystemUtilizationSysfsCurrent_Type.__name__ = "Integer32"
_WwpLeosSystemFileSystemUtilizationSysfsCurrent_Object = MibScalar
wwpLeosSystemFileSystemUtilizationSysfsCurrent = _WwpLeosSystemFileSystemUtilizationSysfsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 12, 5),
    _WwpLeosSystemFileSystemUtilizationSysfsCurrent_Type()
)
wwpLeosSystemFileSystemUtilizationSysfsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemFileSystemUtilizationSysfsCurrent.setStatus("current")


class _WwpLeosSystemFileSystemUtilizationSysfsMinimum_Type(Integer32):
    """Custom type wwpLeosSystemFileSystemUtilizationSysfsMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemFileSystemUtilizationSysfsMinimum_Type.__name__ = "Integer32"
_WwpLeosSystemFileSystemUtilizationSysfsMinimum_Object = MibScalar
wwpLeosSystemFileSystemUtilizationSysfsMinimum = _WwpLeosSystemFileSystemUtilizationSysfsMinimum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 12, 6),
    _WwpLeosSystemFileSystemUtilizationSysfsMinimum_Type()
)
wwpLeosSystemFileSystemUtilizationSysfsMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemFileSystemUtilizationSysfsMinimum.setStatus("current")


class _WwpLeosSystemFileSystemUtilizationSysfsMaximum_Type(Integer32):
    """Custom type wwpLeosSystemFileSystemUtilizationSysfsMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosSystemFileSystemUtilizationSysfsMaximum_Type.__name__ = "Integer32"
_WwpLeosSystemFileSystemUtilizationSysfsMaximum_Object = MibScalar
wwpLeosSystemFileSystemUtilizationSysfsMaximum = _WwpLeosSystemFileSystemUtilizationSysfsMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 12, 7),
    _WwpLeosSystemFileSystemUtilizationSysfsMaximum_Type()
)
wwpLeosSystemFileSystemUtilizationSysfsMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemFileSystemUtilizationSysfsMaximum.setStatus("current")


class _WwpLeosSystemFileSystemUtilizationSysfsState_Type(Integer32):
    """Custom type wwpLeosSystemFileSystemUtilizationSysfsState based on Integer32"""
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
        *(("degraded", 3),
          ("faulted", 4),
          ("normal", 1),
          ("warning", 2))
    )


_WwpLeosSystemFileSystemUtilizationSysfsState_Type.__name__ = "Integer32"
_WwpLeosSystemFileSystemUtilizationSysfsState_Object = MibScalar
wwpLeosSystemFileSystemUtilizationSysfsState = _WwpLeosSystemFileSystemUtilizationSysfsState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 12, 8),
    _WwpLeosSystemFileSystemUtilizationSysfsState_Type()
)
wwpLeosSystemFileSystemUtilizationSysfsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemFileSystemUtilizationSysfsState.setStatus("current")
_WwpLeosSystemMemoryUtilization_ObjectIdentity = ObjectIdentity
wwpLeosSystemMemoryUtilization = _WwpLeosSystemMemoryUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 13)
)
_WwpLeosSystemMemoryUtilizationUsedMemoryCurrent_Type = Gauge32
_WwpLeosSystemMemoryUtilizationUsedMemoryCurrent_Object = MibScalar
wwpLeosSystemMemoryUtilizationUsedMemoryCurrent = _WwpLeosSystemMemoryUtilizationUsedMemoryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 13, 1),
    _WwpLeosSystemMemoryUtilizationUsedMemoryCurrent_Type()
)
wwpLeosSystemMemoryUtilizationUsedMemoryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUtilizationUsedMemoryCurrent.setStatus("current")
_WwpLeosSystemMemoryUtilizationUsedMemoryMinimum_Type = Gauge32
_WwpLeosSystemMemoryUtilizationUsedMemoryMinimum_Object = MibScalar
wwpLeosSystemMemoryUtilizationUsedMemoryMinimum = _WwpLeosSystemMemoryUtilizationUsedMemoryMinimum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 13, 2),
    _WwpLeosSystemMemoryUtilizationUsedMemoryMinimum_Type()
)
wwpLeosSystemMemoryUtilizationUsedMemoryMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUtilizationUsedMemoryMinimum.setStatus("current")
_WwpLeosSystemMemoryUtilizationUsedMemoryMaximum_Type = Gauge32
_WwpLeosSystemMemoryUtilizationUsedMemoryMaximum_Object = MibScalar
wwpLeosSystemMemoryUtilizationUsedMemoryMaximum = _WwpLeosSystemMemoryUtilizationUsedMemoryMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 13, 3),
    _WwpLeosSystemMemoryUtilizationUsedMemoryMaximum_Type()
)
wwpLeosSystemMemoryUtilizationUsedMemoryMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUtilizationUsedMemoryMaximum.setStatus("current")
_WwpLeosSystemMemoryUtilizationAvailableMemoryCurrent_Type = Gauge32
_WwpLeosSystemMemoryUtilizationAvailableMemoryCurrent_Object = MibScalar
wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent = _WwpLeosSystemMemoryUtilizationAvailableMemoryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 13, 4),
    _WwpLeosSystemMemoryUtilizationAvailableMemoryCurrent_Type()
)
wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent.setStatus("current")
_WwpLeosSystemMemoryUtilizationAvailableMemoryMinimum_Type = Gauge32
_WwpLeosSystemMemoryUtilizationAvailableMemoryMinimum_Object = MibScalar
wwpLeosSystemMemoryUtilizationAvailableMemoryMinimum = _WwpLeosSystemMemoryUtilizationAvailableMemoryMinimum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 13, 5),
    _WwpLeosSystemMemoryUtilizationAvailableMemoryMinimum_Type()
)
wwpLeosSystemMemoryUtilizationAvailableMemoryMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUtilizationAvailableMemoryMinimum.setStatus("current")
_WwpLeosSystemMemoryUtilizationAvailableMemoryMaximum_Type = Gauge32
_WwpLeosSystemMemoryUtilizationAvailableMemoryMaximum_Object = MibScalar
wwpLeosSystemMemoryUtilizationAvailableMemoryMaximum = _WwpLeosSystemMemoryUtilizationAvailableMemoryMaximum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 13, 6),
    _WwpLeosSystemMemoryUtilizationAvailableMemoryMaximum_Type()
)
wwpLeosSystemMemoryUtilizationAvailableMemoryMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUtilizationAvailableMemoryMaximum.setStatus("current")


class _WwpLeosSystemMemoryUtilizationAvailableMemoryState_Type(Integer32):
    """Custom type wwpLeosSystemMemoryUtilizationAvailableMemoryState based on Integer32"""
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
        *(("degraded", 3),
          ("faulted", 4),
          ("normal", 1),
          ("warning", 2))
    )


_WwpLeosSystemMemoryUtilizationAvailableMemoryState_Type.__name__ = "Integer32"
_WwpLeosSystemMemoryUtilizationAvailableMemoryState_Object = MibScalar
wwpLeosSystemMemoryUtilizationAvailableMemoryState = _WwpLeosSystemMemoryUtilizationAvailableMemoryState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 13, 7),
    _WwpLeosSystemMemoryUtilizationAvailableMemoryState_Type()
)
wwpLeosSystemMemoryUtilizationAvailableMemoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUtilizationAvailableMemoryState.setStatus("current")
_WwpLeosSystemGuardian_ObjectIdentity = ObjectIdentity
wwpLeosSystemGuardian = _WwpLeosSystemGuardian_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 14)
)


class _WwpLeosSystemGuardianAdminEnable_Type(Integer32):
    """Custom type wwpLeosSystemGuardianAdminEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpLeosSystemGuardianAdminEnable_Type.__name__ = "Integer32"
_WwpLeosSystemGuardianAdminEnable_Object = MibScalar
wwpLeosSystemGuardianAdminEnable = _WwpLeosSystemGuardianAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 14, 1),
    _WwpLeosSystemGuardianAdminEnable_Type()
)
wwpLeosSystemGuardianAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemGuardianAdminEnable.setStatus("current")


class _WwpLeosSystemGuardianOperEnable_Type(Integer32):
    """Custom type wwpLeosSystemGuardianOperEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("suspended", 3))
    )


_WwpLeosSystemGuardianOperEnable_Type.__name__ = "Integer32"
_WwpLeosSystemGuardianOperEnable_Object = MibScalar
wwpLeosSystemGuardianOperEnable = _WwpLeosSystemGuardianOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 14, 2),
    _WwpLeosSystemGuardianOperEnable_Type()
)
wwpLeosSystemGuardianOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemGuardianOperEnable.setStatus("current")


class _WwpLeosSystemGuardianLimitNumReboots_Type(Integer32):
    """Custom type wwpLeosSystemGuardianLimitNumReboots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosSystemGuardianLimitNumReboots_Type.__name__ = "Integer32"
_WwpLeosSystemGuardianLimitNumReboots_Object = MibScalar
wwpLeosSystemGuardianLimitNumReboots = _WwpLeosSystemGuardianLimitNumReboots_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 14, 3),
    _WwpLeosSystemGuardianLimitNumReboots_Type()
)
wwpLeosSystemGuardianLimitNumReboots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemGuardianLimitNumReboots.setStatus("current")


class _WwpLeosSystemGuardianConsecutiveReboots_Type(Integer32):
    """Custom type wwpLeosSystemGuardianConsecutiveReboots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemGuardianConsecutiveReboots_Type.__name__ = "Integer32"
_WwpLeosSystemGuardianConsecutiveReboots_Object = MibScalar
wwpLeosSystemGuardianConsecutiveReboots = _WwpLeosSystemGuardianConsecutiveReboots_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 14, 4),
    _WwpLeosSystemGuardianConsecutiveReboots_Type()
)
wwpLeosSystemGuardianConsecutiveReboots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemGuardianConsecutiveReboots.setStatus("current")


class _WwpLeosSystemGuardianTotalReboots_Type(Integer32):
    """Custom type wwpLeosSystemGuardianTotalReboots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosSystemGuardianTotalReboots_Type.__name__ = "Integer32"
_WwpLeosSystemGuardianTotalReboots_Object = MibScalar
wwpLeosSystemGuardianTotalReboots = _WwpLeosSystemGuardianTotalReboots_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 14, 5),
    _WwpLeosSystemGuardianTotalReboots_Type()
)
wwpLeosSystemGuardianTotalReboots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemGuardianTotalReboots.setStatus("current")
_WwpLeosSystemServers_ObjectIdentity = ObjectIdentity
wwpLeosSystemServers = _WwpLeosSystemServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 15)
)


class _WwpLeosSystemSftpServerAdminState_Type(Integer32):
    """Custom type wwpLeosSystemSftpServerAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpLeosSystemSftpServerAdminState_Type.__name__ = "Integer32"
_WwpLeosSystemSftpServerAdminState_Object = MibScalar
wwpLeosSystemSftpServerAdminState = _WwpLeosSystemSftpServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 1, 15, 1),
    _WwpLeosSystemSftpServerAdminState_Type()
)
wwpLeosSystemSftpServerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosSystemSftpServerAdminState.setStatus("current")
_WwpLeosSystemConfigMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosSystemConfigMIBNotificationPrefix = _WwpLeosSystemConfigMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2)
)
_WwpLeosSystemConfigMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosSystemConfigMIBNotifications = _WwpLeosSystemConfigMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0)
)
_WwpLeosSystemConfigMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosSystemConfigMIBConformance = _WwpLeosSystemConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 3)
)
_WwpLeosSystemConfigCompliances_ObjectIdentity = ObjectIdentity
wwpLeosSystemConfigCompliances = _WwpLeosSystemConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 3, 1)
)
_WwpLeosSystemConfigMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosSystemConfigMIBGroups = _WwpLeosSystemConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 3, 2)
)

# Managed Objects groups

wwpLeosDefaultGatewayIPv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 3, 2, 1)
)
wwpLeosDefaultGatewayIPv6Group.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigDefaultGatewayInetAddrType"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigDefaultGatewayInetAddress"))
)
if mibBuilder.loadTexts:
    wwpLeosDefaultGatewayIPv6Group.setStatus("current")

wwpLeosBackupGatewayIPv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 3, 2, 2)
)
wwpLeosBackupGatewayIPv6Group.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigBackupGatewayInetAddrType"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigBackupGatewayInetAddress"))
)
if mibBuilder.loadTexts:
    wwpLeosBackupGatewayIPv6Group.setStatus("current")


# Notification objects

wwpLeosImproperCmdInConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 1)
)
wwpLeosImproperCmdInConfigFile.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigFileName"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigErrLineNum"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigErrLinesTotal"))
)
if mibBuilder.loadTexts:
    wwpLeosImproperCmdInConfigFile.setStatus(
        "current"
    )

wwpLeosSystemServiceModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 2)
)
wwpLeosSystemServiceModeChange.setObjects(
    ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemServiceMode")
)
if mibBuilder.loadTexts:
    wwpLeosSystemServiceModeChange.setStatus(
        "current"
    )

wwpLeosSystemMemoryStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 3)
)
wwpLeosSystemMemoryStatusNotification.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemMemoryUsageMemoryTotal"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemMemoryUsageMemoryFree"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemMemoryUsageStatus"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemMemoryUsageMemoryAvailable"))
)
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryStatusNotification.setStatus(
        "current"
    )

wwpLeosImproperCmdInConfigLineString = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 4)
)
wwpLeosImproperCmdInConfigLineString.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigErrStr"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigErrLineNum"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemConfigFileName"))
)
if mibBuilder.loadTexts:
    wwpLeosImproperCmdInConfigLineString.setStatus(
        "current"
    )

wwpLeosSystemCpuUtilization5SecondStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 5)
)
wwpLeosSystemCpuUtilization5SecondStatusTrap.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuUtilizationLast5Seconds"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuUtilizationLast5SecondsState"))
)
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilization5SecondStatusTrap.setStatus(
        "current"
    )

wwpLeosSystemCpuUtilization10SecondStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 6)
)
wwpLeosSystemCpuUtilization10SecondStatusTrap.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuUtilizationLast10Seconds"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuUtilizationLast10SecondsState"))
)
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilization10SecondStatusTrap.setStatus(
        "current"
    )

wwpLeosSystemCpuUtilization60SecondStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 7)
)
wwpLeosSystemCpuUtilization60SecondStatusTrap.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuUtilizationLast60Seconds"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuUtilizationLast60SecondsState"))
)
if mibBuilder.loadTexts:
    wwpLeosSystemCpuUtilization60SecondStatusTrap.setStatus(
        "current"
    )

wwpLeosSystemCpu1MinLoadStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 8)
)
wwpLeosSystemCpu1MinLoadStatusTrap.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuLoad1Min"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuLoad1MinState"))
)
if mibBuilder.loadTexts:
    wwpLeosSystemCpu1MinLoadStatusTrap.setStatus(
        "current"
    )

wwpLeosSystemCpu5MinLoadStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 9)
)
wwpLeosSystemCpu5MinLoadStatusTrap.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuLoad5Min"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuLoad5MinState"))
)
if mibBuilder.loadTexts:
    wwpLeosSystemCpu5MinLoadStatusTrap.setStatus(
        "current"
    )

wwpLeosSystemCpu15MinLoadStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 10)
)
wwpLeosSystemCpu15MinLoadStatusTrap.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuLoad15Min"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemCpuLoad15MinState"))
)
if mibBuilder.loadTexts:
    wwpLeosSystemCpu15MinLoadStatusTrap.setStatus(
        "current"
    )

wwpLeosSystemMemoryUtilizationStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 11)
)
wwpLeosSystemMemoryUtilizationStatusTrap.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemMemoryUtilizationAvailableMemoryState"))
)
if mibBuilder.loadTexts:
    wwpLeosSystemMemoryUtilizationStatusTrap.setStatus(
        "current"
    )

wwpLeosSystemFileSystemUtilizationTmpStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 12)
)
wwpLeosSystemFileSystemUtilizationTmpStatusTrap.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemFileSystemUtilizationTmpfsCurrent"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemFileSystemUtilizationTmpfsState"))
)
if mibBuilder.loadTexts:
    wwpLeosSystemFileSystemUtilizationTmpStatusTrap.setStatus(
        "current"
    )

wwpLeosSystemFileSystemUtilizationSysfsStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 2, 0, 13)
)
wwpLeosSystemFileSystemUtilizationSysfsStatusTrap.setObjects(
      *(("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemFileSystemUtilizationSysfsCurrent"),
        ("WWP-LEOS-SYSTEM-CONFIG-MIB", "wwpLeosSystemFileSystemUtilizationSysfsState"))
)
if mibBuilder.loadTexts:
    wwpLeosSystemFileSystemUtilizationSysfsStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

wwpLeosDefaultGatewayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosDefaultGatewayCompliance.setStatus(
        "current"
    )

wwpLeosBackupGatewayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 12, 3, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosBackupGatewayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-SYSTEM-CONFIG-MIB",
    **{"FileName": FileName,
       "wwpLeosSystemConfigMIB": wwpLeosSystemConfigMIB,
       "wwpLeosSystemConfigMIBObjects": wwpLeosSystemConfigMIBObjects,
       "wwpLeosSystemConfigAttr": wwpLeosSystemConfigAttr,
       "wwpLeosSystemConfigDefaultGateway": wwpLeosSystemConfigDefaultGateway,
       "wwpLeosSystemConfigBootCmdFile": wwpLeosSystemConfigBootCmdFile,
       "wwpLeosSystemConfigBootCfgFile": wwpLeosSystemConfigBootCfgFile,
       "wwpLeosSystemClockDateTime": wwpLeosSystemClockDateTime,
       "wwpLeosSystemConfigSavePermFile": wwpLeosSystemConfigSavePermFile,
       "wwpLeosSystemConfigLastFileNameReset": wwpLeosSystemConfigLastFileNameReset,
       "wwpLeosSystemServiceMode": wwpLeosSystemServiceMode,
       "wwpLeosSystemConfigBackupGateway": wwpLeosSystemConfigBackupGateway,
       "wwpLeosSystemConfigCustomerCfgFile": wwpLeosSystemConfigCustomerCfgFile,
       "wwpLeosSystemConfigDefaultGatewayTable": wwpLeosSystemConfigDefaultGatewayTable,
       "wwpLeosSystemConfigDefaultGatewayEntry": wwpLeosSystemConfigDefaultGatewayEntry,
       "wwpLeosSystemConfigDefaultGatewayIndex": wwpLeosSystemConfigDefaultGatewayIndex,
       "wwpLeosSystemConfigDefaultGatewayInetAddrType": wwpLeosSystemConfigDefaultGatewayInetAddrType,
       "wwpLeosSystemConfigDefaultGatewayInetAddress": wwpLeosSystemConfigDefaultGatewayInetAddress,
       "wwpLeosSystemConfigDefaultGatewayInterfaceName": wwpLeosSystemConfigDefaultGatewayInterfaceName,
       "wwpLeosSystemConfigDefaultGatewayMetric": wwpLeosSystemConfigDefaultGatewayMetric,
       "wwpLeosSystemConfigDefaultGatewayStatus": wwpLeosSystemConfigDefaultGatewayStatus,
       "wwpLeosSystemConfigBackupGatewayTable": wwpLeosSystemConfigBackupGatewayTable,
       "wwpLeosSystemConfigBackupGatewayEntry": wwpLeosSystemConfigBackupGatewayEntry,
       "wwpLeosSystemConfigBackupGatewayIndex": wwpLeosSystemConfigBackupGatewayIndex,
       "wwpLeosSystemConfigBackupGatewayInetAddrType": wwpLeosSystemConfigBackupGatewayInetAddrType,
       "wwpLeosSystemConfigBackupGatewayInetAddress": wwpLeosSystemConfigBackupGatewayInetAddress,
       "wwpLeosSystemConfigBackupGatewayInterfaceName": wwpLeosSystemConfigBackupGatewayInterfaceName,
       "wwpLeosSystemConfigBackupGatewayMetric": wwpLeosSystemConfigBackupGatewayMetric,
       "wwpLeosSystemConfigBackupGatewayStatus": wwpLeosSystemConfigBackupGatewayStatus,
       "wwpLeosSystemConfig": wwpLeosSystemConfig,
       "wwpLeosSystemConfigSaveFileName": wwpLeosSystemConfigSaveFileName,
       "wwpLeosSystemConfigControl": wwpLeosSystemConfigControl,
       "wwpLeosSystemConfigFilepath": wwpLeosSystemConfigFilepath,
       "wwpLeosSystemConfigFileTable": wwpLeosSystemConfigFileTable,
       "wwpLeosSystemConfigFileEntry": wwpLeosSystemConfigFileEntry,
       "wwpLeosSystemConfigFileIndex": wwpLeosSystemConfigFileIndex,
       "wwpLeosSystemConfigFileName": wwpLeosSystemConfigFileName,
       "wwpLeosSystemConfigActivateFile": wwpLeosSystemConfigActivateFile,
       "wwpLeosSystemTelnet": wwpLeosSystemTelnet,
       "wwpLeosTelnetMaxBaseUserSessions": wwpLeosTelnetMaxBaseUserSessions,
       "wwpLeosTelnetMaxSuperUserSessions": wwpLeosTelnetMaxSuperUserSessions,
       "wwpLeosTelnetMaxAdminUserSessions": wwpLeosTelnetMaxAdminUserSessions,
       "wwpLeosSystemCpuLoadQuery": wwpLeosSystemCpuLoadQuery,
       "wwpLeosSystemCpuLoad1Min": wwpLeosSystemCpuLoad1Min,
       "wwpLeosSystemCpuLoad10Min": wwpLeosSystemCpuLoad10Min,
       "wwpLeosSystemCpuLoad15Min": wwpLeosSystemCpuLoad15Min,
       "wwpLeosSystemCpuLoad5Min": wwpLeosSystemCpuLoad5Min,
       "wwpLeosSystemCpuLoad1MinMinimum": wwpLeosSystemCpuLoad1MinMinimum,
       "wwpLeosSystemCpuLoad1MinMaximum": wwpLeosSystemCpuLoad1MinMaximum,
       "wwpLeosSystemCpuLoad1MinState": wwpLeosSystemCpuLoad1MinState,
       "wwpLeosSystemCpuLoad15MinMinimum": wwpLeosSystemCpuLoad15MinMinimum,
       "wwpLeosSystemCpuLoad15MinMaximum": wwpLeosSystemCpuLoad15MinMaximum,
       "wwpLeosSystemCpuLoad15MinState": wwpLeosSystemCpuLoad15MinState,
       "wwpLeosSystemCpuLoad5MinMinimum": wwpLeosSystemCpuLoad5MinMinimum,
       "wwpLeosSystemCpuLoad5MinMaximum": wwpLeosSystemCpuLoad5MinMaximum,
       "wwpLeosSystemCpuLoad5MinState": wwpLeosSystemCpuLoad5MinState,
       "wwpLeosSystemConfigNotif": wwpLeosSystemConfigNotif,
       "wwpLeosSystemConfigNotifTable": wwpLeosSystemConfigNotifTable,
       "wwpLeosSystemConfigNotifEntry": wwpLeosSystemConfigNotifEntry,
       "wwpLeosSystemConfigErrLineNum": wwpLeosSystemConfigErrLineNum,
       "wwpLeosSystemConfigErrStr": wwpLeosSystemConfigErrStr,
       "wwpLeosSystemConfigErrLinesTotal": wwpLeosSystemConfigErrLinesTotal,
       "wwpLeosSystemMemoryUsageQuery": wwpLeosSystemMemoryUsageQuery,
       "wwpLeosSystemMemoryUsageTable": wwpLeosSystemMemoryUsageTable,
       "wwpLeosSystemMemoryUsageEntry": wwpLeosSystemMemoryUsageEntry,
       "wwpLeosSystemMemoryUsagePoolIndex": wwpLeosSystemMemoryUsagePoolIndex,
       "wwpLeosSystemMemoryUsageMemoryTotal": wwpLeosSystemMemoryUsageMemoryTotal,
       "wwpLeosSystemMemoryUsageMemoryLWM": wwpLeosSystemMemoryUsageMemoryLWM,
       "wwpLeosSystemMemoryUsageMemoryFree": wwpLeosSystemMemoryUsageMemoryFree,
       "wwpLeosSystemMemoryUsageStatus": wwpLeosSystemMemoryUsageStatus,
       "wwpLeosSystemMemoryUsageMemoryUsed": wwpLeosSystemMemoryUsageMemoryUsed,
       "wwpLeosSystemMemoryUsageMemoryAvailable": wwpLeosSystemMemoryUsageMemoryAvailable,
       "wwpLeosSystemXFtp": wwpLeosSystemXFtp,
       "wwpLeosSystemXFtpMode": wwpLeosSystemXFtpMode,
       "wwpLeosSystemXFtpServer": wwpLeosSystemXFtpServer,
       "wwpLeosSystemXFtpUserName": wwpLeosSystemXFtpUserName,
       "wwpLeosSystemXFtpPasswd": wwpLeosSystemXFtpPasswd,
       "wwpLeosSystemXFtpNumOfRetries": wwpLeosSystemXFtpNumOfRetries,
       "wwpLeosSystemXFtpRetryInterval": wwpLeosSystemXFtpRetryInterval,
       "wwpLeosSystemXFtpConnectionTimeout": wwpLeosSystemXFtpConnectionTimeout,
       "wwpLeosSystemXFtpTFtpServerTable": wwpLeosSystemXFtpTFtpServerTable,
       "wwpLeosSystemXFtpTFtpServerEntry": wwpLeosSystemXFtpTFtpServerEntry,
       "wwpLeosSystemXFtpTFtpServerIndex": wwpLeosSystemXFtpTFtpServerIndex,
       "wwpLeosSystemXFtpTFtpServerHostName": wwpLeosSystemXFtpTFtpServerHostName,
       "wwpLeosSystemXFtpTFtpServerRowStatus": wwpLeosSystemXFtpTFtpServerRowStatus,
       "wwpLeosSystemXFtpFtpServerTable": wwpLeosSystemXFtpFtpServerTable,
       "wwpLeosSystemXFtpFtpServerEntry": wwpLeosSystemXFtpFtpServerEntry,
       "wwpLeosSystemXFtpFtpServerIndex": wwpLeosSystemXFtpFtpServerIndex,
       "wwpLeosSystemXFtpFtpServerHostName": wwpLeosSystemXFtpFtpServerHostName,
       "wwpLeosSystemXFtpFtpServerUserName": wwpLeosSystemXFtpFtpServerUserName,
       "wwpLeosSystemXFtpFtpServerPassword": wwpLeosSystemXFtpFtpServerPassword,
       "wwpLeosSystemXFtpFtpServerSecret": wwpLeosSystemXFtpFtpServerSecret,
       "wwpLeosSystemXFtpFtpServerRowStatus": wwpLeosSystemXFtpFtpServerRowStatus,
       "wwpLeosSystemXFtpSFtpServerTable": wwpLeosSystemXFtpSFtpServerTable,
       "wwpLeosSystemXFtpSFtpServerEntry": wwpLeosSystemXFtpSFtpServerEntry,
       "wwpLeosSystemXFtpSFtpServerIndex": wwpLeosSystemXFtpSFtpServerIndex,
       "wwpLeosSystemXFtpSFtpServerHostName": wwpLeosSystemXFtpSFtpServerHostName,
       "wwpLeosSystemXFtpSFtpServerUserName": wwpLeosSystemXFtpSFtpServerUserName,
       "wwpLeosSystemXFtpSFtpServerPassword": wwpLeosSystemXFtpSFtpServerPassword,
       "wwpLeosSystemXFtpSFtpServerSecret": wwpLeosSystemXFtpSFtpServerSecret,
       "wwpLeosSystemXFtpSFtpServerRowStatus": wwpLeosSystemXFtpSFtpServerRowStatus,
       "wwpLeosSystemCpuUtilization": wwpLeosSystemCpuUtilization,
       "wwpLeosSystemCpuUtilizationLast5Seconds": wwpLeosSystemCpuUtilizationLast5Seconds,
       "wwpLeosSystemCpuUtilizationLast5SecondsMinimum": wwpLeosSystemCpuUtilizationLast5SecondsMinimum,
       "wwpLeosSystemCpuUtilizationLast5SecondsMaximum": wwpLeosSystemCpuUtilizationLast5SecondsMaximum,
       "wwpLeosSystemCpuUtilizationLast5SecondsState": wwpLeosSystemCpuUtilizationLast5SecondsState,
       "wwpLeosSystemCpuUtilizationLast10Seconds": wwpLeosSystemCpuUtilizationLast10Seconds,
       "wwpLeosSystemCpuUtilizationLast10SecondsMinimum": wwpLeosSystemCpuUtilizationLast10SecondsMinimum,
       "wwpLeosSystemCpuUtilizationLast10SecondsMaximum": wwpLeosSystemCpuUtilizationLast10SecondsMaximum,
       "wwpLeosSystemCpuUtilizationLast10SecondsState": wwpLeosSystemCpuUtilizationLast10SecondsState,
       "wwpLeosSystemCpuUtilizationLast60Seconds": wwpLeosSystemCpuUtilizationLast60Seconds,
       "wwpLeosSystemCpuUtilizationLast60SecondsMinimum": wwpLeosSystemCpuUtilizationLast60SecondsMinimum,
       "wwpLeosSystemCpuUtilizationLast60SecondsMaximum": wwpLeosSystemCpuUtilizationLast60SecondsMaximum,
       "wwpLeosSystemCpuUtilizationLast60SecondsState": wwpLeosSystemCpuUtilizationLast60SecondsState,
       "wwpLeosSystemFileSystemUtilization": wwpLeosSystemFileSystemUtilization,
       "wwpLeosSystemFileSystemUtilizationTmpfsCurrent": wwpLeosSystemFileSystemUtilizationTmpfsCurrent,
       "wwpLeosSystemFileSystemUtilizationTmpfsMinimum": wwpLeosSystemFileSystemUtilizationTmpfsMinimum,
       "wwpLeosSystemFileSystemUtilizationTmpfsMaximum": wwpLeosSystemFileSystemUtilizationTmpfsMaximum,
       "wwpLeosSystemFileSystemUtilizationTmpfsState": wwpLeosSystemFileSystemUtilizationTmpfsState,
       "wwpLeosSystemFileSystemUtilizationSysfsCurrent": wwpLeosSystemFileSystemUtilizationSysfsCurrent,
       "wwpLeosSystemFileSystemUtilizationSysfsMinimum": wwpLeosSystemFileSystemUtilizationSysfsMinimum,
       "wwpLeosSystemFileSystemUtilizationSysfsMaximum": wwpLeosSystemFileSystemUtilizationSysfsMaximum,
       "wwpLeosSystemFileSystemUtilizationSysfsState": wwpLeosSystemFileSystemUtilizationSysfsState,
       "wwpLeosSystemMemoryUtilization": wwpLeosSystemMemoryUtilization,
       "wwpLeosSystemMemoryUtilizationUsedMemoryCurrent": wwpLeosSystemMemoryUtilizationUsedMemoryCurrent,
       "wwpLeosSystemMemoryUtilizationUsedMemoryMinimum": wwpLeosSystemMemoryUtilizationUsedMemoryMinimum,
       "wwpLeosSystemMemoryUtilizationUsedMemoryMaximum": wwpLeosSystemMemoryUtilizationUsedMemoryMaximum,
       "wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent": wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent,
       "wwpLeosSystemMemoryUtilizationAvailableMemoryMinimum": wwpLeosSystemMemoryUtilizationAvailableMemoryMinimum,
       "wwpLeosSystemMemoryUtilizationAvailableMemoryMaximum": wwpLeosSystemMemoryUtilizationAvailableMemoryMaximum,
       "wwpLeosSystemMemoryUtilizationAvailableMemoryState": wwpLeosSystemMemoryUtilizationAvailableMemoryState,
       "wwpLeosSystemGuardian": wwpLeosSystemGuardian,
       "wwpLeosSystemGuardianAdminEnable": wwpLeosSystemGuardianAdminEnable,
       "wwpLeosSystemGuardianOperEnable": wwpLeosSystemGuardianOperEnable,
       "wwpLeosSystemGuardianLimitNumReboots": wwpLeosSystemGuardianLimitNumReboots,
       "wwpLeosSystemGuardianConsecutiveReboots": wwpLeosSystemGuardianConsecutiveReboots,
       "wwpLeosSystemGuardianTotalReboots": wwpLeosSystemGuardianTotalReboots,
       "wwpLeosSystemServers": wwpLeosSystemServers,
       "wwpLeosSystemSftpServerAdminState": wwpLeosSystemSftpServerAdminState,
       "wwpLeosSystemConfigMIBNotificationPrefix": wwpLeosSystemConfigMIBNotificationPrefix,
       "wwpLeosSystemConfigMIBNotifications": wwpLeosSystemConfigMIBNotifications,
       "wwpLeosImproperCmdInConfigFile": wwpLeosImproperCmdInConfigFile,
       "wwpLeosSystemServiceModeChange": wwpLeosSystemServiceModeChange,
       "wwpLeosSystemMemoryStatusNotification": wwpLeosSystemMemoryStatusNotification,
       "wwpLeosImproperCmdInConfigLineString": wwpLeosImproperCmdInConfigLineString,
       "wwpLeosSystemCpuUtilization5SecondStatusTrap": wwpLeosSystemCpuUtilization5SecondStatusTrap,
       "wwpLeosSystemCpuUtilization10SecondStatusTrap": wwpLeosSystemCpuUtilization10SecondStatusTrap,
       "wwpLeosSystemCpuUtilization60SecondStatusTrap": wwpLeosSystemCpuUtilization60SecondStatusTrap,
       "wwpLeosSystemCpu1MinLoadStatusTrap": wwpLeosSystemCpu1MinLoadStatusTrap,
       "wwpLeosSystemCpu5MinLoadStatusTrap": wwpLeosSystemCpu5MinLoadStatusTrap,
       "wwpLeosSystemCpu15MinLoadStatusTrap": wwpLeosSystemCpu15MinLoadStatusTrap,
       "wwpLeosSystemMemoryUtilizationStatusTrap": wwpLeosSystemMemoryUtilizationStatusTrap,
       "wwpLeosSystemFileSystemUtilizationTmpStatusTrap": wwpLeosSystemFileSystemUtilizationTmpStatusTrap,
       "wwpLeosSystemFileSystemUtilizationSysfsStatusTrap": wwpLeosSystemFileSystemUtilizationSysfsStatusTrap,
       "wwpLeosSystemConfigMIBConformance": wwpLeosSystemConfigMIBConformance,
       "wwpLeosSystemConfigCompliances": wwpLeosSystemConfigCompliances,
       "wwpLeosDefaultGatewayCompliance": wwpLeosDefaultGatewayCompliance,
       "wwpLeosBackupGatewayCompliance": wwpLeosBackupGatewayCompliance,
       "wwpLeosSystemConfigMIBGroups": wwpLeosSystemConfigMIBGroups,
       "wwpLeosDefaultGatewayIPv6Group": wwpLeosDefaultGatewayIPv6Group,
       "wwpLeosBackupGatewayIPv6Group": wwpLeosBackupGatewayIPv6Group}
)
