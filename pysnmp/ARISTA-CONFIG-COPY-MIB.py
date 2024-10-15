# SNMP MIB module (ARISTA-CONFIG-COPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-CONFIG-COPY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:18 2024
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

(aristaMibs,
 aristaModules,
 aristaProducts) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs",
    "aristaModules",
    "aristaProducts")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

aristaConfigCopyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7)
)
aristaConfigCopyMIB.setRevisions(
        ("2014-08-15 00:00",
         "2013-02-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigCopyState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("completed", 3),
          ("failed", 4),
          ("inactive", 0),
          ("running", 2),
          ("scheduled", 1))
    )



class ConfigCopyFailureCause(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("timeout", 2),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AristaConfigCopyCommandTable_Object = MibTable
aristaConfigCopyCommandTable = _AristaConfigCopyCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1)
)
if mibBuilder.loadTexts:
    aristaConfigCopyCommandTable.setStatus("current")
_AristaConfigCopyCommandEntry_Object = MibTableRow
aristaConfigCopyCommandEntry = _AristaConfigCopyCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1)
)
aristaConfigCopyCommandEntry.setIndexNames(
    (0, "ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyName"),
    (0, "ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyId"),
)
if mibBuilder.loadTexts:
    aristaConfigCopyCommandEntry.setStatus("current")


class _AristaConfigCopyName_Type(DisplayString):
    """Custom type aristaConfigCopyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AristaConfigCopyName_Type.__name__ = "DisplayString"
_AristaConfigCopyName_Object = MibTableColumn
aristaConfigCopyName = _AristaConfigCopyName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 1),
    _AristaConfigCopyName_Type()
)
aristaConfigCopyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaConfigCopyName.setStatus("current")
_AristaConfigCopyId_Type = Unsigned32
_AristaConfigCopyId_Object = MibTableColumn
aristaConfigCopyId = _AristaConfigCopyId_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 2),
    _AristaConfigCopyId_Type()
)
aristaConfigCopyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaConfigCopyId.setStatus("current")


class _AristaConfigCopySourceUri_Type(DisplayString):
    """Custom type aristaConfigCopySourceUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AristaConfigCopySourceUri_Type.__name__ = "DisplayString"
_AristaConfigCopySourceUri_Object = MibTableColumn
aristaConfigCopySourceUri = _AristaConfigCopySourceUri_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 3),
    _AristaConfigCopySourceUri_Type()
)
aristaConfigCopySourceUri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aristaConfigCopySourceUri.setStatus("current")


class _AristaConfigCopyDestUri_Type(DisplayString):
    """Custom type aristaConfigCopyDestUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AristaConfigCopyDestUri_Type.__name__ = "DisplayString"
_AristaConfigCopyDestUri_Object = MibTableColumn
aristaConfigCopyDestUri = _AristaConfigCopyDestUri_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 4),
    _AristaConfigCopyDestUri_Type()
)
aristaConfigCopyDestUri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aristaConfigCopyDestUri.setStatus("current")
_AristaConfigCopyState_Type = ConfigCopyState
_AristaConfigCopyState_Object = MibTableColumn
aristaConfigCopyState = _AristaConfigCopyState_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 5),
    _AristaConfigCopyState_Type()
)
aristaConfigCopyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaConfigCopyState.setStatus("current")


class _AristaConfigCopyTimeout_Type(Unsigned32):
    """Custom type aristaConfigCopyTimeout based on Unsigned32"""
    defaultValue = 60


_AristaConfigCopyTimeout_Object = MibTableColumn
aristaConfigCopyTimeout = _AristaConfigCopyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 6),
    _AristaConfigCopyTimeout_Type()
)
aristaConfigCopyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aristaConfigCopyTimeout.setStatus("current")
_AristaConfigCopyTimeStarted_Type = DateAndTime
_AristaConfigCopyTimeStarted_Object = MibTableColumn
aristaConfigCopyTimeStarted = _AristaConfigCopyTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 7),
    _AristaConfigCopyTimeStarted_Type()
)
aristaConfigCopyTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaConfigCopyTimeStarted.setStatus("current")
_AristaConfigCopyTimeCompleted_Type = DateAndTime
_AristaConfigCopyTimeCompleted_Object = MibTableColumn
aristaConfigCopyTimeCompleted = _AristaConfigCopyTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 8),
    _AristaConfigCopyTimeCompleted_Type()
)
aristaConfigCopyTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaConfigCopyTimeCompleted.setStatus("current")
_AristaConfigCopyFailureCause_Type = ConfigCopyFailureCause
_AristaConfigCopyFailureCause_Object = MibTableColumn
aristaConfigCopyFailureCause = _AristaConfigCopyFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 9),
    _AristaConfigCopyFailureCause_Type()
)
aristaConfigCopyFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaConfigCopyFailureCause.setStatus("current")
_AristaConfigCopyFailureMessage_Type = DisplayString
_AristaConfigCopyFailureMessage_Object = MibTableColumn
aristaConfigCopyFailureMessage = _AristaConfigCopyFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 10),
    _AristaConfigCopyFailureMessage_Type()
)
aristaConfigCopyFailureMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaConfigCopyFailureMessage.setStatus("current")
_AristaConfigCopyRowStatus_Type = RowStatus
_AristaConfigCopyRowStatus_Object = MibTableColumn
aristaConfigCopyRowStatus = _AristaConfigCopyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 11),
    _AristaConfigCopyRowStatus_Type()
)
aristaConfigCopyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aristaConfigCopyRowStatus.setStatus("current")
_AristaConfigCopyConformance_ObjectIdentity = ObjectIdentity
aristaConfigCopyConformance = _AristaConfigCopyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 2)
)
_AristaConfigCopyCompliances_ObjectIdentity = ObjectIdentity
aristaConfigCopyCompliances = _AristaConfigCopyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 1)
)
_AristaConfigCopyGroups_ObjectIdentity = ObjectIdentity
aristaConfigCopyGroups = _AristaConfigCopyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 2)
)

# Managed Objects groups

aristaConfigCopyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 2, 1)
)
aristaConfigCopyObjectsGroup.setObjects(
      *(("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopySourceUri"),
        ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyDestUri"),
        ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyState"),
        ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeout"),
        ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeStarted"),
        ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeCompleted"),
        ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyFailureCause"),
        ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyFailureMessage"),
        ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyRowStatus"))
)
if mibBuilder.loadTexts:
    aristaConfigCopyObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaConfigCopyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aristaConfigCopyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-CONFIG-COPY-MIB",
    **{"ConfigCopyState": ConfigCopyState,
       "ConfigCopyFailureCause": ConfigCopyFailureCause,
       "aristaConfigCopyMIB": aristaConfigCopyMIB,
       "aristaConfigCopyCommandTable": aristaConfigCopyCommandTable,
       "aristaConfigCopyCommandEntry": aristaConfigCopyCommandEntry,
       "aristaConfigCopyName": aristaConfigCopyName,
       "aristaConfigCopyId": aristaConfigCopyId,
       "aristaConfigCopySourceUri": aristaConfigCopySourceUri,
       "aristaConfigCopyDestUri": aristaConfigCopyDestUri,
       "aristaConfigCopyState": aristaConfigCopyState,
       "aristaConfigCopyTimeout": aristaConfigCopyTimeout,
       "aristaConfigCopyTimeStarted": aristaConfigCopyTimeStarted,
       "aristaConfigCopyTimeCompleted": aristaConfigCopyTimeCompleted,
       "aristaConfigCopyFailureCause": aristaConfigCopyFailureCause,
       "aristaConfigCopyFailureMessage": aristaConfigCopyFailureMessage,
       "aristaConfigCopyRowStatus": aristaConfigCopyRowStatus,
       "aristaConfigCopyConformance": aristaConfigCopyConformance,
       "aristaConfigCopyCompliances": aristaConfigCopyCompliances,
       "aristaConfigCopyCompliance": aristaConfigCopyCompliance,
       "aristaConfigCopyGroups": aristaConfigCopyGroups,
       "aristaConfigCopyObjectsGroup": aristaConfigCopyObjectsGroup}
)
