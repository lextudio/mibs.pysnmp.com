# SNMP MIB module (SBFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SBFC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:47 2024
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
 iso,
 private) = mibBuilder.importSymbols(
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
    "iso",
    "private")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Stonesoft_ObjectIdentity = ObjectIdentity
stonesoft = _Stonesoft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369)
)
_StoneSystem_ObjectIdentity = ObjectIdentity
stoneSystem = _StoneSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 1)
)


class _AgentDescr_Type(DisplayString):
    """Custom type agentDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentDescr_Type.__name__ = "DisplayString"
_AgentDescr_Object = MibScalar
agentDescr = _AgentDescr_Object(
    (1, 3, 6, 1, 4, 1, 1369, 1, 1),
    _AgentDescr_Type()
)
agentDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDescr.setStatus("mandatory")


class _AgentVersion_Type(DisplayString):
    """Custom type agentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentVersion_Type.__name__ = "DisplayString"
_AgentVersion_Object = MibScalar
agentVersion = _AgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 1369, 1, 2),
    _AgentVersion_Type()
)
agentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVersion.setStatus("mandatory")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 2)
)
_FullCluster_ObjectIdentity = ObjectIdentity
fullCluster = _FullCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2)
)
_SbfcClusterID_Type = Integer32
_SbfcClusterID_Object = MibScalar
sbfcClusterID = _SbfcClusterID_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 1),
    _SbfcClusterID_Type()
)
sbfcClusterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcClusterID.setStatus("mandatory")
_SbfcMemberID_Type = Integer32
_SbfcMemberID_Object = MibScalar
sbfcMemberID = _SbfcMemberID_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 2),
    _SbfcMemberID_Type()
)
sbfcMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcMemberID.setStatus("mandatory")
_SbfcMaxNodeID_Type = Integer32
_SbfcMaxNodeID_Object = MibScalar
sbfcMaxNodeID = _SbfcMaxNodeID_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 3),
    _SbfcMaxNodeID_Type()
)
sbfcMaxNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcMaxNodeID.setStatus("mandatory")
_SbfcModule_ObjectIdentity = ObjectIdentity
sbfcModule = _SbfcModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 4)
)


class _SbfcModuleVersion_Type(DisplayString):
    """Custom type sbfcModuleVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbfcModuleVersion_Type.__name__ = "DisplayString"
_SbfcModuleVersion_Object = MibScalar
sbfcModuleVersion = _SbfcModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 4, 1),
    _SbfcModuleVersion_Type()
)
sbfcModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcModuleVersion.setStatus("mandatory")


class _SbfcModulePatchLevel_Type(DisplayString):
    """Custom type sbfcModulePatchLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbfcModulePatchLevel_Type.__name__ = "DisplayString"
_SbfcModulePatchLevel_Object = MibScalar
sbfcModulePatchLevel = _SbfcModulePatchLevel_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 4, 2),
    _SbfcModulePatchLevel_Type()
)
sbfcModulePatchLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcModulePatchLevel.setStatus("mandatory")
_SbfcDriver_ObjectIdentity = ObjectIdentity
sbfcDriver = _SbfcDriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 5)
)


class _SbfcDriverVersion_Type(DisplayString):
    """Custom type sbfcDriverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbfcDriverVersion_Type.__name__ = "DisplayString"
_SbfcDriverVersion_Object = MibScalar
sbfcDriverVersion = _SbfcDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 5, 1),
    _SbfcDriverVersion_Type()
)
sbfcDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcDriverVersion.setStatus("mandatory")


class _SbfcDriverPatchLevel_Type(DisplayString):
    """Custom type sbfcDriverPatchLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbfcDriverPatchLevel_Type.__name__ = "DisplayString"
_SbfcDriverPatchLevel_Object = MibScalar
sbfcDriverPatchLevel = _SbfcDriverPatchLevel_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 5, 2),
    _SbfcDriverPatchLevel_Type()
)
sbfcDriverPatchLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcDriverPatchLevel.setStatus("mandatory")


class _SbfcOSName_Type(DisplayString):
    """Custom type sbfcOSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbfcOSName_Type.__name__ = "DisplayString"
_SbfcOSName_Object = MibScalar
sbfcOSName = _SbfcOSName_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 6),
    _SbfcOSName_Type()
)
sbfcOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcOSName.setStatus("mandatory")


class _SbfcOSVersion_Type(DisplayString):
    """Custom type sbfcOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SbfcOSVersion_Type.__name__ = "DisplayString"
_SbfcOSVersion_Object = MibScalar
sbfcOSVersion = _SbfcOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 7),
    _SbfcOSVersion_Type()
)
sbfcOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcOSVersion.setStatus("mandatory")
_SbfcAgeOfStatus_Type = Integer32
_SbfcAgeOfStatus_Object = MibScalar
sbfcAgeOfStatus = _SbfcAgeOfStatus_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 8),
    _SbfcAgeOfStatus_Type()
)
sbfcAgeOfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcAgeOfStatus.setStatus("mandatory")
_SbfcNodeTable_Object = MibTable
sbfcNodeTable = _SbfcNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 9)
)
if mibBuilder.loadTexts:
    sbfcNodeTable.setStatus("mandatory")
_SbfcNodeEntry_Object = MibTableRow
sbfcNodeEntry = _SbfcNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    sbfcNodeEntry.setStatus("mandatory")


class _SbfcNodeID_Type(Integer32):
    """Custom type sbfcNodeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SbfcNodeID_Type.__name__ = "Integer32"
_SbfcNodeID_Object = MibTableColumn
sbfcNodeID = _SbfcNodeID_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 1),
    _SbfcNodeID_Type()
)
sbfcNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcNodeID.setStatus("mandatory")


class _SbfcNodeStatus_Type(Integer32):
    """Custom type sbfcNodeStatus based on Integer32"""
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
        *(("going-locked-offline", 9),
          ("going-locked-online", 11),
          ("going-offline", 4),
          ("going-online", 2),
          ("going-standby", 15),
          ("locked-offline", 8),
          ("locked-offline-ready-for-restart", 12),
          ("locked-online", 10),
          ("locked-online-ready-for-restart", 13),
          ("offline", 1),
          ("offline-ready-for-restart", 6),
          ("online", 3),
          ("online-ready-for-restart", 7),
          ("standby", 14),
          ("standby-ready-for-restart", 16),
          ("unknown", 5))
    )


_SbfcNodeStatus_Type.__name__ = "Integer32"
_SbfcNodeStatus_Object = MibTableColumn
sbfcNodeStatus = _SbfcNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 2),
    _SbfcNodeStatus_Type()
)
sbfcNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcNodeStatus.setStatus("mandatory")
_SbfcNodeLoad_Type = Integer32
_SbfcNodeLoad_Object = MibTableColumn
sbfcNodeLoad = _SbfcNodeLoad_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 3),
    _SbfcNodeLoad_Type()
)
sbfcNodeLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcNodeLoad.setStatus("mandatory")
_SbfcNodeCapacity_Type = Integer32
_SbfcNodeCapacity_Object = MibScalar
sbfcNodeCapacity = _SbfcNodeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 4),
    _SbfcNodeCapacity_Type()
)
sbfcNodeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcNodeCapacity.setStatus("mandatory")
_SbfcNodeControlIp_Type = IpAddress
_SbfcNodeControlIp_Object = MibScalar
sbfcNodeControlIp = _SbfcNodeControlIp_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 5),
    _SbfcNodeControlIp_Type()
)
sbfcNodeControlIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcNodeControlIp.setStatus("mandatory")


class _SbfcNodeControlPort_Type(Integer32):
    """Custom type sbfcNodeControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SbfcNodeControlPort_Type.__name__ = "Integer32"
_SbfcNodeControlPort_Object = MibTableColumn
sbfcNodeControlPort = _SbfcNodeControlPort_Object(
    (1, 3, 6, 1, 4, 1, 1369, 2, 2, 9, 1, 6),
    _SbfcNodeControlPort_Type()
)
sbfcNodeControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbfcNodeControlPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SBFC-MIB",
    **{"stonesoft": stonesoft,
       "stoneSystem": stoneSystem,
       "agentDescr": agentDescr,
       "agentVersion": agentVersion,
       "products": products,
       "fullCluster": fullCluster,
       "sbfcClusterID": sbfcClusterID,
       "sbfcMemberID": sbfcMemberID,
       "sbfcMaxNodeID": sbfcMaxNodeID,
       "sbfcModule": sbfcModule,
       "sbfcModuleVersion": sbfcModuleVersion,
       "sbfcModulePatchLevel": sbfcModulePatchLevel,
       "sbfcDriver": sbfcDriver,
       "sbfcDriverVersion": sbfcDriverVersion,
       "sbfcDriverPatchLevel": sbfcDriverPatchLevel,
       "sbfcOSName": sbfcOSName,
       "sbfcOSVersion": sbfcOSVersion,
       "sbfcAgeOfStatus": sbfcAgeOfStatus,
       "sbfcNodeTable": sbfcNodeTable,
       "sbfcNodeEntry": sbfcNodeEntry,
       "sbfcNodeID": sbfcNodeID,
       "sbfcNodeStatus": sbfcNodeStatus,
       "sbfcNodeLoad": sbfcNodeLoad,
       "sbfcNodeCapacity": sbfcNodeCapacity,
       "sbfcNodeControlIp": sbfcNodeControlIp,
       "sbfcNodeControlPort": sbfcNodeControlPort}
)
