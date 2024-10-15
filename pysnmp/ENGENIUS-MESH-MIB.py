# SNMP MIB module (ENGENIUS-MESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENGENIUS-MESH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:34 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

engeniusmesh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1)
)
engeniusmesh.setRevisions(
        ("2008-03-07 10:00",
         "2008-03-04 10:00",
         "2008-02-28 16:00",
         "2008-02-26 17:00",
         "2008-01-21 16:00",
         "2007-11-29 15:00",
         "2007-11-23 17:00",
         "2007-10-05 10:00",
         "2007-10-02 10:30",
         "2007-09-26 19:00",
         "2007-09-20 13:00",
         "2007-09-13 12:00",
         "2007-08-29 17:00",
         "2007-08-21 17:00",
         "2007-08-03 11:00",
         "2007-07-18 17:00",
         "2007-07-11 17:00",
         "2007-07-10 14:00",
         "2007-06-20 17:00",
         "2007-06-08 16:00",
         "2007-06-01 15:00",
         "2007-05-08 17:00",
         "2007-04-25 16:00",
         "2007-04-10 10:00",
         "2007-04-02 10:00",
         "2007-02-09 17:00",
         "2007-02-08 18:00",
         "2007-02-08 10:00",
         "2007-01-15 10:00",
         "2007-01-11 10:00",
         "2007-01-08 10:00",
         "2006-12-14 10:00",
         "2006-12-01 10:00",
         "2006-11-29 10:00",
         "2006-11-28 10:00",
         "2006-11-23 10:00",
         "2006-11-10 10:00",
         "2006-11-08 10:00",
         "2006-11-06 10:00",
         "2006-11-02 10:00",
         "2006-10-30 10:00",
         "2006-10-27 10:00",
         "2006-10-18 10:00",
         "2006-10-05 10:00",
         "2006-10-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Engenius_ObjectIdentity = ObjectIdentity
engenius = _Engenius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125)
)
_NodeStatus_ObjectIdentity = ObjectIdentity
nodeStatus = _NodeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1)
)
_NodeStatusSystem_ObjectIdentity = ObjectIdentity
nodeStatusSystem = _NodeStatusSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 1)
)


class _SystemUptime_Type(DisplayString):
    """Custom type systemUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SystemUptime_Type.__name__ = "DisplayString"
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 1, 1),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_SystemMemory_Type = Integer32
_SystemMemory_Object = MibScalar
systemMemory = _SystemMemory_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 1, 2),
    _SystemMemory_Type()
)
systemMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMemory.setStatus("current")


class _SystemDevicename_Type(DisplayString):
    """Custom type systemDevicename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SystemDevicename_Type.__name__ = "DisplayString"
_SystemDevicename_Object = MibScalar
systemDevicename = _SystemDevicename_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 1, 3),
    _SystemDevicename_Type()
)
systemDevicename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDevicename.setStatus("current")
_SystemCheckingState_Type = DisplayString
_SystemCheckingState_Object = MibScalar
systemCheckingState = _SystemCheckingState_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 1, 4),
    _SystemCheckingState_Type()
)
systemCheckingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCheckingState.setStatus("current")
_NodeStatusTrap_ObjectIdentity = ObjectIdentity
nodeStatusTrap = _NodeStatusTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2)
)
_TrapVariable_ObjectIdentity = ObjectIdentity
trapVariable = _TrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 1)
)
_GenericTrapVariable_Type = DisplayString
_GenericTrapVariable_Object = MibScalar
genericTrapVariable = _GenericTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 1, 1),
    _GenericTrapVariable_Type()
)
genericTrapVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTrapVariable.setStatus("current")
_GenericTrapVarMACAddress_Type = MacAddress
_GenericTrapVarMACAddress_Object = MibScalar
genericTrapVarMACAddress = _GenericTrapVarMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 1, 2),
    _GenericTrapVarMACAddress_Type()
)
genericTrapVarMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTrapVarMACAddress.setStatus("current")
_GenericTrapVarHostIPAddress_Type = IpAddress
_GenericTrapVarHostIPAddress_Object = MibScalar
genericTrapVarHostIPAddress = _GenericTrapVarHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 1, 3),
    _GenericTrapVarHostIPAddress_Type()
)
genericTrapVarHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTrapVarHostIPAddress.setStatus("current")
_GenericTrapVarHostname_Type = DisplayString
_GenericTrapVarHostname_Object = MibScalar
genericTrapVarHostname = _GenericTrapVarHostname_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 1, 4),
    _GenericTrapVarHostname_Type()
)
genericTrapVarHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTrapVarHostname.setStatus("current")
_GenericTrapVarInterface_Type = Integer32
_GenericTrapVarInterface_Object = MibScalar
genericTrapVarInterface = _GenericTrapVarInterface_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 1, 5),
    _GenericTrapVarInterface_Type()
)
genericTrapVarInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTrapVarInterface.setStatus("current")


class _GenericTrapVarWirelessCard_Type(Integer32):
    """Custom type genericTrapVarWirelessCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cardA", 1),
          ("cardB", 2))
    )


_GenericTrapVarWirelessCard_Type.__name__ = "Integer32"
_GenericTrapVarWirelessCard_Object = MibScalar
genericTrapVarWirelessCard = _GenericTrapVarWirelessCard_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 1, 6),
    _GenericTrapVarWirelessCard_Type()
)
genericTrapVarWirelessCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTrapVarWirelessCard.setStatus("current")


class _GenericTrapVarEthernetPort_Type(Integer32):
    """Custom type genericTrapVarEthernetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethPortA", 1),
          ("ethPortB", 2))
    )


_GenericTrapVarEthernetPort_Type.__name__ = "Integer32"
_GenericTrapVarEthernetPort_Object = MibScalar
genericTrapVarEthernetPort = _GenericTrapVarEthernetPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 1, 7),
    _GenericTrapVarEthernetPort_Type()
)
genericTrapVarEthernetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTrapVarEthernetPort.setStatus("current")
_GenericTrapVarCount_Type = Integer32
_GenericTrapVarCount_Object = MibScalar
genericTrapVarCount = _GenericTrapVarCount_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 1, 8),
    _GenericTrapVarCount_Type()
)
genericTrapVarCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTrapVarCount.setStatus("current")
_AdminTraps_ObjectIdentity = ObjectIdentity
adminTraps = _AdminTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    adminTraps.setStatus("current")
_UserTraps_ObjectIdentity = ObjectIdentity
userTraps = _UserTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    userTraps.setStatus("current")
_SystemTraps_ObjectIdentity = ObjectIdentity
systemTraps = _SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    systemTraps.setStatus("current")
_NodeConfiguration_ObjectIdentity = ObjectIdentity
nodeConfiguration = _NodeConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2)
)
_NodeConfigurationSystem_ObjectIdentity = ObjectIdentity
nodeConfigurationSystem = _NodeConfigurationSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 1)
)


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 1, 1),
    _SystemName_Type()
)
systemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _SystemLocation_Type(DisplayString):
    """Custom type systemLocation based on DisplayString"""
    defaultValue = OctetString("Unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemLocation_Type.__name__ = "DisplayString"
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 1, 2),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLocation.setStatus("current")


class _SystemContactName_Type(DisplayString):
    """Custom type systemContactName based on DisplayString"""
    defaultValue = OctetString("Unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemContactName_Type.__name__ = "DisplayString"
_SystemContactName_Object = MibScalar
systemContactName = _SystemContactName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 1, 3),
    _SystemContactName_Type()
)
systemContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemContactName.setStatus("current")


class _SystemContactMail_Type(DisplayString):
    """Custom type systemContactMail based on DisplayString"""
    defaultValue = OctetString("Unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemContactMail_Type.__name__ = "DisplayString"
_SystemContactMail_Object = MibScalar
systemContactMail = _SystemContactMail_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 1, 4),
    _SystemContactMail_Type()
)
systemContactMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemContactMail.setStatus("current")


class _SystemContactPhone_Type(DisplayString):
    """Custom type systemContactPhone based on DisplayString"""
    defaultValue = OctetString("Unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemContactPhone_Type.__name__ = "DisplayString"
_SystemContactPhone_Object = MibScalar
systemContactPhone = _SystemContactPhone_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 1, 5),
    _SystemContactPhone_Type()
)
systemContactPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemContactPhone.setStatus("current")


class _SystemDescription_Type(DisplayString):
    """Custom type systemDescription based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemDescription_Type.__name__ = "DisplayString"
_SystemDescription_Object = MibScalar
systemDescription = _SystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 1, 6),
    _SystemDescription_Type()
)
systemDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDescription.setStatus("current")


class _SystemObjectid_Type(DisplayString):
    """Custom type systemObjectid based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemObjectid_Type.__name__ = "DisplayString"
_SystemObjectid_Object = MibScalar
systemObjectid = _SystemObjectid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 1, 7),
    _SystemObjectid_Type()
)
systemObjectid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemObjectid.setStatus("current")


class _SystemOperatemode_Type(Integer32):
    """Custom type systemOperatemode based on Integer32"""
    defaultValue = 1

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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 6),
          ("client", 16),
          ("clientrelay", 3),
          ("clientrouter", 17),
          ("dualradiocrelay", 10),
          ("dualradiogw", 8),
          ("dualradiorelay", 9),
          ("gateway", 1),
          ("layer2", 5),
          ("layer2gw", 4),
          ("masterbridge", 13),
          ("mlrd", 11),
          ("relay", 2),
          ("repeater", 15),
          ("router", 7),
          ("slavebridge", 12),
          ("wdsbridge", 14),
          ("wdsrouter", 18))
    )


_SystemOperatemode_Type.__name__ = "Integer32"
_SystemOperatemode_Object = MibScalar
systemOperatemode = _SystemOperatemode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 1, 8),
    _SystemOperatemode_Type()
)
systemOperatemode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemOperatemode.setStatus("current")


class _SystemUpdateMode_Type(Integer32):
    """Custom type systemUpdateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_SystemUpdateMode_Type.__name__ = "Integer32"
_SystemUpdateMode_Object = MibScalar
systemUpdateMode = _SystemUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 1, 9),
    _SystemUpdateMode_Type()
)
systemUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemUpdateMode.setStatus("current")
_NodeConfigurationEthernet_ObjectIdentity = ObjectIdentity
nodeConfigurationEthernet = _NodeConfigurationEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2)
)
_EthernetInterfaceTable_Object = MibTable
ethernetInterfaceTable = _EthernetInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ethernetInterfaceTable.setStatus("current")
_EthernetInterfaceTableEntry_Object = MibTableRow
ethernetInterfaceTableEntry = _EthernetInterfaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1)
)
ethernetInterfaceTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "ethInterfaceTableIndex"),
)
if mibBuilder.loadTexts:
    ethernetInterfaceTableEntry.setStatus("current")


class _EthInterfaceTableIndex_Type(Integer32):
    """Custom type ethInterfaceTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_EthInterfaceTableIndex_Type.__name__ = "Integer32"
_EthInterfaceTableIndex_Object = MibTableColumn
ethInterfaceTableIndex = _EthInterfaceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1, 1),
    _EthInterfaceTableIndex_Type()
)
ethInterfaceTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethInterfaceTableIndex.setStatus("current")


class _EthInterfaceTableName_Type(OctetString):
    """Custom type ethInterfaceTableName based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EthInterfaceTableName_Type.__name__ = "OctetString"
_EthInterfaceTableName_Object = MibTableColumn
ethInterfaceTableName = _EthInterfaceTableName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1, 2),
    _EthInterfaceTableName_Type()
)
ethInterfaceTableName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethInterfaceTableName.setStatus("current")


class _EthInterfaceTableBase_Type(OctetString):
    """Custom type ethInterfaceTableBase based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EthInterfaceTableBase_Type.__name__ = "OctetString"
_EthInterfaceTableBase_Object = MibTableColumn
ethInterfaceTableBase = _EthInterfaceTableBase_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1, 3),
    _EthInterfaceTableBase_Type()
)
ethInterfaceTableBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethInterfaceTableBase.setStatus("current")


class _EthInterfaceTableMac_Type(MacAddress):
    """Custom type ethInterfaceTableMac based on MacAddress"""
    defaultValue = OctetString("Nil")


_EthInterfaceTableMac_Object = MibTableColumn
ethInterfaceTableMac = _EthInterfaceTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1, 4),
    _EthInterfaceTableMac_Type()
)
ethInterfaceTableMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethInterfaceTableMac.setStatus("current")


class _EthInterfaceTableBridge_Type(OctetString):
    """Custom type ethInterfaceTableBridge based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EthInterfaceTableBridge_Type.__name__ = "OctetString"
_EthInterfaceTableBridge_Object = MibTableColumn
ethInterfaceTableBridge = _EthInterfaceTableBridge_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1, 5),
    _EthInterfaceTableBridge_Type()
)
ethInterfaceTableBridge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethInterfaceTableBridge.setStatus("current")


class _EthInterfaceTableBridgeCost_Type(Integer32):
    """Custom type ethInterfaceTableBridgeCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_EthInterfaceTableBridgeCost_Type.__name__ = "Integer32"
_EthInterfaceTableBridgeCost_Object = MibTableColumn
ethInterfaceTableBridgeCost = _EthInterfaceTableBridgeCost_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1, 6),
    _EthInterfaceTableBridgeCost_Type()
)
ethInterfaceTableBridgeCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethInterfaceTableBridgeCost.setStatus("current")


class _EthInterfaceTableBridgePrio_Type(Integer32):
    """Custom type ethInterfaceTableBridgePrio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_EthInterfaceTableBridgePrio_Type.__name__ = "Integer32"
_EthInterfaceTableBridgePrio_Object = MibTableColumn
ethInterfaceTableBridgePrio = _EthInterfaceTableBridgePrio_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1, 7),
    _EthInterfaceTableBridgePrio_Type()
)
ethInterfaceTableBridgePrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethInterfaceTableBridgePrio.setStatus("current")


class _EthInterfaceTableComments_Type(DisplayString):
    """Custom type ethInterfaceTableComments based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EthInterfaceTableComments_Type.__name__ = "DisplayString"
_EthInterfaceTableComments_Object = MibTableColumn
ethInterfaceTableComments = _EthInterfaceTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1, 8),
    _EthInterfaceTableComments_Type()
)
ethInterfaceTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethInterfaceTableComments.setStatus("current")


class _EthInterfaceTableActive_Type(Integer32):
    """Custom type ethInterfaceTableActive based on Integer32"""
    defaultValue = 1

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


_EthInterfaceTableActive_Type.__name__ = "Integer32"
_EthInterfaceTableActive_Object = MibTableColumn
ethInterfaceTableActive = _EthInterfaceTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1, 9),
    _EthInterfaceTableActive_Type()
)
ethInterfaceTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethInterfaceTableActive.setStatus("current")
_EthInterfaceTableRowStatus_Type = RowStatus
_EthInterfaceTableRowStatus_Object = MibTableColumn
ethInterfaceTableRowStatus = _EthInterfaceTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 2, 1, 1, 10),
    _EthInterfaceTableRowStatus_Type()
)
ethInterfaceTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethInterfaceTableRowStatus.setStatus("current")
_NodeConfigurationWireless_ObjectIdentity = ObjectIdentity
nodeConfigurationWireless = _NodeConfigurationWireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3)
)
_WirelessInterfaceTable_Object = MibTable
wirelessInterfaceTable = _WirelessInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    wirelessInterfaceTable.setStatus("current")
_WirelessInterfaceTableEntry_Object = MibTableRow
wirelessInterfaceTableEntry = _WirelessInterfaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1)
)
wirelessInterfaceTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "wlanInterfaceTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessInterfaceTableEntry.setStatus("current")


class _WlanInterfaceTableIndex_Type(Integer32):
    """Custom type wlanInterfaceTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_WlanInterfaceTableIndex_Type.__name__ = "Integer32"
_WlanInterfaceTableIndex_Object = MibTableColumn
wlanInterfaceTableIndex = _WlanInterfaceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 1),
    _WlanInterfaceTableIndex_Type()
)
wlanInterfaceTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanInterfaceTableIndex.setStatus("current")


class _WlanInterfaceTableName_Type(OctetString):
    """Custom type wlanInterfaceTableName based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanInterfaceTableName_Type.__name__ = "OctetString"
_WlanInterfaceTableName_Object = MibTableColumn
wlanInterfaceTableName = _WlanInterfaceTableName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 2),
    _WlanInterfaceTableName_Type()
)
wlanInterfaceTableName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableName.setStatus("current")


class _WlanInterfaceTableBase_Type(OctetString):
    """Custom type wlanInterfaceTableBase based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanInterfaceTableBase_Type.__name__ = "OctetString"
_WlanInterfaceTableBase_Object = MibTableColumn
wlanInterfaceTableBase = _WlanInterfaceTableBase_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 3),
    _WlanInterfaceTableBase_Type()
)
wlanInterfaceTableBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableBase.setStatus("current")


class _WlanInterfaceTableBridge_Type(OctetString):
    """Custom type wlanInterfaceTableBridge based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanInterfaceTableBridge_Type.__name__ = "OctetString"
_WlanInterfaceTableBridge_Object = MibTableColumn
wlanInterfaceTableBridge = _WlanInterfaceTableBridge_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 4),
    _WlanInterfaceTableBridge_Type()
)
wlanInterfaceTableBridge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableBridge.setStatus("current")


class _WlanInterfaceTableBridgeCost_Type(Integer32):
    """Custom type wlanInterfaceTableBridgeCost based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WlanInterfaceTableBridgeCost_Type.__name__ = "Integer32"
_WlanInterfaceTableBridgeCost_Object = MibTableColumn
wlanInterfaceTableBridgeCost = _WlanInterfaceTableBridgeCost_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 5),
    _WlanInterfaceTableBridgeCost_Type()
)
wlanInterfaceTableBridgeCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableBridgeCost.setStatus("current")


class _WlanInterfaceTableBridgePrio_Type(Integer32):
    """Custom type wlanInterfaceTableBridgePrio based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WlanInterfaceTableBridgePrio_Type.__name__ = "Integer32"
_WlanInterfaceTableBridgePrio_Object = MibTableColumn
wlanInterfaceTableBridgePrio = _WlanInterfaceTableBridgePrio_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 6),
    _WlanInterfaceTableBridgePrio_Type()
)
wlanInterfaceTableBridgePrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableBridgePrio.setStatus("current")


class _WlanInterfaceTableMode_Type(Integer32):
    """Custom type wlanInterfaceTableMode based on Integer32"""
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
        *(("adhoc", 3),
          ("ap", 1),
          ("sta", 2),
          ("wds", 4))
    )


_WlanInterfaceTableMode_Type.__name__ = "Integer32"
_WlanInterfaceTableMode_Object = MibTableColumn
wlanInterfaceTableMode = _WlanInterfaceTableMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 7),
    _WlanInterfaceTableMode_Type()
)
wlanInterfaceTableMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableMode.setStatus("current")


class _WlanInterfaceTableBand_Type(Integer32):
    """Custom type wlanInterfaceTableBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 3))
    )


_WlanInterfaceTableBand_Type.__name__ = "Integer32"
_WlanInterfaceTableBand_Object = MibTableColumn
wlanInterfaceTableBand = _WlanInterfaceTableBand_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 8),
    _WlanInterfaceTableBand_Type()
)
wlanInterfaceTableBand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableBand.setStatus("current")


class _WlanInterfaceTableEssid_Type(DisplayString):
    """Custom type wlanInterfaceTableEssid based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanInterfaceTableEssid_Type.__name__ = "DisplayString"
_WlanInterfaceTableEssid_Object = MibTableColumn
wlanInterfaceTableEssid = _WlanInterfaceTableEssid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 9),
    _WlanInterfaceTableEssid_Type()
)
wlanInterfaceTableEssid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableEssid.setStatus("current")


class _WlanInterfaceTableFreq_Type(Integer32):
    """Custom type wlanInterfaceTableFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_WlanInterfaceTableFreq_Type.__name__ = "Integer32"
_WlanInterfaceTableFreq_Object = MibTableColumn
wlanInterfaceTableFreq = _WlanInterfaceTableFreq_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 10),
    _WlanInterfaceTableFreq_Type()
)
wlanInterfaceTableFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableFreq.setStatus("current")
_WlanInterfaceTableMac_Type = MacAddress
_WlanInterfaceTableMac_Object = MibTableColumn
wlanInterfaceTableMac = _WlanInterfaceTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 11),
    _WlanInterfaceTableMac_Type()
)
wlanInterfaceTableMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableMac.setStatus("current")


class _WlanInterfaceTableSecurity_Type(Integer32):
    """Custom type wlanInterfaceTableSecurity based on Integer32"""
    defaultValue = 1

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
        *(("aes", 4),
          ("open", 1),
          ("wep", 2),
          ("wpa1", 3),
          ("wpa1n2", 6),
          ("wpa2", 5))
    )


_WlanInterfaceTableSecurity_Type.__name__ = "Integer32"
_WlanInterfaceTableSecurity_Object = MibTableColumn
wlanInterfaceTableSecurity = _WlanInterfaceTableSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 12),
    _WlanInterfaceTableSecurity_Type()
)
wlanInterfaceTableSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableSecurity.setStatus("current")


class _WlanInterfaceTableWpaType_Type(Integer32):
    """Custom type wlanInterfaceTableWpaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("tkip", 1))
    )


_WlanInterfaceTableWpaType_Type.__name__ = "Integer32"
_WlanInterfaceTableWpaType_Object = MibTableColumn
wlanInterfaceTableWpaType = _WlanInterfaceTableWpaType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 13),
    _WlanInterfaceTableWpaType_Type()
)
wlanInterfaceTableWpaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableWpaType.setStatus("current")


class _WlanInterfaceTableDot1x_Type(Integer32):
    """Custom type wlanInterfaceTableDot1x based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WlanInterfaceTableDot1x_Type.__name__ = "Integer32"
_WlanInterfaceTableDot1x_Object = MibTableColumn
wlanInterfaceTableDot1x = _WlanInterfaceTableDot1x_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 14),
    _WlanInterfaceTableDot1x_Type()
)
wlanInterfaceTableDot1x.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableDot1x.setStatus("current")


class _WlanInterfaceTableEncryptionKey_Type(OctetString):
    """Custom type wlanInterfaceTableEncryptionKey based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlanInterfaceTableEncryptionKey_Type.__name__ = "OctetString"
_WlanInterfaceTableEncryptionKey_Object = MibTableColumn
wlanInterfaceTableEncryptionKey = _WlanInterfaceTableEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 15),
    _WlanInterfaceTableEncryptionKey_Type()
)
wlanInterfaceTableEncryptionKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableEncryptionKey.setStatus("current")


class _WlanInterfaceTableBroadcastSsid_Type(Integer32):
    """Custom type wlanInterfaceTableBroadcastSsid based on Integer32"""
    defaultValue = 1

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


_WlanInterfaceTableBroadcastSsid_Type.__name__ = "Integer32"
_WlanInterfaceTableBroadcastSsid_Object = MibTableColumn
wlanInterfaceTableBroadcastSsid = _WlanInterfaceTableBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 16),
    _WlanInterfaceTableBroadcastSsid_Type()
)
wlanInterfaceTableBroadcastSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableBroadcastSsid.setStatus("current")


class _WlanInterfaceTableBeaconInt_Type(Integer32):
    """Custom type wlanInterfaceTableBeaconInt based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_WlanInterfaceTableBeaconInt_Type.__name__ = "Integer32"
_WlanInterfaceTableBeaconInt_Object = MibTableColumn
wlanInterfaceTableBeaconInt = _WlanInterfaceTableBeaconInt_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 17),
    _WlanInterfaceTableBeaconInt_Type()
)
wlanInterfaceTableBeaconInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableBeaconInt.setStatus("current")


class _WlanInterfaceTableRtsThreshold_Type(Integer32):
    """Custom type wlanInterfaceTableRtsThreshold based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_WlanInterfaceTableRtsThreshold_Type.__name__ = "Integer32"
_WlanInterfaceTableRtsThreshold_Object = MibTableColumn
wlanInterfaceTableRtsThreshold = _WlanInterfaceTableRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 18),
    _WlanInterfaceTableRtsThreshold_Type()
)
wlanInterfaceTableRtsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableRtsThreshold.setStatus("current")


class _WlanInterfaceTableFragThreshold_Type(Integer32):
    """Custom type wlanInterfaceTableFragThreshold based on Integer32"""
    defaultValue = 2346

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 2346),
    )


_WlanInterfaceTableFragThreshold_Type.__name__ = "Integer32"
_WlanInterfaceTableFragThreshold_Object = MibTableColumn
wlanInterfaceTableFragThreshold = _WlanInterfaceTableFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 19),
    _WlanInterfaceTableFragThreshold_Type()
)
wlanInterfaceTableFragThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableFragThreshold.setStatus("current")


class _WlanInterfaceTableDtimInterval_Type(Integer32):
    """Custom type wlanInterfaceTableDtimInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WlanInterfaceTableDtimInterval_Type.__name__ = "Integer32"
_WlanInterfaceTableDtimInterval_Object = MibTableColumn
wlanInterfaceTableDtimInterval = _WlanInterfaceTableDtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 20),
    _WlanInterfaceTableDtimInterval_Type()
)
wlanInterfaceTableDtimInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableDtimInterval.setStatus("current")


class _WlanInterfaceTableDatarate_Type(Integer32):
    """Custom type wlanInterfaceTableDatarate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_WlanInterfaceTableDatarate_Type.__name__ = "Integer32"
_WlanInterfaceTableDatarate_Object = MibTableColumn
wlanInterfaceTableDatarate = _WlanInterfaceTableDatarate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 21),
    _WlanInterfaceTableDatarate_Type()
)
wlanInterfaceTableDatarate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableDatarate.setStatus("current")


class _WlanInterfaceTableDiversity_Type(Integer32):
    """Custom type wlanInterfaceTableDiversity based on Integer32"""
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
        *(("carddefault", 3),
          ("disable", 2),
          ("enable", 1))
    )


_WlanInterfaceTableDiversity_Type.__name__ = "Integer32"
_WlanInterfaceTableDiversity_Object = MibTableColumn
wlanInterfaceTableDiversity = _WlanInterfaceTableDiversity_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 22),
    _WlanInterfaceTableDiversity_Type()
)
wlanInterfaceTableDiversity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableDiversity.setStatus("current")


class _WlanInterfaceTableTxAntenna_Type(Integer32):
    """Custom type wlanInterfaceTableTxAntenna based on Integer32"""
    defaultValue = 3

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
        *(("carddefault", 3),
          ("diversity", 0),
          ("port1", 1),
          ("port2", 2))
    )


_WlanInterfaceTableTxAntenna_Type.__name__ = "Integer32"
_WlanInterfaceTableTxAntenna_Object = MibTableColumn
wlanInterfaceTableTxAntenna = _WlanInterfaceTableTxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 23),
    _WlanInterfaceTableTxAntenna_Type()
)
wlanInterfaceTableTxAntenna.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableTxAntenna.setStatus("current")


class _WlanInterfaceTableRxAntenna_Type(Integer32):
    """Custom type wlanInterfaceTableRxAntenna based on Integer32"""
    defaultValue = 3

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
        *(("carddefault", 3),
          ("diversity", 0),
          ("port1", 1),
          ("port2", 2))
    )


_WlanInterfaceTableRxAntenna_Type.__name__ = "Integer32"
_WlanInterfaceTableRxAntenna_Object = MibTableColumn
wlanInterfaceTableRxAntenna = _WlanInterfaceTableRxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 24),
    _WlanInterfaceTableRxAntenna_Type()
)
wlanInterfaceTableRxAntenna.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableRxAntenna.setStatus("current")


class _WlanInterfaceTableCrntTxPower_Type(Integer32):
    """Custom type wlanInterfaceTableCrntTxPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_WlanInterfaceTableCrntTxPower_Type.__name__ = "Integer32"
_WlanInterfaceTableCrntTxPower_Object = MibTableColumn
wlanInterfaceTableCrntTxPower = _WlanInterfaceTableCrntTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 25),
    _WlanInterfaceTableCrntTxPower_Type()
)
wlanInterfaceTableCrntTxPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableCrntTxPower.setStatus("current")


class _WlanInterfaceTableTxPower_Type(Integer32):
    """Custom type wlanInterfaceTableTxPower based on Integer32"""
    defaultValue = 9999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_WlanInterfaceTableTxPower_Type.__name__ = "Integer32"
_WlanInterfaceTableTxPower_Object = MibTableColumn
wlanInterfaceTableTxPower = _WlanInterfaceTableTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 26),
    _WlanInterfaceTableTxPower_Type()
)
wlanInterfaceTableTxPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableTxPower.setStatus("current")


class _WlanInterfaceTableSeperation_Type(Integer32):
    """Custom type wlanInterfaceTableSeperation based on Integer32"""
    defaultValue = 2

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


_WlanInterfaceTableSeperation_Type.__name__ = "Integer32"
_WlanInterfaceTableSeperation_Object = MibTableColumn
wlanInterfaceTableSeperation = _WlanInterfaceTableSeperation_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 27),
    _WlanInterfaceTableSeperation_Type()
)
wlanInterfaceTableSeperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableSeperation.setStatus("current")


class _WlanInterfaceTableComments_Type(DisplayString):
    """Custom type wlanInterfaceTableComments based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WlanInterfaceTableComments_Type.__name__ = "DisplayString"
_WlanInterfaceTableComments_Object = MibTableColumn
wlanInterfaceTableComments = _WlanInterfaceTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 28),
    _WlanInterfaceTableComments_Type()
)
wlanInterfaceTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableComments.setStatus("current")


class _WlanInterfaceTableActive_Type(Integer32):
    """Custom type wlanInterfaceTableActive based on Integer32"""
    defaultValue = 1

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


_WlanInterfaceTableActive_Type.__name__ = "Integer32"
_WlanInterfaceTableActive_Object = MibTableColumn
wlanInterfaceTableActive = _WlanInterfaceTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 29),
    _WlanInterfaceTableActive_Type()
)
wlanInterfaceTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableActive.setStatus("current")
_WlanInterfaceTableRowStatus_Type = RowStatus
_WlanInterfaceTableRowStatus_Object = MibTableColumn
wlanInterfaceTableRowStatus = _WlanInterfaceTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 1, 1, 30),
    _WlanInterfaceTableRowStatus_Type()
)
wlanInterfaceTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wlanInterfaceTableRowStatus.setStatus("current")
_WirelessFrequencyMeshTable_Object = MibTable
wirelessFrequencyMeshTable = _WirelessFrequencyMeshTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    wirelessFrequencyMeshTable.setStatus("current")
_WirelessFrequencyMeshTableEntry_Object = MibTableRow
wirelessFrequencyMeshTableEntry = _WirelessFrequencyMeshTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 2, 1)
)
wirelessFrequencyMeshTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "wlanFrequencyMeshTableIndex"),
)
if mibBuilder.loadTexts:
    wirelessFrequencyMeshTableEntry.setStatus("current")


class _WlanFrequencyMeshTableIndex_Type(Integer32):
    """Custom type wlanFrequencyMeshTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WlanFrequencyMeshTableIndex_Type.__name__ = "Integer32"
_WlanFrequencyMeshTableIndex_Object = MibTableColumn
wlanFrequencyMeshTableIndex = _WlanFrequencyMeshTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 2, 1, 1),
    _WlanFrequencyMeshTableIndex_Type()
)
wlanFrequencyMeshTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanFrequencyMeshTableIndex.setStatus("current")


class _WlanFrequencyMeshTableChannel_Type(Integer32):
    """Custom type wlanFrequencyMeshTableChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WlanFrequencyMeshTableChannel_Type.__name__ = "Integer32"
_WlanFrequencyMeshTableChannel_Object = MibTableColumn
wlanFrequencyMeshTableChannel = _WlanFrequencyMeshTableChannel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 2, 1, 2),
    _WlanFrequencyMeshTableChannel_Type()
)
wlanFrequencyMeshTableChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanFrequencyMeshTableChannel.setStatus("current")
_WlanFrequencyMeshTableFrequency_Type = OctetString
_WlanFrequencyMeshTableFrequency_Object = MibTableColumn
wlanFrequencyMeshTableFrequency = _WlanFrequencyMeshTableFrequency_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 2, 1, 3),
    _WlanFrequencyMeshTableFrequency_Type()
)
wlanFrequencyMeshTableFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanFrequencyMeshTableFrequency.setStatus("current")
_WlanFrequencyMeshTableRowStatus_Type = RowStatus
_WlanFrequencyMeshTableRowStatus_Object = MibTableColumn
wlanFrequencyMeshTableRowStatus = _WlanFrequencyMeshTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 2, 1, 4),
    _WlanFrequencyMeshTableRowStatus_Type()
)
wlanFrequencyMeshTableRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanFrequencyMeshTableRowStatus.setStatus("current")
_WirelessFrequencyAp0Table_Object = MibTable
wirelessFrequencyAp0Table = _WirelessFrequencyAp0Table_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    wirelessFrequencyAp0Table.setStatus("current")
_WirelessFrequencyAp0TableEntry_Object = MibTableRow
wirelessFrequencyAp0TableEntry = _WirelessFrequencyAp0TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 3, 1)
)
wirelessFrequencyAp0TableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "wlanFrequencyAp0TableIndex"),
)
if mibBuilder.loadTexts:
    wirelessFrequencyAp0TableEntry.setStatus("current")


class _WlanFrequencyAp0TableIndex_Type(Integer32):
    """Custom type wlanFrequencyAp0TableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WlanFrequencyAp0TableIndex_Type.__name__ = "Integer32"
_WlanFrequencyAp0TableIndex_Object = MibTableColumn
wlanFrequencyAp0TableIndex = _WlanFrequencyAp0TableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 3, 1, 1),
    _WlanFrequencyAp0TableIndex_Type()
)
wlanFrequencyAp0TableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanFrequencyAp0TableIndex.setStatus("current")


class _WlanFrequencyAp0TableChannel_Type(Integer32):
    """Custom type wlanFrequencyAp0TableChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WlanFrequencyAp0TableChannel_Type.__name__ = "Integer32"
_WlanFrequencyAp0TableChannel_Object = MibTableColumn
wlanFrequencyAp0TableChannel = _WlanFrequencyAp0TableChannel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 3, 1, 2),
    _WlanFrequencyAp0TableChannel_Type()
)
wlanFrequencyAp0TableChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanFrequencyAp0TableChannel.setStatus("current")
_WlanFrequencyAp0TableFrequency_Type = OctetString
_WlanFrequencyAp0TableFrequency_Object = MibTableColumn
wlanFrequencyAp0TableFrequency = _WlanFrequencyAp0TableFrequency_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 3, 1, 3),
    _WlanFrequencyAp0TableFrequency_Type()
)
wlanFrequencyAp0TableFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanFrequencyAp0TableFrequency.setStatus("current")
_WlanFrequencyAp0TableRowStatus_Type = RowStatus
_WlanFrequencyAp0TableRowStatus_Object = MibTableColumn
wlanFrequencyAp0TableRowStatus = _WlanFrequencyAp0TableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 3, 1, 4),
    _WlanFrequencyAp0TableRowStatus_Type()
)
wlanFrequencyAp0TableRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanFrequencyAp0TableRowStatus.setStatus("current")
_WirelessFrequencyAp1Table_Object = MibTable
wirelessFrequencyAp1Table = _WirelessFrequencyAp1Table_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    wirelessFrequencyAp1Table.setStatus("current")
_WirelessFrequencyAp1TableEntry_Object = MibTableRow
wirelessFrequencyAp1TableEntry = _WirelessFrequencyAp1TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 4, 1)
)
wirelessFrequencyAp1TableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "wlanFrequencyAp1TableIndex"),
)
if mibBuilder.loadTexts:
    wirelessFrequencyAp1TableEntry.setStatus("current")


class _WlanFrequencyAp1TableIndex_Type(Integer32):
    """Custom type wlanFrequencyAp1TableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WlanFrequencyAp1TableIndex_Type.__name__ = "Integer32"
_WlanFrequencyAp1TableIndex_Object = MibTableColumn
wlanFrequencyAp1TableIndex = _WlanFrequencyAp1TableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 4, 1, 1),
    _WlanFrequencyAp1TableIndex_Type()
)
wlanFrequencyAp1TableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanFrequencyAp1TableIndex.setStatus("current")


class _WlanFrequencyAp1TableChannel_Type(Integer32):
    """Custom type wlanFrequencyAp1TableChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WlanFrequencyAp1TableChannel_Type.__name__ = "Integer32"
_WlanFrequencyAp1TableChannel_Object = MibTableColumn
wlanFrequencyAp1TableChannel = _WlanFrequencyAp1TableChannel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 4, 1, 2),
    _WlanFrequencyAp1TableChannel_Type()
)
wlanFrequencyAp1TableChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanFrequencyAp1TableChannel.setStatus("current")
_WlanFrequencyAp1TableFrequency_Type = OctetString
_WlanFrequencyAp1TableFrequency_Object = MibTableColumn
wlanFrequencyAp1TableFrequency = _WlanFrequencyAp1TableFrequency_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 4, 1, 3),
    _WlanFrequencyAp1TableFrequency_Type()
)
wlanFrequencyAp1TableFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanFrequencyAp1TableFrequency.setStatus("current")
_WlanFrequencyAp1TableRowStatus_Type = RowStatus
_WlanFrequencyAp1TableRowStatus_Object = MibTableColumn
wlanFrequencyAp1TableRowStatus = _WlanFrequencyAp1TableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 3, 4, 1, 4),
    _WlanFrequencyAp1TableRowStatus_Type()
)
wlanFrequencyAp1TableRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanFrequencyAp1TableRowStatus.setStatus("current")
_NodeConfigurationVlan_ObjectIdentity = ObjectIdentity
nodeConfigurationVlan = _NodeConfigurationVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4)
)
_VlanInterfaceTable_Object = MibTable
vlanInterfaceTable = _VlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vlanInterfaceTable.setStatus("current")
_VlanInterfaceTableEntry_Object = MibTableRow
vlanInterfaceTableEntry = _VlanInterfaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1)
)
vlanInterfaceTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "vlanInterfaceTableIndex"),
)
if mibBuilder.loadTexts:
    vlanInterfaceTableEntry.setStatus("current")


class _VlanInterfaceTableIndex_Type(Integer32):
    """Custom type vlanInterfaceTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VlanInterfaceTableIndex_Type.__name__ = "Integer32"
_VlanInterfaceTableIndex_Object = MibTableColumn
vlanInterfaceTableIndex = _VlanInterfaceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 1),
    _VlanInterfaceTableIndex_Type()
)
vlanInterfaceTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanInterfaceTableIndex.setStatus("current")


class _VlanInterfaceTableName_Type(OctetString):
    """Custom type vlanInterfaceTableName based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanInterfaceTableName_Type.__name__ = "OctetString"
_VlanInterfaceTableName_Object = MibTableColumn
vlanInterfaceTableName = _VlanInterfaceTableName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 2),
    _VlanInterfaceTableName_Type()
)
vlanInterfaceTableName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInterfaceTableName.setStatus("current")


class _VlanInterfaceTableBase_Type(OctetString):
    """Custom type vlanInterfaceTableBase based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanInterfaceTableBase_Type.__name__ = "OctetString"
_VlanInterfaceTableBase_Object = MibTableColumn
vlanInterfaceTableBase = _VlanInterfaceTableBase_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 3),
    _VlanInterfaceTableBase_Type()
)
vlanInterfaceTableBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInterfaceTableBase.setStatus("current")
_VlanInterfaceTableMac_Type = MacAddress
_VlanInterfaceTableMac_Object = MibTableColumn
vlanInterfaceTableMac = _VlanInterfaceTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 4),
    _VlanInterfaceTableMac_Type()
)
vlanInterfaceTableMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInterfaceTableMac.setStatus("current")
_VlanInterfaceTableId_Type = Integer32
_VlanInterfaceTableId_Object = MibTableColumn
vlanInterfaceTableId = _VlanInterfaceTableId_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 5),
    _VlanInterfaceTableId_Type()
)
vlanInterfaceTableId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInterfaceTableId.setStatus("current")


class _VlanInterfaceTableBridge_Type(OctetString):
    """Custom type vlanInterfaceTableBridge based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanInterfaceTableBridge_Type.__name__ = "OctetString"
_VlanInterfaceTableBridge_Object = MibTableColumn
vlanInterfaceTableBridge = _VlanInterfaceTableBridge_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 6),
    _VlanInterfaceTableBridge_Type()
)
vlanInterfaceTableBridge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInterfaceTableBridge.setStatus("current")


class _VlanInterfaceTableBridgeCost_Type(Integer32):
    """Custom type vlanInterfaceTableBridgeCost based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_VlanInterfaceTableBridgeCost_Type.__name__ = "Integer32"
_VlanInterfaceTableBridgeCost_Object = MibTableColumn
vlanInterfaceTableBridgeCost = _VlanInterfaceTableBridgeCost_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 7),
    _VlanInterfaceTableBridgeCost_Type()
)
vlanInterfaceTableBridgeCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInterfaceTableBridgeCost.setStatus("current")


class _VlanInterfaceTableBridgePrio_Type(Integer32):
    """Custom type vlanInterfaceTableBridgePrio based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_VlanInterfaceTableBridgePrio_Type.__name__ = "Integer32"
_VlanInterfaceTableBridgePrio_Object = MibTableColumn
vlanInterfaceTableBridgePrio = _VlanInterfaceTableBridgePrio_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 8),
    _VlanInterfaceTableBridgePrio_Type()
)
vlanInterfaceTableBridgePrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInterfaceTableBridgePrio.setStatus("current")


class _VlanInterfaceTableComments_Type(DisplayString):
    """Custom type vlanInterfaceTableComments based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanInterfaceTableComments_Type.__name__ = "DisplayString"
_VlanInterfaceTableComments_Object = MibTableColumn
vlanInterfaceTableComments = _VlanInterfaceTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 9),
    _VlanInterfaceTableComments_Type()
)
vlanInterfaceTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInterfaceTableComments.setStatus("current")


class _VlanInterfaceTableActive_Type(Integer32):
    """Custom type vlanInterfaceTableActive based on Integer32"""
    defaultValue = 1

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


_VlanInterfaceTableActive_Type.__name__ = "Integer32"
_VlanInterfaceTableActive_Object = MibTableColumn
vlanInterfaceTableActive = _VlanInterfaceTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 10),
    _VlanInterfaceTableActive_Type()
)
vlanInterfaceTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInterfaceTableActive.setStatus("current")
_VlanInterfaceTableRowStatus_Type = RowStatus
_VlanInterfaceTableRowStatus_Object = MibTableColumn
vlanInterfaceTableRowStatus = _VlanInterfaceTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 4, 1, 1, 11),
    _VlanInterfaceTableRowStatus_Type()
)
vlanInterfaceTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanInterfaceTableRowStatus.setStatus("current")
_NodeConfigurationBridge_ObjectIdentity = ObjectIdentity
nodeConfigurationBridge = _NodeConfigurationBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5)
)
_BridgeInterfaceTable_Object = MibTable
bridgeInterfaceTable = _BridgeInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    bridgeInterfaceTable.setStatus("current")
_BridgeInterfaceTableEntry_Object = MibTableRow
bridgeInterfaceTableEntry = _BridgeInterfaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1)
)
bridgeInterfaceTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "bridgeInterfaceTableIndex"),
)
if mibBuilder.loadTexts:
    bridgeInterfaceTableEntry.setStatus("current")


class _BridgeInterfaceTableIndex_Type(Integer32):
    """Custom type bridgeInterfaceTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BridgeInterfaceTableIndex_Type.__name__ = "Integer32"
_BridgeInterfaceTableIndex_Object = MibTableColumn
bridgeInterfaceTableIndex = _BridgeInterfaceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 1),
    _BridgeInterfaceTableIndex_Type()
)
bridgeInterfaceTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeInterfaceTableIndex.setStatus("current")


class _BridgeInterfaceTableName_Type(OctetString):
    """Custom type bridgeInterfaceTableName based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BridgeInterfaceTableName_Type.__name__ = "OctetString"
_BridgeInterfaceTableName_Object = MibTableColumn
bridgeInterfaceTableName = _BridgeInterfaceTableName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 2),
    _BridgeInterfaceTableName_Type()
)
bridgeInterfaceTableName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTableName.setStatus("current")
_BridgeInterfaceTableMac_Type = MacAddress
_BridgeInterfaceTableMac_Object = MibTableColumn
bridgeInterfaceTableMac = _BridgeInterfaceTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 3),
    _BridgeInterfaceTableMac_Type()
)
bridgeInterfaceTableMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTableMac.setStatus("current")


class _BridgeInterfaceTableAge_Type(Integer32):
    """Custom type bridgeInterfaceTableAge based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_BridgeInterfaceTableAge_Type.__name__ = "Integer32"
_BridgeInterfaceTableAge_Object = MibTableColumn
bridgeInterfaceTableAge = _BridgeInterfaceTableAge_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 4),
    _BridgeInterfaceTableAge_Type()
)
bridgeInterfaceTableAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTableAge.setStatus("current")


class _BridgeInterfaceTablePrio_Type(Integer32):
    """Custom type bridgeInterfaceTablePrio based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_BridgeInterfaceTablePrio_Type.__name__ = "Integer32"
_BridgeInterfaceTablePrio_Object = MibTableColumn
bridgeInterfaceTablePrio = _BridgeInterfaceTablePrio_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 5),
    _BridgeInterfaceTablePrio_Type()
)
bridgeInterfaceTablePrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTablePrio.setStatus("current")


class _BridgeInterfaceTableFwdDelay_Type(Integer32):
    """Custom type bridgeInterfaceTableFwdDelay based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_BridgeInterfaceTableFwdDelay_Type.__name__ = "Integer32"
_BridgeInterfaceTableFwdDelay_Object = MibTableColumn
bridgeInterfaceTableFwdDelay = _BridgeInterfaceTableFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 6),
    _BridgeInterfaceTableFwdDelay_Type()
)
bridgeInterfaceTableFwdDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTableFwdDelay.setStatus("current")


class _BridgeInterfaceTableHelloInt_Type(Integer32):
    """Custom type bridgeInterfaceTableHelloInt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_BridgeInterfaceTableHelloInt_Type.__name__ = "Integer32"
_BridgeInterfaceTableHelloInt_Object = MibTableColumn
bridgeInterfaceTableHelloInt = _BridgeInterfaceTableHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 7),
    _BridgeInterfaceTableHelloInt_Type()
)
bridgeInterfaceTableHelloInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTableHelloInt.setStatus("current")


class _BridgeInterfaceTableMaxAge_Type(Integer32):
    """Custom type bridgeInterfaceTableMaxAge based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_BridgeInterfaceTableMaxAge_Type.__name__ = "Integer32"
_BridgeInterfaceTableMaxAge_Object = MibTableColumn
bridgeInterfaceTableMaxAge = _BridgeInterfaceTableMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 8),
    _BridgeInterfaceTableMaxAge_Type()
)
bridgeInterfaceTableMaxAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTableMaxAge.setStatus("current")


class _BridgeInterfaceTableStp_Type(Integer32):
    """Custom type bridgeInterfaceTableStp based on Integer32"""
    defaultValue = 2

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


_BridgeInterfaceTableStp_Type.__name__ = "Integer32"
_BridgeInterfaceTableStp_Object = MibTableColumn
bridgeInterfaceTableStp = _BridgeInterfaceTableStp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 9),
    _BridgeInterfaceTableStp_Type()
)
bridgeInterfaceTableStp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTableStp.setStatus("current")


class _BridgeInterfaceTableComments_Type(DisplayString):
    """Custom type bridgeInterfaceTableComments based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BridgeInterfaceTableComments_Type.__name__ = "DisplayString"
_BridgeInterfaceTableComments_Object = MibTableColumn
bridgeInterfaceTableComments = _BridgeInterfaceTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 10),
    _BridgeInterfaceTableComments_Type()
)
bridgeInterfaceTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTableComments.setStatus("current")


class _BridgeInterfaceTableActive_Type(Integer32):
    """Custom type bridgeInterfaceTableActive based on Integer32"""
    defaultValue = 1

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


_BridgeInterfaceTableActive_Type.__name__ = "Integer32"
_BridgeInterfaceTableActive_Object = MibTableColumn
bridgeInterfaceTableActive = _BridgeInterfaceTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 11),
    _BridgeInterfaceTableActive_Type()
)
bridgeInterfaceTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTableActive.setStatus("current")
_BridgeInterfaceTableRowStatus_Type = RowStatus
_BridgeInterfaceTableRowStatus_Object = MibTableColumn
bridgeInterfaceTableRowStatus = _BridgeInterfaceTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 5, 1, 1, 12),
    _BridgeInterfaceTableRowStatus_Type()
)
bridgeInterfaceTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeInterfaceTableRowStatus.setStatus("current")
_NodeConfigurationIpaddress_ObjectIdentity = ObjectIdentity
nodeConfigurationIpaddress = _NodeConfigurationIpaddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6)
)
_IpAddressesTable_Object = MibTable
ipAddressesTable = _IpAddressesTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ipAddressesTable.setStatus("current")
_IpAddressesTableEntry_Object = MibTableRow
ipAddressesTableEntry = _IpAddressesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1)
)
ipAddressesTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "ipAddressesTableIndex"),
)
if mibBuilder.loadTexts:
    ipAddressesTableEntry.setStatus("current")


class _IpAddressesTableIndex_Type(Integer32):
    """Custom type ipAddressesTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IpAddressesTableIndex_Type.__name__ = "Integer32"
_IpAddressesTableIndex_Object = MibTableColumn
ipAddressesTableIndex = _IpAddressesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 1),
    _IpAddressesTableIndex_Type()
)
ipAddressesTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressesTableIndex.setStatus("current")


class _IpAddressesTableIface_Type(OctetString):
    """Custom type ipAddressesTableIface based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpAddressesTableIface_Type.__name__ = "OctetString"
_IpAddressesTableIface_Object = MibTableColumn
ipAddressesTableIface = _IpAddressesTableIface_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 2),
    _IpAddressesTableIface_Type()
)
ipAddressesTableIface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressesTableIface.setStatus("current")


class _IpAddressesTableType_Type(Integer32):
    """Custom type ipAddressesTableType based on Integer32"""
    defaultValue = 2

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
        *(("dhcp", 2),
          ("ipalias", 4),
          ("pppoe", 3),
          ("static", 1))
    )


_IpAddressesTableType_Type.__name__ = "Integer32"
_IpAddressesTableType_Object = MibTableColumn
ipAddressesTableType = _IpAddressesTableType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 3),
    _IpAddressesTableType_Type()
)
ipAddressesTableType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressesTableType.setStatus("current")
_IpAddressesTableIp_Type = IpAddress
_IpAddressesTableIp_Object = MibTableColumn
ipAddressesTableIp = _IpAddressesTableIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 4),
    _IpAddressesTableIp_Type()
)
ipAddressesTableIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressesTableIp.setStatus("current")
_IpAddressesTableNetmask_Type = IpAddress
_IpAddressesTableNetmask_Object = MibTableColumn
ipAddressesTableNetmask = _IpAddressesTableNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 5),
    _IpAddressesTableNetmask_Type()
)
ipAddressesTableNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressesTableNetmask.setStatus("current")
_IpAddressesTableBroadcast_Type = IpAddress
_IpAddressesTableBroadcast_Object = MibTableColumn
ipAddressesTableBroadcast = _IpAddressesTableBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 6),
    _IpAddressesTableBroadcast_Type()
)
ipAddressesTableBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressesTableBroadcast.setStatus("current")
_IpAddressesTableGateway_Type = IpAddress
_IpAddressesTableGateway_Object = MibTableColumn
ipAddressesTableGateway = _IpAddressesTableGateway_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 7),
    _IpAddressesTableGateway_Type()
)
ipAddressesTableGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressesTableGateway.setStatus("current")


class _IpAddressesTableRouted_Type(Integer32):
    """Custom type ipAddressesTableRouted based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nat", 2),
          ("routable", 1))
    )


_IpAddressesTableRouted_Type.__name__ = "Integer32"
_IpAddressesTableRouted_Object = MibTableColumn
ipAddressesTableRouted = _IpAddressesTableRouted_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 8),
    _IpAddressesTableRouted_Type()
)
ipAddressesTableRouted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressesTableRouted.setStatus("current")


class _IpAddressesTableComments_Type(DisplayString):
    """Custom type ipAddressesTableComments based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpAddressesTableComments_Type.__name__ = "DisplayString"
_IpAddressesTableComments_Object = MibTableColumn
ipAddressesTableComments = _IpAddressesTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 9),
    _IpAddressesTableComments_Type()
)
ipAddressesTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressesTableComments.setStatus("current")


class _IpAddressesTableActive_Type(Integer32):
    """Custom type ipAddressesTableActive based on Integer32"""
    defaultValue = 1

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


_IpAddressesTableActive_Type.__name__ = "Integer32"
_IpAddressesTableActive_Object = MibTableColumn
ipAddressesTableActive = _IpAddressesTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 10),
    _IpAddressesTableActive_Type()
)
ipAddressesTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressesTableActive.setStatus("current")
_IpAddressesTableRowStatus_Type = RowStatus
_IpAddressesTableRowStatus_Object = MibTableColumn
ipAddressesTableRowStatus = _IpAddressesTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 6, 1, 1, 11),
    _IpAddressesTableRowStatus_Type()
)
ipAddressesTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipAddressesTableRowStatus.setStatus("current")
_NodeConfigurationNetwork_ObjectIdentity = ObjectIdentity
nodeConfigurationNetwork = _NodeConfigurationNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 7)
)
_NetworkPrimaryDns_Type = IpAddress
_NetworkPrimaryDns_Object = MibScalar
networkPrimaryDns = _NetworkPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 7, 1),
    _NetworkPrimaryDns_Type()
)
networkPrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPrimaryDns.setStatus("current")
_NetworkSecondaryDns_Type = IpAddress
_NetworkSecondaryDns_Object = MibScalar
networkSecondaryDns = _NetworkSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 7, 2),
    _NetworkSecondaryDns_Type()
)
networkSecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkSecondaryDns.setStatus("current")


class _NetworkDomain_Type(OctetString):
    """Custom type networkDomain based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NetworkDomain_Type.__name__ = "OctetString"
_NetworkDomain_Object = MibScalar
networkDomain = _NetworkDomain_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 7, 3),
    _NetworkDomain_Type()
)
networkDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkDomain.setStatus("current")
_NodeConfigurationSyslog_ObjectIdentity = ObjectIdentity
nodeConfigurationSyslog = _NodeConfigurationSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 8)
)


class _SyslogActive_Type(Integer32):
    """Custom type syslogActive based on Integer32"""
    defaultValue = 1

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


_SyslogActive_Type.__name__ = "Integer32"
_SyslogActive_Object = MibScalar
syslogActive = _SyslogActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 8, 1),
    _SyslogActive_Type()
)
syslogActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogActive.setStatus("current")


class _SyslogKlog_Type(Integer32):
    """Custom type syslogKlog based on Integer32"""
    defaultValue = 2

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


_SyslogKlog_Type.__name__ = "Integer32"
_SyslogKlog_Object = MibScalar
syslogKlog = _SyslogKlog_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 8, 2),
    _SyslogKlog_Type()
)
syslogKlog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogKlog.setStatus("current")


class _SyslogLevel_Type(Integer32):
    """Custom type syslogLevel based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SyslogLevel_Type.__name__ = "Integer32"
_SyslogLevel_Object = MibScalar
syslogLevel = _SyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 8, 3),
    _SyslogLevel_Type()
)
syslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogLevel.setStatus("current")


class _SyslogRemoteActive_Type(Integer32):
    """Custom type syslogRemoteActive based on Integer32"""
    defaultValue = 2

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


_SyslogRemoteActive_Type.__name__ = "Integer32"
_SyslogRemoteActive_Object = MibScalar
syslogRemoteActive = _SyslogRemoteActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 8, 4),
    _SyslogRemoteActive_Type()
)
syslogRemoteActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogRemoteActive.setStatus("current")


class _SyslogRemoteAddress_Type(OctetString):
    """Custom type syslogRemoteAddress based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SyslogRemoteAddress_Type.__name__ = "OctetString"
_SyslogRemoteAddress_Object = MibScalar
syslogRemoteAddress = _SyslogRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 8, 5),
    _SyslogRemoteAddress_Type()
)
syslogRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogRemoteAddress.setStatus("current")
_NodeConfigurationOlsr_ObjectIdentity = ObjectIdentity
nodeConfigurationOlsr = _NodeConfigurationOlsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9)
)


class _OlsrActive_Type(Integer32):
    """Custom type olsrActive based on Integer32"""
    defaultValue = 1

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


_OlsrActive_Type.__name__ = "Integer32"
_OlsrActive_Object = MibScalar
olsrActive = _OlsrActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 1),
    _OlsrActive_Type()
)
olsrActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrActive.setStatus("current")


class _OlsrTosValue_Type(Integer32):
    """Custom type olsrTosValue based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_OlsrTosValue_Type.__name__ = "Integer32"
_OlsrTosValue_Object = MibScalar
olsrTosValue = _OlsrTosValue_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 2),
    _OlsrTosValue_Type()
)
olsrTosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrTosValue.setStatus("current")


class _OlsrWillingnessActive_Type(Integer32):
    """Custom type olsrWillingnessActive based on Integer32"""
    defaultValue = 1

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


_OlsrWillingnessActive_Type.__name__ = "Integer32"
_OlsrWillingnessActive_Object = MibScalar
olsrWillingnessActive = _OlsrWillingnessActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 3),
    _OlsrWillingnessActive_Type()
)
olsrWillingnessActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrWillingnessActive.setStatus("current")


class _OlsrWillingness_Type(Integer32):
    """Custom type olsrWillingness based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OlsrWillingness_Type.__name__ = "Integer32"
_OlsrWillingness_Object = MibScalar
olsrWillingness = _OlsrWillingness_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 4),
    _OlsrWillingness_Type()
)
olsrWillingness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrWillingness.setStatus("current")


class _OlsrHysteresisActive_Type(Integer32):
    """Custom type olsrHysteresisActive based on Integer32"""
    defaultValue = 2

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


_OlsrHysteresisActive_Type.__name__ = "Integer32"
_OlsrHysteresisActive_Object = MibScalar
olsrHysteresisActive = _OlsrHysteresisActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 5),
    _OlsrHysteresisActive_Type()
)
olsrHysteresisActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrHysteresisActive.setStatus("current")


class _OlsrHysteresisScaling_Type(OctetString):
    """Custom type olsrHysteresisScaling based on OctetString"""
    defaultValue = OctetString("0.50")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrHysteresisScaling_Type.__name__ = "OctetString"
_OlsrHysteresisScaling_Object = MibScalar
olsrHysteresisScaling = _OlsrHysteresisScaling_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 6),
    _OlsrHysteresisScaling_Type()
)
olsrHysteresisScaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrHysteresisScaling.setStatus("current")


class _OlsrHysteresisThrHigh_Type(OctetString):
    """Custom type olsrHysteresisThrHigh based on OctetString"""
    defaultValue = OctetString("0.80")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrHysteresisThrHigh_Type.__name__ = "OctetString"
_OlsrHysteresisThrHigh_Object = MibScalar
olsrHysteresisThrHigh = _OlsrHysteresisThrHigh_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 7),
    _OlsrHysteresisThrHigh_Type()
)
olsrHysteresisThrHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrHysteresisThrHigh.setStatus("current")


class _OlsrHysteresisThrLow_Type(OctetString):
    """Custom type olsrHysteresisThrLow based on OctetString"""
    defaultValue = OctetString("0.30")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrHysteresisThrLow_Type.__name__ = "OctetString"
_OlsrHysteresisThrLow_Object = MibScalar
olsrHysteresisThrLow = _OlsrHysteresisThrLow_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 8),
    _OlsrHysteresisThrLow_Type()
)
olsrHysteresisThrLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrHysteresisThrLow.setStatus("current")


class _OlsrLinkQualityType_Type(Integer32):
    """Custom type olsrLinkQualityType based on Integer32"""
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
        *(("disable", 0),
          ("useformpr", 1),
          ("useformprandrouting", 2))
    )


_OlsrLinkQualityType_Type.__name__ = "Integer32"
_OlsrLinkQualityType_Object = MibScalar
olsrLinkQualityType = _OlsrLinkQualityType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 9),
    _OlsrLinkQualityType_Type()
)
olsrLinkQualityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrLinkQualityType.setStatus("current")


class _OlsrLinkQualitySize_Type(Integer32):
    """Custom type olsrLinkQualitySize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 128),
    )


_OlsrLinkQualitySize_Type.__name__ = "Integer32"
_OlsrLinkQualitySize_Object = MibScalar
olsrLinkQualitySize = _OlsrLinkQualitySize_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 10),
    _OlsrLinkQualitySize_Type()
)
olsrLinkQualitySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrLinkQualitySize.setStatus("current")


class _OlsrPollRate_Type(OctetString):
    """Custom type olsrPollRate based on OctetString"""
    defaultValue = OctetString("0.05")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrPollRate_Type.__name__ = "OctetString"
_OlsrPollRate_Object = MibScalar
olsrPollRate = _OlsrPollRate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 11),
    _OlsrPollRate_Type()
)
olsrPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrPollRate.setStatus("current")


class _OlsrTcType_Type(Integer32):
    """Custom type olsrTcType based on Integer32"""
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
        *(("sendallneighbors", 2),
          ("sendonlymprselectors", 0),
          ("sendonlymprselectorsandmprs", 1))
    )


_OlsrTcType_Type.__name__ = "Integer32"
_OlsrTcType_Object = MibScalar
olsrTcType = _OlsrTcType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 12),
    _OlsrTcType_Type()
)
olsrTcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrTcType.setStatus("current")


class _OlsrMpr_Type(Integer32):
    """Custom type olsrMpr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OlsrMpr_Type.__name__ = "Integer32"
_OlsrMpr_Object = MibScalar
olsrMpr = _OlsrMpr_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 13),
    _OlsrMpr_Type()
)
olsrMpr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrMpr.setStatus("current")


class _OlsrSharedKey_Type(DisplayString):
    """Custom type olsrSharedKey based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrSharedKey_Type.__name__ = "DisplayString"
_OlsrSharedKey_Object = MibScalar
olsrSharedKey = _OlsrSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 14),
    _OlsrSharedKey_Type()
)
olsrSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olsrSharedKey.setStatus("current")
_OlsrInterfaceTable_Object = MibTable
olsrInterfaceTable = _OlsrInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15)
)
if mibBuilder.loadTexts:
    olsrInterfaceTable.setStatus("current")
_OlsrInterfaceTableEntry_Object = MibTableRow
olsrInterfaceTableEntry = _OlsrInterfaceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1)
)
olsrInterfaceTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "olsrInterfaceTableIndex"),
)
if mibBuilder.loadTexts:
    olsrInterfaceTableEntry.setStatus("current")


class _OlsrInterfaceTableIndex_Type(Integer32):
    """Custom type olsrInterfaceTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_OlsrInterfaceTableIndex_Type.__name__ = "Integer32"
_OlsrInterfaceTableIndex_Object = MibTableColumn
olsrInterfaceTableIndex = _OlsrInterfaceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 1),
    _OlsrInterfaceTableIndex_Type()
)
olsrInterfaceTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrInterfaceTableIndex.setStatus("current")


class _OlsrInterfaceTableIface_Type(OctetString):
    """Custom type olsrInterfaceTableIface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrInterfaceTableIface_Type.__name__ = "OctetString"
_OlsrInterfaceTableIface_Object = MibTableColumn
olsrInterfaceTableIface = _OlsrInterfaceTableIface_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 2),
    _OlsrInterfaceTableIface_Type()
)
olsrInterfaceTableIface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableIface.setStatus("current")


class _OlsrInterfaceTableHelloInterval_Type(OctetString):
    """Custom type olsrInterfaceTableHelloInterval based on OctetString"""
    defaultValue = OctetString("2.0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrInterfaceTableHelloInterval_Type.__name__ = "OctetString"
_OlsrInterfaceTableHelloInterval_Object = MibTableColumn
olsrInterfaceTableHelloInterval = _OlsrInterfaceTableHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 3),
    _OlsrInterfaceTableHelloInterval_Type()
)
olsrInterfaceTableHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableHelloInterval.setStatus("current")


class _OlsrInterfaceTableHelloValidity_Type(OctetString):
    """Custom type olsrInterfaceTableHelloValidity based on OctetString"""
    defaultValue = OctetString("30.0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrInterfaceTableHelloValidity_Type.__name__ = "OctetString"
_OlsrInterfaceTableHelloValidity_Object = MibTableColumn
olsrInterfaceTableHelloValidity = _OlsrInterfaceTableHelloValidity_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 4),
    _OlsrInterfaceTableHelloValidity_Type()
)
olsrInterfaceTableHelloValidity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableHelloValidity.setStatus("current")


class _OlsrInterfaceTableTcInterval_Type(OctetString):
    """Custom type olsrInterfaceTableTcInterval based on OctetString"""
    defaultValue = OctetString("5.0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrInterfaceTableTcInterval_Type.__name__ = "OctetString"
_OlsrInterfaceTableTcInterval_Object = MibTableColumn
olsrInterfaceTableTcInterval = _OlsrInterfaceTableTcInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 5),
    _OlsrInterfaceTableTcInterval_Type()
)
olsrInterfaceTableTcInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableTcInterval.setStatus("current")


class _OlsrInterfaceTableTcValidity_Type(OctetString):
    """Custom type olsrInterfaceTableTcValidity based on OctetString"""
    defaultValue = OctetString("60.0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrInterfaceTableTcValidity_Type.__name__ = "OctetString"
_OlsrInterfaceTableTcValidity_Object = MibTableColumn
olsrInterfaceTableTcValidity = _OlsrInterfaceTableTcValidity_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 6),
    _OlsrInterfaceTableTcValidity_Type()
)
olsrInterfaceTableTcValidity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableTcValidity.setStatus("current")


class _OlsrInterfaceTableMidInterval_Type(OctetString):
    """Custom type olsrInterfaceTableMidInterval based on OctetString"""
    defaultValue = OctetString("5.0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrInterfaceTableMidInterval_Type.__name__ = "OctetString"
_OlsrInterfaceTableMidInterval_Object = MibTableColumn
olsrInterfaceTableMidInterval = _OlsrInterfaceTableMidInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 7),
    _OlsrInterfaceTableMidInterval_Type()
)
olsrInterfaceTableMidInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableMidInterval.setStatus("current")


class _OlsrInterfaceTableMidValidity_Type(OctetString):
    """Custom type olsrInterfaceTableMidValidity based on OctetString"""
    defaultValue = OctetString("60.0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrInterfaceTableMidValidity_Type.__name__ = "OctetString"
_OlsrInterfaceTableMidValidity_Object = MibTableColumn
olsrInterfaceTableMidValidity = _OlsrInterfaceTableMidValidity_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 8),
    _OlsrInterfaceTableMidValidity_Type()
)
olsrInterfaceTableMidValidity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableMidValidity.setStatus("current")


class _OlsrInterfaceTableHnaInterval_Type(OctetString):
    """Custom type olsrInterfaceTableHnaInterval based on OctetString"""
    defaultValue = OctetString("5.0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrInterfaceTableHnaInterval_Type.__name__ = "OctetString"
_OlsrInterfaceTableHnaInterval_Object = MibTableColumn
olsrInterfaceTableHnaInterval = _OlsrInterfaceTableHnaInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 9),
    _OlsrInterfaceTableHnaInterval_Type()
)
olsrInterfaceTableHnaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableHnaInterval.setStatus("current")


class _OlsrInterfaceTableHnaValidity_Type(OctetString):
    """Custom type olsrInterfaceTableHnaValidity based on OctetString"""
    defaultValue = OctetString("60.0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrInterfaceTableHnaValidity_Type.__name__ = "OctetString"
_OlsrInterfaceTableHnaValidity_Object = MibTableColumn
olsrInterfaceTableHnaValidity = _OlsrInterfaceTableHnaValidity_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 10),
    _OlsrInterfaceTableHnaValidity_Type()
)
olsrInterfaceTableHnaValidity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableHnaValidity.setStatus("current")


class _OlsrInterfaceTableComments_Type(DisplayString):
    """Custom type olsrInterfaceTableComments based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrInterfaceTableComments_Type.__name__ = "DisplayString"
_OlsrInterfaceTableComments_Object = MibTableColumn
olsrInterfaceTableComments = _OlsrInterfaceTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 11),
    _OlsrInterfaceTableComments_Type()
)
olsrInterfaceTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableComments.setStatus("current")


class _OlsrInterfaceTableActive_Type(Integer32):
    """Custom type olsrInterfaceTableActive based on Integer32"""
    defaultValue = 1

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


_OlsrInterfaceTableActive_Type.__name__ = "Integer32"
_OlsrInterfaceTableActive_Object = MibTableColumn
olsrInterfaceTableActive = _OlsrInterfaceTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 12),
    _OlsrInterfaceTableActive_Type()
)
olsrInterfaceTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableActive.setStatus("current")
_OlsrInterfaceTableRowStatus_Type = RowStatus
_OlsrInterfaceTableRowStatus_Object = MibTableColumn
olsrInterfaceTableRowStatus = _OlsrInterfaceTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 9, 15, 1, 13),
    _OlsrInterfaceTableRowStatus_Type()
)
olsrInterfaceTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrInterfaceTableRowStatus.setStatus("current")
_NodeConfigurationRoute_ObjectIdentity = ObjectIdentity
nodeConfigurationRoute = _NodeConfigurationRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10)
)
_RouteTable_Object = MibTable
routeTable = _RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    routeTable.setStatus("current")
_RouteTableEntry_Object = MibTableRow
routeTableEntry = _RouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1, 1)
)
routeTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "routeTableIndex"),
)
if mibBuilder.loadTexts:
    routeTableEntry.setStatus("current")


class _RouteTableIndex_Type(Integer32):
    """Custom type routeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_RouteTableIndex_Type.__name__ = "Integer32"
_RouteTableIndex_Object = MibTableColumn
routeTableIndex = _RouteTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1, 1, 1),
    _RouteTableIndex_Type()
)
routeTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    routeTableIndex.setStatus("current")
_RouteTableSubnet_Type = IpAddress
_RouteTableSubnet_Object = MibTableColumn
routeTableSubnet = _RouteTableSubnet_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1, 1, 2),
    _RouteTableSubnet_Type()
)
routeTableSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    routeTableSubnet.setStatus("current")
_RouteTableNetmask_Type = IpAddress
_RouteTableNetmask_Object = MibTableColumn
routeTableNetmask = _RouteTableNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1, 1, 3),
    _RouteTableNetmask_Type()
)
routeTableNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    routeTableNetmask.setStatus("current")
_RouteTableGateway_Type = IpAddress
_RouteTableGateway_Object = MibTableColumn
routeTableGateway = _RouteTableGateway_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1, 1, 4),
    _RouteTableGateway_Type()
)
routeTableGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    routeTableGateway.setStatus("current")


class _RouteTableDevice_Type(OctetString):
    """Custom type routeTableDevice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RouteTableDevice_Type.__name__ = "OctetString"
_RouteTableDevice_Object = MibTableColumn
routeTableDevice = _RouteTableDevice_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1, 1, 5),
    _RouteTableDevice_Type()
)
routeTableDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    routeTableDevice.setStatus("current")


class _RouteTableDirect_Type(Integer32):
    """Custom type routeTableDirect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("indirect", 2))
    )


_RouteTableDirect_Type.__name__ = "Integer32"
_RouteTableDirect_Object = MibTableColumn
routeTableDirect = _RouteTableDirect_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1, 1, 6),
    _RouteTableDirect_Type()
)
routeTableDirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    routeTableDirect.setStatus("current")


class _RouteTableComments_Type(DisplayString):
    """Custom type routeTableComments based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RouteTableComments_Type.__name__ = "DisplayString"
_RouteTableComments_Object = MibTableColumn
routeTableComments = _RouteTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1, 1, 7),
    _RouteTableComments_Type()
)
routeTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    routeTableComments.setStatus("current")


class _RouteTableActive_Type(Integer32):
    """Custom type routeTableActive based on Integer32"""
    defaultValue = 1

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


_RouteTableActive_Type.__name__ = "Integer32"
_RouteTableActive_Object = MibTableColumn
routeTableActive = _RouteTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1, 1, 8),
    _RouteTableActive_Type()
)
routeTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    routeTableActive.setStatus("current")
_RouteTableRowStatus_Type = RowStatus
_RouteTableRowStatus_Object = MibTableColumn
routeTableRowStatus = _RouteTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 10, 1, 1, 9),
    _RouteTableRowStatus_Type()
)
routeTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    routeTableRowStatus.setStatus("current")
_NodeConfigurationNtp_ObjectIdentity = ObjectIdentity
nodeConfigurationNtp = _NodeConfigurationNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11)
)


class _NtpActive_Type(Integer32):
    """Custom type ntpActive based on Integer32"""
    defaultValue = 1

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


_NtpActive_Type.__name__ = "Integer32"
_NtpActive_Object = MibScalar
ntpActive = _NtpActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 1),
    _NtpActive_Type()
)
ntpActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpActive.setStatus("current")


class _NtpTimezone_Type(DisplayString):
    """Custom type ntpTimezone based on DisplayString"""
    defaultValue = OctetString("337")


_NtpTimezone_Object = MibScalar
ntpTimezone = _NtpTimezone_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 2),
    _NtpTimezone_Type()
)
ntpTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimezone.setStatus("current")
_NtpTable_Object = MibTable
ntpTable = _NtpTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 3)
)
if mibBuilder.loadTexts:
    ntpTable.setStatus("current")
_NtpTableEntry_Object = MibTableRow
ntpTableEntry = _NtpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 3, 1)
)
ntpTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "ntpTableIndex"),
)
if mibBuilder.loadTexts:
    ntpTableEntry.setStatus("current")


class _NtpTableIndex_Type(Integer32):
    """Custom type ntpTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_NtpTableIndex_Type.__name__ = "Integer32"
_NtpTableIndex_Object = MibTableColumn
ntpTableIndex = _NtpTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 3, 1, 1),
    _NtpTableIndex_Type()
)
ntpTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpTableIndex.setStatus("current")


class _NtpTableServer_Type(OctetString):
    """Custom type ntpTableServer based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtpTableServer_Type.__name__ = "OctetString"
_NtpTableServer_Object = MibTableColumn
ntpTableServer = _NtpTableServer_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 3, 1, 2),
    _NtpTableServer_Type()
)
ntpTableServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpTableServer.setStatus("current")


class _NtpTableMinPoll_Type(Integer32):
    """Custom type ntpTableMinPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_NtpTableMinPoll_Type.__name__ = "Integer32"
_NtpTableMinPoll_Object = MibTableColumn
ntpTableMinPoll = _NtpTableMinPoll_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 3, 1, 3),
    _NtpTableMinPoll_Type()
)
ntpTableMinPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpTableMinPoll.setStatus("current")


class _NtpTableMaxPoll_Type(Integer32):
    """Custom type ntpTableMaxPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NtpTableMaxPoll_Type.__name__ = "Integer32"
_NtpTableMaxPoll_Object = MibTableColumn
ntpTableMaxPoll = _NtpTableMaxPoll_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 3, 1, 4),
    _NtpTableMaxPoll_Type()
)
ntpTableMaxPoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpTableMaxPoll.setStatus("current")


class _NtpTableComments_Type(DisplayString):
    """Custom type ntpTableComments based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtpTableComments_Type.__name__ = "DisplayString"
_NtpTableComments_Object = MibTableColumn
ntpTableComments = _NtpTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 3, 1, 5),
    _NtpTableComments_Type()
)
ntpTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpTableComments.setStatus("current")


class _NtpTableActive_Type(Integer32):
    """Custom type ntpTableActive based on Integer32"""
    defaultValue = 1

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


_NtpTableActive_Type.__name__ = "Integer32"
_NtpTableActive_Object = MibTableColumn
ntpTableActive = _NtpTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 3, 1, 6),
    _NtpTableActive_Type()
)
ntpTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpTableActive.setStatus("current")
_NtpTableRowStatus_Type = RowStatus
_NtpTableRowStatus_Object = MibTableColumn
ntpTableRowStatus = _NtpTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 11, 3, 1, 7),
    _NtpTableRowStatus_Type()
)
ntpTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpTableRowStatus.setStatus("current")
_NodeConfigurationDhcpd_ObjectIdentity = ObjectIdentity
nodeConfigurationDhcpd = _NodeConfigurationDhcpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12)
)
_DhcpdTable_Object = MibTable
dhcpdTable = _DhcpdTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    dhcpdTable.setStatus("current")
_DhcpdTableEntry_Object = MibTableRow
dhcpdTableEntry = _DhcpdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1)
)
dhcpdTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "dhcpdTableIndex"),
)
if mibBuilder.loadTexts:
    dhcpdTableEntry.setStatus("current")


class _DhcpdTableIndex_Type(Integer32):
    """Custom type dhcpdTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DhcpdTableIndex_Type.__name__ = "Integer32"
_DhcpdTableIndex_Object = MibTableColumn
dhcpdTableIndex = _DhcpdTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 1),
    _DhcpdTableIndex_Type()
)
dhcpdTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpdTableIndex.setStatus("current")


class _DhcpdTableIface_Type(OctetString):
    """Custom type dhcpdTableIface based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DhcpdTableIface_Type.__name__ = "OctetString"
_DhcpdTableIface_Object = MibTableColumn
dhcpdTableIface = _DhcpdTableIface_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 2),
    _DhcpdTableIface_Type()
)
dhcpdTableIface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableIface.setStatus("current")
_DhcpdTableSubnet_Type = IpAddress
_DhcpdTableSubnet_Object = MibTableColumn
dhcpdTableSubnet = _DhcpdTableSubnet_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 3),
    _DhcpdTableSubnet_Type()
)
dhcpdTableSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableSubnet.setStatus("current")
_DhcpdTableNetstart_Type = IpAddress
_DhcpdTableNetstart_Object = MibTableColumn
dhcpdTableNetstart = _DhcpdTableNetstart_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 4),
    _DhcpdTableNetstart_Type()
)
dhcpdTableNetstart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableNetstart.setStatus("current")
_DhcpdTableNetend_Type = IpAddress
_DhcpdTableNetend_Object = MibTableColumn
dhcpdTableNetend = _DhcpdTableNetend_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 5),
    _DhcpdTableNetend_Type()
)
dhcpdTableNetend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableNetend.setStatus("current")
_DhcpdTableNetmask_Type = IpAddress
_DhcpdTableNetmask_Object = MibTableColumn
dhcpdTableNetmask = _DhcpdTableNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 6),
    _DhcpdTableNetmask_Type()
)
dhcpdTableNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableNetmask.setStatus("current")


class _DhcpdTableMaxLease_Type(Integer32):
    """Custom type dhcpdTableMaxLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 864000),
    )


_DhcpdTableMaxLease_Type.__name__ = "Integer32"
_DhcpdTableMaxLease_Object = MibTableColumn
dhcpdTableMaxLease = _DhcpdTableMaxLease_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 7),
    _DhcpdTableMaxLease_Type()
)
dhcpdTableMaxLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableMaxLease.setStatus("current")


class _DhcpdTableLease_Type(Integer32):
    """Custom type dhcpdTableLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 864000),
    )


_DhcpdTableLease_Type.__name__ = "Integer32"
_DhcpdTableLease_Object = MibTableColumn
dhcpdTableLease = _DhcpdTableLease_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 8),
    _DhcpdTableLease_Type()
)
dhcpdTableLease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableLease.setStatus("current")


class _DhcpdTableDomain_Type(OctetString):
    """Custom type dhcpdTableDomain based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DhcpdTableDomain_Type.__name__ = "OctetString"
_DhcpdTableDomain_Object = MibTableColumn
dhcpdTableDomain = _DhcpdTableDomain_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 9),
    _DhcpdTableDomain_Type()
)
dhcpdTableDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableDomain.setStatus("current")
_DhcpdTableDns_Type = IpAddress
_DhcpdTableDns_Object = MibTableColumn
dhcpdTableDns = _DhcpdTableDns_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 10),
    _DhcpdTableDns_Type()
)
dhcpdTableDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableDns.setStatus("current")
_DhcpdTableRouter_Type = IpAddress
_DhcpdTableRouter_Object = MibTableColumn
dhcpdTableRouter = _DhcpdTableRouter_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 11),
    _DhcpdTableRouter_Type()
)
dhcpdTableRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableRouter.setStatus("current")


class _DhcpdTableComments_Type(DisplayString):
    """Custom type dhcpdTableComments based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DhcpdTableComments_Type.__name__ = "DisplayString"
_DhcpdTableComments_Object = MibTableColumn
dhcpdTableComments = _DhcpdTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 12),
    _DhcpdTableComments_Type()
)
dhcpdTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableComments.setStatus("current")


class _DhcpdTableActive_Type(Integer32):
    """Custom type dhcpdTableActive based on Integer32"""
    defaultValue = 1

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


_DhcpdTableActive_Type.__name__ = "Integer32"
_DhcpdTableActive_Object = MibTableColumn
dhcpdTableActive = _DhcpdTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 13),
    _DhcpdTableActive_Type()
)
dhcpdTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableActive.setStatus("current")
_DhcpdTableRowStatus_Type = RowStatus
_DhcpdTableRowStatus_Object = MibTableColumn
dhcpdTableRowStatus = _DhcpdTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 1, 1, 14),
    _DhcpdTableRowStatus_Type()
)
dhcpdTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpdTableRowStatus.setStatus("current")


class _DhcpdActive_Type(Integer32):
    """Custom type dhcpdActive based on Integer32"""
    defaultValue = 1

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


_DhcpdActive_Type.__name__ = "Integer32"
_DhcpdActive_Object = MibScalar
dhcpdActive = _DhcpdActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 2),
    _DhcpdActive_Type()
)
dhcpdActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpdActive.setStatus("current")


class _DhcpClientExecute_Type(Integer32):
    """Custom type dhcpClientExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DhcpClientExecute_Type.__name__ = "Integer32"
_DhcpClientExecute_Object = MibScalar
dhcpClientExecute = _DhcpClientExecute_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 3),
    _DhcpClientExecute_Type()
)
dhcpClientExecute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientExecute.setStatus("current")
_DhcpClientTable_Object = MibTable
dhcpClientTable = _DhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 4)
)
if mibBuilder.loadTexts:
    dhcpClientTable.setStatus("current")
_DhcpClientTableEntry_Object = MibTableRow
dhcpClientTableEntry = _DhcpClientTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 4, 1)
)
dhcpClientTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "dhcpClientTableIndex"),
)
if mibBuilder.loadTexts:
    dhcpClientTableEntry.setStatus("current")


class _DhcpClientTableIndex_Type(Integer32):
    """Custom type dhcpClientTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_DhcpClientTableIndex_Type.__name__ = "Integer32"
_DhcpClientTableIndex_Object = MibTableColumn
dhcpClientTableIndex = _DhcpClientTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 4, 1, 1),
    _DhcpClientTableIndex_Type()
)
dhcpClientTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpClientTableIndex.setStatus("current")
_DhcpClientTableIp_Type = IpAddress
_DhcpClientTableIp_Object = MibTableColumn
dhcpClientTableIp = _DhcpClientTableIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 4, 1, 2),
    _DhcpClientTableIp_Type()
)
dhcpClientTableIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientTableIp.setStatus("current")
_DhcpClientTableMac_Type = MacAddress
_DhcpClientTableMac_Object = MibTableColumn
dhcpClientTableMac = _DhcpClientTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 4, 1, 3),
    _DhcpClientTableMac_Type()
)
dhcpClientTableMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientTableMac.setStatus("current")
_DhcpClientTableHostname_Type = DisplayString
_DhcpClientTableHostname_Object = MibTableColumn
dhcpClientTableHostname = _DhcpClientTableHostname_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 12, 4, 1, 4),
    _DhcpClientTableHostname_Type()
)
dhcpClientTableHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientTableHostname.setStatus("current")
_NodeConfigurationDns_ObjectIdentity = ObjectIdentity
nodeConfigurationDns = _NodeConfigurationDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13)
)


class _DnsActive_Type(Integer32):
    """Custom type dnsActive based on Integer32"""
    defaultValue = 1

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


_DnsActive_Type.__name__ = "Integer32"
_DnsActive_Object = MibScalar
dnsActive = _DnsActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 1),
    _DnsActive_Type()
)
dnsActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsActive.setStatus("current")


class _DnsDomainNeeded_Type(Integer32):
    """Custom type dnsDomainNeeded based on Integer32"""
    defaultValue = 2

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


_DnsDomainNeeded_Type.__name__ = "Integer32"
_DnsDomainNeeded_Object = MibScalar
dnsDomainNeeded = _DnsDomainNeeded_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 2),
    _DnsDomainNeeded_Type()
)
dnsDomainNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDomainNeeded.setStatus("current")


class _DnsBogusPriv_Type(Integer32):
    """Custom type dnsBogusPriv based on Integer32"""
    defaultValue = 2

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


_DnsBogusPriv_Type.__name__ = "Integer32"
_DnsBogusPriv_Object = MibScalar
dnsBogusPriv = _DnsBogusPriv_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 3),
    _DnsBogusPriv_Type()
)
dnsBogusPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsBogusPriv.setStatus("current")


class _DnsFilterWin2k_Type(Integer32):
    """Custom type dnsFilterWin2k based on Integer32"""
    defaultValue = 1

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


_DnsFilterWin2k_Type.__name__ = "Integer32"
_DnsFilterWin2k_Object = MibScalar
dnsFilterWin2k = _DnsFilterWin2k_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 4),
    _DnsFilterWin2k_Type()
)
dnsFilterWin2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsFilterWin2k.setStatus("current")


class _DnsStrictOrder_Type(Integer32):
    """Custom type dnsStrictOrder based on Integer32"""
    defaultValue = 1

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


_DnsStrictOrder_Type.__name__ = "Integer32"
_DnsStrictOrder_Object = MibScalar
dnsStrictOrder = _DnsStrictOrder_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 5),
    _DnsStrictOrder_Type()
)
dnsStrictOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsStrictOrder.setStatus("current")
_DnsTable_Object = MibTable
dnsTable = _DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 6)
)
if mibBuilder.loadTexts:
    dnsTable.setStatus("current")
_DnsTableEntry_Object = MibTableRow
dnsTableEntry = _DnsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 6, 1)
)
dnsTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "dnsTableIndex"),
)
if mibBuilder.loadTexts:
    dnsTableEntry.setStatus("current")


class _DnsTableIndex_Type(Integer32):
    """Custom type dnsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DnsTableIndex_Type.__name__ = "Integer32"
_DnsTableIndex_Object = MibTableColumn
dnsTableIndex = _DnsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 6, 1, 1),
    _DnsTableIndex_Type()
)
dnsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsTableIndex.setStatus("current")


class _DnsTableDns_Type(OctetString):
    """Custom type dnsTableDns based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DnsTableDns_Type.__name__ = "OctetString"
_DnsTableDns_Object = MibTableColumn
dnsTableDns = _DnsTableDns_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 6, 1, 2),
    _DnsTableDns_Type()
)
dnsTableDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTableDns.setStatus("current")
_DnsTableIpaddress_Type = IpAddress
_DnsTableIpaddress_Object = MibTableColumn
dnsTableIpaddress = _DnsTableIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 6, 1, 3),
    _DnsTableIpaddress_Type()
)
dnsTableIpaddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTableIpaddress.setStatus("current")


class _DnsTableComments_Type(DisplayString):
    """Custom type dnsTableComments based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DnsTableComments_Type.__name__ = "DisplayString"
_DnsTableComments_Object = MibTableColumn
dnsTableComments = _DnsTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 6, 1, 4),
    _DnsTableComments_Type()
)
dnsTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTableComments.setStatus("current")


class _DnsTableActive_Type(Integer32):
    """Custom type dnsTableActive based on Integer32"""
    defaultValue = 1

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


_DnsTableActive_Type.__name__ = "Integer32"
_DnsTableActive_Object = MibTableColumn
dnsTableActive = _DnsTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 6, 1, 5),
    _DnsTableActive_Type()
)
dnsTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTableActive.setStatus("current")
_DnsTableRowStatus_Type = RowStatus
_DnsTableRowStatus_Object = MibTableColumn
dnsTableRowStatus = _DnsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 13, 6, 1, 6),
    _DnsTableRowStatus_Type()
)
dnsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTableRowStatus.setStatus("current")
_NodeConfigurationTopology_ObjectIdentity = ObjectIdentity
nodeConfigurationTopology = _NodeConfigurationTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 14)
)
_TopologyTable_Object = MibTable
topologyTable = _TopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 14, 1)
)
if mibBuilder.loadTexts:
    topologyTable.setStatus("current")
_TopologyTableEntry_Object = MibTableRow
topologyTableEntry = _TopologyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 14, 1, 1)
)
topologyTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "topologyTableIndex"),
)
if mibBuilder.loadTexts:
    topologyTableEntry.setStatus("current")


class _TopologyTableIndex_Type(Integer32):
    """Custom type topologyTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_TopologyTableIndex_Type.__name__ = "Integer32"
_TopologyTableIndex_Object = MibTableColumn
topologyTableIndex = _TopologyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 14, 1, 1, 1),
    _TopologyTableIndex_Type()
)
topologyTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    topologyTableIndex.setStatus("current")


class _TopologyTableSource_Type(OctetString):
    """Custom type topologyTableSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 17),
    )


_TopologyTableSource_Type.__name__ = "OctetString"
_TopologyTableSource_Object = MibTableColumn
topologyTableSource = _TopologyTableSource_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 14, 1, 1, 2),
    _TopologyTableSource_Type()
)
topologyTableSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyTableSource.setStatus("current")


class _TopologyTableDestination_Type(OctetString):
    """Custom type topologyTableDestination based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 17),
    )


_TopologyTableDestination_Type.__name__ = "OctetString"
_TopologyTableDestination_Object = MibTableColumn
topologyTableDestination = _TopologyTableDestination_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 14, 1, 1, 3),
    _TopologyTableDestination_Type()
)
topologyTableDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyTableDestination.setStatus("current")


class _TopologyTableLabel_Type(OctetString):
    """Custom type topologyTableLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TopologyTableLabel_Type.__name__ = "OctetString"
_TopologyTableLabel_Object = MibTableColumn
topologyTableLabel = _TopologyTableLabel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 14, 1, 1, 4),
    _TopologyTableLabel_Type()
)
topologyTableLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyTableLabel.setStatus("current")


class _TopologyTableStyle_Type(OctetString):
    """Custom type topologyTableStyle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TopologyTableStyle_Type.__name__ = "OctetString"
_TopologyTableStyle_Object = MibTableColumn
topologyTableStyle = _TopologyTableStyle_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 14, 1, 1, 5),
    _TopologyTableStyle_Type()
)
topologyTableStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyTableStyle.setStatus("current")
_NodeConfigurationFirewall_ObjectIdentity = ObjectIdentity
nodeConfigurationFirewall = _NodeConfigurationFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15)
)


class _FirewallActive_Type(Integer32):
    """Custom type firewallActive based on Integer32"""
    defaultValue = 2

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


_FirewallActive_Type.__name__ = "Integer32"
_FirewallActive_Object = MibScalar
firewallActive = _FirewallActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 1),
    _FirewallActive_Type()
)
firewallActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallActive.setStatus("current")
_FirewallTable_Object = MibTable
firewallTable = _FirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2)
)
if mibBuilder.loadTexts:
    firewallTable.setStatus("current")
_FirewallTableEntry_Object = MibTableRow
firewallTableEntry = _FirewallTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1)
)
firewallTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "firewallTableIndex"),
)
if mibBuilder.loadTexts:
    firewallTableEntry.setStatus("current")


class _FirewallTableIndex_Type(Integer32):
    """Custom type firewallTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_FirewallTableIndex_Type.__name__ = "Integer32"
_FirewallTableIndex_Object = MibTableColumn
firewallTableIndex = _FirewallTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 1),
    _FirewallTableIndex_Type()
)
firewallTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    firewallTableIndex.setStatus("current")


class _FirewallTableTarget_Type(Integer32):
    """Custom type firewallTableTarget based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_FirewallTableTarget_Type.__name__ = "Integer32"
_FirewallTableTarget_Object = MibTableColumn
firewallTableTarget = _FirewallTableTarget_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 2),
    _FirewallTableTarget_Type()
)
firewallTableTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableTarget.setStatus("current")


class _FirewallTableSrcIface_Type(OctetString):
    """Custom type firewallTableSrcIface based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FirewallTableSrcIface_Type.__name__ = "OctetString"
_FirewallTableSrcIface_Object = MibTableColumn
firewallTableSrcIface = _FirewallTableSrcIface_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 3),
    _FirewallTableSrcIface_Type()
)
firewallTableSrcIface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableSrcIface.setStatus("current")


class _FirewallTableDstIface_Type(OctetString):
    """Custom type firewallTableDstIface based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FirewallTableDstIface_Type.__name__ = "OctetString"
_FirewallTableDstIface_Object = MibTableColumn
firewallTableDstIface = _FirewallTableDstIface_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 4),
    _FirewallTableDstIface_Type()
)
firewallTableDstIface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableDstIface.setStatus("current")
_FirewallTableSrcIp_Type = IpAddress
_FirewallTableSrcIp_Object = MibTableColumn
firewallTableSrcIp = _FirewallTableSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 5),
    _FirewallTableSrcIp_Type()
)
firewallTableSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableSrcIp.setStatus("current")
_FirewallTableSrcMask_Type = IpAddress
_FirewallTableSrcMask_Object = MibTableColumn
firewallTableSrcMask = _FirewallTableSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 6),
    _FirewallTableSrcMask_Type()
)
firewallTableSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableSrcMask.setStatus("current")
_FirewallTableDstIp_Type = IpAddress
_FirewallTableDstIp_Object = MibTableColumn
firewallTableDstIp = _FirewallTableDstIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 7),
    _FirewallTableDstIp_Type()
)
firewallTableDstIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableDstIp.setStatus("current")
_FirewallTableDstMask_Type = IpAddress
_FirewallTableDstMask_Object = MibTableColumn
firewallTableDstMask = _FirewallTableDstMask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 8),
    _FirewallTableDstMask_Type()
)
firewallTableDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableDstMask.setStatus("current")


class _FirewallTableProtocol_Type(Integer32):
    """Custom type firewallTableProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FirewallTableProtocol_Type.__name__ = "Integer32"
_FirewallTableProtocol_Object = MibTableColumn
firewallTableProtocol = _FirewallTableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 9),
    _FirewallTableProtocol_Type()
)
firewallTableProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableProtocol.setStatus("current")


class _FirewallTableStartPort_Type(Integer32):
    """Custom type firewallTableStartPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_FirewallTableStartPort_Type.__name__ = "Integer32"
_FirewallTableStartPort_Object = MibTableColumn
firewallTableStartPort = _FirewallTableStartPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 10),
    _FirewallTableStartPort_Type()
)
firewallTableStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableStartPort.setStatus("current")


class _FirewallTableEndPort_Type(Integer32):
    """Custom type firewallTableEndPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_FirewallTableEndPort_Type.__name__ = "Integer32"
_FirewallTableEndPort_Object = MibTableColumn
firewallTableEndPort = _FirewallTableEndPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 11),
    _FirewallTableEndPort_Type()
)
firewallTableEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableEndPort.setStatus("current")


class _FirewallTableUserGroup_Type(Integer32):
    """Custom type firewallTableUserGroup based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 999999),
    )


_FirewallTableUserGroup_Type.__name__ = "Integer32"
_FirewallTableUserGroup_Object = MibTableColumn
firewallTableUserGroup = _FirewallTableUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 12),
    _FirewallTableUserGroup_Type()
)
firewallTableUserGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableUserGroup.setStatus("current")


class _FirewallTableComment_Type(DisplayString):
    """Custom type firewallTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FirewallTableComment_Type.__name__ = "DisplayString"
_FirewallTableComment_Object = MibTableColumn
firewallTableComment = _FirewallTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 13),
    _FirewallTableComment_Type()
)
firewallTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableComment.setStatus("current")


class _FirewallTableActive_Type(Integer32):
    """Custom type firewallTableActive based on Integer32"""
    defaultValue = 1

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


_FirewallTableActive_Type.__name__ = "Integer32"
_FirewallTableActive_Object = MibTableColumn
firewallTableActive = _FirewallTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 14),
    _FirewallTableActive_Type()
)
firewallTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableActive.setStatus("current")
_FirewallTableRowStatus_Type = RowStatus
_FirewallTableRowStatus_Object = MibTableColumn
firewallTableRowStatus = _FirewallTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 15, 2, 1, 15),
    _FirewallTableRowStatus_Type()
)
firewallTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    firewallTableRowStatus.setStatus("current")
_NodeConfigurationMacaccess_ObjectIdentity = ObjectIdentity
nodeConfigurationMacaccess = _NodeConfigurationMacaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16)
)


class _MacaccessActive_Type(Integer32):
    """Custom type macaccessActive based on Integer32"""
    defaultValue = 2

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


_MacaccessActive_Type.__name__ = "Integer32"
_MacaccessActive_Object = MibScalar
macaccessActive = _MacaccessActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 1),
    _MacaccessActive_Type()
)
macaccessActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macaccessActive.setStatus("current")


class _MacaccessType_Type(Integer32):
    """Custom type macaccessType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_MacaccessType_Type.__name__ = "Integer32"
_MacaccessType_Object = MibScalar
macaccessType = _MacaccessType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 2),
    _MacaccessType_Type()
)
macaccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macaccessType.setStatus("current")


class _MacActiveListExecute_Type(Integer32):
    """Custom type macActiveListExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MacActiveListExecute_Type.__name__ = "Integer32"
_MacActiveListExecute_Object = MibScalar
macActiveListExecute = _MacActiveListExecute_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 3),
    _MacActiveListExecute_Type()
)
macActiveListExecute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macActiveListExecute.setStatus("current")
_MacaccessTable_Object = MibTable
macaccessTable = _MacaccessTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 4)
)
if mibBuilder.loadTexts:
    macaccessTable.setStatus("current")
_MacaccessTableEntry_Object = MibTableRow
macaccessTableEntry = _MacaccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 4, 1)
)
macaccessTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "macaccessTableIndex"),
)
if mibBuilder.loadTexts:
    macaccessTableEntry.setStatus("current")


class _MacaccessTableIndex_Type(Integer32):
    """Custom type macaccessTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_MacaccessTableIndex_Type.__name__ = "Integer32"
_MacaccessTableIndex_Object = MibTableColumn
macaccessTableIndex = _MacaccessTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 4, 1, 1),
    _MacaccessTableIndex_Type()
)
macaccessTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macaccessTableIndex.setStatus("current")
_MacaccessTableMac_Type = MacAddress
_MacaccessTableMac_Object = MibTableColumn
macaccessTableMac = _MacaccessTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 4, 1, 2),
    _MacaccessTableMac_Type()
)
macaccessTableMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macaccessTableMac.setStatus("current")


class _MacaccessTableType_Type(Integer32):
    """Custom type macaccessTableType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_MacaccessTableType_Type.__name__ = "Integer32"
_MacaccessTableType_Object = MibTableColumn
macaccessTableType = _MacaccessTableType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 4, 1, 3),
    _MacaccessTableType_Type()
)
macaccessTableType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macaccessTableType.setStatus("current")


class _MacaccessTableComment_Type(DisplayString):
    """Custom type macaccessTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MacaccessTableComment_Type.__name__ = "DisplayString"
_MacaccessTableComment_Object = MibTableColumn
macaccessTableComment = _MacaccessTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 4, 1, 4),
    _MacaccessTableComment_Type()
)
macaccessTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macaccessTableComment.setStatus("current")


class _MacaccessTableActive_Type(Integer32):
    """Custom type macaccessTableActive based on Integer32"""
    defaultValue = 1

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


_MacaccessTableActive_Type.__name__ = "Integer32"
_MacaccessTableActive_Object = MibTableColumn
macaccessTableActive = _MacaccessTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 4, 1, 5),
    _MacaccessTableActive_Type()
)
macaccessTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macaccessTableActive.setStatus("current")
_MacaccessTableRowStatus_Type = RowStatus
_MacaccessTableRowStatus_Object = MibTableColumn
macaccessTableRowStatus = _MacaccessTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 4, 1, 6),
    _MacaccessTableRowStatus_Type()
)
macaccessTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macaccessTableRowStatus.setStatus("current")
_MacActiveTable_Object = MibTable
macActiveTable = _MacActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 5)
)
if mibBuilder.loadTexts:
    macActiveTable.setStatus("current")
_MacActiveTableEntry_Object = MibTableRow
macActiveTableEntry = _MacActiveTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 5, 1)
)
macActiveTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "macActiveTableIndex"),
)
if mibBuilder.loadTexts:
    macActiveTableEntry.setStatus("current")


class _MacActiveTableIndex_Type(Integer32):
    """Custom type macActiveTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_MacActiveTableIndex_Type.__name__ = "Integer32"
_MacActiveTableIndex_Object = MibTableColumn
macActiveTableIndex = _MacActiveTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 5, 1, 1),
    _MacActiveTableIndex_Type()
)
macActiveTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macActiveTableIndex.setStatus("current")
_MacActiveTableMac_Type = MacAddress
_MacActiveTableMac_Object = MibTableColumn
macActiveTableMac = _MacActiveTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 5, 1, 2),
    _MacActiveTableMac_Type()
)
macActiveTableMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macActiveTableMac.setStatus("current")
_MacActiveTableIp_Type = IpAddress
_MacActiveTableIp_Object = MibTableColumn
macActiveTableIp = _MacActiveTableIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 16, 5, 1, 3),
    _MacActiveTableIp_Type()
)
macActiveTableIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macActiveTableIp.setStatus("current")
_NodeConfigurationNat_ObjectIdentity = ObjectIdentity
nodeConfigurationNat = _NodeConfigurationNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17)
)


class _NatActive_Type(Integer32):
    """Custom type natActive based on Integer32"""
    defaultValue = 2

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


_NatActive_Type.__name__ = "Integer32"
_NatActive_Object = MibScalar
natActive = _NatActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17, 1),
    _NatActive_Type()
)
natActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natActive.setStatus("current")
_NatTable_Object = MibTable
natTable = _NatTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17, 2)
)
if mibBuilder.loadTexts:
    natTable.setStatus("current")
_NatTableEntry_Object = MibTableRow
natTableEntry = _NatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17, 2, 1)
)
natTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "natTableIndex"),
)
if mibBuilder.loadTexts:
    natTableEntry.setStatus("current")


class _NatTableIndex_Type(Integer32):
    """Custom type natTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_NatTableIndex_Type.__name__ = "Integer32"
_NatTableIndex_Object = MibTableColumn
natTableIndex = _NatTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17, 2, 1, 1),
    _NatTableIndex_Type()
)
natTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    natTableIndex.setStatus("current")


class _NatTableProtocol_Type(Integer32):
    """Custom type natTableProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_NatTableProtocol_Type.__name__ = "Integer32"
_NatTableProtocol_Object = MibTableColumn
natTableProtocol = _NatTableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17, 2, 1, 2),
    _NatTableProtocol_Type()
)
natTableProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natTableProtocol.setStatus("current")


class _NatTablePort_Type(Integer32):
    """Custom type natTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NatTablePort_Type.__name__ = "Integer32"
_NatTablePort_Object = MibTableColumn
natTablePort = _NatTablePort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17, 2, 1, 3),
    _NatTablePort_Type()
)
natTablePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natTablePort.setStatus("current")
_NatTableIp_Type = IpAddress
_NatTableIp_Object = MibTableColumn
natTableIp = _NatTableIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17, 2, 1, 4),
    _NatTableIp_Type()
)
natTableIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natTableIp.setStatus("current")


class _NatTableComment_Type(DisplayString):
    """Custom type natTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NatTableComment_Type.__name__ = "DisplayString"
_NatTableComment_Object = MibTableColumn
natTableComment = _NatTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17, 2, 1, 5),
    _NatTableComment_Type()
)
natTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natTableComment.setStatus("current")


class _NatTableActive_Type(Integer32):
    """Custom type natTableActive based on Integer32"""
    defaultValue = 1

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


_NatTableActive_Type.__name__ = "Integer32"
_NatTableActive_Object = MibTableColumn
natTableActive = _NatTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17, 2, 1, 6),
    _NatTableActive_Type()
)
natTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natTableActive.setStatus("current")
_NatTableRowStatus_Type = RowStatus
_NatTableRowStatus_Object = MibTableColumn
natTableRowStatus = _NatTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 17, 2, 1, 7),
    _NatTableRowStatus_Type()
)
natTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    natTableRowStatus.setStatus("current")
_NodeConfigurationOlsrGW_ObjectIdentity = ObjectIdentity
nodeConfigurationOlsrGW = _NodeConfigurationOlsrGW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 18)
)
_OlsrGatewayTable_Object = MibTable
olsrGatewayTable = _OlsrGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    olsrGatewayTable.setStatus("current")
_OlsrGatewayTableEntry_Object = MibTableRow
olsrGatewayTableEntry = _OlsrGatewayTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 18, 1, 1)
)
olsrGatewayTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "olsrGatewayTableIndex"),
)
if mibBuilder.loadTexts:
    olsrGatewayTableEntry.setStatus("current")


class _OlsrGatewayTableIndex_Type(Integer32):
    """Custom type olsrGatewayTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_OlsrGatewayTableIndex_Type.__name__ = "Integer32"
_OlsrGatewayTableIndex_Object = MibTableColumn
olsrGatewayTableIndex = _OlsrGatewayTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 18, 1, 1, 1),
    _OlsrGatewayTableIndex_Type()
)
olsrGatewayTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    olsrGatewayTableIndex.setStatus("current")
_OlsrGatewayTableSubnet_Type = IpAddress
_OlsrGatewayTableSubnet_Object = MibTableColumn
olsrGatewayTableSubnet = _OlsrGatewayTableSubnet_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 18, 1, 1, 2),
    _OlsrGatewayTableSubnet_Type()
)
olsrGatewayTableSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrGatewayTableSubnet.setStatus("current")
_OlsrGatewayTableNetmask_Type = IpAddress
_OlsrGatewayTableNetmask_Object = MibTableColumn
olsrGatewayTableNetmask = _OlsrGatewayTableNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 18, 1, 1, 3),
    _OlsrGatewayTableNetmask_Type()
)
olsrGatewayTableNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrGatewayTableNetmask.setStatus("current")


class _OlsrGatewayTableComments_Type(DisplayString):
    """Custom type olsrGatewayTableComments based on DisplayString"""
    defaultValue = OctetString("none")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OlsrGatewayTableComments_Type.__name__ = "DisplayString"
_OlsrGatewayTableComments_Object = MibTableColumn
olsrGatewayTableComments = _OlsrGatewayTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 18, 1, 1, 4),
    _OlsrGatewayTableComments_Type()
)
olsrGatewayTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrGatewayTableComments.setStatus("current")


class _OlsrGatewayTableActive_Type(Integer32):
    """Custom type olsrGatewayTableActive based on Integer32"""
    defaultValue = 1

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


_OlsrGatewayTableActive_Type.__name__ = "Integer32"
_OlsrGatewayTableActive_Object = MibTableColumn
olsrGatewayTableActive = _OlsrGatewayTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 18, 1, 1, 5),
    _OlsrGatewayTableActive_Type()
)
olsrGatewayTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrGatewayTableActive.setStatus("current")
_OlsrGatewayTableRowStatus_Type = RowStatus
_OlsrGatewayTableRowStatus_Object = MibTableColumn
olsrGatewayTableRowStatus = _OlsrGatewayTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 18, 1, 1, 6),
    _OlsrGatewayTableRowStatus_Type()
)
olsrGatewayTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    olsrGatewayTableRowStatus.setStatus("current")
_NodeConfigurationShaping_ObjectIdentity = ObjectIdentity
nodeConfigurationShaping = _NodeConfigurationShaping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19)
)


class _ShapingActive_Type(Integer32):
    """Custom type shapingActive based on Integer32"""
    defaultValue = 2

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


_ShapingActive_Type.__name__ = "Integer32"
_ShapingActive_Object = MibScalar
shapingActive = _ShapingActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 1),
    _ShapingActive_Type()
)
shapingActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shapingActive.setStatus("current")


class _ShapingWanRateup_Type(Integer32):
    """Custom type shapingWanRateup based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_ShapingWanRateup_Type.__name__ = "Integer32"
_ShapingWanRateup_Object = MibScalar
shapingWanRateup = _ShapingWanRateup_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 2),
    _ShapingWanRateup_Type()
)
shapingWanRateup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shapingWanRateup.setStatus("current")


class _ShapingWanRatedown_Type(Integer32):
    """Custom type shapingWanRatedown based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_ShapingWanRatedown_Type.__name__ = "Integer32"
_ShapingWanRatedown_Object = MibScalar
shapingWanRatedown = _ShapingWanRatedown_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 3),
    _ShapingWanRatedown_Type()
)
shapingWanRatedown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shapingWanRatedown.setStatus("current")


class _ShapingMeshRateup_Type(Integer32):
    """Custom type shapingMeshRateup based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ShapingMeshRateup_Type.__name__ = "Integer32"
_ShapingMeshRateup_Object = MibScalar
shapingMeshRateup = _ShapingMeshRateup_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 4),
    _ShapingMeshRateup_Type()
)
shapingMeshRateup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shapingMeshRateup.setStatus("current")


class _ShapingMeshRatedown_Type(Integer32):
    """Custom type shapingMeshRatedown based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ShapingMeshRatedown_Type.__name__ = "Integer32"
_ShapingMeshRatedown_Object = MibScalar
shapingMeshRatedown = _ShapingMeshRatedown_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 5),
    _ShapingMeshRatedown_Type()
)
shapingMeshRatedown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shapingMeshRatedown.setStatus("current")


class _ShapingVlanRateup_Type(Integer32):
    """Custom type shapingVlanRateup based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ShapingVlanRateup_Type.__name__ = "Integer32"
_ShapingVlanRateup_Object = MibScalar
shapingVlanRateup = _ShapingVlanRateup_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 6),
    _ShapingVlanRateup_Type()
)
shapingVlanRateup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shapingVlanRateup.setStatus("current")


class _ShapingVlanRatedown_Type(Integer32):
    """Custom type shapingVlanRatedown based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ShapingVlanRatedown_Type.__name__ = "Integer32"
_ShapingVlanRatedown_Object = MibScalar
shapingVlanRatedown = _ShapingVlanRatedown_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 7),
    _ShapingVlanRatedown_Type()
)
shapingVlanRatedown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shapingVlanRatedown.setStatus("current")


class _ShapingDefaultup_Type(Integer32):
    """Custom type shapingDefaultup based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_ShapingDefaultup_Type.__name__ = "Integer32"
_ShapingDefaultup_Object = MibScalar
shapingDefaultup = _ShapingDefaultup_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 8),
    _ShapingDefaultup_Type()
)
shapingDefaultup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shapingDefaultup.setStatus("current")


class _ShapingDefaultdown_Type(Integer32):
    """Custom type shapingDefaultdown based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_ShapingDefaultdown_Type.__name__ = "Integer32"
_ShapingDefaultdown_Object = MibScalar
shapingDefaultdown = _ShapingDefaultdown_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 9),
    _ShapingDefaultdown_Type()
)
shapingDefaultdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shapingDefaultdown.setStatus("current")
_ShapingTable_Object = MibTable
shapingTable = _ShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10)
)
if mibBuilder.loadTexts:
    shapingTable.setStatus("current")
_ShapingTableEntry_Object = MibTableRow
shapingTableEntry = _ShapingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10, 1)
)
shapingTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "shapingTableIndex"),
)
if mibBuilder.loadTexts:
    shapingTableEntry.setStatus("current")


class _ShapingTableIndex_Type(Integer32):
    """Custom type shapingTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ShapingTableIndex_Type.__name__ = "Integer32"
_ShapingTableIndex_Object = MibTableColumn
shapingTableIndex = _ShapingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10, 1, 1),
    _ShapingTableIndex_Type()
)
shapingTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    shapingTableIndex.setStatus("current")


class _ShapingTableProtocol_Type(Integer32):
    """Custom type shapingTableProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_ShapingTableProtocol_Type.__name__ = "Integer32"
_ShapingTableProtocol_Object = MibTableColumn
shapingTableProtocol = _ShapingTableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10, 1, 2),
    _ShapingTableProtocol_Type()
)
shapingTableProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    shapingTableProtocol.setStatus("current")


class _ShapingTablePort_Type(Integer32):
    """Custom type shapingTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ShapingTablePort_Type.__name__ = "Integer32"
_ShapingTablePort_Object = MibTableColumn
shapingTablePort = _ShapingTablePort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10, 1, 3),
    _ShapingTablePort_Type()
)
shapingTablePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    shapingTablePort.setStatus("current")


class _ShapingTableMinsize_Type(Integer32):
    """Custom type shapingTableMinsize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ShapingTableMinsize_Type.__name__ = "Integer32"
_ShapingTableMinsize_Object = MibTableColumn
shapingTableMinsize = _ShapingTableMinsize_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10, 1, 4),
    _ShapingTableMinsize_Type()
)
shapingTableMinsize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    shapingTableMinsize.setStatus("current")


class _ShapingTableMaxsize_Type(Integer32):
    """Custom type shapingTableMaxsize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ShapingTableMaxsize_Type.__name__ = "Integer32"
_ShapingTableMaxsize_Object = MibTableColumn
shapingTableMaxsize = _ShapingTableMaxsize_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10, 1, 5),
    _ShapingTableMaxsize_Type()
)
shapingTableMaxsize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    shapingTableMaxsize.setStatus("current")


class _ShapingTablePriority_Type(Integer32):
    """Custom type shapingTablePriority based on Integer32"""
    defaultValue = 1

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
        *(("background", 1),
          ("besteffort", 4),
          ("video", 2),
          ("voice", 3))
    )


_ShapingTablePriority_Type.__name__ = "Integer32"
_ShapingTablePriority_Object = MibTableColumn
shapingTablePriority = _ShapingTablePriority_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10, 1, 6),
    _ShapingTablePriority_Type()
)
shapingTablePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    shapingTablePriority.setStatus("current")


class _ShapingTableComment_Type(DisplayString):
    """Custom type shapingTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ShapingTableComment_Type.__name__ = "DisplayString"
_ShapingTableComment_Object = MibTableColumn
shapingTableComment = _ShapingTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10, 1, 7),
    _ShapingTableComment_Type()
)
shapingTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    shapingTableComment.setStatus("current")


class _ShapingTableActive_Type(Integer32):
    """Custom type shapingTableActive based on Integer32"""
    defaultValue = 1

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


_ShapingTableActive_Type.__name__ = "Integer32"
_ShapingTableActive_Object = MibTableColumn
shapingTableActive = _ShapingTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10, 1, 8),
    _ShapingTableActive_Type()
)
shapingTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    shapingTableActive.setStatus("current")
_ShapingTableRowStatus_Type = RowStatus
_ShapingTableRowStatus_Object = MibTableColumn
shapingTableRowStatus = _ShapingTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 19, 10, 1, 9),
    _ShapingTableRowStatus_Type()
)
shapingTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    shapingTableRowStatus.setStatus("current")
_NodeConfigurationPppoe_ObjectIdentity = ObjectIdentity
nodeConfigurationPppoe = _NodeConfigurationPppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 20)
)


class _PppoeActive_Type(Integer32):
    """Custom type pppoeActive based on Integer32"""
    defaultValue = 2

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


_PppoeActive_Type.__name__ = "Integer32"
_PppoeActive_Object = MibScalar
pppoeActive = _PppoeActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 20, 1),
    _PppoeActive_Type()
)
pppoeActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeActive.setStatus("current")


class _PppoeUsername_Type(DisplayString):
    """Custom type pppoeUsername based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PppoeUsername_Type.__name__ = "DisplayString"
_PppoeUsername_Object = MibScalar
pppoeUsername = _PppoeUsername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 20, 2),
    _PppoeUsername_Type()
)
pppoeUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeUsername.setStatus("current")


class _PppoePassword_Type(DisplayString):
    """Custom type pppoePassword based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PppoePassword_Type.__name__ = "DisplayString"
_PppoePassword_Object = MibScalar
pppoePassword = _PppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 20, 3),
    _PppoePassword_Type()
)
pppoePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePassword.setStatus("current")


class _PppoeAuthType_Type(Integer32):
    """Custom type pppoeAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )


_PppoeAuthType_Type.__name__ = "Integer32"
_PppoeAuthType_Object = MibScalar
pppoeAuthType = _PppoeAuthType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 20, 4),
    _PppoeAuthType_Type()
)
pppoeAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeAuthType.setStatus("current")


class _PppoeUseChap_Type(Integer32):
    """Custom type pppoeUseChap based on Integer32"""
    defaultValue = 2

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


_PppoeUseChap_Type.__name__ = "Integer32"
_PppoeUseChap_Object = MibScalar
pppoeUseChap = _PppoeUseChap_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 20, 5),
    _PppoeUseChap_Type()
)
pppoeUseChap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeUseChap.setStatus("current")


class _PppoeChapUsername_Type(DisplayString):
    """Custom type pppoeChapUsername based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PppoeChapUsername_Type.__name__ = "DisplayString"
_PppoeChapUsername_Object = MibScalar
pppoeChapUsername = _PppoeChapUsername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 20, 6),
    _PppoeChapUsername_Type()
)
pppoeChapUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeChapUsername.setStatus("current")


class _PppoeChapPassword_Type(DisplayString):
    """Custom type pppoeChapPassword based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PppoeChapPassword_Type.__name__ = "DisplayString"
_PppoeChapPassword_Object = MibScalar
pppoeChapPassword = _PppoeChapPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 20, 7),
    _PppoeChapPassword_Type()
)
pppoeChapPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeChapPassword.setStatus("current")
_NodeConfigurationPptp_ObjectIdentity = ObjectIdentity
nodeConfigurationPptp = _NodeConfigurationPptp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21)
)


class _PptpActive_Type(Integer32):
    """Custom type pptpActive based on Integer32"""
    defaultValue = 1

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


_PptpActive_Type.__name__ = "Integer32"
_PptpActive_Object = MibScalar
pptpActive = _PptpActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 1),
    _PptpActive_Type()
)
pptpActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpActive.setStatus("current")
_PptpTable_Object = MibTable
pptpTable = _PptpTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 2)
)
if mibBuilder.loadTexts:
    pptpTable.setStatus("current")
_PptpTableEntry_Object = MibTableRow
pptpTableEntry = _PptpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 2, 1)
)
pptpTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "pptpTableIndex"),
)
if mibBuilder.loadTexts:
    pptpTableEntry.setStatus("current")


class _PptpTableIndex_Type(Integer32):
    """Custom type pptpTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PptpTableIndex_Type.__name__ = "Integer32"
_PptpTableIndex_Object = MibTableColumn
pptpTableIndex = _PptpTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 2, 1, 1),
    _PptpTableIndex_Type()
)
pptpTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pptpTableIndex.setStatus("current")


class _PptpTableUsername_Type(DisplayString):
    """Custom type pptpTableUsername based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PptpTableUsername_Type.__name__ = "DisplayString"
_PptpTableUsername_Object = MibTableColumn
pptpTableUsername = _PptpTableUsername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 2, 1, 2),
    _PptpTableUsername_Type()
)
pptpTableUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pptpTableUsername.setStatus("current")


class _PptpTablePassword_Type(DisplayString):
    """Custom type pptpTablePassword based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PptpTablePassword_Type.__name__ = "DisplayString"
_PptpTablePassword_Object = MibTableColumn
pptpTablePassword = _PptpTablePassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 2, 1, 3),
    _PptpTablePassword_Type()
)
pptpTablePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pptpTablePassword.setStatus("current")
_PptpTableIp_Type = IpAddress
_PptpTableIp_Object = MibTableColumn
pptpTableIp = _PptpTableIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 2, 1, 4),
    _PptpTableIp_Type()
)
pptpTableIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pptpTableIp.setStatus("current")


class _PptpTableComment_Type(DisplayString):
    """Custom type pptpTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PptpTableComment_Type.__name__ = "DisplayString"
_PptpTableComment_Object = MibTableColumn
pptpTableComment = _PptpTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 2, 1, 5),
    _PptpTableComment_Type()
)
pptpTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pptpTableComment.setStatus("current")


class _PptpTableActive_Type(Integer32):
    """Custom type pptpTableActive based on Integer32"""
    defaultValue = 1

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


_PptpTableActive_Type.__name__ = "Integer32"
_PptpTableActive_Object = MibTableColumn
pptpTableActive = _PptpTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 2, 1, 6),
    _PptpTableActive_Type()
)
pptpTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pptpTableActive.setStatus("current")
_PptpTableRowStatus_Type = RowStatus
_PptpTableRowStatus_Object = MibTableColumn
pptpTableRowStatus = _PptpTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 2, 1, 7),
    _PptpTableRowStatus_Type()
)
pptpTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pptpTableRowStatus.setStatus("current")
_PptpServerip_Type = IpAddress
_PptpServerip_Object = MibScalar
pptpServerip = _PptpServerip_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 3),
    _PptpServerip_Type()
)
pptpServerip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpServerip.setStatus("current")
_PptpStartip_Type = IpAddress
_PptpStartip_Object = MibScalar
pptpStartip = _PptpStartip_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 4),
    _PptpStartip_Type()
)
pptpStartip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpStartip.setStatus("current")
_PptpEndip_Type = IpAddress
_PptpEndip_Object = MibScalar
pptpEndip = _PptpEndip_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 21, 5),
    _PptpEndip_Type()
)
pptpEndip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pptpEndip.setStatus("current")
_NodeConfigurationTmipd_ObjectIdentity = ObjectIdentity
nodeConfigurationTmipd = _NodeConfigurationTmipd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 22)
)


class _TmipdActive_Type(Integer32):
    """Custom type tmipdActive based on Integer32"""
    defaultValue = 2

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


_TmipdActive_Type.__name__ = "Integer32"
_TmipdActive_Object = MibScalar
tmipdActive = _TmipdActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 22, 1),
    _TmipdActive_Type()
)
tmipdActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmipdActive.setStatus("current")


class _TmipdNetname_Type(OctetString):
    """Custom type tmipdNetname based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmipdNetname_Type.__name__ = "OctetString"
_TmipdNetname_Object = MibScalar
tmipdNetname = _TmipdNetname_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 22, 2),
    _TmipdNetname_Type()
)
tmipdNetname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmipdNetname.setStatus("current")
_TmipdMlrdip_Type = IpAddress
_TmipdMlrdip_Object = MibScalar
tmipdMlrdip = _TmipdMlrdip_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 22, 3),
    _TmipdMlrdip_Type()
)
tmipdMlrdip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmipdMlrdip.setStatus("current")


class _TmipdVlan_Type(OctetString):
    """Custom type tmipdVlan based on OctetString"""
    defaultValue = OctetString("vlan0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmipdVlan_Type.__name__ = "OctetString"
_TmipdVlan_Object = MibScalar
tmipdVlan = _TmipdVlan_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 22, 4),
    _TmipdVlan_Type()
)
tmipdVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmipdVlan.setStatus("current")
_NodeConfigurationCaptive_ObjectIdentity = ObjectIdentity
nodeConfigurationCaptive = _NodeConfigurationCaptive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23)
)


class _CaptiveActive_Type(Integer32):
    """Custom type captiveActive based on Integer32"""
    defaultValue = 2

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


_CaptiveActive_Type.__name__ = "Integer32"
_CaptiveActive_Object = MibScalar
captiveActive = _CaptiveActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 1),
    _CaptiveActive_Type()
)
captiveActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveActive.setStatus("current")


class _CaptiveRedirect_Type(DisplayString):
    """Custom type captiveRedirect based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_CaptiveRedirect_Type.__name__ = "DisplayString"
_CaptiveRedirect_Object = MibScalar
captiveRedirect = _CaptiveRedirect_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 2),
    _CaptiveRedirect_Type()
)
captiveRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveRedirect.setStatus("current")


class _CaptivePop3push_Type(Integer32):
    """Custom type captivePop3push based on Integer32"""
    defaultValue = 1

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


_CaptivePop3push_Type.__name__ = "Integer32"
_CaptivePop3push_Object = MibScalar
captivePop3push = _CaptivePop3push_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 3),
    _CaptivePop3push_Type()
)
captivePop3push.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captivePop3push.setStatus("current")


class _CaptiveExternalActive_Type(Integer32):
    """Custom type captiveExternalActive based on Integer32"""
    defaultValue = 2

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


_CaptiveExternalActive_Type.__name__ = "Integer32"
_CaptiveExternalActive_Object = MibScalar
captiveExternalActive = _CaptiveExternalActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 4),
    _CaptiveExternalActive_Type()
)
captiveExternalActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveExternalActive.setStatus("current")


class _CaptiveExternalServer_Type(DisplayString):
    """Custom type captiveExternalServer based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_CaptiveExternalServer_Type.__name__ = "DisplayString"
_CaptiveExternalServer_Object = MibScalar
captiveExternalServer = _CaptiveExternalServer_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 5),
    _CaptiveExternalServer_Type()
)
captiveExternalServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveExternalServer.setStatus("current")


class _CaptiveDefaultIdleTimeout_Type(Integer32):
    """Custom type captiveDefaultIdleTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaptiveDefaultIdleTimeout_Type.__name__ = "Integer32"
_CaptiveDefaultIdleTimeout_Object = MibScalar
captiveDefaultIdleTimeout = _CaptiveDefaultIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 6),
    _CaptiveDefaultIdleTimeout_Type()
)
captiveDefaultIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveDefaultIdleTimeout.setStatus("current")


class _CaptiveDefaultSessionTimeout_Type(Integer32):
    """Custom type captiveDefaultSessionTimeout based on Integer32"""
    defaultValue = 65000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CaptiveDefaultSessionTimeout_Type.__name__ = "Integer32"
_CaptiveDefaultSessionTimeout_Object = MibScalar
captiveDefaultSessionTimeout = _CaptiveDefaultSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 7),
    _CaptiveDefaultSessionTimeout_Type()
)
captiveDefaultSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveDefaultSessionTimeout.setStatus("current")


class _CaptiveHttpActive_Type(Integer32):
    """Custom type captiveHttpActive based on Integer32"""
    defaultValue = 1

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


_CaptiveHttpActive_Type.__name__ = "Integer32"
_CaptiveHttpActive_Object = MibScalar
captiveHttpActive = _CaptiveHttpActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 8),
    _CaptiveHttpActive_Type()
)
captiveHttpActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveHttpActive.setStatus("current")


class _CaptiveHttpPort_Type(Integer32):
    """Custom type captiveHttpPort based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_CaptiveHttpPort_Type.__name__ = "Integer32"
_CaptiveHttpPort_Object = MibScalar
captiveHttpPort = _CaptiveHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 9),
    _CaptiveHttpPort_Type()
)
captiveHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveHttpPort.setStatus("current")


class _CaptiveHttpsActive_Type(Integer32):
    """Custom type captiveHttpsActive based on Integer32"""
    defaultValue = 1

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


_CaptiveHttpsActive_Type.__name__ = "Integer32"
_CaptiveHttpsActive_Object = MibScalar
captiveHttpsActive = _CaptiveHttpsActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 10),
    _CaptiveHttpsActive_Type()
)
captiveHttpsActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveHttpsActive.setStatus("current")


class _CaptiveHttpsPort_Type(Integer32):
    """Custom type captiveHttpsPort based on Integer32"""
    defaultValue = 3001

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_CaptiveHttpsPort_Type.__name__ = "Integer32"
_CaptiveHttpsPort_Object = MibScalar
captiveHttpsPort = _CaptiveHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 11),
    _CaptiveHttpsPort_Type()
)
captiveHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveHttpsPort.setStatus("current")


class _CaptiveWebspaceActive_Type(Integer32):
    """Custom type captiveWebspaceActive based on Integer32"""
    defaultValue = 1

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


_CaptiveWebspaceActive_Type.__name__ = "Integer32"
_CaptiveWebspaceActive_Object = MibScalar
captiveWebspaceActive = _CaptiveWebspaceActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 12),
    _CaptiveWebspaceActive_Type()
)
captiveWebspaceActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveWebspaceActive.setStatus("current")


class _CaptiveWebspacePort_Type(Integer32):
    """Custom type captiveWebspacePort based on Integer32"""
    defaultValue = 3002

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_CaptiveWebspacePort_Type.__name__ = "Integer32"
_CaptiveWebspacePort_Object = MibScalar
captiveWebspacePort = _CaptiveWebspacePort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 13),
    _CaptiveWebspacePort_Type()
)
captiveWebspacePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveWebspacePort.setStatus("current")


class _CaptiveDefaultLanguage_Type(DisplayString):
    """Custom type captiveDefaultLanguage based on DisplayString"""
    defaultValue = OctetString("english")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CaptiveDefaultLanguage_Type.__name__ = "DisplayString"
_CaptiveDefaultLanguage_Object = MibScalar
captiveDefaultLanguage = _CaptiveDefaultLanguage_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 14),
    _CaptiveDefaultLanguage_Type()
)
captiveDefaultLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveDefaultLanguage.setStatus("current")


class _CaptiveMultipleUsername_Type(Integer32):
    """Custom type captiveMultipleUsername based on Integer32"""
    defaultValue = 2

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


_CaptiveMultipleUsername_Type.__name__ = "Integer32"
_CaptiveMultipleUsername_Object = MibScalar
captiveMultipleUsername = _CaptiveMultipleUsername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 15),
    _CaptiveMultipleUsername_Type()
)
captiveMultipleUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captiveMultipleUsername.setStatus("current")


class _Captive1xLogin_Type(Integer32):
    """Custom type captive1xLogin based on Integer32"""
    defaultValue = 1

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


_Captive1xLogin_Type.__name__ = "Integer32"
_Captive1xLogin_Object = MibScalar
captive1xLogin = _Captive1xLogin_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 23, 16),
    _Captive1xLogin_Type()
)
captive1xLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    captive1xLogin.setStatus("current")
_NodeConfigurationRadiusClient_ObjectIdentity = ObjectIdentity
nodeConfigurationRadiusClient = _NodeConfigurationRadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24)
)


class _RadiusclientActive_Type(Integer32):
    """Custom type radiusclientActive based on Integer32"""
    defaultValue = 1

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


_RadiusclientActive_Type.__name__ = "Integer32"
_RadiusclientActive_Object = MibScalar
radiusclientActive = _RadiusclientActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 1),
    _RadiusclientActive_Type()
)
radiusclientActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusclientActive.setStatus("current")


class _RadiusclientNasid_Type(DisplayString):
    """Custom type radiusclientNasid based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RadiusclientNasid_Type.__name__ = "DisplayString"
_RadiusclientNasid_Object = MibScalar
radiusclientNasid = _RadiusclientNasid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 2),
    _RadiusclientNasid_Type()
)
radiusclientNasid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusclientNasid.setStatus("current")


class _RadiusclientCalledstationid_Type(DisplayString):
    """Custom type radiusclientCalledstationid based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RadiusclientCalledstationid_Type.__name__ = "DisplayString"
_RadiusclientCalledstationid_Object = MibScalar
radiusclientCalledstationid = _RadiusclientCalledstationid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 3),
    _RadiusclientCalledstationid_Type()
)
radiusclientCalledstationid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusclientCalledstationid.setStatus("current")


class _RadiusclientNasport_Type(Integer32):
    """Custom type radiusclientNasport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusclientNasport_Type.__name__ = "Integer32"
_RadiusclientNasport_Object = MibScalar
radiusclientNasport = _RadiusclientNasport_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 4),
    _RadiusclientNasport_Type()
)
radiusclientNasport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusclientNasport.setStatus("current")


class _RadiusclientNasporttype_Type(Integer32):
    """Custom type radiusclientNasporttype based on Integer32"""
    defaultValue = 19

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusclientNasporttype_Type.__name__ = "Integer32"
_RadiusclientNasporttype_Object = MibScalar
radiusclientNasporttype = _RadiusclientNasporttype_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 5),
    _RadiusclientNasporttype_Type()
)
radiusclientNasporttype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusclientNasporttype.setStatus("current")


class _RadiusclientInterimupdate_Type(Integer32):
    """Custom type radiusclientInterimupdate based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusclientInterimupdate_Type.__name__ = "Integer32"
_RadiusclientInterimupdate_Object = MibScalar
radiusclientInterimupdate = _RadiusclientInterimupdate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 6),
    _RadiusclientInterimupdate_Type()
)
radiusclientInterimupdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusclientInterimupdate.setStatus("current")
_RadiusclientTable_Object = MibTable
radiusclientTable = _RadiusclientTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 7)
)
if mibBuilder.loadTexts:
    radiusclientTable.setStatus("current")
_RadiusclientTableEntry_Object = MibTableRow
radiusclientTableEntry = _RadiusclientTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 7, 1)
)
radiusclientTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "radiusclientTableIndex"),
)
if mibBuilder.loadTexts:
    radiusclientTableEntry.setStatus("current")


class _RadiusclientTableIndex_Type(Integer32):
    """Custom type radiusclientTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RadiusclientTableIndex_Type.__name__ = "Integer32"
_RadiusclientTableIndex_Object = MibTableColumn
radiusclientTableIndex = _RadiusclientTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 7, 1, 1),
    _RadiusclientTableIndex_Type()
)
radiusclientTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusclientTableIndex.setStatus("current")


class _RadiusclientTableServername_Type(DisplayString):
    """Custom type radiusclientTableServername based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RadiusclientTableServername_Type.__name__ = "DisplayString"
_RadiusclientTableServername_Object = MibTableColumn
radiusclientTableServername = _RadiusclientTableServername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 7, 1, 2),
    _RadiusclientTableServername_Type()
)
radiusclientTableServername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusclientTableServername.setStatus("current")


class _RadiusclientTableServertype_Type(Integer32):
    """Custom type radiusclientTableServertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 2),
          ("authenticate", 1))
    )


_RadiusclientTableServertype_Type.__name__ = "Integer32"
_RadiusclientTableServertype_Object = MibTableColumn
radiusclientTableServertype = _RadiusclientTableServertype_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 7, 1, 3),
    _RadiusclientTableServertype_Type()
)
radiusclientTableServertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusclientTableServertype.setStatus("current")


class _RadiusclientTableServerport_Type(Integer32):
    """Custom type radiusclientTableServerport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusclientTableServerport_Type.__name__ = "Integer32"
_RadiusclientTableServerport_Object = MibTableColumn
radiusclientTableServerport = _RadiusclientTableServerport_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 7, 1, 4),
    _RadiusclientTableServerport_Type()
)
radiusclientTableServerport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusclientTableServerport.setStatus("current")


class _RadiusclientTableServersecret_Type(DisplayString):
    """Custom type radiusclientTableServersecret based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadiusclientTableServersecret_Type.__name__ = "DisplayString"
_RadiusclientTableServersecret_Object = MibTableColumn
radiusclientTableServersecret = _RadiusclientTableServersecret_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 7, 1, 5),
    _RadiusclientTableServersecret_Type()
)
radiusclientTableServersecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusclientTableServersecret.setStatus("current")


class _RadiusclientTableComment_Type(DisplayString):
    """Custom type radiusclientTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RadiusclientTableComment_Type.__name__ = "DisplayString"
_RadiusclientTableComment_Object = MibTableColumn
radiusclientTableComment = _RadiusclientTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 7, 1, 6),
    _RadiusclientTableComment_Type()
)
radiusclientTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusclientTableComment.setStatus("current")


class _RadiusclientTableActive_Type(Integer32):
    """Custom type radiusclientTableActive based on Integer32"""
    defaultValue = 1

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


_RadiusclientTableActive_Type.__name__ = "Integer32"
_RadiusclientTableActive_Object = MibTableColumn
radiusclientTableActive = _RadiusclientTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 7, 1, 7),
    _RadiusclientTableActive_Type()
)
radiusclientTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusclientTableActive.setStatus("current")
_RadiusclientTableRowStatus_Type = RowStatus
_RadiusclientTableRowStatus_Object = MibTableColumn
radiusclientTableRowStatus = _RadiusclientTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 24, 7, 1, 8),
    _RadiusclientTableRowStatus_Type()
)
radiusclientTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusclientTableRowStatus.setStatus("current")
_NodeConfigurationHttpd_ObjectIdentity = ObjectIdentity
nodeConfigurationHttpd = _NodeConfigurationHttpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25)
)


class _HttpdActive_Type(Integer32):
    """Custom type httpdActive based on Integer32"""
    defaultValue = 1

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


_HttpdActive_Type.__name__ = "Integer32"
_HttpdActive_Object = MibScalar
httpdActive = _HttpdActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 1),
    _HttpdActive_Type()
)
httpdActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpdActive.setStatus("current")


class _HttpdPort_Type(Integer32):
    """Custom type httpdPort based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HttpdPort_Type.__name__ = "Integer32"
_HttpdPort_Object = MibScalar
httpdPort = _HttpdPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 2),
    _HttpdPort_Type()
)
httpdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpdPort.setStatus("current")


class _HttpdUsername_Type(DisplayString):
    """Custom type httpdUsername based on DisplayString"""
    defaultValue = OctetString("admin")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HttpdUsername_Type.__name__ = "DisplayString"
_HttpdUsername_Object = MibScalar
httpdUsername = _HttpdUsername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 3),
    _HttpdUsername_Type()
)
httpdUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpdUsername.setStatus("current")


class _HttpdPassword_Type(DisplayString):
    """Custom type httpdPassword based on DisplayString"""
    defaultValue = OctetString("admin")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HttpdPassword_Type.__name__ = "DisplayString"
_HttpdPassword_Object = MibScalar
httpdPassword = _HttpdPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 4),
    _HttpdPassword_Type()
)
httpdPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpdPassword.setStatus("current")


class _HttpdAccessctrl_Type(Integer32):
    """Custom type httpdAccessctrl based on Integer32"""
    defaultValue = 1

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


_HttpdAccessctrl_Type.__name__ = "Integer32"
_HttpdAccessctrl_Object = MibScalar
httpdAccessctrl = _HttpdAccessctrl_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 5),
    _HttpdAccessctrl_Type()
)
httpdAccessctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpdAccessctrl.setStatus("current")
_HttpdTable_Object = MibTable
httpdTable = _HttpdTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 6)
)
if mibBuilder.loadTexts:
    httpdTable.setStatus("current")
_HttpdTableEntry_Object = MibTableRow
httpdTableEntry = _HttpdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 6, 1)
)
httpdTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "httpdTableIndex"),
)
if mibBuilder.loadTexts:
    httpdTableEntry.setStatus("current")


class _HttpdTableIndex_Type(Integer32):
    """Custom type httpdTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HttpdTableIndex_Type.__name__ = "Integer32"
_HttpdTableIndex_Object = MibTableColumn
httpdTableIndex = _HttpdTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 6, 1, 1),
    _HttpdTableIndex_Type()
)
httpdTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    httpdTableIndex.setStatus("current")


class _HttpdTableDevice_Type(OctetString):
    """Custom type httpdTableDevice based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HttpdTableDevice_Type.__name__ = "OctetString"
_HttpdTableDevice_Object = MibTableColumn
httpdTableDevice = _HttpdTableDevice_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 6, 1, 2),
    _HttpdTableDevice_Type()
)
httpdTableDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    httpdTableDevice.setStatus("current")
_HttpdTableSubnet_Type = IpAddress
_HttpdTableSubnet_Object = MibTableColumn
httpdTableSubnet = _HttpdTableSubnet_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 6, 1, 3),
    _HttpdTableSubnet_Type()
)
httpdTableSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    httpdTableSubnet.setStatus("current")
_HttpdTableNetmask_Type = IpAddress
_HttpdTableNetmask_Object = MibTableColumn
httpdTableNetmask = _HttpdTableNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 6, 1, 4),
    _HttpdTableNetmask_Type()
)
httpdTableNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    httpdTableNetmask.setStatus("current")


class _HttpdTableDevnet_Type(Integer32):
    """Custom type httpdTableDevnet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("device", 1),
          ("network", 2))
    )


_HttpdTableDevnet_Type.__name__ = "Integer32"
_HttpdTableDevnet_Object = MibTableColumn
httpdTableDevnet = _HttpdTableDevnet_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 6, 1, 5),
    _HttpdTableDevnet_Type()
)
httpdTableDevnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    httpdTableDevnet.setStatus("current")


class _HttpdTableComment_Type(DisplayString):
    """Custom type httpdTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HttpdTableComment_Type.__name__ = "DisplayString"
_HttpdTableComment_Object = MibTableColumn
httpdTableComment = _HttpdTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 6, 1, 6),
    _HttpdTableComment_Type()
)
httpdTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    httpdTableComment.setStatus("current")


class _HttpdTableActive_Type(Integer32):
    """Custom type httpdTableActive based on Integer32"""
    defaultValue = 1

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


_HttpdTableActive_Type.__name__ = "Integer32"
_HttpdTableActive_Object = MibTableColumn
httpdTableActive = _HttpdTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 6, 1, 7),
    _HttpdTableActive_Type()
)
httpdTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    httpdTableActive.setStatus("current")
_HttpdTableRowStatus_Type = RowStatus
_HttpdTableRowStatus_Object = MibTableColumn
httpdTableRowStatus = _HttpdTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 6, 1, 8),
    _HttpdTableRowStatus_Type()
)
httpdTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    httpdTableRowStatus.setStatus("current")


class _HttpdCertPassword_Type(DisplayString):
    """Custom type httpdCertPassword based on DisplayString"""
    defaultValue = OctetString("httpconf")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HttpdCertPassword_Type.__name__ = "DisplayString"
_HttpdCertPassword_Object = MibScalar
httpdCertPassword = _HttpdCertPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 25, 7),
    _HttpdCertPassword_Type()
)
httpdCertPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpdCertPassword.setStatus("current")
_NodeConfigurationSnmpd_ObjectIdentity = ObjectIdentity
nodeConfigurationSnmpd = _NodeConfigurationSnmpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26)
)


class _SnmpdActive_Type(Integer32):
    """Custom type snmpdActive based on Integer32"""
    defaultValue = 1

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


_SnmpdActive_Type.__name__ = "Integer32"
_SnmpdActive_Object = MibScalar
snmpdActive = _SnmpdActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 1),
    _SnmpdActive_Type()
)
snmpdActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdActive.setStatus("current")


class _SnmpdVersion_Type(Integer32):
    """Custom type snmpdVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("v1o2c", 1),
          ("v3", 2))
    )


_SnmpdVersion_Type.__name__ = "Integer32"
_SnmpdVersion_Object = MibScalar
snmpdVersion = _SnmpdVersion_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 2),
    _SnmpdVersion_Type()
)
snmpdVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdVersion.setStatus("current")


class _SnmpdPort_Type(Integer32):
    """Custom type snmpdPort based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpdPort_Type.__name__ = "Integer32"
_SnmpdPort_Object = MibScalar
snmpdPort = _SnmpdPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 3),
    _SnmpdPort_Type()
)
snmpdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdPort.setStatus("current")


class _SnmpdReadcommunity_Type(DisplayString):
    """Custom type snmpdReadcommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_SnmpdReadcommunity_Type.__name__ = "DisplayString"
_SnmpdReadcommunity_Object = MibScalar
snmpdReadcommunity = _SnmpdReadcommunity_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 4),
    _SnmpdReadcommunity_Type()
)
snmpdReadcommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdReadcommunity.setStatus("current")


class _SnmpdWritecommunity_Type(DisplayString):
    """Custom type snmpdWritecommunity based on DisplayString"""
    defaultValue = OctetString("private")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_SnmpdWritecommunity_Type.__name__ = "DisplayString"
_SnmpdWritecommunity_Object = MibScalar
snmpdWritecommunity = _SnmpdWritecommunity_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 5),
    _SnmpdWritecommunity_Type()
)
snmpdWritecommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdWritecommunity.setStatus("current")


class _SnmpdReadusername_Type(DisplayString):
    """Custom type snmpdReadusername based on DisplayString"""
    defaultValue = OctetString("snmpv3rouser")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 50),
    )


_SnmpdReadusername_Type.__name__ = "DisplayString"
_SnmpdReadusername_Object = MibScalar
snmpdReadusername = _SnmpdReadusername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 6),
    _SnmpdReadusername_Type()
)
snmpdReadusername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdReadusername.setStatus("current")


class _SnmpdWriteusername_Type(DisplayString):
    """Custom type snmpdWriteusername based on DisplayString"""
    defaultValue = OctetString("snmpv3rwuser")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 50),
    )


_SnmpdWriteusername_Type.__name__ = "DisplayString"
_SnmpdWriteusername_Object = MibScalar
snmpdWriteusername = _SnmpdWriteusername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 7),
    _SnmpdWriteusername_Type()
)
snmpdWriteusername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdWriteusername.setStatus("current")


class _SnmpdPassword_Type(DisplayString):
    """Custom type snmpdPassword based on DisplayString"""
    defaultValue = OctetString("snmpv3password")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 50),
    )


_SnmpdPassword_Type.__name__ = "DisplayString"
_SnmpdPassword_Object = MibScalar
snmpdPassword = _SnmpdPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 8),
    _SnmpdPassword_Type()
)
snmpdPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdPassword.setStatus("current")


class _SnmpdPassphrase_Type(DisplayString):
    """Custom type snmpdPassphrase based on DisplayString"""
    defaultValue = OctetString("snmpv3passphrase")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 50),
    )


_SnmpdPassphrase_Type.__name__ = "DisplayString"
_SnmpdPassphrase_Object = MibScalar
snmpdPassphrase = _SnmpdPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 9),
    _SnmpdPassphrase_Type()
)
snmpdPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdPassphrase.setStatus("current")


class _SnmpdAccessctrl_Type(Integer32):
    """Custom type snmpdAccessctrl based on Integer32"""
    defaultValue = 1

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


_SnmpdAccessctrl_Type.__name__ = "Integer32"
_SnmpdAccessctrl_Object = MibScalar
snmpdAccessctrl = _SnmpdAccessctrl_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 10),
    _SnmpdAccessctrl_Type()
)
snmpdAccessctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpdAccessctrl.setStatus("current")
_SnmpdTable_Object = MibTable
snmpdTable = _SnmpdTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 11)
)
if mibBuilder.loadTexts:
    snmpdTable.setStatus("current")
_SnmpdTableEntry_Object = MibTableRow
snmpdTableEntry = _SnmpdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 11, 1)
)
snmpdTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "snmpdTableIndex"),
)
if mibBuilder.loadTexts:
    snmpdTableEntry.setStatus("current")


class _SnmpdTableIndex_Type(Integer32):
    """Custom type snmpdTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SnmpdTableIndex_Type.__name__ = "Integer32"
_SnmpdTableIndex_Object = MibTableColumn
snmpdTableIndex = _SnmpdTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 11, 1, 1),
    _SnmpdTableIndex_Type()
)
snmpdTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpdTableIndex.setStatus("current")


class _SnmpdTableDevice_Type(OctetString):
    """Custom type snmpdTableDevice based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpdTableDevice_Type.__name__ = "OctetString"
_SnmpdTableDevice_Object = MibTableColumn
snmpdTableDevice = _SnmpdTableDevice_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 11, 1, 2),
    _SnmpdTableDevice_Type()
)
snmpdTableDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpdTableDevice.setStatus("current")
_SnmpdTableSubnet_Type = IpAddress
_SnmpdTableSubnet_Object = MibTableColumn
snmpdTableSubnet = _SnmpdTableSubnet_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 11, 1, 3),
    _SnmpdTableSubnet_Type()
)
snmpdTableSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpdTableSubnet.setStatus("current")
_SnmpdTableNetmask_Type = IpAddress
_SnmpdTableNetmask_Object = MibTableColumn
snmpdTableNetmask = _SnmpdTableNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 11, 1, 4),
    _SnmpdTableNetmask_Type()
)
snmpdTableNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpdTableNetmask.setStatus("current")


class _SnmpdTableDevnet_Type(Integer32):
    """Custom type snmpdTableDevnet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("device", 1),
          ("network", 2))
    )


_SnmpdTableDevnet_Type.__name__ = "Integer32"
_SnmpdTableDevnet_Object = MibTableColumn
snmpdTableDevnet = _SnmpdTableDevnet_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 11, 1, 5),
    _SnmpdTableDevnet_Type()
)
snmpdTableDevnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpdTableDevnet.setStatus("current")


class _SnmpdTableComment_Type(DisplayString):
    """Custom type snmpdTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpdTableComment_Type.__name__ = "DisplayString"
_SnmpdTableComment_Object = MibTableColumn
snmpdTableComment = _SnmpdTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 11, 1, 6),
    _SnmpdTableComment_Type()
)
snmpdTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpdTableComment.setStatus("current")


class _SnmpdTableActive_Type(Integer32):
    """Custom type snmpdTableActive based on Integer32"""
    defaultValue = 1

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


_SnmpdTableActive_Type.__name__ = "Integer32"
_SnmpdTableActive_Object = MibTableColumn
snmpdTableActive = _SnmpdTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 11, 1, 7),
    _SnmpdTableActive_Type()
)
snmpdTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpdTableActive.setStatus("current")
_SnmpdTableRowStatus_Type = RowStatus
_SnmpdTableRowStatus_Object = MibTableColumn
snmpdTableRowStatus = _SnmpdTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 26, 11, 1, 8),
    _SnmpdTableRowStatus_Type()
)
snmpdTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpdTableRowStatus.setStatus("current")
_NodeConfigurationTrap_ObjectIdentity = ObjectIdentity
nodeConfigurationTrap = _NodeConfigurationTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27)
)


class _TrapActive_Type(Integer32):
    """Custom type trapActive based on Integer32"""
    defaultValue = 2

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


_TrapActive_Type.__name__ = "Integer32"
_TrapActive_Object = MibScalar
trapActive = _TrapActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 1),
    _TrapActive_Type()
)
trapActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActive.setStatus("current")


class _TrapConfiguration_Type(Integer32):
    """Custom type trapConfiguration based on Integer32"""
    defaultValue = 1

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


_TrapConfiguration_Type.__name__ = "Integer32"
_TrapConfiguration_Object = MibScalar
trapConfiguration = _TrapConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 2),
    _TrapConfiguration_Type()
)
trapConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapConfiguration.setStatus("current")


class _TrapSecurity_Type(Integer32):
    """Custom type trapSecurity based on Integer32"""
    defaultValue = 1

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


_TrapSecurity_Type.__name__ = "Integer32"
_TrapSecurity_Object = MibScalar
trapSecurity = _TrapSecurity_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 3),
    _TrapSecurity_Type()
)
trapSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSecurity.setStatus("current")


class _TrapWireless_Type(Integer32):
    """Custom type trapWireless based on Integer32"""
    defaultValue = 1

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


_TrapWireless_Type.__name__ = "Integer32"
_TrapWireless_Object = MibScalar
trapWireless = _TrapWireless_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 4),
    _TrapWireless_Type()
)
trapWireless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapWireless.setStatus("current")


class _TrapOperational_Type(Integer32):
    """Custom type trapOperational based on Integer32"""
    defaultValue = 1

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


_TrapOperational_Type.__name__ = "Integer32"
_TrapOperational_Object = MibScalar
trapOperational = _TrapOperational_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 5),
    _TrapOperational_Type()
)
trapOperational.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapOperational.setStatus("current")


class _TrapFlash_Type(Integer32):
    """Custom type trapFlash based on Integer32"""
    defaultValue = 1

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


_TrapFlash_Type.__name__ = "Integer32"
_TrapFlash_Object = MibScalar
trapFlash = _TrapFlash_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 6),
    _TrapFlash_Type()
)
trapFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapFlash.setStatus("current")


class _TrapTftp_Type(Integer32):
    """Custom type trapTftp based on Integer32"""
    defaultValue = 1

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


_TrapTftp_Type.__name__ = "Integer32"
_TrapTftp_Object = MibScalar
trapTftp = _TrapTftp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 7),
    _TrapTftp_Type()
)
trapTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapTftp.setStatus("current")


class _TrapImage_Type(Integer32):
    """Custom type trapImage based on Integer32"""
    defaultValue = 1

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


_TrapImage_Type.__name__ = "Integer32"
_TrapImage_Object = MibScalar
trapImage = _TrapImage_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 8),
    _TrapImage_Type()
)
trapImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapImage.setStatus("current")


class _TrapAuthentication_Type(Integer32):
    """Custom type trapAuthentication based on Integer32"""
    defaultValue = 1

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


_TrapAuthentication_Type.__name__ = "Integer32"
_TrapAuthentication_Object = MibScalar
trapAuthentication = _TrapAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 9),
    _TrapAuthentication_Type()
)
trapAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAuthentication.setStatus("current")
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("current")
_TrapTableEntry_Object = MibTableRow
trapTableEntry = _TrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1)
)
trapTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "trapTableIndex"),
)
if mibBuilder.loadTexts:
    trapTableEntry.setStatus("current")


class _TrapTableIndex_Type(Integer32):
    """Custom type trapTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TrapTableIndex_Type.__name__ = "Integer32"
_TrapTableIndex_Object = MibTableColumn
trapTableIndex = _TrapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1, 1),
    _TrapTableIndex_Type()
)
trapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapTableIndex.setStatus("current")
_TrapTableIp_Type = IpAddress
_TrapTableIp_Object = MibTableColumn
trapTableIp = _TrapTableIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1, 2),
    _TrapTableIp_Type()
)
trapTableIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapTableIp.setStatus("current")


class _TrapTableCommunity_Type(DisplayString):
    """Custom type trapTableCommunity based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 32),
    )


_TrapTableCommunity_Type.__name__ = "DisplayString"
_TrapTableCommunity_Object = MibTableColumn
trapTableCommunity = _TrapTableCommunity_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1, 3),
    _TrapTableCommunity_Type()
)
trapTableCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapTableCommunity.setStatus("current")


class _TrapTableUsername_Type(DisplayString):
    """Custom type trapTableUsername based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 50),
    )


_TrapTableUsername_Type.__name__ = "DisplayString"
_TrapTableUsername_Object = MibTableColumn
trapTableUsername = _TrapTableUsername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1, 4),
    _TrapTableUsername_Type()
)
trapTableUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapTableUsername.setStatus("current")


class _TrapTableAuthpasswd_Type(DisplayString):
    """Custom type trapTableAuthpasswd based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 50),
    )


_TrapTableAuthpasswd_Type.__name__ = "DisplayString"
_TrapTableAuthpasswd_Object = MibTableColumn
trapTableAuthpasswd = _TrapTableAuthpasswd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1, 5),
    _TrapTableAuthpasswd_Type()
)
trapTableAuthpasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapTableAuthpasswd.setStatus("current")


class _TrapTablePrivpasswd_Type(DisplayString):
    """Custom type trapTablePrivpasswd based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 50),
    )


_TrapTablePrivpasswd_Type.__name__ = "DisplayString"
_TrapTablePrivpasswd_Object = MibTableColumn
trapTablePrivpasswd = _TrapTablePrivpasswd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1, 6),
    _TrapTablePrivpasswd_Type()
)
trapTablePrivpasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapTablePrivpasswd.setStatus("current")


class _TrapTableVersion_Type(Integer32):
    """Custom type trapTableVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version2c", 1),
          ("version3", 2))
    )


_TrapTableVersion_Type.__name__ = "Integer32"
_TrapTableVersion_Object = MibTableColumn
trapTableVersion = _TrapTableVersion_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1, 7),
    _TrapTableVersion_Type()
)
trapTableVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapTableVersion.setStatus("current")


class _TrapTableComment_Type(DisplayString):
    """Custom type trapTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrapTableComment_Type.__name__ = "DisplayString"
_TrapTableComment_Object = MibTableColumn
trapTableComment = _TrapTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1, 8),
    _TrapTableComment_Type()
)
trapTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapTableComment.setStatus("current")


class _TrapTableActive_Type(Integer32):
    """Custom type trapTableActive based on Integer32"""
    defaultValue = 1

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


_TrapTableActive_Type.__name__ = "Integer32"
_TrapTableActive_Object = MibTableColumn
trapTableActive = _TrapTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1, 9),
    _TrapTableActive_Type()
)
trapTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapTableActive.setStatus("current")
_TrapTableRowStatus_Type = RowStatus
_TrapTableRowStatus_Object = MibTableColumn
trapTableRowStatus = _TrapTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 27, 10, 1, 10),
    _TrapTableRowStatus_Type()
)
trapTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapTableRowStatus.setStatus("current")
_NodeConfigurationDdns_ObjectIdentity = ObjectIdentity
nodeConfigurationDdns = _NodeConfigurationDdns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 28)
)


class _DdnsActive_Type(Integer32):
    """Custom type ddnsActive based on Integer32"""
    defaultValue = 1

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


_DdnsActive_Type.__name__ = "Integer32"
_DdnsActive_Object = MibScalar
ddnsActive = _DdnsActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 28, 1),
    _DdnsActive_Type()
)
ddnsActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsActive.setStatus("current")


class _DdnsServer_Type(Integer32):
    """Custom type ddnsServer based on Integer32"""
    defaultValue = 1

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
        *(("dyndns", 1),
          ("easydns", 2),
          ("no-ip", 3),
          ("tzo", 5),
          ("zoneedit", 4))
    )


_DdnsServer_Type.__name__ = "Integer32"
_DdnsServer_Object = MibScalar
ddnsServer = _DdnsServer_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 28, 2),
    _DdnsServer_Type()
)
ddnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsServer.setStatus("current")


class _DdnsHostname_Type(DisplayString):
    """Custom type ddnsHostname based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_DdnsHostname_Type.__name__ = "DisplayString"
_DdnsHostname_Object = MibScalar
ddnsHostname = _DdnsHostname_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 28, 3),
    _DdnsHostname_Type()
)
ddnsHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsHostname.setStatus("current")


class _DdnsUsername_Type(DisplayString):
    """Custom type ddnsUsername based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DdnsUsername_Type.__name__ = "DisplayString"
_DdnsUsername_Object = MibScalar
ddnsUsername = _DdnsUsername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 28, 4),
    _DdnsUsername_Type()
)
ddnsUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsUsername.setStatus("current")


class _DdnsPassword_Type(DisplayString):
    """Custom type ddnsPassword based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DdnsPassword_Type.__name__ = "DisplayString"
_DdnsPassword_Object = MibScalar
ddnsPassword = _DdnsPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 28, 5),
    _DdnsPassword_Type()
)
ddnsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsPassword.setStatus("current")
_NodeConfigurationZeroconfig_ObjectIdentity = ObjectIdentity
nodeConfigurationZeroconfig = _NodeConfigurationZeroconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 29)
)


class _ZeroconfigActive_Type(Integer32):
    """Custom type zeroconfigActive based on Integer32"""
    defaultValue = 2

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


_ZeroconfigActive_Type.__name__ = "Integer32"
_ZeroconfigActive_Object = MibScalar
zeroconfigActive = _ZeroconfigActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 29, 1),
    _ZeroconfigActive_Type()
)
zeroconfigActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zeroconfigActive.setStatus("current")


class _ZeroconfigProxyActive_Type(Integer32):
    """Custom type zeroconfigProxyActive based on Integer32"""
    defaultValue = 1

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


_ZeroconfigProxyActive_Type.__name__ = "Integer32"
_ZeroconfigProxyActive_Object = MibScalar
zeroconfigProxyActive = _ZeroconfigProxyActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 29, 2),
    _ZeroconfigProxyActive_Type()
)
zeroconfigProxyActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zeroconfigProxyActive.setStatus("current")


class _ZeroconfigProxyport_Type(Integer32):
    """Custom type zeroconfigProxyport based on Integer32"""
    defaultValue = 8080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_ZeroconfigProxyport_Type.__name__ = "Integer32"
_ZeroconfigProxyport_Object = MibScalar
zeroconfigProxyport = _ZeroconfigProxyport_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 29, 3),
    _ZeroconfigProxyport_Type()
)
zeroconfigProxyport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zeroconfigProxyport.setStatus("current")


class _ZeroconfigStaticipActive_Type(Integer32):
    """Custom type zeroconfigStaticipActive based on Integer32"""
    defaultValue = 1

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


_ZeroconfigStaticipActive_Type.__name__ = "Integer32"
_ZeroconfigStaticipActive_Object = MibScalar
zeroconfigStaticipActive = _ZeroconfigStaticipActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 29, 4),
    _ZeroconfigStaticipActive_Type()
)
zeroconfigStaticipActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zeroconfigStaticipActive.setStatus("current")
_NodeConfigurationSignallevel_ObjectIdentity = ObjectIdentity
nodeConfigurationSignallevel = _NodeConfigurationSignallevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30)
)


class _SignallevelExecute_Type(Integer32):
    """Custom type signallevelExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SignallevelExecute_Type.__name__ = "Integer32"
_SignallevelExecute_Object = MibScalar
signallevelExecute = _SignallevelExecute_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 1),
    _SignallevelExecute_Type()
)
signallevelExecute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallevelExecute.setStatus("current")
_SignallevelTable_Object = MibTable
signallevelTable = _SignallevelTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2)
)
if mibBuilder.loadTexts:
    signallevelTable.setStatus("current")
_SignallevelTableEntry_Object = MibTableRow
signallevelTableEntry = _SignallevelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2, 1)
)
signallevelTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "signallevelTableIndex"),
)
if mibBuilder.loadTexts:
    signallevelTableEntry.setStatus("current")


class _SignallevelTableIndex_Type(Integer32):
    """Custom type signallevelTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SignallevelTableIndex_Type.__name__ = "Integer32"
_SignallevelTableIndex_Object = MibTableColumn
signallevelTableIndex = _SignallevelTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2, 1, 1),
    _SignallevelTableIndex_Type()
)
signallevelTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    signallevelTableIndex.setStatus("current")
_SignallevelTableSource_Type = OctetString
_SignallevelTableSource_Object = MibTableColumn
signallevelTableSource = _SignallevelTableSource_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2, 1, 2),
    _SignallevelTableSource_Type()
)
signallevelTableSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallevelTableSource.setStatus("current")
_SignallevelTableDestination_Type = OctetString
_SignallevelTableDestination_Object = MibTableColumn
signallevelTableDestination = _SignallevelTableDestination_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2, 1, 3),
    _SignallevelTableDestination_Type()
)
signallevelTableDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallevelTableDestination.setStatus("current")
_SignallevelTableRssi_Type = OctetString
_SignallevelTableRssi_Object = MibTableColumn
signallevelTableRssi = _SignallevelTableRssi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2, 1, 4),
    _SignallevelTableRssi_Type()
)
signallevelTableRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallevelTableRssi.setStatus("current")
_ClientInfoTable_Object = MibTable
clientInfoTable = _ClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3)
)
if mibBuilder.loadTexts:
    clientInfoTable.setStatus("current")
_ClientInfoTableEntry_Object = MibTableRow
clientInfoTableEntry = _ClientInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1)
)
clientInfoTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "clientInfoTableIndex"),
)
if mibBuilder.loadTexts:
    clientInfoTableEntry.setStatus("current")


class _ClientInfoTableIndex_Type(Integer32):
    """Custom type clientInfoTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_ClientInfoTableIndex_Type.__name__ = "Integer32"
_ClientInfoTableIndex_Object = MibTableColumn
clientInfoTableIndex = _ClientInfoTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 1),
    _ClientInfoTableIndex_Type()
)
clientInfoTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clientInfoTableIndex.setStatus("current")
_ClientInfoTableEssid_Type = OctetString
_ClientInfoTableEssid_Object = MibTableColumn
clientInfoTableEssid = _ClientInfoTableEssid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 2),
    _ClientInfoTableEssid_Type()
)
clientInfoTableEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableEssid.setStatus("current")
_ClientInfoTableMac_Type = OctetString
_ClientInfoTableMac_Object = MibTableColumn
clientInfoTableMac = _ClientInfoTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 3),
    _ClientInfoTableMac_Type()
)
clientInfoTableMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableMac.setStatus("current")
_ClientInfoTableChannel_Type = OctetString
_ClientInfoTableChannel_Object = MibTableColumn
clientInfoTableChannel = _ClientInfoTableChannel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 4),
    _ClientInfoTableChannel_Type()
)
clientInfoTableChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableChannel.setStatus("current")
_ClientInfoTableRate_Type = OctetString
_ClientInfoTableRate_Object = MibTableColumn
clientInfoTableRate = _ClientInfoTableRate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 5),
    _ClientInfoTableRate_Type()
)
clientInfoTableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableRate.setStatus("current")
_ClientInfoTableRssi_Type = OctetString
_ClientInfoTableRssi_Object = MibTableColumn
clientInfoTableRssi = _ClientInfoTableRssi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 6),
    _ClientInfoTableRssi_Type()
)
clientInfoTableRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableRssi.setStatus("current")
_ClientInfoTableIdletime_Type = OctetString
_ClientInfoTableIdletime_Object = MibTableColumn
clientInfoTableIdletime = _ClientInfoTableIdletime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 7),
    _ClientInfoTableIdletime_Type()
)
clientInfoTableIdletime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableIdletime.setStatus("current")
_ClientStatTable_Object = MibTable
clientStatTable = _ClientStatTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 4)
)
if mibBuilder.loadTexts:
    clientStatTable.setStatus("current")
_ClientStatTableEntry_Object = MibTableRow
clientStatTableEntry = _ClientStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 4, 1)
)
clientStatTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "clientStatTableIndex"),
)
if mibBuilder.loadTexts:
    clientStatTableEntry.setStatus("current")


class _ClientStatTableIndex_Type(Integer32):
    """Custom type clientStatTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_ClientStatTableIndex_Type.__name__ = "Integer32"
_ClientStatTableIndex_Object = MibTableColumn
clientStatTableIndex = _ClientStatTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 4, 1, 1),
    _ClientStatTableIndex_Type()
)
clientStatTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clientStatTableIndex.setStatus("current")
_ClientStatTableIp_Type = IpAddress
_ClientStatTableIp_Object = MibTableColumn
clientStatTableIp = _ClientStatTableIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 4, 1, 2),
    _ClientStatTableIp_Type()
)
clientStatTableIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientStatTableIp.setStatus("current")
_ClientStatTableMac_Type = MacAddress
_ClientStatTableMac_Object = MibTableColumn
clientStatTableMac = _ClientStatTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 4, 1, 3),
    _ClientStatTableMac_Type()
)
clientStatTableMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientStatTableMac.setStatus("current")
_ClientStatTableTx_Type = OctetString
_ClientStatTableTx_Object = MibTableColumn
clientStatTableTx = _ClientStatTableTx_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 4, 1, 4),
    _ClientStatTableTx_Type()
)
clientStatTableTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientStatTableTx.setStatus("current")
_ClientStatTableRx_Type = OctetString
_ClientStatTableRx_Object = MibTableColumn
clientStatTableRx = _ClientStatTableRx_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 4, 1, 5),
    _ClientStatTableRx_Type()
)
clientStatTableRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientStatTableRx.setStatus("current")
_ClientStatTableTxPkt_Type = OctetString
_ClientStatTableTxPkt_Object = MibTableColumn
clientStatTableTxPkt = _ClientStatTableTxPkt_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 4, 1, 6),
    _ClientStatTableTxPkt_Type()
)
clientStatTableTxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientStatTableTxPkt.setStatus("current")
_ClientStatTableRxPkt_Type = OctetString
_ClientStatTableRxPkt_Object = MibTableColumn
clientStatTableRxPkt = _ClientStatTableRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 4, 1, 7),
    _ClientStatTableRxPkt_Type()
)
clientStatTableRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientStatTableRxPkt.setStatus("current")
_ClientStatTableOnlinetime_Type = OctetString
_ClientStatTableOnlinetime_Object = MibTableColumn
clientStatTableOnlinetime = _ClientStatTableOnlinetime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 4, 1, 8),
    _ClientStatTableOnlinetime_Type()
)
clientStatTableOnlinetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientStatTableOnlinetime.setStatus("current")
_NodeConfigurationIpsec_ObjectIdentity = ObjectIdentity
nodeConfigurationIpsec = _NodeConfigurationIpsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31)
)


class _IpsecActive_Type(Integer32):
    """Custom type ipsecActive based on Integer32"""
    defaultValue = 1

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


_IpsecActive_Type.__name__ = "Integer32"
_IpsecActive_Object = MibScalar
ipsecActive = _IpsecActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 1),
    _IpsecActive_Type()
)
ipsecActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecActive.setStatus("current")


class _IpsecType_Type(Integer32):
    """Custom type ipsecType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("psk", 3),
          ("rsa", 2),
          ("x509", 1))
    )


_IpsecType_Type.__name__ = "Integer32"
_IpsecType_Object = MibScalar
ipsecType = _IpsecType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 2),
    _IpsecType_Type()
)
ipsecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecType.setStatus("current")


class _IpsecLocalId_Type(OctetString):
    """Custom type ipsecLocalId based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IpsecLocalId_Type.__name__ = "OctetString"
_IpsecLocalId_Object = MibScalar
ipsecLocalId = _IpsecLocalId_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 3),
    _IpsecLocalId_Type()
)
ipsecLocalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecLocalId.setStatus("current")


class _IpsecRemoteId_Type(OctetString):
    """Custom type ipsecRemoteId based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IpsecRemoteId_Type.__name__ = "OctetString"
_IpsecRemoteId_Object = MibScalar
ipsecRemoteId = _IpsecRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 4),
    _IpsecRemoteId_Type()
)
ipsecRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecRemoteId.setStatus("current")
_IpsecRemoteIp_Type = IpAddress
_IpsecRemoteIp_Object = MibScalar
ipsecRemoteIp = _IpsecRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 5),
    _IpsecRemoteIp_Type()
)
ipsecRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecRemoteIp.setStatus("current")
_IpsecRemoteSubnet_Type = IpAddress
_IpsecRemoteSubnet_Object = MibScalar
ipsecRemoteSubnet = _IpsecRemoteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 6),
    _IpsecRemoteSubnet_Type()
)
ipsecRemoteSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecRemoteSubnet.setStatus("current")
_IpsecRemoteNetmask_Type = IpAddress
_IpsecRemoteNetmask_Object = MibScalar
ipsecRemoteNetmask = _IpsecRemoteNetmask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 7),
    _IpsecRemoteNetmask_Type()
)
ipsecRemoteNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecRemoteNetmask.setStatus("current")


class _IpsecLocalCertpass_Type(OctetString):
    """Custom type ipsecLocalCertpass based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_IpsecLocalCertpass_Type.__name__ = "OctetString"
_IpsecLocalCertpass_Object = MibScalar
ipsecLocalCertpass = _IpsecLocalCertpass_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 8),
    _IpsecLocalCertpass_Type()
)
ipsecLocalCertpass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecLocalCertpass.setStatus("current")


class _IpsecLocalRsa_Type(OctetString):
    """Custom type ipsecLocalRsa based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_IpsecLocalRsa_Type.__name__ = "OctetString"
_IpsecLocalRsa_Object = MibScalar
ipsecLocalRsa = _IpsecLocalRsa_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 9),
    _IpsecLocalRsa_Type()
)
ipsecLocalRsa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecLocalRsa.setStatus("current")


class _IpsecRemoteRsa_Type(OctetString):
    """Custom type ipsecRemoteRsa based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_IpsecRemoteRsa_Type.__name__ = "OctetString"
_IpsecRemoteRsa_Object = MibScalar
ipsecRemoteRsa = _IpsecRemoteRsa_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 10),
    _IpsecRemoteRsa_Type()
)
ipsecRemoteRsa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecRemoteRsa.setStatus("current")


class _IpsecPsk_Type(OctetString):
    """Custom type ipsecPsk based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_IpsecPsk_Type.__name__ = "OctetString"
_IpsecPsk_Object = MibScalar
ipsecPsk = _IpsecPsk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 31, 11),
    _IpsecPsk_Type()
)
ipsecPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsecPsk.setStatus("current")
_NodeConfigurationL2tpc_ObjectIdentity = ObjectIdentity
nodeConfigurationL2tpc = _NodeConfigurationL2tpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 32)
)


class _L2tpcActive_Type(Integer32):
    """Custom type l2tpcActive based on Integer32"""
    defaultValue = 1

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


_L2tpcActive_Type.__name__ = "Integer32"
_L2tpcActive_Object = MibScalar
l2tpcActive = _L2tpcActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 32, 1),
    _L2tpcActive_Type()
)
l2tpcActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpcActive.setStatus("current")


class _L2tpcLns_Type(OctetString):
    """Custom type l2tpcLns based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_L2tpcLns_Type.__name__ = "OctetString"
_L2tpcLns_Object = MibScalar
l2tpcLns = _L2tpcLns_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 32, 2),
    _L2tpcLns_Type()
)
l2tpcLns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpcLns.setStatus("current")


class _L2tpcUsername_Type(DisplayString):
    """Custom type l2tpcUsername based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_L2tpcUsername_Type.__name__ = "DisplayString"
_L2tpcUsername_Object = MibScalar
l2tpcUsername = _L2tpcUsername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 32, 3),
    _L2tpcUsername_Type()
)
l2tpcUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpcUsername.setStatus("current")


class _L2tpcSecret_Type(DisplayString):
    """Custom type l2tpcSecret based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_L2tpcSecret_Type.__name__ = "DisplayString"
_L2tpcSecret_Object = MibScalar
l2tpcSecret = _L2tpcSecret_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 32, 4),
    _L2tpcSecret_Type()
)
l2tpcSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpcSecret.setStatus("current")
_NodeConfigurationAutoip_ObjectIdentity = ObjectIdentity
nodeConfigurationAutoip = _NodeConfigurationAutoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 33)
)


class _AutoipActive_Type(Integer32):
    """Custom type autoipActive based on Integer32"""
    defaultValue = 1

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


_AutoipActive_Type.__name__ = "Integer32"
_AutoipActive_Object = MibScalar
autoipActive = _AutoipActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 33, 1),
    _AutoipActive_Type()
)
autoipActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoipActive.setStatus("current")


class _AutoipMeship_Type(Integer32):
    """Custom type autoipMeship based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AutoipMeship_Type.__name__ = "Integer32"
_AutoipMeship_Object = MibScalar
autoipMeship = _AutoipMeship_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 33, 2),
    _AutoipMeship_Type()
)
autoipMeship.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoipMeship.setStatus("current")


class _AutoipVlanip_Type(Integer32):
    """Custom type autoipVlanip based on Integer32"""
    defaultValue = 172

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AutoipVlanip_Type.__name__ = "Integer32"
_AutoipVlanip_Object = MibScalar
autoipVlanip = _AutoipVlanip_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 33, 3),
    _AutoipVlanip_Type()
)
autoipVlanip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoipVlanip.setStatus("current")
_NodeConfigurationInterfaces_ObjectIdentity = ObjectIdentity
nodeConfigurationInterfaces = _NodeConfigurationInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 34)
)
_InterfacesTable_Object = MibTable
interfacesTable = _InterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 34, 1)
)
if mibBuilder.loadTexts:
    interfacesTable.setStatus("current")
_InterfacesTableEntry_Object = MibTableRow
interfacesTableEntry = _InterfacesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 34, 1, 1)
)
interfacesTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "interfacesTableIndex"),
)
if mibBuilder.loadTexts:
    interfacesTableEntry.setStatus("current")


class _InterfacesTableIndex_Type(Integer32):
    """Custom type interfacesTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_InterfacesTableIndex_Type.__name__ = "Integer32"
_InterfacesTableIndex_Object = MibTableColumn
interfacesTableIndex = _InterfacesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 34, 1, 1, 1),
    _InterfacesTableIndex_Type()
)
interfacesTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfacesTableIndex.setStatus("current")
_InterfacesTableDev_Type = OctetString
_InterfacesTableDev_Object = MibTableColumn
interfacesTableDev = _InterfacesTableDev_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 34, 1, 1, 2),
    _InterfacesTableDev_Type()
)
interfacesTableDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacesTableDev.setStatus("current")
_InterfacesTableLabel_Type = OctetString
_InterfacesTableLabel_Object = MibTableColumn
interfacesTableLabel = _InterfacesTableLabel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 34, 1, 1, 3),
    _InterfacesTableLabel_Type()
)
interfacesTableLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacesTableLabel.setStatus("current")
_NodeConfigurationMlrd_ObjectIdentity = ObjectIdentity
nodeConfigurationMlrd = _NodeConfigurationMlrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35)
)


class _MlrdActive_Type(Integer32):
    """Custom type mlrdActive based on Integer32"""
    defaultValue = 1

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


_MlrdActive_Type.__name__ = "Integer32"
_MlrdActive_Object = MibScalar
mlrdActive = _MlrdActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 1),
    _MlrdActive_Type()
)
mlrdActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlrdActive.setStatus("current")


class _MlrdNetname_Type(OctetString):
    """Custom type mlrdNetname based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MlrdNetname_Type.__name__ = "OctetString"
_MlrdNetname_Object = MibScalar
mlrdNetname = _MlrdNetname_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 2),
    _MlrdNetname_Type()
)
mlrdNetname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlrdNetname.setStatus("current")


class _MlrdBackupActive_Type(Integer32):
    """Custom type mlrdBackupActive based on Integer32"""
    defaultValue = 2

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


_MlrdBackupActive_Type.__name__ = "Integer32"
_MlrdBackupActive_Object = MibScalar
mlrdBackupActive = _MlrdBackupActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 3),
    _MlrdBackupActive_Type()
)
mlrdBackupActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlrdBackupActive.setStatus("current")


class _MlrdRole_Type(Integer32):
    """Custom type mlrdRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_MlrdRole_Type.__name__ = "Integer32"
_MlrdRole_Object = MibScalar
mlrdRole = _MlrdRole_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 4),
    _MlrdRole_Type()
)
mlrdRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlrdRole.setStatus("current")


class _MlrdPeer_Type(OctetString):
    """Custom type mlrdPeer based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MlrdPeer_Type.__name__ = "OctetString"
_MlrdPeer_Object = MibScalar
mlrdPeer = _MlrdPeer_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 5),
    _MlrdPeer_Type()
)
mlrdPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlrdPeer.setStatus("current")


class _MlrdBackupInterval_Type(Integer32):
    """Custom type mlrdBackupInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 9999),
    )


_MlrdBackupInterval_Type.__name__ = "Integer32"
_MlrdBackupInterval_Object = MibScalar
mlrdBackupInterval = _MlrdBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 6),
    _MlrdBackupInterval_Type()
)
mlrdBackupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlrdBackupInterval.setStatus("current")


class _MlrdStaticActive_Type(Integer32):
    """Custom type mlrdStaticActive based on Integer32"""
    defaultValue = 2

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


_MlrdStaticActive_Type.__name__ = "Integer32"
_MlrdStaticActive_Object = MibScalar
mlrdStaticActive = _MlrdStaticActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 7),
    _MlrdStaticActive_Type()
)
mlrdStaticActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlrdStaticActive.setStatus("current")
_MlrdTable_Object = MibTable
mlrdTable = _MlrdTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 8)
)
if mibBuilder.loadTexts:
    mlrdTable.setStatus("current")
_MlrdTableEntry_Object = MibTableRow
mlrdTableEntry = _MlrdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 8, 1)
)
mlrdTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "mlrdTableIndex"),
)
if mibBuilder.loadTexts:
    mlrdTableEntry.setStatus("current")


class _MlrdTableIndex_Type(Integer32):
    """Custom type mlrdTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MlrdTableIndex_Type.__name__ = "Integer32"
_MlrdTableIndex_Object = MibTableColumn
mlrdTableIndex = _MlrdTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 8, 1, 1),
    _MlrdTableIndex_Type()
)
mlrdTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mlrdTableIndex.setStatus("current")
_MlrdTableMac_Type = MacAddress
_MlrdTableMac_Object = MibTableColumn
mlrdTableMac = _MlrdTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 8, 1, 2),
    _MlrdTableMac_Type()
)
mlrdTableMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mlrdTableMac.setStatus("current")
_MlrdTableIp_Type = IpAddress
_MlrdTableIp_Object = MibTableColumn
mlrdTableIp = _MlrdTableIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 8, 1, 3),
    _MlrdTableIp_Type()
)
mlrdTableIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mlrdTableIp.setStatus("current")
_MlrdTableParent_Type = IpAddress
_MlrdTableParent_Object = MibTableColumn
mlrdTableParent = _MlrdTableParent_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 8, 1, 4),
    _MlrdTableParent_Type()
)
mlrdTableParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mlrdTableParent.setStatus("current")
_MlrdTableDefaultRoute_Type = IpAddress
_MlrdTableDefaultRoute_Object = MibTableColumn
mlrdTableDefaultRoute = _MlrdTableDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 8, 1, 5),
    _MlrdTableDefaultRoute_Type()
)
mlrdTableDefaultRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mlrdTableDefaultRoute.setStatus("current")


class _MlrdTableComment_Type(DisplayString):
    """Custom type mlrdTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MlrdTableComment_Type.__name__ = "DisplayString"
_MlrdTableComment_Object = MibTableColumn
mlrdTableComment = _MlrdTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 8, 1, 6),
    _MlrdTableComment_Type()
)
mlrdTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mlrdTableComment.setStatus("current")


class _MlrdTableActive_Type(Integer32):
    """Custom type mlrdTableActive based on Integer32"""
    defaultValue = 1

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


_MlrdTableActive_Type.__name__ = "Integer32"
_MlrdTableActive_Object = MibTableColumn
mlrdTableActive = _MlrdTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 8, 1, 7),
    _MlrdTableActive_Type()
)
mlrdTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mlrdTableActive.setStatus("current")
_MlrdTableRowStatus_Type = RowStatus
_MlrdTableRowStatus_Object = MibTableColumn
mlrdTableRowStatus = _MlrdTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 35, 8, 1, 8),
    _MlrdTableRowStatus_Type()
)
mlrdTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mlrdTableRowStatus.setStatus("current")
_NodeConfigurationRoutedog_ObjectIdentity = ObjectIdentity
nodeConfigurationRoutedog = _NodeConfigurationRoutedog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 36)
)


class _RoutedogActive_Type(Integer32):
    """Custom type routedogActive based on Integer32"""
    defaultValue = 1

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


_RoutedogActive_Type.__name__ = "Integer32"
_RoutedogActive_Object = MibScalar
routedogActive = _RoutedogActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 36, 1),
    _RoutedogActive_Type()
)
routedogActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routedogActive.setStatus("current")


class _RoutedogSsid_Type(DisplayString):
    """Custom type routedogSsid based on DisplayString"""
    defaultValue = OctetString("ServiceDown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RoutedogSsid_Type.__name__ = "DisplayString"
_RoutedogSsid_Object = MibScalar
routedogSsid = _RoutedogSsid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 36, 2),
    _RoutedogSsid_Type()
)
routedogSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routedogSsid.setStatus("current")


class _RoutedogInterval_Type(Integer32):
    """Custom type routedogInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_RoutedogInterval_Type.__name__ = "Integer32"
_RoutedogInterval_Object = MibScalar
routedogInterval = _RoutedogInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 36, 3),
    _RoutedogInterval_Type()
)
routedogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routedogInterval.setStatus("current")


class _RoutedogReboot_Type(Integer32):
    """Custom type routedogReboot based on Integer32"""
    defaultValue = 2

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


_RoutedogReboot_Type.__name__ = "Integer32"
_RoutedogReboot_Object = MibScalar
routedogReboot = _RoutedogReboot_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 36, 4),
    _RoutedogReboot_Type()
)
routedogReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routedogReboot.setStatus("current")


class _RoutedogIntervaCount_Type(Integer32):
    """Custom type routedogIntervaCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RoutedogIntervaCount_Type.__name__ = "Integer32"
_RoutedogIntervaCount_Object = MibScalar
routedogIntervaCount = _RoutedogIntervaCount_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 36, 5),
    _RoutedogIntervaCount_Type()
)
routedogIntervaCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routedogIntervaCount.setStatus("current")
_NodeConfigurationLinuxdog_ObjectIdentity = ObjectIdentity
nodeConfigurationLinuxdog = _NodeConfigurationLinuxdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 37)
)


class _LinuxdogActive_Type(Integer32):
    """Custom type linuxdogActive based on Integer32"""
    defaultValue = 1

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


_LinuxdogActive_Type.__name__ = "Integer32"
_LinuxdogActive_Object = MibScalar
linuxdogActive = _LinuxdogActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 37, 1),
    _LinuxdogActive_Type()
)
linuxdogActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linuxdogActive.setStatus("current")


class _LinuxdogInterval_Type(Integer32):
    """Custom type linuxdogInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_LinuxdogInterval_Type.__name__ = "Integer32"
_LinuxdogInterval_Object = MibScalar
linuxdogInterval = _LinuxdogInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 37, 2),
    _LinuxdogInterval_Type()
)
linuxdogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linuxdogInterval.setStatus("current")
_NodeConfigurationAdvTunning_ObjectIdentity = ObjectIdentity
nodeConfigurationAdvTunning = _NodeConfigurationAdvTunning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38)
)


class _AdvTunningConntrackMax_Type(Integer32):
    """Custom type advTunningConntrackMax based on Integer32"""
    defaultValue = 212368

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 212368),
    )


_AdvTunningConntrackMax_Type.__name__ = "Integer32"
_AdvTunningConntrackMax_Object = MibScalar
advTunningConntrackMax = _AdvTunningConntrackMax_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 1),
    _AdvTunningConntrackMax_Type()
)
advTunningConntrackMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackMax.setStatus("current")


class _AdvTunningConntrackGenericTimeout_Type(Integer32):
    """Custom type advTunningConntrackGenericTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1200),
    )


_AdvTunningConntrackGenericTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackGenericTimeout_Object = MibScalar
advTunningConntrackGenericTimeout = _AdvTunningConntrackGenericTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 2),
    _AdvTunningConntrackGenericTimeout_Type()
)
advTunningConntrackGenericTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackGenericTimeout.setStatus("current")


class _AdvTunningConntrackIcmpTimeout_Type(Integer32):
    """Custom type advTunningConntrackIcmpTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_AdvTunningConntrackIcmpTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackIcmpTimeout_Object = MibScalar
advTunningConntrackIcmpTimeout = _AdvTunningConntrackIcmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 3),
    _AdvTunningConntrackIcmpTimeout_Type()
)
advTunningConntrackIcmpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackIcmpTimeout.setStatus("current")


class _AdvTunningConntrackTcpcloseTimeout_Type(Integer32):
    """Custom type advTunningConntrackTcpcloseTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AdvTunningConntrackTcpcloseTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackTcpcloseTimeout_Object = MibScalar
advTunningConntrackTcpcloseTimeout = _AdvTunningConntrackTcpcloseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 4),
    _AdvTunningConntrackTcpcloseTimeout_Type()
)
advTunningConntrackTcpcloseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackTcpcloseTimeout.setStatus("current")


class _AdvTunningConntrackTcpclosewaitTimeout_Type(Integer32):
    """Custom type advTunningConntrackTcpclosewaitTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_AdvTunningConntrackTcpclosewaitTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackTcpclosewaitTimeout_Object = MibScalar
advTunningConntrackTcpclosewaitTimeout = _AdvTunningConntrackTcpclosewaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 5),
    _AdvTunningConntrackTcpclosewaitTimeout_Type()
)
advTunningConntrackTcpclosewaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackTcpclosewaitTimeout.setStatus("current")


class _AdvTunningConntrackTcpestablishTimeout_Type(Integer32):
    """Custom type advTunningConntrackTcpestablishTimeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 864000),
    )


_AdvTunningConntrackTcpestablishTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackTcpestablishTimeout_Object = MibScalar
advTunningConntrackTcpestablishTimeout = _AdvTunningConntrackTcpestablishTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 6),
    _AdvTunningConntrackTcpestablishTimeout_Type()
)
advTunningConntrackTcpestablishTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackTcpestablishTimeout.setStatus("current")


class _AdvTunningConntrackTcpfinwaitTimeout_Type(Integer32):
    """Custom type advTunningConntrackTcpfinwaitTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_AdvTunningConntrackTcpfinwaitTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackTcpfinwaitTimeout_Object = MibScalar
advTunningConntrackTcpfinwaitTimeout = _AdvTunningConntrackTcpfinwaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 7),
    _AdvTunningConntrackTcpfinwaitTimeout_Type()
)
advTunningConntrackTcpfinwaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackTcpfinwaitTimeout.setStatus("current")


class _AdvTunningConntrackTcplastackTimeout_Type(Integer32):
    """Custom type advTunningConntrackTcplastackTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_AdvTunningConntrackTcplastackTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackTcplastackTimeout_Object = MibScalar
advTunningConntrackTcplastackTimeout = _AdvTunningConntrackTcplastackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 8),
    _AdvTunningConntrackTcplastackTimeout_Type()
)
advTunningConntrackTcplastackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackTcplastackTimeout.setStatus("current")


class _AdvTunningConntrackTcpsynrecvTimeout_Type(Integer32):
    """Custom type advTunningConntrackTcpsynrecvTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_AdvTunningConntrackTcpsynrecvTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackTcpsynrecvTimeout_Object = MibScalar
advTunningConntrackTcpsynrecvTimeout = _AdvTunningConntrackTcpsynrecvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 9),
    _AdvTunningConntrackTcpsynrecvTimeout_Type()
)
advTunningConntrackTcpsynrecvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackTcpsynrecvTimeout.setStatus("current")


class _AdvTunningConntrackTcpsynsentTimeout_Type(Integer32):
    """Custom type advTunningConntrackTcpsynsentTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 240),
    )


_AdvTunningConntrackTcpsynsentTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackTcpsynsentTimeout_Object = MibScalar
advTunningConntrackTcpsynsentTimeout = _AdvTunningConntrackTcpsynsentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 10),
    _AdvTunningConntrackTcpsynsentTimeout_Type()
)
advTunningConntrackTcpsynsentTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackTcpsynsentTimeout.setStatus("current")


class _AdvTunningConntrackTcptimewaitTimeout_Type(Integer32):
    """Custom type advTunningConntrackTcptimewaitTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 240),
    )


_AdvTunningConntrackTcptimewaitTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackTcptimewaitTimeout_Object = MibScalar
advTunningConntrackTcptimewaitTimeout = _AdvTunningConntrackTcptimewaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 11),
    _AdvTunningConntrackTcptimewaitTimeout_Type()
)
advTunningConntrackTcptimewaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackTcptimewaitTimeout.setStatus("current")


class _AdvTunningConntrackUdpTimeout_Type(Integer32):
    """Custom type advTunningConntrackUdpTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_AdvTunningConntrackUdpTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackUdpTimeout_Object = MibScalar
advTunningConntrackUdpTimeout = _AdvTunningConntrackUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 12),
    _AdvTunningConntrackUdpTimeout_Type()
)
advTunningConntrackUdpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackUdpTimeout.setStatus("current")


class _AdvTunningConntrackUdpstreamTimeout_Type(Integer32):
    """Custom type advTunningConntrackUdpstreamTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 360),
    )


_AdvTunningConntrackUdpstreamTimeout_Type.__name__ = "Integer32"
_AdvTunningConntrackUdpstreamTimeout_Object = MibScalar
advTunningConntrackUdpstreamTimeout = _AdvTunningConntrackUdpstreamTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 13),
    _AdvTunningConntrackUdpstreamTimeout_Type()
)
advTunningConntrackUdpstreamTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningConntrackUdpstreamTimeout.setStatus("current")


class _AdvTunningWirelessRadio0Distance_Type(Integer32):
    """Custom type advTunningWirelessRadio0Distance based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdvTunningWirelessRadio0Distance_Type.__name__ = "Integer32"
_AdvTunningWirelessRadio0Distance_Object = MibScalar
advTunningWirelessRadio0Distance = _AdvTunningWirelessRadio0Distance_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 14),
    _AdvTunningWirelessRadio0Distance_Type()
)
advTunningWirelessRadio0Distance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningWirelessRadio0Distance.setStatus("current")


class _AdvTunningWirelessRadio1Distance_Type(Integer32):
    """Custom type advTunningWirelessRadio1Distance based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdvTunningWirelessRadio1Distance_Type.__name__ = "Integer32"
_AdvTunningWirelessRadio1Distance_Object = MibScalar
advTunningWirelessRadio1Distance = _AdvTunningWirelessRadio1Distance_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 15),
    _AdvTunningWirelessRadio1Distance_Type()
)
advTunningWirelessRadio1Distance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningWirelessRadio1Distance.setStatus("current")


class _AdvTunningWirelessRadio2Distance_Type(Integer32):
    """Custom type advTunningWirelessRadio2Distance based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdvTunningWirelessRadio2Distance_Type.__name__ = "Integer32"
_AdvTunningWirelessRadio2Distance_Object = MibScalar
advTunningWirelessRadio2Distance = _AdvTunningWirelessRadio2Distance_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 16),
    _AdvTunningWirelessRadio2Distance_Type()
)
advTunningWirelessRadio2Distance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningWirelessRadio2Distance.setStatus("current")


class _AdvTunningWirelessRadio3Distance_Type(Integer32):
    """Custom type advTunningWirelessRadio3Distance based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_AdvTunningWirelessRadio3Distance_Type.__name__ = "Integer32"
_AdvTunningWirelessRadio3Distance_Object = MibScalar
advTunningWirelessRadio3Distance = _AdvTunningWirelessRadio3Distance_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 17),
    _AdvTunningWirelessRadio3Distance_Type()
)
advTunningWirelessRadio3Distance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningWirelessRadio3Distance.setStatus("current")


class _AdvTunningWirelessRegionDomain_Type(Integer32):
    """Custom type advTunningWirelessRegionDomain based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AdvTunningWirelessRegionDomain_Type.__name__ = "Integer32"
_AdvTunningWirelessRegionDomain_Object = MibScalar
advTunningWirelessRegionDomain = _AdvTunningWirelessRegionDomain_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 18),
    _AdvTunningWirelessRegionDomain_Type()
)
advTunningWirelessRegionDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advTunningWirelessRegionDomain.setStatus("current")


class _AdvTunningWirelessCountry_Type(Integer32):
    """Custom type advTunningWirelessCountry based on Integer32"""
    defaultValue = 840

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AdvTunningWirelessCountry_Type.__name__ = "Integer32"
_AdvTunningWirelessCountry_Object = MibScalar
advTunningWirelessCountry = _AdvTunningWirelessCountry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 19),
    _AdvTunningWirelessCountry_Type()
)
advTunningWirelessCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningWirelessCountry.setStatus("current")


class _AdvTunningWirelessOutdoor_Type(Integer32):
    """Custom type advTunningWirelessOutdoor based on Integer32"""
    defaultValue = 1

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


_AdvTunningWirelessOutdoor_Type.__name__ = "Integer32"
_AdvTunningWirelessOutdoor_Object = MibScalar
advTunningWirelessOutdoor = _AdvTunningWirelessOutdoor_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 20),
    _AdvTunningWirelessOutdoor_Type()
)
advTunningWirelessOutdoor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningWirelessOutdoor.setStatus("current")


class _AdvTunningWirelessXChannel_Type(Integer32):
    """Custom type advTunningWirelessXChannel based on Integer32"""
    defaultValue = 2

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


_AdvTunningWirelessXChannel_Type.__name__ = "Integer32"
_AdvTunningWirelessXChannel_Object = MibScalar
advTunningWirelessXChannel = _AdvTunningWirelessXChannel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 38, 21),
    _AdvTunningWirelessXChannel_Type()
)
advTunningWirelessXChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advTunningWirelessXChannel.setStatus("current")
_NodeConfigurationSshd_ObjectIdentity = ObjectIdentity
nodeConfigurationSshd = _NodeConfigurationSshd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 39)
)


class _SshdActive_Type(Integer32):
    """Custom type sshdActive based on Integer32"""
    defaultValue = 1

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


_SshdActive_Type.__name__ = "Integer32"
_SshdActive_Object = MibScalar
sshdActive = _SshdActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 39, 1),
    _SshdActive_Type()
)
sshdActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshdActive.setStatus("current")


class _SshdPort_Type(Integer32):
    """Custom type sshdPort based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SshdPort_Type.__name__ = "Integer32"
_SshdPort_Object = MibScalar
sshdPort = _SshdPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 39, 2),
    _SshdPort_Type()
)
sshdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshdPort.setStatus("current")
_NodeConfigutationWme_ObjectIdentity = ObjectIdentity
nodeConfigutationWme = _NodeConfigutationWme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40)
)
_WmeTable_Object = MibTable
wmeTable = _WmeTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1)
)
if mibBuilder.loadTexts:
    wmeTable.setStatus("current")
_WmeTableEntry_Object = MibTableRow
wmeTableEntry = _WmeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1)
)
wmeTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "wmeTableIndex"),
)
if mibBuilder.loadTexts:
    wmeTableEntry.setStatus("current")


class _WmeTableIndex_Type(Integer32):
    """Custom type wmeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WmeTableIndex_Type.__name__ = "Integer32"
_WmeTableIndex_Object = MibTableColumn
wmeTableIndex = _WmeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 1),
    _WmeTableIndex_Type()
)
wmeTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wmeTableIndex.setStatus("current")


class _WmeTableName_Type(OctetString):
    """Custom type wmeTableName based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WmeTableName_Type.__name__ = "OctetString"
_WmeTableName_Object = MibTableColumn
wmeTableName = _WmeTableName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 2),
    _WmeTableName_Type()
)
wmeTableName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableName.setStatus("current")


class _WmeTableCwminBe_Type(Integer32):
    """Custom type wmeTableCwminBe based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableCwminBe_Type.__name__ = "Integer32"
_WmeTableCwminBe_Object = MibTableColumn
wmeTableCwminBe = _WmeTableCwminBe_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 3),
    _WmeTableCwminBe_Type()
)
wmeTableCwminBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableCwminBe.setStatus("current")


class _WmeTableCwminBk_Type(Integer32):
    """Custom type wmeTableCwminBk based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableCwminBk_Type.__name__ = "Integer32"
_WmeTableCwminBk_Object = MibTableColumn
wmeTableCwminBk = _WmeTableCwminBk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 4),
    _WmeTableCwminBk_Type()
)
wmeTableCwminBk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableCwminBk.setStatus("current")


class _WmeTableCwminVi_Type(Integer32):
    """Custom type wmeTableCwminVi based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableCwminVi_Type.__name__ = "Integer32"
_WmeTableCwminVi_Object = MibTableColumn
wmeTableCwminVi = _WmeTableCwminVi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 5),
    _WmeTableCwminVi_Type()
)
wmeTableCwminVi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableCwminVi.setStatus("current")


class _WmeTableCwminVo_Type(Integer32):
    """Custom type wmeTableCwminVo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableCwminVo_Type.__name__ = "Integer32"
_WmeTableCwminVo_Object = MibTableColumn
wmeTableCwminVo = _WmeTableCwminVo_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 6),
    _WmeTableCwminVo_Type()
)
wmeTableCwminVo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableCwminVo.setStatus("current")


class _WmeTableBssCwminBe_Type(Integer32):
    """Custom type wmeTableBssCwminBe based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssCwminBe_Type.__name__ = "Integer32"
_WmeTableBssCwminBe_Object = MibTableColumn
wmeTableBssCwminBe = _WmeTableBssCwminBe_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 7),
    _WmeTableBssCwminBe_Type()
)
wmeTableBssCwminBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssCwminBe.setStatus("current")


class _WmeTableBssCwminBk_Type(Integer32):
    """Custom type wmeTableBssCwminBk based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssCwminBk_Type.__name__ = "Integer32"
_WmeTableBssCwminBk_Object = MibTableColumn
wmeTableBssCwminBk = _WmeTableBssCwminBk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 8),
    _WmeTableBssCwminBk_Type()
)
wmeTableBssCwminBk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssCwminBk.setStatus("current")


class _WmeTableBssCwminVi_Type(Integer32):
    """Custom type wmeTableBssCwminVi based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssCwminVi_Type.__name__ = "Integer32"
_WmeTableBssCwminVi_Object = MibTableColumn
wmeTableBssCwminVi = _WmeTableBssCwminVi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 9),
    _WmeTableBssCwminVi_Type()
)
wmeTableBssCwminVi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssCwminVi.setStatus("current")


class _WmeTableBssCwminVo_Type(Integer32):
    """Custom type wmeTableBssCwminVo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssCwminVo_Type.__name__ = "Integer32"
_WmeTableBssCwminVo_Object = MibTableColumn
wmeTableBssCwminVo = _WmeTableBssCwminVo_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 10),
    _WmeTableBssCwminVo_Type()
)
wmeTableBssCwminVo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssCwminVo.setStatus("current")


class _WmeTableCwmaxBe_Type(Integer32):
    """Custom type wmeTableCwmaxBe based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableCwmaxBe_Type.__name__ = "Integer32"
_WmeTableCwmaxBe_Object = MibTableColumn
wmeTableCwmaxBe = _WmeTableCwmaxBe_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 11),
    _WmeTableCwmaxBe_Type()
)
wmeTableCwmaxBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableCwmaxBe.setStatus("current")


class _WmeTableCwmaxBk_Type(Integer32):
    """Custom type wmeTableCwmaxBk based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableCwmaxBk_Type.__name__ = "Integer32"
_WmeTableCwmaxBk_Object = MibTableColumn
wmeTableCwmaxBk = _WmeTableCwmaxBk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 12),
    _WmeTableCwmaxBk_Type()
)
wmeTableCwmaxBk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableCwmaxBk.setStatus("current")


class _WmeTableCwmaxVi_Type(Integer32):
    """Custom type wmeTableCwmaxVi based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableCwmaxVi_Type.__name__ = "Integer32"
_WmeTableCwmaxVi_Object = MibTableColumn
wmeTableCwmaxVi = _WmeTableCwmaxVi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 13),
    _WmeTableCwmaxVi_Type()
)
wmeTableCwmaxVi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableCwmaxVi.setStatus("current")


class _WmeTableCwmaxVo_Type(Integer32):
    """Custom type wmeTableCwmaxVo based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableCwmaxVo_Type.__name__ = "Integer32"
_WmeTableCwmaxVo_Object = MibTableColumn
wmeTableCwmaxVo = _WmeTableCwmaxVo_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 14),
    _WmeTableCwmaxVo_Type()
)
wmeTableCwmaxVo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableCwmaxVo.setStatus("current")


class _WmeTableBssCwmaxBe_Type(Integer32):
    """Custom type wmeTableBssCwmaxBe based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssCwmaxBe_Type.__name__ = "Integer32"
_WmeTableBssCwmaxBe_Object = MibTableColumn
wmeTableBssCwmaxBe = _WmeTableBssCwmaxBe_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 15),
    _WmeTableBssCwmaxBe_Type()
)
wmeTableBssCwmaxBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssCwmaxBe.setStatus("current")


class _WmeTableBssCwmaxBk_Type(Integer32):
    """Custom type wmeTableBssCwmaxBk based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssCwmaxBk_Type.__name__ = "Integer32"
_WmeTableBssCwmaxBk_Object = MibTableColumn
wmeTableBssCwmaxBk = _WmeTableBssCwmaxBk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 16),
    _WmeTableBssCwmaxBk_Type()
)
wmeTableBssCwmaxBk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssCwmaxBk.setStatus("current")


class _WmeTableBssCwmaxVi_Type(Integer32):
    """Custom type wmeTableBssCwmaxVi based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssCwmaxVi_Type.__name__ = "Integer32"
_WmeTableBssCwmaxVi_Object = MibTableColumn
wmeTableBssCwmaxVi = _WmeTableBssCwmaxVi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 17),
    _WmeTableBssCwmaxVi_Type()
)
wmeTableBssCwmaxVi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssCwmaxVi.setStatus("current")


class _WmeTableBssCwmaxVo_Type(Integer32):
    """Custom type wmeTableBssCwmaxVo based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssCwmaxVo_Type.__name__ = "Integer32"
_WmeTableBssCwmaxVo_Object = MibTableColumn
wmeTableBssCwmaxVo = _WmeTableBssCwmaxVo_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 18),
    _WmeTableBssCwmaxVo_Type()
)
wmeTableBssCwmaxVo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssCwmaxVo.setStatus("current")


class _WmeTableAifsnBe_Type(Integer32):
    """Custom type wmeTableAifsnBe based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableAifsnBe_Type.__name__ = "Integer32"
_WmeTableAifsnBe_Object = MibTableColumn
wmeTableAifsnBe = _WmeTableAifsnBe_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 19),
    _WmeTableAifsnBe_Type()
)
wmeTableAifsnBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableAifsnBe.setStatus("current")


class _WmeTableAifsnBk_Type(Integer32):
    """Custom type wmeTableAifsnBk based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableAifsnBk_Type.__name__ = "Integer32"
_WmeTableAifsnBk_Object = MibTableColumn
wmeTableAifsnBk = _WmeTableAifsnBk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 20),
    _WmeTableAifsnBk_Type()
)
wmeTableAifsnBk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableAifsnBk.setStatus("current")


class _WmeTableAifsnVi_Type(Integer32):
    """Custom type wmeTableAifsnVi based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableAifsnVi_Type.__name__ = "Integer32"
_WmeTableAifsnVi_Object = MibTableColumn
wmeTableAifsnVi = _WmeTableAifsnVi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 21),
    _WmeTableAifsnVi_Type()
)
wmeTableAifsnVi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableAifsnVi.setStatus("current")


class _WmeTableAifsnVo_Type(Integer32):
    """Custom type wmeTableAifsnVo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableAifsnVo_Type.__name__ = "Integer32"
_WmeTableAifsnVo_Object = MibTableColumn
wmeTableAifsnVo = _WmeTableAifsnVo_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 22),
    _WmeTableAifsnVo_Type()
)
wmeTableAifsnVo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableAifsnVo.setStatus("current")


class _WmeTableBssAifsnBe_Type(Integer32):
    """Custom type wmeTableBssAifsnBe based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssAifsnBe_Type.__name__ = "Integer32"
_WmeTableBssAifsnBe_Object = MibTableColumn
wmeTableBssAifsnBe = _WmeTableBssAifsnBe_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 23),
    _WmeTableBssAifsnBe_Type()
)
wmeTableBssAifsnBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssAifsnBe.setStatus("current")


class _WmeTableBssAifsnBk_Type(Integer32):
    """Custom type wmeTableBssAifsnBk based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssAifsnBk_Type.__name__ = "Integer32"
_WmeTableBssAifsnBk_Object = MibTableColumn
wmeTableBssAifsnBk = _WmeTableBssAifsnBk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 24),
    _WmeTableBssAifsnBk_Type()
)
wmeTableBssAifsnBk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssAifsnBk.setStatus("current")


class _WmeTableBssAifsnVi_Type(Integer32):
    """Custom type wmeTableBssAifsnVi based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssAifsnVi_Type.__name__ = "Integer32"
_WmeTableBssAifsnVi_Object = MibTableColumn
wmeTableBssAifsnVi = _WmeTableBssAifsnVi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 25),
    _WmeTableBssAifsnVi_Type()
)
wmeTableBssAifsnVi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssAifsnVi.setStatus("current")


class _WmeTableBssAifsnVo_Type(Integer32):
    """Custom type wmeTableBssAifsnVo based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WmeTableBssAifsnVo_Type.__name__ = "Integer32"
_WmeTableBssAifsnVo_Object = MibTableColumn
wmeTableBssAifsnVo = _WmeTableBssAifsnVo_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 26),
    _WmeTableBssAifsnVo_Type()
)
wmeTableBssAifsnVo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssAifsnVo.setStatus("current")


class _WmeTableTxoplimitBe_Type(Integer32):
    """Custom type wmeTableTxoplimitBe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmeTableTxoplimitBe_Type.__name__ = "Integer32"
_WmeTableTxoplimitBe_Object = MibTableColumn
wmeTableTxoplimitBe = _WmeTableTxoplimitBe_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 27),
    _WmeTableTxoplimitBe_Type()
)
wmeTableTxoplimitBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableTxoplimitBe.setStatus("current")


class _WmeTableTxoplimitBk_Type(Integer32):
    """Custom type wmeTableTxoplimitBk based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmeTableTxoplimitBk_Type.__name__ = "Integer32"
_WmeTableTxoplimitBk_Object = MibTableColumn
wmeTableTxoplimitBk = _WmeTableTxoplimitBk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 28),
    _WmeTableTxoplimitBk_Type()
)
wmeTableTxoplimitBk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableTxoplimitBk.setStatus("current")


class _WmeTableTxoplimitVi_Type(Integer32):
    """Custom type wmeTableTxoplimitVi based on Integer32"""
    defaultValue = 3008

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmeTableTxoplimitVi_Type.__name__ = "Integer32"
_WmeTableTxoplimitVi_Object = MibTableColumn
wmeTableTxoplimitVi = _WmeTableTxoplimitVi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 29),
    _WmeTableTxoplimitVi_Type()
)
wmeTableTxoplimitVi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableTxoplimitVi.setStatus("current")


class _WmeTableTxoplimitVo_Type(Integer32):
    """Custom type wmeTableTxoplimitVo based on Integer32"""
    defaultValue = 1504

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmeTableTxoplimitVo_Type.__name__ = "Integer32"
_WmeTableTxoplimitVo_Object = MibTableColumn
wmeTableTxoplimitVo = _WmeTableTxoplimitVo_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 30),
    _WmeTableTxoplimitVo_Type()
)
wmeTableTxoplimitVo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableTxoplimitVo.setStatus("current")


class _WmeTableBssTxoplimitBe_Type(Integer32):
    """Custom type wmeTableBssTxoplimitBe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmeTableBssTxoplimitBe_Type.__name__ = "Integer32"
_WmeTableBssTxoplimitBe_Object = MibTableColumn
wmeTableBssTxoplimitBe = _WmeTableBssTxoplimitBe_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 31),
    _WmeTableBssTxoplimitBe_Type()
)
wmeTableBssTxoplimitBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssTxoplimitBe.setStatus("current")


class _WmeTableBssTxoplimitBk_Type(Integer32):
    """Custom type wmeTableBssTxoplimitBk based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmeTableBssTxoplimitBk_Type.__name__ = "Integer32"
_WmeTableBssTxoplimitBk_Object = MibTableColumn
wmeTableBssTxoplimitBk = _WmeTableBssTxoplimitBk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 32),
    _WmeTableBssTxoplimitBk_Type()
)
wmeTableBssTxoplimitBk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssTxoplimitBk.setStatus("current")


class _WmeTableBssTxoplimitVi_Type(Integer32):
    """Custom type wmeTableBssTxoplimitVi based on Integer32"""
    defaultValue = 3008

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmeTableBssTxoplimitVi_Type.__name__ = "Integer32"
_WmeTableBssTxoplimitVi_Object = MibTableColumn
wmeTableBssTxoplimitVi = _WmeTableBssTxoplimitVi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 33),
    _WmeTableBssTxoplimitVi_Type()
)
wmeTableBssTxoplimitVi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssTxoplimitVi.setStatus("current")


class _WmeTableBssTxoplimitVo_Type(Integer32):
    """Custom type wmeTableBssTxoplimitVo based on Integer32"""
    defaultValue = 1504

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WmeTableBssTxoplimitVo_Type.__name__ = "Integer32"
_WmeTableBssTxoplimitVo_Object = MibTableColumn
wmeTableBssTxoplimitVo = _WmeTableBssTxoplimitVo_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 34),
    _WmeTableBssTxoplimitVo_Type()
)
wmeTableBssTxoplimitVo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableBssTxoplimitVo.setStatus("current")


class _WmeTableAcmBe_Type(Integer32):
    """Custom type wmeTableAcmBe based on Integer32"""
    defaultValue = 2

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


_WmeTableAcmBe_Type.__name__ = "Integer32"
_WmeTableAcmBe_Object = MibTableColumn
wmeTableAcmBe = _WmeTableAcmBe_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 35),
    _WmeTableAcmBe_Type()
)
wmeTableAcmBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableAcmBe.setStatus("current")


class _WmeTableAcmBk_Type(Integer32):
    """Custom type wmeTableAcmBk based on Integer32"""
    defaultValue = 2

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


_WmeTableAcmBk_Type.__name__ = "Integer32"
_WmeTableAcmBk_Object = MibTableColumn
wmeTableAcmBk = _WmeTableAcmBk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 36),
    _WmeTableAcmBk_Type()
)
wmeTableAcmBk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableAcmBk.setStatus("current")


class _WmeTableAcmVi_Type(Integer32):
    """Custom type wmeTableAcmVi based on Integer32"""
    defaultValue = 2

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


_WmeTableAcmVi_Type.__name__ = "Integer32"
_WmeTableAcmVi_Object = MibTableColumn
wmeTableAcmVi = _WmeTableAcmVi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 37),
    _WmeTableAcmVi_Type()
)
wmeTableAcmVi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableAcmVi.setStatus("current")


class _WmeTableAcmVo_Type(Integer32):
    """Custom type wmeTableAcmVo based on Integer32"""
    defaultValue = 2

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


_WmeTableAcmVo_Type.__name__ = "Integer32"
_WmeTableAcmVo_Object = MibTableColumn
wmeTableAcmVo = _WmeTableAcmVo_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 38),
    _WmeTableAcmVo_Type()
)
wmeTableAcmVo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableAcmVo.setStatus("current")


class _WmeTableNoackpolicyBe_Type(Integer32):
    """Custom type wmeTableNoackpolicyBe based on Integer32"""
    defaultValue = 2

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


_WmeTableNoackpolicyBe_Type.__name__ = "Integer32"
_WmeTableNoackpolicyBe_Object = MibTableColumn
wmeTableNoackpolicyBe = _WmeTableNoackpolicyBe_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 39),
    _WmeTableNoackpolicyBe_Type()
)
wmeTableNoackpolicyBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableNoackpolicyBe.setStatus("current")


class _WmeTableNoackpolicyBk_Type(Integer32):
    """Custom type wmeTableNoackpolicyBk based on Integer32"""
    defaultValue = 2

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


_WmeTableNoackpolicyBk_Type.__name__ = "Integer32"
_WmeTableNoackpolicyBk_Object = MibTableColumn
wmeTableNoackpolicyBk = _WmeTableNoackpolicyBk_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 40),
    _WmeTableNoackpolicyBk_Type()
)
wmeTableNoackpolicyBk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableNoackpolicyBk.setStatus("current")


class _WmeTableNoackpolicyVi_Type(Integer32):
    """Custom type wmeTableNoackpolicyVi based on Integer32"""
    defaultValue = 2

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


_WmeTableNoackpolicyVi_Type.__name__ = "Integer32"
_WmeTableNoackpolicyVi_Object = MibTableColumn
wmeTableNoackpolicyVi = _WmeTableNoackpolicyVi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 41),
    _WmeTableNoackpolicyVi_Type()
)
wmeTableNoackpolicyVi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableNoackpolicyVi.setStatus("current")


class _WmeTableNoackpolicyVo_Type(Integer32):
    """Custom type wmeTableNoackpolicyVo based on Integer32"""
    defaultValue = 2

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


_WmeTableNoackpolicyVo_Type.__name__ = "Integer32"
_WmeTableNoackpolicyVo_Object = MibTableColumn
wmeTableNoackpolicyVo = _WmeTableNoackpolicyVo_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 42),
    _WmeTableNoackpolicyVo_Type()
)
wmeTableNoackpolicyVo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableNoackpolicyVo.setStatus("current")


class _WmeTableComment_Type(DisplayString):
    """Custom type wmeTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WmeTableComment_Type.__name__ = "DisplayString"
_WmeTableComment_Object = MibTableColumn
wmeTableComment = _WmeTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 43),
    _WmeTableComment_Type()
)
wmeTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableComment.setStatus("current")


class _WmeTableActive_Type(Integer32):
    """Custom type wmeTableActive based on Integer32"""
    defaultValue = 1

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


_WmeTableActive_Type.__name__ = "Integer32"
_WmeTableActive_Object = MibTableColumn
wmeTableActive = _WmeTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 44),
    _WmeTableActive_Type()
)
wmeTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableActive.setStatus("current")
_WmeTableRowStatus_Type = RowStatus
_WmeTableRowStatus_Object = MibTableColumn
wmeTableRowStatus = _WmeTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 40, 1, 1, 45),
    _WmeTableRowStatus_Type()
)
wmeTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wmeTableRowStatus.setStatus("current")
_NodeConfigurationTm75_ObjectIdentity = ObjectIdentity
nodeConfigurationTm75 = _NodeConfigurationTm75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 41)
)


class _Tm75Active_Type(Integer32):
    """Custom type tm75Active based on Integer32"""
    defaultValue = 1

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


_Tm75Active_Type.__name__ = "Integer32"
_Tm75Active_Object = MibScalar
tm75Active = _Tm75Active_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 41, 1),
    _Tm75Active_Type()
)
tm75Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tm75Active.setStatus("current")


class _Tm75Resolution_Type(Integer32):
    """Custom type tm75Resolution based on Integer32"""
    defaultValue = 0

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
        *(("pt0625c", 3),
          ("pt125c", 2),
          ("pt25c", 1),
          ("pt5c", 0))
    )


_Tm75Resolution_Type.__name__ = "Integer32"
_Tm75Resolution_Object = MibScalar
tm75Resolution = _Tm75Resolution_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 41, 2),
    _Tm75Resolution_Type()
)
tm75Resolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tm75Resolution.setStatus("current")


class _Tm75Temperature_Type(OctetString):
    """Custom type tm75Temperature based on OctetString"""
    defaultValue = OctetString("X")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Tm75Temperature_Type.__name__ = "OctetString"
_Tm75Temperature_Object = MibScalar
tm75Temperature = _Tm75Temperature_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 41, 3),
    _Tm75Temperature_Type()
)
tm75Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tm75Temperature.setStatus("current")
_NodeConfigurationNmsAddress_ObjectIdentity = ObjectIdentity
nodeConfigurationNmsAddress = _NodeConfigurationNmsAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 42)
)
_NmsAddressTable_Object = MibTable
nmsAddressTable = _NmsAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 42, 1)
)
if mibBuilder.loadTexts:
    nmsAddressTable.setStatus("current")
_NmsAddressTableEntry_Object = MibTableRow
nmsAddressTableEntry = _NmsAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 42, 1, 1)
)
nmsAddressTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "nmsAddressTableIndex"),
)
if mibBuilder.loadTexts:
    nmsAddressTableEntry.setStatus("current")


class _NmsAddressTableIndex_Type(Integer32):
    """Custom type nmsAddressTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_NmsAddressTableIndex_Type.__name__ = "Integer32"
_NmsAddressTableIndex_Object = MibTableColumn
nmsAddressTableIndex = _NmsAddressTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 42, 1, 1, 1),
    _NmsAddressTableIndex_Type()
)
nmsAddressTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmsAddressTableIndex.setStatus("current")


class _NmsAddressTableAddress_Type(DisplayString):
    """Custom type nmsAddressTableAddress based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NmsAddressTableAddress_Type.__name__ = "DisplayString"
_NmsAddressTableAddress_Object = MibTableColumn
nmsAddressTableAddress = _NmsAddressTableAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 42, 1, 1, 2),
    _NmsAddressTableAddress_Type()
)
nmsAddressTableAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsAddressTableAddress.setStatus("current")


class _NmsAddressTablePort_Type(Integer32):
    """Custom type nmsAddressTablePort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NmsAddressTablePort_Type.__name__ = "Integer32"
_NmsAddressTablePort_Object = MibTableColumn
nmsAddressTablePort = _NmsAddressTablePort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 42, 1, 1, 3),
    _NmsAddressTablePort_Type()
)
nmsAddressTablePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsAddressTablePort.setStatus("current")


class _NmsAddressTableInterval_Type(Integer32):
    """Custom type nmsAddressTableInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300000),
    )


_NmsAddressTableInterval_Type.__name__ = "Integer32"
_NmsAddressTableInterval_Object = MibTableColumn
nmsAddressTableInterval = _NmsAddressTableInterval_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 42, 1, 1, 4),
    _NmsAddressTableInterval_Type()
)
nmsAddressTableInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsAddressTableInterval.setStatus("current")


class _NmsAddressTableComment_Type(DisplayString):
    """Custom type nmsAddressTableComment based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NmsAddressTableComment_Type.__name__ = "DisplayString"
_NmsAddressTableComment_Object = MibTableColumn
nmsAddressTableComment = _NmsAddressTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 42, 1, 1, 5),
    _NmsAddressTableComment_Type()
)
nmsAddressTableComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsAddressTableComment.setStatus("current")


class _NmsAddressTableActive_Type(Integer32):
    """Custom type nmsAddressTableActive based on Integer32"""
    defaultValue = 1

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


_NmsAddressTableActive_Type.__name__ = "Integer32"
_NmsAddressTableActive_Object = MibTableColumn
nmsAddressTableActive = _NmsAddressTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 42, 1, 1, 6),
    _NmsAddressTableActive_Type()
)
nmsAddressTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsAddressTableActive.setStatus("current")
_NmsAddressTableRowStatus_Type = RowStatus
_NmsAddressTableRowStatus_Object = MibTableColumn
nmsAddressTableRowStatus = _NmsAddressTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 42, 1, 1, 7),
    _NmsAddressTableRowStatus_Type()
)
nmsAddressTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsAddressTableRowStatus.setStatus("current")
_NodeConfigurationUserDb_ObjectIdentity = ObjectIdentity
nodeConfigurationUserDb = _NodeConfigurationUserDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43)
)


class _UserDbUsername_Type(DisplayString):
    """Custom type userDbUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserDbUsername_Type.__name__ = "DisplayString"
_UserDbUsername_Object = MibScalar
userDbUsername = _UserDbUsername_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 1),
    _UserDbUsername_Type()
)
userDbUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDbUsername.setStatus("current")


class _UserDbPassword_Type(DisplayString):
    """Custom type userDbPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserDbPassword_Type.__name__ = "DisplayString"
_UserDbPassword_Object = MibScalar
userDbPassword = _UserDbPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 2),
    _UserDbPassword_Type()
)
userDbPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDbPassword.setStatus("current")


class _UserDbGroupid_Type(DisplayString):
    """Custom type userDbGroupid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserDbGroupid_Type.__name__ = "DisplayString"
_UserDbGroupid_Object = MibScalar
userDbGroupid = _UserDbGroupid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 3),
    _UserDbGroupid_Type()
)
userDbGroupid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDbGroupid.setStatus("current")


class _UserDbAddCmd_Type(Integer32):
    """Custom type userDbAddCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UserDbAddCmd_Type.__name__ = "Integer32"
_UserDbAddCmd_Object = MibScalar
userDbAddCmd = _UserDbAddCmd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 4),
    _UserDbAddCmd_Type()
)
userDbAddCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDbAddCmd.setStatus("current")


class _UserDbEditCmd_Type(Integer32):
    """Custom type userDbEditCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UserDbEditCmd_Type.__name__ = "Integer32"
_UserDbEditCmd_Object = MibScalar
userDbEditCmd = _UserDbEditCmd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 5),
    _UserDbEditCmd_Type()
)
userDbEditCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDbEditCmd.setStatus("current")


class _UserDbDelCmd_Type(Integer32):
    """Custom type userDbDelCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_UserDbDelCmd_Type.__name__ = "Integer32"
_UserDbDelCmd_Object = MibScalar
userDbDelCmd = _UserDbDelCmd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 6),
    _UserDbDelCmd_Type()
)
userDbDelCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userDbDelCmd.setStatus("current")
_UserDbTable_Object = MibTable
userDbTable = _UserDbTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 7)
)
if mibBuilder.loadTexts:
    userDbTable.setStatus("current")
_UserDbTableEntry_Object = MibTableRow
userDbTableEntry = _UserDbTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 7, 1)
)
userDbTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "userDbTableIndex"),
)
if mibBuilder.loadTexts:
    userDbTableEntry.setStatus("current")


class _UserDbTableIndex_Type(Integer32):
    """Custom type userDbTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_UserDbTableIndex_Type.__name__ = "Integer32"
_UserDbTableIndex_Object = MibTableColumn
userDbTableIndex = _UserDbTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 7, 1, 1),
    _UserDbTableIndex_Type()
)
userDbTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userDbTableIndex.setStatus("current")


class _UserDbTableName_Type(DisplayString):
    """Custom type userDbTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserDbTableName_Type.__name__ = "DisplayString"
_UserDbTableName_Object = MibTableColumn
userDbTableName = _UserDbTableName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 7, 1, 2),
    _UserDbTableName_Type()
)
userDbTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDbTableName.setStatus("current")


class _UserDbTablePassword_Type(DisplayString):
    """Custom type userDbTablePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserDbTablePassword_Type.__name__ = "DisplayString"
_UserDbTablePassword_Object = MibTableColumn
userDbTablePassword = _UserDbTablePassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 7, 1, 3),
    _UserDbTablePassword_Type()
)
userDbTablePassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDbTablePassword.setStatus("current")


class _UserDbTableGid_Type(Integer32):
    """Custom type userDbTableGid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 999999),
    )


_UserDbTableGid_Type.__name__ = "Integer32"
_UserDbTableGid_Object = MibTableColumn
userDbTableGid = _UserDbTableGid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 7, 1, 4),
    _UserDbTableGid_Type()
)
userDbTableGid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDbTableGid.setStatus("current")


class _UserDbTableStatus_Type(Integer32):
    """Custom type userDbTableStatus based on Integer32"""
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
        *(("enable", 1),
          ("expired", 4),
          ("idle", 3),
          ("loggedin", 2))
    )


_UserDbTableStatus_Type.__name__ = "Integer32"
_UserDbTableStatus_Object = MibTableColumn
userDbTableStatus = _UserDbTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 43, 7, 1, 5),
    _UserDbTableStatus_Type()
)
userDbTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDbTableStatus.setStatus("current")
_NodeConfigurationUserGroup_ObjectIdentity = ObjectIdentity
nodeConfigurationUserGroup = _NodeConfigurationUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44)
)


class _UserGroupId_Type(DisplayString):
    """Custom type userGroupId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupId_Type.__name__ = "DisplayString"
_UserGroupId_Object = MibScalar
userGroupId = _UserGroupId_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 1),
    _UserGroupId_Type()
)
userGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupId.setStatus("current")


class _UserGroupName_Type(DisplayString):
    """Custom type userGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupName_Type.__name__ = "DisplayString"
_UserGroupName_Object = MibScalar
userGroupName = _UserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 2),
    _UserGroupName_Type()
)
userGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupName.setStatus("current")


class _UserGroupLanguage_Type(DisplayString):
    """Custom type userGroupLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupLanguage_Type.__name__ = "DisplayString"
_UserGroupLanguage_Object = MibScalar
userGroupLanguage = _UserGroupLanguage_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 3),
    _UserGroupLanguage_Type()
)
userGroupLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupLanguage.setStatus("current")


class _UserGroupUpload_Type(DisplayString):
    """Custom type userGroupUpload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupUpload_Type.__name__ = "DisplayString"
_UserGroupUpload_Object = MibScalar
userGroupUpload = _UserGroupUpload_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 4),
    _UserGroupUpload_Type()
)
userGroupUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupUpload.setStatus("current")


class _UserGroupDownload_Type(DisplayString):
    """Custom type userGroupDownload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupDownload_Type.__name__ = "DisplayString"
_UserGroupDownload_Object = MibScalar
userGroupDownload = _UserGroupDownload_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 5),
    _UserGroupDownload_Type()
)
userGroupDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupDownload.setStatus("current")


class _UserGroupIdleTimeout_Type(DisplayString):
    """Custom type userGroupIdleTimeout based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupIdleTimeout_Type.__name__ = "DisplayString"
_UserGroupIdleTimeout_Object = MibScalar
userGroupIdleTimeout = _UserGroupIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 6),
    _UserGroupIdleTimeout_Type()
)
userGroupIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupIdleTimeout.setStatus("current")


class _UserGroupSessionTimeout_Type(DisplayString):
    """Custom type userGroupSessionTimeout based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupSessionTimeout_Type.__name__ = "DisplayString"
_UserGroupSessionTimeout_Object = MibScalar
userGroupSessionTimeout = _UserGroupSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 7),
    _UserGroupSessionTimeout_Type()
)
userGroupSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupSessionTimeout.setStatus("current")


class _UserGroupUrl_Type(DisplayString):
    """Custom type userGroupUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_UserGroupUrl_Type.__name__ = "DisplayString"
_UserGroupUrl_Object = MibScalar
userGroupUrl = _UserGroupUrl_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 8),
    _UserGroupUrl_Type()
)
userGroupUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupUrl.setStatus("current")


class _UserGroupComment_Type(DisplayString):
    """Custom type userGroupComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupComment_Type.__name__ = "DisplayString"
_UserGroupComment_Object = MibScalar
userGroupComment = _UserGroupComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 9),
    _UserGroupComment_Type()
)
userGroupComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupComment.setStatus("current")


class _UserGroupAddCmd_Type(Integer32):
    """Custom type userGroupAddCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UserGroupAddCmd_Type.__name__ = "Integer32"
_UserGroupAddCmd_Object = MibScalar
userGroupAddCmd = _UserGroupAddCmd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 10),
    _UserGroupAddCmd_Type()
)
userGroupAddCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupAddCmd.setStatus("current")


class _UserGroupEditCmd_Type(Integer32):
    """Custom type userGroupEditCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UserGroupEditCmd_Type.__name__ = "Integer32"
_UserGroupEditCmd_Object = MibScalar
userGroupEditCmd = _UserGroupEditCmd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 11),
    _UserGroupEditCmd_Type()
)
userGroupEditCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupEditCmd.setStatus("current")


class _UserGroupDelCmd_Type(Integer32):
    """Custom type userGroupDelCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_UserGroupDelCmd_Type.__name__ = "Integer32"
_UserGroupDelCmd_Object = MibScalar
userGroupDelCmd = _UserGroupDelCmd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 12),
    _UserGroupDelCmd_Type()
)
userGroupDelCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userGroupDelCmd.setStatus("current")
_UserGroupTable_Object = MibTable
userGroupTable = _UserGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13)
)
if mibBuilder.loadTexts:
    userGroupTable.setStatus("current")
_UserGroupTableEntry_Object = MibTableRow
userGroupTableEntry = _UserGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1)
)
userGroupTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "userGroupTableIndex"),
)
if mibBuilder.loadTexts:
    userGroupTableEntry.setStatus("current")


class _UserGroupTableIndex_Type(Integer32):
    """Custom type userGroupTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_UserGroupTableIndex_Type.__name__ = "Integer32"
_UserGroupTableIndex_Object = MibTableColumn
userGroupTableIndex = _UserGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1, 1),
    _UserGroupTableIndex_Type()
)
userGroupTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userGroupTableIndex.setStatus("current")


class _UserGroupTableGid_Type(Integer32):
    """Custom type userGroupTableGid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_UserGroupTableGid_Type.__name__ = "Integer32"
_UserGroupTableGid_Object = MibTableColumn
userGroupTableGid = _UserGroupTableGid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1, 2),
    _UserGroupTableGid_Type()
)
userGroupTableGid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGroupTableGid.setStatus("current")


class _UserGroupTableName_Type(DisplayString):
    """Custom type userGroupTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupTableName_Type.__name__ = "DisplayString"
_UserGroupTableName_Object = MibTableColumn
userGroupTableName = _UserGroupTableName_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1, 3),
    _UserGroupTableName_Type()
)
userGroupTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGroupTableName.setStatus("current")


class _UserGroupTableLanguage_Type(DisplayString):
    """Custom type userGroupTableLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupTableLanguage_Type.__name__ = "DisplayString"
_UserGroupTableLanguage_Object = MibTableColumn
userGroupTableLanguage = _UserGroupTableLanguage_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1, 4),
    _UserGroupTableLanguage_Type()
)
userGroupTableLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGroupTableLanguage.setStatus("current")


class _UserGroupTableUpload_Type(Integer32):
    """Custom type userGroupTableUpload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 300000),
    )


_UserGroupTableUpload_Type.__name__ = "Integer32"
_UserGroupTableUpload_Object = MibTableColumn
userGroupTableUpload = _UserGroupTableUpload_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1, 5),
    _UserGroupTableUpload_Type()
)
userGroupTableUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGroupTableUpload.setStatus("current")


class _UserGroupTableDownload_Type(Integer32):
    """Custom type userGroupTableDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 300000),
    )


_UserGroupTableDownload_Type.__name__ = "Integer32"
_UserGroupTableDownload_Object = MibTableColumn
userGroupTableDownload = _UserGroupTableDownload_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1, 6),
    _UserGroupTableDownload_Type()
)
userGroupTableDownload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGroupTableDownload.setStatus("current")


class _UserGroupTableIdleTimeout_Type(Integer32):
    """Custom type userGroupTableIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_UserGroupTableIdleTimeout_Type.__name__ = "Integer32"
_UserGroupTableIdleTimeout_Object = MibTableColumn
userGroupTableIdleTimeout = _UserGroupTableIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1, 7),
    _UserGroupTableIdleTimeout_Type()
)
userGroupTableIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGroupTableIdleTimeout.setStatus("current")


class _UserGroupTableSessTimeout_Type(Integer32):
    """Custom type userGroupTableSessTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_UserGroupTableSessTimeout_Type.__name__ = "Integer32"
_UserGroupTableSessTimeout_Object = MibTableColumn
userGroupTableSessTimeout = _UserGroupTableSessTimeout_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1, 8),
    _UserGroupTableSessTimeout_Type()
)
userGroupTableSessTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGroupTableSessTimeout.setStatus("current")


class _UserGroupTableUrl_Type(DisplayString):
    """Custom type userGroupTableUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_UserGroupTableUrl_Type.__name__ = "DisplayString"
_UserGroupTableUrl_Object = MibTableColumn
userGroupTableUrl = _UserGroupTableUrl_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1, 9),
    _UserGroupTableUrl_Type()
)
userGroupTableUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGroupTableUrl.setStatus("current")


class _UserGroupTableComment_Type(DisplayString):
    """Custom type userGroupTableComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserGroupTableComment_Type.__name__ = "DisplayString"
_UserGroupTableComment_Object = MibTableColumn
userGroupTableComment = _UserGroupTableComment_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 44, 13, 1, 10),
    _UserGroupTableComment_Type()
)
userGroupTableComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userGroupTableComment.setStatus("current")
_NodeConfigurationStatickey_ObjectIdentity = ObjectIdentity
nodeConfigurationStatickey = _NodeConfigurationStatickey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 45)
)


class _StatickeyWifi0Key0_Type(OctetString):
    """Custom type statickeyWifi0Key0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StatickeyWifi0Key0_Type.__name__ = "OctetString"
_StatickeyWifi0Key0_Object = MibScalar
statickeyWifi0Key0 = _StatickeyWifi0Key0_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 45, 1),
    _StatickeyWifi0Key0_Type()
)
statickeyWifi0Key0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statickeyWifi0Key0.setStatus("current")


class _StatickeyWifi0Key1_Type(OctetString):
    """Custom type statickeyWifi0Key1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StatickeyWifi0Key1_Type.__name__ = "OctetString"
_StatickeyWifi0Key1_Object = MibScalar
statickeyWifi0Key1 = _StatickeyWifi0Key1_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 45, 2),
    _StatickeyWifi0Key1_Type()
)
statickeyWifi0Key1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statickeyWifi0Key1.setStatus("current")


class _StatickeyWifi0Key2_Type(OctetString):
    """Custom type statickeyWifi0Key2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StatickeyWifi0Key2_Type.__name__ = "OctetString"
_StatickeyWifi0Key2_Object = MibScalar
statickeyWifi0Key2 = _StatickeyWifi0Key2_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 45, 3),
    _StatickeyWifi0Key2_Type()
)
statickeyWifi0Key2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statickeyWifi0Key2.setStatus("current")


class _StatickeyWifi0Key3_Type(OctetString):
    """Custom type statickeyWifi0Key3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StatickeyWifi0Key3_Type.__name__ = "OctetString"
_StatickeyWifi0Key3_Object = MibScalar
statickeyWifi0Key3 = _StatickeyWifi0Key3_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 45, 4),
    _StatickeyWifi0Key3_Type()
)
statickeyWifi0Key3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statickeyWifi0Key3.setStatus("current")


class _StatickeyWifi1Key0_Type(OctetString):
    """Custom type statickeyWifi1Key0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StatickeyWifi1Key0_Type.__name__ = "OctetString"
_StatickeyWifi1Key0_Object = MibScalar
statickeyWifi1Key0 = _StatickeyWifi1Key0_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 45, 5),
    _StatickeyWifi1Key0_Type()
)
statickeyWifi1Key0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statickeyWifi1Key0.setStatus("current")


class _StatickeyWifi1Key1_Type(OctetString):
    """Custom type statickeyWifi1Key1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StatickeyWifi1Key1_Type.__name__ = "OctetString"
_StatickeyWifi1Key1_Object = MibScalar
statickeyWifi1Key1 = _StatickeyWifi1Key1_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 45, 6),
    _StatickeyWifi1Key1_Type()
)
statickeyWifi1Key1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statickeyWifi1Key1.setStatus("current")


class _StatickeyWifi1Key2_Type(OctetString):
    """Custom type statickeyWifi1Key2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StatickeyWifi1Key2_Type.__name__ = "OctetString"
_StatickeyWifi1Key2_Object = MibScalar
statickeyWifi1Key2 = _StatickeyWifi1Key2_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 45, 7),
    _StatickeyWifi1Key2_Type()
)
statickeyWifi1Key2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statickeyWifi1Key2.setStatus("current")


class _StatickeyWifi1Key3_Type(OctetString):
    """Custom type statickeyWifi1Key3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_StatickeyWifi1Key3_Type.__name__ = "OctetString"
_StatickeyWifi1Key3_Object = MibScalar
statickeyWifi1Key3 = _StatickeyWifi1Key3_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 45, 8),
    _StatickeyWifi1Key3_Type()
)
statickeyWifi1Key3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statickeyWifi1Key3.setStatus("current")
_NodeConfigurationDhcrelay_ObjectIdentity = ObjectIdentity
nodeConfigurationDhcrelay = _NodeConfigurationDhcrelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46)
)


class _DhcrelayActive_Type(Integer32):
    """Custom type dhcrelayActive based on Integer32"""
    defaultValue = 2

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


_DhcrelayActive_Type.__name__ = "Integer32"
_DhcrelayActive_Object = MibScalar
dhcrelayActive = _DhcrelayActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 1),
    _DhcrelayActive_Type()
)
dhcrelayActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcrelayActive.setStatus("current")


class _DhcrelayPort_Type(Integer32):
    """Custom type dhcrelayPort based on Integer32"""
    defaultValue = 67

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DhcrelayPort_Type.__name__ = "Integer32"
_DhcrelayPort_Object = MibScalar
dhcrelayPort = _DhcrelayPort_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 2),
    _DhcrelayPort_Type()
)
dhcrelayPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcrelayPort.setStatus("current")


class _DhcrelayHopcount_Type(Integer32):
    """Custom type dhcrelayHopcount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DhcrelayHopcount_Type.__name__ = "Integer32"
_DhcrelayHopcount_Object = MibScalar
dhcrelayHopcount = _DhcrelayHopcount_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 3),
    _DhcrelayHopcount_Type()
)
dhcrelayHopcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcrelayHopcount.setStatus("current")


class _DhcrelayPktsize_Type(Integer32):
    """Custom type dhcrelayPktsize based on Integer32"""
    defaultValue = 1400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 1400),
    )


_DhcrelayPktsize_Type.__name__ = "Integer32"
_DhcrelayPktsize_Object = MibScalar
dhcrelayPktsize = _DhcrelayPktsize_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 4),
    _DhcrelayPktsize_Type()
)
dhcrelayPktsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcrelayPktsize.setStatus("current")
_DhcrelayTable_Object = MibTable
dhcrelayTable = _DhcrelayTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 5)
)
if mibBuilder.loadTexts:
    dhcrelayTable.setStatus("current")
_DhcrelayTableEntry_Object = MibTableRow
dhcrelayTableEntry = _DhcrelayTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 5, 1)
)
dhcrelayTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "dhcrelayTableIndex"),
)
if mibBuilder.loadTexts:
    dhcrelayTableEntry.setStatus("current")


class _DhcrelayTableIndex_Type(Integer32):
    """Custom type dhcrelayTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_DhcrelayTableIndex_Type.__name__ = "Integer32"
_DhcrelayTableIndex_Object = MibTableColumn
dhcrelayTableIndex = _DhcrelayTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 5, 1, 1),
    _DhcrelayTableIndex_Type()
)
dhcrelayTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcrelayTableIndex.setStatus("current")


class _DhcrelayTableType_Type(Integer32):
    """Custom type dhcrelayTableType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 2),
          ("server", 1))
    )


_DhcrelayTableType_Type.__name__ = "Integer32"
_DhcrelayTableType_Object = MibTableColumn
dhcrelayTableType = _DhcrelayTableType_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 5, 1, 2),
    _DhcrelayTableType_Type()
)
dhcrelayTableType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcrelayTableType.setStatus("current")


class _DhcrelayTableExtra_Type(DisplayString):
    """Custom type dhcrelayTableExtra based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DhcrelayTableExtra_Type.__name__ = "DisplayString"
_DhcrelayTableExtra_Object = MibTableColumn
dhcrelayTableExtra = _DhcrelayTableExtra_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 5, 1, 3),
    _DhcrelayTableExtra_Type()
)
dhcrelayTableExtra.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcrelayTableExtra.setStatus("current")


class _DhcrelayTableComments_Type(DisplayString):
    """Custom type dhcrelayTableComments based on DisplayString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DhcrelayTableComments_Type.__name__ = "DisplayString"
_DhcrelayTableComments_Object = MibTableColumn
dhcrelayTableComments = _DhcrelayTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 5, 1, 4),
    _DhcrelayTableComments_Type()
)
dhcrelayTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcrelayTableComments.setStatus("current")


class _DhcrelayTableActive_Type(Integer32):
    """Custom type dhcrelayTableActive based on Integer32"""
    defaultValue = 1

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


_DhcrelayTableActive_Type.__name__ = "Integer32"
_DhcrelayTableActive_Object = MibTableColumn
dhcrelayTableActive = _DhcrelayTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 5, 1, 5),
    _DhcrelayTableActive_Type()
)
dhcrelayTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcrelayTableActive.setStatus("current")
_DhcrelayTableRowStatus_Type = RowStatus
_DhcrelayTableRowStatus_Object = MibTableColumn
dhcrelayTableRowStatus = _DhcrelayTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 46, 5, 1, 6),
    _DhcrelayTableRowStatus_Type()
)
dhcrelayTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcrelayTableRowStatus.setStatus("current")
_NodeConfigurationMulticast_ObjectIdentity = ObjectIdentity
nodeConfigurationMulticast = _NodeConfigurationMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 47)
)


class _MulticastActive_Type(Integer32):
    """Custom type multicastActive based on Integer32"""
    defaultValue = 1

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


_MulticastActive_Type.__name__ = "Integer32"
_MulticastActive_Object = MibScalar
multicastActive = _MulticastActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 47, 1),
    _MulticastActive_Type()
)
multicastActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastActive.setStatus("current")
_NodeConfigurationOspfd_ObjectIdentity = ObjectIdentity
nodeConfigurationOspfd = _NodeConfigurationOspfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 48)
)


class _OspfdActive_Type(Integer32):
    """Custom type ospfdActive based on Integer32"""
    defaultValue = 2

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


_OspfdActive_Type.__name__ = "Integer32"
_OspfdActive_Object = MibScalar
ospfdActive = _OspfdActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 48, 1),
    _OspfdActive_Type()
)
ospfdActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfdActive.setStatus("current")
_NodeConfigurationEbtables_ObjectIdentity = ObjectIdentity
nodeConfigurationEbtables = _NodeConfigurationEbtables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49)
)


class _EbtablesActive_Type(Integer32):
    """Custom type ebtablesActive based on Integer32"""
    defaultValue = 2

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


_EbtablesActive_Type.__name__ = "Integer32"
_EbtablesActive_Object = MibScalar
ebtablesActive = _EbtablesActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 1),
    _EbtablesActive_Type()
)
ebtablesActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebtablesActive.setStatus("current")
_EbTable_Object = MibTable
ebTable = _EbTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2)
)
if mibBuilder.loadTexts:
    ebTable.setStatus("current")
_EbTableEntry_Object = MibTableRow
ebTableEntry = _EbTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1)
)
ebTableEntry.setIndexNames(
    (0, "ENGENIUS-MESH-MIB", "ebTableIndex"),
)
if mibBuilder.loadTexts:
    ebTableEntry.setStatus("current")


class _EbTableIndex_Type(Integer32):
    """Custom type ebTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_EbTableIndex_Type.__name__ = "Integer32"
_EbTableIndex_Object = MibTableColumn
ebTableIndex = _EbTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 1),
    _EbTableIndex_Type()
)
ebTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ebTableIndex.setStatus("current")


class _EbTableTarget_Type(Integer32):
    """Custom type ebTableTarget based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_EbTableTarget_Type.__name__ = "Integer32"
_EbTableTarget_Object = MibTableColumn
ebTableTarget = _EbTableTarget_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 2),
    _EbTableTarget_Type()
)
ebTableTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableTarget.setStatus("current")


class _EbTableSrcIface_Type(OctetString):
    """Custom type ebTableSrcIface based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EbTableSrcIface_Type.__name__ = "OctetString"
_EbTableSrcIface_Object = MibTableColumn
ebTableSrcIface = _EbTableSrcIface_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 3),
    _EbTableSrcIface_Type()
)
ebTableSrcIface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableSrcIface.setStatus("current")


class _EbTableDstIface_Type(OctetString):
    """Custom type ebTableDstIface based on OctetString"""
    defaultValue = OctetString("Nil")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EbTableDstIface_Type.__name__ = "OctetString"
_EbTableDstIface_Object = MibTableColumn
ebTableDstIface = _EbTableDstIface_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 4),
    _EbTableDstIface_Type()
)
ebTableDstIface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableDstIface.setStatus("current")


class _EbTableMatchMac_Type(Integer32):
    """Custom type ebTableMatchMac based on Integer32"""
    defaultValue = 1

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


_EbTableMatchMac_Type.__name__ = "Integer32"
_EbTableMatchMac_Object = MibTableColumn
ebTableMatchMac = _EbTableMatchMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 5),
    _EbTableMatchMac_Type()
)
ebTableMatchMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableMatchMac.setStatus("current")
_EbTableSrcMac_Type = MacAddress
_EbTableSrcMac_Object = MibTableColumn
ebTableSrcMac = _EbTableSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 6),
    _EbTableSrcMac_Type()
)
ebTableSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableSrcMac.setStatus("current")
_EbTableDstMac_Type = MacAddress
_EbTableDstMac_Object = MibTableColumn
ebTableDstMac = _EbTableDstMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 7),
    _EbTableDstMac_Type()
)
ebTableDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableDstMac.setStatus("current")


class _EbTableProtocol_Type(Integer32):
    """Custom type ebTableProtocol based on Integer32"""
    defaultValue = 1

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
        *(("arp", 2),
          ("e802dot1q", 3),
          ("ipv4", 1),
          ("ppp", 4))
    )


_EbTableProtocol_Type.__name__ = "Integer32"
_EbTableProtocol_Object = MibTableColumn
ebTableProtocol = _EbTableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 8),
    _EbTableProtocol_Type()
)
ebTableProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableProtocol.setStatus("current")
_EbTableSrcIp_Type = IpAddress
_EbTableSrcIp_Object = MibTableColumn
ebTableSrcIp = _EbTableSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 9),
    _EbTableSrcIp_Type()
)
ebTableSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableSrcIp.setStatus("current")
_EbTableSrcMask_Type = IpAddress
_EbTableSrcMask_Object = MibTableColumn
ebTableSrcMask = _EbTableSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 10),
    _EbTableSrcMask_Type()
)
ebTableSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableSrcMask.setStatus("current")
_EbTableDstIp_Type = IpAddress
_EbTableDstIp_Object = MibTableColumn
ebTableDstIp = _EbTableDstIp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 11),
    _EbTableDstIp_Type()
)
ebTableDstIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableDstIp.setStatus("current")
_EbTableDstMask_Type = IpAddress
_EbTableDstMask_Object = MibTableColumn
ebTableDstMask = _EbTableDstMask_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 12),
    _EbTableDstMask_Type()
)
ebTableDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableDstMask.setStatus("current")


class _EbTableIpProt_Type(Integer32):
    """Custom type ebTableIpProt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 6),
          ("udp", 17))
    )


_EbTableIpProt_Type.__name__ = "Integer32"
_EbTableIpProt_Object = MibTableColumn
ebTableIpProt = _EbTableIpProt_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 13),
    _EbTableIpProt_Type()
)
ebTableIpProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableIpProt.setStatus("current")


class _EbTableSrcPortStart_Type(Integer32):
    """Custom type ebTableSrcPortStart based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65536),
    )


_EbTableSrcPortStart_Type.__name__ = "Integer32"
_EbTableSrcPortStart_Object = MibTableColumn
ebTableSrcPortStart = _EbTableSrcPortStart_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 14),
    _EbTableSrcPortStart_Type()
)
ebTableSrcPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableSrcPortStart.setStatus("current")


class _EbTableSrcPortEnd_Type(Integer32):
    """Custom type ebTableSrcPortEnd based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65536),
    )


_EbTableSrcPortEnd_Type.__name__ = "Integer32"
_EbTableSrcPortEnd_Object = MibTableColumn
ebTableSrcPortEnd = _EbTableSrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 15),
    _EbTableSrcPortEnd_Type()
)
ebTableSrcPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableSrcPortEnd.setStatus("current")


class _EbTableDstPortStart_Type(Integer32):
    """Custom type ebTableDstPortStart based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65536),
    )


_EbTableDstPortStart_Type.__name__ = "Integer32"
_EbTableDstPortStart_Object = MibTableColumn
ebTableDstPortStart = _EbTableDstPortStart_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 16),
    _EbTableDstPortStart_Type()
)
ebTableDstPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableDstPortStart.setStatus("current")


class _EbTableDstPortEnd_Type(Integer32):
    """Custom type ebTableDstPortEnd based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65536),
    )


_EbTableDstPortEnd_Type.__name__ = "Integer32"
_EbTableDstPortEnd_Object = MibTableColumn
ebTableDstPortEnd = _EbTableDstPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 17),
    _EbTableDstPortEnd_Type()
)
ebTableDstPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableDstPortEnd.setStatus("current")


class _EbTableVlanid_Type(Integer32):
    """Custom type ebTableVlanid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_EbTableVlanid_Type.__name__ = "Integer32"
_EbTableVlanid_Object = MibTableColumn
ebTableVlanid = _EbTableVlanid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 18),
    _EbTableVlanid_Type()
)
ebTableVlanid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableVlanid.setStatus("current")


class _EbTableComments_Type(DisplayString):
    """Custom type ebTableComments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EbTableComments_Type.__name__ = "DisplayString"
_EbTableComments_Object = MibTableColumn
ebTableComments = _EbTableComments_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 19),
    _EbTableComments_Type()
)
ebTableComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableComments.setStatus("current")


class _EbTableActive_Type(Integer32):
    """Custom type ebTableActive based on Integer32"""
    defaultValue = 1

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


_EbTableActive_Type.__name__ = "Integer32"
_EbTableActive_Object = MibTableColumn
ebTableActive = _EbTableActive_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 20),
    _EbTableActive_Type()
)
ebTableActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableActive.setStatus("current")
_EbTableRowStatus_Type = RowStatus
_EbTableRowStatus_Object = MibTableColumn
ebTableRowStatus = _EbTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 49, 2, 1, 21),
    _EbTableRowStatus_Type()
)
ebTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ebTableRowStatus.setStatus("current")
_NodeCommand_ObjectIdentity = ObjectIdentity
nodeCommand = _NodeCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3)
)
_NodeCommandReboot_ObjectIdentity = ObjectIdentity
nodeCommandReboot = _NodeCommandReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 1)
)


class _RebootTime_Type(Integer32):
    """Custom type rebootTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_RebootTime_Type.__name__ = "Integer32"
_RebootTime_Object = MibScalar
rebootTime = _RebootTime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 1, 1),
    _RebootTime_Type()
)
rebootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootTime.setStatus("current")
_NodeCommandReset_ObjectIdentity = ObjectIdentity
nodeCommandReset = _NodeCommandReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 2)
)


class _ResetToDefault_Type(Integer32):
    """Custom type resetToDefault based on Integer32"""
    defaultValue = 0


_ResetToDefault_Object = MibScalar
resetToDefault = _ResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 2, 1),
    _ResetToDefault_Type()
)
resetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetToDefault.setStatus("current")
_NodeCommandUpload_ObjectIdentity = ObjectIdentity
nodeCommandUpload = _NodeCommandUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 3)
)
_UploadDownloadFilename_Type = DisplayString
_UploadDownloadFilename_Object = MibScalar
uploadDownloadFilename = _UploadDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 3, 1),
    _UploadDownloadFilename_Type()
)
uploadDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadDownloadFilename.setStatus("current")


class _UploadDownloadFiletype_Type(Integer32):
    """Custom type uploadDownloadFiletype based on Integer32"""
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
        *(("config", 1),
          ("firmware", 2),
          ("iprsa", 5),
          ("ipx509local", 3),
          ("ipx509remote", 4))
    )


_UploadDownloadFiletype_Type.__name__ = "Integer32"
_UploadDownloadFiletype_Object = MibScalar
uploadDownloadFiletype = _UploadDownloadFiletype_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 3, 2),
    _UploadDownloadFiletype_Type()
)
uploadDownloadFiletype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadDownloadFiletype.setStatus("current")
_UploadDownloadIpaddress_Type = IpAddress
_UploadDownloadIpaddress_Object = MibScalar
uploadDownloadIpaddress = _UploadDownloadIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 3, 3),
    _UploadDownloadIpaddress_Type()
)
uploadDownloadIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadDownloadIpaddress.setStatus("current")


class _UploadDownloadPassword_Type(DisplayString):
    """Custom type uploadDownloadPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UploadDownloadPassword_Type.__name__ = "DisplayString"
_UploadDownloadPassword_Object = MibScalar
uploadDownloadPassword = _UploadDownloadPassword_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 3, 4),
    _UploadDownloadPassword_Type()
)
uploadDownloadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadDownloadPassword.setStatus("current")


class _UploadDownloadOperationtype_Type(Integer32):
    """Custom type uploadDownloadOperationtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2),
          ("uploadandreboot", 3))
    )


_UploadDownloadOperationtype_Type.__name__ = "Integer32"
_UploadDownloadOperationtype_Object = MibScalar
uploadDownloadOperationtype = _UploadDownloadOperationtype_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 3, 5),
    _UploadDownloadOperationtype_Type()
)
uploadDownloadOperationtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadDownloadOperationtype.setStatus("current")


class _UploadDownloadExecutetftp_Type(Integer32):
    """Custom type uploadDownloadExecutetftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_UploadDownloadExecutetftp_Type.__name__ = "Integer32"
_UploadDownloadExecutetftp_Object = MibScalar
uploadDownloadExecutetftp = _UploadDownloadExecutetftp_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 3, 6),
    _UploadDownloadExecutetftp_Type()
)
uploadDownloadExecutetftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadDownloadExecutetftp.setStatus("current")
_NodeCommandLogoutBlock_ObjectIdentity = ObjectIdentity
nodeCommandLogoutBlock = _NodeCommandLogoutBlock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 4)
)
_LogoutAndBlockAction_Type = IpAddress
_LogoutAndBlockAction_Object = MibScalar
logoutAndBlockAction = _LogoutAndBlockAction_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 4, 1),
    _LogoutAndBlockAction_Type()
)
logoutAndBlockAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logoutAndBlockAction.setStatus("current")
_NodeCommandRestartSnmp_ObjectIdentity = ObjectIdentity
nodeCommandRestartSnmp = _NodeCommandRestartSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 5)
)
_RestartSnmpService_Type = Integer32
_RestartSnmpService_Object = MibScalar
restartSnmpService = _RestartSnmpService_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 3, 5, 1),
    _RestartSnmpService_Type()
)
restartSnmpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartSnmpService.setStatus("current")

# Managed Objects groups


# Notification objects

adminTrapsAdminConf = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 2, 1)
)
adminTrapsAdminConf.setObjects(
      *(("ENGENIUS-MESH-MIB", "genericTrapVarHostIPAddress"),
        ("ENGENIUS-MESH-MIB", "genericTrapVariable"))
)
if mibBuilder.loadTexts:
    adminTrapsAdminConf.setStatus(
        "current"
    )

adminTrapsAdminCmd = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 2, 2)
)
adminTrapsAdminCmd.setObjects(
      *(("ENGENIUS-MESH-MIB", "genericTrapVarHostIPAddress"),
        ("ENGENIUS-MESH-MIB", "genericTrapVariable"))
)
if mibBuilder.loadTexts:
    adminTrapsAdminCmd.setStatus(
        "current"
    )

userTrapsUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 3, 1)
)
userTrapsUserLogin.setObjects(
      *(("ENGENIUS-MESH-MIB", "genericTrapVarHostIPAddress"),
        ("ENGENIUS-MESH-MIB", "genericTrapVariable"))
)
if mibBuilder.loadTexts:
    userTrapsUserLogin.setStatus(
        "current"
    )

userTrapsUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 3, 2)
)
userTrapsUserLogout.setObjects(
      *(("ENGENIUS-MESH-MIB", "genericTrapVarHostIPAddress"),
        ("ENGENIUS-MESH-MIB", "genericTrapVariable"))
)
if mibBuilder.loadTexts:
    userTrapsUserLogout.setStatus(
        "current"
    )

systemTrapsSystemReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 4, 1)
)
systemTrapsSystemReboot.setObjects(
      *(("ENGENIUS-MESH-MIB", "genericTrapVarHostIPAddress"),
        ("ENGENIUS-MESH-MIB", "genericTrapVariable"))
)
if mibBuilder.loadTexts:
    systemTrapsSystemReboot.setStatus(
        "current"
    )

systemTrapsSystemRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 4, 2)
)
systemTrapsSystemRestore.setObjects(
      *(("ENGENIUS-MESH-MIB", "genericTrapVarHostIPAddress"),
        ("ENGENIUS-MESH-MIB", "genericTrapVariable"))
)
if mibBuilder.loadTexts:
    systemTrapsSystemRestore.setStatus(
        "current"
    )

systemTrapsSystemUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 4, 3)
)
systemTrapsSystemUpgrade.setObjects(
      *(("ENGENIUS-MESH-MIB", "genericTrapVarHostIPAddress"),
        ("ENGENIUS-MESH-MIB", "genericTrapVariable"))
)
if mibBuilder.loadTexts:
    systemTrapsSystemUpgrade.setStatus(
        "current"
    )

systemTrapsSystemConf = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 4, 4)
)
systemTrapsSystemConf.setObjects(
      *(("ENGENIUS-MESH-MIB", "genericTrapVarHostIPAddress"),
        ("ENGENIUS-MESH-MIB", "genericTrapVariable"))
)
if mibBuilder.loadTexts:
    systemTrapsSystemConf.setStatus(
        "current"
    )

systemTrapsSystemStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 14125, 1, 1, 2, 4, 5)
)
systemTrapsSystemStatus.setObjects(
      *(("ENGENIUS-MESH-MIB", "genericTrapVarHostIPAddress"),
        ("ENGENIUS-MESH-MIB", "genericTrapVariable"))
)
if mibBuilder.loadTexts:
    systemTrapsSystemStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENGENIUS-MESH-MIB",
    **{"engenius": engenius,
       "engeniusmesh": engeniusmesh,
       "nodeStatus": nodeStatus,
       "nodeStatusSystem": nodeStatusSystem,
       "systemUptime": systemUptime,
       "systemMemory": systemMemory,
       "systemDevicename": systemDevicename,
       "systemCheckingState": systemCheckingState,
       "nodeStatusTrap": nodeStatusTrap,
       "trapVariable": trapVariable,
       "genericTrapVariable": genericTrapVariable,
       "genericTrapVarMACAddress": genericTrapVarMACAddress,
       "genericTrapVarHostIPAddress": genericTrapVarHostIPAddress,
       "genericTrapVarHostname": genericTrapVarHostname,
       "genericTrapVarInterface": genericTrapVarInterface,
       "genericTrapVarWirelessCard": genericTrapVarWirelessCard,
       "genericTrapVarEthernetPort": genericTrapVarEthernetPort,
       "genericTrapVarCount": genericTrapVarCount,
       "adminTraps": adminTraps,
       "adminTrapsAdminConf": adminTrapsAdminConf,
       "adminTrapsAdminCmd": adminTrapsAdminCmd,
       "userTraps": userTraps,
       "userTrapsUserLogin": userTrapsUserLogin,
       "userTrapsUserLogout": userTrapsUserLogout,
       "systemTraps": systemTraps,
       "systemTrapsSystemReboot": systemTrapsSystemReboot,
       "systemTrapsSystemRestore": systemTrapsSystemRestore,
       "systemTrapsSystemUpgrade": systemTrapsSystemUpgrade,
       "systemTrapsSystemConf": systemTrapsSystemConf,
       "systemTrapsSystemStatus": systemTrapsSystemStatus,
       "nodeConfiguration": nodeConfiguration,
       "nodeConfigurationSystem": nodeConfigurationSystem,
       "systemName": systemName,
       "systemLocation": systemLocation,
       "systemContactName": systemContactName,
       "systemContactMail": systemContactMail,
       "systemContactPhone": systemContactPhone,
       "systemDescription": systemDescription,
       "systemObjectid": systemObjectid,
       "systemOperatemode": systemOperatemode,
       "systemUpdateMode": systemUpdateMode,
       "nodeConfigurationEthernet": nodeConfigurationEthernet,
       "ethernetInterfaceTable": ethernetInterfaceTable,
       "ethernetInterfaceTableEntry": ethernetInterfaceTableEntry,
       "ethInterfaceTableIndex": ethInterfaceTableIndex,
       "ethInterfaceTableName": ethInterfaceTableName,
       "ethInterfaceTableBase": ethInterfaceTableBase,
       "ethInterfaceTableMac": ethInterfaceTableMac,
       "ethInterfaceTableBridge": ethInterfaceTableBridge,
       "ethInterfaceTableBridgeCost": ethInterfaceTableBridgeCost,
       "ethInterfaceTableBridgePrio": ethInterfaceTableBridgePrio,
       "ethInterfaceTableComments": ethInterfaceTableComments,
       "ethInterfaceTableActive": ethInterfaceTableActive,
       "ethInterfaceTableRowStatus": ethInterfaceTableRowStatus,
       "nodeConfigurationWireless": nodeConfigurationWireless,
       "wirelessInterfaceTable": wirelessInterfaceTable,
       "wirelessInterfaceTableEntry": wirelessInterfaceTableEntry,
       "wlanInterfaceTableIndex": wlanInterfaceTableIndex,
       "wlanInterfaceTableName": wlanInterfaceTableName,
       "wlanInterfaceTableBase": wlanInterfaceTableBase,
       "wlanInterfaceTableBridge": wlanInterfaceTableBridge,
       "wlanInterfaceTableBridgeCost": wlanInterfaceTableBridgeCost,
       "wlanInterfaceTableBridgePrio": wlanInterfaceTableBridgePrio,
       "wlanInterfaceTableMode": wlanInterfaceTableMode,
       "wlanInterfaceTableBand": wlanInterfaceTableBand,
       "wlanInterfaceTableEssid": wlanInterfaceTableEssid,
       "wlanInterfaceTableFreq": wlanInterfaceTableFreq,
       "wlanInterfaceTableMac": wlanInterfaceTableMac,
       "wlanInterfaceTableSecurity": wlanInterfaceTableSecurity,
       "wlanInterfaceTableWpaType": wlanInterfaceTableWpaType,
       "wlanInterfaceTableDot1x": wlanInterfaceTableDot1x,
       "wlanInterfaceTableEncryptionKey": wlanInterfaceTableEncryptionKey,
       "wlanInterfaceTableBroadcastSsid": wlanInterfaceTableBroadcastSsid,
       "wlanInterfaceTableBeaconInt": wlanInterfaceTableBeaconInt,
       "wlanInterfaceTableRtsThreshold": wlanInterfaceTableRtsThreshold,
       "wlanInterfaceTableFragThreshold": wlanInterfaceTableFragThreshold,
       "wlanInterfaceTableDtimInterval": wlanInterfaceTableDtimInterval,
       "wlanInterfaceTableDatarate": wlanInterfaceTableDatarate,
       "wlanInterfaceTableDiversity": wlanInterfaceTableDiversity,
       "wlanInterfaceTableTxAntenna": wlanInterfaceTableTxAntenna,
       "wlanInterfaceTableRxAntenna": wlanInterfaceTableRxAntenna,
       "wlanInterfaceTableCrntTxPower": wlanInterfaceTableCrntTxPower,
       "wlanInterfaceTableTxPower": wlanInterfaceTableTxPower,
       "wlanInterfaceTableSeperation": wlanInterfaceTableSeperation,
       "wlanInterfaceTableComments": wlanInterfaceTableComments,
       "wlanInterfaceTableActive": wlanInterfaceTableActive,
       "wlanInterfaceTableRowStatus": wlanInterfaceTableRowStatus,
       "wirelessFrequencyMeshTable": wirelessFrequencyMeshTable,
       "wirelessFrequencyMeshTableEntry": wirelessFrequencyMeshTableEntry,
       "wlanFrequencyMeshTableIndex": wlanFrequencyMeshTableIndex,
       "wlanFrequencyMeshTableChannel": wlanFrequencyMeshTableChannel,
       "wlanFrequencyMeshTableFrequency": wlanFrequencyMeshTableFrequency,
       "wlanFrequencyMeshTableRowStatus": wlanFrequencyMeshTableRowStatus,
       "wirelessFrequencyAp0Table": wirelessFrequencyAp0Table,
       "wirelessFrequencyAp0TableEntry": wirelessFrequencyAp0TableEntry,
       "wlanFrequencyAp0TableIndex": wlanFrequencyAp0TableIndex,
       "wlanFrequencyAp0TableChannel": wlanFrequencyAp0TableChannel,
       "wlanFrequencyAp0TableFrequency": wlanFrequencyAp0TableFrequency,
       "wlanFrequencyAp0TableRowStatus": wlanFrequencyAp0TableRowStatus,
       "wirelessFrequencyAp1Table": wirelessFrequencyAp1Table,
       "wirelessFrequencyAp1TableEntry": wirelessFrequencyAp1TableEntry,
       "wlanFrequencyAp1TableIndex": wlanFrequencyAp1TableIndex,
       "wlanFrequencyAp1TableChannel": wlanFrequencyAp1TableChannel,
       "wlanFrequencyAp1TableFrequency": wlanFrequencyAp1TableFrequency,
       "wlanFrequencyAp1TableRowStatus": wlanFrequencyAp1TableRowStatus,
       "nodeConfigurationVlan": nodeConfigurationVlan,
       "vlanInterfaceTable": vlanInterfaceTable,
       "vlanInterfaceTableEntry": vlanInterfaceTableEntry,
       "vlanInterfaceTableIndex": vlanInterfaceTableIndex,
       "vlanInterfaceTableName": vlanInterfaceTableName,
       "vlanInterfaceTableBase": vlanInterfaceTableBase,
       "vlanInterfaceTableMac": vlanInterfaceTableMac,
       "vlanInterfaceTableId": vlanInterfaceTableId,
       "vlanInterfaceTableBridge": vlanInterfaceTableBridge,
       "vlanInterfaceTableBridgeCost": vlanInterfaceTableBridgeCost,
       "vlanInterfaceTableBridgePrio": vlanInterfaceTableBridgePrio,
       "vlanInterfaceTableComments": vlanInterfaceTableComments,
       "vlanInterfaceTableActive": vlanInterfaceTableActive,
       "vlanInterfaceTableRowStatus": vlanInterfaceTableRowStatus,
       "nodeConfigurationBridge": nodeConfigurationBridge,
       "bridgeInterfaceTable": bridgeInterfaceTable,
       "bridgeInterfaceTableEntry": bridgeInterfaceTableEntry,
       "bridgeInterfaceTableIndex": bridgeInterfaceTableIndex,
       "bridgeInterfaceTableName": bridgeInterfaceTableName,
       "bridgeInterfaceTableMac": bridgeInterfaceTableMac,
       "bridgeInterfaceTableAge": bridgeInterfaceTableAge,
       "bridgeInterfaceTablePrio": bridgeInterfaceTablePrio,
       "bridgeInterfaceTableFwdDelay": bridgeInterfaceTableFwdDelay,
       "bridgeInterfaceTableHelloInt": bridgeInterfaceTableHelloInt,
       "bridgeInterfaceTableMaxAge": bridgeInterfaceTableMaxAge,
       "bridgeInterfaceTableStp": bridgeInterfaceTableStp,
       "bridgeInterfaceTableComments": bridgeInterfaceTableComments,
       "bridgeInterfaceTableActive": bridgeInterfaceTableActive,
       "bridgeInterfaceTableRowStatus": bridgeInterfaceTableRowStatus,
       "nodeConfigurationIpaddress": nodeConfigurationIpaddress,
       "ipAddressesTable": ipAddressesTable,
       "ipAddressesTableEntry": ipAddressesTableEntry,
       "ipAddressesTableIndex": ipAddressesTableIndex,
       "ipAddressesTableIface": ipAddressesTableIface,
       "ipAddressesTableType": ipAddressesTableType,
       "ipAddressesTableIp": ipAddressesTableIp,
       "ipAddressesTableNetmask": ipAddressesTableNetmask,
       "ipAddressesTableBroadcast": ipAddressesTableBroadcast,
       "ipAddressesTableGateway": ipAddressesTableGateway,
       "ipAddressesTableRouted": ipAddressesTableRouted,
       "ipAddressesTableComments": ipAddressesTableComments,
       "ipAddressesTableActive": ipAddressesTableActive,
       "ipAddressesTableRowStatus": ipAddressesTableRowStatus,
       "nodeConfigurationNetwork": nodeConfigurationNetwork,
       "networkPrimaryDns": networkPrimaryDns,
       "networkSecondaryDns": networkSecondaryDns,
       "networkDomain": networkDomain,
       "nodeConfigurationSyslog": nodeConfigurationSyslog,
       "syslogActive": syslogActive,
       "syslogKlog": syslogKlog,
       "syslogLevel": syslogLevel,
       "syslogRemoteActive": syslogRemoteActive,
       "syslogRemoteAddress": syslogRemoteAddress,
       "nodeConfigurationOlsr": nodeConfigurationOlsr,
       "olsrActive": olsrActive,
       "olsrTosValue": olsrTosValue,
       "olsrWillingnessActive": olsrWillingnessActive,
       "olsrWillingness": olsrWillingness,
       "olsrHysteresisActive": olsrHysteresisActive,
       "olsrHysteresisScaling": olsrHysteresisScaling,
       "olsrHysteresisThrHigh": olsrHysteresisThrHigh,
       "olsrHysteresisThrLow": olsrHysteresisThrLow,
       "olsrLinkQualityType": olsrLinkQualityType,
       "olsrLinkQualitySize": olsrLinkQualitySize,
       "olsrPollRate": olsrPollRate,
       "olsrTcType": olsrTcType,
       "olsrMpr": olsrMpr,
       "olsrSharedKey": olsrSharedKey,
       "olsrInterfaceTable": olsrInterfaceTable,
       "olsrInterfaceTableEntry": olsrInterfaceTableEntry,
       "olsrInterfaceTableIndex": olsrInterfaceTableIndex,
       "olsrInterfaceTableIface": olsrInterfaceTableIface,
       "olsrInterfaceTableHelloInterval": olsrInterfaceTableHelloInterval,
       "olsrInterfaceTableHelloValidity": olsrInterfaceTableHelloValidity,
       "olsrInterfaceTableTcInterval": olsrInterfaceTableTcInterval,
       "olsrInterfaceTableTcValidity": olsrInterfaceTableTcValidity,
       "olsrInterfaceTableMidInterval": olsrInterfaceTableMidInterval,
       "olsrInterfaceTableMidValidity": olsrInterfaceTableMidValidity,
       "olsrInterfaceTableHnaInterval": olsrInterfaceTableHnaInterval,
       "olsrInterfaceTableHnaValidity": olsrInterfaceTableHnaValidity,
       "olsrInterfaceTableComments": olsrInterfaceTableComments,
       "olsrInterfaceTableActive": olsrInterfaceTableActive,
       "olsrInterfaceTableRowStatus": olsrInterfaceTableRowStatus,
       "nodeConfigurationRoute": nodeConfigurationRoute,
       "routeTable": routeTable,
       "routeTableEntry": routeTableEntry,
       "routeTableIndex": routeTableIndex,
       "routeTableSubnet": routeTableSubnet,
       "routeTableNetmask": routeTableNetmask,
       "routeTableGateway": routeTableGateway,
       "routeTableDevice": routeTableDevice,
       "routeTableDirect": routeTableDirect,
       "routeTableComments": routeTableComments,
       "routeTableActive": routeTableActive,
       "routeTableRowStatus": routeTableRowStatus,
       "nodeConfigurationNtp": nodeConfigurationNtp,
       "ntpActive": ntpActive,
       "ntpTimezone": ntpTimezone,
       "ntpTable": ntpTable,
       "ntpTableEntry": ntpTableEntry,
       "ntpTableIndex": ntpTableIndex,
       "ntpTableServer": ntpTableServer,
       "ntpTableMinPoll": ntpTableMinPoll,
       "ntpTableMaxPoll": ntpTableMaxPoll,
       "ntpTableComments": ntpTableComments,
       "ntpTableActive": ntpTableActive,
       "ntpTableRowStatus": ntpTableRowStatus,
       "nodeConfigurationDhcpd": nodeConfigurationDhcpd,
       "dhcpdTable": dhcpdTable,
       "dhcpdTableEntry": dhcpdTableEntry,
       "dhcpdTableIndex": dhcpdTableIndex,
       "dhcpdTableIface": dhcpdTableIface,
       "dhcpdTableSubnet": dhcpdTableSubnet,
       "dhcpdTableNetstart": dhcpdTableNetstart,
       "dhcpdTableNetend": dhcpdTableNetend,
       "dhcpdTableNetmask": dhcpdTableNetmask,
       "dhcpdTableMaxLease": dhcpdTableMaxLease,
       "dhcpdTableLease": dhcpdTableLease,
       "dhcpdTableDomain": dhcpdTableDomain,
       "dhcpdTableDns": dhcpdTableDns,
       "dhcpdTableRouter": dhcpdTableRouter,
       "dhcpdTableComments": dhcpdTableComments,
       "dhcpdTableActive": dhcpdTableActive,
       "dhcpdTableRowStatus": dhcpdTableRowStatus,
       "dhcpdActive": dhcpdActive,
       "dhcpClientExecute": dhcpClientExecute,
       "dhcpClientTable": dhcpClientTable,
       "dhcpClientTableEntry": dhcpClientTableEntry,
       "dhcpClientTableIndex": dhcpClientTableIndex,
       "dhcpClientTableIp": dhcpClientTableIp,
       "dhcpClientTableMac": dhcpClientTableMac,
       "dhcpClientTableHostname": dhcpClientTableHostname,
       "nodeConfigurationDns": nodeConfigurationDns,
       "dnsActive": dnsActive,
       "dnsDomainNeeded": dnsDomainNeeded,
       "dnsBogusPriv": dnsBogusPriv,
       "dnsFilterWin2k": dnsFilterWin2k,
       "dnsStrictOrder": dnsStrictOrder,
       "dnsTable": dnsTable,
       "dnsTableEntry": dnsTableEntry,
       "dnsTableIndex": dnsTableIndex,
       "dnsTableDns": dnsTableDns,
       "dnsTableIpaddress": dnsTableIpaddress,
       "dnsTableComments": dnsTableComments,
       "dnsTableActive": dnsTableActive,
       "dnsTableRowStatus": dnsTableRowStatus,
       "nodeConfigurationTopology": nodeConfigurationTopology,
       "topologyTable": topologyTable,
       "topologyTableEntry": topologyTableEntry,
       "topologyTableIndex": topologyTableIndex,
       "topologyTableSource": topologyTableSource,
       "topologyTableDestination": topologyTableDestination,
       "topologyTableLabel": topologyTableLabel,
       "topologyTableStyle": topologyTableStyle,
       "nodeConfigurationFirewall": nodeConfigurationFirewall,
       "firewallActive": firewallActive,
       "firewallTable": firewallTable,
       "firewallTableEntry": firewallTableEntry,
       "firewallTableIndex": firewallTableIndex,
       "firewallTableTarget": firewallTableTarget,
       "firewallTableSrcIface": firewallTableSrcIface,
       "firewallTableDstIface": firewallTableDstIface,
       "firewallTableSrcIp": firewallTableSrcIp,
       "firewallTableSrcMask": firewallTableSrcMask,
       "firewallTableDstIp": firewallTableDstIp,
       "firewallTableDstMask": firewallTableDstMask,
       "firewallTableProtocol": firewallTableProtocol,
       "firewallTableStartPort": firewallTableStartPort,
       "firewallTableEndPort": firewallTableEndPort,
       "firewallTableUserGroup": firewallTableUserGroup,
       "firewallTableComment": firewallTableComment,
       "firewallTableActive": firewallTableActive,
       "firewallTableRowStatus": firewallTableRowStatus,
       "nodeConfigurationMacaccess": nodeConfigurationMacaccess,
       "macaccessActive": macaccessActive,
       "macaccessType": macaccessType,
       "macActiveListExecute": macActiveListExecute,
       "macaccessTable": macaccessTable,
       "macaccessTableEntry": macaccessTableEntry,
       "macaccessTableIndex": macaccessTableIndex,
       "macaccessTableMac": macaccessTableMac,
       "macaccessTableType": macaccessTableType,
       "macaccessTableComment": macaccessTableComment,
       "macaccessTableActive": macaccessTableActive,
       "macaccessTableRowStatus": macaccessTableRowStatus,
       "macActiveTable": macActiveTable,
       "macActiveTableEntry": macActiveTableEntry,
       "macActiveTableIndex": macActiveTableIndex,
       "macActiveTableMac": macActiveTableMac,
       "macActiveTableIp": macActiveTableIp,
       "nodeConfigurationNat": nodeConfigurationNat,
       "natActive": natActive,
       "natTable": natTable,
       "natTableEntry": natTableEntry,
       "natTableIndex": natTableIndex,
       "natTableProtocol": natTableProtocol,
       "natTablePort": natTablePort,
       "natTableIp": natTableIp,
       "natTableComment": natTableComment,
       "natTableActive": natTableActive,
       "natTableRowStatus": natTableRowStatus,
       "nodeConfigurationOlsrGW": nodeConfigurationOlsrGW,
       "olsrGatewayTable": olsrGatewayTable,
       "olsrGatewayTableEntry": olsrGatewayTableEntry,
       "olsrGatewayTableIndex": olsrGatewayTableIndex,
       "olsrGatewayTableSubnet": olsrGatewayTableSubnet,
       "olsrGatewayTableNetmask": olsrGatewayTableNetmask,
       "olsrGatewayTableComments": olsrGatewayTableComments,
       "olsrGatewayTableActive": olsrGatewayTableActive,
       "olsrGatewayTableRowStatus": olsrGatewayTableRowStatus,
       "nodeConfigurationShaping": nodeConfigurationShaping,
       "shapingActive": shapingActive,
       "shapingWanRateup": shapingWanRateup,
       "shapingWanRatedown": shapingWanRatedown,
       "shapingMeshRateup": shapingMeshRateup,
       "shapingMeshRatedown": shapingMeshRatedown,
       "shapingVlanRateup": shapingVlanRateup,
       "shapingVlanRatedown": shapingVlanRatedown,
       "shapingDefaultup": shapingDefaultup,
       "shapingDefaultdown": shapingDefaultdown,
       "shapingTable": shapingTable,
       "shapingTableEntry": shapingTableEntry,
       "shapingTableIndex": shapingTableIndex,
       "shapingTableProtocol": shapingTableProtocol,
       "shapingTablePort": shapingTablePort,
       "shapingTableMinsize": shapingTableMinsize,
       "shapingTableMaxsize": shapingTableMaxsize,
       "shapingTablePriority": shapingTablePriority,
       "shapingTableComment": shapingTableComment,
       "shapingTableActive": shapingTableActive,
       "shapingTableRowStatus": shapingTableRowStatus,
       "nodeConfigurationPppoe": nodeConfigurationPppoe,
       "pppoeActive": pppoeActive,
       "pppoeUsername": pppoeUsername,
       "pppoePassword": pppoePassword,
       "pppoeAuthType": pppoeAuthType,
       "pppoeUseChap": pppoeUseChap,
       "pppoeChapUsername": pppoeChapUsername,
       "pppoeChapPassword": pppoeChapPassword,
       "nodeConfigurationPptp": nodeConfigurationPptp,
       "pptpActive": pptpActive,
       "pptpTable": pptpTable,
       "pptpTableEntry": pptpTableEntry,
       "pptpTableIndex": pptpTableIndex,
       "pptpTableUsername": pptpTableUsername,
       "pptpTablePassword": pptpTablePassword,
       "pptpTableIp": pptpTableIp,
       "pptpTableComment": pptpTableComment,
       "pptpTableActive": pptpTableActive,
       "pptpTableRowStatus": pptpTableRowStatus,
       "pptpServerip": pptpServerip,
       "pptpStartip": pptpStartip,
       "pptpEndip": pptpEndip,
       "nodeConfigurationTmipd": nodeConfigurationTmipd,
       "tmipdActive": tmipdActive,
       "tmipdNetname": tmipdNetname,
       "tmipdMlrdip": tmipdMlrdip,
       "tmipdVlan": tmipdVlan,
       "nodeConfigurationCaptive": nodeConfigurationCaptive,
       "captiveActive": captiveActive,
       "captiveRedirect": captiveRedirect,
       "captivePop3push": captivePop3push,
       "captiveExternalActive": captiveExternalActive,
       "captiveExternalServer": captiveExternalServer,
       "captiveDefaultIdleTimeout": captiveDefaultIdleTimeout,
       "captiveDefaultSessionTimeout": captiveDefaultSessionTimeout,
       "captiveHttpActive": captiveHttpActive,
       "captiveHttpPort": captiveHttpPort,
       "captiveHttpsActive": captiveHttpsActive,
       "captiveHttpsPort": captiveHttpsPort,
       "captiveWebspaceActive": captiveWebspaceActive,
       "captiveWebspacePort": captiveWebspacePort,
       "captiveDefaultLanguage": captiveDefaultLanguage,
       "captiveMultipleUsername": captiveMultipleUsername,
       "captive1xLogin": captive1xLogin,
       "nodeConfigurationRadiusClient": nodeConfigurationRadiusClient,
       "radiusclientActive": radiusclientActive,
       "radiusclientNasid": radiusclientNasid,
       "radiusclientCalledstationid": radiusclientCalledstationid,
       "radiusclientNasport": radiusclientNasport,
       "radiusclientNasporttype": radiusclientNasporttype,
       "radiusclientInterimupdate": radiusclientInterimupdate,
       "radiusclientTable": radiusclientTable,
       "radiusclientTableEntry": radiusclientTableEntry,
       "radiusclientTableIndex": radiusclientTableIndex,
       "radiusclientTableServername": radiusclientTableServername,
       "radiusclientTableServertype": radiusclientTableServertype,
       "radiusclientTableServerport": radiusclientTableServerport,
       "radiusclientTableServersecret": radiusclientTableServersecret,
       "radiusclientTableComment": radiusclientTableComment,
       "radiusclientTableActive": radiusclientTableActive,
       "radiusclientTableRowStatus": radiusclientTableRowStatus,
       "nodeConfigurationHttpd": nodeConfigurationHttpd,
       "httpdActive": httpdActive,
       "httpdPort": httpdPort,
       "httpdUsername": httpdUsername,
       "httpdPassword": httpdPassword,
       "httpdAccessctrl": httpdAccessctrl,
       "httpdTable": httpdTable,
       "httpdTableEntry": httpdTableEntry,
       "httpdTableIndex": httpdTableIndex,
       "httpdTableDevice": httpdTableDevice,
       "httpdTableSubnet": httpdTableSubnet,
       "httpdTableNetmask": httpdTableNetmask,
       "httpdTableDevnet": httpdTableDevnet,
       "httpdTableComment": httpdTableComment,
       "httpdTableActive": httpdTableActive,
       "httpdTableRowStatus": httpdTableRowStatus,
       "httpdCertPassword": httpdCertPassword,
       "nodeConfigurationSnmpd": nodeConfigurationSnmpd,
       "snmpdActive": snmpdActive,
       "snmpdVersion": snmpdVersion,
       "snmpdPort": snmpdPort,
       "snmpdReadcommunity": snmpdReadcommunity,
       "snmpdWritecommunity": snmpdWritecommunity,
       "snmpdReadusername": snmpdReadusername,
       "snmpdWriteusername": snmpdWriteusername,
       "snmpdPassword": snmpdPassword,
       "snmpdPassphrase": snmpdPassphrase,
       "snmpdAccessctrl": snmpdAccessctrl,
       "snmpdTable": snmpdTable,
       "snmpdTableEntry": snmpdTableEntry,
       "snmpdTableIndex": snmpdTableIndex,
       "snmpdTableDevice": snmpdTableDevice,
       "snmpdTableSubnet": snmpdTableSubnet,
       "snmpdTableNetmask": snmpdTableNetmask,
       "snmpdTableDevnet": snmpdTableDevnet,
       "snmpdTableComment": snmpdTableComment,
       "snmpdTableActive": snmpdTableActive,
       "snmpdTableRowStatus": snmpdTableRowStatus,
       "nodeConfigurationTrap": nodeConfigurationTrap,
       "trapActive": trapActive,
       "trapConfiguration": trapConfiguration,
       "trapSecurity": trapSecurity,
       "trapWireless": trapWireless,
       "trapOperational": trapOperational,
       "trapFlash": trapFlash,
       "trapTftp": trapTftp,
       "trapImage": trapImage,
       "trapAuthentication": trapAuthentication,
       "trapTable": trapTable,
       "trapTableEntry": trapTableEntry,
       "trapTableIndex": trapTableIndex,
       "trapTableIp": trapTableIp,
       "trapTableCommunity": trapTableCommunity,
       "trapTableUsername": trapTableUsername,
       "trapTableAuthpasswd": trapTableAuthpasswd,
       "trapTablePrivpasswd": trapTablePrivpasswd,
       "trapTableVersion": trapTableVersion,
       "trapTableComment": trapTableComment,
       "trapTableActive": trapTableActive,
       "trapTableRowStatus": trapTableRowStatus,
       "nodeConfigurationDdns": nodeConfigurationDdns,
       "ddnsActive": ddnsActive,
       "ddnsServer": ddnsServer,
       "ddnsHostname": ddnsHostname,
       "ddnsUsername": ddnsUsername,
       "ddnsPassword": ddnsPassword,
       "nodeConfigurationZeroconfig": nodeConfigurationZeroconfig,
       "zeroconfigActive": zeroconfigActive,
       "zeroconfigProxyActive": zeroconfigProxyActive,
       "zeroconfigProxyport": zeroconfigProxyport,
       "zeroconfigStaticipActive": zeroconfigStaticipActive,
       "nodeConfigurationSignallevel": nodeConfigurationSignallevel,
       "signallevelExecute": signallevelExecute,
       "signallevelTable": signallevelTable,
       "signallevelTableEntry": signallevelTableEntry,
       "signallevelTableIndex": signallevelTableIndex,
       "signallevelTableSource": signallevelTableSource,
       "signallevelTableDestination": signallevelTableDestination,
       "signallevelTableRssi": signallevelTableRssi,
       "clientInfoTable": clientInfoTable,
       "clientInfoTableEntry": clientInfoTableEntry,
       "clientInfoTableIndex": clientInfoTableIndex,
       "clientInfoTableEssid": clientInfoTableEssid,
       "clientInfoTableMac": clientInfoTableMac,
       "clientInfoTableChannel": clientInfoTableChannel,
       "clientInfoTableRate": clientInfoTableRate,
       "clientInfoTableRssi": clientInfoTableRssi,
       "clientInfoTableIdletime": clientInfoTableIdletime,
       "clientStatTable": clientStatTable,
       "clientStatTableEntry": clientStatTableEntry,
       "clientStatTableIndex": clientStatTableIndex,
       "clientStatTableIp": clientStatTableIp,
       "clientStatTableMac": clientStatTableMac,
       "clientStatTableTx": clientStatTableTx,
       "clientStatTableRx": clientStatTableRx,
       "clientStatTableTxPkt": clientStatTableTxPkt,
       "clientStatTableRxPkt": clientStatTableRxPkt,
       "clientStatTableOnlinetime": clientStatTableOnlinetime,
       "nodeConfigurationIpsec": nodeConfigurationIpsec,
       "ipsecActive": ipsecActive,
       "ipsecType": ipsecType,
       "ipsecLocalId": ipsecLocalId,
       "ipsecRemoteId": ipsecRemoteId,
       "ipsecRemoteIp": ipsecRemoteIp,
       "ipsecRemoteSubnet": ipsecRemoteSubnet,
       "ipsecRemoteNetmask": ipsecRemoteNetmask,
       "ipsecLocalCertpass": ipsecLocalCertpass,
       "ipsecLocalRsa": ipsecLocalRsa,
       "ipsecRemoteRsa": ipsecRemoteRsa,
       "ipsecPsk": ipsecPsk,
       "nodeConfigurationL2tpc": nodeConfigurationL2tpc,
       "l2tpcActive": l2tpcActive,
       "l2tpcLns": l2tpcLns,
       "l2tpcUsername": l2tpcUsername,
       "l2tpcSecret": l2tpcSecret,
       "nodeConfigurationAutoip": nodeConfigurationAutoip,
       "autoipActive": autoipActive,
       "autoipMeship": autoipMeship,
       "autoipVlanip": autoipVlanip,
       "nodeConfigurationInterfaces": nodeConfigurationInterfaces,
       "interfacesTable": interfacesTable,
       "interfacesTableEntry": interfacesTableEntry,
       "interfacesTableIndex": interfacesTableIndex,
       "interfacesTableDev": interfacesTableDev,
       "interfacesTableLabel": interfacesTableLabel,
       "nodeConfigurationMlrd": nodeConfigurationMlrd,
       "mlrdActive": mlrdActive,
       "mlrdNetname": mlrdNetname,
       "mlrdBackupActive": mlrdBackupActive,
       "mlrdRole": mlrdRole,
       "mlrdPeer": mlrdPeer,
       "mlrdBackupInterval": mlrdBackupInterval,
       "mlrdStaticActive": mlrdStaticActive,
       "mlrdTable": mlrdTable,
       "mlrdTableEntry": mlrdTableEntry,
       "mlrdTableIndex": mlrdTableIndex,
       "mlrdTableMac": mlrdTableMac,
       "mlrdTableIp": mlrdTableIp,
       "mlrdTableParent": mlrdTableParent,
       "mlrdTableDefaultRoute": mlrdTableDefaultRoute,
       "mlrdTableComment": mlrdTableComment,
       "mlrdTableActive": mlrdTableActive,
       "mlrdTableRowStatus": mlrdTableRowStatus,
       "nodeConfigurationRoutedog": nodeConfigurationRoutedog,
       "routedogActive": routedogActive,
       "routedogSsid": routedogSsid,
       "routedogInterval": routedogInterval,
       "routedogReboot": routedogReboot,
       "routedogIntervaCount": routedogIntervaCount,
       "nodeConfigurationLinuxdog": nodeConfigurationLinuxdog,
       "linuxdogActive": linuxdogActive,
       "linuxdogInterval": linuxdogInterval,
       "nodeConfigurationAdvTunning": nodeConfigurationAdvTunning,
       "advTunningConntrackMax": advTunningConntrackMax,
       "advTunningConntrackGenericTimeout": advTunningConntrackGenericTimeout,
       "advTunningConntrackIcmpTimeout": advTunningConntrackIcmpTimeout,
       "advTunningConntrackTcpcloseTimeout": advTunningConntrackTcpcloseTimeout,
       "advTunningConntrackTcpclosewaitTimeout": advTunningConntrackTcpclosewaitTimeout,
       "advTunningConntrackTcpestablishTimeout": advTunningConntrackTcpestablishTimeout,
       "advTunningConntrackTcpfinwaitTimeout": advTunningConntrackTcpfinwaitTimeout,
       "advTunningConntrackTcplastackTimeout": advTunningConntrackTcplastackTimeout,
       "advTunningConntrackTcpsynrecvTimeout": advTunningConntrackTcpsynrecvTimeout,
       "advTunningConntrackTcpsynsentTimeout": advTunningConntrackTcpsynsentTimeout,
       "advTunningConntrackTcptimewaitTimeout": advTunningConntrackTcptimewaitTimeout,
       "advTunningConntrackUdpTimeout": advTunningConntrackUdpTimeout,
       "advTunningConntrackUdpstreamTimeout": advTunningConntrackUdpstreamTimeout,
       "advTunningWirelessRadio0Distance": advTunningWirelessRadio0Distance,
       "advTunningWirelessRadio1Distance": advTunningWirelessRadio1Distance,
       "advTunningWirelessRadio2Distance": advTunningWirelessRadio2Distance,
       "advTunningWirelessRadio3Distance": advTunningWirelessRadio3Distance,
       "advTunningWirelessRegionDomain": advTunningWirelessRegionDomain,
       "advTunningWirelessCountry": advTunningWirelessCountry,
       "advTunningWirelessOutdoor": advTunningWirelessOutdoor,
       "advTunningWirelessXChannel": advTunningWirelessXChannel,
       "nodeConfigurationSshd": nodeConfigurationSshd,
       "sshdActive": sshdActive,
       "sshdPort": sshdPort,
       "nodeConfigutationWme": nodeConfigutationWme,
       "wmeTable": wmeTable,
       "wmeTableEntry": wmeTableEntry,
       "wmeTableIndex": wmeTableIndex,
       "wmeTableName": wmeTableName,
       "wmeTableCwminBe": wmeTableCwminBe,
       "wmeTableCwminBk": wmeTableCwminBk,
       "wmeTableCwminVi": wmeTableCwminVi,
       "wmeTableCwminVo": wmeTableCwminVo,
       "wmeTableBssCwminBe": wmeTableBssCwminBe,
       "wmeTableBssCwminBk": wmeTableBssCwminBk,
       "wmeTableBssCwminVi": wmeTableBssCwminVi,
       "wmeTableBssCwminVo": wmeTableBssCwminVo,
       "wmeTableCwmaxBe": wmeTableCwmaxBe,
       "wmeTableCwmaxBk": wmeTableCwmaxBk,
       "wmeTableCwmaxVi": wmeTableCwmaxVi,
       "wmeTableCwmaxVo": wmeTableCwmaxVo,
       "wmeTableBssCwmaxBe": wmeTableBssCwmaxBe,
       "wmeTableBssCwmaxBk": wmeTableBssCwmaxBk,
       "wmeTableBssCwmaxVi": wmeTableBssCwmaxVi,
       "wmeTableBssCwmaxVo": wmeTableBssCwmaxVo,
       "wmeTableAifsnBe": wmeTableAifsnBe,
       "wmeTableAifsnBk": wmeTableAifsnBk,
       "wmeTableAifsnVi": wmeTableAifsnVi,
       "wmeTableAifsnVo": wmeTableAifsnVo,
       "wmeTableBssAifsnBe": wmeTableBssAifsnBe,
       "wmeTableBssAifsnBk": wmeTableBssAifsnBk,
       "wmeTableBssAifsnVi": wmeTableBssAifsnVi,
       "wmeTableBssAifsnVo": wmeTableBssAifsnVo,
       "wmeTableTxoplimitBe": wmeTableTxoplimitBe,
       "wmeTableTxoplimitBk": wmeTableTxoplimitBk,
       "wmeTableTxoplimitVi": wmeTableTxoplimitVi,
       "wmeTableTxoplimitVo": wmeTableTxoplimitVo,
       "wmeTableBssTxoplimitBe": wmeTableBssTxoplimitBe,
       "wmeTableBssTxoplimitBk": wmeTableBssTxoplimitBk,
       "wmeTableBssTxoplimitVi": wmeTableBssTxoplimitVi,
       "wmeTableBssTxoplimitVo": wmeTableBssTxoplimitVo,
       "wmeTableAcmBe": wmeTableAcmBe,
       "wmeTableAcmBk": wmeTableAcmBk,
       "wmeTableAcmVi": wmeTableAcmVi,
       "wmeTableAcmVo": wmeTableAcmVo,
       "wmeTableNoackpolicyBe": wmeTableNoackpolicyBe,
       "wmeTableNoackpolicyBk": wmeTableNoackpolicyBk,
       "wmeTableNoackpolicyVi": wmeTableNoackpolicyVi,
       "wmeTableNoackpolicyVo": wmeTableNoackpolicyVo,
       "wmeTableComment": wmeTableComment,
       "wmeTableActive": wmeTableActive,
       "wmeTableRowStatus": wmeTableRowStatus,
       "nodeConfigurationTm75": nodeConfigurationTm75,
       "tm75Active": tm75Active,
       "tm75Resolution": tm75Resolution,
       "tm75Temperature": tm75Temperature,
       "nodeConfigurationNmsAddress": nodeConfigurationNmsAddress,
       "nmsAddressTable": nmsAddressTable,
       "nmsAddressTableEntry": nmsAddressTableEntry,
       "nmsAddressTableIndex": nmsAddressTableIndex,
       "nmsAddressTableAddress": nmsAddressTableAddress,
       "nmsAddressTablePort": nmsAddressTablePort,
       "nmsAddressTableInterval": nmsAddressTableInterval,
       "nmsAddressTableComment": nmsAddressTableComment,
       "nmsAddressTableActive": nmsAddressTableActive,
       "nmsAddressTableRowStatus": nmsAddressTableRowStatus,
       "nodeConfigurationUserDb": nodeConfigurationUserDb,
       "userDbUsername": userDbUsername,
       "userDbPassword": userDbPassword,
       "userDbGroupid": userDbGroupid,
       "userDbAddCmd": userDbAddCmd,
       "userDbEditCmd": userDbEditCmd,
       "userDbDelCmd": userDbDelCmd,
       "userDbTable": userDbTable,
       "userDbTableEntry": userDbTableEntry,
       "userDbTableIndex": userDbTableIndex,
       "userDbTableName": userDbTableName,
       "userDbTablePassword": userDbTablePassword,
       "userDbTableGid": userDbTableGid,
       "userDbTableStatus": userDbTableStatus,
       "nodeConfigurationUserGroup": nodeConfigurationUserGroup,
       "userGroupId": userGroupId,
       "userGroupName": userGroupName,
       "userGroupLanguage": userGroupLanguage,
       "userGroupUpload": userGroupUpload,
       "userGroupDownload": userGroupDownload,
       "userGroupIdleTimeout": userGroupIdleTimeout,
       "userGroupSessionTimeout": userGroupSessionTimeout,
       "userGroupUrl": userGroupUrl,
       "userGroupComment": userGroupComment,
       "userGroupAddCmd": userGroupAddCmd,
       "userGroupEditCmd": userGroupEditCmd,
       "userGroupDelCmd": userGroupDelCmd,
       "userGroupTable": userGroupTable,
       "userGroupTableEntry": userGroupTableEntry,
       "userGroupTableIndex": userGroupTableIndex,
       "userGroupTableGid": userGroupTableGid,
       "userGroupTableName": userGroupTableName,
       "userGroupTableLanguage": userGroupTableLanguage,
       "userGroupTableUpload": userGroupTableUpload,
       "userGroupTableDownload": userGroupTableDownload,
       "userGroupTableIdleTimeout": userGroupTableIdleTimeout,
       "userGroupTableSessTimeout": userGroupTableSessTimeout,
       "userGroupTableUrl": userGroupTableUrl,
       "userGroupTableComment": userGroupTableComment,
       "nodeConfigurationStatickey": nodeConfigurationStatickey,
       "statickeyWifi0Key0": statickeyWifi0Key0,
       "statickeyWifi0Key1": statickeyWifi0Key1,
       "statickeyWifi0Key2": statickeyWifi0Key2,
       "statickeyWifi0Key3": statickeyWifi0Key3,
       "statickeyWifi1Key0": statickeyWifi1Key0,
       "statickeyWifi1Key1": statickeyWifi1Key1,
       "statickeyWifi1Key2": statickeyWifi1Key2,
       "statickeyWifi1Key3": statickeyWifi1Key3,
       "nodeConfigurationDhcrelay": nodeConfigurationDhcrelay,
       "dhcrelayActive": dhcrelayActive,
       "dhcrelayPort": dhcrelayPort,
       "dhcrelayHopcount": dhcrelayHopcount,
       "dhcrelayPktsize": dhcrelayPktsize,
       "dhcrelayTable": dhcrelayTable,
       "dhcrelayTableEntry": dhcrelayTableEntry,
       "dhcrelayTableIndex": dhcrelayTableIndex,
       "dhcrelayTableType": dhcrelayTableType,
       "dhcrelayTableExtra": dhcrelayTableExtra,
       "dhcrelayTableComments": dhcrelayTableComments,
       "dhcrelayTableActive": dhcrelayTableActive,
       "dhcrelayTableRowStatus": dhcrelayTableRowStatus,
       "nodeConfigurationMulticast": nodeConfigurationMulticast,
       "multicastActive": multicastActive,
       "nodeConfigurationOspfd": nodeConfigurationOspfd,
       "ospfdActive": ospfdActive,
       "nodeConfigurationEbtables": nodeConfigurationEbtables,
       "ebtablesActive": ebtablesActive,
       "ebTable": ebTable,
       "ebTableEntry": ebTableEntry,
       "ebTableIndex": ebTableIndex,
       "ebTableTarget": ebTableTarget,
       "ebTableSrcIface": ebTableSrcIface,
       "ebTableDstIface": ebTableDstIface,
       "ebTableMatchMac": ebTableMatchMac,
       "ebTableSrcMac": ebTableSrcMac,
       "ebTableDstMac": ebTableDstMac,
       "ebTableProtocol": ebTableProtocol,
       "ebTableSrcIp": ebTableSrcIp,
       "ebTableSrcMask": ebTableSrcMask,
       "ebTableDstIp": ebTableDstIp,
       "ebTableDstMask": ebTableDstMask,
       "ebTableIpProt": ebTableIpProt,
       "ebTableSrcPortStart": ebTableSrcPortStart,
       "ebTableSrcPortEnd": ebTableSrcPortEnd,
       "ebTableDstPortStart": ebTableDstPortStart,
       "ebTableDstPortEnd": ebTableDstPortEnd,
       "ebTableVlanid": ebTableVlanid,
       "ebTableComments": ebTableComments,
       "ebTableActive": ebTableActive,
       "ebTableRowStatus": ebTableRowStatus,
       "nodeCommand": nodeCommand,
       "nodeCommandReboot": nodeCommandReboot,
       "rebootTime": rebootTime,
       "nodeCommandReset": nodeCommandReset,
       "resetToDefault": resetToDefault,
       "nodeCommandUpload": nodeCommandUpload,
       "uploadDownloadFilename": uploadDownloadFilename,
       "uploadDownloadFiletype": uploadDownloadFiletype,
       "uploadDownloadIpaddress": uploadDownloadIpaddress,
       "uploadDownloadPassword": uploadDownloadPassword,
       "uploadDownloadOperationtype": uploadDownloadOperationtype,
       "uploadDownloadExecutetftp": uploadDownloadExecutetftp,
       "nodeCommandLogoutBlock": nodeCommandLogoutBlock,
       "logoutAndBlockAction": logoutAndBlockAction,
       "nodeCommandRestartSnmp": nodeCommandRestartSnmp,
       "restartSnmpService": restartSnmpService}
)
