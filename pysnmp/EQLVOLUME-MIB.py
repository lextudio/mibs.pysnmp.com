# SNMP MIB module (EQLVOLUME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLVOLUME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:57 2024
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
 eqlGroupTaskIndex,
 eqlLdapLoginAccessName,
 eqlLdapLoginAccessType,
 eqlStorageGroupAdminAccountIndex) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "UTFString",
    "eqlGroupId",
    "eqlGroupTaskIndex",
    "eqlLdapLoginAccessName",
    "eqlLdapLoginAccessType",
    "eqlStorageGroupAdminAccountIndex")

(eqlStoragePoolIndex,) = mibBuilder.importSymbols(
    "EQLSTORAGEPOOL-MIB",
    "eqlStoragePoolIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eqliscsiModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 5)
)
eqliscsiModule.setRevisions(
        ("2002-09-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ACLAppliesTo(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snapshot-only", 2),
          ("volume-and-snapshot", 3),
          ("volume-only", 1))
    )



class SiteIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class SiteIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ReplSiteQuotaType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("size", 1))
    )



class StatusEnabledDefault(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )



class StatusDisabledDefault(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class StatusAutoDefault(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("disabled", 2),
          ("enabled", 1))
    )



class VirtualVolumeType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("config-VVol", 1),
          ("data-VVol", 2),
          ("swap-VVol", 3),
          ("unknown", 0))
    )



class EQLRowPointer(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )



class EQL2PartRowPointerStr(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )



class VirtualVolumeSnapshotStatus(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("in-progress", 1),
          ("unknown", 0))
    )



class VirtualVolumeCreatedAs(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast-clone", 3),
          ("snapshot", 2),
          ("stand-alone", 1))
    )



# MIB Managed Objects in the order of their OIDs

_EqliscsiObjects_ObjectIdentity = ObjectIdentity
eqliscsiObjects = _EqliscsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1)
)
_EqliscsiTarget_ObjectIdentity = ObjectIdentity
eqliscsiTarget = _EqliscsiTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7)
)
_EqliscsiVolumeTable_Object = MibTable
eqliscsiVolumeTable = _EqliscsiVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeTable.setStatus("current")
_EqliscsiVolumeEntry_Object = MibTableRow
eqliscsiVolumeEntry = _EqliscsiVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1)
)
eqliscsiVolumeEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeEntry.setStatus("current")
_EqliscsiVolumeIndex_Type = Unsigned32
_EqliscsiVolumeIndex_Object = MibTableColumn
eqliscsiVolumeIndex = _EqliscsiVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 1),
    _EqliscsiVolumeIndex_Type()
)
eqliscsiVolumeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeIndex.setStatus("current")
_EqliscsiVolumeRowStatus_Type = RowStatus
_EqliscsiVolumeRowStatus_Object = MibTableColumn
eqliscsiVolumeRowStatus = _EqliscsiVolumeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 2),
    _EqliscsiVolumeRowStatus_Type()
)
eqliscsiVolumeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeRowStatus.setStatus("current")


class _EqliscsiVolumePsvId_Type(OctetString):
    """Custom type eqliscsiVolumePsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiVolumePsvId_Type.__name__ = "OctetString"
_EqliscsiVolumePsvId_Object = MibTableColumn
eqliscsiVolumePsvId = _EqliscsiVolumePsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 3),
    _EqliscsiVolumePsvId_Type()
)
eqliscsiVolumePsvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumePsvId.setStatus("current")


class _EqliscsiVolumeName_Type(UTFString):
    """Custom type eqliscsiVolumeName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqliscsiVolumeName_Type.__name__ = "UTFString"
_EqliscsiVolumeName_Object = MibTableColumn
eqliscsiVolumeName = _EqliscsiVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 4),
    _EqliscsiVolumeName_Type()
)
eqliscsiVolumeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeName.setStatus("current")


class _EqliscsiVolumeSite_Type(OctetString):
    """Custom type eqliscsiVolumeSite based on OctetString"""
    defaultValue = OctetString("default")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiVolumeSite_Type.__name__ = "OctetString"
_EqliscsiVolumeSite_Object = MibTableColumn
eqliscsiVolumeSite = _EqliscsiVolumeSite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 5),
    _EqliscsiVolumeSite_Type()
)
eqliscsiVolumeSite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSite.setStatus("current")


class _EqliscsiVolumeDescription_Type(UTFString):
    """Custom type eqliscsiVolumeDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiVolumeDescription_Type.__name__ = "UTFString"
_EqliscsiVolumeDescription_Object = MibTableColumn
eqliscsiVolumeDescription = _EqliscsiVolumeDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 6),
    _EqliscsiVolumeDescription_Type()
)
eqliscsiVolumeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeDescription.setStatus("current")


class _EqliscsiVolumeAccessType_Type(Integer32):
    """Custom type eqliscsiVolumeAccessType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 2),
          ("read-write", 1))
    )


_EqliscsiVolumeAccessType_Type.__name__ = "Integer32"
_EqliscsiVolumeAccessType_Object = MibTableColumn
eqliscsiVolumeAccessType = _EqliscsiVolumeAccessType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 7),
    _EqliscsiVolumeAccessType_Type()
)
eqliscsiVolumeAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeAccessType.setStatus("current")
_EqliscsiVolumeSize_Type = Integer32
_EqliscsiVolumeSize_Object = MibTableColumn
eqliscsiVolumeSize = _EqliscsiVolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 8),
    _EqliscsiVolumeSize_Type()
)
eqliscsiVolumeSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSize.setStatus("current")


class _EqliscsiVolumeAdminStatus_Type(Integer32):
    """Custom type eqliscsiVolumeAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("offline-control", 5),
          ("online", 1),
          ("online-control", 4),
          ("online-lost-cached-blocks", 3))
    )


_EqliscsiVolumeAdminStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeAdminStatus_Object = MibTableColumn
eqliscsiVolumeAdminStatus = _EqliscsiVolumeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 9),
    _EqliscsiVolumeAdminStatus_Type()
)
eqliscsiVolumeAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeAdminStatus.setStatus("current")


class _EqliscsiVolumeReservedPercentage_Type(Integer32):
    """Custom type eqliscsiVolumeReservedPercentage based on Integer32"""
    defaultValue = 100


_EqliscsiVolumeReservedPercentage_Object = MibTableColumn
eqliscsiVolumeReservedPercentage = _EqliscsiVolumeReservedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 10),
    _EqliscsiVolumeReservedPercentage_Type()
)
eqliscsiVolumeReservedPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReservedPercentage.setStatus("current")


class _EqliscsiVolumeSnapWarningLevel_Type(Integer32):
    """Custom type eqliscsiVolumeSnapWarningLevel based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqliscsiVolumeSnapWarningLevel_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapWarningLevel_Object = MibTableColumn
eqliscsiVolumeSnapWarningLevel = _EqliscsiVolumeSnapWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 11),
    _EqliscsiVolumeSnapWarningLevel_Type()
)
eqliscsiVolumeSnapWarningLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapWarningLevel.setStatus("current")


class _EqliscsiVolumeSnapDeletionPolicy_Type(Integer32):
    """Custom type eqliscsiVolumeSnapDeletionPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete-oldest", 2),
          ("make-volume-offline", 1),
          ("stop-snapshots", 3))
    )


_EqliscsiVolumeSnapDeletionPolicy_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapDeletionPolicy_Object = MibTableColumn
eqliscsiVolumeSnapDeletionPolicy = _EqliscsiVolumeSnapDeletionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 12),
    _EqliscsiVolumeSnapDeletionPolicy_Type()
)
eqliscsiVolumeSnapDeletionPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapDeletionPolicy.setStatus("current")


class _EqliscsiVolumeAutoloadBalancing_Type(Integer32):
    """Custom type eqliscsiVolumeAutoloadBalancing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EqliscsiVolumeAutoloadBalancing_Type.__name__ = "Integer32"
_EqliscsiVolumeAutoloadBalancing_Object = MibTableColumn
eqliscsiVolumeAutoloadBalancing = _EqliscsiVolumeAutoloadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 13),
    _EqliscsiVolumeAutoloadBalancing_Type()
)
eqliscsiVolumeAutoloadBalancing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeAutoloadBalancing.setStatus("current")


class _EqliscsiVolumeTargetAlias_Type(OctetString):
    """Custom type eqliscsiVolumeTargetAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiVolumeTargetAlias_Type.__name__ = "OctetString"
_EqliscsiVolumeTargetAlias_Object = MibTableColumn
eqliscsiVolumeTargetAlias = _EqliscsiVolumeTargetAlias_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 14),
    _EqliscsiVolumeTargetAlias_Type()
)
eqliscsiVolumeTargetAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeTargetAlias.setStatus("current")


class _EqliscsiVolumeTargetIscsiName_Type(OctetString):
    """Custom type eqliscsiVolumeTargetIscsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiVolumeTargetIscsiName_Type.__name__ = "OctetString"
_EqliscsiVolumeTargetIscsiName_Object = MibTableColumn
eqliscsiVolumeTargetIscsiName = _EqliscsiVolumeTargetIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 15),
    _EqliscsiVolumeTargetIscsiName_Type()
)
eqliscsiVolumeTargetIscsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeTargetIscsiName.setStatus("current")
_EqliscsiVolumeNodeIndex_Type = Unsigned32
_EqliscsiVolumeNodeIndex_Object = MibTableColumn
eqliscsiVolumeNodeIndex = _EqliscsiVolumeNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 16),
    _EqliscsiVolumeNodeIndex_Type()
)
eqliscsiVolumeNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeNodeIndex.setStatus("current")


class _EqliscsiVolumeHdrDigests_Type(TruthValue):
    """Custom type eqliscsiVolumeHdrDigests based on TruthValue"""


_EqliscsiVolumeHdrDigests_Object = MibTableColumn
eqliscsiVolumeHdrDigests = _EqliscsiVolumeHdrDigests_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 17),
    _EqliscsiVolumeHdrDigests_Type()
)
eqliscsiVolumeHdrDigests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeHdrDigests.setStatus("current")


class _EqliscsiVolumeDataDigests_Type(TruthValue):
    """Custom type eqliscsiVolumeDataDigests based on TruthValue"""


_EqliscsiVolumeDataDigests_Object = MibTableColumn
eqliscsiVolumeDataDigests = _EqliscsiVolumeDataDigests_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 18),
    _EqliscsiVolumeDataDigests_Type()
)
eqliscsiVolumeDataDigests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeDataDigests.setStatus("current")


class _EqliscsiVolumeCloneSrcPsvId_Type(OctetString):
    """Custom type eqliscsiVolumeCloneSrcPsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiVolumeCloneSrcPsvId_Type.__name__ = "OctetString"
_EqliscsiVolumeCloneSrcPsvId_Object = MibTableColumn
eqliscsiVolumeCloneSrcPsvId = _EqliscsiVolumeCloneSrcPsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 19),
    _EqliscsiVolumeCloneSrcPsvId_Type()
)
eqliscsiVolumeCloneSrcPsvId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeCloneSrcPsvId.setStatus("current")


class _EqliscsiVolumeReplService_Type(Integer32):
    """Custom type eqliscsiVolumeReplService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("failover", 6),
          ("host-control-target", 5),
          ("none", 1),
          ("pe-control-target", 7),
          ("replica-control-target", 4),
          ("replica-site", 2),
          ("replicated-primary", 3))
    )


_EqliscsiVolumeReplService_Type.__name__ = "Integer32"
_EqliscsiVolumeReplService_Object = MibTableColumn
eqliscsiVolumeReplService = _EqliscsiVolumeReplService_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 20),
    _EqliscsiVolumeReplService_Type()
)
eqliscsiVolumeReplService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplService.setStatus("current")


class _EqliscsiVolumeMultInitiator_Type(Integer32):
    """Custom type eqliscsiVolumeMultInitiator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 0),
          ("not-allowed", 1))
    )


_EqliscsiVolumeMultInitiator_Type.__name__ = "Integer32"
_EqliscsiVolumeMultInitiator_Object = MibTableColumn
eqliscsiVolumeMultInitiator = _EqliscsiVolumeMultInitiator_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 21),
    _EqliscsiVolumeMultInitiator_Type()
)
eqliscsiVolumeMultInitiator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeMultInitiator.setStatus("current")
_EqliscsiVolumeStoragePoolIndex_Type = Unsigned32
_EqliscsiVolumeStoragePoolIndex_Object = MibTableColumn
eqliscsiVolumeStoragePoolIndex = _EqliscsiVolumeStoragePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 22),
    _EqliscsiVolumeStoragePoolIndex_Type()
)
eqliscsiVolumeStoragePoolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeStoragePoolIndex.setStatus("current")
_EqliscsiVolumeStoragePoolSourceIndex_Type = Unsigned32
_EqliscsiVolumeStoragePoolSourceIndex_Object = MibTableColumn
eqliscsiVolumeStoragePoolSourceIndex = _EqliscsiVolumeStoragePoolSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 23),
    _EqliscsiVolumeStoragePoolSourceIndex_Type()
)
eqliscsiVolumeStoragePoolSourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeStoragePoolSourceIndex.setStatus("current")
_EqliscsiVolumeTargetLocalMemberId_Type = Unsigned32
_EqliscsiVolumeTargetLocalMemberId_Object = MibTableColumn
eqliscsiVolumeTargetLocalMemberId = _EqliscsiVolumeTargetLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 24),
    _EqliscsiVolumeTargetLocalMemberId_Type()
)
eqliscsiVolumeTargetLocalMemberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeTargetLocalMemberId.setStatus("current")
_EqliscsiVolumeTargetIndex_Type = Unsigned32
_EqliscsiVolumeTargetIndex_Object = MibTableColumn
eqliscsiVolumeTargetIndex = _EqliscsiVolumeTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 25),
    _EqliscsiVolumeTargetIndex_Type()
)
eqliscsiVolumeTargetIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeTargetIndex.setStatus("current")


class _EqliscsiVolumeThinProvision_Type(TruthValue):
    """Custom type eqliscsiVolumeThinProvision based on TruthValue"""


_EqliscsiVolumeThinProvision_Object = MibTableColumn
eqliscsiVolumeThinProvision = _EqliscsiVolumeThinProvision_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 26),
    _EqliscsiVolumeThinProvision_Type()
)
eqliscsiVolumeThinProvision.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeThinProvision.setStatus("current")


class _EqliscsiVolumeMinThinReserve_Type(Unsigned32):
    """Custom type eqliscsiVolumeMinThinReserve based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EqliscsiVolumeMinThinReserve_Type.__name__ = "Unsigned32"
_EqliscsiVolumeMinThinReserve_Object = MibTableColumn
eqliscsiVolumeMinThinReserve = _EqliscsiVolumeMinThinReserve_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 27),
    _EqliscsiVolumeMinThinReserve_Type()
)
eqliscsiVolumeMinThinReserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeMinThinReserve.setStatus("current")


class _EqliscsiVolumeThinWarnPercentage_Type(Unsigned32):
    """Custom type eqliscsiVolumeThinWarnPercentage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqliscsiVolumeThinWarnPercentage_Type.__name__ = "Unsigned32"
_EqliscsiVolumeThinWarnPercentage_Object = MibTableColumn
eqliscsiVolumeThinWarnPercentage = _EqliscsiVolumeThinWarnPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 28),
    _EqliscsiVolumeThinWarnPercentage_Type()
)
eqliscsiVolumeThinWarnPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeThinWarnPercentage.setStatus("current")


class _EqliscsiVolumeThinMaxGrowPercentage_Type(Unsigned32):
    """Custom type eqliscsiVolumeThinMaxGrowPercentage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqliscsiVolumeThinMaxGrowPercentage_Type.__name__ = "Unsigned32"
_EqliscsiVolumeThinMaxGrowPercentage_Object = MibTableColumn
eqliscsiVolumeThinMaxGrowPercentage = _EqliscsiVolumeThinMaxGrowPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 29),
    _EqliscsiVolumeThinMaxGrowPercentage_Type()
)
eqliscsiVolumeThinMaxGrowPercentage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeThinMaxGrowPercentage.setStatus("current")


class _EqliscsiVolumeShrinkAutoAdjust_Type(TruthValue):
    """Custom type eqliscsiVolumeShrinkAutoAdjust based on TruthValue"""


_EqliscsiVolumeShrinkAutoAdjust_Object = MibTableColumn
eqliscsiVolumeShrinkAutoAdjust = _EqliscsiVolumeShrinkAutoAdjust_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 30),
    _EqliscsiVolumeShrinkAutoAdjust_Type()
)
eqliscsiVolumeShrinkAutoAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeShrinkAutoAdjust.setStatus("current")
_EqliscsiVolumeReplRollbackSeqNum_Type = Counter64
_EqliscsiVolumeReplRollbackSeqNum_Object = MibTableColumn
eqliscsiVolumeReplRollbackSeqNum = _EqliscsiVolumeReplRollbackSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 31),
    _EqliscsiVolumeReplRollbackSeqNum_Type()
)
eqliscsiVolumeReplRollbackSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplRollbackSeqNum.setStatus("current")


class _EqliscsiVolumeThinWarnMode_Type(Integer32):
    """Custom type eqliscsiVolumeThinWarnMode based on Integer32"""
    defaultValue = 0

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
        *(("warnWithHardOnly", 4),
          ("warnWithIscsi", 1),
          ("warnWithOffline", 0),
          ("warnWithOfflineForced", 2),
          ("warnWithSoftOnly", 3))
    )


_EqliscsiVolumeThinWarnMode_Type.__name__ = "Integer32"
_EqliscsiVolumeThinWarnMode_Object = MibTableColumn
eqliscsiVolumeThinWarnMode = _EqliscsiVolumeThinWarnMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 32),
    _EqliscsiVolumeThinWarnMode_Type()
)
eqliscsiVolumeThinWarnMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeThinWarnMode.setStatus("current")


class _EqliscsiVolumeFlags_Type(Bits):
    """Custom type eqliscsiVolumeFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("flag12", 12),
          ("flag13", 13),
          ("flag14", 14),
          ("flag15", 15),
          ("flag16", 16),
          ("flag17", 17),
          ("flag18", 18),
          ("flag19", 19),
          ("flag20", 20),
          ("flag21", 21),
          ("flag22", 22),
          ("flag23", 23),
          ("flag24", 24),
          ("flag25", 25),
          ("flag26", 26),
          ("flag27", 27),
          ("flag28", 28),
          ("flag29", 29),
          ("flag3", 3),
          ("flag30", 30),
          ("flag31", 31),
          ("flag4", 4),
          ("flag5", 5),
          ("flag8", 8),
          ("flags11", 11),
          ("iSNSDiscoverable", 0),
          ("isDeleted", 10),
          ("isNASVolume", 6),
          ("isPoolSyncReplicated", 2),
          ("isSyncRepAfoEnabled", 7),
          ("isUnmanaged", 1),
          ("syncReplAllowUnprotectedAccess", 9))
    )

_EqliscsiVolumeFlags_Type.__name__ = "Bits"
_EqliscsiVolumeFlags_Object = MibTableColumn
eqliscsiVolumeFlags = _EqliscsiVolumeFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 33),
    _EqliscsiVolumeFlags_Type()
)
eqliscsiVolumeFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeFlags.setStatus("current")


class _EqliscsiVolumeTemplate_Type(TruthValue):
    """Custom type eqliscsiVolumeTemplate based on TruthValue"""


_EqliscsiVolumeTemplate_Object = MibTableColumn
eqliscsiVolumeTemplate = _EqliscsiVolumeTemplate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 34),
    _EqliscsiVolumeTemplate_Type()
)
eqliscsiVolumeTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeTemplate.setStatus("current")


class _EqliscsiVolumeThinClone_Type(TruthValue):
    """Custom type eqliscsiVolumeThinClone based on TruthValue"""


_EqliscsiVolumeThinClone_Object = MibTableColumn
eqliscsiVolumeThinClone = _EqliscsiVolumeThinClone_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 35),
    _EqliscsiVolumeThinClone_Type()
)
eqliscsiVolumeThinClone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeThinClone.setStatus("current")


class _EqliscsiVolumeThinCloneParentMemberId_Type(Unsigned32):
    """Custom type eqliscsiVolumeThinCloneParentMemberId based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolumeThinCloneParentMemberId_Object = MibTableColumn
eqliscsiVolumeThinCloneParentMemberId = _EqliscsiVolumeThinCloneParentMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 36),
    _EqliscsiVolumeThinCloneParentMemberId_Type()
)
eqliscsiVolumeThinCloneParentMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeThinCloneParentMemberId.setStatus("current")


class _EqliscsiVolumeThinCloneParentVolIndex_Type(Unsigned32):
    """Custom type eqliscsiVolumeThinCloneParentVolIndex based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolumeThinCloneParentVolIndex_Object = MibTableColumn
eqliscsiVolumeThinCloneParentVolIndex = _EqliscsiVolumeThinCloneParentVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 37),
    _EqliscsiVolumeThinCloneParentVolIndex_Type()
)
eqliscsiVolumeThinCloneParentVolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeThinCloneParentVolIndex.setStatus("current")


class _EqliscsiVolumeThinCloneParentPsvId_Type(OctetString):
    """Custom type eqliscsiVolumeThinCloneParentPsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiVolumeThinCloneParentPsvId_Type.__name__ = "OctetString"
_EqliscsiVolumeThinCloneParentPsvId_Object = MibTableColumn
eqliscsiVolumeThinCloneParentPsvId = _EqliscsiVolumeThinCloneParentPsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 38),
    _EqliscsiVolumeThinCloneParentPsvId_Type()
)
eqliscsiVolumeThinCloneParentPsvId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeThinCloneParentPsvId.setStatus("current")


class _EqliscsiVolumeAdminAccountKey_Type(Unsigned32):
    """Custom type eqliscsiVolumeAdminAccountKey based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolumeAdminAccountKey_Object = MibTableColumn
eqliscsiVolumeAdminAccountKey = _EqliscsiVolumeAdminAccountKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 39),
    _EqliscsiVolumeAdminAccountKey_Type()
)
eqliscsiVolumeAdminAccountKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeAdminAccountKey.setStatus("current")


class _EqliscsiVolumeSCSIQErr_Type(Integer32):
    """Custom type eqliscsiVolumeSCSIQErr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("allCommandsAborted", 5),
          ("none", 0),
          ("oneOne", 4),
          ("oneZero", 3),
          ("zeroOne", 2),
          ("zeroZero", 1))
    )


_EqliscsiVolumeSCSIQErr_Type.__name__ = "Integer32"
_EqliscsiVolumeSCSIQErr_Object = MibTableColumn
eqliscsiVolumeSCSIQErr = _EqliscsiVolumeSCSIQErr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 40),
    _EqliscsiVolumeSCSIQErr_Type()
)
eqliscsiVolumeSCSIQErr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSCSIQErr.setStatus("current")


class _EqliscsiVolumeBorrow_Type(StatusAutoDefault):
    """Custom type eqliscsiVolumeBorrow based on StatusAutoDefault"""


_EqliscsiVolumeBorrow_Object = MibTableColumn
eqliscsiVolumeBorrow = _EqliscsiVolumeBorrow_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 41),
    _EqliscsiVolumeBorrow_Type()
)
eqliscsiVolumeBorrow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeBorrow.setStatus("current")


class _EqliscsiVolumeSectorSize_Type(Integer32):
    """Custom type eqliscsiVolumeSectorSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sector-size-4096-bytes", 1),
          ("sector-size-512-bytes", 0))
    )


_EqliscsiVolumeSectorSize_Type.__name__ = "Integer32"
_EqliscsiVolumeSectorSize_Object = MibTableColumn
eqliscsiVolumeSectorSize = _EqliscsiVolumeSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 1, 1, 42),
    _EqliscsiVolumeSectorSize_Type()
)
eqliscsiVolumeSectorSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSectorSize.setStatus("current")
_EqliscsiSnapshotTable_Object = MibTable
eqliscsiSnapshotTable = _EqliscsiSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2)
)
if mibBuilder.loadTexts:
    eqliscsiSnapshotTable.setStatus("current")
_EqliscsiSnapshotEntry_Object = MibTableRow
eqliscsiSnapshotEntry = _EqliscsiSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1)
)
eqliscsiSnapshotEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiSnapshotIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiSnapshotEntry.setStatus("current")
_EqliscsiSnapshotIndex_Type = Unsigned32
_EqliscsiSnapshotIndex_Object = MibTableColumn
eqliscsiSnapshotIndex = _EqliscsiSnapshotIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 1),
    _EqliscsiSnapshotIndex_Type()
)
eqliscsiSnapshotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSnapshotIndex.setStatus("current")
_EqliscsiSnapshotRowStatus_Type = RowStatus
_EqliscsiSnapshotRowStatus_Object = MibTableColumn
eqliscsiSnapshotRowStatus = _EqliscsiSnapshotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 2),
    _EqliscsiSnapshotRowStatus_Type()
)
eqliscsiSnapshotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotRowStatus.setStatus("current")


class _EqliscsiSnapshotPsvId_Type(OctetString):
    """Custom type eqliscsiSnapshotPsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiSnapshotPsvId_Type.__name__ = "OctetString"
_EqliscsiSnapshotPsvId_Object = MibTableColumn
eqliscsiSnapshotPsvId = _EqliscsiSnapshotPsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 3),
    _EqliscsiSnapshotPsvId_Type()
)
eqliscsiSnapshotPsvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotPsvId.setStatus("current")


class _EqliscsiSnapshotBasePsvId_Type(OctetString):
    """Custom type eqliscsiSnapshotBasePsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiSnapshotBasePsvId_Type.__name__ = "OctetString"
_EqliscsiSnapshotBasePsvId_Object = MibTableColumn
eqliscsiSnapshotBasePsvId = _EqliscsiSnapshotBasePsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 4),
    _EqliscsiSnapshotBasePsvId_Type()
)
eqliscsiSnapshotBasePsvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotBasePsvId.setStatus("current")


class _EqliscsiSnapshotName_Type(OctetString):
    """Custom type eqliscsiSnapshotName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiSnapshotName_Type.__name__ = "OctetString"
_EqliscsiSnapshotName_Object = MibTableColumn
eqliscsiSnapshotName = _EqliscsiSnapshotName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 5),
    _EqliscsiSnapshotName_Type()
)
eqliscsiSnapshotName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotName.setStatus("current")


class _EqliscsiSnapshotAccessType_Type(Integer32):
    """Custom type eqliscsiSnapshotAccessType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 2),
          ("read-write", 1))
    )


_EqliscsiSnapshotAccessType_Type.__name__ = "Integer32"
_EqliscsiSnapshotAccessType_Object = MibTableColumn
eqliscsiSnapshotAccessType = _EqliscsiSnapshotAccessType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 6),
    _EqliscsiSnapshotAccessType_Type()
)
eqliscsiSnapshotAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotAccessType.setStatus("current")
_EqliscsiSnapshotSize_Type = Integer32
_EqliscsiSnapshotSize_Object = MibTableColumn
eqliscsiSnapshotSize = _EqliscsiSnapshotSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 7),
    _EqliscsiSnapshotSize_Type()
)
eqliscsiSnapshotSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotSize.setStatus("current")


class _EqliscsiSnapshotAdminStatus_Type(Integer32):
    """Custom type eqliscsiSnapshotAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("online-lost-cached-blocks", 3))
    )


_EqliscsiSnapshotAdminStatus_Type.__name__ = "Integer32"
_EqliscsiSnapshotAdminStatus_Object = MibTableColumn
eqliscsiSnapshotAdminStatus = _EqliscsiSnapshotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 8),
    _EqliscsiSnapshotAdminStatus_Type()
)
eqliscsiSnapshotAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotAdminStatus.setStatus("current")
_EqliscsiSnapshotTimestamp_Type = Counter32
_EqliscsiSnapshotTimestamp_Object = MibTableColumn
eqliscsiSnapshotTimestamp = _EqliscsiSnapshotTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 9),
    _EqliscsiSnapshotTimestamp_Type()
)
eqliscsiSnapshotTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotTimestamp.setStatus("current")


class _EqliscsiSnapshotScheduleName_Type(OctetString):
    """Custom type eqliscsiSnapshotScheduleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiSnapshotScheduleName_Type.__name__ = "OctetString"
_EqliscsiSnapshotScheduleName_Object = MibTableColumn
eqliscsiSnapshotScheduleName = _EqliscsiSnapshotScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 10),
    _EqliscsiSnapshotScheduleName_Type()
)
eqliscsiSnapshotScheduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotScheduleName.setStatus("current")


class _EqliscsiSnapshotRollBack_Type(TruthValue):
    """Custom type eqliscsiSnapshotRollBack based on TruthValue"""
    defaultValue = 2


_EqliscsiSnapshotRollBack_Object = MibTableColumn
eqliscsiSnapshotRollBack = _EqliscsiSnapshotRollBack_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 11),
    _EqliscsiSnapshotRollBack_Type()
)
eqliscsiSnapshotRollBack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotRollBack.setStatus("current")


class _EqliscsiSnapshotTargetAlias_Type(OctetString):
    """Custom type eqliscsiSnapshotTargetAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiSnapshotTargetAlias_Type.__name__ = "OctetString"
_EqliscsiSnapshotTargetAlias_Object = MibTableColumn
eqliscsiSnapshotTargetAlias = _EqliscsiSnapshotTargetAlias_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 12),
    _EqliscsiSnapshotTargetAlias_Type()
)
eqliscsiSnapshotTargetAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotTargetAlias.setStatus("current")


class _EqliscsiSnapshotTargetIscsiName_Type(OctetString):
    """Custom type eqliscsiSnapshotTargetIscsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiSnapshotTargetIscsiName_Type.__name__ = "OctetString"
_EqliscsiSnapshotTargetIscsiName_Object = MibTableColumn
eqliscsiSnapshotTargetIscsiName = _EqliscsiSnapshotTargetIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 13),
    _EqliscsiSnapshotTargetIscsiName_Type()
)
eqliscsiSnapshotTargetIscsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotTargetIscsiName.setStatus("current")
_EqliscsiSnapshotScheduleIndex_Type = Integer32
_EqliscsiSnapshotScheduleIndex_Object = MibTableColumn
eqliscsiSnapshotScheduleIndex = _EqliscsiSnapshotScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 14),
    _EqliscsiSnapshotScheduleIndex_Type()
)
eqliscsiSnapshotScheduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotScheduleIndex.setStatus("current")


class _EqliscsiSnapshotDescription_Type(UTFString):
    """Custom type eqliscsiSnapshotDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiSnapshotDescription_Type.__name__ = "UTFString"
_EqliscsiSnapshotDescription_Object = MibTableColumn
eqliscsiSnapshotDescription = _EqliscsiSnapshotDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 15),
    _EqliscsiSnapshotDescription_Type()
)
eqliscsiSnapshotDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotDescription.setStatus("current")
_EqliscsiSnapshotNodeIndex_Type = Unsigned32
_EqliscsiSnapshotNodeIndex_Object = MibTableColumn
eqliscsiSnapshotNodeIndex = _EqliscsiSnapshotNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 16),
    _EqliscsiSnapshotNodeIndex_Type()
)
eqliscsiSnapshotNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotNodeIndex.setStatus("current")
_EqliscsiSnapshotReplicated_Type = SiteIndexOrZero
_EqliscsiSnapshotReplicated_Object = MibTableColumn
eqliscsiSnapshotReplicated = _EqliscsiSnapshotReplicated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 17),
    _EqliscsiSnapshotReplicated_Type()
)
eqliscsiSnapshotReplicated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotReplicated.setStatus("current")


class _EqliscsiSnapshotType_Type(Integer32):
    """Custom type eqliscsiSnapshotType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("replica-site", 2),
          ("sync-repl-failback", 4),
          ("sync-repl-protected", 3))
    )


_EqliscsiSnapshotType_Type.__name__ = "Integer32"
_EqliscsiSnapshotType_Object = MibTableColumn
eqliscsiSnapshotType = _EqliscsiSnapshotType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 18),
    _EqliscsiSnapshotType_Type()
)
eqliscsiSnapshotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotType.setStatus("current")


class _EqliscsiSnapshotCollectionIndex_Type(Integer32):
    """Custom type eqliscsiSnapshotCollectionIndex based on Integer32"""
    defaultValue = 0


_EqliscsiSnapshotCollectionIndex_Object = MibTableColumn
eqliscsiSnapshotCollectionIndex = _EqliscsiSnapshotCollectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 19),
    _EqliscsiSnapshotCollectionIndex_Type()
)
eqliscsiSnapshotCollectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotCollectionIndex.setStatus("current")
_EqliscsiSnapshotStoragePoolIndex_Type = Unsigned32
_EqliscsiSnapshotStoragePoolIndex_Object = MibTableColumn
eqliscsiSnapshotStoragePoolIndex = _EqliscsiSnapshotStoragePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 20),
    _EqliscsiSnapshotStoragePoolIndex_Type()
)
eqliscsiSnapshotStoragePoolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotStoragePoolIndex.setStatus("current")
_EqliscsiSnapshotTargetLocalMemberId_Type = Unsigned32
_EqliscsiSnapshotTargetLocalMemberId_Object = MibTableColumn
eqliscsiSnapshotTargetLocalMemberId = _EqliscsiSnapshotTargetLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 21),
    _EqliscsiSnapshotTargetLocalMemberId_Type()
)
eqliscsiSnapshotTargetLocalMemberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiSnapshotTargetLocalMemberId.setStatus("current")
_EqliscsiSnapshotTargetIndex_Type = Unsigned32
_EqliscsiSnapshotTargetIndex_Object = MibTableColumn
eqliscsiSnapshotTargetIndex = _EqliscsiSnapshotTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 22),
    _EqliscsiSnapshotTargetIndex_Type()
)
eqliscsiSnapshotTargetIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiSnapshotTargetIndex.setStatus("current")


class _EqliscsiSnapshotMultInitiator_Type(Integer32):
    """Custom type eqliscsiSnapshotMultInitiator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 0),
          ("not-allowed", 1))
    )


_EqliscsiSnapshotMultInitiator_Type.__name__ = "Integer32"
_EqliscsiSnapshotMultInitiator_Object = MibTableColumn
eqliscsiSnapshotMultInitiator = _EqliscsiSnapshotMultInitiator_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 23),
    _EqliscsiSnapshotMultInitiator_Type()
)
eqliscsiSnapshotMultInitiator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiSnapshotMultInitiator.setStatus("current")


class _EqliscsiSnapshotFlags_Type(Bits):
    """Custom type eqliscsiSnapshotFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("compressible", 2),
          ("externalPauseReplication", 1),
          ("flag10", 10),
          ("flag11", 11),
          ("flag12", 12),
          ("flag13", 13),
          ("flag14", 14),
          ("flag15", 15),
          ("flag16", 16),
          ("flag17", 17),
          ("flag18", 18),
          ("flag19", 19),
          ("flag20", 20),
          ("flag21", 21),
          ("flag22", 22),
          ("flag23", 23),
          ("flag24", 24),
          ("flag25", 25),
          ("flag26", 26),
          ("flag27", 27),
          ("flag28", 28),
          ("flag29", 29),
          ("flag3", 3),
          ("flag30", 30),
          ("flag31", 31),
          ("flag4", 4),
          ("flag5", 5),
          ("flag6", 6),
          ("flag7", 7),
          ("flag8", 8),
          ("flag9", 9),
          ("iSNSDiscoverable", 0))
    )

_EqliscsiSnapshotFlags_Type.__name__ = "Bits"
_EqliscsiSnapshotFlags_Object = MibTableColumn
eqliscsiSnapshotFlags = _EqliscsiSnapshotFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 24),
    _EqliscsiSnapshotFlags_Type()
)
eqliscsiSnapshotFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotFlags.setStatus("current")
_EqliscsiSnapshotCompressionDelay_Type = Unsigned32
_EqliscsiSnapshotCompressionDelay_Object = MibTableColumn
eqliscsiSnapshotCompressionDelay = _EqliscsiSnapshotCompressionDelay_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 25),
    _EqliscsiSnapshotCompressionDelay_Type()
)
eqliscsiSnapshotCompressionDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiSnapshotCompressionDelay.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapshotCompressionDelay.setUnits("minutes")
_EqliscsiSnapshotLifeExpectancy_Type = Unsigned32
_EqliscsiSnapshotLifeExpectancy_Object = MibTableColumn
eqliscsiSnapshotLifeExpectancy = _EqliscsiSnapshotLifeExpectancy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 2, 1, 26),
    _EqliscsiSnapshotLifeExpectancy_Type()
)
eqliscsiSnapshotLifeExpectancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiSnapshotLifeExpectancy.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapshotLifeExpectancy.setUnits("minutes")
_EqliscsiVolumeMemberTable_Object = MibTable
eqliscsiVolumeMemberTable = _EqliscsiVolumeMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 3)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeMemberTable.setStatus("current")
_EqliscsiVolumeMemberEntry_Object = MibTableRow
eqliscsiVolumeMemberEntry = _EqliscsiVolumeMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 3, 1)
)
eqliscsiVolumeMemberEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeMemberIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeMemberEntry.setStatus("current")
_EqliscsiVolumeMemberIndex_Type = Integer32
_EqliscsiVolumeMemberIndex_Object = MibTableColumn
eqliscsiVolumeMemberIndex = _EqliscsiVolumeMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 3, 1, 1),
    _EqliscsiVolumeMemberIndex_Type()
)
eqliscsiVolumeMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeMemberIndex.setStatus("current")
_EqliscsiVolumeMemberPssId_Type = Integer32
_EqliscsiVolumeMemberPssId_Object = MibTableColumn
eqliscsiVolumeMemberPssId = _EqliscsiVolumeMemberPssId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 3, 1, 2),
    _EqliscsiVolumeMemberPssId_Type()
)
eqliscsiVolumeMemberPssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeMemberPssId.setStatus("current")
_EqliscsiVolumeMemberShareOfVolume_Type = Integer32
_EqliscsiVolumeMemberShareOfVolume_Object = MibTableColumn
eqliscsiVolumeMemberShareOfVolume = _EqliscsiVolumeMemberShareOfVolume_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 3, 1, 3),
    _EqliscsiVolumeMemberShareOfVolume_Type()
)
eqliscsiVolumeMemberShareOfVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeMemberShareOfVolume.setStatus("current")
_EqliscsiVolumeInitiatorsTable_Object = MibTable
eqliscsiVolumeInitiatorsTable = _EqliscsiVolumeInitiatorsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 4)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeInitiatorsTable.setStatus("deprecated")
_EqliscsiVolumeInitiatorsEntry_Object = MibTableRow
eqliscsiVolumeInitiatorsEntry = _EqliscsiVolumeInitiatorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 4, 1)
)
eqliscsiVolumeInitiatorsEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeInitiatorsIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeInitiatorsEntry.setStatus("current")
_EqliscsiVolumeInitiatorsIndex_Type = Integer32
_EqliscsiVolumeInitiatorsIndex_Object = MibTableColumn
eqliscsiVolumeInitiatorsIndex = _EqliscsiVolumeInitiatorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 4, 1, 1),
    _EqliscsiVolumeInitiatorsIndex_Type()
)
eqliscsiVolumeInitiatorsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeInitiatorsIndex.setStatus("current")


class _EqliscsiVolumeInitiatorsName_Type(OctetString):
    """Custom type eqliscsiVolumeInitiatorsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiVolumeInitiatorsName_Type.__name__ = "OctetString"
_EqliscsiVolumeInitiatorsName_Object = MibTableColumn
eqliscsiVolumeInitiatorsName = _EqliscsiVolumeInitiatorsName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 4, 1, 2),
    _EqliscsiVolumeInitiatorsName_Type()
)
eqliscsiVolumeInitiatorsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeInitiatorsName.setStatus("current")
_EqliscsiVolumeSnapshotPolicyTable_Object = MibTable
eqliscsiVolumeSnapshotPolicyTable = _EqliscsiVolumeSnapshotPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyTable.setStatus("current")
_EqliscsiVolumeSnapshotPolicyEntry_Object = MibTableRow
eqliscsiVolumeSnapshotPolicyEntry = _EqliscsiVolumeSnapshotPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1)
)
eqliscsiVolumeSnapshotPolicyEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeSnapshotPolicyIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyEntry.setStatus("current")
_EqliscsiVolumeSnapshotPolicyIndex_Type = Integer32
_EqliscsiVolumeSnapshotPolicyIndex_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyIndex = _EqliscsiVolumeSnapshotPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 1),
    _EqliscsiVolumeSnapshotPolicyIndex_Type()
)
eqliscsiVolumeSnapshotPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyIndex.setStatus("current")
_EqliscsiVolumeSnapshotPolicyRowStatus_Type = RowStatus
_EqliscsiVolumeSnapshotPolicyRowStatus_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyRowStatus = _EqliscsiVolumeSnapshotPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 2),
    _EqliscsiVolumeSnapshotPolicyRowStatus_Type()
)
eqliscsiVolumeSnapshotPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyRowStatus.setStatus("current")


class _EqliscsiVolumeSnapshotPolicyName_Type(OctetString):
    """Custom type eqliscsiVolumeSnapshotPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqliscsiVolumeSnapshotPolicyName_Type.__name__ = "OctetString"
_EqliscsiVolumeSnapshotPolicyName_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyName = _EqliscsiVolumeSnapshotPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 3),
    _EqliscsiVolumeSnapshotPolicyName_Type()
)
eqliscsiVolumeSnapshotPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyName.setStatus("current")


class _EqliscsiVolumeSnapshotPolicyAccessType_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyAccessType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 2),
          ("read-write", 1))
    )


_EqliscsiVolumeSnapshotPolicyAccessType_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyAccessType_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyAccessType = _EqliscsiVolumeSnapshotPolicyAccessType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 4),
    _EqliscsiVolumeSnapshotPolicyAccessType_Type()
)
eqliscsiVolumeSnapshotPolicyAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyAccessType.setStatus("current")


class _EqliscsiVolumeSnapshotPolicyStatus_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_EqliscsiVolumeSnapshotPolicyStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyStatus_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyStatus = _EqliscsiVolumeSnapshotPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 5),
    _EqliscsiVolumeSnapshotPolicyStatus_Type()
)
eqliscsiVolumeSnapshotPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyStatus.setStatus("current")


class _EqliscsiVolumeSnapshotPolicyMaxKeep_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyMaxKeep based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqliscsiVolumeSnapshotPolicyMaxKeep_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyMaxKeep_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyMaxKeep = _EqliscsiVolumeSnapshotPolicyMaxKeep_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 6),
    _EqliscsiVolumeSnapshotPolicyMaxKeep_Type()
)
eqliscsiVolumeSnapshotPolicyMaxKeep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyMaxKeep.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyMaxKeep.setUnits("snapshots")


class _EqliscsiVolumeSnapshotPolicyType_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("daily", 2),
          ("hourly", 5),
          ("monthly", 4),
          ("once", 1),
          ("weekly", 3))
    )


_EqliscsiVolumeSnapshotPolicyType_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyType_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyType = _EqliscsiVolumeSnapshotPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 7),
    _EqliscsiVolumeSnapshotPolicyType_Type()
)
eqliscsiVolumeSnapshotPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyType.setStatus("current")


class _EqliscsiVolumeSnapshotPolicyRepeatFactor_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyRepeatFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqliscsiVolumeSnapshotPolicyRepeatFactor_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyRepeatFactor_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyRepeatFactor = _EqliscsiVolumeSnapshotPolicyRepeatFactor_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 8),
    _EqliscsiVolumeSnapshotPolicyRepeatFactor_Type()
)
eqliscsiVolumeSnapshotPolicyRepeatFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyRepeatFactor.setStatus("current")


class _EqliscsiVolumeSnapshotPolicyStartTime_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyStartTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_EqliscsiVolumeSnapshotPolicyStartTime_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyStartTime_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyStartTime = _EqliscsiVolumeSnapshotPolicyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 9),
    _EqliscsiVolumeSnapshotPolicyStartTime_Type()
)
eqliscsiVolumeSnapshotPolicyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyStartTime.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyStartTime.setUnits("minutes")


class _EqliscsiVolumeSnapshotPolicyEndTime_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_EqliscsiVolumeSnapshotPolicyEndTime_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyEndTime_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyEndTime = _EqliscsiVolumeSnapshotPolicyEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 10),
    _EqliscsiVolumeSnapshotPolicyEndTime_Type()
)
eqliscsiVolumeSnapshotPolicyEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyEndTime.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyEndTime.setUnits("minutes")


class _EqliscsiVolumeSnapshotPolicyTimeFrequency_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyTimeFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_EqliscsiVolumeSnapshotPolicyTimeFrequency_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyTimeFrequency_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyTimeFrequency = _EqliscsiVolumeSnapshotPolicyTimeFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 11),
    _EqliscsiVolumeSnapshotPolicyTimeFrequency_Type()
)
eqliscsiVolumeSnapshotPolicyTimeFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyTimeFrequency.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyTimeFrequency.setUnits("minutes")


class _EqliscsiVolumeSnapshotPolicyStartDate_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyStartDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqliscsiVolumeSnapshotPolicyStartDate_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyStartDate_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyStartDate = _EqliscsiVolumeSnapshotPolicyStartDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 12),
    _EqliscsiVolumeSnapshotPolicyStartDate_Type()
)
eqliscsiVolumeSnapshotPolicyStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyStartDate.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyStartDate.setUnits("days")


class _EqliscsiVolumeSnapshotPolicyEndDate_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyEndDate based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqliscsiVolumeSnapshotPolicyEndDate_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyEndDate_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyEndDate = _EqliscsiVolumeSnapshotPolicyEndDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 13),
    _EqliscsiVolumeSnapshotPolicyEndDate_Type()
)
eqliscsiVolumeSnapshotPolicyEndDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyEndDate.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyEndDate.setUnits("days")
_EqliscsiVolumeSnapshotPolicyWeekMask_Type = Integer32
_EqliscsiVolumeSnapshotPolicyWeekMask_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyWeekMask = _EqliscsiVolumeSnapshotPolicyWeekMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 14),
    _EqliscsiVolumeSnapshotPolicyWeekMask_Type()
)
eqliscsiVolumeSnapshotPolicyWeekMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyWeekMask.setStatus("current")
_EqliscsiVolumeSnapshotPolicyMonthMask_Type = Integer32
_EqliscsiVolumeSnapshotPolicyMonthMask_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyMonthMask = _EqliscsiVolumeSnapshotPolicyMonthMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 15),
    _EqliscsiVolumeSnapshotPolicyMonthMask_Type()
)
eqliscsiVolumeSnapshotPolicyMonthMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyMonthMask.setStatus("current")
_EqliscsiVolumeSnapshotPolicyNextCreate_Type = Counter32
_EqliscsiVolumeSnapshotPolicyNextCreate_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyNextCreate = _EqliscsiVolumeSnapshotPolicyNextCreate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 16),
    _EqliscsiVolumeSnapshotPolicyNextCreate_Type()
)
eqliscsiVolumeSnapshotPolicyNextCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyNextCreate.setStatus("current")


class _EqliscsiVolumeSnapshotPolicyOccurence_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyOccurence based on Integer32"""
    defaultValue = 0


_EqliscsiVolumeSnapshotPolicyOccurence_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyOccurence = _EqliscsiVolumeSnapshotPolicyOccurence_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 17),
    _EqliscsiVolumeSnapshotPolicyOccurence_Type()
)
eqliscsiVolumeSnapshotPolicyOccurence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyOccurence.setStatus("current")
_EqliscsiVolumeSnapshotPolicyReplication_Type = SiteIndexOrZero
_EqliscsiVolumeSnapshotPolicyReplication_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyReplication = _EqliscsiVolumeSnapshotPolicyReplication_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 18),
    _EqliscsiVolumeSnapshotPolicyReplication_Type()
)
eqliscsiVolumeSnapshotPolicyReplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyReplication.setStatus("current")


class _EqliscsiVolumeSnapshotPolicyAdminStatus_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_EqliscsiVolumeSnapshotPolicyAdminStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyAdminStatus_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyAdminStatus = _EqliscsiVolumeSnapshotPolicyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 5, 1, 19),
    _EqliscsiVolumeSnapshotPolicyAdminStatus_Type()
)
eqliscsiVolumeSnapshotPolicyAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyAdminStatus.setStatus("current")
_EqliscsiVolumeACLTable_Object = MibTable
eqliscsiVolumeACLTable = _EqliscsiVolumeACLTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeACLTable.setStatus("current")
_EqliscsiVolumeACLEntry_Object = MibTableRow
eqliscsiVolumeACLEntry = _EqliscsiVolumeACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1)
)
eqliscsiVolumeACLEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeACLIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeACLEntry.setStatus("current")
_EqliscsiVolumeACLIndex_Type = Integer32
_EqliscsiVolumeACLIndex_Object = MibTableColumn
eqliscsiVolumeACLIndex = _EqliscsiVolumeACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 1),
    _EqliscsiVolumeACLIndex_Type()
)
eqliscsiVolumeACLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLIndex.setStatus("current")


class _EqliscsiVolumeACLInitiatorName_Type(UTFString):
    """Custom type eqliscsiVolumeACLInitiatorName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiVolumeACLInitiatorName_Type.__name__ = "UTFString"
_EqliscsiVolumeACLInitiatorName_Object = MibTableColumn
eqliscsiVolumeACLInitiatorName = _EqliscsiVolumeACLInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 2),
    _EqliscsiVolumeACLInitiatorName_Type()
)
eqliscsiVolumeACLInitiatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorName.setStatus("current")
_EqliscsiVolumeACLInitiatorIpAddress_Type = IpAddress
_EqliscsiVolumeACLInitiatorIpAddress_Object = MibTableColumn
eqliscsiVolumeACLInitiatorIpAddress = _EqliscsiVolumeACLInitiatorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 3),
    _EqliscsiVolumeACLInitiatorIpAddress_Type()
)
eqliscsiVolumeACLInitiatorIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorIpAddress.setStatus("current")


class _EqliscsiVolumeACLInitiatorAuthenticationMethod_Type(Integer32):
    """Custom type eqliscsiVolumeACLInitiatorAuthenticationMethod based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("chap-local", 2),
          ("chap5", 1),
          ("none", 4),
          ("srp-local", 3))
    )


_EqliscsiVolumeACLInitiatorAuthenticationMethod_Type.__name__ = "Integer32"
_EqliscsiVolumeACLInitiatorAuthenticationMethod_Object = MibTableColumn
eqliscsiVolumeACLInitiatorAuthenticationMethod = _EqliscsiVolumeACLInitiatorAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 4),
    _EqliscsiVolumeACLInitiatorAuthenticationMethod_Type()
)
eqliscsiVolumeACLInitiatorAuthenticationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorAuthenticationMethod.setStatus("current")


class _EqliscsiVolumeACLInitiatorUserName_Type(UTFString):
    """Custom type eqliscsiVolumeACLInitiatorUserName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiVolumeACLInitiatorUserName_Type.__name__ = "UTFString"
_EqliscsiVolumeACLInitiatorUserName_Object = MibTableColumn
eqliscsiVolumeACLInitiatorUserName = _EqliscsiVolumeACLInitiatorUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 5),
    _EqliscsiVolumeACLInitiatorUserName_Type()
)
eqliscsiVolumeACLInitiatorUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorUserName.setStatus("deprecated")


class _EqliscsiVolumeACLInitiatorUserPassword_Type(OctetString):
    """Custom type eqliscsiVolumeACLInitiatorUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiVolumeACLInitiatorUserPassword_Type.__name__ = "OctetString"
_EqliscsiVolumeACLInitiatorUserPassword_Object = MibTableColumn
eqliscsiVolumeACLInitiatorUserPassword = _EqliscsiVolumeACLInitiatorUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 6),
    _EqliscsiVolumeACLInitiatorUserPassword_Type()
)
eqliscsiVolumeACLInitiatorUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorUserPassword.setStatus("current")


class _EqliscsiVolumeACLTargetType_Type(ACLAppliesTo):
    """Custom type eqliscsiVolumeACLTargetType based on ACLAppliesTo"""


_EqliscsiVolumeACLTargetType_Object = MibTableColumn
eqliscsiVolumeACLTargetType = _EqliscsiVolumeACLTargetType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 7),
    _EqliscsiVolumeACLTargetType_Type()
)
eqliscsiVolumeACLTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLTargetType.setStatus("current")
_EqliscsiVolumeACLRowStatus_Type = RowStatus
_EqliscsiVolumeACLRowStatus_Object = MibTableColumn
eqliscsiVolumeACLRowStatus = _EqliscsiVolumeACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 8),
    _EqliscsiVolumeACLRowStatus_Type()
)
eqliscsiVolumeACLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLRowStatus.setStatus("current")


class _EqliscsiVolumeACLInitiatorUserName2_Type(UTFString):
    """Custom type eqliscsiVolumeACLInitiatorUserName2 based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqliscsiVolumeACLInitiatorUserName2_Type.__name__ = "UTFString"
_EqliscsiVolumeACLInitiatorUserName2_Object = MibTableColumn
eqliscsiVolumeACLInitiatorUserName2 = _EqliscsiVolumeACLInitiatorUserName2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 9),
    _EqliscsiVolumeACLInitiatorUserName2_Type()
)
eqliscsiVolumeACLInitiatorUserName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorUserName2.setStatus("current")


class _EqliscsiVolumeACLAuthType_Type(Integer32):
    """Custom type eqliscsiVolumeACLAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eql-psg-chap", 2),
          ("mpio", 5),
          ("ms-vds", 4),
          ("none", 1),
          ("not-set", 0),
          ("radius", 3))
    )


_EqliscsiVolumeACLAuthType_Type.__name__ = "Integer32"
_EqliscsiVolumeACLAuthType_Object = MibTableColumn
eqliscsiVolumeACLAuthType = _EqliscsiVolumeACLAuthType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 10),
    _EqliscsiVolumeACLAuthType_Type()
)
eqliscsiVolumeACLAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLAuthType.setStatus("current")
_EqliscsiVolumeACLInitiatorIpWildcard_Type = IpAddress
_EqliscsiVolumeACLInitiatorIpWildcard_Object = MibTableColumn
eqliscsiVolumeACLInitiatorIpWildcard = _EqliscsiVolumeACLInitiatorIpWildcard_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 11),
    _EqliscsiVolumeACLInitiatorIpWildcard_Type()
)
eqliscsiVolumeACLInitiatorIpWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorIpWildcard.setStatus("current")
_EqliscsiVolumeACLInitiatorInetAddressType_Type = InetAddressType
_EqliscsiVolumeACLInitiatorInetAddressType_Object = MibTableColumn
eqliscsiVolumeACLInitiatorInetAddressType = _EqliscsiVolumeACLInitiatorInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 12),
    _EqliscsiVolumeACLInitiatorInetAddressType_Type()
)
eqliscsiVolumeACLInitiatorInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorInetAddressType.setStatus("current")
_EqliscsiVolumeACLInitiatorInetAddress_Type = InetAddress
_EqliscsiVolumeACLInitiatorInetAddress_Object = MibTableColumn
eqliscsiVolumeACLInitiatorInetAddress = _EqliscsiVolumeACLInitiatorInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 13),
    _EqliscsiVolumeACLInitiatorInetAddress_Type()
)
eqliscsiVolumeACLInitiatorInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorInetAddress.setStatus("current")
_EqliscsiVolumeACLInitiatorInetWildcardType_Type = InetAddressType
_EqliscsiVolumeACLInitiatorInetWildcardType_Object = MibTableColumn
eqliscsiVolumeACLInitiatorInetWildcardType = _EqliscsiVolumeACLInitiatorInetWildcardType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 14),
    _EqliscsiVolumeACLInitiatorInetWildcardType_Type()
)
eqliscsiVolumeACLInitiatorInetWildcardType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorInetWildcardType.setStatus("current")
_EqliscsiVolumeACLInitiatorInetWildcard_Type = InetAddress
_EqliscsiVolumeACLInitiatorInetWildcard_Object = MibTableColumn
eqliscsiVolumeACLInitiatorInetWildcard = _EqliscsiVolumeACLInitiatorInetWildcard_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 6, 1, 15),
    _EqliscsiVolumeACLInitiatorInetWildcard_Type()
)
eqliscsiVolumeACLInitiatorInetWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeACLInitiatorInetWildcard.setStatus("current")
_EqliscsiVolumeStatusTable_Object = MibTable
eqliscsiVolumeStatusTable = _EqliscsiVolumeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusTable.setStatus("current")
_EqliscsiVolumeStatusEntry_Object = MibTableRow
eqliscsiVolumeStatusEntry = _EqliscsiVolumeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusEntry.setStatus("current")


class _EqliscsiVolumeStatusPsvId_Type(OctetString):
    """Custom type eqliscsiVolumeStatusPsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiVolumeStatusPsvId_Type.__name__ = "OctetString"
_EqliscsiVolumeStatusPsvId_Object = MibTableColumn
eqliscsiVolumeStatusPsvId = _EqliscsiVolumeStatusPsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 1),
    _EqliscsiVolumeStatusPsvId_Type()
)
eqliscsiVolumeStatusPsvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusPsvId.setStatus("current")
_EqliscsiVolumeStatusReservedSpace_Type = Integer32
_EqliscsiVolumeStatusReservedSpace_Object = MibTableColumn
eqliscsiVolumeStatusReservedSpace = _EqliscsiVolumeStatusReservedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 2),
    _EqliscsiVolumeStatusReservedSpace_Type()
)
eqliscsiVolumeStatusReservedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusReservedSpace.setStatus("current")


class _EqliscsiVolumeStatusReservedSpaceAvail_Type(Integer32):
    """Custom type eqliscsiVolumeStatusReservedSpaceAvail based on Integer32"""
    defaultValue = 0


_EqliscsiVolumeStatusReservedSpaceAvail_Object = MibTableColumn
eqliscsiVolumeStatusReservedSpaceAvail = _EqliscsiVolumeStatusReservedSpaceAvail_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 3),
    _EqliscsiVolumeStatusReservedSpaceAvail_Type()
)
eqliscsiVolumeStatusReservedSpaceAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusReservedSpaceAvail.setStatus("current")
_EqliscsiVolumeStatusActualMemberCount_Type = Integer32
_EqliscsiVolumeStatusActualMemberCount_Object = MibTableColumn
eqliscsiVolumeStatusActualMemberCount = _EqliscsiVolumeStatusActualMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 4),
    _EqliscsiVolumeStatusActualMemberCount_Type()
)
eqliscsiVolumeStatusActualMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusActualMemberCount.setStatus("current")
_EqliscsiVolumeStatusNumSnapshots_Type = Integer32
_EqliscsiVolumeStatusNumSnapshots_Object = MibTableColumn
eqliscsiVolumeStatusNumSnapshots = _EqliscsiVolumeStatusNumSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 5),
    _EqliscsiVolumeStatusNumSnapshots_Type()
)
eqliscsiVolumeStatusNumSnapshots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusNumSnapshots.setStatus("current")
_EqliscsiVolumeStatusCreationTime_Type = DateAndTime
_EqliscsiVolumeStatusCreationTime_Object = MibTableColumn
eqliscsiVolumeStatusCreationTime = _EqliscsiVolumeStatusCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 6),
    _EqliscsiVolumeStatusCreationTime_Type()
)
eqliscsiVolumeStatusCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusCreationTime.setStatus("current")


class _EqliscsiVolumeStatusAvailable_Type(Integer32):
    """Custom type eqliscsiVolumeStatusAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("membersMissing", 2))
    )


_EqliscsiVolumeStatusAvailable_Type.__name__ = "Integer32"
_EqliscsiVolumeStatusAvailable_Object = MibTableColumn
eqliscsiVolumeStatusAvailable = _EqliscsiVolumeStatusAvailable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 7),
    _EqliscsiVolumeStatusAvailable_Type()
)
eqliscsiVolumeStatusAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusAvailable.setStatus("current")


class _EqliscsiVolumeStatusOperStatus_Type(Integer32):
    """Custom type eqliscsiVolumeStatusOperStatus based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("available-no-new-connections", 10),
          ("not-available", 2),
          ("not-available-due-to-internal-error", 11),
          ("not-available-due-to-lost-cached-blocks", 5),
          ("not-available-due-to-members-offline", 4),
          ("not-available-due-to-missing-pages", 8),
          ("not-available-due-to-nospace-for-auto-grow", 7),
          ("not-available-due-to-snap-reserve-met", 3),
          ("not-available-due-to-syncrep", 9),
          ("not-available-due-to-thin-max-growth-met", 6))
    )


_EqliscsiVolumeStatusOperStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeStatusOperStatus_Object = MibTableColumn
eqliscsiVolumeStatusOperStatus = _EqliscsiVolumeStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 8),
    _EqliscsiVolumeStatusOperStatus_Type()
)
eqliscsiVolumeStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusOperStatus.setStatus("current")
_EqliscsiVolumeStatusConnections_Type = Integer32
_EqliscsiVolumeStatusConnections_Object = MibTableColumn
eqliscsiVolumeStatusConnections = _EqliscsiVolumeStatusConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 9),
    _EqliscsiVolumeStatusConnections_Type()
)
eqliscsiVolumeStatusConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusConnections.setStatus("current")


class _EqliscsiVolumeStatusLostRaidBlocksAction_Type(Integer32):
    """Custom type eqliscsiVolumeStatusLostRaidBlocksAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mark-valid", 1),
          ("zero-out", 2))
    )


_EqliscsiVolumeStatusLostRaidBlocksAction_Type.__name__ = "Integer32"
_EqliscsiVolumeStatusLostRaidBlocksAction_Object = MibTableColumn
eqliscsiVolumeStatusLostRaidBlocksAction = _EqliscsiVolumeStatusLostRaidBlocksAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 10),
    _EqliscsiVolumeStatusLostRaidBlocksAction_Type()
)
eqliscsiVolumeStatusLostRaidBlocksAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusLostRaidBlocksAction.setStatus("current")


class _EqliscsiVolumeStatusNumReplicas_Type(Unsigned32):
    """Custom type eqliscsiVolumeStatusNumReplicas based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolumeStatusNumReplicas_Object = MibTableColumn
eqliscsiVolumeStatusNumReplicas = _EqliscsiVolumeStatusNumReplicas_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 11),
    _EqliscsiVolumeStatusNumReplicas_Type()
)
eqliscsiVolumeStatusNumReplicas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusNumReplicas.setStatus("current")


class _EqliscsiVolumeStatusReplReserveSpace_Type(Unsigned32):
    """Custom type eqliscsiVolumeStatusReplReserveSpace based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolumeStatusReplReserveSpace_Object = MibTableColumn
eqliscsiVolumeStatusReplReserveSpace = _EqliscsiVolumeStatusReplReserveSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 12),
    _EqliscsiVolumeStatusReplReserveSpace_Type()
)
eqliscsiVolumeStatusReplReserveSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusReplReserveSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusReplReserveSpace.setUnits("MB")
_EqliscsiVolumeStatusAllocatedSpace_Type = Unsigned32
_EqliscsiVolumeStatusAllocatedSpace_Object = MibTableColumn
eqliscsiVolumeStatusAllocatedSpace = _EqliscsiVolumeStatusAllocatedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 13),
    _EqliscsiVolumeStatusAllocatedSpace_Type()
)
eqliscsiVolumeStatusAllocatedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusAllocatedSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusAllocatedSpace.setUnits("MB")
_EqliscsiVolumeStatusReplResvInUse_Type = Unsigned32
_EqliscsiVolumeStatusReplResvInUse_Object = MibTableColumn
eqliscsiVolumeStatusReplResvInUse = _EqliscsiVolumeStatusReplResvInUse_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 14),
    _EqliscsiVolumeStatusReplResvInUse_Type()
)
eqliscsiVolumeStatusReplResvInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusReplResvInUse.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusReplResvInUse.setUnits("MB")
_EqliscsiVolumeStatusReplTxData_Type = Unsigned32
_EqliscsiVolumeStatusReplTxData_Object = MibTableColumn
eqliscsiVolumeStatusReplTxData = _EqliscsiVolumeStatusReplTxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 15),
    _EqliscsiVolumeStatusReplTxData_Type()
)
eqliscsiVolumeStatusReplTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusReplTxData.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusReplTxData.setUnits("MB")
_EqliscsiVolumeStatusNumOnlineSnaps_Type = Unsigned32
_EqliscsiVolumeStatusNumOnlineSnaps_Object = MibTableColumn
eqliscsiVolumeStatusNumOnlineSnaps = _EqliscsiVolumeStatusNumOnlineSnaps_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 16),
    _EqliscsiVolumeStatusNumOnlineSnaps_Type()
)
eqliscsiVolumeStatusNumOnlineSnaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusNumOnlineSnaps.setStatus("current")
_EqliscsiVolumeStatusPagesSharedWithParent_Type = Unsigned32
_EqliscsiVolumeStatusPagesSharedWithParent_Object = MibTableColumn
eqliscsiVolumeStatusPagesSharedWithParent = _EqliscsiVolumeStatusPagesSharedWithParent_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 17),
    _EqliscsiVolumeStatusPagesSharedWithParent_Type()
)
eqliscsiVolumeStatusPagesSharedWithParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusPagesSharedWithParent.setStatus("current")
_EqliscsiVolumeStatusExternalConnections_Type = Integer32
_EqliscsiVolumeStatusExternalConnections_Object = MibTableColumn
eqliscsiVolumeStatusExternalConnections = _EqliscsiVolumeStatusExternalConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 18),
    _EqliscsiVolumeStatusExternalConnections_Type()
)
eqliscsiVolumeStatusExternalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusExternalConnections.setStatus("current")
_EqliscsiVolumeStatusSpaceBorrowing_Type = Integer32
_EqliscsiVolumeStatusSpaceBorrowing_Object = MibTableColumn
eqliscsiVolumeStatusSpaceBorrowing = _EqliscsiVolumeStatusSpaceBorrowing_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 19),
    _EqliscsiVolumeStatusSpaceBorrowing_Type()
)
eqliscsiVolumeStatusSpaceBorrowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusSpaceBorrowing.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusSpaceBorrowing.setUnits("MB")


class _EqliscsiVolumeStatusBorrow_Type(Integer32):
    """Custom type eqliscsiVolumeStatusBorrow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unavailable", 0))
    )


_EqliscsiVolumeStatusBorrow_Type.__name__ = "Integer32"
_EqliscsiVolumeStatusBorrow_Object = MibTableColumn
eqliscsiVolumeStatusBorrow = _EqliscsiVolumeStatusBorrow_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 7, 1, 20),
    _EqliscsiVolumeStatusBorrow_Type()
)
eqliscsiVolumeStatusBorrow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatusBorrow.setStatus("current")
_EqliscsiSnapshotStatusTable_Object = MibTable
eqliscsiSnapshotStatusTable = _EqliscsiSnapshotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 8)
)
if mibBuilder.loadTexts:
    eqliscsiSnapshotStatusTable.setStatus("current")
_EqliscsiSnapshotStatusEntry_Object = MibTableRow
eqliscsiSnapshotStatusEntry = _EqliscsiSnapshotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 8, 1)
)
if mibBuilder.loadTexts:
    eqliscsiSnapshotStatusEntry.setStatus("current")


class _EqliscsiSnapshotStatusOperStatus_Type(Integer32):
    """Custom type eqliscsiSnapshotStatusOperStatus based on Integer32"""
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
        *(("available", 1),
          ("not-available", 2),
          ("not-available-due-to-lost-cached-blocks", 5),
          ("not-available-due-to-members-offline", 4),
          ("not-available-due-to-missing-pages", 8),
          ("not-available-due-to-nospace-for-auto-grow", 7),
          ("not-available-due-to-snap-reserve-met", 3),
          ("not-available-due-to-thin-max-growth-met", 6))
    )


_EqliscsiSnapshotStatusOperStatus_Type.__name__ = "Integer32"
_EqliscsiSnapshotStatusOperStatus_Object = MibTableColumn
eqliscsiSnapshotStatusOperStatus = _EqliscsiSnapshotStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 8, 1, 1),
    _EqliscsiSnapshotStatusOperStatus_Type()
)
eqliscsiSnapshotStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotStatusOperStatus.setStatus("current")
_EqliscsiSnapshotStatusConnections_Type = Integer32
_EqliscsiSnapshotStatusConnections_Object = MibTableColumn
eqliscsiSnapshotStatusConnections = _EqliscsiSnapshotStatusConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 8, 1, 2),
    _EqliscsiSnapshotStatusConnections_Type()
)
eqliscsiSnapshotStatusConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapshotStatusConnections.setStatus("current")


class _EqliscsiSnapshotStatusLostRaidBlocksAction_Type(Integer32):
    """Custom type eqliscsiSnapshotStatusLostRaidBlocksAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mark-valid", 1),
          ("zero-out", 2))
    )


_EqliscsiSnapshotStatusLostRaidBlocksAction_Type.__name__ = "Integer32"
_EqliscsiSnapshotStatusLostRaidBlocksAction_Object = MibTableColumn
eqliscsiSnapshotStatusLostRaidBlocksAction = _EqliscsiSnapshotStatusLostRaidBlocksAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 8, 1, 10),
    _EqliscsiSnapshotStatusLostRaidBlocksAction_Type()
)
eqliscsiSnapshotStatusLostRaidBlocksAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiSnapshotStatusLostRaidBlocksAction.setStatus("current")
_EqliscsiAdminGroup_ObjectIdentity = ObjectIdentity
eqliscsiAdminGroup = _EqliscsiAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 9)
)
_EqliscsiLocalMemberId_Type = Unsigned32
_EqliscsiLocalMemberId_Object = MibScalar
eqliscsiLocalMemberId = _EqliscsiLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 9, 1),
    _EqliscsiLocalMemberId_Type()
)
eqliscsiLocalMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiLocalMemberId.setStatus("current")
_EqliscsiLocalMemberIdLow_Type = Unsigned32
_EqliscsiLocalMemberIdLow_Object = MibScalar
eqliscsiLocalMemberIdLow = _EqliscsiLocalMemberIdLow_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 9, 2),
    _EqliscsiLocalMemberIdLow_Type()
)
eqliscsiLocalMemberIdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiLocalMemberIdLow.setStatus("current")
_EqliscsiLocalMemberIdHigh_Type = Unsigned32
_EqliscsiLocalMemberIdHigh_Object = MibScalar
eqliscsiLocalMemberIdHigh = _EqliscsiLocalMemberIdHigh_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 9, 3),
    _EqliscsiLocalMemberIdHigh_Type()
)
eqliscsiLocalMemberIdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiLocalMemberIdHigh.setStatus("current")
_EqliscsiVolumeAdminGroup_ObjectIdentity = ObjectIdentity
eqliscsiVolumeAdminGroup = _EqliscsiVolumeAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10)
)
_EqliscsiLastVolumeIndex_Type = Unsigned32
_EqliscsiLastVolumeIndex_Object = MibScalar
eqliscsiLastVolumeIndex = _EqliscsiLastVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 1),
    _EqliscsiLastVolumeIndex_Type()
)
eqliscsiLastVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiLastVolumeIndex.setStatus("current")
_EqliscsiVolumeIndexLow_Type = Unsigned32
_EqliscsiVolumeIndexLow_Object = MibScalar
eqliscsiVolumeIndexLow = _EqliscsiVolumeIndexLow_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 2),
    _EqliscsiVolumeIndexLow_Type()
)
eqliscsiVolumeIndexLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeIndexLow.setStatus("current")
_EqliscsiVolumeIndexHigh_Type = Unsigned32
_EqliscsiVolumeIndexHigh_Object = MibScalar
eqliscsiVolumeIndexHigh = _EqliscsiVolumeIndexHigh_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 3),
    _EqliscsiVolumeIndexHigh_Type()
)
eqliscsiVolumeIndexHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeIndexHigh.setStatus("current")
_EqliscsiVolumeLowPsvId0_Type = Unsigned32
_EqliscsiVolumeLowPsvId0_Object = MibScalar
eqliscsiVolumeLowPsvId0 = _EqliscsiVolumeLowPsvId0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 4),
    _EqliscsiVolumeLowPsvId0_Type()
)
eqliscsiVolumeLowPsvId0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeLowPsvId0.setStatus("current")
_EqliscsiVolumeLowPsvId1_Type = Unsigned32
_EqliscsiVolumeLowPsvId1_Object = MibScalar
eqliscsiVolumeLowPsvId1 = _EqliscsiVolumeLowPsvId1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 5),
    _EqliscsiVolumeLowPsvId1_Type()
)
eqliscsiVolumeLowPsvId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeLowPsvId1.setStatus("current")
_EqliscsiVolumeLowPsvId2_Type = Unsigned32
_EqliscsiVolumeLowPsvId2_Object = MibScalar
eqliscsiVolumeLowPsvId2 = _EqliscsiVolumeLowPsvId2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 6),
    _EqliscsiVolumeLowPsvId2_Type()
)
eqliscsiVolumeLowPsvId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeLowPsvId2.setStatus("current")
_EqliscsiVolumeLowPsvId3_Type = Unsigned32
_EqliscsiVolumeLowPsvId3_Object = MibScalar
eqliscsiVolumeLowPsvId3 = _EqliscsiVolumeLowPsvId3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 7),
    _EqliscsiVolumeLowPsvId3_Type()
)
eqliscsiVolumeLowPsvId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeLowPsvId3.setStatus("current")
_EqliscsiVolumeHighPsvId0_Type = Unsigned32
_EqliscsiVolumeHighPsvId0_Object = MibScalar
eqliscsiVolumeHighPsvId0 = _EqliscsiVolumeHighPsvId0_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 8),
    _EqliscsiVolumeHighPsvId0_Type()
)
eqliscsiVolumeHighPsvId0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeHighPsvId0.setStatus("current")
_EqliscsiVolumeHighPsvId1_Type = Unsigned32
_EqliscsiVolumeHighPsvId1_Object = MibScalar
eqliscsiVolumeHighPsvId1 = _EqliscsiVolumeHighPsvId1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 9),
    _EqliscsiVolumeHighPsvId1_Type()
)
eqliscsiVolumeHighPsvId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeHighPsvId1.setStatus("current")
_EqliscsiVolumeHighPsvId2_Type = Unsigned32
_EqliscsiVolumeHighPsvId2_Object = MibScalar
eqliscsiVolumeHighPsvId2 = _EqliscsiVolumeHighPsvId2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 10),
    _EqliscsiVolumeHighPsvId2_Type()
)
eqliscsiVolumeHighPsvId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeHighPsvId2.setStatus("current")
_EqliscsiVolumeHighPsvId3_Type = Unsigned32
_EqliscsiVolumeHighPsvId3_Object = MibScalar
eqliscsiVolumeHighPsvId3 = _EqliscsiVolumeHighPsvId3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 10, 11),
    _EqliscsiVolumeHighPsvId3_Type()
)
eqliscsiVolumeHighPsvId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeHighPsvId3.setStatus("current")
_EqliscsiSnapshotAdminGroup_ObjectIdentity = ObjectIdentity
eqliscsiSnapshotAdminGroup = _EqliscsiSnapshotAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 11)
)
_EqliscsiLastSnapshotIndex_Type = Unsigned32
_EqliscsiLastSnapshotIndex_Object = MibScalar
eqliscsiLastSnapshotIndex = _EqliscsiLastSnapshotIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 11, 1),
    _EqliscsiLastSnapshotIndex_Type()
)
eqliscsiLastSnapshotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiLastSnapshotIndex.setStatus("current")
_EqliscsiVolumeAuthAttributesTable_Object = MibTable
eqliscsiVolumeAuthAttributesTable = _EqliscsiVolumeAuthAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 12)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeAuthAttributesTable.setStatus("current")
_EqliscsiVolumeAuthAttributesEntry_Object = MibTableRow
eqliscsiVolumeAuthAttributesEntry = _EqliscsiVolumeAuthAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 12, 1)
)
eqliscsiVolumeAuthAttributesEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeAuthAttributesEntry.setStatus("current")
_EqliscsiVolumeAuthRowStatus_Type = RowStatus
_EqliscsiVolumeAuthRowStatus_Object = MibTableColumn
eqliscsiVolumeAuthRowStatus = _EqliscsiVolumeAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 12, 1, 1),
    _EqliscsiVolumeAuthRowStatus_Type()
)
eqliscsiVolumeAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeAuthRowStatus.setStatus("current")
_EqliscsiVolumeAuthIdentity_Type = RowPointer
_EqliscsiVolumeAuthIdentity_Object = MibTableColumn
eqliscsiVolumeAuthIdentity = _EqliscsiVolumeAuthIdentity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 12, 1, 2),
    _EqliscsiVolumeAuthIdentity_Type()
)
eqliscsiVolumeAuthIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeAuthIdentity.setStatus("current")
_EqliscsiVolumeBindingTable_Object = MibTable
eqliscsiVolumeBindingTable = _EqliscsiVolumeBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 13)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeBindingTable.setStatus("current")
_EqliscsiVolumeBindingEntry_Object = MibTableRow
eqliscsiVolumeBindingEntry = _EqliscsiVolumeBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 13, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeBindingEntry.setStatus("current")
_EqliscsiVolumeBindingRowStatus_Type = RowStatus
_EqliscsiVolumeBindingRowStatus_Object = MibTableColumn
eqliscsiVolumeBindingRowStatus = _EqliscsiVolumeBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 13, 1, 1),
    _EqliscsiVolumeBindingRowStatus_Type()
)
eqliscsiVolumeBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeBindingRowStatus.setStatus("current")
_EqliscsiVolumeReplSiteTable_Object = MibTable
eqliscsiVolumeReplSiteTable = _EqliscsiVolumeReplSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteTable.setStatus("current")
_EqliscsiVolumeReplSiteEntry_Object = MibTableRow
eqliscsiVolumeReplSiteEntry = _EqliscsiVolumeReplSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1)
)
eqliscsiVolumeReplSiteEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteEntry.setStatus("current")
_EqliscsiVolumeReplSiteIndex_Type = SiteIndex
_EqliscsiVolumeReplSiteIndex_Object = MibTableColumn
eqliscsiVolumeReplSiteIndex = _EqliscsiVolumeReplSiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 1),
    _EqliscsiVolumeReplSiteIndex_Type()
)
eqliscsiVolumeReplSiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteIndex.setStatus("current")
_EqliscsiVolumeReplSiteRowStatus_Type = RowStatus
_EqliscsiVolumeReplSiteRowStatus_Object = MibTableColumn
eqliscsiVolumeReplSiteRowStatus = _EqliscsiVolumeReplSiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 2),
    _EqliscsiVolumeReplSiteRowStatus_Type()
)
eqliscsiVolumeReplSiteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteRowStatus.setStatus("current")


class _EqliscsiVolumeReplSiteName_Type(DisplayString):
    """Custom type eqliscsiVolumeReplSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqliscsiVolumeReplSiteName_Type.__name__ = "DisplayString"
_EqliscsiVolumeReplSiteName_Object = MibTableColumn
eqliscsiVolumeReplSiteName = _EqliscsiVolumeReplSiteName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 3),
    _EqliscsiVolumeReplSiteName_Type()
)
eqliscsiVolumeReplSiteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteName.setStatus("current")
_EqliscsiVolumeReplSiteIpAddr_Type = IpAddress
_EqliscsiVolumeReplSiteIpAddr_Object = MibTableColumn
eqliscsiVolumeReplSiteIpAddr = _EqliscsiVolumeReplSiteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 4),
    _EqliscsiVolumeReplSiteIpAddr_Type()
)
eqliscsiVolumeReplSiteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteIpAddr.setStatus("current")
_EqliscsiVolumeReplSiteControlCredentials_Type = RowPointer
_EqliscsiVolumeReplSiteControlCredentials_Object = MibTableColumn
eqliscsiVolumeReplSiteControlCredentials = _EqliscsiVolumeReplSiteControlCredentials_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 5),
    _EqliscsiVolumeReplSiteControlCredentials_Type()
)
eqliscsiVolumeReplSiteControlCredentials.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteControlCredentials.setStatus("current")


class _EqliscsiVolumeReplControlTargetIscsiName_Type(OctetString):
    """Custom type eqliscsiVolumeReplControlTargetIscsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiVolumeReplControlTargetIscsiName_Type.__name__ = "OctetString"
_EqliscsiVolumeReplControlTargetIscsiName_Object = MibTableColumn
eqliscsiVolumeReplControlTargetIscsiName = _EqliscsiVolumeReplControlTargetIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 6),
    _EqliscsiVolumeReplControlTargetIscsiName_Type()
)
eqliscsiVolumeReplControlTargetIscsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplControlTargetIscsiName.setStatus("current")
_EqliscsiVolumeReplSiteSNMPContext_Type = DisplayString
_EqliscsiVolumeReplSiteSNMPContext_Object = MibTableColumn
eqliscsiVolumeReplSiteSNMPContext = _EqliscsiVolumeReplSiteSNMPContext_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 7),
    _EqliscsiVolumeReplSiteSNMPContext_Type()
)
eqliscsiVolumeReplSiteSNMPContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteSNMPContext.setStatus("current")


class _EqliscsiVolumeReplSiteContact_Type(DisplayString):
    """Custom type eqliscsiVolumeReplSiteContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiVolumeReplSiteContact_Type.__name__ = "DisplayString"
_EqliscsiVolumeReplSiteContact_Object = MibTableColumn
eqliscsiVolumeReplSiteContact = _EqliscsiVolumeReplSiteContact_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 8),
    _EqliscsiVolumeReplSiteContact_Type()
)
eqliscsiVolumeReplSiteContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteContact.setStatus("current")


class _EqliscsiVolumeReplSiteEmail_Type(DisplayString):
    """Custom type eqliscsiVolumeReplSiteEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiVolumeReplSiteEmail_Type.__name__ = "DisplayString"
_EqliscsiVolumeReplSiteEmail_Object = MibTableColumn
eqliscsiVolumeReplSiteEmail = _EqliscsiVolumeReplSiteEmail_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 9),
    _EqliscsiVolumeReplSiteEmail_Type()
)
eqliscsiVolumeReplSiteEmail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteEmail.setStatus("current")


class _EqliscsiVolumeReplSitePhone_Type(DisplayString):
    """Custom type eqliscsiVolumeReplSitePhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqliscsiVolumeReplSitePhone_Type.__name__ = "DisplayString"
_EqliscsiVolumeReplSitePhone_Object = MibTableColumn
eqliscsiVolumeReplSitePhone = _EqliscsiVolumeReplSitePhone_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 10),
    _EqliscsiVolumeReplSitePhone_Type()
)
eqliscsiVolumeReplSitePhone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSitePhone.setStatus("current")


class _EqliscsiVolumeReplSiteMobile_Type(DisplayString):
    """Custom type eqliscsiVolumeReplSiteMobile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqliscsiVolumeReplSiteMobile_Type.__name__ = "DisplayString"
_EqliscsiVolumeReplSiteMobile_Object = MibTableColumn
eqliscsiVolumeReplSiteMobile = _EqliscsiVolumeReplSiteMobile_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 11),
    _EqliscsiVolumeReplSiteMobile_Type()
)
eqliscsiVolumeReplSiteMobile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteMobile.setStatus("current")


class _EqliscsiVolumeReplSiteDescription_Type(UTFString):
    """Custom type eqliscsiVolumeReplSiteDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiVolumeReplSiteDescription_Type.__name__ = "UTFString"
_EqliscsiVolumeReplSiteDescription_Object = MibTableColumn
eqliscsiVolumeReplSiteDescription = _EqliscsiVolumeReplSiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 12),
    _EqliscsiVolumeReplSiteDescription_Type()
)
eqliscsiVolumeReplSiteDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteDescription.setStatus("current")
_EqliscsiVolumeReplSiteSpaceAllocated_Type = Unsigned32
_EqliscsiVolumeReplSiteSpaceAllocated_Object = MibTableColumn
eqliscsiVolumeReplSiteSpaceAllocated = _EqliscsiVolumeReplSiteSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 13),
    _EqliscsiVolumeReplSiteSpaceAllocated_Type()
)
eqliscsiVolumeReplSiteSpaceAllocated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteSpaceAllocated.setStatus("current")
_EqliscsiVolumeReplSiteSpaceUsed_Type = Unsigned32
_EqliscsiVolumeReplSiteSpaceUsed_Object = MibTableColumn
eqliscsiVolumeReplSiteSpaceUsed = _EqliscsiVolumeReplSiteSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 14),
    _EqliscsiVolumeReplSiteSpaceUsed_Type()
)
eqliscsiVolumeReplSiteSpaceUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteSpaceUsed.setStatus("current")


class _EqliscsiVolumeReplControlChannelStatus_Type(Integer32):
    """Custom type eqliscsiVolumeReplControlChannelStatus based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("authentication-failed", 6),
          ("control-credentials-not-configured", 5),
          ("control-target-not-configured", 3),
          ("control-target-not-present-at-replica-site", 4),
          ("generic-error", 2),
          ("ipaddress-not-configured", 1),
          ("logged-in", 7),
          ("logged-out", 8),
          ("paused", 9))
    )


_EqliscsiVolumeReplControlChannelStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeReplControlChannelStatus_Object = MibTableColumn
eqliscsiVolumeReplControlChannelStatus = _EqliscsiVolumeReplControlChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 15),
    _EqliscsiVolumeReplControlChannelStatus_Type()
)
eqliscsiVolumeReplControlChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplControlChannelStatus.setStatus("current")


class _EqliscsiVolumeReplSiteAdminStatus_Type(Integer32):
    """Custom type eqliscsiVolumeReplSiteAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("paused", 2))
    )


_EqliscsiVolumeReplSiteAdminStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeReplSiteAdminStatus_Object = MibTableColumn
eqliscsiVolumeReplSiteAdminStatus = _EqliscsiVolumeReplSiteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 16),
    _EqliscsiVolumeReplSiteAdminStatus_Type()
)
eqliscsiVolumeReplSiteAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteAdminStatus.setStatus("current")
_EqliscsiVolumeReplSiteTotalNumSnapshots_Type = Unsigned32
_EqliscsiVolumeReplSiteTotalNumSnapshots_Object = MibTableColumn
eqliscsiVolumeReplSiteTotalNumSnapshots = _EqliscsiVolumeReplSiteTotalNumSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 17),
    _EqliscsiVolumeReplSiteTotalNumSnapshots_Type()
)
eqliscsiVolumeReplSiteTotalNumSnapshots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteTotalNumSnapshots.setStatus("current")
_EqliscsiVolumeReplSiteSpaceSubscribed_Type = Unsigned32
_EqliscsiVolumeReplSiteSpaceSubscribed_Object = MibTableColumn
eqliscsiVolumeReplSiteSpaceSubscribed = _EqliscsiVolumeReplSiteSpaceSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 18),
    _EqliscsiVolumeReplSiteSpaceSubscribed_Type()
)
eqliscsiVolumeReplSiteSpaceSubscribed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteSpaceSubscribed.setStatus("current")
_EqliscsiVolumeReplSiteInetAddrType_Type = InetAddressType
_EqliscsiVolumeReplSiteInetAddrType_Object = MibTableColumn
eqliscsiVolumeReplSiteInetAddrType = _EqliscsiVolumeReplSiteInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 19),
    _EqliscsiVolumeReplSiteInetAddrType_Type()
)
eqliscsiVolumeReplSiteInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteInetAddrType.setStatus("current")
_EqliscsiVolumeReplSiteInetAddr_Type = InetAddress
_EqliscsiVolumeReplSiteInetAddr_Object = MibTableColumn
eqliscsiVolumeReplSiteInetAddr = _EqliscsiVolumeReplSiteInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 20),
    _EqliscsiVolumeReplSiteInetAddr_Type()
)
eqliscsiVolumeReplSiteInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteInetAddr.setStatus("current")
_EqliscsiVolumeReplSiteNASPartnershipId_Type = Unsigned32
_EqliscsiVolumeReplSiteNASPartnershipId_Object = MibTableColumn
eqliscsiVolumeReplSiteNASPartnershipId = _EqliscsiVolumeReplSiteNASPartnershipId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 21),
    _EqliscsiVolumeReplSiteNASPartnershipId_Type()
)
eqliscsiVolumeReplSiteNASPartnershipId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteNASPartnershipId.setStatus("current")


class _EqliscsiVolumeReplSiteBlockState_Type(StatusEnabledDefault):
    """Custom type eqliscsiVolumeReplSiteBlockState based on StatusEnabledDefault"""


_EqliscsiVolumeReplSiteBlockState_Object = MibTableColumn
eqliscsiVolumeReplSiteBlockState = _EqliscsiVolumeReplSiteBlockState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 22),
    _EqliscsiVolumeReplSiteBlockState_Type()
)
eqliscsiVolumeReplSiteBlockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteBlockState.setStatus("current")


class _EqliscsiVolumeReplSiteNASState_Type(StatusDisabledDefault):
    """Custom type eqliscsiVolumeReplSiteNASState based on StatusDisabledDefault"""


_EqliscsiVolumeReplSiteNASState_Object = MibTableColumn
eqliscsiVolumeReplSiteNASState = _EqliscsiVolumeReplSiteNASState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 23),
    _EqliscsiVolumeReplSiteNASState_Type()
)
eqliscsiVolumeReplSiteNASState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteNASState.setStatus("current")


class _EqliscsiVolumeReplSiteType_Type(Integer32):
    """Custom type eqliscsiVolumeReplSiteType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("normal", 0))
    )


_EqliscsiVolumeReplSiteType_Type.__name__ = "Integer32"
_EqliscsiVolumeReplSiteType_Object = MibTableColumn
eqliscsiVolumeReplSiteType = _EqliscsiVolumeReplSiteType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 14, 1, 24),
    _EqliscsiVolumeReplSiteType_Type()
)
eqliscsiVolumeReplSiteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteType.setStatus("current")
_EqliscsiVolumeReplicationTable_Object = MibTable
eqliscsiVolumeReplicationTable = _EqliscsiVolumeReplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeReplicationTable.setStatus("current")
_EqliscsiVolumeReplicationEntry_Object = MibTableRow
eqliscsiVolumeReplicationEntry = _EqliscsiVolumeReplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1)
)
eqliscsiVolumeReplicationEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeReplicationEntry.setStatus("current")
_EqliscsiVolumeReplRowStatus_Type = RowStatus
_EqliscsiVolumeReplRowStatus_Object = MibTableColumn
eqliscsiVolumeReplRowStatus = _EqliscsiVolumeReplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 1),
    _EqliscsiVolumeReplRowStatus_Type()
)
eqliscsiVolumeReplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplRowStatus.setStatus("current")


class _EqliscsiVolumeReplAdminStatus_Type(Integer32):
    """Custom type eqliscsiVolumeReplAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("paused", 3))
    )


_EqliscsiVolumeReplAdminStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeReplAdminStatus_Object = MibTableColumn
eqliscsiVolumeReplAdminStatus = _EqliscsiVolumeReplAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 2),
    _EqliscsiVolumeReplAdminStatus_Type()
)
eqliscsiVolumeReplAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplAdminStatus.setStatus("current")


class _EqliscsiVolumeReplRemoteIscsiName_Type(OctetString):
    """Custom type eqliscsiVolumeReplRemoteIscsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiVolumeReplRemoteIscsiName_Type.__name__ = "OctetString"
_EqliscsiVolumeReplRemoteIscsiName_Object = MibTableColumn
eqliscsiVolumeReplRemoteIscsiName = _EqliscsiVolumeReplRemoteIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 3),
    _EqliscsiVolumeReplRemoteIscsiName_Type()
)
eqliscsiVolumeReplRemoteIscsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplRemoteIscsiName.setStatus("current")


class _EqliscsiVolumeReplRemoteIscsiPort_Type(Unsigned32):
    """Custom type eqliscsiVolumeReplRemoteIscsiPort based on Unsigned32"""
    defaultValue = 3260


_EqliscsiVolumeReplRemoteIscsiPort_Object = MibTableColumn
eqliscsiVolumeReplRemoteIscsiPort = _EqliscsiVolumeReplRemoteIscsiPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 4),
    _EqliscsiVolumeReplRemoteIscsiPort_Type()
)
eqliscsiVolumeReplRemoteIscsiPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplRemoteIscsiPort.setStatus("current")


class _EqliscsiVolumeReplRemotePsvId_Type(OctetString):
    """Custom type eqliscsiVolumeReplRemotePsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiVolumeReplRemotePsvId_Type.__name__ = "OctetString"
_EqliscsiVolumeReplRemotePsvId_Object = MibTableColumn
eqliscsiVolumeReplRemotePsvId = _EqliscsiVolumeReplRemotePsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 5),
    _EqliscsiVolumeReplRemotePsvId_Type()
)
eqliscsiVolumeReplRemotePsvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplRemotePsvId.setStatus("current")


class _EqliscsiVolumeReplDiscardPolicy_Type(Integer32):
    """Custom type eqliscsiVolumeReplDiscardPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("overRun", 1))
    )


_EqliscsiVolumeReplDiscardPolicy_Type.__name__ = "Integer32"
_EqliscsiVolumeReplDiscardPolicy_Object = MibTableColumn
eqliscsiVolumeReplDiscardPolicy = _EqliscsiVolumeReplDiscardPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 6),
    _EqliscsiVolumeReplDiscardPolicy_Type()
)
eqliscsiVolumeReplDiscardPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplDiscardPolicy.setStatus("current")


class _EqliscsiVolumeReplReserve_Type(Unsigned32):
    """Custom type eqliscsiVolumeReplReserve based on Unsigned32"""
    defaultValue = 200


_EqliscsiVolumeReplReserve_Object = MibTableColumn
eqliscsiVolumeReplReserve = _EqliscsiVolumeReplReserve_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 7),
    _EqliscsiVolumeReplReserve_Type()
)
eqliscsiVolumeReplReserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplReserve.setStatus("current")


class _EqliscsiVolumeReplDeletionPolicy_Type(Integer32):
    """Custom type eqliscsiVolumeReplDeletionPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-only", 1),
          ("remote", 2))
    )


_EqliscsiVolumeReplDeletionPolicy_Type.__name__ = "Integer32"
_EqliscsiVolumeReplDeletionPolicy_Object = MibTableColumn
eqliscsiVolumeReplDeletionPolicy = _EqliscsiVolumeReplDeletionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 8),
    _EqliscsiVolumeReplDeletionPolicy_Type()
)
eqliscsiVolumeReplDeletionPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplDeletionPolicy.setStatus("current")


class _EqliscsiVolumeReplNumReplicas_Type(Unsigned32):
    """Custom type eqliscsiVolumeReplNumReplicas based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolumeReplNumReplicas_Object = MibTableColumn
eqliscsiVolumeReplNumReplicas = _EqliscsiVolumeReplNumReplicas_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 9),
    _EqliscsiVolumeReplNumReplicas_Type()
)
eqliscsiVolumeReplNumReplicas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplNumReplicas.setStatus("current")


class _EqliscsiVolumeReplPrimaryReserve_Type(Unsigned32):
    """Custom type eqliscsiVolumeReplPrimaryReserve based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_EqliscsiVolumeReplPrimaryReserve_Type.__name__ = "Unsigned32"
_EqliscsiVolumeReplPrimaryReserve_Object = MibTableColumn
eqliscsiVolumeReplPrimaryReserve = _EqliscsiVolumeReplPrimaryReserve_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 10),
    _EqliscsiVolumeReplPrimaryReserve_Type()
)
eqliscsiVolumeReplPrimaryReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplPrimaryReserve.setStatus("current")


class _EqliscsiVolumeReplPrimaryBorrow_Type(TruthValue):
    """Custom type eqliscsiVolumeReplPrimaryBorrow based on TruthValue"""


_EqliscsiVolumeReplPrimaryBorrow_Object = MibTableColumn
eqliscsiVolumeReplPrimaryBorrow = _EqliscsiVolumeReplPrimaryBorrow_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 11),
    _EqliscsiVolumeReplPrimaryBorrow_Type()
)
eqliscsiVolumeReplPrimaryBorrow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplPrimaryBorrow.setStatus("current")


class _EqliscsiVolumeReplManualReplStatus_Type(Integer32):
    """Custom type eqliscsiVolumeReplManualReplStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("done", 3),
          ("enabled", 1))
    )


_EqliscsiVolumeReplManualReplStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeReplManualReplStatus_Object = MibTableColumn
eqliscsiVolumeReplManualReplStatus = _EqliscsiVolumeReplManualReplStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 12),
    _EqliscsiVolumeReplManualReplStatus_Type()
)
eqliscsiVolumeReplManualReplStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplManualReplStatus.setStatus("current")
_EqliscsiVolumeReplCurLwMark_Type = Integer32
_EqliscsiVolumeReplCurLwMark_Object = MibTableColumn
eqliscsiVolumeReplCurLwMark = _EqliscsiVolumeReplCurLwMark_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 13),
    _EqliscsiVolumeReplCurLwMark_Type()
)
eqliscsiVolumeReplCurLwMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplCurLwMark.setStatus("current")
_EqliscsiVolumeReplLwMark_Type = Integer32
_EqliscsiVolumeReplLwMark_Object = MibTableColumn
eqliscsiVolumeReplLwMark = _EqliscsiVolumeReplLwMark_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 14),
    _EqliscsiVolumeReplLwMark_Type()
)
eqliscsiVolumeReplLwMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplLwMark.setStatus("current")
_EqliscsiVolumeReplSize_Type = Integer32
_EqliscsiVolumeReplSize_Object = MibTableColumn
eqliscsiVolumeReplSize = _EqliscsiVolumeReplSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 15),
    _EqliscsiVolumeReplSize_Type()
)
eqliscsiVolumeReplSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSize.setStatus("current")
_EqliscsiVolumeReplThinProvision_Type = TruthValue
_EqliscsiVolumeReplThinProvision_Object = MibTableColumn
eqliscsiVolumeReplThinProvision = _EqliscsiVolumeReplThinProvision_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 16),
    _EqliscsiVolumeReplThinProvision_Type()
)
eqliscsiVolumeReplThinProvision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplThinProvision.setStatus("current")
_EqliscsiVolumeReplMinThinReserve_Type = Unsigned32
_EqliscsiVolumeReplMinThinReserve_Object = MibTableColumn
eqliscsiVolumeReplMinThinReserve = _EqliscsiVolumeReplMinThinReserve_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 17),
    _EqliscsiVolumeReplMinThinReserve_Type()
)
eqliscsiVolumeReplMinThinReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplMinThinReserve.setStatus("current")
_EqliscsiVolumeReplThinWarnPercentage_Type = Unsigned32
_EqliscsiVolumeReplThinWarnPercentage_Object = MibTableColumn
eqliscsiVolumeReplThinWarnPercentage = _EqliscsiVolumeReplThinWarnPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 18),
    _EqliscsiVolumeReplThinWarnPercentage_Type()
)
eqliscsiVolumeReplThinWarnPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplThinWarnPercentage.setStatus("current")
_EqliscsiVolumeReplThinMaxGrowPercentage_Type = Unsigned32
_EqliscsiVolumeReplThinMaxGrowPercentage_Object = MibTableColumn
eqliscsiVolumeReplThinMaxGrowPercentage = _EqliscsiVolumeReplThinMaxGrowPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 19),
    _EqliscsiVolumeReplThinMaxGrowPercentage_Type()
)
eqliscsiVolumeReplThinMaxGrowPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplThinMaxGrowPercentage.setStatus("current")
_EqliscsiVolumeReplDynamicThinReserve_Type = Unsigned32
_EqliscsiVolumeReplDynamicThinReserve_Object = MibTableColumn
eqliscsiVolumeReplDynamicThinReserve = _EqliscsiVolumeReplDynamicThinReserve_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 20),
    _EqliscsiVolumeReplDynamicThinReserve_Type()
)
eqliscsiVolumeReplDynamicThinReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplDynamicThinReserve.setStatus("current")


class _EqliscsiVolumeReplFailBackMode_Type(Integer32):
    """Custom type eqliscsiVolumeReplFailBackMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("normal", 0))
    )


_EqliscsiVolumeReplFailBackMode_Type.__name__ = "Integer32"
_EqliscsiVolumeReplFailBackMode_Object = MibTableColumn
eqliscsiVolumeReplFailBackMode = _EqliscsiVolumeReplFailBackMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 21),
    _EqliscsiVolumeReplFailBackMode_Type()
)
eqliscsiVolumeReplFailBackMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplFailBackMode.setStatus("current")


class _EqliscsiVolumeReplPromoteSeqNum_Type(Counter64):
    """Custom type eqliscsiVolumeReplPromoteSeqNum based on Counter64"""
    defaultValue = 0


_EqliscsiVolumeReplPromoteSeqNum_Object = MibTableColumn
eqliscsiVolumeReplPromoteSeqNum = _EqliscsiVolumeReplPromoteSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 22),
    _EqliscsiVolumeReplPromoteSeqNum_Type()
)
eqliscsiVolumeReplPromoteSeqNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplPromoteSeqNum.setStatus("current")


class _EqliscsiVolumeReplTemplateReplicated_Type(TruthValue):
    """Custom type eqliscsiVolumeReplTemplateReplicated based on TruthValue"""


_EqliscsiVolumeReplTemplateReplicated_Object = MibTableColumn
eqliscsiVolumeReplTemplateReplicated = _EqliscsiVolumeReplTemplateReplicated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 23),
    _EqliscsiVolumeReplTemplateReplicated_Type()
)
eqliscsiVolumeReplTemplateReplicated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplTemplateReplicated.setStatus("current")


class _EqliscsiVolumeReplSyncAdminStatus_Type(Integer32):
    """Custom type eqliscsiVolumeReplSyncAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EqliscsiVolumeReplSyncAdminStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeReplSyncAdminStatus_Object = MibTableColumn
eqliscsiVolumeReplSyncAdminStatus = _EqliscsiVolumeReplSyncAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 24),
    _EqliscsiVolumeReplSyncAdminStatus_Type()
)
eqliscsiVolumeReplSyncAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSyncAdminStatus.setStatus("current")


class _EqliscsiVolumeReplSyncOperStatus_Type(Integer32):
    """Custom type eqliscsiVolumeReplSyncOperStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("first-sync-done", 2),
          ("waiting-for-first-sync", 1))
    )


_EqliscsiVolumeReplSyncOperStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeReplSyncOperStatus_Object = MibTableColumn
eqliscsiVolumeReplSyncOperStatus = _EqliscsiVolumeReplSyncOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 25),
    _EqliscsiVolumeReplSyncOperStatus_Type()
)
eqliscsiVolumeReplSyncOperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSyncOperStatus.setStatus("current")


class _EqliscsiVolumeReplThinClone_Type(TruthValue):
    """Custom type eqliscsiVolumeReplThinClone based on TruthValue"""


_EqliscsiVolumeReplThinClone_Object = MibTableColumn
eqliscsiVolumeReplThinClone = _EqliscsiVolumeReplThinClone_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 15, 1, 26),
    _EqliscsiVolumeReplThinClone_Type()
)
eqliscsiVolumeReplThinClone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplThinClone.setStatus("current")
_EqliscsiVolumeReplicationStatusTable_Object = MibTable
eqliscsiVolumeReplicationStatusTable = _EqliscsiVolumeReplicationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 16)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeReplicationStatusTable.setStatus("current")
_EqliscsiVolumeReplicationStatusEntry_Object = MibTableRow
eqliscsiVolumeReplicationStatusEntry = _EqliscsiVolumeReplicationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 16, 1)
)
eqliscsiVolumeReplicationStatusEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeReplicationStatusEntry.setStatus("current")


class _EqliscsiVolumeReplOperStatus_Type(Integer32):
    """Custom type eqliscsiVolumeReplOperStatus based on Integer32"""
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
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("authFailure", 5),
          ("cancelling", 15),
          ("completed", 6),
          ("disabled", 1),
          ("failed", 11),
          ("farEndDown", 4),
          ("inProgress", 2),
          ("manualDataTransferInProgress", 17),
          ("nomoresnapallowed", 13),
          ("partnerPausedLocal", 10),
          ("paused", 7),
          ("pendingDataTransfer", 16),
          ("remoteDisallowDowngradesNotSet", 18),
          ("remotePartnerNeedsUpgrade", 19),
          ("remotePaused", 9),
          ("remoteReplReserveInvalid", 14),
          ("remoteReplReserveLow", 12),
          ("remoteResizeFailed", 8),
          ("waiting", 3))
    )


_EqliscsiVolumeReplOperStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeReplOperStatus_Object = MibTableColumn
eqliscsiVolumeReplOperStatus = _EqliscsiVolumeReplOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 16, 1, 1),
    _EqliscsiVolumeReplOperStatus_Type()
)
eqliscsiVolumeReplOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplOperStatus.setStatus("current")
_EqliscsiVolumeReplMBRemaining_Type = Counter64
_EqliscsiVolumeReplMBRemaining_Object = MibTableColumn
eqliscsiVolumeReplMBRemaining = _EqliscsiVolumeReplMBRemaining_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 16, 1, 2),
    _EqliscsiVolumeReplMBRemaining_Type()
)
eqliscsiVolumeReplMBRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplMBRemaining.setStatus("current")
_EqliscsiVolumeReplMBCompleted_Type = Counter64
_EqliscsiVolumeReplMBCompleted_Object = MibTableColumn
eqliscsiVolumeReplMBCompleted = _EqliscsiVolumeReplMBCompleted_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 16, 1, 3),
    _EqliscsiVolumeReplMBCompleted_Type()
)
eqliscsiVolumeReplMBCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplMBCompleted.setStatus("current")
_EqliscsiVolumeReplCurrentSnapshot_Type = RowPointer
_EqliscsiVolumeReplCurrentSnapshot_Object = MibTableColumn
eqliscsiVolumeReplCurrentSnapshot = _EqliscsiVolumeReplCurrentSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 16, 1, 5),
    _EqliscsiVolumeReplCurrentSnapshot_Type()
)
eqliscsiVolumeReplCurrentSnapshot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplCurrentSnapshot.setStatus("current")
_EqliscsiVolumeReplCancel_Type = TruthValue
_EqliscsiVolumeReplCancel_Object = MibTableColumn
eqliscsiVolumeReplCancel = _EqliscsiVolumeReplCancel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 16, 1, 6),
    _EqliscsiVolumeReplCancel_Type()
)
eqliscsiVolumeReplCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplCancel.setStatus("current")
_EqliscsiVolumeRemoteReplReserveIncrNeeded_Type = Unsigned32
_EqliscsiVolumeRemoteReplReserveIncrNeeded_Object = MibTableColumn
eqliscsiVolumeRemoteReplReserveIncrNeeded = _EqliscsiVolumeRemoteReplReserveIncrNeeded_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 16, 1, 7),
    _EqliscsiVolumeRemoteReplReserveIncrNeeded_Type()
)
eqliscsiVolumeRemoteReplReserveIncrNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeRemoteReplReserveIncrNeeded.setStatus("current")
_EqliscsiVolumeReplFailbackSnap_Type = RowPointer
_EqliscsiVolumeReplFailbackSnap_Object = MibTableColumn
eqliscsiVolumeReplFailbackSnap = _EqliscsiVolumeReplFailbackSnap_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 16, 1, 8),
    _EqliscsiVolumeReplFailbackSnap_Type()
)
eqliscsiVolumeReplFailbackSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplFailbackSnap.setStatus("current")
_EqliscsiRemoteReplicaTable_Object = MibTable
eqliscsiRemoteReplicaTable = _EqliscsiRemoteReplicaTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17)
)
if mibBuilder.loadTexts:
    eqliscsiRemoteReplicaTable.setStatus("current")
_EqliscsiRemoteReplicaEntry_Object = MibTableRow
eqliscsiRemoteReplicaEntry = _EqliscsiRemoteReplicaEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1)
)
eqliscsiRemoteReplicaEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiRemoteVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiRemoteSnapIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiRemoteReplicaEntry.setStatus("current")
_EqliscsiRemoteVolumeIndex_Type = Unsigned32
_EqliscsiRemoteVolumeIndex_Object = MibTableColumn
eqliscsiRemoteVolumeIndex = _EqliscsiRemoteVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1, 1),
    _EqliscsiRemoteVolumeIndex_Type()
)
eqliscsiRemoteVolumeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiRemoteVolumeIndex.setStatus("current")
_EqliscsiRemoteSnapIndex_Type = Unsigned32
_EqliscsiRemoteSnapIndex_Object = MibTableColumn
eqliscsiRemoteSnapIndex = _EqliscsiRemoteSnapIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1, 2),
    _EqliscsiRemoteSnapIndex_Type()
)
eqliscsiRemoteSnapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiRemoteSnapIndex.setStatus("current")


class _EqliscsiRemoteReplName_Type(OctetString):
    """Custom type eqliscsiRemoteReplName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiRemoteReplName_Type.__name__ = "OctetString"
_EqliscsiRemoteReplName_Object = MibTableColumn
eqliscsiRemoteReplName = _EqliscsiRemoteReplName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1, 3),
    _EqliscsiRemoteReplName_Type()
)
eqliscsiRemoteReplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplName.setStatus("current")


class _EqliscsiRemoteReplISCSIName_Type(OctetString):
    """Custom type eqliscsiRemoteReplISCSIName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiRemoteReplISCSIName_Type.__name__ = "OctetString"
_EqliscsiRemoteReplISCSIName_Object = MibTableColumn
eqliscsiRemoteReplISCSIName = _EqliscsiRemoteReplISCSIName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1, 4),
    _EqliscsiRemoteReplISCSIName_Type()
)
eqliscsiRemoteReplISCSIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplISCSIName.setStatus("current")


class _EqliscsiRemoteReplPsvId_Type(OctetString):
    """Custom type eqliscsiRemoteReplPsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiRemoteReplPsvId_Type.__name__ = "OctetString"
_EqliscsiRemoteReplPsvId_Object = MibTableColumn
eqliscsiRemoteReplPsvId = _EqliscsiRemoteReplPsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1, 5),
    _EqliscsiRemoteReplPsvId_Type()
)
eqliscsiRemoteReplPsvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplPsvId.setStatus("current")


class _EqliscsiRemoteReplAdminStatus_Type(Integer32):
    """Custom type eqliscsiRemoteReplAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("in-progress", 2),
          ("incomplete", 3),
          ("none", 0))
    )


_EqliscsiRemoteReplAdminStatus_Type.__name__ = "Integer32"
_EqliscsiRemoteReplAdminStatus_Object = MibTableColumn
eqliscsiRemoteReplAdminStatus = _EqliscsiRemoteReplAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1, 6),
    _EqliscsiRemoteReplAdminStatus_Type()
)
eqliscsiRemoteReplAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplAdminStatus.setStatus("current")
_EqliscsiRemoteReplTimeStamp_Type = Counter32
_EqliscsiRemoteReplTimeStamp_Object = MibTableColumn
eqliscsiRemoteReplTimeStamp = _EqliscsiRemoteReplTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1, 7),
    _EqliscsiRemoteReplTimeStamp_Type()
)
eqliscsiRemoteReplTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplTimeStamp.setStatus("current")
_EqliscsiRemoteReplSnapColIndex_Type = Unsigned32
_EqliscsiRemoteReplSnapColIndex_Object = MibTableColumn
eqliscsiRemoteReplSnapColIndex = _EqliscsiRemoteReplSnapColIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1, 8),
    _EqliscsiRemoteReplSnapColIndex_Type()
)
eqliscsiRemoteReplSnapColIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplSnapColIndex.setStatus("current")


class _EqliscsiRemoteReplScheduleIndex_Type(Unsigned32):
    """Custom type eqliscsiRemoteReplScheduleIndex based on Unsigned32"""
    defaultValue = 0


_EqliscsiRemoteReplScheduleIndex_Object = MibTableColumn
eqliscsiRemoteReplScheduleIndex = _EqliscsiRemoteReplScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1, 9),
    _EqliscsiRemoteReplScheduleIndex_Type()
)
eqliscsiRemoteReplScheduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplScheduleIndex.setStatus("current")
_EqliscsiRemoteReplLocalMemberId_Type = Unsigned32
_EqliscsiRemoteReplLocalMemberId_Object = MibTableColumn
eqliscsiRemoteReplLocalMemberId = _EqliscsiRemoteReplLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 17, 1, 10),
    _EqliscsiRemoteReplLocalMemberId_Type()
)
eqliscsiRemoteReplLocalMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplLocalMemberId.setStatus("current")
_EqliscsiReplicaSetTable_Object = MibTable
eqliscsiReplicaSetTable = _EqliscsiReplicaSetTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18)
)
if mibBuilder.loadTexts:
    eqliscsiReplicaSetTable.setStatus("current")
_EqliscsiReplicaSetEntry_Object = MibTableRow
eqliscsiReplicaSetEntry = _EqliscsiReplicaSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1)
)
eqliscsiReplicaSetEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiReplicaSetEntry.setStatus("current")


class _EqliscsiReplicaSetPrimaryIscsiName_Type(OctetString):
    """Custom type eqliscsiReplicaSetPrimaryIscsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiReplicaSetPrimaryIscsiName_Type.__name__ = "OctetString"
_EqliscsiReplicaSetPrimaryIscsiName_Object = MibTableColumn
eqliscsiReplicaSetPrimaryIscsiName = _EqliscsiReplicaSetPrimaryIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 1),
    _EqliscsiReplicaSetPrimaryIscsiName_Type()
)
eqliscsiReplicaSetPrimaryIscsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetPrimaryIscsiName.setStatus("current")


class _EqliscsiReplicaSetReserve_Type(Unsigned32):
    """Custom type eqliscsiReplicaSetReserve based on Unsigned32"""
    defaultValue = 100


_EqliscsiReplicaSetReserve_Object = MibTableColumn
eqliscsiReplicaSetReserve = _EqliscsiReplicaSetReserve_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 2),
    _EqliscsiReplicaSetReserve_Type()
)
eqliscsiReplicaSetReserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetReserve.setStatus("current")
_EqliscsiReplicaSetSite_Type = SiteIndex
_EqliscsiReplicaSetSite_Object = MibTableColumn
eqliscsiReplicaSetSite = _EqliscsiReplicaSetSite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 3),
    _EqliscsiReplicaSetSite_Type()
)
eqliscsiReplicaSetSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetSite.setStatus("current")


class _EqliscsiReplicaSetAdminStatus_Type(Integer32):
    """Custom type eqliscsiReplicaSetAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("started", 2),
          ("stopped", 1))
    )


_EqliscsiReplicaSetAdminStatus_Type.__name__ = "Integer32"
_EqliscsiReplicaSetAdminStatus_Object = MibTableColumn
eqliscsiReplicaSetAdminStatus = _EqliscsiReplicaSetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 4),
    _EqliscsiReplicaSetAdminStatus_Type()
)
eqliscsiReplicaSetAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetAdminStatus.setStatus("current")


class _EqliscsiReplicaSetPromotePolicy_Type(Integer32):
    """Custom type eqliscsiReplicaSetPromotePolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default-iscsi-name", 1),
          ("primary-iscsi-name", 2))
    )


_EqliscsiReplicaSetPromotePolicy_Type.__name__ = "Integer32"
_EqliscsiReplicaSetPromotePolicy_Object = MibTableColumn
eqliscsiReplicaSetPromotePolicy = _EqliscsiReplicaSetPromotePolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 5),
    _EqliscsiReplicaSetPromotePolicy_Type()
)
eqliscsiReplicaSetPromotePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetPromotePolicy.setStatus("current")


class _EqliscsiReplicaSetManualReplStatus_Type(Integer32):
    """Custom type eqliscsiReplicaSetManualReplStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("done", 3),
          ("enabled", 1))
    )


_EqliscsiReplicaSetManualReplStatus_Type.__name__ = "Integer32"
_EqliscsiReplicaSetManualReplStatus_Object = MibTableColumn
eqliscsiReplicaSetManualReplStatus = _EqliscsiReplicaSetManualReplStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 12),
    _EqliscsiReplicaSetManualReplStatus_Type()
)
eqliscsiReplicaSetManualReplStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetManualReplStatus.setStatus("current")


class _EqliscsiReplicaSetFailBackMode_Type(Integer32):
    """Custom type eqliscsiReplicaSetFailBackMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("normal", 0))
    )


_EqliscsiReplicaSetFailBackMode_Type.__name__ = "Integer32"
_EqliscsiReplicaSetFailBackMode_Object = MibTableColumn
eqliscsiReplicaSetFailBackMode = _EqliscsiReplicaSetFailBackMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 13),
    _EqliscsiReplicaSetFailBackMode_Type()
)
eqliscsiReplicaSetFailBackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetFailBackMode.setStatus("current")


class _EqliscsiReplicaSetType_Type(Integer32):
    """Custom type eqliscsiReplicaSetType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail-back", 1),
          ("regular", 0))
    )


_EqliscsiReplicaSetType_Type.__name__ = "Integer32"
_EqliscsiReplicaSetType_Object = MibTableColumn
eqliscsiReplicaSetType = _EqliscsiReplicaSetType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 14),
    _EqliscsiReplicaSetType_Type()
)
eqliscsiReplicaSetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetType.setStatus("current")


class _EqliscsiReplicaSetAccess_Type(Integer32):
    """Custom type eqliscsiReplicaSetAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-access", 0),
          ("read-only", 1))
    )


_EqliscsiReplicaSetAccess_Type.__name__ = "Integer32"
_EqliscsiReplicaSetAccess_Object = MibTableColumn
eqliscsiReplicaSetAccess = _EqliscsiReplicaSetAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 15),
    _EqliscsiReplicaSetAccess_Type()
)
eqliscsiReplicaSetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetAccess.setStatus("current")
_EqliscsiReplicaSetFailbackReserve_Type = Unsigned32
_EqliscsiReplicaSetFailbackReserve_Object = MibTableColumn
eqliscsiReplicaSetFailbackReserve = _EqliscsiReplicaSetFailbackReserve_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 16),
    _EqliscsiReplicaSetFailbackReserve_Type()
)
eqliscsiReplicaSetFailbackReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetFailbackReserve.setStatus("current")


class _EqliscsiReplicaSetLSRPsvId_Type(OctetString):
    """Custom type eqliscsiReplicaSetLSRPsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiReplicaSetLSRPsvId_Type.__name__ = "OctetString"
_EqliscsiReplicaSetLSRPsvId_Object = MibTableColumn
eqliscsiReplicaSetLSRPsvId = _EqliscsiReplicaSetLSRPsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 17),
    _EqliscsiReplicaSetLSRPsvId_Type()
)
eqliscsiReplicaSetLSRPsvId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetLSRPsvId.setStatus("current")
_EqliscsiReplicaSetOrigSize_Type = Unsigned32
_EqliscsiReplicaSetOrigSize_Object = MibTableColumn
eqliscsiReplicaSetOrigSize = _EqliscsiReplicaSetOrigSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 18),
    _EqliscsiReplicaSetOrigSize_Type()
)
eqliscsiReplicaSetOrigSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetOrigSize.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetOrigSize.setUnits("MB")
_EqliscsiReplicaSetPrimaryMemberId_Type = Unsigned32
_EqliscsiReplicaSetPrimaryMemberId_Object = MibTableColumn
eqliscsiReplicaSetPrimaryMemberId = _EqliscsiReplicaSetPrimaryMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 19),
    _EqliscsiReplicaSetPrimaryMemberId_Type()
)
eqliscsiReplicaSetPrimaryMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetPrimaryMemberId.setStatus("current")
_EqliscsiReplicaSetPrimaryVolumeIndex_Type = Unsigned32
_EqliscsiReplicaSetPrimaryVolumeIndex_Object = MibTableColumn
eqliscsiReplicaSetPrimaryVolumeIndex = _EqliscsiReplicaSetPrimaryVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 20),
    _EqliscsiReplicaSetPrimaryVolumeIndex_Type()
)
eqliscsiReplicaSetPrimaryVolumeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetPrimaryVolumeIndex.setStatus("current")
_EqliscsiReplicaSetPrimarySite_Type = Unsigned32
_EqliscsiReplicaSetPrimarySite_Object = MibTableColumn
eqliscsiReplicaSetPrimarySite = _EqliscsiReplicaSetPrimarySite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 21),
    _EqliscsiReplicaSetPrimarySite_Type()
)
eqliscsiReplicaSetPrimarySite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetPrimarySite.setStatus("current")


class _EqliscsiReplicaSetTemplateReplicated_Type(TruthValue):
    """Custom type eqliscsiReplicaSetTemplateReplicated based on TruthValue"""


_EqliscsiReplicaSetTemplateReplicated_Object = MibTableColumn
eqliscsiReplicaSetTemplateReplicated = _EqliscsiReplicaSetTemplateReplicated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 22),
    _EqliscsiReplicaSetTemplateReplicated_Type()
)
eqliscsiReplicaSetTemplateReplicated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetTemplateReplicated.setStatus("current")


class _EqliscsiReplicaSetSyncAdminStatus_Type(Integer32):
    """Custom type eqliscsiReplicaSetSyncAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EqliscsiReplicaSetSyncAdminStatus_Type.__name__ = "Integer32"
_EqliscsiReplicaSetSyncAdminStatus_Object = MibTableColumn
eqliscsiReplicaSetSyncAdminStatus = _EqliscsiReplicaSetSyncAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 23),
    _EqliscsiReplicaSetSyncAdminStatus_Type()
)
eqliscsiReplicaSetSyncAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetSyncAdminStatus.setStatus("current")


class _EqliscsiReplicaSetThinClone_Type(TruthValue):
    """Custom type eqliscsiReplicaSetThinClone based on TruthValue"""


_EqliscsiReplicaSetThinClone_Object = MibTableColumn
eqliscsiReplicaSetThinClone = _EqliscsiReplicaSetThinClone_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 24),
    _EqliscsiReplicaSetThinClone_Type()
)
eqliscsiReplicaSetThinClone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetThinClone.setStatus("current")


class _EqliscsiReplicaSetRemotePsvId_Type(OctetString):
    """Custom type eqliscsiReplicaSetRemotePsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiReplicaSetRemotePsvId_Type.__name__ = "OctetString"
_EqliscsiReplicaSetRemotePsvId_Object = MibTableColumn
eqliscsiReplicaSetRemotePsvId = _EqliscsiReplicaSetRemotePsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 18, 1, 25),
    _EqliscsiReplicaSetRemotePsvId_Type()
)
eqliscsiReplicaSetRemotePsvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetRemotePsvId.setStatus("current")
_EqliscsiReplicaSetStatusTable_Object = MibTable
eqliscsiReplicaSetStatusTable = _EqliscsiReplicaSetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 19)
)
if mibBuilder.loadTexts:
    eqliscsiReplicaSetStatusTable.setStatus("current")
_EqliscsiReplicaSetStatusEntry_Object = MibTableRow
eqliscsiReplicaSetStatusEntry = _EqliscsiReplicaSetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 19, 1)
)
eqliscsiReplicaSetStatusEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiReplicaSetStatusEntry.setStatus("current")


class _EqliscsiReplicaSetOperStatus_Type(Integer32):
    """Custom type eqliscsiReplicaSetOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("authFailure", 5),
          ("farEndDown", 4),
          ("inProgress", 2),
          ("stopped", 1),
          ("waiting", 3))
    )


_EqliscsiReplicaSetOperStatus_Type.__name__ = "Integer32"
_EqliscsiReplicaSetOperStatus_Object = MibTableColumn
eqliscsiReplicaSetOperStatus = _EqliscsiReplicaSetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 19, 1, 1),
    _EqliscsiReplicaSetOperStatus_Type()
)
eqliscsiReplicaSetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetOperStatus.setStatus("current")
_EqliscsiReplicaSetSize_Type = Unsigned32
_EqliscsiReplicaSetSize_Object = MibTableColumn
eqliscsiReplicaSetSize = _EqliscsiReplicaSetSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 19, 1, 2),
    _EqliscsiReplicaSetSize_Type()
)
eqliscsiReplicaSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetSize.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetSize.setUnits("MB")
_EqliscsiReplicantSiteTable_Object = MibTable
eqliscsiReplicantSiteTable = _EqliscsiReplicantSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20)
)
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteTable.setStatus("current")
_EqliscsiReplicantSiteEntry_Object = MibTableRow
eqliscsiReplicantSiteEntry = _EqliscsiReplicantSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1)
)
eqliscsiReplicantSiteEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiReplicantSiteIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteEntry.setStatus("current")
_EqliscsiReplicantSiteIndex_Type = SiteIndex
_EqliscsiReplicantSiteIndex_Object = MibTableColumn
eqliscsiReplicantSiteIndex = _EqliscsiReplicantSiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 1),
    _EqliscsiReplicantSiteIndex_Type()
)
eqliscsiReplicantSiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteIndex.setStatus("current")
_EqliscsiReplicantSiteRowStatus_Type = RowStatus
_EqliscsiReplicantSiteRowStatus_Object = MibTableColumn
eqliscsiReplicantSiteRowStatus = _EqliscsiReplicantSiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 2),
    _EqliscsiReplicantSiteRowStatus_Type()
)
eqliscsiReplicantSiteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteRowStatus.setStatus("current")


class _EqliscsiReplicantSiteName_Type(DisplayString):
    """Custom type eqliscsiReplicantSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqliscsiReplicantSiteName_Type.__name__ = "DisplayString"
_EqliscsiReplicantSiteName_Object = MibTableColumn
eqliscsiReplicantSiteName = _EqliscsiReplicantSiteName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 3),
    _EqliscsiReplicantSiteName_Type()
)
eqliscsiReplicantSiteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteName.setStatus("current")
_EqliscsiReplicantSiteIpAddr_Type = IpAddress
_EqliscsiReplicantSiteIpAddr_Object = MibTableColumn
eqliscsiReplicantSiteIpAddr = _EqliscsiReplicantSiteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 4),
    _EqliscsiReplicantSiteIpAddr_Type()
)
eqliscsiReplicantSiteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteIpAddr.setStatus("current")
_EqliscsiReplicantSiteControlCredentials_Type = RowPointer
_EqliscsiReplicantSiteControlCredentials_Object = MibTableColumn
eqliscsiReplicantSiteControlCredentials = _EqliscsiReplicantSiteControlCredentials_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 5),
    _EqliscsiReplicantSiteControlCredentials_Type()
)
eqliscsiReplicantSiteControlCredentials.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteControlCredentials.setStatus("current")


class _EqliscsiReplicantControlTargetIscsiName_Type(OctetString):
    """Custom type eqliscsiReplicantControlTargetIscsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiReplicantControlTargetIscsiName_Type.__name__ = "OctetString"
_EqliscsiReplicantControlTargetIscsiName_Object = MibTableColumn
eqliscsiReplicantControlTargetIscsiName = _EqliscsiReplicantControlTargetIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 6),
    _EqliscsiReplicantControlTargetIscsiName_Type()
)
eqliscsiReplicantControlTargetIscsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantControlTargetIscsiName.setStatus("current")
_EqliscsiReplicantSiteSNMPContext_Type = DisplayString
_EqliscsiReplicantSiteSNMPContext_Object = MibTableColumn
eqliscsiReplicantSiteSNMPContext = _EqliscsiReplicantSiteSNMPContext_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 7),
    _EqliscsiReplicantSiteSNMPContext_Type()
)
eqliscsiReplicantSiteSNMPContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteSNMPContext.setStatus("current")


class _EqliscsiReplicantSiteContact_Type(DisplayString):
    """Custom type eqliscsiReplicantSiteContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiReplicantSiteContact_Type.__name__ = "DisplayString"
_EqliscsiReplicantSiteContact_Object = MibTableColumn
eqliscsiReplicantSiteContact = _EqliscsiReplicantSiteContact_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 8),
    _EqliscsiReplicantSiteContact_Type()
)
eqliscsiReplicantSiteContact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteContact.setStatus("current")


class _EqliscsiReplicantSiteEmail_Type(DisplayString):
    """Custom type eqliscsiReplicantSiteEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiReplicantSiteEmail_Type.__name__ = "DisplayString"
_EqliscsiReplicantSiteEmail_Object = MibTableColumn
eqliscsiReplicantSiteEmail = _EqliscsiReplicantSiteEmail_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 9),
    _EqliscsiReplicantSiteEmail_Type()
)
eqliscsiReplicantSiteEmail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteEmail.setStatus("current")


class _EqliscsiReplicantSitePhone_Type(DisplayString):
    """Custom type eqliscsiReplicantSitePhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqliscsiReplicantSitePhone_Type.__name__ = "DisplayString"
_EqliscsiReplicantSitePhone_Object = MibTableColumn
eqliscsiReplicantSitePhone = _EqliscsiReplicantSitePhone_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 10),
    _EqliscsiReplicantSitePhone_Type()
)
eqliscsiReplicantSitePhone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSitePhone.setStatus("current")


class _EqliscsiReplicantSiteMobile_Type(DisplayString):
    """Custom type eqliscsiReplicantSiteMobile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqliscsiReplicantSiteMobile_Type.__name__ = "DisplayString"
_EqliscsiReplicantSiteMobile_Object = MibTableColumn
eqliscsiReplicantSiteMobile = _EqliscsiReplicantSiteMobile_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 11),
    _EqliscsiReplicantSiteMobile_Type()
)
eqliscsiReplicantSiteMobile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteMobile.setStatus("current")


class _EqliscsiReplicantSiteDescription_Type(UTFString):
    """Custom type eqliscsiReplicantSiteDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiReplicantSiteDescription_Type.__name__ = "UTFString"
_EqliscsiReplicantSiteDescription_Object = MibTableColumn
eqliscsiReplicantSiteDescription = _EqliscsiReplicantSiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 12),
    _EqliscsiReplicantSiteDescription_Type()
)
eqliscsiReplicantSiteDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteDescription.setStatus("current")
_EqliscsiReplicantSiteSpaceAllocated_Type = Unsigned32
_EqliscsiReplicantSiteSpaceAllocated_Object = MibTableColumn
eqliscsiReplicantSiteSpaceAllocated = _EqliscsiReplicantSiteSpaceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 13),
    _EqliscsiReplicantSiteSpaceAllocated_Type()
)
eqliscsiReplicantSiteSpaceAllocated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteSpaceAllocated.setStatus("current")
_EqliscsiReplicantSiteSpaceUsed_Type = Unsigned32
_EqliscsiReplicantSiteSpaceUsed_Object = MibTableColumn
eqliscsiReplicantSiteSpaceUsed = _EqliscsiReplicantSiteSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 14),
    _EqliscsiReplicantSiteSpaceUsed_Type()
)
eqliscsiReplicantSiteSpaceUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteSpaceUsed.setStatus("current")


class _EqliscsiReplicantSiteControlChannelStatus_Type(Integer32):
    """Custom type eqliscsiReplicantSiteControlChannelStatus based on Integer32"""
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
        *(("authentication-failed", 3),
          ("control-credentials-not-configured", 2),
          ("control-target-not-configured", 1),
          ("logged-in", 4),
          ("logged-out", 5),
          ("paused", 6))
    )


_EqliscsiReplicantSiteControlChannelStatus_Type.__name__ = "Integer32"
_EqliscsiReplicantSiteControlChannelStatus_Object = MibTableColumn
eqliscsiReplicantSiteControlChannelStatus = _EqliscsiReplicantSiteControlChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 15),
    _EqliscsiReplicantSiteControlChannelStatus_Type()
)
eqliscsiReplicantSiteControlChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteControlChannelStatus.setStatus("current")


class _EqliscsiReplicantSiteAdminStatus_Type(Integer32):
    """Custom type eqliscsiReplicantSiteAdminStatus based on Integer32"""
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
        *(("enabled", 1),
          ("nuke", 3),
          ("paused", 2))
    )


_EqliscsiReplicantSiteAdminStatus_Type.__name__ = "Integer32"
_EqliscsiReplicantSiteAdminStatus_Object = MibTableColumn
eqliscsiReplicantSiteAdminStatus = _EqliscsiReplicantSiteAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 16),
    _EqliscsiReplicantSiteAdminStatus_Type()
)
eqliscsiReplicantSiteAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteAdminStatus.setStatus("current")
_EqliscsiReplicantSiteTotalNumSnapshots_Type = Unsigned32
_EqliscsiReplicantSiteTotalNumSnapshots_Object = MibTableColumn
eqliscsiReplicantSiteTotalNumSnapshots = _EqliscsiReplicantSiteTotalNumSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 17),
    _EqliscsiReplicantSiteTotalNumSnapshots_Type()
)
eqliscsiReplicantSiteTotalNumSnapshots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteTotalNumSnapshots.setStatus("current")
_EqliscsiReplicantSiteStoragePoolIndex_Type = Unsigned32
_EqliscsiReplicantSiteStoragePoolIndex_Object = MibTableColumn
eqliscsiReplicantSiteStoragePoolIndex = _EqliscsiReplicantSiteStoragePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 18),
    _EqliscsiReplicantSiteStoragePoolIndex_Type()
)
eqliscsiReplicantSiteStoragePoolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteStoragePoolIndex.setStatus("current")
_EqliscsiReplicantSiteSpaceSubscribed_Type = Unsigned32
_EqliscsiReplicantSiteSpaceSubscribed_Object = MibTableColumn
eqliscsiReplicantSiteSpaceSubscribed = _EqliscsiReplicantSiteSpaceSubscribed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 19),
    _EqliscsiReplicantSiteSpaceSubscribed_Type()
)
eqliscsiReplicantSiteSpaceSubscribed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteSpaceSubscribed.setStatus("current")
_EqliscsiReplicantSiteInetAddrType_Type = InetAddressType
_EqliscsiReplicantSiteInetAddrType_Object = MibTableColumn
eqliscsiReplicantSiteInetAddrType = _EqliscsiReplicantSiteInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 20),
    _EqliscsiReplicantSiteInetAddrType_Type()
)
eqliscsiReplicantSiteInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteInetAddrType.setStatus("current")
_EqliscsiReplicantSiteInetAddr_Type = InetAddress
_EqliscsiReplicantSiteInetAddr_Object = MibTableColumn
eqliscsiReplicantSiteInetAddr = _EqliscsiReplicantSiteInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 21),
    _EqliscsiReplicantSiteInetAddr_Type()
)
eqliscsiReplicantSiteInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteInetAddr.setStatus("current")
_EqliscsiReplicantSiteUnmanagedSpace_Type = Unsigned32
_EqliscsiReplicantSiteUnmanagedSpace_Object = MibTableColumn
eqliscsiReplicantSiteUnmanagedSpace = _EqliscsiReplicantSiteUnmanagedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 22),
    _EqliscsiReplicantSiteUnmanagedSpace_Type()
)
eqliscsiReplicantSiteUnmanagedSpace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteUnmanagedSpace.setStatus("current")


class _EqliscsiReplicantSiteReplType_Type(Integer32):
    """Custom type eqliscsiReplicantSiteReplType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("normal", 0))
    )


_EqliscsiReplicantSiteReplType_Type.__name__ = "Integer32"
_EqliscsiReplicantSiteReplType_Object = MibTableColumn
eqliscsiReplicantSiteReplType = _EqliscsiReplicantSiteReplType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 20, 1, 23),
    _EqliscsiReplicantSiteReplType_Type()
)
eqliscsiReplicantSiteReplType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteReplType.setStatus("current")
_EqliscsiVolCollectionObjectsTable_Object = MibTable
eqliscsiVolCollectionObjectsTable = _EqliscsiVolCollectionObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 21)
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionObjectsTable.setStatus("current")
_EqliscsiVolCollectionObjectsEntry_Object = MibTableRow
eqliscsiVolCollectionObjectsEntry = _EqliscsiVolCollectionObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 21, 1)
)
eqliscsiVolCollectionObjectsEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolCollectionIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionObjectsEntry.setStatus("current")
_EqliscsiVolCollectionIndex_Type = Unsigned32
_EqliscsiVolCollectionIndex_Object = MibTableColumn
eqliscsiVolCollectionIndex = _EqliscsiVolCollectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 21, 1, 1),
    _EqliscsiVolCollectionIndex_Type()
)
eqliscsiVolCollectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionIndex.setStatus("current")
_EqliscsiVolCollectionObjectRowStatus_Type = RowStatus
_EqliscsiVolCollectionObjectRowStatus_Object = MibTableColumn
eqliscsiVolCollectionObjectRowStatus = _EqliscsiVolCollectionObjectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 21, 1, 2),
    _EqliscsiVolCollectionObjectRowStatus_Type()
)
eqliscsiVolCollectionObjectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionObjectRowStatus.setStatus("current")
_EqliscsiVolCollectionTable_Object = MibTable
eqliscsiVolCollectionTable = _EqliscsiVolCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 22)
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionTable.setStatus("current")
_EqliscsiVolCollectionEntry_Object = MibTableRow
eqliscsiVolCollectionEntry = _EqliscsiVolCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 22, 1)
)
eqliscsiVolCollectionEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolCollectionIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionEntry.setStatus("current")
_EqliscsiVolCollectionRowStatus_Type = RowStatus
_EqliscsiVolCollectionRowStatus_Object = MibTableColumn
eqliscsiVolCollectionRowStatus = _EqliscsiVolCollectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 22, 1, 1),
    _EqliscsiVolCollectionRowStatus_Type()
)
eqliscsiVolCollectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionRowStatus.setStatus("current")


class _EqliscsiVolCollectionName_Type(OctetString):
    """Custom type eqliscsiVolCollectionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiVolCollectionName_Type.__name__ = "OctetString"
_EqliscsiVolCollectionName_Object = MibTableColumn
eqliscsiVolCollectionName = _EqliscsiVolCollectionName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 22, 1, 2),
    _EqliscsiVolCollectionName_Type()
)
eqliscsiVolCollectionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionName.setStatus("current")


class _EqliscsiVolCollectionDescription_Type(UTFString):
    """Custom type eqliscsiVolCollectionDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiVolCollectionDescription_Type.__name__ = "UTFString"
_EqliscsiVolCollectionDescription_Object = MibTableColumn
eqliscsiVolCollectionDescription = _EqliscsiVolCollectionDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 22, 1, 3),
    _EqliscsiVolCollectionDescription_Type()
)
eqliscsiVolCollectionDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionDescription.setStatus("current")


class _EqliscsiVolCollectionReplService_Type(Integer32):
    """Custom type eqliscsiVolCollectionReplService based on Integer32"""
    defaultValue = 0

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
          ("replica-site", 1),
          ("replicated-primary", 2))
    )


_EqliscsiVolCollectionReplService_Type.__name__ = "Integer32"
_EqliscsiVolCollectionReplService_Object = MibTableColumn
eqliscsiVolCollectionReplService = _EqliscsiVolCollectionReplService_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 22, 1, 4),
    _EqliscsiVolCollectionReplService_Type()
)
eqliscsiVolCollectionReplService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionReplService.setStatus("current")


class _EqliscsiVolCollectionSite_Type(SiteIndexOrZero):
    """Custom type eqliscsiVolCollectionSite based on SiteIndexOrZero"""
    defaultValue = 0


_EqliscsiVolCollectionSite_Object = MibTableColumn
eqliscsiVolCollectionSite = _EqliscsiVolCollectionSite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 22, 1, 5),
    _EqliscsiVolCollectionSite_Type()
)
eqliscsiVolCollectionSite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSite.setStatus("current")


class _EqliscsiVolCollectionFlags_Type(Bits):
    """Custom type eqliscsiVolCollectionFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("flag1", 1),
          ("flag10", 10),
          ("flag11", 11),
          ("flag12", 12),
          ("flag13", 13),
          ("flag14", 14),
          ("flag15", 15),
          ("flag16", 16),
          ("flag17", 17),
          ("flag18", 18),
          ("flag19", 19),
          ("flag2", 2),
          ("flag20", 20),
          ("flag21", 21),
          ("flag22", 22),
          ("flag23", 23),
          ("flag24", 24),
          ("flag25", 25),
          ("flag26", 26),
          ("flag27", 27),
          ("flag28", 28),
          ("flag29", 29),
          ("flag3", 3),
          ("flag30", 30),
          ("flag31", 31),
          ("flag4", 4),
          ("flag5", 5),
          ("flag6", 6),
          ("flag7", 7),
          ("flag8", 8),
          ("flag9", 9),
          ("isPoolSyncReplicated", 0))
    )

_EqliscsiVolCollectionFlags_Type.__name__ = "Bits"
_EqliscsiVolCollectionFlags_Object = MibTableColumn
eqliscsiVolCollectionFlags = _EqliscsiVolCollectionFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 22, 1, 6),
    _EqliscsiVolCollectionFlags_Type()
)
eqliscsiVolCollectionFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionFlags.setStatus("current")
_EqliscsiSnapCollectionObjectsTable_Object = MibTable
eqliscsiSnapCollectionObjectsTable = _EqliscsiSnapCollectionObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 23)
)
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionObjectsTable.setStatus("current")
_EqliscsiSnapCollectionObjectsEntry_Object = MibTableRow
eqliscsiSnapCollectionObjectsEntry = _EqliscsiSnapCollectionObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 23, 1)
)
eqliscsiSnapCollectionObjectsEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiSnapCollectionIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiSnapshotIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionObjectsEntry.setStatus("current")
_EqliscsiSnapCollectionIndex_Type = Unsigned32
_EqliscsiSnapCollectionIndex_Object = MibTableColumn
eqliscsiSnapCollectionIndex = _EqliscsiSnapCollectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 23, 1, 1),
    _EqliscsiSnapCollectionIndex_Type()
)
eqliscsiSnapCollectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionIndex.setStatus("current")
_EqliscsiSnapCollectionObjectRowStatus_Type = RowStatus
_EqliscsiSnapCollectionObjectRowStatus_Object = MibTableColumn
eqliscsiSnapCollectionObjectRowStatus = _EqliscsiSnapCollectionObjectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 23, 1, 2),
    _EqliscsiSnapCollectionObjectRowStatus_Type()
)
eqliscsiSnapCollectionObjectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionObjectRowStatus.setStatus("current")
_EqliscsiSnapCollectionTable_Object = MibTable
eqliscsiSnapCollectionTable = _EqliscsiSnapCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24)
)
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionTable.setStatus("current")
_EqliscsiSnapCollectionEntry_Object = MibTableRow
eqliscsiSnapCollectionEntry = _EqliscsiSnapCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1)
)
eqliscsiSnapCollectionEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiSnapCollectionIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionEntry.setStatus("current")
_EqliscsiSnapCollectionRowStatus_Type = RowStatus
_EqliscsiSnapCollectionRowStatus_Object = MibTableColumn
eqliscsiSnapCollectionRowStatus = _EqliscsiSnapCollectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 1),
    _EqliscsiSnapCollectionRowStatus_Type()
)
eqliscsiSnapCollectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionRowStatus.setStatus("current")


class _EqliscsiSnapCollectionName_Type(OctetString):
    """Custom type eqliscsiSnapCollectionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_EqliscsiSnapCollectionName_Type.__name__ = "OctetString"
_EqliscsiSnapCollectionName_Object = MibTableColumn
eqliscsiSnapCollectionName = _EqliscsiSnapCollectionName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 2),
    _EqliscsiSnapCollectionName_Type()
)
eqliscsiSnapCollectionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionName.setStatus("current")


class _EqliscsiSnapCollectionDescription_Type(UTFString):
    """Custom type eqliscsiSnapCollectionDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiSnapCollectionDescription_Type.__name__ = "UTFString"
_EqliscsiSnapCollectionDescription_Object = MibTableColumn
eqliscsiSnapCollectionDescription = _EqliscsiSnapCollectionDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 3),
    _EqliscsiSnapCollectionDescription_Type()
)
eqliscsiSnapCollectionDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionDescription.setStatus("current")
_EqliscsiSnapCollectionTimestamp_Type = Counter32
_EqliscsiSnapCollectionTimestamp_Object = MibTableColumn
eqliscsiSnapCollectionTimestamp = _EqliscsiSnapCollectionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 4),
    _EqliscsiSnapCollectionTimestamp_Type()
)
eqliscsiSnapCollectionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionTimestamp.setStatus("current")
_EqliscsiSnapCollectionNoofSnaps_Type = Unsigned32
_EqliscsiSnapCollectionNoofSnaps_Object = MibTableColumn
eqliscsiSnapCollectionNoofSnaps = _EqliscsiSnapCollectionNoofSnaps_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 5),
    _EqliscsiSnapCollectionNoofSnaps_Type()
)
eqliscsiSnapCollectionNoofSnaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionNoofSnaps.setStatus("current")
_EqliscsiSnapCollectionVolIndex_Type = Unsigned32
_EqliscsiSnapCollectionVolIndex_Object = MibTableColumn
eqliscsiSnapCollectionVolIndex = _EqliscsiSnapCollectionVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 6),
    _EqliscsiSnapCollectionVolIndex_Type()
)
eqliscsiSnapCollectionVolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionVolIndex.setStatus("current")


class _EqliscsiSnapCollectionVSS_Type(Integer32):
    """Custom type eqliscsiSnapCollectionVSS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("regular", 0),
          ("vss", 1))
    )


_EqliscsiSnapCollectionVSS_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionVSS_Object = MibTableColumn
eqliscsiSnapCollectionVSS = _EqliscsiSnapCollectionVSS_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 7),
    _EqliscsiSnapCollectionVSS_Type()
)
eqliscsiSnapCollectionVSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionVSS.setStatus("current")
_EqliscsiSnapCollectionScheduleIndex_Type = Integer32
_EqliscsiSnapCollectionScheduleIndex_Object = MibTableColumn
eqliscsiSnapCollectionScheduleIndex = _EqliscsiSnapCollectionScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 8),
    _EqliscsiSnapCollectionScheduleIndex_Type()
)
eqliscsiSnapCollectionScheduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionScheduleIndex.setStatus("current")
_EqliscsiSnapCollectionReplicated_Type = SiteIndexOrZero
_EqliscsiSnapCollectionReplicated_Object = MibTableColumn
eqliscsiSnapCollectionReplicated = _EqliscsiSnapCollectionReplicated_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 9),
    _EqliscsiSnapCollectionReplicated_Type()
)
eqliscsiSnapCollectionReplicated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionReplicated.setStatus("current")


class _EqliscsiSnapCollectionType_Type(Integer32):
    """Custom type eqliscsiSnapCollectionType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("regular", 0),
          ("replica-site", 1))
    )


_EqliscsiSnapCollectionType_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionType_Object = MibTableColumn
eqliscsiSnapCollectionType = _EqliscsiSnapCollectionType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 10),
    _EqliscsiSnapCollectionType_Type()
)
eqliscsiSnapCollectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionType.setStatus("current")


class _EqliscsiSnapCollectionSite_Type(SiteIndexOrZero):
    """Custom type eqliscsiSnapCollectionSite based on SiteIndexOrZero"""
    defaultValue = 0


_EqliscsiSnapCollectionSite_Object = MibTableColumn
eqliscsiSnapCollectionSite = _EqliscsiSnapCollectionSite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 24, 1, 11),
    _EqliscsiSnapCollectionSite_Type()
)
eqliscsiSnapCollectionSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionSite.setStatus("current")
_EqliscsiSnapCollectionPolicyTable_Object = MibTable
eqliscsiSnapCollectionPolicyTable = _EqliscsiSnapCollectionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25)
)
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyTable.setStatus("current")
_EqliscsiSnapCollectionPolicyEntry_Object = MibTableRow
eqliscsiSnapCollectionPolicyEntry = _EqliscsiSnapCollectionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1)
)
eqliscsiSnapCollectionPolicyEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolCollectionIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiSnapCollectionPolicyIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyEntry.setStatus("current")
_EqliscsiSnapCollectionPolicyIndex_Type = Integer32
_EqliscsiSnapCollectionPolicyIndex_Object = MibTableColumn
eqliscsiSnapCollectionPolicyIndex = _EqliscsiSnapCollectionPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 1),
    _EqliscsiSnapCollectionPolicyIndex_Type()
)
eqliscsiSnapCollectionPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyIndex.setStatus("current")
_EqliscsiSnapCollectionPolicyRowStatus_Type = RowStatus
_EqliscsiSnapCollectionPolicyRowStatus_Object = MibTableColumn
eqliscsiSnapCollectionPolicyRowStatus = _EqliscsiSnapCollectionPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 2),
    _EqliscsiSnapCollectionPolicyRowStatus_Type()
)
eqliscsiSnapCollectionPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyRowStatus.setStatus("current")


class _EqliscsiSnapCollectionPolicyName_Type(OctetString):
    """Custom type eqliscsiSnapCollectionPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqliscsiSnapCollectionPolicyName_Type.__name__ = "OctetString"
_EqliscsiSnapCollectionPolicyName_Object = MibTableColumn
eqliscsiSnapCollectionPolicyName = _EqliscsiSnapCollectionPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 3),
    _EqliscsiSnapCollectionPolicyName_Type()
)
eqliscsiSnapCollectionPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyName.setStatus("current")


class _EqliscsiSnapCollectionPolicyAccessType_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyAccessType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 2),
          ("read-write", 1))
    )


_EqliscsiSnapCollectionPolicyAccessType_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyAccessType_Object = MibTableColumn
eqliscsiSnapCollectionPolicyAccessType = _EqliscsiSnapCollectionPolicyAccessType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 4),
    _EqliscsiSnapCollectionPolicyAccessType_Type()
)
eqliscsiSnapCollectionPolicyAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyAccessType.setStatus("current")


class _EqliscsiSnapCollectionPolicyStatus_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_EqliscsiSnapCollectionPolicyStatus_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyStatus_Object = MibTableColumn
eqliscsiSnapCollectionPolicyStatus = _EqliscsiSnapCollectionPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 5),
    _EqliscsiSnapCollectionPolicyStatus_Type()
)
eqliscsiSnapCollectionPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyStatus.setStatus("current")


class _EqliscsiSnapCollectionPolicyMaxKeep_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyMaxKeep based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqliscsiSnapCollectionPolicyMaxKeep_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyMaxKeep_Object = MibTableColumn
eqliscsiSnapCollectionPolicyMaxKeep = _EqliscsiSnapCollectionPolicyMaxKeep_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 6),
    _EqliscsiSnapCollectionPolicyMaxKeep_Type()
)
eqliscsiSnapCollectionPolicyMaxKeep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyMaxKeep.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyMaxKeep.setUnits("snapshots")


class _EqliscsiSnapCollectionPolicyType_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("daily", 2),
          ("hourly", 5),
          ("monthly", 4),
          ("once", 1),
          ("weekly", 3))
    )


_EqliscsiSnapCollectionPolicyType_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyType_Object = MibTableColumn
eqliscsiSnapCollectionPolicyType = _EqliscsiSnapCollectionPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 7),
    _EqliscsiSnapCollectionPolicyType_Type()
)
eqliscsiSnapCollectionPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyType.setStatus("current")


class _EqliscsiSnapCollectionPolicyRepeatFactor_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyRepeatFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqliscsiSnapCollectionPolicyRepeatFactor_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyRepeatFactor_Object = MibTableColumn
eqliscsiSnapCollectionPolicyRepeatFactor = _EqliscsiSnapCollectionPolicyRepeatFactor_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 8),
    _EqliscsiSnapCollectionPolicyRepeatFactor_Type()
)
eqliscsiSnapCollectionPolicyRepeatFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyRepeatFactor.setStatus("current")


class _EqliscsiSnapCollectionPolicyStartTime_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyStartTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_EqliscsiSnapCollectionPolicyStartTime_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyStartTime_Object = MibTableColumn
eqliscsiSnapCollectionPolicyStartTime = _EqliscsiSnapCollectionPolicyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 9),
    _EqliscsiSnapCollectionPolicyStartTime_Type()
)
eqliscsiSnapCollectionPolicyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyStartTime.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyStartTime.setUnits("minutes")


class _EqliscsiSnapCollectionPolicyEndTime_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_EqliscsiSnapCollectionPolicyEndTime_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyEndTime_Object = MibTableColumn
eqliscsiSnapCollectionPolicyEndTime = _EqliscsiSnapCollectionPolicyEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 10),
    _EqliscsiSnapCollectionPolicyEndTime_Type()
)
eqliscsiSnapCollectionPolicyEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyEndTime.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyEndTime.setUnits("minutes")


class _EqliscsiSnapCollectionPolicyTimeFrequency_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyTimeFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_EqliscsiSnapCollectionPolicyTimeFrequency_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyTimeFrequency_Object = MibTableColumn
eqliscsiSnapCollectionPolicyTimeFrequency = _EqliscsiSnapCollectionPolicyTimeFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 11),
    _EqliscsiSnapCollectionPolicyTimeFrequency_Type()
)
eqliscsiSnapCollectionPolicyTimeFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyTimeFrequency.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyTimeFrequency.setUnits("minutes")


class _EqliscsiSnapCollectionPolicyStartDate_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyStartDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqliscsiSnapCollectionPolicyStartDate_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyStartDate_Object = MibTableColumn
eqliscsiSnapCollectionPolicyStartDate = _EqliscsiSnapCollectionPolicyStartDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 12),
    _EqliscsiSnapCollectionPolicyStartDate_Type()
)
eqliscsiSnapCollectionPolicyStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyStartDate.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyStartDate.setUnits("days")


class _EqliscsiSnapCollectionPolicyEndDate_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyEndDate based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqliscsiSnapCollectionPolicyEndDate_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyEndDate_Object = MibTableColumn
eqliscsiSnapCollectionPolicyEndDate = _EqliscsiSnapCollectionPolicyEndDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 13),
    _EqliscsiSnapCollectionPolicyEndDate_Type()
)
eqliscsiSnapCollectionPolicyEndDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyEndDate.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyEndDate.setUnits("days")
_EqliscsiSnapCollectionPolicyWeekMask_Type = Integer32
_EqliscsiSnapCollectionPolicyWeekMask_Object = MibTableColumn
eqliscsiSnapCollectionPolicyWeekMask = _EqliscsiSnapCollectionPolicyWeekMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 14),
    _EqliscsiSnapCollectionPolicyWeekMask_Type()
)
eqliscsiSnapCollectionPolicyWeekMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyWeekMask.setStatus("current")
_EqliscsiSnapCollectionPolicyMonthMask_Type = Integer32
_EqliscsiSnapCollectionPolicyMonthMask_Object = MibTableColumn
eqliscsiSnapCollectionPolicyMonthMask = _EqliscsiSnapCollectionPolicyMonthMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 15),
    _EqliscsiSnapCollectionPolicyMonthMask_Type()
)
eqliscsiSnapCollectionPolicyMonthMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyMonthMask.setStatus("current")
_EqliscsiSnapCollectionPolicyNextCreate_Type = Counter32
_EqliscsiSnapCollectionPolicyNextCreate_Object = MibTableColumn
eqliscsiSnapCollectionPolicyNextCreate = _EqliscsiSnapCollectionPolicyNextCreate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 16),
    _EqliscsiSnapCollectionPolicyNextCreate_Type()
)
eqliscsiSnapCollectionPolicyNextCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyNextCreate.setStatus("current")


class _EqliscsiSnapCollectionPolicyOccurence_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyOccurence based on Integer32"""
    defaultValue = 0


_EqliscsiSnapCollectionPolicyOccurence_Object = MibTableColumn
eqliscsiSnapCollectionPolicyOccurence = _EqliscsiSnapCollectionPolicyOccurence_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 17),
    _EqliscsiSnapCollectionPolicyOccurence_Type()
)
eqliscsiSnapCollectionPolicyOccurence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyOccurence.setStatus("current")
_EqliscsiSnapCollectionPolicyReplication_Type = SiteIndexOrZero
_EqliscsiSnapCollectionPolicyReplication_Object = MibTableColumn
eqliscsiSnapCollectionPolicyReplication = _EqliscsiSnapCollectionPolicyReplication_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 18),
    _EqliscsiSnapCollectionPolicyReplication_Type()
)
eqliscsiSnapCollectionPolicyReplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyReplication.setStatus("current")


class _EqliscsiSnapCollectionPolicyAdminStatus_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_EqliscsiSnapCollectionPolicyAdminStatus_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyAdminStatus_Object = MibTableColumn
eqliscsiSnapCollectionPolicyAdminStatus = _EqliscsiSnapCollectionPolicyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 25, 1, 19),
    _EqliscsiSnapCollectionPolicyAdminStatus_Type()
)
eqliscsiSnapCollectionPolicyAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyAdminStatus.setStatus("current")
_EqliscsiVolCollectionStatusTable_Object = MibTable
eqliscsiVolCollectionStatusTable = _EqliscsiVolCollectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 26)
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionStatusTable.setStatus("current")
_EqliscsiVolCollectionStatusEntry_Object = MibTableRow
eqliscsiVolCollectionStatusEntry = _EqliscsiVolCollectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 26, 1)
)
eqliscsiVolCollectionStatusEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolCollectionIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionStatusEntry.setStatus("current")


class _EqliscsiNoOfSnapCollections_Type(Unsigned32):
    """Custom type eqliscsiNoOfSnapCollections based on Unsigned32"""
    defaultValue = 0


_EqliscsiNoOfSnapCollections_Object = MibTableColumn
eqliscsiNoOfSnapCollections = _EqliscsiNoOfSnapCollections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 26, 1, 1),
    _EqliscsiNoOfSnapCollections_Type()
)
eqliscsiNoOfSnapCollections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiNoOfSnapCollections.setStatus("current")
_EqliscsiSnapCollectionAdminGroup_ObjectIdentity = ObjectIdentity
eqliscsiSnapCollectionAdminGroup = _EqliscsiSnapCollectionAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 27)
)
_EqliscsiLastSnapCollectionIndex_Type = Unsigned32
_EqliscsiLastSnapCollectionIndex_Object = MibScalar
eqliscsiLastSnapCollectionIndex = _EqliscsiLastSnapCollectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 27, 1),
    _EqliscsiLastSnapCollectionIndex_Type()
)
eqliscsiLastSnapCollectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiLastSnapCollectionIndex.setStatus("current")
_EqliscsiRemoteReplicaCollectionObjectsTable_Object = MibTable
eqliscsiRemoteReplicaCollectionObjectsTable = _EqliscsiRemoteReplicaCollectionObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 28)
)
if mibBuilder.loadTexts:
    eqliscsiRemoteReplicaCollectionObjectsTable.setStatus("current")
_EqliscsiRemoteReplicaCollectionObjectsEntry_Object = MibTableRow
eqliscsiRemoteReplicaCollectionObjectsEntry = _EqliscsiRemoteReplicaCollectionObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 28, 1)
)
eqliscsiRemoteReplicaCollectionObjectsEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiRemoteSnapCollectionIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiRemoteVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiRemoteSnapIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiRemoteReplicaCollectionObjectsEntry.setStatus("current")
_EqliscsiRemoteSnapCollectionIndex_Type = Unsigned32
_EqliscsiRemoteSnapCollectionIndex_Object = MibTableColumn
eqliscsiRemoteSnapCollectionIndex = _EqliscsiRemoteSnapCollectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 28, 1, 1),
    _EqliscsiRemoteSnapCollectionIndex_Type()
)
eqliscsiRemoteSnapCollectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiRemoteSnapCollectionIndex.setStatus("current")
_EqliscsiRemoteReplCollectionObjRowStatus_Type = RowStatus
_EqliscsiRemoteReplCollectionObjRowStatus_Object = MibTableColumn
eqliscsiRemoteReplCollectionObjRowStatus = _EqliscsiRemoteReplCollectionObjRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 28, 1, 2),
    _EqliscsiRemoteReplCollectionObjRowStatus_Type()
)
eqliscsiRemoteReplCollectionObjRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplCollectionObjRowStatus.setStatus("current")
_EqliscsiRemoteReplicaCollectionTable_Object = MibTable
eqliscsiRemoteReplicaCollectionTable = _EqliscsiRemoteReplicaCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 29)
)
if mibBuilder.loadTexts:
    eqliscsiRemoteReplicaCollectionTable.setStatus("current")
_EqliscsiRemoteReplicaCollectionEntry_Object = MibTableRow
eqliscsiRemoteReplicaCollectionEntry = _EqliscsiRemoteReplicaCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 29, 1)
)
eqliscsiRemoteReplicaCollectionEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiRemoteSnapCollectionIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiRemoteReplicaCollectionEntry.setStatus("current")


class _EqliscsiRemoteReplCollectionName_Type(OctetString):
    """Custom type eqliscsiRemoteReplCollectionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiRemoteReplCollectionName_Type.__name__ = "OctetString"
_EqliscsiRemoteReplCollectionName_Object = MibTableColumn
eqliscsiRemoteReplCollectionName = _EqliscsiRemoteReplCollectionName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 29, 1, 1),
    _EqliscsiRemoteReplCollectionName_Type()
)
eqliscsiRemoteReplCollectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplCollectionName.setStatus("current")


class _EqliscsiRemoteReplCollectionAdminStatus_Type(Integer32):
    """Custom type eqliscsiRemoteReplCollectionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("none", 0))
    )


_EqliscsiRemoteReplCollectionAdminStatus_Type.__name__ = "Integer32"
_EqliscsiRemoteReplCollectionAdminStatus_Object = MibTableColumn
eqliscsiRemoteReplCollectionAdminStatus = _EqliscsiRemoteReplCollectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 29, 1, 2),
    _EqliscsiRemoteReplCollectionAdminStatus_Type()
)
eqliscsiRemoteReplCollectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplCollectionAdminStatus.setStatus("current")
_EqliscsiRemoteReplCollectionTimeStamp_Type = Counter32
_EqliscsiRemoteReplCollectionTimeStamp_Object = MibTableColumn
eqliscsiRemoteReplCollectionTimeStamp = _EqliscsiRemoteReplCollectionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 29, 1, 3),
    _EqliscsiRemoteReplCollectionTimeStamp_Type()
)
eqliscsiRemoteReplCollectionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplCollectionTimeStamp.setStatus("current")
_EqliscsiRemoteReplCollectionVolIndex_Type = Unsigned32
_EqliscsiRemoteReplCollectionVolIndex_Object = MibTableColumn
eqliscsiRemoteReplCollectionVolIndex = _EqliscsiRemoteReplCollectionVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 29, 1, 4),
    _EqliscsiRemoteReplCollectionVolIndex_Type()
)
eqliscsiRemoteReplCollectionVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplCollectionVolIndex.setStatus("current")
_EqliscsiRemoteReplCollectionSchedIndex_Type = Unsigned32
_EqliscsiRemoteReplCollectionSchedIndex_Object = MibTableColumn
eqliscsiRemoteReplCollectionSchedIndex = _EqliscsiRemoteReplCollectionSchedIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 29, 1, 5),
    _EqliscsiRemoteReplCollectionSchedIndex_Type()
)
eqliscsiRemoteReplCollectionSchedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiRemoteReplCollectionSchedIndex.setStatus("current")
_EqliscsiVolColReplicationTable_Object = MibTable
eqliscsiVolColReplicationTable = _EqliscsiVolColReplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 30)
)
if mibBuilder.loadTexts:
    eqliscsiVolColReplicationTable.setStatus("current")
_EqliscsiVolColReplicationEntry_Object = MibTableRow
eqliscsiVolColReplicationEntry = _EqliscsiVolColReplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 30, 1)
)
eqliscsiVolColReplicationEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolCollectionIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolColReplicationEntry.setStatus("current")
_EqliscsiVolColReplRowStatus_Type = RowStatus
_EqliscsiVolColReplRowStatus_Object = MibTableColumn
eqliscsiVolColReplRowStatus = _EqliscsiVolColReplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 30, 1, 1),
    _EqliscsiVolColReplRowStatus_Type()
)
eqliscsiVolColReplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolColReplRowStatus.setStatus("current")


class _EqliscsiVolColReplAdminStatus_Type(Integer32):
    """Custom type eqliscsiVolColReplAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EqliscsiVolColReplAdminStatus_Type.__name__ = "Integer32"
_EqliscsiVolColReplAdminStatus_Object = MibTableColumn
eqliscsiVolColReplAdminStatus = _EqliscsiVolColReplAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 30, 1, 2),
    _EqliscsiVolColReplAdminStatus_Type()
)
eqliscsiVolColReplAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolColReplAdminStatus.setStatus("current")


class _EqliscsiVolColReplDeletionPolicy_Type(Integer32):
    """Custom type eqliscsiVolColReplDeletionPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-only", 1),
          ("remote", 2))
    )


_EqliscsiVolColReplDeletionPolicy_Type.__name__ = "Integer32"
_EqliscsiVolColReplDeletionPolicy_Object = MibTableColumn
eqliscsiVolColReplDeletionPolicy = _EqliscsiVolColReplDeletionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 30, 1, 3),
    _EqliscsiVolColReplDeletionPolicy_Type()
)
eqliscsiVolColReplDeletionPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolColReplDeletionPolicy.setStatus("current")
_EqliscsiVolColReplRemoteCollectionId_Type = Unsigned32
_EqliscsiVolColReplRemoteCollectionId_Object = MibTableColumn
eqliscsiVolColReplRemoteCollectionId = _EqliscsiVolColReplRemoteCollectionId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 30, 1, 4),
    _EqliscsiVolColReplRemoteCollectionId_Type()
)
eqliscsiVolColReplRemoteCollectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolColReplRemoteCollectionId.setStatus("current")
_EqliscsiVolColReplStatusTable_Object = MibTable
eqliscsiVolColReplStatusTable = _EqliscsiVolColReplStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 31)
)
if mibBuilder.loadTexts:
    eqliscsiVolColReplStatusTable.setStatus("current")
_EqliscsiVolColReplStatusEntry_Object = MibTableRow
eqliscsiVolColReplStatusEntry = _EqliscsiVolColReplStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 31, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolColReplStatusEntry.setStatus("current")


class _EqliscsiVolColReplStatusNumReplicas_Type(Unsigned32):
    """Custom type eqliscsiVolColReplStatusNumReplicas based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolColReplStatusNumReplicas_Object = MibTableColumn
eqliscsiVolColReplStatusNumReplicas = _EqliscsiVolColReplStatusNumReplicas_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 31, 1, 1),
    _EqliscsiVolColReplStatusNumReplicas_Type()
)
eqliscsiVolColReplStatusNumReplicas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolColReplStatusNumReplicas.setStatus("current")
_EqlVolumePoolPlacementTable_Object = MibTable
eqlVolumePoolPlacementTable = _EqlVolumePoolPlacementTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 32)
)
if mibBuilder.loadTexts:
    eqlVolumePoolPlacementTable.setStatus("current")
_EqlVolumePoolPlacementEntry_Object = MibTableRow
eqlVolumePoolPlacementEntry = _EqlVolumePoolPlacementEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 32, 1)
)
eqlVolumePoolPlacementEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqlVolumePoolPlacementEntry.setStatus("current")


class _EqlVolumePoolPlacementiscsiVolumePsvId_Type(OctetString):
    """Custom type eqlVolumePoolPlacementiscsiVolumePsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlVolumePoolPlacementiscsiVolumePsvId_Type.__name__ = "OctetString"
_EqlVolumePoolPlacementiscsiVolumePsvId_Object = MibTableColumn
eqlVolumePoolPlacementiscsiVolumePsvId = _EqlVolumePoolPlacementiscsiVolumePsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 32, 1, 1),
    _EqlVolumePoolPlacementiscsiVolumePsvId_Type()
)
eqlVolumePoolPlacementiscsiVolumePsvId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlVolumePoolPlacementiscsiVolumePsvId.setStatus("current")
_EqliscsiVolReplStatisticsTable_Object = MibTable
eqliscsiVolReplStatisticsTable = _EqliscsiVolReplStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 33)
)
if mibBuilder.loadTexts:
    eqliscsiVolReplStatisticsTable.setStatus("current")
_EqliscsiVolReplStatisticsEntry_Object = MibTableRow
eqliscsiVolReplStatisticsEntry = _EqliscsiVolReplStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 33, 1)
)
eqliscsiVolReplStatisticsEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiReplSampleIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolReplStatisticsEntry.setStatus("current")
_EqliscsiReplSampleIndex_Type = Unsigned32
_EqliscsiReplSampleIndex_Object = MibTableColumn
eqliscsiReplSampleIndex = _EqliscsiReplSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 33, 1, 1),
    _EqliscsiReplSampleIndex_Type()
)
eqliscsiReplSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiReplSampleIndex.setStatus("current")
_EqliscsiReplStartTime_Type = Counter32
_EqliscsiReplStartTime_Object = MibTableColumn
eqliscsiReplStartTime = _EqliscsiReplStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 33, 1, 2),
    _EqliscsiReplStartTime_Type()
)
eqliscsiReplStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplStartTime.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiReplStartTime.setUnits("seconds")
_EqliscsiReplEndTime_Type = Counter32
_EqliscsiReplEndTime_Object = MibTableColumn
eqliscsiReplEndTime = _EqliscsiReplEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 33, 1, 3),
    _EqliscsiReplEndTime_Type()
)
eqliscsiReplEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplEndTime.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiReplEndTime.setUnits("seconds")
_EqliscsiReplTxData_Type = Counter64
_EqliscsiReplTxData_Object = MibTableColumn
eqliscsiReplTxData = _EqliscsiReplTxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 33, 1, 4),
    _EqliscsiReplTxData_Type()
)
eqliscsiReplTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplTxData.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiReplTxData.setUnits("MB")


class _EqliscsiReplTxStatus_Type(Integer32):
    """Custom type eqliscsiReplTxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cancelled", 2),
          ("failed", 3),
          ("in-progress", 0),
          ("incomplete", 5),
          ("remoteReplicaSetIsFailoverVolume", 4),
          ("success", 1))
    )


_EqliscsiReplTxStatus_Type.__name__ = "Integer32"
_EqliscsiReplTxStatus_Object = MibTableColumn
eqliscsiReplTxStatus = _EqliscsiReplTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 33, 1, 5),
    _EqliscsiReplTxStatus_Type()
)
eqliscsiReplTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplTxStatus.setStatus("current")
_EqliscsiVolumeStatisticsTable_Object = MibTable
eqliscsiVolumeStatisticsTable = _EqliscsiVolumeStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeStatisticsTable.setStatus("current")
_EqliscsiVolumeStatisticsEntry_Object = MibTableRow
eqliscsiVolumeStatisticsEntry = _EqliscsiVolumeStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeStatisticsEntry.setStatus("current")
_EqliscsiVolumeStatsCmdPdus_Type = Counter32
_EqliscsiVolumeStatsCmdPdus_Object = MibTableColumn
eqliscsiVolumeStatsCmdPdus = _EqliscsiVolumeStatsCmdPdus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 1),
    _EqliscsiVolumeStatsCmdPdus_Type()
)
eqliscsiVolumeStatsCmdPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsCmdPdus.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsCmdPdus.setUnits("PDUs")
_EqliscsiVolumeStatsRspPdus_Type = Counter32
_EqliscsiVolumeStatsRspPdus_Object = MibTableColumn
eqliscsiVolumeStatsRspPdus = _EqliscsiVolumeStatsRspPdus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 2),
    _EqliscsiVolumeStatsRspPdus_Type()
)
eqliscsiVolumeStatsRspPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsRspPdus.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsRspPdus.setUnits("PDUs")
_EqliscsiVolumeStatsTxData_Type = Counter64
_EqliscsiVolumeStatsTxData_Object = MibTableColumn
eqliscsiVolumeStatsTxData = _EqliscsiVolumeStatsTxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 3),
    _EqliscsiVolumeStatsTxData_Type()
)
eqliscsiVolumeStatsTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsTxData.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsTxData.setUnits("octets")
_EqliscsiVolumeStatsRxData_Type = Counter64
_EqliscsiVolumeStatsRxData_Object = MibTableColumn
eqliscsiVolumeStatsRxData = _EqliscsiVolumeStatsRxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 4),
    _EqliscsiVolumeStatsRxData_Type()
)
eqliscsiVolumeStatsRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsRxData.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsRxData.setUnits("octets")
_EqliscsiVolumeStatsNoOfSessions_Type = Unsigned32
_EqliscsiVolumeStatsNoOfSessions_Object = MibTableColumn
eqliscsiVolumeStatsNoOfSessions = _EqliscsiVolumeStatsNoOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 5),
    _EqliscsiVolumeStatsNoOfSessions_Type()
)
eqliscsiVolumeStatsNoOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsNoOfSessions.setStatus("current")
_EqliscsiVolumeStatsReadLatency_Type = Counter64
_EqliscsiVolumeStatsReadLatency_Object = MibTableColumn
eqliscsiVolumeStatsReadLatency = _EqliscsiVolumeStatsReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 6),
    _EqliscsiVolumeStatsReadLatency_Type()
)
eqliscsiVolumeStatsReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsReadLatency.setStatus("current")
_EqliscsiVolumeStatsWriteLatency_Type = Counter64
_EqliscsiVolumeStatsWriteLatency_Object = MibTableColumn
eqliscsiVolumeStatsWriteLatency = _EqliscsiVolumeStatsWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 7),
    _EqliscsiVolumeStatsWriteLatency_Type()
)
eqliscsiVolumeStatsWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsWriteLatency.setStatus("current")
_EqliscsiVolumeStatsReadOpCount_Type = Counter64
_EqliscsiVolumeStatsReadOpCount_Object = MibTableColumn
eqliscsiVolumeStatsReadOpCount = _EqliscsiVolumeStatsReadOpCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 8),
    _EqliscsiVolumeStatsReadOpCount_Type()
)
eqliscsiVolumeStatsReadOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsReadOpCount.setStatus("current")
_EqliscsiVolumeStatsWriteOpCount_Type = Counter64
_EqliscsiVolumeStatsWriteOpCount_Object = MibTableColumn
eqliscsiVolumeStatsWriteOpCount = _EqliscsiVolumeStatsWriteOpCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 9),
    _EqliscsiVolumeStatsWriteOpCount_Type()
)
eqliscsiVolumeStatsWriteOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsWriteOpCount.setStatus("current")
_EqliscsiVolumeStatsReadAvgLatency_Type = Gauge32
_EqliscsiVolumeStatsReadAvgLatency_Object = MibTableColumn
eqliscsiVolumeStatsReadAvgLatency = _EqliscsiVolumeStatsReadAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 10),
    _EqliscsiVolumeStatsReadAvgLatency_Type()
)
eqliscsiVolumeStatsReadAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsReadAvgLatency.setStatus("current")
_EqliscsiVolumeStatsWriteAvgLatency_Type = Gauge32
_EqliscsiVolumeStatsWriteAvgLatency_Object = MibTableColumn
eqliscsiVolumeStatsWriteAvgLatency = _EqliscsiVolumeStatsWriteAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 11),
    _EqliscsiVolumeStatsWriteAvgLatency_Type()
)
eqliscsiVolumeStatsWriteAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsWriteAvgLatency.setStatus("current")
_EqliscsiVolumeStatsIscsiReadWriteCmdsReceived_Type = Counter32
_EqliscsiVolumeStatsIscsiReadWriteCmdsReceived_Object = MibTableColumn
eqliscsiVolumeStatsIscsiReadWriteCmdsReceived = _EqliscsiVolumeStatsIscsiReadWriteCmdsReceived_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 12),
    _EqliscsiVolumeStatsIscsiReadWriteCmdsReceived_Type()
)
eqliscsiVolumeStatsIscsiReadWriteCmdsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsIscsiReadWriteCmdsReceived.setStatus("current")
_EqliscsiVolumeStatsIscsiReadWriteCmdsCompleted_Type = Counter32
_EqliscsiVolumeStatsIscsiReadWriteCmdsCompleted_Object = MibTableColumn
eqliscsiVolumeStatsIscsiReadWriteCmdsCompleted = _EqliscsiVolumeStatsIscsiReadWriteCmdsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 13),
    _EqliscsiVolumeStatsIscsiReadWriteCmdsCompleted_Type()
)
eqliscsiVolumeStatsIscsiReadWriteCmdsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsIscsiReadWriteCmdsCompleted.setStatus("current")
_EqliscsiVolumeStatsHCIscsiReadWriteCmdsReceived_Type = Counter64
_EqliscsiVolumeStatsHCIscsiReadWriteCmdsReceived_Object = MibTableColumn
eqliscsiVolumeStatsHCIscsiReadWriteCmdsReceived = _EqliscsiVolumeStatsHCIscsiReadWriteCmdsReceived_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 14),
    _EqliscsiVolumeStatsHCIscsiReadWriteCmdsReceived_Type()
)
eqliscsiVolumeStatsHCIscsiReadWriteCmdsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsHCIscsiReadWriteCmdsReceived.setStatus("current")
_EqliscsiVolumeStatsHCIscsiTotalQD_Type = Counter64
_EqliscsiVolumeStatsHCIscsiTotalQD_Object = MibTableColumn
eqliscsiVolumeStatsHCIscsiTotalQD = _EqliscsiVolumeStatsHCIscsiTotalQD_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 15),
    _EqliscsiVolumeStatsHCIscsiTotalQD_Type()
)
eqliscsiVolumeStatsHCIscsiTotalQD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsHCIscsiTotalQD.setStatus("current")
_EqliscsiVolumeStatsMisAlignedIO_Type = Counter64
_EqliscsiVolumeStatsMisAlignedIO_Object = MibTableColumn
eqliscsiVolumeStatsMisAlignedIO = _EqliscsiVolumeStatsMisAlignedIO_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 34, 1, 16),
    _EqliscsiVolumeStatsMisAlignedIO_Type()
)
eqliscsiVolumeStatsMisAlignedIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStatsMisAlignedIO.setStatus("current")
_EqliscsiTargetAdminGroup_ObjectIdentity = ObjectIdentity
eqliscsiTargetAdminGroup = _EqliscsiTargetAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 35)
)
_EqliscsiLastTargetIndex_Type = Unsigned32
_EqliscsiLastTargetIndex_Object = MibScalar
eqliscsiLastTargetIndex = _EqliscsiLastTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 35, 1),
    _EqliscsiLastTargetIndex_Type()
)
eqliscsiLastTargetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiLastTargetIndex.setStatus("current")
_EqliscsiTargetTable_Object = MibTable
eqliscsiTargetTable = _EqliscsiTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 36)
)
if mibBuilder.loadTexts:
    eqliscsiTargetTable.setStatus("current")
_EqliscsiTargetEntry_Object = MibTableRow
eqliscsiTargetEntry = _EqliscsiTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 36, 1)
)
eqliscsiTargetEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiTargetIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiTargetEntry.setStatus("current")
_EqliscsiTargetIndex_Type = Unsigned32
_EqliscsiTargetIndex_Object = MibTableColumn
eqliscsiTargetIndex = _EqliscsiTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 36, 1, 1),
    _EqliscsiTargetIndex_Type()
)
eqliscsiTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiTargetIndex.setStatus("current")
_EqliscsiTargetRowStatus_Type = RowStatus
_EqliscsiTargetRowStatus_Object = MibTableColumn
eqliscsiTargetRowStatus = _EqliscsiTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 36, 1, 2),
    _EqliscsiTargetRowStatus_Type()
)
eqliscsiTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiTargetRowStatus.setStatus("current")


class _EqliscsiTargetUUID_Type(OctetString):
    """Custom type eqliscsiTargetUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiTargetUUID_Type.__name__ = "OctetString"
_EqliscsiTargetUUID_Object = MibTableColumn
eqliscsiTargetUUID = _EqliscsiTargetUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 36, 1, 3),
    _EqliscsiTargetUUID_Type()
)
eqliscsiTargetUUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiTargetUUID.setStatus("current")


class _EqliscsiTargetAlias_Type(OctetString):
    """Custom type eqliscsiTargetAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EqliscsiTargetAlias_Type.__name__ = "OctetString"
_EqliscsiTargetAlias_Object = MibTableColumn
eqliscsiTargetAlias = _EqliscsiTargetAlias_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 36, 1, 4),
    _EqliscsiTargetAlias_Type()
)
eqliscsiTargetAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiTargetAlias.setStatus("current")


class _EqliscsiTargetIscsiName_Type(OctetString):
    """Custom type eqliscsiTargetIscsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiTargetIscsiName_Type.__name__ = "OctetString"
_EqliscsiTargetIscsiName_Object = MibTableColumn
eqliscsiTargetIscsiName = _EqliscsiTargetIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 36, 1, 5),
    _EqliscsiTargetIscsiName_Type()
)
eqliscsiTargetIscsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiTargetIscsiName.setStatus("current")
_EqliscsiTargetReserved1_Type = Unsigned32
_EqliscsiTargetReserved1_Object = MibTableColumn
eqliscsiTargetReserved1 = _EqliscsiTargetReserved1_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 36, 1, 6),
    _EqliscsiTargetReserved1_Type()
)
eqliscsiTargetReserved1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiTargetReserved1.setStatus("current")
_EqliscsiTargetReserved2_Type = Unsigned32
_EqliscsiTargetReserved2_Object = MibTableColumn
eqliscsiTargetReserved2 = _EqliscsiTargetReserved2_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 36, 1, 7),
    _EqliscsiTargetReserved2_Type()
)
eqliscsiTargetReserved2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiTargetReserved2.setStatus("current")
_EqliscsiTargetReserved3_Type = Unsigned32
_EqliscsiTargetReserved3_Object = MibTableColumn
eqliscsiTargetReserved3 = _EqliscsiTargetReserved3_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 36, 1, 8),
    _EqliscsiTargetReserved3_Type()
)
eqliscsiTargetReserved3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiTargetReserved3.setStatus("current")
_EqliscsiTargetChapSecretsTable_Object = MibTable
eqliscsiTargetChapSecretsTable = _EqliscsiTargetChapSecretsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 37)
)
if mibBuilder.loadTexts:
    eqliscsiTargetChapSecretsTable.setStatus("current")
_EqliscsiTargetChapSecretsEntry_Object = MibTableRow
eqliscsiTargetChapSecretsEntry = _EqliscsiTargetChapSecretsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 37, 1)
)
eqliscsiTargetChapSecretsEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiTargetIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiTargetChapSecretsUsage"),
    (0, "EQLVOLUME-MIB", "eqliscsiTargetChapSecretsIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiTargetChapSecretsEntry.setStatus("current")


class _EqliscsiTargetChapSecretsUsage_Type(Integer32):
    """Custom type eqliscsiTargetChapSecretsUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound-iscsi-chap", 1),
          ("inbound-repl-chap", 3),
          ("outbound-iscsi-chap", 2))
    )


_EqliscsiTargetChapSecretsUsage_Type.__name__ = "Integer32"
_EqliscsiTargetChapSecretsUsage_Object = MibTableColumn
eqliscsiTargetChapSecretsUsage = _EqliscsiTargetChapSecretsUsage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 37, 1, 1),
    _EqliscsiTargetChapSecretsUsage_Type()
)
eqliscsiTargetChapSecretsUsage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiTargetChapSecretsUsage.setStatus("current")
_EqliscsiTargetChapSecretsIndex_Type = Unsigned32
_EqliscsiTargetChapSecretsIndex_Object = MibTableColumn
eqliscsiTargetChapSecretsIndex = _EqliscsiTargetChapSecretsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 37, 1, 2),
    _EqliscsiTargetChapSecretsIndex_Type()
)
eqliscsiTargetChapSecretsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiTargetChapSecretsIndex.setStatus("current")
_EqliscsiTargetChapSecretsRowStatus_Type = RowStatus
_EqliscsiTargetChapSecretsRowStatus_Object = MibTableColumn
eqliscsiTargetChapSecretsRowStatus = _EqliscsiTargetChapSecretsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 37, 1, 3),
    _EqliscsiTargetChapSecretsRowStatus_Type()
)
eqliscsiTargetChapSecretsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiTargetChapSecretsRowStatus.setStatus("current")


class _EqliscsiTargetChapSecretsUserName_Type(OctetString):
    """Custom type eqliscsiTargetChapSecretsUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqliscsiTargetChapSecretsUserName_Type.__name__ = "OctetString"
_EqliscsiTargetChapSecretsUserName_Object = MibTableColumn
eqliscsiTargetChapSecretsUserName = _EqliscsiTargetChapSecretsUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 37, 1, 4),
    _EqliscsiTargetChapSecretsUserName_Type()
)
eqliscsiTargetChapSecretsUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiTargetChapSecretsUserName.setStatus("current")


class _EqliscsiTargetChapSecretsPassword_Type(OctetString):
    """Custom type eqliscsiTargetChapSecretsPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqliscsiTargetChapSecretsPassword_Type.__name__ = "OctetString"
_EqliscsiTargetChapSecretsPassword_Object = MibTableColumn
eqliscsiTargetChapSecretsPassword = _EqliscsiTargetChapSecretsPassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 37, 1, 5),
    _EqliscsiTargetChapSecretsPassword_Type()
)
eqliscsiTargetChapSecretsPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiTargetChapSecretsPassword.setStatus("current")
_EqliscsiVolumeSnapshotPolicyStatusTable_Object = MibTable
eqliscsiVolumeSnapshotPolicyStatusTable = _EqliscsiVolumeSnapshotPolicyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 38)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyStatusTable.setStatus("current")
_EqliscsiVolumeSnapshotPolicyStatusEntry_Object = MibTableRow
eqliscsiVolumeSnapshotPolicyStatusEntry = _EqliscsiVolumeSnapshotPolicyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 38, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyStatusEntry.setStatus("current")
_EqliscsiVolumeSnapshotPolicyStatusNextCreate_Type = Counter32
_EqliscsiVolumeSnapshotPolicyStatusNextCreate_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyStatusNextCreate = _EqliscsiVolumeSnapshotPolicyStatusNextCreate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 38, 1, 1),
    _EqliscsiVolumeSnapshotPolicyStatusNextCreate_Type()
)
eqliscsiVolumeSnapshotPolicyStatusNextCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyStatusNextCreate.setStatus("current")


class _EqliscsiVolumeSnapshotPolicyStatusOperStatus_Type(Integer32):
    """Custom type eqliscsiVolumeSnapshotPolicyStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0),
          ("expired", 2))
    )


_EqliscsiVolumeSnapshotPolicyStatusOperStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeSnapshotPolicyStatusOperStatus_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyStatusOperStatus = _EqliscsiVolumeSnapshotPolicyStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 38, 1, 2),
    _EqliscsiVolumeSnapshotPolicyStatusOperStatus_Type()
)
eqliscsiVolumeSnapshotPolicyStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyStatusOperStatus.setStatus("current")
_EqliscsiVolumeSnapshotPolicyStatusNoOfSnaps_Type = Integer32
_EqliscsiVolumeSnapshotPolicyStatusNoOfSnaps_Object = MibTableColumn
eqliscsiVolumeSnapshotPolicyStatusNoOfSnaps = _EqliscsiVolumeSnapshotPolicyStatusNoOfSnaps_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 38, 1, 3),
    _EqliscsiVolumeSnapshotPolicyStatusNoOfSnaps_Type()
)
eqliscsiVolumeSnapshotPolicyStatusNoOfSnaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSnapshotPolicyStatusNoOfSnaps.setStatus("current")
_EqliscsiSnapCollectionPolicyStatusTable_Object = MibTable
eqliscsiSnapCollectionPolicyStatusTable = _EqliscsiSnapCollectionPolicyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 39)
)
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyStatusTable.setStatus("current")
_EqliscsiSnapCollectionPolicyStatusEntry_Object = MibTableRow
eqliscsiSnapCollectionPolicyStatusEntry = _EqliscsiSnapCollectionPolicyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 39, 1)
)
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyStatusEntry.setStatus("current")
_EqliscsiSnapCollectionPolicyStatusNextCreate_Type = Counter32
_EqliscsiSnapCollectionPolicyStatusNextCreate_Object = MibTableColumn
eqliscsiSnapCollectionPolicyStatusNextCreate = _EqliscsiSnapCollectionPolicyStatusNextCreate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 39, 1, 1),
    _EqliscsiSnapCollectionPolicyStatusNextCreate_Type()
)
eqliscsiSnapCollectionPolicyStatusNextCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyStatusNextCreate.setStatus("current")


class _EqliscsiSnapCollectionPolicyStatusOperStatus_Type(Integer32):
    """Custom type eqliscsiSnapCollectionPolicyStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0),
          ("expired", 2))
    )


_EqliscsiSnapCollectionPolicyStatusOperStatus_Type.__name__ = "Integer32"
_EqliscsiSnapCollectionPolicyStatusOperStatus_Object = MibTableColumn
eqliscsiSnapCollectionPolicyStatusOperStatus = _EqliscsiSnapCollectionPolicyStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 39, 1, 2),
    _EqliscsiSnapCollectionPolicyStatusOperStatus_Type()
)
eqliscsiSnapCollectionPolicyStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyStatusOperStatus.setStatus("current")
_EqliscsiSnapCollectionPolicyStatusNoOfCollections_Type = Integer32
_EqliscsiSnapCollectionPolicyStatusNoOfCollections_Object = MibTableColumn
eqliscsiSnapCollectionPolicyStatusNoOfCollections = _EqliscsiSnapCollectionPolicyStatusNoOfCollections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 39, 1, 3),
    _EqliscsiSnapCollectionPolicyStatusNoOfCollections_Type()
)
eqliscsiSnapCollectionPolicyStatusNoOfCollections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapCollectionPolicyStatusNoOfCollections.setStatus("current")
_EqliscsiVolumeOpsTable_Object = MibTable
eqliscsiVolumeOpsTable = _EqliscsiVolumeOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsTable.setStatus("current")
_EqliscsiVolumeOpsEntry_Object = MibTableRow
eqliscsiVolumeOpsEntry = _EqliscsiVolumeOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40, 1)
)
eqliscsiVolumeOpsEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeOpsIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsEntry.setStatus("current")
_EqliscsiVolumeOpsIndex_Type = Unsigned32
_EqliscsiVolumeOpsIndex_Object = MibTableColumn
eqliscsiVolumeOpsIndex = _EqliscsiVolumeOpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40, 1, 1),
    _EqliscsiVolumeOpsIndex_Type()
)
eqliscsiVolumeOpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsIndex.setStatus("current")
_EqliscsiVolumeOpsRowStatus_Type = RowStatus
_EqliscsiVolumeOpsRowStatus_Object = MibTableColumn
eqliscsiVolumeOpsRowStatus = _EqliscsiVolumeOpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40, 1, 2),
    _EqliscsiVolumeOpsRowStatus_Type()
)
eqliscsiVolumeOpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsRowStatus.setStatus("current")


class _EqliscsiVolumeOpsOperation_Type(Integer32):
    """Custom type eqliscsiVolumeOpsOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("movePool", 1),
          ("none", 0))
    )


_EqliscsiVolumeOpsOperation_Type.__name__ = "Integer32"
_EqliscsiVolumeOpsOperation_Object = MibTableColumn
eqliscsiVolumeOpsOperation = _EqliscsiVolumeOpsOperation_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40, 1, 3),
    _EqliscsiVolumeOpsOperation_Type()
)
eqliscsiVolumeOpsOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsOperation.setStatus("current")


class _EqliscsiVolumeOpsExec_Type(Integer32):
    """Custom type eqliscsiVolumeOpsExec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 1),
          ("failed", 2),
          ("none", 0))
    )


_EqliscsiVolumeOpsExec_Type.__name__ = "Integer32"
_EqliscsiVolumeOpsExec_Object = MibTableColumn
eqliscsiVolumeOpsExec = _EqliscsiVolumeOpsExec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40, 1, 4),
    _EqliscsiVolumeOpsExec_Type()
)
eqliscsiVolumeOpsExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsExec.setStatus("current")
_EqliscsiVolumeOpsStartTime_Type = Counter32
_EqliscsiVolumeOpsStartTime_Object = MibTableColumn
eqliscsiVolumeOpsStartTime = _EqliscsiVolumeOpsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40, 1, 5),
    _EqliscsiVolumeOpsStartTime_Type()
)
eqliscsiVolumeOpsStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsStartTime.setStatus("current")


class _EqliscsiVolumeOpsStoragePoolSourceIndex_Type(Unsigned32):
    """Custom type eqliscsiVolumeOpsStoragePoolSourceIndex based on Unsigned32"""
    defaultValue = 1


_EqliscsiVolumeOpsStoragePoolSourceIndex_Object = MibTableColumn
eqliscsiVolumeOpsStoragePoolSourceIndex = _EqliscsiVolumeOpsStoragePoolSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40, 1, 6),
    _EqliscsiVolumeOpsStoragePoolSourceIndex_Type()
)
eqliscsiVolumeOpsStoragePoolSourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsStoragePoolSourceIndex.setStatus("current")


class _EqliscsiVolumeOpsStoragePoolDestinationIndex_Type(Unsigned32):
    """Custom type eqliscsiVolumeOpsStoragePoolDestinationIndex based on Unsigned32"""
    defaultValue = 1


_EqliscsiVolumeOpsStoragePoolDestinationIndex_Object = MibTableColumn
eqliscsiVolumeOpsStoragePoolDestinationIndex = _EqliscsiVolumeOpsStoragePoolDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40, 1, 7),
    _EqliscsiVolumeOpsStoragePoolDestinationIndex_Type()
)
eqliscsiVolumeOpsStoragePoolDestinationIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsStoragePoolDestinationIndex.setStatus("current")
_EqliscsiVolumeOpsVolBalCommandIndex_Type = Unsigned32
_EqliscsiVolumeOpsVolBalCommandIndex_Object = MibTableColumn
eqliscsiVolumeOpsVolBalCommandIndex = _EqliscsiVolumeOpsVolBalCommandIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40, 1, 8),
    _EqliscsiVolumeOpsVolBalCommandIndex_Type()
)
eqliscsiVolumeOpsVolBalCommandIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsVolBalCommandIndex.setStatus("current")
_EqliscsiVolumeOpsVolBalCommandiscsiLocalMemberId_Type = Unsigned32
_EqliscsiVolumeOpsVolBalCommandiscsiLocalMemberId_Object = MibTableColumn
eqliscsiVolumeOpsVolBalCommandiscsiLocalMemberId = _EqliscsiVolumeOpsVolBalCommandiscsiLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 40, 1, 9),
    _EqliscsiVolumeOpsVolBalCommandiscsiLocalMemberId_Type()
)
eqliscsiVolumeOpsVolBalCommandiscsiLocalMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsVolBalCommandiscsiLocalMemberId.setStatus("current")
_EqliscsiReplicaSetExtensionTable_Object = MibTable
eqliscsiReplicaSetExtensionTable = _EqliscsiReplicaSetExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 41)
)
if mibBuilder.loadTexts:
    eqliscsiReplicaSetExtensionTable.setStatus("current")
_EqliscsiReplicaSetExtensionEntry_Object = MibTableRow
eqliscsiReplicaSetExtensionEntry = _EqliscsiReplicaSetExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 41, 1)
)
if mibBuilder.loadTexts:
    eqliscsiReplicaSetExtensionEntry.setStatus("current")


class _EqliscsiReplicaSetPrimaryPsvId_Type(OctetString):
    """Custom type eqliscsiReplicaSetPrimaryPsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiReplicaSetPrimaryPsvId_Type.__name__ = "OctetString"
_EqliscsiReplicaSetPrimaryPsvId_Object = MibTableColumn
eqliscsiReplicaSetPrimaryPsvId = _EqliscsiReplicaSetPrimaryPsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 41, 1, 1),
    _EqliscsiReplicaSetPrimaryPsvId_Type()
)
eqliscsiReplicaSetPrimaryPsvId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicaSetPrimaryPsvId.setStatus("current")
_EqliscsiVolumeStoragePreferenceTable_Object = MibTable
eqliscsiVolumeStoragePreferenceTable = _EqliscsiVolumeStoragePreferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 42)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeStoragePreferenceTable.setStatus("current")
_EqliscsiVolumeStoragePreferenceEntry_Object = MibTableRow
eqliscsiVolumeStoragePreferenceEntry = _EqliscsiVolumeStoragePreferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 42, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeStoragePreferenceEntry.setStatus("current")
_EqliscsiVolumeStoragePreferenceRowStatus_Type = RowStatus
_EqliscsiVolumeStoragePreferenceRowStatus_Object = MibTableColumn
eqliscsiVolumeStoragePreferenceRowStatus = _EqliscsiVolumeStoragePreferenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 42, 1, 1),
    _EqliscsiVolumeStoragePreferenceRowStatus_Type()
)
eqliscsiVolumeStoragePreferenceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeStoragePreferenceRowStatus.setStatus("current")


class _EqliscsiVolumeStoragePreferenceRAIDType_Type(Integer32):
    """Custom type eqliscsiVolumeStoragePreferenceRAIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              6,
              10,
              50,
              60,
              61)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("raid10", 10),
          ("raid5", 5),
          ("raid50", 50),
          ("raid6", 6),
          ("raid6-accelerated", 61),
          ("raid60", 60))
    )


_EqliscsiVolumeStoragePreferenceRAIDType_Type.__name__ = "Integer32"
_EqliscsiVolumeStoragePreferenceRAIDType_Object = MibTableColumn
eqliscsiVolumeStoragePreferenceRAIDType = _EqliscsiVolumeStoragePreferenceRAIDType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 42, 1, 2),
    _EqliscsiVolumeStoragePreferenceRAIDType_Type()
)
eqliscsiVolumeStoragePreferenceRAIDType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeStoragePreferenceRAIDType.setStatus("current")


class _EqliscsiVolumeStoragePreferenceDriveType_Type(Integer32):
    """Custom type eqliscsiVolumeStoragePreferenceDriveType based on Integer32"""
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
          ("sas", 1),
          ("sata", 2))
    )


_EqliscsiVolumeStoragePreferenceDriveType_Type.__name__ = "Integer32"
_EqliscsiVolumeStoragePreferenceDriveType_Object = MibTableColumn
eqliscsiVolumeStoragePreferenceDriveType = _EqliscsiVolumeStoragePreferenceDriveType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 42, 1, 3),
    _EqliscsiVolumeStoragePreferenceDriveType_Type()
)
eqliscsiVolumeStoragePreferenceDriveType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeStoragePreferenceDriveType.setStatus("current")


class _EqliscsiVolumeStoragePreferenceDiskSpeed_Type(Integer32):
    """Custom type eqliscsiVolumeStoragePreferenceDiskSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5400,
              7200,
              10000,
              15000)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("s10000", 10000),
          ("s15000", 15000),
          ("s5400", 5400),
          ("s7200", 7200))
    )


_EqliscsiVolumeStoragePreferenceDiskSpeed_Type.__name__ = "Integer32"
_EqliscsiVolumeStoragePreferenceDiskSpeed_Object = MibTableColumn
eqliscsiVolumeStoragePreferenceDiskSpeed = _EqliscsiVolumeStoragePreferenceDiskSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 42, 1, 4),
    _EqliscsiVolumeStoragePreferenceDiskSpeed_Type()
)
eqliscsiVolumeStoragePreferenceDiskSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeStoragePreferenceDiskSpeed.setStatus("current")


class _EqliscsiVolumeStoragePreferenceRAIDTypeStatus_Type(Integer32):
    """Custom type eqliscsiVolumeStoragePreferenceRAIDTypeStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("honored", 2),
          ("in-progress", 1),
          ("none", 0),
          ("not-available", 3),
          ("over-subscribed", 4),
          ("temporarily-unknown", 5))
    )


_EqliscsiVolumeStoragePreferenceRAIDTypeStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeStoragePreferenceRAIDTypeStatus_Object = MibTableColumn
eqliscsiVolumeStoragePreferenceRAIDTypeStatus = _EqliscsiVolumeStoragePreferenceRAIDTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 42, 1, 5),
    _EqliscsiVolumeStoragePreferenceRAIDTypeStatus_Type()
)
eqliscsiVolumeStoragePreferenceRAIDTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeStoragePreferenceRAIDTypeStatus.setStatus("current")
_EqlAdminAccountVolumeTable_Object = MibTable
eqlAdminAccountVolumeTable = _EqlAdminAccountVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 43)
)
if mibBuilder.loadTexts:
    eqlAdminAccountVolumeTable.setStatus("current")
_EqlAdminAccountVolumeEntry_Object = MibTableRow
eqlAdminAccountVolumeEntry = _EqlAdminAccountVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 43, 1)
)
eqlAdminAccountVolumeEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqlAdminAccountVolumeEntry.setStatus("current")


class _EqlAdminAccountVolumeAccess_Type(Integer32):
    """Custom type eqlAdminAccountVolumeAccess based on Integer32"""
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


_EqlAdminAccountVolumeAccess_Type.__name__ = "Integer32"
_EqlAdminAccountVolumeAccess_Object = MibTableColumn
eqlAdminAccountVolumeAccess = _EqlAdminAccountVolumeAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 43, 1, 1),
    _EqlAdminAccountVolumeAccess_Type()
)
eqlAdminAccountVolumeAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAdminAccountVolumeAccess.setStatus("current")
_EqlAdminAccountReplicantSiteTable_Object = MibTable
eqlAdminAccountReplicantSiteTable = _EqlAdminAccountReplicantSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 44)
)
if mibBuilder.loadTexts:
    eqlAdminAccountReplicantSiteTable.setStatus("current")
_EqlAdminAccountReplicantSiteEntry_Object = MibTableRow
eqlAdminAccountReplicantSiteEntry = _EqlAdminAccountReplicantSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 44, 1)
)
eqlAdminAccountReplicantSiteEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiReplicantSiteIndex"),
)
if mibBuilder.loadTexts:
    eqlAdminAccountReplicantSiteEntry.setStatus("current")


class _EqlAdminAccountReplicantSiteAccess_Type(Integer32):
    """Custom type eqlAdminAccountReplicantSiteAccess based on Integer32"""
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


_EqlAdminAccountReplicantSiteAccess_Type.__name__ = "Integer32"
_EqlAdminAccountReplicantSiteAccess_Object = MibTableColumn
eqlAdminAccountReplicantSiteAccess = _EqlAdminAccountReplicantSiteAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 44, 1, 1),
    _EqlAdminAccountReplicantSiteAccess_Type()
)
eqlAdminAccountReplicantSiteAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAdminAccountReplicantSiteAccess.setStatus("current")
_EqlAdminAccountVolCollectionTable_Object = MibTable
eqlAdminAccountVolCollectionTable = _EqlAdminAccountVolCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 45)
)
if mibBuilder.loadTexts:
    eqlAdminAccountVolCollectionTable.setStatus("current")
_EqlAdminAccountVolCollectionEntry_Object = MibTableRow
eqlAdminAccountVolCollectionEntry = _EqlAdminAccountVolCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 45, 1)
)
eqlAdminAccountVolCollectionEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolCollectionIndex"),
)
if mibBuilder.loadTexts:
    eqlAdminAccountVolCollectionEntry.setStatus("current")


class _EqlAdminAccountVolCollectionAccess_Type(Integer32):
    """Custom type eqlAdminAccountVolCollectionAccess based on Integer32"""
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


_EqlAdminAccountVolCollectionAccess_Type.__name__ = "Integer32"
_EqlAdminAccountVolCollectionAccess_Object = MibTableColumn
eqlAdminAccountVolCollectionAccess = _EqlAdminAccountVolCollectionAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 45, 1, 1),
    _EqlAdminAccountVolCollectionAccess_Type()
)
eqlAdminAccountVolCollectionAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlAdminAccountVolCollectionAccess.setStatus("current")
_EqliscsiVolumeOpsStatusTable_Object = MibTable
eqliscsiVolumeOpsStatusTable = _EqliscsiVolumeOpsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 46)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsStatusTable.setStatus("current")
_EqliscsiVolumeOpsStatusEntry_Object = MibTableRow
eqliscsiVolumeOpsStatusEntry = _EqliscsiVolumeOpsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 46, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsStatusEntry.setStatus("current")
_EqliscsiVolumeOpsStatusCompletePct_Type = Unsigned32
_EqliscsiVolumeOpsStatusCompletePct_Object = MibTableColumn
eqliscsiVolumeOpsStatusCompletePct = _EqliscsiVolumeOpsStatusCompletePct_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 46, 1, 1),
    _EqliscsiVolumeOpsStatusCompletePct_Type()
)
eqliscsiVolumeOpsStatusCompletePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeOpsStatusCompletePct.setStatus("current")
_EqliscsiVolumeDynamicConfigTable_Object = MibTable
eqliscsiVolumeDynamicConfigTable = _EqliscsiVolumeDynamicConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 47)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeDynamicConfigTable.setStatus("current")
_EqliscsiVolumeDynamicConfigEntry_Object = MibTableRow
eqliscsiVolumeDynamicConfigEntry = _EqliscsiVolumeDynamicConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 47, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeDynamicConfigEntry.setStatus("current")
_EqliscsiVolumeDynamicRowStatus_Type = RowStatus
_EqliscsiVolumeDynamicRowStatus_Object = MibTableColumn
eqliscsiVolumeDynamicRowStatus = _EqliscsiVolumeDynamicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 47, 1, 1),
    _EqliscsiVolumeDynamicRowStatus_Type()
)
eqliscsiVolumeDynamicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeDynamicRowStatus.setStatus("current")
_EqliscsiVolumeDynamicThinReserve_Type = Unsigned32
_EqliscsiVolumeDynamicThinReserve_Object = MibTableColumn
eqliscsiVolumeDynamicThinReserve = _EqliscsiVolumeDynamicThinReserve_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 47, 1, 2),
    _EqliscsiVolumeDynamicThinReserve_Type()
)
eqliscsiVolumeDynamicThinReserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeDynamicThinReserve.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeDynamicThinReserve.setUnits("MB")


class _EqliscsiVolumeDynamicInUseHighWaterMark_Type(Unsigned32):
    """Custom type eqliscsiVolumeDynamicInUseHighWaterMark based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolumeDynamicInUseHighWaterMark_Object = MibTableColumn
eqliscsiVolumeDynamicInUseHighWaterMark = _EqliscsiVolumeDynamicInUseHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 47, 1, 3),
    _EqliscsiVolumeDynamicInUseHighWaterMark_Type()
)
eqliscsiVolumeDynamicInUseHighWaterMark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeDynamicInUseHighWaterMark.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeDynamicInUseHighWaterMark.setUnits("MB")


class _EqliscsiVolumeDynamicInUseHighWaterMarkTimestamp_Type(Unsigned32):
    """Custom type eqliscsiVolumeDynamicInUseHighWaterMarkTimestamp based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolumeDynamicInUseHighWaterMarkTimestamp_Object = MibTableColumn
eqliscsiVolumeDynamicInUseHighWaterMarkTimestamp = _EqliscsiVolumeDynamicInUseHighWaterMarkTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 47, 1, 4),
    _EqliscsiVolumeDynamicInUseHighWaterMarkTimestamp_Type()
)
eqliscsiVolumeDynamicInUseHighWaterMarkTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeDynamicInUseHighWaterMarkTimestamp.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeDynamicInUseHighWaterMarkTimestamp.setUnits("seconds")
_EqliscsiVolumeReplSiteStatusTable_Object = MibTable
eqliscsiVolumeReplSiteStatusTable = _EqliscsiVolumeReplSiteStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 48)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteStatusTable.setStatus("current")
_EqliscsiVolumeReplSiteStatusEntry_Object = MibTableRow
eqliscsiVolumeReplSiteStatusEntry = _EqliscsiVolumeReplSiteStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 48, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteStatusEntry.setStatus("current")
_EqliscsiVolumeReplSiteFailbackSpace_Type = Unsigned32
_EqliscsiVolumeReplSiteFailbackSpace_Object = MibTableColumn
eqliscsiVolumeReplSiteFailbackSpace = _EqliscsiVolumeReplSiteFailbackSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 48, 1, 1),
    _EqliscsiVolumeReplSiteFailbackSpace_Type()
)
eqliscsiVolumeReplSiteFailbackSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteFailbackSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteFailbackSpace.setUnits("MB")
_EqliscsiVolumeChunkTable_Object = MibTable
eqliscsiVolumeChunkTable = _EqliscsiVolumeChunkTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 49)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeChunkTable.setStatus("current")
_EqliscsiVolumeChunkEntry_Object = MibTableRow
eqliscsiVolumeChunkEntry = _EqliscsiVolumeChunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 49, 1)
)
eqliscsiVolumeChunkEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeChunkIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeChunkEntry.setStatus("current")
_EqliscsiVolumeChunkIndex_Type = Unsigned32
_EqliscsiVolumeChunkIndex_Object = MibTableColumn
eqliscsiVolumeChunkIndex = _EqliscsiVolumeChunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 49, 1, 1),
    _EqliscsiVolumeChunkIndex_Type()
)
eqliscsiVolumeChunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeChunkIndex.setStatus("current")


class _EqliscsiVolumeChunkVersion_Type(Unsigned32):
    """Custom type eqliscsiVolumeChunkVersion based on Unsigned32"""
    defaultValue = 1


_EqliscsiVolumeChunkVersion_Object = MibTableColumn
eqliscsiVolumeChunkVersion = _EqliscsiVolumeChunkVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 49, 1, 2),
    _EqliscsiVolumeChunkVersion_Type()
)
eqliscsiVolumeChunkVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeChunkVersion.setStatus("current")
_EqliscsiVolumeChunkSegmentSize_Type = Unsigned32
_EqliscsiVolumeChunkSegmentSize_Object = MibTableColumn
eqliscsiVolumeChunkSegmentSize = _EqliscsiVolumeChunkSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 49, 1, 3),
    _EqliscsiVolumeChunkSegmentSize_Type()
)
eqliscsiVolumeChunkSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeChunkSegmentSize.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeChunkSegmentSize.setUnits("KB")
_EqliscsiVolumeChunkSegments_Type = Unsigned32
_EqliscsiVolumeChunkSegments_Object = MibTableColumn
eqliscsiVolumeChunkSegments = _EqliscsiVolumeChunkSegments_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 49, 1, 4),
    _EqliscsiVolumeChunkSegments_Type()
)
eqliscsiVolumeChunkSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeChunkSegments.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeChunkSegments.setUnits("segments")


class _EqliscsiVolumeChunkModified_Type(OctetString):
    """Custom type eqliscsiVolumeChunkModified based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1024, 1024),
    )


_EqliscsiVolumeChunkModified_Type.__name__ = "OctetString"
_EqliscsiVolumeChunkModified_Object = MibTableColumn
eqliscsiVolumeChunkModified = _EqliscsiVolumeChunkModified_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 49, 1, 5),
    _EqliscsiVolumeChunkModified_Type()
)
eqliscsiVolumeChunkModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeChunkModified.setStatus("current")
_EqliscsiReplicantSiteOpsTable_Object = MibTable
eqliscsiReplicantSiteOpsTable = _EqliscsiReplicantSiteOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50)
)
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsTable.setStatus("current")
_EqliscsiReplicantSiteOpsEntry_Object = MibTableRow
eqliscsiReplicantSiteOpsEntry = _EqliscsiReplicantSiteOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50, 1)
)
eqliscsiReplicantSiteOpsEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLVOLUME-MIB", "eqliscsiReplicantSiteIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiReplicantSiteOpsIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsEntry.setStatus("current")
_EqliscsiReplicantSiteOpsIndex_Type = Unsigned32
_EqliscsiReplicantSiteOpsIndex_Object = MibTableColumn
eqliscsiReplicantSiteOpsIndex = _EqliscsiReplicantSiteOpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50, 1, 1),
    _EqliscsiReplicantSiteOpsIndex_Type()
)
eqliscsiReplicantSiteOpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsIndex.setStatus("current")
_EqliscsiReplicantSiteOpsRowStatus_Type = RowStatus
_EqliscsiReplicantSiteOpsRowStatus_Object = MibTableColumn
eqliscsiReplicantSiteOpsRowStatus = _EqliscsiReplicantSiteOpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50, 1, 2),
    _EqliscsiReplicantSiteOpsRowStatus_Type()
)
eqliscsiReplicantSiteOpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsRowStatus.setStatus("current")


class _EqliscsiReplicantSiteOpsOperation_Type(Integer32):
    """Custom type eqliscsiReplicantSiteOpsOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("movePool", 1),
          ("none", 0))
    )


_EqliscsiReplicantSiteOpsOperation_Type.__name__ = "Integer32"
_EqliscsiReplicantSiteOpsOperation_Object = MibTableColumn
eqliscsiReplicantSiteOpsOperation = _EqliscsiReplicantSiteOpsOperation_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50, 1, 3),
    _EqliscsiReplicantSiteOpsOperation_Type()
)
eqliscsiReplicantSiteOpsOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsOperation.setStatus("current")


class _EqliscsiReplicantSiteOpsExec_Type(Integer32):
    """Custom type eqliscsiReplicantSiteOpsExec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 1),
          ("failed", 2),
          ("none", 0))
    )


_EqliscsiReplicantSiteOpsExec_Type.__name__ = "Integer32"
_EqliscsiReplicantSiteOpsExec_Object = MibTableColumn
eqliscsiReplicantSiteOpsExec = _EqliscsiReplicantSiteOpsExec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50, 1, 4),
    _EqliscsiReplicantSiteOpsExec_Type()
)
eqliscsiReplicantSiteOpsExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsExec.setStatus("current")
_EqliscsiReplicantSiteOpsStartTime_Type = Counter32
_EqliscsiReplicantSiteOpsStartTime_Object = MibTableColumn
eqliscsiReplicantSiteOpsStartTime = _EqliscsiReplicantSiteOpsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50, 1, 5),
    _EqliscsiReplicantSiteOpsStartTime_Type()
)
eqliscsiReplicantSiteOpsStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsStartTime.setStatus("current")


class _EqliscsiReplicantSiteOpsStoragePoolSourceIndex_Type(Unsigned32):
    """Custom type eqliscsiReplicantSiteOpsStoragePoolSourceIndex based on Unsigned32"""
    defaultValue = 1


_EqliscsiReplicantSiteOpsStoragePoolSourceIndex_Object = MibTableColumn
eqliscsiReplicantSiteOpsStoragePoolSourceIndex = _EqliscsiReplicantSiteOpsStoragePoolSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50, 1, 6),
    _EqliscsiReplicantSiteOpsStoragePoolSourceIndex_Type()
)
eqliscsiReplicantSiteOpsStoragePoolSourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsStoragePoolSourceIndex.setStatus("current")


class _EqliscsiReplicantSiteOpsStoragePoolDestinationIndex_Type(Unsigned32):
    """Custom type eqliscsiReplicantSiteOpsStoragePoolDestinationIndex based on Unsigned32"""
    defaultValue = 1


_EqliscsiReplicantSiteOpsStoragePoolDestinationIndex_Object = MibTableColumn
eqliscsiReplicantSiteOpsStoragePoolDestinationIndex = _EqliscsiReplicantSiteOpsStoragePoolDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50, 1, 7),
    _EqliscsiReplicantSiteOpsStoragePoolDestinationIndex_Type()
)
eqliscsiReplicantSiteOpsStoragePoolDestinationIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsStoragePoolDestinationIndex.setStatus("current")
_EqliscsiReplicantSiteOpsVolBalCommandIndex_Type = Unsigned32
_EqliscsiReplicantSiteOpsVolBalCommandIndex_Object = MibTableColumn
eqliscsiReplicantSiteOpsVolBalCommandIndex = _EqliscsiReplicantSiteOpsVolBalCommandIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50, 1, 8),
    _EqliscsiReplicantSiteOpsVolBalCommandIndex_Type()
)
eqliscsiReplicantSiteOpsVolBalCommandIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsVolBalCommandIndex.setStatus("current")
_EqliscsiReplicantSiteOpsVolBalCommandiscsiLocalMemberId_Type = Unsigned32
_EqliscsiReplicantSiteOpsVolBalCommandiscsiLocalMemberId_Object = MibTableColumn
eqliscsiReplicantSiteOpsVolBalCommandiscsiLocalMemberId = _EqliscsiReplicantSiteOpsVolBalCommandiscsiLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 50, 1, 9),
    _EqliscsiReplicantSiteOpsVolBalCommandiscsiLocalMemberId_Type()
)
eqliscsiReplicantSiteOpsVolBalCommandiscsiLocalMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsVolBalCommandiscsiLocalMemberId.setStatus("current")
_EqliscsiReplicantSiteOpsStatusTable_Object = MibTable
eqliscsiReplicantSiteOpsStatusTable = _EqliscsiReplicantSiteOpsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 51)
)
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsStatusTable.setStatus("current")
_EqliscsiReplicantSiteOpsStatusEntry_Object = MibTableRow
eqliscsiReplicantSiteOpsStatusEntry = _EqliscsiReplicantSiteOpsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 51, 1)
)
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsStatusEntry.setStatus("current")
_EqliscsiReplicantSiteOpsStatusCompletePct_Type = Unsigned32
_EqliscsiReplicantSiteOpsStatusCompletePct_Object = MibTableColumn
eqliscsiReplicantSiteOpsStatusCompletePct = _EqliscsiReplicantSiteOpsStatusCompletePct_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 51, 1, 1),
    _EqliscsiReplicantSiteOpsStatusCompletePct_Type()
)
eqliscsiReplicantSiteOpsStatusCompletePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteOpsStatusCompletePct.setStatus("current")
_EqliscsiReplicantSiteStatusTable_Object = MibTable
eqliscsiReplicantSiteStatusTable = _EqliscsiReplicantSiteStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 52)
)
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteStatusTable.setStatus("current")
_EqliscsiReplicantSiteStatusEntry_Object = MibTableRow
eqliscsiReplicantSiteStatusEntry = _EqliscsiReplicantSiteStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 52, 1)
)
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteStatusEntry.setStatus("current")


class _EqliscsiReplicantSiteStatusAvailable_Type(Integer32):
    """Custom type eqliscsiReplicantSiteStatusAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("not-available", 1))
    )


_EqliscsiReplicantSiteStatusAvailable_Type.__name__ = "Integer32"
_EqliscsiReplicantSiteStatusAvailable_Object = MibTableColumn
eqliscsiReplicantSiteStatusAvailable = _EqliscsiReplicantSiteStatusAvailable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 52, 1, 1),
    _EqliscsiReplicantSiteStatusAvailable_Type()
)
eqliscsiReplicantSiteStatusAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteStatusAvailable.setStatus("current")


class _EqliscsiReplicantSiteStatusMajorVersion_Type(Unsigned32):
    """Custom type eqliscsiReplicantSiteStatusMajorVersion based on Unsigned32"""
    defaultValue = 3


_EqliscsiReplicantSiteStatusMajorVersion_Object = MibTableColumn
eqliscsiReplicantSiteStatusMajorVersion = _EqliscsiReplicantSiteStatusMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 52, 1, 2),
    _EqliscsiReplicantSiteStatusMajorVersion_Type()
)
eqliscsiReplicantSiteStatusMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteStatusMajorVersion.setStatus("current")


class _EqliscsiReplicantSiteStatusMinorVersion_Type(Unsigned32):
    """Custom type eqliscsiReplicantSiteStatusMinorVersion based on Unsigned32"""
    defaultValue = 2


_EqliscsiReplicantSiteStatusMinorVersion_Object = MibTableColumn
eqliscsiReplicantSiteStatusMinorVersion = _EqliscsiReplicantSiteStatusMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 52, 1, 3),
    _EqliscsiReplicantSiteStatusMinorVersion_Type()
)
eqliscsiReplicantSiteStatusMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteStatusMinorVersion.setStatus("current")


class _EqliscsiReplicantSiteStatusMaintVersion_Type(Unsigned32):
    """Custom type eqliscsiReplicantSiteStatusMaintVersion based on Unsigned32"""
    defaultValue = 0


_EqliscsiReplicantSiteStatusMaintVersion_Object = MibTableColumn
eqliscsiReplicantSiteStatusMaintVersion = _EqliscsiReplicantSiteStatusMaintVersion_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 52, 1, 4),
    _EqliscsiReplicantSiteStatusMaintVersion_Type()
)
eqliscsiReplicantSiteStatusMaintVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiReplicantSiteStatusMaintVersion.setStatus("current")
_EqliscsiVolumeTaskStatusTable_Object = MibTable
eqliscsiVolumeTaskStatusTable = _EqliscsiVolumeTaskStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 53)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeTaskStatusTable.setStatus("current")
_EqliscsiVolumeTaskStatusEntry_Object = MibTableRow
eqliscsiVolumeTaskStatusEntry = _EqliscsiVolumeTaskStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 53, 1)
)
eqliscsiVolumeTaskStatusEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLGROUP-MIB", "eqlGroupTaskIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeTaskStatusEntry.setStatus("current")


class _EqliscsiVolumeTaskStatusErrorCode_Type(Unsigned32):
    """Custom type eqliscsiVolumeTaskStatusErrorCode based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolumeTaskStatusErrorCode_Object = MibTableColumn
eqliscsiVolumeTaskStatusErrorCode = _EqliscsiVolumeTaskStatusErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 53, 1, 1),
    _EqliscsiVolumeTaskStatusErrorCode_Type()
)
eqliscsiVolumeTaskStatusErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeTaskStatusErrorCode.setStatus("current")
_EqliscsiVolumeTemplateThinClonesTable_Object = MibTable
eqliscsiVolumeTemplateThinClonesTable = _EqliscsiVolumeTemplateThinClonesTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 54)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeTemplateThinClonesTable.setStatus("current")
_EqliscsiVolumeTemplateThinClonesEntry_Object = MibTableRow
eqliscsiVolumeTemplateThinClonesEntry = _EqliscsiVolumeTemplateThinClonesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 54, 1)
)
eqliscsiVolumeTemplateThinClonesEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiThinCloneLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiThinCloneVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeTemplateThinClonesEntry.setStatus("current")
_EqliscsiThinCloneLocalMemberId_Type = Unsigned32
_EqliscsiThinCloneLocalMemberId_Object = MibTableColumn
eqliscsiThinCloneLocalMemberId = _EqliscsiThinCloneLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 54, 1, 1),
    _EqliscsiThinCloneLocalMemberId_Type()
)
eqliscsiThinCloneLocalMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiThinCloneLocalMemberId.setStatus("current")
_EqliscsiThinCloneVolumeIndex_Type = Unsigned32
_EqliscsiThinCloneVolumeIndex_Object = MibTableColumn
eqliscsiThinCloneVolumeIndex = _EqliscsiThinCloneVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 54, 1, 2),
    _EqliscsiThinCloneVolumeIndex_Type()
)
eqliscsiThinCloneVolumeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiThinCloneVolumeIndex.setStatus("current")


class _EqliscsiVolumeTemplateThinClonesMember_Type(TruthValue):
    """Custom type eqliscsiVolumeTemplateThinClonesMember based on TruthValue"""


_EqliscsiVolumeTemplateThinClonesMember_Object = MibTableColumn
eqliscsiVolumeTemplateThinClonesMember = _EqliscsiVolumeTemplateThinClonesMember_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 54, 1, 3),
    _EqliscsiVolumeTemplateThinClonesMember_Type()
)
eqliscsiVolumeTemplateThinClonesMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeTemplateThinClonesMember.setStatus("current")
_EqliscsiVolumeAdminAccountTable_Object = MibTable
eqliscsiVolumeAdminAccountTable = _EqliscsiVolumeAdminAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 55)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeAdminAccountTable.setStatus("current")
_EqliscsiVolumeAdminAccountEntry_Object = MibTableRow
eqliscsiVolumeAdminAccountEntry = _EqliscsiVolumeAdminAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 55, 1)
)
eqliscsiVolumeAdminAccountEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeAdminAccountEntry.setStatus("current")
_EqliscsiVolumeAdminAccountRowStatus_Type = RowStatus
_EqliscsiVolumeAdminAccountRowStatus_Object = MibTableColumn
eqliscsiVolumeAdminAccountRowStatus = _EqliscsiVolumeAdminAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 55, 1, 1),
    _EqliscsiVolumeAdminAccountRowStatus_Type()
)
eqliscsiVolumeAdminAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeAdminAccountRowStatus.setStatus("current")
_EqliscsiTemplateVolumeStatusTable_Object = MibTable
eqliscsiTemplateVolumeStatusTable = _EqliscsiTemplateVolumeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 56)
)
if mibBuilder.loadTexts:
    eqliscsiTemplateVolumeStatusTable.setStatus("current")
_EqliscsiTemplateVolumeStatusEntry_Object = MibTableRow
eqliscsiTemplateVolumeStatusEntry = _EqliscsiTemplateVolumeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 56, 1)
)
if mibBuilder.loadTexts:
    eqliscsiTemplateVolumeStatusEntry.setStatus("current")
_EqliscsiTemplateVolumeStatusNumThinClones_Type = Unsigned32
_EqliscsiTemplateVolumeStatusNumThinClones_Object = MibTableColumn
eqliscsiTemplateVolumeStatusNumThinClones = _EqliscsiTemplateVolumeStatusNumThinClones_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 56, 1, 1),
    _EqliscsiTemplateVolumeStatusNumThinClones_Type()
)
eqliscsiTemplateVolumeStatusNumThinClones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiTemplateVolumeStatusNumThinClones.setStatus("current")
_EqliscsiTemplateVolumeStatusNumThinCloneReplicators_Type = Unsigned32
_EqliscsiTemplateVolumeStatusNumThinCloneReplicators_Object = MibTableColumn
eqliscsiTemplateVolumeStatusNumThinCloneReplicators = _EqliscsiTemplateVolumeStatusNumThinCloneReplicators_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 56, 1, 2),
    _EqliscsiTemplateVolumeStatusNumThinCloneReplicators_Type()
)
eqliscsiTemplateVolumeStatusNumThinCloneReplicators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiTemplateVolumeStatusNumThinCloneReplicators.setStatus("current")
_EqliscsiTemplateVolumeStatusNumThinCloneReplicaSets_Type = Unsigned32
_EqliscsiTemplateVolumeStatusNumThinCloneReplicaSets_Object = MibTableColumn
eqliscsiTemplateVolumeStatusNumThinCloneReplicaSets = _EqliscsiTemplateVolumeStatusNumThinCloneReplicaSets_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 56, 1, 3),
    _EqliscsiTemplateVolumeStatusNumThinCloneReplicaSets_Type()
)
eqliscsiTemplateVolumeStatusNumThinCloneReplicaSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiTemplateVolumeStatusNumThinCloneReplicaSets.setStatus("current")
_EqliscsiSnapAccumulatedStatisticsTable_Object = MibTable
eqliscsiSnapAccumulatedStatisticsTable = _EqliscsiSnapAccumulatedStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57)
)
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatisticsTable.setStatus("current")
_EqliscsiSnapAccumulatedStatisticsEntry_Object = MibTableRow
eqliscsiSnapAccumulatedStatisticsEntry = _EqliscsiSnapAccumulatedStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1)
)
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatisticsEntry.setStatus("current")
_EqliscsiSnapAccumulatedStatsCmdPdus_Type = Counter32
_EqliscsiSnapAccumulatedStatsCmdPdus_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsCmdPdus = _EqliscsiSnapAccumulatedStatsCmdPdus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 1),
    _EqliscsiSnapAccumulatedStatsCmdPdus_Type()
)
eqliscsiSnapAccumulatedStatsCmdPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsCmdPdus.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsCmdPdus.setUnits("PDUs")
_EqliscsiSnapAccumulatedStatsRspPdus_Type = Counter32
_EqliscsiSnapAccumulatedStatsRspPdus_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsRspPdus = _EqliscsiSnapAccumulatedStatsRspPdus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 2),
    _EqliscsiSnapAccumulatedStatsRspPdus_Type()
)
eqliscsiSnapAccumulatedStatsRspPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsRspPdus.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsRspPdus.setUnits("PDUs")
_EqliscsiSnapAccumulatedStatsTxData_Type = Counter64
_EqliscsiSnapAccumulatedStatsTxData_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsTxData = _EqliscsiSnapAccumulatedStatsTxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 3),
    _EqliscsiSnapAccumulatedStatsTxData_Type()
)
eqliscsiSnapAccumulatedStatsTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsTxData.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsTxData.setUnits("octets")
_EqliscsiSnapAccumulatedStatsRxData_Type = Counter64
_EqliscsiSnapAccumulatedStatsRxData_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsRxData = _EqliscsiSnapAccumulatedStatsRxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 4),
    _EqliscsiSnapAccumulatedStatsRxData_Type()
)
eqliscsiSnapAccumulatedStatsRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsRxData.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsRxData.setUnits("octets")
_EqliscsiSnapAccumulatedStatsNoOfSessions_Type = Unsigned32
_EqliscsiSnapAccumulatedStatsNoOfSessions_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsNoOfSessions = _EqliscsiSnapAccumulatedStatsNoOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 5),
    _EqliscsiSnapAccumulatedStatsNoOfSessions_Type()
)
eqliscsiSnapAccumulatedStatsNoOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsNoOfSessions.setStatus("current")
_EqliscsiSnapAccumulatedStatsReadLatency_Type = Counter64
_EqliscsiSnapAccumulatedStatsReadLatency_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsReadLatency = _EqliscsiSnapAccumulatedStatsReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 6),
    _EqliscsiSnapAccumulatedStatsReadLatency_Type()
)
eqliscsiSnapAccumulatedStatsReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsReadLatency.setStatus("current")
_EqliscsiSnapAccumulatedStatsWriteLatency_Type = Counter64
_EqliscsiSnapAccumulatedStatsWriteLatency_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsWriteLatency = _EqliscsiSnapAccumulatedStatsWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 7),
    _EqliscsiSnapAccumulatedStatsWriteLatency_Type()
)
eqliscsiSnapAccumulatedStatsWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsWriteLatency.setStatus("current")
_EqliscsiSnapAccumulatedStatsReadOpCount_Type = Counter64
_EqliscsiSnapAccumulatedStatsReadOpCount_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsReadOpCount = _EqliscsiSnapAccumulatedStatsReadOpCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 8),
    _EqliscsiSnapAccumulatedStatsReadOpCount_Type()
)
eqliscsiSnapAccumulatedStatsReadOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsReadOpCount.setStatus("current")
_EqliscsiSnapAccumulatedStatsWriteOpCount_Type = Counter64
_EqliscsiSnapAccumulatedStatsWriteOpCount_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsWriteOpCount = _EqliscsiSnapAccumulatedStatsWriteOpCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 9),
    _EqliscsiSnapAccumulatedStatsWriteOpCount_Type()
)
eqliscsiSnapAccumulatedStatsWriteOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsWriteOpCount.setStatus("current")
_EqliscsiSnapAccumulatedStatsReadAvgLatency_Type = Gauge32
_EqliscsiSnapAccumulatedStatsReadAvgLatency_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsReadAvgLatency = _EqliscsiSnapAccumulatedStatsReadAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 10),
    _EqliscsiSnapAccumulatedStatsReadAvgLatency_Type()
)
eqliscsiSnapAccumulatedStatsReadAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsReadAvgLatency.setStatus("current")
_EqliscsiSnapAccumulatedStatsWriteAvgLatency_Type = Gauge32
_EqliscsiSnapAccumulatedStatsWriteAvgLatency_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsWriteAvgLatency = _EqliscsiSnapAccumulatedStatsWriteAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 11),
    _EqliscsiSnapAccumulatedStatsWriteAvgLatency_Type()
)
eqliscsiSnapAccumulatedStatsWriteAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsWriteAvgLatency.setStatus("current")
_EqliscsiSnapAccumulatedStatsIscsiReadWriteCmdsReceived_Type = Counter64
_EqliscsiSnapAccumulatedStatsIscsiReadWriteCmdsReceived_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsIscsiReadWriteCmdsReceived = _EqliscsiSnapAccumulatedStatsIscsiReadWriteCmdsReceived_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 12),
    _EqliscsiSnapAccumulatedStatsIscsiReadWriteCmdsReceived_Type()
)
eqliscsiSnapAccumulatedStatsIscsiReadWriteCmdsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsIscsiReadWriteCmdsReceived.setStatus("current")
_EqliscsiSnapAccumulatedStatsIscsiTotalQD_Type = Counter64
_EqliscsiSnapAccumulatedStatsIscsiTotalQD_Object = MibTableColumn
eqliscsiSnapAccumulatedStatsIscsiTotalQD = _EqliscsiSnapAccumulatedStatsIscsiTotalQD_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 57, 1, 13),
    _EqliscsiSnapAccumulatedStatsIscsiTotalQD_Type()
)
eqliscsiSnapAccumulatedStatsIscsiTotalQD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSnapAccumulatedStatsIscsiTotalQD.setStatus("current")
_EqliscsiVolumeReplSiteAdminAccountTable_Object = MibTable
eqliscsiVolumeReplSiteAdminAccountTable = _EqliscsiVolumeReplSiteAdminAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 58)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteAdminAccountTable.setStatus("current")
_EqliscsiVolumeReplSiteAdminAccountEntry_Object = MibTableRow
eqliscsiVolumeReplSiteAdminAccountEntry = _EqliscsiVolumeReplSiteAdminAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 58, 1)
)
eqliscsiVolumeReplSiteAdminAccountEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
    (0, "EQLGROUP-MIB", "eqlStorageGroupAdminAccountIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteAdminAccountEntry.setStatus("current")
_EqliscsiVolumeReplSiteAdminAccountRowStatus_Type = RowStatus
_EqliscsiVolumeReplSiteAdminAccountRowStatus_Object = MibTableColumn
eqliscsiVolumeReplSiteAdminAccountRowStatus = _EqliscsiVolumeReplSiteAdminAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 58, 1, 1),
    _EqliscsiVolumeReplSiteAdminAccountRowStatus_Type()
)
eqliscsiVolumeReplSiteAdminAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteAdminAccountRowStatus.setStatus("current")
_EqliscsiVolumeReplSiteAdminAccountQuotaType_Type = ReplSiteQuotaType
_EqliscsiVolumeReplSiteAdminAccountQuotaType_Object = MibTableColumn
eqliscsiVolumeReplSiteAdminAccountQuotaType = _EqliscsiVolumeReplSiteAdminAccountQuotaType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 58, 1, 2),
    _EqliscsiVolumeReplSiteAdminAccountQuotaType_Type()
)
eqliscsiVolumeReplSiteAdminAccountQuotaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteAdminAccountQuotaType.setStatus("current")
_EqliscsiVolumeReplSiteAdminAccountQuota_Type = Unsigned32
_EqliscsiVolumeReplSiteAdminAccountQuota_Object = MibTableColumn
eqliscsiVolumeReplSiteAdminAccountQuota = _EqliscsiVolumeReplSiteAdminAccountQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 58, 1, 3),
    _EqliscsiVolumeReplSiteAdminAccountQuota_Type()
)
eqliscsiVolumeReplSiteAdminAccountQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeReplSiteAdminAccountQuota.setStatus("current")
_EqlLdapLoginAccessReplSiteTable_Object = MibTable
eqlLdapLoginAccessReplSiteTable = _EqlLdapLoginAccessReplSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 59)
)
if mibBuilder.loadTexts:
    eqlLdapLoginAccessReplSiteTable.setStatus("current")
_EqlLdapLoginAccessReplSiteEntry_Object = MibTableRow
eqlLdapLoginAccessReplSiteEntry = _EqlLdapLoginAccessReplSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 59, 1)
)
eqlLdapLoginAccessReplSiteEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLGROUP-MIB", "eqlLdapLoginAccessType"),
    (0, "EQLGROUP-MIB", "eqlLdapLoginAccessName"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
)
if mibBuilder.loadTexts:
    eqlLdapLoginAccessReplSiteEntry.setStatus("current")
_EqlLdapLoginAccessReplSiteQuotaType_Type = ReplSiteQuotaType
_EqlLdapLoginAccessReplSiteQuotaType_Object = MibTableColumn
eqlLdapLoginAccessReplSiteQuotaType = _EqlLdapLoginAccessReplSiteQuotaType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 59, 1, 1),
    _EqlLdapLoginAccessReplSiteQuotaType_Type()
)
eqlLdapLoginAccessReplSiteQuotaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessReplSiteQuotaType.setStatus("current")
_EqlLdapLoginAccessReplSiteQuota_Type = Unsigned32
_EqlLdapLoginAccessReplSiteQuota_Object = MibTableColumn
eqlLdapLoginAccessReplSiteQuota = _EqlLdapLoginAccessReplSiteQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 59, 1, 2),
    _EqlLdapLoginAccessReplSiteQuota_Type()
)
eqlLdapLoginAccessReplSiteQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessReplSiteQuota.setStatus("current")
_EqlLdapLoginAccessReplSiteRowStatus_Type = RowStatus
_EqlLdapLoginAccessReplSiteRowStatus_Object = MibTableColumn
eqlLdapLoginAccessReplSiteRowStatus = _EqlLdapLoginAccessReplSiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 59, 1, 3),
    _EqlLdapLoginAccessReplSiteRowStatus_Type()
)
eqlLdapLoginAccessReplSiteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlLdapLoginAccessReplSiteRowStatus.setStatus("current")
_EqliscsiVolumeSyncReplExtensionTable_Object = MibTable
eqliscsiVolumeSyncReplExtensionTable = _EqliscsiVolumeSyncReplExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 60)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplExtensionTable.setStatus("current")
_EqliscsiVolumeSyncReplExtensionEntry_Object = MibTableRow
eqliscsiVolumeSyncReplExtensionEntry = _EqliscsiVolumeSyncReplExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 60, 1)
)
eqliscsiVolumeSyncReplExtensionEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplExtensionEntry.setStatus("current")
_EqliscsiVolumeSyncReplExtRowStatus_Type = RowStatus
_EqliscsiVolumeSyncReplExtRowStatus_Object = MibTableColumn
eqliscsiVolumeSyncReplExtRowStatus = _EqliscsiVolumeSyncReplExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 60, 1, 1),
    _EqliscsiVolumeSyncReplExtRowStatus_Type()
)
eqliscsiVolumeSyncReplExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplExtRowStatus.setStatus("current")
_EqliscsiVolumeSyncReplExtSyncReplLocalMemberId_Type = Unsigned32
_EqliscsiVolumeSyncReplExtSyncReplLocalMemberId_Object = MibTableColumn
eqliscsiVolumeSyncReplExtSyncReplLocalMemberId = _EqliscsiVolumeSyncReplExtSyncReplLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 60, 1, 2),
    _EqliscsiVolumeSyncReplExtSyncReplLocalMemberId_Type()
)
eqliscsiVolumeSyncReplExtSyncReplLocalMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplExtSyncReplLocalMemberId.setStatus("current")
_EqliscsiVolumeSyncReplExtSyncReplIndex_Type = Unsigned32
_EqliscsiVolumeSyncReplExtSyncReplIndex_Object = MibTableColumn
eqliscsiVolumeSyncReplExtSyncReplIndex = _EqliscsiVolumeSyncReplExtSyncReplIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 60, 1, 3),
    _EqliscsiVolumeSyncReplExtSyncReplIndex_Type()
)
eqliscsiVolumeSyncReplExtSyncReplIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplExtSyncReplIndex.setStatus("current")


class _EqliscsiVolumeSyncReplExtIntTargetIscsiName_Type(OctetString):
    """Custom type eqliscsiVolumeSyncReplExtIntTargetIscsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 223),
    )


_EqliscsiVolumeSyncReplExtIntTargetIscsiName_Type.__name__ = "OctetString"
_EqliscsiVolumeSyncReplExtIntTargetIscsiName_Object = MibTableColumn
eqliscsiVolumeSyncReplExtIntTargetIscsiName = _EqliscsiVolumeSyncReplExtIntTargetIscsiName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 60, 1, 4),
    _EqliscsiVolumeSyncReplExtIntTargetIscsiName_Type()
)
eqliscsiVolumeSyncReplExtIntTargetIscsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplExtIntTargetIscsiName.setStatus("current")
_EqliscsiVolumeSyncReplTable_Object = MibTable
eqliscsiVolumeSyncReplTable = _EqliscsiVolumeSyncReplTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 61)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplTable.setStatus("current")
_EqliscsiVolumeSyncReplEntry_Object = MibTableRow
eqliscsiVolumeSyncReplEntry = _EqliscsiVolumeSyncReplEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 61, 1)
)
eqliscsiVolumeSyncReplEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeSyncReplLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeSyncReplIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplEntry.setStatus("current")
_EqliscsiVolumeSyncReplRowStatus_Type = RowStatus
_EqliscsiVolumeSyncReplRowStatus_Object = MibTableColumn
eqliscsiVolumeSyncReplRowStatus = _EqliscsiVolumeSyncReplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 61, 1, 1),
    _EqliscsiVolumeSyncReplRowStatus_Type()
)
eqliscsiVolumeSyncReplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplRowStatus.setStatus("current")
_EqliscsiVolumeSyncReplLocalMemberId_Type = Unsigned32
_EqliscsiVolumeSyncReplLocalMemberId_Object = MibTableColumn
eqliscsiVolumeSyncReplLocalMemberId = _EqliscsiVolumeSyncReplLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 61, 1, 2),
    _EqliscsiVolumeSyncReplLocalMemberId_Type()
)
eqliscsiVolumeSyncReplLocalMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplLocalMemberId.setStatus("current")
_EqliscsiVolumeSyncReplIndex_Type = Unsigned32
_EqliscsiVolumeSyncReplIndex_Object = MibTableColumn
eqliscsiVolumeSyncReplIndex = _EqliscsiVolumeSyncReplIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 61, 1, 3),
    _EqliscsiVolumeSyncReplIndex_Type()
)
eqliscsiVolumeSyncReplIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplIndex.setStatus("current")


class _EqliscsiVolumeSyncReplPaused_Type(TruthValue):
    """Custom type eqliscsiVolumeSyncReplPaused based on TruthValue"""


_EqliscsiVolumeSyncReplPaused_Object = MibTableColumn
eqliscsiVolumeSyncReplPaused = _EqliscsiVolumeSyncReplPaused_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 61, 1, 4),
    _EqliscsiVolumeSyncReplPaused_Type()
)
eqliscsiVolumeSyncReplPaused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplPaused.setStatus("current")
_EqliscsiVolumeSyncReplPeerTable_Object = MibTable
eqliscsiVolumeSyncReplPeerTable = _EqliscsiVolumeSyncReplPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 62)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplPeerTable.setStatus("current")
_EqliscsiVolumeSyncReplPeerEntry_Object = MibTableRow
eqliscsiVolumeSyncReplPeerEntry = _EqliscsiVolumeSyncReplPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 62, 1)
)
eqliscsiVolumeSyncReplPeerEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeSyncReplPeerLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeSyncReplPeerVolIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplPeerEntry.setStatus("current")
_EqliscsiVolumeSyncReplPeerLocalMemberId_Type = Unsigned32
_EqliscsiVolumeSyncReplPeerLocalMemberId_Object = MibTableColumn
eqliscsiVolumeSyncReplPeerLocalMemberId = _EqliscsiVolumeSyncReplPeerLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 62, 1, 1),
    _EqliscsiVolumeSyncReplPeerLocalMemberId_Type()
)
eqliscsiVolumeSyncReplPeerLocalMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplPeerLocalMemberId.setStatus("current")
_EqliscsiVolumeSyncReplPeerVolIndex_Type = Unsigned32
_EqliscsiVolumeSyncReplPeerVolIndex_Object = MibTableColumn
eqliscsiVolumeSyncReplPeerVolIndex = _EqliscsiVolumeSyncReplPeerVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 62, 1, 2),
    _EqliscsiVolumeSyncReplPeerVolIndex_Type()
)
eqliscsiVolumeSyncReplPeerVolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplPeerVolIndex.setStatus("current")


class _EqliscsiVolumeSyncReplPeerPsvId_Type(OctetString):
    """Custom type eqliscsiVolumeSyncReplPeerPsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiVolumeSyncReplPeerPsvId_Type.__name__ = "OctetString"
_EqliscsiVolumeSyncReplPeerPsvId_Object = MibTableColumn
eqliscsiVolumeSyncReplPeerPsvId = _EqliscsiVolumeSyncReplPeerPsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 62, 1, 3),
    _EqliscsiVolumeSyncReplPeerPsvId_Type()
)
eqliscsiVolumeSyncReplPeerPsvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplPeerPsvId.setStatus("current")
_EqliscsiVolumeSyncReplStatusTable_Object = MibTable
eqliscsiVolumeSyncReplStatusTable = _EqliscsiVolumeSyncReplStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 63)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplStatusTable.setStatus("current")
_EqliscsiVolumeSyncReplStatusEntry_Object = MibTableRow
eqliscsiVolumeSyncReplStatusEntry = _EqliscsiVolumeSyncReplStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 63, 1)
)
eqliscsiVolumeSyncReplStatusEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplStatusEntry.setStatus("current")


class _EqliscsiVolumeSyncReplStatusSyncStatus_Type(Integer32):
    """Custom type eqliscsiVolumeSyncReplStatusSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("in-sync", 1),
          ("out-of-sync", 2),
          ("out-of-sync-due-to-alt-pool-lost-blocks", 7),
          ("out-of-sync-due-to-member-offline", 5),
          ("out-of-sync-due-to-no-pool-space-for-auto-grow", 6),
          ("out-of-sync-due-to-paused", 3),
          ("out-of-sync-due-to-snap-reserve-met", 4))
    )


_EqliscsiVolumeSyncReplStatusSyncStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeSyncReplStatusSyncStatus_Object = MibTableColumn
eqliscsiVolumeSyncReplStatusSyncStatus = _EqliscsiVolumeSyncReplStatusSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 63, 1, 1),
    _EqliscsiVolumeSyncReplStatusSyncStatus_Type()
)
eqliscsiVolumeSyncReplStatusSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplStatusSyncStatus.setStatus("current")


class _EqliscsiVolumeSyncReplStatusUnreplicatedChanges_Type(Integer32):
    """Custom type eqliscsiVolumeSyncReplStatusUnreplicatedChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 3),
          ("yes", 1))
    )


_EqliscsiVolumeSyncReplStatusUnreplicatedChanges_Type.__name__ = "Integer32"
_EqliscsiVolumeSyncReplStatusUnreplicatedChanges_Object = MibTableColumn
eqliscsiVolumeSyncReplStatusUnreplicatedChanges = _EqliscsiVolumeSyncReplStatusUnreplicatedChanges_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 63, 1, 2),
    _EqliscsiVolumeSyncReplStatusUnreplicatedChanges_Type()
)
eqliscsiVolumeSyncReplStatusUnreplicatedChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplStatusUnreplicatedChanges.setStatus("current")
_EqliscsiVolumeSyncReplStatusTotalTxDataMB_Type = Unsigned32
_EqliscsiVolumeSyncReplStatusTotalTxDataMB_Object = MibTableColumn
eqliscsiVolumeSyncReplStatusTotalTxDataMB = _EqliscsiVolumeSyncReplStatusTotalTxDataMB_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 63, 1, 3),
    _EqliscsiVolumeSyncReplStatusTotalTxDataMB_Type()
)
eqliscsiVolumeSyncReplStatusTotalTxDataMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplStatusTotalTxDataMB.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplStatusTotalTxDataMB.setUnits("MB")
_EqliscsiVolumeSyncReplStatusRemainingTxDataMB_Type = Unsigned32
_EqliscsiVolumeSyncReplStatusRemainingTxDataMB_Object = MibTableColumn
eqliscsiVolumeSyncReplStatusRemainingTxDataMB = _EqliscsiVolumeSyncReplStatusRemainingTxDataMB_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 63, 1, 4),
    _EqliscsiVolumeSyncReplStatusRemainingTxDataMB_Type()
)
eqliscsiVolumeSyncReplStatusRemainingTxDataMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplStatusRemainingTxDataMB.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplStatusRemainingTxDataMB.setUnits("MB")
_EqliscsiVolumeSyncReplVirtualTable_Object = MibTable
eqliscsiVolumeSyncReplVirtualTable = _EqliscsiVolumeSyncReplVirtualTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 64)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualTable.setStatus("current")
_EqliscsiVolumeSyncReplVirtualEntry_Object = MibTableRow
eqliscsiVolumeSyncReplVirtualEntry = _EqliscsiVolumeSyncReplVirtualEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 64, 1)
)
eqliscsiVolumeSyncReplVirtualEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualEntry.setStatus("current")


class _EqliscsiVolumeSyncReplVirtualAccessType_Type(Integer32):
    """Custom type eqliscsiVolumeSyncReplVirtualAccessType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 2),
          ("read-write", 1))
    )


_EqliscsiVolumeSyncReplVirtualAccessType_Type.__name__ = "Integer32"
_EqliscsiVolumeSyncReplVirtualAccessType_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualAccessType = _EqliscsiVolumeSyncReplVirtualAccessType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 64, 1, 1),
    _EqliscsiVolumeSyncReplVirtualAccessType_Type()
)
eqliscsiVolumeSyncReplVirtualAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualAccessType.setStatus("current")


class _EqliscsiVolumeSyncReplVirtualAdminStatus_Type(Integer32):
    """Custom type eqliscsiVolumeSyncReplVirtualAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("online-lost-cached-blocks", 3))
    )


_EqliscsiVolumeSyncReplVirtualAdminStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeSyncReplVirtualAdminStatus_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualAdminStatus = _EqliscsiVolumeSyncReplVirtualAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 64, 1, 2),
    _EqliscsiVolumeSyncReplVirtualAdminStatus_Type()
)
eqliscsiVolumeSyncReplVirtualAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualAdminStatus.setStatus("current")


class _EqliscsiVolumeSyncReplVirtualMultInitiator_Type(Integer32):
    """Custom type eqliscsiVolumeSyncReplVirtualMultInitiator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 0),
          ("not-allowed", 1))
    )


_EqliscsiVolumeSyncReplVirtualMultInitiator_Type.__name__ = "Integer32"
_EqliscsiVolumeSyncReplVirtualMultInitiator_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualMultInitiator = _EqliscsiVolumeSyncReplVirtualMultInitiator_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 64, 1, 3),
    _EqliscsiVolumeSyncReplVirtualMultInitiator_Type()
)
eqliscsiVolumeSyncReplVirtualMultInitiator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualMultInitiator.setStatus("current")
_EqliscsiVolumeSyncReplVirtualStatusTable_Object = MibTable
eqliscsiVolumeSyncReplVirtualStatusTable = _EqliscsiVolumeSyncReplVirtualStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 65)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusTable.setStatus("current")
_EqliscsiVolumeSyncReplVirtualStatusEntry_Object = MibTableRow
eqliscsiVolumeSyncReplVirtualStatusEntry = _EqliscsiVolumeSyncReplVirtualStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 65, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusEntry.setStatus("current")
_EqliscsiVolumeSyncReplVirtualStatusReservedSpace_Type = Integer32
_EqliscsiVolumeSyncReplVirtualStatusReservedSpace_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualStatusReservedSpace = _EqliscsiVolumeSyncReplVirtualStatusReservedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 65, 1, 1),
    _EqliscsiVolumeSyncReplVirtualStatusReservedSpace_Type()
)
eqliscsiVolumeSyncReplVirtualStatusReservedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusReservedSpace.setStatus("current")


class _EqliscsiVolumeSyncReplVirtualStatusReservedSpaceAvail_Type(Integer32):
    """Custom type eqliscsiVolumeSyncReplVirtualStatusReservedSpaceAvail based on Integer32"""
    defaultValue = 0


_EqliscsiVolumeSyncReplVirtualStatusReservedSpaceAvail_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualStatusReservedSpaceAvail = _EqliscsiVolumeSyncReplVirtualStatusReservedSpaceAvail_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 65, 1, 2),
    _EqliscsiVolumeSyncReplVirtualStatusReservedSpaceAvail_Type()
)
eqliscsiVolumeSyncReplVirtualStatusReservedSpaceAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusReservedSpaceAvail.setStatus("current")
_EqliscsiVolumeSyncReplVirtualStatusNumSnapshots_Type = Integer32
_EqliscsiVolumeSyncReplVirtualStatusNumSnapshots_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualStatusNumSnapshots = _EqliscsiVolumeSyncReplVirtualStatusNumSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 65, 1, 3),
    _EqliscsiVolumeSyncReplVirtualStatusNumSnapshots_Type()
)
eqliscsiVolumeSyncReplVirtualStatusNumSnapshots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusNumSnapshots.setStatus("current")


class _EqliscsiVolumeSyncReplVirtualStatusOperStatus_Type(Integer32):
    """Custom type eqliscsiVolumeSyncReplVirtualStatusOperStatus based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("available-no-new-connections", 10),
          ("not-available", 2),
          ("not-available-due-to-internal-error", 11),
          ("not-available-due-to-lost-cached-blocks", 5),
          ("not-available-due-to-members-offline", 4),
          ("not-available-due-to-missing-pages", 8),
          ("not-available-due-to-nospace-for-auto-grow", 7),
          ("not-available-due-to-snap-reserve-met", 3),
          ("not-available-due-to-syncrep", 9),
          ("not-available-due-to-thin-max-growth-met", 6))
    )


_EqliscsiVolumeSyncReplVirtualStatusOperStatus_Type.__name__ = "Integer32"
_EqliscsiVolumeSyncReplVirtualStatusOperStatus_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualStatusOperStatus = _EqliscsiVolumeSyncReplVirtualStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 65, 1, 4),
    _EqliscsiVolumeSyncReplVirtualStatusOperStatus_Type()
)
eqliscsiVolumeSyncReplVirtualStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusOperStatus.setStatus("current")
_EqliscsiVolumeSyncReplVirtualStatusConnections_Type = Integer32
_EqliscsiVolumeSyncReplVirtualStatusConnections_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualStatusConnections = _EqliscsiVolumeSyncReplVirtualStatusConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 65, 1, 5),
    _EqliscsiVolumeSyncReplVirtualStatusConnections_Type()
)
eqliscsiVolumeSyncReplVirtualStatusConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusConnections.setStatus("current")
_EqliscsiVolumeSyncReplVirtualStatusAllocatedSpace_Type = Unsigned32
_EqliscsiVolumeSyncReplVirtualStatusAllocatedSpace_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualStatusAllocatedSpace = _EqliscsiVolumeSyncReplVirtualStatusAllocatedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 65, 1, 6),
    _EqliscsiVolumeSyncReplVirtualStatusAllocatedSpace_Type()
)
eqliscsiVolumeSyncReplVirtualStatusAllocatedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusAllocatedSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusAllocatedSpace.setUnits("MB")
_EqliscsiVolumeSyncReplVirtualStatusVolReserveSpace_Type = Unsigned32
_EqliscsiVolumeSyncReplVirtualStatusVolReserveSpace_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualStatusVolReserveSpace = _EqliscsiVolumeSyncReplVirtualStatusVolReserveSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 65, 1, 7),
    _EqliscsiVolumeSyncReplVirtualStatusVolReserveSpace_Type()
)
eqliscsiVolumeSyncReplVirtualStatusVolReserveSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusVolReserveSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusVolReserveSpace.setUnits("MB")
_EqliscsiVolumeSyncReplVirtualStatusExtConnections_Type = Integer32
_EqliscsiVolumeSyncReplVirtualStatusExtConnections_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualStatusExtConnections = _EqliscsiVolumeSyncReplVirtualStatusExtConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 65, 1, 8),
    _EqliscsiVolumeSyncReplVirtualStatusExtConnections_Type()
)
eqliscsiVolumeSyncReplVirtualStatusExtConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatusExtConnections.setStatus("current")
_EqliscsiVolumeSyncReplVirtualStatisticsTable_Object = MibTable
eqliscsiVolumeSyncReplVirtualStatisticsTable = _EqliscsiVolumeSyncReplVirtualStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 66)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatisticsTable.setStatus("current")
_EqliscsiVolumeSyncReplVirtualStatisticsEntry_Object = MibTableRow
eqliscsiVolumeSyncReplVirtualStatisticsEntry = _EqliscsiVolumeSyncReplVirtualStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 66, 1)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatisticsEntry.setStatus("current")
_EqliscsiVolumeSyncReplVirtualStatsTxData_Type = Counter64
_EqliscsiVolumeSyncReplVirtualStatsTxData_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualStatsTxData = _EqliscsiVolumeSyncReplVirtualStatsTxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 66, 1, 1),
    _EqliscsiVolumeSyncReplVirtualStatsTxData_Type()
)
eqliscsiVolumeSyncReplVirtualStatsTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatsTxData.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatsTxData.setUnits("octets")
_EqliscsiVolumeSyncReplVirtualStatsRxData_Type = Counter64
_EqliscsiVolumeSyncReplVirtualStatsRxData_Object = MibTableColumn
eqliscsiVolumeSyncReplVirtualStatsRxData = _EqliscsiVolumeSyncReplVirtualStatsRxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 66, 1, 2),
    _EqliscsiVolumeSyncReplVirtualStatsRxData_Type()
)
eqliscsiVolumeSyncReplVirtualStatsRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatsRxData.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplVirtualStatsRxData.setUnits("octets")
_EqliscsiVsrVirtualSyncReplStatusTable_Object = MibTable
eqliscsiVsrVirtualSyncReplStatusTable = _EqliscsiVsrVirtualSyncReplStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 67)
)
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplStatusTable.setStatus("current")
_EqliscsiVsrVirtualSyncReplStatusEntry_Object = MibTableRow
eqliscsiVsrVirtualSyncReplStatusEntry = _EqliscsiVsrVirtualSyncReplStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 67, 1)
)
eqliscsiVsrVirtualSyncReplStatusEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplStatusEntry.setStatus("current")


class _EqliscsiVsrVirtualSyncReplStatusSyncStatus_Type(Integer32):
    """Custom type eqliscsiVsrVirtualSyncReplStatusSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("in-sync", 1),
          ("out-of-sync", 2),
          ("out-of-sync-due-to-alt-pool-lost-blocks", 7),
          ("out-of-sync-due-to-member-offline", 5),
          ("out-of-sync-due-to-no-pool-space-for-auto-grow", 6),
          ("out-of-sync-due-to-paused", 3),
          ("out-of-sync-due-to-snap-reserve-met", 4))
    )


_EqliscsiVsrVirtualSyncReplStatusSyncStatus_Type.__name__ = "Integer32"
_EqliscsiVsrVirtualSyncReplStatusSyncStatus_Object = MibTableColumn
eqliscsiVsrVirtualSyncReplStatusSyncStatus = _EqliscsiVsrVirtualSyncReplStatusSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 67, 1, 1),
    _EqliscsiVsrVirtualSyncReplStatusSyncStatus_Type()
)
eqliscsiVsrVirtualSyncReplStatusSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplStatusSyncStatus.setStatus("current")


class _EqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges_Type(Integer32):
    """Custom type eqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 3),
          ("yes", 1))
    )


_EqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges_Type.__name__ = "Integer32"
_EqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges_Object = MibTableColumn
eqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges = _EqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 67, 1, 2),
    _EqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges_Type()
)
eqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges.setStatus("current")
_EqliscsiVsrVirtualSyncReplStatusTotalTxDataMB_Type = Unsigned32
_EqliscsiVsrVirtualSyncReplStatusTotalTxDataMB_Object = MibTableColumn
eqliscsiVsrVirtualSyncReplStatusTotalTxDataMB = _EqliscsiVsrVirtualSyncReplStatusTotalTxDataMB_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 67, 1, 3),
    _EqliscsiVsrVirtualSyncReplStatusTotalTxDataMB_Type()
)
eqliscsiVsrVirtualSyncReplStatusTotalTxDataMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplStatusTotalTxDataMB.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplStatusTotalTxDataMB.setUnits("MB")
_EqliscsiVsrVirtualSyncReplStatusRemainingTxDataMB_Type = Unsigned32
_EqliscsiVsrVirtualSyncReplStatusRemainingTxDataMB_Object = MibTableColumn
eqliscsiVsrVirtualSyncReplStatusRemainingTxDataMB = _EqliscsiVsrVirtualSyncReplStatusRemainingTxDataMB_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 67, 1, 4),
    _EqliscsiVsrVirtualSyncReplStatusRemainingTxDataMB_Type()
)
eqliscsiVsrVirtualSyncReplStatusRemainingTxDataMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplStatusRemainingTxDataMB.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplStatusRemainingTxDataMB.setUnits("MB")
_EqliscsiSyncReplAfoStateTable_Object = MibTable
eqliscsiSyncReplAfoStateTable = _EqliscsiSyncReplAfoStateTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 68)
)
if mibBuilder.loadTexts:
    eqliscsiSyncReplAfoStateTable.setStatus("current")
_EqliscsiSyncReplAfoStateEntry_Object = MibTableRow
eqliscsiSyncReplAfoStateEntry = _EqliscsiSyncReplAfoStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 68, 1)
)
eqliscsiSyncReplAfoStateEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId0"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId1"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId2"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId3"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId0"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId1"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId2"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId3"),
)
if mibBuilder.loadTexts:
    eqliscsiSyncReplAfoStateEntry.setStatus("current")
_EqliscsiSyncReplAfoSeqNum_Type = Unsigned32
_EqliscsiSyncReplAfoSeqNum_Object = MibTableColumn
eqliscsiSyncReplAfoSeqNum = _EqliscsiSyncReplAfoSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 68, 1, 1),
    _EqliscsiSyncReplAfoSeqNum_Type()
)
eqliscsiSyncReplAfoSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSyncReplAfoSeqNum.setStatus("current")
_EqliscsiSyncReplAfoState_Type = Unsigned32
_EqliscsiSyncReplAfoState_Object = MibTableColumn
eqliscsiSyncReplAfoState = _EqliscsiSyncReplAfoState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 68, 1, 2),
    _EqliscsiSyncReplAfoState_Type()
)
eqliscsiSyncReplAfoState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSyncReplAfoState.setStatus("current")


class _EqliscsiSyncReplAfoGrpLeadUuid_Type(OctetString):
    """Custom type eqliscsiSyncReplAfoGrpLeadUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiSyncReplAfoGrpLeadUuid_Type.__name__ = "OctetString"
_EqliscsiSyncReplAfoGrpLeadUuid_Object = MibTableColumn
eqliscsiSyncReplAfoGrpLeadUuid = _EqliscsiSyncReplAfoGrpLeadUuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 68, 1, 3),
    _EqliscsiSyncReplAfoGrpLeadUuid_Type()
)
eqliscsiSyncReplAfoGrpLeadUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSyncReplAfoGrpLeadUuid.setStatus("current")
_EqliscsiVolCollectionSyncReplActivePoolTable_Object = MibTable
eqliscsiVolCollectionSyncReplActivePoolTable = _EqliscsiVolCollectionSyncReplActivePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 69)
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplActivePoolTable.setStatus("current")
_EqliscsiVolCollectionSyncReplActivePoolEntry_Object = MibTableRow
eqliscsiVolCollectionSyncReplActivePoolEntry = _EqliscsiVolCollectionSyncReplActivePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 69, 1)
)
eqliscsiVolCollectionSyncReplActivePoolEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolCollectionIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplActivePoolEntry.setStatus("current")
_EqliscsiVolCollectionSyncReplActivePoolRowStatus_Type = RowStatus
_EqliscsiVolCollectionSyncReplActivePoolRowStatus_Object = MibTableColumn
eqliscsiVolCollectionSyncReplActivePoolRowStatus = _EqliscsiVolCollectionSyncReplActivePoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 69, 1, 1),
    _EqliscsiVolCollectionSyncReplActivePoolRowStatus_Type()
)
eqliscsiVolCollectionSyncReplActivePoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplActivePoolRowStatus.setStatus("current")


class _EqliscsiVolCollectionSyncReplActivePoolIndex_Type(Unsigned32):
    """Custom type eqliscsiVolCollectionSyncReplActivePoolIndex based on Unsigned32"""
    defaultValue = 0


_EqliscsiVolCollectionSyncReplActivePoolIndex_Object = MibTableColumn
eqliscsiVolCollectionSyncReplActivePoolIndex = _EqliscsiVolCollectionSyncReplActivePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 69, 1, 2),
    _EqliscsiVolCollectionSyncReplActivePoolIndex_Type()
)
eqliscsiVolCollectionSyncReplActivePoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplActivePoolIndex.setStatus("current")


class _EqliscsiVolCollectionSyncReplActivePoolFlags_Type(Bits):
    """Custom type eqliscsiVolCollectionSyncReplActivePoolFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("flag10", 10),
          ("flag11", 11),
          ("flag12", 12),
          ("flag13", 13),
          ("flag14", 14),
          ("flag15", 15),
          ("flag16", 16),
          ("flag17", 17),
          ("flag18", 18),
          ("flag19", 19),
          ("flag2", 2),
          ("flag20", 20),
          ("flag21", 21),
          ("flag22", 22),
          ("flag23", 23),
          ("flag24", 24),
          ("flag25", 25),
          ("flag26", 26),
          ("flag27", 27),
          ("flag28", 28),
          ("flag29", 29),
          ("flag3", 3),
          ("flag30", 30),
          ("flag31", 31),
          ("flag4", 4),
          ("flag5", 5),
          ("flag6", 6),
          ("flag7", 7),
          ("flag8", 8),
          ("flag9", 9),
          ("syncReplDiscardActiveChanges", 0),
          ("syncReplForceFailover", 1))
    )

_EqliscsiVolCollectionSyncReplActivePoolFlags_Type.__name__ = "Bits"
_EqliscsiVolCollectionSyncReplActivePoolFlags_Object = MibTableColumn
eqliscsiVolCollectionSyncReplActivePoolFlags = _EqliscsiVolCollectionSyncReplActivePoolFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 69, 1, 3),
    _EqliscsiVolCollectionSyncReplActivePoolFlags_Type()
)
eqliscsiVolCollectionSyncReplActivePoolFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplActivePoolFlags.setStatus("current")
_EqliscsiVolCollectionSyncReplStatusTable_Object = MibTable
eqliscsiVolCollectionSyncReplStatusTable = _EqliscsiVolCollectionSyncReplStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 70)
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplStatusTable.setStatus("current")
_EqliscsiVolCollectionSyncReplStatusEntry_Object = MibTableRow
eqliscsiVolCollectionSyncReplStatusEntry = _EqliscsiVolCollectionSyncReplStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 70, 1)
)
eqliscsiVolCollectionSyncReplStatusEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolCollectionIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplStatusEntry.setStatus("current")


class _EqliscsiVolCollectionSyncReplStatusSyncStatus_Type(Integer32):
    """Custom type eqliscsiVolCollectionSyncReplStatusSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in-sync", 1),
          ("out-of-sync", 2))
    )


_EqliscsiVolCollectionSyncReplStatusSyncStatus_Type.__name__ = "Integer32"
_EqliscsiVolCollectionSyncReplStatusSyncStatus_Object = MibTableColumn
eqliscsiVolCollectionSyncReplStatusSyncStatus = _EqliscsiVolCollectionSyncReplStatusSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 70, 1, 1),
    _EqliscsiVolCollectionSyncReplStatusSyncStatus_Type()
)
eqliscsiVolCollectionSyncReplStatusSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplStatusSyncStatus.setStatus("current")


class _EqliscsiVolCollectionSyncReplStatusUnreplicatedChanges_Type(Integer32):
    """Custom type eqliscsiVolCollectionSyncReplStatusUnreplicatedChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 3),
          ("yes", 1))
    )


_EqliscsiVolCollectionSyncReplStatusUnreplicatedChanges_Type.__name__ = "Integer32"
_EqliscsiVolCollectionSyncReplStatusUnreplicatedChanges_Object = MibTableColumn
eqliscsiVolCollectionSyncReplStatusUnreplicatedChanges = _EqliscsiVolCollectionSyncReplStatusUnreplicatedChanges_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 70, 1, 2),
    _EqliscsiVolCollectionSyncReplStatusUnreplicatedChanges_Type()
)
eqliscsiVolCollectionSyncReplStatusUnreplicatedChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplStatusUnreplicatedChanges.setStatus("current")
_EqliscsiVolCollectionSyncReplStatusTotalTxDataMB_Type = Unsigned32
_EqliscsiVolCollectionSyncReplStatusTotalTxDataMB_Object = MibTableColumn
eqliscsiVolCollectionSyncReplStatusTotalTxDataMB = _EqliscsiVolCollectionSyncReplStatusTotalTxDataMB_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 70, 1, 3),
    _EqliscsiVolCollectionSyncReplStatusTotalTxDataMB_Type()
)
eqliscsiVolCollectionSyncReplStatusTotalTxDataMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplStatusTotalTxDataMB.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplStatusTotalTxDataMB.setUnits("MB")
_EqliscsiVolCollectionSyncReplStatusRemainingTxDataMB_Type = Unsigned32
_EqliscsiVolCollectionSyncReplStatusRemainingTxDataMB_Object = MibTableColumn
eqliscsiVolCollectionSyncReplStatusRemainingTxDataMB = _EqliscsiVolCollectionSyncReplStatusRemainingTxDataMB_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 70, 1, 4),
    _EqliscsiVolCollectionSyncReplStatusRemainingTxDataMB_Type()
)
eqliscsiVolCollectionSyncReplStatusRemainingTxDataMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplStatusRemainingTxDataMB.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplStatusRemainingTxDataMB.setUnits("MB")
_EqliscsiVolumeSyncReplIndexVolumesTable_Object = MibTable
eqliscsiVolumeSyncReplIndexVolumesTable = _EqliscsiVolumeSyncReplIndexVolumesTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 71)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplIndexVolumesTable.setStatus("current")
_EqliscsiVolumeSyncReplIndexVolumesEntry_Object = MibTableRow
eqliscsiVolumeSyncReplIndexVolumesEntry = _EqliscsiVolumeSyncReplIndexVolumesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 71, 1)
)
eqliscsiVolumeSyncReplIndexVolumesEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeSyncReplLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeSyncReplIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplIndexVolumesEntry.setStatus("current")


class _EqliscsiVolumeSyncReplIndexVolumesPsvId_Type(OctetString):
    """Custom type eqliscsiVolumeSyncReplIndexVolumesPsvId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiVolumeSyncReplIndexVolumesPsvId_Type.__name__ = "OctetString"
_EqliscsiVolumeSyncReplIndexVolumesPsvId_Object = MibTableColumn
eqliscsiVolumeSyncReplIndexVolumesPsvId = _EqliscsiVolumeSyncReplIndexVolumesPsvId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 71, 1, 1),
    _EqliscsiVolumeSyncReplIndexVolumesPsvId_Type()
)
eqliscsiVolumeSyncReplIndexVolumesPsvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplIndexVolumesPsvId.setStatus("current")
_EqliscsiVolumeSyncReplSyncActiveOfflineTable_Object = MibTable
eqliscsiVolumeSyncReplSyncActiveOfflineTable = _EqliscsiVolumeSyncReplSyncActiveOfflineTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 72)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplSyncActiveOfflineTable.setStatus("current")
_EqliscsiVolumeSyncReplSyncActiveOfflineEntry_Object = MibTableRow
eqliscsiVolumeSyncReplSyncActiveOfflineEntry = _EqliscsiVolumeSyncReplSyncActiveOfflineEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 72, 1)
)
eqliscsiVolumeSyncReplSyncActiveOfflineEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplSyncActiveOfflineEntry.setStatus("current")


class _EqliscsiVolumeSyncReplSyncActiveOffline_Type(TruthValue):
    """Custom type eqliscsiVolumeSyncReplSyncActiveOffline based on TruthValue"""


_EqliscsiVolumeSyncReplSyncActiveOffline_Object = MibTableColumn
eqliscsiVolumeSyncReplSyncActiveOffline = _EqliscsiVolumeSyncReplSyncActiveOffline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 72, 1, 1),
    _EqliscsiVolumeSyncReplSyncActiveOffline_Type()
)
eqliscsiVolumeSyncReplSyncActiveOffline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplSyncActiveOffline.setStatus("current")
_EqliscsiDeletedVolumeInfoTable_Object = MibTable
eqliscsiDeletedVolumeInfoTable = _EqliscsiDeletedVolumeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 73)
)
if mibBuilder.loadTexts:
    eqliscsiDeletedVolumeInfoTable.setStatus("current")
_EqliscsiDeletedVolumeInfoEntry_Object = MibTableRow
eqliscsiDeletedVolumeInfoEntry = _EqliscsiDeletedVolumeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 73, 1)
)
eqliscsiDeletedVolumeInfoEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiDeletedVolumeInfoEntry.setStatus("current")
_EqliscsiDeletedVolumeInfoRowStatus_Type = RowStatus
_EqliscsiDeletedVolumeInfoRowStatus_Object = MibTableColumn
eqliscsiDeletedVolumeInfoRowStatus = _EqliscsiDeletedVolumeInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 73, 1, 1),
    _EqliscsiDeletedVolumeInfoRowStatus_Type()
)
eqliscsiDeletedVolumeInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiDeletedVolumeInfoRowStatus.setStatus("current")


class _EqliscsiDeletedVolumeInfoOriginalName_Type(UTFString):
    """Custom type eqliscsiDeletedVolumeInfoOriginalName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqliscsiDeletedVolumeInfoOriginalName_Type.__name__ = "UTFString"
_EqliscsiDeletedVolumeInfoOriginalName_Object = MibTableColumn
eqliscsiDeletedVolumeInfoOriginalName = _EqliscsiDeletedVolumeInfoOriginalName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 73, 1, 2),
    _EqliscsiDeletedVolumeInfoOriginalName_Type()
)
eqliscsiDeletedVolumeInfoOriginalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiDeletedVolumeInfoOriginalName.setStatus("current")


class _EqliscsiDeletedVolumeInfoOriginalType_Type(Integer32):
    """Custom type eqliscsiDeletedVolumeInfoOriginalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classic", 1),
          ("snapshot", 3),
          ("thin-provisioned", 2))
    )


_EqliscsiDeletedVolumeInfoOriginalType_Type.__name__ = "Integer32"
_EqliscsiDeletedVolumeInfoOriginalType_Object = MibTableColumn
eqliscsiDeletedVolumeInfoOriginalType = _EqliscsiDeletedVolumeInfoOriginalType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 73, 1, 3),
    _EqliscsiDeletedVolumeInfoOriginalType_Type()
)
eqliscsiDeletedVolumeInfoOriginalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiDeletedVolumeInfoOriginalType.setStatus("current")


class _EqliscsiDeletedVolumeFlags_Type(Bits):
    """Custom type eqliscsiDeletedVolumeFlags based on Bits"""
    namedValues = NamedValues(
        *(("failback", 1),
          ("flag10", 10),
          ("flag11", 11),
          ("flag12", 12),
          ("flag13", 13),
          ("flag14", 14),
          ("flag15", 15),
          ("flag16", 16),
          ("flag17", 17),
          ("flag18", 18),
          ("flag19", 19),
          ("flag20", 20),
          ("flag21", 21),
          ("flag22", 22),
          ("flag23", 23),
          ("flag24", 24),
          ("flag25", 25),
          ("flag26", 26),
          ("flag27", 27),
          ("flag28", 28),
          ("flag29", 29),
          ("flag30", 30),
          ("flag31", 31),
          ("flag6", 6),
          ("flag7", 7),
          ("flag8", 8),
          ("flag9", 9),
          ("recovery", 2),
          ("replicaset", 0),
          ("syncrep", 3),
          ("template", 4),
          ("thinClone", 5))
    )

_EqliscsiDeletedVolumeFlags_Type.__name__ = "Bits"
_EqliscsiDeletedVolumeFlags_Object = MibTableColumn
eqliscsiDeletedVolumeFlags = _EqliscsiDeletedVolumeFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 73, 1, 4),
    _EqliscsiDeletedVolumeFlags_Type()
)
eqliscsiDeletedVolumeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiDeletedVolumeFlags.setStatus("current")
_EqliscsiDeletedVolumeInfoDeleteDate_Type = Counter32
_EqliscsiDeletedVolumeInfoDeleteDate_Object = MibTableColumn
eqliscsiDeletedVolumeInfoDeleteDate = _EqliscsiDeletedVolumeInfoDeleteDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 73, 1, 5),
    _EqliscsiDeletedVolumeInfoDeleteDate_Type()
)
eqliscsiDeletedVolumeInfoDeleteDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiDeletedVolumeInfoDeleteDate.setStatus("current")
_EqliscsiDeletedVolumeThinWarnPercentage_Type = Unsigned32
_EqliscsiDeletedVolumeThinWarnPercentage_Object = MibTableColumn
eqliscsiDeletedVolumeThinWarnPercentage = _EqliscsiDeletedVolumeThinWarnPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 73, 1, 6),
    _EqliscsiDeletedVolumeThinWarnPercentage_Type()
)
eqliscsiDeletedVolumeThinWarnPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiDeletedVolumeThinWarnPercentage.setStatus("current")
_EqliscsiDeletedVolumeThinMaxGrowPercentage_Type = Unsigned32
_EqliscsiDeletedVolumeThinMaxGrowPercentage_Object = MibTableColumn
eqliscsiDeletedVolumeThinMaxGrowPercentage = _EqliscsiDeletedVolumeThinMaxGrowPercentage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 73, 1, 7),
    _EqliscsiDeletedVolumeThinMaxGrowPercentage_Type()
)
eqliscsiDeletedVolumeThinMaxGrowPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiDeletedVolumeThinMaxGrowPercentage.setStatus("current")
_EqliscsiVolumeSyncReplActivePeerTable_Object = MibTable
eqliscsiVolumeSyncReplActivePeerTable = _EqliscsiVolumeSyncReplActivePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 74)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplActivePeerTable.setStatus("current")
_EqliscsiVolumeSyncReplActivePeerEntry_Object = MibTableRow
eqliscsiVolumeSyncReplActivePeerEntry = _EqliscsiVolumeSyncReplActivePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 74, 1)
)
eqliscsiVolumeSyncReplActivePeerEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeSyncReplLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeSyncReplIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplActivePeerEntry.setStatus("current")
_EqliscsiVolumeSyncReplActivePeerRowStatus_Type = RowStatus
_EqliscsiVolumeSyncReplActivePeerRowStatus_Object = MibTableColumn
eqliscsiVolumeSyncReplActivePeerRowStatus = _EqliscsiVolumeSyncReplActivePeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 74, 1, 1),
    _EqliscsiVolumeSyncReplActivePeerRowStatus_Type()
)
eqliscsiVolumeSyncReplActivePeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplActivePeerRowStatus.setStatus("current")
_EqliscsiVolumeSyncReplActivePeerLocalMemberId_Type = Unsigned32
_EqliscsiVolumeSyncReplActivePeerLocalMemberId_Object = MibTableColumn
eqliscsiVolumeSyncReplActivePeerLocalMemberId = _EqliscsiVolumeSyncReplActivePeerLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 74, 1, 2),
    _EqliscsiVolumeSyncReplActivePeerLocalMemberId_Type()
)
eqliscsiVolumeSyncReplActivePeerLocalMemberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplActivePeerLocalMemberId.setStatus("current")
_EqliscsiVolumeSyncReplActivePeerVolIndex_Type = Unsigned32
_EqliscsiVolumeSyncReplActivePeerVolIndex_Object = MibTableColumn
eqliscsiVolumeSyncReplActivePeerVolIndex = _EqliscsiVolumeSyncReplActivePeerVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 74, 1, 3),
    _EqliscsiVolumeSyncReplActivePeerVolIndex_Type()
)
eqliscsiVolumeSyncReplActivePeerVolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplActivePeerVolIndex.setStatus("current")


class _EqliscsiVolumeSyncReplActivePeerFlags_Type(Bits):
    """Custom type eqliscsiVolumeSyncReplActivePeerFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("flag10", 10),
          ("flag11", 11),
          ("flag12", 12),
          ("flag13", 13),
          ("flag14", 14),
          ("flag15", 15),
          ("flag16", 16),
          ("flag17", 17),
          ("flag18", 18),
          ("flag19", 19),
          ("flag2", 2),
          ("flag20", 20),
          ("flag21", 21),
          ("flag22", 22),
          ("flag23", 23),
          ("flag24", 24),
          ("flag25", 25),
          ("flag26", 26),
          ("flag27", 27),
          ("flag28", 28),
          ("flag29", 29),
          ("flag3", 3),
          ("flag30", 30),
          ("flag31", 31),
          ("flag4", 4),
          ("flag5", 5),
          ("flag6", 6),
          ("flag7", 7),
          ("flag8", 8),
          ("flag9", 9),
          ("syncReplDiscardActiveChanges", 0),
          ("syncReplForceFailover", 1))
    )

_EqliscsiVolumeSyncReplActivePeerFlags_Type.__name__ = "Bits"
_EqliscsiVolumeSyncReplActivePeerFlags_Object = MibTableColumn
eqliscsiVolumeSyncReplActivePeerFlags = _EqliscsiVolumeSyncReplActivePeerFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 74, 1, 4),
    _EqliscsiVolumeSyncReplActivePeerFlags_Type()
)
eqliscsiVolumeSyncReplActivePeerFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplActivePeerFlags.setStatus("current")
_EqliscsiVolumeSyncReplActivePeerLookupTable_Object = MibTable
eqliscsiVolumeSyncReplActivePeerLookupTable = _EqliscsiVolumeSyncReplActivePeerLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 75)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplActivePeerLookupTable.setStatus("current")
_EqliscsiVolumeSyncReplActivePeerLookupEntry_Object = MibTableRow
eqliscsiVolumeSyncReplActivePeerLookupEntry = _EqliscsiVolumeSyncReplActivePeerLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 75, 1)
)
eqliscsiVolumeSyncReplActivePeerLookupEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplActivePeerLookupEntry.setStatus("current")
_EqliscsiVolumeSyncReplActivePeerLookupLocalMemberId_Type = Unsigned32
_EqliscsiVolumeSyncReplActivePeerLookupLocalMemberId_Object = MibTableColumn
eqliscsiVolumeSyncReplActivePeerLookupLocalMemberId = _EqliscsiVolumeSyncReplActivePeerLookupLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 75, 1, 1),
    _EqliscsiVolumeSyncReplActivePeerLookupLocalMemberId_Type()
)
eqliscsiVolumeSyncReplActivePeerLookupLocalMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplActivePeerLookupLocalMemberId.setStatus("current")
_EqliscsiVolumeSyncReplActivePeerLookupVolIndex_Type = Unsigned32
_EqliscsiVolumeSyncReplActivePeerLookupVolIndex_Object = MibTableColumn
eqliscsiVolumeSyncReplActivePeerLookupVolIndex = _EqliscsiVolumeSyncReplActivePeerLookupVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 75, 1, 2),
    _EqliscsiVolumeSyncReplActivePeerLookupVolIndex_Type()
)
eqliscsiVolumeSyncReplActivePeerLookupVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplActivePeerLookupVolIndex.setStatus("current")
_EqliscsiVolumeSyncReplFailbackTable_Object = MibTable
eqliscsiVolumeSyncReplFailbackTable = _EqliscsiVolumeSyncReplFailbackTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 76)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplFailbackTable.setStatus("current")
_EqliscsiVolumeSyncReplFailbackEntry_Object = MibTableRow
eqliscsiVolumeSyncReplFailbackEntry = _EqliscsiVolumeSyncReplFailbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 76, 1)
)
eqliscsiVolumeSyncReplFailbackEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplFailbackEntry.setStatus("current")
_EqliscsiVolumeSyncReplFailbackRowStatus_Type = RowStatus
_EqliscsiVolumeSyncReplFailbackRowStatus_Object = MibTableColumn
eqliscsiVolumeSyncReplFailbackRowStatus = _EqliscsiVolumeSyncReplFailbackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 76, 1, 1),
    _EqliscsiVolumeSyncReplFailbackRowStatus_Type()
)
eqliscsiVolumeSyncReplFailbackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplFailbackRowStatus.setStatus("current")


class _EqliscsiVolumeSyncReplAllowFailback_Type(TruthValue):
    """Custom type eqliscsiVolumeSyncReplAllowFailback based on TruthValue"""


_EqliscsiVolumeSyncReplAllowFailback_Object = MibTableColumn
eqliscsiVolumeSyncReplAllowFailback = _EqliscsiVolumeSyncReplAllowFailback_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 76, 1, 2),
    _EqliscsiVolumeSyncReplAllowFailback_Type()
)
eqliscsiVolumeSyncReplAllowFailback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolumeSyncReplAllowFailback.setStatus("current")
_EqliscsiVolCollectionSyncReplSyncActiveOfflineTable_Object = MibTable
eqliscsiVolCollectionSyncReplSyncActiveOfflineTable = _EqliscsiVolCollectionSyncReplSyncActiveOfflineTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 77)
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplSyncActiveOfflineTable.setStatus("current")
_EqliscsiVolCollectionSyncReplSyncActiveOfflineEntry_Object = MibTableRow
eqliscsiVolCollectionSyncReplSyncActiveOfflineEntry = _EqliscsiVolCollectionSyncReplSyncActiveOfflineEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 77, 1)
)
eqliscsiVolCollectionSyncReplSyncActiveOfflineEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolCollectionIndex"),
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplSyncActiveOfflineEntry.setStatus("current")


class _EqliscsiVolCollectionSyncReplSyncActiveOffline_Type(TruthValue):
    """Custom type eqliscsiVolCollectionSyncReplSyncActiveOffline based on TruthValue"""


_EqliscsiVolCollectionSyncReplSyncActiveOffline_Object = MibTableColumn
eqliscsiVolCollectionSyncReplSyncActiveOffline = _EqliscsiVolCollectionSyncReplSyncActiveOffline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 77, 1, 1),
    _EqliscsiVolCollectionSyncReplSyncActiveOffline_Type()
)
eqliscsiVolCollectionSyncReplSyncActiveOffline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqliscsiVolCollectionSyncReplSyncActiveOffline.setStatus("current")
_EqliscsiSyncReplStateTable_Object = MibTable
eqliscsiSyncReplStateTable = _EqliscsiSyncReplStateTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 78)
)
if mibBuilder.loadTexts:
    eqliscsiSyncReplStateTable.setStatus("current")
_EqliscsiSyncReplStateEntry_Object = MibTableRow
eqliscsiSyncReplStateEntry = _EqliscsiSyncReplStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 78, 1)
)
eqliscsiSyncReplStateEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId0"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId1"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId2"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId3"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId0"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId1"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId2"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId3"),
)
if mibBuilder.loadTexts:
    eqliscsiSyncReplStateEntry.setStatus("current")
_EqliscsiSyncReplStateSeqNum_Type = Unsigned32
_EqliscsiSyncReplStateSeqNum_Object = MibTableColumn
eqliscsiSyncReplStateSeqNum = _EqliscsiSyncReplStateSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 78, 1, 1),
    _EqliscsiSyncReplStateSeqNum_Type()
)
eqliscsiSyncReplStateSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSyncReplStateSeqNum.setStatus("current")
_EqliscsiSyncReplStateState_Type = Unsigned32
_EqliscsiSyncReplStateState_Object = MibTableColumn
eqliscsiSyncReplStateState = _EqliscsiSyncReplStateState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 78, 1, 2),
    _EqliscsiSyncReplStateState_Type()
)
eqliscsiSyncReplStateState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSyncReplStateState.setStatus("current")


class _EqliscsiSyncReplStateGrpLeadUuid_Type(OctetString):
    """Custom type eqliscsiSyncReplStateGrpLeadUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiSyncReplStateGrpLeadUuid_Type.__name__ = "OctetString"
_EqliscsiSyncReplStateGrpLeadUuid_Object = MibTableColumn
eqliscsiSyncReplStateGrpLeadUuid = _EqliscsiSyncReplStateGrpLeadUuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 78, 1, 3),
    _EqliscsiSyncReplStateGrpLeadUuid_Type()
)
eqliscsiSyncReplStateGrpLeadUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSyncReplStateGrpLeadUuid.setStatus("current")
_EqliscsiVsrVirtualSyncReplSyncActiveOfflineTable_Object = MibTable
eqliscsiVsrVirtualSyncReplSyncActiveOfflineTable = _EqliscsiVsrVirtualSyncReplSyncActiveOfflineTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 79)
)
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplSyncActiveOfflineTable.setStatus("current")
_EqliscsiVsrVirtualSyncReplSyncActiveOfflineEntry_Object = MibTableRow
eqliscsiVsrVirtualSyncReplSyncActiveOfflineEntry = _EqliscsiVsrVirtualSyncReplSyncActiveOfflineEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 79, 1)
)
eqliscsiVsrVirtualSyncReplSyncActiveOfflineEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplSyncActiveOfflineEntry.setStatus("current")


class _EqliscsiVsrVirtualSyncReplSyncActiveOffline_Type(TruthValue):
    """Custom type eqliscsiVsrVirtualSyncReplSyncActiveOffline based on TruthValue"""


_EqliscsiVsrVirtualSyncReplSyncActiveOffline_Object = MibTableColumn
eqliscsiVsrVirtualSyncReplSyncActiveOffline = _EqliscsiVsrVirtualSyncReplSyncActiveOffline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 79, 1, 1),
    _EqliscsiVsrVirtualSyncReplSyncActiveOffline_Type()
)
eqliscsiVsrVirtualSyncReplSyncActiveOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVsrVirtualSyncReplSyncActiveOffline.setStatus("current")
_EqliscsiVsrCollectionSyncReplSyncActiveOfflineTable_Object = MibTable
eqliscsiVsrCollectionSyncReplSyncActiveOfflineTable = _EqliscsiVsrCollectionSyncReplSyncActiveOfflineTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 80)
)
if mibBuilder.loadTexts:
    eqliscsiVsrCollectionSyncReplSyncActiveOfflineTable.setStatus("current")
_EqliscsiVsrCollectionSyncReplSyncActiveOfflineEntry_Object = MibTableRow
eqliscsiVsrCollectionSyncReplSyncActiveOfflineEntry = _EqliscsiVsrCollectionSyncReplSyncActiveOfflineEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 80, 1)
)
eqliscsiVsrCollectionSyncReplSyncActiveOfflineEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolCollectionIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVsrCollectionSyncReplSyncActiveOfflineEntry.setStatus("current")


class _EqliscsiVsrCollectionSyncReplSyncActiveOffline_Type(TruthValue):
    """Custom type eqliscsiVsrCollectionSyncReplSyncActiveOffline based on TruthValue"""


_EqliscsiVsrCollectionSyncReplSyncActiveOffline_Object = MibTableColumn
eqliscsiVsrCollectionSyncReplSyncActiveOffline = _EqliscsiVsrCollectionSyncReplSyncActiveOffline_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 80, 1, 1),
    _EqliscsiVsrCollectionSyncReplSyncActiveOffline_Type()
)
eqliscsiVsrCollectionSyncReplSyncActiveOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVsrCollectionSyncReplSyncActiveOffline.setStatus("current")
_EqliscsiVolNameSecondaryIndexTable_Object = MibTable
eqliscsiVolNameSecondaryIndexTable = _EqliscsiVolNameSecondaryIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 81)
)
if mibBuilder.loadTexts:
    eqliscsiVolNameSecondaryIndexTable.setStatus("current")
_EqliscsiVolNameSecondaryIndexEntry_Object = MibTableRow
eqliscsiVolNameSecondaryIndexEntry = _EqliscsiVolNameSecondaryIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 81, 1)
)
eqliscsiVolNameSecondaryIndexEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeName"),
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolNameSecondaryIndexEntry.setStatus("current")
_EqliscsiVolNameSecondaryIndexRowStatus_Type = RowStatus
_EqliscsiVolNameSecondaryIndexRowStatus_Object = MibTableColumn
eqliscsiVolNameSecondaryIndexRowStatus = _EqliscsiVolNameSecondaryIndexRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 81, 1, 1),
    _EqliscsiVolNameSecondaryIndexRowStatus_Type()
)
eqliscsiVolNameSecondaryIndexRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiVolNameSecondaryIndexRowStatus.setStatus("current")
_EqliscsiSharedVolumeSetTable_Object = MibTable
eqliscsiSharedVolumeSetTable = _EqliscsiSharedVolumeSetTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 82)
)
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSetTable.setStatus("current")
_EqliscsiSharedVolumeSetEntry_Object = MibTableRow
eqliscsiSharedVolumeSetEntry = _EqliscsiSharedVolumeSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 82, 1)
)
eqliscsiSharedVolumeSetEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeSetIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSetEntry.setStatus("current")
_EqliscsiSharedVolumeSetIndex_Type = Unsigned32
_EqliscsiSharedVolumeSetIndex_Object = MibTableColumn
eqliscsiSharedVolumeSetIndex = _EqliscsiSharedVolumeSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 82, 1, 1),
    _EqliscsiSharedVolumeSetIndex_Type()
)
eqliscsiSharedVolumeSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSetIndex.setStatus("current")
_EqliscsiSharedVolumeSetRowStatus_Type = RowStatus
_EqliscsiSharedVolumeSetRowStatus_Object = MibTableColumn
eqliscsiSharedVolumeSetRowStatus = _EqliscsiSharedVolumeSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 82, 1, 2),
    _EqliscsiSharedVolumeSetRowStatus_Type()
)
eqliscsiSharedVolumeSetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSetRowStatus.setStatus("current")


class _EqliscsiSharedVolumeSetPsvid_Type(OctetString):
    """Custom type eqliscsiSharedVolumeSetPsvid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiSharedVolumeSetPsvid_Type.__name__ = "OctetString"
_EqliscsiSharedVolumeSetPsvid_Object = MibTableColumn
eqliscsiSharedVolumeSetPsvid = _EqliscsiSharedVolumeSetPsvid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 82, 1, 3),
    _EqliscsiSharedVolumeSetPsvid_Type()
)
eqliscsiSharedVolumeSetPsvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSetPsvid.setStatus("current")


class _EqliscsiSharedVolumeSetSectorSize_Type(Integer32):
    """Custom type eqliscsiSharedVolumeSetSectorSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sector-size-4096-bytes", 1),
          ("sector-size-512-bytes", 0))
    )


_EqliscsiSharedVolumeSetSectorSize_Type.__name__ = "Integer32"
_EqliscsiSharedVolumeSetSectorSize_Object = MibTableColumn
eqliscsiSharedVolumeSetSectorSize = _EqliscsiSharedVolumeSetSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 82, 1, 4),
    _EqliscsiSharedVolumeSetSectorSize_Type()
)
eqliscsiSharedVolumeSetSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSetSectorSize.setStatus("current")


class _EqliscsiSharedVolumeSetStorageBucketUUID_Type(OctetString):
    """Custom type eqliscsiSharedVolumeSetStorageBucketUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiSharedVolumeSetStorageBucketUUID_Type.__name__ = "OctetString"
_EqliscsiSharedVolumeSetStorageBucketUUID_Object = MibTableColumn
eqliscsiSharedVolumeSetStorageBucketUUID = _EqliscsiSharedVolumeSetStorageBucketUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 82, 1, 5),
    _EqliscsiSharedVolumeSetStorageBucketUUID_Type()
)
eqliscsiSharedVolumeSetStorageBucketUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSetStorageBucketUUID.setStatus("current")
_EqliscsiSharedVolumeSharedVolumeSetBucket_Type = EQL2PartRowPointerStr
_EqliscsiSharedVolumeSharedVolumeSetBucket_Object = MibTableColumn
eqliscsiSharedVolumeSharedVolumeSetBucket = _EqliscsiSharedVolumeSharedVolumeSetBucket_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 82, 1, 6),
    _EqliscsiSharedVolumeSharedVolumeSetBucket_Type()
)
eqliscsiSharedVolumeSharedVolumeSetBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSharedVolumeSetBucket.setStatus("current")


class _EqliscsiSharedVolumeSetBucketFullPolicy_Type(Integer32):
    """Custom type eqliscsiSharedVolumeSetBucketFullPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("keep-online-fail-write-to-unallocated-pages", 0),
          ("make-svs-offline", 1))
    )


_EqliscsiSharedVolumeSetBucketFullPolicy_Type.__name__ = "Integer32"
_EqliscsiSharedVolumeSetBucketFullPolicy_Object = MibTableColumn
eqliscsiSharedVolumeSetBucketFullPolicy = _EqliscsiSharedVolumeSetBucketFullPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 82, 1, 7),
    _EqliscsiSharedVolumeSetBucketFullPolicy_Type()
)
eqliscsiSharedVolumeSetBucketFullPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSetBucketFullPolicy.setStatus("current")
_EqliscsiSharedVolumeTable_Object = MibTable
eqliscsiSharedVolumeTable = _EqliscsiSharedVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83)
)
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeTable.setStatus("current")
_EqliscsiSharedVolumeEntry_Object = MibTableRow
eqliscsiSharedVolumeEntry = _EqliscsiSharedVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1)
)
eqliscsiSharedVolumeEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeEntry.setStatus("current")
_EqliscsiSharedVolumeIndex_Type = Unsigned32
_EqliscsiSharedVolumeIndex_Object = MibTableColumn
eqliscsiSharedVolumeIndex = _EqliscsiSharedVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 1),
    _EqliscsiSharedVolumeIndex_Type()
)
eqliscsiSharedVolumeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeIndex.setStatus("current")
_EqliscsiSharedVolumeRowStatus_Type = RowStatus
_EqliscsiSharedVolumeRowStatus_Object = MibTableColumn
eqliscsiSharedVolumeRowStatus = _EqliscsiSharedVolumeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 2),
    _EqliscsiSharedVolumeRowStatus_Type()
)
eqliscsiSharedVolumeRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeRowStatus.setStatus("current")


class _EqliscsiSharedVolumePsvid_Type(OctetString):
    """Custom type eqliscsiSharedVolumePsvid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiSharedVolumePsvid_Type.__name__ = "OctetString"
_EqliscsiSharedVolumePsvid_Object = MibTableColumn
eqliscsiSharedVolumePsvid = _EqliscsiSharedVolumePsvid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 3),
    _EqliscsiSharedVolumePsvid_Type()
)
eqliscsiSharedVolumePsvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumePsvid.setStatus("current")


class _EqliscsiSharedVolumeName_Type(UTFString):
    """Custom type eqliscsiSharedVolumeName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqliscsiSharedVolumeName_Type.__name__ = "UTFString"
_EqliscsiSharedVolumeName_Object = MibTableColumn
eqliscsiSharedVolumeName = _EqliscsiSharedVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 4),
    _EqliscsiSharedVolumeName_Type()
)
eqliscsiSharedVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeName.setStatus("current")
_EqliscsiSharedVolumeSize_Type = Integer32
_EqliscsiSharedVolumeSize_Object = MibTableColumn
eqliscsiSharedVolumeSize = _EqliscsiSharedVolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 5),
    _EqliscsiSharedVolumeSize_Type()
)
eqliscsiSharedVolumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSize.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSize.setUnits("MB")


class _EqliscsiSharedVolumeCreatedAs_Type(VirtualVolumeCreatedAs):
    """Custom type eqliscsiSharedVolumeCreatedAs based on VirtualVolumeCreatedAs"""


_EqliscsiSharedVolumeCreatedAs_Object = MibTableColumn
eqliscsiSharedVolumeCreatedAs = _EqliscsiSharedVolumeCreatedAs_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 6),
    _EqliscsiSharedVolumeCreatedAs_Type()
)
eqliscsiSharedVolumeCreatedAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeCreatedAs.setStatus("current")
_EqliscsiSharedVolumeIfSnapshotOrFastCloneMyParentVVol_Type = EQL2PartRowPointerStr
_EqliscsiSharedVolumeIfSnapshotOrFastCloneMyParentVVol_Object = MibTableColumn
eqliscsiSharedVolumeIfSnapshotOrFastCloneMyParentVVol = _EqliscsiSharedVolumeIfSnapshotOrFastCloneMyParentVVol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 7),
    _EqliscsiSharedVolumeIfSnapshotOrFastCloneMyParentVVol_Type()
)
eqliscsiSharedVolumeIfSnapshotOrFastCloneMyParentVVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeIfSnapshotOrFastCloneMyParentVVol.setStatus("current")
_EqliscsiSharedVolumeSharedVolumeSet_Type = EQL2PartRowPointerStr
_EqliscsiSharedVolumeSharedVolumeSet_Object = MibTableColumn
eqliscsiSharedVolumeSharedVolumeSet = _EqliscsiSharedVolumeSharedVolumeSet_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 8),
    _EqliscsiSharedVolumeSharedVolumeSet_Type()
)
eqliscsiSharedVolumeSharedVolumeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSharedVolumeSet.setStatus("current")


class _EqliscsiSharedVolumeDescription_Type(UTFString):
    """Custom type eqliscsiSharedVolumeDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiSharedVolumeDescription_Type.__name__ = "UTFString"
_EqliscsiSharedVolumeDescription_Object = MibTableColumn
eqliscsiSharedVolumeDescription = _EqliscsiSharedVolumeDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 9),
    _EqliscsiSharedVolumeDescription_Type()
)
eqliscsiSharedVolumeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeDescription.setStatus("current")


class _EqliscsiSharedVolumeFlags_Type(Bits):
    """Custom type eqliscsiSharedVolumeFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("isVvol", 0)
    )

_EqliscsiSharedVolumeFlags_Type.__name__ = "Bits"
_EqliscsiSharedVolumeFlags_Object = MibTableColumn
eqliscsiSharedVolumeFlags = _EqliscsiSharedVolumeFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 10),
    _EqliscsiSharedVolumeFlags_Type()
)
eqliscsiSharedVolumeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeFlags.setStatus("current")
_EqliscsiSharedVolumeSecondaryLunId_Type = Unsigned32
_EqliscsiSharedVolumeSecondaryLunId_Object = MibTableColumn
eqliscsiSharedVolumeSecondaryLunId = _EqliscsiSharedVolumeSecondaryLunId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 83, 1, 11),
    _EqliscsiSharedVolumeSecondaryLunId_Type()
)
eqliscsiSharedVolumeSecondaryLunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeSecondaryLunId.setStatus("current")
_EqlVmwareVirtualVolumeTable_Object = MibTable
eqlVmwareVirtualVolumeTable = _EqlVmwareVirtualVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 84)
)
if mibBuilder.loadTexts:
    eqlVmwareVirtualVolumeTable.setStatus("current")
_EqlVmwareVirtualVolumeEntry_Object = MibTableRow
eqlVmwareVirtualVolumeEntry = _EqlVmwareVirtualVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 84, 1)
)
eqlVmwareVirtualVolumeEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqlVmwareVirtualVolumeEntry.setStatus("current")
_EqlVmwareVirtualVolumeRowStatus_Type = RowStatus
_EqlVmwareVirtualVolumeRowStatus_Object = MibTableColumn
eqlVmwareVirtualVolumeRowStatus = _EqlVmwareVirtualVolumeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 84, 1, 1),
    _EqlVmwareVirtualVolumeRowStatus_Type()
)
eqlVmwareVirtualVolumeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVmwareVirtualVolumeRowStatus.setStatus("current")
_EqlVmwareVirtualVolumeType_Type = VirtualVolumeType
_EqlVmwareVirtualVolumeType_Object = MibTableColumn
eqlVmwareVirtualVolumeType = _EqlVmwareVirtualVolumeType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 84, 1, 2),
    _EqlVmwareVirtualVolumeType_Type()
)
eqlVmwareVirtualVolumeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlVmwareVirtualVolumeType.setStatus("current")
_EqlVmWareVirtualVolumeIfSnapshotCreateDate_Type = Counter32
_EqlVmWareVirtualVolumeIfSnapshotCreateDate_Object = MibTableColumn
eqlVmWareVirtualVolumeIfSnapshotCreateDate = _EqlVmWareVirtualVolumeIfSnapshotCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 84, 1, 3),
    _EqlVmWareVirtualVolumeIfSnapshotCreateDate_Type()
)
eqlVmWareVirtualVolumeIfSnapshotCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlVmWareVirtualVolumeIfSnapshotCreateDate.setStatus("current")
_EqliscsiSharedVolumeStatusTable_Object = MibTable
eqliscsiSharedVolumeStatusTable = _EqliscsiSharedVolumeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 85)
)
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatusTable.setStatus("current")
_EqliscsiSharedVolumeStatusEntry_Object = MibTableRow
eqliscsiSharedVolumeStatusEntry = _EqliscsiSharedVolumeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 85, 1)
)
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatusEntry.setStatus("current")
_EqliscsiSharedVolumeStatusAllocatedSpace_Type = Unsigned32
_EqliscsiSharedVolumeStatusAllocatedSpace_Object = MibTableColumn
eqliscsiSharedVolumeStatusAllocatedSpace = _EqliscsiSharedVolumeStatusAllocatedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 85, 1, 1),
    _EqliscsiSharedVolumeStatusAllocatedSpace_Type()
)
eqliscsiSharedVolumeStatusAllocatedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatusAllocatedSpace.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatusAllocatedSpace.setUnits("MB")
_EqliscsiSharedVolumeStatusSharedSpace_Type = Unsigned32
_EqliscsiSharedVolumeStatusSharedSpace_Object = MibTableColumn
eqliscsiSharedVolumeStatusSharedSpace = _EqliscsiSharedVolumeStatusSharedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 85, 1, 2),
    _EqliscsiSharedVolumeStatusSharedSpace_Type()
)
eqliscsiSharedVolumeStatusSharedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatusSharedSpace.setStatus("current")


class _EqliscsiSharedVolumeStatusOperStatus_Type(Integer32):
    """Custom type eqliscsiSharedVolumeStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("not-available", 2),
          ("not-available-due-to-internal-error", 9),
          ("not-available-due-to-lost-cached-blocks", 4),
          ("not-available-due-to-members-offline", 3),
          ("not-available-due-to-missing-pages", 8),
          ("not-available-due-to-nospace-for-auto-grow", 7),
          ("not-available-due-to-thin-max-growth-met", 5))
    )


_EqliscsiSharedVolumeStatusOperStatus_Type.__name__ = "Integer32"
_EqliscsiSharedVolumeStatusOperStatus_Object = MibTableColumn
eqliscsiSharedVolumeStatusOperStatus = _EqliscsiSharedVolumeStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 85, 1, 3),
    _EqliscsiSharedVolumeStatusOperStatus_Type()
)
eqliscsiSharedVolumeStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatusOperStatus.setStatus("current")
_EqliscsiDynVVolTable_Object = MibTable
eqliscsiDynVVolTable = _EqliscsiDynVVolTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86)
)
if mibBuilder.loadTexts:
    eqliscsiDynVVolTable.setStatus("current")
_EqliscsiDynVVolEntry_Object = MibTableRow
eqliscsiDynVVolEntry = _EqliscsiDynVVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1)
)
eqliscsiDynVVolEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiDynVVolEntry.setStatus("current")
_EqliscsiDynVVolRowStatus_Type = RowStatus
_EqliscsiDynVVolRowStatus_Object = MibTableColumn
eqliscsiDynVVolRowStatus = _EqliscsiDynVVolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 1),
    _EqliscsiDynVVolRowStatus_Type()
)
eqliscsiDynVVolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiDynVVolRowStatus.setStatus("current")


class _EqliscsiDynVVolName_Type(UTFString):
    """Custom type eqliscsiDynVVolName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqliscsiDynVVolName_Type.__name__ = "UTFString"
_EqliscsiDynVVolName_Object = MibTableColumn
eqliscsiDynVVolName = _EqliscsiDynVVolName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 2),
    _EqliscsiDynVVolName_Type()
)
eqliscsiDynVVolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiDynVVolName.setStatus("current")
_EqliscsiDynVVolSize_Type = Integer32
_EqliscsiDynVVolSize_Object = MibTableColumn
eqliscsiDynVVolSize = _EqliscsiDynVVolSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 3),
    _EqliscsiDynVVolSize_Type()
)
eqliscsiDynVVolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiDynVVolSize.setStatus("current")
_EqliscsiDynVVolContainer_Type = EQL2PartRowPointerStr
_EqliscsiDynVVolContainer_Object = MibTableColumn
eqliscsiDynVVolContainer = _EqliscsiDynVVolContainer_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 4),
    _EqliscsiDynVVolContainer_Type()
)
eqliscsiDynVVolContainer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiDynVVolContainer.setStatus("current")


class _EqliscsiDynVVolDesc_Type(UTFString):
    """Custom type eqliscsiDynVVolDesc based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqliscsiDynVVolDesc_Type.__name__ = "UTFString"
_EqliscsiDynVVolDesc_Object = MibTableColumn
eqliscsiDynVVolDesc = _EqliscsiDynVVolDesc_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 5),
    _EqliscsiDynVVolDesc_Type()
)
eqliscsiDynVVolDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiDynVVolDesc.setStatus("current")
_EqliscsiDynVVolCreatedAs_Type = VirtualVolumeCreatedAs
_EqliscsiDynVVolCreatedAs_Object = MibTableColumn
eqliscsiDynVVolCreatedAs = _EqliscsiDynVVolCreatedAs_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 6),
    _EqliscsiDynVVolCreatedAs_Type()
)
eqliscsiDynVVolCreatedAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiDynVVolCreatedAs.setStatus("current")
_EqliscsiDynVVolIfSnapshotOrFastCloneMyParentVVol_Type = EQL2PartRowPointerStr
_EqliscsiDynVVolIfSnapshotOrFastCloneMyParentVVol_Object = MibTableColumn
eqliscsiDynVVolIfSnapshotOrFastCloneMyParentVVol = _EqliscsiDynVVolIfSnapshotOrFastCloneMyParentVVol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 7),
    _EqliscsiDynVVolIfSnapshotOrFastCloneMyParentVVol_Type()
)
eqliscsiDynVVolIfSnapshotOrFastCloneMyParentVVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiDynVVolIfSnapshotOrFastCloneMyParentVVol.setStatus("current")
_EqliscsiDynVVolType_Type = VirtualVolumeType
_EqliscsiDynVVolType_Object = MibTableColumn
eqliscsiDynVVolType = _EqliscsiDynVVolType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 8),
    _EqliscsiDynVVolType_Type()
)
eqliscsiDynVVolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiDynVVolType.setStatus("current")
_EqliscsiDynVVolCreateIsDerived_Type = TruthValue
_EqliscsiDynVVolCreateIsDerived_Object = MibTableColumn
eqliscsiDynVVolCreateIsDerived = _EqliscsiDynVVolCreateIsDerived_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 9),
    _EqliscsiDynVVolCreateIsDerived_Type()
)
eqliscsiDynVVolCreateIsDerived.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiDynVVolCreateIsDerived.setStatus("current")


class _EqliscsiDynVVolCreateDerivedType_Type(Integer32):
    """Custom type eqliscsiDynVVolCreateDerivedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clone", 4),
          ("fast-clone", 3),
          ("snapshot", 2))
    )


_EqliscsiDynVVolCreateDerivedType_Type.__name__ = "Integer32"
_EqliscsiDynVVolCreateDerivedType_Object = MibTableColumn
eqliscsiDynVVolCreateDerivedType = _EqliscsiDynVVolCreateDerivedType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 10),
    _EqliscsiDynVVolCreateDerivedType_Type()
)
eqliscsiDynVVolCreateDerivedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiDynVVolCreateDerivedType.setStatus("current")
_EqliscsiDynVVolCreateDerivedFromParent_Type = EQL2PartRowPointerStr
_EqliscsiDynVVolCreateDerivedFromParent_Object = MibTableColumn
eqliscsiDynVVolCreateDerivedFromParent = _EqliscsiDynVVolCreateDerivedFromParent_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 11),
    _EqliscsiDynVVolCreateDerivedFromParent_Type()
)
eqliscsiDynVVolCreateDerivedFromParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiDynVVolCreateDerivedFromParent.setStatus("current")
_EqliscsiDynVVolIfSnapshotMyStatus_Type = VirtualVolumeSnapshotStatus
_EqliscsiDynVVolIfSnapshotMyStatus_Object = MibTableColumn
eqliscsiDynVVolIfSnapshotMyStatus = _EqliscsiDynVVolIfSnapshotMyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 12),
    _EqliscsiDynVVolIfSnapshotMyStatus_Type()
)
eqliscsiDynVVolIfSnapshotMyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiDynVVolIfSnapshotMyStatus.setStatus("current")


class _EqliscsiDynVVolPsvid_Type(OctetString):
    """Custom type eqliscsiDynVVolPsvid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiDynVVolPsvid_Type.__name__ = "OctetString"
_EqliscsiDynVVolPsvid_Object = MibTableColumn
eqliscsiDynVVolPsvid = _EqliscsiDynVVolPsvid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 86, 1, 13),
    _EqliscsiDynVVolPsvid_Type()
)
eqliscsiDynVVolPsvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiDynVVolPsvid.setStatus("current")
_EqlDynamicSharedVolumeCopyTable_Object = MibTable
eqlDynamicSharedVolumeCopyTable = _EqlDynamicSharedVolumeCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 87)
)
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeCopyTable.setStatus("current")
_EqlDynamicSharedVolumeCopyEntry_Object = MibTableRow
eqlDynamicSharedVolumeCopyEntry = _EqlDynamicSharedVolumeCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 87, 1)
)
eqlDynamicSharedVolumeCopyEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeCopyEntry.setStatus("current")
_EqlDynamicSharedVolumeCopyRowStatus_Type = RowStatus
_EqlDynamicSharedVolumeCopyRowStatus_Object = MibTableColumn
eqlDynamicSharedVolumeCopyRowStatus = _EqlDynamicSharedVolumeCopyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 87, 1, 1),
    _EqlDynamicSharedVolumeCopyRowStatus_Type()
)
eqlDynamicSharedVolumeCopyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeCopyRowStatus.setStatus("current")
_EqlDynamicSharedVolumeCopyDestSharedVolume_Type = EQL2PartRowPointerStr
_EqlDynamicSharedVolumeCopyDestSharedVolume_Object = MibTableColumn
eqlDynamicSharedVolumeCopyDestSharedVolume = _EqlDynamicSharedVolumeCopyDestSharedVolume_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 87, 1, 2),
    _EqlDynamicSharedVolumeCopyDestSharedVolume_Type()
)
eqlDynamicSharedVolumeCopyDestSharedVolume.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeCopyDestSharedVolume.setStatus("current")
_EqlDynamicSharedVolumeCopySourceSharedVolume_Type = EQL2PartRowPointerStr
_EqlDynamicSharedVolumeCopySourceSharedVolume_Object = MibTableColumn
eqlDynamicSharedVolumeCopySourceSharedVolume = _EqlDynamicSharedVolumeCopySourceSharedVolume_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 87, 1, 3),
    _EqlDynamicSharedVolumeCopySourceSharedVolume_Type()
)
eqlDynamicSharedVolumeCopySourceSharedVolume.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeCopySourceSharedVolume.setStatus("current")
_EqlDynamicSharedVolumeBindUnbindTable_Object = MibTable
eqlDynamicSharedVolumeBindUnbindTable = _EqlDynamicSharedVolumeBindUnbindTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 88)
)
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeBindUnbindTable.setStatus("current")
_EqlDynamicSharedVolumeBindUnbindEntry_Object = MibTableRow
eqlDynamicSharedVolumeBindUnbindEntry = _EqlDynamicSharedVolumeBindUnbindEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 88, 1)
)
eqlDynamicSharedVolumeBindUnbindEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeBindUnbindEntry.setStatus("current")
_EqlDynamicSharedVolumeBindUnbindRowStatus_Type = RowStatus
_EqlDynamicSharedVolumeBindUnbindRowStatus_Object = MibTableColumn
eqlDynamicSharedVolumeBindUnbindRowStatus = _EqlDynamicSharedVolumeBindUnbindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 88, 1, 1),
    _EqlDynamicSharedVolumeBindUnbindRowStatus_Type()
)
eqlDynamicSharedVolumeBindUnbindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeBindUnbindRowStatus.setStatus("current")


class _EqlDynamicSharedVolumeBindUnbindOper_Type(Integer32):
    """Custom type eqlDynamicSharedVolumeBindUnbindOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bind", 1),
          ("unbind", 2))
    )


_EqlDynamicSharedVolumeBindUnbindOper_Type.__name__ = "Integer32"
_EqlDynamicSharedVolumeBindUnbindOper_Object = MibTableColumn
eqlDynamicSharedVolumeBindUnbindOper = _EqlDynamicSharedVolumeBindUnbindOper_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 88, 1, 2),
    _EqlDynamicSharedVolumeBindUnbindOper_Type()
)
eqlDynamicSharedVolumeBindUnbindOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeBindUnbindOper.setStatus("current")
_EqlDynamicSharedVolumeBindUnbindAccessGroupIndex_Type = Unsigned32
_EqlDynamicSharedVolumeBindUnbindAccessGroupIndex_Object = MibTableColumn
eqlDynamicSharedVolumeBindUnbindAccessGroupIndex = _EqlDynamicSharedVolumeBindUnbindAccessGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 88, 1, 3),
    _EqlDynamicSharedVolumeBindUnbindAccessGroupIndex_Type()
)
eqlDynamicSharedVolumeBindUnbindAccessGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeBindUnbindAccessGroupIndex.setStatus("current")


class _EqlDynamicSharedVolumeBindUnbindOperAugment_Type(Integer32):
    """Custom type eqlDynamicSharedVolumeBindUnbindOperAugment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotUpdateAccess", 2),
          ("update", 0),
          ("updateAccess", 1))
    )


_EqlDynamicSharedVolumeBindUnbindOperAugment_Type.__name__ = "Integer32"
_EqlDynamicSharedVolumeBindUnbindOperAugment_Object = MibTableColumn
eqlDynamicSharedVolumeBindUnbindOperAugment = _EqlDynamicSharedVolumeBindUnbindOperAugment_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 88, 1, 4),
    _EqlDynamicSharedVolumeBindUnbindOperAugment_Type()
)
eqlDynamicSharedVolumeBindUnbindOperAugment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeBindUnbindOperAugment.setStatus("current")
_EqliscsiSharedVolumeMetadataTable_Object = MibTable
eqliscsiSharedVolumeMetadataTable = _EqliscsiSharedVolumeMetadataTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 89)
)
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeMetadataTable.setStatus("current")
_EqliscsiSharedVolumeMetadataEntry_Object = MibTableRow
eqliscsiSharedVolumeMetadataEntry = _EqliscsiSharedVolumeMetadataEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 89, 1)
)
eqliscsiSharedVolumeMetadataEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeMetadataIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeMetadataEntry.setStatus("current")
_EqliscsiSharedVolumeMetadataRowStatus_Type = RowStatus
_EqliscsiSharedVolumeMetadataRowStatus_Object = MibTableColumn
eqliscsiSharedVolumeMetadataRowStatus = _EqliscsiSharedVolumeMetadataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 89, 1, 1),
    _EqliscsiSharedVolumeMetadataRowStatus_Type()
)
eqliscsiSharedVolumeMetadataRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeMetadataRowStatus.setStatus("current")
_EqliscsiSharedVolumeMetadataIndex_Type = Unsigned32
_EqliscsiSharedVolumeMetadataIndex_Object = MibTableColumn
eqliscsiSharedVolumeMetadataIndex = _EqliscsiSharedVolumeMetadataIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 89, 1, 2),
    _EqliscsiSharedVolumeMetadataIndex_Type()
)
eqliscsiSharedVolumeMetadataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeMetadataIndex.setStatus("current")


class _EqliscsiSharedVolumeMetadataKey_Type(UTFString):
    """Custom type eqliscsiSharedVolumeMetadataKey based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_EqliscsiSharedVolumeMetadataKey_Type.__name__ = "UTFString"
_EqliscsiSharedVolumeMetadataKey_Object = MibTableColumn
eqliscsiSharedVolumeMetadataKey = _EqliscsiSharedVolumeMetadataKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 89, 1, 3),
    _EqliscsiSharedVolumeMetadataKey_Type()
)
eqliscsiSharedVolumeMetadataKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeMetadataKey.setStatus("current")


class _EqliscsiSharedVolumeMetadataValue_Type(UTFString):
    """Custom type eqliscsiSharedVolumeMetadataValue based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EqliscsiSharedVolumeMetadataValue_Type.__name__ = "UTFString"
_EqliscsiSharedVolumeMetadataValue_Object = MibTableColumn
eqliscsiSharedVolumeMetadataValue = _EqliscsiSharedVolumeMetadataValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 89, 1, 4),
    _EqliscsiSharedVolumeMetadataValue_Type()
)
eqliscsiSharedVolumeMetadataValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeMetadataValue.setStatus("current")
_EqlPreppedSnapshotVVolTable_Object = MibTable
eqlPreppedSnapshotVVolTable = _EqlPreppedSnapshotVVolTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 90)
)
if mibBuilder.loadTexts:
    eqlPreppedSnapshotVVolTable.setStatus("current")
_EqlPreppedSnapshotVVolEntry_Object = MibTableRow
eqlPreppedSnapshotVVolEntry = _EqlPreppedSnapshotVVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 90, 1)
)
eqlPreppedSnapshotVVolEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqlPreppedSnapshotVVolEntry.setStatus("current")
_EqlPreppedSnapshotVVolRowStatus_Type = RowStatus
_EqlPreppedSnapshotVVolRowStatus_Object = MibTableColumn
eqlPreppedSnapshotVVolRowStatus = _EqlPreppedSnapshotVVolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 90, 1, 1),
    _EqlPreppedSnapshotVVolRowStatus_Type()
)
eqlPreppedSnapshotVVolRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPreppedSnapshotVVolRowStatus.setStatus("current")


class _EqlPreppedSnapshotVVolPsvid_Type(OctetString):
    """Custom type eqlPreppedSnapshotVVolPsvid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlPreppedSnapshotVVolPsvid_Type.__name__ = "OctetString"
_EqlPreppedSnapshotVVolPsvid_Object = MibTableColumn
eqlPreppedSnapshotVVolPsvid = _EqlPreppedSnapshotVVolPsvid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 90, 1, 2),
    _EqlPreppedSnapshotVVolPsvid_Type()
)
eqlPreppedSnapshotVVolPsvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPreppedSnapshotVVolPsvid.setStatus("current")


class _EqlPreppedSnapshotVVolName_Type(UTFString):
    """Custom type eqlPreppedSnapshotVVolName based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlPreppedSnapshotVVolName_Type.__name__ = "UTFString"
_EqlPreppedSnapshotVVolName_Object = MibTableColumn
eqlPreppedSnapshotVVolName = _EqlPreppedSnapshotVVolName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 90, 1, 3),
    _EqlPreppedSnapshotVVolName_Type()
)
eqlPreppedSnapshotVVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPreppedSnapshotVVolName.setStatus("current")
_EqlPreppedSnapshotVVolSize_Type = Integer32
_EqlPreppedSnapshotVVolSize_Object = MibTableColumn
eqlPreppedSnapshotVVolSize = _EqlPreppedSnapshotVVolSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 90, 1, 4),
    _EqlPreppedSnapshotVVolSize_Type()
)
eqlPreppedSnapshotVVolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPreppedSnapshotVVolSize.setStatus("current")
if mibBuilder.loadTexts:
    eqlPreppedSnapshotVVolSize.setUnits("MB")
_EqlPreppedSnapshotVVolMyParentVVol_Type = EQL2PartRowPointerStr
_EqlPreppedSnapshotVVolMyParentVVol_Object = MibTableColumn
eqlPreppedSnapshotVVolMyParentVVol = _EqlPreppedSnapshotVVolMyParentVVol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 90, 1, 5),
    _EqlPreppedSnapshotVVolMyParentVVol_Type()
)
eqlPreppedSnapshotVVolMyParentVVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPreppedSnapshotVVolMyParentVVol.setStatus("current")
_EqlPreppedSnapshotVVolBucket_Type = EQL2PartRowPointerStr
_EqlPreppedSnapshotVVolBucket_Object = MibTableColumn
eqlPreppedSnapshotVVolBucket = _EqlPreppedSnapshotVVolBucket_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 90, 1, 6),
    _EqlPreppedSnapshotVVolBucket_Type()
)
eqlPreppedSnapshotVVolBucket.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlPreppedSnapshotVVolBucket.setStatus("current")


class _EqlPreppedSnapshotVVolDescription_Type(UTFString):
    """Custom type eqlPreppedSnapshotVVolDescription based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlPreppedSnapshotVVolDescription_Type.__name__ = "UTFString"
_EqlPreppedSnapshotVVolDescription_Object = MibTableColumn
eqlPreppedSnapshotVVolDescription = _EqlPreppedSnapshotVVolDescription_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 90, 1, 7),
    _EqlPreppedSnapshotVVolDescription_Type()
)
eqlPreppedSnapshotVVolDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlPreppedSnapshotVVolDescription.setStatus("current")
_EqlDynamicSharedVolumeDiffTable_Object = MibTable
eqlDynamicSharedVolumeDiffTable = _EqlDynamicSharedVolumeDiffTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 91)
)
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffTable.setStatus("current")
_EqlDynamicSharedVolumeDiffEntry_Object = MibTableRow
eqlDynamicSharedVolumeDiffEntry = _EqlDynamicSharedVolumeDiffEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 91, 1)
)
eqlDynamicSharedVolumeDiffEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffEntry.setStatus("current")
_EqlDynamicSharedVolumeDiffRowStatus_Type = RowStatus
_EqlDynamicSharedVolumeDiffRowStatus_Object = MibTableColumn
eqlDynamicSharedVolumeDiffRowStatus = _EqlDynamicSharedVolumeDiffRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 91, 1, 1),
    _EqlDynamicSharedVolumeDiffRowStatus_Type()
)
eqlDynamicSharedVolumeDiffRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffRowStatus.setStatus("current")
_EqlDynamicSharedVolumeDiffBaseIndex_Type = EQL2PartRowPointerStr
_EqlDynamicSharedVolumeDiffBaseIndex_Object = MibTableColumn
eqlDynamicSharedVolumeDiffBaseIndex = _EqlDynamicSharedVolumeDiffBaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 91, 1, 2),
    _EqlDynamicSharedVolumeDiffBaseIndex_Type()
)
eqlDynamicSharedVolumeDiffBaseIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffBaseIndex.setStatus("current")


class _EqlDynamicSharedVolumeDiffAdmin_Type(Integer32):
    """Custom type eqlDynamicSharedVolumeDiffAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allocatedBitMap", 2),
          ("unSharedBitMap", 1),
          ("unsharedChunks", 3))
    )


_EqlDynamicSharedVolumeDiffAdmin_Type.__name__ = "Integer32"
_EqlDynamicSharedVolumeDiffAdmin_Object = MibTableColumn
eqlDynamicSharedVolumeDiffAdmin = _EqlDynamicSharedVolumeDiffAdmin_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 91, 1, 3),
    _EqlDynamicSharedVolumeDiffAdmin_Type()
)
eqlDynamicSharedVolumeDiffAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffAdmin.setStatus("current")
_EqlDynamicSharedVolumeDiffStartSegmentOffset_Type = Counter64
_EqlDynamicSharedVolumeDiffStartSegmentOffset_Object = MibTableColumn
eqlDynamicSharedVolumeDiffStartSegmentOffset = _EqlDynamicSharedVolumeDiffStartSegmentOffset_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 91, 1, 4),
    _EqlDynamicSharedVolumeDiffStartSegmentOffset_Type()
)
eqlDynamicSharedVolumeDiffStartSegmentOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffStartSegmentOffset.setStatus("current")
_EqlDynamicSharedVolumeDiffSegmentsLength_Type = Counter64
_EqlDynamicSharedVolumeDiffSegmentsLength_Object = MibTableColumn
eqlDynamicSharedVolumeDiffSegmentsLength = _EqlDynamicSharedVolumeDiffSegmentsLength_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 91, 1, 5),
    _EqlDynamicSharedVolumeDiffSegmentsLength_Type()
)
eqlDynamicSharedVolumeDiffSegmentsLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffSegmentsLength.setStatus("current")
_EqlDynamicSharedVolumeDiffChunkSize_Type = Unsigned32
_EqlDynamicSharedVolumeDiffChunkSize_Object = MibTableColumn
eqlDynamicSharedVolumeDiffChunkSize = _EqlDynamicSharedVolumeDiffChunkSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 91, 1, 6),
    _EqlDynamicSharedVolumeDiffChunkSize_Type()
)
eqlDynamicSharedVolumeDiffChunkSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffChunkSize.setStatus("current")
_EqliscsiVolumeCompressionConfigurationTable_Object = MibTable
eqliscsiVolumeCompressionConfigurationTable = _EqliscsiVolumeCompressionConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 92)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeCompressionConfigurationTable.setStatus("current")
_EqliscsiVolumeCompressionConfigurationEntry_Object = MibTableRow
eqliscsiVolumeCompressionConfigurationEntry = _EqliscsiVolumeCompressionConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 92, 1)
)
eqliscsiVolumeCompressionConfigurationEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeCompressionConfigurationEntry.setStatus("current")
_EqliscsiVolumeCompressionConfigurationRowStatus_Type = RowStatus
_EqliscsiVolumeCompressionConfigurationRowStatus_Object = MibTableColumn
eqliscsiVolumeCompressionConfigurationRowStatus = _EqliscsiVolumeCompressionConfigurationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 92, 1, 1),
    _EqliscsiVolumeCompressionConfigurationRowStatus_Type()
)
eqliscsiVolumeCompressionConfigurationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeCompressionConfigurationRowStatus.setStatus("current")


class _EqliscsiVolumeCompressionConfigurationPolicy_Type(Integer32):
    """Custom type eqliscsiVolumeCompressionConfigurationPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("automatic", 0),
          ("never", 3),
          ("user-defined", 2))
    )


_EqliscsiVolumeCompressionConfigurationPolicy_Type.__name__ = "Integer32"
_EqliscsiVolumeCompressionConfigurationPolicy_Object = MibTableColumn
eqliscsiVolumeCompressionConfigurationPolicy = _EqliscsiVolumeCompressionConfigurationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 92, 1, 2),
    _EqliscsiVolumeCompressionConfigurationPolicy_Type()
)
eqliscsiVolumeCompressionConfigurationPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeCompressionConfigurationPolicy.setStatus("current")


class _EqliscsiVolumeCompressionConfigurationSnapDelay_Type(Integer32):
    """Custom type eqliscsiVolumeCompressionConfigurationSnapDelay based on Integer32"""
    defaultValue = 1440


_EqliscsiVolumeCompressionConfigurationSnapDelay_Object = MibTableColumn
eqliscsiVolumeCompressionConfigurationSnapDelay = _EqliscsiVolumeCompressionConfigurationSnapDelay_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 92, 1, 3),
    _EqliscsiVolumeCompressionConfigurationSnapDelay_Type()
)
eqliscsiVolumeCompressionConfigurationSnapDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeCompressionConfigurationSnapDelay.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiVolumeCompressionConfigurationSnapDelay.setUnits("minutes")
_EqlDynamicSharedVolumeDiffChunkTable_Object = MibTable
eqlDynamicSharedVolumeDiffChunkTable = _EqlDynamicSharedVolumeDiffChunkTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 93)
)
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffChunkTable.setStatus("current")
_EqlDynamicSharedVolumeDiffChunkEntry_Object = MibTableRow
eqlDynamicSharedVolumeDiffChunkEntry = _EqlDynamicSharedVolumeDiffChunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 93, 1)
)
eqlDynamicSharedVolumeDiffChunkEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiSharedVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqlDynamicSharedVolumeDiffChunkIndex"),
)
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffChunkEntry.setStatus("current")
_EqlDynamicSharedVolumeDiffChunkIndex_Type = Unsigned32
_EqlDynamicSharedVolumeDiffChunkIndex_Object = MibTableColumn
eqlDynamicSharedVolumeDiffChunkIndex = _EqlDynamicSharedVolumeDiffChunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 93, 1, 1),
    _EqlDynamicSharedVolumeDiffChunkIndex_Type()
)
eqlDynamicSharedVolumeDiffChunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffChunkIndex.setStatus("current")
_EqlDynamicSharedVolumeDiffChunkSegmentSize_Type = Unsigned32
_EqlDynamicSharedVolumeDiffChunkSegmentSize_Object = MibTableColumn
eqlDynamicSharedVolumeDiffChunkSegmentSize = _EqlDynamicSharedVolumeDiffChunkSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 93, 1, 2),
    _EqlDynamicSharedVolumeDiffChunkSegmentSize_Type()
)
eqlDynamicSharedVolumeDiffChunkSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffChunkSegmentSize.setStatus("current")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffChunkSegmentSize.setUnits("KB")
_EqlDynamicSharedVolumeDiffNumChunkSegments_Type = Unsigned32
_EqlDynamicSharedVolumeDiffNumChunkSegments_Object = MibTableColumn
eqlDynamicSharedVolumeDiffNumChunkSegments = _EqlDynamicSharedVolumeDiffNumChunkSegments_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 93, 1, 3),
    _EqlDynamicSharedVolumeDiffNumChunkSegments_Type()
)
eqlDynamicSharedVolumeDiffNumChunkSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffNumChunkSegments.setStatus("current")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffNumChunkSegments.setUnits("segments")


class _EqlDynamicSharedVolumeDiffChunkModified_Type(OctetString):
    """Custom type eqlDynamicSharedVolumeDiffChunkModified based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1024, 1024),
    )


_EqlDynamicSharedVolumeDiffChunkModified_Type.__name__ = "OctetString"
_EqlDynamicSharedVolumeDiffChunkModified_Object = MibTableColumn
eqlDynamicSharedVolumeDiffChunkModified = _EqlDynamicSharedVolumeDiffChunkModified_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 93, 1, 4),
    _EqlDynamicSharedVolumeDiffChunkModified_Type()
)
eqlDynamicSharedVolumeDiffChunkModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlDynamicSharedVolumeDiffChunkModified.setStatus("current")
_EqliscsiVolumeMetadataTable_Object = MibTable
eqliscsiVolumeMetadataTable = _EqliscsiVolumeMetadataTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 94)
)
if mibBuilder.loadTexts:
    eqliscsiVolumeMetadataTable.setStatus("current")
_EqliscsiVolumeMetadataEntry_Object = MibTableRow
eqliscsiVolumeMetadataEntry = _EqliscsiVolumeMetadataEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 94, 1)
)
eqliscsiVolumeMetadataEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeMetadataIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiVolumeMetadataEntry.setStatus("current")
_EqliscsiVolumeMetadataRowStatus_Type = RowStatus
_EqliscsiVolumeMetadataRowStatus_Object = MibTableColumn
eqliscsiVolumeMetadataRowStatus = _EqliscsiVolumeMetadataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 94, 1, 1),
    _EqliscsiVolumeMetadataRowStatus_Type()
)
eqliscsiVolumeMetadataRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeMetadataRowStatus.setStatus("current")
_EqliscsiVolumeMetadataIndex_Type = Unsigned32
_EqliscsiVolumeMetadataIndex_Object = MibTableColumn
eqliscsiVolumeMetadataIndex = _EqliscsiVolumeMetadataIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 94, 1, 2),
    _EqliscsiVolumeMetadataIndex_Type()
)
eqliscsiVolumeMetadataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiVolumeMetadataIndex.setStatus("current")


class _EqliscsiVolumeMetadataKey_Type(UTFString):
    """Custom type eqliscsiVolumeMetadataKey based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_EqliscsiVolumeMetadataKey_Type.__name__ = "UTFString"
_EqliscsiVolumeMetadataKey_Object = MibTableColumn
eqliscsiVolumeMetadataKey = _EqliscsiVolumeMetadataKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 94, 1, 3),
    _EqliscsiVolumeMetadataKey_Type()
)
eqliscsiVolumeMetadataKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeMetadataKey.setStatus("current")


class _EqliscsiVolumeMetadataValue_Type(UTFString):
    """Custom type eqliscsiVolumeMetadataValue based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EqliscsiVolumeMetadataValue_Type.__name__ = "UTFString"
_EqliscsiVolumeMetadataValue_Object = MibTableColumn
eqliscsiVolumeMetadataValue = _EqliscsiVolumeMetadataValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 94, 1, 4),
    _EqliscsiVolumeMetadataValue_Type()
)
eqliscsiVolumeMetadataValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiVolumeMetadataValue.setStatus("current")
_EqliscsiSnapshotMetadataTable_Object = MibTable
eqliscsiSnapshotMetadataTable = _EqliscsiSnapshotMetadataTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 95)
)
if mibBuilder.loadTexts:
    eqliscsiSnapshotMetadataTable.setStatus("current")
_EqliscsiSnapshotMetadataEntry_Object = MibTableRow
eqliscsiSnapshotMetadataEntry = _EqliscsiSnapshotMetadataEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 95, 1)
)
eqliscsiSnapshotMetadataEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiSnapshotIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiSnapshotMetadataIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiSnapshotMetadataEntry.setStatus("current")
_EqliscsiSnapshotMetadataRowStatus_Type = RowStatus
_EqliscsiSnapshotMetadataRowStatus_Object = MibTableColumn
eqliscsiSnapshotMetadataRowStatus = _EqliscsiSnapshotMetadataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 95, 1, 1),
    _EqliscsiSnapshotMetadataRowStatus_Type()
)
eqliscsiSnapshotMetadataRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotMetadataRowStatus.setStatus("current")
_EqliscsiSnapshotMetadataIndex_Type = Unsigned32
_EqliscsiSnapshotMetadataIndex_Object = MibTableColumn
eqliscsiSnapshotMetadataIndex = _EqliscsiSnapshotMetadataIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 95, 1, 2),
    _EqliscsiSnapshotMetadataIndex_Type()
)
eqliscsiSnapshotMetadataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSnapshotMetadataIndex.setStatus("current")


class _EqliscsiSnapshotMetadataKey_Type(UTFString):
    """Custom type eqliscsiSnapshotMetadataKey based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_EqliscsiSnapshotMetadataKey_Type.__name__ = "UTFString"
_EqliscsiSnapshotMetadataKey_Object = MibTableColumn
eqliscsiSnapshotMetadataKey = _EqliscsiSnapshotMetadataKey_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 95, 1, 3),
    _EqliscsiSnapshotMetadataKey_Type()
)
eqliscsiSnapshotMetadataKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotMetadataKey.setStatus("current")


class _EqliscsiSnapshotMetadataValue_Type(UTFString):
    """Custom type eqliscsiSnapshotMetadataValue based on UTFString"""
    subtypeSpec = UTFString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EqliscsiSnapshotMetadataValue_Type.__name__ = "UTFString"
_EqliscsiSnapshotMetadataValue_Object = MibTableColumn
eqliscsiSnapshotMetadataValue = _EqliscsiSnapshotMetadataValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 95, 1, 4),
    _EqliscsiSnapshotMetadataValue_Type()
)
eqliscsiSnapshotMetadataValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqliscsiSnapshotMetadataValue.setStatus("current")
_EqliscsiSyncReplAfoTiebreakerTable_Object = MibTable
eqliscsiSyncReplAfoTiebreakerTable = _EqliscsiSyncReplAfoTiebreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 96)
)
if mibBuilder.loadTexts:
    eqliscsiSyncReplAfoTiebreakerTable.setStatus("current")
_EqliscsiSyncReplAfoTiebreakerEntry_Object = MibTableRow
eqliscsiSyncReplAfoTiebreakerEntry = _EqliscsiSyncReplAfoTiebreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 96, 1)
)
eqliscsiSyncReplAfoTiebreakerEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId0"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId1"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId2"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeLowPsvId3"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId0"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId1"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId2"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeHighPsvId3"),
)
if mibBuilder.loadTexts:
    eqliscsiSyncReplAfoTiebreakerEntry.setStatus("current")
_EqliscsiSyncReplAfoTiebreakerSeqNum_Type = Counter64
_EqliscsiSyncReplAfoTiebreakerSeqNum_Object = MibTableColumn
eqliscsiSyncReplAfoTiebreakerSeqNum = _EqliscsiSyncReplAfoTiebreakerSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 96, 1, 1),
    _EqliscsiSyncReplAfoTiebreakerSeqNum_Type()
)
eqliscsiSyncReplAfoTiebreakerSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSyncReplAfoTiebreakerSeqNum.setStatus("current")


class _EqliscsiSyncReplAfoTiebreaker_Type(OctetString):
    """Custom type eqliscsiSyncReplAfoTiebreaker based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiSyncReplAfoTiebreaker_Type.__name__ = "OctetString"
_EqliscsiSyncReplAfoTiebreaker_Object = MibTableColumn
eqliscsiSyncReplAfoTiebreaker = _EqliscsiSyncReplAfoTiebreaker_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 96, 1, 2),
    _EqliscsiSyncReplAfoTiebreaker_Type()
)
eqliscsiSyncReplAfoTiebreaker.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSyncReplAfoTiebreaker.setStatus("current")


class _EqliscsiSyncReplAfoTiebreakerGrpLeadUuid_Type(OctetString):
    """Custom type eqliscsiSyncReplAfoTiebreakerGrpLeadUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqliscsiSyncReplAfoTiebreakerGrpLeadUuid_Type.__name__ = "OctetString"
_EqliscsiSyncReplAfoTiebreakerGrpLeadUuid_Object = MibTableColumn
eqliscsiSyncReplAfoTiebreakerGrpLeadUuid = _EqliscsiSyncReplAfoTiebreakerGrpLeadUuid_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 96, 1, 3),
    _EqliscsiSyncReplAfoTiebreakerGrpLeadUuid_Type()
)
eqliscsiSyncReplAfoTiebreakerGrpLeadUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqliscsiSyncReplAfoTiebreakerGrpLeadUuid.setStatus("current")
_EqliscsiSharedVolumeStatisticsTable_Object = MibTable
eqliscsiSharedVolumeStatisticsTable = _EqliscsiSharedVolumeStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97)
)
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatisticsTable.setStatus("current")
_EqliscsiSharedVolumeStatisticsEntry_Object = MibTableRow
eqliscsiSharedVolumeStatisticsEntry = _EqliscsiSharedVolumeStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1)
)
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatisticsEntry.setStatus("current")
_EqliscsiSharedVolumeStatsCmdPdus_Type = Counter32
_EqliscsiSharedVolumeStatsCmdPdus_Object = MibTableColumn
eqliscsiSharedVolumeStatsCmdPdus = _EqliscsiSharedVolumeStatsCmdPdus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 1),
    _EqliscsiSharedVolumeStatsCmdPdus_Type()
)
eqliscsiSharedVolumeStatsCmdPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsCmdPdus.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsCmdPdus.setUnits("PDUs")
_EqliscsiSharedVolumeStatsRspPdus_Type = Counter32
_EqliscsiSharedVolumeStatsRspPdus_Object = MibTableColumn
eqliscsiSharedVolumeStatsRspPdus = _EqliscsiSharedVolumeStatsRspPdus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 2),
    _EqliscsiSharedVolumeStatsRspPdus_Type()
)
eqliscsiSharedVolumeStatsRspPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsRspPdus.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsRspPdus.setUnits("PDUs")
_EqliscsiSharedVolumeStatsTxData_Type = Counter64
_EqliscsiSharedVolumeStatsTxData_Object = MibTableColumn
eqliscsiSharedVolumeStatsTxData = _EqliscsiSharedVolumeStatsTxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 3),
    _EqliscsiSharedVolumeStatsTxData_Type()
)
eqliscsiSharedVolumeStatsTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsTxData.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsTxData.setUnits("octets")
_EqliscsiSharedVolumeStatsRxData_Type = Counter64
_EqliscsiSharedVolumeStatsRxData_Object = MibTableColumn
eqliscsiSharedVolumeStatsRxData = _EqliscsiSharedVolumeStatsRxData_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 4),
    _EqliscsiSharedVolumeStatsRxData_Type()
)
eqliscsiSharedVolumeStatsRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsRxData.setStatus("current")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsRxData.setUnits("octets")
_EqliscsiSharedVolumeStatsNoOfSessions_Type = Unsigned32
_EqliscsiSharedVolumeStatsNoOfSessions_Object = MibTableColumn
eqliscsiSharedVolumeStatsNoOfSessions = _EqliscsiSharedVolumeStatsNoOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 5),
    _EqliscsiSharedVolumeStatsNoOfSessions_Type()
)
eqliscsiSharedVolumeStatsNoOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsNoOfSessions.setStatus("current")
_EqliscsiSharedVolumeStatsReadLatency_Type = Counter64
_EqliscsiSharedVolumeStatsReadLatency_Object = MibTableColumn
eqliscsiSharedVolumeStatsReadLatency = _EqliscsiSharedVolumeStatsReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 6),
    _EqliscsiSharedVolumeStatsReadLatency_Type()
)
eqliscsiSharedVolumeStatsReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsReadLatency.setStatus("current")
_EqliscsiSharedVolumeStatsWriteLatency_Type = Counter64
_EqliscsiSharedVolumeStatsWriteLatency_Object = MibTableColumn
eqliscsiSharedVolumeStatsWriteLatency = _EqliscsiSharedVolumeStatsWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 7),
    _EqliscsiSharedVolumeStatsWriteLatency_Type()
)
eqliscsiSharedVolumeStatsWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsWriteLatency.setStatus("current")
_EqliscsiSharedVolumeStatsReadOpCount_Type = Counter64
_EqliscsiSharedVolumeStatsReadOpCount_Object = MibTableColumn
eqliscsiSharedVolumeStatsReadOpCount = _EqliscsiSharedVolumeStatsReadOpCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 8),
    _EqliscsiSharedVolumeStatsReadOpCount_Type()
)
eqliscsiSharedVolumeStatsReadOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsReadOpCount.setStatus("current")
_EqliscsiSharedVolumeStatsWriteOpCount_Type = Counter64
_EqliscsiSharedVolumeStatsWriteOpCount_Object = MibTableColumn
eqliscsiSharedVolumeStatsWriteOpCount = _EqliscsiSharedVolumeStatsWriteOpCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 9),
    _EqliscsiSharedVolumeStatsWriteOpCount_Type()
)
eqliscsiSharedVolumeStatsWriteOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsWriteOpCount.setStatus("current")
_EqliscsiSharedVolumeStatsReadAvgLatency_Type = Gauge32
_EqliscsiSharedVolumeStatsReadAvgLatency_Object = MibTableColumn
eqliscsiSharedVolumeStatsReadAvgLatency = _EqliscsiSharedVolumeStatsReadAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 10),
    _EqliscsiSharedVolumeStatsReadAvgLatency_Type()
)
eqliscsiSharedVolumeStatsReadAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsReadAvgLatency.setStatus("current")
_EqliscsiSharedVolumeStatsWriteAvgLatency_Type = Gauge32
_EqliscsiSharedVolumeStatsWriteAvgLatency_Object = MibTableColumn
eqliscsiSharedVolumeStatsWriteAvgLatency = _EqliscsiSharedVolumeStatsWriteAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 11),
    _EqliscsiSharedVolumeStatsWriteAvgLatency_Type()
)
eqliscsiSharedVolumeStatsWriteAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsWriteAvgLatency.setStatus("current")
_EqliscsiSharedVolumeStatsHCIscsiReadWriteCmdsReceived_Type = Counter64
_EqliscsiSharedVolumeStatsHCIscsiReadWriteCmdsReceived_Object = MibTableColumn
eqliscsiSharedVolumeStatsHCIscsiReadWriteCmdsReceived = _EqliscsiSharedVolumeStatsHCIscsiReadWriteCmdsReceived_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 13),
    _EqliscsiSharedVolumeStatsHCIscsiReadWriteCmdsReceived_Type()
)
eqliscsiSharedVolumeStatsHCIscsiReadWriteCmdsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsHCIscsiReadWriteCmdsReceived.setStatus("current")
_EqliscsiSharedVolumeStatsHCIscsiTotalQD_Type = Counter64
_EqliscsiSharedVolumeStatsHCIscsiTotalQD_Object = MibTableColumn
eqliscsiSharedVolumeStatsHCIscsiTotalQD = _EqliscsiSharedVolumeStatsHCIscsiTotalQD_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 14),
    _EqliscsiSharedVolumeStatsHCIscsiTotalQD_Type()
)
eqliscsiSharedVolumeStatsHCIscsiTotalQD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsHCIscsiTotalQD.setStatus("current")
_EqliscsiSharedVolumeStatsMisAlignedIO_Type = Counter64
_EqliscsiSharedVolumeStatsMisAlignedIO_Object = MibTableColumn
eqliscsiSharedVolumeStatsMisAlignedIO = _EqliscsiSharedVolumeStatsMisAlignedIO_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 7, 97, 1, 15),
    _EqliscsiSharedVolumeStatsMisAlignedIO_Type()
)
eqliscsiSharedVolumeStatsMisAlignedIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiSharedVolumeStatsMisAlignedIO.setStatus("current")
_EqliscsiNodeTable_Object = MibTable
eqliscsiNodeTable = _EqliscsiNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 8)
)
if mibBuilder.loadTexts:
    eqliscsiNodeTable.setStatus("current")
_EqliscsiNodeEntry_Object = MibTableRow
eqliscsiNodeEntry = _EqliscsiNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 8, 1)
)
eqliscsiNodeEntry.setIndexNames(
    (0, "EQLVOLUME-MIB", "eqliscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    eqliscsiNodeEntry.setStatus("current")
_EqliscsiNodeIndex_Type = Unsigned32
_EqliscsiNodeIndex_Object = MibTableColumn
eqliscsiNodeIndex = _EqliscsiNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 8, 1, 1),
    _EqliscsiNodeIndex_Type()
)
eqliscsiNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiNodeIndex.setStatus("current")
_EqliscsiNodeLocalMemberId_Type = Unsigned32
_EqliscsiNodeLocalMemberId_Object = MibTableColumn
eqliscsiNodeLocalMemberId = _EqliscsiNodeLocalMemberId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 8, 1, 2),
    _EqliscsiNodeLocalMemberId_Type()
)
eqliscsiNodeLocalMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiNodeLocalMemberId.setStatus("current")
_EqliscsiNodeVolumeIndex_Type = Unsigned32
_EqliscsiNodeVolumeIndex_Object = MibTableColumn
eqliscsiNodeVolumeIndex = _EqliscsiNodeVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 8, 1, 3),
    _EqliscsiNodeVolumeIndex_Type()
)
eqliscsiNodeVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiNodeVolumeIndex.setStatus("current")
_EqliscsiNodeSnapshotIndex_Type = Unsigned32
_EqliscsiNodeSnapshotIndex_Object = MibTableColumn
eqliscsiNodeSnapshotIndex = _EqliscsiNodeSnapshotIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 5, 1, 8, 1, 4),
    _EqliscsiNodeSnapshotIndex_Type()
)
eqliscsiNodeSnapshotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqliscsiNodeSnapshotIndex.setStatus("current")
_EqliscsiNotifications_ObjectIdentity = ObjectIdentity
eqliscsiNotifications = _EqliscsiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 5, 2)
)
_EqliscsiConformance_ObjectIdentity = ObjectIdentity
eqliscsiConformance = _EqliscsiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 5, 3)
)
eqliscsiVolumeEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolumeStatusEntry")
)
eqliscsiVolumeStatusEntry.setIndexNames(*eqliscsiVolumeEntry.getIndexNames())
eqliscsiSnapshotEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiSnapshotStatusEntry")
)
eqliscsiSnapshotStatusEntry.setIndexNames(*eqliscsiSnapshotEntry.getIndexNames())
eqliscsiVolumeMemberEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolumeBindingEntry")
)
eqliscsiVolumeBindingEntry.setIndexNames(*eqliscsiVolumeMemberEntry.getIndexNames())
eqliscsiVolColReplicationEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolColReplStatusEntry")
)
eqliscsiVolColReplStatusEntry.setIndexNames(*eqliscsiVolColReplicationEntry.getIndexNames())
eqliscsiVolumeEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolumeStatisticsEntry")
)
eqliscsiVolumeStatisticsEntry.setIndexNames(*eqliscsiVolumeEntry.getIndexNames())
eqliscsiVolumeSnapshotPolicyEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolumeSnapshotPolicyStatusEntry")
)
eqliscsiVolumeSnapshotPolicyStatusEntry.setIndexNames(*eqliscsiVolumeSnapshotPolicyEntry.getIndexNames())
eqliscsiSnapCollectionPolicyEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiSnapCollectionPolicyStatusEntry")
)
eqliscsiSnapCollectionPolicyStatusEntry.setIndexNames(*eqliscsiSnapCollectionPolicyEntry.getIndexNames())
eqliscsiReplicaSetEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiReplicaSetExtensionEntry")
)
eqliscsiReplicaSetExtensionEntry.setIndexNames(*eqliscsiReplicaSetEntry.getIndexNames())
eqliscsiVolumeEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolumeStoragePreferenceEntry")
)
eqliscsiVolumeStoragePreferenceEntry.setIndexNames(*eqliscsiVolumeEntry.getIndexNames())
eqliscsiVolumeOpsEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolumeOpsStatusEntry")
)
eqliscsiVolumeOpsStatusEntry.setIndexNames(*eqliscsiVolumeOpsEntry.getIndexNames())
eqliscsiVolumeEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolumeDynamicConfigEntry")
)
eqliscsiVolumeDynamicConfigEntry.setIndexNames(*eqliscsiVolumeEntry.getIndexNames())
eqliscsiVolumeReplSiteEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolumeReplSiteStatusEntry")
)
eqliscsiVolumeReplSiteStatusEntry.setIndexNames(*eqliscsiVolumeReplSiteEntry.getIndexNames())
eqliscsiReplicantSiteOpsEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiReplicantSiteOpsStatusEntry")
)
eqliscsiReplicantSiteOpsStatusEntry.setIndexNames(*eqliscsiReplicantSiteOpsEntry.getIndexNames())
eqliscsiReplicantSiteEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiReplicantSiteStatusEntry")
)
eqliscsiReplicantSiteStatusEntry.setIndexNames(*eqliscsiReplicantSiteEntry.getIndexNames())
eqliscsiVolumeEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiTemplateVolumeStatusEntry")
)
eqliscsiTemplateVolumeStatusEntry.setIndexNames(*eqliscsiVolumeEntry.getIndexNames())
eqliscsiVolumeEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiSnapAccumulatedStatisticsEntry")
)
eqliscsiSnapAccumulatedStatisticsEntry.setIndexNames(*eqliscsiVolumeEntry.getIndexNames())
eqliscsiVolumeSyncReplVirtualEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolumeSyncReplVirtualStatusEntry")
)
eqliscsiVolumeSyncReplVirtualStatusEntry.setIndexNames(*eqliscsiVolumeSyncReplVirtualEntry.getIndexNames())
eqliscsiVolumeSyncReplVirtualEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiVolumeSyncReplVirtualStatisticsEntry")
)
eqliscsiVolumeSyncReplVirtualStatisticsEntry.setIndexNames(*eqliscsiVolumeSyncReplVirtualEntry.getIndexNames())
eqliscsiSharedVolumeEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiSharedVolumeStatusEntry")
)
eqliscsiSharedVolumeStatusEntry.setIndexNames(*eqliscsiSharedVolumeEntry.getIndexNames())
eqliscsiSharedVolumeEntry.registerAugmentions(
    ("EQLVOLUME-MIB",
     "eqliscsiSharedVolumeStatisticsEntry")
)
eqliscsiSharedVolumeStatisticsEntry.setIndexNames(*eqliscsiSharedVolumeEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLVOLUME-MIB",
    **{"ACLAppliesTo": ACLAppliesTo,
       "SiteIndex": SiteIndex,
       "SiteIndexOrZero": SiteIndexOrZero,
       "ReplSiteQuotaType": ReplSiteQuotaType,
       "StatusEnabledDefault": StatusEnabledDefault,
       "StatusDisabledDefault": StatusDisabledDefault,
       "StatusAutoDefault": StatusAutoDefault,
       "VirtualVolumeType": VirtualVolumeType,
       "EQLRowPointer": EQLRowPointer,
       "EQL2PartRowPointerStr": EQL2PartRowPointerStr,
       "VirtualVolumeSnapshotStatus": VirtualVolumeSnapshotStatus,
       "VirtualVolumeCreatedAs": VirtualVolumeCreatedAs,
       "eqliscsiModule": eqliscsiModule,
       "eqliscsiObjects": eqliscsiObjects,
       "eqliscsiTarget": eqliscsiTarget,
       "eqliscsiVolumeTable": eqliscsiVolumeTable,
       "eqliscsiVolumeEntry": eqliscsiVolumeEntry,
       "eqliscsiVolumeIndex": eqliscsiVolumeIndex,
       "eqliscsiVolumeRowStatus": eqliscsiVolumeRowStatus,
       "eqliscsiVolumePsvId": eqliscsiVolumePsvId,
       "eqliscsiVolumeName": eqliscsiVolumeName,
       "eqliscsiVolumeSite": eqliscsiVolumeSite,
       "eqliscsiVolumeDescription": eqliscsiVolumeDescription,
       "eqliscsiVolumeAccessType": eqliscsiVolumeAccessType,
       "eqliscsiVolumeSize": eqliscsiVolumeSize,
       "eqliscsiVolumeAdminStatus": eqliscsiVolumeAdminStatus,
       "eqliscsiVolumeReservedPercentage": eqliscsiVolumeReservedPercentage,
       "eqliscsiVolumeSnapWarningLevel": eqliscsiVolumeSnapWarningLevel,
       "eqliscsiVolumeSnapDeletionPolicy": eqliscsiVolumeSnapDeletionPolicy,
       "eqliscsiVolumeAutoloadBalancing": eqliscsiVolumeAutoloadBalancing,
       "eqliscsiVolumeTargetAlias": eqliscsiVolumeTargetAlias,
       "eqliscsiVolumeTargetIscsiName": eqliscsiVolumeTargetIscsiName,
       "eqliscsiVolumeNodeIndex": eqliscsiVolumeNodeIndex,
       "eqliscsiVolumeHdrDigests": eqliscsiVolumeHdrDigests,
       "eqliscsiVolumeDataDigests": eqliscsiVolumeDataDigests,
       "eqliscsiVolumeCloneSrcPsvId": eqliscsiVolumeCloneSrcPsvId,
       "eqliscsiVolumeReplService": eqliscsiVolumeReplService,
       "eqliscsiVolumeMultInitiator": eqliscsiVolumeMultInitiator,
       "eqliscsiVolumeStoragePoolIndex": eqliscsiVolumeStoragePoolIndex,
       "eqliscsiVolumeStoragePoolSourceIndex": eqliscsiVolumeStoragePoolSourceIndex,
       "eqliscsiVolumeTargetLocalMemberId": eqliscsiVolumeTargetLocalMemberId,
       "eqliscsiVolumeTargetIndex": eqliscsiVolumeTargetIndex,
       "eqliscsiVolumeThinProvision": eqliscsiVolumeThinProvision,
       "eqliscsiVolumeMinThinReserve": eqliscsiVolumeMinThinReserve,
       "eqliscsiVolumeThinWarnPercentage": eqliscsiVolumeThinWarnPercentage,
       "eqliscsiVolumeThinMaxGrowPercentage": eqliscsiVolumeThinMaxGrowPercentage,
       "eqliscsiVolumeShrinkAutoAdjust": eqliscsiVolumeShrinkAutoAdjust,
       "eqliscsiVolumeReplRollbackSeqNum": eqliscsiVolumeReplRollbackSeqNum,
       "eqliscsiVolumeThinWarnMode": eqliscsiVolumeThinWarnMode,
       "eqliscsiVolumeFlags": eqliscsiVolumeFlags,
       "eqliscsiVolumeTemplate": eqliscsiVolumeTemplate,
       "eqliscsiVolumeThinClone": eqliscsiVolumeThinClone,
       "eqliscsiVolumeThinCloneParentMemberId": eqliscsiVolumeThinCloneParentMemberId,
       "eqliscsiVolumeThinCloneParentVolIndex": eqliscsiVolumeThinCloneParentVolIndex,
       "eqliscsiVolumeThinCloneParentPsvId": eqliscsiVolumeThinCloneParentPsvId,
       "eqliscsiVolumeAdminAccountKey": eqliscsiVolumeAdminAccountKey,
       "eqliscsiVolumeSCSIQErr": eqliscsiVolumeSCSIQErr,
       "eqliscsiVolumeBorrow": eqliscsiVolumeBorrow,
       "eqliscsiVolumeSectorSize": eqliscsiVolumeSectorSize,
       "eqliscsiSnapshotTable": eqliscsiSnapshotTable,
       "eqliscsiSnapshotEntry": eqliscsiSnapshotEntry,
       "eqliscsiSnapshotIndex": eqliscsiSnapshotIndex,
       "eqliscsiSnapshotRowStatus": eqliscsiSnapshotRowStatus,
       "eqliscsiSnapshotPsvId": eqliscsiSnapshotPsvId,
       "eqliscsiSnapshotBasePsvId": eqliscsiSnapshotBasePsvId,
       "eqliscsiSnapshotName": eqliscsiSnapshotName,
       "eqliscsiSnapshotAccessType": eqliscsiSnapshotAccessType,
       "eqliscsiSnapshotSize": eqliscsiSnapshotSize,
       "eqliscsiSnapshotAdminStatus": eqliscsiSnapshotAdminStatus,
       "eqliscsiSnapshotTimestamp": eqliscsiSnapshotTimestamp,
       "eqliscsiSnapshotScheduleName": eqliscsiSnapshotScheduleName,
       "eqliscsiSnapshotRollBack": eqliscsiSnapshotRollBack,
       "eqliscsiSnapshotTargetAlias": eqliscsiSnapshotTargetAlias,
       "eqliscsiSnapshotTargetIscsiName": eqliscsiSnapshotTargetIscsiName,
       "eqliscsiSnapshotScheduleIndex": eqliscsiSnapshotScheduleIndex,
       "eqliscsiSnapshotDescription": eqliscsiSnapshotDescription,
       "eqliscsiSnapshotNodeIndex": eqliscsiSnapshotNodeIndex,
       "eqliscsiSnapshotReplicated": eqliscsiSnapshotReplicated,
       "eqliscsiSnapshotType": eqliscsiSnapshotType,
       "eqliscsiSnapshotCollectionIndex": eqliscsiSnapshotCollectionIndex,
       "eqliscsiSnapshotStoragePoolIndex": eqliscsiSnapshotStoragePoolIndex,
       "eqliscsiSnapshotTargetLocalMemberId": eqliscsiSnapshotTargetLocalMemberId,
       "eqliscsiSnapshotTargetIndex": eqliscsiSnapshotTargetIndex,
       "eqliscsiSnapshotMultInitiator": eqliscsiSnapshotMultInitiator,
       "eqliscsiSnapshotFlags": eqliscsiSnapshotFlags,
       "eqliscsiSnapshotCompressionDelay": eqliscsiSnapshotCompressionDelay,
       "eqliscsiSnapshotLifeExpectancy": eqliscsiSnapshotLifeExpectancy,
       "eqliscsiVolumeMemberTable": eqliscsiVolumeMemberTable,
       "eqliscsiVolumeMemberEntry": eqliscsiVolumeMemberEntry,
       "eqliscsiVolumeMemberIndex": eqliscsiVolumeMemberIndex,
       "eqliscsiVolumeMemberPssId": eqliscsiVolumeMemberPssId,
       "eqliscsiVolumeMemberShareOfVolume": eqliscsiVolumeMemberShareOfVolume,
       "eqliscsiVolumeInitiatorsTable": eqliscsiVolumeInitiatorsTable,
       "eqliscsiVolumeInitiatorsEntry": eqliscsiVolumeInitiatorsEntry,
       "eqliscsiVolumeInitiatorsIndex": eqliscsiVolumeInitiatorsIndex,
       "eqliscsiVolumeInitiatorsName": eqliscsiVolumeInitiatorsName,
       "eqliscsiVolumeSnapshotPolicyTable": eqliscsiVolumeSnapshotPolicyTable,
       "eqliscsiVolumeSnapshotPolicyEntry": eqliscsiVolumeSnapshotPolicyEntry,
       "eqliscsiVolumeSnapshotPolicyIndex": eqliscsiVolumeSnapshotPolicyIndex,
       "eqliscsiVolumeSnapshotPolicyRowStatus": eqliscsiVolumeSnapshotPolicyRowStatus,
       "eqliscsiVolumeSnapshotPolicyName": eqliscsiVolumeSnapshotPolicyName,
       "eqliscsiVolumeSnapshotPolicyAccessType": eqliscsiVolumeSnapshotPolicyAccessType,
       "eqliscsiVolumeSnapshotPolicyStatus": eqliscsiVolumeSnapshotPolicyStatus,
       "eqliscsiVolumeSnapshotPolicyMaxKeep": eqliscsiVolumeSnapshotPolicyMaxKeep,
       "eqliscsiVolumeSnapshotPolicyType": eqliscsiVolumeSnapshotPolicyType,
       "eqliscsiVolumeSnapshotPolicyRepeatFactor": eqliscsiVolumeSnapshotPolicyRepeatFactor,
       "eqliscsiVolumeSnapshotPolicyStartTime": eqliscsiVolumeSnapshotPolicyStartTime,
       "eqliscsiVolumeSnapshotPolicyEndTime": eqliscsiVolumeSnapshotPolicyEndTime,
       "eqliscsiVolumeSnapshotPolicyTimeFrequency": eqliscsiVolumeSnapshotPolicyTimeFrequency,
       "eqliscsiVolumeSnapshotPolicyStartDate": eqliscsiVolumeSnapshotPolicyStartDate,
       "eqliscsiVolumeSnapshotPolicyEndDate": eqliscsiVolumeSnapshotPolicyEndDate,
       "eqliscsiVolumeSnapshotPolicyWeekMask": eqliscsiVolumeSnapshotPolicyWeekMask,
       "eqliscsiVolumeSnapshotPolicyMonthMask": eqliscsiVolumeSnapshotPolicyMonthMask,
       "eqliscsiVolumeSnapshotPolicyNextCreate": eqliscsiVolumeSnapshotPolicyNextCreate,
       "eqliscsiVolumeSnapshotPolicyOccurence": eqliscsiVolumeSnapshotPolicyOccurence,
       "eqliscsiVolumeSnapshotPolicyReplication": eqliscsiVolumeSnapshotPolicyReplication,
       "eqliscsiVolumeSnapshotPolicyAdminStatus": eqliscsiVolumeSnapshotPolicyAdminStatus,
       "eqliscsiVolumeACLTable": eqliscsiVolumeACLTable,
       "eqliscsiVolumeACLEntry": eqliscsiVolumeACLEntry,
       "eqliscsiVolumeACLIndex": eqliscsiVolumeACLIndex,
       "eqliscsiVolumeACLInitiatorName": eqliscsiVolumeACLInitiatorName,
       "eqliscsiVolumeACLInitiatorIpAddress": eqliscsiVolumeACLInitiatorIpAddress,
       "eqliscsiVolumeACLInitiatorAuthenticationMethod": eqliscsiVolumeACLInitiatorAuthenticationMethod,
       "eqliscsiVolumeACLInitiatorUserName": eqliscsiVolumeACLInitiatorUserName,
       "eqliscsiVolumeACLInitiatorUserPassword": eqliscsiVolumeACLInitiatorUserPassword,
       "eqliscsiVolumeACLTargetType": eqliscsiVolumeACLTargetType,
       "eqliscsiVolumeACLRowStatus": eqliscsiVolumeACLRowStatus,
       "eqliscsiVolumeACLInitiatorUserName2": eqliscsiVolumeACLInitiatorUserName2,
       "eqliscsiVolumeACLAuthType": eqliscsiVolumeACLAuthType,
       "eqliscsiVolumeACLInitiatorIpWildcard": eqliscsiVolumeACLInitiatorIpWildcard,
       "eqliscsiVolumeACLInitiatorInetAddressType": eqliscsiVolumeACLInitiatorInetAddressType,
       "eqliscsiVolumeACLInitiatorInetAddress": eqliscsiVolumeACLInitiatorInetAddress,
       "eqliscsiVolumeACLInitiatorInetWildcardType": eqliscsiVolumeACLInitiatorInetWildcardType,
       "eqliscsiVolumeACLInitiatorInetWildcard": eqliscsiVolumeACLInitiatorInetWildcard,
       "eqliscsiVolumeStatusTable": eqliscsiVolumeStatusTable,
       "eqliscsiVolumeStatusEntry": eqliscsiVolumeStatusEntry,
       "eqliscsiVolumeStatusPsvId": eqliscsiVolumeStatusPsvId,
       "eqliscsiVolumeStatusReservedSpace": eqliscsiVolumeStatusReservedSpace,
       "eqliscsiVolumeStatusReservedSpaceAvail": eqliscsiVolumeStatusReservedSpaceAvail,
       "eqliscsiVolumeStatusActualMemberCount": eqliscsiVolumeStatusActualMemberCount,
       "eqliscsiVolumeStatusNumSnapshots": eqliscsiVolumeStatusNumSnapshots,
       "eqliscsiVolumeStatusCreationTime": eqliscsiVolumeStatusCreationTime,
       "eqliscsiVolumeStatusAvailable": eqliscsiVolumeStatusAvailable,
       "eqliscsiVolumeStatusOperStatus": eqliscsiVolumeStatusOperStatus,
       "eqliscsiVolumeStatusConnections": eqliscsiVolumeStatusConnections,
       "eqliscsiVolumeStatusLostRaidBlocksAction": eqliscsiVolumeStatusLostRaidBlocksAction,
       "eqliscsiVolumeStatusNumReplicas": eqliscsiVolumeStatusNumReplicas,
       "eqliscsiVolumeStatusReplReserveSpace": eqliscsiVolumeStatusReplReserveSpace,
       "eqliscsiVolumeStatusAllocatedSpace": eqliscsiVolumeStatusAllocatedSpace,
       "eqliscsiVolumeStatusReplResvInUse": eqliscsiVolumeStatusReplResvInUse,
       "eqliscsiVolumeStatusReplTxData": eqliscsiVolumeStatusReplTxData,
       "eqliscsiVolumeStatusNumOnlineSnaps": eqliscsiVolumeStatusNumOnlineSnaps,
       "eqliscsiVolumeStatusPagesSharedWithParent": eqliscsiVolumeStatusPagesSharedWithParent,
       "eqliscsiVolumeStatusExternalConnections": eqliscsiVolumeStatusExternalConnections,
       "eqliscsiVolumeStatusSpaceBorrowing": eqliscsiVolumeStatusSpaceBorrowing,
       "eqliscsiVolumeStatusBorrow": eqliscsiVolumeStatusBorrow,
       "eqliscsiSnapshotStatusTable": eqliscsiSnapshotStatusTable,
       "eqliscsiSnapshotStatusEntry": eqliscsiSnapshotStatusEntry,
       "eqliscsiSnapshotStatusOperStatus": eqliscsiSnapshotStatusOperStatus,
       "eqliscsiSnapshotStatusConnections": eqliscsiSnapshotStatusConnections,
       "eqliscsiSnapshotStatusLostRaidBlocksAction": eqliscsiSnapshotStatusLostRaidBlocksAction,
       "eqliscsiAdminGroup": eqliscsiAdminGroup,
       "eqliscsiLocalMemberId": eqliscsiLocalMemberId,
       "eqliscsiLocalMemberIdLow": eqliscsiLocalMemberIdLow,
       "eqliscsiLocalMemberIdHigh": eqliscsiLocalMemberIdHigh,
       "eqliscsiVolumeAdminGroup": eqliscsiVolumeAdminGroup,
       "eqliscsiLastVolumeIndex": eqliscsiLastVolumeIndex,
       "eqliscsiVolumeIndexLow": eqliscsiVolumeIndexLow,
       "eqliscsiVolumeIndexHigh": eqliscsiVolumeIndexHigh,
       "eqliscsiVolumeLowPsvId0": eqliscsiVolumeLowPsvId0,
       "eqliscsiVolumeLowPsvId1": eqliscsiVolumeLowPsvId1,
       "eqliscsiVolumeLowPsvId2": eqliscsiVolumeLowPsvId2,
       "eqliscsiVolumeLowPsvId3": eqliscsiVolumeLowPsvId3,
       "eqliscsiVolumeHighPsvId0": eqliscsiVolumeHighPsvId0,
       "eqliscsiVolumeHighPsvId1": eqliscsiVolumeHighPsvId1,
       "eqliscsiVolumeHighPsvId2": eqliscsiVolumeHighPsvId2,
       "eqliscsiVolumeHighPsvId3": eqliscsiVolumeHighPsvId3,
       "eqliscsiSnapshotAdminGroup": eqliscsiSnapshotAdminGroup,
       "eqliscsiLastSnapshotIndex": eqliscsiLastSnapshotIndex,
       "eqliscsiVolumeAuthAttributesTable": eqliscsiVolumeAuthAttributesTable,
       "eqliscsiVolumeAuthAttributesEntry": eqliscsiVolumeAuthAttributesEntry,
       "eqliscsiVolumeAuthRowStatus": eqliscsiVolumeAuthRowStatus,
       "eqliscsiVolumeAuthIdentity": eqliscsiVolumeAuthIdentity,
       "eqliscsiVolumeBindingTable": eqliscsiVolumeBindingTable,
       "eqliscsiVolumeBindingEntry": eqliscsiVolumeBindingEntry,
       "eqliscsiVolumeBindingRowStatus": eqliscsiVolumeBindingRowStatus,
       "eqliscsiVolumeReplSiteTable": eqliscsiVolumeReplSiteTable,
       "eqliscsiVolumeReplSiteEntry": eqliscsiVolumeReplSiteEntry,
       "eqliscsiVolumeReplSiteIndex": eqliscsiVolumeReplSiteIndex,
       "eqliscsiVolumeReplSiteRowStatus": eqliscsiVolumeReplSiteRowStatus,
       "eqliscsiVolumeReplSiteName": eqliscsiVolumeReplSiteName,
       "eqliscsiVolumeReplSiteIpAddr": eqliscsiVolumeReplSiteIpAddr,
       "eqliscsiVolumeReplSiteControlCredentials": eqliscsiVolumeReplSiteControlCredentials,
       "eqliscsiVolumeReplControlTargetIscsiName": eqliscsiVolumeReplControlTargetIscsiName,
       "eqliscsiVolumeReplSiteSNMPContext": eqliscsiVolumeReplSiteSNMPContext,
       "eqliscsiVolumeReplSiteContact": eqliscsiVolumeReplSiteContact,
       "eqliscsiVolumeReplSiteEmail": eqliscsiVolumeReplSiteEmail,
       "eqliscsiVolumeReplSitePhone": eqliscsiVolumeReplSitePhone,
       "eqliscsiVolumeReplSiteMobile": eqliscsiVolumeReplSiteMobile,
       "eqliscsiVolumeReplSiteDescription": eqliscsiVolumeReplSiteDescription,
       "eqliscsiVolumeReplSiteSpaceAllocated": eqliscsiVolumeReplSiteSpaceAllocated,
       "eqliscsiVolumeReplSiteSpaceUsed": eqliscsiVolumeReplSiteSpaceUsed,
       "eqliscsiVolumeReplControlChannelStatus": eqliscsiVolumeReplControlChannelStatus,
       "eqliscsiVolumeReplSiteAdminStatus": eqliscsiVolumeReplSiteAdminStatus,
       "eqliscsiVolumeReplSiteTotalNumSnapshots": eqliscsiVolumeReplSiteTotalNumSnapshots,
       "eqliscsiVolumeReplSiteSpaceSubscribed": eqliscsiVolumeReplSiteSpaceSubscribed,
       "eqliscsiVolumeReplSiteInetAddrType": eqliscsiVolumeReplSiteInetAddrType,
       "eqliscsiVolumeReplSiteInetAddr": eqliscsiVolumeReplSiteInetAddr,
       "eqliscsiVolumeReplSiteNASPartnershipId": eqliscsiVolumeReplSiteNASPartnershipId,
       "eqliscsiVolumeReplSiteBlockState": eqliscsiVolumeReplSiteBlockState,
       "eqliscsiVolumeReplSiteNASState": eqliscsiVolumeReplSiteNASState,
       "eqliscsiVolumeReplSiteType": eqliscsiVolumeReplSiteType,
       "eqliscsiVolumeReplicationTable": eqliscsiVolumeReplicationTable,
       "eqliscsiVolumeReplicationEntry": eqliscsiVolumeReplicationEntry,
       "eqliscsiVolumeReplRowStatus": eqliscsiVolumeReplRowStatus,
       "eqliscsiVolumeReplAdminStatus": eqliscsiVolumeReplAdminStatus,
       "eqliscsiVolumeReplRemoteIscsiName": eqliscsiVolumeReplRemoteIscsiName,
       "eqliscsiVolumeReplRemoteIscsiPort": eqliscsiVolumeReplRemoteIscsiPort,
       "eqliscsiVolumeReplRemotePsvId": eqliscsiVolumeReplRemotePsvId,
       "eqliscsiVolumeReplDiscardPolicy": eqliscsiVolumeReplDiscardPolicy,
       "eqliscsiVolumeReplReserve": eqliscsiVolumeReplReserve,
       "eqliscsiVolumeReplDeletionPolicy": eqliscsiVolumeReplDeletionPolicy,
       "eqliscsiVolumeReplNumReplicas": eqliscsiVolumeReplNumReplicas,
       "eqliscsiVolumeReplPrimaryReserve": eqliscsiVolumeReplPrimaryReserve,
       "eqliscsiVolumeReplPrimaryBorrow": eqliscsiVolumeReplPrimaryBorrow,
       "eqliscsiVolumeReplManualReplStatus": eqliscsiVolumeReplManualReplStatus,
       "eqliscsiVolumeReplCurLwMark": eqliscsiVolumeReplCurLwMark,
       "eqliscsiVolumeReplLwMark": eqliscsiVolumeReplLwMark,
       "eqliscsiVolumeReplSize": eqliscsiVolumeReplSize,
       "eqliscsiVolumeReplThinProvision": eqliscsiVolumeReplThinProvision,
       "eqliscsiVolumeReplMinThinReserve": eqliscsiVolumeReplMinThinReserve,
       "eqliscsiVolumeReplThinWarnPercentage": eqliscsiVolumeReplThinWarnPercentage,
       "eqliscsiVolumeReplThinMaxGrowPercentage": eqliscsiVolumeReplThinMaxGrowPercentage,
       "eqliscsiVolumeReplDynamicThinReserve": eqliscsiVolumeReplDynamicThinReserve,
       "eqliscsiVolumeReplFailBackMode": eqliscsiVolumeReplFailBackMode,
       "eqliscsiVolumeReplPromoteSeqNum": eqliscsiVolumeReplPromoteSeqNum,
       "eqliscsiVolumeReplTemplateReplicated": eqliscsiVolumeReplTemplateReplicated,
       "eqliscsiVolumeReplSyncAdminStatus": eqliscsiVolumeReplSyncAdminStatus,
       "eqliscsiVolumeReplSyncOperStatus": eqliscsiVolumeReplSyncOperStatus,
       "eqliscsiVolumeReplThinClone": eqliscsiVolumeReplThinClone,
       "eqliscsiVolumeReplicationStatusTable": eqliscsiVolumeReplicationStatusTable,
       "eqliscsiVolumeReplicationStatusEntry": eqliscsiVolumeReplicationStatusEntry,
       "eqliscsiVolumeReplOperStatus": eqliscsiVolumeReplOperStatus,
       "eqliscsiVolumeReplMBRemaining": eqliscsiVolumeReplMBRemaining,
       "eqliscsiVolumeReplMBCompleted": eqliscsiVolumeReplMBCompleted,
       "eqliscsiVolumeReplCurrentSnapshot": eqliscsiVolumeReplCurrentSnapshot,
       "eqliscsiVolumeReplCancel": eqliscsiVolumeReplCancel,
       "eqliscsiVolumeRemoteReplReserveIncrNeeded": eqliscsiVolumeRemoteReplReserveIncrNeeded,
       "eqliscsiVolumeReplFailbackSnap": eqliscsiVolumeReplFailbackSnap,
       "eqliscsiRemoteReplicaTable": eqliscsiRemoteReplicaTable,
       "eqliscsiRemoteReplicaEntry": eqliscsiRemoteReplicaEntry,
       "eqliscsiRemoteVolumeIndex": eqliscsiRemoteVolumeIndex,
       "eqliscsiRemoteSnapIndex": eqliscsiRemoteSnapIndex,
       "eqliscsiRemoteReplName": eqliscsiRemoteReplName,
       "eqliscsiRemoteReplISCSIName": eqliscsiRemoteReplISCSIName,
       "eqliscsiRemoteReplPsvId": eqliscsiRemoteReplPsvId,
       "eqliscsiRemoteReplAdminStatus": eqliscsiRemoteReplAdminStatus,
       "eqliscsiRemoteReplTimeStamp": eqliscsiRemoteReplTimeStamp,
       "eqliscsiRemoteReplSnapColIndex": eqliscsiRemoteReplSnapColIndex,
       "eqliscsiRemoteReplScheduleIndex": eqliscsiRemoteReplScheduleIndex,
       "eqliscsiRemoteReplLocalMemberId": eqliscsiRemoteReplLocalMemberId,
       "eqliscsiReplicaSetTable": eqliscsiReplicaSetTable,
       "eqliscsiReplicaSetEntry": eqliscsiReplicaSetEntry,
       "eqliscsiReplicaSetPrimaryIscsiName": eqliscsiReplicaSetPrimaryIscsiName,
       "eqliscsiReplicaSetReserve": eqliscsiReplicaSetReserve,
       "eqliscsiReplicaSetSite": eqliscsiReplicaSetSite,
       "eqliscsiReplicaSetAdminStatus": eqliscsiReplicaSetAdminStatus,
       "eqliscsiReplicaSetPromotePolicy": eqliscsiReplicaSetPromotePolicy,
       "eqliscsiReplicaSetManualReplStatus": eqliscsiReplicaSetManualReplStatus,
       "eqliscsiReplicaSetFailBackMode": eqliscsiReplicaSetFailBackMode,
       "eqliscsiReplicaSetType": eqliscsiReplicaSetType,
       "eqliscsiReplicaSetAccess": eqliscsiReplicaSetAccess,
       "eqliscsiReplicaSetFailbackReserve": eqliscsiReplicaSetFailbackReserve,
       "eqliscsiReplicaSetLSRPsvId": eqliscsiReplicaSetLSRPsvId,
       "eqliscsiReplicaSetOrigSize": eqliscsiReplicaSetOrigSize,
       "eqliscsiReplicaSetPrimaryMemberId": eqliscsiReplicaSetPrimaryMemberId,
       "eqliscsiReplicaSetPrimaryVolumeIndex": eqliscsiReplicaSetPrimaryVolumeIndex,
       "eqliscsiReplicaSetPrimarySite": eqliscsiReplicaSetPrimarySite,
       "eqliscsiReplicaSetTemplateReplicated": eqliscsiReplicaSetTemplateReplicated,
       "eqliscsiReplicaSetSyncAdminStatus": eqliscsiReplicaSetSyncAdminStatus,
       "eqliscsiReplicaSetThinClone": eqliscsiReplicaSetThinClone,
       "eqliscsiReplicaSetRemotePsvId": eqliscsiReplicaSetRemotePsvId,
       "eqliscsiReplicaSetStatusTable": eqliscsiReplicaSetStatusTable,
       "eqliscsiReplicaSetStatusEntry": eqliscsiReplicaSetStatusEntry,
       "eqliscsiReplicaSetOperStatus": eqliscsiReplicaSetOperStatus,
       "eqliscsiReplicaSetSize": eqliscsiReplicaSetSize,
       "eqliscsiReplicantSiteTable": eqliscsiReplicantSiteTable,
       "eqliscsiReplicantSiteEntry": eqliscsiReplicantSiteEntry,
       "eqliscsiReplicantSiteIndex": eqliscsiReplicantSiteIndex,
       "eqliscsiReplicantSiteRowStatus": eqliscsiReplicantSiteRowStatus,
       "eqliscsiReplicantSiteName": eqliscsiReplicantSiteName,
       "eqliscsiReplicantSiteIpAddr": eqliscsiReplicantSiteIpAddr,
       "eqliscsiReplicantSiteControlCredentials": eqliscsiReplicantSiteControlCredentials,
       "eqliscsiReplicantControlTargetIscsiName": eqliscsiReplicantControlTargetIscsiName,
       "eqliscsiReplicantSiteSNMPContext": eqliscsiReplicantSiteSNMPContext,
       "eqliscsiReplicantSiteContact": eqliscsiReplicantSiteContact,
       "eqliscsiReplicantSiteEmail": eqliscsiReplicantSiteEmail,
       "eqliscsiReplicantSitePhone": eqliscsiReplicantSitePhone,
       "eqliscsiReplicantSiteMobile": eqliscsiReplicantSiteMobile,
       "eqliscsiReplicantSiteDescription": eqliscsiReplicantSiteDescription,
       "eqliscsiReplicantSiteSpaceAllocated": eqliscsiReplicantSiteSpaceAllocated,
       "eqliscsiReplicantSiteSpaceUsed": eqliscsiReplicantSiteSpaceUsed,
       "eqliscsiReplicantSiteControlChannelStatus": eqliscsiReplicantSiteControlChannelStatus,
       "eqliscsiReplicantSiteAdminStatus": eqliscsiReplicantSiteAdminStatus,
       "eqliscsiReplicantSiteTotalNumSnapshots": eqliscsiReplicantSiteTotalNumSnapshots,
       "eqliscsiReplicantSiteStoragePoolIndex": eqliscsiReplicantSiteStoragePoolIndex,
       "eqliscsiReplicantSiteSpaceSubscribed": eqliscsiReplicantSiteSpaceSubscribed,
       "eqliscsiReplicantSiteInetAddrType": eqliscsiReplicantSiteInetAddrType,
       "eqliscsiReplicantSiteInetAddr": eqliscsiReplicantSiteInetAddr,
       "eqliscsiReplicantSiteUnmanagedSpace": eqliscsiReplicantSiteUnmanagedSpace,
       "eqliscsiReplicantSiteReplType": eqliscsiReplicantSiteReplType,
       "eqliscsiVolCollectionObjectsTable": eqliscsiVolCollectionObjectsTable,
       "eqliscsiVolCollectionObjectsEntry": eqliscsiVolCollectionObjectsEntry,
       "eqliscsiVolCollectionIndex": eqliscsiVolCollectionIndex,
       "eqliscsiVolCollectionObjectRowStatus": eqliscsiVolCollectionObjectRowStatus,
       "eqliscsiVolCollectionTable": eqliscsiVolCollectionTable,
       "eqliscsiVolCollectionEntry": eqliscsiVolCollectionEntry,
       "eqliscsiVolCollectionRowStatus": eqliscsiVolCollectionRowStatus,
       "eqliscsiVolCollectionName": eqliscsiVolCollectionName,
       "eqliscsiVolCollectionDescription": eqliscsiVolCollectionDescription,
       "eqliscsiVolCollectionReplService": eqliscsiVolCollectionReplService,
       "eqliscsiVolCollectionSite": eqliscsiVolCollectionSite,
       "eqliscsiVolCollectionFlags": eqliscsiVolCollectionFlags,
       "eqliscsiSnapCollectionObjectsTable": eqliscsiSnapCollectionObjectsTable,
       "eqliscsiSnapCollectionObjectsEntry": eqliscsiSnapCollectionObjectsEntry,
       "eqliscsiSnapCollectionIndex": eqliscsiSnapCollectionIndex,
       "eqliscsiSnapCollectionObjectRowStatus": eqliscsiSnapCollectionObjectRowStatus,
       "eqliscsiSnapCollectionTable": eqliscsiSnapCollectionTable,
       "eqliscsiSnapCollectionEntry": eqliscsiSnapCollectionEntry,
       "eqliscsiSnapCollectionRowStatus": eqliscsiSnapCollectionRowStatus,
       "eqliscsiSnapCollectionName": eqliscsiSnapCollectionName,
       "eqliscsiSnapCollectionDescription": eqliscsiSnapCollectionDescription,
       "eqliscsiSnapCollectionTimestamp": eqliscsiSnapCollectionTimestamp,
       "eqliscsiSnapCollectionNoofSnaps": eqliscsiSnapCollectionNoofSnaps,
       "eqliscsiSnapCollectionVolIndex": eqliscsiSnapCollectionVolIndex,
       "eqliscsiSnapCollectionVSS": eqliscsiSnapCollectionVSS,
       "eqliscsiSnapCollectionScheduleIndex": eqliscsiSnapCollectionScheduleIndex,
       "eqliscsiSnapCollectionReplicated": eqliscsiSnapCollectionReplicated,
       "eqliscsiSnapCollectionType": eqliscsiSnapCollectionType,
       "eqliscsiSnapCollectionSite": eqliscsiSnapCollectionSite,
       "eqliscsiSnapCollectionPolicyTable": eqliscsiSnapCollectionPolicyTable,
       "eqliscsiSnapCollectionPolicyEntry": eqliscsiSnapCollectionPolicyEntry,
       "eqliscsiSnapCollectionPolicyIndex": eqliscsiSnapCollectionPolicyIndex,
       "eqliscsiSnapCollectionPolicyRowStatus": eqliscsiSnapCollectionPolicyRowStatus,
       "eqliscsiSnapCollectionPolicyName": eqliscsiSnapCollectionPolicyName,
       "eqliscsiSnapCollectionPolicyAccessType": eqliscsiSnapCollectionPolicyAccessType,
       "eqliscsiSnapCollectionPolicyStatus": eqliscsiSnapCollectionPolicyStatus,
       "eqliscsiSnapCollectionPolicyMaxKeep": eqliscsiSnapCollectionPolicyMaxKeep,
       "eqliscsiSnapCollectionPolicyType": eqliscsiSnapCollectionPolicyType,
       "eqliscsiSnapCollectionPolicyRepeatFactor": eqliscsiSnapCollectionPolicyRepeatFactor,
       "eqliscsiSnapCollectionPolicyStartTime": eqliscsiSnapCollectionPolicyStartTime,
       "eqliscsiSnapCollectionPolicyEndTime": eqliscsiSnapCollectionPolicyEndTime,
       "eqliscsiSnapCollectionPolicyTimeFrequency": eqliscsiSnapCollectionPolicyTimeFrequency,
       "eqliscsiSnapCollectionPolicyStartDate": eqliscsiSnapCollectionPolicyStartDate,
       "eqliscsiSnapCollectionPolicyEndDate": eqliscsiSnapCollectionPolicyEndDate,
       "eqliscsiSnapCollectionPolicyWeekMask": eqliscsiSnapCollectionPolicyWeekMask,
       "eqliscsiSnapCollectionPolicyMonthMask": eqliscsiSnapCollectionPolicyMonthMask,
       "eqliscsiSnapCollectionPolicyNextCreate": eqliscsiSnapCollectionPolicyNextCreate,
       "eqliscsiSnapCollectionPolicyOccurence": eqliscsiSnapCollectionPolicyOccurence,
       "eqliscsiSnapCollectionPolicyReplication": eqliscsiSnapCollectionPolicyReplication,
       "eqliscsiSnapCollectionPolicyAdminStatus": eqliscsiSnapCollectionPolicyAdminStatus,
       "eqliscsiVolCollectionStatusTable": eqliscsiVolCollectionStatusTable,
       "eqliscsiVolCollectionStatusEntry": eqliscsiVolCollectionStatusEntry,
       "eqliscsiNoOfSnapCollections": eqliscsiNoOfSnapCollections,
       "eqliscsiSnapCollectionAdminGroup": eqliscsiSnapCollectionAdminGroup,
       "eqliscsiLastSnapCollectionIndex": eqliscsiLastSnapCollectionIndex,
       "eqliscsiRemoteReplicaCollectionObjectsTable": eqliscsiRemoteReplicaCollectionObjectsTable,
       "eqliscsiRemoteReplicaCollectionObjectsEntry": eqliscsiRemoteReplicaCollectionObjectsEntry,
       "eqliscsiRemoteSnapCollectionIndex": eqliscsiRemoteSnapCollectionIndex,
       "eqliscsiRemoteReplCollectionObjRowStatus": eqliscsiRemoteReplCollectionObjRowStatus,
       "eqliscsiRemoteReplicaCollectionTable": eqliscsiRemoteReplicaCollectionTable,
       "eqliscsiRemoteReplicaCollectionEntry": eqliscsiRemoteReplicaCollectionEntry,
       "eqliscsiRemoteReplCollectionName": eqliscsiRemoteReplCollectionName,
       "eqliscsiRemoteReplCollectionAdminStatus": eqliscsiRemoteReplCollectionAdminStatus,
       "eqliscsiRemoteReplCollectionTimeStamp": eqliscsiRemoteReplCollectionTimeStamp,
       "eqliscsiRemoteReplCollectionVolIndex": eqliscsiRemoteReplCollectionVolIndex,
       "eqliscsiRemoteReplCollectionSchedIndex": eqliscsiRemoteReplCollectionSchedIndex,
       "eqliscsiVolColReplicationTable": eqliscsiVolColReplicationTable,
       "eqliscsiVolColReplicationEntry": eqliscsiVolColReplicationEntry,
       "eqliscsiVolColReplRowStatus": eqliscsiVolColReplRowStatus,
       "eqliscsiVolColReplAdminStatus": eqliscsiVolColReplAdminStatus,
       "eqliscsiVolColReplDeletionPolicy": eqliscsiVolColReplDeletionPolicy,
       "eqliscsiVolColReplRemoteCollectionId": eqliscsiVolColReplRemoteCollectionId,
       "eqliscsiVolColReplStatusTable": eqliscsiVolColReplStatusTable,
       "eqliscsiVolColReplStatusEntry": eqliscsiVolColReplStatusEntry,
       "eqliscsiVolColReplStatusNumReplicas": eqliscsiVolColReplStatusNumReplicas,
       "eqlVolumePoolPlacementTable": eqlVolumePoolPlacementTable,
       "eqlVolumePoolPlacementEntry": eqlVolumePoolPlacementEntry,
       "eqlVolumePoolPlacementiscsiVolumePsvId": eqlVolumePoolPlacementiscsiVolumePsvId,
       "eqliscsiVolReplStatisticsTable": eqliscsiVolReplStatisticsTable,
       "eqliscsiVolReplStatisticsEntry": eqliscsiVolReplStatisticsEntry,
       "eqliscsiReplSampleIndex": eqliscsiReplSampleIndex,
       "eqliscsiReplStartTime": eqliscsiReplStartTime,
       "eqliscsiReplEndTime": eqliscsiReplEndTime,
       "eqliscsiReplTxData": eqliscsiReplTxData,
       "eqliscsiReplTxStatus": eqliscsiReplTxStatus,
       "eqliscsiVolumeStatisticsTable": eqliscsiVolumeStatisticsTable,
       "eqliscsiVolumeStatisticsEntry": eqliscsiVolumeStatisticsEntry,
       "eqliscsiVolumeStatsCmdPdus": eqliscsiVolumeStatsCmdPdus,
       "eqliscsiVolumeStatsRspPdus": eqliscsiVolumeStatsRspPdus,
       "eqliscsiVolumeStatsTxData": eqliscsiVolumeStatsTxData,
       "eqliscsiVolumeStatsRxData": eqliscsiVolumeStatsRxData,
       "eqliscsiVolumeStatsNoOfSessions": eqliscsiVolumeStatsNoOfSessions,
       "eqliscsiVolumeStatsReadLatency": eqliscsiVolumeStatsReadLatency,
       "eqliscsiVolumeStatsWriteLatency": eqliscsiVolumeStatsWriteLatency,
       "eqliscsiVolumeStatsReadOpCount": eqliscsiVolumeStatsReadOpCount,
       "eqliscsiVolumeStatsWriteOpCount": eqliscsiVolumeStatsWriteOpCount,
       "eqliscsiVolumeStatsReadAvgLatency": eqliscsiVolumeStatsReadAvgLatency,
       "eqliscsiVolumeStatsWriteAvgLatency": eqliscsiVolumeStatsWriteAvgLatency,
       "eqliscsiVolumeStatsIscsiReadWriteCmdsReceived": eqliscsiVolumeStatsIscsiReadWriteCmdsReceived,
       "eqliscsiVolumeStatsIscsiReadWriteCmdsCompleted": eqliscsiVolumeStatsIscsiReadWriteCmdsCompleted,
       "eqliscsiVolumeStatsHCIscsiReadWriteCmdsReceived": eqliscsiVolumeStatsHCIscsiReadWriteCmdsReceived,
       "eqliscsiVolumeStatsHCIscsiTotalQD": eqliscsiVolumeStatsHCIscsiTotalQD,
       "eqliscsiVolumeStatsMisAlignedIO": eqliscsiVolumeStatsMisAlignedIO,
       "eqliscsiTargetAdminGroup": eqliscsiTargetAdminGroup,
       "eqliscsiLastTargetIndex": eqliscsiLastTargetIndex,
       "eqliscsiTargetTable": eqliscsiTargetTable,
       "eqliscsiTargetEntry": eqliscsiTargetEntry,
       "eqliscsiTargetIndex": eqliscsiTargetIndex,
       "eqliscsiTargetRowStatus": eqliscsiTargetRowStatus,
       "eqliscsiTargetUUID": eqliscsiTargetUUID,
       "eqliscsiTargetAlias": eqliscsiTargetAlias,
       "eqliscsiTargetIscsiName": eqliscsiTargetIscsiName,
       "eqliscsiTargetReserved1": eqliscsiTargetReserved1,
       "eqliscsiTargetReserved2": eqliscsiTargetReserved2,
       "eqliscsiTargetReserved3": eqliscsiTargetReserved3,
       "eqliscsiTargetChapSecretsTable": eqliscsiTargetChapSecretsTable,
       "eqliscsiTargetChapSecretsEntry": eqliscsiTargetChapSecretsEntry,
       "eqliscsiTargetChapSecretsUsage": eqliscsiTargetChapSecretsUsage,
       "eqliscsiTargetChapSecretsIndex": eqliscsiTargetChapSecretsIndex,
       "eqliscsiTargetChapSecretsRowStatus": eqliscsiTargetChapSecretsRowStatus,
       "eqliscsiTargetChapSecretsUserName": eqliscsiTargetChapSecretsUserName,
       "eqliscsiTargetChapSecretsPassword": eqliscsiTargetChapSecretsPassword,
       "eqliscsiVolumeSnapshotPolicyStatusTable": eqliscsiVolumeSnapshotPolicyStatusTable,
       "eqliscsiVolumeSnapshotPolicyStatusEntry": eqliscsiVolumeSnapshotPolicyStatusEntry,
       "eqliscsiVolumeSnapshotPolicyStatusNextCreate": eqliscsiVolumeSnapshotPolicyStatusNextCreate,
       "eqliscsiVolumeSnapshotPolicyStatusOperStatus": eqliscsiVolumeSnapshotPolicyStatusOperStatus,
       "eqliscsiVolumeSnapshotPolicyStatusNoOfSnaps": eqliscsiVolumeSnapshotPolicyStatusNoOfSnaps,
       "eqliscsiSnapCollectionPolicyStatusTable": eqliscsiSnapCollectionPolicyStatusTable,
       "eqliscsiSnapCollectionPolicyStatusEntry": eqliscsiSnapCollectionPolicyStatusEntry,
       "eqliscsiSnapCollectionPolicyStatusNextCreate": eqliscsiSnapCollectionPolicyStatusNextCreate,
       "eqliscsiSnapCollectionPolicyStatusOperStatus": eqliscsiSnapCollectionPolicyStatusOperStatus,
       "eqliscsiSnapCollectionPolicyStatusNoOfCollections": eqliscsiSnapCollectionPolicyStatusNoOfCollections,
       "eqliscsiVolumeOpsTable": eqliscsiVolumeOpsTable,
       "eqliscsiVolumeOpsEntry": eqliscsiVolumeOpsEntry,
       "eqliscsiVolumeOpsIndex": eqliscsiVolumeOpsIndex,
       "eqliscsiVolumeOpsRowStatus": eqliscsiVolumeOpsRowStatus,
       "eqliscsiVolumeOpsOperation": eqliscsiVolumeOpsOperation,
       "eqliscsiVolumeOpsExec": eqliscsiVolumeOpsExec,
       "eqliscsiVolumeOpsStartTime": eqliscsiVolumeOpsStartTime,
       "eqliscsiVolumeOpsStoragePoolSourceIndex": eqliscsiVolumeOpsStoragePoolSourceIndex,
       "eqliscsiVolumeOpsStoragePoolDestinationIndex": eqliscsiVolumeOpsStoragePoolDestinationIndex,
       "eqliscsiVolumeOpsVolBalCommandIndex": eqliscsiVolumeOpsVolBalCommandIndex,
       "eqliscsiVolumeOpsVolBalCommandiscsiLocalMemberId": eqliscsiVolumeOpsVolBalCommandiscsiLocalMemberId,
       "eqliscsiReplicaSetExtensionTable": eqliscsiReplicaSetExtensionTable,
       "eqliscsiReplicaSetExtensionEntry": eqliscsiReplicaSetExtensionEntry,
       "eqliscsiReplicaSetPrimaryPsvId": eqliscsiReplicaSetPrimaryPsvId,
       "eqliscsiVolumeStoragePreferenceTable": eqliscsiVolumeStoragePreferenceTable,
       "eqliscsiVolumeStoragePreferenceEntry": eqliscsiVolumeStoragePreferenceEntry,
       "eqliscsiVolumeStoragePreferenceRowStatus": eqliscsiVolumeStoragePreferenceRowStatus,
       "eqliscsiVolumeStoragePreferenceRAIDType": eqliscsiVolumeStoragePreferenceRAIDType,
       "eqliscsiVolumeStoragePreferenceDriveType": eqliscsiVolumeStoragePreferenceDriveType,
       "eqliscsiVolumeStoragePreferenceDiskSpeed": eqliscsiVolumeStoragePreferenceDiskSpeed,
       "eqliscsiVolumeStoragePreferenceRAIDTypeStatus": eqliscsiVolumeStoragePreferenceRAIDTypeStatus,
       "eqlAdminAccountVolumeTable": eqlAdminAccountVolumeTable,
       "eqlAdminAccountVolumeEntry": eqlAdminAccountVolumeEntry,
       "eqlAdminAccountVolumeAccess": eqlAdminAccountVolumeAccess,
       "eqlAdminAccountReplicantSiteTable": eqlAdminAccountReplicantSiteTable,
       "eqlAdminAccountReplicantSiteEntry": eqlAdminAccountReplicantSiteEntry,
       "eqlAdminAccountReplicantSiteAccess": eqlAdminAccountReplicantSiteAccess,
       "eqlAdminAccountVolCollectionTable": eqlAdminAccountVolCollectionTable,
       "eqlAdminAccountVolCollectionEntry": eqlAdminAccountVolCollectionEntry,
       "eqlAdminAccountVolCollectionAccess": eqlAdminAccountVolCollectionAccess,
       "eqliscsiVolumeOpsStatusTable": eqliscsiVolumeOpsStatusTable,
       "eqliscsiVolumeOpsStatusEntry": eqliscsiVolumeOpsStatusEntry,
       "eqliscsiVolumeOpsStatusCompletePct": eqliscsiVolumeOpsStatusCompletePct,
       "eqliscsiVolumeDynamicConfigTable": eqliscsiVolumeDynamicConfigTable,
       "eqliscsiVolumeDynamicConfigEntry": eqliscsiVolumeDynamicConfigEntry,
       "eqliscsiVolumeDynamicRowStatus": eqliscsiVolumeDynamicRowStatus,
       "eqliscsiVolumeDynamicThinReserve": eqliscsiVolumeDynamicThinReserve,
       "eqliscsiVolumeDynamicInUseHighWaterMark": eqliscsiVolumeDynamicInUseHighWaterMark,
       "eqliscsiVolumeDynamicInUseHighWaterMarkTimestamp": eqliscsiVolumeDynamicInUseHighWaterMarkTimestamp,
       "eqliscsiVolumeReplSiteStatusTable": eqliscsiVolumeReplSiteStatusTable,
       "eqliscsiVolumeReplSiteStatusEntry": eqliscsiVolumeReplSiteStatusEntry,
       "eqliscsiVolumeReplSiteFailbackSpace": eqliscsiVolumeReplSiteFailbackSpace,
       "eqliscsiVolumeChunkTable": eqliscsiVolumeChunkTable,
       "eqliscsiVolumeChunkEntry": eqliscsiVolumeChunkEntry,
       "eqliscsiVolumeChunkIndex": eqliscsiVolumeChunkIndex,
       "eqliscsiVolumeChunkVersion": eqliscsiVolumeChunkVersion,
       "eqliscsiVolumeChunkSegmentSize": eqliscsiVolumeChunkSegmentSize,
       "eqliscsiVolumeChunkSegments": eqliscsiVolumeChunkSegments,
       "eqliscsiVolumeChunkModified": eqliscsiVolumeChunkModified,
       "eqliscsiReplicantSiteOpsTable": eqliscsiReplicantSiteOpsTable,
       "eqliscsiReplicantSiteOpsEntry": eqliscsiReplicantSiteOpsEntry,
       "eqliscsiReplicantSiteOpsIndex": eqliscsiReplicantSiteOpsIndex,
       "eqliscsiReplicantSiteOpsRowStatus": eqliscsiReplicantSiteOpsRowStatus,
       "eqliscsiReplicantSiteOpsOperation": eqliscsiReplicantSiteOpsOperation,
       "eqliscsiReplicantSiteOpsExec": eqliscsiReplicantSiteOpsExec,
       "eqliscsiReplicantSiteOpsStartTime": eqliscsiReplicantSiteOpsStartTime,
       "eqliscsiReplicantSiteOpsStoragePoolSourceIndex": eqliscsiReplicantSiteOpsStoragePoolSourceIndex,
       "eqliscsiReplicantSiteOpsStoragePoolDestinationIndex": eqliscsiReplicantSiteOpsStoragePoolDestinationIndex,
       "eqliscsiReplicantSiteOpsVolBalCommandIndex": eqliscsiReplicantSiteOpsVolBalCommandIndex,
       "eqliscsiReplicantSiteOpsVolBalCommandiscsiLocalMemberId": eqliscsiReplicantSiteOpsVolBalCommandiscsiLocalMemberId,
       "eqliscsiReplicantSiteOpsStatusTable": eqliscsiReplicantSiteOpsStatusTable,
       "eqliscsiReplicantSiteOpsStatusEntry": eqliscsiReplicantSiteOpsStatusEntry,
       "eqliscsiReplicantSiteOpsStatusCompletePct": eqliscsiReplicantSiteOpsStatusCompletePct,
       "eqliscsiReplicantSiteStatusTable": eqliscsiReplicantSiteStatusTable,
       "eqliscsiReplicantSiteStatusEntry": eqliscsiReplicantSiteStatusEntry,
       "eqliscsiReplicantSiteStatusAvailable": eqliscsiReplicantSiteStatusAvailable,
       "eqliscsiReplicantSiteStatusMajorVersion": eqliscsiReplicantSiteStatusMajorVersion,
       "eqliscsiReplicantSiteStatusMinorVersion": eqliscsiReplicantSiteStatusMinorVersion,
       "eqliscsiReplicantSiteStatusMaintVersion": eqliscsiReplicantSiteStatusMaintVersion,
       "eqliscsiVolumeTaskStatusTable": eqliscsiVolumeTaskStatusTable,
       "eqliscsiVolumeTaskStatusEntry": eqliscsiVolumeTaskStatusEntry,
       "eqliscsiVolumeTaskStatusErrorCode": eqliscsiVolumeTaskStatusErrorCode,
       "eqliscsiVolumeTemplateThinClonesTable": eqliscsiVolumeTemplateThinClonesTable,
       "eqliscsiVolumeTemplateThinClonesEntry": eqliscsiVolumeTemplateThinClonesEntry,
       "eqliscsiThinCloneLocalMemberId": eqliscsiThinCloneLocalMemberId,
       "eqliscsiThinCloneVolumeIndex": eqliscsiThinCloneVolumeIndex,
       "eqliscsiVolumeTemplateThinClonesMember": eqliscsiVolumeTemplateThinClonesMember,
       "eqliscsiVolumeAdminAccountTable": eqliscsiVolumeAdminAccountTable,
       "eqliscsiVolumeAdminAccountEntry": eqliscsiVolumeAdminAccountEntry,
       "eqliscsiVolumeAdminAccountRowStatus": eqliscsiVolumeAdminAccountRowStatus,
       "eqliscsiTemplateVolumeStatusTable": eqliscsiTemplateVolumeStatusTable,
       "eqliscsiTemplateVolumeStatusEntry": eqliscsiTemplateVolumeStatusEntry,
       "eqliscsiTemplateVolumeStatusNumThinClones": eqliscsiTemplateVolumeStatusNumThinClones,
       "eqliscsiTemplateVolumeStatusNumThinCloneReplicators": eqliscsiTemplateVolumeStatusNumThinCloneReplicators,
       "eqliscsiTemplateVolumeStatusNumThinCloneReplicaSets": eqliscsiTemplateVolumeStatusNumThinCloneReplicaSets,
       "eqliscsiSnapAccumulatedStatisticsTable": eqliscsiSnapAccumulatedStatisticsTable,
       "eqliscsiSnapAccumulatedStatisticsEntry": eqliscsiSnapAccumulatedStatisticsEntry,
       "eqliscsiSnapAccumulatedStatsCmdPdus": eqliscsiSnapAccumulatedStatsCmdPdus,
       "eqliscsiSnapAccumulatedStatsRspPdus": eqliscsiSnapAccumulatedStatsRspPdus,
       "eqliscsiSnapAccumulatedStatsTxData": eqliscsiSnapAccumulatedStatsTxData,
       "eqliscsiSnapAccumulatedStatsRxData": eqliscsiSnapAccumulatedStatsRxData,
       "eqliscsiSnapAccumulatedStatsNoOfSessions": eqliscsiSnapAccumulatedStatsNoOfSessions,
       "eqliscsiSnapAccumulatedStatsReadLatency": eqliscsiSnapAccumulatedStatsReadLatency,
       "eqliscsiSnapAccumulatedStatsWriteLatency": eqliscsiSnapAccumulatedStatsWriteLatency,
       "eqliscsiSnapAccumulatedStatsReadOpCount": eqliscsiSnapAccumulatedStatsReadOpCount,
       "eqliscsiSnapAccumulatedStatsWriteOpCount": eqliscsiSnapAccumulatedStatsWriteOpCount,
       "eqliscsiSnapAccumulatedStatsReadAvgLatency": eqliscsiSnapAccumulatedStatsReadAvgLatency,
       "eqliscsiSnapAccumulatedStatsWriteAvgLatency": eqliscsiSnapAccumulatedStatsWriteAvgLatency,
       "eqliscsiSnapAccumulatedStatsIscsiReadWriteCmdsReceived": eqliscsiSnapAccumulatedStatsIscsiReadWriteCmdsReceived,
       "eqliscsiSnapAccumulatedStatsIscsiTotalQD": eqliscsiSnapAccumulatedStatsIscsiTotalQD,
       "eqliscsiVolumeReplSiteAdminAccountTable": eqliscsiVolumeReplSiteAdminAccountTable,
       "eqliscsiVolumeReplSiteAdminAccountEntry": eqliscsiVolumeReplSiteAdminAccountEntry,
       "eqliscsiVolumeReplSiteAdminAccountRowStatus": eqliscsiVolumeReplSiteAdminAccountRowStatus,
       "eqliscsiVolumeReplSiteAdminAccountQuotaType": eqliscsiVolumeReplSiteAdminAccountQuotaType,
       "eqliscsiVolumeReplSiteAdminAccountQuota": eqliscsiVolumeReplSiteAdminAccountQuota,
       "eqlLdapLoginAccessReplSiteTable": eqlLdapLoginAccessReplSiteTable,
       "eqlLdapLoginAccessReplSiteEntry": eqlLdapLoginAccessReplSiteEntry,
       "eqlLdapLoginAccessReplSiteQuotaType": eqlLdapLoginAccessReplSiteQuotaType,
       "eqlLdapLoginAccessReplSiteQuota": eqlLdapLoginAccessReplSiteQuota,
       "eqlLdapLoginAccessReplSiteRowStatus": eqlLdapLoginAccessReplSiteRowStatus,
       "eqliscsiVolumeSyncReplExtensionTable": eqliscsiVolumeSyncReplExtensionTable,
       "eqliscsiVolumeSyncReplExtensionEntry": eqliscsiVolumeSyncReplExtensionEntry,
       "eqliscsiVolumeSyncReplExtRowStatus": eqliscsiVolumeSyncReplExtRowStatus,
       "eqliscsiVolumeSyncReplExtSyncReplLocalMemberId": eqliscsiVolumeSyncReplExtSyncReplLocalMemberId,
       "eqliscsiVolumeSyncReplExtSyncReplIndex": eqliscsiVolumeSyncReplExtSyncReplIndex,
       "eqliscsiVolumeSyncReplExtIntTargetIscsiName": eqliscsiVolumeSyncReplExtIntTargetIscsiName,
       "eqliscsiVolumeSyncReplTable": eqliscsiVolumeSyncReplTable,
       "eqliscsiVolumeSyncReplEntry": eqliscsiVolumeSyncReplEntry,
       "eqliscsiVolumeSyncReplRowStatus": eqliscsiVolumeSyncReplRowStatus,
       "eqliscsiVolumeSyncReplLocalMemberId": eqliscsiVolumeSyncReplLocalMemberId,
       "eqliscsiVolumeSyncReplIndex": eqliscsiVolumeSyncReplIndex,
       "eqliscsiVolumeSyncReplPaused": eqliscsiVolumeSyncReplPaused,
       "eqliscsiVolumeSyncReplPeerTable": eqliscsiVolumeSyncReplPeerTable,
       "eqliscsiVolumeSyncReplPeerEntry": eqliscsiVolumeSyncReplPeerEntry,
       "eqliscsiVolumeSyncReplPeerLocalMemberId": eqliscsiVolumeSyncReplPeerLocalMemberId,
       "eqliscsiVolumeSyncReplPeerVolIndex": eqliscsiVolumeSyncReplPeerVolIndex,
       "eqliscsiVolumeSyncReplPeerPsvId": eqliscsiVolumeSyncReplPeerPsvId,
       "eqliscsiVolumeSyncReplStatusTable": eqliscsiVolumeSyncReplStatusTable,
       "eqliscsiVolumeSyncReplStatusEntry": eqliscsiVolumeSyncReplStatusEntry,
       "eqliscsiVolumeSyncReplStatusSyncStatus": eqliscsiVolumeSyncReplStatusSyncStatus,
       "eqliscsiVolumeSyncReplStatusUnreplicatedChanges": eqliscsiVolumeSyncReplStatusUnreplicatedChanges,
       "eqliscsiVolumeSyncReplStatusTotalTxDataMB": eqliscsiVolumeSyncReplStatusTotalTxDataMB,
       "eqliscsiVolumeSyncReplStatusRemainingTxDataMB": eqliscsiVolumeSyncReplStatusRemainingTxDataMB,
       "eqliscsiVolumeSyncReplVirtualTable": eqliscsiVolumeSyncReplVirtualTable,
       "eqliscsiVolumeSyncReplVirtualEntry": eqliscsiVolumeSyncReplVirtualEntry,
       "eqliscsiVolumeSyncReplVirtualAccessType": eqliscsiVolumeSyncReplVirtualAccessType,
       "eqliscsiVolumeSyncReplVirtualAdminStatus": eqliscsiVolumeSyncReplVirtualAdminStatus,
       "eqliscsiVolumeSyncReplVirtualMultInitiator": eqliscsiVolumeSyncReplVirtualMultInitiator,
       "eqliscsiVolumeSyncReplVirtualStatusTable": eqliscsiVolumeSyncReplVirtualStatusTable,
       "eqliscsiVolumeSyncReplVirtualStatusEntry": eqliscsiVolumeSyncReplVirtualStatusEntry,
       "eqliscsiVolumeSyncReplVirtualStatusReservedSpace": eqliscsiVolumeSyncReplVirtualStatusReservedSpace,
       "eqliscsiVolumeSyncReplVirtualStatusReservedSpaceAvail": eqliscsiVolumeSyncReplVirtualStatusReservedSpaceAvail,
       "eqliscsiVolumeSyncReplVirtualStatusNumSnapshots": eqliscsiVolumeSyncReplVirtualStatusNumSnapshots,
       "eqliscsiVolumeSyncReplVirtualStatusOperStatus": eqliscsiVolumeSyncReplVirtualStatusOperStatus,
       "eqliscsiVolumeSyncReplVirtualStatusConnections": eqliscsiVolumeSyncReplVirtualStatusConnections,
       "eqliscsiVolumeSyncReplVirtualStatusAllocatedSpace": eqliscsiVolumeSyncReplVirtualStatusAllocatedSpace,
       "eqliscsiVolumeSyncReplVirtualStatusVolReserveSpace": eqliscsiVolumeSyncReplVirtualStatusVolReserveSpace,
       "eqliscsiVolumeSyncReplVirtualStatusExtConnections": eqliscsiVolumeSyncReplVirtualStatusExtConnections,
       "eqliscsiVolumeSyncReplVirtualStatisticsTable": eqliscsiVolumeSyncReplVirtualStatisticsTable,
       "eqliscsiVolumeSyncReplVirtualStatisticsEntry": eqliscsiVolumeSyncReplVirtualStatisticsEntry,
       "eqliscsiVolumeSyncReplVirtualStatsTxData": eqliscsiVolumeSyncReplVirtualStatsTxData,
       "eqliscsiVolumeSyncReplVirtualStatsRxData": eqliscsiVolumeSyncReplVirtualStatsRxData,
       "eqliscsiVsrVirtualSyncReplStatusTable": eqliscsiVsrVirtualSyncReplStatusTable,
       "eqliscsiVsrVirtualSyncReplStatusEntry": eqliscsiVsrVirtualSyncReplStatusEntry,
       "eqliscsiVsrVirtualSyncReplStatusSyncStatus": eqliscsiVsrVirtualSyncReplStatusSyncStatus,
       "eqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges": eqliscsiVsrVirtualSyncReplStatusUnreplicatedChanges,
       "eqliscsiVsrVirtualSyncReplStatusTotalTxDataMB": eqliscsiVsrVirtualSyncReplStatusTotalTxDataMB,
       "eqliscsiVsrVirtualSyncReplStatusRemainingTxDataMB": eqliscsiVsrVirtualSyncReplStatusRemainingTxDataMB,
       "eqliscsiSyncReplAfoStateTable": eqliscsiSyncReplAfoStateTable,
       "eqliscsiSyncReplAfoStateEntry": eqliscsiSyncReplAfoStateEntry,
       "eqliscsiSyncReplAfoSeqNum": eqliscsiSyncReplAfoSeqNum,
       "eqliscsiSyncReplAfoState": eqliscsiSyncReplAfoState,
       "eqliscsiSyncReplAfoGrpLeadUuid": eqliscsiSyncReplAfoGrpLeadUuid,
       "eqliscsiVolCollectionSyncReplActivePoolTable": eqliscsiVolCollectionSyncReplActivePoolTable,
       "eqliscsiVolCollectionSyncReplActivePoolEntry": eqliscsiVolCollectionSyncReplActivePoolEntry,
       "eqliscsiVolCollectionSyncReplActivePoolRowStatus": eqliscsiVolCollectionSyncReplActivePoolRowStatus,
       "eqliscsiVolCollectionSyncReplActivePoolIndex": eqliscsiVolCollectionSyncReplActivePoolIndex,
       "eqliscsiVolCollectionSyncReplActivePoolFlags": eqliscsiVolCollectionSyncReplActivePoolFlags,
       "eqliscsiVolCollectionSyncReplStatusTable": eqliscsiVolCollectionSyncReplStatusTable,
       "eqliscsiVolCollectionSyncReplStatusEntry": eqliscsiVolCollectionSyncReplStatusEntry,
       "eqliscsiVolCollectionSyncReplStatusSyncStatus": eqliscsiVolCollectionSyncReplStatusSyncStatus,
       "eqliscsiVolCollectionSyncReplStatusUnreplicatedChanges": eqliscsiVolCollectionSyncReplStatusUnreplicatedChanges,
       "eqliscsiVolCollectionSyncReplStatusTotalTxDataMB": eqliscsiVolCollectionSyncReplStatusTotalTxDataMB,
       "eqliscsiVolCollectionSyncReplStatusRemainingTxDataMB": eqliscsiVolCollectionSyncReplStatusRemainingTxDataMB,
       "eqliscsiVolumeSyncReplIndexVolumesTable": eqliscsiVolumeSyncReplIndexVolumesTable,
       "eqliscsiVolumeSyncReplIndexVolumesEntry": eqliscsiVolumeSyncReplIndexVolumesEntry,
       "eqliscsiVolumeSyncReplIndexVolumesPsvId": eqliscsiVolumeSyncReplIndexVolumesPsvId,
       "eqliscsiVolumeSyncReplSyncActiveOfflineTable": eqliscsiVolumeSyncReplSyncActiveOfflineTable,
       "eqliscsiVolumeSyncReplSyncActiveOfflineEntry": eqliscsiVolumeSyncReplSyncActiveOfflineEntry,
       "eqliscsiVolumeSyncReplSyncActiveOffline": eqliscsiVolumeSyncReplSyncActiveOffline,
       "eqliscsiDeletedVolumeInfoTable": eqliscsiDeletedVolumeInfoTable,
       "eqliscsiDeletedVolumeInfoEntry": eqliscsiDeletedVolumeInfoEntry,
       "eqliscsiDeletedVolumeInfoRowStatus": eqliscsiDeletedVolumeInfoRowStatus,
       "eqliscsiDeletedVolumeInfoOriginalName": eqliscsiDeletedVolumeInfoOriginalName,
       "eqliscsiDeletedVolumeInfoOriginalType": eqliscsiDeletedVolumeInfoOriginalType,
       "eqliscsiDeletedVolumeFlags": eqliscsiDeletedVolumeFlags,
       "eqliscsiDeletedVolumeInfoDeleteDate": eqliscsiDeletedVolumeInfoDeleteDate,
       "eqliscsiDeletedVolumeThinWarnPercentage": eqliscsiDeletedVolumeThinWarnPercentage,
       "eqliscsiDeletedVolumeThinMaxGrowPercentage": eqliscsiDeletedVolumeThinMaxGrowPercentage,
       "eqliscsiVolumeSyncReplActivePeerTable": eqliscsiVolumeSyncReplActivePeerTable,
       "eqliscsiVolumeSyncReplActivePeerEntry": eqliscsiVolumeSyncReplActivePeerEntry,
       "eqliscsiVolumeSyncReplActivePeerRowStatus": eqliscsiVolumeSyncReplActivePeerRowStatus,
       "eqliscsiVolumeSyncReplActivePeerLocalMemberId": eqliscsiVolumeSyncReplActivePeerLocalMemberId,
       "eqliscsiVolumeSyncReplActivePeerVolIndex": eqliscsiVolumeSyncReplActivePeerVolIndex,
       "eqliscsiVolumeSyncReplActivePeerFlags": eqliscsiVolumeSyncReplActivePeerFlags,
       "eqliscsiVolumeSyncReplActivePeerLookupTable": eqliscsiVolumeSyncReplActivePeerLookupTable,
       "eqliscsiVolumeSyncReplActivePeerLookupEntry": eqliscsiVolumeSyncReplActivePeerLookupEntry,
       "eqliscsiVolumeSyncReplActivePeerLookupLocalMemberId": eqliscsiVolumeSyncReplActivePeerLookupLocalMemberId,
       "eqliscsiVolumeSyncReplActivePeerLookupVolIndex": eqliscsiVolumeSyncReplActivePeerLookupVolIndex,
       "eqliscsiVolumeSyncReplFailbackTable": eqliscsiVolumeSyncReplFailbackTable,
       "eqliscsiVolumeSyncReplFailbackEntry": eqliscsiVolumeSyncReplFailbackEntry,
       "eqliscsiVolumeSyncReplFailbackRowStatus": eqliscsiVolumeSyncReplFailbackRowStatus,
       "eqliscsiVolumeSyncReplAllowFailback": eqliscsiVolumeSyncReplAllowFailback,
       "eqliscsiVolCollectionSyncReplSyncActiveOfflineTable": eqliscsiVolCollectionSyncReplSyncActiveOfflineTable,
       "eqliscsiVolCollectionSyncReplSyncActiveOfflineEntry": eqliscsiVolCollectionSyncReplSyncActiveOfflineEntry,
       "eqliscsiVolCollectionSyncReplSyncActiveOffline": eqliscsiVolCollectionSyncReplSyncActiveOffline,
       "eqliscsiSyncReplStateTable": eqliscsiSyncReplStateTable,
       "eqliscsiSyncReplStateEntry": eqliscsiSyncReplStateEntry,
       "eqliscsiSyncReplStateSeqNum": eqliscsiSyncReplStateSeqNum,
       "eqliscsiSyncReplStateState": eqliscsiSyncReplStateState,
       "eqliscsiSyncReplStateGrpLeadUuid": eqliscsiSyncReplStateGrpLeadUuid,
       "eqliscsiVsrVirtualSyncReplSyncActiveOfflineTable": eqliscsiVsrVirtualSyncReplSyncActiveOfflineTable,
       "eqliscsiVsrVirtualSyncReplSyncActiveOfflineEntry": eqliscsiVsrVirtualSyncReplSyncActiveOfflineEntry,
       "eqliscsiVsrVirtualSyncReplSyncActiveOffline": eqliscsiVsrVirtualSyncReplSyncActiveOffline,
       "eqliscsiVsrCollectionSyncReplSyncActiveOfflineTable": eqliscsiVsrCollectionSyncReplSyncActiveOfflineTable,
       "eqliscsiVsrCollectionSyncReplSyncActiveOfflineEntry": eqliscsiVsrCollectionSyncReplSyncActiveOfflineEntry,
       "eqliscsiVsrCollectionSyncReplSyncActiveOffline": eqliscsiVsrCollectionSyncReplSyncActiveOffline,
       "eqliscsiVolNameSecondaryIndexTable": eqliscsiVolNameSecondaryIndexTable,
       "eqliscsiVolNameSecondaryIndexEntry": eqliscsiVolNameSecondaryIndexEntry,
       "eqliscsiVolNameSecondaryIndexRowStatus": eqliscsiVolNameSecondaryIndexRowStatus,
       "eqliscsiSharedVolumeSetTable": eqliscsiSharedVolumeSetTable,
       "eqliscsiSharedVolumeSetEntry": eqliscsiSharedVolumeSetEntry,
       "eqliscsiSharedVolumeSetIndex": eqliscsiSharedVolumeSetIndex,
       "eqliscsiSharedVolumeSetRowStatus": eqliscsiSharedVolumeSetRowStatus,
       "eqliscsiSharedVolumeSetPsvid": eqliscsiSharedVolumeSetPsvid,
       "eqliscsiSharedVolumeSetSectorSize": eqliscsiSharedVolumeSetSectorSize,
       "eqliscsiSharedVolumeSetStorageBucketUUID": eqliscsiSharedVolumeSetStorageBucketUUID,
       "eqliscsiSharedVolumeSharedVolumeSetBucket": eqliscsiSharedVolumeSharedVolumeSetBucket,
       "eqliscsiSharedVolumeSetBucketFullPolicy": eqliscsiSharedVolumeSetBucketFullPolicy,
       "eqliscsiSharedVolumeTable": eqliscsiSharedVolumeTable,
       "eqliscsiSharedVolumeEntry": eqliscsiSharedVolumeEntry,
       "eqliscsiSharedVolumeIndex": eqliscsiSharedVolumeIndex,
       "eqliscsiSharedVolumeRowStatus": eqliscsiSharedVolumeRowStatus,
       "eqliscsiSharedVolumePsvid": eqliscsiSharedVolumePsvid,
       "eqliscsiSharedVolumeName": eqliscsiSharedVolumeName,
       "eqliscsiSharedVolumeSize": eqliscsiSharedVolumeSize,
       "eqliscsiSharedVolumeCreatedAs": eqliscsiSharedVolumeCreatedAs,
       "eqliscsiSharedVolumeIfSnapshotOrFastCloneMyParentVVol": eqliscsiSharedVolumeIfSnapshotOrFastCloneMyParentVVol,
       "eqliscsiSharedVolumeSharedVolumeSet": eqliscsiSharedVolumeSharedVolumeSet,
       "eqliscsiSharedVolumeDescription": eqliscsiSharedVolumeDescription,
       "eqliscsiSharedVolumeFlags": eqliscsiSharedVolumeFlags,
       "eqliscsiSharedVolumeSecondaryLunId": eqliscsiSharedVolumeSecondaryLunId,
       "eqlVmwareVirtualVolumeTable": eqlVmwareVirtualVolumeTable,
       "eqlVmwareVirtualVolumeEntry": eqlVmwareVirtualVolumeEntry,
       "eqlVmwareVirtualVolumeRowStatus": eqlVmwareVirtualVolumeRowStatus,
       "eqlVmwareVirtualVolumeType": eqlVmwareVirtualVolumeType,
       "eqlVmWareVirtualVolumeIfSnapshotCreateDate": eqlVmWareVirtualVolumeIfSnapshotCreateDate,
       "eqliscsiSharedVolumeStatusTable": eqliscsiSharedVolumeStatusTable,
       "eqliscsiSharedVolumeStatusEntry": eqliscsiSharedVolumeStatusEntry,
       "eqliscsiSharedVolumeStatusAllocatedSpace": eqliscsiSharedVolumeStatusAllocatedSpace,
       "eqliscsiSharedVolumeStatusSharedSpace": eqliscsiSharedVolumeStatusSharedSpace,
       "eqliscsiSharedVolumeStatusOperStatus": eqliscsiSharedVolumeStatusOperStatus,
       "eqliscsiDynVVolTable": eqliscsiDynVVolTable,
       "eqliscsiDynVVolEntry": eqliscsiDynVVolEntry,
       "eqliscsiDynVVolRowStatus": eqliscsiDynVVolRowStatus,
       "eqliscsiDynVVolName": eqliscsiDynVVolName,
       "eqliscsiDynVVolSize": eqliscsiDynVVolSize,
       "eqliscsiDynVVolContainer": eqliscsiDynVVolContainer,
       "eqliscsiDynVVolDesc": eqliscsiDynVVolDesc,
       "eqliscsiDynVVolCreatedAs": eqliscsiDynVVolCreatedAs,
       "eqliscsiDynVVolIfSnapshotOrFastCloneMyParentVVol": eqliscsiDynVVolIfSnapshotOrFastCloneMyParentVVol,
       "eqliscsiDynVVolType": eqliscsiDynVVolType,
       "eqliscsiDynVVolCreateIsDerived": eqliscsiDynVVolCreateIsDerived,
       "eqliscsiDynVVolCreateDerivedType": eqliscsiDynVVolCreateDerivedType,
       "eqliscsiDynVVolCreateDerivedFromParent": eqliscsiDynVVolCreateDerivedFromParent,
       "eqliscsiDynVVolIfSnapshotMyStatus": eqliscsiDynVVolIfSnapshotMyStatus,
       "eqliscsiDynVVolPsvid": eqliscsiDynVVolPsvid,
       "eqlDynamicSharedVolumeCopyTable": eqlDynamicSharedVolumeCopyTable,
       "eqlDynamicSharedVolumeCopyEntry": eqlDynamicSharedVolumeCopyEntry,
       "eqlDynamicSharedVolumeCopyRowStatus": eqlDynamicSharedVolumeCopyRowStatus,
       "eqlDynamicSharedVolumeCopyDestSharedVolume": eqlDynamicSharedVolumeCopyDestSharedVolume,
       "eqlDynamicSharedVolumeCopySourceSharedVolume": eqlDynamicSharedVolumeCopySourceSharedVolume,
       "eqlDynamicSharedVolumeBindUnbindTable": eqlDynamicSharedVolumeBindUnbindTable,
       "eqlDynamicSharedVolumeBindUnbindEntry": eqlDynamicSharedVolumeBindUnbindEntry,
       "eqlDynamicSharedVolumeBindUnbindRowStatus": eqlDynamicSharedVolumeBindUnbindRowStatus,
       "eqlDynamicSharedVolumeBindUnbindOper": eqlDynamicSharedVolumeBindUnbindOper,
       "eqlDynamicSharedVolumeBindUnbindAccessGroupIndex": eqlDynamicSharedVolumeBindUnbindAccessGroupIndex,
       "eqlDynamicSharedVolumeBindUnbindOperAugment": eqlDynamicSharedVolumeBindUnbindOperAugment,
       "eqliscsiSharedVolumeMetadataTable": eqliscsiSharedVolumeMetadataTable,
       "eqliscsiSharedVolumeMetadataEntry": eqliscsiSharedVolumeMetadataEntry,
       "eqliscsiSharedVolumeMetadataRowStatus": eqliscsiSharedVolumeMetadataRowStatus,
       "eqliscsiSharedVolumeMetadataIndex": eqliscsiSharedVolumeMetadataIndex,
       "eqliscsiSharedVolumeMetadataKey": eqliscsiSharedVolumeMetadataKey,
       "eqliscsiSharedVolumeMetadataValue": eqliscsiSharedVolumeMetadataValue,
       "eqlPreppedSnapshotVVolTable": eqlPreppedSnapshotVVolTable,
       "eqlPreppedSnapshotVVolEntry": eqlPreppedSnapshotVVolEntry,
       "eqlPreppedSnapshotVVolRowStatus": eqlPreppedSnapshotVVolRowStatus,
       "eqlPreppedSnapshotVVolPsvid": eqlPreppedSnapshotVVolPsvid,
       "eqlPreppedSnapshotVVolName": eqlPreppedSnapshotVVolName,
       "eqlPreppedSnapshotVVolSize": eqlPreppedSnapshotVVolSize,
       "eqlPreppedSnapshotVVolMyParentVVol": eqlPreppedSnapshotVVolMyParentVVol,
       "eqlPreppedSnapshotVVolBucket": eqlPreppedSnapshotVVolBucket,
       "eqlPreppedSnapshotVVolDescription": eqlPreppedSnapshotVVolDescription,
       "eqlDynamicSharedVolumeDiffTable": eqlDynamicSharedVolumeDiffTable,
       "eqlDynamicSharedVolumeDiffEntry": eqlDynamicSharedVolumeDiffEntry,
       "eqlDynamicSharedVolumeDiffRowStatus": eqlDynamicSharedVolumeDiffRowStatus,
       "eqlDynamicSharedVolumeDiffBaseIndex": eqlDynamicSharedVolumeDiffBaseIndex,
       "eqlDynamicSharedVolumeDiffAdmin": eqlDynamicSharedVolumeDiffAdmin,
       "eqlDynamicSharedVolumeDiffStartSegmentOffset": eqlDynamicSharedVolumeDiffStartSegmentOffset,
       "eqlDynamicSharedVolumeDiffSegmentsLength": eqlDynamicSharedVolumeDiffSegmentsLength,
       "eqlDynamicSharedVolumeDiffChunkSize": eqlDynamicSharedVolumeDiffChunkSize,
       "eqliscsiVolumeCompressionConfigurationTable": eqliscsiVolumeCompressionConfigurationTable,
       "eqliscsiVolumeCompressionConfigurationEntry": eqliscsiVolumeCompressionConfigurationEntry,
       "eqliscsiVolumeCompressionConfigurationRowStatus": eqliscsiVolumeCompressionConfigurationRowStatus,
       "eqliscsiVolumeCompressionConfigurationPolicy": eqliscsiVolumeCompressionConfigurationPolicy,
       "eqliscsiVolumeCompressionConfigurationSnapDelay": eqliscsiVolumeCompressionConfigurationSnapDelay,
       "eqlDynamicSharedVolumeDiffChunkTable": eqlDynamicSharedVolumeDiffChunkTable,
       "eqlDynamicSharedVolumeDiffChunkEntry": eqlDynamicSharedVolumeDiffChunkEntry,
       "eqlDynamicSharedVolumeDiffChunkIndex": eqlDynamicSharedVolumeDiffChunkIndex,
       "eqlDynamicSharedVolumeDiffChunkSegmentSize": eqlDynamicSharedVolumeDiffChunkSegmentSize,
       "eqlDynamicSharedVolumeDiffNumChunkSegments": eqlDynamicSharedVolumeDiffNumChunkSegments,
       "eqlDynamicSharedVolumeDiffChunkModified": eqlDynamicSharedVolumeDiffChunkModified,
       "eqliscsiVolumeMetadataTable": eqliscsiVolumeMetadataTable,
       "eqliscsiVolumeMetadataEntry": eqliscsiVolumeMetadataEntry,
       "eqliscsiVolumeMetadataRowStatus": eqliscsiVolumeMetadataRowStatus,
       "eqliscsiVolumeMetadataIndex": eqliscsiVolumeMetadataIndex,
       "eqliscsiVolumeMetadataKey": eqliscsiVolumeMetadataKey,
       "eqliscsiVolumeMetadataValue": eqliscsiVolumeMetadataValue,
       "eqliscsiSnapshotMetadataTable": eqliscsiSnapshotMetadataTable,
       "eqliscsiSnapshotMetadataEntry": eqliscsiSnapshotMetadataEntry,
       "eqliscsiSnapshotMetadataRowStatus": eqliscsiSnapshotMetadataRowStatus,
       "eqliscsiSnapshotMetadataIndex": eqliscsiSnapshotMetadataIndex,
       "eqliscsiSnapshotMetadataKey": eqliscsiSnapshotMetadataKey,
       "eqliscsiSnapshotMetadataValue": eqliscsiSnapshotMetadataValue,
       "eqliscsiSyncReplAfoTiebreakerTable": eqliscsiSyncReplAfoTiebreakerTable,
       "eqliscsiSyncReplAfoTiebreakerEntry": eqliscsiSyncReplAfoTiebreakerEntry,
       "eqliscsiSyncReplAfoTiebreakerSeqNum": eqliscsiSyncReplAfoTiebreakerSeqNum,
       "eqliscsiSyncReplAfoTiebreaker": eqliscsiSyncReplAfoTiebreaker,
       "eqliscsiSyncReplAfoTiebreakerGrpLeadUuid": eqliscsiSyncReplAfoTiebreakerGrpLeadUuid,
       "eqliscsiSharedVolumeStatisticsTable": eqliscsiSharedVolumeStatisticsTable,
       "eqliscsiSharedVolumeStatisticsEntry": eqliscsiSharedVolumeStatisticsEntry,
       "eqliscsiSharedVolumeStatsCmdPdus": eqliscsiSharedVolumeStatsCmdPdus,
       "eqliscsiSharedVolumeStatsRspPdus": eqliscsiSharedVolumeStatsRspPdus,
       "eqliscsiSharedVolumeStatsTxData": eqliscsiSharedVolumeStatsTxData,
       "eqliscsiSharedVolumeStatsRxData": eqliscsiSharedVolumeStatsRxData,
       "eqliscsiSharedVolumeStatsNoOfSessions": eqliscsiSharedVolumeStatsNoOfSessions,
       "eqliscsiSharedVolumeStatsReadLatency": eqliscsiSharedVolumeStatsReadLatency,
       "eqliscsiSharedVolumeStatsWriteLatency": eqliscsiSharedVolumeStatsWriteLatency,
       "eqliscsiSharedVolumeStatsReadOpCount": eqliscsiSharedVolumeStatsReadOpCount,
       "eqliscsiSharedVolumeStatsWriteOpCount": eqliscsiSharedVolumeStatsWriteOpCount,
       "eqliscsiSharedVolumeStatsReadAvgLatency": eqliscsiSharedVolumeStatsReadAvgLatency,
       "eqliscsiSharedVolumeStatsWriteAvgLatency": eqliscsiSharedVolumeStatsWriteAvgLatency,
       "eqliscsiSharedVolumeStatsHCIscsiReadWriteCmdsReceived": eqliscsiSharedVolumeStatsHCIscsiReadWriteCmdsReceived,
       "eqliscsiSharedVolumeStatsHCIscsiTotalQD": eqliscsiSharedVolumeStatsHCIscsiTotalQD,
       "eqliscsiSharedVolumeStatsMisAlignedIO": eqliscsiSharedVolumeStatsMisAlignedIO,
       "eqliscsiNodeTable": eqliscsiNodeTable,
       "eqliscsiNodeEntry": eqliscsiNodeEntry,
       "eqliscsiNodeIndex": eqliscsiNodeIndex,
       "eqliscsiNodeLocalMemberId": eqliscsiNodeLocalMemberId,
       "eqliscsiNodeVolumeIndex": eqliscsiNodeVolumeIndex,
       "eqliscsiNodeSnapshotIndex": eqliscsiNodeSnapshotIndex,
       "eqliscsiNotifications": eqliscsiNotifications,
       "eqliscsiConformance": eqliscsiConformance}
)
