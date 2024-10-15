# SNMP MIB module (SALIX-PRODUCT-PLUGIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-PRODUCT-PLUGIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:28 2024
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

(atmfM4CellProtoHistIndex,
 atmfM4PlugInUnitEntry) = mibBuilder.importSymbols(
    "ATM-FORUM-M4-MIB",
    "atmfM4CellProtoHistIndex",
    "atmfM4PlugInUnitEntry")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(platform1,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "platform1")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

salixProductPlugInMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SalixPlugInUnitType(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dpu", 2),
          ("ds3Liu", 10),
          ("fan", 7),
          ("hardDrive", 8),
          ("hsf", 5),
          ("liu", 4),
          ("mpu", 1),
          ("packetLiu", 12),
          ("powerSupply", 6),
          ("smu", 3),
          ("softwarePacketLiu", 11),
          ("unknown", 0),
          ("xcoder", 9))
    )



# MIB Managed Objects in the order of their OIDs

_SalixProductPlugInMIBObjects_ObjectIdentity = ObjectIdentity
salixProductPlugInMIBObjects = _SalixProductPlugInMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1)
)
_SalixPlugInUnit_ObjectIdentity = ObjectIdentity
salixPlugInUnit = _SalixPlugInUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1)
)
_SalixPlugInUnitDpuTable_Object = MibTable
salixPlugInUnitDpuTable = _SalixPlugInUnitDpuTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    salixPlugInUnitDpuTable.setStatus("current")
_SalixPlugInUnitDpuEntry_Object = MibTableRow
salixPlugInUnitDpuEntry = _SalixPlugInUnitDpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 1, 1)
)
salixPlugInUnitDpuEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    salixPlugInUnitDpuEntry.setStatus("current")


class _SalixDpuProcessorType_Type(Integer32):
    """Custom type salixDpuProcessorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("mipsR4700", 1)
    )


_SalixDpuProcessorType_Type.__name__ = "Integer32"
_SalixDpuProcessorType_Object = MibTableColumn
salixDpuProcessorType = _SalixDpuProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 1, 1, 1),
    _SalixDpuProcessorType_Type()
)
salixDpuProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixDpuProcessorType.setStatus("current")
_SalixPlugInUnitLiuTable_Object = MibTable
salixPlugInUnitLiuTable = _SalixPlugInUnitLiuTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    salixPlugInUnitLiuTable.setStatus("current")
_SalixPlugInUnitLiuEntry_Object = MibTableRow
salixPlugInUnitLiuEntry = _SalixPlugInUnitLiuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 2, 1)
)
salixPlugInUnitLiuEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    salixPlugInUnitLiuEntry.setStatus("current")


class _SalixLiuOrderwireEnabled_Type(TruthValue):
    """Custom type salixLiuOrderwireEnabled based on TruthValue"""


_SalixLiuOrderwireEnabled_Object = MibTableColumn
salixLiuOrderwireEnabled = _SalixLiuOrderwireEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 2, 1, 1),
    _SalixLiuOrderwireEnabled_Type()
)
salixLiuOrderwireEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixLiuOrderwireEnabled.setStatus("current")


class _SalixLiuOrderwireSonetLine_Type(Integer32):
    """Custom type salixLiuOrderwireSonetLine based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SalixLiuOrderwireSonetLine_Type.__name__ = "Integer32"
_SalixLiuOrderwireSonetLine_Object = MibTableColumn
salixLiuOrderwireSonetLine = _SalixLiuOrderwireSonetLine_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 2, 1, 2),
    _SalixLiuOrderwireSonetLine_Type()
)
salixLiuOrderwireSonetLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixLiuOrderwireSonetLine.setStatus("current")


class _SalixLiuOrderwireSonetLayer_Type(Integer32):
    """Custom type salixLiuOrderwireSonetLayer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 2),
          ("section", 1))
    )


_SalixLiuOrderwireSonetLayer_Type.__name__ = "Integer32"
_SalixLiuOrderwireSonetLayer_Object = MibTableColumn
salixLiuOrderwireSonetLayer = _SalixLiuOrderwireSonetLayer_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 2, 1, 3),
    _SalixLiuOrderwireSonetLayer_Type()
)
salixLiuOrderwireSonetLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixLiuOrderwireSonetLayer.setStatus("current")
_SalixPlugInUnitSyncTable_Object = MibTable
salixPlugInUnitSyncTable = _SalixPlugInUnitSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    salixPlugInUnitSyncTable.setStatus("current")
_SalixPlugInUnitSyncEntry_Object = MibTableRow
salixPlugInUnitSyncEntry = _SalixPlugInUnitSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 3, 1)
)
salixPlugInUnitSyncEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    salixPlugInUnitSyncEntry.setStatus("current")


class _SalixSyncSlotIdentifier_Type(Integer32):
    """Custom type salixSyncSlotIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SalixSyncSlotIdentifier_Type.__name__ = "Integer32"
_SalixSyncSlotIdentifier_Object = MibTableColumn
salixSyncSlotIdentifier = _SalixSyncSlotIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 3, 1, 1),
    _SalixSyncSlotIdentifier_Type()
)
salixSyncSlotIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixSyncSlotIdentifier.setStatus("current")
_SalixPlugInUnitXcdrTable_Object = MibTable
salixPlugInUnitXcdrTable = _SalixPlugInUnitXcdrTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    salixPlugInUnitXcdrTable.setStatus("current")
_SalixPlugInUnitXcdrEntry_Object = MibTableRow
salixPlugInUnitXcdrEntry = _SalixPlugInUnitXcdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 6, 1)
)
salixPlugInUnitXcdrEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    salixPlugInUnitXcdrEntry.setStatus("current")


class _SalixPlugInUnitXcdrPercentWorkingDsp_Type(Integer32):
    """Custom type salixPlugInUnitXcdrPercentWorkingDsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SalixPlugInUnitXcdrPercentWorkingDsp_Type.__name__ = "Integer32"
_SalixPlugInUnitXcdrPercentWorkingDsp_Object = MibTableColumn
salixPlugInUnitXcdrPercentWorkingDsp = _SalixPlugInUnitXcdrPercentWorkingDsp_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 6, 1, 1),
    _SalixPlugInUnitXcdrPercentWorkingDsp_Type()
)
salixPlugInUnitXcdrPercentWorkingDsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salixPlugInUnitXcdrPercentWorkingDsp.setStatus("current")


class _SalixPlugInUnitXcdrType_Type(Integer32):
    """Custom type salixPlugInUnitXcdrType based on Integer32"""
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
        *(("toneAndAnnouncementServer", 2),
          ("universalServer", 3),
          ("voipServer", 1))
    )


_SalixPlugInUnitXcdrType_Type.__name__ = "Integer32"
_SalixPlugInUnitXcdrType_Object = MibTableColumn
salixPlugInUnitXcdrType = _SalixPlugInUnitXcdrType_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 6, 1, 2),
    _SalixPlugInUnitXcdrType_Type()
)
salixPlugInUnitXcdrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixPlugInUnitXcdrType.setStatus("current")
_SalixPlugInUnitDs3LiuTable_Object = MibTable
salixPlugInUnitDs3LiuTable = _SalixPlugInUnitDs3LiuTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    salixPlugInUnitDs3LiuTable.setStatus("current")
_SalixPlugInUnitDs3LiuEntry_Object = MibTableRow
salixPlugInUnitDs3LiuEntry = _SalixPlugInUnitDs3LiuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 7, 1)
)
salixPlugInUnitDs3LiuEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    salixPlugInUnitDs3LiuEntry.setStatus("current")


class _SalixDs3LiuGroupNumber_Type(Integer32):
    """Custom type salixDs3LiuGroupNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SalixDs3LiuGroupNumber_Type.__name__ = "Integer32"
_SalixDs3LiuGroupNumber_Object = MibTableColumn
salixDs3LiuGroupNumber = _SalixDs3LiuGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 1, 1, 7, 1, 1),
    _SalixDs3LiuGroupNumber_Type()
)
salixDs3LiuGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixDs3LiuGroupNumber.setStatus("current")
_SalixProductPlugInMIBTraps_ObjectIdentity = ObjectIdentity
salixProductPlugInMIBTraps = _SalixProductPlugInMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 2)
)
_SalixProductPlugInMIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixProductPlugInMIBTrapPrefix = _SalixProductPlugInMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 2, 0)
)
_SalixProductPlugInMIBCompliance_ObjectIdentity = ObjectIdentity
salixProductPlugInMIBCompliance = _SalixProductPlugInMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 3)
)
_SalixPPIGroups_ObjectIdentity = ObjectIdentity
salixPPIGroups = _SalixPPIGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 3, 1)
)
_SalixPPICompliances_ObjectIdentity = ObjectIdentity
salixPPICompliances = _SalixPPICompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 3, 2)
)

# Managed Objects groups

salixPPIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 3, 1)
)
salixPPIGroup.setObjects(
      *(("SALIX-PRODUCT-PLUGIN-MIB", "salixDpuProcessorType"),
        ("SALIX-PRODUCT-PLUGIN-MIB", "salixLiuOrderwireEnabled"),
        ("SALIX-PRODUCT-PLUGIN-MIB", "salixLiuOrderwireSonetLine"),
        ("SALIX-PRODUCT-PLUGIN-MIB", "salixLiuOrderwireSonetLayer"))
)
if mibBuilder.loadTexts:
    salixPPIGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

salixPPICompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 5, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    salixPPICompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-PRODUCT-PLUGIN-MIB",
    **{"SalixPlugInUnitType": SalixPlugInUnitType,
       "salixProductPlugInMIB": salixProductPlugInMIB,
       "salixProductPlugInMIBObjects": salixProductPlugInMIBObjects,
       "salixPlugInUnit": salixPlugInUnit,
       "salixPlugInUnitDpuTable": salixPlugInUnitDpuTable,
       "salixPlugInUnitDpuEntry": salixPlugInUnitDpuEntry,
       "salixDpuProcessorType": salixDpuProcessorType,
       "salixPlugInUnitLiuTable": salixPlugInUnitLiuTable,
       "salixPlugInUnitLiuEntry": salixPlugInUnitLiuEntry,
       "salixLiuOrderwireEnabled": salixLiuOrderwireEnabled,
       "salixLiuOrderwireSonetLine": salixLiuOrderwireSonetLine,
       "salixLiuOrderwireSonetLayer": salixLiuOrderwireSonetLayer,
       "salixPlugInUnitSyncTable": salixPlugInUnitSyncTable,
       "salixPlugInUnitSyncEntry": salixPlugInUnitSyncEntry,
       "salixSyncSlotIdentifier": salixSyncSlotIdentifier,
       "salixPlugInUnitXcdrTable": salixPlugInUnitXcdrTable,
       "salixPlugInUnitXcdrEntry": salixPlugInUnitXcdrEntry,
       "salixPlugInUnitXcdrPercentWorkingDsp": salixPlugInUnitXcdrPercentWorkingDsp,
       "salixPlugInUnitXcdrType": salixPlugInUnitXcdrType,
       "salixPlugInUnitDs3LiuTable": salixPlugInUnitDs3LiuTable,
       "salixPlugInUnitDs3LiuEntry": salixPlugInUnitDs3LiuEntry,
       "salixDs3LiuGroupNumber": salixDs3LiuGroupNumber,
       "salixProductPlugInMIBTraps": salixProductPlugInMIBTraps,
       "salixProductPlugInMIBTrapPrefix": salixProductPlugInMIBTrapPrefix,
       "salixProductPlugInMIBCompliance": salixProductPlugInMIBCompliance,
       "salixPPIGroups": salixPPIGroups,
       "salixPPIGroup": salixPPIGroup,
       "salixPPICompliances": salixPPICompliances,
       "salixPPICompliance": salixPPICompliance}
)
