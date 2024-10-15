# SNMP MIB module (CLAB-WIFI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CLAB-WIFI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:41 2024
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

(clabProjWireless,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjWireless")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

clabWIFIMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1)
)
clabWIFIMib.setRevisions(
        ("2017-04-13 00:00",
         "2016-08-03 00:00",
         "2016-03-30 00:00",
         "2015-12-02 00:00",
         "2014-03-11 00:00",
         "2012-01-06 00:00",
         "2010-09-27 00:00",
         "2010-07-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PktErrorRateType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-9"


# MIB Managed Objects in the order of their OIDs

_ClabWIFINotifications_ObjectIdentity = ObjectIdentity
clabWIFINotifications = _ClabWIFINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 0)
)
_ClabWIFIWIFIEventNotifgroup_ObjectIdentity = ObjectIdentity
clabWIFIWIFIEventNotifgroup = _ClabWIFIWIFIEventNotifgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 0, 2)
)


class _ClabWIFIWIFIEventNotifText_Type(SnmpAdminString):
    """Custom type clabWIFIWIFIEventNotifText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClabWIFIWIFIEventNotifText_Type.__name__ = "SnmpAdminString"
_ClabWIFIWIFIEventNotifText_Object = MibScalar
clabWIFIWIFIEventNotifText = _ClabWIFIWIFIEventNotifText_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 0, 2, 1),
    _ClabWIFIWIFIEventNotifText_Type()
)
clabWIFIWIFIEventNotifText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clabWIFIWIFIEventNotifText.setStatus("current")
_ClabWIFIWIFIEventNotifEventId_Type = Unsigned32
_ClabWIFIWIFIEventNotifEventId_Object = MibScalar
clabWIFIWIFIEventNotifEventId = _ClabWIFIWIFIEventNotifEventId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 0, 2, 2),
    _ClabWIFIWIFIEventNotifEventId_Type()
)
clabWIFIWIFIEventNotifEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clabWIFIWIFIEventNotifEventId.setStatus("current")
_ClabWIFIWIFIEventNotifTimeStamp_Type = DateAndTime
_ClabWIFIWIFIEventNotifTimeStamp_Object = MibScalar
clabWIFIWIFIEventNotifTimeStamp = _ClabWIFIWIFIEventNotifTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 0, 2, 3),
    _ClabWIFIWIFIEventNotifTimeStamp_Type()
)
clabWIFIWIFIEventNotifTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clabWIFIWIFIEventNotifTimeStamp.setStatus("current")
_ClabWIFIObjects_ObjectIdentity = ObjectIdentity
clabWIFIObjects = _ClabWIFIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1)
)
_ClabWIFIWiFi_ObjectIdentity = ObjectIdentity
clabWIFIWiFi = _ClabWIFIWiFi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 1)
)
_ClabWIFIWiFiRadioNumberOfEntries_Type = Unsigned32
_ClabWIFIWiFiRadioNumberOfEntries_Object = MibScalar
clabWIFIWiFiRadioNumberOfEntries = _ClabWIFIWiFiRadioNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 1, 1),
    _ClabWIFIWiFiRadioNumberOfEntries_Type()
)
clabWIFIWiFiRadioNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIWiFiRadioNumberOfEntries.setStatus("current")
_ClabWIFIWiFiSSIDNumberOfEntries_Type = Unsigned32
_ClabWIFIWiFiSSIDNumberOfEntries_Object = MibScalar
clabWIFIWiFiSSIDNumberOfEntries = _ClabWIFIWiFiSSIDNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 1, 2),
    _ClabWIFIWiFiSSIDNumberOfEntries_Type()
)
clabWIFIWiFiSSIDNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIWiFiSSIDNumberOfEntries.setStatus("current")
_ClabWIFIWiFiAccessPointNumberOfEntries_Type = Unsigned32
_ClabWIFIWiFiAccessPointNumberOfEntries_Object = MibScalar
clabWIFIWiFiAccessPointNumberOfEntries = _ClabWIFIWiFiAccessPointNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 1, 3),
    _ClabWIFIWiFiAccessPointNumberOfEntries_Type()
)
clabWIFIWiFiAccessPointNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIWiFiAccessPointNumberOfEntries.setStatus("current")
_ClabWIFIWiFiEndPointNumberOfEntries_Type = Unsigned32
_ClabWIFIWiFiEndPointNumberOfEntries_Object = MibScalar
clabWIFIWiFiEndPointNumberOfEntries = _ClabWIFIWiFiEndPointNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 1, 4),
    _ClabWIFIWiFiEndPointNumberOfEntries_Type()
)
clabWIFIWiFiEndPointNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIWiFiEndPointNumberOfEntries.setStatus("current")
_ClabWIFISSIDSteeringEnabled_Type = TruthValue
_ClabWIFISSIDSteeringEnabled_Object = MibScalar
clabWIFISSIDSteeringEnabled = _ClabWIFISSIDSteeringEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 1, 5),
    _ClabWIFISSIDSteeringEnabled_Type()
)
clabWIFISSIDSteeringEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFISSIDSteeringEnabled.setStatus("current")
_ClabWIFICommitSettings_Type = TruthValue
_ClabWIFICommitSettings_Object = MibScalar
clabWIFICommitSettings = _ClabWIFICommitSettings_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 1, 6),
    _ClabWIFICommitSettings_Type()
)
clabWIFICommitSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFICommitSettings.setStatus("current")
_ClabWIFIRadioTable_Object = MibTable
clabWIFIRadioTable = _ClabWIFIRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    clabWIFIRadioTable.setStatus("current")
_ClabWIFIRadioEntry_Object = MibTableRow
clabWIFIRadioEntry = _ClabWIFIRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1)
)
clabWIFIRadioEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIRadioId"),
)
if mibBuilder.loadTexts:
    clabWIFIRadioEntry.setStatus("current")
_ClabWIFIRadioId_Type = InterfaceIndex
_ClabWIFIRadioId_Object = MibTableColumn
clabWIFIRadioId = _ClabWIFIRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 1),
    _ClabWIFIRadioId_Type()
)
clabWIFIRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIRadioId.setStatus("current")
_ClabWIFIRadioEnable_Type = TruthValue
_ClabWIFIRadioEnable_Object = MibTableColumn
clabWIFIRadioEnable = _ClabWIFIRadioEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 2),
    _ClabWIFIRadioEnable_Type()
)
clabWIFIRadioEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioEnable.setStatus("current")


class _ClabWIFIRadioStatus_Type(Integer32):
    """Custom type clabWIFIRadioStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("error", 8),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("unknown", 4),
          ("up", 1))
    )


_ClabWIFIRadioStatus_Type.__name__ = "Integer32"
_ClabWIFIRadioStatus_Object = MibTableColumn
clabWIFIRadioStatus = _ClabWIFIRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 3),
    _ClabWIFIRadioStatus_Type()
)
clabWIFIRadioStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatus.setStatus("current")


class _ClabWIFIRadioAlias_Type(SnmpAdminString):
    """Custom type clabWIFIRadioAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabWIFIRadioAlias_Type.__name__ = "SnmpAdminString"
_ClabWIFIRadioAlias_Object = MibTableColumn
clabWIFIRadioAlias = _ClabWIFIRadioAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 4),
    _ClabWIFIRadioAlias_Type()
)
clabWIFIRadioAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioAlias.setStatus("current")


class _ClabWIFIRadioName_Type(SnmpAdminString):
    """Custom type clabWIFIRadioName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabWIFIRadioName_Type.__name__ = "SnmpAdminString"
_ClabWIFIRadioName_Object = MibTableColumn
clabWIFIRadioName = _ClabWIFIRadioName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 5),
    _ClabWIFIRadioName_Type()
)
clabWIFIRadioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioName.setStatus("current")
_ClabWIFIRadioLastChange_Type = Unsigned32
_ClabWIFIRadioLastChange_Object = MibTableColumn
clabWIFIRadioLastChange = _ClabWIFIRadioLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 6),
    _ClabWIFIRadioLastChange_Type()
)
clabWIFIRadioLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioLastChange.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioLastChange.setUnits("seconds")


class _ClabWIFIRadioLowerLayers_Type(SnmpAdminString):
    """Custom type clabWIFIRadioLowerLayers based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ClabWIFIRadioLowerLayers_Type.__name__ = "SnmpAdminString"
_ClabWIFIRadioLowerLayers_Object = MibTableColumn
clabWIFIRadioLowerLayers = _ClabWIFIRadioLowerLayers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 7),
    _ClabWIFIRadioLowerLayers_Type()
)
clabWIFIRadioLowerLayers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioLowerLayers.setStatus("current")
_ClabWIFIRadioUpstream_Type = TruthValue
_ClabWIFIRadioUpstream_Object = MibTableColumn
clabWIFIRadioUpstream = _ClabWIFIRadioUpstream_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 8),
    _ClabWIFIRadioUpstream_Type()
)
clabWIFIRadioUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioUpstream.setStatus("current")
_ClabWIFIRadioMaxBitRate_Type = Unsigned32
_ClabWIFIRadioMaxBitRate_Object = MibTableColumn
clabWIFIRadioMaxBitRate = _ClabWIFIRadioMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 9),
    _ClabWIFIRadioMaxBitRate_Type()
)
clabWIFIRadioMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioMaxBitRate.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioMaxBitRate.setUnits("Mbps")
_ClabWIFIRadioSupportedFrequencyBands_Type = SnmpAdminString
_ClabWIFIRadioSupportedFrequencyBands_Object = MibTableColumn
clabWIFIRadioSupportedFrequencyBands = _ClabWIFIRadioSupportedFrequencyBands_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 10),
    _ClabWIFIRadioSupportedFrequencyBands_Type()
)
clabWIFIRadioSupportedFrequencyBands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioSupportedFrequencyBands.setStatus("current")


class _ClabWIFIRadioOperatingFrequencyBand_Type(Integer32):
    """Custom type clabWIFIRadioOperatingFrequencyBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("n2dot4Ghz", 1),
          ("n5Ghz", 2))
    )


_ClabWIFIRadioOperatingFrequencyBand_Type.__name__ = "Integer32"
_ClabWIFIRadioOperatingFrequencyBand_Object = MibTableColumn
clabWIFIRadioOperatingFrequencyBand = _ClabWIFIRadioOperatingFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 11),
    _ClabWIFIRadioOperatingFrequencyBand_Type()
)
clabWIFIRadioOperatingFrequencyBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioOperatingFrequencyBand.setStatus("current")
_ClabWIFIRadioSupportedStandards_Type = SnmpAdminString
_ClabWIFIRadioSupportedStandards_Object = MibTableColumn
clabWIFIRadioSupportedStandards = _ClabWIFIRadioSupportedStandards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 12),
    _ClabWIFIRadioSupportedStandards_Type()
)
clabWIFIRadioSupportedStandards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioSupportedStandards.setStatus("current")


class _ClabWIFIRadioOperatingStandards_Type(Integer32):
    """Custom type clabWIFIRadioOperatingStandards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("ac", 6),
          ("b", 2),
          ("g", 3),
          ("n", 5))
    )


_ClabWIFIRadioOperatingStandards_Type.__name__ = "Integer32"
_ClabWIFIRadioOperatingStandards_Object = MibTableColumn
clabWIFIRadioOperatingStandards = _ClabWIFIRadioOperatingStandards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 13),
    _ClabWIFIRadioOperatingStandards_Type()
)
clabWIFIRadioOperatingStandards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioOperatingStandards.setStatus("current")


class _ClabWIFIRadioPossibleChannels_Type(SnmpAdminString):
    """Custom type clabWIFIRadioPossibleChannels based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ClabWIFIRadioPossibleChannels_Type.__name__ = "SnmpAdminString"
_ClabWIFIRadioPossibleChannels_Object = MibTableColumn
clabWIFIRadioPossibleChannels = _ClabWIFIRadioPossibleChannels_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 14),
    _ClabWIFIRadioPossibleChannels_Type()
)
clabWIFIRadioPossibleChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioPossibleChannels.setStatus("current")


class _ClabWIFIRadioChannelsInUse_Type(SnmpAdminString):
    """Custom type clabWIFIRadioChannelsInUse based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ClabWIFIRadioChannelsInUse_Type.__name__ = "SnmpAdminString"
_ClabWIFIRadioChannelsInUse_Object = MibTableColumn
clabWIFIRadioChannelsInUse = _ClabWIFIRadioChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 15),
    _ClabWIFIRadioChannelsInUse_Type()
)
clabWIFIRadioChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelsInUse.setStatus("current")


class _ClabWIFIRadioChannel_Type(Unsigned32):
    """Custom type clabWIFIRadioChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClabWIFIRadioChannel_Type.__name__ = "Unsigned32"
_ClabWIFIRadioChannel_Object = MibTableColumn
clabWIFIRadioChannel = _ClabWIFIRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 16),
    _ClabWIFIRadioChannel_Type()
)
clabWIFIRadioChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioChannel.setStatus("current")
_ClabWIFIRadioAutoChannelSupported_Type = TruthValue
_ClabWIFIRadioAutoChannelSupported_Object = MibTableColumn
clabWIFIRadioAutoChannelSupported = _ClabWIFIRadioAutoChannelSupported_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 17),
    _ClabWIFIRadioAutoChannelSupported_Type()
)
clabWIFIRadioAutoChannelSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioAutoChannelSupported.setStatus("current")
_ClabWIFIRadioAutoChannelEnable_Type = TruthValue
_ClabWIFIRadioAutoChannelEnable_Object = MibTableColumn
clabWIFIRadioAutoChannelEnable = _ClabWIFIRadioAutoChannelEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 18),
    _ClabWIFIRadioAutoChannelEnable_Type()
)
clabWIFIRadioAutoChannelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioAutoChannelEnable.setStatus("current")
_ClabWIFIRadioAutoChannelRefreshPeriod_Type = Unsigned32
_ClabWIFIRadioAutoChannelRefreshPeriod_Object = MibTableColumn
clabWIFIRadioAutoChannelRefreshPeriod = _ClabWIFIRadioAutoChannelRefreshPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 19),
    _ClabWIFIRadioAutoChannelRefreshPeriod_Type()
)
clabWIFIRadioAutoChannelRefreshPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioAutoChannelRefreshPeriod.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioAutoChannelRefreshPeriod.setUnits("seconds")


class _ClabWIFIRadioOperatingChannelBandwidth_Type(Integer32):
    """Custom type clabWIFIRadioOperatingChannelBandwidth based on Integer32"""
    defaultValue = 6

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
        *(("ac160MHz", 4),
          ("ac80MHz", 3),
          ("ac80plus80MHz", 5),
          ("auto", 6),
          ("n20MHz", 1),
          ("n40MHz", 2))
    )


_ClabWIFIRadioOperatingChannelBandwidth_Type.__name__ = "Integer32"
_ClabWIFIRadioOperatingChannelBandwidth_Object = MibTableColumn
clabWIFIRadioOperatingChannelBandwidth = _ClabWIFIRadioOperatingChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 20),
    _ClabWIFIRadioOperatingChannelBandwidth_Type()
)
clabWIFIRadioOperatingChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioOperatingChannelBandwidth.setStatus("current")


class _ClabWIFIRadioExtensionChannel_Type(Integer32):
    """Custom type clabWIFIRadioExtensionChannel based on Integer32"""
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
        *(("aboveControlChannel", 1),
          ("auto", 3),
          ("belowControlChannel", 2))
    )


_ClabWIFIRadioExtensionChannel_Type.__name__ = "Integer32"
_ClabWIFIRadioExtensionChannel_Object = MibTableColumn
clabWIFIRadioExtensionChannel = _ClabWIFIRadioExtensionChannel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 21),
    _ClabWIFIRadioExtensionChannel_Type()
)
clabWIFIRadioExtensionChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioExtensionChannel.setStatus("current")


class _ClabWIFIRadioGuardInterval_Type(Integer32):
    """Custom type clabWIFIRadioGuardInterval based on Integer32"""
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
        *(("auto", 3),
          ("n400nsec", 1),
          ("n800nsec", 2))
    )


_ClabWIFIRadioGuardInterval_Type.__name__ = "Integer32"
_ClabWIFIRadioGuardInterval_Object = MibTableColumn
clabWIFIRadioGuardInterval = _ClabWIFIRadioGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 22),
    _ClabWIFIRadioGuardInterval_Type()
)
clabWIFIRadioGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioGuardInterval.setStatus("current")


class _ClabWIFIRadioMCS_Type(Integer32):
    """Custom type clabWIFIRadioMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_ClabWIFIRadioMCS_Type.__name__ = "Integer32"
_ClabWIFIRadioMCS_Object = MibTableColumn
clabWIFIRadioMCS = _ClabWIFIRadioMCS_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 23),
    _ClabWIFIRadioMCS_Type()
)
clabWIFIRadioMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioMCS.setStatus("current")


class _ClabWIFIRadioTransmitPowerSupported_Type(SnmpAdminString):
    """Custom type clabWIFIRadioTransmitPowerSupported based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabWIFIRadioTransmitPowerSupported_Type.__name__ = "SnmpAdminString"
_ClabWIFIRadioTransmitPowerSupported_Object = MibTableColumn
clabWIFIRadioTransmitPowerSupported = _ClabWIFIRadioTransmitPowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 24),
    _ClabWIFIRadioTransmitPowerSupported_Type()
)
clabWIFIRadioTransmitPowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioTransmitPowerSupported.setStatus("current")


class _ClabWIFIRadioTransmitPower_Type(Unsigned32):
    """Custom type clabWIFIRadioTransmitPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ClabWIFIRadioTransmitPower_Type.__name__ = "Unsigned32"
_ClabWIFIRadioTransmitPower_Object = MibTableColumn
clabWIFIRadioTransmitPower = _ClabWIFIRadioTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 25),
    _ClabWIFIRadioTransmitPower_Type()
)
clabWIFIRadioTransmitPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioTransmitPower.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioTransmitPower.setUnits("percentage")
_ClabWIFIRadioIEEE80211hSupported_Type = TruthValue
_ClabWIFIRadioIEEE80211hSupported_Object = MibTableColumn
clabWIFIRadioIEEE80211hSupported = _ClabWIFIRadioIEEE80211hSupported_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 26),
    _ClabWIFIRadioIEEE80211hSupported_Type()
)
clabWIFIRadioIEEE80211hSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioIEEE80211hSupported.setStatus("current")
_ClabWIFIRadioIEEE80211hEnabled_Type = TruthValue
_ClabWIFIRadioIEEE80211hEnabled_Object = MibTableColumn
clabWIFIRadioIEEE80211hEnabled = _ClabWIFIRadioIEEE80211hEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 27),
    _ClabWIFIRadioIEEE80211hEnabled_Type()
)
clabWIFIRadioIEEE80211hEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioIEEE80211hEnabled.setStatus("current")
_ClabWIFIRadioRegulatoryDomain_Type = SnmpAdminString
_ClabWIFIRadioRegulatoryDomain_Object = MibTableColumn
clabWIFIRadioRegulatoryDomain = _ClabWIFIRadioRegulatoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 28),
    _ClabWIFIRadioRegulatoryDomain_Type()
)
clabWIFIRadioRegulatoryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioRegulatoryDomain.setStatus("current")


class _ClabWIFIRadioNonContiguousChannel_Type(Unsigned32):
    """Custom type clabWIFIRadioNonContiguousChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClabWIFIRadioNonContiguousChannel_Type.__name__ = "Unsigned32"
_ClabWIFIRadioNonContiguousChannel_Object = MibTableColumn
clabWIFIRadioNonContiguousChannel = _ClabWIFIRadioNonContiguousChannel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 29),
    _ClabWIFIRadioNonContiguousChannel_Type()
)
clabWIFIRadioNonContiguousChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioNonContiguousChannel.setStatus("current")
_ClabWIFIRadioCarrierSenseThresholdInUse_Type = Integer32
_ClabWIFIRadioCarrierSenseThresholdInUse_Object = MibTableColumn
clabWIFIRadioCarrierSenseThresholdInUse = _ClabWIFIRadioCarrierSenseThresholdInUse_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 30),
    _ClabWIFIRadioCarrierSenseThresholdInUse_Type()
)
clabWIFIRadioCarrierSenseThresholdInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioCarrierSenseThresholdInUse.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioCarrierSenseThresholdInUse.setUnits("dBm")
_ClabWIFIRadioCarrierSenseThresholdRange_Type = Integer32
_ClabWIFIRadioCarrierSenseThresholdRange_Object = MibTableColumn
clabWIFIRadioCarrierSenseThresholdRange = _ClabWIFIRadioCarrierSenseThresholdRange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 31),
    _ClabWIFIRadioCarrierSenseThresholdRange_Type()
)
clabWIFIRadioCarrierSenseThresholdRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioCarrierSenseThresholdRange.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIRadioCarrierSenseThresholdRange.setUnits("dBm")
_ClabWIFIRadioStatsChanUtilization_Type = Unsigned32
_ClabWIFIRadioStatsChanUtilization_Object = MibTableColumn
clabWIFIRadioStatsChanUtilization = _ClabWIFIRadioStatsChanUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 32),
    _ClabWIFIRadioStatsChanUtilization_Type()
)
clabWIFIRadioStatsChanUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsChanUtilization.setStatus("deprecated")
_ClabWIFIRadioRtsCtsExchange_Type = Integer32
_ClabWIFIRadioRtsCtsExchange_Object = MibTableColumn
clabWIFIRadioRtsCtsExchange = _ClabWIFIRadioRtsCtsExchange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 33),
    _ClabWIFIRadioRtsCtsExchange_Type()
)
clabWIFIRadioRtsCtsExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioRtsCtsExchange.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioRtsCtsExchange.setUnits("bytes")
_ClabWIFIRadioFrameAggregationLevel_Type = Unsigned32
_ClabWIFIRadioFrameAggregationLevel_Object = MibTableColumn
clabWIFIRadioFrameAggregationLevel = _ClabWIFIRadioFrameAggregationLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 34),
    _ClabWIFIRadioFrameAggregationLevel_Type()
)
clabWIFIRadioFrameAggregationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIRadioFrameAggregationLevel.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIRadioFrameAggregationLevel.setUnits("frames")
_ClabWIFIRadioThroughput_Type = Unsigned32
_ClabWIFIRadioThroughput_Object = MibTableColumn
clabWIFIRadioThroughput = _ClabWIFIRadioThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 35),
    _ClabWIFIRadioThroughput_Type()
)
clabWIFIRadioThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioThroughput.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIRadioThroughput.setUnits("Mbps")
_ClabWIFIRadioPktErrorRateSTA_Type = PktErrorRateType
_ClabWIFIRadioPktErrorRateSTA_Object = MibTableColumn
clabWIFIRadioPktErrorRateSTA = _ClabWIFIRadioPktErrorRateSTA_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 36),
    _ClabWIFIRadioPktErrorRateSTA_Type()
)
clabWIFIRadioPktErrorRateSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioPktErrorRateSTA.setStatus("deprecated")


class _ClabWIFIRadioRetryLimit_Type(Unsigned32):
    """Custom type clabWIFIRadioRetryLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ClabWIFIRadioRetryLimit_Type.__name__ = "Unsigned32"
_ClabWIFIRadioRetryLimit_Object = MibTableColumn
clabWIFIRadioRetryLimit = _ClabWIFIRadioRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 37),
    _ClabWIFIRadioRetryLimit_Type()
)
clabWIFIRadioRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioRetryLimit.setStatus("current")


class _ClabWIFIRadioCCARequest_Type(OctetString):
    """Custom type clabWIFIRadioCCARequest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_ClabWIFIRadioCCARequest_Type.__name__ = "OctetString"
_ClabWIFIRadioCCARequest_Object = MibTableColumn
clabWIFIRadioCCARequest = _ClabWIFIRadioCCARequest_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 38),
    _ClabWIFIRadioCCARequest_Type()
)
clabWIFIRadioCCARequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioCCARequest.setStatus("current")


class _ClabWIFIRadioRPIHistogramRequest_Type(OctetString):
    """Custom type clabWIFIRadioRPIHistogramRequest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_ClabWIFIRadioRPIHistogramRequest_Type.__name__ = "OctetString"
_ClabWIFIRadioRPIHistogramRequest_Object = MibTableColumn
clabWIFIRadioRPIHistogramRequest = _ClabWIFIRadioRPIHistogramRequest_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 39),
    _ClabWIFIRadioRPIHistogramRequest_Type()
)
clabWIFIRadioRPIHistogramRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioRPIHistogramRequest.setStatus("current")
_ClabWIFIRadioFragmentationThreshold_Type = Unsigned32
_ClabWIFIRadioFragmentationThreshold_Object = MibTableColumn
clabWIFIRadioFragmentationThreshold = _ClabWIFIRadioFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 40),
    _ClabWIFIRadioFragmentationThreshold_Type()
)
clabWIFIRadioFragmentationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioFragmentationThreshold.setStatus("current")
_ClabWIFIRadioRTSThreshold_Type = Unsigned32
_ClabWIFIRadioRTSThreshold_Object = MibTableColumn
clabWIFIRadioRTSThreshold = _ClabWIFIRadioRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 41),
    _ClabWIFIRadioRTSThreshold_Type()
)
clabWIFIRadioRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioRTSThreshold.setStatus("current")
_ClabWIFIRadioLongRetryLimit_Type = Unsigned32
_ClabWIFIRadioLongRetryLimit_Object = MibTableColumn
clabWIFIRadioLongRetryLimit = _ClabWIFIRadioLongRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 42),
    _ClabWIFIRadioLongRetryLimit_Type()
)
clabWIFIRadioLongRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioLongRetryLimit.setStatus("current")
_ClabWIFIRadioBeaconPeriod_Type = Unsigned32
_ClabWIFIRadioBeaconPeriod_Object = MibTableColumn
clabWIFIRadioBeaconPeriod = _ClabWIFIRadioBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 43),
    _ClabWIFIRadioBeaconPeriod_Type()
)
clabWIFIRadioBeaconPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioBeaconPeriod.setStatus("current")
_ClabWIFIRadioDTIMPeriod_Type = Unsigned32
_ClabWIFIRadioDTIMPeriod_Object = MibTableColumn
clabWIFIRadioDTIMPeriod = _ClabWIFIRadioDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 44),
    _ClabWIFIRadioDTIMPeriod_Type()
)
clabWIFIRadioDTIMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioDTIMPeriod.setStatus("current")
_ClabWIFIRadioPacketAggregationEnable_Type = TruthValue
_ClabWIFIRadioPacketAggregationEnable_Object = MibTableColumn
clabWIFIRadioPacketAggregationEnable = _ClabWIFIRadioPacketAggregationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 45),
    _ClabWIFIRadioPacketAggregationEnable_Type()
)
clabWIFIRadioPacketAggregationEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioPacketAggregationEnable.setStatus("current")
_ClabWIFIRadioBasicDataTransmitRates_Type = SnmpAdminString
_ClabWIFIRadioBasicDataTransmitRates_Object = MibTableColumn
clabWIFIRadioBasicDataTransmitRates = _ClabWIFIRadioBasicDataTransmitRates_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 46),
    _ClabWIFIRadioBasicDataTransmitRates_Type()
)
clabWIFIRadioBasicDataTransmitRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioBasicDataTransmitRates.setStatus("current")
_ClabWIFIRadioOperationalDataTransmitRates_Type = SnmpAdminString
_ClabWIFIRadioOperationalDataTransmitRates_Object = MibTableColumn
clabWIFIRadioOperationalDataTransmitRates = _ClabWIFIRadioOperationalDataTransmitRates_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 47),
    _ClabWIFIRadioOperationalDataTransmitRates_Type()
)
clabWIFIRadioOperationalDataTransmitRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioOperationalDataTransmitRates.setStatus("current")
_ClabWIFIRadioSupportedDataTransmitRates_Type = SnmpAdminString
_ClabWIFIRadioSupportedDataTransmitRates_Object = MibTableColumn
clabWIFIRadioSupportedDataTransmitRates = _ClabWIFIRadioSupportedDataTransmitRates_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 48),
    _ClabWIFIRadioSupportedDataTransmitRates_Type()
)
clabWIFIRadioSupportedDataTransmitRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioSupportedDataTransmitRates.setStatus("current")
_ClabWIFIRadioCarrierSenseThresholdRangeMin_Type = Integer32
_ClabWIFIRadioCarrierSenseThresholdRangeMin_Object = MibTableColumn
clabWIFIRadioCarrierSenseThresholdRangeMin = _ClabWIFIRadioCarrierSenseThresholdRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 49),
    _ClabWIFIRadioCarrierSenseThresholdRangeMin_Type()
)
clabWIFIRadioCarrierSenseThresholdRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioCarrierSenseThresholdRangeMin.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioCarrierSenseThresholdRangeMin.setUnits("dBm")
_ClabWIFIRadioCarrierSenseThresholdRangeMax_Type = Integer32
_ClabWIFIRadioCarrierSenseThresholdRangeMax_Object = MibTableColumn
clabWIFIRadioCarrierSenseThresholdRangeMax = _ClabWIFIRadioCarrierSenseThresholdRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 50),
    _ClabWIFIRadioCarrierSenseThresholdRangeMax_Type()
)
clabWIFIRadioCarrierSenseThresholdRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioCarrierSenseThresholdRangeMax.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioCarrierSenseThresholdRangeMax.setUnits("dBm")


class _ClabWIFIRadioCCAReport_Type(OctetString):
    """Custom type clabWIFIRadioCCAReport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_ClabWIFIRadioCCAReport_Type.__name__ = "OctetString"
_ClabWIFIRadioCCAReport_Object = MibTableColumn
clabWIFIRadioCCAReport = _ClabWIFIRadioCCAReport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 51),
    _ClabWIFIRadioCCAReport_Type()
)
clabWIFIRadioCCAReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioCCAReport.setStatus("current")


class _ClabWIFIRadioRPIHistogramReport_Type(OctetString):
    """Custom type clabWIFIRadioRPIHistogramReport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_ClabWIFIRadioRPIHistogramReport_Type.__name__ = "OctetString"
_ClabWIFIRadioRPIHistogramReport_Object = MibTableColumn
clabWIFIRadioRPIHistogramReport = _ClabWIFIRadioRPIHistogramReport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 52),
    _ClabWIFIRadioRPIHistogramReport_Type()
)
clabWIFIRadioRPIHistogramReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioRPIHistogramReport.setStatus("current")


class _ClabWIFIRadioPreambleType_Type(Integer32):
    """Custom type clabWIFIRadioPreambleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("long", 2),
          ("short", 1))
    )


_ClabWIFIRadioPreambleType_Type.__name__ = "Integer32"
_ClabWIFIRadioPreambleType_Object = MibTableColumn
clabWIFIRadioPreambleType = _ClabWIFIRadioPreambleType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 2, 1, 53),
    _ClabWIFIRadioPreambleType_Type()
)
clabWIFIRadioPreambleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioPreambleType.setStatus("current")
_ClabWIFIRadioStatsTable_Object = MibTable
clabWIFIRadioStatsTable = _ClabWIFIRadioStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    clabWIFIRadioStatsTable.setStatus("current")
_ClabWIFIRadioStatsEntry_Object = MibTableRow
clabWIFIRadioStatsEntry = _ClabWIFIRadioStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1)
)
clabWIFIRadioStatsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIRadioId"),
)
if mibBuilder.loadTexts:
    clabWIFIRadioStatsEntry.setStatus("current")
_ClabWIFIRadioStatsBytesSent_Type = Counter64
_ClabWIFIRadioStatsBytesSent_Object = MibTableColumn
clabWIFIRadioStatsBytesSent = _ClabWIFIRadioStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 1),
    _ClabWIFIRadioStatsBytesSent_Type()
)
clabWIFIRadioStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsBytesSent.setStatus("current")
_ClabWIFIRadioStatsBytesReceived_Type = Counter64
_ClabWIFIRadioStatsBytesReceived_Object = MibTableColumn
clabWIFIRadioStatsBytesReceived = _ClabWIFIRadioStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 2),
    _ClabWIFIRadioStatsBytesReceived_Type()
)
clabWIFIRadioStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsBytesReceived.setStatus("current")
_ClabWIFIRadioStatsPacketsSent_Type = Counter64
_ClabWIFIRadioStatsPacketsSent_Object = MibTableColumn
clabWIFIRadioStatsPacketsSent = _ClabWIFIRadioStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 3),
    _ClabWIFIRadioStatsPacketsSent_Type()
)
clabWIFIRadioStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsPacketsSent.setStatus("current")
_ClabWIFIRadioStatsPacketsReceived_Type = Counter64
_ClabWIFIRadioStatsPacketsReceived_Object = MibTableColumn
clabWIFIRadioStatsPacketsReceived = _ClabWIFIRadioStatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 4),
    _ClabWIFIRadioStatsPacketsReceived_Type()
)
clabWIFIRadioStatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsPacketsReceived.setStatus("current")
_ClabWIFIRadioStatsErrorsSent_Type = Counter32
_ClabWIFIRadioStatsErrorsSent_Object = MibTableColumn
clabWIFIRadioStatsErrorsSent = _ClabWIFIRadioStatsErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 5),
    _ClabWIFIRadioStatsErrorsSent_Type()
)
clabWIFIRadioStatsErrorsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsErrorsSent.setStatus("current")
_ClabWIFIRadioStatsErrorsReceived_Type = Counter32
_ClabWIFIRadioStatsErrorsReceived_Object = MibTableColumn
clabWIFIRadioStatsErrorsReceived = _ClabWIFIRadioStatsErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 6),
    _ClabWIFIRadioStatsErrorsReceived_Type()
)
clabWIFIRadioStatsErrorsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsErrorsReceived.setStatus("current")
_ClabWIFIRadioStatsDiscardPacketsSent_Type = Counter32
_ClabWIFIRadioStatsDiscardPacketsSent_Object = MibTableColumn
clabWIFIRadioStatsDiscardPacketsSent = _ClabWIFIRadioStatsDiscardPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 7),
    _ClabWIFIRadioStatsDiscardPacketsSent_Type()
)
clabWIFIRadioStatsDiscardPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsDiscardPacketsSent.setStatus("current")
_ClabWIFIRadioStatsDiscardPacketsReceived_Type = Counter32
_ClabWIFIRadioStatsDiscardPacketsReceived_Object = MibTableColumn
clabWIFIRadioStatsDiscardPacketsReceived = _ClabWIFIRadioStatsDiscardPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 8),
    _ClabWIFIRadioStatsDiscardPacketsReceived_Type()
)
clabWIFIRadioStatsDiscardPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsDiscardPacketsReceived.setStatus("current")
_ClabWIFIRadioStatsPLCPErrorCount_Type = Counter32
_ClabWIFIRadioStatsPLCPErrorCount_Object = MibTableColumn
clabWIFIRadioStatsPLCPErrorCount = _ClabWIFIRadioStatsPLCPErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 9),
    _ClabWIFIRadioStatsPLCPErrorCount_Type()
)
clabWIFIRadioStatsPLCPErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsPLCPErrorCount.setStatus("current")
_ClabWIFIRadioStatsFCSErrorCount_Type = Counter32
_ClabWIFIRadioStatsFCSErrorCount_Object = MibTableColumn
clabWIFIRadioStatsFCSErrorCount = _ClabWIFIRadioStatsFCSErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 10),
    _ClabWIFIRadioStatsFCSErrorCount_Type()
)
clabWIFIRadioStatsFCSErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsFCSErrorCount.setStatus("current")
_ClabWIFIRadioStatsInvalidMACCount_Type = Counter32
_ClabWIFIRadioStatsInvalidMACCount_Object = MibTableColumn
clabWIFIRadioStatsInvalidMACCount = _ClabWIFIRadioStatsInvalidMACCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 11),
    _ClabWIFIRadioStatsInvalidMACCount_Type()
)
clabWIFIRadioStatsInvalidMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsInvalidMACCount.setStatus("current")
_ClabWIFIRadioStatsPacketsOtherReceived_Type = Counter32
_ClabWIFIRadioStatsPacketsOtherReceived_Object = MibTableColumn
clabWIFIRadioStatsPacketsOtherReceived = _ClabWIFIRadioStatsPacketsOtherReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 12),
    _ClabWIFIRadioStatsPacketsOtherReceived_Type()
)
clabWIFIRadioStatsPacketsOtherReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsPacketsOtherReceived.setStatus("current")
_ClabWIFIRadioStatsNoise_Type = Integer32
_ClabWIFIRadioStatsNoise_Object = MibTableColumn
clabWIFIRadioStatsNoise = _ClabWIFIRadioStatsNoise_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 13),
    _ClabWIFIRadioStatsNoise_Type()
)
clabWIFIRadioStatsNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsNoise.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsNoise.setUnits("dBm")
_ClabWIFIRadioStatsFramesRetransmissionsSent_Type = Counter64
_ClabWIFIRadioStatsFramesRetransmissionsSent_Object = MibTableColumn
clabWIFIRadioStatsFramesRetransmissionsSent = _ClabWIFIRadioStatsFramesRetransmissionsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 14),
    _ClabWIFIRadioStatsFramesRetransmissionsSent_Type()
)
clabWIFIRadioStatsFramesRetransmissionsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsFramesRetransmissionsSent.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsFramesRetransmissionsSent.setUnits("frames")
_ClabWIFIRadioStatsFramesDuplicatedReceived_Type = Counter64
_ClabWIFIRadioStatsFramesDuplicatedReceived_Object = MibTableColumn
clabWIFIRadioStatsFramesDuplicatedReceived = _ClabWIFIRadioStatsFramesDuplicatedReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 15),
    _ClabWIFIRadioStatsFramesDuplicatedReceived_Type()
)
clabWIFIRadioStatsFramesDuplicatedReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsFramesDuplicatedReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsFramesDuplicatedReceived.setUnits("frames")


class _ClabWIFIRadioStatsChannelUtilization_Type(Unsigned32):
    """Custom type clabWIFIRadioStatsChannelUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ClabWIFIRadioStatsChannelUtilization_Type.__name__ = "Unsigned32"
_ClabWIFIRadioStatsChannelUtilization_Object = MibTableColumn
clabWIFIRadioStatsChannelUtilization = _ClabWIFIRadioStatsChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 3, 1, 16),
    _ClabWIFIRadioStatsChannelUtilization_Type()
)
clabWIFIRadioStatsChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsChannelUtilization.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioStatsChannelUtilization.setUnits("percentage")
_ClabWIFISSIDTable_Object = MibTable
clabWIFISSIDTable = _ClabWIFISSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    clabWIFISSIDTable.setStatus("current")
_ClabWIFISSIDEntry_Object = MibTableRow
clabWIFISSIDEntry = _ClabWIFISSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1)
)
clabWIFISSIDEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFISSIDId"),
)
if mibBuilder.loadTexts:
    clabWIFISSIDEntry.setStatus("current")
_ClabWIFISSIDId_Type = InterfaceIndex
_ClabWIFISSIDId_Object = MibTableColumn
clabWIFISSIDId = _ClabWIFISSIDId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 1),
    _ClabWIFISSIDId_Type()
)
clabWIFISSIDId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFISSIDId.setStatus("current")
_ClabWIFISSIDEnable_Type = TruthValue
_ClabWIFISSIDEnable_Object = MibTableColumn
clabWIFISSIDEnable = _ClabWIFISSIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 2),
    _ClabWIFISSIDEnable_Type()
)
clabWIFISSIDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDEnable.setStatus("current")


class _ClabWIFISSIDStatus_Type(Integer32):
    """Custom type clabWIFISSIDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("error", 8),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("unknown", 4),
          ("up", 1))
    )


_ClabWIFISSIDStatus_Type.__name__ = "Integer32"
_ClabWIFISSIDStatus_Object = MibTableColumn
clabWIFISSIDStatus = _ClabWIFISSIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 3),
    _ClabWIFISSIDStatus_Type()
)
clabWIFISSIDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatus.setStatus("current")


class _ClabWIFISSIDAlias_Type(SnmpAdminString):
    """Custom type clabWIFISSIDAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabWIFISSIDAlias_Type.__name__ = "SnmpAdminString"
_ClabWIFISSIDAlias_Object = MibTableColumn
clabWIFISSIDAlias = _ClabWIFISSIDAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 4),
    _ClabWIFISSIDAlias_Type()
)
clabWIFISSIDAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDAlias.setStatus("current")


class _ClabWIFISSIDName_Type(SnmpAdminString):
    """Custom type clabWIFISSIDName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabWIFISSIDName_Type.__name__ = "SnmpAdminString"
_ClabWIFISSIDName_Object = MibTableColumn
clabWIFISSIDName = _ClabWIFISSIDName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 5),
    _ClabWIFISSIDName_Type()
)
clabWIFISSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDName.setStatus("current")
_ClabWIFISSIDLastChange_Type = Unsigned32
_ClabWIFISSIDLastChange_Object = MibTableColumn
clabWIFISSIDLastChange = _ClabWIFISSIDLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 6),
    _ClabWIFISSIDLastChange_Type()
)
clabWIFISSIDLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDLastChange.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFISSIDLastChange.setUnits("seconds")


class _ClabWIFISSIDLowerLayers_Type(SnmpAdminString):
    """Custom type clabWIFISSIDLowerLayers based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ClabWIFISSIDLowerLayers_Type.__name__ = "SnmpAdminString"
_ClabWIFISSIDLowerLayers_Object = MibTableColumn
clabWIFISSIDLowerLayers = _ClabWIFISSIDLowerLayers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 7),
    _ClabWIFISSIDLowerLayers_Type()
)
clabWIFISSIDLowerLayers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDLowerLayers.setStatus("current")
_ClabWIFISSIDBSSID_Type = MacAddress
_ClabWIFISSIDBSSID_Object = MibTableColumn
clabWIFISSIDBSSID = _ClabWIFISSIDBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 8),
    _ClabWIFISSIDBSSID_Type()
)
clabWIFISSIDBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDBSSID.setStatus("current")
_ClabWIFISSIDMACAddress_Type = MacAddress
_ClabWIFISSIDMACAddress_Object = MibTableColumn
clabWIFISSIDMACAddress = _ClabWIFISSIDMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 9),
    _ClabWIFISSIDMACAddress_Type()
)
clabWIFISSIDMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDMACAddress.setStatus("current")


class _ClabWIFISSIDSSID_Type(SnmpAdminString):
    """Custom type clabWIFISSIDSSID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClabWIFISSIDSSID_Type.__name__ = "SnmpAdminString"
_ClabWIFISSIDSSID_Object = MibTableColumn
clabWIFISSIDSSID = _ClabWIFISSIDSSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 10),
    _ClabWIFISSIDSSID_Type()
)
clabWIFISSIDSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDSSID.setStatus("current")
_ClabWIFISSIDRowStatus_Type = RowStatus
_ClabWIFISSIDRowStatus_Object = MibTableColumn
clabWIFISSIDRowStatus = _ClabWIFISSIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 11),
    _ClabWIFISSIDRowStatus_Type()
)
clabWIFISSIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDRowStatus.setStatus("current")
_ClabWIFISSIDFragmentationEnable_Type = TruthValue
_ClabWIFISSIDFragmentationEnable_Object = MibTableColumn
clabWIFISSIDFragmentationEnable = _ClabWIFISSIDFragmentationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 12),
    _ClabWIFISSIDFragmentationEnable_Type()
)
clabWIFISSIDFragmentationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFISSIDFragmentationEnable.setStatus("current")
_ClabWIFISSIDPeriodicStatsNumberOfEntries_Type = Integer32
_ClabWIFISSIDPeriodicStatsNumberOfEntries_Object = MibTableColumn
clabWIFISSIDPeriodicStatsNumberOfEntries = _ClabWIFISSIDPeriodicStatsNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 4, 1, 13),
    _ClabWIFISSIDPeriodicStatsNumberOfEntries_Type()
)
clabWIFISSIDPeriodicStatsNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDPeriodicStatsNumberOfEntries.setStatus("current")
_ClabWIFISSIDStatsTable_Object = MibTable
clabWIFISSIDStatsTable = _ClabWIFISSIDStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    clabWIFISSIDStatsTable.setStatus("current")
_ClabWIFISSIDStatsEntry_Object = MibTableRow
clabWIFISSIDStatsEntry = _ClabWIFISSIDStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1)
)
clabWIFISSIDStatsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFISSIDId"),
)
if mibBuilder.loadTexts:
    clabWIFISSIDStatsEntry.setStatus("current")
_ClabWIFISSIDStatsBytesSent_Type = Counter64
_ClabWIFISSIDStatsBytesSent_Object = MibTableColumn
clabWIFISSIDStatsBytesSent = _ClabWIFISSIDStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 1),
    _ClabWIFISSIDStatsBytesSent_Type()
)
clabWIFISSIDStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsBytesSent.setStatus("current")
_ClabWIFISSIDStatsBytesReceived_Type = Counter64
_ClabWIFISSIDStatsBytesReceived_Object = MibTableColumn
clabWIFISSIDStatsBytesReceived = _ClabWIFISSIDStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 2),
    _ClabWIFISSIDStatsBytesReceived_Type()
)
clabWIFISSIDStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsBytesReceived.setStatus("current")
_ClabWIFISSIDStatsPacketsSent_Type = Counter64
_ClabWIFISSIDStatsPacketsSent_Object = MibTableColumn
clabWIFISSIDStatsPacketsSent = _ClabWIFISSIDStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 3),
    _ClabWIFISSIDStatsPacketsSent_Type()
)
clabWIFISSIDStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsPacketsSent.setStatus("current")
_ClabWIFISSIDStatsPacketsReceived_Type = Counter64
_ClabWIFISSIDStatsPacketsReceived_Object = MibTableColumn
clabWIFISSIDStatsPacketsReceived = _ClabWIFISSIDStatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 4),
    _ClabWIFISSIDStatsPacketsReceived_Type()
)
clabWIFISSIDStatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsPacketsReceived.setStatus("current")
_ClabWIFISSIDStatsErrorsSent_Type = Counter32
_ClabWIFISSIDStatsErrorsSent_Object = MibTableColumn
clabWIFISSIDStatsErrorsSent = _ClabWIFISSIDStatsErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 5),
    _ClabWIFISSIDStatsErrorsSent_Type()
)
clabWIFISSIDStatsErrorsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsErrorsSent.setStatus("current")
_ClabWIFISSIDStatsErrorsReceived_Type = Counter32
_ClabWIFISSIDStatsErrorsReceived_Object = MibTableColumn
clabWIFISSIDStatsErrorsReceived = _ClabWIFISSIDStatsErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 6),
    _ClabWIFISSIDStatsErrorsReceived_Type()
)
clabWIFISSIDStatsErrorsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsErrorsReceived.setStatus("current")
_ClabWIFISSIDStatsUnicastPacketsSent_Type = Counter64
_ClabWIFISSIDStatsUnicastPacketsSent_Object = MibTableColumn
clabWIFISSIDStatsUnicastPacketsSent = _ClabWIFISSIDStatsUnicastPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 7),
    _ClabWIFISSIDStatsUnicastPacketsSent_Type()
)
clabWIFISSIDStatsUnicastPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsUnicastPacketsSent.setStatus("current")
_ClabWIFISSIDStatsUnicastPacketsReceived_Type = Counter64
_ClabWIFISSIDStatsUnicastPacketsReceived_Object = MibTableColumn
clabWIFISSIDStatsUnicastPacketsReceived = _ClabWIFISSIDStatsUnicastPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 8),
    _ClabWIFISSIDStatsUnicastPacketsReceived_Type()
)
clabWIFISSIDStatsUnicastPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsUnicastPacketsReceived.setStatus("current")
_ClabWIFISSIDStatsDiscardPacketsSent_Type = Counter32
_ClabWIFISSIDStatsDiscardPacketsSent_Object = MibTableColumn
clabWIFISSIDStatsDiscardPacketsSent = _ClabWIFISSIDStatsDiscardPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 9),
    _ClabWIFISSIDStatsDiscardPacketsSent_Type()
)
clabWIFISSIDStatsDiscardPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsDiscardPacketsSent.setStatus("current")
_ClabWIFISSIDStatsDiscardPacketsReceived_Type = Counter32
_ClabWIFISSIDStatsDiscardPacketsReceived_Object = MibTableColumn
clabWIFISSIDStatsDiscardPacketsReceived = _ClabWIFISSIDStatsDiscardPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 10),
    _ClabWIFISSIDStatsDiscardPacketsReceived_Type()
)
clabWIFISSIDStatsDiscardPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsDiscardPacketsReceived.setStatus("current")
_ClabWIFISSIDStatsMulticastPacketsSent_Type = Counter64
_ClabWIFISSIDStatsMulticastPacketsSent_Object = MibTableColumn
clabWIFISSIDStatsMulticastPacketsSent = _ClabWIFISSIDStatsMulticastPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 11),
    _ClabWIFISSIDStatsMulticastPacketsSent_Type()
)
clabWIFISSIDStatsMulticastPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsMulticastPacketsSent.setStatus("current")
_ClabWIFISSIDStatsMulticastPacketsReceived_Type = Counter64
_ClabWIFISSIDStatsMulticastPacketsReceived_Object = MibTableColumn
clabWIFISSIDStatsMulticastPacketsReceived = _ClabWIFISSIDStatsMulticastPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 12),
    _ClabWIFISSIDStatsMulticastPacketsReceived_Type()
)
clabWIFISSIDStatsMulticastPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsMulticastPacketsReceived.setStatus("current")
_ClabWIFISSIDStatsBroadcastPacketsSent_Type = Counter64
_ClabWIFISSIDStatsBroadcastPacketsSent_Object = MibTableColumn
clabWIFISSIDStatsBroadcastPacketsSent = _ClabWIFISSIDStatsBroadcastPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 13),
    _ClabWIFISSIDStatsBroadcastPacketsSent_Type()
)
clabWIFISSIDStatsBroadcastPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsBroadcastPacketsSent.setStatus("current")
_ClabWIFISSIDStatsBroadcastPacketsReceived_Type = Counter64
_ClabWIFISSIDStatsBroadcastPacketsReceived_Object = MibTableColumn
clabWIFISSIDStatsBroadcastPacketsReceived = _ClabWIFISSIDStatsBroadcastPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 14),
    _ClabWIFISSIDStatsBroadcastPacketsReceived_Type()
)
clabWIFISSIDStatsBroadcastPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsBroadcastPacketsReceived.setStatus("current")
_ClabWIFISSIDStatsUnknownProtoPacketsReceived_Type = Counter32
_ClabWIFISSIDStatsUnknownProtoPacketsReceived_Object = MibTableColumn
clabWIFISSIDStatsUnknownProtoPacketsReceived = _ClabWIFISSIDStatsUnknownProtoPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 15),
    _ClabWIFISSIDStatsUnknownProtoPacketsReceived_Type()
)
clabWIFISSIDStatsUnknownProtoPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsUnknownProtoPacketsReceived.setStatus("current")
_ClabWIFISSIDStatsRetransCount_Type = Counter32
_ClabWIFISSIDStatsRetransCount_Object = MibTableColumn
clabWIFISSIDStatsRetransCount = _ClabWIFISSIDStatsRetransCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 16),
    _ClabWIFISSIDStatsRetransCount_Type()
)
clabWIFISSIDStatsRetransCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsRetransCount.setStatus("current")
_ClabWIFISSIDStatsRetryCount_Type = Counter32
_ClabWIFISSIDStatsRetryCount_Object = MibTableColumn
clabWIFISSIDStatsRetryCount = _ClabWIFISSIDStatsRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 17),
    _ClabWIFISSIDStatsRetryCount_Type()
)
clabWIFISSIDStatsRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsRetryCount.setStatus("current")
_ClabWIFISSIDStatsMultipleRetryCount_Type = Counter32
_ClabWIFISSIDStatsMultipleRetryCount_Object = MibTableColumn
clabWIFISSIDStatsMultipleRetryCount = _ClabWIFISSIDStatsMultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 18),
    _ClabWIFISSIDStatsMultipleRetryCount_Type()
)
clabWIFISSIDStatsMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsMultipleRetryCount.setStatus("current")
_ClabWIFISSIDStatsACKFailureCount_Type = Counter32
_ClabWIFISSIDStatsACKFailureCount_Object = MibTableColumn
clabWIFISSIDStatsACKFailureCount = _ClabWIFISSIDStatsACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 19),
    _ClabWIFISSIDStatsACKFailureCount_Type()
)
clabWIFISSIDStatsACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsACKFailureCount.setStatus("current")
_ClabWIFISSIDStatsAggregatedPacketCount_Type = Counter32
_ClabWIFISSIDStatsAggregatedPacketCount_Object = MibTableColumn
clabWIFISSIDStatsAggregatedPacketCount = _ClabWIFISSIDStatsAggregatedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 5, 1, 20),
    _ClabWIFISSIDStatsAggregatedPacketCount_Type()
)
clabWIFISSIDStatsAggregatedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDStatsAggregatedPacketCount.setStatus("current")
_ClabWIFIAccessPointTable_Object = MibTable
clabWIFIAccessPointTable = _ClabWIFIAccessPointTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointTable.setStatus("current")
_ClabWIFIAccessPointEntry_Object = MibTableRow
clabWIFIAccessPointEntry = _ClabWIFIAccessPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1)
)
clabWIFIAccessPointEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointEntry.setStatus("current")


class _ClabWIFIAccessPointId_Type(Unsigned32):
    """Custom type clabWIFIAccessPointId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ClabWIFIAccessPointId_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointId_Object = MibTableColumn
clabWIFIAccessPointId = _ClabWIFIAccessPointId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 1),
    _ClabWIFIAccessPointId_Type()
)
clabWIFIAccessPointId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointId.setStatus("current")
_ClabWIFIAccessPointEnable_Type = TruthValue
_ClabWIFIAccessPointEnable_Object = MibTableColumn
clabWIFIAccessPointEnable = _ClabWIFIAccessPointEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 2),
    _ClabWIFIAccessPointEnable_Type()
)
clabWIFIAccessPointEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointEnable.setStatus("current")


class _ClabWIFIAccessPointStatus_Type(Integer32):
    """Custom type clabWIFIAccessPointStatus based on Integer32"""
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
          ("enabled", 2),
          ("error", 4),
          ("errorMisconfigured", 3))
    )


_ClabWIFIAccessPointStatus_Type.__name__ = "Integer32"
_ClabWIFIAccessPointStatus_Object = MibTableColumn
clabWIFIAccessPointStatus = _ClabWIFIAccessPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 3),
    _ClabWIFIAccessPointStatus_Type()
)
clabWIFIAccessPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointStatus.setStatus("current")


class _ClabWIFIAccessPointAlias_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabWIFIAccessPointAlias_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointAlias_Object = MibTableColumn
clabWIFIAccessPointAlias = _ClabWIFIAccessPointAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 4),
    _ClabWIFIAccessPointAlias_Type()
)
clabWIFIAccessPointAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAlias.setStatus("current")
_ClabWIFIAccessPointSSIDReference_Type = Unsigned32
_ClabWIFIAccessPointSSIDReference_Object = MibTableColumn
clabWIFIAccessPointSSIDReference = _ClabWIFIAccessPointSSIDReference_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 5),
    _ClabWIFIAccessPointSSIDReference_Type()
)
clabWIFIAccessPointSSIDReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSSIDReference.setStatus("current")
_ClabWIFIAccessPointSSIDAdvertisementEnabled_Type = TruthValue
_ClabWIFIAccessPointSSIDAdvertisementEnabled_Object = MibTableColumn
clabWIFIAccessPointSSIDAdvertisementEnabled = _ClabWIFIAccessPointSSIDAdvertisementEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 6),
    _ClabWIFIAccessPointSSIDAdvertisementEnabled_Type()
)
clabWIFIAccessPointSSIDAdvertisementEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSSIDAdvertisementEnabled.setStatus("current")


class _ClabWIFIAccessPointRetryLimit_Type(Unsigned32):
    """Custom type clabWIFIAccessPointRetryLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ClabWIFIAccessPointRetryLimit_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointRetryLimit_Object = MibTableColumn
clabWIFIAccessPointRetryLimit = _ClabWIFIAccessPointRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 7),
    _ClabWIFIAccessPointRetryLimit_Type()
)
clabWIFIAccessPointRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRetryLimit.setStatus("deprecated")
_ClabWIFIAccessPointWMMCapability_Type = TruthValue
_ClabWIFIAccessPointWMMCapability_Object = MibTableColumn
clabWIFIAccessPointWMMCapability = _ClabWIFIAccessPointWMMCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 8),
    _ClabWIFIAccessPointWMMCapability_Type()
)
clabWIFIAccessPointWMMCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWMMCapability.setStatus("current")
_ClabWIFIAccessPointUAPSDCapability_Type = TruthValue
_ClabWIFIAccessPointUAPSDCapability_Object = MibTableColumn
clabWIFIAccessPointUAPSDCapability = _ClabWIFIAccessPointUAPSDCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 9),
    _ClabWIFIAccessPointUAPSDCapability_Type()
)
clabWIFIAccessPointUAPSDCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointUAPSDCapability.setStatus("current")
_ClabWIFIAccessPointWMMEnable_Type = TruthValue
_ClabWIFIAccessPointWMMEnable_Object = MibTableColumn
clabWIFIAccessPointWMMEnable = _ClabWIFIAccessPointWMMEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 10),
    _ClabWIFIAccessPointWMMEnable_Type()
)
clabWIFIAccessPointWMMEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWMMEnable.setStatus("current")
_ClabWIFIAccessPointUAPSDEnable_Type = TruthValue
_ClabWIFIAccessPointUAPSDEnable_Object = MibTableColumn
clabWIFIAccessPointUAPSDEnable = _ClabWIFIAccessPointUAPSDEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 11),
    _ClabWIFIAccessPointUAPSDEnable_Type()
)
clabWIFIAccessPointUAPSDEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointUAPSDEnable.setStatus("current")
_ClabWIFIAccessPointAssociatedDeviceNumberOfEntries_Type = Unsigned32
_ClabWIFIAccessPointAssociatedDeviceNumberOfEntries_Object = MibTableColumn
clabWIFIAccessPointAssociatedDeviceNumberOfEntries = _ClabWIFIAccessPointAssociatedDeviceNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 12),
    _ClabWIFIAccessPointAssociatedDeviceNumberOfEntries_Type()
)
clabWIFIAccessPointAssociatedDeviceNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAssociatedDeviceNumberOfEntries.setStatus("current")
_ClabWIFIAccessPointRowStatus_Type = RowStatus
_ClabWIFIAccessPointRowStatus_Object = MibTableColumn
clabWIFIAccessPointRowStatus = _ClabWIFIAccessPointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 13),
    _ClabWIFIAccessPointRowStatus_Type()
)
clabWIFIAccessPointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRowStatus.setStatus("current")
_ClabWIFIAccessPointPublicAccessMode_Type = TruthValue
_ClabWIFIAccessPointPublicAccessMode_Object = MibTableColumn
clabWIFIAccessPointPublicAccessMode = _ClabWIFIAccessPointPublicAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 14),
    _ClabWIFIAccessPointPublicAccessMode_Type()
)
clabWIFIAccessPointPublicAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPublicAccessMode.setStatus("current")
_ClabWIFIAccessPointIsolationEnable_Type = TruthValue
_ClabWIFIAccessPointIsolationEnable_Object = MibTableColumn
clabWIFIAccessPointIsolationEnable = _ClabWIFIAccessPointIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 15),
    _ClabWIFIAccessPointIsolationEnable_Type()
)
clabWIFIAccessPointIsolationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointIsolationEnable.setStatus("current")
_ClabWIFIAccessPointMaxAssociatedDevices_Type = Unsigned32
_ClabWIFIAccessPointMaxAssociatedDevices_Object = MibTableColumn
clabWIFIAccessPointMaxAssociatedDevices = _ClabWIFIAccessPointMaxAssociatedDevices_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 16),
    _ClabWIFIAccessPointMaxAssociatedDevices_Type()
)
clabWIFIAccessPointMaxAssociatedDevices.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointMaxAssociatedDevices.setStatus("current")
_ClabWIFIAccessPointPasspointSupported_Type = TruthValue
_ClabWIFIAccessPointPasspointSupported_Object = MibTableColumn
clabWIFIAccessPointPasspointSupported = _ClabWIFIAccessPointPasspointSupported_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 17),
    _ClabWIFIAccessPointPasspointSupported_Type()
)
clabWIFIAccessPointPasspointSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointSupported.setStatus("current")
_ClabWIFIAccessPointPasspointEnabled_Type = TruthValue
_ClabWIFIAccessPointPasspointEnabled_Object = MibTableColumn
clabWIFIAccessPointPasspointEnabled = _ClabWIFIAccessPointPasspointEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 18),
    _ClabWIFIAccessPointPasspointEnabled_Type()
)
clabWIFIAccessPointPasspointEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointEnabled.setStatus("current")
_ClabWIFIAccessPointInterworkingCapability_Type = TruthValue
_ClabWIFIAccessPointInterworkingCapability_Object = MibTableColumn
clabWIFIAccessPointInterworkingCapability = _ClabWIFIAccessPointInterworkingCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 19),
    _ClabWIFIAccessPointInterworkingCapability_Type()
)
clabWIFIAccessPointInterworkingCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointInterworkingCapability.setStatus("current")
_ClabWIFIAccessPointInterworkingServiceEnabled_Type = TruthValue
_ClabWIFIAccessPointInterworkingServiceEnabled_Object = MibTableColumn
clabWIFIAccessPointInterworkingServiceEnabled = _ClabWIFIAccessPointInterworkingServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 20),
    _ClabWIFIAccessPointInterworkingServiceEnabled_Type()
)
clabWIFIAccessPointInterworkingServiceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointInterworkingServiceEnabled.setStatus("current")
_ClabWIFIAccessPointAccessControlFilterEnable_Type = TruthValue
_ClabWIFIAccessPointAccessControlFilterEnable_Object = MibTableColumn
clabWIFIAccessPointAccessControlFilterEnable = _ClabWIFIAccessPointAccessControlFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 21),
    _ClabWIFIAccessPointAccessControlFilterEnable_Type()
)
clabWIFIAccessPointAccessControlFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccessControlFilterEnable.setStatus("deprecated")
_ClabWIFIAccessPointMACAddressControlEnable_Type = TruthValue
_ClabWIFIAccessPointMACAddressControlEnable_Object = MibTableColumn
clabWIFIAccessPointMACAddressControlEnable = _ClabWIFIAccessPointMACAddressControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 22),
    _ClabWIFIAccessPointMACAddressControlEnable_Type()
)
clabWIFIAccessPointMACAddressControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointMACAddressControlEnable.setStatus("current")


class _ClabWIFIAccessPointAllowedMACAddress_Type(OctetString):
    """Custom type clabWIFIAccessPointAllowedMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_ClabWIFIAccessPointAllowedMACAddress_Type.__name__ = "OctetString"
_ClabWIFIAccessPointAllowedMACAddress_Object = MibTableColumn
clabWIFIAccessPointAllowedMACAddress = _ClabWIFIAccessPointAllowedMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 23),
    _ClabWIFIAccessPointAllowedMACAddress_Type()
)
clabWIFIAccessPointAllowedMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAllowedMACAddress.setStatus("current")
_ClabWIFIAccessPointClientSessionNumberOfEntries_Type = Unsigned32
_ClabWIFIAccessPointClientSessionNumberOfEntries_Object = MibTableColumn
clabWIFIAccessPointClientSessionNumberOfEntries = _ClabWIFIAccessPointClientSessionNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 24),
    _ClabWIFIAccessPointClientSessionNumberOfEntries_Type()
)
clabWIFIAccessPointClientSessionNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointClientSessionNumberOfEntries.setStatus("current")
_ClabWIFIAccessPointAssociatedDeviceCount_Type = Unsigned32
_ClabWIFIAccessPointAssociatedDeviceCount_Object = MibTableColumn
clabWIFIAccessPointAssociatedDeviceCount = _ClabWIFIAccessPointAssociatedDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 6, 1, 25),
    _ClabWIFIAccessPointAssociatedDeviceCount_Type()
)
clabWIFIAccessPointAssociatedDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAssociatedDeviceCount.setStatus("deprecated")
_ClabWIFIAccessPointSecurityTable_Object = MibTable
clabWIFIAccessPointSecurityTable = _ClabWIFIAccessPointSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityTable.setStatus("current")
_ClabWIFIAccessPointSecurityEntry_Object = MibTableRow
clabWIFIAccessPointSecurityEntry = _ClabWIFIAccessPointSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1)
)
clabWIFIAccessPointSecurityEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityEntry.setStatus("current")
_ClabWIFIAccessPointSecurityModesSupported_Type = SnmpAdminString
_ClabWIFIAccessPointSecurityModesSupported_Object = MibTableColumn
clabWIFIAccessPointSecurityModesSupported = _ClabWIFIAccessPointSecurityModesSupported_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 1),
    _ClabWIFIAccessPointSecurityModesSupported_Type()
)
clabWIFIAccessPointSecurityModesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityModesSupported.setStatus("current")


class _ClabWIFIAccessPointSecurityModeEnabled_Type(Integer32):
    """Custom type clabWIFIAccessPointSecurityModeEnabled based on Integer32"""
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
        *(("none", 1),
          ("wep128", 3),
          ("wep64", 2),
          ("wpa2Enterprise", 8),
          ("wpa2Personal", 5),
          ("wpaEnterprise", 7),
          ("wpaPersonal", 4),
          ("wpawpa2Enterprise", 9),
          ("wpawpa2Personal", 6))
    )


_ClabWIFIAccessPointSecurityModeEnabled_Type.__name__ = "Integer32"
_ClabWIFIAccessPointSecurityModeEnabled_Object = MibTableColumn
clabWIFIAccessPointSecurityModeEnabled = _ClabWIFIAccessPointSecurityModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 2),
    _ClabWIFIAccessPointSecurityModeEnabled_Type()
)
clabWIFIAccessPointSecurityModeEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityModeEnabled.setStatus("current")


class _ClabWIFIAccessPointSecurityWEPKey_Type(OctetString):
    """Custom type clabWIFIAccessPointSecurityWEPKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(13, 13),
    )


_ClabWIFIAccessPointSecurityWEPKey_Type.__name__ = "OctetString"
_ClabWIFIAccessPointSecurityWEPKey_Object = MibTableColumn
clabWIFIAccessPointSecurityWEPKey = _ClabWIFIAccessPointSecurityWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 3),
    _ClabWIFIAccessPointSecurityWEPKey_Type()
)
clabWIFIAccessPointSecurityWEPKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityWEPKey.setStatus("current")


class _ClabWIFIAccessPointSecurityPreSharedKey_Type(OctetString):
    """Custom type clabWIFIAccessPointSecurityPreSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_ClabWIFIAccessPointSecurityPreSharedKey_Type.__name__ = "OctetString"
_ClabWIFIAccessPointSecurityPreSharedKey_Object = MibTableColumn
clabWIFIAccessPointSecurityPreSharedKey = _ClabWIFIAccessPointSecurityPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 4),
    _ClabWIFIAccessPointSecurityPreSharedKey_Type()
)
clabWIFIAccessPointSecurityPreSharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityPreSharedKey.setStatus("current")


class _ClabWIFIAccessPointSecurityKeyPassphrase_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointSecurityKeyPassphrase based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ClabWIFIAccessPointSecurityKeyPassphrase_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointSecurityKeyPassphrase_Object = MibTableColumn
clabWIFIAccessPointSecurityKeyPassphrase = _ClabWIFIAccessPointSecurityKeyPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 5),
    _ClabWIFIAccessPointSecurityKeyPassphrase_Type()
)
clabWIFIAccessPointSecurityKeyPassphrase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityKeyPassphrase.setStatus("current")


class _ClabWIFIAccessPointSecurityRekeyingInterval_Type(Unsigned32):
    """Custom type clabWIFIAccessPointSecurityRekeyingInterval based on Unsigned32"""
    defaultValue = 3600


_ClabWIFIAccessPointSecurityRekeyingInterval_Object = MibTableColumn
clabWIFIAccessPointSecurityRekeyingInterval = _ClabWIFIAccessPointSecurityRekeyingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 6),
    _ClabWIFIAccessPointSecurityRekeyingInterval_Type()
)
clabWIFIAccessPointSecurityRekeyingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityRekeyingInterval.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityRekeyingInterval.setUnits("seconds")
_ClabWIFIAccessPointSecurityRadiusServerIPAddrType_Type = InetAddressType
_ClabWIFIAccessPointSecurityRadiusServerIPAddrType_Object = MibTableColumn
clabWIFIAccessPointSecurityRadiusServerIPAddrType = _ClabWIFIAccessPointSecurityRadiusServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 7),
    _ClabWIFIAccessPointSecurityRadiusServerIPAddrType_Type()
)
clabWIFIAccessPointSecurityRadiusServerIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityRadiusServerIPAddrType.setStatus("current")
_ClabWIFIAccessPointSecurityRadiusServerIPAddr_Type = InetAddress
_ClabWIFIAccessPointSecurityRadiusServerIPAddr_Object = MibTableColumn
clabWIFIAccessPointSecurityRadiusServerIPAddr = _ClabWIFIAccessPointSecurityRadiusServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 8),
    _ClabWIFIAccessPointSecurityRadiusServerIPAddr_Type()
)
clabWIFIAccessPointSecurityRadiusServerIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityRadiusServerIPAddr.setStatus("current")


class _ClabWIFIAccessPointSecurityRadiusServerPort_Type(InetPortNumber):
    """Custom type clabWIFIAccessPointSecurityRadiusServerPort based on InetPortNumber"""
    defaultValue = 1812


_ClabWIFIAccessPointSecurityRadiusServerPort_Object = MibTableColumn
clabWIFIAccessPointSecurityRadiusServerPort = _ClabWIFIAccessPointSecurityRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 9),
    _ClabWIFIAccessPointSecurityRadiusServerPort_Type()
)
clabWIFIAccessPointSecurityRadiusServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityRadiusServerPort.setStatus("current")
_ClabWIFIAccessPointSecurityRadiusSecret_Type = SnmpAdminString
_ClabWIFIAccessPointSecurityRadiusSecret_Object = MibTableColumn
clabWIFIAccessPointSecurityRadiusSecret = _ClabWIFIAccessPointSecurityRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 10),
    _ClabWIFIAccessPointSecurityRadiusSecret_Type()
)
clabWIFIAccessPointSecurityRadiusSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityRadiusSecret.setStatus("current")
_ClabWIFIAccessPointSecurityRowstatus_Type = RowStatus
_ClabWIFIAccessPointSecurityRowstatus_Object = MibTableColumn
clabWIFIAccessPointSecurityRowstatus = _ClabWIFIAccessPointSecurityRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 11),
    _ClabWIFIAccessPointSecurityRowstatus_Type()
)
clabWIFIAccessPointSecurityRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityRowstatus.setStatus("current")


class _ClabWIFIAccessPointSecurityWEPKey2_Type(OctetString):
    """Custom type clabWIFIAccessPointSecurityWEPKey2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(13, 13),
    )


_ClabWIFIAccessPointSecurityWEPKey2_Type.__name__ = "OctetString"
_ClabWIFIAccessPointSecurityWEPKey2_Object = MibTableColumn
clabWIFIAccessPointSecurityWEPKey2 = _ClabWIFIAccessPointSecurityWEPKey2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 12),
    _ClabWIFIAccessPointSecurityWEPKey2_Type()
)
clabWIFIAccessPointSecurityWEPKey2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityWEPKey2.setStatus("current")


class _ClabWIFIAccessPointSecurityWEPKey3_Type(OctetString):
    """Custom type clabWIFIAccessPointSecurityWEPKey3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(13, 13),
    )


_ClabWIFIAccessPointSecurityWEPKey3_Type.__name__ = "OctetString"
_ClabWIFIAccessPointSecurityWEPKey3_Object = MibTableColumn
clabWIFIAccessPointSecurityWEPKey3 = _ClabWIFIAccessPointSecurityWEPKey3_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 13),
    _ClabWIFIAccessPointSecurityWEPKey3_Type()
)
clabWIFIAccessPointSecurityWEPKey3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityWEPKey3.setStatus("current")


class _ClabWIFIAccessPointSecurityWEPKey4_Type(OctetString):
    """Custom type clabWIFIAccessPointSecurityWEPKey4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(13, 13),
    )


_ClabWIFIAccessPointSecurityWEPKey4_Type.__name__ = "OctetString"
_ClabWIFIAccessPointSecurityWEPKey4_Object = MibTableColumn
clabWIFIAccessPointSecurityWEPKey4 = _ClabWIFIAccessPointSecurityWEPKey4_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 14),
    _ClabWIFIAccessPointSecurityWEPKey4_Type()
)
clabWIFIAccessPointSecurityWEPKey4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityWEPKey4.setStatus("current")


class _ClabWIFIAccessPointSecurityWEPIndex_Type(Unsigned32):
    """Custom type clabWIFIAccessPointSecurityWEPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ClabWIFIAccessPointSecurityWEPIndex_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointSecurityWEPIndex_Object = MibTableColumn
clabWIFIAccessPointSecurityWEPIndex = _ClabWIFIAccessPointSecurityWEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 15),
    _ClabWIFIAccessPointSecurityWEPIndex_Type()
)
clabWIFIAccessPointSecurityWEPIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityWEPIndex.setStatus("current")


class _ClabWIFIAccessPointSecurityWEPPassPhrase_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointSecurityWEPPassPhrase based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 63),
    )


_ClabWIFIAccessPointSecurityWEPPassPhrase_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointSecurityWEPPassPhrase_Object = MibTableColumn
clabWIFIAccessPointSecurityWEPPassPhrase = _ClabWIFIAccessPointSecurityWEPPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 16),
    _ClabWIFIAccessPointSecurityWEPPassPhrase_Type()
)
clabWIFIAccessPointSecurityWEPPassPhrase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityWEPPassPhrase.setStatus("current")


class _ClabWIFIAccessPointSecurityWPAEncryption_Type(Integer32):
    """Custom type clabWIFIAccessPointSecurityWPAEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("tkipaes", 2))
    )


_ClabWIFIAccessPointSecurityWPAEncryption_Type.__name__ = "Integer32"
_ClabWIFIAccessPointSecurityWPAEncryption_Object = MibTableColumn
clabWIFIAccessPointSecurityWPAEncryption = _ClabWIFIAccessPointSecurityWPAEncryption_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 17),
    _ClabWIFIAccessPointSecurityWPAEncryption_Type()
)
clabWIFIAccessPointSecurityWPAEncryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityWPAEncryption.setStatus("current")
_ClabWIFIAccessPointSecuritySecondaryRadiusServerIPAddrType_Type = InetAddressType
_ClabWIFIAccessPointSecuritySecondaryRadiusServerIPAddrType_Object = MibTableColumn
clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddrType = _ClabWIFIAccessPointSecuritySecondaryRadiusServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 18),
    _ClabWIFIAccessPointSecuritySecondaryRadiusServerIPAddrType_Type()
)
clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddrType.setStatus("current")
_ClabWIFIAccessPointSecuritySecondaryRadiusServerIPAddr_Type = InetAddress
_ClabWIFIAccessPointSecuritySecondaryRadiusServerIPAddr_Object = MibTableColumn
clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddr = _ClabWIFIAccessPointSecuritySecondaryRadiusServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 19),
    _ClabWIFIAccessPointSecuritySecondaryRadiusServerIPAddr_Type()
)
clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddr.setStatus("current")


class _ClabWIFIAccessPointSecuritySecondaryRadiusServerPort_Type(InetPortNumber):
    """Custom type clabWIFIAccessPointSecuritySecondaryRadiusServerPort based on InetPortNumber"""
    defaultValue = 1812


_ClabWIFIAccessPointSecuritySecondaryRadiusServerPort_Object = MibTableColumn
clabWIFIAccessPointSecuritySecondaryRadiusServerPort = _ClabWIFIAccessPointSecuritySecondaryRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 20),
    _ClabWIFIAccessPointSecuritySecondaryRadiusServerPort_Type()
)
clabWIFIAccessPointSecuritySecondaryRadiusServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecuritySecondaryRadiusServerPort.setStatus("current")
_ClabWIFIAccessPointSecuritySecondaryRadiusSecret_Type = SnmpAdminString
_ClabWIFIAccessPointSecuritySecondaryRadiusSecret_Object = MibTableColumn
clabWIFIAccessPointSecuritySecondaryRadiusSecret = _ClabWIFIAccessPointSecuritySecondaryRadiusSecret_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 21),
    _ClabWIFIAccessPointSecuritySecondaryRadiusSecret_Type()
)
clabWIFIAccessPointSecuritySecondaryRadiusSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecuritySecondaryRadiusSecret.setStatus("current")
_ClabWIFIAccessPointSecurityEnableManagementFrameProtection_Type = TruthValue
_ClabWIFIAccessPointSecurityEnableManagementFrameProtection_Object = MibTableColumn
clabWIFIAccessPointSecurityEnableManagementFrameProtection = _ClabWIFIAccessPointSecurityEnableManagementFrameProtection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 22),
    _ClabWIFIAccessPointSecurityEnableManagementFrameProtection_Type()
)
clabWIFIAccessPointSecurityEnableManagementFrameProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityEnableManagementFrameProtection.setStatus("current")
_ClabWIFIAccessPointSecurityReset_Type = TruthValue
_ClabWIFIAccessPointSecurityReset_Object = MibTableColumn
clabWIFIAccessPointSecurityReset = _ClabWIFIAccessPointSecurityReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 23),
    _ClabWIFIAccessPointSecurityReset_Type()
)
clabWIFIAccessPointSecurityReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityReset.setStatus("current")
_ClabWIFIAccessPointRadiusRetries_Type = Integer32
_ClabWIFIAccessPointRadiusRetries_Object = MibTableColumn
clabWIFIAccessPointRadiusRetries = _ClabWIFIAccessPointRadiusRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 24),
    _ClabWIFIAccessPointRadiusRetries_Type()
)
clabWIFIAccessPointRadiusRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusRetries.setStatus("current")
_ClabWIFIAccessPointSecurityLanRoutingEnabled_Type = TruthValue
_ClabWIFIAccessPointSecurityLanRoutingEnabled_Object = MibTableColumn
clabWIFIAccessPointSecurityLanRoutingEnabled = _ClabWIFIAccessPointSecurityLanRoutingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 7, 1, 25),
    _ClabWIFIAccessPointSecurityLanRoutingEnabled_Type()
)
clabWIFIAccessPointSecurityLanRoutingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointSecurityLanRoutingEnabled.setStatus("current")
_ClabWIFIAccessPointWPSTable_Object = MibTable
clabWIFIAccessPointWPSTable = _ClabWIFIAccessPointWPSTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSTable.setStatus("current")
_ClabWIFIAccessPointWPSEntry_Object = MibTableRow
clabWIFIAccessPointWPSEntry = _ClabWIFIAccessPointWPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8, 1)
)
clabWIFIAccessPointWPSEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSEntry.setStatus("current")


class _ClabWIFIAccessPointWPSEnable_Type(TruthValue):
    """Custom type clabWIFIAccessPointWPSEnable based on TruthValue"""


_ClabWIFIAccessPointWPSEnable_Object = MibTableColumn
clabWIFIAccessPointWPSEnable = _ClabWIFIAccessPointWPSEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8, 1, 1),
    _ClabWIFIAccessPointWPSEnable_Type()
)
clabWIFIAccessPointWPSEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSEnable.setStatus("current")
_ClabWIFIAccessPointWPSConfigMethodsSupported_Type = SnmpAdminString
_ClabWIFIAccessPointWPSConfigMethodsSupported_Object = MibTableColumn
clabWIFIAccessPointWPSConfigMethodsSupported = _ClabWIFIAccessPointWPSConfigMethodsSupported_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8, 1, 2),
    _ClabWIFIAccessPointWPSConfigMethodsSupported_Type()
)
clabWIFIAccessPointWPSConfigMethodsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSConfigMethodsSupported.setStatus("current")


class _ClabWIFIAccessPointWPSConfigMethodsEnabled_Type(Integer32):
    """Custom type clabWIFIAccessPointWPSConfigMethodsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("externalNFCToken", 3),
          ("integratedNFCToken", 4),
          ("nfcInterface", 5),
          ("pin", 7),
          ("pushButton", 8),
          ("usbFlashDrive", 1))
    )


_ClabWIFIAccessPointWPSConfigMethodsEnabled_Type.__name__ = "Integer32"
_ClabWIFIAccessPointWPSConfigMethodsEnabled_Object = MibTableColumn
clabWIFIAccessPointWPSConfigMethodsEnabled = _ClabWIFIAccessPointWPSConfigMethodsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8, 1, 3),
    _ClabWIFIAccessPointWPSConfigMethodsEnabled_Type()
)
clabWIFIAccessPointWPSConfigMethodsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSConfigMethodsEnabled.setStatus("deprecated")
_ClabWIFIAccessPointWPSRowStatus_Type = RowStatus
_ClabWIFIAccessPointWPSRowStatus_Object = MibTableColumn
clabWIFIAccessPointWPSRowStatus = _ClabWIFIAccessPointWPSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8, 1, 4),
    _ClabWIFIAccessPointWPSRowStatus_Type()
)
clabWIFIAccessPointWPSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSRowStatus.setStatus("current")


class _ClabWIFIAccessPointWPSSetWPSMethod_Type(Integer32):
    """Custom type clabWIFIAccessPointWPSSetWPSMethod based on Integer32"""
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
        *(("display", 6),
          ("ethernet", 2),
          ("externalNFCToken", 3),
          ("integratedNFCToken", 4),
          ("keypad", 9),
          ("nfcInterface", 5),
          ("pin", 7),
          ("pushButton", 8),
          ("usbFlashDrive", 1))
    )


_ClabWIFIAccessPointWPSSetWPSMethod_Type.__name__ = "Integer32"
_ClabWIFIAccessPointWPSSetWPSMethod_Object = MibTableColumn
clabWIFIAccessPointWPSSetWPSMethod = _ClabWIFIAccessPointWPSSetWPSMethod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8, 1, 5),
    _ClabWIFIAccessPointWPSSetWPSMethod_Type()
)
clabWIFIAccessPointWPSSetWPSMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSSetWPSMethod.setStatus("deprecated")
_ClabWIFIAccessPointWPSAPPin_Type = SnmpAdminString
_ClabWIFIAccessPointWPSAPPin_Object = MibTableColumn
clabWIFIAccessPointWPSAPPin = _ClabWIFIAccessPointWPSAPPin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8, 1, 6),
    _ClabWIFIAccessPointWPSAPPin_Type()
)
clabWIFIAccessPointWPSAPPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSAPPin.setStatus("current")
_ClabWIFIAccessPointWPSSetWPSClientPin_Type = SnmpAdminString
_ClabWIFIAccessPointWPSSetWPSClientPin_Object = MibTableColumn
clabWIFIAccessPointWPSSetWPSClientPin = _ClabWIFIAccessPointWPSSetWPSClientPin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8, 1, 7),
    _ClabWIFIAccessPointWPSSetWPSClientPin_Type()
)
clabWIFIAccessPointWPSSetWPSClientPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSSetWPSClientPin.setStatus("current")
_ClabWIFIAccessPointWPSConfigMethodsEnable_Type = SnmpAdminString
_ClabWIFIAccessPointWPSConfigMethodsEnable_Object = MibTableColumn
clabWIFIAccessPointWPSConfigMethodsEnable = _ClabWIFIAccessPointWPSConfigMethodsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8, 1, 8),
    _ClabWIFIAccessPointWPSConfigMethodsEnable_Type()
)
clabWIFIAccessPointWPSConfigMethodsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSConfigMethodsEnable.setStatus("current")


class _ClabWIFIAccessPointWPSSetWPSMethods_Type(Bits):
    """Custom type clabWIFIAccessPointWPSSetWPSMethods based on Bits"""
    namedValues = NamedValues(
        *(("display", 5),
          ("ethernet", 1),
          ("externalNFCToken", 2),
          ("integratedNFCToken", 3),
          ("keypad", 8),
          ("nfcInterface", 4),
          ("pin", 6),
          ("pushButton", 7),
          ("usbFlashDrive", 0))
    )

_ClabWIFIAccessPointWPSSetWPSMethods_Type.__name__ = "Bits"
_ClabWIFIAccessPointWPSSetWPSMethods_Object = MibTableColumn
clabWIFIAccessPointWPSSetWPSMethods = _ClabWIFIAccessPointWPSSetWPSMethods_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 8, 1, 9),
    _ClabWIFIAccessPointWPSSetWPSMethods_Type()
)
clabWIFIAccessPointWPSSetWPSMethods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointWPSSetWPSMethods.setStatus("current")
_ClabWIFIAssociatedDeviceTable_Object = MibTable
clabWIFIAssociatedDeviceTable = _ClabWIFIAssociatedDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceTable.setStatus("current")
_ClabWIFIAssociatedDeviceEntry_Object = MibTableRow
clabWIFIAssociatedDeviceEntry = _ClabWIFIAssociatedDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1)
)
clabWIFIAssociatedDeviceEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceId"),
)
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceEntry.setStatus("current")
_ClabWIFIAssociatedDeviceId_Type = Unsigned32
_ClabWIFIAssociatedDeviceId_Object = MibTableColumn
clabWIFIAssociatedDeviceId = _ClabWIFIAssociatedDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 1),
    _ClabWIFIAssociatedDeviceId_Type()
)
clabWIFIAssociatedDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceId.setStatus("current")
_ClabWIFIAssociatedDeviceMACAddress_Type = MacAddress
_ClabWIFIAssociatedDeviceMACAddress_Object = MibTableColumn
clabWIFIAssociatedDeviceMACAddress = _ClabWIFIAssociatedDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 2),
    _ClabWIFIAssociatedDeviceMACAddress_Type()
)
clabWIFIAssociatedDeviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceMACAddress.setStatus("current")
_ClabWIFIAssociatedDeviceAuthenticationState_Type = TruthValue
_ClabWIFIAssociatedDeviceAuthenticationState_Object = MibTableColumn
clabWIFIAssociatedDeviceAuthenticationState = _ClabWIFIAssociatedDeviceAuthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 3),
    _ClabWIFIAssociatedDeviceAuthenticationState_Type()
)
clabWIFIAssociatedDeviceAuthenticationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceAuthenticationState.setStatus("current")


class _ClabWIFIAssociatedDeviceLastDataDownlinkRate_Type(Unsigned32):
    """Custom type clabWIFIAssociatedDeviceLastDataDownlinkRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 600000),
    )


_ClabWIFIAssociatedDeviceLastDataDownlinkRate_Type.__name__ = "Unsigned32"
_ClabWIFIAssociatedDeviceLastDataDownlinkRate_Object = MibTableColumn
clabWIFIAssociatedDeviceLastDataDownlinkRate = _ClabWIFIAssociatedDeviceLastDataDownlinkRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 4),
    _ClabWIFIAssociatedDeviceLastDataDownlinkRate_Type()
)
clabWIFIAssociatedDeviceLastDataDownlinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceLastDataDownlinkRate.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceLastDataDownlinkRate.setUnits("kbps")


class _ClabWIFIAssociatedDeviceLastDataUplinkRate_Type(Unsigned32):
    """Custom type clabWIFIAssociatedDeviceLastDataUplinkRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 600000),
    )


_ClabWIFIAssociatedDeviceLastDataUplinkRate_Type.__name__ = "Unsigned32"
_ClabWIFIAssociatedDeviceLastDataUplinkRate_Object = MibTableColumn
clabWIFIAssociatedDeviceLastDataUplinkRate = _ClabWIFIAssociatedDeviceLastDataUplinkRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 5),
    _ClabWIFIAssociatedDeviceLastDataUplinkRate_Type()
)
clabWIFIAssociatedDeviceLastDataUplinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceLastDataUplinkRate.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceLastDataUplinkRate.setUnits("kbps")


class _ClabWIFIAssociatedDeviceSignalStrength_Type(Integer32):
    """Custom type clabWIFIAssociatedDeviceSignalStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 0),
    )


_ClabWIFIAssociatedDeviceSignalStrength_Type.__name__ = "Integer32"
_ClabWIFIAssociatedDeviceSignalStrength_Object = MibTableColumn
clabWIFIAssociatedDeviceSignalStrength = _ClabWIFIAssociatedDeviceSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 6),
    _ClabWIFIAssociatedDeviceSignalStrength_Type()
)
clabWIFIAssociatedDeviceSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceSignalStrength.setUnits("dBm")


class _ClabWIFIAssociatedDeviceRetransmissions_Type(Unsigned32):
    """Custom type clabWIFIAssociatedDeviceRetransmissions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClabWIFIAssociatedDeviceRetransmissions_Type.__name__ = "Unsigned32"
_ClabWIFIAssociatedDeviceRetransmissions_Object = MibTableColumn
clabWIFIAssociatedDeviceRetransmissions = _ClabWIFIAssociatedDeviceRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 7),
    _ClabWIFIAssociatedDeviceRetransmissions_Type()
)
clabWIFIAssociatedDeviceRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceRetransmissions.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceRetransmissions.setUnits("packets")
_ClabWIFIAssociatedDeviceActive_Type = TruthValue
_ClabWIFIAssociatedDeviceActive_Object = MibTableColumn
clabWIFIAssociatedDeviceActive = _ClabWIFIAssociatedDeviceActive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 8),
    _ClabWIFIAssociatedDeviceActive_Type()
)
clabWIFIAssociatedDeviceActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceActive.setStatus("current")
_ClabWIFIAssociatedDeviceMaxPacketRetryCount_Type = Unsigned32
_ClabWIFIAssociatedDeviceMaxPacketRetryCount_Object = MibTableColumn
clabWIFIAssociatedDeviceMaxPacketRetryCount = _ClabWIFIAssociatedDeviceMaxPacketRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 9),
    _ClabWIFIAssociatedDeviceMaxPacketRetryCount_Type()
)
clabWIFIAssociatedDeviceMaxPacketRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceMaxPacketRetryCount.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceMaxPacketRetryCount.setUnits("packets")
_ClabWIFIAssociatedDeviceStationCount_Type = Counter32
_ClabWIFIAssociatedDeviceStationCount_Object = MibTableColumn
clabWIFIAssociatedDeviceStationCount = _ClabWIFIAssociatedDeviceStationCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 10),
    _ClabWIFIAssociatedDeviceStationCount_Type()
)
clabWIFIAssociatedDeviceStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceStationCount.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceStationCount.setUnits("stations")
_ClabWIFIAssociatedDeviceMaxNumOfStations_Type = Unsigned32
_ClabWIFIAssociatedDeviceMaxNumOfStations_Object = MibTableColumn
clabWIFIAssociatedDeviceMaxNumOfStations = _ClabWIFIAssociatedDeviceMaxNumOfStations_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 11),
    _ClabWIFIAssociatedDeviceMaxNumOfStations_Type()
)
clabWIFIAssociatedDeviceMaxNumOfStations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceMaxNumOfStations.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceMaxNumOfStations.setUnits("stations")


class _ClabWIFIAssociatedDeviceSecurityMode_Type(Integer32):
    """Custom type clabWIFIAssociatedDeviceSecurityMode based on Integer32"""
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
        *(("none", 1),
          ("wep128", 3),
          ("wep64", 2),
          ("wpa2Enterprise", 8),
          ("wpa2Personal", 5),
          ("wpaEnterprise", 7),
          ("wpaPersonal", 4),
          ("wpaWPA2Personal", 6),
          ("wpaWpa2Enterprise", 9))
    )


_ClabWIFIAssociatedDeviceSecurityMode_Type.__name__ = "Integer32"
_ClabWIFIAssociatedDeviceSecurityMode_Object = MibTableColumn
clabWIFIAssociatedDeviceSecurityMode = _ClabWIFIAssociatedDeviceSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 12),
    _ClabWIFIAssociatedDeviceSecurityMode_Type()
)
clabWIFIAssociatedDeviceSecurityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceSecurityMode.setStatus("current")


class _ClabWIFIAssociatedDeviceEncryptionAlgorithm_Type(Integer32):
    """Custom type clabWIFIAssociatedDeviceEncryptionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 3),
          ("tkip", 2),
          ("unknown", 1))
    )


_ClabWIFIAssociatedDeviceEncryptionAlgorithm_Type.__name__ = "Integer32"
_ClabWIFIAssociatedDeviceEncryptionAlgorithm_Object = MibTableColumn
clabWIFIAssociatedDeviceEncryptionAlgorithm = _ClabWIFIAssociatedDeviceEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 13),
    _ClabWIFIAssociatedDeviceEncryptionAlgorithm_Type()
)
clabWIFIAssociatedDeviceEncryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceEncryptionAlgorithm.setStatus("deprecated")


class _ClabWIFIAssociatedDeviceAssociationState_Type(Integer32):
    """Custom type clabWIFIAssociatedDeviceAssociationState based on Integer32"""
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
        *(("clientDisassociated", 2),
          ("connected", 1),
          ("forcedDisassociationAuth", 3),
          ("forcedDisassociationNetMode", 5),
          ("forcedDisassociationSnr", 6),
          ("forcedDisassociationTimeout", 4),
          ("other", 7))
    )


_ClabWIFIAssociatedDeviceAssociationState_Type.__name__ = "Integer32"
_ClabWIFIAssociatedDeviceAssociationState_Object = MibTableColumn
clabWIFIAssociatedDeviceAssociationState = _ClabWIFIAssociatedDeviceAssociationState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 9, 1, 14),
    _ClabWIFIAssociatedDeviceAssociationState_Type()
)
clabWIFIAssociatedDeviceAssociationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAssociatedDeviceAssociationState.setStatus("current")
_ClabWIFIDataRateStatsTable_Object = MibTable
clabWIFIDataRateStatsTable = _ClabWIFIDataRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 10)
)
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsTable.setStatus("deprecated")
_ClabWIFIDataRateStatsEntry_Object = MibTableRow
clabWIFIDataRateStatsEntry = _ClabWIFIDataRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 10, 1)
)
clabWIFIDataRateStatsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIRadioId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIDataRateStatsRate"),
)
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsEntry.setStatus("deprecated")
_ClabWIFIDataRateStatsRate_Type = Unsigned32
_ClabWIFIDataRateStatsRate_Object = MibTableColumn
clabWIFIDataRateStatsRate = _ClabWIFIDataRateStatsRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 10, 1, 1),
    _ClabWIFIDataRateStatsRate_Type()
)
clabWIFIDataRateStatsRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsRate.setUnits("Mbps")
_ClabWIFIDataRateStatsFramesSent_Type = Counter64
_ClabWIFIDataRateStatsFramesSent_Object = MibTableColumn
clabWIFIDataRateStatsFramesSent = _ClabWIFIDataRateStatsFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 10, 1, 2),
    _ClabWIFIDataRateStatsFramesSent_Type()
)
clabWIFIDataRateStatsFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsFramesSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsFramesSent.setUnits("frames")
_ClabWIFIDataRateStatsFramesRetransmissionsSent_Type = Counter64
_ClabWIFIDataRateStatsFramesRetransmissionsSent_Object = MibTableColumn
clabWIFIDataRateStatsFramesRetransmissionsSent = _ClabWIFIDataRateStatsFramesRetransmissionsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 10, 1, 3),
    _ClabWIFIDataRateStatsFramesRetransmissionsSent_Type()
)
clabWIFIDataRateStatsFramesRetransmissionsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsFramesRetransmissionsSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsFramesRetransmissionsSent.setUnits("frames")
_ClabWIFIDataRateStatsFramesReceived_Type = Counter64
_ClabWIFIDataRateStatsFramesReceived_Object = MibTableColumn
clabWIFIDataRateStatsFramesReceived = _ClabWIFIDataRateStatsFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 10, 1, 4),
    _ClabWIFIDataRateStatsFramesReceived_Type()
)
clabWIFIDataRateStatsFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsFramesReceived.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsFramesReceived.setUnits("frames")
_ClabWIFIDataRateStatsFramesDuplicatedReceived_Type = Counter64
_ClabWIFIDataRateStatsFramesDuplicatedReceived_Object = MibTableColumn
clabWIFIDataRateStatsFramesDuplicatedReceived = _ClabWIFIDataRateStatsFramesDuplicatedReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 10, 1, 5),
    _ClabWIFIDataRateStatsFramesDuplicatedReceived_Type()
)
clabWIFIDataRateStatsFramesDuplicatedReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsFramesDuplicatedReceived.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIDataRateStatsFramesDuplicatedReceived.setUnits("frames")
_ClabWIFIPeriodicStatsTable_Object = MibTable
clabWIFIPeriodicStatsTable = _ClabWIFIPeriodicStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11)
)
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsTable.setStatus("current")
_ClabWIFIPeriodicStatsEntry_Object = MibTableRow
clabWIFIPeriodicStatsEntry = _ClabWIFIPeriodicStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1)
)
clabWIFIPeriodicStatsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFISSIDId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIPeriodicStatsInterval"),
    (0, "CLAB-WIFI-MIB", "clabWIFIPeriodicStatsId"),
)
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsEntry.setStatus("current")


class _ClabWIFIPeriodicStatsInterval_Type(Unsigned32):
    """Custom type clabWIFIPeriodicStatsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(96, 96),
    )


_ClabWIFIPeriodicStatsInterval_Type.__name__ = "Unsigned32"
_ClabWIFIPeriodicStatsInterval_Object = MibTableColumn
clabWIFIPeriodicStatsInterval = _ClabWIFIPeriodicStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 1),
    _ClabWIFIPeriodicStatsInterval_Type()
)
clabWIFIPeriodicStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsInterval.setStatus("current")
_ClabWIFIPeriodicStatsId_Type = Unsigned32
_ClabWIFIPeriodicStatsId_Object = MibTableColumn
clabWIFIPeriodicStatsId = _ClabWIFIPeriodicStatsId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 2),
    _ClabWIFIPeriodicStatsId_Type()
)
clabWIFIPeriodicStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsId.setStatus("current")
_ClabWIFIPeriodicStatsDeviceMACAddress_Type = MacAddress
_ClabWIFIPeriodicStatsDeviceMACAddress_Object = MibTableColumn
clabWIFIPeriodicStatsDeviceMACAddress = _ClabWIFIPeriodicStatsDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 3),
    _ClabWIFIPeriodicStatsDeviceMACAddress_Type()
)
clabWIFIPeriodicStatsDeviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDeviceMACAddress.setStatus("current")
_ClabWIFIPeriodicStatsFramesSent_Type = Counter64
_ClabWIFIPeriodicStatsFramesSent_Object = MibTableColumn
clabWIFIPeriodicStatsFramesSent = _ClabWIFIPeriodicStatsFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 4),
    _ClabWIFIPeriodicStatsFramesSent_Type()
)
clabWIFIPeriodicStatsFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsFramesSent.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsFramesSent.setUnits("frames")
_ClabWIFIPeriodicStatsDataFramesSentAck_Type = Counter64
_ClabWIFIPeriodicStatsDataFramesSentAck_Object = MibTableColumn
clabWIFIPeriodicStatsDataFramesSentAck = _ClabWIFIPeriodicStatsDataFramesSentAck_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 5),
    _ClabWIFIPeriodicStatsDataFramesSentAck_Type()
)
clabWIFIPeriodicStatsDataFramesSentAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDataFramesSentAck.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDataFramesSentAck.setUnits("frames")
_ClabWIFIPeriodicStatsDataFramesSentNoAck_Type = Counter64
_ClabWIFIPeriodicStatsDataFramesSentNoAck_Object = MibTableColumn
clabWIFIPeriodicStatsDataFramesSentNoAck = _ClabWIFIPeriodicStatsDataFramesSentNoAck_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 6),
    _ClabWIFIPeriodicStatsDataFramesSentNoAck_Type()
)
clabWIFIPeriodicStatsDataFramesSentNoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDataFramesSentNoAck.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDataFramesSentNoAck.setUnits("frames")
_ClabWIFIPeriodicStatsDataFramesLost_Type = Counter64
_ClabWIFIPeriodicStatsDataFramesLost_Object = MibTableColumn
clabWIFIPeriodicStatsDataFramesLost = _ClabWIFIPeriodicStatsDataFramesLost_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 7),
    _ClabWIFIPeriodicStatsDataFramesLost_Type()
)
clabWIFIPeriodicStatsDataFramesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDataFramesLost.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDataFramesLost.setUnits("frames")
_ClabWIFIPeriodicStatsFramesReceived_Type = Counter64
_ClabWIFIPeriodicStatsFramesReceived_Object = MibTableColumn
clabWIFIPeriodicStatsFramesReceived = _ClabWIFIPeriodicStatsFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 8),
    _ClabWIFIPeriodicStatsFramesReceived_Type()
)
clabWIFIPeriodicStatsFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsFramesReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsFramesReceived.setUnits("frames")
_ClabWIFIPeriodicStatsDataFramesReceived_Type = Counter64
_ClabWIFIPeriodicStatsDataFramesReceived_Object = MibTableColumn
clabWIFIPeriodicStatsDataFramesReceived = _ClabWIFIPeriodicStatsDataFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 9),
    _ClabWIFIPeriodicStatsDataFramesReceived_Type()
)
clabWIFIPeriodicStatsDataFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDataFramesReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDataFramesReceived.setUnits("frames")
_ClabWIFIPeriodicStatsDataFramesDuplicateReceived_Type = Counter64
_ClabWIFIPeriodicStatsDataFramesDuplicateReceived_Object = MibTableColumn
clabWIFIPeriodicStatsDataFramesDuplicateReceived = _ClabWIFIPeriodicStatsDataFramesDuplicateReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 10),
    _ClabWIFIPeriodicStatsDataFramesDuplicateReceived_Type()
)
clabWIFIPeriodicStatsDataFramesDuplicateReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDataFramesDuplicateReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDataFramesDuplicateReceived.setUnits("frames")
_ClabWIFIPeriodicStatsProbesReceived_Type = Counter32
_ClabWIFIPeriodicStatsProbesReceived_Object = MibTableColumn
clabWIFIPeriodicStatsProbesReceived = _ClabWIFIPeriodicStatsProbesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 11),
    _ClabWIFIPeriodicStatsProbesReceived_Type()
)
clabWIFIPeriodicStatsProbesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsProbesReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsProbesReceived.setUnits("probes")
_ClabWIFIPeriodicStatsProbesRejected_Type = Counter32
_ClabWIFIPeriodicStatsProbesRejected_Object = MibTableColumn
clabWIFIPeriodicStatsProbesRejected = _ClabWIFIPeriodicStatsProbesRejected_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 12),
    _ClabWIFIPeriodicStatsProbesRejected_Type()
)
clabWIFIPeriodicStatsProbesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsProbesRejected.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsProbesRejected.setUnits("probes")
_ClabWIFIPeriodicStatsRSSI_Type = Integer32
_ClabWIFIPeriodicStatsRSSI_Object = MibTableColumn
clabWIFIPeriodicStatsRSSI = _ClabWIFIPeriodicStatsRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 13),
    _ClabWIFIPeriodicStatsRSSI_Type()
)
clabWIFIPeriodicStatsRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsRSSI.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsRSSI.setUnits("dBm")
_ClabWIFIPeriodicStatsSNR_Type = Integer32
_ClabWIFIPeriodicStatsSNR_Object = MibTableColumn
clabWIFIPeriodicStatsSNR = _ClabWIFIPeriodicStatsSNR_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 14),
    _ClabWIFIPeriodicStatsSNR_Type()
)
clabWIFIPeriodicStatsSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsSNR.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsSNR.setUnits("dB")
_ClabWIFIPeriodicStatsDisassociations_Type = Counter32
_ClabWIFIPeriodicStatsDisassociations_Object = MibTableColumn
clabWIFIPeriodicStatsDisassociations = _ClabWIFIPeriodicStatsDisassociations_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 15),
    _ClabWIFIPeriodicStatsDisassociations_Type()
)
clabWIFIPeriodicStatsDisassociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDisassociations.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsDisassociations.setUnits("disassociations")
_ClabWIFIPeriodicStatsAuthenticationFailures_Type = Counter32
_ClabWIFIPeriodicStatsAuthenticationFailures_Object = MibTableColumn
clabWIFIPeriodicStatsAuthenticationFailures = _ClabWIFIPeriodicStatsAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 16),
    _ClabWIFIPeriodicStatsAuthenticationFailures_Type()
)
clabWIFIPeriodicStatsAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsAuthenticationFailures.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsAuthenticationFailures.setUnits("authenticationfailures")
_ClabWIFIPeriodicStatsLastTimeAssociation_Type = DateAndTime
_ClabWIFIPeriodicStatsLastTimeAssociation_Object = MibTableColumn
clabWIFIPeriodicStatsLastTimeAssociation = _ClabWIFIPeriodicStatsLastTimeAssociation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 17),
    _ClabWIFIPeriodicStatsLastTimeAssociation_Type()
)
clabWIFIPeriodicStatsLastTimeAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsLastTimeAssociation.setStatus("current")
_ClabWIFIPeriodicStatsLastTimeDisassociation_Type = DateAndTime
_ClabWIFIPeriodicStatsLastTimeDisassociation_Object = MibTableColumn
clabWIFIPeriodicStatsLastTimeDisassociation = _ClabWIFIPeriodicStatsLastTimeDisassociation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 11, 1, 18),
    _ClabWIFIPeriodicStatsLastTimeDisassociation_Type()
)
clabWIFIPeriodicStatsLastTimeDisassociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIPeriodicStatsLastTimeDisassociation.setStatus("current")
_ClabWIFISSIDPolicyTable_Object = MibTable
clabWIFISSIDPolicyTable = _ClabWIFISSIDPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyTable.setStatus("current")
_ClabWIFISSIDPolicyEntry_Object = MibTableRow
clabWIFISSIDPolicyEntry = _ClabWIFISSIDPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1)
)
clabWIFISSIDPolicyEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFISSIDId"),
)
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyEntry.setStatus("current")


class _ClabWIFISSIDPolicyBlockAfterAttempts_Type(Unsigned32):
    """Custom type clabWIFISSIDPolicyBlockAfterAttempts based on Unsigned32"""
    defaultValue = 0


_ClabWIFISSIDPolicyBlockAfterAttempts_Object = MibTableColumn
clabWIFISSIDPolicyBlockAfterAttempts = _ClabWIFISSIDPolicyBlockAfterAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 1),
    _ClabWIFISSIDPolicyBlockAfterAttempts_Type()
)
clabWIFISSIDPolicyBlockAfterAttempts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyBlockAfterAttempts.setStatus("current")


class _ClabWIFISSIDPolicyAllocatedBandwidth_Type(Unsigned32):
    """Custom type clabWIFISSIDPolicyAllocatedBandwidth based on Unsigned32"""
    defaultValue = 0


_ClabWIFISSIDPolicyAllocatedBandwidth_Object = MibTableColumn
clabWIFISSIDPolicyAllocatedBandwidth = _ClabWIFISSIDPolicyAllocatedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 2),
    _ClabWIFISSIDPolicyAllocatedBandwidth_Type()
)
clabWIFISSIDPolicyAllocatedBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyAllocatedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyAllocatedBandwidth.setUnits("Mbps")


class _ClabWIFISSIDPolicyAuthenticationFailures_Type(Unsigned32):
    """Custom type clabWIFISSIDPolicyAuthenticationFailures based on Unsigned32"""
    defaultValue = 0


_ClabWIFISSIDPolicyAuthenticationFailures_Object = MibTableColumn
clabWIFISSIDPolicyAuthenticationFailures = _ClabWIFISSIDPolicyAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 3),
    _ClabWIFISSIDPolicyAuthenticationFailures_Type()
)
clabWIFISSIDPolicyAuthenticationFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyAuthenticationFailures.setStatus("current")


class _ClabWIFISSIDPolicyNonAuthenticatedTraffic_Type(Unsigned32):
    """Custom type clabWIFISSIDPolicyNonAuthenticatedTraffic based on Unsigned32"""
    defaultValue = 0


_ClabWIFISSIDPolicyNonAuthenticatedTraffic_Object = MibTableColumn
clabWIFISSIDPolicyNonAuthenticatedTraffic = _ClabWIFISSIDPolicyNonAuthenticatedTraffic_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 4),
    _ClabWIFISSIDPolicyNonAuthenticatedTraffic_Type()
)
clabWIFISSIDPolicyNonAuthenticatedTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyNonAuthenticatedTraffic.setStatus("current")


class _ClabWIFISSIDPolicyAssociationFailures_Type(Unsigned32):
    """Custom type clabWIFISSIDPolicyAssociationFailures based on Unsigned32"""
    defaultValue = 0


_ClabWIFISSIDPolicyAssociationFailures_Object = MibTableColumn
clabWIFISSIDPolicyAssociationFailures = _ClabWIFISSIDPolicyAssociationFailures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 5),
    _ClabWIFISSIDPolicyAssociationFailures_Type()
)
clabWIFISSIDPolicyAssociationFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyAssociationFailures.setStatus("current")


class _ClabWIFISSIDPolicyStatsInterval_Type(Unsigned32):
    """Custom type clabWIFISSIDPolicyStatsInterval based on Unsigned32"""
    defaultValue = 0


_ClabWIFISSIDPolicyStatsInterval_Object = MibTableColumn
clabWIFISSIDPolicyStatsInterval = _ClabWIFISSIDPolicyStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 6),
    _ClabWIFISSIDPolicyStatsInterval_Type()
)
clabWIFISSIDPolicyStatsInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyStatsInterval.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyStatsInterval.setUnits("minutes")


class _ClabWIFISSIDPolicySNRThreshold_Type(Integer32):
    """Custom type clabWIFISSIDPolicySNRThreshold based on Integer32"""
    defaultValue = -100


_ClabWIFISSIDPolicySNRThreshold_Object = MibTableColumn
clabWIFISSIDPolicySNRThreshold = _ClabWIFISSIDPolicySNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 7),
    _ClabWIFISSIDPolicySNRThreshold_Type()
)
clabWIFISSIDPolicySNRThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicySNRThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicySNRThreshold.setUnits("dB")


class _ClabWIFISSIDPolicyANPIThreshold_Type(Integer32):
    """Custom type clabWIFISSIDPolicyANPIThreshold based on Integer32"""
    defaultValue = -100


_ClabWIFISSIDPolicyANPIThreshold_Object = MibTableColumn
clabWIFISSIDPolicyANPIThreshold = _ClabWIFISSIDPolicyANPIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 8),
    _ClabWIFISSIDPolicyANPIThreshold_Type()
)
clabWIFISSIDPolicyANPIThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyANPIThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyANPIThreshold.setUnits("dBm")


class _ClabWIFISSIDPolicyLowReceivedPowerThreshold_Type(Integer32):
    """Custom type clabWIFISSIDPolicyLowReceivedPowerThreshold based on Integer32"""
    defaultValue = -100


_ClabWIFISSIDPolicyLowReceivedPowerThreshold_Object = MibTableColumn
clabWIFISSIDPolicyLowReceivedPowerThreshold = _ClabWIFISSIDPolicyLowReceivedPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 9),
    _ClabWIFISSIDPolicyLowReceivedPowerThreshold_Type()
)
clabWIFISSIDPolicyLowReceivedPowerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyLowReceivedPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyLowReceivedPowerThreshold.setUnits("dBm")


class _ClabWIFISSIDPolicyLowPowerDeniedAccessThreshold_Type(Integer32):
    """Custom type clabWIFISSIDPolicyLowPowerDeniedAccessThreshold based on Integer32"""
    defaultValue = -100


_ClabWIFISSIDPolicyLowPowerDeniedAccessThreshold_Object = MibTableColumn
clabWIFISSIDPolicyLowPowerDeniedAccessThreshold = _ClabWIFISSIDPolicyLowPowerDeniedAccessThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 10),
    _ClabWIFISSIDPolicyLowPowerDeniedAccessThreshold_Type()
)
clabWIFISSIDPolicyLowPowerDeniedAccessThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyLowPowerDeniedAccessThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyLowPowerDeniedAccessThreshold.setUnits("dBm")


class _ClabWIFISSIDPolicyLowPowerDisassociationThreshold_Type(Integer32):
    """Custom type clabWIFISSIDPolicyLowPowerDisassociationThreshold based on Integer32"""
    defaultValue = -100


_ClabWIFISSIDPolicyLowPowerDisassociationThreshold_Object = MibTableColumn
clabWIFISSIDPolicyLowPowerDisassociationThreshold = _ClabWIFISSIDPolicyLowPowerDisassociationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 11),
    _ClabWIFISSIDPolicyLowPowerDisassociationThreshold_Type()
)
clabWIFISSIDPolicyLowPowerDisassociationThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyLowPowerDisassociationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyLowPowerDisassociationThreshold.setUnits("dBm")
_ClabWIFISSIDPolicyRowStatus_Type = RowStatus
_ClabWIFISSIDPolicyRowStatus_Object = MibTableColumn
clabWIFISSIDPolicyRowStatus = _ClabWIFISSIDPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 12),
    _ClabWIFISSIDPolicyRowStatus_Type()
)
clabWIFISSIDPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyRowStatus.setStatus("current")
_ClabWIFISSIDPolicyBeaconMcsLevelInUse_Type = SnmpAdminString
_ClabWIFISSIDPolicyBeaconMcsLevelInUse_Object = MibTableColumn
clabWIFISSIDPolicyBeaconMcsLevelInUse = _ClabWIFISSIDPolicyBeaconMcsLevelInUse_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 13),
    _ClabWIFISSIDPolicyBeaconMcsLevelInUse_Type()
)
clabWIFISSIDPolicyBeaconMcsLevelInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyBeaconMcsLevelInUse.setStatus("current")
_ClabWIFISSIDPolicyBeaconMcsLevelsSupported_Type = SnmpAdminString
_ClabWIFISSIDPolicyBeaconMcsLevelsSupported_Object = MibTableColumn
clabWIFISSIDPolicyBeaconMcsLevelsSupported = _ClabWIFISSIDPolicyBeaconMcsLevelsSupported_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 12, 1, 14),
    _ClabWIFISSIDPolicyBeaconMcsLevelsSupported_Type()
)
clabWIFISSIDPolicyBeaconMcsLevelsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFISSIDPolicyBeaconMcsLevelsSupported.setStatus("current")
_ClabWIFIClientSessionsTable_Object = MibTable
clabWIFIClientSessionsTable = _ClabWIFIClientSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 13)
)
if mibBuilder.loadTexts:
    clabWIFIClientSessionsTable.setStatus("current")
_ClabWIFIClientSessionsEntry_Object = MibTableRow
clabWIFIClientSessionsEntry = _ClabWIFIClientSessionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 13, 1)
)
clabWIFIClientSessionsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIClientSessionsId"),
)
if mibBuilder.loadTexts:
    clabWIFIClientSessionsEntry.setStatus("current")
_ClabWIFIClientSessionsId_Type = Unsigned32
_ClabWIFIClientSessionsId_Object = MibTableColumn
clabWIFIClientSessionsId = _ClabWIFIClientSessionsId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 13, 1, 1),
    _ClabWIFIClientSessionsId_Type()
)
clabWIFIClientSessionsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIClientSessionsId.setStatus("current")
_ClabWIFIClientSessionsDeviceMACAddress_Type = MacAddress
_ClabWIFIClientSessionsDeviceMACAddress_Object = MibTableColumn
clabWIFIClientSessionsDeviceMACAddress = _ClabWIFIClientSessionsDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 13, 1, 2),
    _ClabWIFIClientSessionsDeviceMACAddress_Type()
)
clabWIFIClientSessionsDeviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientSessionsDeviceMACAddress.setStatus("current")
_ClabWIFIClientSessionsStart_Type = DateAndTime
_ClabWIFIClientSessionsStart_Object = MibTableColumn
clabWIFIClientSessionsStart = _ClabWIFIClientSessionsStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 13, 1, 3),
    _ClabWIFIClientSessionsStart_Type()
)
clabWIFIClientSessionsStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientSessionsStart.setStatus("current")
_ClabWIFIClientSessionsStop_Type = DateAndTime
_ClabWIFIClientSessionsStop_Object = MibTableColumn
clabWIFIClientSessionsStop = _ClabWIFIClientSessionsStop_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 13, 1, 4),
    _ClabWIFIClientSessionsStop_Type()
)
clabWIFIClientSessionsStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientSessionsStop.setStatus("current")
_ClabWIFIClientSessionsTerminationCode_Type = Unsigned32
_ClabWIFIClientSessionsTerminationCode_Object = MibTableColumn
clabWIFIClientSessionsTerminationCode = _ClabWIFIClientSessionsTerminationCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 13, 1, 5),
    _ClabWIFIClientSessionsTerminationCode_Type()
)
clabWIFIClientSessionsTerminationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientSessionsTerminationCode.setStatus("current")


class _ClabWIFIClientSessionsTerminationMeaning_Type(SnmpAdminString):
    """Custom type clabWIFIClientSessionsTerminationMeaning based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClabWIFIClientSessionsTerminationMeaning_Type.__name__ = "SnmpAdminString"
_ClabWIFIClientSessionsTerminationMeaning_Object = MibTableColumn
clabWIFIClientSessionsTerminationMeaning = _ClabWIFIClientSessionsTerminationMeaning_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 13, 1, 6),
    _ClabWIFIClientSessionsTerminationMeaning_Type()
)
clabWIFIClientSessionsTerminationMeaning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientSessionsTerminationMeaning.setStatus("current")
_ClabWIFIClientStatsTable_Object = MibTable
clabWIFIClientStatsTable = _ClabWIFIClientStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14)
)
if mibBuilder.loadTexts:
    clabWIFIClientStatsTable.setStatus("current")
_ClabWIFIClientStatsEntry_Object = MibTableRow
clabWIFIClientStatsEntry = _ClabWIFIClientStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1)
)
clabWIFIClientStatsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIClientStatsInterval"),
    (0, "CLAB-WIFI-MIB", "clabWIFIClientStatsId"),
)
if mibBuilder.loadTexts:
    clabWIFIClientStatsEntry.setStatus("current")


class _ClabWIFIClientStatsInterval_Type(Unsigned32):
    """Custom type clabWIFIClientStatsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(96, 96),
    )


_ClabWIFIClientStatsInterval_Type.__name__ = "Unsigned32"
_ClabWIFIClientStatsInterval_Object = MibTableColumn
clabWIFIClientStatsInterval = _ClabWIFIClientStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 1),
    _ClabWIFIClientStatsInterval_Type()
)
clabWIFIClientStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIClientStatsInterval.setStatus("current")
_ClabWIFIClientStatsId_Type = Unsigned32
_ClabWIFIClientStatsId_Object = MibTableColumn
clabWIFIClientStatsId = _ClabWIFIClientStatsId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 2),
    _ClabWIFIClientStatsId_Type()
)
clabWIFIClientStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIClientStatsId.setStatus("current")
_ClabWIFIClientStatsDeviceMACAddress_Type = MacAddress
_ClabWIFIClientStatsDeviceMACAddress_Object = MibTableColumn
clabWIFIClientStatsDeviceMACAddress = _ClabWIFIClientStatsDeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 3),
    _ClabWIFIClientStatsDeviceMACAddress_Type()
)
clabWIFIClientStatsDeviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDeviceMACAddress.setStatus("current")
_ClabWIFIClientStatsFramesSent_Type = Counter64
_ClabWIFIClientStatsFramesSent_Object = MibTableColumn
clabWIFIClientStatsFramesSent = _ClabWIFIClientStatsFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 4),
    _ClabWIFIClientStatsFramesSent_Type()
)
clabWIFIClientStatsFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsFramesSent.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsFramesSent.setUnits("frames")
_ClabWIFIClientStatsDataFramesSentAck_Type = Counter64
_ClabWIFIClientStatsDataFramesSentAck_Object = MibTableColumn
clabWIFIClientStatsDataFramesSentAck = _ClabWIFIClientStatsDataFramesSentAck_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 5),
    _ClabWIFIClientStatsDataFramesSentAck_Type()
)
clabWIFIClientStatsDataFramesSentAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDataFramesSentAck.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDataFramesSentAck.setUnits("frames")
_ClabWIFIClientStatsDataFramesSentNoAck_Type = Counter64
_ClabWIFIClientStatsDataFramesSentNoAck_Object = MibTableColumn
clabWIFIClientStatsDataFramesSentNoAck = _ClabWIFIClientStatsDataFramesSentNoAck_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 6),
    _ClabWIFIClientStatsDataFramesSentNoAck_Type()
)
clabWIFIClientStatsDataFramesSentNoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDataFramesSentNoAck.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDataFramesSentNoAck.setUnits("frames")
_ClabWIFIClientStatsDataFramesLost_Type = Counter64
_ClabWIFIClientStatsDataFramesLost_Object = MibTableColumn
clabWIFIClientStatsDataFramesLost = _ClabWIFIClientStatsDataFramesLost_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 7),
    _ClabWIFIClientStatsDataFramesLost_Type()
)
clabWIFIClientStatsDataFramesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDataFramesLost.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDataFramesLost.setUnits("frames")
_ClabWIFIClientStatsFramesReceived_Type = Counter64
_ClabWIFIClientStatsFramesReceived_Object = MibTableColumn
clabWIFIClientStatsFramesReceived = _ClabWIFIClientStatsFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 8),
    _ClabWIFIClientStatsFramesReceived_Type()
)
clabWIFIClientStatsFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsFramesReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsFramesReceived.setUnits("frames")
_ClabWIFIClientStatsDataFramesReceived_Type = Counter64
_ClabWIFIClientStatsDataFramesReceived_Object = MibTableColumn
clabWIFIClientStatsDataFramesReceived = _ClabWIFIClientStatsDataFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 9),
    _ClabWIFIClientStatsDataFramesReceived_Type()
)
clabWIFIClientStatsDataFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDataFramesReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDataFramesReceived.setUnits("frames")
_ClabWIFIClientStatsDataFramesDuplicateReceived_Type = Counter64
_ClabWIFIClientStatsDataFramesDuplicateReceived_Object = MibTableColumn
clabWIFIClientStatsDataFramesDuplicateReceived = _ClabWIFIClientStatsDataFramesDuplicateReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 10),
    _ClabWIFIClientStatsDataFramesDuplicateReceived_Type()
)
clabWIFIClientStatsDataFramesDuplicateReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDataFramesDuplicateReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDataFramesDuplicateReceived.setUnits("frames")
_ClabWIFIClientStatsProbesReceived_Type = Counter32
_ClabWIFIClientStatsProbesReceived_Object = MibTableColumn
clabWIFIClientStatsProbesReceived = _ClabWIFIClientStatsProbesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 11),
    _ClabWIFIClientStatsProbesReceived_Type()
)
clabWIFIClientStatsProbesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsProbesReceived.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsProbesReceived.setUnits("probes")
_ClabWIFIClientStatsProbesRejected_Type = Counter32
_ClabWIFIClientStatsProbesRejected_Object = MibTableColumn
clabWIFIClientStatsProbesRejected = _ClabWIFIClientStatsProbesRejected_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 12),
    _ClabWIFIClientStatsProbesRejected_Type()
)
clabWIFIClientStatsProbesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsProbesRejected.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsProbesRejected.setUnits("probes")
_ClabWIFIClientStatsRSSI_Type = Integer32
_ClabWIFIClientStatsRSSI_Object = MibTableColumn
clabWIFIClientStatsRSSI = _ClabWIFIClientStatsRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 13),
    _ClabWIFIClientStatsRSSI_Type()
)
clabWIFIClientStatsRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsRSSI.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsRSSI.setUnits("dBm")
_ClabWIFIClientStatsSNR_Type = Integer32
_ClabWIFIClientStatsSNR_Object = MibTableColumn
clabWIFIClientStatsSNR = _ClabWIFIClientStatsSNR_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 14),
    _ClabWIFIClientStatsSNR_Type()
)
clabWIFIClientStatsSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsSNR.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsSNR.setUnits("dB")
_ClabWIFIClientStatsDisassociations_Type = Counter32
_ClabWIFIClientStatsDisassociations_Object = MibTableColumn
clabWIFIClientStatsDisassociations = _ClabWIFIClientStatsDisassociations_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 15),
    _ClabWIFIClientStatsDisassociations_Type()
)
clabWIFIClientStatsDisassociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDisassociations.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsDisassociations.setUnits("disassociations")
_ClabWIFIClientStatsAuthenticationFailures_Type = Counter32
_ClabWIFIClientStatsAuthenticationFailures_Object = MibTableColumn
clabWIFIClientStatsAuthenticationFailures = _ClabWIFIClientStatsAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 16),
    _ClabWIFIClientStatsAuthenticationFailures_Type()
)
clabWIFIClientStatsAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsAuthenticationFailures.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIClientStatsAuthenticationFailures.setUnits("authenticationfailures")
_ClabWIFIClientStatsLastTimeAssociation_Type = DateAndTime
_ClabWIFIClientStatsLastTimeAssociation_Object = MibTableColumn
clabWIFIClientStatsLastTimeAssociation = _ClabWIFIClientStatsLastTimeAssociation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 17),
    _ClabWIFIClientStatsLastTimeAssociation_Type()
)
clabWIFIClientStatsLastTimeAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsLastTimeAssociation.setStatus("current")
_ClabWIFIClientStatsLastTimeDisassociation_Type = DateAndTime
_ClabWIFIClientStatsLastTimeDisassociation_Object = MibTableColumn
clabWIFIClientStatsLastTimeDisassociation = _ClabWIFIClientStatsLastTimeDisassociation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 18),
    _ClabWIFIClientStatsLastTimeDisassociation_Type()
)
clabWIFIClientStatsLastTimeDisassociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsLastTimeDisassociation.setStatus("current")
_ClabWIFIClientStatsThroughput_Type = Unsigned32
_ClabWIFIClientStatsThroughput_Object = MibTableColumn
clabWIFIClientStatsThroughput = _ClabWIFIClientStatsThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 19),
    _ClabWIFIClientStatsThroughput_Type()
)
clabWIFIClientStatsThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsThroughput.setStatus("current")
_ClabWIFIClientStatsPktErrorRatePerSTA_Type = Unsigned32
_ClabWIFIClientStatsPktErrorRatePerSTA_Object = MibTableColumn
clabWIFIClientStatsPktErrorRatePerSTA = _ClabWIFIClientStatsPktErrorRatePerSTA_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 14, 1, 20),
    _ClabWIFIClientStatsPktErrorRatePerSTA_Type()
)
clabWIFIClientStatsPktErrorRatePerSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIClientStatsPktErrorRatePerSTA.setStatus("current")
_ClabWIFIRadiusClientTable_Object = MibTable
clabWIFIRadiusClientTable = _ClabWIFIRadiusClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15)
)
if mibBuilder.loadTexts:
    clabWIFIRadiusClientTable.setStatus("current")
_ClabWIFIRadiusClientEntry_Object = MibTableRow
clabWIFIRadiusClientEntry = _ClabWIFIRadiusClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1)
)
clabWIFIRadiusClientEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIRadiusClientEntry.setStatus("current")
_ClabWIFIRadiusClientNASIdentifier_Type = SnmpAdminString
_ClabWIFIRadiusClientNASIdentifier_Object = MibTableColumn
clabWIFIRadiusClientNASIdentifier = _ClabWIFIRadiusClientNASIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1, 1),
    _ClabWIFIRadiusClientNASIdentifier_Type()
)
clabWIFIRadiusClientNASIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIRadiusClientNASIdentifier.setStatus("current")


class _ClabWIFIRadiusClientLocationPolicy_Type(OctetString):
    """Custom type clabWIFIRadiusClientLocationPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabWIFIRadiusClientLocationPolicy_Type.__name__ = "OctetString"
_ClabWIFIRadiusClientLocationPolicy_Object = MibTableColumn
clabWIFIRadiusClientLocationPolicy = _ClabWIFIRadiusClientLocationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1, 2),
    _ClabWIFIRadiusClientLocationPolicy_Type()
)
clabWIFIRadiusClientLocationPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIRadiusClientLocationPolicy.setStatus("current")


class _ClabWIFIRadiusClientOperatorName_Type(SnmpAdminString):
    """Custom type clabWIFIRadiusClientOperatorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClabWIFIRadiusClientOperatorName_Type.__name__ = "SnmpAdminString"
_ClabWIFIRadiusClientOperatorName_Object = MibTableColumn
clabWIFIRadiusClientOperatorName = _ClabWIFIRadiusClientOperatorName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1, 3),
    _ClabWIFIRadiusClientOperatorName_Type()
)
clabWIFIRadiusClientOperatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIRadiusClientOperatorName.setStatus("current")


class _ClabWIFIRadiusClientLocationInformation_Type(OctetString):
    """Custom type clabWIFIRadiusClientLocationInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_ClabWIFIRadiusClientLocationInformation_Type.__name__ = "OctetString"
_ClabWIFIRadiusClientLocationInformation_Object = MibTableColumn
clabWIFIRadiusClientLocationInformation = _ClabWIFIRadiusClientLocationInformation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1, 4),
    _ClabWIFIRadiusClientLocationInformation_Type()
)
clabWIFIRadiusClientLocationInformation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIRadiusClientLocationInformation.setStatus("current")


class _ClabWIFIRadiusClientLocationData_Type(OctetString):
    """Custom type clabWIFIRadiusClientLocationData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_ClabWIFIRadiusClientLocationData_Type.__name__ = "OctetString"
_ClabWIFIRadiusClientLocationData_Object = MibTableColumn
clabWIFIRadiusClientLocationData = _ClabWIFIRadiusClientLocationData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1, 5),
    _ClabWIFIRadiusClientLocationData_Type()
)
clabWIFIRadiusClientLocationData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIRadiusClientLocationData.setStatus("current")


class _ClabWIFIRadiusClientUsageReports_Type(TruthValue):
    """Custom type clabWIFIRadiusClientUsageReports based on TruthValue"""


_ClabWIFIRadiusClientUsageReports_Object = MibTableColumn
clabWIFIRadiusClientUsageReports = _ClabWIFIRadiusClientUsageReports_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1, 6),
    _ClabWIFIRadiusClientUsageReports_Type()
)
clabWIFIRadiusClientUsageReports.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIRadiusClientUsageReports.setStatus("current")


class _ClabWIFIRadiusClientIntervalInterimReport_Type(TruthValue):
    """Custom type clabWIFIRadiusClientIntervalInterimReport based on TruthValue"""


_ClabWIFIRadiusClientIntervalInterimReport_Object = MibTableColumn
clabWIFIRadiusClientIntervalInterimReport = _ClabWIFIRadiusClientIntervalInterimReport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1, 7),
    _ClabWIFIRadiusClientIntervalInterimReport_Type()
)
clabWIFIRadiusClientIntervalInterimReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIRadiusClientIntervalInterimReport.setStatus("current")


class _ClabWIFIRadiusClientAPTransitionReport_Type(TruthValue):
    """Custom type clabWIFIRadiusClientAPTransitionReport based on TruthValue"""


_ClabWIFIRadiusClientAPTransitionReport_Object = MibTableColumn
clabWIFIRadiusClientAPTransitionReport = _ClabWIFIRadiusClientAPTransitionReport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1, 8),
    _ClabWIFIRadiusClientAPTransitionReport_Type()
)
clabWIFIRadiusClientAPTransitionReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIRadiusClientAPTransitionReport.setStatus("current")


class _ClabWIFIRadiusClientGigawordReport_Type(TruthValue):
    """Custom type clabWIFIRadiusClientGigawordReport based on TruthValue"""


_ClabWIFIRadiusClientGigawordReport_Object = MibTableColumn
clabWIFIRadiusClientGigawordReport = _ClabWIFIRadiusClientGigawordReport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1, 9),
    _ClabWIFIRadiusClientGigawordReport_Type()
)
clabWIFIRadiusClientGigawordReport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIRadiusClientGigawordReport.setStatus("current")
_ClabWIFIRadiusClientRowStatus_Type = RowStatus
_ClabWIFIRadiusClientRowStatus_Object = MibTableColumn
clabWIFIRadiusClientRowStatus = _ClabWIFIRadiusClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 15, 1, 10),
    _ClabWIFIRadiusClientRowStatus_Type()
)
clabWIFIRadiusClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIRadiusClientRowStatus.setStatus("current")
_ClabWIFIWIFICommitSettings_ObjectIdentity = ObjectIdentity
clabWIFIWIFICommitSettings = _ClabWIFIWIFICommitSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 16)
)
_ClabWIFIWIFICommitSettingsValue_Type = TruthValue
_ClabWIFIWIFICommitSettingsValue_Object = MibScalar
clabWIFIWIFICommitSettingsValue = _ClabWIFIWIFICommitSettingsValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 16, 1),
    _ClabWIFIWIFICommitSettingsValue_Type()
)
clabWIFIWIFICommitSettingsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIWIFICommitSettingsValue.setStatus("deprecated")
_ClabWIFIApNeighborStatsTable_Object = MibTable
clabWIFIApNeighborStatsTable = _ClabWIFIApNeighborStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 17)
)
if mibBuilder.loadTexts:
    clabWIFIApNeighborStatsTable.setStatus("deprecated")
_ClabWIFIApNeighborStatsEntry_Object = MibTableRow
clabWIFIApNeighborStatsEntry = _ClabWIFIApNeighborStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 17, 1)
)
clabWIFIApNeighborStatsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIApNeighborStatsEntry.setStatus("deprecated")


class _ClabWIFIApNeighborStatsSSID_Type(SnmpAdminString):
    """Custom type clabWIFIApNeighborStatsSSID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClabWIFIApNeighborStatsSSID_Type.__name__ = "SnmpAdminString"
_ClabWIFIApNeighborStatsSSID_Object = MibTableColumn
clabWIFIApNeighborStatsSSID = _ClabWIFIApNeighborStatsSSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 17, 1, 1),
    _ClabWIFIApNeighborStatsSSID_Type()
)
clabWIFIApNeighborStatsSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIApNeighborStatsSSID.setStatus("deprecated")


class _ClabWIFIApNeighborStatsCurrentChannel_Type(Unsigned32):
    """Custom type clabWIFIApNeighborStatsCurrentChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClabWIFIApNeighborStatsCurrentChannel_Type.__name__ = "Unsigned32"
_ClabWIFIApNeighborStatsCurrentChannel_Object = MibTableColumn
clabWIFIApNeighborStatsCurrentChannel = _ClabWIFIApNeighborStatsCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 17, 1, 2),
    _ClabWIFIApNeighborStatsCurrentChannel_Type()
)
clabWIFIApNeighborStatsCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIApNeighborStatsCurrentChannel.setStatus("deprecated")


class _ClabWIFIApNeighborStatsCurrentBandwidth_Type(Unsigned32):
    """Custom type clabWIFIApNeighborStatsCurrentBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(160, 160),
    )


_ClabWIFIApNeighborStatsCurrentBandwidth_Type.__name__ = "Unsigned32"
_ClabWIFIApNeighborStatsCurrentBandwidth_Object = MibTableColumn
clabWIFIApNeighborStatsCurrentBandwidth = _ClabWIFIApNeighborStatsCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 17, 1, 3),
    _ClabWIFIApNeighborStatsCurrentBandwidth_Type()
)
clabWIFIApNeighborStatsCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIApNeighborStatsCurrentBandwidth.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIApNeighborStatsCurrentBandwidth.setUnits("MHz")
_ClabWIFIApNeighborStatsRSSI_Type = Integer32
_ClabWIFIApNeighborStatsRSSI_Object = MibTableColumn
clabWIFIApNeighborStatsRSSI = _ClabWIFIApNeighborStatsRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 17, 1, 4),
    _ClabWIFIApNeighborStatsRSSI_Type()
)
clabWIFIApNeighborStatsRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIApNeighborStatsRSSI.setStatus("deprecated")
if mibBuilder.loadTexts:
    clabWIFIApNeighborStatsRSSI.setUnits("dBm")
_ClabWIFIAccessPointAccessControlFilter_ObjectIdentity = ObjectIdentity
clabWIFIAccessPointAccessControlFilter = _ClabWIFIAccessPointAccessControlFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 18)
)
_ClabWIFIAccessPointClearAccessControlFilterTable_Type = TruthValue
_ClabWIFIAccessPointClearAccessControlFilterTable_Object = MibScalar
clabWIFIAccessPointClearAccessControlFilterTable = _ClabWIFIAccessPointClearAccessControlFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 18, 1),
    _ClabWIFIAccessPointClearAccessControlFilterTable_Type()
)
clabWIFIAccessPointClearAccessControlFilterTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointClearAccessControlFilterTable.setStatus("current")
_ClabWIFIAccessPointAccessControlFilterAccessAllow_Type = TruthValue
_ClabWIFIAccessPointAccessControlFilterAccessAllow_Object = MibScalar
clabWIFIAccessPointAccessControlFilterAccessAllow = _ClabWIFIAccessPointAccessControlFilterAccessAllow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 18, 2),
    _ClabWIFIAccessPointAccessControlFilterAccessAllow_Type()
)
clabWIFIAccessPointAccessControlFilterAccessAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccessControlFilterAccessAllow.setStatus("current")
_ClabWIFIAccessPointAccessControlFilterTable_Object = MibTable
clabWIFIAccessPointAccessControlFilterTable = _ClabWIFIAccessPointAccessControlFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 18, 3)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccessControlFilterTable.setStatus("current")
_ClabWIFIAccessPointAccessControlFilterEntry_Object = MibTableRow
clabWIFIAccessPointAccessControlFilterEntry = _ClabWIFIAccessPointAccessControlFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 18, 3, 1)
)
clabWIFIAccessPointAccessControlFilterEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointAccessControlFilterIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccessControlFilterEntry.setStatus("current")
_ClabWIFIAccessPointAccessControlFilterIndex_Type = Unsigned32
_ClabWIFIAccessPointAccessControlFilterIndex_Object = MibTableColumn
clabWIFIAccessPointAccessControlFilterIndex = _ClabWIFIAccessPointAccessControlFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 18, 3, 1, 1),
    _ClabWIFIAccessPointAccessControlFilterIndex_Type()
)
clabWIFIAccessPointAccessControlFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccessControlFilterIndex.setStatus("current")
_ClabWIFIAccessPointAccessControlFilterMACAddress_Type = MacAddress
_ClabWIFIAccessPointAccessControlFilterMACAddress_Object = MibTableColumn
clabWIFIAccessPointAccessControlFilterMACAddress = _ClabWIFIAccessPointAccessControlFilterMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 18, 3, 1, 2),
    _ClabWIFIAccessPointAccessControlFilterMACAddress_Type()
)
clabWIFIAccessPointAccessControlFilterMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccessControlFilterMACAddress.setStatus("current")
_ClabWIFIAccessPointAccessControlFilterNumberOfEntries_Type = Integer32
_ClabWIFIAccessPointAccessControlFilterNumberOfEntries_Object = MibScalar
clabWIFIAccessPointAccessControlFilterNumberOfEntries = _ClabWIFIAccessPointAccessControlFilterNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 18, 4),
    _ClabWIFIAccessPointAccessControlFilterNumberOfEntries_Type()
)
clabWIFIAccessPointAccessControlFilterNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccessControlFilterNumberOfEntries.setStatus("current")
_ClabWIFIAccessPointPasspoint_ObjectIdentity = ObjectIdentity
clabWIFIAccessPointPasspoint = _ClabWIFIAccessPointPasspoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19)
)
_ClabWIFIAccessPointInterworkingServiceTable_Object = MibTable
clabWIFIAccessPointInterworkingServiceTable = _ClabWIFIAccessPointInterworkingServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointInterworkingServiceTable.setStatus("current")
_ClabWIFIAccessPointInterworkingServiceEntry_Object = MibTableRow
clabWIFIAccessPointInterworkingServiceEntry = _ClabWIFIAccessPointInterworkingServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 1, 1)
)
clabWIFIAccessPointInterworkingServiceEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointInterworkingServiceEntry.setStatus("current")
_ClabWIFIAccessPointInterworkingServiceInternet_Type = TruthValue
_ClabWIFIAccessPointInterworkingServiceInternet_Object = MibTableColumn
clabWIFIAccessPointInterworkingServiceInternet = _ClabWIFIAccessPointInterworkingServiceInternet_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 1, 1, 1),
    _ClabWIFIAccessPointInterworkingServiceInternet_Type()
)
clabWIFIAccessPointInterworkingServiceInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointInterworkingServiceInternet.setStatus("current")
_ClabWIFIAccessPointInterworkingServiceHESSID_Type = MacAddress
_ClabWIFIAccessPointInterworkingServiceHESSID_Object = MibTableColumn
clabWIFIAccessPointInterworkingServiceHESSID = _ClabWIFIAccessPointInterworkingServiceHESSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 1, 1, 2),
    _ClabWIFIAccessPointInterworkingServiceHESSID_Type()
)
clabWIFIAccessPointInterworkingServiceHESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointInterworkingServiceHESSID.setStatus("current")


class _ClabWIFIAccessPointInterworkingServiceAccessNetworkType_Type(OctetString):
    """Custom type clabWIFIAccessPointInterworkingServiceAccessNetworkType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ClabWIFIAccessPointInterworkingServiceAccessNetworkType_Type.__name__ = "OctetString"
_ClabWIFIAccessPointInterworkingServiceAccessNetworkType_Object = MibTableColumn
clabWIFIAccessPointInterworkingServiceAccessNetworkType = _ClabWIFIAccessPointInterworkingServiceAccessNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 1, 1, 3),
    _ClabWIFIAccessPointInterworkingServiceAccessNetworkType_Type()
)
clabWIFIAccessPointInterworkingServiceAccessNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointInterworkingServiceAccessNetworkType.setStatus("current")


class _ClabWIFIAccessPointInterworkingServiceVenueGroupCode_Type(OctetString):
    """Custom type clabWIFIAccessPointInterworkingServiceVenueGroupCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ClabWIFIAccessPointInterworkingServiceVenueGroupCode_Type.__name__ = "OctetString"
_ClabWIFIAccessPointInterworkingServiceVenueGroupCode_Object = MibTableColumn
clabWIFIAccessPointInterworkingServiceVenueGroupCode = _ClabWIFIAccessPointInterworkingServiceVenueGroupCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 1, 1, 4),
    _ClabWIFIAccessPointInterworkingServiceVenueGroupCode_Type()
)
clabWIFIAccessPointInterworkingServiceVenueGroupCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointInterworkingServiceVenueGroupCode.setStatus("current")


class _ClabWIFIAccessPointInterworkingServiceVenueTypeCode_Type(OctetString):
    """Custom type clabWIFIAccessPointInterworkingServiceVenueTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ClabWIFIAccessPointInterworkingServiceVenueTypeCode_Type.__name__ = "OctetString"
_ClabWIFIAccessPointInterworkingServiceVenueTypeCode_Object = MibTableColumn
clabWIFIAccessPointInterworkingServiceVenueTypeCode = _ClabWIFIAccessPointInterworkingServiceVenueTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 1, 1, 5),
    _ClabWIFIAccessPointInterworkingServiceVenueTypeCode_Type()
)
clabWIFIAccessPointInterworkingServiceVenueTypeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointInterworkingServiceVenueTypeCode.setStatus("current")
_ClabWIFIAccessPointPasspointTable_Object = MibTable
clabWIFIAccessPointPasspointTable = _ClabWIFIAccessPointPasspointTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointTable.setStatus("current")
_ClabWIFIAccessPointPasspointEntry_Object = MibTableRow
clabWIFIAccessPointPasspointEntry = _ClabWIFIAccessPointPasspointEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1)
)
clabWIFIAccessPointPasspointEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointEntry.setStatus("current")


class _ClabWIFIAccessPointPasspointCapabilityList_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointCapabilityList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClabWIFIAccessPointPasspointCapabilityList_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointCapabilityList_Object = MibTableColumn
clabWIFIAccessPointPasspointCapabilityList = _ClabWIFIAccessPointPasspointCapabilityList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1, 1),
    _ClabWIFIAccessPointPasspointCapabilityList_Type()
)
clabWIFIAccessPointPasspointCapabilityList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointCapabilityList.setStatus("deprecated")
_ClabWIFIAccessPointPasspointOnlineSignupSupported_Type = TruthValue
_ClabWIFIAccessPointPasspointOnlineSignupSupported_Object = MibTableColumn
clabWIFIAccessPointPasspointOnlineSignupSupported = _ClabWIFIAccessPointPasspointOnlineSignupSupported_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1, 2),
    _ClabWIFIAccessPointPasspointOnlineSignupSupported_Type()
)
clabWIFIAccessPointPasspointOnlineSignupSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOnlineSignupSupported.setStatus("current")
_ClabWIFIAccessPointPasspointDGAFEnable_Type = TruthValue
_ClabWIFIAccessPointPasspointDGAFEnable_Object = MibTableColumn
clabWIFIAccessPointPasspointDGAFEnable = _ClabWIFIAccessPointPasspointDGAFEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1, 3),
    _ClabWIFIAccessPointPasspointDGAFEnable_Type()
)
clabWIFIAccessPointPasspointDGAFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointDGAFEnable.setStatus("current")
_ClabWIFIAccessPointPasspointP2PEnable_Type = TruthValue
_ClabWIFIAccessPointPasspointP2PEnable_Object = MibTableColumn
clabWIFIAccessPointPasspointP2PEnable = _ClabWIFIAccessPointPasspointP2PEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1, 4),
    _ClabWIFIAccessPointPasspointP2PEnable_Type()
)
clabWIFIAccessPointPasspointP2PEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointP2PEnable.setStatus("current")
_ClabWIFIAccessPointPasspointQoSMappingEnable_Type = TruthValue
_ClabWIFIAccessPointPasspointQoSMappingEnable_Object = MibTableColumn
clabWIFIAccessPointPasspointQoSMappingEnable = _ClabWIFIAccessPointPasspointQoSMappingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1, 5),
    _ClabWIFIAccessPointPasspointQoSMappingEnable_Type()
)
clabWIFIAccessPointPasspointQoSMappingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointQoSMappingEnable.setStatus("current")
_ClabWIFIAccessPointPasspointASRAEnable_Type = TruthValue
_ClabWIFIAccessPointPasspointASRAEnable_Object = MibTableColumn
clabWIFIAccessPointPasspointASRAEnable = _ClabWIFIAccessPointPasspointASRAEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1, 6),
    _ClabWIFIAccessPointPasspointASRAEnable_Type()
)
clabWIFIAccessPointPasspointASRAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointASRAEnable.setStatus("current")
_ClabWIFIAccessPointPasspointANQPDomainID_Type = Integer32
_ClabWIFIAccessPointPasspointANQPDomainID_Object = MibTableColumn
clabWIFIAccessPointPasspointANQPDomainID = _ClabWIFIAccessPointPasspointANQPDomainID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1, 7),
    _ClabWIFIAccessPointPasspointANQPDomainID_Type()
)
clabWIFIAccessPointPasspointANQPDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointANQPDomainID.setStatus("current")
_ClabWIFIAccessPointPasspointEAPMethod_Type = OctetString
_ClabWIFIAccessPointPasspointEAPMethod_Object = MibTableColumn
clabWIFIAccessPointPasspointEAPMethod = _ClabWIFIAccessPointPasspointEAPMethod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1, 8),
    _ClabWIFIAccessPointPasspointEAPMethod_Type()
)
clabWIFIAccessPointPasspointEAPMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointEAPMethod.setStatus("current")
_ClabWIFIAccessPointPasspointManagementFrameProtectionEnable_Type = TruthValue
_ClabWIFIAccessPointPasspointManagementFrameProtectionEnable_Object = MibTableColumn
clabWIFIAccessPointPasspointManagementFrameProtectionEnable = _ClabWIFIAccessPointPasspointManagementFrameProtectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1, 9),
    _ClabWIFIAccessPointPasspointManagementFrameProtectionEnable_Type()
)
clabWIFIAccessPointPasspointManagementFrameProtectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointManagementFrameProtectionEnable.setStatus("current")


class _ClabWIFIAccessPointPasspointCapabilities_Type(Bits):
    """Custom type clabWIFIAccessPointPasspointCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("connectionCapability", 4),
          ("hsCapabilityList", 1),
          ("hsQueryList", 0),
          ("iconBinaryFile", 10),
          ("iconRequest", 9),
          ("naiHomeRealmQuery", 5),
          ("operatingClassIndication", 6),
          ("operatorFriendlyName", 2),
          ("osuProvidersList", 7),
          ("reserved", 8),
          ("wanMetrics", 3))
    )

_ClabWIFIAccessPointPasspointCapabilities_Type.__name__ = "Bits"
_ClabWIFIAccessPointPasspointCapabilities_Object = MibTableColumn
clabWIFIAccessPointPasspointCapabilities = _ClabWIFIAccessPointPasspointCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 2, 1, 10),
    _ClabWIFIAccessPointPasspointCapabilities_Type()
)
clabWIFIAccessPointPasspointCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointCapabilities.setStatus("current")
_ClabWIFIAccessPointPasspointVenueNamesTable_Object = MibTable
clabWIFIAccessPointPasspointVenueNamesTable = _ClabWIFIAccessPointPasspointVenueNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 3)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointVenueNamesTable.setStatus("deprecated")
_ClabWIFIAccessPointPasspointVenueNamesEntry_Object = MibTableRow
clabWIFIAccessPointPasspointVenueNamesEntry = _ClabWIFIAccessPointPasspointVenueNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 3, 1)
)
clabWIFIAccessPointPasspointVenueNamesEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointVenueNamesEntry.setStatus("deprecated")
_ClabWIFIAccessPointPasspointVenueNameIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointVenueNameIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointVenueNameIndex = _ClabWIFIAccessPointPasspointVenueNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 3, 1, 1),
    _ClabWIFIAccessPointPasspointVenueNameIndex_Type()
)
clabWIFIAccessPointPasspointVenueNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointVenueNameIndex.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointVenueNameCountryCode_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointVenueNameCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_ClabWIFIAccessPointPasspointVenueNameCountryCode_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointVenueNameCountryCode_Object = MibTableColumn
clabWIFIAccessPointPasspointVenueNameCountryCode = _ClabWIFIAccessPointPasspointVenueNameCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 3, 1, 2),
    _ClabWIFIAccessPointPasspointVenueNameCountryCode_Type()
)
clabWIFIAccessPointPasspointVenueNameCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointVenueNameCountryCode.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointVenueName_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointVenueName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClabWIFIAccessPointPasspointVenueName_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointVenueName_Object = MibTableColumn
clabWIFIAccessPointPasspointVenueName = _ClabWIFIAccessPointPasspointVenueName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 3, 1, 3),
    _ClabWIFIAccessPointPasspointVenueName_Type()
)
clabWIFIAccessPointPasspointVenueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointVenueName.setStatus("deprecated")
_ClabWIFIAccessPointPasspointOperatorNamesTable_Object = MibTable
clabWIFIAccessPointPasspointOperatorNamesTable = _ClabWIFIAccessPointPasspointOperatorNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 4)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOperatorNamesTable.setStatus("current")
_ClabWIFIAccessPointPasspointOperatorNamesEntry_Object = MibTableRow
clabWIFIAccessPointPasspointOperatorNamesEntry = _ClabWIFIAccessPointPasspointOperatorNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 4, 1)
)
clabWIFIAccessPointPasspointOperatorNamesEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOperatorNameIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOperatorNamesEntry.setStatus("current")
_ClabWIFIAccessPointPasspointOperatorNameIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointOperatorNameIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointOperatorNameIndex = _ClabWIFIAccessPointPasspointOperatorNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 4, 1, 1),
    _ClabWIFIAccessPointPasspointOperatorNameIndex_Type()
)
clabWIFIAccessPointPasspointOperatorNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOperatorNameIndex.setStatus("current")


class _ClabWIFIAccessPointPasspointOperatorNameCountryCode_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointOperatorNameCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_ClabWIFIAccessPointPasspointOperatorNameCountryCode_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointOperatorNameCountryCode_Object = MibTableColumn
clabWIFIAccessPointPasspointOperatorNameCountryCode = _ClabWIFIAccessPointPasspointOperatorNameCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 4, 1, 2),
    _ClabWIFIAccessPointPasspointOperatorNameCountryCode_Type()
)
clabWIFIAccessPointPasspointOperatorNameCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOperatorNameCountryCode.setStatus("current")


class _ClabWIFIAccessPointPasspointOperatorName_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointOperatorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClabWIFIAccessPointPasspointOperatorName_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointOperatorName_Object = MibTableColumn
clabWIFIAccessPointPasspointOperatorName = _ClabWIFIAccessPointPasspointOperatorName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 4, 1, 3),
    _ClabWIFIAccessPointPasspointOperatorName_Type()
)
clabWIFIAccessPointPasspointOperatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOperatorName.setStatus("current")
_ClabWIFIAccessPointPasspointConsortiumTable_Object = MibTable
clabWIFIAccessPointPasspointConsortiumTable = _ClabWIFIAccessPointPasspointConsortiumTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 5)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointConsortiumTable.setStatus("current")
_ClabWIFIAccessPointPasspointConsortiumEntry_Object = MibTableRow
clabWIFIAccessPointPasspointConsortiumEntry = _ClabWIFIAccessPointPasspointConsortiumEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 5, 1)
)
clabWIFIAccessPointPasspointConsortiumEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointConsortiumIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointConsortiumEntry.setStatus("current")
_ClabWIFIAccessPointPasspointConsortiumIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointConsortiumIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointConsortiumIndex = _ClabWIFIAccessPointPasspointConsortiumIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 5, 1, 1),
    _ClabWIFIAccessPointPasspointConsortiumIndex_Type()
)
clabWIFIAccessPointPasspointConsortiumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointConsortiumIndex.setStatus("current")


class _ClabWIFIAccessPointPasspointConsortiumOI_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointConsortiumOI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_ClabWIFIAccessPointPasspointConsortiumOI_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointConsortiumOI_Object = MibTableColumn
clabWIFIAccessPointPasspointConsortiumOI = _ClabWIFIAccessPointPasspointConsortiumOI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 5, 1, 2),
    _ClabWIFIAccessPointPasspointConsortiumOI_Type()
)
clabWIFIAccessPointPasspointConsortiumOI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointConsortiumOI.setStatus("current")
_ClabWIFIAccessPointPasspointDomainNamesTable_Object = MibTable
clabWIFIAccessPointPasspointDomainNamesTable = _ClabWIFIAccessPointPasspointDomainNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 6)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointDomainNamesTable.setStatus("deprecated")
_ClabWIFIAccessPointPasspointDomainNamesEntry_Object = MibTableRow
clabWIFIAccessPointPasspointDomainNamesEntry = _ClabWIFIAccessPointPasspointDomainNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 6, 1)
)
clabWIFIAccessPointPasspointDomainNamesEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointDomainNamesIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointDomainNamesEntry.setStatus("current")
_ClabWIFIAccessPointPasspointDomainNamesIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointDomainNamesIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointDomainNamesIndex = _ClabWIFIAccessPointPasspointDomainNamesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 6, 1, 1),
    _ClabWIFIAccessPointPasspointDomainNamesIndex_Type()
)
clabWIFIAccessPointPasspointDomainNamesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointDomainNamesIndex.setStatus("current")


class _ClabWIFIAccessPointPasspointDomainNamesDomainName_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointDomainNamesDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_ClabWIFIAccessPointPasspointDomainNamesDomainName_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointDomainNamesDomainName_Object = MibTableColumn
clabWIFIAccessPointPasspointDomainNamesDomainName = _ClabWIFIAccessPointPasspointDomainNamesDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 6, 1, 2),
    _ClabWIFIAccessPointPasspointDomainNamesDomainName_Type()
)
clabWIFIAccessPointPasspointDomainNamesDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointDomainNamesDomainName.setStatus("current")
_ClabWIFIAccessPointPasspointThreeGPPNetworkTable_Object = MibTable
clabWIFIAccessPointPasspointThreeGPPNetworkTable = _ClabWIFIAccessPointPasspointThreeGPPNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 7)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointThreeGPPNetworkTable.setStatus("current")
_ClabWIFIAccessPointPasspointThreeGPPNetworkEntry_Object = MibTableRow
clabWIFIAccessPointPasspointThreeGPPNetworkEntry = _ClabWIFIAccessPointPasspointThreeGPPNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 7, 1)
)
clabWIFIAccessPointPasspointThreeGPPNetworkEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointThreeGPPNetworkIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointThreeGPPNetworkEntry.setStatus("current")
_ClabWIFIAccessPointPasspointThreeGPPNetworkIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointThreeGPPNetworkIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointThreeGPPNetworkIndex = _ClabWIFIAccessPointPasspointThreeGPPNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 7, 1, 1),
    _ClabWIFIAccessPointPasspointThreeGPPNetworkIndex_Type()
)
clabWIFIAccessPointPasspointThreeGPPNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointThreeGPPNetworkIndex.setStatus("current")


class _ClabWIFIAccessPointPasspointThreeGPPNetworkMNC_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointThreeGPPNetworkMNC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(3, 3),
    )


_ClabWIFIAccessPointPasspointThreeGPPNetworkMNC_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointThreeGPPNetworkMNC_Object = MibTableColumn
clabWIFIAccessPointPasspointThreeGPPNetworkMNC = _ClabWIFIAccessPointPasspointThreeGPPNetworkMNC_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 7, 1, 5),
    _ClabWIFIAccessPointPasspointThreeGPPNetworkMNC_Type()
)
clabWIFIAccessPointPasspointThreeGPPNetworkMNC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointThreeGPPNetworkMNC.setStatus("current")


class _ClabWIFIAccessPointPasspointThreeGPPNetworkMCC_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointThreeGPPNetworkMCC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_ClabWIFIAccessPointPasspointThreeGPPNetworkMCC_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointThreeGPPNetworkMCC_Object = MibTableColumn
clabWIFIAccessPointPasspointThreeGPPNetworkMCC = _ClabWIFIAccessPointPasspointThreeGPPNetworkMCC_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 7, 1, 6),
    _ClabWIFIAccessPointPasspointThreeGPPNetworkMCC_Type()
)
clabWIFIAccessPointPasspointThreeGPPNetworkMCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointThreeGPPNetworkMCC.setStatus("current")
_ClabWIFIAccessPointPasspointNAIRealmsTable_Object = MibTable
clabWIFIAccessPointPasspointNAIRealmsTable = _ClabWIFIAccessPointPasspointNAIRealmsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 8)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointNAIRealmsTable.setStatus("deprecated")
_ClabWIFIAccessPointPasspointNAIRealmsEntry_Object = MibTableRow
clabWIFIAccessPointPasspointNAIRealmsEntry = _ClabWIFIAccessPointPasspointNAIRealmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 8, 1)
)
clabWIFIAccessPointPasspointNAIRealmsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointNAIRealmsIndex"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointNAIRealmsEapMethodsIndex"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointNAIRealmsEapMethodsAuthParmIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointNAIRealmsEntry.setStatus("deprecated")
_ClabWIFIAccessPointPasspointNAIRealmsIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointNAIRealmsIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointNAIRealmsIndex = _ClabWIFIAccessPointPasspointNAIRealmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 8, 1, 1),
    _ClabWIFIAccessPointPasspointNAIRealmsIndex_Type()
)
clabWIFIAccessPointPasspointNAIRealmsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointNAIRealmsIndex.setStatus("deprecated")
_ClabWIFIAccessPointPasspointNAIRealmsEapMethodsIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointNAIRealmsEapMethodsIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointNAIRealmsEapMethodsIndex = _ClabWIFIAccessPointPasspointNAIRealmsEapMethodsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 8, 1, 2),
    _ClabWIFIAccessPointPasspointNAIRealmsEapMethodsIndex_Type()
)
clabWIFIAccessPointPasspointNAIRealmsEapMethodsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointNAIRealmsEapMethodsIndex.setStatus("deprecated")
_ClabWIFIAccessPointPasspointNAIRealmsEapMethodsAuthParmIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointNAIRealmsEapMethodsAuthParmIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointNAIRealmsEapMethodsAuthParmIndex = _ClabWIFIAccessPointPasspointNAIRealmsEapMethodsAuthParmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 8, 1, 3),
    _ClabWIFIAccessPointPasspointNAIRealmsEapMethodsAuthParmIndex_Type()
)
clabWIFIAccessPointPasspointNAIRealmsEapMethodsAuthParmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointNAIRealmsEapMethodsAuthParmIndex.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointNAIRealmsEncodingType_Type(Integer32):
    """Custom type clabWIFIAccessPointPasspointNAIRealmsEncodingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfc", 1),
          ("utf", 2))
    )


_ClabWIFIAccessPointPasspointNAIRealmsEncodingType_Type.__name__ = "Integer32"
_ClabWIFIAccessPointPasspointNAIRealmsEncodingType_Object = MibTableColumn
clabWIFIAccessPointPasspointNAIRealmsEncodingType = _ClabWIFIAccessPointPasspointNAIRealmsEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 8, 1, 4),
    _ClabWIFIAccessPointPasspointNAIRealmsEncodingType_Type()
)
clabWIFIAccessPointPasspointNAIRealmsEncodingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointNAIRealmsEncodingType.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointNAIRealms_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointNAIRealms based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_ClabWIFIAccessPointPasspointNAIRealms_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointNAIRealms_Object = MibTableColumn
clabWIFIAccessPointPasspointNAIRealms = _ClabWIFIAccessPointPasspointNAIRealms_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 8, 1, 5),
    _ClabWIFIAccessPointPasspointNAIRealms_Type()
)
clabWIFIAccessPointPasspointNAIRealms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointNAIRealms.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointNAIRealmsEapMethod_Type(Integer32):
    """Custom type clabWIFIAccessPointPasspointNAIRealmsEapMethod based on Integer32"""
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
        *(("eapmschapv2", 5),
          ("eaptls", 2),
          ("eapttls", 3),
          ("none", 1),
          ("peap", 4))
    )


_ClabWIFIAccessPointPasspointNAIRealmsEapMethod_Type.__name__ = "Integer32"
_ClabWIFIAccessPointPasspointNAIRealmsEapMethod_Object = MibTableColumn
clabWIFIAccessPointPasspointNAIRealmsEapMethod = _ClabWIFIAccessPointPasspointNAIRealmsEapMethod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 8, 1, 11),
    _ClabWIFIAccessPointPasspointNAIRealmsEapMethod_Type()
)
clabWIFIAccessPointPasspointNAIRealmsEapMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointNAIRealmsEapMethod.setStatus("deprecated")
_ClabWIFIAccessPointPasspointNAIRealmsEapAuthParametersID_Type = OctetString
_ClabWIFIAccessPointPasspointNAIRealmsEapAuthParametersID_Object = MibTableColumn
clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersID = _ClabWIFIAccessPointPasspointNAIRealmsEapAuthParametersID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 8, 1, 12),
    _ClabWIFIAccessPointPasspointNAIRealmsEapAuthParametersID_Type()
)
clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersID.setStatus("deprecated")
_ClabWIFIAccessPointPasspointNAIRealmsEapAuthParametersValue_Type = OctetString
_ClabWIFIAccessPointPasspointNAIRealmsEapAuthParametersValue_Object = MibTableColumn
clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersValue = _ClabWIFIAccessPointPasspointNAIRealmsEapAuthParametersValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 8, 1, 13),
    _ClabWIFIAccessPointPasspointNAIRealmsEapAuthParametersValue_Type()
)
clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersValue.setStatus("deprecated")
_ClabWIFIAccessPointPasspointOSUTable_Object = MibTable
clabWIFIAccessPointPasspointOSUTable = _ClabWIFIAccessPointPasspointOSUTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUTable.setStatus("deprecated")
_ClabWIFIAccessPointPasspointOSUEntry_Object = MibTableRow
clabWIFIAccessPointPasspointOSUEntry = _ClabWIFIAccessPointPasspointOSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1)
)
clabWIFIAccessPointPasspointOSUEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderIndex"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderNamesIndex"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderIconsIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUEntry.setStatus("deprecated")
_ClabWIFIAccessPointPasspointOSUProviderIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointOSUProviderIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderIndex = _ClabWIFIAccessPointPasspointOSUProviderIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 1),
    _ClabWIFIAccessPointPasspointOSUProviderIndex_Type()
)
clabWIFIAccessPointPasspointOSUProviderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderIndex.setStatus("deprecated")
_ClabWIFIAccessPointPasspointOSUProviderNamesIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointOSUProviderNamesIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderNamesIndex = _ClabWIFIAccessPointPasspointOSUProviderNamesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 2),
    _ClabWIFIAccessPointPasspointOSUProviderNamesIndex_Type()
)
clabWIFIAccessPointPasspointOSUProviderNamesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderNamesIndex.setStatus("deprecated")
_ClabWIFIAccessPointPasspointOSUProviderIconsIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointOSUProviderIconsIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderIconsIndex = _ClabWIFIAccessPointPasspointOSUProviderIconsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 3),
    _ClabWIFIAccessPointPasspointOSUProviderIconsIndex_Type()
)
clabWIFIAccessPointPasspointOSUProviderIconsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderIconsIndex.setStatus("deprecated")
_ClabWIFIAccessPointPasspointOSUProviderServiceDescIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspointOSUProviderServiceDescIndex_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderServiceDescIndex = _ClabWIFIAccessPointPasspointOSUProviderServiceDescIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 4),
    _ClabWIFIAccessPointPasspointOSUProviderServiceDescIndex_Type()
)
clabWIFIAccessPointPasspointOSUProviderServiceDescIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderServiceDescIndex.setStatus("deprecated")
_ClabWIFIAccessPointPasspointOSUProviderServerURI_Type = SnmpAdminString
_ClabWIFIAccessPointPasspointOSUProviderServerURI_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderServerURI = _ClabWIFIAccessPointPasspointOSUProviderServerURI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 5),
    _ClabWIFIAccessPointPasspointOSUProviderServerURI_Type()
)
clabWIFIAccessPointPasspointOSUProviderServerURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderServerURI.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderNAI_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointOSUProviderNAI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_ClabWIFIAccessPointPasspointOSUProviderNAI_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointOSUProviderNAI_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderNAI = _ClabWIFIAccessPointPasspointOSUProviderNAI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 6),
    _ClabWIFIAccessPointPasspointOSUProviderNAI_Type()
)
clabWIFIAccessPointPasspointOSUProviderNAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderNAI.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderNamesLanguageCode_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspointOSUProviderNamesLanguageCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_ClabWIFIAccessPointPasspointOSUProviderNamesLanguageCode_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspointOSUProviderNamesLanguageCode_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderNamesLanguageCode = _ClabWIFIAccessPointPasspointOSUProviderNamesLanguageCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 7),
    _ClabWIFIAccessPointPasspointOSUProviderNamesLanguageCode_Type()
)
clabWIFIAccessPointPasspointOSUProviderNamesLanguageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderNamesLanguageCode.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderNamesFriendlyName_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointOSUProviderNamesFriendlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 504),
    )


_ClabWIFIAccessPointPasspointOSUProviderNamesFriendlyName_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointOSUProviderNamesFriendlyName_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderNamesFriendlyName = _ClabWIFIAccessPointPasspointOSUProviderNamesFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 8),
    _ClabWIFIAccessPointPasspointOSUProviderNamesFriendlyName_Type()
)
clabWIFIAccessPointPasspointOSUProviderNamesFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderNamesFriendlyName.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderIconFileName_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointOSUProviderIconFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClabWIFIAccessPointPasspointOSUProviderIconFileName_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointOSUProviderIconFileName_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderIconFileName = _ClabWIFIAccessPointPasspointOSUProviderIconFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 9),
    _ClabWIFIAccessPointPasspointOSUProviderIconFileName_Type()
)
clabWIFIAccessPointPasspointOSUProviderIconFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderIconFileName.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderIconType_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointOSUProviderIconType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClabWIFIAccessPointPasspointOSUProviderIconType_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointOSUProviderIconType_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderIconType = _ClabWIFIAccessPointPasspointOSUProviderIconType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 10),
    _ClabWIFIAccessPointPasspointOSUProviderIconType_Type()
)
clabWIFIAccessPointPasspointOSUProviderIconType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderIconType.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderIconWidth_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspointOSUProviderIconWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClabWIFIAccessPointPasspointOSUProviderIconWidth_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspointOSUProviderIconWidth_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderIconWidth = _ClabWIFIAccessPointPasspointOSUProviderIconWidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 11),
    _ClabWIFIAccessPointPasspointOSUProviderIconWidth_Type()
)
clabWIFIAccessPointPasspointOSUProviderIconWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderIconWidth.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderIconHeight_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspointOSUProviderIconHeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClabWIFIAccessPointPasspointOSUProviderIconHeight_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspointOSUProviderIconHeight_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderIconHeight = _ClabWIFIAccessPointPasspointOSUProviderIconHeight_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 12),
    _ClabWIFIAccessPointPasspointOSUProviderIconHeight_Type()
)
clabWIFIAccessPointPasspointOSUProviderIconHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderIconHeight.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderIconLanguageCode_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspointOSUProviderIconLanguageCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_ClabWIFIAccessPointPasspointOSUProviderIconLanguageCode_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspointOSUProviderIconLanguageCode_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderIconLanguageCode = _ClabWIFIAccessPointPasspointOSUProviderIconLanguageCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 13),
    _ClabWIFIAccessPointPasspointOSUProviderIconLanguageCode_Type()
)
clabWIFIAccessPointPasspointOSUProviderIconLanguageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderIconLanguageCode.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_ClabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode = _ClabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 14),
    _ClabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode_Type()
)
clabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderServiceDescription_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointOSUProviderServiceDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(504, 504),
    )


_ClabWIFIAccessPointPasspointOSUProviderServiceDescription_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointOSUProviderServiceDescription_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderServiceDescription = _ClabWIFIAccessPointPasspointOSUProviderServiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 15),
    _ClabWIFIAccessPointPasspointOSUProviderServiceDescription_Type()
)
clabWIFIAccessPointPasspointOSUProviderServiceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderServiceDescription.setStatus("deprecated")


class _ClabWIFIAccessPointPasspointOSUProviderMethodsList_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspointOSUProviderMethodsList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClabWIFIAccessPointPasspointOSUProviderMethodsList_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspointOSUProviderMethodsList_Object = MibTableColumn
clabWIFIAccessPointPasspointOSUProviderMethodsList = _ClabWIFIAccessPointPasspointOSUProviderMethodsList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 9, 1, 16),
    _ClabWIFIAccessPointPasspointOSUProviderMethodsList_Type()
)
clabWIFIAccessPointPasspointOSUProviderMethodsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointOSUProviderMethodsList.setStatus("deprecated")
_ClabWIFIAccessPointPasspoint2VenueNamesTable_Object = MibTable
clabWIFIAccessPointPasspoint2VenueNamesTable = _ClabWIFIAccessPointPasspoint2VenueNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 10)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2VenueNamesTable.setStatus("current")
_ClabWIFIAccessPointPasspoint2VenueNamesEntry_Object = MibTableRow
clabWIFIAccessPointPasspoint2VenueNamesEntry = _ClabWIFIAccessPointPasspoint2VenueNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 10, 1)
)
clabWIFIAccessPointPasspoint2VenueNamesEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2VenueNameIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2VenueNamesEntry.setStatus("current")
_ClabWIFIAccessPointPasspoint2VenueNameIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspoint2VenueNameIndex_Object = MibTableColumn
clabWIFIAccessPointPasspoint2VenueNameIndex = _ClabWIFIAccessPointPasspoint2VenueNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 10, 1, 1),
    _ClabWIFIAccessPointPasspoint2VenueNameIndex_Type()
)
clabWIFIAccessPointPasspoint2VenueNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2VenueNameIndex.setStatus("current")


class _ClabWIFIAccessPointPasspoint2VenueNameCountryCode_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointPasspoint2VenueNameCountryCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
        ValueSizeConstraint(5, 5),
    )


_ClabWIFIAccessPointPasspoint2VenueNameCountryCode_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointPasspoint2VenueNameCountryCode_Object = MibTableColumn
clabWIFIAccessPointPasspoint2VenueNameCountryCode = _ClabWIFIAccessPointPasspoint2VenueNameCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 10, 1, 2),
    _ClabWIFIAccessPointPasspoint2VenueNameCountryCode_Type()
)
clabWIFIAccessPointPasspoint2VenueNameCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2VenueNameCountryCode.setStatus("current")


class _ClabWIFIAccessPointPasspoint2VenueName_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointPasspoint2VenueName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClabWIFIAccessPointPasspoint2VenueName_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointPasspoint2VenueName_Object = MibTableColumn
clabWIFIAccessPointPasspoint2VenueName = _ClabWIFIAccessPointPasspoint2VenueName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 10, 1, 3),
    _ClabWIFIAccessPointPasspoint2VenueName_Type()
)
clabWIFIAccessPointPasspoint2VenueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2VenueName.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsTable_Object = MibTable
clabWIFIAccessPointPasspoint2NAIRealmsTable = _ClabWIFIAccessPointPasspoint2NAIRealmsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 11)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsTable.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsEntry_Object = MibTableRow
clabWIFIAccessPointPasspoint2NAIRealmsEntry = _ClabWIFIAccessPointPasspoint2NAIRealmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 11, 1)
)
clabWIFIAccessPointPasspoint2NAIRealmsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealmsIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEntry.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspoint2NAIRealmsIndex_Object = MibTableColumn
clabWIFIAccessPointPasspoint2NAIRealmsIndex = _ClabWIFIAccessPointPasspoint2NAIRealmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 11, 1, 1),
    _ClabWIFIAccessPointPasspoint2NAIRealmsIndex_Type()
)
clabWIFIAccessPointPasspoint2NAIRealmsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsIndex.setStatus("current")


class _ClabWIFIAccessPointPasspoint2NAIRealmsEncodingType_Type(Integer32):
    """Custom type clabWIFIAccessPointPasspoint2NAIRealmsEncodingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfc", 1),
          ("utf", 2))
    )


_ClabWIFIAccessPointPasspoint2NAIRealmsEncodingType_Type.__name__ = "Integer32"
_ClabWIFIAccessPointPasspoint2NAIRealmsEncodingType_Object = MibTableColumn
clabWIFIAccessPointPasspoint2NAIRealmsEncodingType = _ClabWIFIAccessPointPasspoint2NAIRealmsEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 11, 1, 2),
    _ClabWIFIAccessPointPasspoint2NAIRealmsEncodingType_Type()
)
clabWIFIAccessPointPasspoint2NAIRealmsEncodingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEncodingType.setStatus("current")


class _ClabWIFIAccessPointPasspoint2NAIRealms_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointPasspoint2NAIRealms based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_ClabWIFIAccessPointPasspoint2NAIRealms_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointPasspoint2NAIRealms_Object = MibTableColumn
clabWIFIAccessPointPasspoint2NAIRealms = _ClabWIFIAccessPointPasspoint2NAIRealms_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 11, 1, 3),
    _ClabWIFIAccessPointPasspoint2NAIRealms_Type()
)
clabWIFIAccessPointPasspoint2NAIRealms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealms.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsTable_Object = MibTable
clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsTable = _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 12)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsTable.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsEntry_Object = MibTableRow
clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsEntry = _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 12, 1)
)
clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealmsIndex"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsEntry.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex_Object = MibTableColumn
clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex = _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 12, 1, 1),
    _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex_Type()
)
clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex.setStatus("current")


class _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethod_Type(Integer32):
    """Custom type clabWIFIAccessPointPasspoint2NAIRealmsEapMethod based on Integer32"""
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
        *(("eapmschapv2", 5),
          ("eaptls", 2),
          ("eapttls", 3),
          ("none", 1),
          ("peap", 4))
    )


_ClabWIFIAccessPointPasspoint2NAIRealmsEapMethod_Type.__name__ = "Integer32"
_ClabWIFIAccessPointPasspoint2NAIRealmsEapMethod_Object = MibTableColumn
clabWIFIAccessPointPasspoint2NAIRealmsEapMethod = _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 12, 1, 2),
    _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethod_Type()
)
clabWIFIAccessPointPasspoint2NAIRealmsEapMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEapMethod.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthTable_Object = MibTable
clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthTable = _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 13)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthTable.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthEntry_Object = MibTableRow
clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthEntry = _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 13, 1)
)
clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealmsIndex"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthParmIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthEntry.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthParmIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthParmIndex_Object = MibTableColumn
clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthParmIndex = _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthParmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 13, 1, 1),
    _ClabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthParmIndex_Type()
)
clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthParmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthParmIndex.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersID_Type = OctetString
_ClabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersID_Object = MibTableColumn
clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersID = _ClabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 13, 1, 2),
    _ClabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersID_Type()
)
clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersID.setStatus("current")
_ClabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersValue_Type = OctetString
_ClabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersValue_Object = MibTableColumn
clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersValue = _ClabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 13, 1, 3),
    _ClabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersValue_Type()
)
clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersValue.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUTable_Object = MibTable
clabWIFIAccessPointPasspoint2OSUTable = _ClabWIFIAccessPointPasspoint2OSUTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 14)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUTable.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUEntry_Object = MibTableRow
clabWIFIAccessPointPasspoint2OSUEntry = _ClabWIFIAccessPointPasspoint2OSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 14, 1)
)
clabWIFIAccessPointPasspoint2OSUEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUEntry.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUProviderIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspoint2OSUProviderIndex_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderIndex = _ClabWIFIAccessPointPasspoint2OSUProviderIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 14, 1, 1),
    _ClabWIFIAccessPointPasspoint2OSUProviderIndex_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderIndex.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderServerURI_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderServerURI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderServerURI_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointPasspoint2OSUProviderServerURI_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderServerURI = _ClabWIFIAccessPointPasspoint2OSUProviderServerURI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 14, 1, 2),
    _ClabWIFIAccessPointPasspoint2OSUProviderServerURI_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderServerURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderServerURI.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderNAI_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderNAI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderNAI_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointPasspoint2OSUProviderNAI_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderNAI = _ClabWIFIAccessPointPasspoint2OSUProviderNAI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 14, 1, 3),
    _ClabWIFIAccessPointPasspoint2OSUProviderNAI_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderNAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderNAI.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderMethodsList_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderMethodsList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderMethodsList_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspoint2OSUProviderMethodsList_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderMethodsList = _ClabWIFIAccessPointPasspoint2OSUProviderMethodsList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 14, 1, 4),
    _ClabWIFIAccessPointPasspoint2OSUProviderMethodsList_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderMethodsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderMethodsList.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUProviderNamesTable_Object = MibTable
clabWIFIAccessPointPasspoint2OSUProviderNamesTable = _ClabWIFIAccessPointPasspoint2OSUProviderNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 15)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderNamesTable.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUProviderNamesEntry_Object = MibTableRow
clabWIFIAccessPointPasspoint2OSUProviderNamesEntry = _ClabWIFIAccessPointPasspoint2OSUProviderNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 15, 1)
)
clabWIFIAccessPointPasspoint2OSUProviderNamesEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderIndex"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderNamesIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderNamesEntry.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUProviderNamesIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspoint2OSUProviderNamesIndex_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderNamesIndex = _ClabWIFIAccessPointPasspoint2OSUProviderNamesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 15, 1, 1),
    _ClabWIFIAccessPointPasspoint2OSUProviderNamesIndex_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderNamesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderNamesIndex.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode = _ClabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 15, 1, 2),
    _ClabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 504),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName = _ClabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 15, 1, 3),
    _ClabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUProviderIconsTable_Object = MibTable
clabWIFIAccessPointPasspoint2OSUProviderIconsTable = _ClabWIFIAccessPointPasspoint2OSUProviderIconsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 16)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderIconsTable.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUProviderIconsEntry_Object = MibTableRow
clabWIFIAccessPointPasspoint2OSUProviderIconsEntry = _ClabWIFIAccessPointPasspoint2OSUProviderIconsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 16, 1)
)
clabWIFIAccessPointPasspoint2OSUProviderIconsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderIndex"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderIconsIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderIconsEntry.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUProviderIconsIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspoint2OSUProviderIconsIndex_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderIconsIndex = _ClabWIFIAccessPointPasspoint2OSUProviderIconsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 16, 1, 1),
    _ClabWIFIAccessPointPasspoint2OSUProviderIconsIndex_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderIconsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderIconsIndex.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderIconFileName_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderIconFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderIconFileName_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointPasspoint2OSUProviderIconFileName_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderIconFileName = _ClabWIFIAccessPointPasspoint2OSUProviderIconFileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 16, 1, 2),
    _ClabWIFIAccessPointPasspoint2OSUProviderIconFileName_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderIconFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderIconFileName.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderIconType_Type(OctetString):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderIconType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderIconType_Type.__name__ = "OctetString"
_ClabWIFIAccessPointPasspoint2OSUProviderIconType_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderIconType = _ClabWIFIAccessPointPasspoint2OSUProviderIconType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 16, 1, 3),
    _ClabWIFIAccessPointPasspoint2OSUProviderIconType_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderIconType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderIconType.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderIconWidth_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderIconWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderIconWidth_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspoint2OSUProviderIconWidth_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderIconWidth = _ClabWIFIAccessPointPasspoint2OSUProviderIconWidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 16, 1, 4),
    _ClabWIFIAccessPointPasspoint2OSUProviderIconWidth_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderIconWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderIconWidth.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderIconHeight_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderIconHeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderIconHeight_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspoint2OSUProviderIconHeight_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderIconHeight = _ClabWIFIAccessPointPasspoint2OSUProviderIconHeight_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 16, 1, 5),
    _ClabWIFIAccessPointPasspoint2OSUProviderIconHeight_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderIconHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderIconHeight.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode = _ClabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 16, 1, 6),
    _ClabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUProviderServiceDescTable_Object = MibTable
clabWIFIAccessPointPasspoint2OSUProviderServiceDescTable = _ClabWIFIAccessPointPasspoint2OSUProviderServiceDescTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 17)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderServiceDescTable.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUProviderServiceDescEntry_Object = MibTableRow
clabWIFIAccessPointPasspoint2OSUProviderServiceDescEntry = _ClabWIFIAccessPointPasspoint2OSUProviderServiceDescEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 17, 1)
)
clabWIFIAccessPointPasspoint2OSUProviderServiceDescEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderIndex"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderServiceDescIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderServiceDescEntry.setStatus("current")
_ClabWIFIAccessPointPasspoint2OSUProviderServiceDescIndex_Type = Unsigned32
_ClabWIFIAccessPointPasspoint2OSUProviderServiceDescIndex_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderServiceDescIndex = _ClabWIFIAccessPointPasspoint2OSUProviderServiceDescIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 17, 1, 1),
    _ClabWIFIAccessPointPasspoint2OSUProviderServiceDescIndex_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderServiceDescIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderServiceDescIndex.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode = _ClabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 17, 1, 2),
    _ClabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode.setStatus("current")


class _ClabWIFIAccessPointPasspoint2OSUProviderServiceDescription_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointPasspoint2OSUProviderServiceDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(504, 504),
    )


_ClabWIFIAccessPointPasspoint2OSUProviderServiceDescription_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointPasspoint2OSUProviderServiceDescription_Object = MibTableColumn
clabWIFIAccessPointPasspoint2OSUProviderServiceDescription = _ClabWIFIAccessPointPasspoint2OSUProviderServiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 19, 17, 1, 3),
    _ClabWIFIAccessPointPasspoint2OSUProviderServiceDescription_Type()
)
clabWIFIAccessPointPasspoint2OSUProviderServiceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspoint2OSUProviderServiceDescription.setStatus("current")
_ClabWIFIAccessPointPasspointWANMetrics_ObjectIdentity = ObjectIdentity
clabWIFIAccessPointPasspointWANMetrics = _ClabWIFIAccessPointPasspointWANMetrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 20)
)


class _ClabWIFIAccessPointPasspointWANMetricsLinkStatus_Type(Integer32):
    """Custom type clabWIFIAccessPointPasspointWANMetricsLinkStatus based on Integer32"""
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
        *(("linkDown", 3),
          ("linkTest", 4),
          ("linkUp", 2),
          ("reserved", 1))
    )


_ClabWIFIAccessPointPasspointWANMetricsLinkStatus_Type.__name__ = "Integer32"
_ClabWIFIAccessPointPasspointWANMetricsLinkStatus_Object = MibScalar
clabWIFIAccessPointPasspointWANMetricsLinkStatus = _ClabWIFIAccessPointPasspointWANMetricsLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 20, 1),
    _ClabWIFIAccessPointPasspointWANMetricsLinkStatus_Type()
)
clabWIFIAccessPointPasspointWANMetricsLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointWANMetricsLinkStatus.setStatus("current")
_ClabWIFIAccessPointPasspointWANMetricsAtCapacity_Type = TruthValue
_ClabWIFIAccessPointPasspointWANMetricsAtCapacity_Object = MibScalar
clabWIFIAccessPointPasspointWANMetricsAtCapacity = _ClabWIFIAccessPointPasspointWANMetricsAtCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 20, 2),
    _ClabWIFIAccessPointPasspointWANMetricsAtCapacity_Type()
)
clabWIFIAccessPointPasspointWANMetricsAtCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointWANMetricsAtCapacity.setStatus("current")
_ClabWIFIAccessPointPasspointWANMetricsDownlinkSpeed_Type = Unsigned32
_ClabWIFIAccessPointPasspointWANMetricsDownlinkSpeed_Object = MibScalar
clabWIFIAccessPointPasspointWANMetricsDownlinkSpeed = _ClabWIFIAccessPointPasspointWANMetricsDownlinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 20, 3),
    _ClabWIFIAccessPointPasspointWANMetricsDownlinkSpeed_Type()
)
clabWIFIAccessPointPasspointWANMetricsDownlinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointWANMetricsDownlinkSpeed.setStatus("current")
_ClabWIFIAccessPointPasspointWANMetricsUplinkSpeed_Type = Unsigned32
_ClabWIFIAccessPointPasspointWANMetricsUplinkSpeed_Object = MibScalar
clabWIFIAccessPointPasspointWANMetricsUplinkSpeed = _ClabWIFIAccessPointPasspointWANMetricsUplinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 20, 4),
    _ClabWIFIAccessPointPasspointWANMetricsUplinkSpeed_Type()
)
clabWIFIAccessPointPasspointWANMetricsUplinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointWANMetricsUplinkSpeed.setStatus("current")


class _ClabWIFIAccessPointPasspointWANMetricsDownlinkLoad_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspointWANMetricsDownlinkLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClabWIFIAccessPointPasspointWANMetricsDownlinkLoad_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspointWANMetricsDownlinkLoad_Object = MibScalar
clabWIFIAccessPointPasspointWANMetricsDownlinkLoad = _ClabWIFIAccessPointPasspointWANMetricsDownlinkLoad_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 20, 5),
    _ClabWIFIAccessPointPasspointWANMetricsDownlinkLoad_Type()
)
clabWIFIAccessPointPasspointWANMetricsDownlinkLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointWANMetricsDownlinkLoad.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointWANMetricsDownlinkLoad.setUnits("percentage")


class _ClabWIFIAccessPointPasspointWANMetricsUplinkLoad_Type(Unsigned32):
    """Custom type clabWIFIAccessPointPasspointWANMetricsUplinkLoad based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClabWIFIAccessPointPasspointWANMetricsUplinkLoad_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointPasspointWANMetricsUplinkLoad_Object = MibScalar
clabWIFIAccessPointPasspointWANMetricsUplinkLoad = _ClabWIFIAccessPointPasspointWANMetricsUplinkLoad_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 20, 6),
    _ClabWIFIAccessPointPasspointWANMetricsUplinkLoad_Type()
)
clabWIFIAccessPointPasspointWANMetricsUplinkLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointWANMetricsUplinkLoad.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAccessPointPasspointWANMetricsUplinkLoad.setUnits("percentage")
_ClabWIFINeighboringWiFiDiagnostics_ObjectIdentity = ObjectIdentity
clabWIFINeighboringWiFiDiagnostics = _ClabWIFINeighboringWiFiDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21)
)


class _ClabWIFINeighboringWiFiDiagnosticsMode_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiDiagnosticsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interval", 2),
          ("manual", 1),
          ("stop", 3))
    )


_ClabWIFINeighboringWiFiDiagnosticsMode_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiDiagnosticsMode_Object = MibScalar
clabWIFINeighboringWiFiDiagnosticsMode = _ClabWIFINeighboringWiFiDiagnosticsMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 1),
    _ClabWIFINeighboringWiFiDiagnosticsMode_Type()
)
clabWIFINeighboringWiFiDiagnosticsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsMode.setStatus("current")


class _ClabWIFINeighboringWiFiDiagnosticsInterval_Type(Unsigned32):
    """Custom type clabWIFINeighboringWiFiDiagnosticsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ClabWIFINeighboringWiFiDiagnosticsInterval_Type.__name__ = "Unsigned32"
_ClabWIFINeighboringWiFiDiagnosticsInterval_Object = MibScalar
clabWIFINeighboringWiFiDiagnosticsInterval = _ClabWIFINeighboringWiFiDiagnosticsInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 2),
    _ClabWIFINeighboringWiFiDiagnosticsInterval_Type()
)
clabWIFINeighboringWiFiDiagnosticsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsInterval.setStatus("current")


class _ClabWIFINeighboringWiFiDiagnosticsState_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiDiagnosticsState based on Integer32"""
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
        *(("completed", 3),
          ("error", 4),
          ("none", 1),
          ("requested", 2))
    )


_ClabWIFINeighboringWiFiDiagnosticsState_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiDiagnosticsState_Object = MibScalar
clabWIFINeighboringWiFiDiagnosticsState = _ClabWIFINeighboringWiFiDiagnosticsState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 3),
    _ClabWIFINeighboringWiFiDiagnosticsState_Type()
)
clabWIFINeighboringWiFiDiagnosticsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsState.setStatus("current")
_ClabWIFINeighboringWiFiDiagnosticsTableClear_Type = TruthValue
_ClabWIFINeighboringWiFiDiagnosticsTableClear_Object = MibScalar
clabWIFINeighboringWiFiDiagnosticsTableClear = _ClabWIFINeighboringWiFiDiagnosticsTableClear_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 4),
    _ClabWIFINeighboringWiFiDiagnosticsTableClear_Type()
)
clabWIFINeighboringWiFiDiagnosticsTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsTableClear.setStatus("current")
_ClabWIFINeighboringWiFiDiagnosticsTableMaxNumberOfEntries_Type = Unsigned32
_ClabWIFINeighboringWiFiDiagnosticsTableMaxNumberOfEntries_Object = MibScalar
clabWIFINeighboringWiFiDiagnosticsTableMaxNumberOfEntries = _ClabWIFINeighboringWiFiDiagnosticsTableMaxNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 5),
    _ClabWIFINeighboringWiFiDiagnosticsTableMaxNumberOfEntries_Type()
)
clabWIFINeighboringWiFiDiagnosticsTableMaxNumberOfEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsTableMaxNumberOfEntries.setStatus("current")
_ClabWIFINeighboringWiFiDiagnosticsResultTable_Object = MibTable
clabWIFINeighboringWiFiDiagnosticsResultTable = _ClabWIFINeighboringWiFiDiagnosticsResultTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6)
)
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsResultTable.setStatus("current")
_ClabWIFINeighboringWiFiDiagnosticsResultEntry_Object = MibTableRow
clabWIFINeighboringWiFiDiagnosticsResultEntry = _ClabWIFINeighboringWiFiDiagnosticsResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1)
)
clabWIFINeighboringWiFiDiagnosticsResultEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIRadioId"),
    (0, "CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDiagnosticsResultIndex"),
)
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsResultEntry.setStatus("current")
_ClabWIFINeighboringWiFiDiagnosticsResultIndex_Type = Unsigned32
_ClabWIFINeighboringWiFiDiagnosticsResultIndex_Object = MibTableColumn
clabWIFINeighboringWiFiDiagnosticsResultIndex = _ClabWIFINeighboringWiFiDiagnosticsResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 1),
    _ClabWIFINeighboringWiFiDiagnosticsResultIndex_Type()
)
clabWIFINeighboringWiFiDiagnosticsResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsResultIndex.setStatus("current")


class _ClabWIFINeighboringWiFiSSID_Type(OctetString):
    """Custom type clabWIFINeighboringWiFiSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClabWIFINeighboringWiFiSSID_Type.__name__ = "OctetString"
_ClabWIFINeighboringWiFiSSID_Object = MibTableColumn
clabWIFINeighboringWiFiSSID = _ClabWIFINeighboringWiFiSSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 2),
    _ClabWIFINeighboringWiFiSSID_Type()
)
clabWIFINeighboringWiFiSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiSSID.setStatus("current")
_ClabWIFINeighboringWiFiBSSID_Type = MacAddress
_ClabWIFINeighboringWiFiBSSID_Object = MibTableColumn
clabWIFINeighboringWiFiBSSID = _ClabWIFINeighboringWiFiBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 3),
    _ClabWIFINeighboringWiFiBSSID_Type()
)
clabWIFINeighboringWiFiBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiBSSID.setStatus("current")


class _ClabWIFINeighboringWiFiMode_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adhoc", 1),
          ("infrastructure", 2))
    )


_ClabWIFINeighboringWiFiMode_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiMode_Object = MibTableColumn
clabWIFINeighboringWiFiMode = _ClabWIFINeighboringWiFiMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 4),
    _ClabWIFINeighboringWiFiMode_Type()
)
clabWIFINeighboringWiFiMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiMode.setStatus("current")


class _ClabWIFINeighboringWiFiChannel_Type(Unsigned32):
    """Custom type clabWIFINeighboringWiFiChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClabWIFINeighboringWiFiChannel_Type.__name__ = "Unsigned32"
_ClabWIFINeighboringWiFiChannel_Object = MibTableColumn
clabWIFINeighboringWiFiChannel = _ClabWIFINeighboringWiFiChannel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 5),
    _ClabWIFINeighboringWiFiChannel_Type()
)
clabWIFINeighboringWiFiChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiChannel.setStatus("current")


class _ClabWIFINeighboringWiFiSignalStrength_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiSignalStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 0),
    )


_ClabWIFINeighboringWiFiSignalStrength_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiSignalStrength_Object = MibTableColumn
clabWIFINeighboringWiFiSignalStrength = _ClabWIFINeighboringWiFiSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 6),
    _ClabWIFINeighboringWiFiSignalStrength_Type()
)
clabWIFINeighboringWiFiSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiSignalStrength.setStatus("current")


class _ClabWIFINeighboringWiFiSecurityModeEnabled_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiSecurityModeEnabled based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("wep", 2),
          ("wpa", 3),
          ("wpa2", 4),
          ("wpa2enterprise", 7),
          ("wpaenterprise", 6),
          ("wpawpa2", 5),
          ("wpawpa2enterprise", 8))
    )


_ClabWIFINeighboringWiFiSecurityModeEnabled_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiSecurityModeEnabled_Object = MibTableColumn
clabWIFINeighboringWiFiSecurityModeEnabled = _ClabWIFINeighboringWiFiSecurityModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 7),
    _ClabWIFINeighboringWiFiSecurityModeEnabled_Type()
)
clabWIFINeighboringWiFiSecurityModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiSecurityModeEnabled.setStatus("current")


class _ClabWIFINeighboringWiFiEncryptionMode_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiEncryptionMode based on Integer32"""
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


_ClabWIFINeighboringWiFiEncryptionMode_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiEncryptionMode_Object = MibTableColumn
clabWIFINeighboringWiFiEncryptionMode = _ClabWIFINeighboringWiFiEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 8),
    _ClabWIFINeighboringWiFiEncryptionMode_Type()
)
clabWIFINeighboringWiFiEncryptionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiEncryptionMode.setStatus("current")


class _ClabWIFINeighboringWiFiOperatingFrequencyBand_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiOperatingFrequencyBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ghz24", 1),
          ("ghz5", 2))
    )


_ClabWIFINeighboringWiFiOperatingFrequencyBand_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiOperatingFrequencyBand_Object = MibTableColumn
clabWIFINeighboringWiFiOperatingFrequencyBand = _ClabWIFINeighboringWiFiOperatingFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 9),
    _ClabWIFINeighboringWiFiOperatingFrequencyBand_Type()
)
clabWIFINeighboringWiFiOperatingFrequencyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiOperatingFrequencyBand.setStatus("current")


class _ClabWIFINeighboringWiFiSupportedStandards_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiSupportedStandards based on Integer32"""
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
        *(("a", 1),
          ("ac", 5),
          ("b", 2),
          ("g", 3),
          ("n", 4))
    )


_ClabWIFINeighboringWiFiSupportedStandards_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiSupportedStandards_Object = MibTableColumn
clabWIFINeighboringWiFiSupportedStandards = _ClabWIFINeighboringWiFiSupportedStandards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 10),
    _ClabWIFINeighboringWiFiSupportedStandards_Type()
)
clabWIFINeighboringWiFiSupportedStandards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiSupportedStandards.setStatus("current")
_ClabWIFINeighboringWiFiOperatingStandards_Type = SnmpAdminString
_ClabWIFINeighboringWiFiOperatingStandards_Object = MibTableColumn
clabWIFINeighboringWiFiOperatingStandards = _ClabWIFINeighboringWiFiOperatingStandards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 11),
    _ClabWIFINeighboringWiFiOperatingStandards_Type()
)
clabWIFINeighboringWiFiOperatingStandards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiOperatingStandards.setStatus("current")


class _ClabWIFINeighboringWiFiOperatingChannelBandwidth_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiOperatingChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 8),
          ("mHz160", 4),
          ("mHz20", 1),
          ("mHz40", 2),
          ("mHz80", 3),
          ("mHz80plus80", 5))
    )


_ClabWIFINeighboringWiFiOperatingChannelBandwidth_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiOperatingChannelBandwidth_Object = MibTableColumn
clabWIFINeighboringWiFiOperatingChannelBandwidth = _ClabWIFINeighboringWiFiOperatingChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 12),
    _ClabWIFINeighboringWiFiOperatingChannelBandwidth_Type()
)
clabWIFINeighboringWiFiOperatingChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiOperatingChannelBandwidth.setStatus("current")
_ClabWIFINeighboringWiFiBeaconPeriod_Type = Unsigned32
_ClabWIFINeighboringWiFiBeaconPeriod_Object = MibTableColumn
clabWIFINeighboringWiFiBeaconPeriod = _ClabWIFINeighboringWiFiBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 13),
    _ClabWIFINeighboringWiFiBeaconPeriod_Type()
)
clabWIFINeighboringWiFiBeaconPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiBeaconPeriod.setStatus("current")


class _ClabWIFINeighboringWiFiNoise_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiNoise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 0),
    )


_ClabWIFINeighboringWiFiNoise_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiNoise_Object = MibTableColumn
clabWIFINeighboringWiFiNoise = _ClabWIFINeighboringWiFiNoise_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 14),
    _ClabWIFINeighboringWiFiNoise_Type()
)
clabWIFINeighboringWiFiNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiNoise.setStatus("current")


class _ClabWIFINeighboringWiFiBasicDataTransferRates_Type(OctetString):
    """Custom type clabWIFINeighboringWiFiBasicDataTransferRates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ClabWIFINeighboringWiFiBasicDataTransferRates_Type.__name__ = "OctetString"
_ClabWIFINeighboringWiFiBasicDataTransferRates_Object = MibTableColumn
clabWIFINeighboringWiFiBasicDataTransferRates = _ClabWIFINeighboringWiFiBasicDataTransferRates_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 15),
    _ClabWIFINeighboringWiFiBasicDataTransferRates_Type()
)
clabWIFINeighboringWiFiBasicDataTransferRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiBasicDataTransferRates.setStatus("current")


class _ClabWIFINeighboringWiFiSupportedDataTransferRates_Type(OctetString):
    """Custom type clabWIFINeighboringWiFiSupportedDataTransferRates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ClabWIFINeighboringWiFiSupportedDataTransferRates_Type.__name__ = "OctetString"
_ClabWIFINeighboringWiFiSupportedDataTransferRates_Object = MibTableColumn
clabWIFINeighboringWiFiSupportedDataTransferRates = _ClabWIFINeighboringWiFiSupportedDataTransferRates_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 16),
    _ClabWIFINeighboringWiFiSupportedDataTransferRates_Type()
)
clabWIFINeighboringWiFiSupportedDataTransferRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiSupportedDataTransferRates.setStatus("current")
_ClabWIFINeighboringWiFiDTIMPeriod_Type = Unsigned32
_ClabWIFINeighboringWiFiDTIMPeriod_Object = MibTableColumn
clabWIFINeighboringWiFiDTIMPeriod = _ClabWIFINeighboringWiFiDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 17),
    _ClabWIFINeighboringWiFiDTIMPeriod_Type()
)
clabWIFINeighboringWiFiDTIMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDTIMPeriod.setStatus("current")


class _ClabWIFINeighboringWiFiSidebandPosition_Type(Integer32):
    """Custom type clabWIFINeighboringWiFiSidebandPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 2),
          ("upper", 1))
    )


_ClabWIFINeighboringWiFiSidebandPosition_Type.__name__ = "Integer32"
_ClabWIFINeighboringWiFiSidebandPosition_Object = MibTableColumn
clabWIFINeighboringWiFiSidebandPosition = _ClabWIFINeighboringWiFiSidebandPosition_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 18),
    _ClabWIFINeighboringWiFiSidebandPosition_Type()
)
clabWIFINeighboringWiFiSidebandPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiSidebandPosition.setStatus("current")
_ClabWIFINeighboringWiFiDiagnosticsLastRunTimestamp_Type = DateAndTime
_ClabWIFINeighboringWiFiDiagnosticsLastRunTimestamp_Object = MibTableColumn
clabWIFINeighboringWiFiDiagnosticsLastRunTimestamp = _ClabWIFINeighboringWiFiDiagnosticsLastRunTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 19),
    _ClabWIFINeighboringWiFiDiagnosticsLastRunTimestamp_Type()
)
clabWIFINeighboringWiFiDiagnosticsLastRunTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsLastRunTimestamp.setStatus("current")


class _ClabWIFINeighboringWiFiDiagnosticsNonContiguousChannel_Type(Unsigned32):
    """Custom type clabWIFINeighboringWiFiDiagnosticsNonContiguousChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClabWIFINeighboringWiFiDiagnosticsNonContiguousChannel_Type.__name__ = "Unsigned32"
_ClabWIFINeighboringWiFiDiagnosticsNonContiguousChannel_Object = MibTableColumn
clabWIFINeighboringWiFiDiagnosticsNonContiguousChannel = _ClabWIFINeighboringWiFiDiagnosticsNonContiguousChannel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 6, 1, 20),
    _ClabWIFINeighboringWiFiDiagnosticsNonContiguousChannel_Type()
)
clabWIFINeighboringWiFiDiagnosticsNonContiguousChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsNonContiguousChannel.setStatus("current")
_ClabWIFINeighboringWiFiDiagnosticsResultNumberOfEntries_Type = Unsigned32
_ClabWIFINeighboringWiFiDiagnosticsResultNumberOfEntries_Object = MibScalar
clabWIFINeighboringWiFiDiagnosticsResultNumberOfEntries = _ClabWIFINeighboringWiFiDiagnosticsResultNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 21, 7),
    _ClabWIFINeighboringWiFiDiagnosticsResultNumberOfEntries_Type()
)
clabWIFINeighboringWiFiDiagnosticsResultNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFINeighboringWiFiDiagnosticsResultNumberOfEntries.setStatus("current")
_ClabWIFIRadioChannelWiFiDiagnostics_ObjectIdentity = ObjectIdentity
clabWIFIRadioChannelWiFiDiagnostics = _ClabWIFIRadioChannelWiFiDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22)
)


class _ClabWIFIRadioChannelWiFiDiagnosticsState_Type(Integer32):
    """Custom type clabWIFIRadioChannelWiFiDiagnosticsState based on Integer32"""
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
        *(("completed", 3),
          ("error", 4),
          ("none", 1),
          ("requested", 2))
    )


_ClabWIFIRadioChannelWiFiDiagnosticsState_Type.__name__ = "Integer32"
_ClabWIFIRadioChannelWiFiDiagnosticsState_Object = MibScalar
clabWIFIRadioChannelWiFiDiagnosticsState = _ClabWIFIRadioChannelWiFiDiagnosticsState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 1),
    _ClabWIFIRadioChannelWiFiDiagnosticsState_Type()
)
clabWIFIRadioChannelWiFiDiagnosticsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsState.setStatus("current")
_ClabWIFIRadioChannelWiFiDiagnosticsLastRunTimestamp_Type = DateAndTime
_ClabWIFIRadioChannelWiFiDiagnosticsLastRunTimestamp_Object = MibScalar
clabWIFIRadioChannelWiFiDiagnosticsLastRunTimestamp = _ClabWIFIRadioChannelWiFiDiagnosticsLastRunTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 2),
    _ClabWIFIRadioChannelWiFiDiagnosticsLastRunTimestamp_Type()
)
clabWIFIRadioChannelWiFiDiagnosticsLastRunTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsLastRunTimestamp.setStatus("current")
_ClabWIFIRadioChannelWiFiDiagnosticsResultNumberOfEntries_Type = Unsigned32
_ClabWIFIRadioChannelWiFiDiagnosticsResultNumberOfEntries_Object = MibScalar
clabWIFIRadioChannelWiFiDiagnosticsResultNumberOfEntries = _ClabWIFIRadioChannelWiFiDiagnosticsResultNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 3),
    _ClabWIFIRadioChannelWiFiDiagnosticsResultNumberOfEntries_Type()
)
clabWIFIRadioChannelWiFiDiagnosticsResultNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultNumberOfEntries.setStatus("current")
_ClabWIFIRadioChannelWiFiDiagnosticsResultsTable_Object = MibTable
clabWIFIRadioChannelWiFiDiagnosticsResultsTable = _ClabWIFIRadioChannelWiFiDiagnosticsResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 4)
)
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultsTable.setStatus("current")
_ClabWIFIRadioChannelWiFiDiagnosticsResultsEntry_Object = MibTableRow
clabWIFIRadioChannelWiFiDiagnosticsResultsEntry = _ClabWIFIRadioChannelWiFiDiagnosticsResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 4, 1)
)
clabWIFIRadioChannelWiFiDiagnosticsResultsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIRadioChannelWiFiDiagnosticsResultsChannel"),
)
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultsEntry.setStatus("current")
_ClabWIFIRadioChannelWiFiDiagnosticsResultsChannel_Type = Unsigned32
_ClabWIFIRadioChannelWiFiDiagnosticsResultsChannel_Object = MibTableColumn
clabWIFIRadioChannelWiFiDiagnosticsResultsChannel = _ClabWIFIRadioChannelWiFiDiagnosticsResultsChannel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 4, 1, 1),
    _ClabWIFIRadioChannelWiFiDiagnosticsResultsChannel_Type()
)
clabWIFIRadioChannelWiFiDiagnosticsResultsChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultsChannel.setStatus("current")


class _ClabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth_Type(Integer32):
    """Custom type clabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth based on Integer32"""
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
        *(("mhz160", 4),
          ("mhz20", 1),
          ("mhz40", 2),
          ("mhz80", 3))
    )


_ClabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth_Type.__name__ = "Integer32"
_ClabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth_Object = MibTableColumn
clabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth = _ClabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 4, 1, 2),
    _ClabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth_Type()
)
clabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth.setStatus("current")


class _ClabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity_Type(Unsigned32):
    """Custom type clabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ClabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity_Type.__name__ = "Unsigned32"
_ClabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity_Object = MibTableColumn
clabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity = _ClabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 4, 1, 3),
    _ClabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity_Type()
)
clabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity.setUnits("percentage")


class _ClabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi_Type(Unsigned32):
    """Custom type clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ClabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi_Type.__name__ = "Unsigned32"
_ClabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi_Object = MibTableColumn
clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi = _ClabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 4, 1, 4),
    _ClabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi_Type()
)
clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi.setUnits("percentage")
_ClabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFiClasses_Type = SnmpAdminString
_ClabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFiClasses_Object = MibTableColumn
clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFiClasses = _ClabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFiClasses_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 4, 1, 5),
    _ClabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFiClasses_Type()
)
clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFiClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFiClasses.setStatus("current")


class _ClabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand_Type(Integer32):
    """Custom type clabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ghz24", 1),
          ("ghz5", 2))
    )


_ClabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand_Type.__name__ = "Integer32"
_ClabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand_Object = MibTableColumn
clabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand = _ClabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 22, 4, 1, 6),
    _ClabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand_Type()
)
clabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand.setStatus("current")
_ClabWIFIAccessPointAccountingTable_Object = MibTable
clabWIFIAccessPointAccountingTable = _ClabWIFIAccessPointAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingTable.setStatus("current")
_ClabWIFIAccessPointAccountingEntry_Object = MibTableRow
clabWIFIAccessPointAccountingEntry = _ClabWIFIAccessPointAccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1)
)
clabWIFIAccessPointAccountingEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingEntry.setStatus("current")
_ClabWIFIAccessPointAccountingEnable_Type = TruthValue
_ClabWIFIAccessPointAccountingEnable_Object = MibTableColumn
clabWIFIAccessPointAccountingEnable = _ClabWIFIAccessPointAccountingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 1),
    _ClabWIFIAccessPointAccountingEnable_Type()
)
clabWIFIAccessPointAccountingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingEnable.setStatus("current")
_ClabWIFIAccessPointAccountingServerIPAddrType_Type = InetAddressType
_ClabWIFIAccessPointAccountingServerIPAddrType_Object = MibTableColumn
clabWIFIAccessPointAccountingServerIPAddrType = _ClabWIFIAccessPointAccountingServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 2),
    _ClabWIFIAccessPointAccountingServerIPAddrType_Type()
)
clabWIFIAccessPointAccountingServerIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingServerIPAddrType.setStatus("current")
_ClabWIFIAccessPointAccountingServerIPAddr_Type = InetAddress
_ClabWIFIAccessPointAccountingServerIPAddr_Object = MibTableColumn
clabWIFIAccessPointAccountingServerIPAddr = _ClabWIFIAccessPointAccountingServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 3),
    _ClabWIFIAccessPointAccountingServerIPAddr_Type()
)
clabWIFIAccessPointAccountingServerIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingServerIPAddr.setStatus("current")
_ClabWIFIAccessPointAccountingSecondaryServerIPAddrType_Type = InetAddressType
_ClabWIFIAccessPointAccountingSecondaryServerIPAddrType_Object = MibTableColumn
clabWIFIAccessPointAccountingSecondaryServerIPAddrType = _ClabWIFIAccessPointAccountingSecondaryServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 4),
    _ClabWIFIAccessPointAccountingSecondaryServerIPAddrType_Type()
)
clabWIFIAccessPointAccountingSecondaryServerIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingSecondaryServerIPAddrType.setStatus("current")
_ClabWIFIAccessPointAccountingSecondaryServerIPAddr_Type = InetAddress
_ClabWIFIAccessPointAccountingSecondaryServerIPAddr_Object = MibTableColumn
clabWIFIAccessPointAccountingSecondaryServerIPAddr = _ClabWIFIAccessPointAccountingSecondaryServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 5),
    _ClabWIFIAccessPointAccountingSecondaryServerIPAddr_Type()
)
clabWIFIAccessPointAccountingSecondaryServerIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingSecondaryServerIPAddr.setStatus("current")


class _ClabWIFIAccessPointAccountingServerPort_Type(InetPortNumber):
    """Custom type clabWIFIAccessPointAccountingServerPort based on InetPortNumber"""
    defaultValue = 1813


_ClabWIFIAccessPointAccountingServerPort_Object = MibTableColumn
clabWIFIAccessPointAccountingServerPort = _ClabWIFIAccessPointAccountingServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 6),
    _ClabWIFIAccessPointAccountingServerPort_Type()
)
clabWIFIAccessPointAccountingServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingServerPort.setStatus("current")


class _ClabWIFIAccessPointAccountingSecondaryServerPort_Type(InetPortNumber):
    """Custom type clabWIFIAccessPointAccountingSecondaryServerPort based on InetPortNumber"""
    defaultValue = 1813


_ClabWIFIAccessPointAccountingSecondaryServerPort_Object = MibTableColumn
clabWIFIAccessPointAccountingSecondaryServerPort = _ClabWIFIAccessPointAccountingSecondaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 7),
    _ClabWIFIAccessPointAccountingSecondaryServerPort_Type()
)
clabWIFIAccessPointAccountingSecondaryServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingSecondaryServerPort.setStatus("current")
_ClabWIFIAccessPointAccountingSecret_Type = SnmpAdminString
_ClabWIFIAccessPointAccountingSecret_Object = MibTableColumn
clabWIFIAccessPointAccountingSecret = _ClabWIFIAccessPointAccountingSecret_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 8),
    _ClabWIFIAccessPointAccountingSecret_Type()
)
clabWIFIAccessPointAccountingSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingSecret.setStatus("current")
_ClabWIFIAccessPointAccountingSecondarySecret_Type = SnmpAdminString
_ClabWIFIAccessPointAccountingSecondarySecret_Object = MibTableColumn
clabWIFIAccessPointAccountingSecondarySecret = _ClabWIFIAccessPointAccountingSecondarySecret_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 9),
    _ClabWIFIAccessPointAccountingSecondarySecret_Type()
)
clabWIFIAccessPointAccountingSecondarySecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingSecondarySecret.setStatus("current")
_ClabWIFIAccessPointAccountingInterimInterval_Type = Unsigned32
_ClabWIFIAccessPointAccountingInterimInterval_Object = MibTableColumn
clabWIFIAccessPointAccountingInterimInterval = _ClabWIFIAccessPointAccountingInterimInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 10),
    _ClabWIFIAccessPointAccountingInterimInterval_Type()
)
clabWIFIAccessPointAccountingInterimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingInterimInterval.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingInterimInterval.setUnits("seconds")
_ClabWIFIAccessPointAccountingRowStatus_Type = RowStatus
_ClabWIFIAccessPointAccountingRowStatus_Object = MibTableColumn
clabWIFIAccessPointAccountingRowStatus = _ClabWIFIAccessPointAccountingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 23, 1, 11),
    _ClabWIFIAccessPointAccountingRowStatus_Type()
)
clabWIFIAccessPointAccountingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAccountingRowStatus.setStatus("current")
_ClabWIFIAccessPointACTable_Object = MibTable
clabWIFIAccessPointACTable = _ClabWIFIAccessPointACTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointACTable.setStatus("deprecated")
_ClabWIFIAccessPointACEntry_Object = MibTableRow
clabWIFIAccessPointACEntry = _ClabWIFIAccessPointACEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24, 1)
)
clabWIFIAccessPointACEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointACEntry.setStatus("deprecated")


class _ClabWIFIAccessPointACAccessCategory_Type(Integer32):
    """Custom type clabWIFIAccessPointACAccessCategory based on Integer32"""
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
        *(("be", 1),
          ("bk", 2),
          ("vi", 3),
          ("vo", 4))
    )


_ClabWIFIAccessPointACAccessCategory_Type.__name__ = "Integer32"
_ClabWIFIAccessPointACAccessCategory_Object = MibTableColumn
clabWIFIAccessPointACAccessCategory = _ClabWIFIAccessPointACAccessCategory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24, 1, 1),
    _ClabWIFIAccessPointACAccessCategory_Type()
)
clabWIFIAccessPointACAccessCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACAccessCategory.setStatus("deprecated")


class _ClabWIFIAccessPointACAlias_Type(OctetString):
    """Custom type clabWIFIAccessPointACAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabWIFIAccessPointACAlias_Type.__name__ = "OctetString"
_ClabWIFIAccessPointACAlias_Object = MibTableColumn
clabWIFIAccessPointACAlias = _ClabWIFIAccessPointACAlias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24, 1, 2),
    _ClabWIFIAccessPointACAlias_Type()
)
clabWIFIAccessPointACAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACAlias.setStatus("deprecated")
_ClabWIFIAccessPointACAIFSN_Type = Unsigned32
_ClabWIFIAccessPointACAIFSN_Object = MibTableColumn
clabWIFIAccessPointACAIFSN = _ClabWIFIAccessPointACAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24, 1, 3),
    _ClabWIFIAccessPointACAIFSN_Type()
)
clabWIFIAccessPointACAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACAIFSN.setStatus("deprecated")
_ClabWIFIAccessPointACECWMin_Type = Unsigned32
_ClabWIFIAccessPointACECWMin_Object = MibTableColumn
clabWIFIAccessPointACECWMin = _ClabWIFIAccessPointACECWMin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24, 1, 4),
    _ClabWIFIAccessPointACECWMin_Type()
)
clabWIFIAccessPointACECWMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACECWMin.setStatus("deprecated")
_ClabWIFIAccessPointACECWMax_Type = Unsigned32
_ClabWIFIAccessPointACECWMax_Object = MibTableColumn
clabWIFIAccessPointACECWMax = _ClabWIFIAccessPointACECWMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24, 1, 5),
    _ClabWIFIAccessPointACECWMax_Type()
)
clabWIFIAccessPointACECWMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACECWMax.setStatus("deprecated")
_ClabWIFIAccessPointACTxOpMax_Type = Unsigned32
_ClabWIFIAccessPointACTxOpMax_Object = MibTableColumn
clabWIFIAccessPointACTxOpMax = _ClabWIFIAccessPointACTxOpMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24, 1, 6),
    _ClabWIFIAccessPointACTxOpMax_Type()
)
clabWIFIAccessPointACTxOpMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACTxOpMax.setStatus("deprecated")
_ClabWIFIAccessPointACAckPolicy_Type = TruthValue
_ClabWIFIAccessPointACAckPolicy_Object = MibTableColumn
clabWIFIAccessPointACAckPolicy = _ClabWIFIAccessPointACAckPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24, 1, 7),
    _ClabWIFIAccessPointACAckPolicy_Type()
)
clabWIFIAccessPointACAckPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACAckPolicy.setStatus("deprecated")
_ClabWIFIAccessPointACOutQLenHistogramIntervals_Type = OctetString
_ClabWIFIAccessPointACOutQLenHistogramIntervals_Object = MibTableColumn
clabWIFIAccessPointACOutQLenHistogramIntervals = _ClabWIFIAccessPointACOutQLenHistogramIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24, 1, 8),
    _ClabWIFIAccessPointACOutQLenHistogramIntervals_Type()
)
clabWIFIAccessPointACOutQLenHistogramIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACOutQLenHistogramIntervals.setStatus("deprecated")
_ClabWIFIAccessPointACOutQLenHistogramSampleInterval_Type = Unsigned32
_ClabWIFIAccessPointACOutQLenHistogramSampleInterval_Object = MibTableColumn
clabWIFIAccessPointACOutQLenHistogramSampleInterval = _ClabWIFIAccessPointACOutQLenHistogramSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 24, 1, 9),
    _ClabWIFIAccessPointACOutQLenHistogramSampleInterval_Type()
)
clabWIFIAccessPointACOutQLenHistogramSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACOutQLenHistogramSampleInterval.setStatus("deprecated")
_ClabWIFIAccessPointACStatsTable_Object = MibTable
clabWIFIAccessPointACStatsTable = _ClabWIFIAccessPointACStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsTable.setStatus("deprecated")
_ClabWIFIAccessPointACStatsEntry_Object = MibTableRow
clabWIFIAccessPointACStatsEntry = _ClabWIFIAccessPointACStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1)
)
clabWIFIAccessPointACStatsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsEntry.setStatus("deprecated")
_ClabWIFIAccessPointACStatsBytesSent_Type = Counter64
_ClabWIFIAccessPointACStatsBytesSent_Object = MibTableColumn
clabWIFIAccessPointACStatsBytesSent = _ClabWIFIAccessPointACStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1, 1),
    _ClabWIFIAccessPointACStatsBytesSent_Type()
)
clabWIFIAccessPointACStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsBytesSent.setStatus("deprecated")
_ClabWIFIAccessPointACStatsBytesReceived_Type = Counter64
_ClabWIFIAccessPointACStatsBytesReceived_Object = MibTableColumn
clabWIFIAccessPointACStatsBytesReceived = _ClabWIFIAccessPointACStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1, 2),
    _ClabWIFIAccessPointACStatsBytesReceived_Type()
)
clabWIFIAccessPointACStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsBytesReceived.setStatus("deprecated")
_ClabWIFIAccessPointACStatsPacketsSent_Type = Counter64
_ClabWIFIAccessPointACStatsPacketsSent_Object = MibTableColumn
clabWIFIAccessPointACStatsPacketsSent = _ClabWIFIAccessPointACStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1, 3),
    _ClabWIFIAccessPointACStatsPacketsSent_Type()
)
clabWIFIAccessPointACStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsPacketsSent.setStatus("deprecated")
_ClabWIFIAccessPointACStatsPacketsReceived_Type = Counter64
_ClabWIFIAccessPointACStatsPacketsReceived_Object = MibTableColumn
clabWIFIAccessPointACStatsPacketsReceived = _ClabWIFIAccessPointACStatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1, 4),
    _ClabWIFIAccessPointACStatsPacketsReceived_Type()
)
clabWIFIAccessPointACStatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsPacketsReceived.setStatus("deprecated")
_ClabWIFIAccessPointACStatsErrorsSent_Type = Unsigned32
_ClabWIFIAccessPointACStatsErrorsSent_Object = MibTableColumn
clabWIFIAccessPointACStatsErrorsSent = _ClabWIFIAccessPointACStatsErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1, 5),
    _ClabWIFIAccessPointACStatsErrorsSent_Type()
)
clabWIFIAccessPointACStatsErrorsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsErrorsSent.setStatus("deprecated")
_ClabWIFIAccessPointACStatsErrorsReceived_Type = Unsigned32
_ClabWIFIAccessPointACStatsErrorsReceived_Object = MibTableColumn
clabWIFIAccessPointACStatsErrorsReceived = _ClabWIFIAccessPointACStatsErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1, 6),
    _ClabWIFIAccessPointACStatsErrorsReceived_Type()
)
clabWIFIAccessPointACStatsErrorsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsErrorsReceived.setStatus("deprecated")
_ClabWIFIAccessPointACStatsDiscardPacketsSent_Type = Unsigned32
_ClabWIFIAccessPointACStatsDiscardPacketsSent_Object = MibTableColumn
clabWIFIAccessPointACStatsDiscardPacketsSent = _ClabWIFIAccessPointACStatsDiscardPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1, 7),
    _ClabWIFIAccessPointACStatsDiscardPacketsSent_Type()
)
clabWIFIAccessPointACStatsDiscardPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsDiscardPacketsSent.setStatus("deprecated")
_ClabWIFIAccessPointACStatsDiscardPacketsReceived_Type = Unsigned32
_ClabWIFIAccessPointACStatsDiscardPacketsReceived_Object = MibTableColumn
clabWIFIAccessPointACStatsDiscardPacketsReceived = _ClabWIFIAccessPointACStatsDiscardPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1, 8),
    _ClabWIFIAccessPointACStatsDiscardPacketsReceived_Type()
)
clabWIFIAccessPointACStatsDiscardPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsDiscardPacketsReceived.setStatus("deprecated")
_ClabWIFIAccessPointACStatsRetransCount_Type = Unsigned32
_ClabWIFIAccessPointACStatsRetransCount_Object = MibTableColumn
clabWIFIAccessPointACStatsRetransCount = _ClabWIFIAccessPointACStatsRetransCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1, 9),
    _ClabWIFIAccessPointACStatsRetransCount_Type()
)
clabWIFIAccessPointACStatsRetransCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsRetransCount.setStatus("deprecated")
_ClabWIFIAccessPointACStatsOutQLenHistogram_Type = OctetString
_ClabWIFIAccessPointACStatsOutQLenHistogram_Object = MibTableColumn
clabWIFIAccessPointACStatsOutQLenHistogram = _ClabWIFIAccessPointACStatsOutQLenHistogram_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 25, 1, 10),
    _ClabWIFIAccessPointACStatsOutQLenHistogram_Type()
)
clabWIFIAccessPointACStatsOutQLenHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointACStatsOutQLenHistogram.setStatus("deprecated")
_ClabWIFIAccessPointRadiusSettingsObjects_ObjectIdentity = ObjectIdentity
clabWIFIAccessPointRadiusSettingsObjects = _ClabWIFIAccessPointRadiusSettingsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 26)
)
_ClabWIFIAccessPointRadiusSettingsRadiusServerRetries_Type = Unsigned32
_ClabWIFIAccessPointRadiusSettingsRadiusServerRetries_Object = MibScalar
clabWIFIAccessPointRadiusSettingsRadiusServerRetries = _ClabWIFIAccessPointRadiusSettingsRadiusServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 26, 1),
    _ClabWIFIAccessPointRadiusSettingsRadiusServerRetries_Type()
)
clabWIFIAccessPointRadiusSettingsRadiusServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsRadiusServerRetries.setStatus("current")
_ClabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout_Type = Unsigned32
_ClabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout_Object = MibScalar
clabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout = _ClabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 26, 2),
    _ClabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout_Type()
)
clabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout.setUnits("seconds")
_ClabWIFIAccessPointRadiusSettingsPMKLifetime_Type = Unsigned32
_ClabWIFIAccessPointRadiusSettingsPMKLifetime_Object = MibScalar
clabWIFIAccessPointRadiusSettingsPMKLifetime = _ClabWIFIAccessPointRadiusSettingsPMKLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 26, 3),
    _ClabWIFIAccessPointRadiusSettingsPMKLifetime_Type()
)
clabWIFIAccessPointRadiusSettingsPMKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsPMKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsPMKLifetime.setUnits("seconds")
_ClabWIFIAccessPointRadiusSettingsPMKCachingEnable_Type = TruthValue
_ClabWIFIAccessPointRadiusSettingsPMKCachingEnable_Object = MibScalar
clabWIFIAccessPointRadiusSettingsPMKCachingEnable = _ClabWIFIAccessPointRadiusSettingsPMKCachingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 26, 4),
    _ClabWIFIAccessPointRadiusSettingsPMKCachingEnable_Type()
)
clabWIFIAccessPointRadiusSettingsPMKCachingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsPMKCachingEnable.setStatus("current")
_ClabWIFIAccessPointRadiusSettingsPMKCachingInterval_Type = Unsigned32
_ClabWIFIAccessPointRadiusSettingsPMKCachingInterval_Object = MibScalar
clabWIFIAccessPointRadiusSettingsPMKCachingInterval = _ClabWIFIAccessPointRadiusSettingsPMKCachingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 26, 5),
    _ClabWIFIAccessPointRadiusSettingsPMKCachingInterval_Type()
)
clabWIFIAccessPointRadiusSettingsPMKCachingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsPMKCachingInterval.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsPMKCachingInterval.setUnits("seconds")
_ClabWIFIAccessPointRadiusSettingsMaxAuthenticationAttempts_Type = Unsigned32
_ClabWIFIAccessPointRadiusSettingsMaxAuthenticationAttempts_Object = MibScalar
clabWIFIAccessPointRadiusSettingsMaxAuthenticationAttempts = _ClabWIFIAccessPointRadiusSettingsMaxAuthenticationAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 26, 6),
    _ClabWIFIAccessPointRadiusSettingsMaxAuthenticationAttempts_Type()
)
clabWIFIAccessPointRadiusSettingsMaxAuthenticationAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsMaxAuthenticationAttempts.setStatus("current")
_ClabWIFIAccessPointRadiusSettingsBlacklistTableTimeout_Type = Unsigned32
_ClabWIFIAccessPointRadiusSettingsBlacklistTableTimeout_Object = MibScalar
clabWIFIAccessPointRadiusSettingsBlacklistTableTimeout = _ClabWIFIAccessPointRadiusSettingsBlacklistTableTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 26, 7),
    _ClabWIFIAccessPointRadiusSettingsBlacklistTableTimeout_Type()
)
clabWIFIAccessPointRadiusSettingsBlacklistTableTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsBlacklistTableTimeout.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsBlacklistTableTimeout.setUnits("seconds")
_ClabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval_Type = Unsigned32
_ClabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval_Object = MibScalar
clabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval = _ClabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 26, 8),
    _ClabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval_Type()
)
clabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval.setUnits("seconds")
_ClabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth_Type = Unsigned32
_ClabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth_Object = MibScalar
clabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth = _ClabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 26, 9),
    _ClabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth_Type()
)
clabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth.setStatus("current")
if mibBuilder.loadTexts:
    clabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth.setUnits("seconds")
_ClabWIFIAccessPointAC2Table_Object = MibTable
clabWIFIAccessPointAC2Table = _ClabWIFIAccessPointAC2Table_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2Table.setStatus("current")
_ClabWIFIAccessPointAC2Entry_Object = MibTableRow
clabWIFIAccessPointAC2Entry = _ClabWIFIAccessPointAC2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1)
)
clabWIFIAccessPointAC2Entry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointAC2Index"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2Entry.setStatus("current")
_ClabWIFIAccessPointAC2Index_Type = Unsigned32
_ClabWIFIAccessPointAC2Index_Object = MibTableColumn
clabWIFIAccessPointAC2Index = _ClabWIFIAccessPointAC2Index_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1, 1),
    _ClabWIFIAccessPointAC2Index_Type()
)
clabWIFIAccessPointAC2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2Index.setStatus("current")


class _ClabWIFIAccessPointAC2AccessCategory_Type(Integer32):
    """Custom type clabWIFIAccessPointAC2AccessCategory based on Integer32"""
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
        *(("be", 1),
          ("bk", 2),
          ("vi", 3),
          ("vo", 4))
    )


_ClabWIFIAccessPointAC2AccessCategory_Type.__name__ = "Integer32"
_ClabWIFIAccessPointAC2AccessCategory_Object = MibTableColumn
clabWIFIAccessPointAC2AccessCategory = _ClabWIFIAccessPointAC2AccessCategory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1, 2),
    _ClabWIFIAccessPointAC2AccessCategory_Type()
)
clabWIFIAccessPointAC2AccessCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2AccessCategory.setStatus("current")


class _ClabWIFIAccessPointAC2Alias_Type(SnmpAdminString):
    """Custom type clabWIFIAccessPointAC2Alias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ClabWIFIAccessPointAC2Alias_Type.__name__ = "SnmpAdminString"
_ClabWIFIAccessPointAC2Alias_Object = MibTableColumn
clabWIFIAccessPointAC2Alias = _ClabWIFIAccessPointAC2Alias_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1, 3),
    _ClabWIFIAccessPointAC2Alias_Type()
)
clabWIFIAccessPointAC2Alias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2Alias.setStatus("current")


class _ClabWIFIAccessPointAC2AIFSN_Type(Unsigned32):
    """Custom type clabWIFIAccessPointAC2AIFSN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_ClabWIFIAccessPointAC2AIFSN_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointAC2AIFSN_Object = MibTableColumn
clabWIFIAccessPointAC2AIFSN = _ClabWIFIAccessPointAC2AIFSN_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1, 4),
    _ClabWIFIAccessPointAC2AIFSN_Type()
)
clabWIFIAccessPointAC2AIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2AIFSN.setStatus("current")


class _ClabWIFIAccessPointAC2ECWMin_Type(Unsigned32):
    """Custom type clabWIFIAccessPointAC2ECWMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ClabWIFIAccessPointAC2ECWMin_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointAC2ECWMin_Object = MibTableColumn
clabWIFIAccessPointAC2ECWMin = _ClabWIFIAccessPointAC2ECWMin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1, 5),
    _ClabWIFIAccessPointAC2ECWMin_Type()
)
clabWIFIAccessPointAC2ECWMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2ECWMin.setStatus("current")


class _ClabWIFIAccessPointAC2ECWMax_Type(Unsigned32):
    """Custom type clabWIFIAccessPointAC2ECWMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ClabWIFIAccessPointAC2ECWMax_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointAC2ECWMax_Object = MibTableColumn
clabWIFIAccessPointAC2ECWMax = _ClabWIFIAccessPointAC2ECWMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1, 6),
    _ClabWIFIAccessPointAC2ECWMax_Type()
)
clabWIFIAccessPointAC2ECWMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2ECWMax.setStatus("current")


class _ClabWIFIAccessPointAC2TxOpMax_Type(Unsigned32):
    """Custom type clabWIFIAccessPointAC2TxOpMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClabWIFIAccessPointAC2TxOpMax_Type.__name__ = "Unsigned32"
_ClabWIFIAccessPointAC2TxOpMax_Object = MibTableColumn
clabWIFIAccessPointAC2TxOpMax = _ClabWIFIAccessPointAC2TxOpMax_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1, 7),
    _ClabWIFIAccessPointAC2TxOpMax_Type()
)
clabWIFIAccessPointAC2TxOpMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2TxOpMax.setStatus("current")
_ClabWIFIAccessPointAC2AckPolicy_Type = TruthValue
_ClabWIFIAccessPointAC2AckPolicy_Object = MibTableColumn
clabWIFIAccessPointAC2AckPolicy = _ClabWIFIAccessPointAC2AckPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1, 8),
    _ClabWIFIAccessPointAC2AckPolicy_Type()
)
clabWIFIAccessPointAC2AckPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2AckPolicy.setStatus("current")
_ClabWIFIAccessPointAC2OutQLenHistogramIntervals_Type = SnmpAdminString
_ClabWIFIAccessPointAC2OutQLenHistogramIntervals_Object = MibTableColumn
clabWIFIAccessPointAC2OutQLenHistogramIntervals = _ClabWIFIAccessPointAC2OutQLenHistogramIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1, 9),
    _ClabWIFIAccessPointAC2OutQLenHistogramIntervals_Type()
)
clabWIFIAccessPointAC2OutQLenHistogramIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2OutQLenHistogramIntervals.setStatus("current")
_ClabWIFIAccessPointAC2OutQLenHistogramSampleInterval_Type = Unsigned32
_ClabWIFIAccessPointAC2OutQLenHistogramSampleInterval_Object = MibTableColumn
clabWIFIAccessPointAC2OutQLenHistogramSampleInterval = _ClabWIFIAccessPointAC2OutQLenHistogramSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 27, 1, 10),
    _ClabWIFIAccessPointAC2OutQLenHistogramSampleInterval_Type()
)
clabWIFIAccessPointAC2OutQLenHistogramSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2OutQLenHistogramSampleInterval.setStatus("current")
_ClabWIFIAccessPointAC2StatsTable_Object = MibTable
clabWIFIAccessPointAC2StatsTable = _ClabWIFIAccessPointAC2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28)
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsTable.setStatus("current")
_ClabWIFIAccessPointAC2StatsEntry_Object = MibTableRow
clabWIFIAccessPointAC2StatsEntry = _ClabWIFIAccessPointAC2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1)
)
clabWIFIAccessPointAC2StatsEntry.setIndexNames(
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointId"),
    (0, "CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsIndex"),
)
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsEntry.setStatus("current")
_ClabWIFIAccessPointAC2StatsIndex_Type = Unsigned32
_ClabWIFIAccessPointAC2StatsIndex_Object = MibTableColumn
clabWIFIAccessPointAC2StatsIndex = _ClabWIFIAccessPointAC2StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 1),
    _ClabWIFIAccessPointAC2StatsIndex_Type()
)
clabWIFIAccessPointAC2StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsIndex.setStatus("current")
_ClabWIFIAccessPointAC2StatsBytesSent_Type = Counter64
_ClabWIFIAccessPointAC2StatsBytesSent_Object = MibTableColumn
clabWIFIAccessPointAC2StatsBytesSent = _ClabWIFIAccessPointAC2StatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 2),
    _ClabWIFIAccessPointAC2StatsBytesSent_Type()
)
clabWIFIAccessPointAC2StatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsBytesSent.setStatus("current")
_ClabWIFIAccessPointAC2StatsBytesReceived_Type = Counter64
_ClabWIFIAccessPointAC2StatsBytesReceived_Object = MibTableColumn
clabWIFIAccessPointAC2StatsBytesReceived = _ClabWIFIAccessPointAC2StatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 3),
    _ClabWIFIAccessPointAC2StatsBytesReceived_Type()
)
clabWIFIAccessPointAC2StatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsBytesReceived.setStatus("current")
_ClabWIFIAccessPointAC2StatsPacketsSent_Type = Counter64
_ClabWIFIAccessPointAC2StatsPacketsSent_Object = MibTableColumn
clabWIFIAccessPointAC2StatsPacketsSent = _ClabWIFIAccessPointAC2StatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 4),
    _ClabWIFIAccessPointAC2StatsPacketsSent_Type()
)
clabWIFIAccessPointAC2StatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsPacketsSent.setStatus("current")
_ClabWIFIAccessPointAC2StatsPacketsReceived_Type = Counter64
_ClabWIFIAccessPointAC2StatsPacketsReceived_Object = MibTableColumn
clabWIFIAccessPointAC2StatsPacketsReceived = _ClabWIFIAccessPointAC2StatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 5),
    _ClabWIFIAccessPointAC2StatsPacketsReceived_Type()
)
clabWIFIAccessPointAC2StatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsPacketsReceived.setStatus("current")
_ClabWIFIAccessPointAC2StatsErrorsSent_Type = Unsigned32
_ClabWIFIAccessPointAC2StatsErrorsSent_Object = MibTableColumn
clabWIFIAccessPointAC2StatsErrorsSent = _ClabWIFIAccessPointAC2StatsErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 6),
    _ClabWIFIAccessPointAC2StatsErrorsSent_Type()
)
clabWIFIAccessPointAC2StatsErrorsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsErrorsSent.setStatus("current")
_ClabWIFIAccessPointAC2StatsErrorsReceived_Type = Unsigned32
_ClabWIFIAccessPointAC2StatsErrorsReceived_Object = MibTableColumn
clabWIFIAccessPointAC2StatsErrorsReceived = _ClabWIFIAccessPointAC2StatsErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 7),
    _ClabWIFIAccessPointAC2StatsErrorsReceived_Type()
)
clabWIFIAccessPointAC2StatsErrorsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsErrorsReceived.setStatus("current")
_ClabWIFIAccessPointAC2StatsDiscardPacketsSent_Type = Unsigned32
_ClabWIFIAccessPointAC2StatsDiscardPacketsSent_Object = MibTableColumn
clabWIFIAccessPointAC2StatsDiscardPacketsSent = _ClabWIFIAccessPointAC2StatsDiscardPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 8),
    _ClabWIFIAccessPointAC2StatsDiscardPacketsSent_Type()
)
clabWIFIAccessPointAC2StatsDiscardPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsDiscardPacketsSent.setStatus("current")
_ClabWIFIAccessPointAC2StatsDiscardPacketsReceived_Type = Unsigned32
_ClabWIFIAccessPointAC2StatsDiscardPacketsReceived_Object = MibTableColumn
clabWIFIAccessPointAC2StatsDiscardPacketsReceived = _ClabWIFIAccessPointAC2StatsDiscardPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 9),
    _ClabWIFIAccessPointAC2StatsDiscardPacketsReceived_Type()
)
clabWIFIAccessPointAC2StatsDiscardPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsDiscardPacketsReceived.setStatus("current")
_ClabWIFIAccessPointAC2StatsRetransCount_Type = Unsigned32
_ClabWIFIAccessPointAC2StatsRetransCount_Object = MibTableColumn
clabWIFIAccessPointAC2StatsRetransCount = _ClabWIFIAccessPointAC2StatsRetransCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 10),
    _ClabWIFIAccessPointAC2StatsRetransCount_Type()
)
clabWIFIAccessPointAC2StatsRetransCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsRetransCount.setStatus("current")
_ClabWIFIAccessPointAC2StatsOutQLenHistogram_Type = SnmpAdminString
_ClabWIFIAccessPointAC2StatsOutQLenHistogram_Object = MibTableColumn
clabWIFIAccessPointAC2StatsOutQLenHistogram = _ClabWIFIAccessPointAC2StatsOutQLenHistogram_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 1, 28, 1, 11),
    _ClabWIFIAccessPointAC2StatsOutQLenHistogram_Type()
)
clabWIFIAccessPointAC2StatsOutQLenHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clabWIFIAccessPointAC2StatsOutQLenHistogram.setStatus("current")
_ClabWIFIMibConformance_ObjectIdentity = ObjectIdentity
clabWIFIMibConformance = _ClabWIFIMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 2)
)
_ClabWIFIMibCompliances_ObjectIdentity = ObjectIdentity
clabWIFIMibCompliances = _ClabWIFIMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 2, 1)
)
_ClabWIFIMibGroups_ObjectIdentity = ObjectIdentity
clabWIFIMibGroups = _ClabWIFIMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 2, 2)
)

# Managed Objects groups

clabWIFIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 2, 2, 1)
)
clabWIFIGroup.setObjects(
      *(("CLAB-WIFI-MIB", "clabWIFIWiFiRadioNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFIWiFiSSIDNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFIWiFiAccessPointNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFIWiFiEndPointNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDSteeringEnabled"),
        ("CLAB-WIFI-MIB", "clabWIFICommitSettings"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatus"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioAlias"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioName"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioLastChange"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioLowerLayers"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioUpstream"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioMaxBitRate"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioSupportedFrequencyBands"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioOperatingFrequencyBand"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioSupportedStandards"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioOperatingStandards"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioPossibleChannels"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioChannelsInUse"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioChannel"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioAutoChannelSupported"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioAutoChannelEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioAutoChannelRefreshPeriod"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioOperatingChannelBandwidth"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioExtensionChannel"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioGuardInterval"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioMCS"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioTransmitPowerSupported"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioTransmitPower"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioIEEE80211hSupported"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioIEEE80211hEnabled"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioRegulatoryDomain"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioNonContiguousChannel"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioCarrierSenseThresholdInUse"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioRtsCtsExchange"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioRetryLimit"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioCCARequest"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioRPIHistogramRequest"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioFragmentationThreshold"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioRTSThreshold"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioLongRetryLimit"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioBeaconPeriod"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioDTIMPeriod"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioPacketAggregationEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioBasicDataTransmitRates"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioOperationalDataTransmitRates"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioSupportedDataTransmitRates"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioCarrierSenseThresholdRangeMin"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioCarrierSenseThresholdRangeMax"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioCCAReport"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioRPIHistogramReport"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioPreambleType"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsBytesSent"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsBytesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsErrorsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsErrorsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsDiscardPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsDiscardPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsPLCPErrorCount"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsFCSErrorCount"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsInvalidMACCount"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsPacketsOtherReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsNoise"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsFramesRetransmissionsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsFramesDuplicatedReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsChannelUtilization"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioChannelWiFiDiagnosticsState"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioChannelWiFiDiagnosticsLastRunTimestamp"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioChannelWiFiDiagnosticsResultNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFiClasses"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDiagnosticsMode"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDiagnosticsInterval"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDiagnosticsState"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDiagnosticsTableClear"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDiagnosticsTableMaxNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiSSID"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiBSSID"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiMode"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiChannel"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiSignalStrength"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiSecurityModeEnabled"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiEncryptionMode"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiOperatingFrequencyBand"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiSupportedStandards"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiOperatingStandards"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiOperatingChannelBandwidth"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiBeaconPeriod"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiNoise"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiBasicDataTransferRates"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiSupportedDataTransferRates"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDTIMPeriod"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiSidebandPosition"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDiagnosticsLastRunTimestamp"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDiagnosticsNonContiguousChannel"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDiagnosticsResultNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFINeighboringWiFiDiagnosticsLastRunTimestamp"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDEnable"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatus"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDAlias"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDName"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDLastChange"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDLowerLayers"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDBSSID"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDMACAddress"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDSSID"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDRowStatus"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDFragmentationEnable"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPeriodicStatsNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsBytesSent"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsBytesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsErrorsSent"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsErrorsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsUnicastPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsUnicastPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsDiscardPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsDiscardPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsMulticastPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsMulticastPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsBroadcastPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsBroadcastPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsUnknownProtoPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsRetransCount"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsRetryCount"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsMultipleRetryCount"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsACKFailureCount"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDStatsAggregatedPacketCount"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointStatus"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAlias"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSSIDReference"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSSIDAdvertisementEnabled"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWMMCapability"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointUAPSDCapability"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWMMEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointUAPSDEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAssociatedDeviceNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRowStatus"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPublicAccessMode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointIsolationEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointMaxAssociatedDevices"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointSupported"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointEnabled"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointInterworkingCapability"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointInterworkingServiceEnabled"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointMACAddressControlEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAllowedMACAddress"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointClientSessionNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityModesSupported"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityModeEnabled"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityWEPKey"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityPreSharedKey"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityKeyPassphrase"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityRekeyingInterval"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityRadiusServerIPAddrType"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityRadiusServerIPAddr"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityRadiusServerPort"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityRadiusSecret"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityRowstatus"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityWEPKey2"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityWEPKey3"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityWEPKey4"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityWEPIndex"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityWEPPassPhrase"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityWPAEncryption"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddrType"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddr"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecuritySecondaryRadiusServerPort"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecuritySecondaryRadiusSecret"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityEnableManagementFrameProtection"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityReset"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRadiusRetries"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointSecurityLanRoutingEnabled"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWPSEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWPSConfigMethodsSupported"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWPSRowStatus"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWPSSetWPSMethods"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWPSAPPin"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWPSSetWPSClientPin"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWPSConfigMethodsEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceMACAddress"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceAuthenticationState"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceLastDataDownlinkRate"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceLastDataUplinkRate"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceSignalStrength"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceRetransmissions"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceActive"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceMaxPacketRetryCount"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceSecurityMode"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceAssociationState"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsDeviceMACAddress"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsFramesSent"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsDataFramesSentAck"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsDataFramesSentNoAck"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsDataFramesLost"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsFramesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsDataFramesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsDataFramesDuplicateReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsProbesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsProbesRejected"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsRSSI"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsSNR"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsDisassociations"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsAuthenticationFailures"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsLastTimeAssociation"),
        ("CLAB-WIFI-MIB", "clabWIFIPeriodicStatsLastTimeDisassociation"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyBlockAfterAttempts"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyAllocatedBandwidth"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyAuthenticationFailures"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyNonAuthenticatedTraffic"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyAssociationFailures"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyStatsInterval"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicySNRThreshold"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyANPIThreshold"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyLowReceivedPowerThreshold"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyLowPowerDeniedAccessThreshold"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyLowPowerDisassociationThreshold"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyRowStatus"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyBeaconMcsLevelInUse"),
        ("CLAB-WIFI-MIB", "clabWIFISSIDPolicyBeaconMcsLevelsSupported"),
        ("CLAB-WIFI-MIB", "clabWIFIClientSessionsDeviceMACAddress"),
        ("CLAB-WIFI-MIB", "clabWIFIClientSessionsStart"),
        ("CLAB-WIFI-MIB", "clabWIFIClientSessionsStop"),
        ("CLAB-WIFI-MIB", "clabWIFIClientSessionsTerminationCode"),
        ("CLAB-WIFI-MIB", "clabWIFIClientSessionsTerminationMeaning"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsDeviceMACAddress"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsFramesSent"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsDataFramesSentAck"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsDataFramesSentNoAck"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsDataFramesLost"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsFramesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsDataFramesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsDataFramesDuplicateReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsProbesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsProbesRejected"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsRSSI"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsSNR"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsDisassociations"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsAuthenticationFailures"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsLastTimeAssociation"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsLastTimeDisassociation"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsThroughput"),
        ("CLAB-WIFI-MIB", "clabWIFIClientStatsPktErrorRatePerSTA"),
        ("CLAB-WIFI-MIB", "clabWIFIRadiusClientNASIdentifier"),
        ("CLAB-WIFI-MIB", "clabWIFIRadiusClientLocationPolicy"),
        ("CLAB-WIFI-MIB", "clabWIFIRadiusClientOperatorName"),
        ("CLAB-WIFI-MIB", "clabWIFIRadiusClientLocationInformation"),
        ("CLAB-WIFI-MIB", "clabWIFIRadiusClientLocationData"),
        ("CLAB-WIFI-MIB", "clabWIFIRadiusClientUsageReports"),
        ("CLAB-WIFI-MIB", "clabWIFIRadiusClientIntervalInterimReport"),
        ("CLAB-WIFI-MIB", "clabWIFIRadiusClientAPTransitionReport"),
        ("CLAB-WIFI-MIB", "clabWIFIRadiusClientGigawordReport"),
        ("CLAB-WIFI-MIB", "clabWIFIRadiusClientRowStatus"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointClearAccessControlFilterTable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccessControlFilterAccessAllow"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccessControlFilterMACAddress"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccessControlFilterNumberOfEntries"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointInterworkingServiceInternet"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointInterworkingServiceHESSID"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointInterworkingServiceAccessNetworkType"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointInterworkingServiceVenueGroupCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointInterworkingServiceVenueTypeCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointCapabilities"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOnlineSignupSupported"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointDGAFEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointP2PEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointQoSMappingEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointASRAEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointANQPDomainID"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointEAPMethod"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointManagementFrameProtectionEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOperatorNameCountryCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOperatorName"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointConsortiumOI"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointDomainNamesDomainName"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointThreeGPPNetworkMNC"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointThreeGPPNetworkMCC"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2VenueNameCountryCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2VenueName"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealmsEncodingType"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealms"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealmsEapMethod"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersID"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersValue"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderServerURI"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderNAI"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderIconFileName"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderIconType"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderIconWidth"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderIconHeight"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderServiceDescription"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspoint2OSUProviderMethodsList"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointWANMetricsLinkStatus"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointWANMetricsAtCapacity"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointWANMetricsDownlinkSpeed"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointWANMetricsUplinkSpeed"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointWANMetricsDownlinkLoad"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointWANMetricsUplinkLoad"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingServerIPAddrType"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingServerIPAddr"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingSecondaryServerIPAddrType"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingSecondaryServerIPAddr"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingServerPort"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingSecondaryServerPort"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingSecret"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingSecondarySecret"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingInterimInterval"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccountingRowStatus"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2AccessCategory"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2Alias"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2AIFSN"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2ECWMin"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2ECWMax"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2TxOpMax"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2AckPolicy"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2OutQLenHistogramIntervals"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2OutQLenHistogramSampleInterval"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsBytesSent"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsBytesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsErrorsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsErrorsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsDiscardPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsDiscardPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsRetransCount"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAC2StatsOutQLenHistogram"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRadiusSettingsRadiusServerRetries"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRadiusSettingsPMKLifetime"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRadiusSettingsPMKCachingEnable"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRadiusSettingsPMKCachingInterval"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRadiusSettingsMaxAuthenticationAttempts"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRadiusSettingsBlacklistTableTimeout"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth"),
        ("CLAB-WIFI-MIB", "clabWIFIWIFIEventNotifText"),
        ("CLAB-WIFI-MIB", "clabWIFIWIFIEventNotifEventId"),
        ("CLAB-WIFI-MIB", "clabWIFIWIFIEventNotifTimeStamp"))
)
if mibBuilder.loadTexts:
    clabWIFIGroup.setStatus("current")

clabDeprecatedObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 2, 2, 99)
)
clabDeprecatedObjectsGroup.setObjects(
      *(("CLAB-WIFI-MIB", "clabWIFIRadioCarrierSenseThresholdRange"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioStatsChanUtilization"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioFrameAggregationLevel"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioThroughput"),
        ("CLAB-WIFI-MIB", "clabWIFIRadioPktErrorRateSTA"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointRetryLimit"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWPSConfigMethodsEnabled"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointWPSSetWPSMethod"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAssociatedDeviceCount"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceStationCount"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceMaxNumOfStations"),
        ("CLAB-WIFI-MIB", "clabWIFIAssociatedDeviceEncryptionAlgorithm"),
        ("CLAB-WIFI-MIB", "clabWIFIDataRateStatsFramesSent"),
        ("CLAB-WIFI-MIB", "clabWIFIDataRateStatsFramesRetransmissionsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIDataRateStatsFramesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIDataRateStatsFramesDuplicatedReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIWIFICommitSettingsValue"),
        ("CLAB-WIFI-MIB", "clabWIFIApNeighborStatsSSID"),
        ("CLAB-WIFI-MIB", "clabWIFIApNeighborStatsCurrentChannel"),
        ("CLAB-WIFI-MIB", "clabWIFIApNeighborStatsCurrentBandwidth"),
        ("CLAB-WIFI-MIB", "clabWIFIApNeighborStatsRSSI"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointCapabilityList"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointVenueNameCountryCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointVenueName"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointNAIRealmsEncodingType"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointNAIRealms"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointNAIRealmsEapMethod"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersID"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersValue"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderServerURI"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderNAI"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderNamesLanguageCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderNamesFriendlyName"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderIconFileName"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderIconType"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderIconWidth"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderIconHeight"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderIconLanguageCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderServiceDescription"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointPasspointOSUProviderMethodsList"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACAccessCategory"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACAlias"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACAIFSN"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACECWMin"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACECWMax"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACTxOpMax"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACAckPolicy"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACOutQLenHistogramIntervals"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACOutQLenHistogramSampleInterval"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACStatsBytesSent"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACStatsBytesReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACStatsPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACStatsPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACStatsErrorsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACStatsErrorsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACStatsDiscardPacketsSent"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACStatsDiscardPacketsReceived"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACStatsRetransCount"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointACStatsOutQLenHistogram"),
        ("CLAB-WIFI-MIB", "clabWIFIAccessPointAccessControlFilterEnable"))
)
if mibBuilder.loadTexts:
    clabDeprecatedObjectsGroup.setStatus("obsolete")


# Notification objects

clabWIFIWIFIEventNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 0, 1)
)
clabWIFIWIFIEventNotif.setObjects(
      *(("CLAB-WIFI-MIB", "clabWIFIWIFIEventNotifText"),
        ("CLAB-WIFI-MIB", "clabWIFIWIFIEventNotifEventId"),
        ("CLAB-WIFI-MIB", "clabWIFIWIFIEventNotifTimeStamp"))
)
if mibBuilder.loadTexts:
    clabWIFIWIFIEventNotif.setStatus(
        "current"
    )


# Notifications groups

clabWIFINotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 2, 2, 2)
)
clabWIFINotificationsGroup.setObjects(
    ("CLAB-WIFI-MIB", "clabWIFIWIFIEventNotif")
)
if mibBuilder.loadTexts:
    clabWIFINotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

clabWIFICompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    clabWIFICompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-WIFI-MIB",
    **{"PktErrorRateType": PktErrorRateType,
       "clabWIFIMib": clabWIFIMib,
       "clabWIFINotifications": clabWIFINotifications,
       "clabWIFIWIFIEventNotif": clabWIFIWIFIEventNotif,
       "clabWIFIWIFIEventNotifgroup": clabWIFIWIFIEventNotifgroup,
       "clabWIFIWIFIEventNotifText": clabWIFIWIFIEventNotifText,
       "clabWIFIWIFIEventNotifEventId": clabWIFIWIFIEventNotifEventId,
       "clabWIFIWIFIEventNotifTimeStamp": clabWIFIWIFIEventNotifTimeStamp,
       "clabWIFIObjects": clabWIFIObjects,
       "clabWIFIWiFi": clabWIFIWiFi,
       "clabWIFIWiFiRadioNumberOfEntries": clabWIFIWiFiRadioNumberOfEntries,
       "clabWIFIWiFiSSIDNumberOfEntries": clabWIFIWiFiSSIDNumberOfEntries,
       "clabWIFIWiFiAccessPointNumberOfEntries": clabWIFIWiFiAccessPointNumberOfEntries,
       "clabWIFIWiFiEndPointNumberOfEntries": clabWIFIWiFiEndPointNumberOfEntries,
       "clabWIFISSIDSteeringEnabled": clabWIFISSIDSteeringEnabled,
       "clabWIFICommitSettings": clabWIFICommitSettings,
       "clabWIFIRadioTable": clabWIFIRadioTable,
       "clabWIFIRadioEntry": clabWIFIRadioEntry,
       "clabWIFIRadioId": clabWIFIRadioId,
       "clabWIFIRadioEnable": clabWIFIRadioEnable,
       "clabWIFIRadioStatus": clabWIFIRadioStatus,
       "clabWIFIRadioAlias": clabWIFIRadioAlias,
       "clabWIFIRadioName": clabWIFIRadioName,
       "clabWIFIRadioLastChange": clabWIFIRadioLastChange,
       "clabWIFIRadioLowerLayers": clabWIFIRadioLowerLayers,
       "clabWIFIRadioUpstream": clabWIFIRadioUpstream,
       "clabWIFIRadioMaxBitRate": clabWIFIRadioMaxBitRate,
       "clabWIFIRadioSupportedFrequencyBands": clabWIFIRadioSupportedFrequencyBands,
       "clabWIFIRadioOperatingFrequencyBand": clabWIFIRadioOperatingFrequencyBand,
       "clabWIFIRadioSupportedStandards": clabWIFIRadioSupportedStandards,
       "clabWIFIRadioOperatingStandards": clabWIFIRadioOperatingStandards,
       "clabWIFIRadioPossibleChannels": clabWIFIRadioPossibleChannels,
       "clabWIFIRadioChannelsInUse": clabWIFIRadioChannelsInUse,
       "clabWIFIRadioChannel": clabWIFIRadioChannel,
       "clabWIFIRadioAutoChannelSupported": clabWIFIRadioAutoChannelSupported,
       "clabWIFIRadioAutoChannelEnable": clabWIFIRadioAutoChannelEnable,
       "clabWIFIRadioAutoChannelRefreshPeriod": clabWIFIRadioAutoChannelRefreshPeriod,
       "clabWIFIRadioOperatingChannelBandwidth": clabWIFIRadioOperatingChannelBandwidth,
       "clabWIFIRadioExtensionChannel": clabWIFIRadioExtensionChannel,
       "clabWIFIRadioGuardInterval": clabWIFIRadioGuardInterval,
       "clabWIFIRadioMCS": clabWIFIRadioMCS,
       "clabWIFIRadioTransmitPowerSupported": clabWIFIRadioTransmitPowerSupported,
       "clabWIFIRadioTransmitPower": clabWIFIRadioTransmitPower,
       "clabWIFIRadioIEEE80211hSupported": clabWIFIRadioIEEE80211hSupported,
       "clabWIFIRadioIEEE80211hEnabled": clabWIFIRadioIEEE80211hEnabled,
       "clabWIFIRadioRegulatoryDomain": clabWIFIRadioRegulatoryDomain,
       "clabWIFIRadioNonContiguousChannel": clabWIFIRadioNonContiguousChannel,
       "clabWIFIRadioCarrierSenseThresholdInUse": clabWIFIRadioCarrierSenseThresholdInUse,
       "clabWIFIRadioCarrierSenseThresholdRange": clabWIFIRadioCarrierSenseThresholdRange,
       "clabWIFIRadioStatsChanUtilization": clabWIFIRadioStatsChanUtilization,
       "clabWIFIRadioRtsCtsExchange": clabWIFIRadioRtsCtsExchange,
       "clabWIFIRadioFrameAggregationLevel": clabWIFIRadioFrameAggregationLevel,
       "clabWIFIRadioThroughput": clabWIFIRadioThroughput,
       "clabWIFIRadioPktErrorRateSTA": clabWIFIRadioPktErrorRateSTA,
       "clabWIFIRadioRetryLimit": clabWIFIRadioRetryLimit,
       "clabWIFIRadioCCARequest": clabWIFIRadioCCARequest,
       "clabWIFIRadioRPIHistogramRequest": clabWIFIRadioRPIHistogramRequest,
       "clabWIFIRadioFragmentationThreshold": clabWIFIRadioFragmentationThreshold,
       "clabWIFIRadioRTSThreshold": clabWIFIRadioRTSThreshold,
       "clabWIFIRadioLongRetryLimit": clabWIFIRadioLongRetryLimit,
       "clabWIFIRadioBeaconPeriod": clabWIFIRadioBeaconPeriod,
       "clabWIFIRadioDTIMPeriod": clabWIFIRadioDTIMPeriod,
       "clabWIFIRadioPacketAggregationEnable": clabWIFIRadioPacketAggregationEnable,
       "clabWIFIRadioBasicDataTransmitRates": clabWIFIRadioBasicDataTransmitRates,
       "clabWIFIRadioOperationalDataTransmitRates": clabWIFIRadioOperationalDataTransmitRates,
       "clabWIFIRadioSupportedDataTransmitRates": clabWIFIRadioSupportedDataTransmitRates,
       "clabWIFIRadioCarrierSenseThresholdRangeMin": clabWIFIRadioCarrierSenseThresholdRangeMin,
       "clabWIFIRadioCarrierSenseThresholdRangeMax": clabWIFIRadioCarrierSenseThresholdRangeMax,
       "clabWIFIRadioCCAReport": clabWIFIRadioCCAReport,
       "clabWIFIRadioRPIHistogramReport": clabWIFIRadioRPIHistogramReport,
       "clabWIFIRadioPreambleType": clabWIFIRadioPreambleType,
       "clabWIFIRadioStatsTable": clabWIFIRadioStatsTable,
       "clabWIFIRadioStatsEntry": clabWIFIRadioStatsEntry,
       "clabWIFIRadioStatsBytesSent": clabWIFIRadioStatsBytesSent,
       "clabWIFIRadioStatsBytesReceived": clabWIFIRadioStatsBytesReceived,
       "clabWIFIRadioStatsPacketsSent": clabWIFIRadioStatsPacketsSent,
       "clabWIFIRadioStatsPacketsReceived": clabWIFIRadioStatsPacketsReceived,
       "clabWIFIRadioStatsErrorsSent": clabWIFIRadioStatsErrorsSent,
       "clabWIFIRadioStatsErrorsReceived": clabWIFIRadioStatsErrorsReceived,
       "clabWIFIRadioStatsDiscardPacketsSent": clabWIFIRadioStatsDiscardPacketsSent,
       "clabWIFIRadioStatsDiscardPacketsReceived": clabWIFIRadioStatsDiscardPacketsReceived,
       "clabWIFIRadioStatsPLCPErrorCount": clabWIFIRadioStatsPLCPErrorCount,
       "clabWIFIRadioStatsFCSErrorCount": clabWIFIRadioStatsFCSErrorCount,
       "clabWIFIRadioStatsInvalidMACCount": clabWIFIRadioStatsInvalidMACCount,
       "clabWIFIRadioStatsPacketsOtherReceived": clabWIFIRadioStatsPacketsOtherReceived,
       "clabWIFIRadioStatsNoise": clabWIFIRadioStatsNoise,
       "clabWIFIRadioStatsFramesRetransmissionsSent": clabWIFIRadioStatsFramesRetransmissionsSent,
       "clabWIFIRadioStatsFramesDuplicatedReceived": clabWIFIRadioStatsFramesDuplicatedReceived,
       "clabWIFIRadioStatsChannelUtilization": clabWIFIRadioStatsChannelUtilization,
       "clabWIFISSIDTable": clabWIFISSIDTable,
       "clabWIFISSIDEntry": clabWIFISSIDEntry,
       "clabWIFISSIDId": clabWIFISSIDId,
       "clabWIFISSIDEnable": clabWIFISSIDEnable,
       "clabWIFISSIDStatus": clabWIFISSIDStatus,
       "clabWIFISSIDAlias": clabWIFISSIDAlias,
       "clabWIFISSIDName": clabWIFISSIDName,
       "clabWIFISSIDLastChange": clabWIFISSIDLastChange,
       "clabWIFISSIDLowerLayers": clabWIFISSIDLowerLayers,
       "clabWIFISSIDBSSID": clabWIFISSIDBSSID,
       "clabWIFISSIDMACAddress": clabWIFISSIDMACAddress,
       "clabWIFISSIDSSID": clabWIFISSIDSSID,
       "clabWIFISSIDRowStatus": clabWIFISSIDRowStatus,
       "clabWIFISSIDFragmentationEnable": clabWIFISSIDFragmentationEnable,
       "clabWIFISSIDPeriodicStatsNumberOfEntries": clabWIFISSIDPeriodicStatsNumberOfEntries,
       "clabWIFISSIDStatsTable": clabWIFISSIDStatsTable,
       "clabWIFISSIDStatsEntry": clabWIFISSIDStatsEntry,
       "clabWIFISSIDStatsBytesSent": clabWIFISSIDStatsBytesSent,
       "clabWIFISSIDStatsBytesReceived": clabWIFISSIDStatsBytesReceived,
       "clabWIFISSIDStatsPacketsSent": clabWIFISSIDStatsPacketsSent,
       "clabWIFISSIDStatsPacketsReceived": clabWIFISSIDStatsPacketsReceived,
       "clabWIFISSIDStatsErrorsSent": clabWIFISSIDStatsErrorsSent,
       "clabWIFISSIDStatsErrorsReceived": clabWIFISSIDStatsErrorsReceived,
       "clabWIFISSIDStatsUnicastPacketsSent": clabWIFISSIDStatsUnicastPacketsSent,
       "clabWIFISSIDStatsUnicastPacketsReceived": clabWIFISSIDStatsUnicastPacketsReceived,
       "clabWIFISSIDStatsDiscardPacketsSent": clabWIFISSIDStatsDiscardPacketsSent,
       "clabWIFISSIDStatsDiscardPacketsReceived": clabWIFISSIDStatsDiscardPacketsReceived,
       "clabWIFISSIDStatsMulticastPacketsSent": clabWIFISSIDStatsMulticastPacketsSent,
       "clabWIFISSIDStatsMulticastPacketsReceived": clabWIFISSIDStatsMulticastPacketsReceived,
       "clabWIFISSIDStatsBroadcastPacketsSent": clabWIFISSIDStatsBroadcastPacketsSent,
       "clabWIFISSIDStatsBroadcastPacketsReceived": clabWIFISSIDStatsBroadcastPacketsReceived,
       "clabWIFISSIDStatsUnknownProtoPacketsReceived": clabWIFISSIDStatsUnknownProtoPacketsReceived,
       "clabWIFISSIDStatsRetransCount": clabWIFISSIDStatsRetransCount,
       "clabWIFISSIDStatsRetryCount": clabWIFISSIDStatsRetryCount,
       "clabWIFISSIDStatsMultipleRetryCount": clabWIFISSIDStatsMultipleRetryCount,
       "clabWIFISSIDStatsACKFailureCount": clabWIFISSIDStatsACKFailureCount,
       "clabWIFISSIDStatsAggregatedPacketCount": clabWIFISSIDStatsAggregatedPacketCount,
       "clabWIFIAccessPointTable": clabWIFIAccessPointTable,
       "clabWIFIAccessPointEntry": clabWIFIAccessPointEntry,
       "clabWIFIAccessPointId": clabWIFIAccessPointId,
       "clabWIFIAccessPointEnable": clabWIFIAccessPointEnable,
       "clabWIFIAccessPointStatus": clabWIFIAccessPointStatus,
       "clabWIFIAccessPointAlias": clabWIFIAccessPointAlias,
       "clabWIFIAccessPointSSIDReference": clabWIFIAccessPointSSIDReference,
       "clabWIFIAccessPointSSIDAdvertisementEnabled": clabWIFIAccessPointSSIDAdvertisementEnabled,
       "clabWIFIAccessPointRetryLimit": clabWIFIAccessPointRetryLimit,
       "clabWIFIAccessPointWMMCapability": clabWIFIAccessPointWMMCapability,
       "clabWIFIAccessPointUAPSDCapability": clabWIFIAccessPointUAPSDCapability,
       "clabWIFIAccessPointWMMEnable": clabWIFIAccessPointWMMEnable,
       "clabWIFIAccessPointUAPSDEnable": clabWIFIAccessPointUAPSDEnable,
       "clabWIFIAccessPointAssociatedDeviceNumberOfEntries": clabWIFIAccessPointAssociatedDeviceNumberOfEntries,
       "clabWIFIAccessPointRowStatus": clabWIFIAccessPointRowStatus,
       "clabWIFIAccessPointPublicAccessMode": clabWIFIAccessPointPublicAccessMode,
       "clabWIFIAccessPointIsolationEnable": clabWIFIAccessPointIsolationEnable,
       "clabWIFIAccessPointMaxAssociatedDevices": clabWIFIAccessPointMaxAssociatedDevices,
       "clabWIFIAccessPointPasspointSupported": clabWIFIAccessPointPasspointSupported,
       "clabWIFIAccessPointPasspointEnabled": clabWIFIAccessPointPasspointEnabled,
       "clabWIFIAccessPointInterworkingCapability": clabWIFIAccessPointInterworkingCapability,
       "clabWIFIAccessPointInterworkingServiceEnabled": clabWIFIAccessPointInterworkingServiceEnabled,
       "clabWIFIAccessPointAccessControlFilterEnable": clabWIFIAccessPointAccessControlFilterEnable,
       "clabWIFIAccessPointMACAddressControlEnable": clabWIFIAccessPointMACAddressControlEnable,
       "clabWIFIAccessPointAllowedMACAddress": clabWIFIAccessPointAllowedMACAddress,
       "clabWIFIAccessPointClientSessionNumberOfEntries": clabWIFIAccessPointClientSessionNumberOfEntries,
       "clabWIFIAccessPointAssociatedDeviceCount": clabWIFIAccessPointAssociatedDeviceCount,
       "clabWIFIAccessPointSecurityTable": clabWIFIAccessPointSecurityTable,
       "clabWIFIAccessPointSecurityEntry": clabWIFIAccessPointSecurityEntry,
       "clabWIFIAccessPointSecurityModesSupported": clabWIFIAccessPointSecurityModesSupported,
       "clabWIFIAccessPointSecurityModeEnabled": clabWIFIAccessPointSecurityModeEnabled,
       "clabWIFIAccessPointSecurityWEPKey": clabWIFIAccessPointSecurityWEPKey,
       "clabWIFIAccessPointSecurityPreSharedKey": clabWIFIAccessPointSecurityPreSharedKey,
       "clabWIFIAccessPointSecurityKeyPassphrase": clabWIFIAccessPointSecurityKeyPassphrase,
       "clabWIFIAccessPointSecurityRekeyingInterval": clabWIFIAccessPointSecurityRekeyingInterval,
       "clabWIFIAccessPointSecurityRadiusServerIPAddrType": clabWIFIAccessPointSecurityRadiusServerIPAddrType,
       "clabWIFIAccessPointSecurityRadiusServerIPAddr": clabWIFIAccessPointSecurityRadiusServerIPAddr,
       "clabWIFIAccessPointSecurityRadiusServerPort": clabWIFIAccessPointSecurityRadiusServerPort,
       "clabWIFIAccessPointSecurityRadiusSecret": clabWIFIAccessPointSecurityRadiusSecret,
       "clabWIFIAccessPointSecurityRowstatus": clabWIFIAccessPointSecurityRowstatus,
       "clabWIFIAccessPointSecurityWEPKey2": clabWIFIAccessPointSecurityWEPKey2,
       "clabWIFIAccessPointSecurityWEPKey3": clabWIFIAccessPointSecurityWEPKey3,
       "clabWIFIAccessPointSecurityWEPKey4": clabWIFIAccessPointSecurityWEPKey4,
       "clabWIFIAccessPointSecurityWEPIndex": clabWIFIAccessPointSecurityWEPIndex,
       "clabWIFIAccessPointSecurityWEPPassPhrase": clabWIFIAccessPointSecurityWEPPassPhrase,
       "clabWIFIAccessPointSecurityWPAEncryption": clabWIFIAccessPointSecurityWPAEncryption,
       "clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddrType": clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddrType,
       "clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddr": clabWIFIAccessPointSecuritySecondaryRadiusServerIPAddr,
       "clabWIFIAccessPointSecuritySecondaryRadiusServerPort": clabWIFIAccessPointSecuritySecondaryRadiusServerPort,
       "clabWIFIAccessPointSecuritySecondaryRadiusSecret": clabWIFIAccessPointSecuritySecondaryRadiusSecret,
       "clabWIFIAccessPointSecurityEnableManagementFrameProtection": clabWIFIAccessPointSecurityEnableManagementFrameProtection,
       "clabWIFIAccessPointSecurityReset": clabWIFIAccessPointSecurityReset,
       "clabWIFIAccessPointRadiusRetries": clabWIFIAccessPointRadiusRetries,
       "clabWIFIAccessPointSecurityLanRoutingEnabled": clabWIFIAccessPointSecurityLanRoutingEnabled,
       "clabWIFIAccessPointWPSTable": clabWIFIAccessPointWPSTable,
       "clabWIFIAccessPointWPSEntry": clabWIFIAccessPointWPSEntry,
       "clabWIFIAccessPointWPSEnable": clabWIFIAccessPointWPSEnable,
       "clabWIFIAccessPointWPSConfigMethodsSupported": clabWIFIAccessPointWPSConfigMethodsSupported,
       "clabWIFIAccessPointWPSConfigMethodsEnabled": clabWIFIAccessPointWPSConfigMethodsEnabled,
       "clabWIFIAccessPointWPSRowStatus": clabWIFIAccessPointWPSRowStatus,
       "clabWIFIAccessPointWPSSetWPSMethod": clabWIFIAccessPointWPSSetWPSMethod,
       "clabWIFIAccessPointWPSAPPin": clabWIFIAccessPointWPSAPPin,
       "clabWIFIAccessPointWPSSetWPSClientPin": clabWIFIAccessPointWPSSetWPSClientPin,
       "clabWIFIAccessPointWPSConfigMethodsEnable": clabWIFIAccessPointWPSConfigMethodsEnable,
       "clabWIFIAccessPointWPSSetWPSMethods": clabWIFIAccessPointWPSSetWPSMethods,
       "clabWIFIAssociatedDeviceTable": clabWIFIAssociatedDeviceTable,
       "clabWIFIAssociatedDeviceEntry": clabWIFIAssociatedDeviceEntry,
       "clabWIFIAssociatedDeviceId": clabWIFIAssociatedDeviceId,
       "clabWIFIAssociatedDeviceMACAddress": clabWIFIAssociatedDeviceMACAddress,
       "clabWIFIAssociatedDeviceAuthenticationState": clabWIFIAssociatedDeviceAuthenticationState,
       "clabWIFIAssociatedDeviceLastDataDownlinkRate": clabWIFIAssociatedDeviceLastDataDownlinkRate,
       "clabWIFIAssociatedDeviceLastDataUplinkRate": clabWIFIAssociatedDeviceLastDataUplinkRate,
       "clabWIFIAssociatedDeviceSignalStrength": clabWIFIAssociatedDeviceSignalStrength,
       "clabWIFIAssociatedDeviceRetransmissions": clabWIFIAssociatedDeviceRetransmissions,
       "clabWIFIAssociatedDeviceActive": clabWIFIAssociatedDeviceActive,
       "clabWIFIAssociatedDeviceMaxPacketRetryCount": clabWIFIAssociatedDeviceMaxPacketRetryCount,
       "clabWIFIAssociatedDeviceStationCount": clabWIFIAssociatedDeviceStationCount,
       "clabWIFIAssociatedDeviceMaxNumOfStations": clabWIFIAssociatedDeviceMaxNumOfStations,
       "clabWIFIAssociatedDeviceSecurityMode": clabWIFIAssociatedDeviceSecurityMode,
       "clabWIFIAssociatedDeviceEncryptionAlgorithm": clabWIFIAssociatedDeviceEncryptionAlgorithm,
       "clabWIFIAssociatedDeviceAssociationState": clabWIFIAssociatedDeviceAssociationState,
       "clabWIFIDataRateStatsTable": clabWIFIDataRateStatsTable,
       "clabWIFIDataRateStatsEntry": clabWIFIDataRateStatsEntry,
       "clabWIFIDataRateStatsRate": clabWIFIDataRateStatsRate,
       "clabWIFIDataRateStatsFramesSent": clabWIFIDataRateStatsFramesSent,
       "clabWIFIDataRateStatsFramesRetransmissionsSent": clabWIFIDataRateStatsFramesRetransmissionsSent,
       "clabWIFIDataRateStatsFramesReceived": clabWIFIDataRateStatsFramesReceived,
       "clabWIFIDataRateStatsFramesDuplicatedReceived": clabWIFIDataRateStatsFramesDuplicatedReceived,
       "clabWIFIPeriodicStatsTable": clabWIFIPeriodicStatsTable,
       "clabWIFIPeriodicStatsEntry": clabWIFIPeriodicStatsEntry,
       "clabWIFIPeriodicStatsInterval": clabWIFIPeriodicStatsInterval,
       "clabWIFIPeriodicStatsId": clabWIFIPeriodicStatsId,
       "clabWIFIPeriodicStatsDeviceMACAddress": clabWIFIPeriodicStatsDeviceMACAddress,
       "clabWIFIPeriodicStatsFramesSent": clabWIFIPeriodicStatsFramesSent,
       "clabWIFIPeriodicStatsDataFramesSentAck": clabWIFIPeriodicStatsDataFramesSentAck,
       "clabWIFIPeriodicStatsDataFramesSentNoAck": clabWIFIPeriodicStatsDataFramesSentNoAck,
       "clabWIFIPeriodicStatsDataFramesLost": clabWIFIPeriodicStatsDataFramesLost,
       "clabWIFIPeriodicStatsFramesReceived": clabWIFIPeriodicStatsFramesReceived,
       "clabWIFIPeriodicStatsDataFramesReceived": clabWIFIPeriodicStatsDataFramesReceived,
       "clabWIFIPeriodicStatsDataFramesDuplicateReceived": clabWIFIPeriodicStatsDataFramesDuplicateReceived,
       "clabWIFIPeriodicStatsProbesReceived": clabWIFIPeriodicStatsProbesReceived,
       "clabWIFIPeriodicStatsProbesRejected": clabWIFIPeriodicStatsProbesRejected,
       "clabWIFIPeriodicStatsRSSI": clabWIFIPeriodicStatsRSSI,
       "clabWIFIPeriodicStatsSNR": clabWIFIPeriodicStatsSNR,
       "clabWIFIPeriodicStatsDisassociations": clabWIFIPeriodicStatsDisassociations,
       "clabWIFIPeriodicStatsAuthenticationFailures": clabWIFIPeriodicStatsAuthenticationFailures,
       "clabWIFIPeriodicStatsLastTimeAssociation": clabWIFIPeriodicStatsLastTimeAssociation,
       "clabWIFIPeriodicStatsLastTimeDisassociation": clabWIFIPeriodicStatsLastTimeDisassociation,
       "clabWIFISSIDPolicyTable": clabWIFISSIDPolicyTable,
       "clabWIFISSIDPolicyEntry": clabWIFISSIDPolicyEntry,
       "clabWIFISSIDPolicyBlockAfterAttempts": clabWIFISSIDPolicyBlockAfterAttempts,
       "clabWIFISSIDPolicyAllocatedBandwidth": clabWIFISSIDPolicyAllocatedBandwidth,
       "clabWIFISSIDPolicyAuthenticationFailures": clabWIFISSIDPolicyAuthenticationFailures,
       "clabWIFISSIDPolicyNonAuthenticatedTraffic": clabWIFISSIDPolicyNonAuthenticatedTraffic,
       "clabWIFISSIDPolicyAssociationFailures": clabWIFISSIDPolicyAssociationFailures,
       "clabWIFISSIDPolicyStatsInterval": clabWIFISSIDPolicyStatsInterval,
       "clabWIFISSIDPolicySNRThreshold": clabWIFISSIDPolicySNRThreshold,
       "clabWIFISSIDPolicyANPIThreshold": clabWIFISSIDPolicyANPIThreshold,
       "clabWIFISSIDPolicyLowReceivedPowerThreshold": clabWIFISSIDPolicyLowReceivedPowerThreshold,
       "clabWIFISSIDPolicyLowPowerDeniedAccessThreshold": clabWIFISSIDPolicyLowPowerDeniedAccessThreshold,
       "clabWIFISSIDPolicyLowPowerDisassociationThreshold": clabWIFISSIDPolicyLowPowerDisassociationThreshold,
       "clabWIFISSIDPolicyRowStatus": clabWIFISSIDPolicyRowStatus,
       "clabWIFISSIDPolicyBeaconMcsLevelInUse": clabWIFISSIDPolicyBeaconMcsLevelInUse,
       "clabWIFISSIDPolicyBeaconMcsLevelsSupported": clabWIFISSIDPolicyBeaconMcsLevelsSupported,
       "clabWIFIClientSessionsTable": clabWIFIClientSessionsTable,
       "clabWIFIClientSessionsEntry": clabWIFIClientSessionsEntry,
       "clabWIFIClientSessionsId": clabWIFIClientSessionsId,
       "clabWIFIClientSessionsDeviceMACAddress": clabWIFIClientSessionsDeviceMACAddress,
       "clabWIFIClientSessionsStart": clabWIFIClientSessionsStart,
       "clabWIFIClientSessionsStop": clabWIFIClientSessionsStop,
       "clabWIFIClientSessionsTerminationCode": clabWIFIClientSessionsTerminationCode,
       "clabWIFIClientSessionsTerminationMeaning": clabWIFIClientSessionsTerminationMeaning,
       "clabWIFIClientStatsTable": clabWIFIClientStatsTable,
       "clabWIFIClientStatsEntry": clabWIFIClientStatsEntry,
       "clabWIFIClientStatsInterval": clabWIFIClientStatsInterval,
       "clabWIFIClientStatsId": clabWIFIClientStatsId,
       "clabWIFIClientStatsDeviceMACAddress": clabWIFIClientStatsDeviceMACAddress,
       "clabWIFIClientStatsFramesSent": clabWIFIClientStatsFramesSent,
       "clabWIFIClientStatsDataFramesSentAck": clabWIFIClientStatsDataFramesSentAck,
       "clabWIFIClientStatsDataFramesSentNoAck": clabWIFIClientStatsDataFramesSentNoAck,
       "clabWIFIClientStatsDataFramesLost": clabWIFIClientStatsDataFramesLost,
       "clabWIFIClientStatsFramesReceived": clabWIFIClientStatsFramesReceived,
       "clabWIFIClientStatsDataFramesReceived": clabWIFIClientStatsDataFramesReceived,
       "clabWIFIClientStatsDataFramesDuplicateReceived": clabWIFIClientStatsDataFramesDuplicateReceived,
       "clabWIFIClientStatsProbesReceived": clabWIFIClientStatsProbesReceived,
       "clabWIFIClientStatsProbesRejected": clabWIFIClientStatsProbesRejected,
       "clabWIFIClientStatsRSSI": clabWIFIClientStatsRSSI,
       "clabWIFIClientStatsSNR": clabWIFIClientStatsSNR,
       "clabWIFIClientStatsDisassociations": clabWIFIClientStatsDisassociations,
       "clabWIFIClientStatsAuthenticationFailures": clabWIFIClientStatsAuthenticationFailures,
       "clabWIFIClientStatsLastTimeAssociation": clabWIFIClientStatsLastTimeAssociation,
       "clabWIFIClientStatsLastTimeDisassociation": clabWIFIClientStatsLastTimeDisassociation,
       "clabWIFIClientStatsThroughput": clabWIFIClientStatsThroughput,
       "clabWIFIClientStatsPktErrorRatePerSTA": clabWIFIClientStatsPktErrorRatePerSTA,
       "clabWIFIRadiusClientTable": clabWIFIRadiusClientTable,
       "clabWIFIRadiusClientEntry": clabWIFIRadiusClientEntry,
       "clabWIFIRadiusClientNASIdentifier": clabWIFIRadiusClientNASIdentifier,
       "clabWIFIRadiusClientLocationPolicy": clabWIFIRadiusClientLocationPolicy,
       "clabWIFIRadiusClientOperatorName": clabWIFIRadiusClientOperatorName,
       "clabWIFIRadiusClientLocationInformation": clabWIFIRadiusClientLocationInformation,
       "clabWIFIRadiusClientLocationData": clabWIFIRadiusClientLocationData,
       "clabWIFIRadiusClientUsageReports": clabWIFIRadiusClientUsageReports,
       "clabWIFIRadiusClientIntervalInterimReport": clabWIFIRadiusClientIntervalInterimReport,
       "clabWIFIRadiusClientAPTransitionReport": clabWIFIRadiusClientAPTransitionReport,
       "clabWIFIRadiusClientGigawordReport": clabWIFIRadiusClientGigawordReport,
       "clabWIFIRadiusClientRowStatus": clabWIFIRadiusClientRowStatus,
       "clabWIFIWIFICommitSettings": clabWIFIWIFICommitSettings,
       "clabWIFIWIFICommitSettingsValue": clabWIFIWIFICommitSettingsValue,
       "clabWIFIApNeighborStatsTable": clabWIFIApNeighborStatsTable,
       "clabWIFIApNeighborStatsEntry": clabWIFIApNeighborStatsEntry,
       "clabWIFIApNeighborStatsSSID": clabWIFIApNeighborStatsSSID,
       "clabWIFIApNeighborStatsCurrentChannel": clabWIFIApNeighborStatsCurrentChannel,
       "clabWIFIApNeighborStatsCurrentBandwidth": clabWIFIApNeighborStatsCurrentBandwidth,
       "clabWIFIApNeighborStatsRSSI": clabWIFIApNeighborStatsRSSI,
       "clabWIFIAccessPointAccessControlFilter": clabWIFIAccessPointAccessControlFilter,
       "clabWIFIAccessPointClearAccessControlFilterTable": clabWIFIAccessPointClearAccessControlFilterTable,
       "clabWIFIAccessPointAccessControlFilterAccessAllow": clabWIFIAccessPointAccessControlFilterAccessAllow,
       "clabWIFIAccessPointAccessControlFilterTable": clabWIFIAccessPointAccessControlFilterTable,
       "clabWIFIAccessPointAccessControlFilterEntry": clabWIFIAccessPointAccessControlFilterEntry,
       "clabWIFIAccessPointAccessControlFilterIndex": clabWIFIAccessPointAccessControlFilterIndex,
       "clabWIFIAccessPointAccessControlFilterMACAddress": clabWIFIAccessPointAccessControlFilterMACAddress,
       "clabWIFIAccessPointAccessControlFilterNumberOfEntries": clabWIFIAccessPointAccessControlFilterNumberOfEntries,
       "clabWIFIAccessPointPasspoint": clabWIFIAccessPointPasspoint,
       "clabWIFIAccessPointInterworkingServiceTable": clabWIFIAccessPointInterworkingServiceTable,
       "clabWIFIAccessPointInterworkingServiceEntry": clabWIFIAccessPointInterworkingServiceEntry,
       "clabWIFIAccessPointInterworkingServiceInternet": clabWIFIAccessPointInterworkingServiceInternet,
       "clabWIFIAccessPointInterworkingServiceHESSID": clabWIFIAccessPointInterworkingServiceHESSID,
       "clabWIFIAccessPointInterworkingServiceAccessNetworkType": clabWIFIAccessPointInterworkingServiceAccessNetworkType,
       "clabWIFIAccessPointInterworkingServiceVenueGroupCode": clabWIFIAccessPointInterworkingServiceVenueGroupCode,
       "clabWIFIAccessPointInterworkingServiceVenueTypeCode": clabWIFIAccessPointInterworkingServiceVenueTypeCode,
       "clabWIFIAccessPointPasspointTable": clabWIFIAccessPointPasspointTable,
       "clabWIFIAccessPointPasspointEntry": clabWIFIAccessPointPasspointEntry,
       "clabWIFIAccessPointPasspointCapabilityList": clabWIFIAccessPointPasspointCapabilityList,
       "clabWIFIAccessPointPasspointOnlineSignupSupported": clabWIFIAccessPointPasspointOnlineSignupSupported,
       "clabWIFIAccessPointPasspointDGAFEnable": clabWIFIAccessPointPasspointDGAFEnable,
       "clabWIFIAccessPointPasspointP2PEnable": clabWIFIAccessPointPasspointP2PEnable,
       "clabWIFIAccessPointPasspointQoSMappingEnable": clabWIFIAccessPointPasspointQoSMappingEnable,
       "clabWIFIAccessPointPasspointASRAEnable": clabWIFIAccessPointPasspointASRAEnable,
       "clabWIFIAccessPointPasspointANQPDomainID": clabWIFIAccessPointPasspointANQPDomainID,
       "clabWIFIAccessPointPasspointEAPMethod": clabWIFIAccessPointPasspointEAPMethod,
       "clabWIFIAccessPointPasspointManagementFrameProtectionEnable": clabWIFIAccessPointPasspointManagementFrameProtectionEnable,
       "clabWIFIAccessPointPasspointCapabilities": clabWIFIAccessPointPasspointCapabilities,
       "clabWIFIAccessPointPasspointVenueNamesTable": clabWIFIAccessPointPasspointVenueNamesTable,
       "clabWIFIAccessPointPasspointVenueNamesEntry": clabWIFIAccessPointPasspointVenueNamesEntry,
       "clabWIFIAccessPointPasspointVenueNameIndex": clabWIFIAccessPointPasspointVenueNameIndex,
       "clabWIFIAccessPointPasspointVenueNameCountryCode": clabWIFIAccessPointPasspointVenueNameCountryCode,
       "clabWIFIAccessPointPasspointVenueName": clabWIFIAccessPointPasspointVenueName,
       "clabWIFIAccessPointPasspointOperatorNamesTable": clabWIFIAccessPointPasspointOperatorNamesTable,
       "clabWIFIAccessPointPasspointOperatorNamesEntry": clabWIFIAccessPointPasspointOperatorNamesEntry,
       "clabWIFIAccessPointPasspointOperatorNameIndex": clabWIFIAccessPointPasspointOperatorNameIndex,
       "clabWIFIAccessPointPasspointOperatorNameCountryCode": clabWIFIAccessPointPasspointOperatorNameCountryCode,
       "clabWIFIAccessPointPasspointOperatorName": clabWIFIAccessPointPasspointOperatorName,
       "clabWIFIAccessPointPasspointConsortiumTable": clabWIFIAccessPointPasspointConsortiumTable,
       "clabWIFIAccessPointPasspointConsortiumEntry": clabWIFIAccessPointPasspointConsortiumEntry,
       "clabWIFIAccessPointPasspointConsortiumIndex": clabWIFIAccessPointPasspointConsortiumIndex,
       "clabWIFIAccessPointPasspointConsortiumOI": clabWIFIAccessPointPasspointConsortiumOI,
       "clabWIFIAccessPointPasspointDomainNamesTable": clabWIFIAccessPointPasspointDomainNamesTable,
       "clabWIFIAccessPointPasspointDomainNamesEntry": clabWIFIAccessPointPasspointDomainNamesEntry,
       "clabWIFIAccessPointPasspointDomainNamesIndex": clabWIFIAccessPointPasspointDomainNamesIndex,
       "clabWIFIAccessPointPasspointDomainNamesDomainName": clabWIFIAccessPointPasspointDomainNamesDomainName,
       "clabWIFIAccessPointPasspointThreeGPPNetworkTable": clabWIFIAccessPointPasspointThreeGPPNetworkTable,
       "clabWIFIAccessPointPasspointThreeGPPNetworkEntry": clabWIFIAccessPointPasspointThreeGPPNetworkEntry,
       "clabWIFIAccessPointPasspointThreeGPPNetworkIndex": clabWIFIAccessPointPasspointThreeGPPNetworkIndex,
       "clabWIFIAccessPointPasspointThreeGPPNetworkMNC": clabWIFIAccessPointPasspointThreeGPPNetworkMNC,
       "clabWIFIAccessPointPasspointThreeGPPNetworkMCC": clabWIFIAccessPointPasspointThreeGPPNetworkMCC,
       "clabWIFIAccessPointPasspointNAIRealmsTable": clabWIFIAccessPointPasspointNAIRealmsTable,
       "clabWIFIAccessPointPasspointNAIRealmsEntry": clabWIFIAccessPointPasspointNAIRealmsEntry,
       "clabWIFIAccessPointPasspointNAIRealmsIndex": clabWIFIAccessPointPasspointNAIRealmsIndex,
       "clabWIFIAccessPointPasspointNAIRealmsEapMethodsIndex": clabWIFIAccessPointPasspointNAIRealmsEapMethodsIndex,
       "clabWIFIAccessPointPasspointNAIRealmsEapMethodsAuthParmIndex": clabWIFIAccessPointPasspointNAIRealmsEapMethodsAuthParmIndex,
       "clabWIFIAccessPointPasspointNAIRealmsEncodingType": clabWIFIAccessPointPasspointNAIRealmsEncodingType,
       "clabWIFIAccessPointPasspointNAIRealms": clabWIFIAccessPointPasspointNAIRealms,
       "clabWIFIAccessPointPasspointNAIRealmsEapMethod": clabWIFIAccessPointPasspointNAIRealmsEapMethod,
       "clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersID": clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersID,
       "clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersValue": clabWIFIAccessPointPasspointNAIRealmsEapAuthParametersValue,
       "clabWIFIAccessPointPasspointOSUTable": clabWIFIAccessPointPasspointOSUTable,
       "clabWIFIAccessPointPasspointOSUEntry": clabWIFIAccessPointPasspointOSUEntry,
       "clabWIFIAccessPointPasspointOSUProviderIndex": clabWIFIAccessPointPasspointOSUProviderIndex,
       "clabWIFIAccessPointPasspointOSUProviderNamesIndex": clabWIFIAccessPointPasspointOSUProviderNamesIndex,
       "clabWIFIAccessPointPasspointOSUProviderIconsIndex": clabWIFIAccessPointPasspointOSUProviderIconsIndex,
       "clabWIFIAccessPointPasspointOSUProviderServiceDescIndex": clabWIFIAccessPointPasspointOSUProviderServiceDescIndex,
       "clabWIFIAccessPointPasspointOSUProviderServerURI": clabWIFIAccessPointPasspointOSUProviderServerURI,
       "clabWIFIAccessPointPasspointOSUProviderNAI": clabWIFIAccessPointPasspointOSUProviderNAI,
       "clabWIFIAccessPointPasspointOSUProviderNamesLanguageCode": clabWIFIAccessPointPasspointOSUProviderNamesLanguageCode,
       "clabWIFIAccessPointPasspointOSUProviderNamesFriendlyName": clabWIFIAccessPointPasspointOSUProviderNamesFriendlyName,
       "clabWIFIAccessPointPasspointOSUProviderIconFileName": clabWIFIAccessPointPasspointOSUProviderIconFileName,
       "clabWIFIAccessPointPasspointOSUProviderIconType": clabWIFIAccessPointPasspointOSUProviderIconType,
       "clabWIFIAccessPointPasspointOSUProviderIconWidth": clabWIFIAccessPointPasspointOSUProviderIconWidth,
       "clabWIFIAccessPointPasspointOSUProviderIconHeight": clabWIFIAccessPointPasspointOSUProviderIconHeight,
       "clabWIFIAccessPointPasspointOSUProviderIconLanguageCode": clabWIFIAccessPointPasspointOSUProviderIconLanguageCode,
       "clabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode": clabWIFIAccessPointPasspointOSUProviderServiceDescLanguageCode,
       "clabWIFIAccessPointPasspointOSUProviderServiceDescription": clabWIFIAccessPointPasspointOSUProviderServiceDescription,
       "clabWIFIAccessPointPasspointOSUProviderMethodsList": clabWIFIAccessPointPasspointOSUProviderMethodsList,
       "clabWIFIAccessPointPasspoint2VenueNamesTable": clabWIFIAccessPointPasspoint2VenueNamesTable,
       "clabWIFIAccessPointPasspoint2VenueNamesEntry": clabWIFIAccessPointPasspoint2VenueNamesEntry,
       "clabWIFIAccessPointPasspoint2VenueNameIndex": clabWIFIAccessPointPasspoint2VenueNameIndex,
       "clabWIFIAccessPointPasspoint2VenueNameCountryCode": clabWIFIAccessPointPasspoint2VenueNameCountryCode,
       "clabWIFIAccessPointPasspoint2VenueName": clabWIFIAccessPointPasspoint2VenueName,
       "clabWIFIAccessPointPasspoint2NAIRealmsTable": clabWIFIAccessPointPasspoint2NAIRealmsTable,
       "clabWIFIAccessPointPasspoint2NAIRealmsEntry": clabWIFIAccessPointPasspoint2NAIRealmsEntry,
       "clabWIFIAccessPointPasspoint2NAIRealmsIndex": clabWIFIAccessPointPasspoint2NAIRealmsIndex,
       "clabWIFIAccessPointPasspoint2NAIRealmsEncodingType": clabWIFIAccessPointPasspoint2NAIRealmsEncodingType,
       "clabWIFIAccessPointPasspoint2NAIRealms": clabWIFIAccessPointPasspoint2NAIRealms,
       "clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsTable": clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsTable,
       "clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsEntry": clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsEntry,
       "clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex": clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsIndex,
       "clabWIFIAccessPointPasspoint2NAIRealmsEapMethod": clabWIFIAccessPointPasspoint2NAIRealmsEapMethod,
       "clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthTable": clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthTable,
       "clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthEntry": clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthEntry,
       "clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthParmIndex": clabWIFIAccessPointPasspoint2NAIRealmsEapMethodsAuthParmIndex,
       "clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersID": clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersID,
       "clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersValue": clabWIFIAccessPointPasspoint2NAIRealmsEapAuthParametersValue,
       "clabWIFIAccessPointPasspoint2OSUTable": clabWIFIAccessPointPasspoint2OSUTable,
       "clabWIFIAccessPointPasspoint2OSUEntry": clabWIFIAccessPointPasspoint2OSUEntry,
       "clabWIFIAccessPointPasspoint2OSUProviderIndex": clabWIFIAccessPointPasspoint2OSUProviderIndex,
       "clabWIFIAccessPointPasspoint2OSUProviderServerURI": clabWIFIAccessPointPasspoint2OSUProviderServerURI,
       "clabWIFIAccessPointPasspoint2OSUProviderNAI": clabWIFIAccessPointPasspoint2OSUProviderNAI,
       "clabWIFIAccessPointPasspoint2OSUProviderMethodsList": clabWIFIAccessPointPasspoint2OSUProviderMethodsList,
       "clabWIFIAccessPointPasspoint2OSUProviderNamesTable": clabWIFIAccessPointPasspoint2OSUProviderNamesTable,
       "clabWIFIAccessPointPasspoint2OSUProviderNamesEntry": clabWIFIAccessPointPasspoint2OSUProviderNamesEntry,
       "clabWIFIAccessPointPasspoint2OSUProviderNamesIndex": clabWIFIAccessPointPasspoint2OSUProviderNamesIndex,
       "clabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode": clabWIFIAccessPointPasspoint2OSUProviderNamesLanguageCode,
       "clabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName": clabWIFIAccessPointPasspoint2OSUProviderNamesFriendlyName,
       "clabWIFIAccessPointPasspoint2OSUProviderIconsTable": clabWIFIAccessPointPasspoint2OSUProviderIconsTable,
       "clabWIFIAccessPointPasspoint2OSUProviderIconsEntry": clabWIFIAccessPointPasspoint2OSUProviderIconsEntry,
       "clabWIFIAccessPointPasspoint2OSUProviderIconsIndex": clabWIFIAccessPointPasspoint2OSUProviderIconsIndex,
       "clabWIFIAccessPointPasspoint2OSUProviderIconFileName": clabWIFIAccessPointPasspoint2OSUProviderIconFileName,
       "clabWIFIAccessPointPasspoint2OSUProviderIconType": clabWIFIAccessPointPasspoint2OSUProviderIconType,
       "clabWIFIAccessPointPasspoint2OSUProviderIconWidth": clabWIFIAccessPointPasspoint2OSUProviderIconWidth,
       "clabWIFIAccessPointPasspoint2OSUProviderIconHeight": clabWIFIAccessPointPasspoint2OSUProviderIconHeight,
       "clabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode": clabWIFIAccessPointPasspoint2OSUProviderIconLanguageCode,
       "clabWIFIAccessPointPasspoint2OSUProviderServiceDescTable": clabWIFIAccessPointPasspoint2OSUProviderServiceDescTable,
       "clabWIFIAccessPointPasspoint2OSUProviderServiceDescEntry": clabWIFIAccessPointPasspoint2OSUProviderServiceDescEntry,
       "clabWIFIAccessPointPasspoint2OSUProviderServiceDescIndex": clabWIFIAccessPointPasspoint2OSUProviderServiceDescIndex,
       "clabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode": clabWIFIAccessPointPasspoint2OSUProviderServiceDescLanguageCode,
       "clabWIFIAccessPointPasspoint2OSUProviderServiceDescription": clabWIFIAccessPointPasspoint2OSUProviderServiceDescription,
       "clabWIFIAccessPointPasspointWANMetrics": clabWIFIAccessPointPasspointWANMetrics,
       "clabWIFIAccessPointPasspointWANMetricsLinkStatus": clabWIFIAccessPointPasspointWANMetricsLinkStatus,
       "clabWIFIAccessPointPasspointWANMetricsAtCapacity": clabWIFIAccessPointPasspointWANMetricsAtCapacity,
       "clabWIFIAccessPointPasspointWANMetricsDownlinkSpeed": clabWIFIAccessPointPasspointWANMetricsDownlinkSpeed,
       "clabWIFIAccessPointPasspointWANMetricsUplinkSpeed": clabWIFIAccessPointPasspointWANMetricsUplinkSpeed,
       "clabWIFIAccessPointPasspointWANMetricsDownlinkLoad": clabWIFIAccessPointPasspointWANMetricsDownlinkLoad,
       "clabWIFIAccessPointPasspointWANMetricsUplinkLoad": clabWIFIAccessPointPasspointWANMetricsUplinkLoad,
       "clabWIFINeighboringWiFiDiagnostics": clabWIFINeighboringWiFiDiagnostics,
       "clabWIFINeighboringWiFiDiagnosticsMode": clabWIFINeighboringWiFiDiagnosticsMode,
       "clabWIFINeighboringWiFiDiagnosticsInterval": clabWIFINeighboringWiFiDiagnosticsInterval,
       "clabWIFINeighboringWiFiDiagnosticsState": clabWIFINeighboringWiFiDiagnosticsState,
       "clabWIFINeighboringWiFiDiagnosticsTableClear": clabWIFINeighboringWiFiDiagnosticsTableClear,
       "clabWIFINeighboringWiFiDiagnosticsTableMaxNumberOfEntries": clabWIFINeighboringWiFiDiagnosticsTableMaxNumberOfEntries,
       "clabWIFINeighboringWiFiDiagnosticsResultTable": clabWIFINeighboringWiFiDiagnosticsResultTable,
       "clabWIFINeighboringWiFiDiagnosticsResultEntry": clabWIFINeighboringWiFiDiagnosticsResultEntry,
       "clabWIFINeighboringWiFiDiagnosticsResultIndex": clabWIFINeighboringWiFiDiagnosticsResultIndex,
       "clabWIFINeighboringWiFiSSID": clabWIFINeighboringWiFiSSID,
       "clabWIFINeighboringWiFiBSSID": clabWIFINeighboringWiFiBSSID,
       "clabWIFINeighboringWiFiMode": clabWIFINeighboringWiFiMode,
       "clabWIFINeighboringWiFiChannel": clabWIFINeighboringWiFiChannel,
       "clabWIFINeighboringWiFiSignalStrength": clabWIFINeighboringWiFiSignalStrength,
       "clabWIFINeighboringWiFiSecurityModeEnabled": clabWIFINeighboringWiFiSecurityModeEnabled,
       "clabWIFINeighboringWiFiEncryptionMode": clabWIFINeighboringWiFiEncryptionMode,
       "clabWIFINeighboringWiFiOperatingFrequencyBand": clabWIFINeighboringWiFiOperatingFrequencyBand,
       "clabWIFINeighboringWiFiSupportedStandards": clabWIFINeighboringWiFiSupportedStandards,
       "clabWIFINeighboringWiFiOperatingStandards": clabWIFINeighboringWiFiOperatingStandards,
       "clabWIFINeighboringWiFiOperatingChannelBandwidth": clabWIFINeighboringWiFiOperatingChannelBandwidth,
       "clabWIFINeighboringWiFiBeaconPeriod": clabWIFINeighboringWiFiBeaconPeriod,
       "clabWIFINeighboringWiFiNoise": clabWIFINeighboringWiFiNoise,
       "clabWIFINeighboringWiFiBasicDataTransferRates": clabWIFINeighboringWiFiBasicDataTransferRates,
       "clabWIFINeighboringWiFiSupportedDataTransferRates": clabWIFINeighboringWiFiSupportedDataTransferRates,
       "clabWIFINeighboringWiFiDTIMPeriod": clabWIFINeighboringWiFiDTIMPeriod,
       "clabWIFINeighboringWiFiSidebandPosition": clabWIFINeighboringWiFiSidebandPosition,
       "clabWIFINeighboringWiFiDiagnosticsLastRunTimestamp": clabWIFINeighboringWiFiDiagnosticsLastRunTimestamp,
       "clabWIFINeighboringWiFiDiagnosticsNonContiguousChannel": clabWIFINeighboringWiFiDiagnosticsNonContiguousChannel,
       "clabWIFINeighboringWiFiDiagnosticsResultNumberOfEntries": clabWIFINeighboringWiFiDiagnosticsResultNumberOfEntries,
       "clabWIFIRadioChannelWiFiDiagnostics": clabWIFIRadioChannelWiFiDiagnostics,
       "clabWIFIRadioChannelWiFiDiagnosticsState": clabWIFIRadioChannelWiFiDiagnosticsState,
       "clabWIFIRadioChannelWiFiDiagnosticsLastRunTimestamp": clabWIFIRadioChannelWiFiDiagnosticsLastRunTimestamp,
       "clabWIFIRadioChannelWiFiDiagnosticsResultNumberOfEntries": clabWIFIRadioChannelWiFiDiagnosticsResultNumberOfEntries,
       "clabWIFIRadioChannelWiFiDiagnosticsResultsTable": clabWIFIRadioChannelWiFiDiagnosticsResultsTable,
       "clabWIFIRadioChannelWiFiDiagnosticsResultsEntry": clabWIFIRadioChannelWiFiDiagnosticsResultsEntry,
       "clabWIFIRadioChannelWiFiDiagnosticsResultsChannel": clabWIFIRadioChannelWiFiDiagnosticsResultsChannel,
       "clabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth": clabWIFIRadioChannelWiFiDiagnosticsResultsBandwidth,
       "clabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity": clabWIFIRadioChannelWiFiDiagnosticsResultsAvailableCapacity,
       "clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi": clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFi,
       "clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFiClasses": clabWIFIRadioChannelWiFiDiagnosticsResultsNonWiFiClasses,
       "clabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand": clabWIFIRadioChannelWiFiDiagnosticsResultsFrequencyBand,
       "clabWIFIAccessPointAccountingTable": clabWIFIAccessPointAccountingTable,
       "clabWIFIAccessPointAccountingEntry": clabWIFIAccessPointAccountingEntry,
       "clabWIFIAccessPointAccountingEnable": clabWIFIAccessPointAccountingEnable,
       "clabWIFIAccessPointAccountingServerIPAddrType": clabWIFIAccessPointAccountingServerIPAddrType,
       "clabWIFIAccessPointAccountingServerIPAddr": clabWIFIAccessPointAccountingServerIPAddr,
       "clabWIFIAccessPointAccountingSecondaryServerIPAddrType": clabWIFIAccessPointAccountingSecondaryServerIPAddrType,
       "clabWIFIAccessPointAccountingSecondaryServerIPAddr": clabWIFIAccessPointAccountingSecondaryServerIPAddr,
       "clabWIFIAccessPointAccountingServerPort": clabWIFIAccessPointAccountingServerPort,
       "clabWIFIAccessPointAccountingSecondaryServerPort": clabWIFIAccessPointAccountingSecondaryServerPort,
       "clabWIFIAccessPointAccountingSecret": clabWIFIAccessPointAccountingSecret,
       "clabWIFIAccessPointAccountingSecondarySecret": clabWIFIAccessPointAccountingSecondarySecret,
       "clabWIFIAccessPointAccountingInterimInterval": clabWIFIAccessPointAccountingInterimInterval,
       "clabWIFIAccessPointAccountingRowStatus": clabWIFIAccessPointAccountingRowStatus,
       "clabWIFIAccessPointACTable": clabWIFIAccessPointACTable,
       "clabWIFIAccessPointACEntry": clabWIFIAccessPointACEntry,
       "clabWIFIAccessPointACAccessCategory": clabWIFIAccessPointACAccessCategory,
       "clabWIFIAccessPointACAlias": clabWIFIAccessPointACAlias,
       "clabWIFIAccessPointACAIFSN": clabWIFIAccessPointACAIFSN,
       "clabWIFIAccessPointACECWMin": clabWIFIAccessPointACECWMin,
       "clabWIFIAccessPointACECWMax": clabWIFIAccessPointACECWMax,
       "clabWIFIAccessPointACTxOpMax": clabWIFIAccessPointACTxOpMax,
       "clabWIFIAccessPointACAckPolicy": clabWIFIAccessPointACAckPolicy,
       "clabWIFIAccessPointACOutQLenHistogramIntervals": clabWIFIAccessPointACOutQLenHistogramIntervals,
       "clabWIFIAccessPointACOutQLenHistogramSampleInterval": clabWIFIAccessPointACOutQLenHistogramSampleInterval,
       "clabWIFIAccessPointACStatsTable": clabWIFIAccessPointACStatsTable,
       "clabWIFIAccessPointACStatsEntry": clabWIFIAccessPointACStatsEntry,
       "clabWIFIAccessPointACStatsBytesSent": clabWIFIAccessPointACStatsBytesSent,
       "clabWIFIAccessPointACStatsBytesReceived": clabWIFIAccessPointACStatsBytesReceived,
       "clabWIFIAccessPointACStatsPacketsSent": clabWIFIAccessPointACStatsPacketsSent,
       "clabWIFIAccessPointACStatsPacketsReceived": clabWIFIAccessPointACStatsPacketsReceived,
       "clabWIFIAccessPointACStatsErrorsSent": clabWIFIAccessPointACStatsErrorsSent,
       "clabWIFIAccessPointACStatsErrorsReceived": clabWIFIAccessPointACStatsErrorsReceived,
       "clabWIFIAccessPointACStatsDiscardPacketsSent": clabWIFIAccessPointACStatsDiscardPacketsSent,
       "clabWIFIAccessPointACStatsDiscardPacketsReceived": clabWIFIAccessPointACStatsDiscardPacketsReceived,
       "clabWIFIAccessPointACStatsRetransCount": clabWIFIAccessPointACStatsRetransCount,
       "clabWIFIAccessPointACStatsOutQLenHistogram": clabWIFIAccessPointACStatsOutQLenHistogram,
       "clabWIFIAccessPointRadiusSettingsObjects": clabWIFIAccessPointRadiusSettingsObjects,
       "clabWIFIAccessPointRadiusSettingsRadiusServerRetries": clabWIFIAccessPointRadiusSettingsRadiusServerRetries,
       "clabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout": clabWIFIAccessPointRadiusSettingsRadiusServerRequestTimeout,
       "clabWIFIAccessPointRadiusSettingsPMKLifetime": clabWIFIAccessPointRadiusSettingsPMKLifetime,
       "clabWIFIAccessPointRadiusSettingsPMKCachingEnable": clabWIFIAccessPointRadiusSettingsPMKCachingEnable,
       "clabWIFIAccessPointRadiusSettingsPMKCachingInterval": clabWIFIAccessPointRadiusSettingsPMKCachingInterval,
       "clabWIFIAccessPointRadiusSettingsMaxAuthenticationAttempts": clabWIFIAccessPointRadiusSettingsMaxAuthenticationAttempts,
       "clabWIFIAccessPointRadiusSettingsBlacklistTableTimeout": clabWIFIAccessPointRadiusSettingsBlacklistTableTimeout,
       "clabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval": clabWIFIAccessPointRadiusSettingsIdentityRequestRetryInterval,
       "clabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth": clabWIFIAccessPointRadiusSettingsQuietPeriodAfterFailedAuth,
       "clabWIFIAccessPointAC2Table": clabWIFIAccessPointAC2Table,
       "clabWIFIAccessPointAC2Entry": clabWIFIAccessPointAC2Entry,
       "clabWIFIAccessPointAC2Index": clabWIFIAccessPointAC2Index,
       "clabWIFIAccessPointAC2AccessCategory": clabWIFIAccessPointAC2AccessCategory,
       "clabWIFIAccessPointAC2Alias": clabWIFIAccessPointAC2Alias,
       "clabWIFIAccessPointAC2AIFSN": clabWIFIAccessPointAC2AIFSN,
       "clabWIFIAccessPointAC2ECWMin": clabWIFIAccessPointAC2ECWMin,
       "clabWIFIAccessPointAC2ECWMax": clabWIFIAccessPointAC2ECWMax,
       "clabWIFIAccessPointAC2TxOpMax": clabWIFIAccessPointAC2TxOpMax,
       "clabWIFIAccessPointAC2AckPolicy": clabWIFIAccessPointAC2AckPolicy,
       "clabWIFIAccessPointAC2OutQLenHistogramIntervals": clabWIFIAccessPointAC2OutQLenHistogramIntervals,
       "clabWIFIAccessPointAC2OutQLenHistogramSampleInterval": clabWIFIAccessPointAC2OutQLenHistogramSampleInterval,
       "clabWIFIAccessPointAC2StatsTable": clabWIFIAccessPointAC2StatsTable,
       "clabWIFIAccessPointAC2StatsEntry": clabWIFIAccessPointAC2StatsEntry,
       "clabWIFIAccessPointAC2StatsIndex": clabWIFIAccessPointAC2StatsIndex,
       "clabWIFIAccessPointAC2StatsBytesSent": clabWIFIAccessPointAC2StatsBytesSent,
       "clabWIFIAccessPointAC2StatsBytesReceived": clabWIFIAccessPointAC2StatsBytesReceived,
       "clabWIFIAccessPointAC2StatsPacketsSent": clabWIFIAccessPointAC2StatsPacketsSent,
       "clabWIFIAccessPointAC2StatsPacketsReceived": clabWIFIAccessPointAC2StatsPacketsReceived,
       "clabWIFIAccessPointAC2StatsErrorsSent": clabWIFIAccessPointAC2StatsErrorsSent,
       "clabWIFIAccessPointAC2StatsErrorsReceived": clabWIFIAccessPointAC2StatsErrorsReceived,
       "clabWIFIAccessPointAC2StatsDiscardPacketsSent": clabWIFIAccessPointAC2StatsDiscardPacketsSent,
       "clabWIFIAccessPointAC2StatsDiscardPacketsReceived": clabWIFIAccessPointAC2StatsDiscardPacketsReceived,
       "clabWIFIAccessPointAC2StatsRetransCount": clabWIFIAccessPointAC2StatsRetransCount,
       "clabWIFIAccessPointAC2StatsOutQLenHistogram": clabWIFIAccessPointAC2StatsOutQLenHistogram,
       "clabWIFIMibConformance": clabWIFIMibConformance,
       "clabWIFIMibCompliances": clabWIFIMibCompliances,
       "clabWIFICompliance": clabWIFICompliance,
       "clabWIFIMibGroups": clabWIFIMibGroups,
       "clabWIFIGroup": clabWIFIGroup,
       "clabWIFINotificationsGroup": clabWIFINotificationsGroup,
       "clabDeprecatedObjectsGroup": clabDeprecatedObjectsGroup}
)
