# SNMP MIB module (REDLINE-BS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDLINE-BS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:29 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(redlineSystem,) = mibBuilder.importSymbols(
    "REDLINE-MIB",
    "redlineSystem")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

redlineBsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2)
)
redlineBsMib.setRevisions(
        ("2005-10-28 15:43",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RedlineBsDhcpObjects_ObjectIdentity = ObjectIdentity
redlineBsDhcpObjects = _RedlineBsDhcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 1)
)


class _RedlineBsIpAddressSource_Type(Integer32):
    """Custom type redlineBsIpAddressSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2))
    )


_RedlineBsIpAddressSource_Type.__name__ = "Integer32"
_RedlineBsIpAddressSource_Object = MibScalar
redlineBsIpAddressSource = _RedlineBsIpAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 1, 1),
    _RedlineBsIpAddressSource_Type()
)
redlineBsIpAddressSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsIpAddressSource.setStatus("current")


class _RedlineBsDhcpPacketsRelay_Type(Integer32):
    """Custom type redlineBsDhcpPacketsRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRelay", 2),
          ("relay", 1))
    )


_RedlineBsDhcpPacketsRelay_Type.__name__ = "Integer32"
_RedlineBsDhcpPacketsRelay_Object = MibScalar
redlineBsDhcpPacketsRelay = _RedlineBsDhcpPacketsRelay_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 1, 2),
    _RedlineBsDhcpPacketsRelay_Type()
)
redlineBsDhcpPacketsRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsDhcpPacketsRelay.setStatus("current")
_RedlineBsSntpObjects_ObjectIdentity = ObjectIdentity
redlineBsSntpObjects = _RedlineBsSntpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 2)
)


class _RedlineBsRefreshTime_Type(Integer32):
    """Custom type redlineBsRefreshTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("refresh", 2))
    )


_RedlineBsRefreshTime_Type.__name__ = "Integer32"
_RedlineBsRefreshTime_Object = MibScalar
redlineBsRefreshTime = _RedlineBsRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 2, 1),
    _RedlineBsRefreshTime_Type()
)
redlineBsRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsRefreshTime.setStatus("current")


class _RedlineBsDayLightSaving_Type(Integer32):
    """Custom type redlineBsDayLightSaving based on Integer32"""
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


_RedlineBsDayLightSaving_Type.__name__ = "Integer32"
_RedlineBsDayLightSaving_Object = MibScalar
redlineBsDayLightSaving = _RedlineBsDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 2, 2),
    _RedlineBsDayLightSaving_Type()
)
redlineBsDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsDayLightSaving.setStatus("current")
_RedlineBsTimezone_Type = Integer32
_RedlineBsTimezone_Object = MibScalar
redlineBsTimezone = _RedlineBsTimezone_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 2, 3),
    _RedlineBsTimezone_Type()
)
redlineBsTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsTimezone.setStatus("current")


class _RedlineBsTimeServerIpAddressType_Type(InetAddressType):
    """Custom type redlineBsTimeServerIpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_RedlineBsTimeServerIpAddressType_Type.__name__ = "InetAddressType"
_RedlineBsTimeServerIpAddressType_Object = MibScalar
redlineBsTimeServerIpAddressType = _RedlineBsTimeServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 2, 4),
    _RedlineBsTimeServerIpAddressType_Type()
)
redlineBsTimeServerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsTimeServerIpAddressType.setStatus("current")
_RedlineBsTimeServerIpAddress_Type = InetAddress
_RedlineBsTimeServerIpAddress_Object = MibScalar
redlineBsTimeServerIpAddress = _RedlineBsTimeServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 2, 5),
    _RedlineBsTimeServerIpAddress_Type()
)
redlineBsTimeServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsTimeServerIpAddress.setStatus("current")
_RedlineBsTimezoneMin_Type = Integer32
_RedlineBsTimezoneMin_Object = MibScalar
redlineBsTimezoneMin = _RedlineBsTimezoneMin_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 2, 6),
    _RedlineBsTimezoneMin_Type()
)
redlineBsTimezoneMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsTimezoneMin.setStatus("current")
_RedlineBsConfigSaveObjects_ObjectIdentity = ObjectIdentity
redlineBsConfigSaveObjects = _RedlineBsConfigSaveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 3)
)


class _RedlineBsSnmpConfigSave_Type(Integer32):
    """Custom type redlineBsSnmpConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("save", 2))
    )


_RedlineBsSnmpConfigSave_Type.__name__ = "Integer32"
_RedlineBsSnmpConfigSave_Object = MibScalar
redlineBsSnmpConfigSave = _RedlineBsSnmpConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 3, 1),
    _RedlineBsSnmpConfigSave_Type()
)
redlineBsSnmpConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsSnmpConfigSave.setStatus("current")


class _RedlineBsSfConfigSave_Type(Integer32):
    """Custom type redlineBsSfConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("save", 2))
    )


_RedlineBsSfConfigSave_Type.__name__ = "Integer32"
_RedlineBsSfConfigSave_Object = MibScalar
redlineBsSfConfigSave = _RedlineBsSfConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 3, 2),
    _RedlineBsSfConfigSave_Type()
)
redlineBsSfConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsSfConfigSave.setStatus("current")
_RedlineBsSystemObjects_ObjectIdentity = ObjectIdentity
redlineBsSystemObjects = _RedlineBsSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 4)
)


class _RedlineBsRadioType_Type(OctetString):
    """Custom type redlineBsRadioType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RedlineBsRadioType_Type.__name__ = "OctetString"
_RedlineBsRadioType_Object = MibScalar
redlineBsRadioType = _RedlineBsRadioType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 4, 1),
    _RedlineBsRadioType_Type()
)
redlineBsRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsRadioType.setStatus("current")
_RedlineBsRfObjects_ObjectIdentity = ObjectIdentity
redlineBsRfObjects = _RedlineBsRfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 5)
)
_RedlineBsDownlinkChanFreq_Type = Unsigned32
_RedlineBsDownlinkChanFreq_Object = MibScalar
redlineBsDownlinkChanFreq = _RedlineBsDownlinkChanFreq_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 5, 1),
    _RedlineBsDownlinkChanFreq_Type()
)
redlineBsDownlinkChanFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsDownlinkChanFreq.setStatus("current")
if mibBuilder.loadTexts:
    redlineBsDownlinkChanFreq.setUnits("kHz")
_RedlineBsUplinkChanFreq_Type = Unsigned32
_RedlineBsUplinkChanFreq_Object = MibScalar
redlineBsUplinkChanFreq = _RedlineBsUplinkChanFreq_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 5, 2),
    _RedlineBsUplinkChanFreq_Type()
)
redlineBsUplinkChanFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsUplinkChanFreq.setStatus("current")
if mibBuilder.loadTexts:
    redlineBsUplinkChanFreq.setUnits("kHz")
_RedlineBsPhyObjects_ObjectIdentity = ObjectIdentity
redlineBsPhyObjects = _RedlineBsPhyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 6)
)
_RedlineBsChannelSize_Type = Unsigned32
_RedlineBsChannelSize_Object = MibScalar
redlineBsChannelSize = _RedlineBsChannelSize_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 6, 1),
    _RedlineBsChannelSize_Type()
)
redlineBsChannelSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsChannelSize.setStatus("current")
if mibBuilder.loadTexts:
    redlineBsChannelSize.setUnits("KHz")
_RedlineBsEthObjects_ObjectIdentity = ObjectIdentity
redlineBsEthObjects = _RedlineBsEthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 7)
)


class _RedlineBsManagementAccess_Type(Integer32):
    """Custom type redlineBsManagementAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataPort", 1),
          ("mgtPort", 2))
    )


_RedlineBsManagementAccess_Type.__name__ = "Integer32"
_RedlineBsManagementAccess_Object = MibScalar
redlineBsManagementAccess = _RedlineBsManagementAccess_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 7, 1),
    _RedlineBsManagementAccess_Type()
)
redlineBsManagementAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsManagementAccess.setStatus("current")


class _RedlineBsDataPortSettings_Type(Integer32):
    """Custom type redlineBsDataPortSettings based on Integer32"""
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
        *(("autoDetect", 1),
          ("fullDuplex10", 3),
          ("fullDuplex100", 2),
          ("halfDuplex10", 5),
          ("halfDuplex100", 4))
    )


_RedlineBsDataPortSettings_Type.__name__ = "Integer32"
_RedlineBsDataPortSettings_Object = MibScalar
redlineBsDataPortSettings = _RedlineBsDataPortSettings_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 7, 2),
    _RedlineBsDataPortSettings_Type()
)
redlineBsDataPortSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsDataPortSettings.setStatus("current")


class _RedlineBsMgtPortSettings_Type(Integer32):
    """Custom type redlineBsMgtPortSettings based on Integer32"""
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
        *(("autoDetect", 1),
          ("fullDuplex10", 3),
          ("fullDuplex100", 2),
          ("halfDuplex10", 5),
          ("halfDuplex100", 4))
    )


_RedlineBsMgtPortSettings_Type.__name__ = "Integer32"
_RedlineBsMgtPortSettings_Object = MibScalar
redlineBsMgtPortSettings = _RedlineBsMgtPortSettings_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 7, 3),
    _RedlineBsMgtPortSettings_Type()
)
redlineBsMgtPortSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsMgtPortSettings.setStatus("current")
_RedlineBsVlanObjects_ObjectIdentity = ObjectIdentity
redlineBsVlanObjects = _RedlineBsVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 8)
)


class _RedlineBsVlanTrafficTagging_Type(Integer32):
    """Custom type redlineBsVlanTrafficTagging based on Integer32"""
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


_RedlineBsVlanTrafficTagging_Type.__name__ = "Integer32"
_RedlineBsVlanTrafficTagging_Object = MibScalar
redlineBsVlanTrafficTagging = _RedlineBsVlanTrafficTagging_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 8, 1),
    _RedlineBsVlanTrafficTagging_Type()
)
redlineBsVlanTrafficTagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsVlanTrafficTagging.setStatus("current")
_RedlineBsVlanId_Type = Unsigned32
_RedlineBsVlanId_Object = MibScalar
redlineBsVlanId = _RedlineBsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 8, 2),
    _RedlineBsVlanId_Type()
)
redlineBsVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsVlanId.setStatus("current")
_RedlineBsSmcObjects_ObjectIdentity = ObjectIdentity
redlineBsSmcObjects = _RedlineBsSmcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 9)
)


class _RedlineBsSmcCurrentOperMode_Type(Integer32):
    """Custom type redlineBsSmcCurrentOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maintenance", 2),
          ("normal", 1))
    )


_RedlineBsSmcCurrentOperMode_Type.__name__ = "Integer32"
_RedlineBsSmcCurrentOperMode_Object = MibScalar
redlineBsSmcCurrentOperMode = _RedlineBsSmcCurrentOperMode_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 9, 1),
    _RedlineBsSmcCurrentOperMode_Type()
)
redlineBsSmcCurrentOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redlineBsSmcCurrentOperMode.setStatus("current")
_RedlineBsPowerSupplyAndCoolingObjects_ObjectIdentity = ObjectIdentity
redlineBsPowerSupplyAndCoolingObjects = _RedlineBsPowerSupplyAndCoolingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10)
)
_RedlineBsPowerSupplyTable_Object = MibTable
redlineBsPowerSupplyTable = _RedlineBsPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    redlineBsPowerSupplyTable.setStatus("current")
_RedlineBsPowerSupplyEntry_Object = MibTableRow
redlineBsPowerSupplyEntry = _RedlineBsPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 1, 1)
)
redlineBsPowerSupplyEntry.setIndexNames(
    (0, "REDLINE-BS-MIB", "redlineBsPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    redlineBsPowerSupplyEntry.setStatus("current")
_RedlineBsPowerSupplyIndex_Type = Integer32
_RedlineBsPowerSupplyIndex_Object = MibTableColumn
redlineBsPowerSupplyIndex = _RedlineBsPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 1, 1, 1),
    _RedlineBsPowerSupplyIndex_Type()
)
redlineBsPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineBsPowerSupplyIndex.setStatus("current")


class _RedlineBsPowerSupplyName_Type(DisplayString):
    """Custom type redlineBsPowerSupplyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineBsPowerSupplyName_Type.__name__ = "DisplayString"
_RedlineBsPowerSupplyName_Object = MibTableColumn
redlineBsPowerSupplyName = _RedlineBsPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 1, 1, 2),
    _RedlineBsPowerSupplyName_Type()
)
redlineBsPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsPowerSupplyName.setStatus("current")


class _RedlineBsPowerSupplyType_Type(Integer32):
    """Custom type redlineBsPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("externalShared", 3),
          ("internal", 1))
    )


_RedlineBsPowerSupplyType_Type.__name__ = "Integer32"
_RedlineBsPowerSupplyType_Object = MibTableColumn
redlineBsPowerSupplyType = _RedlineBsPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 1, 1, 3),
    _RedlineBsPowerSupplyType_Type()
)
redlineBsPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsPowerSupplyType.setStatus("current")


class _RedlineBsPowerSupplyStatus_Type(Integer32):
    """Custom type redlineBsPowerSupplyStatus based on Integer32"""
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


_RedlineBsPowerSupplyStatus_Type.__name__ = "Integer32"
_RedlineBsPowerSupplyStatus_Object = MibTableColumn
redlineBsPowerSupplyStatus = _RedlineBsPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 1, 1, 4),
    _RedlineBsPowerSupplyStatus_Type()
)
redlineBsPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsPowerSupplyStatus.setStatus("current")
_RedlineBsTemperatureTable_Object = MibTable
redlineBsTemperatureTable = _RedlineBsTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    redlineBsTemperatureTable.setStatus("current")
_RedlineBsTemperatureEntry_Object = MibTableRow
redlineBsTemperatureEntry = _RedlineBsTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 2, 1)
)
redlineBsTemperatureEntry.setIndexNames(
    (0, "REDLINE-BS-MIB", "redlineBsUnitIndex"),
)
if mibBuilder.loadTexts:
    redlineBsTemperatureEntry.setStatus("current")
_RedlineBsUnitIndex_Type = Integer32
_RedlineBsUnitIndex_Object = MibTableColumn
redlineBsUnitIndex = _RedlineBsUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 2, 1, 1),
    _RedlineBsUnitIndex_Type()
)
redlineBsUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineBsUnitIndex.setStatus("current")


class _RedlineBsUnitName_Type(DisplayString):
    """Custom type redlineBsUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineBsUnitName_Type.__name__ = "DisplayString"
_RedlineBsUnitName_Object = MibTableColumn
redlineBsUnitName = _RedlineBsUnitName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 2, 1, 2),
    _RedlineBsUnitName_Type()
)
redlineBsUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsUnitName.setStatus("current")


class _RedlineBsUnitType_Type(Integer32):
    """Custom type redlineBsUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_RedlineBsUnitType_Type.__name__ = "Integer32"
_RedlineBsUnitType_Object = MibTableColumn
redlineBsUnitType = _RedlineBsUnitType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 2, 1, 3),
    _RedlineBsUnitType_Type()
)
redlineBsUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsUnitType.setStatus("current")


class _RedlineBsCurrTemperature_Type(Integer32):
    """Custom type redlineBsCurrTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 100),
    )


_RedlineBsCurrTemperature_Type.__name__ = "Integer32"
_RedlineBsCurrTemperature_Object = MibTableColumn
redlineBsCurrTemperature = _RedlineBsCurrTemperature_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 2, 1, 4),
    _RedlineBsCurrTemperature_Type()
)
redlineBsCurrTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsCurrTemperature.setStatus("current")
if mibBuilder.loadTexts:
    redlineBsCurrTemperature.setUnits("degrees Celsius")
_RedlineBsTempThresholdTable_Object = MibTable
redlineBsTempThresholdTable = _RedlineBsTempThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 3)
)
if mibBuilder.loadTexts:
    redlineBsTempThresholdTable.setStatus("current")
_RedlineBsTempThresholdEntry_Object = MibTableRow
redlineBsTempThresholdEntry = _RedlineBsTempThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 3, 1)
)
redlineBsTempThresholdEntry.setIndexNames(
    (0, "REDLINE-BS-MIB", "redlineBsUnitIndex"),
    (0, "REDLINE-BS-MIB", "redlineBsTempThresholdIndex"),
)
if mibBuilder.loadTexts:
    redlineBsTempThresholdEntry.setStatus("current")
_RedlineBsTempThresholdIndex_Type = Integer32
_RedlineBsTempThresholdIndex_Object = MibTableColumn
redlineBsTempThresholdIndex = _RedlineBsTempThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 3, 1, 1),
    _RedlineBsTempThresholdIndex_Type()
)
redlineBsTempThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineBsTempThresholdIndex.setStatus("current")


class _RedlineBsTempTrapThreshold_Type(Integer32):
    """Custom type redlineBsTempTrapThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 100),
    )


_RedlineBsTempTrapThreshold_Type.__name__ = "Integer32"
_RedlineBsTempTrapThreshold_Object = MibTableColumn
redlineBsTempTrapThreshold = _RedlineBsTempTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 3, 1, 2),
    _RedlineBsTempTrapThreshold_Type()
)
redlineBsTempTrapThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsTempTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    redlineBsTempTrapThreshold.setUnits("degrees Celsius")


class _RedlineBsTempTrapClrThreshold_Type(Integer32):
    """Custom type redlineBsTempTrapClrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 100),
    )


_RedlineBsTempTrapClrThreshold_Type.__name__ = "Integer32"
_RedlineBsTempTrapClrThreshold_Object = MibTableColumn
redlineBsTempTrapClrThreshold = _RedlineBsTempTrapClrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 3, 1, 3),
    _RedlineBsTempTrapClrThreshold_Type()
)
redlineBsTempTrapClrThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsTempTrapClrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    redlineBsTempTrapClrThreshold.setUnits("degrees Celsius")


class _RedlineBsTempThresholdName_Type(DisplayString):
    """Custom type redlineBsTempThresholdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineBsTempThresholdName_Type.__name__ = "DisplayString"
_RedlineBsTempThresholdName_Object = MibTableColumn
redlineBsTempThresholdName = _RedlineBsTempThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 3, 1, 4),
    _RedlineBsTempThresholdName_Type()
)
redlineBsTempThresholdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsTempThresholdName.setStatus("current")


class _RedlineBsTemperatureTrapTrigger_Type(Integer32):
    """Custom type redlineBsTemperatureTrapTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temperatureFalling", 2),
          ("temperatureRising", 1))
    )


_RedlineBsTemperatureTrapTrigger_Type.__name__ = "Integer32"
_RedlineBsTemperatureTrapTrigger_Object = MibTableColumn
redlineBsTemperatureTrapTrigger = _RedlineBsTemperatureTrapTrigger_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 3, 1, 5),
    _RedlineBsTemperatureTrapTrigger_Type()
)
redlineBsTemperatureTrapTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsTemperatureTrapTrigger.setStatus("current")
_RedlineBsFanTable_Object = MibTable
redlineBsFanTable = _RedlineBsFanTable_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 4)
)
if mibBuilder.loadTexts:
    redlineBsFanTable.setStatus("current")
_RedlineBsFanEntry_Object = MibTableRow
redlineBsFanEntry = _RedlineBsFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 4, 1)
)
redlineBsFanEntry.setIndexNames(
    (0, "REDLINE-BS-MIB", "redlineBsFanIndex"),
)
if mibBuilder.loadTexts:
    redlineBsFanEntry.setStatus("current")
_RedlineBsFanIndex_Type = Integer32
_RedlineBsFanIndex_Object = MibTableColumn
redlineBsFanIndex = _RedlineBsFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 4, 1, 1),
    _RedlineBsFanIndex_Type()
)
redlineBsFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    redlineBsFanIndex.setStatus("current")


class _RedlineBsFanName_Type(DisplayString):
    """Custom type redlineBsFanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RedlineBsFanName_Type.__name__ = "DisplayString"
_RedlineBsFanName_Object = MibTableColumn
redlineBsFanName = _RedlineBsFanName_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 4, 1, 2),
    _RedlineBsFanName_Type()
)
redlineBsFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsFanName.setStatus("current")


class _RedlineBsFanStatus_Type(Integer32):
    """Custom type redlineBsFanStatus based on Integer32"""
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


_RedlineBsFanStatus_Type.__name__ = "Integer32"
_RedlineBsFanStatus_Object = MibTableColumn
redlineBsFanStatus = _RedlineBsFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 10, 4, 1, 3),
    _RedlineBsFanStatus_Type()
)
redlineBsFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redlineBsFanStatus.setStatus("current")
_RedlineBsNotificationObjects_ObjectIdentity = ObjectIdentity
redlineBsNotificationObjects = _RedlineBsNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 11)
)
_RedlineBsTrapDefinitions_ObjectIdentity = ObjectIdentity
redlineBsTrapDefinitions = _RedlineBsTrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 11, 0)
)
_RedlineBsTrapMibObjects_ObjectIdentity = ObjectIdentity
redlineBsTrapMibObjects = _RedlineBsTrapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 11, 1)
)


class _RedlineBsTrapType_Type(Integer32):
    """Custom type redlineBsTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapClr", 2),
          ("trapSet", 1))
    )


_RedlineBsTrapType_Type.__name__ = "Integer32"
_RedlineBsTrapType_Object = MibScalar
redlineBsTrapType = _RedlineBsTrapType_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 11, 1, 1),
    _RedlineBsTrapType_Type()
)
redlineBsTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    redlineBsTrapType.setStatus("current")
_RedlineBsTrapPowerSupplyIndex_Type = Integer32
_RedlineBsTrapPowerSupplyIndex_Object = MibScalar
redlineBsTrapPowerSupplyIndex = _RedlineBsTrapPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 11, 1, 2),
    _RedlineBsTrapPowerSupplyIndex_Type()
)
redlineBsTrapPowerSupplyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    redlineBsTrapPowerSupplyIndex.setStatus("current")
_RedlineBsTrapUnitIndex_Type = Integer32
_RedlineBsTrapUnitIndex_Object = MibScalar
redlineBsTrapUnitIndex = _RedlineBsTrapUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 11, 1, 3),
    _RedlineBsTrapUnitIndex_Type()
)
redlineBsTrapUnitIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    redlineBsTrapUnitIndex.setStatus("current")
_RedlineBsTrapTempThresholdIndex_Type = Integer32
_RedlineBsTrapTempThresholdIndex_Object = MibScalar
redlineBsTrapTempThresholdIndex = _RedlineBsTrapTempThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 11, 1, 4),
    _RedlineBsTrapTempThresholdIndex_Type()
)
redlineBsTrapTempThresholdIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    redlineBsTrapTempThresholdIndex.setStatus("current")
_RedlineBsConformance_ObjectIdentity = ObjectIdentity
redlineBsConformance = _RedlineBsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12)
)
_RedlineBsGroups_ObjectIdentity = ObjectIdentity
redlineBsGroups = _RedlineBsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1)
)
_RedlineBsCompls_ObjectIdentity = ObjectIdentity
redlineBsCompls = _RedlineBsCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 2)
)

# Managed Objects groups

redlineBsDhcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 1)
)
redlineBsDhcpGroup.setObjects(
      *(("REDLINE-BS-MIB", "redlineBsIpAddressSource"),
        ("REDLINE-BS-MIB", "redlineBsDhcpPacketsRelay"))
)
if mibBuilder.loadTexts:
    redlineBsDhcpGroup.setStatus("current")

redlineBsSntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 2)
)
redlineBsSntpGroup.setObjects(
      *(("REDLINE-BS-MIB", "redlineBsRefreshTime"),
        ("REDLINE-BS-MIB", "redlineBsDayLightSaving"),
        ("REDLINE-BS-MIB", "redlineBsTimezone"),
        ("REDLINE-BS-MIB", "redlineBsTimeServerIpAddressType"),
        ("REDLINE-BS-MIB", "redlineBsTimeServerIpAddress"),
        ("REDLINE-BS-MIB", "redlineBsTimezoneMin"))
)
if mibBuilder.loadTexts:
    redlineBsSntpGroup.setStatus("current")

redlineBsConfigSaveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 3)
)
redlineBsConfigSaveGroup.setObjects(
      *(("REDLINE-BS-MIB", "redlineBsSnmpConfigSave"),
        ("REDLINE-BS-MIB", "redlineBsSfConfigSave"))
)
if mibBuilder.loadTexts:
    redlineBsConfigSaveGroup.setStatus("current")

redlineBsSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 4)
)
redlineBsSystemGroup.setObjects(
    ("REDLINE-BS-MIB", "redlineBsRadioType")
)
if mibBuilder.loadTexts:
    redlineBsSystemGroup.setStatus("current")

redlineBsRfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 5)
)
redlineBsRfGroup.setObjects(
      *(("REDLINE-BS-MIB", "redlineBsDownlinkChanFreq"),
        ("REDLINE-BS-MIB", "redlineBsUplinkChanFreq"))
)
if mibBuilder.loadTexts:
    redlineBsRfGroup.setStatus("current")

redlineBsPhyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 6)
)
redlineBsPhyGroup.setObjects(
    ("REDLINE-BS-MIB", "redlineBsChannelSize")
)
if mibBuilder.loadTexts:
    redlineBsPhyGroup.setStatus("current")

redlineBsEthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 7)
)
redlineBsEthGroup.setObjects(
      *(("REDLINE-BS-MIB", "redlineBsManagementAccess"),
        ("REDLINE-BS-MIB", "redlineBsDataPortSettings"))
)
if mibBuilder.loadTexts:
    redlineBsEthGroup.setStatus("current")

redlineBsVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 8)
)
redlineBsVlanGroup.setObjects(
      *(("REDLINE-BS-MIB", "redlineBsVlanTrafficTagging"),
        ("REDLINE-BS-MIB", "redlineBsVlanId"))
)
if mibBuilder.loadTexts:
    redlineBsVlanGroup.setStatus("current")

redlineBsSmcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 9)
)
redlineBsSmcGroup.setObjects(
    ("REDLINE-BS-MIB", "redlineBsSmcCurrentOperMode")
)
if mibBuilder.loadTexts:
    redlineBsSmcGroup.setStatus("current")

redlineBsPowerSupplyAndCoolingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 10)
)
redlineBsPowerSupplyAndCoolingGroup.setObjects(
      *(("REDLINE-BS-MIB", "redlineBsPowerSupplyName"),
        ("REDLINE-BS-MIB", "redlineBsPowerSupplyType"),
        ("REDLINE-BS-MIB", "redlineBsPowerSupplyStatus"),
        ("REDLINE-BS-MIB", "redlineBsUnitName"),
        ("REDLINE-BS-MIB", "redlineBsUnitType"),
        ("REDLINE-BS-MIB", "redlineBsCurrTemperature"),
        ("REDLINE-BS-MIB", "redlineBsTempTrapThreshold"),
        ("REDLINE-BS-MIB", "redlineBsTempTrapClrThreshold"),
        ("REDLINE-BS-MIB", "redlineBsTempThresholdName"),
        ("REDLINE-BS-MIB", "redlineBsTemperatureTrapTrigger"),
        ("REDLINE-BS-MIB", "redlineBsFanName"),
        ("REDLINE-BS-MIB", "redlineBsFanStatus"),
        ("REDLINE-BS-MIB", "redlineBsTrapType"))
)
if mibBuilder.loadTexts:
    redlineBsPowerSupplyAndCoolingGroup.setStatus("current")


# Notification objects

redlineBsPowerSupplyStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 11, 0, 1)
)
redlineBsPowerSupplyStatusTrap.setObjects(
      *(("REDLINE-BS-MIB", "redlineBsTrapPowerSupplyIndex"),
        ("REDLINE-BS-MIB", "redlineBsPowerSupplyStatus"))
)
if mibBuilder.loadTexts:
    redlineBsPowerSupplyStatusTrap.setStatus(
        "current"
    )

redlineBsTempThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 11, 0, 2)
)
redlineBsTempThresholdTrap.setObjects(
      *(("REDLINE-BS-MIB", "redlineBsTrapUnitIndex"),
        ("REDLINE-BS-MIB", "redlineBsTrapTempThresholdIndex"),
        ("REDLINE-BS-MIB", "redlineBsCurrTemperature"),
        ("REDLINE-BS-MIB", "redlineBsTemperatureTrapTrigger"),
        ("REDLINE-BS-MIB", "redlineBsTrapType"))
)
if mibBuilder.loadTexts:
    redlineBsTempThresholdTrap.setStatus(
        "current"
    )


# Notifications groups

redlineBsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 1, 11)
)
redlineBsNotificationGroup.setObjects(
      *(("REDLINE-BS-MIB", "redlineBsPowerSupplyStatusTrap"),
        ("REDLINE-BS-MIB", "redlineBsTempThresholdTrap"))
)
if mibBuilder.loadTexts:
    redlineBsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

redlineBsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    redlineBsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDLINE-BS-MIB",
    **{"redlineBsMib": redlineBsMib,
       "redlineBsDhcpObjects": redlineBsDhcpObjects,
       "redlineBsIpAddressSource": redlineBsIpAddressSource,
       "redlineBsDhcpPacketsRelay": redlineBsDhcpPacketsRelay,
       "redlineBsSntpObjects": redlineBsSntpObjects,
       "redlineBsRefreshTime": redlineBsRefreshTime,
       "redlineBsDayLightSaving": redlineBsDayLightSaving,
       "redlineBsTimezone": redlineBsTimezone,
       "redlineBsTimeServerIpAddressType": redlineBsTimeServerIpAddressType,
       "redlineBsTimeServerIpAddress": redlineBsTimeServerIpAddress,
       "redlineBsTimezoneMin": redlineBsTimezoneMin,
       "redlineBsConfigSaveObjects": redlineBsConfigSaveObjects,
       "redlineBsSnmpConfigSave": redlineBsSnmpConfigSave,
       "redlineBsSfConfigSave": redlineBsSfConfigSave,
       "redlineBsSystemObjects": redlineBsSystemObjects,
       "redlineBsRadioType": redlineBsRadioType,
       "redlineBsRfObjects": redlineBsRfObjects,
       "redlineBsDownlinkChanFreq": redlineBsDownlinkChanFreq,
       "redlineBsUplinkChanFreq": redlineBsUplinkChanFreq,
       "redlineBsPhyObjects": redlineBsPhyObjects,
       "redlineBsChannelSize": redlineBsChannelSize,
       "redlineBsEthObjects": redlineBsEthObjects,
       "redlineBsManagementAccess": redlineBsManagementAccess,
       "redlineBsDataPortSettings": redlineBsDataPortSettings,
       "redlineBsMgtPortSettings": redlineBsMgtPortSettings,
       "redlineBsVlanObjects": redlineBsVlanObjects,
       "redlineBsVlanTrafficTagging": redlineBsVlanTrafficTagging,
       "redlineBsVlanId": redlineBsVlanId,
       "redlineBsSmcObjects": redlineBsSmcObjects,
       "redlineBsSmcCurrentOperMode": redlineBsSmcCurrentOperMode,
       "redlineBsPowerSupplyAndCoolingObjects": redlineBsPowerSupplyAndCoolingObjects,
       "redlineBsPowerSupplyTable": redlineBsPowerSupplyTable,
       "redlineBsPowerSupplyEntry": redlineBsPowerSupplyEntry,
       "redlineBsPowerSupplyIndex": redlineBsPowerSupplyIndex,
       "redlineBsPowerSupplyName": redlineBsPowerSupplyName,
       "redlineBsPowerSupplyType": redlineBsPowerSupplyType,
       "redlineBsPowerSupplyStatus": redlineBsPowerSupplyStatus,
       "redlineBsTemperatureTable": redlineBsTemperatureTable,
       "redlineBsTemperatureEntry": redlineBsTemperatureEntry,
       "redlineBsUnitIndex": redlineBsUnitIndex,
       "redlineBsUnitName": redlineBsUnitName,
       "redlineBsUnitType": redlineBsUnitType,
       "redlineBsCurrTemperature": redlineBsCurrTemperature,
       "redlineBsTempThresholdTable": redlineBsTempThresholdTable,
       "redlineBsTempThresholdEntry": redlineBsTempThresholdEntry,
       "redlineBsTempThresholdIndex": redlineBsTempThresholdIndex,
       "redlineBsTempTrapThreshold": redlineBsTempTrapThreshold,
       "redlineBsTempTrapClrThreshold": redlineBsTempTrapClrThreshold,
       "redlineBsTempThresholdName": redlineBsTempThresholdName,
       "redlineBsTemperatureTrapTrigger": redlineBsTemperatureTrapTrigger,
       "redlineBsFanTable": redlineBsFanTable,
       "redlineBsFanEntry": redlineBsFanEntry,
       "redlineBsFanIndex": redlineBsFanIndex,
       "redlineBsFanName": redlineBsFanName,
       "redlineBsFanStatus": redlineBsFanStatus,
       "redlineBsNotificationObjects": redlineBsNotificationObjects,
       "redlineBsTrapDefinitions": redlineBsTrapDefinitions,
       "redlineBsPowerSupplyStatusTrap": redlineBsPowerSupplyStatusTrap,
       "redlineBsTempThresholdTrap": redlineBsTempThresholdTrap,
       "redlineBsTrapMibObjects": redlineBsTrapMibObjects,
       "redlineBsTrapType": redlineBsTrapType,
       "redlineBsTrapPowerSupplyIndex": redlineBsTrapPowerSupplyIndex,
       "redlineBsTrapUnitIndex": redlineBsTrapUnitIndex,
       "redlineBsTrapTempThresholdIndex": redlineBsTrapTempThresholdIndex,
       "redlineBsConformance": redlineBsConformance,
       "redlineBsGroups": redlineBsGroups,
       "redlineBsDhcpGroup": redlineBsDhcpGroup,
       "redlineBsSntpGroup": redlineBsSntpGroup,
       "redlineBsConfigSaveGroup": redlineBsConfigSaveGroup,
       "redlineBsSystemGroup": redlineBsSystemGroup,
       "redlineBsRfGroup": redlineBsRfGroup,
       "redlineBsPhyGroup": redlineBsPhyGroup,
       "redlineBsEthGroup": redlineBsEthGroup,
       "redlineBsVlanGroup": redlineBsVlanGroup,
       "redlineBsSmcGroup": redlineBsSmcGroup,
       "redlineBsPowerSupplyAndCoolingGroup": redlineBsPowerSupplyAndCoolingGroup,
       "redlineBsNotificationGroup": redlineBsNotificationGroup,
       "redlineBsCompls": redlineBsCompls,
       "redlineBsCompliance": redlineBsCompliance}
)
