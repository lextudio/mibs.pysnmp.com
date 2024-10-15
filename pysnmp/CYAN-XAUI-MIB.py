# SNMP MIB module (CYAN-XAUI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-XAUI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:18 2024
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

(cyanEntityModules,) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "cyanEntityModules")

(CyanAdminStateTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSecServiceStateTc")

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

cyanXauiModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170)
)
cyanXauiModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanXauiMibObjects_ObjectIdentity = ObjectIdentity
cyanXauiMibObjects = _CyanXauiMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1)
)
_CyanXauiTable_Object = MibTable
cyanXauiTable = _CyanXauiTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1)
)
if mibBuilder.loadTexts:
    cyanXauiTable.setStatus("current")
_CyanXauiEntry_Object = MibTableRow
cyanXauiEntry = _CyanXauiEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1)
)
cyanXauiEntry.setIndexNames(
    (0, "CYAN-XAUI-MIB", "cyanXauiShelfId"),
    (0, "CYAN-XAUI-MIB", "cyanXauiModuleId"),
    (0, "CYAN-XAUI-MIB", "cyanXauiXauiId"),
)
if mibBuilder.loadTexts:
    cyanXauiEntry.setStatus("current")


class _CyanXauiShelfId_Type(Unsigned32):
    """Custom type cyanXauiShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanXauiShelfId_Type.__name__ = "Unsigned32"
_CyanXauiShelfId_Object = MibTableColumn
cyanXauiShelfId = _CyanXauiShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 1),
    _CyanXauiShelfId_Type()
)
cyanXauiShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanXauiShelfId.setStatus("current")
_CyanXauiModuleId_Type = Unsigned32
_CyanXauiModuleId_Object = MibTableColumn
cyanXauiModuleId = _CyanXauiModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 2),
    _CyanXauiModuleId_Type()
)
cyanXauiModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanXauiModuleId.setStatus("current")
_CyanXauiXauiId_Type = Unsigned32
_CyanXauiXauiId_Object = MibTableColumn
cyanXauiXauiId = _CyanXauiXauiId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 3),
    _CyanXauiXauiId_Type()
)
cyanXauiXauiId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanXauiXauiId.setStatus("current")
_CyanXauiAdminState_Type = CyanAdminStateTc
_CyanXauiAdminState_Object = MibTableColumn
cyanXauiAdminState = _CyanXauiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 4),
    _CyanXauiAdminState_Type()
)
cyanXauiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXauiAdminState.setStatus("current")
_CyanXauiAutoinserviceSoakTimeSec_Type = Integer32
_CyanXauiAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanXauiAutoinserviceSoakTimeSec = _CyanXauiAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 5),
    _CyanXauiAutoinserviceSoakTimeSec_Type()
)
cyanXauiAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXauiAutoinserviceSoakTimeSec.setStatus("current")
_CyanXauiOperState_Type = CyanOpStateTc
_CyanXauiOperState_Object = MibTableColumn
cyanXauiOperState = _CyanXauiOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 6),
    _CyanXauiOperState_Type()
)
cyanXauiOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXauiOperState.setStatus("current")
_CyanXauiOperStateQual_Type = CyanOpStateQualTc
_CyanXauiOperStateQual_Object = MibTableColumn
cyanXauiOperStateQual = _CyanXauiOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 7),
    _CyanXauiOperStateQual_Type()
)
cyanXauiOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXauiOperStateQual.setStatus("current")
_CyanXauiPortSpeedMbps_Type = Unsigned32
_CyanXauiPortSpeedMbps_Object = MibTableColumn
cyanXauiPortSpeedMbps = _CyanXauiPortSpeedMbps_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 8),
    _CyanXauiPortSpeedMbps_Type()
)
cyanXauiPortSpeedMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXauiPortSpeedMbps.setStatus("current")
_CyanXauiSecServState_Type = CyanSecServiceStateTc
_CyanXauiSecServState_Object = MibTableColumn
cyanXauiSecServState = _CyanXauiSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 1, 1, 1, 9),
    _CyanXauiSecServState_Type()
)
cyanXauiSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanXauiSecServState.setStatus("current")

# Managed Objects groups

cyanXauiObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 20)
)
cyanXauiObjectGroup.setObjects(
      *(("CYAN-XAUI-MIB", "cyanXauiAdminState"),
        ("CYAN-XAUI-MIB", "cyanXauiAutoinserviceSoakTimeSec"),
        ("CYAN-XAUI-MIB", "cyanXauiOperState"),
        ("CYAN-XAUI-MIB", "cyanXauiOperStateQual"),
        ("CYAN-XAUI-MIB", "cyanXauiPortSpeedMbps"),
        ("CYAN-XAUI-MIB", "cyanXauiSecServState"))
)
if mibBuilder.loadTexts:
    cyanXauiObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanXauiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 170, 30)
)
if mibBuilder.loadTexts:
    cyanXauiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-XAUI-MIB",
    **{"cyanXauiModule": cyanXauiModule,
       "cyanXauiMibObjects": cyanXauiMibObjects,
       "cyanXauiTable": cyanXauiTable,
       "cyanXauiEntry": cyanXauiEntry,
       "cyanXauiShelfId": cyanXauiShelfId,
       "cyanXauiModuleId": cyanXauiModuleId,
       "cyanXauiXauiId": cyanXauiXauiId,
       "cyanXauiAdminState": cyanXauiAdminState,
       "cyanXauiAutoinserviceSoakTimeSec": cyanXauiAutoinserviceSoakTimeSec,
       "cyanXauiOperState": cyanXauiOperState,
       "cyanXauiOperStateQual": cyanXauiOperStateQual,
       "cyanXauiPortSpeedMbps": cyanXauiPortSpeedMbps,
       "cyanXauiSecServState": cyanXauiSecServState,
       "cyanXauiObjectGroup": cyanXauiObjectGroup,
       "cyanXauiCompliance": cyanXauiCompliance}
)
