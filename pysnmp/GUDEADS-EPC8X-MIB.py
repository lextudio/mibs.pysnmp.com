# SNMP MIB module (GUDEADS-EPC8X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GUDEADS-EPC8X-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:19 2024
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

gudeads = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28507)
)
gudeads.setRevisions(
        ("2007-03-05 13:56",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsEPC8_ObjectIdentity = ObjectIdentity
gadsEPC8 = _GadsEPC8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 1)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0)
)
_Epc8Objects_ObjectIdentity = ObjectIdentity
epc8Objects = _Epc8Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1)
)
_Epc8SNMPaccess_ObjectIdentity = ObjectIdentity
epc8SNMPaccess = _Epc8SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 1)
)


class _Epc8TrapCtrl_Type(Integer32):
    """Custom type epc8TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Epc8TrapCtrl_Type.__name__ = "Integer32"
_Epc8TrapCtrl_Object = MibScalar
epc8TrapCtrl = _Epc8TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 1, 1),
    _Epc8TrapCtrl_Type()
)
epc8TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8TrapCtrl.setStatus("current")
_Epc8TrapIPTable_Object = MibTable
epc8TrapIPTable = _Epc8TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    epc8TrapIPTable.setStatus("current")
_Epc8TrapIPEntry_Object = MibTableRow
epc8TrapIPEntry = _Epc8TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 1, 2, 1)
)
epc8TrapIPEntry.setIndexNames(
    (0, "GUDEADS-EPC8X-MIB", "epc8TrapIPIndex"),
)
if mibBuilder.loadTexts:
    epc8TrapIPEntry.setStatus("current")


class _Epc8TrapIPIndex_Type(Integer32):
    """Custom type epc8TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc8TrapIPIndex_Type.__name__ = "Integer32"
_Epc8TrapIPIndex_Object = MibTableColumn
epc8TrapIPIndex = _Epc8TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 1, 2, 1, 1),
    _Epc8TrapIPIndex_Type()
)
epc8TrapIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    epc8TrapIPIndex.setStatus("current")


class _Epc8TrapIPAddr_Type(IpAddress):
    """Custom type epc8TrapIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_Epc8TrapIPAddr_Object = MibTableColumn
epc8TrapIPAddr = _Epc8TrapIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 1, 2, 1, 2),
    _Epc8TrapIPAddr_Type()
)
epc8TrapIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8TrapIPAddr.setStatus("current")


class _Epc8TrapIPPort_Type(Integer32):
    """Custom type epc8TrapIPPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Epc8TrapIPPort_Type.__name__ = "Integer32"
_Epc8TrapIPPort_Object = MibTableColumn
epc8TrapIPPort = _Epc8TrapIPPort_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 1, 2, 1, 3),
    _Epc8TrapIPPort_Type()
)
epc8TrapIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8TrapIPPort.setStatus("current")
_Epc8powerports_ObjectIdentity = ObjectIdentity
epc8powerports = _Epc8powerports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2)
)


class _Epc8portNumber_Type(Integer32):
    """Custom type epc8portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc8portNumber_Type.__name__ = "Integer32"
_Epc8portNumber_Object = MibScalar
epc8portNumber = _Epc8portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2, 1),
    _Epc8portNumber_Type()
)
epc8portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8portNumber.setStatus("current")
_Epc8portTable_Object = MibTable
epc8portTable = _Epc8portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    epc8portTable.setStatus("current")
_Epc8portEntry_Object = MibTableRow
epc8portEntry = _Epc8portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2, 2, 1)
)
epc8portEntry.setIndexNames(
    (0, "GUDEADS-EPC8X-MIB", "epc8PortIndex"),
)
if mibBuilder.loadTexts:
    epc8portEntry.setStatus("current")


class _Epc8PortIndex_Type(Integer32):
    """Custom type epc8PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc8PortIndex_Type.__name__ = "Integer32"
_Epc8PortIndex_Object = MibTableColumn
epc8PortIndex = _Epc8PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2, 2, 1, 1),
    _Epc8PortIndex_Type()
)
epc8PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    epc8PortIndex.setStatus("current")


class _Epc8PortName_Type(OctetString):
    """Custom type epc8PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Epc8PortName_Type.__name__ = "OctetString"
_Epc8PortName_Object = MibTableColumn
epc8PortName = _Epc8PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2, 2, 1, 2),
    _Epc8PortName_Type()
)
epc8PortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8PortName.setStatus("current")


class _Epc8PortState_Type(Integer32):
    """Custom type epc8PortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Epc8PortState_Type.__name__ = "Integer32"
_Epc8PortState_Object = MibTableColumn
epc8PortState = _Epc8PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2, 2, 1, 3),
    _Epc8PortState_Type()
)
epc8PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8PortState.setStatus("current")
_Epc8PortSwitchCount_Type = Counter32
_Epc8PortSwitchCount_Object = MibTableColumn
epc8PortSwitchCount = _Epc8PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2, 2, 1, 4),
    _Epc8PortSwitchCount_Type()
)
epc8PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8PortSwitchCount.setStatus("current")


class _Epc8PortStartupMode_Type(Integer32):
    """Custom type epc8PortStartupMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("laststate", 2),
          ("off", 0),
          ("on", 1))
    )


_Epc8PortStartupMode_Type.__name__ = "Integer32"
_Epc8PortStartupMode_Object = MibTableColumn
epc8PortStartupMode = _Epc8PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2, 2, 1, 5),
    _Epc8PortStartupMode_Type()
)
epc8PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8PortStartupMode.setStatus("current")


class _Epc8PortStartupDelay_Type(Integer32):
    """Custom type epc8PortStartupDelay based on Integer32"""
    defaultValue = 0


_Epc8PortStartupDelay_Object = MibTableColumn
epc8PortStartupDelay = _Epc8PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2, 2, 1, 6),
    _Epc8PortStartupDelay_Type()
)
epc8PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    epc8PortStartupDelay.setUnits("seconds")


class _Epc8PortRepowerTime_Type(Integer32):
    """Custom type epc8PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Epc8PortRepowerTime_Type.__name__ = "Integer32"
_Epc8PortRepowerTime_Object = MibTableColumn
epc8PortRepowerTime = _Epc8PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 2, 2, 1, 7),
    _Epc8PortRepowerTime_Type()
)
epc8PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc8PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    epc8PortRepowerTime.setUnits("seconds")
_Epc8Sensors_ObjectIdentity = ObjectIdentity
epc8Sensors = _Epc8Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 3)
)
_Epc8Irms_Type = Integer32
_Epc8Irms_Object = MibScalar
epc8Irms = _Epc8Irms_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 3, 1),
    _Epc8Irms_Type()
)
epc8Irms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8Irms.setStatus("current")
if mibBuilder.loadTexts:
    epc8Irms.setUnits("mA")
_Epc8SensorTable_Object = MibTable
epc8SensorTable = _Epc8SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    epc8SensorTable.setStatus("current")
_Epc8SensorEntry_Object = MibTableRow
epc8SensorEntry = _Epc8SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 3, 2, 1)
)
epc8SensorEntry.setIndexNames(
    (0, "GUDEADS-EPC8X-MIB", "epc8SensorIndex"),
)
if mibBuilder.loadTexts:
    epc8SensorEntry.setStatus("current")


class _Epc8SensorIndex_Type(Integer32):
    """Custom type epc8SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Epc8SensorIndex_Type.__name__ = "Integer32"
_Epc8SensorIndex_Object = MibTableColumn
epc8SensorIndex = _Epc8SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 3, 2, 1, 1),
    _Epc8SensorIndex_Type()
)
epc8SensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    epc8SensorIndex.setStatus("current")
_Epc8TempSensor_Type = Integer32
_Epc8TempSensor_Object = MibTableColumn
epc8TempSensor = _Epc8TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 3, 2, 1, 2),
    _Epc8TempSensor_Type()
)
epc8TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc8TempSensor.setUnits("10th of degree Celsius")
_Epc8HygroSensor_Type = Integer32
_Epc8HygroSensor_Object = MibTableColumn
epc8HygroSensor = _Epc8HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 1, 1, 3, 2, 1, 3),
    _Epc8HygroSensor_Type()
)
epc8HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc8HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    epc8HygroSensor.setUnits("10th of percentage humidity")
_Epc8Conf_ObjectIdentity = ObjectIdentity
epc8Conf = _Epc8Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 1, 3)
)
_Epc8Groups_ObjectIdentity = ObjectIdentity
epc8Groups = _Epc8Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 1, 3, 1)
)
_Epc8Compls_ObjectIdentity = ObjectIdentity
epc8Compls = _Epc8Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 1, 3, 2)
)

# Managed Objects groups

epc8BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 1, 3, 1, 1)
)
epc8BasicGroup.setObjects(
      *(("GUDEADS-EPC8X-MIB", "epc8portNumber"),
        ("GUDEADS-EPC8X-MIB", "epc8PortName"),
        ("GUDEADS-EPC8X-MIB", "epc8PortState"),
        ("GUDEADS-EPC8X-MIB", "epc8PortSwitchCount"),
        ("GUDEADS-EPC8X-MIB", "epc8TrapCtrl"),
        ("GUDEADS-EPC8X-MIB", "epc8TrapIPAddr"),
        ("GUDEADS-EPC8X-MIB", "epc8TrapIPPort"),
        ("GUDEADS-EPC8X-MIB", "epc8PortStartupMode"),
        ("GUDEADS-EPC8X-MIB", "epc8PortStartupDelay"),
        ("GUDEADS-EPC8X-MIB", "epc8PortRepowerTime"),
        ("GUDEADS-EPC8X-MIB", "epc8Irms"),
        ("GUDEADS-EPC8X-MIB", "epc8TempSensor"),
        ("GUDEADS-EPC8X-MIB", "epc8HygroSensor"))
)
if mibBuilder.loadTexts:
    epc8BasicGroup.setStatus("current")


# Notification objects

epcSwitchEvtPort1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 1)
)
epcSwitchEvtPort1.setObjects(
      *(("GUDEADS-EPC8X-MIB", "epc8PortName"),
        ("GUDEADS-EPC8X-MIB", "epc8PortState"),
        ("GUDEADS-EPC8X-MIB", "epc8PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epcSwitchEvtPort1.setStatus(
        "current"
    )

epcSwitchEvtPort2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 2)
)
epcSwitchEvtPort2.setObjects(
      *(("GUDEADS-EPC8X-MIB", "epc8PortName"),
        ("GUDEADS-EPC8X-MIB", "epc8PortState"),
        ("GUDEADS-EPC8X-MIB", "epc8PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epcSwitchEvtPort2.setStatus(
        "current"
    )

epcSwitchEvtPort3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 3)
)
epcSwitchEvtPort3.setObjects(
      *(("GUDEADS-EPC8X-MIB", "epc8PortName"),
        ("GUDEADS-EPC8X-MIB", "epc8PortState"),
        ("GUDEADS-EPC8X-MIB", "epc8PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epcSwitchEvtPort3.setStatus(
        "current"
    )

epcSwitchEvtPort4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 4)
)
epcSwitchEvtPort4.setObjects(
      *(("GUDEADS-EPC8X-MIB", "epc8PortName"),
        ("GUDEADS-EPC8X-MIB", "epc8PortState"),
        ("GUDEADS-EPC8X-MIB", "epc8PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epcSwitchEvtPort4.setStatus(
        "current"
    )

epcSwitchEvtPort5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 5)
)
epcSwitchEvtPort5.setObjects(
      *(("GUDEADS-EPC8X-MIB", "epc8PortName"),
        ("GUDEADS-EPC8X-MIB", "epc8PortState"),
        ("GUDEADS-EPC8X-MIB", "epc8PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epcSwitchEvtPort5.setStatus(
        "current"
    )

epcSwitchEvtPort6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 6)
)
epcSwitchEvtPort6.setObjects(
      *(("GUDEADS-EPC8X-MIB", "epc8PortName"),
        ("GUDEADS-EPC8X-MIB", "epc8PortState"),
        ("GUDEADS-EPC8X-MIB", "epc8PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epcSwitchEvtPort6.setStatus(
        "current"
    )

epcSwitchEvtPort7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 7)
)
epcSwitchEvtPort7.setObjects(
      *(("GUDEADS-EPC8X-MIB", "epc8PortName"),
        ("GUDEADS-EPC8X-MIB", "epc8PortState"),
        ("GUDEADS-EPC8X-MIB", "epc8PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epcSwitchEvtPort7.setStatus(
        "current"
    )

epcSwitchEvtPort8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 8)
)
epcSwitchEvtPort8.setObjects(
      *(("GUDEADS-EPC8X-MIB", "epc8PortName"),
        ("GUDEADS-EPC8X-MIB", "epc8PortState"),
        ("GUDEADS-EPC8X-MIB", "epc8PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epcSwitchEvtPort8.setStatus(
        "current"
    )

epc8TempEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 9)
)
epc8TempEvtSen1.setObjects(
    ("GUDEADS-EPC8X-MIB", "epc8TempSensor")
)
if mibBuilder.loadTexts:
    epc8TempEvtSen1.setStatus(
        "current"
    )

epc8TempEvtSen2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 10)
)
epc8TempEvtSen2.setObjects(
    ("GUDEADS-EPC8X-MIB", "epc8TempSensor")
)
if mibBuilder.loadTexts:
    epc8TempEvtSen2.setStatus(
        "current"
    )

epc8HygroEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 11)
)
epc8HygroEvtSen1.setObjects(
    ("GUDEADS-EPC8X-MIB", "epc8HygroSensor")
)
if mibBuilder.loadTexts:
    epc8HygroEvtSen1.setStatus(
        "current"
    )

epc8HygroEvtSen2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 1, 0, 12)
)
epc8HygroEvtSen2.setObjects(
    ("GUDEADS-EPC8X-MIB", "epc8HygroSensor")
)
if mibBuilder.loadTexts:
    epc8HygroEvtSen2.setStatus(
        "current"
    )


# Notifications groups

epc8NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 1, 3, 1, 2)
)
epc8NotificationGroup.setObjects(
      *(("GUDEADS-EPC8X-MIB", "epcSwitchEvtPort1"),
        ("GUDEADS-EPC8X-MIB", "epcSwitchEvtPort2"),
        ("GUDEADS-EPC8X-MIB", "epcSwitchEvtPort3"),
        ("GUDEADS-EPC8X-MIB", "epcSwitchEvtPort4"),
        ("GUDEADS-EPC8X-MIB", "epcSwitchEvtPort5"),
        ("GUDEADS-EPC8X-MIB", "epcSwitchEvtPort6"),
        ("GUDEADS-EPC8X-MIB", "epcSwitchEvtPort7"),
        ("GUDEADS-EPC8X-MIB", "epcSwitchEvtPort8"),
        ("GUDEADS-EPC8X-MIB", "epc8TempEvtSen1"),
        ("GUDEADS-EPC8X-MIB", "epc8HygroEvtSen1"),
        ("GUDEADS-EPC8X-MIB", "epc8TempEvtSen2"),
        ("GUDEADS-EPC8X-MIB", "epc8HygroEvtSen2"))
)
if mibBuilder.loadTexts:
    epc8NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EPC8X-MIB",
    **{"gudeads": gudeads,
       "gadsEPC8": gadsEPC8,
       "events": events,
       "epcSwitchEvtPort1": epcSwitchEvtPort1,
       "epcSwitchEvtPort2": epcSwitchEvtPort2,
       "epcSwitchEvtPort3": epcSwitchEvtPort3,
       "epcSwitchEvtPort4": epcSwitchEvtPort4,
       "epcSwitchEvtPort5": epcSwitchEvtPort5,
       "epcSwitchEvtPort6": epcSwitchEvtPort6,
       "epcSwitchEvtPort7": epcSwitchEvtPort7,
       "epcSwitchEvtPort8": epcSwitchEvtPort8,
       "epc8TempEvtSen1": epc8TempEvtSen1,
       "epc8TempEvtSen2": epc8TempEvtSen2,
       "epc8HygroEvtSen1": epc8HygroEvtSen1,
       "epc8HygroEvtSen2": epc8HygroEvtSen2,
       "epc8Objects": epc8Objects,
       "epc8SNMPaccess": epc8SNMPaccess,
       "epc8TrapCtrl": epc8TrapCtrl,
       "epc8TrapIPTable": epc8TrapIPTable,
       "epc8TrapIPEntry": epc8TrapIPEntry,
       "epc8TrapIPIndex": epc8TrapIPIndex,
       "epc8TrapIPAddr": epc8TrapIPAddr,
       "epc8TrapIPPort": epc8TrapIPPort,
       "epc8powerports": epc8powerports,
       "epc8portNumber": epc8portNumber,
       "epc8portTable": epc8portTable,
       "epc8portEntry": epc8portEntry,
       "epc8PortIndex": epc8PortIndex,
       "epc8PortName": epc8PortName,
       "epc8PortState": epc8PortState,
       "epc8PortSwitchCount": epc8PortSwitchCount,
       "epc8PortStartupMode": epc8PortStartupMode,
       "epc8PortStartupDelay": epc8PortStartupDelay,
       "epc8PortRepowerTime": epc8PortRepowerTime,
       "epc8Sensors": epc8Sensors,
       "epc8Irms": epc8Irms,
       "epc8SensorTable": epc8SensorTable,
       "epc8SensorEntry": epc8SensorEntry,
       "epc8SensorIndex": epc8SensorIndex,
       "epc8TempSensor": epc8TempSensor,
       "epc8HygroSensor": epc8HygroSensor,
       "epc8Conf": epc8Conf,
       "epc8Groups": epc8Groups,
       "epc8BasicGroup": epc8BasicGroup,
       "epc8NotificationGroup": epc8NotificationGroup,
       "epc8Compls": epc8Compls}
)
