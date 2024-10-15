# SNMP MIB module (EQLTAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLTAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:13 2024
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

(UTFString,
 eqlGroupId,
 eqlStorageGroupAdminAccountIndex) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "UTFString",
    "eqlGroupId",
    "eqlStorageGroupAdminAccountIndex")

(eqliscsiLocalMemberId,
 eqliscsiVolumeIndex) = mibBuilder.importSymbols(
    "EQLVOLUME-MIB",
    "eqliscsiLocalMemberId",
    "eqliscsiVolumeIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

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
    "enterprises",
    "iso")

(DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eqltagModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 23)
)
eqltagModule.setRevisions(
        ("2011-10-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqltagObjects_ObjectIdentity = ObjectIdentity
eqltagObjects = _EqltagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1)
)
_EqlTagTable_Object = MibTable
eqlTagTable = _EqlTagTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 1)
)
if mibBuilder.loadTexts:
    eqlTagTable.setStatus("current")
_EqlTagEntry_Object = MibTableRow
eqlTagEntry = _EqlTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1)
)
eqlTagEntry.setIndexNames(
    (0, "EQLTAG-MIB", "eqlTagType"),
    (0, "EQLTAG-MIB", "eqlTagIndex"),
)
if mibBuilder.loadTexts:
    eqlTagEntry.setStatus("current")


class _EqlTagType_Type(Integer32):
    """Custom type eqlTagType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("folder", 1)
    )


_EqlTagType_Type.__name__ = "Integer32"
_EqlTagType_Object = MibTableColumn
eqlTagType = _EqlTagType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 1),
    _EqlTagType_Type()
)
eqlTagType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlTagType.setStatus("current")
_EqlTagIndex_Type = Unsigned32
_EqlTagIndex_Object = MibTableColumn
eqlTagIndex = _EqlTagIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 2),
    _EqlTagIndex_Type()
)
eqlTagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlTagIndex.setStatus("current")
_EqlTagRowStatus_Type = RowStatus
_EqlTagRowStatus_Object = MibTableColumn
eqlTagRowStatus = _EqlTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 3),
    _EqlTagRowStatus_Type()
)
eqlTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTagRowStatus.setStatus("current")


class _EqlTagValue_Type(UTFString):
    """Custom type eqlTagValue based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlTagValue_Type.__name__ = "UTFString"
_EqlTagValue_Object = MibTableColumn
eqlTagValue = _EqlTagValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 4),
    _EqlTagValue_Type()
)
eqlTagValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlTagValue.setStatus("current")


class _EqlTagAdminAccountKey_Type(Unsigned32):
    """Custom type eqlTagAdminAccountKey based on Unsigned32"""
    defaultValue = 0


_EqlTagAdminAccountKey_Object = MibTableColumn
eqlTagAdminAccountKey = _EqlTagAdminAccountKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 5),
    _EqlTagAdminAccountKey_Type()
)
eqlTagAdminAccountKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlTagAdminAccountKey.setStatus("current")


class _EqlTagValueDescription_Type(UTFString):
    """Custom type eqlTagValueDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlTagValueDescription_Type.__name__ = "UTFString"
_EqlTagValueDescription_Object = MibTableColumn
eqlTagValueDescription = _EqlTagValueDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 1, 1, 6),
    _EqlTagValueDescription_Type()
)
eqlTagValueDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlTagValueDescription.setStatus("current")
_EqlTagObjectTable_Object = MibTable
eqlTagObjectTable = _EqlTagObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 2)
)
if mibBuilder.loadTexts:
    eqlTagObjectTable.setStatus("current")
_EqlTagObjectEntry_Object = MibTableRow
eqlTagObjectEntry = _EqlTagObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 2, 1)
)
eqlTagObjectEntry.setIndexNames(
    (0, "EQLTAG-MIB", "eqlTagType"),
    (0, "EQLTAG-MIB", "eqlTagIndex"),
    (0, "EQLTAG-MIB", "eqlTagObjectIndex"),
)
if mibBuilder.loadTexts:
    eqlTagObjectEntry.setStatus("current")
_EqlTagObjectIndex_Type = Unsigned32
_EqlTagObjectIndex_Object = MibTableColumn
eqlTagObjectIndex = _EqlTagObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 2, 1, 1),
    _EqlTagObjectIndex_Type()
)
eqlTagObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlTagObjectIndex.setStatus("current")
_EqlTagObjectTaggedObjectPointer_Type = RowPointer
_EqlTagObjectTaggedObjectPointer_Object = MibTableColumn
eqlTagObjectTaggedObjectPointer = _EqlTagObjectTaggedObjectPointer_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 2, 1, 2),
    _EqlTagObjectTaggedObjectPointer_Type()
)
eqlTagObjectTaggedObjectPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlTagObjectTaggedObjectPointer.setStatus("current")
_EqlTagObjectRowStatus_Type = RowStatus
_EqlTagObjectRowStatus_Object = MibTableColumn
eqlTagObjectRowStatus = _EqlTagObjectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 2, 1, 3),
    _EqlTagObjectRowStatus_Type()
)
eqlTagObjectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlTagObjectRowStatus.setStatus("current")
_EqlAdminAccountTagTable_Object = MibTable
eqlAdminAccountTagTable = _EqlAdminAccountTagTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 3)
)
if mibBuilder.loadTexts:
    eqlAdminAccountTagTable.setStatus("current")
_EqlAdminAccountTagEntry_Object = MibTableRow
eqlAdminAccountTagEntry = _EqlAdminAccountTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 3, 1)
)
eqlAdminAccountTagEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
    (0, "EQLTAG-MIB", "eqlTagType"),
    (0, "EQLTAG-MIB", "eqlTagIndex"),
)
if mibBuilder.loadTexts:
    eqlAdminAccountTagEntry.setStatus("current")


class _EqlAdminAccountTagAccess_Type(Integer32):
    """Custom type eqlAdminAccountTagAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2))
    )


_EqlAdminAccountTagAccess_Type.__name__ = "Integer32"
_EqlAdminAccountTagAccess_Object = MibTableColumn
eqlAdminAccountTagAccess = _EqlAdminAccountTagAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 3, 1, 1),
    _EqlAdminAccountTagAccess_Type()
)
eqlAdminAccountTagAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAdminAccountTagAccess.setStatus("current")
_EqlVolumeTagTable_Object = MibTable
eqlVolumeTagTable = _EqlVolumeTagTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 4)
)
if mibBuilder.loadTexts:
    eqlVolumeTagTable.setStatus("current")
_EqlVolumeTagEntry_Object = MibTableRow
eqlVolumeTagEntry = _EqlVolumeTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 4, 1)
)
eqlVolumeTagEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLTAG-MIB", "eqlTagType"),
    (0, "EQLTAG-MIB", "eqlTagIndex"),
)
if mibBuilder.loadTexts:
    eqlVolumeTagEntry.setStatus("current")


class _EqlVolumeTagValue_Type(UTFString):
    """Custom type eqlVolumeTagValue based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqlVolumeTagValue_Type.__name__ = "UTFString"
_EqlVolumeTagValue_Object = MibTableColumn
eqlVolumeTagValue = _EqlVolumeTagValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 23, 1, 4, 1, 1),
    _EqlVolumeTagValue_Type()
)
eqlVolumeTagValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVolumeTagValue.setStatus("current")
_EqltagNotifications_ObjectIdentity = ObjectIdentity
eqltagNotifications = _EqltagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 23, 2)
)
_EqltagConformance_ObjectIdentity = ObjectIdentity
eqltagConformance = _EqltagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 23, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLTAG-MIB",
    **{"eqltagModule": eqltagModule,
       "eqltagObjects": eqltagObjects,
       "eqlTagTable": eqlTagTable,
       "eqlTagEntry": eqlTagEntry,
       "eqlTagType": eqlTagType,
       "eqlTagIndex": eqlTagIndex,
       "eqlTagRowStatus": eqlTagRowStatus,
       "eqlTagValue": eqlTagValue,
       "eqlTagAdminAccountKey": eqlTagAdminAccountKey,
       "eqlTagValueDescription": eqlTagValueDescription,
       "eqlTagObjectTable": eqlTagObjectTable,
       "eqlTagObjectEntry": eqlTagObjectEntry,
       "eqlTagObjectIndex": eqlTagObjectIndex,
       "eqlTagObjectTaggedObjectPointer": eqlTagObjectTaggedObjectPointer,
       "eqlTagObjectRowStatus": eqlTagObjectRowStatus,
       "eqlAdminAccountTagTable": eqlAdminAccountTagTable,
       "eqlAdminAccountTagEntry": eqlAdminAccountTagEntry,
       "eqlAdminAccountTagAccess": eqlAdminAccountTagAccess,
       "eqlVolumeTagTable": eqlVolumeTagTable,
       "eqlVolumeTagEntry": eqlVolumeTagEntry,
       "eqlVolumeTagValue": eqlVolumeTagValue,
       "eqltagNotifications": eqltagNotifications,
       "eqltagConformance": eqltagConformance}
)
