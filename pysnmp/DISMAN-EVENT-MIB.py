# SNMP MIB module (DISMAN-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DISMAN-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:14 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(SnmpTagValue,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagValue")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dismanEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 88)
)
dismanEventMIB.setRevisions(
        ("2001-11-14 00:00",
         "2000-10-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FailureReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0,
              1,
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
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("authorizationError", 16),
          ("badDestination", -2),
          ("badType", -5),
          ("badValue", 3),
          ("commitFailed", 14),
          ("destinationUnreachable", -3),
          ("genErr", 5),
          ("inconsistentName", 18),
          ("inconsistentValue", 12),
          ("localResourceLack", -1),
          ("noAccess", 6),
          ("noCreation", 11),
          ("noError", 0),
          ("noResponse", -4),
          ("noSuchName", 2),
          ("notWritable", 17),
          ("readOnly", 4),
          ("resourceUnavailable", 13),
          ("sampleOverrun", -6),
          ("tooBig", 1),
          ("undoFailed", 15),
          ("wrongEncoding", 9),
          ("wrongLength", 8),
          ("wrongType", 7),
          ("wrongValue", 10))
    )



# MIB Managed Objects in the order of their OIDs

_SysUpTimeInstance_ObjectIdentity = ObjectIdentity
sysUpTimeInstance = _SysUpTimeInstance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1, 3, 0)
)
_DismanEventMIBObjects_ObjectIdentity = ObjectIdentity
dismanEventMIBObjects = _DismanEventMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 1)
)
_MteResource_ObjectIdentity = ObjectIdentity
mteResource = _MteResource_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 1, 1)
)


class _MteResourceSampleMinimum_Type(Integer32):
    """Custom type mteResourceSampleMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MteResourceSampleMinimum_Type.__name__ = "Integer32"
_MteResourceSampleMinimum_Object = MibScalar
mteResourceSampleMinimum = _MteResourceSampleMinimum_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 1, 1),
    _MteResourceSampleMinimum_Type()
)
mteResourceSampleMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteResourceSampleMinimum.setStatus("current")
if mibBuilder.loadTexts:
    mteResourceSampleMinimum.setUnits("seconds")
_MteResourceSampleInstanceMaximum_Type = Unsigned32
_MteResourceSampleInstanceMaximum_Object = MibScalar
mteResourceSampleInstanceMaximum = _MteResourceSampleInstanceMaximum_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 1, 2),
    _MteResourceSampleInstanceMaximum_Type()
)
mteResourceSampleInstanceMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteResourceSampleInstanceMaximum.setStatus("current")
if mibBuilder.loadTexts:
    mteResourceSampleInstanceMaximum.setUnits("instances")
_MteResourceSampleInstances_Type = Gauge32
_MteResourceSampleInstances_Object = MibScalar
mteResourceSampleInstances = _MteResourceSampleInstances_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 1, 3),
    _MteResourceSampleInstances_Type()
)
mteResourceSampleInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mteResourceSampleInstances.setStatus("current")
if mibBuilder.loadTexts:
    mteResourceSampleInstances.setUnits("instances")
_MteResourceSampleInstancesHigh_Type = Gauge32
_MteResourceSampleInstancesHigh_Object = MibScalar
mteResourceSampleInstancesHigh = _MteResourceSampleInstancesHigh_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 1, 4),
    _MteResourceSampleInstancesHigh_Type()
)
mteResourceSampleInstancesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mteResourceSampleInstancesHigh.setStatus("current")
if mibBuilder.loadTexts:
    mteResourceSampleInstancesHigh.setUnits("instances")
_MteResourceSampleInstanceLacks_Type = Counter32
_MteResourceSampleInstanceLacks_Object = MibScalar
mteResourceSampleInstanceLacks = _MteResourceSampleInstanceLacks_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 1, 5),
    _MteResourceSampleInstanceLacks_Type()
)
mteResourceSampleInstanceLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mteResourceSampleInstanceLacks.setStatus("current")
if mibBuilder.loadTexts:
    mteResourceSampleInstanceLacks.setUnits("instances")
_MteTrigger_ObjectIdentity = ObjectIdentity
mteTrigger = _MteTrigger_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 1, 2)
)
_MteTriggerFailures_Type = Counter32
_MteTriggerFailures_Object = MibScalar
mteTriggerFailures = _MteTriggerFailures_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 1),
    _MteTriggerFailures_Type()
)
mteTriggerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mteTriggerFailures.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerFailures.setUnits("failures")
_MteTriggerTable_Object = MibTable
mteTriggerTable = _MteTriggerTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mteTriggerTable.setStatus("current")
_MteTriggerEntry_Object = MibTableRow
mteTriggerEntry = _MteTriggerEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1)
)
mteTriggerEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteTriggerName"),
)
if mibBuilder.loadTexts:
    mteTriggerEntry.setStatus("current")


class _MteOwner_Type(SnmpAdminString):
    """Custom type mteOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteOwner_Type.__name__ = "SnmpAdminString"
_MteOwner_Object = MibTableColumn
mteOwner = _MteOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 1),
    _MteOwner_Type()
)
mteOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mteOwner.setStatus("current")


class _MteTriggerName_Type(SnmpAdminString):
    """Custom type mteTriggerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MteTriggerName_Type.__name__ = "SnmpAdminString"
_MteTriggerName_Object = MibTableColumn
mteTriggerName = _MteTriggerName_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 2),
    _MteTriggerName_Type()
)
mteTriggerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mteTriggerName.setStatus("current")


class _MteTriggerComment_Type(SnmpAdminString):
    """Custom type mteTriggerComment based on SnmpAdminString"""
    defaultHexValue = ""


_MteTriggerComment_Object = MibTableColumn
mteTriggerComment = _MteTriggerComment_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 3),
    _MteTriggerComment_Type()
)
mteTriggerComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerComment.setStatus("current")


class _MteTriggerTest_Type(Bits):
    """Custom type mteTriggerTest based on Bits"""
    defaultBinValue = "01"

    namedValues = NamedValues(
        *(("boolean", 1),
          ("existence", 0),
          ("threshold", 2))
    )

_MteTriggerTest_Type.__name__ = "Bits"
_MteTriggerTest_Object = MibTableColumn
mteTriggerTest = _MteTriggerTest_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 4),
    _MteTriggerTest_Type()
)
mteTriggerTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerTest.setStatus("current")


class _MteTriggerSampleType_Type(Integer32):
    """Custom type mteTriggerSampleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_MteTriggerSampleType_Type.__name__ = "Integer32"
_MteTriggerSampleType_Object = MibTableColumn
mteTriggerSampleType = _MteTriggerSampleType_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 5),
    _MteTriggerSampleType_Type()
)
mteTriggerSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerSampleType.setStatus("current")


class _MteTriggerValueID_Type(ObjectIdentifier):
    """Custom type mteTriggerValueID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_MteTriggerValueID_Object = MibTableColumn
mteTriggerValueID = _MteTriggerValueID_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 6),
    _MteTriggerValueID_Type()
)
mteTriggerValueID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerValueID.setStatus("current")


class _MteTriggerValueIDWildcard_Type(TruthValue):
    """Custom type mteTriggerValueIDWildcard based on TruthValue"""


_MteTriggerValueIDWildcard_Object = MibTableColumn
mteTriggerValueIDWildcard = _MteTriggerValueIDWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 7),
    _MteTriggerValueIDWildcard_Type()
)
mteTriggerValueIDWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerValueIDWildcard.setStatus("current")


class _MteTriggerTargetTag_Type(SnmpTagValue):
    """Custom type mteTriggerTargetTag based on SnmpTagValue"""
    defaultHexValue = ""


_MteTriggerTargetTag_Object = MibTableColumn
mteTriggerTargetTag = _MteTriggerTargetTag_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 8),
    _MteTriggerTargetTag_Type()
)
mteTriggerTargetTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerTargetTag.setStatus("current")


class _MteTriggerContextName_Type(SnmpAdminString):
    """Custom type mteTriggerContextName based on SnmpAdminString"""
    defaultHexValue = ""


_MteTriggerContextName_Object = MibTableColumn
mteTriggerContextName = _MteTriggerContextName_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 9),
    _MteTriggerContextName_Type()
)
mteTriggerContextName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerContextName.setStatus("current")


class _MteTriggerContextNameWildcard_Type(TruthValue):
    """Custom type mteTriggerContextNameWildcard based on TruthValue"""


_MteTriggerContextNameWildcard_Object = MibTableColumn
mteTriggerContextNameWildcard = _MteTriggerContextNameWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 10),
    _MteTriggerContextNameWildcard_Type()
)
mteTriggerContextNameWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerContextNameWildcard.setStatus("current")


class _MteTriggerFrequency_Type(Unsigned32):
    """Custom type mteTriggerFrequency based on Unsigned32"""
    defaultValue = 600


_MteTriggerFrequency_Object = MibTableColumn
mteTriggerFrequency = _MteTriggerFrequency_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 11),
    _MteTriggerFrequency_Type()
)
mteTriggerFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerFrequency.setStatus("current")
if mibBuilder.loadTexts:
    mteTriggerFrequency.setUnits("seconds")


class _MteTriggerObjectsOwner_Type(SnmpAdminString):
    """Custom type mteTriggerObjectsOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerObjectsOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerObjectsOwner_Object = MibTableColumn
mteTriggerObjectsOwner = _MteTriggerObjectsOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 12),
    _MteTriggerObjectsOwner_Type()
)
mteTriggerObjectsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerObjectsOwner.setStatus("current")


class _MteTriggerObjects_Type(SnmpAdminString):
    """Custom type mteTriggerObjects based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerObjects_Type.__name__ = "SnmpAdminString"
_MteTriggerObjects_Object = MibTableColumn
mteTriggerObjects = _MteTriggerObjects_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 13),
    _MteTriggerObjects_Type()
)
mteTriggerObjects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerObjects.setStatus("current")


class _MteTriggerEnabled_Type(TruthValue):
    """Custom type mteTriggerEnabled based on TruthValue"""


_MteTriggerEnabled_Object = MibTableColumn
mteTriggerEnabled = _MteTriggerEnabled_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 14),
    _MteTriggerEnabled_Type()
)
mteTriggerEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerEnabled.setStatus("current")
_MteTriggerEntryStatus_Type = RowStatus
_MteTriggerEntryStatus_Object = MibTableColumn
mteTriggerEntryStatus = _MteTriggerEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 15),
    _MteTriggerEntryStatus_Type()
)
mteTriggerEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerEntryStatus.setStatus("current")


class _MteTriggerEntryStorageType_Type(StorageType):
    """Custom type mteTriggerEntryStorageType based on StorageType"""


_MteTriggerEntryStorageType_Object = MibTableColumn
mteTriggerEntryStorageType = _MteTriggerEntryStorageType_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 2, 1, 16),
    _MteTriggerEntryStorageType_Type()
)
mteTriggerEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteTriggerEntryStorageType.setStatus("current")
_MteTriggerDeltaTable_Object = MibTable
mteTriggerDeltaTable = _MteTriggerDeltaTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mteTriggerDeltaTable.setStatus("current")
_MteTriggerDeltaEntry_Object = MibTableRow
mteTriggerDeltaEntry = _MteTriggerDeltaEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1)
)
mteTriggerDeltaEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteTriggerName"),
)
if mibBuilder.loadTexts:
    mteTriggerDeltaEntry.setStatus("current")


class _MteTriggerDeltaDiscontinuityID_Type(ObjectIdentifier):
    """Custom type mteTriggerDeltaDiscontinuityID based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 2, 1, 1, 3, 0)


_MteTriggerDeltaDiscontinuityID_Object = MibTableColumn
mteTriggerDeltaDiscontinuityID = _MteTriggerDeltaDiscontinuityID_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 1),
    _MteTriggerDeltaDiscontinuityID_Type()
)
mteTriggerDeltaDiscontinuityID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerDeltaDiscontinuityID.setStatus("current")


class _MteTriggerDeltaDiscontinuityIDWildcard_Type(TruthValue):
    """Custom type mteTriggerDeltaDiscontinuityIDWildcard based on TruthValue"""


_MteTriggerDeltaDiscontinuityIDWildcard_Object = MibTableColumn
mteTriggerDeltaDiscontinuityIDWildcard = _MteTriggerDeltaDiscontinuityIDWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 2),
    _MteTriggerDeltaDiscontinuityIDWildcard_Type()
)
mteTriggerDeltaDiscontinuityIDWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerDeltaDiscontinuityIDWildcard.setStatus("current")


class _MteTriggerDeltaDiscontinuityIDType_Type(Integer32):
    """Custom type mteTriggerDeltaDiscontinuityIDType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dateAndTime", 3),
          ("timeStamp", 2),
          ("timeTicks", 1))
    )


_MteTriggerDeltaDiscontinuityIDType_Type.__name__ = "Integer32"
_MteTriggerDeltaDiscontinuityIDType_Object = MibTableColumn
mteTriggerDeltaDiscontinuityIDType = _MteTriggerDeltaDiscontinuityIDType_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 3, 1, 3),
    _MteTriggerDeltaDiscontinuityIDType_Type()
)
mteTriggerDeltaDiscontinuityIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerDeltaDiscontinuityIDType.setStatus("current")
_MteTriggerExistenceTable_Object = MibTable
mteTriggerExistenceTable = _MteTriggerExistenceTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4)
)
if mibBuilder.loadTexts:
    mteTriggerExistenceTable.setStatus("current")
_MteTriggerExistenceEntry_Object = MibTableRow
mteTriggerExistenceEntry = _MteTriggerExistenceEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1)
)
mteTriggerExistenceEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteTriggerName"),
)
if mibBuilder.loadTexts:
    mteTriggerExistenceEntry.setStatus("current")


class _MteTriggerExistenceTest_Type(Bits):
    """Custom type mteTriggerExistenceTest based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("absent", 1),
          ("changed", 2),
          ("present", 0))
    )

_MteTriggerExistenceTest_Type.__name__ = "Bits"
_MteTriggerExistenceTest_Object = MibTableColumn
mteTriggerExistenceTest = _MteTriggerExistenceTest_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 1),
    _MteTriggerExistenceTest_Type()
)
mteTriggerExistenceTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceTest.setStatus("current")


class _MteTriggerExistenceStartup_Type(Bits):
    """Custom type mteTriggerExistenceStartup based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 0))
    )

_MteTriggerExistenceStartup_Type.__name__ = "Bits"
_MteTriggerExistenceStartup_Object = MibTableColumn
mteTriggerExistenceStartup = _MteTriggerExistenceStartup_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 2),
    _MteTriggerExistenceStartup_Type()
)
mteTriggerExistenceStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceStartup.setStatus("current")


class _MteTriggerExistenceObjectsOwner_Type(SnmpAdminString):
    """Custom type mteTriggerExistenceObjectsOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerExistenceObjectsOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerExistenceObjectsOwner_Object = MibTableColumn
mteTriggerExistenceObjectsOwner = _MteTriggerExistenceObjectsOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 3),
    _MteTriggerExistenceObjectsOwner_Type()
)
mteTriggerExistenceObjectsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceObjectsOwner.setStatus("current")


class _MteTriggerExistenceObjects_Type(SnmpAdminString):
    """Custom type mteTriggerExistenceObjects based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerExistenceObjects_Type.__name__ = "SnmpAdminString"
_MteTriggerExistenceObjects_Object = MibTableColumn
mteTriggerExistenceObjects = _MteTriggerExistenceObjects_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 4),
    _MteTriggerExistenceObjects_Type()
)
mteTriggerExistenceObjects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceObjects.setStatus("current")


class _MteTriggerExistenceEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerExistenceEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerExistenceEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerExistenceEventOwner_Object = MibTableColumn
mteTriggerExistenceEventOwner = _MteTriggerExistenceEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 5),
    _MteTriggerExistenceEventOwner_Type()
)
mteTriggerExistenceEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceEventOwner.setStatus("current")


class _MteTriggerExistenceEvent_Type(SnmpAdminString):
    """Custom type mteTriggerExistenceEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerExistenceEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerExistenceEvent_Object = MibTableColumn
mteTriggerExistenceEvent = _MteTriggerExistenceEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 4, 1, 6),
    _MteTriggerExistenceEvent_Type()
)
mteTriggerExistenceEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerExistenceEvent.setStatus("current")
_MteTriggerBooleanTable_Object = MibTable
mteTriggerBooleanTable = _MteTriggerBooleanTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mteTriggerBooleanTable.setStatus("current")
_MteTriggerBooleanEntry_Object = MibTableRow
mteTriggerBooleanEntry = _MteTriggerBooleanEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1)
)
mteTriggerBooleanEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteTriggerName"),
)
if mibBuilder.loadTexts:
    mteTriggerBooleanEntry.setStatus("current")


class _MteTriggerBooleanComparison_Type(Integer32):
    """Custom type mteTriggerBooleanComparison based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("greater", 5),
          ("greaterOrEqual", 6),
          ("less", 3),
          ("lessOrEqual", 4),
          ("unequal", 1))
    )


_MteTriggerBooleanComparison_Type.__name__ = "Integer32"
_MteTriggerBooleanComparison_Object = MibTableColumn
mteTriggerBooleanComparison = _MteTriggerBooleanComparison_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 1),
    _MteTriggerBooleanComparison_Type()
)
mteTriggerBooleanComparison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanComparison.setStatus("current")


class _MteTriggerBooleanValue_Type(Integer32):
    """Custom type mteTriggerBooleanValue based on Integer32"""
    defaultValue = 0


_MteTriggerBooleanValue_Object = MibTableColumn
mteTriggerBooleanValue = _MteTriggerBooleanValue_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 2),
    _MteTriggerBooleanValue_Type()
)
mteTriggerBooleanValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanValue.setStatus("current")


class _MteTriggerBooleanStartup_Type(TruthValue):
    """Custom type mteTriggerBooleanStartup based on TruthValue"""


_MteTriggerBooleanStartup_Object = MibTableColumn
mteTriggerBooleanStartup = _MteTriggerBooleanStartup_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 3),
    _MteTriggerBooleanStartup_Type()
)
mteTriggerBooleanStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanStartup.setStatus("current")


class _MteTriggerBooleanObjectsOwner_Type(SnmpAdminString):
    """Custom type mteTriggerBooleanObjectsOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerBooleanObjectsOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerBooleanObjectsOwner_Object = MibTableColumn
mteTriggerBooleanObjectsOwner = _MteTriggerBooleanObjectsOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 4),
    _MteTriggerBooleanObjectsOwner_Type()
)
mteTriggerBooleanObjectsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanObjectsOwner.setStatus("current")


class _MteTriggerBooleanObjects_Type(SnmpAdminString):
    """Custom type mteTriggerBooleanObjects based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerBooleanObjects_Type.__name__ = "SnmpAdminString"
_MteTriggerBooleanObjects_Object = MibTableColumn
mteTriggerBooleanObjects = _MteTriggerBooleanObjects_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 5),
    _MteTriggerBooleanObjects_Type()
)
mteTriggerBooleanObjects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanObjects.setStatus("current")


class _MteTriggerBooleanEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerBooleanEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerBooleanEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerBooleanEventOwner_Object = MibTableColumn
mteTriggerBooleanEventOwner = _MteTriggerBooleanEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 6),
    _MteTriggerBooleanEventOwner_Type()
)
mteTriggerBooleanEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanEventOwner.setStatus("current")


class _MteTriggerBooleanEvent_Type(SnmpAdminString):
    """Custom type mteTriggerBooleanEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerBooleanEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerBooleanEvent_Object = MibTableColumn
mteTriggerBooleanEvent = _MteTriggerBooleanEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 5, 1, 7),
    _MteTriggerBooleanEvent_Type()
)
mteTriggerBooleanEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerBooleanEvent.setStatus("current")
_MteTriggerThresholdTable_Object = MibTable
mteTriggerThresholdTable = _MteTriggerThresholdTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mteTriggerThresholdTable.setStatus("current")
_MteTriggerThresholdEntry_Object = MibTableRow
mteTriggerThresholdEntry = _MteTriggerThresholdEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1)
)
mteTriggerThresholdEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteTriggerName"),
)
if mibBuilder.loadTexts:
    mteTriggerThresholdEntry.setStatus("current")


class _MteTriggerThresholdStartup_Type(Integer32):
    """Custom type mteTriggerThresholdStartup based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("falling", 2),
          ("rising", 1),
          ("risingOrFalling", 3))
    )


_MteTriggerThresholdStartup_Type.__name__ = "Integer32"
_MteTriggerThresholdStartup_Object = MibTableColumn
mteTriggerThresholdStartup = _MteTriggerThresholdStartup_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 1),
    _MteTriggerThresholdStartup_Type()
)
mteTriggerThresholdStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdStartup.setStatus("current")


class _MteTriggerThresholdRising_Type(Integer32):
    """Custom type mteTriggerThresholdRising based on Integer32"""
    defaultValue = 0


_MteTriggerThresholdRising_Object = MibTableColumn
mteTriggerThresholdRising = _MteTriggerThresholdRising_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 2),
    _MteTriggerThresholdRising_Type()
)
mteTriggerThresholdRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdRising.setStatus("current")


class _MteTriggerThresholdFalling_Type(Integer32):
    """Custom type mteTriggerThresholdFalling based on Integer32"""
    defaultValue = 0


_MteTriggerThresholdFalling_Object = MibTableColumn
mteTriggerThresholdFalling = _MteTriggerThresholdFalling_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 3),
    _MteTriggerThresholdFalling_Type()
)
mteTriggerThresholdFalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdFalling.setStatus("current")


class _MteTriggerThresholdDeltaRising_Type(Integer32):
    """Custom type mteTriggerThresholdDeltaRising based on Integer32"""
    defaultValue = 0


_MteTriggerThresholdDeltaRising_Object = MibTableColumn
mteTriggerThresholdDeltaRising = _MteTriggerThresholdDeltaRising_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 4),
    _MteTriggerThresholdDeltaRising_Type()
)
mteTriggerThresholdDeltaRising.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaRising.setStatus("current")


class _MteTriggerThresholdDeltaFalling_Type(Integer32):
    """Custom type mteTriggerThresholdDeltaFalling based on Integer32"""
    defaultValue = 0


_MteTriggerThresholdDeltaFalling_Object = MibTableColumn
mteTriggerThresholdDeltaFalling = _MteTriggerThresholdDeltaFalling_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 5),
    _MteTriggerThresholdDeltaFalling_Type()
)
mteTriggerThresholdDeltaFalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaFalling.setStatus("current")


class _MteTriggerThresholdObjectsOwner_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdObjectsOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdObjectsOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdObjectsOwner_Object = MibTableColumn
mteTriggerThresholdObjectsOwner = _MteTriggerThresholdObjectsOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 6),
    _MteTriggerThresholdObjectsOwner_Type()
)
mteTriggerThresholdObjectsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdObjectsOwner.setStatus("current")


class _MteTriggerThresholdObjects_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdObjects based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdObjects_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdObjects_Object = MibTableColumn
mteTriggerThresholdObjects = _MteTriggerThresholdObjects_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 7),
    _MteTriggerThresholdObjects_Type()
)
mteTriggerThresholdObjects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdObjects.setStatus("current")


class _MteTriggerThresholdRisingEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdRisingEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdRisingEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdRisingEventOwner_Object = MibTableColumn
mteTriggerThresholdRisingEventOwner = _MteTriggerThresholdRisingEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 8),
    _MteTriggerThresholdRisingEventOwner_Type()
)
mteTriggerThresholdRisingEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdRisingEventOwner.setStatus("current")


class _MteTriggerThresholdRisingEvent_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdRisingEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdRisingEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdRisingEvent_Object = MibTableColumn
mteTriggerThresholdRisingEvent = _MteTriggerThresholdRisingEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 9),
    _MteTriggerThresholdRisingEvent_Type()
)
mteTriggerThresholdRisingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdRisingEvent.setStatus("current")


class _MteTriggerThresholdFallingEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdFallingEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdFallingEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdFallingEventOwner_Object = MibTableColumn
mteTriggerThresholdFallingEventOwner = _MteTriggerThresholdFallingEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 10),
    _MteTriggerThresholdFallingEventOwner_Type()
)
mteTriggerThresholdFallingEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdFallingEventOwner.setStatus("current")


class _MteTriggerThresholdFallingEvent_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdFallingEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdFallingEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdFallingEvent_Object = MibTableColumn
mteTriggerThresholdFallingEvent = _MteTriggerThresholdFallingEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 11),
    _MteTriggerThresholdFallingEvent_Type()
)
mteTriggerThresholdFallingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdFallingEvent.setStatus("current")


class _MteTriggerThresholdDeltaRisingEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdDeltaRisingEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdDeltaRisingEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdDeltaRisingEventOwner_Object = MibTableColumn
mteTriggerThresholdDeltaRisingEventOwner = _MteTriggerThresholdDeltaRisingEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 12),
    _MteTriggerThresholdDeltaRisingEventOwner_Type()
)
mteTriggerThresholdDeltaRisingEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaRisingEventOwner.setStatus("current")


class _MteTriggerThresholdDeltaRisingEvent_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdDeltaRisingEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdDeltaRisingEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdDeltaRisingEvent_Object = MibTableColumn
mteTriggerThresholdDeltaRisingEvent = _MteTriggerThresholdDeltaRisingEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 13),
    _MteTriggerThresholdDeltaRisingEvent_Type()
)
mteTriggerThresholdDeltaRisingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaRisingEvent.setStatus("current")


class _MteTriggerThresholdDeltaFallingEventOwner_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdDeltaFallingEventOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdDeltaFallingEventOwner_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdDeltaFallingEventOwner_Object = MibTableColumn
mteTriggerThresholdDeltaFallingEventOwner = _MteTriggerThresholdDeltaFallingEventOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 14),
    _MteTriggerThresholdDeltaFallingEventOwner_Type()
)
mteTriggerThresholdDeltaFallingEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaFallingEventOwner.setStatus("current")


class _MteTriggerThresholdDeltaFallingEvent_Type(SnmpAdminString):
    """Custom type mteTriggerThresholdDeltaFallingEvent based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteTriggerThresholdDeltaFallingEvent_Type.__name__ = "SnmpAdminString"
_MteTriggerThresholdDeltaFallingEvent_Object = MibTableColumn
mteTriggerThresholdDeltaFallingEvent = _MteTriggerThresholdDeltaFallingEvent_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 2, 6, 1, 15),
    _MteTriggerThresholdDeltaFallingEvent_Type()
)
mteTriggerThresholdDeltaFallingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteTriggerThresholdDeltaFallingEvent.setStatus("current")
_MteObjects_ObjectIdentity = ObjectIdentity
mteObjects = _MteObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 1, 3)
)
_MteObjectsTable_Object = MibTable
mteObjectsTable = _MteObjectsTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mteObjectsTable.setStatus("current")
_MteObjectsEntry_Object = MibTableRow
mteObjectsEntry = _MteObjectsEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1)
)
mteObjectsEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (0, "DISMAN-EVENT-MIB", "mteObjectsName"),
    (0, "DISMAN-EVENT-MIB", "mteObjectsIndex"),
)
if mibBuilder.loadTexts:
    mteObjectsEntry.setStatus("current")


class _MteObjectsName_Type(SnmpAdminString):
    """Custom type mteObjectsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MteObjectsName_Type.__name__ = "SnmpAdminString"
_MteObjectsName_Object = MibTableColumn
mteObjectsName = _MteObjectsName_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 1),
    _MteObjectsName_Type()
)
mteObjectsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mteObjectsName.setStatus("current")


class _MteObjectsIndex_Type(Unsigned32):
    """Custom type mteObjectsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MteObjectsIndex_Type.__name__ = "Unsigned32"
_MteObjectsIndex_Object = MibTableColumn
mteObjectsIndex = _MteObjectsIndex_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 2),
    _MteObjectsIndex_Type()
)
mteObjectsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mteObjectsIndex.setStatus("current")


class _MteObjectsID_Type(ObjectIdentifier):
    """Custom type mteObjectsID based on ObjectIdentifier"""
    defaultValue = (0, 0)


_MteObjectsID_Object = MibTableColumn
mteObjectsID = _MteObjectsID_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 3),
    _MteObjectsID_Type()
)
mteObjectsID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteObjectsID.setStatus("current")


class _MteObjectsIDWildcard_Type(TruthValue):
    """Custom type mteObjectsIDWildcard based on TruthValue"""


_MteObjectsIDWildcard_Object = MibTableColumn
mteObjectsIDWildcard = _MteObjectsIDWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 4),
    _MteObjectsIDWildcard_Type()
)
mteObjectsIDWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteObjectsIDWildcard.setStatus("current")
_MteObjectsEntryStatus_Type = RowStatus
_MteObjectsEntryStatus_Object = MibTableColumn
mteObjectsEntryStatus = _MteObjectsEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 5),
    _MteObjectsEntryStatus_Type()
)
mteObjectsEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteObjectsEntryStatus.setStatus("current")


class _MteObjectsEntryStorageType_Type(StorageType):
    """Custom type mteObjectsEntryStorageType based on StorageType"""


_MteObjectsEntryStorageType_Object = MibTableColumn
mteObjectsEntryStorageType = _MteObjectsEntryStorageType_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 3, 1, 1, 6),
    _MteObjectsEntryStorageType_Type()
)
mteObjectsEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteObjectsEntryStorageType.setStatus("current")
_MteEvent_ObjectIdentity = ObjectIdentity
mteEvent = _MteEvent_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 1, 4)
)
_MteEventFailures_Type = Counter32
_MteEventFailures_Object = MibScalar
mteEventFailures = _MteEventFailures_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 1),
    _MteEventFailures_Type()
)
mteEventFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mteEventFailures.setStatus("current")
_MteEventTable_Object = MibTable
mteEventTable = _MteEventTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mteEventTable.setStatus("current")
_MteEventEntry_Object = MibTableRow
mteEventEntry = _MteEventEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1)
)
mteEventEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteEventName"),
)
if mibBuilder.loadTexts:
    mteEventEntry.setStatus("current")


class _MteEventName_Type(SnmpAdminString):
    """Custom type mteEventName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MteEventName_Type.__name__ = "SnmpAdminString"
_MteEventName_Object = MibTableColumn
mteEventName = _MteEventName_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 1),
    _MteEventName_Type()
)
mteEventName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mteEventName.setStatus("current")


class _MteEventComment_Type(SnmpAdminString):
    """Custom type mteEventComment based on SnmpAdminString"""
    defaultHexValue = ""


_MteEventComment_Object = MibTableColumn
mteEventComment = _MteEventComment_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 2),
    _MteEventComment_Type()
)
mteEventComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteEventComment.setStatus("current")


class _MteEventActions_Type(Bits):
    """Custom type mteEventActions based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("notification", 0),
          ("set", 1))
    )

_MteEventActions_Type.__name__ = "Bits"
_MteEventActions_Object = MibTableColumn
mteEventActions = _MteEventActions_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 3),
    _MteEventActions_Type()
)
mteEventActions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteEventActions.setStatus("current")


class _MteEventEnabled_Type(TruthValue):
    """Custom type mteEventEnabled based on TruthValue"""


_MteEventEnabled_Object = MibTableColumn
mteEventEnabled = _MteEventEnabled_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 4),
    _MteEventEnabled_Type()
)
mteEventEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteEventEnabled.setStatus("current")
_MteEventEntryStatus_Type = RowStatus
_MteEventEntryStatus_Object = MibTableColumn
mteEventEntryStatus = _MteEventEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 5),
    _MteEventEntryStatus_Type()
)
mteEventEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteEventEntryStatus.setStatus("current")


class _MteEventEntryStorageType_Type(StorageType):
    """Custom type mteEventEntryStorageType based on StorageType"""


_MteEventEntryStorageType_Object = MibTableColumn
mteEventEntryStorageType = _MteEventEntryStorageType_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 2, 1, 6),
    _MteEventEntryStorageType_Type()
)
mteEventEntryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mteEventEntryStorageType.setStatus("current")
_MteEventNotificationTable_Object = MibTable
mteEventNotificationTable = _MteEventNotificationTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 3)
)
if mibBuilder.loadTexts:
    mteEventNotificationTable.setStatus("current")
_MteEventNotificationEntry_Object = MibTableRow
mteEventNotificationEntry = _MteEventNotificationEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1)
)
mteEventNotificationEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteEventName"),
)
if mibBuilder.loadTexts:
    mteEventNotificationEntry.setStatus("current")


class _MteEventNotification_Type(ObjectIdentifier):
    """Custom type mteEventNotification based on ObjectIdentifier"""
    defaultValue = (0, 0)


_MteEventNotification_Object = MibTableColumn
mteEventNotification = _MteEventNotification_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 1),
    _MteEventNotification_Type()
)
mteEventNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventNotification.setStatus("current")


class _MteEventNotificationObjectsOwner_Type(SnmpAdminString):
    """Custom type mteEventNotificationObjectsOwner based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteEventNotificationObjectsOwner_Type.__name__ = "SnmpAdminString"
_MteEventNotificationObjectsOwner_Object = MibTableColumn
mteEventNotificationObjectsOwner = _MteEventNotificationObjectsOwner_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 2),
    _MteEventNotificationObjectsOwner_Type()
)
mteEventNotificationObjectsOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventNotificationObjectsOwner.setStatus("current")


class _MteEventNotificationObjects_Type(SnmpAdminString):
    """Custom type mteEventNotificationObjects based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MteEventNotificationObjects_Type.__name__ = "SnmpAdminString"
_MteEventNotificationObjects_Object = MibTableColumn
mteEventNotificationObjects = _MteEventNotificationObjects_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 3, 1, 3),
    _MteEventNotificationObjects_Type()
)
mteEventNotificationObjects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventNotificationObjects.setStatus("current")
_MteEventSetTable_Object = MibTable
mteEventSetTable = _MteEventSetTable_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4)
)
if mibBuilder.loadTexts:
    mteEventSetTable.setStatus("current")
_MteEventSetEntry_Object = MibTableRow
mteEventSetEntry = _MteEventSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1)
)
mteEventSetEntry.setIndexNames(
    (0, "DISMAN-EVENT-MIB", "mteOwner"),
    (1, "DISMAN-EVENT-MIB", "mteEventName"),
)
if mibBuilder.loadTexts:
    mteEventSetEntry.setStatus("current")


class _MteEventSetObject_Type(ObjectIdentifier):
    """Custom type mteEventSetObject based on ObjectIdentifier"""
    defaultValue = (0, 0)


_MteEventSetObject_Object = MibTableColumn
mteEventSetObject = _MteEventSetObject_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 1),
    _MteEventSetObject_Type()
)
mteEventSetObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetObject.setStatus("current")


class _MteEventSetObjectWildcard_Type(TruthValue):
    """Custom type mteEventSetObjectWildcard based on TruthValue"""


_MteEventSetObjectWildcard_Object = MibTableColumn
mteEventSetObjectWildcard = _MteEventSetObjectWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 2),
    _MteEventSetObjectWildcard_Type()
)
mteEventSetObjectWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetObjectWildcard.setStatus("current")


class _MteEventSetValue_Type(Integer32):
    """Custom type mteEventSetValue based on Integer32"""
    defaultValue = 0


_MteEventSetValue_Object = MibTableColumn
mteEventSetValue = _MteEventSetValue_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 3),
    _MteEventSetValue_Type()
)
mteEventSetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetValue.setStatus("current")


class _MteEventSetTargetTag_Type(SnmpTagValue):
    """Custom type mteEventSetTargetTag based on SnmpTagValue"""
    defaultHexValue = ""


_MteEventSetTargetTag_Object = MibTableColumn
mteEventSetTargetTag = _MteEventSetTargetTag_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 4),
    _MteEventSetTargetTag_Type()
)
mteEventSetTargetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetTargetTag.setStatus("current")


class _MteEventSetContextName_Type(SnmpAdminString):
    """Custom type mteEventSetContextName based on SnmpAdminString"""
    defaultHexValue = ""


_MteEventSetContextName_Object = MibTableColumn
mteEventSetContextName = _MteEventSetContextName_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 5),
    _MteEventSetContextName_Type()
)
mteEventSetContextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetContextName.setStatus("current")


class _MteEventSetContextNameWildcard_Type(TruthValue):
    """Custom type mteEventSetContextNameWildcard based on TruthValue"""


_MteEventSetContextNameWildcard_Object = MibTableColumn
mteEventSetContextNameWildcard = _MteEventSetContextNameWildcard_Object(
    (1, 3, 6, 1, 2, 1, 88, 1, 4, 4, 1, 6),
    _MteEventSetContextNameWildcard_Type()
)
mteEventSetContextNameWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mteEventSetContextNameWildcard.setStatus("current")
_DismanEventMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
dismanEventMIBNotificationPrefix = _DismanEventMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 2)
)
_DismanEventMIBNotifications_ObjectIdentity = ObjectIdentity
dismanEventMIBNotifications = _DismanEventMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 2, 0)
)
_DismanEventMIBNotificationObjects_ObjectIdentity = ObjectIdentity
dismanEventMIBNotificationObjects = _DismanEventMIBNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 2, 1)
)
_MteHotTrigger_Type = SnmpAdminString
_MteHotTrigger_Object = MibScalar
mteHotTrigger = _MteHotTrigger_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 1),
    _MteHotTrigger_Type()
)
mteHotTrigger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteHotTrigger.setStatus("current")
_MteHotTargetName_Type = SnmpAdminString
_MteHotTargetName_Object = MibScalar
mteHotTargetName = _MteHotTargetName_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 2),
    _MteHotTargetName_Type()
)
mteHotTargetName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteHotTargetName.setStatus("current")
_MteHotContextName_Type = SnmpAdminString
_MteHotContextName_Object = MibScalar
mteHotContextName = _MteHotContextName_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 3),
    _MteHotContextName_Type()
)
mteHotContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteHotContextName.setStatus("current")
_MteHotOID_Type = ObjectIdentifier
_MteHotOID_Object = MibScalar
mteHotOID = _MteHotOID_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 4),
    _MteHotOID_Type()
)
mteHotOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteHotOID.setStatus("current")
_MteHotValue_Type = Integer32
_MteHotValue_Object = MibScalar
mteHotValue = _MteHotValue_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 5),
    _MteHotValue_Type()
)
mteHotValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteHotValue.setStatus("current")
_MteFailedReason_Type = FailureReason
_MteFailedReason_Object = MibScalar
mteFailedReason = _MteFailedReason_Object(
    (1, 3, 6, 1, 2, 1, 88, 2, 1, 6),
    _MteFailedReason_Type()
)
mteFailedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mteFailedReason.setStatus("current")
_DismanEventMIBConformance_ObjectIdentity = ObjectIdentity
dismanEventMIBConformance = _DismanEventMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 3)
)
_DismanEventMIBCompliances_ObjectIdentity = ObjectIdentity
dismanEventMIBCompliances = _DismanEventMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 3, 1)
)
_DismanEventMIBGroups_ObjectIdentity = ObjectIdentity
dismanEventMIBGroups = _DismanEventMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 88, 3, 2)
)

# Managed Objects groups

dismanEventResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 1)
)
dismanEventResourceGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteResourceSampleMinimum"),
        ("DISMAN-EVENT-MIB", "mteResourceSampleInstanceMaximum"),
        ("DISMAN-EVENT-MIB", "mteResourceSampleInstances"),
        ("DISMAN-EVENT-MIB", "mteResourceSampleInstancesHigh"),
        ("DISMAN-EVENT-MIB", "mteResourceSampleInstanceLacks"))
)
if mibBuilder.loadTexts:
    dismanEventResourceGroup.setStatus("current")

dismanEventTriggerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 2)
)
dismanEventTriggerGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteTriggerFailures"),
        ("DISMAN-EVENT-MIB", "mteTriggerComment"),
        ("DISMAN-EVENT-MIB", "mteTriggerTest"),
        ("DISMAN-EVENT-MIB", "mteTriggerSampleType"),
        ("DISMAN-EVENT-MIB", "mteTriggerValueID"),
        ("DISMAN-EVENT-MIB", "mteTriggerValueIDWildcard"),
        ("DISMAN-EVENT-MIB", "mteTriggerTargetTag"),
        ("DISMAN-EVENT-MIB", "mteTriggerContextName"),
        ("DISMAN-EVENT-MIB", "mteTriggerContextNameWildcard"),
        ("DISMAN-EVENT-MIB", "mteTriggerFrequency"),
        ("DISMAN-EVENT-MIB", "mteTriggerObjectsOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerObjects"),
        ("DISMAN-EVENT-MIB", "mteTriggerEnabled"),
        ("DISMAN-EVENT-MIB", "mteTriggerEntryStatus"),
        ("DISMAN-EVENT-MIB", "mteTriggerEntryStorageType"),
        ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityID"),
        ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityIDWildcard"),
        ("DISMAN-EVENT-MIB", "mteTriggerDeltaDiscontinuityIDType"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceTest"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceStartup"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceObjectsOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceObjects"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerExistenceEvent"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanComparison"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanValue"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanStartup"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanObjectsOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanObjects"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerBooleanEvent"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdStartup"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdObjectsOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdObjects"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdRising"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdFalling"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRising"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFalling"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdRisingEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdRisingEvent"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdFallingEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdFallingEvent"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRisingEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaRisingEvent"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFallingEventOwner"),
        ("DISMAN-EVENT-MIB", "mteTriggerThresholdDeltaFallingEvent"))
)
if mibBuilder.loadTexts:
    dismanEventTriggerGroup.setStatus("current")

dismanEventObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 3)
)
dismanEventObjectsGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteObjectsID"),
        ("DISMAN-EVENT-MIB", "mteObjectsIDWildcard"),
        ("DISMAN-EVENT-MIB", "mteObjectsEntryStatus"),
        ("DISMAN-EVENT-MIB", "mteObjectsEntryStorageType"))
)
if mibBuilder.loadTexts:
    dismanEventObjectsGroup.setStatus("current")

dismanEventEventGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 4)
)
dismanEventEventGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteEventFailures"),
        ("DISMAN-EVENT-MIB", "mteEventComment"),
        ("DISMAN-EVENT-MIB", "mteEventActions"),
        ("DISMAN-EVENT-MIB", "mteEventEnabled"),
        ("DISMAN-EVENT-MIB", "mteEventEntryStatus"),
        ("DISMAN-EVENT-MIB", "mteEventEntryStorageType"),
        ("DISMAN-EVENT-MIB", "mteEventNotification"),
        ("DISMAN-EVENT-MIB", "mteEventNotificationObjectsOwner"),
        ("DISMAN-EVENT-MIB", "mteEventNotificationObjects"),
        ("DISMAN-EVENT-MIB", "mteEventSetObject"),
        ("DISMAN-EVENT-MIB", "mteEventSetObjectWildcard"),
        ("DISMAN-EVENT-MIB", "mteEventSetValue"),
        ("DISMAN-EVENT-MIB", "mteEventSetTargetTag"),
        ("DISMAN-EVENT-MIB", "mteEventSetContextName"),
        ("DISMAN-EVENT-MIB", "mteEventSetContextNameWildcard"))
)
if mibBuilder.loadTexts:
    dismanEventEventGroup.setStatus("current")

dismanEventNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 5)
)
dismanEventNotificationObjectGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteHotValue"),
        ("DISMAN-EVENT-MIB", "mteFailedReason"))
)
if mibBuilder.loadTexts:
    dismanEventNotificationObjectGroup.setStatus("current")


# Notification objects

mteTriggerFired = NotificationType(
    (1, 3, 6, 1, 2, 1, 88, 2, 0, 1)
)
mteTriggerFired.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteHotValue"))
)
if mibBuilder.loadTexts:
    mteTriggerFired.setStatus(
        "current"
    )

mteTriggerRising = NotificationType(
    (1, 3, 6, 1, 2, 1, 88, 2, 0, 2)
)
mteTriggerRising.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteHotValue"))
)
if mibBuilder.loadTexts:
    mteTriggerRising.setStatus(
        "current"
    )

mteTriggerFalling = NotificationType(
    (1, 3, 6, 1, 2, 1, 88, 2, 0, 3)
)
mteTriggerFalling.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteHotValue"))
)
if mibBuilder.loadTexts:
    mteTriggerFalling.setStatus(
        "current"
    )

mteTriggerFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 88, 2, 0, 4)
)
mteTriggerFailure.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteFailedReason"))
)
if mibBuilder.loadTexts:
    mteTriggerFailure.setStatus(
        "current"
    )

mteEventSetFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 88, 2, 0, 5)
)
mteEventSetFailure.setObjects(
      *(("DISMAN-EVENT-MIB", "mteHotTrigger"),
        ("DISMAN-EVENT-MIB", "mteHotTargetName"),
        ("DISMAN-EVENT-MIB", "mteHotContextName"),
        ("DISMAN-EVENT-MIB", "mteHotOID"),
        ("DISMAN-EVENT-MIB", "mteFailedReason"))
)
if mibBuilder.loadTexts:
    mteEventSetFailure.setStatus(
        "current"
    )


# Notifications groups

dismanEventNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 88, 3, 2, 6)
)
dismanEventNotificationGroup.setObjects(
      *(("DISMAN-EVENT-MIB", "mteTriggerFired"),
        ("DISMAN-EVENT-MIB", "mteTriggerRising"),
        ("DISMAN-EVENT-MIB", "mteTriggerFalling"),
        ("DISMAN-EVENT-MIB", "mteTriggerFailure"),
        ("DISMAN-EVENT-MIB", "mteEventSetFailure"))
)
if mibBuilder.loadTexts:
    dismanEventNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dismanEventMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 88, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dismanEventMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DISMAN-EVENT-MIB",
    **{"FailureReason": FailureReason,
       "sysUpTimeInstance": sysUpTimeInstance,
       "dismanEventMIB": dismanEventMIB,
       "dismanEventMIBObjects": dismanEventMIBObjects,
       "mteResource": mteResource,
       "mteResourceSampleMinimum": mteResourceSampleMinimum,
       "mteResourceSampleInstanceMaximum": mteResourceSampleInstanceMaximum,
       "mteResourceSampleInstances": mteResourceSampleInstances,
       "mteResourceSampleInstancesHigh": mteResourceSampleInstancesHigh,
       "mteResourceSampleInstanceLacks": mteResourceSampleInstanceLacks,
       "mteTrigger": mteTrigger,
       "mteTriggerFailures": mteTriggerFailures,
       "mteTriggerTable": mteTriggerTable,
       "mteTriggerEntry": mteTriggerEntry,
       "mteOwner": mteOwner,
       "mteTriggerName": mteTriggerName,
       "mteTriggerComment": mteTriggerComment,
       "mteTriggerTest": mteTriggerTest,
       "mteTriggerSampleType": mteTriggerSampleType,
       "mteTriggerValueID": mteTriggerValueID,
       "mteTriggerValueIDWildcard": mteTriggerValueIDWildcard,
       "mteTriggerTargetTag": mteTriggerTargetTag,
       "mteTriggerContextName": mteTriggerContextName,
       "mteTriggerContextNameWildcard": mteTriggerContextNameWildcard,
       "mteTriggerFrequency": mteTriggerFrequency,
       "mteTriggerObjectsOwner": mteTriggerObjectsOwner,
       "mteTriggerObjects": mteTriggerObjects,
       "mteTriggerEnabled": mteTriggerEnabled,
       "mteTriggerEntryStatus": mteTriggerEntryStatus,
       "mteTriggerEntryStorageType": mteTriggerEntryStorageType,
       "mteTriggerDeltaTable": mteTriggerDeltaTable,
       "mteTriggerDeltaEntry": mteTriggerDeltaEntry,
       "mteTriggerDeltaDiscontinuityID": mteTriggerDeltaDiscontinuityID,
       "mteTriggerDeltaDiscontinuityIDWildcard": mteTriggerDeltaDiscontinuityIDWildcard,
       "mteTriggerDeltaDiscontinuityIDType": mteTriggerDeltaDiscontinuityIDType,
       "mteTriggerExistenceTable": mteTriggerExistenceTable,
       "mteTriggerExistenceEntry": mteTriggerExistenceEntry,
       "mteTriggerExistenceTest": mteTriggerExistenceTest,
       "mteTriggerExistenceStartup": mteTriggerExistenceStartup,
       "mteTriggerExistenceObjectsOwner": mteTriggerExistenceObjectsOwner,
       "mteTriggerExistenceObjects": mteTriggerExistenceObjects,
       "mteTriggerExistenceEventOwner": mteTriggerExistenceEventOwner,
       "mteTriggerExistenceEvent": mteTriggerExistenceEvent,
       "mteTriggerBooleanTable": mteTriggerBooleanTable,
       "mteTriggerBooleanEntry": mteTriggerBooleanEntry,
       "mteTriggerBooleanComparison": mteTriggerBooleanComparison,
       "mteTriggerBooleanValue": mteTriggerBooleanValue,
       "mteTriggerBooleanStartup": mteTriggerBooleanStartup,
       "mteTriggerBooleanObjectsOwner": mteTriggerBooleanObjectsOwner,
       "mteTriggerBooleanObjects": mteTriggerBooleanObjects,
       "mteTriggerBooleanEventOwner": mteTriggerBooleanEventOwner,
       "mteTriggerBooleanEvent": mteTriggerBooleanEvent,
       "mteTriggerThresholdTable": mteTriggerThresholdTable,
       "mteTriggerThresholdEntry": mteTriggerThresholdEntry,
       "mteTriggerThresholdStartup": mteTriggerThresholdStartup,
       "mteTriggerThresholdRising": mteTriggerThresholdRising,
       "mteTriggerThresholdFalling": mteTriggerThresholdFalling,
       "mteTriggerThresholdDeltaRising": mteTriggerThresholdDeltaRising,
       "mteTriggerThresholdDeltaFalling": mteTriggerThresholdDeltaFalling,
       "mteTriggerThresholdObjectsOwner": mteTriggerThresholdObjectsOwner,
       "mteTriggerThresholdObjects": mteTriggerThresholdObjects,
       "mteTriggerThresholdRisingEventOwner": mteTriggerThresholdRisingEventOwner,
       "mteTriggerThresholdRisingEvent": mteTriggerThresholdRisingEvent,
       "mteTriggerThresholdFallingEventOwner": mteTriggerThresholdFallingEventOwner,
       "mteTriggerThresholdFallingEvent": mteTriggerThresholdFallingEvent,
       "mteTriggerThresholdDeltaRisingEventOwner": mteTriggerThresholdDeltaRisingEventOwner,
       "mteTriggerThresholdDeltaRisingEvent": mteTriggerThresholdDeltaRisingEvent,
       "mteTriggerThresholdDeltaFallingEventOwner": mteTriggerThresholdDeltaFallingEventOwner,
       "mteTriggerThresholdDeltaFallingEvent": mteTriggerThresholdDeltaFallingEvent,
       "mteObjects": mteObjects,
       "mteObjectsTable": mteObjectsTable,
       "mteObjectsEntry": mteObjectsEntry,
       "mteObjectsName": mteObjectsName,
       "mteObjectsIndex": mteObjectsIndex,
       "mteObjectsID": mteObjectsID,
       "mteObjectsIDWildcard": mteObjectsIDWildcard,
       "mteObjectsEntryStatus": mteObjectsEntryStatus,
       "mteObjectsEntryStorageType": mteObjectsEntryStorageType,
       "mteEvent": mteEvent,
       "mteEventFailures": mteEventFailures,
       "mteEventTable": mteEventTable,
       "mteEventEntry": mteEventEntry,
       "mteEventName": mteEventName,
       "mteEventComment": mteEventComment,
       "mteEventActions": mteEventActions,
       "mteEventEnabled": mteEventEnabled,
       "mteEventEntryStatus": mteEventEntryStatus,
       "mteEventEntryStorageType": mteEventEntryStorageType,
       "mteEventNotificationTable": mteEventNotificationTable,
       "mteEventNotificationEntry": mteEventNotificationEntry,
       "mteEventNotification": mteEventNotification,
       "mteEventNotificationObjectsOwner": mteEventNotificationObjectsOwner,
       "mteEventNotificationObjects": mteEventNotificationObjects,
       "mteEventSetTable": mteEventSetTable,
       "mteEventSetEntry": mteEventSetEntry,
       "mteEventSetObject": mteEventSetObject,
       "mteEventSetObjectWildcard": mteEventSetObjectWildcard,
       "mteEventSetValue": mteEventSetValue,
       "mteEventSetTargetTag": mteEventSetTargetTag,
       "mteEventSetContextName": mteEventSetContextName,
       "mteEventSetContextNameWildcard": mteEventSetContextNameWildcard,
       "dismanEventMIBNotificationPrefix": dismanEventMIBNotificationPrefix,
       "dismanEventMIBNotifications": dismanEventMIBNotifications,
       "mteTriggerFired": mteTriggerFired,
       "mteTriggerRising": mteTriggerRising,
       "mteTriggerFalling": mteTriggerFalling,
       "mteTriggerFailure": mteTriggerFailure,
       "mteEventSetFailure": mteEventSetFailure,
       "dismanEventMIBNotificationObjects": dismanEventMIBNotificationObjects,
       "mteHotTrigger": mteHotTrigger,
       "mteHotTargetName": mteHotTargetName,
       "mteHotContextName": mteHotContextName,
       "mteHotOID": mteHotOID,
       "mteHotValue": mteHotValue,
       "mteFailedReason": mteFailedReason,
       "dismanEventMIBConformance": dismanEventMIBConformance,
       "dismanEventMIBCompliances": dismanEventMIBCompliances,
       "dismanEventMIBCompliance": dismanEventMIBCompliance,
       "dismanEventMIBGroups": dismanEventMIBGroups,
       "dismanEventResourceGroup": dismanEventResourceGroup,
       "dismanEventTriggerGroup": dismanEventTriggerGroup,
       "dismanEventObjectsGroup": dismanEventObjectsGroup,
       "dismanEventEventGroup": dismanEventEventGroup,
       "dismanEventNotificationObjectGroup": dismanEventNotificationObjectGroup,
       "dismanEventNotificationGroup": dismanEventNotificationGroup}
)
