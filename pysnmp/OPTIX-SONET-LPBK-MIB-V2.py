# SNMP MIB module (OPTIX-SONET-LPBK-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-SONET-LPBK-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:30 2024
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

(optixCommonSonet,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixCommonSonet")

(MOD2Type,) = mibBuilder.importSymbols(
    "OPTIX-SONET-TC-MIB",
    "MOD2Type")

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

optixSonetMaintenance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LpbkType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("crs", 3),
          ("ds1feac", 4),
          ("ds3feac", 5),
          ("fac2ni", 6),
          ("facility", 2),
          ("noloop", 255),
          ("terminal", 1))
    )



# MIB Managed Objects in the order of their OIDs

_OptixSonetLoopback_ObjectIdentity = ObjectIdentity
optixSonetLoopback = _OptixSonetLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10)
)
_LpbkStateTable_Object = MibTable
lpbkStateTable = _LpbkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10)
)
if mibBuilder.loadTexts:
    lpbkStateTable.setStatus("current")
_LpbkStateEntry_Object = MibTableRow
lpbkStateEntry = _LpbkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1)
)
lpbkStateEntry.setIndexNames(
    (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkStateMOD2"),
    (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkStateSlot"),
    (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkStatePort"),
    (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkStatePath"),
    (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkStateVT"),
)
if mibBuilder.loadTexts:
    lpbkStateEntry.setStatus("current")
_LpbkStateMOD2_Type = MOD2Type
_LpbkStateMOD2_Object = MibTableColumn
lpbkStateMOD2 = _LpbkStateMOD2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 1),
    _LpbkStateMOD2_Type()
)
lpbkStateMOD2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkStateMOD2.setStatus("current")
_LpbkStateSlot_Type = Gauge32
_LpbkStateSlot_Object = MibTableColumn
lpbkStateSlot = _LpbkStateSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 2),
    _LpbkStateSlot_Type()
)
lpbkStateSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkStateSlot.setStatus("current")
_LpbkStatePort_Type = Gauge32
_LpbkStatePort_Object = MibTableColumn
lpbkStatePort = _LpbkStatePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 3),
    _LpbkStatePort_Type()
)
lpbkStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkStatePort.setStatus("current")
_LpbkStatePath_Type = Gauge32
_LpbkStatePath_Object = MibTableColumn
lpbkStatePath = _LpbkStatePath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 4),
    _LpbkStatePath_Type()
)
lpbkStatePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkStatePath.setStatus("current")
_LpbkStateVT_Type = Gauge32
_LpbkStateVT_Object = MibTableColumn
lpbkStateVT = _LpbkStateVT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 5),
    _LpbkStateVT_Type()
)
lpbkStateVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkStateVT.setStatus("current")
_LpbkStateLpbkType_Type = LpbkType
_LpbkStateLpbkType_Object = MibTableColumn
lpbkStateLpbkType = _LpbkStateLpbkType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 6),
    _LpbkStateLpbkType_Type()
)
lpbkStateLpbkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkStateLpbkType.setStatus("current")
_LpbkStateTimeout_Type = Gauge32
_LpbkStateTimeout_Object = MibTableColumn
lpbkStateTimeout = _LpbkStateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 7),
    _LpbkStateTimeout_Type()
)
lpbkStateTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkStateTimeout.setStatus("current")
_LpbkFlagTable_Object = MibTable
lpbkFlagTable = _LpbkFlagTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20)
)
if mibBuilder.loadTexts:
    lpbkFlagTable.setStatus("current")
_LpbkFlagEntry_Object = MibTableRow
lpbkFlagEntry = _LpbkFlagEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1)
)
lpbkFlagEntry.setIndexNames(
    (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagMOD2"),
    (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagSlot"),
    (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagPort"),
    (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagPath"),
    (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagVT"),
)
if mibBuilder.loadTexts:
    lpbkFlagEntry.setStatus("current")
_LpbkFlagMOD2_Type = MOD2Type
_LpbkFlagMOD2_Object = MibTableColumn
lpbkFlagMOD2 = _LpbkFlagMOD2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 1),
    _LpbkFlagMOD2_Type()
)
lpbkFlagMOD2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkFlagMOD2.setStatus("current")
_LpbkFlagSlot_Type = Gauge32
_LpbkFlagSlot_Object = MibTableColumn
lpbkFlagSlot = _LpbkFlagSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 2),
    _LpbkFlagSlot_Type()
)
lpbkFlagSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkFlagSlot.setStatus("current")
_LpbkFlagPort_Type = Gauge32
_LpbkFlagPort_Object = MibTableColumn
lpbkFlagPort = _LpbkFlagPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 3),
    _LpbkFlagPort_Type()
)
lpbkFlagPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkFlagPort.setStatus("current")
_LpbkFlagPath_Type = Gauge32
_LpbkFlagPath_Object = MibTableColumn
lpbkFlagPath = _LpbkFlagPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 4),
    _LpbkFlagPath_Type()
)
lpbkFlagPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkFlagPath.setStatus("current")
_LpbkFlagVT_Type = Gauge32
_LpbkFlagVT_Object = MibTableColumn
lpbkFlagVT = _LpbkFlagVT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 5),
    _LpbkFlagVT_Type()
)
lpbkFlagVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkFlagVT.setStatus("current")
_LpbkFlagLpbkType_Type = LpbkType
_LpbkFlagLpbkType_Object = MibTableColumn
lpbkFlagLpbkType = _LpbkFlagLpbkType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 6),
    _LpbkFlagLpbkType_Type()
)
lpbkFlagLpbkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkFlagLpbkType.setStatus("current")


class _LpbkFlagEnFlag_Type(Integer32):
    """Custom type lpbkFlagEnFlag based on Integer32"""
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


_LpbkFlagEnFlag_Type.__name__ = "Integer32"
_LpbkFlagEnFlag_Object = MibTableColumn
lpbkFlagEnFlag = _LpbkFlagEnFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 7),
    _LpbkFlagEnFlag_Type()
)
lpbkFlagEnFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkFlagEnFlag.setStatus("current")
_LpbkFlagTimeout_Type = Gauge32
_LpbkFlagTimeout_Object = MibTableColumn
lpbkFlagTimeout = _LpbkFlagTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 8),
    _LpbkFlagTimeout_Type()
)
lpbkFlagTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkFlagTimeout.setStatus("current")
_OptixSonetMaintenanceConformance_ObjectIdentity = ObjectIdentity
optixSonetMaintenanceConformance = _OptixSonetMaintenanceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 11)
)
_OptixSonetMaintenanceGroups_ObjectIdentity = ObjectIdentity
optixSonetMaintenanceGroups = _OptixSonetMaintenanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 11, 1)
)
_OptixSonetMaintenanceCompliances_ObjectIdentity = ObjectIdentity
optixSonetMaintenanceCompliances = _OptixSonetMaintenanceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 11, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 11, 1, 1)
)
currentObjectGroup.setObjects(
      *(("OPTIX-SONET-LPBK-MIB-V2", "lpbkStateMOD2"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStateSlot"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStatePort"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStatePath"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStateVT"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStateLpbkType"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStateTimeout"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagMOD2"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagSlot"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagPort"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagPath"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagVT"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagLpbkType"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagEnFlag"),
        ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagTimeout"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 11, 2, 1)
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-SONET-LPBK-MIB-V2",
    **{"LpbkType": LpbkType,
       "optixSonetMaintenance": optixSonetMaintenance,
       "optixSonetLoopback": optixSonetLoopback,
       "lpbkStateTable": lpbkStateTable,
       "lpbkStateEntry": lpbkStateEntry,
       "lpbkStateMOD2": lpbkStateMOD2,
       "lpbkStateSlot": lpbkStateSlot,
       "lpbkStatePort": lpbkStatePort,
       "lpbkStatePath": lpbkStatePath,
       "lpbkStateVT": lpbkStateVT,
       "lpbkStateLpbkType": lpbkStateLpbkType,
       "lpbkStateTimeout": lpbkStateTimeout,
       "lpbkFlagTable": lpbkFlagTable,
       "lpbkFlagEntry": lpbkFlagEntry,
       "lpbkFlagMOD2": lpbkFlagMOD2,
       "lpbkFlagSlot": lpbkFlagSlot,
       "lpbkFlagPort": lpbkFlagPort,
       "lpbkFlagPath": lpbkFlagPath,
       "lpbkFlagVT": lpbkFlagVT,
       "lpbkFlagLpbkType": lpbkFlagLpbkType,
       "lpbkFlagEnFlag": lpbkFlagEnFlag,
       "lpbkFlagTimeout": lpbkFlagTimeout,
       "optixSonetMaintenanceConformance": optixSonetMaintenanceConformance,
       "optixSonetMaintenanceGroups": optixSonetMaintenanceGroups,
       "currentObjectGroup": currentObjectGroup,
       "optixSonetMaintenanceCompliances": optixSonetMaintenanceCompliances,
       "basicCompliance": basicCompliance}
)
