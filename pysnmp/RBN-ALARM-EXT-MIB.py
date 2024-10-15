# SNMP MIB module (RBN-ALARM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-ALARM-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:51 2024
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

(alarmClearDateAndTime,
 alarmClearIndex,
 alarmListName,
 alarmModelEntry) = mibBuilder.importSymbols(
    "ALARM-MIB",
    "alarmClearDateAndTime",
    "alarmClearIndex",
    "alarmListName",
    "alarmModelEntry")

(rbnModules,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnModules")

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

rbnAlarmExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53)
)
rbnAlarmExtMib.setRevisions(
        ("2009-09-18 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnAlarmObjects_ObjectIdentity = ObjectIdentity
rbnAlarmObjects = _RbnAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1)
)
_RbnAlarmModel_ObjectIdentity = ObjectIdentity
rbnAlarmModel = _RbnAlarmModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 1)
)
_RbnAlarmModelTable_Object = MibTable
rbnAlarmModelTable = _RbnAlarmModelTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAlarmModelTable.setStatus("current")
_RbnAlarmModelEntry_Object = MibTableRow
rbnAlarmModelEntry = _RbnAlarmModelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAlarmModelEntry.setStatus("current")


class _RbnAlarmModelResourceIdx_Type(Unsigned32):
    """Custom type rbnAlarmModelResourceIdx based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 512),
    )


_RbnAlarmModelResourceIdx_Type.__name__ = "Unsigned32"
_RbnAlarmModelResourceIdx_Object = MibTableColumn
rbnAlarmModelResourceIdx = _RbnAlarmModelResourceIdx_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 1, 1, 1, 1),
    _RbnAlarmModelResourceIdx_Type()
)
rbnAlarmModelResourceIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnAlarmModelResourceIdx.setStatus("current")
_RbnAlarmActive_ObjectIdentity = ObjectIdentity
rbnAlarmActive = _RbnAlarmActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 2)
)
_RbnAlarmClear_ObjectIdentity = ObjectIdentity
rbnAlarmClear = _RbnAlarmClear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3)
)
_RbnAlarmClearResourceTable_Object = MibTable
rbnAlarmClearResourceTable = _RbnAlarmClearResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rbnAlarmClearResourceTable.setStatus("current")
_RbnAlarmClearResourceEntry_Object = MibTableRow
rbnAlarmClearResourceEntry = _RbnAlarmClearResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1)
)
rbnAlarmClearResourceEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmClearDateAndTime"),
    (0, "ALARM-MIB", "alarmClearIndex"),
)
if mibBuilder.loadTexts:
    rbnAlarmClearResourceEntry.setStatus("current")
_RbnAlarmClearResourceID_Type = ObjectIdentifier
_RbnAlarmClearResourceID_Object = MibTableColumn
rbnAlarmClearResourceID = _RbnAlarmClearResourceID_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 1),
    _RbnAlarmClearResourceID_Type()
)
rbnAlarmClearResourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAlarmClearResourceID.setStatus("current")


class _RbnAlarmClearResourceValueType_Type(Integer32):
    """Custom type rbnAlarmClearResourceValueType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("counter32", 1),
          ("counter64", 8),
          ("integer32", 4),
          ("ipAddress", 5),
          ("objectId", 7),
          ("octetString", 6),
          ("timeTicks", 3),
          ("unsigned32", 2))
    )


_RbnAlarmClearResourceValueType_Type.__name__ = "Integer32"
_RbnAlarmClearResourceValueType_Object = MibTableColumn
rbnAlarmClearResourceValueType = _RbnAlarmClearResourceValueType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 3),
    _RbnAlarmClearResourceValueType_Type()
)
rbnAlarmClearResourceValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAlarmClearResourceValueType.setStatus("current")
_RbnAlarmClearResourceCounter32Val_Type = Counter32
_RbnAlarmClearResourceCounter32Val_Object = MibTableColumn
rbnAlarmClearResourceCounter32Val = _RbnAlarmClearResourceCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 4),
    _RbnAlarmClearResourceCounter32Val_Type()
)
rbnAlarmClearResourceCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAlarmClearResourceCounter32Val.setStatus("current")
_RbnAlarmClearResourceUnsigned32Val_Type = Unsigned32
_RbnAlarmClearResourceUnsigned32Val_Object = MibTableColumn
rbnAlarmClearResourceUnsigned32Val = _RbnAlarmClearResourceUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 5),
    _RbnAlarmClearResourceUnsigned32Val_Type()
)
rbnAlarmClearResourceUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAlarmClearResourceUnsigned32Val.setStatus("current")
_RbnAlarmClearResourceTimeTicksVal_Type = TimeTicks
_RbnAlarmClearResourceTimeTicksVal_Object = MibTableColumn
rbnAlarmClearResourceTimeTicksVal = _RbnAlarmClearResourceTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 6),
    _RbnAlarmClearResourceTimeTicksVal_Type()
)
rbnAlarmClearResourceTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAlarmClearResourceTimeTicksVal.setStatus("current")
_RbnAlarmClearResourceInteger32Val_Type = Integer32
_RbnAlarmClearResourceInteger32Val_Object = MibTableColumn
rbnAlarmClearResourceInteger32Val = _RbnAlarmClearResourceInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 7),
    _RbnAlarmClearResourceInteger32Val_Type()
)
rbnAlarmClearResourceInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAlarmClearResourceInteger32Val.setStatus("current")


class _RbnAlarmClearResourceOctetStringVal_Type(OctetString):
    """Custom type rbnAlarmClearResourceOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_RbnAlarmClearResourceOctetStringVal_Type.__name__ = "OctetString"
_RbnAlarmClearResourceOctetStringVal_Object = MibTableColumn
rbnAlarmClearResourceOctetStringVal = _RbnAlarmClearResourceOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 8),
    _RbnAlarmClearResourceOctetStringVal_Type()
)
rbnAlarmClearResourceOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAlarmClearResourceOctetStringVal.setStatus("current")
_RbnAlarmClearResourceIpAddressVal_Type = IpAddress
_RbnAlarmClearResourceIpAddressVal_Object = MibTableColumn
rbnAlarmClearResourceIpAddressVal = _RbnAlarmClearResourceIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 9),
    _RbnAlarmClearResourceIpAddressVal_Type()
)
rbnAlarmClearResourceIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAlarmClearResourceIpAddressVal.setStatus("current")
_RbnAlarmClearResourceOidVal_Type = ObjectIdentifier
_RbnAlarmClearResourceOidVal_Object = MibTableColumn
rbnAlarmClearResourceOidVal = _RbnAlarmClearResourceOidVal_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 10),
    _RbnAlarmClearResourceOidVal_Type()
)
rbnAlarmClearResourceOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAlarmClearResourceOidVal.setStatus("current")
_RbnAlarmClearResourceCounter64Val_Type = Counter64
_RbnAlarmClearResourceCounter64Val_Object = MibTableColumn
rbnAlarmClearResourceCounter64Val = _RbnAlarmClearResourceCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 1, 3, 1, 1, 11),
    _RbnAlarmClearResourceCounter64Val_Type()
)
rbnAlarmClearResourceCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAlarmClearResourceCounter64Val.setStatus("current")
_RbnAlarmExtConformance_ObjectIdentity = ObjectIdentity
rbnAlarmExtConformance = _RbnAlarmExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 2)
)
_RbnAlarmExtCompliances_ObjectIdentity = ObjectIdentity
rbnAlarmExtCompliances = _RbnAlarmExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 2, 1)
)
_RbnAlarmExtGroups_ObjectIdentity = ObjectIdentity
rbnAlarmExtGroups = _RbnAlarmExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 2, 2)
)
alarmModelEntry.registerAugmentions(
    ("RBN-ALARM-EXT-MIB",
     "rbnAlarmModelEntry")
)
rbnAlarmModelEntry.setIndexNames(*alarmModelEntry.getIndexNames())

# Managed Objects groups

rbnAlarmModelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 2, 2, 1)
)
rbnAlarmModelGroup.setObjects(
    ("RBN-ALARM-EXT-MIB", "rbnAlarmModelResourceIdx")
)
if mibBuilder.loadTexts:
    rbnAlarmModelGroup.setStatus("current")

rbnAlarmClearGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 2, 2, 2)
)
rbnAlarmClearGroup.setObjects(
      *(("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceID"),
        ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceValueType"),
        ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceCounter32Val"),
        ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceUnsigned32Val"),
        ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceTimeTicksVal"),
        ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceInteger32Val"),
        ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceOctetStringVal"),
        ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceIpAddressVal"),
        ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceOidVal"),
        ("RBN-ALARM-EXT-MIB", "rbnAlarmClearResourceCounter64Val"))
)
if mibBuilder.loadTexts:
    rbnAlarmClearGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnAlarmExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 5, 53, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAlarmExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-ALARM-EXT-MIB",
    **{"rbnAlarmExtMib": rbnAlarmExtMib,
       "rbnAlarmObjects": rbnAlarmObjects,
       "rbnAlarmModel": rbnAlarmModel,
       "rbnAlarmModelTable": rbnAlarmModelTable,
       "rbnAlarmModelEntry": rbnAlarmModelEntry,
       "rbnAlarmModelResourceIdx": rbnAlarmModelResourceIdx,
       "rbnAlarmActive": rbnAlarmActive,
       "rbnAlarmClear": rbnAlarmClear,
       "rbnAlarmClearResourceTable": rbnAlarmClearResourceTable,
       "rbnAlarmClearResourceEntry": rbnAlarmClearResourceEntry,
       "rbnAlarmClearResourceID": rbnAlarmClearResourceID,
       "rbnAlarmClearResourceValueType": rbnAlarmClearResourceValueType,
       "rbnAlarmClearResourceCounter32Val": rbnAlarmClearResourceCounter32Val,
       "rbnAlarmClearResourceUnsigned32Val": rbnAlarmClearResourceUnsigned32Val,
       "rbnAlarmClearResourceTimeTicksVal": rbnAlarmClearResourceTimeTicksVal,
       "rbnAlarmClearResourceInteger32Val": rbnAlarmClearResourceInteger32Val,
       "rbnAlarmClearResourceOctetStringVal": rbnAlarmClearResourceOctetStringVal,
       "rbnAlarmClearResourceIpAddressVal": rbnAlarmClearResourceIpAddressVal,
       "rbnAlarmClearResourceOidVal": rbnAlarmClearResourceOidVal,
       "rbnAlarmClearResourceCounter64Val": rbnAlarmClearResourceCounter64Val,
       "rbnAlarmExtConformance": rbnAlarmExtConformance,
       "rbnAlarmExtCompliances": rbnAlarmExtCompliances,
       "rbnAlarmExtCompliance": rbnAlarmExtCompliance,
       "rbnAlarmExtGroups": rbnAlarmExtGroups,
       "rbnAlarmModelGroup": rbnAlarmModelGroup,
       "rbnAlarmClearGroup": rbnAlarmClearGroup}
)
