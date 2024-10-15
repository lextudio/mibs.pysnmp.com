# SNMP MIB module (Pulizzi) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Pulizzi
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:34 2024
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

pulizzi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20677)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipc3600_ObjectIdentity = ObjectIdentity
ipc3600 = _Ipc3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1)
)
_UnitConfig_ObjectIdentity = ObjectIdentity
unitConfig = _UnitConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 1)
)
_UnitName_Type = OctetString
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 1, 1),
    _UnitName_Type()
)
unitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitName.setStatus("current")
_UnitTime_Type = OctetString
_UnitTime_Object = MibScalar
unitTime = _UnitTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 1, 2),
    _UnitTime_Type()
)
unitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitTime.setStatus("current")
_UnitDate_Type = OctetString
_UnitDate_Object = MibScalar
unitDate = _UnitDate_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 1, 3),
    _UnitDate_Type()
)
unitDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitDate.setStatus("current")


class _UnitDayOfWeek_Type(Integer32):
    """Custom type unitDayOfWeek based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UnitDayOfWeek_Type.__name__ = "Integer32"
_UnitDayOfWeek_Object = MibScalar
unitDayOfWeek = _UnitDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 1, 4),
    _UnitDayOfWeek_Type()
)
unitDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitDayOfWeek.setStatus("current")
_KeyBoardTime_Type = Integer32
_KeyBoardTime_Object = MibScalar
keyBoardTime = _KeyBoardTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 1, 5),
    _KeyBoardTime_Type()
)
keyBoardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyBoardTime.setStatus("current")
_NetworkSettings_ObjectIdentity = ObjectIdentity
networkSettings = _NetworkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 2)
)
_UnitIPAddress_Type = IpAddress
_UnitIPAddress_Object = MibScalar
unitIPAddress = _UnitIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 2, 1),
    _UnitIPAddress_Type()
)
unitIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitIPAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 2, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 2, 3),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")
_WebPort_Type = Integer32
_WebPort_Object = MibScalar
webPort = _WebPort_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 2, 4),
    _WebPort_Type()
)
webPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webPort.setStatus("current")


class _WebEnabled_Type(Integer32):
    """Custom type webEnabled based on Integer32"""
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


_WebEnabled_Type.__name__ = "Integer32"
_WebEnabled_Object = MibScalar
webEnabled = _WebEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 2, 5),
    _WebEnabled_Type()
)
webEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webEnabled.setStatus("current")
_MacAddress_Type = OctetString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 2, 6),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_SerialSettings_ObjectIdentity = ObjectIdentity
serialSettings = _SerialSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 3)
)
_BaudRate_Type = Integer32
_BaudRate_Object = MibScalar
baudRate = _BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 3, 1),
    _BaudRate_Type()
)
baudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baudRate.setStatus("current")
_TelnetSettings_ObjectIdentity = ObjectIdentity
telnetSettings = _TelnetSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 4)
)
_TelnetPort_Type = Integer32
_TelnetPort_Object = MibScalar
telnetPort = _TelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 4, 1),
    _TelnetPort_Type()
)
telnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPort.setStatus("current")


class _TelnetEnabled_Type(Integer32):
    """Custom type telnetEnabled based on Integer32"""
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


_TelnetEnabled_Type.__name__ = "Integer32"
_TelnetEnabled_Object = MibScalar
telnetEnabled = _TelnetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 4, 2),
    _TelnetEnabled_Type()
)
telnetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetEnabled.setStatus("current")
_OutletMngt_ObjectIdentity = ObjectIdentity
outletMngt = _OutletMngt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5)
)
_OutletConfig_ObjectIdentity = ObjectIdentity
outletConfig = _OutletConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1)
)
_Outlet1_ObjectIdentity = ObjectIdentity
outlet1 = _Outlet1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 1)
)
_Outlet1Name_Type = OctetString
_Outlet1Name_Object = MibScalar
outlet1Name = _Outlet1Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 1, 1),
    _Outlet1Name_Type()
)
outlet1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1Name.setStatus("current")
_Outlet1Link_Type = OctetString
_Outlet1Link_Object = MibScalar
outlet1Link = _Outlet1Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 1, 2),
    _Outlet1Link_Type()
)
outlet1Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1Link.setStatus("current")
_Outlet1SequenceTime_Type = Integer32
_Outlet1SequenceTime_Object = MibScalar
outlet1SequenceTime = _Outlet1SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 1, 3),
    _Outlet1SequenceTime_Type()
)
outlet1SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1SequenceTime.setStatus("current")
_Outlet1RebootTime_Type = Integer32
_Outlet1RebootTime_Object = MibScalar
outlet1RebootTime = _Outlet1RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 1, 4),
    _Outlet1RebootTime_Type()
)
outlet1RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1RebootTime.setStatus("current")
_Outlet2_ObjectIdentity = ObjectIdentity
outlet2 = _Outlet2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 2)
)
_Outlet2Name_Type = OctetString
_Outlet2Name_Object = MibScalar
outlet2Name = _Outlet2Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 2, 1),
    _Outlet2Name_Type()
)
outlet2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2Name.setStatus("current")
_Outlet2Link_Type = OctetString
_Outlet2Link_Object = MibScalar
outlet2Link = _Outlet2Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 2, 2),
    _Outlet2Link_Type()
)
outlet2Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2Link.setStatus("current")
_Outlet2SequenceTime_Type = Integer32
_Outlet2SequenceTime_Object = MibScalar
outlet2SequenceTime = _Outlet2SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 2, 3),
    _Outlet2SequenceTime_Type()
)
outlet2SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2SequenceTime.setStatus("current")
_Outlet2RebootTime_Type = Integer32
_Outlet2RebootTime_Object = MibScalar
outlet2RebootTime = _Outlet2RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 2, 4),
    _Outlet2RebootTime_Type()
)
outlet2RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2RebootTime.setStatus("current")
_Outlet3_ObjectIdentity = ObjectIdentity
outlet3 = _Outlet3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 3)
)
_Outlet3Name_Type = OctetString
_Outlet3Name_Object = MibScalar
outlet3Name = _Outlet3Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 3, 1),
    _Outlet3Name_Type()
)
outlet3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3Name.setStatus("current")
_Outlet3Link_Type = OctetString
_Outlet3Link_Object = MibScalar
outlet3Link = _Outlet3Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 3, 2),
    _Outlet3Link_Type()
)
outlet3Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3Link.setStatus("current")
_Outlet3SequenceTime_Type = Integer32
_Outlet3SequenceTime_Object = MibScalar
outlet3SequenceTime = _Outlet3SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 3, 3),
    _Outlet3SequenceTime_Type()
)
outlet3SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3SequenceTime.setStatus("current")
_Outlet3RebootTime_Type = Integer32
_Outlet3RebootTime_Object = MibScalar
outlet3RebootTime = _Outlet3RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 3, 4),
    _Outlet3RebootTime_Type()
)
outlet3RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3RebootTime.setStatus("current")
_Outlet4_ObjectIdentity = ObjectIdentity
outlet4 = _Outlet4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 4)
)
_Outlet4Name_Type = OctetString
_Outlet4Name_Object = MibScalar
outlet4Name = _Outlet4Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 4, 1),
    _Outlet4Name_Type()
)
outlet4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4Name.setStatus("current")
_Outlet4Link_Type = OctetString
_Outlet4Link_Object = MibScalar
outlet4Link = _Outlet4Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 4, 2),
    _Outlet4Link_Type()
)
outlet4Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4Link.setStatus("current")
_Outlet4SequenceTime_Type = Integer32
_Outlet4SequenceTime_Object = MibScalar
outlet4SequenceTime = _Outlet4SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 4, 3),
    _Outlet4SequenceTime_Type()
)
outlet4SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4SequenceTime.setStatus("current")
_Outlet4RebootTime_Type = Integer32
_Outlet4RebootTime_Object = MibScalar
outlet4RebootTime = _Outlet4RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 4, 4),
    _Outlet4RebootTime_Type()
)
outlet4RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4RebootTime.setStatus("current")
_Outlet5_ObjectIdentity = ObjectIdentity
outlet5 = _Outlet5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 5)
)
_Outlet5Name_Type = OctetString
_Outlet5Name_Object = MibScalar
outlet5Name = _Outlet5Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 5, 1),
    _Outlet5Name_Type()
)
outlet5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5Name.setStatus("current")
_Outlet5Link_Type = OctetString
_Outlet5Link_Object = MibScalar
outlet5Link = _Outlet5Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 5, 2),
    _Outlet5Link_Type()
)
outlet5Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5Link.setStatus("current")
_Outlet5SequenceTime_Type = Integer32
_Outlet5SequenceTime_Object = MibScalar
outlet5SequenceTime = _Outlet5SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 5, 3),
    _Outlet5SequenceTime_Type()
)
outlet5SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5SequenceTime.setStatus("current")
_Outlet5RebootTime_Type = Integer32
_Outlet5RebootTime_Object = MibScalar
outlet5RebootTime = _Outlet5RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 5, 4),
    _Outlet5RebootTime_Type()
)
outlet5RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5RebootTime.setStatus("current")
_Outlet6_ObjectIdentity = ObjectIdentity
outlet6 = _Outlet6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 6)
)
_Outlet6Name_Type = OctetString
_Outlet6Name_Object = MibScalar
outlet6Name = _Outlet6Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 6, 1),
    _Outlet6Name_Type()
)
outlet6Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6Name.setStatus("current")
_Outlet6Link_Type = OctetString
_Outlet6Link_Object = MibScalar
outlet6Link = _Outlet6Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 6, 2),
    _Outlet6Link_Type()
)
outlet6Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6Link.setStatus("current")
_Outlet6SequenceTime_Type = Integer32
_Outlet6SequenceTime_Object = MibScalar
outlet6SequenceTime = _Outlet6SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 6, 3),
    _Outlet6SequenceTime_Type()
)
outlet6SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6SequenceTime.setStatus("current")
_Outlet6RebootTime_Type = Integer32
_Outlet6RebootTime_Object = MibScalar
outlet6RebootTime = _Outlet6RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 6, 4),
    _Outlet6RebootTime_Type()
)
outlet6RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6RebootTime.setStatus("current")
_Outlet7_ObjectIdentity = ObjectIdentity
outlet7 = _Outlet7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 7)
)
_Outlet7Name_Type = OctetString
_Outlet7Name_Object = MibScalar
outlet7Name = _Outlet7Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 7, 1),
    _Outlet7Name_Type()
)
outlet7Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7Name.setStatus("current")
_Outlet7Link_Type = OctetString
_Outlet7Link_Object = MibScalar
outlet7Link = _Outlet7Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 7, 2),
    _Outlet7Link_Type()
)
outlet7Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7Link.setStatus("current")
_Outlet7SequenceTime_Type = Integer32
_Outlet7SequenceTime_Object = MibScalar
outlet7SequenceTime = _Outlet7SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 7, 3),
    _Outlet7SequenceTime_Type()
)
outlet7SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7SequenceTime.setStatus("current")
_Outlet7RebootTime_Type = Integer32
_Outlet7RebootTime_Object = MibScalar
outlet7RebootTime = _Outlet7RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 7, 4),
    _Outlet7RebootTime_Type()
)
outlet7RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7RebootTime.setStatus("current")
_Outlet8_ObjectIdentity = ObjectIdentity
outlet8 = _Outlet8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 8)
)
_Outlet8Name_Type = OctetString
_Outlet8Name_Object = MibScalar
outlet8Name = _Outlet8Name_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 8, 1),
    _Outlet8Name_Type()
)
outlet8Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8Name.setStatus("current")
_Outlet8Link_Type = OctetString
_Outlet8Link_Object = MibScalar
outlet8Link = _Outlet8Link_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 8, 2),
    _Outlet8Link_Type()
)
outlet8Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8Link.setStatus("current")
_Outlet8SequenceTime_Type = Integer32
_Outlet8SequenceTime_Object = MibScalar
outlet8SequenceTime = _Outlet8SequenceTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 8, 3),
    _Outlet8SequenceTime_Type()
)
outlet8SequenceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8SequenceTime.setStatus("current")
_Outlet8RebootTime_Type = Integer32
_Outlet8RebootTime_Object = MibScalar
outlet8RebootTime = _Outlet8RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 1, 8, 4),
    _Outlet8RebootTime_Type()
)
outlet8RebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8RebootTime.setStatus("current")
_OutletControl_ObjectIdentity = ObjectIdentity
outletControl = _OutletControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 2)
)


class _GlobalCommand_Type(Integer32):
    """Custom type globalCommand based on Integer32"""
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
        *(("globalOff", 2),
          ("globalOn", 1),
          ("sequenceOff", 4),
          ("sequenceOn", 3))
    )


_GlobalCommand_Type.__name__ = "Integer32"
_GlobalCommand_Object = MibScalar
globalCommand = _GlobalCommand_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 2, 1),
    _GlobalCommand_Type()
)
globalCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalCommand.setStatus("current")


class _Outlet1Command_Type(Integer32):
    """Custom type outlet1Command based on Integer32"""
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
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet1Command_Type.__name__ = "Integer32"
_Outlet1Command_Object = MibScalar
outlet1Command = _Outlet1Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 2, 2),
    _Outlet1Command_Type()
)
outlet1Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet1Command.setStatus("current")


class _Outlet2Command_Type(Integer32):
    """Custom type outlet2Command based on Integer32"""
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
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet2Command_Type.__name__ = "Integer32"
_Outlet2Command_Object = MibScalar
outlet2Command = _Outlet2Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 2, 3),
    _Outlet2Command_Type()
)
outlet2Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet2Command.setStatus("current")


class _Outlet3Command_Type(Integer32):
    """Custom type outlet3Command based on Integer32"""
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
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet3Command_Type.__name__ = "Integer32"
_Outlet3Command_Object = MibScalar
outlet3Command = _Outlet3Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 2, 4),
    _Outlet3Command_Type()
)
outlet3Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet3Command.setStatus("current")


class _Outlet4Command_Type(Integer32):
    """Custom type outlet4Command based on Integer32"""
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
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet4Command_Type.__name__ = "Integer32"
_Outlet4Command_Object = MibScalar
outlet4Command = _Outlet4Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 2, 5),
    _Outlet4Command_Type()
)
outlet4Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet4Command.setStatus("current")


class _Outlet5Command_Type(Integer32):
    """Custom type outlet5Command based on Integer32"""
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
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet5Command_Type.__name__ = "Integer32"
_Outlet5Command_Object = MibScalar
outlet5Command = _Outlet5Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 2, 6),
    _Outlet5Command_Type()
)
outlet5Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet5Command.setStatus("current")


class _Outlet6Command_Type(Integer32):
    """Custom type outlet6Command based on Integer32"""
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
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet6Command_Type.__name__ = "Integer32"
_Outlet6Command_Object = MibScalar
outlet6Command = _Outlet6Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 2, 7),
    _Outlet6Command_Type()
)
outlet6Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet6Command.setStatus("current")


class _Outlet7Command_Type(Integer32):
    """Custom type outlet7Command based on Integer32"""
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
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet7Command_Type.__name__ = "Integer32"
_Outlet7Command_Object = MibScalar
outlet7Command = _Outlet7Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 2, 8),
    _Outlet7Command_Type()
)
outlet7Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet7Command.setStatus("current")


class _Outlet8Command_Type(Integer32):
    """Custom type outlet8Command based on Integer32"""
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
        *(("immediateOff", 2),
          ("immediateOn", 1),
          ("nochange", 4),
          ("reboot", 3))
    )


_Outlet8Command_Type.__name__ = "Integer32"
_Outlet8Command_Object = MibScalar
outlet8Command = _Outlet8Command_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 2, 9),
    _Outlet8Command_Type()
)
outlet8Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outlet8Command.setStatus("current")
_OutletStatus_ObjectIdentity = ObjectIdentity
outletStatus = _OutletStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 3)
)


class _Outlet1Status_Type(Integer32):
    """Custom type outlet1Status based on Integer32"""
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


_Outlet1Status_Type.__name__ = "Integer32"
_Outlet1Status_Object = MibScalar
outlet1Status = _Outlet1Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 3, 1),
    _Outlet1Status_Type()
)
outlet1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet1Status.setStatus("current")


class _Outlet2Status_Type(Integer32):
    """Custom type outlet2Status based on Integer32"""
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


_Outlet2Status_Type.__name__ = "Integer32"
_Outlet2Status_Object = MibScalar
outlet2Status = _Outlet2Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 3, 2),
    _Outlet2Status_Type()
)
outlet2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet2Status.setStatus("current")


class _Outlet3Status_Type(Integer32):
    """Custom type outlet3Status based on Integer32"""
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


_Outlet3Status_Type.__name__ = "Integer32"
_Outlet3Status_Object = MibScalar
outlet3Status = _Outlet3Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 3, 3),
    _Outlet3Status_Type()
)
outlet3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet3Status.setStatus("current")


class _Outlet4Status_Type(Integer32):
    """Custom type outlet4Status based on Integer32"""
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


_Outlet4Status_Type.__name__ = "Integer32"
_Outlet4Status_Object = MibScalar
outlet4Status = _Outlet4Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 3, 4),
    _Outlet4Status_Type()
)
outlet4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet4Status.setStatus("current")


class _Outlet5Status_Type(Integer32):
    """Custom type outlet5Status based on Integer32"""
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


_Outlet5Status_Type.__name__ = "Integer32"
_Outlet5Status_Object = MibScalar
outlet5Status = _Outlet5Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 3, 5),
    _Outlet5Status_Type()
)
outlet5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet5Status.setStatus("current")


class _Outlet6Status_Type(Integer32):
    """Custom type outlet6Status based on Integer32"""
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


_Outlet6Status_Type.__name__ = "Integer32"
_Outlet6Status_Object = MibScalar
outlet6Status = _Outlet6Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 3, 6),
    _Outlet6Status_Type()
)
outlet6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet6Status.setStatus("current")


class _Outlet7Status_Type(Integer32):
    """Custom type outlet7Status based on Integer32"""
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


_Outlet7Status_Type.__name__ = "Integer32"
_Outlet7Status_Object = MibScalar
outlet7Status = _Outlet7Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 3, 7),
    _Outlet7Status_Type()
)
outlet7Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet7Status.setStatus("current")


class _Outlet8Status_Type(Integer32):
    """Custom type outlet8Status based on Integer32"""
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


_Outlet8Status_Type.__name__ = "Integer32"
_Outlet8Status_Object = MibScalar
outlet8Status = _Outlet8Status_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 5, 3, 8),
    _Outlet8Status_Type()
)
outlet8Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outlet8Status.setStatus("current")
_LogManagerConfig_ObjectIdentity = ObjectIdentity
logManagerConfig = _LogManagerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6)
)
_MailServerIPAddress_Type = IpAddress
_MailServerIPAddress_Object = MibScalar
mailServerIPAddress = _MailServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 1),
    _MailServerIPAddress_Type()
)
mailServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailServerIPAddress.setStatus("current")
_SendLogFrom_Type = OctetString
_SendLogFrom_Object = MibScalar
sendLogFrom = _SendLogFrom_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 2),
    _SendLogFrom_Type()
)
sendLogFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendLogFrom.setStatus("current")
_SendLogToUser1Address_Type = OctetString
_SendLogToUser1Address_Object = MibScalar
sendLogToUser1Address = _SendLogToUser1Address_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 3),
    _SendLogToUser1Address_Type()
)
sendLogToUser1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendLogToUser1Address.setStatus("current")
_SendLogToUser2Address_Type = OctetString
_SendLogToUser2Address_Object = MibScalar
sendLogToUser2Address = _SendLogToUser2Address_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 4),
    _SendLogToUser2Address_Type()
)
sendLogToUser2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendLogToUser2Address.setStatus("current")
_SendAllertsToUser1Address_Type = OctetString
_SendAllertsToUser1Address_Object = MibScalar
sendAllertsToUser1Address = _SendAllertsToUser1Address_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 5),
    _SendAllertsToUser1Address_Type()
)
sendAllertsToUser1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendAllertsToUser1Address.setStatus("current")
_SendAllertsToUser2Address_Type = OctetString
_SendAllertsToUser2Address_Object = MibScalar
sendAllertsToUser2Address = _SendAllertsToUser2Address_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 6),
    _SendAllertsToUser2Address_Type()
)
sendAllertsToUser2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendAllertsToUser2Address.setStatus("current")


class _SendLogFrequency_Type(Integer32):
    """Custom type sendLogFrequency based on Integer32"""
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
        *(("daily", 8),
          ("never", 10),
          ("weekly-on-Friday", 6),
          ("weekly-on-Monday", 2),
          ("weekly-on-Saturday", 7),
          ("weekly-on-Sunday", 1),
          ("weekly-on-Thursday", 5),
          ("weekly-on-Tuesday", 3),
          ("weekly-on-Wednesday", 4),
          ("when-full", 9))
    )


_SendLogFrequency_Type.__name__ = "Integer32"
_SendLogFrequency_Object = MibScalar
sendLogFrequency = _SendLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 7),
    _SendLogFrequency_Type()
)
sendLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendLogFrequency.setStatus("current")
_SendLogTime_Type = OctetString
_SendLogTime_Object = MibScalar
sendLogTime = _SendLogTime_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 8),
    _SendLogTime_Type()
)
sendLogTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendLogTime.setStatus("current")


class _UserLogInLogOut_Type(Integer32):
    """Custom type userLogInLogOut based on Integer32"""
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
        *(("disabled", 1),
          ("sendAllert", 3),
          ("sendToLog", 2),
          ("sendtoLogAndAllert", 4))
    )


_UserLogInLogOut_Type.__name__ = "Integer32"
_UserLogInLogOut_Object = MibScalar
userLogInLogOut = _UserLogInLogOut_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 9),
    _UserLogInLogOut_Type()
)
userLogInLogOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLogInLogOut.setStatus("current")


class _UserLogInLogOutFailed_Type(Integer32):
    """Custom type userLogInLogOutFailed based on Integer32"""
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
        *(("disabled", 1),
          ("sendAllert", 3),
          ("sendToLog", 2),
          ("sendtoLogAndAllert", 4))
    )


_UserLogInLogOutFailed_Type.__name__ = "Integer32"
_UserLogInLogOutFailed_Object = MibScalar
userLogInLogOutFailed = _UserLogInLogOutFailed_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 10),
    _UserLogInLogOutFailed_Type()
)
userLogInLogOutFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLogInLogOutFailed.setStatus("current")


class _OutletActivity_Type(Integer32):
    """Custom type outletActivity based on Integer32"""
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
        *(("disabled", 1),
          ("sendAllert", 3),
          ("sendToLog", 2),
          ("sendtoLogAndAllert", 4))
    )


_OutletActivity_Type.__name__ = "Integer32"
_OutletActivity_Object = MibScalar
outletActivity = _OutletActivity_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 11),
    _OutletActivity_Type()
)
outletActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outletActivity.setStatus("current")


class _SystemOnOff_Type(Integer32):
    """Custom type systemOnOff based on Integer32"""
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
        *(("disabled", 1),
          ("sendAllert", 3),
          ("sendToLog", 2),
          ("sendtoLogAndAllert", 4))
    )


_SystemOnOff_Type.__name__ = "Integer32"
_SystemOnOff_Object = MibScalar
systemOnOff = _SystemOnOff_Object(
    (1, 3, 6, 1, 4, 1, 20677, 1, 6, 12),
    _SystemOnOff_Type()
)
systemOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOnOff.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Pulizzi",
    **{"pulizzi": pulizzi,
       "ipc3600": ipc3600,
       "unitConfig": unitConfig,
       "unitName": unitName,
       "unitTime": unitTime,
       "unitDate": unitDate,
       "unitDayOfWeek": unitDayOfWeek,
       "keyBoardTime": keyBoardTime,
       "networkSettings": networkSettings,
       "unitIPAddress": unitIPAddress,
       "subnetMask": subnetMask,
       "defaultGateway": defaultGateway,
       "webPort": webPort,
       "webEnabled": webEnabled,
       "macAddress": macAddress,
       "serialSettings": serialSettings,
       "baudRate": baudRate,
       "telnetSettings": telnetSettings,
       "telnetPort": telnetPort,
       "telnetEnabled": telnetEnabled,
       "outletMngt": outletMngt,
       "outletConfig": outletConfig,
       "outlet1": outlet1,
       "outlet1Name": outlet1Name,
       "outlet1Link": outlet1Link,
       "outlet1SequenceTime": outlet1SequenceTime,
       "outlet1RebootTime": outlet1RebootTime,
       "outlet2": outlet2,
       "outlet2Name": outlet2Name,
       "outlet2Link": outlet2Link,
       "outlet2SequenceTime": outlet2SequenceTime,
       "outlet2RebootTime": outlet2RebootTime,
       "outlet3": outlet3,
       "outlet3Name": outlet3Name,
       "outlet3Link": outlet3Link,
       "outlet3SequenceTime": outlet3SequenceTime,
       "outlet3RebootTime": outlet3RebootTime,
       "outlet4": outlet4,
       "outlet4Name": outlet4Name,
       "outlet4Link": outlet4Link,
       "outlet4SequenceTime": outlet4SequenceTime,
       "outlet4RebootTime": outlet4RebootTime,
       "outlet5": outlet5,
       "outlet5Name": outlet5Name,
       "outlet5Link": outlet5Link,
       "outlet5SequenceTime": outlet5SequenceTime,
       "outlet5RebootTime": outlet5RebootTime,
       "outlet6": outlet6,
       "outlet6Name": outlet6Name,
       "outlet6Link": outlet6Link,
       "outlet6SequenceTime": outlet6SequenceTime,
       "outlet6RebootTime": outlet6RebootTime,
       "outlet7": outlet7,
       "outlet7Name": outlet7Name,
       "outlet7Link": outlet7Link,
       "outlet7SequenceTime": outlet7SequenceTime,
       "outlet7RebootTime": outlet7RebootTime,
       "outlet8": outlet8,
       "outlet8Name": outlet8Name,
       "outlet8Link": outlet8Link,
       "outlet8SequenceTime": outlet8SequenceTime,
       "outlet8RebootTime": outlet8RebootTime,
       "outletControl": outletControl,
       "globalCommand": globalCommand,
       "outlet1Command": outlet1Command,
       "outlet2Command": outlet2Command,
       "outlet3Command": outlet3Command,
       "outlet4Command": outlet4Command,
       "outlet5Command": outlet5Command,
       "outlet6Command": outlet6Command,
       "outlet7Command": outlet7Command,
       "outlet8Command": outlet8Command,
       "outletStatus": outletStatus,
       "outlet1Status": outlet1Status,
       "outlet2Status": outlet2Status,
       "outlet3Status": outlet3Status,
       "outlet4Status": outlet4Status,
       "outlet5Status": outlet5Status,
       "outlet6Status": outlet6Status,
       "outlet7Status": outlet7Status,
       "outlet8Status": outlet8Status,
       "logManagerConfig": logManagerConfig,
       "mailServerIPAddress": mailServerIPAddress,
       "sendLogFrom": sendLogFrom,
       "sendLogToUser1Address": sendLogToUser1Address,
       "sendLogToUser2Address": sendLogToUser2Address,
       "sendAllertsToUser1Address": sendAllertsToUser1Address,
       "sendAllertsToUser2Address": sendAllertsToUser2Address,
       "sendLogFrequency": sendLogFrequency,
       "sendLogTime": sendLogTime,
       "userLogInLogOut": userLogInLogOut,
       "userLogInLogOutFailed": userLogInLogOutFailed,
       "outletActivity": outletActivity,
       "systemOnOff": systemOnOff}
)
