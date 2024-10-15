# SNMP MIB module (MBG-SNMP-XPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MBG-SNMP-XPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:37 2024
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

(mbgSnmpRoot,) = mibBuilder.importSymbols(
    "MBG-SNMP-ROOT-MIB",
    "mbgSnmpRoot")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

mbgXPT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 10)
)
mbgXPT.setRevisions(
        ("2012-01-25 00:00",
         "2006-01-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MbgGPSRefclock1_ObjectIdentity = ObjectIdentity
mbgGPSRefclock1 = _MbgGPSRefclock1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2)
)
_MbgGPSRefclock1Type_Type = DisplayString
_MbgGPSRefclock1Type_Object = MibScalar
mbgGPSRefclock1Type = _MbgGPSRefclock1Type_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2, 1),
    _MbgGPSRefclock1Type_Type()
)
mbgGPSRefclock1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRefclock1Type.setStatus("current")


class _MbgGPSRefclock1TypeVal_Type(Integer32):
    """Custom type mbgGPSRefclock1TypeVal based on Integer32"""
    defaultValue = 0


_MbgGPSRefclock1TypeVal_Object = MibScalar
mbgGPSRefclock1TypeVal = _MbgGPSRefclock1TypeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2, 2),
    _MbgGPSRefclock1TypeVal_Type()
)
mbgGPSRefclock1TypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRefclock1TypeVal.setStatus("current")
_MbgGPSRefclock1Mode_Type = DisplayString
_MbgGPSRefclock1Mode_Object = MibScalar
mbgGPSRefclock1Mode = _MbgGPSRefclock1Mode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2, 3),
    _MbgGPSRefclock1Mode_Type()
)
mbgGPSRefclock1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRefclock1Mode.setStatus("current")


class _MbgGPSRefclock1ModeVal_Type(Integer32):
    """Custom type mbgGPSRefclock1ModeVal based on Integer32"""
    defaultValue = 0


_MbgGPSRefclock1ModeVal_Object = MibScalar
mbgGPSRefclock1ModeVal = _MbgGPSRefclock1ModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2, 4),
    _MbgGPSRefclock1ModeVal_Type()
)
mbgGPSRefclock1ModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRefclock1ModeVal.setStatus("current")
_MbgGPSRef1GpsState_Type = DisplayString
_MbgGPSRef1GpsState_Object = MibScalar
mbgGPSRef1GpsState = _MbgGPSRef1GpsState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2, 5),
    _MbgGPSRef1GpsState_Type()
)
mbgGPSRef1GpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef1GpsState.setStatus("current")


class _MbgGPSRef1GpsStateVal_Type(Integer32):
    """Custom type mbgGPSRef1GpsStateVal based on Integer32"""
    defaultValue = 0


_MbgGPSRef1GpsStateVal_Object = MibScalar
mbgGPSRef1GpsStateVal = _MbgGPSRef1GpsStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2, 6),
    _MbgGPSRef1GpsStateVal_Type()
)
mbgGPSRef1GpsStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef1GpsStateVal.setStatus("current")
_MbgGPSRef1GpsPosition_Type = DisplayString
_MbgGPSRef1GpsPosition_Object = MibScalar
mbgGPSRef1GpsPosition = _MbgGPSRef1GpsPosition_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2, 7),
    _MbgGPSRef1GpsPosition_Type()
)
mbgGPSRef1GpsPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef1GpsPosition.setStatus("current")
_MbgGPSRef1GpsSatellites_Type = DisplayString
_MbgGPSRef1GpsSatellites_Object = MibScalar
mbgGPSRef1GpsSatellites = _MbgGPSRef1GpsSatellites_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2, 8),
    _MbgGPSRef1GpsSatellites_Type()
)
mbgGPSRef1GpsSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef1GpsSatellites.setStatus("current")
_MbgGPSRef1GpsSatellitesGood_Type = Integer32
_MbgGPSRef1GpsSatellitesGood_Object = MibScalar
mbgGPSRef1GpsSatellitesGood = _MbgGPSRef1GpsSatellitesGood_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2, 9),
    _MbgGPSRef1GpsSatellitesGood_Type()
)
mbgGPSRef1GpsSatellitesGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef1GpsSatellitesGood.setStatus("current")
_MbgGPSRef1GpsSatellitesInView_Type = Integer32
_MbgGPSRef1GpsSatellitesInView_Object = MibScalar
mbgGPSRef1GpsSatellitesInView = _MbgGPSRef1GpsSatellitesInView_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 2, 10),
    _MbgGPSRef1GpsSatellitesInView_Type()
)
mbgGPSRef1GpsSatellitesInView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef1GpsSatellitesInView.setStatus("current")
_MbgGPSRefclock2_ObjectIdentity = ObjectIdentity
mbgGPSRefclock2 = _MbgGPSRefclock2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3)
)
_MbgGPSRefclock2Type_Type = DisplayString
_MbgGPSRefclock2Type_Object = MibScalar
mbgGPSRefclock2Type = _MbgGPSRefclock2Type_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3, 1),
    _MbgGPSRefclock2Type_Type()
)
mbgGPSRefclock2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRefclock2Type.setStatus("current")


class _MbgGPSRefclock2TypeVal_Type(Integer32):
    """Custom type mbgGPSRefclock2TypeVal based on Integer32"""
    defaultValue = 0


_MbgGPSRefclock2TypeVal_Object = MibScalar
mbgGPSRefclock2TypeVal = _MbgGPSRefclock2TypeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3, 2),
    _MbgGPSRefclock2TypeVal_Type()
)
mbgGPSRefclock2TypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRefclock2TypeVal.setStatus("current")
_MbgGPSRefclock2Mode_Type = DisplayString
_MbgGPSRefclock2Mode_Object = MibScalar
mbgGPSRefclock2Mode = _MbgGPSRefclock2Mode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3, 3),
    _MbgGPSRefclock2Mode_Type()
)
mbgGPSRefclock2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRefclock2Mode.setStatus("current")


class _MbgGPSRefclock2ModeVal_Type(Integer32):
    """Custom type mbgGPSRefclock2ModeVal based on Integer32"""
    defaultValue = 0


_MbgGPSRefclock2ModeVal_Object = MibScalar
mbgGPSRefclock2ModeVal = _MbgGPSRefclock2ModeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3, 4),
    _MbgGPSRefclock2ModeVal_Type()
)
mbgGPSRefclock2ModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRefclock2ModeVal.setStatus("current")
_MbgGPSRef2GpsState_Type = DisplayString
_MbgGPSRef2GpsState_Object = MibScalar
mbgGPSRef2GpsState = _MbgGPSRef2GpsState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3, 5),
    _MbgGPSRef2GpsState_Type()
)
mbgGPSRef2GpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef2GpsState.setStatus("current")


class _MbgGPSRef2GpsStateVal_Type(Integer32):
    """Custom type mbgGPSRef2GpsStateVal based on Integer32"""
    defaultValue = 0


_MbgGPSRef2GpsStateVal_Object = MibScalar
mbgGPSRef2GpsStateVal = _MbgGPSRef2GpsStateVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3, 6),
    _MbgGPSRef2GpsStateVal_Type()
)
mbgGPSRef2GpsStateVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef2GpsStateVal.setStatus("current")
_MbgGPSRef2GpsPosition_Type = DisplayString
_MbgGPSRef2GpsPosition_Object = MibScalar
mbgGPSRef2GpsPosition = _MbgGPSRef2GpsPosition_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3, 7),
    _MbgGPSRef2GpsPosition_Type()
)
mbgGPSRef2GpsPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef2GpsPosition.setStatus("current")
_MbgGPSRef2GpsSatellites_Type = DisplayString
_MbgGPSRef2GpsSatellites_Object = MibScalar
mbgGPSRef2GpsSatellites = _MbgGPSRef2GpsSatellites_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3, 8),
    _MbgGPSRef2GpsSatellites_Type()
)
mbgGPSRef2GpsSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef2GpsSatellites.setStatus("current")
_MbgGPSRef2GpsSatellitesGood_Type = Integer32
_MbgGPSRef2GpsSatellitesGood_Object = MibScalar
mbgGPSRef2GpsSatellitesGood = _MbgGPSRef2GpsSatellitesGood_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3, 9),
    _MbgGPSRef2GpsSatellitesGood_Type()
)
mbgGPSRef2GpsSatellitesGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef2GpsSatellitesGood.setStatus("current")
_MbgGPSRef2GpsSatellitesInView_Type = Integer32
_MbgGPSRef2GpsSatellitesInView_Object = MibScalar
mbgGPSRef2GpsSatellitesInView = _MbgGPSRef2GpsSatellitesInView_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 3, 10),
    _MbgGPSRef2GpsSatellitesInView_Type()
)
mbgGPSRef2GpsSatellitesInView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSRef2GpsSatellitesInView.setStatus("current")
_MbgSCU_ObjectIdentity = ObjectIdentity
mbgSCU = _MbgSCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4)
)
_MbgSCUType_Type = DisplayString
_MbgSCUType_Object = MibScalar
mbgSCUType = _MbgSCUType_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 1),
    _MbgSCUType_Type()
)
mbgSCUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUType.setStatus("current")


class _MbgSCUTypeVal_Type(Integer32):
    """Custom type mbgSCUTypeVal based on Integer32"""
    defaultValue = 0


_MbgSCUTypeVal_Object = MibScalar
mbgSCUTypeVal = _MbgSCUTypeVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 2),
    _MbgSCUTypeVal_Type()
)
mbgSCUTypeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUTypeVal.setStatus("current")
_MbgSCUMaster_Type = DisplayString
_MbgSCUMaster_Object = MibScalar
mbgSCUMaster = _MbgSCUMaster_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 3),
    _MbgSCUMaster_Type()
)
mbgSCUMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUMaster.setStatus("current")


class _MbgSCUMasterVal_Type(Integer32):
    """Custom type mbgSCUMasterVal based on Integer32"""
    defaultValue = 0


_MbgSCUMasterVal_Object = MibScalar
mbgSCUMasterVal = _MbgSCUMasterVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 4),
    _MbgSCUMasterVal_Type()
)
mbgSCUMasterVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUMasterVal.setStatus("current")
_MbgSCUMasterselect_Type = DisplayString
_MbgSCUMasterselect_Object = MibScalar
mbgSCUMasterselect = _MbgSCUMasterselect_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 5),
    _MbgSCUMasterselect_Type()
)
mbgSCUMasterselect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUMasterselect.setStatus("current")


class _MbgSCUMasterselectVal_Type(Integer32):
    """Custom type mbgSCUMasterselectVal based on Integer32"""
    defaultValue = 0


_MbgSCUMasterselectVal_Object = MibScalar
mbgSCUMasterselectVal = _MbgSCUMasterselectVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 6),
    _MbgSCUMasterselectVal_Type()
)
mbgSCUMasterselectVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUMasterselectVal.setStatus("current")
_MbgSCUTimeSync1_Type = Integer32
_MbgSCUTimeSync1_Object = MibScalar
mbgSCUTimeSync1 = _MbgSCUTimeSync1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 7),
    _MbgSCUTimeSync1_Type()
)
mbgSCUTimeSync1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUTimeSync1.setStatus("current")
_MbgSCUTimeSync2_Type = Integer32
_MbgSCUTimeSync2_Object = MibScalar
mbgSCUTimeSync2 = _MbgSCUTimeSync2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 8),
    _MbgSCUTimeSync2_Type()
)
mbgSCUTimeSync2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUTimeSync2.setStatus("current")
_MbgSCUTimelimitError_Type = Integer32
_MbgSCUTimelimitError_Object = MibScalar
mbgSCUTimelimitError = _MbgSCUTimelimitError_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 9),
    _MbgSCUTimelimitError_Type()
)
mbgSCUTimelimitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUTimelimitError.setStatus("current")
_MbgSCUDisableOutputs_Type = Integer32
_MbgSCUDisableOutputs_Object = MibScalar
mbgSCUDisableOutputs = _MbgSCUDisableOutputs_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 10),
    _MbgSCUDisableOutputs_Type()
)
mbgSCUDisableOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUDisableOutputs.setStatus("current")
_MbgSCUSelectedInput_Type = DisplayString
_MbgSCUSelectedInput_Object = MibScalar
mbgSCUSelectedInput = _MbgSCUSelectedInput_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 11),
    _MbgSCUSelectedInput_Type()
)
mbgSCUSelectedInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUSelectedInput.setStatus("current")
_MbgSCUSelectedInputVal_Type = Integer32
_MbgSCUSelectedInputVal_Object = MibScalar
mbgSCUSelectedInputVal = _MbgSCUSelectedInputVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 12),
    _MbgSCUSelectedInputVal_Type()
)
mbgSCUSelectedInputVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUSelectedInputVal.setStatus("current")
_MbgSCUACOMode_Type = Integer32
_MbgSCUACOMode_Object = MibScalar
mbgSCUACOMode = _MbgSCUACOMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 13),
    _MbgSCUACOMode_Type()
)
mbgSCUACOMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUACOMode.setStatus("current")
_MbgSCUPSUStatus_Type = DisplayString
_MbgSCUPSUStatus_Object = MibScalar
mbgSCUPSUStatus = _MbgSCUPSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 14),
    _MbgSCUPSUStatus_Type()
)
mbgSCUPSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUPSUStatus.setStatus("current")
_MbgSCUPSU1Status_Type = Integer32
_MbgSCUPSU1Status_Object = MibScalar
mbgSCUPSU1Status = _MbgSCUPSU1Status_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 15),
    _MbgSCUPSU1Status_Type()
)
mbgSCUPSU1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUPSU1Status.setStatus("current")
_MbgSCUPSU2Status_Type = Integer32
_MbgSCUPSU2Status_Object = MibScalar
mbgSCUPSU2Status = _MbgSCUPSU2Status_Object(
    (1, 3, 6, 1, 4, 1, 5597, 10, 4, 16),
    _MbgSCUPSU2Status_Type()
)
mbgSCUPSU2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUPSU2Status.setStatus("current")
_MbgXPTTraps_ObjectIdentity = ObjectIdentity
mbgXPTTraps = _MbgXPTTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5)
)
_MbgXPTConformance_ObjectIdentity = ObjectIdentity
mbgXPTConformance = _MbgXPTConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 10, 90)
)
_MbgXPTCompliances_ObjectIdentity = ObjectIdentity
mbgXPTCompliances = _MbgXPTCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 10, 90, 1)
)
_MbgXPTGroups_ObjectIdentity = ObjectIdentity
mbgXPTGroups = _MbgXPTGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 10, 90, 2)
)

# Managed Objects groups

mbgXPTObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5597, 10, 90, 2, 1)
)
mbgXPTObjectsGroup.setObjects(
      *(("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1Type"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1TypeVal"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1Mode"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock1ModeVal"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsState"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsStateVal"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsPosition"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsSatellites"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsSatellitesGood"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef1GpsSatellitesInView"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2Type"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2TypeVal"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2Mode"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRefclock2ModeVal"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsState"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsStateVal"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsPosition"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsSatellites"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsSatellitesGood"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSRef2GpsSatellitesInView"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUType"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUTypeVal"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUMaster"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUMasterVal"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUMasterselect"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUMasterselectVal"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUTimeSync1"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUTimeSync2"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUTimelimitError"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUDisableOutputs"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUSelectedInput"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUSelectedInputVal"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUACOMode"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUPSUStatus"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUPSU1Status"),
        ("MBG-SNMP-XPT-MIB", "mbgSCUPSU2Status"))
)
if mibBuilder.loadTexts:
    mbgXPTObjectsGroup.setStatus("current")


# Notification objects

mbgGPSTrapColdBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 1)
)
if mibBuilder.loadTexts:
    mbgGPSTrapColdBoot.setStatus(
        "current"
    )

mbgGPSTrapWarmBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 2)
)
if mibBuilder.loadTexts:
    mbgGPSTrapWarmBoot.setStatus(
        "current"
    )

mbgGPSNavSolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 3)
)
if mibBuilder.loadTexts:
    mbgGPSNavSolved.setStatus(
        "current"
    )

mbgGPSTrapReceiverNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 4)
)
if mibBuilder.loadTexts:
    mbgGPSTrapReceiverNotResponding.setStatus(
        "current"
    )

mbgGPSTrapReceiverNotSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 5)
)
if mibBuilder.loadTexts:
    mbgGPSTrapReceiverNotSync.setStatus(
        "current"
    )

mbgGPSTrapAntennaFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 6)
)
if mibBuilder.loadTexts:
    mbgGPSTrapAntennaFaulty.setStatus(
        "current"
    )

mbgGPSTrapAntennaReconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 7)
)
if mibBuilder.loadTexts:
    mbgGPSTrapAntennaReconnect.setStatus(
        "current"
    )

mbgGPSTrapLANXPTBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 8)
)
if mibBuilder.loadTexts:
    mbgGPSTrapLANXPTBoot.setStatus(
        "current"
    )

mbgGPSTrapLeapSecondAnnounced = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 9)
)
if mibBuilder.loadTexts:
    mbgGPSTrapLeapSecondAnnounced.setStatus(
        "current"
    )

mbgGPSTrapMasterclockSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 10)
)
if mibBuilder.loadTexts:
    mbgGPSTrapMasterclockSwitchover.setStatus(
        "current"
    )

mbgGPSTrapPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 11)
)
if mibBuilder.loadTexts:
    mbgGPSTrapPowerSupplyFailure.setStatus(
        "current"
    )

mbgGPSTrapPowerSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 12)
)
if mibBuilder.loadTexts:
    mbgGPSTrapPowerSupplyOK.setStatus(
        "current"
    )

mbgGPSTrapTestNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 10, 5, 99)
)
if mibBuilder.loadTexts:
    mbgGPSTrapTestNotification.setStatus(
        "current"
    )


# Notifications groups

mbgXPTTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5597, 10, 90, 2, 2)
)
mbgXPTTrapsGroup.setObjects(
      *(("MBG-SNMP-XPT-MIB", "mbgGPSTrapColdBoot"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapWarmBoot"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSNavSolved"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapReceiverNotResponding"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapReceiverNotSync"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapAntennaFaulty"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapAntennaReconnect"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapLANXPTBoot"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapLeapSecondAnnounced"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapMasterclockSwitchover"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapPowerSupplyFailure"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapPowerSupplyOK"),
        ("MBG-SNMP-XPT-MIB", "mbgGPSTrapTestNotification"))
)
if mibBuilder.loadTexts:
    mbgXPTTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mbgXPTCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5597, 10, 90, 1, 1)
)
if mibBuilder.loadTexts:
    mbgXPTCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MBG-SNMP-XPT-MIB",
    **{"mbgXPT": mbgXPT,
       "mbgGPSRefclock1": mbgGPSRefclock1,
       "mbgGPSRefclock1Type": mbgGPSRefclock1Type,
       "mbgGPSRefclock1TypeVal": mbgGPSRefclock1TypeVal,
       "mbgGPSRefclock1Mode": mbgGPSRefclock1Mode,
       "mbgGPSRefclock1ModeVal": mbgGPSRefclock1ModeVal,
       "mbgGPSRef1GpsState": mbgGPSRef1GpsState,
       "mbgGPSRef1GpsStateVal": mbgGPSRef1GpsStateVal,
       "mbgGPSRef1GpsPosition": mbgGPSRef1GpsPosition,
       "mbgGPSRef1GpsSatellites": mbgGPSRef1GpsSatellites,
       "mbgGPSRef1GpsSatellitesGood": mbgGPSRef1GpsSatellitesGood,
       "mbgGPSRef1GpsSatellitesInView": mbgGPSRef1GpsSatellitesInView,
       "mbgGPSRefclock2": mbgGPSRefclock2,
       "mbgGPSRefclock2Type": mbgGPSRefclock2Type,
       "mbgGPSRefclock2TypeVal": mbgGPSRefclock2TypeVal,
       "mbgGPSRefclock2Mode": mbgGPSRefclock2Mode,
       "mbgGPSRefclock2ModeVal": mbgGPSRefclock2ModeVal,
       "mbgGPSRef2GpsState": mbgGPSRef2GpsState,
       "mbgGPSRef2GpsStateVal": mbgGPSRef2GpsStateVal,
       "mbgGPSRef2GpsPosition": mbgGPSRef2GpsPosition,
       "mbgGPSRef2GpsSatellites": mbgGPSRef2GpsSatellites,
       "mbgGPSRef2GpsSatellitesGood": mbgGPSRef2GpsSatellitesGood,
       "mbgGPSRef2GpsSatellitesInView": mbgGPSRef2GpsSatellitesInView,
       "mbgSCU": mbgSCU,
       "mbgSCUType": mbgSCUType,
       "mbgSCUTypeVal": mbgSCUTypeVal,
       "mbgSCUMaster": mbgSCUMaster,
       "mbgSCUMasterVal": mbgSCUMasterVal,
       "mbgSCUMasterselect": mbgSCUMasterselect,
       "mbgSCUMasterselectVal": mbgSCUMasterselectVal,
       "mbgSCUTimeSync1": mbgSCUTimeSync1,
       "mbgSCUTimeSync2": mbgSCUTimeSync2,
       "mbgSCUTimelimitError": mbgSCUTimelimitError,
       "mbgSCUDisableOutputs": mbgSCUDisableOutputs,
       "mbgSCUSelectedInput": mbgSCUSelectedInput,
       "mbgSCUSelectedInputVal": mbgSCUSelectedInputVal,
       "mbgSCUACOMode": mbgSCUACOMode,
       "mbgSCUPSUStatus": mbgSCUPSUStatus,
       "mbgSCUPSU1Status": mbgSCUPSU1Status,
       "mbgSCUPSU2Status": mbgSCUPSU2Status,
       "mbgXPTTraps": mbgXPTTraps,
       "mbgGPSTrapColdBoot": mbgGPSTrapColdBoot,
       "mbgGPSTrapWarmBoot": mbgGPSTrapWarmBoot,
       "mbgGPSNavSolved": mbgGPSNavSolved,
       "mbgGPSTrapReceiverNotResponding": mbgGPSTrapReceiverNotResponding,
       "mbgGPSTrapReceiverNotSync": mbgGPSTrapReceiverNotSync,
       "mbgGPSTrapAntennaFaulty": mbgGPSTrapAntennaFaulty,
       "mbgGPSTrapAntennaReconnect": mbgGPSTrapAntennaReconnect,
       "mbgGPSTrapLANXPTBoot": mbgGPSTrapLANXPTBoot,
       "mbgGPSTrapLeapSecondAnnounced": mbgGPSTrapLeapSecondAnnounced,
       "mbgGPSTrapMasterclockSwitchover": mbgGPSTrapMasterclockSwitchover,
       "mbgGPSTrapPowerSupplyFailure": mbgGPSTrapPowerSupplyFailure,
       "mbgGPSTrapPowerSupplyOK": mbgGPSTrapPowerSupplyOK,
       "mbgGPSTrapTestNotification": mbgGPSTrapTestNotification,
       "mbgXPTConformance": mbgXPTConformance,
       "mbgXPTCompliances": mbgXPTCompliances,
       "mbgXPTCompliance": mbgXPTCompliance,
       "mbgXPTGroups": mbgXPTGroups,
       "mbgXPTObjectsGroup": mbgXPTObjectsGroup,
       "mbgXPTTrapsGroup": mbgXPTTrapsGroup}
)
