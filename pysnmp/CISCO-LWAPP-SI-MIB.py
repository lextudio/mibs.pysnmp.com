# SNMP MIB module (CISCO-LWAPP-SI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-SI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:00 2024
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

(cLApDot11IfSlotId,
 cLApName,
 cLApSysMacAddress,
 ciscoLwappSpectrum) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApDot11IfSlotId",
    "cLApName",
    "cLApSysMacAddress",
    "ciscoLwappSpectrum")

(CLDot11Band,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLDot11Band")

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

ciscoLwappSiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1)
)
ciscoLwappSiMIB.setRevisions(
        ("2015-05-18 00:00",
         "2011-10-01 00:00",
         "2011-05-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappSiMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappSiMIBNotifs = _CiscoLwappSiMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0)
)
_CiscoLwappSiMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappSiMIBObjects = _CiscoLwappSiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1)
)
_CiscoLwappAirQuality_ObjectIdentity = ObjectIdentity
ciscoLwappAirQuality = _CiscoLwappAirQuality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1)
)
_CLSiAqTable_Object = MibTable
cLSiAqTable = _CLSiAqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLSiAqTable.setStatus("current")
_CLSiAqEntry_Object = MibTableRow
cLSiAqEntry = _CLSiAqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1)
)
cLSiAqEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-SI-MIB", "cLSiAqChannelNumber"),
)
if mibBuilder.loadTexts:
    cLSiAqEntry.setStatus("current")


class _CLSiAqChannelNumber_Type(Unsigned32):
    """Custom type cLSiAqChannelNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CLSiAqChannelNumber_Type.__name__ = "Unsigned32"
_CLSiAqChannelNumber_Object = MibTableColumn
cLSiAqChannelNumber = _CLSiAqChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1, 1),
    _CLSiAqChannelNumber_Type()
)
cLSiAqChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSiAqChannelNumber.setStatus("current")


class _CLSiAqMinIndex_Type(Unsigned32):
    """Custom type cLSiAqMinIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLSiAqMinIndex_Type.__name__ = "Unsigned32"
_CLSiAqMinIndex_Object = MibTableColumn
cLSiAqMinIndex = _CLSiAqMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1, 2),
    _CLSiAqMinIndex_Type()
)
cLSiAqMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqMinIndex.setStatus("current")


class _CLSiAqIndex_Type(Unsigned32):
    """Custom type cLSiAqIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLSiAqIndex_Type.__name__ = "Unsigned32"
_CLSiAqIndex_Object = MibTableColumn
cLSiAqIndex = _CLSiAqIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1, 3),
    _CLSiAqIndex_Type()
)
cLSiAqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqIndex.setStatus("current")


class _CLSiAqTotalChannelPower_Type(Integer32):
    """Custom type cLSiAqTotalChannelPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_CLSiAqTotalChannelPower_Type.__name__ = "Integer32"
_CLSiAqTotalChannelPower_Object = MibTableColumn
cLSiAqTotalChannelPower = _CLSiAqTotalChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1, 4),
    _CLSiAqTotalChannelPower_Type()
)
cLSiAqTotalChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqTotalChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    cLSiAqTotalChannelPower.setUnits("dbm")


class _CLSiAqTotalChannelDutyCycle_Type(Unsigned32):
    """Custom type cLSiAqTotalChannelDutyCycle based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLSiAqTotalChannelDutyCycle_Type.__name__ = "Unsigned32"
_CLSiAqTotalChannelDutyCycle_Object = MibTableColumn
cLSiAqTotalChannelDutyCycle = _CLSiAqTotalChannelDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1, 5),
    _CLSiAqTotalChannelDutyCycle_Type()
)
cLSiAqTotalChannelDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqTotalChannelDutyCycle.setStatus("current")
if mibBuilder.loadTexts:
    cLSiAqTotalChannelDutyCycle.setUnits("percent")


class _CLSiAqInterferencePower_Type(Integer32):
    """Custom type cLSiAqInterferencePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_CLSiAqInterferencePower_Type.__name__ = "Integer32"
_CLSiAqInterferencePower_Object = MibTableColumn
cLSiAqInterferencePower = _CLSiAqInterferencePower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1, 6),
    _CLSiAqInterferencePower_Type()
)
cLSiAqInterferencePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqInterferencePower.setStatus("current")
if mibBuilder.loadTexts:
    cLSiAqInterferencePower.setUnits("dbm")


class _CLSiAqInterferenceDutyCycle_Type(Unsigned32):
    """Custom type cLSiAqInterferenceDutyCycle based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLSiAqInterferenceDutyCycle_Type.__name__ = "Unsigned32"
_CLSiAqInterferenceDutyCycle_Object = MibTableColumn
cLSiAqInterferenceDutyCycle = _CLSiAqInterferenceDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1, 7),
    _CLSiAqInterferenceDutyCycle_Type()
)
cLSiAqInterferenceDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqInterferenceDutyCycle.setStatus("current")
if mibBuilder.loadTexts:
    cLSiAqInterferenceDutyCycle.setUnits("percent")
_CLSiAqInterferenceDeviceCount_Type = Unsigned32
_CLSiAqInterferenceDeviceCount_Object = MibTableColumn
cLSiAqInterferenceDeviceCount = _CLSiAqInterferenceDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1, 8),
    _CLSiAqInterferenceDeviceCount_Type()
)
cLSiAqInterferenceDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqInterferenceDeviceCount.setStatus("current")


class _CLSiAqInterfererClassReportCount_Type(Unsigned32):
    """Custom type cLSiAqInterfererClassReportCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CLSiAqInterfererClassReportCount_Type.__name__ = "Unsigned32"
_CLSiAqInterfererClassReportCount_Object = MibTableColumn
cLSiAqInterfererClassReportCount = _CLSiAqInterfererClassReportCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1, 9),
    _CLSiAqInterfererClassReportCount_Type()
)
cLSiAqInterfererClassReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqInterfererClassReportCount.setStatus("current")
_CLSiAqTimeStamp_Type = Unsigned32
_CLSiAqTimeStamp_Object = MibTableColumn
cLSiAqTimeStamp = _CLSiAqTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 1, 1, 10),
    _CLSiAqTimeStamp_Type()
)
cLSiAqTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqTimeStamp.setStatus("current")
_CLSiAqInterferenceClassReportTable_Object = MibTable
cLSiAqInterferenceClassReportTable = _CLSiAqInterferenceClassReportTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportTable.setStatus("current")
_CLSiAqInterferenceClassReportEntry_Object = MibTableRow
cLSiAqInterferenceClassReportEntry = _CLSiAqInterferenceClassReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 2, 1)
)
cLSiAqInterferenceClassReportEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-SI-MIB", "cLSiAqChannelNumber"),
    (0, "CISCO-LWAPP-SI-MIB", "cLSiAqInterferenceClassReportIndex"),
)
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportEntry.setStatus("current")
_CLSiAqInterferenceClassReportIndex_Type = Unsigned32
_CLSiAqInterferenceClassReportIndex_Object = MibTableColumn
cLSiAqInterferenceClassReportIndex = _CLSiAqInterferenceClassReportIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 2, 1, 1),
    _CLSiAqInterferenceClassReportIndex_Type()
)
cLSiAqInterferenceClassReportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportIndex.setStatus("current")


class _CLSiAqInterferenceClassReportDeviceClass_Type(Integer32):
    """Custom type cLSiAqInterferenceClassReportDeviceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              10,
              17,
              18,
              19,
              25,
              26,
              27,
              28,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("bluetoothDiscovery", 17),
          ("bluetoothLink", 1),
          ("canopy", 34),
          ("continuousTransmitter", 25),
          ("dectLikePhone", 26),
          ("eightZeroTwoDot11Fh", 10),
          ("eightZeroTwoDot15dot4", 28),
          ("jammer", 19),
          ("microsoftDevice", 35),
          ("microwaveOven", 8),
          ("radar", 33),
          ("superAg", 32),
          ("tddTransmitter", 18),
          ("videoCamera", 27),
          ("wiMaxFixed", 37),
          ("wiMaxMobile", 36),
          ("wifiInvalidChannel", 31),
          ("wifiInverted", 30))
    )


_CLSiAqInterferenceClassReportDeviceClass_Type.__name__ = "Integer32"
_CLSiAqInterferenceClassReportDeviceClass_Object = MibTableColumn
cLSiAqInterferenceClassReportDeviceClass = _CLSiAqInterferenceClassReportDeviceClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 2, 1, 2),
    _CLSiAqInterferenceClassReportDeviceClass_Type()
)
cLSiAqInterferenceClassReportDeviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportDeviceClass.setStatus("current")


class _CLSiAqInterferenceClassReportSeverityIndex_Type(Unsigned32):
    """Custom type cLSiAqInterferenceClassReportSeverityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLSiAqInterferenceClassReportSeverityIndex_Type.__name__ = "Unsigned32"
_CLSiAqInterferenceClassReportSeverityIndex_Object = MibTableColumn
cLSiAqInterferenceClassReportSeverityIndex = _CLSiAqInterferenceClassReportSeverityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 2, 1, 3),
    _CLSiAqInterferenceClassReportSeverityIndex_Type()
)
cLSiAqInterferenceClassReportSeverityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportSeverityIndex.setStatus("current")


class _CLSiAqInterferenceClassReportPower_Type(Integer32):
    """Custom type cLSiAqInterferenceClassReportPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_CLSiAqInterferenceClassReportPower_Type.__name__ = "Integer32"
_CLSiAqInterferenceClassReportPower_Object = MibTableColumn
cLSiAqInterferenceClassReportPower = _CLSiAqInterferenceClassReportPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 2, 1, 4),
    _CLSiAqInterferenceClassReportPower_Type()
)
cLSiAqInterferenceClassReportPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportPower.setStatus("current")
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportPower.setUnits("dbm")


class _CLSiAqInterferenceClassReportDutyCycle_Type(Unsigned32):
    """Custom type cLSiAqInterferenceClassReportDutyCycle based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLSiAqInterferenceClassReportDutyCycle_Type.__name__ = "Unsigned32"
_CLSiAqInterferenceClassReportDutyCycle_Object = MibTableColumn
cLSiAqInterferenceClassReportDutyCycle = _CLSiAqInterferenceClassReportDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 2, 1, 5),
    _CLSiAqInterferenceClassReportDutyCycle_Type()
)
cLSiAqInterferenceClassReportDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportDutyCycle.setStatus("current")
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportDutyCycle.setUnits("percent")
_CLSiAqInterferenceClassReportDeviceCount_Type = Unsigned32
_CLSiAqInterferenceClassReportDeviceCount_Object = MibTableColumn
cLSiAqInterferenceClassReportDeviceCount = _CLSiAqInterferenceClassReportDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 1, 2, 1, 6),
    _CLSiAqInterferenceClassReportDeviceCount_Type()
)
cLSiAqInterferenceClassReportDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportDeviceCount.setStatus("current")
_CiscoLwappInterference_ObjectIdentity = ObjectIdentity
ciscoLwappInterference = _CiscoLwappInterference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2)
)
_CLSiIdrTable_Object = MibTable
cLSiIdrTable = _CLSiIdrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLSiIdrTable.setStatus("current")
_CLSiIdrEntry_Object = MibTableRow
cLSiIdrEntry = _CLSiIdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1)
)
cLSiIdrEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-SI-MIB", "cLSiIdrDeviceId"),
)
if mibBuilder.loadTexts:
    cLSiIdrEntry.setStatus("current")
_CLSiIdrDeviceId_Type = Unsigned32
_CLSiIdrDeviceId_Object = MibTableColumn
cLSiIdrDeviceId = _CLSiIdrDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 1),
    _CLSiIdrDeviceId_Type()
)
cLSiIdrDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSiIdrDeviceId.setStatus("current")
_CLSiIdrClusterId_Type = MacAddress
_CLSiIdrClusterId_Object = MibTableColumn
cLSiIdrClusterId = _CLSiIdrClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 2),
    _CLSiIdrClusterId_Type()
)
cLSiIdrClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterId.setStatus("current")
_CLSiIdrTimeStamp_Type = Unsigned32
_CLSiIdrTimeStamp_Object = MibTableColumn
cLSiIdrTimeStamp = _CLSiIdrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 3),
    _CLSiIdrTimeStamp_Type()
)
cLSiIdrTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrTimeStamp.setStatus("current")


class _CLSiIdrDeviceType_Type(Integer32):
    """Custom type cLSiIdrDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              10,
              17,
              18,
              19,
              25,
              26,
              27,
              28,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("bluetoothDiscovery", 17),
          ("bluetoothLink", 1),
          ("canopy", 34),
          ("continuousTransmitter", 25),
          ("dectLikePhone", 26),
          ("eightZeroTwoDot11Fh", 10),
          ("eightZeroTwoDot15dot4", 28),
          ("jammer", 19),
          ("microsoftDevice", 35),
          ("microwaveOven", 8),
          ("radar", 33),
          ("superAg", 32),
          ("tddTransmitter", 18),
          ("videoCamera", 27),
          ("wiMaxFixed", 37),
          ("wiMaxMobile", 36),
          ("wifiInvalidChannel", 31),
          ("wifiInverted", 30))
    )


_CLSiIdrDeviceType_Type.__name__ = "Integer32"
_CLSiIdrDeviceType_Object = MibTableColumn
cLSiIdrDeviceType = _CLSiIdrDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 4),
    _CLSiIdrDeviceType_Type()
)
cLSiIdrDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrDeviceType.setStatus("current")


class _CLSiIdrSeverity_Type(Unsigned32):
    """Custom type cLSiIdrSeverity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLSiIdrSeverity_Type.__name__ = "Unsigned32"
_CLSiIdrSeverity_Object = MibTableColumn
cLSiIdrSeverity = _CLSiIdrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 5),
    _CLSiIdrSeverity_Type()
)
cLSiIdrSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrSeverity.setStatus("current")
_CLSiIdrDetectingApMac_Type = MacAddress
_CLSiIdrDetectingApMac_Object = MibTableColumn
cLSiIdrDetectingApMac = _CLSiIdrDetectingApMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 6),
    _CLSiIdrDetectingApMac_Type()
)
cLSiIdrDetectingApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrDetectingApMac.setStatus("current")


class _CLSiIdrDutyCycle_Type(Unsigned32):
    """Custom type cLSiIdrDutyCycle based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLSiIdrDutyCycle_Type.__name__ = "Unsigned32"
_CLSiIdrDutyCycle_Object = MibTableColumn
cLSiIdrDutyCycle = _CLSiIdrDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 7),
    _CLSiIdrDutyCycle_Type()
)
cLSiIdrDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrDutyCycle.setStatus("current")
if mibBuilder.loadTexts:
    cLSiIdrDutyCycle.setUnits("percent")
_CLSiIdrAntennaId_Type = Unsigned32
_CLSiIdrAntennaId_Object = MibTableColumn
cLSiIdrAntennaId = _CLSiIdrAntennaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 8),
    _CLSiIdrAntennaId_Type()
)
cLSiIdrAntennaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrAntennaId.setStatus("current")


class _CLSiIdrRssi_Type(Integer32):
    """Custom type cLSiIdrRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_CLSiIdrRssi_Type.__name__ = "Integer32"
_CLSiIdrRssi_Object = MibTableColumn
cLSiIdrRssi = _CLSiIdrRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 9),
    _CLSiIdrRssi_Type()
)
cLSiIdrRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrRssi.setStatus("current")
if mibBuilder.loadTexts:
    cLSiIdrRssi.setUnits("dbm")
_CLSiIdrRadioBandId_Type = CLDot11Band
_CLSiIdrRadioBandId_Object = MibTableColumn
cLSiIdrRadioBandId = _CLSiIdrRadioBandId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 10),
    _CLSiIdrRadioBandId_Type()
)
cLSiIdrRadioBandId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrRadioBandId.setStatus("current")
_CLSiIdrAffectedChannels_Type = Unsigned32
_CLSiIdrAffectedChannels_Object = MibTableColumn
cLSiIdrAffectedChannels = _CLSiIdrAffectedChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 11),
    _CLSiIdrAffectedChannels_Type()
)
cLSiIdrAffectedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrAffectedChannels.setStatus("current")
_CLSiIdrDeviceSignatureLen_Type = Unsigned32
_CLSiIdrDeviceSignatureLen_Object = MibTableColumn
cLSiIdrDeviceSignatureLen = _CLSiIdrDeviceSignatureLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 12),
    _CLSiIdrDeviceSignatureLen_Type()
)
cLSiIdrDeviceSignatureLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrDeviceSignatureLen.setStatus("current")


class _CLSiIdrDeviceSignature_Type(OctetString):
    """Custom type cLSiIdrDeviceSignature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLSiIdrDeviceSignature_Type.__name__ = "OctetString"
_CLSiIdrDeviceSignature_Object = MibTableColumn
cLSiIdrDeviceSignature = _CLSiIdrDeviceSignature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 1, 1, 13),
    _CLSiIdrDeviceSignature_Type()
)
cLSiIdrDeviceSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrDeviceSignature.setStatus("current")
_CLSiIdrClusterTable_Object = MibTable
cLSiIdrClusterTable = _CLSiIdrClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cLSiIdrClusterTable.setStatus("current")
_CLSiIdrClusterEntry_Object = MibTableRow
cLSiIdrClusterEntry = _CLSiIdrClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1)
)
cLSiIdrClusterEntry.setIndexNames(
    (0, "CISCO-LWAPP-SI-MIB", "cLSiIdrClusterRadioBandId"),
    (0, "CISCO-LWAPP-SI-MIB", "cLSiIdrClusterClusterId"),
    (0, "CISCO-LWAPP-SI-MIB", "cLSiIdrClusterDeviceIndex"),
)
if mibBuilder.loadTexts:
    cLSiIdrClusterEntry.setStatus("current")
_CLSiIdrClusterRadioBandId_Type = CLDot11Band
_CLSiIdrClusterRadioBandId_Object = MibTableColumn
cLSiIdrClusterRadioBandId = _CLSiIdrClusterRadioBandId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 1),
    _CLSiIdrClusterRadioBandId_Type()
)
cLSiIdrClusterRadioBandId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterRadioBandId.setStatus("current")
_CLSiIdrClusterClusterId_Type = MacAddress
_CLSiIdrClusterClusterId_Object = MibTableColumn
cLSiIdrClusterClusterId = _CLSiIdrClusterClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 2),
    _CLSiIdrClusterClusterId_Type()
)
cLSiIdrClusterClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterClusterId.setStatus("current")


class _CLSiIdrClusterDeviceIndex_Type(Unsigned32):
    """Custom type cLSiIdrClusterDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CLSiIdrClusterDeviceIndex_Type.__name__ = "Unsigned32"
_CLSiIdrClusterDeviceIndex_Object = MibTableColumn
cLSiIdrClusterDeviceIndex = _CLSiIdrClusterDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 3),
    _CLSiIdrClusterDeviceIndex_Type()
)
cLSiIdrClusterDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSiIdrClusterDeviceIndex.setStatus("current")
_CLSiIdrClusterDeviceId_Type = Unsigned32
_CLSiIdrClusterDeviceId_Object = MibTableColumn
cLSiIdrClusterDeviceId = _CLSiIdrClusterDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 4),
    _CLSiIdrClusterDeviceId_Type()
)
cLSiIdrClusterDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterDeviceId.setStatus("current")
_CLSiIdrClusterTimeStamp_Type = Unsigned32
_CLSiIdrClusterTimeStamp_Object = MibTableColumn
cLSiIdrClusterTimeStamp = _CLSiIdrClusterTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 5),
    _CLSiIdrClusterTimeStamp_Type()
)
cLSiIdrClusterTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterTimeStamp.setStatus("current")


class _CLSiIdrClusterDeviceType_Type(Integer32):
    """Custom type cLSiIdrClusterDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              10,
              17,
              18,
              19,
              25,
              26,
              27,
              28,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("bluetoothDiscovery", 17),
          ("bluetoothLink", 1),
          ("canopy", 34),
          ("continuousTransmitter", 25),
          ("dectLikePhone", 26),
          ("eightZeroTwoDot11Fh", 10),
          ("eightZeroTwoDot15dot4", 28),
          ("jammer", 19),
          ("microsoftDevice", 35),
          ("microwaveOven", 8),
          ("radar", 33),
          ("superAg", 32),
          ("tddTransmitter", 18),
          ("unclassified", 39),
          ("unknown", 40),
          ("videoCamera", 27),
          ("wiMaxFixed", 37),
          ("wiMaxMobile", 36),
          ("wifiAci", 38),
          ("wifiInvalidChannel", 31),
          ("wifiInverted", 30))
    )


_CLSiIdrClusterDeviceType_Type.__name__ = "Integer32"
_CLSiIdrClusterDeviceType_Object = MibTableColumn
cLSiIdrClusterDeviceType = _CLSiIdrClusterDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 6),
    _CLSiIdrClusterDeviceType_Type()
)
cLSiIdrClusterDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterDeviceType.setStatus("current")


class _CLSiIdrClusterSeverity_Type(Unsigned32):
    """Custom type cLSiIdrClusterSeverity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLSiIdrClusterSeverity_Type.__name__ = "Unsigned32"
_CLSiIdrClusterSeverity_Object = MibTableColumn
cLSiIdrClusterSeverity = _CLSiIdrClusterSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 7),
    _CLSiIdrClusterSeverity_Type()
)
cLSiIdrClusterSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterSeverity.setStatus("current")
_CLSiIdrClusterDetectingApMac_Type = MacAddress
_CLSiIdrClusterDetectingApMac_Object = MibTableColumn
cLSiIdrClusterDetectingApMac = _CLSiIdrClusterDetectingApMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 8),
    _CLSiIdrClusterDetectingApMac_Type()
)
cLSiIdrClusterDetectingApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterDetectingApMac.setStatus("current")


class _CLSiIdrClusterDutyCycle_Type(Unsigned32):
    """Custom type cLSiIdrClusterDutyCycle based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CLSiIdrClusterDutyCycle_Type.__name__ = "Unsigned32"
_CLSiIdrClusterDutyCycle_Object = MibTableColumn
cLSiIdrClusterDutyCycle = _CLSiIdrClusterDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 9),
    _CLSiIdrClusterDutyCycle_Type()
)
cLSiIdrClusterDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterDutyCycle.setStatus("current")
if mibBuilder.loadTexts:
    cLSiIdrClusterDutyCycle.setUnits("percent")
_CLSiIdrClusterAntennaId_Type = Unsigned32
_CLSiIdrClusterAntennaId_Object = MibTableColumn
cLSiIdrClusterAntennaId = _CLSiIdrClusterAntennaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 10),
    _CLSiIdrClusterAntennaId_Type()
)
cLSiIdrClusterAntennaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterAntennaId.setStatus("current")


class _CLSiIdrClusterRssi_Type(Integer32):
    """Custom type cLSiIdrClusterRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_CLSiIdrClusterRssi_Type.__name__ = "Integer32"
_CLSiIdrClusterRssi_Object = MibTableColumn
cLSiIdrClusterRssi = _CLSiIdrClusterRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 11),
    _CLSiIdrClusterRssi_Type()
)
cLSiIdrClusterRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterRssi.setStatus("current")
if mibBuilder.loadTexts:
    cLSiIdrClusterRssi.setUnits("dbm")
_CLSiIdrClusterAffectedChannels_Type = Unsigned32
_CLSiIdrClusterAffectedChannels_Object = MibTableColumn
cLSiIdrClusterAffectedChannels = _CLSiIdrClusterAffectedChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 12),
    _CLSiIdrClusterAffectedChannels_Type()
)
cLSiIdrClusterAffectedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterAffectedChannels.setStatus("current")
_CLSiIdrClusterDeviceSignatureLen_Type = Unsigned32
_CLSiIdrClusterDeviceSignatureLen_Object = MibTableColumn
cLSiIdrClusterDeviceSignatureLen = _CLSiIdrClusterDeviceSignatureLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 13),
    _CLSiIdrClusterDeviceSignatureLen_Type()
)
cLSiIdrClusterDeviceSignatureLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterDeviceSignatureLen.setStatus("current")


class _CLSiIdrClusterDeviceSignature_Type(OctetString):
    """Custom type cLSiIdrClusterDeviceSignature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLSiIdrClusterDeviceSignature_Type.__name__ = "OctetString"
_CLSiIdrClusterDeviceSignature_Object = MibTableColumn
cLSiIdrClusterDeviceSignature = _CLSiIdrClusterDeviceSignature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 14),
    _CLSiIdrClusterDeviceSignature_Type()
)
cLSiIdrClusterDeviceSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterDeviceSignature.setStatus("current")
_CLSiIdrClusterCenterIndex_Type = Unsigned32
_CLSiIdrClusterCenterIndex_Object = MibTableColumn
cLSiIdrClusterCenterIndex = _CLSiIdrClusterCenterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 15),
    _CLSiIdrClusterCenterIndex_Type()
)
cLSiIdrClusterCenterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterCenterIndex.setStatus("current")


class _CLSiIdrClusterType_Type(Integer32):
    """Custom type cLSiIdrClusterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              10,
              17,
              18,
              19,
              25,
              26,
              27,
              28,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("bluetoothDiscovery", 17),
          ("bluetoothLink", 1),
          ("canopy", 34),
          ("continuousTransmitter", 25),
          ("dectLikePhone", 26),
          ("eightZeroTwoDot11Fh", 10),
          ("eightZeroTwoDot15dot4", 28),
          ("jammer", 19),
          ("microsoftDevice", 35),
          ("microwaveOven", 8),
          ("radar", 33),
          ("superAg", 32),
          ("tddTransmitter", 18),
          ("unclassified", 39),
          ("unknown", 40),
          ("videoCamera", 27),
          ("wiMaxFixed", 37),
          ("wiMaxMobile", 36),
          ("wifiAci", 38),
          ("wifiInvalidChannel", 31),
          ("wifiInverted", 30))
    )


_CLSiIdrClusterType_Type.__name__ = "Integer32"
_CLSiIdrClusterType_Object = MibTableColumn
cLSiIdrClusterType = _CLSiIdrClusterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 2, 1, 16),
    _CLSiIdrClusterType_Type()
)
cLSiIdrClusterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiIdrClusterType.setStatus("current")
_CLSiPersistentDeviceTable_Object = MibTable
cLSiPersistentDeviceTable = _CLSiPersistentDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cLSiPersistentDeviceTable.setStatus("current")
_CLSiPersistentDeviceEntry_Object = MibTableRow
cLSiPersistentDeviceEntry = _CLSiPersistentDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 3, 1)
)
cLSiPersistentDeviceEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-SI-MIB", "cLSiPersistentDeviceId"),
)
if mibBuilder.loadTexts:
    cLSiPersistentDeviceEntry.setStatus("current")
_CLSiPersistentDeviceId_Type = Unsigned32
_CLSiPersistentDeviceId_Object = MibTableColumn
cLSiPersistentDeviceId = _CLSiPersistentDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 3, 1, 1),
    _CLSiPersistentDeviceId_Type()
)
cLSiPersistentDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSiPersistentDeviceId.setStatus("current")
_CLSiPersistentDeviceType_Type = OctetString
_CLSiPersistentDeviceType_Object = MibTableColumn
cLSiPersistentDeviceType = _CLSiPersistentDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 3, 1, 2),
    _CLSiPersistentDeviceType_Type()
)
cLSiPersistentDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiPersistentDeviceType.setStatus("current")
_CLSiPersistentTimeStamp_Type = Unsigned32
_CLSiPersistentTimeStamp_Object = MibTableColumn
cLSiPersistentTimeStamp = _CLSiPersistentTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 3, 1, 3),
    _CLSiPersistentTimeStamp_Type()
)
cLSiPersistentTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiPersistentTimeStamp.setStatus("current")
_CLSiPersistentDeviceChanTable_Object = MibTable
cLSiPersistentDeviceChanTable = _CLSiPersistentDeviceChanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cLSiPersistentDeviceChanTable.setStatus("current")
_CLSiPersistentDeviceChanEntry_Object = MibTableRow
cLSiPersistentDeviceChanEntry = _CLSiPersistentDeviceChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 4, 1)
)
cLSiPersistentDeviceChanEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-SI-MIB", "cLSiPersistentDeviceId"),
    (0, "CISCO-LWAPP-SI-MIB", "cLSiPersistentDeviceChanIndex"),
)
if mibBuilder.loadTexts:
    cLSiPersistentDeviceChanEntry.setStatus("current")
_CLSiPersistentDeviceChanIndex_Type = Unsigned32
_CLSiPersistentDeviceChanIndex_Object = MibTableColumn
cLSiPersistentDeviceChanIndex = _CLSiPersistentDeviceChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 4, 1, 1),
    _CLSiPersistentDeviceChanIndex_Type()
)
cLSiPersistentDeviceChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSiPersistentDeviceChanIndex.setStatus("current")


class _CLSiChannelAffected_Type(Unsigned32):
    """Custom type cLSiChannelAffected based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CLSiChannelAffected_Type.__name__ = "Unsigned32"
_CLSiChannelAffected_Object = MibTableColumn
cLSiChannelAffected = _CLSiChannelAffected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 4, 1, 2),
    _CLSiChannelAffected_Type()
)
cLSiChannelAffected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiChannelAffected.setStatus("current")
_CLSiChannelUtil_Type = Unsigned32
_CLSiChannelUtil_Object = MibTableColumn
cLSiChannelUtil = _CLSiChannelUtil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 4, 1, 3),
    _CLSiChannelUtil_Type()
)
cLSiChannelUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiChannelUtil.setStatus("current")


class _CLSiChannelRSSI_Type(Integer32):
    """Custom type cLSiChannelRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_CLSiChannelRSSI_Type.__name__ = "Integer32"
_CLSiChannelRSSI_Object = MibTableColumn
cLSiChannelRSSI = _CLSiChannelRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 2, 4, 1, 4),
    _CLSiChannelRSSI_Type()
)
cLSiChannelRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiChannelRSSI.setStatus("current")
_CiscoLwappSiDot11Band_ObjectIdentity = ObjectIdentity
ciscoLwappSiDot11Band = _CiscoLwappSiDot11Band_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3)
)
_CLSiDot11BandTable_Object = MibTable
cLSiDot11BandTable = _CLSiDot11BandTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLSiDot11BandTable.setStatus("current")
_CLSiDot11BandEntry_Object = MibTableRow
cLSiDot11BandEntry = _CLSiDot11BandEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1)
)
cLSiDot11BandEntry.setIndexNames(
    (0, "CISCO-LWAPP-SI-MIB", "cLSiD11Band"),
)
if mibBuilder.loadTexts:
    cLSiDot11BandEntry.setStatus("current")
_CLSiD11Band_Type = CLDot11Band
_CLSiD11Band_Object = MibTableColumn
cLSiD11Band = _CLSiD11Band_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 1),
    _CLSiD11Band_Type()
)
cLSiD11Band.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLSiD11Band.setStatus("current")


class _CLSiD11SpectrumIntelligenceEnable_Type(TruthValue):
    """Custom type cLSiD11SpectrumIntelligenceEnable based on TruthValue"""


_CLSiD11SpectrumIntelligenceEnable_Object = MibTableColumn
cLSiD11SpectrumIntelligenceEnable = _CLSiD11SpectrumIntelligenceEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 2),
    _CLSiD11SpectrumIntelligenceEnable_Type()
)
cLSiD11SpectrumIntelligenceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11SpectrumIntelligenceEnable.setStatus("current")


class _CLSiD11InterferenceDeviceList_Type(Bits):
    """Custom type cLSiD11InterferenceDeviceList based on Bits"""
    namedValues = NamedValues(
        *(("bluetoothDiscovery", 14),
          ("bluetoothLink", 17),
          ("canopy", 3),
          ("continuousTransmitter", 11),
          ("dectLikePhone", 10),
          ("eightZeroTwoDot11Fh", 15),
          ("eightZeroTwoDot15dot4", 8),
          ("jammer", 12),
          ("microwaveOven", 16),
          ("radar", 4),
          ("superAg", 5),
          ("tddTransmitter", 13),
          ("videoCamera", 9),
          ("wiMaxFixed", 0),
          ("wiMaxMobile", 1),
          ("wifiInvalidChannel", 6),
          ("wifiInverted", 7),
          ("xbox", 2))
    )

_CLSiD11InterferenceDeviceList_Type.__name__ = "Bits"
_CLSiD11InterferenceDeviceList_Object = MibTableColumn
cLSiD11InterferenceDeviceList = _CLSiD11InterferenceDeviceList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 3),
    _CLSiD11InterferenceDeviceList_Type()
)
cLSiD11InterferenceDeviceList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11InterferenceDeviceList.setStatus("current")


class _CLSiD11PollingInterval_Type(Unsigned32):
    """Custom type cLSiD11PollingInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 60),
    )


_CLSiD11PollingInterval_Type.__name__ = "Unsigned32"
_CLSiD11PollingInterval_Object = MibTableColumn
cLSiD11PollingInterval = _CLSiD11PollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 4),
    _CLSiD11PollingInterval_Type()
)
cLSiD11PollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11PollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLSiD11PollingInterval.setUnits("minutes")


class _CLSiD11IdrReportingEnable_Type(TruthValue):
    """Custom type cLSiD11IdrReportingEnable based on TruthValue"""


_CLSiD11IdrReportingEnable_Object = MibTableColumn
cLSiD11IdrReportingEnable = _CLSiD11IdrReportingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 6),
    _CLSiD11IdrReportingEnable_Type()
)
cLSiD11IdrReportingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11IdrReportingEnable.setStatus("current")


class _CLSiD11AqiTrapEnable_Type(TruthValue):
    """Custom type cLSiD11AqiTrapEnable based on TruthValue"""


_CLSiD11AqiTrapEnable_Object = MibTableColumn
cLSiD11AqiTrapEnable = _CLSiD11AqiTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 7),
    _CLSiD11AqiTrapEnable_Type()
)
cLSiD11AqiTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11AqiTrapEnable.setStatus("current")


class _CLSiD11AqiTrapThreshold_Type(Unsigned32):
    """Custom type cLSiD11AqiTrapThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLSiD11AqiTrapThreshold_Type.__name__ = "Unsigned32"
_CLSiD11AqiTrapThreshold_Object = MibTableColumn
cLSiD11AqiTrapThreshold = _CLSiD11AqiTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 8),
    _CLSiD11AqiTrapThreshold_Type()
)
cLSiD11AqiTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11AqiTrapThreshold.setStatus("current")


class _CLSiD11IdrTrapEnable_Type(TruthValue):
    """Custom type cLSiD11IdrTrapEnable based on TruthValue"""


_CLSiD11IdrTrapEnable_Object = MibTableColumn
cLSiD11IdrTrapEnable = _CLSiD11IdrTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 9),
    _CLSiD11IdrTrapEnable_Type()
)
cLSiD11IdrTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11IdrTrapEnable.setStatus("current")


class _CLSiD11IdrTrapDeviceList_Type(Bits):
    """Custom type cLSiD11IdrTrapDeviceList based on Bits"""
    namedValues = NamedValues(
        *(("bluetoothDiscovery", 14),
          ("bluetoothLink", 17),
          ("canopy", 3),
          ("continuousTransmitter", 11),
          ("dectLikePhone", 10),
          ("eightZeroTwoDot11Fh", 15),
          ("eightZeroTwoDot15dot4", 8),
          ("jammer", 12),
          ("microwaveOven", 16),
          ("radar", 4),
          ("superAg", 5),
          ("tddTransmitter", 13),
          ("videoCamera", 9),
          ("wiMaxFixed", 0),
          ("wiMaxMobile", 1),
          ("wifiInvalidChannel", 6),
          ("wifiInverted", 7),
          ("xbox", 2))
    )

_CLSiD11IdrTrapDeviceList_Type.__name__ = "Bits"
_CLSiD11IdrTrapDeviceList_Object = MibTableColumn
cLSiD11IdrTrapDeviceList = _CLSiD11IdrTrapDeviceList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 10),
    _CLSiD11IdrTrapDeviceList_Type()
)
cLSiD11IdrTrapDeviceList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11IdrTrapDeviceList.setStatus("current")
_CLSiD11IdrPersistentDevicePropagation_Type = TruthValue
_CLSiD11IdrPersistentDevicePropagation_Object = MibTableColumn
cLSiD11IdrPersistentDevicePropagation = _CLSiD11IdrPersistentDevicePropagation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 11),
    _CLSiD11IdrPersistentDevicePropagation_Type()
)
cLSiD11IdrPersistentDevicePropagation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11IdrPersistentDevicePropagation.setStatus("current")
_CLSiD11IdrUnclassifiedTrapEnable_Type = TruthValue
_CLSiD11IdrUnclassifiedTrapEnable_Object = MibTableColumn
cLSiD11IdrUnclassifiedTrapEnable = _CLSiD11IdrUnclassifiedTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 12),
    _CLSiD11IdrUnclassifiedTrapEnable_Type()
)
cLSiD11IdrUnclassifiedTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11IdrUnclassifiedTrapEnable.setStatus("current")


class _CLSiD11IdrUnclassifiedTrapThreshold_Type(Unsigned32):
    """Custom type cLSiD11IdrUnclassifiedTrapThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLSiD11IdrUnclassifiedTrapThreshold_Type.__name__ = "Unsigned32"
_CLSiD11IdrUnclassifiedTrapThreshold_Object = MibTableColumn
cLSiD11IdrUnclassifiedTrapThreshold = _CLSiD11IdrUnclassifiedTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 1, 1, 13),
    _CLSiD11IdrUnclassifiedTrapThreshold_Type()
)
cLSiD11IdrUnclassifiedTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11IdrUnclassifiedTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cLSiD11IdrUnclassifiedTrapThreshold.setUnits("percent")
_CLSiDot11BandEventDrivenRrmTable_Object = MibTable
cLSiDot11BandEventDrivenRrmTable = _CLSiDot11BandEventDrivenRrmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cLSiDot11BandEventDrivenRrmTable.setStatus("current")
_CLSiDot11BandEventDrivenRrmEntry_Object = MibTableRow
cLSiDot11BandEventDrivenRrmEntry = _CLSiDot11BandEventDrivenRrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 2, 1)
)
cLSiDot11BandEventDrivenRrmEntry.setIndexNames(
    (0, "CISCO-LWAPP-SI-MIB", "cLSiD11Band"),
)
if mibBuilder.loadTexts:
    cLSiDot11BandEventDrivenRrmEntry.setStatus("current")


class _CLSiD11EventDrivenRrmEnable_Type(TruthValue):
    """Custom type cLSiD11EventDrivenRrmEnable based on TruthValue"""


_CLSiD11EventDrivenRrmEnable_Object = MibTableColumn
cLSiD11EventDrivenRrmEnable = _CLSiD11EventDrivenRrmEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 2, 1, 1),
    _CLSiD11EventDrivenRrmEnable_Type()
)
cLSiD11EventDrivenRrmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11EventDrivenRrmEnable.setStatus("current")


class _CLSiD11EventDrivenRrmThresLvl_Type(Integer32):
    """Custom type cLSiD11EventDrivenRrmThresLvl based on Integer32"""
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
        *(("custom", 4),
          ("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_CLSiD11EventDrivenRrmThresLvl_Type.__name__ = "Integer32"
_CLSiD11EventDrivenRrmThresLvl_Object = MibTableColumn
cLSiD11EventDrivenRrmThresLvl = _CLSiD11EventDrivenRrmThresLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 2, 1, 2),
    _CLSiD11EventDrivenRrmThresLvl_Type()
)
cLSiD11EventDrivenRrmThresLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11EventDrivenRrmThresLvl.setStatus("current")


class _CLSiD11EventDrivenRrmCustomThresVal_Type(Unsigned32):
    """Custom type cLSiD11EventDrivenRrmCustomThresVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CLSiD11EventDrivenRrmCustomThresVal_Type.__name__ = "Unsigned32"
_CLSiD11EventDrivenRrmCustomThresVal_Object = MibTableColumn
cLSiD11EventDrivenRrmCustomThresVal = _CLSiD11EventDrivenRrmCustomThresVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 3, 2, 1, 3),
    _CLSiD11EventDrivenRrmCustomThresVal_Type()
)
cLSiD11EventDrivenRrmCustomThresVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiD11EventDrivenRrmCustomThresVal.setStatus("current")
if mibBuilder.loadTexts:
    cLSiD11EventDrivenRrmCustomThresVal.setUnits("percent")
_CiscoLwappSiApIf_ObjectIdentity = ObjectIdentity
ciscoLwappSiApIf = _CiscoLwappSiApIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 4)
)
_CLSiApIfTable_Object = MibTable
cLSiApIfTable = _CLSiApIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cLSiApIfTable.setStatus("current")
_CLSiApIfEntry_Object = MibTableRow
cLSiApIfEntry = _CLSiApIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 4, 1, 1)
)
cLSiApIfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLSiApIfEntry.setStatus("current")


class _CLSiApIfSpectrumIntelligenceEnable_Type(TruthValue):
    """Custom type cLSiApIfSpectrumIntelligenceEnable based on TruthValue"""


_CLSiApIfSpectrumIntelligenceEnable_Object = MibTableColumn
cLSiApIfSpectrumIntelligenceEnable = _CLSiApIfSpectrumIntelligenceEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 4, 1, 1, 1),
    _CLSiApIfSpectrumIntelligenceEnable_Type()
)
cLSiApIfSpectrumIntelligenceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiApIfSpectrumIntelligenceEnable.setStatus("current")
_CLSiApIfSpectrumCapable_Type = TruthValue
_CLSiApIfSpectrumCapable_Object = MibTableColumn
cLSiApIfSpectrumCapable = _CLSiApIfSpectrumCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 4, 1, 1, 2),
    _CLSiApIfSpectrumCapable_Type()
)
cLSiApIfSpectrumCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiApIfSpectrumCapable.setStatus("current")


class _CLSiApIfRapidUpdateEnable_Type(TruthValue):
    """Custom type cLSiApIfRapidUpdateEnable based on TruthValue"""


_CLSiApIfRapidUpdateEnable_Object = MibTableColumn
cLSiApIfRapidUpdateEnable = _CLSiApIfRapidUpdateEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 4, 1, 1, 3),
    _CLSiApIfRapidUpdateEnable_Type()
)
cLSiApIfRapidUpdateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiApIfRapidUpdateEnable.setStatus("current")


class _CLSiApIfDetailSpectrumModeEnable_Type(TruthValue):
    """Custom type cLSiApIfDetailSpectrumModeEnable based on TruthValue"""


_CLSiApIfDetailSpectrumModeEnable_Object = MibTableColumn
cLSiApIfDetailSpectrumModeEnable = _CLSiApIfDetailSpectrumModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 4, 1, 1, 4),
    _CLSiApIfDetailSpectrumModeEnable_Type()
)
cLSiApIfDetailSpectrumModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLSiApIfDetailSpectrumModeEnable.setStatus("current")


class _CLSiApIfSensordOperationalStatus_Type(Integer32):
    """Custom type cLSiApIfSensordOperationalStatus based on Integer32"""
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
        *(("down", 2),
          ("notApplicable", 3),
          ("up", 1))
    )


_CLSiApIfSensordOperationalStatus_Type.__name__ = "Integer32"
_CLSiApIfSensordOperationalStatus_Object = MibTableColumn
cLSiApIfSensordOperationalStatus = _CLSiApIfSensordOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 4, 1, 1, 5),
    _CLSiApIfSensordOperationalStatus_Type()
)
cLSiApIfSensordOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiApIfSensordOperationalStatus.setStatus("current")
_CLSiApIfNumOfSeActiveConnection_Type = Unsigned32
_CLSiApIfNumOfSeActiveConnection_Object = MibTableColumn
cLSiApIfNumOfSeActiveConnection = _CLSiApIfNumOfSeActiveConnection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 4, 1, 1, 6),
    _CLSiApIfNumOfSeActiveConnection_Type()
)
cLSiApIfNumOfSeActiveConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiApIfNumOfSeActiveConnection.setStatus("current")


class _CLSiApIfSensordErrorCode_Type(Integer32):
    """Custom type cLSiApIfSensordErrorCode based on Integer32"""
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
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("apNonCleanAirMode", 3),
          ("configured", 1),
          ("failedChannelConfig", 4),
          ("failedConnectionWithSensor", 6),
          ("failedResourceAllocation", 5),
          ("failedSIStream", 8),
          ("invalidSIConfig", 2),
          ("radioDisabled", 9),
          ("radioNotCleanAirCapable", 7),
          ("recoverableError", 129),
          ("unrecoverableCrash", 130))
    )


_CLSiApIfSensordErrorCode_Type.__name__ = "Integer32"
_CLSiApIfSensordErrorCode_Object = MibTableColumn
cLSiApIfSensordErrorCode = _CLSiApIfSensordErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 1, 4, 1, 1, 7),
    _CLSiApIfSensordErrorCode_Type()
)
cLSiApIfSensordErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLSiApIfSensordErrorCode.setStatus("current")
_CiscoLwappSiMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappSiMIBConform = _CiscoLwappSiMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2)
)
_CiscoLwappSiMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappSiMIBCompliances = _CiscoLwappSiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 1)
)
_CiscoLwappSiMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappSiMIBGroups = _CiscoLwappSiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2)
)
_CiscoLwappSiMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappSiMIBNotifObjects = _CiscoLwappSiMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 3)
)
_CLSiAlarmClear_Type = TruthValue
_CLSiAlarmClear_Object = MibScalar
cLSiAlarmClear = _CLSiAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 3, 1),
    _CLSiAlarmClear_Type()
)
cLSiAlarmClear.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLSiAlarmClear.setStatus("current")
_CLSiIdrPreviousClusterId_Type = MacAddress
_CLSiIdrPreviousClusterId_Object = MibScalar
cLSiIdrPreviousClusterId = _CLSiIdrPreviousClusterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 3, 2),
    _CLSiIdrPreviousClusterId_Type()
)
cLSiIdrPreviousClusterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLSiIdrPreviousClusterId.setStatus("current")
_CLSiApAqLimit_Type = Integer32
_CLSiApAqLimit_Object = MibScalar
cLSiApAqLimit = _CLSiApAqLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 3, 3),
    _CLSiApAqLimit_Type()
)
cLSiApAqLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLSiApAqLimit.setStatus("current")


class _CLSiD11IdrUnclassifiedCurrentSevIndex_Type(Unsigned32):
    """Custom type cLSiD11IdrUnclassifiedCurrentSevIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLSiD11IdrUnclassifiedCurrentSevIndex_Type.__name__ = "Unsigned32"
_CLSiD11IdrUnclassifiedCurrentSevIndex_Object = MibScalar
cLSiD11IdrUnclassifiedCurrentSevIndex = _CLSiD11IdrUnclassifiedCurrentSevIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 3, 4),
    _CLSiD11IdrUnclassifiedCurrentSevIndex_Type()
)
cLSiD11IdrUnclassifiedCurrentSevIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLSiD11IdrUnclassifiedCurrentSevIndex.setStatus("current")
if mibBuilder.loadTexts:
    cLSiD11IdrUnclassifiedCurrentSevIndex.setUnits("percent")

# Managed Objects groups

cLSiApIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 1)
)
cLSiApIfConfigGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiApIfSpectrumIntelligenceEnable"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApIfRapidUpdateEnable"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApIfDetailSpectrumModeEnable"))
)
if mibBuilder.loadTexts:
    cLSiApIfConfigGroup.setStatus("current")

cLSiApIfStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 2)
)
cLSiApIfStatusGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiApIfSpectrumCapable"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApIfSensordOperationalStatus"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApIfNumOfSeActiveConnection"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApIfSensordErrorCode"))
)
if mibBuilder.loadTexts:
    cLSiApIfStatusGroup.setStatus("current")

cLSiD11ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 3)
)
cLSiD11ConfigGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiD11SpectrumIntelligenceEnable"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11InterferenceDeviceList"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11PollingInterval"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11IdrReportingEnable"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11AqiTrapEnable"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11AqiTrapThreshold"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11IdrTrapEnable"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11IdrTrapDeviceList"))
)
if mibBuilder.loadTexts:
    cLSiD11ConfigGroup.setStatus("current")

cLSiAqChannelStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 4)
)
cLSiAqChannelStatusGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiAqMinIndex"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqIndex"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqTotalChannelPower"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqTotalChannelDutyCycle"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqInterferencePower"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqInterferenceDutyCycle"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqInterferenceDeviceCount"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqInterfererClassReportCount"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqTimeStamp"))
)
if mibBuilder.loadTexts:
    cLSiAqChannelStatusGroup.setStatus("current")

cLSiAqInterferenceClassReportStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 5)
)
cLSiAqInterferenceClassReportStatusGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiAqInterferenceClassReportDeviceClass"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqInterferenceClassReportSeverityIndex"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqInterferenceClassReportPower"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqInterferenceClassReportDutyCycle"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqInterferenceClassReportDeviceCount"))
)
if mibBuilder.loadTexts:
    cLSiAqInterferenceClassReportStatusGroup.setStatus("current")

cLSiIdrStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 6)
)
cLSiIdrStatusGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrTimeStamp"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrDeviceType"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrSeverity"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrDetectingApMac"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrDutyCycle"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrAntennaId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrRssi"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrRadioBandId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrAffectedChannels"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrDeviceSignatureLen"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrDeviceSignature"))
)
if mibBuilder.loadTexts:
    cLSiIdrStatusGroup.setStatus("current")

cLSiIdrClusterStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 7)
)
cLSiIdrClusterStatusGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterRadioBandId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterClusterId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterDeviceId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterTimeStamp"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterDeviceType"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterSeverity"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterDetectingApMac"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterDutyCycle"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterAntennaId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterRssi"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterAffectedChannels"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterDeviceSignatureLen"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterDeviceSignature"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterCenterIndex"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterType"))
)
if mibBuilder.loadTexts:
    cLSiIdrClusterStatusGroup.setStatus("current")

cLSiD11EventDrivenRrmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 8)
)
cLSiD11EventDrivenRrmConfigGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiD11EventDrivenRrmEnable"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11EventDrivenRrmThresLvl"))
)
if mibBuilder.loadTexts:
    cLSiD11EventDrivenRrmConfigGroup.setStatus("current")

cLSiPersistentDeviceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 9)
)
cLSiPersistentDeviceStatusGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiPersistentDeviceType"),
        ("CISCO-LWAPP-SI-MIB", "cLSiPersistentTimeStamp"))
)
if mibBuilder.loadTexts:
    cLSiPersistentDeviceStatusGroup.setStatus("current")

cLSiPersistentDeviceChanStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 10)
)
cLSiPersistentDeviceChanStatusGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiChannelAffected"),
        ("CISCO-LWAPP-SI-MIB", "cLSiChannelUtil"),
        ("CISCO-LWAPP-SI-MIB", "cLSiChannelRSSI"))
)
if mibBuilder.loadTexts:
    cLSiPersistentDeviceChanStatusGroup.setStatus("current")

cLSiD11ConfigSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 11)
)
cLSiD11ConfigSup1Group.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiD11IdrPersistentDevicePropagation"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11IdrUnclassifiedTrapEnable"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11IdrUnclassifiedTrapThreshold"))
)
if mibBuilder.loadTexts:
    cLSiD11ConfigSup1Group.setStatus("current")

cLSiD11EventDrivenRrmConfigSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 12)
)
cLSiD11EventDrivenRrmConfigSup1Group.setObjects(
    ("CISCO-LWAPP-SI-MIB", "cLSiD11EventDrivenRrmCustomThresVal")
)
if mibBuilder.loadTexts:
    cLSiD11EventDrivenRrmConfigSup1Group.setStatus("current")

ciscoLwappSiMIBNotifVariableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 14)
)
ciscoLwappSiMIBNotifVariableGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiAlarmClear"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrPreviousClusterId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApAqLimit"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11IdrUnclassifiedCurrentSevIndex"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiMIBNotifVariableGroup.setStatus("current")


# Notification objects

ciscoLwappSiAqLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0, 1)
)
ciscoLwappSiAqLow.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqChannelNumber"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqIndex"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11AqiTrapThreshold"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAlarmClear"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiAqLow.setStatus(
        "deprecated"
    )

ciscoLwappSiIdrDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0, 2)
)
ciscoLwappSiIdrDevice.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrDeviceId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrDeviceType"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrAffectedChannels"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrSeverity"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAlarmClear"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrPreviousClusterId"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiIdrDevice.setStatus(
        "deprecated"
    )

ciscoLwappSiSensorCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0, 3)
)
ciscoLwappSiSensorCrash.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApIfSensordOperationalStatus"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApIfSensordErrorCode"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiSensorCrash.setStatus(
        "deprecated"
    )

ciscoLwappSiAqBufferUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0, 4)
)
ciscoLwappSiAqBufferUnavailable.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApAqLimit"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAlarmClear"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiAqBufferUnavailable.setStatus(
        "deprecated"
    )

ciscoLwappSiAqLowSeverityHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0, 5)
)
ciscoLwappSiAqLowSeverityHigh.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqChannelNumber"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAqIndex"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11AqiTrapThreshold"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11IdrUnclassifiedTrapThreshold"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11IdrUnclassifiedCurrentSevIndex"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAlarmClear"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiAqLowSeverityHigh.setStatus(
        "deprecated"
    )

ciscoLwappSiAqLowRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0, 6)
)
ciscoLwappSiAqLowRev1.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiAqIndex"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11AqiTrapThreshold"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAlarmClear"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiAqLowRev1.setStatus(
        "current"
    )

ciscoLwappSiIdrDeviceRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0, 7)
)
ciscoLwappSiIdrDeviceRev1.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiIdrDeviceType"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrAffectedChannels"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrSeverity"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrClusterId"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAlarmClear"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-SI-MIB", "cLSiIdrPreviousClusterId"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiIdrDeviceRev1.setStatus(
        "current"
    )

ciscoLwappSiSensorCrashRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0, 8)
)
ciscoLwappSiSensorCrashRev1.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApIfSensordOperationalStatus"),
        ("CISCO-LWAPP-SI-MIB", "cLSiApIfSensordErrorCode"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiSensorCrashRev1.setStatus(
        "current"
    )

ciscoLwappSiAqBufferUnavailableRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0, 9)
)
ciscoLwappSiAqBufferUnavailableRev1.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiApAqLimit"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAlarmClear"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiAqBufferUnavailableRev1.setStatus(
        "current"
    )

ciscoLwappSiAqLowSeverityHighRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 0, 10)
)
ciscoLwappSiAqLowSeverityHighRev1.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "cLSiAqIndex"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11AqiTrapThreshold"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11IdrUnclassifiedTrapThreshold"),
        ("CISCO-LWAPP-SI-MIB", "cLSiD11IdrUnclassifiedCurrentSevIndex"),
        ("CISCO-LWAPP-SI-MIB", "cLSiAlarmClear"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiAqLowSeverityHighRev1.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappSiMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 13)
)
ciscoLwappSiMIBNotifGroup.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "ciscoLwappSiAqLow"),
        ("CISCO-LWAPP-SI-MIB", "ciscoLwappSiIdrDevice"),
        ("CISCO-LWAPP-SI-MIB", "ciscoLwappSiSensorCrash"),
        ("CISCO-LWAPP-SI-MIB", "ciscoLwappSiAqBufferUnavailable"),
        ("CISCO-LWAPP-SI-MIB", "ciscoLwappSiAqLowSeverityHigh"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiMIBNotifGroup.setStatus(
        "deprecated"
    )

ciscoLwappSiMIBNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 2, 15)
)
ciscoLwappSiMIBNotifGroupRev1.setObjects(
      *(("CISCO-LWAPP-SI-MIB", "ciscoLwappSiAqLowRev1"),
        ("CISCO-LWAPP-SI-MIB", "ciscoLwappSiIdrDeviceRev1"),
        ("CISCO-LWAPP-SI-MIB", "ciscoLwappSiSensorCrashRev1"),
        ("CISCO-LWAPP-SI-MIB", "ciscoLwappSiAqBufferUnavailableRev1"),
        ("CISCO-LWAPP-SI-MIB", "ciscoLwappSiAqLowSeverityHighRev1"))
)
if mibBuilder.loadTexts:
    ciscoLwappSiMIBNotifGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappApSiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappApSiMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappApSiMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappApSiMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappApSiMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappApSiMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-SI-MIB",
    **{"ciscoLwappSiMIB": ciscoLwappSiMIB,
       "ciscoLwappSiMIBNotifs": ciscoLwappSiMIBNotifs,
       "ciscoLwappSiAqLow": ciscoLwappSiAqLow,
       "ciscoLwappSiIdrDevice": ciscoLwappSiIdrDevice,
       "ciscoLwappSiSensorCrash": ciscoLwappSiSensorCrash,
       "ciscoLwappSiAqBufferUnavailable": ciscoLwappSiAqBufferUnavailable,
       "ciscoLwappSiAqLowSeverityHigh": ciscoLwappSiAqLowSeverityHigh,
       "ciscoLwappSiAqLowRev1": ciscoLwappSiAqLowRev1,
       "ciscoLwappSiIdrDeviceRev1": ciscoLwappSiIdrDeviceRev1,
       "ciscoLwappSiSensorCrashRev1": ciscoLwappSiSensorCrashRev1,
       "ciscoLwappSiAqBufferUnavailableRev1": ciscoLwappSiAqBufferUnavailableRev1,
       "ciscoLwappSiAqLowSeverityHighRev1": ciscoLwappSiAqLowSeverityHighRev1,
       "ciscoLwappSiMIBObjects": ciscoLwappSiMIBObjects,
       "ciscoLwappAirQuality": ciscoLwappAirQuality,
       "cLSiAqTable": cLSiAqTable,
       "cLSiAqEntry": cLSiAqEntry,
       "cLSiAqChannelNumber": cLSiAqChannelNumber,
       "cLSiAqMinIndex": cLSiAqMinIndex,
       "cLSiAqIndex": cLSiAqIndex,
       "cLSiAqTotalChannelPower": cLSiAqTotalChannelPower,
       "cLSiAqTotalChannelDutyCycle": cLSiAqTotalChannelDutyCycle,
       "cLSiAqInterferencePower": cLSiAqInterferencePower,
       "cLSiAqInterferenceDutyCycle": cLSiAqInterferenceDutyCycle,
       "cLSiAqInterferenceDeviceCount": cLSiAqInterferenceDeviceCount,
       "cLSiAqInterfererClassReportCount": cLSiAqInterfererClassReportCount,
       "cLSiAqTimeStamp": cLSiAqTimeStamp,
       "cLSiAqInterferenceClassReportTable": cLSiAqInterferenceClassReportTable,
       "cLSiAqInterferenceClassReportEntry": cLSiAqInterferenceClassReportEntry,
       "cLSiAqInterferenceClassReportIndex": cLSiAqInterferenceClassReportIndex,
       "cLSiAqInterferenceClassReportDeviceClass": cLSiAqInterferenceClassReportDeviceClass,
       "cLSiAqInterferenceClassReportSeverityIndex": cLSiAqInterferenceClassReportSeverityIndex,
       "cLSiAqInterferenceClassReportPower": cLSiAqInterferenceClassReportPower,
       "cLSiAqInterferenceClassReportDutyCycle": cLSiAqInterferenceClassReportDutyCycle,
       "cLSiAqInterferenceClassReportDeviceCount": cLSiAqInterferenceClassReportDeviceCount,
       "ciscoLwappInterference": ciscoLwappInterference,
       "cLSiIdrTable": cLSiIdrTable,
       "cLSiIdrEntry": cLSiIdrEntry,
       "cLSiIdrDeviceId": cLSiIdrDeviceId,
       "cLSiIdrClusterId": cLSiIdrClusterId,
       "cLSiIdrTimeStamp": cLSiIdrTimeStamp,
       "cLSiIdrDeviceType": cLSiIdrDeviceType,
       "cLSiIdrSeverity": cLSiIdrSeverity,
       "cLSiIdrDetectingApMac": cLSiIdrDetectingApMac,
       "cLSiIdrDutyCycle": cLSiIdrDutyCycle,
       "cLSiIdrAntennaId": cLSiIdrAntennaId,
       "cLSiIdrRssi": cLSiIdrRssi,
       "cLSiIdrRadioBandId": cLSiIdrRadioBandId,
       "cLSiIdrAffectedChannels": cLSiIdrAffectedChannels,
       "cLSiIdrDeviceSignatureLen": cLSiIdrDeviceSignatureLen,
       "cLSiIdrDeviceSignature": cLSiIdrDeviceSignature,
       "cLSiIdrClusterTable": cLSiIdrClusterTable,
       "cLSiIdrClusterEntry": cLSiIdrClusterEntry,
       "cLSiIdrClusterRadioBandId": cLSiIdrClusterRadioBandId,
       "cLSiIdrClusterClusterId": cLSiIdrClusterClusterId,
       "cLSiIdrClusterDeviceIndex": cLSiIdrClusterDeviceIndex,
       "cLSiIdrClusterDeviceId": cLSiIdrClusterDeviceId,
       "cLSiIdrClusterTimeStamp": cLSiIdrClusterTimeStamp,
       "cLSiIdrClusterDeviceType": cLSiIdrClusterDeviceType,
       "cLSiIdrClusterSeverity": cLSiIdrClusterSeverity,
       "cLSiIdrClusterDetectingApMac": cLSiIdrClusterDetectingApMac,
       "cLSiIdrClusterDutyCycle": cLSiIdrClusterDutyCycle,
       "cLSiIdrClusterAntennaId": cLSiIdrClusterAntennaId,
       "cLSiIdrClusterRssi": cLSiIdrClusterRssi,
       "cLSiIdrClusterAffectedChannels": cLSiIdrClusterAffectedChannels,
       "cLSiIdrClusterDeviceSignatureLen": cLSiIdrClusterDeviceSignatureLen,
       "cLSiIdrClusterDeviceSignature": cLSiIdrClusterDeviceSignature,
       "cLSiIdrClusterCenterIndex": cLSiIdrClusterCenterIndex,
       "cLSiIdrClusterType": cLSiIdrClusterType,
       "cLSiPersistentDeviceTable": cLSiPersistentDeviceTable,
       "cLSiPersistentDeviceEntry": cLSiPersistentDeviceEntry,
       "cLSiPersistentDeviceId": cLSiPersistentDeviceId,
       "cLSiPersistentDeviceType": cLSiPersistentDeviceType,
       "cLSiPersistentTimeStamp": cLSiPersistentTimeStamp,
       "cLSiPersistentDeviceChanTable": cLSiPersistentDeviceChanTable,
       "cLSiPersistentDeviceChanEntry": cLSiPersistentDeviceChanEntry,
       "cLSiPersistentDeviceChanIndex": cLSiPersistentDeviceChanIndex,
       "cLSiChannelAffected": cLSiChannelAffected,
       "cLSiChannelUtil": cLSiChannelUtil,
       "cLSiChannelRSSI": cLSiChannelRSSI,
       "ciscoLwappSiDot11Band": ciscoLwappSiDot11Band,
       "cLSiDot11BandTable": cLSiDot11BandTable,
       "cLSiDot11BandEntry": cLSiDot11BandEntry,
       "cLSiD11Band": cLSiD11Band,
       "cLSiD11SpectrumIntelligenceEnable": cLSiD11SpectrumIntelligenceEnable,
       "cLSiD11InterferenceDeviceList": cLSiD11InterferenceDeviceList,
       "cLSiD11PollingInterval": cLSiD11PollingInterval,
       "cLSiD11IdrReportingEnable": cLSiD11IdrReportingEnable,
       "cLSiD11AqiTrapEnable": cLSiD11AqiTrapEnable,
       "cLSiD11AqiTrapThreshold": cLSiD11AqiTrapThreshold,
       "cLSiD11IdrTrapEnable": cLSiD11IdrTrapEnable,
       "cLSiD11IdrTrapDeviceList": cLSiD11IdrTrapDeviceList,
       "cLSiD11IdrPersistentDevicePropagation": cLSiD11IdrPersistentDevicePropagation,
       "cLSiD11IdrUnclassifiedTrapEnable": cLSiD11IdrUnclassifiedTrapEnable,
       "cLSiD11IdrUnclassifiedTrapThreshold": cLSiD11IdrUnclassifiedTrapThreshold,
       "cLSiDot11BandEventDrivenRrmTable": cLSiDot11BandEventDrivenRrmTable,
       "cLSiDot11BandEventDrivenRrmEntry": cLSiDot11BandEventDrivenRrmEntry,
       "cLSiD11EventDrivenRrmEnable": cLSiD11EventDrivenRrmEnable,
       "cLSiD11EventDrivenRrmThresLvl": cLSiD11EventDrivenRrmThresLvl,
       "cLSiD11EventDrivenRrmCustomThresVal": cLSiD11EventDrivenRrmCustomThresVal,
       "ciscoLwappSiApIf": ciscoLwappSiApIf,
       "cLSiApIfTable": cLSiApIfTable,
       "cLSiApIfEntry": cLSiApIfEntry,
       "cLSiApIfSpectrumIntelligenceEnable": cLSiApIfSpectrumIntelligenceEnable,
       "cLSiApIfSpectrumCapable": cLSiApIfSpectrumCapable,
       "cLSiApIfRapidUpdateEnable": cLSiApIfRapidUpdateEnable,
       "cLSiApIfDetailSpectrumModeEnable": cLSiApIfDetailSpectrumModeEnable,
       "cLSiApIfSensordOperationalStatus": cLSiApIfSensordOperationalStatus,
       "cLSiApIfNumOfSeActiveConnection": cLSiApIfNumOfSeActiveConnection,
       "cLSiApIfSensordErrorCode": cLSiApIfSensordErrorCode,
       "ciscoLwappSiMIBConform": ciscoLwappSiMIBConform,
       "ciscoLwappSiMIBCompliances": ciscoLwappSiMIBCompliances,
       "ciscoLwappApSiMIBCompliance": ciscoLwappApSiMIBCompliance,
       "ciscoLwappApSiMIBComplianceRev1": ciscoLwappApSiMIBComplianceRev1,
       "ciscoLwappApSiMIBComplianceRev2": ciscoLwappApSiMIBComplianceRev2,
       "ciscoLwappSiMIBGroups": ciscoLwappSiMIBGroups,
       "cLSiApIfConfigGroup": cLSiApIfConfigGroup,
       "cLSiApIfStatusGroup": cLSiApIfStatusGroup,
       "cLSiD11ConfigGroup": cLSiD11ConfigGroup,
       "cLSiAqChannelStatusGroup": cLSiAqChannelStatusGroup,
       "cLSiAqInterferenceClassReportStatusGroup": cLSiAqInterferenceClassReportStatusGroup,
       "cLSiIdrStatusGroup": cLSiIdrStatusGroup,
       "cLSiIdrClusterStatusGroup": cLSiIdrClusterStatusGroup,
       "cLSiD11EventDrivenRrmConfigGroup": cLSiD11EventDrivenRrmConfigGroup,
       "cLSiPersistentDeviceStatusGroup": cLSiPersistentDeviceStatusGroup,
       "cLSiPersistentDeviceChanStatusGroup": cLSiPersistentDeviceChanStatusGroup,
       "cLSiD11ConfigSup1Group": cLSiD11ConfigSup1Group,
       "cLSiD11EventDrivenRrmConfigSup1Group": cLSiD11EventDrivenRrmConfigSup1Group,
       "ciscoLwappSiMIBNotifGroup": ciscoLwappSiMIBNotifGroup,
       "ciscoLwappSiMIBNotifVariableGroup": ciscoLwappSiMIBNotifVariableGroup,
       "ciscoLwappSiMIBNotifGroupRev1": ciscoLwappSiMIBNotifGroupRev1,
       "ciscoLwappSiMIBNotifObjects": ciscoLwappSiMIBNotifObjects,
       "cLSiAlarmClear": cLSiAlarmClear,
       "cLSiIdrPreviousClusterId": cLSiIdrPreviousClusterId,
       "cLSiApAqLimit": cLSiApAqLimit,
       "cLSiD11IdrUnclassifiedCurrentSevIndex": cLSiD11IdrUnclassifiedCurrentSevIndex}
)
