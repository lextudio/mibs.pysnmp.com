# SNMP MIB module (DGS-6600-SYSTEM-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-6600-SYSTEM-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:00 2024
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

(dgs6600_system,) = mibBuilder.importSymbols(
    "DGS-6600-ID-MIB",
    "dgs6600-system")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dgs6600SystemInfoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SystemBasicInfo_ObjectIdentity = ObjectIdentity
systemBasicInfo = _SystemBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1)
)
_SystemCPUutilization_ObjectIdentity = ObjectIdentity
systemCPUutilization = _SystemCPUutilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 1)
)
_SystemCPUutilizationIn5sec_Type = Integer32
_SystemCPUutilizationIn5sec_Object = MibScalar
systemCPUutilizationIn5sec = _SystemCPUutilizationIn5sec_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 1, 1),
    _SystemCPUutilizationIn5sec_Type()
)
systemCPUutilizationIn5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCPUutilizationIn5sec.setStatus("current")
_SystemCPUutilizationIn1min_Type = Integer32
_SystemCPUutilizationIn1min_Object = MibScalar
systemCPUutilizationIn1min = _SystemCPUutilizationIn1min_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 1, 2),
    _SystemCPUutilizationIn1min_Type()
)
systemCPUutilizationIn1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCPUutilizationIn1min.setStatus("current")
_SystemCPUutilizationIn5min_Type = Integer32
_SystemCPUutilizationIn5min_Object = MibScalar
systemCPUutilizationIn5min = _SystemCPUutilizationIn5min_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 1, 3),
    _SystemCPUutilizationIn5min_Type()
)
systemCPUutilizationIn5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCPUutilizationIn5min.setStatus("current")
_SystemDRAMutilizationTable_Object = MibTable
systemDRAMutilizationTable = _SystemDRAMutilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    systemDRAMutilizationTable.setStatus("current")
_SystemDRAMutilizationEntry_Object = MibTableRow
systemDRAMutilizationEntry = _SystemDRAMutilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 2, 1)
)
systemDRAMutilizationEntry.setIndexNames(
    (0, "DGS-6600-SYSTEM-INFO-MIB", "systemDRAMutilizationUnitID"),
)
if mibBuilder.loadTexts:
    systemDRAMutilizationEntry.setStatus("current")


class _SystemDRAMutilizationUnitID_Type(Integer32):
    """Custom type systemDRAMutilizationUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SystemDRAMutilizationUnitID_Type.__name__ = "Integer32"
_SystemDRAMutilizationUnitID_Object = MibTableColumn
systemDRAMutilizationUnitID = _SystemDRAMutilizationUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 2, 1, 1),
    _SystemDRAMutilizationUnitID_Type()
)
systemDRAMutilizationUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemDRAMutilizationUnitID.setStatus("current")
_SystemDRAMutilizationTotalDRAM_Type = Integer32
_SystemDRAMutilizationTotalDRAM_Object = MibTableColumn
systemDRAMutilizationTotalDRAM = _SystemDRAMutilizationTotalDRAM_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 2, 1, 2),
    _SystemDRAMutilizationTotalDRAM_Type()
)
systemDRAMutilizationTotalDRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDRAMutilizationTotalDRAM.setStatus("current")
if mibBuilder.loadTexts:
    systemDRAMutilizationTotalDRAM.setUnits("KB")
_SystemDRAMutilizationUsedDRAM_Type = Integer32
_SystemDRAMutilizationUsedDRAM_Object = MibTableColumn
systemDRAMutilizationUsedDRAM = _SystemDRAMutilizationUsedDRAM_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 2, 1, 3),
    _SystemDRAMutilizationUsedDRAM_Type()
)
systemDRAMutilizationUsedDRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDRAMutilizationUsedDRAM.setStatus("current")
if mibBuilder.loadTexts:
    systemDRAMutilizationUsedDRAM.setUnits("KB")
_SystemDRAMutilization_Type = Integer32
_SystemDRAMutilization_Object = MibTableColumn
systemDRAMutilization = _SystemDRAMutilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 2, 1, 4),
    _SystemDRAMutilization_Type()
)
systemDRAMutilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDRAMutilization.setStatus("current")
_SystemFLASHutilizationTable_Object = MibTable
systemFLASHutilizationTable = _SystemFLASHutilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    systemFLASHutilizationTable.setStatus("current")
_SystemFLASHutilizationEntry_Object = MibTableRow
systemFLASHutilizationEntry = _SystemFLASHutilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 3, 1)
)
systemFLASHutilizationEntry.setIndexNames(
    (0, "DGS-6600-SYSTEM-INFO-MIB", "systemFLASHutilizationUnitID"),
)
if mibBuilder.loadTexts:
    systemFLASHutilizationEntry.setStatus("current")


class _SystemFLASHutilizationUnitID_Type(Integer32):
    """Custom type systemFLASHutilizationUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SystemFLASHutilizationUnitID_Type.__name__ = "Integer32"
_SystemFLASHutilizationUnitID_Object = MibTableColumn
systemFLASHutilizationUnitID = _SystemFLASHutilizationUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 3, 1, 1),
    _SystemFLASHutilizationUnitID_Type()
)
systemFLASHutilizationUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFLASHutilizationUnitID.setStatus("current")
_SystemFLASHutilizationTotalFLASH_Type = Integer32
_SystemFLASHutilizationTotalFLASH_Object = MibTableColumn
systemFLASHutilizationTotalFLASH = _SystemFLASHutilizationTotalFLASH_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 3, 1, 2),
    _SystemFLASHutilizationTotalFLASH_Type()
)
systemFLASHutilizationTotalFLASH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFLASHutilizationTotalFLASH.setStatus("current")
if mibBuilder.loadTexts:
    systemFLASHutilizationTotalFLASH.setUnits("KB")
_SystemFLASHutilizationUsedFLASH_Type = Integer32
_SystemFLASHutilizationUsedFLASH_Object = MibTableColumn
systemFLASHutilizationUsedFLASH = _SystemFLASHutilizationUsedFLASH_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 3, 1, 3),
    _SystemFLASHutilizationUsedFLASH_Type()
)
systemFLASHutilizationUsedFLASH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFLASHutilizationUsedFLASH.setStatus("current")
if mibBuilder.loadTexts:
    systemFLASHutilizationUsedFLASH.setUnits("KB")
_SystemFLASHutilization_Type = Integer32
_SystemFLASHutilization_Object = MibTableColumn
systemFLASHutilization = _SystemFLASHutilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 120, 100, 1, 1, 1, 3, 1, 4),
    _SystemFLASHutilization_Type()
)
systemFLASHutilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFLASHutilization.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-6600-SYSTEM-INFO-MIB",
    **{"dgs6600SystemInfoMIB": dgs6600SystemInfoMIB,
       "systemBasicInfo": systemBasicInfo,
       "systemCPUutilization": systemCPUutilization,
       "systemCPUutilizationIn5sec": systemCPUutilizationIn5sec,
       "systemCPUutilizationIn1min": systemCPUutilizationIn1min,
       "systemCPUutilizationIn5min": systemCPUutilizationIn5min,
       "systemDRAMutilizationTable": systemDRAMutilizationTable,
       "systemDRAMutilizationEntry": systemDRAMutilizationEntry,
       "systemDRAMutilizationUnitID": systemDRAMutilizationUnitID,
       "systemDRAMutilizationTotalDRAM": systemDRAMutilizationTotalDRAM,
       "systemDRAMutilizationUsedDRAM": systemDRAMutilizationUsedDRAM,
       "systemDRAMutilization": systemDRAMutilization,
       "systemFLASHutilizationTable": systemFLASHutilizationTable,
       "systemFLASHutilizationEntry": systemFLASHutilizationEntry,
       "systemFLASHutilizationUnitID": systemFLASHutilizationUnitID,
       "systemFLASHutilizationTotalFLASH": systemFLASHutilizationTotalFLASH,
       "systemFLASHutilizationUsedFLASH": systemFLASHutilizationUsedFLASH,
       "systemFLASHutilization": systemFLASHutilization}
)
