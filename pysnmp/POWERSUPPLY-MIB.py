# SNMP MIB module (POWERSUPPLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POWERSUPPLY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:29 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfPsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55)
)
hpicfPsMIB.setRevisions(
        ("2013-08-20 00:00",
         "2013-06-13 00:00",
         "2013-03-07 10:00",
         "2008-08-27 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfDcPsIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class HpicfDcPsState(Integer32, TextualConvention):
    status = "current"
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
        *(("psAuxFailure", 7),
          ("psAuxNotPowered", 9),
          ("psFailed", 4),
          ("psMax", 6),
          ("psNotPlugged", 2),
          ("psNotPowered", 8),
          ("psNotPresent", 1),
          ("psPermFailure", 5),
          ("psPowered", 3))
    )



class HpicfXpsConnectionStatus(Integer32, TextualConvention):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("autoDisabled", 8),
          ("available", 2),
          ("cannotPower", 7),
          ("mismatch", 4),
          ("notConnected", 0),
          ("notReady", 5),
          ("overCurrent", 6),
          ("unavailable", 1))
    )



class HpicfXpsZoneStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("faulted", 3),
          ("inReset", 5),
          ("notConnected", 1),
          ("notReady", 2),
          ("powered", 4))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfEntityPs_ObjectIdentity = ObjectIdentity
hpicfEntityPs = _HpicfEntityPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1)
)
_HpicfPsTable_Object = MibTable
hpicfPsTable = _HpicfPsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfPsTable.setStatus("current")
_HpicfPsEntry_Object = MibTableRow
hpicfPsEntry = _HpicfPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1)
)
hpicfPsEntry.setIndexNames(
    (0, "POWERSUPPLY-MIB", "hpicfPsBayNum"),
)
if mibBuilder.loadTexts:
    hpicfPsEntry.setStatus("current")
_HpicfPsBayNum_Type = HpicfDcPsIndex
_HpicfPsBayNum_Object = MibTableColumn
hpicfPsBayNum = _HpicfPsBayNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 1),
    _HpicfPsBayNum_Type()
)
hpicfPsBayNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPsBayNum.setStatus("current")
_HpicfPsState_Type = HpicfDcPsState
_HpicfPsState_Object = MibTableColumn
hpicfPsState = _HpicfPsState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 2),
    _HpicfPsState_Type()
)
hpicfPsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsState.setStatus("current")
_HpicfPsFailures_Type = Counter32
_HpicfPsFailures_Object = MibTableColumn
hpicfPsFailures = _HpicfPsFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 3),
    _HpicfPsFailures_Type()
)
hpicfPsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsFailures.setStatus("current")
_HpicfPsTemp_Type = Integer32
_HpicfPsTemp_Object = MibTableColumn
hpicfPsTemp = _HpicfPsTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 4),
    _HpicfPsTemp_Type()
)
hpicfPsTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsTemp.setStatus("current")


class _HpicfPsVoltageInfo_Type(SnmpAdminString):
    """Custom type hpicfPsVoltageInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpicfPsVoltageInfo_Type.__name__ = "SnmpAdminString"
_HpicfPsVoltageInfo_Object = MibTableColumn
hpicfPsVoltageInfo = _HpicfPsVoltageInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 5),
    _HpicfPsVoltageInfo_Type()
)
hpicfPsVoltageInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsVoltageInfo.setStatus("current")
_HpicfPsWattageCur_Type = Integer32
_HpicfPsWattageCur_Object = MibTableColumn
hpicfPsWattageCur = _HpicfPsWattageCur_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 6),
    _HpicfPsWattageCur_Type()
)
hpicfPsWattageCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsWattageCur.setStatus("current")
_HpicfPsWattageMax_Type = Integer32
_HpicfPsWattageMax_Object = MibTableColumn
hpicfPsWattageMax = _HpicfPsWattageMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 7),
    _HpicfPsWattageMax_Type()
)
hpicfPsWattageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsWattageMax.setStatus("current")
_HpicfPsLastCall_Type = Counter32
_HpicfPsLastCall_Object = MibTableColumn
hpicfPsLastCall = _HpicfPsLastCall_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 8),
    _HpicfPsLastCall_Type()
)
hpicfPsLastCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsLastCall.setStatus("current")


class _HpicfPsModel_Type(DisplayString):
    """Custom type hpicfPsModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfPsModel_Type.__name__ = "DisplayString"
_HpicfPsModel_Object = MibTableColumn
hpicfPsModel = _HpicfPsModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 9),
    _HpicfPsModel_Type()
)
hpicfPsModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPsModel.setStatus("current")
_HpicfXpsTable_Object = MibTable
hpicfXpsTable = _HpicfXpsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfXpsTable.setStatus("current")
_HpicfXpsEntry_Object = MibTableRow
hpicfXpsEntry = _HpicfXpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1)
)
hpicfXpsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "POWERSUPPLY-MIB", "hpicfXpsConnectingPort"),
)
if mibBuilder.loadTexts:
    hpicfXpsEntry.setStatus("current")
_HpicfXpsConnectingPort_Type = Unsigned32
_HpicfXpsConnectingPort_Object = MibTableColumn
hpicfXpsConnectingPort = _HpicfXpsConnectingPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 1),
    _HpicfXpsConnectingPort_Type()
)
hpicfXpsConnectingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfXpsConnectingPort.setStatus("current")


class _HpicfXpsPortOperStatus_Type(Integer32):
    """Custom type hpicfXpsPortOperStatus based on Integer32"""
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


_HpicfXpsPortOperStatus_Type.__name__ = "Integer32"
_HpicfXpsPortOperStatus_Object = MibTableColumn
hpicfXpsPortOperStatus = _HpicfXpsPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 2),
    _HpicfXpsPortOperStatus_Type()
)
hpicfXpsPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsPortOperStatus.setStatus("current")
_HpicfXpsSwitchSerialNo_Type = DisplayString
_HpicfXpsSwitchSerialNo_Object = MibTableColumn
hpicfXpsSwitchSerialNo = _HpicfXpsSwitchSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 3),
    _HpicfXpsSwitchSerialNo_Type()
)
hpicfXpsSwitchSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsSwitchSerialNo.setStatus("current")
_HpicfXpsConnectionState_Type = HpicfXpsConnectionStatus
_HpicfXpsConnectionState_Object = MibTableColumn
hpicfXpsConnectionState = _HpicfXpsConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 4),
    _HpicfXpsConnectionState_Type()
)
hpicfXpsConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsConnectionState.setStatus("current")
_HpicfXpsSysName_Type = DisplayString
_HpicfXpsSysName_Object = MibTableColumn
hpicfXpsSysName = _HpicfXpsSysName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 5),
    _HpicfXpsSysName_Type()
)
hpicfXpsSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsSysName.setStatus("current")
_HpicfXpsMACAddress_Type = MacAddress
_HpicfXpsMACAddress_Object = MibTableColumn
hpicfXpsMACAddress = _HpicfXpsMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 6),
    _HpicfXpsMACAddress_Type()
)
hpicfXpsMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsMACAddress.setStatus("current")
_HpicfXpsSwitchOSVersion_Type = DisplayString
_HpicfXpsSwitchOSVersion_Object = MibTableColumn
hpicfXpsSwitchOSVersion = _HpicfXpsSwitchOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 7),
    _HpicfXpsSwitchOSVersion_Type()
)
hpicfXpsSwitchOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsSwitchOSVersion.setStatus("current")
_HpicfXpsSwitchIpsVoltage_Type = Unsigned32
_HpicfXpsSwitchIpsVoltage_Object = MibTableColumn
hpicfXpsSwitchIpsVoltage = _HpicfXpsSwitchIpsVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 8),
    _HpicfXpsSwitchIpsVoltage_Type()
)
hpicfXpsSwitchIpsVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsSwitchIpsVoltage.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXpsSwitchIpsVoltage.setUnits("Volts")
_HpicfXpsSwitchIpsWattage_Type = Unsigned32
_HpicfXpsSwitchIpsWattage_Object = MibTableColumn
hpicfXpsSwitchIpsWattage = _HpicfXpsSwitchIpsWattage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 9),
    _HpicfXpsSwitchIpsWattage_Type()
)
hpicfXpsSwitchIpsWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsSwitchIpsWattage.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXpsSwitchIpsWattage.setUnits("Watts")
_HpicfXpsPower_Type = Unsigned32
_HpicfXpsPower_Object = MibTableColumn
hpicfXpsPower = _HpicfXpsPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 10),
    _HpicfXpsPower_Type()
)
hpicfXpsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsPower.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXpsPower.setUnits("Watts")
_HpicfXpsSupportedCableVersion_Type = Unsigned32
_HpicfXpsSupportedCableVersion_Object = MibTableColumn
hpicfXpsSupportedCableVersion = _HpicfXpsSupportedCableVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 11),
    _HpicfXpsSupportedCableVersion_Type()
)
hpicfXpsSupportedCableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsSupportedCableVersion.setStatus("current")
_HpicfXpsSupportedZoneVersion_Type = Unsigned32
_HpicfXpsSupportedZoneVersion_Object = MibTableColumn
hpicfXpsSupportedZoneVersion = _HpicfXpsSupportedZoneVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 12),
    _HpicfXpsSupportedZoneVersion_Type()
)
hpicfXpsSupportedZoneVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsSupportedZoneVersion.setStatus("current")
_HpicfXpsSwitchModType_Type = DisplayString
_HpicfXpsSwitchModType_Object = MibTableColumn
hpicfXpsSwitchModType = _HpicfXpsSwitchModType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 13),
    _HpicfXpsSwitchModType_Type()
)
hpicfXpsSwitchModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsSwitchModType.setStatus("current")
_HpicfXpsSwitchConfigTable_Object = MibTable
hpicfXpsSwitchConfigTable = _HpicfXpsSwitchConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfXpsSwitchConfigTable.setStatus("current")
_HpicfXpsSwitchConfigEntry_Object = MibTableRow
hpicfXpsSwitchConfigEntry = _HpicfXpsSwitchConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1)
)
hpicfXpsSwitchConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfXpsSwitchConfigEntry.setStatus("current")


class _HpicfXpsSwitchAdminStatus_Type(Integer32):
    """Custom type hpicfXpsSwitchAdminStatus based on Integer32"""
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


_HpicfXpsSwitchAdminStatus_Type.__name__ = "Integer32"
_HpicfXpsSwitchAdminStatus_Object = MibTableColumn
hpicfXpsSwitchAdminStatus = _HpicfXpsSwitchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 1),
    _HpicfXpsSwitchAdminStatus_Type()
)
hpicfXpsSwitchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXpsSwitchAdminStatus.setStatus("current")


class _HpicfXpsSwitchAutoRecovery_Type(Integer32):
    """Custom type hpicfXpsSwitchAutoRecovery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HpicfXpsSwitchAutoRecovery_Type.__name__ = "Integer32"
_HpicfXpsSwitchAutoRecovery_Object = MibTableColumn
hpicfXpsSwitchAutoRecovery = _HpicfXpsSwitchAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 2),
    _HpicfXpsSwitchAutoRecovery_Type()
)
hpicfXpsSwitchAutoRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXpsSwitchAutoRecovery.setStatus("current")


class _HpicfXpsAllowPortsSupported_Type(Unsigned32):
    """Custom type hpicfXpsAllowPortsSupported based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_HpicfXpsAllowPortsSupported_Type.__name__ = "Unsigned32"
_HpicfXpsAllowPortsSupported_Object = MibTableColumn
hpicfXpsAllowPortsSupported = _HpicfXpsAllowPortsSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 3),
    _HpicfXpsAllowPortsSupported_Type()
)
hpicfXpsAllowPortsSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXpsAllowPortsSupported.setStatus("current")


class _HpicfXpsReset_Type(Integer32):
    """Custom type hpicfXpsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryReset", 2),
          ("noReset", 1))
    )


_HpicfXpsReset_Type.__name__ = "Integer32"
_HpicfXpsReset_Object = MibTableColumn
hpicfXpsReset = _HpicfXpsReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 4),
    _HpicfXpsReset_Type()
)
hpicfXpsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXpsReset.setStatus("current")


class _HpicfXpsType_Type(OctetString):
    """Custom type hpicfXpsType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfXpsType_Type.__name__ = "OctetString"
_HpicfXpsType_Object = MibTableColumn
hpicfXpsType = _HpicfXpsType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 5),
    _HpicfXpsType_Type()
)
hpicfXpsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsType.setStatus("current")
_HpicfXpsSerialNum_Type = SnmpAdminString
_HpicfXpsSerialNum_Object = MibTableColumn
hpicfXpsSerialNum = _HpicfXpsSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 6),
    _HpicfXpsSerialNum_Type()
)
hpicfXpsSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsSerialNum.setStatus("current")
_HpicfXpsModuleName_Type = SnmpAdminString
_HpicfXpsModuleName_Object = MibTableColumn
hpicfXpsModuleName = _HpicfXpsModuleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 7),
    _HpicfXpsModuleName_Type()
)
hpicfXpsModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsModuleName.setStatus("current")


class _HpicfXpsPowerShareReqStatus_Type(Integer32):
    """Custom type hpicfXpsPowerShareReqStatus based on Integer32"""
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
        *(("failed", 4),
          ("idle", 1),
          ("inProgress", 2),
          ("success", 3))
    )


_HpicfXpsPowerShareReqStatus_Type.__name__ = "Integer32"
_HpicfXpsPowerShareReqStatus_Object = MibTableColumn
hpicfXpsPowerShareReqStatus = _HpicfXpsPowerShareReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 8),
    _HpicfXpsPowerShareReqStatus_Type()
)
hpicfXpsPowerShareReqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsPowerShareReqStatus.setStatus("current")


class _HpicfXpsResetReqStatus_Type(Integer32):
    """Custom type hpicfXpsResetReqStatus based on Integer32"""
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
        *(("failed", 4),
          ("idle", 1),
          ("inProgress", 2),
          ("success", 3))
    )


_HpicfXpsResetReqStatus_Type.__name__ = "Integer32"
_HpicfXpsResetReqStatus_Object = MibTableColumn
hpicfXpsResetReqStatus = _HpicfXpsResetReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 9),
    _HpicfXpsResetReqStatus_Type()
)
hpicfXpsResetReqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsResetReqStatus.setStatus("current")
_HpicfXpsZoneTable_Object = MibTable
hpicfXpsZoneTable = _HpicfXpsZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfXpsZoneTable.setStatus("current")
_HpicfXpsZoneEntry_Object = MibTableRow
hpicfXpsZoneEntry = _HpicfXpsZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1)
)
hpicfXpsZoneEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfXpsZoneEntry.setStatus("current")


class _HpicfXpsZoneNo_Type(Unsigned32):
    """Custom type hpicfXpsZoneNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HpicfXpsZoneNo_Type.__name__ = "Unsigned32"
_HpicfXpsZoneNo_Object = MibTableColumn
hpicfXpsZoneNo = _HpicfXpsZoneNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 1),
    _HpicfXpsZoneNo_Type()
)
hpicfXpsZoneNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsZoneNo.setStatus("current")
_HpicfXpsZoneState_Type = HpicfXpsZoneStatus
_HpicfXpsZoneState_Object = MibTableColumn
hpicfXpsZoneState = _HpicfXpsZoneState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 2),
    _HpicfXpsZoneState_Type()
)
hpicfXpsZoneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsZoneState.setStatus("current")


class _HpicfXpsZonePowerShareMap_Type(OctetString):
    """Custom type hpicfXpsZonePowerShareMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfXpsZonePowerShareMap_Type.__name__ = "OctetString"
_HpicfXpsZonePowerShareMap_Object = MibTableColumn
hpicfXpsZonePowerShareMap = _HpicfXpsZonePowerShareMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 3),
    _HpicfXpsZonePowerShareMap_Type()
)
hpicfXpsZonePowerShareMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXpsZonePowerShareMap.setStatus("current")
_HpicfXpsZoneVoltage_Type = Unsigned32
_HpicfXpsZoneVoltage_Object = MibTableColumn
hpicfXpsZoneVoltage = _HpicfXpsZoneVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 4),
    _HpicfXpsZoneVoltage_Type()
)
hpicfXpsZoneVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsZoneVoltage.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXpsZoneVoltage.setUnits("Volts")
_HpicfXpsZoneWattage_Type = Unsigned32
_HpicfXpsZoneWattage_Object = MibTableColumn
hpicfXpsZoneWattage = _HpicfXpsZoneWattage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 5),
    _HpicfXpsZoneWattage_Type()
)
hpicfXpsZoneWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsZoneWattage.setStatus("current")
if mibBuilder.loadTexts:
    hpicfXpsZoneWattage.setUnits("Watts")
_HpicfXpsPSURev_Type = Unsigned32
_HpicfXpsPSURev_Object = MibTableColumn
hpicfXpsPSURev = _HpicfXpsPSURev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 6),
    _HpicfXpsPSURev_Type()
)
hpicfXpsPSURev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsPSURev.setStatus("current")
_HpicfXpsPSUModule_Type = SnmpAdminString
_HpicfXpsPSUModule_Object = MibTableColumn
hpicfXpsPSUModule = _HpicfXpsPSUModule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 7),
    _HpicfXpsPSUModule_Type()
)
hpicfXpsPSUModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsPSUModule.setStatus("current")
_HpicfXpsZonePowerShareForce_Type = TruthValue
_HpicfXpsZonePowerShareForce_Object = MibTableColumn
hpicfXpsZonePowerShareForce = _HpicfXpsZonePowerShareForce_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 8),
    _HpicfXpsZonePowerShareForce_Type()
)
hpicfXpsZonePowerShareForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfXpsZonePowerShareForce.setStatus("current")
_HpicfXpsZoneRecordVersion_Type = Unsigned32
_HpicfXpsZoneRecordVersion_Object = MibTableColumn
hpicfXpsZoneRecordVersion = _HpicfXpsZoneRecordVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 9),
    _HpicfXpsZoneRecordVersion_Type()
)
hpicfXpsZoneRecordVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfXpsZoneRecordVersion.setStatus("current")
_HpicfPsConformance_ObjectIdentity = ObjectIdentity
hpicfPsConformance = _HpicfPsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2)
)
_HpicfPsCompliance_ObjectIdentity = ObjectIdentity
hpicfPsCompliance = _HpicfPsCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1)
)
_HpicfPsGroups_ObjectIdentity = ObjectIdentity
hpicfPsGroups = _HpicfPsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2)
)

# Managed Objects groups

hpicfPsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2, 1)
)
hpicfPsGroup.setObjects(
      *(("POWERSUPPLY-MIB", "hpicfPsState"),
        ("POWERSUPPLY-MIB", "hpicfPsFailures"),
        ("POWERSUPPLY-MIB", "hpicfPsTemp"),
        ("POWERSUPPLY-MIB", "hpicfPsVoltageInfo"),
        ("POWERSUPPLY-MIB", "hpicfPsWattageCur"),
        ("POWERSUPPLY-MIB", "hpicfPsWattageMax"),
        ("POWERSUPPLY-MIB", "hpicfPsLastCall"))
)
if mibBuilder.loadTexts:
    hpicfPsGroup.setStatus("deprecated")

hpicfXpsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2, 2)
)
hpicfXpsGroup.setObjects(
      *(("POWERSUPPLY-MIB", "hpicfXpsPortOperStatus"),
        ("POWERSUPPLY-MIB", "hpicfXpsSwitchSerialNo"),
        ("POWERSUPPLY-MIB", "hpicfXpsConnectionState"),
        ("POWERSUPPLY-MIB", "hpicfXpsSysName"),
        ("POWERSUPPLY-MIB", "hpicfXpsMACAddress"),
        ("POWERSUPPLY-MIB", "hpicfXpsSwitchOSVersion"),
        ("POWERSUPPLY-MIB", "hpicfXpsSwitchIpsVoltage"),
        ("POWERSUPPLY-MIB", "hpicfXpsSwitchIpsWattage"),
        ("POWERSUPPLY-MIB", "hpicfXpsPower"),
        ("POWERSUPPLY-MIB", "hpicfXpsSwitchAdminStatus"),
        ("POWERSUPPLY-MIB", "hpicfXpsSwitchAutoRecovery"),
        ("POWERSUPPLY-MIB", "hpicfXpsAllowPortsSupported"),
        ("POWERSUPPLY-MIB", "hpicfXpsReset"),
        ("POWERSUPPLY-MIB", "hpicfXpsType"),
        ("POWERSUPPLY-MIB", "hpicfXpsSerialNum"),
        ("POWERSUPPLY-MIB", "hpicfXpsModuleName"),
        ("POWERSUPPLY-MIB", "hpicfXpsPowerShareReqStatus"),
        ("POWERSUPPLY-MIB", "hpicfXpsResetReqStatus"),
        ("POWERSUPPLY-MIB", "hpicfXpsSupportedCableVersion"),
        ("POWERSUPPLY-MIB", "hpicfXpsSupportedZoneVersion"),
        ("POWERSUPPLY-MIB", "hpicfXpsSwitchModType"))
)
if mibBuilder.loadTexts:
    hpicfXpsGroup.setStatus("current")

hpicfXpsZoneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2, 3)
)
hpicfXpsZoneGroup.setObjects(
      *(("POWERSUPPLY-MIB", "hpicfXpsZoneNo"),
        ("POWERSUPPLY-MIB", "hpicfXpsZoneState"),
        ("POWERSUPPLY-MIB", "hpicfXpsZonePowerShareMap"),
        ("POWERSUPPLY-MIB", "hpicfXpsZoneVoltage"),
        ("POWERSUPPLY-MIB", "hpicfXpsZoneWattage"),
        ("POWERSUPPLY-MIB", "hpicfXpsPSURev"),
        ("POWERSUPPLY-MIB", "hpicfXpsPSUModule"),
        ("POWERSUPPLY-MIB", "hpicfXpsZonePowerShareForce"),
        ("POWERSUPPLY-MIB", "hpicfXpsZoneRecordVersion"))
)
if mibBuilder.loadTexts:
    hpicfXpsZoneGroup.setStatus("current")

hpicfPsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2, 4)
)
hpicfPsGroup1.setObjects(
      *(("POWERSUPPLY-MIB", "hpicfPsState"),
        ("POWERSUPPLY-MIB", "hpicfPsFailures"),
        ("POWERSUPPLY-MIB", "hpicfPsTemp"),
        ("POWERSUPPLY-MIB", "hpicfPsVoltageInfo"),
        ("POWERSUPPLY-MIB", "hpicfPsWattageCur"),
        ("POWERSUPPLY-MIB", "hpicfPsWattageMax"),
        ("POWERSUPPLY-MIB", "hpicfPsLastCall"),
        ("POWERSUPPLY-MIB", "hpicfPsModel"))
)
if mibBuilder.loadTexts:
    hpicfPsGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDcPsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDcPsCompliance.setStatus(
        "deprecated"
    )

hpicfXpsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfXpsCompliance.setStatus(
        "current"
    )

hpicfXpsZoneCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfXpsZoneCompliance.setStatus(
        "current"
    )

hpicfDcPsCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfDcPsCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POWERSUPPLY-MIB",
    **{"HpicfDcPsIndex": HpicfDcPsIndex,
       "HpicfDcPsState": HpicfDcPsState,
       "HpicfXpsConnectionStatus": HpicfXpsConnectionStatus,
       "HpicfXpsZoneStatus": HpicfXpsZoneStatus,
       "hpicfPsMIB": hpicfPsMIB,
       "hpicfEntityPs": hpicfEntityPs,
       "hpicfPsTable": hpicfPsTable,
       "hpicfPsEntry": hpicfPsEntry,
       "hpicfPsBayNum": hpicfPsBayNum,
       "hpicfPsState": hpicfPsState,
       "hpicfPsFailures": hpicfPsFailures,
       "hpicfPsTemp": hpicfPsTemp,
       "hpicfPsVoltageInfo": hpicfPsVoltageInfo,
       "hpicfPsWattageCur": hpicfPsWattageCur,
       "hpicfPsWattageMax": hpicfPsWattageMax,
       "hpicfPsLastCall": hpicfPsLastCall,
       "hpicfPsModel": hpicfPsModel,
       "hpicfXpsTable": hpicfXpsTable,
       "hpicfXpsEntry": hpicfXpsEntry,
       "hpicfXpsConnectingPort": hpicfXpsConnectingPort,
       "hpicfXpsPortOperStatus": hpicfXpsPortOperStatus,
       "hpicfXpsSwitchSerialNo": hpicfXpsSwitchSerialNo,
       "hpicfXpsConnectionState": hpicfXpsConnectionState,
       "hpicfXpsSysName": hpicfXpsSysName,
       "hpicfXpsMACAddress": hpicfXpsMACAddress,
       "hpicfXpsSwitchOSVersion": hpicfXpsSwitchOSVersion,
       "hpicfXpsSwitchIpsVoltage": hpicfXpsSwitchIpsVoltage,
       "hpicfXpsSwitchIpsWattage": hpicfXpsSwitchIpsWattage,
       "hpicfXpsPower": hpicfXpsPower,
       "hpicfXpsSupportedCableVersion": hpicfXpsSupportedCableVersion,
       "hpicfXpsSupportedZoneVersion": hpicfXpsSupportedZoneVersion,
       "hpicfXpsSwitchModType": hpicfXpsSwitchModType,
       "hpicfXpsSwitchConfigTable": hpicfXpsSwitchConfigTable,
       "hpicfXpsSwitchConfigEntry": hpicfXpsSwitchConfigEntry,
       "hpicfXpsSwitchAdminStatus": hpicfXpsSwitchAdminStatus,
       "hpicfXpsSwitchAutoRecovery": hpicfXpsSwitchAutoRecovery,
       "hpicfXpsAllowPortsSupported": hpicfXpsAllowPortsSupported,
       "hpicfXpsReset": hpicfXpsReset,
       "hpicfXpsType": hpicfXpsType,
       "hpicfXpsSerialNum": hpicfXpsSerialNum,
       "hpicfXpsModuleName": hpicfXpsModuleName,
       "hpicfXpsPowerShareReqStatus": hpicfXpsPowerShareReqStatus,
       "hpicfXpsResetReqStatus": hpicfXpsResetReqStatus,
       "hpicfXpsZoneTable": hpicfXpsZoneTable,
       "hpicfXpsZoneEntry": hpicfXpsZoneEntry,
       "hpicfXpsZoneNo": hpicfXpsZoneNo,
       "hpicfXpsZoneState": hpicfXpsZoneState,
       "hpicfXpsZonePowerShareMap": hpicfXpsZonePowerShareMap,
       "hpicfXpsZoneVoltage": hpicfXpsZoneVoltage,
       "hpicfXpsZoneWattage": hpicfXpsZoneWattage,
       "hpicfXpsPSURev": hpicfXpsPSURev,
       "hpicfXpsPSUModule": hpicfXpsPSUModule,
       "hpicfXpsZonePowerShareForce": hpicfXpsZonePowerShareForce,
       "hpicfXpsZoneRecordVersion": hpicfXpsZoneRecordVersion,
       "hpicfPsConformance": hpicfPsConformance,
       "hpicfPsCompliance": hpicfPsCompliance,
       "hpicfDcPsCompliance": hpicfDcPsCompliance,
       "hpicfXpsCompliance": hpicfXpsCompliance,
       "hpicfXpsZoneCompliance": hpicfXpsZoneCompliance,
       "hpicfDcPsCompliance1": hpicfDcPsCompliance1,
       "hpicfPsGroups": hpicfPsGroups,
       "hpicfPsGroup": hpicfPsGroup,
       "hpicfXpsGroup": hpicfXpsGroup,
       "hpicfXpsZoneGroup": hpicfXpsZoneGroup,
       "hpicfPsGroup1": hpicfPsGroup1}
)
