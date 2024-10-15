# SNMP MIB module (ZYXEL-NWA-SERIES_v1-4-2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-NWA-SERIES
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:26 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PhysAddress,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "PhysAddress")

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

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_ProWireless_ObjectIdentity = ObjectIdentity
proWireless = _ProWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9)
)
_PwCommon_ObjectIdentity = ObjectIdentity
pwCommon = _PwCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1)
)


class _PwSwVersion_Type(DisplayString):
    """Custom type pwSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PwSwVersion_Type.__name__ = "DisplayString"
_PwSwVersion_Object = MibScalar
pwSwVersion = _PwSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 1),
    _PwSwVersion_Type()
)
pwSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwSwVersion.setStatus("current")


class _PwCfgVersion_Type(DisplayString):
    """Custom type pwCfgVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PwCfgVersion_Type.__name__ = "DisplayString"
_PwCfgVersion_Object = MibScalar
pwCfgVersion = _PwCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 2),
    _PwCfgVersion_Type()
)
pwCfgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCfgVersion.setStatus("mandatory")
_PwTftpServer_Type = IpAddress
_PwTftpServer_Object = MibScalar
pwTftpServer = _PwTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 3),
    _PwTftpServer_Type()
)
pwTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTftpServer.setStatus("mandatory")


class _PwTftpFileName_Type(DisplayString):
    """Custom type pwTftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PwTftpFileName_Type.__name__ = "DisplayString"
_PwTftpFileName_Object = MibScalar
pwTftpFileName = _PwTftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 4),
    _PwTftpFileName_Type()
)
pwTftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTftpFileName.setStatus("mandatory")


class _PwTftpFileType_Type(Integer32):
    """Custom type pwTftpFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("romfile", 2),
          ("software", 1),
          ("textconfig", 3))
    )


_PwTftpFileType_Type.__name__ = "Integer32"
_PwTftpFileType_Object = MibScalar
pwTftpFileType = _PwTftpFileType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 5),
    _PwTftpFileType_Type()
)
pwTftpFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTftpFileType.setStatus("mandatory")


class _PwTftpOpStatus_Type(Integer32):
    """Custom type pwTftpOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("idle", 0),
          ("inprogress", 1),
          ("success", 3),
          ("timeout", 4))
    )


_PwTftpOpStatus_Type.__name__ = "Integer32"
_PwTftpOpStatus_Object = MibScalar
pwTftpOpStatus = _PwTftpOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 6),
    _PwTftpOpStatus_Type()
)
pwTftpOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTftpOpStatus.setStatus("mandatory")


class _PwTftpOpCommand_Type(Integer32):
    """Custom type pwTftpOpCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 2),
          ("upload", 1))
    )


_PwTftpOpCommand_Type.__name__ = "Integer32"
_PwTftpOpCommand_Object = MibScalar
pwTftpOpCommand = _PwTftpOpCommand_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 7),
    _PwTftpOpCommand_Type()
)
pwTftpOpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTftpOpCommand.setStatus("mandatory")


class _PwSystemReboot_Type(Integer32):
    """Custom type pwSystemReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reboot", 1),
          ("running", 0))
    )


_PwSystemReboot_Type.__name__ = "Integer32"
_PwSystemReboot_Object = MibScalar
pwSystemReboot = _PwSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 8),
    _PwSystemReboot_Type()
)
pwSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwSystemReboot.setStatus("mandatory")


class _PwAutoCfgMessage_Type(DisplayString):
    """Custom type pwAutoCfgMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PwAutoCfgMessage_Type.__name__ = "DisplayString"
_PwAutoCfgMessage_Object = MibScalar
pwAutoCfgMessage = _PwAutoCfgMessage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 9),
    _PwAutoCfgMessage_Type()
)
pwAutoCfgMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAutoCfgMessage.setStatus("mandatory")
_PwCPUUsage_Type = OctetString
_PwCPUUsage_Object = MibScalar
pwCPUUsage = _PwCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 10),
    _PwCPUUsage_Type()
)
pwCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCPUUsage.setStatus("current")
_PwMemoryUsage_Type = OctetString
_PwMemoryUsage_Object = MibScalar
pwMemoryUsage = _PwMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 11),
    _PwMemoryUsage_Type()
)
pwMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMemoryUsage.setStatus("current")
_PwSystemCountry_Type = OctetString
_PwSystemCountry_Object = MibScalar
pwSystemCountry = _PwSystemCountry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 13),
    _PwSystemCountry_Type()
)
pwSystemCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwSystemCountry.setStatus("current")


class _PwPassword_Type(DisplayString):
    """Custom type pwPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PwPassword_Type.__name__ = "DisplayString"
_PwPassword_Object = MibScalar
pwPassword = _PwPassword_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 1, 14),
    _PwPassword_Type()
)
pwPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pwPassword.setStatus("mandatory")
_PwTraps_ObjectIdentity = ObjectIdentity
pwTraps = _PwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2)
)
_PwTrapControl_ObjectIdentity = ObjectIdentity
pwTrapControl = _PwTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1)
)


class _PwTrapWirelessStatus_Type(Integer32):
    """Custom type pwTrapWirelessStatus based on Integer32"""
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


_PwTrapWirelessStatus_Type.__name__ = "Integer32"
_PwTrapWirelessStatus_Object = MibScalar
pwTrapWirelessStatus = _PwTrapWirelessStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1, 1),
    _PwTrapWirelessStatus_Type()
)
pwTrapWirelessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTrapWirelessStatus.setStatus("current")


class _PwTrapSecurityStatus_Type(Integer32):
    """Custom type pwTrapSecurityStatus based on Integer32"""
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


_PwTrapSecurityStatus_Type.__name__ = "Integer32"
_PwTrapSecurityStatus_Object = MibScalar
pwTrapSecurityStatus = _PwTrapSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1, 2),
    _PwTrapSecurityStatus_Type()
)
pwTrapSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTrapSecurityStatus.setStatus("current")


class _PwTrapTFTPStatus_Type(Integer32):
    """Custom type pwTrapTFTPStatus based on Integer32"""
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


_PwTrapTFTPStatus_Type.__name__ = "Integer32"
_PwTrapTFTPStatus_Object = MibScalar
pwTrapTFTPStatus = _PwTrapTFTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 1, 3),
    _PwTrapTFTPStatus_Type()
)
pwTrapTFTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwTrapTFTPStatus.setStatus("current")
_PwTrapVariables_ObjectIdentity = ObjectIdentity
pwTrapVariables = _PwTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2)
)
_PwTrapGenericMessage_Type = DisplayString
_PwTrapGenericMessage_Object = MibScalar
pwTrapGenericMessage = _PwTrapGenericMessage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2, 1),
    _PwTrapGenericMessage_Type()
)
pwTrapGenericMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pwTrapGenericMessage.setStatus("current")
_PwTrapMACAddress_Type = DisplayString
_PwTrapMACAddress_Object = MibScalar
pwTrapMACAddress = _PwTrapMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2, 2),
    _PwTrapMACAddress_Type()
)
pwTrapMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pwTrapMACAddress.setStatus("current")
_PwTrapWlanSSID_Type = DisplayString
_PwTrapWlanSSID_Object = MibScalar
pwTrapWlanSSID = _PwTrapWlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 2, 3),
    _PwTrapWlanSSID_Type()
)
pwTrapWlanSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pwTrapWlanSSID.setStatus("current")
_PwTrapTypes_ObjectIdentity = ObjectIdentity
pwTrapTypes = _PwTrapTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3)
)
_PwWirelessTraps_ObjectIdentity = ObjectIdentity
pwWirelessTraps = _PwWirelessTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 1)
)
_PwSecurityTraps_ObjectIdentity = ObjectIdentity
pwSecurityTraps = _PwSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 2)
)
_PwTFTPTraps_ObjectIdentity = ObjectIdentity
pwTFTPTraps = _PwTFTPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 3)
)
_PwStations_ObjectIdentity = ObjectIdentity
pwStations = _PwStations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3)
)
_PwStationTable_Object = MibTable
pwStationTable = _PwStationTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pwStationTable.setStatus("current")
_PwStationEntry_Object = MibTableRow
pwStationEntry = _PwStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1)
)
pwStationEntry.setIndexNames(
    (0, "ZYXEL-NWA-SERIES_v1-4-2", "pwStationIndex"),
)
if mibBuilder.loadTexts:
    pwStationEntry.setStatus("current")


class _PwStationIndex_Type(Integer32):
    """Custom type pwStationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PwStationIndex_Type.__name__ = "Integer32"
_PwStationIndex_Object = MibTableColumn
pwStationIndex = _PwStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 1),
    _PwStationIndex_Type()
)
pwStationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwStationIndex.setStatus("current")


class _PwStationMacAddress_Type(OctetString):
    """Custom type pwStationMacAddress based on OctetString"""
    defaultValue = OctetString("public")


_PwStationMacAddress_Object = MibTableColumn
pwStationMacAddress = _PwStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 2),
    _PwStationMacAddress_Type()
)
pwStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwStationMacAddress.setStatus("current")
_PwStationAssociateTime_Type = OctetString
_PwStationAssociateTime_Object = MibTableColumn
pwStationAssociateTime = _PwStationAssociateTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 3),
    _PwStationAssociateTime_Type()
)
pwStationAssociateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwStationAssociateTime.setStatus("current")
_PwStationSSID_Type = OctetString
_PwStationSSID_Object = MibTableColumn
pwStationSSID = _PwStationSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 4),
    _PwStationSSID_Type()
)
pwStationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwStationSSID.setStatus("current")
_PwStationStatus_Type = RowStatus
_PwStationStatus_Object = MibTableColumn
pwStationStatus = _PwStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 5),
    _PwStationStatus_Type()
)
pwStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwStationStatus.setStatus("current")
_PwRogueAPDetect_ObjectIdentity = ObjectIdentity
pwRogueAPDetect = _PwRogueAPDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4)
)
_PwRogueAPPeriodTable_Object = MibTable
pwRogueAPPeriodTable = _PwRogueAPPeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pwRogueAPPeriodTable.setStatus("current")
_PwRogueAPPeriodEntry_Object = MibTableRow
pwRogueAPPeriodEntry = _PwRogueAPPeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1, 1)
)
pwRogueAPPeriodEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pwRogueAPPeriodEntry.setStatus("current")


class _PwRogueAPPeriodDetection_Type(Integer32):
    """Custom type pwRogueAPPeriodDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PwRogueAPPeriodDetection_Type.__name__ = "Integer32"
_PwRogueAPPeriodDetection_Object = MibTableColumn
pwRogueAPPeriodDetection = _PwRogueAPPeriodDetection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1, 1, 1),
    _PwRogueAPPeriodDetection_Type()
)
pwRogueAPPeriodDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwRogueAPPeriodDetection.setStatus("current")
_PwRogueAPPeriod_Type = Integer32
_PwRogueAPPeriod_Object = MibTableColumn
pwRogueAPPeriod = _PwRogueAPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1, 1, 2),
    _PwRogueAPPeriod_Type()
)
pwRogueAPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwRogueAPPeriod.setStatus("current")
_PwRogueAPExpirationTime_Type = Integer32
_PwRogueAPExpirationTime_Object = MibTableColumn
pwRogueAPExpirationTime = _PwRogueAPExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1, 1, 3),
    _PwRogueAPExpirationTime_Type()
)
pwRogueAPExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwRogueAPExpirationTime.setStatus("current")
_PwRogueAPDetectTable_Object = MibTable
pwRogueAPDetectTable = _PwRogueAPDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2)
)
if mibBuilder.loadTexts:
    pwRogueAPDetectTable.setStatus("current")
_PwRogueAPDetectEntry_Object = MibTableRow
pwRogueAPDetectEntry = _PwRogueAPDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1)
)
pwRogueAPDetectEntry.setIndexNames(
    (0, "ZYXEL-NWA-SERIES_v1-4-2", "pwRogueAPIndex"),
)
if mibBuilder.loadTexts:
    pwRogueAPDetectEntry.setStatus("current")


class _PwRogueAPIndex_Type(Integer32):
    """Custom type pwRogueAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PwRogueAPIndex_Type.__name__ = "Integer32"
_PwRogueAPIndex_Object = MibTableColumn
pwRogueAPIndex = _PwRogueAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 1),
    _PwRogueAPIndex_Type()
)
pwRogueAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRogueAPIndex.setStatus("current")
_PwRogueAPSSID_Type = OctetString
_PwRogueAPSSID_Object = MibTableColumn
pwRogueAPSSID = _PwRogueAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 2),
    _PwRogueAPSSID_Type()
)
pwRogueAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRogueAPSSID.setStatus("current")
_PwRogueAPMacAddress_Type = OctetString
_PwRogueAPMacAddress_Object = MibTableColumn
pwRogueAPMacAddress = _PwRogueAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 3),
    _PwRogueAPMacAddress_Type()
)
pwRogueAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRogueAPMacAddress.setStatus("current")
_PwRogueAPChannel_Type = OctetString
_PwRogueAPChannel_Object = MibTableColumn
pwRogueAPChannel = _PwRogueAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 4),
    _PwRogueAPChannel_Type()
)
pwRogueAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRogueAPChannel.setStatus("current")
_PwRogueAPSecurity_Type = OctetString
_PwRogueAPSecurity_Object = MibTableColumn
pwRogueAPSecurity = _PwRogueAPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 5),
    _PwRogueAPSecurity_Type()
)
pwRogueAPSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRogueAPSecurity.setStatus("current")
_PwRogueAPSignal_Type = OctetString
_PwRogueAPSignal_Object = MibTableColumn
pwRogueAPSignal = _PwRogueAPSignal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 6),
    _PwRogueAPSignal_Type()
)
pwRogueAPSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwRogueAPSignal.setStatus("current")
_PwFriendlyAPTable_Object = MibTable
pwFriendlyAPTable = _PwFriendlyAPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3)
)
if mibBuilder.loadTexts:
    pwFriendlyAPTable.setStatus("current")
_PwFriendlyAPEntry_Object = MibTableRow
pwFriendlyAPEntry = _PwFriendlyAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1)
)
pwFriendlyAPEntry.setIndexNames(
    (0, "ZYXEL-NWA-SERIES_v1-4-2", "pwFriendlyAPIndex"),
)
if mibBuilder.loadTexts:
    pwFriendlyAPEntry.setStatus("current")


class _PwFriendlyAPIndex_Type(Integer32):
    """Custom type pwFriendlyAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PwFriendlyAPIndex_Type.__name__ = "Integer32"
_PwFriendlyAPIndex_Object = MibTableColumn
pwFriendlyAPIndex = _PwFriendlyAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 1),
    _PwFriendlyAPIndex_Type()
)
pwFriendlyAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwFriendlyAPIndex.setStatus("current")
_PwFriendlyAPSSID_Type = OctetString
_PwFriendlyAPSSID_Object = MibTableColumn
pwFriendlyAPSSID = _PwFriendlyAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 2),
    _PwFriendlyAPSSID_Type()
)
pwFriendlyAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwFriendlyAPSSID.setStatus("current")
_PwFriendlyAPMacAddress_Type = OctetString
_PwFriendlyAPMacAddress_Object = MibTableColumn
pwFriendlyAPMacAddress = _PwFriendlyAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 3),
    _PwFriendlyAPMacAddress_Type()
)
pwFriendlyAPMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwFriendlyAPMacAddress.setStatus("current")
_PwFriendlyAPChannel_Type = OctetString
_PwFriendlyAPChannel_Object = MibTableColumn
pwFriendlyAPChannel = _PwFriendlyAPChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 4),
    _PwFriendlyAPChannel_Type()
)
pwFriendlyAPChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwFriendlyAPChannel.setStatus("current")
_PwFriendlyAPSecurity_Type = OctetString
_PwFriendlyAPSecurity_Object = MibTableColumn
pwFriendlyAPSecurity = _PwFriendlyAPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 5),
    _PwFriendlyAPSecurity_Type()
)
pwFriendlyAPSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwFriendlyAPSecurity.setStatus("current")
_PwFriendlyAPSignal_Type = OctetString
_PwFriendlyAPSignal_Object = MibTableColumn
pwFriendlyAPSignal = _PwFriendlyAPSignal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 6),
    _PwFriendlyAPSignal_Type()
)
pwFriendlyAPSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwFriendlyAPSignal.setStatus("current")
_PwFriendlyAPDescription_Type = OctetString
_PwFriendlyAPDescription_Object = MibTableColumn
pwFriendlyAPDescription = _PwFriendlyAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 3, 1, 7),
    _PwFriendlyAPDescription_Type()
)
pwFriendlyAPDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwFriendlyAPDescription.setStatus("current")
_PwWlanControl_ObjectIdentity = ObjectIdentity
pwWlanControl = _PwWlanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5)
)
_PwWlanControlTable_Object = MibTable
pwWlanControlTable = _PwWlanControlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1)
)
if mibBuilder.loadTexts:
    pwWlanControlTable.setStatus("current")
_PwWlanControlEntry_Object = MibTableRow
pwWlanControlEntry = _PwWlanControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1)
)
pwWlanControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pwWlanControlEntry.setStatus("current")


class _PwWlanMode_Type(Integer32):
    """Custom type pwWlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("mode_802_11a", 4),
          ("mode_802_11b", 1),
          ("mode_802_11bg", 3),
          ("mode_802_11g", 2),
          ("mode_802_11na", 7),
          ("mode_802_11ng", 6))
    )


_PwWlanMode_Type.__name__ = "Integer32"
_PwWlanMode_Object = MibTableColumn
pwWlanMode = _PwWlanMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 1),
    _PwWlanMode_Type()
)
pwWlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwWlanMode.setStatus("current")
_PwWlanSupportedChannel_Type = OctetString
_PwWlanSupportedChannel_Object = MibTableColumn
pwWlanSupportedChannel = _PwWlanSupportedChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 3),
    _PwWlanSupportedChannel_Type()
)
pwWlanSupportedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwWlanSupportedChannel.setStatus("current")


class _PwWlanChannel_Type(Integer32):
    """Custom type pwWlanChannel based on Integer32"""
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              100,
              104,
              108,
              112,
              116,
              120,
              124,
              128,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165)
        )
    )
    namedValues = NamedValues(
        *(("channel-01_2412mhz", 1),
          ("channel-02_2417mhz", 2),
          ("channel-03_2422mhz", 3),
          ("channel-04_2427mhz", 4),
          ("channel-05_2432mhz", 5),
          ("channel-06_2437mhz", 6),
          ("channel-07_2442mhz", 7),
          ("channel-08_2447mhz", 8),
          ("channel-09_2452mhz", 9),
          ("channel-100_5500mhz", 100),
          ("channel-104_5520mhz", 104),
          ("channel-108_5540mhz", 108),
          ("channel-10_2457mhz", 10),
          ("channel-112_5560mhz", 112),
          ("channel-116_5580mhz", 116),
          ("channel-11_2462mhz", 11),
          ("channel-120_5600mhz", 120),
          ("channel-124_5620mhz", 124),
          ("channel-128_5640mhz", 128),
          ("channel-12_2467mhz", 12),
          ("channel-132_5660mhz", 132),
          ("channel-136_5680mhz", 136),
          ("channel-13_2472mhz", 13),
          ("channel-140_5700mhz", 140),
          ("channel-149_5745mhz", 149),
          ("channel-153_5765mhz", 153),
          ("channel-157_5785mhz", 157),
          ("channel-161_5805mhz", 161),
          ("channel-165_5825mhz", 165),
          ("channel-36_5180mhz", 36),
          ("channel-40_5200mhz", 40),
          ("channel-44_5220mhz", 44),
          ("channel-48_5240mhz", 48),
          ("channel-52_5260mhz", 52),
          ("channel-56_5280mhz", 56),
          ("channel-60_5300mhz", 60),
          ("channel-64_5320mhz", 64))
    )


_PwWlanChannel_Type.__name__ = "Integer32"
_PwWlanChannel_Object = MibTableColumn
pwWlanChannel = _PwWlanChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 4),
    _PwWlanChannel_Type()
)
pwWlanChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwWlanChannel.setStatus("current")


class _PwWlanTxPower_Type(Integer32):
    """Custom type pwWlanTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("eighth", 8),
          ("full", 1),
          ("half", 2),
          ("minimum", 16),
          ("quarter", 4))
    )


_PwWlanTxPower_Type.__name__ = "Integer32"
_PwWlanTxPower_Object = MibTableColumn
pwWlanTxPower = _PwWlanTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 5),
    _PwWlanTxPower_Type()
)
pwWlanTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwWlanTxPower.setStatus("current")


class _PwAutoChannelSelection_Type(Integer32):
    """Custom type pwAutoChannelSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enble", 1))
    )


_PwAutoChannelSelection_Type.__name__ = "Integer32"
_PwAutoChannelSelection_Object = MibTableColumn
pwAutoChannelSelection = _PwAutoChannelSelection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 6),
    _PwAutoChannelSelection_Type()
)
pwAutoChannelSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwAutoChannelSelection.setStatus("current")


class _PwCurrentChannel_Type(Integer32):
    """Custom type pwCurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              36,
              40,
              44,
              48,
              52,
              56,
              60,
              64,
              100,
              104,
              108,
              112,
              116,
              120,
              124,
              128,
              132,
              136,
              140,
              149,
              153,
              157,
              161,
              165)
        )
    )
    namedValues = NamedValues(
        *(("channel-01_2412mhz", 1),
          ("channel-02_2417mhz", 2),
          ("channel-03_2422mhz", 3),
          ("channel-04_2427mhz", 4),
          ("channel-05_2432mhz", 5),
          ("channel-06_2437mhz", 6),
          ("channel-07_2442mhz", 7),
          ("channel-08_2447mhz", 8),
          ("channel-09_2452mhz", 9),
          ("channel-100_5500mhz", 100),
          ("channel-104_5520mhz", 104),
          ("channel-108_5540mhz", 108),
          ("channel-10_2457mhz", 10),
          ("channel-112_5560mhz", 112),
          ("channel-116_5580mhz", 116),
          ("channel-11_2462mhz", 11),
          ("channel-120_5600mhz", 120),
          ("channel-124_5620mhz", 124),
          ("channel-128_5640mhz", 128),
          ("channel-12_2467mhz", 12),
          ("channel-132_5660mhz", 132),
          ("channel-136_5680mhz", 136),
          ("channel-13_2472mhz", 13),
          ("channel-140_5700mhz", 140),
          ("channel-149_5745mhz", 149),
          ("channel-153_5765mhz", 153),
          ("channel-157_5785mhz", 157),
          ("channel-161_5805mhz", 161),
          ("channel-165_5825mhz", 165),
          ("channel-36_5180mhz", 36),
          ("channel-40_5200mhz", 40),
          ("channel-44_5220mhz", 44),
          ("channel-48_5240mhz", 48),
          ("channel-52_5260mhz", 52),
          ("channel-56_5280mhz", 56),
          ("channel-60_5300mhz", 60),
          ("channel-64_5320mhz", 64),
          ("device_is_disable", 0))
    )


_PwCurrentChannel_Type.__name__ = "Integer32"
_PwCurrentChannel_Object = MibTableColumn
pwCurrentChannel = _PwCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 7),
    _PwCurrentChannel_Type()
)
pwCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwCurrentChannel.setStatus("current")
_PwStationCount_Type = Counter32
_PwStationCount_Object = MibTableColumn
pwStationCount = _PwStationCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 8),
    _PwStationCount_Type()
)
pwStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwStationCount.setStatus("current")
_PwWlanSupportedMode_Type = OctetString
_PwWlanSupportedMode_Object = MibTableColumn
pwWlanSupportedMode = _PwWlanSupportedMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1, 1, 9),
    _PwWlanSupportedMode_Type()
)
pwWlanSupportedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwWlanSupportedMode.setStatus("current")
_PwWlanStatistics_ObjectIdentity = ObjectIdentity
pwWlanStatistics = _PwWlanStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6)
)
_PwWlanStatisticsTable_Object = MibTable
pwWlanStatisticsTable = _PwWlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pwWlanStatisticsTable.setStatus("current")
_PwWlanStatisticsEntry_Object = MibTableRow
pwWlanStatisticsEntry = _PwWlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1)
)
pwWlanStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pwWlanStatisticsEntry.setStatus("current")
_PwDot11FailedCount_Type = Counter32
_PwDot11FailedCount_Object = MibTableColumn
pwDot11FailedCount = _PwDot11FailedCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 1),
    _PwDot11FailedCount_Type()
)
pwDot11FailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwDot11FailedCount.setStatus("current")
_PwDot11RetryCount_Type = Counter32
_PwDot11RetryCount_Object = MibTableColumn
pwDot11RetryCount = _PwDot11RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 2),
    _PwDot11RetryCount_Type()
)
pwDot11RetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwDot11RetryCount.setStatus("current")
_PwDot11ACKFailureCount_Type = Counter32
_PwDot11ACKFailureCount_Object = MibTableColumn
pwDot11ACKFailureCount = _PwDot11ACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 3),
    _PwDot11ACKFailureCount_Type()
)
pwDot11ACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwDot11ACKFailureCount.setStatus("current")
_PwDot11ReceivedFragmentCount_Type = Counter32
_PwDot11ReceivedFragmentCount_Object = MibTableColumn
pwDot11ReceivedFragmentCount = _PwDot11ReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 4),
    _PwDot11ReceivedFragmentCount_Type()
)
pwDot11ReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwDot11ReceivedFragmentCount.setStatus("current")
_PwDot11TransmittedFrameCount_Type = Counter32
_PwDot11TransmittedFrameCount_Object = MibTableColumn
pwDot11TransmittedFrameCount = _PwDot11TransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 5),
    _PwDot11TransmittedFrameCount_Type()
)
pwDot11TransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwDot11TransmittedFrameCount.setStatus("current")
_PwDot11ReceivedPktCount_Type = Counter32
_PwDot11ReceivedPktCount_Object = MibTableColumn
pwDot11ReceivedPktCount = _PwDot11ReceivedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 6),
    _PwDot11ReceivedPktCount_Type()
)
pwDot11ReceivedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwDot11ReceivedPktCount.setStatus("current")
_PwDot11TransmittedPktCount_Type = Counter32
_PwDot11TransmittedPktCount_Object = MibTableColumn
pwDot11TransmittedPktCount = _PwDot11TransmittedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 7),
    _PwDot11TransmittedPktCount_Type()
)
pwDot11TransmittedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwDot11TransmittedPktCount.setStatus("current")
_PwDot11ReceptionRate_Type = Counter32
_PwDot11ReceptionRate_Object = MibTableColumn
pwDot11ReceptionRate = _PwDot11ReceptionRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 8),
    _PwDot11ReceptionRate_Type()
)
pwDot11ReceptionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwDot11ReceptionRate.setStatus("current")
_PwDot11TransmissionRate_Type = Counter32
_PwDot11TransmissionRate_Object = MibTableColumn
pwDot11TransmissionRate = _PwDot11TransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6, 1, 1, 9),
    _PwDot11TransmissionRate_Type()
)
pwDot11TransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwDot11TransmissionRate.setStatus("current")
_NwaSeries_ObjectIdentity = ObjectIdentity
nwaSeries = _NwaSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 100)
)
_Nwa3100_ObjectIdentity = ObjectIdentity
nwa3100 = _Nwa3100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 1)
)
_Nwa3500_ObjectIdentity = ObjectIdentity
nwa3500 = _Nwa3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 2)
)
_Nwa3160_ObjectIdentity = ObjectIdentity
nwa3160 = _Nwa3160_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 3)
)
_Nwa3163_ObjectIdentity = ObjectIdentity
nwa3163 = _Nwa3163_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 4)
)
_Nwa3550_ObjectIdentity = ObjectIdentity
nwa3550 = _Nwa3550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 5)
)
_Nwa3165_ObjectIdentity = ObjectIdentity
nwa3165 = _Nwa3165_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 6)
)
_Nwa1100_ObjectIdentity = ObjectIdentity
nwa1100 = _Nwa1100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 7)
)
_Nwa3166_ObjectIdentity = ObjectIdentity
nwa3166 = _Nwa3166_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 100, 8)
)

# Managed Objects groups


# Notification objects

pwWlanStaAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pwWlanStaAssociation.setStatus(
        "current"
    )

pwWlanStaDisassociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    pwWlanStaDisassociation.setStatus(
        "current"
    )

pwWlanStaAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    pwWlanStaAuthFail.setStatus(
        "current"
    )

pwTFTPStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 2, 3, 3, 1)
)
pwTFTPStatus.setObjects(
      *(("ZYXEL-NWA-SERIES_v1-4-2", "pwTrapGenericMessage"),
        ("ZYXEL-NWA-SERIES_v1-4-2", "pwTftpOpStatus"),
        ("ZYXEL-NWA-SERIES_v1-4-2", "pwTftpServer"),
        ("ZYXEL-NWA-SERIES_v1-4-2", "pwTftpFileName"),
        ("ZYXEL-NWA-SERIES_v1-4-2", "pwTftpFileType"),
        ("ZYXEL-NWA-SERIES_v1-4-2", "pwTftpOpCommand"))
)
if mibBuilder.loadTexts:
    pwTFTPStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-NWA-SERIES_v1-4-2",
    **{"DisplayString": DisplayString,
       "zyxel": zyxel,
       "products": products,
       "proWireless": proWireless,
       "pwCommon": pwCommon,
       "pwSwVersion": pwSwVersion,
       "pwCfgVersion": pwCfgVersion,
       "pwTftpServer": pwTftpServer,
       "pwTftpFileName": pwTftpFileName,
       "pwTftpFileType": pwTftpFileType,
       "pwTftpOpStatus": pwTftpOpStatus,
       "pwTftpOpCommand": pwTftpOpCommand,
       "pwSystemReboot": pwSystemReboot,
       "pwAutoCfgMessage": pwAutoCfgMessage,
       "pwCPUUsage": pwCPUUsage,
       "pwMemoryUsage": pwMemoryUsage,
       "pwSystemCountry": pwSystemCountry,
       "pwPassword": pwPassword,
       "pwTraps": pwTraps,
       "pwTrapControl": pwTrapControl,
       "pwTrapWirelessStatus": pwTrapWirelessStatus,
       "pwTrapSecurityStatus": pwTrapSecurityStatus,
       "pwTrapTFTPStatus": pwTrapTFTPStatus,
       "pwTrapVariables": pwTrapVariables,
       "pwTrapGenericMessage": pwTrapGenericMessage,
       "pwTrapMACAddress": pwTrapMACAddress,
       "pwTrapWlanSSID": pwTrapWlanSSID,
       "pwTrapTypes": pwTrapTypes,
       "pwWirelessTraps": pwWirelessTraps,
       "pwWlanStaAssociation": pwWlanStaAssociation,
       "pwWlanStaDisassociation": pwWlanStaDisassociation,
       "pwSecurityTraps": pwSecurityTraps,
       "pwWlanStaAuthFail": pwWlanStaAuthFail,
       "pwTFTPTraps": pwTFTPTraps,
       "pwTFTPStatus": pwTFTPStatus,
       "pwStations": pwStations,
       "pwStationTable": pwStationTable,
       "pwStationEntry": pwStationEntry,
       "pwStationIndex": pwStationIndex,
       "pwStationMacAddress": pwStationMacAddress,
       "pwStationAssociateTime": pwStationAssociateTime,
       "pwStationSSID": pwStationSSID,
       "pwStationStatus": pwStationStatus,
       "pwRogueAPDetect": pwRogueAPDetect,
       "pwRogueAPPeriodTable": pwRogueAPPeriodTable,
       "pwRogueAPPeriodEntry": pwRogueAPPeriodEntry,
       "pwRogueAPPeriodDetection": pwRogueAPPeriodDetection,
       "pwRogueAPPeriod": pwRogueAPPeriod,
       "pwRogueAPExpirationTime": pwRogueAPExpirationTime,
       "pwRogueAPDetectTable": pwRogueAPDetectTable,
       "pwRogueAPDetectEntry": pwRogueAPDetectEntry,
       "pwRogueAPIndex": pwRogueAPIndex,
       "pwRogueAPSSID": pwRogueAPSSID,
       "pwRogueAPMacAddress": pwRogueAPMacAddress,
       "pwRogueAPChannel": pwRogueAPChannel,
       "pwRogueAPSecurity": pwRogueAPSecurity,
       "pwRogueAPSignal": pwRogueAPSignal,
       "pwFriendlyAPTable": pwFriendlyAPTable,
       "pwFriendlyAPEntry": pwFriendlyAPEntry,
       "pwFriendlyAPIndex": pwFriendlyAPIndex,
       "pwFriendlyAPSSID": pwFriendlyAPSSID,
       "pwFriendlyAPMacAddress": pwFriendlyAPMacAddress,
       "pwFriendlyAPChannel": pwFriendlyAPChannel,
       "pwFriendlyAPSecurity": pwFriendlyAPSecurity,
       "pwFriendlyAPSignal": pwFriendlyAPSignal,
       "pwFriendlyAPDescription": pwFriendlyAPDescription,
       "pwWlanControl": pwWlanControl,
       "pwWlanControlTable": pwWlanControlTable,
       "pwWlanControlEntry": pwWlanControlEntry,
       "pwWlanMode": pwWlanMode,
       "pwWlanSupportedChannel": pwWlanSupportedChannel,
       "pwWlanChannel": pwWlanChannel,
       "pwWlanTxPower": pwWlanTxPower,
       "pwAutoChannelSelection": pwAutoChannelSelection,
       "pwCurrentChannel": pwCurrentChannel,
       "pwStationCount": pwStationCount,
       "pwWlanSupportedMode": pwWlanSupportedMode,
       "pwWlanStatistics": pwWlanStatistics,
       "pwWlanStatisticsTable": pwWlanStatisticsTable,
       "pwWlanStatisticsEntry": pwWlanStatisticsEntry,
       "pwDot11FailedCount": pwDot11FailedCount,
       "pwDot11RetryCount": pwDot11RetryCount,
       "pwDot11ACKFailureCount": pwDot11ACKFailureCount,
       "pwDot11ReceivedFragmentCount": pwDot11ReceivedFragmentCount,
       "pwDot11TransmittedFrameCount": pwDot11TransmittedFrameCount,
       "pwDot11ReceivedPktCount": pwDot11ReceivedPktCount,
       "pwDot11TransmittedPktCount": pwDot11TransmittedPktCount,
       "pwDot11ReceptionRate": pwDot11ReceptionRate,
       "pwDot11TransmissionRate": pwDot11TransmissionRate,
       "nwaSeries": nwaSeries,
       "nwa3100": nwa3100,
       "nwa3500": nwa3500,
       "nwa3160": nwa3160,
       "nwa3163": nwa3163,
       "nwa3550": nwa3550,
       "nwa3165": nwa3165,
       "nwa1100": nwa1100,
       "nwa3166": nwa3166}
)
