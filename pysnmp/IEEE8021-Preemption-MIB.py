# SNMP MIB module (IEEE8021-Preemption-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-Preemption-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:36 2024
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

(ieee8021BridgeBaseComponentId,
 ieee8021BridgeBasePort) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId",
    "ieee8021BridgeBasePort")

(IEEE8021PriorityValue,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue",
    "ieee802dot1mibs")

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

ieee8021PreemptionMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 29)
)
ieee8021PreemptionMib.setRevisions(
        ("2018-06-21 00:00",
         "2016-08-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021PreemptionNotifications_ObjectIdentity = ObjectIdentity
ieee8021PreemptionNotifications = _Ieee8021PreemptionNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 29, 0)
)
_Ieee8021PreemptionObjects_ObjectIdentity = ObjectIdentity
ieee8021PreemptionObjects = _Ieee8021PreemptionObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 29, 1)
)
_Ieee8021PreemptionParameters_ObjectIdentity = ObjectIdentity
ieee8021PreemptionParameters = _Ieee8021PreemptionParameters_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1)
)
_Ieee8021PreemptionParameterTable_Object = MibTable
ieee8021PreemptionParameterTable = _Ieee8021PreemptionParameterTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021PreemptionParameterTable.setStatus("current")
_Ieee8021PreemptionParameterEntry_Object = MibTableRow
ieee8021PreemptionParameterEntry = _Ieee8021PreemptionParameterEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1, 1)
)
ieee8021PreemptionParameterEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-Preemption-MIB", "ieee8021PreemptionPriority"),
)
if mibBuilder.loadTexts:
    ieee8021PreemptionParameterEntry.setStatus("current")
_Ieee8021PreemptionPriority_Type = IEEE8021PriorityValue
_Ieee8021PreemptionPriority_Object = MibTableColumn
ieee8021PreemptionPriority = _Ieee8021PreemptionPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1, 1, 1),
    _Ieee8021PreemptionPriority_Type()
)
ieee8021PreemptionPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PreemptionPriority.setStatus("current")


class _Ieee8021FramePreemptionAdminStatus_Type(Integer32):
    """Custom type ieee8021FramePreemptionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("express", 1),
          ("preemptible", 2))
    )


_Ieee8021FramePreemptionAdminStatus_Type.__name__ = "Integer32"
_Ieee8021FramePreemptionAdminStatus_Object = MibTableColumn
ieee8021FramePreemptionAdminStatus = _Ieee8021FramePreemptionAdminStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 1, 1, 2),
    _Ieee8021FramePreemptionAdminStatus_Type()
)
ieee8021FramePreemptionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021FramePreemptionAdminStatus.setStatus("current")
_Ieee8021PreemptionConfigTable_Object = MibTable
ieee8021PreemptionConfigTable = _Ieee8021PreemptionConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021PreemptionConfigTable.setStatus("current")
_Ieee8021PreemptionConfigEntry_Object = MibTableRow
ieee8021PreemptionConfigEntry = _Ieee8021PreemptionConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1)
)
ieee8021PreemptionConfigEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021PreemptionConfigEntry.setStatus("current")
_Ieee8021FramePreemptionHoldAdvance_Type = Unsigned32
_Ieee8021FramePreemptionHoldAdvance_Object = MibTableColumn
ieee8021FramePreemptionHoldAdvance = _Ieee8021FramePreemptionHoldAdvance_Object(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 1),
    _Ieee8021FramePreemptionHoldAdvance_Type()
)
ieee8021FramePreemptionHoldAdvance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FramePreemptionHoldAdvance.setStatus("current")
_Ieee8021FramePreemptionReleaseAdvance_Type = Unsigned32
_Ieee8021FramePreemptionReleaseAdvance_Object = MibTableColumn
ieee8021FramePreemptionReleaseAdvance = _Ieee8021FramePreemptionReleaseAdvance_Object(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 2),
    _Ieee8021FramePreemptionReleaseAdvance_Type()
)
ieee8021FramePreemptionReleaseAdvance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FramePreemptionReleaseAdvance.setStatus("current")


class _Ieee8021FramePreemptionActive_Type(Integer32):
    """Custom type ieee8021FramePreemptionActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("idle", 1))
    )


_Ieee8021FramePreemptionActive_Type.__name__ = "Integer32"
_Ieee8021FramePreemptionActive_Object = MibTableColumn
ieee8021FramePreemptionActive = _Ieee8021FramePreemptionActive_Object(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 3),
    _Ieee8021FramePreemptionActive_Type()
)
ieee8021FramePreemptionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FramePreemptionActive.setStatus("current")


class _Ieee8021FramePreemptionHoldRequest_Type(Integer32):
    """Custom type ieee8021FramePreemptionHoldRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hold", 1),
          ("release", 2))
    )


_Ieee8021FramePreemptionHoldRequest_Type.__name__ = "Integer32"
_Ieee8021FramePreemptionHoldRequest_Object = MibTableColumn
ieee8021FramePreemptionHoldRequest = _Ieee8021FramePreemptionHoldRequest_Object(
    (1, 3, 111, 2, 802, 1, 1, 29, 1, 1, 2, 1, 4),
    _Ieee8021FramePreemptionHoldRequest_Type()
)
ieee8021FramePreemptionHoldRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021FramePreemptionHoldRequest.setStatus("current")
_Ieee8021PreemptionConformance_ObjectIdentity = ObjectIdentity
ieee8021PreemptionConformance = _Ieee8021PreemptionConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 29, 2)
)
_Ieee8021PreemptionCompliances_ObjectIdentity = ObjectIdentity
ieee8021PreemptionCompliances = _Ieee8021PreemptionCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 29, 2, 1)
)
_Ieee8021PreemptionGroups_ObjectIdentity = ObjectIdentity
ieee8021PreemptionGroups = _Ieee8021PreemptionGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 29, 2, 2)
)

# Managed Objects groups

ieee8021PreemptionGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 29, 2, 2, 1)
)
ieee8021PreemptionGroup.setObjects(
      *(("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionAdminStatus"),
        ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionHoldAdvance"),
        ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionReleaseAdvance"),
        ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionActive"),
        ("IEEE8021-Preemption-MIB", "ieee8021FramePreemptionHoldRequest"))
)
if mibBuilder.loadTexts:
    ieee8021PreemptionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021PreemptionCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 29, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021PreemptionCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-Preemption-MIB",
    **{"ieee8021PreemptionMib": ieee8021PreemptionMib,
       "ieee8021PreemptionNotifications": ieee8021PreemptionNotifications,
       "ieee8021PreemptionObjects": ieee8021PreemptionObjects,
       "ieee8021PreemptionParameters": ieee8021PreemptionParameters,
       "ieee8021PreemptionParameterTable": ieee8021PreemptionParameterTable,
       "ieee8021PreemptionParameterEntry": ieee8021PreemptionParameterEntry,
       "ieee8021PreemptionPriority": ieee8021PreemptionPriority,
       "ieee8021FramePreemptionAdminStatus": ieee8021FramePreemptionAdminStatus,
       "ieee8021PreemptionConfigTable": ieee8021PreemptionConfigTable,
       "ieee8021PreemptionConfigEntry": ieee8021PreemptionConfigEntry,
       "ieee8021FramePreemptionHoldAdvance": ieee8021FramePreemptionHoldAdvance,
       "ieee8021FramePreemptionReleaseAdvance": ieee8021FramePreemptionReleaseAdvance,
       "ieee8021FramePreemptionActive": ieee8021FramePreemptionActive,
       "ieee8021FramePreemptionHoldRequest": ieee8021FramePreemptionHoldRequest,
       "ieee8021PreemptionConformance": ieee8021PreemptionConformance,
       "ieee8021PreemptionCompliances": ieee8021PreemptionCompliances,
       "ieee8021PreemptionCompliance": ieee8021PreemptionCompliance,
       "ieee8021PreemptionGroups": ieee8021PreemptionGroups,
       "ieee8021PreemptionGroup": ieee8021PreemptionGroup}
)
