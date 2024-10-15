# SNMP MIB module (SNA-NAU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNA-NAU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:30 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 InstancePointer,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "InstancePointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

snanauMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnanauObjects_ObjectIdentity = ObjectIdentity
snanauObjects = _SnanauObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 1)
)
_SnaNode_ObjectIdentity = ObjectIdentity
snaNode = _SnaNode_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 1, 1)
)
_SnaNodeAdminTable_Object = MibTable
snaNodeAdminTable = _SnaNodeAdminTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1)
)
if mibBuilder.loadTexts:
    snaNodeAdminTable.setStatus("current")
_SnaNodeAdminEntry_Object = MibTableRow
snaNodeAdminEntry = _SnaNodeAdminEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1)
)
snaNodeAdminEntry.setIndexNames(
    (0, "SNA-NAU-MIB", "snaNodeAdminIndex"),
)
if mibBuilder.loadTexts:
    snaNodeAdminEntry.setStatus("current")
_SnaNodeAdminIndex_Type = Integer32
_SnaNodeAdminIndex_Object = MibTableColumn
snaNodeAdminIndex = _SnaNodeAdminIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 1),
    _SnaNodeAdminIndex_Type()
)
snaNodeAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snaNodeAdminIndex.setStatus("current")


class _SnaNodeAdminName_Type(DisplayString):
    """Custom type snaNodeAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SnaNodeAdminName_Type.__name__ = "DisplayString"
_SnaNodeAdminName_Object = MibTableColumn
snaNodeAdminName = _SnaNodeAdminName_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 2),
    _SnaNodeAdminName_Type()
)
snaNodeAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminName.setStatus("current")


class _SnaNodeAdminType_Type(Integer32):
    """Custom type snaNodeAdminType based on Integer32"""
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
        *(("endNode", 5),
          ("networkNode", 6),
          ("other", 1),
          ("pu10", 2),
          ("pu20", 3),
          ("t21len", 4))
    )


_SnaNodeAdminType_Type.__name__ = "Integer32"
_SnaNodeAdminType_Object = MibTableColumn
snaNodeAdminType = _SnaNodeAdminType_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 3),
    _SnaNodeAdminType_Type()
)
snaNodeAdminType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminType.setStatus("current")


class _SnaNodeAdminXidFormat_Type(Integer32):
    """Custom type snaNodeAdminXidFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("format0", 1),
          ("format1", 2),
          ("format3", 3))
    )


_SnaNodeAdminXidFormat_Type.__name__ = "Integer32"
_SnaNodeAdminXidFormat_Object = MibTableColumn
snaNodeAdminXidFormat = _SnaNodeAdminXidFormat_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 4),
    _SnaNodeAdminXidFormat_Type()
)
snaNodeAdminXidFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminXidFormat.setStatus("current")


class _SnaNodeAdminBlockNum_Type(DisplayString):
    """Custom type snaNodeAdminBlockNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SnaNodeAdminBlockNum_Type.__name__ = "DisplayString"
_SnaNodeAdminBlockNum_Object = MibTableColumn
snaNodeAdminBlockNum = _SnaNodeAdminBlockNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 5),
    _SnaNodeAdminBlockNum_Type()
)
snaNodeAdminBlockNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminBlockNum.setStatus("current")


class _SnaNodeAdminIdNum_Type(DisplayString):
    """Custom type snaNodeAdminIdNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_SnaNodeAdminIdNum_Type.__name__ = "DisplayString"
_SnaNodeAdminIdNum_Object = MibTableColumn
snaNodeAdminIdNum = _SnaNodeAdminIdNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 6),
    _SnaNodeAdminIdNum_Type()
)
snaNodeAdminIdNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminIdNum.setStatus("current")


class _SnaNodeAdminEnablingMethod_Type(Integer32):
    """Custom type snaNodeAdminEnablingMethod based on Integer32"""
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
        *(("demand", 3),
          ("onlyMS", 4),
          ("other", 1),
          ("startup", 2))
    )


_SnaNodeAdminEnablingMethod_Type.__name__ = "Integer32"
_SnaNodeAdminEnablingMethod_Object = MibTableColumn
snaNodeAdminEnablingMethod = _SnaNodeAdminEnablingMethod_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 7),
    _SnaNodeAdminEnablingMethod_Type()
)
snaNodeAdminEnablingMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminEnablingMethod.setStatus("current")


class _SnaNodeAdminLuTermDefault_Type(Integer32):
    """Custom type snaNodeAdminLuTermDefault based on Integer32"""
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
        *(("poweroff", 4),
          ("rshutd", 3),
          ("termself", 2),
          ("unbind", 1))
    )


_SnaNodeAdminLuTermDefault_Type.__name__ = "Integer32"
_SnaNodeAdminLuTermDefault_Object = MibTableColumn
snaNodeAdminLuTermDefault = _SnaNodeAdminLuTermDefault_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 8),
    _SnaNodeAdminLuTermDefault_Type()
)
snaNodeAdminLuTermDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminLuTermDefault.setStatus("current")
_SnaNodeAdminMaxLu_Type = Integer32
_SnaNodeAdminMaxLu_Object = MibTableColumn
snaNodeAdminMaxLu = _SnaNodeAdminMaxLu_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 9),
    _SnaNodeAdminMaxLu_Type()
)
snaNodeAdminMaxLu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminMaxLu.setStatus("current")


class _SnaNodeAdminHostDescription_Type(DisplayString):
    """Custom type snaNodeAdminHostDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnaNodeAdminHostDescription_Type.__name__ = "DisplayString"
_SnaNodeAdminHostDescription_Object = MibTableColumn
snaNodeAdminHostDescription = _SnaNodeAdminHostDescription_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 10),
    _SnaNodeAdminHostDescription_Type()
)
snaNodeAdminHostDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminHostDescription.setStatus("current")


class _SnaNodeAdminStopMethod_Type(Integer32):
    """Custom type snaNodeAdminStopMethod based on Integer32"""
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
        *(("force", 4),
          ("immed", 3),
          ("normal", 2),
          ("other", 1))
    )


_SnaNodeAdminStopMethod_Type.__name__ = "Integer32"
_SnaNodeAdminStopMethod_Object = MibTableColumn
snaNodeAdminStopMethod = _SnaNodeAdminStopMethod_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 11),
    _SnaNodeAdminStopMethod_Type()
)
snaNodeAdminStopMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminStopMethod.setStatus("current")


class _SnaNodeAdminState_Type(Integer32):
    """Custom type snaNodeAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SnaNodeAdminState_Type.__name__ = "Integer32"
_SnaNodeAdminState_Object = MibTableColumn
snaNodeAdminState = _SnaNodeAdminState_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 12),
    _SnaNodeAdminState_Type()
)
snaNodeAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminState.setStatus("current")
_SnaNodeAdminRowStatus_Type = RowStatus
_SnaNodeAdminRowStatus_Object = MibTableColumn
snaNodeAdminRowStatus = _SnaNodeAdminRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 1, 1, 13),
    _SnaNodeAdminRowStatus_Type()
)
snaNodeAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeAdminRowStatus.setStatus("current")
_SnaNodeAdminTableLastChange_Type = TimeStamp
_SnaNodeAdminTableLastChange_Object = MibScalar
snaNodeAdminTableLastChange = _SnaNodeAdminTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 2),
    _SnaNodeAdminTableLastChange_Type()
)
snaNodeAdminTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeAdminTableLastChange.setStatus("current")
_SnaNodeOperTable_Object = MibTable
snaNodeOperTable = _SnaNodeOperTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3)
)
if mibBuilder.loadTexts:
    snaNodeOperTable.setStatus("current")
_SnaNodeOperEntry_Object = MibTableRow
snaNodeOperEntry = _SnaNodeOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1)
)
snaNodeOperEntry.setIndexNames(
    (0, "SNA-NAU-MIB", "snaNodeAdminIndex"),
)
if mibBuilder.loadTexts:
    snaNodeOperEntry.setStatus("current")


class _SnaNodeOperName_Type(DisplayString):
    """Custom type snaNodeOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SnaNodeOperName_Type.__name__ = "DisplayString"
_SnaNodeOperName_Object = MibTableColumn
snaNodeOperName = _SnaNodeOperName_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 1),
    _SnaNodeOperName_Type()
)
snaNodeOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperName.setStatus("current")


class _SnaNodeOperType_Type(Integer32):
    """Custom type snaNodeOperType based on Integer32"""
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
        *(("endNode", 5),
          ("networkNode", 6),
          ("other", 1),
          ("pu10", 2),
          ("pu20", 3),
          ("t21LEN", 4))
    )


_SnaNodeOperType_Type.__name__ = "Integer32"
_SnaNodeOperType_Object = MibTableColumn
snaNodeOperType = _SnaNodeOperType_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 2),
    _SnaNodeOperType_Type()
)
snaNodeOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperType.setStatus("current")


class _SnaNodeOperXidFormat_Type(Integer32):
    """Custom type snaNodeOperXidFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("format0", 1),
          ("format1", 2),
          ("format3", 3))
    )


_SnaNodeOperXidFormat_Type.__name__ = "Integer32"
_SnaNodeOperXidFormat_Object = MibTableColumn
snaNodeOperXidFormat = _SnaNodeOperXidFormat_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 3),
    _SnaNodeOperXidFormat_Type()
)
snaNodeOperXidFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperXidFormat.setStatus("current")


class _SnaNodeOperBlockNum_Type(DisplayString):
    """Custom type snaNodeOperBlockNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SnaNodeOperBlockNum_Type.__name__ = "DisplayString"
_SnaNodeOperBlockNum_Object = MibTableColumn
snaNodeOperBlockNum = _SnaNodeOperBlockNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 4),
    _SnaNodeOperBlockNum_Type()
)
snaNodeOperBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperBlockNum.setStatus("current")


class _SnaNodeOperIdNum_Type(DisplayString):
    """Custom type snaNodeOperIdNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_SnaNodeOperIdNum_Type.__name__ = "DisplayString"
_SnaNodeOperIdNum_Object = MibTableColumn
snaNodeOperIdNum = _SnaNodeOperIdNum_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 5),
    _SnaNodeOperIdNum_Type()
)
snaNodeOperIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperIdNum.setStatus("current")


class _SnaNodeOperEnablingMethod_Type(Integer32):
    """Custom type snaNodeOperEnablingMethod based on Integer32"""
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
        *(("demand", 3),
          ("onlyMS", 4),
          ("other", 1),
          ("startup", 2))
    )


_SnaNodeOperEnablingMethod_Type.__name__ = "Integer32"
_SnaNodeOperEnablingMethod_Object = MibTableColumn
snaNodeOperEnablingMethod = _SnaNodeOperEnablingMethod_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 6),
    _SnaNodeOperEnablingMethod_Type()
)
snaNodeOperEnablingMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperEnablingMethod.setStatus("current")


class _SnaNodeOperLuTermDefault_Type(Integer32):
    """Custom type snaNodeOperLuTermDefault based on Integer32"""
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
        *(("poweroff", 4),
          ("rshutd", 3),
          ("termself", 2),
          ("unbind", 1))
    )


_SnaNodeOperLuTermDefault_Type.__name__ = "Integer32"
_SnaNodeOperLuTermDefault_Object = MibTableColumn
snaNodeOperLuTermDefault = _SnaNodeOperLuTermDefault_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 7),
    _SnaNodeOperLuTermDefault_Type()
)
snaNodeOperLuTermDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperLuTermDefault.setStatus("current")
_SnaNodeOperMaxLu_Type = Integer32
_SnaNodeOperMaxLu_Object = MibTableColumn
snaNodeOperMaxLu = _SnaNodeOperMaxLu_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 8),
    _SnaNodeOperMaxLu_Type()
)
snaNodeOperMaxLu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperMaxLu.setStatus("current")


class _SnaNodeOperHostDescription_Type(DisplayString):
    """Custom type snaNodeOperHostDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnaNodeOperHostDescription_Type.__name__ = "DisplayString"
_SnaNodeOperHostDescription_Object = MibTableColumn
snaNodeOperHostDescription = _SnaNodeOperHostDescription_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 9),
    _SnaNodeOperHostDescription_Type()
)
snaNodeOperHostDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperHostDescription.setStatus("current")


class _SnaNodeOperStopMethod_Type(Integer32):
    """Custom type snaNodeOperStopMethod based on Integer32"""
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
        *(("force", 4),
          ("immed", 3),
          ("normal", 2),
          ("other", 1))
    )


_SnaNodeOperStopMethod_Type.__name__ = "Integer32"
_SnaNodeOperStopMethod_Object = MibTableColumn
snaNodeOperStopMethod = _SnaNodeOperStopMethod_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 10),
    _SnaNodeOperStopMethod_Type()
)
snaNodeOperStopMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperStopMethod.setStatus("current")


class _SnaNodeOperState_Type(Integer32):
    """Custom type snaNodeOperState based on Integer32"""
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
        *(("active", 2),
          ("inactive", 1),
          ("stopping", 4),
          ("waiting", 3))
    )


_SnaNodeOperState_Type.__name__ = "Integer32"
_SnaNodeOperState_Object = MibTableColumn
snaNodeOperState = _SnaNodeOperState_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 11),
    _SnaNodeOperState_Type()
)
snaNodeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperState.setStatus("current")


class _SnaNodeOperHostSscpId_Type(OctetString):
    """Custom type snaNodeOperHostSscpId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SnaNodeOperHostSscpId_Type.__name__ = "OctetString"
_SnaNodeOperHostSscpId_Object = MibTableColumn
snaNodeOperHostSscpId = _SnaNodeOperHostSscpId_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 12),
    _SnaNodeOperHostSscpId_Type()
)
snaNodeOperHostSscpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperHostSscpId.setStatus("current")
_SnaNodeOperStartTime_Type = TimeStamp
_SnaNodeOperStartTime_Object = MibTableColumn
snaNodeOperStartTime = _SnaNodeOperStartTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 13),
    _SnaNodeOperStartTime_Type()
)
snaNodeOperStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperStartTime.setStatus("current")
_SnaNodeOperLastStateChange_Type = TimeStamp
_SnaNodeOperLastStateChange_Object = MibTableColumn
snaNodeOperLastStateChange = _SnaNodeOperLastStateChange_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 14),
    _SnaNodeOperLastStateChange_Type()
)
snaNodeOperLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperLastStateChange.setStatus("current")
_SnaNodeOperActFailures_Type = Counter32
_SnaNodeOperActFailures_Object = MibTableColumn
snaNodeOperActFailures = _SnaNodeOperActFailures_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 15),
    _SnaNodeOperActFailures_Type()
)
snaNodeOperActFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperActFailures.setStatus("current")


class _SnaNodeOperActFailureReason_Type(Integer32):
    """Custom type snaNodeOperActFailureReason based on Integer32"""
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
        *(("badConfiguration", 4),
          ("internalError", 5),
          ("linkFailure", 2),
          ("noResources", 3),
          ("other", 1))
    )


_SnaNodeOperActFailureReason_Type.__name__ = "Integer32"
_SnaNodeOperActFailureReason_Object = MibTableColumn
snaNodeOperActFailureReason = _SnaNodeOperActFailureReason_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 3, 1, 16),
    _SnaNodeOperActFailureReason_Type()
)
snaNodeOperActFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperActFailureReason.setStatus("current")
_SnaNodeOperTableLastChange_Type = TimeStamp
_SnaNodeOperTableLastChange_Object = MibScalar
snaNodeOperTableLastChange = _SnaNodeOperTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 4),
    _SnaNodeOperTableLastChange_Type()
)
snaNodeOperTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeOperTableLastChange.setStatus("current")
_SnaPu20StatsTable_Object = MibTable
snaPu20StatsTable = _SnaPu20StatsTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5)
)
if mibBuilder.loadTexts:
    snaPu20StatsTable.setStatus("current")
_SnaPu20StatsEntry_Object = MibTableRow
snaPu20StatsEntry = _SnaPu20StatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1)
)
snaPu20StatsEntry.setIndexNames(
    (0, "SNA-NAU-MIB", "snaNodeAdminIndex"),
)
if mibBuilder.loadTexts:
    snaPu20StatsEntry.setStatus("current")
_SnaPu20StatsSentBytes_Type = Counter32
_SnaPu20StatsSentBytes_Object = MibTableColumn
snaPu20StatsSentBytes = _SnaPu20StatsSentBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 1),
    _SnaPu20StatsSentBytes_Type()
)
snaPu20StatsSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaPu20StatsSentBytes.setStatus("current")
_SnaPu20StatsReceivedBytes_Type = Counter32
_SnaPu20StatsReceivedBytes_Object = MibTableColumn
snaPu20StatsReceivedBytes = _SnaPu20StatsReceivedBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 2),
    _SnaPu20StatsReceivedBytes_Type()
)
snaPu20StatsReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaPu20StatsReceivedBytes.setStatus("current")
_SnaPu20StatsSentPius_Type = Counter32
_SnaPu20StatsSentPius_Object = MibTableColumn
snaPu20StatsSentPius = _SnaPu20StatsSentPius_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 3),
    _SnaPu20StatsSentPius_Type()
)
snaPu20StatsSentPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaPu20StatsSentPius.setStatus("current")
_SnaPu20StatsReceivedPius_Type = Counter32
_SnaPu20StatsReceivedPius_Object = MibTableColumn
snaPu20StatsReceivedPius = _SnaPu20StatsReceivedPius_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 4),
    _SnaPu20StatsReceivedPius_Type()
)
snaPu20StatsReceivedPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaPu20StatsReceivedPius.setStatus("current")
_SnaPu20StatsSentNegativeResps_Type = Counter32
_SnaPu20StatsSentNegativeResps_Object = MibTableColumn
snaPu20StatsSentNegativeResps = _SnaPu20StatsSentNegativeResps_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 5),
    _SnaPu20StatsSentNegativeResps_Type()
)
snaPu20StatsSentNegativeResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaPu20StatsSentNegativeResps.setStatus("current")
_SnaPu20StatsReceivedNegativeResps_Type = Counter32
_SnaPu20StatsReceivedNegativeResps_Object = MibTableColumn
snaPu20StatsReceivedNegativeResps = _SnaPu20StatsReceivedNegativeResps_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 6),
    _SnaPu20StatsReceivedNegativeResps_Type()
)
snaPu20StatsReceivedNegativeResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaPu20StatsReceivedNegativeResps.setStatus("current")
_SnaPu20StatsActLus_Type = Gauge32
_SnaPu20StatsActLus_Object = MibTableColumn
snaPu20StatsActLus = _SnaPu20StatsActLus_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 7),
    _SnaPu20StatsActLus_Type()
)
snaPu20StatsActLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaPu20StatsActLus.setStatus("current")
_SnaPu20StatsInActLus_Type = Gauge32
_SnaPu20StatsInActLus_Object = MibTableColumn
snaPu20StatsInActLus = _SnaPu20StatsInActLus_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 8),
    _SnaPu20StatsInActLus_Type()
)
snaPu20StatsInActLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaPu20StatsInActLus.setStatus("current")
_SnaPu20StatsBindLus_Type = Gauge32
_SnaPu20StatsBindLus_Object = MibTableColumn
snaPu20StatsBindLus = _SnaPu20StatsBindLus_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 5, 1, 9),
    _SnaPu20StatsBindLus_Type()
)
snaPu20StatsBindLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaPu20StatsBindLus.setStatus("current")
_SnaNodeLinkAdminTable_Object = MibTable
snaNodeLinkAdminTable = _SnaNodeLinkAdminTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 6)
)
if mibBuilder.loadTexts:
    snaNodeLinkAdminTable.setStatus("current")
_SnaNodeLinkAdminEntry_Object = MibTableRow
snaNodeLinkAdminEntry = _SnaNodeLinkAdminEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1)
)
snaNodeLinkAdminEntry.setIndexNames(
    (0, "SNA-NAU-MIB", "snaNodeAdminIndex"),
    (0, "SNA-NAU-MIB", "snaNodeLinkAdminIndex"),
)
if mibBuilder.loadTexts:
    snaNodeLinkAdminEntry.setStatus("current")
_SnaNodeLinkAdminIndex_Type = Integer32
_SnaNodeLinkAdminIndex_Object = MibTableColumn
snaNodeLinkAdminIndex = _SnaNodeLinkAdminIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 1),
    _SnaNodeLinkAdminIndex_Type()
)
snaNodeLinkAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snaNodeLinkAdminIndex.setStatus("current")
_SnaNodeLinkAdminSpecific_Type = InstancePointer
_SnaNodeLinkAdminSpecific_Object = MibTableColumn
snaNodeLinkAdminSpecific = _SnaNodeLinkAdminSpecific_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 2),
    _SnaNodeLinkAdminSpecific_Type()
)
snaNodeLinkAdminSpecific.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeLinkAdminSpecific.setStatus("current")
_SnaNodeLinkAdminMaxPiu_Type = Integer32
_SnaNodeLinkAdminMaxPiu_Object = MibTableColumn
snaNodeLinkAdminMaxPiu = _SnaNodeLinkAdminMaxPiu_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 3),
    _SnaNodeLinkAdminMaxPiu_Type()
)
snaNodeLinkAdminMaxPiu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeLinkAdminMaxPiu.setStatus("current")
_SnaNodeLinkAdminRowStatus_Type = RowStatus
_SnaNodeLinkAdminRowStatus_Object = MibTableColumn
snaNodeLinkAdminRowStatus = _SnaNodeLinkAdminRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 6, 1, 4),
    _SnaNodeLinkAdminRowStatus_Type()
)
snaNodeLinkAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaNodeLinkAdminRowStatus.setStatus("current")
_SnaNodeLinkAdminTableLastChange_Type = TimeStamp
_SnaNodeLinkAdminTableLastChange_Object = MibScalar
snaNodeLinkAdminTableLastChange = _SnaNodeLinkAdminTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 7),
    _SnaNodeLinkAdminTableLastChange_Type()
)
snaNodeLinkAdminTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeLinkAdminTableLastChange.setStatus("current")
_SnaNodeLinkOperTable_Object = MibTable
snaNodeLinkOperTable = _SnaNodeLinkOperTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 8)
)
if mibBuilder.loadTexts:
    snaNodeLinkOperTable.setStatus("current")
_SnaNodeLinkOperEntry_Object = MibTableRow
snaNodeLinkOperEntry = _SnaNodeLinkOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 8, 1)
)
snaNodeLinkOperEntry.setIndexNames(
    (0, "SNA-NAU-MIB", "snaNodeAdminIndex"),
    (0, "SNA-NAU-MIB", "snaNodeLinkAdminIndex"),
)
if mibBuilder.loadTexts:
    snaNodeLinkOperEntry.setStatus("current")
_SnaNodeLinkOperSpecific_Type = InstancePointer
_SnaNodeLinkOperSpecific_Object = MibTableColumn
snaNodeLinkOperSpecific = _SnaNodeLinkOperSpecific_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 8, 1, 1),
    _SnaNodeLinkOperSpecific_Type()
)
snaNodeLinkOperSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeLinkOperSpecific.setStatus("current")
_SnaNodeLinkOperMaxPiu_Type = Integer32
_SnaNodeLinkOperMaxPiu_Object = MibTableColumn
snaNodeLinkOperMaxPiu = _SnaNodeLinkOperMaxPiu_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 8, 1, 2),
    _SnaNodeLinkOperMaxPiu_Type()
)
snaNodeLinkOperMaxPiu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeLinkOperMaxPiu.setStatus("current")
_SnaNodeLinkOperTableLastChange_Type = TimeStamp
_SnaNodeLinkOperTableLastChange_Object = MibScalar
snaNodeLinkOperTableLastChange = _SnaNodeLinkOperTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 9),
    _SnaNodeLinkOperTableLastChange_Type()
)
snaNodeLinkOperTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaNodeLinkOperTableLastChange.setStatus("current")
_SnaNodeTraps_ObjectIdentity = ObjectIdentity
snaNodeTraps = _SnaNodeTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 10)
)
_SnaLu_ObjectIdentity = ObjectIdentity
snaLu = _SnaLu_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 1, 2)
)
_SnaLuAdminTable_Object = MibTable
snaLuAdminTable = _SnaLuAdminTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1)
)
if mibBuilder.loadTexts:
    snaLuAdminTable.setStatus("current")
_SnaLuAdminEntry_Object = MibTableRow
snaLuAdminEntry = _SnaLuAdminEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1)
)
snaLuAdminEntry.setIndexNames(
    (0, "SNA-NAU-MIB", "snaNodeAdminIndex"),
    (0, "SNA-NAU-MIB", "snaLuAdminLuIndex"),
)
if mibBuilder.loadTexts:
    snaLuAdminEntry.setStatus("current")
_SnaLuAdminLuIndex_Type = Integer32
_SnaLuAdminLuIndex_Object = MibTableColumn
snaLuAdminLuIndex = _SnaLuAdminLuIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 1),
    _SnaLuAdminLuIndex_Type()
)
snaLuAdminLuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snaLuAdminLuIndex.setStatus("current")


class _SnaLuAdminName_Type(DisplayString):
    """Custom type snaLuAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnaLuAdminName_Type.__name__ = "DisplayString"
_SnaLuAdminName_Object = MibTableColumn
snaLuAdminName = _SnaLuAdminName_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 2),
    _SnaLuAdminName_Type()
)
snaLuAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaLuAdminName.setStatus("current")


class _SnaLuAdminSnaName_Type(DisplayString):
    """Custom type snaLuAdminSnaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SnaLuAdminSnaName_Type.__name__ = "DisplayString"
_SnaLuAdminSnaName_Object = MibTableColumn
snaLuAdminSnaName = _SnaLuAdminSnaName_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 3),
    _SnaLuAdminSnaName_Type()
)
snaLuAdminSnaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaLuAdminSnaName.setStatus("current")


class _SnaLuAdminType_Type(Integer32):
    """Custom type snaLuAdminType based on Integer32"""
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
        *(("lu0", 2),
          ("lu1", 3),
          ("lu2", 4),
          ("lu3", 5),
          ("lu4", 6),
          ("lu62", 7),
          ("lu7", 8),
          ("other", 1))
    )


_SnaLuAdminType_Type.__name__ = "Integer32"
_SnaLuAdminType_Object = MibTableColumn
snaLuAdminType = _SnaLuAdminType_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 4),
    _SnaLuAdminType_Type()
)
snaLuAdminType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaLuAdminType.setStatus("current")


class _SnaLuAdminDepType_Type(Integer32):
    """Custom type snaLuAdminDepType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dependent", 1),
          ("independent", 2))
    )


_SnaLuAdminDepType_Type.__name__ = "Integer32"
_SnaLuAdminDepType_Object = MibTableColumn
snaLuAdminDepType = _SnaLuAdminDepType_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 5),
    _SnaLuAdminDepType_Type()
)
snaLuAdminDepType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaLuAdminDepType.setStatus("current")


class _SnaLuAdminLocalAddress_Type(OctetString):
    """Custom type snaLuAdminLocalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SnaLuAdminLocalAddress_Type.__name__ = "OctetString"
_SnaLuAdminLocalAddress_Object = MibTableColumn
snaLuAdminLocalAddress = _SnaLuAdminLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 6),
    _SnaLuAdminLocalAddress_Type()
)
snaLuAdminLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaLuAdminLocalAddress.setStatus("current")


class _SnaLuAdminDisplayModel_Type(Integer32):
    """Custom type snaLuAdminDisplayModel based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 10),
          ("invalid", 1),
          ("model2A", 2),
          ("model2B", 3),
          ("model3A", 4),
          ("model3B", 5),
          ("model4A", 6),
          ("model4B", 7),
          ("model5A", 8),
          ("model5B", 9))
    )


_SnaLuAdminDisplayModel_Type.__name__ = "Integer32"
_SnaLuAdminDisplayModel_Object = MibTableColumn
snaLuAdminDisplayModel = _SnaLuAdminDisplayModel_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 7),
    _SnaLuAdminDisplayModel_Type()
)
snaLuAdminDisplayModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaLuAdminDisplayModel.setStatus("current")


class _SnaLuAdminTerm_Type(Integer32):
    """Custom type snaLuAdminTerm based on Integer32"""
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
        *(("poweroff", 4),
          ("rshutd", 3),
          ("termself", 2),
          ("unbind", 1))
    )


_SnaLuAdminTerm_Type.__name__ = "Integer32"
_SnaLuAdminTerm_Object = MibTableColumn
snaLuAdminTerm = _SnaLuAdminTerm_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 8),
    _SnaLuAdminTerm_Type()
)
snaLuAdminTerm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaLuAdminTerm.setStatus("current")
_SnaLuAdminRowStatus_Type = RowStatus
_SnaLuAdminRowStatus_Object = MibTableColumn
snaLuAdminRowStatus = _SnaLuAdminRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 1, 1, 9),
    _SnaLuAdminRowStatus_Type()
)
snaLuAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snaLuAdminRowStatus.setStatus("current")
_SnaLuOperTable_Object = MibTable
snaLuOperTable = _SnaLuOperTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2)
)
if mibBuilder.loadTexts:
    snaLuOperTable.setStatus("current")
_SnaLuOperEntry_Object = MibTableRow
snaLuOperEntry = _SnaLuOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1)
)
snaLuOperEntry.setIndexNames(
    (0, "SNA-NAU-MIB", "snaNodeAdminIndex"),
    (0, "SNA-NAU-MIB", "snaLuAdminLuIndex"),
)
if mibBuilder.loadTexts:
    snaLuOperEntry.setStatus("current")


class _SnaLuOperName_Type(DisplayString):
    """Custom type snaLuOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnaLuOperName_Type.__name__ = "DisplayString"
_SnaLuOperName_Object = MibTableColumn
snaLuOperName = _SnaLuOperName_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 1),
    _SnaLuOperName_Type()
)
snaLuOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuOperName.setStatus("current")


class _SnaLuOperSnaName_Type(DisplayString):
    """Custom type snaLuOperSnaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_SnaLuOperSnaName_Type.__name__ = "DisplayString"
_SnaLuOperSnaName_Object = MibTableColumn
snaLuOperSnaName = _SnaLuOperSnaName_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 2),
    _SnaLuOperSnaName_Type()
)
snaLuOperSnaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuOperSnaName.setStatus("current")


class _SnaLuOperType_Type(Integer32):
    """Custom type snaLuOperType based on Integer32"""
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
        *(("lu0", 2),
          ("lu1", 3),
          ("lu2", 4),
          ("lu3", 5),
          ("lu4", 6),
          ("lu62", 7),
          ("lu7", 8),
          ("other", 1))
    )


_SnaLuOperType_Type.__name__ = "Integer32"
_SnaLuOperType_Object = MibTableColumn
snaLuOperType = _SnaLuOperType_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 3),
    _SnaLuOperType_Type()
)
snaLuOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuOperType.setStatus("current")


class _SnaLuOperDepType_Type(Integer32):
    """Custom type snaLuOperDepType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dependent", 1),
          ("independent", 2))
    )


_SnaLuOperDepType_Type.__name__ = "Integer32"
_SnaLuOperDepType_Object = MibTableColumn
snaLuOperDepType = _SnaLuOperDepType_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 4),
    _SnaLuOperDepType_Type()
)
snaLuOperDepType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuOperDepType.setStatus("current")


class _SnaLuOperLocalAddress_Type(OctetString):
    """Custom type snaLuOperLocalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SnaLuOperLocalAddress_Type.__name__ = "OctetString"
_SnaLuOperLocalAddress_Object = MibTableColumn
snaLuOperLocalAddress = _SnaLuOperLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 5),
    _SnaLuOperLocalAddress_Type()
)
snaLuOperLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuOperLocalAddress.setStatus("current")


class _SnaLuOperDisplayModel_Type(Integer32):
    """Custom type snaLuOperDisplayModel based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 10),
          ("invalid", 1),
          ("model2A", 2),
          ("model2B", 3),
          ("model3A", 4),
          ("model3B", 5),
          ("model4A", 6),
          ("model4B", 7),
          ("model5A", 8),
          ("model5B", 9))
    )


_SnaLuOperDisplayModel_Type.__name__ = "Integer32"
_SnaLuOperDisplayModel_Object = MibTableColumn
snaLuOperDisplayModel = _SnaLuOperDisplayModel_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 6),
    _SnaLuOperDisplayModel_Type()
)
snaLuOperDisplayModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuOperDisplayModel.setStatus("current")


class _SnaLuOperTerm_Type(Integer32):
    """Custom type snaLuOperTerm based on Integer32"""
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
        *(("poweroff", 4),
          ("rshutd", 3),
          ("termself", 2),
          ("unbind", 1))
    )


_SnaLuOperTerm_Type.__name__ = "Integer32"
_SnaLuOperTerm_Object = MibTableColumn
snaLuOperTerm = _SnaLuOperTerm_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 7),
    _SnaLuOperTerm_Type()
)
snaLuOperTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuOperTerm.setStatus("current")


class _SnaLuOperState_Type(Integer32):
    """Custom type snaLuOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_SnaLuOperState_Type.__name__ = "Integer32"
_SnaLuOperState_Object = MibTableColumn
snaLuOperState = _SnaLuOperState_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 8),
    _SnaLuOperState_Type()
)
snaLuOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuOperState.setStatus("current")
_SnaLuOperSessnCount_Type = Gauge32
_SnaLuOperSessnCount_Object = MibTableColumn
snaLuOperSessnCount = _SnaLuOperSessnCount_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 2, 1, 9),
    _SnaLuOperSessnCount_Type()
)
snaLuOperSessnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuOperSessnCount.setStatus("current")
_SnaLuSessnTable_Object = MibTable
snaLuSessnTable = _SnaLuSessnTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3)
)
if mibBuilder.loadTexts:
    snaLuSessnTable.setStatus("current")
_SnaLuSessnEntry_Object = MibTableRow
snaLuSessnEntry = _SnaLuSessnEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1)
)
snaLuSessnEntry.setIndexNames(
    (0, "SNA-NAU-MIB", "snaNodeAdminIndex"),
    (0, "SNA-NAU-MIB", "snaLuAdminLuIndex"),
    (0, "SNA-NAU-MIB", "snaLuSessnRluIndex"),
    (0, "SNA-NAU-MIB", "snaLuSessnIndex"),
)
if mibBuilder.loadTexts:
    snaLuSessnEntry.setStatus("current")
_SnaLuSessnRluIndex_Type = Integer32
_SnaLuSessnRluIndex_Object = MibTableColumn
snaLuSessnRluIndex = _SnaLuSessnRluIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 1),
    _SnaLuSessnRluIndex_Type()
)
snaLuSessnRluIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnRluIndex.setStatus("current")
_SnaLuSessnIndex_Type = Integer32
_SnaLuSessnIndex_Object = MibTableColumn
snaLuSessnIndex = _SnaLuSessnIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 2),
    _SnaLuSessnIndex_Type()
)
snaLuSessnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnIndex.setStatus("current")


class _SnaLuSessnLocalApplName_Type(DisplayString):
    """Custom type snaLuSessnLocalApplName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnaLuSessnLocalApplName_Type.__name__ = "DisplayString"
_SnaLuSessnLocalApplName_Object = MibTableColumn
snaLuSessnLocalApplName = _SnaLuSessnLocalApplName_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 3),
    _SnaLuSessnLocalApplName_Type()
)
snaLuSessnLocalApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnLocalApplName.setStatus("current")


class _SnaLuSessnRemoteLuName_Type(DisplayString):
    """Custom type snaLuSessnRemoteLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SnaLuSessnRemoteLuName_Type.__name__ = "DisplayString"
_SnaLuSessnRemoteLuName_Object = MibTableColumn
snaLuSessnRemoteLuName = _SnaLuSessnRemoteLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 4),
    _SnaLuSessnRemoteLuName_Type()
)
snaLuSessnRemoteLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnRemoteLuName.setStatus("current")


class _SnaLuSessnMaxSndRuSize_Type(Integer32):
    """Custom type snaLuSessnMaxSndRuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_SnaLuSessnMaxSndRuSize_Type.__name__ = "Integer32"
_SnaLuSessnMaxSndRuSize_Object = MibTableColumn
snaLuSessnMaxSndRuSize = _SnaLuSessnMaxSndRuSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 5),
    _SnaLuSessnMaxSndRuSize_Type()
)
snaLuSessnMaxSndRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnMaxSndRuSize.setStatus("current")


class _SnaLuSessnMaxRcvRuSize_Type(Integer32):
    """Custom type snaLuSessnMaxRcvRuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_SnaLuSessnMaxRcvRuSize_Type.__name__ = "Integer32"
_SnaLuSessnMaxRcvRuSize_Object = MibTableColumn
snaLuSessnMaxRcvRuSize = _SnaLuSessnMaxRcvRuSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 6),
    _SnaLuSessnMaxRcvRuSize_Type()
)
snaLuSessnMaxRcvRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnMaxRcvRuSize.setStatus("current")


class _SnaLuSessnSndPacingSize_Type(Integer32):
    """Custom type snaLuSessnSndPacingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SnaLuSessnSndPacingSize_Type.__name__ = "Integer32"
_SnaLuSessnSndPacingSize_Object = MibTableColumn
snaLuSessnSndPacingSize = _SnaLuSessnSndPacingSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 7),
    _SnaLuSessnSndPacingSize_Type()
)
snaLuSessnSndPacingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnSndPacingSize.setStatus("current")


class _SnaLuSessnRcvPacingSize_Type(Integer32):
    """Custom type snaLuSessnRcvPacingSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SnaLuSessnRcvPacingSize_Type.__name__ = "Integer32"
_SnaLuSessnRcvPacingSize_Object = MibTableColumn
snaLuSessnRcvPacingSize = _SnaLuSessnRcvPacingSize_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 8),
    _SnaLuSessnRcvPacingSize_Type()
)
snaLuSessnRcvPacingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnRcvPacingSize.setStatus("current")
_SnaLuSessnActiveTime_Type = TimeStamp
_SnaLuSessnActiveTime_Object = MibTableColumn
snaLuSessnActiveTime = _SnaLuSessnActiveTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 9),
    _SnaLuSessnActiveTime_Type()
)
snaLuSessnActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnActiveTime.setStatus("current")


class _SnaLuSessnAdminState_Type(Integer32):
    """Custom type snaLuSessnAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bound", 3),
          ("unbound", 1))
    )


_SnaLuSessnAdminState_Type.__name__ = "Integer32"
_SnaLuSessnAdminState_Object = MibTableColumn
snaLuSessnAdminState = _SnaLuSessnAdminState_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 10),
    _SnaLuSessnAdminState_Type()
)
snaLuSessnAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snaLuSessnAdminState.setStatus("current")


class _SnaLuSessnOperState_Type(Integer32):
    """Custom type snaLuSessnOperState based on Integer32"""
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
        *(("bound", 3),
          ("pendingBind", 2),
          ("pendingUnbind", 4),
          ("unbound", 1))
    )


_SnaLuSessnOperState_Type.__name__ = "Integer32"
_SnaLuSessnOperState_Object = MibTableColumn
snaLuSessnOperState = _SnaLuSessnOperState_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 11),
    _SnaLuSessnOperState_Type()
)
snaLuSessnOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnOperState.setStatus("current")


class _SnaLuSessnSenseData_Type(OctetString):
    """Custom type snaLuSessnSenseData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SnaLuSessnSenseData_Type.__name__ = "OctetString"
_SnaLuSessnSenseData_Object = MibTableColumn
snaLuSessnSenseData = _SnaLuSessnSenseData_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 12),
    _SnaLuSessnSenseData_Type()
)
snaLuSessnSenseData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnSenseData.setStatus("current")


class _SnaLuSessnTerminationRu_Type(Integer32):
    """Custom type snaLuSessnTerminationRu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bindFailure", 2),
          ("other", 1),
          ("unbind", 3))
    )


_SnaLuSessnTerminationRu_Type.__name__ = "Integer32"
_SnaLuSessnTerminationRu_Object = MibTableColumn
snaLuSessnTerminationRu = _SnaLuSessnTerminationRu_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 13),
    _SnaLuSessnTerminationRu_Type()
)
snaLuSessnTerminationRu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnTerminationRu.setStatus("current")


class _SnaLuSessnUnbindType_Type(OctetString):
    """Custom type snaLuSessnUnbindType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_SnaLuSessnUnbindType_Type.__name__ = "OctetString"
_SnaLuSessnUnbindType_Object = MibTableColumn
snaLuSessnUnbindType = _SnaLuSessnUnbindType_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 14),
    _SnaLuSessnUnbindType_Type()
)
snaLuSessnUnbindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnUnbindType.setStatus("current")
_SnaLuSessnLinkIndex_Type = Integer32
_SnaLuSessnLinkIndex_Object = MibTableColumn
snaLuSessnLinkIndex = _SnaLuSessnLinkIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 3, 1, 15),
    _SnaLuSessnLinkIndex_Type()
)
snaLuSessnLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnLinkIndex.setStatus("current")
_SnaLuSessnStatsTable_Object = MibTable
snaLuSessnStatsTable = _SnaLuSessnStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 4)
)
if mibBuilder.loadTexts:
    snaLuSessnStatsTable.setStatus("current")
_SnaLuSessnStatsEntry_Object = MibTableRow
snaLuSessnStatsEntry = _SnaLuSessnStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1)
)
snaLuSessnStatsEntry.setIndexNames(
    (0, "SNA-NAU-MIB", "snaNodeAdminIndex"),
    (0, "SNA-NAU-MIB", "snaLuAdminLuIndex"),
    (0, "SNA-NAU-MIB", "snaLuSessnRluIndex"),
    (0, "SNA-NAU-MIB", "snaLuSessnIndex"),
)
if mibBuilder.loadTexts:
    snaLuSessnStatsEntry.setStatus("current")
_SnaLuSessnStatsSentBytes_Type = Counter32
_SnaLuSessnStatsSentBytes_Object = MibTableColumn
snaLuSessnStatsSentBytes = _SnaLuSessnStatsSentBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 1),
    _SnaLuSessnStatsSentBytes_Type()
)
snaLuSessnStatsSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnStatsSentBytes.setStatus("current")
_SnaLuSessnStatsReceivedBytes_Type = Counter32
_SnaLuSessnStatsReceivedBytes_Object = MibTableColumn
snaLuSessnStatsReceivedBytes = _SnaLuSessnStatsReceivedBytes_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 2),
    _SnaLuSessnStatsReceivedBytes_Type()
)
snaLuSessnStatsReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnStatsReceivedBytes.setStatus("current")
_SnaLuSessnStatsSentRus_Type = Counter32
_SnaLuSessnStatsSentRus_Object = MibTableColumn
snaLuSessnStatsSentRus = _SnaLuSessnStatsSentRus_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 3),
    _SnaLuSessnStatsSentRus_Type()
)
snaLuSessnStatsSentRus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnStatsSentRus.setStatus("current")
_SnaLuSessnStatsReceivedRus_Type = Counter32
_SnaLuSessnStatsReceivedRus_Object = MibTableColumn
snaLuSessnStatsReceivedRus = _SnaLuSessnStatsReceivedRus_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 4),
    _SnaLuSessnStatsReceivedRus_Type()
)
snaLuSessnStatsReceivedRus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnStatsReceivedRus.setStatus("current")
_SnaLuSessnStatsSentNegativeResps_Type = Counter32
_SnaLuSessnStatsSentNegativeResps_Object = MibTableColumn
snaLuSessnStatsSentNegativeResps = _SnaLuSessnStatsSentNegativeResps_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 5),
    _SnaLuSessnStatsSentNegativeResps_Type()
)
snaLuSessnStatsSentNegativeResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnStatsSentNegativeResps.setStatus("current")
_SnaLuSessnStatsReceivedNegativeResps_Type = Counter32
_SnaLuSessnStatsReceivedNegativeResps_Object = MibTableColumn
snaLuSessnStatsReceivedNegativeResps = _SnaLuSessnStatsReceivedNegativeResps_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 4, 1, 6),
    _SnaLuSessnStatsReceivedNegativeResps_Type()
)
snaLuSessnStatsReceivedNegativeResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuSessnStatsReceivedNegativeResps.setStatus("current")
_SnaLuTraps_ObjectIdentity = ObjectIdentity
snaLuTraps = _SnaLuTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 5)
)
_SnaMgtTools_ObjectIdentity = ObjectIdentity
snaMgtTools = _SnaMgtTools_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 1, 3)
)
_SnaLuRtmTable_Object = MibTable
snaLuRtmTable = _SnaLuRtmTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1)
)
if mibBuilder.loadTexts:
    snaLuRtmTable.setStatus("current")
_SnaLuRtmEntry_Object = MibTableRow
snaLuRtmEntry = _SnaLuRtmEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1)
)
snaLuRtmEntry.setIndexNames(
    (0, "SNA-NAU-MIB", "snaLuRtmPuIndex"),
    (0, "SNA-NAU-MIB", "snaLuRtmLuIndex"),
)
if mibBuilder.loadTexts:
    snaLuRtmEntry.setStatus("current")
_SnaLuRtmPuIndex_Type = Integer32
_SnaLuRtmPuIndex_Object = MibTableColumn
snaLuRtmPuIndex = _SnaLuRtmPuIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 1),
    _SnaLuRtmPuIndex_Type()
)
snaLuRtmPuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snaLuRtmPuIndex.setStatus("current")
_SnaLuRtmLuIndex_Type = Integer32
_SnaLuRtmLuIndex_Object = MibTableColumn
snaLuRtmLuIndex = _SnaLuRtmLuIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 2),
    _SnaLuRtmLuIndex_Type()
)
snaLuRtmLuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snaLuRtmLuIndex.setStatus("current")


class _SnaLuRtmState_Type(Integer32):
    """Custom type snaLuRtmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SnaLuRtmState_Type.__name__ = "Integer32"
_SnaLuRtmState_Object = MibTableColumn
snaLuRtmState = _SnaLuRtmState_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 3),
    _SnaLuRtmState_Type()
)
snaLuRtmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmState.setStatus("current")
_SnaLuRtmStateTime_Type = TimeStamp
_SnaLuRtmStateTime_Object = MibTableColumn
snaLuRtmStateTime = _SnaLuRtmStateTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 4),
    _SnaLuRtmStateTime_Type()
)
snaLuRtmStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmStateTime.setStatus("current")


class _SnaLuRtmDef_Type(Integer32):
    """Custom type snaLuRtmDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cdeb", 3),
          ("firstChar", 1),
          ("kb", 2))
    )


_SnaLuRtmDef_Type.__name__ = "Integer32"
_SnaLuRtmDef_Object = MibTableColumn
snaLuRtmDef = _SnaLuRtmDef_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 5),
    _SnaLuRtmDef_Type()
)
snaLuRtmDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmDef.setStatus("current")
_SnaLuRtmBoundary1_Type = Integer32
_SnaLuRtmBoundary1_Object = MibTableColumn
snaLuRtmBoundary1 = _SnaLuRtmBoundary1_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 6),
    _SnaLuRtmBoundary1_Type()
)
snaLuRtmBoundary1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmBoundary1.setStatus("current")
_SnaLuRtmBoundary2_Type = Integer32
_SnaLuRtmBoundary2_Object = MibTableColumn
snaLuRtmBoundary2 = _SnaLuRtmBoundary2_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 7),
    _SnaLuRtmBoundary2_Type()
)
snaLuRtmBoundary2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmBoundary2.setStatus("current")
_SnaLuRtmBoundary3_Type = Integer32
_SnaLuRtmBoundary3_Object = MibTableColumn
snaLuRtmBoundary3 = _SnaLuRtmBoundary3_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 8),
    _SnaLuRtmBoundary3_Type()
)
snaLuRtmBoundary3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmBoundary3.setStatus("current")
_SnaLuRtmBoundary4_Type = Integer32
_SnaLuRtmBoundary4_Object = MibTableColumn
snaLuRtmBoundary4 = _SnaLuRtmBoundary4_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 9),
    _SnaLuRtmBoundary4_Type()
)
snaLuRtmBoundary4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmBoundary4.setStatus("current")
_SnaLuRtmCounter1_Type = Counter32
_SnaLuRtmCounter1_Object = MibTableColumn
snaLuRtmCounter1 = _SnaLuRtmCounter1_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 10),
    _SnaLuRtmCounter1_Type()
)
snaLuRtmCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmCounter1.setStatus("current")
_SnaLuRtmCounter2_Type = Counter32
_SnaLuRtmCounter2_Object = MibTableColumn
snaLuRtmCounter2 = _SnaLuRtmCounter2_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 11),
    _SnaLuRtmCounter2_Type()
)
snaLuRtmCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmCounter2.setStatus("current")
_SnaLuRtmCounter3_Type = Counter32
_SnaLuRtmCounter3_Object = MibTableColumn
snaLuRtmCounter3 = _SnaLuRtmCounter3_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 12),
    _SnaLuRtmCounter3_Type()
)
snaLuRtmCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmCounter3.setStatus("current")
_SnaLuRtmCounter4_Type = Counter32
_SnaLuRtmCounter4_Object = MibTableColumn
snaLuRtmCounter4 = _SnaLuRtmCounter4_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 13),
    _SnaLuRtmCounter4_Type()
)
snaLuRtmCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmCounter4.setStatus("current")
_SnaLuRtmOverFlows_Type = Counter32
_SnaLuRtmOverFlows_Object = MibTableColumn
snaLuRtmOverFlows = _SnaLuRtmOverFlows_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 14),
    _SnaLuRtmOverFlows_Type()
)
snaLuRtmOverFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmOverFlows.setStatus("current")
_SnaLuRtmObjPercent_Type = Integer32
_SnaLuRtmObjPercent_Object = MibTableColumn
snaLuRtmObjPercent = _SnaLuRtmObjPercent_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 15),
    _SnaLuRtmObjPercent_Type()
)
snaLuRtmObjPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmObjPercent.setStatus("current")


class _SnaLuRtmObjRange_Type(Integer32):
    """Custom type snaLuRtmObjRange based on Integer32"""
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
        *(("other", 1),
          ("range1", 2),
          ("range2", 3),
          ("range3", 4),
          ("range4", 5),
          ("range5", 6))
    )


_SnaLuRtmObjRange_Type.__name__ = "Integer32"
_SnaLuRtmObjRange_Object = MibTableColumn
snaLuRtmObjRange = _SnaLuRtmObjRange_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 16),
    _SnaLuRtmObjRange_Type()
)
snaLuRtmObjRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmObjRange.setStatus("current")
_SnaLuRtmNumTrans_Type = Integer32
_SnaLuRtmNumTrans_Object = MibTableColumn
snaLuRtmNumTrans = _SnaLuRtmNumTrans_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 17),
    _SnaLuRtmNumTrans_Type()
)
snaLuRtmNumTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmNumTrans.setStatus("current")
_SnaLuRtmLastRspTime_Type = Integer32
_SnaLuRtmLastRspTime_Object = MibTableColumn
snaLuRtmLastRspTime = _SnaLuRtmLastRspTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 18),
    _SnaLuRtmLastRspTime_Type()
)
snaLuRtmLastRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmLastRspTime.setStatus("current")
_SnaLuRtmAvgRspTime_Type = Integer32
_SnaLuRtmAvgRspTime_Object = MibTableColumn
snaLuRtmAvgRspTime = _SnaLuRtmAvgRspTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 1, 3, 1, 1, 19),
    _SnaLuRtmAvgRspTime_Type()
)
snaLuRtmAvgRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snaLuRtmAvgRspTime.setStatus("current")
_SnanauConformance_ObjectIdentity = ObjectIdentity
snanauConformance = _SnanauConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 2)
)
_SnanauCompliances_ObjectIdentity = ObjectIdentity
snanauCompliances = _SnanauCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 2, 1)
)
_SnanauGroups_ObjectIdentity = ObjectIdentity
snanauGroups = _SnanauGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 2, 2)
)

# Managed Objects groups

snaNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 2, 2, 1)
)
snaNodeGroup.setObjects(
      *(("SNA-NAU-MIB", "snaNodeAdminName"),
        ("SNA-NAU-MIB", "snaNodeAdminType"),
        ("SNA-NAU-MIB", "snaNodeAdminXidFormat"),
        ("SNA-NAU-MIB", "snaNodeAdminBlockNum"),
        ("SNA-NAU-MIB", "snaNodeAdminIdNum"),
        ("SNA-NAU-MIB", "snaNodeAdminEnablingMethod"),
        ("SNA-NAU-MIB", "snaNodeAdminLuTermDefault"),
        ("SNA-NAU-MIB", "snaNodeAdminMaxLu"),
        ("SNA-NAU-MIB", "snaNodeAdminHostDescription"),
        ("SNA-NAU-MIB", "snaNodeAdminStopMethod"),
        ("SNA-NAU-MIB", "snaNodeAdminState"),
        ("SNA-NAU-MIB", "snaNodeAdminRowStatus"),
        ("SNA-NAU-MIB", "snaNodeAdminTableLastChange"),
        ("SNA-NAU-MIB", "snaNodeOperName"),
        ("SNA-NAU-MIB", "snaNodeOperType"),
        ("SNA-NAU-MIB", "snaNodeOperXidFormat"),
        ("SNA-NAU-MIB", "snaNodeOperBlockNum"),
        ("SNA-NAU-MIB", "snaNodeOperIdNum"),
        ("SNA-NAU-MIB", "snaNodeOperEnablingMethod"),
        ("SNA-NAU-MIB", "snaNodeOperLuTermDefault"),
        ("SNA-NAU-MIB", "snaNodeOperMaxLu"),
        ("SNA-NAU-MIB", "snaNodeOperHostDescription"),
        ("SNA-NAU-MIB", "snaNodeOperStopMethod"),
        ("SNA-NAU-MIB", "snaNodeOperState"),
        ("SNA-NAU-MIB", "snaNodeOperHostSscpId"),
        ("SNA-NAU-MIB", "snaNodeOperStartTime"),
        ("SNA-NAU-MIB", "snaNodeOperLastStateChange"),
        ("SNA-NAU-MIB", "snaNodeOperActFailures"),
        ("SNA-NAU-MIB", "snaNodeOperActFailureReason"),
        ("SNA-NAU-MIB", "snaNodeOperTableLastChange"),
        ("SNA-NAU-MIB", "snaNodeLinkAdminSpecific"),
        ("SNA-NAU-MIB", "snaNodeLinkAdminMaxPiu"),
        ("SNA-NAU-MIB", "snaNodeLinkAdminRowStatus"),
        ("SNA-NAU-MIB", "snaNodeLinkAdminTableLastChange"),
        ("SNA-NAU-MIB", "snaNodeLinkOperSpecific"),
        ("SNA-NAU-MIB", "snaNodeLinkOperMaxPiu"),
        ("SNA-NAU-MIB", "snaNodeLinkOperTableLastChange"))
)
if mibBuilder.loadTexts:
    snaNodeGroup.setStatus("current")

snaLuGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 2, 2, 2)
)
snaLuGroup.setObjects(
      *(("SNA-NAU-MIB", "snaLuAdminName"),
        ("SNA-NAU-MIB", "snaLuAdminSnaName"),
        ("SNA-NAU-MIB", "snaLuAdminType"),
        ("SNA-NAU-MIB", "snaLuAdminDepType"),
        ("SNA-NAU-MIB", "snaLuAdminLocalAddress"),
        ("SNA-NAU-MIB", "snaLuAdminDisplayModel"),
        ("SNA-NAU-MIB", "snaLuAdminTerm"),
        ("SNA-NAU-MIB", "snaLuAdminRowStatus"),
        ("SNA-NAU-MIB", "snaLuOperName"),
        ("SNA-NAU-MIB", "snaLuOperSnaName"),
        ("SNA-NAU-MIB", "snaLuOperType"),
        ("SNA-NAU-MIB", "snaLuOperDepType"),
        ("SNA-NAU-MIB", "snaLuOperLocalAddress"),
        ("SNA-NAU-MIB", "snaLuOperDisplayModel"),
        ("SNA-NAU-MIB", "snaLuOperTerm"),
        ("SNA-NAU-MIB", "snaLuOperState"),
        ("SNA-NAU-MIB", "snaLuOperSessnCount"))
)
if mibBuilder.loadTexts:
    snaLuGroup.setStatus("current")

snaSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 2, 2, 3)
)
snaSessionGroup.setObjects(
      *(("SNA-NAU-MIB", "snaLuSessnRluIndex"),
        ("SNA-NAU-MIB", "snaLuSessnIndex"),
        ("SNA-NAU-MIB", "snaLuSessnLocalApplName"),
        ("SNA-NAU-MIB", "snaLuSessnRemoteLuName"),
        ("SNA-NAU-MIB", "snaLuSessnMaxSndRuSize"),
        ("SNA-NAU-MIB", "snaLuSessnMaxRcvRuSize"),
        ("SNA-NAU-MIB", "snaLuSessnSndPacingSize"),
        ("SNA-NAU-MIB", "snaLuSessnRcvPacingSize"),
        ("SNA-NAU-MIB", "snaLuSessnActiveTime"),
        ("SNA-NAU-MIB", "snaLuSessnAdminState"),
        ("SNA-NAU-MIB", "snaLuSessnOperState"),
        ("SNA-NAU-MIB", "snaLuSessnSenseData"),
        ("SNA-NAU-MIB", "snaLuSessnTerminationRu"),
        ("SNA-NAU-MIB", "snaLuSessnUnbindType"),
        ("SNA-NAU-MIB", "snaLuSessnLinkIndex"),
        ("SNA-NAU-MIB", "snaLuSessnStatsSentBytes"),
        ("SNA-NAU-MIB", "snaLuSessnStatsReceivedBytes"),
        ("SNA-NAU-MIB", "snaLuSessnStatsSentRus"),
        ("SNA-NAU-MIB", "snaLuSessnStatsReceivedRus"),
        ("SNA-NAU-MIB", "snaLuSessnStatsSentNegativeResps"),
        ("SNA-NAU-MIB", "snaLuSessnStatsReceivedNegativeResps"))
)
if mibBuilder.loadTexts:
    snaSessionGroup.setStatus("current")

snaPu20Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 2, 2, 4)
)
snaPu20Group.setObjects(
      *(("SNA-NAU-MIB", "snaPu20StatsSentBytes"),
        ("SNA-NAU-MIB", "snaPu20StatsReceivedBytes"),
        ("SNA-NAU-MIB", "snaPu20StatsSentPius"),
        ("SNA-NAU-MIB", "snaPu20StatsReceivedPius"),
        ("SNA-NAU-MIB", "snaPu20StatsSentNegativeResps"),
        ("SNA-NAU-MIB", "snaPu20StatsReceivedNegativeResps"),
        ("SNA-NAU-MIB", "snaPu20StatsActLus"),
        ("SNA-NAU-MIB", "snaPu20StatsInActLus"),
        ("SNA-NAU-MIB", "snaPu20StatsBindLus"))
)
if mibBuilder.loadTexts:
    snaPu20Group.setStatus("current")

snaMgtToolsRtmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 2, 2, 5)
)
snaMgtToolsRtmGroup.setObjects(
      *(("SNA-NAU-MIB", "snaLuRtmState"),
        ("SNA-NAU-MIB", "snaLuRtmStateTime"),
        ("SNA-NAU-MIB", "snaLuRtmDef"),
        ("SNA-NAU-MIB", "snaLuRtmBoundary1"),
        ("SNA-NAU-MIB", "snaLuRtmBoundary2"),
        ("SNA-NAU-MIB", "snaLuRtmBoundary3"),
        ("SNA-NAU-MIB", "snaLuRtmBoundary4"),
        ("SNA-NAU-MIB", "snaLuRtmCounter1"),
        ("SNA-NAU-MIB", "snaLuRtmCounter2"),
        ("SNA-NAU-MIB", "snaLuRtmCounter3"),
        ("SNA-NAU-MIB", "snaLuRtmCounter4"),
        ("SNA-NAU-MIB", "snaLuRtmOverFlows"),
        ("SNA-NAU-MIB", "snaLuRtmObjPercent"),
        ("SNA-NAU-MIB", "snaLuRtmObjRange"),
        ("SNA-NAU-MIB", "snaLuRtmNumTrans"),
        ("SNA-NAU-MIB", "snaLuRtmLastRspTime"),
        ("SNA-NAU-MIB", "snaLuRtmAvgRspTime"))
)
if mibBuilder.loadTexts:
    snaMgtToolsRtmGroup.setStatus("current")


# Notification objects

snaNodeStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 10, 1)
)
snaNodeStateChangeTrap.setObjects(
      *(("SNA-NAU-MIB", "snaNodeOperName"),
        ("SNA-NAU-MIB", "snaNodeOperState"))
)
if mibBuilder.loadTexts:
    snaNodeStateChangeTrap.setStatus(
        "current"
    )

snaNodeActFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 1, 1, 10, 2)
)
snaNodeActFailTrap.setObjects(
      *(("SNA-NAU-MIB", "snaNodeOperName"),
        ("SNA-NAU-MIB", "snaNodeOperState"),
        ("SNA-NAU-MIB", "snaNodeOperActFailureReason"))
)
if mibBuilder.loadTexts:
    snaNodeActFailTrap.setStatus(
        "current"
    )

snaLuStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 5, 1)
)
snaLuStateChangeTrap.setObjects(
      *(("SNA-NAU-MIB", "snaLuOperName"),
        ("SNA-NAU-MIB", "snaLuOperSnaName"),
        ("SNA-NAU-MIB", "snaLuOperState"))
)
if mibBuilder.loadTexts:
    snaLuStateChangeTrap.setStatus(
        "current"
    )

snaLuSessnBindFailTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 1, 2, 5, 2)
)
snaLuSessnBindFailTrap.setObjects(
      *(("SNA-NAU-MIB", "snaLuSessnLocalApplName"),
        ("SNA-NAU-MIB", "snaLuSessnRemoteLuName"),
        ("SNA-NAU-MIB", "snaLuSessnOperState"),
        ("SNA-NAU-MIB", "snaLuSessnSenseData"))
)
if mibBuilder.loadTexts:
    snaLuSessnBindFailTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

snanauCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 2, 1, 1)
)
if mibBuilder.loadTexts:
    snanauCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNA-NAU-MIB",
    **{"snanauMIB": snanauMIB,
       "snanauObjects": snanauObjects,
       "snaNode": snaNode,
       "snaNodeAdminTable": snaNodeAdminTable,
       "snaNodeAdminEntry": snaNodeAdminEntry,
       "snaNodeAdminIndex": snaNodeAdminIndex,
       "snaNodeAdminName": snaNodeAdminName,
       "snaNodeAdminType": snaNodeAdminType,
       "snaNodeAdminXidFormat": snaNodeAdminXidFormat,
       "snaNodeAdminBlockNum": snaNodeAdminBlockNum,
       "snaNodeAdminIdNum": snaNodeAdminIdNum,
       "snaNodeAdminEnablingMethod": snaNodeAdminEnablingMethod,
       "snaNodeAdminLuTermDefault": snaNodeAdminLuTermDefault,
       "snaNodeAdminMaxLu": snaNodeAdminMaxLu,
       "snaNodeAdminHostDescription": snaNodeAdminHostDescription,
       "snaNodeAdminStopMethod": snaNodeAdminStopMethod,
       "snaNodeAdminState": snaNodeAdminState,
       "snaNodeAdminRowStatus": snaNodeAdminRowStatus,
       "snaNodeAdminTableLastChange": snaNodeAdminTableLastChange,
       "snaNodeOperTable": snaNodeOperTable,
       "snaNodeOperEntry": snaNodeOperEntry,
       "snaNodeOperName": snaNodeOperName,
       "snaNodeOperType": snaNodeOperType,
       "snaNodeOperXidFormat": snaNodeOperXidFormat,
       "snaNodeOperBlockNum": snaNodeOperBlockNum,
       "snaNodeOperIdNum": snaNodeOperIdNum,
       "snaNodeOperEnablingMethod": snaNodeOperEnablingMethod,
       "snaNodeOperLuTermDefault": snaNodeOperLuTermDefault,
       "snaNodeOperMaxLu": snaNodeOperMaxLu,
       "snaNodeOperHostDescription": snaNodeOperHostDescription,
       "snaNodeOperStopMethod": snaNodeOperStopMethod,
       "snaNodeOperState": snaNodeOperState,
       "snaNodeOperHostSscpId": snaNodeOperHostSscpId,
       "snaNodeOperStartTime": snaNodeOperStartTime,
       "snaNodeOperLastStateChange": snaNodeOperLastStateChange,
       "snaNodeOperActFailures": snaNodeOperActFailures,
       "snaNodeOperActFailureReason": snaNodeOperActFailureReason,
       "snaNodeOperTableLastChange": snaNodeOperTableLastChange,
       "snaPu20StatsTable": snaPu20StatsTable,
       "snaPu20StatsEntry": snaPu20StatsEntry,
       "snaPu20StatsSentBytes": snaPu20StatsSentBytes,
       "snaPu20StatsReceivedBytes": snaPu20StatsReceivedBytes,
       "snaPu20StatsSentPius": snaPu20StatsSentPius,
       "snaPu20StatsReceivedPius": snaPu20StatsReceivedPius,
       "snaPu20StatsSentNegativeResps": snaPu20StatsSentNegativeResps,
       "snaPu20StatsReceivedNegativeResps": snaPu20StatsReceivedNegativeResps,
       "snaPu20StatsActLus": snaPu20StatsActLus,
       "snaPu20StatsInActLus": snaPu20StatsInActLus,
       "snaPu20StatsBindLus": snaPu20StatsBindLus,
       "snaNodeLinkAdminTable": snaNodeLinkAdminTable,
       "snaNodeLinkAdminEntry": snaNodeLinkAdminEntry,
       "snaNodeLinkAdminIndex": snaNodeLinkAdminIndex,
       "snaNodeLinkAdminSpecific": snaNodeLinkAdminSpecific,
       "snaNodeLinkAdminMaxPiu": snaNodeLinkAdminMaxPiu,
       "snaNodeLinkAdminRowStatus": snaNodeLinkAdminRowStatus,
       "snaNodeLinkAdminTableLastChange": snaNodeLinkAdminTableLastChange,
       "snaNodeLinkOperTable": snaNodeLinkOperTable,
       "snaNodeLinkOperEntry": snaNodeLinkOperEntry,
       "snaNodeLinkOperSpecific": snaNodeLinkOperSpecific,
       "snaNodeLinkOperMaxPiu": snaNodeLinkOperMaxPiu,
       "snaNodeLinkOperTableLastChange": snaNodeLinkOperTableLastChange,
       "snaNodeTraps": snaNodeTraps,
       "snaNodeStateChangeTrap": snaNodeStateChangeTrap,
       "snaNodeActFailTrap": snaNodeActFailTrap,
       "snaLu": snaLu,
       "snaLuAdminTable": snaLuAdminTable,
       "snaLuAdminEntry": snaLuAdminEntry,
       "snaLuAdminLuIndex": snaLuAdminLuIndex,
       "snaLuAdminName": snaLuAdminName,
       "snaLuAdminSnaName": snaLuAdminSnaName,
       "snaLuAdminType": snaLuAdminType,
       "snaLuAdminDepType": snaLuAdminDepType,
       "snaLuAdminLocalAddress": snaLuAdminLocalAddress,
       "snaLuAdminDisplayModel": snaLuAdminDisplayModel,
       "snaLuAdminTerm": snaLuAdminTerm,
       "snaLuAdminRowStatus": snaLuAdminRowStatus,
       "snaLuOperTable": snaLuOperTable,
       "snaLuOperEntry": snaLuOperEntry,
       "snaLuOperName": snaLuOperName,
       "snaLuOperSnaName": snaLuOperSnaName,
       "snaLuOperType": snaLuOperType,
       "snaLuOperDepType": snaLuOperDepType,
       "snaLuOperLocalAddress": snaLuOperLocalAddress,
       "snaLuOperDisplayModel": snaLuOperDisplayModel,
       "snaLuOperTerm": snaLuOperTerm,
       "snaLuOperState": snaLuOperState,
       "snaLuOperSessnCount": snaLuOperSessnCount,
       "snaLuSessnTable": snaLuSessnTable,
       "snaLuSessnEntry": snaLuSessnEntry,
       "snaLuSessnRluIndex": snaLuSessnRluIndex,
       "snaLuSessnIndex": snaLuSessnIndex,
       "snaLuSessnLocalApplName": snaLuSessnLocalApplName,
       "snaLuSessnRemoteLuName": snaLuSessnRemoteLuName,
       "snaLuSessnMaxSndRuSize": snaLuSessnMaxSndRuSize,
       "snaLuSessnMaxRcvRuSize": snaLuSessnMaxRcvRuSize,
       "snaLuSessnSndPacingSize": snaLuSessnSndPacingSize,
       "snaLuSessnRcvPacingSize": snaLuSessnRcvPacingSize,
       "snaLuSessnActiveTime": snaLuSessnActiveTime,
       "snaLuSessnAdminState": snaLuSessnAdminState,
       "snaLuSessnOperState": snaLuSessnOperState,
       "snaLuSessnSenseData": snaLuSessnSenseData,
       "snaLuSessnTerminationRu": snaLuSessnTerminationRu,
       "snaLuSessnUnbindType": snaLuSessnUnbindType,
       "snaLuSessnLinkIndex": snaLuSessnLinkIndex,
       "snaLuSessnStatsTable": snaLuSessnStatsTable,
       "snaLuSessnStatsEntry": snaLuSessnStatsEntry,
       "snaLuSessnStatsSentBytes": snaLuSessnStatsSentBytes,
       "snaLuSessnStatsReceivedBytes": snaLuSessnStatsReceivedBytes,
       "snaLuSessnStatsSentRus": snaLuSessnStatsSentRus,
       "snaLuSessnStatsReceivedRus": snaLuSessnStatsReceivedRus,
       "snaLuSessnStatsSentNegativeResps": snaLuSessnStatsSentNegativeResps,
       "snaLuSessnStatsReceivedNegativeResps": snaLuSessnStatsReceivedNegativeResps,
       "snaLuTraps": snaLuTraps,
       "snaLuStateChangeTrap": snaLuStateChangeTrap,
       "snaLuSessnBindFailTrap": snaLuSessnBindFailTrap,
       "snaMgtTools": snaMgtTools,
       "snaLuRtmTable": snaLuRtmTable,
       "snaLuRtmEntry": snaLuRtmEntry,
       "snaLuRtmPuIndex": snaLuRtmPuIndex,
       "snaLuRtmLuIndex": snaLuRtmLuIndex,
       "snaLuRtmState": snaLuRtmState,
       "snaLuRtmStateTime": snaLuRtmStateTime,
       "snaLuRtmDef": snaLuRtmDef,
       "snaLuRtmBoundary1": snaLuRtmBoundary1,
       "snaLuRtmBoundary2": snaLuRtmBoundary2,
       "snaLuRtmBoundary3": snaLuRtmBoundary3,
       "snaLuRtmBoundary4": snaLuRtmBoundary4,
       "snaLuRtmCounter1": snaLuRtmCounter1,
       "snaLuRtmCounter2": snaLuRtmCounter2,
       "snaLuRtmCounter3": snaLuRtmCounter3,
       "snaLuRtmCounter4": snaLuRtmCounter4,
       "snaLuRtmOverFlows": snaLuRtmOverFlows,
       "snaLuRtmObjPercent": snaLuRtmObjPercent,
       "snaLuRtmObjRange": snaLuRtmObjRange,
       "snaLuRtmNumTrans": snaLuRtmNumTrans,
       "snaLuRtmLastRspTime": snaLuRtmLastRspTime,
       "snaLuRtmAvgRspTime": snaLuRtmAvgRspTime,
       "snanauConformance": snanauConformance,
       "snanauCompliances": snanauCompliances,
       "snanauCompliance": snanauCompliance,
       "snanauGroups": snanauGroups,
       "snaNodeGroup": snaNodeGroup,
       "snaLuGroup": snaLuGroup,
       "snaSessionGroup": snaSessionGroup,
       "snaPu20Group": snaPu20Group,
       "snaMgtToolsRtmGroup": snaMgtToolsRtmGroup}
)
