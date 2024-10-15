# SNMP MIB module (HP-ICF-VG-RPTR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-VG-RPTR
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:26 2024
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

(hpicfObjectModules,
 hpicfVg,
 hpicfVgRptrTrapsPrefix) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfObjectModules",
    "hpicfVg",
    "hpicfVgRptrTrapsPrefix")

(icfVgPortStatus,) = mibBuilder.importSymbols(
    "ICF-VG-RPTR",
    "icfVgPortStatus")

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

hpicfVgRptrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11)
)
hpicfVgRptrMib.setRevisions(
        ("2000-11-03 22:25",
         "1997-03-06 03:45",
         "1996-09-10 02:36",
         "1996-02-14 22:53",
         "1995-01-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfVgRptrConformance_ObjectIdentity = ObjectIdentity
hpicfVgRptrConformance = _HpicfVgRptrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1)
)
_HpicfVgRptrCompliances_ObjectIdentity = ObjectIdentity
hpicfVgRptrCompliances = _HpicfVgRptrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 1)
)
_HpicfVgRptrGroups_ObjectIdentity = ObjectIdentity
hpicfVgRptrGroups = _HpicfVgRptrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2)
)
_HpVgBasic_ObjectIdentity = ObjectIdentity
hpVgBasic = _HpVgBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1)
)
_HpVgBasicGlobal_ObjectIdentity = ObjectIdentity
hpVgBasicGlobal = _HpVgBasicGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1)
)


class _HpVgEntityName_Type(DisplayString):
    """Custom type hpVgEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpVgEntityName_Type.__name__ = "DisplayString"
_HpVgEntityName_Object = MibScalar
hpVgEntityName = _HpVgEntityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 1),
    _HpVgEntityName_Type()
)
hpVgEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgEntityName.setStatus("current")
_HpVgRedundantUpLinksFlag_Type = TruthValue
_HpVgRedundantUpLinksFlag_Object = MibScalar
hpVgRedundantUpLinksFlag = _HpVgRedundantUpLinksFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 2),
    _HpVgRedundantUpLinksFlag_Type()
)
hpVgRedundantUpLinksFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpVgRedundantUpLinksFlag.setStatus("current")
_HpVgXcvrTable_Object = MibTable
hpVgXcvrTable = _HpVgXcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpVgXcvrTable.setStatus("current")
_HpVgXcvrEntry_Object = MibTableRow
hpVgXcvrEntry = _HpVgXcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1)
)
hpVgXcvrEntry.setIndexNames(
    (0, "HP-ICF-VG-RPTR", "hpVgXcvrGroupIndex"),
    (0, "HP-ICF-VG-RPTR", "hpVgXcvrIndex"),
)
if mibBuilder.loadTexts:
    hpVgXcvrEntry.setStatus("current")


class _HpVgXcvrGroupIndex_Type(Integer32):
    """Custom type hpVgXcvrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpVgXcvrGroupIndex_Type.__name__ = "Integer32"
_HpVgXcvrGroupIndex_Object = MibTableColumn
hpVgXcvrGroupIndex = _HpVgXcvrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 1),
    _HpVgXcvrGroupIndex_Type()
)
hpVgXcvrGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVgXcvrGroupIndex.setStatus("current")


class _HpVgXcvrIndex_Type(Integer32):
    """Custom type hpVgXcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpVgXcvrIndex_Type.__name__ = "Integer32"
_HpVgXcvrIndex_Object = MibTableColumn
hpVgXcvrIndex = _HpVgXcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 2),
    _HpVgXcvrIndex_Type()
)
hpVgXcvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVgXcvrIndex.setStatus("current")


class _HpVgXcvrType_Type(Integer32):
    """Custom type hpVgXcvrType based on Integer32"""
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
        *(("fibre", 6),
          ("other", 1),
          ("pmdMissing", 3),
          ("stp2", 5),
          ("unknown", 2),
          ("utp4", 4))
    )


_HpVgXcvrType_Type.__name__ = "Integer32"
_HpVgXcvrType_Object = MibTableColumn
hpVgXcvrType = _HpVgXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 3),
    _HpVgXcvrType_Type()
)
hpVgXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgXcvrType.setStatus("current")


class _HpVgXcvrAssociatedPort_Type(Integer32):
    """Custom type hpVgXcvrAssociatedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpVgXcvrAssociatedPort_Type.__name__ = "Integer32"
_HpVgXcvrAssociatedPort_Object = MibTableColumn
hpVgXcvrAssociatedPort = _HpVgXcvrAssociatedPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 4),
    _HpVgXcvrAssociatedPort_Type()
)
hpVgXcvrAssociatedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpVgXcvrAssociatedPort.setStatus("current")


class _HpVgXcvrState_Type(Integer32):
    """Custom type hpVgXcvrState based on Integer32"""
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
        *(("inUse", 2),
          ("linkFailure", 5),
          ("silent", 4),
          ("standby", 3),
          ("unknown", 1))
    )


_HpVgXcvrState_Type.__name__ = "Integer32"
_HpVgXcvrState_Object = MibTableColumn
hpVgXcvrState = _HpVgXcvrState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 5),
    _HpVgXcvrState_Type()
)
hpVgXcvrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgXcvrState.setStatus("current")
_HpVgXcvrAbandonments_Type = Counter32
_HpVgXcvrAbandonments_Object = MibTableColumn
hpVgXcvrAbandonments = _HpVgXcvrAbandonments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 6),
    _HpVgXcvrAbandonments_Type()
)
hpVgXcvrAbandonments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgXcvrAbandonments.setStatus("current")
_HpVgXcvrIsMovable_Type = TruthValue
_HpVgXcvrIsMovable_Object = MibTableColumn
hpVgXcvrIsMovable = _HpVgXcvrIsMovable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 3, 1, 7),
    _HpVgXcvrIsMovable_Type()
)
hpVgXcvrIsMovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgXcvrIsMovable.setStatus("current")


class _HpVgNullAddrTraining_Type(Integer32):
    """Custom type hpVgNullAddrTraining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowNullAddr", 2),
          ("preventNullAddr", 1))
    )


_HpVgNullAddrTraining_Type.__name__ = "Integer32"
_HpVgNullAddrTraining_Object = MibScalar
hpVgNullAddrTraining = _HpVgNullAddrTraining_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 4),
    _HpVgNullAddrTraining_Type()
)
hpVgNullAddrTraining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpVgNullAddrTraining.setStatus("current")
_HpVgBasicGroup_ObjectIdentity = ObjectIdentity
hpVgBasicGroup = _HpVgBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2)
)
_HpVgBasicGroupTable_Object = MibTable
hpVgBasicGroupTable = _HpVgBasicGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpVgBasicGroupTable.setStatus("current")
_HpVgBasicGroupEntry_Object = MibTableRow
hpVgBasicGroupEntry = _HpVgBasicGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1)
)
hpVgBasicGroupEntry.setIndexNames(
    (0, "HP-ICF-VG-RPTR", "hpVgGrpGroupIndex"),
)
if mibBuilder.loadTexts:
    hpVgBasicGroupEntry.setStatus("current")


class _HpVgGrpGroupIndex_Type(Integer32):
    """Custom type hpVgGrpGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpVgGrpGroupIndex_Type.__name__ = "Integer32"
_HpVgGrpGroupIndex_Object = MibTableColumn
hpVgGrpGroupIndex = _HpVgGrpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 1),
    _HpVgGrpGroupIndex_Type()
)
hpVgGrpGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVgGrpGroupIndex.setStatus("current")


class _HpVgGrpPortsAdminStatus_Type(OctetString):
    """Custom type hpVgGrpPortsAdminStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpVgGrpPortsAdminStatus_Type.__name__ = "OctetString"
_HpVgGrpPortsAdminStatus_Object = MibTableColumn
hpVgGrpPortsAdminStatus = _HpVgGrpPortsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 2),
    _HpVgGrpPortsAdminStatus_Type()
)
hpVgGrpPortsAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgGrpPortsAdminStatus.setStatus("current")


class _HpVgGrpPortsTrained_Type(OctetString):
    """Custom type hpVgGrpPortsTrained based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpVgGrpPortsTrained_Type.__name__ = "OctetString"
_HpVgGrpPortsTrained_Object = MibTableColumn
hpVgGrpPortsTrained = _HpVgGrpPortsTrained_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 3),
    _HpVgGrpPortsTrained_Type()
)
hpVgGrpPortsTrained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgGrpPortsTrained.setStatus("current")


class _HpVgGrpPortsInTraining_Type(OctetString):
    """Custom type hpVgGrpPortsInTraining based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpVgGrpPortsInTraining_Type.__name__ = "OctetString"
_HpVgGrpPortsInTraining_Object = MibTableColumn
hpVgGrpPortsInTraining = _HpVgGrpPortsInTraining_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 4),
    _HpVgGrpPortsInTraining_Type()
)
hpVgGrpPortsInTraining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgGrpPortsInTraining.setStatus("current")


class _HpVgGrpPortsCascaded_Type(OctetString):
    """Custom type hpVgGrpPortsCascaded based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpVgGrpPortsCascaded_Type.__name__ = "OctetString"
_HpVgGrpPortsCascaded_Object = MibTableColumn
hpVgGrpPortsCascaded = _HpVgGrpPortsCascaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 5),
    _HpVgGrpPortsCascaded_Type()
)
hpVgGrpPortsCascaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgGrpPortsCascaded.setStatus("current")


class _HpVgGrpPortsPromiscuous_Type(OctetString):
    """Custom type hpVgGrpPortsPromiscuous based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpVgGrpPortsPromiscuous_Type.__name__ = "OctetString"
_HpVgGrpPortsPromiscuous_Object = MibTableColumn
hpVgGrpPortsPromiscuous = _HpVgGrpPortsPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 6),
    _HpVgGrpPortsPromiscuous_Type()
)
hpVgGrpPortsPromiscuous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgGrpPortsPromiscuous.setStatus("current")
_HpVgBasicPort_ObjectIdentity = ObjectIdentity
hpVgBasicPort = _HpVgBasicPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3)
)
_HpVgBasicPortTable_Object = MibTable
hpVgBasicPortTable = _HpVgBasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpVgBasicPortTable.setStatus("current")
_HpVgBasicPortEntry_Object = MibTableRow
hpVgBasicPortEntry = _HpVgBasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1)
)
hpVgBasicPortEntry.setIndexNames(
    (0, "HP-ICF-VG-RPTR", "hpVgPortGroupIndex"),
    (0, "HP-ICF-VG-RPTR", "hpVgPortIndex"),
)
if mibBuilder.loadTexts:
    hpVgBasicPortEntry.setStatus("current")


class _HpVgPortGroupIndex_Type(Integer32):
    """Custom type hpVgPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpVgPortGroupIndex_Type.__name__ = "Integer32"
_HpVgPortGroupIndex_Object = MibTableColumn
hpVgPortGroupIndex = _HpVgPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 1),
    _HpVgPortGroupIndex_Type()
)
hpVgPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVgPortGroupIndex.setStatus("current")


class _HpVgPortIndex_Type(Integer32):
    """Custom type hpVgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpVgPortIndex_Type.__name__ = "Integer32"
_HpVgPortIndex_Object = MibTableColumn
hpVgPortIndex = _HpVgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 2),
    _HpVgPortIndex_Type()
)
hpVgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVgPortIndex.setStatus("current")
_HpVgPortPolarityReversed_Type = TruthValue
_HpVgPortPolarityReversed_Object = MibTableColumn
hpVgPortPolarityReversed = _HpVgPortPolarityReversed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 3),
    _HpVgPortPolarityReversed_Type()
)
hpVgPortPolarityReversed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgPortPolarityReversed.setStatus("current")
_HpVgPortWireSkewError_Type = TruthValue
_HpVgPortWireSkewError_Object = MibTableColumn
hpVgPortWireSkewError = _HpVgPortWireSkewError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 4),
    _HpVgPortWireSkewError_Type()
)
hpVgPortWireSkewError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgPortWireSkewError.setStatus("current")
_HpVgPortAssociatedXcvrIndex_Type = Integer32
_HpVgPortAssociatedXcvrIndex_Object = MibTableColumn
hpVgPortAssociatedXcvrIndex = _HpVgPortAssociatedXcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 5),
    _HpVgPortAssociatedXcvrIndex_Type()
)
hpVgPortAssociatedXcvrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpVgPortAssociatedXcvrIndex.setStatus("current")
_HpVgPortNumAssociatedXcvrs_Type = Integer32
_HpVgPortNumAssociatedXcvrs_Object = MibTableColumn
hpVgPortNumAssociatedXcvrs = _HpVgPortNumAssociatedXcvrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 6),
    _HpVgPortNumAssociatedXcvrs_Type()
)
hpVgPortNumAssociatedXcvrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgPortNumAssociatedXcvrs.setStatus("current")
_HpVgMonitor_ObjectIdentity = ObjectIdentity
hpVgMonitor = _HpVgMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2)
)
_HpVgMonitorGlobal_ObjectIdentity = ObjectIdentity
hpVgMonitorGlobal = _HpVgMonitorGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1)
)
_HpVgMonCounters_ObjectIdentity = ObjectIdentity
hpVgMonCounters = _HpVgMonCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1)
)
_HpVgMonGlbReadableFrames_Type = Counter32
_HpVgMonGlbReadableFrames_Object = MibScalar
hpVgMonGlbReadableFrames = _HpVgMonGlbReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 1),
    _HpVgMonGlbReadableFrames_Type()
)
hpVgMonGlbReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbReadableFrames.setStatus("current")
_HpVgMonGlbReadableOctets_Type = Counter32
_HpVgMonGlbReadableOctets_Object = MibScalar
hpVgMonGlbReadableOctets = _HpVgMonGlbReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 2),
    _HpVgMonGlbReadableOctets_Type()
)
hpVgMonGlbReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbReadableOctets.setStatus("current")
_HpVgMonGlbUnreadableOctets_Type = Counter32
_HpVgMonGlbUnreadableOctets_Object = MibScalar
hpVgMonGlbUnreadableOctets = _HpVgMonGlbUnreadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 3),
    _HpVgMonGlbUnreadableOctets_Type()
)
hpVgMonGlbUnreadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbUnreadableOctets.setStatus("current")
_HpVgMonGlbHighPriorityFrames_Type = Counter32
_HpVgMonGlbHighPriorityFrames_Object = MibScalar
hpVgMonGlbHighPriorityFrames = _HpVgMonGlbHighPriorityFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 4),
    _HpVgMonGlbHighPriorityFrames_Type()
)
hpVgMonGlbHighPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbHighPriorityFrames.setStatus("current")
_HpVgMonGlbHighPriorityOctets_Type = Counter32
_HpVgMonGlbHighPriorityOctets_Object = MibScalar
hpVgMonGlbHighPriorityOctets = _HpVgMonGlbHighPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 5),
    _HpVgMonGlbHighPriorityOctets_Type()
)
hpVgMonGlbHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbHighPriorityOctets.setStatus("current")
_HpVgMonGlbBroadcastFrames_Type = Counter32
_HpVgMonGlbBroadcastFrames_Object = MibScalar
hpVgMonGlbBroadcastFrames = _HpVgMonGlbBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 6),
    _HpVgMonGlbBroadcastFrames_Type()
)
hpVgMonGlbBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbBroadcastFrames.setStatus("current")
_HpVgMonGlbMulticastFrames_Type = Counter32
_HpVgMonGlbMulticastFrames_Object = MibScalar
hpVgMonGlbMulticastFrames = _HpVgMonGlbMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 7),
    _HpVgMonGlbMulticastFrames_Type()
)
hpVgMonGlbMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbMulticastFrames.setStatus("current")
_HpVgMonGlbIPMFrames_Type = Counter32
_HpVgMonGlbIPMFrames_Object = MibScalar
hpVgMonGlbIPMFrames = _HpVgMonGlbIPMFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 8),
    _HpVgMonGlbIPMFrames_Type()
)
hpVgMonGlbIPMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbIPMFrames.setStatus("current")
_HpVgMonGlbDataErrorFrames_Type = Counter32
_HpVgMonGlbDataErrorFrames_Object = MibScalar
hpVgMonGlbDataErrorFrames = _HpVgMonGlbDataErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 9),
    _HpVgMonGlbDataErrorFrames_Type()
)
hpVgMonGlbDataErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbDataErrorFrames.setStatus("current")
_HpVgMonGlbPriorityPromotions_Type = Counter32
_HpVgMonGlbPriorityPromotions_Object = MibScalar
hpVgMonGlbPriorityPromotions = _HpVgMonGlbPriorityPromotions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 10),
    _HpVgMonGlbPriorityPromotions_Type()
)
hpVgMonGlbPriorityPromotions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbPriorityPromotions.setStatus("current")
_HpVgMonGlbHCReadableOctets_Type = Counter64
_HpVgMonGlbHCReadableOctets_Object = MibScalar
hpVgMonGlbHCReadableOctets = _HpVgMonGlbHCReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 11),
    _HpVgMonGlbHCReadableOctets_Type()
)
hpVgMonGlbHCReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbHCReadableOctets.setStatus("current")
_HpVgMonGlbHCUnreadableOctets_Type = Counter64
_HpVgMonGlbHCUnreadableOctets_Object = MibScalar
hpVgMonGlbHCUnreadableOctets = _HpVgMonGlbHCUnreadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 12),
    _HpVgMonGlbHCUnreadableOctets_Type()
)
hpVgMonGlbHCUnreadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbHCUnreadableOctets.setStatus("current")
_HpVgMonGlbHCHighPriorityOctets_Type = Counter64
_HpVgMonGlbHCHighPriorityOctets_Object = MibScalar
hpVgMonGlbHCHighPriorityOctets = _HpVgMonGlbHCHighPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 13),
    _HpVgMonGlbHCHighPriorityOctets_Type()
)
hpVgMonGlbHCHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbHCHighPriorityOctets.setStatus("current")
_HpVgMonGlbHCNormPriorityOctets_Type = Counter64
_HpVgMonGlbHCNormPriorityOctets_Object = MibScalar
hpVgMonGlbHCNormPriorityOctets = _HpVgMonGlbHCNormPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 14),
    _HpVgMonGlbHCNormPriorityOctets_Type()
)
hpVgMonGlbHCNormPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbHCNormPriorityOctets.setStatus("current")
_HpVgMonGlbNormPriorityFrames_Type = Counter32
_HpVgMonGlbNormPriorityFrames_Object = MibScalar
hpVgMonGlbNormPriorityFrames = _HpVgMonGlbNormPriorityFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 15),
    _HpVgMonGlbNormPriorityFrames_Type()
)
hpVgMonGlbNormPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbNormPriorityFrames.setStatus("current")
_HpVgMonGlbNormPriorityOctets_Type = Counter32
_HpVgMonGlbNormPriorityOctets_Object = MibScalar
hpVgMonGlbNormPriorityOctets = _HpVgMonGlbNormPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 16),
    _HpVgMonGlbNormPriorityOctets_Type()
)
hpVgMonGlbNormPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbNormPriorityOctets.setStatus("current")
_HpVgMonGlbNullAddressedFrames_Type = Counter32
_HpVgMonGlbNullAddressedFrames_Object = MibScalar
hpVgMonGlbNullAddressedFrames = _HpVgMonGlbNullAddressedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 17),
    _HpVgMonGlbNullAddressedFrames_Type()
)
hpVgMonGlbNullAddressedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbNullAddressedFrames.setStatus("current")
_HpVgMonGlbOversizeFrames_Type = Counter32
_HpVgMonGlbOversizeFrames_Object = MibScalar
hpVgMonGlbOversizeFrames = _HpVgMonGlbOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 18),
    _HpVgMonGlbOversizeFrames_Type()
)
hpVgMonGlbOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbOversizeFrames.setStatus("current")
_HpVgMonGlbTransitionToTrainings_Type = Counter32
_HpVgMonGlbTransitionToTrainings_Object = MibScalar
hpVgMonGlbTransitionToTrainings = _HpVgMonGlbTransitionToTrainings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 19),
    _HpVgMonGlbTransitionToTrainings_Type()
)
hpVgMonGlbTransitionToTrainings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbTransitionToTrainings.setStatus("current")
_HpVgMonitorGroup_ObjectIdentity = ObjectIdentity
hpVgMonitorGroup = _HpVgMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 2)
)
_HpVgMonitorPort_ObjectIdentity = ObjectIdentity
hpVgMonitorPort = _HpVgMonitorPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 3)
)

# Managed Objects groups

hpicfVgRptrPreDot12BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 1)
)
hpicfVgRptrPreDot12BasicGroup.setObjects(
      *(("HP-ICF-VG-RPTR", "hpVgEntityName"),
        ("HP-ICF-VG-RPTR", "hpVgGrpPortsAdminStatus"),
        ("HP-ICF-VG-RPTR", "hpVgGrpPortsTrained"),
        ("HP-ICF-VG-RPTR", "hpVgGrpPortsInTraining"),
        ("HP-ICF-VG-RPTR", "hpVgGrpPortsCascaded"),
        ("HP-ICF-VG-RPTR", "hpVgGrpPortsPromiscuous"),
        ("HP-ICF-VG-RPTR", "hpVgPortPolarityReversed"),
        ("HP-ICF-VG-RPTR", "hpVgPortWireSkewError"))
)
if mibBuilder.loadTexts:
    hpicfVgRptrPreDot12BasicGroup.setStatus("obsolete")

hpicfVgRptrBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 2)
)
hpicfVgRptrBasicGroup.setObjects(
      *(("HP-ICF-VG-RPTR", "hpVgEntityName"),
        ("HP-ICF-VG-RPTR", "hpVgNullAddrTraining"),
        ("HP-ICF-VG-RPTR", "hpVgGrpPortsAdminStatus"),
        ("HP-ICF-VG-RPTR", "hpVgGrpPortsTrained"),
        ("HP-ICF-VG-RPTR", "hpVgGrpPortsInTraining"),
        ("HP-ICF-VG-RPTR", "hpVgGrpPortsCascaded"),
        ("HP-ICF-VG-RPTR", "hpVgGrpPortsPromiscuous"),
        ("HP-ICF-VG-RPTR", "hpVgPortPolarityReversed"),
        ("HP-ICF-VG-RPTR", "hpVgPortWireSkewError"))
)
if mibBuilder.loadTexts:
    hpicfVgRptrBasicGroup.setStatus("current")

hpicfVgRptrPreDot12MonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 3)
)
hpicfVgRptrPreDot12MonitorGroup.setObjects(
      *(("HP-ICF-VG-RPTR", "hpVgMonGlbReadableFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbReadableOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbUnreadableOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHighPriorityFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHighPriorityOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbBroadcastFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbMulticastFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbIPMFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbDataErrorFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbPriorityPromotions"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHCReadableOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHCUnreadableOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHCHighPriorityOctets"))
)
if mibBuilder.loadTexts:
    hpicfVgRptrPreDot12MonitorGroup.setStatus("obsolete")

hpicfVgRptrMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 4)
)
hpicfVgRptrMonitorGroup.setObjects(
      *(("HP-ICF-VG-RPTR", "hpVgMonGlbReadableFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbReadableOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbUnreadableOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHighPriorityFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHighPriorityOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbBroadcastFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbMulticastFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbIPMFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbDataErrorFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbPriorityPromotions"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHCReadableOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHCUnreadableOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHCHighPriorityOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbHCNormPriorityOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbNormPriorityFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbNormPriorityOctets"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbNullAddressedFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbOversizeFrames"),
        ("HP-ICF-VG-RPTR", "hpVgMonGlbTransitionToTrainings"))
)
if mibBuilder.loadTexts:
    hpicfVgRptrMonitorGroup.setStatus("current")

hpicfVgRptrXcvrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 5)
)
hpicfVgRptrXcvrGroup.setObjects(
      *(("HP-ICF-VG-RPTR", "hpVgXcvrType"),
        ("HP-ICF-VG-RPTR", "hpVgXcvrAssociatedPort"),
        ("HP-ICF-VG-RPTR", "hpVgXcvrState"),
        ("HP-ICF-VG-RPTR", "hpVgXcvrAbandonments"),
        ("HP-ICF-VG-RPTR", "hpVgXcvrIsMovable"),
        ("HP-ICF-VG-RPTR", "hpVgPortAssociatedXcvrIndex"),
        ("HP-ICF-VG-RPTR", "hpVgPortNumAssociatedXcvrs"))
)
if mibBuilder.loadTexts:
    hpicfVgRptrXcvrGroup.setStatus("current")

hpicfVgRptrRedundantUplinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 6)
)
hpicfVgRptrRedundantUplinkGroup.setObjects(
    ("HP-ICF-VG-RPTR", "hpVgRedundantUpLinksFlag")
)
if mibBuilder.loadTexts:
    hpicfVgRptrRedundantUplinkGroup.setStatus("current")


# Notification objects

hpVgRedundantUplinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 3, 0, 1)
)
hpVgRedundantUplinkTrap.setObjects(
    ("HP-ICF-VG-RPTR", "hpVgXcvrState")
)
if mibBuilder.loadTexts:
    hpVgRedundantUplinkTrap.setStatus(
        "current"
    )

hpVgLossOfActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 3, 0, 2)
)
hpVgLossOfActiveTrap.setObjects(
    ("ICF-VG-RPTR", "icfVgPortStatus")
)
if mibBuilder.loadTexts:
    hpVgLossOfActiveTrap.setStatus(
        "current"
    )


# Notifications groups

hpicfVgRptrBasicTraps = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 7)
)
hpicfVgRptrBasicTraps.setObjects(
    ("HP-ICF-VG-RPTR", "hpVgLossOfActiveTrap")
)
if mibBuilder.loadTexts:
    hpicfVgRptrBasicTraps.setStatus(
        "current"
    )

hpicfVgRptrRedundantUplinkTraps = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 2, 8)
)
hpicfVgRptrRedundantUplinkTraps.setObjects(
    ("HP-ICF-VG-RPTR", "hpVgRedundantUplinkTrap")
)
if mibBuilder.loadTexts:
    hpicfVgRptrRedundantUplinkTraps.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfVgRptrPreDot12Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfVgRptrPreDot12Compliance.setStatus(
        "obsolete"
    )

hpicfVgRptrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfVgRptrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-VG-RPTR",
    **{"hpicfVgRptrMib": hpicfVgRptrMib,
       "hpicfVgRptrConformance": hpicfVgRptrConformance,
       "hpicfVgRptrCompliances": hpicfVgRptrCompliances,
       "hpicfVgRptrPreDot12Compliance": hpicfVgRptrPreDot12Compliance,
       "hpicfVgRptrCompliance": hpicfVgRptrCompliance,
       "hpicfVgRptrGroups": hpicfVgRptrGroups,
       "hpicfVgRptrPreDot12BasicGroup": hpicfVgRptrPreDot12BasicGroup,
       "hpicfVgRptrBasicGroup": hpicfVgRptrBasicGroup,
       "hpicfVgRptrPreDot12MonitorGroup": hpicfVgRptrPreDot12MonitorGroup,
       "hpicfVgRptrMonitorGroup": hpicfVgRptrMonitorGroup,
       "hpicfVgRptrXcvrGroup": hpicfVgRptrXcvrGroup,
       "hpicfVgRptrRedundantUplinkGroup": hpicfVgRptrRedundantUplinkGroup,
       "hpicfVgRptrBasicTraps": hpicfVgRptrBasicTraps,
       "hpicfVgRptrRedundantUplinkTraps": hpicfVgRptrRedundantUplinkTraps,
       "hpVgBasic": hpVgBasic,
       "hpVgBasicGlobal": hpVgBasicGlobal,
       "hpVgEntityName": hpVgEntityName,
       "hpVgRedundantUpLinksFlag": hpVgRedundantUpLinksFlag,
       "hpVgXcvrTable": hpVgXcvrTable,
       "hpVgXcvrEntry": hpVgXcvrEntry,
       "hpVgXcvrGroupIndex": hpVgXcvrGroupIndex,
       "hpVgXcvrIndex": hpVgXcvrIndex,
       "hpVgXcvrType": hpVgXcvrType,
       "hpVgXcvrAssociatedPort": hpVgXcvrAssociatedPort,
       "hpVgXcvrState": hpVgXcvrState,
       "hpVgXcvrAbandonments": hpVgXcvrAbandonments,
       "hpVgXcvrIsMovable": hpVgXcvrIsMovable,
       "hpVgNullAddrTraining": hpVgNullAddrTraining,
       "hpVgBasicGroup": hpVgBasicGroup,
       "hpVgBasicGroupTable": hpVgBasicGroupTable,
       "hpVgBasicGroupEntry": hpVgBasicGroupEntry,
       "hpVgGrpGroupIndex": hpVgGrpGroupIndex,
       "hpVgGrpPortsAdminStatus": hpVgGrpPortsAdminStatus,
       "hpVgGrpPortsTrained": hpVgGrpPortsTrained,
       "hpVgGrpPortsInTraining": hpVgGrpPortsInTraining,
       "hpVgGrpPortsCascaded": hpVgGrpPortsCascaded,
       "hpVgGrpPortsPromiscuous": hpVgGrpPortsPromiscuous,
       "hpVgBasicPort": hpVgBasicPort,
       "hpVgBasicPortTable": hpVgBasicPortTable,
       "hpVgBasicPortEntry": hpVgBasicPortEntry,
       "hpVgPortGroupIndex": hpVgPortGroupIndex,
       "hpVgPortIndex": hpVgPortIndex,
       "hpVgPortPolarityReversed": hpVgPortPolarityReversed,
       "hpVgPortWireSkewError": hpVgPortWireSkewError,
       "hpVgPortAssociatedXcvrIndex": hpVgPortAssociatedXcvrIndex,
       "hpVgPortNumAssociatedXcvrs": hpVgPortNumAssociatedXcvrs,
       "hpVgMonitor": hpVgMonitor,
       "hpVgMonitorGlobal": hpVgMonitorGlobal,
       "hpVgMonCounters": hpVgMonCounters,
       "hpVgMonGlbReadableFrames": hpVgMonGlbReadableFrames,
       "hpVgMonGlbReadableOctets": hpVgMonGlbReadableOctets,
       "hpVgMonGlbUnreadableOctets": hpVgMonGlbUnreadableOctets,
       "hpVgMonGlbHighPriorityFrames": hpVgMonGlbHighPriorityFrames,
       "hpVgMonGlbHighPriorityOctets": hpVgMonGlbHighPriorityOctets,
       "hpVgMonGlbBroadcastFrames": hpVgMonGlbBroadcastFrames,
       "hpVgMonGlbMulticastFrames": hpVgMonGlbMulticastFrames,
       "hpVgMonGlbIPMFrames": hpVgMonGlbIPMFrames,
       "hpVgMonGlbDataErrorFrames": hpVgMonGlbDataErrorFrames,
       "hpVgMonGlbPriorityPromotions": hpVgMonGlbPriorityPromotions,
       "hpVgMonGlbHCReadableOctets": hpVgMonGlbHCReadableOctets,
       "hpVgMonGlbHCUnreadableOctets": hpVgMonGlbHCUnreadableOctets,
       "hpVgMonGlbHCHighPriorityOctets": hpVgMonGlbHCHighPriorityOctets,
       "hpVgMonGlbHCNormPriorityOctets": hpVgMonGlbHCNormPriorityOctets,
       "hpVgMonGlbNormPriorityFrames": hpVgMonGlbNormPriorityFrames,
       "hpVgMonGlbNormPriorityOctets": hpVgMonGlbNormPriorityOctets,
       "hpVgMonGlbNullAddressedFrames": hpVgMonGlbNullAddressedFrames,
       "hpVgMonGlbOversizeFrames": hpVgMonGlbOversizeFrames,
       "hpVgMonGlbTransitionToTrainings": hpVgMonGlbTransitionToTrainings,
       "hpVgMonitorGroup": hpVgMonitorGroup,
       "hpVgMonitorPort": hpVgMonitorPort,
       "hpVgRedundantUplinkTrap": hpVgRedundantUplinkTrap,
       "hpVgLossOfActiveTrap": hpVgLossOfActiveTrap}
)
