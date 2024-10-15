# SNMP MIB module (GUDEADS-EPC2X6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GUDEADS-EPC2X6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:18 2024
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

_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 0)
)
_GadsEPC2x6_ObjectIdentity = ObjectIdentity
gadsEPC2x6 = _GadsEPC2x6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 6)
)
_Epc2x6Objects_ObjectIdentity = ObjectIdentity
epc2x6Objects = _Epc2x6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1)
)
_Epc2x6SNMPaccess_ObjectIdentity = ObjectIdentity
epc2x6SNMPaccess = _Epc2x6SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 1)
)


class _Epc2x6TrapCtrl_Type(Integer32):
    """Custom type epc2x6TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Epc2x6TrapCtrl_Type.__name__ = "Integer32"
_Epc2x6TrapCtrl_Object = MibScalar
epc2x6TrapCtrl = _Epc2x6TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 1, 1),
    _Epc2x6TrapCtrl_Type()
)
epc2x6TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc2x6TrapCtrl.setStatus("current")
_Epc2x6TrapIPTable_Object = MibTable
epc2x6TrapIPTable = _Epc2x6TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    epc2x6TrapIPTable.setStatus("current")
_Epc2x6TrapIPEntry_Object = MibTableRow
epc2x6TrapIPEntry = _Epc2x6TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 1, 2, 1)
)
epc2x6TrapIPEntry.setIndexNames(
    (0, "GUDEADS-EPC2X6-MIB", "epc2x6TrapIPIndex"),
)
if mibBuilder.loadTexts:
    epc2x6TrapIPEntry.setStatus("current")


class _Epc2x6TrapIPIndex_Type(Integer32):
    """Custom type epc2x6TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Epc2x6TrapIPIndex_Type.__name__ = "Integer32"
_Epc2x6TrapIPIndex_Object = MibTableColumn
epc2x6TrapIPIndex = _Epc2x6TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 1, 2, 1, 1),
    _Epc2x6TrapIPIndex_Type()
)
epc2x6TrapIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    epc2x6TrapIPIndex.setStatus("current")


class _Epc2x6TrapIPAddr_Type(IpAddress):
    """Custom type epc2x6TrapIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_Epc2x6TrapIPAddr_Object = MibTableColumn
epc2x6TrapIPAddr = _Epc2x6TrapIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 1, 2, 1, 2),
    _Epc2x6TrapIPAddr_Type()
)
epc2x6TrapIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc2x6TrapIPAddr.setStatus("current")


class _Epc2x6TrapIPPort_Type(Integer32):
    """Custom type epc2x6TrapIPPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_Epc2x6TrapIPPort_Type.__name__ = "Integer32"
_Epc2x6TrapIPPort_Object = MibTableColumn
epc2x6TrapIPPort = _Epc2x6TrapIPPort_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 1, 2, 1, 3),
    _Epc2x6TrapIPPort_Type()
)
epc2x6TrapIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc2x6TrapIPPort.setStatus("current")
_Epc2x6powerports_ObjectIdentity = ObjectIdentity
epc2x6powerports = _Epc2x6powerports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2)
)


class _Epc2x6portNumber_Type(Integer32):
    """Custom type epc2x6portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Epc2x6portNumber_Type.__name__ = "Integer32"
_Epc2x6portNumber_Object = MibScalar
epc2x6portNumber = _Epc2x6portNumber_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 1),
    _Epc2x6portNumber_Type()
)
epc2x6portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc2x6portNumber.setStatus("current")
_Epc2x6portTable_Object = MibTable
epc2x6portTable = _Epc2x6portTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    epc2x6portTable.setStatus("current")
_Epc2x6portEntry_Object = MibTableRow
epc2x6portEntry = _Epc2x6portEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 2, 1)
)
epc2x6portEntry.setIndexNames(
    (0, "GUDEADS-EPC2X6-MIB", "epc2x6PortIndex"),
)
if mibBuilder.loadTexts:
    epc2x6portEntry.setStatus("current")


class _Epc2x6PortIndex_Type(Integer32):
    """Custom type epc2x6PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Epc2x6PortIndex_Type.__name__ = "Integer32"
_Epc2x6PortIndex_Object = MibTableColumn
epc2x6PortIndex = _Epc2x6PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 2, 1, 1),
    _Epc2x6PortIndex_Type()
)
epc2x6PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    epc2x6PortIndex.setStatus("current")


class _Epc2x6PortName_Type(OctetString):
    """Custom type epc2x6PortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Epc2x6PortName_Type.__name__ = "OctetString"
_Epc2x6PortName_Object = MibTableColumn
epc2x6PortName = _Epc2x6PortName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 2, 1, 2),
    _Epc2x6PortName_Type()
)
epc2x6PortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc2x6PortName.setStatus("current")


class _Epc2x6PortState_Type(Integer32):
    """Custom type epc2x6PortState based on Integer32"""
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


_Epc2x6PortState_Type.__name__ = "Integer32"
_Epc2x6PortState_Object = MibTableColumn
epc2x6PortState = _Epc2x6PortState_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 2, 1, 3),
    _Epc2x6PortState_Type()
)
epc2x6PortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc2x6PortState.setStatus("current")
_Epc2x6PortSwitchCount_Type = Counter32
_Epc2x6PortSwitchCount_Object = MibTableColumn
epc2x6PortSwitchCount = _Epc2x6PortSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 2, 1, 4),
    _Epc2x6PortSwitchCount_Type()
)
epc2x6PortSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc2x6PortSwitchCount.setStatus("current")


class _Epc2x6PortStartupMode_Type(Integer32):
    """Custom type epc2x6PortStartupMode based on Integer32"""
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


_Epc2x6PortStartupMode_Type.__name__ = "Integer32"
_Epc2x6PortStartupMode_Object = MibTableColumn
epc2x6PortStartupMode = _Epc2x6PortStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 2, 1, 5),
    _Epc2x6PortStartupMode_Type()
)
epc2x6PortStartupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc2x6PortStartupMode.setStatus("current")


class _Epc2x6PortStartupDelay_Type(Integer32):
    """Custom type epc2x6PortStartupDelay based on Integer32"""
    defaultValue = 0


_Epc2x6PortStartupDelay_Object = MibTableColumn
epc2x6PortStartupDelay = _Epc2x6PortStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 2, 1, 6),
    _Epc2x6PortStartupDelay_Type()
)
epc2x6PortStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc2x6PortStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    epc2x6PortStartupDelay.setUnits("seconds")


class _Epc2x6PortRepowerTime_Type(Integer32):
    """Custom type epc2x6PortRepowerTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Epc2x6PortRepowerTime_Type.__name__ = "Integer32"
_Epc2x6PortRepowerTime_Object = MibTableColumn
epc2x6PortRepowerTime = _Epc2x6PortRepowerTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 2, 1, 7),
    _Epc2x6PortRepowerTime_Type()
)
epc2x6PortRepowerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    epc2x6PortRepowerTime.setStatus("current")
if mibBuilder.loadTexts:
    epc2x6PortRepowerTime.setUnits("seconds")


class _Epc2x6portFuses_Type(Integer32):
    """Custom type epc2x6portFuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Epc2x6portFuses_Type.__name__ = "Integer32"
_Epc2x6portFuses_Object = MibScalar
epc2x6portFuses = _Epc2x6portFuses_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 2, 3),
    _Epc2x6portFuses_Type()
)
epc2x6portFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc2x6portFuses.setStatus("current")
_Epc2x6Temperature_Type = Integer32
_Epc2x6Temperature_Object = MibScalar
epc2x6Temperature = _Epc2x6Temperature_Object(
    (1, 3, 6, 1, 4, 1, 28507, 6, 1, 3),
    _Epc2x6Temperature_Type()
)
epc2x6Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    epc2x6Temperature.setStatus("current")
if mibBuilder.loadTexts:
    epc2x6Temperature.setUnits("10th of degree Celsius")
_Epc2x6Conf_ObjectIdentity = ObjectIdentity
epc2x6Conf = _Epc2x6Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 6, 3)
)
_Epc2x6Groups_ObjectIdentity = ObjectIdentity
epc2x6Groups = _Epc2x6Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 6, 3, 1)
)
_Epc2x6Compls_ObjectIdentity = ObjectIdentity
epc2x6Compls = _Epc2x6Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 6, 3, 2)
)

# Managed Objects groups

epc2x6BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 6, 3, 1, 1)
)
epc2x6BasicGroup.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6portNumber"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6TrapCtrl"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6TrapIPAddr"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6TrapIPPort"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6Temperature"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6portFuses"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortStartupMode"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortStartupDelay"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortRepowerTime"))
)
if mibBuilder.loadTexts:
    epc2x6BasicGroup.setStatus("current")


# Notification objects

epc2x6witchEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 1)
)
epc2x6witchEvt1.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt1.setStatus(
        "current"
    )

epc2x6witchEvt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 2)
)
epc2x6witchEvt2.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt2.setStatus(
        "current"
    )

epc2x6witchEvt3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 3)
)
epc2x6witchEvt3.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt3.setStatus(
        "current"
    )

epc2x6witchEvt4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 4)
)
epc2x6witchEvt4.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt4.setStatus(
        "current"
    )

epc2x6witchEvt5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 5)
)
epc2x6witchEvt5.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt5.setStatus(
        "current"
    )

epc2x6witchEvt6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 6)
)
epc2x6witchEvt6.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt6.setStatus(
        "current"
    )

epc2x6witchEvt7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 7)
)
epc2x6witchEvt7.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt7.setStatus(
        "current"
    )

epc2x6witchEvt8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 8)
)
epc2x6witchEvt8.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt8.setStatus(
        "current"
    )

epc2x6witchEvt9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 9)
)
epc2x6witchEvt9.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt9.setStatus(
        "current"
    )

epc2x6witchEvt10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 10)
)
epc2x6witchEvt10.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt10.setStatus(
        "current"
    )

epc2x6witchEvt11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 11)
)
epc2x6witchEvt11.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt11.setStatus(
        "current"
    )

epc2x6witchEvt12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 12)
)
epc2x6witchEvt12.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6PortName"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortState"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6PortSwitchCount"))
)
if mibBuilder.loadTexts:
    epc2x6witchEvt12.setStatus(
        "current"
    )

epc2x6FuseEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 13)
)
epc2x6FuseEvt.setObjects(
    ("GUDEADS-EPC2X6-MIB", "epc2x6portFuses")
)
if mibBuilder.loadTexts:
    epc2x6FuseEvt.setStatus(
        "current"
    )

epc2x6TempEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 0, 14)
)
epc2x6TempEvt.setObjects(
    ("GUDEADS-EPC2X6-MIB", "epc2x6Temperature")
)
if mibBuilder.loadTexts:
    epc2x6TempEvt.setStatus(
        "current"
    )


# Notifications groups

epc2x6NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 6, 3, 1, 2)
)
epc2x6NotificationGroup.setObjects(
      *(("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt1"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt2"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt3"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt4"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt5"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt6"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt7"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt8"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt9"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt10"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt11"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6witchEvt12"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6TempEvt"),
        ("GUDEADS-EPC2X6-MIB", "epc2x6FuseEvt"))
)
if mibBuilder.loadTexts:
    epc2x6NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-EPC2X6-MIB",
    **{"gudeads": gudeads,
       "events": events,
       "epc2x6witchEvt1": epc2x6witchEvt1,
       "epc2x6witchEvt2": epc2x6witchEvt2,
       "epc2x6witchEvt3": epc2x6witchEvt3,
       "epc2x6witchEvt4": epc2x6witchEvt4,
       "epc2x6witchEvt5": epc2x6witchEvt5,
       "epc2x6witchEvt6": epc2x6witchEvt6,
       "epc2x6witchEvt7": epc2x6witchEvt7,
       "epc2x6witchEvt8": epc2x6witchEvt8,
       "epc2x6witchEvt9": epc2x6witchEvt9,
       "epc2x6witchEvt10": epc2x6witchEvt10,
       "epc2x6witchEvt11": epc2x6witchEvt11,
       "epc2x6witchEvt12": epc2x6witchEvt12,
       "epc2x6FuseEvt": epc2x6FuseEvt,
       "epc2x6TempEvt": epc2x6TempEvt,
       "gadsEPC2x6": gadsEPC2x6,
       "epc2x6Objects": epc2x6Objects,
       "epc2x6SNMPaccess": epc2x6SNMPaccess,
       "epc2x6TrapCtrl": epc2x6TrapCtrl,
       "epc2x6TrapIPTable": epc2x6TrapIPTable,
       "epc2x6TrapIPEntry": epc2x6TrapIPEntry,
       "epc2x6TrapIPIndex": epc2x6TrapIPIndex,
       "epc2x6TrapIPAddr": epc2x6TrapIPAddr,
       "epc2x6TrapIPPort": epc2x6TrapIPPort,
       "epc2x6powerports": epc2x6powerports,
       "epc2x6portNumber": epc2x6portNumber,
       "epc2x6portTable": epc2x6portTable,
       "epc2x6portEntry": epc2x6portEntry,
       "epc2x6PortIndex": epc2x6PortIndex,
       "epc2x6PortName": epc2x6PortName,
       "epc2x6PortState": epc2x6PortState,
       "epc2x6PortSwitchCount": epc2x6PortSwitchCount,
       "epc2x6PortStartupMode": epc2x6PortStartupMode,
       "epc2x6PortStartupDelay": epc2x6PortStartupDelay,
       "epc2x6PortRepowerTime": epc2x6PortRepowerTime,
       "epc2x6portFuses": epc2x6portFuses,
       "epc2x6Temperature": epc2x6Temperature,
       "epc2x6Conf": epc2x6Conf,
       "epc2x6Groups": epc2x6Groups,
       "epc2x6BasicGroup": epc2x6BasicGroup,
       "epc2x6NotificationGroup": epc2x6NotificationGroup,
       "epc2x6Compls": epc2x6Compls}
)
