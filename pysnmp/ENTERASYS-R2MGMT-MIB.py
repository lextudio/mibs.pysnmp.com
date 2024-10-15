# SNMP MIB module (ENTERASYS-R2MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-R2MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:25 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

enterasysR2MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11)
)
enterasysR2MgmtMIB.setRevisions(
        ("2004-07-08 15:30",
         "2002-03-07 19:35",
         "2001-06-26 17:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysR2MgmtObjects_ObjectIdentity = ObjectIdentity
etsysR2MgmtObjects = _EtsysR2MgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1)
)
_EtsysR2MgmtParams_ObjectIdentity = ObjectIdentity
etsysR2MgmtParams = _EtsysR2MgmtParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 1)
)
_EtsysR2MgmtMemorySize_Type = Integer32
_EtsysR2MgmtMemorySize_Object = MibScalar
etsysR2MgmtMemorySize = _EtsysR2MgmtMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 1, 1),
    _EtsysR2MgmtMemorySize_Type()
)
etsysR2MgmtMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysR2MgmtMemorySize.setStatus("current")
_EtsysR2MgmtWEBInterface_Type = EnabledStatus
_EtsysR2MgmtWEBInterface_Object = MibScalar
etsysR2MgmtWEBInterface = _EtsysR2MgmtWEBInterface_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 1, 2),
    _EtsysR2MgmtWEBInterface_Type()
)
etsysR2MgmtWEBInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysR2MgmtWEBInterface.setStatus("current")
_EtsysR2MgmtTelnetInterface_Type = EnabledStatus
_EtsysR2MgmtTelnetInterface_Object = MibScalar
etsysR2MgmtTelnetInterface = _EtsysR2MgmtTelnetInterface_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 1, 3),
    _EtsysR2MgmtTelnetInterface_Type()
)
etsysR2MgmtTelnetInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysR2MgmtTelnetInterface.setStatus("current")


class _EtsysR2MgmtVlan_Type(Integer32):
    """Custom type etsysR2MgmtVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_EtsysR2MgmtVlan_Type.__name__ = "Integer32"
_EtsysR2MgmtVlan_Object = MibScalar
etsysR2MgmtVlan = _EtsysR2MgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 1, 4),
    _EtsysR2MgmtVlan_Type()
)
etsysR2MgmtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysR2MgmtVlan.setStatus("current")
_EtsysR2MgmtCounters_ObjectIdentity = ObjectIdentity
etsysR2MgmtCounters = _EtsysR2MgmtCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 2)
)
_EtsysR2MgmtPowerups_Type = Counter32
_EtsysR2MgmtPowerups_Object = MibScalar
etsysR2MgmtPowerups = _EtsysR2MgmtPowerups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 2, 1),
    _EtsysR2MgmtPowerups_Type()
)
etsysR2MgmtPowerups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysR2MgmtPowerups.setStatus("current")
_EtsysR2MgmtResets_Type = Counter32
_EtsysR2MgmtResets_Object = MibScalar
etsysR2MgmtResets = _EtsysR2MgmtResets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 2, 2),
    _EtsysR2MgmtResets_Type()
)
etsysR2MgmtResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysR2MgmtResets.setStatus("current")
_EtsysR2MgmtUnsolicitedResets_Type = Counter32
_EtsysR2MgmtUnsolicitedResets_Object = MibScalar
etsysR2MgmtUnsolicitedResets = _EtsysR2MgmtUnsolicitedResets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 2, 3),
    _EtsysR2MgmtUnsolicitedResets_Type()
)
etsysR2MgmtUnsolicitedResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysR2MgmtUnsolicitedResets.setStatus("current")
_EtsysR2MgmtErrorLog_ObjectIdentity = ObjectIdentity
etsysR2MgmtErrorLog = _EtsysR2MgmtErrorLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 3)
)


class _EtsysR2MgmtErrLogNumEntries_Type(Integer32):
    """Custom type etsysR2MgmtErrLogNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysR2MgmtErrLogNumEntries_Type.__name__ = "Integer32"
_EtsysR2MgmtErrLogNumEntries_Object = MibScalar
etsysR2MgmtErrLogNumEntries = _EtsysR2MgmtErrLogNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 3, 1),
    _EtsysR2MgmtErrLogNumEntries_Type()
)
etsysR2MgmtErrLogNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysR2MgmtErrLogNumEntries.setStatus("current")
_EtsysR2MgmtErrLogTable_Object = MibTable
etsysR2MgmtErrLogTable = _EtsysR2MgmtErrLogTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 3, 2)
)
if mibBuilder.loadTexts:
    etsysR2MgmtErrLogTable.setStatus("current")
_EtsysR2MgmtErrLogEntry_Object = MibTableRow
etsysR2MgmtErrLogEntry = _EtsysR2MgmtErrLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 3, 2, 1)
)
etsysR2MgmtErrLogEntry.setIndexNames(
    (0, "ENTERASYS-R2MGMT-MIB", "etsysR2MgmtErrLogIndex"),
)
if mibBuilder.loadTexts:
    etsysR2MgmtErrLogEntry.setStatus("current")


class _EtsysR2MgmtErrLogIndex_Type(Integer32):
    """Custom type etsysR2MgmtErrLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysR2MgmtErrLogIndex_Type.__name__ = "Integer32"
_EtsysR2MgmtErrLogIndex_Object = MibTableColumn
etsysR2MgmtErrLogIndex = _EtsysR2MgmtErrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 3, 2, 1, 1),
    _EtsysR2MgmtErrLogIndex_Type()
)
etsysR2MgmtErrLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysR2MgmtErrLogIndex.setStatus("current")
_EtsysR2MgmtErrLogTimeStamp_Type = TimeTicks
_EtsysR2MgmtErrLogTimeStamp_Object = MibTableColumn
etsysR2MgmtErrLogTimeStamp = _EtsysR2MgmtErrLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 3, 2, 1, 2),
    _EtsysR2MgmtErrLogTimeStamp_Type()
)
etsysR2MgmtErrLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysR2MgmtErrLogTimeStamp.setStatus("current")


class _EtsysR2MgmtErrLogResetNumber_Type(Integer32):
    """Custom type etsysR2MgmtErrLogResetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysR2MgmtErrLogResetNumber_Type.__name__ = "Integer32"
_EtsysR2MgmtErrLogResetNumber_Object = MibTableColumn
etsysR2MgmtErrLogResetNumber = _EtsysR2MgmtErrLogResetNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 3, 2, 1, 3),
    _EtsysR2MgmtErrLogResetNumber_Type()
)
etsysR2MgmtErrLogResetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysR2MgmtErrLogResetNumber.setStatus("current")


class _EtsysR2MgmtErrLogInfo_Type(SnmpAdminString):
    """Custom type etsysR2MgmtErrLogInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysR2MgmtErrLogInfo_Type.__name__ = "SnmpAdminString"
_EtsysR2MgmtErrLogInfo_Object = MibTableColumn
etsysR2MgmtErrLogInfo = _EtsysR2MgmtErrLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 3, 2, 1, 4),
    _EtsysR2MgmtErrLogInfo_Type()
)
etsysR2MgmtErrLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysR2MgmtErrLogInfo.setStatus("current")
_EtsysR2MgmtLoader_ObjectIdentity = ObjectIdentity
etsysR2MgmtLoader = _EtsysR2MgmtLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 4)
)
_EtsysR2MgmtCrashUploadUseBootp_Type = TruthValue
_EtsysR2MgmtCrashUploadUseBootp_Object = MibScalar
etsysR2MgmtCrashUploadUseBootp = _EtsysR2MgmtCrashUploadUseBootp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 4, 1),
    _EtsysR2MgmtCrashUploadUseBootp_Type()
)
etsysR2MgmtCrashUploadUseBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysR2MgmtCrashUploadUseBootp.setStatus("current")
_EtsysR2MgmtCrashUploadServerIP_Type = IpAddress
_EtsysR2MgmtCrashUploadServerIP_Object = MibScalar
etsysR2MgmtCrashUploadServerIP = _EtsysR2MgmtCrashUploadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 4, 2),
    _EtsysR2MgmtCrashUploadServerIP_Type()
)
etsysR2MgmtCrashUploadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysR2MgmtCrashUploadServerIP.setStatus("current")


class _EtsysR2MgmtCrashUploadDirectory_Type(OctetString):
    """Custom type etsysR2MgmtCrashUploadDirectory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EtsysR2MgmtCrashUploadDirectory_Type.__name__ = "OctetString"
_EtsysR2MgmtCrashUploadDirectory_Object = MibScalar
etsysR2MgmtCrashUploadDirectory = _EtsysR2MgmtCrashUploadDirectory_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 4, 3),
    _EtsysR2MgmtCrashUploadDirectory_Type()
)
etsysR2MgmtCrashUploadDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysR2MgmtCrashUploadDirectory.setStatus("current")
_EtsysR2MgmtUplineDumpMode_Type = EnabledStatus
_EtsysR2MgmtUplineDumpMode_Object = MibScalar
etsysR2MgmtUplineDumpMode = _EtsysR2MgmtUplineDumpMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 1, 4, 4),
    _EtsysR2MgmtUplineDumpMode_Type()
)
etsysR2MgmtUplineDumpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysR2MgmtUplineDumpMode.setStatus("current")
_EtsysR2MgmtConformance_ObjectIdentity = ObjectIdentity
etsysR2MgmtConformance = _EtsysR2MgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 2)
)
_EtsysR2MgmtGroups_ObjectIdentity = ObjectIdentity
etsysR2MgmtGroups = _EtsysR2MgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 2, 1)
)
_EtsysR2MgmtCompliances_ObjectIdentity = ObjectIdentity
etsysR2MgmtCompliances = _EtsysR2MgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 2, 2)
)

# Managed Objects groups

etsysR2MgmtBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 2, 1, 1)
)
etsysR2MgmtBaseGroup.setObjects(
      *(("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtMemorySize"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtWEBInterface"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtTelnetInterface"))
)
if mibBuilder.loadTexts:
    etsysR2MgmtBaseGroup.setStatus("deprecated")

etsysR2MgmtCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 2, 1, 2)
)
etsysR2MgmtCountersGroup.setObjects(
      *(("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtPowerups"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtResets"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtUnsolicitedResets"))
)
if mibBuilder.loadTexts:
    etsysR2MgmtCountersGroup.setStatus("current")

etsysR2MgmtErrLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 2, 1, 3)
)
etsysR2MgmtErrLogGroup.setObjects(
      *(("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtErrLogNumEntries"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtErrLogIndex"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtErrLogTimeStamp"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtErrLogResetNumber"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtErrLogInfo"))
)
if mibBuilder.loadTexts:
    etsysR2MgmtErrLogGroup.setStatus("current")

etsysR2MgmtLoaderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 2, 1, 4)
)
etsysR2MgmtLoaderGroup.setObjects(
      *(("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtCrashUploadUseBootp"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtCrashUploadServerIP"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtCrashUploadDirectory"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtUplineDumpMode"))
)
if mibBuilder.loadTexts:
    etsysR2MgmtLoaderGroup.setStatus("current")

etsysR2MgmtBaseGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 2, 1, 5)
)
etsysR2MgmtBaseGroupV2.setObjects(
      *(("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtMemorySize"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtWEBInterface"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtTelnetInterface"),
        ("ENTERASYS-R2MGMT-MIB", "etsysR2MgmtVlan"))
)
if mibBuilder.loadTexts:
    etsysR2MgmtBaseGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysR2MgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysR2MgmtCompliance.setStatus(
        "deprecated"
    )

etsysR2MgmtComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 11, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysR2MgmtComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-R2MGMT-MIB",
    **{"enterasysR2MgmtMIB": enterasysR2MgmtMIB,
       "etsysR2MgmtObjects": etsysR2MgmtObjects,
       "etsysR2MgmtParams": etsysR2MgmtParams,
       "etsysR2MgmtMemorySize": etsysR2MgmtMemorySize,
       "etsysR2MgmtWEBInterface": etsysR2MgmtWEBInterface,
       "etsysR2MgmtTelnetInterface": etsysR2MgmtTelnetInterface,
       "etsysR2MgmtVlan": etsysR2MgmtVlan,
       "etsysR2MgmtCounters": etsysR2MgmtCounters,
       "etsysR2MgmtPowerups": etsysR2MgmtPowerups,
       "etsysR2MgmtResets": etsysR2MgmtResets,
       "etsysR2MgmtUnsolicitedResets": etsysR2MgmtUnsolicitedResets,
       "etsysR2MgmtErrorLog": etsysR2MgmtErrorLog,
       "etsysR2MgmtErrLogNumEntries": etsysR2MgmtErrLogNumEntries,
       "etsysR2MgmtErrLogTable": etsysR2MgmtErrLogTable,
       "etsysR2MgmtErrLogEntry": etsysR2MgmtErrLogEntry,
       "etsysR2MgmtErrLogIndex": etsysR2MgmtErrLogIndex,
       "etsysR2MgmtErrLogTimeStamp": etsysR2MgmtErrLogTimeStamp,
       "etsysR2MgmtErrLogResetNumber": etsysR2MgmtErrLogResetNumber,
       "etsysR2MgmtErrLogInfo": etsysR2MgmtErrLogInfo,
       "etsysR2MgmtLoader": etsysR2MgmtLoader,
       "etsysR2MgmtCrashUploadUseBootp": etsysR2MgmtCrashUploadUseBootp,
       "etsysR2MgmtCrashUploadServerIP": etsysR2MgmtCrashUploadServerIP,
       "etsysR2MgmtCrashUploadDirectory": etsysR2MgmtCrashUploadDirectory,
       "etsysR2MgmtUplineDumpMode": etsysR2MgmtUplineDumpMode,
       "etsysR2MgmtConformance": etsysR2MgmtConformance,
       "etsysR2MgmtGroups": etsysR2MgmtGroups,
       "etsysR2MgmtBaseGroup": etsysR2MgmtBaseGroup,
       "etsysR2MgmtCountersGroup": etsysR2MgmtCountersGroup,
       "etsysR2MgmtErrLogGroup": etsysR2MgmtErrLogGroup,
       "etsysR2MgmtLoaderGroup": etsysR2MgmtLoaderGroup,
       "etsysR2MgmtBaseGroupV2": etsysR2MgmtBaseGroupV2,
       "etsysR2MgmtCompliances": etsysR2MgmtCompliances,
       "etsysR2MgmtCompliance": etsysR2MgmtCompliance,
       "etsysR2MgmtComplianceV2": etsysR2MgmtComplianceV2}
)
