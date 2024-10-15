# SNMP MIB module (ZYXEL-PROWIRELESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-PROWIRELESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:40 2024
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
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
    pwSwVersion.setStatus("mandatory")


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
    (0, "ZYXEL-PROWIRELESS-MIB", "pwStationIndex"),
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
pwStationMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwStationMacAddress.setStatus("current")
_PwStationAssociateTime_Type = OctetString
_PwStationAssociateTime_Object = MibTableColumn
pwStationAssociateTime = _PwStationAssociateTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 3),
    _PwStationAssociateTime_Type()
)
pwStationAssociateTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwStationAssociateTime.setStatus("current")
_PwStationSSID_Type = OctetString
_PwStationSSID_Object = MibTableColumn
pwStationSSID = _PwStationSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 4),
    _PwStationSSID_Type()
)
pwStationSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwStationSSID.setStatus("current")
_PwStationStatus_Type = RowStatus
_PwStationStatus_Object = MibTableColumn
pwStationStatus = _PwStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 3, 2, 1, 5),
    _PwStationStatus_Type()
)
pwStationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwStationStatus.setStatus("current")
_PwAPDetect_ObjectIdentity = ObjectIdentity
pwAPDetect = _PwAPDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4)
)


class _PwAPDetectInterval_Type(Integer32):
    """Custom type pwAPDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("disable", 0)
    )


_PwAPDetectInterval_Type.__name__ = "Integer32"
_PwAPDetectInterval_Object = MibScalar
pwAPDetectInterval = _PwAPDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 1),
    _PwAPDetectInterval_Type()
)
pwAPDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwAPDetectInterval.setStatus("current")
_PwAPDetectTable_Object = MibTable
pwAPDetectTable = _PwAPDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2)
)
if mibBuilder.loadTexts:
    pwAPDetectTable.setStatus("current")
_PwAPDetectEntry_Object = MibTableRow
pwAPDetectEntry = _PwAPDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1)
)
pwAPDetectEntry.setIndexNames(
    (0, "ZYXEL-PROWIRELESS-MIB", "pwAPDetectIndex"),
)
if mibBuilder.loadTexts:
    pwAPDetectEntry.setStatus("current")


class _PwAPDetectIndex_Type(Integer32):
    """Custom type pwAPDetectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PwAPDetectIndex_Type.__name__ = "Integer32"
_PwAPDetectIndex_Object = MibTableColumn
pwAPDetectIndex = _PwAPDetectIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 1),
    _PwAPDetectIndex_Type()
)
pwAPDetectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAPDetectIndex.setStatus("current")
_PwAPDetectSSID_Type = OctetString
_PwAPDetectSSID_Object = MibTableColumn
pwAPDetectSSID = _PwAPDetectSSID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 2),
    _PwAPDetectSSID_Type()
)
pwAPDetectSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAPDetectSSID.setStatus("current")
_PwAPDetectMacAddress_Type = OctetString
_PwAPDetectMacAddress_Object = MibTableColumn
pwAPDetectMacAddress = _PwAPDetectMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 3),
    _PwAPDetectMacAddress_Type()
)
pwAPDetectMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAPDetectMacAddress.setStatus("current")
_PwAPDetectChannel_Type = OctetString
_PwAPDetectChannel_Object = MibTableColumn
pwAPDetectChannel = _PwAPDetectChannel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 4),
    _PwAPDetectChannel_Type()
)
pwAPDetectChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAPDetectChannel.setStatus("current")


class _PwAPDetectSignal_Type(Integer32):
    """Custom type pwAPDetectSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PwAPDetectSignal_Type.__name__ = "Integer32"
_PwAPDetectSignal_Object = MibTableColumn
pwAPDetectSignal = _PwAPDetectSignal_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 5),
    _PwAPDetectSignal_Type()
)
pwAPDetectSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAPDetectSignal.setStatus("current")


class _PwAPDetectNetwork_Type(Integer32):
    """Custom type pwAPDetectNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("adhoc", 1),
          ("infra", 0))
    )


_PwAPDetectNetwork_Type.__name__ = "Integer32"
_PwAPDetectNetwork_Object = MibTableColumn
pwAPDetectNetwork = _PwAPDetectNetwork_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 6),
    _PwAPDetectNetwork_Type()
)
pwAPDetectNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAPDetectNetwork.setStatus("current")


class _PwAPDetectSecurity_Type(Integer32):
    """Custom type pwAPDetectSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wep", 1),
          ("wpa", 2))
    )


_PwAPDetectSecurity_Type.__name__ = "Integer32"
_PwAPDetectSecurity_Object = MibTableColumn
pwAPDetectSecurity = _PwAPDetectSecurity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 7),
    _PwAPDetectSecurity_Type()
)
pwAPDetectSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwAPDetectSecurity.setStatus("current")
_PwAPDetectStatus_Type = RowStatus
_PwAPDetectStatus_Object = MibTableColumn
pwAPDetectStatus = _PwAPDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 4, 2, 1, 8),
    _PwAPDetectStatus_Type()
)
pwAPDetectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwAPDetectStatus.setStatus("current")
_PwWlanControl_ObjectIdentity = ObjectIdentity
pwWlanControl = _PwWlanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5)
)


class _PwMacFilterActive_Type(Integer32):
    """Custom type pwMacFilterActive based on Integer32"""
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


_PwMacFilterActive_Type.__name__ = "Integer32"
_PwMacFilterActive_Object = MibScalar
pwMacFilterActive = _PwMacFilterActive_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 1),
    _PwMacFilterActive_Type()
)
pwMacFilterActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMacFilterActive.setStatus("current")


class _PwMacFilterAction_Type(Integer32):
    """Custom type pwMacFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("discard", 2))
    )


_PwMacFilterAction_Type.__name__ = "Integer32"
_PwMacFilterAction_Object = MibScalar
pwMacFilterAction = _PwMacFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 2),
    _PwMacFilterAction_Type()
)
pwMacFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMacFilterAction.setStatus("current")
_PwMacFilterTable_Object = MibTable
pwMacFilterTable = _PwMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 3)
)
if mibBuilder.loadTexts:
    pwMacFilterTable.setStatus("current")
_PwMacFilterEntry_Object = MibTableRow
pwMacFilterEntry = _PwMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 3, 1)
)
pwMacFilterEntry.setIndexNames(
    (0, "ZYXEL-PROWIRELESS-MIB", "pwMacFilterIndex"),
)
if mibBuilder.loadTexts:
    pwMacFilterEntry.setStatus("current")


class _PwMacFilterIndex_Type(Integer32):
    """Custom type pwMacFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PwMacFilterIndex_Type.__name__ = "Integer32"
_PwMacFilterIndex_Object = MibTableColumn
pwMacFilterIndex = _PwMacFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 3, 1, 1),
    _PwMacFilterIndex_Type()
)
pwMacFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwMacFilterIndex.setStatus("current")
_PwMacFilterMacAddress_Type = OctetString
_PwMacFilterMacAddress_Object = MibTableColumn
pwMacFilterMacAddress = _PwMacFilterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 3, 1, 2),
    _PwMacFilterMacAddress_Type()
)
pwMacFilterMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwMacFilterMacAddress.setStatus("current")
_PwMacFilterStatus_Type = RowStatus
_PwMacFilterStatus_Object = MibTableColumn
pwMacFilterStatus = _PwMacFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 3, 1, 3),
    _PwMacFilterStatus_Type()
)
pwMacFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwMacFilterStatus.setStatus("current")


class _PwWlanTxPower_Type(Integer32):
    """Custom type pwWlanTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("eighth", 8),
          ("full", 1),
          ("half", 2),
          ("quarter", 4))
    )


_PwWlanTxPower_Type.__name__ = "Integer32"
_PwWlanTxPower_Object = MibScalar
pwWlanTxPower = _PwWlanTxPower_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 5, 4),
    _PwWlanTxPower_Type()
)
pwWlanTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwWlanTxPower.setStatus("current")
_PwWlanExtControl_ObjectIdentity = ObjectIdentity
pwWlanExtControl = _PwWlanExtControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 9, 6)
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
      *(("ZYXEL-PROWIRELESS-MIB", "pwTrapGenericMessage"),
        ("ZYXEL-PROWIRELESS-MIB", "pwTftpOpStatus"),
        ("ZYXEL-PROWIRELESS-MIB", "pwTftpServer"),
        ("ZYXEL-PROWIRELESS-MIB", "pwTftpFileName"),
        ("ZYXEL-PROWIRELESS-MIB", "pwTftpFileType"),
        ("ZYXEL-PROWIRELESS-MIB", "pwTftpOpCommand"))
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
    "ZYXEL-PROWIRELESS-MIB",
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
       "pwAPDetect": pwAPDetect,
       "pwAPDetectInterval": pwAPDetectInterval,
       "pwAPDetectTable": pwAPDetectTable,
       "pwAPDetectEntry": pwAPDetectEntry,
       "pwAPDetectIndex": pwAPDetectIndex,
       "pwAPDetectSSID": pwAPDetectSSID,
       "pwAPDetectMacAddress": pwAPDetectMacAddress,
       "pwAPDetectChannel": pwAPDetectChannel,
       "pwAPDetectSignal": pwAPDetectSignal,
       "pwAPDetectNetwork": pwAPDetectNetwork,
       "pwAPDetectSecurity": pwAPDetectSecurity,
       "pwAPDetectStatus": pwAPDetectStatus,
       "pwWlanControl": pwWlanControl,
       "pwMacFilterActive": pwMacFilterActive,
       "pwMacFilterAction": pwMacFilterAction,
       "pwMacFilterTable": pwMacFilterTable,
       "pwMacFilterEntry": pwMacFilterEntry,
       "pwMacFilterIndex": pwMacFilterIndex,
       "pwMacFilterMacAddress": pwMacFilterMacAddress,
       "pwMacFilterStatus": pwMacFilterStatus,
       "pwWlanTxPower": pwWlanTxPower,
       "pwWlanExtControl": pwWlanExtControl}
)
