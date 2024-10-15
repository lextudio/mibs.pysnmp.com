# SNMP MIB module (ESI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ESI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:48 2024
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

_Esi_ObjectIdentity = ObjectIdentity
esi = _Esi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 1)
)
_GenGroupVersion_Type = Integer32
_GenGroupVersion_Object = MibScalar
genGroupVersion = _GenGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 1),
    _GenGroupVersion_Type()
)
genGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupVersion.setStatus("mandatory")
_GenMIBVersion_Type = Integer32
_GenMIBVersion_Object = MibScalar
genMIBVersion = _GenMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 2),
    _GenMIBVersion_Type()
)
genMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genMIBVersion.setStatus("mandatory")


class _GenProductName_Type(DisplayString):
    """Custom type genProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GenProductName_Type.__name__ = "DisplayString"
_GenProductName_Object = MibScalar
genProductName = _GenProductName_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 3),
    _GenProductName_Type()
)
genProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProductName.setStatus("mandatory")


class _GenProductNumber_Type(DisplayString):
    """Custom type genProductNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_GenProductNumber_Type.__name__ = "DisplayString"
_GenProductNumber_Object = MibScalar
genProductNumber = _GenProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 4),
    _GenProductNumber_Type()
)
genProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProductNumber.setStatus("mandatory")


class _GenSerialNumber_Type(DisplayString):
    """Custom type genSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_GenSerialNumber_Type.__name__ = "DisplayString"
_GenSerialNumber_Object = MibScalar
genSerialNumber = _GenSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 5),
    _GenSerialNumber_Type()
)
genSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSerialNumber.setStatus("mandatory")


class _GenHWAddress_Type(OctetString):
    """Custom type genHWAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_GenHWAddress_Type.__name__ = "OctetString"
_GenHWAddress_Object = MibScalar
genHWAddress = _GenHWAddress_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 6),
    _GenHWAddress_Type()
)
genHWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genHWAddress.setStatus("mandatory")


class _GenCableType_Type(Integer32):
    """Custom type genCableType based on Integer32"""
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
        *(("aui", 3),
          ("fiber100fx", 6),
          ("stp", 5),
          ("tenbase2", 1),
          ("tenbaseT", 2),
          ("utp", 4))
    )


_GenCableType_Type.__name__ = "Integer32"
_GenCableType_Object = MibScalar
genCableType = _GenCableType_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 7),
    _GenCableType_Type()
)
genCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCableType.setStatus("mandatory")


class _GenDateCode_Type(DisplayString):
    """Custom type genDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GenDateCode_Type.__name__ = "DisplayString"
_GenDateCode_Object = MibScalar
genDateCode = _GenDateCode_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 8),
    _GenDateCode_Type()
)
genDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDateCode.setStatus("mandatory")


class _GenVersion_Type(DisplayString):
    """Custom type genVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_GenVersion_Type.__name__ = "DisplayString"
_GenVersion_Object = MibScalar
genVersion = _GenVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 9),
    _GenVersion_Type()
)
genVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVersion.setStatus("mandatory")


class _GenConfigurationDirty_Type(Integer32):
    """Custom type genConfigurationDirty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_GenConfigurationDirty_Type.__name__ = "Integer32"
_GenConfigurationDirty_Object = MibScalar
genConfigurationDirty = _GenConfigurationDirty_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 10),
    _GenConfigurationDirty_Type()
)
genConfigurationDirty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genConfigurationDirty.setStatus("mandatory")


class _GenCompanyName_Type(DisplayString):
    """Custom type genCompanyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GenCompanyName_Type.__name__ = "DisplayString"
_GenCompanyName_Object = MibScalar
genCompanyName = _GenCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 11),
    _GenCompanyName_Type()
)
genCompanyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCompanyName.setStatus("mandatory")


class _GenCompanyLoc_Type(DisplayString):
    """Custom type genCompanyLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GenCompanyLoc_Type.__name__ = "DisplayString"
_GenCompanyLoc_Object = MibScalar
genCompanyLoc = _GenCompanyLoc_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 12),
    _GenCompanyLoc_Type()
)
genCompanyLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCompanyLoc.setStatus("mandatory")


class _GenCompanyPhone_Type(DisplayString):
    """Custom type genCompanyPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GenCompanyPhone_Type.__name__ = "DisplayString"
_GenCompanyPhone_Object = MibScalar
genCompanyPhone = _GenCompanyPhone_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 13),
    _GenCompanyPhone_Type()
)
genCompanyPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCompanyPhone.setStatus("mandatory")


class _GenCompanyTechSupport_Type(DisplayString):
    """Custom type genCompanyTechSupport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GenCompanyTechSupport_Type.__name__ = "DisplayString"
_GenCompanyTechSupport_Object = MibScalar
genCompanyTechSupport = _GenCompanyTechSupport_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 14),
    _GenCompanyTechSupport_Type()
)
genCompanyTechSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCompanyTechSupport.setStatus("mandatory")
_GenProtocols_ObjectIdentity = ObjectIdentity
genProtocols = _GenProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 1, 15)
)
_GenNumProtocols_Type = Integer32
_GenNumProtocols_Object = MibScalar
genNumProtocols = _GenNumProtocols_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 15, 1),
    _GenNumProtocols_Type()
)
genNumProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genNumProtocols.setStatus("mandatory")
_GenProtocolTable_Object = MibTable
genProtocolTable = _GenProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 15, 2)
)
if mibBuilder.loadTexts:
    genProtocolTable.setStatus("mandatory")
_GenProtocolEntry_Object = MibTableRow
genProtocolEntry = _GenProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 15, 2, 1)
)
genProtocolEntry.setIndexNames(
    (0, "ESI-MIB", "genProtocolIndex"),
)
if mibBuilder.loadTexts:
    genProtocolEntry.setStatus("mandatory")
_GenProtocolIndex_Type = Integer32
_GenProtocolIndex_Object = MibTableColumn
genProtocolIndex = _GenProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 15, 2, 1, 1),
    _GenProtocolIndex_Type()
)
genProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProtocolIndex.setStatus("mandatory")


class _GenProtocolDescr_Type(DisplayString):
    """Custom type genProtocolDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenProtocolDescr_Type.__name__ = "DisplayString"
_GenProtocolDescr_Object = MibTableColumn
genProtocolDescr = _GenProtocolDescr_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 15, 2, 1, 2),
    _GenProtocolDescr_Type()
)
genProtocolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProtocolDescr.setStatus("mandatory")


class _GenProtocolID_Type(Integer32):
    """Custom type genProtocolID based on Integer32"""
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
        *(("ethertalk", 5),
          ("lanmanger", 4),
          ("netware", 2),
          ("tcp-ip", 1),
          ("vines", 3))
    )


_GenProtocolID_Type.__name__ = "Integer32"
_GenProtocolID_Object = MibTableColumn
genProtocolID = _GenProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 15, 2, 1, 3),
    _GenProtocolID_Type()
)
genProtocolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genProtocolID.setStatus("mandatory")


class _GenSysUpTimeString_Type(DisplayString):
    """Custom type genSysUpTimeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_GenSysUpTimeString_Type.__name__ = "DisplayString"
_GenSysUpTimeString_Object = MibScalar
genSysUpTimeString = _GenSysUpTimeString_Object(
    (1, 3, 6, 1, 4, 1, 683, 1, 16),
    _GenSysUpTimeString_Type()
)
genSysUpTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSysUpTimeString.setStatus("mandatory")
_Commands_ObjectIdentity = ObjectIdentity
commands = _Commands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 2)
)
_CmdGroupVersion_Type = Integer32
_CmdGroupVersion_Object = MibScalar
cmdGroupVersion = _CmdGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 2, 1),
    _CmdGroupVersion_Type()
)
cmdGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdGroupVersion.setStatus("mandatory")


class _CmdReset_Type(Integer32):
    """Custom type cmdReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmdReset_Type.__name__ = "Integer32"
_CmdReset_Object = MibScalar
cmdReset = _CmdReset_Object(
    (1, 3, 6, 1, 4, 1, 683, 2, 2),
    _CmdReset_Type()
)
cmdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdReset.setStatus("optional")


class _CmdPrintConfig_Type(Integer32):
    """Custom type cmdPrintConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmdPrintConfig_Type.__name__ = "Integer32"
_CmdPrintConfig_Object = MibScalar
cmdPrintConfig = _CmdPrintConfig_Object(
    (1, 3, 6, 1, 4, 1, 683, 2, 3),
    _CmdPrintConfig_Type()
)
cmdPrintConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdPrintConfig.setStatus("optional")


class _CmdRestoreDefaults_Type(Integer32):
    """Custom type cmdRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmdRestoreDefaults_Type.__name__ = "Integer32"
_CmdRestoreDefaults_Object = MibScalar
cmdRestoreDefaults = _CmdRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 683, 2, 4),
    _CmdRestoreDefaults_Type()
)
cmdRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdRestoreDefaults.setStatus("optional")
_EsiSNMP_ObjectIdentity = ObjectIdentity
esiSNMP = _EsiSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 3)
)
_SnmpGroupVersion_Type = Integer32
_SnmpGroupVersion_Object = MibScalar
snmpGroupVersion = _SnmpGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 3, 1),
    _SnmpGroupVersion_Type()
)
snmpGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGroupVersion.setStatus("mandatory")
_EsiSNMPCommands_ObjectIdentity = ObjectIdentity
esiSNMPCommands = _EsiSNMPCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 3, 2)
)


class _SnmpRestoreDefaults_Type(Integer32):
    """Custom type snmpRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SnmpRestoreDefaults_Type.__name__ = "Integer32"
_SnmpRestoreDefaults_Object = MibScalar
snmpRestoreDefaults = _SnmpRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 683, 3, 2, 1),
    _SnmpRestoreDefaults_Type()
)
snmpRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpRestoreDefaults.setStatus("optional")


class _SnmpGetCommunityName_Type(DisplayString):
    """Custom type snmpGetCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SnmpGetCommunityName_Type.__name__ = "DisplayString"
_SnmpGetCommunityName_Object = MibScalar
snmpGetCommunityName = _SnmpGetCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 683, 3, 3),
    _SnmpGetCommunityName_Type()
)
snmpGetCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGetCommunityName.setStatus("optional")


class _SnmpSetCommunityName_Type(DisplayString):
    """Custom type snmpSetCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SnmpSetCommunityName_Type.__name__ = "DisplayString"
_SnmpSetCommunityName_Object = MibScalar
snmpSetCommunityName = _SnmpSetCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 683, 3, 4),
    _SnmpSetCommunityName_Type()
)
snmpSetCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSetCommunityName.setStatus("optional")


class _SnmpTrapCommunityName_Type(DisplayString):
    """Custom type snmpTrapCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SnmpTrapCommunityName_Type.__name__ = "DisplayString"
_SnmpTrapCommunityName_Object = MibScalar
snmpTrapCommunityName = _SnmpTrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 683, 3, 5),
    _SnmpTrapCommunityName_Type()
)
snmpTrapCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunityName.setStatus("optional")
_Driver_ObjectIdentity = ObjectIdentity
driver = _Driver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 4)
)
_DriverGroupVersion_Type = Integer32
_DriverGroupVersion_Object = MibScalar
driverGroupVersion = _DriverGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 4, 1),
    _DriverGroupVersion_Type()
)
driverGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverGroupVersion.setStatus("mandatory")
_DriverRXPackets_Type = Counter32
_DriverRXPackets_Object = MibScalar
driverRXPackets = _DriverRXPackets_Object(
    (1, 3, 6, 1, 4, 1, 683, 4, 2),
    _DriverRXPackets_Type()
)
driverRXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverRXPackets.setStatus("mandatory")
_DriverTXPackets_Type = Counter32
_DriverTXPackets_Object = MibScalar
driverTXPackets = _DriverTXPackets_Object(
    (1, 3, 6, 1, 4, 1, 683, 4, 3),
    _DriverTXPackets_Type()
)
driverTXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverTXPackets.setStatus("mandatory")
_DriverRXPacketsUnavailable_Type = Counter32
_DriverRXPacketsUnavailable_Object = MibScalar
driverRXPacketsUnavailable = _DriverRXPacketsUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 683, 4, 4),
    _DriverRXPacketsUnavailable_Type()
)
driverRXPacketsUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverRXPacketsUnavailable.setStatus("mandatory")
_DriverRXPacketErrors_Type = Counter32
_DriverRXPacketErrors_Object = MibScalar
driverRXPacketErrors = _DriverRXPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 683, 4, 5),
    _DriverRXPacketErrors_Type()
)
driverRXPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverRXPacketErrors.setStatus("mandatory")
_DriverTXPacketErrors_Type = Counter32
_DriverTXPacketErrors_Object = MibScalar
driverTXPacketErrors = _DriverTXPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 683, 4, 6),
    _DriverTXPacketErrors_Type()
)
driverTXPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverTXPacketErrors.setStatus("mandatory")
_DriverTXPacketRetries_Type = Counter32
_DriverTXPacketRetries_Object = MibScalar
driverTXPacketRetries = _DriverTXPacketRetries_Object(
    (1, 3, 6, 1, 4, 1, 683, 4, 7),
    _DriverTXPacketRetries_Type()
)
driverTXPacketRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverTXPacketRetries.setStatus("mandatory")
_DriverChecksumErrors_Type = Counter32
_DriverChecksumErrors_Object = MibScalar
driverChecksumErrors = _DriverChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 683, 4, 8),
    _DriverChecksumErrors_Type()
)
driverChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driverChecksumErrors.setStatus("mandatory")
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 5)
)
_TrGroupVersion_Type = Integer32
_TrGroupVersion_Object = MibScalar
trGroupVersion = _TrGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 5, 1),
    _TrGroupVersion_Type()
)
trGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trGroupVersion.setStatus("mandatory")
_TrCommands_ObjectIdentity = ObjectIdentity
trCommands = _TrCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 5, 2)
)


class _TrRestoreDefaults_Type(Integer32):
    """Custom type trRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrRestoreDefaults_Type.__name__ = "Integer32"
_TrRestoreDefaults_Object = MibScalar
trRestoreDefaults = _TrRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 683, 5, 2, 1),
    _TrRestoreDefaults_Type()
)
trRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trRestoreDefaults.setStatus("optional")
_TrConfigure_ObjectIdentity = ObjectIdentity
trConfigure = _TrConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 5, 3)
)


class _TrPriority_Type(Integer32):
    """Custom type trPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_TrPriority_Type.__name__ = "Integer32"
_TrPriority_Object = MibScalar
trPriority = _TrPriority_Object(
    (1, 3, 6, 1, 4, 1, 683, 5, 3, 1),
    _TrPriority_Type()
)
trPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trPriority.setStatus("optional")


class _TrEarlyTokenRelease_Type(Integer32):
    """Custom type trEarlyTokenRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TrEarlyTokenRelease_Type.__name__ = "Integer32"
_TrEarlyTokenRelease_Object = MibScalar
trEarlyTokenRelease = _TrEarlyTokenRelease_Object(
    (1, 3, 6, 1, 4, 1, 683, 5, 3, 2),
    _TrEarlyTokenRelease_Type()
)
trEarlyTokenRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trEarlyTokenRelease.setStatus("optional")


class _TrPacketSize_Type(Integer32):
    """Custom type trPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("four-k", 3),
          ("one-k", 1),
          ("two-k", 2))
    )


_TrPacketSize_Type.__name__ = "Integer32"
_TrPacketSize_Object = MibScalar
trPacketSize = _TrPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 683, 5, 3, 3),
    _TrPacketSize_Type()
)
trPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trPacketSize.setStatus("optional")


class _TrRouting_Type(Integer32):
    """Custom type trRouting based on Integer32"""
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
        *(("all-None", 2),
          ("off", 1),
          ("single-All", 3),
          ("single-None", 4))
    )


_TrRouting_Type.__name__ = "Integer32"
_TrRouting_Object = MibScalar
trRouting = _TrRouting_Object(
    (1, 3, 6, 1, 4, 1, 683, 5, 3, 4),
    _TrRouting_Type()
)
trRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trRouting.setStatus("optional")


class _TrLocallyAdminAddr_Type(OctetString):
    """Custom type trLocallyAdminAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TrLocallyAdminAddr_Type.__name__ = "OctetString"
_TrLocallyAdminAddr_Object = MibScalar
trLocallyAdminAddr = _TrLocallyAdminAddr_Object(
    (1, 3, 6, 1, 4, 1, 683, 5, 3, 5),
    _TrLocallyAdminAddr_Type()
)
trLocallyAdminAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trLocallyAdminAddr.setStatus("optional")
_PrintServers_ObjectIdentity = ObjectIdentity
printServers = _PrintServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6)
)
_PsGeneral_ObjectIdentity = ObjectIdentity
psGeneral = _PsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 1)
)
_PsGroupVersion_Type = Integer32
_PsGroupVersion_Object = MibScalar
psGroupVersion = _PsGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 1, 1),
    _PsGroupVersion_Type()
)
psGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psGroupVersion.setStatus("mandatory")


class _PsJetAdminEnabled_Type(Integer32):
    """Custom type psJetAdminEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PsJetAdminEnabled_Type.__name__ = "Integer32"
_PsJetAdminEnabled_Object = MibScalar
psJetAdminEnabled = _PsJetAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 1, 2),
    _PsJetAdminEnabled_Type()
)
psJetAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psJetAdminEnabled.setStatus("mandatory")


class _PsVerifyConfiguration_Type(Integer32):
    """Custom type psVerifyConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("getvalue", 0),
          ("serial-configuration", 1))
    )


_PsVerifyConfiguration_Type.__name__ = "Integer32"
_PsVerifyConfiguration_Object = MibScalar
psVerifyConfiguration = _PsVerifyConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 1, 3),
    _PsVerifyConfiguration_Type()
)
psVerifyConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psVerifyConfiguration.setStatus("optional")
_PsOutput_ObjectIdentity = ObjectIdentity
psOutput = _PsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 2)
)
_OutputGroupVersion_Type = Integer32
_OutputGroupVersion_Object = MibScalar
outputGroupVersion = _OutputGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 1),
    _OutputGroupVersion_Type()
)
outputGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputGroupVersion.setStatus("mandatory")
_OutputCommands_ObjectIdentity = ObjectIdentity
outputCommands = _OutputCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 2)
)


class _OutputRestoreDefaults_Type(Integer32):
    """Custom type outputRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_OutputRestoreDefaults_Type.__name__ = "Integer32"
_OutputRestoreDefaults_Object = MibScalar
outputRestoreDefaults = _OutputRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 2, 1),
    _OutputRestoreDefaults_Type()
)
outputRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputRestoreDefaults.setStatus("mandatory")
_OutputCommandsTable_Object = MibTable
outputCommandsTable = _OutputCommandsTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    outputCommandsTable.setStatus("mandatory")
_OutputCommandsEntry_Object = MibTableRow
outputCommandsEntry = _OutputCommandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 2, 2, 1)
)
outputCommandsEntry.setIndexNames(
    (0, "ESI-MIB", "outputIndex"),
)
if mibBuilder.loadTexts:
    outputCommandsEntry.setStatus("mandatory")


class _OutputCancelCurrentJob_Type(Integer32):
    """Custom type outputCancelCurrentJob based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_OutputCancelCurrentJob_Type.__name__ = "Integer32"
_OutputCancelCurrentJob_Object = MibTableColumn
outputCancelCurrentJob = _OutputCancelCurrentJob_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 2, 2, 1, 1),
    _OutputCancelCurrentJob_Type()
)
outputCancelCurrentJob.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputCancelCurrentJob.setStatus("optional")
_OutputConfigure_ObjectIdentity = ObjectIdentity
outputConfigure = _OutputConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3)
)
_OutputNumPorts_Type = Integer32
_OutputNumPorts_Object = MibScalar
outputNumPorts = _OutputNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 1),
    _OutputNumPorts_Type()
)
outputNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputNumPorts.setStatus("mandatory")
_OutputTable_Object = MibTable
outputTable = _OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2)
)
if mibBuilder.loadTexts:
    outputTable.setStatus("mandatory")
_OutputEntry_Object = MibTableRow
outputEntry = _OutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1)
)
outputEntry.setIndexNames(
    (0, "ESI-MIB", "outputIndex"),
)
if mibBuilder.loadTexts:
    outputEntry.setStatus("mandatory")
_OutputIndex_Type = Integer32
_OutputIndex_Object = MibTableColumn
outputIndex = _OutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 1),
    _OutputIndex_Type()
)
outputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputIndex.setStatus("mandatory")


class _OutputName_Type(DisplayString):
    """Custom type outputName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_OutputName_Type.__name__ = "DisplayString"
_OutputName_Object = MibTableColumn
outputName = _OutputName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 2),
    _OutputName_Type()
)
outputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputName.setStatus("mandatory")


class _OutputStatusString_Type(DisplayString):
    """Custom type outputStatusString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_OutputStatusString_Type.__name__ = "DisplayString"
_OutputStatusString_Object = MibTableColumn
outputStatusString = _OutputStatusString_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 3),
    _OutputStatusString_Type()
)
outputStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputStatusString.setStatus("mandatory")


class _OutputStatus_Type(Integer32):
    """Custom type outputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-Line", 2),
          ("on-Line", 1))
    )


_OutputStatus_Type.__name__ = "Integer32"
_OutputStatus_Object = MibTableColumn
outputStatus = _OutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 4),
    _OutputStatus_Type()
)
outputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputStatus.setStatus("mandatory")


class _OutputExtendedStatus_Type(Integer32):
    """Custom type outputExtendedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              15)
        )
    )
    namedValues = NamedValues(
        *(("door-Open", 6),
          ("no-Printer-Attached", 2),
          ("none", 1),
          ("paper-Jam", 5),
          ("paper-Out", 4),
          ("printer-Error", 15),
          ("toner-Low", 3))
    )


_OutputExtendedStatus_Type.__name__ = "Integer32"
_OutputExtendedStatus_Object = MibTableColumn
outputExtendedStatus = _OutputExtendedStatus_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 5),
    _OutputExtendedStatus_Type()
)
outputExtendedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputExtendedStatus.setStatus("mandatory")


class _OutputPrinter_Type(Integer32):
    """Custom type outputPrinter based on Integer32"""
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
        *(("hp-III", 1),
          ("hp-IIISi", 2),
          ("ibm", 3),
          ("no-Specific-Printer", 4))
    )


_OutputPrinter_Type.__name__ = "Integer32"
_OutputPrinter_Object = MibTableColumn
outputPrinter = _OutputPrinter_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 6),
    _OutputPrinter_Type()
)
outputPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputPrinter.setStatus("optional")


class _OutputLanguageSwitching_Type(Integer32):
    """Custom type outputLanguageSwitching based on Integer32"""
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
        *(("als", 4),
          ("off", 1),
          ("pcl", 2),
          ("postScript", 3))
    )


_OutputLanguageSwitching_Type.__name__ = "Integer32"
_OutputLanguageSwitching_Object = MibTableColumn
outputLanguageSwitching = _OutputLanguageSwitching_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 7),
    _OutputLanguageSwitching_Type()
)
outputLanguageSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputLanguageSwitching.setStatus("optional")


class _OutputConfigLanguage_Type(Integer32):
    """Custom type outputConfigLanguage based on Integer32"""
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
        *(("epl-zpl", 5),
          ("off", 4),
          ("pcl", 2),
          ("postScript", 3),
          ("text", 1))
    )


_OutputConfigLanguage_Type.__name__ = "Integer32"
_OutputConfigLanguage_Object = MibTableColumn
outputConfigLanguage = _OutputConfigLanguage_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 8),
    _OutputConfigLanguage_Type()
)
outputConfigLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfigLanguage.setStatus("mandatory")


class _OutputPCLString_Type(OctetString):
    """Custom type outputPCLString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )


_OutputPCLString_Type.__name__ = "OctetString"
_OutputPCLString_Object = MibTableColumn
outputPCLString = _OutputPCLString_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 9),
    _OutputPCLString_Type()
)
outputPCLString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputPCLString.setStatus("optional")


class _OutputPSString_Type(OctetString):
    """Custom type outputPSString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(127, 127),
    )


_OutputPSString_Type.__name__ = "OctetString"
_OutputPSString_Object = MibTableColumn
outputPSString = _OutputPSString_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 10),
    _OutputPSString_Type()
)
outputPSString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputPSString.setStatus("optional")


class _OutputCascaded_Type(Integer32):
    """Custom type outputCascaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_OutputCascaded_Type.__name__ = "Integer32"
_OutputCascaded_Object = MibTableColumn
outputCascaded = _OutputCascaded_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 11),
    _OutputCascaded_Type()
)
outputCascaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputCascaded.setStatus("optional")


class _OutputSetting_Type(Integer32):
    """Custom type outputSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32758,
              32759,
              32760,
              32761,
              32762,
              32763,
              32764,
              32765,
              32766,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("extendedLink", 32767),
          ("ieee-1284-ecp-or-fast-nibble-mode", 32766),
          ("ieee-1284-std-nibble-mode", 32763),
          ("internal", 32765),
          ("parallel-compatibility-no-bidi", 32762),
          ("serial-bidirectional", 32759),
          ("serial-infrared", 32758),
          ("serial-input", 32761),
          ("serial-unidirectional", 32760),
          ("z-Link", 32764))
    )


_OutputSetting_Type.__name__ = "Integer32"
_OutputSetting_Object = MibTableColumn
outputSetting = _OutputSetting_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 12),
    _OutputSetting_Type()
)
outputSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputSetting.setStatus("mandatory")


class _OutputOwner_Type(Integer32):
    """Custom type outputOwner based on Integer32"""
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
        *(("config-Page", 7),
          ("etherTalk", 6),
          ("lanManager", 5),
          ("netware", 3),
          ("no-Owner", 1),
          ("tcpip", 2),
          ("vines", 4))
    )


_OutputOwner_Type.__name__ = "Integer32"
_OutputOwner_Object = MibTableColumn
outputOwner = _OutputOwner_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 13),
    _OutputOwner_Type()
)
outputOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputOwner.setStatus("mandatory")


class _OutputBIDIStatusEnabled_Type(Integer32):
    """Custom type outputBIDIStatusEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_OutputBIDIStatusEnabled_Type.__name__ = "Integer32"
_OutputBIDIStatusEnabled_Object = MibTableColumn
outputBIDIStatusEnabled = _OutputBIDIStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 14),
    _OutputBIDIStatusEnabled_Type()
)
outputBIDIStatusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputBIDIStatusEnabled.setStatus("optional")


class _OutputPrinterModel_Type(DisplayString):
    """Custom type outputPrinterModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_OutputPrinterModel_Type.__name__ = "DisplayString"
_OutputPrinterModel_Object = MibTableColumn
outputPrinterModel = _OutputPrinterModel_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 15),
    _OutputPrinterModel_Type()
)
outputPrinterModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPrinterModel.setStatus("optional")


class _OutputPrinterDisplay_Type(DisplayString):
    """Custom type outputPrinterDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_OutputPrinterDisplay_Type.__name__ = "DisplayString"
_OutputPrinterDisplay_Object = MibTableColumn
outputPrinterDisplay = _OutputPrinterDisplay_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 16),
    _OutputPrinterDisplay_Type()
)
outputPrinterDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPrinterDisplay.setStatus("optional")


class _OutputCapabilities_Type(Integer32):
    """Custom type outputCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              262144,
              524288,
              1048576,
              2097152,
              4194304,
              8388608,
              16777216,
              33554432,
              67108864,
              134217728,
              268435456,
              536870912,
              1073741824)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 33554432),
          ("extendedLink", 268435456),
          ("ieee-1284-ecp-or-fast-nibble-mode", 1073741824),
          ("ieee-1284-std-nibble-mode", 8388608),
          ("internal", 536870912),
          ("parallel-compatibility-no-bidi", 4194304),
          ("serial-Output", 134217728),
          ("serial-Software-Handshake", 67108864),
          ("serial-Uni-Baud-115200", 16),
          ("serial-Uni-Baud-19200", 2),
          ("serial-Uni-Baud-38400", 4),
          ("serial-Uni-Baud-57600", 8),
          ("serial-Uni-Baud-9600", 1),
          ("serial-bidi-Baud-19200", 64),
          ("serial-bidi-Baud-38400", 128),
          ("serial-bidi-Baud-57600", 256),
          ("serial-bidi-Baud-9600", 32),
          ("serial-config-settings", 2097152),
          ("serial-in", 1048576),
          ("serial-irin", 524288),
          ("z-link", 16777216),
          ("zpl-epl-capable", 262144))
    )


_OutputCapabilities_Type.__name__ = "Integer32"
_OutputCapabilities_Object = MibTableColumn
outputCapabilities = _OutputCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 17),
    _OutputCapabilities_Type()
)
outputCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCapabilities.setStatus("mandatory")


class _OutputHandshake_Type(Integer32):
    """Custom type outputHandshake based on Integer32"""
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
        *(("hardware", 3),
          ("hardware-Software", 2),
          ("not-Supported", 1),
          ("software", 4))
    )


_OutputHandshake_Type.__name__ = "Integer32"
_OutputHandshake_Object = MibTableColumn
outputHandshake = _OutputHandshake_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 18),
    _OutputHandshake_Type()
)
outputHandshake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputHandshake.setStatus("optional")


class _OutputDataBits_Type(Integer32):
    """Custom type outputDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("eight-bits", 8),
          ("not-Supported", 255),
          ("seven-bits", 7))
    )


_OutputDataBits_Type.__name__ = "Integer32"
_OutputDataBits_Object = MibTableColumn
outputDataBits = _OutputDataBits_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 19),
    _OutputDataBits_Type()
)
outputDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputDataBits.setStatus("optional")


class _OutputStopBits_Type(Integer32):
    """Custom type outputStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-Supported", 255),
          ("one-bit", 1),
          ("two-bits", 2))
    )


_OutputStopBits_Type.__name__ = "Integer32"
_OutputStopBits_Object = MibTableColumn
outputStopBits = _OutputStopBits_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 20),
    _OutputStopBits_Type()
)
outputStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputStopBits.setStatus("optional")


class _OutputParity_Type(Integer32):
    """Custom type outputParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("not-Supported", 255),
          ("odd", 2))
    )


_OutputParity_Type.__name__ = "Integer32"
_OutputParity_Object = MibTableColumn
outputParity = _OutputParity_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 21),
    _OutputParity_Type()
)
outputParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputParity.setStatus("optional")


class _OutputBaudRate_Type(Integer32):
    """Custom type outputBaudRate based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional-19200", 7),
          ("bidirectional-38400", 8),
          ("bidirectional-57600", 9),
          ("bidirectional-9600", 6),
          ("unidirectional-115200", 5),
          ("unidirectional-19200", 2),
          ("unidirectional-38400", 3),
          ("unidirectional-57600", 4),
          ("unidirectional-9600", 1))
    )


_OutputBaudRate_Type.__name__ = "Integer32"
_OutputBaudRate_Object = MibTableColumn
outputBaudRate = _OutputBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 22),
    _OutputBaudRate_Type()
)
outputBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputBaudRate.setStatus("optional")


class _OutputProtocolManager_Type(Integer32):
    """Custom type outputProtocolManager based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protocol-1284-4", 2),
          ("protocol-compatibility", 1),
          ("protocol-none", 0))
    )


_OutputProtocolManager_Type.__name__ = "Integer32"
_OutputProtocolManager_Object = MibTableColumn
outputProtocolManager = _OutputProtocolManager_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 3, 2, 1, 23),
    _OutputProtocolManager_Type()
)
outputProtocolManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputProtocolManager.setStatus("optional")
_OutputDisplayMask_Type = Integer32
_OutputDisplayMask_Object = MibScalar
outputDisplayMask = _OutputDisplayMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 4),
    _OutputDisplayMask_Type()
)
outputDisplayMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputDisplayMask.setStatus("mandatory")
_OutputAvailableTrapsMask_Type = Integer32
_OutputAvailableTrapsMask_Object = MibScalar
outputAvailableTrapsMask = _OutputAvailableTrapsMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 5),
    _OutputAvailableTrapsMask_Type()
)
outputAvailableTrapsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputAvailableTrapsMask.setStatus("mandatory")
_OutputJobLog_ObjectIdentity = ObjectIdentity
outputJobLog = _OutputJobLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 6)
)
_OutputNumLogEntries_Type = Integer32
_OutputNumLogEntries_Object = MibScalar
outputNumLogEntries = _OutputNumLogEntries_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 6, 1),
    _OutputNumLogEntries_Type()
)
outputNumLogEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputNumLogEntries.setStatus("mandatory")
_OutputJobLogTable_Object = MibTable
outputJobLogTable = _OutputJobLogTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 6, 2)
)
if mibBuilder.loadTexts:
    outputJobLogTable.setStatus("mandatory")
_OutputJobLogEntry_Object = MibTableRow
outputJobLogEntry = _OutputJobLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 6, 2, 1)
)
outputJobLogEntry.setIndexNames(
    (0, "ESI-MIB", "outputIndex"),
)
if mibBuilder.loadTexts:
    outputJobLogEntry.setStatus("mandatory")


class _OutputJobLogInformation_Type(DisplayString):
    """Custom type outputJobLogInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_OutputJobLogInformation_Type.__name__ = "DisplayString"
_OutputJobLogInformation_Object = MibTableColumn
outputJobLogInformation = _OutputJobLogInformation_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 6, 2, 1, 1),
    _OutputJobLogInformation_Type()
)
outputJobLogInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputJobLogInformation.setStatus("mandatory")


class _OutputJobLogTime_Type(DisplayString):
    """Custom type outputJobLogTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_OutputJobLogTime_Type.__name__ = "DisplayString"
_OutputJobLogTime_Object = MibTableColumn
outputJobLogTime = _OutputJobLogTime_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 6, 2, 1, 2),
    _OutputJobLogTime_Type()
)
outputJobLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputJobLogTime.setStatus("mandatory")
_OutputTotalJobTable_Object = MibTable
outputTotalJobTable = _OutputTotalJobTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 6, 3)
)
if mibBuilder.loadTexts:
    outputTotalJobTable.setStatus("mandatory")
_OutputTotalJobEntry_Object = MibTableRow
outputTotalJobEntry = _OutputTotalJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 6, 3, 1)
)
outputTotalJobEntry.setIndexNames(
    (0, "ESI-MIB", "outputTotalJobIndex"),
)
if mibBuilder.loadTexts:
    outputTotalJobEntry.setStatus("mandatory")
_OutputTotalJobIndex_Type = Integer32
_OutputTotalJobIndex_Object = MibTableColumn
outputTotalJobIndex = _OutputTotalJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 6, 3, 1, 1),
    _OutputTotalJobIndex_Type()
)
outputTotalJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTotalJobIndex.setStatus("mandatory")
_OutputTotalJobsLogged_Type = Integer32
_OutputTotalJobsLogged_Object = MibTableColumn
outputTotalJobsLogged = _OutputTotalJobsLogged_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 2, 6, 3, 1, 2),
    _OutputTotalJobsLogged_Type()
)
outputTotalJobsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputTotalJobsLogged.setStatus("mandatory")
_PsProtocols_ObjectIdentity = ObjectIdentity
psProtocols = _PsProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3)
)
_Tcpip_ObjectIdentity = ObjectIdentity
tcpip = _Tcpip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1)
)
_TcpipGroupVersion_Type = Integer32
_TcpipGroupVersion_Object = MibScalar
tcpipGroupVersion = _TcpipGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 1),
    _TcpipGroupVersion_Type()
)
tcpipGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipGroupVersion.setStatus("mandatory")


class _TcpipEnabled_Type(Integer32):
    """Custom type tcpipEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipEnabled_Type.__name__ = "Integer32"
_TcpipEnabled_Object = MibScalar
tcpipEnabled = _TcpipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 2),
    _TcpipEnabled_Type()
)
tcpipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipEnabled.setStatus("optional")
_TcpipCommands_ObjectIdentity = ObjectIdentity
tcpipCommands = _TcpipCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 3)
)


class _TcpipRestoreDefaults_Type(Integer32):
    """Custom type tcpipRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipRestoreDefaults_Type.__name__ = "Integer32"
_TcpipRestoreDefaults_Object = MibScalar
tcpipRestoreDefaults = _TcpipRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 3, 1),
    _TcpipRestoreDefaults_Type()
)
tcpipRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipRestoreDefaults.setStatus("optional")


class _TcpipFirmwareUpgrade_Type(Integer32):
    """Custom type tcpipFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipFirmwareUpgrade_Type.__name__ = "Integer32"
_TcpipFirmwareUpgrade_Object = MibScalar
tcpipFirmwareUpgrade = _TcpipFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 3, 2),
    _TcpipFirmwareUpgrade_Type()
)
tcpipFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipFirmwareUpgrade.setStatus("optional")
_TcpipConfigure_ObjectIdentity = ObjectIdentity
tcpipConfigure = _TcpipConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4)
)
_TcpipIPAddress_Type = IpAddress
_TcpipIPAddress_Object = MibScalar
tcpipIPAddress = _TcpipIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 1),
    _TcpipIPAddress_Type()
)
tcpipIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipIPAddress.setStatus("optional")
_TcpipDefaultGateway_Type = IpAddress
_TcpipDefaultGateway_Object = MibScalar
tcpipDefaultGateway = _TcpipDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 2),
    _TcpipDefaultGateway_Type()
)
tcpipDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipDefaultGateway.setStatus("optional")
_TcpipSubnetMask_Type = IpAddress
_TcpipSubnetMask_Object = MibScalar
tcpipSubnetMask = _TcpipSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 3),
    _TcpipSubnetMask_Type()
)
tcpipSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSubnetMask.setStatus("optional")


class _TcpipUsingNetProtocols_Type(Integer32):
    """Custom type tcpipUsingNetProtocols based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipUsingNetProtocols_Type.__name__ = "Integer32"
_TcpipUsingNetProtocols_Object = MibScalar
tcpipUsingNetProtocols = _TcpipUsingNetProtocols_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 4),
    _TcpipUsingNetProtocols_Type()
)
tcpipUsingNetProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipUsingNetProtocols.setStatus("optional")
_TcpipBootProtocolsEnabled_Type = Integer32
_TcpipBootProtocolsEnabled_Object = MibScalar
tcpipBootProtocolsEnabled = _TcpipBootProtocolsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 5),
    _TcpipBootProtocolsEnabled_Type()
)
tcpipBootProtocolsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipBootProtocolsEnabled.setStatus("optional")


class _TcpipIPAddressSource_Type(Integer32):
    """Custom type tcpipIPAddressSource based on Integer32"""
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
        *(("bootp", 4),
          ("default", 2),
          ("dhcp", 5),
          ("glean", 6),
          ("permanent", 1),
          ("rarp", 3))
    )


_TcpipIPAddressSource_Type.__name__ = "Integer32"
_TcpipIPAddressSource_Object = MibScalar
tcpipIPAddressSource = _TcpipIPAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 6),
    _TcpipIPAddressSource_Type()
)
tcpipIPAddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipIPAddressSource.setStatus("optional")
_TcpipIPAddressServerAddress_Type = IpAddress
_TcpipIPAddressServerAddress_Object = MibScalar
tcpipIPAddressServerAddress = _TcpipIPAddressServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 7),
    _TcpipIPAddressServerAddress_Type()
)
tcpipIPAddressServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipIPAddressServerAddress.setStatus("optional")


class _TcpipTimeoutChecking_Type(Integer32):
    """Custom type tcpipTimeoutChecking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipTimeoutChecking_Type.__name__ = "Integer32"
_TcpipTimeoutChecking_Object = MibScalar
tcpipTimeoutChecking = _TcpipTimeoutChecking_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 8),
    _TcpipTimeoutChecking_Type()
)
tcpipTimeoutChecking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipTimeoutChecking.setStatus("optional")
_TcpipNumTraps_Type = Integer32
_TcpipNumTraps_Object = MibScalar
tcpipNumTraps = _TcpipNumTraps_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 9),
    _TcpipNumTraps_Type()
)
tcpipNumTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipNumTraps.setStatus("mandatory")
_TcpipTrapTable_Object = MibTable
tcpipTrapTable = _TcpipTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 10)
)
if mibBuilder.loadTexts:
    tcpipTrapTable.setStatus("mandatory")
_TcpipTrapEntry_Object = MibTableRow
tcpipTrapEntry = _TcpipTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 10, 1)
)
tcpipTrapEntry.setIndexNames(
    (0, "ESI-MIB", "tcpipTrapIndex"),
)
if mibBuilder.loadTexts:
    tcpipTrapEntry.setStatus("mandatory")
_TcpipTrapIndex_Type = Integer32
_TcpipTrapIndex_Object = MibTableColumn
tcpipTrapIndex = _TcpipTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 10, 1, 1),
    _TcpipTrapIndex_Type()
)
tcpipTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipTrapIndex.setStatus("mandatory")
_TcpipTrapDestination_Type = IpAddress
_TcpipTrapDestination_Object = MibTableColumn
tcpipTrapDestination = _TcpipTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 10, 1, 2),
    _TcpipTrapDestination_Type()
)
tcpipTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipTrapDestination.setStatus("optional")
_TcpipProtocolTrapMask_Type = Integer32
_TcpipProtocolTrapMask_Object = MibTableColumn
tcpipProtocolTrapMask = _TcpipProtocolTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 10, 1, 3),
    _TcpipProtocolTrapMask_Type()
)
tcpipProtocolTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipProtocolTrapMask.setStatus("optional")
_TcpipPrinterTrapMask_Type = Integer32
_TcpipPrinterTrapMask_Object = MibTableColumn
tcpipPrinterTrapMask = _TcpipPrinterTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 10, 1, 4),
    _TcpipPrinterTrapMask_Type()
)
tcpipPrinterTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPrinterTrapMask.setStatus("optional")
_TcpipOutputTrapMask_Type = Integer32
_TcpipOutputTrapMask_Object = MibTableColumn
tcpipOutputTrapMask = _TcpipOutputTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 10, 1, 5),
    _TcpipOutputTrapMask_Type()
)
tcpipOutputTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipOutputTrapMask.setStatus("optional")


class _TcpipBanners_Type(Integer32):
    """Custom type tcpipBanners based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipBanners_Type.__name__ = "Integer32"
_TcpipBanners_Object = MibScalar
tcpipBanners = _TcpipBanners_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 11),
    _TcpipBanners_Type()
)
tcpipBanners.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipBanners.setStatus("optional")
_TcpipWinsAddress_Type = IpAddress
_TcpipWinsAddress_Object = MibScalar
tcpipWinsAddress = _TcpipWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 12),
    _TcpipWinsAddress_Type()
)
tcpipWinsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWinsAddress.setStatus("optional")


class _TcpipWinsAddressSource_Type(Integer32):
    """Custom type tcpipWinsAddressSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("permanent", 2))
    )


_TcpipWinsAddressSource_Type.__name__ = "Integer32"
_TcpipWinsAddressSource_Object = MibScalar
tcpipWinsAddressSource = _TcpipWinsAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 13),
    _TcpipWinsAddressSource_Type()
)
tcpipWinsAddressSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWinsAddressSource.setStatus("optional")


class _TcpipConfigPassword_Type(DisplayString):
    """Custom type tcpipConfigPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 24),
    )


_TcpipConfigPassword_Type.__name__ = "DisplayString"
_TcpipConfigPassword_Object = MibScalar
tcpipConfigPassword = _TcpipConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 14),
    _TcpipConfigPassword_Type()
)
tcpipConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipConfigPassword.setStatus("optional")


class _TcpipTimeoutCheckingValue_Type(Integer32):
    """Custom type tcpipTimeoutCheckingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TcpipTimeoutCheckingValue_Type.__name__ = "Integer32"
_TcpipTimeoutCheckingValue_Object = MibScalar
tcpipTimeoutCheckingValue = _TcpipTimeoutCheckingValue_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 15),
    _TcpipTimeoutCheckingValue_Type()
)
tcpipTimeoutCheckingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipTimeoutCheckingValue.setStatus("optional")


class _TcpipArpInterval_Type(Integer32):
    """Custom type tcpipArpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_TcpipArpInterval_Type.__name__ = "Integer32"
_TcpipArpInterval_Object = MibScalar
tcpipArpInterval = _TcpipArpInterval_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 16),
    _TcpipArpInterval_Type()
)
tcpipArpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipArpInterval.setStatus("optional")
_TcpipRawPortNumber_Type = Integer32
_TcpipRawPortNumber_Object = MibScalar
tcpipRawPortNumber = _TcpipRawPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 17),
    _TcpipRawPortNumber_Type()
)
tcpipRawPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipRawPortNumber.setStatus("optional")
_TcpipNumSecurity_Type = Integer32
_TcpipNumSecurity_Object = MibScalar
tcpipNumSecurity = _TcpipNumSecurity_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 18),
    _TcpipNumSecurity_Type()
)
tcpipNumSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipNumSecurity.setStatus("mandatory")
_TcpipSecurityTable_Object = MibTable
tcpipSecurityTable = _TcpipSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 19)
)
if mibBuilder.loadTexts:
    tcpipSecurityTable.setStatus("mandatory")
_TcpipSecurityEntry_Object = MibTableRow
tcpipSecurityEntry = _TcpipSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 19, 1)
)
tcpipSecurityEntry.setIndexNames(
    (0, "ESI-MIB", "tcpipSecurityIndex"),
)
if mibBuilder.loadTexts:
    tcpipSecurityEntry.setStatus("mandatory")
_TcpipSecurityIndex_Type = Integer32
_TcpipSecurityIndex_Object = MibTableColumn
tcpipSecurityIndex = _TcpipSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 19, 1, 1),
    _TcpipSecurityIndex_Type()
)
tcpipSecurityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipSecurityIndex.setStatus("mandatory")
_TcpipSecureStartIPAddress_Type = IpAddress
_TcpipSecureStartIPAddress_Object = MibTableColumn
tcpipSecureStartIPAddress = _TcpipSecureStartIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 19, 1, 2),
    _TcpipSecureStartIPAddress_Type()
)
tcpipSecureStartIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSecureStartIPAddress.setStatus("optional")
_TcpipSecureEndIPAddress_Type = IpAddress
_TcpipSecureEndIPAddress_Object = MibTableColumn
tcpipSecureEndIPAddress = _TcpipSecureEndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 19, 1, 3),
    _TcpipSecureEndIPAddress_Type()
)
tcpipSecureEndIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSecureEndIPAddress.setStatus("optional")
_TcpipSecurePrinterMask_Type = Integer32
_TcpipSecurePrinterMask_Object = MibTableColumn
tcpipSecurePrinterMask = _TcpipSecurePrinterMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 19, 1, 4),
    _TcpipSecurePrinterMask_Type()
)
tcpipSecurePrinterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSecurePrinterMask.setStatus("optional")


class _TcpipSecureAdminEnabled_Type(Integer32):
    """Custom type tcpipSecureAdminEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipSecureAdminEnabled_Type.__name__ = "Integer32"
_TcpipSecureAdminEnabled_Object = MibTableColumn
tcpipSecureAdminEnabled = _TcpipSecureAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 19, 1, 5),
    _TcpipSecureAdminEnabled_Type()
)
tcpipSecureAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSecureAdminEnabled.setStatus("optional")


class _TcpipLowBandwidth_Type(Integer32):
    """Custom type tcpipLowBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TcpipLowBandwidth_Type.__name__ = "Integer32"
_TcpipLowBandwidth_Object = MibScalar
tcpipLowBandwidth = _TcpipLowBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 20),
    _TcpipLowBandwidth_Type()
)
tcpipLowBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipLowBandwidth.setStatus("optional")
_TcpipNumLogicalPrinters_Type = Integer32
_TcpipNumLogicalPrinters_Object = MibScalar
tcpipNumLogicalPrinters = _TcpipNumLogicalPrinters_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 21),
    _TcpipNumLogicalPrinters_Type()
)
tcpipNumLogicalPrinters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipNumLogicalPrinters.setStatus("mandatory")
_TcpipMLPTable_Object = MibTable
tcpipMLPTable = _TcpipMLPTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 22)
)
if mibBuilder.loadTexts:
    tcpipMLPTable.setStatus("mandatory")
_TcpipMLPEntry_Object = MibTableRow
tcpipMLPEntry = _TcpipMLPEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 22, 1)
)
tcpipMLPEntry.setIndexNames(
    (0, "ESI-MIB", "tcpipMLPIndex"),
)
if mibBuilder.loadTexts:
    tcpipMLPEntry.setStatus("mandatory")
_TcpipMLPIndex_Type = Integer32
_TcpipMLPIndex_Object = MibTableColumn
tcpipMLPIndex = _TcpipMLPIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 22, 1, 1),
    _TcpipMLPIndex_Type()
)
tcpipMLPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipMLPIndex.setStatus("optional")


class _TcpipMLPName_Type(DisplayString):
    """Custom type tcpipMLPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TcpipMLPName_Type.__name__ = "DisplayString"
_TcpipMLPName_Object = MibTableColumn
tcpipMLPName = _TcpipMLPName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 22, 1, 2),
    _TcpipMLPName_Type()
)
tcpipMLPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPName.setStatus("optional")
_TcpipMLPPort_Type = Integer32
_TcpipMLPPort_Object = MibTableColumn
tcpipMLPPort = _TcpipMLPPort_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 22, 1, 3),
    _TcpipMLPPort_Type()
)
tcpipMLPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPPort.setStatus("optional")
_TcpipMLPTCPPort_Type = Integer32
_TcpipMLPTCPPort_Object = MibTableColumn
tcpipMLPTCPPort = _TcpipMLPTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 22, 1, 4),
    _TcpipMLPTCPPort_Type()
)
tcpipMLPTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPTCPPort.setStatus("optional")


class _TcpipMLPPreString_Type(DisplayString):
    """Custom type tcpipMLPPreString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TcpipMLPPreString_Type.__name__ = "DisplayString"
_TcpipMLPPreString_Object = MibTableColumn
tcpipMLPPreString = _TcpipMLPPreString_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 22, 1, 5),
    _TcpipMLPPreString_Type()
)
tcpipMLPPreString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPPreString.setStatus("optional")


class _TcpipMLPPostString_Type(DisplayString):
    """Custom type tcpipMLPPostString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TcpipMLPPostString_Type.__name__ = "DisplayString"
_TcpipMLPPostString_Object = MibTableColumn
tcpipMLPPostString = _TcpipMLPPostString_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 22, 1, 6),
    _TcpipMLPPostString_Type()
)
tcpipMLPPostString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPPostString.setStatus("optional")
_TcpipMLPDeleteBytes_Type = Integer32
_TcpipMLPDeleteBytes_Object = MibTableColumn
tcpipMLPDeleteBytes = _TcpipMLPDeleteBytes_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 22, 1, 7),
    _TcpipMLPDeleteBytes_Type()
)
tcpipMLPDeleteBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipMLPDeleteBytes.setStatus("optional")
_TcpipSmtpServerAddr_Type = IpAddress
_TcpipSmtpServerAddr_Object = MibScalar
tcpipSmtpServerAddr = _TcpipSmtpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 23),
    _TcpipSmtpServerAddr_Type()
)
tcpipSmtpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSmtpServerAddr.setStatus("optional")
_TcpipNumSmtpDestinations_Type = Integer32
_TcpipNumSmtpDestinations_Object = MibScalar
tcpipNumSmtpDestinations = _TcpipNumSmtpDestinations_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 24),
    _TcpipNumSmtpDestinations_Type()
)
tcpipNumSmtpDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipNumSmtpDestinations.setStatus("mandatory")
_TcpipSmtpTable_Object = MibTable
tcpipSmtpTable = _TcpipSmtpTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 25)
)
if mibBuilder.loadTexts:
    tcpipSmtpTable.setStatus("mandatory")
_TcpipSmtpEntry_Object = MibTableRow
tcpipSmtpEntry = _TcpipSmtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 25, 1)
)
tcpipSmtpEntry.setIndexNames(
    (0, "ESI-MIB", "tcpipSmtpIndex"),
)
if mibBuilder.loadTexts:
    tcpipSmtpEntry.setStatus("mandatory")
_TcpipSmtpIndex_Type = Integer32
_TcpipSmtpIndex_Object = MibTableColumn
tcpipSmtpIndex = _TcpipSmtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 25, 1, 1),
    _TcpipSmtpIndex_Type()
)
tcpipSmtpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipSmtpIndex.setStatus("mandatory")


class _TcpipSmtpEmailAddr_Type(OctetString):
    """Custom type tcpipSmtpEmailAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipSmtpEmailAddr_Type.__name__ = "OctetString"
_TcpipSmtpEmailAddr_Object = MibTableColumn
tcpipSmtpEmailAddr = _TcpipSmtpEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 25, 1, 2),
    _TcpipSmtpEmailAddr_Type()
)
tcpipSmtpEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSmtpEmailAddr.setStatus("optional")
_TcpipSmtpProtocolMask_Type = Integer32
_TcpipSmtpProtocolMask_Object = MibTableColumn
tcpipSmtpProtocolMask = _TcpipSmtpProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 25, 1, 3),
    _TcpipSmtpProtocolMask_Type()
)
tcpipSmtpProtocolMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSmtpProtocolMask.setStatus("optional")
_TcpipSmtpPrinterMask_Type = Integer32
_TcpipSmtpPrinterMask_Object = MibTableColumn
tcpipSmtpPrinterMask = _TcpipSmtpPrinterMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 25, 1, 4),
    _TcpipSmtpPrinterMask_Type()
)
tcpipSmtpPrinterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSmtpPrinterMask.setStatus("optional")
_TcpipSmtpOutputMask_Type = Integer32
_TcpipSmtpOutputMask_Object = MibTableColumn
tcpipSmtpOutputMask = _TcpipSmtpOutputMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 25, 1, 5),
    _TcpipSmtpOutputMask_Type()
)
tcpipSmtpOutputMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipSmtpOutputMask.setStatus("optional")


class _TcpipWebAdminName_Type(OctetString):
    """Custom type tcpipWebAdminName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_TcpipWebAdminName_Type.__name__ = "OctetString"
_TcpipWebAdminName_Object = MibScalar
tcpipWebAdminName = _TcpipWebAdminName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 26),
    _TcpipWebAdminName_Type()
)
tcpipWebAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebAdminName.setStatus("optional")


class _TcpipWebAdminPassword_Type(OctetString):
    """Custom type tcpipWebAdminPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_TcpipWebAdminPassword_Type.__name__ = "OctetString"
_TcpipWebAdminPassword_Object = MibScalar
tcpipWebAdminPassword = _TcpipWebAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 27),
    _TcpipWebAdminPassword_Type()
)
tcpipWebAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebAdminPassword.setStatus("optional")


class _TcpipWebUserName_Type(OctetString):
    """Custom type tcpipWebUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_TcpipWebUserName_Type.__name__ = "OctetString"
_TcpipWebUserName_Object = MibScalar
tcpipWebUserName = _TcpipWebUserName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 28),
    _TcpipWebUserName_Type()
)
tcpipWebUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebUserName.setStatus("optional")


class _TcpipWebUserPassword_Type(OctetString):
    """Custom type tcpipWebUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_TcpipWebUserPassword_Type.__name__ = "OctetString"
_TcpipWebUserPassword_Object = MibScalar
tcpipWebUserPassword = _TcpipWebUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 29),
    _TcpipWebUserPassword_Type()
)
tcpipWebUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebUserPassword.setStatus("optional")
_TcpipWebHtttpPort_Type = Integer32
_TcpipWebHtttpPort_Object = MibScalar
tcpipWebHtttpPort = _TcpipWebHtttpPort_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 30),
    _TcpipWebHtttpPort_Type()
)
tcpipWebHtttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebHtttpPort.setStatus("optional")


class _TcpipWebFaqURL_Type(OctetString):
    """Custom type tcpipWebFaqURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipWebFaqURL_Type.__name__ = "OctetString"
_TcpipWebFaqURL_Object = MibScalar
tcpipWebFaqURL = _TcpipWebFaqURL_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 31),
    _TcpipWebFaqURL_Type()
)
tcpipWebFaqURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebFaqURL.setStatus("optional")


class _TcpipWebUpdateURL_Type(OctetString):
    """Custom type tcpipWebUpdateURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipWebUpdateURL_Type.__name__ = "OctetString"
_TcpipWebUpdateURL_Object = MibScalar
tcpipWebUpdateURL = _TcpipWebUpdateURL_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 32),
    _TcpipWebUpdateURL_Type()
)
tcpipWebUpdateURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebUpdateURL.setStatus("optional")


class _TcpipWebCustomLinkName_Type(OctetString):
    """Custom type tcpipWebCustomLinkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_TcpipWebCustomLinkName_Type.__name__ = "OctetString"
_TcpipWebCustomLinkName_Object = MibScalar
tcpipWebCustomLinkName = _TcpipWebCustomLinkName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 33),
    _TcpipWebCustomLinkName_Type()
)
tcpipWebCustomLinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebCustomLinkName.setStatus("optional")


class _TcpipWebCustomLinkURL_Type(OctetString):
    """Custom type tcpipWebCustomLinkURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipWebCustomLinkURL_Type.__name__ = "OctetString"
_TcpipWebCustomLinkURL_Object = MibScalar
tcpipWebCustomLinkURL = _TcpipWebCustomLinkURL_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 34),
    _TcpipWebCustomLinkURL_Type()
)
tcpipWebCustomLinkURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipWebCustomLinkURL.setStatus("optional")
_TcpipPOP3ServerAddress_Type = IpAddress
_TcpipPOP3ServerAddress_Object = MibScalar
tcpipPOP3ServerAddress = _TcpipPOP3ServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 35),
    _TcpipPOP3ServerAddress_Type()
)
tcpipPOP3ServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPOP3ServerAddress.setStatus("optional")
_TcpipPOP3PollInterval_Type = Integer32
_TcpipPOP3PollInterval_Object = MibScalar
tcpipPOP3PollInterval = _TcpipPOP3PollInterval_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 36),
    _TcpipPOP3PollInterval_Type()
)
tcpipPOP3PollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPOP3PollInterval.setStatus("mandatory")


class _TcpipPOP3UserName_Type(OctetString):
    """Custom type tcpipPOP3UserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipPOP3UserName_Type.__name__ = "OctetString"
_TcpipPOP3UserName_Object = MibScalar
tcpipPOP3UserName = _TcpipPOP3UserName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 37),
    _TcpipPOP3UserName_Type()
)
tcpipPOP3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPOP3UserName.setStatus("optional")


class _TcpipPOP3Password_Type(OctetString):
    """Custom type tcpipPOP3Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_TcpipPOP3Password_Type.__name__ = "OctetString"
_TcpipPOP3Password_Object = MibScalar
tcpipPOP3Password = _TcpipPOP3Password_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 38),
    _TcpipPOP3Password_Type()
)
tcpipPOP3Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipPOP3Password.setStatus("optional")


class _TcpipDomainName_Type(OctetString):
    """Custom type tcpipDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_TcpipDomainName_Type.__name__ = "OctetString"
_TcpipDomainName_Object = MibScalar
tcpipDomainName = _TcpipDomainName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 4, 39),
    _TcpipDomainName_Type()
)
tcpipDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpipDomainName.setStatus("optional")
_TcpipStatus_ObjectIdentity = ObjectIdentity
tcpipStatus = _TcpipStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 5)
)


class _TcpipError_Type(DisplayString):
    """Custom type tcpipError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TcpipError_Type.__name__ = "DisplayString"
_TcpipError_Object = MibScalar
tcpipError = _TcpipError_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 5, 1),
    _TcpipError_Type()
)
tcpipError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipError.setStatus("optional")
_TcpipDisplayMask_Type = Integer32
_TcpipDisplayMask_Object = MibScalar
tcpipDisplayMask = _TcpipDisplayMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 1, 6),
    _TcpipDisplayMask_Type()
)
tcpipDisplayMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpipDisplayMask.setStatus("mandatory")
_Netware_ObjectIdentity = ObjectIdentity
netware = _Netware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2)
)
_NwGroupVersion_Type = Integer32
_NwGroupVersion_Object = MibScalar
nwGroupVersion = _NwGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 1),
    _NwGroupVersion_Type()
)
nwGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwGroupVersion.setStatus("mandatory")


class _NwEnabled_Type(Integer32):
    """Custom type nwEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwEnabled_Type.__name__ = "Integer32"
_NwEnabled_Object = MibScalar
nwEnabled = _NwEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 2),
    _NwEnabled_Type()
)
nwEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwEnabled.setStatus("optional")
_NwCommands_ObjectIdentity = ObjectIdentity
nwCommands = _NwCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 3)
)


class _NwRestoreDefaults_Type(Integer32):
    """Custom type nwRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwRestoreDefaults_Type.__name__ = "Integer32"
_NwRestoreDefaults_Object = MibScalar
nwRestoreDefaults = _NwRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 3, 1),
    _NwRestoreDefaults_Type()
)
nwRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwRestoreDefaults.setStatus("optional")


class _NwFirmwareUpgrade_Type(Integer32):
    """Custom type nwFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwFirmwareUpgrade_Type.__name__ = "Integer32"
_NwFirmwareUpgrade_Object = MibScalar
nwFirmwareUpgrade = _NwFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 3, 2),
    _NwFirmwareUpgrade_Type()
)
nwFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwFirmwareUpgrade.setStatus("optional")
_NwConfigure_ObjectIdentity = ObjectIdentity
nwConfigure = _NwConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4)
)


class _NwFrameFormat_Type(Integer32):
    """Custom type nwFrameFormat based on Integer32"""
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
        *(("ethernet-802-2", 4),
          ("ethernet-802-3", 3),
          ("ethernet-II", 2),
          ("ethernet-Snap", 5),
          ("token-Ring", 6),
          ("token-Ring-Snap", 7),
          ("unknown", 1))
    )


_NwFrameFormat_Type.__name__ = "Integer32"
_NwFrameFormat_Object = MibScalar
nwFrameFormat = _NwFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 1),
    _NwFrameFormat_Type()
)
nwFrameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFrameFormat.setStatus("optional")


class _NwSetFrameFormat_Type(Integer32):
    """Custom type nwSetFrameFormat based on Integer32"""
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
        *(("auto-Sense", 1),
          ("forced-Ethernet-802-2", 4),
          ("forced-Ethernet-802-3", 3),
          ("forced-Ethernet-II", 2),
          ("forced-Ethernet-Snap", 5),
          ("forced-Token-Ring", 6),
          ("forced-Token-Ring-Snap", 7))
    )


_NwSetFrameFormat_Type.__name__ = "Integer32"
_NwSetFrameFormat_Object = MibScalar
nwSetFrameFormat = _NwSetFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 2),
    _NwSetFrameFormat_Type()
)
nwSetFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwSetFrameFormat.setStatus("optional")


class _NwMode_Type(Integer32):
    """Custom type nwMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pserver", 2),
          ("rprinter", 3),
          ("unknown", 1))
    )


_NwMode_Type.__name__ = "Integer32"
_NwMode_Object = MibScalar
nwMode = _NwMode_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 3),
    _NwMode_Type()
)
nwMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwMode.setStatus("optional")


class _NwPrintServerName_Type(DisplayString):
    """Custom type nwPrintServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwPrintServerName_Type.__name__ = "DisplayString"
_NwPrintServerName_Object = MibScalar
nwPrintServerName = _NwPrintServerName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 4),
    _NwPrintServerName_Type()
)
nwPrintServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPrintServerName.setStatus("optional")


class _NwPrintServerPassword_Type(DisplayString):
    """Custom type nwPrintServerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_NwPrintServerPassword_Type.__name__ = "DisplayString"
_NwPrintServerPassword_Object = MibScalar
nwPrintServerPassword = _NwPrintServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 5),
    _NwPrintServerPassword_Type()
)
nwPrintServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPrintServerPassword.setStatus("optional")


class _NwQueueScanTime_Type(Integer32):
    """Custom type nwQueueScanTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NwQueueScanTime_Type.__name__ = "Integer32"
_NwQueueScanTime_Object = MibScalar
nwQueueScanTime = _NwQueueScanTime_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 6),
    _NwQueueScanTime_Type()
)
nwQueueScanTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwQueueScanTime.setStatus("optional")


class _NwNetworkNumber_Type(OctetString):
    """Custom type nwNetworkNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NwNetworkNumber_Type.__name__ = "OctetString"
_NwNetworkNumber_Object = MibScalar
nwNetworkNumber = _NwNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 7),
    _NwNetworkNumber_Type()
)
nwNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNetworkNumber.setStatus("optional")
_NwMaxFileServers_Type = Integer32
_NwMaxFileServers_Object = MibScalar
nwMaxFileServers = _NwMaxFileServers_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 8),
    _NwMaxFileServers_Type()
)
nwMaxFileServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwMaxFileServers.setStatus("optional")
_NwFileServerTable_Object = MibTable
nwFileServerTable = _NwFileServerTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 9)
)
if mibBuilder.loadTexts:
    nwFileServerTable.setStatus("optional")
_NwFileServerEntry_Object = MibTableRow
nwFileServerEntry = _NwFileServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 9, 1)
)
nwFileServerEntry.setIndexNames(
    (0, "ESI-MIB", "nwFileServerIndex"),
)
if mibBuilder.loadTexts:
    nwFileServerEntry.setStatus("optional")
_NwFileServerIndex_Type = Integer32
_NwFileServerIndex_Object = MibTableColumn
nwFileServerIndex = _NwFileServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 9, 1, 1),
    _NwFileServerIndex_Type()
)
nwFileServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFileServerIndex.setStatus("optional")


class _NwFileServerName_Type(DisplayString):
    """Custom type nwFileServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwFileServerName_Type.__name__ = "DisplayString"
_NwFileServerName_Object = MibTableColumn
nwFileServerName = _NwFileServerName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 9, 1, 2),
    _NwFileServerName_Type()
)
nwFileServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwFileServerName.setStatus("optional")


class _NwFileServerConnectionStatus_Type(Integer32):
    """Custom type nwFileServerConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              258,
              261,
              276,
              512,
              515,
              768,
              769,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("bad-CONNECTION", 768),
          ("bad-SERVICE-CONNECTION", 769),
          ("down", 2),
          ("other", 32767),
          ("pse-CANT-LOGIN", 276),
          ("pse-NO-RESPONSE", 261),
          ("pse-NO-SUCH-QUEUE", 512),
          ("pse-UNABLE-TO-ATTACH-TO-QUEUE", 515),
          ("pse-UNKNOWN-FILE-SERVER", 258),
          ("serverNeverAttached", 5),
          ("serverReattaching", 4),
          ("startupInProgress", 3),
          ("up", 1))
    )


_NwFileServerConnectionStatus_Type.__name__ = "Integer32"
_NwFileServerConnectionStatus_Object = MibTableColumn
nwFileServerConnectionStatus = _NwFileServerConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 9, 1, 3),
    _NwFileServerConnectionStatus_Type()
)
nwFileServerConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwFileServerConnectionStatus.setStatus("optional")
_NwPortTable_Object = MibTable
nwPortTable = _NwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10)
)
if mibBuilder.loadTexts:
    nwPortTable.setStatus("optional")
_NwPortEntry_Object = MibTableRow
nwPortEntry = _NwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10, 1)
)
nwPortEntry.setIndexNames(
    (0, "ESI-MIB", "nwPortIndex"),
)
if mibBuilder.loadTexts:
    nwPortEntry.setStatus("optional")
_NwPortIndex_Type = Integer32
_NwPortIndex_Object = MibTableColumn
nwPortIndex = _NwPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10, 1, 1),
    _NwPortIndex_Type()
)
nwPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwPortIndex.setStatus("optional")


class _NwPortStatus_Type(DisplayString):
    """Custom type nwPortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NwPortStatus_Type.__name__ = "DisplayString"
_NwPortStatus_Object = MibTableColumn
nwPortStatus = _NwPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10, 1, 2),
    _NwPortStatus_Type()
)
nwPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwPortStatus.setStatus("optional")


class _NwPortPrinterNumber_Type(Integer32):
    """Custom type nwPortPrinterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwPortPrinterNumber_Type.__name__ = "Integer32"
_NwPortPrinterNumber_Object = MibTableColumn
nwPortPrinterNumber = _NwPortPrinterNumber_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10, 1, 3),
    _NwPortPrinterNumber_Type()
)
nwPortPrinterNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortPrinterNumber.setStatus("optional")


class _NwPortFontDownload_Type(Integer32):
    """Custom type nwPortFontDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled-No-Power-Sense", 2),
          ("enabled-Power-Sense", 3))
    )


_NwPortFontDownload_Type.__name__ = "Integer32"
_NwPortFontDownload_Object = MibTableColumn
nwPortFontDownload = _NwPortFontDownload_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10, 1, 4),
    _NwPortFontDownload_Type()
)
nwPortFontDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortFontDownload.setStatus("optional")


class _NwPortPCLQueue_Type(DisplayString):
    """Custom type nwPortPCLQueue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwPortPCLQueue_Type.__name__ = "DisplayString"
_NwPortPCLQueue_Object = MibTableColumn
nwPortPCLQueue = _NwPortPCLQueue_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10, 1, 5),
    _NwPortPCLQueue_Type()
)
nwPortPCLQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortPCLQueue.setStatus("optional")


class _NwPortPSQueue_Type(DisplayString):
    """Custom type nwPortPSQueue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwPortPSQueue_Type.__name__ = "DisplayString"
_NwPortPSQueue_Object = MibTableColumn
nwPortPSQueue = _NwPortPSQueue_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10, 1, 6),
    _NwPortPSQueue_Type()
)
nwPortPSQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortPSQueue.setStatus("optional")


class _NwPortFormsOn_Type(Integer32):
    """Custom type nwPortFormsOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwPortFormsOn_Type.__name__ = "Integer32"
_NwPortFormsOn_Object = MibTableColumn
nwPortFormsOn = _NwPortFormsOn_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10, 1, 7),
    _NwPortFormsOn_Type()
)
nwPortFormsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortFormsOn.setStatus("optional")


class _NwPortFormNumber_Type(Integer32):
    """Custom type nwPortFormNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NwPortFormNumber_Type.__name__ = "Integer32"
_NwPortFormNumber_Object = MibTableColumn
nwPortFormNumber = _NwPortFormNumber_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10, 1, 8),
    _NwPortFormNumber_Type()
)
nwPortFormNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortFormNumber.setStatus("optional")


class _NwPortNotification_Type(Integer32):
    """Custom type nwPortNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwPortNotification_Type.__name__ = "Integer32"
_NwPortNotification_Object = MibTableColumn
nwPortNotification = _NwPortNotification_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 10, 1, 9),
    _NwPortNotification_Type()
)
nwPortNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPortNotification.setStatus("optional")
_NwNumTraps_Type = Integer32
_NwNumTraps_Object = MibScalar
nwNumTraps = _NwNumTraps_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 11),
    _NwNumTraps_Type()
)
nwNumTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwNumTraps.setStatus("mandatory")
_NwTrapTable_Object = MibTable
nwTrapTable = _NwTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 12)
)
if mibBuilder.loadTexts:
    nwTrapTable.setStatus("mandatory")
_NwTrapEntry_Object = MibTableRow
nwTrapEntry = _NwTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 12, 1)
)
nwTrapEntry.setIndexNames(
    (0, "ESI-MIB", "nwTrapIndex"),
)
if mibBuilder.loadTexts:
    nwTrapEntry.setStatus("mandatory")
_NwTrapIndex_Type = Integer32
_NwTrapIndex_Object = MibTableColumn
nwTrapIndex = _NwTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 12, 1, 1),
    _NwTrapIndex_Type()
)
nwTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwTrapIndex.setStatus("mandatory")


class _NwTrapDestination_Type(OctetString):
    """Custom type nwTrapDestination based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NwTrapDestination_Type.__name__ = "OctetString"
_NwTrapDestination_Object = MibTableColumn
nwTrapDestination = _NwTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 12, 1, 2),
    _NwTrapDestination_Type()
)
nwTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwTrapDestination.setStatus("optional")


class _NwTrapDestinationNet_Type(OctetString):
    """Custom type nwTrapDestinationNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NwTrapDestinationNet_Type.__name__ = "OctetString"
_NwTrapDestinationNet_Object = MibTableColumn
nwTrapDestinationNet = _NwTrapDestinationNet_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 12, 1, 3),
    _NwTrapDestinationNet_Type()
)
nwTrapDestinationNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwTrapDestinationNet.setStatus("mandatory")
_NwProtocolTrapMask_Type = Integer32
_NwProtocolTrapMask_Object = MibTableColumn
nwProtocolTrapMask = _NwProtocolTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 12, 1, 4),
    _NwProtocolTrapMask_Type()
)
nwProtocolTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwProtocolTrapMask.setStatus("optional")
_NwPrinterTrapMask_Type = Integer32
_NwPrinterTrapMask_Object = MibTableColumn
nwPrinterTrapMask = _NwPrinterTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 12, 1, 5),
    _NwPrinterTrapMask_Type()
)
nwPrinterTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwPrinterTrapMask.setStatus("optional")
_NwOutputTrapMask_Type = Integer32
_NwOutputTrapMask_Object = MibTableColumn
nwOutputTrapMask = _NwOutputTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 12, 1, 6),
    _NwOutputTrapMask_Type()
)
nwOutputTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwOutputTrapMask.setStatus("optional")


class _NwNDSPrintServerName_Type(DisplayString):
    """Custom type nwNDSPrintServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_NwNDSPrintServerName_Type.__name__ = "DisplayString"
_NwNDSPrintServerName_Object = MibScalar
nwNDSPrintServerName = _NwNDSPrintServerName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 13),
    _NwNDSPrintServerName_Type()
)
nwNDSPrintServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPrintServerName.setStatus("optional")


class _NwNDSPreferredDSTree_Type(DisplayString):
    """Custom type nwNDSPreferredDSTree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwNDSPreferredDSTree_Type.__name__ = "DisplayString"
_NwNDSPreferredDSTree_Object = MibScalar
nwNDSPreferredDSTree = _NwNDSPreferredDSTree_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 14),
    _NwNDSPreferredDSTree_Type()
)
nwNDSPreferredDSTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPreferredDSTree.setStatus("optional")


class _NwNDSPreferredDSFileServer_Type(DisplayString):
    """Custom type nwNDSPreferredDSFileServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_NwNDSPreferredDSFileServer_Type.__name__ = "DisplayString"
_NwNDSPreferredDSFileServer_Object = MibScalar
nwNDSPreferredDSFileServer = _NwNDSPreferredDSFileServer_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 15),
    _NwNDSPreferredDSFileServer_Type()
)
nwNDSPreferredDSFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPreferredDSFileServer.setStatus("optional")
_NwNDSPacketCheckSumEnabled_Type = Integer32
_NwNDSPacketCheckSumEnabled_Object = MibScalar
nwNDSPacketCheckSumEnabled = _NwNDSPacketCheckSumEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 16),
    _NwNDSPacketCheckSumEnabled_Type()
)
nwNDSPacketCheckSumEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPacketCheckSumEnabled.setStatus("optional")
_NwNDSPacketSignatureLevel_Type = Integer32
_NwNDSPacketSignatureLevel_Object = MibScalar
nwNDSPacketSignatureLevel = _NwNDSPacketSignatureLevel_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 17),
    _NwNDSPacketSignatureLevel_Type()
)
nwNDSPacketSignatureLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwNDSPacketSignatureLevel.setStatus("optional")
_NwAvailablePrintModes_Type = Integer32
_NwAvailablePrintModes_Object = MibScalar
nwAvailablePrintModes = _NwAvailablePrintModes_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 18),
    _NwAvailablePrintModes_Type()
)
nwAvailablePrintModes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwAvailablePrintModes.setStatus("optional")


class _NwDirectPrintEnabled_Type(Integer32):
    """Custom type nwDirectPrintEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwDirectPrintEnabled_Type.__name__ = "Integer32"
_NwDirectPrintEnabled_Object = MibScalar
nwDirectPrintEnabled = _NwDirectPrintEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 19),
    _NwDirectPrintEnabled_Type()
)
nwDirectPrintEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDirectPrintEnabled.setStatus("optional")


class _NwJAConfig_Type(Integer32):
    """Custom type nwJAConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwJAConfig_Type.__name__ = "Integer32"
_NwJAConfig_Object = MibScalar
nwJAConfig = _NwJAConfig_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 20),
    _NwJAConfig_Type()
)
nwJAConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwJAConfig.setStatus("optional")


class _NwDisableSAP_Type(Integer32):
    """Custom type nwDisableSAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NwDisableSAP_Type.__name__ = "Integer32"
_NwDisableSAP_Object = MibScalar
nwDisableSAP = _NwDisableSAP_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 4, 21),
    _NwDisableSAP_Type()
)
nwDisableSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwDisableSAP.setStatus("optional")
_NwStatus_ObjectIdentity = ObjectIdentity
nwStatus = _NwStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 5)
)


class _NwError_Type(DisplayString):
    """Custom type nwError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_NwError_Type.__name__ = "DisplayString"
_NwError_Object = MibScalar
nwError = _NwError_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 5, 1),
    _NwError_Type()
)
nwError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwError.setStatus("optional")
_NwDisplayMask_Type = Integer32
_NwDisplayMask_Object = MibScalar
nwDisplayMask = _NwDisplayMask_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 2, 6),
    _NwDisplayMask_Type()
)
nwDisplayMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwDisplayMask.setStatus("mandatory")
_Vines_ObjectIdentity = ObjectIdentity
vines = _Vines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3)
)
_BvGroupVersion_Type = Integer32
_BvGroupVersion_Object = MibScalar
bvGroupVersion = _BvGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 1),
    _BvGroupVersion_Type()
)
bvGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvGroupVersion.setStatus("mandatory")


class _BvEnabled_Type(Integer32):
    """Custom type bvEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BvEnabled_Type.__name__ = "Integer32"
_BvEnabled_Object = MibScalar
bvEnabled = _BvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 2),
    _BvEnabled_Type()
)
bvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvEnabled.setStatus("optional")
_BvCommands_ObjectIdentity = ObjectIdentity
bvCommands = _BvCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 3)
)


class _BvRestoreDefaults_Type(Integer32):
    """Custom type bvRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BvRestoreDefaults_Type.__name__ = "Integer32"
_BvRestoreDefaults_Object = MibScalar
bvRestoreDefaults = _BvRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 3, 1),
    _BvRestoreDefaults_Type()
)
bvRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvRestoreDefaults.setStatus("optional")


class _BvFirmwareUpgrade_Type(Integer32):
    """Custom type bvFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BvFirmwareUpgrade_Type.__name__ = "Integer32"
_BvFirmwareUpgrade_Object = MibScalar
bvFirmwareUpgrade = _BvFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 3, 2),
    _BvFirmwareUpgrade_Type()
)
bvFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvFirmwareUpgrade.setStatus("optional")


class _BvSetSequenceRouting_Type(Integer32):
    """Custom type bvSetSequenceRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic-Routing", 1),
          ("force-Non-Sequenced-Routing", 3),
          ("force-Sequenced-Routing", 2))
    )


_BvSetSequenceRouting_Type.__name__ = "Integer32"
_BvSetSequenceRouting_Object = MibScalar
bvSetSequenceRouting = _BvSetSequenceRouting_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 3, 3),
    _BvSetSequenceRouting_Type()
)
bvSetSequenceRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvSetSequenceRouting.setStatus("optional")


class _BvDisableVPMan_Type(Integer32):
    """Custom type bvDisableVPMan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BvDisableVPMan_Type.__name__ = "Integer32"
_BvDisableVPMan_Object = MibScalar
bvDisableVPMan = _BvDisableVPMan_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 3, 4),
    _BvDisableVPMan_Type()
)
bvDisableVPMan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvDisableVPMan.setStatus("optional")
_BvConfigure_ObjectIdentity = ObjectIdentity
bvConfigure = _BvConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 4)
)


class _BvLoginName_Type(DisplayString):
    """Custom type bvLoginName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 63),
    )


_BvLoginName_Type.__name__ = "DisplayString"
_BvLoginName_Object = MibScalar
bvLoginName = _BvLoginName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 4, 1),
    _BvLoginName_Type()
)
bvLoginName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvLoginName.setStatus("optional")


class _BvLoginPassword_Type(DisplayString):
    """Custom type bvLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BvLoginPassword_Type.__name__ = "DisplayString"
_BvLoginPassword_Object = MibScalar
bvLoginPassword = _BvLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 4, 2),
    _BvLoginPassword_Type()
)
bvLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvLoginPassword.setStatus("optional")
_BvNumberPrintServices_Type = Integer32
_BvNumberPrintServices_Object = MibScalar
bvNumberPrintServices = _BvNumberPrintServices_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 4, 3),
    _BvNumberPrintServices_Type()
)
bvNumberPrintServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvNumberPrintServices.setStatus("optional")
_BvPrintServiceTable_Object = MibTable
bvPrintServiceTable = _BvPrintServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 4, 4)
)
if mibBuilder.loadTexts:
    bvPrintServiceTable.setStatus("optional")
_BvPrintServiceEntry_Object = MibTableRow
bvPrintServiceEntry = _BvPrintServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 4, 4, 1)
)
bvPrintServiceEntry.setIndexNames(
    (0, "ESI-MIB", "bvPrintServiceIndex"),
)
if mibBuilder.loadTexts:
    bvPrintServiceEntry.setStatus("optional")
_BvPrintServiceIndex_Type = Integer32
_BvPrintServiceIndex_Object = MibTableColumn
bvPrintServiceIndex = _BvPrintServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 4, 4, 1, 1),
    _BvPrintServiceIndex_Type()
)
bvPrintServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPrintServiceIndex.setStatus("optional")


class _BvPrintServiceName_Type(DisplayString):
    """Custom type bvPrintServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BvPrintServiceName_Type.__name__ = "DisplayString"
_BvPrintServiceName_Object = MibTableColumn
bvPrintServiceName = _BvPrintServiceName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 4, 4, 1, 2),
    _BvPrintServiceName_Type()
)
bvPrintServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvPrintServiceName.setStatus("optional")
_BvPrintServiceRouting_Type = Integer32
_BvPrintServiceRouting_Object = MibTableColumn
bvPrintServiceRouting = _BvPrintServiceRouting_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 4, 4, 1, 3),
    _BvPrintServiceRouting_Type()
)
bvPrintServiceRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvPrintServiceRouting.setStatus("optional")


class _BvPnicDescription_Type(DisplayString):
    """Custom type bvPnicDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BvPnicDescription_Type.__name__ = "DisplayString"
_BvPnicDescription_Object = MibScalar
bvPnicDescription = _BvPnicDescription_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 4, 5),
    _BvPnicDescription_Type()
)
bvPnicDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bvPnicDescription.setStatus("optional")
_BvStatus_ObjectIdentity = ObjectIdentity
bvStatus = _BvStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5)
)


class _BvError_Type(DisplayString):
    """Custom type bvError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_BvError_Type.__name__ = "DisplayString"
_BvError_Object = MibScalar
bvError = _BvError_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 1),
    _BvError_Type()
)
bvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvError.setStatus("optional")


class _BvRouting_Type(Integer32):
    """Custom type bvRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              32766,
              32767)
        )
    )
    namedValues = NamedValues(
        *(("non-Sequenced-Routing", 2),
          ("protocol-Disabled", 32767),
          ("sequenced-Routing", 1),
          ("unknown-Routing", 32766))
    )


_BvRouting_Type.__name__ = "Integer32"
_BvRouting_Object = MibScalar
bvRouting = _BvRouting_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 2),
    _BvRouting_Type()
)
bvRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvRouting.setStatus("optional")
_BvNumPrintServices_Type = Integer32
_BvNumPrintServices_Object = MibScalar
bvNumPrintServices = _BvNumPrintServices_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 3),
    _BvNumPrintServices_Type()
)
bvNumPrintServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvNumPrintServices.setStatus("optional")
_BvPrintServiceStatusTable_Object = MibTable
bvPrintServiceStatusTable = _BvPrintServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4)
)
if mibBuilder.loadTexts:
    bvPrintServiceStatusTable.setStatus("optional")
_BvPrintServiceStatusEntry_Object = MibTableRow
bvPrintServiceStatusEntry = _BvPrintServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1)
)
bvPrintServiceStatusEntry.setIndexNames(
    (0, "ESI-MIB", "bvPSStatusIndex"),
)
if mibBuilder.loadTexts:
    bvPrintServiceStatusEntry.setStatus("optional")
_BvPSStatusIndex_Type = Integer32
_BvPSStatusIndex_Object = MibTableColumn
bvPSStatusIndex = _BvPSStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1, 1),
    _BvPSStatusIndex_Type()
)
bvPSStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPSStatusIndex.setStatus("optional")


class _BvPSName_Type(DisplayString):
    """Custom type bvPSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_BvPSName_Type.__name__ = "DisplayString"
_BvPSName_Object = MibTableColumn
bvPSName = _BvPSName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1, 2),
    _BvPSName_Type()
)
bvPSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPSName.setStatus("optional")


class _BvPSStatus_Type(DisplayString):
    """Custom type bvPSStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_BvPSStatus_Type.__name__ = "DisplayString"
_BvPSStatus_Object = MibTableColumn
bvPSStatus = _BvPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1, 3),
    _BvPSStatus_Type()
)
bvPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPSStatus.setStatus("optional")
_BvPSDestination_Type = Integer32
_BvPSDestination_Object = MibTableColumn
bvPSDestination = _BvPSDestination_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1, 4),
    _BvPSDestination_Type()
)
bvPSDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPSDestination.setStatus("optional")


class _BvPrinterStatus_Type(DisplayString):
    """Custom type bvPrinterStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BvPrinterStatus_Type.__name__ = "DisplayString"
_BvPrinterStatus_Object = MibTableColumn
bvPrinterStatus = _BvPrinterStatus_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1, 5),
    _BvPrinterStatus_Type()
)
bvPrinterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvPrinterStatus.setStatus("optional")


class _BvJobActive_Type(Integer32):
    """Custom type bvJobActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BvJobActive_Type.__name__ = "Integer32"
_BvJobActive_Object = MibTableColumn
bvJobActive = _BvJobActive_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1, 6),
    _BvJobActive_Type()
)
bvJobActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvJobActive.setStatus("optional")


class _BvJobSource_Type(DisplayString):
    """Custom type bvJobSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BvJobSource_Type.__name__ = "DisplayString"
_BvJobSource_Object = MibTableColumn
bvJobSource = _BvJobSource_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1, 7),
    _BvJobSource_Type()
)
bvJobSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvJobSource.setStatus("optional")


class _BvJobTitle_Type(DisplayString):
    """Custom type bvJobTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BvJobTitle_Type.__name__ = "DisplayString"
_BvJobTitle_Object = MibTableColumn
bvJobTitle = _BvJobTitle_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1, 8),
    _BvJobTitle_Type()
)
bvJobTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvJobTitle.setStatus("optional")


class _BvJobSize_Type(DisplayString):
    """Custom type bvJobSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_BvJobSize_Type.__name__ = "DisplayString"
_BvJobSize_Object = MibTableColumn
bvJobSize = _BvJobSize_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1, 9),
    _BvJobSize_Type()
)
bvJobSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvJobSize.setStatus("optional")


class _BvJobNumber_Type(DisplayString):
    """Custom type bvJobNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BvJobNumber_Type.__name__ = "DisplayString"
_BvJobNumber_Object = MibTableColumn
bvJobNumber = _BvJobNumber_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 3, 5, 4, 1, 10),
    _BvJobNumber_Type()
)
bvJobNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bvJobNumber.setStatus("optional")
_LanManager_ObjectIdentity = ObjectIdentity
lanManager = _LanManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 4)
)
_LmGroupVersion_Type = Integer32
_LmGroupVersion_Object = MibScalar
lmGroupVersion = _LmGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 4, 1),
    _LmGroupVersion_Type()
)
lmGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmGroupVersion.setStatus("mandatory")


class _LmEnabled_Type(Integer32):
    """Custom type lmEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LmEnabled_Type.__name__ = "Integer32"
_LmEnabled_Object = MibScalar
lmEnabled = _LmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 4, 2),
    _LmEnabled_Type()
)
lmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmEnabled.setStatus("optional")
_ETalk_ObjectIdentity = ObjectIdentity
eTalk = _ETalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5)
)
_ETalkGroupVersion_Type = Integer32
_ETalkGroupVersion_Object = MibScalar
eTalkGroupVersion = _ETalkGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 1),
    _ETalkGroupVersion_Type()
)
eTalkGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkGroupVersion.setStatus("mandatory")


class _ETalkEnabled_Type(Integer32):
    """Custom type eTalkEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ETalkEnabled_Type.__name__ = "Integer32"
_ETalkEnabled_Object = MibScalar
eTalkEnabled = _ETalkEnabled_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 2),
    _ETalkEnabled_Type()
)
eTalkEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkEnabled.setStatus("optional")
_ETalkCommands_ObjectIdentity = ObjectIdentity
eTalkCommands = _ETalkCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 3)
)


class _ETalkRestoreDefaults_Type(Integer32):
    """Custom type eTalkRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ETalkRestoreDefaults_Type.__name__ = "Integer32"
_ETalkRestoreDefaults_Object = MibScalar
eTalkRestoreDefaults = _ETalkRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 3, 1),
    _ETalkRestoreDefaults_Type()
)
eTalkRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkRestoreDefaults.setStatus("optional")
_ETalkConfigure_ObjectIdentity = ObjectIdentity
eTalkConfigure = _ETalkConfigure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4)
)


class _ETalkNetwork_Type(OctetString):
    """Custom type eTalkNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ETalkNetwork_Type.__name__ = "OctetString"
_ETalkNetwork_Object = MibScalar
eTalkNetwork = _ETalkNetwork_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 1),
    _ETalkNetwork_Type()
)
eTalkNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkNetwork.setStatus("optional")


class _ETalkNode_Type(OctetString):
    """Custom type eTalkNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ETalkNode_Type.__name__ = "OctetString"
_ETalkNode_Object = MibScalar
eTalkNode = _ETalkNode_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 2),
    _ETalkNode_Type()
)
eTalkNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkNode.setStatus("optional")
_ETalkNumPorts_Type = Integer32
_ETalkNumPorts_Object = MibScalar
eTalkNumPorts = _ETalkNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 3),
    _ETalkNumPorts_Type()
)
eTalkNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkNumPorts.setStatus("optional")
_ETalkPortTable_Object = MibTable
eTalkPortTable = _ETalkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 4)
)
if mibBuilder.loadTexts:
    eTalkPortTable.setStatus("optional")
_ETalkPortEntry_Object = MibTableRow
eTalkPortEntry = _ETalkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 4, 1)
)
eTalkPortEntry.setIndexNames(
    (0, "ESI-MIB", "eTalkPortIndex"),
)
if mibBuilder.loadTexts:
    eTalkPortEntry.setStatus("optional")
_ETalkPortIndex_Type = Integer32
_ETalkPortIndex_Object = MibTableColumn
eTalkPortIndex = _ETalkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 4, 1, 1),
    _ETalkPortIndex_Type()
)
eTalkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkPortIndex.setStatus("optional")


class _ETalkPortEnable_Type(Integer32):
    """Custom type eTalkPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ETalkPortEnable_Type.__name__ = "Integer32"
_ETalkPortEnable_Object = MibTableColumn
eTalkPortEnable = _ETalkPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 4, 1, 2),
    _ETalkPortEnable_Type()
)
eTalkPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkPortEnable.setStatus("optional")


class _ETalkName_Type(DisplayString):
    """Custom type eTalkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ETalkName_Type.__name__ = "DisplayString"
_ETalkName_Object = MibTableColumn
eTalkName = _ETalkName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 4, 1, 3),
    _ETalkName_Type()
)
eTalkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkName.setStatus("optional")


class _ETalkActiveName_Type(DisplayString):
    """Custom type eTalkActiveName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ETalkActiveName_Type.__name__ = "DisplayString"
_ETalkActiveName_Object = MibTableColumn
eTalkActiveName = _ETalkActiveName_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 4, 1, 4),
    _ETalkActiveName_Type()
)
eTalkActiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkActiveName.setStatus("optional")


class _ETalkType1_Type(DisplayString):
    """Custom type eTalkType1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ETalkType1_Type.__name__ = "DisplayString"
_ETalkType1_Object = MibTableColumn
eTalkType1 = _ETalkType1_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 4, 1, 5),
    _ETalkType1_Type()
)
eTalkType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkType1.setStatus("optional")


class _ETalkType2_Type(DisplayString):
    """Custom type eTalkType2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ETalkType2_Type.__name__ = "DisplayString"
_ETalkType2_Object = MibTableColumn
eTalkType2 = _ETalkType2_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 4, 1, 6),
    _ETalkType2_Type()
)
eTalkType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkType2.setStatus("optional")


class _ETalkZone_Type(DisplayString):
    """Custom type eTalkZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ETalkZone_Type.__name__ = "DisplayString"
_ETalkZone_Object = MibTableColumn
eTalkZone = _ETalkZone_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 4, 1, 7),
    _ETalkZone_Type()
)
eTalkZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eTalkZone.setStatus("optional")


class _ETalkActiveZone_Type(DisplayString):
    """Custom type eTalkActiveZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ETalkActiveZone_Type.__name__ = "DisplayString"
_ETalkActiveZone_Object = MibTableColumn
eTalkActiveZone = _ETalkActiveZone_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 4, 4, 1, 8),
    _ETalkActiveZone_Type()
)
eTalkActiveZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkActiveZone.setStatus("optional")
_ETalkStatus_ObjectIdentity = ObjectIdentity
eTalkStatus = _ETalkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 5)
)


class _ETalkError_Type(DisplayString):
    """Custom type eTalkError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ETalkError_Type.__name__ = "DisplayString"
_ETalkError_Object = MibScalar
eTalkError = _ETalkError_Object(
    (1, 3, 6, 1, 4, 1, 683, 6, 3, 5, 5, 1),
    _ETalkError_Type()
)
eTalkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTalkError.setStatus("optional")

# Managed Objects groups


# Notification objects

trapPrinterOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 683, 6, 0, 1)
)
trapPrinterOnline.setObjects(
    ("ESI-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterOnline.setStatus(
        ""
    )

trapPrinterOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 683, 6, 0, 2)
)
trapPrinterOffline.setObjects(
    ("ESI-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterOffline.setStatus(
        ""
    )

trapNoPrinterAttached = NotificationType(
    (1, 3, 6, 1, 4, 1, 683, 6, 0, 3)
)
trapNoPrinterAttached.setObjects(
    ("ESI-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapNoPrinterAttached.setStatus(
        ""
    )

trapPrinterTonerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 683, 6, 0, 4)
)
trapPrinterTonerLow.setObjects(
    ("ESI-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterTonerLow.setStatus(
        ""
    )

trapPrinterPaperOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 683, 6, 0, 5)
)
trapPrinterPaperOut.setObjects(
    ("ESI-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterPaperOut.setStatus(
        ""
    )

trapPrinterPaperJam = NotificationType(
    (1, 3, 6, 1, 4, 1, 683, 6, 0, 6)
)
trapPrinterPaperJam.setObjects(
    ("ESI-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterPaperJam.setStatus(
        ""
    )

trapPrinterDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 683, 6, 0, 7)
)
trapPrinterDoorOpen.setObjects(
    ("ESI-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterDoorOpen.setStatus(
        ""
    )

trapPrinterError = NotificationType(
    (1, 3, 6, 1, 4, 1, 683, 6, 0, 16)
)
trapPrinterError.setObjects(
    ("ESI-MIB", "outputIndex")
)
if mibBuilder.loadTexts:
    trapPrinterError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESI-MIB",
    **{"esi": esi,
       "general": general,
       "genGroupVersion": genGroupVersion,
       "genMIBVersion": genMIBVersion,
       "genProductName": genProductName,
       "genProductNumber": genProductNumber,
       "genSerialNumber": genSerialNumber,
       "genHWAddress": genHWAddress,
       "genCableType": genCableType,
       "genDateCode": genDateCode,
       "genVersion": genVersion,
       "genConfigurationDirty": genConfigurationDirty,
       "genCompanyName": genCompanyName,
       "genCompanyLoc": genCompanyLoc,
       "genCompanyPhone": genCompanyPhone,
       "genCompanyTechSupport": genCompanyTechSupport,
       "genProtocols": genProtocols,
       "genNumProtocols": genNumProtocols,
       "genProtocolTable": genProtocolTable,
       "genProtocolEntry": genProtocolEntry,
       "genProtocolIndex": genProtocolIndex,
       "genProtocolDescr": genProtocolDescr,
       "genProtocolID": genProtocolID,
       "genSysUpTimeString": genSysUpTimeString,
       "commands": commands,
       "cmdGroupVersion": cmdGroupVersion,
       "cmdReset": cmdReset,
       "cmdPrintConfig": cmdPrintConfig,
       "cmdRestoreDefaults": cmdRestoreDefaults,
       "esiSNMP": esiSNMP,
       "snmpGroupVersion": snmpGroupVersion,
       "esiSNMPCommands": esiSNMPCommands,
       "snmpRestoreDefaults": snmpRestoreDefaults,
       "snmpGetCommunityName": snmpGetCommunityName,
       "snmpSetCommunityName": snmpSetCommunityName,
       "snmpTrapCommunityName": snmpTrapCommunityName,
       "driver": driver,
       "driverGroupVersion": driverGroupVersion,
       "driverRXPackets": driverRXPackets,
       "driverTXPackets": driverTXPackets,
       "driverRXPacketsUnavailable": driverRXPacketsUnavailable,
       "driverRXPacketErrors": driverRXPacketErrors,
       "driverTXPacketErrors": driverTXPacketErrors,
       "driverTXPacketRetries": driverTXPacketRetries,
       "driverChecksumErrors": driverChecksumErrors,
       "tokenRing": tokenRing,
       "trGroupVersion": trGroupVersion,
       "trCommands": trCommands,
       "trRestoreDefaults": trRestoreDefaults,
       "trConfigure": trConfigure,
       "trPriority": trPriority,
       "trEarlyTokenRelease": trEarlyTokenRelease,
       "trPacketSize": trPacketSize,
       "trRouting": trRouting,
       "trLocallyAdminAddr": trLocallyAdminAddr,
       "printServers": printServers,
       "trapPrinterOnline": trapPrinterOnline,
       "trapPrinterOffline": trapPrinterOffline,
       "trapNoPrinterAttached": trapNoPrinterAttached,
       "trapPrinterTonerLow": trapPrinterTonerLow,
       "trapPrinterPaperOut": trapPrinterPaperOut,
       "trapPrinterPaperJam": trapPrinterPaperJam,
       "trapPrinterDoorOpen": trapPrinterDoorOpen,
       "trapPrinterError": trapPrinterError,
       "psGeneral": psGeneral,
       "psGroupVersion": psGroupVersion,
       "psJetAdminEnabled": psJetAdminEnabled,
       "psVerifyConfiguration": psVerifyConfiguration,
       "psOutput": psOutput,
       "outputGroupVersion": outputGroupVersion,
       "outputCommands": outputCommands,
       "outputRestoreDefaults": outputRestoreDefaults,
       "outputCommandsTable": outputCommandsTable,
       "outputCommandsEntry": outputCommandsEntry,
       "outputCancelCurrentJob": outputCancelCurrentJob,
       "outputConfigure": outputConfigure,
       "outputNumPorts": outputNumPorts,
       "outputTable": outputTable,
       "outputEntry": outputEntry,
       "outputIndex": outputIndex,
       "outputName": outputName,
       "outputStatusString": outputStatusString,
       "outputStatus": outputStatus,
       "outputExtendedStatus": outputExtendedStatus,
       "outputPrinter": outputPrinter,
       "outputLanguageSwitching": outputLanguageSwitching,
       "outputConfigLanguage": outputConfigLanguage,
       "outputPCLString": outputPCLString,
       "outputPSString": outputPSString,
       "outputCascaded": outputCascaded,
       "outputSetting": outputSetting,
       "outputOwner": outputOwner,
       "outputBIDIStatusEnabled": outputBIDIStatusEnabled,
       "outputPrinterModel": outputPrinterModel,
       "outputPrinterDisplay": outputPrinterDisplay,
       "outputCapabilities": outputCapabilities,
       "outputHandshake": outputHandshake,
       "outputDataBits": outputDataBits,
       "outputStopBits": outputStopBits,
       "outputParity": outputParity,
       "outputBaudRate": outputBaudRate,
       "outputProtocolManager": outputProtocolManager,
       "outputDisplayMask": outputDisplayMask,
       "outputAvailableTrapsMask": outputAvailableTrapsMask,
       "outputJobLog": outputJobLog,
       "outputNumLogEntries": outputNumLogEntries,
       "outputJobLogTable": outputJobLogTable,
       "outputJobLogEntry": outputJobLogEntry,
       "outputJobLogInformation": outputJobLogInformation,
       "outputJobLogTime": outputJobLogTime,
       "outputTotalJobTable": outputTotalJobTable,
       "outputTotalJobEntry": outputTotalJobEntry,
       "outputTotalJobIndex": outputTotalJobIndex,
       "outputTotalJobsLogged": outputTotalJobsLogged,
       "psProtocols": psProtocols,
       "tcpip": tcpip,
       "tcpipGroupVersion": tcpipGroupVersion,
       "tcpipEnabled": tcpipEnabled,
       "tcpipCommands": tcpipCommands,
       "tcpipRestoreDefaults": tcpipRestoreDefaults,
       "tcpipFirmwareUpgrade": tcpipFirmwareUpgrade,
       "tcpipConfigure": tcpipConfigure,
       "tcpipIPAddress": tcpipIPAddress,
       "tcpipDefaultGateway": tcpipDefaultGateway,
       "tcpipSubnetMask": tcpipSubnetMask,
       "tcpipUsingNetProtocols": tcpipUsingNetProtocols,
       "tcpipBootProtocolsEnabled": tcpipBootProtocolsEnabled,
       "tcpipIPAddressSource": tcpipIPAddressSource,
       "tcpipIPAddressServerAddress": tcpipIPAddressServerAddress,
       "tcpipTimeoutChecking": tcpipTimeoutChecking,
       "tcpipNumTraps": tcpipNumTraps,
       "tcpipTrapTable": tcpipTrapTable,
       "tcpipTrapEntry": tcpipTrapEntry,
       "tcpipTrapIndex": tcpipTrapIndex,
       "tcpipTrapDestination": tcpipTrapDestination,
       "tcpipProtocolTrapMask": tcpipProtocolTrapMask,
       "tcpipPrinterTrapMask": tcpipPrinterTrapMask,
       "tcpipOutputTrapMask": tcpipOutputTrapMask,
       "tcpipBanners": tcpipBanners,
       "tcpipWinsAddress": tcpipWinsAddress,
       "tcpipWinsAddressSource": tcpipWinsAddressSource,
       "tcpipConfigPassword": tcpipConfigPassword,
       "tcpipTimeoutCheckingValue": tcpipTimeoutCheckingValue,
       "tcpipArpInterval": tcpipArpInterval,
       "tcpipRawPortNumber": tcpipRawPortNumber,
       "tcpipNumSecurity": tcpipNumSecurity,
       "tcpipSecurityTable": tcpipSecurityTable,
       "tcpipSecurityEntry": tcpipSecurityEntry,
       "tcpipSecurityIndex": tcpipSecurityIndex,
       "tcpipSecureStartIPAddress": tcpipSecureStartIPAddress,
       "tcpipSecureEndIPAddress": tcpipSecureEndIPAddress,
       "tcpipSecurePrinterMask": tcpipSecurePrinterMask,
       "tcpipSecureAdminEnabled": tcpipSecureAdminEnabled,
       "tcpipLowBandwidth": tcpipLowBandwidth,
       "tcpipNumLogicalPrinters": tcpipNumLogicalPrinters,
       "tcpipMLPTable": tcpipMLPTable,
       "tcpipMLPEntry": tcpipMLPEntry,
       "tcpipMLPIndex": tcpipMLPIndex,
       "tcpipMLPName": tcpipMLPName,
       "tcpipMLPPort": tcpipMLPPort,
       "tcpipMLPTCPPort": tcpipMLPTCPPort,
       "tcpipMLPPreString": tcpipMLPPreString,
       "tcpipMLPPostString": tcpipMLPPostString,
       "tcpipMLPDeleteBytes": tcpipMLPDeleteBytes,
       "tcpipSmtpServerAddr": tcpipSmtpServerAddr,
       "tcpipNumSmtpDestinations": tcpipNumSmtpDestinations,
       "tcpipSmtpTable": tcpipSmtpTable,
       "tcpipSmtpEntry": tcpipSmtpEntry,
       "tcpipSmtpIndex": tcpipSmtpIndex,
       "tcpipSmtpEmailAddr": tcpipSmtpEmailAddr,
       "tcpipSmtpProtocolMask": tcpipSmtpProtocolMask,
       "tcpipSmtpPrinterMask": tcpipSmtpPrinterMask,
       "tcpipSmtpOutputMask": tcpipSmtpOutputMask,
       "tcpipWebAdminName": tcpipWebAdminName,
       "tcpipWebAdminPassword": tcpipWebAdminPassword,
       "tcpipWebUserName": tcpipWebUserName,
       "tcpipWebUserPassword": tcpipWebUserPassword,
       "tcpipWebHtttpPort": tcpipWebHtttpPort,
       "tcpipWebFaqURL": tcpipWebFaqURL,
       "tcpipWebUpdateURL": tcpipWebUpdateURL,
       "tcpipWebCustomLinkName": tcpipWebCustomLinkName,
       "tcpipWebCustomLinkURL": tcpipWebCustomLinkURL,
       "tcpipPOP3ServerAddress": tcpipPOP3ServerAddress,
       "tcpipPOP3PollInterval": tcpipPOP3PollInterval,
       "tcpipPOP3UserName": tcpipPOP3UserName,
       "tcpipPOP3Password": tcpipPOP3Password,
       "tcpipDomainName": tcpipDomainName,
       "tcpipStatus": tcpipStatus,
       "tcpipError": tcpipError,
       "tcpipDisplayMask": tcpipDisplayMask,
       "netware": netware,
       "nwGroupVersion": nwGroupVersion,
       "nwEnabled": nwEnabled,
       "nwCommands": nwCommands,
       "nwRestoreDefaults": nwRestoreDefaults,
       "nwFirmwareUpgrade": nwFirmwareUpgrade,
       "nwConfigure": nwConfigure,
       "nwFrameFormat": nwFrameFormat,
       "nwSetFrameFormat": nwSetFrameFormat,
       "nwMode": nwMode,
       "nwPrintServerName": nwPrintServerName,
       "nwPrintServerPassword": nwPrintServerPassword,
       "nwQueueScanTime": nwQueueScanTime,
       "nwNetworkNumber": nwNetworkNumber,
       "nwMaxFileServers": nwMaxFileServers,
       "nwFileServerTable": nwFileServerTable,
       "nwFileServerEntry": nwFileServerEntry,
       "nwFileServerIndex": nwFileServerIndex,
       "nwFileServerName": nwFileServerName,
       "nwFileServerConnectionStatus": nwFileServerConnectionStatus,
       "nwPortTable": nwPortTable,
       "nwPortEntry": nwPortEntry,
       "nwPortIndex": nwPortIndex,
       "nwPortStatus": nwPortStatus,
       "nwPortPrinterNumber": nwPortPrinterNumber,
       "nwPortFontDownload": nwPortFontDownload,
       "nwPortPCLQueue": nwPortPCLQueue,
       "nwPortPSQueue": nwPortPSQueue,
       "nwPortFormsOn": nwPortFormsOn,
       "nwPortFormNumber": nwPortFormNumber,
       "nwPortNotification": nwPortNotification,
       "nwNumTraps": nwNumTraps,
       "nwTrapTable": nwTrapTable,
       "nwTrapEntry": nwTrapEntry,
       "nwTrapIndex": nwTrapIndex,
       "nwTrapDestination": nwTrapDestination,
       "nwTrapDestinationNet": nwTrapDestinationNet,
       "nwProtocolTrapMask": nwProtocolTrapMask,
       "nwPrinterTrapMask": nwPrinterTrapMask,
       "nwOutputTrapMask": nwOutputTrapMask,
       "nwNDSPrintServerName": nwNDSPrintServerName,
       "nwNDSPreferredDSTree": nwNDSPreferredDSTree,
       "nwNDSPreferredDSFileServer": nwNDSPreferredDSFileServer,
       "nwNDSPacketCheckSumEnabled": nwNDSPacketCheckSumEnabled,
       "nwNDSPacketSignatureLevel": nwNDSPacketSignatureLevel,
       "nwAvailablePrintModes": nwAvailablePrintModes,
       "nwDirectPrintEnabled": nwDirectPrintEnabled,
       "nwJAConfig": nwJAConfig,
       "nwDisableSAP": nwDisableSAP,
       "nwStatus": nwStatus,
       "nwError": nwError,
       "nwDisplayMask": nwDisplayMask,
       "vines": vines,
       "bvGroupVersion": bvGroupVersion,
       "bvEnabled": bvEnabled,
       "bvCommands": bvCommands,
       "bvRestoreDefaults": bvRestoreDefaults,
       "bvFirmwareUpgrade": bvFirmwareUpgrade,
       "bvSetSequenceRouting": bvSetSequenceRouting,
       "bvDisableVPMan": bvDisableVPMan,
       "bvConfigure": bvConfigure,
       "bvLoginName": bvLoginName,
       "bvLoginPassword": bvLoginPassword,
       "bvNumberPrintServices": bvNumberPrintServices,
       "bvPrintServiceTable": bvPrintServiceTable,
       "bvPrintServiceEntry": bvPrintServiceEntry,
       "bvPrintServiceIndex": bvPrintServiceIndex,
       "bvPrintServiceName": bvPrintServiceName,
       "bvPrintServiceRouting": bvPrintServiceRouting,
       "bvPnicDescription": bvPnicDescription,
       "bvStatus": bvStatus,
       "bvError": bvError,
       "bvRouting": bvRouting,
       "bvNumPrintServices": bvNumPrintServices,
       "bvPrintServiceStatusTable": bvPrintServiceStatusTable,
       "bvPrintServiceStatusEntry": bvPrintServiceStatusEntry,
       "bvPSStatusIndex": bvPSStatusIndex,
       "bvPSName": bvPSName,
       "bvPSStatus": bvPSStatus,
       "bvPSDestination": bvPSDestination,
       "bvPrinterStatus": bvPrinterStatus,
       "bvJobActive": bvJobActive,
       "bvJobSource": bvJobSource,
       "bvJobTitle": bvJobTitle,
       "bvJobSize": bvJobSize,
       "bvJobNumber": bvJobNumber,
       "lanManager": lanManager,
       "lmGroupVersion": lmGroupVersion,
       "lmEnabled": lmEnabled,
       "eTalk": eTalk,
       "eTalkGroupVersion": eTalkGroupVersion,
       "eTalkEnabled": eTalkEnabled,
       "eTalkCommands": eTalkCommands,
       "eTalkRestoreDefaults": eTalkRestoreDefaults,
       "eTalkConfigure": eTalkConfigure,
       "eTalkNetwork": eTalkNetwork,
       "eTalkNode": eTalkNode,
       "eTalkNumPorts": eTalkNumPorts,
       "eTalkPortTable": eTalkPortTable,
       "eTalkPortEntry": eTalkPortEntry,
       "eTalkPortIndex": eTalkPortIndex,
       "eTalkPortEnable": eTalkPortEnable,
       "eTalkName": eTalkName,
       "eTalkActiveName": eTalkActiveName,
       "eTalkType1": eTalkType1,
       "eTalkType2": eTalkType2,
       "eTalkZone": eTalkZone,
       "eTalkActiveZone": eTalkActiveZone,
       "eTalkStatus": eTalkStatus,
       "eTalkError": eTalkError}
)
