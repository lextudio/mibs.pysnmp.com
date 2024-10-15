# SNMP MIB module (PRINTER-PORT-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PRINTER-PORT-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:42 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ppmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2)
)
ppmMIB.setRevisions(
        ("2005-10-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PpmMIBObjects_ObjectIdentity = ObjectIdentity
ppmMIBObjects = _PpmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1)
)
_PpmGeneral_ObjectIdentity = ObjectIdentity
ppmGeneral = _PpmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1)
)


class _PpmGeneralNaturalLanguage_Type(SnmpAdminString):
    """Custom type ppmGeneralNaturalLanguage based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PpmGeneralNaturalLanguage_Type.__name__ = "SnmpAdminString"
_PpmGeneralNaturalLanguage_Object = MibScalar
ppmGeneralNaturalLanguage = _PpmGeneralNaturalLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1, 1),
    _PpmGeneralNaturalLanguage_Type()
)
ppmGeneralNaturalLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmGeneralNaturalLanguage.setStatus("current")


class _PpmGeneralNumberOfPrinters_Type(Gauge32):
    """Custom type ppmGeneralNumberOfPrinters based on Gauge32"""
    defaultValue = 0


_PpmGeneralNumberOfPrinters_Object = MibScalar
ppmGeneralNumberOfPrinters = _PpmGeneralNumberOfPrinters_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1, 2),
    _PpmGeneralNumberOfPrinters_Type()
)
ppmGeneralNumberOfPrinters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmGeneralNumberOfPrinters.setStatus("current")


class _PpmGeneralNumberOfPorts_Type(Gauge32):
    """Custom type ppmGeneralNumberOfPorts based on Gauge32"""
    defaultValue = 0


_PpmGeneralNumberOfPorts_Object = MibScalar
ppmGeneralNumberOfPorts = _PpmGeneralNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 1, 3),
    _PpmGeneralNumberOfPorts_Type()
)
ppmGeneralNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmGeneralNumberOfPorts.setStatus("current")
_PpmPrinter_ObjectIdentity = ObjectIdentity
ppmPrinter = _PpmPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2)
)
_PpmPrinterTable_Object = MibTable
ppmPrinterTable = _PpmPrinterTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ppmPrinterTable.setStatus("current")
_PpmPrinterEntry_Object = MibTableRow
ppmPrinterEntry = _PpmPrinterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1)
)
ppmPrinterEntry.setIndexNames(
    (0, "PRINTER-PORT-MONITOR-MIB", "ppmPrinterIndex"),
)
if mibBuilder.loadTexts:
    ppmPrinterEntry.setStatus("current")


class _PpmPrinterIndex_Type(Integer32):
    """Custom type ppmPrinterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PpmPrinterIndex_Type.__name__ = "Integer32"
_PpmPrinterIndex_Object = MibTableColumn
ppmPrinterIndex = _PpmPrinterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 1),
    _PpmPrinterIndex_Type()
)
ppmPrinterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ppmPrinterIndex.setStatus("current")


class _PpmPrinterName_Type(SnmpAdminString):
    """Custom type ppmPrinterName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PpmPrinterName_Type.__name__ = "SnmpAdminString"
_PpmPrinterName_Object = MibTableColumn
ppmPrinterName = _PpmPrinterName_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 2),
    _PpmPrinterName_Type()
)
ppmPrinterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterName.setStatus("current")


class _PpmPrinterIEEE1284DeviceId_Type(OctetString):
    """Custom type ppmPrinterIEEE1284DeviceId based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_PpmPrinterIEEE1284DeviceId_Type.__name__ = "OctetString"
_PpmPrinterIEEE1284DeviceId_Object = MibTableColumn
ppmPrinterIEEE1284DeviceId = _PpmPrinterIEEE1284DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 3),
    _PpmPrinterIEEE1284DeviceId_Type()
)
ppmPrinterIEEE1284DeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterIEEE1284DeviceId.setStatus("current")


class _PpmPrinterNumberOfPorts_Type(Gauge32):
    """Custom type ppmPrinterNumberOfPorts based on Gauge32"""
    defaultValue = 0


_PpmPrinterNumberOfPorts_Object = MibTableColumn
ppmPrinterNumberOfPorts = _PpmPrinterNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 4),
    _PpmPrinterNumberOfPorts_Type()
)
ppmPrinterNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterNumberOfPorts.setStatus("current")


class _PpmPrinterPreferredPortIndex_Type(Integer32):
    """Custom type ppmPrinterPreferredPortIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PpmPrinterPreferredPortIndex_Type.__name__ = "Integer32"
_PpmPrinterPreferredPortIndex_Object = MibTableColumn
ppmPrinterPreferredPortIndex = _PpmPrinterPreferredPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 5),
    _PpmPrinterPreferredPortIndex_Type()
)
ppmPrinterPreferredPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterPreferredPortIndex.setStatus("current")


class _PpmPrinterHrDeviceIndex_Type(Integer32):
    """Custom type ppmPrinterHrDeviceIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PpmPrinterHrDeviceIndex_Type.__name__ = "Integer32"
_PpmPrinterHrDeviceIndex_Object = MibTableColumn
ppmPrinterHrDeviceIndex = _PpmPrinterHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 6),
    _PpmPrinterHrDeviceIndex_Type()
)
ppmPrinterHrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterHrDeviceIndex.setStatus("current")


class _PpmPrinterSnmpCommunityName_Type(OctetString):
    """Custom type ppmPrinterSnmpCommunityName based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PpmPrinterSnmpCommunityName_Type.__name__ = "OctetString"
_PpmPrinterSnmpCommunityName_Object = MibTableColumn
ppmPrinterSnmpCommunityName = _PpmPrinterSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 7),
    _PpmPrinterSnmpCommunityName_Type()
)
ppmPrinterSnmpCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterSnmpCommunityName.setStatus("current")


class _PpmPrinterSnmpQueryEnabled_Type(TruthValue):
    """Custom type ppmPrinterSnmpQueryEnabled based on TruthValue"""


_PpmPrinterSnmpQueryEnabled_Object = MibTableColumn
ppmPrinterSnmpQueryEnabled = _PpmPrinterSnmpQueryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 2, 1, 1, 8),
    _PpmPrinterSnmpQueryEnabled_Type()
)
ppmPrinterSnmpQueryEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPrinterSnmpQueryEnabled.setStatus("current")
_PpmPort_ObjectIdentity = ObjectIdentity
ppmPort = _PpmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3)
)
_PpmPortTable_Object = MibTable
ppmPortTable = _PpmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ppmPortTable.setStatus("current")
_PpmPortEntry_Object = MibTableRow
ppmPortEntry = _PpmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1)
)
ppmPortEntry.setIndexNames(
    (0, "PRINTER-PORT-MONITOR-MIB", "ppmPrinterIndex"),
    (0, "PRINTER-PORT-MONITOR-MIB", "ppmPortIndex"),
)
if mibBuilder.loadTexts:
    ppmPortEntry.setStatus("current")


class _PpmPortIndex_Type(Integer32):
    """Custom type ppmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PpmPortIndex_Type.__name__ = "Integer32"
_PpmPortIndex_Object = MibTableColumn
ppmPortIndex = _PpmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 1),
    _PpmPortIndex_Type()
)
ppmPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ppmPortIndex.setStatus("current")


class _PpmPortEnabled_Type(TruthValue):
    """Custom type ppmPortEnabled based on TruthValue"""


_PpmPortEnabled_Object = MibTableColumn
ppmPortEnabled = _PpmPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 2),
    _PpmPortEnabled_Type()
)
ppmPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortEnabled.setStatus("current")


class _PpmPortName_Type(SnmpAdminString):
    """Custom type ppmPortName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PpmPortName_Type.__name__ = "SnmpAdminString"
_PpmPortName_Object = MibTableColumn
ppmPortName = _PpmPortName_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 3),
    _PpmPortName_Type()
)
ppmPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortName.setStatus("current")


class _PpmPortServiceNameOrURI_Type(SnmpAdminString):
    """Custom type ppmPortServiceNameOrURI based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PpmPortServiceNameOrURI_Type.__name__ = "SnmpAdminString"
_PpmPortServiceNameOrURI_Object = MibTableColumn
ppmPortServiceNameOrURI = _PpmPortServiceNameOrURI_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 4),
    _PpmPortServiceNameOrURI_Type()
)
ppmPortServiceNameOrURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortServiceNameOrURI.setStatus("current")


class _PpmPortProtocolType_Type(Integer32):
    """Custom type ppmPortProtocolType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PpmPortProtocolType_Type.__name__ = "Integer32"
_PpmPortProtocolType_Object = MibTableColumn
ppmPortProtocolType = _PpmPortProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 5),
    _PpmPortProtocolType_Type()
)
ppmPortProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortProtocolType.setStatus("current")


class _PpmPortProtocolTargetPort_Type(Integer32):
    """Custom type ppmPortProtocolTargetPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PpmPortProtocolTargetPort_Type.__name__ = "Integer32"
_PpmPortProtocolTargetPort_Object = MibTableColumn
ppmPortProtocolTargetPort = _PpmPortProtocolTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 6),
    _PpmPortProtocolTargetPort_Type()
)
ppmPortProtocolTargetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortProtocolTargetPort.setStatus("current")


class _PpmPortProtocolAltSourceEnabled_Type(TruthValue):
    """Custom type ppmPortProtocolAltSourceEnabled based on TruthValue"""


_PpmPortProtocolAltSourceEnabled_Object = MibTableColumn
ppmPortProtocolAltSourceEnabled = _PpmPortProtocolAltSourceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 7),
    _PpmPortProtocolAltSourceEnabled_Type()
)
ppmPortProtocolAltSourceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortProtocolAltSourceEnabled.setStatus("current")


class _PpmPortPrtChannelIndex_Type(Integer32):
    """Custom type ppmPortPrtChannelIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PpmPortPrtChannelIndex_Type.__name__ = "Integer32"
_PpmPortPrtChannelIndex_Object = MibTableColumn
ppmPortPrtChannelIndex = _PpmPortPrtChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 8),
    _PpmPortPrtChannelIndex_Type()
)
ppmPortPrtChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortPrtChannelIndex.setStatus("current")


class _PpmPortLprByteCountEnabled_Type(TruthValue):
    """Custom type ppmPortLprByteCountEnabled based on TruthValue"""


_PpmPortLprByteCountEnabled_Object = MibTableColumn
ppmPortLprByteCountEnabled = _PpmPortLprByteCountEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 1, 3, 1, 1, 9),
    _PpmPortLprByteCountEnabled_Type()
)
ppmPortLprByteCountEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppmPortLprByteCountEnabled.setStatus("current")
_PpmMIBConformance_ObjectIdentity = ObjectIdentity
ppmMIBConformance = _PpmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 2)
)
_PpmMIBObjectGroups_ObjectIdentity = ObjectIdentity
ppmMIBObjectGroups = _PpmMIBObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 2, 2)
)

# Managed Objects groups

ppmGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 2, 2, 1)
)
ppmGeneralGroup.setObjects(
      *(("PRINTER-PORT-MONITOR-MIB", "ppmGeneralNaturalLanguage"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmGeneralNumberOfPrinters"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmGeneralNumberOfPorts"))
)
if mibBuilder.loadTexts:
    ppmGeneralGroup.setStatus("current")

ppmPrinterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 2, 2, 2)
)
ppmPrinterGroup.setObjects(
      *(("PRINTER-PORT-MONITOR-MIB", "ppmPrinterName"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterIEEE1284DeviceId"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterNumberOfPorts"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterPreferredPortIndex"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterHrDeviceIndex"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterSnmpCommunityName"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPrinterSnmpQueryEnabled"))
)
if mibBuilder.loadTexts:
    ppmPrinterGroup.setStatus("current")

ppmPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 2, 2, 3)
)
ppmPortGroup.setObjects(
      *(("PRINTER-PORT-MONITOR-MIB", "ppmPortEnabled"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPortName"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPortServiceNameOrURI"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPortProtocolType"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPortProtocolTargetPort"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPortProtocolAltSourceEnabled"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPortPrtChannelIndex"),
        ("PRINTER-PORT-MONITOR-MIB", "ppmPortLprByteCountEnabled"))
)
if mibBuilder.loadTexts:
    ppmPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ppmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2699, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ppmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRINTER-PORT-MONITOR-MIB",
    **{"ppmMIB": ppmMIB,
       "ppmMIBObjects": ppmMIBObjects,
       "ppmGeneral": ppmGeneral,
       "ppmGeneralNaturalLanguage": ppmGeneralNaturalLanguage,
       "ppmGeneralNumberOfPrinters": ppmGeneralNumberOfPrinters,
       "ppmGeneralNumberOfPorts": ppmGeneralNumberOfPorts,
       "ppmPrinter": ppmPrinter,
       "ppmPrinterTable": ppmPrinterTable,
       "ppmPrinterEntry": ppmPrinterEntry,
       "ppmPrinterIndex": ppmPrinterIndex,
       "ppmPrinterName": ppmPrinterName,
       "ppmPrinterIEEE1284DeviceId": ppmPrinterIEEE1284DeviceId,
       "ppmPrinterNumberOfPorts": ppmPrinterNumberOfPorts,
       "ppmPrinterPreferredPortIndex": ppmPrinterPreferredPortIndex,
       "ppmPrinterHrDeviceIndex": ppmPrinterHrDeviceIndex,
       "ppmPrinterSnmpCommunityName": ppmPrinterSnmpCommunityName,
       "ppmPrinterSnmpQueryEnabled": ppmPrinterSnmpQueryEnabled,
       "ppmPort": ppmPort,
       "ppmPortTable": ppmPortTable,
       "ppmPortEntry": ppmPortEntry,
       "ppmPortIndex": ppmPortIndex,
       "ppmPortEnabled": ppmPortEnabled,
       "ppmPortName": ppmPortName,
       "ppmPortServiceNameOrURI": ppmPortServiceNameOrURI,
       "ppmPortProtocolType": ppmPortProtocolType,
       "ppmPortProtocolTargetPort": ppmPortProtocolTargetPort,
       "ppmPortProtocolAltSourceEnabled": ppmPortProtocolAltSourceEnabled,
       "ppmPortPrtChannelIndex": ppmPortPrtChannelIndex,
       "ppmPortLprByteCountEnabled": ppmPortLprByteCountEnabled,
       "ppmMIBConformance": ppmMIBConformance,
       "ppmMIBCompliance": ppmMIBCompliance,
       "ppmMIBObjectGroups": ppmMIBObjectGroups,
       "ppmGeneralGroup": ppmGeneralGroup,
       "ppmPrinterGroup": ppmPrinterGroup,
       "ppmPortGroup": ppmPortGroup}
)
