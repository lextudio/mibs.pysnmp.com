# SNMP MIB module (HH3C-MDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MDC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:06 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cMDC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136)
)
hh3cMDC.setRevisions(
        ("2013-03-05 14:48",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cMdcActionValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )



class Hh3cMdcRunStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 3),
          ("inactive", 1),
          ("starting", 2),
          ("stopping", 4),
          ("updating", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cMDCScalarObjects_ObjectIdentity = ObjectIdentity
hh3cMDCScalarObjects = _Hh3cMDCScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 1)
)
_Hh3cMDCMaxMDCNum_Type = Integer32
_Hh3cMDCMaxMDCNum_Object = MibScalar
hh3cMDCMaxMDCNum = _Hh3cMDCMaxMDCNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 1, 1),
    _Hh3cMDCMaxMDCNum_Type()
)
hh3cMDCMaxMDCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCMaxMDCNum.setStatus("current")
_Hh3cMDCCurrentMDCNum_Type = Integer32
_Hh3cMDCCurrentMDCNum_Object = MibScalar
hh3cMDCCurrentMDCNum = _Hh3cMDCCurrentMDCNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 1, 2),
    _Hh3cMDCCurrentMDCNum_Type()
)
hh3cMDCCurrentMDCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCCurrentMDCNum.setStatus("current")
_Hh3cMDCTables_ObjectIdentity = ObjectIdentity
hh3cMDCTables = _Hh3cMDCTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2)
)
_Hh3cMDCControl_ObjectIdentity = ObjectIdentity
hh3cMDCControl = _Hh3cMDCControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 1)
)
_Hh3cMDCControlTable_Object = MibTable
hh3cMDCControlTable = _Hh3cMDCControlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cMDCControlTable.setStatus("current")
_Hh3cMDCControlEntry_Object = MibTableRow
hh3cMDCControlEntry = _Hh3cMDCControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 1, 1, 1)
)
hh3cMDCControlEntry.setIndexNames(
    (0, "HH3C-MDC-MIB", "hh3cMDCIndex"),
)
if mibBuilder.loadTexts:
    hh3cMDCControlEntry.setStatus("current")


class _Hh3cMDCIndex_Type(Integer32):
    """Custom type hh3cMDCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cMDCIndex_Type.__name__ = "Integer32"
_Hh3cMDCIndex_Object = MibTableColumn
hh3cMDCIndex = _Hh3cMDCIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 1, 1, 1, 1),
    _Hh3cMDCIndex_Type()
)
hh3cMDCIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMDCIndex.setStatus("current")


class _Hh3cMDCName_Type(DisplayString):
    """Custom type hh3cMDCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cMDCName_Type.__name__ = "DisplayString"
_Hh3cMDCName_Object = MibTableColumn
hh3cMDCName = _Hh3cMDCName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 1, 1, 1, 2),
    _Hh3cMDCName_Type()
)
hh3cMDCName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMDCName.setStatus("current")


class _Hh3cMDCAction_Type(Hh3cMdcActionValue):
    """Custom type hh3cMDCAction based on Hh3cMdcActionValue"""


_Hh3cMDCAction_Object = MibTableColumn
hh3cMDCAction = _Hh3cMDCAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 1, 1, 1, 3),
    _Hh3cMDCAction_Type()
)
hh3cMDCAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMDCAction.setStatus("current")
_Hh3cMDCStatus_Type = Hh3cMdcRunStatus
_Hh3cMDCStatus_Object = MibTableColumn
hh3cMDCStatus = _Hh3cMDCStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 1, 1, 1, 4),
    _Hh3cMDCStatus_Type()
)
hh3cMDCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCStatus.setStatus("current")
_Hh3cMDCRowStatus_Type = RowStatus
_Hh3cMDCRowStatus_Object = MibTableColumn
hh3cMDCRowStatus = _Hh3cMDCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 1, 1, 1, 5),
    _Hh3cMDCRowStatus_Type()
)
hh3cMDCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMDCRowStatus.setStatus("current")
_Hh3cMDCResource_ObjectIdentity = ObjectIdentity
hh3cMDCResource = _Hh3cMDCResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2)
)
_Hh3cMDCDISKResourceTable_Object = MibTable
hh3cMDCDISKResourceTable = _Hh3cMDCDISKResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceTable.setStatus("current")
_Hh3cMDCDISKResourceEntry_Object = MibTableRow
hh3cMDCDISKResourceEntry = _Hh3cMDCDISKResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 1, 1)
)
hh3cMDCDISKResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HH3C-MDC-MIB", "hh3cMDCIndex"),
    (0, "HH3C-MDC-MIB", "hh3cMDCDISKResourceInstance"),
)
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceEntry.setStatus("current")


class _Hh3cMDCDISKResourceInstance_Type(Integer32):
    """Custom type hh3cMDCDISKResourceInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cMDCDISKResourceInstance_Type.__name__ = "Integer32"
_Hh3cMDCDISKResourceInstance_Object = MibTableColumn
hh3cMDCDISKResourceInstance = _Hh3cMDCDISKResourceInstance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 1, 1, 1),
    _Hh3cMDCDISKResourceInstance_Type()
)
hh3cMDCDISKResourceInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceInstance.setStatus("current")


class _Hh3cMDCDISKResourceInstanceName_Type(DisplayString):
    """Custom type hh3cMDCDISKResourceInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cMDCDISKResourceInstanceName_Type.__name__ = "DisplayString"
_Hh3cMDCDISKResourceInstanceName_Object = MibTableColumn
hh3cMDCDISKResourceInstanceName = _Hh3cMDCDISKResourceInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 1, 1, 2),
    _Hh3cMDCDISKResourceInstanceName_Type()
)
hh3cMDCDISKResourceInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceInstanceName.setStatus("current")


class _Hh3cMDCDISKResourceMinLimit_Type(Integer32):
    """Custom type hh3cMDCDISKResourceMinLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cMDCDISKResourceMinLimit_Type.__name__ = "Integer32"
_Hh3cMDCDISKResourceMinLimit_Object = MibTableColumn
hh3cMDCDISKResourceMinLimit = _Hh3cMDCDISKResourceMinLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 1, 1, 3),
    _Hh3cMDCDISKResourceMinLimit_Type()
)
hh3cMDCDISKResourceMinLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceMinLimit.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceMinLimit.setUnits("percent")


class _Hh3cMDCDISKResourceMaxLimit_Type(Integer32):
    """Custom type hh3cMDCDISKResourceMaxLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cMDCDISKResourceMaxLimit_Type.__name__ = "Integer32"
_Hh3cMDCDISKResourceMaxLimit_Object = MibTableColumn
hh3cMDCDISKResourceMaxLimit = _Hh3cMDCDISKResourceMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 1, 1, 4),
    _Hh3cMDCDISKResourceMaxLimit_Type()
)
hh3cMDCDISKResourceMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceMaxLimit.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceMaxLimit.setUnits("percent")
_Hh3cMDCDISKResourceReserve_Type = Unsigned32
_Hh3cMDCDISKResourceReserve_Object = MibTableColumn
hh3cMDCDISKResourceReserve = _Hh3cMDCDISKResourceReserve_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 1, 1, 5),
    _Hh3cMDCDISKResourceReserve_Type()
)
hh3cMDCDISKResourceReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceReserve.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceReserve.setUnits("KB")
_Hh3cMDCDISKResourceQuota_Type = Unsigned32
_Hh3cMDCDISKResourceQuota_Object = MibTableColumn
hh3cMDCDISKResourceQuota = _Hh3cMDCDISKResourceQuota_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 1, 1, 6),
    _Hh3cMDCDISKResourceQuota_Type()
)
hh3cMDCDISKResourceQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceQuota.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceQuota.setUnits("KB")
_Hh3cMDCDISKResourceUsage_Type = Unsigned32
_Hh3cMDCDISKResourceUsage_Object = MibTableColumn
hh3cMDCDISKResourceUsage = _Hh3cMDCDISKResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 1, 1, 7),
    _Hh3cMDCDISKResourceUsage_Type()
)
hh3cMDCDISKResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceUsage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceUsage.setUnits("KB")
_Hh3cMDCDISKResourceAvailable_Type = Unsigned32
_Hh3cMDCDISKResourceAvailable_Object = MibTableColumn
hh3cMDCDISKResourceAvailable = _Hh3cMDCDISKResourceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 1, 1, 8),
    _Hh3cMDCDISKResourceAvailable_Type()
)
hh3cMDCDISKResourceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceAvailable.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCDISKResourceAvailable.setUnits("KB")
_Hh3cMDCMemoryResourceTable_Object = MibTable
hh3cMDCMemoryResourceTable = _Hh3cMDCMemoryResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceTable.setStatus("current")
_Hh3cMDCMemoryResourceEntry_Object = MibTableRow
hh3cMDCMemoryResourceEntry = _Hh3cMDCMemoryResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 2, 1)
)
hh3cMDCMemoryResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HH3C-MDC-MIB", "hh3cMDCIndex"),
)
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceEntry.setStatus("current")


class _Hh3cMDCMemoryResourceMinLimit_Type(Integer32):
    """Custom type hh3cMDCMemoryResourceMinLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cMDCMemoryResourceMinLimit_Type.__name__ = "Integer32"
_Hh3cMDCMemoryResourceMinLimit_Object = MibTableColumn
hh3cMDCMemoryResourceMinLimit = _Hh3cMDCMemoryResourceMinLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 2, 1, 1),
    _Hh3cMDCMemoryResourceMinLimit_Type()
)
hh3cMDCMemoryResourceMinLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceMinLimit.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceMinLimit.setUnits("percent")


class _Hh3cMDCMemoryResourceMaxLimit_Type(Integer32):
    """Custom type hh3cMDCMemoryResourceMaxLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cMDCMemoryResourceMaxLimit_Type.__name__ = "Integer32"
_Hh3cMDCMemoryResourceMaxLimit_Object = MibTableColumn
hh3cMDCMemoryResourceMaxLimit = _Hh3cMDCMemoryResourceMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 2, 1, 2),
    _Hh3cMDCMemoryResourceMaxLimit_Type()
)
hh3cMDCMemoryResourceMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceMaxLimit.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceMaxLimit.setUnits("percent")
_Hh3cMDCMemoryResourceReserve_Type = Unsigned32
_Hh3cMDCMemoryResourceReserve_Object = MibTableColumn
hh3cMDCMemoryResourceReserve = _Hh3cMDCMemoryResourceReserve_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 2, 1, 3),
    _Hh3cMDCMemoryResourceReserve_Type()
)
hh3cMDCMemoryResourceReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceReserve.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceReserve.setUnits("KB")
_Hh3cMDCMemoryResourceQuota_Type = Unsigned32
_Hh3cMDCMemoryResourceQuota_Object = MibTableColumn
hh3cMDCMemoryResourceQuota = _Hh3cMDCMemoryResourceQuota_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 2, 1, 4),
    _Hh3cMDCMemoryResourceQuota_Type()
)
hh3cMDCMemoryResourceQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceQuota.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceQuota.setUnits("KB")
_Hh3cMDCMemoryResourceUsage_Type = Unsigned32
_Hh3cMDCMemoryResourceUsage_Object = MibTableColumn
hh3cMDCMemoryResourceUsage = _Hh3cMDCMemoryResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 2, 1, 5),
    _Hh3cMDCMemoryResourceUsage_Type()
)
hh3cMDCMemoryResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceUsage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceUsage.setUnits("KB")
_Hh3cMDCMemoryResourceAvailable_Type = Unsigned32
_Hh3cMDCMemoryResourceAvailable_Object = MibTableColumn
hh3cMDCMemoryResourceAvailable = _Hh3cMDCMemoryResourceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 2, 1, 6),
    _Hh3cMDCMemoryResourceAvailable_Type()
)
hh3cMDCMemoryResourceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceAvailable.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCMemoryResourceAvailable.setUnits("KB")
_Hh3cMDCCPUResourceTable_Object = MibTable
hh3cMDCCPUResourceTable = _Hh3cMDCCPUResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cMDCCPUResourceTable.setStatus("current")
_Hh3cMDCCPUResourceEntry_Object = MibTableRow
hh3cMDCCPUResourceEntry = _Hh3cMDCCPUResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 3, 1)
)
hh3cMDCCPUResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HH3C-MDC-MIB", "hh3cMDCIndex"),
)
if mibBuilder.loadTexts:
    hh3cMDCCPUResourceEntry.setStatus("current")


class _Hh3cMDCCPUResourceLimit_Type(Integer32):
    """Custom type hh3cMDCCPUResourceLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3cMDCCPUResourceLimit_Type.__name__ = "Integer32"
_Hh3cMDCCPUResourceLimit_Object = MibTableColumn
hh3cMDCCPUResourceLimit = _Hh3cMDCCPUResourceLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 3, 1, 1),
    _Hh3cMDCCPUResourceLimit_Type()
)
hh3cMDCCPUResourceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMDCCPUResourceLimit.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCCPUResourceLimit.setUnits("weight")


class _Hh3cMDCCPUResourceUsage_Type(Integer32):
    """Custom type hh3cMDCCPUResourceUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cMDCCPUResourceUsage_Type.__name__ = "Integer32"
_Hh3cMDCCPUResourceUsage_Object = MibTableColumn
hh3cMDCCPUResourceUsage = _Hh3cMDCCPUResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 2, 3, 1, 2),
    _Hh3cMDCCPUResourceUsage_Type()
)
hh3cMDCCPUResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCCPUResourceUsage.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMDCCPUResourceUsage.setUnits("percent")
_Hh3cMDCLocation_ObjectIdentity = ObjectIdentity
hh3cMDCLocation = _Hh3cMDCLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 3)
)
_Hh3cMDCLocationTable_Object = MibTable
hh3cMDCLocationTable = _Hh3cMDCLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cMDCLocationTable.setStatus("current")
_Hh3cMDCLocationEntry_Object = MibTableRow
hh3cMDCLocationEntry = _Hh3cMDCLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 3, 1, 1)
)
hh3cMDCLocationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HH3C-MDC-MIB", "hh3cMDCIndex"),
)
if mibBuilder.loadTexts:
    hh3cMDCLocationEntry.setStatus("current")
_Hh3cMDCLocationStatus_Type = TruthValue
_Hh3cMDCLocationStatus_Object = MibTableColumn
hh3cMDCLocationStatus = _Hh3cMDCLocationStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 3, 1, 1, 1),
    _Hh3cMDCLocationStatus_Type()
)
hh3cMDCLocationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMDCLocationStatus.setStatus("current")
_Hh3cMDCAllocate_ObjectIdentity = ObjectIdentity
hh3cMDCAllocate = _Hh3cMDCAllocate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 4)
)
_Hh3cMDCGroupIfTable_Object = MibTable
hh3cMDCGroupIfTable = _Hh3cMDCGroupIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cMDCGroupIfTable.setStatus("current")
_Hh3cMDCGroupIfEntry_Object = MibTableRow
hh3cMDCGroupIfEntry = _Hh3cMDCGroupIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 4, 1, 1)
)
hh3cMDCGroupIfEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cMDCGroupIfEntry.setStatus("current")
_Hh3cMDCGroupIdentity_Type = Integer32
_Hh3cMDCGroupIdentity_Object = MibTableColumn
hh3cMDCGroupIdentity = _Hh3cMDCGroupIdentity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 4, 1, 1, 2),
    _Hh3cMDCGroupIdentity_Type()
)
hh3cMDCGroupIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCGroupIdentity.setStatus("current")
_Hh3cMDCAllocateTable_Object = MibTable
hh3cMDCAllocateTable = _Hh3cMDCAllocateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cMDCAllocateTable.setStatus("current")
_Hh3cMDCAllocateEntry_Object = MibTableRow
hh3cMDCAllocateEntry = _Hh3cMDCAllocateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 4, 2, 1)
)
hh3cMDCAllocateEntry.setIndexNames(
    (0, "HH3C-MDC-MIB", "hh3cMDCAllocateGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cMDCAllocateEntry.setStatus("current")


class _Hh3cMDCAllocateGroupIndex_Type(Integer32):
    """Custom type hh3cMDCAllocateGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cMDCAllocateGroupIndex_Type.__name__ = "Integer32"
_Hh3cMDCAllocateGroupIndex_Object = MibTableColumn
hh3cMDCAllocateGroupIndex = _Hh3cMDCAllocateGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 4, 2, 1, 1),
    _Hh3cMDCAllocateGroupIndex_Type()
)
hh3cMDCAllocateGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMDCAllocateGroupIndex.setStatus("current")


class _Hh3cMDCAllocateGroupDescription_Type(DisplayString):
    """Custom type hh3cMDCAllocateGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cMDCAllocateGroupDescription_Type.__name__ = "DisplayString"
_Hh3cMDCAllocateGroupDescription_Object = MibTableColumn
hh3cMDCAllocateGroupDescription = _Hh3cMDCAllocateGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 4, 2, 1, 2),
    _Hh3cMDCAllocateGroupDescription_Type()
)
hh3cMDCAllocateGroupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMDCAllocateGroupDescription.setStatus("current")


class _Hh3cMDCAllocateMDCId_Type(Integer32):
    """Custom type hh3cMDCAllocateMDCId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cMDCAllocateMDCId_Type.__name__ = "Integer32"
_Hh3cMDCAllocateMDCId_Object = MibTableColumn
hh3cMDCAllocateMDCId = _Hh3cMDCAllocateMDCId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 2, 4, 2, 1, 3),
    _Hh3cMDCAllocateMDCId_Type()
)
hh3cMDCAllocateMDCId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMDCAllocateMDCId.setStatus("current")
_Hh3cMDCNotification_ObjectIdentity = ObjectIdentity
hh3cMDCNotification = _Hh3cMDCNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 3)
)
_Hh3cMDCNotificationObjects_ObjectIdentity = ObjectIdentity
hh3cMDCNotificationObjects = _Hh3cMDCNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cMDCStateChangeToActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 3, 0, 1)
)
hh3cMDCStateChangeToActive.setObjects(
      *(("HH3C-MDC-MIB", "hh3cMDCIndex"),
        ("HH3C-MDC-MIB", "hh3cMDCName"))
)
if mibBuilder.loadTexts:
    hh3cMDCStateChangeToActive.setStatus(
        "current"
    )

hh3cMDCStateChangeToInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 136, 3, 0, 2)
)
hh3cMDCStateChangeToInactive.setObjects(
      *(("HH3C-MDC-MIB", "hh3cMDCIndex"),
        ("HH3C-MDC-MIB", "hh3cMDCName"))
)
if mibBuilder.loadTexts:
    hh3cMDCStateChangeToInactive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MDC-MIB",
    **{"Hh3cMdcActionValue": Hh3cMdcActionValue,
       "Hh3cMdcRunStatus": Hh3cMdcRunStatus,
       "hh3cMDC": hh3cMDC,
       "hh3cMDCScalarObjects": hh3cMDCScalarObjects,
       "hh3cMDCMaxMDCNum": hh3cMDCMaxMDCNum,
       "hh3cMDCCurrentMDCNum": hh3cMDCCurrentMDCNum,
       "hh3cMDCTables": hh3cMDCTables,
       "hh3cMDCControl": hh3cMDCControl,
       "hh3cMDCControlTable": hh3cMDCControlTable,
       "hh3cMDCControlEntry": hh3cMDCControlEntry,
       "hh3cMDCIndex": hh3cMDCIndex,
       "hh3cMDCName": hh3cMDCName,
       "hh3cMDCAction": hh3cMDCAction,
       "hh3cMDCStatus": hh3cMDCStatus,
       "hh3cMDCRowStatus": hh3cMDCRowStatus,
       "hh3cMDCResource": hh3cMDCResource,
       "hh3cMDCDISKResourceTable": hh3cMDCDISKResourceTable,
       "hh3cMDCDISKResourceEntry": hh3cMDCDISKResourceEntry,
       "hh3cMDCDISKResourceInstance": hh3cMDCDISKResourceInstance,
       "hh3cMDCDISKResourceInstanceName": hh3cMDCDISKResourceInstanceName,
       "hh3cMDCDISKResourceMinLimit": hh3cMDCDISKResourceMinLimit,
       "hh3cMDCDISKResourceMaxLimit": hh3cMDCDISKResourceMaxLimit,
       "hh3cMDCDISKResourceReserve": hh3cMDCDISKResourceReserve,
       "hh3cMDCDISKResourceQuota": hh3cMDCDISKResourceQuota,
       "hh3cMDCDISKResourceUsage": hh3cMDCDISKResourceUsage,
       "hh3cMDCDISKResourceAvailable": hh3cMDCDISKResourceAvailable,
       "hh3cMDCMemoryResourceTable": hh3cMDCMemoryResourceTable,
       "hh3cMDCMemoryResourceEntry": hh3cMDCMemoryResourceEntry,
       "hh3cMDCMemoryResourceMinLimit": hh3cMDCMemoryResourceMinLimit,
       "hh3cMDCMemoryResourceMaxLimit": hh3cMDCMemoryResourceMaxLimit,
       "hh3cMDCMemoryResourceReserve": hh3cMDCMemoryResourceReserve,
       "hh3cMDCMemoryResourceQuota": hh3cMDCMemoryResourceQuota,
       "hh3cMDCMemoryResourceUsage": hh3cMDCMemoryResourceUsage,
       "hh3cMDCMemoryResourceAvailable": hh3cMDCMemoryResourceAvailable,
       "hh3cMDCCPUResourceTable": hh3cMDCCPUResourceTable,
       "hh3cMDCCPUResourceEntry": hh3cMDCCPUResourceEntry,
       "hh3cMDCCPUResourceLimit": hh3cMDCCPUResourceLimit,
       "hh3cMDCCPUResourceUsage": hh3cMDCCPUResourceUsage,
       "hh3cMDCLocation": hh3cMDCLocation,
       "hh3cMDCLocationTable": hh3cMDCLocationTable,
       "hh3cMDCLocationEntry": hh3cMDCLocationEntry,
       "hh3cMDCLocationStatus": hh3cMDCLocationStatus,
       "hh3cMDCAllocate": hh3cMDCAllocate,
       "hh3cMDCGroupIfTable": hh3cMDCGroupIfTable,
       "hh3cMDCGroupIfEntry": hh3cMDCGroupIfEntry,
       "hh3cMDCGroupIdentity": hh3cMDCGroupIdentity,
       "hh3cMDCAllocateTable": hh3cMDCAllocateTable,
       "hh3cMDCAllocateEntry": hh3cMDCAllocateEntry,
       "hh3cMDCAllocateGroupIndex": hh3cMDCAllocateGroupIndex,
       "hh3cMDCAllocateGroupDescription": hh3cMDCAllocateGroupDescription,
       "hh3cMDCAllocateMDCId": hh3cMDCAllocateMDCId,
       "hh3cMDCNotification": hh3cMDCNotification,
       "hh3cMDCNotificationObjects": hh3cMDCNotificationObjects,
       "hh3cMDCStateChangeToActive": hh3cMDCStateChangeToActive,
       "hh3cMDCStateChangeToInactive": hh3cMDCStateChangeToInactive}
)
