# SNMP MIB module (CISCO-IF-CALL-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IF-CALL-SERVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:08 2024
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

(BulkConfigResult,
 ConfigIterator) = mibBuilder.importSymbols(
    "CISCO-TC",
    "BulkConfigResult",
    "ConfigIterator")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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

ciscoIfCallServiceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968)
)
ciscoIfCallServiceMIB.setRevisions(
        ("2003-04-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CIfCallServiceOperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("oosPending", 3),
          ("outOfService", 2))
    )



class CIfCallServiceAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forcedOutOfService", 2),
          ("gracefulOutOfService", 3),
          ("inService", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIfCallServiceMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIfCallServiceMIBNotifs = _CiscoIfCallServiceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 0)
)
_CiscoIfCallServiceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIfCallServiceMIBObjects = _CiscoIfCallServiceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 1)
)
_CicServiceConfig_ObjectIdentity = ObjectIdentity
cicServiceConfig = _CicServiceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1)
)
_CicServiceTable_Object = MibTable
cicServiceTable = _CicServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cicServiceTable.setStatus("current")
_CicServiceEntry_Object = MibTableRow
cicServiceEntry = _CicServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1)
)
cicServiceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cicServiceEntry.setStatus("current")
_CicServiceOperState_Type = CIfCallServiceOperState
_CicServiceOperState_Object = MibTableColumn
cicServiceOperState = _CicServiceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 1),
    _CicServiceOperState_Type()
)
cicServiceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cicServiceOperState.setStatus("current")


class _CicServiceAdminState_Type(CIfCallServiceAdminState):
    """Custom type cicServiceAdminState based on CIfCallServiceAdminState"""


_CicServiceAdminState_Object = MibTableColumn
cicServiceAdminState = _CicServiceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 2),
    _CicServiceAdminState_Type()
)
cicServiceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicServiceAdminState.setStatus("current")


class _CicServiceGraceTime_Type(Unsigned32):
    """Custom type cicServiceGraceTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CicServiceGraceTime_Type.__name__ = "Unsigned32"
_CicServiceGraceTime_Object = MibTableColumn
cicServiceGraceTime = _CicServiceGraceTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 3),
    _CicServiceGraceTime_Type()
)
cicServiceGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicServiceGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    cicServiceGraceTime.setUnits("seconds")


class _CicServiceRepetition_Type(ConfigIterator):
    """Custom type cicServiceRepetition based on ConfigIterator"""
    defaultValue = 1


_CicServiceRepetition_Object = MibTableColumn
cicServiceRepetition = _CicServiceRepetition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 4),
    _CicServiceRepetition_Type()
)
cicServiceRepetition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicServiceRepetition.setStatus("current")
_CicServiceRepeatOwner_Type = OwnerString
_CicServiceRepeatOwner_Object = MibTableColumn
cicServiceRepeatOwner = _CicServiceRepeatOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 5),
    _CicServiceRepeatOwner_Type()
)
cicServiceRepeatOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cicServiceRepeatOwner.setStatus("current")
_CicServiceRepeatResult_Type = BulkConfigResult
_CicServiceRepeatResult_Object = MibTableColumn
cicServiceRepeatResult = _CicServiceRepeatResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 6),
    _CicServiceRepeatResult_Type()
)
cicServiceRepeatResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cicServiceRepeatResult.setStatus("current")
_CiscoIfCallServiceMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIfCallServiceMIBConformance = _CiscoIfCallServiceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 2)
)
_CicServiceCompliances_ObjectIdentity = ObjectIdentity
cicServiceCompliances = _CicServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 1)
)
_CicServiceGroups_ObjectIdentity = ObjectIdentity
cicServiceGroups = _CicServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 2)
)

# Managed Objects groups

cicServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 2, 1)
)
cicServiceGroup.setObjects(
      *(("CISCO-IF-CALL-SERVICE-MIB", "cicServiceOperState"),
        ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceAdminState"),
        ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceGraceTime"),
        ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepetition"),
        ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepeatOwner"),
        ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepeatResult"))
)
if mibBuilder.loadTexts:
    cicServiceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cicServiceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cicServiceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IF-CALL-SERVICE-MIB",
    **{"CIfCallServiceOperState": CIfCallServiceOperState,
       "CIfCallServiceAdminState": CIfCallServiceAdminState,
       "ciscoIfCallServiceMIB": ciscoIfCallServiceMIB,
       "ciscoIfCallServiceMIBNotifs": ciscoIfCallServiceMIBNotifs,
       "ciscoIfCallServiceMIBObjects": ciscoIfCallServiceMIBObjects,
       "cicServiceConfig": cicServiceConfig,
       "cicServiceTable": cicServiceTable,
       "cicServiceEntry": cicServiceEntry,
       "cicServiceOperState": cicServiceOperState,
       "cicServiceAdminState": cicServiceAdminState,
       "cicServiceGraceTime": cicServiceGraceTime,
       "cicServiceRepetition": cicServiceRepetition,
       "cicServiceRepeatOwner": cicServiceRepeatOwner,
       "cicServiceRepeatResult": cicServiceRepeatResult,
       "ciscoIfCallServiceMIBConformance": ciscoIfCallServiceMIBConformance,
       "cicServiceCompliances": cicServiceCompliances,
       "cicServiceCompliance": cicServiceCompliance,
       "cicServiceGroups": cicServiceGroups,
       "cicServiceGroup": cicServiceGroup}
)
