# SNMP MIB module (IMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IMM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:03 2024
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
 NotificationType,
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
    "NotificationType",
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



class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



class InetAddressIPv6(OctetString, TextualConvention):
    status = "mandatory"
    displayHint = "02x:02x:02x:02x:02x:02x:02x:02x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmAgents_ObjectIdentity = ObjectIdentity
ibmAgents = _IbmAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3)
)
_NetfinitySupportProcessorAgent_ObjectIdentity = ObjectIdentity
netfinitySupportProcessorAgent = _NetfinitySupportProcessorAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51)
)
_IbmIntegratedManagementModuleMIB_ObjectIdentity = ObjectIdentity
ibmIntegratedManagementModuleMIB = _IbmIntegratedManagementModuleMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3)
)
_Monitors_ObjectIdentity = ObjectIdentity
monitors = _Monitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1)
)
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1)
)
_TempNumber_Type = Gauge32
_TempNumber_Object = MibScalar
tempNumber = _TempNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 1),
    _TempNumber_Type()
)
tempNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNumber.setStatus("mandatory")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("mandatory")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1)
)
tempEntry.setIndexNames(
    (0, "IMM-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("mandatory")


class _TempIndex_Type(Integer32):
    """Custom type tempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TempIndex_Type.__name__ = "Integer32"
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempIndex.setStatus("mandatory")


class _TempDescr_Type(DisplayString):
    """Custom type tempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempDescr_Type.__name__ = "DisplayString"
_TempDescr_Object = MibTableColumn
tempDescr = _TempDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 2),
    _TempDescr_Type()
)
tempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDescr.setStatus("mandatory")
_TempReading_Type = Integer32
_TempReading_Object = MibTableColumn
tempReading = _TempReading_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 3),
    _TempReading_Type()
)
tempReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempReading.setUnits("Degrees Celsius")
_TempNominalReading_Type = Integer32
_TempNominalReading_Object = MibTableColumn
tempNominalReading = _TempNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 4),
    _TempNominalReading_Type()
)
tempNominalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNominalReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempNominalReading.setUnits("Degrees Celsius")
_TempNonRecovLimitHigh_Type = Integer32
_TempNonRecovLimitHigh_Object = MibTableColumn
tempNonRecovLimitHigh = _TempNonRecovLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 5),
    _TempNonRecovLimitHigh_Type()
)
tempNonRecovLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNonRecovLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempNonRecovLimitHigh.setUnits("Degrees Celsius")
_TempCritLimitHigh_Type = Integer32
_TempCritLimitHigh_Object = MibTableColumn
tempCritLimitHigh = _TempCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 6),
    _TempCritLimitHigh_Type()
)
tempCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempCritLimitHigh.setUnits("Degrees Celsius")
_TempNonCritLimitHigh_Type = Integer32
_TempNonCritLimitHigh_Object = MibTableColumn
tempNonCritLimitHigh = _TempNonCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 7),
    _TempNonCritLimitHigh_Type()
)
tempNonCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNonCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempNonCritLimitHigh.setUnits("Degrees Celsius")
_TempNonRecovLimitLow_Type = Integer32
_TempNonRecovLimitLow_Object = MibTableColumn
tempNonRecovLimitLow = _TempNonRecovLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 8),
    _TempNonRecovLimitLow_Type()
)
tempNonRecovLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNonRecovLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempNonRecovLimitLow.setUnits("Degrees Celsius")
_TempCritLimitLow_Type = Integer32
_TempCritLimitLow_Object = MibTableColumn
tempCritLimitLow = _TempCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 9),
    _TempCritLimitLow_Type()
)
tempCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempCritLimitLow.setUnits("Degrees Celsius")
_TempNonCritLimitLow_Type = Integer32
_TempNonCritLimitLow_Object = MibTableColumn
tempNonCritLimitLow = _TempNonCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 10),
    _TempNonCritLimitLow_Type()
)
tempNonCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNonCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempNonCritLimitLow.setUnits("Degrees Celsius")


class _TempHealthStatus_Type(DisplayString):
    """Custom type tempHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TempHealthStatus_Type.__name__ = "DisplayString"
_TempHealthStatus_Object = MibTableColumn
tempHealthStatus = _TempHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 1, 2, 1, 11),
    _TempHealthStatus_Type()
)
tempHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHealthStatus.setStatus("mandatory")
_Voltage_ObjectIdentity = ObjectIdentity
voltage = _Voltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2)
)
_VoltNumber_Type = Gauge32
_VoltNumber_Object = MibScalar
voltNumber = _VoltNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 1),
    _VoltNumber_Type()
)
voltNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNumber.setStatus("mandatory")
_VoltTable_Object = MibTable
voltTable = _VoltTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    voltTable.setStatus("mandatory")
_VoltEntry_Object = MibTableRow
voltEntry = _VoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1)
)
voltEntry.setIndexNames(
    (0, "IMM-MIB", "voltIndex"),
)
if mibBuilder.loadTexts:
    voltEntry.setStatus("mandatory")


class _VoltIndex_Type(Integer32):
    """Custom type voltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VoltIndex_Type.__name__ = "Integer32"
_VoltIndex_Object = MibTableColumn
voltIndex = _VoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 1),
    _VoltIndex_Type()
)
voltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltIndex.setStatus("mandatory")


class _VoltDescr_Type(DisplayString):
    """Custom type voltDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltDescr_Type.__name__ = "DisplayString"
_VoltDescr_Object = MibTableColumn
voltDescr = _VoltDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 2),
    _VoltDescr_Type()
)
voltDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltDescr.setStatus("mandatory")
_VoltReading_Type = Integer32
_VoltReading_Object = MibTableColumn
voltReading = _VoltReading_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 3),
    _VoltReading_Type()
)
voltReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltReading.setUnits("Millivolts")
_VoltNominalReading_Type = Integer32
_VoltNominalReading_Object = MibTableColumn
voltNominalReading = _VoltNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 4),
    _VoltNominalReading_Type()
)
voltNominalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNominalReading.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltNominalReading.setUnits("Millivolts")
_VoltNonRecovLimitHigh_Type = Integer32
_VoltNonRecovLimitHigh_Object = MibTableColumn
voltNonRecovLimitHigh = _VoltNonRecovLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 5),
    _VoltNonRecovLimitHigh_Type()
)
voltNonRecovLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNonRecovLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltNonRecovLimitHigh.setUnits("Millivolts")
_VoltCritLimitHigh_Type = Integer32
_VoltCritLimitHigh_Object = MibTableColumn
voltCritLimitHigh = _VoltCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 6),
    _VoltCritLimitHigh_Type()
)
voltCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltCritLimitHigh.setUnits("Millivolts")
_VoltNonCritLimitHigh_Type = Integer32
_VoltNonCritLimitHigh_Object = MibTableColumn
voltNonCritLimitHigh = _VoltNonCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 7),
    _VoltNonCritLimitHigh_Type()
)
voltNonCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNonCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltNonCritLimitHigh.setUnits("Millivolts")
_VoltNonRecovLimitLow_Type = Integer32
_VoltNonRecovLimitLow_Object = MibTableColumn
voltNonRecovLimitLow = _VoltNonRecovLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 8),
    _VoltNonRecovLimitLow_Type()
)
voltNonRecovLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNonRecovLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltNonRecovLimitLow.setUnits("Millivolts")
_VoltCritLimitLow_Type = Integer32
_VoltCritLimitLow_Object = MibTableColumn
voltCritLimitLow = _VoltCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 9),
    _VoltCritLimitLow_Type()
)
voltCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltCritLimitLow.setUnits("Millivolts")
_VoltNonCritLimitLow_Type = Integer32
_VoltNonCritLimitLow_Object = MibTableColumn
voltNonCritLimitLow = _VoltNonCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 10),
    _VoltNonCritLimitLow_Type()
)
voltNonCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltNonCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    voltNonCritLimitLow.setUnits("Millivolts")


class _VoltHealthStatus_Type(DisplayString):
    """Custom type voltHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_VoltHealthStatus_Type.__name__ = "DisplayString"
_VoltHealthStatus_Object = MibTableColumn
voltHealthStatus = _VoltHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 2, 2, 1, 11),
    _VoltHealthStatus_Type()
)
voltHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltHealthStatus.setStatus("mandatory")
_Fans_ObjectIdentity = ObjectIdentity
fans = _Fans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3)
)
_FanNumber_Type = Gauge32
_FanNumber_Object = MibScalar
fanNumber = _FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 1),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumber.setStatus("mandatory")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("mandatory")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1)
)
fanEntry.setIndexNames(
    (0, "IMM-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("mandatory")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("mandatory")


class _FanDescr_Type(DisplayString):
    """Custom type fanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FanDescr_Type.__name__ = "DisplayString"
_FanDescr_Object = MibTableColumn
fanDescr = _FanDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1, 2),
    _FanDescr_Type()
)
fanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDescr.setStatus("mandatory")
_FanSpeed_Type = OctetString
_FanSpeed_Object = MibTableColumn
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1, 3),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("mandatory")
_FanNonRecovLimitHigh_Type = Integer32
_FanNonRecovLimitHigh_Object = MibTableColumn
fanNonRecovLimitHigh = _FanNonRecovLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1, 4),
    _FanNonRecovLimitHigh_Type()
)
fanNonRecovLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNonRecovLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanNonRecovLimitHigh.setUnits("RPM")
_FanCritLimitHigh_Type = Integer32
_FanCritLimitHigh_Object = MibTableColumn
fanCritLimitHigh = _FanCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1, 5),
    _FanCritLimitHigh_Type()
)
fanCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanCritLimitHigh.setUnits("RPM")
_FanNonCritLimitHigh_Type = Integer32
_FanNonCritLimitHigh_Object = MibTableColumn
fanNonCritLimitHigh = _FanNonCritLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1, 6),
    _FanNonCritLimitHigh_Type()
)
fanNonCritLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNonCritLimitHigh.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanNonCritLimitHigh.setUnits("RPM")
_FanNonRecovLimitLow_Type = Integer32
_FanNonRecovLimitLow_Object = MibTableColumn
fanNonRecovLimitLow = _FanNonRecovLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1, 7),
    _FanNonRecovLimitLow_Type()
)
fanNonRecovLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNonRecovLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanNonRecovLimitLow.setUnits("RPM")
_FanCritLimitLow_Type = Integer32
_FanCritLimitLow_Object = MibTableColumn
fanCritLimitLow = _FanCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1, 8),
    _FanCritLimitLow_Type()
)
fanCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanCritLimitLow.setUnits("RPM")
_FanNonCritLimitLow_Type = Integer32
_FanNonCritLimitLow_Object = MibTableColumn
fanNonCritLimitLow = _FanNonCritLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1, 9),
    _FanNonCritLimitLow_Type()
)
fanNonCritLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNonCritLimitLow.setStatus("mandatory")
if mibBuilder.loadTexts:
    fanNonCritLimitLow.setUnits("RPM")


class _FanHealthStatus_Type(DisplayString):
    """Custom type fanHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FanHealthStatus_Type.__name__ = "DisplayString"
_FanHealthStatus_Object = MibTableColumn
fanHealthStatus = _FanHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 3, 2, 1, 10),
    _FanHealthStatus_Type()
)
fanHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanHealthStatus.setStatus("mandatory")
_SystemHealth_ObjectIdentity = ObjectIdentity
systemHealth = _SystemHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 4)
)


class _SystemHealthStat_Type(Integer32):
    """Custom type systemHealthStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("nonCritical", 4),
          ("nonRecoverable", 0),
          ("normal", 255))
    )


_SystemHealthStat_Type.__name__ = "Integer32"
_SystemHealthStat_Object = MibScalar
systemHealthStat = _SystemHealthStat_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 4, 1),
    _SystemHealthStat_Type()
)
systemHealthStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthStat.setStatus("mandatory")
_SystemHealthSummaryTable_Object = MibTable
systemHealthSummaryTable = _SystemHealthSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    systemHealthSummaryTable.setStatus("mandatory")
_SystemHealthSummaryEntry_Object = MibTableRow
systemHealthSummaryEntry = _SystemHealthSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 4, 2, 1)
)
systemHealthSummaryEntry.setIndexNames(
    (0, "IMM-MIB", "systemHealthSummaryIndex"),
)
if mibBuilder.loadTexts:
    systemHealthSummaryEntry.setStatus("mandatory")


class _SystemHealthSummaryIndex_Type(Integer32):
    """Custom type systemHealthSummaryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SystemHealthSummaryIndex_Type.__name__ = "Integer32"
_SystemHealthSummaryIndex_Object = MibTableColumn
systemHealthSummaryIndex = _SystemHealthSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 4, 2, 1, 1),
    _SystemHealthSummaryIndex_Type()
)
systemHealthSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthSummaryIndex.setStatus("mandatory")
_SystemHealthSummarySeverity_Type = OctetString
_SystemHealthSummarySeverity_Object = MibTableColumn
systemHealthSummarySeverity = _SystemHealthSummarySeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 4, 2, 1, 2),
    _SystemHealthSummarySeverity_Type()
)
systemHealthSummarySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthSummarySeverity.setStatus("mandatory")
_SystemHealthSummaryDescription_Type = OctetString
_SystemHealthSummaryDescription_Object = MibTableColumn
systemHealthSummaryDescription = _SystemHealthSummaryDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 4, 2, 1, 3),
    _SystemHealthSummaryDescription_Type()
)
systemHealthSummaryDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHealthSummaryDescription.setStatus("mandatory")
_VpdInformation_ObjectIdentity = ObjectIdentity
vpdInformation = _VpdInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5)
)
_ImmVpdTable_Object = MibTable
immVpdTable = _ImmVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    immVpdTable.setStatus("mandatory")
_ImmVpdEntry_Object = MibTableRow
immVpdEntry = _ImmVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 1, 1)
)
immVpdEntry.setIndexNames(
    (0, "IMM-MIB", "immVpdIndex"),
)
if mibBuilder.loadTexts:
    immVpdEntry.setStatus("mandatory")


class _ImmVpdIndex_Type(Integer32):
    """Custom type immVpdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ImmVpdIndex_Type.__name__ = "Integer32"
_ImmVpdIndex_Object = MibTableColumn
immVpdIndex = _ImmVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 1, 1, 1),
    _ImmVpdIndex_Type()
)
immVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    immVpdIndex.setStatus("mandatory")
_ImmVpdType_Type = OctetString
_ImmVpdType_Object = MibTableColumn
immVpdType = _ImmVpdType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 1, 1, 2),
    _ImmVpdType_Type()
)
immVpdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    immVpdType.setStatus("mandatory")
_ImmVpdVersionString_Type = OctetString
_ImmVpdVersionString_Object = MibTableColumn
immVpdVersionString = _ImmVpdVersionString_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 1, 1, 3),
    _ImmVpdVersionString_Type()
)
immVpdVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    immVpdVersionString.setStatus("mandatory")
_ImmVpdReleaseDate_Type = OctetString
_ImmVpdReleaseDate_Object = MibTableColumn
immVpdReleaseDate = _ImmVpdReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 1, 1, 4),
    _ImmVpdReleaseDate_Type()
)
immVpdReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    immVpdReleaseDate.setStatus("mandatory")
_MachineVpd_ObjectIdentity = ObjectIdentity
machineVpd = _MachineVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 2)
)
_MachineLevelVpd_ObjectIdentity = ObjectIdentity
machineLevelVpd = _MachineLevelVpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 2, 1)
)
_MachineLevelVpdMachineType_Type = OctetString
_MachineLevelVpdMachineType_Object = MibScalar
machineLevelVpdMachineType = _MachineLevelVpdMachineType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 2, 1, 1),
    _MachineLevelVpdMachineType_Type()
)
machineLevelVpdMachineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLevelVpdMachineType.setStatus("mandatory")
_MachineLevelVpdMachineModel_Type = OctetString
_MachineLevelVpdMachineModel_Object = MibScalar
machineLevelVpdMachineModel = _MachineLevelVpdMachineModel_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 2, 1, 2),
    _MachineLevelVpdMachineModel_Type()
)
machineLevelVpdMachineModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLevelVpdMachineModel.setStatus("mandatory")
_MachineLevelSerialNumber_Type = OctetString
_MachineLevelSerialNumber_Object = MibScalar
machineLevelSerialNumber = _MachineLevelSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 2, 1, 3),
    _MachineLevelSerialNumber_Type()
)
machineLevelSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLevelSerialNumber.setStatus("mandatory")
_MachineLevelUUID_Type = OctetString
_MachineLevelUUID_Object = MibScalar
machineLevelUUID = _MachineLevelUUID_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 2, 1, 4),
    _MachineLevelUUID_Type()
)
machineLevelUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLevelUUID.setStatus("mandatory")
_MachineLevelProductName_Type = OctetString
_MachineLevelProductName_Object = MibScalar
machineLevelProductName = _MachineLevelProductName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 2, 1, 5),
    _MachineLevelProductName_Type()
)
machineLevelProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineLevelProductName.setStatus("mandatory")
_SystemComponentLevelVpdTable_Object = MibTable
systemComponentLevelVpdTable = _SystemComponentLevelVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 17)
)
if mibBuilder.loadTexts:
    systemComponentLevelVpdTable.setStatus("mandatory")
_SystemComponentLevelVpdEntry_Object = MibTableRow
systemComponentLevelVpdEntry = _SystemComponentLevelVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 17, 1)
)
systemComponentLevelVpdEntry.setIndexNames(
    (0, "IMM-MIB", "componentLevelVpdIndex"),
)
if mibBuilder.loadTexts:
    systemComponentLevelVpdEntry.setStatus("mandatory")


class _ComponentLevelVpdIndex_Type(Integer32):
    """Custom type componentLevelVpdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ComponentLevelVpdIndex_Type.__name__ = "Integer32"
_ComponentLevelVpdIndex_Object = MibTableColumn
componentLevelVpdIndex = _ComponentLevelVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 17, 1, 1),
    _ComponentLevelVpdIndex_Type()
)
componentLevelVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdIndex.setStatus("mandatory")
_ComponentLevelVpdFruNumber_Type = OctetString
_ComponentLevelVpdFruNumber_Object = MibTableColumn
componentLevelVpdFruNumber = _ComponentLevelVpdFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 17, 1, 2),
    _ComponentLevelVpdFruNumber_Type()
)
componentLevelVpdFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdFruNumber.setStatus("mandatory")
_ComponentLevelVpdFruName_Type = OctetString
_ComponentLevelVpdFruName_Object = MibTableColumn
componentLevelVpdFruName = _ComponentLevelVpdFruName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 17, 1, 3),
    _ComponentLevelVpdFruName_Type()
)
componentLevelVpdFruName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdFruName.setStatus("mandatory")
_ComponentLevelVpdSerialNumber_Type = OctetString
_ComponentLevelVpdSerialNumber_Object = MibTableColumn
componentLevelVpdSerialNumber = _ComponentLevelVpdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 17, 1, 4),
    _ComponentLevelVpdSerialNumber_Type()
)
componentLevelVpdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdSerialNumber.setStatus("mandatory")
_ComponentLevelVpdManufacturingId_Type = OctetString
_ComponentLevelVpdManufacturingId_Object = MibTableColumn
componentLevelVpdManufacturingId = _ComponentLevelVpdManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 17, 1, 5),
    _ComponentLevelVpdManufacturingId_Type()
)
componentLevelVpdManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdManufacturingId.setStatus("mandatory")
_SystemComponentLevelVpdTrackingTable_Object = MibTable
systemComponentLevelVpdTrackingTable = _SystemComponentLevelVpdTrackingTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 18)
)
if mibBuilder.loadTexts:
    systemComponentLevelVpdTrackingTable.setStatus("mandatory")
_SystemComponentLevelVpdTrackingEntry_Object = MibTableRow
systemComponentLevelVpdTrackingEntry = _SystemComponentLevelVpdTrackingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 18, 1)
)
systemComponentLevelVpdTrackingEntry.setIndexNames(
    (0, "IMM-MIB", "componentLevelVpdTrackingIndex"),
)
if mibBuilder.loadTexts:
    systemComponentLevelVpdTrackingEntry.setStatus("mandatory")


class _ComponentLevelVpdTrackingIndex_Type(Integer32):
    """Custom type componentLevelVpdTrackingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ComponentLevelVpdTrackingIndex_Type.__name__ = "Integer32"
_ComponentLevelVpdTrackingIndex_Object = MibTableColumn
componentLevelVpdTrackingIndex = _ComponentLevelVpdTrackingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 18, 1, 1),
    _ComponentLevelVpdTrackingIndex_Type()
)
componentLevelVpdTrackingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingIndex.setStatus("mandatory")
_ComponentLevelVpdTrackingFruNumber_Type = OctetString
_ComponentLevelVpdTrackingFruNumber_Object = MibTableColumn
componentLevelVpdTrackingFruNumber = _ComponentLevelVpdTrackingFruNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 18, 1, 2),
    _ComponentLevelVpdTrackingFruNumber_Type()
)
componentLevelVpdTrackingFruNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingFruNumber.setStatus("mandatory")
_ComponentLevelVpdTrackingFruName_Type = OctetString
_ComponentLevelVpdTrackingFruName_Object = MibTableColumn
componentLevelVpdTrackingFruName = _ComponentLevelVpdTrackingFruName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 18, 1, 3),
    _ComponentLevelVpdTrackingFruName_Type()
)
componentLevelVpdTrackingFruName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingFruName.setStatus("mandatory")
_ComponentLevelVpdTrackingSerialNumber_Type = OctetString
_ComponentLevelVpdTrackingSerialNumber_Object = MibTableColumn
componentLevelVpdTrackingSerialNumber = _ComponentLevelVpdTrackingSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 18, 1, 4),
    _ComponentLevelVpdTrackingSerialNumber_Type()
)
componentLevelVpdTrackingSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingSerialNumber.setStatus("mandatory")
_ComponentLevelVpdTrackingManufacturingId_Type = OctetString
_ComponentLevelVpdTrackingManufacturingId_Object = MibTableColumn
componentLevelVpdTrackingManufacturingId = _ComponentLevelVpdTrackingManufacturingId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 18, 1, 5),
    _ComponentLevelVpdTrackingManufacturingId_Type()
)
componentLevelVpdTrackingManufacturingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingManufacturingId.setStatus("mandatory")
_ComponentLevelVpdTrackingAction_Type = OctetString
_ComponentLevelVpdTrackingAction_Object = MibTableColumn
componentLevelVpdTrackingAction = _ComponentLevelVpdTrackingAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 18, 1, 6),
    _ComponentLevelVpdTrackingAction_Type()
)
componentLevelVpdTrackingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingAction.setStatus("mandatory")
_ComponentLevelVpdTrackingTimestamp_Type = OctetString
_ComponentLevelVpdTrackingTimestamp_Object = MibTableColumn
componentLevelVpdTrackingTimestamp = _ComponentLevelVpdTrackingTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 18, 1, 7),
    _ComponentLevelVpdTrackingTimestamp_Type()
)
componentLevelVpdTrackingTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLevelVpdTrackingTimestamp.setStatus("mandatory")
_HostMACAddressTable_Object = MibTable
hostMACAddressTable = _HostMACAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 19)
)
if mibBuilder.loadTexts:
    hostMACAddressTable.setStatus("mandatory")
_HostMACAddressEntry_Object = MibTableRow
hostMACAddressEntry = _HostMACAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 19, 1)
)
hostMACAddressEntry.setIndexNames(
    (0, "IMM-MIB", "hostMACAddressIndex"),
)
if mibBuilder.loadTexts:
    hostMACAddressEntry.setStatus("mandatory")


class _HostMACAddressIndex_Type(Integer32):
    """Custom type hostMACAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HostMACAddressIndex_Type.__name__ = "Integer32"
_HostMACAddressIndex_Object = MibTableColumn
hostMACAddressIndex = _HostMACAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 19, 1, 1),
    _HostMACAddressIndex_Type()
)
hostMACAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMACAddressIndex.setStatus("mandatory")
_HostMACAddressDescription_Type = DisplayString
_HostMACAddressDescription_Object = MibTableColumn
hostMACAddressDescription = _HostMACAddressDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 19, 1, 2),
    _HostMACAddressDescription_Type()
)
hostMACAddressDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMACAddressDescription.setStatus("mandatory")
_HostMACAddress_Type = DisplayString
_HostMACAddress_Object = MibTableColumn
hostMACAddress = _HostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 19, 1, 3),
    _HostMACAddress_Type()
)
hostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMACAddress.setStatus("mandatory")
_SystemCPUVpdTable_Object = MibTable
systemCPUVpdTable = _SystemCPUVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20)
)
if mibBuilder.loadTexts:
    systemCPUVpdTable.setStatus("mandatory")
_SystemCPUVpdEntry_Object = MibTableRow
systemCPUVpdEntry = _SystemCPUVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1)
)
systemCPUVpdEntry.setIndexNames(
    (0, "IMM-MIB", "cpuVpdIndex"),
)
if mibBuilder.loadTexts:
    systemCPUVpdEntry.setStatus("mandatory")


class _CpuVpdIndex_Type(Integer32):
    """Custom type cpuVpdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CpuVpdIndex_Type.__name__ = "Integer32"
_CpuVpdIndex_Object = MibTableColumn
cpuVpdIndex = _CpuVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 1),
    _CpuVpdIndex_Type()
)
cpuVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdIndex.setStatus("mandatory")
_CpuVpdDescription_Type = DisplayString
_CpuVpdDescription_Object = MibTableColumn
cpuVpdDescription = _CpuVpdDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 2),
    _CpuVpdDescription_Type()
)
cpuVpdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdDescription.setStatus("mandatory")
_CpuVpdSpeed_Type = Integer32
_CpuVpdSpeed_Object = MibTableColumn
cpuVpdSpeed = _CpuVpdSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 3),
    _CpuVpdSpeed_Type()
)
cpuVpdSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdSpeed.setStatus("mandatory")
_CpuVpdIdentifier_Type = DisplayString
_CpuVpdIdentifier_Object = MibTableColumn
cpuVpdIdentifier = _CpuVpdIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 4),
    _CpuVpdIdentifier_Type()
)
cpuVpdIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdIdentifier.setStatus("mandatory")
_CpuVpdType_Type = DisplayString
_CpuVpdType_Object = MibTableColumn
cpuVpdType = _CpuVpdType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 5),
    _CpuVpdType_Type()
)
cpuVpdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdType.setStatus("mandatory")
_CpuVpdFamily_Type = DisplayString
_CpuVpdFamily_Object = MibTableColumn
cpuVpdFamily = _CpuVpdFamily_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 6),
    _CpuVpdFamily_Type()
)
cpuVpdFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdFamily.setStatus("mandatory")
_CpuVpdCores_Type = Integer32
_CpuVpdCores_Object = MibTableColumn
cpuVpdCores = _CpuVpdCores_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 7),
    _CpuVpdCores_Type()
)
cpuVpdCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdCores.setStatus("mandatory")
_CpuVpdThreads_Type = Integer32
_CpuVpdThreads_Object = MibTableColumn
cpuVpdThreads = _CpuVpdThreads_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 8),
    _CpuVpdThreads_Type()
)
cpuVpdThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdThreads.setStatus("mandatory")
_CpuVpdVoltage_Type = Integer32
_CpuVpdVoltage_Object = MibTableColumn
cpuVpdVoltage = _CpuVpdVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 9),
    _CpuVpdVoltage_Type()
)
cpuVpdVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdVoltage.setStatus("mandatory")
_CpuVpdDataWidth_Type = Integer32
_CpuVpdDataWidth_Object = MibTableColumn
cpuVpdDataWidth = _CpuVpdDataWidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 10),
    _CpuVpdDataWidth_Type()
)
cpuVpdDataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdDataWidth.setStatus("mandatory")
_CpuVpdHealthStatus_Type = DisplayString
_CpuVpdHealthStatus_Object = MibTableColumn
cpuVpdHealthStatus = _CpuVpdHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 20, 1, 11),
    _CpuVpdHealthStatus_Type()
)
cpuVpdHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVpdHealthStatus.setStatus("mandatory")
_SystemMemoryVpdTable_Object = MibTable
systemMemoryVpdTable = _SystemMemoryVpdTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 21)
)
if mibBuilder.loadTexts:
    systemMemoryVpdTable.setStatus("mandatory")
_SystemMemoryVpdEntry_Object = MibTableRow
systemMemoryVpdEntry = _SystemMemoryVpdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 21, 1)
)
systemMemoryVpdEntry.setIndexNames(
    (0, "IMM-MIB", "memoryVpdIndex"),
)
if mibBuilder.loadTexts:
    systemMemoryVpdEntry.setStatus("mandatory")


class _MemoryVpdIndex_Type(Integer32):
    """Custom type memoryVpdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MemoryVpdIndex_Type.__name__ = "Integer32"
_MemoryVpdIndex_Object = MibTableColumn
memoryVpdIndex = _MemoryVpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 21, 1, 1),
    _MemoryVpdIndex_Type()
)
memoryVpdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdIndex.setStatus("mandatory")
_MemoryVpdDescription_Type = DisplayString
_MemoryVpdDescription_Object = MibTableColumn
memoryVpdDescription = _MemoryVpdDescription_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 21, 1, 2),
    _MemoryVpdDescription_Type()
)
memoryVpdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdDescription.setStatus("mandatory")
_MemoryVpdPartNumber_Type = DisplayString
_MemoryVpdPartNumber_Object = MibTableColumn
memoryVpdPartNumber = _MemoryVpdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 21, 1, 3),
    _MemoryVpdPartNumber_Type()
)
memoryVpdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdPartNumber.setStatus("mandatory")
_MemoryVpdFRUSerialNumber_Type = DisplayString
_MemoryVpdFRUSerialNumber_Object = MibTableColumn
memoryVpdFRUSerialNumber = _MemoryVpdFRUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 21, 1, 4),
    _MemoryVpdFRUSerialNumber_Type()
)
memoryVpdFRUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdFRUSerialNumber.setStatus("mandatory")
_MemoryVpdManufactureDate_Type = DisplayString
_MemoryVpdManufactureDate_Object = MibTableColumn
memoryVpdManufactureDate = _MemoryVpdManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 21, 1, 5),
    _MemoryVpdManufactureDate_Type()
)
memoryVpdManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdManufactureDate.setStatus("mandatory")
_MemoryVpdType_Type = DisplayString
_MemoryVpdType_Object = MibTableColumn
memoryVpdType = _MemoryVpdType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 21, 1, 6),
    _MemoryVpdType_Type()
)
memoryVpdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdType.setStatus("mandatory")
_MemoryVpdSize_Type = Integer32
_MemoryVpdSize_Object = MibTableColumn
memoryVpdSize = _MemoryVpdSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 21, 1, 7),
    _MemoryVpdSize_Type()
)
memoryVpdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryVpdSize.setStatus("mandatory")


class _MemoryHealthStatus_Type(DisplayString):
    """Custom type memoryHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MemoryHealthStatus_Type.__name__ = "DisplayString"
_MemoryHealthStatus_Object = MibTableColumn
memoryHealthStatus = _MemoryHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 5, 21, 1, 8),
    _MemoryHealthStatus_Type()
)
memoryHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryHealthStatus.setStatus("mandatory")
_Users_ObjectIdentity = ObjectIdentity
users = _Users_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 6)
)
_ImmUsers_ObjectIdentity = ObjectIdentity
immUsers = _ImmUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 6, 1)
)
_CurrentlyLoggedInTable_Object = MibTable
currentlyLoggedInTable = _CurrentlyLoggedInTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    currentlyLoggedInTable.setStatus("mandatory")
_CurrentlyLoggedInEntry_Object = MibTableRow
currentlyLoggedInEntry = _CurrentlyLoggedInEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 6, 1, 1, 1)
)
currentlyLoggedInEntry.setIndexNames(
    (0, "IMM-MIB", "currentlyLoggedInEntryIndex"),
)
if mibBuilder.loadTexts:
    currentlyLoggedInEntry.setStatus("mandatory")


class _CurrentlyLoggedInEntryIndex_Type(Integer32):
    """Custom type currentlyLoggedInEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CurrentlyLoggedInEntryIndex_Type.__name__ = "Integer32"
_CurrentlyLoggedInEntryIndex_Object = MibTableColumn
currentlyLoggedInEntryIndex = _CurrentlyLoggedInEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 6, 1, 1, 1, 1),
    _CurrentlyLoggedInEntryIndex_Type()
)
currentlyLoggedInEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyLoggedInEntryIndex.setStatus("mandatory")


class _CurrentlyLoggedInEntryUserId_Type(OctetString):
    """Custom type currentlyLoggedInEntryUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CurrentlyLoggedInEntryUserId_Type.__name__ = "OctetString"
_CurrentlyLoggedInEntryUserId_Object = MibTableColumn
currentlyLoggedInEntryUserId = _CurrentlyLoggedInEntryUserId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 6, 1, 1, 1, 2),
    _CurrentlyLoggedInEntryUserId_Type()
)
currentlyLoggedInEntryUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyLoggedInEntryUserId.setStatus("mandatory")


class _CurrentlyLoggedInEntryAccMethod_Type(OctetString):
    """Custom type currentlyLoggedInEntryAccMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CurrentlyLoggedInEntryAccMethod_Type.__name__ = "OctetString"
_CurrentlyLoggedInEntryAccMethod_Object = MibTableColumn
currentlyLoggedInEntryAccMethod = _CurrentlyLoggedInEntryAccMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 6, 1, 1, 1, 3),
    _CurrentlyLoggedInEntryAccMethod_Type()
)
currentlyLoggedInEntryAccMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyLoggedInEntryAccMethod.setStatus("mandatory")
_Leds_ObjectIdentity = ObjectIdentity
leds = _Leds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 8)
)


class _IdentityLED_Type(Integer32):
    """Custom type identityLED based on Integer32"""
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
        *(("blinking", 2),
          ("notAvailable", 3),
          ("off", 0),
          ("on", 1))
    )


_IdentityLED_Type.__name__ = "Integer32"
_IdentityLED_Object = MibScalar
identityLED = _IdentityLED_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 8, 1),
    _IdentityLED_Type()
)
identityLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identityLED.setStatus("mandatory")
_AllLEDsTable_Object = MibTable
allLEDsTable = _AllLEDsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 8, 2)
)
if mibBuilder.loadTexts:
    allLEDsTable.setStatus("mandatory")
_AllLEDsEntry_Object = MibTableRow
allLEDsEntry = _AllLEDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 8, 2, 1)
)
allLEDsEntry.setIndexNames(
    (0, "IMM-MIB", "ledIndex"),
)
if mibBuilder.loadTexts:
    allLEDsEntry.setStatus("mandatory")


class _LedIndex_Type(Integer32):
    """Custom type ledIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_LedIndex_Type.__name__ = "Integer32"
_LedIndex_Object = MibTableColumn
ledIndex = _LedIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 8, 2, 1, 1),
    _LedIndex_Type()
)
ledIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledIndex.setStatus("mandatory")
_LedIdentifier_Type = Integer32
_LedIdentifier_Object = MibTableColumn
ledIdentifier = _LedIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 8, 2, 1, 2),
    _LedIdentifier_Type()
)
ledIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledIdentifier.setStatus("mandatory")
_LedLabel_Type = DisplayString
_LedLabel_Object = MibTableColumn
ledLabel = _LedLabel_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 8, 2, 1, 4),
    _LedLabel_Type()
)
ledLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledLabel.setStatus("mandatory")


class _LedState_Type(Integer32):
    """Custom type ledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blinking", 2),
          ("off", 0),
          ("on", 1))
    )


_LedState_Type.__name__ = "Integer32"
_LedState_Object = MibTableColumn
ledState = _LedState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 8, 2, 1, 5),
    _LedState_Type()
)
ledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledState.setStatus("mandatory")
_LedColor_Type = DisplayString
_LedColor_Object = MibTableColumn
ledColor = _LedColor_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 8, 2, 1, 6),
    _LedColor_Type()
)
ledColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledColor.setStatus("mandatory")


class _InformationLED_Type(Integer32):
    """Custom type informationLED based on Integer32"""
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
        *(("blinking", 2),
          ("notAvailable", 3),
          ("off", 0),
          ("on", 1))
    )


_InformationLED_Type.__name__ = "Integer32"
_InformationLED_Object = MibScalar
informationLED = _InformationLED_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 8, 3),
    _InformationLED_Type()
)
informationLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    informationLED.setStatus("mandatory")
_OsFailureCapture_ObjectIdentity = ObjectIdentity
osFailureCapture = _OsFailureCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 9)
)


class _OsFailureCaptureTftpServer_Type(OctetString):
    """Custom type osFailureCaptureTftpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OsFailureCaptureTftpServer_Type.__name__ = "OctetString"
_OsFailureCaptureTftpServer_Object = MibScalar
osFailureCaptureTftpServer = _OsFailureCaptureTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 9, 1),
    _OsFailureCaptureTftpServer_Type()
)
osFailureCaptureTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osFailureCaptureTftpServer.setStatus("mandatory")


class _OsFailureCaptureFileName_Type(OctetString):
    """Custom type osFailureCaptureFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_OsFailureCaptureFileName_Type.__name__ = "OctetString"
_OsFailureCaptureFileName_Object = MibScalar
osFailureCaptureFileName = _OsFailureCaptureFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 9, 2),
    _OsFailureCaptureFileName_Type()
)
osFailureCaptureFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osFailureCaptureFileName.setStatus("mandatory")


class _OsFailureCaptureSaveStart_Type(Integer32):
    """Custom type osFailureCaptureSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 1),
          ("execute-nowait", 2))
    )


_OsFailureCaptureSaveStart_Type.__name__ = "Integer32"
_OsFailureCaptureSaveStart_Object = MibScalar
osFailureCaptureSaveStart = _OsFailureCaptureSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 9, 3),
    _OsFailureCaptureSaveStart_Type()
)
osFailureCaptureSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osFailureCaptureSaveStart.setStatus("mandatory")


class _OsFailureCaptureSaveStatus_Type(Integer32):
    """Custom type osFailureCaptureSaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("nocapture", 2),
          ("success", 0))
    )


_OsFailureCaptureSaveStatus_Type.__name__ = "Integer32"
_OsFailureCaptureSaveStatus_Object = MibScalar
osFailureCaptureSaveStatus = _OsFailureCaptureSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 9, 4),
    _OsFailureCaptureSaveStatus_Type()
)
osFailureCaptureSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osFailureCaptureSaveStatus.setStatus("mandatory")
_FuelGauge_ObjectIdentity = ObjectIdentity
fuelGauge = _FuelGauge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10)
)
_FuelGaugeInformation_ObjectIdentity = ObjectIdentity
fuelGaugeInformation = _FuelGaugeInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1)
)


class _FuelGaugePowerCappingPolicySetting_Type(Integer32):
    """Custom type fuelGaugePowerCappingPolicySetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noPowerLimit", 0),
          ("staticPowerLimit", 1))
    )


_FuelGaugePowerCappingPolicySetting_Type.__name__ = "Integer32"
_FuelGaugePowerCappingPolicySetting_Object = MibScalar
fuelGaugePowerCappingPolicySetting = _FuelGaugePowerCappingPolicySetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 1),
    _FuelGaugePowerCappingPolicySetting_Type()
)
fuelGaugePowerCappingPolicySetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fuelGaugePowerCappingPolicySetting.setStatus("mandatory")
_FuelGaugeStaticPowerPcapSoftMin_Type = Integer32
_FuelGaugeStaticPowerPcapSoftMin_Object = MibScalar
fuelGaugeStaticPowerPcapSoftMin = _FuelGaugeStaticPowerPcapSoftMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 2),
    _FuelGaugeStaticPowerPcapSoftMin_Type()
)
fuelGaugeStaticPowerPcapSoftMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeStaticPowerPcapSoftMin.setStatus("mandatory")
_FuelGaugeStaticPowerPcapMin_Type = Integer32
_FuelGaugeStaticPowerPcapMin_Object = MibScalar
fuelGaugeStaticPowerPcapMin = _FuelGaugeStaticPowerPcapMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 3),
    _FuelGaugeStaticPowerPcapMin_Type()
)
fuelGaugeStaticPowerPcapMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeStaticPowerPcapMin.setStatus("mandatory")
_FuelGaugeStaticPowerPcapCurrentSetting_Type = Integer32
_FuelGaugeStaticPowerPcapCurrentSetting_Object = MibScalar
fuelGaugeStaticPowerPcapCurrentSetting = _FuelGaugeStaticPowerPcapCurrentSetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 4),
    _FuelGaugeStaticPowerPcapCurrentSetting_Type()
)
fuelGaugeStaticPowerPcapCurrentSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fuelGaugeStaticPowerPcapCurrentSetting.setStatus("mandatory")
_FuelGaugeStaticPowerPcapMax_Type = Integer32
_FuelGaugeStaticPowerPcapMax_Object = MibScalar
fuelGaugeStaticPowerPcapMax = _FuelGaugeStaticPowerPcapMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 5),
    _FuelGaugeStaticPowerPcapMax_Type()
)
fuelGaugeStaticPowerPcapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeStaticPowerPcapMax.setStatus("mandatory")


class _FuelGaugeStaticPowerPcapMode_Type(Integer32):
    """Custom type fuelGaugeStaticPowerPcapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 0))
    )


_FuelGaugeStaticPowerPcapMode_Type.__name__ = "Integer32"
_FuelGaugeStaticPowerPcapMode_Object = MibScalar
fuelGaugeStaticPowerPcapMode = _FuelGaugeStaticPowerPcapMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 6),
    _FuelGaugeStaticPowerPcapMode_Type()
)
fuelGaugeStaticPowerPcapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fuelGaugeStaticPowerPcapMode.setStatus("mandatory")
_FuelGaugeSystemMaxPower_Type = Integer32
_FuelGaugeSystemMaxPower_Object = MibScalar
fuelGaugeSystemMaxPower = _FuelGaugeSystemMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 7),
    _FuelGaugeSystemMaxPower_Type()
)
fuelGaugeSystemMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeSystemMaxPower.setStatus("mandatory")
_FuelGaugePowerRemaining_Type = Integer32
_FuelGaugePowerRemaining_Object = MibScalar
fuelGaugePowerRemaining = _FuelGaugePowerRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 8),
    _FuelGaugePowerRemaining_Type()
)
fuelGaugePowerRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerRemaining.setStatus("mandatory")
_FuelGaugeTotalPowerAvaialble_Type = Integer32
_FuelGaugeTotalPowerAvaialble_Object = MibScalar
fuelGaugeTotalPowerAvaialble = _FuelGaugeTotalPowerAvaialble_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 9),
    _FuelGaugeTotalPowerAvaialble_Type()
)
fuelGaugeTotalPowerAvaialble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeTotalPowerAvaialble.setStatus("mandatory")
_FuelGaugeTotalPowerInUse_Type = Integer32
_FuelGaugeTotalPowerInUse_Object = MibScalar
fuelGaugeTotalPowerInUse = _FuelGaugeTotalPowerInUse_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 10),
    _FuelGaugeTotalPowerInUse_Type()
)
fuelGaugeTotalPowerInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeTotalPowerInUse.setStatus("mandatory")
_FuelGaugeTotalThermalOutput_Type = Integer32
_FuelGaugeTotalThermalOutput_Object = MibScalar
fuelGaugeTotalThermalOutput = _FuelGaugeTotalThermalOutput_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 11),
    _FuelGaugeTotalThermalOutput_Type()
)
fuelGaugeTotalThermalOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugeTotalThermalOutput.setStatus("mandatory")
_FuelGaugePowerConsumptionCpu_Type = Integer32
_FuelGaugePowerConsumptionCpu_Object = MibScalar
fuelGaugePowerConsumptionCpu = _FuelGaugePowerConsumptionCpu_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 12),
    _FuelGaugePowerConsumptionCpu_Type()
)
fuelGaugePowerConsumptionCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerConsumptionCpu.setStatus("mandatory")
_FuelGaugePowerConsumptionMemory_Type = Integer32
_FuelGaugePowerConsumptionMemory_Object = MibScalar
fuelGaugePowerConsumptionMemory = _FuelGaugePowerConsumptionMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 13),
    _FuelGaugePowerConsumptionMemory_Type()
)
fuelGaugePowerConsumptionMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerConsumptionMemory.setStatus("mandatory")
_FuelGaugePowerConsumptionOther_Type = Integer32
_FuelGaugePowerConsumptionOther_Object = MibScalar
fuelGaugePowerConsumptionOther = _FuelGaugePowerConsumptionOther_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 1, 15),
    _FuelGaugePowerConsumptionOther_Type()
)
fuelGaugePowerConsumptionOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelGaugePowerConsumptionOther.setStatus("mandatory")
_PowerPolicyInformation_ObjectIdentity = ObjectIdentity
powerPolicyInformation = _PowerPolicyInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 2)
)
_PowerPolicyTable_Object = MibTable
powerPolicyTable = _PowerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    powerPolicyTable.setStatus("mandatory")
_PowerPolicyEntry_Object = MibTableRow
powerPolicyEntry = _PowerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 2, 1, 1)
)
powerPolicyEntry.setIndexNames(
    (0, "IMM-MIB", "powerPolicyIndex"),
)
if mibBuilder.loadTexts:
    powerPolicyEntry.setStatus("mandatory")
_PowerPolicyIndex_Type = Integer32
_PowerPolicyIndex_Object = MibTableColumn
powerPolicyIndex = _PowerPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 2, 1, 1, 1),
    _PowerPolicyIndex_Type()
)
powerPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyIndex.setStatus("mandatory")
_PowerPolicyName_Type = OctetString
_PowerPolicyName_Object = MibTableColumn
powerPolicyName = _PowerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 2, 1, 1, 2),
    _PowerPolicyName_Type()
)
powerPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyName.setStatus("mandatory")
_PowerPolicyPwrSupplyFailureLimit_Type = Integer32
_PowerPolicyPwrSupplyFailureLimit_Object = MibTableColumn
powerPolicyPwrSupplyFailureLimit = _PowerPolicyPwrSupplyFailureLimit_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 2, 1, 1, 3),
    _PowerPolicyPwrSupplyFailureLimit_Type()
)
powerPolicyPwrSupplyFailureLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyPwrSupplyFailureLimit.setStatus("mandatory")
_PowerPolicyMaxPowerLimit_Type = Integer32
_PowerPolicyMaxPowerLimit_Object = MibTableColumn
powerPolicyMaxPowerLimit = _PowerPolicyMaxPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 2, 1, 1, 4),
    _PowerPolicyMaxPowerLimit_Type()
)
powerPolicyMaxPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyMaxPowerLimit.setStatus("mandatory")
_PowerPolicyEstimatedUtilization_Type = Integer32
_PowerPolicyEstimatedUtilization_Object = MibTableColumn
powerPolicyEstimatedUtilization = _PowerPolicyEstimatedUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 2, 1, 1, 5),
    _PowerPolicyEstimatedUtilization_Type()
)
powerPolicyEstimatedUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPolicyEstimatedUtilization.setStatus("mandatory")


class _PowerPolicyActivate_Type(Integer32):
    """Custom type powerPolicyActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PowerPolicyActivate_Type.__name__ = "Integer32"
_PowerPolicyActivate_Object = MibTableColumn
powerPolicyActivate = _PowerPolicyActivate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 2, 1, 1, 6),
    _PowerPolicyActivate_Type()
)
powerPolicyActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerPolicyActivate.setStatus("mandatory")
_PowerPowerTrending_ObjectIdentity = ObjectIdentity
powerPowerTrending = _PowerPowerTrending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 3)
)


class _PowerTrendingPeriod_Type(Integer32):
    """Custom type powerTrendingPeriod based on Integer32"""
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
        *(("last12Hours", 2),
          ("last24Hours", 3),
          ("last6Hours", 1),
          ("lastHour", 0))
    )


_PowerTrendingPeriod_Type.__name__ = "Integer32"
_PowerTrendingPeriod_Object = MibScalar
powerTrendingPeriod = _PowerTrendingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 3, 1),
    _PowerTrendingPeriod_Type()
)
powerTrendingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerTrendingPeriod.setStatus("mandatory")


class _PowerTrendingPowerType_Type(Integer32):
    """Custom type powerTrendingPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 0))
    )


_PowerTrendingPowerType_Type.__name__ = "Integer32"
_PowerTrendingPowerType_Object = MibScalar
powerTrendingPowerType = _PowerTrendingPowerType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 3, 2),
    _PowerTrendingPowerType_Type()
)
powerTrendingPowerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerTrendingPowerType.setStatus("mandatory")
_PowerTrendingSampleTable_Object = MibTable
powerTrendingSampleTable = _PowerTrendingSampleTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 3, 3)
)
if mibBuilder.loadTexts:
    powerTrendingSampleTable.setStatus("mandatory")
_PowerTrendingSampleEntry_Object = MibTableRow
powerTrendingSampleEntry = _PowerTrendingSampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 3, 3, 1)
)
powerTrendingSampleEntry.setIndexNames(
    (0, "IMM-MIB", "powerTrendingSampleIndex"),
)
if mibBuilder.loadTexts:
    powerTrendingSampleEntry.setStatus("mandatory")
_PowerTrendingSampleIndex_Type = Integer32
_PowerTrendingSampleIndex_Object = MibTableColumn
powerTrendingSampleIndex = _PowerTrendingSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 3, 3, 1, 1),
    _PowerTrendingSampleIndex_Type()
)
powerTrendingSampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleIndex.setStatus("mandatory")
_PowerTrendingSampleTimeStamp_Type = OctetString
_PowerTrendingSampleTimeStamp_Object = MibTableColumn
powerTrendingSampleTimeStamp = _PowerTrendingSampleTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 3, 3, 1, 2),
    _PowerTrendingSampleTimeStamp_Type()
)
powerTrendingSampleTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleTimeStamp.setStatus("mandatory")
_PowerTrendingSampleAve_Type = Integer32
_PowerTrendingSampleAve_Object = MibTableColumn
powerTrendingSampleAve = _PowerTrendingSampleAve_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 3, 3, 1, 3),
    _PowerTrendingSampleAve_Type()
)
powerTrendingSampleAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleAve.setStatus("mandatory")
_PowerTrendingSampleMin_Type = Integer32
_PowerTrendingSampleMin_Object = MibTableColumn
powerTrendingSampleMin = _PowerTrendingSampleMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 3, 3, 1, 4),
    _PowerTrendingSampleMin_Type()
)
powerTrendingSampleMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleMin.setStatus("mandatory")
_PowerTrendingSampleMax_Type = Integer32
_PowerTrendingSampleMax_Object = MibTableColumn
powerTrendingSampleMax = _PowerTrendingSampleMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 10, 3, 3, 1, 5),
    _PowerTrendingSampleMax_Type()
)
powerTrendingSampleMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTrendingSampleMax.setStatus("mandatory")
_PowerModule_ObjectIdentity = ObjectIdentity
powerModule = _PowerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 11)
)
_PowerNumber_Type = Gauge32
_PowerNumber_Object = MibScalar
powerNumber = _PowerNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 11, 1),
    _PowerNumber_Type()
)
powerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerNumber.setStatus("mandatory")
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 11, 2)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("mandatory")
_PowerEntry_Object = MibTableRow
powerEntry = _PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 11, 2, 1)
)
powerEntry.setIndexNames(
    (0, "IMM-MIB", "powerIndex"),
)
if mibBuilder.loadTexts:
    powerEntry.setStatus("mandatory")


class _PowerIndex_Type(Integer32):
    """Custom type powerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PowerIndex_Type.__name__ = "Integer32"
_PowerIndex_Object = MibTableColumn
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 11, 2, 1, 1),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerIndex.setStatus("mandatory")


class _PowerFruName_Type(DisplayString):
    """Custom type powerFruName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerFruName_Type.__name__ = "DisplayString"
_PowerFruName_Object = MibTableColumn
powerFruName = _PowerFruName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 11, 2, 1, 2),
    _PowerFruName_Type()
)
powerFruName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFruName.setStatus("mandatory")


class _PowerPartNumber_Type(DisplayString):
    """Custom type powerPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerPartNumber_Type.__name__ = "DisplayString"
_PowerPartNumber_Object = MibTableColumn
powerPartNumber = _PowerPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 11, 2, 1, 3),
    _PowerPartNumber_Type()
)
powerPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPartNumber.setStatus("mandatory")


class _PowerFRUNumber_Type(DisplayString):
    """Custom type powerFRUNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerFRUNumber_Type.__name__ = "DisplayString"
_PowerFRUNumber_Object = MibTableColumn
powerFRUNumber = _PowerFRUNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 11, 2, 1, 4),
    _PowerFRUNumber_Type()
)
powerFRUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFRUNumber.setStatus("mandatory")


class _PowerFRUSerialNumber_Type(DisplayString):
    """Custom type powerFRUSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerFRUSerialNumber_Type.__name__ = "DisplayString"
_PowerFRUSerialNumber_Object = MibTableColumn
powerFRUSerialNumber = _PowerFRUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 11, 2, 1, 5),
    _PowerFRUSerialNumber_Type()
)
powerFRUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFRUSerialNumber.setStatus("mandatory")


class _PowerHealthStatus_Type(DisplayString):
    """Custom type powerHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerHealthStatus_Type.__name__ = "DisplayString"
_PowerHealthStatus_Object = MibTableColumn
powerHealthStatus = _PowerHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 11, 2, 1, 6),
    _PowerHealthStatus_Type()
)
powerHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerHealthStatus.setStatus("mandatory")
_Disks_ObjectIdentity = ObjectIdentity
disks = _Disks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 12)
)
_DiskNumber_Type = Gauge32
_DiskNumber_Object = MibScalar
diskNumber = _DiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 12, 1),
    _DiskNumber_Type()
)
diskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNumber.setStatus("mandatory")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 12, 2)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("mandatory")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 12, 2, 1)
)
diskEntry.setIndexNames(
    (0, "IMM-MIB", "diskIndex"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("mandatory")


class _DiskIndex_Type(Integer32):
    """Custom type diskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DiskIndex_Type.__name__ = "Integer32"
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 12, 2, 1, 1),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIndex.setStatus("mandatory")


class _DiskFruName_Type(DisplayString):
    """Custom type diskFruName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DiskFruName_Type.__name__ = "DisplayString"
_DiskFruName_Object = MibTableColumn
diskFruName = _DiskFruName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 12, 2, 1, 2),
    _DiskFruName_Type()
)
diskFruName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFruName.setStatus("mandatory")


class _DiskHealthStatus_Type(DisplayString):
    """Custom type diskHealthStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DiskHealthStatus_Type.__name__ = "DisplayString"
_DiskHealthStatus_Object = MibTableColumn
diskHealthStatus = _DiskHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 1, 12, 2, 1, 3),
    _DiskHealthStatus_Type()
)
diskHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskHealthStatus.setStatus("mandatory")
_ErrorLogs_ObjectIdentity = ObjectIdentity
errorLogs = _ErrorLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2)
)
_EventLog_ObjectIdentity = ObjectIdentity
eventLog = _EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1)
)
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("mandatory")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 1, 1)
)
eventLogEntry.setIndexNames(
    (0, "IMM-MIB", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("mandatory")


class _EventLogIndex_Type(Integer32):
    """Custom type eventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_EventLogIndex_Type.__name__ = "Integer32"
_EventLogIndex_Object = MibTableColumn
eventLogIndex = _EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 1, 1, 1),
    _EventLogIndex_Type()
)
eventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogIndex.setStatus("mandatory")
_EventLogString_Type = OctetString
_EventLogString_Object = MibTableColumn
eventLogString = _EventLogString_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 1, 1, 2),
    _EventLogString_Type()
)
eventLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogString.setStatus("mandatory")


class _EventLogSeverity_Type(Integer32):
    """Custom type eventLogSeverity based on Integer32"""
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
        *(("error", 0),
          ("information", 2),
          ("other", 3),
          ("warning", 1))
    )


_EventLogSeverity_Type.__name__ = "Integer32"
_EventLogSeverity_Object = MibTableColumn
eventLogSeverity = _EventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 1, 1, 3),
    _EventLogSeverity_Type()
)
eventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogSeverity.setStatus("mandatory")
_EventLogDate_Type = OctetString
_EventLogDate_Object = MibTableColumn
eventLogDate = _EventLogDate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 1, 1, 4),
    _EventLogDate_Type()
)
eventLogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDate.setStatus("mandatory")
_EventLogTime_Type = OctetString
_EventLogTime_Object = MibTableColumn
eventLogTime = _EventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 1, 1, 5),
    _EventLogTime_Type()
)
eventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTime.setStatus("mandatory")


class _EventLogClr_Type(Integer32):
    """Custom type eventLogClr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_EventLogClr_Type.__name__ = "Integer32"
_EventLogClr_Object = MibScalar
eventLogClr = _EventLogClr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 3),
    _EventLogClr_Type()
)
eventLogClr.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    eventLogClr.setStatus("mandatory")


class _EventLogTftpServer_Type(OctetString):
    """Custom type eventLogTftpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_EventLogTftpServer_Type.__name__ = "OctetString"
_EventLogTftpServer_Object = MibScalar
eventLogTftpServer = _EventLogTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 4),
    _EventLogTftpServer_Type()
)
eventLogTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLogTftpServer.setStatus("mandatory")


class _EventLogFileName_Type(OctetString):
    """Custom type eventLogFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_EventLogFileName_Type.__name__ = "OctetString"
_EventLogFileName_Object = MibScalar
eventLogFileName = _EventLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 5),
    _EventLogFileName_Type()
)
eventLogFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLogFileName.setStatus("mandatory")


class _EventLogSaveStart_Type(Integer32):
    """Custom type eventLogSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 1),
          ("execute-nowait", 2))
    )


_EventLogSaveStart_Type.__name__ = "Integer32"
_EventLogSaveStart_Object = MibScalar
eventLogSaveStart = _EventLogSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 6),
    _EventLogSaveStart_Type()
)
eventLogSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLogSaveStart.setStatus("mandatory")


class _EventLogSaveStatus_Type(Integer32):
    """Custom type eventLogSaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("success", 0))
    )


_EventLogSaveStatus_Type.__name__ = "Integer32"
_EventLogSaveStatus_Object = MibScalar
eventLogSaveStatus = _EventLogSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 2, 1, 7),
    _EventLogSaveStatus_Type()
)
eventLogSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogSaveStatus.setStatus("mandatory")
_ConfigureSP_ObjectIdentity = ObjectIdentity
configureSP = _ConfigureSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3)
)
_RemoteAccessConfig_ObjectIdentity = ObjectIdentity
remoteAccessConfig = _RemoteAccessConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1)
)
_GeneralRemoteCfg_ObjectIdentity = ObjectIdentity
generalRemoteCfg = _GeneralRemoteCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1)
)


class _RemoteAlertRetryDelay_Type(Integer32):
    """Custom type remoteAlertRetryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              60,
              90,
              120,
              150,
              180,
              210,
              240)
        )
    )
    namedValues = NamedValues(
        *(("fourMinutes", 240),
          ("noDelay", 0),
          ("oneAndHalfMinutes", 90),
          ("oneHalfMinute", 30),
          ("oneMinute", 60),
          ("threeAndHalfMinutes", 210),
          ("threeMinutes", 180),
          ("twoAndHalfMinutes", 150),
          ("twoMinutes", 120))
    )


_RemoteAlertRetryDelay_Type.__name__ = "Integer32"
_RemoteAlertRetryDelay_Object = MibScalar
remoteAlertRetryDelay = _RemoteAlertRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 1),
    _RemoteAlertRetryDelay_Type()
)
remoteAlertRetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertRetryDelay.setStatus("mandatory")


class _RemoteAlertRetryCount_Type(Integer32):
    """Custom type remoteAlertRetryCount based on Integer32"""
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
        *(("noretry", 0),
          ("retry1", 1),
          ("retry2", 2),
          ("retry3", 3),
          ("retry4", 4),
          ("retry5", 5),
          ("retry6", 6),
          ("retry7", 7),
          ("retry8", 8))
    )


_RemoteAlertRetryCount_Type.__name__ = "Integer32"
_RemoteAlertRetryCount_Object = MibScalar
remoteAlertRetryCount = _RemoteAlertRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 2),
    _RemoteAlertRetryCount_Type()
)
remoteAlertRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertRetryCount.setStatus("mandatory")


class _RemoteAlertEntryDelay_Type(Integer32):
    """Custom type remoteAlertEntryDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              60,
              90,
              120,
              150,
              180,
              210,
              240)
        )
    )
    namedValues = NamedValues(
        *(("fourMinutes", 240),
          ("noDelay", 0),
          ("oneAndHalfMinutes", 90),
          ("oneHalfMinute", 30),
          ("oneMinute", 60),
          ("threeAndHalfMinutes", 210),
          ("threeMinutes", 180),
          ("twoAndHalfMinutes", 150),
          ("twoMinutes", 120))
    )


_RemoteAlertEntryDelay_Type.__name__ = "Integer32"
_RemoteAlertEntryDelay_Object = MibScalar
remoteAlertEntryDelay = _RemoteAlertEntryDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 3),
    _RemoteAlertEntryDelay_Type()
)
remoteAlertEntryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertEntryDelay.setStatus("mandatory")


class _SnmpCriticalAlerts_Type(Integer32):
    """Custom type snmpCriticalAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpCriticalAlerts_Type.__name__ = "Integer32"
_SnmpCriticalAlerts_Object = MibScalar
snmpCriticalAlerts = _SnmpCriticalAlerts_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 4),
    _SnmpCriticalAlerts_Type()
)
snmpCriticalAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCriticalAlerts.setStatus("mandatory")


class _SnmpWarningAlerts_Type(Integer32):
    """Custom type snmpWarningAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpWarningAlerts_Type.__name__ = "Integer32"
_SnmpWarningAlerts_Object = MibScalar
snmpWarningAlerts = _SnmpWarningAlerts_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 5),
    _SnmpWarningAlerts_Type()
)
snmpWarningAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpWarningAlerts.setStatus("mandatory")


class _SnmpSystemAlerts_Type(Integer32):
    """Custom type snmpSystemAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnmpSystemAlerts_Type.__name__ = "Integer32"
_SnmpSystemAlerts_Object = MibScalar
snmpSystemAlerts = _SnmpSystemAlerts_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 6),
    _SnmpSystemAlerts_Type()
)
snmpSystemAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemAlerts.setStatus("mandatory")


class _RemoteAccessTamperDelay_Type(Integer32):
    """Custom type remoteAccessTamperDelay based on Integer32"""
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
              10,
              15,
              20,
              30,
              60,
              120,
              180,
              240)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 15),
          ("fiveMinutes", 5),
          ("fourMinutes", 4),
          ("nowait", 0),
          ("oneEightyMinutes", 180),
          ("oneMinute", 1),
          ("oneTwentyMinutes", 120),
          ("sevenMinutes", 7),
          ("sixMinutes", 6),
          ("sixtyMinutes", 60),
          ("tenMinutes", 10),
          ("thirtyMinutes", 30),
          ("threeMinutes", 3),
          ("twentyMinutes", 20),
          ("twoFortyMinutes", 240),
          ("twoMinutes", 2))
    )


_RemoteAccessTamperDelay_Type.__name__ = "Integer32"
_RemoteAccessTamperDelay_Object = MibScalar
remoteAccessTamperDelay = _RemoteAccessTamperDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 7),
    _RemoteAccessTamperDelay_Type()
)
remoteAccessTamperDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessTamperDelay.setStatus("mandatory")


class _UserAuthenticationMethod_Type(Integer32):
    """Custom type userAuthenticationMethod based on Integer32"""
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
        *(("ldapFirstThenLocal", 3),
          ("ldapOnly", 1),
          ("localFirstThenLdap", 2),
          ("localOnly", 0))
    )


_UserAuthenticationMethod_Type.__name__ = "Integer32"
_UserAuthenticationMethod_Object = MibScalar
userAuthenticationMethod = _UserAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 8),
    _UserAuthenticationMethod_Type()
)
userAuthenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthenticationMethod.setStatus("mandatory")


class _WebInactivityTimeout_Type(Integer32):
    """Custom type webInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 3),
          ("fiveMinutes", 1),
          ("noTimeout", 5),
          ("oneMinutes", 0),
          ("tenMinutes", 2),
          ("twentyMinutes", 4),
          ("userPicksTimeout", 6))
    )


_WebInactivityTimeout_Type.__name__ = "Integer32"
_WebInactivityTimeout_Object = MibScalar
webInactivityTimeout = _WebInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 9),
    _WebInactivityTimeout_Type()
)
webInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webInactivityTimeout.setStatus("mandatory")
_SnmpAlertFilters_ObjectIdentity = ObjectIdentity
snmpAlertFilters = _SnmpAlertFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10)
)


class _SafSpTrapTempC_Type(Integer32):
    """Custom type safSpTrapTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapTempC_Type.__name__ = "Integer32"
_SafSpTrapTempC_Object = MibScalar
safSpTrapTempC = _SafSpTrapTempC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 2),
    _SafSpTrapTempC_Type()
)
safSpTrapTempC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapTempC.setStatus("mandatory")


class _SafSpTrapVoltC_Type(Integer32):
    """Custom type safSpTrapVoltC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapVoltC_Type.__name__ = "Integer32"
_SafSpTrapVoltC_Object = MibScalar
safSpTrapVoltC = _SafSpTrapVoltC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 3),
    _SafSpTrapVoltC_Type()
)
safSpTrapVoltC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapVoltC.setStatus("mandatory")


class _SafSpTrapPowerC_Type(Integer32):
    """Custom type safSpTrapPowerC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapPowerC_Type.__name__ = "Integer32"
_SafSpTrapPowerC_Object = MibScalar
safSpTrapPowerC = _SafSpTrapPowerC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 4),
    _SafSpTrapPowerC_Type()
)
safSpTrapPowerC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapPowerC.setStatus("mandatory")


class _SafSpTrapHdC_Type(Integer32):
    """Custom type safSpTrapHdC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapHdC_Type.__name__ = "Integer32"
_SafSpTrapHdC_Object = MibScalar
safSpTrapHdC = _SafSpTrapHdC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 5),
    _SafSpTrapHdC_Type()
)
safSpTrapHdC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapHdC.setStatus("mandatory")


class _SafSpTrapFanC_Type(Integer32):
    """Custom type safSpTrapFanC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapFanC_Type.__name__ = "Integer32"
_SafSpTrapFanC_Object = MibScalar
safSpTrapFanC = _SafSpTrapFanC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 6),
    _SafSpTrapFanC_Type()
)
safSpTrapFanC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapFanC.setStatus("mandatory")


class _SafSpTrapIhcC_Type(Integer32):
    """Custom type safSpTrapIhcC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapIhcC_Type.__name__ = "Integer32"
_SafSpTrapIhcC_Object = MibScalar
safSpTrapIhcC = _SafSpTrapIhcC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 7),
    _SafSpTrapIhcC_Type()
)
safSpTrapIhcC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapIhcC.setStatus("mandatory")


class _SafSpTrapCPUC_Type(Integer32):
    """Custom type safSpTrapCPUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapCPUC_Type.__name__ = "Integer32"
_SafSpTrapCPUC_Object = MibScalar
safSpTrapCPUC = _SafSpTrapCPUC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 8),
    _SafSpTrapCPUC_Type()
)
safSpTrapCPUC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapCPUC.setStatus("mandatory")


class _SafSpTrapMemoryC_Type(Integer32):
    """Custom type safSpTrapMemoryC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapMemoryC_Type.__name__ = "Integer32"
_SafSpTrapMemoryC_Object = MibScalar
safSpTrapMemoryC = _SafSpTrapMemoryC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 9),
    _SafSpTrapMemoryC_Type()
)
safSpTrapMemoryC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapMemoryC.setStatus("mandatory")


class _SafSpTrapRdpsC_Type(Integer32):
    """Custom type safSpTrapRdpsC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapRdpsC_Type.__name__ = "Integer32"
_SafSpTrapRdpsC_Object = MibScalar
safSpTrapRdpsC = _SafSpTrapRdpsC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 10),
    _SafSpTrapRdpsC_Type()
)
safSpTrapRdpsC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapRdpsC.setStatus("mandatory")


class _SafSpTrapHardwareC_Type(Integer32):
    """Custom type safSpTrapHardwareC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapHardwareC_Type.__name__ = "Integer32"
_SafSpTrapHardwareC_Object = MibScalar
safSpTrapHardwareC = _SafSpTrapHardwareC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 11),
    _SafSpTrapHardwareC_Type()
)
safSpTrapHardwareC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapHardwareC.setStatus("mandatory")


class _SafSpTrapRdpsN_Type(Integer32):
    """Custom type safSpTrapRdpsN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapRdpsN_Type.__name__ = "Integer32"
_SafSpTrapRdpsN_Object = MibScalar
safSpTrapRdpsN = _SafSpTrapRdpsN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 12),
    _SafSpTrapRdpsN_Type()
)
safSpTrapRdpsN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapRdpsN.setStatus("mandatory")


class _SafSpTrapTempN_Type(Integer32):
    """Custom type safSpTrapTempN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapTempN_Type.__name__ = "Integer32"
_SafSpTrapTempN_Object = MibScalar
safSpTrapTempN = _SafSpTrapTempN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 13),
    _SafSpTrapTempN_Type()
)
safSpTrapTempN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapTempN.setStatus("mandatory")


class _SafSpTrapVoltN_Type(Integer32):
    """Custom type safSpTrapVoltN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapVoltN_Type.__name__ = "Integer32"
_SafSpTrapVoltN_Object = MibScalar
safSpTrapVoltN = _SafSpTrapVoltN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 14),
    _SafSpTrapVoltN_Type()
)
safSpTrapVoltN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapVoltN.setStatus("mandatory")


class _SafSpTrapPowerN_Type(Integer32):
    """Custom type safSpTrapPowerN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapPowerN_Type.__name__ = "Integer32"
_SafSpTrapPowerN_Object = MibScalar
safSpTrapPowerN = _SafSpTrapPowerN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 15),
    _SafSpTrapPowerN_Type()
)
safSpTrapPowerN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapPowerN.setStatus("mandatory")


class _SafSpTrapFanN_Type(Integer32):
    """Custom type safSpTrapFanN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapFanN_Type.__name__ = "Integer32"
_SafSpTrapFanN_Object = MibScalar
safSpTrapFanN = _SafSpTrapFanN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 16),
    _SafSpTrapFanN_Type()
)
safSpTrapFanN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapFanN.setStatus("mandatory")


class _SafSpTrapCPUN_Type(Integer32):
    """Custom type safSpTrapCPUN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapCPUN_Type.__name__ = "Integer32"
_SafSpTrapCPUN_Object = MibScalar
safSpTrapCPUN = _SafSpTrapCPUN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 17),
    _SafSpTrapCPUN_Type()
)
safSpTrapCPUN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapCPUN.setStatus("mandatory")


class _SafSpTrapMemoryN_Type(Integer32):
    """Custom type safSpTrapMemoryN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapMemoryN_Type.__name__ = "Integer32"
_SafSpTrapMemoryN_Object = MibScalar
safSpTrapMemoryN = _SafSpTrapMemoryN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 18),
    _SafSpTrapMemoryN_Type()
)
safSpTrapMemoryN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapMemoryN.setStatus("mandatory")


class _SafSpTrapHardwareN_Type(Integer32):
    """Custom type safSpTrapHardwareN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapHardwareN_Type.__name__ = "Integer32"
_SafSpTrapHardwareN_Object = MibScalar
safSpTrapHardwareN = _SafSpTrapHardwareN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 19),
    _SafSpTrapHardwareN_Type()
)
safSpTrapHardwareN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapHardwareN.setStatus("mandatory")


class _SafSpTrapRLogin_Type(Integer32):
    """Custom type safSpTrapRLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapRLogin_Type.__name__ = "Integer32"
_SafSpTrapRLogin_Object = MibScalar
safSpTrapRLogin = _SafSpTrapRLogin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 20),
    _SafSpTrapRLogin_Type()
)
safSpTrapRLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapRLogin.setStatus("mandatory")


class _SafSpTrapOsToS_Type(Integer32):
    """Custom type safSpTrapOsToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapOsToS_Type.__name__ = "Integer32"
_SafSpTrapOsToS_Object = MibScalar
safSpTrapOsToS = _SafSpTrapOsToS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 21),
    _SafSpTrapOsToS_Type()
)
safSpTrapOsToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapOsToS.setStatus("mandatory")


class _SafSpTrapAppS_Type(Integer32):
    """Custom type safSpTrapAppS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapAppS_Type.__name__ = "Integer32"
_SafSpTrapAppS_Object = MibScalar
safSpTrapAppS = _SafSpTrapAppS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 22),
    _SafSpTrapAppS_Type()
)
safSpTrapAppS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapAppS.setStatus("mandatory")


class _SafSpTrapPowerS_Type(Integer32):
    """Custom type safSpTrapPowerS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapPowerS_Type.__name__ = "Integer32"
_SafSpTrapPowerS_Object = MibScalar
safSpTrapPowerS = _SafSpTrapPowerS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 23),
    _SafSpTrapPowerS_Type()
)
safSpTrapPowerS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapPowerS.setStatus("mandatory")


class _SafSpTrapBootS_Type(Integer32):
    """Custom type safSpTrapBootS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapBootS_Type.__name__ = "Integer32"
_SafSpTrapBootS_Object = MibScalar
safSpTrapBootS = _SafSpTrapBootS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 24),
    _SafSpTrapBootS_Type()
)
safSpTrapBootS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapBootS.setStatus("mandatory")


class _SafSpTrapLdrToS_Type(Integer32):
    """Custom type safSpTrapLdrToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapLdrToS_Type.__name__ = "Integer32"
_SafSpTrapLdrToS_Object = MibScalar
safSpTrapLdrToS = _SafSpTrapLdrToS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 25),
    _SafSpTrapLdrToS_Type()
)
safSpTrapLdrToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapLdrToS.setStatus("mandatory")


class _SafSpTrapPFAS_Type(Integer32):
    """Custom type safSpTrapPFAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapPFAS_Type.__name__ = "Integer32"
_SafSpTrapPFAS_Object = MibScalar
safSpTrapPFAS = _SafSpTrapPFAS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 26),
    _SafSpTrapPFAS_Type()
)
safSpTrapPFAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapPFAS.setStatus("mandatory")


class _SafSpTrapSysLogS_Type(Integer32):
    """Custom type safSpTrapSysLogS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapSysLogS_Type.__name__ = "Integer32"
_SafSpTrapSysLogS_Object = MibScalar
safSpTrapSysLogS = _SafSpTrapSysLogS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 27),
    _SafSpTrapSysLogS_Type()
)
safSpTrapSysLogS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapSysLogS.setStatus("mandatory")


class _SafSpTrapNwChangeS_Type(Integer32):
    """Custom type safSpTrapNwChangeS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SafSpTrapNwChangeS_Type.__name__ = "Integer32"
_SafSpTrapNwChangeS_Object = MibScalar
safSpTrapNwChangeS = _SafSpTrapNwChangeS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 10, 28),
    _SafSpTrapNwChangeS_Type()
)
safSpTrapNwChangeS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safSpTrapNwChangeS.setStatus("mandatory")
_CustomSecuritySettings_ObjectIdentity = ObjectIdentity
customSecuritySettings = _CustomSecuritySettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20)
)


class _LoginPasswordRequired_Type(Integer32):
    """Custom type loginPasswordRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LoginPasswordRequired_Type.__name__ = "Integer32"
_LoginPasswordRequired_Object = MibScalar
loginPasswordRequired = _LoginPasswordRequired_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 1),
    _LoginPasswordRequired_Type()
)
loginPasswordRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginPasswordRequired.setStatus("mandatory")
_PasswordExpirationPeriod_Type = Integer32
_PasswordExpirationPeriod_Object = MibScalar
passwordExpirationPeriod = _PasswordExpirationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 2),
    _PasswordExpirationPeriod_Type()
)
passwordExpirationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwordExpirationPeriod.setStatus("mandatory")


class _MinimumPasswordReuseCycle_Type(Integer32):
    """Custom type minimumPasswordReuseCycle based on Integer32"""
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
        *(("fivePasswords", 5),
          ("fourPasswords", 4),
          ("none", 0),
          ("onePassword", 1),
          ("threePasswords", 3),
          ("twoPasswords", 2))
    )


_MinimumPasswordReuseCycle_Type.__name__ = "Integer32"
_MinimumPasswordReuseCycle_Object = MibScalar
minimumPasswordReuseCycle = _MinimumPasswordReuseCycle_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 3),
    _MinimumPasswordReuseCycle_Type()
)
minimumPasswordReuseCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minimumPasswordReuseCycle.setStatus("mandatory")


class _ComplexPasswordRulesEnforced_Type(Integer32):
    """Custom type complexPasswordRulesEnforced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ComplexPasswordRulesEnforced_Type.__name__ = "Integer32"
_ComplexPasswordRulesEnforced_Object = MibScalar
complexPasswordRulesEnforced = _ComplexPasswordRulesEnforced_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 4),
    _ComplexPasswordRulesEnforced_Type()
)
complexPasswordRulesEnforced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    complexPasswordRulesEnforced.setStatus("mandatory")


class _MinimumPasswordLength_Type(Integer32):
    """Custom type minimumPasswordLength based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("passwordLength10", 10),
          ("passwordLength11", 11),
          ("passwordLength12", 12),
          ("passwordLength13", 13),
          ("passwordLength14", 14),
          ("passwordLength15", 15),
          ("passwordLength16", 16),
          ("passwordLength5", 5),
          ("passwordLength6", 6),
          ("passwordLength7", 7),
          ("passwordLength8", 8),
          ("passwordLength9", 9),
          ("passwordLengthFour", 4),
          ("passwordLengthOne", 1),
          ("passwordLengthThree", 3),
          ("passwordLengthTwo", 2))
    )


_MinimumPasswordLength_Type.__name__ = "Integer32"
_MinimumPasswordLength_Object = MibScalar
minimumPasswordLength = _MinimumPasswordLength_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 5),
    _MinimumPasswordLength_Type()
)
minimumPasswordLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minimumPasswordLength.setStatus("mandatory")


class _DefaultAdminPasswordExpired_Type(Integer32):
    """Custom type defaultAdminPasswordExpired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DefaultAdminPasswordExpired_Type.__name__ = "Integer32"
_DefaultAdminPasswordExpired_Object = MibScalar
defaultAdminPasswordExpired = _DefaultAdminPasswordExpired_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 6),
    _DefaultAdminPasswordExpired_Type()
)
defaultAdminPasswordExpired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultAdminPasswordExpired.setStatus("mandatory")


class _MinimumDiffCharsPassword_Type(Integer32):
    """Custom type minimumDiffCharsPassword based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("eightChars", 8),
          ("elevenChars", 11),
          ("fifteenChars", 15),
          ("fiveChars", 5),
          ("fourChars", 4),
          ("fourteenChars", 14),
          ("nineChars", 9),
          ("none", 0),
          ("oneChar", 1),
          ("sevenChars", 7),
          ("sixChars", 6),
          ("tenChars", 10),
          ("thirteenChars", 13),
          ("threeChars", 3),
          ("twelveChars", 12),
          ("twoChars", 2))
    )


_MinimumDiffCharsPassword_Type.__name__ = "Integer32"
_MinimumDiffCharsPassword_Object = MibScalar
minimumDiffCharsPassword = _MinimumDiffCharsPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 7),
    _MinimumDiffCharsPassword_Type()
)
minimumDiffCharsPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minimumDiffCharsPassword.setStatus("mandatory")


class _ChangePasswordFirstAccess_Type(Integer32):
    """Custom type changePasswordFirstAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ChangePasswordFirstAccess_Type.__name__ = "Integer32"
_ChangePasswordFirstAccess_Object = MibScalar
changePasswordFirstAccess = _ChangePasswordFirstAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 8),
    _ChangePasswordFirstAccess_Type()
)
changePasswordFirstAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    changePasswordFirstAccess.setStatus("mandatory")


class _AccountLockoutPeriod_Type(Integer32):
    """Custom type accountLockoutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              10,
              15,
              20,
              30,
              60,
              120,
              180,
              240)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 15),
          ("fiveMinutes", 5),
          ("nowait", 0),
          ("oneEightyMinutes", 180),
          ("oneMinute", 1),
          ("oneTwentyMinutes", 120),
          ("sixtyMinutes", 60),
          ("tenMinutes", 10),
          ("thirtyMinutes", 30),
          ("twentyMinutes", 20),
          ("twoFortyMinutes", 240),
          ("twoMinutes", 2))
    )


_AccountLockoutPeriod_Type.__name__ = "Integer32"
_AccountLockoutPeriod_Object = MibScalar
accountLockoutPeriod = _AccountLockoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 9),
    _AccountLockoutPeriod_Type()
)
accountLockoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountLockoutPeriod.setStatus("mandatory")


class _MaxLoginFailures_Type(Integer32):
    """Custom type maxLoginFailures based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eightTimes", 8),
          ("fiveTimes", 5),
          ("fourTimes", 4),
          ("nineTimes", 9),
          ("none", 0),
          ("oneTime", 1),
          ("sevenTimes", 7),
          ("sixTimes", 6),
          ("tenTimes", 10),
          ("threeTimes", 3),
          ("twoTimes", 2))
    )


_MaxLoginFailures_Type.__name__ = "Integer32"
_MaxLoginFailures_Object = MibScalar
maxLoginFailures = _MaxLoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 10),
    _MaxLoginFailures_Type()
)
maxLoginFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxLoginFailures.setStatus("mandatory")
_PasswordChangeInterval_Type = Integer32
_PasswordChangeInterval_Object = MibScalar
passwordChangeInterval = _PasswordChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 1, 20, 11),
    _PasswordChangeInterval_Type()
)
passwordChangeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwordChangeInterval.setStatus("mandatory")
_SerialPortCfg_ObjectIdentity = ObjectIdentity
serialPortCfg = _SerialPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 2)
)


class _PortBaud_Type(Integer32):
    """Custom type portBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("baud115200", 7),
          ("baud19200", 4),
          ("baud38400", 5),
          ("baud57600", 6),
          ("baud9600", 3))
    )


_PortBaud_Type.__name__ = "Integer32"
_PortBaud_Object = MibScalar
portBaud = _PortBaud_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 2, 1),
    _PortBaud_Type()
)
portBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaud.setStatus("mandatory")


class _PortParity_Type(Integer32):
    """Custom type portParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 0),
          ("odd", 1))
    )


_PortParity_Type.__name__ = "Integer32"
_PortParity_Object = MibScalar
portParity = _PortParity_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 2, 2),
    _PortParity_Type()
)
portParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portParity.setStatus("mandatory")
_SerialRedirect_ObjectIdentity = ObjectIdentity
serialRedirect = _SerialRedirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 2, 3)
)


class _EnterCLIkeySeq_Type(OctetString):
    """Custom type enterCLIkeySeq based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EnterCLIkeySeq_Type.__name__ = "OctetString"
_EnterCLIkeySeq_Object = MibScalar
enterCLIkeySeq = _EnterCLIkeySeq_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 2, 3, 1),
    _EnterCLIkeySeq_Type()
)
enterCLIkeySeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enterCLIkeySeq.setStatus("mandatory")


class _PortStopBits_Type(Integer32):
    """Custom type portStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oneStopbit", 0),
          ("twoOrOnePtFive", 1))
    )


_PortStopBits_Type.__name__ = "Integer32"
_PortStopBits_Object = MibScalar
portStopBits = _PortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 2, 4),
    _PortStopBits_Type()
)
portStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portStopBits.setStatus("mandatory")


class _PortCLImode_Type(Integer32):
    """Custom type portCLImode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cliDisable", 0),
          ("cliWithEMScompatibleKeystrokeSeq", 1),
          ("cliWithUserDefinedKeystrokeSeq", 2))
    )


_PortCLImode_Type.__name__ = "Integer32"
_PortCLImode_Object = MibScalar
portCLImode = _PortCLImode_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 2, 18),
    _PortCLImode_Type()
)
portCLImode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCLImode.setStatus("mandatory")
_RemoteAlertIds_ObjectIdentity = ObjectIdentity
remoteAlertIds = _RemoteAlertIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3)
)
_RemoteAlertIdsTable_Object = MibTable
remoteAlertIdsTable = _RemoteAlertIdsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    remoteAlertIdsTable.setStatus("mandatory")
_RemoteAlertIdsEntry_Object = MibTableRow
remoteAlertIdsEntry = _RemoteAlertIdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1)
)
remoteAlertIdsEntry.setIndexNames(
    (0, "IMM-MIB", "remoteAlertIdEntryIndex"),
)
if mibBuilder.loadTexts:
    remoteAlertIdsEntry.setStatus("mandatory")


class _RemoteAlertIdEntryIndex_Type(Integer32):
    """Custom type remoteAlertIdEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_RemoteAlertIdEntryIndex_Type.__name__ = "Integer32"
_RemoteAlertIdEntryIndex_Object = MibTableColumn
remoteAlertIdEntryIndex = _RemoteAlertIdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 1),
    _RemoteAlertIdEntryIndex_Type()
)
remoteAlertIdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAlertIdEntryIndex.setStatus("mandatory")


class _RemoteAlertIdEntryStatus_Type(Integer32):
    """Custom type remoteAlertIdEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_RemoteAlertIdEntryStatus_Type.__name__ = "Integer32"
_RemoteAlertIdEntryStatus_Object = MibTableColumn
remoteAlertIdEntryStatus = _RemoteAlertIdEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 2),
    _RemoteAlertIdEntryStatus_Type()
)
remoteAlertIdEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntryStatus.setStatus("mandatory")


class _RemoteAlertIdEntryName_Type(OctetString):
    """Custom type remoteAlertIdEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RemoteAlertIdEntryName_Type.__name__ = "OctetString"
_RemoteAlertIdEntryName_Object = MibTableColumn
remoteAlertIdEntryName = _RemoteAlertIdEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 3),
    _RemoteAlertIdEntryName_Type()
)
remoteAlertIdEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntryName.setStatus("mandatory")


class _RemoteAlertIdEmailAddr_Type(OctetString):
    """Custom type remoteAlertIdEmailAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 320),
    )


_RemoteAlertIdEmailAddr_Type.__name__ = "OctetString"
_RemoteAlertIdEmailAddr_Object = MibTableColumn
remoteAlertIdEmailAddr = _RemoteAlertIdEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 4),
    _RemoteAlertIdEmailAddr_Type()
)
remoteAlertIdEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEmailAddr.setStatus("mandatory")


class _RemoteAlertIdEntryCriticalAlert_Type(Integer32):
    """Custom type remoteAlertIdEntryCriticalAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoteAlertIdEntryCriticalAlert_Type.__name__ = "Integer32"
_RemoteAlertIdEntryCriticalAlert_Object = MibTableColumn
remoteAlertIdEntryCriticalAlert = _RemoteAlertIdEntryCriticalAlert_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 5),
    _RemoteAlertIdEntryCriticalAlert_Type()
)
remoteAlertIdEntryCriticalAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntryCriticalAlert.setStatus("mandatory")


class _RemoteAlertIdEntryWarningAlert_Type(Integer32):
    """Custom type remoteAlertIdEntryWarningAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoteAlertIdEntryWarningAlert_Type.__name__ = "Integer32"
_RemoteAlertIdEntryWarningAlert_Object = MibTableColumn
remoteAlertIdEntryWarningAlert = _RemoteAlertIdEntryWarningAlert_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 6),
    _RemoteAlertIdEntryWarningAlert_Type()
)
remoteAlertIdEntryWarningAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntryWarningAlert.setStatus("mandatory")


class _RemoteAlertIdEntrySystemAlert_Type(Integer32):
    """Custom type remoteAlertIdEntrySystemAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RemoteAlertIdEntrySystemAlert_Type.__name__ = "Integer32"
_RemoteAlertIdEntrySystemAlert_Object = MibTableColumn
remoteAlertIdEntrySystemAlert = _RemoteAlertIdEntrySystemAlert_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 7),
    _RemoteAlertIdEntrySystemAlert_Type()
)
remoteAlertIdEntrySystemAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntrySystemAlert.setStatus("mandatory")


class _RemoteAlertIdEntryAttachmentsToEmailAlerts_Type(Integer32):
    """Custom type remoteAlertIdEntryAttachmentsToEmailAlerts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("attachEventLog", 1),
          ("noAttachments", 0))
    )


_RemoteAlertIdEntryAttachmentsToEmailAlerts_Type.__name__ = "Integer32"
_RemoteAlertIdEntryAttachmentsToEmailAlerts_Object = MibTableColumn
remoteAlertIdEntryAttachmentsToEmailAlerts = _RemoteAlertIdEntryAttachmentsToEmailAlerts_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 8),
    _RemoteAlertIdEntryAttachmentsToEmailAlerts_Type()
)
remoteAlertIdEntryAttachmentsToEmailAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntryAttachmentsToEmailAlerts.setStatus("mandatory")
_RemoteAlertIdEntrySyslogPortAssignment_Type = Integer32
_RemoteAlertIdEntrySyslogPortAssignment_Object = MibTableColumn
remoteAlertIdEntrySyslogPortAssignment = _RemoteAlertIdEntrySyslogPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 9),
    _RemoteAlertIdEntrySyslogPortAssignment_Type()
)
remoteAlertIdEntrySyslogPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntrySyslogPortAssignment.setStatus("mandatory")


class _RemoteAlertIdEntrySyslogHostname_Type(OctetString):
    """Custom type remoteAlertIdEntrySyslogHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteAlertIdEntrySyslogHostname_Type.__name__ = "OctetString"
_RemoteAlertIdEntrySyslogHostname_Object = MibTableColumn
remoteAlertIdEntrySyslogHostname = _RemoteAlertIdEntrySyslogHostname_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 10),
    _RemoteAlertIdEntrySyslogHostname_Type()
)
remoteAlertIdEntrySyslogHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntrySyslogHostname.setStatus("mandatory")


class _RemoteAlertIdEntryType_Type(Integer32):
    """Custom type remoteAlertIdEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("email", 1),
          ("syslog", 2))
    )


_RemoteAlertIdEntryType_Type.__name__ = "Integer32"
_RemoteAlertIdEntryType_Object = MibTableColumn
remoteAlertIdEntryType = _RemoteAlertIdEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 1, 1, 11),
    _RemoteAlertIdEntryType_Type()
)
remoteAlertIdEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAlertIdEntryType.setStatus("mandatory")
_RemoteAlertFiltersTable_Object = MibTable
remoteAlertFiltersTable = _RemoteAlertFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    remoteAlertFiltersTable.setStatus("mandatory")
_RemoteAlertFiltersEntry_Object = MibTableRow
remoteAlertFiltersEntry = _RemoteAlertFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1)
)
remoteAlertFiltersEntry.setIndexNames(
    (0, "IMM-MIB", "rafIndex"),
)
if mibBuilder.loadTexts:
    remoteAlertFiltersEntry.setStatus("mandatory")


class _RafIndex_Type(Integer32):
    """Custom type rafIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RafIndex_Type.__name__ = "Integer32"
_RafIndex_Object = MibTableColumn
rafIndex = _RafIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 1),
    _RafIndex_Type()
)
rafIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rafIndex.setStatus("mandatory")


class _RafSpTrapTempC_Type(Integer32):
    """Custom type rafSpTrapTempC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapTempC_Type.__name__ = "Integer32"
_RafSpTrapTempC_Object = MibTableColumn
rafSpTrapTempC = _RafSpTrapTempC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 2),
    _RafSpTrapTempC_Type()
)
rafSpTrapTempC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapTempC.setStatus("mandatory")


class _RafSpTrapVoltC_Type(Integer32):
    """Custom type rafSpTrapVoltC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapVoltC_Type.__name__ = "Integer32"
_RafSpTrapVoltC_Object = MibTableColumn
rafSpTrapVoltC = _RafSpTrapVoltC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 3),
    _RafSpTrapVoltC_Type()
)
rafSpTrapVoltC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapVoltC.setStatus("mandatory")


class _RafSpTrapPowerC_Type(Integer32):
    """Custom type rafSpTrapPowerC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapPowerC_Type.__name__ = "Integer32"
_RafSpTrapPowerC_Object = MibTableColumn
rafSpTrapPowerC = _RafSpTrapPowerC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 4),
    _RafSpTrapPowerC_Type()
)
rafSpTrapPowerC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapPowerC.setStatus("mandatory")


class _RafSpTrapHdC_Type(Integer32):
    """Custom type rafSpTrapHdC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapHdC_Type.__name__ = "Integer32"
_RafSpTrapHdC_Object = MibTableColumn
rafSpTrapHdC = _RafSpTrapHdC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 5),
    _RafSpTrapHdC_Type()
)
rafSpTrapHdC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapHdC.setStatus("mandatory")


class _RafSpTrapFanC_Type(Integer32):
    """Custom type rafSpTrapFanC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapFanC_Type.__name__ = "Integer32"
_RafSpTrapFanC_Object = MibTableColumn
rafSpTrapFanC = _RafSpTrapFanC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 6),
    _RafSpTrapFanC_Type()
)
rafSpTrapFanC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapFanC.setStatus("mandatory")


class _RafSpTrapIhcC_Type(Integer32):
    """Custom type rafSpTrapIhcC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapIhcC_Type.__name__ = "Integer32"
_RafSpTrapIhcC_Object = MibTableColumn
rafSpTrapIhcC = _RafSpTrapIhcC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 7),
    _RafSpTrapIhcC_Type()
)
rafSpTrapIhcC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapIhcC.setStatus("mandatory")


class _RafSpTrapCPUC_Type(Integer32):
    """Custom type rafSpTrapCPUC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapCPUC_Type.__name__ = "Integer32"
_RafSpTrapCPUC_Object = MibTableColumn
rafSpTrapCPUC = _RafSpTrapCPUC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 8),
    _RafSpTrapCPUC_Type()
)
rafSpTrapCPUC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapCPUC.setStatus("mandatory")


class _RafSpTrapMemoryC_Type(Integer32):
    """Custom type rafSpTrapMemoryC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapMemoryC_Type.__name__ = "Integer32"
_RafSpTrapMemoryC_Object = MibTableColumn
rafSpTrapMemoryC = _RafSpTrapMemoryC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 9),
    _RafSpTrapMemoryC_Type()
)
rafSpTrapMemoryC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapMemoryC.setStatus("mandatory")


class _RafSpTrapRdpsC_Type(Integer32):
    """Custom type rafSpTrapRdpsC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapRdpsC_Type.__name__ = "Integer32"
_RafSpTrapRdpsC_Object = MibTableColumn
rafSpTrapRdpsC = _RafSpTrapRdpsC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 10),
    _RafSpTrapRdpsC_Type()
)
rafSpTrapRdpsC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapRdpsC.setStatus("mandatory")


class _RafSpTrapHardwareC_Type(Integer32):
    """Custom type rafSpTrapHardwareC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapHardwareC_Type.__name__ = "Integer32"
_RafSpTrapHardwareC_Object = MibTableColumn
rafSpTrapHardwareC = _RafSpTrapHardwareC_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 11),
    _RafSpTrapHardwareC_Type()
)
rafSpTrapHardwareC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapHardwareC.setStatus("mandatory")


class _RafSpTrapRdpsN_Type(Integer32):
    """Custom type rafSpTrapRdpsN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapRdpsN_Type.__name__ = "Integer32"
_RafSpTrapRdpsN_Object = MibTableColumn
rafSpTrapRdpsN = _RafSpTrapRdpsN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 12),
    _RafSpTrapRdpsN_Type()
)
rafSpTrapRdpsN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapRdpsN.setStatus("mandatory")


class _RafSpTrapTempN_Type(Integer32):
    """Custom type rafSpTrapTempN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapTempN_Type.__name__ = "Integer32"
_RafSpTrapTempN_Object = MibTableColumn
rafSpTrapTempN = _RafSpTrapTempN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 13),
    _RafSpTrapTempN_Type()
)
rafSpTrapTempN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapTempN.setStatus("mandatory")


class _RafSpTrapVoltN_Type(Integer32):
    """Custom type rafSpTrapVoltN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapVoltN_Type.__name__ = "Integer32"
_RafSpTrapVoltN_Object = MibTableColumn
rafSpTrapVoltN = _RafSpTrapVoltN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 14),
    _RafSpTrapVoltN_Type()
)
rafSpTrapVoltN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapVoltN.setStatus("mandatory")


class _RafSpTrapPowerN_Type(Integer32):
    """Custom type rafSpTrapPowerN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapPowerN_Type.__name__ = "Integer32"
_RafSpTrapPowerN_Object = MibTableColumn
rafSpTrapPowerN = _RafSpTrapPowerN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 15),
    _RafSpTrapPowerN_Type()
)
rafSpTrapPowerN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapPowerN.setStatus("mandatory")


class _RafSpTrapFanN_Type(Integer32):
    """Custom type rafSpTrapFanN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapFanN_Type.__name__ = "Integer32"
_RafSpTrapFanN_Object = MibTableColumn
rafSpTrapFanN = _RafSpTrapFanN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 16),
    _RafSpTrapFanN_Type()
)
rafSpTrapFanN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapFanN.setStatus("mandatory")


class _RafSpTrapCPUN_Type(Integer32):
    """Custom type rafSpTrapCPUN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapCPUN_Type.__name__ = "Integer32"
_RafSpTrapCPUN_Object = MibTableColumn
rafSpTrapCPUN = _RafSpTrapCPUN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 17),
    _RafSpTrapCPUN_Type()
)
rafSpTrapCPUN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapCPUN.setStatus("mandatory")


class _RafSpTrapMemoryN_Type(Integer32):
    """Custom type rafSpTrapMemoryN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapMemoryN_Type.__name__ = "Integer32"
_RafSpTrapMemoryN_Object = MibTableColumn
rafSpTrapMemoryN = _RafSpTrapMemoryN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 18),
    _RafSpTrapMemoryN_Type()
)
rafSpTrapMemoryN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapMemoryN.setStatus("mandatory")


class _RafSpTrapHardwareN_Type(Integer32):
    """Custom type rafSpTrapHardwareN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapHardwareN_Type.__name__ = "Integer32"
_RafSpTrapHardwareN_Object = MibTableColumn
rafSpTrapHardwareN = _RafSpTrapHardwareN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 19),
    _RafSpTrapHardwareN_Type()
)
rafSpTrapHardwareN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapHardwareN.setStatus("mandatory")


class _RafSpTrapRLogin_Type(Integer32):
    """Custom type rafSpTrapRLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapRLogin_Type.__name__ = "Integer32"
_RafSpTrapRLogin_Object = MibTableColumn
rafSpTrapRLogin = _RafSpTrapRLogin_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 20),
    _RafSpTrapRLogin_Type()
)
rafSpTrapRLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapRLogin.setStatus("mandatory")


class _RafSpTrapOsToS_Type(Integer32):
    """Custom type rafSpTrapOsToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapOsToS_Type.__name__ = "Integer32"
_RafSpTrapOsToS_Object = MibTableColumn
rafSpTrapOsToS = _RafSpTrapOsToS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 21),
    _RafSpTrapOsToS_Type()
)
rafSpTrapOsToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapOsToS.setStatus("mandatory")


class _RafSpTrapAppS_Type(Integer32):
    """Custom type rafSpTrapAppS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapAppS_Type.__name__ = "Integer32"
_RafSpTrapAppS_Object = MibTableColumn
rafSpTrapAppS = _RafSpTrapAppS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 22),
    _RafSpTrapAppS_Type()
)
rafSpTrapAppS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapAppS.setStatus("mandatory")


class _RafSpTrapPowerS_Type(Integer32):
    """Custom type rafSpTrapPowerS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapPowerS_Type.__name__ = "Integer32"
_RafSpTrapPowerS_Object = MibTableColumn
rafSpTrapPowerS = _RafSpTrapPowerS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 23),
    _RafSpTrapPowerS_Type()
)
rafSpTrapPowerS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapPowerS.setStatus("mandatory")


class _RafSpTrapBootS_Type(Integer32):
    """Custom type rafSpTrapBootS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapBootS_Type.__name__ = "Integer32"
_RafSpTrapBootS_Object = MibTableColumn
rafSpTrapBootS = _RafSpTrapBootS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 24),
    _RafSpTrapBootS_Type()
)
rafSpTrapBootS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapBootS.setStatus("mandatory")


class _RafSpTrapLdrToS_Type(Integer32):
    """Custom type rafSpTrapLdrToS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapLdrToS_Type.__name__ = "Integer32"
_RafSpTrapLdrToS_Object = MibTableColumn
rafSpTrapLdrToS = _RafSpTrapLdrToS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 25),
    _RafSpTrapLdrToS_Type()
)
rafSpTrapLdrToS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapLdrToS.setStatus("mandatory")


class _RafSpTrapPFAS_Type(Integer32):
    """Custom type rafSpTrapPFAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapPFAS_Type.__name__ = "Integer32"
_RafSpTrapPFAS_Object = MibTableColumn
rafSpTrapPFAS = _RafSpTrapPFAS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 26),
    _RafSpTrapPFAS_Type()
)
rafSpTrapPFAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapPFAS.setStatus("mandatory")


class _RafSpTrapSysLogS_Type(Integer32):
    """Custom type rafSpTrapSysLogS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapSysLogS_Type.__name__ = "Integer32"
_RafSpTrapSysLogS_Object = MibTableColumn
rafSpTrapSysLogS = _RafSpTrapSysLogS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 27),
    _RafSpTrapSysLogS_Type()
)
rafSpTrapSysLogS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapSysLogS.setStatus("mandatory")


class _RafSpTrapNwChangeS_Type(Integer32):
    """Custom type rafSpTrapNwChangeS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RafSpTrapNwChangeS_Type.__name__ = "Integer32"
_RafSpTrapNwChangeS_Object = MibTableColumn
rafSpTrapNwChangeS = _RafSpTrapNwChangeS_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 2, 1, 28),
    _RafSpTrapNwChangeS_Type()
)
rafSpTrapNwChangeS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rafSpTrapNwChangeS.setStatus("mandatory")


class _GenerateTestAlert_Type(Integer32):
    """Custom type generateTestAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_GenerateTestAlert_Type.__name__ = "Integer32"
_GenerateTestAlert_Object = MibScalar
generateTestAlert = _GenerateTestAlert_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 3, 30),
    _GenerateTestAlert_Type()
)
generateTestAlert.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    generateTestAlert.setStatus("mandatory")
_RemoteAccessIds_ObjectIdentity = ObjectIdentity
remoteAccessIds = _RemoteAccessIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4)
)
_RemoteAccessIdsTable_Object = MibTable
remoteAccessIdsTable = _RemoteAccessIdsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    remoteAccessIdsTable.setStatus("mandatory")
_RemoteAccessIdsEntry_Object = MibTableRow
remoteAccessIdsEntry = _RemoteAccessIdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 1, 1)
)
remoteAccessIdsEntry.setIndexNames(
    (0, "IMM-MIB", "remoteAccessIdEntryIndex"),
)
if mibBuilder.loadTexts:
    remoteAccessIdsEntry.setStatus("mandatory")


class _RemoteAccessIdEntryIndex_Type(Integer32):
    """Custom type remoteAccessIdEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RemoteAccessIdEntryIndex_Type.__name__ = "Integer32"
_RemoteAccessIdEntryIndex_Object = MibTableColumn
remoteAccessIdEntryIndex = _RemoteAccessIdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 1, 1, 1),
    _RemoteAccessIdEntryIndex_Type()
)
remoteAccessIdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessIdEntryIndex.setStatus("mandatory")


class _RemoteAccessIdEntryUserId_Type(OctetString):
    """Custom type remoteAccessIdEntryUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RemoteAccessIdEntryUserId_Type.__name__ = "OctetString"
_RemoteAccessIdEntryUserId_Object = MibTableColumn
remoteAccessIdEntryUserId = _RemoteAccessIdEntryUserId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 1, 1, 2),
    _RemoteAccessIdEntryUserId_Type()
)
remoteAccessIdEntryUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessIdEntryUserId.setStatus("mandatory")


class _RemoteAccessIdEntryPassword_Type(OctetString):
    """Custom type remoteAccessIdEntryPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RemoteAccessIdEntryPassword_Type.__name__ = "OctetString"
_RemoteAccessIdEntryPassword_Object = MibTableColumn
remoteAccessIdEntryPassword = _RemoteAccessIdEntryPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 1, 1, 3),
    _RemoteAccessIdEntryPassword_Type()
)
remoteAccessIdEntryPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAccessIdEntryPassword.setStatus("mandatory")


class _RemoteAccessIdEntryUserPwdLeftDays_Type(Integer32):
    """Custom type remoteAccessIdEntryUserPwdLeftDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_RemoteAccessIdEntryUserPwdLeftDays_Type.__name__ = "Integer32"
_RemoteAccessIdEntryUserPwdLeftDays_Object = MibTableColumn
remoteAccessIdEntryUserPwdLeftDays = _RemoteAccessIdEntryUserPwdLeftDays_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 1, 1, 4),
    _RemoteAccessIdEntryUserPwdLeftDays_Type()
)
remoteAccessIdEntryUserPwdLeftDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteAccessIdEntryUserPwdLeftDays.setStatus("mandatory")
_RemoteAccessUserAuthorityLevelTable_Object = MibTable
remoteAccessUserAuthorityLevelTable = _RemoteAccessUserAuthorityLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    remoteAccessUserAuthorityLevelTable.setStatus("mandatory")
_RemoteAccessUserAuthorityLevelEntry_Object = MibTableRow
remoteAccessUserAuthorityLevelEntry = _RemoteAccessUserAuthorityLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1)
)
remoteAccessUserAuthorityLevelEntry.setIndexNames(
    (0, "IMM-MIB", "ualIndex"),
)
if mibBuilder.loadTexts:
    remoteAccessUserAuthorityLevelEntry.setStatus("mandatory")


class _UalIndex_Type(Integer32):
    """Custom type ualIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UalIndex_Type.__name__ = "Integer32"
_UalIndex_Object = MibTableColumn
ualIndex = _UalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 1),
    _UalIndex_Type()
)
ualIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualIndex.setStatus("mandatory")


class _UalId_Type(OctetString):
    """Custom type ualId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UalId_Type.__name__ = "OctetString"
_UalId_Object = MibTableColumn
ualId = _UalId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 2),
    _UalId_Type()
)
ualId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ualId.setStatus("mandatory")


class _UalSupervisor_Type(Integer32):
    """Custom type ualSupervisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalSupervisor_Type.__name__ = "Integer32"
_UalSupervisor_Object = MibTableColumn
ualSupervisor = _UalSupervisor_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 3),
    _UalSupervisor_Type()
)
ualSupervisor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualSupervisor.setStatus("mandatory")


class _UalReadOnly_Type(Integer32):
    """Custom type ualReadOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalReadOnly_Type.__name__ = "Integer32"
_UalReadOnly_Object = MibTableColumn
ualReadOnly = _UalReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 4),
    _UalReadOnly_Type()
)
ualReadOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualReadOnly.setStatus("mandatory")


class _UalAccountManagement_Type(Integer32):
    """Custom type ualAccountManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAccountManagement_Type.__name__ = "Integer32"
_UalAccountManagement_Object = MibTableColumn
ualAccountManagement = _UalAccountManagement_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 5),
    _UalAccountManagement_Type()
)
ualAccountManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualAccountManagement.setStatus("mandatory")


class _UalConsoleAccess_Type(Integer32):
    """Custom type ualConsoleAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalConsoleAccess_Type.__name__ = "Integer32"
_UalConsoleAccess_Object = MibTableColumn
ualConsoleAccess = _UalConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 6),
    _UalConsoleAccess_Type()
)
ualConsoleAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualConsoleAccess.setStatus("mandatory")


class _UalConsoleAndVirtualMediaAccess_Type(Integer32):
    """Custom type ualConsoleAndVirtualMediaAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalConsoleAndVirtualMediaAccess_Type.__name__ = "Integer32"
_UalConsoleAndVirtualMediaAccess_Object = MibTableColumn
ualConsoleAndVirtualMediaAccess = _UalConsoleAndVirtualMediaAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 7),
    _UalConsoleAndVirtualMediaAccess_Type()
)
ualConsoleAndVirtualMediaAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualConsoleAndVirtualMediaAccess.setStatus("mandatory")


class _UalServerPowerAccess_Type(Integer32):
    """Custom type ualServerPowerAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalServerPowerAccess_Type.__name__ = "Integer32"
_UalServerPowerAccess_Object = MibTableColumn
ualServerPowerAccess = _UalServerPowerAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 8),
    _UalServerPowerAccess_Type()
)
ualServerPowerAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualServerPowerAccess.setStatus("mandatory")


class _UalAllowClearLog_Type(Integer32):
    """Custom type ualAllowClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAllowClearLog_Type.__name__ = "Integer32"
_UalAllowClearLog_Object = MibTableColumn
ualAllowClearLog = _UalAllowClearLog_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 9),
    _UalAllowClearLog_Type()
)
ualAllowClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualAllowClearLog.setStatus("mandatory")


class _UalAdapterBasicConfig_Type(Integer32):
    """Custom type ualAdapterBasicConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAdapterBasicConfig_Type.__name__ = "Integer32"
_UalAdapterBasicConfig_Object = MibTableColumn
ualAdapterBasicConfig = _UalAdapterBasicConfig_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 10),
    _UalAdapterBasicConfig_Type()
)
ualAdapterBasicConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualAdapterBasicConfig.setStatus("mandatory")


class _UalAdapterNetworkAndSecurityConfig_Type(Integer32):
    """Custom type ualAdapterNetworkAndSecurityConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAdapterNetworkAndSecurityConfig_Type.__name__ = "Integer32"
_UalAdapterNetworkAndSecurityConfig_Object = MibTableColumn
ualAdapterNetworkAndSecurityConfig = _UalAdapterNetworkAndSecurityConfig_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 11),
    _UalAdapterNetworkAndSecurityConfig_Type()
)
ualAdapterNetworkAndSecurityConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualAdapterNetworkAndSecurityConfig.setStatus("mandatory")


class _UalAdapterAdvancedConfig_Type(Integer32):
    """Custom type ualAdapterAdvancedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UalAdapterAdvancedConfig_Type.__name__ = "Integer32"
_UalAdapterAdvancedConfig_Object = MibTableColumn
ualAdapterAdvancedConfig = _UalAdapterAdvancedConfig_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 4, 2, 1, 12),
    _UalAdapterAdvancedConfig_Type()
)
ualAdapterAdvancedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ualAdapterAdvancedConfig.setStatus("mandatory")
_GroupProfiles_ObjectIdentity = ObjectIdentity
groupProfiles = _GroupProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5)
)
_GroupIdsTable_Object = MibTable
groupIdsTable = _GroupIdsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    groupIdsTable.setStatus("mandatory")
_GroupIdsEntry_Object = MibTableRow
groupIdsEntry = _GroupIdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 1, 1)
)
groupIdsEntry.setIndexNames(
    (0, "IMM-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    groupIdsEntry.setStatus("mandatory")


class _GroupIndex_Type(Integer32):
    """Custom type groupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GroupIndex_Type.__name__ = "Integer32"
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 1, 1, 1),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupIndex.setStatus("mandatory")


class _GroupId_Type(OctetString):
    """Custom type groupId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GroupId_Type.__name__ = "OctetString"
_GroupId_Object = MibTableColumn
groupId = _GroupId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 1, 1, 2),
    _GroupId_Type()
)
groupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupId.setStatus("mandatory")
_GroupRole_Type = OctetString
_GroupRole_Object = MibTableColumn
groupRole = _GroupRole_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 1, 1, 3),
    _GroupRole_Type()
)
groupRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRole.setStatus("mandatory")
_GroupRBSroleTable_Object = MibTable
groupRBSroleTable = _GroupRBSroleTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    groupRBSroleTable.setStatus("mandatory")
_GroupRBSroleEntry_Object = MibTableRow
groupRBSroleEntry = _GroupRBSroleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1)
)
groupRBSroleEntry.setIndexNames(
    (0, "IMM-MIB", "groupRBSroleIndex"),
)
if mibBuilder.loadTexts:
    groupRBSroleEntry.setStatus("mandatory")


class _GroupRBSroleIndex_Type(Integer32):
    """Custom type groupRBSroleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GroupRBSroleIndex_Type.__name__ = "Integer32"
_GroupRBSroleIndex_Object = MibTableColumn
groupRBSroleIndex = _GroupRBSroleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 1),
    _GroupRBSroleIndex_Type()
)
groupRBSroleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSroleIndex.setStatus("mandatory")


class _GroupRBSroleId_Type(OctetString):
    """Custom type groupRBSroleId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_GroupRBSroleId_Type.__name__ = "OctetString"
_GroupRBSroleId_Object = MibTableColumn
groupRBSroleId = _GroupRBSroleId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 2),
    _GroupRBSroleId_Type()
)
groupRBSroleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupRBSroleId.setStatus("mandatory")


class _GroupRBSSupervisor_Type(Integer32):
    """Custom type groupRBSSupervisor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSSupervisor_Type.__name__ = "Integer32"
_GroupRBSSupervisor_Object = MibTableColumn
groupRBSSupervisor = _GroupRBSSupervisor_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 3),
    _GroupRBSSupervisor_Type()
)
groupRBSSupervisor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupRBSSupervisor.setStatus("mandatory")


class _GroupRBSOperator_Type(Integer32):
    """Custom type groupRBSOperator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSOperator_Type.__name__ = "Integer32"
_GroupRBSOperator_Object = MibTableColumn
groupRBSOperator = _GroupRBSOperator_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 4),
    _GroupRBSOperator_Type()
)
groupRBSOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupRBSOperator.setStatus("mandatory")


class _GroupRBSNetworkSecurity_Type(Integer32):
    """Custom type groupRBSNetworkSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSNetworkSecurity_Type.__name__ = "Integer32"
_GroupRBSNetworkSecurity_Object = MibTableColumn
groupRBSNetworkSecurity = _GroupRBSNetworkSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 5),
    _GroupRBSNetworkSecurity_Type()
)
groupRBSNetworkSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupRBSNetworkSecurity.setStatus("mandatory")


class _GroupRBSUserAccountManagement_Type(Integer32):
    """Custom type groupRBSUserAccountManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSUserAccountManagement_Type.__name__ = "Integer32"
_GroupRBSUserAccountManagement_Object = MibTableColumn
groupRBSUserAccountManagement = _GroupRBSUserAccountManagement_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 6),
    _GroupRBSUserAccountManagement_Type()
)
groupRBSUserAccountManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupRBSUserAccountManagement.setStatus("mandatory")


class _GroupRBSRemoteConsoleAccess_Type(Integer32):
    """Custom type groupRBSRemoteConsoleAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSRemoteConsoleAccess_Type.__name__ = "Integer32"
_GroupRBSRemoteConsoleAccess_Object = MibTableColumn
groupRBSRemoteConsoleAccess = _GroupRBSRemoteConsoleAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 7),
    _GroupRBSRemoteConsoleAccess_Type()
)
groupRBSRemoteConsoleAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupRBSRemoteConsoleAccess.setStatus("mandatory")


class _GroupRBSRemoteConsoleRemoteDiskAccess_Type(Integer32):
    """Custom type groupRBSRemoteConsoleRemoteDiskAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSRemoteConsoleRemoteDiskAccess_Type.__name__ = "Integer32"
_GroupRBSRemoteConsoleRemoteDiskAccess_Object = MibTableColumn
groupRBSRemoteConsoleRemoteDiskAccess = _GroupRBSRemoteConsoleRemoteDiskAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 8),
    _GroupRBSRemoteConsoleRemoteDiskAccess_Type()
)
groupRBSRemoteConsoleRemoteDiskAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupRBSRemoteConsoleRemoteDiskAccess.setStatus("mandatory")


class _GroupRBSServerPowerRestartAccess_Type(Integer32):
    """Custom type groupRBSServerPowerRestartAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSServerPowerRestartAccess_Type.__name__ = "Integer32"
_GroupRBSServerPowerRestartAccess_Object = MibTableColumn
groupRBSServerPowerRestartAccess = _GroupRBSServerPowerRestartAccess_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 9),
    _GroupRBSServerPowerRestartAccess_Type()
)
groupRBSServerPowerRestartAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupRBSServerPowerRestartAccess.setStatus("mandatory")


class _GroupRBSBasicAdapterConfiguration_Type(Integer32):
    """Custom type groupRBSBasicAdapterConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSBasicAdapterConfiguration_Type.__name__ = "Integer32"
_GroupRBSBasicAdapterConfiguration_Object = MibTableColumn
groupRBSBasicAdapterConfiguration = _GroupRBSBasicAdapterConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 10),
    _GroupRBSBasicAdapterConfiguration_Type()
)
groupRBSBasicAdapterConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupRBSBasicAdapterConfiguration.setStatus("mandatory")


class _GroupRBSClearEventLog_Type(Integer32):
    """Custom type groupRBSClearEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSClearEventLog_Type.__name__ = "Integer32"
_GroupRBSClearEventLog_Object = MibTableColumn
groupRBSClearEventLog = _GroupRBSClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 11),
    _GroupRBSClearEventLog_Type()
)
groupRBSClearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupRBSClearEventLog.setStatus("mandatory")


class _GroupRBSAdvancedAdapterConfiguration_Type(Integer32):
    """Custom type groupRBSAdvancedAdapterConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_GroupRBSAdvancedAdapterConfiguration_Type.__name__ = "Integer32"
_GroupRBSAdvancedAdapterConfiguration_Object = MibTableColumn
groupRBSAdvancedAdapterConfiguration = _GroupRBSAdvancedAdapterConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 5, 2, 1, 12),
    _GroupRBSAdvancedAdapterConfiguration_Type()
)
groupRBSAdvancedAdapterConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupRBSAdvancedAdapterConfiguration.setStatus("mandatory")
_SshClientAuth_ObjectIdentity = ObjectIdentity
sshClientAuth = _SshClientAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6)
)
_SshClientAuthPubKeyTable_Object = MibTable
sshClientAuthPubKeyTable = _SshClientAuthPubKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sshClientAuthPubKeyTable.setStatus("mandatory")
_SshClientAuthPubKeyEntry_Object = MibTableRow
sshClientAuthPubKeyEntry = _SshClientAuthPubKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1, 1)
)
sshClientAuthPubKeyEntry.setIndexNames(
    (0, "IMM-MIB", "sshClientAuthRemoteAccessIdIndex"),
    (0, "IMM-MIB", "sshClientAuthPubKeyIndex"),
)
if mibBuilder.loadTexts:
    sshClientAuthPubKeyEntry.setStatus("mandatory")


class _SshClientAuthRemoteAccessIdIndex_Type(Integer32):
    """Custom type sshClientAuthRemoteAccessIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SshClientAuthRemoteAccessIdIndex_Type.__name__ = "Integer32"
_SshClientAuthRemoteAccessIdIndex_Object = MibTableColumn
sshClientAuthRemoteAccessIdIndex = _SshClientAuthRemoteAccessIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1, 1, 1),
    _SshClientAuthRemoteAccessIdIndex_Type()
)
sshClientAuthRemoteAccessIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshClientAuthRemoteAccessIdIndex.setStatus("mandatory")


class _SshClientAuthPubKeyIndex_Type(Integer32):
    """Custom type sshClientAuthPubKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SshClientAuthPubKeyIndex_Type.__name__ = "Integer32"
_SshClientAuthPubKeyIndex_Object = MibTableColumn
sshClientAuthPubKeyIndex = _SshClientAuthPubKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1, 1, 2),
    _SshClientAuthPubKeyIndex_Type()
)
sshClientAuthPubKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyIndex.setStatus("mandatory")


class _SshClientAuthPubKeyType_Type(Integer32):
    """Custom type sshClientAuthPubKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sshDss", 1),
          ("sshRsa", 2))
    )


_SshClientAuthPubKeyType_Type.__name__ = "Integer32"
_SshClientAuthPubKeyType_Object = MibTableColumn
sshClientAuthPubKeyType = _SshClientAuthPubKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1, 1, 3),
    _SshClientAuthPubKeyType_Type()
)
sshClientAuthPubKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyType.setStatus("mandatory")


class _SshClientAuthPubKeySize_Type(Integer32):
    """Custom type sshClientAuthPubKeySize based on Integer32"""
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
        *(("bits1024", 3),
          ("bits2048", 4),
          ("bits4096", 5),
          ("bits512", 1),
          ("bits768", 2))
    )


_SshClientAuthPubKeySize_Type.__name__ = "Integer32"
_SshClientAuthPubKeySize_Object = MibTableColumn
sshClientAuthPubKeySize = _SshClientAuthPubKeySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1, 1, 4),
    _SshClientAuthPubKeySize_Type()
)
sshClientAuthPubKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshClientAuthPubKeySize.setStatus("mandatory")
_SshClientAuthPubKeyFingerprint_Type = OctetString
_SshClientAuthPubKeyFingerprint_Object = MibTableColumn
sshClientAuthPubKeyFingerprint = _SshClientAuthPubKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1, 1, 5),
    _SshClientAuthPubKeyFingerprint_Type()
)
sshClientAuthPubKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyFingerprint.setStatus("mandatory")
_SshClientAuthPubKeyAcceptFrom_Type = OctetString
_SshClientAuthPubKeyAcceptFrom_Object = MibTableColumn
sshClientAuthPubKeyAcceptFrom = _SshClientAuthPubKeyAcceptFrom_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1, 1, 6),
    _SshClientAuthPubKeyAcceptFrom_Type()
)
sshClientAuthPubKeyAcceptFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyAcceptFrom.setStatus("mandatory")
_SshClientAuthPubKeyComment_Type = OctetString
_SshClientAuthPubKeyComment_Object = MibTableColumn
sshClientAuthPubKeyComment = _SshClientAuthPubKeyComment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1, 1, 7),
    _SshClientAuthPubKeyComment_Type()
)
sshClientAuthPubKeyComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyComment.setStatus("mandatory")


class _SshClientAuthPubKeyAction_Type(Integer32):
    """Custom type sshClientAuthPubKeyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("export", 2),
          ("import", 1))
    )


_SshClientAuthPubKeyAction_Type.__name__ = "Integer32"
_SshClientAuthPubKeyAction_Object = MibTableColumn
sshClientAuthPubKeyAction = _SshClientAuthPubKeyAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1, 1, 8),
    _SshClientAuthPubKeyAction_Type()
)
sshClientAuthPubKeyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyAction.setStatus("mandatory")
_SshClientAuthPubKeyEntryStatus_Type = EntryStatus
_SshClientAuthPubKeyEntryStatus_Object = MibTableColumn
sshClientAuthPubKeyEntryStatus = _SshClientAuthPubKeyEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 1, 1, 9),
    _SshClientAuthPubKeyEntryStatus_Type()
)
sshClientAuthPubKeyEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyEntryStatus.setStatus("mandatory")
_SshClientAuthPubKeyUnused_Type = Integer32
_SshClientAuthPubKeyUnused_Object = MibScalar
sshClientAuthPubKeyUnused = _SshClientAuthPubKeyUnused_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 2),
    _SshClientAuthPubKeyUnused_Type()
)
sshClientAuthPubKeyUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyUnused.setStatus("mandatory")
_SshClientAuthPubKeyTftpServer_Type = OctetString
_SshClientAuthPubKeyTftpServer_Object = MibScalar
sshClientAuthPubKeyTftpServer = _SshClientAuthPubKeyTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 3),
    _SshClientAuthPubKeyTftpServer_Type()
)
sshClientAuthPubKeyTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyTftpServer.setStatus("mandatory")
_SshClientAuthPubKeyFileName_Type = OctetString
_SshClientAuthPubKeyFileName_Object = MibScalar
sshClientAuthPubKeyFileName = _SshClientAuthPubKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 4),
    _SshClientAuthPubKeyFileName_Type()
)
sshClientAuthPubKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyFileName.setStatus("mandatory")


class _SshClientAuthPubKeyFileFormat_Type(Integer32):
    """Custom type sshClientAuthPubKeyFileFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSSH", 1),
          ("rfc4716", 2))
    )


_SshClientAuthPubKeyFileFormat_Type.__name__ = "Integer32"
_SshClientAuthPubKeyFileFormat_Object = MibScalar
sshClientAuthPubKeyFileFormat = _SshClientAuthPubKeyFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 1, 6, 5),
    _SshClientAuthPubKeyFileFormat_Type()
)
sshClientAuthPubKeyFileFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshClientAuthPubKeyFileFormat.setStatus("mandatory")
_SpClock_ObjectIdentity = ObjectIdentity
spClock = _SpClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 2)
)
_SpClockDateAndTimeSetting_Type = OctetString
_SpClockDateAndTimeSetting_Object = MibScalar
spClockDateAndTimeSetting = _SpClockDateAndTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 2, 1),
    _SpClockDateAndTimeSetting_Type()
)
spClockDateAndTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spClockDateAndTimeSetting.setStatus("mandatory")
_SpClockTimezoneSetting_Type = OctetString
_SpClockTimezoneSetting_Object = MibScalar
spClockTimezoneSetting = _SpClockTimezoneSetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 2, 2),
    _SpClockTimezoneSetting_Type()
)
spClockTimezoneSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spClockTimezoneSetting.setStatus("mandatory")
_SpIdentification_ObjectIdentity = ObjectIdentity
spIdentification = _SpIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 3)
)


class _SpTxtId_Type(OctetString):
    """Custom type spTxtId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SpTxtId_Type.__name__ = "OctetString"
_SpTxtId_Object = MibScalar
spTxtId = _SpTxtId_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 3, 1),
    _SpTxtId_Type()
)
spTxtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spTxtId.setStatus("mandatory")
_SpRoomID_Type = DisplayString
_SpRoomID_Object = MibScalar
spRoomID = _SpRoomID_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 3, 2),
    _SpRoomID_Type()
)
spRoomID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spRoomID.setStatus("mandatory")
_SpRackID_Type = DisplayString
_SpRackID_Object = MibScalar
spRackID = _SpRackID_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 3, 3),
    _SpRackID_Type()
)
spRackID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spRackID.setStatus("mandatory")
_SpRackUnitPosition_Type = DisplayString
_SpRackUnitPosition_Object = MibScalar
spRackUnitPosition = _SpRackUnitPosition_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 3, 4),
    _SpRackUnitPosition_Type()
)
spRackUnitPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spRackUnitPosition.setStatus("mandatory")
_SpRackUnitHeight_Type = DisplayString
_SpRackUnitHeight_Object = MibScalar
spRackUnitHeight = _SpRackUnitHeight_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 3, 5),
    _SpRackUnitHeight_Type()
)
spRackUnitHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRackUnitHeight.setStatus("mandatory")
_SpRackBladeBay_Type = DisplayString
_SpRackBladeBay_Object = MibScalar
spRackBladeBay = _SpRackBladeBay_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 3, 6),
    _SpRackBladeBay_Type()
)
spRackBladeBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spRackBladeBay.setStatus("mandatory")
_NetworkConfiguration_ObjectIdentity = ObjectIdentity
networkConfiguration = _NetworkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4)
)
_NetworkInterfaces_ObjectIdentity = ObjectIdentity
networkInterfaces = _NetworkInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1)
)
_EthernetInterface_ObjectIdentity = ObjectIdentity
ethernetInterface = _EthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1)
)


class _EthernetInterfaceType_Type(OctetString):
    """Custom type ethernetInterfaceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EthernetInterfaceType_Type.__name__ = "OctetString"
_EthernetInterfaceType_Object = MibScalar
ethernetInterfaceType = _EthernetInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 1),
    _EthernetInterfaceType_Type()
)
ethernetInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceType.setStatus("mandatory")


class _EthernetInterfaceEnabled_Type(Integer32):
    """Custom type ethernetInterfaceEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interfaceDisabled", 0),
          ("interfaceEnabled", 1))
    )


_EthernetInterfaceEnabled_Type.__name__ = "Integer32"
_EthernetInterfaceEnabled_Object = MibScalar
ethernetInterfaceEnabled = _EthernetInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 2),
    _EthernetInterfaceEnabled_Type()
)
ethernetInterfaceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceEnabled.setStatus("mandatory")


class _EthernetInterfaceHostName_Type(OctetString):
    """Custom type ethernetInterfaceHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EthernetInterfaceHostName_Type.__name__ = "OctetString"
_EthernetInterfaceHostName_Object = MibScalar
ethernetInterfaceHostName = _EthernetInterfaceHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 3),
    _EthernetInterfaceHostName_Type()
)
ethernetInterfaceHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceHostName.setStatus("mandatory")
_EthernetInterfaceIPAddress_Type = IpAddress
_EthernetInterfaceIPAddress_Object = MibScalar
ethernetInterfaceIPAddress = _EthernetInterfaceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 4),
    _EthernetInterfaceIPAddress_Type()
)
ethernetInterfaceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceIPAddress.setStatus("mandatory")


class _EthernetInterfaceAutoNegotiate_Type(Integer32):
    """Custom type ethernetInterfaceAutoNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_EthernetInterfaceAutoNegotiate_Type.__name__ = "Integer32"
_EthernetInterfaceAutoNegotiate_Object = MibScalar
ethernetInterfaceAutoNegotiate = _EthernetInterfaceAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 5),
    _EthernetInterfaceAutoNegotiate_Type()
)
ethernetInterfaceAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceAutoNegotiate.setStatus("mandatory")


class _EthernetInterfaceDataRate_Type(Integer32):
    """Custom type ethernetInterfaceDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enet100Megabit", 4),
          ("enet10Megabit", 3))
    )


_EthernetInterfaceDataRate_Type.__name__ = "Integer32"
_EthernetInterfaceDataRate_Object = MibScalar
ethernetInterfaceDataRate = _EthernetInterfaceDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 6),
    _EthernetInterfaceDataRate_Type()
)
ethernetInterfaceDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceDataRate.setStatus("mandatory")


class _EthernetInterfaceDuplexSetting_Type(Integer32):
    """Custom type ethernetInterfaceDuplexSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_EthernetInterfaceDuplexSetting_Type.__name__ = "Integer32"
_EthernetInterfaceDuplexSetting_Object = MibScalar
ethernetInterfaceDuplexSetting = _EthernetInterfaceDuplexSetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 7),
    _EthernetInterfaceDuplexSetting_Type()
)
ethernetInterfaceDuplexSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceDuplexSetting.setStatus("mandatory")


class _EthernetInterfaceLAA_Type(OctetString):
    """Custom type ethernetInterfaceLAA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_EthernetInterfaceLAA_Type.__name__ = "OctetString"
_EthernetInterfaceLAA_Object = MibScalar
ethernetInterfaceLAA = _EthernetInterfaceLAA_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 8),
    _EthernetInterfaceLAA_Type()
)
ethernetInterfaceLAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceLAA.setStatus("mandatory")


class _EthernetInterfaceDhcpEnabled_Type(Integer32):
    """Custom type ethernetInterfaceDhcpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpDisabled", 0),
          ("dhcpEnabled", 1),
          ("dhcpTry", 2))
    )


_EthernetInterfaceDhcpEnabled_Type.__name__ = "Integer32"
_EthernetInterfaceDhcpEnabled_Object = MibScalar
ethernetInterfaceDhcpEnabled = _EthernetInterfaceDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 9),
    _EthernetInterfaceDhcpEnabled_Type()
)
ethernetInterfaceDhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceDhcpEnabled.setStatus("mandatory")
_EthernetInterfaceGatewayIPAddress_Type = IpAddress
_EthernetInterfaceGatewayIPAddress_Object = MibScalar
ethernetInterfaceGatewayIPAddress = _EthernetInterfaceGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 10),
    _EthernetInterfaceGatewayIPAddress_Type()
)
ethernetInterfaceGatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceGatewayIPAddress.setStatus("mandatory")


class _EthernetInterfaceBIA_Type(OctetString):
    """Custom type ethernetInterfaceBIA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EthernetInterfaceBIA_Type.__name__ = "OctetString"
_EthernetInterfaceBIA_Object = MibScalar
ethernetInterfaceBIA = _EthernetInterfaceBIA_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 11),
    _EthernetInterfaceBIA_Type()
)
ethernetInterfaceBIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceBIA.setStatus("mandatory")
_EthernetInterfaceMTU_Type = Integer32
_EthernetInterfaceMTU_Object = MibScalar
ethernetInterfaceMTU = _EthernetInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 12),
    _EthernetInterfaceMTU_Type()
)
ethernetInterfaceMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceMTU.setStatus("mandatory")
_EthernetInterfaceSubnetMask_Type = IpAddress
_EthernetInterfaceSubnetMask_Object = MibScalar
ethernetInterfaceSubnetMask = _EthernetInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 13),
    _EthernetInterfaceSubnetMask_Type()
)
ethernetInterfaceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceSubnetMask.setStatus("mandatory")
_DhcpEthernetInterface_ObjectIdentity = ObjectIdentity
dhcpEthernetInterface = _DhcpEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 14)
)


class _DhcpHostName_Type(OctetString):
    """Custom type dhcpHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpHostName_Type.__name__ = "OctetString"
_DhcpHostName_Object = MibScalar
dhcpHostName = _DhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 14, 1),
    _DhcpHostName_Type()
)
dhcpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpHostName.setStatus("mandatory")
_DhcpIPAddress_Type = IpAddress
_DhcpIPAddress_Object = MibScalar
dhcpIPAddress = _DhcpIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 14, 2),
    _DhcpIPAddress_Type()
)
dhcpIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpIPAddress.setStatus("mandatory")
_DhcpGatewayIPAddress_Type = IpAddress
_DhcpGatewayIPAddress_Object = MibScalar
dhcpGatewayIPAddress = _DhcpGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 14, 3),
    _DhcpGatewayIPAddress_Type()
)
dhcpGatewayIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpGatewayIPAddress.setStatus("mandatory")
_DhcpSubnetMask_Type = IpAddress
_DhcpSubnetMask_Object = MibScalar
dhcpSubnetMask = _DhcpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 14, 4),
    _DhcpSubnetMask_Type()
)
dhcpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetMask.setStatus("mandatory")


class _DhcpDomainName_Type(OctetString):
    """Custom type dhcpDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpDomainName_Type.__name__ = "OctetString"
_DhcpDomainName_Object = MibScalar
dhcpDomainName = _DhcpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 14, 5),
    _DhcpDomainName_Type()
)
dhcpDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpDomainName.setStatus("mandatory")
_DhcpPrimaryDNSServer_Type = IpAddress
_DhcpPrimaryDNSServer_Object = MibScalar
dhcpPrimaryDNSServer = _DhcpPrimaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 14, 6),
    _DhcpPrimaryDNSServer_Type()
)
dhcpPrimaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPrimaryDNSServer.setStatus("mandatory")
_DhcpSecondaryDNSServer_Type = IpAddress
_DhcpSecondaryDNSServer_Object = MibScalar
dhcpSecondaryDNSServer = _DhcpSecondaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 14, 7),
    _DhcpSecondaryDNSServer_Type()
)
dhcpSecondaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSecondaryDNSServer.setStatus("mandatory")
_DhcpTertiaryDNSServer_Type = IpAddress
_DhcpTertiaryDNSServer_Object = MibScalar
dhcpTertiaryDNSServer = _DhcpTertiaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 14, 8),
    _DhcpTertiaryDNSServer_Type()
)
dhcpTertiaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpTertiaryDNSServer.setStatus("mandatory")


class _EthernetInterfaceVlan_Type(Integer32):
    """Custom type ethernetInterfaceVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_EthernetInterfaceVlan_Type.__name__ = "Integer32"
_EthernetInterfaceVlan_Object = MibScalar
ethernetInterfaceVlan = _EthernetInterfaceVlan_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 15),
    _EthernetInterfaceVlan_Type()
)
ethernetInterfaceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceVlan.setStatus("mandatory")


class _EthernetInterfaceVlanID_Type(Integer32):
    """Custom type ethernetInterfaceVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EthernetInterfaceVlanID_Type.__name__ = "Integer32"
_EthernetInterfaceVlanID_Object = MibScalar
ethernetInterfaceVlanID = _EthernetInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 1, 16),
    _EthernetInterfaceVlanID_Type()
)
ethernetInterfaceVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceVlanID.setStatus("mandatory")
_EthernetInterfaceIPv6_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6 = _EthernetInterfaceIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4)
)


class _EthernetInterfaceIPv6Enabled_Type(Integer32):
    """Custom type ethernetInterfaceIPv6Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EthernetInterfaceIPv6Enabled_Type.__name__ = "Integer32"
_EthernetInterfaceIPv6Enabled_Object = MibScalar
ethernetInterfaceIPv6Enabled = _EthernetInterfaceIPv6Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 2),
    _EthernetInterfaceIPv6Enabled_Type()
)
ethernetInterfaceIPv6Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6Enabled.setStatus("mandatory")
_EthernetInterfaceIPv6Config_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6Config = _EthernetInterfaceIPv6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5)
)
_EthernetInterfaceIPv6LocalAddress_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6LocalAddress = _EthernetInterfaceIPv6LocalAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 1)
)
_EthernetInterfaceIPv6LinkLocalAddress_Type = InetAddressIPv6
_EthernetInterfaceIPv6LinkLocalAddress_Object = MibScalar
ethernetInterfaceIPv6LinkLocalAddress = _EthernetInterfaceIPv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 1, 1),
    _EthernetInterfaceIPv6LinkLocalAddress_Type()
)
ethernetInterfaceIPv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6LinkLocalAddress.setStatus("mandatory")
_EthernetInterfaceIPv6StaticIPConfig_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6StaticIPConfig = _EthernetInterfaceIPv6StaticIPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 2)
)


class _EthernetInterfaceIPv6StaticIPConfigEnabled_Type(Integer32):
    """Custom type ethernetInterfaceIPv6StaticIPConfigEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EthernetInterfaceIPv6StaticIPConfigEnabled_Type.__name__ = "Integer32"
_EthernetInterfaceIPv6StaticIPConfigEnabled_Object = MibScalar
ethernetInterfaceIPv6StaticIPConfigEnabled = _EthernetInterfaceIPv6StaticIPConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 2, 1),
    _EthernetInterfaceIPv6StaticIPConfigEnabled_Type()
)
ethernetInterfaceIPv6StaticIPConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6StaticIPConfigEnabled.setStatus("mandatory")
_EthernetInterfaceIPv6StaticIPAddress_Type = InetAddressIPv6
_EthernetInterfaceIPv6StaticIPAddress_Object = MibScalar
ethernetInterfaceIPv6StaticIPAddress = _EthernetInterfaceIPv6StaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 2, 2),
    _EthernetInterfaceIPv6StaticIPAddress_Type()
)
ethernetInterfaceIPv6StaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6StaticIPAddress.setStatus("mandatory")


class _EthernetInterfaceIPv6StaticIPAddressPrefixLen_Type(Integer32):
    """Custom type ethernetInterfaceIPv6StaticIPAddressPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_EthernetInterfaceIPv6StaticIPAddressPrefixLen_Type.__name__ = "Integer32"
_EthernetInterfaceIPv6StaticIPAddressPrefixLen_Object = MibScalar
ethernetInterfaceIPv6StaticIPAddressPrefixLen = _EthernetInterfaceIPv6StaticIPAddressPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 2, 3),
    _EthernetInterfaceIPv6StaticIPAddressPrefixLen_Type()
)
ethernetInterfaceIPv6StaticIPAddressPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6StaticIPAddressPrefixLen.setStatus("mandatory")
_EthernetInterfaceIPv6StaticIPDefaultRoute_Type = InetAddressIPv6
_EthernetInterfaceIPv6StaticIPDefaultRoute_Object = MibScalar
ethernetInterfaceIPv6StaticIPDefaultRoute = _EthernetInterfaceIPv6StaticIPDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 2, 4),
    _EthernetInterfaceIPv6StaticIPDefaultRoute_Type()
)
ethernetInterfaceIPv6StaticIPDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6StaticIPDefaultRoute.setStatus("mandatory")
_EthernetInterfaceIPv6AutoIPConfig_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6AutoIPConfig = _EthernetInterfaceIPv6AutoIPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3)
)
_EthernetInterfaceDHCPv6Config_ObjectIdentity = ObjectIdentity
ethernetInterfaceDHCPv6Config = _EthernetInterfaceDHCPv6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 2)
)


class _EthernetInterfaceDHCPv6Enabled_Type(Integer32):
    """Custom type ethernetInterfaceDHCPv6Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EthernetInterfaceDHCPv6Enabled_Type.__name__ = "Integer32"
_EthernetInterfaceDHCPv6Enabled_Object = MibScalar
ethernetInterfaceDHCPv6Enabled = _EthernetInterfaceDHCPv6Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 2, 1),
    _EthernetInterfaceDHCPv6Enabled_Type()
)
ethernetInterfaceDHCPv6Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6Enabled.setStatus("mandatory")
_EthernetInterfaceDHCPv6IPAddress_Type = InetAddressIPv6
_EthernetInterfaceDHCPv6IPAddress_Object = MibScalar
ethernetInterfaceDHCPv6IPAddress = _EthernetInterfaceDHCPv6IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 2, 2),
    _EthernetInterfaceDHCPv6IPAddress_Type()
)
ethernetInterfaceDHCPv6IPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6IPAddress.setStatus("mandatory")


class _EthernetInterfaceDHCPv6DomainName_Type(OctetString):
    """Custom type ethernetInterfaceDHCPv6DomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EthernetInterfaceDHCPv6DomainName_Type.__name__ = "OctetString"
_EthernetInterfaceDHCPv6DomainName_Object = MibScalar
ethernetInterfaceDHCPv6DomainName = _EthernetInterfaceDHCPv6DomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 2, 4),
    _EthernetInterfaceDHCPv6DomainName_Type()
)
ethernetInterfaceDHCPv6DomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6DomainName.setStatus("mandatory")
_EthernetInterfaceDHCPv6PrimaryDNSServer_Type = InetAddressIPv6
_EthernetInterfaceDHCPv6PrimaryDNSServer_Object = MibScalar
ethernetInterfaceDHCPv6PrimaryDNSServer = _EthernetInterfaceDHCPv6PrimaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 2, 5),
    _EthernetInterfaceDHCPv6PrimaryDNSServer_Type()
)
ethernetInterfaceDHCPv6PrimaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6PrimaryDNSServer.setStatus("mandatory")
_EthernetInterfaceDHCPv6SecondaryDNSServer_Type = InetAddressIPv6
_EthernetInterfaceDHCPv6SecondaryDNSServer_Object = MibScalar
ethernetInterfaceDHCPv6SecondaryDNSServer = _EthernetInterfaceDHCPv6SecondaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 2, 6),
    _EthernetInterfaceDHCPv6SecondaryDNSServer_Type()
)
ethernetInterfaceDHCPv6SecondaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6SecondaryDNSServer.setStatus("mandatory")
_EthernetInterfaceDHCPv6TertiaryDNSServer_Type = InetAddressIPv6
_EthernetInterfaceDHCPv6TertiaryDNSServer_Object = MibScalar
ethernetInterfaceDHCPv6TertiaryDNSServer = _EthernetInterfaceDHCPv6TertiaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 2, 7),
    _EthernetInterfaceDHCPv6TertiaryDNSServer_Type()
)
ethernetInterfaceDHCPv6TertiaryDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6TertiaryDNSServer.setStatus("mandatory")
_EthernetInterfaceDHCPv6Server_Type = InetAddressIPv6
_EthernetInterfaceDHCPv6Server_Object = MibScalar
ethernetInterfaceDHCPv6Server = _EthernetInterfaceDHCPv6Server_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 2, 8),
    _EthernetInterfaceDHCPv6Server_Type()
)
ethernetInterfaceDHCPv6Server.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceDHCPv6Server.setStatus("mandatory")
_EthernetInterfaceIPv6StatelessAutoConfig_ObjectIdentity = ObjectIdentity
ethernetInterfaceIPv6StatelessAutoConfig = _EthernetInterfaceIPv6StatelessAutoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 3)
)


class _EthernetInterfaceIPv6StatelessAutoConfigEnabled_Type(Integer32):
    """Custom type ethernetInterfaceIPv6StatelessAutoConfigEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EthernetInterfaceIPv6StatelessAutoConfigEnabled_Type.__name__ = "Integer32"
_EthernetInterfaceIPv6StatelessAutoConfigEnabled_Object = MibScalar
ethernetInterfaceIPv6StatelessAutoConfigEnabled = _EthernetInterfaceIPv6StatelessAutoConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 3, 1),
    _EthernetInterfaceIPv6StatelessAutoConfigEnabled_Type()
)
ethernetInterfaceIPv6StatelessAutoConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetInterfaceIPv6StatelessAutoConfigEnabled.setStatus("mandatory")
_EthernetInterfaceStatelessAutoConfigAddressesTable_Object = MibTable
ethernetInterfaceStatelessAutoConfigAddressesTable = _EthernetInterfaceStatelessAutoConfigAddressesTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ethernetInterfaceStatelessAutoConfigAddressesTable.setStatus("mandatory")
_EthernetInterfaceStatelessAutoConfigAddressesEntry_Object = MibTableRow
ethernetInterfaceStatelessAutoConfigAddressesEntry = _EthernetInterfaceStatelessAutoConfigAddressesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 3, 2, 1)
)
ethernetInterfaceStatelessAutoConfigAddressesEntry.setIndexNames(
    (0, "IMM-MIB", "ethernetInterfaceStatelessAutoConfigAddressesIndex"),
)
if mibBuilder.loadTexts:
    ethernetInterfaceStatelessAutoConfigAddressesEntry.setStatus("mandatory")


class _EthernetInterfaceStatelessAutoConfigAddressesIndex_Type(Integer32):
    """Custom type ethernetInterfaceStatelessAutoConfigAddressesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EthernetInterfaceStatelessAutoConfigAddressesIndex_Type.__name__ = "Integer32"
_EthernetInterfaceStatelessAutoConfigAddressesIndex_Object = MibTableColumn
ethernetInterfaceStatelessAutoConfigAddressesIndex = _EthernetInterfaceStatelessAutoConfigAddressesIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 3, 2, 1, 1),
    _EthernetInterfaceStatelessAutoConfigAddressesIndex_Type()
)
ethernetInterfaceStatelessAutoConfigAddressesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceStatelessAutoConfigAddressesIndex.setStatus("mandatory")
_EthernetInterfaceStatelessAutoConfigAddresses_Type = InetAddressIPv6
_EthernetInterfaceStatelessAutoConfigAddresses_Object = MibTableColumn
ethernetInterfaceStatelessAutoConfigAddresses = _EthernetInterfaceStatelessAutoConfigAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 3, 2, 1, 2),
    _EthernetInterfaceStatelessAutoConfigAddresses_Type()
)
ethernetInterfaceStatelessAutoConfigAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceStatelessAutoConfigAddresses.setStatus("mandatory")


class _EthernetInterfaceStatelessAutoConfigAddressesPrefixLen_Type(Integer32):
    """Custom type ethernetInterfaceStatelessAutoConfigAddressesPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_EthernetInterfaceStatelessAutoConfigAddressesPrefixLen_Type.__name__ = "Integer32"
_EthernetInterfaceStatelessAutoConfigAddressesPrefixLen_Object = MibTableColumn
ethernetInterfaceStatelessAutoConfigAddressesPrefixLen = _EthernetInterfaceStatelessAutoConfigAddressesPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 4, 5, 3, 3, 2, 1, 3),
    _EthernetInterfaceStatelessAutoConfigAddressesPrefixLen_Type()
)
ethernetInterfaceStatelessAutoConfigAddressesPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetInterfaceStatelessAutoConfigAddressesPrefixLen.setStatus("mandatory")


class _DdnsStatus_Type(Integer32):
    """Custom type ddnsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DdnsStatus_Type.__name__ = "Integer32"
_DdnsStatus_Object = MibScalar
ddnsStatus = _DdnsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 10),
    _DdnsStatus_Type()
)
ddnsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsStatus.setStatus("mandatory")


class _HostName_Type(OctetString):
    """Custom type hostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HostName_Type.__name__ = "OctetString"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 11),
    _HostName_Type()
)
hostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")


class _DdnsDomainToUse_Type(Integer32):
    """Custom type ddnsDomainToUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("manual", 2))
    )


_DdnsDomainToUse_Type.__name__ = "Integer32"
_DdnsDomainToUse_Object = MibScalar
ddnsDomainToUse = _DdnsDomainToUse_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 12),
    _DdnsDomainToUse_Type()
)
ddnsDomainToUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddnsDomainToUse.setStatus("mandatory")
_DomainName_Type = OctetString
_DomainName_Object = MibScalar
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 1, 13),
    _DomainName_Type()
)
domainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainName.setStatus("mandatory")
_TcpProtocols_ObjectIdentity = ObjectIdentity
tcpProtocols = _TcpProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2)
)
_SnmpAgentConfig_ObjectIdentity = ObjectIdentity
snmpAgentConfig = _SnmpAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1)
)


class _SnmpSystemName_Type(OctetString):
    """Custom type snmpSystemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnmpSystemName_Type.__name__ = "OctetString"
_SnmpSystemName_Object = MibScalar
snmpSystemName = _SnmpSystemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 1),
    _SnmpSystemName_Type()
)
snmpSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemName.setStatus("mandatory")


class _SnmpSystemContact_Type(OctetString):
    """Custom type snmpSystemContact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnmpSystemContact_Type.__name__ = "OctetString"
_SnmpSystemContact_Object = MibScalar
snmpSystemContact = _SnmpSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 2),
    _SnmpSystemContact_Type()
)
snmpSystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemContact.setStatus("mandatory")


class _SnmpSystemLocation_Type(OctetString):
    """Custom type snmpSystemLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnmpSystemLocation_Type.__name__ = "OctetString"
_SnmpSystemLocation_Object = MibScalar
snmpSystemLocation = _SnmpSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 3),
    _SnmpSystemLocation_Type()
)
snmpSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemLocation.setStatus("mandatory")


class _SnmpSystemAgentTrapsDisable_Type(Integer32):
    """Custom type snmpSystemAgentTrapsDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trapsDisabled", 1),
          ("trapsEnabled", 0))
    )


_SnmpSystemAgentTrapsDisable_Type.__name__ = "Integer32"
_SnmpSystemAgentTrapsDisable_Object = MibScalar
snmpSystemAgentTrapsDisable = _SnmpSystemAgentTrapsDisable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 4),
    _SnmpSystemAgentTrapsDisable_Type()
)
snmpSystemAgentTrapsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemAgentTrapsDisable.setStatus("mandatory")
_SnmpAgentCommunityConfig_ObjectIdentity = ObjectIdentity
snmpAgentCommunityConfig = _SnmpAgentCommunityConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 5)
)
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("mandatory")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 5, 1, 1)
)
snmpCommunityEntry.setIndexNames(
    (0, "IMM-MIB", "snmpCommunityEntryIndex"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("mandatory")


class _SnmpCommunityEntryIndex_Type(Integer32):
    """Custom type snmpCommunityEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpCommunityEntryIndex_Type.__name__ = "Integer32"
_SnmpCommunityEntryIndex_Object = MibTableColumn
snmpCommunityEntryIndex = _SnmpCommunityEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 5, 1, 1, 1),
    _SnmpCommunityEntryIndex_Type()
)
snmpCommunityEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityEntryIndex.setStatus("mandatory")


class _SnmpCommunityEntryCommunityName_Type(DisplayString):
    """Custom type snmpCommunityEntryCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SnmpCommunityEntryCommunityName_Type.__name__ = "DisplayString"
_SnmpCommunityEntryCommunityName_Object = MibTableColumn
snmpCommunityEntryCommunityName = _SnmpCommunityEntryCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 5, 1, 1, 2),
    _SnmpCommunityEntryCommunityName_Type()
)
snmpCommunityEntryCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityName.setStatus("mandatory")


class _SnmpCommunityEntryCommunityIpAddress1_Type(OctetString):
    """Custom type snmpCommunityEntryCommunityIpAddress1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SnmpCommunityEntryCommunityIpAddress1_Type.__name__ = "OctetString"
_SnmpCommunityEntryCommunityIpAddress1_Object = MibTableColumn
snmpCommunityEntryCommunityIpAddress1 = _SnmpCommunityEntryCommunityIpAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 5, 1, 1, 3),
    _SnmpCommunityEntryCommunityIpAddress1_Type()
)
snmpCommunityEntryCommunityIpAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityIpAddress1.setStatus("mandatory")


class _SnmpCommunityEntryCommunityIpAddress2_Type(OctetString):
    """Custom type snmpCommunityEntryCommunityIpAddress2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SnmpCommunityEntryCommunityIpAddress2_Type.__name__ = "OctetString"
_SnmpCommunityEntryCommunityIpAddress2_Object = MibTableColumn
snmpCommunityEntryCommunityIpAddress2 = _SnmpCommunityEntryCommunityIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 5, 1, 1, 4),
    _SnmpCommunityEntryCommunityIpAddress2_Type()
)
snmpCommunityEntryCommunityIpAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityIpAddress2.setStatus("mandatory")


class _SnmpCommunityEntryCommunityIpAddress3_Type(OctetString):
    """Custom type snmpCommunityEntryCommunityIpAddress3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SnmpCommunityEntryCommunityIpAddress3_Type.__name__ = "OctetString"
_SnmpCommunityEntryCommunityIpAddress3_Object = MibTableColumn
snmpCommunityEntryCommunityIpAddress3 = _SnmpCommunityEntryCommunityIpAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 5, 1, 1, 5),
    _SnmpCommunityEntryCommunityIpAddress3_Type()
)
snmpCommunityEntryCommunityIpAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityIpAddress3.setStatus("mandatory")


class _SnmpCommunityEntryCommunityViewType_Type(Integer32):
    """Custom type snmpCommunityEntryCommunityViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read-Traps", 1),
          ("traps-Only", 3),
          ("write-Read-Traps", 2))
    )


_SnmpCommunityEntryCommunityViewType_Type.__name__ = "Integer32"
_SnmpCommunityEntryCommunityViewType_Object = MibTableColumn
snmpCommunityEntryCommunityViewType = _SnmpCommunityEntryCommunityViewType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 5, 1, 1, 6),
    _SnmpCommunityEntryCommunityViewType_Type()
)
snmpCommunityEntryCommunityViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityEntryCommunityViewType.setStatus("mandatory")


class _Snmpv1SystemAgentEnable_Type(Integer32):
    """Custom type snmpv1SystemAgentEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Snmpv1SystemAgentEnable_Type.__name__ = "Integer32"
_Snmpv1SystemAgentEnable_Object = MibScalar
snmpv1SystemAgentEnable = _Snmpv1SystemAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 6),
    _Snmpv1SystemAgentEnable_Type()
)
snmpv1SystemAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv1SystemAgentEnable.setStatus("mandatory")


class _Snmpv3SystemAgentEnable_Type(Integer32):
    """Custom type snmpv3SystemAgentEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Snmpv3SystemAgentEnable_Type.__name__ = "Integer32"
_Snmpv3SystemAgentEnable_Object = MibScalar
snmpv3SystemAgentEnable = _Snmpv3SystemAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 7),
    _Snmpv3SystemAgentEnable_Type()
)
snmpv3SystemAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3SystemAgentEnable.setStatus("mandatory")
_SnmpAgentUserProfileConfig_ObjectIdentity = ObjectIdentity
snmpAgentUserProfileConfig = _SnmpAgentUserProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 8)
)
_SnmpUserProfileTable_Object = MibTable
snmpUserProfileTable = _SnmpUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    snmpUserProfileTable.setStatus("mandatory")
_SnmpUserProfileEntry_Object = MibTableRow
snmpUserProfileEntry = _SnmpUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 8, 1, 1)
)
snmpUserProfileEntry.setIndexNames(
    (0, "IMM-MIB", "snmpUserProfileEntryIndex"),
)
if mibBuilder.loadTexts:
    snmpUserProfileEntry.setStatus("mandatory")


class _SnmpUserProfileEntryIndex_Type(Integer32):
    """Custom type snmpUserProfileEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpUserProfileEntryIndex_Type.__name__ = "Integer32"
_SnmpUserProfileEntryIndex_Object = MibTableColumn
snmpUserProfileEntryIndex = _SnmpUserProfileEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 8, 1, 1, 1),
    _SnmpUserProfileEntryIndex_Type()
)
snmpUserProfileEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserProfileEntryIndex.setStatus("mandatory")


class _SnmpUserProfileEntryAuthProt_Type(Integer32):
    """Custom type snmpUserProfileEntryAuthProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1),
          ("sha", 3))
    )


_SnmpUserProfileEntryAuthProt_Type.__name__ = "Integer32"
_SnmpUserProfileEntryAuthProt_Object = MibTableColumn
snmpUserProfileEntryAuthProt = _SnmpUserProfileEntryAuthProt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 8, 1, 1, 2),
    _SnmpUserProfileEntryAuthProt_Type()
)
snmpUserProfileEntryAuthProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryAuthProt.setStatus("mandatory")


class _SnmpUserProfileEntryPrivProt_Type(Integer32):
    """Custom type snmpUserProfileEntryPrivProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aes", 4),
          ("des", 2),
          ("none", 1))
    )


_SnmpUserProfileEntryPrivProt_Type.__name__ = "Integer32"
_SnmpUserProfileEntryPrivProt_Object = MibTableColumn
snmpUserProfileEntryPrivProt = _SnmpUserProfileEntryPrivProt_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 8, 1, 1, 3),
    _SnmpUserProfileEntryPrivProt_Type()
)
snmpUserProfileEntryPrivProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryPrivProt.setStatus("mandatory")


class _SnmpUserProfileEntryPrivPassword_Type(OctetString):
    """Custom type snmpUserProfileEntryPrivPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SnmpUserProfileEntryPrivPassword_Type.__name__ = "OctetString"
_SnmpUserProfileEntryPrivPassword_Object = MibTableColumn
snmpUserProfileEntryPrivPassword = _SnmpUserProfileEntryPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 8, 1, 1, 4),
    _SnmpUserProfileEntryPrivPassword_Type()
)
snmpUserProfileEntryPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryPrivPassword.setStatus("mandatory")


class _SnmpUserProfileEntryViewType_Type(Integer32):
    """Custom type snmpUserProfileEntryViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-Traps", 1),
          ("read-Write-Traps", 2))
    )


_SnmpUserProfileEntryViewType_Type.__name__ = "Integer32"
_SnmpUserProfileEntryViewType_Object = MibTableColumn
snmpUserProfileEntryViewType = _SnmpUserProfileEntryViewType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 8, 1, 1, 5),
    _SnmpUserProfileEntryViewType_Type()
)
snmpUserProfileEntryViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryViewType.setStatus("mandatory")


class _SnmpUserProfileEntryIpAddress_Type(OctetString):
    """Custom type snmpUserProfileEntryIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SnmpUserProfileEntryIpAddress_Type.__name__ = "OctetString"
_SnmpUserProfileEntryIpAddress_Object = MibTableColumn
snmpUserProfileEntryIpAddress = _SnmpUserProfileEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 1, 8, 1, 1, 6),
    _SnmpUserProfileEntryIpAddress_Type()
)
snmpUserProfileEntryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserProfileEntryIpAddress.setStatus("mandatory")
_DnsConfig_ObjectIdentity = ObjectIdentity
dnsConfig = _DnsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 2)
)


class _DnsEnabled_Type(Integer32):
    """Custom type dnsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dnsDisabled", 0),
          ("dnsEnabled", 1))
    )


_DnsEnabled_Type.__name__ = "Integer32"
_DnsEnabled_Object = MibScalar
dnsEnabled = _DnsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 2, 1),
    _DnsEnabled_Type()
)
dnsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsEnabled.setStatus("mandatory")
_DnsServerIPAddress1_Type = IpAddress
_DnsServerIPAddress1_Object = MibScalar
dnsServerIPAddress1 = _DnsServerIPAddress1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 2, 2),
    _DnsServerIPAddress1_Type()
)
dnsServerIPAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerIPAddress1.setStatus("mandatory")
_DnsServerIPAddress2_Type = IpAddress
_DnsServerIPAddress2_Object = MibScalar
dnsServerIPAddress2 = _DnsServerIPAddress2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 2, 3),
    _DnsServerIPAddress2_Type()
)
dnsServerIPAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerIPAddress2.setStatus("mandatory")
_DnsServerIPAddress3_Type = IpAddress
_DnsServerIPAddress3_Object = MibScalar
dnsServerIPAddress3 = _DnsServerIPAddress3_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 2, 4),
    _DnsServerIPAddress3_Type()
)
dnsServerIPAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerIPAddress3.setStatus("mandatory")
_DnsServerIPv6Address1_Type = InetAddressIPv6
_DnsServerIPv6Address1_Object = MibScalar
dnsServerIPv6Address1 = _DnsServerIPv6Address1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 2, 12),
    _DnsServerIPv6Address1_Type()
)
dnsServerIPv6Address1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerIPv6Address1.setStatus("mandatory")
_DnsServerIPv6Address2_Type = InetAddressIPv6
_DnsServerIPv6Address2_Object = MibScalar
dnsServerIPv6Address2 = _DnsServerIPv6Address2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 2, 13),
    _DnsServerIPv6Address2_Type()
)
dnsServerIPv6Address2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerIPv6Address2.setStatus("mandatory")
_DnsServerIPv6Address3_Type = InetAddressIPv6
_DnsServerIPv6Address3_Object = MibScalar
dnsServerIPv6Address3 = _DnsServerIPv6Address3_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 2, 14),
    _DnsServerIPv6Address3_Type()
)
dnsServerIPv6Address3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerIPv6Address3.setStatus("mandatory")


class _DnsPriority_Type(Integer32):
    """Custom type dnsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 2),
          ("ipv6", 1))
    )


_DnsPriority_Type.__name__ = "Integer32"
_DnsPriority_Object = MibScalar
dnsPriority = _DnsPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 2, 20),
    _DnsPriority_Type()
)
dnsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsPriority.setStatus("mandatory")
_SmtpConfig_ObjectIdentity = ObjectIdentity
smtpConfig = _SmtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 3)
)


class _SmtpServerNameOrIPAddress_Type(OctetString):
    """Custom type smtpServerNameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SmtpServerNameOrIPAddress_Type.__name__ = "OctetString"
_SmtpServerNameOrIPAddress_Object = MibScalar
smtpServerNameOrIPAddress = _SmtpServerNameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 3, 1),
    _SmtpServerNameOrIPAddress_Type()
)
smtpServerNameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerNameOrIPAddress.setStatus("mandatory")
_SmtpServerPort_Type = Integer32
_SmtpServerPort_Object = MibScalar
smtpServerPort = _SmtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 3, 2),
    _SmtpServerPort_Type()
)
smtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerPort.setStatus("mandatory")


class _SmtpServerAuthentication_Type(Integer32):
    """Custom type smtpServerAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_SmtpServerAuthentication_Type.__name__ = "Integer32"
_SmtpServerAuthentication_Object = MibScalar
smtpServerAuthentication = _SmtpServerAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 3, 3),
    _SmtpServerAuthentication_Type()
)
smtpServerAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerAuthentication.setStatus("mandatory")


class _SmtpServerAuthenticationUser_Type(OctetString):
    """Custom type smtpServerAuthenticationUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmtpServerAuthenticationUser_Type.__name__ = "OctetString"
_SmtpServerAuthenticationUser_Object = MibScalar
smtpServerAuthenticationUser = _SmtpServerAuthenticationUser_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 3, 4),
    _SmtpServerAuthenticationUser_Type()
)
smtpServerAuthenticationUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerAuthenticationUser.setStatus("mandatory")


class _SmtpServerAuthenticationPassword_Type(OctetString):
    """Custom type smtpServerAuthenticationPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmtpServerAuthenticationPassword_Type.__name__ = "OctetString"
_SmtpServerAuthenticationPassword_Object = MibScalar
smtpServerAuthenticationPassword = _SmtpServerAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 3, 5),
    _SmtpServerAuthenticationPassword_Type()
)
smtpServerAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerAuthenticationPassword.setStatus("mandatory")


class _SmtpServerAuthenticationMethod_Type(Integer32):
    """Custom type smtpServerAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cram-md5", 1),
          ("plain", 0))
    )


_SmtpServerAuthenticationMethod_Type.__name__ = "Integer32"
_SmtpServerAuthenticationMethod_Object = MibScalar
smtpServerAuthenticationMethod = _SmtpServerAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 3, 6),
    _SmtpServerAuthenticationMethod_Type()
)
smtpServerAuthenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerAuthenticationMethod.setStatus("mandatory")
_TcpApplicationConfig_ObjectIdentity = ObjectIdentity
tcpApplicationConfig = _TcpApplicationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4)
)


class _TelnetConnectionCounts_Type(Integer32):
    """Custom type telnetConnectionCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("one", 1),
          ("two", 2))
    )


_TelnetConnectionCounts_Type.__name__ = "Integer32"
_TelnetConnectionCounts_Object = MibScalar
telnetConnectionCounts = _TelnetConnectionCounts_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 1),
    _TelnetConnectionCounts_Type()
)
telnetConnectionCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetConnectionCounts.setStatus("mandatory")


class _SlpAddrType_Type(Integer32):
    """Custom type slpAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 0))
    )


_SlpAddrType_Type.__name__ = "Integer32"
_SlpAddrType_Object = MibScalar
slpAddrType = _SlpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 2),
    _SlpAddrType_Type()
)
slpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slpAddrType.setStatus("mandatory")
_SlpMulticastAddr_Type = IpAddress
_SlpMulticastAddr_Object = MibScalar
slpMulticastAddr = _SlpMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 3),
    _SlpMulticastAddr_Type()
)
slpMulticastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slpMulticastAddr.setStatus("mandatory")
_SshServerConfig_ObjectIdentity = ObjectIdentity
sshServerConfig = _SshServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 5)
)


class _SshServerHostKeySize_Type(Integer32):
    """Custom type sshServerHostKeySize based on Integer32"""
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
        *(("bits1024", 3),
          ("bits2048", 4),
          ("bits4096", 5),
          ("bits512", 1),
          ("bits768", 2))
    )


_SshServerHostKeySize_Type.__name__ = "Integer32"
_SshServerHostKeySize_Object = MibScalar
sshServerHostKeySize = _SshServerHostKeySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 5, 1),
    _SshServerHostKeySize_Type()
)
sshServerHostKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerHostKeySize.setStatus("mandatory")
_SshServerHostKeyFingerprint_Type = OctetString
_SshServerHostKeyFingerprint_Object = MibScalar
sshServerHostKeyFingerprint = _SshServerHostKeyFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 5, 2),
    _SshServerHostKeyFingerprint_Type()
)
sshServerHostKeyFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerHostKeyFingerprint.setStatus("mandatory")


class _SshServerHostKeyGenerate_Type(Integer32):
    """Custom type sshServerHostKeyGenerate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_SshServerHostKeyGenerate_Type.__name__ = "Integer32"
_SshServerHostKeyGenerate_Object = MibScalar
sshServerHostKeyGenerate = _SshServerHostKeyGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 5, 3),
    _SshServerHostKeyGenerate_Type()
)
sshServerHostKeyGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerHostKeyGenerate.setStatus("mandatory")
_SshServerHostKeyGenerateProgress_Type = OctetString
_SshServerHostKeyGenerateProgress_Object = MibScalar
sshServerHostKeyGenerateProgress = _SshServerHostKeyGenerateProgress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 5, 4),
    _SshServerHostKeyGenerateProgress_Type()
)
sshServerHostKeyGenerateProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerHostKeyGenerateProgress.setStatus("mandatory")


class _SshEnable_Type(Integer32):
    """Custom type sshEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SshEnable_Type.__name__ = "Integer32"
_SshEnable_Object = MibScalar
sshEnable = _SshEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 5, 5),
    _SshEnable_Type()
)
sshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshEnable.setStatus("mandatory")
_SslConfig_ObjectIdentity = ObjectIdentity
sslConfig = _SslConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6)
)
_SslHTTPSServerConfigForWeb_ObjectIdentity = ObjectIdentity
sslHTTPSServerConfigForWeb = _SslHTTPSServerConfigForWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 1)
)


class _SslEnableHTTPSforWeb_Type(Integer32):
    """Custom type sslEnableHTTPSforWeb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SslEnableHTTPSforWeb_Type.__name__ = "Integer32"
_SslEnableHTTPSforWeb_Object = MibScalar
sslEnableHTTPSforWeb = _SslEnableHTTPSforWeb_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 1, 1),
    _SslEnableHTTPSforWeb_Type()
)
sslEnableHTTPSforWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslEnableHTTPSforWeb.setStatus("mandatory")


class _SslHTTPSServerWebCertificateGeneration_Type(Integer32):
    """Custom type sslHTTPSServerWebCertificateGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generateNewKeyandCSR", 2),
          ("generateNewKeyandSelfSigned", 1))
    )


_SslHTTPSServerWebCertificateGeneration_Type.__name__ = "Integer32"
_SslHTTPSServerWebCertificateGeneration_Object = MibScalar
sslHTTPSServerWebCertificateGeneration = _SslHTTPSServerWebCertificateGeneration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 1, 2),
    _SslHTTPSServerWebCertificateGeneration_Type()
)
sslHTTPSServerWebCertificateGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslHTTPSServerWebCertificateGeneration.setStatus("mandatory")


class _SslHTTPSServerWebCertificateTransfer_Type(Integer32):
    """Custom type sslHTTPSServerWebCertificateTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadCSR", 3),
          ("downloadCertificate", 2),
          ("importSignedCertificate", 1))
    )


_SslHTTPSServerWebCertificateTransfer_Type.__name__ = "Integer32"
_SslHTTPSServerWebCertificateTransfer_Object = MibScalar
sslHTTPSServerWebCertificateTransfer = _SslHTTPSServerWebCertificateTransfer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 1, 3),
    _SslHTTPSServerWebCertificateTransfer_Type()
)
sslHTTPSServerWebCertificateTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslHTTPSServerWebCertificateTransfer.setStatus("mandatory")


class _SslHTTPSWebCertificateStatus_Type(Integer32):
    """Custom type sslHTTPSWebCertificateStatus based on Integer32"""
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
        *(("ca-signed-and-csr-generated", 6),
          ("ca-signed-installed", 3),
          ("csr-generated", 4),
          ("no-cert-installed", 1),
          ("self-signed-and-csr-generated", 5),
          ("self-signed-installed", 2))
    )


_SslHTTPSWebCertificateStatus_Type.__name__ = "Integer32"
_SslHTTPSWebCertificateStatus_Object = MibScalar
sslHTTPSWebCertificateStatus = _SslHTTPSWebCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 1, 4),
    _SslHTTPSWebCertificateStatus_Type()
)
sslHTTPSWebCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslHTTPSWebCertificateStatus.setStatus("mandatory")
_SslHTTPSServerConfigForCIMXML_ObjectIdentity = ObjectIdentity
sslHTTPSServerConfigForCIMXML = _SslHTTPSServerConfigForCIMXML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 2)
)


class _SslEnableHTTPSforCIMXML_Type(Integer32):
    """Custom type sslEnableHTTPSforCIMXML based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SslEnableHTTPSforCIMXML_Type.__name__ = "Integer32"
_SslEnableHTTPSforCIMXML_Object = MibScalar
sslEnableHTTPSforCIMXML = _SslEnableHTTPSforCIMXML_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 2, 1),
    _SslEnableHTTPSforCIMXML_Type()
)
sslEnableHTTPSforCIMXML.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslEnableHTTPSforCIMXML.setStatus("mandatory")


class _SslHTTPSServerCIMXMLCertificateGeneration_Type(Integer32):
    """Custom type sslHTTPSServerCIMXMLCertificateGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generateNewKeyandCSR", 2),
          ("generateNewKeyandSelfSigned", 1))
    )


_SslHTTPSServerCIMXMLCertificateGeneration_Type.__name__ = "Integer32"
_SslHTTPSServerCIMXMLCertificateGeneration_Object = MibScalar
sslHTTPSServerCIMXMLCertificateGeneration = _SslHTTPSServerCIMXMLCertificateGeneration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 2, 2),
    _SslHTTPSServerCIMXMLCertificateGeneration_Type()
)
sslHTTPSServerCIMXMLCertificateGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslHTTPSServerCIMXMLCertificateGeneration.setStatus("mandatory")


class _SslHTTPSServerCIMXMLCertificateTransfer_Type(Integer32):
    """Custom type sslHTTPSServerCIMXMLCertificateTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadCSR", 3),
          ("downloadCertificate", 2),
          ("importSignedCertificate", 1))
    )


_SslHTTPSServerCIMXMLCertificateTransfer_Type.__name__ = "Integer32"
_SslHTTPSServerCIMXMLCertificateTransfer_Object = MibScalar
sslHTTPSServerCIMXMLCertificateTransfer = _SslHTTPSServerCIMXMLCertificateTransfer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 2, 3),
    _SslHTTPSServerCIMXMLCertificateTransfer_Type()
)
sslHTTPSServerCIMXMLCertificateTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslHTTPSServerCIMXMLCertificateTransfer.setStatus("mandatory")


class _SslHTTPSCIMXMLCertificateStatus_Type(Integer32):
    """Custom type sslHTTPSCIMXMLCertificateStatus based on Integer32"""
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
        *(("ca-signed-and-csr-generated", 6),
          ("ca-signed-installed", 3),
          ("csr-generated", 4),
          ("no-cert-installed", 1),
          ("self-signed-and-csr-generated", 5),
          ("self-signed-installed", 2))
    )


_SslHTTPSCIMXMLCertificateStatus_Type.__name__ = "Integer32"
_SslHTTPSCIMXMLCertificateStatus_Object = MibScalar
sslHTTPSCIMXMLCertificateStatus = _SslHTTPSCIMXMLCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 2, 4),
    _SslHTTPSCIMXMLCertificateStatus_Type()
)
sslHTTPSCIMXMLCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslHTTPSCIMXMLCertificateStatus.setStatus("mandatory")
_SslClientConfigForLDAP_ObjectIdentity = ObjectIdentity
sslClientConfigForLDAP = _SslClientConfigForLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 3)
)


class _SslEnableClientLDAP_Type(Integer32):
    """Custom type sslEnableClientLDAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SslEnableClientLDAP_Type.__name__ = "Integer32"
_SslEnableClientLDAP_Object = MibScalar
sslEnableClientLDAP = _SslEnableClientLDAP_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 3, 1),
    _SslEnableClientLDAP_Type()
)
sslEnableClientLDAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslEnableClientLDAP.setStatus("mandatory")


class _SslClientLDAPCertificateGeneration_Type(Integer32):
    """Custom type sslClientLDAPCertificateGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generateNewKeyandCSR", 2),
          ("generateNewKeyandSelfSigned", 1))
    )


_SslClientLDAPCertificateGeneration_Type.__name__ = "Integer32"
_SslClientLDAPCertificateGeneration_Object = MibScalar
sslClientLDAPCertificateGeneration = _SslClientLDAPCertificateGeneration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 3, 2),
    _SslClientLDAPCertificateGeneration_Type()
)
sslClientLDAPCertificateGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslClientLDAPCertificateGeneration.setStatus("mandatory")


class _SslClientLDAPCertificateDownload_Type(Integer32):
    """Custom type sslClientLDAPCertificateDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadCSR", 3),
          ("downloadCertificate", 2))
    )


_SslClientLDAPCertificateDownload_Type.__name__ = "Integer32"
_SslClientLDAPCertificateDownload_Object = MibScalar
sslClientLDAPCertificateDownload = _SslClientLDAPCertificateDownload_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 3, 3),
    _SslClientLDAPCertificateDownload_Type()
)
sslClientLDAPCertificateDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslClientLDAPCertificateDownload.setStatus("mandatory")


class _SslClientLDAPCertificateImport_Type(Integer32):
    """Custom type sslClientLDAPCertificateImport based on Integer32"""
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
        *(("importSignedCertificate1", 1),
          ("importTrustedCertificate1", 2),
          ("importTrustedCertificate2", 3),
          ("importTrustedCertificate3", 4),
          ("importTrustedCertificate4", 5))
    )


_SslClientLDAPCertificateImport_Type.__name__ = "Integer32"
_SslClientLDAPCertificateImport_Object = MibScalar
sslClientLDAPCertificateImport = _SslClientLDAPCertificateImport_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 3, 4),
    _SslClientLDAPCertificateImport_Type()
)
sslClientLDAPCertificateImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslClientLDAPCertificateImport.setStatus("mandatory")


class _SslClientLDAPCertificateStatus_Type(Integer32):
    """Custom type sslClientLDAPCertificateStatus based on Integer32"""
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
        *(("ca-signed-and-csr-generated", 6),
          ("ca-signed-installed", 3),
          ("csr-generated", 4),
          ("no-cert-installed", 1),
          ("self-signed-and-csr-generated", 5),
          ("self-signed-installed", 2))
    )


_SslClientLDAPCertificateStatus_Type.__name__ = "Integer32"
_SslClientLDAPCertificateStatus_Object = MibScalar
sslClientLDAPCertificateStatus = _SslClientLDAPCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 3, 5),
    _SslClientLDAPCertificateStatus_Type()
)
sslClientLDAPCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientLDAPCertificateStatus.setStatus("mandatory")


class _SslClientLDAPTrustedCertificate1Status_Type(Integer32):
    """Custom type sslClientLDAPTrustedCertificate1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("not-installed", 0))
    )


_SslClientLDAPTrustedCertificate1Status_Type.__name__ = "Integer32"
_SslClientLDAPTrustedCertificate1Status_Object = MibScalar
sslClientLDAPTrustedCertificate1Status = _SslClientLDAPTrustedCertificate1Status_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 3, 6),
    _SslClientLDAPTrustedCertificate1Status_Type()
)
sslClientLDAPTrustedCertificate1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientLDAPTrustedCertificate1Status.setStatus("mandatory")


class _SslClientLDAPTrustedCertificate2Status_Type(Integer32):
    """Custom type sslClientLDAPTrustedCertificate2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("not-installed", 0))
    )


_SslClientLDAPTrustedCertificate2Status_Type.__name__ = "Integer32"
_SslClientLDAPTrustedCertificate2Status_Object = MibScalar
sslClientLDAPTrustedCertificate2Status = _SslClientLDAPTrustedCertificate2Status_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 3, 7),
    _SslClientLDAPTrustedCertificate2Status_Type()
)
sslClientLDAPTrustedCertificate2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientLDAPTrustedCertificate2Status.setStatus("mandatory")


class _SslClientLDAPTrustedCertificate3Status_Type(Integer32):
    """Custom type sslClientLDAPTrustedCertificate3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("not-installed", 0))
    )


_SslClientLDAPTrustedCertificate3Status_Type.__name__ = "Integer32"
_SslClientLDAPTrustedCertificate3Status_Object = MibScalar
sslClientLDAPTrustedCertificate3Status = _SslClientLDAPTrustedCertificate3Status_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 3, 8),
    _SslClientLDAPTrustedCertificate3Status_Type()
)
sslClientLDAPTrustedCertificate3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientLDAPTrustedCertificate3Status.setStatus("mandatory")


class _SslClientLDAPTrustedCertificate4Status_Type(Integer32):
    """Custom type sslClientLDAPTrustedCertificate4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("not-installed", 0))
    )


_SslClientLDAPTrustedCertificate4Status_Type.__name__ = "Integer32"
_SslClientLDAPTrustedCertificate4Status_Object = MibScalar
sslClientLDAPTrustedCertificate4Status = _SslClientLDAPTrustedCertificate4Status_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 3, 9),
    _SslClientLDAPTrustedCertificate4Status_Type()
)
sslClientLDAPTrustedCertificate4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslClientLDAPTrustedCertificate4Status.setStatus("mandatory")


class _SslConfigTftpServer_Type(OctetString):
    """Custom type sslConfigTftpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SslConfigTftpServer_Type.__name__ = "OctetString"
_SslConfigTftpServer_Object = MibScalar
sslConfigTftpServer = _SslConfigTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 4),
    _SslConfigTftpServer_Type()
)
sslConfigTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslConfigTftpServer.setStatus("mandatory")


class _SslConfigFileName_Type(OctetString):
    """Custom type sslConfigFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_SslConfigFileName_Type.__name__ = "OctetString"
_SslConfigFileName_Object = MibScalar
sslConfigFileName = _SslConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 5),
    _SslConfigFileName_Type()
)
sslConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslConfigFileName.setStatus("mandatory")
_SslCertificateData_ObjectIdentity = ObjectIdentity
sslCertificateData = _SslCertificateData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6)
)
_SslCertificateDataCountry_Type = OctetString
_SslCertificateDataCountry_Object = MibScalar
sslCertificateDataCountry = _SslCertificateDataCountry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 1),
    _SslCertificateDataCountry_Type()
)
sslCertificateDataCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataCountry.setStatus("mandatory")
_SslCertificateDataStateorProvince_Type = OctetString
_SslCertificateDataStateorProvince_Object = MibScalar
sslCertificateDataStateorProvince = _SslCertificateDataStateorProvince_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 2),
    _SslCertificateDataStateorProvince_Type()
)
sslCertificateDataStateorProvince.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataStateorProvince.setStatus("mandatory")
_SslCertificateDataCityOrLocality_Type = OctetString
_SslCertificateDataCityOrLocality_Object = MibScalar
sslCertificateDataCityOrLocality = _SslCertificateDataCityOrLocality_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 3),
    _SslCertificateDataCityOrLocality_Type()
)
sslCertificateDataCityOrLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataCityOrLocality.setStatus("mandatory")
_SslCertificateDataOrganizationName_Type = OctetString
_SslCertificateDataOrganizationName_Object = MibScalar
sslCertificateDataOrganizationName = _SslCertificateDataOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 4),
    _SslCertificateDataOrganizationName_Type()
)
sslCertificateDataOrganizationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataOrganizationName.setStatus("mandatory")
_SslCertificateDataIMMHostName_Type = OctetString
_SslCertificateDataIMMHostName_Object = MibScalar
sslCertificateDataIMMHostName = _SslCertificateDataIMMHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 5),
    _SslCertificateDataIMMHostName_Type()
)
sslCertificateDataIMMHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataIMMHostName.setStatus("mandatory")
_SslCertificateDataContact_Type = OctetString
_SslCertificateDataContact_Object = MibScalar
sslCertificateDataContact = _SslCertificateDataContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 6),
    _SslCertificateDataContact_Type()
)
sslCertificateDataContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataContact.setStatus("mandatory")
_SslCertificateDataEmailAddr_Type = OctetString
_SslCertificateDataEmailAddr_Object = MibScalar
sslCertificateDataEmailAddr = _SslCertificateDataEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 7),
    _SslCertificateDataEmailAddr_Type()
)
sslCertificateDataEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataEmailAddr.setStatus("mandatory")
_SslCertificateDataOrganizationUnit_Type = OctetString
_SslCertificateDataOrganizationUnit_Object = MibScalar
sslCertificateDataOrganizationUnit = _SslCertificateDataOrganizationUnit_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 8),
    _SslCertificateDataOrganizationUnit_Type()
)
sslCertificateDataOrganizationUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataOrganizationUnit.setStatus("mandatory")
_SslCertificateDataSurname_Type = OctetString
_SslCertificateDataSurname_Object = MibScalar
sslCertificateDataSurname = _SslCertificateDataSurname_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 9),
    _SslCertificateDataSurname_Type()
)
sslCertificateDataSurname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataSurname.setStatus("mandatory")
_SslCertificateDataGivenName_Type = OctetString
_SslCertificateDataGivenName_Object = MibScalar
sslCertificateDataGivenName = _SslCertificateDataGivenName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 10),
    _SslCertificateDataGivenName_Type()
)
sslCertificateDataGivenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataGivenName.setStatus("mandatory")
_SslCertificateDataInitials_Type = OctetString
_SslCertificateDataInitials_Object = MibScalar
sslCertificateDataInitials = _SslCertificateDataInitials_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 11),
    _SslCertificateDataInitials_Type()
)
sslCertificateDataInitials.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataInitials.setStatus("mandatory")
_SslCertificateDataDNQualifier_Type = OctetString
_SslCertificateDataDNQualifier_Object = MibScalar
sslCertificateDataDNQualifier = _SslCertificateDataDNQualifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 12),
    _SslCertificateDataDNQualifier_Type()
)
sslCertificateDataDNQualifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataDNQualifier.setStatus("mandatory")
_SslCertificateDataCSRChallengePassword_Type = OctetString
_SslCertificateDataCSRChallengePassword_Object = MibScalar
sslCertificateDataCSRChallengePassword = _SslCertificateDataCSRChallengePassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 13),
    _SslCertificateDataCSRChallengePassword_Type()
)
sslCertificateDataCSRChallengePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataCSRChallengePassword.setStatus("mandatory")
_SslCertificateDataCSRUnstructuredName_Type = OctetString
_SslCertificateDataCSRUnstructuredName_Object = MibScalar
sslCertificateDataCSRUnstructuredName = _SslCertificateDataCSRUnstructuredName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 6, 6, 14),
    _SslCertificateDataCSRUnstructuredName_Type()
)
sslCertificateDataCSRUnstructuredName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCertificateDataCSRUnstructuredName.setStatus("mandatory")
_CertDomainNames_ObjectIdentity = ObjectIdentity
certDomainNames = _CertDomainNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 8)
)
_CertDomainNameTable_Object = MibTable
certDomainNameTable = _CertDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 8, 1)
)
if mibBuilder.loadTexts:
    certDomainNameTable.setStatus("mandatory")
_CertDomainNameEntry_Object = MibTableRow
certDomainNameEntry = _CertDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 8, 1, 1)
)
certDomainNameEntry.setIndexNames(
    (0, "IMM-MIB", "certDomainNameIndex"),
)
if mibBuilder.loadTexts:
    certDomainNameEntry.setStatus("mandatory")


class _CertDomainIndex_Type(Integer32):
    """Custom type certDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CertDomainIndex_Type.__name__ = "Integer32"
_CertDomainIndex_Object = MibTableColumn
certDomainIndex = _CertDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 8, 1, 1, 1),
    _CertDomainIndex_Type()
)
certDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certDomainIndex.setStatus("mandatory")
_CertDomainName_Type = OctetString
_CertDomainName_Object = MibTableColumn
certDomainName = _CertDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 8, 1, 1, 2),
    _CertDomainName_Type()
)
certDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certDomainName.setStatus("mandatory")
_CertDomainNameStatus_Type = OctetString
_CertDomainNameStatus_Object = MibTableColumn
certDomainNameStatus = _CertDomainNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 8, 1, 1, 3),
    _CertDomainNameStatus_Type()
)
certDomainNameStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certDomainNameStatus.setStatus("mandatory")
_AddCertDomainName_Type = OctetString
_AddCertDomainName_Object = MibScalar
addCertDomainName = _AddCertDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 8, 2),
    _AddCertDomainName_Type()
)
addCertDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addCertDomainName.setStatus("mandatory")
_RmCertDomainName_Type = OctetString
_RmCertDomainName_Object = MibScalar
rmCertDomainName = _RmCertDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 8, 3),
    _RmCertDomainName_Type()
)
rmCertDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmCertDomainName.setStatus("mandatory")
_SkrServers_ObjectIdentity = ObjectIdentity
skrServers = _SkrServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9)
)
_SkrServerTable_Object = MibTable
skrServerTable = _SkrServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 1)
)
if mibBuilder.loadTexts:
    skrServerTable.setStatus("mandatory")
_SkrServerEntry_Object = MibTableRow
skrServerEntry = _SkrServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 1, 1)
)
skrServerEntry.setIndexNames(
    (0, "IMM-MIB", "skrServerIndex"),
)
if mibBuilder.loadTexts:
    skrServerEntry.setStatus("mandatory")


class _SkrServerIndex_Type(Integer32):
    """Custom type skrServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SkrServerIndex_Type.__name__ = "Integer32"
_SkrServerIndex_Object = MibTableColumn
skrServerIndex = _SkrServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 1, 1, 1),
    _SkrServerIndex_Type()
)
skrServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skrServerIndex.setStatus("mandatory")


class _SkrServerHostname_Type(OctetString):
    """Custom type skrServerHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SkrServerHostname_Type.__name__ = "OctetString"
_SkrServerHostname_Object = MibTableColumn
skrServerHostname = _SkrServerHostname_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 1, 1, 2),
    _SkrServerHostname_Type()
)
skrServerHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrServerHostname.setStatus("mandatory")
_SkrServerPort_Type = Integer32
_SkrServerPort_Object = MibTableColumn
skrServerPort = _SkrServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 1, 1, 3),
    _SkrServerPort_Type()
)
skrServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrServerPort.setStatus("mandatory")


class _SkrServerCertAction_Type(Integer32):
    """Custom type skrServerCertAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("importServerCertificate", 1),
          ("removeServerCertificate", 2))
    )


_SkrServerCertAction_Type.__name__ = "Integer32"
_SkrServerCertAction_Object = MibScalar
skrServerCertAction = _SkrServerCertAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 2),
    _SkrServerCertAction_Type()
)
skrServerCertAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    skrServerCertAction.setStatus("mandatory")


class _SkrDeviceGroup_Type(OctetString):
    """Custom type skrDeviceGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SkrDeviceGroup_Type.__name__ = "OctetString"
_SkrDeviceGroup_Object = MibScalar
skrDeviceGroup = _SkrDeviceGroup_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 3),
    _SkrDeviceGroup_Type()
)
skrDeviceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrDeviceGroup.setStatus("mandatory")
_SkrClientConfigCertficate_ObjectIdentity = ObjectIdentity
skrClientConfigCertficate = _SkrClientConfigCertficate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 4)
)


class _SkrClientCertificateGeneration_Type(Integer32):
    """Custom type skrClientCertificateGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generateNewKeyandCSR", 2),
          ("generateNewKeyandSelfSigned", 1))
    )


_SkrClientCertificateGeneration_Type.__name__ = "Integer32"
_SkrClientCertificateGeneration_Object = MibScalar
skrClientCertificateGeneration = _SkrClientCertificateGeneration_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 4, 1),
    _SkrClientCertificateGeneration_Type()
)
skrClientCertificateGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrClientCertificateGeneration.setStatus("mandatory")


class _SkrClientCertificateTransfer_Type(Integer32):
    """Custom type skrClientCertificateTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadCSR", 3),
          ("downloadCertificate", 2),
          ("importSignedCertificate", 1))
    )


_SkrClientCertificateTransfer_Type.__name__ = "Integer32"
_SkrClientCertificateTransfer_Object = MibScalar
skrClientCertificateTransfer = _SkrClientCertificateTransfer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 4, 2),
    _SkrClientCertificateTransfer_Type()
)
skrClientCertificateTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrClientCertificateTransfer.setStatus("mandatory")


class _SkrClientCertificateStatus_Type(Integer32):
    """Custom type skrClientCertificateStatus based on Integer32"""
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
        *(("ca-signed-and-csr-generated", 6),
          ("ca-signed-installed", 3),
          ("csr-generated", 4),
          ("no-cert-installed", 1),
          ("self-signed-and-csr-generated", 5),
          ("self-signed-installed", 2))
    )


_SkrClientCertificateStatus_Type.__name__ = "Integer32"
_SkrClientCertificateStatus_Object = MibScalar
skrClientCertificateStatus = _SkrClientCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 4, 3),
    _SkrClientCertificateStatus_Type()
)
skrClientCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skrClientCertificateStatus.setStatus("mandatory")
_SkrCertificateData_ObjectIdentity = ObjectIdentity
skrCertificateData = _SkrCertificateData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5)
)
_SkrCertificateDataCountry_Type = OctetString
_SkrCertificateDataCountry_Object = MibScalar
skrCertificateDataCountry = _SkrCertificateDataCountry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 1),
    _SkrCertificateDataCountry_Type()
)
skrCertificateDataCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataCountry.setStatus("mandatory")
_SkrCertificateDataStateorProvince_Type = OctetString
_SkrCertificateDataStateorProvince_Object = MibScalar
skrCertificateDataStateorProvince = _SkrCertificateDataStateorProvince_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 2),
    _SkrCertificateDataStateorProvince_Type()
)
skrCertificateDataStateorProvince.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataStateorProvince.setStatus("mandatory")
_SkrCertificateDataCityOrLocality_Type = OctetString
_SkrCertificateDataCityOrLocality_Object = MibScalar
skrCertificateDataCityOrLocality = _SkrCertificateDataCityOrLocality_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 3),
    _SkrCertificateDataCityOrLocality_Type()
)
skrCertificateDataCityOrLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataCityOrLocality.setStatus("mandatory")
_SkrCertificateDataOrganizationName_Type = OctetString
_SkrCertificateDataOrganizationName_Object = MibScalar
skrCertificateDataOrganizationName = _SkrCertificateDataOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 4),
    _SkrCertificateDataOrganizationName_Type()
)
skrCertificateDataOrganizationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataOrganizationName.setStatus("mandatory")
_SkrCertificateDataIMMHostName_Type = OctetString
_SkrCertificateDataIMMHostName_Object = MibScalar
skrCertificateDataIMMHostName = _SkrCertificateDataIMMHostName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 5),
    _SkrCertificateDataIMMHostName_Type()
)
skrCertificateDataIMMHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataIMMHostName.setStatus("mandatory")
_SkrCertificateDataContact_Type = OctetString
_SkrCertificateDataContact_Object = MibScalar
skrCertificateDataContact = _SkrCertificateDataContact_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 6),
    _SkrCertificateDataContact_Type()
)
skrCertificateDataContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataContact.setStatus("mandatory")
_SkrCertificateDataEmailAddr_Type = OctetString
_SkrCertificateDataEmailAddr_Object = MibScalar
skrCertificateDataEmailAddr = _SkrCertificateDataEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 7),
    _SkrCertificateDataEmailAddr_Type()
)
skrCertificateDataEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataEmailAddr.setStatus("mandatory")
_SkrCertificateDataOrganizationUnit_Type = OctetString
_SkrCertificateDataOrganizationUnit_Object = MibScalar
skrCertificateDataOrganizationUnit = _SkrCertificateDataOrganizationUnit_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 8),
    _SkrCertificateDataOrganizationUnit_Type()
)
skrCertificateDataOrganizationUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataOrganizationUnit.setStatus("mandatory")
_SkrCertificateDataSurname_Type = OctetString
_SkrCertificateDataSurname_Object = MibScalar
skrCertificateDataSurname = _SkrCertificateDataSurname_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 9),
    _SkrCertificateDataSurname_Type()
)
skrCertificateDataSurname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataSurname.setStatus("mandatory")
_SkrCertificateDataGivenName_Type = OctetString
_SkrCertificateDataGivenName_Object = MibScalar
skrCertificateDataGivenName = _SkrCertificateDataGivenName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 10),
    _SkrCertificateDataGivenName_Type()
)
skrCertificateDataGivenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataGivenName.setStatus("mandatory")
_SkrCertificateDataInitials_Type = OctetString
_SkrCertificateDataInitials_Object = MibScalar
skrCertificateDataInitials = _SkrCertificateDataInitials_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 11),
    _SkrCertificateDataInitials_Type()
)
skrCertificateDataInitials.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataInitials.setStatus("mandatory")
_SkrCertificateDataDNQualifier_Type = OctetString
_SkrCertificateDataDNQualifier_Object = MibScalar
skrCertificateDataDNQualifier = _SkrCertificateDataDNQualifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 12),
    _SkrCertificateDataDNQualifier_Type()
)
skrCertificateDataDNQualifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataDNQualifier.setStatus("mandatory")
_SkrCertificateDataCSRChallengePassword_Type = OctetString
_SkrCertificateDataCSRChallengePassword_Object = MibScalar
skrCertificateDataCSRChallengePassword = _SkrCertificateDataCSRChallengePassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 13),
    _SkrCertificateDataCSRChallengePassword_Type()
)
skrCertificateDataCSRChallengePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataCSRChallengePassword.setStatus("mandatory")
_SkrCertificateDataCSRUnstructuredName_Type = OctetString
_SkrCertificateDataCSRUnstructuredName_Object = MibScalar
skrCertificateDataCSRUnstructuredName = _SkrCertificateDataCSRUnstructuredName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 5, 14),
    _SkrCertificateDataCSRUnstructuredName_Type()
)
skrCertificateDataCSRUnstructuredName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrCertificateDataCSRUnstructuredName.setStatus("mandatory")


class _SkrConfigFtpServer_Type(OctetString):
    """Custom type skrConfigFtpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SkrConfigFtpServer_Type.__name__ = "OctetString"
_SkrConfigFtpServer_Object = MibScalar
skrConfigFtpServer = _SkrConfigFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 6),
    _SkrConfigFtpServer_Type()
)
skrConfigFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrConfigFtpServer.setStatus("mandatory")


class _SkrConfigFtpServerMode_Type(Integer32):
    """Custom type skrConfigFtpServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sftp", 3),
          ("tftp", 1))
    )


_SkrConfigFtpServerMode_Type.__name__ = "Integer32"
_SkrConfigFtpServerMode_Object = MibScalar
skrConfigFtpServerMode = _SkrConfigFtpServerMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 7),
    _SkrConfigFtpServerMode_Type()
)
skrConfigFtpServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrConfigFtpServerMode.setStatus("mandatory")
_SkrConfigFtpCallPort_Type = Integer32
_SkrConfigFtpCallPort_Object = MibScalar
skrConfigFtpCallPort = _SkrConfigFtpCallPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 8),
    _SkrConfigFtpCallPort_Type()
)
skrConfigFtpCallPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrConfigFtpCallPort.setStatus("mandatory")


class _SkrConfigFTPCallUserID_Type(OctetString):
    """Custom type skrConfigFTPCallUserID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SkrConfigFTPCallUserID_Type.__name__ = "OctetString"
_SkrConfigFTPCallUserID_Object = MibScalar
skrConfigFTPCallUserID = _SkrConfigFTPCallUserID_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 9),
    _SkrConfigFTPCallUserID_Type()
)
skrConfigFTPCallUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrConfigFTPCallUserID.setStatus("mandatory")


class _SkrConfigFtpCallPassword_Type(OctetString):
    """Custom type skrConfigFtpCallPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SkrConfigFtpCallPassword_Type.__name__ = "OctetString"
_SkrConfigFtpCallPassword_Object = MibScalar
skrConfigFtpCallPassword = _SkrConfigFtpCallPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 10),
    _SkrConfigFtpCallPassword_Type()
)
skrConfigFtpCallPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrConfigFtpCallPassword.setStatus("mandatory")


class _SkrConfigFileName_Type(OctetString):
    """Custom type skrConfigFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_SkrConfigFileName_Type.__name__ = "OctetString"
_SkrConfigFileName_Object = MibScalar
skrConfigFileName = _SkrConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 4, 9, 11),
    _SkrConfigFileName_Type()
)
skrConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skrConfigFileName.setStatus("mandatory")
_TcpPortAssignmentCfg_ObjectIdentity = ObjectIdentity
tcpPortAssignmentCfg = _TcpPortAssignmentCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5)
)


class _TcpPortsRestoreDefault_Type(Integer32):
    """Custom type tcpPortsRestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_TcpPortsRestoreDefault_Type.__name__ = "Integer32"
_TcpPortsRestoreDefault_Object = MibScalar
tcpPortsRestoreDefault = _TcpPortsRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5, 1),
    _TcpPortsRestoreDefault_Type()
)
tcpPortsRestoreDefault.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tcpPortsRestoreDefault.setStatus("mandatory")
_HttpPortAssignment_Type = Integer32
_HttpPortAssignment_Object = MibScalar
httpPortAssignment = _HttpPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5, 2),
    _HttpPortAssignment_Type()
)
httpPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPortAssignment.setStatus("mandatory")
_HttpsPortAssignment_Type = Integer32
_HttpsPortAssignment_Object = MibScalar
httpsPortAssignment = _HttpsPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5, 3),
    _HttpsPortAssignment_Type()
)
httpsPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsPortAssignment.setStatus("mandatory")
_TelnetLegacyCLIPortAssignment_Type = Integer32
_TelnetLegacyCLIPortAssignment_Object = MibScalar
telnetLegacyCLIPortAssignment = _TelnetLegacyCLIPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5, 4),
    _TelnetLegacyCLIPortAssignment_Type()
)
telnetLegacyCLIPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetLegacyCLIPortAssignment.setStatus("mandatory")
_SshLegacyCLIPortAssignment_Type = Integer32
_SshLegacyCLIPortAssignment_Object = MibScalar
sshLegacyCLIPortAssignment = _SshLegacyCLIPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5, 6),
    _SshLegacyCLIPortAssignment_Type()
)
sshLegacyCLIPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshLegacyCLIPortAssignment.setStatus("mandatory")
_SnmpAgentPortAssignment_Type = Integer32
_SnmpAgentPortAssignment_Object = MibScalar
snmpAgentPortAssignment = _SnmpAgentPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5, 8),
    _SnmpAgentPortAssignment_Type()
)
snmpAgentPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentPortAssignment.setStatus("mandatory")
_SnmpTrapsPortAssignment_Type = Integer32
_SnmpTrapsPortAssignment_Object = MibScalar
snmpTrapsPortAssignment = _SnmpTrapsPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5, 9),
    _SnmpTrapsPortAssignment_Type()
)
snmpTrapsPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapsPortAssignment.setStatus("mandatory")
_RemvidPortAssignment_Type = Integer32
_RemvidPortAssignment_Object = MibScalar
remvidPortAssignment = _RemvidPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5, 10),
    _RemvidPortAssignment_Type()
)
remvidPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remvidPortAssignment.setStatus("mandatory")
_IbmSystemDirectorHttpPortAssignment_Type = Integer32
_IbmSystemDirectorHttpPortAssignment_Object = MibScalar
ibmSystemDirectorHttpPortAssignment = _IbmSystemDirectorHttpPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5, 11),
    _IbmSystemDirectorHttpPortAssignment_Type()
)
ibmSystemDirectorHttpPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSystemDirectorHttpPortAssignment.setStatus("mandatory")
_IbmSystemDirectorHttpsPortAssignment_Type = Integer32
_IbmSystemDirectorHttpsPortAssignment_Object = MibScalar
ibmSystemDirectorHttpsPortAssignment = _IbmSystemDirectorHttpsPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 5, 12),
    _IbmSystemDirectorHttpsPortAssignment_Type()
)
ibmSystemDirectorHttpsPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSystemDirectorHttpsPortAssignment.setStatus("mandatory")
_LdapClientCfg_ObjectIdentity = ObjectIdentity
ldapClientCfg = _LdapClientCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6)
)


class _LdapServer1NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer1NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer1NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer1NameOrIPAddress_Object = MibScalar
ldapServer1NameOrIPAddress = _LdapServer1NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 1),
    _LdapServer1NameOrIPAddress_Type()
)
ldapServer1NameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer1NameOrIPAddress.setStatus("mandatory")
_LdapServer1PortNumber_Type = Integer32
_LdapServer1PortNumber_Object = MibScalar
ldapServer1PortNumber = _LdapServer1PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 2),
    _LdapServer1PortNumber_Type()
)
ldapServer1PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer1PortNumber.setStatus("mandatory")


class _LdapServer2NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer2NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer2NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer2NameOrIPAddress_Object = MibScalar
ldapServer2NameOrIPAddress = _LdapServer2NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 3),
    _LdapServer2NameOrIPAddress_Type()
)
ldapServer2NameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer2NameOrIPAddress.setStatus("mandatory")
_LdapServer2PortNumber_Type = Integer32
_LdapServer2PortNumber_Object = MibScalar
ldapServer2PortNumber = _LdapServer2PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 4),
    _LdapServer2PortNumber_Type()
)
ldapServer2PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer2PortNumber.setStatus("mandatory")


class _LdapServer3NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer3NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer3NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer3NameOrIPAddress_Object = MibScalar
ldapServer3NameOrIPAddress = _LdapServer3NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 5),
    _LdapServer3NameOrIPAddress_Type()
)
ldapServer3NameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer3NameOrIPAddress.setStatus("mandatory")
_LdapServer3PortNumber_Type = Integer32
_LdapServer3PortNumber_Object = MibScalar
ldapServer3PortNumber = _LdapServer3PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 6),
    _LdapServer3PortNumber_Type()
)
ldapServer3PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer3PortNumber.setStatus("mandatory")


class _LdapServer4NameOrIPAddress_Type(OctetString):
    """Custom type ldapServer4NameOrIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapServer4NameOrIPAddress_Type.__name__ = "OctetString"
_LdapServer4NameOrIPAddress_Object = MibScalar
ldapServer4NameOrIPAddress = _LdapServer4NameOrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 7),
    _LdapServer4NameOrIPAddress_Type()
)
ldapServer4NameOrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer4NameOrIPAddress.setStatus("mandatory")
_LdapServer4PortNumber_Type = Integer32
_LdapServer4PortNumber_Object = MibScalar
ldapServer4PortNumber = _LdapServer4PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 8),
    _LdapServer4PortNumber_Type()
)
ldapServer4PortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServer4PortNumber.setStatus("mandatory")


class _LdapRootDN_Type(OctetString):
    """Custom type ldapRootDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapRootDN_Type.__name__ = "OctetString"
_LdapRootDN_Object = MibScalar
ldapRootDN = _LdapRootDN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 9),
    _LdapRootDN_Type()
)
ldapRootDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapRootDN.setStatus("mandatory")


class _LdapUserSearchBaseDN_Type(OctetString):
    """Custom type ldapUserSearchBaseDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapUserSearchBaseDN_Type.__name__ = "OctetString"
_LdapUserSearchBaseDN_Object = MibScalar
ldapUserSearchBaseDN = _LdapUserSearchBaseDN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 10),
    _LdapUserSearchBaseDN_Type()
)
ldapUserSearchBaseDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapUserSearchBaseDN.setStatus("deprecated")


class _LdapGroupFilter_Type(OctetString):
    """Custom type ldapGroupFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_LdapGroupFilter_Type.__name__ = "OctetString"
_LdapGroupFilter_Object = MibScalar
ldapGroupFilter = _LdapGroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 11),
    _LdapGroupFilter_Type()
)
ldapGroupFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapGroupFilter.setStatus("mandatory")


class _LdapBindingMethod_Type(Integer32):
    """Custom type ldapBindingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anonymousAuthentication", 0),
          ("clientAuthentication", 1),
          ("userPrincipalName", 2))
    )


_LdapBindingMethod_Type.__name__ = "Integer32"
_LdapBindingMethod_Object = MibScalar
ldapBindingMethod = _LdapBindingMethod_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 12),
    _LdapBindingMethod_Type()
)
ldapBindingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapBindingMethod.setStatus("mandatory")


class _LdapClientAuthenticationDN_Type(OctetString):
    """Custom type ldapClientAuthenticationDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapClientAuthenticationDN_Type.__name__ = "OctetString"
_LdapClientAuthenticationDN_Object = MibScalar
ldapClientAuthenticationDN = _LdapClientAuthenticationDN_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 13),
    _LdapClientAuthenticationDN_Type()
)
ldapClientAuthenticationDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapClientAuthenticationDN.setStatus("mandatory")


class _LdapClientAuthenticationPassword_Type(OctetString):
    """Custom type ldapClientAuthenticationPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_LdapClientAuthenticationPassword_Type.__name__ = "OctetString"
_LdapClientAuthenticationPassword_Object = MibScalar
ldapClientAuthenticationPassword = _LdapClientAuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 14),
    _LdapClientAuthenticationPassword_Type()
)
ldapClientAuthenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapClientAuthenticationPassword.setStatus("mandatory")


class _LdapRoleBasedSecurityEnabled_Type(Integer32):
    """Custom type ldapRoleBasedSecurityEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LdapRoleBasedSecurityEnabled_Type.__name__ = "Integer32"
_LdapRoleBasedSecurityEnabled_Object = MibScalar
ldapRoleBasedSecurityEnabled = _LdapRoleBasedSecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 15),
    _LdapRoleBasedSecurityEnabled_Type()
)
ldapRoleBasedSecurityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapRoleBasedSecurityEnabled.setStatus("mandatory")


class _LdapServerTargetName_Type(OctetString):
    """Custom type ldapServerTargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LdapServerTargetName_Type.__name__ = "OctetString"
_LdapServerTargetName_Object = MibScalar
ldapServerTargetName = _LdapServerTargetName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 16),
    _LdapServerTargetName_Type()
)
ldapServerTargetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServerTargetName.setStatus("mandatory")


class _LdapUIDsearchAttribute_Type(OctetString):
    """Custom type ldapUIDsearchAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapUIDsearchAttribute_Type.__name__ = "OctetString"
_LdapUIDsearchAttribute_Object = MibScalar
ldapUIDsearchAttribute = _LdapUIDsearchAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 17),
    _LdapUIDsearchAttribute_Type()
)
ldapUIDsearchAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapUIDsearchAttribute.setStatus("mandatory")


class _LdapGroupSearchAttribute_Type(OctetString):
    """Custom type ldapGroupSearchAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapGroupSearchAttribute_Type.__name__ = "OctetString"
_LdapGroupSearchAttribute_Object = MibScalar
ldapGroupSearchAttribute = _LdapGroupSearchAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 18),
    _LdapGroupSearchAttribute_Type()
)
ldapGroupSearchAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapGroupSearchAttribute.setStatus("mandatory")


class _LdapLoginPermissionAttribute_Type(OctetString):
    """Custom type ldapLoginPermissionAttribute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapLoginPermissionAttribute_Type.__name__ = "OctetString"
_LdapLoginPermissionAttribute_Object = MibScalar
ldapLoginPermissionAttribute = _LdapLoginPermissionAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 19),
    _LdapLoginPermissionAttribute_Type()
)
ldapLoginPermissionAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapLoginPermissionAttribute.setStatus("mandatory")


class _LdapUseDNSOrPreConfiguredServers_Type(Integer32):
    """Custom type ldapUseDNSOrPreConfiguredServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useDNSToFindLDAPServers", 1),
          ("usePreConfiguredLDAPServers", 0))
    )


_LdapUseDNSOrPreConfiguredServers_Type.__name__ = "Integer32"
_LdapUseDNSOrPreConfiguredServers_Object = MibScalar
ldapUseDNSOrPreConfiguredServers = _LdapUseDNSOrPreConfiguredServers_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 20),
    _LdapUseDNSOrPreConfiguredServers_Type()
)
ldapUseDNSOrPreConfiguredServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapUseDNSOrPreConfiguredServers.setStatus("mandatory")


class _LdapDomainSource_Type(Integer32):
    """Custom type ldapDomainSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extractSearchDomainFromLoginID", 0),
          ("tryLoginFirstThenConfiguredValue", 2),
          ("useOnlyConfiguredSearchDomainBelow", 1))
    )


_LdapDomainSource_Type.__name__ = "Integer32"
_LdapDomainSource_Object = MibScalar
ldapDomainSource = _LdapDomainSource_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 21),
    _LdapDomainSource_Type()
)
ldapDomainSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapDomainSource.setStatus("mandatory")


class _LdapForestName_Type(OctetString):
    """Custom type ldapForestName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapForestName_Type.__name__ = "OctetString"
_LdapForestName_Object = MibScalar
ldapForestName = _LdapForestName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 22),
    _LdapForestName_Type()
)
ldapForestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapForestName.setStatus("mandatory")


class _LdapAuthCfg_Type(Integer32):
    """Custom type ldapAuthCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authenticationAndAuthorization", 0),
          ("authenticationOnly", 1))
    )


_LdapAuthCfg_Type.__name__ = "Integer32"
_LdapAuthCfg_Object = MibScalar
ldapAuthCfg = _LdapAuthCfg_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 23),
    _LdapAuthCfg_Type()
)
ldapAuthCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapAuthCfg.setStatus("mandatory")


class _LdapSearchDomain_Type(OctetString):
    """Custom type ldapSearchDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LdapSearchDomain_Type.__name__ = "OctetString"
_LdapSearchDomain_Object = MibScalar
ldapSearchDomain = _LdapSearchDomain_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 24),
    _LdapSearchDomain_Type()
)
ldapSearchDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapSearchDomain.setStatus("mandatory")


class _LdapServiceName_Type(OctetString):
    """Custom type ldapServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LdapServiceName_Type.__name__ = "OctetString"
_LdapServiceName_Object = MibScalar
ldapServiceName = _LdapServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 6, 25),
    _LdapServiceName_Type()
)
ldapServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ldapServiceName.setStatus("mandatory")
_NtpConfig_ObjectIdentity = ObjectIdentity
ntpConfig = _NtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 8)
)


class _NtpEnable_Type(Integer32):
    """Custom type ntpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NtpEnable_Type.__name__ = "Integer32"
_NtpEnable_Object = MibScalar
ntpEnable = _NtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 8, 1),
    _NtpEnable_Type()
)
ntpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpEnable.setStatus("mandatory")


class _NtpIpAddressHostname1_Type(OctetString):
    """Custom type ntpIpAddressHostname1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NtpIpAddressHostname1_Type.__name__ = "OctetString"
_NtpIpAddressHostname1_Object = MibScalar
ntpIpAddressHostname1 = _NtpIpAddressHostname1_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 8, 2),
    _NtpIpAddressHostname1_Type()
)
ntpIpAddressHostname1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpIpAddressHostname1.setStatus("mandatory")
_NtpUpdateFrequency_Type = Integer32
_NtpUpdateFrequency_Object = MibScalar
ntpUpdateFrequency = _NtpUpdateFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 8, 3),
    _NtpUpdateFrequency_Type()
)
ntpUpdateFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpUpdateFrequency.setStatus("mandatory")


class _NtpIpAddressHostname2_Type(OctetString):
    """Custom type ntpIpAddressHostname2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NtpIpAddressHostname2_Type.__name__ = "OctetString"
_NtpIpAddressHostname2_Object = MibScalar
ntpIpAddressHostname2 = _NtpIpAddressHostname2_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 8, 4),
    _NtpIpAddressHostname2_Type()
)
ntpIpAddressHostname2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpIpAddressHostname2.setStatus("mandatory")


class _NtpUpdateClock_Type(Integer32):
    """Custom type ntpUpdateClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_NtpUpdateClock_Type.__name__ = "Integer32"
_NtpUpdateClock_Object = MibScalar
ntpUpdateClock = _NtpUpdateClock_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 8, 5),
    _NtpUpdateClock_Type()
)
ntpUpdateClock.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ntpUpdateClock.setStatus("mandatory")


class _NtpIpAddressHostname3_Type(OctetString):
    """Custom type ntpIpAddressHostname3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NtpIpAddressHostname3_Type.__name__ = "OctetString"
_NtpIpAddressHostname3_Object = MibScalar
ntpIpAddressHostname3 = _NtpIpAddressHostname3_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 8, 6),
    _NtpIpAddressHostname3_Type()
)
ntpIpAddressHostname3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpIpAddressHostname3.setStatus("mandatory")


class _NtpIpAddressHostname4_Type(OctetString):
    """Custom type ntpIpAddressHostname4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_NtpIpAddressHostname4_Type.__name__ = "OctetString"
_NtpIpAddressHostname4_Object = MibScalar
ntpIpAddressHostname4 = _NtpIpAddressHostname4_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 4, 2, 8, 7),
    _NtpIpAddressHostname4_Type()
)
ntpIpAddressHostname4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpIpAddressHostname4.setStatus("mandatory")
_ConfigurationManagement_ObjectIdentity = ObjectIdentity
configurationManagement = _ConfigurationManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 5)
)


class _ConfigurationManagementTftpServer_Type(OctetString):
    """Custom type configurationManagementTftpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ConfigurationManagementTftpServer_Type.__name__ = "OctetString"
_ConfigurationManagementTftpServer_Object = MibScalar
configurationManagementTftpServer = _ConfigurationManagementTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 5, 1),
    _ConfigurationManagementTftpServer_Type()
)
configurationManagementTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationManagementTftpServer.setStatus("mandatory")


class _ConfigurationManagementFileName_Type(OctetString):
    """Custom type configurationManagementFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_ConfigurationManagementFileName_Type.__name__ = "OctetString"
_ConfigurationManagementFileName_Object = MibScalar
configurationManagementFileName = _ConfigurationManagementFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 5, 2),
    _ConfigurationManagementFileName_Type()
)
configurationManagementFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationManagementFileName.setStatus("mandatory")


class _ConfigurationManagementSaveStart_Type(Integer32):
    """Custom type configurationManagementSaveStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 1),
          ("execute-nowait", 2))
    )


_ConfigurationManagementSaveStart_Type.__name__ = "Integer32"
_ConfigurationManagementSaveStart_Object = MibScalar
configurationManagementSaveStart = _ConfigurationManagementSaveStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 5, 3),
    _ConfigurationManagementSaveStart_Type()
)
configurationManagementSaveStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationManagementSaveStart.setStatus("mandatory")


class _ConfigurationManagementRestoreStart_Type(Integer32):
    """Custom type configurationManagementRestoreStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 1),
          ("execute-nowait", 2))
    )


_ConfigurationManagementRestoreStart_Type.__name__ = "Integer32"
_ConfigurationManagementRestoreStart_Object = MibScalar
configurationManagementRestoreStart = _ConfigurationManagementRestoreStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 5, 4),
    _ConfigurationManagementRestoreStart_Type()
)
configurationManagementRestoreStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationManagementRestoreStart.setStatus("mandatory")


class _ConfigurationManagementStatus_Type(Integer32):
    """Custom type configurationManagementStatus based on Integer32"""
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
        *(("failed", 1),
          ("restoring", 3),
          ("saving", 2),
          ("success", 0))
    )


_ConfigurationManagementStatus_Type.__name__ = "Integer32"
_ConfigurationManagementStatus_Object = MibScalar
configurationManagementStatus = _ConfigurationManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 5, 5),
    _ConfigurationManagementStatus_Type()
)
configurationManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationManagementStatus.setStatus("mandatory")


class _ImmVersionCheck_Type(Integer32):
    """Custom type immVersionCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("immVersion", 2)
    )


_ImmVersionCheck_Type.__name__ = "Integer32"
_ImmVersionCheck_Object = MibScalar
immVersionCheck = _ImmVersionCheck_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 3, 7),
    _ImmVersionCheck_Type()
)
immVersionCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    immVersionCheck.setStatus("mandatory")
_GeneralSystemSettings_ObjectIdentity = ObjectIdentity
generalSystemSettings = _GeneralSystemSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 4)
)
_ServerTimers_ObjectIdentity = ObjectIdentity
serverTimers = _ServerTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 4, 1)
)


class _OSHang_Type(Integer32):
    """Custom type oSHang based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              150,
              180,
              210,
              240,
              600)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("fourMinutes", 240),
          ("tenMinutes", 600),
          ("threeAndHalfMinutes", 210),
          ("threeMinutes", 180),
          ("twoAndHalfMinutes", 150))
    )


_OSHang_Type.__name__ = "Integer32"
_OSHang_Object = MibScalar
oSHang = _OSHang_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 4, 1, 1),
    _OSHang_Type()
)
oSHang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oSHang.setStatus("mandatory")


class _OSLoader_Type(Integer32):
    """Custom type oSLoader based on Integer32"""
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
              8,
              9,
              10,
              15,
              20,
              30,
              40,
              60,
              120,
              240)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("fifteenMinutes", 30),
          ("fiveMinutes", 10),
          ("fourAndHalfMinutes", 9),
          ("fourMinutes", 8),
          ("oneAndHalfMinutes", 3),
          ("oneHalfMinutes", 1),
          ("oneHour", 120),
          ("oneMinutes", 2),
          ("sevenAndHalfMinutes", 15),
          ("tenMinutes", 20),
          ("thirtyMinutes", 60),
          ("threeAndHalfMinutes", 7),
          ("threeMinutes", 6),
          ("twentyMinutes", 40),
          ("twoAndHalfMinutes", 5),
          ("twoHours", 240),
          ("twoMinutes", 4))
    )


_OSLoader_Type.__name__ = "Integer32"
_OSLoader_Object = MibScalar
oSLoader = _OSLoader_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 4, 1, 2),
    _OSLoader_Type()
)
oSLoader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oSLoader.setStatus("mandatory")


class _NetworkPXEboot_Type(Integer32):
    """Custom type networkPXEboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("networkPXEBootDisabled", 0),
          ("networkPXEBootEnabled", 1))
    )


_NetworkPXEboot_Type.__name__ = "Integer32"
_NetworkPXEboot_Object = MibScalar
networkPXEboot = _NetworkPXEboot_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 4, 2),
    _NetworkPXEboot_Type()
)
networkPXEboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkPXEboot.setStatus("mandatory")
_SystemPower_ObjectIdentity = ObjectIdentity
systemPower = _SystemPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5)
)
_PowerStatistics_ObjectIdentity = ObjectIdentity
powerStatistics = _PowerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 1)
)


class _CurrentSysPowerStatus_Type(Integer32):
    """Custom type currentSysPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("poweredOff", 0),
          ("poweredOn", 255),
          ("sleepS3", 1))
    )


_CurrentSysPowerStatus_Type.__name__ = "Integer32"
_CurrentSysPowerStatus_Object = MibScalar
currentSysPowerStatus = _CurrentSysPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 1, 1),
    _CurrentSysPowerStatus_Type()
)
currentSysPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSysPowerStatus.setStatus("mandatory")
_PowerOnHours_Type = Integer32
_PowerOnHours_Object = MibScalar
powerOnHours = _PowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 1, 2),
    _PowerOnHours_Type()
)
powerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnHours.setStatus("mandatory")
_RestartCount_Type = Integer32
_RestartCount_Object = MibScalar
restartCount = _RestartCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 1, 3),
    _RestartCount_Type()
)
restartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restartCount.setStatus("mandatory")


class _SystemState_Type(Integer32):
    """Custom type systemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bootingOSorInUnsupportedOS", 4),
          ("oSBooted", 5),
          ("suspendToRAM", 6),
          ("systemInUEFI", 2),
          ("systemPowerOfforStateUnknown", 0),
          ("systemPowerOnorStartingUEFI", 1),
          ("uEFIErrorDetected", 3))
    )


_SystemState_Type.__name__ = "Integer32"
_SystemState_Object = MibScalar
systemState = _SystemState_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 1, 4),
    _SystemState_Type()
)
systemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemState.setStatus("mandatory")
_PowerSysConfig_ObjectIdentity = ObjectIdentity
powerSysConfig = _PowerSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 2)
)


class _PowerSysOffDelay_Type(Integer32):
    """Custom type powerSysOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              30,
              60,
              120,
              180,
              240,
              300,
              450,
              600,
              900,
              1200,
              1800,
              3600,
              7200)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 900),
          ("fiveMinute", 300),
          ("fourMinutes", 240),
          ("noDelay", 0),
          ("oneHalfMinute", 30),
          ("oneHour", 3600),
          ("oneMinute", 60),
          ("sevenAndHalfMinutes", 450),
          ("tenMinutes", 600),
          ("thirtyMinutes", 1800),
          ("threeMinutes", 180),
          ("twentyMinutes", 1200),
          ("twoHours", 7200),
          ("twoMinutes", 120))
    )


_PowerSysOffDelay_Type.__name__ = "Integer32"
_PowerSysOffDelay_Object = MibScalar
powerSysOffDelay = _PowerSysOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 2, 1),
    _PowerSysOffDelay_Type()
)
powerSysOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSysOffDelay.setStatus("mandatory")
_PowerSysOnClockSetting_Type = OctetString
_PowerSysOnClockSetting_Object = MibScalar
powerSysOnClockSetting = _PowerSysOnClockSetting_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 2, 2),
    _PowerSysOnClockSetting_Type()
)
powerSysOnClockSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSysOnClockSetting.setStatus("mandatory")
_PowerOffSystemControl_ObjectIdentity = ObjectIdentity
powerOffSystemControl = _PowerOffSystemControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 3)
)


class _PowerOffWithOsShutdown_Type(Integer32):
    """Custom type powerOffWithOsShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_PowerOffWithOsShutdown_Type.__name__ = "Integer32"
_PowerOffWithOsShutdown_Object = MibScalar
powerOffWithOsShutdown = _PowerOffWithOsShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 3, 1),
    _PowerOffWithOsShutdown_Type()
)
powerOffWithOsShutdown.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    powerOffWithOsShutdown.setStatus("mandatory")


class _PowerOffImmediately_Type(Integer32):
    """Custom type powerOffImmediately based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_PowerOffImmediately_Type.__name__ = "Integer32"
_PowerOffImmediately_Object = MibScalar
powerOffImmediately = _PowerOffImmediately_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 3, 2),
    _PowerOffImmediately_Type()
)
powerOffImmediately.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    powerOffImmediately.setStatus("mandatory")
_PowerOnSystemControl_ObjectIdentity = ObjectIdentity
powerOnSystemControl = _PowerOnSystemControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 4)
)


class _PowerOnImmediately_Type(Integer32):
    """Custom type powerOnImmediately based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_PowerOnImmediately_Type.__name__ = "Integer32"
_PowerOnImmediately_Object = MibScalar
powerOnImmediately = _PowerOnImmediately_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 4, 2),
    _PowerOnImmediately_Type()
)
powerOnImmediately.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    powerOnImmediately.setStatus("mandatory")
_PowerCyclingSchedule_ObjectIdentity = ObjectIdentity
powerCyclingSchedule = _PowerCyclingSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 5)
)
_SchedulePowerOffWithOsShutdown_Type = OctetString
_SchedulePowerOffWithOsShutdown_Object = MibScalar
schedulePowerOffWithOsShutdown = _SchedulePowerOffWithOsShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 5, 1),
    _SchedulePowerOffWithOsShutdown_Type()
)
schedulePowerOffWithOsShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePowerOffWithOsShutdown.setStatus("mandatory")
_SchedulePowerOnSystem_Type = OctetString
_SchedulePowerOnSystem_Object = MibScalar
schedulePowerOnSystem = _SchedulePowerOnSystem_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 5, 2),
    _SchedulePowerOnSystem_Type()
)
schedulePowerOnSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePowerOnSystem.setStatus("mandatory")
_PowerControlSleep_ObjectIdentity = ObjectIdentity
powerControlSleep = _PowerControlSleep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 6)
)


class _PowerEnterSleep_Type(Integer32):
    """Custom type powerEnterSleep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_PowerEnterSleep_Type.__name__ = "Integer32"
_PowerEnterSleep_Object = MibScalar
powerEnterSleep = _PowerEnterSleep_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 6, 1),
    _PowerEnterSleep_Type()
)
powerEnterSleep.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    powerEnterSleep.setStatus("mandatory")


class _PowerExitSleep_Type(Integer32):
    """Custom type powerExitSleep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_PowerExitSleep_Type.__name__ = "Integer32"
_PowerExitSleep_Object = MibScalar
powerExitSleep = _PowerExitSleep_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 5, 6, 2),
    _PowerExitSleep_Type()
)
powerExitSleep.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    powerExitSleep.setStatus("mandatory")
_RestartReset_ObjectIdentity = ObjectIdentity
restartReset = _RestartReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 6)
)


class _ShutdownOsThenRestart_Type(Integer32):
    """Custom type shutdownOsThenRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_ShutdownOsThenRestart_Type.__name__ = "Integer32"
_ShutdownOsThenRestart_Object = MibScalar
shutdownOsThenRestart = _ShutdownOsThenRestart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 6, 1),
    _ShutdownOsThenRestart_Type()
)
shutdownOsThenRestart.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    shutdownOsThenRestart.setStatus("mandatory")


class _RestartSystemImmediately_Type(Integer32):
    """Custom type restartSystemImmediately based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_RestartSystemImmediately_Type.__name__ = "Integer32"
_RestartSystemImmediately_Object = MibScalar
restartSystemImmediately = _RestartSystemImmediately_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 6, 2),
    _RestartSystemImmediately_Type()
)
restartSystemImmediately.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    restartSystemImmediately.setStatus("mandatory")


class _RestartSPImmediately_Type(Integer32):
    """Custom type restartSPImmediately based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_RestartSPImmediately_Type.__name__ = "Integer32"
_RestartSPImmediately_Object = MibScalar
restartSPImmediately = _RestartSPImmediately_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 6, 3),
    _RestartSPImmediately_Type()
)
restartSPImmediately.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    restartSPImmediately.setStatus("mandatory")


class _ResetSPConfigAndRestart_Type(Integer32):
    """Custom type resetSPConfigAndRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_ResetSPConfigAndRestart_Type.__name__ = "Integer32"
_ResetSPConfigAndRestart_Object = MibScalar
resetSPConfigAndRestart = _ResetSPConfigAndRestart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 6, 4),
    _ResetSPConfigAndRestart_Type()
)
resetSPConfigAndRestart.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    resetSPConfigAndRestart.setStatus("mandatory")
_ScheduleShutdownOsThenRestart_Type = OctetString
_ScheduleShutdownOsThenRestart_Object = MibScalar
scheduleShutdownOsThenRestart = _ScheduleShutdownOsThenRestart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 6, 5),
    _ScheduleShutdownOsThenRestart_Type()
)
scheduleShutdownOsThenRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleShutdownOsThenRestart.setStatus("mandatory")


class _ResetPowerSchedules_Type(Integer32):
    """Custom type resetPowerSchedules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_ResetPowerSchedules_Type.__name__ = "Integer32"
_ResetPowerSchedules_Object = MibScalar
resetPowerSchedules = _ResetPowerSchedules_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 6, 6),
    _ResetPowerSchedules_Type()
)
resetPowerSchedules.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    resetPowerSchedules.setStatus("mandatory")
_FirmwareUpdate_ObjectIdentity = ObjectIdentity
firmwareUpdate = _FirmwareUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 7)
)


class _FirmwareUpdateTarget_Type(Integer32):
    """Custom type firmwareUpdateTarget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("immCard", 0)
    )


_FirmwareUpdateTarget_Type.__name__ = "Integer32"
_FirmwareUpdateTarget_Object = MibScalar
firmwareUpdateTarget = _FirmwareUpdateTarget_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 7, 1),
    _FirmwareUpdateTarget_Type()
)
firmwareUpdateTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateTarget.setStatus("mandatory")


class _FirmwareUpdateTftpServer_Type(OctetString):
    """Custom type firmwareUpdateTftpServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FirmwareUpdateTftpServer_Type.__name__ = "OctetString"
_FirmwareUpdateTftpServer_Object = MibScalar
firmwareUpdateTftpServer = _FirmwareUpdateTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 7, 2),
    _FirmwareUpdateTftpServer_Type()
)
firmwareUpdateTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateTftpServer.setStatus("mandatory")


class _FirmwareUpdateFileName_Type(OctetString):
    """Custom type firmwareUpdateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FirmwareUpdateFileName_Type.__name__ = "OctetString"
_FirmwareUpdateFileName_Object = MibScalar
firmwareUpdateFileName = _FirmwareUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 7, 3),
    _FirmwareUpdateFileName_Type()
)
firmwareUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareUpdateFileName.setStatus("mandatory")


class _FirmwareUpdateStart_Type(Integer32):
    """Custom type firmwareUpdateStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_FirmwareUpdateStart_Type.__name__ = "Integer32"
_FirmwareUpdateStart_Object = MibScalar
firmwareUpdateStart = _FirmwareUpdateStart_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 7, 4),
    _FirmwareUpdateStart_Type()
)
firmwareUpdateStart.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    firmwareUpdateStart.setStatus("mandatory")
_FirmwareUpdateStatus_Type = OctetString
_FirmwareUpdateStatus_Object = MibScalar
firmwareUpdateStatus = _FirmwareUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 7, 5),
    _FirmwareUpdateStatus_Type()
)
firmwareUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpdateStatus.setStatus("mandatory")
_ServiceAdvisor_ObjectIdentity = ObjectIdentity
serviceAdvisor = _ServiceAdvisor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8)
)
_AutoCallHomeSetup_ObjectIdentity = ObjectIdentity
autoCallHomeSetup = _AutoCallHomeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 1)
)


class _AcceptLicenseAgreement_Type(Integer32):
    """Custom type acceptLicenseAgreement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AcceptLicenseAgreement_Type.__name__ = "Integer32"
_AcceptLicenseAgreement_Object = MibScalar
acceptLicenseAgreement = _AcceptLicenseAgreement_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 1, 1),
    _AcceptLicenseAgreement_Type()
)
acceptLicenseAgreement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acceptLicenseAgreement.setStatus("mandatory")


class _ServiceAdvisorEnable_Type(Integer32):
    """Custom type serviceAdvisorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ServiceAdvisorEnable_Type.__name__ = "Integer32"
_ServiceAdvisorEnable_Object = MibScalar
serviceAdvisorEnable = _ServiceAdvisorEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 1, 2),
    _ServiceAdvisorEnable_Type()
)
serviceAdvisorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceAdvisorEnable.setStatus("mandatory")
_ServiceSupportCenter_ObjectIdentity = ObjectIdentity
serviceSupportCenter = _ServiceSupportCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 2)
)
_IbmSupportCenter_Type = OctetString
_IbmSupportCenter_Object = MibScalar
ibmSupportCenter = _IbmSupportCenter_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 2, 1),
    _IbmSupportCenter_Type()
)
ibmSupportCenter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSupportCenter.setStatus("mandatory")
_ContactInformation_ObjectIdentity = ObjectIdentity
contactInformation = _ContactInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3)
)
_CompanyName_Type = OctetString
_CompanyName_Object = MibScalar
companyName = _CompanyName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 1),
    _CompanyName_Type()
)
companyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    companyName.setStatus("mandatory")
_ContactName_Type = OctetString
_ContactName_Object = MibScalar
contactName = _ContactName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 2),
    _ContactName_Type()
)
contactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contactName.setStatus("mandatory")
_PhoneNumber_Type = OctetString
_PhoneNumber_Object = MibScalar
phoneNumber = _PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 3),
    _PhoneNumber_Type()
)
phoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phoneNumber.setStatus("mandatory")
_EmailAddress_Type = OctetString
_EmailAddress_Object = MibScalar
emailAddress = _EmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 4),
    _EmailAddress_Type()
)
emailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailAddress.setStatus("mandatory")
_Address_Type = OctetString
_Address_Object = MibScalar
address = _Address_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 5),
    _Address_Type()
)
address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    address.setStatus("mandatory")
_City_Type = OctetString
_City_Object = MibScalar
city = _City_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 6),
    _City_Type()
)
city.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    city.setStatus("mandatory")
_State_Type = OctetString
_State_Object = MibScalar
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 7),
    _State_Type()
)
state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    state.setStatus("mandatory")
_PostalCode_Type = OctetString
_PostalCode_Object = MibScalar
postalCode = _PostalCode_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 8),
    _PostalCode_Type()
)
postalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    postalCode.setStatus("mandatory")
_PhoneExtension_Type = OctetString
_PhoneExtension_Object = MibScalar
phoneExtension = _PhoneExtension_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 9),
    _PhoneExtension_Type()
)
phoneExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phoneExtension.setStatus("mandatory")
_AltContactName_Type = OctetString
_AltContactName_Object = MibScalar
altContactName = _AltContactName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 10),
    _AltContactName_Type()
)
altContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altContactName.setStatus("mandatory")
_AltPhoneNumber_Type = OctetString
_AltPhoneNumber_Object = MibScalar
altPhoneNumber = _AltPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 11),
    _AltPhoneNumber_Type()
)
altPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altPhoneNumber.setStatus("mandatory")
_AltPhoneExtension_Type = OctetString
_AltPhoneExtension_Object = MibScalar
altPhoneExtension = _AltPhoneExtension_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 12),
    _AltPhoneExtension_Type()
)
altPhoneExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altPhoneExtension.setStatus("mandatory")
_AltEmailAddress_Type = OctetString
_AltEmailAddress_Object = MibScalar
altEmailAddress = _AltEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 13),
    _AltEmailAddress_Type()
)
altEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    altEmailAddress.setStatus("mandatory")
_MachineLocationPhoneNumber_Type = OctetString
_MachineLocationPhoneNumber_Object = MibScalar
machineLocationPhoneNumber = _MachineLocationPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 3, 14),
    _MachineLocationPhoneNumber_Type()
)
machineLocationPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    machineLocationPhoneNumber.setStatus("mandatory")
_HttpProxyConfig_ObjectIdentity = ObjectIdentity
httpProxyConfig = _HttpProxyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 4)
)


class _HttpProxyEnable_Type(Integer32):
    """Custom type httpProxyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HttpProxyEnable_Type.__name__ = "Integer32"
_HttpProxyEnable_Object = MibScalar
httpProxyEnable = _HttpProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 4, 1),
    _HttpProxyEnable_Type()
)
httpProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpProxyEnable.setStatus("mandatory")
_HttpProxyLocation_Type = OctetString
_HttpProxyLocation_Object = MibScalar
httpProxyLocation = _HttpProxyLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 4, 2),
    _HttpProxyLocation_Type()
)
httpProxyLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpProxyLocation.setStatus("mandatory")
_HttpProxyPort_Type = Integer32
_HttpProxyPort_Object = MibScalar
httpProxyPort = _HttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 4, 3),
    _HttpProxyPort_Type()
)
httpProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpProxyPort.setStatus("mandatory")
_HttpProxyUserName_Type = OctetString
_HttpProxyUserName_Object = MibScalar
httpProxyUserName = _HttpProxyUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 4, 4),
    _HttpProxyUserName_Type()
)
httpProxyUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpProxyUserName.setStatus("mandatory")
_HttpProxyPassword_Type = OctetString
_HttpProxyPassword_Object = MibScalar
httpProxyPassword = _HttpProxyPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 4, 5),
    _HttpProxyPassword_Type()
)
httpProxyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpProxyPassword.setStatus("mandatory")
_ActivityLogs_ObjectIdentity = ObjectIdentity
activityLogs = _ActivityLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 5)
)
_ActivityLogTable_Object = MibTable
activityLogTable = _ActivityLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 5, 1)
)
if mibBuilder.loadTexts:
    activityLogTable.setStatus("mandatory")
_ActivityLogEntry_Object = MibTableRow
activityLogEntry = _ActivityLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 5, 1, 1)
)
activityLogEntry.setIndexNames(
    (0, "IMM-MIB", "activityLogIndex"),
)
if mibBuilder.loadTexts:
    activityLogEntry.setStatus("mandatory")


class _ActivityLogIndex_Type(Integer32):
    """Custom type activityLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_ActivityLogIndex_Type.__name__ = "Integer32"
_ActivityLogIndex_Object = MibTableColumn
activityLogIndex = _ActivityLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 5, 1, 1, 1),
    _ActivityLogIndex_Type()
)
activityLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activityLogIndex.setStatus("mandatory")
_ActivityLogString_Type = OctetString
_ActivityLogString_Object = MibTableColumn
activityLogString = _ActivityLogString_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 5, 1, 1, 2),
    _ActivityLogString_Type()
)
activityLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activityLogString.setStatus("mandatory")


class _ActivityLogAcknowledge_Type(Integer32):
    """Custom type activityLogAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ActivityLogAcknowledge_Type.__name__ = "Integer32"
_ActivityLogAcknowledge_Object = MibTableColumn
activityLogAcknowledge = _ActivityLogAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 5, 1, 1, 3),
    _ActivityLogAcknowledge_Type()
)
activityLogAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activityLogAcknowledge.setStatus("mandatory")
_ActivityLogAttribute_Type = OctetString
_ActivityLogAttribute_Object = MibTableColumn
activityLogAttribute = _ActivityLogAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 5, 1, 1, 4),
    _ActivityLogAttribute_Type()
)
activityLogAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activityLogAttribute.setStatus("mandatory")
_AutoFTPSetup_ObjectIdentity = ObjectIdentity
autoFTPSetup = _AutoFTPSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 6)
)


class _AutoFTPCallMode_Type(Integer32):
    """Custom type autoFTPCallMode based on Integer32"""
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
        *(("disabled", 0),
          ("ftp", 1),
          ("sftp", 3),
          ("tftp", 2))
    )


_AutoFTPCallMode_Type.__name__ = "Integer32"
_AutoFTPCallMode_Object = MibScalar
autoFTPCallMode = _AutoFTPCallMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 6, 1),
    _AutoFTPCallMode_Type()
)
autoFTPCallMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFTPCallMode.setStatus("mandatory")


class _AutoFTPCallAddr_Type(OctetString):
    """Custom type autoFTPCallAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AutoFTPCallAddr_Type.__name__ = "OctetString"
_AutoFTPCallAddr_Object = MibScalar
autoFTPCallAddr = _AutoFTPCallAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 6, 2),
    _AutoFTPCallAddr_Type()
)
autoFTPCallAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFTPCallAddr.setStatus("mandatory")
_AutoFTPCallPort_Type = Integer32
_AutoFTPCallPort_Object = MibScalar
autoFTPCallPort = _AutoFTPCallPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 6, 3),
    _AutoFTPCallPort_Type()
)
autoFTPCallPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFTPCallPort.setStatus("mandatory")


class _AutoFTPCallUserID_Type(OctetString):
    """Custom type autoFTPCallUserID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AutoFTPCallUserID_Type.__name__ = "OctetString"
_AutoFTPCallUserID_Object = MibScalar
autoFTPCallUserID = _AutoFTPCallUserID_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 6, 4),
    _AutoFTPCallUserID_Type()
)
autoFTPCallUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFTPCallUserID.setStatus("mandatory")


class _AutoFTPCallPassword_Type(OctetString):
    """Custom type autoFTPCallPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AutoFTPCallPassword_Type.__name__ = "OctetString"
_AutoFTPCallPassword_Object = MibScalar
autoFTPCallPassword = _AutoFTPCallPassword_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 6, 5),
    _AutoFTPCallPassword_Type()
)
autoFTPCallPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFTPCallPassword.setStatus("mandatory")
_CallHomeExclusionEvents_ObjectIdentity = ObjectIdentity
callHomeExclusionEvents = _CallHomeExclusionEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 7)
)
_ReadCallHomeExclusionEventTable_Object = MibTable
readCallHomeExclusionEventTable = _ReadCallHomeExclusionEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 7, 1)
)
if mibBuilder.loadTexts:
    readCallHomeExclusionEventTable.setStatus("mandatory")
_ReadCallHomeExclusionEventEntry_Object = MibTableRow
readCallHomeExclusionEventEntry = _ReadCallHomeExclusionEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 7, 1, 1)
)
readCallHomeExclusionEventEntry.setIndexNames(
    (0, "IMM-MIB", "readCallHomeExclusionEventIndex"),
)
if mibBuilder.loadTexts:
    readCallHomeExclusionEventEntry.setStatus("mandatory")


class _ReadCallHomeExclusionEventIndex_Type(Integer32):
    """Custom type readCallHomeExclusionEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ReadCallHomeExclusionEventIndex_Type.__name__ = "Integer32"
_ReadCallHomeExclusionEventIndex_Object = MibTableColumn
readCallHomeExclusionEventIndex = _ReadCallHomeExclusionEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 7, 1, 1, 1),
    _ReadCallHomeExclusionEventIndex_Type()
)
readCallHomeExclusionEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readCallHomeExclusionEventIndex.setStatus("mandatory")
_ReadCallHomeExclusionEventID_Type = OctetString
_ReadCallHomeExclusionEventID_Object = MibTableColumn
readCallHomeExclusionEventID = _ReadCallHomeExclusionEventID_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 7, 1, 1, 2),
    _ReadCallHomeExclusionEventID_Type()
)
readCallHomeExclusionEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readCallHomeExclusionEventID.setStatus("mandatory")
_AddCallHomeExclusionEvent_Type = OctetString
_AddCallHomeExclusionEvent_Object = MibScalar
addCallHomeExclusionEvent = _AddCallHomeExclusionEvent_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 7, 2),
    _AddCallHomeExclusionEvent_Type()
)
addCallHomeExclusionEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addCallHomeExclusionEvent.setStatus("mandatory")
_RmCallHomeExclusionEvent_Type = OctetString
_RmCallHomeExclusionEvent_Object = MibScalar
rmCallHomeExclusionEvent = _RmCallHomeExclusionEvent_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 7, 3),
    _RmCallHomeExclusionEvent_Type()
)
rmCallHomeExclusionEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmCallHomeExclusionEvent.setStatus("mandatory")


class _RmAllCallHomeExclusionEvent_Type(Integer32):
    """Custom type rmAllCallHomeExclusionEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_RmAllCallHomeExclusionEvent_Type.__name__ = "Integer32"
_RmAllCallHomeExclusionEvent_Object = MibScalar
rmAllCallHomeExclusionEvent = _RmAllCallHomeExclusionEvent_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 7, 4),
    _RmAllCallHomeExclusionEvent_Type()
)
rmAllCallHomeExclusionEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmAllCallHomeExclusionEvent.setStatus("mandatory")
_TestCallHome_ObjectIdentity = ObjectIdentity
testCallHome = _TestCallHome_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 8)
)


class _GenerateTestCallHome_Type(Integer32):
    """Custom type generateTestCallHome based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_GenerateTestCallHome_Type.__name__ = "Integer32"
_GenerateTestCallHome_Object = MibScalar
generateTestCallHome = _GenerateTestCallHome_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 8, 8, 1),
    _GenerateTestCallHome_Type()
)
generateTestCallHome.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    generateTestCallHome.setStatus("mandatory")
_Scaling_ObjectIdentity = ObjectIdentity
scaling = _Scaling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9)
)
_ScalableComplex_ObjectIdentity = ObjectIdentity
scalableComplex = _ScalableComplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 1)
)
_ScalableComplexIdentifier_Type = Integer32
_ScalableComplexIdentifier_Object = MibScalar
scalableComplexIdentifier = _ScalableComplexIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 1, 1),
    _ScalableComplexIdentifier_Type()
)
scalableComplexIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexIdentifier.setStatus("mandatory")
_ScalableComplexNumPartitions_Type = Integer32
_ScalableComplexNumPartitions_Object = MibScalar
scalableComplexNumPartitions = _ScalableComplexNumPartitions_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 1, 2),
    _ScalableComplexNumPartitions_Type()
)
scalableComplexNumPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNumPartitions.setStatus("mandatory")
_ScalableComplexNumNodes_Type = Integer32
_ScalableComplexNumNodes_Object = MibScalar
scalableComplexNumNodes = _ScalableComplexNumNodes_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 1, 3),
    _ScalableComplexNumNodes_Type()
)
scalableComplexNumNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNumNodes.setStatus("mandatory")


class _ScalableComplexClear_Type(Integer32):
    """Custom type scalableComplexClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_ScalableComplexClear_Type.__name__ = "Integer32"
_ScalableComplexClear_Object = MibScalar
scalableComplexClear = _ScalableComplexClear_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 1, 4),
    _ScalableComplexClear_Type()
)
scalableComplexClear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    scalableComplexClear.setStatus("mandatory")
_ScalableComplexPartition_ObjectIdentity = ObjectIdentity
scalableComplexPartition = _ScalableComplexPartition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 2)
)
_ScalableComplexPartitionTable_Object = MibTable
scalableComplexPartitionTable = _ScalableComplexPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 2, 1)
)
if mibBuilder.loadTexts:
    scalableComplexPartitionTable.setStatus("mandatory")
_ScalableComplexPartitionEntry_Object = MibTableRow
scalableComplexPartitionEntry = _ScalableComplexPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 2, 1, 1)
)
scalableComplexPartitionEntry.setIndexNames(
    (0, "IMM-MIB", "scalableComplexPartitionIdentifier"),
)
if mibBuilder.loadTexts:
    scalableComplexPartitionEntry.setStatus("mandatory")


class _ScalableComplexPartitionIdentifier_Type(Integer32):
    """Custom type scalableComplexPartitionIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ScalableComplexPartitionIdentifier_Type.__name__ = "Integer32"
_ScalableComplexPartitionIdentifier_Object = MibTableColumn
scalableComplexPartitionIdentifier = _ScalableComplexPartitionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 2, 1, 1, 1),
    _ScalableComplexPartitionIdentifier_Type()
)
scalableComplexPartitionIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexPartitionIdentifier.setStatus("mandatory")


class _ScalableComplexPartitionMode_Type(Integer32):
    """Custom type scalableComplexPartitionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("partition", 1),
          ("standalone", 2))
    )


_ScalableComplexPartitionMode_Type.__name__ = "Integer32"
_ScalableComplexPartitionMode_Object = MibTableColumn
scalableComplexPartitionMode = _ScalableComplexPartitionMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 2, 1, 1, 2),
    _ScalableComplexPartitionMode_Type()
)
scalableComplexPartitionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scalableComplexPartitionMode.setStatus("mandatory")


class _ScalableComplexPartitionPriNodeKey_Type(OctetString):
    """Custom type scalableComplexPartitionPriNodeKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ScalableComplexPartitionPriNodeKey_Type.__name__ = "OctetString"
_ScalableComplexPartitionPriNodeKey_Object = MibTableColumn
scalableComplexPartitionPriNodeKey = _ScalableComplexPartitionPriNodeKey_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 2, 1, 1, 3),
    _ScalableComplexPartitionPriNodeKey_Type()
)
scalableComplexPartitionPriNodeKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexPartitionPriNodeKey.setStatus("mandatory")
_ScalableComplexPartitionNumNodes_Type = Integer32
_ScalableComplexPartitionNumNodes_Object = MibTableColumn
scalableComplexPartitionNumNodes = _ScalableComplexPartitionNumNodes_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 2, 1, 1, 4),
    _ScalableComplexPartitionNumNodes_Type()
)
scalableComplexPartitionNumNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexPartitionNumNodes.setStatus("mandatory")


class _ScalableComplexPartitionStatus_Type(Integer32):
    """Custom type scalableComplexPartitionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("poweredoff", 1),
          ("poweredon", 2))
    )


_ScalableComplexPartitionStatus_Type.__name__ = "Integer32"
_ScalableComplexPartitionStatus_Object = MibTableColumn
scalableComplexPartitionStatus = _ScalableComplexPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 2, 1, 1, 5),
    _ScalableComplexPartitionStatus_Type()
)
scalableComplexPartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexPartitionStatus.setStatus("mandatory")


class _ScalableComplexPartitionSelect_Type(OctetString):
    """Custom type scalableComplexPartitionSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ScalableComplexPartitionSelect_Type.__name__ = "OctetString"
_ScalableComplexPartitionSelect_Object = MibScalar
scalableComplexPartitionSelect = _ScalableComplexPartitionSelect_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 2, 2),
    _ScalableComplexPartitionSelect_Type()
)
scalableComplexPartitionSelect.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    scalableComplexPartitionSelect.setStatus("mandatory")


class _ScalableComplexPartitionAction_Type(Integer32):
    """Custom type scalableComplexPartitionAction based on Integer32"""
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
        *(("delete", 1),
          ("powercycle", 4),
          ("poweroff", 3),
          ("poweron", 2))
    )


_ScalableComplexPartitionAction_Type.__name__ = "Integer32"
_ScalableComplexPartitionAction_Object = MibScalar
scalableComplexPartitionAction = _ScalableComplexPartitionAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 2, 3),
    _ScalableComplexPartitionAction_Type()
)
scalableComplexPartitionAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    scalableComplexPartitionAction.setStatus("mandatory")
_ScalableComplexPartitionCreate_ObjectIdentity = ObjectIdentity
scalableComplexPartitionCreate = _ScalableComplexPartitionCreate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 3)
)
_ScalableComplexPartitionCreateTable_Object = MibTable
scalableComplexPartitionCreateTable = _ScalableComplexPartitionCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 3, 1)
)
if mibBuilder.loadTexts:
    scalableComplexPartitionCreateTable.setStatus("mandatory")
_ScalableComplexPartitionCreateEntry_Object = MibTableRow
scalableComplexPartitionCreateEntry = _ScalableComplexPartitionCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 3, 1, 1)
)
scalableComplexPartitionCreateEntry.setIndexNames(
    (0, "IMM-MIB", "scalableComplexPartitionCreateIndex"),
)
if mibBuilder.loadTexts:
    scalableComplexPartitionCreateEntry.setStatus("mandatory")


class _ScalableComplexPartitionCreateIndex_Type(Integer32):
    """Custom type scalableComplexPartitionCreateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ScalableComplexPartitionCreateIndex_Type.__name__ = "Integer32"
_ScalableComplexPartitionCreateIndex_Object = MibTableColumn
scalableComplexPartitionCreateIndex = _ScalableComplexPartitionCreateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 3, 1, 1, 1),
    _ScalableComplexPartitionCreateIndex_Type()
)
scalableComplexPartitionCreateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexPartitionCreateIndex.setStatus("mandatory")


class _ScalableComplexPartitionCreateNodeKey_Type(OctetString):
    """Custom type scalableComplexPartitionCreateNodeKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ScalableComplexPartitionCreateNodeKey_Type.__name__ = "OctetString"
_ScalableComplexPartitionCreateNodeKey_Object = MibTableColumn
scalableComplexPartitionCreateNodeKey = _ScalableComplexPartitionCreateNodeKey_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 3, 1, 1, 2),
    _ScalableComplexPartitionCreateNodeKey_Type()
)
scalableComplexPartitionCreateNodeKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scalableComplexPartitionCreateNodeKey.setStatus("mandatory")


class _ScalableComplexPartitionActionCreate_Type(Integer32):
    """Custom type scalableComplexPartitionActionCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("create", 1))
    )


_ScalableComplexPartitionActionCreate_Type.__name__ = "Integer32"
_ScalableComplexPartitionActionCreate_Object = MibScalar
scalableComplexPartitionActionCreate = _ScalableComplexPartitionActionCreate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 3, 2),
    _ScalableComplexPartitionActionCreate_Type()
)
scalableComplexPartitionActionCreate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    scalableComplexPartitionActionCreate.setStatus("mandatory")
_ScalableComplexNode_ObjectIdentity = ObjectIdentity
scalableComplexNode = _ScalableComplexNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4)
)
_ScalableComplexNodeTable_Object = MibTable
scalableComplexNodeTable = _ScalableComplexNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 1)
)
if mibBuilder.loadTexts:
    scalableComplexNodeTable.setStatus("mandatory")
_ScalableComplexNodeEntry_Object = MibTableRow
scalableComplexNodeEntry = _ScalableComplexNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 1, 1)
)
scalableComplexNodeEntry.setIndexNames(
    (0, "IMM-MIB", "scalableComplexNodeIndex"),
)
if mibBuilder.loadTexts:
    scalableComplexNodeEntry.setStatus("mandatory")


class _ScalableComplexNodeIndex_Type(Integer32):
    """Custom type scalableComplexNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ScalableComplexNodeIndex_Type.__name__ = "Integer32"
_ScalableComplexNodeIndex_Object = MibTableColumn
scalableComplexNodeIndex = _ScalableComplexNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 1, 1, 1),
    _ScalableComplexNodeIndex_Type()
)
scalableComplexNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodeIndex.setStatus("mandatory")


class _ScalableComplexNodeSerialNumber_Type(OctetString):
    """Custom type scalableComplexNodeSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ScalableComplexNodeSerialNumber_Type.__name__ = "OctetString"
_ScalableComplexNodeSerialNumber_Object = MibTableColumn
scalableComplexNodeSerialNumber = _ScalableComplexNodeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 1, 1, 2),
    _ScalableComplexNodeSerialNumber_Type()
)
scalableComplexNodeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodeSerialNumber.setStatus("mandatory")


class _ScalableComplexNodeKey_Type(OctetString):
    """Custom type scalableComplexNodeKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ScalableComplexNodeKey_Type.__name__ = "OctetString"
_ScalableComplexNodeKey_Object = MibTableColumn
scalableComplexNodeKey = _ScalableComplexNodeKey_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 1, 1, 3),
    _ScalableComplexNodeKey_Type()
)
scalableComplexNodeKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodeKey.setStatus("mandatory")
_ScalableComplexNodePartitionID_Type = Integer32
_ScalableComplexNodePartitionID_Object = MibTableColumn
scalableComplexNodePartitionID = _ScalableComplexNodePartitionID_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 1, 1, 4),
    _ScalableComplexNodePartitionID_Type()
)
scalableComplexNodePartitionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodePartitionID.setStatus("mandatory")


class _ScalableComplexNodeRole_Type(Integer32):
    """Custom type scalableComplexNodeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("unassigned", 255))
    )


_ScalableComplexNodeRole_Type.__name__ = "Integer32"
_ScalableComplexNodeRole_Object = MibTableColumn
scalableComplexNodeRole = _ScalableComplexNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 1, 1, 5),
    _ScalableComplexNodeRole_Type()
)
scalableComplexNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodeRole.setStatus("mandatory")
_ScalableComplexNodeNumPorts_Type = Integer32
_ScalableComplexNodeNumPorts_Object = MibTableColumn
scalableComplexNodeNumPorts = _ScalableComplexNodeNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 1, 1, 6),
    _ScalableComplexNodeNumPorts_Type()
)
scalableComplexNodeNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodeNumPorts.setStatus("mandatory")


class _ScalableComplexNodeSelect_Type(OctetString):
    """Custom type scalableComplexNodeSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ScalableComplexNodeSelect_Type.__name__ = "OctetString"
_ScalableComplexNodeSelect_Object = MibScalar
scalableComplexNodeSelect = _ScalableComplexNodeSelect_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 2),
    _ScalableComplexNodeSelect_Type()
)
scalableComplexNodeSelect.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    scalableComplexNodeSelect.setStatus("mandatory")


class _ScalableComplexNodeAction_Type(Integer32):
    """Custom type scalableComplexNodeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("poweroff", 1),
          ("poweron", 2))
    )


_ScalableComplexNodeAction_Type.__name__ = "Integer32"
_ScalableComplexNodeAction_Object = MibScalar
scalableComplexNodeAction = _ScalableComplexNodeAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 3),
    _ScalableComplexNodeAction_Type()
)
scalableComplexNodeAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    scalableComplexNodeAction.setStatus("mandatory")


class _ScalableComplexNodeAutoCreate_Type(Integer32):
    """Custom type scalableComplexNodeAutoCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("execute", 1)
    )


_ScalableComplexNodeAutoCreate_Type.__name__ = "Integer32"
_ScalableComplexNodeAutoCreate_Object = MibScalar
scalableComplexNodeAutoCreate = _ScalableComplexNodeAutoCreate_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 4, 4),
    _ScalableComplexNodeAutoCreate_Type()
)
scalableComplexNodeAutoCreate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    scalableComplexNodeAutoCreate.setStatus("mandatory")
_ScalableComplexNodePort_ObjectIdentity = ObjectIdentity
scalableComplexNodePort = _ScalableComplexNodePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 5)
)
_ScalableComplexNodePortTable_Object = MibTable
scalableComplexNodePortTable = _ScalableComplexNodePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 5, 1)
)
if mibBuilder.loadTexts:
    scalableComplexNodePortTable.setStatus("mandatory")
_ScalableComplexNodePortEntry_Object = MibTableRow
scalableComplexNodePortEntry = _ScalableComplexNodePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 5, 1, 1)
)
scalableComplexNodePortEntry.setIndexNames(
    (0, "IMM-MIB", "scalableComplexNodePortIndex"),
    (0, "IMM-MIB", "scalableComplexNodePortNum"),
)
if mibBuilder.loadTexts:
    scalableComplexNodePortEntry.setStatus("mandatory")


class _ScalableComplexNodePortIndex_Type(Integer32):
    """Custom type scalableComplexNodePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ScalableComplexNodePortIndex_Type.__name__ = "Integer32"
_ScalableComplexNodePortIndex_Object = MibTableColumn
scalableComplexNodePortIndex = _ScalableComplexNodePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 5, 1, 1, 1),
    _ScalableComplexNodePortIndex_Type()
)
scalableComplexNodePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodePortIndex.setStatus("mandatory")


class _ScalableComplexNodePortNum_Type(Integer32):
    """Custom type scalableComplexNodePortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ScalableComplexNodePortNum_Type.__name__ = "Integer32"
_ScalableComplexNodePortNum_Object = MibTableColumn
scalableComplexNodePortNum = _ScalableComplexNodePortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 5, 1, 1, 2),
    _ScalableComplexNodePortNum_Type()
)
scalableComplexNodePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodePortNum.setStatus("mandatory")


class _ScalableComplexNodePortRemNodeKey_Type(OctetString):
    """Custom type scalableComplexNodePortRemNodeKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ScalableComplexNodePortRemNodeKey_Type.__name__ = "OctetString"
_ScalableComplexNodePortRemNodeKey_Object = MibTableColumn
scalableComplexNodePortRemNodeKey = _ScalableComplexNodePortRemNodeKey_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 5, 1, 1, 3),
    _ScalableComplexNodePortRemNodeKey_Type()
)
scalableComplexNodePortRemNodeKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodePortRemNodeKey.setStatus("mandatory")
_ScalableComplexNodePortRemNum_Type = Integer32
_ScalableComplexNodePortRemNum_Object = MibTableColumn
scalableComplexNodePortRemNum = _ScalableComplexNodePortRemNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 5, 1, 1, 4),
    _ScalableComplexNodePortRemNum_Type()
)
scalableComplexNodePortRemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodePortRemNum.setStatus("mandatory")


class _ScalableComplexNodePortStatus_Type(Integer32):
    """Custom type scalableComplexNodePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("unknown", 255))
    )


_ScalableComplexNodePortStatus_Type.__name__ = "Integer32"
_ScalableComplexNodePortStatus_Object = MibTableColumn
scalableComplexNodePortStatus = _ScalableComplexNodePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 5, 1, 1, 5),
    _ScalableComplexNodePortStatus_Type()
)
scalableComplexNodePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodePortStatus.setStatus("mandatory")


class _ScalableComplexNodePortType_Type(Integer32):
    """Custom type scalableComplexNodePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("exa", 2),
          ("qpi", 1),
          ("unknown", 255))
    )


_ScalableComplexNodePortType_Type.__name__ = "Integer32"
_ScalableComplexNodePortType_Object = MibTableColumn
scalableComplexNodePortType = _ScalableComplexNodePortType_Object(
    (1, 3, 6, 1, 4, 1, 2, 3, 51, 3, 9, 5, 1, 1, 6),
    _ScalableComplexNodePortType_Type()
)
scalableComplexNodePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scalableComplexNodePortType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IMM-MIB",
    **{"InetAddressIPv6": InetAddressIPv6,
       "EntryStatus": EntryStatus,
       "ibm": ibm,
       "ibmAgents": ibmAgents,
       "netfinitySupportProcessorAgent": netfinitySupportProcessorAgent,
       "ibmIntegratedManagementModuleMIB": ibmIntegratedManagementModuleMIB,
       "monitors": monitors,
       "temperature": temperature,
       "tempNumber": tempNumber,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempDescr": tempDescr,
       "tempReading": tempReading,
       "tempNominalReading": tempNominalReading,
       "tempNonRecovLimitHigh": tempNonRecovLimitHigh,
       "tempCritLimitHigh": tempCritLimitHigh,
       "tempNonCritLimitHigh": tempNonCritLimitHigh,
       "tempNonRecovLimitLow": tempNonRecovLimitLow,
       "tempCritLimitLow": tempCritLimitLow,
       "tempNonCritLimitLow": tempNonCritLimitLow,
       "tempHealthStatus": tempHealthStatus,
       "voltage": voltage,
       "voltNumber": voltNumber,
       "voltTable": voltTable,
       "voltEntry": voltEntry,
       "voltIndex": voltIndex,
       "voltDescr": voltDescr,
       "voltReading": voltReading,
       "voltNominalReading": voltNominalReading,
       "voltNonRecovLimitHigh": voltNonRecovLimitHigh,
       "voltCritLimitHigh": voltCritLimitHigh,
       "voltNonCritLimitHigh": voltNonCritLimitHigh,
       "voltNonRecovLimitLow": voltNonRecovLimitLow,
       "voltCritLimitLow": voltCritLimitLow,
       "voltNonCritLimitLow": voltNonCritLimitLow,
       "voltHealthStatus": voltHealthStatus,
       "fans": fans,
       "fanNumber": fanNumber,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanDescr": fanDescr,
       "fanSpeed": fanSpeed,
       "fanNonRecovLimitHigh": fanNonRecovLimitHigh,
       "fanCritLimitHigh": fanCritLimitHigh,
       "fanNonCritLimitHigh": fanNonCritLimitHigh,
       "fanNonRecovLimitLow": fanNonRecovLimitLow,
       "fanCritLimitLow": fanCritLimitLow,
       "fanNonCritLimitLow": fanNonCritLimitLow,
       "fanHealthStatus": fanHealthStatus,
       "systemHealth": systemHealth,
       "systemHealthStat": systemHealthStat,
       "systemHealthSummaryTable": systemHealthSummaryTable,
       "systemHealthSummaryEntry": systemHealthSummaryEntry,
       "systemHealthSummaryIndex": systemHealthSummaryIndex,
       "systemHealthSummarySeverity": systemHealthSummarySeverity,
       "systemHealthSummaryDescription": systemHealthSummaryDescription,
       "vpdInformation": vpdInformation,
       "immVpdTable": immVpdTable,
       "immVpdEntry": immVpdEntry,
       "immVpdIndex": immVpdIndex,
       "immVpdType": immVpdType,
       "immVpdVersionString": immVpdVersionString,
       "immVpdReleaseDate": immVpdReleaseDate,
       "machineVpd": machineVpd,
       "machineLevelVpd": machineLevelVpd,
       "machineLevelVpdMachineType": machineLevelVpdMachineType,
       "machineLevelVpdMachineModel": machineLevelVpdMachineModel,
       "machineLevelSerialNumber": machineLevelSerialNumber,
       "machineLevelUUID": machineLevelUUID,
       "machineLevelProductName": machineLevelProductName,
       "systemComponentLevelVpdTable": systemComponentLevelVpdTable,
       "systemComponentLevelVpdEntry": systemComponentLevelVpdEntry,
       "componentLevelVpdIndex": componentLevelVpdIndex,
       "componentLevelVpdFruNumber": componentLevelVpdFruNumber,
       "componentLevelVpdFruName": componentLevelVpdFruName,
       "componentLevelVpdSerialNumber": componentLevelVpdSerialNumber,
       "componentLevelVpdManufacturingId": componentLevelVpdManufacturingId,
       "systemComponentLevelVpdTrackingTable": systemComponentLevelVpdTrackingTable,
       "systemComponentLevelVpdTrackingEntry": systemComponentLevelVpdTrackingEntry,
       "componentLevelVpdTrackingIndex": componentLevelVpdTrackingIndex,
       "componentLevelVpdTrackingFruNumber": componentLevelVpdTrackingFruNumber,
       "componentLevelVpdTrackingFruName": componentLevelVpdTrackingFruName,
       "componentLevelVpdTrackingSerialNumber": componentLevelVpdTrackingSerialNumber,
       "componentLevelVpdTrackingManufacturingId": componentLevelVpdTrackingManufacturingId,
       "componentLevelVpdTrackingAction": componentLevelVpdTrackingAction,
       "componentLevelVpdTrackingTimestamp": componentLevelVpdTrackingTimestamp,
       "hostMACAddressTable": hostMACAddressTable,
       "hostMACAddressEntry": hostMACAddressEntry,
       "hostMACAddressIndex": hostMACAddressIndex,
       "hostMACAddressDescription": hostMACAddressDescription,
       "hostMACAddress": hostMACAddress,
       "systemCPUVpdTable": systemCPUVpdTable,
       "systemCPUVpdEntry": systemCPUVpdEntry,
       "cpuVpdIndex": cpuVpdIndex,
       "cpuVpdDescription": cpuVpdDescription,
       "cpuVpdSpeed": cpuVpdSpeed,
       "cpuVpdIdentifier": cpuVpdIdentifier,
       "cpuVpdType": cpuVpdType,
       "cpuVpdFamily": cpuVpdFamily,
       "cpuVpdCores": cpuVpdCores,
       "cpuVpdThreads": cpuVpdThreads,
       "cpuVpdVoltage": cpuVpdVoltage,
       "cpuVpdDataWidth": cpuVpdDataWidth,
       "cpuVpdHealthStatus": cpuVpdHealthStatus,
       "systemMemoryVpdTable": systemMemoryVpdTable,
       "systemMemoryVpdEntry": systemMemoryVpdEntry,
       "memoryVpdIndex": memoryVpdIndex,
       "memoryVpdDescription": memoryVpdDescription,
       "memoryVpdPartNumber": memoryVpdPartNumber,
       "memoryVpdFRUSerialNumber": memoryVpdFRUSerialNumber,
       "memoryVpdManufactureDate": memoryVpdManufactureDate,
       "memoryVpdType": memoryVpdType,
       "memoryVpdSize": memoryVpdSize,
       "memoryHealthStatus": memoryHealthStatus,
       "users": users,
       "immUsers": immUsers,
       "currentlyLoggedInTable": currentlyLoggedInTable,
       "currentlyLoggedInEntry": currentlyLoggedInEntry,
       "currentlyLoggedInEntryIndex": currentlyLoggedInEntryIndex,
       "currentlyLoggedInEntryUserId": currentlyLoggedInEntryUserId,
       "currentlyLoggedInEntryAccMethod": currentlyLoggedInEntryAccMethod,
       "leds": leds,
       "identityLED": identityLED,
       "allLEDsTable": allLEDsTable,
       "allLEDsEntry": allLEDsEntry,
       "ledIndex": ledIndex,
       "ledIdentifier": ledIdentifier,
       "ledLabel": ledLabel,
       "ledState": ledState,
       "ledColor": ledColor,
       "informationLED": informationLED,
       "osFailureCapture": osFailureCapture,
       "osFailureCaptureTftpServer": osFailureCaptureTftpServer,
       "osFailureCaptureFileName": osFailureCaptureFileName,
       "osFailureCaptureSaveStart": osFailureCaptureSaveStart,
       "osFailureCaptureSaveStatus": osFailureCaptureSaveStatus,
       "fuelGauge": fuelGauge,
       "fuelGaugeInformation": fuelGaugeInformation,
       "fuelGaugePowerCappingPolicySetting": fuelGaugePowerCappingPolicySetting,
       "fuelGaugeStaticPowerPcapSoftMin": fuelGaugeStaticPowerPcapSoftMin,
       "fuelGaugeStaticPowerPcapMin": fuelGaugeStaticPowerPcapMin,
       "fuelGaugeStaticPowerPcapCurrentSetting": fuelGaugeStaticPowerPcapCurrentSetting,
       "fuelGaugeStaticPowerPcapMax": fuelGaugeStaticPowerPcapMax,
       "fuelGaugeStaticPowerPcapMode": fuelGaugeStaticPowerPcapMode,
       "fuelGaugeSystemMaxPower": fuelGaugeSystemMaxPower,
       "fuelGaugePowerRemaining": fuelGaugePowerRemaining,
       "fuelGaugeTotalPowerAvaialble": fuelGaugeTotalPowerAvaialble,
       "fuelGaugeTotalPowerInUse": fuelGaugeTotalPowerInUse,
       "fuelGaugeTotalThermalOutput": fuelGaugeTotalThermalOutput,
       "fuelGaugePowerConsumptionCpu": fuelGaugePowerConsumptionCpu,
       "fuelGaugePowerConsumptionMemory": fuelGaugePowerConsumptionMemory,
       "fuelGaugePowerConsumptionOther": fuelGaugePowerConsumptionOther,
       "powerPolicyInformation": powerPolicyInformation,
       "powerPolicyTable": powerPolicyTable,
       "powerPolicyEntry": powerPolicyEntry,
       "powerPolicyIndex": powerPolicyIndex,
       "powerPolicyName": powerPolicyName,
       "powerPolicyPwrSupplyFailureLimit": powerPolicyPwrSupplyFailureLimit,
       "powerPolicyMaxPowerLimit": powerPolicyMaxPowerLimit,
       "powerPolicyEstimatedUtilization": powerPolicyEstimatedUtilization,
       "powerPolicyActivate": powerPolicyActivate,
       "powerPowerTrending": powerPowerTrending,
       "powerTrendingPeriod": powerTrendingPeriod,
       "powerTrendingPowerType": powerTrendingPowerType,
       "powerTrendingSampleTable": powerTrendingSampleTable,
       "powerTrendingSampleEntry": powerTrendingSampleEntry,
       "powerTrendingSampleIndex": powerTrendingSampleIndex,
       "powerTrendingSampleTimeStamp": powerTrendingSampleTimeStamp,
       "powerTrendingSampleAve": powerTrendingSampleAve,
       "powerTrendingSampleMin": powerTrendingSampleMin,
       "powerTrendingSampleMax": powerTrendingSampleMax,
       "powerModule": powerModule,
       "powerNumber": powerNumber,
       "powerTable": powerTable,
       "powerEntry": powerEntry,
       "powerIndex": powerIndex,
       "powerFruName": powerFruName,
       "powerPartNumber": powerPartNumber,
       "powerFRUNumber": powerFRUNumber,
       "powerFRUSerialNumber": powerFRUSerialNumber,
       "powerHealthStatus": powerHealthStatus,
       "disks": disks,
       "diskNumber": diskNumber,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskIndex": diskIndex,
       "diskFruName": diskFruName,
       "diskHealthStatus": diskHealthStatus,
       "errorLogs": errorLogs,
       "eventLog": eventLog,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogIndex": eventLogIndex,
       "eventLogString": eventLogString,
       "eventLogSeverity": eventLogSeverity,
       "eventLogDate": eventLogDate,
       "eventLogTime": eventLogTime,
       "eventLogClr": eventLogClr,
       "eventLogTftpServer": eventLogTftpServer,
       "eventLogFileName": eventLogFileName,
       "eventLogSaveStart": eventLogSaveStart,
       "eventLogSaveStatus": eventLogSaveStatus,
       "configureSP": configureSP,
       "remoteAccessConfig": remoteAccessConfig,
       "generalRemoteCfg": generalRemoteCfg,
       "remoteAlertRetryDelay": remoteAlertRetryDelay,
       "remoteAlertRetryCount": remoteAlertRetryCount,
       "remoteAlertEntryDelay": remoteAlertEntryDelay,
       "snmpCriticalAlerts": snmpCriticalAlerts,
       "snmpWarningAlerts": snmpWarningAlerts,
       "snmpSystemAlerts": snmpSystemAlerts,
       "remoteAccessTamperDelay": remoteAccessTamperDelay,
       "userAuthenticationMethod": userAuthenticationMethod,
       "webInactivityTimeout": webInactivityTimeout,
       "snmpAlertFilters": snmpAlertFilters,
       "safSpTrapTempC": safSpTrapTempC,
       "safSpTrapVoltC": safSpTrapVoltC,
       "safSpTrapPowerC": safSpTrapPowerC,
       "safSpTrapHdC": safSpTrapHdC,
       "safSpTrapFanC": safSpTrapFanC,
       "safSpTrapIhcC": safSpTrapIhcC,
       "safSpTrapCPUC": safSpTrapCPUC,
       "safSpTrapMemoryC": safSpTrapMemoryC,
       "safSpTrapRdpsC": safSpTrapRdpsC,
       "safSpTrapHardwareC": safSpTrapHardwareC,
       "safSpTrapRdpsN": safSpTrapRdpsN,
       "safSpTrapTempN": safSpTrapTempN,
       "safSpTrapVoltN": safSpTrapVoltN,
       "safSpTrapPowerN": safSpTrapPowerN,
       "safSpTrapFanN": safSpTrapFanN,
       "safSpTrapCPUN": safSpTrapCPUN,
       "safSpTrapMemoryN": safSpTrapMemoryN,
       "safSpTrapHardwareN": safSpTrapHardwareN,
       "safSpTrapRLogin": safSpTrapRLogin,
       "safSpTrapOsToS": safSpTrapOsToS,
       "safSpTrapAppS": safSpTrapAppS,
       "safSpTrapPowerS": safSpTrapPowerS,
       "safSpTrapBootS": safSpTrapBootS,
       "safSpTrapLdrToS": safSpTrapLdrToS,
       "safSpTrapPFAS": safSpTrapPFAS,
       "safSpTrapSysLogS": safSpTrapSysLogS,
       "safSpTrapNwChangeS": safSpTrapNwChangeS,
       "customSecuritySettings": customSecuritySettings,
       "loginPasswordRequired": loginPasswordRequired,
       "passwordExpirationPeriod": passwordExpirationPeriod,
       "minimumPasswordReuseCycle": minimumPasswordReuseCycle,
       "complexPasswordRulesEnforced": complexPasswordRulesEnforced,
       "minimumPasswordLength": minimumPasswordLength,
       "defaultAdminPasswordExpired": defaultAdminPasswordExpired,
       "minimumDiffCharsPassword": minimumDiffCharsPassword,
       "changePasswordFirstAccess": changePasswordFirstAccess,
       "accountLockoutPeriod": accountLockoutPeriod,
       "maxLoginFailures": maxLoginFailures,
       "passwordChangeInterval": passwordChangeInterval,
       "serialPortCfg": serialPortCfg,
       "portBaud": portBaud,
       "portParity": portParity,
       "serialRedirect": serialRedirect,
       "enterCLIkeySeq": enterCLIkeySeq,
       "portStopBits": portStopBits,
       "portCLImode": portCLImode,
       "remoteAlertIds": remoteAlertIds,
       "remoteAlertIdsTable": remoteAlertIdsTable,
       "remoteAlertIdsEntry": remoteAlertIdsEntry,
       "remoteAlertIdEntryIndex": remoteAlertIdEntryIndex,
       "remoteAlertIdEntryStatus": remoteAlertIdEntryStatus,
       "remoteAlertIdEntryName": remoteAlertIdEntryName,
       "remoteAlertIdEmailAddr": remoteAlertIdEmailAddr,
       "remoteAlertIdEntryCriticalAlert": remoteAlertIdEntryCriticalAlert,
       "remoteAlertIdEntryWarningAlert": remoteAlertIdEntryWarningAlert,
       "remoteAlertIdEntrySystemAlert": remoteAlertIdEntrySystemAlert,
       "remoteAlertIdEntryAttachmentsToEmailAlerts": remoteAlertIdEntryAttachmentsToEmailAlerts,
       "remoteAlertIdEntrySyslogPortAssignment": remoteAlertIdEntrySyslogPortAssignment,
       "remoteAlertIdEntrySyslogHostname": remoteAlertIdEntrySyslogHostname,
       "remoteAlertIdEntryType": remoteAlertIdEntryType,
       "remoteAlertFiltersTable": remoteAlertFiltersTable,
       "remoteAlertFiltersEntry": remoteAlertFiltersEntry,
       "rafIndex": rafIndex,
       "rafSpTrapTempC": rafSpTrapTempC,
       "rafSpTrapVoltC": rafSpTrapVoltC,
       "rafSpTrapPowerC": rafSpTrapPowerC,
       "rafSpTrapHdC": rafSpTrapHdC,
       "rafSpTrapFanC": rafSpTrapFanC,
       "rafSpTrapIhcC": rafSpTrapIhcC,
       "rafSpTrapCPUC": rafSpTrapCPUC,
       "rafSpTrapMemoryC": rafSpTrapMemoryC,
       "rafSpTrapRdpsC": rafSpTrapRdpsC,
       "rafSpTrapHardwareC": rafSpTrapHardwareC,
       "rafSpTrapRdpsN": rafSpTrapRdpsN,
       "rafSpTrapTempN": rafSpTrapTempN,
       "rafSpTrapVoltN": rafSpTrapVoltN,
       "rafSpTrapPowerN": rafSpTrapPowerN,
       "rafSpTrapFanN": rafSpTrapFanN,
       "rafSpTrapCPUN": rafSpTrapCPUN,
       "rafSpTrapMemoryN": rafSpTrapMemoryN,
       "rafSpTrapHardwareN": rafSpTrapHardwareN,
       "rafSpTrapRLogin": rafSpTrapRLogin,
       "rafSpTrapOsToS": rafSpTrapOsToS,
       "rafSpTrapAppS": rafSpTrapAppS,
       "rafSpTrapPowerS": rafSpTrapPowerS,
       "rafSpTrapBootS": rafSpTrapBootS,
       "rafSpTrapLdrToS": rafSpTrapLdrToS,
       "rafSpTrapPFAS": rafSpTrapPFAS,
       "rafSpTrapSysLogS": rafSpTrapSysLogS,
       "rafSpTrapNwChangeS": rafSpTrapNwChangeS,
       "generateTestAlert": generateTestAlert,
       "remoteAccessIds": remoteAccessIds,
       "remoteAccessIdsTable": remoteAccessIdsTable,
       "remoteAccessIdsEntry": remoteAccessIdsEntry,
       "remoteAccessIdEntryIndex": remoteAccessIdEntryIndex,
       "remoteAccessIdEntryUserId": remoteAccessIdEntryUserId,
       "remoteAccessIdEntryPassword": remoteAccessIdEntryPassword,
       "remoteAccessIdEntryUserPwdLeftDays": remoteAccessIdEntryUserPwdLeftDays,
       "remoteAccessUserAuthorityLevelTable": remoteAccessUserAuthorityLevelTable,
       "remoteAccessUserAuthorityLevelEntry": remoteAccessUserAuthorityLevelEntry,
       "ualIndex": ualIndex,
       "ualId": ualId,
       "ualSupervisor": ualSupervisor,
       "ualReadOnly": ualReadOnly,
       "ualAccountManagement": ualAccountManagement,
       "ualConsoleAccess": ualConsoleAccess,
       "ualConsoleAndVirtualMediaAccess": ualConsoleAndVirtualMediaAccess,
       "ualServerPowerAccess": ualServerPowerAccess,
       "ualAllowClearLog": ualAllowClearLog,
       "ualAdapterBasicConfig": ualAdapterBasicConfig,
       "ualAdapterNetworkAndSecurityConfig": ualAdapterNetworkAndSecurityConfig,
       "ualAdapterAdvancedConfig": ualAdapterAdvancedConfig,
       "groupProfiles": groupProfiles,
       "groupIdsTable": groupIdsTable,
       "groupIdsEntry": groupIdsEntry,
       "groupIndex": groupIndex,
       "groupId": groupId,
       "groupRole": groupRole,
       "groupRBSroleTable": groupRBSroleTable,
       "groupRBSroleEntry": groupRBSroleEntry,
       "groupRBSroleIndex": groupRBSroleIndex,
       "groupRBSroleId": groupRBSroleId,
       "groupRBSSupervisor": groupRBSSupervisor,
       "groupRBSOperator": groupRBSOperator,
       "groupRBSNetworkSecurity": groupRBSNetworkSecurity,
       "groupRBSUserAccountManagement": groupRBSUserAccountManagement,
       "groupRBSRemoteConsoleAccess": groupRBSRemoteConsoleAccess,
       "groupRBSRemoteConsoleRemoteDiskAccess": groupRBSRemoteConsoleRemoteDiskAccess,
       "groupRBSServerPowerRestartAccess": groupRBSServerPowerRestartAccess,
       "groupRBSBasicAdapterConfiguration": groupRBSBasicAdapterConfiguration,
       "groupRBSClearEventLog": groupRBSClearEventLog,
       "groupRBSAdvancedAdapterConfiguration": groupRBSAdvancedAdapterConfiguration,
       "sshClientAuth": sshClientAuth,
       "sshClientAuthPubKeyTable": sshClientAuthPubKeyTable,
       "sshClientAuthPubKeyEntry": sshClientAuthPubKeyEntry,
       "sshClientAuthRemoteAccessIdIndex": sshClientAuthRemoteAccessIdIndex,
       "sshClientAuthPubKeyIndex": sshClientAuthPubKeyIndex,
       "sshClientAuthPubKeyType": sshClientAuthPubKeyType,
       "sshClientAuthPubKeySize": sshClientAuthPubKeySize,
       "sshClientAuthPubKeyFingerprint": sshClientAuthPubKeyFingerprint,
       "sshClientAuthPubKeyAcceptFrom": sshClientAuthPubKeyAcceptFrom,
       "sshClientAuthPubKeyComment": sshClientAuthPubKeyComment,
       "sshClientAuthPubKeyAction": sshClientAuthPubKeyAction,
       "sshClientAuthPubKeyEntryStatus": sshClientAuthPubKeyEntryStatus,
       "sshClientAuthPubKeyUnused": sshClientAuthPubKeyUnused,
       "sshClientAuthPubKeyTftpServer": sshClientAuthPubKeyTftpServer,
       "sshClientAuthPubKeyFileName": sshClientAuthPubKeyFileName,
       "sshClientAuthPubKeyFileFormat": sshClientAuthPubKeyFileFormat,
       "spClock": spClock,
       "spClockDateAndTimeSetting": spClockDateAndTimeSetting,
       "spClockTimezoneSetting": spClockTimezoneSetting,
       "spIdentification": spIdentification,
       "spTxtId": spTxtId,
       "spRoomID": spRoomID,
       "spRackID": spRackID,
       "spRackUnitPosition": spRackUnitPosition,
       "spRackUnitHeight": spRackUnitHeight,
       "spRackBladeBay": spRackBladeBay,
       "networkConfiguration": networkConfiguration,
       "networkInterfaces": networkInterfaces,
       "ethernetInterface": ethernetInterface,
       "ethernetInterfaceType": ethernetInterfaceType,
       "ethernetInterfaceEnabled": ethernetInterfaceEnabled,
       "ethernetInterfaceHostName": ethernetInterfaceHostName,
       "ethernetInterfaceIPAddress": ethernetInterfaceIPAddress,
       "ethernetInterfaceAutoNegotiate": ethernetInterfaceAutoNegotiate,
       "ethernetInterfaceDataRate": ethernetInterfaceDataRate,
       "ethernetInterfaceDuplexSetting": ethernetInterfaceDuplexSetting,
       "ethernetInterfaceLAA": ethernetInterfaceLAA,
       "ethernetInterfaceDhcpEnabled": ethernetInterfaceDhcpEnabled,
       "ethernetInterfaceGatewayIPAddress": ethernetInterfaceGatewayIPAddress,
       "ethernetInterfaceBIA": ethernetInterfaceBIA,
       "ethernetInterfaceMTU": ethernetInterfaceMTU,
       "ethernetInterfaceSubnetMask": ethernetInterfaceSubnetMask,
       "dhcpEthernetInterface": dhcpEthernetInterface,
       "dhcpHostName": dhcpHostName,
       "dhcpIPAddress": dhcpIPAddress,
       "dhcpGatewayIPAddress": dhcpGatewayIPAddress,
       "dhcpSubnetMask": dhcpSubnetMask,
       "dhcpDomainName": dhcpDomainName,
       "dhcpPrimaryDNSServer": dhcpPrimaryDNSServer,
       "dhcpSecondaryDNSServer": dhcpSecondaryDNSServer,
       "dhcpTertiaryDNSServer": dhcpTertiaryDNSServer,
       "ethernetInterfaceVlan": ethernetInterfaceVlan,
       "ethernetInterfaceVlanID": ethernetInterfaceVlanID,
       "ethernetInterfaceIPv6": ethernetInterfaceIPv6,
       "ethernetInterfaceIPv6Enabled": ethernetInterfaceIPv6Enabled,
       "ethernetInterfaceIPv6Config": ethernetInterfaceIPv6Config,
       "ethernetInterfaceIPv6LocalAddress": ethernetInterfaceIPv6LocalAddress,
       "ethernetInterfaceIPv6LinkLocalAddress": ethernetInterfaceIPv6LinkLocalAddress,
       "ethernetInterfaceIPv6StaticIPConfig": ethernetInterfaceIPv6StaticIPConfig,
       "ethernetInterfaceIPv6StaticIPConfigEnabled": ethernetInterfaceIPv6StaticIPConfigEnabled,
       "ethernetInterfaceIPv6StaticIPAddress": ethernetInterfaceIPv6StaticIPAddress,
       "ethernetInterfaceIPv6StaticIPAddressPrefixLen": ethernetInterfaceIPv6StaticIPAddressPrefixLen,
       "ethernetInterfaceIPv6StaticIPDefaultRoute": ethernetInterfaceIPv6StaticIPDefaultRoute,
       "ethernetInterfaceIPv6AutoIPConfig": ethernetInterfaceIPv6AutoIPConfig,
       "ethernetInterfaceDHCPv6Config": ethernetInterfaceDHCPv6Config,
       "ethernetInterfaceDHCPv6Enabled": ethernetInterfaceDHCPv6Enabled,
       "ethernetInterfaceDHCPv6IPAddress": ethernetInterfaceDHCPv6IPAddress,
       "ethernetInterfaceDHCPv6DomainName": ethernetInterfaceDHCPv6DomainName,
       "ethernetInterfaceDHCPv6PrimaryDNSServer": ethernetInterfaceDHCPv6PrimaryDNSServer,
       "ethernetInterfaceDHCPv6SecondaryDNSServer": ethernetInterfaceDHCPv6SecondaryDNSServer,
       "ethernetInterfaceDHCPv6TertiaryDNSServer": ethernetInterfaceDHCPv6TertiaryDNSServer,
       "ethernetInterfaceDHCPv6Server": ethernetInterfaceDHCPv6Server,
       "ethernetInterfaceIPv6StatelessAutoConfig": ethernetInterfaceIPv6StatelessAutoConfig,
       "ethernetInterfaceIPv6StatelessAutoConfigEnabled": ethernetInterfaceIPv6StatelessAutoConfigEnabled,
       "ethernetInterfaceStatelessAutoConfigAddressesTable": ethernetInterfaceStatelessAutoConfigAddressesTable,
       "ethernetInterfaceStatelessAutoConfigAddressesEntry": ethernetInterfaceStatelessAutoConfigAddressesEntry,
       "ethernetInterfaceStatelessAutoConfigAddressesIndex": ethernetInterfaceStatelessAutoConfigAddressesIndex,
       "ethernetInterfaceStatelessAutoConfigAddresses": ethernetInterfaceStatelessAutoConfigAddresses,
       "ethernetInterfaceStatelessAutoConfigAddressesPrefixLen": ethernetInterfaceStatelessAutoConfigAddressesPrefixLen,
       "ddnsStatus": ddnsStatus,
       "hostName": hostName,
       "ddnsDomainToUse": ddnsDomainToUse,
       "domainName": domainName,
       "tcpProtocols": tcpProtocols,
       "snmpAgentConfig": snmpAgentConfig,
       "snmpSystemName": snmpSystemName,
       "snmpSystemContact": snmpSystemContact,
       "snmpSystemLocation": snmpSystemLocation,
       "snmpSystemAgentTrapsDisable": snmpSystemAgentTrapsDisable,
       "snmpAgentCommunityConfig": snmpAgentCommunityConfig,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpCommunityEntryIndex": snmpCommunityEntryIndex,
       "snmpCommunityEntryCommunityName": snmpCommunityEntryCommunityName,
       "snmpCommunityEntryCommunityIpAddress1": snmpCommunityEntryCommunityIpAddress1,
       "snmpCommunityEntryCommunityIpAddress2": snmpCommunityEntryCommunityIpAddress2,
       "snmpCommunityEntryCommunityIpAddress3": snmpCommunityEntryCommunityIpAddress3,
       "snmpCommunityEntryCommunityViewType": snmpCommunityEntryCommunityViewType,
       "snmpv1SystemAgentEnable": snmpv1SystemAgentEnable,
       "snmpv3SystemAgentEnable": snmpv3SystemAgentEnable,
       "snmpAgentUserProfileConfig": snmpAgentUserProfileConfig,
       "snmpUserProfileTable": snmpUserProfileTable,
       "snmpUserProfileEntry": snmpUserProfileEntry,
       "snmpUserProfileEntryIndex": snmpUserProfileEntryIndex,
       "snmpUserProfileEntryAuthProt": snmpUserProfileEntryAuthProt,
       "snmpUserProfileEntryPrivProt": snmpUserProfileEntryPrivProt,
       "snmpUserProfileEntryPrivPassword": snmpUserProfileEntryPrivPassword,
       "snmpUserProfileEntryViewType": snmpUserProfileEntryViewType,
       "snmpUserProfileEntryIpAddress": snmpUserProfileEntryIpAddress,
       "dnsConfig": dnsConfig,
       "dnsEnabled": dnsEnabled,
       "dnsServerIPAddress1": dnsServerIPAddress1,
       "dnsServerIPAddress2": dnsServerIPAddress2,
       "dnsServerIPAddress3": dnsServerIPAddress3,
       "dnsServerIPv6Address1": dnsServerIPv6Address1,
       "dnsServerIPv6Address2": dnsServerIPv6Address2,
       "dnsServerIPv6Address3": dnsServerIPv6Address3,
       "dnsPriority": dnsPriority,
       "smtpConfig": smtpConfig,
       "smtpServerNameOrIPAddress": smtpServerNameOrIPAddress,
       "smtpServerPort": smtpServerPort,
       "smtpServerAuthentication": smtpServerAuthentication,
       "smtpServerAuthenticationUser": smtpServerAuthenticationUser,
       "smtpServerAuthenticationPassword": smtpServerAuthenticationPassword,
       "smtpServerAuthenticationMethod": smtpServerAuthenticationMethod,
       "tcpApplicationConfig": tcpApplicationConfig,
       "telnetConnectionCounts": telnetConnectionCounts,
       "slpAddrType": slpAddrType,
       "slpMulticastAddr": slpMulticastAddr,
       "sshServerConfig": sshServerConfig,
       "sshServerHostKeySize": sshServerHostKeySize,
       "sshServerHostKeyFingerprint": sshServerHostKeyFingerprint,
       "sshServerHostKeyGenerate": sshServerHostKeyGenerate,
       "sshServerHostKeyGenerateProgress": sshServerHostKeyGenerateProgress,
       "sshEnable": sshEnable,
       "sslConfig": sslConfig,
       "sslHTTPSServerConfigForWeb": sslHTTPSServerConfigForWeb,
       "sslEnableHTTPSforWeb": sslEnableHTTPSforWeb,
       "sslHTTPSServerWebCertificateGeneration": sslHTTPSServerWebCertificateGeneration,
       "sslHTTPSServerWebCertificateTransfer": sslHTTPSServerWebCertificateTransfer,
       "sslHTTPSWebCertificateStatus": sslHTTPSWebCertificateStatus,
       "sslHTTPSServerConfigForCIMXML": sslHTTPSServerConfigForCIMXML,
       "sslEnableHTTPSforCIMXML": sslEnableHTTPSforCIMXML,
       "sslHTTPSServerCIMXMLCertificateGeneration": sslHTTPSServerCIMXMLCertificateGeneration,
       "sslHTTPSServerCIMXMLCertificateTransfer": sslHTTPSServerCIMXMLCertificateTransfer,
       "sslHTTPSCIMXMLCertificateStatus": sslHTTPSCIMXMLCertificateStatus,
       "sslClientConfigForLDAP": sslClientConfigForLDAP,
       "sslEnableClientLDAP": sslEnableClientLDAP,
       "sslClientLDAPCertificateGeneration": sslClientLDAPCertificateGeneration,
       "sslClientLDAPCertificateDownload": sslClientLDAPCertificateDownload,
       "sslClientLDAPCertificateImport": sslClientLDAPCertificateImport,
       "sslClientLDAPCertificateStatus": sslClientLDAPCertificateStatus,
       "sslClientLDAPTrustedCertificate1Status": sslClientLDAPTrustedCertificate1Status,
       "sslClientLDAPTrustedCertificate2Status": sslClientLDAPTrustedCertificate2Status,
       "sslClientLDAPTrustedCertificate3Status": sslClientLDAPTrustedCertificate3Status,
       "sslClientLDAPTrustedCertificate4Status": sslClientLDAPTrustedCertificate4Status,
       "sslConfigTftpServer": sslConfigTftpServer,
       "sslConfigFileName": sslConfigFileName,
       "sslCertificateData": sslCertificateData,
       "sslCertificateDataCountry": sslCertificateDataCountry,
       "sslCertificateDataStateorProvince": sslCertificateDataStateorProvince,
       "sslCertificateDataCityOrLocality": sslCertificateDataCityOrLocality,
       "sslCertificateDataOrganizationName": sslCertificateDataOrganizationName,
       "sslCertificateDataIMMHostName": sslCertificateDataIMMHostName,
       "sslCertificateDataContact": sslCertificateDataContact,
       "sslCertificateDataEmailAddr": sslCertificateDataEmailAddr,
       "sslCertificateDataOrganizationUnit": sslCertificateDataOrganizationUnit,
       "sslCertificateDataSurname": sslCertificateDataSurname,
       "sslCertificateDataGivenName": sslCertificateDataGivenName,
       "sslCertificateDataInitials": sslCertificateDataInitials,
       "sslCertificateDataDNQualifier": sslCertificateDataDNQualifier,
       "sslCertificateDataCSRChallengePassword": sslCertificateDataCSRChallengePassword,
       "sslCertificateDataCSRUnstructuredName": sslCertificateDataCSRUnstructuredName,
       "certDomainNames": certDomainNames,
       "certDomainNameTable": certDomainNameTable,
       "certDomainNameEntry": certDomainNameEntry,
       "certDomainIndex": certDomainIndex,
       "certDomainName": certDomainName,
       "certDomainNameStatus": certDomainNameStatus,
       "addCertDomainName": addCertDomainName,
       "rmCertDomainName": rmCertDomainName,
       "skrServers": skrServers,
       "skrServerTable": skrServerTable,
       "skrServerEntry": skrServerEntry,
       "skrServerIndex": skrServerIndex,
       "skrServerHostname": skrServerHostname,
       "skrServerPort": skrServerPort,
       "skrServerCertAction": skrServerCertAction,
       "skrDeviceGroup": skrDeviceGroup,
       "skrClientConfigCertficate": skrClientConfigCertficate,
       "skrClientCertificateGeneration": skrClientCertificateGeneration,
       "skrClientCertificateTransfer": skrClientCertificateTransfer,
       "skrClientCertificateStatus": skrClientCertificateStatus,
       "skrCertificateData": skrCertificateData,
       "skrCertificateDataCountry": skrCertificateDataCountry,
       "skrCertificateDataStateorProvince": skrCertificateDataStateorProvince,
       "skrCertificateDataCityOrLocality": skrCertificateDataCityOrLocality,
       "skrCertificateDataOrganizationName": skrCertificateDataOrganizationName,
       "skrCertificateDataIMMHostName": skrCertificateDataIMMHostName,
       "skrCertificateDataContact": skrCertificateDataContact,
       "skrCertificateDataEmailAddr": skrCertificateDataEmailAddr,
       "skrCertificateDataOrganizationUnit": skrCertificateDataOrganizationUnit,
       "skrCertificateDataSurname": skrCertificateDataSurname,
       "skrCertificateDataGivenName": skrCertificateDataGivenName,
       "skrCertificateDataInitials": skrCertificateDataInitials,
       "skrCertificateDataDNQualifier": skrCertificateDataDNQualifier,
       "skrCertificateDataCSRChallengePassword": skrCertificateDataCSRChallengePassword,
       "skrCertificateDataCSRUnstructuredName": skrCertificateDataCSRUnstructuredName,
       "skrConfigFtpServer": skrConfigFtpServer,
       "skrConfigFtpServerMode": skrConfigFtpServerMode,
       "skrConfigFtpCallPort": skrConfigFtpCallPort,
       "skrConfigFTPCallUserID": skrConfigFTPCallUserID,
       "skrConfigFtpCallPassword": skrConfigFtpCallPassword,
       "skrConfigFileName": skrConfigFileName,
       "tcpPortAssignmentCfg": tcpPortAssignmentCfg,
       "tcpPortsRestoreDefault": tcpPortsRestoreDefault,
       "httpPortAssignment": httpPortAssignment,
       "httpsPortAssignment": httpsPortAssignment,
       "telnetLegacyCLIPortAssignment": telnetLegacyCLIPortAssignment,
       "sshLegacyCLIPortAssignment": sshLegacyCLIPortAssignment,
       "snmpAgentPortAssignment": snmpAgentPortAssignment,
       "snmpTrapsPortAssignment": snmpTrapsPortAssignment,
       "remvidPortAssignment": remvidPortAssignment,
       "ibmSystemDirectorHttpPortAssignment": ibmSystemDirectorHttpPortAssignment,
       "ibmSystemDirectorHttpsPortAssignment": ibmSystemDirectorHttpsPortAssignment,
       "ldapClientCfg": ldapClientCfg,
       "ldapServer1NameOrIPAddress": ldapServer1NameOrIPAddress,
       "ldapServer1PortNumber": ldapServer1PortNumber,
       "ldapServer2NameOrIPAddress": ldapServer2NameOrIPAddress,
       "ldapServer2PortNumber": ldapServer2PortNumber,
       "ldapServer3NameOrIPAddress": ldapServer3NameOrIPAddress,
       "ldapServer3PortNumber": ldapServer3PortNumber,
       "ldapServer4NameOrIPAddress": ldapServer4NameOrIPAddress,
       "ldapServer4PortNumber": ldapServer4PortNumber,
       "ldapRootDN": ldapRootDN,
       "ldapUserSearchBaseDN": ldapUserSearchBaseDN,
       "ldapGroupFilter": ldapGroupFilter,
       "ldapBindingMethod": ldapBindingMethod,
       "ldapClientAuthenticationDN": ldapClientAuthenticationDN,
       "ldapClientAuthenticationPassword": ldapClientAuthenticationPassword,
       "ldapRoleBasedSecurityEnabled": ldapRoleBasedSecurityEnabled,
       "ldapServerTargetName": ldapServerTargetName,
       "ldapUIDsearchAttribute": ldapUIDsearchAttribute,
       "ldapGroupSearchAttribute": ldapGroupSearchAttribute,
       "ldapLoginPermissionAttribute": ldapLoginPermissionAttribute,
       "ldapUseDNSOrPreConfiguredServers": ldapUseDNSOrPreConfiguredServers,
       "ldapDomainSource": ldapDomainSource,
       "ldapForestName": ldapForestName,
       "ldapAuthCfg": ldapAuthCfg,
       "ldapSearchDomain": ldapSearchDomain,
       "ldapServiceName": ldapServiceName,
       "ntpConfig": ntpConfig,
       "ntpEnable": ntpEnable,
       "ntpIpAddressHostname1": ntpIpAddressHostname1,
       "ntpUpdateFrequency": ntpUpdateFrequency,
       "ntpIpAddressHostname2": ntpIpAddressHostname2,
       "ntpUpdateClock": ntpUpdateClock,
       "ntpIpAddressHostname3": ntpIpAddressHostname3,
       "ntpIpAddressHostname4": ntpIpAddressHostname4,
       "configurationManagement": configurationManagement,
       "configurationManagementTftpServer": configurationManagementTftpServer,
       "configurationManagementFileName": configurationManagementFileName,
       "configurationManagementSaveStart": configurationManagementSaveStart,
       "configurationManagementRestoreStart": configurationManagementRestoreStart,
       "configurationManagementStatus": configurationManagementStatus,
       "immVersionCheck": immVersionCheck,
       "generalSystemSettings": generalSystemSettings,
       "serverTimers": serverTimers,
       "oSHang": oSHang,
       "oSLoader": oSLoader,
       "networkPXEboot": networkPXEboot,
       "systemPower": systemPower,
       "powerStatistics": powerStatistics,
       "currentSysPowerStatus": currentSysPowerStatus,
       "powerOnHours": powerOnHours,
       "restartCount": restartCount,
       "systemState": systemState,
       "powerSysConfig": powerSysConfig,
       "powerSysOffDelay": powerSysOffDelay,
       "powerSysOnClockSetting": powerSysOnClockSetting,
       "powerOffSystemControl": powerOffSystemControl,
       "powerOffWithOsShutdown": powerOffWithOsShutdown,
       "powerOffImmediately": powerOffImmediately,
       "powerOnSystemControl": powerOnSystemControl,
       "powerOnImmediately": powerOnImmediately,
       "powerCyclingSchedule": powerCyclingSchedule,
       "schedulePowerOffWithOsShutdown": schedulePowerOffWithOsShutdown,
       "schedulePowerOnSystem": schedulePowerOnSystem,
       "powerControlSleep": powerControlSleep,
       "powerEnterSleep": powerEnterSleep,
       "powerExitSleep": powerExitSleep,
       "restartReset": restartReset,
       "shutdownOsThenRestart": shutdownOsThenRestart,
       "restartSystemImmediately": restartSystemImmediately,
       "restartSPImmediately": restartSPImmediately,
       "resetSPConfigAndRestart": resetSPConfigAndRestart,
       "scheduleShutdownOsThenRestart": scheduleShutdownOsThenRestart,
       "resetPowerSchedules": resetPowerSchedules,
       "firmwareUpdate": firmwareUpdate,
       "firmwareUpdateTarget": firmwareUpdateTarget,
       "firmwareUpdateTftpServer": firmwareUpdateTftpServer,
       "firmwareUpdateFileName": firmwareUpdateFileName,
       "firmwareUpdateStart": firmwareUpdateStart,
       "firmwareUpdateStatus": firmwareUpdateStatus,
       "serviceAdvisor": serviceAdvisor,
       "autoCallHomeSetup": autoCallHomeSetup,
       "acceptLicenseAgreement": acceptLicenseAgreement,
       "serviceAdvisorEnable": serviceAdvisorEnable,
       "serviceSupportCenter": serviceSupportCenter,
       "ibmSupportCenter": ibmSupportCenter,
       "contactInformation": contactInformation,
       "companyName": companyName,
       "contactName": contactName,
       "phoneNumber": phoneNumber,
       "emailAddress": emailAddress,
       "address": address,
       "city": city,
       "state": state,
       "postalCode": postalCode,
       "phoneExtension": phoneExtension,
       "altContactName": altContactName,
       "altPhoneNumber": altPhoneNumber,
       "altPhoneExtension": altPhoneExtension,
       "altEmailAddress": altEmailAddress,
       "machineLocationPhoneNumber": machineLocationPhoneNumber,
       "httpProxyConfig": httpProxyConfig,
       "httpProxyEnable": httpProxyEnable,
       "httpProxyLocation": httpProxyLocation,
       "httpProxyPort": httpProxyPort,
       "httpProxyUserName": httpProxyUserName,
       "httpProxyPassword": httpProxyPassword,
       "activityLogs": activityLogs,
       "activityLogTable": activityLogTable,
       "activityLogEntry": activityLogEntry,
       "activityLogIndex": activityLogIndex,
       "activityLogString": activityLogString,
       "activityLogAcknowledge": activityLogAcknowledge,
       "activityLogAttribute": activityLogAttribute,
       "autoFTPSetup": autoFTPSetup,
       "autoFTPCallMode": autoFTPCallMode,
       "autoFTPCallAddr": autoFTPCallAddr,
       "autoFTPCallPort": autoFTPCallPort,
       "autoFTPCallUserID": autoFTPCallUserID,
       "autoFTPCallPassword": autoFTPCallPassword,
       "callHomeExclusionEvents": callHomeExclusionEvents,
       "readCallHomeExclusionEventTable": readCallHomeExclusionEventTable,
       "readCallHomeExclusionEventEntry": readCallHomeExclusionEventEntry,
       "readCallHomeExclusionEventIndex": readCallHomeExclusionEventIndex,
       "readCallHomeExclusionEventID": readCallHomeExclusionEventID,
       "addCallHomeExclusionEvent": addCallHomeExclusionEvent,
       "rmCallHomeExclusionEvent": rmCallHomeExclusionEvent,
       "rmAllCallHomeExclusionEvent": rmAllCallHomeExclusionEvent,
       "testCallHome": testCallHome,
       "generateTestCallHome": generateTestCallHome,
       "scaling": scaling,
       "scalableComplex": scalableComplex,
       "scalableComplexIdentifier": scalableComplexIdentifier,
       "scalableComplexNumPartitions": scalableComplexNumPartitions,
       "scalableComplexNumNodes": scalableComplexNumNodes,
       "scalableComplexClear": scalableComplexClear,
       "scalableComplexPartition": scalableComplexPartition,
       "scalableComplexPartitionTable": scalableComplexPartitionTable,
       "scalableComplexPartitionEntry": scalableComplexPartitionEntry,
       "scalableComplexPartitionIdentifier": scalableComplexPartitionIdentifier,
       "scalableComplexPartitionMode": scalableComplexPartitionMode,
       "scalableComplexPartitionPriNodeKey": scalableComplexPartitionPriNodeKey,
       "scalableComplexPartitionNumNodes": scalableComplexPartitionNumNodes,
       "scalableComplexPartitionStatus": scalableComplexPartitionStatus,
       "scalableComplexPartitionSelect": scalableComplexPartitionSelect,
       "scalableComplexPartitionAction": scalableComplexPartitionAction,
       "scalableComplexPartitionCreate": scalableComplexPartitionCreate,
       "scalableComplexPartitionCreateTable": scalableComplexPartitionCreateTable,
       "scalableComplexPartitionCreateEntry": scalableComplexPartitionCreateEntry,
       "scalableComplexPartitionCreateIndex": scalableComplexPartitionCreateIndex,
       "scalableComplexPartitionCreateNodeKey": scalableComplexPartitionCreateNodeKey,
       "scalableComplexPartitionActionCreate": scalableComplexPartitionActionCreate,
       "scalableComplexNode": scalableComplexNode,
       "scalableComplexNodeTable": scalableComplexNodeTable,
       "scalableComplexNodeEntry": scalableComplexNodeEntry,
       "scalableComplexNodeIndex": scalableComplexNodeIndex,
       "scalableComplexNodeSerialNumber": scalableComplexNodeSerialNumber,
       "scalableComplexNodeKey": scalableComplexNodeKey,
       "scalableComplexNodePartitionID": scalableComplexNodePartitionID,
       "scalableComplexNodeRole": scalableComplexNodeRole,
       "scalableComplexNodeNumPorts": scalableComplexNodeNumPorts,
       "scalableComplexNodeSelect": scalableComplexNodeSelect,
       "scalableComplexNodeAction": scalableComplexNodeAction,
       "scalableComplexNodeAutoCreate": scalableComplexNodeAutoCreate,
       "scalableComplexNodePort": scalableComplexNodePort,
       "scalableComplexNodePortTable": scalableComplexNodePortTable,
       "scalableComplexNodePortEntry": scalableComplexNodePortEntry,
       "scalableComplexNodePortIndex": scalableComplexNodePortIndex,
       "scalableComplexNodePortNum": scalableComplexNodePortNum,
       "scalableComplexNodePortRemNodeKey": scalableComplexNodePortRemNodeKey,
       "scalableComplexNodePortRemNum": scalableComplexNodePortRemNum,
       "scalableComplexNodePortStatus": scalableComplexNodePortStatus,
       "scalableComplexNodePortType": scalableComplexNodePortType}
)
