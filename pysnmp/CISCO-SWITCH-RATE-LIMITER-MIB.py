# SNMP MIB module (CISCO-SWITCH-RATE-LIMITER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-RATE-LIMITER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:16 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSwitchRateLimiterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 773)
)
ciscoSwitchRateLimiterMIB.setRevisions(
        ("2011-05-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSwitchRateLimiterMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSwitchRateLimiterMIBNotifs = _CiscoSwitchRateLimiterMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 0)
)
_CiscoSwitchRateLimiterMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSwitchRateLimiterMIBObjects = _CiscoSwitchRateLimiterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1)
)
_CsrlRateLimiterInfo_ObjectIdentity = ObjectIdentity
csrlRateLimiterInfo = _CsrlRateLimiterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1)
)
_CsrlRateLimiterClassTable_Object = MibTable
csrlRateLimiterClassTable = _CsrlRateLimiterClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1)
)
if mibBuilder.loadTexts:
    csrlRateLimiterClassTable.setStatus("current")
_CsrlRateLimiterClassEntry_Object = MibTableRow
csrlRateLimiterClassEntry = _CsrlRateLimiterClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1, 1)
)
csrlRateLimiterClassEntry.setIndexNames(
    (0, "CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassId"),
)
if mibBuilder.loadTexts:
    csrlRateLimiterClassEntry.setStatus("current")


class _CsrlRateLimiterClassId_Type(Unsigned32):
    """Custom type csrlRateLimiterClassId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CsrlRateLimiterClassId_Type.__name__ = "Unsigned32"
_CsrlRateLimiterClassId_Object = MibTableColumn
csrlRateLimiterClassId = _CsrlRateLimiterClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1, 1, 1),
    _CsrlRateLimiterClassId_Type()
)
csrlRateLimiterClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csrlRateLimiterClassId.setStatus("current")
_CsrlRateLimiterClassDescr_Type = SnmpAdminString
_CsrlRateLimiterClassDescr_Object = MibTableColumn
csrlRateLimiterClassDescr = _CsrlRateLimiterClassDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 1, 1, 1, 2),
    _CsrlRateLimiterClassDescr_Type()
)
csrlRateLimiterClassDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrlRateLimiterClassDescr.setStatus("current")
_CsrlGlobalRateLimiter_ObjectIdentity = ObjectIdentity
csrlGlobalRateLimiter = _CsrlGlobalRateLimiter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2)
)
_CsrlGlobalRateLimiterTable_Object = MibTable
csrlGlobalRateLimiterTable = _CsrlGlobalRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterTable.setStatus("current")
_CsrlGlobalRateLimiterEntry_Object = MibTableRow
csrlGlobalRateLimiterEntry = _CsrlGlobalRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1)
)
csrlGlobalRateLimiterEntry.setIndexNames(
    (0, "CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassId"),
)
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterEntry.setStatus("current")


class _CsrlGlobalRateLimiterConfigured_Type(Integer32):
    """Custom type csrlGlobalRateLimiterConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_CsrlGlobalRateLimiterConfigured_Type.__name__ = "Integer32"
_CsrlGlobalRateLimiterConfigured_Object = MibTableColumn
csrlGlobalRateLimiterConfigured = _CsrlGlobalRateLimiterConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 1),
    _CsrlGlobalRateLimiterConfigured_Type()
)
csrlGlobalRateLimiterConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterConfigured.setStatus("current")
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterConfigured.setUnits("packets per second")
_CsrlGlobalRateLimiterAllowed_Type = Counter64
_CsrlGlobalRateLimiterAllowed_Object = MibTableColumn
csrlGlobalRateLimiterAllowed = _CsrlGlobalRateLimiterAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 2),
    _CsrlGlobalRateLimiterAllowed_Type()
)
csrlGlobalRateLimiterAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterAllowed.setStatus("current")
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterAllowed.setUnits("packets")
_CsrlGlobalRateLimiterDropped_Type = Counter64
_CsrlGlobalRateLimiterDropped_Object = MibTableColumn
csrlGlobalRateLimiterDropped = _CsrlGlobalRateLimiterDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 3),
    _CsrlGlobalRateLimiterDropped_Type()
)
csrlGlobalRateLimiterDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterDropped.setStatus("current")
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterDropped.setUnits("packets")
_CsrlGlobalRateLimiterTotal_Type = Counter64
_CsrlGlobalRateLimiterTotal_Object = MibTableColumn
csrlGlobalRateLimiterTotal = _CsrlGlobalRateLimiterTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 2, 1, 1, 4),
    _CsrlGlobalRateLimiterTotal_Type()
)
csrlGlobalRateLimiterTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterTotal.setStatus("current")
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterTotal.setUnits("packets")
_CsrlLocalRateLimiter_ObjectIdentity = ObjectIdentity
csrlLocalRateLimiter = _CsrlLocalRateLimiter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3)
)
_CsrlLocalRateLimiterTable_Object = MibTable
csrlLocalRateLimiterTable = _CsrlLocalRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1)
)
if mibBuilder.loadTexts:
    csrlLocalRateLimiterTable.setStatus("current")
_CsrlLocalRateLimiterEntry_Object = MibTableRow
csrlLocalRateLimiterEntry = _CsrlLocalRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1)
)
csrlLocalRateLimiterEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassId"),
)
if mibBuilder.loadTexts:
    csrlLocalRateLimiterEntry.setStatus("current")


class _CsrlLocalRateLimiterConfigured_Type(Integer32):
    """Custom type csrlLocalRateLimiterConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, -2),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_CsrlLocalRateLimiterConfigured_Type.__name__ = "Integer32"
_CsrlLocalRateLimiterConfigured_Object = MibTableColumn
csrlLocalRateLimiterConfigured = _CsrlLocalRateLimiterConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 1),
    _CsrlLocalRateLimiterConfigured_Type()
)
csrlLocalRateLimiterConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csrlLocalRateLimiterConfigured.setStatus("current")
if mibBuilder.loadTexts:
    csrlLocalRateLimiterConfigured.setUnits("packets per second")
_CsrlLocalRateLimiterAllowed_Type = Counter64
_CsrlLocalRateLimiterAllowed_Object = MibTableColumn
csrlLocalRateLimiterAllowed = _CsrlLocalRateLimiterAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 2),
    _CsrlLocalRateLimiterAllowed_Type()
)
csrlLocalRateLimiterAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrlLocalRateLimiterAllowed.setStatus("current")
if mibBuilder.loadTexts:
    csrlLocalRateLimiterAllowed.setUnits("packets")
_CsrlLocalRateLimiterDropped_Type = Counter64
_CsrlLocalRateLimiterDropped_Object = MibTableColumn
csrlLocalRateLimiterDropped = _CsrlLocalRateLimiterDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 3),
    _CsrlLocalRateLimiterDropped_Type()
)
csrlLocalRateLimiterDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrlLocalRateLimiterDropped.setStatus("current")
if mibBuilder.loadTexts:
    csrlLocalRateLimiterDropped.setUnits("packets")
_CsrlLocalRateLimiterTotal_Type = Counter64
_CsrlLocalRateLimiterTotal_Object = MibTableColumn
csrlLocalRateLimiterTotal = _CsrlLocalRateLimiterTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 1, 3, 1, 1, 4),
    _CsrlLocalRateLimiterTotal_Type()
)
csrlLocalRateLimiterTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csrlLocalRateLimiterTotal.setStatus("current")
if mibBuilder.loadTexts:
    csrlLocalRateLimiterTotal.setUnits("packets")
_CiscoSwitchRateLimiterMIBConform_ObjectIdentity = ObjectIdentity
ciscoSwitchRateLimiterMIBConform = _CiscoSwitchRateLimiterMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 2)
)
_CsrlMIBCompliances_ObjectIdentity = ObjectIdentity
csrlMIBCompliances = _CsrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 1)
)
_CsrlMIBGroups_ObjectIdentity = ObjectIdentity
csrlMIBGroups = _CsrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2)
)

# Managed Objects groups

csrlRateLimiterClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2, 1)
)
csrlRateLimiterClassGroup.setObjects(
    ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlRateLimiterClassDescr")
)
if mibBuilder.loadTexts:
    csrlRateLimiterClassGroup.setStatus("current")

csrlGlobalRateLimiterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2, 2)
)
csrlGlobalRateLimiterGroup.setObjects(
      *(("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterConfigured"),
        ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterAllowed"),
        ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterDropped"),
        ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlGlobalRateLimiterTotal"))
)
if mibBuilder.loadTexts:
    csrlGlobalRateLimiterGroup.setStatus("current")

csrlLocalRateLimiterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 2, 3)
)
csrlLocalRateLimiterGroup.setObjects(
      *(("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterConfigured"),
        ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterAllowed"),
        ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterDropped"),
        ("CISCO-SWITCH-RATE-LIMITER-MIB", "csrlLocalRateLimiterTotal"))
)
if mibBuilder.loadTexts:
    csrlLocalRateLimiterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

csrlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 773, 2, 1, 1)
)
if mibBuilder.loadTexts:
    csrlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-RATE-LIMITER-MIB",
    **{"ciscoSwitchRateLimiterMIB": ciscoSwitchRateLimiterMIB,
       "ciscoSwitchRateLimiterMIBNotifs": ciscoSwitchRateLimiterMIBNotifs,
       "ciscoSwitchRateLimiterMIBObjects": ciscoSwitchRateLimiterMIBObjects,
       "csrlRateLimiterInfo": csrlRateLimiterInfo,
       "csrlRateLimiterClassTable": csrlRateLimiterClassTable,
       "csrlRateLimiterClassEntry": csrlRateLimiterClassEntry,
       "csrlRateLimiterClassId": csrlRateLimiterClassId,
       "csrlRateLimiterClassDescr": csrlRateLimiterClassDescr,
       "csrlGlobalRateLimiter": csrlGlobalRateLimiter,
       "csrlGlobalRateLimiterTable": csrlGlobalRateLimiterTable,
       "csrlGlobalRateLimiterEntry": csrlGlobalRateLimiterEntry,
       "csrlGlobalRateLimiterConfigured": csrlGlobalRateLimiterConfigured,
       "csrlGlobalRateLimiterAllowed": csrlGlobalRateLimiterAllowed,
       "csrlGlobalRateLimiterDropped": csrlGlobalRateLimiterDropped,
       "csrlGlobalRateLimiterTotal": csrlGlobalRateLimiterTotal,
       "csrlLocalRateLimiter": csrlLocalRateLimiter,
       "csrlLocalRateLimiterTable": csrlLocalRateLimiterTable,
       "csrlLocalRateLimiterEntry": csrlLocalRateLimiterEntry,
       "csrlLocalRateLimiterConfigured": csrlLocalRateLimiterConfigured,
       "csrlLocalRateLimiterAllowed": csrlLocalRateLimiterAllowed,
       "csrlLocalRateLimiterDropped": csrlLocalRateLimiterDropped,
       "csrlLocalRateLimiterTotal": csrlLocalRateLimiterTotal,
       "ciscoSwitchRateLimiterMIBConform": ciscoSwitchRateLimiterMIBConform,
       "csrlMIBCompliances": csrlMIBCompliances,
       "csrlMIBCompliance": csrlMIBCompliance,
       "csrlMIBGroups": csrlMIBGroups,
       "csrlRateLimiterClassGroup": csrlRateLimiterClassGroup,
       "csrlGlobalRateLimiterGroup": csrlGlobalRateLimiterGroup,
       "csrlLocalRateLimiterGroup": csrlLocalRateLimiterGroup}
)
