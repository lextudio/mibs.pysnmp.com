# SNMP MIB module (XYLAN-HEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-HEALTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:04 2024
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

(xylanHealthArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanHealthArch")


# MODULE-IDENTITY


# Types definitions



class HealthPortUpDownStatus(Integer32):
    """Custom type HealthPortUpDownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("healthPortDn", 1),
          ("healthPortUp", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HealthDeviceInfo_ObjectIdentity = ObjectIdentity
healthDeviceInfo = _HealthDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1)
)


class _HealthDeviceRxData_Type(OctetString):
    """Custom type healthDeviceRxData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthDeviceRxData_Type.__name__ = "OctetString"
_HealthDeviceRxData_Object = MibScalar
healthDeviceRxData = _HealthDeviceRxData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 1),
    _HealthDeviceRxData_Type()
)
healthDeviceRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRxData.setStatus("mandatory")
_HealthDeviceRxTimeDelta_Type = Integer32
_HealthDeviceRxTimeDelta_Object = MibScalar
healthDeviceRxTimeDelta = _HealthDeviceRxTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 2),
    _HealthDeviceRxTimeDelta_Type()
)
healthDeviceRxTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRxTimeDelta.setStatus("mandatory")


class _HealthDeviceRxTxData_Type(OctetString):
    """Custom type healthDeviceRxTxData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthDeviceRxTxData_Type.__name__ = "OctetString"
_HealthDeviceRxTxData_Object = MibScalar
healthDeviceRxTxData = _HealthDeviceRxTxData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 3),
    _HealthDeviceRxTxData_Type()
)
healthDeviceRxTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRxTxData.setStatus("mandatory")
_HealthDeviceRxTxTimeDelta_Type = Integer32
_HealthDeviceRxTxTimeDelta_Object = MibScalar
healthDeviceRxTxTimeDelta = _HealthDeviceRxTxTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 4),
    _HealthDeviceRxTxTimeDelta_Type()
)
healthDeviceRxTxTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceRxTxTimeDelta.setStatus("mandatory")


class _HealthDeviceBackplaneData_Type(OctetString):
    """Custom type healthDeviceBackplaneData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthDeviceBackplaneData_Type.__name__ = "OctetString"
_HealthDeviceBackplaneData_Object = MibScalar
healthDeviceBackplaneData = _HealthDeviceBackplaneData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 5),
    _HealthDeviceBackplaneData_Type()
)
healthDeviceBackplaneData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceBackplaneData.setStatus("mandatory")
_HealthDeviceBackplaneTimeDelta_Type = Integer32
_HealthDeviceBackplaneTimeDelta_Object = MibScalar
healthDeviceBackplaneTimeDelta = _HealthDeviceBackplaneTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 6),
    _HealthDeviceBackplaneTimeDelta_Type()
)
healthDeviceBackplaneTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceBackplaneTimeDelta.setStatus("mandatory")


class _HealthDeviceCamData_Type(OctetString):
    """Custom type healthDeviceCamData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_HealthDeviceCamData_Type.__name__ = "OctetString"
_HealthDeviceCamData_Object = MibScalar
healthDeviceCamData = _HealthDeviceCamData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 7),
    _HealthDeviceCamData_Type()
)
healthDeviceCamData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceCamData.setStatus("mandatory")
_HealthDeviceCamTimeDelta_Type = Integer32
_HealthDeviceCamTimeDelta_Object = MibScalar
healthDeviceCamTimeDelta = _HealthDeviceCamTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 8),
    _HealthDeviceCamTimeDelta_Type()
)
healthDeviceCamTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceCamTimeDelta.setStatus("mandatory")


class _HealthDeviceMemoryData_Type(OctetString):
    """Custom type healthDeviceMemoryData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_HealthDeviceMemoryData_Type.__name__ = "OctetString"
_HealthDeviceMemoryData_Object = MibScalar
healthDeviceMemoryData = _HealthDeviceMemoryData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 9),
    _HealthDeviceMemoryData_Type()
)
healthDeviceMemoryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMemoryData.setStatus("mandatory")
_HealthDeviceMemoryTimeDelta_Type = Integer32
_HealthDeviceMemoryTimeDelta_Object = MibScalar
healthDeviceMemoryTimeDelta = _HealthDeviceMemoryTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 10),
    _HealthDeviceMemoryTimeDelta_Type()
)
healthDeviceMemoryTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMemoryTimeDelta.setStatus("mandatory")
_HealthDeviceCpuData_Type = OctetString
_HealthDeviceCpuData_Object = MibScalar
healthDeviceCpuData = _HealthDeviceCpuData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 11),
    _HealthDeviceCpuData_Type()
)
healthDeviceCpuData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceCpuData.setStatus("mandatory")
_HealthDeviceCpuTimeDelta_Type = Integer32
_HealthDeviceCpuTimeDelta_Object = MibScalar
healthDeviceCpuTimeDelta = _HealthDeviceCpuTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 12),
    _HealthDeviceCpuTimeDelta_Type()
)
healthDeviceCpuTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceCpuTimeDelta.setStatus("mandatory")
_HealthDeviceNumCpus_Type = Integer32
_HealthDeviceNumCpus_Object = MibScalar
healthDeviceNumCpus = _HealthDeviceNumCpus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 13),
    _HealthDeviceNumCpus_Type()
)
healthDeviceNumCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceNumCpus.setStatus("mandatory")
_HealthDeviceMemoryTotal_Type = Integer32
_HealthDeviceMemoryTotal_Object = MibScalar
healthDeviceMemoryTotal = _HealthDeviceMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 14),
    _HealthDeviceMemoryTotal_Type()
)
healthDeviceMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMemoryTotal.setStatus("mandatory")
_HealthDeviceMemoryFree_Type = Integer32
_HealthDeviceMemoryFree_Object = MibScalar
healthDeviceMemoryFree = _HealthDeviceMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 15),
    _HealthDeviceMemoryFree_Type()
)
healthDeviceMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMemoryFree.setStatus("mandatory")
_HealthDeviceMpmCamTotal_Type = Integer32
_HealthDeviceMpmCamTotal_Object = MibScalar
healthDeviceMpmCamTotal = _HealthDeviceMpmCamTotal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 16),
    _HealthDeviceMpmCamTotal_Type()
)
healthDeviceMpmCamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMpmCamTotal.setStatus("mandatory")
_HealthDeviceMpmCamFree_Type = Integer32
_HealthDeviceMpmCamFree_Object = MibScalar
healthDeviceMpmCamFree = _HealthDeviceMpmCamFree_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 17),
    _HealthDeviceMpmCamFree_Type()
)
healthDeviceMpmCamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMpmCamFree.setStatus("mandatory")
_HealthDeviceHreCamTotal_Type = Integer32
_HealthDeviceHreCamTotal_Object = MibScalar
healthDeviceHreCamTotal = _HealthDeviceHreCamTotal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 18),
    _HealthDeviceHreCamTotal_Type()
)
healthDeviceHreCamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceHreCamTotal.setStatus("mandatory")
_HealthDeviceHreCamFree_Type = Integer32
_HealthDeviceHreCamFree_Object = MibScalar
healthDeviceHreCamFree = _HealthDeviceHreCamFree_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 19),
    _HealthDeviceHreCamFree_Type()
)
healthDeviceHreCamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceHreCamFree.setStatus("mandatory")
_HealthDeviceTemp_Type = Integer32
_HealthDeviceTemp_Object = MibScalar
healthDeviceTemp = _HealthDeviceTemp_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 20),
    _HealthDeviceTemp_Type()
)
healthDeviceTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemp.setStatus("mandatory")
_HealthDeviceIPRouteCacheFlushCount_Type = Integer32
_HealthDeviceIPRouteCacheFlushCount_Object = MibScalar
healthDeviceIPRouteCacheFlushCount = _HealthDeviceIPRouteCacheFlushCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 21),
    _HealthDeviceIPRouteCacheFlushCount_Type()
)
healthDeviceIPRouteCacheFlushCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceIPRouteCacheFlushCount.setStatus("mandatory")
_HealthDeviceIPXRouteCacheFlushCount_Type = Integer32
_HealthDeviceIPXRouteCacheFlushCount_Object = MibScalar
healthDeviceIPXRouteCacheFlushCount = _HealthDeviceIPXRouteCacheFlushCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 22),
    _HealthDeviceIPXRouteCacheFlushCount_Type()
)
healthDeviceIPXRouteCacheFlushCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceIPXRouteCacheFlushCount.setStatus("mandatory")
_HealthDeviceMpmRxOverrunCount_Type = Integer32
_HealthDeviceMpmRxOverrunCount_Object = MibScalar
healthDeviceMpmRxOverrunCount = _HealthDeviceMpmRxOverrunCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 23),
    _HealthDeviceMpmRxOverrunCount_Type()
)
healthDeviceMpmRxOverrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMpmRxOverrunCount.setStatus("mandatory")
_HealthDeviceMpmTxOverrunCount_Type = Integer32
_HealthDeviceMpmTxOverrunCount_Object = MibScalar
healthDeviceMpmTxOverrunCount = _HealthDeviceMpmTxOverrunCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 24),
    _HealthDeviceMpmTxOverrunCount_Type()
)
healthDeviceMpmTxOverrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceMpmTxOverrunCount.setStatus("mandatory")


class _HealthDeviceVccData_Type(OctetString):
    """Custom type healthDeviceVccData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthDeviceVccData_Type.__name__ = "OctetString"
_HealthDeviceVccData_Object = MibScalar
healthDeviceVccData = _HealthDeviceVccData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 25),
    _HealthDeviceVccData_Type()
)
healthDeviceVccData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceVccData.setStatus("mandatory")
_HealthDeviceVccTimeDelta_Type = Integer32
_HealthDeviceVccTimeDelta_Object = MibScalar
healthDeviceVccTimeDelta = _HealthDeviceVccTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 26),
    _HealthDeviceVccTimeDelta_Type()
)
healthDeviceVccTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceVccTimeDelta.setStatus("mandatory")


class _HealthDeviceTemperatureData_Type(OctetString):
    """Custom type healthDeviceTemperatureData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthDeviceTemperatureData_Type.__name__ = "OctetString"
_HealthDeviceTemperatureData_Object = MibScalar
healthDeviceTemperatureData = _HealthDeviceTemperatureData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 27),
    _HealthDeviceTemperatureData_Type()
)
healthDeviceTemperatureData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemperatureData.setStatus("mandatory")
_HealthDeviceTemperatureTimeDelta_Type = Integer32
_HealthDeviceTemperatureTimeDelta_Object = MibScalar
healthDeviceTemperatureTimeDelta = _HealthDeviceTemperatureTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 28),
    _HealthDeviceTemperatureTimeDelta_Type()
)
healthDeviceTemperatureTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceTemperatureTimeDelta.setStatus("mandatory")


class _HealthDeviceVpData_Type(OctetString):
    """Custom type healthDeviceVpData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthDeviceVpData_Type.__name__ = "OctetString"
_HealthDeviceVpData_Object = MibScalar
healthDeviceVpData = _HealthDeviceVpData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 29),
    _HealthDeviceVpData_Type()
)
healthDeviceVpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceVpData.setStatus("mandatory")
_HealthDeviceVpTimeDelta_Type = Integer32
_HealthDeviceVpTimeDelta_Object = MibScalar
healthDeviceVpTimeDelta = _HealthDeviceVpTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 30),
    _HealthDeviceVpTimeDelta_Type()
)
healthDeviceVpTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceVpTimeDelta.setStatus("mandatory")
_HealthDeviceHreCollisionTotal_Type = Integer32
_HealthDeviceHreCollisionTotal_Object = MibScalar
healthDeviceHreCollisionTotal = _HealthDeviceHreCollisionTotal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 31),
    _HealthDeviceHreCollisionTotal_Type()
)
healthDeviceHreCollisionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceHreCollisionTotal.setStatus("mandatory")
_HealthDeviceHreCollisionFree_Type = Integer32
_HealthDeviceHreCollisionFree_Object = MibScalar
healthDeviceHreCollisionFree = _HealthDeviceHreCollisionFree_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 1, 32),
    _HealthDeviceHreCollisionFree_Type()
)
healthDeviceHreCollisionFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthDeviceHreCollisionFree.setStatus("mandatory")
_HealthModuleInfo_ObjectIdentity = ObjectIdentity
healthModuleInfo = _HealthModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2)
)
_HealthModuleTable_Object = MibTable
healthModuleTable = _HealthModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    healthModuleTable.setStatus("mandatory")
_HealthModuleEntry_Object = MibTableRow
healthModuleEntry = _HealthModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1)
)
healthModuleEntry.setIndexNames(
    (0, "XYLAN-HEALTH-MIB", "healthModuleSlot"),
)
if mibBuilder.loadTexts:
    healthModuleEntry.setStatus("mandatory")
_HealthModuleSlot_Type = Integer32
_HealthModuleSlot_Object = MibTableColumn
healthModuleSlot = _HealthModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 1),
    _HealthModuleSlot_Type()
)
healthModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleSlot.setStatus("mandatory")


class _HealthModuleRxData_Type(OctetString):
    """Custom type healthModuleRxData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthModuleRxData_Type.__name__ = "OctetString"
_HealthModuleRxData_Object = MibTableColumn
healthModuleRxData = _HealthModuleRxData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 2),
    _HealthModuleRxData_Type()
)
healthModuleRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxData.setStatus("mandatory")
_HealthModuleRxTimeDelta_Type = Integer32
_HealthModuleRxTimeDelta_Object = MibTableColumn
healthModuleRxTimeDelta = _HealthModuleRxTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 3),
    _HealthModuleRxTimeDelta_Type()
)
healthModuleRxTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxTimeDelta.setStatus("mandatory")


class _HealthModuleRxTxData_Type(OctetString):
    """Custom type healthModuleRxTxData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthModuleRxTxData_Type.__name__ = "OctetString"
_HealthModuleRxTxData_Object = MibTableColumn
healthModuleRxTxData = _HealthModuleRxTxData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 4),
    _HealthModuleRxTxData_Type()
)
healthModuleRxTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxTxData.setStatus("mandatory")
_HealthModuleRxTxTimeDelta_Type = Integer32
_HealthModuleRxTxTimeDelta_Object = MibTableColumn
healthModuleRxTxTimeDelta = _HealthModuleRxTxTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 5),
    _HealthModuleRxTxTimeDelta_Type()
)
healthModuleRxTxTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxTxTimeDelta.setStatus("mandatory")


class _HealthModuleBackplaneData_Type(OctetString):
    """Custom type healthModuleBackplaneData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthModuleBackplaneData_Type.__name__ = "OctetString"
_HealthModuleBackplaneData_Object = MibTableColumn
healthModuleBackplaneData = _HealthModuleBackplaneData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 6),
    _HealthModuleBackplaneData_Type()
)
healthModuleBackplaneData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleBackplaneData.setStatus("mandatory")
_HealthModuleBackplaneTimeDelta_Type = Integer32
_HealthModuleBackplaneTimeDelta_Object = MibTableColumn
healthModuleBackplaneTimeDelta = _HealthModuleBackplaneTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 7),
    _HealthModuleBackplaneTimeDelta_Type()
)
healthModuleBackplaneTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleBackplaneTimeDelta.setStatus("mandatory")


class _HealthModuleCamData_Type(OctetString):
    """Custom type healthModuleCamData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthModuleCamData_Type.__name__ = "OctetString"
_HealthModuleCamData_Object = MibTableColumn
healthModuleCamData = _HealthModuleCamData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 8),
    _HealthModuleCamData_Type()
)
healthModuleCamData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCamData.setStatus("mandatory")
_HealthModuleCamTimeDelta_Type = Integer32
_HealthModuleCamTimeDelta_Object = MibTableColumn
healthModuleCamTimeDelta = _HealthModuleCamTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 9),
    _HealthModuleCamTimeDelta_Type()
)
healthModuleCamTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCamTimeDelta.setStatus("mandatory")
_HealthModuleCamNumInstalled_Type = Integer32
_HealthModuleCamNumInstalled_Object = MibTableColumn
healthModuleCamNumInstalled = _HealthModuleCamNumInstalled_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 10),
    _HealthModuleCamNumInstalled_Type()
)
healthModuleCamNumInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCamNumInstalled.setStatus("mandatory")
_HealthModuleCamConfigured_Type = Integer32
_HealthModuleCamConfigured_Object = MibTableColumn
healthModuleCamConfigured = _HealthModuleCamConfigured_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 11),
    _HealthModuleCamConfigured_Type()
)
healthModuleCamConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCamConfigured.setStatus("mandatory")
_HealthModuleCamAvail_Type = Integer32
_HealthModuleCamAvail_Object = MibTableColumn
healthModuleCamAvail = _HealthModuleCamAvail_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 12),
    _HealthModuleCamAvail_Type()
)
healthModuleCamAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCamAvail.setStatus("mandatory")
_HealthModuleCamAvailNonIntern_Type = Integer32
_HealthModuleCamAvailNonIntern_Object = MibTableColumn
healthModuleCamAvailNonIntern = _HealthModuleCamAvailNonIntern_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 13),
    _HealthModuleCamAvailNonIntern_Type()
)
healthModuleCamAvailNonIntern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCamAvailNonIntern.setStatus("mandatory")
_HealthModuleCamFree_Type = Integer32
_HealthModuleCamFree_Object = MibTableColumn
healthModuleCamFree = _HealthModuleCamFree_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 14),
    _HealthModuleCamFree_Type()
)
healthModuleCamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCamFree.setStatus("mandatory")


class _HealthModuleVccData_Type(OctetString):
    """Custom type healthModuleVccData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthModuleVccData_Type.__name__ = "OctetString"
_HealthModuleVccData_Object = MibTableColumn
healthModuleVccData = _HealthModuleVccData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 15),
    _HealthModuleVccData_Type()
)
healthModuleVccData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleVccData.setStatus("mandatory")
_HealthModuleVccTimeDelta_Type = Integer32
_HealthModuleVccTimeDelta_Object = MibTableColumn
healthModuleVccTimeDelta = _HealthModuleVccTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 2, 1, 1, 16),
    _HealthModuleVccTimeDelta_Type()
)
healthModuleVccTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleVccTimeDelta.setStatus("mandatory")
_HealthPortInfo_ObjectIdentity = ObjectIdentity
healthPortInfo = _HealthPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3)
)


class _HealthPortMax_Type(OctetString):
    """Custom type healthPortMax based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(21, 21),
    )


_HealthPortMax_Type.__name__ = "OctetString"
_HealthPortMax_Object = MibScalar
healthPortMax = _HealthPortMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 1),
    _HealthPortMax_Type()
)
healthPortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortMax.setStatus("mandatory")
_HealthPortTable_Object = MibTable
healthPortTable = _HealthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2)
)
if mibBuilder.loadTexts:
    healthPortTable.setStatus("mandatory")
_HealthPortEntry_Object = MibTableRow
healthPortEntry = _HealthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1)
)
healthPortEntry.setIndexNames(
    (0, "XYLAN-HEALTH-MIB", "healthPortSlot"),
    (0, "XYLAN-HEALTH-MIB", "healthPortIF"),
)
if mibBuilder.loadTexts:
    healthPortEntry.setStatus("mandatory")


class _HealthPortSlot_Type(Integer32):
    """Custom type healthPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_HealthPortSlot_Type.__name__ = "Integer32"
_HealthPortSlot_Object = MibTableColumn
healthPortSlot = _HealthPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 1),
    _HealthPortSlot_Type()
)
healthPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortSlot.setStatus("mandatory")
_HealthPortIF_Type = Integer32
_HealthPortIF_Object = MibTableColumn
healthPortIF = _HealthPortIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 2),
    _HealthPortIF_Type()
)
healthPortIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortIF.setStatus("mandatory")
_HealthPortUpDn_Type = HealthPortUpDownStatus
_HealthPortUpDn_Object = MibTableColumn
healthPortUpDn = _HealthPortUpDn_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 3),
    _HealthPortUpDn_Type()
)
healthPortUpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortUpDn.setStatus("mandatory")


class _HealthPortRxData_Type(OctetString):
    """Custom type healthPortRxData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthPortRxData_Type.__name__ = "OctetString"
_HealthPortRxData_Object = MibTableColumn
healthPortRxData = _HealthPortRxData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 4),
    _HealthPortRxData_Type()
)
healthPortRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxData.setStatus("mandatory")
_HealthPortRxTimeDelta_Type = Integer32
_HealthPortRxTimeDelta_Object = MibTableColumn
healthPortRxTimeDelta = _HealthPortRxTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 5),
    _HealthPortRxTimeDelta_Type()
)
healthPortRxTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxTimeDelta.setStatus("mandatory")


class _HealthPortRxTxData_Type(OctetString):
    """Custom type healthPortRxTxData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthPortRxTxData_Type.__name__ = "OctetString"
_HealthPortRxTxData_Object = MibTableColumn
healthPortRxTxData = _HealthPortRxTxData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 6),
    _HealthPortRxTxData_Type()
)
healthPortRxTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxTxData.setStatus("mandatory")
_HealthPortRxTxTimeDelta_Type = Integer32
_HealthPortRxTxTimeDelta_Object = MibTableColumn
healthPortRxTxTimeDelta = _HealthPortRxTxTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 7),
    _HealthPortRxTxTimeDelta_Type()
)
healthPortRxTxTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxTxTimeDelta.setStatus("mandatory")


class _HealthPortBackplaneData_Type(OctetString):
    """Custom type healthPortBackplaneData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthPortBackplaneData_Type.__name__ = "OctetString"
_HealthPortBackplaneData_Object = MibTableColumn
healthPortBackplaneData = _HealthPortBackplaneData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 8),
    _HealthPortBackplaneData_Type()
)
healthPortBackplaneData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortBackplaneData.setStatus("mandatory")
_HealthPortBackplaneTimeDelta_Type = Integer32
_HealthPortBackplaneTimeDelta_Object = MibTableColumn
healthPortBackplaneTimeDelta = _HealthPortBackplaneTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 9),
    _HealthPortBackplaneTimeDelta_Type()
)
healthPortBackplaneTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortBackplaneTimeDelta.setStatus("mandatory")


class _HealthPortVccData_Type(OctetString):
    """Custom type healthPortVccData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HealthPortVccData_Type.__name__ = "OctetString"
_HealthPortVccData_Object = MibTableColumn
healthPortVccData = _HealthPortVccData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 10),
    _HealthPortVccData_Type()
)
healthPortVccData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortVccData.setStatus("mandatory")
_HealthPortVccTimeDelta_Type = Integer32
_HealthPortVccTimeDelta_Object = MibTableColumn
healthPortVccTimeDelta = _HealthPortVccTimeDelta_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 3, 2, 1, 11),
    _HealthPortVccTimeDelta_Type()
)
healthPortVccTimeDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortVccTimeDelta.setStatus("mandatory")
_HealthGroupInfo_ObjectIdentity = ObjectIdentity
healthGroupInfo = _HealthGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 4)
)
_HealthControlInfo_ObjectIdentity = ObjectIdentity
healthControlInfo = _HealthControlInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 5)
)
_HealthSamplingInterval_Type = Integer32
_HealthSamplingInterval_Object = MibScalar
healthSamplingInterval = _HealthSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 5, 1),
    _HealthSamplingInterval_Type()
)
healthSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthSamplingInterval.setStatus("mandatory")
_HealthSamplingReset_Type = Integer32
_HealthSamplingReset_Object = MibScalar
healthSamplingReset = _HealthSamplingReset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 5, 2),
    _HealthSamplingReset_Type()
)
healthSamplingReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    healthSamplingReset.setStatus("mandatory")
_HealthThreshInfo_ObjectIdentity = ObjectIdentity
healthThreshInfo = _HealthThreshInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6)
)


class _HealthThreshDeviceRxLimit_Type(Integer32):
    """Custom type healthThreshDeviceRxLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceRxLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceRxLimit_Object = MibScalar
healthThreshDeviceRxLimit = _HealthThreshDeviceRxLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 1),
    _HealthThreshDeviceRxLimit_Type()
)
healthThreshDeviceRxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceRxLimit.setStatus("mandatory")


class _HealthThreshDeviceRxTxLimit_Type(Integer32):
    """Custom type healthThreshDeviceRxTxLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceRxTxLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceRxTxLimit_Object = MibScalar
healthThreshDeviceRxTxLimit = _HealthThreshDeviceRxTxLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 2),
    _HealthThreshDeviceRxTxLimit_Type()
)
healthThreshDeviceRxTxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceRxTxLimit.setStatus("mandatory")


class _HealthThreshDeviceBackplaneLimit_Type(Integer32):
    """Custom type healthThreshDeviceBackplaneLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceBackplaneLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceBackplaneLimit_Object = MibScalar
healthThreshDeviceBackplaneLimit = _HealthThreshDeviceBackplaneLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 3),
    _HealthThreshDeviceBackplaneLimit_Type()
)
healthThreshDeviceBackplaneLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceBackplaneLimit.setStatus("mandatory")


class _HealthThreshDeviceCamLimit_Type(Integer32):
    """Custom type healthThreshDeviceCamLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceCamLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceCamLimit_Object = MibScalar
healthThreshDeviceCamLimit = _HealthThreshDeviceCamLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 4),
    _HealthThreshDeviceCamLimit_Type()
)
healthThreshDeviceCamLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceCamLimit.setStatus("mandatory")


class _HealthThreshDeviceMemoryLimit_Type(Integer32):
    """Custom type healthThreshDeviceMemoryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceMemoryLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceMemoryLimit_Object = MibScalar
healthThreshDeviceMemoryLimit = _HealthThreshDeviceMemoryLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 5),
    _HealthThreshDeviceMemoryLimit_Type()
)
healthThreshDeviceMemoryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceMemoryLimit.setStatus("mandatory")


class _HealthThreshDeviceCpuLimit_Type(Integer32):
    """Custom type healthThreshDeviceCpuLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceCpuLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceCpuLimit_Object = MibScalar
healthThreshDeviceCpuLimit = _HealthThreshDeviceCpuLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 6),
    _HealthThreshDeviceCpuLimit_Type()
)
healthThreshDeviceCpuLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceCpuLimit.setStatus("mandatory")


class _HealthThreshDeviceSummary_Type(OctetString):
    """Custom type healthThreshDeviceSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(27, 27),
    )


_HealthThreshDeviceSummary_Type.__name__ = "OctetString"
_HealthThreshDeviceSummary_Object = MibScalar
healthThreshDeviceSummary = _HealthThreshDeviceSummary_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 7),
    _HealthThreshDeviceSummary_Type()
)
healthThreshDeviceSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthThreshDeviceSummary.setStatus("mandatory")
_HealthThreshModuleSummaryTable_Object = MibTable
healthThreshModuleSummaryTable = _HealthThreshModuleSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 8)
)
if mibBuilder.loadTexts:
    healthThreshModuleSummaryTable.setStatus("mandatory")
_HealthThreshModuleSummaryEntry_Object = MibTableRow
healthThreshModuleSummaryEntry = _HealthThreshModuleSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 8, 1)
)
healthThreshModuleSummaryEntry.setIndexNames(
    (0, "XYLAN-HEALTH-MIB", "healthThreshModuleSummarySlot"),
)
if mibBuilder.loadTexts:
    healthThreshModuleSummaryEntry.setStatus("mandatory")


class _HealthThreshModuleSummarySlot_Type(Integer32):
    """Custom type healthThreshModuleSummarySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_HealthThreshModuleSummarySlot_Type.__name__ = "Integer32"
_HealthThreshModuleSummarySlot_Object = MibTableColumn
healthThreshModuleSummarySlot = _HealthThreshModuleSummarySlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 8, 1, 1),
    _HealthThreshModuleSummarySlot_Type()
)
healthThreshModuleSummarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthThreshModuleSummarySlot.setStatus("mandatory")


class _HealthThreshModuleSummaryData_Type(OctetString):
    """Custom type healthThreshModuleSummaryData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HealthThreshModuleSummaryData_Type.__name__ = "OctetString"
_HealthThreshModuleSummaryData_Object = MibTableColumn
healthThreshModuleSummaryData = _HealthThreshModuleSummaryData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 8, 1, 2),
    _HealthThreshModuleSummaryData_Type()
)
healthThreshModuleSummaryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthThreshModuleSummaryData.setStatus("mandatory")


class _HealthThreshDevTrapData_Type(OctetString):
    """Custom type healthThreshDevTrapData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_HealthThreshDevTrapData_Type.__name__ = "OctetString"
_HealthThreshDevTrapData_Object = MibScalar
healthThreshDevTrapData = _HealthThreshDevTrapData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 9),
    _HealthThreshDevTrapData_Type()
)
healthThreshDevTrapData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthThreshDevTrapData.setStatus("mandatory")
_HealthThreshModTrapCount_Type = Integer32
_HealthThreshModTrapCount_Object = MibScalar
healthThreshModTrapCount = _HealthThreshModTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 10),
    _HealthThreshModTrapCount_Type()
)
healthThreshModTrapCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthThreshModTrapCount.setStatus("mandatory")


class _HealthThreshModTrapData_Type(OctetString):
    """Custom type healthThreshModTrapData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HealthThreshModTrapData_Type.__name__ = "OctetString"
_HealthThreshModTrapData_Object = MibScalar
healthThreshModTrapData = _HealthThreshModTrapData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 11),
    _HealthThreshModTrapData_Type()
)
healthThreshModTrapData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthThreshModTrapData.setStatus("mandatory")
_HealthThreshPortSummaryTable_Object = MibTable
healthThreshPortSummaryTable = _HealthThreshPortSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 12)
)
if mibBuilder.loadTexts:
    healthThreshPortSummaryTable.setStatus("mandatory")
_HealthThreshPortSummaryEntry_Object = MibTableRow
healthThreshPortSummaryEntry = _HealthThreshPortSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 12, 1)
)
healthThreshPortSummaryEntry.setIndexNames(
    (0, "XYLAN-HEALTH-MIB", "healthThreshPortSummarySlot"),
    (0, "XYLAN-HEALTH-MIB", "healthThreshPortSummaryIF"),
)
if mibBuilder.loadTexts:
    healthThreshPortSummaryEntry.setStatus("mandatory")


class _HealthThreshPortSummarySlot_Type(Integer32):
    """Custom type healthThreshPortSummarySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_HealthThreshPortSummarySlot_Type.__name__ = "Integer32"
_HealthThreshPortSummarySlot_Object = MibTableColumn
healthThreshPortSummarySlot = _HealthThreshPortSummarySlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 12, 1, 1),
    _HealthThreshPortSummarySlot_Type()
)
healthThreshPortSummarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthThreshPortSummarySlot.setStatus("mandatory")


class _HealthThreshPortSummaryIF_Type(Integer32):
    """Custom type healthThreshPortSummaryIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_HealthThreshPortSummaryIF_Type.__name__ = "Integer32"
_HealthThreshPortSummaryIF_Object = MibTableColumn
healthThreshPortSummaryIF = _HealthThreshPortSummaryIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 12, 1, 2),
    _HealthThreshPortSummaryIF_Type()
)
healthThreshPortSummaryIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthThreshPortSummaryIF.setStatus("mandatory")


class _HealthThreshPortSummaryData_Type(OctetString):
    """Custom type healthThreshPortSummaryData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_HealthThreshPortSummaryData_Type.__name__ = "OctetString"
_HealthThreshPortSummaryData_Object = MibTableColumn
healthThreshPortSummaryData = _HealthThreshPortSummaryData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 12, 1, 3),
    _HealthThreshPortSummaryData_Type()
)
healthThreshPortSummaryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthThreshPortSummaryData.setStatus("mandatory")
_HealthThreshPortTrapSlot_Type = Integer32
_HealthThreshPortTrapSlot_Object = MibScalar
healthThreshPortTrapSlot = _HealthThreshPortTrapSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 13),
    _HealthThreshPortTrapSlot_Type()
)
healthThreshPortTrapSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthThreshPortTrapSlot.setStatus("mandatory")
_HealthThreshPortTrapCount_Type = Integer32
_HealthThreshPortTrapCount_Object = MibScalar
healthThreshPortTrapCount = _HealthThreshPortTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 14),
    _HealthThreshPortTrapCount_Type()
)
healthThreshPortTrapCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthThreshPortTrapCount.setStatus("mandatory")


class _HealthThreshPortTrapData_Type(OctetString):
    """Custom type healthThreshPortTrapData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HealthThreshPortTrapData_Type.__name__ = "OctetString"
_HealthThreshPortTrapData_Object = MibScalar
healthThreshPortTrapData = _HealthThreshPortTrapData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 15),
    _HealthThreshPortTrapData_Type()
)
healthThreshPortTrapData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthThreshPortTrapData.setStatus("mandatory")


class _HealthThreshDeviceVccLimit_Type(Integer32):
    """Custom type healthThreshDeviceVccLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceVccLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceVccLimit_Object = MibScalar
healthThreshDeviceVccLimit = _HealthThreshDeviceVccLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 16),
    _HealthThreshDeviceVccLimit_Type()
)
healthThreshDeviceVccLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceVccLimit.setStatus("mandatory")


class _HealthThreshDeviceTemperatureLimit_Type(Integer32):
    """Custom type healthThreshDeviceTemperatureLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceTemperatureLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceTemperatureLimit_Object = MibScalar
healthThreshDeviceTemperatureLimit = _HealthThreshDeviceTemperatureLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 17),
    _HealthThreshDeviceTemperatureLimit_Type()
)
healthThreshDeviceTemperatureLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceTemperatureLimit.setStatus("mandatory")


class _HealthThreshDeviceVpLimit_Type(Integer32):
    """Custom type healthThreshDeviceVpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshDeviceVpLimit_Type.__name__ = "Integer32"
_HealthThreshDeviceVpLimit_Object = MibScalar
healthThreshDeviceVpLimit = _HealthThreshDeviceVpLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 6, 18),
    _HealthThreshDeviceVpLimit_Type()
)
healthThreshDeviceVpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshDeviceVpLimit.setStatus("mandatory")
_Health2DeviceInfo_ObjectIdentity = ObjectIdentity
health2DeviceInfo = _Health2DeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7)
)


class _Health2DeviceRxLatest_Type(Integer32):
    """Custom type health2DeviceRxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceRxLatest_Type.__name__ = "Integer32"
_Health2DeviceRxLatest_Object = MibScalar
health2DeviceRxLatest = _Health2DeviceRxLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 1),
    _Health2DeviceRxLatest_Type()
)
health2DeviceRxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceRxLatest.setStatus("mandatory")


class _Health2DeviceRx1MinAvg_Type(Integer32):
    """Custom type health2DeviceRx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceRx1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceRx1MinAvg_Object = MibScalar
health2DeviceRx1MinAvg = _Health2DeviceRx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 2),
    _Health2DeviceRx1MinAvg_Type()
)
health2DeviceRx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceRx1MinAvg.setStatus("mandatory")


class _Health2DeviceRx1HrAvg_Type(Integer32):
    """Custom type health2DeviceRx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceRx1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceRx1HrAvg_Object = MibScalar
health2DeviceRx1HrAvg = _Health2DeviceRx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 3),
    _Health2DeviceRx1HrAvg_Type()
)
health2DeviceRx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceRx1HrAvg.setStatus("mandatory")


class _Health2DeviceRx1HrMax_Type(Integer32):
    """Custom type health2DeviceRx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceRx1HrMax_Type.__name__ = "Integer32"
_Health2DeviceRx1HrMax_Object = MibScalar
health2DeviceRx1HrMax = _Health2DeviceRx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 4),
    _Health2DeviceRx1HrMax_Type()
)
health2DeviceRx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceRx1HrMax.setStatus("mandatory")


class _Health2DeviceRxTxLatest_Type(Integer32):
    """Custom type health2DeviceRxTxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceRxTxLatest_Type.__name__ = "Integer32"
_Health2DeviceRxTxLatest_Object = MibScalar
health2DeviceRxTxLatest = _Health2DeviceRxTxLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 5),
    _Health2DeviceRxTxLatest_Type()
)
health2DeviceRxTxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceRxTxLatest.setStatus("mandatory")


class _Health2DeviceRxTx1MinAvg_Type(Integer32):
    """Custom type health2DeviceRxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceRxTx1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceRxTx1MinAvg_Object = MibScalar
health2DeviceRxTx1MinAvg = _Health2DeviceRxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 6),
    _Health2DeviceRxTx1MinAvg_Type()
)
health2DeviceRxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceRxTx1MinAvg.setStatus("mandatory")


class _Health2DeviceRxTx1HrAvg_Type(Integer32):
    """Custom type health2DeviceRxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceRxTx1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceRxTx1HrAvg_Object = MibScalar
health2DeviceRxTx1HrAvg = _Health2DeviceRxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 7),
    _Health2DeviceRxTx1HrAvg_Type()
)
health2DeviceRxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceRxTx1HrAvg.setStatus("mandatory")


class _Health2DeviceRxTx1HrMax_Type(Integer32):
    """Custom type health2DeviceRxTx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceRxTx1HrMax_Type.__name__ = "Integer32"
_Health2DeviceRxTx1HrMax_Object = MibScalar
health2DeviceRxTx1HrMax = _Health2DeviceRxTx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 8),
    _Health2DeviceRxTx1HrMax_Type()
)
health2DeviceRxTx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceRxTx1HrMax.setStatus("mandatory")


class _Health2DeviceBackplaneLatest_Type(Integer32):
    """Custom type health2DeviceBackplaneLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceBackplaneLatest_Type.__name__ = "Integer32"
_Health2DeviceBackplaneLatest_Object = MibScalar
health2DeviceBackplaneLatest = _Health2DeviceBackplaneLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 9),
    _Health2DeviceBackplaneLatest_Type()
)
health2DeviceBackplaneLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceBackplaneLatest.setStatus("mandatory")


class _Health2DeviceBackplane1MinAvg_Type(Integer32):
    """Custom type health2DeviceBackplane1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceBackplane1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceBackplane1MinAvg_Object = MibScalar
health2DeviceBackplane1MinAvg = _Health2DeviceBackplane1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 10),
    _Health2DeviceBackplane1MinAvg_Type()
)
health2DeviceBackplane1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceBackplane1MinAvg.setStatus("mandatory")


class _Health2DeviceBackplane1HrAvg_Type(Integer32):
    """Custom type health2DeviceBackplane1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceBackplane1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceBackplane1HrAvg_Object = MibScalar
health2DeviceBackplane1HrAvg = _Health2DeviceBackplane1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 11),
    _Health2DeviceBackplane1HrAvg_Type()
)
health2DeviceBackplane1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceBackplane1HrAvg.setStatus("mandatory")


class _Health2DeviceBackplane1HrMax_Type(Integer32):
    """Custom type health2DeviceBackplane1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceBackplane1HrMax_Type.__name__ = "Integer32"
_Health2DeviceBackplane1HrMax_Object = MibScalar
health2DeviceBackplane1HrMax = _Health2DeviceBackplane1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 12),
    _Health2DeviceBackplane1HrMax_Type()
)
health2DeviceBackplane1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceBackplane1HrMax.setStatus("mandatory")


class _Health2DeviceMpmCamLatest_Type(Integer32):
    """Custom type health2DeviceMpmCamLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceMpmCamLatest_Type.__name__ = "Integer32"
_Health2DeviceMpmCamLatest_Object = MibScalar
health2DeviceMpmCamLatest = _Health2DeviceMpmCamLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 13),
    _Health2DeviceMpmCamLatest_Type()
)
health2DeviceMpmCamLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceMpmCamLatest.setStatus("mandatory")


class _Health2DeviceMpmCam1MinAvg_Type(Integer32):
    """Custom type health2DeviceMpmCam1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceMpmCam1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceMpmCam1MinAvg_Object = MibScalar
health2DeviceMpmCam1MinAvg = _Health2DeviceMpmCam1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 14),
    _Health2DeviceMpmCam1MinAvg_Type()
)
health2DeviceMpmCam1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceMpmCam1MinAvg.setStatus("mandatory")


class _Health2DeviceMpmCam1HrAvg_Type(Integer32):
    """Custom type health2DeviceMpmCam1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceMpmCam1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceMpmCam1HrAvg_Object = MibScalar
health2DeviceMpmCam1HrAvg = _Health2DeviceMpmCam1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 15),
    _Health2DeviceMpmCam1HrAvg_Type()
)
health2DeviceMpmCam1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceMpmCam1HrAvg.setStatus("mandatory")


class _Health2DeviceMpmCam1HrMax_Type(Integer32):
    """Custom type health2DeviceMpmCam1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceMpmCam1HrMax_Type.__name__ = "Integer32"
_Health2DeviceMpmCam1HrMax_Object = MibScalar
health2DeviceMpmCam1HrMax = _Health2DeviceMpmCam1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 16),
    _Health2DeviceMpmCam1HrMax_Type()
)
health2DeviceMpmCam1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceMpmCam1HrMax.setStatus("mandatory")


class _Health2DeviceHreCamLatest_Type(Integer32):
    """Custom type health2DeviceHreCamLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceHreCamLatest_Type.__name__ = "Integer32"
_Health2DeviceHreCamLatest_Object = MibScalar
health2DeviceHreCamLatest = _Health2DeviceHreCamLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 17),
    _Health2DeviceHreCamLatest_Type()
)
health2DeviceHreCamLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceHreCamLatest.setStatus("mandatory")


class _Health2DeviceHreCam1MinAvg_Type(Integer32):
    """Custom type health2DeviceHreCam1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceHreCam1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceHreCam1MinAvg_Object = MibScalar
health2DeviceHreCam1MinAvg = _Health2DeviceHreCam1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 18),
    _Health2DeviceHreCam1MinAvg_Type()
)
health2DeviceHreCam1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceHreCam1MinAvg.setStatus("mandatory")


class _Health2DeviceHreCam1HrAvg_Type(Integer32):
    """Custom type health2DeviceHreCam1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceHreCam1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceHreCam1HrAvg_Object = MibScalar
health2DeviceHreCam1HrAvg = _Health2DeviceHreCam1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 19),
    _Health2DeviceHreCam1HrAvg_Type()
)
health2DeviceHreCam1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceHreCam1HrAvg.setStatus("mandatory")


class _Health2DeviceHreCam1HrMax_Type(Integer32):
    """Custom type health2DeviceHreCam1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceHreCam1HrMax_Type.__name__ = "Integer32"
_Health2DeviceHreCam1HrMax_Object = MibScalar
health2DeviceHreCam1HrMax = _Health2DeviceHreCam1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 20),
    _Health2DeviceHreCam1HrMax_Type()
)
health2DeviceHreCam1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceHreCam1HrMax.setStatus("mandatory")


class _Health2DeviceMemoryLatest_Type(Integer32):
    """Custom type health2DeviceMemoryLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceMemoryLatest_Type.__name__ = "Integer32"
_Health2DeviceMemoryLatest_Object = MibScalar
health2DeviceMemoryLatest = _Health2DeviceMemoryLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 21),
    _Health2DeviceMemoryLatest_Type()
)
health2DeviceMemoryLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceMemoryLatest.setStatus("mandatory")


class _Health2DeviceMemory1MinAvg_Type(Integer32):
    """Custom type health2DeviceMemory1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceMemory1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceMemory1MinAvg_Object = MibScalar
health2DeviceMemory1MinAvg = _Health2DeviceMemory1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 22),
    _Health2DeviceMemory1MinAvg_Type()
)
health2DeviceMemory1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceMemory1MinAvg.setStatus("mandatory")


class _Health2DeviceMemory1HrAvg_Type(Integer32):
    """Custom type health2DeviceMemory1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceMemory1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceMemory1HrAvg_Object = MibScalar
health2DeviceMemory1HrAvg = _Health2DeviceMemory1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 23),
    _Health2DeviceMemory1HrAvg_Type()
)
health2DeviceMemory1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceMemory1HrAvg.setStatus("mandatory")


class _Health2DeviceMemory1HrMax_Type(Integer32):
    """Custom type health2DeviceMemory1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceMemory1HrMax_Type.__name__ = "Integer32"
_Health2DeviceMemory1HrMax_Object = MibScalar
health2DeviceMemory1HrMax = _Health2DeviceMemory1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 24),
    _Health2DeviceMemory1HrMax_Type()
)
health2DeviceMemory1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceMemory1HrMax.setStatus("mandatory")
_Health2DeviceNumCpus_Type = Integer32
_Health2DeviceNumCpus_Object = MibScalar
health2DeviceNumCpus = _Health2DeviceNumCpus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 25),
    _Health2DeviceNumCpus_Type()
)
health2DeviceNumCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceNumCpus.setStatus("mandatory")
_Health2DeviceCpuTable_Object = MibTable
health2DeviceCpuTable = _Health2DeviceCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 26)
)
if mibBuilder.loadTexts:
    health2DeviceCpuTable.setStatus("mandatory")
_Health2DeviceCpuEntry_Object = MibTableRow
health2DeviceCpuEntry = _Health2DeviceCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 26, 1)
)
health2DeviceCpuEntry.setIndexNames(
    (0, "XYLAN-HEALTH-MIB", "health2DeviceCpuNum"),
)
if mibBuilder.loadTexts:
    health2DeviceCpuEntry.setStatus("mandatory")
_Health2DeviceCpuNum_Type = Integer32
_Health2DeviceCpuNum_Object = MibTableColumn
health2DeviceCpuNum = _Health2DeviceCpuNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 26, 1, 1),
    _Health2DeviceCpuNum_Type()
)
health2DeviceCpuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceCpuNum.setStatus("mandatory")


class _Health2DeviceCpuLatest_Type(Integer32):
    """Custom type health2DeviceCpuLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceCpuLatest_Type.__name__ = "Integer32"
_Health2DeviceCpuLatest_Object = MibTableColumn
health2DeviceCpuLatest = _Health2DeviceCpuLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 26, 1, 2),
    _Health2DeviceCpuLatest_Type()
)
health2DeviceCpuLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceCpuLatest.setStatus("mandatory")


class _Health2DeviceCpu1MinAvg_Type(Integer32):
    """Custom type health2DeviceCpu1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceCpu1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceCpu1MinAvg_Object = MibTableColumn
health2DeviceCpu1MinAvg = _Health2DeviceCpu1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 26, 1, 3),
    _Health2DeviceCpu1MinAvg_Type()
)
health2DeviceCpu1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceCpu1MinAvg.setStatus("mandatory")


class _Health2DeviceCpu1HrAvg_Type(Integer32):
    """Custom type health2DeviceCpu1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceCpu1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceCpu1HrAvg_Object = MibTableColumn
health2DeviceCpu1HrAvg = _Health2DeviceCpu1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 26, 1, 4),
    _Health2DeviceCpu1HrAvg_Type()
)
health2DeviceCpu1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceCpu1HrAvg.setStatus("mandatory")


class _Health2DeviceCpu1HrMax_Type(Integer32):
    """Custom type health2DeviceCpu1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceCpu1HrMax_Type.__name__ = "Integer32"
_Health2DeviceCpu1HrMax_Object = MibTableColumn
health2DeviceCpu1HrMax = _Health2DeviceCpu1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 26, 1, 5),
    _Health2DeviceCpu1HrMax_Type()
)
health2DeviceCpu1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceCpu1HrMax.setStatus("mandatory")


class _Health2DeviceVccLatest_Type(Integer32):
    """Custom type health2DeviceVccLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceVccLatest_Type.__name__ = "Integer32"
_Health2DeviceVccLatest_Object = MibScalar
health2DeviceVccLatest = _Health2DeviceVccLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 27),
    _Health2DeviceVccLatest_Type()
)
health2DeviceVccLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceVccLatest.setStatus("mandatory")


class _Health2DeviceVcc1MinAvg_Type(Integer32):
    """Custom type health2DeviceVcc1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceVcc1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceVcc1MinAvg_Object = MibScalar
health2DeviceVcc1MinAvg = _Health2DeviceVcc1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 28),
    _Health2DeviceVcc1MinAvg_Type()
)
health2DeviceVcc1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceVcc1MinAvg.setStatus("mandatory")


class _Health2DeviceVcc1HrAvg_Type(Integer32):
    """Custom type health2DeviceVcc1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceVcc1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceVcc1HrAvg_Object = MibScalar
health2DeviceVcc1HrAvg = _Health2DeviceVcc1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 29),
    _Health2DeviceVcc1HrAvg_Type()
)
health2DeviceVcc1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceVcc1HrAvg.setStatus("mandatory")


class _Health2DeviceVcc1HrMax_Type(Integer32):
    """Custom type health2DeviceVcc1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceVcc1HrMax_Type.__name__ = "Integer32"
_Health2DeviceVcc1HrMax_Object = MibScalar
health2DeviceVcc1HrMax = _Health2DeviceVcc1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 30),
    _Health2DeviceVcc1HrMax_Type()
)
health2DeviceVcc1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceVcc1HrMax.setStatus("mandatory")


class _Health2DeviceTemperatureLatest_Type(Integer32):
    """Custom type health2DeviceTemperatureLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceTemperatureLatest_Type.__name__ = "Integer32"
_Health2DeviceTemperatureLatest_Object = MibScalar
health2DeviceTemperatureLatest = _Health2DeviceTemperatureLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 31),
    _Health2DeviceTemperatureLatest_Type()
)
health2DeviceTemperatureLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceTemperatureLatest.setStatus("mandatory")


class _Health2DeviceTemperature1MinAvg_Type(Integer32):
    """Custom type health2DeviceTemperature1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceTemperature1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceTemperature1MinAvg_Object = MibScalar
health2DeviceTemperature1MinAvg = _Health2DeviceTemperature1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 32),
    _Health2DeviceTemperature1MinAvg_Type()
)
health2DeviceTemperature1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceTemperature1MinAvg.setStatus("mandatory")


class _Health2DeviceTemperature1HrAvg_Type(Integer32):
    """Custom type health2DeviceTemperature1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceTemperature1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceTemperature1HrAvg_Object = MibScalar
health2DeviceTemperature1HrAvg = _Health2DeviceTemperature1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 33),
    _Health2DeviceTemperature1HrAvg_Type()
)
health2DeviceTemperature1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceTemperature1HrAvg.setStatus("mandatory")


class _Health2DeviceTemperature1HrMax_Type(Integer32):
    """Custom type health2DeviceTemperature1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceTemperature1HrMax_Type.__name__ = "Integer32"
_Health2DeviceTemperature1HrMax_Object = MibScalar
health2DeviceTemperature1HrMax = _Health2DeviceTemperature1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 34),
    _Health2DeviceTemperature1HrMax_Type()
)
health2DeviceTemperature1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceTemperature1HrMax.setStatus("mandatory")


class _Health2DeviceVpLatest_Type(Integer32):
    """Custom type health2DeviceVpLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceVpLatest_Type.__name__ = "Integer32"
_Health2DeviceVpLatest_Object = MibScalar
health2DeviceVpLatest = _Health2DeviceVpLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 35),
    _Health2DeviceVpLatest_Type()
)
health2DeviceVpLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceVpLatest.setStatus("mandatory")


class _Health2DeviceVp1MinAvg_Type(Integer32):
    """Custom type health2DeviceVp1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceVp1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceVp1MinAvg_Object = MibScalar
health2DeviceVp1MinAvg = _Health2DeviceVp1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 36),
    _Health2DeviceVp1MinAvg_Type()
)
health2DeviceVp1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceVp1MinAvg.setStatus("mandatory")


class _Health2DeviceVp1HrAvg_Type(Integer32):
    """Custom type health2DeviceVp1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceVp1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceVp1HrAvg_Object = MibScalar
health2DeviceVp1HrAvg = _Health2DeviceVp1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 37),
    _Health2DeviceVp1HrAvg_Type()
)
health2DeviceVp1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceVp1HrAvg.setStatus("mandatory")


class _Health2DeviceVp1HrMax_Type(Integer32):
    """Custom type health2DeviceVp1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceVp1HrMax_Type.__name__ = "Integer32"
_Health2DeviceVp1HrMax_Object = MibScalar
health2DeviceVp1HrMax = _Health2DeviceVp1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 38),
    _Health2DeviceVp1HrMax_Type()
)
health2DeviceVp1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceVp1HrMax.setStatus("mandatory")


class _Health2DeviceHreCollisionLatest_Type(Integer32):
    """Custom type health2DeviceHreCollisionLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceHreCollisionLatest_Type.__name__ = "Integer32"
_Health2DeviceHreCollisionLatest_Object = MibScalar
health2DeviceHreCollisionLatest = _Health2DeviceHreCollisionLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 39),
    _Health2DeviceHreCollisionLatest_Type()
)
health2DeviceHreCollisionLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceHreCollisionLatest.setStatus("mandatory")


class _Health2DeviceHreCollision1MinAvg_Type(Integer32):
    """Custom type health2DeviceHreCollision1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceHreCollision1MinAvg_Type.__name__ = "Integer32"
_Health2DeviceHreCollision1MinAvg_Object = MibScalar
health2DeviceHreCollision1MinAvg = _Health2DeviceHreCollision1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 40),
    _Health2DeviceHreCollision1MinAvg_Type()
)
health2DeviceHreCollision1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceHreCollision1MinAvg.setStatus("mandatory")


class _Health2DeviceHreCollision1HrAvg_Type(Integer32):
    """Custom type health2DeviceHreCollision1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceHreCollision1HrAvg_Type.__name__ = "Integer32"
_Health2DeviceHreCollision1HrAvg_Object = MibScalar
health2DeviceHreCollision1HrAvg = _Health2DeviceHreCollision1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 41),
    _Health2DeviceHreCollision1HrAvg_Type()
)
health2DeviceHreCollision1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceHreCollision1HrAvg.setStatus("mandatory")


class _Health2DeviceHreCollision1HrMax_Type(Integer32):
    """Custom type health2DeviceHreCollision1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2DeviceHreCollision1HrMax_Type.__name__ = "Integer32"
_Health2DeviceHreCollision1HrMax_Object = MibScalar
health2DeviceHreCollision1HrMax = _Health2DeviceHreCollision1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 7, 42),
    _Health2DeviceHreCollision1HrMax_Type()
)
health2DeviceHreCollision1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2DeviceHreCollision1HrMax.setStatus("mandatory")
_Health2ModuleInfo_ObjectIdentity = ObjectIdentity
health2ModuleInfo = _Health2ModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8)
)
_Health2ModuleTable_Object = MibTable
health2ModuleTable = _Health2ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1)
)
if mibBuilder.loadTexts:
    health2ModuleTable.setStatus("mandatory")
_Health2ModuleEntry_Object = MibTableRow
health2ModuleEntry = _Health2ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1)
)
health2ModuleEntry.setIndexNames(
    (0, "XYLAN-HEALTH-MIB", "health2ModuleSlot"),
)
if mibBuilder.loadTexts:
    health2ModuleEntry.setStatus("mandatory")
_Health2ModuleSlot_Type = Integer32
_Health2ModuleSlot_Object = MibTableColumn
health2ModuleSlot = _Health2ModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 1),
    _Health2ModuleSlot_Type()
)
health2ModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleSlot.setStatus("mandatory")


class _Health2ModuleRxLatest_Type(Integer32):
    """Custom type health2ModuleRxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleRxLatest_Type.__name__ = "Integer32"
_Health2ModuleRxLatest_Object = MibTableColumn
health2ModuleRxLatest = _Health2ModuleRxLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 2),
    _Health2ModuleRxLatest_Type()
)
health2ModuleRxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleRxLatest.setStatus("mandatory")


class _Health2ModuleRx1MinAvg_Type(Integer32):
    """Custom type health2ModuleRx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleRx1MinAvg_Type.__name__ = "Integer32"
_Health2ModuleRx1MinAvg_Object = MibTableColumn
health2ModuleRx1MinAvg = _Health2ModuleRx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 3),
    _Health2ModuleRx1MinAvg_Type()
)
health2ModuleRx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleRx1MinAvg.setStatus("mandatory")


class _Health2ModuleRx1HrAvg_Type(Integer32):
    """Custom type health2ModuleRx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleRx1HrAvg_Type.__name__ = "Integer32"
_Health2ModuleRx1HrAvg_Object = MibTableColumn
health2ModuleRx1HrAvg = _Health2ModuleRx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 4),
    _Health2ModuleRx1HrAvg_Type()
)
health2ModuleRx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleRx1HrAvg.setStatus("mandatory")


class _Health2ModuleRx1HrMax_Type(Integer32):
    """Custom type health2ModuleRx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleRx1HrMax_Type.__name__ = "Integer32"
_Health2ModuleRx1HrMax_Object = MibTableColumn
health2ModuleRx1HrMax = _Health2ModuleRx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 5),
    _Health2ModuleRx1HrMax_Type()
)
health2ModuleRx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleRx1HrMax.setStatus("mandatory")


class _Health2ModuleRxTxLatest_Type(Integer32):
    """Custom type health2ModuleRxTxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleRxTxLatest_Type.__name__ = "Integer32"
_Health2ModuleRxTxLatest_Object = MibTableColumn
health2ModuleRxTxLatest = _Health2ModuleRxTxLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 6),
    _Health2ModuleRxTxLatest_Type()
)
health2ModuleRxTxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleRxTxLatest.setStatus("mandatory")


class _Health2ModuleRxTx1MinAvg_Type(Integer32):
    """Custom type health2ModuleRxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleRxTx1MinAvg_Type.__name__ = "Integer32"
_Health2ModuleRxTx1MinAvg_Object = MibTableColumn
health2ModuleRxTx1MinAvg = _Health2ModuleRxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 7),
    _Health2ModuleRxTx1MinAvg_Type()
)
health2ModuleRxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleRxTx1MinAvg.setStatus("mandatory")


class _Health2ModuleRxTx1HrAvg_Type(Integer32):
    """Custom type health2ModuleRxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleRxTx1HrAvg_Type.__name__ = "Integer32"
_Health2ModuleRxTx1HrAvg_Object = MibTableColumn
health2ModuleRxTx1HrAvg = _Health2ModuleRxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 8),
    _Health2ModuleRxTx1HrAvg_Type()
)
health2ModuleRxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleRxTx1HrAvg.setStatus("mandatory")


class _Health2ModuleRxTx1HrMax_Type(Integer32):
    """Custom type health2ModuleRxTx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleRxTx1HrMax_Type.__name__ = "Integer32"
_Health2ModuleRxTx1HrMax_Object = MibTableColumn
health2ModuleRxTx1HrMax = _Health2ModuleRxTx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 9),
    _Health2ModuleRxTx1HrMax_Type()
)
health2ModuleRxTx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleRxTx1HrMax.setStatus("mandatory")


class _Health2ModuleBackplaneLatest_Type(Integer32):
    """Custom type health2ModuleBackplaneLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleBackplaneLatest_Type.__name__ = "Integer32"
_Health2ModuleBackplaneLatest_Object = MibTableColumn
health2ModuleBackplaneLatest = _Health2ModuleBackplaneLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 10),
    _Health2ModuleBackplaneLatest_Type()
)
health2ModuleBackplaneLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleBackplaneLatest.setStatus("mandatory")


class _Health2ModuleBackplane1MinAvg_Type(Integer32):
    """Custom type health2ModuleBackplane1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleBackplane1MinAvg_Type.__name__ = "Integer32"
_Health2ModuleBackplane1MinAvg_Object = MibTableColumn
health2ModuleBackplane1MinAvg = _Health2ModuleBackplane1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 11),
    _Health2ModuleBackplane1MinAvg_Type()
)
health2ModuleBackplane1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleBackplane1MinAvg.setStatus("mandatory")


class _Health2ModuleBackplane1HrAvg_Type(Integer32):
    """Custom type health2ModuleBackplane1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleBackplane1HrAvg_Type.__name__ = "Integer32"
_Health2ModuleBackplane1HrAvg_Object = MibTableColumn
health2ModuleBackplane1HrAvg = _Health2ModuleBackplane1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 12),
    _Health2ModuleBackplane1HrAvg_Type()
)
health2ModuleBackplane1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleBackplane1HrAvg.setStatus("mandatory")


class _Health2ModuleBackplane1HrMax_Type(Integer32):
    """Custom type health2ModuleBackplane1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleBackplane1HrMax_Type.__name__ = "Integer32"
_Health2ModuleBackplane1HrMax_Object = MibTableColumn
health2ModuleBackplane1HrMax = _Health2ModuleBackplane1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 13),
    _Health2ModuleBackplane1HrMax_Type()
)
health2ModuleBackplane1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleBackplane1HrMax.setStatus("mandatory")


class _Health2ModuleCamLatest_Type(Integer32):
    """Custom type health2ModuleCamLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleCamLatest_Type.__name__ = "Integer32"
_Health2ModuleCamLatest_Object = MibTableColumn
health2ModuleCamLatest = _Health2ModuleCamLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 14),
    _Health2ModuleCamLatest_Type()
)
health2ModuleCamLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleCamLatest.setStatus("mandatory")


class _Health2ModuleCam1MinAvg_Type(Integer32):
    """Custom type health2ModuleCam1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleCam1MinAvg_Type.__name__ = "Integer32"
_Health2ModuleCam1MinAvg_Object = MibTableColumn
health2ModuleCam1MinAvg = _Health2ModuleCam1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 15),
    _Health2ModuleCam1MinAvg_Type()
)
health2ModuleCam1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleCam1MinAvg.setStatus("mandatory")


class _Health2ModuleCam1HrAvg_Type(Integer32):
    """Custom type health2ModuleCam1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleCam1HrAvg_Type.__name__ = "Integer32"
_Health2ModuleCam1HrAvg_Object = MibTableColumn
health2ModuleCam1HrAvg = _Health2ModuleCam1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 16),
    _Health2ModuleCam1HrAvg_Type()
)
health2ModuleCam1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleCam1HrAvg.setStatus("mandatory")


class _Health2ModuleCam1HrMax_Type(Integer32):
    """Custom type health2ModuleCam1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleCam1HrMax_Type.__name__ = "Integer32"
_Health2ModuleCam1HrMax_Object = MibTableColumn
health2ModuleCam1HrMax = _Health2ModuleCam1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 17),
    _Health2ModuleCam1HrMax_Type()
)
health2ModuleCam1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleCam1HrMax.setStatus("mandatory")


class _Health2ModuleVccLatest_Type(Integer32):
    """Custom type health2ModuleVccLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleVccLatest_Type.__name__ = "Integer32"
_Health2ModuleVccLatest_Object = MibTableColumn
health2ModuleVccLatest = _Health2ModuleVccLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 18),
    _Health2ModuleVccLatest_Type()
)
health2ModuleVccLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleVccLatest.setStatus("mandatory")


class _Health2ModuleVcc1MinAvg_Type(Integer32):
    """Custom type health2ModuleVcc1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleVcc1MinAvg_Type.__name__ = "Integer32"
_Health2ModuleVcc1MinAvg_Object = MibTableColumn
health2ModuleVcc1MinAvg = _Health2ModuleVcc1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 19),
    _Health2ModuleVcc1MinAvg_Type()
)
health2ModuleVcc1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleVcc1MinAvg.setStatus("mandatory")


class _Health2ModuleVcc1HrAvg_Type(Integer32):
    """Custom type health2ModuleVcc1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleVcc1HrAvg_Type.__name__ = "Integer32"
_Health2ModuleVcc1HrAvg_Object = MibTableColumn
health2ModuleVcc1HrAvg = _Health2ModuleVcc1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 20),
    _Health2ModuleVcc1HrAvg_Type()
)
health2ModuleVcc1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleVcc1HrAvg.setStatus("mandatory")


class _Health2ModuleVcc1HrMax_Type(Integer32):
    """Custom type health2ModuleVcc1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2ModuleVcc1HrMax_Type.__name__ = "Integer32"
_Health2ModuleVcc1HrMax_Object = MibTableColumn
health2ModuleVcc1HrMax = _Health2ModuleVcc1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 8, 1, 1, 21),
    _Health2ModuleVcc1HrMax_Type()
)
health2ModuleVcc1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2ModuleVcc1HrMax.setStatus("mandatory")
_Health2PortInfo_ObjectIdentity = ObjectIdentity
health2PortInfo = _Health2PortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9)
)
_Health2PortTable_Object = MibTable
health2PortTable = _Health2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1)
)
if mibBuilder.loadTexts:
    health2PortTable.setStatus("mandatory")
_Health2PortEntry_Object = MibTableRow
health2PortEntry = _Health2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1)
)
health2PortEntry.setIndexNames(
    (0, "XYLAN-HEALTH-MIB", "health2PortSlot"),
    (0, "XYLAN-HEALTH-MIB", "health2PortIF"),
)
if mibBuilder.loadTexts:
    health2PortEntry.setStatus("mandatory")


class _Health2PortSlot_Type(Integer32):
    """Custom type health2PortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Health2PortSlot_Type.__name__ = "Integer32"
_Health2PortSlot_Object = MibTableColumn
health2PortSlot = _Health2PortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 1),
    _Health2PortSlot_Type()
)
health2PortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortSlot.setStatus("mandatory")
_Health2PortIF_Type = Integer32
_Health2PortIF_Object = MibTableColumn
health2PortIF = _Health2PortIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 2),
    _Health2PortIF_Type()
)
health2PortIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortIF.setStatus("mandatory")


class _Health2PortRxLatest_Type(Integer32):
    """Custom type health2PortRxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortRxLatest_Type.__name__ = "Integer32"
_Health2PortRxLatest_Object = MibTableColumn
health2PortRxLatest = _Health2PortRxLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 3),
    _Health2PortRxLatest_Type()
)
health2PortRxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortRxLatest.setStatus("mandatory")


class _Health2PortRx1MinAvg_Type(Integer32):
    """Custom type health2PortRx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortRx1MinAvg_Type.__name__ = "Integer32"
_Health2PortRx1MinAvg_Object = MibTableColumn
health2PortRx1MinAvg = _Health2PortRx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 4),
    _Health2PortRx1MinAvg_Type()
)
health2PortRx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortRx1MinAvg.setStatus("mandatory")


class _Health2PortRx1HrAvg_Type(Integer32):
    """Custom type health2PortRx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortRx1HrAvg_Type.__name__ = "Integer32"
_Health2PortRx1HrAvg_Object = MibTableColumn
health2PortRx1HrAvg = _Health2PortRx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 5),
    _Health2PortRx1HrAvg_Type()
)
health2PortRx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortRx1HrAvg.setStatus("mandatory")


class _Health2PortRx1HrMax_Type(Integer32):
    """Custom type health2PortRx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortRx1HrMax_Type.__name__ = "Integer32"
_Health2PortRx1HrMax_Object = MibTableColumn
health2PortRx1HrMax = _Health2PortRx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 6),
    _Health2PortRx1HrMax_Type()
)
health2PortRx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortRx1HrMax.setStatus("mandatory")


class _Health2PortRxTxLatest_Type(Integer32):
    """Custom type health2PortRxTxLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortRxTxLatest_Type.__name__ = "Integer32"
_Health2PortRxTxLatest_Object = MibTableColumn
health2PortRxTxLatest = _Health2PortRxTxLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 7),
    _Health2PortRxTxLatest_Type()
)
health2PortRxTxLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortRxTxLatest.setStatus("mandatory")


class _Health2PortRxTx1MinAvg_Type(Integer32):
    """Custom type health2PortRxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortRxTx1MinAvg_Type.__name__ = "Integer32"
_Health2PortRxTx1MinAvg_Object = MibTableColumn
health2PortRxTx1MinAvg = _Health2PortRxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 8),
    _Health2PortRxTx1MinAvg_Type()
)
health2PortRxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortRxTx1MinAvg.setStatus("mandatory")


class _Health2PortRxTx1HrAvg_Type(Integer32):
    """Custom type health2PortRxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortRxTx1HrAvg_Type.__name__ = "Integer32"
_Health2PortRxTx1HrAvg_Object = MibTableColumn
health2PortRxTx1HrAvg = _Health2PortRxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 9),
    _Health2PortRxTx1HrAvg_Type()
)
health2PortRxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortRxTx1HrAvg.setStatus("mandatory")


class _Health2PortRxTx1HrMax_Type(Integer32):
    """Custom type health2PortRxTx1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortRxTx1HrMax_Type.__name__ = "Integer32"
_Health2PortRxTx1HrMax_Object = MibTableColumn
health2PortRxTx1HrMax = _Health2PortRxTx1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 10),
    _Health2PortRxTx1HrMax_Type()
)
health2PortRxTx1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortRxTx1HrMax.setStatus("mandatory")


class _Health2PortBackplaneLatest_Type(Integer32):
    """Custom type health2PortBackplaneLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortBackplaneLatest_Type.__name__ = "Integer32"
_Health2PortBackplaneLatest_Object = MibTableColumn
health2PortBackplaneLatest = _Health2PortBackplaneLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 11),
    _Health2PortBackplaneLatest_Type()
)
health2PortBackplaneLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortBackplaneLatest.setStatus("mandatory")


class _Health2PortBackplane1MinAvg_Type(Integer32):
    """Custom type health2PortBackplane1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortBackplane1MinAvg_Type.__name__ = "Integer32"
_Health2PortBackplane1MinAvg_Object = MibTableColumn
health2PortBackplane1MinAvg = _Health2PortBackplane1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 12),
    _Health2PortBackplane1MinAvg_Type()
)
health2PortBackplane1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortBackplane1MinAvg.setStatus("mandatory")


class _Health2PortBackplane1HrAvg_Type(Integer32):
    """Custom type health2PortBackplane1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortBackplane1HrAvg_Type.__name__ = "Integer32"
_Health2PortBackplane1HrAvg_Object = MibTableColumn
health2PortBackplane1HrAvg = _Health2PortBackplane1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 13),
    _Health2PortBackplane1HrAvg_Type()
)
health2PortBackplane1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortBackplane1HrAvg.setStatus("mandatory")


class _Health2PortBackplane1HrMax_Type(Integer32):
    """Custom type health2PortBackplane1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortBackplane1HrMax_Type.__name__ = "Integer32"
_Health2PortBackplane1HrMax_Object = MibTableColumn
health2PortBackplane1HrMax = _Health2PortBackplane1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 14),
    _Health2PortBackplane1HrMax_Type()
)
health2PortBackplane1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortBackplane1HrMax.setStatus("mandatory")


class _Health2PortVccLatest_Type(Integer32):
    """Custom type health2PortVccLatest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortVccLatest_Type.__name__ = "Integer32"
_Health2PortVccLatest_Object = MibTableColumn
health2PortVccLatest = _Health2PortVccLatest_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 15),
    _Health2PortVccLatest_Type()
)
health2PortVccLatest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortVccLatest.setStatus("mandatory")


class _Health2PortVcc1MinAvg_Type(Integer32):
    """Custom type health2PortVcc1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortVcc1MinAvg_Type.__name__ = "Integer32"
_Health2PortVcc1MinAvg_Object = MibTableColumn
health2PortVcc1MinAvg = _Health2PortVcc1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 16),
    _Health2PortVcc1MinAvg_Type()
)
health2PortVcc1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortVcc1MinAvg.setStatus("mandatory")


class _Health2PortVcc1HrAvg_Type(Integer32):
    """Custom type health2PortVcc1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortVcc1HrAvg_Type.__name__ = "Integer32"
_Health2PortVcc1HrAvg_Object = MibTableColumn
health2PortVcc1HrAvg = _Health2PortVcc1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 17),
    _Health2PortVcc1HrAvg_Type()
)
health2PortVcc1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortVcc1HrAvg.setStatus("mandatory")


class _Health2PortVcc1HrMax_Type(Integer32):
    """Custom type health2PortVcc1HrMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Health2PortVcc1HrMax_Type.__name__ = "Integer32"
_Health2PortVcc1HrMax_Object = MibTableColumn
health2PortVcc1HrMax = _Health2PortVcc1HrMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 18, 9, 1, 1, 18),
    _Health2PortVcc1HrMax_Type()
)
health2PortVcc1HrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    health2PortVcc1HrMax.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-HEALTH-MIB",
    **{"HealthPortUpDownStatus": HealthPortUpDownStatus,
       "healthDeviceInfo": healthDeviceInfo,
       "healthDeviceRxData": healthDeviceRxData,
       "healthDeviceRxTimeDelta": healthDeviceRxTimeDelta,
       "healthDeviceRxTxData": healthDeviceRxTxData,
       "healthDeviceRxTxTimeDelta": healthDeviceRxTxTimeDelta,
       "healthDeviceBackplaneData": healthDeviceBackplaneData,
       "healthDeviceBackplaneTimeDelta": healthDeviceBackplaneTimeDelta,
       "healthDeviceCamData": healthDeviceCamData,
       "healthDeviceCamTimeDelta": healthDeviceCamTimeDelta,
       "healthDeviceMemoryData": healthDeviceMemoryData,
       "healthDeviceMemoryTimeDelta": healthDeviceMemoryTimeDelta,
       "healthDeviceCpuData": healthDeviceCpuData,
       "healthDeviceCpuTimeDelta": healthDeviceCpuTimeDelta,
       "healthDeviceNumCpus": healthDeviceNumCpus,
       "healthDeviceMemoryTotal": healthDeviceMemoryTotal,
       "healthDeviceMemoryFree": healthDeviceMemoryFree,
       "healthDeviceMpmCamTotal": healthDeviceMpmCamTotal,
       "healthDeviceMpmCamFree": healthDeviceMpmCamFree,
       "healthDeviceHreCamTotal": healthDeviceHreCamTotal,
       "healthDeviceHreCamFree": healthDeviceHreCamFree,
       "healthDeviceTemp": healthDeviceTemp,
       "healthDeviceIPRouteCacheFlushCount": healthDeviceIPRouteCacheFlushCount,
       "healthDeviceIPXRouteCacheFlushCount": healthDeviceIPXRouteCacheFlushCount,
       "healthDeviceMpmRxOverrunCount": healthDeviceMpmRxOverrunCount,
       "healthDeviceMpmTxOverrunCount": healthDeviceMpmTxOverrunCount,
       "healthDeviceVccData": healthDeviceVccData,
       "healthDeviceVccTimeDelta": healthDeviceVccTimeDelta,
       "healthDeviceTemperatureData": healthDeviceTemperatureData,
       "healthDeviceTemperatureTimeDelta": healthDeviceTemperatureTimeDelta,
       "healthDeviceVpData": healthDeviceVpData,
       "healthDeviceVpTimeDelta": healthDeviceVpTimeDelta,
       "healthDeviceHreCollisionTotal": healthDeviceHreCollisionTotal,
       "healthDeviceHreCollisionFree": healthDeviceHreCollisionFree,
       "healthModuleInfo": healthModuleInfo,
       "healthModuleTable": healthModuleTable,
       "healthModuleEntry": healthModuleEntry,
       "healthModuleSlot": healthModuleSlot,
       "healthModuleRxData": healthModuleRxData,
       "healthModuleRxTimeDelta": healthModuleRxTimeDelta,
       "healthModuleRxTxData": healthModuleRxTxData,
       "healthModuleRxTxTimeDelta": healthModuleRxTxTimeDelta,
       "healthModuleBackplaneData": healthModuleBackplaneData,
       "healthModuleBackplaneTimeDelta": healthModuleBackplaneTimeDelta,
       "healthModuleCamData": healthModuleCamData,
       "healthModuleCamTimeDelta": healthModuleCamTimeDelta,
       "healthModuleCamNumInstalled": healthModuleCamNumInstalled,
       "healthModuleCamConfigured": healthModuleCamConfigured,
       "healthModuleCamAvail": healthModuleCamAvail,
       "healthModuleCamAvailNonIntern": healthModuleCamAvailNonIntern,
       "healthModuleCamFree": healthModuleCamFree,
       "healthModuleVccData": healthModuleVccData,
       "healthModuleVccTimeDelta": healthModuleVccTimeDelta,
       "healthPortInfo": healthPortInfo,
       "healthPortMax": healthPortMax,
       "healthPortTable": healthPortTable,
       "healthPortEntry": healthPortEntry,
       "healthPortSlot": healthPortSlot,
       "healthPortIF": healthPortIF,
       "healthPortUpDn": healthPortUpDn,
       "healthPortRxData": healthPortRxData,
       "healthPortRxTimeDelta": healthPortRxTimeDelta,
       "healthPortRxTxData": healthPortRxTxData,
       "healthPortRxTxTimeDelta": healthPortRxTxTimeDelta,
       "healthPortBackplaneData": healthPortBackplaneData,
       "healthPortBackplaneTimeDelta": healthPortBackplaneTimeDelta,
       "healthPortVccData": healthPortVccData,
       "healthPortVccTimeDelta": healthPortVccTimeDelta,
       "healthGroupInfo": healthGroupInfo,
       "healthControlInfo": healthControlInfo,
       "healthSamplingInterval": healthSamplingInterval,
       "healthSamplingReset": healthSamplingReset,
       "healthThreshInfo": healthThreshInfo,
       "healthThreshDeviceRxLimit": healthThreshDeviceRxLimit,
       "healthThreshDeviceRxTxLimit": healthThreshDeviceRxTxLimit,
       "healthThreshDeviceBackplaneLimit": healthThreshDeviceBackplaneLimit,
       "healthThreshDeviceCamLimit": healthThreshDeviceCamLimit,
       "healthThreshDeviceMemoryLimit": healthThreshDeviceMemoryLimit,
       "healthThreshDeviceCpuLimit": healthThreshDeviceCpuLimit,
       "healthThreshDeviceSummary": healthThreshDeviceSummary,
       "healthThreshModuleSummaryTable": healthThreshModuleSummaryTable,
       "healthThreshModuleSummaryEntry": healthThreshModuleSummaryEntry,
       "healthThreshModuleSummarySlot": healthThreshModuleSummarySlot,
       "healthThreshModuleSummaryData": healthThreshModuleSummaryData,
       "healthThreshDevTrapData": healthThreshDevTrapData,
       "healthThreshModTrapCount": healthThreshModTrapCount,
       "healthThreshModTrapData": healthThreshModTrapData,
       "healthThreshPortSummaryTable": healthThreshPortSummaryTable,
       "healthThreshPortSummaryEntry": healthThreshPortSummaryEntry,
       "healthThreshPortSummarySlot": healthThreshPortSummarySlot,
       "healthThreshPortSummaryIF": healthThreshPortSummaryIF,
       "healthThreshPortSummaryData": healthThreshPortSummaryData,
       "healthThreshPortTrapSlot": healthThreshPortTrapSlot,
       "healthThreshPortTrapCount": healthThreshPortTrapCount,
       "healthThreshPortTrapData": healthThreshPortTrapData,
       "healthThreshDeviceVccLimit": healthThreshDeviceVccLimit,
       "healthThreshDeviceTemperatureLimit": healthThreshDeviceTemperatureLimit,
       "healthThreshDeviceVpLimit": healthThreshDeviceVpLimit,
       "health2DeviceInfo": health2DeviceInfo,
       "health2DeviceRxLatest": health2DeviceRxLatest,
       "health2DeviceRx1MinAvg": health2DeviceRx1MinAvg,
       "health2DeviceRx1HrAvg": health2DeviceRx1HrAvg,
       "health2DeviceRx1HrMax": health2DeviceRx1HrMax,
       "health2DeviceRxTxLatest": health2DeviceRxTxLatest,
       "health2DeviceRxTx1MinAvg": health2DeviceRxTx1MinAvg,
       "health2DeviceRxTx1HrAvg": health2DeviceRxTx1HrAvg,
       "health2DeviceRxTx1HrMax": health2DeviceRxTx1HrMax,
       "health2DeviceBackplaneLatest": health2DeviceBackplaneLatest,
       "health2DeviceBackplane1MinAvg": health2DeviceBackplane1MinAvg,
       "health2DeviceBackplane1HrAvg": health2DeviceBackplane1HrAvg,
       "health2DeviceBackplane1HrMax": health2DeviceBackplane1HrMax,
       "health2DeviceMpmCamLatest": health2DeviceMpmCamLatest,
       "health2DeviceMpmCam1MinAvg": health2DeviceMpmCam1MinAvg,
       "health2DeviceMpmCam1HrAvg": health2DeviceMpmCam1HrAvg,
       "health2DeviceMpmCam1HrMax": health2DeviceMpmCam1HrMax,
       "health2DeviceHreCamLatest": health2DeviceHreCamLatest,
       "health2DeviceHreCam1MinAvg": health2DeviceHreCam1MinAvg,
       "health2DeviceHreCam1HrAvg": health2DeviceHreCam1HrAvg,
       "health2DeviceHreCam1HrMax": health2DeviceHreCam1HrMax,
       "health2DeviceMemoryLatest": health2DeviceMemoryLatest,
       "health2DeviceMemory1MinAvg": health2DeviceMemory1MinAvg,
       "health2DeviceMemory1HrAvg": health2DeviceMemory1HrAvg,
       "health2DeviceMemory1HrMax": health2DeviceMemory1HrMax,
       "health2DeviceNumCpus": health2DeviceNumCpus,
       "health2DeviceCpuTable": health2DeviceCpuTable,
       "health2DeviceCpuEntry": health2DeviceCpuEntry,
       "health2DeviceCpuNum": health2DeviceCpuNum,
       "health2DeviceCpuLatest": health2DeviceCpuLatest,
       "health2DeviceCpu1MinAvg": health2DeviceCpu1MinAvg,
       "health2DeviceCpu1HrAvg": health2DeviceCpu1HrAvg,
       "health2DeviceCpu1HrMax": health2DeviceCpu1HrMax,
       "health2DeviceVccLatest": health2DeviceVccLatest,
       "health2DeviceVcc1MinAvg": health2DeviceVcc1MinAvg,
       "health2DeviceVcc1HrAvg": health2DeviceVcc1HrAvg,
       "health2DeviceVcc1HrMax": health2DeviceVcc1HrMax,
       "health2DeviceTemperatureLatest": health2DeviceTemperatureLatest,
       "health2DeviceTemperature1MinAvg": health2DeviceTemperature1MinAvg,
       "health2DeviceTemperature1HrAvg": health2DeviceTemperature1HrAvg,
       "health2DeviceTemperature1HrMax": health2DeviceTemperature1HrMax,
       "health2DeviceVpLatest": health2DeviceVpLatest,
       "health2DeviceVp1MinAvg": health2DeviceVp1MinAvg,
       "health2DeviceVp1HrAvg": health2DeviceVp1HrAvg,
       "health2DeviceVp1HrMax": health2DeviceVp1HrMax,
       "health2DeviceHreCollisionLatest": health2DeviceHreCollisionLatest,
       "health2DeviceHreCollision1MinAvg": health2DeviceHreCollision1MinAvg,
       "health2DeviceHreCollision1HrAvg": health2DeviceHreCollision1HrAvg,
       "health2DeviceHreCollision1HrMax": health2DeviceHreCollision1HrMax,
       "health2ModuleInfo": health2ModuleInfo,
       "health2ModuleTable": health2ModuleTable,
       "health2ModuleEntry": health2ModuleEntry,
       "health2ModuleSlot": health2ModuleSlot,
       "health2ModuleRxLatest": health2ModuleRxLatest,
       "health2ModuleRx1MinAvg": health2ModuleRx1MinAvg,
       "health2ModuleRx1HrAvg": health2ModuleRx1HrAvg,
       "health2ModuleRx1HrMax": health2ModuleRx1HrMax,
       "health2ModuleRxTxLatest": health2ModuleRxTxLatest,
       "health2ModuleRxTx1MinAvg": health2ModuleRxTx1MinAvg,
       "health2ModuleRxTx1HrAvg": health2ModuleRxTx1HrAvg,
       "health2ModuleRxTx1HrMax": health2ModuleRxTx1HrMax,
       "health2ModuleBackplaneLatest": health2ModuleBackplaneLatest,
       "health2ModuleBackplane1MinAvg": health2ModuleBackplane1MinAvg,
       "health2ModuleBackplane1HrAvg": health2ModuleBackplane1HrAvg,
       "health2ModuleBackplane1HrMax": health2ModuleBackplane1HrMax,
       "health2ModuleCamLatest": health2ModuleCamLatest,
       "health2ModuleCam1MinAvg": health2ModuleCam1MinAvg,
       "health2ModuleCam1HrAvg": health2ModuleCam1HrAvg,
       "health2ModuleCam1HrMax": health2ModuleCam1HrMax,
       "health2ModuleVccLatest": health2ModuleVccLatest,
       "health2ModuleVcc1MinAvg": health2ModuleVcc1MinAvg,
       "health2ModuleVcc1HrAvg": health2ModuleVcc1HrAvg,
       "health2ModuleVcc1HrMax": health2ModuleVcc1HrMax,
       "health2PortInfo": health2PortInfo,
       "health2PortTable": health2PortTable,
       "health2PortEntry": health2PortEntry,
       "health2PortSlot": health2PortSlot,
       "health2PortIF": health2PortIF,
       "health2PortRxLatest": health2PortRxLatest,
       "health2PortRx1MinAvg": health2PortRx1MinAvg,
       "health2PortRx1HrAvg": health2PortRx1HrAvg,
       "health2PortRx1HrMax": health2PortRx1HrMax,
       "health2PortRxTxLatest": health2PortRxTxLatest,
       "health2PortRxTx1MinAvg": health2PortRxTx1MinAvg,
       "health2PortRxTx1HrAvg": health2PortRxTx1HrAvg,
       "health2PortRxTx1HrMax": health2PortRxTx1HrMax,
       "health2PortBackplaneLatest": health2PortBackplaneLatest,
       "health2PortBackplane1MinAvg": health2PortBackplane1MinAvg,
       "health2PortBackplane1HrAvg": health2PortBackplane1HrAvg,
       "health2PortBackplane1HrMax": health2PortBackplane1HrMax,
       "health2PortVccLatest": health2PortVccLatest,
       "health2PortVcc1MinAvg": health2PortVcc1MinAvg,
       "health2PortVcc1HrAvg": health2PortVcc1HrAvg,
       "health2PortVcc1HrMax": health2PortVcc1HrMax}
)
