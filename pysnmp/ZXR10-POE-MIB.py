# SNMP MIB module (ZXR10-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-POE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:04 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10POE_ObjectIdentity = ObjectIdentity
zxr10POE = _Zxr10POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319)
)
_PseTable_Object = MibTable
pseTable = _PseTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 1)
)
if mibBuilder.loadTexts:
    pseTable.setStatus("current")
_PseEntry_Object = MibTableRow
pseEntry = _PseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1)
)
pseEntry.setIndexNames(
    (0, "ZXR10-POE-MIB", "pseGroupIndex"),
)
if mibBuilder.loadTexts:
    pseEntry.setStatus("current")


class _PseGroupIndex_Type(Integer32):
    """Custom type pseGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PseGroupIndex_Type.__name__ = "Integer32"
_PseGroupIndex_Object = MibTableColumn
pseGroupIndex = _PseGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 1),
    _PseGroupIndex_Type()
)
pseGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pseGroupIndex.setStatus("current")


class _OverTemperatureAutoRecovery_Type(Integer32):
    """Custom type overTemperatureAutoRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OverTemperatureAutoRecovery_Type.__name__ = "Integer32"
_OverTemperatureAutoRecovery_Object = MibTableColumn
overTemperatureAutoRecovery = _OverTemperatureAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 2),
    _OverTemperatureAutoRecovery_Type()
)
overTemperatureAutoRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overTemperatureAutoRecovery.setStatus("current")
_PsePeakPower_Type = DisplayString
_PsePeakPower_Object = MibTableColumn
psePeakPower = _PsePeakPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 3),
    _PsePeakPower_Type()
)
psePeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psePeakPower.setStatus("current")
if mibBuilder.loadTexts:
    psePeakPower.setUnits("Watts")
_PsePeakPowerTime_Type = DisplayString
_PsePeakPowerTime_Object = MibTableColumn
psePeakPowerTime = _PsePeakPowerTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 4),
    _PsePeakPowerTime_Type()
)
psePeakPowerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psePeakPowerTime.setStatus("current")
_PseCurrentTemperature_Type = DisplayString
_PseCurrentTemperature_Object = MibTableColumn
pseCurrentTemperature = _PseCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 5),
    _PseCurrentTemperature_Type()
)
pseCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseCurrentTemperature.setStatus("current")
_PseFirmwareVersion_Type = DisplayString
_PseFirmwareVersion_Object = MibTableColumn
pseFirmwareVersion = _PseFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 6),
    _PseFirmwareVersion_Type()
)
pseFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseFirmwareVersion.setStatus("current")
_PseCriticalPower_Type = DisplayString
_PseCriticalPower_Object = MibTableColumn
pseCriticalPower = _PseCriticalPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 1, 1, 7),
    _PseCriticalPower_Type()
)
pseCriticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pseCriticalPower.setStatus("current")
if mibBuilder.loadTexts:
    pseCriticalPower.setUnits("Watts")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1)
)
portEntry.setIndexNames(
    (0, "ZXR10-POE-MIB", "portEntryGroupIndex"),
    (0, "ZXR10-POE-MIB", "portEntryPortIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")


class _PortEntryGroupIndex_Type(Integer32):
    """Custom type portEntryGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortEntryGroupIndex_Type.__name__ = "Integer32"
_PortEntryGroupIndex_Object = MibTableColumn
portEntryGroupIndex = _PortEntryGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 1),
    _PortEntryGroupIndex_Type()
)
portEntryGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portEntryGroupIndex.setStatus("current")


class _PortEntryPortIndex_Type(Integer32):
    """Custom type portEntryPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortEntryPortIndex_Type.__name__ = "Integer32"
_PortEntryPortIndex_Object = MibTableColumn
portEntryPortIndex = _PortEntryPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 2),
    _PortEntryPortIndex_Type()
)
portEntryPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portEntryPortIndex.setStatus("current")
_InterfaceCurrentPower_Type = DisplayString
_InterfaceCurrentPower_Object = MibTableColumn
interfaceCurrentPower = _InterfaceCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 3),
    _InterfaceCurrentPower_Type()
)
interfaceCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceCurrentPower.setStatus("current")
if mibBuilder.loadTexts:
    interfaceCurrentPower.setUnits("Watts")
_InterfaceAvgPower_Type = DisplayString
_InterfaceAvgPower_Object = MibTableColumn
interfaceAvgPower = _InterfaceAvgPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 4),
    _InterfaceAvgPower_Type()
)
interfaceAvgPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceAvgPower.setStatus("current")
if mibBuilder.loadTexts:
    interfaceAvgPower.setUnits("Watts")
_InterfacePeakPower_Type = DisplayString
_InterfacePeakPower_Object = MibTableColumn
interfacePeakPower = _InterfacePeakPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 5),
    _InterfacePeakPower_Type()
)
interfacePeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacePeakPower.setStatus("current")
if mibBuilder.loadTexts:
    interfacePeakPower.setUnits("Watts")
_InterfacepeakPowerTime_Type = DisplayString
_InterfacepeakPowerTime_Object = MibTableColumn
interfacepeakPowerTime = _InterfacepeakPowerTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 6),
    _InterfacepeakPowerTime_Type()
)
interfacepeakPowerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacepeakPowerTime.setStatus("current")


class _EnhancedMode_Type(Integer32):
    """Custom type enhancedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_EnhancedMode_Type.__name__ = "Integer32"
_EnhancedMode_Object = MibTableColumn
enhancedMode = _EnhancedMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 7),
    _EnhancedMode_Type()
)
enhancedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enhancedMode.setStatus("current")


class _PdMaxPower_Type(Integer32):
    """Custom type pdMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eighteen", 3),
          ("fifteen-point-four", 0),
          ("four", 1),
          ("seven", 2),
          ("thirty", 5),
          ("twenty-seven", 4))
    )


_PdMaxPower_Type.__name__ = "Integer32"
_PdMaxPower_Object = MibTableColumn
pdMaxPower = _PdMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 319, 2, 1, 8),
    _PdMaxPower_Type()
)
pdMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdMaxPower.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-POE-MIB",
    **{"DisplayString": DisplayString,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10POE": zxr10POE,
       "pseTable": pseTable,
       "pseEntry": pseEntry,
       "pseGroupIndex": pseGroupIndex,
       "overTemperatureAutoRecovery": overTemperatureAutoRecovery,
       "psePeakPower": psePeakPower,
       "psePeakPowerTime": psePeakPowerTime,
       "pseCurrentTemperature": pseCurrentTemperature,
       "pseFirmwareVersion": pseFirmwareVersion,
       "pseCriticalPower": pseCriticalPower,
       "portTable": portTable,
       "portEntry": portEntry,
       "portEntryGroupIndex": portEntryGroupIndex,
       "portEntryPortIndex": portEntryPortIndex,
       "interfaceCurrentPower": interfaceCurrentPower,
       "interfaceAvgPower": interfaceAvgPower,
       "interfacePeakPower": interfacePeakPower,
       "interfacepeakPowerTime": interfacepeakPowerTime,
       "enhancedMode": enhancedMode,
       "pdMaxPower": pdMaxPower}
)
