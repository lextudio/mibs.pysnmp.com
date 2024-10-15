# SNMP MIB module (EXTREME-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(extremeVlanIfIndex,) = mibBuilder.importSymbols(
    "EXTREME-VLAN-MIB",
    "extremeVlanIfIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeQos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeQosCommon_ObjectIdentity = ObjectIdentity
extremeQosCommon = _ExtremeQosCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1)
)


class _ExtremeUnitPaceMode_Type(Integer32):
    """Custom type extremeUnitPaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lowLatency", 3),
          ("normalEthernet", 2),
          ("notApplicable", 1))
    )


_ExtremeUnitPaceMode_Type.__name__ = "Integer32"
_ExtremeUnitPaceMode_Object = MibScalar
extremeUnitPaceMode = _ExtremeUnitPaceMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 1),
    _ExtremeUnitPaceMode_Type()
)
extremeUnitPaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeUnitPaceMode.setStatus("deprecated")


class _ExtremeQosMode_Type(Integer32):
    """Custom type extremeQosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_ExtremeQosMode_Type.__name__ = "Integer32"
_ExtremeQosMode_Object = MibScalar
extremeQosMode = _ExtremeQosMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 4),
    _ExtremeQosMode_Type()
)
extremeQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeQosMode.setStatus("deprecated")
_ExtremeQosUnconfigure_Type = TruthValue
_ExtremeQosUnconfigure_Object = MibScalar
extremeQosUnconfigure = _ExtremeQosUnconfigure_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 5),
    _ExtremeQosUnconfigure_Type()
)
extremeQosUnconfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeQosUnconfigure.setStatus("deprecated")
_ExtremeQosProfileTable_Object = MibTable
extremeQosProfileTable = _ExtremeQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    extremeQosProfileTable.setStatus("current")
_ExtremeQosProfileEntry_Object = MibTableRow
extremeQosProfileEntry = _ExtremeQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 6, 1)
)
extremeQosProfileEntry.setIndexNames(
    (0, "EXTREME-QOS-MIB", "extremeQosProfileIndex"),
)
if mibBuilder.loadTexts:
    extremeQosProfileEntry.setStatus("current")


class _ExtremeQosProfileIndex_Type(Integer32):
    """Custom type extremeQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeQosProfileIndex_Type.__name__ = "Integer32"
_ExtremeQosProfileIndex_Object = MibTableColumn
extremeQosProfileIndex = _ExtremeQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 6, 1, 1),
    _ExtremeQosProfileIndex_Type()
)
extremeQosProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosProfileIndex.setStatus("current")


class _ExtremeQosProfileName_Type(DisplayString):
    """Custom type extremeQosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ExtremeQosProfileName_Type.__name__ = "DisplayString"
_ExtremeQosProfileName_Object = MibTableColumn
extremeQosProfileName = _ExtremeQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 6, 1, 2),
    _ExtremeQosProfileName_Type()
)
extremeQosProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosProfileName.setStatus("current")


class _ExtremeQosProfileMinBw_Type(Integer32):
    """Custom type extremeQosProfileMinBw based on Integer32"""
    defaultValue = 0


_ExtremeQosProfileMinBw_Object = MibTableColumn
extremeQosProfileMinBw = _ExtremeQosProfileMinBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 6, 1, 3),
    _ExtremeQosProfileMinBw_Type()
)
extremeQosProfileMinBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosProfileMinBw.setStatus("current")


class _ExtremeQosProfileMaxBw_Type(Integer32):
    """Custom type extremeQosProfileMaxBw based on Integer32"""
    defaultValue = 100


_ExtremeQosProfileMaxBw_Object = MibTableColumn
extremeQosProfileMaxBw = _ExtremeQosProfileMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 6, 1, 4),
    _ExtremeQosProfileMaxBw_Type()
)
extremeQosProfileMaxBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosProfileMaxBw.setStatus("current")


class _ExtremeQosProfilePriority_Type(Integer32):
    """Custom type extremeQosProfilePriority based on Integer32"""
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
        *(("high", 7),
          ("highHi", 8),
          ("low", 1),
          ("lowHi", 2),
          ("medium", 5),
          ("mediumHi", 6),
          ("normal", 3),
          ("normalHi", 4))
    )


_ExtremeQosProfilePriority_Type.__name__ = "Integer32"
_ExtremeQosProfilePriority_Object = MibTableColumn
extremeQosProfilePriority = _ExtremeQosProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 6, 1, 5),
    _ExtremeQosProfilePriority_Type()
)
extremeQosProfilePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosProfilePriority.setStatus("current")
_ExtremeQosProfileRowStatus_Type = RowStatus
_ExtremeQosProfileRowStatus_Object = MibTableColumn
extremeQosProfileRowStatus = _ExtremeQosProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 6, 1, 6),
    _ExtremeQosProfileRowStatus_Type()
)
extremeQosProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosProfileRowStatus.setStatus("current")
_ExtremeQosByVlanMappingTable_Object = MibTable
extremeQosByVlanMappingTable = _ExtremeQosByVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    extremeQosByVlanMappingTable.setStatus("current")
_ExtremeQosByVlanMappingEntry_Object = MibTableRow
extremeQosByVlanMappingEntry = _ExtremeQosByVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 7, 1)
)
extremeQosByVlanMappingEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeQosByVlanMappingEntry.setStatus("current")


class _ExtremeQosByVlanMappingQosProfileIndex_Type(Integer32):
    """Custom type extremeQosByVlanMappingQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeQosByVlanMappingQosProfileIndex_Type.__name__ = "Integer32"
_ExtremeQosByVlanMappingQosProfileIndex_Object = MibTableColumn
extremeQosByVlanMappingQosProfileIndex = _ExtremeQosByVlanMappingQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 7, 1, 1),
    _ExtremeQosByVlanMappingQosProfileIndex_Type()
)
extremeQosByVlanMappingQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeQosByVlanMappingQosProfileIndex.setStatus("current")
_ExtremePerPortQosTable_Object = MibTable
extremePerPortQosTable = _ExtremePerPortQosTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    extremePerPortQosTable.setStatus("current")
_ExtremePerPortQosEntry_Object = MibTableRow
extremePerPortQosEntry = _ExtremePerPortQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 8, 1)
)
extremePerPortQosEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-QOS-MIB", "extremePerPortQosIndex"),
)
if mibBuilder.loadTexts:
    extremePerPortQosEntry.setStatus("current")


class _ExtremePerPortQosIndex_Type(Integer32):
    """Custom type extremePerPortQosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremePerPortQosIndex_Type.__name__ = "Integer32"
_ExtremePerPortQosIndex_Object = MibTableColumn
extremePerPortQosIndex = _ExtremePerPortQosIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 8, 1, 1),
    _ExtremePerPortQosIndex_Type()
)
extremePerPortQosIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePerPortQosIndex.setStatus("current")


class _ExtremePerPortQosMinBw_Type(Integer32):
    """Custom type extremePerPortQosMinBw based on Integer32"""
    defaultValue = 0


_ExtremePerPortQosMinBw_Object = MibTableColumn
extremePerPortQosMinBw = _ExtremePerPortQosMinBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 8, 1, 2),
    _ExtremePerPortQosMinBw_Type()
)
extremePerPortQosMinBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePerPortQosMinBw.setStatus("current")


class _ExtremePerPortQosMaxBw_Type(Integer32):
    """Custom type extremePerPortQosMaxBw based on Integer32"""
    defaultValue = 100


_ExtremePerPortQosMaxBw_Object = MibTableColumn
extremePerPortQosMaxBw = _ExtremePerPortQosMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 8, 1, 3),
    _ExtremePerPortQosMaxBw_Type()
)
extremePerPortQosMaxBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePerPortQosMaxBw.setStatus("current")


class _ExtremePerPortQosPriority_Type(Integer32):
    """Custom type extremePerPortQosPriority based on Integer32"""
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
        *(("high", 7),
          ("highHi", 8),
          ("low", 1),
          ("lowHi", 2),
          ("medium", 5),
          ("mediumHi", 6),
          ("normal", 3),
          ("normalHi", 4))
    )


_ExtremePerPortQosPriority_Type.__name__ = "Integer32"
_ExtremePerPortQosPriority_Object = MibTableColumn
extremePerPortQosPriority = _ExtremePerPortQosPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 8, 1, 4),
    _ExtremePerPortQosPriority_Type()
)
extremePerPortQosPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePerPortQosPriority.setStatus("current")
_ExtremePerPortQosRowStatus_Type = RowStatus
_ExtremePerPortQosRowStatus_Object = MibTableColumn
extremePerPortQosRowStatus = _ExtremePerPortQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 8, 1, 5),
    _ExtremePerPortQosRowStatus_Type()
)
extremePerPortQosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePerPortQosRowStatus.setStatus("current")
_ExtremeQosIngressPriorityTable_Object = MibTable
extremeQosIngressPriorityTable = _ExtremeQosIngressPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 9)
)
if mibBuilder.loadTexts:
    extremeQosIngressPriorityTable.setStatus("current")
_ExtremeQosIngressPriorityEntry_Object = MibTableRow
extremeQosIngressPriorityEntry = _ExtremeQosIngressPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 9, 1)
)
extremeQosIngressPriorityEntry.setIndexNames(
    (0, "EXTREME-QOS-MIB", "extremeQosIngressPriorityIndex"),
)
if mibBuilder.loadTexts:
    extremeQosIngressPriorityEntry.setStatus("current")


class _ExtremeQosIngressPriorityIndex_Type(Integer32):
    """Custom type extremeQosIngressPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeQosIngressPriorityIndex_Type.__name__ = "Integer32"
_ExtremeQosIngressPriorityIndex_Object = MibTableColumn
extremeQosIngressPriorityIndex = _ExtremeQosIngressPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 9, 1, 1),
    _ExtremeQosIngressPriorityIndex_Type()
)
extremeQosIngressPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeQosIngressPriorityIndex.setStatus("current")


class _ExtremeQosIngressPriorityName_Type(DisplayString):
    """Custom type extremeQosIngressPriorityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ExtremeQosIngressPriorityName_Type.__name__ = "DisplayString"
_ExtremeQosIngressPriorityName_Object = MibTableColumn
extremeQosIngressPriorityName = _ExtremeQosIngressPriorityName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 9, 1, 2),
    _ExtremeQosIngressPriorityName_Type()
)
extremeQosIngressPriorityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeQosIngressPriorityName.setStatus("current")


class _ExtremeQosIngressPriorityValue_Type(Integer32):
    """Custom type extremeQosIngressPriorityValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ExtremeQosIngressPriorityValue_Type.__name__ = "Integer32"
_ExtremeQosIngressPriorityValue_Object = MibTableColumn
extremeQosIngressPriorityValue = _ExtremeQosIngressPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 9, 1, 3),
    _ExtremeQosIngressPriorityValue_Type()
)
extremeQosIngressPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeQosIngressPriorityValue.setStatus("current")
_ExtremeIQosProfileTable_Object = MibTable
extremeIQosProfileTable = _ExtremeIQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    extremeIQosProfileTable.setStatus("current")
_ExtremeIQosProfileEntry_Object = MibTableRow
extremeIQosProfileEntry = _ExtremeIQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 10, 1)
)
extremeIQosProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-QOS-MIB", "extremeIQosProfileIndex"),
)
if mibBuilder.loadTexts:
    extremeIQosProfileEntry.setStatus("current")


class _ExtremeIQosProfileIndex_Type(Integer32):
    """Custom type extremeIQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeIQosProfileIndex_Type.__name__ = "Integer32"
_ExtremeIQosProfileIndex_Object = MibTableColumn
extremeIQosProfileIndex = _ExtremeIQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 10, 1, 1),
    _ExtremeIQosProfileIndex_Type()
)
extremeIQosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeIQosProfileIndex.setStatus("current")


class _ExtremeIQosProfileName_Type(DisplayString):
    """Custom type extremeIQosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ExtremeIQosProfileName_Type.__name__ = "DisplayString"
_ExtremeIQosProfileName_Object = MibTableColumn
extremeIQosProfileName = _ExtremeIQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 10, 1, 2),
    _ExtremeIQosProfileName_Type()
)
extremeIQosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeIQosProfileName.setStatus("current")


class _ExtremeIQosProfileMinBwType_Type(Integer32):
    """Custom type extremeIQosProfileMinBwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("mbps", 3),
          ("percentage", 1))
    )


_ExtremeIQosProfileMinBwType_Type.__name__ = "Integer32"
_ExtremeIQosProfileMinBwType_Object = MibTableColumn
extremeIQosProfileMinBwType = _ExtremeIQosProfileMinBwType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 10, 1, 3),
    _ExtremeIQosProfileMinBwType_Type()
)
extremeIQosProfileMinBwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeIQosProfileMinBwType.setStatus("current")


class _ExtremeIQosProfileMinBw_Type(Integer32):
    """Custom type extremeIQosProfileMinBw based on Integer32"""
    defaultValue = 0


_ExtremeIQosProfileMinBw_Object = MibTableColumn
extremeIQosProfileMinBw = _ExtremeIQosProfileMinBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 10, 1, 4),
    _ExtremeIQosProfileMinBw_Type()
)
extremeIQosProfileMinBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeIQosProfileMinBw.setStatus("current")


class _ExtremeIQosProfileMaxBwType_Type(Integer32):
    """Custom type extremeIQosProfileMaxBwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("mbps", 3),
          ("percentage", 1))
    )


_ExtremeIQosProfileMaxBwType_Type.__name__ = "Integer32"
_ExtremeIQosProfileMaxBwType_Object = MibTableColumn
extremeIQosProfileMaxBwType = _ExtremeIQosProfileMaxBwType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 10, 1, 5),
    _ExtremeIQosProfileMaxBwType_Type()
)
extremeIQosProfileMaxBwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeIQosProfileMaxBwType.setStatus("current")


class _ExtremeIQosProfileMaxBw_Type(Integer32):
    """Custom type extremeIQosProfileMaxBw based on Integer32"""
    defaultValue = 0


_ExtremeIQosProfileMaxBw_Object = MibTableColumn
extremeIQosProfileMaxBw = _ExtremeIQosProfileMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 10, 1, 6),
    _ExtremeIQosProfileMaxBw_Type()
)
extremeIQosProfileMaxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeIQosProfileMaxBw.setStatus("current")
_ExtremeIQosProfileRED_Type = Integer32
_ExtremeIQosProfileRED_Object = MibTableColumn
extremeIQosProfileRED = _ExtremeIQosProfileRED_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 10, 1, 7),
    _ExtremeIQosProfileRED_Type()
)
extremeIQosProfileRED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeIQosProfileRED.setStatus("current")
_ExtremeIQosProfileMaxBuf_Type = Integer32
_ExtremeIQosProfileMaxBuf_Object = MibTableColumn
extremeIQosProfileMaxBuf = _ExtremeIQosProfileMaxBuf_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 10, 1, 8),
    _ExtremeIQosProfileMaxBuf_Type()
)
extremeIQosProfileMaxBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeIQosProfileMaxBuf.setStatus("current")
_ExtremeIQosByVlanMappingTable_Object = MibTable
extremeIQosByVlanMappingTable = _ExtremeIQosByVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 11)
)
if mibBuilder.loadTexts:
    extremeIQosByVlanMappingTable.setStatus("current")
_ExtremeIQosByVlanMappingEntry_Object = MibTableRow
extremeIQosByVlanMappingEntry = _ExtremeIQosByVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 11, 1)
)
extremeIQosByVlanMappingEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeIQosByVlanMappingEntry.setStatus("current")


class _ExtremeIQosByVlanMappingIQosProfileIndex_Type(Integer32):
    """Custom type extremeIQosByVlanMappingIQosProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeIQosByVlanMappingIQosProfileIndex_Type.__name__ = "Integer32"
_ExtremeIQosByVlanMappingIQosProfileIndex_Object = MibTableColumn
extremeIQosByVlanMappingIQosProfileIndex = _ExtremeIQosByVlanMappingIQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 3, 1, 11, 1, 1),
    _ExtremeIQosByVlanMappingIQosProfileIndex_Type()
)
extremeIQosByVlanMappingIQosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeIQosByVlanMappingIQosProfileIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-QOS-MIB",
    **{"extremeQos": extremeQos,
       "extremeQosCommon": extremeQosCommon,
       "extremeUnitPaceMode": extremeUnitPaceMode,
       "extremeQosMode": extremeQosMode,
       "extremeQosUnconfigure": extremeQosUnconfigure,
       "extremeQosProfileTable": extremeQosProfileTable,
       "extremeQosProfileEntry": extremeQosProfileEntry,
       "extremeQosProfileIndex": extremeQosProfileIndex,
       "extremeQosProfileName": extremeQosProfileName,
       "extremeQosProfileMinBw": extremeQosProfileMinBw,
       "extremeQosProfileMaxBw": extremeQosProfileMaxBw,
       "extremeQosProfilePriority": extremeQosProfilePriority,
       "extremeQosProfileRowStatus": extremeQosProfileRowStatus,
       "extremeQosByVlanMappingTable": extremeQosByVlanMappingTable,
       "extremeQosByVlanMappingEntry": extremeQosByVlanMappingEntry,
       "extremeQosByVlanMappingQosProfileIndex": extremeQosByVlanMappingQosProfileIndex,
       "extremePerPortQosTable": extremePerPortQosTable,
       "extremePerPortQosEntry": extremePerPortQosEntry,
       "extremePerPortQosIndex": extremePerPortQosIndex,
       "extremePerPortQosMinBw": extremePerPortQosMinBw,
       "extremePerPortQosMaxBw": extremePerPortQosMaxBw,
       "extremePerPortQosPriority": extremePerPortQosPriority,
       "extremePerPortQosRowStatus": extremePerPortQosRowStatus,
       "extremeQosIngressPriorityTable": extremeQosIngressPriorityTable,
       "extremeQosIngressPriorityEntry": extremeQosIngressPriorityEntry,
       "extremeQosIngressPriorityIndex": extremeQosIngressPriorityIndex,
       "extremeQosIngressPriorityName": extremeQosIngressPriorityName,
       "extremeQosIngressPriorityValue": extremeQosIngressPriorityValue,
       "extremeIQosProfileTable": extremeIQosProfileTable,
       "extremeIQosProfileEntry": extremeIQosProfileEntry,
       "extremeIQosProfileIndex": extremeIQosProfileIndex,
       "extremeIQosProfileName": extremeIQosProfileName,
       "extremeIQosProfileMinBwType": extremeIQosProfileMinBwType,
       "extremeIQosProfileMinBw": extremeIQosProfileMinBw,
       "extremeIQosProfileMaxBwType": extremeIQosProfileMaxBwType,
       "extremeIQosProfileMaxBw": extremeIQosProfileMaxBw,
       "extremeIQosProfileRED": extremeIQosProfileRED,
       "extremeIQosProfileMaxBuf": extremeIQosProfileMaxBuf,
       "extremeIQosByVlanMappingTable": extremeIQosByVlanMappingTable,
       "extremeIQosByVlanMappingEntry": extremeIQosByVlanMappingEntry,
       "extremeIQosByVlanMappingIQosProfileIndex": extremeIQosByVlanMappingIQosProfileIndex}
)
