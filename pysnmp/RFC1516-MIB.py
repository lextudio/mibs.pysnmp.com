# SNMP MIB module (RFC1516-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1516-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:32 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "RFC1286-MIB",
    "MacAddress")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpDot3RptrMgt_ObjectIdentity = ObjectIdentity
snmpDot3RptrMgt = _SnmpDot3RptrMgt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22)
)
_RptrBasicPackage_ObjectIdentity = ObjectIdentity
rptrBasicPackage = _RptrBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1)
)
_RptrRptrInfo_ObjectIdentity = ObjectIdentity
rptrRptrInfo = _RptrRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 1)
)


class _RptrGroupCapacity_Type(Integer32):
    """Custom type rptrGroupCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrGroupCapacity_Type.__name__ = "Integer32"
_RptrGroupCapacity_Object = MibScalar
rptrGroupCapacity = _RptrGroupCapacity_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 1),
    _RptrGroupCapacity_Type()
)
rptrGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupCapacity.setStatus("mandatory")


class _RptrOperStatus_Type(Integer32):
    """Custom type rptrOperStatus based on Integer32"""
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
        *(("generalFailure", 6),
          ("groupFailure", 4),
          ("ok", 2),
          ("other", 1),
          ("portFailure", 5),
          ("rptrFailure", 3))
    )


_RptrOperStatus_Type.__name__ = "Integer32"
_RptrOperStatus_Object = MibScalar
rptrOperStatus = _RptrOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 2),
    _RptrOperStatus_Type()
)
rptrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrOperStatus.setStatus("mandatory")


class _RptrHealthText_Type(DisplayString):
    """Custom type rptrHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RptrHealthText_Type.__name__ = "DisplayString"
_RptrHealthText_Object = MibScalar
rptrHealthText = _RptrHealthText_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 3),
    _RptrHealthText_Type()
)
rptrHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrHealthText.setStatus("mandatory")


class _RptrReset_Type(Integer32):
    """Custom type rptrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_RptrReset_Type.__name__ = "Integer32"
_RptrReset_Object = MibScalar
rptrReset = _RptrReset_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 4),
    _RptrReset_Type()
)
rptrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrReset.setStatus("mandatory")


class _RptrNonDisruptTest_Type(Integer32):
    """Custom type rptrNonDisruptTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest", 1),
          ("selfTest", 2))
    )


_RptrNonDisruptTest_Type.__name__ = "Integer32"
_RptrNonDisruptTest_Object = MibScalar
rptrNonDisruptTest = _RptrNonDisruptTest_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 5),
    _RptrNonDisruptTest_Type()
)
rptrNonDisruptTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrNonDisruptTest.setStatus("mandatory")
_RptrTotalPartitionedPorts_Type = Gauge32
_RptrTotalPartitionedPorts_Object = MibScalar
rptrTotalPartitionedPorts = _RptrTotalPartitionedPorts_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 1, 6),
    _RptrTotalPartitionedPorts_Type()
)
rptrTotalPartitionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTotalPartitionedPorts.setStatus("mandatory")
_RptrGroupInfo_ObjectIdentity = ObjectIdentity
rptrGroupInfo = _RptrGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 2)
)
_RptrGroupTable_Object = MibTable
rptrGroupTable = _RptrGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rptrGroupTable.setStatus("mandatory")
_RptrGroupEntry_Object = MibTableRow
rptrGroupEntry = _RptrGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1)
)
rptrGroupEntry.setIndexNames(
    (0, "RFC1516-MIB", "rptrGroupIndex"),
)
if mibBuilder.loadTexts:
    rptrGroupEntry.setStatus("mandatory")


class _RptrGroupIndex_Type(Integer32):
    """Custom type rptrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrGroupIndex_Type.__name__ = "Integer32"
_RptrGroupIndex_Object = MibTableColumn
rptrGroupIndex = _RptrGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 1),
    _RptrGroupIndex_Type()
)
rptrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupIndex.setStatus("mandatory")


class _RptrGroupDescr_Type(DisplayString):
    """Custom type rptrGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RptrGroupDescr_Type.__name__ = "DisplayString"
_RptrGroupDescr_Object = MibTableColumn
rptrGroupDescr = _RptrGroupDescr_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 2),
    _RptrGroupDescr_Type()
)
rptrGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupDescr.setStatus("mandatory")
_RptrGroupObjectID_Type = ObjectIdentifier
_RptrGroupObjectID_Object = MibTableColumn
rptrGroupObjectID = _RptrGroupObjectID_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 3),
    _RptrGroupObjectID_Type()
)
rptrGroupObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupObjectID.setStatus("mandatory")


class _RptrGroupOperStatus_Type(Integer32):
    """Custom type rptrGroupOperStatus based on Integer32"""
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
        *(("malfunctioning", 3),
          ("notPresent", 4),
          ("operational", 2),
          ("other", 1),
          ("resetInProgress", 6),
          ("underTest", 5))
    )


_RptrGroupOperStatus_Type.__name__ = "Integer32"
_RptrGroupOperStatus_Object = MibTableColumn
rptrGroupOperStatus = _RptrGroupOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 4),
    _RptrGroupOperStatus_Type()
)
rptrGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupOperStatus.setStatus("mandatory")
_RptrGroupLastOperStatusChange_Type = TimeTicks
_RptrGroupLastOperStatusChange_Object = MibTableColumn
rptrGroupLastOperStatusChange = _RptrGroupLastOperStatusChange_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 5),
    _RptrGroupLastOperStatusChange_Type()
)
rptrGroupLastOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupLastOperStatusChange.setStatus("mandatory")


class _RptrGroupPortCapacity_Type(Integer32):
    """Custom type rptrGroupPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrGroupPortCapacity_Type.__name__ = "Integer32"
_RptrGroupPortCapacity_Object = MibTableColumn
rptrGroupPortCapacity = _RptrGroupPortCapacity_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 2, 1, 1, 6),
    _RptrGroupPortCapacity_Type()
)
rptrGroupPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrGroupPortCapacity.setStatus("mandatory")
_RptrPortInfo_ObjectIdentity = ObjectIdentity
rptrPortInfo = _RptrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 1, 3)
)
_RptrPortTable_Object = MibTable
rptrPortTable = _RptrPortTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rptrPortTable.setStatus("mandatory")
_RptrPortEntry_Object = MibTableRow
rptrPortEntry = _RptrPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1)
)
rptrPortEntry.setIndexNames(
    (0, "RFC1516-MIB", "rptrPortGroupIndex"),
    (0, "RFC1516-MIB", "rptrPortIndex"),
)
if mibBuilder.loadTexts:
    rptrPortEntry.setStatus("mandatory")


class _RptrPortGroupIndex_Type(Integer32):
    """Custom type rptrPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrPortGroupIndex_Type.__name__ = "Integer32"
_RptrPortGroupIndex_Object = MibTableColumn
rptrPortGroupIndex = _RptrPortGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 1),
    _RptrPortGroupIndex_Type()
)
rptrPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortGroupIndex.setStatus("mandatory")


class _RptrPortIndex_Type(Integer32):
    """Custom type rptrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrPortIndex_Type.__name__ = "Integer32"
_RptrPortIndex_Object = MibTableColumn
rptrPortIndex = _RptrPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 2),
    _RptrPortIndex_Type()
)
rptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortIndex.setStatus("mandatory")


class _RptrPortAdminStatus_Type(Integer32):
    """Custom type rptrPortAdminStatus based on Integer32"""
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


_RptrPortAdminStatus_Type.__name__ = "Integer32"
_RptrPortAdminStatus_Object = MibTableColumn
rptrPortAdminStatus = _RptrPortAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 3),
    _RptrPortAdminStatus_Type()
)
rptrPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rptrPortAdminStatus.setStatus("mandatory")


class _RptrPortAutoPartitionState_Type(Integer32):
    """Custom type rptrPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 2),
          ("notAutoPartitioned", 1))
    )


_RptrPortAutoPartitionState_Type.__name__ = "Integer32"
_RptrPortAutoPartitionState_Object = MibTableColumn
rptrPortAutoPartitionState = _RptrPortAutoPartitionState_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 4),
    _RptrPortAutoPartitionState_Type()
)
rptrPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortAutoPartitionState.setStatus("mandatory")


class _RptrPortOperStatus_Type(Integer32):
    """Custom type rptrPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notPresent", 3),
          ("operational", 1))
    )


_RptrPortOperStatus_Type.__name__ = "Integer32"
_RptrPortOperStatus_Object = MibTableColumn
rptrPortOperStatus = _RptrPortOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 5),
    _RptrPortOperStatus_Type()
)
rptrPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortOperStatus.setStatus("mandatory")
_RptrMonitorPackage_ObjectIdentity = ObjectIdentity
rptrMonitorPackage = _RptrMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2)
)
_RptrMonitorRptrInfo_ObjectIdentity = ObjectIdentity
rptrMonitorRptrInfo = _RptrMonitorRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 1)
)
_RptrMonitorTransmitCollisions_Type = Counter32
_RptrMonitorTransmitCollisions_Object = MibScalar
rptrMonitorTransmitCollisions = _RptrMonitorTransmitCollisions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 1, 1),
    _RptrMonitorTransmitCollisions_Type()
)
rptrMonitorTransmitCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorTransmitCollisions.setStatus("mandatory")
_RptrMonitorGroupInfo_ObjectIdentity = ObjectIdentity
rptrMonitorGroupInfo = _RptrMonitorGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 2)
)
_RptrMonitorGroupTable_Object = MibTable
rptrMonitorGroupTable = _RptrMonitorGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rptrMonitorGroupTable.setStatus("mandatory")
_RptrMonitorGroupEntry_Object = MibTableRow
rptrMonitorGroupEntry = _RptrMonitorGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1)
)
rptrMonitorGroupEntry.setIndexNames(
    (0, "RFC1516-MIB", "rptrMonitorGroupIndex"),
)
if mibBuilder.loadTexts:
    rptrMonitorGroupEntry.setStatus("mandatory")


class _RptrMonitorGroupIndex_Type(Integer32):
    """Custom type rptrMonitorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrMonitorGroupIndex_Type.__name__ = "Integer32"
_RptrMonitorGroupIndex_Object = MibTableColumn
rptrMonitorGroupIndex = _RptrMonitorGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 1),
    _RptrMonitorGroupIndex_Type()
)
rptrMonitorGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupIndex.setStatus("mandatory")
_RptrMonitorGroupTotalFrames_Type = Counter32
_RptrMonitorGroupTotalFrames_Object = MibTableColumn
rptrMonitorGroupTotalFrames = _RptrMonitorGroupTotalFrames_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 2),
    _RptrMonitorGroupTotalFrames_Type()
)
rptrMonitorGroupTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalFrames.setStatus("mandatory")
_RptrMonitorGroupTotalOctets_Type = Counter32
_RptrMonitorGroupTotalOctets_Object = MibTableColumn
rptrMonitorGroupTotalOctets = _RptrMonitorGroupTotalOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 3),
    _RptrMonitorGroupTotalOctets_Type()
)
rptrMonitorGroupTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalOctets.setStatus("mandatory")
_RptrMonitorGroupTotalErrors_Type = Counter32
_RptrMonitorGroupTotalErrors_Object = MibTableColumn
rptrMonitorGroupTotalErrors = _RptrMonitorGroupTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 2, 1, 1, 4),
    _RptrMonitorGroupTotalErrors_Type()
)
rptrMonitorGroupTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorGroupTotalErrors.setStatus("mandatory")
_RptrMonitorPortInfo_ObjectIdentity = ObjectIdentity
rptrMonitorPortInfo = _RptrMonitorPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 2, 3)
)
_RptrMonitorPortTable_Object = MibTable
rptrMonitorPortTable = _RptrMonitorPortTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rptrMonitorPortTable.setStatus("mandatory")
_RptrMonitorPortEntry_Object = MibTableRow
rptrMonitorPortEntry = _RptrMonitorPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1)
)
rptrMonitorPortEntry.setIndexNames(
    (0, "RFC1516-MIB", "rptrMonitorPortGroupIndex"),
    (0, "RFC1516-MIB", "rptrMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    rptrMonitorPortEntry.setStatus("mandatory")


class _RptrMonitorPortGroupIndex_Type(Integer32):
    """Custom type rptrMonitorPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrMonitorPortGroupIndex_Type.__name__ = "Integer32"
_RptrMonitorPortGroupIndex_Object = MibTableColumn
rptrMonitorPortGroupIndex = _RptrMonitorPortGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 1),
    _RptrMonitorPortGroupIndex_Type()
)
rptrMonitorPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortGroupIndex.setStatus("mandatory")


class _RptrMonitorPortIndex_Type(Integer32):
    """Custom type rptrMonitorPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrMonitorPortIndex_Type.__name__ = "Integer32"
_RptrMonitorPortIndex_Object = MibTableColumn
rptrMonitorPortIndex = _RptrMonitorPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 2),
    _RptrMonitorPortIndex_Type()
)
rptrMonitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortIndex.setStatus("mandatory")
_RptrMonitorPortReadableFrames_Type = Counter32
_RptrMonitorPortReadableFrames_Object = MibTableColumn
rptrMonitorPortReadableFrames = _RptrMonitorPortReadableFrames_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 3),
    _RptrMonitorPortReadableFrames_Type()
)
rptrMonitorPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortReadableFrames.setStatus("mandatory")
_RptrMonitorPortReadableOctets_Type = Counter32
_RptrMonitorPortReadableOctets_Object = MibTableColumn
rptrMonitorPortReadableOctets = _RptrMonitorPortReadableOctets_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 4),
    _RptrMonitorPortReadableOctets_Type()
)
rptrMonitorPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortReadableOctets.setStatus("mandatory")
_RptrMonitorPortFCSErrors_Type = Counter32
_RptrMonitorPortFCSErrors_Object = MibTableColumn
rptrMonitorPortFCSErrors = _RptrMonitorPortFCSErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 5),
    _RptrMonitorPortFCSErrors_Type()
)
rptrMonitorPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortFCSErrors.setStatus("mandatory")
_RptrMonitorPortAlignmentErrors_Type = Counter32
_RptrMonitorPortAlignmentErrors_Object = MibTableColumn
rptrMonitorPortAlignmentErrors = _RptrMonitorPortAlignmentErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 6),
    _RptrMonitorPortAlignmentErrors_Type()
)
rptrMonitorPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortAlignmentErrors.setStatus("mandatory")
_RptrMonitorPortFrameTooLongs_Type = Counter32
_RptrMonitorPortFrameTooLongs_Object = MibTableColumn
rptrMonitorPortFrameTooLongs = _RptrMonitorPortFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 7),
    _RptrMonitorPortFrameTooLongs_Type()
)
rptrMonitorPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortFrameTooLongs.setStatus("mandatory")
_RptrMonitorPortShortEvents_Type = Counter32
_RptrMonitorPortShortEvents_Object = MibTableColumn
rptrMonitorPortShortEvents = _RptrMonitorPortShortEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 8),
    _RptrMonitorPortShortEvents_Type()
)
rptrMonitorPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortShortEvents.setStatus("mandatory")
_RptrMonitorPortRunts_Type = Counter32
_RptrMonitorPortRunts_Object = MibTableColumn
rptrMonitorPortRunts = _RptrMonitorPortRunts_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 9),
    _RptrMonitorPortRunts_Type()
)
rptrMonitorPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortRunts.setStatus("mandatory")
_RptrMonitorPortCollisions_Type = Counter32
_RptrMonitorPortCollisions_Object = MibTableColumn
rptrMonitorPortCollisions = _RptrMonitorPortCollisions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 10),
    _RptrMonitorPortCollisions_Type()
)
rptrMonitorPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortCollisions.setStatus("mandatory")
_RptrMonitorPortLateEvents_Type = Counter32
_RptrMonitorPortLateEvents_Object = MibTableColumn
rptrMonitorPortLateEvents = _RptrMonitorPortLateEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 11),
    _RptrMonitorPortLateEvents_Type()
)
rptrMonitorPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortLateEvents.setStatus("mandatory")
_RptrMonitorPortVeryLongEvents_Type = Counter32
_RptrMonitorPortVeryLongEvents_Object = MibTableColumn
rptrMonitorPortVeryLongEvents = _RptrMonitorPortVeryLongEvents_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 12),
    _RptrMonitorPortVeryLongEvents_Type()
)
rptrMonitorPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortVeryLongEvents.setStatus("mandatory")
_RptrMonitorPortDataRateMismatches_Type = Counter32
_RptrMonitorPortDataRateMismatches_Object = MibTableColumn
rptrMonitorPortDataRateMismatches = _RptrMonitorPortDataRateMismatches_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 13),
    _RptrMonitorPortDataRateMismatches_Type()
)
rptrMonitorPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortDataRateMismatches.setStatus("mandatory")
_RptrMonitorPortAutoPartitions_Type = Counter32
_RptrMonitorPortAutoPartitions_Object = MibTableColumn
rptrMonitorPortAutoPartitions = _RptrMonitorPortAutoPartitions_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 14),
    _RptrMonitorPortAutoPartitions_Type()
)
rptrMonitorPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortAutoPartitions.setStatus("mandatory")
_RptrMonitorPortTotalErrors_Type = Counter32
_RptrMonitorPortTotalErrors_Object = MibTableColumn
rptrMonitorPortTotalErrors = _RptrMonitorPortTotalErrors_Object(
    (1, 3, 6, 1, 2, 1, 22, 2, 3, 1, 1, 15),
    _RptrMonitorPortTotalErrors_Type()
)
rptrMonitorPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrMonitorPortTotalErrors.setStatus("mandatory")
_RptrAddrTrackPackage_ObjectIdentity = ObjectIdentity
rptrAddrTrackPackage = _RptrAddrTrackPackage_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3)
)
_RptrAddrTrackRptrInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackRptrInfo = _RptrAddrTrackRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 1)
)
_RptrAddrTrackGroupInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackGroupInfo = _RptrAddrTrackGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 2)
)
_RptrAddrTrackPortInfo_ObjectIdentity = ObjectIdentity
rptrAddrTrackPortInfo = _RptrAddrTrackPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 22, 3, 3)
)
_RptrAddrTrackTable_Object = MibTable
rptrAddrTrackTable = _RptrAddrTrackTable_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1)
)
if mibBuilder.loadTexts:
    rptrAddrTrackTable.setStatus("mandatory")
_RptrAddrTrackEntry_Object = MibTableRow
rptrAddrTrackEntry = _RptrAddrTrackEntry_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1)
)
rptrAddrTrackEntry.setIndexNames(
    (0, "RFC1516-MIB", "rptrAddrTrackGroupIndex"),
    (0, "RFC1516-MIB", "rptrAddrTrackPortIndex"),
)
if mibBuilder.loadTexts:
    rptrAddrTrackEntry.setStatus("mandatory")


class _RptrAddrTrackGroupIndex_Type(Integer32):
    """Custom type rptrAddrTrackGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrAddrTrackGroupIndex_Type.__name__ = "Integer32"
_RptrAddrTrackGroupIndex_Object = MibTableColumn
rptrAddrTrackGroupIndex = _RptrAddrTrackGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 1),
    _RptrAddrTrackGroupIndex_Type()
)
rptrAddrTrackGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackGroupIndex.setStatus("mandatory")


class _RptrAddrTrackPortIndex_Type(Integer32):
    """Custom type rptrAddrTrackPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RptrAddrTrackPortIndex_Type.__name__ = "Integer32"
_RptrAddrTrackPortIndex_Object = MibTableColumn
rptrAddrTrackPortIndex = _RptrAddrTrackPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 2),
    _RptrAddrTrackPortIndex_Type()
)
rptrAddrTrackPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackPortIndex.setStatus("mandatory")
_RptrAddrTrackLastSourceAddress_Type = MacAddress
_RptrAddrTrackLastSourceAddress_Object = MibTableColumn
rptrAddrTrackLastSourceAddress = _RptrAddrTrackLastSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 3),
    _RptrAddrTrackLastSourceAddress_Type()
)
rptrAddrTrackLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackLastSourceAddress.setStatus("deprecated")
_RptrAddrTrackSourceAddrChanges_Type = Counter32
_RptrAddrTrackSourceAddrChanges_Object = MibTableColumn
rptrAddrTrackSourceAddrChanges = _RptrAddrTrackSourceAddrChanges_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 4),
    _RptrAddrTrackSourceAddrChanges_Type()
)
rptrAddrTrackSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackSourceAddrChanges.setStatus("mandatory")
_RptrAddrTrackNewLastSrcAddress_Type = OctetString
_RptrAddrTrackNewLastSrcAddress_Object = MibTableColumn
rptrAddrTrackNewLastSrcAddress = _RptrAddrTrackNewLastSrcAddress_Object(
    (1, 3, 6, 1, 2, 1, 22, 3, 3, 1, 1, 5),
    _RptrAddrTrackNewLastSrcAddress_Type()
)
rptrAddrTrackNewLastSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrAddrTrackNewLastSrcAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rptrHealth = NotificationType(
    (1, 3, 6, 1, 2, 1, 22, 0, 1)
)
rptrHealth.setObjects(
    ("RFC1516-MIB", "rptrOperStatus")
)
if mibBuilder.loadTexts:
    rptrHealth.setStatus(
        ""
    )

rptrGroupChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 22, 0, 2)
)
rptrGroupChange.setObjects(
    ("RFC1516-MIB", "rptrGroupIndex")
)
if mibBuilder.loadTexts:
    rptrGroupChange.setStatus(
        ""
    )

rptrResetEvent = NotificationType(
    (1, 3, 6, 1, 2, 1, 22, 0, 3)
)
rptrResetEvent.setObjects(
    ("RFC1516-MIB", "rptrOperStatus")
)
if mibBuilder.loadTexts:
    rptrResetEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1516-MIB",
    **{"snmpDot3RptrMgt": snmpDot3RptrMgt,
       "rptrHealth": rptrHealth,
       "rptrGroupChange": rptrGroupChange,
       "rptrResetEvent": rptrResetEvent,
       "rptrBasicPackage": rptrBasicPackage,
       "rptrRptrInfo": rptrRptrInfo,
       "rptrGroupCapacity": rptrGroupCapacity,
       "rptrOperStatus": rptrOperStatus,
       "rptrHealthText": rptrHealthText,
       "rptrReset": rptrReset,
       "rptrNonDisruptTest": rptrNonDisruptTest,
       "rptrTotalPartitionedPorts": rptrTotalPartitionedPorts,
       "rptrGroupInfo": rptrGroupInfo,
       "rptrGroupTable": rptrGroupTable,
       "rptrGroupEntry": rptrGroupEntry,
       "rptrGroupIndex": rptrGroupIndex,
       "rptrGroupDescr": rptrGroupDescr,
       "rptrGroupObjectID": rptrGroupObjectID,
       "rptrGroupOperStatus": rptrGroupOperStatus,
       "rptrGroupLastOperStatusChange": rptrGroupLastOperStatusChange,
       "rptrGroupPortCapacity": rptrGroupPortCapacity,
       "rptrPortInfo": rptrPortInfo,
       "rptrPortTable": rptrPortTable,
       "rptrPortEntry": rptrPortEntry,
       "rptrPortGroupIndex": rptrPortGroupIndex,
       "rptrPortIndex": rptrPortIndex,
       "rptrPortAdminStatus": rptrPortAdminStatus,
       "rptrPortAutoPartitionState": rptrPortAutoPartitionState,
       "rptrPortOperStatus": rptrPortOperStatus,
       "rptrMonitorPackage": rptrMonitorPackage,
       "rptrMonitorRptrInfo": rptrMonitorRptrInfo,
       "rptrMonitorTransmitCollisions": rptrMonitorTransmitCollisions,
       "rptrMonitorGroupInfo": rptrMonitorGroupInfo,
       "rptrMonitorGroupTable": rptrMonitorGroupTable,
       "rptrMonitorGroupEntry": rptrMonitorGroupEntry,
       "rptrMonitorGroupIndex": rptrMonitorGroupIndex,
       "rptrMonitorGroupTotalFrames": rptrMonitorGroupTotalFrames,
       "rptrMonitorGroupTotalOctets": rptrMonitorGroupTotalOctets,
       "rptrMonitorGroupTotalErrors": rptrMonitorGroupTotalErrors,
       "rptrMonitorPortInfo": rptrMonitorPortInfo,
       "rptrMonitorPortTable": rptrMonitorPortTable,
       "rptrMonitorPortEntry": rptrMonitorPortEntry,
       "rptrMonitorPortGroupIndex": rptrMonitorPortGroupIndex,
       "rptrMonitorPortIndex": rptrMonitorPortIndex,
       "rptrMonitorPortReadableFrames": rptrMonitorPortReadableFrames,
       "rptrMonitorPortReadableOctets": rptrMonitorPortReadableOctets,
       "rptrMonitorPortFCSErrors": rptrMonitorPortFCSErrors,
       "rptrMonitorPortAlignmentErrors": rptrMonitorPortAlignmentErrors,
       "rptrMonitorPortFrameTooLongs": rptrMonitorPortFrameTooLongs,
       "rptrMonitorPortShortEvents": rptrMonitorPortShortEvents,
       "rptrMonitorPortRunts": rptrMonitorPortRunts,
       "rptrMonitorPortCollisions": rptrMonitorPortCollisions,
       "rptrMonitorPortLateEvents": rptrMonitorPortLateEvents,
       "rptrMonitorPortVeryLongEvents": rptrMonitorPortVeryLongEvents,
       "rptrMonitorPortDataRateMismatches": rptrMonitorPortDataRateMismatches,
       "rptrMonitorPortAutoPartitions": rptrMonitorPortAutoPartitions,
       "rptrMonitorPortTotalErrors": rptrMonitorPortTotalErrors,
       "rptrAddrTrackPackage": rptrAddrTrackPackage,
       "rptrAddrTrackRptrInfo": rptrAddrTrackRptrInfo,
       "rptrAddrTrackGroupInfo": rptrAddrTrackGroupInfo,
       "rptrAddrTrackPortInfo": rptrAddrTrackPortInfo,
       "rptrAddrTrackTable": rptrAddrTrackTable,
       "rptrAddrTrackEntry": rptrAddrTrackEntry,
       "rptrAddrTrackGroupIndex": rptrAddrTrackGroupIndex,
       "rptrAddrTrackPortIndex": rptrAddrTrackPortIndex,
       "rptrAddrTrackLastSourceAddress": rptrAddrTrackLastSourceAddress,
       "rptrAddrTrackSourceAddrChanges": rptrAddrTrackSourceAddrChanges,
       "rptrAddrTrackNewLastSrcAddress": rptrAddrTrackNewLastSrcAddress}
)
