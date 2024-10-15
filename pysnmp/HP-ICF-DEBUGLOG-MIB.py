# SNMP MIB module (HP-ICF-DEBUGLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DEBUGLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:14 2024
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

(hpicfDebugLog,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfDebugLog")

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

hpicfDebugLogMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1)
)
hpicfDebugLogMib.setRevisions(
        ("2017-07-04 00:00",
         "2016-03-18 00:00",
         "2016-02-17 00:00",
         "2009-09-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfDebugDestType(Integer32, TextualConvention):
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
        *(("buffer", 2),
          ("none", 0),
          ("syslog", 1))
    )



class HpicfDebugLogLevels(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("debug", 5),
          ("debug2", 6),
          ("debug3", 7),
          ("error", 2),
          ("fatal", 1),
          ("info", 3),
          ("quiet", 0),
          ("verbose", 4))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfDebugLogObjects_ObjectIdentity = ObjectIdentity
hpicfDebugLogObjects = _HpicfDebugLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1)
)
_HpicfDebugLogControlTable_Object = MibTable
hpicfDebugLogControlTable = _HpicfDebugLogControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDebugLogControlTable.setStatus("current")
_HpicfDebugLogControlEntry_Object = MibTableRow
hpicfDebugLogControlEntry = _HpicfDebugLogControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1)
)
hpicfDebugLogControlEntry.setIndexNames(
    (0, "HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogIndex"),
)
if mibBuilder.loadTexts:
    hpicfDebugLogControlEntry.setStatus("current")


class _HpicfDebugLogIndex_Type(Integer32):
    """Custom type hpicfDebugLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfDebugLogIndex_Type.__name__ = "Integer32"
_HpicfDebugLogIndex_Object = MibTableColumn
hpicfDebugLogIndex = _HpicfDebugLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 1),
    _HpicfDebugLogIndex_Type()
)
hpicfDebugLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDebugLogIndex.setStatus("current")


class _HpicfDebugLogDescr_Type(DisplayString):
    """Custom type hpicfDebugLogDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDebugLogDescr_Type.__name__ = "DisplayString"
_HpicfDebugLogDescr_Object = MibTableColumn
hpicfDebugLogDescr = _HpicfDebugLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 2),
    _HpicfDebugLogDescr_Type()
)
hpicfDebugLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDebugLogDescr.setStatus("current")


class _HpicfDebugLogContainedIn_Type(Integer32):
    """Custom type hpicfDebugLogContainedIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfDebugLogContainedIn_Type.__name__ = "Integer32"
_HpicfDebugLogContainedIn_Object = MibTableColumn
hpicfDebugLogContainedIn = _HpicfDebugLogContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 3),
    _HpicfDebugLogContainedIn_Type()
)
hpicfDebugLogContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDebugLogContainedIn.setStatus("current")
_HpicfDebugLogStatus_Type = TruthValue
_HpicfDebugLogStatus_Object = MibTableColumn
hpicfDebugLogStatus = _HpicfDebugLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 4),
    _HpicfDebugLogStatus_Type()
)
hpicfDebugLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDebugLogStatus.setStatus("current")
_HpicfDebugLogPersistent_Type = TruthValue
_HpicfDebugLogPersistent_Object = MibTableColumn
hpicfDebugLogPersistent = _HpicfDebugLogPersistent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 5),
    _HpicfDebugLogPersistent_Type()
)
hpicfDebugLogPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDebugLogPersistent.setStatus("current")


class _HpicfDebugLogLevel_Type(HpicfDebugLogLevels):
    """Custom type hpicfDebugLogLevel based on HpicfDebugLogLevels"""


_HpicfDebugLogLevel_Object = MibScalar
hpicfDebugLogLevel = _HpicfDebugLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 2),
    _HpicfDebugLogLevel_Type()
)
hpicfDebugLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDebugLogLevel.setStatus("current")
_HpicfDebugDestControlTable_Object = MibTable
hpicfDebugDestControlTable = _HpicfDebugDestControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfDebugDestControlTable.setStatus("current")
_HpicfDebugDestControlEntry_Object = MibTableRow
hpicfDebugDestControlEntry = _HpicfDebugDestControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1)
)
hpicfDebugDestControlEntry.setIndexNames(
    (0, "HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestIndex"),
)
if mibBuilder.loadTexts:
    hpicfDebugDestControlEntry.setStatus("current")
_HpicfDebugDestIndex_Type = HpicfDebugDestType
_HpicfDebugDestIndex_Object = MibTableColumn
hpicfDebugDestIndex = _HpicfDebugDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 1),
    _HpicfDebugDestIndex_Type()
)
hpicfDebugDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDebugDestIndex.setStatus("current")
_HpicfDebugDestStatus_Type = TruthValue
_HpicfDebugDestStatus_Object = MibTableColumn
hpicfDebugDestStatus = _HpicfDebugDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 2),
    _HpicfDebugDestStatus_Type()
)
hpicfDebugDestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDebugDestStatus.setStatus("current")
_HpicfDebugDestPersistent_Type = TruthValue
_HpicfDebugDestPersistent_Object = MibTableColumn
hpicfDebugDestPersistent = _HpicfDebugDestPersistent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 3),
    _HpicfDebugDestPersistent_Type()
)
hpicfDebugDestPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDebugDestPersistent.setStatus("current")


class _HpicfDebugTimeStamp_Type(TruthValue):
    """Custom type hpicfDebugTimeStamp based on TruthValue"""


_HpicfDebugTimeStamp_Object = MibScalar
hpicfDebugTimeStamp = _HpicfDebugTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 4),
    _HpicfDebugTimeStamp_Type()
)
hpicfDebugTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDebugTimeStamp.setStatus("current")
_HpicfDebugLogConformance_ObjectIdentity = ObjectIdentity
hpicfDebugLogConformance = _HpicfDebugLogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2)
)
_HpicfDebugLogCompliances_ObjectIdentity = ObjectIdentity
hpicfDebugLogCompliances = _HpicfDebugLogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1)
)
_HpicfDebugLogGroups_ObjectIdentity = ObjectIdentity
hpicfDebugLogGroups = _HpicfDebugLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 2)
)
_HpicfDebugDestGroups_ObjectIdentity = ObjectIdentity
hpicfDebugDestGroups = _HpicfDebugDestGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 3)
)
_HpicfDebugTimeStampGroups_ObjectIdentity = ObjectIdentity
hpicfDebugTimeStampGroups = _HpicfDebugTimeStampGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 4)
)

# Managed Objects groups

hpicfDebugLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 2, 1)
)
hpicfDebugLogGroup.setObjects(
      *(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogDescr"),
        ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogContainedIn"),
        ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogStatus"),
        ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogLevel"),
        ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogPersistent"))
)
if mibBuilder.loadTexts:
    hpicfDebugLogGroup.setStatus("current")

hpicfDebugDestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 3, 1)
)
hpicfDebugDestGroup.setObjects(
      *(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestStatus"),
        ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestPersistent"))
)
if mibBuilder.loadTexts:
    hpicfDebugDestGroup.setStatus("current")

hpicfDebugTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 4, 1)
)
hpicfDebugTimeStampGroup.setObjects(
    ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugTimeStamp")
)
if mibBuilder.loadTexts:
    hpicfDebugTimeStampGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDebugLogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDebugLogCompliance.setStatus(
        "deprecated"
    )

hpicfDebugLogCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfDebugLogCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DEBUGLOG-MIB",
    **{"HpicfDebugDestType": HpicfDebugDestType,
       "HpicfDebugLogLevels": HpicfDebugLogLevels,
       "hpicfDebugLogMib": hpicfDebugLogMib,
       "hpicfDebugLogObjects": hpicfDebugLogObjects,
       "hpicfDebugLogControlTable": hpicfDebugLogControlTable,
       "hpicfDebugLogControlEntry": hpicfDebugLogControlEntry,
       "hpicfDebugLogIndex": hpicfDebugLogIndex,
       "hpicfDebugLogDescr": hpicfDebugLogDescr,
       "hpicfDebugLogContainedIn": hpicfDebugLogContainedIn,
       "hpicfDebugLogStatus": hpicfDebugLogStatus,
       "hpicfDebugLogPersistent": hpicfDebugLogPersistent,
       "hpicfDebugLogLevel": hpicfDebugLogLevel,
       "hpicfDebugDestControlTable": hpicfDebugDestControlTable,
       "hpicfDebugDestControlEntry": hpicfDebugDestControlEntry,
       "hpicfDebugDestIndex": hpicfDebugDestIndex,
       "hpicfDebugDestStatus": hpicfDebugDestStatus,
       "hpicfDebugDestPersistent": hpicfDebugDestPersistent,
       "hpicfDebugTimeStamp": hpicfDebugTimeStamp,
       "hpicfDebugLogConformance": hpicfDebugLogConformance,
       "hpicfDebugLogCompliances": hpicfDebugLogCompliances,
       "hpicfDebugLogCompliance": hpicfDebugLogCompliance,
       "hpicfDebugLogCompliance1": hpicfDebugLogCompliance1,
       "hpicfDebugLogGroups": hpicfDebugLogGroups,
       "hpicfDebugLogGroup": hpicfDebugLogGroup,
       "hpicfDebugDestGroups": hpicfDebugDestGroups,
       "hpicfDebugDestGroup": hpicfDebugDestGroup,
       "hpicfDebugTimeStampGroups": hpicfDebugTimeStampGroups,
       "hpicfDebugTimeStampGroup": hpicfDebugTimeStampGroup}
)
