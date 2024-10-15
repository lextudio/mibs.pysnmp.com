# SNMP MIB module (H323GW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H323GW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:45 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(MmAliasAddress,
 MmAliasTag,
 MmControlsCommands,
 MmErrorProbableCause,
 MmErrorSeverity,
 MmGlobalIdentifier,
 MmTAddressTag,
 MmTerminalAudioCapability,
 MmTerminalDataCapability,
 MmTerminalVideoCapability,
 mmH323GatewayRoot) = mibBuilder.importSymbols(
    "MULTI-MEDIA-MIB-TC",
    "MmAliasAddress",
    "MmAliasTag",
    "MmControlsCommands",
    "MmErrorProbableCause",
    "MmErrorSeverity",
    "MmGlobalIdentifier",
    "MmTAddressTag",
    "MmTerminalAudioCapability",
    "MmTerminalDataCapability",
    "MmTerminalVideoCapability",
    "mmH323GatewayRoot")

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
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

h323Gw = ModuleIdentity(
    (0, 0, 8, 341, 1, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H323gwSpecificTypes(Integer32, TextualConvention):
    status = "current"
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
        *(("h320", 3),
          ("h323", 2),
          ("other", 1),
          ("pstn", 4))
    )



class H323gwConnectionCommand(Integer32, TextualConvention):
    status = "current"
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
        *(("disconnect", 1),
          ("hold", 2),
          ("resetStats", 4),
          ("resume", 3))
    )



# MIB Managed Objects in the order of their OIDs

_H323GwSystem_ObjectIdentity = ObjectIdentity
h323GwSystem = _H323GwSystem_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 1)
)
_H323GwSystemTable_Object = MibTable
h323GwSystemTable = _H323GwSystemTable_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h323GwSystemTable.setStatus("current")
_H323GwSystemEntry_Object = MibTableRow
h323GwSystemEntry = _H323GwSystemEntry_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1)
)
h323GwSystemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwSystemEntry.setStatus("current")


class _H323GwSystemNameAndMaker_Type(DisplayString):
    """Custom type h323GwSystemNameAndMaker based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H323GwSystemNameAndMaker_Type.__name__ = "DisplayString"
_H323GwSystemNameAndMaker_Object = MibTableColumn
h323GwSystemNameAndMaker = _H323GwSystemNameAndMaker_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1, 1),
    _H323GwSystemNameAndMaker_Type()
)
h323GwSystemNameAndMaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwSystemNameAndMaker.setStatus("current")
_H323GwSystemSoftwareVersionNumber_Type = DisplayString
_H323GwSystemSoftwareVersionNumber_Object = MibTableColumn
h323GwSystemSoftwareVersionNumber = _H323GwSystemSoftwareVersionNumber_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1, 2),
    _H323GwSystemSoftwareVersionNumber_Type()
)
h323GwSystemSoftwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwSystemSoftwareVersionNumber.setStatus("current")
_H323GwSystemHardwareVersionNumber_Type = DisplayString
_H323GwSystemHardwareVersionNumber_Object = MibTableColumn
h323GwSystemHardwareVersionNumber = _H323GwSystemHardwareVersionNumber_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1, 3),
    _H323GwSystemHardwareVersionNumber_Type()
)
h323GwSystemHardwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwSystemHardwareVersionNumber.setStatus("current")


class _H323GwSystemContact_Type(DisplayString):
    """Custom type h323GwSystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H323GwSystemContact_Type.__name__ = "DisplayString"
_H323GwSystemContact_Object = MibTableColumn
h323GwSystemContact = _H323GwSystemContact_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1, 4),
    _H323GwSystemContact_Type()
)
h323GwSystemContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwSystemContact.setStatus("current")


class _H323GwSystemt35CountryCode_Type(Integer32):
    """Custom type h323GwSystemt35CountryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H323GwSystemt35CountryCode_Type.__name__ = "Integer32"
_H323GwSystemt35CountryCode_Object = MibTableColumn
h323GwSystemt35CountryCode = _H323GwSystemt35CountryCode_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1, 5),
    _H323GwSystemt35CountryCode_Type()
)
h323GwSystemt35CountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwSystemt35CountryCode.setStatus("current")


class _H323GwSystemt35CountryCodeExtention_Type(Integer32):
    """Custom type h323GwSystemt35CountryCodeExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H323GwSystemt35CountryCodeExtention_Type.__name__ = "Integer32"
_H323GwSystemt35CountryCodeExtention_Object = MibTableColumn
h323GwSystemt35CountryCodeExtention = _H323GwSystemt35CountryCodeExtention_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1, 6),
    _H323GwSystemt35CountryCodeExtention_Type()
)
h323GwSystemt35CountryCodeExtention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwSystemt35CountryCodeExtention.setStatus("current")


class _H323GwSystemt35ManufacturerCode_Type(Integer32):
    """Custom type h323GwSystemt35ManufacturerCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H323GwSystemt35ManufacturerCode_Type.__name__ = "Integer32"
_H323GwSystemt35ManufacturerCode_Object = MibTableColumn
h323GwSystemt35ManufacturerCode = _H323GwSystemt35ManufacturerCode_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1, 7),
    _H323GwSystemt35ManufacturerCode_Type()
)
h323GwSystemt35ManufacturerCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwSystemt35ManufacturerCode.setStatus("current")


class _H323GwSystemLocation_Type(DisplayString):
    """Custom type h323GwSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H323GwSystemLocation_Type.__name__ = "DisplayString"
_H323GwSystemLocation_Object = MibTableColumn
h323GwSystemLocation = _H323GwSystemLocation_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1, 8),
    _H323GwSystemLocation_Type()
)
h323GwSystemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwSystemLocation.setStatus("current")
_H323GwSystemUptime_Type = TimeTicks
_H323GwSystemUptime_Object = MibTableColumn
h323GwSystemUptime = _H323GwSystemUptime_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1, 9),
    _H323GwSystemUptime_Type()
)
h323GwSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwSystemUptime.setStatus("current")
_H323GwSystemLocalTime_Type = DateAndTime
_H323GwSystemLocalTime_Object = MibTableColumn
h323GwSystemLocalTime = _H323GwSystemLocalTime_Object(
    (0, 0, 8, 341, 1, 4, 1, 1, 1, 1, 10),
    _H323GwSystemLocalTime_Type()
)
h323GwSystemLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwSystemLocalTime.setStatus("current")
_H323GwConfiguration_ObjectIdentity = ObjectIdentity
h323GwConfiguration = _H323GwConfiguration_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 2)
)
_H323GwConfigurationTable_Object = MibTable
h323GwConfigurationTable = _H323GwConfigurationTable_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h323GwConfigurationTable.setStatus("current")
_H323GwConfigurationEntry_Object = MibTableRow
h323GwConfigurationEntry = _H323GwConfigurationEntry_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 1, 1)
)
h323GwConfigurationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwConfigurationEntry.setStatus("current")


class _H323GwConfigurationEnableNotifications_Type(Integer32):
    """Custom type h323GwConfigurationEnableNotifications based on Integer32"""
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


_H323GwConfigurationEnableNotifications_Type.__name__ = "Integer32"
_H323GwConfigurationEnableNotifications_Object = MibTableColumn
h323GwConfigurationEnableNotifications = _H323GwConfigurationEnableNotifications_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 1, 1, 1),
    _H323GwConfigurationEnableNotifications_Type()
)
h323GwConfigurationEnableNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwConfigurationEnableNotifications.setStatus("current")
_H323GwConfigurationLeadingAliasAddressTag_Type = MmAliasTag
_H323GwConfigurationLeadingAliasAddressTag_Object = MibTableColumn
h323GwConfigurationLeadingAliasAddressTag = _H323GwConfigurationLeadingAliasAddressTag_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 1, 1, 2),
    _H323GwConfigurationLeadingAliasAddressTag_Type()
)
h323GwConfigurationLeadingAliasAddressTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwConfigurationLeadingAliasAddressTag.setStatus("current")
_H323GwConfigurationLeadingAliasAddress_Type = MmAliasAddress
_H323GwConfigurationLeadingAliasAddress_Object = MibTableColumn
h323GwConfigurationLeadingAliasAddress = _H323GwConfigurationLeadingAliasAddress_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 1, 1, 3),
    _H323GwConfigurationLeadingAliasAddress_Type()
)
h323GwConfigurationLeadingAliasAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwConfigurationLeadingAliasAddress.setStatus("current")
_H323GwConfigurationH323Table_Object = MibTable
h323GwConfigurationH323Table = _H323GwConfigurationH323Table_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h323GwConfigurationH323Table.setStatus("current")
_H323GwConfigurationH323Entry_Object = MibTableRow
h323GwConfigurationH323Entry = _H323GwConfigurationH323Entry_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 2, 1)
)
h323GwConfigurationH323Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwConfigurationH323Entry.setStatus("current")
_H323GwConfigurationH323CallSignalingAddressTag_Type = MmTAddressTag
_H323GwConfigurationH323CallSignalingAddressTag_Object = MibTableColumn
h323GwConfigurationH323CallSignalingAddressTag = _H323GwConfigurationH323CallSignalingAddressTag_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 2, 1, 1),
    _H323GwConfigurationH323CallSignalingAddressTag_Type()
)
h323GwConfigurationH323CallSignalingAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConfigurationH323CallSignalingAddressTag.setStatus("current")
_H323GwConfigurationH323CallSignalingAddress_Type = TAddress
_H323GwConfigurationH323CallSignalingAddress_Object = MibTableColumn
h323GwConfigurationH323CallSignalingAddress = _H323GwConfigurationH323CallSignalingAddress_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 2, 1, 2),
    _H323GwConfigurationH323CallSignalingAddress_Type()
)
h323GwConfigurationH323CallSignalingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConfigurationH323CallSignalingAddress.setStatus("current")
_H323GwConfigurationH323GatekeeperAddressTag_Type = MmTAddressTag
_H323GwConfigurationH323GatekeeperAddressTag_Object = MibTableColumn
h323GwConfigurationH323GatekeeperAddressTag = _H323GwConfigurationH323GatekeeperAddressTag_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 2, 1, 3),
    _H323GwConfigurationH323GatekeeperAddressTag_Type()
)
h323GwConfigurationH323GatekeeperAddressTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwConfigurationH323GatekeeperAddressTag.setStatus("current")
_H323GwConfigurationH323GatekeeperAddress_Type = TAddress
_H323GwConfigurationH323GatekeeperAddress_Object = MibTableColumn
h323GwConfigurationH323GatekeeperAddress = _H323GwConfigurationH323GatekeeperAddress_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 2, 1, 4),
    _H323GwConfigurationH323GatekeeperAddress_Type()
)
h323GwConfigurationH323GatekeeperAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwConfigurationH323GatekeeperAddress.setStatus("current")
_H323GwConfigurationH320Table_Object = MibTable
h323GwConfigurationH320Table = _H323GwConfigurationH320Table_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h323GwConfigurationH320Table.setStatus("current")
_H323GwConfigurationH320Entry_Object = MibTableRow
h323GwConfigurationH320Entry = _H323GwConfigurationH320Entry_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 3, 1)
)
h323GwConfigurationH320Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwConfigurationH320Entry.setStatus("current")
_H323GwConfigurationH320TotalPorts_Type = Unsigned32
_H323GwConfigurationH320TotalPorts_Object = MibTableColumn
h323GwConfigurationH320TotalPorts = _H323GwConfigurationH320TotalPorts_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 3, 1, 1),
    _H323GwConfigurationH320TotalPorts_Type()
)
h323GwConfigurationH320TotalPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwConfigurationH320TotalPorts.setStatus("current")
_H323GwConfigurationPstnTable_Object = MibTable
h323GwConfigurationPstnTable = _H323GwConfigurationPstnTable_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 4)
)
if mibBuilder.loadTexts:
    h323GwConfigurationPstnTable.setStatus("current")
_H323GwConfigurationPstnEntry_Object = MibTableRow
h323GwConfigurationPstnEntry = _H323GwConfigurationPstnEntry_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 4, 1)
)
h323GwConfigurationPstnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwConfigurationPstnEntry.setStatus("current")
_H323GwConfigurationPstnTotalPorts_Type = Unsigned32
_H323GwConfigurationPstnTotalPorts_Object = MibTableColumn
h323GwConfigurationPstnTotalPorts = _H323GwConfigurationPstnTotalPorts_Object(
    (0, 0, 8, 341, 1, 4, 1, 2, 4, 1, 1),
    _H323GwConfigurationPstnTotalPorts_Type()
)
h323GwConfigurationPstnTotalPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwConfigurationPstnTotalPorts.setStatus("current")
_H323GwCapabilities_ObjectIdentity = ObjectIdentity
h323GwCapabilities = _H323GwCapabilities_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 3)
)
_H323GwCapabilitiesH323Table_Object = MibTable
h323GwCapabilitiesH323Table = _H323GwCapabilitiesH323Table_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h323GwCapabilitiesH323Table.setStatus("current")
_H323GwCapabilitiesH323Entry_Object = MibTableRow
h323GwCapabilitiesH323Entry = _H323GwCapabilitiesH323Entry_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 1, 1)
)
h323GwCapabilitiesH323Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwCapabilitiesH323Entry.setStatus("current")
_H323GwCapabilitiesH323AudioRecv_Type = MmTerminalAudioCapability
_H323GwCapabilitiesH323AudioRecv_Object = MibTableColumn
h323GwCapabilitiesH323AudioRecv = _H323GwCapabilitiesH323AudioRecv_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 1, 1, 1),
    _H323GwCapabilitiesH323AudioRecv_Type()
)
h323GwCapabilitiesH323AudioRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH323AudioRecv.setStatus("current")
_H323GwCapabilitiesH323AudioSend_Type = MmTerminalAudioCapability
_H323GwCapabilitiesH323AudioSend_Object = MibTableColumn
h323GwCapabilitiesH323AudioSend = _H323GwCapabilitiesH323AudioSend_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 1, 1, 2),
    _H323GwCapabilitiesH323AudioSend_Type()
)
h323GwCapabilitiesH323AudioSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH323AudioSend.setStatus("current")
_H323GwCapabilitiesH323VideoRecv_Type = MmTerminalVideoCapability
_H323GwCapabilitiesH323VideoRecv_Object = MibTableColumn
h323GwCapabilitiesH323VideoRecv = _H323GwCapabilitiesH323VideoRecv_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 1, 1, 3),
    _H323GwCapabilitiesH323VideoRecv_Type()
)
h323GwCapabilitiesH323VideoRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH323VideoRecv.setStatus("current")
_H323GwCapabilitiesH323VideoSend_Type = MmTerminalVideoCapability
_H323GwCapabilitiesH323VideoSend_Object = MibTableColumn
h323GwCapabilitiesH323VideoSend = _H323GwCapabilitiesH323VideoSend_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 1, 1, 4),
    _H323GwCapabilitiesH323VideoSend_Type()
)
h323GwCapabilitiesH323VideoSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH323VideoSend.setStatus("current")
_H323GwCapabilitiesH323DataRecv_Type = MmTerminalDataCapability
_H323GwCapabilitiesH323DataRecv_Object = MibTableColumn
h323GwCapabilitiesH323DataRecv = _H323GwCapabilitiesH323DataRecv_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 1, 1, 5),
    _H323GwCapabilitiesH323DataRecv_Type()
)
h323GwCapabilitiesH323DataRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH323DataRecv.setStatus("current")
_H323GwCapabilitiesH323DataSend_Type = MmTerminalDataCapability
_H323GwCapabilitiesH323DataSend_Object = MibTableColumn
h323GwCapabilitiesH323DataSend = _H323GwCapabilitiesH323DataSend_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 1, 1, 6),
    _H323GwCapabilitiesH323DataSend_Type()
)
h323GwCapabilitiesH323DataSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH323DataSend.setStatus("current")
_H323GwCapabilitiesH320Table_Object = MibTable
h323GwCapabilitiesH320Table = _H323GwCapabilitiesH320Table_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h323GwCapabilitiesH320Table.setStatus("current")
_H323GwCapabilitiesH320Entry_Object = MibTableRow
h323GwCapabilitiesH320Entry = _H323GwCapabilitiesH320Entry_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 2, 1)
)
h323GwCapabilitiesH320Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwCapabilitiesH320Entry.setStatus("current")
_H323GwCapabilitiesH320AudioRecv_Type = MmTerminalAudioCapability
_H323GwCapabilitiesH320AudioRecv_Object = MibTableColumn
h323GwCapabilitiesH320AudioRecv = _H323GwCapabilitiesH320AudioRecv_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 2, 1, 1),
    _H323GwCapabilitiesH320AudioRecv_Type()
)
h323GwCapabilitiesH320AudioRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH320AudioRecv.setStatus("current")
_H323GwCapabilitiesH320AudioSend_Type = MmTerminalAudioCapability
_H323GwCapabilitiesH320AudioSend_Object = MibTableColumn
h323GwCapabilitiesH320AudioSend = _H323GwCapabilitiesH320AudioSend_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 2, 1, 2),
    _H323GwCapabilitiesH320AudioSend_Type()
)
h323GwCapabilitiesH320AudioSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH320AudioSend.setStatus("current")
_H323GwCapabilitiesH320VideoRecv_Type = MmTerminalVideoCapability
_H323GwCapabilitiesH320VideoRecv_Object = MibTableColumn
h323GwCapabilitiesH320VideoRecv = _H323GwCapabilitiesH320VideoRecv_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 2, 1, 3),
    _H323GwCapabilitiesH320VideoRecv_Type()
)
h323GwCapabilitiesH320VideoRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH320VideoRecv.setStatus("current")
_H323GwCapabilitiesH320VideoSend_Type = MmTerminalVideoCapability
_H323GwCapabilitiesH320VideoSend_Object = MibTableColumn
h323GwCapabilitiesH320VideoSend = _H323GwCapabilitiesH320VideoSend_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 2, 1, 4),
    _H323GwCapabilitiesH320VideoSend_Type()
)
h323GwCapabilitiesH320VideoSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH320VideoSend.setStatus("current")
_H323GwCapabilitiesH320DataRecv_Type = MmTerminalDataCapability
_H323GwCapabilitiesH320DataRecv_Object = MibTableColumn
h323GwCapabilitiesH320DataRecv = _H323GwCapabilitiesH320DataRecv_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 2, 1, 5),
    _H323GwCapabilitiesH320DataRecv_Type()
)
h323GwCapabilitiesH320DataRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH320DataRecv.setStatus("current")
_H323GwCapabilitiesH320DataSend_Type = MmTerminalDataCapability
_H323GwCapabilitiesH320DataSend_Object = MibTableColumn
h323GwCapabilitiesH320DataSend = _H323GwCapabilitiesH320DataSend_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 2, 1, 6),
    _H323GwCapabilitiesH320DataSend_Type()
)
h323GwCapabilitiesH320DataSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesH320DataSend.setStatus("current")
_H323GwCapabilitiesPstnTable_Object = MibTable
h323GwCapabilitiesPstnTable = _H323GwCapabilitiesPstnTable_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    h323GwCapabilitiesPstnTable.setStatus("current")
_H323GwCapabilitiesPstnEntry_Object = MibTableRow
h323GwCapabilitiesPstnEntry = _H323GwCapabilitiesPstnEntry_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 3, 1)
)
h323GwCapabilitiesPstnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwCapabilitiesPstnEntry.setStatus("current")
_H323GwCapabilitiesPstnTotalPorts_Type = Unsigned32
_H323GwCapabilitiesPstnTotalPorts_Object = MibTableColumn
h323GwCapabilitiesPstnTotalPorts = _H323GwCapabilitiesPstnTotalPorts_Object(
    (0, 0, 8, 341, 1, 4, 1, 3, 3, 1, 1),
    _H323GwCapabilitiesPstnTotalPorts_Type()
)
h323GwCapabilitiesPstnTotalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCapabilitiesPstnTotalPorts.setStatus("current")
_H323GwConnections_ObjectIdentity = ObjectIdentity
h323GwConnections = _H323GwConnections_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 4)
)
_H323GwConnectionsTable_Object = MibTable
h323GwConnectionsTable = _H323GwConnectionsTable_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h323GwConnectionsTable.setStatus("current")
_H323GwConnectionsEntry_Object = MibTableRow
h323GwConnectionsEntry = _H323GwConnectionsEntry_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1)
)
h323GwConnectionsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H323GW-MIB", "h323GwConnectionsEstablishedCallId"),
    (0, "H323GW-MIB", "h323GwConnectionsIndex"),
)
if mibBuilder.loadTexts:
    h323GwConnectionsEntry.setStatus("current")
_H323GwConnectionsEstablishedCallId_Type = MmGlobalIdentifier
_H323GwConnectionsEstablishedCallId_Object = MibTableColumn
h323GwConnectionsEstablishedCallId = _H323GwConnectionsEstablishedCallId_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 1),
    _H323GwConnectionsEstablishedCallId_Type()
)
h323GwConnectionsEstablishedCallId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h323GwConnectionsEstablishedCallId.setStatus("current")
_H323GwConnectionsIndex_Type = Integer32
_H323GwConnectionsIndex_Object = MibTableColumn
h323GwConnectionsIndex = _H323GwConnectionsIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 2),
    _H323GwConnectionsIndex_Type()
)
h323GwConnectionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h323GwConnectionsIndex.setStatus("current")
_H323GwConnectionsCommand_Type = H323gwConnectionCommand
_H323GwConnectionsCommand_Object = MibTableColumn
h323GwConnectionsCommand = _H323GwConnectionsCommand_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 3),
    _H323GwConnectionsCommand_Type()
)
h323GwConnectionsCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwConnectionsCommand.setStatus("current")
_H323GwConnectionsStartTime_Type = DateAndTime
_H323GwConnectionsStartTime_Object = MibTableColumn
h323GwConnectionsStartTime = _H323GwConnectionsStartTime_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 4),
    _H323GwConnectionsStartTime_Type()
)
h323GwConnectionsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsStartTime.setStatus("current")
_H323GwConnectionsTotalErrors_Type = Counter32
_H323GwConnectionsTotalErrors_Object = MibTableColumn
h323GwConnectionsTotalErrors = _H323GwConnectionsTotalErrors_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 5),
    _H323GwConnectionsTotalErrors_Type()
)
h323GwConnectionsTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsTotalErrors.setStatus("current")
_H323GwConnectionsLastError_Type = MmErrorProbableCause
_H323GwConnectionsLastError_Object = MibTableColumn
h323GwConnectionsLastError = _H323GwConnectionsLastError_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 6),
    _H323GwConnectionsLastError_Type()
)
h323GwConnectionsLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsLastError.setStatus("current")


class _H323GwConnectionsConnectionDirection_Type(Integer32):
    """Custom type h323GwConnectionsConnectionDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_H323GwConnectionsConnectionDirection_Type.__name__ = "Integer32"
_H323GwConnectionsConnectionDirection_Object = MibTableColumn
h323GwConnectionsConnectionDirection = _H323GwConnectionsConnectionDirection_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 7),
    _H323GwConnectionsConnectionDirection_Type()
)
h323GwConnectionsConnectionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsConnectionDirection.setStatus("current")
_H323GwConnectionsType_Type = H323gwSpecificTypes
_H323GwConnectionsType_Object = MibTableColumn
h323GwConnectionsType = _H323GwConnectionsType_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 8),
    _H323GwConnectionsType_Type()
)
h323GwConnectionsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsType.setStatus("current")
_H323GwConnectionsAliasAddressTag_Type = MmAliasTag
_H323GwConnectionsAliasAddressTag_Object = MibTableColumn
h323GwConnectionsAliasAddressTag = _H323GwConnectionsAliasAddressTag_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 9),
    _H323GwConnectionsAliasAddressTag_Type()
)
h323GwConnectionsAliasAddressTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsAliasAddressTag.setStatus("current")
_H323GwConnectionsAliasAddress_Type = MmAliasAddress
_H323GwConnectionsAliasAddress_Object = MibTableColumn
h323GwConnectionsAliasAddress = _H323GwConnectionsAliasAddress_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 10),
    _H323GwConnectionsAliasAddress_Type()
)
h323GwConnectionsAliasAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsAliasAddress.setStatus("current")
_H323GwConnectionsSpecificIndex_Type = Integer32
_H323GwConnectionsSpecificIndex_Object = MibTableColumn
h323GwConnectionsSpecificIndex = _H323GwConnectionsSpecificIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 1, 1, 11),
    _H323GwConnectionsSpecificIndex_Type()
)
h323GwConnectionsSpecificIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsSpecificIndex.setStatus("current")
_H323GwConnectionsH323Table_Object = MibTable
h323GwConnectionsH323Table = _H323GwConnectionsH323Table_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    h323GwConnectionsH323Table.setStatus("current")
_H323GwConnectionsH323Entry_Object = MibTableRow
h323GwConnectionsH323Entry = _H323GwConnectionsH323Entry_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 2, 1)
)
h323GwConnectionsH323Entry.setIndexNames(
    (0, "H323GW-MIB", "h323GwConnectionsH323Index"),
)
if mibBuilder.loadTexts:
    h323GwConnectionsH323Entry.setStatus("current")
_H323GwConnectionsH323Index_Type = Integer32
_H323GwConnectionsH323Index_Object = MibTableColumn
h323GwConnectionsH323Index = _H323GwConnectionsH323Index_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 2, 1, 1),
    _H323GwConnectionsH323Index_Type()
)
h323GwConnectionsH323Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h323GwConnectionsH323Index.setStatus("current")
_H323GwConnectionsH323CallSignallingIndex_Type = Integer32
_H323GwConnectionsH323CallSignallingIndex_Object = MibTableColumn
h323GwConnectionsH323CallSignallingIndex = _H323GwConnectionsH323CallSignallingIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 2, 1, 2),
    _H323GwConnectionsH323CallSignallingIndex_Type()
)
h323GwConnectionsH323CallSignallingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsH323CallSignallingIndex.setStatus("current")
_H323GwConnectionsH323ControlChannelIndex_Type = Integer32
_H323GwConnectionsH323ControlChannelIndex_Object = MibTableColumn
h323GwConnectionsH323ControlChannelIndex = _H323GwConnectionsH323ControlChannelIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 2, 1, 3),
    _H323GwConnectionsH323ControlChannelIndex_Type()
)
h323GwConnectionsH323ControlChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsH323ControlChannelIndex.setStatus("current")
_H323GwConnectionsH323RtpSessionIndex_Type = Integer32
_H323GwConnectionsH323RtpSessionIndex_Object = MibTableColumn
h323GwConnectionsH323RtpSessionIndex = _H323GwConnectionsH323RtpSessionIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 2, 1, 4),
    _H323GwConnectionsH323RtpSessionIndex_Type()
)
h323GwConnectionsH323RtpSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsH323RtpSessionIndex.setStatus("current")


class _H323GwConnectionsH323GwIfIndex_Type(InterfaceIndex):
    """Custom type h323GwConnectionsH323GwIfIndex based on InterfaceIndex"""
    defaultValue = 1


_H323GwConnectionsH323GwIfIndex_Object = MibTableColumn
h323GwConnectionsH323GwIfIndex = _H323GwConnectionsH323GwIfIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 2, 1, 5),
    _H323GwConnectionsH323GwIfIndex_Type()
)
h323GwConnectionsH323GwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h323GwConnectionsH323GwIfIndex.setStatus("current")
_H323GwConnectionsH320Table_Object = MibTable
h323GwConnectionsH320Table = _H323GwConnectionsH320Table_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    h323GwConnectionsH320Table.setStatus("current")
_H323GwConnectionsH320Entry_Object = MibTableRow
h323GwConnectionsH320Entry = _H323GwConnectionsH320Entry_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 3, 1)
)
h323GwConnectionsH320Entry.setIndexNames(
    (0, "H323GW-MIB", "h323GwConnectionsH320Index"),
)
if mibBuilder.loadTexts:
    h323GwConnectionsH320Entry.setStatus("current")
_H323GwConnectionsH320Index_Type = Integer32
_H323GwConnectionsH320Index_Object = MibTableColumn
h323GwConnectionsH320Index = _H323GwConnectionsH320Index_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 3, 1, 1),
    _H323GwConnectionsH320Index_Type()
)
h323GwConnectionsH320Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h323GwConnectionsH320Index.setStatus("current")
_H323GwConnectionsH320CapsH320TableIndex_Type = Integer32
_H323GwConnectionsH320CapsH320TableIndex_Object = MibTableColumn
h323GwConnectionsH320CapsH320TableIndex = _H323GwConnectionsH320CapsH320TableIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 3, 1, 2),
    _H323GwConnectionsH320CapsH320TableIndex_Type()
)
h323GwConnectionsH320CapsH320TableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsH320CapsH320TableIndex.setStatus("current")
_H323GwConnectionsH320CallStatusTableIndex_Type = Integer32
_H323GwConnectionsH320CallStatusTableIndex_Object = MibTableColumn
h323GwConnectionsH320CallStatusTableIndex = _H323GwConnectionsH320CallStatusTableIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 3, 1, 3),
    _H323GwConnectionsH320CallStatusTableIndex_Type()
)
h323GwConnectionsH320CallStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsH320CallStatusTableIndex.setStatus("current")
_H323GwConnectionsH320H221StatsTableIndex_Type = Integer32
_H323GwConnectionsH320H221StatsTableIndex_Object = MibTableColumn
h323GwConnectionsH320H221StatsTableIndex = _H323GwConnectionsH320H221StatsTableIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 3, 1, 4),
    _H323GwConnectionsH320H221StatsTableIndex_Type()
)
h323GwConnectionsH320H221StatsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwConnectionsH320H221StatsTableIndex.setStatus("current")


class _H323GwConnectionsH320GwIfIndex_Type(InterfaceIndex):
    """Custom type h323GwConnectionsH320GwIfIndex based on InterfaceIndex"""
    defaultValue = 1


_H323GwConnectionsH320GwIfIndex_Object = MibTableColumn
h323GwConnectionsH320GwIfIndex = _H323GwConnectionsH320GwIfIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 3, 1, 5),
    _H323GwConnectionsH320GwIfIndex_Type()
)
h323GwConnectionsH320GwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h323GwConnectionsH320GwIfIndex.setStatus("current")
_H323GwConnectionsPstnTable_Object = MibTable
h323GwConnectionsPstnTable = _H323GwConnectionsPstnTable_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 4)
)
if mibBuilder.loadTexts:
    h323GwConnectionsPstnTable.setStatus("current")
_H323GwConnectionsPstnEntry_Object = MibTableRow
h323GwConnectionsPstnEntry = _H323GwConnectionsPstnEntry_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 4, 1)
)
h323GwConnectionsPstnEntry.setIndexNames(
    (0, "H323GW-MIB", "h323GwConnectionsPstnIndex"),
)
if mibBuilder.loadTexts:
    h323GwConnectionsPstnEntry.setStatus("current")
_H323GwConnectionsPstnIndex_Type = Integer32
_H323GwConnectionsPstnIndex_Object = MibTableColumn
h323GwConnectionsPstnIndex = _H323GwConnectionsPstnIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 4, 1, 1),
    _H323GwConnectionsPstnIndex_Type()
)
h323GwConnectionsPstnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h323GwConnectionsPstnIndex.setStatus("current")


class _H323GwConnectionsPstnGwIfIndex_Type(InterfaceIndex):
    """Custom type h323GwConnectionsPstnGwIfIndex based on InterfaceIndex"""
    defaultValue = 1


_H323GwConnectionsPstnGwIfIndex_Object = MibTableColumn
h323GwConnectionsPstnGwIfIndex = _H323GwConnectionsPstnGwIfIndex_Object(
    (0, 0, 8, 341, 1, 4, 1, 4, 4, 1, 2),
    _H323GwConnectionsPstnGwIfIndex_Type()
)
h323GwConnectionsPstnGwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h323GwConnectionsPstnGwIfIndex.setStatus("current")
_H323GwCalls_ObjectIdentity = ObjectIdentity
h323GwCalls = _H323GwCalls_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 5)
)
_H323GwCallsTable_Object = MibTable
h323GwCallsTable = _H323GwCallsTable_Object(
    (0, 0, 8, 341, 1, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    h323GwCallsTable.setStatus("current")
_H323GwCallsTableEntry_Object = MibTableRow
h323GwCallsTableEntry = _H323GwCallsTableEntry_Object(
    (0, 0, 8, 341, 1, 4, 1, 5, 1, 1)
)
h323GwCallsTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H323GW-MIB", "h323GwCallsEstablishedCallId"),
)
if mibBuilder.loadTexts:
    h323GwCallsTableEntry.setStatus("current")
_H323GwCallsEstablishedCallId_Type = MmGlobalIdentifier
_H323GwCallsEstablishedCallId_Object = MibTableColumn
h323GwCallsEstablishedCallId = _H323GwCallsEstablishedCallId_Object(
    (0, 0, 8, 341, 1, 4, 1, 5, 1, 1, 1),
    _H323GwCallsEstablishedCallId_Type()
)
h323GwCallsEstablishedCallId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h323GwCallsEstablishedCallId.setStatus("current")
_H323GwCallsNumberOfConnectedDevices_Type = Integer32
_H323GwCallsNumberOfConnectedDevices_Object = MibTableColumn
h323GwCallsNumberOfConnectedDevices = _H323GwCallsNumberOfConnectedDevices_Object(
    (0, 0, 8, 341, 1, 4, 1, 5, 1, 1, 2),
    _H323GwCallsNumberOfConnectedDevices_Type()
)
h323GwCallsNumberOfConnectedDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCallsNumberOfConnectedDevices.setStatus("current")
_H323GwCallsGatewayAllocatedCallId_Type = Integer32
_H323GwCallsGatewayAllocatedCallId_Object = MibTableColumn
h323GwCallsGatewayAllocatedCallId = _H323GwCallsGatewayAllocatedCallId_Object(
    (0, 0, 8, 341, 1, 4, 1, 5, 1, 1, 3),
    _H323GwCallsGatewayAllocatedCallId_Type()
)
h323GwCallsGatewayAllocatedCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCallsGatewayAllocatedCallId.setStatus("current")
_H323GwCallsStartTime_Type = DateAndTime
_H323GwCallsStartTime_Object = MibTableColumn
h323GwCallsStartTime = _H323GwCallsStartTime_Object(
    (0, 0, 8, 341, 1, 4, 1, 5, 1, 1, 4),
    _H323GwCallsStartTime_Type()
)
h323GwCallsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCallsStartTime.setStatus("current")
_H323GwCallsTotalErrors_Type = Counter32
_H323GwCallsTotalErrors_Object = MibTableColumn
h323GwCallsTotalErrors = _H323GwCallsTotalErrors_Object(
    (0, 0, 8, 341, 1, 4, 1, 5, 1, 1, 5),
    _H323GwCallsTotalErrors_Type()
)
h323GwCallsTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCallsTotalErrors.setStatus("current")
_H323GwCallsLastError_Type = MmErrorProbableCause
_H323GwCallsLastError_Object = MibTableColumn
h323GwCallsLastError = _H323GwCallsLastError_Object(
    (0, 0, 8, 341, 1, 4, 1, 5, 1, 1, 6),
    _H323GwCallsLastError_Type()
)
h323GwCallsLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwCallsLastError.setStatus("current")
_H323GwStatistics_ObjectIdentity = ObjectIdentity
h323GwStatistics = _H323GwStatistics_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 6)
)
_H323GwStatisticsTable_Object = MibTable
h323GwStatisticsTable = _H323GwStatisticsTable_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    h323GwStatisticsTable.setStatus("current")
_H323GwStatisticsEntry_Object = MibTableRow
h323GwStatisticsEntry = _H323GwStatisticsEntry_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1)
)
h323GwStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwStatisticsEntry.setStatus("current")
_H323GwStatisticsTotalCallsNo_Type = Counter32
_H323GwStatisticsTotalCallsNo_Object = MibTableColumn
h323GwStatisticsTotalCallsNo = _H323GwStatisticsTotalCallsNo_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 1),
    _H323GwStatisticsTotalCallsNo_Type()
)
h323GwStatisticsTotalCallsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsTotalCallsNo.setStatus("current")
_H323GwStatisticsActiveConnectionsNo_Type = Gauge32
_H323GwStatisticsActiveConnectionsNo_Object = MibTableColumn
h323GwStatisticsActiveConnectionsNo = _H323GwStatisticsActiveConnectionsNo_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 2),
    _H323GwStatisticsActiveConnectionsNo_Type()
)
h323GwStatisticsActiveConnectionsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsActiveConnectionsNo.setStatus("current")
_H323GwStatisticsActiveCallsNo_Type = Gauge32
_H323GwStatisticsActiveCallsNo_Object = MibTableColumn
h323GwStatisticsActiveCallsNo = _H323GwStatisticsActiveCallsNo_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 3),
    _H323GwStatisticsActiveCallsNo_Type()
)
h323GwStatisticsActiveCallsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsActiveCallsNo.setStatus("current")
_H323GwStatisticsAdditionalEstCalls_Type = Gauge32
_H323GwStatisticsAdditionalEstCalls_Object = MibTableColumn
h323GwStatisticsAdditionalEstCalls = _H323GwStatisticsAdditionalEstCalls_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 4),
    _H323GwStatisticsAdditionalEstCalls_Type()
)
h323GwStatisticsAdditionalEstCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwStatisticsAdditionalEstCalls.setStatus("current")
_H323GwStatisticsAvrgSimultaneousCalls_Type = Gauge32
_H323GwStatisticsAvrgSimultaneousCalls_Object = MibTableColumn
h323GwStatisticsAvrgSimultaneousCalls = _H323GwStatisticsAvrgSimultaneousCalls_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 5),
    _H323GwStatisticsAvrgSimultaneousCalls_Type()
)
h323GwStatisticsAvrgSimultaneousCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsAvrgSimultaneousCalls.setStatus("current")
_H323GwStatisticsAvrgCallTime_Type = TimeTicks
_H323GwStatisticsAvrgCallTime_Object = MibTableColumn
h323GwStatisticsAvrgCallTime = _H323GwStatisticsAvrgCallTime_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 6),
    _H323GwStatisticsAvrgCallTime_Type()
)
h323GwStatisticsAvrgCallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsAvrgCallTime.setStatus("current")
_H323GwStatisticsTotalErrors_Type = Counter32
_H323GwStatisticsTotalErrors_Object = MibTableColumn
h323GwStatisticsTotalErrors = _H323GwStatisticsTotalErrors_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 7),
    _H323GwStatisticsTotalErrors_Type()
)
h323GwStatisticsTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsTotalErrors.setStatus("current")
_H323GwStatisticsLastErrorEventTime_Type = DateAndTime
_H323GwStatisticsLastErrorEventTime_Object = MibTableColumn
h323GwStatisticsLastErrorEventTime = _H323GwStatisticsLastErrorEventTime_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 8),
    _H323GwStatisticsLastErrorEventTime_Type()
)
h323GwStatisticsLastErrorEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsLastErrorEventTime.setStatus("current")
_H323GwStatisticsLastErrorSeverity_Type = MmErrorSeverity
_H323GwStatisticsLastErrorSeverity_Object = MibTableColumn
h323GwStatisticsLastErrorSeverity = _H323GwStatisticsLastErrorSeverity_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 9),
    _H323GwStatisticsLastErrorSeverity_Type()
)
h323GwStatisticsLastErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsLastErrorSeverity.setStatus("current")
_H323GwStatisticsLastErrorProbableCause_Type = MmErrorProbableCause
_H323GwStatisticsLastErrorProbableCause_Object = MibTableColumn
h323GwStatisticsLastErrorProbableCause = _H323GwStatisticsLastErrorProbableCause_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 10),
    _H323GwStatisticsLastErrorProbableCause_Type()
)
h323GwStatisticsLastErrorProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsLastErrorProbableCause.setStatus("current")
_H323GwStatisticsLastErrorAdditionalText_Type = DisplayString
_H323GwStatisticsLastErrorAdditionalText_Object = MibTableColumn
h323GwStatisticsLastErrorAdditionalText = _H323GwStatisticsLastErrorAdditionalText_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 1, 1, 11),
    _H323GwStatisticsLastErrorAdditionalText_Type()
)
h323GwStatisticsLastErrorAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsLastErrorAdditionalText.setStatus("current")
_H323GwStatisticsH323Table_Object = MibTable
h323GwStatisticsH323Table = _H323GwStatisticsH323Table_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 2)
)
if mibBuilder.loadTexts:
    h323GwStatisticsH323Table.setStatus("current")
_H323GwStatisticsH323Entry_Object = MibTableRow
h323GwStatisticsH323Entry = _H323GwStatisticsH323Entry_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 2, 1)
)
h323GwStatisticsH323Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwStatisticsH323Entry.setStatus("current")
_H323GwStatisticsH323TotalPacketsLost_Type = Counter32
_H323GwStatisticsH323TotalPacketsLost_Object = MibTableColumn
h323GwStatisticsH323TotalPacketsLost = _H323GwStatisticsH323TotalPacketsLost_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 2, 1, 1),
    _H323GwStatisticsH323TotalPacketsLost_Type()
)
h323GwStatisticsH323TotalPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsH323TotalPacketsLost.setStatus("current")
_H323GwStatisticsH323PacketsRecv_Type = Counter32
_H323GwStatisticsH323PacketsRecv_Object = MibTableColumn
h323GwStatisticsH323PacketsRecv = _H323GwStatisticsH323PacketsRecv_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 2, 1, 2),
    _H323GwStatisticsH323PacketsRecv_Type()
)
h323GwStatisticsH323PacketsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsH323PacketsRecv.setStatus("current")
_H323GwStatisticsH323PacketsSent_Type = Counter32
_H323GwStatisticsH323PacketsSent_Object = MibTableColumn
h323GwStatisticsH323PacketsSent = _H323GwStatisticsH323PacketsSent_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 2, 1, 3),
    _H323GwStatisticsH323PacketsSent_Type()
)
h323GwStatisticsH323PacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsH323PacketsSent.setStatus("current")
_H323GwStatisticsH323BytesRecv_Type = Counter64
_H323GwStatisticsH323BytesRecv_Object = MibTableColumn
h323GwStatisticsH323BytesRecv = _H323GwStatisticsH323BytesRecv_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 2, 1, 4),
    _H323GwStatisticsH323BytesRecv_Type()
)
h323GwStatisticsH323BytesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsH323BytesRecv.setStatus("current")
_H323GwStatisticsH323BytesSent_Type = Counter64
_H323GwStatisticsH323BytesSent_Object = MibTableColumn
h323GwStatisticsH323BytesSent = _H323GwStatisticsH323BytesSent_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 2, 1, 5),
    _H323GwStatisticsH323BytesSent_Type()
)
h323GwStatisticsH323BytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsH323BytesSent.setStatus("current")
_H323GwStatisticsH323ActiveConnectionsNo_Type = Gauge32
_H323GwStatisticsH323ActiveConnectionsNo_Object = MibTableColumn
h323GwStatisticsH323ActiveConnectionsNo = _H323GwStatisticsH323ActiveConnectionsNo_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 2, 1, 6),
    _H323GwStatisticsH323ActiveConnectionsNo_Type()
)
h323GwStatisticsH323ActiveConnectionsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsH323ActiveConnectionsNo.setStatus("current")
_H323GwStatisticsH320Table_Object = MibTable
h323GwStatisticsH320Table = _H323GwStatisticsH320Table_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 3)
)
if mibBuilder.loadTexts:
    h323GwStatisticsH320Table.setStatus("current")
_H323GwStatisticsH320Entry_Object = MibTableRow
h323GwStatisticsH320Entry = _H323GwStatisticsH320Entry_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 3, 1)
)
h323GwStatisticsH320Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwStatisticsH320Entry.setStatus("current")
_H323GwStatisticsH320TotalPortsFailed_Type = Unsigned32
_H323GwStatisticsH320TotalPortsFailed_Object = MibTableColumn
h323GwStatisticsH320TotalPortsFailed = _H323GwStatisticsH320TotalPortsFailed_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 3, 1, 1),
    _H323GwStatisticsH320TotalPortsFailed_Type()
)
h323GwStatisticsH320TotalPortsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsH320TotalPortsFailed.setStatus("current")
_H323GwStatisticsH320ActiveConnectionsNo_Type = Gauge32
_H323GwStatisticsH320ActiveConnectionsNo_Object = MibTableColumn
h323GwStatisticsH320ActiveConnectionsNo = _H323GwStatisticsH320ActiveConnectionsNo_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 3, 1, 2),
    _H323GwStatisticsH320ActiveConnectionsNo_Type()
)
h323GwStatisticsH320ActiveConnectionsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsH320ActiveConnectionsNo.setStatus("current")
_H323GwStatisticsPstnTable_Object = MibTable
h323GwStatisticsPstnTable = _H323GwStatisticsPstnTable_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 4)
)
if mibBuilder.loadTexts:
    h323GwStatisticsPstnTable.setStatus("current")
_H323GwStatisticsPstnEntry_Object = MibTableRow
h323GwStatisticsPstnEntry = _H323GwStatisticsPstnEntry_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 4, 1)
)
h323GwStatisticsPstnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h323GwStatisticsPstnEntry.setStatus("current")
_H323GwStatisticsPstnTotalPortsFailed_Type = Unsigned32
_H323GwStatisticsPstnTotalPortsFailed_Object = MibTableColumn
h323GwStatisticsPstnTotalPortsFailed = _H323GwStatisticsPstnTotalPortsFailed_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 4, 1, 1),
    _H323GwStatisticsPstnTotalPortsFailed_Type()
)
h323GwStatisticsPstnTotalPortsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsPstnTotalPortsFailed.setStatus("current")
_H323GwStatisticsPstnTotalUnusedPorts_Type = Unsigned32
_H323GwStatisticsPstnTotalUnusedPorts_Object = MibTableColumn
h323GwStatisticsPstnTotalUnusedPorts = _H323GwStatisticsPstnTotalUnusedPorts_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 4, 1, 2),
    _H323GwStatisticsPstnTotalUnusedPorts_Type()
)
h323GwStatisticsPstnTotalUnusedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsPstnTotalUnusedPorts.setStatus("current")
_H323GwStatisticsPstnActiveConnectionsNo_Type = Gauge32
_H323GwStatisticsPstnActiveConnectionsNo_Object = MibTableColumn
h323GwStatisticsPstnActiveConnectionsNo = _H323GwStatisticsPstnActiveConnectionsNo_Object(
    (0, 0, 8, 341, 1, 4, 1, 6, 4, 1, 3),
    _H323GwStatisticsPstnActiveConnectionsNo_Type()
)
h323GwStatisticsPstnActiveConnectionsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h323GwStatisticsPstnActiveConnectionsNo.setStatus("current")
_H323GwControls_ObjectIdentity = ObjectIdentity
h323GwControls = _H323GwControls_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 7)
)
_H323GwControlsCommands_Type = MmControlsCommands
_H323GwControlsCommands_Object = MibScalar
h323GwControlsCommands = _H323GwControlsCommands_Object(
    (0, 0, 8, 341, 1, 4, 1, 7, 1),
    _H323GwControlsCommands_Type()
)
h323GwControlsCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323GwControlsCommands.setStatus("current")
_H323GwNotifications_ObjectIdentity = ObjectIdentity
h323GwNotifications = _H323GwNotifications_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 8, 0)
)
_H323GwMIBConformance_ObjectIdentity = ObjectIdentity
h323GwMIBConformance = _H323GwMIBConformance_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 9)
)
_H323GwMIBCompliance_ObjectIdentity = ObjectIdentity
h323GwMIBCompliance = _H323GwMIBCompliance_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 9, 1)
)
_H323GwMIBGroups_ObjectIdentity = ObjectIdentity
h323GwMIBGroups = _H323GwMIBGroups_ObjectIdentity(
    (0, 0, 8, 341, 1, 4, 1, 9, 2)
)

# Managed Objects groups

h323GwSystemGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 4, 1, 9, 2, 1)
)
h323GwSystemGroup.setObjects(
      *(("H323GW-MIB", "h323GwSystemNameAndMaker"),
        ("H323GW-MIB", "h323GwSystemSoftwareVersionNumber"),
        ("H323GW-MIB", "h323GwSystemHardwareVersionNumber"),
        ("H323GW-MIB", "h323GwSystemContact"),
        ("H323GW-MIB", "h323GwSystemt35CountryCode"),
        ("H323GW-MIB", "h323GwSystemt35CountryCodeExtention"),
        ("H323GW-MIB", "h323GwSystemt35ManufacturerCode"),
        ("H323GW-MIB", "h323GwSystemLocation"),
        ("H323GW-MIB", "h323GwSystemUptime"),
        ("H323GW-MIB", "h323GwSystemLocalTime"))
)
if mibBuilder.loadTexts:
    h323GwSystemGroup.setStatus("current")

h323GwConfigurationGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 4, 1, 9, 2, 2)
)
h323GwConfigurationGroup.setObjects(
      *(("H323GW-MIB", "h323GwConfigurationEnableNotifications"),
        ("H323GW-MIB", "h323GwConfigurationLeadingAliasAddressTag"),
        ("H323GW-MIB", "h323GwConfigurationLeadingAliasAddress"),
        ("H323GW-MIB", "h323GwConfigurationH323CallSignalingAddressTag"),
        ("H323GW-MIB", "h323GwConfigurationH323CallSignalingAddress"),
        ("H323GW-MIB", "h323GwConfigurationH323GatekeeperAddressTag"),
        ("H323GW-MIB", "h323GwConfigurationH323GatekeeperAddress"),
        ("H323GW-MIB", "h323GwConfigurationH320TotalPorts"),
        ("H323GW-MIB", "h323GwConfigurationPstnTotalPorts"))
)
if mibBuilder.loadTexts:
    h323GwConfigurationGroup.setStatus("current")

h323GwCapabilitiesGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 4, 1, 9, 2, 3)
)
h323GwCapabilitiesGroup.setObjects(
      *(("H323GW-MIB", "h323GwCapabilitiesH323AudioRecv"),
        ("H323GW-MIB", "h323GwCapabilitiesH323AudioSend"),
        ("H323GW-MIB", "h323GwCapabilitiesH323VideoRecv"),
        ("H323GW-MIB", "h323GwCapabilitiesH323VideoSend"),
        ("H323GW-MIB", "h323GwCapabilitiesH323DataRecv"),
        ("H323GW-MIB", "h323GwCapabilitiesH323DataSend"),
        ("H323GW-MIB", "h323GwCapabilitiesPstnTotalPorts"))
)
if mibBuilder.loadTexts:
    h323GwCapabilitiesGroup.setStatus("current")

h323GwConnectionsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 4, 1, 9, 2, 4)
)
h323GwConnectionsGroup.setObjects(
      *(("H323GW-MIB", "h323GwConnectionsCommand"),
        ("H323GW-MIB", "h323GwConnectionsStartTime"),
        ("H323GW-MIB", "h323GwConnectionsTotalErrors"),
        ("H323GW-MIB", "h323GwConnectionsLastError"),
        ("H323GW-MIB", "h323GwConnectionsConnectionDirection"),
        ("H323GW-MIB", "h323GwConnectionsType"),
        ("H323GW-MIB", "h323GwConnectionsAliasAddressTag"),
        ("H323GW-MIB", "h323GwConnectionsAliasAddress"),
        ("H323GW-MIB", "h323GwConnectionsSpecificIndex"),
        ("H323GW-MIB", "h323GwConnectionsH323CallSignallingIndex"),
        ("H323GW-MIB", "h323GwConnectionsH323ControlChannelIndex"),
        ("H323GW-MIB", "h323GwConnectionsH323RtpSessionIndex"),
        ("H323GW-MIB", "h323GwConnectionsH320CapsH320TableIndex"),
        ("H323GW-MIB", "h323GwConnectionsH320CallStatusTableIndex"),
        ("H323GW-MIB", "h323GwConnectionsH320H221StatsTableIndex"))
)
if mibBuilder.loadTexts:
    h323GwConnectionsGroup.setStatus("current")

h323GwCallsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 4, 1, 9, 2, 5)
)
h323GwCallsGroup.setObjects(
      *(("H323GW-MIB", "h323GwCallsNumberOfConnectedDevices"),
        ("H323GW-MIB", "h323GwCallsGatewayAllocatedCallId"),
        ("H323GW-MIB", "h323GwCallsStartTime"),
        ("H323GW-MIB", "h323GwCallsTotalErrors"),
        ("H323GW-MIB", "h323GwCallsLastError"))
)
if mibBuilder.loadTexts:
    h323GwCallsGroup.setStatus("current")

h323GwStatisticsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 4, 1, 9, 2, 6)
)
h323GwStatisticsGroup.setObjects(
      *(("H323GW-MIB", "h323GwStatisticsTotalCallsNo"),
        ("H323GW-MIB", "h323GwStatisticsActiveConnectionsNo"),
        ("H323GW-MIB", "h323GwStatisticsActiveCallsNo"),
        ("H323GW-MIB", "h323GwStatisticsAdditionalEstCalls"),
        ("H323GW-MIB", "h323GwStatisticsAvrgSimultaneousCalls"),
        ("H323GW-MIB", "h323GwStatisticsAvrgCallTime"),
        ("H323GW-MIB", "h323GwStatisticsTotalErrors"),
        ("H323GW-MIB", "h323GwStatisticsLastErrorEventTime"),
        ("H323GW-MIB", "h323GwStatisticsLastErrorSeverity"),
        ("H323GW-MIB", "h323GwStatisticsLastErrorProbableCause"),
        ("H323GW-MIB", "h323GwStatisticsLastErrorAdditionalText"),
        ("H323GW-MIB", "h323GwStatisticsH323TotalPacketsLost"),
        ("H323GW-MIB", "h323GwStatisticsH323PacketsRecv"),
        ("H323GW-MIB", "h323GwStatisticsH323PacketsSent"),
        ("H323GW-MIB", "h323GwStatisticsH323BytesRecv"),
        ("H323GW-MIB", "h323GwStatisticsH323BytesSent"),
        ("H323GW-MIB", "h323GwStatisticsH320TotalPortsFailed"),
        ("H323GW-MIB", "h323GwStatisticsH320ActiveConnectionsNo"),
        ("H323GW-MIB", "h323GwStatisticsPstnTotalPortsFailed"),
        ("H323GW-MIB", "h323GwStatisticsPstnTotalUnusedPorts"),
        ("H323GW-MIB", "h323GwStatisticsPstnActiveConnectionsNo"))
)
if mibBuilder.loadTexts:
    h323GwStatisticsGroup.setStatus("current")

h323GwControlsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 4, 1, 9, 2, 7)
)
h323GwControlsGroup.setObjects(
    ("H323GW-MIB", "h323GwControlsCommands")
)
if mibBuilder.loadTexts:
    h323GwControlsGroup.setStatus("current")


# Notification objects

h323GwStart = NotificationType(
    (0, 0, 8, 341, 1, 4, 1, 8, 0, 1)
)
h323GwStart.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h323GwStart.setStatus(
        "current"
    )

h323GwGoingDown = NotificationType(
    (0, 0, 8, 341, 1, 4, 1, 8, 0, 2)
)
h323GwGoingDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    h323GwGoingDown.setStatus(
        "current"
    )

h323GwError = NotificationType(
    (0, 0, 8, 341, 1, 4, 1, 8, 0, 3)
)
h323GwError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H323GW-MIB", "h323GwStatisticsLastErrorEventTime"),
        ("H323GW-MIB", "h323GwStatisticsLastErrorSeverity"),
        ("H323GW-MIB", "h323GwStatisticsLastErrorProbableCause"))
)
if mibBuilder.loadTexts:
    h323GwError.setStatus(
        "current"
    )


# Notifications groups

h323GwNotificationsGroup = NotificationGroup(
    (0, 0, 8, 341, 1, 4, 1, 9, 2, 8)
)
h323GwNotificationsGroup.setObjects(
      *(("H323GW-MIB", "h323GwStart"),
        ("H323GW-MIB", "h323GwGoingDown"),
        ("H323GW-MIB", "h323GwError"))
)
if mibBuilder.loadTexts:
    h323GwNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h323GwCompliance = ModuleCompliance(
    (0, 0, 8, 341, 1, 4, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    h323GwCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H323GW-MIB",
    **{"H323gwSpecificTypes": H323gwSpecificTypes,
       "H323gwConnectionCommand": H323gwConnectionCommand,
       "h323Gw": h323Gw,
       "h323GwSystem": h323GwSystem,
       "h323GwSystemTable": h323GwSystemTable,
       "h323GwSystemEntry": h323GwSystemEntry,
       "h323GwSystemNameAndMaker": h323GwSystemNameAndMaker,
       "h323GwSystemSoftwareVersionNumber": h323GwSystemSoftwareVersionNumber,
       "h323GwSystemHardwareVersionNumber": h323GwSystemHardwareVersionNumber,
       "h323GwSystemContact": h323GwSystemContact,
       "h323GwSystemt35CountryCode": h323GwSystemt35CountryCode,
       "h323GwSystemt35CountryCodeExtention": h323GwSystemt35CountryCodeExtention,
       "h323GwSystemt35ManufacturerCode": h323GwSystemt35ManufacturerCode,
       "h323GwSystemLocation": h323GwSystemLocation,
       "h323GwSystemUptime": h323GwSystemUptime,
       "h323GwSystemLocalTime": h323GwSystemLocalTime,
       "h323GwConfiguration": h323GwConfiguration,
       "h323GwConfigurationTable": h323GwConfigurationTable,
       "h323GwConfigurationEntry": h323GwConfigurationEntry,
       "h323GwConfigurationEnableNotifications": h323GwConfigurationEnableNotifications,
       "h323GwConfigurationLeadingAliasAddressTag": h323GwConfigurationLeadingAliasAddressTag,
       "h323GwConfigurationLeadingAliasAddress": h323GwConfigurationLeadingAliasAddress,
       "h323GwConfigurationH323Table": h323GwConfigurationH323Table,
       "h323GwConfigurationH323Entry": h323GwConfigurationH323Entry,
       "h323GwConfigurationH323CallSignalingAddressTag": h323GwConfigurationH323CallSignalingAddressTag,
       "h323GwConfigurationH323CallSignalingAddress": h323GwConfigurationH323CallSignalingAddress,
       "h323GwConfigurationH323GatekeeperAddressTag": h323GwConfigurationH323GatekeeperAddressTag,
       "h323GwConfigurationH323GatekeeperAddress": h323GwConfigurationH323GatekeeperAddress,
       "h323GwConfigurationH320Table": h323GwConfigurationH320Table,
       "h323GwConfigurationH320Entry": h323GwConfigurationH320Entry,
       "h323GwConfigurationH320TotalPorts": h323GwConfigurationH320TotalPorts,
       "h323GwConfigurationPstnTable": h323GwConfigurationPstnTable,
       "h323GwConfigurationPstnEntry": h323GwConfigurationPstnEntry,
       "h323GwConfigurationPstnTotalPorts": h323GwConfigurationPstnTotalPorts,
       "h323GwCapabilities": h323GwCapabilities,
       "h323GwCapabilitiesH323Table": h323GwCapabilitiesH323Table,
       "h323GwCapabilitiesH323Entry": h323GwCapabilitiesH323Entry,
       "h323GwCapabilitiesH323AudioRecv": h323GwCapabilitiesH323AudioRecv,
       "h323GwCapabilitiesH323AudioSend": h323GwCapabilitiesH323AudioSend,
       "h323GwCapabilitiesH323VideoRecv": h323GwCapabilitiesH323VideoRecv,
       "h323GwCapabilitiesH323VideoSend": h323GwCapabilitiesH323VideoSend,
       "h323GwCapabilitiesH323DataRecv": h323GwCapabilitiesH323DataRecv,
       "h323GwCapabilitiesH323DataSend": h323GwCapabilitiesH323DataSend,
       "h323GwCapabilitiesH320Table": h323GwCapabilitiesH320Table,
       "h323GwCapabilitiesH320Entry": h323GwCapabilitiesH320Entry,
       "h323GwCapabilitiesH320AudioRecv": h323GwCapabilitiesH320AudioRecv,
       "h323GwCapabilitiesH320AudioSend": h323GwCapabilitiesH320AudioSend,
       "h323GwCapabilitiesH320VideoRecv": h323GwCapabilitiesH320VideoRecv,
       "h323GwCapabilitiesH320VideoSend": h323GwCapabilitiesH320VideoSend,
       "h323GwCapabilitiesH320DataRecv": h323GwCapabilitiesH320DataRecv,
       "h323GwCapabilitiesH320DataSend": h323GwCapabilitiesH320DataSend,
       "h323GwCapabilitiesPstnTable": h323GwCapabilitiesPstnTable,
       "h323GwCapabilitiesPstnEntry": h323GwCapabilitiesPstnEntry,
       "h323GwCapabilitiesPstnTotalPorts": h323GwCapabilitiesPstnTotalPorts,
       "h323GwConnections": h323GwConnections,
       "h323GwConnectionsTable": h323GwConnectionsTable,
       "h323GwConnectionsEntry": h323GwConnectionsEntry,
       "h323GwConnectionsEstablishedCallId": h323GwConnectionsEstablishedCallId,
       "h323GwConnectionsIndex": h323GwConnectionsIndex,
       "h323GwConnectionsCommand": h323GwConnectionsCommand,
       "h323GwConnectionsStartTime": h323GwConnectionsStartTime,
       "h323GwConnectionsTotalErrors": h323GwConnectionsTotalErrors,
       "h323GwConnectionsLastError": h323GwConnectionsLastError,
       "h323GwConnectionsConnectionDirection": h323GwConnectionsConnectionDirection,
       "h323GwConnectionsType": h323GwConnectionsType,
       "h323GwConnectionsAliasAddressTag": h323GwConnectionsAliasAddressTag,
       "h323GwConnectionsAliasAddress": h323GwConnectionsAliasAddress,
       "h323GwConnectionsSpecificIndex": h323GwConnectionsSpecificIndex,
       "h323GwConnectionsH323Table": h323GwConnectionsH323Table,
       "h323GwConnectionsH323Entry": h323GwConnectionsH323Entry,
       "h323GwConnectionsH323Index": h323GwConnectionsH323Index,
       "h323GwConnectionsH323CallSignallingIndex": h323GwConnectionsH323CallSignallingIndex,
       "h323GwConnectionsH323ControlChannelIndex": h323GwConnectionsH323ControlChannelIndex,
       "h323GwConnectionsH323RtpSessionIndex": h323GwConnectionsH323RtpSessionIndex,
       "h323GwConnectionsH323GwIfIndex": h323GwConnectionsH323GwIfIndex,
       "h323GwConnectionsH320Table": h323GwConnectionsH320Table,
       "h323GwConnectionsH320Entry": h323GwConnectionsH320Entry,
       "h323GwConnectionsH320Index": h323GwConnectionsH320Index,
       "h323GwConnectionsH320CapsH320TableIndex": h323GwConnectionsH320CapsH320TableIndex,
       "h323GwConnectionsH320CallStatusTableIndex": h323GwConnectionsH320CallStatusTableIndex,
       "h323GwConnectionsH320H221StatsTableIndex": h323GwConnectionsH320H221StatsTableIndex,
       "h323GwConnectionsH320GwIfIndex": h323GwConnectionsH320GwIfIndex,
       "h323GwConnectionsPstnTable": h323GwConnectionsPstnTable,
       "h323GwConnectionsPstnEntry": h323GwConnectionsPstnEntry,
       "h323GwConnectionsPstnIndex": h323GwConnectionsPstnIndex,
       "h323GwConnectionsPstnGwIfIndex": h323GwConnectionsPstnGwIfIndex,
       "h323GwCalls": h323GwCalls,
       "h323GwCallsTable": h323GwCallsTable,
       "h323GwCallsTableEntry": h323GwCallsTableEntry,
       "h323GwCallsEstablishedCallId": h323GwCallsEstablishedCallId,
       "h323GwCallsNumberOfConnectedDevices": h323GwCallsNumberOfConnectedDevices,
       "h323GwCallsGatewayAllocatedCallId": h323GwCallsGatewayAllocatedCallId,
       "h323GwCallsStartTime": h323GwCallsStartTime,
       "h323GwCallsTotalErrors": h323GwCallsTotalErrors,
       "h323GwCallsLastError": h323GwCallsLastError,
       "h323GwStatistics": h323GwStatistics,
       "h323GwStatisticsTable": h323GwStatisticsTable,
       "h323GwStatisticsEntry": h323GwStatisticsEntry,
       "h323GwStatisticsTotalCallsNo": h323GwStatisticsTotalCallsNo,
       "h323GwStatisticsActiveConnectionsNo": h323GwStatisticsActiveConnectionsNo,
       "h323GwStatisticsActiveCallsNo": h323GwStatisticsActiveCallsNo,
       "h323GwStatisticsAdditionalEstCalls": h323GwStatisticsAdditionalEstCalls,
       "h323GwStatisticsAvrgSimultaneousCalls": h323GwStatisticsAvrgSimultaneousCalls,
       "h323GwStatisticsAvrgCallTime": h323GwStatisticsAvrgCallTime,
       "h323GwStatisticsTotalErrors": h323GwStatisticsTotalErrors,
       "h323GwStatisticsLastErrorEventTime": h323GwStatisticsLastErrorEventTime,
       "h323GwStatisticsLastErrorSeverity": h323GwStatisticsLastErrorSeverity,
       "h323GwStatisticsLastErrorProbableCause": h323GwStatisticsLastErrorProbableCause,
       "h323GwStatisticsLastErrorAdditionalText": h323GwStatisticsLastErrorAdditionalText,
       "h323GwStatisticsH323Table": h323GwStatisticsH323Table,
       "h323GwStatisticsH323Entry": h323GwStatisticsH323Entry,
       "h323GwStatisticsH323TotalPacketsLost": h323GwStatisticsH323TotalPacketsLost,
       "h323GwStatisticsH323PacketsRecv": h323GwStatisticsH323PacketsRecv,
       "h323GwStatisticsH323PacketsSent": h323GwStatisticsH323PacketsSent,
       "h323GwStatisticsH323BytesRecv": h323GwStatisticsH323BytesRecv,
       "h323GwStatisticsH323BytesSent": h323GwStatisticsH323BytesSent,
       "h323GwStatisticsH323ActiveConnectionsNo": h323GwStatisticsH323ActiveConnectionsNo,
       "h323GwStatisticsH320Table": h323GwStatisticsH320Table,
       "h323GwStatisticsH320Entry": h323GwStatisticsH320Entry,
       "h323GwStatisticsH320TotalPortsFailed": h323GwStatisticsH320TotalPortsFailed,
       "h323GwStatisticsH320ActiveConnectionsNo": h323GwStatisticsH320ActiveConnectionsNo,
       "h323GwStatisticsPstnTable": h323GwStatisticsPstnTable,
       "h323GwStatisticsPstnEntry": h323GwStatisticsPstnEntry,
       "h323GwStatisticsPstnTotalPortsFailed": h323GwStatisticsPstnTotalPortsFailed,
       "h323GwStatisticsPstnTotalUnusedPorts": h323GwStatisticsPstnTotalUnusedPorts,
       "h323GwStatisticsPstnActiveConnectionsNo": h323GwStatisticsPstnActiveConnectionsNo,
       "h323GwControls": h323GwControls,
       "h323GwControlsCommands": h323GwControlsCommands,
       "h323GwNotifications": h323GwNotifications,
       "h323GwStart": h323GwStart,
       "h323GwGoingDown": h323GwGoingDown,
       "h323GwError": h323GwError,
       "h323GwMIBConformance": h323GwMIBConformance,
       "h323GwMIBCompliance": h323GwMIBCompliance,
       "h323GwCompliance": h323GwCompliance,
       "h323GwMIBGroups": h323GwMIBGroups,
       "h323GwSystemGroup": h323GwSystemGroup,
       "h323GwConfigurationGroup": h323GwConfigurationGroup,
       "h323GwCapabilitiesGroup": h323GwCapabilitiesGroup,
       "h323GwConnectionsGroup": h323GwConnectionsGroup,
       "h323GwCallsGroup": h323GwCallsGroup,
       "h323GwStatisticsGroup": h323GwStatisticsGroup,
       "h323GwControlsGroup": h323GwControlsGroup,
       "h323GwNotificationsGroup": h323GwNotificationsGroup}
)
