# SNMP MIB module (GUDEADS-PDU8310-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GUDEADS-PDU8310-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:20 2024
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

_GadsPDU8310_ObjectIdentity = ObjectIdentity
gadsPDU8310 = _GadsPDU8310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 0)
)
_Pdu8310Objects_ObjectIdentity = ObjectIdentity
pdu8310Objects = _Pdu8310Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1)
)
_Pdu8310CommonConfig_ObjectIdentity = ObjectIdentity
pdu8310CommonConfig = _Pdu8310CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 1)
)
_Pdu8310SNMPaccess_ObjectIdentity = ObjectIdentity
pdu8310SNMPaccess = _Pdu8310SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 1, 1)
)


class _Pdu8310TrapCtrl_Type(Integer32):
    """Custom type pdu8310TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Pdu8310TrapCtrl_Type.__name__ = "Integer32"
_Pdu8310TrapCtrl_Object = MibScalar
pdu8310TrapCtrl = _Pdu8310TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 1, 1, 1),
    _Pdu8310TrapCtrl_Type()
)
pdu8310TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8310TrapCtrl.setStatus("current")
_Pdu8310TrapIPTable_Object = MibTable
pdu8310TrapIPTable = _Pdu8310TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8310TrapIPTable.setStatus("current")
_Pdu8310TrapIPEntry_Object = MibTableRow
pdu8310TrapIPEntry = _Pdu8310TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 1, 1, 2, 1)
)
pdu8310TrapIPEntry.setIndexNames(
    (0, "GUDEADS-PDU8310-MIB", "pdu8310TrapIPIndex"),
)
if mibBuilder.loadTexts:
    pdu8310TrapIPEntry.setStatus("current")


class _Pdu8310TrapIPIndex_Type(Integer32):
    """Custom type pdu8310TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Pdu8310TrapIPIndex_Type.__name__ = "Integer32"
_Pdu8310TrapIPIndex_Object = MibTableColumn
pdu8310TrapIPIndex = _Pdu8310TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 1, 1, 2, 1, 1),
    _Pdu8310TrapIPIndex_Type()
)
pdu8310TrapIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu8310TrapIPIndex.setStatus("current")


class _Pdu8310TrapAddr_Type(OctetString):
    """Custom type pdu8310TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Pdu8310TrapAddr_Type.__name__ = "OctetString"
_Pdu8310TrapAddr_Object = MibTableColumn
pdu8310TrapAddr = _Pdu8310TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 1, 1, 2, 1, 2),
    _Pdu8310TrapAddr_Type()
)
pdu8310TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8310TrapAddr.setStatus("current")
_Pdu8310DeviceConfig_ObjectIdentity = ObjectIdentity
pdu8310DeviceConfig = _Pdu8310DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 2)
)
_Pdu8310IntActors_ObjectIdentity = ObjectIdentity
pdu8310IntActors = _Pdu8310IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 3)
)
_Pdu8310ExtActors_ObjectIdentity = ObjectIdentity
pdu8310ExtActors = _Pdu8310ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 4)
)
_Pdu8310IntSensors_ObjectIdentity = ObjectIdentity
pdu8310IntSensors = _Pdu8310IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5)
)
_Pdu8310PowerChan_ObjectIdentity = ObjectIdentity
pdu8310PowerChan = _Pdu8310PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1)
)


class _Pdu8310ActivePowerChan_Type(Unsigned32):
    """Custom type pdu8310ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Pdu8310ActivePowerChan_Type.__name__ = "Unsigned32"
_Pdu8310ActivePowerChan_Object = MibScalar
pdu8310ActivePowerChan = _Pdu8310ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 1),
    _Pdu8310ActivePowerChan_Type()
)
pdu8310ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310ActivePowerChan.setStatus("current")
_Pdu8310PowerTable_Object = MibTable
pdu8310PowerTable = _Pdu8310PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8310PowerTable.setStatus("current")
_Pdu8310PowerEntry_Object = MibTableRow
pdu8310PowerEntry = _Pdu8310PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1)
)
pdu8310PowerEntry.setIndexNames(
    (0, "GUDEADS-PDU8310-MIB", "pdu8310PowerIndex"),
)
if mibBuilder.loadTexts:
    pdu8310PowerEntry.setStatus("current")


class _Pdu8310PowerIndex_Type(Integer32):
    """Custom type pdu8310PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Pdu8310PowerIndex_Type.__name__ = "Integer32"
_Pdu8310PowerIndex_Object = MibTableColumn
pdu8310PowerIndex = _Pdu8310PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 1),
    _Pdu8310PowerIndex_Type()
)
pdu8310PowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu8310PowerIndex.setStatus("current")


class _Pdu8310ChanStatus_Type(Integer32):
    """Custom type pdu8310ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu8310ChanStatus_Type.__name__ = "Integer32"
_Pdu8310ChanStatus_Object = MibTableColumn
pdu8310ChanStatus = _Pdu8310ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 2),
    _Pdu8310ChanStatus_Type()
)
pdu8310ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310ChanStatus.setStatus("current")
_Pdu8310EnergyActive_Type = Unsigned32
_Pdu8310EnergyActive_Object = MibTableColumn
pdu8310EnergyActive = _Pdu8310EnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 3),
    _Pdu8310EnergyActive_Type()
)
pdu8310EnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310EnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310EnergyActive.setUnits("Wh")
_Pdu8310PowerActive_Type = Unsigned32
_Pdu8310PowerActive_Object = MibTableColumn
pdu8310PowerActive = _Pdu8310PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 4),
    _Pdu8310PowerActive_Type()
)
pdu8310PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310PowerActive.setUnits("W")
_Pdu8310Current_Type = Unsigned32
_Pdu8310Current_Object = MibTableColumn
pdu8310Current = _Pdu8310Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 5),
    _Pdu8310Current_Type()
)
pdu8310Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310Current.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310Current.setUnits("mA")
_Pdu8310Voltage_Type = Unsigned32
_Pdu8310Voltage_Object = MibTableColumn
pdu8310Voltage = _Pdu8310Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 6),
    _Pdu8310Voltage_Type()
)
pdu8310Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310Voltage.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310Voltage.setUnits("V")
_Pdu8310Frequency_Type = Unsigned32
_Pdu8310Frequency_Object = MibTableColumn
pdu8310Frequency = _Pdu8310Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 7),
    _Pdu8310Frequency_Type()
)
pdu8310Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310Frequency.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310Frequency.setUnits("0.01 hz")
_Pdu8310PowerFactor_Type = Integer32
_Pdu8310PowerFactor_Object = MibTableColumn
pdu8310PowerFactor = _Pdu8310PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 8),
    _Pdu8310PowerFactor_Type()
)
pdu8310PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310PowerFactor.setUnits("0.001")
_Pdu8310Pangle_Type = Integer32
_Pdu8310Pangle_Object = MibTableColumn
pdu8310Pangle = _Pdu8310Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 9),
    _Pdu8310Pangle_Type()
)
pdu8310Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310Pangle.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310Pangle.setUnits("0.1 degree")
_Pdu8310PowerApparent_Type = Unsigned32
_Pdu8310PowerApparent_Object = MibTableColumn
pdu8310PowerApparent = _Pdu8310PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 10),
    _Pdu8310PowerApparent_Type()
)
pdu8310PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310PowerApparent.setUnits("VA")
_Pdu8310PowerReactive_Type = Unsigned32
_Pdu8310PowerReactive_Object = MibTableColumn
pdu8310PowerReactive = _Pdu8310PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 11),
    _Pdu8310PowerReactive_Type()
)
pdu8310PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310PowerReactive.setUnits("VAR")
_Pdu8310EnergyReactive_Type = Unsigned32
_Pdu8310EnergyReactive_Object = MibTableColumn
pdu8310EnergyReactive = _Pdu8310EnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 12),
    _Pdu8310EnergyReactive_Type()
)
pdu8310EnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310EnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310EnergyReactive.setUnits("VARh")
_Pdu8310EnergyActiveResettable_Type = Unsigned32
_Pdu8310EnergyActiveResettable_Object = MibTableColumn
pdu8310EnergyActiveResettable = _Pdu8310EnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 13),
    _Pdu8310EnergyActiveResettable_Type()
)
pdu8310EnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310EnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310EnergyActiveResettable.setUnits("Wh")
_Pdu8310EnergyReactiveResettable_Type = Unsigned32
_Pdu8310EnergyReactiveResettable_Object = MibTableColumn
pdu8310EnergyReactiveResettable = _Pdu8310EnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 14),
    _Pdu8310EnergyReactiveResettable_Type()
)
pdu8310EnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310EnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310EnergyReactiveResettable.setUnits("VARh")
_Pdu8310ResetTime_Type = Unsigned32
_Pdu8310ResetTime_Object = MibTableColumn
pdu8310ResetTime = _Pdu8310ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 5, 1, 2, 1, 15),
    _Pdu8310ResetTime_Type()
)
pdu8310ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8310ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    pdu8310ResetTime.setUnits("s")
_Pdu8310ExtSensors_ObjectIdentity = ObjectIdentity
pdu8310ExtSensors = _Pdu8310ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 1, 6)
)
_Pdu8310Conf_ObjectIdentity = ObjectIdentity
pdu8310Conf = _Pdu8310Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 2)
)
_Pdu8310Groups_ObjectIdentity = ObjectIdentity
pdu8310Groups = _Pdu8310Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 2, 1)
)
_Pdu8310Compls_ObjectIdentity = ObjectIdentity
pdu8310Compls = _Pdu8310Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 27, 2, 2)
)

# Managed Objects groups

pdu8310BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 27, 2, 1, 1)
)
pdu8310BasicGroup.setObjects(
      *(("GUDEADS-PDU8310-MIB", "pdu8310TrapCtrl"),
        ("GUDEADS-PDU8310-MIB", "pdu8310TrapAddr"),
        ("GUDEADS-PDU8310-MIB", "pdu8310ActivePowerChan"),
        ("GUDEADS-PDU8310-MIB", "pdu8310ChanStatus"),
        ("GUDEADS-PDU8310-MIB", "pdu8310EnergyActive"),
        ("GUDEADS-PDU8310-MIB", "pdu8310PowerActive"),
        ("GUDEADS-PDU8310-MIB", "pdu8310Current"),
        ("GUDEADS-PDU8310-MIB", "pdu8310Voltage"),
        ("GUDEADS-PDU8310-MIB", "pdu8310Frequency"),
        ("GUDEADS-PDU8310-MIB", "pdu8310PowerFactor"),
        ("GUDEADS-PDU8310-MIB", "pdu8310Pangle"),
        ("GUDEADS-PDU8310-MIB", "pdu8310PowerApparent"),
        ("GUDEADS-PDU8310-MIB", "pdu8310PowerReactive"),
        ("GUDEADS-PDU8310-MIB", "pdu8310EnergyReactive"),
        ("GUDEADS-PDU8310-MIB", "pdu8310EnergyActiveResettable"),
        ("GUDEADS-PDU8310-MIB", "pdu8310EnergyReactiveResettable"),
        ("GUDEADS-PDU8310-MIB", "pdu8310ResetTime"))
)
if mibBuilder.loadTexts:
    pdu8310BasicGroup.setStatus("current")


# Notification objects

pdu8310AmperageEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 27, 0, 1)
)
pdu8310AmperageEvt1.setObjects(
      *(("GUDEADS-PDU8310-MIB", "pdu8310PowerActive"),
        ("GUDEADS-PDU8310-MIB", "pdu8310Current"),
        ("GUDEADS-PDU8310-MIB", "pdu8310Voltage"),
        ("GUDEADS-PDU8310-MIB", "pdu8310Frequency"),
        ("GUDEADS-PDU8310-MIB", "pdu8310PowerApparent"),
        ("GUDEADS-PDU8310-MIB", "pdu8310PowerReactive"))
)
if mibBuilder.loadTexts:
    pdu8310AmperageEvt1.setStatus(
        "current"
    )


# Notifications groups

pdu8310NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 27, 2, 1, 2)
)
pdu8310NotificationGroup.setObjects(
    ("GUDEADS-PDU8310-MIB", "pdu8310AmperageEvt1")
)
if mibBuilder.loadTexts:
    pdu8310NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-PDU8310-MIB",
    **{"gudeads": gudeads,
       "gadsPDU8310": gadsPDU8310,
       "events": events,
       "pdu8310AmperageEvt1": pdu8310AmperageEvt1,
       "pdu8310Objects": pdu8310Objects,
       "pdu8310CommonConfig": pdu8310CommonConfig,
       "pdu8310SNMPaccess": pdu8310SNMPaccess,
       "pdu8310TrapCtrl": pdu8310TrapCtrl,
       "pdu8310TrapIPTable": pdu8310TrapIPTable,
       "pdu8310TrapIPEntry": pdu8310TrapIPEntry,
       "pdu8310TrapIPIndex": pdu8310TrapIPIndex,
       "pdu8310TrapAddr": pdu8310TrapAddr,
       "pdu8310DeviceConfig": pdu8310DeviceConfig,
       "pdu8310IntActors": pdu8310IntActors,
       "pdu8310ExtActors": pdu8310ExtActors,
       "pdu8310IntSensors": pdu8310IntSensors,
       "pdu8310PowerChan": pdu8310PowerChan,
       "pdu8310ActivePowerChan": pdu8310ActivePowerChan,
       "pdu8310PowerTable": pdu8310PowerTable,
       "pdu8310PowerEntry": pdu8310PowerEntry,
       "pdu8310PowerIndex": pdu8310PowerIndex,
       "pdu8310ChanStatus": pdu8310ChanStatus,
       "pdu8310EnergyActive": pdu8310EnergyActive,
       "pdu8310PowerActive": pdu8310PowerActive,
       "pdu8310Current": pdu8310Current,
       "pdu8310Voltage": pdu8310Voltage,
       "pdu8310Frequency": pdu8310Frequency,
       "pdu8310PowerFactor": pdu8310PowerFactor,
       "pdu8310Pangle": pdu8310Pangle,
       "pdu8310PowerApparent": pdu8310PowerApparent,
       "pdu8310PowerReactive": pdu8310PowerReactive,
       "pdu8310EnergyReactive": pdu8310EnergyReactive,
       "pdu8310EnergyActiveResettable": pdu8310EnergyActiveResettable,
       "pdu8310EnergyReactiveResettable": pdu8310EnergyReactiveResettable,
       "pdu8310ResetTime": pdu8310ResetTime,
       "pdu8310ExtSensors": pdu8310ExtSensors,
       "pdu8310Conf": pdu8310Conf,
       "pdu8310Groups": pdu8310Groups,
       "pdu8310BasicGroup": pdu8310BasicGroup,
       "pdu8310NotificationGroup": pdu8310NotificationGroup,
       "pdu8310Compls": pdu8310Compls}
)
