# SNMP MIB module (HP700RX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP700RX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:14 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetPeripherals_ObjectIdentity = ObjectIdentity
netPeripherals = _NetPeripherals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9)
)
_HpXStation_ObjectIdentity = ObjectIdentity
hpXStation = _HpXStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1)
)
_Terminal_ObjectIdentity = ObjectIdentity
terminal = _Terminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1)
)


class _Monitor_Type(Integer32):
    """Custom type monitor based on Integer32"""
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
        *(("a1097", 1),
          ("hp98753", 6),
          ("hp98754", 2),
          ("hp98774", 11),
          ("hp98785", 7),
          ("hp98789", 3),
          ("hpa1497", 5),
          ("hpd1182", 10),
          ("hpd1187", 4),
          ("hpd1188", 8),
          ("hpd1195", 9),
          ("hpd1195x1224", 12),
          ("hpd1195x640", 13))
    )


_Monitor_Type.__name__ = "Integer32"
_Monitor_Object = MibScalar
monitor = _Monitor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 1),
    _Monitor_Type()
)
monitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitor.setStatus("mandatory")
_MonitorDescription_Type = DisplayString
_MonitorDescription_Object = MibScalar
monitorDescription = _MonitorDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 2),
    _MonitorDescription_Type()
)
monitorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorDescription.setStatus("mandatory")


class _At2kbLEDControl_Type(Integer32):
    """Custom type at2kbLEDControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("local", 2))
    )


_At2kbLEDControl_Type.__name__ = "Integer32"
_At2kbLEDControl_Object = MibScalar
at2kbLEDControl = _At2kbLEDControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 3),
    _At2kbLEDControl_Type()
)
at2kbLEDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    at2kbLEDControl.setStatus("mandatory")


class _At2kbLanguage_Type(Integer32):
    """Custom type at2kbLanguage based on Integer32"""
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
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("belgian", 9),
          ("candianenglish", 15),
          ("candianfrench", 6),
          ("danish", 2),
          ("decLK401english", 21),
          ("dutch", 13),
          ("english", 7),
          ("finnish", 8),
          ("french", 3),
          ("german", 11),
          ("hangul", 17),
          ("italian", 14),
          ("kanji", 20),
          ("norwegian", 4),
          ("reserved", 22),
          ("simplifiedchinese", 18),
          ("spanish", 10),
          ("swedish", 12),
          ("swissfrench", 16),
          ("swissgerman", 5),
          ("traditionalchinese", 19),
          ("usascii", 1))
    )


_At2kbLanguage_Type.__name__ = "Integer32"
_At2kbLanguage_Object = MibScalar
at2kbLanguage = _At2kbLanguage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 4),
    _At2kbLanguage_Type()
)
at2kbLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    at2kbLanguage.setStatus("mandatory")


class _SerialSpeed_Type(Integer32):
    """Custom type serialSpeed based on Integer32"""
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
        *(("bps1200", 5),
          ("bps150", 2),
          ("bps19200", 9),
          ("bps2400", 6),
          ("bps300", 3),
          ("bps38400", 10),
          ("bps4800", 7),
          ("bps600", 4),
          ("bps75", 1),
          ("bps9600", 8))
    )


_SerialSpeed_Type.__name__ = "Integer32"
_SerialSpeed_Object = MibScalar
serialSpeed = _SerialSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 5),
    _SerialSpeed_Type()
)
serialSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialSpeed.setStatus("mandatory")


class _SerialDataBits_Type(Integer32):
    """Custom type serialDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bits7", 1),
          ("bits8", 2))
    )


_SerialDataBits_Type.__name__ = "Integer32"
_SerialDataBits_Object = MibScalar
serialDataBits = _SerialDataBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 6),
    _SerialDataBits_Type()
)
serialDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDataBits.setStatus("mandatory")


class _SerialStopBits_Type(Integer32):
    """Custom type serialStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bits1", 1),
          ("bits2", 2))
    )


_SerialStopBits_Type.__name__ = "Integer32"
_SerialStopBits_Object = MibScalar
serialStopBits = _SerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 7),
    _SerialStopBits_Type()
)
serialStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialStopBits.setStatus("mandatory")


class _SerialParity_Type(Integer32):
    """Custom type serialParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 1),
          ("odd", 3))
    )


_SerialParity_Type.__name__ = "Integer32"
_SerialParity_Object = MibScalar
serialParity = _SerialParity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 8),
    _SerialParity_Type()
)
serialParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialParity.setStatus("mandatory")


class _SerialPacing_Type(Integer32):
    """Custom type serialPacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rtscts", 3),
          ("xonxoff", 2))
    )


_SerialPacing_Type.__name__ = "Integer32"
_SerialPacing_Object = MibScalar
serialPacing = _SerialPacing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 9),
    _SerialPacing_Type()
)
serialPacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPacing.setStatus("mandatory")


class _SerialUse_Type(Integer32):
    """Custom type serialUse based on Integer32"""
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
        *(("auxiliary", 3),
          ("diagnostics", 4),
          ("disabled", 1),
          ("primary", 2),
          ("serialsession", 5),
          ("slip", 6))
    )


_SerialUse_Type.__name__ = "Integer32"
_SerialUse_Object = MibScalar
serialUse = _SerialUse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 10),
    _SerialUse_Type()
)
serialUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialUse.setStatus("mandatory")


class _ParallelUse_Type(Integer32):
    """Custom type parallelUse based on Integer32"""
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
        *(("auxiliary", 3),
          ("diagnostics", 4),
          ("disabled", 1),
          ("primary", 2))
    )


_ParallelUse_Type.__name__ = "Integer32"
_ParallelUse_Object = MibScalar
parallelUse = _ParallelUse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 11),
    _ParallelUse_Type()
)
parallelUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parallelUse.setStatus("mandatory")


class _PortuseEnable_Type(Integer32):
    """Custom type portuseEnable based on Integer32"""
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


_PortuseEnable_Type.__name__ = "Integer32"
_PortuseEnable_Object = MibScalar
portuseEnable = _PortuseEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 1, 12),
    _PortuseEnable_Type()
)
portuseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portuseEnable.setStatus("mandatory")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2)
)


class _NetworkParamsFrom_Type(Integer32):
    """Custom type networkParamsFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 1),
          ("eeprom", 2))
    )


_NetworkParamsFrom_Type.__name__ = "Integer32"
_NetworkParamsFrom_Object = MibScalar
networkParamsFrom = _NetworkParamsFrom_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 1),
    _NetworkParamsFrom_Type()
)
networkParamsFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkParamsFrom.setStatus("mandatory")
_ConfigedAddress_Type = DisplayString
_ConfigedAddress_Object = MibScalar
configedAddress = _ConfigedAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 2),
    _ConfigedAddress_Type()
)
configedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configedAddress.setStatus("mandatory")
_ConfigedSubnetMask_Type = DisplayString
_ConfigedSubnetMask_Object = MibScalar
configedSubnetMask = _ConfigedSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 3),
    _ConfigedSubnetMask_Type()
)
configedSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configedSubnetMask.setStatus("mandatory")
_ConfigedRouteTable_Object = MibTable
configedRouteTable = _ConfigedRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    configedRouteTable.setStatus("mandatory")
_RouteTableEntry_Object = MibTableRow
routeTableEntry = _RouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 4, 1)
)
routeTableEntry.setIndexNames(
    (0, "HP700RX-MIB", "routeIndex"),
)
if mibBuilder.loadTexts:
    routeTableEntry.setStatus("mandatory")
_RouteIndex_Type = Integer32
_RouteIndex_Object = MibTableColumn
routeIndex = _RouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 4, 1, 1),
    _RouteIndex_Type()
)
routeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeIndex.setStatus("mandatory")
_RouteGateway_Type = DisplayString
_RouteGateway_Object = MibTableColumn
routeGateway = _RouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 4, 1, 2),
    _RouteGateway_Type()
)
routeGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeGateway.setStatus("mandatory")
_RouteDestination_Type = DisplayString
_RouteDestination_Object = MibTableColumn
routeDestination = _RouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 4, 1, 3),
    _RouteDestination_Type()
)
routeDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeDestination.setStatus("mandatory")
_PrimaryFileServer_Type = DisplayString
_PrimaryFileServer_Object = MibScalar
primaryFileServer = _PrimaryFileServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 5),
    _PrimaryFileServer_Type()
)
primaryFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryFileServer.setStatus("mandatory")


class _PrimaryAccessMethod_Type(Integer32):
    """Custom type primaryAccessMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nfs", 2),
          ("tftp", 1))
    )


_PrimaryAccessMethod_Type.__name__ = "Integer32"
_PrimaryAccessMethod_Object = MibScalar
primaryAccessMethod = _PrimaryAccessMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 6),
    _PrimaryAccessMethod_Type()
)
primaryAccessMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryAccessMethod.setStatus("mandatory")
_AlternateFileServer_Type = DisplayString
_AlternateFileServer_Object = MibScalar
alternateFileServer = _AlternateFileServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 7),
    _AlternateFileServer_Type()
)
alternateFileServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateFileServer.setStatus("mandatory")


class _AlternateAccessMethod_Type(Integer32):
    """Custom type alternateAccessMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nfs", 2),
          ("tftp", 1))
    )


_AlternateAccessMethod_Type.__name__ = "Integer32"
_AlternateAccessMethod_Object = MibScalar
alternateAccessMethod = _AlternateAccessMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 8),
    _AlternateAccessMethod_Type()
)
alternateAccessMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateAccessMethod.setStatus("mandatory")
_FileTimeout_Type = Integer32
_FileTimeout_Object = MibScalar
fileTimeout = _FileTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 9),
    _FileTimeout_Type()
)
fileTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTimeout.setStatus("mandatory")
_PrimaryNameServer_Type = DisplayString
_PrimaryNameServer_Object = MibScalar
primaryNameServer = _PrimaryNameServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 10),
    _PrimaryNameServer_Type()
)
primaryNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryNameServer.setStatus("mandatory")
_AlternateNameServer_Type = DisplayString
_AlternateNameServer_Object = MibScalar
alternateNameServer = _AlternateNameServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 11),
    _AlternateNameServer_Type()
)
alternateNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateNameServer.setStatus("mandatory")
_Domain_Type = DisplayString
_Domain_Object = MibScalar
domain = _Domain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 12),
    _Domain_Type()
)
domain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domain.setStatus("mandatory")
_TerminalName_Type = DisplayString
_TerminalName_Object = MibScalar
terminalName = _TerminalName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 13),
    _TerminalName_Type()
)
terminalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminalName.setStatus("mandatory")
_SlipLocalAddress_Type = DisplayString
_SlipLocalAddress_Object = MibScalar
slipLocalAddress = _SlipLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 14),
    _SlipLocalAddress_Type()
)
slipLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipLocalAddress.setStatus("mandatory")
_SlipRemoteAddress_Type = DisplayString
_SlipRemoteAddress_Object = MibScalar
slipRemoteAddress = _SlipRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 15),
    _SlipRemoteAddress_Type()
)
slipRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipRemoteAddress.setStatus("mandatory")
_SlipMask_Type = DisplayString
_SlipMask_Object = MibScalar
slipMask = _SlipMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 2, 16),
    _SlipMask_Type()
)
slipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipMask.setStatus("mandatory")
_Startup_ObjectIdentity = ObjectIdentity
startup = _Startup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3)
)


class _RomFonts_Type(Integer32):
    """Custom type romFonts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_RomFonts_Type.__name__ = "Integer32"
_RomFonts_Object = MibScalar
romFonts = _RomFonts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 1),
    _RomFonts_Type()
)
romFonts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    romFonts.setStatus("mandatory")


class _RgbFileFrom_Type(Integer32):
    """Custom type rgbFileFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("rom", 2))
    )


_RgbFileFrom_Type.__name__ = "Integer32"
_RgbFileFrom_Object = MibScalar
rgbFileFrom = _RgbFileFrom_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 2),
    _RgbFileFrom_Type()
)
rgbFileFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgbFileFrom.setStatus("mandatory")


class _BootFileFrom_Type(Integer32):
    """Custom type bootFileFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("rom", 2))
    )


_BootFileFrom_Type.__name__ = "Integer32"
_BootFileFrom_Object = MibScalar
bootFileFrom = _BootFileFrom_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 3),
    _BootFileFrom_Type()
)
bootFileFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootFileFrom.setStatus("mandatory")
_BootFileName_Type = DisplayString
_BootFileName_Object = MibScalar
bootFileName = _BootFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 4),
    _BootFileName_Type()
)
bootFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootFileName.setStatus("mandatory")


class _RemoteConfigEnabled_Type(Integer32):
    """Custom type remoteConfigEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_RemoteConfigEnabled_Type.__name__ = "Integer32"
_RemoteConfigEnabled_Object = MibScalar
remoteConfigEnabled = _RemoteConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 5),
    _RemoteConfigEnabled_Type()
)
remoteConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteConfigEnabled.setStatus("mandatory")
_RemoteConfigFile_Type = DisplayString
_RemoteConfigFile_Object = MibScalar
remoteConfigFile = _RemoteConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 6),
    _RemoteConfigFile_Type()
)
remoteConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteConfigFile.setStatus("mandatory")


class _XdmcpEnabled_Type(Integer32):
    """Custom type xdmcpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_XdmcpEnabled_Type.__name__ = "Integer32"
_XdmcpEnabled_Object = MibScalar
xdmcpEnabled = _XdmcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 7),
    _XdmcpEnabled_Type()
)
xdmcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdmcpEnabled.setStatus("mandatory")


class _XdmcpType_Type(Integer32):
    """Custom type xdmcpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("direct", 2),
          ("indirect", 3))
    )


_XdmcpType_Type.__name__ = "Integer32"
_XdmcpType_Object = MibScalar
xdmcpType = _XdmcpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 8),
    _XdmcpType_Type()
)
xdmcpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdmcpType.setStatus("mandatory")
_XdmcpHost_Type = DisplayString
_XdmcpHost_Object = MibScalar
xdmcpHost = _XdmcpHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 9),
    _XdmcpHost_Type()
)
xdmcpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdmcpHost.setStatus("mandatory")


class _TelnetAutoStart_Type(Integer32):
    """Custom type telnetAutoStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TelnetAutoStart_Type.__name__ = "Integer32"
_TelnetAutoStart_Object = MibScalar
telnetAutoStart = _TelnetAutoStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 10),
    _TelnetAutoStart_Type()
)
telnetAutoStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetAutoStart.setStatus("mandatory")


class _TelnetCharSet_Type(Integer32):
    """Custom type telnetCharSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hpRoman8", 3),
          ("isoLatin1", 2),
          ("usascii", 1))
    )


_TelnetCharSet_Type.__name__ = "Integer32"
_TelnetCharSet_Object = MibScalar
telnetCharSet = _TelnetCharSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 11),
    _TelnetCharSet_Type()
)
telnetCharSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetCharSet.setStatus("mandatory")
_TelnetHost_Type = DisplayString
_TelnetHost_Object = MibScalar
telnetHost = _TelnetHost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 12),
    _TelnetHost_Type()
)
telnetHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetHost.setStatus("mandatory")
_FontPathTable_Object = MibTable
fontPathTable = _FontPathTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 13)
)
if mibBuilder.loadTexts:
    fontPathTable.setStatus("mandatory")
_FontEntry_Object = MibTableRow
fontEntry = _FontEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 13, 1)
)
fontEntry.setIndexNames(
    (0, "HP700RX-MIB", "fontIndex"),
)
if mibBuilder.loadTexts:
    fontEntry.setStatus("mandatory")
_FontIndex_Type = Integer32
_FontIndex_Object = MibTableColumn
fontIndex = _FontIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 13, 1, 1),
    _FontIndex_Type()
)
fontIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fontIndex.setStatus("mandatory")
_FontPath_Type = DisplayString
_FontPath_Object = MibTableColumn
fontPath = _FontPath_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 3, 13, 1, 2),
    _FontPath_Type()
)
fontPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fontPath.setStatus("mandatory")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4)
)
_MemInstalled_Type = Integer32
_MemInstalled_Object = MibScalar
memInstalled = _MemInstalled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 1),
    _MemInstalled_Type()
)
memInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memInstalled.setStatus("mandatory")
_MemFree_Type = Integer32
_MemFree_Object = MibScalar
memFree = _MemFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 2),
    _MemFree_Type()
)
memFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFree.setStatus("mandatory")
_MemLowMark_Type = Integer32
_MemLowMark_Object = MibScalar
memLowMark = _MemLowMark_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 3),
    _MemLowMark_Type()
)
memLowMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memLowMark.setStatus("mandatory")
_MemFrags_Type = Integer32
_MemFrags_Object = MibScalar
memFrags = _MemFrags_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 4),
    _MemFrags_Type()
)
memFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFrags.setStatus("mandatory")
_MemLargestFrag_Type = Integer32
_MemLargestFrag_Object = MibScalar
memLargestFrag = _MemLargestFrag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 5),
    _MemLargestFrag_Type()
)
memLargestFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memLargestFrag.setStatus("mandatory")
_MemBackingstore_Type = Integer32
_MemBackingstore_Object = MibScalar
memBackingstore = _MemBackingstore_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 6),
    _MemBackingstore_Type()
)
memBackingstore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBackingstore.setStatus("mandatory")
_MemReclaims_Type = Counter32
_MemReclaims_Object = MibScalar
memReclaims = _MemReclaims_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 7),
    _MemReclaims_Type()
)
memReclaims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memReclaims.setStatus("mandatory")
_SerialInOctets_Type = Counter32
_SerialInOctets_Object = MibScalar
serialInOctets = _SerialInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 8),
    _SerialInOctets_Type()
)
serialInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialInOctets.setStatus("mandatory")
_SerialOutOctets_Type = Counter32
_SerialOutOctets_Object = MibScalar
serialOutOctets = _SerialOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 9),
    _SerialOutOctets_Type()
)
serialOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialOutOctets.setStatus("mandatory")
_SerialInErrors_Type = Counter32
_SerialInErrors_Object = MibScalar
serialInErrors = _SerialInErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 10),
    _SerialInErrors_Type()
)
serialInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialInErrors.setStatus("mandatory")
_ParallelOutOctets_Type = Counter32
_ParallelOutOctets_Object = MibScalar
parallelOutOctets = _ParallelOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 11),
    _ParallelOutOctets_Type()
)
parallelOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelOutOctets.setStatus("mandatory")
_ParallelErrors_Type = Counter32
_ParallelErrors_Object = MibScalar
parallelErrors = _ParallelErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 12),
    _ParallelErrors_Type()
)
parallelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parallelErrors.setStatus("mandatory")
_EtherInPackets_Type = Counter32
_EtherInPackets_Object = MibScalar
etherInPackets = _EtherInPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 13),
    _EtherInPackets_Type()
)
etherInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherInPackets.setStatus("mandatory")
_EtherInCRCErrors_Type = Counter32
_EtherInCRCErrors_Object = MibScalar
etherInCRCErrors = _EtherInCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 14),
    _EtherInCRCErrors_Type()
)
etherInCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherInCRCErrors.setStatus("mandatory")
_EtherInNoBuffers_Type = Counter32
_EtherInNoBuffers_Object = MibScalar
etherInNoBuffers = _EtherInNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 15),
    _EtherInNoBuffers_Type()
)
etherInNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherInNoBuffers.setStatus("mandatory")
_EtherInRunts_Type = Counter32
_EtherInRunts_Object = MibScalar
etherInRunts = _EtherInRunts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 16),
    _EtherInRunts_Type()
)
etherInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherInRunts.setStatus("mandatory")
_EtherInOctets_Type = Counter32
_EtherInOctets_Object = MibScalar
etherInOctets = _EtherInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 17),
    _EtherInOctets_Type()
)
etherInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherInOctets.setStatus("mandatory")
_EtherOutPackets_Type = Counter32
_EtherOutPackets_Object = MibScalar
etherOutPackets = _EtherOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 18),
    _EtherOutPackets_Type()
)
etherOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOutPackets.setStatus("mandatory")
_EtherOutOneCollisions_Type = Counter32
_EtherOutOneCollisions_Object = MibScalar
etherOutOneCollisions = _EtherOutOneCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 19),
    _EtherOutOneCollisions_Type()
)
etherOutOneCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOutOneCollisions.setStatus("mandatory")
_EtherOutTwoCollisions_Type = Counter32
_EtherOutTwoCollisions_Object = MibScalar
etherOutTwoCollisions = _EtherOutTwoCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 20),
    _EtherOutTwoCollisions_Type()
)
etherOutTwoCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOutTwoCollisions.setStatus("mandatory")
_EtherOutMoreCollisions_Type = Counter32
_EtherOutMoreCollisions_Object = MibScalar
etherOutMoreCollisions = _EtherOutMoreCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 21),
    _EtherOutMoreCollisions_Type()
)
etherOutMoreCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOutMoreCollisions.setStatus("mandatory")
_EtherOutMaxCollisions_Type = Counter32
_EtherOutMaxCollisions_Object = MibScalar
etherOutMaxCollisions = _EtherOutMaxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 22),
    _EtherOutMaxCollisions_Type()
)
etherOutMaxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOutMaxCollisions.setStatus("mandatory")
_EtherOutNoBuffers_Type = Counter32
_EtherOutNoBuffers_Object = MibScalar
etherOutNoBuffers = _EtherOutNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 23),
    _EtherOutNoBuffers_Type()
)
etherOutNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOutNoBuffers.setStatus("mandatory")
_EtherOutOctets_Type = Counter32
_EtherOutOctets_Object = MibScalar
etherOutOctets = _EtherOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 24),
    _EtherOutOctets_Type()
)
etherOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherOutOctets.setStatus("mandatory")
_TftpTimeouts_Type = Counter32
_TftpTimeouts_Object = MibScalar
tftpTimeouts = _TftpTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 25),
    _TftpTimeouts_Type()
)
tftpTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpTimeouts.setStatus("mandatory")
_StatsTime_Type = TimeTicks
_StatsTime_Object = MibScalar
statsTime = _StatsTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 26),
    _StatsTime_Type()
)
statsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsTime.setStatus("mandatory")
_SlipInPackets_Type = Counter32
_SlipInPackets_Object = MibScalar
slipInPackets = _SlipInPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 27),
    _SlipInPackets_Type()
)
slipInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipInPackets.setStatus("mandatory")
_SlipInOctets_Type = Counter32
_SlipInOctets_Object = MibScalar
slipInOctets = _SlipInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 28),
    _SlipInOctets_Type()
)
slipInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipInOctets.setStatus("mandatory")
_SlipInErrs_Type = Counter32
_SlipInErrs_Object = MibScalar
slipInErrs = _SlipInErrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 29),
    _SlipInErrs_Type()
)
slipInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipInErrs.setStatus("mandatory")
_SlipOutPackets_Type = Counter32
_SlipOutPackets_Object = MibScalar
slipOutPackets = _SlipOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 30),
    _SlipOutPackets_Type()
)
slipOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipOutPackets.setStatus("mandatory")
_SlipOutOctets_Type = Counter32
_SlipOutOctets_Object = MibScalar
slipOutOctets = _SlipOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 31),
    _SlipOutOctets_Type()
)
slipOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipOutOctets.setStatus("mandatory")
_SlipOutErrors_Type = Counter32
_SlipOutErrors_Object = MibScalar
slipOutErrors = _SlipOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 32),
    _SlipOutErrors_Type()
)
slipOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipOutErrors.setStatus("mandatory")
_EtherInAlignErrors_Type = Counter32
_EtherInAlignErrors_Object = MibScalar
etherInAlignErrors = _EtherInAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 33),
    _EtherInAlignErrors_Type()
)
etherInAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherInAlignErrors.setStatus("mandatory")
_EtherInCollisions_Type = Counter32
_EtherInCollisions_Object = MibScalar
etherInCollisions = _EtherInCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 4, 34),
    _EtherInCollisions_Type()
)
etherInCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherInCollisions.setStatus("mandatory")
_Preferences_ObjectIdentity = ObjectIdentity
preferences = _Preferences_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 5)
)


class _ClientAuthentication_Type(Integer32):
    """Custom type clientAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientAuthentication_Type.__name__ = "Integer32"
_ClientAuthentication_Object = MibScalar
clientAuthentication = _ClientAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 5, 1),
    _ClientAuthentication_Type()
)
clientAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientAuthentication.setStatus("mandatory")


class _AccessControls_Type(Integer32):
    """Custom type accessControls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AccessControls_Type.__name__ = "Integer32"
_AccessControls_Object = MibScalar
accessControls = _AccessControls_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 5, 2),
    _AccessControls_Type()
)
accessControls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControls.setStatus("mandatory")


class _R3BugCompatability_Type(Integer32):
    """Custom type r3BugCompatability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_R3BugCompatability_Type.__name__ = "Integer32"
_R3BugCompatability_Object = MibScalar
r3BugCompatability = _R3BugCompatability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 5, 3),
    _R3BugCompatability_Type()
)
r3BugCompatability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    r3BugCompatability.setStatus("mandatory")
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 6)
)


class _ResetEnable_Type(Integer32):
    """Custom type resetEnable based on Integer32"""
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


_ResetEnable_Type.__name__ = "Integer32"
_ResetEnable_Object = MibScalar
resetEnable = _ResetEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 6, 1),
    _ResetEnable_Type()
)
resetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetEnable.setStatus("mandatory")


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont", 2),
          ("reset", 1))
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 3, 1, 6, 2),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("mandatory")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4)
)
_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 7)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 1)
)
_SnmpdConf_ObjectIdentity = ObjectIdentity
snmpdConf = _SnmpdConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 13, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP700RX-MIB",
    **{"hp": hp,
       "nm": nm,
       "system": system,
       "netPeripherals": netPeripherals,
       "hpXStation": hpXStation,
       "config": config,
       "terminal": terminal,
       "monitor": monitor,
       "monitorDescription": monitorDescription,
       "at2kbLEDControl": at2kbLEDControl,
       "at2kbLanguage": at2kbLanguage,
       "serialSpeed": serialSpeed,
       "serialDataBits": serialDataBits,
       "serialStopBits": serialStopBits,
       "serialParity": serialParity,
       "serialPacing": serialPacing,
       "serialUse": serialUse,
       "parallelUse": parallelUse,
       "portuseEnable": portuseEnable,
       "network": network,
       "networkParamsFrom": networkParamsFrom,
       "configedAddress": configedAddress,
       "configedSubnetMask": configedSubnetMask,
       "configedRouteTable": configedRouteTable,
       "routeTableEntry": routeTableEntry,
       "routeIndex": routeIndex,
       "routeGateway": routeGateway,
       "routeDestination": routeDestination,
       "primaryFileServer": primaryFileServer,
       "primaryAccessMethod": primaryAccessMethod,
       "alternateFileServer": alternateFileServer,
       "alternateAccessMethod": alternateAccessMethod,
       "fileTimeout": fileTimeout,
       "primaryNameServer": primaryNameServer,
       "alternateNameServer": alternateNameServer,
       "domain": domain,
       "terminalName": terminalName,
       "slipLocalAddress": slipLocalAddress,
       "slipRemoteAddress": slipRemoteAddress,
       "slipMask": slipMask,
       "startup": startup,
       "romFonts": romFonts,
       "rgbFileFrom": rgbFileFrom,
       "bootFileFrom": bootFileFrom,
       "bootFileName": bootFileName,
       "remoteConfigEnabled": remoteConfigEnabled,
       "remoteConfigFile": remoteConfigFile,
       "xdmcpEnabled": xdmcpEnabled,
       "xdmcpType": xdmcpType,
       "xdmcpHost": xdmcpHost,
       "telnetAutoStart": telnetAutoStart,
       "telnetCharSet": telnetCharSet,
       "telnetHost": telnetHost,
       "fontPathTable": fontPathTable,
       "fontEntry": fontEntry,
       "fontIndex": fontIndex,
       "fontPath": fontPath,
       "statistics": statistics,
       "memInstalled": memInstalled,
       "memFree": memFree,
       "memLowMark": memLowMark,
       "memFrags": memFrags,
       "memLargestFrag": memLargestFrag,
       "memBackingstore": memBackingstore,
       "memReclaims": memReclaims,
       "serialInOctets": serialInOctets,
       "serialOutOctets": serialOutOctets,
       "serialInErrors": serialInErrors,
       "parallelOutOctets": parallelOutOctets,
       "parallelErrors": parallelErrors,
       "etherInPackets": etherInPackets,
       "etherInCRCErrors": etherInCRCErrors,
       "etherInNoBuffers": etherInNoBuffers,
       "etherInRunts": etherInRunts,
       "etherInOctets": etherInOctets,
       "etherOutPackets": etherOutPackets,
       "etherOutOneCollisions": etherOutOneCollisions,
       "etherOutTwoCollisions": etherOutTwoCollisions,
       "etherOutMoreCollisions": etherOutMoreCollisions,
       "etherOutMaxCollisions": etherOutMaxCollisions,
       "etherOutNoBuffers": etherOutNoBuffers,
       "etherOutOctets": etherOutOctets,
       "tftpTimeouts": tftpTimeouts,
       "statsTime": statsTime,
       "slipInPackets": slipInPackets,
       "slipInOctets": slipInOctets,
       "slipInErrs": slipInErrs,
       "slipOutPackets": slipOutPackets,
       "slipOutOctets": slipOutOctets,
       "slipOutErrors": slipOutErrors,
       "etherInAlignErrors": etherInAlignErrors,
       "etherInCollisions": etherInCollisions,
       "preferences": preferences,
       "clientAuthentication": clientAuthentication,
       "accessControls": accessControls,
       "r3BugCompatability": r3BugCompatability,
       "reset": reset,
       "resetEnable": resetEnable,
       "reboot": reboot,
       "interface": interface,
       "icmp": icmp,
       "snmp": snmp,
       "trap": trap,
       "snmpdConf": snmpdConf}
)
