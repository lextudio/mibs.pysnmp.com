# SNMP MIB module (HPN-ICF-MIRRORGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MIRRORGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:06 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfMirrGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68)
)
hpnicfMirrGroup.setRevisions(
        ("2006-01-10 19:03",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfMGInfoObjects_ObjectIdentity = ObjectIdentity
hpnicfMGInfoObjects = _HpnicfMGInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1)
)
_HpnicfMGObjects_ObjectIdentity = ObjectIdentity
hpnicfMGObjects = _HpnicfMGObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 1)
)
_HpnicfMGTable_Object = MibTable
hpnicfMGTable = _HpnicfMGTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfMGTable.setStatus("current")
_HpnicfMGEntry_Object = MibTableRow
hpnicfMGEntry = _HpnicfMGEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 1, 1, 1)
)
hpnicfMGEntry.setIndexNames(
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGID"),
)
if mibBuilder.loadTexts:
    hpnicfMGEntry.setStatus("current")


class _HpnicfMGID_Type(Integer32):
    """Custom type hpnicfMGID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfMGID_Type.__name__ = "Integer32"
_HpnicfMGID_Object = MibTableColumn
hpnicfMGID = _HpnicfMGID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 1, 1, 1, 1),
    _HpnicfMGID_Type()
)
hpnicfMGID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMGID.setStatus("current")


class _HpnicfMGType_Type(Integer32):
    """Custom type hpnicfMGType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remoteDestination", 3),
          ("remoteSource", 2))
    )


_HpnicfMGType_Type.__name__ = "Integer32"
_HpnicfMGType_Object = MibTableColumn
hpnicfMGType = _HpnicfMGType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 1, 1, 1, 2),
    _HpnicfMGType_Type()
)
hpnicfMGType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGType.setStatus("current")


class _HpnicfMGStatus_Type(Integer32):
    """Custom type hpnicfMGStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HpnicfMGStatus_Type.__name__ = "Integer32"
_HpnicfMGStatus_Object = MibTableColumn
hpnicfMGStatus = _HpnicfMGStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 1, 1, 1, 3),
    _HpnicfMGStatus_Type()
)
hpnicfMGStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMGStatus.setStatus("current")
_HpnicfMGRowStatus_Type = RowStatus
_HpnicfMGRowStatus_Object = MibTableColumn
hpnicfMGRowStatus = _HpnicfMGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 1, 1, 1, 4),
    _HpnicfMGRowStatus_Type()
)
hpnicfMGRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGRowStatus.setStatus("current")
_HpnicfMGMirrorIfObjects_ObjectIdentity = ObjectIdentity
hpnicfMGMirrorIfObjects = _HpnicfMGMirrorIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 2)
)
_HpnicfMGMirrorIfTable_Object = MibTable
hpnicfMGMirrorIfTable = _HpnicfMGMirrorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfMGMirrorIfTable.setStatus("current")
_HpnicfMGMirrorIfEntry_Object = MibTableRow
hpnicfMGMirrorIfEntry = _HpnicfMGMirrorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 2, 1, 1)
)
hpnicfMGMirrorIfEntry.setIndexNames(
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGID"),
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGMirrorIfIndex"),
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGMirrorDirection"),
)
if mibBuilder.loadTexts:
    hpnicfMGMirrorIfEntry.setStatus("current")
_HpnicfMGMirrorIfIndex_Type = Integer32
_HpnicfMGMirrorIfIndex_Object = MibTableColumn
hpnicfMGMirrorIfIndex = _HpnicfMGMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 2, 1, 1, 1),
    _HpnicfMGMirrorIfIndex_Type()
)
hpnicfMGMirrorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMGMirrorIfIndex.setStatus("current")


class _HpnicfMGMirrorDirection_Type(Integer32):
    """Custom type hpnicfMGMirrorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_HpnicfMGMirrorDirection_Type.__name__ = "Integer32"
_HpnicfMGMirrorDirection_Object = MibTableColumn
hpnicfMGMirrorDirection = _HpnicfMGMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 2, 1, 1, 2),
    _HpnicfMGMirrorDirection_Type()
)
hpnicfMGMirrorDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMGMirrorDirection.setStatus("current")
_HpnicfMGMirrorRowStatus_Type = RowStatus
_HpnicfMGMirrorRowStatus_Object = MibTableColumn
hpnicfMGMirrorRowStatus = _HpnicfMGMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 2, 1, 1, 3),
    _HpnicfMGMirrorRowStatus_Type()
)
hpnicfMGMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGMirrorRowStatus.setStatus("current")
_HpnicfMGMonitorIfObjects_ObjectIdentity = ObjectIdentity
hpnicfMGMonitorIfObjects = _HpnicfMGMonitorIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 3)
)
_HpnicfMGMonitorIfTable_Object = MibTable
hpnicfMGMonitorIfTable = _HpnicfMGMonitorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfMGMonitorIfTable.setStatus("current")
_HpnicfMGMonitorIfEntry_Object = MibTableRow
hpnicfMGMonitorIfEntry = _HpnicfMGMonitorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 3, 1, 1)
)
hpnicfMGMonitorIfEntry.setIndexNames(
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGID"),
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGMonitorIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMGMonitorIfEntry.setStatus("current")
_HpnicfMGMonitorIfIndex_Type = Integer32
_HpnicfMGMonitorIfIndex_Object = MibTableColumn
hpnicfMGMonitorIfIndex = _HpnicfMGMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 3, 1, 1, 1),
    _HpnicfMGMonitorIfIndex_Type()
)
hpnicfMGMonitorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMGMonitorIfIndex.setStatus("current")
_HpnicfMGMonitorRowStatus_Type = RowStatus
_HpnicfMGMonitorRowStatus_Object = MibTableColumn
hpnicfMGMonitorRowStatus = _HpnicfMGMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 3, 1, 1, 2),
    _HpnicfMGMonitorRowStatus_Type()
)
hpnicfMGMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGMonitorRowStatus.setStatus("current")
_HpnicfMGReflectorIfObjects_ObjectIdentity = ObjectIdentity
hpnicfMGReflectorIfObjects = _HpnicfMGReflectorIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 4)
)
_HpnicfMGReflectorIfTable_Object = MibTable
hpnicfMGReflectorIfTable = _HpnicfMGReflectorIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfMGReflectorIfTable.setStatus("current")
_HpnicfMGReflectorIfEntry_Object = MibTableRow
hpnicfMGReflectorIfEntry = _HpnicfMGReflectorIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 4, 1, 1)
)
hpnicfMGReflectorIfEntry.setIndexNames(
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGID"),
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGReflectorIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMGReflectorIfEntry.setStatus("current")
_HpnicfMGReflectorIfIndex_Type = Integer32
_HpnicfMGReflectorIfIndex_Object = MibTableColumn
hpnicfMGReflectorIfIndex = _HpnicfMGReflectorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 4, 1, 1, 1),
    _HpnicfMGReflectorIfIndex_Type()
)
hpnicfMGReflectorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMGReflectorIfIndex.setStatus("current")
_HpnicfMGReflectorRowStatus_Type = RowStatus
_HpnicfMGReflectorRowStatus_Object = MibTableColumn
hpnicfMGReflectorRowStatus = _HpnicfMGReflectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 4, 1, 1, 2),
    _HpnicfMGReflectorRowStatus_Type()
)
hpnicfMGReflectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGReflectorRowStatus.setStatus("current")
_HpnicfMGRprobeVlanObjects_ObjectIdentity = ObjectIdentity
hpnicfMGRprobeVlanObjects = _HpnicfMGRprobeVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 5)
)
_HpnicfMGRprobeVlanTable_Object = MibTable
hpnicfMGRprobeVlanTable = _HpnicfMGRprobeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfMGRprobeVlanTable.setStatus("current")
_HpnicfMGRprobeVlanEntry_Object = MibTableRow
hpnicfMGRprobeVlanEntry = _HpnicfMGRprobeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 5, 1, 1)
)
hpnicfMGRprobeVlanEntry.setIndexNames(
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGID"),
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGRprobeVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfMGRprobeVlanEntry.setStatus("current")


class _HpnicfMGRprobeVlanID_Type(Integer32):
    """Custom type hpnicfMGRprobeVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfMGRprobeVlanID_Type.__name__ = "Integer32"
_HpnicfMGRprobeVlanID_Object = MibTableColumn
hpnicfMGRprobeVlanID = _HpnicfMGRprobeVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 5, 1, 1, 1),
    _HpnicfMGRprobeVlanID_Type()
)
hpnicfMGRprobeVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMGRprobeVlanID.setStatus("current")
_HpnicfMGRprobeVlanRowStatus_Type = RowStatus
_HpnicfMGRprobeVlanRowStatus_Object = MibTableColumn
hpnicfMGRprobeVlanRowStatus = _HpnicfMGRprobeVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 5, 1, 1, 2),
    _HpnicfMGRprobeVlanRowStatus_Type()
)
hpnicfMGRprobeVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGRprobeVlanRowStatus.setStatus("current")
_HpnicfMGEgressIfObjects_ObjectIdentity = ObjectIdentity
hpnicfMGEgressIfObjects = _HpnicfMGEgressIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 6)
)
_HpnicfMGEgressIfTable_Object = MibTable
hpnicfMGEgressIfTable = _HpnicfMGEgressIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpnicfMGEgressIfTable.setStatus("current")
_HpnicfMGEgressIfEntry_Object = MibTableRow
hpnicfMGEgressIfEntry = _HpnicfMGEgressIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 6, 1, 1)
)
hpnicfMGEgressIfEntry.setIndexNames(
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGID"),
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGEgressIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMGEgressIfEntry.setStatus("current")


class _HpnicfMGEgressIfIndex_Type(Integer32):
    """Custom type hpnicfMGEgressIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfMGEgressIfIndex_Type.__name__ = "Integer32"
_HpnicfMGEgressIfIndex_Object = MibTableColumn
hpnicfMGEgressIfIndex = _HpnicfMGEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 6, 1, 1, 1),
    _HpnicfMGEgressIfIndex_Type()
)
hpnicfMGEgressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMGEgressIfIndex.setStatus("current")
_HpnicfMGEgressRowStatus_Type = RowStatus
_HpnicfMGEgressRowStatus_Object = MibTableColumn
hpnicfMGEgressRowStatus = _HpnicfMGEgressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 6, 1, 1, 2),
    _HpnicfMGEgressRowStatus_Type()
)
hpnicfMGEgressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGEgressRowStatus.setStatus("current")
_HpnicfMGMirrorVlanObjects_ObjectIdentity = ObjectIdentity
hpnicfMGMirrorVlanObjects = _HpnicfMGMirrorVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 7)
)
_HpnicfMGMirrorVlanTable_Object = MibTable
hpnicfMGMirrorVlanTable = _HpnicfMGMirrorVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpnicfMGMirrorVlanTable.setStatus("current")
_HpnicfMGMirrorVlanEntry_Object = MibTableRow
hpnicfMGMirrorVlanEntry = _HpnicfMGMirrorVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 7, 1, 1)
)
hpnicfMGMirrorVlanEntry.setIndexNames(
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGID"),
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGMirrorVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfMGMirrorVlanEntry.setStatus("current")


class _HpnicfMGMirrorVlanID_Type(Integer32):
    """Custom type hpnicfMGMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfMGMirrorVlanID_Type.__name__ = "Integer32"
_HpnicfMGMirrorVlanID_Object = MibTableColumn
hpnicfMGMirrorVlanID = _HpnicfMGMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 7, 1, 1, 1),
    _HpnicfMGMirrorVlanID_Type()
)
hpnicfMGMirrorVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMGMirrorVlanID.setStatus("current")


class _HpnicfMGMirrorVlanDirection_Type(Integer32):
    """Custom type hpnicfMGMirrorVlanDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_HpnicfMGMirrorVlanDirection_Type.__name__ = "Integer32"
_HpnicfMGMirrorVlanDirection_Object = MibTableColumn
hpnicfMGMirrorVlanDirection = _HpnicfMGMirrorVlanDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 7, 1, 1, 2),
    _HpnicfMGMirrorVlanDirection_Type()
)
hpnicfMGMirrorVlanDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGMirrorVlanDirection.setStatus("current")
_HpnicfMGMirrorVlanRowStatus_Type = RowStatus
_HpnicfMGMirrorVlanRowStatus_Object = MibTableColumn
hpnicfMGMirrorVlanRowStatus = _HpnicfMGMirrorVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 7, 1, 1, 3),
    _HpnicfMGMirrorVlanRowStatus_Type()
)
hpnicfMGMirrorVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGMirrorVlanRowStatus.setStatus("current")
_HpnicfMGMirrorCpuObjects_ObjectIdentity = ObjectIdentity
hpnicfMGMirrorCpuObjects = _HpnicfMGMirrorCpuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 8)
)
_HpnicfMGMirrorCpuTable_Object = MibTable
hpnicfMGMirrorCpuTable = _HpnicfMGMirrorCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hpnicfMGMirrorCpuTable.setStatus("current")
_HpnicfMGMirrorCpuEntry_Object = MibTableRow
hpnicfMGMirrorCpuEntry = _HpnicfMGMirrorCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 8, 1, 1)
)
hpnicfMGMirrorCpuEntry.setIndexNames(
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGID"),
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGMirrorCpuChassis"),
    (0, "HPN-ICF-MIRRORGROUP-MIB", "hpnicfMGMirrorCpuSlot"),
)
if mibBuilder.loadTexts:
    hpnicfMGMirrorCpuEntry.setStatus("current")
_HpnicfMGMirrorCpuChassis_Type = Unsigned32
_HpnicfMGMirrorCpuChassis_Object = MibTableColumn
hpnicfMGMirrorCpuChassis = _HpnicfMGMirrorCpuChassis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 8, 1, 1, 1),
    _HpnicfMGMirrorCpuChassis_Type()
)
hpnicfMGMirrorCpuChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMGMirrorCpuChassis.setStatus("current")
_HpnicfMGMirrorCpuSlot_Type = Unsigned32
_HpnicfMGMirrorCpuSlot_Object = MibTableColumn
hpnicfMGMirrorCpuSlot = _HpnicfMGMirrorCpuSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 8, 1, 1, 2),
    _HpnicfMGMirrorCpuSlot_Type()
)
hpnicfMGMirrorCpuSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMGMirrorCpuSlot.setStatus("current")


class _HpnicfMGMirrorCpuDirection_Type(Integer32):
    """Custom type hpnicfMGMirrorCpuDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_HpnicfMGMirrorCpuDirection_Type.__name__ = "Integer32"
_HpnicfMGMirrorCpuDirection_Object = MibTableColumn
hpnicfMGMirrorCpuDirection = _HpnicfMGMirrorCpuDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 8, 1, 1, 3),
    _HpnicfMGMirrorCpuDirection_Type()
)
hpnicfMGMirrorCpuDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGMirrorCpuDirection.setStatus("current")
_HpnicfMGMirrorCpuRowStatus_Type = RowStatus
_HpnicfMGMirrorCpuRowStatus_Object = MibTableColumn
hpnicfMGMirrorCpuRowStatus = _HpnicfMGMirrorCpuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 68, 1, 8, 1, 1, 4),
    _HpnicfMGMirrorCpuRowStatus_Type()
)
hpnicfMGMirrorCpuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMGMirrorCpuRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MIRRORGROUP-MIB",
    **{"hpnicfMirrGroup": hpnicfMirrGroup,
       "hpnicfMGInfoObjects": hpnicfMGInfoObjects,
       "hpnicfMGObjects": hpnicfMGObjects,
       "hpnicfMGTable": hpnicfMGTable,
       "hpnicfMGEntry": hpnicfMGEntry,
       "hpnicfMGID": hpnicfMGID,
       "hpnicfMGType": hpnicfMGType,
       "hpnicfMGStatus": hpnicfMGStatus,
       "hpnicfMGRowStatus": hpnicfMGRowStatus,
       "hpnicfMGMirrorIfObjects": hpnicfMGMirrorIfObjects,
       "hpnicfMGMirrorIfTable": hpnicfMGMirrorIfTable,
       "hpnicfMGMirrorIfEntry": hpnicfMGMirrorIfEntry,
       "hpnicfMGMirrorIfIndex": hpnicfMGMirrorIfIndex,
       "hpnicfMGMirrorDirection": hpnicfMGMirrorDirection,
       "hpnicfMGMirrorRowStatus": hpnicfMGMirrorRowStatus,
       "hpnicfMGMonitorIfObjects": hpnicfMGMonitorIfObjects,
       "hpnicfMGMonitorIfTable": hpnicfMGMonitorIfTable,
       "hpnicfMGMonitorIfEntry": hpnicfMGMonitorIfEntry,
       "hpnicfMGMonitorIfIndex": hpnicfMGMonitorIfIndex,
       "hpnicfMGMonitorRowStatus": hpnicfMGMonitorRowStatus,
       "hpnicfMGReflectorIfObjects": hpnicfMGReflectorIfObjects,
       "hpnicfMGReflectorIfTable": hpnicfMGReflectorIfTable,
       "hpnicfMGReflectorIfEntry": hpnicfMGReflectorIfEntry,
       "hpnicfMGReflectorIfIndex": hpnicfMGReflectorIfIndex,
       "hpnicfMGReflectorRowStatus": hpnicfMGReflectorRowStatus,
       "hpnicfMGRprobeVlanObjects": hpnicfMGRprobeVlanObjects,
       "hpnicfMGRprobeVlanTable": hpnicfMGRprobeVlanTable,
       "hpnicfMGRprobeVlanEntry": hpnicfMGRprobeVlanEntry,
       "hpnicfMGRprobeVlanID": hpnicfMGRprobeVlanID,
       "hpnicfMGRprobeVlanRowStatus": hpnicfMGRprobeVlanRowStatus,
       "hpnicfMGEgressIfObjects": hpnicfMGEgressIfObjects,
       "hpnicfMGEgressIfTable": hpnicfMGEgressIfTable,
       "hpnicfMGEgressIfEntry": hpnicfMGEgressIfEntry,
       "hpnicfMGEgressIfIndex": hpnicfMGEgressIfIndex,
       "hpnicfMGEgressRowStatus": hpnicfMGEgressRowStatus,
       "hpnicfMGMirrorVlanObjects": hpnicfMGMirrorVlanObjects,
       "hpnicfMGMirrorVlanTable": hpnicfMGMirrorVlanTable,
       "hpnicfMGMirrorVlanEntry": hpnicfMGMirrorVlanEntry,
       "hpnicfMGMirrorVlanID": hpnicfMGMirrorVlanID,
       "hpnicfMGMirrorVlanDirection": hpnicfMGMirrorVlanDirection,
       "hpnicfMGMirrorVlanRowStatus": hpnicfMGMirrorVlanRowStatus,
       "hpnicfMGMirrorCpuObjects": hpnicfMGMirrorCpuObjects,
       "hpnicfMGMirrorCpuTable": hpnicfMGMirrorCpuTable,
       "hpnicfMGMirrorCpuEntry": hpnicfMGMirrorCpuEntry,
       "hpnicfMGMirrorCpuChassis": hpnicfMGMirrorCpuChassis,
       "hpnicfMGMirrorCpuSlot": hpnicfMGMirrorCpuSlot,
       "hpnicfMGMirrorCpuDirection": hpnicfMGMirrorCpuDirection,
       "hpnicfMGMirrorCpuRowStatus": hpnicfMGMirrorCpuRowStatus}
)
