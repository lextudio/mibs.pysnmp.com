# SNMP MIB module (GUDEADS-PDU8110-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GUDEADS-PDU8110-MIB
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

_GadsPDU8110_ObjectIdentity = ObjectIdentity
gadsPDU8110 = _GadsPDU8110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 0)
)
_Pdu8110Objects_ObjectIdentity = ObjectIdentity
pdu8110Objects = _Pdu8110Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1)
)
_Pdu8110CommonConfig_ObjectIdentity = ObjectIdentity
pdu8110CommonConfig = _Pdu8110CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 1)
)
_Pdu8110SNMPaccess_ObjectIdentity = ObjectIdentity
pdu8110SNMPaccess = _Pdu8110SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1)
)


class _Pdu8110TrapCtrl_Type(Integer32):
    """Custom type pdu8110TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Pdu8110TrapCtrl_Type.__name__ = "Integer32"
_Pdu8110TrapCtrl_Object = MibScalar
pdu8110TrapCtrl = _Pdu8110TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1, 1),
    _Pdu8110TrapCtrl_Type()
)
pdu8110TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8110TrapCtrl.setStatus("current")
_Pdu8110TrapIPTable_Object = MibTable
pdu8110TrapIPTable = _Pdu8110TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8110TrapIPTable.setStatus("current")
_Pdu8110TrapIPEntry_Object = MibTableRow
pdu8110TrapIPEntry = _Pdu8110TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1, 2, 1)
)
pdu8110TrapIPEntry.setIndexNames(
    (0, "GUDEADS-PDU8110-MIB", "pdu8110TrapIPIndex"),
)
if mibBuilder.loadTexts:
    pdu8110TrapIPEntry.setStatus("current")


class _Pdu8110TrapIPIndex_Type(Integer32):
    """Custom type pdu8110TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Pdu8110TrapIPIndex_Type.__name__ = "Integer32"
_Pdu8110TrapIPIndex_Object = MibTableColumn
pdu8110TrapIPIndex = _Pdu8110TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1, 2, 1, 1),
    _Pdu8110TrapIPIndex_Type()
)
pdu8110TrapIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu8110TrapIPIndex.setStatus("current")


class _Pdu8110TrapAddr_Type(OctetString):
    """Custom type pdu8110TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Pdu8110TrapAddr_Type.__name__ = "OctetString"
_Pdu8110TrapAddr_Object = MibTableColumn
pdu8110TrapAddr = _Pdu8110TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 1, 1, 2, 1, 2),
    _Pdu8110TrapAddr_Type()
)
pdu8110TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8110TrapAddr.setStatus("current")
_Pdu8110DeviceConfig_ObjectIdentity = ObjectIdentity
pdu8110DeviceConfig = _Pdu8110DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 2)
)
_Pdu8110IntActors_ObjectIdentity = ObjectIdentity
pdu8110IntActors = _Pdu8110IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 3)
)
_Pdu8110ExtActors_ObjectIdentity = ObjectIdentity
pdu8110ExtActors = _Pdu8110ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 4)
)
_Pdu8110IntSensors_ObjectIdentity = ObjectIdentity
pdu8110IntSensors = _Pdu8110IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 5)
)
_Pdu8110PowerChan_ObjectIdentity = ObjectIdentity
pdu8110PowerChan = _Pdu8110PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1)
)


class _Pdu8110ActivePowerChan_Type(Unsigned32):
    """Custom type pdu8110ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu8110ActivePowerChan_Type.__name__ = "Unsigned32"
_Pdu8110ActivePowerChan_Object = MibScalar
pdu8110ActivePowerChan = _Pdu8110ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 1),
    _Pdu8110ActivePowerChan_Type()
)
pdu8110ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8110ActivePowerChan.setStatus("current")
_Pdu8110PowerTable_Object = MibTable
pdu8110PowerTable = _Pdu8110PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8110PowerTable.setStatus("current")
_Pdu8110PowerEntry_Object = MibTableRow
pdu8110PowerEntry = _Pdu8110PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 2, 1)
)
pdu8110PowerEntry.setIndexNames(
    (0, "GUDEADS-PDU8110-MIB", "pdu8110PowerIndex"),
)
if mibBuilder.loadTexts:
    pdu8110PowerEntry.setStatus("current")


class _Pdu8110PowerIndex_Type(Integer32):
    """Custom type pdu8110PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Pdu8110PowerIndex_Type.__name__ = "Integer32"
_Pdu8110PowerIndex_Object = MibTableColumn
pdu8110PowerIndex = _Pdu8110PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 2, 1, 1),
    _Pdu8110PowerIndex_Type()
)
pdu8110PowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu8110PowerIndex.setStatus("current")


class _Pdu8110ChanStatus_Type(Integer32):
    """Custom type pdu8110ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu8110ChanStatus_Type.__name__ = "Integer32"
_Pdu8110ChanStatus_Object = MibTableColumn
pdu8110ChanStatus = _Pdu8110ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 2, 1, 2),
    _Pdu8110ChanStatus_Type()
)
pdu8110ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8110ChanStatus.setStatus("current")
_Pdu8110Current_Type = Unsigned32
_Pdu8110Current_Object = MibTableColumn
pdu8110Current = _Pdu8110Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 5, 1, 2, 1, 5),
    _Pdu8110Current_Type()
)
pdu8110Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8110Current.setStatus("current")
if mibBuilder.loadTexts:
    pdu8110Current.setUnits("mA")
_Pdu8110ExtSensors_ObjectIdentity = ObjectIdentity
pdu8110ExtSensors = _Pdu8110ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 6)
)
_Pdu8110SensorTable_Object = MibTable
pdu8110SensorTable = _Pdu8110SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 6, 1)
)
if mibBuilder.loadTexts:
    pdu8110SensorTable.setStatus("current")
_Pdu8110SensorEntry_Object = MibTableRow
pdu8110SensorEntry = _Pdu8110SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 6, 1, 1)
)
pdu8110SensorEntry.setIndexNames(
    (0, "GUDEADS-PDU8110-MIB", "pdu8110SensorIndex"),
)
if mibBuilder.loadTexts:
    pdu8110SensorEntry.setStatus("current")


class _Pdu8110SensorIndex_Type(Integer32):
    """Custom type pdu8110SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu8110SensorIndex_Type.__name__ = "Integer32"
_Pdu8110SensorIndex_Object = MibTableColumn
pdu8110SensorIndex = _Pdu8110SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 6, 1, 1, 1),
    _Pdu8110SensorIndex_Type()
)
pdu8110SensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu8110SensorIndex.setStatus("current")
_Pdu8110TempSensor_Type = Integer32
_Pdu8110TempSensor_Object = MibTableColumn
pdu8110TempSensor = _Pdu8110TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 6, 1, 1, 2),
    _Pdu8110TempSensor_Type()
)
pdu8110TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8110TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8110TempSensor.setUnits("0.1 degree Celsius")
_Pdu8110HygroSensor_Type = Integer32
_Pdu8110HygroSensor_Object = MibTableColumn
pdu8110HygroSensor = _Pdu8110HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 23, 1, 6, 1, 1, 3),
    _Pdu8110HygroSensor_Type()
)
pdu8110HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8110HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8110HygroSensor.setUnits("0.1 percent humidity")
_Pdu8110Conf_ObjectIdentity = ObjectIdentity
pdu8110Conf = _Pdu8110Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 2)
)
_Pdu8110Groups_ObjectIdentity = ObjectIdentity
pdu8110Groups = _Pdu8110Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 2, 1)
)
_Pdu8110Compls_ObjectIdentity = ObjectIdentity
pdu8110Compls = _Pdu8110Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 23, 2, 2)
)

# Managed Objects groups

pdu8110BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 23, 2, 1, 1)
)
pdu8110BasicGroup.setObjects(
      *(("GUDEADS-PDU8110-MIB", "pdu8110TrapCtrl"),
        ("GUDEADS-PDU8110-MIB", "pdu8110TrapAddr"),
        ("GUDEADS-PDU8110-MIB", "pdu8110ActivePowerChan"),
        ("GUDEADS-PDU8110-MIB", "pdu8110ChanStatus"),
        ("GUDEADS-PDU8110-MIB", "pdu8110Current"),
        ("GUDEADS-PDU8110-MIB", "pdu8110TempSensor"),
        ("GUDEADS-PDU8110-MIB", "pdu8110HygroSensor"))
)
if mibBuilder.loadTexts:
    pdu8110BasicGroup.setStatus("current")


# Notification objects

pdu8110TempEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 23, 0, 1)
)
pdu8110TempEvtSen1.setObjects(
    ("GUDEADS-PDU8110-MIB", "pdu8110TempSensor")
)
if mibBuilder.loadTexts:
    pdu8110TempEvtSen1.setStatus(
        "current"
    )

pdu8110TempEvtSen2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 23, 0, 2)
)
pdu8110TempEvtSen2.setObjects(
    ("GUDEADS-PDU8110-MIB", "pdu8110TempSensor")
)
if mibBuilder.loadTexts:
    pdu8110TempEvtSen2.setStatus(
        "current"
    )

pdu8110HygroEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 23, 0, 3)
)
pdu8110HygroEvtSen1.setObjects(
    ("GUDEADS-PDU8110-MIB", "pdu8110HygroSensor")
)
if mibBuilder.loadTexts:
    pdu8110HygroEvtSen1.setStatus(
        "current"
    )

pdu8110HygroEvtSen2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 23, 0, 4)
)
pdu8110HygroEvtSen2.setObjects(
    ("GUDEADS-PDU8110-MIB", "pdu8110HygroSensor")
)
if mibBuilder.loadTexts:
    pdu8110HygroEvtSen2.setStatus(
        "current"
    )


# Notifications groups

pdu8110NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 23, 2, 1, 2)
)
pdu8110NotificationGroup.setObjects(
      *(("GUDEADS-PDU8110-MIB", "pdu8110TempEvtSen1"),
        ("GUDEADS-PDU8110-MIB", "pdu8110TempEvtSen2"),
        ("GUDEADS-PDU8110-MIB", "pdu8110HygroEvtSen1"),
        ("GUDEADS-PDU8110-MIB", "pdu8110HygroEvtSen2"))
)
if mibBuilder.loadTexts:
    pdu8110NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-PDU8110-MIB",
    **{"gudeads": gudeads,
       "gadsPDU8110": gadsPDU8110,
       "events": events,
       "pdu8110TempEvtSen1": pdu8110TempEvtSen1,
       "pdu8110TempEvtSen2": pdu8110TempEvtSen2,
       "pdu8110HygroEvtSen1": pdu8110HygroEvtSen1,
       "pdu8110HygroEvtSen2": pdu8110HygroEvtSen2,
       "pdu8110Objects": pdu8110Objects,
       "pdu8110CommonConfig": pdu8110CommonConfig,
       "pdu8110SNMPaccess": pdu8110SNMPaccess,
       "pdu8110TrapCtrl": pdu8110TrapCtrl,
       "pdu8110TrapIPTable": pdu8110TrapIPTable,
       "pdu8110TrapIPEntry": pdu8110TrapIPEntry,
       "pdu8110TrapIPIndex": pdu8110TrapIPIndex,
       "pdu8110TrapAddr": pdu8110TrapAddr,
       "pdu8110DeviceConfig": pdu8110DeviceConfig,
       "pdu8110IntActors": pdu8110IntActors,
       "pdu8110ExtActors": pdu8110ExtActors,
       "pdu8110IntSensors": pdu8110IntSensors,
       "pdu8110PowerChan": pdu8110PowerChan,
       "pdu8110ActivePowerChan": pdu8110ActivePowerChan,
       "pdu8110PowerTable": pdu8110PowerTable,
       "pdu8110PowerEntry": pdu8110PowerEntry,
       "pdu8110PowerIndex": pdu8110PowerIndex,
       "pdu8110ChanStatus": pdu8110ChanStatus,
       "pdu8110Current": pdu8110Current,
       "pdu8110ExtSensors": pdu8110ExtSensors,
       "pdu8110SensorTable": pdu8110SensorTable,
       "pdu8110SensorEntry": pdu8110SensorEntry,
       "pdu8110SensorIndex": pdu8110SensorIndex,
       "pdu8110TempSensor": pdu8110TempSensor,
       "pdu8110HygroSensor": pdu8110HygroSensor,
       "pdu8110Conf": pdu8110Conf,
       "pdu8110Groups": pdu8110Groups,
       "pdu8110BasicGroup": pdu8110BasicGroup,
       "pdu8110NotificationGroup": pdu8110NotificationGroup,
       "pdu8110Compls": pdu8110Compls}
)
