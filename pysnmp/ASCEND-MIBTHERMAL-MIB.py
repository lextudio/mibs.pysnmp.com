# SNMP MIB module (ASCEND-MIBTHERMAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBTHERMAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:26 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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

_MibthermalProfile_ObjectIdentity = ObjectIdentity
mibthermalProfile = _MibthermalProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 129)
)
_MibthermalProfileTable_Object = MibTable
mibthermalProfileTable = _MibthermalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1)
)
if mibBuilder.loadTexts:
    mibthermalProfileTable.setStatus("mandatory")
_MibthermalProfileEntry_Object = MibTableRow
mibthermalProfileEntry = _MibthermalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1)
)
mibthermalProfileEntry.setIndexNames(
    (0, "ASCEND-MIBTHERMAL-MIB", "thermalProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibthermalProfileEntry.setStatus("mandatory")
_ThermalProfile_Index_o_Type = Integer32
_ThermalProfile_Index_o_Object = MibScalar
thermalProfile_Index_o = _ThermalProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 1),
    _ThermalProfile_Index_o_Type()
)
thermalProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thermalProfile_Index_o.setStatus("mandatory")
_ThermalProfile_FantrayLownoiseRpm_Type = Integer32
_ThermalProfile_FantrayLownoiseRpm_Object = MibScalar
thermalProfile_FantrayLownoiseRpm = _ThermalProfile_FantrayLownoiseRpm_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 2),
    _ThermalProfile_FantrayLownoiseRpm_Type()
)
thermalProfile_FantrayLownoiseRpm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalProfile_FantrayLownoiseRpm.setStatus("mandatory")


class _ThermalProfile_OperationMode_Type(Integer32):
    """Custom type thermalProfile_OperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoRegulation", 3),
          ("fullSpeedOnly", 1),
          ("lowNoiseSpeedOnly", 2))
    )


_ThermalProfile_OperationMode_Type.__name__ = "Integer32"
_ThermalProfile_OperationMode_Object = MibScalar
thermalProfile_OperationMode = _ThermalProfile_OperationMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 3),
    _ThermalProfile_OperationMode_Type()
)
thermalProfile_OperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalProfile_OperationMode.setStatus("mandatory")
_ThermalProfile_LowTemperatureThreshold_Type = Integer32
_ThermalProfile_LowTemperatureThreshold_Object = MibScalar
thermalProfile_LowTemperatureThreshold = _ThermalProfile_LowTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 4),
    _ThermalProfile_LowTemperatureThreshold_Type()
)
thermalProfile_LowTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalProfile_LowTemperatureThreshold.setStatus("mandatory")
_ThermalProfile_HighTemperatureThreshold_Type = Integer32
_ThermalProfile_HighTemperatureThreshold_Object = MibScalar
thermalProfile_HighTemperatureThreshold = _ThermalProfile_HighTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 5),
    _ThermalProfile_HighTemperatureThreshold_Type()
)
thermalProfile_HighTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalProfile_HighTemperatureThreshold.setStatus("mandatory")
_ThermalProfile_AlarmTemperatureTrigger_Type = Integer32
_ThermalProfile_AlarmTemperatureTrigger_Object = MibScalar
thermalProfile_AlarmTemperatureTrigger = _ThermalProfile_AlarmTemperatureTrigger_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 6),
    _ThermalProfile_AlarmTemperatureTrigger_Type()
)
thermalProfile_AlarmTemperatureTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalProfile_AlarmTemperatureTrigger.setStatus("mandatory")


class _ThermalProfile_Action_o_Type(Integer32):
    """Custom type thermalProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_ThermalProfile_Action_o_Type.__name__ = "Integer32"
_ThermalProfile_Action_o_Object = MibScalar
thermalProfile_Action_o = _ThermalProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 7),
    _ThermalProfile_Action_o_Type()
)
thermalProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalProfile_Action_o.setStatus("mandatory")
_ThermalProfile_BottomLowTemperatureThreshold_Type = Integer32
_ThermalProfile_BottomLowTemperatureThreshold_Object = MibScalar
thermalProfile_BottomLowTemperatureThreshold = _ThermalProfile_BottomLowTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 8),
    _ThermalProfile_BottomLowTemperatureThreshold_Type()
)
thermalProfile_BottomLowTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalProfile_BottomLowTemperatureThreshold.setStatus("mandatory")
_ThermalProfile_BottomHighTemperatureThreshold_Type = Integer32
_ThermalProfile_BottomHighTemperatureThreshold_Object = MibScalar
thermalProfile_BottomHighTemperatureThreshold = _ThermalProfile_BottomHighTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 9),
    _ThermalProfile_BottomHighTemperatureThreshold_Type()
)
thermalProfile_BottomHighTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalProfile_BottomHighTemperatureThreshold.setStatus("mandatory")
_ThermalProfile_TopLowTemperatureThreshold_Type = Integer32
_ThermalProfile_TopLowTemperatureThreshold_Object = MibScalar
thermalProfile_TopLowTemperatureThreshold = _ThermalProfile_TopLowTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 10),
    _ThermalProfile_TopLowTemperatureThreshold_Type()
)
thermalProfile_TopLowTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalProfile_TopLowTemperatureThreshold.setStatus("mandatory")
_ThermalProfile_TopHighTemperatureThreshold_Type = Integer32
_ThermalProfile_TopHighTemperatureThreshold_Object = MibScalar
thermalProfile_TopHighTemperatureThreshold = _ThermalProfile_TopHighTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 129, 1, 1, 11),
    _ThermalProfile_TopHighTemperatureThreshold_Type()
)
thermalProfile_TopHighTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thermalProfile_TopHighTemperatureThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBTHERMAL-MIB",
    **{"DisplayString": DisplayString,
       "mibthermalProfile": mibthermalProfile,
       "mibthermalProfileTable": mibthermalProfileTable,
       "mibthermalProfileEntry": mibthermalProfileEntry,
       "thermalProfile-Index-o": thermalProfile_Index_o,
       "thermalProfile-FantrayLownoiseRpm": thermalProfile_FantrayLownoiseRpm,
       "thermalProfile-OperationMode": thermalProfile_OperationMode,
       "thermalProfile-LowTemperatureThreshold": thermalProfile_LowTemperatureThreshold,
       "thermalProfile-HighTemperatureThreshold": thermalProfile_HighTemperatureThreshold,
       "thermalProfile-AlarmTemperatureTrigger": thermalProfile_AlarmTemperatureTrigger,
       "thermalProfile-Action-o": thermalProfile_Action_o,
       "thermalProfile-BottomLowTemperatureThreshold": thermalProfile_BottomLowTemperatureThreshold,
       "thermalProfile-BottomHighTemperatureThreshold": thermalProfile_BottomHighTemperatureThreshold,
       "thermalProfile-TopLowTemperatureThreshold": thermalProfile_TopLowTemperatureThreshold,
       "thermalProfile-TopHighTemperatureThreshold": thermalProfile_TopHighTemperatureThreshold}
)
